# Revision after draft check, round 1 — 25-3ds-and-sca

Date: 2026-11-24. Report judged: round 1, 23 failed results (18 major, 5 minor). One line per failed result. Words: 6,498 before, 6,822 after (`max_words` raised 6,500 to 6,825, 5%). `timetoread` 28 to 30. Apart from the corrections listed, no fact, number, date, quotation, hedge, figure image, caption text, callout, source entry or `[[link]]` was changed.

## evidence_is_explained

- Break-even "3% × €120 ÷ €135" (major): fixed. A sentence before it says what each policy is expected to cost (3% of €120 in lost sales against the fraud probability times €135), so the formula is the point where the two are equal.

## transition_expresses_declared_relationship

- "A membership is built from those two rules" (major): fixed. The rules are named: an authenticated set-up, then merchant-initiated payments outside the rule and without a shift. Spec `recurring.transition_in.carries_over` says the same.

## flow_is_followable (major)

- Hook's two €120 passes vs the scene's €49 set-up (spec): fixed in spec and prose. Hook, p01 evidence, p03 and the closing callback now follow the ledger: Mila's challenged €49 membership set-up (12 January 2027) and Bram de Wit's unchallenged €120 pass (2 February 2027, Studio Noord, exemption granted, studio's loss €135 if lost). Spec `introduction.hook.content` and `conclusion.callback.to` corrected.
- Journey note brings in a third payment (spec): mitigated in prose, unit kept (the journey note is a book-wide convention). It now says the followed payment is "a third one" and that Mila is the challenged member of the opening. Spec p03 wording aligned.
- "on every payment a merchant allowed it kept the loss": fixed ("the merchant kept the loss on every payment the rules allowed").
- "The condition is the set-up.": fixed; the condition is stated in the sentence it belongs to.
- Hedge on the three shares: fixed; the hedge is kept and the sum shown (29 + 22 + 26 = 77%).
- "by network and region" unexplained: fixed. The table's lead quotes Adyen ("In some regions, card schemes may grant liability shift after a successful frictionless flow"), confirmed in the verification file (item 41, A-reg). Spec p17 evidence records it.
- Figure 2 in the liability section (spec): fixed in spec and prose. The ask-or-skip figure moved to the decision section after p23 (spec evidence moved from p17 to p23). Figures renumbered by position: the membership timeline is now Figure 2, ask-or-skip Figure 3; caption texts unchanged.
- "only the third follows it" before the table: fixed; the three policies are named before the table and the sentence says the table compares them.
- Delegation classification set up nowhere: fixed. "Delegated authentication" is glossed at first use (providers section) and the passkey paragraph states the classification as a definition plus the author's reading.
- "Assume that…" (spec): fixed in spec and prose. The exemption request and grant are stated as ledger fact; only the `scaExemptionRequested` field is marked "(the field is an illustration)", as the ledger does. Spec p37 evidence reworded.
- What Is Moving position and overlap with chapter 50 (spec): not moved (topical section). Not trimmed to a pointer: the spec does not allow it (intent.know and AC-3, a blocker, require the PSD3 status and the attributed Adyen reading in this chapter; chapter 50 covers PSD3 beyond authentication, per the non-goals). Transition strengthened: the section opens by saying why it comes before Larkfield's policy (Larkfield has UK and US studios; the European rules are being rewritten); In Practice picks up "the limits on them". Recommendation for the editor: leave as is; if trimmed later, cut chapter 50's repeat of the authentication points, not this chapter's.
- Where They Differ repeats the previous section (spec): house format; transition strengthened. The opening says what the side-by-side view is for and that the columns repeat cited facts so each row reads on its own. Merging would remove a required house section.

## flow_is_followable (minor)

- Issuer-applied exemption paragraph hard to place: fixed ("One case is not in the table, because it turns on who asked"; the two readings separated with a colon).
- Break-even formula (flow reader 1): fixed with the evidence fix above.
- Adyen advice about the issuer-applied exemption vs frictionless: fixed; a sentence says the same lever serves the neighboring outcome, which by Adyen's account also shifts the loss.
- Evidence-age marker inside the definition: fixed; moved to the end of the paragraph in the style guide's form.

## known_before_new

- "Authenticate" (major): fixed; glossed as Adyen's authentication product at first use.
- "Sessions flow" (major): fixed; glossed as Adyen's recommended integration built on `/sessions`, distinguished from Stripe's conference.
- "payment record store" and `waiting_on` (major): fixed; one-clause glosses from the glossary and chapter 8.
- Scheme passkeys and delegated authentication before definition (minor): fixed; both glossed at first use in the providers section.

## Not changed

- No failure judged wrong. No content inconsistency found requiring a correction beyond the hook (ledger).
