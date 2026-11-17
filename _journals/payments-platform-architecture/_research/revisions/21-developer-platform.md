# Revision log — 21-developer-platform (draft check round 1, ESCALATE)

Revised 2026-11-24. One line per failed result. No fact, number, date, quotation, hedge, source, figure, caption or `[[link]]` changed.

## Major

- one_controlling_idea_per_paragraph, What to Take Away ¶4 (p31; spec fault): agreed. Split in spec and prose at "So for each provider, write down five terms…": p31 keeps the part synthesis (edges, incidents, Keel decisions); new unit p34 holds the course of action and its so-what. No sentence lost.
- flow_is_followable, scene ¶2 (third question unanswered): fixed in draft and in p06's controlling idea. The answer is taken from the chapter itself (FAILURE PATTERNS callout: "a per-endpoint limit nobody had read"; Request Limits: a one-kind batch "meets the 25, not the 100") and the ledger (the wave met Stripe's rate limit): "Stripe's limit for one endpoint, written on a documentation page that nobody on the team had read", with a pointer to the limits section for the figure.
- flow_is_followable, Request Limits ¶3 ("Note the third row of the table"): fixed in draft. The sentence now announces the table and states the row's content in full (25 a second of one endpoint, not the 100 of the account), so it reads without the table.
- flow_is_followable, comparison table, request-logs row (spec fault): row kept (verified). Forward pointer added in the sentence before the table: the last row runs ahead, logs are a means of recovery explained in "When It Goes Wrong", and Workbench is glossed (the developer area of Stripe's Dashboard, per the chapter's own quotation). p19's controlling idea records it. House format; transition strengthened.
- flow_is_followable, When It Goes Wrong ¶1 ("the Phantom Payment in reverse"): agreed. "In reverse" removed in draft and in p25: the case is the pattern as the callout and the patterns page define it (a payment believed failed without the provider's confirmed record).
- flow_is_followable, What to Take Away ¶4 (change of scale; position): house format; transition strengthened. The unit now opens by saying the chapter closes Part IV and the last take-away is the part's; the split above shortens it; "key retention" is now "idempotency-key retention" and the five terms are given as "what can be read back by identifier, and then the four edges" (five after four explained). Spec takeaway wording aligned.

## Minor

- flow_is_followable, Request Limits ¶5 (first, second, third design before the table): fixed. The three designs are named in the opening sentence (react, pace, agree) and referred to by name.
- Judge's note, Credentials opening (weakest transition, passed): one short sentence added ("Take the review's first question, the key.").
- Judge's note, request-log paragraph ties thinly to the thesis (passed): not changed.

## Spec changes

- p31 split, new p34; p06, p19, p25 controlling ideas; conclusion takeaway wording; `max_words` 5000 -> 5250 (5%; the page was at exactly 5,000 and has no connective text of that size to trim); `revised` and changelog entry dated 2026-11-24.

## Checks

- `validate_spec.py payments-platform-architecture 21-developer-platform`: ok.
- `check_draft.py structure`: pass, 5,111 words (limit 5,250). `timetoread` stays 22 (5,111 / 230).
