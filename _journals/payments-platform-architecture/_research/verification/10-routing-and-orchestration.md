# Verification — 10-routing-and-orchestration (`payment-routing-and-orchestration`)

Verification pass of 17 November 2026. Every source in the page's Sources section was fetched in this session (Stripe and Adyen documentation as `.md`; the Stripe blog posts, the Sessions talk page with its transcript, the Adyen press release and product page, Spreedly, Primer, Gr4vy, the Hyperswitch README and the two Federal Reserve pages as HTML). Each quotation was compared with the fetched text by script after normalizing typographic quotes and markdown marks, and the surrounding passage was read. The Sessions transcript was read in full. "Not public" and "not found" statements were tested against `https://docs.stripe.com/llms.txt`, `https://docs.adyen.com/llms.txt` and three web searches.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Stripe guide: it "can dynamically route payments to the best connections" when a processor is down | https://stripe.com/guides/optimizing-authorization-rates | confirmed | No edit. The URL redirects by visitor locale; the English page was read |
| 2 | Adyen setting, "off by default", routes "each transaction to the highest-converting or lowest-cost acquirer or network" | https://docs.adyen.com/partners/uplift-enablement | hedged | Both quotations match. The page is partner documentation; the sentence now says "Adyen's documentation for partners" |
| 3 | Regulation II forbids restricting debit processing "to less than two unaffiliated networks" | https://www.federalreserve.gov/paymentsystems/regii-about.htm | confirmed | No edit |
| 4 | Regulation II forbids "inhibiting a merchant's ability to direct the routing of a debit transaction over any network that the issuer has enabled to process it" | same | confirmed | No edit |
| 5 | A 2022 update, effective 1 July 2023, "extended" the requirement to online payments; "still described on the Federal Reserve's page" | https://www.federalreserve.gov/newsevents/pressreleases/bcreg20221003a.htm | corrected | The press release of 3 October 2022 says the updates "specify" that issuers enable two networks for all debit transactions, "including 'card-not-present' transactions"; effective July 1, 2023. The Regulation II page mentions neither 2022 nor 2023. Sentence and evidence-age note rewritten; take-away bullet reworded |
| 6 | US debit cards can run on a global network or a domestic debit network such as PULSE or STAR | https://docs.adyen.com/online-payments/network-tokenization | confirmed | Adyen lists Accel, Maestro USA, NYCE, PULSE, STAR |
| 7 | Adyen announced Intelligent Payment Routing for US debit on 9 September 2024 | https://www.adyen.com/press-and-media/adyens-intelligent-payment-routing-usdebit | confirmed | Dateline "Sept. 9, 2024" |
| 8 | "a pilot of over 20 enterprise merchants" | same | confirmed | No edit |
| 9 | "achieved an average of 26% cost savings with a 0.22% uplift in authorization rates against earlier debit performance" | same | confirmed | No edit |
| 10 | Adyen lets the merchant set network priorities, "For example, 1: PULSE and 2: Visa" | https://docs.adyen.com/online-payments/network-tokenization | confirmed | Added "(n.d., accessed November 2026)". The passage concerns co-badged network tokens in the US |
| 11 | Stripe: Adaptive Acceptance "might automatically retry an eligible transaction on a US debit network (also known as PINless network) after it's declined on an international network" | https://docs.stripe.com/payments/analytics/optimization | confirmed | No edit |
| 12 | "I found no Stripe page on first-attempt least-cost routing" | https://support.stripe.com/questions/supporting-dual-network-debit-cards-in-australia | corrected | True for US debit (docs index and web search: nothing). But Stripe's support site says "Stripe automatically implements least-cost routing for all of its Australian merchants". Sentence narrowed to US debit, the Australian fact added with its source; table cell updated |
| 13 | Alex Ginet (Stripe), Sessions, April 2026: three motives "redundancy and reliability", "performance and cost optimization", "geo expansion" | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | Transcript; video upload date 29 April 2026 |
| 14 | Stripe previewed Stripe Orchestration on 7 May 2025 | https://stripe.com/blog/top-product-updates-sessions-2025 | confirmed | "We previewed Stripe Orchestration"; page dated May 7, 2025 |
| 15 | Documentation said "Orchestration is in private preview" on 17 November 2026 | https://docs.stripe.com/payments/orchestration | confirmed | Fetched 17 November 2026 |
| 16 | It routes card payments to Adyen, Braintree or Worldpay's WPG gateway | https://docs.stripe.com/payments/orchestration/feature-support | confirmed | Feature table columns: Adyen, Braintree, Worldpay WPG |
| 17 | A rule is a condition on amount, currency, card country, issuer, type or BIN | https://docs.stripe.com/payments/orchestration/rules | corrected | The page lists a seventh condition, Metadata; added |
| 18 | "Stripe executes the conditions in order, from left to right, and applies the first action that matches a payment's condition" | same | confirmed | No edit |
| 19 | Each action names a main processor and, optionally, one retry processor | https://docs.stripe.com/payments/orchestration/route-payments | confirmed | "(Optional) Add a processor to retry the payment one more time" |
| 20 | "All related activity (including payment processing fees and liability for transaction losses) remain subject to the terms that you agreed to with that processor." | https://docs.stripe.com/payments/orchestration | confirmed | No edit |
| 21 | "Orchestration also doesn't support disputes or settlement-related activity. To manage these activities, access your third-party processor's dashboard." | same | confirmed | No edit |
| 22 | Feature support "doesn't include non-card payments or Link, Capital, Connect, Terminal, or Organizations" | same | confirmed | No edit |
| 23 | "Stripe creates Payment Records and Payment Attempt Records instead of Charges for payments routed to other processors" | https://docs.stripe.com/payments/orchestration/route-payments | confirmed | No edit |
| 24 | "If your back-end systems assume there's always a Balance Transaction after a successful payment, that's no longer true." | same | confirmed | No edit |
| 25 | Stripe's analytics cannot show an authorization rate for another processor: "Stripe doesn't have access to non-Stripe data." | https://docs.stripe.com/payments/analytics/acceptance | confirmed | No edit |
| 26 | Joshua Barton (Canva): "when you're doing chargebacks or you're doing refunds, your operations team now has to go into a second portal" | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | No edit to the quotation; "chargeback" glossed in the preceding paragraph |
| 27 | Spreedly homepage: "Hold every credential in your own vault, use it with any provider" | https://www.spreedly.com/ | confirmed | No edit |
| 28 | Stripe Vault and Forward is "available only to businesses with a dedicated Stripe account team" | https://docs.stripe.com/payments/vault-and-forward | confirmed | No edit |
| 29 | Its published destinations include Adyen, Braintree, Worldpay and Spreedly | same | confirmed | All four are in the list of supported endpoints |
| 30 | Adyen: "You can forward payment details that you stored with Adyen to a PCI compliant third party, like a payment service provider (PSP). We support forwarding card details, and network tokens." | https://docs.adyen.com/online-payments/tokenization/forward-payment-details | confirmed | No edit |
| 31 | Adyen's support must enable forwarding; the page lists no destinations | same | confirmed | "Contact our Support Team to enable forwarding"; the destination is a `baseUrl` the merchant supplies |
| 32 | Stripe: "We believe our customers own the sensitive data they entrust to Stripe." | https://docs.stripe.com/get-started/data-migrations/pan-export | confirmed | No edit |
| 33 | Stripe "can only transfer your card data to another PCI DSS Level 1-compliant payment processor" | same | confirmed | No edit |
| 34 | Stripe "doesn't export your account's payment history, subscriptions, or other objects" | same | confirmed | No edit |
| 35 | Adyen import: "migrating payment data usually takes 10 days or more" | https://docs.adyen.com/development-resources/migrating-payment-data | confirmed | No edit. Page metadata says last modified 2019-12-06; cited as n.d. like other documentation |
| 36 | "I found no Adyen documentation page that describes an export" | https://help.adyen.com/knowledge/ecommerce-integrations/tokenization | hedged | True of docs.adyen.com (index searched). But Adyen's help center lists an article "How can I prepare for token migration? [Export]"; its link returned a 301 to the general tokenization documentation page, which has no export content, and the Wayback Machine query failed. Sentence now says so; table cell and Sources updated |
| 37 | A network token is issued to the token requestor; if the provider asked, the token is the provider's to use | https://docs.adyen.com/online-payments/network-tokenization | hedged | No fetched source states the general rule; it is industry practice. "is the provider's" weakened to "is typically the provider's"; the consequence is already in the INFERENCE block |
| 38 | Adyen: "Network tokenization is only applicable for payments acquired by Adyen. It cannot be used with external acquirer connections." | same | confirmed | No edit |
| 39 | "The alternative it offers is to manage tokens yourself" | same | hedged | The page offers "Manage network tokens yourself" as an implementation option, not as a remedy for external acquirers. Reworded and the page's sentence quoted |
| 40 | Spreedly: "allowing merchants to request network tokens using their merchant-specific TRID" | https://developer.spreedly.com/docs/network-tokenization | confirmed | No edit |
| 41 | Stripe's export page does not mention network tokens | https://docs.stripe.com/get-started/data-migrations/pan-export | confirmed | Page read in full |
| 42 | Neither company documents whether network tokens move with an export, or under whose requestor ID they are provisioned | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | confirmed | No hit for "requestor" or "TRID" on the Stripe optimization page, Stripe's network-token guide, or Adyen's network tokenization and forward pages; web search found nothing |
| 43 | Canva noticed it needed orchestration only when it added a third provider | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | "It's really when we put the third PSP in" |
| 44 | Jon Krauss (Stripe) on network tokenization and card account updater: "those are independent integrations themselves with the schemes." | same | confirmed | No edit |
| 45 | Spreedly, Primer, Gr4vy and Hyperswitch sell adapters and a vault; Hyperswitch is open source | https://www.spreedly.com/ ; https://primer.io/ ; https://gr4vy.com/ ; https://github.com/juspay/hyperswitch | confirmed | Each homepage names orchestration and a vault |
| 46 | Hyperswitch promises routing "to the PSP with the highest predicted auth rate" | https://github.com/juspay/hyperswitch | confirmed | README, main branch |
| 47 | Krauss: "there are added milliseconds to the end-to-end transaction flow" | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | No edit |
| 48 | Krauss: an orchestrator "creates concentration risk with the orchestrator themselves" | same | confirmed | No edit |
| 49 | Barton: "no one's going to use 400 PSPs" | same | confirmed | No edit |
| 50 | "If you don't have active rules, payments route to Stripe" | https://docs.stripe.com/payments/orchestration/rules | confirmed | No edit |
| 51 | "Link transactions are automatically excluded from your routing rules and always processed on Stripe" | https://docs.stripe.com/payments/orchestration/route-payments | confirmed | No edit |
| 52 | With error protection, a payment needing an unsupported feature goes to Stripe | https://docs.stripe.com/payments/orchestration/feature-support | confirmed | No edit |
| 53 | "As of November 2026 this option exists only at Stripe" | https://docs.adyen.com/llms.txt | hedged | Checked only for Stripe and Adyen; now "of the two companies only Stripe offers this option" |
| 54 | Barton is product lead for global payments at Canva; the layer was built in-house over five providers | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | Speaker list; "we have five PSPs that we've integrated to" |
| 55 | Barton: "the real reason why we did this was redundancy. We accept payments in over 190 countries" | same | confirmed | No edit |
| 56 | It paid off when a provider was degraded without being down, which uptime figures do not count | same | confirmed | No edit |
| 57 | Barton: "What we didn't realize at the time was actually the real power is where you send the traffic the first time." | same | confirmed | No edit |
| 58 | Barton: "country is not the real signal. It's going to be BIN and issuer" | same | confirmed | No edit |
| 59 | Barton: "you had a mid for good traffic, a mid for bad traffic" | same | confirmed | No edit |
| 60 | Barton: "it takes maybe six months or more to integrate a new PSP and that's engineering time", after the contract and verification | same | confirmed | No edit |
| 61 | Barton: "you're spending three-plus months warming up" | same | confirmed | No edit |
| 62 | Barton: "once you start including operational people, it's close to 30 people just working on this." | same | confirmed | No edit |
| 63 | Barton: "it's worth it, so do it" | same | confirmed | No edit |
| 64 | Ginet's example: half a point is worth "$500,000 in revenue" to a business processing a hundred million dollars a year | same | confirmed | No edit |
| 65 | The session also presented Stripe's own product | same | confirmed | Krauss presents Stripe Orchestration in the talk |
| 66 | Lead: "the one merchant that has described it in public" | same | hedged | The page later says "the one detailed merchant account I found", and the spec changelog records that other merchants' posts were dropped. Lead now says "the most detailed public account by a merchant" |
| 67 | Closing: "Canva's thirty people were doing the per-provider work no layer touches" | same | corrected | Barton says only that close to 30 people work on this "once you start including operational people"; he does not say what they do. Now "Canva's close to thirty people include the operations staff who work in each provider's portal" |
| 68 | No audited or independent comparison of approval rates is public; neither company publishes the scale at which routing pays | https://docs.stripe.com/llms.txt ; https://docs.adyen.com/llms.txt | not checked | A negative that cannot be established by fetching; the sentence is worded as the author's finding ("I found") and was left |
| 69 | Adyen Multi pay-in "is currently in pilot phase" | https://docs.adyen.com/marketplaces/multi-pay-in | confirmed | Page last modified 17 November 2026 |
| 70 | Multi pay-in lets a platform "combine payments processed by Adyen with third-party acquired volume" | same | confirmed | No edit |
| 71 | Stripe said on 29 April 2026 it had previewed, for European marketplaces, "unified payouts through Stripe" | https://stripe.com/blog/everything-we-announced-at-sessions-2026 | confirmed | "marketplaces that sell in Europe"; page dated 2026-04-29 |
| 72 | Table: Stripe Orchestration previewed May 2025, private preview, cards to Adyen, Braintree, Worldpay WPG | rows 14–16 | confirmed | No edit |
| 73 | Table: Adyen, "No such product found in public documentation" | https://docs.adyen.com/reporting/settlement-reconciliation/transaction-level/external-settlement-detail-report | corrected | No rule-based routing product is in the Adyen index, but Adyen documents payments for which it "is not the acquirer" (a merchant's own American Express or PayPal agreement) and "external acquirer connections". Cell now says both; source added |
| 74 | Table: Stripe routes across its own connections; US debit as retry path; first-attempt least-cost routing not found | rows 1, 11, 12 | corrected | Cell now says documented for Australia, not found for US debit |
| 75 | Table: Adyen routes among acquirers and networks, off by default; US debit product since September 2024 | rows 2, 7 | confirmed | No edit |
| 76 | Table: Stripe Vault and Forward: account team, published destinations | rows 28, 29 | confirmed | No edit |
| 77 | Table: Adyen `/forward`: enabled by support, cards and network tokens, no published destinations | rows 30, 31 | confirmed | No edit |
| 78 | Table: Stripe bulk export is a documented policy with conditions | rows 32–34 | confirmed | No edit |
| 79 | Table: Adyen "Import documented; export procedure not found" | row 36 | corrected | Now: import documented; an export article is listed in the help center but could not be read on 17 November 2026 |
| 80 | Table: Stripe unified payouts, previewed April 2026 | row 71 | confirmed | No edit |
| 81 | Table: Adyen Multi pay-in, in pilot | row 69 | confirmed | No edit |
| 82 | Krauss: "Stripe Orchestration is an investment in a broader strategy of an open architecture. You're not going to have to be locked into Stripe." | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | No edit |
| 83 | Adyen product page: "Unlike fragmented legacy architectures, Adyen brings payments onto one single platform" | https://www.adyen.com/uplift | confirmed | No edit |
| 84 | Orchestration excludes Connect, which rules it out for platforms | https://docs.stripe.com/payments/orchestration | confirmed | Also the retries page: `on_behalf_of` with Connect is an ineligible feature |
| 85 | After a 3-D Secure attempt that still fails, "Orchestration doesn't retry the transaction on the retry processor" | https://docs.stripe.com/payments/orchestration/retries | confirmed | No edit |
| 86 | An unsupported feature "fails with a `400` error code `orchestration_unsupported`" | https://docs.stripe.com/payments/orchestration/feature-support | confirmed | No edit |
| 87 | The merchant must supply the acquirer BIN of the processor for 3-D Secure | https://docs.stripe.com/payments/orchestration/route-payments | confirmed | No edit |
| 88 | Canva spoke of three months of warm-up | https://stripe.com/sessions/2026/more-psps-more-problems | confirmed | No edit |
| 89 | "For payments routed to third-party processors, those processors administer the refunds." | https://docs.stripe.com/payments/orchestration | confirmed | No edit |
| 90 | Key point: Stripe's documentation puts most of disputes, settlement, balances, method coverage and stored cards outside Orchestration | rows 21–24 | confirmed | No edit |
| 91 | Key point: neither Stripe nor Adyen documents whether network tokens survive a move | row 42 | confirmed | No edit |
| 92 | Take-away: Stripe and Adyen both document routing inside their own networks | rows 1, 2 | confirmed | No edit |
| 93 | Take-away: US debit must work on two unaffiliated networks; online payments since 1 July 2023 | rows 3–5 | corrected | Now "spelled out for online payments from 1 July 2023" |
| 94 | Take-away: Orchestration (private preview) excludes disputes, settlement, non-card methods and platform payments | rows 15, 21, 22 | confirmed | No edit |
| 95 | Link is Stripe's own wallet; a card account updater supplies new details when a card is replaced | https://docs.stripe.com/payments/vault-and-forward ; https://stripe.com/guides/optimizing-authorization-rates | confirmed | Both glosses match the fetched pages |
| 96 | Sample-size arithmetic: 16 × 0.90 × 0.10 ÷ 0.005² ≈ 57,600 per route, about 115,000 per test | — | confirmed | Recomputed; a standard rule of thumb, labeled as an assumption in the page |

