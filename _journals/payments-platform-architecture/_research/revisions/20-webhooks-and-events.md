# Revision after draft check, round 1 — 20-webhooks-and-events

Date: 2026-11-17. Report judged: spec `1bed38f356c44be7`, draft `af75703a08bd96c5` (11 failed results: 8 major, 3 minor; 1 waived). One line per failed result. Words: 6,022 before, 6,389 after (`max_words` 6,500, unchanged). `timetoread` 26 to 28. Apart from the editor-authorized changes listed, no fact, number, date, quotation, hedge, figure, caption, source entry or `[[link]]` was changed. One `[[platform-payment-models]]` link was added with the gloss of Adyen for Platforms.

## evidence_is_explained

- Promises table: fixed. A lead-in at the end of p12 says what the table collects and points ahead for its two rows the section does not argue (signatures, a later section; changes with no event, such as Adyen's successful settlement, in the receiver section). Spec p12 evidence notes it.

## transition_expresses_declared_relationship

- Receiver ¶1, "these limits": fixed. The section now opens by naming what a sender can promise, whichever way it is built (repetition in a window: duplicates, disorder, stale payloads, burst or gap, silence), then says the receiver's design answers those limits.
- When It Goes Wrong ¶4, "The opposite failure": fixed. It now picks up "genuine events … misread" (the spec's carries_over) and names the reverse, a genuine event your own verification rejects.

## flow_is_followable (major)

- Signatures ¶1, "One term of the contract is left" after "The last term": fixed ("The last delivery term"; "Beyond the delivery terms, one term of the contract is left").
- Position of "What Building the Sender Involves" (spec, both readers): not moved (sections never move). Transitions strengthened on both sides: the sender section opens on the two behaviors it explains (Adyen's burst, Stripe's disorder); the receiver section opens on what any sender can promise. The roadmap now says why it comes there. For the editor (below).
- Contracts ¶2, "After a few more attempts the webhook is set to Failing": fixed against verification row 15. The two Adyen pages differ: the handling guide marks the webhook Failing once 10 seconds pass; the troubleshooting page says “We retry sending the webhook message a few more times before we set the status of the webhook to Failing”. The paragraph now quotes the troubleshooting page and says the two pages differ on when Failing begins.
- In Practice ¶3, row `paid` before confirmation: fixed (content correction, editor-authorized). The example now runs the confirming step: the stored, verified `AUTHORISATION` notification is the record Adyen has given (no Checkout API read-back, rulings 12 and 29); the row moves to `paid` with Adyen's own events as its source, which changes to the report when the settlement report confirms it (ledger K2; chapter 17 ledger line, `confirm` returns `own_events`, later `report`, on Adyen); ledger entries still come from the report (ruling 28). The receiver rule (p31) now says the same for Adyen. Spec p31 and p37 reworded.
- When It Goes Wrong ¶3, "A third failure": fixed ("Outages and their recovery delay or lose events. Disorder, the next failure, misleads without losing anything.").

## flow_is_followable (waived)

- Position of Where They Differ: house format; no change needed beyond the existing opening sentence.

## known_before_new

- Contracts ¶3, transfer webhooks and the platform product: fixed. Glossed as Adyen for Platforms, Adyen's product for platforms such as Larkfield, whose transfer webhooks report movements of funds on its balance platform, the layer that keeps each seller's balance (glossary rows on the platform product and the balance platform).
- Contracts ¶3, "snapshot event" in a quotation before its definition (minor): fixed with a clause before the quotation (the kind that carries a copy of the object, described later).
- In Practice ¶3, Larkfield on Adyen / Mila's provider (minor): fixed in the introduction's Mila paragraph ("Studio Noord takes its online payments through Adyen, Larkfield's other provider besides Stripe"; ledger).

## conclusion_calls_back_to_introduction

- Fixed. The "Silence is a state of its own" bullet now returns to 14 September 2026: Stripe's retries delivered every event; a receiver that read nine hours of silence as "unknown, go and read" would have kept the doors open.

## Heading "Forgery" with no forgery case (editor's point)

- Fixed in spec and prose: the heading is now "Long Outages, Bursts, Disorder and Failed Verification", which is what the section covers. No forged-event case was added.

## For the editor

1. Section "What Building the Sender Involves, and What Nobody Has Published" (spec `/sections/5`), quote: "All of this is the contract as seen from the receiving side, and the receiving side is all there is to see." Both flow readers would put it directly after "The Two Delivery Contracts, Term by Term". Recommendation: move it there. Its only evidence is the retry and order terms of that section, and the two behaviors it explains (burst, disorder) are introduced there; signatures and payload do not depend on it, and the receiver section would still follow from it through the payload section with no change to its opening. The spec's flow rationale would need one sentence changed. Transitions are strengthened in place meanwhile.

## Checks

- `validate_spec.py payments-platform-architecture 20-webhooks-and-events`: ok. `check_draft.py structure`: pass, 6,389 words. Build not run (brief, change 6).
