# Research brief: Authorization optimization, routing and orchestration

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 09 (authorization optimization), 10 (routing and orchestration), and parts of 23 (network tokens: effect on approval rates, how each provider exposes them) and 29 (dunning: retry scheduling, card updater and tokens in recovery). The anchors are Stripe and Adyen; card networks, the Federal Reserve, independent orchestrators and merchant accounts appear where they clarify an architectural choice.

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated documentation and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: from a reputable secondary source, not a primary document. The kind of source is named (acquirer bulletin, trade press, vendor homepage, mirror of a social post).
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including every statement about how Stripe, Adyen or any other company works internally beyond what it has published.

**Every performance number in this brief is a vendor claim** unless stated otherwise. None was audited by a third party. Each is recorded with its exact wording, who made it, when, and the metric definition where one was published. Where no definition was published, the brief says so.

**Evidence age.** Sources published before November 2023 are flagged **(evidence age: N years)**. Stripe and Adyen documentation pages carry no reliable publication date. Adyen's markdown pages expose a `last_modified` field, but many show the build timestamp of the fetch day and at least one is plainly wrong (the Uplift page shows 2022, although Uplift launched in January 2025), so the field is not used as a date here.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: preview and pilot status (Stripe Orchestration, Adyen Multi pay-in), product names (Authorization Boost, Uplift module names), prices, network retry thresholds and fees, and supported-processor lists.

**Research limitation.** What could not be fetched or verified:

- **Visa and Mastercard rule texts.** The current Visa Core Rules and Mastercard Transaction Processing Rules were not fetched. Retry limits come from one Visa bulletin (September 2020), Adyen's documentation, and acquirer summaries (PayPal, Braintree, TabaPay). These sources **disagree on the Visa limit** (15 or 20 reattempts in 30 days); see 2.2.
- **Mastercard Automatic Billing Updater** developer pages render client-side and returned no text. Visa's VAU overview page returned only its first paragraph.
- **Adyen's token export procedure.** The help-centre article "How can I prepare for token migration? [Export]" redirected to the tokenization documentation and could not be read; its content is known only from a search summary.
- **Airbnb engineering posts** on Medium returned 403. No Booking.com account of multi-provider routing was found. The Uber URL for a 2023 payments integration case study returned 404.
- **Stripe pages for local acquiring, level 2/3 data, US debit routing and a dedicated network-token documentation page** returned 404 at the URLs tried; what Stripe says on these topics comes from other pages that were fetched.
- **Stripe's 2026 product-update list** mentions Authorization Boost but not Stripe Orchestration; no general-availability announcement for Orchestration was found.
- **Hyperswitch, Primer and Gr4vy** facts are vendor self-descriptions from a homepage or README.

---

## PART 1: Why payments are declined, and how success is measured (chapter 09)

### 1.1 Who declines, and why