Counts: 96 claims; 81 confirmed, 8 corrected, 6 hedged, 0 unsupported, 0 unreachable, 1 not checked.

## Could not verify, and what was done

- **Adyen's export article.** `https://help.adyen.com/knowledge/ecommerce-integrations/tokenization/how-to-prepare-for-token-migration-export` is listed on the help center's tokenization page, but the link answers with a 301 to `https://docs.adyen.com/online-payments/tokenization`, which has no export content (checked with curl and with WebFetch). The Wayback Machine availability query returned an upstream error. A web search summary describes the article (a formal letter of intent, a CSV export once the receiving vault confirms the format), but a search summary is not a source, so the page states only that the article is listed and could not be read. The research brief tags the procedure WIDELY REPORTED from the same kind of summary; it was not used.
- **Row 68**, the absence of any independent comparison of approval rates, is a negative left as the author's finding.
- **Stripe's US least-cost routing.** No docs.stripe.com page was found (index search, one web search, two guessed URLs returned 404). The statement stays, narrowed to US debit.

## Links

All 30 URLs in Sources and Evidence returned HTTP 200 on 17 November 2026. `stripe.com/guides/...` and `stripe.com/sessions/...` redirect to a locale path chosen by the visitor's location; the canonical URLs were kept. Three sources were added (Stripe support on Australian least-cost routing, Adyen help center tokenization index, Adyen External settlement detail report). Two multi-URL bullets were split into one URL each. All `[[permalinks]]` are in the style guide's list.

