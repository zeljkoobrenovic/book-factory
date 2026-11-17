# Research brief: The card payment lifecycle and the card networks

Prepared 17 November 2026 for chapter writers of *SETTLED: Architecting Payments and Revenue Infrastructure*. Feeds chapters 01 (journey of a payment), 02 (authorization), 03 (clearing and settlement), 04 (refunds, reversals and disputes), 05 (payment economics), and journeys 42 (card payment) and 45 (dispute). The brief covers the parties, the authorization message path, capture, clearing and settlement, money flowing backward, and who earns what, and for each topic records what Stripe and Adyen have each published. Terminals, local payment methods, tokens, 3-D Secure, fraud scoring, ledgers and platform splits belong to the sibling briefs (`acquiring`, `carddata`, `risk`, `ledger`, `platforms`).

## How to read this brief

Every substantive claim carries one tag:

- **[VERIFIED: url, published YYYY-MM(-DD)]**: the page was fetched in this session (17 November 2026) and the passage supports the claim. Quoted text is quoted exactly. The date is the source's publication date; undated documentation and product pages are marked "n.d., accessed 2026-11".
- **[WIDELY REPORTED: url, YYYY]**: a reputable secondary source (the kind is named: law-firm briefing, trade press, vendor marketing), not a primary document.
- **[ASSUMPTION/JUDGEMENT]**: industry knowledge or the analyst's inference, including every statement about how Stripe, Adyen or a card network works internally beyond what it has published.

**Evidence age.** Stripe and Adyen documentation pages are living documents without a visible publication date. Adyen's markdown pages carry a `last_modified` metadata field, but it is not reliable: some pages show today's timestamp and others show 2019–2023 dates while containing rules dated July 2025 and April 2026. All documentation is therefore tagged "n.d., accessed 2026-11". Sources published before November 2023 are flagged **(evidence age: N years)**.

**The network rulebooks.** The Visa Core Rules and Visa Product and Service Rules are public and the edition dated **24 October 2026** was downloaded and searched in this session; it is the strongest primary source in this brief. The equivalent Mastercard documents were not reachable (see below), so every Mastercard rule here is reported through Stripe's or Adyen's rendering of it, and says so.

**Research limitation.**

- **Mastercard rule documents** (Chargeback Guide, Transaction Processing Rules, Mastercard Rules, Security Rules and Procedures) returned HTTP 403 to both the fetch tool and curl on `mastercard.us`. Mastercard's chargeback cycles, time limits, authorization validity, Excessive Chargeback Program thresholds and Merchant Advice Codes are therefore taken from Stripe and Adyen documentation, not from Mastercard. Writers must not present them as quotations from Mastercard.
- **ISO 8583** itself is a paid standard; `iso.org/standard/79451.html` and the ANSI preview returned 403. The description of the message structure comes from Stripe's own explainer (updated 18 September 2026) and is otherwise ASSUMPTION/JUDGEMENT. The edition year (2023) was seen only in a search-result snippet.
- **Verifi** product pages (`/products/...`) returned 404 and the Verifi home page 403; two older Verifi marketing pages were readable. **Ethoca** redirects to a `mastercard.com` page that returned 403. Pre-dispute products are documented mainly through Stripe's and Adyen's descriptions.
- **Stripe's "June 2025 pricing updates for disputes"** support article needs JavaScript and returned no body; dispute fees come from Stripe's pricing page instead.
- **Stripe's pricing page is geo-localised.** The default URL served Dutch text; the English Netherlands page (`/en-nl/pricing`) and a US-language request to `/us/pricing` were read. Prices differ by country; both are quoted with their country.
- **The Adyen pricing page** renders payment-method names client-side; the Visa row was confirmed on Adyen's Visa payment-method page.
- **The US merchant settlement**: the facts up to 15 July 2026 come from Visa's annual report filed 5 November 2026. A final-approval hearing reportedly scheduled for 16 November 2026 appeared only in search snippets; its outcome was not found. One trade-press article on preliminary approval (americascreditunions.org) and two others (qz.com, a Reuters syndication) returned 403 or empty bodies.
- **Adyen's FY2025 annual report** was not downloaded; full-year figures come from the H2 2025 results press release and the H1 2026 shareholder letter.
- The **Productscape domain model** named in the research brief was not used as a source for any claim here.

**Volatility flags.** ⚠ marks claims likely to change within 12 months: provider pricing and fees, features in private preview, monitoring-programme thresholds, authorization windows, the Regulation II litigation, the US merchant settlement, and anything in the Visa rules marked "Effective" with a 2026–2027 date.

---

## PART 1: The parties and the four-party model (chapter 01)

### 1.1 The four-party model in the networks' own words

