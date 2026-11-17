# Verification — 02-authorization (`payment-authorization`)

Verification pass of 17 November 2026. Every source was fetched in this session (Stripe and Adyen pages as `.md`, the Visa rules PDF converted with pdftotext, the Visa 10-K from EDGAR, the Adyen OpenAPI file from GitHub). Quotations were compared with the fetched text by script after normalizing typographic quotes and markdown marks, and the surrounding passage was read for each.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Visa definition of Authorization (quote); edition 24 October 2026 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Inline link reduced to plain text (ruling 22) |
| 2 | Visa 10-K FY2026 quote on the authorization path; filed 2026-11-05 | https://www.sec.gov/Archives/edgar/data/1403161/000140316126000134/v-20260930.htm | confirmed | Sentence now says Form 10-K, filed November 2026 |
| 3 | Stripe ISO 8583 explainer: 'Each message is built from an MTI, a bitmap, and data elements'; updated 18 September 2026 | https://stripe.com/en-nl/resources/more/iso-8583 | confirmed | No edit |
| 4 | MTI is a four-digit number; bitmap marks which fields are present | same | confirmed | No edit |
| 5 | 'isn't self-describing'; each network keeps its own variant | same | confirmed | No edit |
| 6 | 'ISO 8583 still dominates card authorisation, even as ISO 20022 gains adoption on other payment systems' | same | confirmed | No edit |
| 7 | 'Businesses that use a payments provider such as Stripe don't have to build or manage these messages themselves' | same | confirmed | No edit |
| 8 | Adyen's API does not expose the ISO 8583 message | https://docs.adyen.com/llms.txt | hedged | No Adyen page states this; reworded to 'nothing on the Adyen pages read for this chapter exposes it' (index search for ISO 8583: no hits) |
| 9 | Visa response code '51 (Not sufficient funds)' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Table 7-2 |
| 10 | Stripe: 'Authorizing a payment guarantees the amount by holding it on the customer's payment method' | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 11 | Adyen: pre-authorization 'verifies that the shopper's account is valid ... but does not debit the account.' | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 12 | Stripe: statements 'don't always distinguish between authorizations and captured (settled) payments' | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 13 | Visa gives the acquirer a maximum number of days to process after approval | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Section 5.7.3.5 |
| 14 | A dispute can come for about 120 days | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Dispute time limits of 120 calendar days in chapter 11 of the rules; detail owned by another chapter |
| 15 | Stripe: 'When Stripe blocks a payment, it doesn't obtain authorization from the card issuer' | https://docs.stripe.com/declines | confirmed | No edit |
| 16 | Adyen refusal reason 20 FRAUD: 'The pre-authorization risk checks resulted in a fraud score of 100 or more.' | https://docs.adyen.com/development-resources/refusal-reasons | confirmed | No edit |
| 17 | Visa rule 7.3.6.3: issuer 'must send to VisaNet the Decline Response code that most accurately reflects the reason for the decline' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 18 | Stripe: 'Card issuers categorize most declines as generic (generic_decline), making the exact decline reason unclear.' | https://docs.stripe.com/declines/card | confirmed | No edit |
| 19 | Adyen: 'The most frequent refusal reason, 05: Do not honor, falls into this category.' | https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed | No edit |
| 20 | Visa sorts decline codes into four categories with reattempt limits | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Table 7-2 |
| 21 | Adyen's page says 15 retries in 30 days; the rule says 20 (ruling 19) | https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed | Adyen page still says 15 on 2026-11-17; Visa Table 7-2 says 20 |
| 22 | Mastercard Merchant Advice Codes, 'from 03 : Do not try again to 30 : Retry after 10 days' | https://docs.adyen.com/development-resources/raw-acquirer-responses | corrected | Both values exist, but Adyen's table runs from 01 to 43; 'from ... to' replaced by 'with values such as ... and ...' |
| 23 | Adyen: 'Not all Mastercard issuers return the MAC.' | https://docs.adyen.com/development-resources/raw-acquirer-responses | confirmed | No edit |
| 24 | Table 7-2 Category 1 'Issuer will never approve'; codes 04, 14, 46 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 25 | Category 1: 'a Merchant must never resubmit' for the same card | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Rule text: 'for the same Payment Credential' |
| 26 | Category 2 'Issuer cannot approve at this time'; codes 51, 91 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 27 | 'Reattempt permitted (up to 20 attempts in 30 days)' for Categories 2, 3 and 4 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 28 | Category 3 'Data quality'; codes 54, N7 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Added a one-clause gloss of CVV2 |
| 29 | Category 4 'All other Decline Response codes'; 05 by Adyen's page | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf ; https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed | No edit |
| 30 | Soft and hard decline are not terms in the Visa rule text (ruling 15) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Neither phrase appears as a defined term in the 24 October 2026 edition; Mastercard not readable |
| 31 | Stripe decline code `authentication_required` | https://docs.stripe.com/declines/codes | confirmed | No edit |
| 32 | Adyen reason 38 is 'Retry with 3D Secure' | https://docs.adyen.com/development-resources/refusal-reasons | corrected | Reason 38 is named 'Authentication required'; 'Retry with 3D Secure.' is the last sentence of its description. Sentence fixed |
| 33 | Stripe next step for `insufficient_funds`: 'The customer needs to use an alternative payment method' | https://docs.stripe.com/declines/codes | confirmed | No edit |
| 34 | Visa puts code 51 in Category 2 | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 35 | Stripe `decline_code` field, values `insufficient_funds`, `generic_decline` | https://docs.stripe.com/api/errors ; https://docs.stripe.com/declines/codes | confirmed | Field name was not on any listed source; Stripe API reference 'Errors' added to Sources |
| 36 | Stripe `network_decline_code`: 'The card network provides this 2-4 digit code' | https://docs.stripe.com/declines/card | confirmed | No edit |
| 37 | Stripe `network_advice_code` and `advice_code` values do_not_try_again, try_again_later, confirm_card_data | https://docs.stripe.com/declines/card | confirmed | No edit |
| 38 | Adyen `refusalReason`, `refusalReasonCode`; 12 'Not enough balance' | https://docs.adyen.com/development-resources/refusal-reasons | confirmed | No edit |
| 39 | Adyen `refusalReasonRaw` example '51 : Insufficient funds/over credit limit'; off until enabled in the Customer Area | https://docs.adyen.com/development-resources/raw-acquirer-responses | confirmed | No edit |
| 40 | Adyen `additionalData.merchantAdviceCode` for Mastercard; mapping of raw responses to Visa categories | https://docs.adyen.com/development-resources/raw-acquirer-responses | confirmed | No edit |
| 41 | Adyen: 'Visa charges system integrity fees. These fees are related to excessive retries of failed transactions' | https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed | No edit |
| 42 | Adyen reason 46: 'Transaction blocked by Adyen to prevent excessive retry fees' | https://docs.adyen.com/development-resources/refusal-reasons | confirmed | No edit |
| 43 | Stripe 'blocks a payment that would have incurred network retry penalties and likely failed' | https://docs.stripe.com/payments/analytics/optimization | confirmed | No edit |
| 44 | Stripe 'recommends a maximum of eight retries'; 'Card issuers might see creating additional retries as potential fraud' | https://docs.stripe.com/declines/card | confirmed | No edit |
| 45 | Fee amounts are not on the pages read | https://docs.adyen.com/development-resources/raw-acquirer-responses/visa-integrity-fees | confirmed | No amounts on the Adyen or Stripe pages fetched |
| 46 | Timeframe starts from 'a valid Authorization' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Table 5-11 footnote 1 |
| 47 | Table 5-11: card-absent cardholder-initiated 10 calendar days | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 48 | Table 5-11: 'with an extended Authorization indicator' 30 calendar days | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 49 | Table 5-11: estimated authorization at cruise line, lodging, vehicle rental 30 calendar days | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | The table also has a 10-day row for other rental merchants, not shown on the page |
| 50 | Table 5-11: card present 5 calendar days | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 51 | Table 5-11: all merchant-initiated transactions 5 calendar days | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 52 | Key point: '5 to 30 days under Visa's rules' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | hedged | True of the general Table 5-11 only; Table 5-12 has country-specific windows of 1 to 30 days. Key point now says 'in Visa's general table' and one sentence names Table 5-12 |
| 53 | Stripe: Visa customer-initiated online 7 days | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 54 | Adyen: Visa card-not-present customer-initiated 10 days | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 55 | Stripe's page gives no reason for 7 against 10 | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 56 | Stripe: Visa merchant-initiated 5 days; 'The exact authorization window is 4 days and 18 hours, to allow time for clearing processes.' | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 57 | Adyen: Visa merchant-initiated 5 days | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 58 | Stripe: Mastercard online 7 days | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 59 | Adyen: Mastercard 7 days final authorization, 30 days pre-authorization | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 60 | Stripe `capture_before` on the charge 'indicates when the authorization expires' | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 61 | Adyen: 'Adyen expires (pre-)authorization requests automatically after 28 days from the day the payment is authorized' | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | Source scopes it to 'the global card schemes' |
| 62 | Stripe: `capture_before` is 'the most reliable and accurate way to determine your charge's authorization window' | https://docs.stripe.com/payments/cits-and-mits | confirmed | No edit |
| 63 | Adyen pages read document no field equivalent to `capture_before` | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | True of the pages fetched; the full API reference was not searched field by field |
| 64 | Adyen `EXPIRE` webhook: payment 'has expired on the Adyen payments platform' | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | No edit |
| 65 | Stripe: 'If the authorization expires before you capture the funds, the funds are released and the payment status changes to canceled.' | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 66 | Adyen: late capture 'increases the risk of' failed capture, 'Increased interchange fees', 'Card scheme transaction fees', chargeback for 'No Authorization' or 'Late Presentment' | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 67 | Visa Dispute Condition 11.3 (No Authorization/Late Presentment) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Section 11.9.3 |
| 68 | Visa definition of Estimated Authorization Request (quote) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 69 | Adyen: final authorizations 'By default'; `additionalData.authorisationType` | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 70 | Visa: 'An Incremental Authorization Request does not extend the processing timeframes' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 71 | Stripe: 'a maximum of 10 incremental authorization attempts per PaymentIntent'; offered to users on IC+ | https://docs.stripe.com/payments/incremental-authorization | confirmed | Read in the '?platform=web&ui=elements' variant of the page |
| 72 | Adyen: 'authorization adjustment'; eligibility by merchant category code | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 73 | Visa definition of Partial Authorization (quote) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 74 | Stripe partial authorization: `request_partial_authorization`, `amount_authorized`; opt-in | https://docs.stripe.com/payments/partial-authorization | hedged | Confirmed, but the page also limits the feature to IC+ pricing; clause added |
| 75 | Adyen partial: `additionalData.allowPartialAuth`, result code `PartiallyAuthorised` | https://docs.adyen.com/online-payments/partial-authorizations ; https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes | confirmed | No edit |
| 76 | Visa definition of Account Verification (quote) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 77 | Visa: before storing a credential, an authorization or, 'If payment is not required', an Account Verification | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Table 5-21 |
| 78 | Adyen: 'We recommend that you store payment details by making a zero-auth transaction' | https://docs.adyen.com/online-payments/tokenization/create-tokens | confirmed | No edit |
| 79 | Stripe saves a card with a SetupIntent; the page does not say whether a zero-amount verification is sent | https://docs.stripe.com/payments/setup-intents | confirmed | No mention of a zero-amount message on the page; one-clause gloss of SetupIntent added |
| 80 | Visa definition of Authorization Reversal (quote) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 81 | Visa: reversal within 24 hours when a sale is not completed, or for the difference when the final amount is lower | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Table 5-13 |
| 82 | Stripe: canceling a PaymentIntent 'releases any held funds' | https://docs.stripe.com/payments/paymentintents/lifecycle | confirmed | No edit |
| 83 | Stripe uses 'reversal' for a refund issued shortly after the charge | https://docs.stripe.com/refunds | confirmed | No edit |
| 84 | Adyen: cancel before capture; the reversal cancels an uncaptured payment and refunds a captured one | https://docs.adyen.com/online-payments/cancel ; https://docs.adyen.com/online-payments/reversal | confirmed | No edit |
| 85 | Stripe definition of a merchant-initiated transaction (quote) | https://docs.stripe.com/payments/cits-and-mits | confirmed | No edit |
| 86 | Visa definition of Stored Credential (quote with ellipsis) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Source lists further parties (Agentic Payment Provider; Biometric Solution Provider from 24 April 2027) not quoted |
| 87 | Visa: cardholder agreement in writing before storing | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | Table 5-21 |
| 88 | Visa: 'If the initial Authorization Request or Account Verification is not approved, the Merchant must not store the credential.' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 89 | Visa: 'POS Entry Mode code 10' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 90 | Visa: declined merchant-initiated request, written notice and 'at least 7 calendar days to pay by other means.' | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | No edit |
| 91 | Stripe: 'Stripe and the card network classify transactions as MIT or CIT based on signals of cardholder participation, not solely on API parameters'; the `off_session` and CVC example | https://docs.stripe.com/payments/place-a-hold-on-a-payment-method | confirmed | No edit |
| 92 | Adyen `shopperInteraction` (Ecommerce, ContAuth) and `recurringProcessingModel` (CardOnFile, Subscription, UnscheduledCardOnFile) | https://docs.adyen.com/online-payments/tokenization/make-token-payments ; https://docs.adyen.com/online-payments/tokenization/create-tokens | confirmed | No edit |
| 93 | Adyen validity table: merchant-initiated row applies to 'ContAuth + Subscription / UnscheduledCardOnFile' | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | No edit |
| 94 | Nothing on the Adyen pages read says Adyen reclassifies | https://docs.adyen.com/online-payments/adjust-authorisation | confirmed | True of the pages fetched |
| 95 | Stripe: 'When a connection fails, you might not know whether Stripe received or executed the request.' | https://docs.stripe.com/error-low-level | confirmed | No edit |
| 96 | Stripe: 'Treat the outcome of a request that returns 500 as indeterminate ...' | https://docs.stripe.com/error-low-level | confirmed | No edit |
| 97 | Stripe: 'Retry with the same idempotency key and parameters within the first 24 hours after the original request.' | https://docs.stripe.com/error-low-level | confirmed | No edit |
| 98 | Stripe keeps keys 'for at least 24 hours' and returns the saved response | https://docs.stripe.com/error-low-level ; https://docs.stripe.com/api/idempotent_requests | confirmed | Scoped by Stripe to API v1 |
| 99 | Stripe: 'Don't retry with a new idempotency key until you've resolved the original outcome. Retrieve the relevant object' | https://docs.stripe.com/error-low-level | confirmed | No edit |
| 100 | Adyen Checkout API v72 specification has three GET operations, none returning a payment by reference | https://github.com/Adyen/adyen-openapi/blob/main/json/CheckoutService-v72.json | confirmed | Parsed the file: GET /paymentLinks/{linkId}, /sessions/{sessionId}, /storedPaymentMethods. v72 is the latest in the repository (v73 returns 404). Source URL now points at the file |
| 101 | Adyen: 'If you do not receive a response (for example, in case of a timeout), you can safely retry the request with the same HTTP header' | https://docs.adyen.com/development-resources/api-idempotency | confirmed | No edit |
| 102 | Adyen: keys 'are valid for a period of 7 to 14 days after first submission.' | https://docs.adyen.com/development-resources/api-idempotency | confirmed | No edit |
| 103 | Adyen: cancel by own reference 'up to 24 hours after authorization'; recommended only 'if you generate a unique references ...' (sic) | https://docs.adyen.com/online-payments/cancel | confirmed | The grammatical slip is Adyen's |
| 104 | Adyen reversal for when 'you are not sure if a payment has been captured' | https://docs.adyen.com/online-payments/reversal | confirmed | No edit |
| 105 | INFERENCE block: Adyen's page does not say cancel by reference was built for timeouts | https://docs.adyen.com/online-payments/cancel | confirmed | Correctly labeled as inference |
| 106 | Visa definition of Stand-In Processing (STIP) (quote) | https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf | confirmed | The source adds '(including Visa Smarter Stand-In Processing)' before the quoted part |
| 107 | Stripe's table of Visa codes glosses 91 as 'time-out when no stand-in' | https://docs.stripe.com/declines/network-codes | confirmed | No edit |
| 108 | With code 91 'you see Stripe's `issuer_not_available` or Adyen's reason 9' | https://docs.stripe.com/declines/codes ; https://docs.adyen.com/development-resources/refusal-reasons | hedged | Both reasons exist, but neither page ties them to Visa code 91; sentence now says so and labels the link as the author's reading |
| 109 | Neither provider says whether an approval came from stand-in | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | confirmed | Index search for stand-in, stand in, STIP: no hits on the acquiring side at either provider |
| 110 | Neither describes its handling of a timeout on its own call to the network, or its API-to-network translation | same | confirmed | True of the pages fetched for this chapter |
| 111 | Mastercard rules could not be read (ruling 17) | - | not checked | Not re-attempted in this pass; the page makes no Mastercard claim except through Stripe's and Adyen's pages, which were checked |
| 112 | Adyen: 'we recommend that you rely on the webhook to trigger any business logic' | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | No edit |
| 113 | Adyen result code `Authorised`, PSP reference, `AUTHORISATION` webhook | https://docs.adyen.com/online-payments/build-your-integration/payment-result-codes ; https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | No edit |
| 114 | Where They Differ, row 1: 7 days / 10 days | as above | confirmed | No edit |
| 115 | Where They Differ, row 2: `capture_before` / per-scheme table, 28 days, `EXPIRE` | as above | confirmed | No edit |
| 116 | Where They Differ, row 3: classification | as above | confirmed | No edit |
| 117 | Where They Differ, row 4: timeout resolution | as above | confirmed | No edit |
| 118 | Where They Differ, row 5: `network_decline_code` on the charge outcome / `refusalReasonRaw` once enabled | https://docs.stripe.com/declines ; https://docs.adyen.com/development-resources/raw-acquirer-responses | confirmed | No edit |
| 119 | Where They Differ, row 6: stand-in 'Not public' for both | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | confirmed | See the stand-in row above |
| 120 | Take-away: both providers document a same-key retry | as above | confirmed | No edit |
| 121 | Sources: every URL returns 200 without redirect | all 30 URLs | confirmed | One URL replaced by a more specific one (OpenAPI file) |
| 122 | Sources: entry titles match the pages | nine entries | corrected | Titles updated to the pages' current titles: Stripe decline codes; Increment an authorization; The Setup Intents API; How Payment Intents and Setup Intents work; Payments optimization; Authorization adjustment; Raw responses; Webhook structure and types; Result codes |

