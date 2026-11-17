# Verification — 05-payment-economics (`payment-economics`)

Verification pass of 17 November 2026. Every source below was fetched in this session (curl; `.md` variants for docs.stripe.com and docs.adyen.com; SEC with the research-bot User-Agent; the EU regulation through `publications.europa.eu/resource/celex/32015R0751` with `Accept: application/xhtml+xml`; the Stripe letter and the Adyen shareholder letter as the PDFs linked from their landing pages). Quotations were compared with the fetched text by script, typographic quotes aside.

Short names for sources: **S-price** = stripe.com/en-nl/pricing; **S-ext / S-inc / S-multi / S-over / S-part** = docs.stripe.com/payments/{extended-authorization, incremental-authorization, multicapture, overcapture, partial-authorization}; **S-opt** = docs.stripe.com/payments/analytics/optimization; **S-ref** = docs.stripe.com/refunds; **S-letter** = stripe.com/en-nl/annual-updates/2025 (PDF); **A-price** = adyen.com/pricing; **A-visa** = adyen.com/payment-methods/visa; **A-adj** = docs.adyen.com/online-payments/adjust-authorisation; **A-vif** = docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees; **A-refusal** = docs.adyen.com/development-resources/refusal-reasons; **A-disp** = docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow; **A-cap / A-partial / A-fees** = docs.adyen.com/online-payments/capture, /online-payments/partial-authorizations, /platforms/online-payments/transaction-fees; **A-H1** = Adyen H1 2026 press release; **A-H1-SL** = investors.adyen.com/financials/h1-2026-c2a1a (PDF, 46 pages); **A-H2** = Adyen H2 2025 press release; **V-10K** = Visa Form 10-K, fiscal 2026; **M-10K** = Mastercard Form 10-K, 2025; **IFR** = Regulation (EU) 2015/751; **Fed-avg / Fed-about / Fed-2023** = the three Federal Reserve pages; **CFM** = Consumer Finance Monitor, 28 October 2026; **ABA** = ABA Banking Journal, 3 November 2026.

