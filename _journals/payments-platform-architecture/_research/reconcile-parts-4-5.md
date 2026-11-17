# Reconcile log — parts 4 and 5 (17 November 2026)

Scope: `part-4.json`, `part-5.json`; pages `part-4-intro`, 17–21, `part-5-intro`, 22–26. No chapter thesis claim and no part thesis claim was changed. Every journal-entry change below was copied word for word into the page spec, with one changelog entry per spec.

## Part IV fragment (`part-4.json`)

Part-level fields
- `opening.hook.content`: "Four of Larkfield's eight incidents in 2026 happened at the provider's API" → "Four of Larkfield's eight incidents happened in 2026 at the provider's API" (ruling 24). Same in `part-4-intro/spec.json`.
- `closing.so_what`: "a nightly reconciliation runs" → "reconciliation against the provider's reports runs" (ruling 28; ledger `[editor]` line 1). Same in `21-developer-platform/spec.json` (conclusion) and in the closing paragraph of `21-developer-platform/index.md`.
- `thesis.how_why`: "published only in part, mostly in Stripe engineering posts from 2017" → "much of it in Stripe engineering posts from 2017" (part-4-intro verification, row 3). Same in `part-4-intro/spec.json` (thesis and one evidence note).

`payment-api-design` (17)
- `intent.outcome.know[1]`: "several API families with their own hosts, version counters, pagination and error formats" → "several API families with their own version counters and, in most cases, their own hosts, pagination and error formats" (verification rows 51 and 77: two platform APIs share a host, three APIs share an error format). Also supporting claim C3 in the page spec.

`idempotency-and-retries` (18)
- Journal entry: no change needed (the Adyen 2021 passage was already in it).
- Cross-page fix (ruling 30): six "last modified" dates removed from the running text of `index.md` and five from Sources, with the evidence-age notes built on them; Adyen documentation is now "n.d., accessed November 2026". In `spec.json` the same stamps were removed from 23 evidence and source strings, and two source titles corrected ('Response handling' → 'HTTP status codes'; 'Terminal API fundamentals' → 'Terminal API').

`payment-api-versioning` (19)
- Journal entry: no change needed.
- Cross-page fix (ruling 30): two metadata dates removed from the running text; the sentence that chose the lifecycle page partly because "by the pages' metadata it is the newer of the two" now rests on the two remaining reasons (more specific; the release note agrees); three "page metadata: last modified" notes removed from Sources. Spec unchanged (its unit already gives only "the more specific").

`payment-webhooks-and-events` (20)
- Journal entry: the three fields its verifier flagged (know[1], AC-1, so_what) were already scoped to "Checkout API for online payments" (ruling 29). No change.

