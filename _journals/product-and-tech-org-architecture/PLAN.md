# Book Plan

**Title:** Architecting Product & Tech Organizations — *Applying system design and product thinking to teams, interfaces and decision rights — and how AI moves the constraint*

**Status:** Phase 1 approved 2026-11-19; Phase 2 (specs, then chapters) in progress · **Created:** 2026-11-19

This file holds the title, thesis, structure, table of contents, input and anchor mapping, gaps and decisions.

## Decisions (author, 2026-11-19)

| Question | Decision |
| --- | --- |
| Title | Option 1, as above |
| Size | 41 chapters in 11 parts (40, plus the product-lens chapter added below) |
| Two lenses | The book applies **system design and product thinking** to organization design: design the organization like a system, and run its design like a product. New chapter 2, *The Organization as a Product*; every chapter states the user and the outcome measure of its patterns |
| Words per chapter | 3,500–5,000 |
| Running example | One fictional company followed through all five scaling stages |
| AI treatment | "What AI Changes Here" in every chapter of Parts I–X; Part XI synthesizes |
| The Gebler posts | Theme prompts only; not cited |
| Existing `grounded-*` and `org-design` journals | Cross-linked, not absorbed |
| Folder name | Renamed to `product-and-tech-org-architecture` |

Not yet answered, proceeding on these defaults until told otherwise: employer-internal material is not used; the author's job architecture, rituals catalogue and controls appear as reference templates; the default reader works in a single company with several product lines; data, design and security leadership get one section each in chapter 18, not chapters of their own; the repository's outcome-spec pipeline is used (journal spec → post specs → draft → draft check).

## 1. Title options

| # | Title | Subtitle | Why |
| --- | --- | --- | --- |
| 1 (recommended) | **Architecting Product & Tech Organizations** | *Applying system design and product thinking to teams, interfaces and decision rights — and how AI moves the constraint* | Matches the series ("Architecting Agentic Systems"), says exactly what the book does, searchable. |
| 2 | **The Organization Is the System** | *Architecting product and technology organizations from 10 to 1,000+ people* | Leads with the thesis; stronger as a statement, weaker as a search term. |
| 3 | **Load-Bearing Structure** | *How product and tech organizations are designed, scaled and rebuilt* | Most distinctive; the metaphor (some structure carries load, most does not) is useful but needs the subtitle to be understood. |

## 2. Thesis

A product and tech organization is a system, and it can be architected like one: teams are components, ownership boundaries are module boundaries, rituals and contracts are interfaces, and work, information and decisions are the flows. The architecture's job is to place three scarce capacities — **attention** (cognitive load), **judgment** (who decides what, with which context) and **verification** (how the organization knows that what it built is right and worth building) — where the work needs them, and to keep the cost of coordination below the value it buys. Most organizational failures are architectural: a boundary in the wrong place, an interface nobody owns, a decision made far from its information, a structure kept after the constraint it was built for has moved. Will Larson's models describe how to size, staff and run the engineering side of that system; *Build What Matters* describes how a vision becomes outcomes on the product side; they meet at planning, decision rights and metrics, and the book resolves them there. AI makes the architectural view urgent rather than optional: when producing code and artifacts becomes cheap, the constraint moves to deciding what is worth building and verifying that it is correct, safe and valued — so team size, roles, ratios and cadences that were designed around scarce production capacity have to be re-derived, not assumed.

**Two disciplines, applied to the organization itself.** *System design* says what the organization is and what can be changed: components, interfaces, flows, constraints, four levers, trade-offs and failure modes. *Product thinking* says how the changing is done: the organization has users (the people and teams in it, and the teams and customers who depend on each team) and owes them outcomes, so a change to it is discovered before it is designed, given an outcome, placed on a roadmap toward a vision of the organization, tested with the smallest change, and judged by the outcome it moves. Larson's models supply most of the first; *Build What Matters* supplies the second, applied here to the organization as well as to the product it builds.

Three ideas run through every chapter:

- **Structure follows the constraint.** Each design choice is justified by the capacity that is scarce at that stage and scale. When the constraint moves (growth, a platform, AI), the structure is revisited.
- **Interfaces matter more than boxes.** The org chart is the least informative diagram. Team APIs, interaction modes, decision rights and planning contracts decide how the system behaves.
- **Every structure has a failure mode and an expiry date.** Each pattern is presented with what it costs, how it fails, and the signal that says it is time to change it.

