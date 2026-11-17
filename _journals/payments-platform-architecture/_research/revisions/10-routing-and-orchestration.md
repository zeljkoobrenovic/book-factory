# Revision after draft check, round 2 — 10-routing-and-orchestration

Date: 2026-11-24. Report judged: round 2 (after one revision by the checker), 16 failed results: 9 major, 7 minor. One line per failed result. Words: 5,887 before, 6,165 after (`max_words` 6,500, unchanged). `timetoread` 24 to 27. Apart from the editor-authorized corrections listed below, no fact, number, date, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## transition_expresses_declared_relationship

- In Practice at Larkfield: fixed. The section opens "Applied to Larkfield, the staged rule and the two companies' positions lead to decision K8 of Keel".
- Questions to Ask: fixed. A sentence before the list derives the questions from the positions.

## flow_is_followable (major)

- Canva talk used before it is presented: fixed. The talk, its three speakers and what Canva built are introduced at first use, in the section on two kinds of routing; later mentions point back to "the Sessions talk".
- In practice ¶1, answers that cannot be matched to the three questions: fixed. The section gives two reasons for K8 (structural, before the questions; statistical, the third question); the rehearsal paragraph names the first and second questions.
- In practice ¶2, €1,120 million, €910 million and 27.6 million unannounced: fixed (editor-authorized). The paragraph derives €1,120 million from the scene's €493 million and €627 million, says €910 million in 27.6 million payments is the online part, and says both are Larkfield's 2026 totals from the book's introduction of the company, fictional like it.
- In practice ¶3, Studio Noord (spec): fixed (editor-authorized), in spec and prose. See the ledger note below.
- Where They Differ, external-acquirer fact only in a cell: fixed. The lead paragraph now says two rows need a new fact and states it before the Multi pay-in fact; spec p36 evidence records it.

## flow_is_followable (minor)

- Position of "Stripe and Adyen: Where They Differ" (spec): house format; transition strengthened (last sentence of the staged-rule paragraph and the section's first two sentences).
- Introduction, "ended there too": fixed ("ended on the same proposal, because every lever it described sits inside one provider").
- Double Charge "without the remedy": fixed. The sentence says what the incident was (a timed-out renewal retried under a new key, from the ledger) and which remedy is missing.
- "all three": fixed ("all three answers").
- "The second way out": fixed ("Forwarding is one way out of a single provider's vault. A second moves…").
- "stage" before stages are defined: fixed. The opening of the section was recast.
- Bold evidence-age parenthesis on Regulation II: no action; the style guide requires the mark.

## known_before_new

- KEY POINTS callout, "network tokens" and "cryptogram": not fixed; callouts may not be touched. For the editor.
- Failure-patterns callout, "idempotency key": not fixed; same reason. For the editor.

## What the ledger says about Studio Noord

The ledger gives Ines Bakker's Studio Noord as "On Adyen since 2024; three instructors, 410 members", and says "Studio Noord is on Adyen". Chapter 10's own line says each of the 50 largest studios keeps a verified account at both providers and that the switch moves payments that bring their own credential ("Mila's pass would move"). No line, and no `[editor]` line, says Studio Noord is one of the 50 or has a Stripe account. The ledger is silent, so the example states the condition: the switch works only for the 50; unless Studio Noord is one of them, Mila's pass cannot move; for a studio with both accounts a pass like hers moves and a membership like hers does not. The words "without trouble" are gone. Spec p41 was changed to match.

## For the editor

1. KEY POINTS, third bullet: "On network tokens, Adyen's terms (2025) describe a service that shares them for use with other providers, with the cryptogram still from Adyen". Recommend one clause each for network token and cryptogram, taken from the stored-cards section.
2. Failure patterns, The Double Charge: "across two providers that share no idempotency key". Recommend the clause from When It Goes Wrong ("the key by which a retry is recognized as a repeat").
3. Studio Noord: if the author wants the unconditional example back, add an `[editor]` ledger line saying whether Studio Noord is one of the 50; with 410 members it probably is not.
