# Step 4 of 4: assign stable R-numbers and write posts/bibliography/index.md.
# R-numbers live in ids.json (normalized URL key -> R-number). Existing sources keep their number;
# new sources append from the next free number; a removed source's number is retired, never reused.
# Delete ids.json only to deliberately renumber the whole register (never after publication).
# Every count on the page is computed here from srcs4.json; nothing on the page is typed by hand.
import json, re, os, glob
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
from classify import TOPICS, REG, STD, FIL, LET, DOC, TERMS, ENG, PR, GUIDE, SEC, MODEL, OWN
D = json.load(open(os.path.join(HERE, 'srcs4.json')))

TOPDESC = [
    "What the card networks and the payment schemes publish themselves: Visa's public rules and fee tables, the networks' annual filings and press releases, and the pages of scheme operators such as iDEAL, Pay.UK, the European Payments Initiative and The Clearing House. Mastercard's rule documents could not be retrieved in November 2026, so its rules are cited through Stripe's and Adyen's documentation.",
    'Legal texts of the EU, its member states, the UK, the US and India, publications of central banks, supervisors and tax authorities, and the standards a payment system is built against: PCI DSS, EMV and IFRS 15.',
    "Stripe's documentation, API reference, changelog, support site and status page. These pages are undated and change without notice; each was read in November 2026.",
    "Stripe's engineering and developer blogs, incident reports, Stripe Sessions talks, newsroom releases, guides and product pages.",
    "Stripe's annual letters, its services agreement and the legal, licence and pricing pages of its entities. Stripe is a private company: its company figures come from these letters and from its newsroom, not from audited accounts.",
    "Adyen's documentation, API reference and specifications, release notes, help center and status page. These pages are undated and change without notice; each was read in November 2026.",
    "Adyen's engineering posts and explainers in its knowledge hub, product pages and press releases about products and acquisitions.",
    "Adyen's annual report, half-year shareholder letters and business updates with their results releases, and its terms, licence and pricing pages. Adyen is listed: its annual report carries audited financial statements.",
    'Documentation, engineering posts, filings and announcements of companies other than Stripe and Adyen: PayPal, Checkout.com, Block, Orb, Uber, Airbnb, Apple, Google and others, most of them cited in the contrast cases and the billing chapters.',
    'Trade press, law-firm briefings, analysts and independent engineers. These are secondary sources: the chapters use them to fill a gap and say so in the sentence that cites them.',
    "The Productscape domain model the book was planned from. It is listed once so that the planning input is visible; it is not public and supports no claim.",
]
TYPEDESC = [
    (REG, 'Legal texts, court opinions, and the publications of central banks, supervisors and tax authorities', 'Supports a requirement or an official position at its date. A legal text stays in force until it is amended or replaced, so its age matters less than whether it still applies; what it means for one business is a question for its lawyers'),
    (STD, "Visa's public rules and fee tables, PCI DSS, EMV and IFRS texts and the pages of the bodies and scheme operators that maintain them", 'Supports what the rule or the standard requires in the cited version; it says nothing about how a provider implements it'),
    (FIL, "Adyen's annual report, shareholder letters and business updates, and the SEC filings of Visa, Mastercard, PayPal, Block and Global Payments", "Supports a reported figure or event at its date. An annual report or a Form 10-K carries audited financial statements; a half-year letter or a quarterly update does not. Written for investors, not as design documentation"),
    (LET, "Stripe's annual letters", 'Supports what a private company chose to say about itself in that year. The figures are not audited and are not defined the way a listed company defines them, so they are not compared with audited figures'),
    (DOC, 'Documentation, API references, specifications, release notes, support articles and status pages', "Supports an interface as it was read. Most pages are undated ('n.d.'), so the access month, November 2026, says when; the page may have changed since. It describes behavior a customer can see, not how the system is built"),
    (TERMS, 'Service agreements, acquirer and licence disclosures, pricing pages and policies', 'Supports who the contracting entity is, what licence it holds and what the terms say at the stated version; terms and prices differ by country and change'),
    (ENG, "Engineering blog posts, incident reports and conference talks by a company's own engineers", 'Supports only what the company said it had built in the year of the post. The system may have been replaced since, and the post is silent on what was not published'),
    (PR, 'Newsroom and press releases, results releases and launch or acquisition announcements', 'Supports that the company announced something on that date. Performance figures in a release are the company\'s claims, and announced is not the same as generally available'),
    (GUIDE, 'Guides, explainers, product pages and product blog posts', "Supports how a company describes a product or a subject to its customers. Vendor claims are claims; an explainer by a provider about a regulation is a secondary source for that regulation"),
    (SEC, 'Trade press, law-firm and analyst briefings, independent engineers and podcasts', "Marked '(secondary source)'. Fills a gap where no first-party source was found and is named as secondary in the sentence that cites it; follow it to the primary source where one exists"),
    (MODEL, "The author's Productscape domain model of payments and revenue infrastructure", "Planning material, not evidence: it shaped the book's coverage, mapped in [[domain-coverage]], and is not a source for any fact"),
]
COMPANIES = ['Stripe', 'Adyen', 'Card networks and payment schemes', 'Regulators and standards bodies', 'Other companies',
             'Independent authors, analysts and press', 'The author']

