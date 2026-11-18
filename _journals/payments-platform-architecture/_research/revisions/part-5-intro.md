# Revision log — part-5-intro (draft check round 1, ESCALATE)

Revised 2026-11-17. One line per failed result. No fact, number, date, quotation, hedge, figure, caption or `[[link]]` changed; every added clause repeats the owning chapter or the Part V thesis.

## Major

- conclusion_synthesizes_and_answers_so_what, Where to Begin ¶1: fixed in draft; the declared so-what is now a sentence of the conclusion ("Whichever you read, ask what stayed with the business and who owns it before you count the risk as handled"). p12's controlling idea carries it.
- flow_is_followable, Introduction ¶1 ("€1 drop-in payments"): fixed in draft: "€1 payments for a trial drop-in class" (ledger, additions for chapter 24: the widget sold €1 trial drop-ins).
- flow_is_followable, Introduction ¶3 (3-D Secure sentence drops the remainder; the "Loss" tile): fixed in draft and spec. The sentence now ends "and leaves it with you on every payment that is merchant-initiated or exempted at the request of your side" (the Part V thesis as reworded by the author). One sentence before Figure 2 says which tile is which (Threshold: the loss on what you accept; Loss: the loss on payments not authenticated). Spec: p03's controlling idea gains the remainder; the Figure 2 evidence item says "loss" where it said "exemptions". Figure and caption untouched.
- flow_is_followable, Introduction ¶4 ("The rules are also linked"): fixed in draft and in p04: the controls are linked, "so a choice about one is a choice about another", which is the step the readers missed before "So I would stop asking".
- flow_is_followable, Chapters ¶4 ("the risk rule's third action"): fixed in draft. The fraud paragraph now says a merchant's own risk rule can allow, block or, between the two, request 3-D Secure (chapter 24's wording); the next paragraph picks up "that third action, the request for 3-D Secure". p09's controlling idea records the clause.
- flow_is_followable, Sources line ("makes no factual claim of its own"): fixed: "every fact on this page is repeated from the chapter that states and cites it". The non-goal in the spec says the same.
- known_before_new, Introduction ¶3 (network token, provider token): fixed in draft and p03: one-clause glosses from the glossary (a substitute card number the card network issues; a reference only your provider can turn back into a card). The later repetition of the network-token gloss in the chapter list was shortened.
- known_before_new, "PCI": fixed in draft: "The card industry's security standard, PCI DSS (the Payment Card Industry Data Security Standard)" at first use; "most of PCI DSS's scope" in the chapter list, so "PCI guide" and "PCI form" connect.

## Minor

- flow_is_followable, Introduction ¶1 (weekend not tied to the claim): fixed with one clause ("because a frame served by its provider collected them"), from the spec's own evidence item and chapter 22. p01 aligned.
- Judge's note on the 41%/86% figures (passed, "thin but sufficient"): not changed.

## Spec changes

- Controlling ideas of p01, p03, p04, p09, p12; Figure 2 evidence wording; non-goal 4; `revised` and changelog entry dated 2026-11-17. No unit added, moved or removed. `max_words` unchanged (1,200).

## Checks

- `validate_spec.py payments-platform-architecture part-5-intro`: ok.
- `check_draft.py structure`: pass, 1,190 words (limit 1,200). `timetoread` stays 5 (1,190 / 230).
