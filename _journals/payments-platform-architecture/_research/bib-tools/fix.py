# Step 3 of 4: corrections on top of the rule-based classification, and the selection of each source's
# title, link, publisher, date, marks and claim from what the citing chapters wrote. Reads srcs3.json,
# writes srcs4.json, and prints the audit lines to read after every run:
#   no date         an entry with neither a date nor "n.d." (fix the chapter's entry)
#   DATE CONFLICT   chapters give one URL different dates (fetch the page, correct the chapters; or settle it in META_URL)
#   TITLE VARIANTS  chapters give one URL different full titles (correct the chapters; or settle it in TITLE)
#   SAME TITLE      two entries share a title: usually one document under two URLs (add it to EQUIV in gen.py)
#   AGE             a chapter's "(evidence age: N years)" mark disagrees with the entry's date
# Evidence age is counted to the research cut-off, November 2026. An entry dated before November 2023 is
# marked "(evidence age: N years)" as the chapters mark it; where a chapter wrote the mark itself
# ("evidence age: 11 years; in force"), its wording is kept.
import json, re, os
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
from classify import (TOPICS, NET, REGS, S_DOC, S_ENG, S_LEG, A_DOC, A_ENG, A_LEG, OTHER, PRACT, OWN, COMPANY_OF,
                      REG, STD, FIL, LET, DOC, TERMS, ENG, PR, GUIDE, SEC, MODEL)
D = json.load(open(os.path.join(HERE, 'srcs3.json')))
CUTOFF = (2026, 11)   # research cut-off: year, month
FLAG_BEFORE = (2023, 11)  # "older than about three years": dated November 2023 or earlier

# URL substring -> (topic or None, type or None): single sources the rules in classify.py get wrong
FIX = {
    # company blog posts that announce or explain a product (a named author does not make them engineering posts)
    'stripe.com/blog/everything-we-announced-at-sessions-2026': (None, GUIDE),
    'stripe.com/blog/top-product-updates-sessions-2025': (None, GUIDE),
    'stripe.com/blog/our-biggest-ever-upgrades-to-stripe-billing': (None, GUIDE),
    'stripe.com/blog/metronome-stripe-building-the-future-of-billing': (None, GUIDE),
    'stripe.com/blog/using-ai-optimize-payments-performance': (None, GUIDE),
    'stripe.com/blog/workbench-a-new-way-to-debug': (None, GUIDE),
    'stripe.com/blog/connect-express-onboarding': (None, GUIDE),
    'stripe.dev/blog/stripe-developer-digest': (None, GUIDE),
    'stripe.dev/blog/sessions-2025-dev-track-resources': (None, GUIDE),
    'stripe.com/sessions/2026/opening-remarks-and-product': (None, GUIDE),  # a product keynote
    'adyen.com/knowledge-hub/why-adyen-acquired-orb': (None, GUIDE),
    'adyen.com/knowledge-hub/rescue-failed-subscription-payments': (None, GUIDE),
    'adyen.com/knowledge-hub/adyen-joins-x402-foundation': (None, PR),
    # other companies
    'lemonsqueezy.com/blog/': (None, PR),
    'tempo.xyz/blog/mainnet': (None, PR),
    'cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments': (None, PR),
    'developer.apple.com/support/terms/': (None, TERMS),
    'paddle.com/pricing': (None, TERMS),
    'cockroachlabs.com/blog/adyen-guarantees-idempotency': (OTHER, GUIDE),  # a database vendor's customer story
    # a regulator's page that is neither a rule nor a decision stays "regulator publication"; a court opinion is law
}
# URL substring (a trailing $ anchors the end of the URL) -> display title
TITLE = {
    # link texts that only make sense inside their citing line
    'celex/02013R0575-20260101': 'Regulation (EU) No 575/2013, consolidated text of 2026-01-01',
    'fca.org.uk/publication/policy/ps25-12.pdf': 'PS25/12 (PDF)',
    'revenue-recognition/connect/destination-charges': 'Revenue Recognition for Connect platforms: destination charges',
    'treasury/connect/requirements': 'Treasury for platforms: requirements',
    'treasury/connect/legacy/v1/requirements': 'Treasury for platforms, legacy version: requirements',
    'docs.adyen.com/sitemap.xml': 'Adyen documentation sitemap',
    'docs.stripe.com/sitemap.xml': 'Stripe documentation sitemap',
    'help.adyen.com/sitemap.xml': 'Adyen help center sitemap',
    'adyen.com/licenses/singapore': 'Licenses and disclosures: Singapore',
    'adyen.com/licenses/united-states': 'Licenses and disclosures: United States',
    'stripe.com/pricing$': 'Stripe pricing',
    'paddle.com/pricing': 'Paddle pricing',
    'adyen.com/pricing$': 'Adyen pricing',
    'docs.withorb.com/integrations-and-exports/adyen': 'Orb documentation: Adyen integration',
}
# URL substring -> "Publisher, date": settles the metadata where the harvest cannot read it from the citing lines
META_URL = {
    'docs.adyen.com/online-payments/release-notes': 'Adyen documentation, n.d. (dated entries from 2018 to 2026), accessed 2026-11',
    'docs.adyen.com/release-notes/platforms-and-financial-products': 'Adyen documentation, n.d. (dated entries to 2026-11-13), accessed 2026-11',
    'docs.stripe.com/changelog$': 'Stripe documentation, n.d. (dated entries to 2026-10-28), accessed 2026-11',
}
# AGE notes that were read and are right as the chapter wrote them (URL substring)
AGE_OK = ['docs.adyen.com/online-payments/release-notes',       # old dated entries on an undated page
          'paypal.com/us/brc/article/avoid-excessive-retries',  # the mark is about the rules the article cites
          'adyen.com/knowledge-hub/how-adyen-does-ai']          # the chapter marks a two-year-old post; the register marks from three