| # | Claim (short) | Source | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Adyen: you "can see exactly what you’re being charged for each transaction" | A-price (FAQ) | confirmed | — |
| 2 | Stripe contrasts IC+ with "a flat rate for all transactions" | S-ext (tooltip definition) | confirmed | — |
| 3 | "merchant discount rate" is the networks' term | V-10K ("merchant discount rate (MDR)"), M-10K | confirmed | Visa source entry now names it |
| 4 | Visa: "Generally, IRFs are paid by acquirers to issuers. We establish default IRFs…" | V-10K | confirmed | — |
| 5 | Visa 10-K is for fiscal 2026, filed November 2026 (5 Nov) | V-10K (fiscal year ended 30 September 2026; signatures dated November 5, 2026) | confirmed | — |
| 6 | Mastercard: "Although we do not earn revenues from interchange…" | M-10K | confirmed | — |
| 7 | Mastercard 10-K for 2025, filed February 2026 (11 Feb) | M-10K (dated February 11, 2026) | confirmed | — |
| 8 | Visa: "Payments volume is the primary driver for our service revenue…" | V-10K | confirmed | — |
| 9 | Visa: international transaction revenue "Earned for cross-border transaction processing and currency conversion activities" | V-10K | confirmed | — |
| 10 | Mastercard: "The merchant discount rate is established by the acquirer…" | M-10K | confirmed | — |
| 11 | Mastercard: "We administer the collection and remittance of interchange fees through the settlement process" | M-10K | confirmed | — |
| 12 | Interchange is decided by the clearing record, not the approval | none (labeled "industry practice" in the text) | not checked | No source fetched states it in general; the Adyen quote in claim 13 is the documented case. Left as labeled industry practice |
| 13 | Adyen: late capture risks "Increased interchange fees", "Card scheme transaction fees", a failed capture, a chargeback; "increases the risk of" | A-adj | confirmed | Source title corrected to "Authorization adjustment" |
| 14 | IFR Article 3 quote, 0,2 % debit | IFR | confirmed | — |
| 15 | IFR Article 4 "0,3 %" credit; member states may set lower domestic caps | IFR (Art. 3(2), Art. 4, recital 14) | confirmed | — |
| 16 | Caps do not apply to "transactions with commercial cards" or cards "issued by three party payment card schemes" | IFR Art. 1(3) | confirmed | — |
| 17 | IFR published 19 May 2015; evidence age 11 years | IFR (OJ L 123, 19.5.2015) | confirmed | — |
| 18 | IFR "in force" | — | not checked | The original text was read; the consolidated version on EUR-Lex returned an empty 202 response to curl. Claim kept (the regulation has no expiry clause in the text read) |
| 19 | IFR Article 9 quote (unblended charges unless requested in writing) | IFR | confirmed | — |
| 20 | IFR Article 12 quote; aggregation with the payee's consent | IFR | confirmed | — |
| 21 | Regulation II cap formula quote; page updated December 2025 | Fed-avg (Last Update: December 19, 2025) | confirmed | — |
| 22 | Cap applies to issuers "with $10 billion or more in assets" (October 2023) | Fed-2023 | confirmed | Source entry no longer mentions the 24.5-cent example, which the text does not use |
| 23 | US credit cards are not capped | Fed-about, Fed-avg (Regulation II covers debit only) | confirmed by the scope of the rule | No source states the negative in one sentence |
| 24 | 2024 averages: covered $0.23, exempt $0.51 | Fed-avg ("All networks" row) | confirmed | — |
| 25 | Routing rule quote ("less than two unaffiliated networks") | Fed-about (Last Update: May 17, 2024) | confirmed | — |
| 26 | Eighth Circuit, *Corner Post*, late October 2026, unanimous, upheld vacatur of the 21-cent standard | CFM, ABA (both secondary) | hedged | The sentence now says the account rests on two secondary sources. They differ on the day (CFM: 26 October; ABA: "Date: Oct. 27, 2026"); the page says "late October" |
| 27 | Decision "would not become effective until issuance of the mandate" | CFM | confirmed (secondary source, attributed) | — |
| 28 | Visa: "Recent conflicting federal court decisions on the validity of Regulation II's interchange fee standard" | V-10K | confirmed | — |
| 29 | Credit settlement preliminarily approved "on June 9, 2026"; no final approval | V-10K | corrected | Page said "I found no final approval". The 10-K says the plaintiffs moved for final approval on July 15, 2026 and reports none; the sentence now says so |
| 30 | Stripe NL card prices: 1.5% + €0.25 standard EEA, 2.8% + €0.25 premium EEA, 2.5% + €0.25 UK, 3.15% + €0.25 international, "+ 2% if currency conversion is required" | S-price | confirmed | — |
| 31 | EEA = EU plus Iceland, Liechtenstein, Norway | — | not checked | General knowledge; no source fetched |
| 32 | Stripe IC+ definition quote | S-ext, S-inc, S-multi, S-over, S-part, S-opt | confirmed | — |
| 33 | Stripe: "No setup fees, monthly fees, or hidden fees" | S-price | confirmed | — |
| 34 | Stripe Custom column: "available for businesses with large payments volume or unique business models", lists "IC+ pricing" | S-price | confirmed | — |
| 35 | Stripe's IC+ markup is not published | S-price; docs.stripe.com/llms.txt searched for "IC+", "interchange", "pricing" | confirmed as far as searched | — |
| 36 | Adyen: "For each transaction, we charge a fixed processing fee + a fee determined by the payment method." | A-price | confirmed | — |
| 37 | Adyen: processing fee $0.13, "Interchange+ + 0.60%" for Visa and Mastercard | A-price, A-visa, adyen.com/payment-methods/mastercard | confirmed | Added "in the rows marked Global": the page also has country rows (for example Denmark, Finland, Norway) with other amounts |
| 38 | Adyen: "Interchange fees are variable, our Interchange++ pricing passes these fees directly to you" | A-price, A-visa | confirmed | — |
| 39 | Adyen: "The fees outlined above are indicative"; "We do have a minimum invoice depending on industry or business model" | A-price (FAQ) | confirmed | — |
| 40 | Some Adyen methods carry a fixed percentage | A-price (for example "$0.13 + 4%") | confirmed | — |
| 41 | Stripe blocks a payment "that would have incurred network retry penalties" | S-opt | confirmed | — |
| 42 | Stripe: "We block payments that are unlikely to succeed before they reach the card networks, saving you unnecessary scheme fees." | S-opt | confirmed | — |
| 43 | Adyen: "Visa charges system integrity fees. These fees are related to excessive retries…" | A-vif | confirmed | — |
| 44 | Adyen refusal reason 46 blocks a retry | A-refusal ("Transaction blocked by Adyen to prevent excessive retry fees") | confirmed | — |
| 45 | Stripe: "an additional 0.08% fee per transaction" for extended authorization "in some merchant categories" | S-ext (footnote to the Visa row "All other merchant categories") | corrected | The fee is stated for Visa only, outside hotel, lodging, vehicle rental and cruise line. Text and table cell now say so; "merchant category" glossed |
| 46 | Stripe: "Stripe’s processing fees from the original transaction aren’t returned." | S-ref | confirmed | — |
| 47 | Stripe: "IC+ users might see a difference in cost between reversals and refunds because reversals usually incur lower network fees." | S-ref (the rendered sentence; the `.md` variant carries the IC+ tooltip inline) | confirmed | — |
| 48 | Adyen price list has a "Payment method refund fee" column | A-price (label in the page data; shown under the Refund toggle) | confirmed | Not visible in the static text of the page; found in the embedded page data |
| 49 | Stripe NL dispute fees: "€20.00 for each dispute you receive", €20.00 "for each dispute you respond to manually", "You get this fee back for won disputes", "In rare cases, network fees also apply." | S-price | confirmed | — |
| 50 | Adyen "debits the payment amount and the chargeback processing fee from your account" | A-disp | confirmed | Source title corrected to "Dispute flow" |
| 51 | Adyen's chargeback fee amount is not public | A-price, A-disp, docs.adyen.com/llms.txt searched for "chargeback fee" | confirmed as far as searched | — |
| 52 | Adyen: "Interchange++ is a pricing model which accurately tracks Interchange rates and scheme fees right down to a transaction level…" | A-price (FAQ) | confirmed | — |
| 53 | Five Stripe pages carry the "IC+ feature" label; what each feature does; extended authorization up to 30 days | S-ext ("IC+ Feature"), S-inc, S-multi, S-over, S-part | confirmed | — |
| 54 | "We offer extended authorizations to users on IC+ pricing. If you’re on blended Stripe pricing and want access to this feature, contact us" | S-ext | confirmed | — |
| 55 | Stripe: "Optimization features can help reduce network costs for businesses on IC+ pricing"; "Stripe uses interchange and scheme fee rules…to compute costs you would have incurred…" | S-opt | confirmed | Source title corrected to "Payments optimization" |
| 56 | "for businesses on IC+ Stripe computes what they saved" | S-opt | hedged | The page calls the figures estimates and says Stripe "doesn’t reconcile these estimates directly with the fees applied to your account". "computes" changed to "estimates" |
| 57 | Authorisation Boost: "Included at no additional charge for businesses on standard payments pricing"; "0.2% per successful online card transaction for accounts with custom payments pricing" | S-price | confirmed | — |
| 58 | Adyen equivalents enabled by support and by merchant category, no pricing-plan condition | A-adj, A-cap, A-partial | confirmed | A-cap and A-partial added to Sources (they were read by the writer but not listed) |
| 59 | Adyen net revenue definition quote ("Net non-interest revenue (…) and Net interest income") | A-H1-SL, non-IFRS measures note | confirmed | — |
| 60 | Deducted costs are those "that do not form part of the passthrough settlement fees" | A-H1-SL, note 1 | corrected | The PDF reads "pass-" at a line end and "through" on the next line, so the quoted spelling could not be matched. The clause is now a paraphrase without quotation marks |
| 61 | "Net revenue was €1,302.9 million, up 19% year-on-year"; "Processed volume was €803.8 billion, up 24% YoY"; 13 August 2026 | A-H1 | confirmed | — |
| 62 | "Take rate landed at 16.2 bps, reflecting expected volume tiering…"; letter unaudited | A-H1-SL | confirmed | 1,302.9 ÷ 803,800 = 16.2 basis points |
| 63 | Stripe letter: "$1.9 trillion in total volume, up 34% from 2024, and equivalent to roughly 1.6% of global GDP"; "Stripe remained robustly profitable"; 24 February 2026 | S-letter (PDF) | confirmed | The PDF text reads "February 24, 202" (last digit not extracted); the year follows from the letter's subject |
| 64 | "The letter gives no revenue figure" | S-letter (PDF) | corrected | The letter gives one revenue number, for a product family: the Revenue suite is "on track to hit an annual run rate of $1 billion this year". The sentence now says no figure for the company's revenue and quotes that one |
| 65 | Adyen 2025: processed volume "up 21% excluding a single large-volume customer, or 8% YoY including this customer"; net revenue up 18%; 12 February 2026 | A-H2 (full-year key metrics) | confirmed | — |
| 66 | Where They Differ, row 1 (defaults) | claims 30, 36–39 | confirmed | — |
| 67 | Where They Differ, row 2 (the other model) | claims 34, 35, 39, 40; A-fees | confirmed | Adyen cell gained a documented fact: the platform documentation defines a fee type "AdyenCommission" as "The transaction fee due to Adyen under blended rates" |
| 68 | Where They Differ, rows 3–4 (refunds, dispute fee) | claims 46, 48–51 | confirmed | — |
| 69 | Where They Differ, row 5 (features and plan) | claims 53, 57, 58 | confirmed | — |
| 70 | Where They Differ, row 6 (financials) | claims 61–64 | confirmed | "H1 2026" written out |
| 71 | KEY POINTS and "Established" bullets | claims 4, 6, 10, 14–16, 19, 30, 37, 53, 62 | confirmed | — |
| 72 | New sentence: Adyen's processing costs are "also applicable to refused and cancelled payments" | A-fees | confirmed (added) | Added to the paragraph on declines; it answers a spec open question |

