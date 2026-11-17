# Verification — 26-kyc-aml-and-regulation (`payment-compliance-and-regulation`)

Verification pass of 17 November 2026. Every source below was fetched in this session with `curl`: Stripe and Adyen documentation as `.md` variants; the EU texts from `publications.europa.eu/resource/celex/<CELEX>` (they return 404 with `Accept: text/html` today and 200 with `Accept: application/xhtml+xml` and `Accept-Language: eng`); the FinCEN order as PDF converted with `pdftotext`; stripe.com pages with an `en-us` locale cookie (without it the legal page redirects to the `/nl/` edition); the two Stripe support articles from the JSON embedded in their HTML (the pages are client-rendered). Quotations were compared with the fetched text by script after normalizing typographic quotes, dashes, backticks and markdown links; every quoted string in the article matches its source.

Abbreviations: S = `https://docs.stripe.com`, A = `https://docs.adyen.com`, AMLR = Regulation (EU) 2024/1624 (`http://publications.europa.eu/resource/celex/32024R1624`), IPR = Regulation (EU) 2024/886 (`…/celex/32024R0886`), DORA = Regulation (EU) 2022/2554 (`…/celex/32022R2554`), OEIL = `https://oeil.europarl.europa.eu/oeil/en/procedure-file`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | AMLR "shall apply from 10 July 2027" | AMLR, Article 90 | confirmed | — |
| 2 | AMLR is one directly applicable rulebook | AMLR, Article 90 ("directly applicable in all Member States") | confirmed | Inline link removed; attribution "the EU's AML Regulation, published in June 2024" added |
| 3 | Until then national laws under the earlier directive apply | Directive (EU) 2024/1640, Article 77 (`…/celex/32024L1640`): "Directive (EU) 2015/849 is repealed with effect from 10 July 2027" | confirmed | The brief tagged this as an assumption; now sourced. Clause "which is repealed on the same date" and a source entry added |
| 4 | Beneficial owner: "any natural person who ultimately owns or controls a legal entity" | AMLR, Article 2(1)(28) | confirmed | — |
| 5 | Article 52: "direct or indirect ownership of 25 % or more of the shares or voting rights or other ownership interest in the corporate entity" | AMLR, Article 52(1) | confirmed | — |
| 6 | FinCEN: "identify and verify the identity of any individual who owns 25 percent or more of a legal entity, and an individual who controls the legal entity" | https://www.fincen.gov/resources/statutes-and-regulations/cdd-final-rule | confirmed | — |
| 7 | "covered institutions must…" (who is covered) | same page: "U.S. banks, mutual funds, brokers or dealers in securities, futures commission merchants, and introducing brokers in commodities" | hedged | The page did not say who is covered, which read as if payment companies were. Now "banks, securities brokers, mutual funds and similar firms, which its rule calls covered financial institutions". FinCEN expanded on first use |
| 8 | "the rule dates from 2016"; source entry "evidence age: 8 years" | FinCEN order FIN-2026-R001, Background: issued 2016 (81 FR 29398, May 11, 2016), "May 11, 2018 applicability date" | corrected | 2016 to 2026 is 10 years, not 8. Text now "issued in 2016 and has applied since May 2018 **(evidence age: 10 years; still in force)**"; source entry and spec evidence line changed |
| 9 | FinCEN order of 13 February 2026 "relaxed when owners must be re-identified" | https://www.fincen.gov/system/files/2026-02/FinCEN-Order-CCDExceptiveRelief.pdf ("Issue Date: February 13, 2026"; relief from identifying owners "at each new account opening") | corrected | The order was not fetched by the writer; fetched and read now. Wording made exact: it "removed the duty to identify the owners again each time an existing customer opens another account". Source entry no longer says "not re-fetched" |
| 10 | Adyen asks for "Individuals who directly or indirectly own 25% or more of the total shares, voting rights or other equity in the organization" | A/platforms/verification-requirements.md | confirmed | Inline link removed |
| 11 | Article 20(1)(d): "verifying whether the customer or the beneficial owners are subject to targeted financial sanctions" | AMLR, Article 20(1)(d) | confirmed | — |
| 12 | OFAC 50 Percent Rule: an entity owned 50 percent or more by blocked persons is blocked; ownership, not control | https://ofac.treasury.gov/faqs/topic/1521 (FAQ 398, 399, 401) | confirmed | Inline link removed; attribution to OFAC's FAQ added |
| 13 | PEP: "a natural person who is or has been entrusted with prominent public functions" | AMLR, Article 2(1)(34) | confirmed | — |
| 14 | Article 26(4): banks and financial institutions repeat the sanctions check "upon any new designation" | AMLR, Article 26(4), second subparagraph ("For credit institutions and financial institutions…") | confirmed | — |
| 15 | Article 26(1): monitoring "throughout the course of a business relationship, to ensure that those transactions are consistent with the obliged entity's knowledge of the customer, the customer's business activity and risk profile" | AMLR, Article 26(1) | confirmed | — |
| 16 | Article 69: "All suspicious transactions, including attempted transactions"; reported to the FIU | AMLR, Article 69(1) | confirmed | — |
| 17 | Article 73: "shall not disclose to the customer concerned or to other third persons" | AMLR, Article 73(1) | confirmed | — |
| 18 | Adyen's list: last update 13 November 2025; "R" restricted, "P" prohibited | https://www.adyen.com/legal/list-restricted-prohibited ("Last update Nov 13 2025") | confirmed | Inline link removed |
| 19 | "We will require additional documentation prior to onboarding" | same | confirmed | — |
| 20 | Reasons: laws; "Requirements of our payment partners (e.g. card networks)"; "Level of assessed risk (e.g. chargebacks, fraud)"; "Reputational impact to Adyen" | same (the last item continues "and cost aspects associated with this") | confirmed | — |
| 21 | Stripe's list: last updated 22 September 2026; prohibited and restricted categories and per-country additions; "read in its Dutch edition" | https://stripe.com/legal/restricted-businesses (English, with locale cookie): "Last updated: 2026-09-22"; sections "Prohibited businesses", "Restricted businesses", "Jurisdiction-specific prohibited businesses" | corrected | The English edition was read in this pass, so the Dutch-edition remark is removed; "per-country additions" is now "additions per jurisdiction". Still a paraphrase |
| 22 | Article 26(2): update interval at most "1 year" for higher-risk customers, "5 years" for all others | AMLR, Article 26(2) | confirmed | — |
| 23 | Article 26(3): review on a "change in the relevant circumstances of a customer" | AMLR, Article 26(3)(a) | confirmed | — |
| 24 | Stripe defines a `requirements` structure; changes arrive through `account.updated` | S/connect/handling-api-verification.md?accounts-namespace=v1 | confirmed | Inline link removed |
| 25 | `currently_due` definition | same, properties table | confirmed | — |
| 26 | `eventually_due` definition | same | confirmed | — |
| 27 | `past_due` definition | same | confirmed | — |
| 28 | `pending_verification` definition | same | confirmed | — |
| 29 | `current_deadline`: "the earliest deadline across all of the account's requested capabilities and risk requirements" | same (continues ", including any hidden capabilities") | confirmed | — |
| 30 | `disabled_reason`: "why the account isn't enabled and why it can't process charges or transfers" | same | confirmed | — |
| 31 | "Stripe typically disables payouts on the account if we don't receive the information by the `current_deadline`" | same | confirmed | — |
| 32 | If the account stays unresponsive, "Stripe might also disable the ability to process charges." | same ("if payouts are already disabled and the account is unresponsive to our inquiries") | confirmed | — |
| 33 | Thresholds: "At certain variable thresholds—usually when a specified amount of time has passed or volume of charges have been made—… Stripe temporarily pauses charges or payouts if the information isn't provided or verified" | S/connect/identity-verification.md | confirmed | Inline link removed |
| 34 | "Stripe frequently updates KYC requirements, often due to changes implemented by financial regulators, card networks, and other financial institutions." | S/connect/handle-verification-updates.md?accounts-namespace=v1 | confirmed | Inline link removed |
| 35 | `future_requirements` deadline "represents when entries in `future_requirements` will move to `requirements`" | same | confirmed | — |
| 36 | Where Stripe collects requirements it "handles upcoming requirement changes for your connected accounts automatically"; otherwise the platform does | same (`requirement_collection` `stripe` or `application`) | confirmed | — |
| 37 | API onboarding "must plan on reviewing and updating onboarding requirements at least every 6 months" | S/connect/onboarding.md | confirmed | Inline link removed |
| 38 | `sanctions_review`: "We must verify that the business isn't involved with a sanctioned person or jurisdiction" | S/connect/handling-api-verification.md | confirmed | — |
| 39 | Requirement types `pep_review`, `restricted_or_prohibited_industry_diligence`, `other_compliance_inquiry` | same | confirmed | — |
| 40 | `legal_hold`: "Stripe is required to hold funds for a legal reason" | same | confirmed | — |
| 41 | `disabled_reason` values `under_review`, `listed` ("The account might be on a prohibited persons or companies list. Stripe investigates and either rejects or reinstates the account accordingly.") and `requirements.past_due` | same | confirmed | — |
| 42 | Adyen: "As required by payment industry regulations, Adyen must verify the users in your platform before you can process payments, pay out their funds, and offer financial products to them." | A/platforms/verification-overview.md | confirmed | Inline link removed |
| 43 | Adyen verifies a legal entity; capabilities sit on the account holder; flags `requested`, `allowed`, `enabled`; `enabled` is the platform's switch | A/platforms/verification-overview/capabilities.md | confirmed | Inline link removed |
| 44 | "The capability can only be used when it is both allowed and enabled." | same | confirmed | — |
| 45 | `verificationStatus` `pending`, `valid`, `invalid`, `rejected`; problems with verification errors and remediating actions | same | confirmed | — |
| 46 | Adyen verifies again when capabilities are requested, when data changes and at a periodic data review, "each with a deadline" | A/platforms/verification-overview.md: "Adyen may set a deadline" for these events; a deadline is always set only for the data review | hedged | Now "and for each it may set a deadline" (text and spec controlling idea) |
| 47 | Standard "30-day period" for `sendToTransferInstrument` and other payout-side capabilities; "60-day period" for `receivePayments` and others | same, deadlines table | confirmed | — |
| 48 | "Users are allowed to continue using the capabilities while the deadline is active" | same | confirmed | — |
| 49 | "a standard deadline could be shortened or removed in specific situations" | same | confirmed | — |
| 50 | "Adyen occasionally requires your users to review and confirm that their data is up-to-date." | A/platforms/verification-overview/data-review-process.md | confirmed | Inline link removed |
| 51 | Data review webhook: status `invalid`, error 3_10 "Review of data is required", `allowed` "Remains set to `true`" until the deadline | same, Step 1 table | confirmed | — |
| 52 | Payment facilitators may verify in tiers; on a move to a higher tier "their payouts are temporarily disallowed until they complete additional verification checks" | A/platforms/verification-overview/verification-types.md | confirmed | Inline link removed |
| 53 | Account-holder webhooks "are only triggered for capability-related changes to the account holder. Data changes to the legal entity of the account holder do not trigger webhooks." | A/platforms/verification-overview.md | confirmed | — |
| 54 | Five routes to a restriction "on both providers", including a periodic review | #33–36, #38–41, #46–52, #86 | hedged | Stripe's periodic route is announced and in preview (#86); parenthesis "(on Stripe still in preview in 2026)" added |
| 55 | Neither company publishes its monitoring scenarios, sanctions-screening logic or re-verification intervals | Searched `docs.stripe.com/llms.txt`, `docs.adyen.com/llms.txt`, Adyen's verification-code pages (`A/platforms/kyc-verification-codes/*.md`), Stripe support. Found: https://stripe.com/resources/more/ongoing-seller-compliance-monitoring (last updated August 31, 2026), a general guide that lists monitoring patterns "for general information and education purposes only"; Stripe's KYC Refresh article says frequency "depends on its risk profile, local regulatory requirements, and when account information was last updated"; Adyen's data-review page mentions a "next scheduled review" without an interval | hedged | Claim stands. One sentence added naming Stripe's general guide and saying it is not a description of Stripe's own system; source entry added |
| 56 | Stripe Radar: "We calculate account-level risk using KYC information, transactions, geographic risk factors, and behavior patterns." presented as evidence that monitoring exists | S/radar/rules.md (the sentence follows the rules `:account_fraud_risk_level:`; it concerns connected accounts' fraud risk) | hedged | Quotation exact. "account-level models" is now "account-level fraud models", and the reading is weakened to "accounts are watched after onboarding … Stripe's sentence is about fraud risk, not money laundering" |
| 57 | "Adyen has one sentence": "Verification deadlines may be adjusted based on ongoing account monitoring and subsequent verification checks." | A/platforms/verification-overview.md; the capabilities page also says card-issuing levels "may also require more checks and increased monitoring" | hedged | Quotation exact. Now "Adyen's verification overview has one sentence" |
| 58 | Inference block: Articles 26(1), 26(2), 26(4), 69 as the basis | AMLR | confirmed | — |
| 59 | DORA "shall apply from 17 January 2025" | DORA, Article 64 | confirmed | Inline link removed; evidence-age note moved into the sentence (published 27 December 2022, about 4 years) |
| 60 | DORA scope names credit institutions, payment institutions and electronic money institutions | DORA, Article 2(1)(a), (b), (d) | confirmed | — |
| 61 | Article 19: "Financial entities shall report major ICT-related incidents" | DORA, Article 19(1) | confirmed | ICT expanded |
| 62 | Firms "must keep a register of their technology suppliers" | DORA, Article 28(3): "a register of information in relation to all contractual arrangements on the use of ICT services provided by ICT third-party service providers" | hedged | Now "a register of their contracts with technology suppliers" |
| 63 | On 18 November 2025 the ESAs published the list of designated critical providers, under direct oversight | https://www.eba.europa.eu/publications-and-media/press-releases/european-supervisory-authorities-designate-critical-ict-third-party-providers-under-digital ("18 November 2025"; "publish today the list of designated critical ICT third-party providers"; "direct oversight engagement") | confirmed | Inline link removed |
| 64 | "I found no DORA statement by Stripe or Adyen" | Web search in this session returned none from stripe.com or adyen.com | confirmed (as an absence; a search cannot prove it) | — |
| 65 | Euro-area PSPs: receive instant euro transfers by 9 January 2025, send by 9 October 2025 | IPR, Article 5a(8), first subparagraph | confirmed | Inline link removed |
| 66 | Verification of payee: "a service ensuring verification of the payee"; euro area by 9 October 2025 | IPR, Article 5c(1) and 5c(9) | confirmed | — |
| 67 | Verification of payee in non-euro member states by 9 July 2027 | IPR, Article 5c(9) | confirmed | — |
| 68 | Euro-area payment and e-money institutions: instant transfers by 9 April 2027 | IPR, Article 5a(8), third subparagraph | confirmed | — |
| 69 | The payee check happens before the transfer is authorized (table cell) | IPR, Article 5c(1) and recital 20 | confirmed | — |
| 70 | Instant transfer reaches the payee "within 10 seconds" | IPR, Article 5a(4)(c) | confirmed | — |
| 71 | Article 5d: "shall carry out such verifications immediately after the entry into force of any new targeted financial restrictive measures … and at least once every calendar day", against all customers | IPR, Article 5d(1) ("any of their PSUs") | confirmed | — |
| 72 | During an instant transfer providers "shall not verify" payer or payee against those lists again | IPR, Article 5d(2) | confirmed | — |
| 73 | Table: instant payments "in application for euro-area providers that already offered credit transfers (in practice, banks); future date for others" | IPR, Article 5a(1) and 5a(8) (non-euro: receive 9 January 2027, send 9 July 2027) | confirmed ("in practice, banks" is the author's gloss) | — |
| 74 | Table: AMLR adopted, applies from 10 July 2027; review intervals one and five years | #1, #22 | confirmed | — |
| 75 | AMLA operating; direct supervision not started; "During 2028" start of direct supervision by AMLA's own timeline | https://www.amla.europa.eu/about-amla_en (Timeline: "Summer 2025 AMLA starts operations"; "During 2027 40 obliged entities are selected to be directly supervised"; "During 2028 Start of direct supervision, with AMLA fully operational"); Regulation (EU) 2024/1620, Article 108 ("shall apply from 1 July 2025") | confirmed | — |
| 76 | AMLA supervises selected cross-border firms | same page ("Directly supervising selected financial sector entities that operate on cross border basis") | confirmed | — |
| 77 | PSD3 and PSR not adopted on 17 November 2026 | OEIL?reference=2023/0210(COD) and OEIL?reference=2023/0209(COD), both fetched 17 November 2026: status "Awaiting Parliament 2nd reading" | confirmed | The page cited one file for both texts; the PSD3 file was fetched too and a source entry added. Text now "procedure files for the two texts, read on that day" |
| 78 | "Council position published" on 5 November 2026 | both files: "05/11/2026 Council position published" (08543/1/2026 and 08535/1/2026) | confirmed | — |
| 79 | Indicative plenary date 14 December 2026 | both files: "14/12/2026 Indicative plenary sitting date, 2nd reading" | confirmed | — |
| 80 | Procedure-file URL | `oeil.secure.europarl.europa.eu` redirects to `oeil.europarl.europa.eu` | corrected | URL replaced with the final one in Sources and in the spec |
| 81 | Adyen's explainer (12 October 2026): "General application is expected 21 months after entry into force" | https://www.adyen.com/knowledge-hub/psd3 (displayed "October 12th, 2026"; "last updated 12 October 2026") | confirmed | Inline link removed |
| 82 | FinCEN order FIN-2026-R001 in effect, 13 February 2026 (table) | the order (#9) | confirmed | Last cell reworded to "Covered institutions need not identify owners again at each new account" |
| 83 | Three designs; K6 "verification is state, not a form" | scenario ledger, K6 | confirmed (Larkfield) | — |
| 84 | Where They Differ, row 1: what is verified and switched | #24, #43 | confirmed | — |
| 85 | Row 2: what is outstanding | #25–28, #45 | confirmed | — |
| 86 | Row 5, Stripe: periodic re-verification "Not public as an interval or an API event" | https://support.stripe.com/questions/kyc-refresh-upcoming-periodic-confirmation-requirements ("Last Updated: October 2026"): "Stripe will periodically add attestation requirements to connected accounts"; "Attestation requirements appear in the account's `requirements` hash, and they trigger the same `account.updated` webhook events"; "The first rollout applies to connected accounts in Europe"; "The KYC Refresh API is currently available in private preview. During the preview, impacted KYC refresh requirements have no due dates and do not affect capabilities."; public preview "in Q1 2027". Also https://support.stripe.com/questions/why-do-my-connected-accounts-need-reverification ("Connected accounts must be reverified periodically") | corrected | "Not public" was wrong: Stripe has announced it and documents it as an API requirement in preview. The cell now states that, with its status; the last column is reworded; two sentences added in the Stripe mechanism paragraph; source entry added |
| 87 | Row 3: Stripe one `current_deadline`, no standard length published; Adyen 30 and 60 days | #29, #47, #49; no length found in the three Stripe pages | confirmed | — |
| 88 | Row 4, Adyen: announced rule changes "Not public: no equivalent structure found" | A/release-notes/platforms-and-financial-products.md (dated entries to 2026-11-13; for example "Starting Q2 2024, verification of proof of signatory will be required for all users… who request a business account"); `llms.txt` lists no page for upcoming requirements on the current platform (one exists for classic platforms, for 1 August 2022) | hedged | No API structure found, but changes are announced in release notes. Cell now says so; one sentence added in the Adyen mechanism paragraph; source entry added |
| 89 | Row 6, Adyen: sanctions and PEP reviews "Not public: not named in the verification pages" | A/platforms/kyc-verification-codes.md and its three sub-pages, the four verification pages: no "sanction", "politically exposed" or "PEP" | confirmed | — |
| 90 | Row 7: transaction monitoring not public for both | #55 | confirmed | — |
| 91 | Failure table, Stripe threshold: "An entry that moved from `eventually_due` to `currently_due`" | S/connect/handling-api-verification.md: "it appears in both the `eventually_due` and `currently_due` arrays" | corrected | Now "An entry in `eventually_due` that now also appears in `currently_due`" |
| 92 | Failure table, Stripe periodic review: "Not documented as an event" | #86 | corrected | Now names the attestation requirement and its preview status |
| 93 | Failure table, Adyen deadline passed: capability no longer `allowed`, status `invalid` | A capabilities page (`invalid`: "sets the capability to `allowed`: false") | confirmed | — |
| 94 | Failure table, Adyen rule change: "Not public as a structure" | #88 | hedged | "an entry in the release notes" added |
| 95 | Failure table, compliance review rows | #38–41, #49, #89 | confirmed | — |
| 96 | Adyen: `rejected` "is final and any errors cannot be resolved by updating data or uploading documents." | A capabilities page | confirmed | — |
| 97 | Stripe expects platforms to handle risk-related requirements "by notifying connected accounts of identified issues so you can guide them to resolve through Stripe interfaces" | S/connect/handle-verification-updates.md (not the handling page) | confirmed | — |
| 98 | "Even after Stripe verifies a connected account, platforms still must monitor for and prevent fraud. Don't rely on Stripe's verification to meet any independent legal KYC or verification requirements." | S/connect/identity-verification.md | confirmed | — |
| 99 | Take-away: sanctions checks repeat "upon any new designation"; monitoring "throughout the course of a business relationship"; caps from 10 July 2027 | #14, #15, #22 | confirmed | — |
| 100 | Take-away: Stripe "typically disables payouts"; both document that a passed deadline stops the capability | #31, #46–51 | confirmed | — |
| 101 | Take-away: status of DORA, AMLR, PSD3 and PSR on 17 November 2026 | #59, #1, #77 | confirmed | — |
| 102 | Closing: identity data collected for verification feeds the risk score of the seller's account | #56 | confirmed | — |
| 103 | Publication dates in Sources: AMLR 2024-06-19, IPR 2024-03-19, DORA 2022-12-27 | Official Journal references in the texts (OJ 19.6.2024; 19.3.2024; OJ L 333, 27.12.2022) | confirmed | — |
| 104 | Stripe on Connect is a product for platforms (scene) | S/connect pages | confirmed | — |

Counts: 104 claims; 88 confirmed, 7 corrected, 9 hedged, 0 unsupported, 0 unreachable.

## Could not verify, and what I did

- **Nothing was unreachable.** Two things needed a second route: the EU texts (header change, above) and Stripe's support articles (client-rendered; the text was read from the JSON in the page source).
- **"I found no DORA statement by Stripe or Adyen"** is an absence. One search in this session found none; the sentence stays as the author's statement of what he found.
- **"No standard deadline length published" for Stripe** was checked against the three Connect pages cited and the documentation index only, not every Stripe page.
- **Stripe's KYC Refresh is in motion.** The article says public preview in Q1 2027 and a first rollout in Europe. Re-check before print: the cell and the two sentences describe the state in October–November 2026.
- **PSD3 and the PSR** had a plenary date four weeks after the research date (14 December 2026). The page says "not adopted on 17 November 2026", which is what both procedure files showed today. Re-check before print.

## Rulings and format

- Ruling 22: 21 inline external links reduced to plain attributions; each URL is in Sources and Evidence. Sources gained five entries (Stripe KYC Refresh support article; Stripe's guide on ongoing monitoring; Adyen release notes; Directive (EU) 2024/1640; procedure file 2023/0209(COD)); none removed; every entry is used in the text.
- Evidence age: DORA (2022) and the FinCEN rule (2016) are flagged in the sentence and in the source entry. No other source is older than three years.
- "Part V" in the hand-off is now `[[part-5]]`; the next part was already `[[part-6]]`. All `[[permalink]]` targets are in the style guide's list (`marketplace-regulation` is an allowed LISTED link).
- Terms: FinCEN and ICT expanded on first use. No banned words; American spelling.
- `timetoread`: 6,321 words ÷ 230 = 27; unchanged.
- No unit added, dropped, merged or reordered. Spec: five evidence or controlling-idea lines aligned with the corrections, two open-question lines updated, changelog entry added.

## Larkfield consistency

- Checked against the ledger: 230 studios, May 2026, up to 12 days; €1.12 billion ÷ 6,200 ÷ 365 ≈ €495; × 230 × 12 ≈ €1.4 million; Femke de Graaf from January 2027; Jonas Weber as owner; alerts at 14 and 3 days; Mila's pass on Tuesday 9 March 2027 (weekday correct), €117.47 on Thursday 11 March; Silent Webhook 14 September 2026, 9 hours, no weekday named; Ironworks Climbing on Stripe, Studio Noord on Adyen; K2, K4, K6. All agree. Ruling 23 (legacy Custom accounts, Larkfield collects requirements) is consistent with the scene.
- **One fix.** The closing said "one studio paused for 31 hours by a fraud control". The ledger (chapter 24's line) says an engineer switched off the studio's online payments for the 31 hours. Now "one studio's online payments paused for 31 hours in the response to a fraud attack"; the spec's callback line was changed to match.

## Ledger conflicts

- None.

## For other pages

- `34-platform-onboarding-and-verification` and any page that says Stripe has no periodic re-verification flow: Stripe's support article "KYC Refresh: Upcoming periodic confirmation requirements" (last updated October 2026) announces one (attestation requirements in `requirements`; API in private preview in 2026, public preview planned for Q1 2027; first rollout in Europe). Under K6, Larkfield's move to embedded onboarding matters here: the article says embedded components present the confirmation automatically, while API onboarding needs an integration change.
- `brief-fraud-risk-and-compliance.md` (not edited): it dates the FinCEN rule's evidence age as 8 years (it is 10 from issue, 8 from applicability) and did not find the KYC Refresh article.
- Other pages that cite `oeil.secure.europarl.europa.eu`: the host now redirects to `oeil.europarl.europa.eu`.
