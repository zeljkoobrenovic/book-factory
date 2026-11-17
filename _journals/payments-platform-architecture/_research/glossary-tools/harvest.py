"""Harvest glossary candidates from SETTLED as written.

    python3 harvest.py            # everything
    python3 harvest.py owns       # PLAN.md "Owns" lists, each term checked against rows.py and crosswalk.py
    python3 harvest.py bold       # every sentence that introduces a bolded term, per chapter
    python3 harvest.py acronyms   # acronyms with the words around their first expansion

Standard library only. Read the output next to rows.py: a term a chapter bolds or owns and the glossary lacks
is a row to write (open the chapter; do not define from memory).
"""
import os, re, sys, collections
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
mode = sys.argv[1] if len(sys.argv) > 1 else 'all'
posts = re.findall(r'- (\S+)/index\.md', open(os.path.join(ROOT, 'config.yaml')).read())


def body_of(folder):
    f = os.path.join(ROOT, 'posts', folder, 'index.md')
    if not os.path.exists(f) or folder == 'glossary':
        return None
    t = open(f).read().split('## Sources and Evidence')[0].split('\n---', 1)[1]
    return re.sub(r'<!-- illustration-placeholder.*?-->', '', t, flags=re.S)


if mode in ('all', 'owns'):
    from rows import S, AX
    from crosswalk import X
    labels = []
    for sec in S + [AX]:
        for r in sec[3]:
            labels += [r[0]] + list(r[3])
    for sec in X:
        for r in sec[3]:
            labels += [r[0], r[1], r[2]] + list(r[6])
    hay = ' ; '.join(labels).lower()
    plan = open(os.path.join(ROOT, 'PLAN.md')).read()
    print('===== PLAN.md "Owns" terms (MISSING = no glossary label contains the term)')
    for m in re.finditer(r'\*\*(\d\d-[a-z0-9-]+) → `([a-z0-9-]+)`\*\*.*?Owns: ([^.]*)\.', plan):
        for term in [x.strip() for x in m.group(3).split(',')]:
            t = re.sub(r'^the ', '', term.lower())
            ok = t in hay or t.rstrip('s') in hay or all(w.rstrip('s') in hay for w in re.split(r'[ /]+| and ', t) if len(w) > 3)
            print('  %-36s %-34s %s' % (m.group(2), term, '' if ok else 'MISSING'))

if mode in ('all', 'bold'):
    skip = re.compile(r'^(Established|Depends on context|The author|Where we are|Figure|\(Evidence age|INFERENCE)')
    for p in posts:
        body = body_of(p)
        if body is None:
            continue
        out, seen = [], set()
        for para in body.split('\n'):
            if para.startswith(('>', '#', '**Figure')):
                continue
            for s in re.split(r'(?<=[.!?])\s+(?=[A-Z*(])', para):
                bs = [b for b in re.findall(r'\*\*([^*]{2,70})\*\*', s)
                      if not skip.match(b) and not b.rstrip().endswith(('.', ':')) and b.lower() not in seen]
                if bs:
                    seen.update(b.lower() for b in bs)
                    out.append(s.strip()[:330])
        print('=====', p, len(out))
        for o in out:
            print('  ', o)

if mode in ('all', 'acronyms'):
    ac = collections.OrderedDict()
    for p in posts:
        body = body_of(p)
        if body is None:
            continue
        for m in re.finditer(r'((?:[A-Za-z0-9\-’\']+\s){1,7})\(([A-Z][A-Za-z0-9\-]{1,8}s?)\)', body):
            a = m.group(2)
            if sum(c.isupper() for c in a) >= 2:
                ac.setdefault(a, (m.group(1).strip()[-60:], p))
        for m in re.finditer(r'\b([A-Z][A-Z0-9]{1,7}s?)\s\(([a-z][^)]{4,70})\)', body):
            ac.setdefault(m.group(1), ('<- ' + m.group(2), p))
    print('===== acronyms')
    for a, (e, p) in sorted(ac.items()):
        print('  %-8s %-64s %s' % (a, e, p))
