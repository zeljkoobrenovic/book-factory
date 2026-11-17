# Verification — 23-network-tokens (`network-tokens`)

Verification pass of 17 November 2026. Every source below was fetched in this session (curl, user agent `Mozilla/5.0 (research-bot)`) and the passage read. Quotations were matched by script against the fetched text (typographic quotes and markdown link markup aside) and the misses read by hand.

Totals: **83 claims checked — 66 confirmed, 7 corrected, 10 hedged, 0 unsupported, 0 unreachable.**

Notes on fetching:

- `stripe.com` pages redirect by location to the Dutch locale (`/nl/`), which is translated. Quotations were checked on the English pages `stripe.com/en-nl/…` and `stripe.com/ie/…`, which carry the same text. The product page is now cited at its Irish address, because the page quotes its British spelling ("Authorisation Boost") and its euro price.
- `docs.stripe.com/api/charges/object.md` (the Markdown copy) does **not** contain `network_token`; the HTML page does (see claim 60).

## Claims

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe, 23 Feb 2023: "approximately 40% of cardholders replaced their cards…"; no source given; refers to 2022 | https://stripe.com/newsroom/news/network-tokens-card-account-updater | confirmed | — (displayed date 23 February 2023; evidence-age mark present) |
| 2 | Adyen: "we automatically swap that for a network token" | https://docs.adyen.com/online-payments/network-tokenization | confirmed | Added "(n.d., accessed November 2026)" to the sentence |
| 3 | Adyen optional fields: "The last four digits of the network token", "The last four digits of the card" | same | confirmed | — |
| 4 | Stripe guide: its tokens are "a nonsensitive string that can be used only by the business that collected the card" | https://stripe.com/guides/understanding-benefits-of-network-tokens | confirmed | — |
| 5 | EMVCo: "an EMV Payment Token is constrained in how it can be used…" | https://www.emvco.com/emv-technologies/payment-tokenisation/ | hedged | The page said EMVCo "defines it in the EMV Payment Tokenisation standard"; the quote is from EMVCo's web page, not the specification. Now "describes it on its EMV Payment Tokenisation page (n.d., accessed November 2026)" |
| 6 | EMVCo: "from point of purchase, to an acquirer…"; "within the merchant environment tokenisation can happen between the merchant and acquirer" | same | confirmed | — |
| 7 | Adyen: "A network token is 16-digit alternative for the Primary Account Number (PAN)…" | https://docs.adyen.com/online-payments/network-tokenization | confirmed | — |
| 8 | The token service provider is in practice the card network, "through services such as the Visa Token Service" | https://developer.spreedly.com/docs/network-tokenization | hedged | No source in the page named the Visa Token Service. Spreedly's documentation does ("the card network's token service (examples include Visa Token Service or Mastercard Digital Enablement Service)"); the sentence now quotes it and says whose wording it is |
| 9 | EMVCo: the TSP Code "is included in the Token Requester ID, which uniquely identifies the pairing…" | https://www.emvco.com/processes/token-service-provider-registration-programme-2/ | confirmed | — |
| 10 | Adyen explainer, September 2024: "A network token can be requested by a merchant, payment gateway, or payment processor." | https://www.adyen.com/knowledge-hub/network-tokenization | confirmed | Displayed date is "September 4th, 2024"; the source entry now says 2024-09-04 and no longer cites the metadata "modified" stamp (ruling 25) |
| 11 | EMVCo specification v2.4, published 9 July 2026 (not read by the author) | https://www.emvco.com/emv-technologies/payment-tokenisation/ | confirmed | — (page lists "Version: v2.4 … Published: 9 Jul 2026") |
| 12 | Adyen: "The requestor sends a PAN to the card scheme… the network issues the token." | Adyen knowledge hub (as 10) | confirmed | — |
| 13 | Visa, 4 June 2024: "over 8,000 issuers" enabled | https://usa.visa.com/about-visa/newsroom/press-releases.releaseId.20701.html | confirmed | — |
| 14 | Stripe documentation index warns not to "assume every card or payment is eligible for network tokenization" | https://docs.stripe.com/llms.txt | hedged | The sentence is in the index's "Integration guidance for LLM agents"; the page now says "in its guidance for AI agents, warns them" |
| 15 | Adyen: "Tokens are domain-locked, meaning the same token can only be used by the party that requested it." | Adyen knowledge hub | confirmed | — |
| 16 | Stripe: "payment credentials that you can dynamically restrict to specific businesses and channels" | https://docs.stripe.com/payments/analytics/acceptance | confirmed | — |
| 17 | Adyen: "card schemes issue a cryptogram each time a customer uses their saved card details to initiate a purchase…" | Adyen knowledge hub | confirmed | — |
| 18 | Adyen field `tokenAuthenticationVerificationValue`: "This is the network token cryptogram." | https://docs.adyen.com/online-payments/network-tokenization | confirmed | — |
| 19 | Stripe: "using a network token often requires a one-time cryptogram… high additional latency compared to using PANs." | Stripe guide (as 4) | confirmed | — |
| 20 | "no source I read says whether a renewal the merchant starts carries one [a cryptogram]" | https://docs.adyen.com/online-payments/network-tokenization | **corrected** | A source already in the page says it. Adyen's request tables for tokens a merchant manages include `mpiData.tokenAuthenticationVerificationValue` for the initial and the one-off (CardOnFile) payment, and omit it for "Subscriptions or automatic top-offs", which carry `paymentMethod.networkPaymentReference` instead. The sentence now says so, and says Stripe's pages are silent on it |
| 21 | Stripe: "determining when to use a network token or the underlying PAN. We maintain PAN redundancy to retry failed network token transactions on the underlying PAN" | Stripe guide | confirmed | — |
| 22 | Adyen: "If a payment attempt with a network token fails (`attempt1`), we automatically retry the payment. In the second attempt (`attempt2`), we do not swap…" | Adyen network-tokenization page | confirmed | — |
| 23 | Stripe: "if a customer lost their card, Stripe would get notified by the network and would update the token directly…" | Stripe guide | confirmed | — |
| 24 | Adyen: "if the shopper receives a new card because the old one expired or was lost, the network token remains the same." | Adyen network-tokenization page | confirmed | — |
| 25 | An account updater delivers the new card number to the provider's vault | https://docs.stripe.com/llms.txt ; https://stripe.com/ie/authorization-boost | confirmed | — (index: "Automatically retrieve updated card numbers and expiration dates from participating card networks") |
| 26 | Stripe "doesn't guarantee any outcomes" for these features | https://docs.stripe.com/payments/analytics/optimization | confirmed | — |
| 27 | Adyen: "Apple Pay uses network tokenization, stores payment information securely in the shopper's Apple Pay eligible device…" | https://docs.adyen.com/payment-methods/apple-pay | confirmed | — |
| 28 | Google: "cards on file on Google.com (`PAN_ONLY`) or a device token on an Android-powered device authenticated with a 3-D Secure cryptogram (`CRYPTOGRAM_3DS`)" | https://developers.google.com/pay/api/web/guides/tutorial | confirmed | — |
| 29 | Stripe's forwarding API sends Apple Pay credentials through `network_token_number` and `network_token_cryptogram` | https://docs.stripe.com/payments/vault-and-forward | confirmed | — |
| 30 | Adyen, Click to Pay: "The card scheme is responsible for securely storing the cardholder data and issuing tokens." | https://docs.adyen.com/payment-methods/cards/click-to-pay | confirmed | — |
| 31 | Mastercard, 11 June 2024: "To eliminate manual card entry, Mastercard is making it easier to embed Click to Pay into merchant sites" | Mastercard newsroom (URL in Sources) | confirmed | — |
| 32 | Adyen: "Currently, Adyen's Click to Pay integration only supports recurring payments on Mastercard Click to Pay" | Adyen Click to Pay page | confirmed | — |
| 33 | "I found no page on Click to Pay in Stripe's documentation index" | https://docs.stripe.com/secure-remote-commerce | **corrected** | True of `llms.txt`, but Stripe does document it, under the name Secure Remote Commerce (the page is in Stripe's sitemap). It says "Users can add cards from Visa, Mastercard, American Express, and Discover to enable Click to Pay", "Secure Remote Commerce is only available in the US at this time" and "We're working to re-enable Secure Remote Commerce onboarding". The sentence now states this; the source was added |
| 34 | Adyen press release, 29 October 2026: "Adyen will initially offer Visa Payment Passkey through Authenticate in the UK… global expansion planned for 2027." | https://www.adyen.com/press-and-media/adyen-visa-payment-passkey | confirmed | — (displayed "October 29th, 2026") |
| 35 | Adyen documentation: "Scheme passkeys are currently in pilot phase…"; "supported for Mastercard network tokenized transactions" | https://docs.adyen.com/online-payments/authentication/scheme-passkeys | confirmed | — |
| 36 | Stripe's documentation index has no page on passkeys for card payments | https://docs.stripe.com/llms.txt | confirmed | Also searched Stripe's sitemap (5,148 addresses): no page with "passkey" in its address. Date added to the sentence |
| 37 | Mastercard: "vision for 100% e-commerce tokenization in Europe by the end of the decade…"; "today secures 25% of all e-commerce transactions globally" | Mastercard newsroom | confirmed | — |
| 38 | Visa: "Currently, 29% of all transactions processed by Visa use tokens"; "more than 10 billion tokens since the technology's launch in 2014" | Visa press release | confirmed | — |
| 39 | Braintree 2023: "Effective 1 October 2023: Visa will introduce a new fee of 2.5bps (0.025%)…"; all European countries except Turkey and France | https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/2023/visa-f23 | confirmed | — |
| 40 | Braintree's fall 2026 bulletin still refers to this fee | https://developer.paypal.com/braintree/articles/risk-and-security/compliance/network-updates/fall/2026 | confirmed | — ("The Visa equivalent is the Secure Credential Framework fee.") |
| 41 | Mastercard revises a comparable fee from 1 January 2027; "four rate changes phased in over three years…"; "In April 2028, Guest Checkout will be included in the non-token fee" | same | confirmed | — |
| 42 | Braintree: "behavioral fees intended to drive tokenization and authentication" | same | confirmed | — |
| 43 | Stripe: VDCU fee sentence; "Mastercard levies a Credential Continuity Program (CCP) fee…" | https://docs.stripe.com/payments/analytics/optimization | confirmed | — |
| 44 | Adyen: "Some schemes, like Visa, might charge a fee for the management of issued tokens. They still charge lower fees…" | Adyen knowledge hub | confirmed | — |
| 45 | CMSPI, 2026: "Beginning in April 2026, Visa will introduce a Card-Present Token Fee…" | https://cmspi.com/april-2026-u-s-network-fee-updates-3-billion-estimated-cost-impact-for-merchants/ | hedged | Quote matches. CMSPI's own footnote for it is a J.P. Morgan bulletin, so this is a secondary source citing another. The text now says "wrote in April 2026, citing a bank's bulletin"; table cell and source entry updated (published 28 April 2026) |
| 46 | Fee table: Mastercard fund "Listed as 5 basis points today in most of Europe" | Braintree fall 2026 bulletin | **corrected** | The bulletin's "Current" row is 7 bps for Germany and 5 bps for the rest of Europe, domestic and intra-European. Cell now reads "5 basis points (7 in Germany) on domestic and intra-European payments" |
| 47 | Stripe: "Visa offers certain discounts on consumer card-not-present payments in some markets" | Stripe optimization page | confirmed | — |
| 48 | Stripe India: "The RBI mandates card on file (CoF) tokenization through the card networks"; "Businesses, Payment Aggregators (PAs), Payment Gateways (PGs), and acquiring banks can no longer store customer card information" | https://docs.stripe.com/india-network-tokenization | confirmed | — |
| 49 | India: tokens need the customer's consent: "Cards won't be automatically tokenized." | same | **corrected** | The quoted sentence closes a note about scope ("This applies only to India domestic businesses for domestic transactions. International businesses on Stripe aren't contracted with Stripe India…"), so it does not evidence consent. Replaced by the page's consent sentence ("Customers must provide explicit consent to allow the tokenization and storage of the card on Stripe's system.") and the scope ("only to India domestic businesses for domestic transactions") |
| 50 | Mastercard: "phase out manual card entry and make e-commerce safer"; Braintree: "to help reduce fraud and improve approval rates" | Mastercard newsroom; Braintree 2023 | confirmed | — |
| 51 | Visa: "a six-basis point increase in payment approval rates globally" | Visa press release | confirmed | — |
| 52 | Table: "CMSPI, citing Visa": "a 6% improvement in authorized rates" | CMSPI | hedged | Quote matches ("which Visa says has been associated with a 6% improvement in authorized rates"). CMSPI's footnote is an article by a Visa author ("Why tokens are key to future proofing your payments"), which I did not read; it concerns token usage growth in 2024. Cell now says so |
| 53 | Adyen: "an average uplift of 3% in authorization rates for businesses on our platform who use network tokenization" | Adyen knowledge hub | confirmed | — |
| 54 | Stripe: "Increase acceptance rates by 3.8% on average with Authorisation Boost"; the bundle is Adaptive Acceptance, network tokens, card account updater | https://stripe.com/ie/authorization-boost | confirmed | Source address changed to the Irish page |
| 55 | "Visa's footnote gives its basis as 'VisaNet CY2023 credit and debit global card-not-present…'" (for the six basis points) | Visa press release | **corrected** | The six-basis-point sentence has no footnote. Footnote 1 ("VisaNet CY2023…") is attached to the $40 billion of incremental e-commerce revenue. The sentence now says the release attaches no footnote to the six basis points and gives this as the nearest stated basis |
| 56 | "a secondary source quotes six percent, a hundred times more" | CMSPI | hedged | CMSPI cites a different Visa text from the press release, so the two figures may not describe one measurement. Sentence now says "attributes six percent to Visa… whether the two describe the same measurement I cannot tell" |
| 57 | Doist quote in Stripe's 2023 release: "over 4%", credited to network tokens and card account updater together | Stripe newsroom | confirmed | — |
| 58 | Visa: "up to 60%" and "$650 million", both footnoted to "Visa Processed global card-not-present (CNP)…" | Visa press release | **corrected** | Only the $650 million carries that footnote (2). The "up to 60%" sentence carries footnote 4, "Visanet, Visa processed transactions as of April 2024". The sentence now gives each figure its own footnote |
| 59 | Adyen returns `retry.attemptN.networkTokenOffered`; "Include the retry attempts" | Adyen network-tokenization page | **corrected** | Adyen writes the parameter as `retry.attempt.networkTokenOffered` in its table and `retry.attempt1.…`, `retry.attempt2.…` in its examples; "attemptN" is not Adyen's spelling. Now written as in the examples |
| 60 | Stripe API reference lists `payment_method_details.card.network_token.used`: "Indicates if Stripe used a network token, either user provided or Stripe managed when processing the transaction" | https://docs.stripe.com/api/charges/object | hedged | Wording confirmed in the HTML page (parent field: "If this card has network token credentials, this contains the details of the network token credentials."; sample response shows `"network_token": {"used": false}`). The page data marks the field with the feature flag `network_token_details_resource_feature`, and the Markdown copy of the page omits it. The text now says so and tells the reader to confirm the account returns it; table cell and source entry updated |
| 61 | Stripe dashboard attributes each payment "to the one most likely responsible for approval"; "The optimization calculations we provide are estimates" | Stripe optimization page | confirmed | — |
| 62 | Stripe "will request tokens on your behalf" | Stripe guide | confirmed | — |
| 63 | Adyen: "We collect and store network tokens from the card schemes" | Adyen network-tokenization page | confirmed | — |
| 64 | Adyen merchant-managed mode: "you can keep your existing network tokens…"; "It is not possible to combine this with our tokenization feature"; "You cannot use 3D Secure for transactions with network tokens that you manage yourself" | Adyen network-tokenization page; https://docs.adyen.com/online-payments/network-tokenization/pan-fallback | confirmed | — |
| 65 | Stripe product page: businesses can "bring external tokens for processing" | https://stripe.com/ie/authorization-boost | confirmed | Full sentence: "Businesses can use Stripe to provision tokens or bring external tokens for processing. Stripe supports network tokens for Visa, Mastercard and American Express." |
| 66 | Spreedly: "Token Requestor Token Service Provider (TR-TSP)"; "request network tokens using their merchant-specific TRID" | https://developer.spreedly.com/docs/network-tokenization | confirmed | — |
| 67 | Adyen: "a token cannot be used by a party other than its requestor" | Adyen knowledge hub | confirmed | — |
| 68 | Stripe export page: encrypted file with "the card details of your customers, email addresses, and any attached metadata"; no mention of network tokens | https://docs.stripe.com/get-started/data-migrations/pan-export | confirmed | — (the word "token" does not occur on the page) |
| 69 | "I found no public Adyen page that describes an export" | https://docs.adyen.com/llms.txt | hedged | Adyen's documentation index lists three pages on importing payment data and none on exporting. A web search returned an Adyen help-center article, "How can I prepare for token migration? [Export]" (`help.adyen.com/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export`); its address now answers 301 to `docs.adyen.com/online-payments/tokenization`, which describes no export, so I could not read it. The text now says exactly that; the "Leaving" table cell says "No export page in the documentation index"; the index was added to Sources |
| 70 | Adyen Forward API: "We support forwarding card details, and network tokens"; one request at a time; only after Support enables it | https://docs.adyen.com/online-payments/tokenization/forward-payment-details | confirmed | — ("Contact our Support Team to enable forwarding card details or network tokens"; one POST `/forward` per forwarded request) |
| 71 | Stripe: "works out of the box for all merchants who use Stripe Payments" | Stripe guide | confirmed | — |
| 72 | Adyen: one page says it "automatically requests network tokens for stored cards when possible", "another says to ask Support to enable them" | https://docs.adyen.com/online-payments/tokenization ; network-tokenization page | hedged | The second sentence, under the heading "Let Adyen manage network tokens", reads "To manage network tokens yourself, ask our Support Team to enable payments with network tokens." It contradicts its own heading, so which mode needs Support is unclear. The cell now quotes it and says where it stands |
| 73 | Stripe: merchant as requestor is mentioned on the product page; "no integration guide found" | Stripe index, sitemap, API reference | confirmed | Searched `llms.txt`, the sitemap and the PaymentIntent and PaymentMethod create pages: no page or request parameter for a merchant's own network token |
| 74 | Scope: Visa, Mastercard, American Express on both; Stripe's list of markets; Adyen "only applicable for payments acquired by Adyen" | Stripe guide and product page; Adyen network-tokenization page | hedged | Both companies write "card networks like Visa, Mastercard, and American Express" (Stripe's product page: "supports network tokens for Visa, Mastercard and American Express"); Adyen also mentions Discover for co-badged US tokens. Cells now say "Names…" |
| 75 | Stripe: "€0.15 per token provisioned for accounts without Authorisation Boost and with custom interchange pricing"; Adyen's prices for network tokenization are not public | https://stripe.com/ie/authorization-boost ; https://www.adyen.com/pricing | confirmed | Adyen's pricing page has no line for tokens |
| 76 | Stripe: `payment_method.automatically_updated` "notifies you of automatic card updates from the network"; "the card's new expiration date and last four digits"; nothing on token-only changes | https://docs.stripe.com/payments/cards/overview | confirmed | — |
| 77 | Adyen: network tokenization "cannot be used with external acquirer connections" | Adyen network-tokenization page | confirmed | — |
| 78 | Adyen fields `latestCard.summary`, `latestCard.expiryDate`, `networkToken.*` | same | confirmed | — |
| 79 | Braintree: related merchant-initiated transactions "that are in scope for tokens or 3DS will avoid the behavioral fee" | Braintree 2023 | confirmed | — |
| 80 | Stripe: "If the card update includes a new card number, the fingerprint changes." | Stripe cards page | confirmed | — |
| 81 | Adyen example: `attempt1` token offered, response code 05; `attempt2` no token, response code 00 | Adyen network-tokenization page | confirmed | — |
| 82 | Stripe: "Any such fees reduce the overall cost saving benefits from network tokens." | Stripe optimization page | confirmed | — |
| 83 | Evidence-age marks: Stripe newsroom (February 2023, 3.7 years); Braintree 2023 bulletin (3 years). No other source predates November 2023 | — | confirmed | — |