chap = D['chapters']  # folder, permalink, title
LIVE = set()  # permalinks that exist now: a [[link]] to a page not yet written is rendered as plain text
for p in glob.glob(os.path.join(ROOT, 'posts', '*', 'index.md')):
    m = re.search(r'^permalink:\s*(\S+)', open(p).read(), re.M)
    if m: LIVE.add(m.group(1).strip('"\''))
LIVE.add('bibliography')
def xl(pm): return f'[[{pm}]]' if pm in LIVE else pm
corder = {pm: i for i, (f, pm, t) in enumerate(chap)}
srcs = D['srcs']
for s in srcs:
    s['chapters'].sort(key=lambda p: corder.get(p, 999))
    s['first'] = corder.get(s['chapters'][0], 999)
srcs.sort(key=lambda s: (s['topic'], s['first']))

idp = os.path.join(HERE, 'ids.json')
ids = json.load(open(idp)) if os.path.exists(idp) and open(idp).read().strip() else {}
nxt = max([int(v[1:]) for v in ids.values()] + [0]) + 1
new = 0
for s in srcs:
    if s['key'] not in ids:
        ids[s['key']] = f'R{nxt}'; nxt += 1; new += 1
    s['id'] = ids[s['key']]
json.dump(ids, open(idp, 'w'), indent=1, ensure_ascii=False)
retired = len(ids) - len(srcs)
num = lambda r: int(r[1:])
srcs.sort(key=lambda s: (s['topic'], num(s['id'])))

def clause(s):
    sup = next((x for x in s['sups'] if x), '').strip()
    if len(sup) > 280:
        cut = sup[:280]; j = max(cut.rfind('; '), cut.rfind('. '))
        sup = cut[:j] if j > 80 else cut.rsplit(' ', 1)[0]
    sup = sup.rstrip(' .;,')
    if sup.count('"') % 2: sup = sup.rstrip('"') if sup.endswith('"') else sup + '"'
    if sup and not (len(sup) > 1 and sup[1].isupper()) and not sup.startswith('`'): sup = sup[0].upper() + sup[1:]
    return (sup + '.') if sup else ''

