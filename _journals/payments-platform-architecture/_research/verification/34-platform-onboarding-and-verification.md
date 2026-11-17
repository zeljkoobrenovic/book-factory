# Verification — 34-platform-onboarding-and-verification

Verified 17 November 2026. Every source below was fetched in this session (`curl`, the `.md` variants of docs.stripe.com and docs.adyen.com; stripe.com and support.stripe.com as HTML) and the passage read. Quotations were compared with the fetched text by script after normalizing typographic quotes and markdown markup. Short forms: S = docs.stripe.com/connect, A = docs.adyen.com/platforms.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Key point: Stripe "typically disables payouts" at a missed deadline "and charges only later" | S/handling-api-verification.md?accounts-namespace=v1 | hedged | Source says charges "might also" be disabled if payouts are already disabled and the account is unresponsive. Now "may disable charges if the account stays unresponsive". |
| 2 | Key point: Adyen standard deadline 30 days (payout capabilities), 60 (receiving payments) | A/verification-overview.md | confirmed | Table read: 30-day group includes `sendToTransferInstrument`; 60-day group includes `receivePayments`. |
| 3 | Key point: API onboarding "Requires integration changes"; review "at least every 6 months" | S/onboarding.md | confirmed | |
| 4 | Key point, Established, synthesis: neither provider publishes a conversion figure for any onboarding flow | stripe.com/blog/connect-express-onboarding | corrected | Stripe blog, 24 June 2019: updates to Express onboarding "drove a 5.3% average increase in conversion rates"; customer quote of 17% (also on stripe.com/connect/onboarding). Page now says no completion rate and no comparison of flows is public, cites the 2019 figure as a vendor claim with evidence age 7 years. |
| 5 | Capability definition quote (Stripe) | S/account-capabilities.md?accounts-namespace=v2 | confirmed | Exact. The bare URL is now only an index of two variants; Sources URL changed to the v2 variant (quote is on v1 and v2). |
| 6 | Requirements "describe the account information that Stripe needs…" | S/handling-api-verification.md?accounts-namespace=v2 | confirmed | |
| 7 | Adyen "As required by payment industry regulations, Adyen must verify…" | A/verification-overview.md | confirmed | |
| 8 | Stripe "The capabilities you request … Requesting more capabilities means…" | S/account-capabilities.md (v1, v2) | confirmed | |
| 9 | Stripe "typically disables payouts on the account if we don't receive the information by the `current_deadline`" | S/handling-api-verification.md?…=v1 | confirmed | |
| 10 | Adyen "If the user does not resolve the verification issues in a timely manner, their capabilities will be disallowed." | A/verification-overview.md | confirmed | |
| 11 | Stripe requirements "vary by account, depending on" country, capabilities, business type, business structure, service agreement, risk level | S/identity-verification.md | confirmed | Six-item list read; "(for example, individual, company)" exact. |
| 12 | Adyen "legal entity type and operating country determine the required verification information" | A/onboard-users.md | confirmed | |
| 13 | Adyen Belgium / United Kingdom sole proprietorship example | A/verification-requirements.md | confirmed | |
| 14 | Adyen general list for an organization (legal name, registration number, registered address, bank account, UBOs, controllers, signatories) | A/verification-requirements.md | confirmed | |
| 15 | "Adyen's criterion is ownership of '25% or more…'" | A/verification-requirements.md | hedged | The 25% rule is Adyen's test for UBOs through ownership; it also has UBOs through control. Now "Adyen's criterion for ownership is". |
| 16 | Stripe "For some capabilities, requesting them enables them permanently…" | S/account-capabilities.md (v1, v2) | confirmed | |
| 17 | Adyen "In the design phase, you set the default capabilities…" and "you must request the additional capability. In some cases, this requires more verification." | A/verification-overview.md | confirmed | |
| 18 | Stripe up-front vs incremental quotes (three) | S/identity-verification.md; S/hosted-onboarding.md | confirmed | |
| 19 | Adyen "As a platform, you should collect verification data from your users upfront…" | A/verification-overview/verification-types.md | confirmed | |
| 20 | Adyen "Only payment facilitators can use staggered verification" | A/verification-overview/verification-types.md | confirmed | See note 1 below on the gloss of "payment facilitator". |
| 21 | Adyen "When a user is moved to a higher tier, their payouts are temporarily disallowed…" | same | confirmed | |
| 22 | Adyen: four tiers, no amounts on that page | same | confirmed | "There are four tiers."; the page gives currencies, no amounts. |
| 23 | Stripe lists hosted, embedded and API onboarding under those names | S/onboarding.md | confirmed | |
| 24 | Adyen lists "Hosted onboarding" and "API-only onboarding", with components for the platform's interface | A/onboard-users.md | confirmed | |
| 25 | Stripe hosted: "a web form hosted by Stripe with your brand's name, color, and icon"; reached by an Account Link | S/onboarding.md; S/hosted-onboarding.md?…=v2 | confirmed | |
| 26 | Stripe "You can only use each temporary Account Link URL once…" and "Don't email, text, or otherwise send account link URLs…" | S/hosted-onboarding.md?…=v2 | confirmed | The page also says "Authenticate the account in your application before redirecting", which supports "assumes a seller who is logged in". |
| 27 | Adyen hosted onboarding "our recommended solution"; "API-initiated"; "Onboarding on invite"; "All actions are performed in your Customer Area" | A/onboard-users.md | confirmed | |
| 28 | Adyen "can securely access the hosted onboarding link with an SMS authentication" | A/onboard-users.md | confirmed | |
| 29 | Adyen release of 4 May 2026: "you can now choose to automatically send the hosted onboarding link by email instead of copying it manually" | docs.adyen.com/release-notes/platforms-and-financial-products.md | confirmed | Entry heading "2026-05-04 — Hosted onboarding"; applies to Onboarding on Invite. |
| 30 | Stripe "You embed the Account onboarding component directly in your application…" | S/onboarding.md | confirmed | |
| 31 | AccountSession expresses "your intent to delegate API access to your connected account" | S/get-started-connect-embedded-components.md?platform=web | confirmed | |
| 32 | Embedded component reads the account's requirements; no "need to update your onboarding integration as compliance requirements change" | S/onboarding.md | confirmed | |
| 33 | Adyen Onboarding components "only cover certain functionality…" | A/onboard-users/components.md | confirmed | The page today lists one component (Transfer Instrument). |
| 34 | Stripe API onboarding: "build an onboarding flow and handle identity verification, localization, and error handling…"; six-month sentence | S/onboarding.md | confirmed | |
| 35 | Stripe table row: automatic updates "Immediate" / "Immediate" / "Requires integration changes"; new countries supported without integration changes for the first two only | S/onboarding.md | confirmed | |
| 36 | Stripe "We don't recommend this option unless…" | S/onboarding.md | confirmed | |
| 37 | Adyen "complete control over the user journey within your platform's environment"; no review interval published | A/onboard-users.md; A/onboard-users/onboarding-versions.md | confirmed | No interval found in the onboarding, versions or guidelines pages. |
| 38 | "own forms also mean that sellers' identity documents pass through the platform's servers" | S/handling-api-verification.md (Files API); S/api-onboarding.md | hedged | Neither provider says this; Stripe's API onboarding collects documents in client-side forms and uploads through the Files API. Now "by my reasoning, the platform's code handles sellers' identity documents"; table cell now "The platform's own form". |
| 39 | Stripe "In most configurations, Stripe is responsible for collecting KYC requirements… `losses_collector` to `application` and `dashboard` to `none`." | S/accounts-v2/connected-account-configuration.md | confirmed | |
| 40 | Stripe "risk reviews … can add extra requirements, which you can't provide using the API"; provided "through a Connect embedded component, Stripe-hosted onboarding, or a remediation link" | S/handling-api-verification.md?…=v2 | confirmed | |
| 41 | Adyen: no rule tying hosted vs API-only to liability ("Not public as a rule") | A/onboard-users.md, onboarding-versions.md, verification-requirements/onboarding-guidelines.md; docs.adyen.com/llms.txt | confirmed | Searched for "liab", "must use hosted", "required"; nothing found. |
| 42 | Adyen events "When users change their data"; "Periodic data reviews required by Adyen" | A/verification-overview.md | confirmed | |
| 43 | Stripe periodic re-verification (ruling 36) | support.stripe.com/questions/kyc-refresh-upcoming-periodic-confirmation-requirements | corrected | The page attributed periodic reviews to Adyen alone. Article read (raw HTML; "Last Updated: October 2026"): KYC Refresh, first rollout in Europe, API in private preview in 2026, public preview Q1 2027. One clause and a source entry added. The page never said "not public" for this. |
| 44 | Stripe "Stripe frequently updates KYC requirements, often due to changes…" | S/handle-verification-updates.md?…=v1 | confirmed | |
| 45 | Stripe "At certain variable thresholds—usually when a specified amount of time has passed or volume of charges have been made…" | S/identity-verification.md | confirmed | |
| 46 | Stripe "However, other consequences might apply… Stripe might also disable the ability to process charges." | S/handling-api-verification.md?…=v1 | confirmed | |
| 47 | Adyen "30-day period" for `sendToTransferInstrument`, "60-day period" for `receivePayments` | A/verification-overview.md | confirmed | |
| 48 | Adyen "Users are allowed to continue using the capabilities"; "a standard deadline could be shortened or removed in specific situations" | A/verification-overview.md | confirmed | |
| 49 | Stripe "Responsible platforms must also monitor their connected accounts' requirement statuses…" | S/handling-api-verification.md (v1, v2) | confirmed | Context: platforms that onboard through the API and collect requirements. |
| 50 | Adyen "can select **Invite decision-maker**…" | A/onboard-users.md | confirmed | |
| 51 | Stripe Notification banner "lists open tasks that can affect a connected account's status or capabilities" | S/supported-embedded-components/notification-banner.md | confirmed | |
| 52 | Stripe "You don't need to identify the specific requirements, because the onboarding interface knows…" | S/hosted-onboarding.md?…=v2 | confirmed | |
| 53 | Adyen invalid status carries "the `verificationErrors`, `subErrors`, and `remediatingActions` arrays" | A/verification-overview/capabilities.md | confirmed | |
| 54 | Adyen View Verification Status component creates the link and "shows their verification status" | A/onboard-users.md | confirmed | |
| 55 | Adyen periodic review: error 3_10, a deadline, `/legalEntities/{id}/confirmDataReview` | A/verification-overview/data-review-process.md | confirmed | |
| 56 | No completion or drop-off rate in the Stripe Connect and Adyen for Platforms documentation or Adyen's release notes | all pages above; both llms.txt indexes; release notes searched for "conver" | confirmed | True of the documentation; the wider claim is row 4. |
| 57 | Adyen: scanning an ID "improves verification pass rates", no number | A/onboard-users.md; adyen.com/the-latest/faster-more-accurate-onboarding-with-the-new-identity-flow-in-hosted-onboarding | confirmed | The news post says the same without a number. |
| 58 | "That leaves the platform to build the measurement" | S/dashboard/onboarding-insights.md; A/kyc-insights.md | corrected | Both providers document a dashboard of the platform's own funnel. Stripe: hosted and embedded only ("Accounts onboarded entirely through the API … aren't included"), data from 4 April 2026. Adyen: "First attempt success rate", "Median verification time", filter by integration type. Two sentences and two source entries added; the seven-stage table stays. |
| 59 | Stripe return URL: "It doesn't mean that all information has been collected… entered and exited properly." | S/hosted-onboarding.md?…=v2 | confirmed | |
| 60 | Stripe "the `v2.core.account[requirements].updated` event sent to your webhook endpoint" | same | confirmed | |
| 61 | Adyen "sends all verification-related updates through webhooks" | A/verification-overview.md | confirmed | |
| 62 | Signals table, Stripe: Account Link or AccountSession; return URL; nothing currently due with entries pending verification; capability `status` `active` | S/hosted-onboarding.md; S/handling-api-verification.md (v1 `pending_verification`; v2 status table) | confirmed | |
| 63 | Signals table, Adyen: account holder created by call or in the Customer Area; hosted link; `verificationStatus` `pending`; capability `allowed` | A/onboard-users.md; A/verification-overview/capabilities.md | confirmed | |
| 64 | Stripe risk page: platform responsible "You can pause payments or payouts…"; Stripe responsible "You can't" | S/risk-management.md | confirmed | See note 2. |
| 65 | Adyen `enabled` setting; "The capability can only be used when it is both allowed and enabled" | A/verification-overview/capabilities.md | confirmed | |
| 66 | Table: ways to collect (both cells) | rows 23, 24, 27, 33 | confirmed | |
| 67 | Table: who may collect (both cells) | rows 39, 41 | confirmed | |
| 68 | Table: how much up front (both cells) | rows 18, 19, 20 | confirmed | |
| 69 | Table: Stripe one deadline per account, no standard length published | S/handling-api-verification.md?…=v1 (`current_deadline` "the earliest deadline across all of the account's requested capabilities"); v2 `summary.minimum_deadline.time` | confirmed | No length in days found on the verification, identity or updates pages. Agrees with chapter 26. |
| 70 | Table: Adyen 30 and 60 days, "shortened or removed" | row 47, 48 | confirmed | |
| 71 | Table: bringing a seller back (both cells) | rows 26, 28, 29, 51, 54 | confirmed | |
| 72 | Table: the platform's own switch (both cells) | rows 64, 65 | confirmed | |
| 73 | Table: published conversion figures "Not public" / "Not public" | rows 4, 58 | corrected | Cells now state what each documents: no completion rate; Stripe's one relative figure from 2019 and a dashboard for hosted and embedded; Adyen's dashboard. |
| 74 | Adyen account structure: legal entity "in each country your user operates in"; "At least one account holder for each country"; "at least one balance account"; "One or more stores … representing the physical locations of your user's businesses"; verified bank account | A/account-structure-resources/platform-structure.md | confirmed | |
| 75 | Stripe capability names `card_payments`, `bacs_debit_payments` | S/account-capabilities.md (v1, v2) | confirmed | |
| 76 | "payouts, which Stripe requests automatically for an account that takes payments. A UK studio uses nothing else." | S/account-capabilities.md?…=v2 | corrected | True in Accounts v2 only (the merchant configuration requests `stripe_balance.payouts`); the sentence now says so. Destination charges also need the transfers capability ("required for functionality such as destination charges"); one sentence added. See "Ledger conflicts". |
| 77 | Stripe interval "at least every 6 months", applied to 2017–2026 ("eighteen reviews") | S/onboarding.md | hedged | The page is undated and current; nothing shows the rule existed in 2017. Now "as documented today". |
| 78 | Stripe "collect information for future requirements before the `future_requirements.current_deadline`" | S/handle-verification-updates.md?…=v1 | confirmed | |
| 79 | Stripe return URL "when they complete the onboarding flow or click **Save for later**…"; refresh URL when "The link is expired (a few minutes went by…)" or opened by "a messaging client that attempts to access the URL to preview it" | S/hosted-onboarding.md?…=v2 | confirmed | The same page: "This URL passes no state." |
| 80 | A chat client's preview uses up an Account Link | same | confirmed | "Many clients automatically visit links, which causes an Account Link to expire." |
| 81 | Adyen `rejected` "is final and any errors cannot be resolved by updating data or uploading documents" | A/verification-overview/capabilities.md | confirmed | |
| 82 | Adyen "Data changes to the legal entity of the account holder do not trigger webhooks" | A/verification-overview.md | confirmed | |
| 83 | Take-away: Stripe lets any platform start small; Adyen tells general platforms to collect first | rows 18, 19 | confirmed | |
| 84 | Hosted table cell: provider's pages "with the platform's name and colors" | S/onboarding.md; A/onboard-users.md (themes) | confirmed | |

