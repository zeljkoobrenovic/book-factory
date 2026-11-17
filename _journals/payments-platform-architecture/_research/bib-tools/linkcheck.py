# Link check for the bibliography: requests every distinct URL the chapters cite once (HEAD, then GET when
# HEAD fails or to read the final URL and the page title), at most 5 in parallel, with a delay per host.
# Usage:  python3 linkcheck.py            check URLs not yet in link-check.json, then write link-check.md
#         python3 linkcheck.py --all      re-check everything
#         python3 linkcheck.py --failed   re-check only the URLs that did not return 200
# Runs gen.py itself when srcs2.json is missing (run.sh removes it). Results are cached in link-check.json;
# hand-written decisions for failures and redirects live in link-check-notes.json and are merged into the report.
# Standard library only. The User-Agent is generic; no personal identifier is sent. SEC EDGAR asks automated
# clients for a contact string and gets the placeholder "research-bot admin@example.com".
import json, os, re, sys, time, threading, html, ssl
import urllib.request, urllib.error
from urllib.parse import urlparse, quote, urlsplit, urlunsplit
from concurrent.futures import ThreadPoolExecutor
HERE = os.path.dirname(os.path.abspath(__file__))
UA = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
SEC_UA = 'research-bot admin@example.com'
DELAY = 0.6  # seconds between two requests to one host
CACHE = os.path.join(HERE, 'link-check.json')
locks = {}; last = {}; glock = threading.Lock()

def wait(host):
    with glock: lk = locks.setdefault(host, threading.Lock())
    with lk:
        d = DELAY - (time.time() - last.get(host, 0))
        if d > 0: time.sleep(d)
        last[host] = time.time()

def safe(u):  # percent-encode characters urllib refuses, keep existing escapes
    p = urlsplit(u)
    return urlunsplit((p.scheme, p.netloc, quote(p.path, safe="/%:@()+,;=~!*'$&"), quote(p.query, safe="=&%:/()+,;~!*'$?"), ''))

def fetch(u, method):
    host = urlparse(u).netloc.lower()
    wait(host)
    req = urllib.request.Request(safe(u), method=method, headers={
        'User-Agent': SEC_UA if host.endswith('sec.gov') else UA,
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8', 'Accept-Language': 'en-US,en;q=0.9'})
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            body = r.read(200000) if method == 'GET' else b''
            return r.status, r.geturl(), body, r.headers.get('Content-Type', '')
    except urllib.error.HTTPError as e:
        return e.code, e.geturl() if hasattr(e, 'geturl') else u, b'', ''
    except Exception as e:
        return 0, u, str(e)[:120].encode(), ''

def check(u):
    st, final, body, ct = fetch(u, 'HEAD')
    head = st
    st, final, body, ct = fetch(u, 'GET')  # GET always: the final URL and the page title are part of the audit
    if st in (0, 429, 500, 502, 503, 504):
        time.sleep(6); st, final, body, ct = fetch(u, 'GET')
    title = ''
    if st == 200 and 'html' in ct:
        m = re.search(rb'<title[^>]*>(.*?)</title>', body, re.S | re.I)
        if m: title = html.unescape(re.sub(r'\s+', ' ', m.group(1).decode('utf-8', 'replace'))).strip()[:200]
    err = body.decode('utf-8', 'replace') if st == 0 else ''
    return dict(url=u, head=head, status=st, final=final, title=title, error=err, checked=time.strftime('%Y-%m-%d'))

def main():
    made = not os.path.exists(os.path.join(HERE, 'srcs2.json'))
    if made:
        import subprocess; subprocess.run([sys.executable, os.path.join(HERE, 'gen.py')], check=True)
    D = json.load(open(os.path.join(HERE, 'srcs2.json')))
    if made: os.remove(os.path.join(HERE, 'srcs2.json'))
    urls = []
    for s in D['srcs']:
        for u in s.get('urls', []) + [x[1] for x in s.get('extra', [])]:
            if u not in urls: urls.append(u)
    cache = json.load(open(CACHE)) if os.path.exists(CACHE) else {}
    if '--all' in sys.argv: todo = urls
    elif '--failed' in sys.argv: todo = [u for u in urls if cache.get(u, {}).get('status') != 200]
    else: todo = [u for u in urls if u not in cache]
    print(len(urls), 'distinct URLs;', len(todo), 'to check')
    with ThreadPoolExecutor(max_workers=5) as ex:
        for i, r in enumerate(ex.map(check, todo)):
            cache[r['url']] = r
            if r['status'] != 200: print(r['status'], r['url'], r['error'], flush=True)
            if i % 50 == 49: json.dump(cache, open(CACHE, 'w'), indent=1, ensure_ascii=False)
    json.dump(cache, open(CACHE, 'w'), indent=1, ensure_ascii=False)
    report(urls, cache, D)

def same(a, b):
    n = lambda u: re.sub(r'^https?://(www\.)?', '', u).rstrip('/').lower()
    return n(a) == n(b)

# Hosts that answer automated clients with 403 or 429 and serve the same page to a browser.
NOTES_FILE = os.path.join(HERE, 'link-check-notes.json')  # URL -> hand-written decision, kept across runs

def report(urls, cache, D):
    notes = json.load(open(NOTES_FILE)) if os.path.exists(NOTES_FILE) else {}
    cited = {}
    for s in D['srcs']:
        for pm, t, m, u in s.get('by', []):
            if u: cited.setdefault(u, [])
            if u and pm not in cited[u]: cited[u].append(pm)
    rows = [cache[u] for u in urls if u in cache]
    ok = [r for r in rows if r['status'] == 200 and same(r['url'], r['final'])]
    moved = [r for r in rows if r['status'] == 200 and not same(r['url'], r['final'])]
    bad = [r for r in rows if r['status'] != 200]
    out = ['# Link check: SETTLED bibliography', '',
           f'Generated by `linkcheck.py` on {time.strftime("%Y-%m-%d")}. Every distinct URL cited in a Sources and Evidence section was requested once (HEAD, then GET) with a generic browser User-Agent, at most 5 in parallel and {DELAY} s between requests to one host.', '',
           f'- URLs checked: **{len(rows)}**', f'- 200 at the cited URL: **{len(ok)}**',
           f'- 200 after a redirect to a different URL: **{len(moved)}**', f'- Not 200: **{len(bad)}**', '']
    out += ['## Not 200', '', '| Status | URL | Cited in | Decision |', '| --- | --- | --- | --- |']
    for r in bad:
        out.append(f"| {r['status'] or 'error'} | {r['url']} | {', '.join(cited.get(r['url'], []))} | {notes.get(r['url'], r['error'] or 'UNDECIDED')} |")
    out += ['', '## Redirected (200 at another URL)', '', '| URL | Final URL | Cited in | Decision |', '| --- | --- | --- | --- |']
    for r in moved:
        out.append(f"| {r['url']} | {r['final']} | {', '.join(cited.get(r['url'], []))} | {notes.get(r['url'], 'UNDECIDED')} |")
    out += ['', '## All URLs', '', '| Status | URL | Final URL (when different) | Page title |', '| --- | --- | --- | --- |']
    for r in rows:
        out.append(f"| {r['status'] or 'error'} | {r['url']} | {'' if same(r['url'], r['final']) else r['final']} | {r['title'].replace('|', '/')[:90]} |")
    open(os.path.join(HERE, 'link-check.md'), 'w').write('\n'.join(out) + '\n')
    print(f'{len(rows)} URLs: {len(ok)} ok, {len(moved)} redirected, {len(bad)} not 200 -> link-check.md')

if __name__ == '__main__':
    main()
