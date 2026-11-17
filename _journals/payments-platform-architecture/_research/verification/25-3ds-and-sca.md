# Verification — 25-3ds-and-sca (`three-d-secure-and-sca`)

Verification pass of 17 November 2026. Every source in the page's Sources section was fetched in this session: Stripe and Adyen documentation as `.md`; the Stripe pricing page, the Stripe support article, the three Adyen press and knowledge-hub pages, the Visa press release and the EMVCo page as HTML; the EBA/ECB report as PDF (text extracted with `pdftotext`); PSD2 and Delegated Regulation 2018/389 from `http://publications.europa.eu/resource/celex/<CELEX>` (served as the Official Journal XHTML when the request carries `Accept: application/xhtml+xml` and `Accept-Language: en`; a request without a language returns HTTP 400, and EUR-Lex itself returns HTTP 202 to a script); the two European Parliament procedure files; and five Council documents on `data.consilium.europa.eu`. Each quotation was compared with the fetched text by script after normalizing typographic quotes and markdown marks, and the surrounding passage was read. "Not public" and "I found no" statements were tested against `https://docs.stripe.com/llms.txt`, `https://docs.adyen.com/llms.txt` and two web searches.

Source keys: S-flow = docs.stripe.com/payments/3d-secure/authentication-flow; S-ex = …/payments/3d-secure/strong-customer-authentication-exemptions; S-rules = …/radar/rules; S-risk = …/radar/risk-settings; S-alone = …/payments/3d-secure/standalone-3d-secure; S-sca = …/strong-customer-authentication; S-hold = …/payments/place-a-hold-on-a-payment-method; S-decl = …/declines/codes; S-save = …/payments/save-and-reuse; S-data = …/payments/3d-secure/data-only; S-price = stripe.com/en-nl/pricing; S-plans = docs.stripe.com/radar/how-radar-works; S-auth = support.stripe.com/questions/stripe-authentication; A-ex = docs.adyen.com/online-payments/psd2-sca-compliance-and-implementation-guide/sca-exemptions; A-oos = …/business-models/out-of-scope-transactions; A-d3ds = docs.adyen.com/risk-management/dynamic-3d-secure; A-auth = docs.adyen.com/online-payments/authentication; A-3ds = …/online-payments/3d-secure; A-reg = …/online-payments/3d-secure-for-regulation-compliance; A-data = …/online-payments/3d-secure/data-only; A-tok = …/online-payments/tokenization/make-token-payments; A-create = …/online-payments/tokenization/create-tokens; A-rc = …/online-payments/build-your-integration/payment-result-codes; A-native = …/online-payments/3d-secure/native-3ds2; A-alone = …/online-payments/3d-secure/standalone-authentication; A-disp = docs.adyen.com/risk-management/manage-disputes; A-apple = docs.adyen.com/payment-methods/apple-pay; A-pass = …/online-payments/authentication/scheme-passkeys; A-jp = docs.adyen.com/industries/markets/japan/credit-card-security-guidelines-compliance-guide; A-au = docs.adyen.com/online-payments/auspaynet-compliance-guide; A-pr1 = adyen.com/press-and-media/adyen-launches-authenticate-upgrade; A-pr2 = adyen.com/press-and-media/adyen-visa-payment-passkey; A-psd3 = adyen.com/knowledge-hub/psd3; PSD2 = publications.europa.eu/resource/celex/32015L2366; RTS = publications.europa.eu/resource/celex/32018R0389; OEIL = oeil.europarl.europa.eu procedure files 2023/0210(COD) and 2023/0209(COD); COUNCIL = data.consilium.europa.eu documents ST 8535/1/26 REV 1 ADD 1, ST 8543/26 ADD 1 REV 1, ST 14798/26, ST 14536/26, ST 15730/26; EBA = ecb.europa.eu/press/intro/publications/pdf/ecb.ebaecb202512.en.pdf; EMV = emvco.com/emv-technologies/3-d-secure/; VISA = usa.visa.com press release 20686.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Key point: Stripe cannot guarantee a flow "because the issuer determines the ultimate authentication flow" | S-flow | confirmed | No edit |
| 2 | Key point: reference rates 0.13%, 0.06%, 0.01% for €100, €250, €500 | RTS (Annex) | confirmed | Annex: EUR 100 0,13; EUR 250 0,06; EUR 500 0,01 for remote card-based payments |
| 3 | Key point: "Scheme passkeys are pilots" | A-pass, A-pr2 | hedged | Adyen's documentation says pilot; its press release of 29 October 2026 announces a first rollout in the UK. Now "in pilot or first rollout" |
| 4 | Key point and take-away: PSD3 and the PSR not adopted on 17 November 2026 | OEIL, COUNCIL | confirmed | See rows 104–106 |
| 5 | PSD2 defines SCA: "an authentication based on the use of two or more elements … reliability of the others" | PSD2 Art. 4(30) | confirmed | Character match on the EU text. The definition continues ("and is designed in such a way as to protect the confidentiality of the authentication data"); the quotation stops before it, which is fair |
| 6 | Article 97 applies when the payer "initiates an electronic payment transaction" | PSD2 Art. 97(1)(b) | confirmed | No edit |
| 7 | The duty sits on payment service providers | PSD2 Art. 97(1) | confirmed | "a payment service provider applies strong customer authentication"; "in practice the issuer" is the author's gloss |
| 8 | The standards "shall apply from 14 September 2019" | RTS Art. 38(2) | confirmed | No edit |
| 9 | The standards address "payment service providers" | RTS Arts. 13–18 | confirmed | Each exemption begins "Payment service providers shall be allowed not to apply" |
| 10 | Low value: "does not exceed EUR 30"; total not over EUR 100 or no more than five payments | RTS Art. 16 | confirmed | No edit |
| 11 | Trusted beneficiary: list held by the payer's own bank, created with SCA | RTS Art. 13 | confirmed | No edit |
| 12 | TRA conditions: fraud rate at or below reference, amount within band, real-time analysis finds nothing abnormal | RTS Art. 18(2) | confirmed | No edit |
| 13 | Article 18: "the fraud rate for that type of transaction, reported by the payment service provider" | RTS Art. 18(2)(a) | confirmed | No edit |
| 14 | Article 20: "shall immediately cease to make use of the exemption" … "where their monitored fraud rate exceeds for two consecutive quarters the reference fraud rate" | RTS Art. 20(2) | confirmed | No edit |
| 15 | Stripe: "EEA merchants have access to TRA exemptions for qualifying low risk transactions up to 250 EUR" | S-ex | confirmed | "EEA" now expanded where it first appears |
| 16 | Stripe: the limit "depends on the Stripe overall fraud rates" | S-ex | confirmed | No edit |
| 17 | Adyen publishes no TRA ceiling | A-ex, A-d3ds, A-auth, sca-options page, Adyen llms.txt | confirmed as far as searched | No amount on any page read |
| 18 | A merchant-initiated payment is outside the rule; Article 14 quotation | RTS Art. 14(1); EBA | hedged | The quotation matches, but Article 14 covers a series "with the same amount and with the same payee" and the standards do not name merchant-initiated payments. The sentence now says so and adds the regulators' own description ("a previously existing mandate that requires the application of SCA when the mandate is granted") |
| 19 | Stripe: such payments "technically fall outside the scope of SCA" | S-ex | confirmed | No edit |
| 20 | Adyen: "The initial transaction should have gone through SCA and the shopper should have agreed to the terms and conditions of the succeeding MITs." | A-oos | confirmed | No edit |
| 21 | EBA/ECB report: "In 2024, around 29% of remote card payments without SCA were exempted under TRA" | EBA | confirmed | No edit to the quotation |
| 22 | MIT "amounted to 22% in 2024"; "26% of remote transactions were reported as being outside the scope of SCA requirements under PSD2" | EBA | confirmed | No edit to the quotations |
| 23 | "that is about three quarters of remote card payments made without strong authentication", after "These exits carry a large share of traffic" | EBA (text and Chart 14) | corrected | The three figures are shares of remote card payments **without** SCA (Chart 14: "in % of total non-SCA card payments"), not of all remote card payments. The lead sentence and the summing sentence were reworded to say so |
| 24 | "fraud rates for card payment transactions authenticated with SCA were consistently and substantially below fraud rates for card transactions without SCA" | EBA | confirmed | No edit |
| 25 | Report identity: EBA/REP/2025/40, December 2025, 2024 data | EBA cover | confirmed | No edit |
| 26 | EMVCo: "EMV 3DS enables the exchange of data, or messages, between the merchant and the issuer to authenticate the consumer and approve the transaction." | EMV | confirmed | No edit |
| 27 | Three components: 3DS server, directory server, access control server | S-alone; A-3ds | confirmed | Stripe names the DS and the ACS; the 3DS server on the merchant's side is named on S-flow ("our optimized 3DS server") |
| 28 | Stripe: "Stripe communicates with the card network's DS and the issuer's Access Control Server (ACS)." | S-alone | confirmed | The page's URL changed; see row 121 |
| 29 | Stripe: "Major card brands no longer support 3D Secure 1" | S-flow | confirmed | No edit |
| 30 | Stripe standalone API ends with "On success, extract the cryptogram, ECI, and DS Transaction ID" | S-alone | confirmed | No edit |
| 31 | The EMVCo specification was not read | — | confirmed | A statement of limits; the specification was not read in this pass either |
| 32 | Adyen: "In a frictionless flow, the acquirer, issuer, and card scheme exchange all necessary information … without further shopper interaction." | A-3ds | confirmed | No edit |
| 33 | Adyen: "In a challenge flow, the issuer requires additional shopper interaction, either through biometrics, two-factor authentication, or similar methods" | A-3ds | confirmed | No edit |
| 34 | Stripe: "Stripe can't guarantee your preference because the issuer determines the ultimate authentication flow." | S-flow | confirmed | No edit |
| 35 | Stripe: "The PaymentIntent transitions to a status of `requires_action`"; client reads `next_action` | S-flow | confirmed | No edit |
| 36 | Adyen returns an `action` object with result codes such as `ChallengeShopper` | A-native, A-rc | confirmed | Neither page was in Sources; both added |
| 37 | Table: if 3-D Secure is unavailable or errors, "the payment proceeds normally" and liability "doesn't generally shift to the issuer" | S-flow | confirmed | No edit |
| 38 | PSD2 Article 74(2), two sentences quoted | PSD2 Art. 74(2) | confirmed | Character match |
| 39 | Stripe: "If 3DS authenticates a payment, the liability for any fraud-related disputes for that payment typically shifts from the seller to the issuer." | S-rules | confirmed | No edit |
| 40 | Table: Adyen, "the liability for fraudulent chargebacks shifts from you to the card issuer" (challenge) | A-reg | confirmed | No edit |
| 41 | Table: Adyen, "Both a successful challenge flow and a successful frictionless flow result in a liability shift"; "by network and region" | A-d3ds, A-reg | confirmed | A-reg: "In some regions, card schemes may grant liability shift after a successful frictionless flow" |
| 42 | Table: Adyen, requested exemption, "the chargeback liability stays with you" | A-ex | confirmed | Also the Mastercard table on A-reg: merchant- or acquirer-requested exemption, "No" |
| 43 | Table: Stripe, "liability shift for fraudulent transactions doesn't apply" | S-ex | confirmed | "When the customer's bank approves an exemption request" |
| 44 | Table: Stripe, merchant-initiated, "neither a customer challenge nor a liability shift occurs" | S-ex | confirmed | No edit |
| 45 | Table: Adyen, "there is no liability shift for the data-only flow" | A-data | confirmed | No edit |
| 46 | Table: Adyen, "Apple Pay supports liability shift for American Express, Discover, JCB, Mastercard, and Visa cards" | A-apple | confirmed | The page adds conditions (iOS version for Visa; Mexican cards through Prosa); "Usually the issuer" covers them |
| 47 | Adyen: an issuer-applied exemption, "The chargeback liability shifts to the issuer" | A-ex | confirmed | No edit |
| 48 | Adyen's Mastercard table: "Yes" where the "issuing bank applies a PSD2 exemption without the merchant or acquirer requesting for it" | A-reg | confirmed | Mastercard table, EU, from September 2019 |
| 49 | Stripe: "If the card issuer applies exemptions, the payment isn't authenticated through 3D Secure, and liability shift doesn't apply." | S-sca | confirmed | The reconciliation of rows 47 and 49 is labeled as the author's reading; left |
| 50 | Stripe: "Successful 3DS authentication doesn't guarantee liability shift." | S-flow | confirmed | No edit |
| 51 | Stripe: "an excessive level of fraud" and a monitoring program; the "no-reply" chargeback that "could invalidate the liability shift" | S-flow | confirmed | No edit |
| 52 | Adyen: "For Visa transactions, the chargeback protection is valid for 90 days" | A-reg | confirmed | The same page says 30 days for Mastercard, "Starting from 2020 … 90 days"; parts of that page are old |
| 53 | Adyen: "A card scheme can downgrade a payment's liability shift during authorization, even if the ECI value indicated a liability shift during authentication." | A-pass | hedged | The sentence is on the scheme-passkeys page, in the context of passkey payments; the text now says where it is |
| 54 | Stripe: "you authenticate the card when it's being saved" and "must also secure agreement from the customer" | S-ex | confirmed | No edit |
| 55 | Stripe: `setup_future_usage` set to `off_session`, or a SetupIntent | S-sca | confirmed | No edit |
| 56 | Adyen: first payment carries `shopperInteraction` **Ecommerce** and a `recurringProcessingModel` such as **Subscription** | A-create, A-tok | corrected | True, but **Ecommerce** is on "Create tokens", which was not in Sources; "Make token payments" has only the later payments. Source entry added |
| 57 | Adyen: "Zero-value authorizations to set up merchant-initiated transactions, for example subscriptions, do require SCA." | A-oos | confirmed | No edit |
| 58 | Stripe: "Set off_session to `true` when creating an off-session payment" | S-sca | confirmed | No edit |
| 59 | Adyen: later charges use `shopperInteraction` **ContAuth** | A-tok | confirmed | No edit |
| 60 | Stripe: "marking a payment as MIT is similar to requesting an exemption; neither a customer challenge nor a liability shift occurs" | S-ex | confirmed | No edit |
| 61 | Adyen's Mastercard table: "PSD2 SCA out-of-scope transactions that were not authenticated with 3D Secure 2", liability shift "No" | A-reg | confirmed | No edit |
| 62 | Stripe: "Exemptions aren't guaranteed, and off-session payments might still require authentication by the bank" | S-sca | confirmed | No edit |
| 63 | Stripe: "Stripe and the card network classify transactions as MIT or CIT based on signals of cardholder participation, not solely on API parameters like off_session" | S-hold | corrected | The quotation is exact, but it is on "Place a hold on a payment method", not on the CIT/MIT page the Sources section named (that page does not contain it). Source entry replaced |
| 64 | Stripe's decline codes include `authentication_required` | S-decl | confirmed | No edit |
| 65 | Adyen: "some issuing banks require SCA for **ContAuth** with **CardOnFile** transactions" | A-tok | confirmed | No edit |
| 66 | Adyen: "By requesting 3D Secure, you add friction. … you reduce fraud and obtain a liability shift." | A-d3ds | confirmed | No edit |
| 67 | Stripe's Dutch pricing page: "€0.03 per 3D Secure attempt for accounts with custom pricing" | S-price | hedged | The quotation matches, but the same line says 3-D Secure is "Included at no additional charge for businesses on standard payments pricing". Both are now quoted, and "a fee per attempt" became "on some contracts, a fee per attempt" |
| 68 | Adyen: risk-based authentication "increases authentication costs" | A-d3ds | confirmed | No edit |
| 69 | Regulators' report: remote card fraud rate in 2024 "0.091% in values" | EBA | confirmed | No edit |
| 70 | Adyen's table: low risk to an exemption, a frictionless flow or data-only; high risk to a challenge; the highest declined | A-auth | confirmed | Rows Low, High, Very high |
| 71 | Stripe's adaptive 3DS "runs machine learning in the background to authenticate medium-risk payments" | S-risk | confirmed | No edit |
| 72 | Adyen: "Send additional information in your payment request to maximize the probability of getting the exemption" | A-ex | hedged | The advice is given for the exemption an issuer applies on its own, not for frictionless authentication in general; the sentence now says so |
| 73 | Adyen: "By default, to optimize conversion, a transaction will use the frictionless flow if it is available." | A-d3ds | confirmed | No edit |
| 74 | Stripe's client library "collects basic device information during 3DS2 authentication and sends it to the issuing bank for their risk analysis" | S-flow | confirmed | Said of Stripe.js and both mobile SDKs |
| 75 | Adyen: "The issuer decides whether to grant the exemption" | A-ex | confirmed | No edit |
| 76 | "Soft decline" is the providers' shorthand, not a network term | ruling 15 | confirmed | Ruling applied in the page already |
| 77 | Stripe: "If requested by the issuer with a soft decline, we automatically reattempt and continue as if required." | S-flow | confirmed | No edit |
| 78 | Adyen: France, from 10 March 2025, "issuers will soft decline all customer initiated authorization exemptions except those requested via EMV 3DS" | A-reg | confirmed | Adyen attributes it to Banque de France guidance |
| 79 | Stripe: "Stripe's mandatory authentication rules run automatically, regardless of whether or not you manually request 3DS" | S-flow | confirmed | No edit |
| 80 | Stripe: "You can't use Stripe APIs to manually turn off 3DS." | S-flow | confirmed | No edit |
| 81 | Adyen: "we always authenticate transactions with 3D Secure if this is required by regulations such as PSD2" | A-d3ds | confirmed | No edit |
| 82 | "Stripe requests applicable SCA exemptions on your behalf" | S-ex | confirmed | No edit |
| 83 | "By default Adyen sends a request for the most suitable exemption type on your behalf." | A-ex | confirmed | No edit |
| 84 | Stripe: "The default method to trigger 3DS is using Radar … their own fraud engine." | S-flow | confirmed | No edit |
| 85 | Radar rule `Request 3D Secure if :risk_level: != 'normal' and :amount_in_usd: > 25` | S-rules | confirmed | No edit |
| 86 | Attributes `is_3d_secure`, `is_3d_secure_authenticated`, `has_liability_shift` | S-rules | confirmed | No edit |
| 87 | "Custom rules need the Radar Plus plan" | S-plans | corrected | Stripe's plan table marks custom rules as supported on Radar Plus **and** Radar Pro. Text and table cell now say "Radar Plus or Pro"; source entry added (the Radar rules page only says "If your Radar plan supports this feature") |
| 88 | `request_three_d_secure` states a preference (`any` or `challenge`); `authentication_flow` on the charge | S-flow | confirmed | No edit |
| 89 | Adyen: "When you create a new company account or merchant account, the default rule is set to **Prefer not**"; the alternative is **Always** | A-d3ds | confirmed | No edit |
| 90 | Adyen: "Rules are evaluated in order, from first to last." | A-d3ds | confirmed | No edit |
| 91 | Adyen: `additionalData.scaExemptionRequested` "containing the type of exemption" | A-ex | confirmed | No edit |
| 92 | Adyen: certain request parameters override its decisions, "reducing our ability to optimize the authentication flow" | A-auth | confirmed | No edit |
| 93 | Adyen: "From July 2026, Adyen is rolling out risk-based exemptions to select companies using Protect premium"; "boosting authorization rates by up to ten percent" | A-d3ds | confirmed | "Protect premium" now glossed. The figure stays labeled as Adyen's own claim |
| 94 | Adyen press release, 22 September 2026: "unlike legacy 3D Secure (3DS) providers, Adyen operates as both the authentication provider and the acquirer. … rather than authentication results alone." | A-pr1 | confirmed | Dateline "September 22nd, 2026" |
| 95 | Conversion gains of 11% and 12% at two merchants, testimonials without a method | A-pr1 | confirmed | Too Good To Go, "11% relative increase during the pilot"; Just Eat Takeaway.com, "12% increase in payment conversion on the eligible traffic" |
| 96 | Adyen's Authentication Engine "Selects the most appropriate authentication method, such as 3D Secure 2, scheme passkey authentication, or Google Secure Payment Authentication" | A-auth | confirmed | No edit |
| 97 | "I found neither the argument nor method selection in Stripe's documentation" | S-auth; Stripe llms.txt; web search | corrected | No design argument and no engine that selects among methods was found. But Stripe's support site describes Stripe Authentication, a device-verification method under delegated authentication, "currently being trialed". The sentence now says so |
| 98 | Both companies sell authentication on its own | S-alone, A-alone | confirmed | Adyen's "Standalone authentication" page was not in Sources; added |
| 99 | Table row 1: floor and default the same; Adyen default "Prefer not" | S-flow, S-ex, A-d3ds, A-ex | confirmed | No edit |
| 100 | Table row 2: Radar rules; Dynamic 3D Secure a separate ordered list that a risk rule can trigger | S-rules, S-plans, A-d3ds | corrected | Stripe cell: "Radar Plus or Pro" (row 87). Adyen cell confirmed (the risk-rule trigger needs Protect premium) |
| 101 | Table row 3: override per request | S-flow, A-auth | confirmed | No edit |
| 102 | Table row 4: Stripe up to 250 EUR, 220 GBP for UK and Swiss merchants; Adyen reports `scaExemptionRequested`, ceiling not public | S-ex, A-ex | confirmed | "Not public" tested on the Adyen pages read and the documentation index |
| 103 | Table row 5: methods beyond 3-D Secure, Stripe "Not public" | S-auth | corrected | Stripe documents one on its support site (row 97). The cell now states the fact; the last column was changed to match. Row 6 (stated design argument, Stripe "Not public") stands as far as searched |
| 104 | Parliament's Legislative Observatory shows both files at "Awaiting Parliament 2nd reading" | OEIL | confirmed | Read 17 November 2026: status of 2023/0210(COD) and 2023/0209(COD). The URL now redirects from `oeil.secure.europarl.europa.eu` to `oeil.europarl.europa.eu`; replaced |
| 105 | "Indicative plenary sitting date, 2nd reading" of 14 December 2026 | OEIL | confirmed | Forecast "14/12/2026" on both files |
| 106 | PSD3 and the PSR "were not adopted on 17 November 2026" | OEIL, COUNCIL | confirmed | True of the acts. Added what the Council pages show: the Council adopted its position at first reading at the end of October 2026 (statement of reasons 8535/1/26 REV 1 ADD 1: "Adopted by the Council on 29 October 2026"; the Commission communication ST 15730/26 gives 28 October; Coreper approved on 28 October per ST 14536/26); the Observatory lists "Council position published" on 5 November and the committee referral for second reading on 12 November. Source entry added |
| 107 | Adyen's reading, 12 October 2026: "SCA isn't going anywhere"; "Merchant-initiated transactions for recurring billing also stay as they are"; "The transaction risk analysis exemption remains but its qualifying conditions could change"; "Issuing banks can seek to recoup losses from acquirers" | A-psd3 | confirmed | Displayed date "October 12th, 2026"; labeled a secondary source |
| 108 | Adyen: "Whether a specific passkey flow qualifies as SCA will depend on the EBA's technical standards."; general application "around late 2028" | A-psd3 | confirmed | "EBA" now expanded at its first use |
| 109 | Other markets: UK, SCA under "the Payment Services Regulations 2017" (Adyen) | A-auth, A-3ds | corrected | The quotation is on the Authentication and 3D Secure 2 pages, not on the regulation-compliance page the Sources entry credited; entries corrected |
| 110 | Stripe's thresholds in pounds: 25, 85, 220 and 440 | S-ex | confirmed | No edit |
| 111 | India: "banks are required to perform authentication on all domestic ecommerce transactions" | A-reg | confirmed | No edit |
| 112 | Japan: SCA for online credit card payments "effective **April 01, 2025**" | A-jp | confirmed | No edit |
| 113 | Australia: both "More than AUD 50,000 in fraud losses" and "Fraud-to-sales ratio of 0.2% or above", two consecutive quarters | A-au | confirmed | No edit |
| 114 | United States, Canada: no mandate; data-only flows; a Visa program tying lower interchange to shared data (Stripe); "no liability shift" (Adyen) | S-data, A-data, A-auth | confirmed | Stripe: "In the United States and Canada, Visa has introduced specific interchange programs for transactions that qualify for DCAP". Adyen: data-only is offered "outside PSD2 SCA regulated markets". "No mandate" is the providers' account, as the paragraph says |
| 115 | Visa announced its Payment Passkey Service on 15 May 2024 | VISA | confirmed | Dateline "May 15, 2024" (2.5 years old; under the three-year flag) |
| 116 | Adyen press release, 29 October 2026: "Adyen will initially offer Visa Payment Passkey through Authenticate in the UK, with further enhancements and a global expansion planned for 2027." | A-pr2 | confirmed | Dateline "October 29th, 2026" |
| 117 | Adyen documentation: "Scheme passkeys are currently in pilot phase, and only enabled for a specific group of merchants"; "supported for Mastercard network tokenized transactions"; "You cannot enforce scheme passkey authentication" | A-pass | confirmed | No edit |
| 118 | "I found no Stripe page on scheme passkeys"; neither company documents authentication delegated to the merchant | Stripe llms.txt; web search; S-auth | hedged | No Stripe page on scheme passkeys was found. Stripe's support site does document delegated authentication to Stripe (Stripe Authentication, in trial); two sentences added with the quotations |
| 119 | Stripe: "payments stuck in an `incomplete` (Dashboard) or `requires_action` (API) status"; "Your customer might also have abandoned the checkout flow." | S-sca | confirmed | No edit |
| 120 | Stripe: use the declined payment's client secret "to allow the customer to authenticate the payment" | S-save | confirmed | No edit |
| 121 | Link: Stripe "Standalone 3DS" | S-alone | corrected | `…/standalone-three-d-secure` redirects to `…/standalone-3d-secure`; URL replaced in the page and the spec |
| 122 | Sources: PSD2 "published 2015-11-25" | PSD2 | corrected | 25 November 2015 is the date of the Directive; it was published in the Official Journal on 23 December 2015 (L 337/35). Entry now gives both |
| 123 | Sources: PSD2 and RTS quotations "re-read in the as-adopted copy at legislation.gov.uk" | PSD2, RTS | corrected | All quotations were matched against the Official Journal text served by the Publications Office of the EU at the cited addresses; the note now says so. The RTS entry lists only the articles the page uses |
| 124 | No public account of either company losing a TRA band | web search, documentation indexes | confirmed as far as searched | Stays labeled as following from the rule |
| 125 | Bram's payment: a €15.00 fee, stated without a label; "the studio loses the €120 and a dispute fee"; loss of €135.00 | A-disp; adyen.com/pricing; ledger | unsupported | No source gives Adyen's fee (its pricing page has no amount). The €15.00 is now labeled illustrative where it first appears, in the worked example and in the Larkfield section. See row 126 |
| 126 | Larkfield section: the loss "stayed on the merchant's side … €120.00 plus the €15.00 fee, €135.00" | A-disp | corrected | Adyen: "A chargeback fee is charged for every booked chargeback", and a reason to accept a dispute is "the risk of losing the chargeback fee for the second booked chargeback". €135.00 is therefore the debit of 24 February and the amount at stake, not a final loss, and a failed defense can cost a second fee. The paragraph now says this and quotes Adyen; source entry added |

