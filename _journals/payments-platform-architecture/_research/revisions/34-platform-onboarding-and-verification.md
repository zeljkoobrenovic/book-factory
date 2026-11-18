# Revision after draft check, round 1 — 34-platform-onboarding-and-verification

Date: 2026-11-17. Report judged: round 1, 22 failed results (11 major, 11 minor), none waived. One line per failed result. Words: 6,300 before, 6,592 after; `max_words` raised 5% from 6,300 to 6,615. `timetoread` 27 to 29. Apart from the corrections listed under "Content", no fact, number, date, quotation, hedge, figure, caption, callout, source entry or `[[link]]` was changed.

## one_controlling_idea_per_paragraph

- When It Goes Wrong ¶3, Adyen's no-webhook sentence (spec, major): fixed by moving the sentence (rule 7) from p37 to p22, where the record and its re-read are set out ("The re-read matters on Adyen in particular: …"). Spec evidence moved from p37 to p22 with a note.

## transition_expresses_declared_relationship

- Two Ways to Lose a Seller ¶1 (major): fixed. The section now opens from the review's two halves and maps them onto the two losses (collection decides whether a seller finishes and whether a later requirement can be met; after sign-up decides whether a reopened requirement stops the money), then "Both rest on two terms." Spec p07 aligned.

## flow_is_followable (major)

- Intro ¶3, Studio Noord unexplained (unclear): fixed with a bridge: "Ironworks is on Stripe. The payment this book follows, Mila Janssen's class pass, was made at Studio Noord, on Adyen, and the same condition held there." Spec p03 aligned.
- API option read as open to all, rule arrives later (unclear): fixed with a forward pointer in p16 ("and on Stripe not open to every platform, as the next paragraph shows"). Order kept. Spec p16 aligned.
- Periodic review ends on an error code and endpoint: fixed; the error code and endpoint come first ("Behind the screen…"), and the paragraph closes from the seller's side (an open item with a date, cleared by confirming the data). Spec p24 aligned.
- Where They Differ lead-in promise broken: fixed both ways. Stripe's one deadline per account and its typical 14 and 28 days for Custom accounts are now stated in the body (p21, from the support article already in Sources; ruling 48g), and the lead-in says that the platform's own switch is cited there first, then makes the "every cell is cited" claim. Spec p21, p28 aligned.
- "Payouts need no capability of their own on this account type" vs the definition (major): fixed. The definition's example is now "receiving transfers from the platform" (Stripe's own definition says "receiving transferred funds"); the payouts sentence is kept and names the account type: Ironworks is a legacy Custom account on Accounts v1, where payouts are not a capability but follow the account's payout settings; Accounts v2 requests a payouts capability automatically (verification row 76, ruling 40c). The hand-off now says "capabilities to take payments and receive transfers are active, and its payouts can run". Spec p07, p31, p42 and hand-off aligned.
- Replay tense (major): fixed; the replay is in the conditional ("would have shown", "would have seen"), and what is in place now is a separate sentence ("That part is now in place: Jonas owns every open deadline…"). Ledger: the K6 design is 2027. Spec p33 aligned.
- "1,140 older Dutch and German studios" (major): fixed; the split is stated before the numbers: Stripe carries every British, American and Belgian studio and the Dutch and German studios onboarded before 2024. The earlier sentence now says "Studios on Adyen, the Dutch and German studios onboarded since 2024". Spec p32, p33 aligned.
- 50 largest studios out of place: fixed; tied to the measurement ("so each can appear once per provider in the count of open requirements"). Spec p34 aligned.
- Adyen no-webhook gap filed under failures (spec): fixed (moved; see above).

## flow_is_followable (minor)

- Two halves vs two losses: fixed (see transition).
- "Studios on Stripe" implies others: fixed; the scene says Larkfield splits studios by studio and Ironworks, like every British studio, is on Stripe.
- Jump from May 2026 to a 2027 review: fixed; "When Femke de Graaf joined Larkfield in January 2027 … she reviewed the incident … and began where Ravi had: on his screen."
- Tier "amounts": fixed; "the amounts at which a seller moves from one to the next".
- "Collection happens once": fixed; "Sign-up ends, even when collection came in stages".
- "Stripe's sentence continues": fixed; "Stripe's sentence on payouts, quoted in the section on losing a seller, continues".
- "the mirror" never used again: fixed; the name is dropped, the link kept.
- Redirect rule in p26 and p35 (spec): fixed by a back-reference in p35 ("the one the measuring section warned of"); both units kept, since p26 states the measurement rule and p35 the failure. Spec p35 aligned.
- "And only a comparison": fixed; "One question stays open whatever these numbers show".
- "did not oblige Larkfield to maintain the fields": fixed; "never obliged Larkfield to build its own forms".
- "both counts": fixed; named (an own form with no field for the new requirement, and a seller's screen with nothing on it).

## Content

- Capability example changed from "receiving payouts" to "receiving transfers from the platform" (Stripe's definition, verification row 5; ruling 40c).
- Payouts sentence: account type and API version named, and how payouts are enabled on it (ruling 40c; verification row 76).
- Hand-off: "capabilities to receive payments and payouts" replaced by "capabilities to take payments and receive transfers are active, and its payouts can run".
- Stripe's per-account deadline and typical 14/28 days stated in the body (source already listed; ruling 48g).
- Providers named for Ironworks (Stripe), Studio Noord (Adyen) and the studio groups, as in the ledger.

## For the editor

- The journal spec's `transition_in` of chapter 35 (journal-spec.json, `carries_over`) still reads "capabilities to receive payments and payouts are active". Recommendation: change it to "capabilities to take payments and receive transfers are active, and whose payouts can run", to match this chapter's hand-off. Not changed here (journal spec).

## Not changed

- No failure judged wrong.
