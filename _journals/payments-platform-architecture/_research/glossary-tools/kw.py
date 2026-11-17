"""Find where the book uses a term: python3 kw.py [-n HITS] [-c CONTEXT] [-f FOLDER_PREFIX] TERM [TERM ...]
Run from anywhere; searches posts/*/index.md of this journal (text before 'Sources and Evidence'),
skipping the glossary itself. Used to check a glossary or crosswalk row against the chapters."""
import re, sys, glob, os
ROOT = os.path.normpath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
args = sys.argv[1:]
n, c, pre = 2, 240, ''
while args and args[0] in ('-n', '-c', '-f'):
    if args[0] == '-n': n = int(args[1])
    elif args[0] == '-f': pre = args[1]
    else: c = int(args[1])
    args = args[2:]
files = sorted(f for f in glob.glob(os.path.join(ROOT, 'posts', '*', 'index.md')) if '/glossary/' not in f and f.split('/')[-2].startswith(pre))
texts = {f: open(f).read().split('## Sources and Evidence')[0] for f in files}
for t in args:
    print('##', t)
    k = 0
    for f, x in texts.items():
        for m in re.finditer(r'(?i)[^\n]{0,%d}' % (c // 2) + re.escape(t) + r'[^\n]{0,%d}' % c, x):
            print('   ', f.split('/')[-2][:22], '|', m.group(0).strip())
            k += 1
            break
        if k >= n: break
    if not k: print('    (not found)')