TITLE_KEY = {'nourl:productscape': '*Payments and Revenue Infrastructure*, a Productscape domain model'}
META_KEY = {'nourl:productscape': 'The author, last reviewed 2026-11-15; not public'}
SUP_KEY = {'nourl:productscape': "The author's planning input for the book's coverage, mapped in [[domain-coverage]]; a planning map, not a description of any company's architecture and not a source for any fact in this book"}

YEAR = re.compile(r'\b(?:19|20)\d\d\b')
MON = {m: i + 1 for i, m in enumerate('january february march april may june july august september october november december'.split())}
MARK = re.compile(r'\s*\(((?:secondary|evidence age)[^()]*)\)', re.I)
def hit(k, u):  # URL substring, or with a trailing $ the URL's end
    return re.sub(r'\.md$', '', u.rstrip('/')).lower().endswith(k[:-1].lower()) if k.endswith('$') else k.lower() in u.lower()

def generic(t):  # a link text that only makes sense inside its citing line ("its requirements", "Singapore", "Form 10-K")
    return len(t) < 14 or t[0].islower() or bool(re.match(r'^(Form )?\d+-[KQ]\b|^Form \d|^(About us|Home ?page|Overview|Documentation|Pricing|Sitemap)$', t))

def date_of(meta):
    """First publication/version date in a citation as a tuple (y[, m[, d]]), or None. Access dates do not count."""
    m2 = re.sub(r'\b(accessed|fetched|retrieved|read|live|snapshot of|archived copy of|list read|banner accessed)\b[^,;)]*', '', meta)
    m2 = MARK.sub('', m2)
    best = None
    for a in re.finditer(r'\b((?:19|20)\d\d)(?:-(\d\d))?(?:-(\d\d))?\b', m2):
        best = (a.start(), tuple(int(x) for x in a.groups() if x)); break
    for a in re.finditer(r'\b(?:(\d{1,2}) )?([A-Z][a-z]+) ((?:19|20)\d\d)\b', m2):
        if a.group(2).lower() in MON and (best is None or a.start() <= best[0]):
            best = (a.start(), (int(a.group(3)), MON[a.group(2).lower()]) + ((int(a.group(1)),) if a.group(1) else ()))
        break
    return best[1] if best else None

def compatible(a, b):  # 2021-07 and 2021-07-28 are one date at two precisions
    n = min(len(a), len(b)); return a[:n] == b[:n]

def clean_meta(m):
    m = MARK.sub('', m).strip()
    m = re.sub(r'\bundated\b', 'n.d.', m)
    m = re.sub(r'^all (?=n\.d)', '', m)
    m = re.sub(r'[\s,;:]+\.?$', '', m)
    return m.strip(' ,:')

def pick_meta(metas):
    ms = [clean_meta(m) for m in metas if m and clean_meta(m)]
    if not ms: return ''
    dated = [m for m in ms if date_of(m)]
    pool = dated or ms
    if dated:  # the most precise date wins, then the wording most chapters use, then the fuller publisher
        prec = max(len(date_of(m)) for m in dated)
        pool = [m for m in dated if len(date_of(m)) == prec]
    c = Counter(pool)
    return max(c, key=lambda m: (c[m], not m[0].isdigit(), len(m)))

def age_years(d):
    if d is None: return None
    if len(d) == 1: return CUTOFF[0] - d[0]
    return ((CUTOFF[0] - d[0]) * 12 + CUTOFF[1] - d[1]) // 12
def old(d):
    return d is not None and (d[0], d[1] if len(d) > 1 else 1) <= FLAG_BEFORE

LC = {}
p = os.path.join(HERE, 'link-check.json')
if os.path.exists(p): LC = json.load(open(p))
def display_url(s):  # among the URLs the chapters use for one document: the page itself, not its .md export or a locale copy
    us = s.get('urls') or ([s['url']] if s['url'] else [])
    if not us: return None
    def rank(u):
        r = LC.get(u, {})
        return (r.get('status', 200) != 200, u.endswith('.md') or '.md?' in u, bool(re.search(r'\.com/[a-z]{2}-[a-z]{2}/', u)), us.index(u))
    return min(us, key=rank)

