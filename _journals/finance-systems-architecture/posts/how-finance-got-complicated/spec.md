---
status: accepted
revised: 2026-11-18
---

# Spec: From Cash Box to Cloud: How Keeping the Books Got This Complicated

## Intent

Take a reader who knows nothing about accounting or finance systems from the simplest way of keeping track of money (a trader alone with a cash box and a list) to today's enterprise finance estate, one step at a time, and introduce each concept the book uses at the step that first needed it. Every step answers the same question: **can someone who was not there trust these numbers, and how would they find out?** The answer grows from "nobody else needs to; he counts the coins" to a chain of records, systems, controls and outside checkers. The page leaves the reader thinking that the fourteen failure patterns on the next page are natural consequences of that growth.

**Thesis (disputable).** Enterprise finance systems are complex not because vendors oversold or architects overbuilt, but because every new reader of the books who was not there (a partner, a lender, a shareholder, an auditor, a regulator, a group) demanded a new way to prove the numbers, and every new way of producing the numbers faster (machines, the ERP, the spreadsheet, the specialist platforms) added another record that must itself be proven. Each was a bargain both sides wanted, and none was ever retired. The rival view this page argues against: that the complexity is accumulated technical debt that a clean, single modern system would remove.

**Role in the preface.** Sits after [[introduction]] and before [[where-finance-architecture-goes-wrong]]. The introduction says the estate must be architected so it can always be reconciled; this page shows, in plain words, why so many records exist to be reconciled; the patterns page names what goes wrong between them. Transition in: the introduction's hand-off ("before the patterns, see how the books got this way"). Hand-off: the patterns page.

## Audience

The book's readers (Chief and Enterprise Architects, finance-systems, solution and integration architects, engineering leaders, finance-transformation leaders), and in particular those from engineering who have no accounting training. Written so that a reader new to finance follows every sentence: short sentences, one new term per paragraph at most, plain words before the term.

## Success criteria

Reader outcomes, checked as probes:

- [ ] Given a concept from a later chapter (double entry, trial balance, period close, ICFR, consolidation, book of record, subledger, clearing account, satellite platform, end-user computing), the reader can say which step introduced it and what limit of the previous step it answered.
- [ ] Given a failure pattern's name from the next page, the reader can say which step makes it possible; each of the fourteen names appears exactly once in the tally's last column.
- [ ] The reader can retell the walk in one sentence per step, and can state for each step what it made possible for both sides (the one who keeps the books and the one who must trust them) before what it cost.
- [ ] The reader can say how the answer to the running question changed from the first step to the last.
- [ ] The reader can tell documented fact from illustration on the page: every year, law and first is sourced and listed; generalizations are marked as common practice or illustration; Northmere appears only at the last step and is labeled fictional; the simplification is declared once, early.
- [ ] The reader leaves expecting a failure wherever two records of the same money are kept by different hands at different times, and opens [[where-finance-architecture-goes-wrong]] with that expectation.

