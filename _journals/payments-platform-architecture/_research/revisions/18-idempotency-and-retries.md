# Revision log — 18-idempotency-and-retries (draft check round 1, ESCALATE)

Revised 2026-11-17. 28 failed results (1 waived). One line per failed result. No fact, number, date, quotation, hedge, figure, caption, source entry or `[[link]]` changed. Words 6,089 before, 6,389 after (limit 6,500, unchanged). `timetoread` 26 to 28.

## one_controlling_idea_per_paragraph

- Retry Policy ¶2 (headers + declines/rate limits), spec fault: repaired. Split into p31 (the providers' retry headers) and new p54 (a decline and a rate limit are not unknown outcomes), with the connecting sentence "Those headers concern failures whose outcome is unknown."

## evidence_is_explained

- Server memory ¶4, requirements table: fixed; the sentence introducing it now says the requirements are why the window is finite.
- Choosing the Key ¶1, key-source table: fixed; p24 says what it shows (only a stored or derived key survives a restart or redelivery; only a derived key survives a second trigger without a lookup).

## transition_expresses_declared_relationship

- Scene ¶1, "For example": fixed ("Larkfield learned the chapter's condition, the same stored key on both sends, by breaking it.").
- Choosing the Key ¶2, "Against this": fixed ("Against the table's first row stands the view that a key per call is enough …").
- Choosing the Key ¶6, "Finally": fixed ("A stored key that any path can find raises the question of how late a path may use it, …").
- Retry Policy ¶3, "In short" (spec fault): repaired; relationship changed to sequence and "In short" dropped ("For the failures that are retried, retrying also needs an end.").
- Downstream ¶5, "The middle": fixed; p36 now frames its two documented cases as the two ends of the chain (the card reader; the merchant's own reference), and p37 opens "The providers' own side of those calls, however, is not public."
- What to Take Away, no pickup: fixed ("**Established.** Behind every failure above and its fallback stand a few settled facts.").

## flow_is_followable

- Scene ¶1, "For example": fixed (above).
- Server memory ¶5, "For example" and "the second contract": fixed ("One design … implements the second contract, the one that carries unfinished work to completion").
- Server memory ¶6, inference before the regional fact (spec fault): repaired; the INFERENCE block moved after the Adyen paragraph (p22) that reports the regional rule, in spec (evidence moved p17 to p22) and prose.
- Server memory ¶6, "after endpoint execution begins" quoted before its source (minor): fixed ("what marks the point, quoted in the next section, after which Stripe saves a response").
- Server memory ¶6, detour (minor, spec order): opening rewritten so the move is motivated ("Whether either company builds its store this way is not on record: …"); unit not moved.
- Scene ¶3, "one writer" (minor): fixed (below).
- In Practice ¶5, the Mila conflict: fixed from the ledger: "Mila Janssen, whose €120.00 class pass this chapter follows, also holds a €49.00 monthly membership at Studio Noord, which is on Adyen, renewed on the 1st of each month. Her renewal of 1 April 2027 …".
- Choosing the Key ¶2, "this" (minor): fixed (above).
- Retry Policy ¶3, "In short" (minor): fixed (above).
- Downstream ¶2, capture gloss inside a quotation-heavy sentence (minor): fixed; the gloss is its own clause after "captures and refunds".
- Downstream ¶4, "the API's edge" reverses direction: fixed; the cancel by reference is named as the merchant's end of the chain, "for when Adyen's identifier for the payment never came back" (chapter 2's wording of Adyen's cancel page; verification row 69).
- Downstream ¶5, "The middle": fixed (above).
- In Practice ¶4, K2 and the sweep: fixed ("the sweep of Keel decision K2, a job that finds every attempt still pending and confirms it against the provider's own record"; ledger K2).
- Choosing the Key ¶5, random UUID vs derived key (minor): fixed ("what must come from the business event is the key's identity, not its value").
- Where They Differ table, "pause, or resend without the key" not yet cited (minor): fixed; the Adyen paragraph (p22) now names the two choices and says they are quoted in the failure section, which refers back to them.
- In Practice ¶4, Checkout API has no read first appears in the replay (minor): fixed; the recommendation after the comparison table says it for Adyen.
- Where They Differ position: waived (house format); transition strengthened ("With the mechanism, the documented terms, the client's choices and the limits of a key all set out, the two providers can now be compared on one page: …").

## known_before_new

- "idempotency key" before its gloss: fixed; glossed at first use in IN THIS CHAPTER, KEY POINTS and the opening paragraph; the scene's later gloss removed.
- "one writer": fixed ("meaning that every money-moving call goes through the payment service"; ledger K1).
- K2 and the sweep: fixed (above).

## Content corrections

- None.

## Checks

- `validate_spec.py payments-platform-architecture 18-idempotency-and-retries`: ok.
- `check_draft.py structure`: pass, 6,389 words (limit 6,500). Build not run (brief, change 6).
