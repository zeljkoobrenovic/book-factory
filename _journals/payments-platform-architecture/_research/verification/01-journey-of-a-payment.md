# Verification — 01-journey-of-a-payment (`journey-of-a-payment`)

Verification pass of 17 November 2026. Every source below was fetched in this session (curl; Stripe and Adyen documentation through the `.md` variants; the Visa rules PDF converted with `pdftotext`; SEC filings with the research-bot User-Agent; the EU regulation from the Publications Office with `Accept: application/xhtml+xml`; Adyen's Annual Report 2025 as the PDF linked from the investor page). Quotations were compared as strings after normalizing typographic quotes and white space.

Short source names: **V10K** = Visa Form 10-K fiscal 2026 (sec.gov, dated 5 November 2026); **MA10K** = Mastercard Form 10-K 2025 (sec.gov, dated 11 February 2026); **VR** = Visa Core Rules and Visa Product and Service Rules, 24 October 2026 (usa.visa.com PDF); **EU751** = Regulation (EU) 2015/751 (publications.europa.eu/resource/celex/32015R0751); **AR25** = Adyen Annual Report 2025 (PDF linked from investors.adyen.com/financials/2025).

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe: "A `succeeded` status indicates … refunded, disputed, returned, or reversed" | docs.stripe.com/payments/payment-methods | confirmed | — |
| 2 | Visa: "transaction processing services … “four-party” model" | V10K | confirmed | — |
| 3 | Visa report is for fiscal 2026, filed November 2026 | V10K | confirmed | Signature date 5 November 2026 |
| 4 | Mastercard: "account holder … issuer … merchant and acquirer (the merchant's financial institution)" | MA10K | confirmed | — |
| 5 | Mastercard report is for 2025, filed February 2026 | MA10K | confirmed | Signature date 11 February 2026 |
| 6 | Visa: "Visa is not a financial institution. We do not issue cards …" | V10K | confirmed | — |
| 7 | Mastercard: "We do not issue cards, extend credit, determine or receive revenue …" | MA10K | confirmed | — |
| 8 | Visa rules, edition of 24 October 2026: Acquirer is "A Member that signs a Merchant or Payment Facilitator …" | VR (glossary) | confirmed | — |
| 9 | Stripe services terms: acquirer is authorized to "receive and remit settlement funds for authorized and cleared Transactions" | stripe.com/legal/ssa-service-terms | confirmed | URL in Sources replaced: `/en-us/legal/ssa-services-terms` now redirects (301) to `/legal/ssa-service-terms` |
| 10 | Adyen: "Acquirers must be licensed by local financial regulators and card schemes to relay transactions." | adyen.com/knowledge-hub/acquiring-bank | confirmed | — |
| 11 | Visa: Acquirer Processor is "A non-Member agent or processor that a Member has engaged" | VR (glossary) | confirmed | — |
| 12 | Visa: Payment Facilitator is "An entity that contracts with an Acquirer to deposit Transactions …" | VR (glossary) | confirmed | — |
| 13 | A payment facilitator is registered with the network by its acquirer | VR section 5.3.1.3 | confirmed | — |
| 14 | Visa will "indemnify issuers and acquirers for settlement losses …" | V10K | confirmed | — |
| 15 | Mastercard: "We do not, however, guarantee payments to merchants by their acquirers" | MA10K | confirmed | — |
| 16 | Mastercard's three services: "we enable the routing of a transaction … settlement banks chosen by us and our customers" | MA10K | confirmed | — |
| 17 | Visa: acquirer passes the transaction to Visa, "which in turn sends the transaction data to the issuer …" | V10K | confirmed | — |
| 18 | Adyen: "By default, payments are captured automatically without a delay, immediately after authorization of the payment request." | docs.adyen.com/online-payments/capture | confirmed | Words match; the source has link markup on "captured" and "authorization" |
| 19 | Visa: at most 10 calendar days to process a cardholder-initiated card-absent transaction | VR Table 5-11 (section 5.7.3.5) | confirmed | Timeframe starts on the date of a valid authorization (footnote 1) |
| 20 | Visa: a presentment is "A Clearing Record that an Acquirer presents to an Issuer through Interchange" | VR (glossary) | confirmed | The quotation is the opening of the definition, which continues "either initially (a first Presentment) or after a Dispute …" |
| 21 | In the rulebook "Interchange" is the exchange of records, not the fee | VR (glossary: "The exchange of Clearing Records between Members") | confirmed | — |
| 22 | Clearing is the network's processing of those records | VR (glossary: "A processing service for the validation and valuation of financial and non-financial records exchanged between Visa and Members") | confirmed | Paraphrase |
| 23 | Visa: settlement is "The reporting and funds transfer of Settlement Amounts owed by one Member to another, or to Visa, as a result of Clearing" | VR (glossary) | confirmed | — |
| 24 | Visa: settlement amount is "The daily net amounts expressed in a Member's Settlement Currency resulting from Clearing" | VR (glossary) | confirmed | — |
| 25 | Visa: issuer "effectively pays the acquirer an amount equal to the value of the transaction, minus the interchange reimbursement fee (IRF)" | V10K | confirmed | — |
| 26 | Stripe: "Stripe uses “T” to refer to the transaction time …" | docs.stripe.com/payouts | confirmed | — |
| 27 | Stripe: "Some payment processors might start “T” from their internal settlement time …" | docs.stripe.com/payouts | confirmed | — |
| 28 | Adyen for Platforms: "sales day settlement model" | docs.adyen.com/platforms/settle-funds | confirmed | — |
| 29 | Adyen: "the funds you get do not depend on the settlement timelines of the schemes and payment methods used by your shoppers"; Sales day payout is the default payout model | docs.adyen.com/account/sales-day-payout | confirmed | — |
| 30 | Adyen terms (last updated 17 June 2024): payout "irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner" | adyen.com/legal/sales-day-payout-terms-of-service | confirmed | Page shows "Last update 17 June 2024" |
| 31 | Visa: "120 calendar days from the Transaction Processing Date" for most kinds of dispute | VR chapter 11 (dispute conditions) | confirmed | 120 days is the limit in the majority of dispute conditions; some have 75 days and several count from one of two dates. "Most kinds" is accurate |
| 32 | Adyen: "In general, a cardholder has a maximum of 120 calendar days from the transaction date to dispute a transaction" | docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes | confirmed | — |
| 33 | Adyen: "In some cases for Visa and Mastercard, the cardholder has a maximum of 540 calendar days" | same | confirmed | — |
| 34 | Mastercard's rules could not be read (HTTP 403) | mastercard.us rules PDF and chargeback guide | confirmed | Both returned 403 again in this pass |
| 35 | EU 2015/751: "‘three party payment card schemes’ … and ‘four party payment card schemes’ …" | EU751 recital 28 | confirmed | — |
| 36 | EU 2015/751 is 11 years old and still in force | EU751; Publications Office metadata notice | confirmed | Published OJ L 123, 19.5.2015; metadata `RESOURCE_LEGAL_IN-FORCE` = true. EUR-Lex itself answers robots with HTTP 202 and an empty page |
| 37 | EU 2015/751: a three-party scheme that licenses others "is considered to be a four party payment card scheme" | EU751 Article 2(18) | confirmed | — |
| 38 | Stripe: a card network "might be an intermediary in front of an issuing bank as with Visa or Mastercard, or a standalone entity as with American Express" | docs.stripe.com/disputes/how-disputes-work | confirmed | — |
| 39 | Stripe: "Customers can't dispute iDEAL \| Wero payments with their bank." | docs.stripe.com/payments/ideal | confirmed | — |
| 40 | Stripe: SEPA Direct Debit can be disputed "without providing a reason for up to 8 weeks after the debit" | docs.stripe.com/payments/sepa-debit | confirmed | — |
| 41 | Adyen: "You cannot defend SEPA chargebacks." | docs.adyen.com/payment-methods/sepa-direct-debit | confirmed | — |
| 42 | Stripe: wallet pays with "A saved payment credential (a tokenized card or bank account stored in the wallet)" | docs.stripe.com/payments/wallets | confirmed | — |
| 43 | Stripe: or "A stored wallet balance (funds held in an account with the wallet provider)" | same | confirmed | — |
| 44 | Adyen: Apple Pay "uses network tokenization" | docs.adyen.com/payment-methods/apple-pay | confirmed | — |
| 45 | Adyen: Apple Pay "supports liability shift for American Express, Discover, JCB, Mastercard, and Visa cards" | same | confirmed | One-clause definition of "liability shift" added (term was used undefined) |
| 46 | Visa section 5.3.1.2: acquirer "liable for all acts, omissions, and other adverse conditions caused by the Payment Facilitator and its Sponsored Merchants" | VR 5.3.1.2 | confirmed | — |
| 47 | Stripe, April 2020: "now processes card transactions through direct integrations with all six major card networks in North America, Latin America, Europe and Asia Pacific"; evidence age 6 years | stripe.com/en-ca/newsroom/news/direct-platform | confirmed | Page metadata date 2020-04-23 |
| 48 | Stripe US: "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers", five banks and one Stripe entity | stripe.com/en-us/legal/acquirer-disclosure | confirmed | Cross River Bank, Deutsche Bank Trust Company Americas, Fifth Third Bank, Pathward N.A., PNC Bank N.A., Stripe MALPB |
| 49 | Stripe Technology Europe Limited is "authorised as an electronic money institution by the Central Bank of Ireland" (2019; evidence age 7 years) | stripe.com/legal/stel | confirmed | Page shows "Last updated: April 5, 2019". URL in Sources replaced: `/stel/legal` redirects (301) to `/legal/stel` |
| 50 | The entity is named in the current acquirer disclosure | stripe.com/en-us/legal/acquirer-disclosure | confirmed | — |
| 51 | Adyen N.V. is "authorised as a credit Institution under the supervision of Dutch Central Bank", a "banking license" | adyen.com/licenses/emea | confirmed | — |
| 52 | Stripe, EEA: "Payment Method Acquirer is Stripe Technology Europe, Ltd." | stripe.com/en-us/legal/acquirer-disclosure | confirmed | The disclosure section is headed "Visa and Mastercard Transactions" |
| 53 | Adyen publishes "no list per country" / "no such list" (KEY POINTS, table row 2, Larkfield cast paragraph) | docs.adyen.com/account/supported-currencies | **corrected** | The page said Adyen publishes no list. Adyen's documentation does list 14 countries and regions with an "Adyen acquiring connection" (AU, HK, IN, JP, MY, NZ, SG, EU, UK, CA, US, BR, MX, UAE) and says a payment goes "through one of our acquiring entities, for example Adyen Singapore". It does not name the acquiring entity per country. KEY POINT 3, the table cell, the sentence after the table and the Larkfield paragraph now say this; source entry added |
| 54 | Adyen's license "includes the ability to provide cross-border acquiring, payment and banking services in all EEA countries" | adyen.com/licenses/emea | confirmed | — |
| 55 | Adyen US: "Adyen N.V. San Francisco Branch is a federal Branch of Adyen, N.V., licensed by the Office of the Comptroller of the Currency and the Federal Reserve Board of Governors" | adyen.com/licenses/united-states | confirmed | The cell now also gives the page's heading, "USA Acquiring" |
| 56 | Adyen US: acquirer of record per payment "Not public" | adyen.com/licenses (all ten regional pages), docs.adyen.com/llms.txt, adyen.com/global-acquiring | confirmed | Searched; no page names the acquirer of record for a US payment. The heading "USA Acquiring" over the branch statement is the nearest public statement and is now in the cell |
| 57 | Stripe is a payment facilitator of "named banks" in the US, Canada, Japan and Thailand; a "Payment Aggregator" of a bank in India | stripe.com/en-us/legal/acquirer-disclosure | **corrected** | "Banks" was wrong for Japan (Sumitomo Mitsui Card Co., Ltd. and JCB Co., Ltd. are card companies): now "named acquirers". Two disclosed cases were missing and are added: Mexico ("both a Payment Method Acquirer and a Payment Facilitator") and the United Arab Emirates ("an Independent Sales Organization (ISO)" of Network International) |
| 58 | Adyen: "Of processed volumes, 84% were full-stack volumes" (Annual Report 2025, March 2026) | AR25 | confirmed | Report dated 5 March 2026; "up from 83% in 2024" |
| 59 | Adyen: banking partners "are used" "in locations where there are no own direct acquiring licenses" | AR25, risk management (concentration risk) | **hedged** | The sentence in the report is about concentration risk: "Concentration risk at Adyen originates primarily at banking partners in locations where there are no own direct acquiring licenses." The cell now quotes it as a risk statement, and "Where the public record stops" says that reading it as a statement about acquiring is the author's inference |
| 60 | Adyen: which locations use banking partners is "Not public" | AR25; docs.adyen.com/account/supported-currencies; adyen.com/licenses | confirmed | Searched. The documentation lists where Adyen has acquiring connections, not where a banking partner stands behind one |
| 61 | Stripe: the Netherlands is listed at 7 calendar days initially and 3 business days by default | docs.stripe.com/payouts | confirmed | — |
| 62 | Stripe paragraph: 7 calendar days "for an account's first payouts" | docs.stripe.com/payouts | **corrected** | Stripe: "The initial settlement timing applies to your first payout". "first payouts" changed to "first payout" |
| 63 | Adyen: typically 2 business days where at least 80% of transactions are in a listed currency such as EUR and acquired in its region | docs.adyen.com/account/sales-day-payout | confirmed | — |
| 64 | Stripe says "card network", Adyen "card scheme" and "shopper" | Stripe and Adyen documentation pages above | confirmed | — |
| 65 | "no public page answers it" (Adyen's acquirer per market) | as 53 | **hedged** | Now "no public page names the acquiring entity or says where a banking partner stands behind it" |
| 66 | Neither company publishes its class of network membership per country | stripe.com acquirer disclosure; adyen.com/licenses pages; docs.stripe.com/llms.txt; docs.adyen.com/llms.txt | confirmed | Absence claim: no hit for "principal member", "membership" or similar in the two documentation indexes or the fetched legal pages. An absence cannot be proven; the search is what was done |
| 67 | Stripe names its US banks without volume shares | stripe.com/en-us/legal/acquirer-disclosure | confirmed | — |
| 68 | Adyen's report does not define "full-stack" where it gives the 84%, nor name who acquires the rest | AR25 (full-text search) | confirmed | "full-stack" occurs once in the report; elsewhere the report describes "the full payments stack (gateway, risk management, processing, acquiring and settlement)" |
| 69 | Only Adyen's terms say whether a payout waits for the network's money; Stripe's payout page does not say either way | docs.stripe.com/payouts; Adyen terms | confirmed | Searched the Stripe page for settle, receive funds, advance, pre-fund, card network: no statement |
| 70 | Stripe's disclosure links each bank's own acquirer terms (inside the INFERENCE block) | stripe.com/en-us/legal/acquirer-disclosure | confirmed | — |
| 71 | EU 2015/751 caps consumer debit interchange at 0.2% | EU751 Article 3(1) | confirmed | — |
| 72 | Adyen names no acquirer per country (Larkfield cast paragraph) | as 53 | **hedged** | Sentence now adds that the documentation lists the European Union as an acquiring connection; the acquirer of record stays labeled as inference |
| 73 | Visa's rule counts from the processing date (Larkfield note on 7 July) | VR | confirmed | — |
| 74 | Payout on the second business day matches the delay Adyen documents for euro payments acquired in the region | docs.adyen.com/account/sales-day-payout | confirmed | — |
| 75 | Stripe's disclosure names Stripe Technology Europe, Ltd. for the EEA; Stripe's clock counts from capture ("Had Studio Noord been on Stripe") | acquirer disclosure; docs.stripe.com/payouts | confirmed | — |
| 76 | Take-aways: four-party structure and three services in the 2026 reports; daily net settlement (Visa rules, October 2026); guarantee stops at the acquirer (Mastercard, 2026); about 120 days | V10K, MA10K, VR, Adyen dispute timeframes | confirmed | Restatements of claims above |
| 77 | Take-aways: Stripe is the acquirer in the EEA and a payment facilitator of banks in the United States | acquirer disclosure | confirmed | — |
| 78 | Take-aways: never for iDEAL, eight weeks without a reason for SEPA Direct Debit, about 120 days for a card | Stripe iDEAL and SEPA pages; VR; Adyen | confirmed | — |

**Totals: 78 claims checked — 72 confirmed, 3 corrected (53, 57, 62), 3 hedged (59, 65, 72), 0 unsupported, 0 unreachable.**

## "Where They Differ" table, cell by cell

- Row 1 (regulated form): Stripe cell = claims 49–50; Adyen cell = claim 51.
- Row 2 (acquirer of record, EEA): Stripe = 52; Adyen = 53–54 (corrected).
- Row 3 (United States): Stripe = 48; Adyen = 55–56.
- Row 4 (where own acquiring stops): Stripe = 57 (corrected); Adyen = 58–60 (59 hedged).
- Row 5 (payout clock): Stripe = 26, 61; Adyen = 29, 63.
- The seven inline links in the table were reduced to plain attributions (ruling 22); every URL is in Sources and Evidence.

## Links

All 26 URLs in Sources and Evidence return HTTP 200. Changed: `https://stripe.com/stel/legal` → `https://stripe.com/legal/stel` (301) and `https://stripe.com/en-us/legal/ssa-services-terms` → `https://stripe.com/legal/ssa-service-terms` (301); both replaced. `https://stripe.com/en-us/legal/acquirer-disclosure` answers with temporary (307) redirects to a locale chosen by the reader's location; kept. The EU regulation URL needs a browser-style `Accept` header (it returns 400 or 404 to a bare request); kept, as the brief prescribes it. All `[[permalinks]]` are in the style guide's valid list; the render check reports three as unresolved only because those pages (`journey-card-payment`, `meet-larkfield`, `where-payment-systems-go-wrong`) are not written yet.

## Could not verify, and what was done

- **Mastercard's own rules** (403). The page already cites Mastercard's dispute window through Adyen's documentation and says so; no change.
- **EUR-Lex** returns an empty page to robots. The regulation's text and its in-force status were read from the Publications Office instead.
- **Absence claims** (56, 60, 66, 68, 69) are confirmed only as "searched and not found" in the pages and indexes named.
- **Industry-practice tables** (the name table, who holds the money, the six-step times, the three provider positions) are labeled in the text as common usage, generalization, typical practice or the author's judgement; only their quoted cells were checked as claims.

## Format and rulings

- Ruling 22 applied (table links removed). Rulings 3, 11, 12, 14, 17 and 18 hold on the page.
- `timetoread` changed from 26 to 27 (6,110 words ÷ 230 = 26.6).
- No unit added, dropped, merged or reordered; `validate_spec.py` and `check_draft.py structure` pass.

## Larkfield consistency

Checked against the ledger: dates and weekdays (Tuesday 9, Wednesday 10, Thursday 11, Friday 12 March 2027; Monday 14 September 2026), €120.00, fee €2.53, €117.47, interchange cap €0.24, 7 July 2027 (120 days from 9 March), method mix 21% + 14% = 35% and 52%, the five states, cast and roles, K2, and the five incidents cited (figures and dates agree). No contradiction found.

## Ledger conflicts

None.

## For other pages

- `06-acquiring-and-network-connectivity` cites the two Stripe URLs that now redirect (`https://stripe.com/en-us/legal/ssa-services-terms`, `https://stripe.com/stel/legal`).
- Any page that says Adyen publishes no per-country acquiring information (ruling 11 context; chapter 6's acquirer inventory) should take account of `https://docs.adyen.com/account/supported-currencies`, which lists Adyen's acquiring connections by country and region.
- Any page that calls Stripe's partners in Japan "banks": the disclosure names Sumitomo Mitsui Card Co., Ltd. and JCB Co., Ltd. Ruling 11 omits Mexico (Stripe both acquirer and facilitator) and the United Arab Emirates (Stripe an ISO of Network International).
- Any page that quotes Adyen's annual report on banking partners: the sentence is about concentration risk, not a description of acquiring.