## 3. Assumptions made from the inputs

The prompt had unfilled placeholders. I resolved them from this folder as follows; correct any that are wrong.

| Placeholder | Resolved as |
| --- | --- |
| Favorite books | `_input/bookshelf/data/leadership.json` (13 categories) and `hard-skills.json` (5 categories), plus 54 reading-notes PDFs in `bookshelf/docs/notes/`. The PDFs are not read yet; each is read when its chapter is written. |
| Checklists | `_input/checklists/data/data.json` — 9 tabs, about 190 checklists, templates and rubrics (the CTO Starter Kit content). |
| My projects | `_input/my-project-links.txt`, read from the local copies under `~/PycharmProjects` (the live sites are JavaScript-rendered). See "Local project sources" below. |
| AI material | `_input/ai-posts/` — five LinkedIn posts by a practising CTO from October–November 2026 on AI and engineering organizations. Used as theme prompts only; not cited. |
| "*-system-architecture book format" | The sibling books in this repository (`agentic-systems-architecture`, `payments-platform-architecture`, …): Preface (introduction, failure patterns, running example), numbered Parts each with an intro page, chapters, and a Reference section. |
| Words per chapter | Proposed 3,500–5,000. |

**Local project sources.** Surveyed at the level of structure and titles; each is read in full when its chapter is written.

| Project (local folder) | What it holds that the book can use | Chapters |
| --- | --- | --- |
| CTO Starter Kit (`cto-starter-kit`, ctostarter.com) | The executive journey as steps with a one-line reason each: First 90 Days, First Year, Long Term, with links into the checklists and "hidden blocker" notes. Also a directory of CTO and product-leader communities. | 13, 18, 23, 24, 26, 28, 30; toolkit |
| Lightweight Data Explorers (`lightweight-data-explorers`) | A product and technology **job architecture** (IC and management levels across product management, design, research, product operations, engineering); a **rituals** catalogue (triad sync, roadmap review, architecture review, incident review, quarterly planning, QBR); **golden paths**; management, operational, engineering and security **controls** with red/yellow/green maturity; a balanced **business scorecard**; Workday people and Slack activity explorers. | 14, 15, 24, 25, 28, 29 |
| Personal Roadmaps (`personal-roadmaps`) | An executive's operating system: focus areas tied to outcomes, initiatives as hypotheses, inspection per delegated area, a commitments ledger, and teams tagged with a type and one of Larson's four team states. | 5, 23, 29 |
| Productscape (`productscape-workspace`) | A method and schema for modelling a product domain: customers, jobs to be done, strategy, products, product bricks, streams, data assets, competition. Useful as the product-side map that team boundaries are drawn against. | 4, 6, 10 |
| LinkedIn Org Mapper (`linkedin-org-mapper`) | A way to reconstruct an organization's functional shape from public profiles. A method for comparing org shapes, not a source of findings. | 29, 32 (method only) |
| obren.io (`zeljkoobrenovic.com`) | Small tools: leadership ladder, OKR pad, value-stream mapping, risk matrix, start-stop-continue, reading notes, catalogs. | toolkit |
| Grounded Architecture (grounded-architecture.io) | Governance by nudges, taxes and mandates; the architecture operating model; lightweight architectural analytics; architect career paths and archetypes; the *Six Simple Rules* and *Culture Map* reflections. | 1, 14, 21, 29, 31 |

Company-internal folders on this machine (`aviv_*`, `de-engineering-strategy`, `capabilities-*`, `iwt_tech_onboarding_docs`) are **not** used unless you say so; they look like employer material rather than published work.

**Existing journals in this repository overlap with this book** and are treated as inputs too: `org-design` (17 decision records), `grounded-engineering-executive`, `grounded-engineering-management`, `grounded-product-management`, `grounded-platforms`, `grounded-people-management-tools`, `tech-strategy`, `ai-dev-strategy`. Those journals restate one source per record as a checklist. This book does the thing they do not: it connects the sources, shows where they conflict, and takes a position. Chapters cross-link to those records rather than repeat them.