## Format and rulings

- Ruling 22: no external URL in the running text (checked by script).
- Hand-off: "Part III" replaced with `[[part-3]]`.
- `timetoread` corrected from 28 to 24 minutes (5,502 words ÷ 230).
- Terms glossed that were not: issuer (lead), chargeback, PCI DSS expanded.
- No unit added, dropped, merged or reordered; the spec changed only in its changelog.

## Larkfield consistency

- Corrected: "about 940,000 renewals a month, each charged against a stored credential" appeared in a paragraph about stored cards, but the ledger (`09-authorization-optimization`) says about 540,000 of the 940,000 are paid by card. The sentence now gives both figures and labels the second as an assumption.
- Checked and consistent: 6,200 studios; 44% / €493M and 56% / €627M; the February 2027 proposal; Tom Hendriks, 2024; Mila's pass (Tuesday 9 March 2027, 19:42, €120.00, wallet, payout Thursday 11 March); the €49.00 membership set up 12 January; the €84.00 refund of 18 March; Bram de Wit's €120.00 dispute (2 February, chargeback 24 February: 22 days); the Double Charge (1 November 2026, 1,840 members, €71,300); 1,140 split studios; cards 52% of €910M and 27.6M online payments (14.4M card payments a year, 1.2M a month); K4 and K8; the 50 largest studios.

## Ledger conflicts

None found.

## For other pages

- Any page that says Adyen documents no export of stored cards should use the same wording as this page: an export article is listed in Adyen's help center but its link redirects.
- Any page that says Stripe documents no least-cost routing should except Australia (Stripe support site).
- `_research/brief-optimization-routing-orchestration.md` line 387 ("No Stripe page describing first-attempt least-cost debit routing") is true only for the United States.

## For the author

- The reading time dropped from 28 to 24 minutes because the front matter did not match the word count; the page is at 5,502 words, at the top of the style guide's target range.
- Whether to ask Adyen for the export procedure and cite it once the help article is readable again.
