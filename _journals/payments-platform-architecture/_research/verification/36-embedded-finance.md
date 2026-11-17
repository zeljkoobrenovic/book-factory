# Verification — 36-embedded-finance (`embedded-finance`)

Verification pass of **17 November 2026**. Every source below was fetched on that day, in this session, with curl: Stripe and Adyen documentation through the `.md` variants, Adyen's H1 2026 shareholder letter as the 46-page PDF linked from the investor page, Stripe's 2025 annual letter as the PDF linked from the letter page (both converted with `pdftotext`), and PSD2 from the Publications Office with `Accept: application/xhtml+xml`. Quotations were compared as strings after normalizing typographic quotes and white space. All availability and status claims on this page are statements about what the documentation said on 17 November 2026; none of the documentation pages carries a publication date (ruling 30).

Short source names. Stripe (`docs.stripe.com/…`): **S-tr** = treasury; **S-t4p** = treasury/connect; **S-req** = treasury/connect/requirements; **S-leg** = treasury/connect/legacy/v1 (the old URL `financial-accounts/connect` redirects here); **S-legreq** = treasury/connect/legacy/v1/requirements; **S-iss** = issuing; **S-how** = issuing/how-issuing-works; **S-glob** = issuing/global; **S-icon** = issuing/connect; **S-rta** = issuing/controls/real-time-authorizations; **S-spend** = issuing/controls/spending-controls; **S-cap** = capital/how-capital-for-platforms-works; **S-risk** = connect/risk-management; **S-inst** = connect/instant-payouts; **S-rel** = release-phases; **S-letter** = Stripe's 2025 annual letter (PDF). Adyen (`docs.adyen.com/…`): **A-ba** = business-accounts; **A-gs** = business-accounts/get-started; **A-iss** = issuing; **A-auth** = issuing/authorisation; **A-rel** = issuing/authorisation/relayed-authorisation; **A-cap** = capital; **A-how** = capital/how-capital-works; **A-plat** = platforms; **A-ver** = platforms/verification-requirements; **A-acct** = platforms/account-structure-resources; **A-pay** = platforms/custom-payouts/on-demand-payouts; **H1** = Adyen H1 2026 shareholder letter (PDF).

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe: financial accounts "receive your settled Stripe earnings, hold funds, and support capabilities such as physical or virtual cards" | S-tr | confirmed | Inline link removed (ruling 22) |
| 2 | Adyen business account: a seller can be paid out into it instead of a bank account elsewhere | A-ba | confirmed | "receive payouts directly to their Adyen business account instead of paying out to a third-party bank account" |
| 3 | Adyen: "Creating a payment instrument issues a card" | A-iss | confirmed | — |
| 4 | Adyen: a balance account "can have one or more payment instruments that can deduct funds from it" | A-iss | confirmed | One-clause gloss of "balance account" added at this first use |
| 5 | Stripe: a card draws on a balance attached to the seller's account | S-how | confirmed | "An Issuing balance is a funding source attached to a connected account" |
| 6 | Adyen Capital: users "repay daily based on a fixed percentage of their processed volume through Adyen" | A-cap | confirmed | — |
| 7 | Stripe Capital: "withholds a fixed percentage of each transaction until the complete balance is repaid" | S-cap | confirmed | — |
| 8 | Adyen H1 2026 letter: "We also capture post-transaction value through our embedded financial products, enabled by our banking licenses. By offering native business accounts, card issuing, and capital within a single integration..." | H1 (PDF, p. 11) | confirmed | Letter dated August 13, 2026. The source entry said the download was not re-read; it was re-fetched and read, and the entry now says so |
| 9 | Adyen documentation: "business financing offers from Adyen"; Adyen is the lender | A-plat; H1 note on financial products ("Capital, in the form of loans and advances") | confirmed | — |
| 10 | Stripe: "Stripe is not a bank. Checking accounts are provided exclusively by Fifth Third Bank, National Association, Member FDIC" | S-tr (footnote) | confirmed | Attribution with "(n.d.)" added in the sentence. The same page says a checking account "is only available in the US"; the comparison table now says "US deposits" |
| 11 | Stripe Issuing partners "with multiple trusted banks" | S-how | confirmed | — |
| 12 | US loans from "Celtic Bank or Lead Bank" | S-cap | confirmed | — |
| 13 | Other financing from outside lenders: Fundbox in Australia and Canada, YouLend in Germany, France and the UK | S-cap | corrected | The page's US table also lists a merchant cash advance provided by YouLend, so "US = banks, elsewhere = outside lenders" was incomplete. The sentence now adds "and for US cash advances" |
| 14 | Stripe: "Treasury platforms must maintain a fraud risk management process that includes proactive measures to prevent and monitor unauthorized or fraudulent activity" | S-req | confirmed | — |
| 15 | Adyen: "You will always be the point of contact for your users" (the page cited business-accounts/get-started) | A-iss; A-gs | corrected | The sentence is on the Adyen Issuing page (A-plat has "You are always the point of contact for your users" under card issuing). It is not on A-gs. The text now attributes it to the Issuing page |
| 16 | Adyen business accounts: platform must "Implement Adyen's Authentication SDK to comply with the PSD2 regulations for online transactions" | A-gs | confirmed | — |
| 17 | PSD2 requires strong customer authentication | publications.europa.eu/resource/celex/32015L2366 (Art. 97) | confirmed | Acronym expanded with its year; the directive added to Sources with its evidence age (11 years, in force) |
| 18 | Stripe: "If your Issuing balance has insufficient funds for the incoming authorization, the authorization will be denied and your webhook endpoint won't receive the `issuing_authorization.request` event" | S-rta | confirmed | — |
| 19 | Stripe spending controls can block merchant categories or countries | S-spend | confirmed | — |
| 20 | Adyen internal checks cover "The available balance in your account" | A-auth | confirmed | — |
| 21 | Adyen: stored transaction rules approve or decline automatically, before relayed authorisation | A-auth (flow steps 2–5) | confirmed | — |
| 22 | Stripe "sends it to your configured endpoint for your approval" | S-rta | confirmed | — |
| 23 | Adyen "sends a webhook to your server"; the feature is called relayed authorisation | A-auth | confirmed | — |
| 24 | Stripe: "If Stripe doesn't receive your approve or decline response within 2 seconds, the `Authorization` is automatically approved or declined based on your timeout settings, or Autopilot settings, if configured" | S-rta | confirmed | — |
| 25 | Adyen: "Your server has up to 2000 milliseconds to respond. If we do not receive a response within this timeframe, we apply your default fallback" | A-auth | confirmed | — |
| 26 | Requirements table: Adyen fallback "Default approval" or "Default refusal" | A-rel | confirmed | — |
| 27 | Requirements table: Adyen HTTP 4xx or 5xx, the default fallback applies | A-rel | confirmed | "If we receive an HTTP 4xx or HTTP 5xx error code, we will apply your default fallback logic" |
| 28 | Requirements table: Stripe error response "Not stated on the page read" | S-rta | corrected | The page does state part of it: a response Stripe cannot process is recorded with `request_history.reason` = `webhook_error`, and Autopilot (public preview) can then decide. What decides without Autopilot is not stated. The cell now says this |
| 29 | Requirements table: when the platform is not asked (Stripe: balance too low; Adyen: its checks or a transaction rule already refused) | S-rta; A-auth | confirmed | — |
| 30 | Stripe: when `request_history.reason` is `webhook_error` or `webhook_timeout`, "Stripe isn't receiving your responses" | S-rta | confirmed | — |
| 31 | Release stages defined (generally available; public preview "open on request"; private preview or pilot; in development) | S-rel; Adyen documentation index (docs.adyen.com/llms.txt) | corrected | Stripe's release-phases page says public preview is "Open to any user with a Stripe account" (some require a request), private preview is "by invitation only", general availability is "Feature-complete". The definitions now follow that page and cite it. Adyen's index lists no page defining "pilot" or "development phase"; the text says Adyen defines neither |
| 32 | Stripe: "Treasury for platforms is in public preview for platforms and connected accounts in the UK" | S-req; S-t4p (GB under "Public preview") | confirmed | "Connected accounts" glossed here, at first use |
| 33 | Stripe: "in private preview for platforms and connected accounts in the US, AU, and the EU" | S-req; S-t4p | hedged | The quotation is exact, but Stripe's overview page lists 24 private-preview countries: 21 EU member states, AU, US and **CA**. Canada is not in the requirements page's sentence. The text now states the difference instead of choosing a page |
| 34 | Access to Treasury for platforms goes through sales | S-req; S-t4p | confirmed | "contact sales to request access" |
| 35 | Legacy version: "Don't build a new v1 integration"; United States only | S-leg; S-legreq | confirmed | URL in Sources replaced with the redirect target |
| 36 | Adyen business accounts: "This feature is in development phase. Some of the APIs, documentation, and processes may change as the feature evolves." | A-ba | confirmed | Banner present on 17 November 2026 |
| 37 | Stripe business cards: 24 countries (US, Canada, UK and 21 in the EEA) | S-glob | confirmed | Counted: AT BE BG CA CY DE EE ES FI FR GB GR HR IE IT LT LU LV MT NL PT SI SK US |
| 38 | Stripe consumer cards: private preview | S-how; S-iss | confirmed | S-how labels the consumer card program "Private preview"; S-iss says "Consumer issuing is available in the US". Cell now reads "Consumer cards (US)" |
| 39 | Stripe stablecoin-backed cards: public preview | S-how; S-glob | confirmed | "Stablecoin" glossed in the cell |
| 40 | Adyen Issuing: supported in the EEA, the UK and the US | A-iss; A-ver | confirmed | Both Adyen pages agree |
| 41 | Adyen: debit cards for organizations and sole proprietors | A-ver; A-plat | confirmed | — |
| 42 | Stripe financing: Australia, Canada, Germany, France, UK, US, through partner lenders | S-cap | confirmed | — |
| 43 | Stripe US line of credit: private preview | S-cap | confirmed | — |
| 44 | Adyen Capital: Finland, France, Netherlands, Spain, Sweden, UK, Canada (not Saskatchewan), US, Australia | A-cap | confirmed | — |
| 45 | Adyen Capital "invite-only" | A-ver | confirmed | "Available on an invite-only basis"; A-cap has "Request an invite" |
| 46 | Adyen: repeat grants "in a pilot phase" | A-how | confirmed | "Subsequent grants are currently in a pilot phase" |
| 47 | Financing reaches Germany on Stripe and not Adyen, the Netherlands on Adyen and not Stripe | S-cap; A-cap | confirmed | — |
| 48 | Stripe: where Stripe bears negative balances, "Your platform can't use Stripe Treasury or Issuing" | S-risk | confirmed | — |
| 49 | Stripe: "Issuing only supports connected accounts that don't use a Stripe-hosted Dashboard, and where your platform is responsible for requirements collection and loss liability" | S-icon; S-how | hedged | The quotation is exact, but the next block on S-icon says "Enabling Issuing on non-custom connected accounts is a new feature. Contact Stripe support to request access." The text now reports both; the "Depends on context" bullet and the comparison cell say a hosted dashboard rules out cards unless Stripe grants access |
| 50 | The Adyen pages read state no loss condition for accounts or cards | A-ba; A-gs; A-iss; A-ver; A-plat | confirmed | True of the pages read; the sentence was already scoped to "the Adyen pages read" |
| 51 | Adyen: business accounts must be "enabled for your balance platform" | A-gs | confirmed | — |
| 52 | Adyen account verification: source of funds, a tax classification, "A live selfie photo" and photo ID for each signatory | A-ver | confirmed | The tax classification is FATCA/CRS, for organizations |
| 53 | Adyen card verification: VAT number or tax ID, and source of funds | A-ver | confirmed | VAT expanded |
| 54 | Neither company gives a date for general availability of its account product | S-t4p; S-req; A-ba; A-gs | confirmed | No date on the pages read; not an exhaustive search of either site |
| 55 | Adyen's product page lists 20 eurozone countries for business accounts | A-ba | corrected | The page lists 20 eurozone countries **and** mainland United Kingdom **and** the United States. The text now says so |
| 56 | Adyen's verification page lists "BE, DE, ES, FR, GB, NL and US" for business accounts | A-ver | confirmed | The two Adyen lists still conflict on 17 November 2026; the text says so and says the author cannot tell which is current |
| 57 | Stripe's documentation counts 24 issuing countries | S-glob | confirmed | "Use local issuing in 24 countries" |
| 58 | Stripe's annual letter (February 2026): "our Issuing product is available in only 22 countries some 7 years after launch" | S-letter (PDF) | hedged | Quotation exact. The page presented 24 against 22 as a disagreement; the letter is nine months older than the check, so the count may have grown. The text now says "nine months older". The PDF's date line extracts as "February 24, 202" (last digit clipped); the year is taken from the letter being the 2025 annual letter |
| 59 | Every documentation page is undated | all `docs.` pages | confirmed | Ruling 30 |
| 60 | Where They Differ, row 1 (license) | claims 8–13 | confirmed | "US deposits" |
| 61 | Where They Differ, row 2 (accounts) | claims 32–36 | corrected | Stripe cell said "private preview elsewhere"; now "private preview in the US, Australia, the EU and, on one page, Canada" |
| 62 | Where They Differ, row 3 (business cards) | claims 37–41 | confirmed | — |
| 63 | Where They Differ, row 4 (time to answer) | claims 24–25 | confirmed | — |
| 64 | Where They Differ, row 5 (financing: six countries, lender varies; nine countries, invite-only, Adyen lends) | claims 42–46 | confirmed | — |
| 65 | Where They Differ, row 6 (condition on the platform) | claims 48–53 | hedged | Stripe cell gains "other account types on request" (claim 49) |
| 66 | Larkfield table: Stripe Issuing offered in NL, DE, BE, UK, US; Adyen Issuing in the EEA | S-glob; A-iss | confirmed | — |
| 67 | Larkfield table: Stripe Issuing balance filled from the Stripe balance or by bank top-up | S-how | confirmed | — |
| 68 | Larkfield table: account product private preview in NL, DE, BE, US; public preview in the UK; in development on Adyen | S-t4p; A-ba | confirmed | — |
| 69 | Adyen: "Funds can be deducted from this account if your users' balance accounts incur negative balances due to refunds and chargebacks" | A-acct | confirmed | — |
| 70 | Stripe: "When platforms and marketplaces are liable for losses, you're liable for uncovered negative balances due to refunds or disputes on instantly paid out funds." | S-inst | confirmed | — |
| 71 | Stripe Instant Payouts "typically settle in the associated debit card or bank account within 30 minutes" | S-inst | confirmed | — |
| 72 | An Adyen payout can request an instant route where the bank supports one | A-pay | confirmed | The claim had no entry in Sources. Page read: priority "instant"; "some do not support **instant** transfers". Source added |
| 73 | Closing: on Stripe a refund of a payment made through the platform debits the platform's balance | docs.stripe.com/connect/destination-charges (variant `?platform=web&ui=elements`) | confirmed | "leaving the platform account to cover the negative balance from the refund"; owned by chapters 33 and 35, not added to this page's Sources |
| 74 | Closing: on Adyen the refund is deducted from the studio's balance account, with the liable balance account behind it | A-acct; docs.adyen.com/platforms/how-adyen-applies-split-instructions | confirmed | The mechanism is documented (split instructions on a refund; liable balance account). Which account Larkfield names is Larkfield's configuration (ledger, chapter 35) |

