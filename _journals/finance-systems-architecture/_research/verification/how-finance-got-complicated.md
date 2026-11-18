# Verification record: how-finance-got-complicated

Date: 2026-11-18. Independent fact-check of `posts/how-finance-got-complicated/index.md` against its cited sources, the style guide, the reviewer brief's evidence and consistency checks, the scenario ledger, the failure-patterns page, the glossary, PLAN "Owns", and Part I and long-term-evolution chapters. Every source below was re-fetched on 2026-11-18 (WebFetch, with curl to confirm exact wording).

## Dated and quoted facts

| # | Fact on the page | Source | Verdict | Note |
| --- | --- | --- | --- | --- |
| 1 | Pacioli's *Summa de arithmetica* printed in Venice in 1494 | https://www.icaew.com/library/library-collection/historical-accounting-literature/highlights-of-the-collection/summa-di-arithmetica | confirmed | "Printed by Paganino de Paganini (Venice; 1494)" |
| 2 | Treatise on double entry, the "Methods of Venice" | same | confirmed | "double-entry bookkeeping - the "Methods of Venice"" |
| 3 | Quote "remains in use today" (body) / "which remains in use today" (sources) | same | confirmed | "the system of accounting which remains in use today" |
| 4 | Securities Act of 1933, quote "financial and other significant information concerning securities being offered for public sale" | https://www.sec.gov/about/about-securities-laws | corrected | Quote verbatim, but the SEC's objective is to "require that investors receive" that information; framing changed to "requiring that investors receive …" |
| 5 | Securities Exchange Act of 1934, quote "empowers the SEC to require periodic reporting of information by companies with publicly traded securities" | same | confirmed | Verbatim |
| 6 | Sarbanes-Oxley Act of 2002, quote "enhance financial disclosures and combat corporate and accounting fraud" | same | corrected | Quote verbatim; the SEC says the Act "mandated a number of reforms to …", page said it "aimed to" (attributed purpose). Now "mandated reforms to" |
| 7 | SOX: management assesses ICFR yearly; larger companies' auditors attest | sourced in [[controls-and-auditability]] (sections 404(a)/(b)) | confirmed | Agrees with ch. 08 and glossary ICFR row |
| 8 | Regulation 1606/2002, consolidated accounts under international standards "for each financial year starting on or after 1 January 2005" | https://eur-lex.europa.eu/eli/reg/2002/1606/oj | confirmed | Article 4, verbatim; applies to companies with securities admitted to a regulated market ("listed") |
| 9 | SAP's RF, first financial accounting system, 1973; the "R" "stood for 'real time'" | https://news.sap.com/2024/05/the-end-of-an-era-hasso-plattner-steps-down/ (2024-05-13) | confirmed | "In 1973, the entrepreneurs launched RF, their first financial accounting system. The "R" in the name stood for "real time."" |
| 10 | September 1992: R/3 "within six weeks to anyone who ordered it there and then" | same | confirmed | Sapphire, Orlando, September 1992; verbatim. "Client-server" is in the same article |
| 11 | SAP founded 1 April 1972 (Sources entry only) | same | confirmed | "on April 1, 1972" |
| 12 | VisiCalc, 1979, "the first spreadsheet for personal computers" | https://www.computerhistory.org/revolution/personal-computers/17/305 | confirmed | Also "a 1979 spreadsheet program by Software Arts" |
| 13 | VisiCalc thirteen years before R/3 was announced | derived (1979, 1992) | confirmed | Arithmetic |
| 14 | "The spreadsheet reached desks before the integrated ERP did" | SAP and CHM pages | corrected | Only R/3 (1992) is sourced; integrated mainframe suites are not dated on the page. Now "before client-server suites such as R/3 did" |
| 15 | "By the mid-twentieth century" large companies outgrew clerks | none read | removed | Unsourced date (the Sources section says punched-card bookkeeping has no source); sentence kept without the date |
| 16 | ViDA entered into force 14 April 2025 | https://taxation-customs.ec.europa.eu/taxation/vat/vat-digital-age-vida_en | confirmed | "Upon entry into force (14 April 2025)" |
| 17 | ViDA digital reporting for cross-border B2B from 1 July 2030, based on e-invoicing | same | confirmed | "Digital Reporting Requirements will affect cross-border B2B transactions from 1 July 2030"; "real-time digital reporting for cross-border trade, based on e-invoicing" |
| 18 | Anchor ages in the timeline paragraph (over 500 years, about 90, under 50) | derived | confirmed | 1494, 1933/34, 1979/1992 |