Counts: 126 claims. Confirmed 107 (two of them "as far as searched"), corrected 12, hedged 6, unsupported and relabeled 1, unreachable 0.

## What could not be verified, and what was done

- **The EMVCo 3-D Secure specification** is behind a license and was not read. The page already says so and names no protocol messages.
- **Mastercard and Visa rule texts** on liability shift were not read (ruling 17). Every network rule in the page is cited as Stripe's or Adyen's account.
- **The agreed PSD3 and PSR texts** (PE787.673, PE787.675; Council 8535/26, 8543/26) were not read. The page presents the content as Adyen's reading, a secondary source.
- **The exact date of the Council's position** differs between Council documents (28 October in the Commission communication and the Coreper note; 29 October on the statement of reasons). The page says "at the end of October 2026" and quotes the statement of reasons.
- **Regulators' texts for the UK, India, Japan and Australia** were not read; the table says each row is the providers' account.
- **"Not public" for Stripe's design argument** (table row 6) rests on the pages read, the documentation index and two searches. It is true as far as searched.
- **Stripe Authentication** is described on Stripe's support site only; the article shows no date and names no networks or issuers. It is cited as "support site, n.d." and as a trial.
- **Adyen's regulation-compliance page** mixes current and old material (it still says Mastercard "will extend liability shift validity to 90 days" from 2020). Only the Visa window, the Mastercard table rows, France and India are taken from it.