def entry(s):
    meta = s['meta'].strip().rstrip('.')
    if meta.endswith('n.d'): meta += '.'
    if meta[:1].islower() and not meta.startswith('iDEAL'): meta = meta[0].upper() + meta[1:]
    title = s['title'].replace('|', '/').replace('[', '(').replace(']', ')')
    head = f"[{title}]({s['url']})" if s['url'] else s['title']
    line = f"- **{s['id']}** · {head}" + (f" — {meta}" if meta else '')
    if s.get('mark'): line += f" **({s['mark']})**"
    parts = [line + ('' if line.endswith('.') else '.')]
    c = clause(s)
    if c: parts.append(c)
    if s.get('extra'): parts.append('Also cited at: ' + ', '.join(f'[{a}]({b})' for a, b in s['extra']) + '.')
    parts.append(f"*{s['type']}.*")
    parts.append('Cited in: ' + ', '.join(xl(p) for p in s['chapters']) + '.')
    out = ' '.join(parts)
    return out.replace('this chapter', 'the citing chapter').replace('This chapter', 'The citing chapter')

def rng(idl):
    idl = sorted(idl, key=num)
    return f"{idl[0]}–{idl[-1]}" if len(idl) > 1 else idl[0]
def n_(n, one, many): return f"{n} {one if n == 1 else many}"

types = Counter(s['type'] for s in srcs)
cited_pages = [pm for f, pm, t in chap if any(pm in s['chapters'] for s in srcs)]
undated = [s for s in srcs if s['date'] == 'n.d.']
aged = [s for s in srcs if s.get('age') is not None]
second = [s for s in srcs if s.get('secondary') and s['type'] != MODEL]
oldest_eng = {c: min((s for s in srcs if s['company'] == c and s['type'] == ENG and s['date'] != 'n.d.'), key=lambda s: s['date'], default=None) for c in ('Stripe', 'Adyen')}
top = max(srcs, key=lambda s: (len(s['chapters']), -num(s['id'])))

body = []
body.append('## How to Read This Register\n')
body.append(f"**R-numbers identify sources; they do not rank them.** The register contains **{len(srcs)} sources** harvested from the Sources and Evidence sections of **{len(cited_pages)} pages**. A document that chapters cite under two addresses (a documentation page and its Markdown export, a page with and without a country prefix) is one entry, with the other address kept as **Also cited at** where it leads somewhere different.\n")
body.append('Identifiers stay stable. A new source receives the next unused number and a removed source retires its number, so an R-number written down today identifies the same document after the register is regenerated.\n')
body.append("Each entry gives, in this order: the R-number, the linked title, the publisher or author, the date, the claim the first citing chapter uses it for, the evidence type in italics, and the pages that cite it. The publisher and date follow the chapters' citations; where chapters cited one document differently, the page itself was read in November 2026 and the chapters were corrected to agree.\n")
body.append(f"**The date is the publication, version or last-updated date the source shows.** **'n.d.'** means the page shows no date: {len(undated)} of the {len(srcs)} entries are undated, almost all of them documentation, and for those the access month (November 2026) is the only indication of when the text was read.\n")
body.append(f"**The age mark flags old evidence.** An entry dated before November 2023 carries **(evidence age: N years)**, counted to the research cut-off of 17 November 2026, as the chapters mark it in their own source lists. {len(aged)} entries carry the mark. For a legal text the mark is a reminder to check that it is still in force; for an engineering post it means the system described may have been replaced, and the citing chapter says whether current documentation confirms the old account.\n")
body.append(f"**The secondary mark flags evidence that is not first-party.** {n_(len(second), 'entry carries', 'entries carry')} **(secondary source)**: trade press, a law firm's or an analyst's briefing, or one company writing about another's rules. A chapter uses such a source only to fill a gap and names it as secondary in the sentence that cites it.\n")
body.append('**The evidence type says how much the source can support.** The table gives each type, the number of entries of that type, what it contains and what it supports.\n')
body.append('| Evidence type | Sources | What it is | What it supports |')
body.append('| --- | --- | --- | --- |')
for t, what, how in TYPEDESC:
    if types.get(t): body.append(f"| {t} | {types[t]} | {what} | {how} |")
