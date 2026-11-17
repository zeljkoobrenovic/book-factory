# Reviewer Brief — verification and editorial pass

You are the verifying editor for pages of **SETTLED: Architecting Payments and Revenue Infrastructure** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/book-factory/_journals/payments-platform-architecture/`; run scripts from the repository root `/Users/zeljkoobrenovic/PycharmProjects/book-factory`). You did **not** write these pages. The author's instruction for this pass: **re-check each claim against its source, confirm all links resolve, and separate what companies have documented from what is inferred.** A wrong, unsourced or outdated sentence about Stripe or Adyen is the worst defect a page can have. Use surgical edits; do not change a page's argument.

## Read first

1. `ROOT/_research/style-guide.md` — evidence discipline, page format, the "Where They Differ" rules, valid permalinks.
2. `ROOT/_research/consistency-issues.md` — **every numbered ruling**. Apply each one that touches your pages.
3. `ROOT/_research/scenario-ledger.md` — the canonical Larkfield facts, including every "Additions by chapter" line.
4. For each assigned page: `index.md` in full and its `spec.json` (for the units and evidence it was written from).

## A. Verify every factual claim (the main job)

For each assigned page:

1. **List the claims.** Go through the article top to bottom and list every sentence or table cell that states a fact about a real company, network, standard, regulation, date, number or quotation. Larkfield facts are not on this list (they go to step C). Labeled inferences and the author's judgements are listed only for the facts they rest on.
2. **Fetch the source of each claim** in this session and read the passage. Use WebFetch, or `curl -sL --max-time 40 -A "Mozilla/5.0 (research-bot)" <url>`; `docs.stripe.com` and `docs.adyen.com` pages usually have a `.md` variant; EUR-Lex texts are served by `http://publications.europa.eu/resource/celex/<CELEX>` with header `Accept: text/html` or `application/xhtml+xml`; SEC EDGAR needs the User-Agent `research-bot admin@example.com`; Medium via its RSS feed. Never put the user's name, email or any personal identifier in a request.
3. **Classify each claim** and act:
   - **confirmed** — the source says it; a quotation matches character for character (typographic quotes aside). No edit.
   - **corrected** — the source says something different (a number, a date, a name, a status such as preview versus generally available, a changed product name). Fix the sentence to what the source says today, keep the date discipline ("as of November 2026").
   - **hedged** — the source supports a weaker statement than the page makes, or only a secondary source supports it. Weaken the sentence and say what kind of source it is.
   - **unsupported** — no source in the page's Sources section supports it and you cannot find one. Remove the claim, or, if it is plainly an inference, move it into an `> **INFERENCE, NOT DOCUMENTED:**` block or label it as the author's judgement.
   - **unreachable** — the source could not be fetched (say why: 403, 404, timeout, client-rendered). Try an official alternative or an archived copy. If none, keep the claim only if a research brief tags it VERIFIED with a date, and mark the source entry "(not re-fetched in the verification pass)".
4. **Check dates and evidence age.** Every company fact carries a year or "n.d., accessed November 2026" in the sentence. Every source older than about three years (published before November 2023) is flagged in the text where it is used (`**(Evidence age: N years; the current system may differ.)**` or equivalent wording) and in its source entry.
5. **Check the "Where They Differ" table** (Parts I–VIII) cell by cell: each Stripe and Adyen cell is a fact you confirmed above, or "Not public", or (last column) a labeled inference. A cell that says "Not public" must be true as far as you can tell: search for the obvious terms before accepting it, in all of: the provider's documentation index (`https://docs.stripe.com/llms.txt`, `https://docs.adyen.com/llms.txt`), which is known to be incomplete; the documentation sitemap; the help or support center (`support.stripe.com`, `help.adyen.com`); the company's own site and engineering blog; and a web search restricted to the provider's domains. Record in the verification file where you searched. If the provider does document it, replace "Not public" with the fact and its source.
6. **Check every link.** Every URL in Sources and Evidence returns a page (follow redirects; note a changed URL and replace it with the final one). Every `[[permalink]]` is in the style guide's valid list.
7. **Sources section.** Every source cited in the text has an entry; every entry is used in the text (remove unused ones); entries follow the format `- [Title](URL), Publisher or author, publication date (or "n.d., accessed 2026-11") — what it supports.` in the three italic-labeled groups; the closing line is present.

Write the result to `ROOT/_research/verification/<folder>.md`: a table `# | Claim (short) | Source URL | Status | What changed`, then a short list of anything you could not verify and what you did about it. This file is the evidence that the claim check was done; be complete and honest in it. A claim you did not check is listed as "not checked", never as confirmed.

## B. Rulings and format

- **Ruling 22:** no external URLs in the running text. Reduce each inline `[text](https://…)` to plain text with the attribution in the sentence (who, what kind of document, year), after checking that the URL is in Sources and Evidence (add it if missing). Leave `[[permalink]]` links and the failure-patterns callout link alone.
- Hand-offs and part references use `[[part-N]]` and `[[permalink]]`, never hard-coded `.html` links or plain "Part III".
- Front matter complete; callouts in order with exact labels; exactly three KEY POINTS; required sections present for the page's kind; `timetoread` equals the `check_draft.py structure` word count ÷ 230.
- Every payments, banking, regulatory or billing term is defined in one clause on first use in the page; every acronym expanded.
- American spelling; none of the style guide's banned words.
- **Do not add, drop, merge or reorder units.** If a fix needs that, make the change in `spec.json` too (same order, same count), re-run `python3 _wiring/validate_spec.py payments-platform-architecture <folder>` and `python3 _wiring/check_draft.py structure _journals/payments-platform-architecture/posts/<folder>`, and add a changelog entry to the spec. Editing wording inside a unit needs no spec change.
- Do not touch illustration placeholders except to correct a factual error in a caption.

## C. Larkfield consistency

Every Larkfield figure, date, name and decision agrees with the ledger and with the page that owns the topic. Check weekdays against dates. Where your page contradicts the ledger, fix your page. Where two ledger lines contradict each other, do not pick silently: record it in your verification file under "Ledger conflicts" and follow the chapter that owns the topic in PLAN.md.

## Files you may write

Your assigned pages' `index.md` and `spec.json`, and `ROOT/_research/verification/<folder>.md`. Nothing else. Problems on other pages go in your verification file under "For other pages".

## Finish

- `python3 _wiring/validate_spec.py payments-platform-architecture <folder>` passes; `check_draft.py structure` passes.
- Build: `python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient error from a parallel build can be ignored if a rerun passes).
- Render check: `python3.11 _journals/payments-platform-architecture/_research/tools/render_check.py <permalink>`; fix `XJ:` entries other than the allowed ones.
- Append to the spec's changelog: `{"date": "2026-11-17", "change": "Verification pass: N claims checked (a confirmed, b corrected, c hedged, d unsupported and removed or relabeled, e unreachable); <one line on the most significant fix>."}`

## Report back

Under 200 words per page: counts by status; every correction (what the page said, what the source says); claims removed or relabeled; sources that could not be reached; ledger conflicts; anything the author must decide.