Counts: 122 rows; confirmed 114, hedged 4, corrected 3, not checked 1.

## Could not verify, and what was done

- **Mastercard's own rules** were not fetched (ruling 17 records them as unreachable). Every Mastercard statement on the page is attributed to Stripe's or Adyen's documentation, and those pages were checked.
- **ISO 8583 itself** is not read (sold by ISO); the page says so and relies on Stripe's explainer, which was checked.
- **Negative claims** ("the pages read do not say …", "Not public") were checked against the fetched pages and the two `llms.txt` indexes only. They are true of those; the full API references were not searched field by field.
- Stripe's incremental-authorization page is now an index of three variants; the quoted sentences are in each integration variant (the `ui=elements` variant was read).

## Format and rulings

- Ruling 22: the one inline external link (Visa Core Rules) was reduced to plain text; its URL is in Sources.
- `timetoread` corrected from 28 to 23 min (5,313 words ÷ 230).
- A doubled comma after `[[acquiring-and-network-connectivity]]` removed.
- Glosses added: CVV2, SetupIntent.
- No unit added, dropped, merged or reordered; `check_draft.py structure` passes; `validate_spec.py` passes; build and render check clean.
- No source is older than three years, so no evidence-age marks are needed.

## Larkfield consistency

Checked against the ledger: the Double Charge (1 November 2026; 1,840; €71,300; 212), the Renewal Wave (38%, 6 hours), Femke de Graaf (joined January 2027), Mila's pass (Tuesday 9 March 2027, 19:42, €120.00, Dutch Visa debit in a phone wallet, Studio Noord on Adyen, no challenge; ruling 14), the membership (€49.00, set up 12 January 2027 with a 3-D Secure challenge), the decline of 1 April and retry of 4 April 2027 (code 51, Category 2, reason 12), K1, K2, K5, and the `pending` state. 9 March 2027 is a Tuesday. 9 March + 10 days = 19 March; + 7 days = 16 March. No contradiction found.

## Ledger conflicts

None found.

## For other pages

- Any page that names Adyen refusal reason 38 should call it "Authentication required"; "Retry with 3D Secure" is its description, not its name.
- Any page citing Stripe partial authorization should note that Stripe's page limits it to IC+ pricing.
- Several Stripe and Adyen documentation pages carry different titles from the ones this page had (see the last table row); other pages citing the same URLs may have the old titles.
- Visa's Table 5-12 sets country-specific validity windows (India, Japan and others); pages that state "5, 10 or 30 days" as universal should say "general".
