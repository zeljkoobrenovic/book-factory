---
name: field-evolution
description: Write the "how we got here" page of a book-shaped journal — a short, plain-language walk from the field's simplest beginning to its current complexity, one step at a time, introducing each key concept at the step that created it, so that the failure patterns that follow read as natural consequences. Use when asked to add, write or revise a history, evolution, origins or "how did it get this complicated" page for a journal in _journals/*/, typically placed in the Preface before the failure-patterns page (for payments — from cash, credit at the village shop and checks to cards, card networks, online payments and platforms).
---

# Field Evolution (the "how we got here" page)

## Goal

Write one preface page that takes a reader who knows nothing about the field
from its **simplest beginning to its present complexity**, in very simple
terms, and leaves them thinking: *given all that, of course these systems fail
the way they do.*

The page is **not a history of the field**. It is an explanation of today's
complexity told in the order it accumulated. Every step exists to introduce a
concept the rest of the book uses, at the moment the world first needed it.
What does not introduce such a concept is left out, however interesting.

It sits in the Preface **after the introduction and before the failure-patterns
page**, and it hands off to that page: the last step of the walk is "and this is
why the following patterns are natural".

## The shape of the page

**One step = one new need, one new concept, one thing it made possible, one new thing that can go wrong.**

Each step is written the same way, in four or five short paragraphs:

1. **Where things stood.** One or two sentences in everyday terms.
2. **What stopped working, or what people wanted next.** The pressure that
   forced a change: distance, strangers, volume, speed, theft, regulation.
3. **What was added, and its name.** The mechanism in plain words first, then
   the term the book uses for it, in bold, with a `[[link]]` to the chapter
   that owns the term. Never the term before the plain words.
4. **What it made possible.** Who could now do what they could not do before,
   for **each side**: the seller who wins a sale or keeps a customer who would
   have gone elsewhere, the buyer who can buy at all. A step is a bargain
   people wanted, not a burden imposed on them, and the page must show the
   gain before the price. (The shopkeeper's promise is a risk for the
   shopkeeper, and also the reason the customer shops there and can eat
   before payday.)
5. **What it cost.** The new party, the new delay, the new copy of a record,
   or the new way to be cheated that came with it. This sentence is what the
   failure-patterns page will pick up.

Rules that give the page its character:

- **Start simpler than the reader expects, then complicate the simple case
  once.** The first step is the form everyone understands (for payments: cash
  for goods, settled on the spot). Then show that even this was never quite
  simple (the village shop that sells on a promise and is paid on payday: a
  debt, a record of it, trust, and a customer who might not pay). The
  complication plants the book's central idea before any technology appears.
  Let the same early scene introduce the field's standing concerns as well as
  its first concept: the shopkeeper who gives credit also decides whom to
  trust, how much, and when to stop, which is risk management in its
  plainest form. A concern met first in a scene anyone can picture is easier
  to recognize later inside a system.
- **Six to nine steps.** Fewer reads as a list of two eras; more reads as a
  history. Merge steps that add no new concept.
- **Order by dependency, not strictly by date.** Usually these coincide. Where
  they do not, put a step where the reader needs its concept and say "by then"
  or "meanwhile". Do not reorder in a way that implies a false chronology.
- **Every step moves the same thing forward.** Pick the one question the whole
  walk keeps asking (for payments: *when is it really paid, and who is on the
  hook until then?*) and answer it again at every step. The answer getting
  longer is the argument of the page.
- **Very simple language.** Short sentences, everyday examples, one new term
  per paragraph at most. A reader who has never heard of the field follows
  every sentence. Follow the journal's style guide for voice and banned words.
- **Concrete words, especially in the opener.** The KEY POINTS and the lead
  name the actual things (the shopkeeper's notebook, the check, the card, the
  seller, the buyer, the wait for the money), not abstractions. Do not build
  the page on a metaphor such as "layers": say "step" or "way of paying", and
  if the stack image is used at all, use it once, next to the figure that
  draws it. A reader should be able to picture every sentence of the opener.
- **A running tally.** After the steps, one table: `Step | What it made
  possible | What it added | New party or delay | What can now go wrong`. The last column uses the book's
  failure-pattern names where one applies, and plain words where none does.
- **An anchor timeline, if the page has dates.** After the tally, a small
  table `Year | What its source dates to that year | Step`, holding only the
  dated facts the steps already gave, in order of time. It adds no date, and
  says why the undated steps (common practice, not events) are absent. It
  shows the reader how old or how recent each step is; it does not replace
  the walk, which stays in the order of the ideas.
- **End on today.** The last step is the present state of the field as the
  book describes it (not a forecast), and the closing paragraph says how many
  parties, records and promises now stand behind the simple act the page
  started with, then hands off to the failure-patterns page.
- **One figure per step, as a series.** Each step gets one small human scene
  that shows its gain and its price together (the baker and the coin; the
  shopkeeper, the notebook and the calendar with payday circled). The scenes
  share one visual language, so the reader sees the same customer and seller
  with one more thing between them each time. Add one overview figure that
  shows accumulation: the same simple act at the bottom, one band per step.

