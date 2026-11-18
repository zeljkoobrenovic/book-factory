# Revision after draft check, round 1 — 38-payment-data-stores-and-consistency

Date: 2026-11-17. Report judged: round 1, 28 failed results (19 major, 9 minor). One line per failed result. Words: 6,423 before, 6,775 after; `max_words` raised 5%, 6,500 to 6,825. `timetoread` 28 to 29. Apart from the correction listed under "Content", no fact, number, date, quotation, hedge, figure, caption, source entry or `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- p26 bundles the limits and the Cockroach store (spec): split. The Cockroach sentences became p46, placed after p24 (both are stores at Adyen's edge; the new unit opens "The same edge holds one more store, and it serves the other half of keeping money right: recognizing a repeated request"); p26 keeps only what is not public and closes the section, as the section flow requires. Spec p26 evidence and p46 added; section flow note updated.

## evidence_is_explained

- Incident 2016 anecdote: fixed; the note on the number now follows the quotation and the unit ends "So dividing data inside one database keeps the transaction whole, but it still has an operational cost, and on a critical store that cost came close to an outage." Spec p25 aligned.

## transition_expresses_declared_relationship

- Scene opens on a gloss of Larkfield: fixed; "At Larkfield ... no consistency boundary had been drawn at all between a payment and what it pays for." Spec p06 aligned.
- Stripe section opening: fixed; "The first published account of living with those costs is Stripe's, in the 2024 post quoted at the start of this chapter."

## flow_is_followable (major)

- 2017 migration paragraph in the Stripe section (spec): kept in place (the spec's section flow keeps Stripe's dated evidence here and the term is defined before Larkfield uses it); the unit now opens "Stripe has published a second kind of move, the one Larkfield's own migration follows at the end of this chapter." Spec p18 aligned.
- Larkfield's schema migration not in the roadmap (spec): fixed; roadmap sentence and spec roadmap promise now name "a change to that store's shape made while it runs"; the migration unit opens "The outbox changed how the store announces a payment; Keel also changed the store's own shape". Spec p05, p37 transition aligned.
- Square/TigerBeetle detour (spec): kept within its section, reframed to support the section's point ("The trade can also be avoided by not sharding the money at all") and closed with a hand-off ("Stripe and Adyen both sharded, and the next two sections report what that cost them") instead of the sentence that undercut it. Not moved to Where They Differ (house-format section; only one reader proposed it). Spec p14 aligned.
- "the coordinator": fixed; replaced by "The platform"; version gating glossed ("a version number attached to each chunk's route") and summarized ("a shard refuses requests that carry an older version").
- PAL parenthetical burying the main clause: fixed; the two expansions moved to a closing parenthesis.
- Partitioning paragraph's purpose: fixed (see evidence_is_explained).
- "The table has a row neither company fills in": fixed; "Neither column of the table describes a transaction that covers more than one shard or cluster, not even in the row on moving money across shards, and no post of either company mentions one." Spec p29 aligned.
- "so take Mila's pass" / decision never narrated: fixed; "Femke's three questions led Larkfield to an outbox in place of Tom's distributed transaction, and it has been live since 1 March 2027. Take Mila's pass." (ledger). Spec p35 aligned.

## flow_is_followable (minor)

- "the latter" in the Adyen quotation: fixed; "(“the latter” in the quotation)" attached to the edge.
- Whose system the table describes: fixed; "The table below puts this in a merchant's terms; it is my reference version for a merchant's system such as Larkfield's".
- "The last step of that reading": fixed; "That these four are how both keep money right is my inference". Spec p03 aligned.
- "under the provider's API": fixed; "Larkfield's, and the provider's own databases behind its API".
- Why the fee-credits post is included: fixed; "The nearest Stripe comes to describing money moving between its own accounts". Spec p20 aligned.
- Cockroach as an afterthought (spec): fixed by the split (p46).
- Adyen partner reports new in the inference section: fixed; "which the same 2021 account says became after sharding". Spec p31 aligned.

## known_before_new

- Keel, K2, K3: fixed; Keel glossed at first use in the scene (2027 program of eight decisions, K1 to K8), K3 glossed with its ledger wording. Spec p06, p08 aligned.
- Clearing account: fixed; glossed in the scene.
- Consistency boundary before its definition: fixed; glossed in the introduction ("the line around the records that change together in one local transaction") and in the failure-patterns callout (rule 3). The key-points callout already says what it is ("which records change together in one local transaction").
- Chunk: fixed; "a chunk is a slice of a collection's data that is placed, and moved, as one unit". Spec p15 aligned.
- Rebalancing: fixed; "moving data to even out the load, called rebalancing".
- Two-phase commit: fixed; glossed before the quotation.
- Partitioning and shards before definition: fixed; shards glossed in place with "described below".
- "detection": fixed; "it finds an error after it happened, where prevention would stop it being written".
- First-of-month renewal run: fixed; "the day member renewals are charged".

## AC-2

- Adyen's messages not tied to idempotency and checking: fixed, labeled as the author's reading: "any such message can fail or arrive twice, so, by my reading, each must be safe to apply twice and must be checked afterwards, the two needs this chapter returns to below." Spec p23 aligned.

## Content

- None changed. (The "row neither company fills in" sentence was contradicted by the table; it now says what the table shows.)

## Not changed

- No failure judged wrong.
