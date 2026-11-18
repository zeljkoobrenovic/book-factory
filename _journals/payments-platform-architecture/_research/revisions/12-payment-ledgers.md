# Revision after draft check, round 1 — 12-payment-ledgers

Date: 2026-11-17. Report judged: round 1, 23 failed results (17 major or blocker, 6 minor). Words 6,241 before, 6,701 after; `max_words` raised from 6,500 to 6,750 (3.8%). `timetoread` 27 to 29. Apart from the corrections listed below, no fact, number, quotation, hedge, figure, caption, callout, source entry or `[[link]]` changed.

## one_controlling_idea_per_paragraph

- Design One ¶3 (p23, spec): split into p23 (the price: 50 rows, sharding, cross-cluster transfers) and p23b (the payment path does not wait; "In 2021, then, Adyen's book was a separate system…").

## evidence_is_explained

- Uber quotation: fixed; a sentence says what it shows ("Uber's record had been split across the systems that move money; its fix, like the two designs above, was one double-entry book of record of its own").

## transition_expresses_declared_relationship

- Into the mechanism section: fixed; opens "The two changes, balanced entries that are never edited and accounts for money in flight, are built from a few parts, defined here one at a time."

## known_before_new

- "webhook" in the Larkfield section: glossed in one clause and linked to [[payment-webhooks-and-events]] at first use.

## flow_is_followable (major)

- "the book's central gap": fixed ("the gap this whole book follows, between the instant answer and the slow truth").
- Nightly query vs nightly entries (fault unclear): fixed against the ledger's chapter 12 line. The scene says the 2025 books, "the first that the team called a ledger", were posted by a nightly job; the payment-table section says that before that ledger existed what each studio was owed was computed by a nightly query, and that the 2025 ledger, posted from the same rows, inherited the view. Spec p09 evidence aligned.
- Payment-table ¶2: the five states are listed, the point (one `refunded` status for a part refund) is made, the two wrong amounts are shown (nothing owed back, or the whole €117.47, against the true €84.00; arithmetic from the page's own figures and ledger line 44), and "the row it was computed from is gone" became "the row no longer holds the state it was computed from".
- €18,400 before it is introduced: the clearing-account paragraph now announces the figure's illustrative €18,400 before Figure 2.
- Sign rule: one sentence added ("on an account of what the book owes… a negative line raises the debt and a positive line pays it down"); the refund line now says "+84.00… which lowers what the studio is owed".
- Uber sentences between the table's announcement and the table: the announcement now follows the Uber sentences, directly before the table.
- Where They Differ (fault unclear; position is house format): house format; transition strengthened. The opening says the section compares the companies' published accounts and that the new material follows the table.
- Larkfield ¶2: the paragraph points to the table, maps each entry to its source (entry 1, entry 2, entries 3 and 4), and says "the two clearing accounts the payment touched".
- Refund paragraph mixing real and hypothetical: split (spec p39 and p39b). p39 is the actual refund, with the Adyen quotation and the old nightly sum; p39b opens "Now take a case that did not happen" and says which balance would be empty ("no sales since the payout to cover the refund").
- Hand-off "Everything in this chapter is the provider's view": fixed; "These questions are for whoever keeps a book. This chapter has looked at a ledger from the keeper's side, a provider's or Larkfield's…". Position under Questions to Ask is house format; transition strengthened.

## flow_is_followable (minor)

- "the query from the previous section": fixed (names the section and quotes the query).
- "the middle column" before the table: fixed ("prevention at the write, the middle column of the table below"); cell "the gate bounds the books" became "the gate's capacity limits the books".
- Payout entries shaped differently from the teaching model: one sentence says so ("what the studio is owed falls only in entry 4").
- Tom Hendriks joined to "I", and "the reconciliation job" named late: split into two sentences; the job is described where it is named ("runs when each provider's reports are ready and posts entries only from their lines"); the scene's rounding cell now says "nightly posting job".
- "One row is documented": fixed ("Two of the table's rows, a missing event and a wrong identifier").
- "internal ledger" in quotation marks: the 2026 post's phrase is now introduced as its own ("The 2026 post also speaks of an 'internal ledger'"; verification row 30).

## no_weak_conclusion_pattern

- Depends on context ¶2, pending amounts as a new idea: the sentence on approving spending and pending amounts is removed; the bullet now states the spec's p46 (staleness and buy-or-build turn on the number of writers and the volume) with the chapter's own figures.

## conclusion_synthesizes_and_answers_so_what / conclusion_calls_back_to_introduction

- Fixed in the author's synthesis: a bullet states the declared synthesis (one idea at three sizes; where the rule is enforced follows from the writers; keeping it is not optional), and the "copy the rules" bullet returns to the €412,000 (three movements with no entry, where each would have shown) and gives the so-what (a team with mutable statuses and computed sums will meet its own).

## AC-3 (blocker)

- Fixed: "Adyen's 50 rows per payment (2021) and Stripe's five billion events a day (2024)", dated from the page's Sources (Adyen post 2021-08-23; Stripe post 2024-02-16); Larkfield's 31.4 million payments dated 2026 from the ledger.

## Content corrections (change 4 of 17 November)

1. Nightly query and nightly posting job made to agree with the ledger's chapter 12 line (two periods, stated as such).
2. AC-3 years added (above).
3. One sentence removed as unsupported by the body: "A system that approves spending against a balance cannot, and needs pending amounts in the store itself."

## For the editor

- The FAILURE PATTERNS callout (Borrowed Blueprint) still reads "a log of five billion events a day" with no year; callouts may be touched only to gloss. Recommend "(Stripe, 2024)" after the figure, for AC-3.