Counts: 74 claims checked; 64 confirmed, 6 corrected (13, 15, 28, 31, 55, 61), 4 hedged (33, 49, 58, 65), 0 unsupported, 0 unreachable, 0 not checked. Row 8 is confirmed, with its Sources entry updated. Rows 60–65 restate earlier rows in the comparison table and are counted once each.

## Where two pages of one provider disagree (stated in the text, not resolved)

- **Adyen, business-account countries.** `business-accounts` lists 20 eurozone countries, mainland United Kingdom and the United States. `platforms/verification-requirements` (tab "Business accounts") lists "BE, DE, ES, FR, GB, NL and US". Both read on 17 November 2026. The chapter reports both and says which is current cannot be told.
- **Stripe, Treasury for platforms private preview.** `treasury/connect/requirements` says "the US, AU, and the EU". `treasury/connect` lists country codes that include CA. The chapter reports both.
- **Stripe, Issuing country count.** Documentation: 24 countries. Annual letter of February 2026: 22. Reported with the nine-month gap.
- **Stripe, not used in the text:** `issuing/how-issuing-works` still says "Treasury for platforms is only available to platforms and connected accounts located in the United States" and links to the legacy requirements page, which contradicts the v2 pages. `issuing` says "Consumer issuing is available in the US" while `issuing/how-issuing-works` marks the consumer card program "Private preview".
- **Adyen, not used in the text:** the prose on `business-accounts` says "the Eurozone (excluding specific Nordic territories)" and the list beneath it includes Finland.

