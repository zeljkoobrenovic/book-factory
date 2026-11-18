# Revision after draft check, round 1 — 28-usage-metering-and-rating

Date: 2026-11-17. Report judged: round 1, 31 failed results (17 major, 14 minor) and 1 waived. One line per failed result. Words (check_draft structure): 5,992 before, 6,339 after (spec `max_words` 6,500, unchanged). `timetoread` 26 to 28. Apart from the corrections listed under "Content", no fact, number, date, quotation, hedge, figure, caption, source entry or `[[link]]` was changed.

## evidence_is_explained

- Contract table: fixed; the lead-in now states the result (ingestion at documented rates and bad events reported afterwards; no promise that a summary is current or an accepted event billed), and the configuration row from the spec evidence is restored (meter unchangeable except its display name, fact already cited in the section on meters).
- "Versioned pricing objects": fixed; completed: in the query design the price in force is one more input to a query run again over the stored events, set against Stripe's invoice not being recomputed.

## transition_expresses_declared_relationship

- Intro p03 contrast: fixed; opens "An amount that has to be counted, like Studio Noord's, is of a different kind from the payment this book follows."
- Scene opening: fixed; "Larkfield shows the claim at a volume where speed cannot be the problem."
- Scene p06: fixed; p05 now names the queue consumer feeding the meter, and p06 opens "What that meter and its queue produced for one studio came out when Ines Bakker … questioned her March invoice". "That same month" removed.
- Why Counting Is Hard opening: fixed; "Femke's question needs a vocabulary first, starting with the unit."
- p24 "Consequently": fixed; "If one design derives the invoice from a durable window and the other from the stored events, the choice comes down to …".

## flow_is_followable (major)

- Mila paragraph between thesis and roadmap: fixed by moving it before the thesis (spec and prose; order p01, p03, p02, p04), transitions fixed on both sides (p02 now opens "A rule has to choose between the three counts"); Mila introduced as a member at Studio Noord with her pass's date. Spec decision-log note on the style-guide order is overtaken by the editor's instruction.
- "That same month": fixed as above. Ledger: the policy is of May 2027 (chapter 28 line); the page already said May; the spec's decision log said "April 2027 policy" and now says May. The date Ines questioned her invoice is not in the ledger and is no longer implied.
- "For instance" at a section head: fixed; the section opens "Stripe's Billing meters give each of the three rules a documented value …, starting with the acceptance window."
- "Consequently": fixed as above.
- "Versioned pricing objects" dangling: fixed as above.
- Orb and Metronome used before being introduced: fixed; Orb glossed in the thesis paragraph and again at its first body use ("the usage-billing company Adyen bought in 2026 and still runs as a separate product"); Metronome named in the roadmap and glossed at first body use (unchanged).

## flow_is_followable (minor)

- 100,000 figure: fixed; the body now states it as the post's capacity, and the FAILURE PATTERNS callout attributes it to Stripe's 2025 post.
- First four fields vs identifier: fixed; the four fields are named and the identifier called the fifth.
- "a billion events" per what: fixed; "billions of events a month". (Heading kept; it is the spec heading.)
- Payment token vs AI token: fixed; "a stored card, kept as a payment token" and AI tokens glossed as "the units of text a model reads and writes (a different sense from a payment token)".
- "Orb's commitments are in early access" out of place: fixed; tied to the paragraph's preview caution ("The same caution covers Orb's commitments, described in the rating section").
- Time-rules cell vs prose: fixed; "by default one hour after the period ends and its invoice is created, at most 72".
- "In short": fixed (house format; transition strengthened): "Set side by side, the documented facts about meters, designs, credits and acquisitions separate the two providers on six aspects."
- Identifier limit as a fourth item: fixed; "Beside the three rules sits a limit on the identifier itself, not a fourth rule".
- Forced connectives: removed "Likewise", "Furthermore", "As a result", "Similarly", "Moreover", "To illustrate", "For example", "Therefore" and one "By contrast"; the remaining connectives express a declared relationship.
- "through sales": fixed; "by arrangement with Stripe's sales team" (Stripe page: "Contact sales" for up to 200,000 events per second; fetched 2026-11-17).
- Price change as an aggregation limit: fixed; "The invoice is not recomputed at finalization, so the late usage has nowhere to go", contrasted with the query design.
- Studio Noord's Adyen/Stripe aside: fixed; the sentence now says why it matters (the meter is Stripe's whichever provider members pay through).
- "Billed twice, one level above the payment" in the callout: fixed; gloss added "in the usage count, before any charge is made".

## flow_is_followable (waived)

- Merge acquisitions and Where They Differ: waived (house format); lead-in strengthened as above.

## known_before_new

- Mila: fixed (above).
- Orb: fixed (above).
- Connected account: fixed; "(a business on Stripe Connect, Stripe's product for platforms)".
- Account grace period: fixed; "its account-wide window for reporting events late, 12 hours by default" (verification #42: the 12-hour grace period is configurable account-wide).
- "Finalized" and "grace period" in KEY POINTS: fixed; glosses of a few words from the body ("fixed, so it no longer changes"; "a delay once the period ends").

## intro_predicts_content

- Roadmap: fixed; it names Metronome by Stripe and Orb by Adyen as usage-billing companies, says "billing for AI model tokens", and "a comparison of Stripe and Adyen".

## Content

- Spec decision log: "the April 2027 policy" corrected to May 2027 (ledger).

## Not changed

- No failure judged wrong. Nothing left for the editor.
