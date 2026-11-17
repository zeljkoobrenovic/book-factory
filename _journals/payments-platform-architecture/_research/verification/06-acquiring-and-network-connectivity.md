# Verification — 06-acquiring-and-network-connectivity (`acquiring-and-network-connectivity`)

Verification pass of 17 November 2026. Every source was fetched in this session with curl (Stripe pages with an English locale cookie, because the site otherwise redirects to a regional language; the Visa rules PDF and Adyen's annual report and shareholder letter PDFs converted with pdftotext; the Block 10-K from EDGAR; Adyen documentation as `.md`). Quotations were compared with the fetched text by script after normalizing typographic quotes and whitespace, and the surrounding passage was read for each.

Counts: 86 claims listed; 71 confirmed, 9 corrected, 3 hedged, 2 unsupported, relabeled, 1 not checked; 0 unreachable.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe, April 2020: "now processes card transactions through direct integrations with all six major card networks…" | https://stripe.com/en-ca/newsroom/news/direct-platform | confirmed | Dated 23 April 2020 on the page; the six are named there (Visa, Mastercard, American Express, Discover, JCB, China Union Pay). |
| 2 | Stripe US: "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers"; five banks plus Stripe MALPB | https://stripe.com/legal/acquirer-disclosure | confirmed | Source URL changed (was /en-us/legal/…; final URL without locale prefix). |
| 3 | Stripe MALPB is a limited-purpose bank of Stripe's own | https://stripe.com/legal/stripe-malpb-acquirer-terms | confirmed | Was supported only by the name and trade press; now by Stripe's own terms (source added). |
| 4 | Adyen's European banking license "obtained in 2017" | https://www.adyen.com/press-and-media/adyen-granted-us-branch-license | confirmed | No edit. |
| 5 | Stripe entities are the acquirer in the EEA and the UK | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 6 | Visa public rules, edition of 24 October 2026 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Title page read. |
| 7 | Visa glossary, Acquirer: "A Member that signs a Merchant or Payment Facilitator… directly or indirectly enters a Transaction into Interchange." | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Added a one-clause gloss of Interchange from the same glossary ("The exchange of Clearing Records between Members"). |
| 8 | Stripe services terms: definition of "Payment Method Acquirer" | https://stripe.com/legal/ssa-service-terms | confirmed | URL changed (ssa-services-terms redirects to ssa-service-terms); replaced. |
| 9 | Adyen: "Acquirers must be licensed by local financial regulators and card schemes to relay transactions." | https://www.adyen.com/knowledge-hub/acquiring-bank | confirmed | Added a gloss of "card scheme". |
| 10 | Stripe Technology Europe: e-money institution, Central Bank of Ireland, C187865, "acquire payment transactions", page dated April 2019 | https://stripe.com/legal/stel | confirmed | "Last updated: April 5, 2019". URL changed (was /stel/legal); replaced. |
| 11 | Stripe's current disclosure names the same entity as EEA acquirer | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 12 | Visa 2.2.1.1: a Principal-Type Member licenses its own BIN or Acquiring Identifier; an Associate-Type Member may use its sponsor's | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 13 | Visa 2.2.1.1 liability quotations (Principal-Type Member; Sponsor) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | The source carries a footnote mark after "responsible"; the quotation is otherwise exact. |
| 14 | BIN = Bank Identification Number; Acquiring Identifier is the acquiring-side identifier | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Glossary entries read. |
| 15 | Mastercard uses "principal" and "affiliate" for its two levels | none (Mastercard rules not readable, ruling 17) | not checked | Kept as written: the page already says the rules could not be read and calls the terms common usage. |
| 16 | Visa glossary, Acquirer Processor: "A non-Member agent or processor…" | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 17 | Visa glossary, Payment Facilitator definition | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 18 | Visa 5.3.1.2: sponsored merchant treated as a merchant of the facilitator's acquirer; acquirer liable | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 19 | Visa 5.3.1.4: direct agreement above USD 1 million; before processing or "within 2 years"; exceptions | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Exceptions read (two-year relationship with reporting; listed merchant categories). |
| 20 | Block 10-K for 2025: "For a majority of our transactions, we do not directly access the payment card networks"; Block is a payment facilitator | https://www.sec.gov/Archives/edgar/data/1512673/000162828026012254/xyz-20251231.htm | confirmed | The filing also says network rules apply to it as a "payment facilitator". |
| 21 | Visa glossary, Domestic Transaction | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 22 | Visa glossary, Transaction Country | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 23 | Any other transaction is an International Transaction | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Glossary: issuer "not located in the Transaction Country". |
| 24 | Visa Core Rules 1.5.1.1: acquirer accepts only from outlets in its Country of Domicile "unless any of the following" | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Section number and its place in the Core Rules confirmed. |
| 25 | Europe exception: "An Acquirer has passported its license in line with EU passporting regulations." | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit. |
| 26 | Stripe local-acquiring guide: "Because the transaction is local, the chances of approval are typically higher…"; last updated August 2023 | https://stripe.com/resources/more/local-acquiring-101 | confirmed | "Last updated August 15, 2023". |
| 27 | Adyen acquiring page: "Local processing can increase authorization rates and reduce cross-border fees." | https://www.adyen.com/global-acquiring | confirmed | No edit. |
| 28 | Neither of those two pages gives a number for the gain | both pages above | confirmed | Both texts searched for percentages. |
| 29 | Klook: "…an overall uplift of 3% in their authorization rates", August 2024 | https://www.adyen.com/knowledge-hub/klook-takes-off-payments-optimization | confirmed | Displayed date August 5th, 2024. |
| 30 | Trade press, April 2020: with direct connectivity firms "can see upwards of half a percentage point of authorization improvement" (publication's wording) | https://www.pymnts.com/digital-payments/2020/stripes-john-collison-on-improving-the-art-of-authorization-amid-a-digital-payments-boom/ | confirmed | The sentence is the publication's paraphrase, as the page says. Source URL replaced by the final URL. |
| 31 | "I found two statements with a number" | https://stripe.com/newsroom/stories/twilio | corrected | A third exists: Stripe's Twilio customer story (17 November 2020). Text now says three and the table has the row; the argument (no isolated figure) is unchanged. |
| 32 | Twilio story: "+5.5% uplift from Stripe's Global Payments Infrastructure", direct integration and local processing, against the previous provider | https://stripe.com/newsroom/stories/twilio | confirmed | New row; source added with evidence age. |
| 33 | Some domestic schemes and clearing systems can be reached only by a member in that country | none | hedged | No source in the page; now introduced as "By common industry account". |
| 34 | Adyen H1 2026 release: "Secured direct access to France's domestic interbank clearing system" | https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne | confirmed | No edit. |
| 35 | H1 2026 shareholder letter cites the French announcement whose title names CB principal membership and STET direct participation | https://investors.adyen.com/financials/h1-2026-c2a1a (PDF) | confirmed | Footnote 10: "Adyen devient membre principal de CB et participant direct de STET…". |
| 36 | The sponsoring bank stays liable for the facilitator and its sellers | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Same passage as 5.3.1.2. |
| 37 | On Stripe's disclosure each US bank comes with "Acquirer Terms" the merchant accepts | https://stripe.com/legal/crb-acquirer-terms ; https://stripe.com/legal/stripe-malpb-acquirer-terms | corrected | The page said the merchant accepts each bank's terms. The terms read (Cross River Bank, last updated 18 November 2025; Stripe MALPB) say they "become effective only when User processes more than $1 million in Transactions on a Network within any twelve-month period" unless the user is network registered. Sentence rewritten; one link is titled "Fifth Third Bank Terms", not "Acquirer Terms". Only two of the six sets of terms were read, and the text says so. |
| 38 | Stripe's Irish and UK entities are e-money institutions | https://stripe.com/legal/stel ; https://stripe.com/legal/spukl | confirmed | No edit. |
| 39 | Georgia's MALPB charter; trade association, July 2025: "will allow… without a sponsoring bank"; "may not solicit or accept deposits from the general public" | https://www.icba.org/w/georgia-approves-stripe-application-to-form-malpb | confirmed | Dated July 08, 2025. Source URL replaced by the final URL. |
| 40 | Trade press, September 2026: "Stripe's MALPB received permission to begin business in May of this year" | https://www.pymnts.com/news/acquiring/2026/payments-firms-put-georgia-limited-purpose-bank-charter-work/ | confirmed | Dated September 14, 2026. Source title corrected to the headline on the page and URL replaced by the final URL. Stripe's MALPB terms are dated 28 May 2026, which agrees. |
| 41 | Adyen N.V. a credit institution under the Dutch central bank since 2017, passported across the EEA | https://www.adyen.com/licenses/emea | confirmed | No edit. |
| 42 | Branch licenses: United States 2021, United Kingdom 2023 | Adyen press releases; licenses pages | confirmed | No edit. |
| 43 | Adyen EEA license quotations (table) | https://www.adyen.com/licenses/emea | confirmed | No edit. |
| 44 | "a federal Branch of Adyen, N.V., licensed by the Office of the Comptroller of the Currency and the Federal Reserve Board of Governors" | https://www.adyen.com/licenses/united-states | confirmed | No edit. |
| 45 | Federal Reserve approval, 24 May 2021 | https://www.federalreserve.gov/newsevents/pressreleases/orders20210524a.htm | confirmed | No edit. |
| 46 | Comptroller's approval announced 14 June 2021 | https://www.adyen.com/press-and-media/adyen-granted-us-branch-license | confirmed | No edit. |
| 47 | UK branch "has been granted authorization as a UK bank", 7 September 2023 | https://www.adyen.com/press-and-media/adyen-granted-uk-banking-authorization | confirmed | No edit. |
| 48 | The current license pages confirm all three licenses | https://www.adyen.com/licenses/emea ; /united-states | confirmed | EEA, UK (Part 4A permission) and US entries read. |
| 49 | Annual Report 2025: "acquiring our own banking licenses in the EU, US, and UK. Operating these licenses ourselves…" | https://investors.adyen.com/financials/2025 (PDF) | confirmed | No edit. |
| 50 | Annual Report 2025: "the speed and autonomy that come from not relying on external parties for regulatory compliance" | https://investors.adyen.com/financials/2025 (PDF) | confirmed | No edit. |
| 51 | H1 2026 letter: "Our own licensed infrastructure grants direct access to payment networks, giving us control over funds" | https://investors.adyen.com/financials/h1-2026-c2a1a (PDF) | confirmed | Letter dated August 13, 2026. |
| 52 | "Of processed volumes, 84% were full-stack volumes, up from 83% in 2024." | https://investors.adyen.com/financials/2025 (PDF) | confirmed | No edit. |
| 53 | "Concentration risk at Adyen originates primarily at banking partners in locations where there are no own direct acquiring licenses." | https://investors.adyen.com/financials/2025 (PDF) | confirmed | No edit. |
| 54 | Adyen relies on partner banks in some markets and does not publish which | https://docs.adyen.com/account/supported-currencies.md | hedged | Ruling 27(b, c). The reliance is now labeled as the author's inference from a concentration-risk sentence. Added what Adyen does publish: the documentation page "Supported payout currencies" lists 14 countries and regions per "Adyen acquiring connection" (Australia, Hong Kong, India, Japan, Malaysia, New Zealand, Singapore, European Union, United Kingdom, Canada, United States, Brazil, Mexico, United Arab Emirates) and says payments go "through one of our acquiring entities, for example Adyen Singapore"; it names no entity per country. Page fetched and read; front matter gives last_modified 2023-02-22, cited as n.d. per the ruling. A May 2021 press release with an older list of local-acquiring markets was also read and is not cited. |
| 55 | "Pass-through payout is the only available payout model in Africa, Brazil, and India"; page last modified 2020 | https://docs.adyen.com/account/getting-paid.md | confirmed | last_modified 2020-11-10; sentence present today. |
| 56 | Adyen publishes no list of networks and countries where it is a principal member | licenses pages, acquiring page, docs.adyen.com/llms.txt, annual report, H1 letter, web search | confirmed | As far as searched; a negative cannot be proven. |
| 57 | INFERENCE block: the report does not define "full-stack" there; 16% is acquired by someone else | https://investors.adyen.com/financials/2025 (PDF) ; https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report.md | hedged | The term occurs once in the report text. Added the documented fact that Adyen reports "transactions for which Adyen is not the acquirer" with American Express and PayPal as examples, so the 16% is not all partner banks. |
| 58 | Stripe table: EEA, "Stripe Technology Europe, Ltd." | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 59 | Stripe table: United Kingdom, Gibraltar, Switzerland, "Stripe Payments UK, Ltd." | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 60 | Stripe table: Australia, New Zealand, Singapore, Malaysia, Hong Kong, Brazil are Stripe entities | https://stripe.com/legal/acquirer-disclosure | confirmed | Hong Kong's is Stripe Payments Europe, Limited. |
| 61 | Stripe table: Canada, Japan, Thailand as payment facilitator of named banks or card companies | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 62 | Stripe table: India "Payment Aggregator" of RBL Bank; UAE "Independent Sales Organization (ISO)" of Network International | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 63 | Stripe table presented as the page's rows | https://stripe.com/legal/acquirer-disclosure | corrected | Mexico was missing: Stripe Payments Mexico "is both a Payment Method Acquirer and a Payment Facilitator" of GetNet México and BBVA México. Row added. |
| 64 | Stripe Payments UK: e-money institution, FCA, 900461, "acquire payment transactions", page dated January 2017 | https://stripe.com/legal/spukl | confirmed | "Last updated: January 26, 2017". URL changed (was /spukl/legal); replaced. |
| 65 | "Stripe MALPB, 505 N Angier Avenue NE, Atlanta, GA" has its own terms and "matches the Georgia charter" | https://stripe.com/legal/stripe-malpb-acquirer-terms | corrected | The match was the page's inference. Stripe's terms (last updated 28 May 2026) state it: "a Georgia Merchant Acquirer Limited Purpose Bank", "a member of the Networks", "Stripe is registered as a Payment Facilitator by Member Bank". Quoted and sourced. |
| 66 | Stripe does not publish how US volume divides among the six, or whether its own bank acquires for all merchants | https://stripe.com/legal/acquirer-disclosure ; MALPB terms | confirmed | As far as searched. |
| 67 | Stripe 2020: "By exchanging information directly with the card networks, rather than relying on intermediaries…" | https://stripe.com/en-ca/newsroom/news/direct-platform | confirmed | No edit. |
| 68 | The list of six networks has not been republished | https://stripe.com/authorization-boost ; docs.stripe.com/llms.txt | confirmed | As far as searched. |
| 69 | Stripe product page: "Stripe has direct connections to card networks to ensure our data is as rich as possible." | https://stripe.com/authorization-boost | confirmed | The cited URL (/payments/authorization) now redirects to the Authorization Boost page; source title and URL replaced. |
| 70 | No public statement by Stripe explains its mix of partner banks and own licenses | Stripe newsroom and legal pages, docs index, web search | confirmed | As far as searched; a negative cannot be proven. |
| 71 | Trade press, April 2025: a Stripe spokesperson called the Georgia application an extension of its work to expand its banking and other partners | https://www.bankingdive.com/news/stripe-georgia-special-banking-charter-credit-card-payments/744921/ | confirmed | Published April 7, 2025; the paraphrase matches the article's. |
| 72 | Where They Differ, regulatory form (both cells) | sources above | confirmed | No edit. |
| 73 | Where They Differ, acquirer of record, Stripe cell | https://stripe.com/legal/acquirer-disclosure | corrected | Said "named banks elsewhere" and left out Brazil; now "the EEA, the UK, Brazil and much of Asia-Pacific; named banks or card companies in the other countries listed". |
| 74 | Where They Differ, acquirer of record, Adyen cell: "Not public per country" | https://docs.adyen.com/account/supported-currencies.md | corrected | Ruling 27(b): Adyen lists 14 countries and regions with an acquiring connection. Cell now states that, says no acquiring entity is named per country, and keeps the 84%. The last-column reading and the advice sentence after the table were changed to match. |
| 75 | Where They Differ, partner banks, Stripe cell | https://stripe.com/legal/acquirer-disclosure | corrected | Mexico added; ruling 27(a): the cell now says the named acquirers are banks, and card companies in Japan. The lead paragraph's "named banks" is now "named acquirers, most of them banks". |
| 76 | Where They Differ, partner banks, Adyen cell | https://investors.adyen.com/financials/2025 (PDF) | confirmed | No edit. |
| 77 | Where They Differ, direct connections (both cells) | sources above | confirmed | No edit. |
| 78 | Where They Differ, stated reason: Stripe "Not public"; Adyen quotation | sources above | confirmed | Stripe cell as far as searched. |
| 79 | Where They Differ, measured gain: "Not public" for both | Twilio story; Klook case | corrected | Both companies publish customer figures; neither isolates local acquiring. Cells now say so with the figure and year. |
| 80 | Adyen's naming of Visa and Mastercard is press boilerplate from 2021 | https://www.adyen.com/press-and-media/adyen-granted-us-branch-license | confirmed | No edit. |
| 81 | Take-away: the USD 1 million rule cited as "Visa Core Rules, October 2026" | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | corrected | Sections 5.3.1.2 and 5.3.1.4 are in the Visa Product and Service Rules, not the Core Rules. Now "Visa's rules, edition of October 2026", with "with exceptions". |
| 82 | Stripe names Stripe Technology Europe as acquirer for the whole EEA, so Mila's payment would still be domestic on Stripe | https://stripe.com/legal/acquirer-disclosure ; https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | The facts are confirmed; the conclusion is labeled as the author's reading in the text. |
| 83 | Journey paragraph: the acquirer of Mila's payment "is Adyen N.V." | https://www.adyen.com/licenses/emea | unsupported, relabeled | Adyen names no acquirer per country; ledger line for chapter 1 requires the label. Now "my reading of Adyen's license page". |
| 84 | Inventory table: "Adyen N.V." as acquirer of record "per the provider's public pages" | https://www.adyen.com/licenses/emea | unsupported, relabeled | Same; cell labeled as the author's reading. |
| 85 | Stripe's public page does not say which acquirer applies per account | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |
| 86 | Stripe's US list had six names in November 2026, one its own new bank | https://stripe.com/legal/acquirer-disclosure | confirmed | No edit. |

## Not verified, and what was done

- **Mastercard's membership terms** (claim 15): the Mastercard rules were not read (ruling 17). The page already says so and presents the terms as common usage; left as written.
- **Four of Stripe's six US acquirer terms** (Deutsche Bank, Fifth Third, Pathward, PNC) were not read. The rewritten sentence says two were read and quotes only Cross River Bank's.
- **Three negatives** (claims 56, 69, 71; also 67 and the Stripe cell in 79) rest on searches of the providers' sites, both documentation indexes (`docs.stripe.com/llms.txt`, `docs.adyen.com/llms.txt`) and a web search. They are true as far as searched.
- **Dates in the Georgia regulator's bulletin** (approval 30 June 2025, start 28 May 2026) appear only in the trade-press article; the page does not use them. The start date agrees with the date on Stripe's MALPB terms.
- **The industry statement on domestic schemes** (claim 33) has no source; it is now worded as common industry account. The French CB and STET case that follows it is sourced.
- The glosses of CB (French domestic card scheme) and STET (French clearing system) are the author's; the shareholder letter gives only the announcement's title.

## Links

All 30 URLs in Sources and Evidence return 200. Replaced by their final URLs: Stripe services terms (`ssa-services-terms` → `ssa-service-terms`), STEL and SPUKL pages (`/stel/legal` → `/legal/stel`, `/spukl/legal` → `/legal/spukl`), Stripe product page (`/payments/authorization` → `/authorization-boost`, title now Authorization Boost), ICBA article, both PYMNTS articles (short `?p=` links → article URLs; the 2026 headline is "Payments Firms Put Georgia's Limited Purpose Bank Charter to Work"). The `en-us` prefix was dropped from Stripe URLs because it redirects. Sources added: Stripe MALPB Acquirer Terms, Cross River Bank Acquirer Terms, Stripe's Twilio story, Adyen's Supported payout currencies page, Adyen's External settlement detail report. The description of Adyen's license pages no longer mentions the UAE license, which the text does not use.

All `[[permalink]]` links are in the style guide's list. The render check reports `[[case-adyen]]` and `[[stripe-and-adyen-bets-compared]]` as unresolved because those pages are not written yet; no `XJ:` entries.

## Format and rulings

- Ruling 22: no external URL in the running text (none found). Rulings 3, 11, 17 and 27 applied; ruling 11's qualifications are all present.
- Glosses added on first use: Interchange (Visa's sense), card scheme, chargeback, Keel.
- `timetoread` changed from 23 to 25 (5,845 words by `check_draft.py structure` ÷ 230 = 25.4).
- No unit added, dropped, merged or reordered; `validate_spec.py` and `check_draft.py structure` pass. Table rows were added inside existing table units (Twilio; Mexico).

## Larkfield consistency

Checked against the ledger: studio counts per market, 3,750 − 1,140 = 2,610, Tuesday 9 March 2027 (weekday correct), 19:42, €120.00, Dutch Visa debit, Femke de Graaf's role and the February 2027 inventory, Tom Hendriks, K8, €1.12 billion ÷ 6,200 ≈ €181,000. All agree.

## Ledger conflicts

- The chapter 1 addition says the acquirer of record for Mila's pass "is treated as Adyen N.V., labeled as inference wherever it is stated (Adyen publishes no acquirer per country)". The chapter 6 addition says the inventory is "filled from the providers' public pages: Adyen N.V. for NL/DE on Adyen". These do not contradict each other, but the chapter 6 line reads as if Adyen's pages named the acquirer. This page owns the topic and now carries the label in both places.

## For other pages

- **Ruling 27** already covers Mexico and the UAE in Stripe's disclosure. One more detail: in India Stripe's stated role is "Payment Aggregator", not payment facilitator.
- **Ruling 27(b)** cites Adyen's page as "Supported currencies"; its title today is "Supported payout currencies", and its `.md` front matter gives last_modified 2023-02-22.
- **Stripe's bank acquirer terms take effect above USD 1 million on a network in twelve months** (Cross River Bank terms, 18 November 2025). `platform-payment-models` (ch. 33) and `case-stripe` may want this primary source for the facilitator threshold.
- **Stripe MALPB** is confirmed by Stripe's own terms dated 28 May 2026 as a network member and acquirer; pages that cite only trade press for it (`case-stripe`, `payments-what-is-moving`) can cite the primary page.
- The acquiring research brief (section 1.6) omits Mexico from the Stripe table.

## For the author to decide

- Length is 5,845 words, above the 4,000–5,500 aim and under the 6,500 limit; the pass added about 300 words of sourced qualification.
- The opening hook now has a stronger answer than the chapter gives it credit for: Stripe's own terms say Stripe MALPB is a network member. Whether to make more of that is an argument change and was not made.
- The title keeps "Licences" as in PLAN.md, while running prose uses "license".
