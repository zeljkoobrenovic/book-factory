# Verification — 19-api-versioning (`payment-api-versioning`)

Verification pass of 17 November 2026. Every source below was fetched in this session with `curl`: Stripe and Adyen documentation as `.md` variants (the Stripe versioning reference also as HTML, because its curl tab is only in the HTML), the three Stripe posts and the Adyen knowledge-hub article as HTML, four Stripe SDK changelogs from GitHub. All 81 strings in typographic double quotes in the article (source quotations, plus a few labels and scare quotes) were matched mechanically against the fetched text; 74 matched outright and 7 differ only by link markup inside the sentence or by a bullet break (rows 3, 13, 44, 49, 53, 64, 70) and were read by eye. All 17 URLs in Sources and Evidence return 200 with no redirect; the two added in this pass also return 200.

| # | Claim (short) | Source URL | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | Key points: Stripe pins by account default, header or, since 2023, SDK release; two named breaking releases a year since October 2024 | https://docs.stripe.com/upgrades ; https://stripe.com/blog/introducing-stripes-new-api-release-process | confirmed | Note: the post is dated 1 October 2024; the first release under the scheme is `2024-09-30.acacia` |
| 2 | Key points: Adyen puts a number in each API's URL; a deprecated Checkout API version has two years to end-of-life | https://docs.adyen.com/development-resources/versioning ; https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | — |
| 3 | Quote "When you use a server-side SDK, your API calls to Stripe use the API version that was current when the SDK was released." | https://docs.stripe.com/upgrades | confirmed | Source has a link on "server-side SDK" |
| 4 | `2022-11-15` was the current version in early 2023 (next is `2023-08-16`) | https://docs.stripe.com/changelog | confirmed | — |
| 5 | `2026-02-25.clover` exists; from `2022-11-15` it crosses four dated versions (2023-08-16, 2023-10-16, 2024-04-10, 2024-06-20) and three named majors (Acacia, Basil, Clover) | https://docs.stripe.com/changelog | confirmed | — |
| 6 | `2025-03-31.basil` removed `subscription` from the Invoice object | https://docs.stripe.com/changelog/basil/2025-03-31/adds-new-parent-field-to-invoicing-objects | confirmed | — |
| 7 | Adyen's list of breaking changes (required request field, removed endpoint or field, renamed field, changed type, changed HTTP status or error code) | https://docs.adyen.com/development-resources/versioning | confirmed | Date flag added: page metadata says last modified 2022-01-18 |
| 8 | Quote "Changing the behavior in a way that requires API consumers to change their integration for it to work properly." | https://docs.adyen.com/development-resources/versioning | confirmed | — |
| 9 | Quote "Just like a power company shouldn't change its voltage every two years…"; 2017 post; evidence age 9 years | https://stripe.com/blog/api-versioning | confirmed | Displayed date August 5, 2017 |
| 10 | "Both companies do make additive changes without a new version" | https://docs.stripe.com/api/versioning ; https://docs.adyen.com/development-resources/versioning | hedged | True of Adyen. Stripe's additive changes come in monthly versions. Now: Adyen applies them to versions in use; Stripe ships them in monthly versions to which you can upgrade "without updating your code" (quote confirmed) |
| 11 | Quote "almost a hundred backwards-incompatible upgrades over the past six years." | https://stripe.com/blog/api-versioning | confirmed | — |
| 12 | Basil page, 31 March 2025: "This version introduces a significant number of breaking changes." | https://docs.stripe.com/changelog/basil | confirmed | — |
| 13 | Adyen release notes, Checkout API v72, 15 April 2026: a "Breaking Changes" heading; "Previously deprecated parameters have been removed." | https://docs.adyen.com/online-payments/release-notes | confirmed | Heading "2026-04-15 — Checkout API — Version 72"; the sentence is under "Removed", with a link on "removed" |
| 14 | Four "classic" Adyen APIs; quote "in new Adyen APIs, adding an optional field to a response body is a non-breaking change, while in classic APIs…" | https://docs.adyen.com/development-resources/versioning | confirmed | Payment, Recurring, Payout, BinLookup |
| 15 | Basil marks the row "Adds expired status for Issuing Authorizations" as breaking; it is a new status value | https://docs.stripe.com/changelog/basil ; https://docs.stripe.com/changelog/basil/2025-03-31/issuing-authorizations-expired | confirmed | Change page read: "introduces a new enum value, `expired`". Wording tightened ("a new value of a status field in responses"); Issuing glossed |
| 16 | 2017 post rejected large versions: "so big and so impactful…"; "retiring API versions and by extension cutting those users off, or maintaining the old versions forever at considerable cost." | https://stripe.com/blog/api-versioning | confirmed | — |
| 17 | "Only one payment provider has published how it pays for pinning" | — | hedged | Not checkable for all providers. Now "Of the two providers, only Stripe has published…" |
| 18 | Post title, date 5 August 2017, author Brandur Leach | https://stripe.com/blog/api-versioning | confirmed | — |
| 19 | Quote "we implement versioning with rolling versions that are named with the date they're released (for example, 2017-05-24)." | https://stripe.com/blog/api-versioning | confirmed | Source begins "At Stripe, we implement…" |
| 20 | Quote "The first time a user makes an API request, their account is automatically pinned…" | https://stripe.com/blog/api-versioning | confirmed | — |
| 21 | A request can override the pin with a `Stripe-Version` header (2017) | https://stripe.com/blog/api-versioning | confirmed | — |
| 22 | Quote "we encapsulate it in a version change module which defines documentation about the change, a transformation, and the set of API resource types…" | https://stripe.com/blog/api-versioning | confirmed | — |
| 23 | Version found from the header, an authorized application or the account's pin; quote "walks back through time and applies each version change module that finds along the way…" | https://stripe.com/blog/api-versioning | confirmed | Source: "authorized OAuth application" |
| 24 | Modules marked as having side effects; quote "This reduced encapsulation makes changes with side effects more complex to maintain, so we try to avoid them." | https://stripe.com/blog/api-versioning | confirmed | — |
| 25 | Quotes "Providing extensive backwards compatibility isn't free…"; "littered throughout the project…"; "we've maintained compatibility with every version of our API since the company's inception in 2011"; "we expect to eventually start retiring our older API versions." | https://stripe.com/blog/api-versioning | confirmed | — |
| 26 | Adyen's versioning page names the expand-contract pattern for its own additive changes | https://docs.adyen.com/development-resources/versioning | confirmed | — |
| 27 | SDK versions that began to carry a version: stripe-node v12 (6 April 2023), stripe-ruby v9, stripe-python v6, stripe-php v11 (all 16 August 2023); earlier ones "use your account's default API version." | https://docs.stripe.com/upgrades ; the four SDK CHANGELOG.md files on GitHub | confirmed | The dates are in the changelog links on the page, not in its text; sentence now says so. Each changelog heading was read (12.0.0 - 2023-04-06; 9.0.0, 6.0.0, 11.0.0 - 2023-08-16) |
| 28 | For Java, Go and .NET the version "is *fixed*" to the SDK release | https://docs.stripe.com/upgrades | confirmed | — |
| 29 | Quote "Make sure that you specify the API version that you're integrating against in your code instead of relying on your account's default API version." | https://docs.stripe.com/upgrades | confirmed | — |
| 30 | Post of 1 October 2024, authors Michael Glukhovsky and Wissam Abirached; quotes "Historically, we've released new API features as soon as they're ready…", "Each semiannual major release—like Acacia—…", "Each monthly release adds new features without breaking changes." | https://stripe.com/blog/introducing-stripes-new-api-release-process | confirmed | — |
| 31 | A footnote: "We may introduce an out-of-cycle breaking change if we determine that your integration would be severely impacted without it." | https://stripe.com/blog/introducing-stripes-new-api-release-process | confirmed | It is footnote 1 of the post |
| 32 | Five majors: `2024-09-30.acacia`, `2025-03-31.basil`, `2025-09-30.clover`, `2026-03-25.dahlia`, `2026-09-30.endive` | https://docs.stripe.com/changelog | confirmed | — |
| 33 | Current version `2026-10-28.endive` as of November 2026 | https://docs.stripe.com/api/versioning | confirmed | "The current version is 2026-10-28.endive." |
| 34 | Change page title "Invoicing resources now specify how they were generated"; `quote`, `subscription`, `subscription_details`, `subscription_proration_date` removed from Invoice; quote "Use `invoice.parent.subscription_details.subscription` (verify `invoice.parent.type` is `subscription_details`) instead of `invoice.subscription`." | https://docs.stripe.com/changelog/basil/2025-03-31/adds-new-parent-field-to-invoicing-objects | confirmed | The prose says "deprecated", the Changes table says "Removed" |
| 35 | Post of 15 June 2026 (Mikael Mello, Anna Mason): "Due to the historical architecture of the v1 platform, it's not trivial to regenerate descriptions for non-current API versions"; for v2 "we also detect and display changes to past API versions (if applicable)." | https://stripe.dev/blog/how-api-changes-flow-into-stripes-developer-products | confirmed | Displayed date 2026.6.15. Neither sentence describes how responses are served: confirmed by reading the post |
| 36 | Table: versions named by release date, release name appended since 2024 | https://docs.stripe.com/api/versioning | confirmed | — |
| 37 | Table: account default confirmed; "the first-request rule is not restated on the pages I read" | https://docs.stripe.com/api-versions | corrected | Stripe's page "How API versioning works" says "Your default API version gets set the first time you make an API request." Cell now quotes it; source added |
| 38 | Table: `Stripe-Version` header overrides per request | https://docs.stripe.com/api/versioning | confirmed | — |
| 39 | Table: "Incompatible changes ship when ready, a few per version" as a 2017 claim | https://stripe.com/blog/api-versioning | hedged | The 2017 post says each version "contains a small set of changes"; "as soon as they're ready" is the 2024 post's description. Cell reworded to the 2017 wording |
| 40 | Table: the pin replaced for SDK users in 2023; Stripe advises setting the version in code | https://docs.stripe.com/upgrades | confirmed | — |
| 41 | Table: walking back through modules not re-described since 2017; no later statement on serving every version since 2011 | searched https://docs.stripe.com/llms.txt, the Stripe pages below, two web searches | confirmed (as an absence) | See "Could not verify" 1 |
| 42 | Versioning reference, upgrade guide, changelog and release-process post contain no retirement policy and no sunset notice | the four pages, plus https://docs.stripe.com/api-versions | confirmed | Text search of each for "sunset", "retir", "end of life" found nothing. Sentence now says "No Stripe source" and names the fifth page |
| 43 | Webhook documentation uses an account "set to an older API version, such as 2015-02-16" | https://docs.stripe.com/webhooks | confirmed | — |
| 44 | Quote "Each API URL contains a version suffix starting with either "v" or "V" character followed by a whole number… We increment the number for every version, but we may skip numbers when needed." | https://docs.adyen.com/development-resources/versioning | confirmed | Source has a link on "we may skip numbers" |
| 45 | "Most integrations use multiple Adyen APIs"; "Each API has a different version."; examples Checkout `v68`, account API `v6`, Balance Platform `v1` | https://docs.adyen.com/development-resources/versioning | confirmed | — |
| 46 | No account default at Adyen | https://docs.adyen.com/development-resources/versioning | confirmed | Follows from the version being in the URL; no default is described anywhere on the page or in the documentation index |
| 47 | Quotes "We implement non-breaking changes in all versions of an API…"; "When we introduce a breaking or incompatible change, we release a new API version." | https://docs.adyen.com/development-resources/versioning | confirmed | — |
| 48 | For Checkout, "we only release major versions." | https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | — |
| 49 | Quote "you should set up your server to be able to accept webhooks of more types and receive more event type values than are listed below." | https://docs.adyen.com/development-resources/webhooks/webhook-types | confirmed | Link on "accept webhooks". Date flag added: page metadata says last modified 2023-10-27. Source entry title corrected to the page's title, "Webhook structure and types" |
| 50 | Quote "We deprecate older versions to protect your data and maintain compliance with financial regulations." | https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | — |
| 51 | Lifecycle table: Active, Inactive, Deprecated (2 years), End-of-Life, four quoted cells | https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | — |
| 52 | Drop-in/Components lifecycle: one year from Deprecated to End-of-Life | https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | — |
| 53 | Release notes of 18 September 2026, under "Removed": "Checkout API v37 is no longer supported. If your integration still uses v37, you must upgrade your integration to the latest available version." | https://docs.adyen.com/online-payments/release-notes | confirmed | Entry "2026-09-18 — Checkout API"; the two sentences are a bullet and its sub-bullet |
| 54 | Quote "if you decide stay in your current version, you can continue to do so. We maintain older versions of our APIs…" | https://docs.adyen.com/development-resources/versioning | confirmed | Quoted as written (the page omits "to") |
| 55 | The two Adyen statements are not reconciled in the documentation | both Adyen pages | confirmed | Added: by page metadata the lifecycle page is the newer (2026-07-29 against 2022-01-18) |
| 56 | v71 dated 1 November 2023, v72 15 April 2026 | https://docs.adyen.com/online-payments/release-notes | confirmed | Also read: v70 30 January 2023, v69 24 May 2022 |
| 57 | No engineering source on how Adyen serves many Checkout versions | https://docs.adyen.com/llms.txt ; web search | confirmed (as an absence) | See "Could not verify" 2 |
| 58 | 2022 article: deprecation flagged "while the deprecated elements are deleted only after one or more versions"; evidence age 4 years | https://www.adyen.com/knowledge-hub/api-first-adyen | confirmed | Displayed date September 27th, 2022 |
| 59 | Lifecycle state of each version is shown in the API Explorer, "which I could not read" | https://docs.adyen.com/api-explorer/Checkout/latest/overview | corrected | The page can be fetched. It lists 17 versions from v40 to v72 and marks v72 "latest", and shows no lifecycle state in the served HTML. Sentence now reports this; source added |
| 60 | Quote "Requests made with curl use your Stripe account's default API version (controlled in Workbench) unless you override it by setting the `Stripe-Version` header." | https://docs.stripe.com/api/versioning | confirmed | — |
| 61 | A request version comes from three places; the most specific wins | https://docs.stripe.com/api-versions | confirmed | Was the author's reading of two pages; Stripe's page lists the three in order. Sentence and source added |
| 62 | Workbench shows "which API versions your integration uses" | https://docs.stripe.com/upgrades | confirmed | — |
| 63 | Quote "Webhook events also use your account's default API version unless you set an API version during endpoint creation" | https://docs.stripe.com/api/versioning | confirmed | — |
| 64 | Quote: the event "generated and sent to your destination is still based on the 2015-02-16 API version. You can't change Event objects after creation." | https://docs.stripe.com/webhooks | confirmed | Links on "Event" in the source |
| 65 | Two-endpoint cut-over: same URL plus a query parameter and the target version; "every event is sent twice…"; 400 on the old endpoint so that "Stripe automatically resends all the events"; then disable it | https://docs.stripe.com/upgrades | confirmed | — |
| 66 | "Thin event payloads are unversioned." | https://docs.stripe.com/upgrades | confirmed | — |
| 67 | Adyen libraries: "without needing to know the API versions. Instead, you need to consider the library version"; each release names its API versions in the release notes | https://docs.adyen.com/development-resources/versioning | confirmed | — |
| 68 | Adyen webhook configuration has a "Version" setting described as "The webhook version." | https://docs.adyen.com/development-resources/webhooks/configure-and-manage | confirmed | — |
| 69 | No Adyen statement on how long old webhook versions are delivered | https://docs.adyen.com/llms.txt ; web search | confirmed (as an absence) | — |
| 70 | "Web Drop-in/Components v5.0.0 is only compatible with Checkout API v68 or later." | https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | Links inside the sentence |
| 71 | Stripe.js has named versions, released twice a year, set in the script URL or the npm package | https://docs.stripe.com/sdks/stripejs-versioning | confirmed | — |
| 72 | "Where They Differ", six rows, Stripe and Adyen cells | rows above | confirmed | Additive-changes row: Stripe cell now also carries the documented advice to ignore "unfamiliar fields and event types". "Not public" cells checked against both documentation indexes |
| 73 | Versioning reference: "match your webhook endpoint API version to the version pinned by your `stripe-ruby` version" | https://docs.stripe.com/api/versioning | confirmed | The source sentence continues; the period moved outside the quotation |
| 74 | Strongly typed SDKs: a mismatched version can "result in request failures" | https://docs.stripe.com/upgrades | confirmed | — |
| 75 | "The Stripe pages I read do not say whether new fields reach older versions" | https://docs.stripe.com/api-versions | corrected | Stripe lists "Adding new properties to existing API responses" and "Adding new event types" as backward-compatible and says "Design your integration to ignore unfamiliar fields and event types." It still does not say outright that these reach older versions; the sentence now gives both facts and keeps the assumption labeled |
| 76 | Stripe's dynamically typed SDKs accept a version per client or per request | https://docs.stripe.com/upgrades | confirmed | Ruby: per client or per request; Python, PHP, Node: globally or per request |
| 77 | Adyen upgrade guides step by step: to v69 from v68, to v70 from v69, to v72 from v70 or v71 | https://docs.adyen.com/online-payments/upgrade-your-integration | confirmed | — |
| 78 | Take-aways (Established), four bullets | rows 11, 13, 1, 2, 47, 63, 68 | confirmed | — |

