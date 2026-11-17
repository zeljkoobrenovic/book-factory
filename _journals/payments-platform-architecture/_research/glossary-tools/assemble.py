"""Assemble posts/glossary/index.md for SETTLED from rows.py, crosswalk.py, head.md, xhead.md and tail.md.

    python3 _journals/payments-platform-architecture/_research/glossary-tools/assemble.py \
        _journals/payments-platform-architecture/posts/glossary/index.md

Re-runnable: edit rows.py (definitions, Larkfield names) or crosswalk.py (provider vocabulary), run again, rebuild.
The script checks that every [[permalink]] used is a page of this book and that no cell breaks a table.
"""
import os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.normpath(os.path.join(HERE, '..', '..'))
sys.path.insert(0, HERE)
from rows import S, AX
from crosswalk import X, DOCS, NONE

OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'posts', 'glossary', 'index.md')

# permalink -> short label for the index (chapter number, or a short name for unnumbered pages)
yaml = open(os.path.join(ROOT, 'config.yaml')).read()
LABEL, PERMALINKS = {}, set()
for folder in re.findall(r'- (\S+)/index\.md', yaml):
    f = os.path.join(ROOT, 'posts', folder, 'index.md')
    if os.path.exists(f):
        pm = re.search(r'^permalink:\s*(\S+)', open(f).read(), re.M).group(1)
    else:
        pm = folder  # reference pages not written yet keep their folder name as permalink
    PERMALINKS.add(pm)
    m = re.match(r'(\d\d)-', folder)
    if m:
        LABEL[pm] = 'ch. %d' % int(m.group(1))
LABEL.update({'introduction': 'Introduction', 'how-payments-got-complicated': 'From Cash to Code',
              'where-payment-systems-go-wrong': 'Failure patterns', 'meet-larkfield': 'Meet Larkfield'})
for n in range(1, 11):
    LABEL['part-%d' % n] = 'Part %s' % ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X'][n - 1]


def links(chs):
    for c in chs:
        if c not in PERMALINKS:
            sys.exit('unknown permalink in a row: ' + c)
    return ', '.join('[[%s]]' % c for c in chs)


def cell(s, what):
    if '|' in s or '\n' in s:
        sys.exit('a cell contains | or a newline: %s: %s' % (what, s[:60]))
    return s


def plain(s):
    return s.replace('*', '').replace('`', '').strip()


index = []   # (label, anchor, owning chapter)
body = []
nrows = xrows = xdoc = lrows = 0


def term_table(anchor, rows):
    out = ['| Term | Definition | Chapter |', '| --- | --- | --- |']
    for term, d, chs, aliases in rows:
        out.append('| **%s** | %s | %s |' % (cell(term, term), cell(d, term), links(chs)))
        for label in [term] + list(aliases):
            index.append((label, anchor, chs[0]))
    return out


for anchor, title, intro, rows in S:
    body += ['## <a id="%s"></a>%s' % (anchor, title), '', intro, ''] + term_table(anchor, rows) + ['']
    nrows += len(rows)

body.append('__XHEAD__')
doc_keys = []
for anchor, title, intro, rows in X:
    body += ['## <a id="%s"></a>%s' % (anchor, title), '', intro, '',
             "| Concept | Stripe's term | Adyen's term | Note | Chapter |", '| --- | --- | --- | --- | --- |']
    for concept, stripe, adyen, note, chs, basis, idx in rows:
        last = links(chs)
        if basis != 'ch':
            xdoc += 1
            for k in basis:
                if k not in DOCS:
                    sys.exit('unknown DOCS key: ' + k)
                if k not in doc_keys:
                    doc_keys.append(k)
            last += '; documentation'
        body.append('| **%s** | %s | %s | %s | %s |' % (cell(concept, concept), cell(stripe, concept),
                                                      cell(adyen, concept), cell(note, concept), last))
        for label in idx:
            index.append((label, anchor, chs[0]))
        xrows += 1
    body.append('')

anchor, title, intro, rows = AX
body += ['## <a id="%s"></a>%s' % (anchor, title), '', intro, '',
         '| Name | What it is (fictional) | Chapter |', '| --- | --- | --- |']
for term, d, chs, aliases in rows:
    body.append('| **%s** | %s | %s |' % (cell(term, term), cell(d, term), links(chs)))
    for label in [term] + list(aliases):
        index.append((label, anchor, chs[0]))
    lrows += 1
body.append('')


# alphabetical index: term -> section of this page, then the owning chapter
def key(label):
    p = plain(label)
    p = re.sub(r'^(The|the|A|An)\s+', '', p)
    p = p.lstrip('“"§€/[ ')
    return p.lower()


seen, groups = set(), {}
for label, anc, ch in sorted(index, key=lambda x: (key(x[0]), x[1])):
    k = (plain(label).lower(), anc)
    if k in seen:
        continue
    seen.add(k)
    first = key(label)[0].upper()
    letter = first if first.isalpha() else '0–9'
    groups.setdefault(letter, []).append('[%s](#%s) ([%s](%s.html))' % (label.replace('[', '').replace(']', ''), anc, LABEL.get(ch, ch), ch))

idx = ['## <a id="g-index"></a>Alphabetical Index', '',
       'Every term, alias, abbreviation, provider term and Larkfield name in the tables above, from A to Z. The term links to the section of this page that defines it; the link in brackets goes to the chapter that owns it. Provider terms carry their company in brackets and point to the crosswalk.', '']
for L in ['0–9'] + [chr(c) for c in range(65, 91)]:
    if L in groups:
        idx.append('- **%s** — ' % L + ' · '.join(groups[L]))
idx.append('')

rd = lambda n: open(os.path.join(HERE, n)).read()
sources = '\n'.join('- [%s](%s), %s, n.d., accessed 2026-11 — %s.' % (DOCS[k][0], DOCS[k][1], DOCS[k][2], DOCS[k][3])
                    for k in doc_keys)
text = rd('head.md') + '\n'.join(body).replace('__XHEAD__', rd('xhead.md')) + '\n' + '\n'.join(idx) + rd('tail.md')
text = text.replace('__DOC_SOURCES__', sources).replace('__NONE__', NONE)
text = text.replace('__NROWS__', str(nrows)).replace('__XROWS__', str(xrows)).replace('__XDOC__', str(xdoc))
# reading time: words of prose and tables up to Sources, link targets left out, divided by 230 (style guide)
main = text.split('\n---', 1)[1].split('## Sources and Evidence')[0]
words = len(re.sub(r'\]\([^)]*\)|\[\[[^\]]+\]\]|<[^>]+>', ' ', main).split())
os.makedirs(os.path.dirname(OUT), exist_ok=True)
open(OUT, 'w').write(text.replace('__TTR__', str(round(words / 230))))
# the book's word count is the one check_draft.py reports (WRITER-BRIEF); use it when the spec is there
try:
    import json, subprocess
    repo = os.path.normpath(os.path.join(ROOT, '..', '..'))
    r = subprocess.run([sys.executable, os.path.join(repo, '_wiring', 'check_draft.py'), 'structure', os.path.dirname(OUT)],
                       capture_output=True, text=True, cwd=repo)
    words = json.loads(r.stdout)['words']
except Exception:
    pass
open(OUT, 'w').write(text.replace('__TTR__', str(round(words / 230))))
print('definition rows', nrows, '| crosswalk rows', xrows, '(from documentation: %d)' % xdoc, '| Larkfield rows', lrows,
      '| index entries', sum(len(v) for v in groups.values()), '| words', words)
