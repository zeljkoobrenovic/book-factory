# Intro Brief — part introductions

A part introduction is written under `WRITER-BRIEF.md` (outcome spec first, then the article, then the verification steps and report), with these differences from a chapter:

- **Read every chapter of the part in full before writing** (`posts/<folder>/index.md` for each folder the part lists in `config.yaml`). The intro states what the chapters actually argue, in their words and numbers, and must not contradict them.
- **Entry:** the post with id `part-<n>` in `journal-spec.json`, together with the part's own `thesis`, `opening` and `flow`. The title equals the section title in `config.yaml` exactly.
- **Format** (style guide, "Part intros"): front matter as for chapters; the opener is only `> **KEY POINTS:**` with exactly three tight bullets (the part's argument across its chapters; each a bold claim plus one short sentence), then `<br>`; a lead of 2–4 short paragraphs that performs the part's `opening` (hook, bridge, roadmap) and names Larkfield as fictional once; 1–2 illustration placeholders that show the part's shape; `## Chapters in this part` with one paragraph per chapter in config order (`[[permalink]]` first, bold the question each answers, name its Larkfield case), ending with "Begin with [[first-chapter-permalink]]."; then a one-line `## Sources and Evidence` noting that sources are cited in each chapter. No "Where They Differ" section, no take-away tiers, no failure-pattern callout, no Questions to Ask.
- **Length:** 800–1,200 words. The spec is correspondingly small (2–3 sections, 8–14 paragraphs).
- **No new facts.** Every statement about Stripe, Adyen, a network or a regulation must already be in a chapter of the part; link the chapter instead of citing a source.
