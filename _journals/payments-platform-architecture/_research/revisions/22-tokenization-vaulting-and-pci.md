# Revision log — 22-tokenization-vaulting-and-pci (draft check round 1, ESCALATE)

Revised 2026-11-17. One line per failed result. No quotation, date, number, hedge, source entry, figure, caption or `[[link]]` changed, except the two content corrections listed under "Content corrections".

## Blocker

- AC-3, Where They Differ ¶1 ("both keep card numbers out of a merchant's systems by the same three moves"): agreed; draft fault. Rewritten so that each move is attributed only to the provider that documents it: both collect in a frame they serve and hand back a token; the isolated vault is documented by Stripe and "not public" for Adyen (the vault section, verification row 88, absence audit). p37 aligned.

## Major

- transition_expresses_declared_relationship, Four Ways ¶1: fixed. A bridging opening sentence carries over the frame, the token and the vault and says the designs follow from them (cause and effect): the choice of how a card reaches them is where "scope follows the path" becomes a questionnaire. p22 aligned.
- flow_is_followable, Four Ways position: same fix; the bridge gives the reason the section comes after the vault and returns to the scope thread.
- flow_is_followable, Introduction ¶1 ("Six months later"): corrected against the ledger (scene in January 2027; Jonas signs in February 2027): "five months later, in January 2027". The sentence now hangs on the second question ("The second question is not idle"). Spec hook aligned.
- flow_is_followable, Introduction ¶3 ("eight weeks earlier"): reordered: 12 January 2027 first ("the month of that unsigned line"), the 9 March wallet payment "eight weeks later" second. Dates unchanged and consistent (12 Jan + 56 days = 9 Mar). p03 aligned.
- flow_is_followable, five names for one form line: one name, "script line", defined at first reference in the scene; "script criterion", "eligibility line", "that confirmation" replaced. Spec controlling ideas aligned (p06, p23, p24, p29, p30, p46, p47).
- flow_is_followable, callback sentence: split in two; the second says how the page relates to the script line (a script on it could copy what is typed, as the page section explains). Spec callback aligned.
- flow_is_followable, "Every Stripe and Adyen cell is a fact cited earlier": agreed; two cells corrected (below) and the sentence now reads "…or says what is not public or could not be read", which is true of every cell.
- known_before_new, "network token": gloss added at first mention (Stripe's guide to network tokens: "the substitute card numbers that a card network issues in place of the real one", from the glossary).
- known_before_new, "Card-Testing Weekend": the opening now names the event.

## Minor

- flow, Radar "only available" vs "performs best": one connecting clause ("is milder…; on either reading"); both statements and the hedge kept.
- flow, 30 January 2025 told after 31 March 2025: reordered: the requirements are "future-dated to take effect on 31 March 2025", and the removal follows as "Two months before that date, on 30 January 2025".
- flow, Card in the Log callout vs failure section: the compromised-script failure now says it is the other road to The Card in the Log (the attacker's server as the system never meant to see the number). Callout untouched. p44 aligned.
- Judge's note, four-designs table not referred to (passed): not changed.

## Content corrections

- Stripe "Reusable token" cell: "returned in the API response" removed. The verification file (claim 25) dropped that phrase as not stated on the cited page; the table had kept it. Also removed from p14.
- Adyen "Export of stored cards" cell: reworded to ruling 31(a) and to the exit section's text ("An export article is listed in the help center, but its address redirects and its procedure could not be read").

## For the editor

- Introduction ¶2 (thesis sentence, locked) says "Payment providers … confine the real numbers to a vault kept apart from their own other systems" as a general statement of the pattern. It is not attributed to Adyen and the vault section and its INFERENCE block qualify it, so I left it; if AC-3 is read strictly, consider "and, at Stripe as documented, confine…" in the journal-spec thesis.
- Restoration: the page was read top to bottom; nothing garbled was found.

## Spec changes

- Hook content; controlling ideas of p03, p06, p14, p22, p23, p24, p29, p30, p37, p44, p46, p47; two transition `carries_over`; callback `how`; `max_words` 6500 -> 6825 (5%); `revised` and changelog dated 2026-11-17. No unit added, moved or removed.

## Checks

- `validate_spec.py payments-platform-architecture 22-tokenization-vaulting-and-pci`: ok.
- `check_draft.py structure`: pass, 6,669 words (limit 6,825). `timetoread` 28 -> 29.
