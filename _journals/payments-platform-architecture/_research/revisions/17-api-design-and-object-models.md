# Revision log — 17-api-design-and-object-models (draft check round 1, ESCALATE)

Revised 2026-11-24. Report judged: spec `check-report.json` round 1 (15 failed results: 13 major, 2 minor). One line per failed result. No fact, number, date, quotation, hedge, figure, caption, source entry or `[[link]]` changed. Words 6,397 before, 6,591 after; `max_words` raised 1.5% (6,500 to 6,600). `timetoread` 27 to 29.

## evidence_is_explained

- p23, now-and-later table not read for the reader: fixed. The sentence before the table says how to read it ("find the operation's row, then the channel that carries the second half of its answer"), and the dispute and settlement glosses follow as "In it, …".

## transition_expresses_declared_relationship

- When It Goes Wrong ¶1, contrast with the working adapter missing: fixed ("The adapter above works because every response arrives; the failures begin where one does not, and the one with money in it is the lost response.").

## flow_is_followable

- Introduction ¶1, "there is … reach it": fixed. The Stripe record is named ("the provider's own payment object") and "it" now reads "that object".
- Object model ¶3, "By contrast with the names": fixed ("The names differ in style; the larger difference is what a name lets you read.").
- Object model ¶6, `/v1` and `/v2` before introduction (spec fault): repaired in spec and prose. p15, the first use, glosses the two namespaces in one sentence (path prefixes with their own conventions; `/v1` holds most of the API, payments included; `/v2` added in 2024); p25 now refers back ("the two namespaces met above").
- Error model ¶5, "In the table" with no referent: fixed with the reading sentence above, which introduces the table before the glosses.
- Error model ¶6, "As a result": fixed ("Stating this line has a cost: …").
- Two Shapes ¶5, uniformity on a different axis from the table (minor, spec fault per judge): fixed in prose without moving the unit ("The table leaves out the axis on which such APIs are usually judged: uniformity."; "the table's row on what you must learn concedes it"); p29's transition_in updated.
- Design practice ¶2, "moreover": fixed ("Stripe has also described how changes to its API are reviewed, in far less detail.").
- Design practice ¶1, "the same 2020 post": fixed; the post is named by author, month and title, the evidence-age mark moved before the sentence that introduces the quotation, and the later Adyen post is "a 2020 Adyen post".
- In Practice ¶2, `pending` vs `authorized` (minor): fixed; the row stays `pending` "because the result code is not allowed to move it", and there is no step through `authorized` "because the account captures automatically" (ledger: captured automatically; chapter 8's mapping).

## known_before_new

- "webhooks" in KEY POINTS and Introduction ¶1: fixed; glossed at both first uses (callout gloss allowed by change 3).
- "settlement report" in the scene: fixed; glossed from the glossary ("the provider's itemized file of what it has settled and paid").
- PaymentIntent and Charge (fault unclear): fixed in draft; the Charge is named as "Stripe's first payment object" (spec p09) and the PaymentIntent glossed where named (glossary: carries one payment through its states, keeps each attempt as a Charge).
- `merchantReference`: fixed ("the field in which Adyen returns your `reference`"; Sources already cites Adyen's webhook-types page for it).

## Also fixed (same kind, not flagged)

- Two take-away bullets opened with misleading connectives ("By contrast with those facts", "In addition"); removed.

## Content corrections

- None.

## Checks

- `validate_spec.py payments-platform-architecture 17-api-design-and-object-models`: ok.
- `check_draft.py structure`: pass, 6,591 words (limit 6,600). Build not run (brief, change 6).