- Visa describes itself as providing "transaction processing services (primarily authorization, clearing and settlement) among consumers, issuing and acquiring financial institutions and sellers in a structure we call the “four-party” model" [VERIFIED: https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm, published 2026-11-05].
- Visa's walkthrough of one payment: "The seller presents the transaction data to an acquirer, usually a bank or third-party processing firm that supports acceptance of Visa cards or payment products, for verification and processing. Through VisaNet, the acquirer presents the transaction data to Visa, which in turn sends the transaction data to the issuer to check the account holder’s account balance or credit line for authorization. After the transaction is authorized, the issuer posts the transaction to the consumer’s account and effectively pays the acquirer an amount equal to the value of the transaction, minus the interchange reimbursement fee (IRF). The acquirer pays the amount of the purchase, minus the merchant discount rate (MDR), to the seller." [VERIFIED: Visa 10-K, 2026-11-05].
- "Visa is not a financial institution. We do not issue cards, extend credit or set rates and fees for account holders of Visa card products nor do we earn revenue from or bear credit risk with respect to any of these activities." [VERIFIED: Visa 10-K, 2026-11-05].
- Mastercard names the same four participants: "account holder (a person or entity who holds a card or uses another device enabled for payment), issuer (the account holder’s financial institution), merchant and acquirer (the merchant’s financial institution)", and says "We do not issue cards, extend credit, determine or receive revenue from interest rates or other fees charged to account holders by issuers, nor do we establish the rates charged by acquirers in connection with merchants’ acceptance of our products." [VERIFIED: https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm, published 2026-02-11].
- EU law defines the two models: "‘three party payment card schemes’ (cardholder — acquiring and issuing scheme — merchant) and ‘four party payment card schemes’ (cardholder — issuing bank — acquiring bank — merchant)". A three-party scheme that licenses other providers to issue or acquire "is considered to be a four party payment card scheme" [VERIFIED: http://publications.europa.eu/resource/celex/32015R0751, published 2015-05-19] **(evidence age: 11 years; the regulation is in force and Visa's November 2026 annual report still cites it as current)**.
- The Visa rulebook's definition of an acquirer already includes the facilitator model: "A Member that signs a Merchant or Payment Facilitator, provides a Cash Disbursement to a Cardholder, or loads funds to a Prepaid Card, and directly or indirectly enters a Transaction into Interchange." [VERIFIED: https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf, published 2026-10-24].
- Scale, for orientation: "During fiscal 2026, Visa’s total payments and cash volume was $18 trillion, and we had over 5 billion payment credentials", with "over 14,000 financial institutions" as clients and "more than 400 million" seller locations [VERIFIED: Visa 10-K, 2026-11-05].

| Party | What it does in one card payment | Holds money? | Carries which risk? |
| --- | --- | --- | --- |
| Cardholder | Presents the card or credential | Their account | Can dispute for months |
| Issuer | Decides the authorization, posts the transaction, pays the acquirer net of interchange | Yes (cardholder funds or credit line) | Cardholder credit risk; fraud where liability sits with the issuer |
| Network (Visa, Mastercard) | Routes authorization, runs clearing, calculates net settlement, sets rules and default interchange | No (not a bank), but guarantees settlement between members | Settlement risk between members |
| Acquirer | Contracts the merchant or payment facilitator, submits transactions, receives settlement, pays the merchant | Yes | Merchant credit risk: chargebacks the merchant cannot pay |
| Processor / gateway | Technical connection for an issuer or acquirer; a gateway only carries messages | No | Operational |
| PSP / payment facilitator | Packages gateway, acquiring (own licence or a partner's), risk and payouts; a facilitator signs sub-merchants under its own acquiring relationship | Usually yes, between settlement and payout | Sub-merchant losses |
| Merchant / platform | Sells; on a platform the sale may belong to the platform or to the seller | After payout | Refunds, chargebacks, fees |

[ASSUMPTION/JUDGEMENT] The table is the analyst's synthesis of the definitions above and standard industry vocabulary; the "holds money" and "risk" columns are generalisations that contracts and local law can change. Whether Stripe or Adyen acts as acquirer, processor or facilitator in a given country is a licensing question for the `acquiring` and `companies` briefs.

### 1.2 Messages versus money, and the timeline

- Authorization, clearing and settlement are three distinct network services. Mastercard: "we enable the routing of a transaction to the issuer for its approval, facilitate the exchange of financial transaction information between issuer and acquirer after a successfully conducted transaction, and settle the transaction by facilitating the exchange of funds between parties via settlement banks chosen by us and our customers." [VERIFIED: Mastercard 10-K, 2026-02-11].
- The dispute window outlives everything else: Adyen states "In general, a cardholder has a maximum of 120 calendar days from the transaction date to dispute a transaction" and "In some cases for Visa and Mastercard, the cardholder has a maximum of 540 calendar days" [VERIFIED: https://docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes.md, n.d., accessed 2026-11].

| Step | Typical time after "pay" | What moves | Who has promised what |
| --- | --- | --- | --- |
| Authorization | 1–3 seconds | A message; a hold on the cardholder's account | Issuer: "I will honour a claim for this amount if it arrives in time" |
| Capture | Seconds to days (up to the validity window) | An instruction inside the provider | Merchant: "I am claiming the money" |
| Clearing (presentment) | Same day to next day | A clearing record through the network | Acquirer: "this is the final amount and data" |
| Settlement | Next business day or later | Net funds between issuer, network settlement bank and acquirer | Network: guarantees members pay each other |
| Payout / funding | T+2 to T+7 depending on provider and country | Bank transfer to the merchant | Provider: "your balance is available" |
| Dispute window | Up to 120 days, in some cases far longer | A chargeback pulls funds back | Nothing is final until this closes |

[ASSUMPTION/JUDGEMENT] The time column combines the documented windows in Parts 2–4 with industry practice; exact timings depend on network, country and provider.

**Stripe vs Adyen.**

| Aspect | Stripe (documented) | Adyen (documented) | Difference the evidence supports |
| --- | --- | --- | --- |
| How the provider describes the parties | Glossary tooltips define card network ("It might be an intermediary in front of an issuing bank as with Visa or Mastercard, or a standalone entity as with American Express") and issuer [VERIFIED: https://docs.stripe.com/disputes/how-disputes-work.md, n.d., accessed 2026-11] | Uses "scheme", "issuer", "acquirer" throughout; exposes the "raw acquirer response" from "a card scheme or issuer" [VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses.md, n.d., accessed 2026-11] | Vocabulary only: Stripe says "network" and "business", Adyen says "scheme", "merchant account" and "shopper" |
| A public end-to-end description of its own role per region | Nothing found in the pages fetched for this brief | Nothing found in the pages fetched for this brief | Not public here; see `companies` and `acquiring` briefs |

**For readers new to payments.** *Issuer*: the bank that gave the customer the card and decides whether to approve. *Acquirer*: the bank or licensed institution that signs the merchant and collects the money for it. *Network (scheme)*: Visa or Mastercard, which carries the messages between the two, sets the rules and nets what they owe each other, without holding either side's customer money. *Three-party network*: one company (classically American Express) is both issuer and acquirer.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Every later chapter inherits one fact from this model: the party that answers the API call (the provider) is not the party that decides (the issuer), moves the money (the network's settlement process) or can take it back (the cardholder through the issuer). A provider's system is therefore built around records of other parties' promises, each with its own clock.

---

## PART 2: Authorization (chapter 02)

### 2.1 The message path and ISO 8583

- Stripe's explainer: ISO 8583 "lets a card issued by one bank be authorised at a terminal operated by a different acquirer. It defines the structure of messages between acquirers and card issuers during a transaction", was "Published in 1987", and "Visa, Mastercard, and many domestic card networks built their authorisation systems on some variant of it." [VERIFIED: https://stripe.com/en-nl/resources/more/iso-8583, published 2026-09-18 ("Last updated 18 September 2026")].
- Structure: "Each message is built from an MTI, a bitmap, and data elements". "MTI: A four-digit number that identifies the message’s version of ISO 8583 (e.g., 1987, 1993, or 2003), as well as its class, function, and origin." "Bitmap: A field or sub-field indicating whether there are other data elements or data element sub-fields elsewhere in the message. A secondary bitmap might also exist." "Data elements: The actual transaction data, such as amount, date, time, and country codes." [VERIFIED: same].
- The limitation that matters to integrators: "The ISO 8583 standard isn’t self-describing, which means a message doesn’t include field names or explanations, so a system needs a matching specification document to interpret it correctly." "Visa, Mastercard, and various domestic networks each maintain their own variant of ISO 8583, with different field definitions and usage rules. The result is that two systems claiming compliance can still fail to communicate." [VERIFIED: same].
- ISO 20022 is not the card-authorization format: "ISO 8583 still dominates card authorisation, even as ISO 20022 gains adoption on other payment systems"; ISO 20022 is "increasingly used in cross-border electronic transfers, Automated Clearing House (ACH), and payment systems such as Fedwire and Single Euro Payments Area (SEPA) Instant Credit Transfer" [VERIFIED: same].
- The conventional message pairs (0100 authorization request / 0110 response, 0200/0210 financial request, 0400/0410 reversal, 0800 network management) and the best-known data elements (2 primary account number, 3 processing code, 4 amount, 7 transmission date and time, 11 system trace audit number, 22 point-of-service entry mode, 37 retrieval reference number, 38 approval code, 39 response code, 41/42 terminal and merchant identifiers, 49 currency) are industry knowledge and were not verified against the standard in this session [ASSUMPTION/JUDGEMENT]. ISO lists the current edition as ISO 8583:2023 [WIDELY REPORTED: https://www.iso.org/standard/79451.html (page blocked; edition seen in a search snippet), 2023].
- The Visa rulebook confirms two of these fields indirectly: a stored-credential transaction must "Use POS Entry Mode code 10", and declines are identified by two-character response codes such as "51 (Not sufficient funds)" [VERIFIED: Visa Core Rules, 2026-10-24].

**Stripe vs Adyen.** Neither exposes ISO 8583 messages to merchants. Stripe has published the explainer above and says "Businesses that use a payments provider such as Stripe don’t have to build or manage these messages themselves." [VERIFIED: https://stripe.com/en-nl/resources/more/iso-8583, 2026-09-18]. Adyen has published nothing found on ISO 8583 itself (searched: Adyen documentation index `docs.adyen.com/llms.txt` for "8583"; not present in the pages fetched), but exposes the network's response as `refusalReasonRaw` (2.2). How either company's internal systems translate an API call into a network message is not public [ASSUMPTION/JUDGEMENT].

### 2.2 The issuer's decision: response codes, decline codes and retry rules

**What the networks say.**

- Visa requires that "An Issuer that declines an Authorization Request or an Account Verification request must send to VisaNet the Decline Response code that most accurately reflects the reason for the decline" [VERIFIED: Visa Core Rules §7.3.6.3, 2026-10-24].
- Visa sorts decline codes into categories with retry limits (Table 7-2). **Category 1, "Issuer will never approve"**: 04, 07, 12, 14, 15, 41, 43, 46, 57, R0, R1, R3; "a Merchant must never resubmit an Authorization Request or Account Verification for the same Payment Credential". **Category 2, "Issuer cannot approve at this time"**: 03, 19, 39, 51, 52, 53, 59, 61, 62, 65, 75, 78, 86, 91, 93, 96 and others; "Reattempt permitted (up to 20 attempts in 30 days)". **Category 3, "Data quality – Revalidate payment"** information also permits reattempts [VERIFIED: Visa Core Rules Table 7-2, 2026-10-24] ⚠.
- ⚠ **Discrepancy to flag.** Adyen's page on Visa system integrity fees says of categories 2 and 3 "You can retry the transaction up to 15 times in a 30-day period", and adds a Category 4 for generic codes: "The most frequent refusal reason, **05: Do not honor**, falls into this category." [VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees.md, n.d., accessed 2026-11]. The Visa rulebook dated 24 October 2026 says 20. Writers should cite the Visa figure and note that provider documentation may lag.
- Visa charges for breaking these rules: "Visa charges system integrity fees. These fees are related to excessive retries of failed transactions, and excessive numbers of transactions that failed due to incorrect payment details." [VERIFIED: Adyen, same page].
- Mastercard returns a second code, the Merchant Advice Code (MAC), "for both approved and refused Mastercard payments"; "If the payment failed, the MAC gives guidance on if and when you can retry the payment." Examples: "03 : Do not try again", "21 : Payment Cancellation", "24 : Retry after 1 hour" through "30 : Retry after 10 days"; "Not all Mastercard issuers return the MAC." [VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses.md, n.d., accessed 2026-11] (Adyen's rendering of Mastercard's specification).

**Stripe vs Adyen: how a decline reaches the merchant.**

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Normalised reason | `decline_code` on the payment error, e.g. `insufficient_funds`, `do_not_honor`, `generic_decline`, `issuer_not_available`, `authentication_required`; "Stripe’s decline codes expand on issuer decline codes by going into more detail" [VERIFIED: https://docs.stripe.com/declines/codes.md, n.d., accessed 2026-11] | `resultCode` (**Refused**, **Error** or **Cancelled**) plus `refusalReason` and numeric `refusalReasonCode`, e.g. 2 Refused, 5 Blocked Card, 9 Issuer Unavailable, 12 Not enough balance, 27 Declined Non Generic, 38 Authentication required [VERIFIED: https://docs.adyen.com/development-resources/refusal-reasons.md, n.d., accessed 2026-11] |
| Raw network code | `network_decline_code` and `network_advice_code` on the charge outcome: "The card network provides this 2-4 digit code"; "The meaning of a code differs based on the card network"; null when no code was received [VERIFIED: https://docs.stripe.com/declines/card.md, n.d., accessed 2026-11] | `refusalReasonRaw`, e.g. "05: Do not honor", "51: Insufficient funds/over credit limit / Not sufficient funds"; must be enabled in the Customer Area; "card schemes and issuers sometimes change the text without notice" [VERIFIED: https://docs.adyen.com/development-resources/raw-acquirer-responses.md, n.d., accessed 2026-11] |
| Retry guidance | `advice_code`: `do_not_try_again`, `try_again_later`, `confirm_card_data`; "Stripe recommends a maximum of eight retries for charges that permit retries" [VERIFIED: https://docs.stripe.com/declines/card.md] | `additionalData.merchantAdviceCode` for Mastercard; a mapping of raw responses to Visa fee categories [VERIFIED: Adyen raw responses and integrity-fee pages] |
| Provider blocks a retry to save network penalties | "Excessive retry prevention: Stripe blocks a payment that would have incurred network retry penalties and likely failed"; offered as a cost optimisation "for businesses on IC+ pricing" [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md, n.d., accessed 2026-11] | Refusal reason 46, "Transaction blocked by Adyen to prevent excessive retry fees": "Adyen's excessive retry prevention service blocked the transaction to make sure that you are not charged penalty fees." [VERIFIED: Adyen refusal reasons] |
| Payment never sent to the issuer | Radar block: `network_status: "not_sent_to_network"`; "When Stripe blocks a payment, it doesn’t obtain authorization from the card issuer." [VERIFIED: https://docs.stripe.com/declines.md, n.d., accessed 2026-11] | Refusal reason 20 "FRAUD": "The pre-authorization risk checks resulted in a fraud score of 100 or more." [VERIFIED: Adyen refusal reasons] |
| What must not be shown to the customer | For `lost_card`, `stolen_card`, `fraudulent`: "present it in the same manner as `generic_decline`" [VERIFIED: Stripe decline codes] | Nothing equivalent found on the refusal-reasons page |

- Most declines carry no usable reason: "Card issuers categorize most declines as generic (generic_decline), making the exact decline reason unclear." [VERIFIED: https://docs.stripe.com/declines/card.md]. Adyen's code 27 exists for the same reason: it "maps all those response codes that cannot be reliably mapped" [VERIFIED: Adyen refusal reasons].
- "Soft decline" and "hard decline" are not network terms. The nearest official vocabulary is Visa's Category 1 (never retry) versus Categories 2–3 (retry within limits), Mastercard's MAC, and the authentication-required decline (Stripe `authentication_required`: "in most cases a soft decline from an issuer triggers an authentication flow"; Adyen 38: "Retry with 3D Secure") [VERIFIED: Stripe decline codes; Adyen refusal reasons].

### 2.3 Holds and authorization validity windows

**Visa's rule (primary).** Table 5-11, "General Approval Response Validity Timeframes", gives the maximum time an acquirer has to process a completed transaction after a valid authorization [VERIFIED: Visa Core Rules §5.7.3.5, 2026-10-24] ⚠:

| Transaction type | Maximum processing timeframe |
| --- | --- |
| Cardholder-initiated, card-absent, with an extended Authorization indicator | 30 calendar days |
| Cardholder-initiated, card-absent | 10 calendar days |
| Estimated Authorization at cruise line, lodging and vehicle rental merchants | 30 calendar days |
| Estimated Authorization at other listed rental merchants | 10 calendar days |
| All other card-present transactions | 5 calendar days |
| All merchant-initiated transactions (instalment, recurring, advance payment, unscheduled credential-on-file) | 5 calendar days |

Country exceptions include Japan ("All Domestic Transactions: 30 calendar days") and India; at an automated fuel dispenser "a Completion Message or a Reversal must be sent within 2 hours"; and "An Incremental Authorization Request does not extend the processing timeframes" [VERIFIED: same].

**Stripe vs Adyen: documented windows.**

| Network and case | Stripe | Adyen |
| --- | --- | --- |
| Visa, card-not-present, customer-initiated | **7 days** | **10 days**; 30 days with Visa "Extended-Auth", which "is currently available only in pilot" |
| Visa, merchant-initiated | 5 days; "The exact authorization window is 4 days and 18 hours, to allow time for clearing processes." | 5 days |
| Visa, card-present | 5 days (4 days 18 hours) | 5 days (POS) |
| Mastercard | 7 days (CIT and MIT); 2 days card-present | 7 days for a final authorization, 30 days for a pre-authorization |
| American Express | 7 days; 2 days card-present | 7 days |
| Discover | 7 days; 2 days card-present | 10 days; 30 for car rental and lodging |
| Cartes Bancaires | not listed on the page | 12 days |
| Provider's own ceiling | `capture_before` on the charge "indicates when the authorization expires"; on expiry "the funds are released and the payment status changes to `canceled`" | "Adyen expires (pre-)authorization requests automatically after 28 days from the day the payment is authorized"; the default can be changed by Support |
| Extended holds | "Extended authorizations", up to 30 days, "to users on IC+ pricing"; for Visa in other merchant categories "Stripe charges an additional 0.08% fee per transaction"; Visa's extended window is "29 days and 18 hours" | Pre-authorization (`additionalData.authorisationType: PreAuth`) with scheme-specific validity; Visa Extended-Auth pilot |

Sources: [VERIFIED: https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md and https://docs.stripe.com/payments/extended-authorization.md?platform=web&ui=elements, n.d., accessed 2026-11]; [VERIFIED: https://docs.adyen.com/online-payments/adjust-authorisation.md, n.d., accessed 2026-11] ⚠.

- **The difference the evidence supports**: Stripe documents a 7-day window for Visa customer-initiated online payments where Visa's rule and Adyen's page say 10. Stripe's page does not explain the gap; that Stripe applies a deliberately conservative uniform window is the analyst's inference [ASSUMPTION/JUDGEMENT].
- Stripe decides which window applies from network signals, not from the API flag alone: "Stripe and the card network classify transactions as MIT or CIT based on signals of cardholder participation, not solely on API parameters like off_session. For example, a payment with `off_session: true` might still be classified as a CIT if a CVC is present" [VERIFIED: Stripe hold page].
- Adyen will let a merchant capture after the network's window has passed, and names the cost: late capture "increases the risk of" a failed capture, "Increased interchange fees", "Card scheme transaction fees" and "A cardholder-initiated chargeback for 'No Authorization' or 'Late Presentment' reasons" [VERIFIED: Adyen adjust-authorisation page]. The matching Visa dispute condition is 11.3, "No Authorization/Late Presentment" [VERIFIED: Visa Core Rules, 2026-10-24].
- Stripe has a private-preview backstop: `capture_method=automatic_delayed`, under which "Stripe captures your card payment before the authorization expires, triggering the capture about 6 hours before the expiration time" [VERIFIED: Stripe hold page] ⚠ (private preview).
- Stripe notes a customer-facing consequence of holds: "Card statements from some issuers and interfaces from payment methods don’t always distinguish between authorizations and captured (settled) payments, which can sometimes confuse customers." [VERIFIED: Stripe hold page].

### 2.4 Estimated, incremental, partial and zero-value authorizations

- Visa definitions: an **Estimated Authorization Request** is "for the amount that a Merchant expects a Cardholder to spend in an individual Transaction and that is submitted before the final Transaction amount is known"; an **Incremental Authorization Request** "Follows an approved Estimated Authorization Request" and "Is for an additional amount"; **Account Verification** is "A message sent by an Acquirer to the Issuer, using a currency unit of zero, for confirmation that a Transaction can be completed using the Card"; the **Partial Authorization Service** has merchants "send a Partial Authorization indicator in all Authorization messages" [VERIFIED: Visa Core Rules glossary, 2026-10-24].
- A new Visa rule dated in the current edition: "Effective 24 October 2026 An Issuer must not use Reason Code 51 (Not sufficient funds) in response to an Account Verification" [VERIFIED: Visa Core Rules Table 7-2, 2026-10-24] ⚠.

| Feature | Stripe | Adyen |
| --- | --- | --- |
| Incremental authorization | "Increase an existing authorization on a confirmed PaymentIntent before you capture it"; "a maximum of 10 incremental authorization attempts per PaymentIntent"; each increment capped at "500 USD (or local equivalent) over, or 500% over the previously authorized amount (whichever is higher)"; does not extend validity; an "IC+ feature" [VERIFIED: https://docs.stripe.com/payments/incremental-authorization.md?platform=web&ui=elements, n.d., accessed 2026-11] | "Authorization adjustment": increase or decrease a pre-authorized amount; eligibility "is determined by your Merchant Category Code (MCC)"; asynchronous (result by webhook) or synchronous (an `adjustAuthorisationData` blob passed from request to request); "Final authorizations" cannot be adjusted [VERIFIED: Adyen adjust-authorisation page] |
| Partial authorization | `request_partial_authorization: if_available`; charge shows `amount_requested`, `amount_authorized` and a status of `partially_authorized`, `fully_authorized`, `declined` or `not_requested`; online card payments only; "IC+ feature"; "as of May 2024, American Express restricts usage of the feature to only debit and prepaid ... while Visa requires you to use the feature across card types" [VERIFIED: https://docs.stripe.com/payments/partial-authorization.md, n.d., accessed 2026-11] | "allows an issuing bank to return an authorization for the available amount when the requested amount is higher than the shopper's balance"; Visa and Mastercard only; not available in the Sessions flow; enabled by Support [VERIFIED: https://docs.adyen.com/online-payments/partial-authorizations.md, n.d., accessed 2026-11] |
| Zero-value authorization | Not described as such on the pages fetched; saving a card without charging uses a SetupIntent [VERIFIED: https://docs.stripe.com/payments/setup-intents.md, n.d., accessed 2026-11]. Whether a SetupIntent sends a zero-amount account verification is not stated on that page [ASSUMPTION/JUDGEMENT] | Explicit: "set the `amount.value` to **0**"; "We recommend that you store payment details by making a zero-auth transaction, because a successful authorization indicates that the payment details were validated by the card scheme." [VERIFIED: https://docs.adyen.com/online-payments/tokenization/create-tokens.md, n.d., accessed 2026-11] |
| Capturing more than authorized | "Overcapture", limited by network and merchant category, e.g. Visa "+20%" for restaurants globally and "+15%" for other categories; an "IC+ feature" [VERIFIED: https://docs.stripe.com/payments/overcapture.md?platform=web&ui=elements, n.d., accessed 2026-11] | Not found as a separate feature in the pages fetched; the documented route is pre-authorization plus adjustment |

- **A commercial pattern worth stating in chapter 05**: on Stripe, extended authorization, incremental authorization, multicapture, overcapture and partial authorization are each labelled an "IC+ feature", available to "users on IC+ pricing"; users "on blended Stripe pricing" must contact support [VERIFIED: the five Stripe pages above]. Adyen gates the equivalents by Support enablement and merchant category, with no pricing-plan condition on the pages fetched [VERIFIED: Adyen capture, adjust and partial-authorization pages].

### 2.5 Reversals and cancels

- Visa: an **Authorization Reversal** is "A V.I.P. System message that cancels an Approval Response." A merchant must submit one "Within 24 hours of Transaction completion" for the difference when the final amount is less than the authorized amounts, and within 24 hours when a transaction is not completed [VERIFIED: Visa Core Rules glossary and Table 5-13, 2026-10-24].
- Stripe: cancelling an uncaptured PaymentIntent releases the hold "at no cost"; a partial capture "automatically releases the remaining amount" [VERIFIED: https://docs.stripe.com/refunds.md and the hold page, n.d., accessed 2026-11].
- Adyen: a cancel applies before capture (CANCELLATION webhook); a **reversal** is for uncertainty: "If you are not sure if a payment has been captured, you can use a reversal to return the funds to the shopper." It "cancels" an uncaptured payment and "refunds" a captured one, and cannot be used after multiple partial captures [VERIFIED: https://docs.adyen.com/online-payments/reversal.md and https://docs.adyen.com/online-payments/cancel.md, n.d., accessed 2026-11].
- Adyen lets a merchant cancel by the merchant's own payment reference instead of Adyen's PSP reference, but only briefly: "You can do this up to 24 hours after authorization." [VERIFIED: Adyen cancel page]. This is the documented answer to the timeout case where the merchant never received a PSP reference [ASSUMPTION/JUDGEMENT on the purpose].
- Stripe has no operation named "reversal" for merchants on the pages fetched; Stripe uses the word for a refund issued so soon that "the original charge drops off the customer’s statement" (4.1) [VERIFIED: Stripe refunds page].

### 2.6 Stand-in processing

- Visa's definition: **Stand-In Processing (STIP)** is "The component (including Visa Smarter Stand-In Processing) that provides Authorization services on behalf of an Issuer when the Issuer, its VisaNet Processor, or a Visa Scheme Processor is unavailable, when Issuer responses exceed the maximum response time, or when the Issuer has instructed Visa to process a Transaction on behalf of the Issuer." [VERIFIED: Visa Core Rules glossary, 2026-10-24].
- Stripe's table of Visa network codes shows where stand-in ends: code 91 is "Issuer or switch inoperative and STIP not applicable or not available for this transaction; time-out when no stand-in" [VERIFIED: https://docs.stripe.com/declines/network-codes.md, n.d., accessed 2026-11].
- What the merchant sees when there is no stand-in: Stripe `issuer_not_available` ("The card issuer couldn’t be reached, so the payment couldn’t be authorized."); Adyen refusal reason 9 "Issuer Unavailable" ("It is not possible to contact the shopper's bank to authorize the transaction.") [VERIFIED: Stripe decline codes; Adyen refusal reasons].
- **Stripe vs Adyen**: neither documents, on the pages fetched, a provider-side stand-in for online payments, or whether an approval came from the issuer or from the network standing in. (Offline and store-and-forward behaviour on terminals belongs to the `acquiring` brief.) Mastercard's stand-in service was not verified (rule documents blocked).

### 2.7 Customer-initiated and merchant-initiated transactions, stored credentials

**Visa's framework (primary).**

- A **Stored Credential** is "Information (including, but not limited to, a Payment Credential) that is stored by any of the following: A Merchant or its agent, a Payment Facilitator, or a Digital Wallet Operator to process future Transactions"; the current edition adds "An Agentic Payment Provider to initiate future Transactions" and, "Effective 24 April 2027", a biometric solution provider [VERIFIED: Visa Core Rules glossary, 2026-10-24] ⚠.
- Before storing: "After a Cardholder agreement has been completed in writing, and before the first Transaction occurs, a Merchant must either: Submit an Authorization Request for the Transaction amount" or "If payment is not required, submit an Account Verification"; "If the initial Authorization Request or Account Verification is not approved, the Merchant must not store the credential." [VERIFIED: Visa Core Rules Table 5-21, 2026-10-24].
- Using it: "A Transaction with a Stored Credential must" use "POS Entry Mode code 10" and, for recurring, instalment or unscheduled credential-on-file transactions, "the appropriate indicator in the POS environment field" [VERIFIED: same].
- When a merchant-initiated authorization is declined, "the Merchant must notify the Cardholder in writing and allow the Cardholder at least 7 calendar days to pay by other means." [VERIFIED: same].
- Definitions: a **Recurring Transaction** is one "in a series of Transactions that use a Stored Credential and that are processed at fixed, regular intervals (not to exceed one year between Transactions)"; an **Unscheduled Credential-on-File Transaction** uses "a Stored Credential for a fixed or variable amount that does not occur on a scheduled or regularly occurring Transaction Date" [VERIFIED: Visa Core Rules glossary, 2026-10-24].
- Mastercard's equivalent framework was not verified from Mastercard (documents blocked). Visa's original 2017 stored-credential framework bulletin was not fetched; the rule text above is the current codification.

**Stripe vs Adyen.**

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| How the merchant declares it | `off_session` on the PaymentIntent and `usage` on the SetupIntent (`off_session` default, or `on_session`) [VERIFIED: https://docs.stripe.com/payments/setup-intents.md] | `shopperInteraction` (**Ecommerce**, **ContAuth**) plus `recurringProcessingModel` (**CardOnFile**, **Subscription**, **UnscheduledCardOnFile**); Adyen's own table treats "ContAuth + Subscription / UnscheduledCardOnFile" as merchant-initiated and "Ecommerce / ContAuth + CardOnFile" as cardholder-initiated [VERIFIED: https://docs.adyen.com/online-payments/tokenization/make-token-payments.md and the adjust-authorisation page, n.d., accessed 2026-11] |
| Who makes the final classification | "Stripe and the card network classify transactions as MIT or CIT based on signals of cardholder participation, not solely on API parameters" [VERIFIED: Stripe hold page] | The merchant's fields, as documented; nothing found saying Adyen reclassifies |
| Definition | "An MIT is a transaction that you initiate without direct participation of your customer, based on a prior agreement with that customer authorizing you to store and use their credentials." [VERIFIED: https://docs.stripe.com/payments/cits-and-mits.md, n.d., accessed 2026-11] | "Subscriptions: recurring transactions you initiate at regular intervals for a product or a service." [VERIFIED: https://docs.adyen.com/online-payments/tokenization.md, n.d., accessed 2026-11] |
| Agreement content | Terms must cover the customer's agreement, "anticipated timing and frequency of payments", how the amount is determined, and the cancellation policy; "Keep a record of each customer’s agreement" [VERIFIED: Stripe CIT/MIT page] | Not on the pages fetched |
| A lifecycle edge case | When the account updater changes a card's brand, "you can’t charge it for any MITs until you get a new cardholder agreement" [VERIFIED: Stripe CIT/MIT page] | Refusal reasons 26 "Revocation Of Auth" ("the shopper requested to stop a subscription") and 50 "Token Revoked" [VERIFIED: Adyen refusal reasons] |

**For readers new to payments.** *Authorization*: the issuer's real-time answer that it will honour a charge of this amount, usually with a hold on the customer's available funds. *Hold*: the reduction of the customer's spendable balance that lasts until capture, reversal or expiry. *Response code*: the two-character reason an issuer returns; providers translate it into their own decline codes. *CIT / MIT*: whether the customer is present in the flow (customer-initiated) or the merchant is charging a stored card under a prior agreement (merchant-initiated); the label changes the validity window, the authentication rules and the dispute rights.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. (1) An authorization is a perishable asset with an expiry that depends on network, CIT/MIT classification, channel and merchant category; store the provider's expiry (`capture_before` on Stripe) with the order, do not compute it. (2) Decline handling needs three inputs kept separately: the provider's normalised reason, the raw network code and the network's retry advice; a retry scheduler that ignores the third generates fees. (3) The unknown-outcome case (a timeout with no reference) needs an idempotent lookup or a cancel-by-own-reference path before any retry. (4) The two providers put the CIT/MIT decision in different places: Stripe infers and may override, Adyen takes the merchant's declaration; a multi-provider integration needs one internal vocabulary mapped to both.

---

## PART 3: Capture, clearing and settlement (chapter 03)

### 3.1 Capture models

| Model | Stripe | Adyen |
| --- | --- | --- |
| Default | Automatic capture unless `capture_method: manual` is set (per PaymentIntent, per Checkout Session or per payment-method type) [VERIFIED: Stripe hold page] | "By default, payments are captured automatically without a delay, immediately after authorization of the payment request." [VERIFIED: https://docs.adyen.com/online-payments/capture.md, n.d., accessed 2026-11] |
| Delayed automatic | Private preview `automatic_delayed` with `capture_by` (`auth_expiry`, `end_of_day`, `target_delay`) [VERIFIED: Stripe hold page] ⚠ | Capture delay per merchant account: "immediate" or "[N] days ... (between 1 and 7)"; per-payment `captureDelayHours` |
| Manual | PaymentIntent moves to `requires_capture`; capture call takes `amount_to_capture` | "you must send a capture request after the payment is authorized"; "Manual capture lets you settle funds on fulfillment, when an order is shipped." The API setting "overrides the setting in the Customer Area" |
| Partial | "A partial capture automatically releases the remaining amount." | "Any unclaimed amount that is left over after partially capturing a payment is automatically cancelled." |
| Multiple | "Multicapture": "Stripe allows up to 50 non-final captures for a single PaymentIntent"; `final_capture=false` keeps the remainder authorized; an "IC+ feature" [VERIFIED: https://docs.stripe.com/payments/multicapture.md?platform=web&ui=elements, n.d., accessed 2026-11] | "Multiple partial captures": "The unclaimed amount after an initial partial capture is not automatically cancelled"; enabled by Support; "The maximum allowable partial captures against a single pre-authorization is determined by the issuer." |
| Capture result | Synchronous status change plus events; `payment_intent.amount_capturable_updated` "on every capture" | Asynchronous: CAPTURE and CAPTURE_FAILED webhooks; "A payment that is automatically captured does *not* trigger a separate CAPTURE webhook." |
| Authorization and capture as one step | Automatic capture | "Direct capture (**SALE**)": "The payment is captured immediately when it is authorized"; "Separate capture (**AUTH**)" otherwise; method-dependent |

Sources: Stripe hold and multicapture pages; [VERIFIED: https://docs.adyen.com/online-payments/capture.md and adjust-authorisation page, n.d., accessed 2026-11].

- **The difference the evidence supports**: on Adyen a capture can fail after the API accepted it and the merchant learns by webhook (CAPTURE_FAILED); Stripe's pages present capture as a call whose result is the object's new state. Whether Stripe's capture can also fail later at the network is not stated on the pages fetched [ASSUMPTION/JUDGEMENT].

### 3.2 Dual-message and single-message systems, clearing and presentment

- The Federal Reserve defines the two families. **Dual-message network**: "A payment card network that typically uses separate messages to authorize and clear a transaction. These networks have traditionally processed signature-authenticated transactions". **Single-message network**: "A payment card network that typically uses a single message to authorize and clear a transaction. These networks normally process PIN-authenticated transactions, although some transactions, such as small-value purchases, may not require any authentication (PIN-less)". Either kind may sometimes use the other pattern [VERIFIED: https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm, published 2025-12-19 ("Last Update")].
- Visa's term for the single-message case: an **Online Financial Transaction** is "A Transaction that is authorized, cleared, and settled in a single online financial message." In the US, "ATM Transactions and PIN-authenticated Visa Debit Transactions must be processed as Full Service Online Financial Transactions through the V.I.P. System." [VERIFIED: Visa Core Rules glossary and Table 5-11 note, 2026-10-24].
- Visa's definitions of the batch side: **Clearing** is "A processing service for the validation and valuation of financial and non-financial records exchanged between Visa and Members." A **Presentment** is "A Clearing Record that an Acquirer presents to an Issuer through Interchange, either initially (a first Presentment) or after a Dispute (a Dispute Response or pre-Arbitration)." **Interchange**, in the rulebook's sense, is "The exchange of Clearing Records between Members"; the fee is the separate term **Interchange Reimbursement Fee**, "A fee between Acquirers and Issuers in the Clearing and Settlement of an Interchange Transaction." [VERIFIED: Visa Core Rules glossary, 2026-10-24].
- The validity windows in 2.3 are, in the rulebook, clearing deadlines: "An Acquirer must process a completed Transaction as specified in Table 5-11". In Europe there is a tighter one: "an Acquirer must submit an intraregional Contactless Transaction into Clearing within 2 calendar days of the Transaction Date" [VERIFIED: Visa Core Rules §5.7.3.5, 2026-10-24].
- Interchange is fixed at clearing, not at authorization: the rate depends on the data in the clearing record and on timeliness ("interchange qualification"). This is industry knowledge; the Visa "Interchange Reimbursement Fee Rate Qualification Guide" is named in the rulebook's document list but is not public [ASSUMPTION/JUDGEMENT; the guide's existence VERIFIED in the Visa Core Rules, 2026-10-24]. Adyen's warning that late capture brings "Increased interchange fees" is a documented instance [VERIFIED: Adyen adjust-authorisation page].
- Clearing file formats (Visa's Base II transaction codes such as TC05 for a sale, Mastercard's IPM files) are not public documents. The Visa VAMP fact sheet names three of the codes in passing: "Count of [Fraud (TC40) + Disputes (TC15)] ÷ Count of Settled Transactions (TC05)" [VERIFIED: https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf, published 2025].

### 3.3 Net settlement between members

- Visa: **Settlement** is "The reporting and funds transfer of Settlement Amounts owed by one Member to another, or to Visa, as a result of Clearing." A **Settlement Amount** is "The daily net amounts expressed in a Member’s Settlement Currency resulting from Clearing. These amounts include Transaction and Fee Collection Transaction totals" [VERIFIED: Visa Core Rules glossary, 2026-10-24].
- The network guarantees members against each other, and that is its settlement risk: "We indemnify issuers and acquirers for settlement losses they may suffer due to the failure of another issuer or acquirer to honor its settlement obligations in accordance with the Visa operating rules. This indemnification creates settlement risk for us due to the difference in timing between the payment transaction date and subsequent settlement date." [VERIFIED: Visa 10-K, 2026-11-05].
- The guarantee stops at the acquirer: "We guarantee the settlement of many of the transactions from issuers to acquirers ... We do not, however, guarantee payments to merchants by their acquirers" [VERIFIED: Mastercard 10-K, 2026-02-11]. A merchant's exposure to its provider between settlement and payout is therefore a matter of the provider's licence and safeguarding, not of network rules [ASSUMPTION/JUDGEMENT; see the `ledger` and `risk` briefs].
- Interchange travels with settlement: "We administer the collection and remittance of interchange fees through the settlement process." [VERIFIED: Mastercard 10-K, 2026-02-11].
- Settlement cut-off times, the number of settlement cycles per day, settlement currencies and the settlement banks used are not in the public rule text read for this brief [ASSUMPTION/JUDGEMENT: next-business-day settlement in major currencies is industry practice].

### 3.4 Funding the merchant

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| States | Balance is `pending` then `available`: "Funds in the pending state represent incoming transactions that haven’t settled into your balance." [VERIFIED: https://docs.stripe.com/payments/balances.md, n.d., accessed 2026-11] | "1. Capture: A payment is captured, and the card scheme or payment method sends the funds to Adyen. 2. Adyen processing: The funds are assigned to a payable batch ... 3. Bank processing" [VERIFIED: https://docs.adyen.com/account/getting-paid.md, n.d., accessed 2026-11] |
| Timing vocabulary | "Settlement timing ... is typically expressed as “T+X” days"; "Stripe uses “T” to refer to the transaction time, which indicates the time of the original payment confirmation or capture", whereas "Some payment processors might start “T” from their internal settlement time, meaning when the funds land in their bank accounts." The page's same-day payout table refers to "Standard T+2 settlement timing" for US dollar accounts and "Standard T+3 settlement timing" for GBP and EUR accounts [VERIFIED: https://docs.stripe.com/payouts.md, n.d., accessed 2026-11] ⚠ | "If the payable balance is positive when the payable batch closes, Adyen instructs the payout to you." Payouts are per merchant account; "Adyen cannot process payouts on bank holidays" [VERIFIED: Adyen getting-paid page] |
| Schedule versus speed | "Choosing a payout schedule doesn’t change how long it takes for your pending balance to become available. It only controls when payouts are sent." | Payout model and payout frequency are separate settings (sales-day payout details are in the `ledger` brief) |
| Business versus calendar days | Delay counted in business days for AU, IN, JP, MY, NZ, TH, AE, US; calendar days for CA, HK, MX, NO, SG, CH, GB and "supported EU countries" [VERIFIED: Stripe payouts page] | Not on the page fetched |

- **The difference the evidence supports**: Stripe states that it counts from capture, not from the moment network funds arrive, and labels the result a "settlement timing". Stripe therefore uses "settlement" for *its* release of funds to the merchant's available balance, which is not the network's settlement (3.3). Adyen's page separates the network sending funds to Adyen from Adyen's batch and the bank's processing. Chapter 03 should define "settled" per layer and warn that the two providers use the word for different events [ASSUMPTION/JUDGEMENT on the framing; the quoted definitions are VERIFIED].
- Whether either provider pays out before it has received network settlement (pre-funding) is not stated on the pages fetched [ASSUMPTION/JUDGEMENT].

**For readers new to payments.** *Capture*: the merchant's instruction to collect an authorized amount. *Clearing*: the exchange of final transaction records between acquirer and issuer through the network, where the amount, the data and the interchange fee become definitive. *Presentment*: the clearing record the acquirer sends for one transaction. *Net settlement*: each member pays or receives one net amount per day for everything cleared, instead of paying per transaction. *Dual-message / single-message*: whether authorization and clearing are two messages (typical for credit and online payments) or one (typical for PIN debit).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. A provider's records necessarily disagree for a while: the authorization system knows an approval, the capture system knows a claim, the clearing files know what was presented, the settlement report knows a net amount, the payout knows a batch. Reconciliation exists because none of these has the same key or the same granularity. The merchant sees only the provider's projection of that chain (a balance transaction on Stripe, a journal line in a payable batch on Adyen) and must not treat "captured" as "received".

---

## PART 4: Refunds, reversals and disputes (chapters 04 and 45)

### 4.1 Void, reversal, refund

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Before capture | Cancel the PaymentIntent "at no cost" | Cancel; "You can only refund a payment after it has been captured." |
| After capture | Refund; "Stripe’s processing fees from the original transaction aren’t returned." | Refund; a "Payment method refund fee" column exists on the public price list [VERIFIED: https://www.adyen.com/pricing, n.d., accessed 2026-11] |
| Unknown state | No separate operation | Reversal endpoint (2.5) |
| Funding the refund | "Refunds use your available Stripe balance (not including pending amounts)"; if insufficient, "Stripe holds the refund as pending for card transactions (refunds for other payment method types fail)", and fails it with `insufficient_funds` after 45 days | Not on the page fetched |
| Synchrony | A refund object with a status; "A refund can fail if the customer’s bank or card issuer can’t process it ... This process can take up to 30 days from the post date." | "The refund process is asynchronous." A webhook with `success: true` means "we sent the refund request to the card scheme"; "in rare cases the refund can be rejected by the card scheme, or reversed" (REFUND_FAILED, REFUNDED_REVERSED) |
| Time to reach the customer | "Successful refunds appear on the bank statement of your customers in real time, depending on the card network and issuing bank." | "It can take up to 40 business days before the funds are returned to the shopper's account, depending on the payment method." |
| Destination | "Refunds can only be sent back to the original payment method used in a charge." | Referenced refunds to the original payment; "unreferenced refunds" (to a card, ACH or IBAN without an original payment) need approval and report through a REFUND_WITH_DATA webhook |
| Refund as reversal | "Some refunds—those issued shortly after the original charge—appear in the form of a *reversal* ... the original charge drops off the customer’s statement"; "IC+ users might see a difference in cost between reversals and refunds because reversals usually incur lower network fees." | The reversal endpoint decides cancel or refund from the payment's state |
| Partial refunds | Any number up to the captured amount | "the sum of the refund amounts cannot be more than the captured amount" |
| Refund and dispute interaction | Failure reason `charge_for_pending_refund_disputed`; "You can’t issue a refund outside the dispute process while the dispute is open." | Adyen auto-defends chargebacks on payments where "more than 90 percent of the captured transaction amount was refunded" (4.8) |

Sources: [VERIFIED: https://docs.stripe.com/refunds.md and https://docs.stripe.com/disputes/how-disputes-work.md, n.d., accessed 2026-11]; [VERIFIED: https://docs.adyen.com/online-payments/refund.md and https://docs.adyen.com/risk-management/manage-disputes.md, n.d., accessed 2026-11].

- ⚠ **Updates the sibling briefs.** The October and November 2026 sibling briefs quoted Stripe's refunds page as saying the customer "sees the refund as a credit approximately 5-10 business days later". The page fetched today says refunds "appear on the bank statement of your customers in real time, depending on the card network and issuing bank". Use the current wording.
- A refund stops being able to prevent a fraud report quickly: "The only time a refund can prevent a fraud report is when it’s processed as a reversal, which usually happens within 2 hours of the payment capture." [VERIFIED: Stripe how-disputes-work page].

### 4.2 The Visa dispute lifecycle

- Visa's vocabulary (the 2018 "Visa Claims Resolution" redesign; the rulebook itself does not use that name): a **Dispute** is "A Transaction that an Issuer returns to an Acquirer"; a **Dispute Response** is "A Clearing Record that an Acquirer presents to an Issuer through Interchange after a Dispute." [VERIFIED: Visa Core Rules glossary, entries last updated April 2018, edition 2026-10-24]. The programme name and its April 2018 launch are [ASSUMPTION/JUDGEMENT] (not found by name in the rule text searched).
- **Four categories of dispute condition** [VERIFIED: Visa Core Rules chapter 11 contents, 2026-10-24]:

| Category | Conditions |
| --- | --- |
| 10 Fraud | 10.1 EMV Liability Shift Counterfeit Fraud; 10.2 EMV Liability Shift – Non-Counterfeit Fraud; 10.3 Other Fraud – Card-Present Environment; 10.4 Other Fraud – Card-Absent Environment; 10.5 Visa Monitoring Programs |
| 11 Authorization | 11.1 Card Recovery Bulletin; 11.2 Declined Authorization; 11.3 No Authorization/Late Presentment |
| 12 Processing Errors | 12.2 Incorrect Transaction Code; 12.3 Incorrect Currency; 12.4 Incorrect Account Number; 12.5 Incorrect Amount; 12.6 Duplicate Processing/Paid by Other Means; 12.7 Invalid Data |
| 13 Consumer Disputes | 13.1 Merchandise/Services Not Received; 13.2 Cancelled Recurring Transaction; 13.3 Not as Described or Defective Merchandise/Services; 13.4 Counterfeit Merchandise; 13.5 Misrepresentation; 13.6 Credit Not Processed; 13.7 Cancelled Merchandise/Services; 13.8 Original Credit Transaction Not Accepted; 13.9 Non-Receipt of Cash at an ATM |

- **Two process flows.** For categories 10 and 11 (Table 11-2), the steps after the dispute are a **pre-arbitration attempt** by the acquirer ("30 calendar days from the Dispute Processing Date"), a **pre-arbitration response** by the issuer ("30 calendar days from the Processing Date of the pre-Arbitration attempt") and **arbitration**; there is no separate dispute-response step. The pre-arbitration attempt "does not apply if the Merchant accepted the Dispute through Rapid Dispute Resolution." For categories 12 and 13 (Table 11-3) there is first a **dispute response** by the acquirer ("30 calendar days from the Dispute Processing Date"), then a pre-arbitration attempt by the *issuer* ("30 calendar days from the Dispute Response Processing Date"), a pre-arbitration response by the acquirer (30 calendar days) and arbitration filed by the issuer. Arbitration filing limits of 10 calendar days and regional exceptions appear in the tables' later rows and footnotes [VERIFIED: Visa Core Rules §11.3, Tables 11-2 and 11-3, 2026-10-24]. Note the reversal of roles: in fraud and authorization disputes the merchant's side must escalate; in consumer and processing disputes the issuer must.
- Adyen names the two flows: "Visa disputes are routed in two default workflows, called **Allocation** and **Collaboration**": "The Allocation flow relates to all fraud and authorization cases. The Collaboration flow relates to all consumer disputes and processing errors." [VERIFIED: https://docs.adyen.com/risk-management/chargeback-guidelines/visa-chargebacks.md, n.d., accessed 2026-11]. The practical difference Adyen documents: "For Allocation chargebacks, if you defend the dispute, the chargeback amount will not be immediately transferred back."
- Stripe describes the same asymmetry from the merchant's side: for "Visa fraud: Your initial response counts as filing for pre-arbitration. If the issuer rejects this response, you can appeal the case straight to arbitration. You must take action within 7 days of the issuer’s rejection." [VERIFIED: https://docs.stripe.com/disputes/arbitration.md, n.d., accessed 2026-11].
- **Time limits for the issuer to dispute**: "120 calendar days from the Transaction Processing Date" for many conditions; "75 calendar days from the Transaction Processing Date" for the authorization conditions 11.1–11.3; for 10.5, "120 calendar days from the date of the Visa Monitoring Program report" [VERIFIED: Visa Core Rules dispute time-limit tables, 2026-10-24]. The 540-day outer limit is Adyen's statement (1.2); it was not located in the Visa text by search.
- ⚠ **A rule change to watch**: "Effective for Disputes processed on or after 24 April 2027 Before initiating a Dispute, the Issuer must validate and reconcile all credits and debits processed by the same Merchant that could be related to the disputed Transaction(s)" and "Submit the Dispute only for the resulting net disputed amount" [VERIFIED: Visa Core Rules Table 11-2, 2026-10-24].
- **Compelling Evidence** is a rulebook term (§11.6.1, "Use of Compelling Evidence") [VERIFIED: Visa Core Rules, 2026-10-24]. Stripe automates the 2023 version for one condition: "For fraudulent disputes with the Visa 10.4 (Card absent fraud) code, Stripe automatically evaluates your transaction history to determine eligibility with Visa Compelling Evidence 3.0." [VERIFIED: https://docs.stripe.com/disputes/responding.md, n.d., accessed 2026-11].

### 4.3 The Mastercard chargeback cycles

All statements here are the providers' renderings (Mastercard documents were blocked).

- Adyen's flow: Notification of Chargeback → Chargeback → Information Supplied → Chargeback Reversed → Pre-Arbitration → Second Chargeback → Scheme Arbitration. "In the Mastercard chargeback process, an issuer can escalate a dispute and file a Pre-Arbitration case. This applies to all Mastercard reason codes, except 4808, 4870, and 4871. These disputes will go to Scheme Arbitration directly if escalated." [VERIFIED: https://docs.adyen.com/risk-management/chargeback-guidelines/mastercard-chargebacks.md, n.d., accessed 2026-11].
- Defence deadline at Adyen: "You must provide your defense documents within **40 days**." [VERIFIED: same].
- Stripe's summary of the last two stages for "Visa non-fraud and Mastercard": the issuer "rejects" the response, "filing pre-arbitration"; "You can submit a final, targeted evidence package to refute their justification within 20 days"; then "Issuers have a finite window (10 days for Visa, 15 days for Mastercard) to elevate the case", after which "they implicitly assume liability." [VERIFIED: Stripe arbitration page].
- The traditional names of the cycles (first chargeback, second presentment, pre-arbitration, arbitration case filing) and the elimination of the "arbitration chargeback" cycle around 2020 are industry knowledge, not verified here [ASSUMPTION/JUDGEMENT].

### 4.4 Reason-code families

| Family | Visa (primary, 4.2) | Mastercard codes as listed by Adyen |
| --- | --- | --- |
| Fraud | 10.x | 4837 No Cardholder Authorization; 4863 Cardholder does not recognize – Potential Fraud; 4849 Questionable merchant activity; 4870 Chip Liability Shift; 4871 Chip/PIN Liability Shift |
| Authorization | 11.x | 4802 / 4808 Requested/Required Authorization not obtained; 4807 Warning Bulletin File; 4812 Account Number Not on File |
| Processing errors | 12.x | 4834 Point of Interaction error; 4842 Late Presentment; 4846 Correct Transaction Currency Code not provided |
| Consumer disputes | 13.x | 4853 (cardholder dispute; Adyen lists sub-reasons such as "Goods not as described/defective"); 4841 Cancelled Recurring Transaction; 4855 Non receipt of merchandise; 4860 Credit not Processed |

[VERIFIED: https://docs.adyen.com/risk-management/understanding-disputes/dispute-reason-codes.md, n.d., accessed 2026-11] for the Mastercard code names as Adyen prints them. Several of the 48xx codes Adyen lists (4841, 4855, 4860, 4842) are older codes that Mastercard consolidated into 4853 and 4834; whether they are still issued is not verified [ASSUMPTION/JUDGEMENT]. Stripe maps every network's codes to its own categories on one page (sections for Visa, Mastercard, American Express, Discover, Klarna, PayPal, Cash App Pay) with per-category "How to prevent it" and "How to overturn it" guidance [VERIFIED: https://docs.stripe.com/disputes/categories.md, n.d., accessed 2026-11]. Mastercard's Excessive Fraud Merchant programme counts "dispute reason code 4837 or 4863" [VERIFIED: https://docs.stripe.com/disputes/monitoring-programs.md, n.d., accessed 2026-11].

### 4.5 Time limits side by side

Calendar days, as Adyen documents them [VERIFIED: https://docs.adyen.com/risk-management/understanding-disputes/dispute-timeframes.md, n.d., accessed 2026-11] ⚠:

| Stage | Visa Collaboration | Visa Allocation | Mastercard | American Express |
| --- | --- | --- | --- | --- |
| Issuer initiates chargeback (from transaction date) | 120 | 120 | 120 | 120 |
| Merchant response to an RFI | n/a | n/a | n/a | 14 |
| Merchant response to a chargeback (from notification) | 9 or 18 | 9 or 18 | 40 | 14 |
| Issuer initiates pre-arbitration | 28 | n/a | 8 to 28 | n/a |
| Final decision (from defence date) | 60 | 45 | 70 | 50 |

- The Visa response window was shortened in North America: "From 21 July 2025, the response timeframe for disputes opened on payments processed locally in the United States and Canada is 9 days. For disputes opened before this date in the United States or Canada, and for all other countries and regions, the response timeframe is 18 days." [VERIFIED: same].
- These are Adyen's merchant-facing deadlines; they are shorter than the 30 calendar days the Visa rules give the acquirer (4.2). The difference is the provider's own processing time [ASSUMPTION/JUDGEMENT].
- Stripe gives ranges instead of a table: "you have a limited time to respond to the card issuer: usually 7-21 days, depending on the card network"; "the issuer has a limited time to evaluate it and decide the outcome: usually 60-75 days"; "The full dispute lifecycle ... can take 2-3 months". The exact deadline is `evidence_details.due_by` on the Dispute object [VERIFIED: Stripe how-disputes-work, arbitration and API pages].
- Other methods are longer: UnionPay 180 days to initiate in Adyen's table; on Stripe "LPMs typically allow customers up to 180 days to file a dispute" [VERIFIED: both pages].

### 4.6 Pre-dispute products

- **Rapid Dispute Resolution (Verifi, a Visa company).** Verifi's description: "When a customer calls their issuer to request a refund through the chargeback process, a pre-dispute is entered into Visa’s issuer dispute submission platform. For RDR participating sellers, the pre-dispute immediately triggers the decision engine to evaluate it with the seller-defined rules for automated resolution." "Sellers can create up to 10 rule scenarios and have 7 attributes to choose from". Resolved cases are "sent to the acquirer on behalf of the issuer through a Visa TC15 financial transaction ... which includes a specific RDR identifier", and "Acquirers may charge a processing fee on pre-disputes resolved via RDR" [WIDELY REPORTED: https://www.verifi.com/10-facts-for-success-rdr.html and https://www.verifi.com/rdr-is-here.html, vendor marketing, n.d.] **(evidence age: undated; written around RDR's launch, approximately six years old; the mechanism is confirmed by Adyen's and Stripe's current pages below)**.
- **Adyen on RDR**: "When a dispute is rapidly resolved, it is resolved through a refund and does **not** become a chargeback." Yet "Although an RDR is a refund, in Adyen, RDR qualified transactions are referred to as chargebacks"; "You cannot defend an RDR chargeback"; and "You will not be charged any chargeback or interchange fees for transactions that go through the RDR flow, and these transactions are not included in the dispute count." [VERIFIED: Adyen Visa chargebacks page].
- **Stripe's dispute prevention**: "Stripe integrates directly with Verifi and Ethoca and provides your existing transaction data on your behalf at time of lookup." "Stripe routes deflection data through Verifi’s Order Insights for Visa transactions and Ethoca’s Consumer Clarity for Mastercard transactions. When eligible, adding Compelling Evidence 3.0 can block disputes entirely." Resolution rules are set through Radar; "Resolved disputes don’t count towards your dispute rate and don’t incur a dispute received fee." [VERIFIED: https://docs.stripe.com/disputes/prevention-preview.md, n.d., accessed 2026-11].
- Stripe prices these per outcome (Netherlands): "€20.00 per Visa resolution", "€20.00 per Visa Compelling Evidence 3.0 block", "€40.00 per Mastercard resolution" [VERIFIED: https://stripe.com/en-nl/pricing, n.d., accessed 2026-11] ⚠.
- **Fraud notifications are not disputes but count.** Stripe: early fraud warnings "include Visa TC40 reports and Mastercard’s System to Avoid Fraud Effectively (SAFE) reports"; "about 40% of Visa and Mastercard EFWs become fraud disputes"; "It’s likely not worthwhile to refund EFWs on charges more than 35 percent higher than your dispute fee." Adyen's equivalent is the Notification of Fraud: "This is not a dispute, and no money is withdrawn from your account." [VERIFIED: Stripe how-disputes-work page; https://docs.adyen.com/risk-management/understanding-disputes/dispute-process-and-flow.md, n.d., accessed 2026-11].
- **Ethoca Alerts** (issuer-to-merchant alert before a chargeback, owned by Mastercard) and **Verifi CDRN** could not be read from the vendors' current pages. Adyen confirms CDRN exists and is excluded from VAMP: "Chargebacks resolved through the Visa Rapid Dispute Resolution (RDR) flow and the Cardholder Dispute Resolution Network (CDRN) are excluded from the ratio calculation." [VERIFIED: https://docs.adyen.com/risk-management/dispute-and-fraud-monitoring.md, n.d., accessed 2026-11]. Adyen's documentation of an Ethoca integration: nothing found in the pages fetched.

### 4.7 Monitoring programmes and current thresholds ⚠

**Visa Acquirer Monitoring Program (VAMP).**

- Visa consolidated "the existing VAMP, Visa Fraud Monitoring Program, and Visa Dispute Monitoring Program into a single global program. Updates to the program thresholds will be effective 1 June 2025", with an advisory period ending 30 September 2025 [VERIFIED: Visa VAMP fact sheet, published 2025]. Adyen dates the consolidation itself to 1 April 2025 [VERIFIED: Adyen monitoring page].
- "VAMP Ratio = Count of [Fraud (TC40) + Disputes (TC15)] ÷ Count of Settled Transactions (TC05)", on "card-not-present VisaNet transactions (domestic and cross-border)"; it "Excludes disputes resolved through pre-dispute solutions" and "TC 40 fraud qualified for Compelling Evidence 3.0" [VERIFIED: Visa VAMP fact sheet].
- Acquirer level: "An acquirer’s portfolio is identified as Above Standard if its VAMP ratio is ≥50bps and as Excessive if ≥70bps" [VERIFIED: same].
- Merchant level: Excessive at "VAMP Ratio: ≥220bps" with "Monthly count of fraud and disputes: ≥1,500" in AP, Canada, EU and US (LAC ≥150bps; CEMEA ≥220bps with "≥150 and amount ≥ USD 75,000"); footnote: "Excessive Merchant threshold reduced to >=150bps in AP, Canada, EU, and U.S. regions on 1 April 2026." [VERIFIED: same].
- Enumeration (card testing): ratio "≥ 2000 bps" and count "≥ 300,000" [VERIFIED: same].
- Both providers now show the post-April-2026 figure. Adyen: "1 April 2026: Equal to or above 1.50%", "a minimum count of 1,500 disputes applies and only card not present (CNP) transactions are considered", and "The merchant excessive ratio identification only applies if the Adyen VAMP ratio is below 0.50%." Stripe: excessive at count 1,500 and ratio "1.5% elsewhere (AP, Canada, EU, US and LAC)", "2.2% in CEMEA", plus a "Non-compliant threshold" of count 5 and ratio 0.5% [VERIFIED: Adyen monitoring page; Stripe monitoring-programs page].
- Double counting: "The same fraudulent transaction might appear in both the TC40 and TC15 reports. Any transaction that appears in both reports will be counted twice for the VAMP count." [VERIFIED: Stripe monitoring-programs page]. Adyen adds that "Notifications of Fraud (NoFs) associated with fraud chargebacks resolved through the RDR flow are not excluded" [VERIFIED: Adyen monitoring page].
- **New in 2026**: "Effective October 2026, the Visa Merchant Elevated Risk Program (MERP) applies to businesses that accept Visa payments in the Asia Pacific region"; Visa "doesn’t publish the thresholds it uses"; consequences can include "Backdated fraud disputes" for "transactions past the standard dispute deadline" [VERIFIED: Stripe monitoring-programs page]. Not found in Adyen's page.
- **Visa Secure Excessive Fraud Program (US)**: thresholds of USD 75,000 of fraud and a 0.9% rate on 3-D Secure-authenticated transactions; a merchant in it "immediately qualif[ies] for Visa dispute reason code 10.5 ... issuers will be allowed to initiate fraud chargebacks that you cannot defend"; "From October 2025, Visa has opened the window for issuers to file disputes with this reason code" [VERIFIED: Adyen monitoring page; Stripe monitoring-programs page].

**Mastercard Excessive Chargeback Program** (providers' rendering).

- **ECM**: 100–299 chargebacks and a rate of 1.5–2.99%. **HECM**: 300 or more and 3%. Rate = this month's chargebacks ÷ last month's captured payments. Fines begin in month two: ECM USD 1,000 (months 2–3) rising to USD 100,000 (month 19+); HECM USD 1,000, 2,000, then up to USD 200,000; from month 4 an "Issuer recovery assessment applies an additional 5 USD per chargeback fee for each chargeback over 300". Exit after "3 consecutive months" below threshold [VERIFIED: Stripe monitoring-programs page; ECM/HECM counts and rates also on the Adyen monitoring page].
- **Excessive Fraud Merchant (EFM)**: at least 1,000 e-commerce Mastercard payments, net fraud volume above USD 50,000, fraud chargeback rate above 0.50%, and 3-D Secure share at or below 10% (non-regulated countries) or 50% (regulated) [VERIFIED: Stripe monitoring-programs page].
- **Calendar difference**: "Visa calculates the ratio of disputes or fraud to the total number of payments in the same calendar month. Mastercard calculates the ratio ... to the total number of payments in the previous month." [VERIFIED: same].
- **What counts**: "Monitoring programs don’t consider refunds when identifying disputes" and "don’t consider dispute outcomes"; "Mastercard counts a chargeback regardless of whether it was hidden due to a refund, regardless of liability shift" [VERIFIED: same].

**Stripe vs Adyen on monitoring.**

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Where the merchant sees its standing | A VAMP dashboard with "Visa data" (reported "with a one-month delay") beside "Stripe data", "Stripe’s own computation ... in real time" | "Card monitoring programs" tab in Risk & dispute analytics, "only on your company account" |
| Unit Visa monitors | "Visa places individual accounts in its programs, but identifies an account by the static component of its statement descriptor and its acquiring bank"; one Stripe business can be several Visa accounts | Thresholds assessed "for both your merchant account(s) and Adyen" |
| The provider's own exposure | Not stated | Stated: "Visa also considers acquirer thresholds ... This means that Adyen also has to make sure that the defined VAMP thresholds are not exceeded." |
| Disputes invisible to the merchant | "Some disputes where you have no liability don’t appear in your Dashboard or API responses because Stripe handles them on your behalf ... However, monitoring programs still include them" | Auto-defended disputes are visible as INFORMATION_SUPPLIED events |

Sources: Stripe monitoring-programs page; Adyen monitoring page (both fetched 2026-11).

### 4.8 How each provider models a dispute

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Object | A `Dispute` object linked to the charge, with `status`, `evidence`, `evidence_details` (`due_by`, `has_evidence`, `past_due`, `submission_count`), `balance_transactions`, `is_charge_refundable`, `enhanced_eligibility_types` (e.g. `visa_compelling_evidence_3`) and `payment_method_details.card.case_type` [VERIFIED: https://docs.stripe.com/api/disputes/object.md and arbitration page, n.d., accessed 2026-11] | A dispute is a series of events and journal entries against the original payment, identified by a `disputePspReference`; no single dispute resource is described on the pages fetched [VERIFIED: https://docs.adyen.com/risk-management/disputes-api.md, n.d., accessed 2026-11] |
| States | `warning_needs_response`, `warning_under_review`, `warning_closed` (inquiry), `needs_response`, `under_review`, `appeal_needs_response`, `appeal_under_review`, `won`, `lost`, `prevented` | Webhook event codes: NOTIFICATION_OF_FRAUD, REQUEST_FOR_INFORMATION, NOTIFICATION_OF_CHARGEBACK, CHARGEBACK, INFORMATION_SUPPLIED, CHARGEBACK_REVERSED, PREARBITRATION_OPEN / _WON / _LOST / _ACCEPTED / _DECLINED / _ISSUER_WITHDRAWN, SCHEME_ARBITRATION, SCHEME_ARBITRATION_LOST, SECOND_CHARGEBACK, DISPUTE_DEFENSE_PERIOD_ENDED, ISSUER_COMMENTS |
| When money leaves | At creation: "Debits the disputed amount, plus a dispute fee, from your Stripe account"; "These funds are held for the entire duration of the dispute." | "Depending on the payment method, the chargeback debit happens a few days after you receive the NoC, or after you defend the dispute"; "Adyen processes the chargeback and debits the payment amount and the chargeback processing fee from your account." |
| When money returns | Only on a win: "The issuer returns the debited chargeback amount to Stripe. Stripe passes this amount back to you." | On CHARGEBACK_REVERSED the amount returns while "The issuer is still reviewing the defense"; "This stage is not final"; a Second Chargeback can take it again |
| Evidence submission | "You’ve only one opportunity to submit your response." | "Submitting the defense documents is irreversible"; API endpoints `/retrieveApplicableDefenseReasons`, `/supplyDefenseDocument`, `/acceptDispute` |
| Automation | **Smart Disputes**: "uses an AI rules engine to analyze incoming disputes", builds and submits the evidence packet; fee "30% of the disputed amount for each dispute you win" | **Auto-defense**: "Adyen will automatically defend applicable chargebacks with no action needed on your part", for refunded payments (more than 90% refunded), fraud codes with liability shift ("does not include payments made with digital wallets"), technically invalid chargebacks, and codes not applicable to the merchant's MCC |
| Pre-arbitration and arbitration | Opt-in "appeals" for eligible businesses; "Filing and ruling fees can exceed 600 USD per appeal. Technical violation fees can exceed 250 USD per violation"; network fees charged "about one month after the card network rules" | Accepting or declining pre-arbitration "requires additional configuration and approval from Adyen"; if the scheme rules for the issuer "you can incur a fee of up to USD 600. This fee is added to the second chargeback." |
| Fees (public) | Netherlands: dispute received €20.00; dispute countered €20.00 ("You get this fee back for won disputes"); dispute appealed €20.00 (not returned). US: $15.00 each [VERIFIED: https://stripe.com/en-nl/pricing and https://stripe.com/us/pricing, n.d., accessed 2026-11] ⚠ | A "chargeback processing fee" exists; **no amount is public** (searched the pricing page text for "chargeback": no fee listed) |
| Fee exceptions | Received fee refundable only in Mexico; no received fee for SEPA businesses on Cartes Bancaires; no countered fee in Mexico and Japan | Not public |
| Outcomes after "final" | "Late win": status "can change from `lost` to `won`" when "issuers credit or debit Stripe for a dispute outside of the regular dispute lifecycle" | American Express "can reopen a dispute that was previously closed in your favor" (SecondChargeback journal) |
| Unchallengeable cases | Closed as lost on notification (e.g. Cartes Bancaires for SEPA businesses, Nigerian payment methods, unanswered Discover inquiries) | RDR chargebacks; Klarna after the RFI stage |

Sources: Stripe how-disputes-work, responding, arbitration, smart-disputes and API pages; Adyen dispute-process-and-flow, timeframes, manage-disputes, Visa and Mastercard guideline pages (all fetched 2026-11).

- ⚠ **Updates the sibling briefs.** The October 2026 sibling brief recorded that Stripe "doesn’t support the arbitration phase". The page fetched today says "eligible businesses that enable appeals can continue challenging eligible disputes through pre-arbitration or arbitration", with new statuses and a "Dispute appealed fee". The `prevented` status is also new.
- **The difference the evidence supports.** Stripe gives a dispute one object with one status and moves money once at the start and once at the end. Adyen exposes the network's cycle more literally: the provisional credit on CHARGEBACK_REVERSED and the possible SECOND_CHARGEBACK are separate financial events. A ledger fed by Adyen events must treat a reversed chargeback as provisional; a ledger fed by Stripe events must treat a `lost` dispute as reopenable [ASSUMPTION/JUDGEMENT on the ledger consequence].
- The disputed amount can differ from the payment: currency conversion ("the 113.74 USD chargeback is now 107.86 EUR to the business instead of the original 100 EUR"), several recurring charges disputed as one, partial disputes, and disputes on partially refunded charges; a payment can also receive more than one dispute [VERIFIED: Stripe how-disputes-work page].

**For readers new to payments.** *Refund*: a new transaction that sends money back and can itself fail. *Reversal / void*: cancelling an authorization (or a very recent charge) so that no payment appears at all. *Chargeback (dispute)*: the issuer returns a transaction to the acquirer on the cardholder's behalf and the funds are pulled back before anyone has judged the claim. *Representment (dispute response)*: the merchant's evidence, sent once through the provider and network to the issuer. *Monitoring programme*: a network scheme that counts a merchant's disputes and fraud reports against its sales every month and fines or restricts merchants above a threshold, whatever the outcomes were.

**Architecture implications** [ASSUMPTION/JUDGEMENT]. (1) A payment record needs to stay mutable in its financial effect for at least 120 days and in rare cases over a year; "final" is a probability, not a state. (2) Dispute handling is deadline-driven work with a single submission, so the evidence (delivery proof, login history, prior undisputed transactions for Compelling Evidence 3.0) has to be captured at the time of sale, not assembled on demand. (3) The monitoring ratio is computed by the network on its own identifiers (statement descriptor and acquirer on Visa) and on counts the merchant cannot fully see, so a platform should compute its own estimate per network identity and alert well below the threshold. (4) Refund-first policies reduce chargeback fees but not the ratio once a fraud report exists; pre-dispute resolution is the only route the fact sheet excludes from the count.

---

## PART 5: Payment economics (chapter 05)

### 5.1 Who sets interchange

- Visa: "Generally, IRFs are paid by acquirers to issuers. We establish default IRFs that apply absent other established settlement terms. These default IRFs are set independently from the revenue we receive from issuers and acquirers." And: "Our acquiring clients are responsible for soliciting sellers and for setting the fees they charge to sellers for the MDR. Visa sets fees to acquirers independently from any fees that acquirers may charge sellers. Therefore, the fees we receive from issuers and acquirers are not derived from IRFs or MDRs." [VERIFIED: Visa 10-K, 2026-11-05].
- Mastercard: "Generally, interchange fees are collected from acquirers and paid to issuers to reimburse the issuers for a portion of the costs incurred." "We (or, alternatively, financial institutions) establish “default interchange fees” that apply when there are no other established settlement terms in place between an issuer and an acquirer." "Although we do not earn revenues from interchange, interchange rates can impact the volume of transactions we see on our payment products." [VERIFIED: Mastercard 10-K, 2026-02-11].
- The merchant's price is the acquirer's: "The merchant discount rate is established by the acquirer to cover its costs of both participating in the four-party system and providing services to merchants." [VERIFIED: Mastercard 10-K, 2026-02-11].
- EU law's definition closes the obvious loophole: "‘interchange fee’ means a fee paid for each transaction directly or indirectly (i.e. through a third party) between the issuer and the acquirer involved in a card-based payment transaction. The net compensation or other agreed remuneration is considered to be part of the interchange fee" [VERIFIED: Regulation (EU) 2015/751 Art. 2, 2015-05-19].

### 5.2 The EU Interchange Fee Regulation (EU) 2015/751

**(evidence age: 11 years; in force; Visa's November 2026 annual report notes "the European Commission (EC) may periodically reassess Interchange Fee Regulations, which could further lower caps or expand regulation to additional products, services and fees" [VERIFIED: Visa 10-K, 2026-11-05])**

- **Caps**: "Payment service providers shall not offer or request a per transaction interchange fee of more than 0,2 % of the value of the transaction for any debit card transaction" (Art. 3); "more than 0,3 % of the value of the transaction for any credit card transaction. For domestic credit card transactions Member States may define a lower per transaction interchange fee cap" (Art. 4) [VERIFIED: http://publications.europa.eu/resource/celex/32015R0751, published 2015-05-19].
- **Scope**: the caps do "not apply to" "transactions with commercial cards", cash withdrawals, and "transactions with payment cards issued by three party payment card schemes" (Art. 1(3)) [VERIFIED: same].
- **Anti-circumvention**: "any agreed remuneration, including net compensation, with an equivalent object or effect of the interchange fee" counts toward the cap (Art. 5) [VERIFIED: same].
- **Separation of scheme and processing** (Art. 7): schemes and processing entities "shall be independent in terms of accounting, organisation and decision-making processes" and "shall not present prices for payment card scheme and processing activities in a bundled manner" [VERIFIED: same]. Visa names the consequence: "as a result of the Interchange Fee Regulation (IFR) in Europe, we may face competition from other networks, processors and other third parties who could process Visa transactions directly with issuers and acquirers." [VERIFIED: Visa 10-K, 2026-11-05].
- **Unblending** (Art. 9), the legal basis for interchange-plus pricing in Europe: "Each acquirer shall offer and charge its payee merchant service charges individually specified for different categories and different brands of payment cards with different interchange fee levels unless payees request the acquirer, in writing, to charge blended merchant service charges." Agreements must give "individually specified information on the amount of the merchant service charges, interchange fees and scheme fees" [VERIFIED: Regulation (EU) 2015/751, 2015-05-19].
- **Per-transaction information** (Art. 12): the payee's provider must give the reference, the amount, and "the amount of any charges for the card-based payment transaction, indicating separately the merchant service charge and the amount of the interchange fee"; with consent this "may be aggregated by brand, application, payment instrument categories and rates of interchange fees" [VERIFIED: same].
- **Dates**: applies "from 8 June 2015, with the exception of Articles 3, 4, 6 and 12, which shall apply from 9 December 2015, and of Articles 7, 8, 9 and 10, which shall apply from 9 June 2016" [VERIFIED: same].
- The UK position after Brexit and the treatment of UK–EEA cross-border card-not-present interchange were not researched for this brief [ASSUMPTION/JUDGEMENT: a known divergence; verify before printing].

### 5.3 The US Durbin amendment, Regulation II and debit routing ⚠

- The rule: a covered issuer "may not receive, for any electronic debit transaction, an interchange fee that exceeds $0.21 plus 0.05 percent multiplied by the value of the transaction, plus a $0.01 fraud-prevention adjustment, if eligible." [VERIFIED: https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm, published 2025-12-19].
- Who is covered: the cap was set in 2011 "for debit card issuers with $10 billion or more in assets" [VERIFIED: https://www.federalreserve.gov/newsevents/pressreleases/bcreg20231025a.htm, published 2023-10-25] **(evidence age: 3 years; the cap level is confirmed by the December 2025 page)**.
- Routing: the rule "prohibits all issuers and networks from restricting the number of networks over which debit transactions may be processed to less than two unaffiliated networks, and from inhibiting a merchant's ability to direct the routing of a debit transaction over any network that the issuer has enabled to process it." [VERIFIED: https://www.federalreserve.gov/paymentsystems/regii-about.htm, published 2024-05-17 ("Last Update")]. Visa describes the later clarification as "requiring issuers to ensure dual-network availability for ecommerce debit transactions" [VERIFIED: Visa 10-K, 2026-11-05].
- **What the cap does, in the Fed's 2024 data** (all networks): covered transactions averaged an interchange fee of **$0.23**, or **0.47%** of an average $48.95 ticket; exempt transactions (small issuers and exempt cards) averaged **$0.51**, or **1.21%** of $42.27; exempt transactions were 39.3% of transactions by number. On dual-message networks alone the exempt average was $0.61 (1.41%) against $0.22 (0.45%) for covered [VERIFIED: Fed average-interchange page, 2025-12-19].
- **2023 proposal**: the Board proposed lowering the cap so that "the cap on an average-sized $50 debit card transaction would decline from 24.5 cents under the current rule to 17.7 cents", with biennial updates [VERIFIED: Fed press release, 2023-10-25] **(evidence age: 3 years; not finalised as far as this session found)**.
- **Litigation, status November 2026.** On 26 October 2026 the US Court of Appeals for the Eighth Circuit, in *Corner Post, Inc. v. Board of Governors of the Federal Reserve System*, unanimously affirmed a North Dakota district court's vacatur of the 21-cent standard, holding that the statute requires distinguishing "between costs that are transaction-specific and those that are not"; the decision "would not become effective until issuance of the mandate"; the district court had stayed its vacatur pending appeal; a separate case, *Linney's Pizza*, went the Fed's way in the Eastern District of Kentucky and was argued in the Sixth Circuit on 22 October 2026 [WIDELY REPORTED: https://www.consumerfinancemonitor.com/2026/10/28/eighth-circuit-invalidates-federal-reserves-21-cent-debit-card-interchange-fee-cap-holding-that-the-durbin-amendment-requires-a-transaction-specific-cost-analysis/, law-firm briefing (Ballard Spahr), 2026; https://bankingjournal.aba.com/2026/11/eighth-circuit-affirms-vacatur-of-regulation-ii/, trade association journal, 2026]. Visa's filing corroborates in general terms: "Recent conflicting federal court decisions on the validity of Regulation II's interchange fee standard have created additional uncertainty and could result in a significantly lower interchange cap for debit transactions." [VERIFIED: Visa 10-K, 2026-11-05]. **Writers should say the cap is under a court ruling that has not yet taken effect, and give the date they checked.** The opinion itself was not fetched.
- **US Department of Justice v. Visa**: "On September 24, 2024, the U.S. Department of Justice filed a complaint ... alleging violations of the Sherman Act. The complaint alleges Visa has monopolized and attempted to monopolize general purpose debit network services and card-not-present debit network services in the United States" [VERIFIED: Visa 10-K, 2026-11-05]. Current procedural status not researched.
- **Credit routing**: "Congress has reintroduced the Credit Card Competition Act (CCCA), legislation requiring, among other things, large issuers to offer routing choices for credit transactions. It remains unclear if the CCCA will gain sufficient traction" [VERIFIED: Visa 10-K, 2026-11-05].
- **Stripe vs Adyen on US debit routing**: nothing found in the pages fetched for either (searched both documentation indexes, `docs.stripe.com/llms.txt` and `docs.adyen.com/llms.txt`, for "debit routing"; an Adyen URL guessed for the topic returned 404). The topic belongs to the `optimization` brief.

### 5.4 The US merchant interchange settlement (credit) ⚠

- From Visa's annual report: "On March 25, 2024, Visa and Mastercard entered into a settlement agreement to resolve the Injunctive Relief Class claims. Following the agreement, the plaintiffs filed a motion for preliminary approval of the settlement, which was denied on June 25, 2024. On November 10, 2025, Visa and Mastercard entered into a superseding amended settlement agreement to resolve the Injunctive Relief Class claims, and the plaintiffs moved for preliminary approval of the settlement, which was granted on June 9, 2026. On July 15, 2026, the Injunctive Relief Class plaintiffs filed a motion for final approval of the settlement." The class is "all merchants that accept Visa or Mastercard credit or debit cards in the United States at any time between December 18, 2020 and entry of final judgment", certified "without opt out rights" [VERIFIED: Visa 10-K, 2026-11-05].
- Terms as reported: the combined average effective credit interchange rate falls by "ten basis points" for five years (the rejected 2024 deal offered seven); standard consumer credit rates capped at 1.25% for eight years; merchants may decline some higher-cost premium and commercial credit cards (a departure from "honor all cards"); wider surcharging and discounting rights; a USD 21 million merchant education programme. Baseline: "a 2.35% weighted average fee on Visa and Mastercard transactions in 2024, according to the Nilson Report" [WIDELY REPORTED: https://www.paymentsdive.com/news/visa-mastercard-reach-legal-pact-with-merchants/805137/ (2025-11-10) and https://www.paymentsdive.com/news/court-approves-visa-mastercard-settlement/822440/ (2026-06-09), trade press, 2025–2026].
- Preliminary approval was granted by Judge Brian Cogan (Eastern District of New York), who wrote that the test is "whether it is fair, reasonable, and adequate"; large merchants including Walmart objected, and the National Association of Convenience Stores said it would appeal a final approval [WIDELY REPORTED: Payments Dive, 2026-06-09]. The Merchant Payments Coalition filed an objection reported on 14 September 2026 [WIDELY REPORTED: https://www.supermarketnews.com/grocery-operations/retailers-object-to-interchange-fee-settlement, trade press, 2026].
- **Status as of 17 November 2026: preliminarily approved, not final.** A final-approval hearing reportedly took place or was scheduled for 16 November 2026; its outcome was not found. The "USD 38 billion" value attached to the deal in headlines was not traced to a primary source [ASSUMPTION/JUDGEMENT on both points; verify before printing].
- The cost to the networks is visible: "During fiscal 2026, we recorded additional accruals of $1.6 billion to address claims associated with the interchange multidistrict litigation." [VERIFIED: Visa 10-K, 2026-11-05].

### 5.5 Scheme fees and other network charges

- Scheme (network) fee schedules are not public. What the public record shows is their *kinds*: Visa earns "service, data processing, international transaction or other revenue", with "Payments volume ... the primary driver for our service revenue, and the number of processed transactions ... the primary driver for our data processing revenue" [VERIFIED: Visa 10-K, 2026-11-05]. So one fee family scales with value, one with message count, one with cross-border activity [ASSUMPTION/JUDGEMENT on the mapping to merchant-facing scheme fees].
- Behavioural fees documented by the providers: Visa "system integrity fees" for excessive retries and bad data (2.2); Mastercard retry "penalty fees" (MAC 03 and 21); Visa "processing integrity fees" and an "Extended Authorisation scheme fee" for late capture; a Mastercard "late capture fee" on US and Canadian domestic transactions; network arbitration filing fees [VERIFIED: Adyen raw-responses, integrity-fee and adjust-authorisation pages; Stripe arbitration page].
- Both providers sell avoidance of these fees as a feature (2.2), and Stripe quantifies it for IC+ users: "Stripe uses interchange and scheme fee rules or specifications from card networks to compute costs you would have incurred without the use of optimizations." [VERIFIED: https://docs.stripe.com/payments/analytics/optimization.md, n.d., accessed 2026-11]. Stripe also states network tokens can "qualify for reduced interchange or avoid scheme fee penalties" [VERIFIED: same].

### 5.6 Blended versus interchange-plus-plus: how each provider prices ⚠

**Stripe.**

- US standard: "2.9% + 30¢ per successful transaction for domestic cards", "+ 0.5% for manually entered cards", "+ 1.5% for international cards", "+ 1% if currency conversion is required"; "No setup fees, monthly fees, or hidden fees." [VERIFIED: https://stripe.com/us/pricing (US-language request), n.d., accessed 2026-11].
- Netherlands standard: "1.5% + €0.25 for standard European Economic Area cards", "2.8% + €0.25 for premium European Economic Area cards", "2.5% + €0.25 for UK cards", "3.15% + €0.25 for international cards", "+ 2% if currency conversion is required"; Klarna "Starting at 2.99% + €0.35" [VERIFIED: https://stripe.com/en-nl/pricing, n.d., accessed 2026-11].
- IC+ is a custom-pricing item, not a published rate: the custom column lists "IC+ pricing", "Volume discounts", "Multi-product discounts", "Country-specific rates", and the page's enterprise section offers "IC+ pricing, discounted flat rates, subscriptions, and buy-rates for platforms." [VERIFIED: both Stripe pricing pages]. Stripe's own definition: "A pricing plan where businesses pay the variable network cost for each transaction plus the Stripe fee rather than a flat rate for all transactions." [VERIFIED: Stripe extended-authorization page].
- Items priced separately for custom-pricing accounts but "Included at no additional charge for businesses on standard payments pricing": 3-D Secure at "€0.03 per 3D Secure attempt for accounts with custom pricing" [VERIFIED: Stripe NL pricing page].
- Stripe's public markup under IC+ is not published; nothing found.

**Adyen.**

- Structure: "For each transaction, we charge a fixed processing fee + a fee determined by the payment method." Visa and Mastercard: "$0.13" processing fee plus "Interchange+ + 0.60%" (the page prints the first plus sign of "Interchange++" as a separator). "Interchange fees are variable, our Interchange++ pricing passes these fees directly to you, giving you more transparency and lower fees overall." [VERIFIED: https://www.adyen.com/pricing and https://www.adyen.com/payment-methods/visa, n.d., accessed 2026-11].
- Some countries show different card rows, e.g. "$0.13 + 0.80% + Interchange++", "$0.13 + DKK 1 + Interchange++" for Denmark, "$0.13 + NOK 1.40 + Interchange++"; American Express appears at a blended "$0.13 + 0.80% + 3.95%" in one region [VERIFIED: Adyen pricing page; the country for the 0.80% rows could not be read from the static HTML].
- "Interchange++ is a pricing model which accurately tracks Interchange rates and scheme fees right down to a transaction level. This means we can calculate the cost of each payment even before it is completed." [VERIFIED: Adyen pricing page].
- "We do not have monthly fees, set-up fees, integration fees or closure fees. We do have a minimum invoice depending on industry or business model." "The fees outlined above are indicative; please get in touch to discuss pricing options." [VERIFIED: same].

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Default public price for cards | Blended, per country | Interchange++ plus fixed fee plus percentage markup |
| The other model | IC+ by negotiation ("custom") | Blended rows appear for some methods (Amex, BNPL, local methods) |
| Markup shown publicly | No (blended only) | Yes: 0.60% + $0.13, "indicative" |
| Minimum commitment | None stated for standard pricing | "a minimum invoice depending on industry or business model" |
| Features tied to pricing model | Five authorization and capture features are "IC+ features" (2.4) | None found |
| Dispute fee | Public (€20 / $15) | Not public |
| Declined, refunded, disputed payments | "per successful transaction"; original fees not returned on refund | Processing fee per transaction; refund fee column |

- **The difference the evidence supports.** Stripe's public default bundles interchange, scheme fees and margin into one number and charges only successful transactions, which makes a decline free to the merchant and a network penalty invisible; Adyen's public default passes network costs through, so the merchant sees them and Adyen's revenue is the markup. EU law makes the unblended form the default the acquirer must *offer* (5.2, Art. 9); Stripe's EU blended pricing presumably relies on the merchant's request or agreement, which is the analyst's reading, not a statement Stripe makes on the pages fetched [ASSUMPTION/JUDGEMENT]. That the two-tier EEA price (1.5% standard, 2.8% premium) reflects the IFR's consumer cap versus uncapped commercial cards is also inference [ASSUMPTION/JUDGEMENT].

### 5.7 How each reports revenue and volume ⚠

**Adyen (listed; reports twice a year).**

- **H1 2026** (published 13 August 2026): "Net revenue was €1,302.9 million, up 19% year-on-year (YoY) (21% on a constant currency basis). Processed volume was €803.8 billion, up 24% YoY. EBITDA was €641.5 million, with an EBITDA margin of 49%, or 50% excluding one-time transaction costs." [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne, published 2026-08-13].
- **Take rate, H1 2026**: "Take rate landed at 16.2 bps, reflecting expected volume tiering as enterprise merchants process at larger scale on our infrastructure." "In-person payments now represent 22% of total volume" (€175.7 billion) [VERIFIED: Adyen H1 2026 Shareholder Letter (PDF linked from https://investors.adyen.com/financials/h1-2026-c2a1a), published 2026-08-13].
- **Full year 2025** (published 12 February 2026): "Net revenue was €2,364.2 million, up 18% YoY, or 21% on a constant currency basis. Processed volume was €1,394.3 billion, up 21% excluding a single large-volume customer, or 8% YoY including this customer." "EBITDA was €1,245.7 million ... with EBITDA margin landing at 53% for the full year, compared to 50% in 2024." Point-of-sale volumes "€311 billion, up 34%" [VERIFIED: https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2, published 2026-02-12].
- **Derived take rate, FY2025**: €2,364.2 million ÷ €1,394.3 billion = **17.0 bps**; H2 2025 alone €1,270.7 million ÷ €745.3 billion = 17.0 bps [ASSUMPTION/JUDGEMENT: analyst arithmetic from the verified figures; Adyen's own FY2025 take-rate statement was not fetched].
- **What "net revenue" is.** Net revenue is "Net non-interest revenue ("Non-interest revenue" less "Costs incurred from financial institutions" and "Costs of goods sold") and Net interest income". H1 2026 composition: settlement fees €866.8 million, processing fees €321.6 million, sales of goods €62.5 million, other services €194.4 million; costs incurred from financial institutions €94.7 million. Those costs are fees "that do not form part of the pass-through settlement fees", and "Principal versus agent for revenue out of settlement fees" is listed as a material accounting judgement [VERIFIED: Adyen H1 2026 Shareholder Letter, 2026-08-13]. So in the current statements, interchange and scheme fees passed through to merchants are not in Adyen's revenue line at all. Adyen's earlier statements showed a much larger gross revenue with pass-through costs deducted; when and how the presentation changed was not verified in this session [ASSUMPTION/JUDGEMENT; check the FY2025 annual report].
- Pillars, H1 2026: Digital €719.7 million (+13%), Unified Commerce €417.7 million (+25%), Platforms €165.5 million (+37%) [VERIFIED: Adyen H1 2026 Shareholder Letter].
- Guidance: "We expect 2026 net revenue growth of 21% to 23% YoY on a constant currency basis, including the contribution of the acquisitions completed on July 1, 2026"; "EBITDA margin above 55% by 2028" [VERIFIED: Adyen H1 2026 press release].

**Stripe (private; reports once a year by letter).**

- "Last year, businesses running on Stripe generated $1.9 trillion in total volume, up 34% from 2024, and equivalent to roughly 1.6% of global GDP." "Stripe remained robustly profitable". The "Revenue suite ... is on track to hit an annual run rate of $1 billion this year." [VERIFIED: Stripe 2025 annual letter (PDF linked from https://stripe.com/en-nl/annual-updates/2025), published 2026-02-24].
- Stripe publishes **no revenue, net revenue or take rate**. "Total volume" is company-reported and its definition (which products, gross or net of refunds) is not given in the passages read [VERIFIED as an absence in the letter passages searched; ASSUMPTION/JUDGEMENT that no figure exists elsewhere].

| Aspect | Stripe | Adyen |
| --- | --- | --- |
| Volume | $1.9 trillion "total volume", calendar 2025, +34% | €1,394.3 billion "processed volume", 2025; €803.8 billion in H1 2026, +24% |
| Revenue | Not published | Net revenue €2,364.2 million (2025); €1,302.9 million (H1 2026) |
| Take rate | Not computable from public figures | 16.2 bps (H1 2026, stated); about 17.0 bps (2025, derived) |
| Profit | "robustly profitable" (no number) | EBITDA margin 53% (2025), 49% (H1 2026) |
| Audit status | Unaudited letter | Audited annual statements; H1 letter "unaudited" |

- **Do not compare the two volumes as like for like.** They are different currencies, different definitions and different customer mixes; Adyen's 2025 growth is also distorted by "a single large-volume customer" [VERIFIED: Adyen H2 2025 press release]. Any Stripe take rate in the book must be labelled an estimate with its source [ASSUMPTION/JUDGEMENT].

### 5.8 An illustrative fee stack on €120 (for the Larkfield thread)

[ASSUMPTION/JUDGEMENT: illustrative arithmetic from published list prices; real contracts differ, scheme fees are not public, and a USD fee is converted approximately.]

| Component | Stripe (Netherlands standard pricing) | Adyen (indicative public pricing) |
| --- | --- | --- |
| Interchange (consumer debit, EEA: max 0.2% = €0.24; consumer credit: max 0.3% = €0.36) | Inside the blended rate | Passed through: €0.24 or €0.36 |
| Scheme fees | Inside the blended rate | Passed through: not public |
| Provider markup | Inside the blended rate | 0.60% = €0.72, plus $0.13 (about €0.11–0.12) |
| Total merchant charge | 1.5% + €0.25 = **€2.05** (standard EEA card); 2.8% + €0.25 = €3.61 (premium EEA card) | About **€1.07–€1.20 plus scheme fees** |
| If the payment is refunded | Fee not returned | Processing fee kept; refund fee may apply |
| If it is disputed | + €20 received, + €20 if countered (returned on a win) | + chargeback fee (not public) |

The comparison says nothing about which provider is cheaper for a given business: Adyen's page states a minimum invoice and "indicative" prices, Stripe's IC+ terms are unpublished, and the blended rate includes products priced separately elsewhere.

**For readers new to payments.** *Interchange*: the per-transaction fee the acquirer pays the issuer, set by default by the network and capped by law for some cards. *Scheme fee*: what the network itself charges issuers and acquirers for processing and membership. *Acquirer markup*: the provider's own margin. *Blended pricing*: one percentage that covers all three. *Interchange++ (IC+)*: interchange and scheme fees passed through at cost with the markup shown separately. *Take rate*: a provider's net revenue divided by the volume it processed, usually in basis points (hundredths of a percent).

**Architecture implications** [ASSUMPTION/JUDGEMENT]. Pricing model decides what the provider's systems must compute and expose. Pass-through pricing requires the provider to calculate interchange and scheme fees per transaction ("even before it is completed", in Adyen's words), report them per transaction (IFR Art. 12), and reconcile them against what the networks later bill; blended pricing lets the provider absorb that variance and makes cost-reducing features (network tokens, retry suppression, timely capture) the provider's own margin lever rather than the merchant's. Stripe's decision to attach advanced authorization features to IC+ follows the same logic: features whose network cost varies per transaction are offered where that cost is passed on.

---

## PART 6: Material for the journeys (chapters 42 and 45)

### 6.1 Journey 42: a card payment from "pay" to settled

[ASSUMPTION/JUDGEMENT: the analyst's synthesis; each row points to the section holding the evidence.]

| # | Step | Party | Message or record | Promise made | Failure that can occur here | Evidence |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Authorization request | Provider → acquirer → network → issuer | Network authorization message (ISO 8583 family) | None yet | Timeout: outcome unknown to the merchant | 2.1, 2.5 |
| 2 | Issuer decision | Issuer (or network stand-in) | Response code, approval code | "I will honour this amount within the validity window" | Decline with a code and retry advice | 2.2, 2.6 |
| 3 | Hold | Issuer | Reduced available balance | Funds reserved | Customer sees a "charge" that is only a hold | 2.3 |
| 4 | Capture | Merchant → provider | Capture call; CAPTURE webhook (Adyen) | "I claim €120" | Authorization expired; capture fails later | 3.1, 2.3 |
| 5 | Clearing | Acquirer → network → issuer | Presentment (clearing record) | Final amount and data; interchange determined | Late presentment; downgrade; dispute right 11.3 | 3.2 |
| 6 | Settlement | Network settlement between members | Daily net settlement amount | Network guarantees members pay | Member failure (covered by network) | 3.3 |
| 7 | Funding | Provider | Balance becomes available; payable batch closes | "Your funds are available" | Reserve, negative balance, bank holiday | 3.4 |
| 8 | Payout | Provider → merchant bank | Bank transfer | Money in the merchant's account | Payout failure or return | 3.4; `ledger` brief |
| 9 | Dispute window | Cardholder via issuer | Dispute | None: the payment can still be taken back | Chargeback up to 120 days or longer | 4.2–4.5 |

### 6.2 Journey 45: the €120 dispute on each provider

[ASSUMPTION/JUDGEMENT: a worked sequence assembled from the verified behaviours in Part 4; the amounts use Stripe's Netherlands list fees; Adyen's fee is not public.]

| Stage | Stripe | Adyen |
| --- | --- | --- |
| Fraud report (optional) | An Early Fraud Warning object (Radar API); counts toward VAMP even if refunded | NOTIFICATION_OF_FRAUD; "no money is withdrawn" |
| Dispute arrives | Dispute object `needs_response`; balance debited €120 + €20 received fee | NOTIFICATION_OF_CHARGEBACK starts the defence period; CHARGEBACK books the debit and a chargeback fee "a few days after" |
| Deadline | `evidence_details.due_by` (network-dependent, "usually 7-21 days") | 18 days for Visa outside the US and Canada; 40 days for Mastercard |
| Evidence | One submission; countered fee €20 charged; status `under_review` | One submission via Customer Area or `/supplyDefenseDocument`; INFORMATION_SUPPLIED |
| While the issuer reviews | Funds stay debited | Collaboration and Mastercard: CHARGEBACK_REVERSED returns the funds provisionally; Allocation: funds stay debited |
| Issuer accepts | `won`; €120 and the countered fee return; received fee kept | Reversal becomes final |
| Issuer rejects | `lost`, or `appeal_needs_response` if appeals are enabled (appeal fee €20, network fees possible) | PREARBITRATION_OPEN where the flow has it; then SECOND_CHARGEBACK (final), plus up to USD 600 if scheme arbitration is lost |
| Monitoring effect | Counted in the month the dispute was received, whatever the outcome; twice on Visa if a TC40 also exists | Same network rule; visible in the Card monitoring programs tab |
| Late surprises | "Late win" from `lost` to `won` | Amex reopening; a new chargeback after issuer withdrawal "if the dispute timeframe still allows" |

---

## Key numbers

| Number | Value | Exact definition | Source and date |
| --- | --- | --- | --- |
| Visa CNP customer-initiated validity | 10 calendar days (30 with extended indicator) | Maximum processing timeframe from a valid authorization | Visa Core Rules Table 5-11, 2026-10-24 ⚠ |
| Visa card-present and MIT validity | 5 calendar days | Same | Same ⚠ |
| Stripe Visa CIT / MIT window | 7 days / 4 days 18 hours | Stripe's documented authorization validity, online | Stripe docs, accessed 2026-11 ⚠ |
| Adyen default authorization expiry | 28 days | Adyen-side automatic expiry, independent of scheme validity | Adyen docs, accessed 2026-11 |
| Visa Category 2 retry limit | 20 attempts in 30 days | Merchant reattempts after a "cannot approve at this time" decline (Adyen's page says 15) | Visa Core Rules Table 7-2, 2026-10-24 ⚠ |
| Stripe multicapture limit | 50 non-final captures | Per PaymentIntent | Stripe docs, accessed 2026-11 |
| Stripe incremental authorizations | 10 attempts | Per PaymentIntent | Stripe docs, accessed 2026-11 |
| Dispute initiation window | 120 calendar days (75 for Visa authorization conditions) | From transaction processing date; issuer's limit | Visa Core Rules ch. 11, 2026-10-24 |
| Outer dispute limit | 540 calendar days | "In some cases for Visa and Mastercard" | Adyen docs, accessed 2026-11 |
| Visa merchant response at Adyen | 9 days (US/Canada, from 21 July 2025) or 18 days | From notification of chargeback | Adyen docs, accessed 2026-11 ⚠ |
| Mastercard merchant response at Adyen | 40 days | From notification of chargeback | Adyen docs, accessed 2026-11 |
| VAMP acquirer thresholds | 50 bps Above Standard; 70 bps Excessive | (TC40 fraud + TC15 disputes) ÷ TC05 settled CNP transactions, monthly | Visa fact sheet, 2025 ⚠ |
| VAMP merchant Excessive | 150 bps from 1 April 2026 (220 bps before), with ≥1,500 cases | Same ratio; AP, Canada, EU, US | Visa fact sheet, 2025; Adyen and Stripe docs ⚠ |
| VAMP enumeration | 20% and 300,000 | Enumerated ÷ all authorizations; monthly count | Visa fact sheet, 2025 |
| Mastercard ECM / HECM | 100–299 and 1.5–2.99% / 300+ and 3% | Chargebacks this month ÷ captured payments last month | Stripe docs (rendering Mastercard), accessed 2026-11 ⚠ |
| EFW-to-dispute conversion | about 40% | Share of Visa and Mastercard early fraud warnings that become fraud disputes if not refunded | Stripe docs, accessed 2026-11 |
| EU interchange caps | 0.2% debit; 0.3% credit | Per-transaction cap, consumer cards, four-party schemes | Regulation (EU) 2015/751, 2015 (in force) |
| US debit cap | $0.21 + 0.05% + $0.01 | Maximum for covered issuers (≥ $10 billion assets) | Federal Reserve, page updated 2025-12-19 ⚠ (court ruling pending effect) |
| US debit interchange, 2024 | $0.23 covered (0.47%); $0.51 exempt (1.21%) | Average fee per transaction, all networks | Federal Reserve, 2025-12-19 |
| US credit settlement | −10 bps for 5 years; 1.25% cap for 8 years | Combined average effective credit interchange; standard consumer rate | Payments Dive, 2025-11-10 and 2026-06-09 ⚠ (not final) |
| Stripe card price, US | 2.9% + 30¢ | Per successful domestic card transaction, standard pricing | Stripe pricing, accessed 2026-11 ⚠ |
| Stripe card price, NL | 1.5% + €0.25 (standard EEA); 2.8% + €0.25 (premium EEA) | Per successful transaction, standard pricing | Stripe pricing (en-nl), accessed 2026-11 ⚠ |
| Stripe dispute fees | €20 received, €20 countered, €20 appealed (NL); $15 each (US) | Per dispute; countered fee returned on a win | Stripe pricing, accessed 2026-11 ⚠ |
| Stripe Smart Disputes fee | 30% | Of the disputed amount, on disputes won | Stripe pricing, accessed 2026-11 ⚠ |
| Adyen card price | $0.13 + Interchange++ + 0.60% | Indicative public price, Visa/Mastercard | Adyen pricing, accessed 2026-11 ⚠ |
| Adyen net revenue | €2,364.2 million (2025); €1,302.9 million (H1 2026) | Net non-interest revenue plus net interest income (non-IFRS) | Adyen, 2026-02-12 and 2026-08-13 |
| Adyen processed volume | €1,394.3 billion (2025); €803.8 billion (H1 2026) | Company-reported | Same |
| Adyen take rate | 16.2 bps (H1 2026, stated); about 17.0 bps (2025, derived) | Net revenue ÷ processed volume | Adyen H1 2026 letter; analyst arithmetic |
| Stripe total volume | $1.9 trillion (2025), +34% | Company-reported "total volume"; definition not given | Stripe annual letter, 2026-02-24 |
| Visa volume | $18 trillion | Total payments and cash volume, fiscal 2026 | Visa 10-K, 2026-11-05 |

## Open questions / not verifiable

1. **Mastercard's own rules.** Authorization validity (7 days final, 30 days pre-authorization), chargeback cycles and time limits, ECP thresholds and fines, Merchant Advice Codes and the stored-credential framework are known here only through Stripe and Adyen. The Mastercard Chargeback Guide and Transaction Processing Rules should be read before chapter 04 prints Mastercard deadlines as fact.
2. **Why Stripe documents 7 days where Visa allows 10** for customer-initiated online payments: not explained by Stripe.
3. **The 15-versus-20 retry limit**: Visa's October 2026 rules say 20 attempts in 30 days; Adyen's page says 15. Which date the limit changed is not established.
4. **Visa's 540-day outer dispute limit** and the name and date of "Visa Claims Resolution": not located in the rule text by search.
5. **Stand-in processing at the providers**: neither says whether an approval was a stand-in approval, nor what they do when an issuer is unreachable beyond returning a decline.
6. **Zero-value authorization on Stripe**: whether a SetupIntent performs a network account verification is not stated on the pages read.
7. **Whether a Stripe capture can fail asynchronously** at the network, as Adyen's CAPTURE_FAILED shows is possible.
8. **Settlement mechanics**: cut-off times, cycles per day, settlement banks and currencies for Visa and Mastercard are not in the public texts read; whether Stripe or Adyen pre-funds payouts before network settlement is not public.
9. **Adyen's chargeback and refund fees**, and Adyen's actual (non-indicative) markup; **Stripe's IC+ markup**. None is public.
10. **Stripe's revenue and take rate**: not published. The definition of "total volume" is not given.
11. **When Adyen moved to presenting pass-through settlement fees outside revenue** (the gross-to-net presentation): not verified; check the FY2025 annual report.
12. **Regulation II**: whether the Eighth Circuit's mandate has issued, whether rehearing or certiorari was sought, the Sixth Circuit's decision, and any new Federal Reserve rulemaking. The court opinion itself was not read.
13. **US merchant settlement**: the outcome of the reported 16 November 2026 final-approval hearing; the source of the "USD 38 billion" figure; the exact card categories merchants may decline.
14. **Ethoca Alerts and Verifi CDRN and Order Insight** from their owners' current pages; Adyen's support for Ethoca.
15. **Stripe and Adyen on US debit routing** (least-cost routing): nothing found in this brief's scope; see the `optimization` brief.
16. **UK interchange after Brexit** and cross-border EEA–UK rates: not researched.
17. **Visa's Merchant Elevated Risk Program** (Asia Pacific, October 2026): known only from Stripe's page; no Visa document found.

## Source list

**Card networks and standards**

- *Visa Core Rules and Visa Product and Service Rules*, Visa, 24 October 2026. https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf. Validity timeframes (Table 5-11), reversal timing (Table 5-13), stored credentials (Table 5-21), decline categories and retry limits (Table 7-2), dispute conditions and time limits (chapter 11), glossary definitions.
- *Visa Acquirer Monitoring Program Overview* (fact sheet), Visa, 2025. https://corporate.visa.com/content/dam/VCOM/corporate/visa-perspectives/security-and-trust/documents/visa-acquirer-monitoring-program-fact-sheet-2025.pdf. VAMP formula and thresholds.
- *Form 10-K for the fiscal year ended 30 September 2026*, Visa Inc., filed 5 November 2026. https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm. Four-party model, default interchange, settlement indemnification, volumes, litigation and regulation status.
- *Form 10-K for the year ended 31 December 2025*, Mastercard Incorporated, filed 11 February 2026. https://www.sec.gov/Archives/edgar/data/1141391/000114139126000013/ma-20251231.htm. Four-party model, default interchange, settlement guarantee.
- *ISO 8583: The message standard behind card authorisations*, Stripe, updated 18 September 2026. https://stripe.com/en-nl/resources/more/iso-8583. Message structure, limits, relation to ISO 20022.
- *10 Facts for Success with Rapid Dispute Resolution* and *Visa + Verifi*, Verifi (a Visa company), n.d. https://www.verifi.com/10-facts-for-success-rdr.html, https://www.verifi.com/rdr-is-here.html. RDR mechanism (vendor marketing, dated).

**Regulators and legal texts**

- *Regulation (EU) 2015/751 on interchange fees for card-based payment transactions*, European Parliament and Council, 29 April 2015 (OJ L 123, 19 May 2015). http://publications.europa.eu/resource/celex/32015R0751. Caps, scope, unblending, separation, per-transaction information, application dates.
- *Regulation II (Debit Card Interchange Fees and Routing)*, Federal Reserve Board, page updated 17 May 2024. https://www.federalreserve.gov/paymentsystems/regii-about.htm. Routing rule, enforcement.
- *Average Debit Card Interchange Fee by Payment Card Network*, Federal Reserve Board, updated 19 December 2025. https://www.federalreserve.gov/paymentsystems/regii-average-interchange-fee.htm. Cap formula, 2024 averages, dual- and single-message definitions.
- *Federal Reserve Board requests comment on a proposal to lower the maximum interchange fee...*, press release, 25 October 2023. https://www.federalreserve.gov/newsevents/pressreleases/bcreg20231025a.htm. 2023 proposal, $10 billion threshold.

**Stripe**

- Documentation (n.d., accessed 17 November 2026): https://docs.stripe.com/payments/place-a-hold-on-a-payment-method.md (validity windows, capture); /payments/extended-authorization.md, /payments/incremental-authorization.md, /payments/multicapture.md, /payments/overcapture.md (each with `?platform=web&ui=elements`), /payments/partial-authorization.md (authorization variants, IC+ gating); /payments/cits-and-mits.md (CIT/MIT); /payments/setup-intents.md; /declines.md, /declines/card.md, /declines/codes.md, /declines/network-codes.md (declines); /refunds.md; /disputes/how-disputes-work.md, /disputes/responding.md, /disputes/arbitration.md, /disputes/categories.md, /disputes/prevention-preview.md, /disputes/smart-disputes.md, /disputes/monitoring-programs.md, /disputes/measuring.md, /api/disputes/object.md (disputes); /payouts.md, /payments/balances.md (funding); /payments/analytics/optimization.md (network cost optimisations).
- *Pricing*, Stripe, n.d. https://stripe.com/en-nl/pricing and https://stripe.com/us/pricing. Card rates, dispute fees, IC+ as custom pricing.
- *Stripe 2025 annual letter*, Patrick and John Collison, 24 February 2026. https://stripe.com/en-nl/annual-updates/2025 (PDF at assets.stripeassets.com). Total volume, growth.

**Adyen**

- Documentation (n.d., accessed 17 November 2026): https://docs.adyen.com/online-payments/adjust-authorisation.md (authorization types, validity); /online-payments/capture.md; /online-payments/cancel.md; /online-payments/reversal.md; /online-payments/refund.md; /online-payments/partial-authorizations.md; /online-payments/tokenization.md, /tokenization/create-tokens.md, /tokenization/make-token-payments.md; /development-resources/refusal-reasons.md; /development-resources/raw-acquirer-responses.md; /development-resources/raw-acquirer-responses/visa-integrity-fees.md; /risk-management/understanding-disputes/dispute-process-and-flow.md, /dispute-timeframes.md, /dispute-reason-codes.md; /risk-management/chargeback-guidelines/visa-chargebacks.md, /mastercard-chargebacks.md; /risk-management/manage-disputes.md; /risk-management/disputes-api.md; /risk-management/dispute-and-fraud-monitoring.md; /account/getting-paid.md.
- *Pricing*, Adyen, n.d. https://www.adyen.com/pricing; *Visa payment method*, https://www.adyen.com/payment-methods/visa. Interchange++ pricing, processing fee.
- *Adyen publishes H1 2026 financial results*, 13 August 2026. https://www.adyen.com/press-and-media/adyen-publishes-h1-2026-financial-results-3wjne. *H1 2026 Shareholder Letter*, https://investors.adyen.com/financials/h1-2026-c2a1a. Net revenue, volume, take rate, revenue composition.
- *Adyen publishes H2 2025 financial results*, 12 February 2026. https://www.adyen.com/press-and-media/adyen-publishes-h2-2025-financial-results-3pgu2. Full-year 2025 figures.

**Secondary sources**

- *Eighth Circuit invalidates Federal Reserve's 21-cent debit card interchange fee cap...*, Consumer Finance Monitor (Ballard Spahr), 28 October 2026. https://www.consumerfinancemonitor.com/2026/10/28/eighth-circuit-invalidates-federal-reserves-21-cent-debit-card-interchange-fee-cap-holding-that-the-durbin-amendment-requires-a-transaction-specific-cost-analysis/. Law-firm briefing on *Corner Post*.
- *Eighth Circuit affirms vacatur of Regulation II*, ABA Banking Journal, 3 November 2026. https://bankingjournal.aba.com/2026/11/eighth-circuit-affirms-vacatur-of-regulation-ii/. Trade association journal.
- *Visa, Mastercard reach legal pact with merchants*, Payments Dive, 10 November 2025. https://www.paymentsdive.com/news/visa-mastercard-reach-legal-pact-with-merchants/805137/. Settlement terms.
- *Court approves Visa-Mastercard settlement*, Payments Dive, 9 June 2026. https://www.paymentsdive.com/news/court-approves-visa-mastercard-settlement/822440/. Preliminary approval.
- *Retailers object to interchange fee settlement*, Supermarket News, 14 September 2026. https://www.supermarketnews.com/grocery-operations/retailers-object-to-interchange-fee-settlement. Objection.
