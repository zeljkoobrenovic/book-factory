# Verification — 16-licences-and-safeguarding (`licences-and-safeguarding`)

Verification pass of 17 November 2026. Every source below was fetched in this session with curl (Stripe and Adyen documentation through the `.md` variants; EU texts from the Publications Office with `Accept: application/xhtml+xml` and `Accept-Language: eng`; PDFs converted with `pdftotext`), except the Stripe UK support article, which renders client-side and was read through a summarizing fetch. Quotations were compared as strings after normalizing typographic quotes and white space. Stripe's legal and guide pages redirect to a locale path by the requester's location (`/nl/…`, `/en-nl/…`); the English text was read with `Accept-Language: en-US`.

Short source names: **PSD2** = Directive (EU) 2015/2366; **EMD** = Directive 2009/110/EC; **CRR** = Regulation (EU) No 575/2013; **PS25/12** = FCA policy statement PDF; **FAQ** = Stripe's "Frequently asked questions about Stripe Connect and PSD2"; **AD** = Stripe acquirer disclosure; **H1** = Adyen H1 2026 shareholder letter (PDF linked from the investor page).

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | CRR: credit institution is "an undertaking the business of which is to take deposits … and to grant credits for its own account" | publications.europa.eu/resource/celex/32013R0575 and …/02013R0575-20260101 | corrected | The quoted sentence is the 2013 wording. The consolidated text of 1 January 2026 reads "an undertaking the business of which consists of any of the following: (a) to take deposits or other repayable funds from the public and to grant credits for its own account; (b) …". The page now quotes only the words common to both, calls it the first limb, names the consolidated text and carries an evidence-age mark (13 years), which was missing |
| 2 | PSD2 Art. 18: accounts "used exclusively for payment transactions" | publications.europa.eu/resource/celex/32015L2366 | confirmed | Art. 18(2) |
| 3 | PSD2 Art. 18: funds "shall not constitute a deposit or other repayable funds" | same | confirmed | Art. 18(3) |
| 4 | PSD2 Art. 7: capital "at no time be less than EUR 125 000" for the main payment services | same | confirmed | Art. 7(c), services 1–5 of Annex I |
| 5 | PSD2 evidence age 11 years; in force; replacement pending | same; rows 22–23 | confirmed | — |
| 6 | EMD Art. 7: "by no later than five business days" after issuance | publications.europa.eu/resource/celex/32009L0110 | hedged | The five days are the outer limit ("In any event, such funds shall be safeguarded by no later than five business days … after the issuance of electronic money"), written for funds received by payment instrument. Sentence now reads "and in any event" |
| 7 | EMD evidence age 17 years; in force | same; row 23 (PSD3 file lists it as to be repealed) | confirmed | — |
| 8 | An EEA license can be passported | FAQ; adyen.com/licenses/emea | confirmed | Both companies describe passporting |
| 9 | CSBS: "net worth (capital), surety bond, and permissible investments (liquidity) requirements" | csbs.org/csbs-money-transmission-modernization-act-mtma | confirmed | A one-clause gloss of "surety bond" added |
| 10 | CSBS: "thirty-one states have enacted the law in full or in part" | same | confirmed | Page text today: "To date, thirty-one states have enacted the law in full or in part." |
| 11 | PSD2 Art. 10: "shall not be commingled at any time with the funds of any natural or legal person other than payment service users on whose behalf the funds are held" | PSD2 | confirmed | — |
| 12 | PSD2 Art. 10: "by the end of the business day following the day when the funds have been received" | PSD2 | confirmed | — |
| 13 | PSD2 Art. 10: "shall be deposited in a separate account in a credit institution or invested in secure, liquid low-risk assets" | PSD2 | confirmed | — |
| 14 | PSD2 Art. 10: "insulated … against the claims of other creditors" | PSD2 | confirmed | Full text: "insulated in accordance with national law in the interest of the payment service users against the claims of other creditors of the payment institution" |
| 15 | PSD2 Art. 10: "an insurance policy or some other comparable guarantee" | PSD2 | confirmed | — |
| 16 | PSD2 Art. 10 applies to "all funds which have been received" | PSD2 | confirmed | — |
| 17 | FCA PS25/12 is dated 7 August 2025; rules "will come into force on 7 May 2026" | fca.org.uk/publication/policy/ps25-12.pdf; fca.org.uk/publications/policy-statements/ps25-12-… | confirmed | Para 2.33 and the instrument's commencement clause |
| 18 | The page said: "I did not confirm commencement from an FCA page published after May 2026" | fca.org.uk/firms/emi-payment-institutions-safeguarding-requirements | corrected | The FCA's safeguarding page for firms shows "Last updated: 07/05/2026" and the update note "Update following new safeguarding rules coming into effect". The page now says the rules came into force and cites this page; the disclaimer is removed |
| 19 | FCA: reconcile "at least once each reconciliation day"; "D+1 segregation requirement"; "D+1 segregation resource" | PS25/12 | confirmed | — |
| 20 | FCA: "If the D+1 segregation resource is lower than … the firm must use its own funds" | PS25/12 | confirmed | Matches; a page number falls inside the passage in the PDF |
| 21 | FCA rules add a monthly return and an annual audit; they are interim rules | PS25/12 (paras 2.22, 4.13; "'Interim rules' (the Supplementary Regime)") | confirmed | — |
| 22 | PSR procedure file: indicative plenary 14 December 2026; "Awaiting Parliament 2nd reading" | oeil.europarl.europa.eu/…reference=2023/0210(COD) | confirmed | URL changed: `oeil.secure.europarl.europa.eu` redirects to `oeil.europarl.europa.eu`; replaced |
| 23 | PSD3 is "agreed and not adopted" as well | oeil.europarl.europa.eu/…reference=2023/0209(COD) | confirmed | The page cited only the regulation's file; the directive's file shows the same status and date and is added to Sources |
| 24 | Stripe: "STEL is authorised as an electronic money institution by the Central Bank of Ireland (reference number: C187865)" | stripe.com/legal/stel | confirmed | "Last updated: April 5, 2019". Source URL `stripe.com/stel/legal` replaced with `stripe.com/legal/stel` |
| 25 | Stripe: "SPUKL is authorised as an electronic money institution by the U.K. Financial Conduct Authority (reference number: 900461)" | stripe.com/gb/legal/spukl | confirmed | "Last updated: January 26, 2017" |
| 26 | Evidence ages 7.5 and almost 10 years | rows 24–25 | confirmed | — |
| 27 | Both entities are named in the Services Agreement of 28 September 2026 | stripe.com/gb/legal/ssa | confirmed | "Last modified: September 28, 2026" |
| 28 | FAQ: "STEL passports its electronic money institution licence" | stripe.com/ie/guides/frequently-asked-questions-about-stripe-connect-and-psd2 | confirmed | "Last updated January 18, 2024" |
| 29 | FAQ: funds "are settled to Stripe's safeguarding accounts, before payout" | same | confirmed | — |
| 30 | FAQ: "only Stripe has control over the funds held in the Stripe-titled safeguarded bank account" | same | confirmed | — |
| 31 | Stripe UK support article: safeguarding accounts at credit institutions; not covered by the FSCS; no bank named | support.stripe.com/questions/safeguarding-stripe-users-funds-in-the-uk | confirmed | Client-rendered; read through a summarizing fetch, which reported the same three points. Kept as a paraphrase, as the page already says |
| 32 | Stripe Payments Company: licenses in 53 jurisdictions (49 states, DC, three territories) | stripe.com/legal/spc/licenses | confirmed | Counted 53 codes; Montana absent; GU, PR, VI present |
| 33 | "For card acquiring it is a payment facilitator of sponsor banks" | stripe.com/en-us/legal/acquirer-disclosure | corrected | "It" was Stripe Payments Company. AD says "Stripe, LLC is a Payment Facilitator of the following Payment Method Acquirers": Cross River Bank, Deutsche Bank Trust Company Americas, Fifth Third Bank, Pathward N.A., PNC Bank N.A. and Stripe MALPB. The page now names Stripe, LLC and says "six named acquirers: five banks and Stripe's own Stripe MALPB" (rulings 11 and 27); "payment facilitator" is glossed |
| 34 | Treasury docs: "Stripe is not a bank" | docs.stripe.com/treasury.md | confirmed | In the footnote, which also says "Checking accounts are provided exclusively by Fifth Third Bank, National Association"; the page now mentions the named bank |
| 35 | Treasury docs: deposit account at "Stripe's banking partner" | same | confirmed | — |
| 36 | Treasury docs: "The bank's records show that the account holds funds for the benefit of Stripe customers" | same | confirmed | Source continues ", including your business." |
| 37 | Treasury docs: "Stripe records how much of the total balance belongs to your business and reconciles that record against the funds held at the bank" | same | confirmed | — |
| 38 | Fee-credits post of 16 April 2026 by Gupta and Samant | stripe.dev/blog/how-we-built-stripe-credits-… | confirmed | Page metadata 2026-04-16; both authors named |
| 39 | "Every real Stripe financial account—merchant payment balances, bank settlement accounts, treasury accounts—is backed by a real bank account." | same | confirmed | — |
| 40 | "we can classify the money sitting behind a credit as corporate funds. It doesn't need to be safeguarded, swept to a bank account, or reconciled against a real cash position." | same | confirmed | — |
| 41 | "We reject attempts to create a transfer between a logical account and a real account at the platform level" | same | confirmed | — |
| 42 | Money movement platform "runs automated intercompany sweeps based on ledger data" | same | confirmed | — |
| 43 | Georgia approved Stripe's application for a merchant acquirer limited purpose bank (given on a secondary source) | dbf.georgia.gov/financial-institutions-bulletin-2026 (May 2026 bulletin PDF) | corrected | Primary source found. The Georgia Department of Banking and Finance's May 2026 bulletin lists "Stripe MALPB, Atlanta, Georgia", approval date 06/30/2025, begin business date 05/28/2026. The page now states the status from the regulator: approved 30 June 2025, in business since 28 May 2026 |
| 44 | A Georgia MALPB "may not solicit or accept deposits from the general public" | icba.org/w/georgia-approves-stripe-application-to-form-malpb | confirmed | Secondary source, labeled. URL changed (redirect); replaced |
| 45 | AD lists "Stripe MALPB" among US acquirers | stripe.com/en-us/legal/acquirer-disclosure; stripe.com/legal/stripe-malpb-acquirer-terms | confirmed | Added Stripe's own terms for the bank (last updated 28 May 2026): "a Georgia Merchant Acquirer Limited Purpose Bank" |
| 46 | OCC, 12 February 2026: "preliminary conditional approval" for Bridge National Trust Bank | occ.treas.gov/…/interpretations-and-decisions/2026/cd1365.pdf | confirmed | Corporate Decision #1365. URL path changed from `interpretations-and-actions` (redirect); replaced |
| 47 | OCC: "Final approval … will not be granted until all preopening requirements are met" | same | confirmed | Full: "Final approval and authorization pursuant to 12 USC 27(a) for the Bank to commence business will not be granted until all preopening requirements are met." |
| 48 | The charter is "for fiduciary and custody business" | same | hedged | The letter also says "The Bank plans to issue USD-denominated stablecoins". The page now says "fiduciary and custody business and for issuing stablecoins"; "stablecoin" is glossed |
| 49 | "I could not verify a final approval as of November 2026" | occ.treas.gov/…/index-interpretations-and-decisions.html; web search | confirmed | The OCC's list shows one entry for the bank (Corporate Decision 1365, 02/12/2026) and none later; a web search returned only reports of the conditional approval. The sentence now says what was looked at. The list would not necessarily carry a final approval, so this stays a negative finding, not proof |
| 50 | Adyen: "Adyen N.V. is authorised as a credit Institution under the supervision of Dutch Central Bank"; passport across the EEA | adyen.com/licenses/emea | confirmed | — |
| 51 | Adyen UK: "authorised as an overseas branch of an EEA credit institution" | same | confirmed | — |
| 52 | Adyen US: "Adyen N.V. San Francisco Branch is a federal Branch of Adyen, N.V., licensed by the Office of the Comptroller of the Currency and the Federal Reserve Board of Governors" | adyen.com/licenses/united-states | confirmed | — |
| 53 | Adyen's 2021 release dates the European banking license to 2017 | adyen.com/press-and-media/adyen-granted-us-branch-license | confirmed | Displayed date June 14th, 2021; "European banking license (obtained in 2017)" |
| 54 | Adyen press release of 9 April 2026: "Adyen is one of the select fintech companies that holds its own banking licenses … fund settlement times" | adyen.com/press-and-media/adyen-launches-intelligent-money-movement | confirmed | Displayed date April 9th, 2026 |
| 55 | Adyen accounts page: "interest on deposited funds" | adyen.com/accounts | confirmed | "Submerchants in the US and EU can earn interest on deposited funds." |
| 56 | "What the bank status means for how merchant funds are held is not on those pages" | docs.adyen.com/platforms/compliance-financial-products/eu-depositor-info-sheet.md | corrected | Adyen's documentation has an EU depositor information sheet (required for business accounts per the compliance-guidelines page): "Deposits in Adyen N.V. are protected by: Dutch statutory Deposit Guarantee Scheme", "EUR 100 000 per depositor per credit institution". The paragraph now states this for the business-account product and says that nothing covers balances waiting for payout |
| 57 | Sales day payout terms (17 June 2024): "irrespective of whether the funds are actually received by Adyen from the Acquirer or Scheme Owner" | adyen.com/legal/sales-day-payout-terms-of-service | confirmed | "Last update 17 June 2024" (ruling 18) |
| 58 | "Prefinancing is capped at 30 days" | docs.adyen.com/account/sales-day-payout/upgrade-to-sdp.md | confirmed | — |
| 59 | Inference block: "Adyen's pages do not say this" | row 56 | corrected | Now: Adyen's pages call the money in its business accounts deposits at Adyen N.V. and say nothing of the kind about a balance waiting for payout. The inference itself is unchanged and stays labeled |
| 60 | H1 2026 letter: "We ended the half with €12.4 billion of total cash. The majority of that number represents balances moving through our system on behalf of our merchants" | investors.adyen.com/financials/h1-2026-c2a1a (PDF link on the page) | confirmed | Re-fetched (46-page PDF); the source entry no longer says "not re-fetched" |
| 61 | H1 2026 letter: finance income "generated primarily from our balances at central and commercial banks"; dated 13 August 2026 | same | confirmed | — |
| 62 | Services Agreement names "Stripe Payments Europe, Limited" with "Stripe Technology Europe, Limited" (EEA) and "Stripe Payments UK Ltd" (UK) | stripe.com/gb/legal/ssa | confirmed | The UK row also covers Gibraltar and Switzerland |
| 63 | Adyen: "You must have a separate balance platform for each region in which you acquire payments" | docs.adyen.com/platforms/account-structure-resources.md | confirmed | — |
| 64 | FAQ: "the platform does not have possession of user's funds at any point" | FAQ | confirmed | — |
| 65 | FAQ: "pre-agreed instructions"; "does not have discretionary authority over the funds" | FAQ | confirmed | — |
| 66 | FAQ: platforms "would generally only be considered to be engaged in providing payment services where they are in possession or control of user funds" | FAQ | confirmed | — |
| 67 | Stripe payfac guide: about US$450,000 over about three years for fifty states; e-money license can cost millions of euros ("served to me in Dutch, so paraphrased") | stripe.com/guides/payfacs | corrected | Read in English this time. The paraphrase is replaced by the quotations "US$150,000/year for approximately 3 years to set up 50 states = US$450,000 minimum" and "Platforms that control the flow of funds need to acquire an e-money license, which can take months and millions of euros to obtain." The guide is undated and its one dated reference is a September 2018 report; the page now says so |
| 68 | "Global Payouts is best for businesses that already hold the licenses required to move money themselves." | docs.stripe.com/global-payouts.md | corrected | Words match, but the source sentence continues ("… and want a payouts-only solution decoupled from payments"); the full stop is moved outside the quotation |
| 69 | "If you manage your customers' funds, you might need a license such as an MTL"; "you're responsible for any desired tracking of recipient funds"; "Covered by Stripe's licensing" | docs.stripe.com/connect/cross-border-payouts-to-recipients/compare-global-payouts.md | confirmed | — |
| 70 | FAQ expects two exemptions to be narrowed by PSD3 | FAQ | confirmed | "both the commercial agent and limited network exemptions—is likely to be narrowed" |
| 71 | FDIC, 17 September 2024: "an important step to ensure that banks know the actual owner of deposits … even if the third party fails" | fdic.gov/news/press-releases/2024/fdic-proposes-deposit-insurance-recordkeeping-rule-banks-third-party | confirmed | Said by Chairman Martin J. Gruenberg; Synapse named once, not described |
| 72 | Table, EEA row (Stripe and Adyen cells) | rows 24, 28, 50 | confirmed | — |
| 73 | Table, UK row | rows 25, 27, 51 | confirmed | — |
| 74 | Table, US row | rows 32–34, 43, 52, 53 | confirmed | Stripe cell now says "five sponsor banks plus its own Georgia acquiring bank, in business since May 2026" |
| 75 | Table, "Where customer funds sit", Adyen: "Not public" | row 56; docs.adyen.com/llms.txt searched for safeguard, deposit, licens | corrected | Replaced with the documented fact for business accounts; "Not public" kept for balances waiting for payout |
| 76 | Table, "Paying out before funds arrive", Stripe: "Not public for standard payouts" | docs.stripe.com/payouts/instant-payouts.md | corrected | Ruling 18: Stripe documents paying ahead for Instant Payouts. Cell now quotes "Funds acquired from card payments are available for Instant Payouts as soon as the charge is complete"; source added |
| 77 | Larkfield walk-through and map: the holder for studios on Adyen is "Adyen N.V." "as the provider documents it" | adyen.com/licenses/emea; ruling 27(b); ledger line for chapter 1 | hedged | Adyen names no entity per country, so this is a reading of the license page. The walk-through now says so and the column header reads "as read from the provider's public pages" |
| 78 | "When It Goes Wrong": no deposit guarantee behind Stripe's UK e-money institution; a Stripe bank appeared in the acquirer disclosure; a trust bank conditionally approved; EU rules weeks from a vote | rows 31, 45, 46, 22 | confirmed | — |