audit = []
for s in D['srcs']:
    u = s['url'] or ''
    for k, (tp, ty) in FIX.items():
        if k in s['key'] or k in u:
            if tp is not None: s['topic'] = tp; s['company'] = COMPANY_OF[tp]
            if ty: s['type'] = ty
    # title: a full title before a link text that only works inside its line; then the title most chapters use
    c = Counter(t for t in s['titles'] if t)
    if c: s['title'] = max(c, key=lambda t: (not generic(t), c[t], -s['titles'].index(t)))
    full = sorted(set(re.sub(r'\W+', '', t).lower() for t in c if not generic(t)))
    settled_title = any(hit(k, u) for k in TITLE)
    for k, t in TITLE.items():
        if hit(k, u): s['title'] = t
    s['title'] = TITLE_KEY.get(s['key'], s['title'])
    if re.match(r'^Form \d|^Form (10|8|20)-', s['title']):  # "Form 10-K for fiscal 2026" -> with the filer's name
        pub = re.sub(r',.*$', '', pick_meta(s['metas']))
        if pub and pub not in s['title']: s['title'] = f"{pub}, {s['title']}"
    if len(full) > 1 and not settled_title:
        audit.append(f"TITLE VARIANTS {s['key']} | " + ' / '.join(sorted(t for t in c if not generic(t))))
    s['url'] = display_url(s)
    # marks the chapters wrote on the entry
    marks = [m.strip() for x in s['metas'] + s['sups'] for m in MARK.findall(x or '')]
    s['sups'] = [MARK.sub('', x or '').strip() for x in s['sups']]
    # publisher and date
    s['meta'] = pick_meta(s['metas'])
    settled = False
    for k, mt in META_URL.items():
        if hit(k, u): s['meta'] = mt; settled = True
    if s['key'] in META_KEY: s['meta'] = META_KEY[s['key']]; settled = True
    d = date_of(s['meta'])
    ds = [date_of(clean_meta(m)) for m in s['metas'] if m and re.search(r'\w', m)]  # a secondary link inside a claim has no citation of its own
    dset = sorted(set(x for x in ds if x))
    conflict = any(not compatible(a, b) for a in dset for b in dset) or (dset and any(x is None for x in ds))
    if conflict and not settled:
        audit.append(f"DATE CONFLICT {s['key']} | " + ' / '.join(sorted(set(f'{pm}: {m}' for pm, t, m, _ in s['by'] if re.search(r'\w', m)))))
    if d is None and 'n.d' not in s['meta']:
        if s['meta'] and re.search(r'\b(accessed|fetched|read)\b', s['meta']):  # "Adyen, accessed 2026-11": an undated page
            s['meta'] = re.sub(r',?\s*\b(transcript accessed|list read|accessed|fetched|read)\b', r', n.d., \1', s['meta'], count=1).strip(' ,')
        else:
            audit.append(f"no date {s['key']} | {s['meta']!r} | {s['chapters']}")
            s['meta'] = (s['meta'] + ', ' if s['meta'] else '') + 'n.d.'
    s['date'] = '-'.join(f'{x:02d}' if i else str(x) for i, x in enumerate(d)) if d else 'n.d.'
    # marks: secondary source, evidence age
    sec = any(m.lower().startswith('secondary') for m in marks) or s['type'] == SEC
    agem = [re.sub(r'^secondary source;\s*', '', m, flags=re.I) for m in marks if 'evidence age' in m.lower()]
    n = age_years(d)
    s['age'] = n if old(d) else None
    mark = ''
    if old(d):
        mark = Counter(agem).most_common(1)[0][0] if agem else f"evidence age: {n} {'year' if n == 1 else 'years'}"
        mark = mark[0].lower() + mark[1:]
        for m in set(agem):
            mm = re.search(r'(\d+(?:\.\d)?)', m)
            if mm and not any(k in u for k in AGE_OK) and abs(float(mm.group(1)) - ((CUTOFF[0] - d[0]) * 12 + CUTOFF[1] - (d[1] if len(d) > 1 else 6)) / 12) > 1:
                audit.append(f"AGE {s['key']} | dated {s['date']} ({n} years) but a chapter says '{m}' | {s['chapters']}")
    elif agem and not any(k in u for k in AGE_OK):
        audit.append(f"AGE {s['key']} | dated {s['date']}, not older than three years, but a chapter says '{agem[0]}' | {s['chapters']}")
    s['secondary'] = sec
    s['mark'] = '; '.join(x for x in (('secondary source' if sec and s['type'] != MODEL else ''), mark) if x)
    if s['key'] in SUP_KEY: s['sups'] = [SUP_KEY[s['key']]]
json.dump(D, open(os.path.join(HERE, 'srcs4.json'), 'w'), indent=1, ensure_ascii=False)
print(dict(Counter(TOPICS[s['topic']] for s in D['srcs'])))
print(dict(Counter(s['type'] for s in D['srcs'])))
print('no URL:', [s['title'] for s in D['srcs'] if not s['url']])
for a in audit: print(a)
seen = {}
for s in D['srcs']:  # two sources with one title: usually one document under two URLs (add it to EQUIV in gen.py)
    k = re.sub(r'\W+', '', s['title'].lower())
    if k in seen and not generic(s['title']): print('SAME TITLE', s['title'][:70], '|', seen[k], '|', s['url'])
    seen[k] = s['url']