body.append('')
body.append('**The evidence is uneven between the two companies, and the counts show where.** The next table counts the entries by who published them, with how many are undated and how many carry the age mark.\n')
body.append('| Publisher | Sources | Undated (n.d.) | Older than three years | Engineering posts or talks | Annual letters, reports and filings |')
body.append('| --- | --- | --- | --- | --- | --- |')
for c in COMPANIES:
    cs = [s for s in srcs if s['company'] == c]
    if cs: body.append(f"| {c} | {len(cs)} | {sum(1 for s in cs if s['date'] == 'n.d.')} | {sum(1 for s in cs if s.get('age') is not None)} | {sum(1 for s in cs if s['type'] == ENG)} | {sum(1 for s in cs if s['type'] in (LET, FIL))} |")
body.append(f"| **Total** | **{len(srcs)}** | **{len(undated)}** | **{len(aged)}** | **{types.get(ENG, 0)}** | **{types.get(LET, 0) + types.get(FIL, 0)}** |")
body.append('')
se, ae = oldest_eng['Stripe'], oldest_eng['Adyen']
if se and ae:
    body.append(f"Two things follow from the table. Most of what the book says about either provider's interface rests on undated documentation read in one month, so it describes November 2026 and nothing later. And the engineering evidence reaches back years: the oldest Stripe engineering source cited is {se['id']} ({se['date'][:4]}) and the oldest Adyen one is {ae['id']} ({ae['date'][:4]}). Stripe's company figures come from annual letters and newsroom releases, Adyen's from an annual report with audited statements, so a figure from one is not set against a figure from the other as if they measured the same thing.\n")