Form: IN THIS SECTION, YOU WILL; exactly three KEY POINTS that name concrete things (the cash box, the ledger, the auditor, the spreadsheet, the payment provider's report), not abstractions; `<br>`; nine `##` steps; a tally table `Step | What it made possible | What it added | New party or delay | What can now go wrong`; an anchor timeline `Year | What its source dates to that year | Step`; closing and hand-off; Sources and Evidence in the book's grouping. One figure per step plus one overview figure (ten). 3,000–4,700 words of prose.

## Structure (one section per step)

Each step: where things stood; what stopped working or what people wanted next; what was added, in plain words, then the book's term in bold with a `[[link]]` to its owning chapter; what it made possible for each side; what it cost; a figure; the running question answered in two bold parts.

1. **The cash box** — a trader alone (illustration). Need: know whether he is ahead. Concept: a list of what came in and went out. Gain: no one else to satisfy. Cost: only he can read it. Answer: nobody else needs to trust it; he counts the coins.
2. **The partner who was not there: journal, ledger, double entry** — partners, lenders and customers on credit must trust books they did not watch. Concepts: journal entry, ledger accounts, double entry ([[accounting-for-architects]]); the second pair of eyes, segregation of duties ([[controls-and-auditability]]). Anchor: Pacioli's *Summa*, Venice, 1494 (ICAEW). Gain: the merchant raises money and sells on credit; the partner invests without travelling; the customer buys before paying. Cost: the books become a second account of reality; balance proves arithmetic, not truth; error and fraud.
3. **The year-end: period, close, statements** — a business that never stops needs a regular measure. Concepts: the period, accruals, the trial balance ([[accounting-for-architects]]), the period close ([[finance-processes]]). Gain: owners know the year's profit; lenders lend to a going business. Cost: a deadline, cut-off, estimates, the close as work.
4. **Shareholders who were never there: standards, the auditor, the law** — strangers buy shares. Concepts: published statements under accounting standards; the external auditor and audit evidence ([[controls-and-auditability]]). Anchors: US Securities Act 1933 and Securities Exchange Act 1934 (SEC). Gain: the company raises money from thousands of strangers; the investor compares companies she never visits. Cost: new parties and deadlines; evidence must be kept; the auditor tests a sample once a year.
5. **Many companies, one owner: entities, currencies, consolidation** — trade across borders and acquisitions. Concepts: legal entity, intercompany, functional currency and translation ([[global-scale]], [[accounting-for-architects]]), consolidation and elimination ([[onestream]]). Anchor: EU Regulation 1606/2002, IFRS for listed groups' consolidated accounts from financial years starting 1 January 2005. Gain: sell and own companies in many countries; the investor sees one group. Cost: many books that must agree; both halves of each intercompany balance; rates; local rules. Pattern: The Permanent Exception.
6. **The machine keeps the books: from punched cards to the ERP** — volume. Concepts: the accounting system, then the ERP as the accounting core and **book of record** ([[finance-landscape]]); controls inside the system; ICFR and SOX ([[controls-and-auditability]]). Anchors: SAP's RF financial accounting system 1973 and R/3 1992 (SAP News); Sarbanes-Oxley Act 2002 (SEC). Gain: thousands of entries a day posted the same way; operations and books share one database; the auditor tests the system's controls rather than every entry. Cost: trust moves to configuration, access and change; customization; one system asked to do everything. Patterns: The Swiss-Army ERP, Customization Concrete, Audit Archaeology.
7. **Meanwhile, the spreadsheet** — the system changes slowly; the accountant needs an answer today. Concept: end-user computing and information produced by the entity ([[controls-and-auditability]], [[technical-debt-and-fitness]]). Anchor: VisiCalc, 1979 (Computer History Museum). Gain: any accountant builds a mapping or a reconciliation in an hour. Cost: logic no one else can see or test. Pattern: Spreadsheet Glue.
8. **Systems around the ledger** — online selling, cards and payment providers, volume, specialist work. Concepts: subledger and summarized posting ([[accounting-for-architects]], [[finance-landscape]]); PSP settlement and the clearing account ([[payments-fundamentals]], [[payments-to-ledger]]); satellite platforms ([[satellite-platforms]]); interfaces and control totals ([[integration-architecture]]); reconciliation between systems ([[traceability-and-reconciliation]]). Common practice, no date. Gain: customers pay by card anywhere; each specialist job done by a platform built for it; the ledger stays readable. Cost: each system keeps its own copy and its own timing. Patterns: The Shadow Ledger, The Suspense Swamp, Lost in Aggregation, Point-to-Point Spaghetti.
9. **Today** — cloud ERP and SaaS platforms on the vendor's release schedule; groups with several ERPs after acquisitions ([[multiple-erps]], [[finance-data-architecture]]); tax authorities that want invoices as data (ViDA in force 14 April 2025, European Commission); continuous accounting and controls by design ([[blackline]], [[controls-and-auditability]]); bots and AI agents ([[ai-in-finance]]). Northmere's €600 Lisbon booking as today's case (fictional; facts from the scenario ledger). Patterns: The Doppelgänger Record, Capability Creep, Big-Bang Bravado, The Borrowed Roadmap, Nobody's Bot.

**Conclusion:** the tally (synthesis), the anchor timeline (how old each step is; undated steps are common practice), the count of what stands behind the €600 that did not stand behind the cash box (callback), the claim that the complexity is the price of trust at a distance, not a mistake (so-what), the expectation to carry forward (takeaway), and the hand-off to [[where-finance-architecture-goes-wrong]]. [[long-term-evolution]] is linked for what comes next, not retold.

## Non-goals

- A history of accounting, auditing or the software industry; companies, founders and deals beyond the few anchors.
- Re-teaching what the chapters own (journal-entry mechanics, ICFR testing, consolidation steps, payment lifecycle): one plain sentence and a link.
- The future of the estate ([[long-term-evolution]] owns stressors and the decade ahead).
- The failure patterns themselves ([[where-finance-architecture-goes-wrong]]) and Northmere's full description ([[meet-northmere]]).
- Any ranking or recommendation of vendors; product names appear only as dated anchors and as Northmere's systems at the last step.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

Article only.

## Open questions

- None blocking. The author may wish to add a dated anchor for the first payment providers or close tools; none was added because the step is common practice and the book's own chapters already date the vendors.

## Decision log

- **2026-11-18** — Written with the `field-evolution` skill, modeled on the sibling books' pages (payments, commerce, listings). The book has no outcome specs (no `journal-spec.json`, every page has `spec.md`), so this spec follows the book's `spec.md` format and records thesis, role and transition here.
- **2026-11-18** — Running question chosen as "can someone who was not there trust these numbers, and how would they find out?" because it ties the field's standing concerns (a record someone else must trust, error and fraud, who checks) to the book's organizing idea, reconciliation.
- **2026-11-18** — Sarbanes-Oxley placed in the machine step, not the auditor step, because its concept for this book is control inside systems; the date order is kept honest with "by then".
- **2026-11-18** — The spreadsheet is its own step ("meanwhile") although it predates R/3, because it answers a different need (speed of change) and introduces its own pattern.
- **2026-11-18** — Rejected an early-business-computer anchor (LEO I, 1951): reputable sources disagree on the date of its first routine job.

## Sources

- **Internal**
  - `PLAN.md`, `_research/style-guide.md`, `_research/scenario-ledger.md` — owners of terms, pattern names, Northmere facts.
  - [[introduction]], [[where-finance-architecture-goes-wrong]], [[meet-northmere]], [[long-term-evolution]], [[glossary]] and Part I chapters.
- **External** (all read on 18 November 2026; listed in the article's Sources and Evidence)
  - ICAEW Library, *Summa de arithmetica* — Venice, 1494; double-entry bookkeeping section.
  - U.S. SEC, "About the Securities Laws" — 1933, 1934 and 2002 acts.
  - EUR-Lex, Regulation (EC) No 1606/2002, Article 4 — IFRS from 2005.
  - SAP News Center, "The End of an Era: Hasso Plattner Steps Down" (2024) — 1972 founding, RF in 1973, R/3 in September 1992.
  - Computer History Museum, "Software: Putting PCs to Work" — VisiCalc, 1979.
  - European Commission, "VAT in the Digital Age" — in force 14 April 2025; digital reporting from 1 July 2030.

## Changelog

- **2026-11-18** — Initial spec and article, at the author's request ("add history page in finance-systems-architecture"); status `accepted` under the author's delegation for these pages. *(AI-mediated session)*
- **2026-11-18** — Independent verification (record in `_research/verification/how-finance-got-complicated.md`): 18 dated or quoted facts re-fetched, 3 wordings corrected, 1 unsourced date removed; Northmere facts and pattern names confirmed; 4,693 words. *(AI-mediated session)*
