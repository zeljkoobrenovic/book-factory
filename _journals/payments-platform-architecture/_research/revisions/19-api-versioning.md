# Revision after draft check, round 1 — 19-api-versioning

Date: 2026-11-24. Report judged: spec `1427c4424be60ee6`, draft `4298cccc9aa0ce0e` (20 failed results: 1 blocker, 16 major, 3 minor; 1 waived). One line per failed result. Words: 6,271 before, 6,730 after; `max_words` raised 4.6% (6,500 to 6,800). `timetoread` 27 to 29. Apart from the editor-authorized changes listed, no fact, number, date, quotation, hedge, figure, caption, source entry or `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- p31 (what Adyen has not published, plus where a lifecycle state is read): spec repaired. Split into new p53 (the state is read in API Explorer; the fetched copy showed none) and p31 (Adyen has published almost nothing on serving versions); prose split at the same point, with a connecting sentence.

## known_before_new

- Scene ¶3, "the Keel program", "K7": fixed. Keel and K7 glossed from the ledger (2027 program, eight numbered decisions; the seventh, versions upgraded on a calendar); Femke's role and start glossed; K7 re-glossed at the start of the practice section.
- Scene ¶2, plant suffix, "named major releases"; "monthly versions", "the major version Basil": fixed. The scene glosses the release-name scheme (two plant-named majors a year since October 2024); "monthly versions" glossed as the releases between majors; Basil glossed where named in the second section.
- Stripe 2017 ¶2, "an authorized application": fixed ("an application authorized to act for the account").

## flow_is_followable (major)

- Scene ¶1, which provider: fixed from the ledger: Larkfield takes members' payments through Adyen and Stripe and bills studios with Stripe Billing; the scene's provider is Stripe.
- Scene ¶2, webhook endpoint aside: fixed. The sentence now says Stripe versions events separately from requests (explained later) and what that meant for the handlers.
- Scene ¶2, "four dated versions and three named major releases": fixed. The count is explained (from `2022-11-15`, four dated versions, then Acacia, Basil, Clover; verification row 5); the practice section refers back to "the scene's" count.
- Scene ¶3, jump to 2027: fixed with a bridge ("Larkfield's story continues a year later, in 2027").
- Adyen ¶1 / Stripe 2017 ¶1, mapping to the designs: fixed. Stripe is named as an instance of the second design and Adyen of the third (the spec's flow rationale and the Adyen section's `advances_thesis`).
- 2023–2024 ¶4, tooling post before the table: fixed in prose and spec. The 2026 tooling-post fact moved after the table, into p26 (spec evidence moved from p25 to p26); p25 now announces the table.
- Table row "small set of incompatible changes" not stated in 2017 section: fixed. p17 prose now states it in the table row's verified wording (verification row 39), as the spec's controlling idea already did.
- Adyen ¶5, "showed no lifecycle state, so check there": fixed in the split unit p53 ("So I report no state here; look up the version you call in the Explorer itself").
- Where They Differ ¶1, cells not yet cited: fixed. The Stripe.js fact is now stated before the inventory table (its source was already in Sources; verification row 71); the comparison lead says the "unfamiliar fields and event types" advice is quoted in the section on what goes wrong. Spec p37 `shows` updated.
- In Practice ¶1, "the previous section's inventory": fixed ("the inventory table from the section on where a version is set"); spec p39 updated.

## flow_is_followable (minor)

- Position of Where They Differ: waived (house format); transition strengthened ("With every place a version is set now cited, the two models can be compared").
- Designs ¶4, shared property vs. the first design's switch-off: spec repaired (p16) and prose qualified ("for as long as the design allows, which in the first is only to the switch-off date").
- Introduction ¶2, the provider did not "stop remembering": fixed with one sentence ("The provider did not forget the version; a dependency replaced it.").
- When It Goes Wrong heading names three failures, section counts four: spec and prose repaired. Heading now "Split Versions, Silent Nulls, Strict Parsers and Forced Jumps"; the section opens by naming four ways; the third and fourth paragraphs name the strict parser and the forced jump.

## conclusion_calls_back_to_introduction

- Fixed. A third synthesis bullet returns to the March 2026 upgrade and the idempotency key's retention window, answering the opening question; spec p50 notes the callback.

## AC-3 (blocker)

- FAILURE PATTERNS callout, "Stripe's machinery for serving every old version answers": fixed as the editor directed. Now "the machinery Stripe described in 2017, nine years ago, for serving every old version answered …".

## Content corrections

- None beyond the above. The callout change dates an undated claim; the Stripe.js sentence and the "small set of incompatible changes" sentence restate facts already on the page and in the verification file.

## Checks

- `validate_spec.py payments-platform-architecture 19-api-versioning`: ok. `check_draft.py structure`: pass, 6,730 words. Build not run (brief, change 6).