Counts: 72 claims; 61 confirmed, 4 corrected (29, 45, 60, 64), 2 hedged (26, 56), 0 unsupported, 0 unreachable, 3 not checked (12, 18, 31), 2 confirmed only as far as a search can show a negative (35, 51).

## Could not verify, and what was done

- **Claim 12** (interchange follows the clearing record): no fetched source states the general rule. It was already labeled industry practice; left.
- **Claim 18** (the regulation is in force): only the 2015 text was read. EUR-Lex's HTML endpoint returned HTTP 202 with an empty body to curl.
- **Claim 31** (EEA membership): not fetched.
- **Eighth Circuit opinion**: not read; two secondary sources that differ by a day on the date of the decision. The page says "late October 2026" and names both as secondary.
- **Documentation page age**: the Adyen pages "Authorization adjustment" and "Transaction fees" carry `last_modified` metadata of 2 August 2023 and 28 April 2023. The pages display no date, so they stay "n.d., accessed 2026-11" (ruling 25); the author may want an evidence-age note.

## Links

All URLs under Sources and Evidence returned HTTP 200 in this session. `http://publications.europa.eu/resource/celex/32015R0751` answers 400 or 404 to a request with `Accept: text/html` alone and 200 with `Accept: application/xhtml+xml` (as a browser sends). The Adyen investor page and the Stripe letter page are landing pages; the quoted text is in the PDFs they link to (noted in the entries). All `[[permalinks]]` are in the style guide's list.

