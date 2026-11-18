# Revision after draft check, round 1 — 11-in-person-payments

Date: 2026-11-17. Report judged: round 1, 21 failed results (16 major, 5 minor). One line per failed result. Words 6,147 before, 6,496 after (`max_words` 6,500, unchanged). `timetoread` 26 to 28. Apart from the corrections listed under "Content corrections", no fact, number, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- In practice ¶2 (p35, spec): split. p35 keeps why offline acceptance was refused; new p35b holds the €3,000 sizing as a credit limit, opening "Turning the request down did not make its risk go away".
- What to Take Away ¶5 (p46, spec): split into p46 (K8 as the consequence of the six-layer table), p46b (callback and synthesis: the 1,140 studios and the opening queue) and p46c (what to write down).

## evidence_is_explained

- The 97% EMVCo statistic: fixed ("Chip is therefore the normal case at the counter, and what an architect has to look for are the exceptions").

## transition_expresses_declared_relationship

- Into "A Terminal Is a Managed Computer": fixed; opens "Because the liability rule turns on what the terminal reads and passes on, the machine doing the reading has to be trusted…".
- Into "When It Goes Wrong": fixed; opens "Larkfield's decisions describe the counter when everything works; four failures test them."

## known_before_new

- Store-and-forward used before it is explained: fixed with a one-clause gloss at first use, pointing to the offline section.
- SAQ B-IP / SAQ C, "Terminal-only", "scope": "Terminal-only merchants" is now "merchants who take cards only through Stripe Terminal, its in-person product"; scope is glossed from the glossary; the page says neither provider compares the two questionnaires and the chapter does not rank them (no source distinguishes them; no fact added).

## flow_is_followable (major)

- "It works through disputes": fixed ("The EMV liability shift works through disputes"); the Visa rule sentence is split into the three base conditions and three numbered alternatives, quotations unchanged.
- Requirements table "As available as the till, no more": cell reworded ("Up whenever the till is up; more buys nothing"); the four-shapes paragraph now takes up the availability row.
- "the opposite end": fixed ("starts from its own online API rather than from a retail protocol"); SDK named as the in-store path and server-driven as the cloud path.
- Adyen wallet claim with nothing before it: fixed by restoring the verified `PaymentAccountReference` quotation (verification row 75; Sources "Card acquisition"); closing sentence now says that at both a wallet card is recognized by a different value.
- "In-person refunds are only available on Interac": fixed; the source's scope is quoted exactly (online refunds "on all card networks except for Interac"; in-person refunds with the card at the reader "only available on Interac"), fetched from the Stripe page.
- Table years differ from earlier citations: fixed under ruling 30 (see corrections).
- "what was being declined": fixed ("what she had refused").
- Mila's refund, where she asked: the ledger records the date, not the channel; the page now says so and states the counter case as a condition.
- What to Take Away ¶5: fixed by the split above; "That is why" now follows "Because an approval rate describes a whole stack".
- Hand-off under "Questions to Ask" (spec, position only): house format; transition strengthened ("Every one of these questions stops at the approval, and so does Part II."); p48 transition updated.

## flow_is_followable (minor)

- "The rule flips": fixed ("Even across many small sites, the in-store path wins when…").
- "The chapter's second question": fixed ("raised by the member's refund at the front desk").
- "the part an engineer would most like to read": named at once ("how keys are handled and how often terminals fail").
- Floor limit vs store-and-forward maximum: fixed from Adyen's setup table (fetched): floor limits for offline EMV (chip and contactless), the store-and-forward maximum and count for store-and-forward.
- Opening queue read as a Larkfield studio: fixed; the hook places it at "a gym whose terminals accept payments offline", and the close returns to "the gym's queue".

## Content corrections (change 4 of 17 November)

1. Adyen documentation dates taken from page metadata (2023, 2025, May 2026, 2026) replaced by "n.d., accessed November 2026" in five places in the text and six table cells (ruling 30; verification rows 20, 24, 35, 49, 73, 80, 101 show these were `last_modified` stamps). The note before the table now says both companies' documentation is undated.
2. Adyen wallet claim: supported (verification row 75); the quotation is restored, not removed.
3. Interac sentence: scope quoted exactly from the Stripe refunds page.
4. Mila's refund channel: ledger silent; stated as a condition, no fact invented.
