# Illustrator Brief — SETTLED visual layer

You are generating the figures of pages of **SETTLED: Architecting Payments and Revenue Infrastructure** (ROOT = `/Users/zeljkoobrenovic/PycharmProjects/book-factory/_journals/payments-platform-architecture/`), a book for engineers and architects new to payments. It matches its sibling books (ORDERED, RECONCILED), which use generated illustrations and no mermaid. The writers have already staged every figure as an `illustration-placeholder` block in the pages; the text has been verified against its sources and corrected since. Your job per assigned page: check each placeholder against the page as it reads now, generate the image, inspect it, replace the placeholder and number the figures.

`GEMINI_API_KEY` is set in the environment. Never print it. Repository root: `/Users/zeljkoobrenovic/PycharmProjects/book-factory` (run scripts from there). Never put the user's name, email or any personal identifier in a request.

## Read first

1. `.claude/skills/article-illustrator/SKILL.md`: placeholder format, asset paths, scripts.
2. `ROOT/_research/style-guide.md`, section on figures (book suffix; real providers are never drawn or named: "Provider A"/"Provider B" or generic elements).
3. For each assigned page: its `index.md` in full.

Scripts: `S=.claude/skills/article-illustrator/scripts`.

**Private scratch:** several illustrators run in parallel. Keep helper files in your own directory under the system temp scratch (`illus-<your first folder>/`), never in a shared location. Edit only your own pages.

## Per page

1. **Validate:** `python3 $S/extract_illustration_placeholders.py ROOT/posts/<folder>/index.md`.
2. **Check each placeholder against the current text before generating.** The page was corrected after the placeholder was written. Every number, date, name and label in the `prompt`, `caption` and `alt` must appear in the page as it reads now and agree with it; a figure must not show something the page now says is unknown as known, or the reverse. Fix the placeholder JSON where it disagrees. The caption states the figure's point in one sentence. The prompt has 5–9 elements with positions and at most about 8 short quoted labels, describes only what should appear, and ends with the book suffix below (add it if missing). No real company, bank, network or product name or logo in any prompt.
3. **Generate:** `python3 $S/generate_illustrations_nanobanana.py ROOT/posts/<folder>/index.md` (no `--replace`).
4. **Inspect every image** with the Read tool against its prompt and caption. Reject an image with a misspelled, garbled or extra label; a wrong number or date; a dollar sign; a missing, extra or misrouted arrow; a logo, brand or real company name; or anything that contradicts the caption or the page. Retry by appending `Corrections: …` to the prompt, then regenerate that one image with `--only <id> --overwrite`. At most 3 attempts; if still wrong, simplify the prompt to the 5–8 elements that carry the caption's point (fewer labels fail less). If it still fails, drop the figure (remove the placeholder) and report it.
5. **Replace and number:** run the generator with `--replace --start-figure 101`, then `python3 ROOT/_research/tools/renumber_figures.py ROOT/posts/<folder>/index.md`. Grep `**Figure` and confirm 1..N with no gaps, every image followed directly by its `**Figure N:** *caption*` line, and any in-text "Figure N" reference still pointing at the right figure.

## Book suffix (every prompt ends with it)

"Style: polished business explainer illustration for a book on payment infrastructure architecture, flat vector style, crisp outlines, minimal shading, light background, disciplined blue, teal, green and orange accents, generous margins. Few short labels, spelled exactly as given in quotes. No photorealism, no 3D render, no dense text, no title text. Draw no logos or brand marks and no real company, bank, card network or software names; show banks, card networks, payment providers, terminals and software as generic unbranded elements. Money is in euros: use the euro sign, never a dollar sign. People are generic customers, studio staff and professionals, never real people."

## Limits

- Do not change prose, except figure-number references handled by the renumber script, and a caption corrected in step 2.
- **Never edit front matter** (another process adds `icon:` and `logo:` lines), `spec.json` units, `config.yaml`, the ledger or other pages. Append one changelog entry to the page's `spec.json`: `{"date": "<today>", "change": "Visual layer: N figures generated and inspected (article-illustrator)."}` and re-run `python3 _wiring/validate_spec.py payments-platform-architecture <folder>`.

## Verify at the end

- `python3 _wiring/check_draft.py structure _journals/payments-platform-architecture/posts/<folder>` passes.
- Build: `python3 _wiring/build.py 2>&1 | grep -iE "error|Traceback" | head` (a transient error from a parallel build can be ignored if a rerun passes).
- Render check: `python3.11 ROOT/_research/tools/render_check.py <permalinks...>`: every page `OK`, all images load.
- `grep -l illustration-placeholder <your index.md files>` prints nothing.
- Log any figure accepted with a known flaw to `ROOT/_research/figure-issues.md` (one small append; re-read its tail first; create it if missing).

## Report back

Under 150 words: per page, figures generated; placeholders corrected against the text (what changed); images retried, simplified or dropped; any figure accepted with a flaw.
