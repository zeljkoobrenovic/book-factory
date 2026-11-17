# Revision log — part-4-intro (draft check round 1, ESCALATE)

Revised 2026-11-24. One line per failed result. No fact, number, date, quotation, hedge, figure, caption or `[[link]]` changed; every added clause repeats the ledger or the owning chapter.

## Major

- evidence_is_explained, Chapters ¶1 ("get payment"): fixed in draft; the sentence now says the call reads only Larkfield's own table, so one name covered both the provider's record and Larkfield's memory of it (spec p05's evidence).
- flow_is_followable, Introduction ¶3 (contracts do not pair with cases): spec and draft repaired. p03 now pairs each case with its contract as the chapters do: lost response, a key; changed shape, a pinned version; later outcome, events; all three resting on a readable identity and state; the refused request is answered by a stated limit, the rate up to which requests are accepted (consistent with the part thesis and Figure 1). KEY POINTS bullet 1 pairs the same way.
- flow_is_followable, callout / ¶2 / closing (three orders): fixed in draft and spec. One order everywhere, the chapters' order (lost, changed, later/missing event, refused): KEY POINTS bullets 1 and 2, p01 (incidents now told Double Charge, Version Cliff, Silent Webhook, Renewal Wave), p02, p03, p10. Decision recorded in the spec.
- flow_is_followable, Sources line ("makes no factual claim of its own"): fixed: "Every fact on this page is repeated from the chapter that states and cites it."
- known_before_new, incident names: fixed in draft; p01 names each incident where it tells it ("In the Double Charge of 1 November, …"), so the chapter paragraphs use known names.
- known_before_new, "idempotency key" before its gloss (spec fault): repaired; glossed at first use in p01 ("an identifier that lets the provider recognize a repeat", glossary) and in KEY POINTS ("which makes a request safe to repeat"); spec hook and p01 updated.

## Minor

- flow_is_followable, Introduction ¶4 (four contracts vs five chapters; "the keys"): fixed: "take the contracts and their limits"; "the credentials, test environments and request limits around all of it".
- flow_is_followable, Chapters ¶3 ("three years of changes" new): fixed; p01 now says the upgrade moved the integration "from a version more than three years old" (ledger), and p07 says "those three years of changes".

## Content corrections

- None.

## Spec changes

- hook, p01 (controlling idea and evidence), p02, p03, p04 controlling ideas; decision log and changelog entries dated 2026-11-24; `revised` 2026-11-24; `max_words` raised 5% (1,200 to 1,260).

## Checks

- `validate_spec.py payments-platform-architecture part-4-intro`: ok.
- `check_draft.py structure`: pass, 1,260 words (limit 1,260). `timetoread` stays 5. Build not run (brief, change 6).