**Bookshelf metadata to fix before citing** (the JSON lists these authors incorrectly; the book will cite the right ones): *The Engineering Executive's Primer* and *Crafting Engineering Strategy* are by Will Larson; *Product Operations* is by Melissa Perri and Denise Tilles; *The Hard Thing About Hard Things* is by Ben Horowitz; *Supercommunicators* is by Charles Duhigg; *AI Engineering* and *Designing Machine Learning Systems* are by Chip Huyen.

## 4. Structure and conventions

**Mapping the requested output to this repository.** The prompt asks for one Markdown file per chapter plus README, glossary, bibliography and a checklist appendix. Here that becomes: one post folder per chapter (`posts/<nn-slug>/index.md`), an `introduction` page (preface and how to read the book), and a Reference section with `toolkit` (all checklists collected), `glossary` and `bibliography`. Each chapter's checklist can also ship as its `checklist.md` tab.

**Chapter template** (from the prompt): The problem → Principles → Patterns → Anti-patterns → Trade-offs → Example → Checklist or decision framework → Key takeaways. Two additions:

- **"What AI Changes Here"** — a short section in every chapter of Parts I–X, with each claim labeled **proven**, **emerging** or **speculative**. Part XI then synthesizes rather than introduces. This keeps AI from being an appendix and keeps each chapter standing alone.
- **"Where the Sources Disagree"** — only in chapters where they do. States the tension and the book's resolution.