## Larkfield consistency

- Dates, amounts, cards and names agree with the ledger (Mila: 12 January 2027 set-up, €49.00, Dutch Visa debit, renewals on the 1st, pass of 9 March 2027 by phone wallet; Bram de Wit: 2 February 2027, €120.00, Dutch Mastercard credit, chargeback 24 February 2027, €15.00 fee; Studio Noord on Adyen; April 2027 policy; 540,000 × €49 ≈ €26.5 million). No weekday is named in the page.
- Arithmetic checked: 3% × €120 ÷ €135 = 2.67%; 30 × €120 = €3,600; 0.5 × €135 = €67.50; 50 × €135 = €6,750.
- **Fixed in this page:** the lead and the closing said the studio "loses" the €120 and that "the loss fell on the studio". `journey-dispute` (which owns the outcome) has the dispute **won**, with a net loss of the €15.00 fee. The page now says the studio "is debited" and that "the dispute fell on the studio", and the Larkfield section gives €135.00 as what is lost "if the dispute is lost", which is the wording of this chapter's ledger line.

## Ledger conflicts

- None. The ledger's `25-3ds-and-sca` line ("the studio's loss if the dispute is lost is €135.00") and its `45-journey-dispute` line (a lost defense costs "€135.00 lost, plus possibly a second fee") agree once the page states €135.00 as conditional.