## "Where They Differ" table

Checked cell by cell (claims 54, 60, 62, 64, 65, 68–75, 78). No cell said "Not public" for a thing a provider documents, except the old "No public export page" for Adyen (claim 69), now narrowed. The last cell of the "Leaving" row read "Not public for either"; it now reads "Neither says what happens to the tokens", which is what the two providers' pages support.

## Links

All 31 addresses in Sources return HTTP 200. Changes: the Authorization Boost entry now points to `https://stripe.com/ie/authorization-boost` (the unlocalized address redirects by the reader's location). Two entries added: Stripe's Secure Remote Commerce guide and Adyen's documentation index. All `[[permalink]]` links are in the style guide's list. No external address in the running text (ruling 22).

## Could not verify, and what I did

- **Adyen's help-center article on token export** (claim 69): the address redirects; an archive lookup was not permitted in this session. The page states the redirect and does not describe the article's content.
- **The Visa-authored article behind CMSPI's "6%"** and **the J.P. Morgan bulletin behind the card-present token fee**: not fetched; both claims stay attributed to CMSPI as a secondary source that cites them (claims 45, 52, 56).
- **EMVCo's specification text**: not read (the page already says so); the two roles rest on EMVCo's public pages, Adyen and Spreedly.
- **Whether `network_token.used` is returned to every Stripe account**: not determinable from public pages (claim 60).

## Format and rulings

- `timetoread` changed from 26 to 27 (6,165 words ÷ 230 = 26.8).
- Ruling 22 (no inline external addresses), ruling 25 (displayed dates), ruling 30 (documentation cited "n.d., accessed November 2026"): applied. Rulings 14 and 17 are respected (Mila's pass is a wallet payment; Mastercard facts come through Mastercard's own press release, Braintree and the providers, not the rules).
- Units unchanged: no unit added, dropped, merged or reordered; `validate_spec.py` and `check_draft.py structure` pass; build and render check pass.

## Larkfield consistency

Lotte Smit's case, the fee (€49.00 × 1.9% + €0.25 = €1.18; €47.82 to the studio), the 210,000 renewals (€10.29 million; 2.5 basis points ≈ €2,570, "about €2,600"), Mila's dates (12 January and 9 March 2027), pass-through pricing on Adyen and the blended rate on Stripe, K4 and K8 all agree with the ledger. The page names no weekdays.

## Ledger conflicts

None. One soft point: the page speaks of Larkfield's "planned migration of 1,140 studios from Stripe to Adyen". The ledger says only that these studios "have not been migrated"; chapter 22 describes what moving them would take. No ledger line dates or decides the migration.

## For other pages

- **`journal-spec.json`, entry `network-tokens`, `how_why`**: it says Stripe has "no interface for the merchant" for network tokens. Stripe documents two things: a read-only field on the charge, `payment_method_details.card.network_token.used` ("Indicates if Stripe used a network token, either user provided or Stripe managed when processing the transaction."; parent: "If this card has network token credentials, this contains the details of the network token credentials."), shown in the HTML API reference behind a feature flag and absent from its Markdown copy; and one sentence on the product page, "Businesses can use Stripe to provision tokens or bring external tokens for processing." No integration guide or request parameter for external tokens was found. The journal spec should say "a read-only field and no documented integration for a merchant's own tokens".
- **`22-tokenization-vaulting-and-pci`** (and any page that says Adyen publishes nothing on export): see claim 69. An Adyen help-center article on token export has existed; its address redirects in November 2026.
- **Any page that says Stripe has no Click to Pay**: see claim 33.
- **`05-payment-economics` / `09-authorization-optimization`**: Braintree's fall 2026 bulletin also lists a Visa "Digital Commerce Services Fee in EU" from 1 April 2027, and says that in the United States the token cryptogram (TAVV) and the Visa Digital Credential Updater are folded into that fee. Not used on this page.