Counts: 84 claims checked; 75 confirmed, 5 corrected (4, 43, 58, 73, 76), 4 hedged (1, 15, 38, 77), 0 unsupported, 0 unreachable. The source URL in row 5 is a link change, listed under Links. Rows 4, 58 and 73 are one finding in three places.

## Links

- All 20 original source URLs returned 200 with no redirect. `https://docs.stripe.com/connect/account-capabilities.md` now returns only an index of two variants; the Sources entry points to `?accounts-namespace=v2`.
- Added: `https://stripe.com/blog/connect-express-onboarding` (200; redirects to a locale path by IP, the canonical URL is kept), `https://docs.stripe.com/connect/dashboard/onboarding-insights.md` (200), `https://docs.adyen.com/platforms/kyc-insights.md` (200), `https://support.stripe.com/questions/kyc-refresh-upcoming-periodic-confirmation-requirements` (200; client-rendered, text read from the JSON embedded in the HTML).
- All `[[permalink]]` links are in the style guide's valid list. Ruling 22: 20 inline external links reduced to plain text; every URL was already in Sources.

## Could not verify, and what I did

- Nothing was unreachable. "Not public" claims (rows 37, 41, 69) are negative findings from the pages and indexes named; they are as good as that search.
- Note 1: the page glosses "payment facilitator" as a platform registered with the card networks. Adyen's account-structure page also treats as payment facilitators platforms with individuals taking in-person payments or with high-risk merchant category codes. The gloss is the general term and was left; the author may want a clause.
- Note 2: Stripe's page on pausing says the workflow is done in the Dashboard and "isn't available when using Accounts v2". The chapter's sentence quotes the risk page and is correct; it does not say this limit.
- The figure caption for the three ways to collect still says the platform's "server then holds the documents first" (row 38). Left alone as a design statement, not a provider fact.