## For other pages

- `02-authorization` cites the "signals of cardholder participation" quotation from `docs.stripe.com/payments/place-a-hold-on-a-payment-method`, which is the right page; any page that credits it to the CIT/MIT page should be corrected.
- Any page that says Stripe documents no authentication method beyond 3-D Secure, or nothing on delegated authentication, should take account of `support.stripe.com/questions/stripe-authentication` (a trial, n.d.).
- Any page that gives PSD2's publication date as 25 November 2015 should say adopted 25 November 2015, published 23 December 2015.
- `payments-what-is-moving` (ch. 50) should carry the same PSD3 and PSR status: Council position at first reading adopted at the end of October 2026, published 5 November; Parliament's second reading indicatively 14 December 2026.
- Stripe's Dutch pricing page says 3-D Secure is included on standard pricing and costs €0.03 per attempt only on custom pricing; `payment-economics` should not present the €0.03 as a general fee.

## Format and rulings

- Ruling 22: no external URL in the running text (only the failure-patterns callout link). Rulings 14, 15, 17 and 30 were already applied.
- `[[permalinks]]`: all thirteen are in the style guide's valid list.
- Links: all 40 URLs in Sources return HTTP 200. Two were replaced with their redirect targets (rows 104 and 121). The two `publications.europa.eu/resource/celex/…` addresses redirect to the Official Journal copy when the request names a language, as a browser does.
- Sources: entries added for pages the text relies on (Stripe "Place a hold on a payment method", "How Radar works", "Stripe Authentication"; Adyen "Create tokens", "Result codes", "Native 3D Secure 2 authentication", "Standalone authentication", "Manage disputes"; the Council's statement of reasons). The CIT/MIT entry was removed because nothing in the text rests on it. The two sibling-book links under "Research and practitioner sources" are pointers for depth and are not cited in the text; left for the author.
- Terms: "EEA", "EBA" and "Protect premium" now expanded or glossed at first use.
- `timetoread` changed from 26 to 28 (6,404 words by `check_draft.py structure` ÷ 230 = 27.8). The spec's maximum is 6,500 words.
- No unit was added, dropped, merged or reordered. `validate_spec.py` and `check_draft.py structure` pass; the build and `render_check.py three-d-secure-and-sca` pass.