## Evidence discipline

A history invites confident folklore. The journal's evidence rules apply here
as everywhere:

- **Dated facts are sourced.** A year, a founding, a first, a law, a standard,
  a number: each rests on a source the journal's style guide would accept
  (the institution's own history page, a standard body, a regulator, a
  filing), is fetched and read before it is written, and is listed under
  Sources and Evidence. Where a chapter of the book already establishes the
  fact, link the chapter and reuse its source.
- **Few dates, well chosen.** A dozen anchor dates at most. The page teaches
  an order of ideas; it does not need the year of everything.
- **The simplification is declared.** Say once, early, that this is a
  simplified account that follows the ideas, that real history was messier and
  differed by country, and that the chapters carry the detail. Mark each
  generalization about "how people paid" as common practice, not as a fact
  about a time and place, unless a source supports it.
- **No "first ever" claims without a source**, and none about what a company
  or network "wanted" or "realized". Say what was introduced and what it made
  possible.
- **Illustrations are labeled.** The village shop, the traveling merchant and
  similar scenes are illustrations, and the text says so. If the journal has a
  fictional running example, bring it in only at the last step, as today's
  case; do not project it into the past.

## Contract and workflow

This page is an ordinary page of the journal and goes through the journal's
normal pipeline. This skill decides its content and shape; the mechanics
belong to the skills it calls.

1. **Read** the journal's `PLAN.md`, style guide, `journal-spec.json` (the
   journal thesis and the preface part), the failure-patterns page or its plan
   entry (pattern names and families), and the glossary or the chapters'
   "Owns" lists, so you know which concepts the book needs introduced and
   which chapter owns each.
2. **List the concepts** the walk must introduce, each with its owning
   chapter. Then **choose the steps**: for each candidate step write one line,
   `need -> concept -> gain (seller, buyer) -> cost`. Drop a step that cannot
   fill all four.
   Check that every concept on the list lands in exactly one step, in an order
   in which no step uses a concept a later step introduces.
3. **Check the page is wired.** The page needs an entry in the journal spec
   (kind `front_matter`, in the preface, between the introduction and the
   failure-patterns page), a line in `config.yaml` in the same place, and a
   contract in `PLAN.md`. If any is missing, add it with the `journal-spec`
   skill's rules (the author decides the argument; adding a page changes the
   preface's flow and the transitions of its neighbors) and say what you
   changed. Its thesis is a real thesis: a disputable claim about *why* the
   field is complex (for example: "each layer was a reasonable answer to a
   real limit of the one before, and none of them was ever removed"), not
   "this page tells the history".
4. **Write the spec** with the `spec-creator` skill: one section per step, the
   tally and the closing as the conclusion. Acceptance criteria are reader
   outcomes, for example: *given a concept from a later chapter, the reader
   says which step introduced it and what limit it answered*; *given a failure
   pattern's name, the reader says which layer makes it possible*.
5. **Verify the dated facts** by fetching their sources, then **write the
   article** with the `detailed-article` skill, in the shape above. Length:
   **3,000–4,200 words** (nine steps with gain and cost each need about 350
   words a step). If it wants to be longer, a step is carrying history that
   introduces no concept: cut it.
6. **Build and check** as the journal's writer brief says (validate the spec,
   structure check, build, render check). Then tell the author which
   neighbors now need a matching edit: the introduction's roadmap and hand-off,
   the failure-patterns page's opening (it can now say "the layers of the
   previous page" instead of re-explaining them), and any "pages in this book"
   count in the README or plan.

## Checks before finishing

- A reader new to the field can retell the walk in one sentence per step.
- Every concept is in plain words before its term, and every term links to
  the chapter that owns it.
- The same question is answered at every step, and the answer grows.
- Each step names what it made possible for both sides, and what it cost;
  the tally's last column matches the book's failure-pattern names exactly.
- The KEY POINTS contain no abstraction a newcomer cannot picture.
- Every dated fact has a fetched source; the simplification is declared; no
  motives are attributed.
- The page ends on the present and hands off to the failure-patterns page.

## Anti-patterns

- A page that is a timeline of events and founders. (History, not
  explanation. A short anchor timeline after the tally is fine.)
- A step that adds a date but no concept.
- Terms first, meaning later; or three new terms in one paragraph.
- "Then technology made everything faster" steps that name no new party,
  delay, record or risk.
- A walk that lists only problems. Every step was adopted because it let
  people trade who could not before; a page that shows only the costs makes
  the complexity look like a mistake.
- An opener built on an abstraction ("layers", "gaps", "separation") in
  place of the things themselves.
- Nostalgia for the simple past, or a claim that the complexity is anyone's
  mistake. Each layer was a reasonable answer to a real limit.
- Unsourced folklore, "first ever" claims, or the fictional running example
  placed in the past.
- Re-explaining what the introduction or the failure-patterns page already
  says, instead of linking to it.