## Ruling 2 (chapter 26 owns verification as state)

No contradiction found. Both chapters give the same Stripe deadline sentence, the same Adyen 30- and 60-day periods and "shortened or removed", the same K6 wording, the same owner (Jonas Weber) and 14- and 3-day alerts, and the same no-webhook sentence. Chapter 34 points to chapter 26 for the mechanism and the mirror. Chapter 26 says Femke reviewed the incident with Jonas Weber, chapter 34 with Aylin Demir; the ledger covers both.

## Larkfield consistency

Checked against the ledger: 11 May 2026 is a Monday, 14 May a Thursday, 20 May a Wednesday (nine days, within the ledger's "up to 12"); 9 March 2027 a Tuesday, 11 March a Thursday; €120.00 and €117.47; 230 of 3,590 is 6.4%; 1,100 + 700 + 650 + 1,140 = 3,590; Adyen hosted onboarding since 2024; 50 largest studios on both providers; legacy Custom accounts with Larkfield as collector (ruling 23). All agree.

## Ledger conflicts

- The ledger line for chapter 34 says "For a UK studio Larkfield requests card payments, Bacs Direct Debit and payouts", and the line for chapter 33 says Larkfield uses destination charges with `on_behalf_of`. Stripe's capabilities page says destination charges require the transfers capability, and on Accounts v1 (legacy Custom accounts) there is no separate payouts capability. The page keeps the ledger's three and adds that the account also needs the capability to receive transfers. The figure placeholder `34-one-company-three-locations` still shows three switches ("Cards", "Debit", "Payouts") and its caption says "three capabilities"; not changed. The author should decide whether the ledger and the figure become card payments, Bacs Direct Debit and transfers.

## For other pages

- `journal-spec.json`, entry `platform-onboarding-and-verification`: the intent, thesis and an acceptance criterion say neither provider publishes conversion figures for its onboarding flows and that the chapter presents no conversion number. Stripe's 2019 post (row 4) and both dashboards (row 58) make that too strong. The post spec copies these fields, so they were left; paragraph-level fields, an open question and the decision log were updated.
- Chapter 26 and any page that says a platform "has to build" onboarding measurement from scratch: both providers document a dashboard (row 58).
- `platform-payment-models` (chapter 33) and the ledger: see "Ledger conflicts" on the transfers capability.

## For the author

1. Whether to reword the journal-spec thesis and acceptance criterion on conversion figures.
2. Whether Ironworks's three capabilities should include transfers (ledger and figure).
3. Whether to keep Stripe's 5.3% figure in the text. It is the source's number, attributed and age-flagged, but an earlier spec decision said no conversion percentage would appear.