body.append("**What the register leaves out.** Private research notes and the book plan are excluded; their claims point to public sources, which are listed here. Cross-references to the companion books RECONCILED, ORDERED and LISTED are reading links, not evidence, and are excluded as well. The author's Productscape planning model appears once, as the last entry, as planning material that supports no claim. A statement the book marks **Not public** has no entry by definition: it records that the public record, searched up to the research cut-off of 17 November 2026, does not say. No source describes Larkfield, which is fictional.\n")
body.append('## Topic Index\n')
body.append(f"Entries are grouped by who published the source, because in this book the publisher and the kind of document decide how much a source supports. Each group below gives its range of identifiers, its number of entries and its most widely cited source; a range runs from the group's lowest to its highest identifier, and because a new source takes the next unused number, ranges can overlap. The most widely cited source in the whole register is {top['id']}, *{top['title'].strip('*')}*, cited in {len(top['chapters'])} pages. To start from a chapter instead, use **Sources by Chapter** near the end.\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    tp = max(ts, key=lambda s: (len(s['chapters']), -num(s['id'])))
    most = '' if i == OWN else f" The most widely cited is {tp['id']}, *{tp['title'].strip('*')}*, cited in {n_(len(tp['chapters']), 'page', 'pages')}."
    body.append(f"**{T} ({rng([s['id'] for s in ts])}, {n_(len(ts), 'source', 'sources')}).** {TOPDESC[i]}{most}\n")
for i, T in enumerate(TOPICS):
    ts = [s for s in srcs if s['topic'] == i]
    if not ts: continue
    body.append(f"## {T}\n")
    body += [entry(s) for s in ts]
    body.append('')
body.append('## Sources by Chapter\n')
body.append('The same sources, read from the citing side: each line lists the identifiers a page cites in its **Sources and Evidence** section, in identifier order, with pages in reading order. Pages that cite no external source of their own (the part introductions and some preface and reference pages) are omitted.\n')
for f, pm, t in chap:
    idl = sorted((s['id'] for s in srcs if pm in s['chapters']), key=num)
    if idl: body.append(f"- {xl(pm)} ({len(idl)}): " + ', '.join(idl) + '.')
body.append('')
body.append("No source above describes Larkfield, the fictional studio-software platform the book follows; architectural recommendations, labeled inferences and labeled assumptions are the author's judgement.")
body.append('')
body.append("This register closes the four reference pages, which answer the four lookups a chapter leaves you with: where a topic is covered ([[domain-coverage]]), which template or card a decision needs ([[toolkit]]), what a word means and what Stripe and Adyen each call it ([[glossary]]) and which source backs a claim (this page). Each answer points back to the chapter that owns it, so a disagreement between a chapter and a reference page is a defect to fix in one of them. Before you build on a statement about Stripe or Adyen, find its entry here and read its type and date; where the entry is an engineering post older than about three years or an undated documentation page, check the provider's current documentation first.")
body_txt = '\n'.join(body)

head = f'''---
title: "Bibliography"
date: 2026-11-17
author: Željko Obrenović
excerpt: "Which sources does the book cite, and how much does each kind of source support? Every public source the pages cite, listed once under a stable R-number with its date, its evidence type and the pages that rely on it, by publisher and by chapter."
permalink: bibliography
timetoread: __TTR__ min read
icon: "assets/icons/bibliography.png"
logo: "assets/images/bibliography/logo.jpeg"
logo_credit: "Image generated by Google Gemini (gemini-3-pro-image-preview)"
---

> **IN THIS SECTION, YOU WILL:** Find the public source behind any claim in the book, with its date, its evidence type and every page that relies on it, and learn how much each kind of source supports.

> **KEY POINTS:**
>
> * **Every public source is listed once, because a page cited it.** Each entry was harvested from a page's **Sources and Evidence** section and carries a stable R-number, its date or 'n.d.', its evidence type and the pages that cite it. An R-number identifies a source; it does not rank it, and nothing is added as further reading.
> * **The type and the date decide how much a source supports.** A regulation or a network rule supports a requirement, audited accounts support a reported figure, an annual letter supports what a private company chose to say, undated documentation supports an interface as read in November 2026, and an engineering post supports only what the company said it had built in the year of the post.
> * **Look the entry up before you rely on a statement about Stripe or Adyen.** Where the entry is an engineering post older than about three years or an undated page, check the current documentation first. No source describes Larkfield, which is fictional; the labeled inferences, recommendations and assumptions are mine.

<br>
Use this register to trace a claim in any chapter to its public source and to see when that evidence was published or read. The entries come from the chapters' own **Sources and Evidence** sections, which sort each chapter's sources into three groups (company, product and investor sources; standards, regulation and official documentation; research and practitioner sources) and mark old or second-hand evidence with **(evidence age: N years)** and **(secondary source)**. Research ran up to **17 November 2026**. **'n.d.' means undated**, so for those entries the access month is the only indication of when the page was read.

The register does what a chapter's own list cannot: it shows how many pages lean on one source and how old the evidence under a subject is. That matters here because the public record is uneven. Stripe's best-known posts on idempotency, rate limiting and versioning are from 2017, Adyen's account of its accounting design is from 2021, most documentation pages are undated, and Stripe's company figures come from annual letters while Adyen's come from audited reports.

The page first explains how to read an entry (R-numbers, dates, the age and secondary marks, the evidence types and what each supports, the counts by publisher, and what is left out), then gives a topic index, the entries grouped by publisher and, near the end, the sources by chapter.

'''
os.makedirs(os.path.join(ROOT, 'posts', 'bibliography'), exist_ok=True)
text = head + body_txt + '\n'
words = len(re.sub(r'\(https?://[^)]+\)', '', text.split('\n---\n', 1)[1]).split())  # the whole page after the front matter
text = text.replace('__TTR__', str(max(5, round(words / 230 / 5) * 5)))
open(os.path.join(ROOT, 'posts', 'bibliography', 'index.md'), 'w').write(text)
print(f"{len(srcs)} sources ({new} new R-numbers, {retired} retired, highest R{nxt - 1}); {words} words")
print('by type:', {t: types[t] for t, _, _ in TYPEDESC if types.get(t)})
print('by publisher:', {c: sum(1 for s in srcs if s['company'] == c) for c in COMPANIES})
print(f"undated: {len(undated)}; age-marked: {len(aged)}; secondary: {len(second)}")
for i, T in enumerate(TOPICS):
    ts = [s['id'] for s in srcs if s['topic'] == i]
    if ts: print(f'  {T}: {len(ts)} ({rng(ts)})')