## Larkfield

All figures recomputed and compared with the ledger (general figures, "Mila's class pass", "The €120 dispute", the three `05-payment-economics` additions): no differences. One label added: the fee-stack table called Adyen "the acquirer"; the ledger (`01-journey-of-a-payment`) requires that to be labeled as inference, so the cell now reads "the acquirer, by inference".

## Ledger conflicts

None found.

## For other pages

- **`journal-spec.json`, entry `payment-economics`, `thesis.how_why` (line 1210), and its copy `_research/journal-spec-parts/part-1.json` (line 527)**: says Stripe's Netherlands price list "charges 1.5% + €0.25 per successful payment on a standard European card". The page does not use "per successful" for online card payments. Its exact wording, under the heading "Domestic cards", is **"1.5% + €0.25 for standard European Economic Area cards"** (the same string appears in the Standard summary column). "per successful" appears on that page only for Klarna ("per successful transaction for Klarna"), Authorisation Boost ("per successful online card transaction"), the Foreign Exchange Quotes API, Managed Payments, Terminal ("per successful charge") and Financial Connections. Suggested wording: "prices a standard European Economic Area card at 1.5% + €0.25". The post's `spec.json` carries the same sentence in `thesis.how_why`; it was **not** changed, because `validate_spec.py` fails with "thesis.how_why: differs from the journal spec" unless both files change together.
- Any page that says a declined attempt is free on Adyen: Adyen's "Transaction fees" page says processing costs are "also applicable to refused and cancelled payments".