Counts: 78 claims checked; 70 confirmed, 3 corrected (37, 59, 75), 3 hedged (10, 17, 39), 0 unsupported, 0 unreachable. Rows 41, 57 and 69 are confirmed absences, which is weaker than a confirmed statement.

## Could not verify, and what I did

1. **Whether Stripe has retired any dated API version.** No Stripe page I fetched says so, and the changelog still lists versions back to `2011-06-21`. A web search returned a Fivetran community post titled "Stripe connector is using API versions that are going EOL" (`support.fivetran.com/hc/en-us/community/posts/42178808979223`). It returns 403 to curl and to the fetch tool and has no archived copy, so I could not read it; the search summary describes a user complaint about the connector's pinned 2019 version and cites no Stripe notice. It is a third-party post and not evidence, but it is a lead against the chapter's "no retirement notice" reading. The article now says "No Stripe source I could find". The author may want to open that post in a browser.
2. **How Adyen serves its Checkout versions.** One web search and the documentation index found nothing beyond the 2022 article already cited. The claim stays as "I found no engineering source".
3. **Lifecycle state of Checkout API v71.** Not in the served HTML of the API Explorer. The article already declines to state it.
4. **Page metadata dates.** Adyen's `.md` pages carry a `last_modified` field: versioning 2022-01-18, webhook types 2023-10-27, upgrade page 2026-07-29, webhook configuration 2026-11-17. The release-notes page says 2023-01-12 while holding entries to October 2026, so the field is not a reliable content date. I report it as metadata in the text and the source entries and keep the citations as "n.d." (ruling 25).