Counts: 78 checked; 65 confirmed, 10 corrected, 3 hedged, 0 unsupported, 0 unreachable.

## Rulings and format

- Ruling 22: 22 inline external links reduced to plain attributions; every URL is in Sources and Evidence.
- Rulings 11 and 27: the US acquiring sentence now names Stripe, LLC, "six named acquirers" and Stripe's own bank; the page makes no claim that Adyen publishes or does not publish a list per country, and the one place that named Adyen N.V. as holder is now marked as a reading.
- Ruling 18: the comparison table no longer says "Not public" for Stripe on paying out ahead.
- Sources added: Stripe MALPB Acquirer Terms; Stripe Instant Payouts; Adyen EU depositor information sheet; FCA safeguarding page; PSD3 procedure file; OCC list of decisions; Georgia bulletin; consolidated CRR. No entry was unused.
- `[[part-3]]` replaces plain "Part III" in the hand-off. "Keel" is glossed on first use. `timetoread` changed from 28 to 25 (5,659 words ÷ 230).
- No unit was added, dropped, merged or reordered; `validate_spec.py` and `check_draft.py structure` pass. Two resolved open questions were removed from `spec.json`, one was reworded and one added.

## Could not verify

- **Stripe's UK safeguarding article** renders client-side; curl returns only the title. Read through a summarizing fetch, so the page keeps its paraphrase and no quotation.
- **Final approval of Bridge National Trust Bank**: not found. A negative result from the OCC's decisions list and a web search; the page says exactly that.
- **Regulators' registers** (Central Bank of Ireland, FCA, DNB, OCC) were not queried; the page already says every license statement is the company's own.
- **What became of the FDIC's 2024 proposal** was not checked; the page already says so.
- The EU texts need the headers `Accept: application/xhtml+xml` and `Accept-Language: eng`; without the second the Publications Office answers 400 or 404. The links work in a browser.

## Ledger conflicts

None. Dates, weekdays (Tuesday 9 March 2027, Thursday 11 March 2027), €120.00, €117.47, €2.53, €84.00, €1.12 billion, €46.0 million, €412,000, 1,140 studios, the five markets and the chapter's own ledger line (April 2027, €43 million) agree. €1.12 billion ÷ 365 × 14 = €42.96 million.

## For other pages

- Any page that says Stripe's Georgia bank is "approved" or cites only the trade association: the Georgia regulator's May 2026 bulletin gives approval 30 June 2025 and start of business 28 May 2026, and Stripe's own terms for the bank are dated 28 May 2026.
- Any page that says the FCA's safeguarding rules "will" come into force, or that commencement was not confirmed: the FCA's page for firms was updated on 7 May 2026 "following new safeguarding rules coming into effect".
- Any page that says Adyen publishes nothing on deposit protection (chapters 13, 36, 47): the EU depositor information sheet in Adyen's documentation covers business accounts.
- Chapter 6: the US payment facilitator is Stripe, LLC; the money transmitter is Stripe Payments Company. They are different entities.
- `[[stripe-and-adyen-bets-compared]]` does not resolve yet because `48-the-bets-compared` is not written; the render check reports it for this page.
