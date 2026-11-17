# Verification — 09-authorization-optimization (`authorization-optimization`)

Verification pass of 17 November 2026. Every source below was fetched in this session: Stripe and Adyen documentation as `.md` variants (the Stripe A/B testing page also as HTML, because its "Private preview" label is not in the `.md` variant), Stripe guides, blog posts and the product page as HTML with `Accept-Language: en-US` (without it stripe.com redirects to the `/nl/` edition), Adyen's press releases, product pages and knowledge-hub article as HTML, the Visa rules PDF converted with `pdftotext`, the PayPal article as HTML, and Adyen's Checkout API description (OpenAPI, v71) from Adyen's public GitHub repository. Every double-quoted string in the article was matched mechanically against the fetched texts (typographic quotes and whitespace normalized) and then read in context. Short URLs: S = `https://docs.stripe.com`, SC = `https://stripe.com`, A = `https://docs.adyen.com`, AC = `https://www.adyen.com`, VR = `https://usa.visa.com/dam/VCOM/download/about-visa/visa-rules-public.pdf`, PP = `https://www.paypal.com/us/brc/article/avoid-excessive-retries-penalties`.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe guide: "some banks classify nearly all declines as 'Do not honour'" | SC/guides/optimizing-authorization-rates | corrected | The page reads “Do not honor.” (American spelling). Quotation, the source entry and the spec's evidence line changed to "Do not honor" |
| 2 | Code 05 means "do not honor" and is generic | A/development-resources/raw-acquirer-responses/visa-integrity-fees ("05: Do not honor, falls into this category [4]"); SC guide | confirmed | — |
| 3 | Stripe: "There are three reasons why a payment might fail": issuer declines, blocked payments, invalid API calls | S/declines | confirmed | — |
| 4 | Stripe: "When Stripe blocks a payment, it doesn't obtain authorization from the card issuer." | S/declines | confirmed | Added a one-clause gloss of "card network" in the same sentence (term was undefined) |
| 5 | A block can be a risk block or made to save a fee | S/declines (Radar blocks; "For users with IC+ pricing, Adaptive Acceptance blocks certain payments to help you avoid unnecessary network costs") | confirmed | — |
| 6 | Stripe: issuer's "automated systems and models decide whether to authorize it. These tools analyze signals such as spending habits, account balance, and card data (expiration date, address information, and CVC)" | S/declines | confirmed | — |
| 7 | Stripe guide: "there are 128 fields in the ISO 8583 message, and each issuing bank can choose how to interpret and combine them" | SC guide | confirmed | Added a one-clause gloss of ISO 8583 |
| 8 | Stripe: "Card issuers categorize most declines as generic (generic_decline), making the exact decline reason unclear" | S/declines/card | confirmed (the page links `generic_decline`; text identical) | — |
| 9 | Stripe: "For privacy and security reasons, card issuers discuss the specifics of a decline only with their cardholders." | S/declines/card | confirmed | — |
| 10 | Adyen refusal reason 27 "Declined Non Generic" "maps all those response codes that cannot be reliably mapped" | A/development-resources/refusal-reasons | confirmed | — |
| 11 | "Soft decline" and "hard decline" are not network terms (ruling 15) | VR, Table 7-2 (neither term is used there) | confirmed | — |
| 12 | Visa's four decline categories are in Table 7-2 of the Visa Core Rules of 24 October 2026 | VR title page; section 7.3.6.3, Table 7-2, p. 547–549 | confirmed | — |
| 13 | Category names: "Issuer will never approve", "Issuer cannot approve at this time", "Data quality – Revalidate payment information", "Generic response codes" | VR Table 7-2 | confirmed | — |
| 14 | Category 1 examples 04, 14, 43, 46 | VR Table 7-2 ("04 (Pick up card [no fraud])", "14 (Invalid account number…)", "43 (Stolen card, pick up)", "46 (Closed account)") | confirmed | — |
| 15 | Category 2 examples 51, 59, 91 | VR Table 7-2 | confirmed | — |
| 16 | Category 3 examples 54, N7 | VR Table 7-2 ("54 (Expired card or expiration date missing)", "N7 (Decline for CVV2 failure)") | confirmed | — |
| 17 | Category 4 is all other codes, including 05 | VR Table 7-2 ("All other Decline Response codes"); 05 is in no other category; Adyen's mapping page says the same | confirmed | — |
| 18 | Mastercard's Merchant Advice Code as Adyen renders it: "03 : Do not try again", "24 : Retry after 1 hour" … "30 : Retry after 10 days"; "Not all Mastercard issuers return the MAC." | A/development-resources/raw-acquirer-responses | confirmed | — |
| 19 | Mastercard's rule documents could not be read (ruling 17) | `mastercard.us/…/transaction-processing-rules.pdf`, `mastercard.com/…/transaction-processing-rules.pdf` | confirmed unreachable (HTTP 403 today) | — |
| 20 | Stripe layers: decline code such as `insufficient_funds`, `generic_decline`; `network_decline_code`, `network_advice_code`; `advice_code` with `do_not_try_again`, `try_again_later`, `confirm_card_data` | S/declines/card; S/declines (outcome example) | confirmed | — |
| 21 | Adyen layers: `resultCode` Refused with `refusalReason`, `refusalReasonCode`; `refusalReasonRaw`, `refusalCodeRaw` once enabled; `merchantAdviceCode` | A refusal-reasons; A raw-acquirer-responses | confirmed | — |
| 22 | Adyen: `refusalCodeRaw` "only available for Visa and Mastercard transactions through our own acquiring platform" | A raw-acquirer-responses | confirmed | — |
| 23 | Adyen publishes a mapping of raw codes to Visa's categories | A visa-integrity-fees | confirmed | — |
| 24 | Stripe authorization rate definition (two quoted sentences, exclusions) | S/payments/analytics/acceptance | confirmed (the page links the excluded terms; text identical) | — |
| 25 | Stripe payment success rate: "unique payment attempts submitted through Stripe" | same | confirmed | — |
| 26 | Stripe's example: 103,000 requests, 3,000 invalid, 1,000 failed authentication, 1,000 blocked, 93,000 authorized; 93% and 94.9% | same (example table) | confirmed | — |
| 27 | Checkout conversion = completed payments over checkouts started | none; the author's definition, not attributed to a company | not a documented claim | — |
| 28 | Stripe raw and deduplicated rate (two quotes); one purchase failing twice then succeeding is 33.3% raw, 100% deduplicated | same (example table) | confirmed | — |
| 29 | Stripe's record of a blocked payment: `"type": "blocked"`, `"network_status": "not_sent_to_network"` | S/declines (both outcome examples) | confirmed | — |
| 30 | Blocking 1,000 more: 93,000 / 97,000 = 95.9%; success rate stays 93% | arithmetic on Stripe's example | confirmed (arithmetic) | — |
| 31 | No public Adyen formula for "authorization rate" or "payment conversion" | A/uplift, A/uplift/uplift-experiments, A/partners/uplift-enablement, `A/llms.txt` searched for "authorization rate", "conversion rate", "payment conversion", "analytics"; the one hit, A/issuing/report-types/balance-platform-accounting-report/authorization-rate, concerns cards Adyen issues and gives no formula | confirmed as far as I can tell ("Not public" check) | — |
| 32 | Stripe: card updates "automatically attempts to update saved card details whenever a customer receives a new card"; "widely supported in the United States"; "International support varies from country to country" | S/payments/cards/overview | confirmed | — |
| 33 | Stripe: `payment_method.automatically_updated` event with "the card's new expiration date and last four digits" | same | confirmed | — |
| 34 | Adyen Real Time Account Updater (four quoted sentences, "appears as a single transaction") | A/online-payments/account-updater/real-time-account-updater | confirmed | — |
| 35 | Stripe guide: "We maintain PAN redundancy to retry failed network token transactions on the underlying PAN" | SC/guides/understanding-benefits-of-network-tokens | confirmed | — |
| 36 | Andreu Mora, Adyen's global head of engineering data, January 2025: "the AI in Uplift can choose to tokenize, use a token, or swap a token for a PAN based on global optimization targets" | AC/knowledge-hub/the-ai-behind-uplift (byline "SVP / Global Head of Engineering Data"; displayed date January 17th, 2025) | confirmed | — |
| 37 | Adyen: "Network tokenization is only applicable for payments acquired by Adyen." | A/online-payments/network-tokenization | confirmed | — |
| 38 | Neither company publishes the approval gain from network tokens alone | SC network-token guide and S/payments/analytics/optimization read; A network-tokenization read | not checked exhaustively (a negative claim; nothing found on the pages read) | — |
| 39 | Stripe guide: "banks are often more likely to approve domestic payments" | SC guide | confirmed | Added a one-clause gloss of acquiring |
| 40 | Stripe guide describes testing postcode formats bank by bank | SC guide ("test a variety of variations to find out if a certain postal code format gets better authorization rates… which treatment is most effective for which bank"; a hypothetical example on the page) | confirmed | — |
| 41 | Adyen Smart Payment Messaging "optimizes issuer messaging (for example, CVC and AVS fields) to increase authorization rates on low-risk transactions" | A/partners/uplift-enablement | confirmed | — |
| 42 | Adyen Authentication Engine "helps decide when to offer strong customer authentication, which exemptions to ask for, and when to request the frictionless or the challenge flow" | A/uplift | confirmed | — |
| 43 | Visa category 1: "a Merchant must never resubmit an Authorization Request or Account Verification for the same Payment Credential" | VR Table 7-2 (cell text wraps across lines) | confirmed | — |
| 44 | Visa categories 2–4: "Reattempt permitted (up to 20 attempts in 30 days)" | VR Table 7-2 | confirmed | — |
| 45 | Adyen's mapping page still says "up to 15 times in a 30-day period" and names an "excessive retry fee" (ruling 19) | A visa-integrity-fees | confirmed | — |
| 46 | Stripe "recommends a maximum of eight retries"; issuers "might see creating additional retries as potential fraud" | S/declines/card | confirmed | — |
| 47 | Mastercard thresholds per PayPal, May 2026: 10 retries in 24 hours, 35 in 30 days | PP (dated May 15, 2026) | hedged | PayPal cites "Mastercard (June 2023) Transaction Processing Rules" for these numbers. Sentence and source entry now say so, with an evidence-age mark for the cited rules |
| 48 | Stripe Smart Retries: default for new accounts "up to 8 retries within 2 weeks"; part of Billing; no retry of a hard decline until a new payment method | S/billing/revenue-recovery/smart-retries | confirmed | — |
| 49 | Adyen Auto Rescue retries refused shopper-not-present payments "at optimal times"; window of 1 to 48 days | A/online-payments/auto-rescue; A/online-payments/auto-rescue/cards ("between 1 and 48 days") | confirmed | — |
| 50 | Neither publishes a recovery rate for scheduled retries | the three pages above | not checked exhaustively (negative claim; nothing found on the pages read) | — |
| 51 | Authorization Boost announced May 2025; bundles Adaptive Acceptance, card account updater, network tokens | SC/blog/using-ai-optimize-payments-performance-payments-intelligence-suite (15 May 2025: "announced last week at Stripe Sessions"); S/payments/analytics/optimization; S a-b-testing | confirmed | — |
| 52 | Stripe: "Adaptive Acceptance uses AI to reformat payment requests based on card issuers' preferences. Stripe can make these changes before sending a payment or after a payment is declined." | S/payments/analytics/optimization | confirmed | — |
| 53 | Stripe retries "without the end customer ever seeing the initial decline" (blog, 12 February 2025) | SC/blog/ai-enhancements-to-adaptive-acceptance (datePublished 2025-02-12) | confirmed | — |
| 54 | Stripe "might automatically retry an eligible transaction on a US debit network" | S optimization | confirmed | — |
| 55 | Stripe, for interchange-plus accounts: "Decline prevention: Stripe blocks a payment from reaching the card network that was unlikely to succeed, avoiding additional scheme fees for the payment." | S optimization (cost savings row; IC+ condition stated on the page and in S/declines) | confirmed | — |
| 56 | Adyen Uplift launched 9 January 2025 | AC/press-and-media/adyen-uplift-launch (displayed "January 9th, 2025") | confirmed | — |
| 57 | Intelligent Payment Routing "chooses among Adyen's own acquirers and networks" and "is off by default" | A/partners/uplift-enablement | hedged | The guide says it routes "each transaction to the highest-converting or lowest-cost acquirer or network"; it does not say "Adyen's own". The description is now the guide's words; "is off by default" confirmed |
| 58 | Smart Payment Messaging "is enabled by default" | same ("This is enabled by default") | confirmed | — |
| 59 | Excessive Retry Prevention Service "is opt-in, not priced, and in maintenance mode"; "may have a negative impact on authorization rates" | same | confirmed | — |
| 60 | Adyen product page: "Auto Retries intelligently retries declined transactions by adapting the route, messaging, authentication, and tokenization to maximize the chance of success – in milliseconds." | AC/uplift/optimize | confirmed | — |
| 61 | Stripe may "reattempt a declined payment on an alternative card network" | S optimization | confirmed | — |
| 62 | Stripe blog: XGBoost to TabTransformer+ (quote in two parts); "We can now train and deploy new versions of our Adaptive Acceptance model multiple times per week" | SC blog of 12 February 2025 | confirmed | — |
| 63 | Adyen: models "optimized globally through Reinforcement Learning" | AC knowledge-hub article | confirmed | — |
| 64 | Adyen: "SLA for transaction processing: 1 second including acquirer communications which consumes around 600 ms"; "touched between 2 and 5 different AI endpoints"; "an allocated latency of 20 ms (median)" | same | hedged | Quotes match. The article lists the SLA among "Adyen Platform numbers from 2023" and states the endpoint figure for Black Friday/Cyber Monday 2024; both qualifiers added |
| 65 | Envelope on Adyen: routing objective for the United States and Australia (three options), messaging optimization level, rescue window, custom risk rules | A uplift-enablement ("For US and Australia, choose between: balance conversion and cost (recommended), prioritize cost, or prioritize conversion"; "adjust the optimization level"); A auto-rescue/cards; A/uplift (Protect) | confirmed | — |
| 66 | Stripe: "businesses using Authorization Boost's real-time optimizations can increase their acceptance rate by 3.8% on average, with some seeing up to 7%" (15 May 2025) | SC blog (John Affaki, datePublished 2025-05-15) | confirmed | — |
| 67 | The 3.8% average is repeated on 29 April 2026 | SC/blog/everything-we-announced-at-sessions-2026 ("helping increase acceptance rates by an average of 3.8%") | confirmed | Source entry now names the author shown on the page (Will Gaybrick) |
| 68 | Stripe: "recovering a record-high $6 billion in falsely declined transactions" in 2024 | SC blog of 12 February 2025 | confirmed | — |
| 69 | Adyen: "AI helps businesses increase payment conversion rates by up to 6% compared to legacy implementations"; "Piloted by 60 enterprise businesses" | AC press release of 9 January 2025 | confirmed | — |
| 70 | Adyen footnote: "Based on the average conversion improvement of merchants that participated in the pilot and used all modules of Adyen Uplift." (product update, January 2025) | AC/the-latest/boost-your-payment-conversion-with-adyen-uplift | confirmed | — |
| 71 | The 3.8% is stated without a definition of "acceptance rate" (relative or points, raw or deduplicated, cohort) | SC blogs of 15 May 2025 and 29 April 2026 | confirmed (no definition beside either statement) | — |
| 72 | Adyen's 6% applies to pilot merchants using "all five Uplift modules, which include checkout and risk features" | AC product update (footnote says "all modules", no count); A/uplift (five modules today: Tokenize, Protect, Authenticate, Optimize, Personalize) | hedged | The 2025 footnote gives no number of modules; the count of five is from today's documentation. Sentence reworded to say so |
| 73 | Stripe: "Stripe doesn't guarantee any outcomes for your use of Authorization Boost features. The optimization calculations we provide are estimates." | S optimization | confirmed | — |
| 74 | Stripe: "For each payment, Stripe assesses the likelihood that optimizations contributed to its success, given that some payments might have otherwise still been approved." | S optimization | confirmed | — |
| 75 | Stripe previewed an A/B test of Authorization Boost on 29 April 2026 | SC Sessions 2026 post ("We previewed the ability to A/B test Authorization Boost") | confirmed | — |
| 76 | In November 2026 the documentation still places it "behind a preview sign-up" | S/payments/analytics/optimization/a-b-testing (HTML: label "Private preview"; section "Request early access" with an email form) | confirmed; wording made exact | Now "still labels it a private preview, with a form to request early access" |
| 77 | A/B test design: two equal random groups, 30 days, results after 37 days, deduplicated payment success rate, significance at 5% | same | confirmed | — |
| 78 | Control group keeps existing optimizations; card account updater runs in both because Stripe "can't apply card credential updates selectively" | same | confirmed | — |
| 79 | Adyen: "we still act on the control group as we define baseline as a 'market baseline'"; "forcing a network token, and retrying with a challenge if the authentication fails. This results in a lower, but more honest uplift calculation" | AC knowledge-hub article | confirmed | — |
| 80 | Adyen experiments run on live transactions; "You can only start optimization experiments following a recommendation." | A/uplift/uplift-experiments ("performed on real transactions, processed with your live Adyen account") | confirmed | — |
| 81 | Sample-size rule 16 × p(1−p)/d² | none; presented as a common rule of thumb in the author's six rules | not a documented claim (arithmetic of the Larkfield use checked: 27,504) | — |
| 82 | "Stripe does not define the 'false decline' behind its $6 billion" | SC blog of 15 May 2025 | corrected | That post glosses false declines as "legitimate transactions mistakenly rejected due to suspected fraud". Sentence now quotes the gloss and says what is missing: how Stripe knows a declined payment was legitimate and how the $6 billion was counted |
| 83 | "Adyen has published no figure since its pilot of 60 businesses" | AC/press-and-media/adyen-launches-authenticate-upgrade (22 September 2026) | corrected | Adyen has published single-customer figures since: that press release quotes an 11% (Too Good To Go) and a 12% (Just Eat Takeaway.com, "on the eligible traffic") increase in payment conversion for its Authenticate module. Sentence corrected to "figures for single named customers only… no figure across merchants"; source entry added |
| 84 | Adyen publishes no price for Uplift | A uplift pages; AC/uplift/optimize; AC/pricing (Uplift appears only as a navigation link) | confirmed as far as I can tell | — |
| 85 | No source gives model features or labels, results by issuer, share of blocked payments that would have been approved, or an audited lift | all sources above | not checked exhaustively (negative claim about the sources read; nothing found in them) | — |
| 86 | Adyen publishes its code mapping for merchants who "have built your own retry logic" | A visa-integrity-fees | confirmed | — |
| 87 | Table: Stripe decline and excessive-retry prevention for interchange-plus accounts | S optimization; S/declines | confirmed | — |
| 88 | Table: Adyen refusal reason 46 "Transaction blocked by Adyen to prevent excessive retry fees" | A refusal-reasons | confirmed | — |
| 89 | Table, "Metric definitions": Adyen "Not public" | see row 31 | confirmed as far as I can tell | — |
| 90 | Table, remaining Stripe and Adyen cells (acting inside the call; scheduled retries; published model detail; headline claim; how a merchant can measure) | rows 34, 48, 49, 52, 58, 62–64, 66, 69, 74–80 | confirmed (each cell restates a row above) | — |
| 91 | Adyen's Checkout API has no call that returns a payment by its identifier (ruling 12) | Adyen OpenAPI, `CheckoutService-v71.json` (`raw.githubusercontent.com/Adyen/adyen-openapi/main/json/`): the only GET paths are `/paymentLinks/{linkId}`, `/sessions/{sessionId}` and `/storedPaymentMethods` | confirmed | — |
| 92 | PayPal (secondary): Visa matches reattempts on acquirer, merchant identifier, card or token, and amount | PP ("using data including, but not limited to, Acquirer, Acquirer Identifier, Card Acceptor ID (CAID), Token/PAN, and transaction amount") | hedged | "matches them on" became "matches them on data that includes" |
| 93 | Whether a retry through a second provider counts against the same limit is not stated in any source read | VR Table 7-2; PP | confirmed for these sources (PP's list starts with the acquirer, which suggests it would not, but neither source says so) | — |
| 94 | Stripe product page describes declining charges "most likely to be rejected, while balancing impact to your auth rates" | SC/authorization-boost (en-US) | confirmed | — |
| 95 | Take-away: Visa allows no reattempt for category 1 and up to 20 in 30 days for the others | VR Table 7-2 | confirmed | — |
| 96 | Lead and key points: Stripe's 3.8% and Adyen's "up to 6%" use different metric names ("acceptance rate", "payment conversion rate") | rows 66 and 69 | confirmed | — |

Counts: 96 rows. 82 confirmed (including three "as far as I can tell" checks of "Not public" or negative statements), 3 corrected, 5 hedged, 0 unsupported and removed, 1 unreachable source (Mastercard's rules, row 19; the page already says so), 2 not documented claims (rows 27 and 81, the author's own definitions) and 3 not checked exhaustively (rows 38, 50 and 85: negative claims about what the companies publish, checked only on the pages read). Rows 4, 7, 39 and 67 are confirmed claims with a format edit beside them.

## Could not verify, and what I did

- **Mastercard's retry thresholds (row 47).** Mastercard's Transaction Processing Rules return HTTP 403 at both known addresses. The numbers stand on PayPal's article, which itself cites the June 2023 edition of those rules. The page already called this a secondary source; it now also names the cited edition and marks its age.
- **Negative claims (rows 38, 50, 85).** "Neither publishes…" and "No source I read gives…" cannot be proven. I checked the pages in Sources and the two documentation indexes and found nothing that contradicts them, after correcting the two that were contradicted (rows 82 and 83). They remain worded as statements about the sources read.
- **Stripe pages by locale.** `stripe.com` guide, product and blog URLs redirect to a `/nl/` edition from this network unless `Accept-Language: en-US` is sent. The canonical URLs in Sources are kept; all quotations were checked against the en-US edition.

## Format and ruling checks

- Ruling 22: the running text has no external URL (only the failure-patterns callout link). Rulings 8, 12, 13, 15, 17 and 19 are applied on the page as written.
- Terms glossed in this pass: card network, ISO 8583, acquiring, blended pricing, dispute.
- `timetoread` changed from 25 to 26 min (5,941 words ÷ 230 = 25.8).
- All 29 source URLs return HTTP 200; one entry added (Adyen press release of 22 September 2026). All twelve `[[permalink]]` targets are in the style guide's list.
- Evidence age: no cited company source is older than November 2023. The only older material is the Mastercard edition PayPal cites (row 47), now flagged.

## Ledger conflicts

None. The December 2026 figures, the 1,140 studios, Mila's dates (9 March, 1 and 4 April 2027), code 51 and decisions K1, K5 and K8 agree with the ledger; all percentages and the sample size recompute.

## For other pages

- Any page that quotes the Stripe authorization-rates guide with "Do not honour" should check the spelling against the en-US page ("Do not honor").
- Any page that says Adyen has published no Uplift figures since the January 2025 pilot should see the press release of 22 September 2026 (single-customer figures for the Authenticate module).
- Any page that cites Mastercard's retry thresholds from PayPal's article should note that PayPal cites Mastercard's rules of June 2023.