## Rulings and format

- Ruling 22: no external URL in the running text (checked by search).
- All `[[permalink]]` links are in the valid list. Exactly three key points; three failure patterns; callouts in order; required sections present.
- Word count from `check_draft.py structure`: 6,293 (was 6,084), under the 6,500 limit; `timetoread` changed from 26 to 27 min.
- No unit added, dropped, merged or reordered. Two controlling ideas and one source line in `spec.json` reworded to match the corrections; changelog entry added.
- `validate_spec.py` passes; `check_draft.py structure` passes; build has no error; `render_check.py payment-api-versioning` is OK.

## Larkfield consistency

- Tuesday 9 March 2027 is a Tuesday; €120.00 pass, Studio Noord on Adyen: agree with the ledger.
- The Version Cliff: March 2026, account default `2022-11-15` last moved early 2023, library carrying `2026-02-25.clover`, `subscription` on the Invoice removed in `2025-03-31.basil`, six days, webhook endpoint on the account default: agree with ledger line `19-api-versioning`.
- **Fixed:** "Until March 2026 the code … belonged to the growth team" read as if ownership changed in March 2026. The ledger says the growth team owned the billing integration until 2027 and chapter 27 moves it in May 2027. The sentence now ends "Until March 2026" on the missing version, not on the ownership.
- K7, the register, May and November upgrades, the webhook endpoint a week later, Adyen Checkout v71 integrated in 2024, Tom Hendriks: agree.

## Ledger conflicts

None.

## For other pages

- `brief-stripe-payments-and-api.md` does not list `https://docs.stripe.com/api-versions` ("How API versioning works"). Chapters 17, 20 and 21 may state that Stripe's documentation does not restate the first-request pin or does not tell integrators to ignore unknown fields; that page does both. It also says the API version governs "Automated Billing operations that Stripe performs on your behalf", which bears on chapters 27 and 41.
- The same page says that versioned Stripe.js "automatically uses the API version associated with the Stripe.js version" and that this cannot be overridden (`docs.stripe.com/sdks/stripejs-versioning`); relevant to chapter 21.