**Evidence labels.** Every claim is one of: source (book and concept named), research finding, documented practice (a named company's published account), the author's experience, recommendation, or illustration. No invented statistics or case studies.

**Running example.** Corvane, a fictional field-service scheduling software company, followed through the five scaling stages (10 → 50 → 150 → 500 → 1,000+), so the same organization is seen breaking and being re-architected at each stage. Labeled fictional throughout, with a ledger of shared facts as in the sibling books.

**Diagrams.** Mermaid for org structures, interaction modes and decision flows; tables for comparisons and trade-offs.

## 5. Table of contents

59 pages: 4 preface pages, 11 part introductions, 41 chapters, 3 reference pages (part introductions not listed below).

Anchor codes: **L-EP** = Larson, *An Elegant Puzzle* · **L-Primer** = Larson, *The Engineering Executive's Primer* · **BWM** = Foster & Nerlikar, *Build What Matters* · **TT** = Skelton & Pais, *Team Topologies* · **GA** = the author's *Grounded Architecture*.

### Preface

- **Introduction: The Organization Is a System You Design.** The thesis, who the book is for, how an executive and an IC read it differently, a "start from the decision in front of you" routing table, the evidence labels, and how the anchors are used.
- **How Organizations Got Complicated: From Three People at One Table to a Thousand.** A short, plain walk through the structures a growing organization adds — manager, product role, split teams, platform, layers, plan, ladder, metric — one need and one concept per step, so the failure patterns read as consequences. Added 2026-11-19 at the author's request.
- **Where Product & Tech Organizations Go Wrong.** Twelve named failure patterns in four families, one per designable element (for example: the Org Chart as Architecture, the Feature Factory, the Platform Nobody Asked For, the Reorg as Strategy, the Review Bottleneck), each with warning signs, mechanism, cost, and the chapters that address it. Draws on BWM's product dysfunctions, Lencioni's five dysfunctions and Larson's team states.
- **Meet the running example.** The fictional company, its product, its stages and the recurring incidents the chapters return to.

### Part I — FOUNDATIONS: The Organization as a System

1. **The Organization as a System That Can Be Architected.** What it means to treat an org as a system: components, interfaces, flows, constraints, feedback loops. What org design can change (boundaries, interfaces, decision rights, incentives) and what it cannot (skill, trust, strategy). Introduces the three scarce capacities used throughout. *Anchor:* L-EP (systems thinking). *Leads:* Meadows, *Thinking in Systems*; Morieux & Tollman, *Six Simple Rules*.
2. **The Organization as a Product: Who It Serves and What It Owes Them.** The second lens. Who the users of an organization's design are, what an outcome of an organizational change is as distinct from its output, and how to run a change as product work: discovery, a stated outcome, a place on a roadmap toward a vision of the organization, the smallest change that tests the diagnosis, an outcome review. Where the analogy stops. *Anchor:* BWM (key outcomes, vision, balanced roadmap, dysfunctions), applied to the organization itself as the author's extension. *Leads:* Perri, *Escaping the Build Trap*; Morieux & Tollman (understand what people do); L-EP (validating a reorganization). Added 2026-11-19.
3. **Conway's Law and the Inverse Conway Maneuver.** Why systems mirror communication structure, the evidence for it, and how to use it deliberately. Where the inverse maneuver works and where it fails (the architecture you want needs skills or trust the teams do not have). *Leads:* TT; Conway (1968). *Inputs:* Conway's Law and Org Chart Problems checklists.
4. **Cognitive Load and Team Boundaries.** Cognitive load as the sizing constraint for what one team can own; fracture planes; domain boundaries from Domain-Driven Design; how to detect an overloaded or underloaded team. *Leads:* TT; Evans. *Inputs:* Team-First Thinking and Team-First Boundaries checklists.
5. **Flow and the Constraint.** Finding the step that limits the whole system; why local optimization makes it worse; Larson's four team states (falling behind, treading water, repaying debt, innovating) as a diagnosis and what to add in each state. *Anchor:* L-EP. *Leads:* *Accelerate*; *The Phoenix Project*. *Gap:* theory of constraints (Goldratt) and queueing (Reinertsen) are not on the bookshelf.

### Part II — TOPOLOGY: Teams and Their Interfaces

6. **Team Types: Stream-Aligned, Platform, Enabling, Complicated-Subsystem.** The four types, what each owns, and when each is justified. Compared with the product-team topology in *Empowered* (platform and experience teams) and BWM's "right team". *Leads:* TT. *Inputs:* Four Fundamental Topologies checklist; `org-design` records.
7. **Interaction Modes and Team APIs.** Collaboration, X-as-a-Service, facilitating; the team API as an explicit contract; how the wrong mode shows up as dependency queues and meetings. *Leads:* TT. *Inputs:* Team Interaction Modes checklist; team charter example.
8. **Team Size and Composition.** Larson's sizing rules (six to eight engineers per manager, four to six managers per manager of managers, no teams below four), why they exist, and the composition of a product team (product, design, engineering, data). Where smaller teams work and what they give up. *Anchor:* L-EP. *Inputs:* Organizational Design checklist; `org-design/team-size-and-composition`.

### Part III — PRODUCT OPERATING MODEL

9. **Outcomes Over Output.** The product dysfunctions BWM names, key outcomes for customers and the business, and why output-driven organizations look productive. Compared with Perri's build trap. *Anchor:* BWM. *Inputs:* Product Dysfunctions and Key Outcomes checklists.
10. **Vision and Product Strategy.** The customer journey vision, working backward from it, and strategy as the sequence of bets that gets there. Compared with Rumelt's kernel and Cagan's vision and principles. *Anchor:* BWM. *Leads:* Rumelt; Cagan. *Inputs:* Customer Journey Vision and Product Strategy checklists.
11. **Roadmaps and Horizons.** The balanced roadmap (innovation, iteration, operation), outcome-based roadmaps, how far ahead a roadmap can honestly look, and what it commits to. *Anchor:* BWM. *Inputs:* Balanced Roadmap checklist; Roadmapping Guide template.
12. **Discovery, Delivery and Empowered Teams.** What a team is empowered to decide, dual-track work, and product operations as the supporting system. **Tension resolved here:** vision-led (direction set at the top) versus empowered (problems solved at the edge) — the book's position is that the vision constrains the problem space and the team owns the solution space, with the boundary made explicit. *Anchor:* BWM. *Leads:* Cagan, *Inspired*, *Empowered*, *Transformed*; Perri & Tilles, *Product Operations*.

### Part IV — ENGINEERING OPERATING MODEL

13. **Engineering Strategy.** Diagnosis, guiding policies and operations; how an engineering strategy is written, launched and reviewed; how it relates to the product strategy of chapter 10. *Anchor:* L-Primer; Larson, *Crafting Engineering Strategy*. *Inputs:* seven Engineering Strategy checklists; `tech-strategy` journal.
14. **Architecture Governance: Advice, Guardrails and Mandates.** Who decides technical direction at each scale; nudges, taxes and mandates; architecture as advice; ADRs; the architect as connector between levels. *Leads:* GA (governance principles, operating model); Hohpe, *The Software Architect Elevator*. *Inputs:* `org-design/architecture-as-advice-and-guardrails`.
15. **Platforms and Developer Experience.** When a platform team earns its cost, platform as a product, the thinnest viable platform, and how to judge a platform. *Leads:* Fournier & Nowland, *Platform Engineering*; Hohpe, *Platform Strategy*; TT. *Inputs:* Platforms tab (30 checklists); `grounded-platforms`.
16. **Quality and Reliability as Operating Model.** Who owns quality, where QA sits, on-call and incident ownership, launch readiness, and the capabilities *Accelerate* links to delivery performance. *Leads:* *Accelerate*; *Continuous Delivery*. *Inputs:* Operational Excellence checklist; `org-design/quality-engineering-enablement`.
17. **Migrations and Technical Debt.** Larson's argument that migrations are the only scalable fix for technical debt, how to run one (derisk, enable, finish), and how to fund debt work in planning. *Anchor:* L-EP. *Inputs:* Systems & Tools checklist; Rearchitecting Platforms checklist.

### Part V — LEADERSHIP STRUCTURE

18. **Executive Roles and Reporting Lines.** CTO, CPO, VP Engineering, heads of design, data and security: what each role is for, the common configurations (separate CTO and CPO, combined CPTO, CTO plus VPE), where design, data and security report, and the first-team principle. *Anchor:* L-Primer. *Leads:* BWM ("right team"); Lencioni. *Gap:* the data and design executive roles are thin in the inputs.
19. **The Product–Engineering–Design Triad.** The triad at team, group and executive level; who decides what; how it fails (product as order-giver, engineering as veto, design as decoration). *Anchor:* BWM and L-Primer jointly. *Leads:* Cagan. *Inputs:* `org-design/product-engineering-partnership`.
20. **Spans, Layers and Managers of Managers.** How spans and layers are derived from team sizing, what each layer is for, the cost of a layer, and what changes when managing managers. *Anchor:* L-EP. *Leads:* Fournier, *The Manager's Path*; Grove, *High Output Management*. *Inputs:* Managing Multiple Teams and Managing Managers checklists.
21. **Staff-Plus and Architects: The Technical Leadership Track.** Staff archetypes, what technical leaders own that managers do not, and how the track connects to governance (chapter 14). *Leads:* Larson, *Staff Engineer*; Reilly, *The Staff Engineer's Path*; GA; Hohpe. *Inputs:* `org-design/staff-plus-technical-leadership`.

### Part VI — ALIGNMENT: Decisions and Planning

22. **Decision Rights and Decision Records.** Who decides, who is consulted, how the decision is recorded; RFCs and ADRs; Larson's policy, consensus and conviction styles; Marquet's intent-based leadership; Drucker on effective decisions. *Anchor:* L-Primer. *Leads:* Drucker; Marquet. *Gap:* named decision-rights frameworks (RAPID, DACI) are not in the inputs.
23. **Planning: Budget, Allocation, Roadmap, Objectives.** **The main point where the anchors meet.** Larson's planning separates the financial plan, the functional allocation and the roadmap; BWM derives the roadmap from vision and outcomes. The book's resolution: Larson's model sets how much capacity goes where, BWM's sets what the capacity is for, and team objectives (*Empowered*) are the contract between them. Planning cadences and what they cost. *Anchor:* L-Primer and BWM jointly. *Gap:* OKR literature (Doerr, Wodtke).
24. **Operating Cadence: Meetings, Writing and Communication Paths.** The minimum set of recurring forums an organization needs at each size, written-first communication, documentation as an interface, and information flow as a design decision. *Anchor:* L-Primer. *Leads:* Grove; *No Rules Rules*. *Inputs:* Effective Meetings and Internal Communication checklists.

### Part VII — TALENT SYSTEMS

25. **Career Ladders and Leveling.** What a ladder is for, the dual track, level definitions that survive calibration, and the failure modes (title inflation, the ladder as checklist). *Anchor:* L-EP. *Leads:* Orosz, *The Software Engineer's Guidebook*. *Inputs:* Careers checklist; `org-design/career-paths-and-progression`.
26. **Hiring and Onboarding.** Hiring as a pipeline to be designed and debugged, structured interviews and rubrics, hiring executives, and onboarding as the other half of hiring. *Anchor:* L-Primer and L-EP. *Leads:* Bock, *Work Rules!*. *Inputs:* four interview frameworks and rubrics; Hiring and Engineering Onboarding checklists.
27. **Performance, Calibration and Growing Managers.** Performance systems, calibration, managing underperformance, promotion, and how managers are developed and judged. *Anchor:* L-EP. *Leads:* Zhuo; Fournier; Scott, *Radical Candor*; Johnson, *Scaling People*. *Inputs:* `grounded-people-management-tools`.

### Part VIII — HEALTH: Measuring the Organization

28. **Measuring Engineering.** Larson's distinction between measuring to plan, to operate, to optimize and to inspire; DORA's four keys; SPACE and developer experience; what each can and cannot tell you, and how metrics get gamed. *Anchor:* L-Primer. *Leads:* *Accelerate*. *Gap:* SPACE and DevEx papers (Forsgren, Storey, Noda and co-authors) are not in the inputs. *Inputs:* Measuring Engineering Organizations checklist; `org-design/org-health-and-flow-metrics`.
29. **Product Outcomes and Organizational Health Signals.** Key outcome metrics and how they tie to planning; leading signals of organizational trouble (attrition patterns, dependency wait, decision latency, on-call load); Larson's inspected trust as the practice that connects metrics to management. *Anchor:* BWM and L-Primer. *Leads:* GA (lightweight architectural analytics, as the method for cheap organizational data).

### Part IX — CULTURE AS ARCHITECTURE

30. **Values, Operating Principles and Rituals.** Values as decision rules rather than posters; Larson's tests for useful values; rituals as recurring interfaces; freedom and responsibility (Netflix) against inspected trust. *Anchor:* L-Primer. *Leads:* *No Rules Rules*; *Work Rules!*; Stripe's operating principles (example in the checklists).
31. **Trust, Conflict and Psychological Safety.** Trust as the precondition for every interface in the book; Lencioni's pyramid; candor and conflict; working across national cultures. *Leads:* Lencioni; Brown; Scott; Covey; Meyer, *The Culture Map*. *Gap:* Edmondson's work on psychological safety is not on the bookshelf.

### Part X — SCALING AND EVOLUTION

32. **Scaling Stages: What Breaks at 10, 50, 150, 500 and 1,000+.** For each stage: the structure that works, the constraint that appears, the first role and process you now need, and what to stop doing. The central reference chapter of the book. *Anchor:* L-EP and L-Primer. *Leads:* Johnson, *Scaling People*; Horowitz; Slootman. *Gap:* stage models (Greiner) and group-size research are not in the inputs; stage thresholds are presented as heuristics, not laws.
33. **Reorganizations: When and How.** When a reorg is the right tool and when it is avoidance; Larson's method (validate the need, project headcount, design, roll out); migrating an organization incrementally; evolving topologies. *Anchor:* L-EP. *Leads:* TT (Evolve Team Structures); Flyvbjerg, *How Big Things Get Done*. *Gap:* Helfand, *Dynamic Reteaming*.
34. **Shocks: Hypergrowth, Downturns and Acquisitions.** What each does to the system and what to protect: onboarding capacity in hypergrowth, trust and focus in a downturn, integration choices in an acquisition. *Anchor:* L-EP (hypergrowth), L-Primer (M&A). *Inputs:* Managing Downturn and M&A checklists.

### Part XI — AI AND THE ORGANIZATION

35. **Where the Constraint Moves.** When implementation gets cheap, which capacity becomes scarce: problem selection, specification, verification, absorption by customers. The evidence so far, including where studies disagree. *Leads:* DORA reports on AI-assisted development; published productivity studies. No anchor covers this.
36. **Team Shape and Roles.** What changes for the engineer, PM, designer, QA and engineering manager; the move toward product engineering; smaller teams and what that does to on-call, bus factor and spans. Each claim labeled proven, emerging or speculative. *Revisits:* chapters 8, 19, 20.
37. **Agentic Delivery: Builders, Reviewers and the Verification Pipeline.** Agentic workflows in the delivery process, the ratio of produced change to review capacity, moving checks into the pipeline so human attention goes to decisions that need judgment, and modularity as the enabler. *Leads:* *Architecting Agentic Systems* (sibling book); `ai-dev-strategy` journal. *Revisits:* chapters 16, 17.
38. **AI Platform Teams, Governance and Risk.** Whether AI capability belongs in a platform team, an enabling team or every team; model and tool governance; security and compliance keeping pace with change volume; AI spend as an operating-model decision. *Leads:* Huyen, *AI Engineering*; `ai-decisions-log`. *Revisits:* chapters 14, 15.
39. **Skills, Hiring and the Junior Pipeline.** Hiring for work that will change, interviewing when AI can produce a polished answer, how juniors develop judgment when the apprenticeship tasks are automated, and what leaders have to unlearn. *Revisits:* chapters 25–27.
40. **Measuring Productivity with AI.** Why activity and speed metrics mislead more than before, pairing speed with quality and security measures, and measuring at the level of outcomes. *Revisits:* chapters 28, 29.
41. **The Assumptions Ledger.** A table of the assumptions in Parts I–X (team size, manager ratios, planning cadence, roadmap horizon, the PM role, build-versus-buy), each marked: still holds, weakened, or broken, with the evidence level and the signal to watch. The book's closing chapter.

### Reference

- **Toolkit** — every chapter's checklist and decision framework collected, plus templates.
- **Glossary** — terms with one-line definitions and the chapter that owns each.
- **Bibliography** — all sources, grouped by type, with the chapters that use them.

## 6. Where the sources meet and conflict

| Tension | Sources | Resolved in |
| --- | --- | --- |
| Direction from the top vs solutions from the team | BWM (vision-led) vs Cagan (empowered teams) | Ch. 12 |
| Capacity-first vs vision-first planning | Larson (budget → allocation → roadmap) vs BWM (vision → strategy → roadmap) | Ch. 23 |
| Stream-aligned teams vs functional reporting lines | TT vs Larson's manager and ladder structures | Ch. 6, 20 |
| Context, not control vs inspected trust | *No Rules Rules* vs L-Primer | Ch. 30 |
| Mandates vs nudges in technical governance | GA and Hohpe vs standards-first practice | Ch. 14 |
| Fixed manager ratios vs flatter, smaller AI-era teams | L-EP vs emerging practice | Ch. 8, 20, 36 |
| Speed metrics vs verification and security | DORA vs the verification-capacity argument of Part XI | Ch. 28, 40 |

## 7. Gaps in the inputs

Topics the scope requires that the bookshelf and checklists do not cover. For each I would use established, well-known sources and say so in the text.

| Gap | Chapters | Candidate established sources |
| --- | --- | --- |
| OKRs | 23 | Doerr, *Measure What Matters*; Wodtke, *Radical Focus* |
| SPACE and developer experience | 28 | Forsgren et al., "The SPACE of Developer Productivity"; Noda et al., "DevEx: What Actually Drives Productivity" |
| Psychological safety | 31 | Edmondson, *The Fearless Organization* |
| Flow and constraints | 5 | Goldratt, *The Goal*; Reinertsen, *The Principles of Product Development Flow* |
| Scaling-stage models | 32 | Greiner, "Evolution and Revolution as Organizations Grow" |
| Reorganization practice | 33 | Helfand, *Dynamic Reteaming* |
| Decision-rights frameworks | 22 | RAPID (Rogers & Blenko, HBR) |
| Design organization | 18, 19 | Merholz & Skinner, *Org Design for Design Orgs* |
| Data organization and the CDO role | 18 | Thin everywhere in the inputs; needs your direction |
| AI and the organization | 35–41 | DORA AI reports, published productivity studies, vendor and company engineering reports — all to be verified and dated at writing time |

Inputs with little or no role in this book: the Emotional Intelligence, Productivity, Communication, Philosophy and "Dealing with Negativity" shelves, the Managing Self and Security checklist tabs, and the ML Engineering checklists. They are about leading yourself or building systems, not about designing the organization. A few (Lencioni, Brown, Scott, Covey, Meyer) feed chapter 31.