`payment-developer-platform` (21)
- `AC-3`: "no published payment rate limits or limiter design exist for Adyen" → "no published payment rate limits and no limiter design were found for Adyen" (verification row 38: an absence cannot be asserted as fact).
- Sources: Adyen entry 'Response handling' retitled 'HTTP status codes' (the page's displayed title).

## Part V fragment (`part-5.json`)

Part-level fields
- `opening.hook.content`: "the studio could not take payments for 31 hours" → "could not sell online for 31 hours" (ledger: only online payments were switched off). Same in `part-5-intro/spec.json`.
- `closing.callback`: "one studio paused for 31 hours by a fraud control" → "one studio's online payments paused for 31 hours in the response to a fraud attack" (chapter 26 verification; the page spec of chapter 26 already had this wording).
- `AC-4 expected`: "(Stripe says Radar is available only with client-side tokenization)" → "(Stripe's PCI guide says Radar is available only with client-side tokenization; its API reference says Radar performs best with it)" (chapter 22 verification, row 60).

`tokenization-vaulting-and-pci` (22)
- `thesis.how_why`: "while no public Adyen export procedure was found" → "while Adyen's help center lists an export article whose procedure could not be read in November 2026" (ruling 31a). Page spec: also supporting claim and two controlling ideas.
- `index.md`, Where They Differ table, "Export of stored cards", Adyen cell: "Not public" → "Help-center article listed; procedure not readable". Word count 6,498 of 6,500.

`network-tokens` (23)
- `AC-2 expected`: "while secondary sources quote about six percent" → "while a secondary source attributes about six percent to Visa" (verification rows 52 and 56: one source, CMSPI, citing a different Visa text). The `how_why` correction on Stripe's read-only field (ruling 35b) was already in place.

`payment-fraud-and-risk` (24)
- `AC-3`: "both companies' merchant underwriting ... are not public" → "both companies' criteria and models for accepting a merchant ... are not public" (verification row 76: Adyen documents its deposit calculation in outline).
- Page spec body: supporting claim and the comparison section's controlling idea no longer say both companies "document ... holdouts"; they say Adyen states one and Stripe's documentation only implies it (row 37). The "not public" unit lists what merchant underwriting covers.

`three-d-secure-and-sca` (25)
- `AC-3`: "marks scheme passkeys as pilots" → "marks scheme passkeys as in pilot or first rollout" (row 3).
- `thesis.how_why`: "documented at Adyen as a pilot; nothing was found for Stripe" → "documented at Adyen as a pilot, with a first rollout in the UK announced on 29 October 2026; for Stripe only an undated support article on Stripe Authentication, a device-verification method in trial, was found, and no selection among methods" (rows 97, 103, 118).
- Page spec body: paragraph p35 controlling idea changed the same way.

`payment-compliance-and-regulation` (26)
- `thesis.how_why`: the sentence "That difference, Stripe documenting rule changes and Adyen documenting the periodic review, is what the public record shows. How either company ... schedules re-verification is not public" now says that Stripe's periodic re-verification is announced (support article, last updated October 2026) and in preview, that Adyen announces rule changes in release notes without an API structure, and that the intervals of re-verification are not public (ruling 36; rows 86 and 88).

## Placeholder fixes

- `part-5-intro`, figure `part-5-no-cards-held-still-a-bill`: the prompt drew "a closed sign", and the alt text said "a studio closed for 31 hours". The studio was open; its online payments were off. Visual goal, prompt and alt now show online sales off for 31 hours. The JSON parses.
- No other placeholder in scope draws a fact that a ruling changed.

## Checked and left unchanged

- Rulings 20, 24, 27, 29, 31b–d, 32, 33, 34, 35, 37, 38, 40, 41, 42, 43, 44, 45: no statement in the old form was found in the twelve pages (searched by pattern). "Checkout API has no call that returns a payment" is scoped wherever it appears.
- Hand-offs use `[[part-5]]`, `[[part-6]]` and chapter permalinks; no external URL in running text; `timetoread` equals words ÷ 230 on all twelve pages.
- Chapter 21 does not mention Adyen's "Peak season readiness" page (ruling 42a: load testing with merchants, utilization "generally less than 30%"). Nothing on the page contradicts it, and the page is at 4,983 of 5,000 words, so no sentence was added.

## Part-claim clause for the author (not changed)

- **Part V thesis claim**, clause: "3-D Secure moves the fraud loss to the issuer when the payer is authenticated and leaves it with the merchant on every payment that is exempted or merchant-initiated".
- Evidence: chapter 25 (section on who asked, verified): when the issuer applies the low-risk exemption itself, Adyen's documentation says "The chargeback liability shifts to the issuer", and its Mastercard table gives "Yes" where the "issuing bank applies a PSD2 exemption without the merchant or acquirer requesting for it". Stripe's page reads differently; the chapter treats the two as different payments. Supporting claim P5-4 already says "leaves it with the party that asked".
- Suggested wording: "... and leaves it with the merchant on every payment that is merchant-initiated or exempted at the request of the merchant's side".

## For the author (carried from verification, not acted on)

- Chapter 17: ruling 1 gives the chapter one sentence and a link on where payment state lives; the page spends a key point, a paragraph, a figure, a table row and a take-away on it. Cutting would drop units.
- Chapter 22: the Sources entry for Adyen's help-center export article is a link that redirects by design.
- Chapter 26: Stripe's KYC Refresh and the PSD3/PSR status should be re-checked before print.

## For other scopes

- None found that the rulings do not already cover.

## Validation

- `validate_spec.py payments-platform-architecture`: `ok` for the journal spec and every page spec.
- `check_draft.py structure`: pass on all twelve pages. Placeholder extraction parses on all twelve.
- Build: no error; the only warnings are for pages not yet written (introduction, part-10-intro, 48, reference pages).