## Counts

- Dated and quoted facts checked: 18; confirmed: 14; corrected: 3; removed: 1.
- Generalizations checked: 16 (cash box, partners, year-end and monthly close, railway shareholders, auditor sampling, subsidiaries per country, acquisitions kept as they were, punched cards, ERP posting, ERP customization, spreadsheet use, systems around the ledger, PSP net settlement, vendor cloud releases, several ERPs after acquisitions, tax authorities wanting invoices as data). All marked as illustration or common practice or sourced, except the mid-twentieth-century date (removed) and the "failure in one country stays there" rationale (cut for length; it was an unsourced reason). No unsourced "first" claims; the only "first" claims are quoted from SAP and the Computer History Museum. One attributed purpose fixed (SOX "aimed to").
- Failure-pattern names in the tally: 14 of 14, each exactly once, names identical to the headings of `where-finance-architecture-goes-wrong`.
- Term links checked: 35 `[[…]]` occurrences, 20 distinct permalinks, all in the style guide's valid list. Owners agree with the glossary "Chapter" column or PLAN "Owns": journal entry, double entry, subledger, accrual, trial balance, translation → accounting-for-architects; reconciliation → traceability-and-reconciliation; SoD, IPE, ICFR, audit trail, external auditor → controls-and-auditability; period close, cut-off → finance-processes; legal entity, intercompany → global-scale; consolidation, elimination → onestream; book of record, volume gradient → finance-landscape; EUC → technical-debt-and-fitness; PSP → payments-fundamentals; clearing account → payments-to-ledger; satellite platform → satellite-platforms; interfaces/control totals → integration-architecture. Accounting standards are linked to accounting-for-architects (multi-GAAP is owned by global-scale); acceptable for a first mention, left unchanged.
- Consistency with Part I and ch. 43: trial balance proves the arithmetic, not the truth (agrees with ch. 05); SOX 404 description agrees with ch. 08; volume gradient and 38,000 lines agree with ch. 04; 71 entities in 38 countries and ViDA dates agree with ch. 10 and ch. 43. No contradictions found.
- Northmere facts checked: 17 (€600; 12 March 2027; Adyen; stay 18–21 April; €1.74 fee; inside a larger batch; Northmere Payments B.V. bank credit 16 March; SFP; €90 commission; €510 owed; ~38,000 GL lines a day; S/4HANA as group ledger; BlackLine matching PSP vs bank vs platform; 71 entities from three ERPs into US dollars; payout 26 April; €14 million average month-end in clearing/suspense in 2026; nine-working-day close; traveler from Germany; 38 countries; listed in New York). Two corrected: "nine-day monthly close" → "nine-working-day"; "sells in 38 countries" → "trades through companies in 38 countries" (ledger: 71 legal entities in 38 countries; ch. 10 wording).
- Figures: 10 captions checked against the text; all agree.

## Edits made to index.md

1. Lead: "a nine-day monthly close" → "a nine-working-day monthly close".
2. Securities Act 1933: "as requiring \"financial …\"" → "as requiring that investors receive \"financial …\"".
3. Machine step: "By the mid-twentieth century large companies recorded more …" → "Large companies came to record more …" (unsourced date removed).
4. Sarbanes-Oxley: "which the SEC says aimed to \"enhance …\"" → "which the SEC says mandated reforms to \"enhance …\"".
5. Spreadsheet step: "before the integrated ERP did" → "before client-server suites such as R/3 did".
6. Today step: "The group sells in 38 countries" → "The group trades through companies in 38 countries".
7. Length (the page measured over 4,700 words after the fixes): removed "and a failure in one country stays there" (group step), "and a manager sees this week's numbers this week" (machine step), "and whoever asked gets the answer this month" (spreadsheet step), and the Sources sentence "The anchors come from Italy, the United States, Germany and the European Union." Final count 4,693 words.