## Could not verify, and what I did

- **The year on Stripe's annual letter.** The PDF text gives "February 24, 202". The HTML page carries no date string. The text says "February 2026"; the Sources entry keeps 2026-02-24, which other verified pages of this book also use.
- **Spendable time of a sale on an issued card**, and **who bears the credit loss on an unpaid grant**: not stated on the pages read. The chapter already says the first must be confirmed with each provider and makes no claim about the second.
- **The build.** `python3 _wiring/build.py` ended three times with `OSError: Directory not empty` in another journal's output folder (parallel builds by other reviewers); the fourth run printed `[built] payments-platform-architecture` with no error, and the built page contains the edited text.
- **Render check.** `render_check.py embedded-finance` reports one unresolved link, `[[stripe-and-adyen-bets-compared]]`. The permalink is in the style guide's valid list; the folder `48-the-bets-compared` named in `config.yaml` does not exist yet. No `XJ:` entries.

## Format and rulings applied

- Ruling 22: 16 inline external links reduced to plain attributions; every URL is in Sources.
- Part references: "Part VII" (twice) and "Parts II to VII" now use `[[part-7]]` and `[[part-2]]`.
- Terms glossed at first use: balance account, connected accounts (moved from a later quotation to the first use), stablecoin, VAT, PSD2.
- Sources: legacy URL replaced by its redirect target; entries added for Stripe's release phases, Adyen's on-demand payouts and PSD2; no unused entries.
- `timetoread` 16 → 17 (3,799 words ÷ 230 = 16.5). The spec's limit is 3,800 words, so every addition was paid for with a trim inside the same unit. No unit was added, dropped, merged or reordered.

## Larkfield consistency

Checked against the ledger: 19:42 on Tuesday 9 March 2027, €120.00 and €117.47, payout Thursday 11 March, refund of €84.00 on 18 March, Ines Bakker's question of 10 March, May and June 2027, the five questions and four conditions, 2,610 / 1,140 / 2,450 studios (650 + 1,100 + 700), 6,200 studios, €156 million, legacy Custom connected accounts (ruling 23). No contradiction found.

## Ledger conflicts

None.

## For other pages

- Any page that cites Adyen's business-account countries, or Stripe's Treasury for platforms preview countries, should state the same two conflicts rather than one list.
- Any page that says a Stripe-hosted dashboard excludes Issuing should add that Stripe's Issuing with Connect page now calls Issuing on non-Custom accounts "a new feature" available on request.
- `[[stripe-and-adyen-bets-compared]]` does not resolve until chapter 48 exists.
