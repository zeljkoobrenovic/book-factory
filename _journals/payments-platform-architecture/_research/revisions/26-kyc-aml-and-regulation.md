# Revision after draft check, round 1 — 26-kyc-aml-and-regulation

Date: 2026-11-17. Report judged: round 1, 15 failed results (12 major, 3 minor) and 1 waived. One line per failed result. Words: 6,482 before, 6,682 after (the spec declares no `max_words`; under the book's 6,900 cap). `timetoread` 27 to 29. Apart from the change listed under "Content", no fact, number, date, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## transition_expresses_declared_relationship

- Designs ¶1 "respond to all this" (major): fixed. The section opens from the declared known information: "Requirements that change for reasons neither the seller nor the platform controls, on a calendar set by regulators and providers, leave a platform … three ways to respond".

## flow_is_followable (major)

- Regulatory Calendar placement (spec): not moved (topical section; whole sections never move). Transitions strengthened on both sides: the calendar now opens from the rule-change route ("the one a platform can see coming, if it reads the calendar the rules come from"), and the designs section opens from the calendar. Spec `calendar.transition_in` and flow rationale updated. Recommendation for the editor: keep the order; the calendar is what the designs must absorb. If a move is ever wanted, the calendar would sit after the designs, before Where They Differ.
- DORA paragraph declares itself off-topic (spec): kept and made to serve the section's point in one sentence: DORA "shows that not every rule on the calendar reaches verification state: a platform tracks its date and status, and its verification record does not change". Not removed because the table row, the Established take-away and the [[payment-reliability-and-availability]] link depend on it. Spec p26 controlling idea aligned.
- Intro ¶3, second storyline: fixed; Studio Noord's payout switch is tied to "the same kind of switch that was off for the 230 studios in May 2026". Spec p03 aligned.
- Larkfield on both providers learned late: fixed; the scene's first paragraph says "Larkfield's studios are split between two providers, Stripe and Adyen." Spec p05 aligned.
- Evidence-age note and FinCEN order interrupt ¶2: fixed; the US dates, the evidence-age mark and the 2026 order moved to the end of the paragraph, after the threshold and the Adyen field.
- Custom-accounts deadline in the table but cited nowhere above: fixed. The fact is now cited in the state-model section (p16), with its support-article source, so the table's "repeats a fact cited above" is true. Spec p16 evidence added.
- "the five controls" unnamed: fixed; named in the sentence (the vault and its tokens, network tokens, fraud scoring, authentication, verification of the business), and the Card-Testing Weekend is placed as "the card-testing attack of August 2026 with which the part's introduction opened" (ledger: 8–9 August 2026). Spec p45 aligned.

## flow_is_followable (minor)

- When "now" is: fixed; "reviewed the May 2026 incident … in her first months in the role; this chapter follows that review."
- "legislates this chapter's claim": fixed; the claim is named in the sentence.
- Article 20(1)(d) after FinCEN and OFAC: fixed; "of the EU AML Regulation" added.

## flow_is_followable (waived)

- Where They Differ position: house format, waived by the author; no change needed beyond the Custom-accounts fix above.

## known_before_new

- K6 in the roadmap: fixed; glossed "(verification is state, not a form)".
- "Keel": fixed; "decision K6 of Keel, Larkfield's 2027 payments program". Spec p30 aligned.
- "Custom accounts": fixed; glossed at first use (p16) from ruling 23: Stripe's connected accounts with no Stripe dashboard of their own, for which the platform collects requirements, as Larkfield's studios on Stripe are.
- "payment record store": fixed; glossed as Larkfield's own record of every payment attempt.

## Content

- One sentence added in p16 states, in prose, the Custom-accounts deadline fact that was previously only in the comparison table (same source, same wording).

## Not changed

- No failure judged wrong.