- Stripe's documentation names three ways a payment fails: "Issuer declines", "Blocked payments" and "Invalid API calls". Only the first is the bank's decision; a blocked payment is stopped by Stripe (Radar, or Adaptive Acceptance for cost reasons) and "doesn't obtain authorization from the card issuer" [VERIFIED: https://docs.stripe.com/declines.md, n.d., accessed 2026-11].
- On the issuer's decision: "When your customer's card issuer or payment provider receives a charge, their automated systems and models decide whether to authorize it. These tools analyze signals such as spending habits, account balance, and card data (expiration date, address information, and CVC)" [VERIFIED: same page].
- Most declines carry no usable reason: "Card issuers categorize most declines as generic (generic_decline), making the exact decline reason unclear." "For privacy and security reasons, card issuers discuss the specifics of a decline only with their cardholders" [VERIFIED: https://docs.stripe.com/declines/card.md, n.d., accessed 2026-11].
- Stripe's guide gives the mechanism: the request is "encoded into a message referred to as an ISO 8583. Issuing banks use complex logic to decide when to decline charges: there are 128 fields in the ISO 8583 message, and each issuing bank can choose how to interpret and combine them." It lists three typical causes: "insufficient funds available on the card, the card information is wrong or outdated, or there's suspicion of fraud". On the generic code: "some banks classify nearly all declines as 'Do not honour'. Or they may purposely hide the specific reason for the decline" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates, n.d., accessed 2026-11].
- Stripe claims online authorization rates "can be 10% lower for online transactions compared to in person" because issuers "use more conservative logic" for card-not-present payments [VERIFIED: same guide]. This is a vendor statement with no dataset or date attached [ASSUMPTION/JUDGEMENT].
- Adyen returns `resultCode`, `refusalReason` and `refusalReasonCode`, with HTTP 200 even for a refusal, and warns: "To prevent malicious use, do not expose the details of the refusal reason to shoppers" [VERIFIED: https://docs.adyen.com/development-resources/refusal-reasons.md, n.d., accessed 2026-11].
- Both providers expose the network's own code next to their normalised reason. Stripe: `network_decline_code` and `network_advice_code` on the charge outcome, "The meaning of a code differs based on the card network"; "Mastercard refers to network advice codes as Merchant Advice Codes (MAC)" [VERIFIED: https://docs.stripe.com/declines/card.md]. Adyen: `refusalCodeRaw` ("only available for Visa and Mastercard transactions through our own acquiring platform") and `refusalReasonRaw`, which must be enabled in the Customer Area [VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees.md, n.d., accessed 2026-11].

### 1.2 Soft and hard declines

Neither "soft decline" nor "hard decline" is a network term. The networks define categories and advice codes; providers and merchants map them to "may retry" and "must not retry" [ASSUMPTION/JUDGEMENT].

| Family | Visa category (see 2.2) | Example raw codes | Retry? | Source |
| --- | --- | --- | --- | --- |
| Issuer will never approve | Category 1 | 04 pickup card, 14 invalid account number, 41 lost, 43 stolen, 46 closed account, 57 not permitted to cardholder, R0/R1/R3 stop payment and revocation | Never | Adyen mapping page |
| Issuer cannot approve at this time | Category 2 | 51 insufficient funds, 59 suspected fraud, 61 exceeds amount limit, 65 exceeds frequency, 91 issuer inoperative, 96 system malfunction | Yes, within a limit | Adyen mapping page |
| Issuer cannot approve with these details | Category 3 | 54 expired card, 82 and N7 CVV failure, 1A additional authentication required | Yes, after fixing the data | Adyen mapping page |
| Generic | Category 4 | 05 do not honor, and every code not listed above | Yes, within a limit | Adyen mapping page |

[VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees.md, n.d., accessed 2026-11]. Adyen notes that "The most frequent refusal reason, **05: Do not honor**, falls into this category" (category 4).

- Stripe defines a hard decline code as one where "the issuing bank has rejected the transaction and you can't retry it", and lists the codes its Smart Retries will not retry: `incorrect_number`, `lost_card`, `pickup_card`, `stolen_card`, `revocation_of_authorization`, `revocation_of_all_authorizations`, `authentication_required`, `highest_risk_level`, `transaction_not_allowed` [VERIFIED: https://docs.stripe.com/billing/revenue-recovery/smart-retries.md, n.d., accessed 2026-11].
- Stripe also gives each declined charge an `advice_code` with three values: `do_not_try_again`, `try_again_later`, `confirm_card_data` [VERIFIED: https://docs.stripe.com/declines/card.md]. These map one-to-one onto Visa categories 1, 2/4 and 3 [ASSUMPTION/JUDGEMENT].
- In Europe a specific soft decline asks for authentication: Visa's code 1A, "Additional customer authentication required (Europe region only)" [WIDELY REPORTED: https://www.paypal.com/us/brc/article/avoid-excessive-retries-penalties, 2026; acquirer guidance by PayPal, dated 15 May 2026]. Stripe surfaces it as `authentication_required`, which Smart Retries treats as non-retryable because the customer must act [VERIFIED: Smart Retries page above].

### 1.3 Authorization rate, payment success rate, conversion rate

Stripe publishes precise definitions. Adyen's public pages use "authorization rate" and "payment conversion" without a formula that this session could find.

- **Authorization rate (Stripe, "also known as network authorization rate")**: "we divide the number of payments authorized by the card issuer by the number of unique payment attempts submitted to the card network for authorization. We exclude invalid API calls, payments that fail 3D Secure authentication, and blocked payments in the denominator because these failures occur before Stripe sends the authorization request to the issuer" [VERIFIED: https://docs.stripe.com/payments/analytics/acceptance.md, n.d., accessed 2026-11].
- **Payment success rate (Stripe)**: "measures the success of all payment attempts throughout the payment process, including 3DS authentication, Stripe or Radar blocks, and card network authentication ... we divide the number of charges authorized by the card network by the number of unique payment attempts submitted through Stripe" [VERIFIED: same page].
- Stripe's worked example: 103,000 requests, 3,000 invalid, 1,000 failed authentication, 1,000 blocked, 93,000 authorized gives a payment success rate of 93% (93,000 / 100,000) and an authorization rate of 94.9% (93,000 / 98,000) [VERIFIED: same page].
- **Raw versus deduplicated**: "The raw rate includes all payment attempts (including retries) to make the same purchase." "The deduplicated rate groups the retried payment attempts together and calculates the acceptance rate based on the final outcome." Example: one purchase with two failed attempts and one success has a raw rate of 33.3% and a deduplicated rate of 100% [VERIFIED: same page].
- How Stripe groups attempts: by invoice for Stripe Invoices; by customer "if they're attempted close to each other in time and for the same amount"; otherwise "on the same card number for attempts close to each other in time and for the same amount" [VERIFIED: same page]. The time window is not published [ASSUMPTION/JUDGEMENT].
- Stripe's own glossary is looser than its analytics page: the guide defines "Authorisation rate" as "The percentage of transactions that you submit and are accepted by the card networks" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates]. Writers should use the analytics-page definitions.
- **Conversion rate** in the checkout sense (completed payments divided by checkout sessions started) is a wider funnel than either Stripe metric: it also loses shoppers who abandon before submitting. Adyen's Uplift claim is stated as "payment conversion rate" and its footnote reads: "Based on the average conversion improvement of merchants that participated in the pilot and used all modules of Adyen Uplift. Results may vary depending on your setup" [VERIFIED: https://www.adyen.com/the-latest/boost-your-payment-conversion-with-adyen-uplift, published 2025-01]. No numerator or denominator is given [ASSUMPTION/JUDGEMENT].

**Stripe vs Adyen (Part 1)**

| Aspect | Stripe (documented) | Adyen (documented) | What the difference suggests |
| --- | --- | --- | --- |
| Metric definitions | Two named rates with formulas, a worked example, raw and deduplicated variants (acceptance analytics page, n.d., accessed 2026-11) | "Authorization rate" and "payment conversion" used in docs and press; no public formula found (searched docs.adyen.com index for uplift, insights, conversion) | Stripe's numbers can be reproduced from its definitions; Adyen's public claims cannot be [ASSUMPTION/JUDGEMENT] |
| Decline detail to merchant | Normalised decline code, advice code, raw network decline and advice codes | Normalised refusal reason and code; raw acquirer response on request, Visa and Mastercard on Adyen's own acquiring | Both hide nothing the network returns; both add their own vocabulary on top [ASSUMPTION/JUDGEMENT] |
| Mapping to network retry rules | Three advice codes; list of nine hard decline codes | A published table mapping raw codes to the four Visa fee categories | Adyen documents the network rule; Stripe documents its own abstraction of it [ASSUMPTION/JUDGEMENT] |

**For readers new to payments.** *Issuer*: the bank that gave the customer the card and decides yes or no on every payment. *Decline code*: the short code the issuer returns with a "no"; most are generic. *Soft decline*: a "no" that might become a "yes" later or with corrected data. *Hard decline*: a "no" that will never change for this card, so retrying is forbidden. *Authorization rate*: approvals divided by the attempts that actually reached the card network.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Store the raw network code, the provider's normalised code and the provider's advice for every attempt; a retry policy written against only the normalised code breaks when a second provider is added. Decide once whether dashboards show raw or deduplicated rates and label every chart: the same month can read 33% or 100%. Keep attempts and purchases as separate entities so the deduplicated rate can be computed by the merchant, not only by the provider. Compare providers only on rates with the same denominator: a provider that blocks likely declines before the network raises its authorization rate and lowers its payment success rate at the same time.

---

## PART 2: Retries and the network rules that limit them (chapters 09 and 29)

### 2.1 Why networks limit retries

A merchant that retries a declined card costs the network and the issuer processing capacity and looks like an attacker testing cards. Stripe: "Card issuers might see creating additional retries as potential fraud, which can result in increased declines for legitimate charges" [VERIFIED: https://docs.stripe.com/declines/card.md, n.d., accessed 2026-11]. Both major networks therefore charge fees for retries beyond a limit, and for any retry of a decline that can never succeed.

### 2.2 Visa: response-code categories and reattempt limits

- "In April 2020, Visa introduced new rules that grouped authorization response codes into four categories and required issuers to send descriptive response codes across all categories to identify the reason for the decline. In turn, acquirers and their merchants should manage authorization reattempts based on the response code categories defined in the rules" [VERIFIED: https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/updates-to-rules-for-declined-transaction-resubmission-and-use-of-authorization-response-codes.pdf, published 2020-09-03] **(evidence age: 6 years; the category structure is confirmed by Adyen's current documentation and by PayPal's May 2026 guidance, the numeric limit is not, see below)**.
- The same bulletin, effective 17 April 2021, moved codes 03, 62, 78 and 93 "from Category 1 to Category 2 (Issuer cannot approve at this time) to allow merchants to reattempt up to 15 times in 30 days", and states: "When a Category 1 (Issuer will never approve) decline code is used, the merchant is not permitted to reattempt the transaction" [VERIFIED: same bulletin]. It applies to "Canada, Europe, LAC, U.S."
- Adyen's current documentation repeats the 15-in-30-days limit for categories 2, 3 and 4 and describes two "system integrity fees": "An **excessive retry fee** for failed transactions that are retried too many times" and "A **data quality fee** that is applied if the number of transactions that failed because you provided incorrect data exceeds a monthly threshold" [VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees.md, n.d., accessed 2026-11].
- ⚠ **Conflict.** PayPal's guidance says: "Visa allows 20 retries in 30 days on soft declines (Cat. 2-4). Visa does not allow retries on hard declines (Cat. 1)." It adds that Visa matches reattempts on "Acquirer, Acquirer Identifier, Card Acceptor ID (CAID), Token/PAN, and transaction amount", and that "If a token is tried, declined then a PAN is tried, no fee" [WIDELY REPORTED: https://www.paypal.com/us/brc/article/avoid-excessive-retries-penalties, 2026; acquirer guidance, fetched, dated 15 May 2026]. TabaPay's developer documentation also says the fee applies to "The 21st consecutive and subsequent reattempted transactions after receiving a Category 2 – 4 decline response within a 30-day period" [WIDELY REPORTED: https://developers.tabapay.com/docs/network-authorization-best-practices, n.d.; processor documentation, fetched]. Either Visa raised the limit from 15 to 20 after 2021 and Adyen's page is stale, or the limit differs by region. This session could not settle it from a Visa document. **Writers should state the rule as "15 or 20 reattempts in 30 days depending on the source and possibly the region" and cite both.**

### 2.3 Mastercard: Transaction Processing Excellence and Merchant Advice Codes

No Mastercard primary document was fetched; everything below is from acquirer and processor communications.

- Braintree's network-update note: "Starting 1 November 2023, merchants will incur fees if they retry a transaction more than 35 times in a 30-day period. As part of Mastercard's Transaction Processing Excellence Program (TPE) ... any further retry attempt(s) past the 35 allowed will incur a $0.15 per transaction fee." "this retry fee will further increase to $0.30/transaction from 1 January 2024, and $.50/transaction from 1 January 2025" [WIDELY REPORTED: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23, 2023; acquirer bulletin, fetched] ⚠ (fees are US figures and change yearly).
- PayPal's 2026 guidance describes two Mastercard thresholds, on "the same account number, at the same card acceptor, and for the same amount": "Allow 10 retries in a 24-hour period then charge a fee for subsequent retries" and "Allow 35 retries in a 30-day period then charge a fee for subsequent retries" [WIDELY REPORTED: https://www.paypal.com/us/brc/article/avoid-excessive-retries-penalties, 2026; acquirer guidance].
- Mastercard hard declines: after certain card-not-present response codes "the Merchant must not initiate any additional authorization requests for the same Transaction with the same PAN and expiration date at any time" [WIDELY REPORTED: same PayPal page, quoting the Mastercard rule].
- **Merchant Advice Codes (MAC)** tell the merchant what to do next. A separate fee applies when a request "is declined with a MAC value of 03 or 21 where then same transaction was attempted in past 30 days and declined with MAC 03 or 21" [WIDELY REPORTED: same PayPal page]. MAC 03 and 21 mean "do not try again" in the common reading [ASSUMPTION/JUDGEMENT; the meanings table was not captured in this session].
- **Timing advice for insufficient funds.** Mastercard's Authorization Optimizer sends a MAC with decline code 51 that "will provide the merchant an optimal time to retry the transaction": values 24 to 30 mean retry after 1 hour, 24 hours, 2 days, 4 days, 6 days, 8 days and 10 days. "A fee applies whether the merchant uses the MAC or not" [WIDELY REPORTED: https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23 and .../2024/mc-su24; acquirer bulletins, fetched]. This is a network-supplied retry schedule, which is new compared with merchant-guessed dunning calendars [ASSUMPTION/JUDGEMENT].

### 2.4 What each provider does about the rules

- **Stripe, guidance**: "card networks limit the number of times you can reattempt a single charge. Stripe recommends a maximum of eight retries for charges that permit retries" [VERIFIED: https://docs.stripe.com/declines/card.md]. Stripe's guide gives a different figure: "many card networks only allow 4 to 6 retries within a 15-day window" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates, n.d.]. The two Stripe statements and the network limits in 2.2 and 2.3 do not agree; the guide's figure has no source [ASSUMPTION/JUDGEMENT].
- **Stripe, product**: within Adaptive Acceptance, "**Excessive retry prevention**: Stripe blocks a payment that would have incurred network retry penalties and likely failed", described further as blocking "charges that are subject to network penalty fees based on prior network decline or advice codes and are likely to fail". "**Decline prevention**: Stripe blocks a payment from reaching the card network that was unlikely to succeed, avoiding additional scheme fees for the payment" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md, n.d., accessed 2026-11]. These apply to businesses on IC+ pricing; a blocked payment returns `"reason": "low_probability_of_authorization"`, `"network_status": "not_sent_to_network"`, `"type": "blocked"` [VERIFIED: https://docs.stripe.com/declines.md].
- **Adyen, guidance**: the mapping page in 2.2 exists "If you have built your own retry logic"; otherwise "The Adyen risk engine helps to avoid such fees" [VERIFIED: Adyen Visa integrity fees page].
- **Adyen, product**: "The Excessive Retry Prevention Service (ERPS) blocks transactions that would incur Visa or Mastercard excessive retry penalty fees. It is opt-in, not priced, and in maintenance mode. ERPS can reduce scheme penalty fees but may have a negative impact on authorization rates" [VERIFIED: https://docs.adyen.com/partners/uplift-enablement.md, n.d., accessed 2026-11] ⚠. The marketing page lists it as "Excessive Retry Protection Service" [VERIFIED: https://www.adyen.com/uplift/optimize, n.d., accessed 2026-11].

### 2.5 Scheduled retries for recurring payments (dunning)

**Stripe Smart Retries** [VERIFIED for every bullet: https://docs.stripe.com/billing/revenue-recovery/smart-retries.md, n.d., accessed 2026-11]:

- "Using AI, Smart Retries chooses the best times to retry failed payment attempts to increase the chance of successfully paying an invoice. The AI model behind Smart Retries uses time-dependent, dynamic signals, such as: The number of different devices that have presented a given payment method in the last *N* hours. The best time to pay (payments made for debit cards in certain countries might be slightly more successful at 12:01 am in local time zones)."
- Policy bounds are the merchant's: "retry payment a specific number of times within a time period: 1 week, 2 weeks, 3 weeks, 1 month, or 2 months. For new Stripe accounts, Stripe enables Smart Retries by default and configures it for up to 8 retries within 2 weeks."
- The alternative is a fixed schedule: "You can configure up to three retries, each with a specific number of days after the previous attempt."
- After a hard decline "Retries continue to be scheduled, and attempt_count continues to increment, but retries only execute after detecting a new payment method."
- Not retried: no payment method, a hard decline code, an India-issued card, a disconnected Connect account.
- Direct debits follow their own limits, not the card policy: ACH Direct Debit 2 retries within 40 days, SEPA Direct Debit 2 within 30 days, Bacs 2 within 30 days, Australia BECS 4 within 30 days, New Zealand BECS 1 within 5 calendar days, in each case for insufficient funds.
- Stripe's guide adds signals not in the documentation: "we look at issuer behavior (such as when the issuing banks change their review thresholds), check for card updates, and analyse activity across Stripe to see if the payment method is being used successfully" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates, n.d.].
- "Smart Retries is incompatible with Stripe Orchestration" [VERIFIED: https://docs.stripe.com/payments/off-session-payments/orchestration.md, n.d., accessed 2026-11].
- No recovery-rate number for Smart Retries was found in the documentation fetched; the docs say only that Smart Retries "are more effective than scheduled retries" [VERIFIED: https://docs.stripe.com/billing/revenue-recovery.md, n.d.].

**Adyen Auto Rescue** [VERIFIED: https://docs.adyen.com/online-payments/auto-rescue.md and https://docs.adyen.com/online-payments/auto-rescue/cards.md, n.d., accessed 2026-11]:

- "Adyen's Auto Rescue automatically retries refused or charged back shopper-not-present transactions such as subscription renewals. It uses smart logic to decide which payments can succeed when retried later, and performs these retries at optimal times." It covers cards and SEPA direct debit.
- Retries happen inside a *rescue window*. Enabled at account level it applies to payments with `shopperInteraction` **ContAuth** and "a rescue window of one calendar month is used". At transaction level the merchant sends `autoRescue: true` and `maxDaysToRescue`, "between **1** and **48** days. We recommend using a rescue window of one calendar month (**30** days)". (The same page's example text says "for a maximum of **40** days", an inconsistency in the documentation.)
- A refused payment response carries `retry.rescueScheduled` (true or false) and `retry.rescueReference`; false "happens when a payment cannot be rescued. For example, because of account closure or fraud". Each attempt and the end of the process arrive as webhooks. The merchant can cancel a rescue, and can have a payment link sent when it ends without success.
- Recovered revenue is reported in a report still named "**RevenueAccelerate**", the older product name for Adyen's optimization features.
- Adyen's marketing page separates two retry products: "Auto Retries intelligently retries declined transactions by adapting the route, messaging, authentication, and tokenization to maximize the chance of success – in milliseconds" (in-flight, during the original payment) and "Auto Rescue ... intelligent retries that reduce involuntary churn" (scheduled, later) [VERIFIED: https://www.adyen.com/uplift/optimize, n.d., accessed 2026-11].

**Stripe vs Adyen (Part 2)**

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Scheduled retry product | Smart Retries, part of Billing; operates on invoices and subscriptions | Auto Rescue, part of payments; operates on any ContAuth payment | Stripe ties learned retries to its billing product; Adyen offers them to merchants that run their own billing [ASSUMPTION/JUDGEMENT] |
| Merchant controls | Number of retries and total window (1 week to 2 months); or a fixed schedule of up to three retries | Rescue window in days (1 to 48); cancel by reference | Both fix the envelope and let the model choose the moments inside it [ASSUMPTION/JUDGEMENT] |
| Published signals | Two examples in docs, three more in a guide | "smart logic", "optimal times"; none named | Neither publishes the model, features or measured lift [ASSUMPTION/JUDGEMENT] |
| Network retry limits | Recommendation (eight); excessive retry prevention inside Adaptive Acceptance for IC+ accounts | Code-to-category mapping table; ERPS, opt-in and "in maintenance mode" | Adyen expects some merchants to build their own retry logic and documents the rule for them [ASSUMPTION/JUDGEMENT] |
| Default | On for new accounts, 8 retries in 2 weeks | Off until Adyen support enables it | Reflects Stripe's self-serve and Adyen's account-managed models [ASSUMPTION/JUDGEMENT] |

**For readers new to payments.** *Dunning*: the process of collecting a recurring payment that failed, by retrying and by contacting the customer. *Involuntary churn*: a subscriber lost because a payment failed, not because they chose to leave. *Merchant Advice Code*: a Mastercard code sent with a decline that tells the merchant whether and when to try again. *Excessive retry fee*: a per-transaction charge from the network for retries beyond its limit.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A retry is a new authorization attempt on the same purchase, so the data model needs a purchase (or invoice) with many attempts, a counter per card and per network, and the last decline category. The retry limit is counted by the network per merchant identifier, card and amount, across every system that can submit an attempt: checkout, the billing engine, a provider's automatic retry and a second provider's fallback all draw on the same budget. A merchant that runs its own dunning on top of a provider's automatic retries must turn one of them off or count both. With two providers the count is harder: the network counts per acquirer and card acceptor ID, so a fallback to a second provider may or may not be counted as a reattempt, and no fetched source says which.

---

## PART 3: The levers that move approval rates (chapters 09 and 23)

### 3.1 Local acquiring

- Stripe: "If your customers use cards issued in a different country than where you registered your Stripe account, they might see an increased rate of declines ... you might want to set up Stripe accounts in larger markets, or in regions that encounter higher decline rates. This allows you to process charges locally" [VERIFIED: https://docs.stripe.com/declines/card.md]. The guide: "Using locally optimised acquiring services helps you maximise acceptance rates (because banks are often more likely to approve domestic payments) and removes foreign and cross-border fees for customers" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates, n.d.].
- Adyen's Intelligent Payment Routing chooses among routes that include local acquiring: it "requires at least two available routes (for example, a local scheme and an international scheme)" and the merchant must "make sure at least two routes (schemes or MCCs) are configured" [VERIFIED: https://docs.adyen.com/partners/uplift-enablement.md].
- Shopify's engineers confirm the pattern from the merchant side: "often payment gateways use local acquirers behind the scenes to optimize authorization rates and lower costs" [VERIFIED: https://shopify.engineering/building-resilient-payment-systems, published 2022-07-28] **(evidence age: 4 years; a general statement, unlikely to have changed)**.
- No quantified, dated figure for the domestic-versus-cross-border approval gap was found from either anchor company in this session.

### 3.2 Network tokens

What each provider documents (the mechanics of tokens belong to the `carddata` brief):

- **Adyen**: "A network token is 16-digit alternative for the Primary Account Number (PAN), and is unique per combination of shopper and merchant." Benefits claimed: tokens stay valid when the card changes, "Higher authorization rates compared to payments made without network tokens", and "each transaction is protected with a single-use cryptogram". Networks named: Visa, Mastercard, American Express [VERIFIED: https://docs.adyen.com/online-payments/network-tokenization.md, n.d., accessed 2026-11].
- Adyen offers two modes: "Let Adyen manage network tokens on your behalf" ("We collect and store network tokens from the card schemes ... we automatically swap the card details from your payment request for the network token") or "Manage network tokens yourself" (bring existing tokens; "not possible to combine this with our tokenization feature") [VERIFIED: same page].
- Adyen's limit: "Network tokenization is only applicable for payments acquired by Adyen. It cannot be used with external acquirer connections" [VERIFIED: same page].
- **Stripe**: "Stripe works with card networks like Visa, Mastercard, and American Express to tokenize a user's repository of PANs into network tokens and maintains them so they stay current." "Our optimised network token solution works out of the box for all merchants who use Stripe Payments" [VERIFIED: https://stripe.com/guides/understanding-benefits-of-network-tokens, n.d., accessed 2026-11].
- Stripe keeps the PAN and chooses per transaction: "Stripe also optimises for future transactions once a token is created, determining when to use a network token or the underlying PAN. We maintain PAN redundancy to retry failed network token transactions on the underlying PAN" [VERIFIED: same guide]. The 2023 press release says the same: "To maximize approval rates, Stripe maintains a secure vault of PANs and intelligently selects whether to use a network token or a PAN for a given transaction" [VERIFIED: https://stripe.com/newsroom/news/network-tokens-card-account-updater, published 2023-02-23] **(evidence age: 3.7 years; confirmed by the current guide and product page)**.
- Stripe names a cost of tokens: "using a network token often requires a one-time cryptogram that needs to be fetched from networks. As a result, network tokens can be prone to high additional latency compared to using PANs" [VERIFIED: Stripe network tokens guide].
- Stripe now also accepts tokens it did not create: "Businesses can use Stripe to provision tokens or bring external tokens for processing" [VERIFIED: https://stripe.com/authorization-boost, n.d., accessed 2026-11].
- Coverage: "network tokens in more than 45 markets" [VERIFIED: https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite, published 2025-05-15].
- Cost effects Stripe documents: "Some payments that use a network token qualify for reduced interchange rates. For example, Visa offers certain discounts on consumer card-not-present payments in some markets"; and "Mastercard levies a Credential Continuity Program (CCP) fee when attempting a payment using outdated card details". Against that: "Stripe doesn't reflect any fees that might occur as a result of network token use, such as the Visa Digital Credential Updater (VDCU) fee" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md].
- Adyen's engineering lead describes the same per-transaction choice as a model action: "the AI in Uplift can choose to tokenize, use a token, or swap a token for a PAN based on global optimization targets", over a vault "hosting north of 2B tokens" [VERIFIED: https://www.adyen.com/knowledge-hub/the-ai-behind-uplift, published 2025-01-17; author Andreu Mora, SVP / Global Head of Engineering Data, Adyen].
- Approval-rate uplift from tokens alone: neither company publishes a number isolated from its other features in the pages fetched. One customer quote: Doist "increase[d] subscription auth rates by over 4%" using network tokens and card account updater together [VERIFIED: Stripe newsroom, 2023-02-23] (evidence age: 3.7 years; a single customer's statement).

### 3.3 Account updater services

- The network services: Visa Account Updater "enables issuers, acquirers, and qualified merchants to exchange updated account information for recurring payments, credential-on-file (COF) transactions" [VERIFIED: https://developer.visa.com/capabilities/vau, n.d., accessed 2026-11]. Mastercard's equivalent is Automatic Billing Updater (ABU) [ASSUMPTION/JUDGEMENT; the Mastercard developer page did not render].
- **Adyen** offers two modes for "Visa, Mastercard, and Cartes Bancaires". Real Time Account Updater: "When you submit a payment that is refused, our Real Time Account Updater instantly checks for updated card details. If there is an update, we immediately retry the payment with the updated card details. This all happens while the payment is being processed, and appears as a single transaction." Conditions: amount not zero, `shopperInteraction` **ContAuth**, no security code in the request [VERIFIED: https://docs.adyen.com/online-payments/account-updater/real-time-account-updater.md, n.d., accessed 2026-11].
- Adyen Batch Account Updater: "You send batch request files to us for updates. We get these updates from the card schemes, and send the updated information back to you in a batch result file." Its stated advantages: "Control over which cards are updated and when" and "Making updated card details available on the initial transaction attempt" [VERIFIED: https://docs.adyen.com/online-payments/account-updater.md]. Adyen's partner guide calls batch "Not recommended due to setup complexity" and the real-time service "an optional paid feature" that "does not send webhooks" [VERIFIED: https://docs.adyen.com/partners/uplift-enablement.md].
- Updates signal four events: a new expiry date, a replacement card, a card reported lost or stolen, and "A shopper informs their card issuer that they no longer authorise you to charge their card automatically" [VERIFIED: Adyen account updater page].
- **Stripe**: "Stripe works with card networks and automatically attempts to update saved card details whenever a customer receives a new card ... It's widely supported in the United States, allowing Stripe to automatically update most American Express, Visa, Mastercard, and Discover cards issued there. International support varies from country to country. It isn't possible to identify cards that support automatic updates." The merchant learns of an update through the `payment_method.automatically_updated` webhook [VERIFIED: https://docs.stripe.com/payments/cards/overview.md, n.d., accessed 2026-11].
- Stripe added real-time updates in 2023: the updater "can now renew credentials at precisely the moment a transaction is being processed ... Stripe now offers real-time updates for Visa in the UK and Europe, and Mastercard globally" [VERIFIED: Stripe newsroom, 2023-02-23] (evidence age: 3.7 years). The 2025 description is "real-time card account updater across all major card networks" [VERIFIED: Stripe blog, 2025-05-15].
- Stripe's cited results: "Postmates experienced a 1.72% uplift from card account updater, leading to $60 million in revenue" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates, n.d.] (undated customer figure; Postmates was acquired by Uber in 2020, so the figure is probably older than five years [ASSUMPTION/JUDGEMENT]). "Last year, approximately 40% of cardholders replaced their cards as a result of the card expiring, getting lost, or being compromised by fraud" [VERIFIED: Stripe newsroom, 2023-02-23; refers to 2022; no source given].
- The updater also runs when Stripe forwards a card to another processor: "Where enabled and available, the Card Account Updater (CAU) automatically attempts to update and provide the latest available card details for requests" [VERIFIED: https://docs.stripe.com/payments/vault-and-forward.md, n.d., accessed 2026-11].

### 3.4 Authentication choices

- Stripe: "we automatically claim SCA exemptions when possible and maximise conversion by only requesting authentication when absolutely necessary" [VERIFIED: Stripe authorization guide]. Adaptive Acceptance adds "**Data Only 3DS**: Stripe reduces scheme fees by sharing additional transaction data with issuers through Data Only flows, without challenging the cardholder" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md].
- Adyen's Authentication Engine "Selects the most appropriate authentication method, such as 3D Secure 2, scheme passkey authentication, or Google Secure Payment Authentication (Google SPA). It considers device capabilities, risk signals, issuer data, real-time performance data, and local regulatory requirements" [VERIFIED: https://docs.adyen.com/online-payments/authentication.md, n.d., accessed 2026-11]. It "helps decide when to offer strong customer authentication, which exemptions to ask for, and when to request the frictionless or the challenge flow based on issuer preference" [VERIFIED: https://docs.adyen.com/uplift.md].
- Adyen's engineering article: "Uplift uses decisioning on which is the best authentication 'rail' to choose to balance fraud, conversion, and cost, and can choose among several available actions such as an exemption, a version of 3DS or a passkey" [VERIFIED: Adyen, The AI behind Uplift, 2025-01-17].
- Stripe counts failed authentication outside the authorization rate (1.3), so an aggressive exemption strategy can raise payment success while lowering the network authorization rate if issuers soft-decline exempted payments [ASSUMPTION/JUDGEMENT]. Detail belongs to chapter 25.

### 3.5 Message formatting and data quality

- Stripe's worked example of formatting: "let's say some customers in the UK quickly type their postcode in all lowercase, with no spaces, into a checkout form. Stripe would notice this pattern and test a variety of variations to find out if a certain postcode format gets better authorisation rates than others. By running these tests with different issuers at the same time, the machine learning models learn which treatment is most effective for which bank" [VERIFIED: Stripe authorization guide].
- Stripe on data: "passing the ZIP code or postal code and CVC can help improve authorisation rates for businesses in the US and UK"; "The impact of other data that you gather, such as the full billing address, might vary by card brand and country" [VERIFIED: Stripe authorization guide and https://docs.stripe.com/declines/card.md].
- Adyen's equivalent is **Smart Payment Messaging**: "Adyen optimizes issuer messaging (for example, CVC and AVS fields) to increase authorization rates on low-risk transactions." It "is enabled by default" and merchants "can adjust the optimization level in their Customer Area under **Uplift** > **Optimize**" [VERIFIED: https://docs.adyen.com/partners/uplift-enablement.md]. Marketing wording: "Optimize adapts payment logic to match each issuing bank's preferences, including CVC and AVS to keep approval rates high" [VERIFIED: https://www.adyen.com/uplift/optimize].
- **Level 2/3 data is a cost lever, not an approval lever.** Adyen: "For Visa and Mastercard, sending Level 2/3 or travel data can lower your interchange fees by up to 1 percent. This data is optional and does not affect authorization rates" [VERIFIED: https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data.md, n.d., accessed 2026-11]. Adyen calls the family "enhanced scheme data" and describes it for "US domestic card online or in-person payments" [VERIFIED: https://docs.adyen.com/uplift.md]. Stripe's level 2/3 documentation was not found at the URLs tried.
- Stripe's Enhanced Issuer Network sends data the other way, to the issuer: "Stripe provides secure access to transaction fraud scores from Stripe Radar ... through an encrypted pathway with issuers including Capital One and Discover." Claim: "On average, businesses see an 8% reduction in fraud and a 1–2% authorization rate uplift" [VERIFIED: https://stripe.com/newsroom/news/enhanced-issuer-network, published 2023-02-21] **(evidence age: 3.7 years)**. The current product page narrows the claim to "a 1%-2% authorisation rate uplift on eligible volume and up to 8% reduction in fraud" and widens the issuers to "several major US and European issuers, including Capital One, Discover and American Express" [VERIFIED: https://stripe.com/authorization-boost, n.d., accessed 2026-11]. No Adyen equivalent was found (searched Adyen docs index and Uplift pages for issuer data sharing).

### 3.6 Timing

- Stripe's guide: for insufficient funds, "If your customers are in the US, you could ask to rerun the charge on the first or 15th of the month (when many Americans get paid)" [VERIFIED: Stripe authorization guide]. Smart Retries' documented example: debit card payments "might be slightly more successful at 12:01 am in local time zones" [VERIFIED: Smart Retries page].
- Mastercard now supplies timing itself through MAC 24 to 30 (2.3).
- Wallets: "Apple Pay and Google Pay lead to higher acceptance rates thanks to two-factor authentication" [VERIFIED: Stripe authorization guide]; no figure given.

**Stripe vs Adyen (Part 3)**

| Lever | Stripe (documented) | Adyen (documented) | What the difference suggests |
| --- | --- | --- | --- |
| Network tokens | Provisioned automatically for Stripe Payments; Stripe picks token or PAN per payment and falls back to PAN; external tokens accepted; Visa, Mastercard, Amex | Adyen-managed or merchant-managed; only on Adyen-acquired payments; can be shared across merchant accounts and forwarded to another PSP; Visa, Mastercard, Amex | Both treat the token as a per-transaction choice, not a replacement for the PAN vault [ASSUMPTION/JUDGEMENT] |
| Account updater | One service, automatic; Visa, Mastercard, Amex, Discover; real-time since 2023; webhook on update | Real-time (on decline, then immediate retry) and batch (file-based); Visa, Mastercard, Cartes Bancaires; no webhook, update in the payment response | Adyen exposes the batch mode a merchant with its own vault needs; Stripe hides the mode [ASSUMPTION/JUDGEMENT] |
| Message formatting | Adaptive Acceptance, before and after a decline | Smart Payment Messaging, on by default, level adjustable | Same idea; Adyen gives the merchant a dial [ASSUMPTION/JUDGEMENT] |
| Issuer data sharing | Enhanced Issuer Network (Radar scores to named issuers) | Nothing public found | A network effect Stripe markets and Adyen does not [ASSUMPTION/JUDGEMENT] |
| Level 2/3 | Not found this session | Enhanced scheme data; "does not affect authorization rates" | Cost lever only |

**For readers new to payments.** *Network token*: a substitute card number issued by Visa or Mastercard for one card at one merchant, which the network keeps valid when the card is reissued. *Account updater*: a network service that tells a merchant's provider the new number or expiry date of a replaced card. *AVS and CVC*: address and security-code checks whose results the issuer can use in its decision. *Level 2/3 data*: extra invoice detail (tax, line items) that lowers interchange on some US business cards.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Three systems can now change the credential behind a stored card without the customer acting: the network token, the account updater and the provider's own choice between them. The merchant's card-on-file record therefore needs an event stream (Stripe's `payment_method.automatically_updated`, Adyen's response fields), not a static row, and "last four digits" shown to the customer can go stale. Because Adyen's real-time updater works by declining first and retrying, a merchant that also runs its own retry logic will see one transaction where two authorizations happened. A merchant that keeps its own PAN vault needs the batch updater or its own network enrolment; this is the hidden cost behind every multi-provider design in Part 6.

---

## PART 4: Stripe's optimization products and the machine learning behind them (chapter 09)

### 4.1 Product names and packaging as of November 2026 ⚠

- **Authorization Boost** is the current bundle: "Increase acceptance rates and reduce network costs with AI-powered payment optimisations, inclusive of Adaptive Acceptance, card account updater and network tokens" [VERIFIED: https://stripe.com/authorization-boost, n.d., accessed 2026-11; fetched in the Ireland locale]. It was previewed at Stripe Sessions on 7 May 2025: "We previewed Authorization Boost, which uses AI to automatically update cards and tokens, route transactions across networks, and determine if and how to retry failed payments" [VERIFIED: https://stripe.com/blog/top-product-updates-sessions-2025, published 2025-05-07].
- Authorization Boost sits inside the **Payments Intelligence Suite**, "an AI-powered set of payment optimisations, fraud prevention and business intelligence products" introduced at the same event [VERIFIED: https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite, published 2025-05-15; byline John Affaki, Payments Business Lead].
- The **Optimized Checkout Suite** is a different product family (the checkout front end: Payment Element, Link and related): "73% of global enterprises new to Stripe choosing to build their checkouts with our Optimized Checkout Suite" [VERIFIED: Stripe Sessions 2025 product updates, 2025-05-07]. It is not the authorization product.
- **Smart Retries** belongs to Billing (2.5). **Enhanced Issuer Network** is listed beside the bundle, not inside it (3.5). An older Stripe description (2023) grouped "Adaptive Acceptance, Smart Retries, and Enhanced Issuer Network" with network tokens and card account updater as "Stripe's suite of payments optimization tools" [VERIFIED: Stripe newsroom, 2023-02-23] (evidence age: 3.7 years; the grouping has since been renamed).
- ⚠ Price, Ireland locale: Authorization Boost "0.2% per successful online card transaction for accounts with custom payments pricing"; Adaptive Acceptance alone "0.08% per successful online card transaction without Authorisation Boost and with custom payments pricing"; card account updater "€0.25 per update"; network tokens "€0.15 per token provisioned for accounts without Authorisation Boost and with custom interchange pricing" [VERIFIED: https://stripe.com/authorization-boost, n.d., accessed 2026-11]. Whether and how standard-pricing accounts are charged is not stated on the page [ASSUMPTION/JUDGEMENT].
- 2026 additions: "You can now use Authorization Boost's new AI-powered optimizations, including support for Data Only authentication flows and PINless debit retries, helping increase acceptance rates by an average of 3.8% and lower processing costs by up to 3.3%"; and "We previewed the ability to A/B test Authorization Boost against your existing payments performance" [VERIFIED: https://stripe.com/blog/everything-we-announced-at-sessions-2026, published 2026-04-29].

### 4.2 What Adaptive Acceptance does

- "Adaptive Acceptance uses AI to reformat payment requests based on card issuers' preferences. Stripe can make these changes before sending a payment or after a payment is declined. For example, Stripe selectively adjusts and reattempts declined payments in real time, which can help recover a significant number of false declines. Additionally, Adaptive Acceptance might apply cost optimizations for businesses on IC+ pricing to help reduce network or interchange fees, or might reattempt a declined payment on an alternative card network" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md, n.d., accessed 2026-11].
- It therefore contains five distinct actions [VERIFIED: same page for each]:
  1. Reformat before authorization, "based on issuer preferences".
  2. Retry after a decline, in real time, with adjusted fields.
  3. "PINless retries: In the US, Stripe might automatically retry an eligible transaction on a US debit network (also known as PINless network) after it's declined on an international network (Visa or Mastercard)."
  4. Block before the network, for cost: excessive retry prevention and decline prevention (2.4).
  5. Data Only 3DS for low-risk payments.
- The retry happens inside the original request: "to improve authorisation rates in real time, before a response is returned to the customer" [VERIFIED: Stripe authorization guide]; "without the end customer ever seeing the initial decline" [VERIFIED: https://stripe.com/blog/ai-enhancements-to-adaptive-acceptance, published 2025-02-12].
- Actions 1 to 3 try to turn a "no" into a "yes"; action 4 turns a probable "no" into a certain "no" to save a fee. They pull the payment success rate in opposite directions, and only IC+ accounts get action 4 [ASSUMPTION/JUDGEMENT, from the documentation above].

### 4.3 The published machine learning: who claimed what, and when

**(a) Stripe blog, "AI enhancements to Adaptive Acceptance", 12 February 2025.** Authors: Ming Chen (Optimizations DS and ML), Keshav Manjrekar (Authentication & Premium Optimizations), Vanya Rybkin, Pierre Garrigues (Core Payments Data Science) [VERIFIED for every bullet: https://stripe.com/blog/ai-enhancements-to-adaptive-acceptance, published 2025-02-12].

- Architecture change: "Our previous approach, based on a gradient-boosted tree model (XGBoost), saved Stripe users billions of dollars in revenue ... We transitioned to a TabTransformer-based deep neural network, which we call TabTransformer+. This system excels at modeling complex interactions among hundreds of factors that influence transaction success."
- "A key enhancement in this new architecture is the addition of high-dimensional embeddings."
- Results claimed: "In 2024, this led to Adaptive Acceptance recovering a record-high $6 billion in falsely declined transactions, reflecting a 60% year-over-year increase in the retry success rate." "Adaptive Acceptance's new AI model achieves 70% greater precision in identifying legitimate transactions that have been falsely declined. This increased precision allowed us to recover more revenue than ever last year while reducing retry attempts by 35%."
- Training: "This new system reduced our model training time from days to hours"; "We can now train and deploy new versions of our Adaptive Acceptance model multiple times per week."
- Stated plan for 2025: "enhance our model architecture with new techniques for pretraining and fine-tuning foundational models".
- What the factors are: "the intricate interplay of factors such as bank policies, routing, messaging, formatting, and issuer preferences".
- Not published: the features, the label definition for a "false decline", the baseline for "70% greater precision", how the $6 billion is counted (gross value of retried-and-approved payments, or an estimate net of payments that would have succeeded anyway) [ASSUMPTION/JUDGEMENT].

**(b) Stripe's Payments Foundation Model, announced 7 May 2025.**

- Newsroom: "Stripe's Payments Foundation Model is trained on tens of billions of transactions, and captures hundreds of subtle signals about each payment that specialised models can't. It will be deployed across Stripe's payments suite to unlock additional performance improvements that were not previously possible." The only result given is in fraud: "Stripe increased its detection rate for attacks on large businesses by 64% practically overnight" [VERIFIED: https://stripe.com/newsroom/news/sessions-2025, published 2025-05-07].
- Blog, 15 May 2025: "it distills almost everything about each payment on Stripe down to a single, versatile embedding." "By classifying sequences of embeddings, our detection rate for attacks on large users significantly increased—from 59% to 97%—overnight." "This is just the beginning: we're exploring ways to roll out our Payments Foundation Model across our products" [VERIFIED: https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite, published 2025-05-15]. (59% to 97% is a 64% relative increase, which reconciles the two statements [ASSUMPTION/JUDGEMENT].)
- The engineer's account: a public post by Gautam Kedia, then in applied machine learning at Stripe: "we built a payments foundation model—a self-supervised network that learns dense, general-purpose vectors for every transaction, much like a language model embeds words. Trained on tens of billions of transactions, it distills each charge's key signals into a single, versatile embedding." He contrasts it with earlier models "trained on discrete features (BIN, zip, payment method, etc.)" where "each model requires task-specific training: for authorization, for fraud, for disputes", and credits those earlier models with "+15% conversion, -30% fraud" [WIDELY REPORTED: https://threadreaderapp.com/user/thegautam, 2025; a mirror of the author's post on X dated 7 May 2025, fetched; the original on X was not fetched].
- **Link to authorization.** The current product page says: "Trained on billions of transactions, Stripe's Payments Foundation Model uses self-supervised learning to improve the performance of products such as Authorisation Boost by capturing and analysing hundreds of subtle signals about each payment" [VERIFIED: https://stripe.com/authorization-boost, n.d., accessed 2026-11]. No authorization-rate result attributed to the foundation model has been published in the sources fetched; the only quantified result is card-testing detection [ASSUMPTION/JUDGEMENT].

**(c) Experiments as a mechanism.** The guide describes "running dozens of experiments with different issuing banks at the same time to understand which treatment is most likely to result in a successful payment" [VERIFIED: Stripe authorization guide, n.d.]. Whether these are randomised experiments, bandits or something else is not stated [ASSUMPTION/JUDGEMENT].

### 4.4 Stripe's headline claims, with wording

| Claim (exact wording) | Source and date | Metric definition published? |
| --- | --- | --- |
| "businesses using Authorization Boost's real-time optimizations can increase their acceptance rate by 3.8% on average, with some seeing up to 7%" | Stripe blog, 2025-05-15 | No: "acceptance rate" is not defined there; relative or percentage points not stated; cohort and baseline not stated |
| "Increase acceptance rates by 3.8% on average ... Businesses on custom interchange pricing can also lower card processing costs by up to 3.3%" | Product page, n.d., accessed 2026-11 | No |
| "recovering 20% of false declines on average" | Product page, n.d., accessed 2026-11 | No definition of false decline or of the denominator |
| "a record-high $6 billion in falsely declined transactions" recovered in 2024 | Stripe blog, 2025-02-12 | No |
| "Twilio SendGrid increased conversion by 2%"; "Notion has increased acceptance rates by 1.9%"; US Mobile "reduce network costs by over 2%" | Product page, n.d. | Customer statements |

[VERIFIED for each row at the URL named in 4.1 to 4.3.] A search summary reported a lower "2.2% on average" figure on other Stripe locale pages; it was not seen on the pages fetched and is not verified.

**Stripe's own disclaimer** should be quoted next to any of these: "Stripe doesn't guarantee any outcomes for your use of Authorization Boost features. The optimization calculations we provide are estimates" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md].

---

## PART 5: Adyen Uplift and its modules (chapter 09)

### 5.1 Names and launch ⚠

- Launch: "Adyen ... announces the launch of Adyen Uplift. The AI-powered payment optimization suite will help businesses increase payment conversion, simplify fraud management, and reduce the cost of payments", "Piloted by 60 enterprise businesses including: Patagonia, On, Indeed, NordSecurity and Fubo" [VERIFIED: https://www.adyen.com/press-and-media/adyen-uplift-launch, published 2025-01-09].
- Five modules, current naming: **Tokenize, Protect, Authenticate, Optimize, Personalize** [VERIFIED: https://docs.adyen.com/uplift.md, n.d., accessed 2026-11]. The marketing page orders them Personalize, Tokenize, Protect, Authenticate, Optimize and calls Uplift "One intelligence layer across the entire payment funnel" [VERIFIED: https://www.adyen.com/uplift, n.d., accessed 2026-11].
- Older names: Adyen's engineering article refers to "(legacy) RevenueProtect", the rules-based risk product, and the Auto Rescue documentation still points to a "RevenueAccelerate" report [VERIFIED: https://www.adyen.com/knowledge-hub/the-ai-behind-uplift, 2025-01-17; https://docs.adyen.com/online-payments/auto-rescue/cards.md]. RevenueAccelerate was the earlier name for the optimization feature set that is now the Optimize module [ASSUMPTION/JUDGEMENT; the old product page returns 404].
- Status in the documentation: "We are developing Adyen Uplift and will be adding more recommendations, insights, and settings. The experience is subject to change and might differ across regions, countries, and integration types." "Adyen Uplift is optimized for online payments and omnichannel integrations" [VERIFIED: https://docs.adyen.com/uplift.md].

### 5.2 What each module contains

| Module | Documented contents | Source |
| --- | --- | --- |
| Tokenize | Adyen tokenization, network tokenization, Real Time Account Updater (batch updater "Not recommended") | docs.adyen.com/uplift.md; partners/uplift-enablement.md |
| Protect | "the latest risk engine", machine learning "that uses Adyen's global transaction data", custom rules and labels as premium features, rule backtesting, data collection from the checkout page | docs.adyen.com/uplift.md |
| Authenticate | The Authentication Engine (3.4), dynamic 3D Secure rules, risk-based authentication with Protect premium | docs.adyen.com/uplift.md; partners/uplift-enablement.md |
| Optimize | Intelligent Payment Routing, Smart Payment Messaging, Auto Rescue, Auto Retries, enhanced scheme data, payment method recommendations, ERPS | partners/uplift-enablement.md; adyen.com/uplift/optimize |
| Personalize | Checkout dashboard, dynamic payment method ordering "prioritizing conversion or cost", checkout experiments | docs.adyen.com/uplift.md |

[VERIFIED: the two documentation pages and the marketing page named in the table, n.d., accessed 2026-11.]

- Partner-guide summary of Optimize: "Intelligent Payment Routing uses machine learning to select the lowest-cost or highest-converting route for each transaction. Enhanced Scheme Data lowers interchange fees on qualifying transactions. Auto Rescue recovers revenue from failed recurring payments by automatically retrying at the optimal time" [VERIFIED: https://docs.adyen.com/partners/uplift-enablement.md].
- Defaults differ per feature: Intelligent Payment Routing "is off by default and requires a one-click enablement in the Customer Area"; Smart Payment Messaging "is enabled by default"; Auto Rescue must be enabled per transaction or per merchant account [VERIFIED: same page].

### 5.3 Adyen's published engineering account

One article, "The AI behind Uplift", by Andreu Mora (SVP / Global Head of Engineering Data, Adyen), 17 January 2025 [VERIFIED for every bullet: https://www.adyen.com/knowledge-hub/the-ai-behind-uplift, published 2025-01-17]. It is more specific about infrastructure than anything Stripe has published on Adaptive Acceptance.

- **Design idea.** "In the past we have deployed ML models to locally optimize every step of a transaction in isolation." Uplift "consists of a collection of machine learning models of various natures that share awareness and knowledge. These models are optimized globally through Reinforcement Learning and share the same objective: to balance fraud, cost, and conversion in harmony."
- **How the models coordinate.** "The current version of Uplift uses message passing, which provides a simple but efficient approach to create awareness that models can condition their estimates on." Larger combined deep-learning models were tried and "would often compromise the engineering requirements (latency, uptime) of online deployments in a critical flow".
- **Latency budget.** "SLA for transaction processing: 1 second including acquirer communications which consumes around 600 ms." "Every single transaction touched between 2 and 5 different AI endpoints where a machine-learning model was making a decision and had an allocated latency of 20 ms (median)." The inference service, named "Alfred", serves "every request with a p50 of 20 ms and p99 of 100 ms".
- **Scale stated.** Black Friday to Cyber Monday 2024: "Peak transaction rate: 163K per minute (2.7K transactions per second)", "Peak API requests: 25K per second".
- **Infrastructure.** "all critical flows of Adyen run on-premise." A feature platform uses Spark for slow features and "Apache Flink" for fast ones, "storing and serving them in a Cassandra backend deployed in different datacenters".
- **Deployment discipline.** "We follow a principal-challenger model for every deployment": new models run first as "ghost" (logging only), then "challenger" on a traffic split, and replace the principal when stronger "with statistical confidence".
- **Baseline for its own claims.** "The unified control group is a split of traffic that is consistent across all elements of a transaction and where models do not act." Adyen still applies a "market baseline" to it: "blocking cards that we know are stolen, SCA (Strong Customer Authentication) exemption, forcing a network token, and retrying with a challenge if the authentication fails. This results in a lower, but more honest uplift calculation for our system."
- **Shopper recognition.** A graph that links transaction attributes "consists of more than 100B nodes and 300B edges"; "we have seen more than 1 billion individuals".
- **Offline evaluation.** Off-policy evaluation lets Adyen test variants "instantly w/ high correlation (+80%) to On-policy Estimates (actual AB Tests)".
- **Foundation model.** "Transformers and Self-supervision are enabling us to build a foundational payments model trained on billions of transactions" (stated as work in progress in January 2025).

### 5.4 Adyen's headline claims, with wording

| Claim (exact wording) | Source and date | Metric definition published? |
| --- | --- | --- |
| "AI helps businesses increase payment conversion rates by up to 6% compared to legacy implementations"; "businesses seeing an overall uplift of up to 6% on their payment conversion rate" | Press release, 2025-01-09 | Footnote elsewhere: "Based on the average conversion improvement of merchants that participated in the pilot and used all modules" (product update, 2025-01). "Up to" and "average" are both used for the same 6% |
| "Adyen's pilot enterprise customers have reduced their manual risk rules by 86% on average, and 35% of customers have completely eliminated manual rules" | Press release, 2025-01-09 | Count of rules; not a payment outcome |
| "Adyen Uplift has reduced payment cost by up to 5% for pilot customers in the U.S." | Press release, 2025-01-09 | "Payment cost" not defined |
| "We've increased our conversion rate on customer initiated transactions by 10%" (Kes Saulis, Nord Security); "increased our conversion rate by up to 2%" (Luca Spichtig, On) | Press release, 2025-01-09 | Customer statements |
| "AI trained on over a trillion dollars worth of global payments data"; "For a retail merchant on the Adyen platform, there is more than a 90% chance that Adyen has seen that shopper before" | Press release, 2025-01-09 | Not a performance metric |

[VERIFIED for each row: https://www.adyen.com/press-and-media/adyen-uplift-launch, published 2025-01-09, and https://www.adyen.com/the-latest/boost-your-payment-conversion-with-adyen-uplift, published 2025-01.] The current marketing page repeats "Up to 6% increase in conversion", "86% fewer manual rules" and "Up to 5% reduction in payment costs" [VERIFIED: https://www.adyen.com/uplift, n.d., accessed 2026-11], so the public numbers have not been updated since the pilot of 60 businesses.

**Stripe vs Adyen (Parts 4 and 5)**

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Bundle | Authorization Boost (Adaptive Acceptance, network tokens, card account updater), priced per successful transaction for custom-pricing accounts | Uplift, five modules spanning checkout, risk, authentication, tokens and routing; pricing not public (the FAQ question exists, the answer was not captured) | Stripe sells authorization as one priced product; Adyen frames it as a suite across the funnel [ASSUMPTION/JUDGEMENT] |
| Published model detail | Model family (XGBoost to "TabTransformer+"), embeddings, retraining cadence; foundation model (self-supervised, embeddings) | Reinforcement learning across models, message passing, latency budgets, serving stack, control-group design | Stripe publishes model architecture and outcomes; Adyen publishes system architecture and method [ASSUMPTION/JUDGEMENT] |
| Headline number | 3.8% average acceptance-rate increase (2025, repeated 2026) | Up to 6% conversion (pilot, January 2025) | Different metrics, cohorts and baselines; they cannot be compared [ASSUMPTION/JUDGEMENT] |
| Baseline described | Estimated counterfactual per payment; 30-day A/B test offered | Unified control group with a "market baseline" | Both acknowledge the counterfactual problem; only Adyen states what its control group still receives [ASSUMPTION/JUDGEMENT] |
| Rules versus learning | Merchant sets retry envelope; model decisions are not configurable | Merchant sets a routing objective and a messaging "optimization level"; custom risk rules are a premium feature | Adyen exposes more dials [ASSUMPTION/JUDGEMENT] |
| What neither publishes | Features, labels, per-issuer results, false-positive cost of blocked payments, an audited lift | Same | The reader cannot verify either claim from public data |

**For readers new to payments.** *False decline*: a legitimate payment the issuer refused, usually on suspicion of fraud. *IC+ pricing* (interchange plus): a pricing plan where the merchant pays the actual network costs plus the provider's fee, so reducing network fees saves the merchant money directly. *Control group*: the share of traffic an optimization does not touch, kept to measure what the optimization changed.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Both providers now make decisions inside the authorization call that the merchant did not ask for: reformatting, retrying, switching networks, blocking. The merchant's system must tolerate one API call producing several network attempts, a "blocked" outcome that never reached the issuer, and a credential or network different from the one requested. Adyen's published budget (about 600 ms of a 1-second target spent on the acquirer leg, 20 ms median per model call) shows why these decisions are made by small models in the payment path and why an external orchestrator adding a hop competes for the same second.

---

## PART 6: How such claims should be measured (chapter 09)

- **Stripe's attribution method.** "For each payment, Stripe assesses the likelihood that optimizations contributed to its success, given that some payments might have otherwise still been approved ... If you apply multiple optimizations to a single payment, we attribute the benefit to the one most likely responsible for approval." Worked example: 100 optimized payments of 50 USD with a 20% likelihood each give "100 payments * 50 USD * 0.20 = 1,000 USD" of recovered volume [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md, n.d., accessed 2026-11]. This is a modelled estimate, not a measured difference.
- **Stripe's cost-savings method.** "Stripe infers what network costs would have been without the use of optimizations ... However, Stripe doesn't reconcile these estimates directly with the fees applied to your account." Estimates are shown "only for domestic payments in the US and Canada" [VERIFIED: same page].
- **Stripe's A/B test** (previewed April 2026): "Stripe randomizes your eligible payment volume between two equal groups"; the test runs 30 days; "Final results are available 37 days after test initiation. Stripe waits 7 days to account for payments that initially failed during the 30-day test period but were successfully retried"; results use deduplicated payment success rates; significance is declared "when the probability of observing a difference at least this large (assuming no true difference exists) is less than 5%" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization/a-b-testing.md, n.d., accessed 2026-11].
- A limit Stripe states itself: card account updater "Always runs on both the Current features and Authorization Boost groups ... because Stripe can't apply card credential updates selectively", so its effect is estimated, not tested. After cancelling, "You can't run another Authorization Boost test for 12 months" [VERIFIED: same page].
- The dashboard's comparison chart "shows the raw rate, rather than the deduplicated rate", while the A/B test uses the deduplicated rate [VERIFIED: optimization page and A/B testing page]. The two will not match.
- **Adyen's experiments.** "Experiments are not simulations. They are performed on real transactions, processed with your live Adyen account." Three kinds: checkout experiments (remove a payment method, or dynamic ordering), optimization experiments ("You can only start optimization experiments following a recommendation"), and risk experiments comparing two risk profiles, which "require Protect premium" [VERIFIED: https://docs.adyen.com/uplift/uplift-experiments.md, n.d., accessed 2026-11].
- **Guardrails the documentation implies.** Adyen says ERPS "may have a negative impact on authorization rates"; Stripe says its features "Predict and proactively decline charges most likely to be rejected, while balancing impact to your auth rates" [VERIFIED: Adyen partner guide; Stripe product page]. Both therefore concede that the cost optimization can remove payments that would have been approved.

A measurement checklist for the chapter [ASSUMPTION/JUDGEMENT]: (1) fix the metric and denominator (authorization rate or payment success rate; raw or deduplicated; count or value); (2) fix the cohort (card-not-present only; first payments or renewals; which countries); (3) use a randomised holdout, not a before-and-after comparison, because issuer behaviour, seasonality and card mix move the rate by more than the claimed lift; (4) wait for retries to complete before reading the result; (5) track guardrails in the same test: fraud and dispute rate, network fees, blocked-payment count, latency; (6) ask what the control group still receives, since a "market baseline" control and a "nothing" control give different lifts.

---

## PART 7: Routing inside one provider (chapter 10)

### 7.1 US debit: the legal basis for merchant routing choice

- Regulation II "prohibits all issuers and networks from restricting the number of networks over which debit transactions may be processed to less than two unaffiliated networks, and from inhibiting a merchant's ability to direct the routing of a debit transaction over any network that the issuer has enabled to process it" [VERIFIED: https://www.federalreserve.gov/paymentsystems/regii-about.htm, n.d., accessed 2026-11]. It implements section 1075 of the Dodd-Frank Act, commonly called the Durbin Amendment.
- The 2022 clarification: "the updates specify that debit card issuers should enable at least two payment card networks to process all debit card transactions, including 'card-not-present' transactions, such as online payments." "When the Board initially issued the rule in July 2011, the market had not developed solutions to broadly support multiple networks for card-not-present debit card transactions." "The final rule will be effective July 1, 2023." "The final rule does not modify requirements concerning interchange fees" [VERIFIED: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20221003a.htm, published 2022-10-03] **(evidence age: 4 years; a final rule, still in force as far as this session found)**.
- Correction for writers: the two-network requirement dates from 2011. The 2023 change extended it in practice to online payments. Adyen's own article describes it loosely ("In July 2023, Durbin was revised ... mandating that all debit cards issued in the US be branded by at least one additional unaffiliated network") [VERIFIED: https://www.adyen.com/knowledge-hub/maximize-your-profit-now-with-intelligent-payment-routing-for-us-debit-cards, published 2024-09-26]; the Federal Reserve's wording above is the accurate one.
- ⚠ The Federal Reserve's page also lists a pending proposal "to lower the maximum interchange fee that a large debit card issuer can receive" [VERIFIED: Regulation II page]; its status was not checked.

### 7.2 Least-cost routing and Adyen's Intelligent Payment Routing

- The unaffiliated US debit networks Adyen names: "Accel, Maestro USA, NYCE, PULSE, or STAR" [VERIFIED: https://docs.adyen.com/online-payments/network-tokenization.md].
- Launch claim: "SAN FRANCISCO, Sept. 9, 2024 — Adyen ... today announced Intelligent Payment Routing for US debit payments, the only AI-based solution in the market that simultaneously optimizes and improves revenue and lowers costs. In a pilot of over 20 enterprise merchants — including eBay, 24 Hour Fitness, Microsoft, among others — Adyen achieved an average of 26% cost savings with a 0.22% uplift in authorization rates against earlier debit performance." "Some merchants saw cost savings as high as 55% and 52% with uplift in authorization rates as high as 1.15% and 0.69%. One customer saw savings as high as $600,000 within the first 30 days" [VERIFIED: https://www.adyen.com/press-and-media/adyens-intelligent-payment-routing-usdebit, published 2024-09-09].
- Metric notes: the comparison is "against earlier debit performance", a before-and-after comparison, not a randomised test. "Cost savings" is not defined (which fees, on which share of volume), and whether 0.22% is relative or in percentage points is not stated [ASSUMPTION/JUDGEMENT].
- Adyen's own framing against plain least-cost routing: "Dual optimization: Minimizes interchange and scheme fees for least cost routing (LCR) while maximizing approval rates with AI" [VERIFIED: Adyen knowledge hub, 2024-09-26]. The same press release says debit was "58% of all US transactions this June" on Adyen's platform.
- In the documentation the feature is general, not only US debit: it routes "each transaction to the highest-converting or lowest-cost acquirer or network", is "off by default", needs "at least two available routes", and "For US and Australia, choose between: balance conversion and cost (recommended), prioritize cost, or prioritize conversion" [VERIFIED: https://docs.adyen.com/partners/uplift-enablement.md, n.d., accessed 2026-11].
- Merchant overrides: routing is based on "Any routing priorities set for your merchant account. For example, 1: PULSE and 2: Visa" and then "Optimized routing determined by Adyen, provided this does not contradict any routing priorities". A single payment can be forced onto a network with `paymentMethod.brand` after a `/cardDetails` lookup [VERIFIED: https://docs.adyen.com/online-payments/network-tokenization.md].
- In person, Adyen terminals apply "Least cost routing: use a card network that results in the lowest fees in your situation" through card application selection rules, with a legal limit in Europe: for co-badged cards issued in the EEA, "if a cardholder uses a co-badged card, and you support both brands, you must let them choose the brand to pay with" [VERIFIED: https://docs.adyen.com/point-of-sale/aid-selection-rules.md, n.d., accessed 2026-11].
- **Stripe** documents debit-network routing only as a retry: Adaptive Acceptance "might automatically retry an eligible transaction on a US debit network (also known as PINless network) after it's declined on an international network" and "might reattempt a declined payment on an alternative card network" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md]. No Stripe page describing first-attempt least-cost debit routing, a merchant-set network priority, or a cost-savings claim for debit routing was found (tried a US debit routing docs URL, 404; searched the fetched optimization, declines and product pages). The 2025 description of Authorization Boost does say it will "route transactions across networks" [VERIFIED: Stripe Sessions 2025 product updates].

### 7.3 Other intra-provider routing

- Stripe on connectivity failover: "If processor downtime does occur, Stripe can dynamically route payments to the best connections. For example, Stripe automatically shifts volume when Visa's US data centres go down for maintenance. Stripe is also directly integrated with six major global card networks" [VERIFIED: https://stripe.com/guides/optimizing-authorization-rates, n.d.].
- Adyen routes among acquiring routes ("the acquiring route with the highest authorization success rate and the lowest cost. You decide what are the objectives: maximizing conversion, minimizing cost or balancing both") [VERIFIED: https://www.adyen.com/uplift/optimize, n.d.]. Adyen can also act as a gateway to another acquirer for some methods: its External settlement detail report "shows details of transactions for which Adyen is not the acquirer. For example, if you have an agreement with American Express or PayPal" [VERIFIED: https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report.md, n.d., accessed 2026-11].

**Stripe vs Adyen (Part 7)**

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| US debit routing | PINless debit network used as a retry path after a Visa or Mastercard decline (docs, n.d.; announced as new in April 2026) | Named product since September 2024, first-attempt routing, three merchant-selectable objectives, merchant network priorities, per-payment override | Adyen sells debit routing as a cost product; Stripe has published it only as a recovery tactic [ASSUMPTION/JUDGEMENT] |
| Published claim | None for debit routing | 26% average cost savings, 0.22% authorization uplift, pilot of 20+ merchants | Vendor claim, before-and-after |
| Merchant control over the network | Not documented | Priorities and forced brand | |
| In-person least-cost routing | Not researched in this brief (see the `acquiring` brief) | Documented through application selection rules | |

**For readers new to payments.** *Co-badged debit card*: a debit card that can be processed over two networks, for example Visa and STAR. *Least-cost routing*: sending each debit payment over whichever of the card's networks charges the merchant less. *PINless debit*: processing an online debit payment over a domestic debit network without the PIN that network requires in a shop. *Regulation II*: the US Federal Reserve rule that requires every debit card to work on two unaffiliated networks and lets the merchant choose.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. The cheapest network is not always the best: debit networks differ in approval rates, dispute rules, token support and whether they carry the data a fraud model wants, which is why Adyen offers "balance" as the recommended objective. Routing choice changes downstream records: the network on the settlement line, the fee lines and the dispute process can differ from what the card's front face suggests, so the ledger must record the network actually used per attempt. A merchant with a network priority list holds a routing rule inside the provider; that rule is configuration to be versioned and reviewed like code.

---

## PART 8: Routing across providers, and the vault problem (chapter 10)

### 8.1 Stripe Orchestration ⚠

- Status: "Orchestration is in private preview" [VERIFIED: https://docs.stripe.com/payments/orchestration.md, n.d., accessed 2026-11]. It was announced on 7 May 2025: "Stripe launched Orchestration, which helps businesses set up, manage, and optimise performance across multiple payment providers – all from the Stripe Dashboard" [VERIFIED: https://stripe.com/newsroom/news/sessions-2025, published 2025-05-07]. Eighteen months later the documentation still says private preview, and the April 2026 announcement list does not mention it.
- What it does: "Update your PaymentIntents integration to route payments to any of the Stripe-supported processors, or automatically route payments created through Billing, Checkout, Payment Links, or the Dashboard"; "automatically retry failed payment transactions with alternative processors"; "Analyze payments performance across each of your processors"; refunds through Stripe's Dashboard or Refunds API, where "those processors administer the refunds" [VERIFIED: orchestration page].
- Contract and liability stay with the other processor: "your third-party processor continues to act as the processor for payments routed to it. All related activity (including payment processing fees and liability for transaction losses) remain subject to the terms that you agreed to with that processor" [VERIFIED: same page].
- **Supported processors in the feature table: Adyen, Braintree, Worldpay WPG.** Per-processor support includes automatic and manual capture, full and partial refunds, 3DS, statement descriptors, Apple Pay and Google Pay, and recurring transactions; network tokens are supported on Adyen and Braintree and "Unsupported" on Worldpay WPG. Footnotes: "Multicapture is currently unsupported"; "3DS isn't supported with Apple Pay and Google Pay (DPAN). Google Pay (FPAN) isn't supported on **Adyen**" [VERIFIED: https://docs.stripe.com/payments/orchestration/feature-support.md, n.d., accessed 2026-11].
- **Stated exclusions:** "Orchestration feature support doesn't include non-card payments or Link, Capital, Connect, Terminal, or Organizations." "Orchestration also doesn't support disputes or settlement-related activity. To manage these activities, access your third-party processor's dashboard" [VERIFIED: orchestration page]. "Orchestration doesn't support the Setup Intents API and flexible acquiring features on other processors. For transactions that involve a 3D Secure request, you're responsible for providing Stripe with the Acquirer BIN that corresponds to the processor you route those transactions to" [VERIFIED: https://docs.stripe.com/payments/orchestration/route-payments.md, n.d., accessed 2026-11]. Off-session routing "only supports card payments and doesn't support Connect or requests that contain raw card data" [VERIFIED: https://docs.stripe.com/payments/off-session-payments/orchestration.md].
- **Rules.** Conditions: amount (with currency), BIN, card country, card issuer, card type (credit, debit, prepaid), currency, metadata. "Stripe executes the conditions in order, from left to right, and applies the first action that matches a payment's condition." Each action names a main processor and an optional retry processor. "You can only have one active set of rules in each sandbox and in live mode." "Active rules are read-only. To make changes, duplicate them and edit the draft." "If you don't have active rules, payments route to Stripe" [VERIFIED: https://docs.stripe.com/payments/orchestration/rules.md, n.d., accessed 2026-11].
- **Retry across processors:** at most one more attempt ("retry the payment one more time if the payment fails on the main processor"). Not retried when 3DS was attempted and failed, or succeeded but the payment still failed; not retried when the retry processor lacks a feature the payment uses. A Radar block on Stripe counts as a decline and is retried on the other processor. Adaptive Acceptance can add its own retry, so "Stripe might ultimately initiate two retries" [VERIFIED: https://docs.stripe.com/payments/orchestration/retries.md and route-payments.md, n.d., accessed 2026-11].
- **Unsupported features fail loudly:** "the request fails with a `400` error code `orchestration_unsupported`", unless the merchant opts in to "error protection", where "we route the payment to Stripe instead of the originally determined payment processor" [VERIFIED: feature-support page].
- **Records change shape.** "Stripe creates Payment Records and Payment Attempt Records instead of Charges for payments routed to other processors. If you rely on Charges for any of your internal reporting or reconciliation, you must use Payment Attempt Records instead across all of your Stripe volume." "Stripe only creates Balance Transactions for payment volume processed on Stripe ... If your back-end systems assume there's always a Balance Transaction after a successful payment, that's no longer true" [VERIFIED: route-payments page].
- Link stays on Stripe: "Link transactions are automatically excluded from your routing rules and always processed on Stripe" [VERIFIED: route-payments page].
- Stripe's analytics cannot see inside the other processor: "You can't specify an authorization rate if you set the processor filter to a non-Stripe processor. Stripe doesn't have access to non-Stripe data" [VERIFIED: https://docs.stripe.com/payments/analytics/acceptance.md].
- Claims made on stage (Stripe Sessions 2026, Jon Krauss of Stripe): Orchestration is "built on Stripe's core infrastructure"; the customer 123cards "in about four months ... were able to double their dunning recovery rate ... and it led to over $140,000 in recovered revenue" [VERIFIED: https://stripe.com/sessions/2026/more-psps-more-problems, transcript, n.d.; Sessions 2026 was held in late April 2026]. The same talk says Billing, Checkout, Radar and 3D Secure are now usable with other processors.

### 8.2 Stripe Vault and Forward API

- Purpose: "The Vault and Forward API allows you to tokenize and store card details in Stripe's PCI-compliant vault and route that data to supported processors or endpoints", to use the Payment Element across processors, "Use Stripe as your primary vault for card details across processors", or "Route card details to your own PCI compliant token vault" [VERIFIED for this section: https://docs.stripe.com/payments/vault-and-forward.md, n.d., accessed 2026-11].
- Access: "available only to businesses with a dedicated Stripe account team".
- Mechanism: the merchant creates a `ForwardingRequest` with a `payment_method`, the destination `url`, the request body with card fields left blank, and a `replacements` list (`card_number`, `card_expiry`, `card_cvc`, `cardholder_name`). Stripe inserts the card data and sends the request. "Stripe forwards the request using the API keys you provide, and only retains hashed and encrypted versions of destination endpoint API keys."
- It is a proxy, not a payment: "the Vault and Forward API doesn't confirm or capture PaymentIntents. As a result, you might unintentionally use them to capture a payment on Stripe that was already captured on another processor."
- Response handling: "Stripe synchronously waits for a response from the destination endpoint. The timeout period for this response is less than a minute. Stripe redacts identified PCI-sensitive data, stores the redacted response". Any destination response is a success to Stripe: "when the destination endpoint returns a status code of `400` to Stripe, the Vault and Forward API responds with a status code of `200`".
- **Supported destinations** are an allow-list of exact endpoints. Named: Accertify, Adyen, Basis Theory, Braintree, CardPointe, Chase Orbital, Checkout, Evervault, Expedia, Fat Zebra, Fiserv, FlexPay, GMO Payment Gateway, PaymentsOS, PCI Vault, ProcessOut, Rewards Network, Shift4, SoftBank, Spreedly, TabaPay, TokenEx, VGS (Very Good Security), Worldpay, Xsolla, Yuno ⚠. For Adyen the endpoints are `/payments` and `/storedPaymentMethods` of Checkout API v68 to v72. "Stripe supports HTTPS APIs that accept JSON or XML requests ... If your destination endpoint isn't supported ... share the endpoint details with your account team."
- The list includes competitors' vaults and orchestrators (Spreedly, VGS, Basis Theory, TokenEx, Evervault, Yuno), so Stripe documents itself as a source vault for other orchestration layers [ASSUMPTION/JUDGEMENT on the interpretation; the list is verified].
- Limits: "CVCs expire automatically after a certain time period and also expire when used with the Vault and Forward API"; credentials saved through Link "are excluded from forwarding"; Apple Pay and Google Pay device tokens can be forwarded with network-token replacement fields (`network_token_number`, `network_token_cryptogram`, and so on) on request to the account team.
- Idempotency: "Use a different and unique key for Stripe and any idempotency keys you provide on the underlying third-party request."
- Stripe now positions Forward as the lower-level option and Orchestration as the managed one: "With Stripe Orchestration, Stripe manages the full processor integration on your behalf ... Same Payment Intents API, no PSP-specific code".

### 8.3 Stripe data portability (PAN export)

- Position: "We believe our customers own the sensitive data they entrust to Stripe. We make sure that you have access to this data—even if you're moving elsewhere. If you decide to leave Stripe for another payment processor, we'll work with your new processor's team to securely transfer your credit card data" [VERIFIED for this section: https://docs.stripe.com/get-started/data-migrations/pan-export.md, n.d., accessed 2026-11].
- Conditions: "we can only transfer your card data to another PCI DSS Level 1-compliant payment processor". Stripe requires the recipient's "current PCI Attestation of Compliance (AOC), or their listing on Visa's Global Registry of Service Providers" and a "PGP public encryption key, which must be 4096 bits or greater in length ... hosted over HTTPS on one of the processor's domain names".
- Content: "an encrypted JSON export file containing your data, including the card details of your customers, email addresses, and any attached metadata". The example shows customer id, card id, full card number, name, expiry and billing address.
- Not exported: "Stripe doesn't export your account's payment history, subscriptions, or other objects"; "We exclude any credentials saved through Link from our exports."
- The export goes processor to processor, started by contacting Stripe support; no self-service API, duration or fee is documented. Network tokens are not mentioned on the page, so whether tokens provisioned by Stripe move with the export is unknown [ASSUMPTION/JUDGEMENT].

### 8.4 Adyen's stance

- **Forward.** "You can forward payment details that you stored with Adyen to a PCI compliant third party, like a payment service provider (PSP). We support forwarding card details, and network tokens." A POST `/forward` request (Checkout API v70 or later) carries placeholders; "Adyen replaces the placeholders with the payment details and makes a request to the third party API on your behalf" and returns "the third party response as a string". Three card flows: forward a token, forward a token with CVC, or "Forward non-tokenized card details ... to let the third party tokenize the card details". It must be enabled by Adyen's support team, and "To forward network tokens, you must create a token with Adyen for the same payment details" [VERIFIED: https://docs.adyen.com/online-payments/tokenization/forward-payment-details.md, n.d., accessed 2026-11]. No allow-list of destinations is published on the page.
- **Multi pay-in** ⚠: "Multi pay-in is currently in pilot phase." It "consolidates all funds processed for your users within Adyen's infrastructure, making it possible for you to combine payments processed by Adyen with third-party acquired volume". The platform receives the other provider's payouts into a "multi pay-in account", then allocates each payment to balance accounts with a `/payments` request carrying split instructions. "To comply with financial regulations, you must allocate the funds you receive in your multi pay-in account to the balance accounts in your balance platform within 24 hours." Limitation: "Multi pay-in does not support separate authorization and capture" [VERIFIED: https://docs.adyen.com/marketplaces/multi-pay-in.md, n.d., accessed 2026-11].
- Multi pay-in is consolidation of money for platforms, not routing of authorizations: Adyen does not send the payment to the other provider; it receives that provider's settlement [ASSUMPTION/JUDGEMENT, from the flow described].
- Stripe has announced the same idea for the same reason: "We previewed the ability for marketplaces that sell in Europe to continue using multiple payment providers while making unified payouts through Stripe. This will help marketplaces comply with upcoming PSD3 regulations without disrupting their multiprocessor setups" [VERIFIED: https://stripe.com/blog/everything-we-announced-at-sessions-2026, published 2026-04-29] ⚠ (private preview Q3, public preview Q4 2026 per the same list).
- **Import and export.** Adyen documents importing stored cards from another provider [VERIFIED: https://docs.adyen.com/development-resources/migrating-payment-data.md exists and is titled "Import data from another payment provider", n.d.]. An export procedure exists in Adyen's help centre (a formal letter of intent, then a CSV export once the receiving vault confirms the format) [WIDELY REPORTED: search summary of https://help.adyen.com/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export, 2026; the page itself could not be read].
- **No multi-acquirer orchestration product.** Nothing in Adyen's documentation index offers routing of payments to other PSPs under rules, comparable to Stripe Orchestration (searched the docs index for orchestration, routing, third-party, external acquirer). Adyen's routing product chooses among routes inside Adyen (7.2), and network tokenization "cannot be used with external acquirer connections" (3.2). Adyen's public argument is the opposite one: "Unlike fragmented legacy architectures, Adyen brings payments onto one single platform" [VERIFIED: https://www.adyen.com/uplift, n.d., accessed 2026-11].

**Stripe vs Adyen (Part 8)**

| Aspect | Stripe | Adyen | What the difference suggests |
| --- | --- | --- | --- |
| Route payments to another PSP | Orchestration, private preview since May 2025; Adyen, Braintree, Worldpay WPG | Nothing public found | Stripe is willing to be the control plane over competitors, including Adyen; Adyen is not [ASSUMPTION/JUDGEMENT] |
| Forward stored cards to a third party | Vault and Forward; account-team only; published allow-list of about 26 destinations | `/forward`; support-enabled; cards and network tokens; no published destination list | Both now offer a proxy out of their vault; neither is self-service [ASSUMPTION/JUDGEMENT] |
| Bulk export when leaving | Documented policy and requirements | Process exists; public detail thin | Both rely on a processor-to-processor transfer under PCI rules |
| Multi-provider for platforms | Unified payouts across processors, previewed 2026 | Multi pay-in, pilot | Both respond to platforms that must keep several acquirers while centralising funds |
| What orchestration leaves out | Disputes, settlement, non-card methods, Connect, Terminal, Link | n/a | Routing is unified; money and its records are not |

Why would a provider help a merchant use its competitors? Stripe's stated reasons, from its own stage: large companies already do it ("About 62% of enterprises actually suggest they prefer to use multiple PSPs", citing unnamed industry research), and "Stripe Orchestration is an investment in a broader strategy of an open architecture. You're not going to have to be locked into Stripe" [VERIFIED: Sessions 2026 transcript]. The commercial reading, that owning the vault, checkout, billing and fraud layers matters more to Stripe than owning every authorization, is inference [ASSUMPTION/JUDGEMENT].

**For readers new to payments.** *Payment orchestration*: a layer that holds the card vault and decides, per payment, which provider processes it. *Vault*: the PCI-compliant store of real card numbers; whoever holds it controls where the cards can be charged. *Failover*: sending a payment to a second provider when the first is down or declines. *Token portability*: whether the stored-card references a merchant holds can be used at, or moved to, another provider.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Stripe's documentation lists exactly what a merchant's own payment service must absorb when a second provider appears: a payment object that no longer implies a balance movement, two dispute and settlement back offices, features that exist on one side only (multicapture, SetupIntents, some wallets), and an acquirer BIN that must match the processor for 3DS. A cross-provider retry is safe only when the first attempt is known to have failed: Stripe refuses to retry after a 3DS attempt for that reason. The vault decides the exit cost: forwarding gives per-request access to the cards, an export gives the cards themselves, and neither moves network tokens cleanly.

---

## PART 9: Independent orchestrators and merchant accounts (chapter 10)

### 9.1 Dedicated orchestrators, as contrast

All statements are vendor self-descriptions.

| Vendor | Verified facts | Source |
| --- | --- | --- |
| **Spreedly** | "Hold every credential in your own vault, use it with any provider, and change processors without asking a customer to re-enter a card." Acts as a token requestor: "As a Token Requestor Token Service Provider (TR-TSP), Spreedly has completed integrations with Visa and Mastercard allowing merchants to request network tokens using their merchant-specific TRID" | https://www.spreedly.com/ and https://developer.spreedly.com/docs/network-tokenization, n.d., accessed 2026-11 |
| **Primer** | Homepage lists a unified vault ("Unify and manage every payment credential in a single, compliant vault"), fallbacks ("Route payments to a secondary processor in the event of a failure"), no-code workflows, and cross-provider observability | https://primer.io/, n.d., accessed 2026-11 |
| **Gr4vy** | "Payment Orchestration Platform for Enterprises"; "Infrastructure as a service: Your own instance, anywhere"; "over 400 payment methods and anti-fraud providers"; a "Vendor-agnostic data vault" | https://gr4vy.com/, n.d., accessed 2026-11 |
| **Hyperswitch (Juspay)** | Open source under the Apache License 2.0; repository created 2022-10-17; self-described as "Open source, composable payments platform ... SaaS and Self-host options"; routing "across Stripe, Adyen, Braintree, Worldpay, Checkout.com, and 120+ others to the PSP with the highest predicted auth rate"; supports "bring-your-own-vault to connect existing providers including VGS and TokenEx" | https://github.com/juspay/hyperswitch (README and repository metadata), accessed 2026-11 |

[VERIFIED: each page fetched in this session at the URL in the row.]

- A dependency between the anchor and the contrast: for network tokens provisioned by Spreedly to be used on Stripe, "Please contact Stripe to have your merchant account configured to use network tokens provisioned through Spreedly" [VERIFIED: Spreedly network tokenization documentation]; and Stripe's Forward allow-list includes `core.spreedly.com/v1/payment_methods.json` [VERIFIED: Stripe Vault and Forward page]. Orchestrators and providers interlock through manual enablement, not open interfaces [ASSUMPTION/JUDGEMENT].
- The orchestrator's distinguishing asset is the merchant-specific token requestor ID: a network token requested under the merchant's own TRID can in principle be used at any acquirer, while a token requested by a PSP is tied to that PSP [ASSUMPTION/JUDGEMENT; consistent with Spreedly's description, not verified from network documentation].

### 9.2 Merchant accounts of multi-provider routing

Few exist in public, and the best one found is recent.

**Canva** (Joshua Barton, Global Product Lead, at Stripe Sessions 2026; in-house orchestration; five integrated PSPs) [VERIFIED for every bullet: https://stripe.com/sessions/2026/more-psps-more-problems, transcript, n.d.; event held late April 2026]:

- Motive: "the real reason why we did this was redundancy. We accept payments in over 190 countries".
- Degradation, not outage, is where it paid off: provider uptime figures do not include "degraded performance. If a network goes down in Mexico or if a payment method goes down in Indonesia, that's not included in your five-nines uptime."
- First-attempt routing mattered more than fallback: "the real power is where you send the traffic the first time." Routing moved from country, to "BIN and issuer", to separate merchant IDs: "you had a mid for good traffic, a mid for bad traffic".
- Costs: "it takes maybe six months or more to integrate a new PSP"; then contracts and KYC; then "three-plus months warming up" a new merchant ID; then tuning. "once you start including operational people, it's close to 30 people just working on this." Operations staff must use a second portal for chargebacks and refunds.
- On choosing an external orchestrator: "a lot of orchestrators out there will tell you they connect to 400 PSPs ... It's all about the quality of the integration to the PSPs and depth of that integration"; "If they don't have the five nines uptime ... you're bringing Stripe's uptime down because the orchestrator's how you get there."
- Verdict: "it's worth it, so do it", with the caveat that "best performance have come with working with our PSPs like Stripe over a long time".

**Stripe's own framing in the same talk** (Alex Ginet, head of product for core payments, and Jon Krauss) [VERIFIED: same transcript]: three motives (redundancy, performance and cost, geographic expansion); an illustrative sum ("a hundred million dollar a year" business finding "half a percent more authorization rate" gains "$500,000"); the build-in-house trade-off ("you need to use things like network tokenization, card account updater, and those are independent integrations themselves with the schemes"); and the orchestrator trade-off ("it creates concentration risk with the orchestrator themselves ... there are added milliseconds to the end-to-end transaction flow"). This is a vendor talk that ends in a product pitch; Canva's remarks are the independent part [ASSUMPTION/JUDGEMENT].

**Shopify** (2022): its payment service keys circuit breakers by country because gateways route through local acquirers: "we add the merchant's country code to the endpoint host and port to create a more fine-grained Semian identifier, so an open circuit due to an local outage in one country doesn't affect transactions for merchants in other countries" [VERIFIED: https://shopify.engineering/building-resilient-payment-systems, published 2022-07-28] **(evidence age: 4 years; describes a technique, not a multi-provider strategy)**.

**Uber** (2018): a meetup summary says Uber supports "over ten ways to accept payments via different payment processor integrations", and describes patterns for integrating new payment service providers: "storing request metadata for idempotent multiplexing and retries, efficient generation of external IDs with limited namespaces, and using deterministic batching" [VERIFIED: https://www.uber.com/blog/payments-platform/, published 2018-12-05] **(evidence age: 8 years; likely describes a replaced system; no routing logic or approval figures are given)**.

**Airbnb, Booking.com:** nothing verifiable in this session (see Research limitation). Writers should not attribute multi-provider routing practices to them from this brief.

**Stripe vs Adyen (Part 9).** Stripe hosts and publishes a customer talk on multi-provider strategy and lists orchestrators among its Forward destinations. No Adyen talk, post or documentation page on merchants using several providers for card processing was found (searched Adyen's docs index and the fetched knowledge-hub and Uplift pages), beyond Multi pay-in for platforms and the Forward API.

**For readers new to payments.** *Merchant ID (MID)*: the account number an acquirer gives a merchant; issuers build a reputation per MID, which is why a new one must be "warmed up" with good traffic. *Token requestor ID (TRID)*: the identifier under which a party asks a network for tokens; tokens belong to the requestor. *Champion and challenger*: sending a small share of traffic to a second provider to compare it with the main one.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Canva's account supports a staged path: one provider; two providers with plain failover; then first-attempt routing rules, which is where both the gain and the complexity are. A routing rule needs evidence per segment (issuer, BIN, country, MID), which a small merchant does not have in enough volume; below some scale a simple rule is the honest design. An external orchestrator moves the single point of failure instead of removing it and adds a hop to a one-second budget. The exit plan (who holds the vault, under whose token requestor ID, and how cards leave) is an architectural decision to make before the second provider, not after.

---

## Key numbers

| Number | Exact definition as published | Source | Date |
| --- | --- | --- | --- |
| 94.9% vs 93% | Stripe's worked example: authorization rate 93,000 / 98,000 versus payment success rate 93,000 / 100,000 | docs.stripe.com/payments/analytics/acceptance | n.d., accessed 2026-11 |
| 15 reattempts in 30 days | Visa limit for category 2 to 4 declines; zero for category 1 | Visa bulletin; Adyen docs | 2020-09-03; n.d. |
| 20 retries in 30 days ⚠ | Same Visa limit as stated by PayPal and TabaPay; conflicts with the row above | paypal.com guidance; TabaPay docs | 2026-05-15; n.d. |
| 35 in 30 days; 10 in 24 hours | Mastercard excessive-attempt thresholds, same card, acceptor and amount | PayPal guidance; Braintree bulletin (35 from 1 Nov 2023) | 2026; 2023 |
| $0.15, $0.30, $0.50 ⚠ | Mastercard excessive retry fee per transaction from Nov 2023, Jan 2024, Jan 2025 (US) | Braintree bulletin | 2023 |
| 8 retries in 2 weeks | Stripe Smart Retries default for new accounts | Stripe docs | n.d., accessed 2026-11 |
| 1 to 48 days | Adyen Auto Rescue `maxDaysToRescue`; one calendar month at account level | Adyen docs | n.d., accessed 2026-11 |
| 3.8% average, up to 7% | "increase their acceptance rate by 3.8% on average, with some seeing up to 7%" with Authorization Boost; metric undefined | Stripe blog | 2025-05-15 |
| up to 3.3% | "lower card processing costs by up to 3.3%", custom interchange pricing | Stripe product page; Sessions 2026 list | n.d.; 2026-04-29 |
| 20% | "recovering 20% of false declines on average" | Stripe product page | n.d., accessed 2026-11 |
| $6 billion | "falsely declined transactions" recovered by Adaptive Acceptance in 2024 | Stripe blog | 2025-02-12 |
| 60%, 70%, 35% | Year-over-year increase in retry success rate; "greater precision"; fewer retry attempts | Stripe blog | 2025-02-12 |
| 59% to 97% | Detection rate for card-testing attacks on large users, after the foundation model | Stripe blog | 2025-05-15 |
| 1–2% and 8% | Enhanced Issuer Network: authorization uplift "on eligible volume", fraud reduction | Stripe newsroom; product page | 2023-02-21; n.d. |
| 0.2% ⚠ | Authorization Boost price per successful online card transaction, custom-pricing accounts (Ireland page) | Stripe product page | n.d., accessed 2026-11 |
| up to 6% | Uplift "payment conversion rate" versus "legacy implementations"; footnoted as the pilot average for merchants using all modules | Adyen press release; product update | 2025-01-09 |
| 86%; 35% | Average reduction in manual risk rules; share of pilot customers with none left | Adyen press release | 2025-01-09 |
| up to 5% | Reduction in "payment cost" for US pilot customers | Adyen press release | 2025-01-09 |
| 60; 20+ | Businesses in the Uplift pilot; merchants in the Intelligent Payment Routing pilot | Adyen press releases | 2025-01-09; 2024-09-09 |
| 26%; 0.22% | Average "cost savings" and authorization-rate uplift "against earlier debit performance", US debit | Adyen press release | 2024-09-09 |
| 1 s; ~600 ms; 20 ms; 100 ms | Adyen transaction SLA; acquirer communication share; model call median; model call p99 | Adyen knowledge hub | 2025-01-17 |
| 2–5 | Model endpoints touched per Adyen transaction | Adyen knowledge hub | 2025-01-17 |
| >2 billion | Tokens in Adyen's vault | Adyen knowledge hub | 2025-01-17 |
| 3 | Processors in Stripe Orchestration's feature table (Adyen, Braintree, Worldpay WPG) ⚠ | Stripe docs | n.d., accessed 2026-11 |
| ~26 | Named destinations on Stripe's Forward allow-list ⚠ | Stripe docs | n.d., accessed 2026-11 |
| 4096 bits | Minimum PGP key length Stripe requires from the receiving processor for a card export | Stripe docs | n.d., accessed 2026-11 |
| 24 hours | Time within which Adyen Multi pay-in funds must be allocated to balance accounts | Adyen docs | n.d., accessed 2026-11 |
| 1 July 2023 | Effective date of the Regulation II clarification covering card-not-present debit | Federal Reserve | 2022-10-03 |
| 6 months; 3+ months; ~30 people; 5 PSPs | Canva: engineering time per new PSP; MID warm-up; payments team including operations; integrated PSPs | Stripe Sessions 2026 transcript | 2026-04 |

## Open questions / not verifiable

1. **The current Visa reattempt limit.** Is it 15 or 20 in 30 days, and does it vary by region? Needs the current Visa Core Rules or a 2025 to 2026 Visa bulletin.
2. **Current Mastercard thresholds and fees** from a Mastercard document, and whether a retry sent through a second acquirer counts against the same limit.
3. **What "acceptance rate" means in Stripe's 3.8% claim**: relative or percentage points, raw or deduplicated, which cohort, measured against what.
4. **How Stripe counts the $6 billion** recovered in 2024, and what share of Adaptive Acceptance retries succeed.
5. **Any authorization-rate result from Stripe's Payments Foundation Model.** Only a fraud result is public.
6. **What Adyen's "payment conversion" denominator is** in the 6% claim, and whether any post-pilot figure exists.
7. **Smart Retries and Auto Rescue recovery rates.** Neither company publishes one in the pages fetched.
8. **False-positive cost of pre-network blocking** (Stripe decline prevention, Adyen ERPS): how many blocked payments would have been approved.
9. **Network-token uplift in isolation**, by region and issuer, from either company or from the networks.
10. **Whether network tokens provisioned by Stripe or Adyen survive an export** to another processor, and under whose token requestor ID they are issued.
11. **When Stripe Orchestration leaves private preview**, its price, and which processors beyond the three in the feature table are supported.
12. **Adyen's export procedure, timeline and fees**, and the list of destinations its Forward API supports.
13. **Stripe first-attempt least-cost debit routing**: whether it exists beyond the documented PINless retry.
14. **Adyen pricing for Uplift modules**, the Real Time Account Updater and network tokenization.
15. **Public engineering accounts from Airbnb, Booking.com, Uber (recent) or Shopify on multi-provider routing.** None verified; the chapter should rely on Canva's 2026 account and say the public record is thin.
16. **Mastercard Automatic Billing Updater and Visa Account Updater details** (real-time versus batch at the network level, coverage by country).

## Source list

**Stripe documentation (n.d., accessed 2026-11)**

- Declines. https://docs.stripe.com/declines.md. Three failure types; blocked-payment outcomes.
- Card declines. https://docs.stripe.com/declines/card.md. Generic declines, network codes, advice codes, eight-retry recommendation, local accounts.
- Acceptance analytics. https://docs.stripe.com/payments/analytics/acceptance.md. Authorization rate, payment success rate, raw and deduplicated rates.
- Payments optimization (Authorization Boost). https://docs.stripe.com/payments/analytics/optimization.md. Feature definitions, attribution and cost-saving methods, disclaimer.
- A/B testing Authorization Boost. https://docs.stripe.com/payments/analytics/optimization/a-b-testing.md. Test design and limits.
- How cards work (automatic card updates). https://docs.stripe.com/payments/cards/overview.md. Card account updater coverage and webhooks.
- Automate payment retries (Smart Retries). https://docs.stripe.com/billing/revenue-recovery/smart-retries.md. Signals, defaults, hard decline codes, direct debit retries.
- Revenue recovery. https://docs.stripe.com/billing/revenue-recovery.md. Feature list.
- Orchestration. https://docs.stripe.com/payments/orchestration.md; rules: .../orchestration/rules.md; routing: .../orchestration/route-payments.md; retries: .../orchestration/retries.md; feature support: .../orchestration/feature-support.md. Preview status, processors, exclusions, rule model, record changes.
- Route off-session payments with Orchestration. https://docs.stripe.com/payments/off-session-payments/orchestration.md. Smart Retries incompatibility; no raw card data.
- Forward card details to third-party API endpoints. https://docs.stripe.com/payments/vault-and-forward.md. Mechanism, limits, destination allow-list.
- Request a payment data export. https://docs.stripe.com/get-started/data-migrations/pan-export.md. Export policy and requirements.

**Stripe product pages, guides, blog and newsroom**

- Authorization Boost product page. Stripe. n.d., accessed 2026-11 (fetched as https://stripe.com/ie/authorization-boost). https://stripe.com/authorization-boost. Bundle contents, 3.8%, 3.3%, 20%, prices, foundation model statement.
- Optimizing authorization rates (guide). Stripe. n.d. (fetched in the Ireland locale). https://stripe.com/guides/optimizing-authorization-rates. ISO 8583, decline reasons, levers, Adaptive Acceptance description, Postmates figure.
- Understanding the benefits of network tokens (guide). Stripe. n.d. https://stripe.com/guides/understanding-benefits-of-network-tokens. Token or PAN choice, latency, coverage.
- AI enhancements to Adaptive Acceptance. Ming Chen, Keshav Manjrekar, Vanya Rybkin, Pierre Garrigues. 2025-02-12. https://stripe.com/blog/ai-enhancements-to-adaptive-acceptance. Model change and results.
- Using AI to optimize payments performance with the Payments Intelligence Suite. John Affaki. 2025-05-15. https://stripe.com/blog/using-ai-optimize-payments-performance-payments-intelligence-suite. Authorization Boost claims; foundation model.
- Stripe accelerates the utility of AI and stablecoins with major launches. Stripe newsroom. 2025-05-07. https://stripe.com/newsroom/news/sessions-2025. Foundation model and Orchestration announcements.
- Top product updates from Sessions 2025. Stripe blog. 2025-05-07. https://stripe.com/blog/top-product-updates-sessions-2025. Authorization Boost and Orchestration previews; Optimized Checkout Suite.
- Everything we announced at Sessions 2026. Stripe blog. 2026-04-29. https://stripe.com/blog/everything-we-announced-at-sessions-2026. PINless debit retries, A/B test preview, unified payouts across processors.
- More PSPs, more problems? When adding multiple processors pays off (talk and transcript). Alex Ginet and Jon Krauss (Stripe), Joshua Barton (Canva). Stripe Sessions 2026. https://stripe.com/sessions/2026/more-psps-more-problems. Trade-offs; Canva's account; 123cards claim.
- Stripe expands network tokens and card account updater to improve conversion. Stripe newsroom. 2023-02-23 (evidence age 3.7 years). https://stripe.com/newsroom/news/network-tokens-card-account-updater. Real-time updater, 40% card replacement, Doist quote.
- Stripe launches Enhanced Issuer Network. Stripe newsroom. 2023-02-21 (evidence age 3.7 years). https://stripe.com/newsroom/news/enhanced-issuer-network. Issuer data sharing and claims.
- Gautam Kedia, post on the payments foundation model, 7 May 2025, read through a mirror. https://threadreaderapp.com/user/thegautam. Engineer's description (secondary copy).

**Adyen documentation (n.d., accessed 2026-11)**

- Adyen Uplift. https://docs.adyen.com/uplift.md. Modules and status.
- Enable Adyen Uplift (partner guide). https://docs.adyen.com/partners/uplift-enablement.md. Feature-level detail, defaults, ERPS.
- Adyen Uplift experiments. https://docs.adyen.com/uplift/uplift-experiments.md. Experiment types.
- Auto Rescue; Auto Rescue for card payments. https://docs.adyen.com/online-payments/auto-rescue.md; .../auto-rescue/cards.md. Rescue window, flags, webhooks, RevenueAccelerate report.
- Account Updater; Real Time Account Updater. https://docs.adyen.com/online-payments/account-updater.md; .../account-updater/real-time-account-updater.md. Modes, schemes, conditions.
- Network tokenization. https://docs.adyen.com/online-payments/network-tokenization.md. Modes, limits, co-badged US debit routing.
- Authentication. https://docs.adyen.com/online-payments/authentication.md. Authentication Engine.
- Refusal reasons. https://docs.adyen.com/development-resources/refusal-reasons.md. Response fields.
- Mapping to Visa system integrity fee categories. https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees.md. Categories, code mapping, 15-in-30 limit.
- Enhanced scheme data. https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data.md. Level 2/3 effect.
- Forward payment details. https://docs.adyen.com/online-payments/tokenization/forward-payment-details.md. Forward API.
- Multi pay-in. https://docs.adyen.com/marketplaces/multi-pay-in.md. Pilot, flow, 24-hour rule.
- External settlement detail report. https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report.md. Adyen as non-acquirer.
- Card application selection. https://docs.adyen.com/point-of-sale/aid-selection-rules.md. In-person least-cost routing and EEA brand choice.
- Import data from another payment provider. https://docs.adyen.com/development-resources/migrating-payment-data.md. Existence of the import process.

**Adyen press, product and knowledge-hub pages**

- Introducing Adyen Uplift. Adyen press release. 2025-01-09. https://www.adyen.com/press-and-media/adyen-uplift-launch. Launch claims and pilot.
- Boost your payment conversion with Adyen Uplift. Adyen product update. 2025-01. https://www.adyen.com/the-latest/boost-your-payment-conversion-with-adyen-uplift. Footnote defining the 6% claim.
- The AI behind Uplift. Andreu Mora, Adyen. 2025-01-17. https://www.adyen.com/knowledge-hub/the-ai-behind-uplift. Engineering account.
- Adyen Uplift; Optimize. Adyen product pages. n.d., accessed 2026-11. https://www.adyen.com/uplift; https://www.adyen.com/uplift/optimize. Current claims and feature names.
- Adyen's Intelligent Payment Routing Achieves 26% Cost Savings. Adyen press release. 2024-09-09. https://www.adyen.com/press-and-media/adyens-intelligent-payment-routing-usdebit. Launch claims.
- Maximize your profit now with Intelligent Payment Routing for US debit cards. Adyen knowledge hub. 2024-09-26. https://www.adyen.com/knowledge-hub/maximize-your-profit-now-with-intelligent-payment-routing-for-us-debit-cards. Positioning against least-cost routing.

**Networks and regulators**

- Updates to Rules for Declined Transaction Resubmission and Use of Authorization Response Codes. Visa. 2020-09-03 (evidence age 6 years). https://usa.visa.com/content/dam/VCOM/global/support-legal/documents/updates-to-rules-for-declined-transaction-resubmission-and-use-of-authorization-response-codes.pdf. Categories and 15-in-30 limit.
- Visa Account Updater overview. Visa Developer. n.d. https://developer.visa.com/capabilities/vau. Service definition.
- Federal Reserve Board finalizes updates to the Board's rule concerning debit card transactions. Federal Reserve. 2022-10-03 (evidence age 4 years). https://www.federalreserve.gov/newsevents/pressreleases/bcreg20221003a.htm. Card-not-present clarification, effective date.
- Regulation II (Debit Card Interchange Fees and Routing). Federal Reserve. n.d. https://www.federalreserve.gov/paymentsystems/regii-about.htm. Rule summary.

**Acquirer and processor summaries of network rules (secondary)**

- How to avoid excessive retries penalties. PayPal (JB Meacham). 2026-05-15. https://www.paypal.com/us/brc/article/avoid-excessive-retries-penalties. Visa 20-in-30 statement, Mastercard thresholds, MAC fee.
- Mastercard network updates, fall 2023 and summer 2024. Braintree (PayPal). 2023; 2024. https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/mastercard-f23; .../2024/mc-su24. Excessive-attempt fee schedule; Authorization Optimizer MAC values.
- Transaction Integrity - Network Fees. TabaPay developer documentation. n.d. https://developers.tabapay.com/docs/network-authorization-best-practices. Visa 20-in-30 statement; Mastercard 35-in-30.

**Orchestrators and merchants**

- Spreedly homepage; Network tokenization documentation. n.d. https://www.spreedly.com/; https://developer.spreedly.com/docs/network-tokenization. Vault positioning; TR-TSP role; Stripe dependency.
- Primer homepage. n.d. https://primer.io/. Vault, fallbacks, workflows.
- Gr4vy homepage. n.d. https://gr4vy.com/. Dedicated instance; connection count.
- Hyperswitch repository. Juspay. Created 2022-10-17. https://github.com/juspay/hyperswitch. Licence and self-description.
- 10 Tips for Building Resilient Payment Systems. Shopify Engineering. 2022-07-28 (evidence age 4 years). https://shopify.engineering/building-resilient-payment-systems. Local acquirers; per-country circuit breakers.
- Engineering Uber's Next-Gen Payments Platform. Uber Engineering. 2018-12-05 (evidence age 8 years). https://www.uber.com/blog/payments-platform/. Processor integrations and integration patterns.
