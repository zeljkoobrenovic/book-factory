---
title: "Introduction: The Organization Is a System You Design"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What does this book argue, who is it for, and how should you read it? It argues that a product and tech organization is a system you can design, with system design and product thinking, to place attention, judgment and verification where the work needs them; it runs in eleven parts from foundations to AI, and a routing table takes you from the decision in front of you to the chapter that answers it."
permalink: introduction
timetoread: 18 min read
---

> **KEY POINTS:**
>
> * **An organization is a system you design.** Its behavior comes from its team boundaries, its interfaces, its decision rights and its incentives. Most of its failures are structural, and replacing people leaves them in place.
> * **Two disciplines, three scarce capacities.** System design says what the organization is and what can be changed. Product thinking says whom it is for and how changing it is run. Both serve to place attention, judgment and verification where the work needs them.
> * **Read in order, or start from your decision.** Eleven parts run from foundations to AI, a routing table takes you from a decision to its chapter, and labels tell you what is sourced, what is my judgment and what is illustration.

<br>

In 2022 Corvane had 45 engineers and customers who asked for more than 45 could build. So it hired. Eighteen months of hiring took it to 95 engineers, and by 2024 it shipped less. The median **lead time** for a change, the time from starting work on it to its release, went from 4 days to 19. It now had eleven product teams, and three of them waited for every launch on one platform team, the team that built and ran what all the others shared. And nobody could say who decided that a feature was ready. Corvane is the fictional company this book follows, 180 people at that point, and its numbers are illustrations. The situation is not invented.

You have probably lived through a version of it: a hiring wave, or a reorganization, that was announced with a promise and did not deliver it. The explanations offered afterwards are usually about people: slow new hires, inexperienced managers, teams that did not communicate. None explains why the same thing happens in company after company with different people. This book gives another explanation. The organization was a system. The system had a **constraint**, the one step that limited everything passing through it. And the change did not touch that step.

That explanation is the book's claim. **A product and tech organization is a system, and you can design it** with the two disciplines its own people already practice on their products. System design says what the organization is and what can be changed. Product thinking says whom it is for and how changing it is run. Both serve to place three scarce capacities, **attention, judgment and verification**, where the work needs them. A constraint is the step at which one of the three has run out, and a structure is right only for the constraint it was built around. Growth moves that constraint and, the book will argue, so does AI.

This introduction says who the book is for and how an executive and an individual contributor read it differently. It sets out the two disciplines and the three capacities, and introduces Corvane. It lays out the eleven parts in order, from foundations to AI. It gives a table that takes you from the decision in front of you to the chapters that answer it. And it explains the labels on the book's evidence and how its main sources are used.

## Who This Book Is For, and Two Ways to Read It

The book has two readers and is written for both at once. The first is the **executive**: a CTO, a CPO, a VP or a Director of Engineering or Product who has to define an organization, grow it or restructure it. The second is the **individual contributor**: an engineer, a product manager, a designer, a data or platform specialist and, with them, the engineering manager of a single team. This reader works inside an organization and wants to know why it is shaped the way it is.

I assume both of you know how software is built and shipped by teams: code review, on-call, roadmaps, quarterly plans. I do not assume you know the vocabulary of organization design. Terms such as *cognitive load*, *interaction mode* or *decision right* are defined in one plain clause the first time a chapter uses them, with a link to the chapter that owns the term, and the [[glossary]] collects them.

The two readers want different things from the same chapter. The executive has to act, so each chapter writes out the decision. The individual contributor wants to follow the reasoning, so it writes out the explanation as well. The table shows how to use a chapter either way.

| | Executive | Individual contributor |
| --- | --- | --- |
| The question you bring | What should I change, and what will it cost? | Why does my organization work this way, and could it work otherwise? |
| What you read for | The decision: the options and when each is right | The explanation: why sensible people behave as they do |
| Sections of a chapter that serve you most | The things to do and what they trade off, the take-aways and the checklist | The opening problem, the model with its terms, and the worked example |
| Where to start | The routing table on this page, from the decision in front of you | Part I in order, then the part about your own work |

Some subjects are left to other books. This one does not cover managing yourself as a leader, or the step-by-step practice of managing people: one-on-ones, feedback, writing reviews. It does not explain how to build a platform, or the technical architecture of systems built on AI. And it stays inside product and technology. I keep separate working records, checklists that each restate one source. They cover several of these subjects, and the section on the anchor books links to them.

## Two Disciplines: System Design and Product Thinking

Whichever of the two readers you are, the claim you have to weigh is the same, and it is clearest against the view it denies. A common view holds that organizations succeed or fail through their people and their culture, and that structure is a secondary, mostly political matter. I argue the opposite. **Most organizational failures are structural.** A boundary between teams sits in the wrong place. An **interface**, the agreed way in which work or information crosses from one team to another, has no owner. A decision is made far from the information it needs. Or a structure is kept after the constraint it was built for has moved. The reason is that people respond sensibly to the situation their place in the organization puts them in: Yves Morieux and Peter Tollman argue in *Six Simple Rules* that behavior in organizations is a rational response to goals, resources and constraints. The first chapter, [[the-organization-as-a-system]], makes the argument in full.

If failures are structural, the structure needs a description, and **system design** supplies one, in four elements. Teams are its components. The contracts and rituals between teams are its interfaces. Work, information and decisions are what flows through it. And three capacities that run out, which the next section defines, are its limits. System design also says what can be changed. A leader who redesigns an organization has four levers: where the **boundaries** between teams sit, what the **interfaces** are, who holds which **decision right** (who may decide a given kind of question, and whose input they need), and what the **incentives** reward. An org chart shows almost none of this.

System design says what to change. It does not say for whom, or how to go about it. **Product thinking** does. An organization has users: the people and teams who work in it, and the teams and customers who depend on each team. It owes them outcomes. So a change to it is run like a change to a product. Discover the problem before choosing the structure. State the outcome the change must move. Place the change on a roadmap toward a stated vision of the organization. Make the smallest change that tests the diagnosis. Then judge the change by its outcome. A reorganization that was carried out is only output. The second chapter, [[the-organization-as-a-product]], gives the method.

Neither discipline replaces the other: design the organization like a system, and run its design like a product. The table sets the two side by side.

| Discipline | The question it answers | What it gives you | The mistake it prevents |
| --- | --- | --- | --- |
| System design | What is the organization, and what in it can be changed? | Four elements to describe it and four levers to change it | Changing something that is not the cause |
| Product thinking | Whom is it for, and how is changing it run? | Users, discovery, a stated outcome, a roadmap and an outcome review | Shipping a change that nobody can judge |

Corvane's hiring wave made both mistakes. Seen with system design, it changed the number of people and almost nothing else. The plan was to grow to 95 engineers in eleven product teams and a platform team of five. The teams were formed in 2023 by dividing the people evenly, without asking what each team could own. Who decided that a feature was ready was left unsaid. Seen with product thinking, the change had no discovery before it and no stated outcome. When the board asked in 2024 whether it had worked, the leadership team could not answer, because nobody had said what "worked" would mean.

## Three Scarce Capacities: Attention, Judgment and Verification

The fourth element of the system-design description, the limits, needs more room, because the whole book is organized around it. Three capacities run out in an organization:

- **Attention** is how much a team can hold in mind well enough to change it safely. It runs out when a team owns more than it can understand.
- **Judgment** is deciding with the relevant information at hand. It runs out when the people who decide are far from the people who know.
- **Verification** is knowing that what was built is correct and was worth building. It runs out when checks pile up faster than anyone can make them.

With these three, the slowdown in the opening can be explained. In 2024 Corvane's VP of Engineering, Dario Vance, read the launch log. Of the 19 days of lead time, about two went into writing a change. The other seventeen went into waiting for a platform engineer to check by hand that the change could be released safely, and then to release it. Who decided that a feature was ready is a separate problem, and the changes did not queue for it. Five platform engineers did this for eleven teams: all eleven needed them for some launches, three for every launch. What had run out was verification. Every engineer Corvane hired wrote changes, so every hire lengthened the queue. The fix added nobody. The hand check was replaced by automated checks that a product team could run on its own change, and three quarters later the median lead time was under 7 days.

Corvane's case is one instance of a rule. A structure is built around whichever capacity is scarce at the time, and it is right for that constraint only. Growth moves the constraint. It does so at recognizable sizes, near 10, 50, 150, 500 and 1,000 people; the thresholds are rules of thumb. The structure built for the old constraint stays, and from then on it produces queues instead of relieving them. So every structure in this book comes with an **expiry signal**: the observation that tells you the structure has outlived the constraint it was built for.

Growth is one force that moves the constraint. The book argues that AI is a second, and that it acts at every size. The inherited rules for team size, people per manager and the rhythm of planning were derived when implementation was the scarce step: a team could build only as much as it could hold in mind, so attention was the limit. **Speculative.** If AI makes implementation cheap, the limit moves from attention toward judgment and verification: deciding what is worth building, and knowing that what was built is right. The rules then have to be derived again. *Speculative* is one of three labels on this book's claims about AI, explained under "How to Read the Evidence": reasoning about what may follow, not a measured result. It would be confirmed where teams report that review and decision queues, and no longer build time, set their pace. Part XI separates what has been measured from what is conjecture.

## Corvane, the Company the Book Follows

A structure that stays after its constraint has moved is easiest to see in one company over time. Corvane, met three times on this page, is that company. **Corvane is fictional.** It makes scheduling software for field-service companies. The book follows it from 12 people in 2018 to about 1,100 in 2028, in five stages, and the hiring wave is the third. Every figure about Corvane is an illustration, and the figures stay the same from chapter to chapter. Its own page, [[corvane-at-five-sizes]], gives the stages, the people and the named incidents.

## Eleven Parts in One Order

The claim, its terms and its company are now in place, and the book is laid out to argue that claim. It has three layers. A **preface** of four pages comes first: this introduction; a short account of how organizations came to have so many structures ([[how-organizations-got-complicated]]); a catalogue of twelve recurring failure patterns ([[where-product-and-tech-organizations-go-wrong]]); and Corvane's page. Then come **eleven parts** with forty-one chapters, each part opened by a short page of its own. A **reference** section closes the book: a [[toolkit]] that collects every chapter's checklist, the glossary and a [[bibliography]].

Each part supplies what the next one needs. Parts I to V build the design from small to large: the idea of a system, then one team and its neighbors, then the product and engineering **operating models** that run across teams (an operating model is the way a function decides and does its recurring work), then the leadership over all of them. Parts VI to IX are the four mechanisms that keep a design true: decisions and plans, talent systems, measurement and culture. Parts X and XI are the two forces that move the constraint, growth first, because its stages are the baseline that AI is compared against.

The eleven parts, each with the question it answers:

1. **Part I — Foundations** (chapters 1–5). What kind of thing is an organization, and what decides how well it works? A system with four levers and with users; software that mirrors its teams; how much one team can own; and the one constraint that limits output.
2. **Part II — Topology** (chapters 6–8). Which kinds of teams, working together how, and how large? Four team types, three ways for two teams to work together, and a team size that is derived, not copied.
3. **Part III — Product** (chapters 9–12). How does an organization decide what to build? Outcomes instead of output, a vision and a strategy, a roadmap that commits only as far as its evidence reaches, and teams that own the solutions.
4. **Part IV — Engineering** (chapters 13–17). How does it decide how to build, and keep the result changeable and reliable? Engineering strategy, governance with few mandates, platforms run as products, quality owned by the teams that ship, and technical debt retired by migrations.
5. **Part V — Leadership** (chapters 18–21). Who leads, and what is each layer for? Executive roles and reporting lines, how product, engineering and design decide together, managers and layers, and senior technical leaders.
6. **Part VI — Alignment** (chapters 22–24). How do many teams decide and plan so that their work adds up? Decision rights and their records, planning, and the recurring meetings and documents that carry information.
7. **Part VII — Talent** (chapters 25–27). How does it get, grow and keep the people the design needs? Career ladders, hiring and onboarding, and performance: the systems that set the incentives.
8. **Part VIII — Health** (chapters 28–29). How does a leader know whether the organization is working? Measuring engineering, product outcomes and early signals of organizational trouble.
9. **Part IX — Culture** (chapters 30–31). What is culture in a designed organization? Values as decision rules, rituals as recurring interfaces, and the trust every interface depends on.
10. **Part X — Evolution** (chapters 32–34). How must the design change as the organization grows or is shocked? What breaks at each size, when and how to reorganize, and what hypergrowth, a downturn or an acquisition does.
11. **Part XI — AI** (chapters 35–41). What does AI change, and how sure can anyone be? Where the constraint moves, team shape and roles, delivery with coding agents, governance, hiring, measurement, and a closing ledger that tests the assumptions of Parts I to X again.

Every chapter has the same shape. It opens with the problem, shown at Corvane. It gives the model, with its terms defined. It gives patterns, which are things to do, each with its user and its outcome measure: who it is for and how you would know it worked. It says how the patterns fail and what they trade off, and works one example through at Corvane. In Parts I to X it then has a section called "What AI Changes Here". It ends with "What to Take Away", a checklist you can run, and its sources.

## Start From the Decision in Front of You

You do not have to read in order. If you have a decision to make, find it in the table and open the chapter in the second column first; it defines its own terms in passing. The third column names either that chapter's prerequisite, the earlier chapter that treats those terms in full and that you can go back to if you need it, or a chapter to read afterwards. A chapter shown in double square brackets is not published yet.

| The decision in front of you | Open first | Prerequisite or follow-up |
| --- | --- | --- |
| A hiring wave did not deliver. Should we add people? | [[flow-and-the-constraint]] | Then [[the-organization-as-a-product]] |
| Where should the boundary between two teams go? | [[cognitive-load-and-team-boundaries]] | Prerequisite: [[conways-law-and-the-inverse-conway-maneuver]] |
| Should we create a platform team? | [[team-types]], which decides whether a platform team is justified | Then [[platforms-and-developer-experience]], on how to run one and judge it |
| Two teams keep waiting on each other. | [[interaction-modes-and-team-apis]] | Prerequisite: [[team-types]] |
| How large should a team be, and how many managers do we need? | [[team-size-and-composition]] | Then [[spans-layers-and-managers-of-managers]] |
| Our roadmap is a list of features promised to customers. | [[outcomes-over-output]] | Then [[roadmaps-and-horizons]] |
| What may a product team decide for itself? | [[discovery-delivery-and-empowered-teams]] | Then [[decision-rights-and-decision-records]] |
| We need an engineering strategy, or we run too many technologies. | [[engineering-strategy]] | Then [[architecture-governance]] |
| Technical debt keeps growing, or a migration never finishes. | [[migrations-and-technical-debt]] | Then [[planning]] |
| Who should report to whom at the top: CTO, CPO, VP Engineering? | [[executive-roles-and-reporting-lines]] | Then [[the-product-engineering-design-triad]] |
| Planning takes too long, and teams still collide. | [[planning]] | Prerequisite: [[decision-rights-and-decision-records]]; then [[operating-cadence]] |
| Promotions reward the wrong work, or we need a career ladder. | [[career-ladders-and-leveling]] | Then [[performance-calibration-and-growing-managers]] |
| What should we measure, and what belongs on the dashboard? | [[measuring-engineering]] | Then [[product-outcomes-and-organizational-health-signals]] |
| Should we reorganize, and how? | [[reorganizations]] | Prerequisites: [[the-organization-as-a-product]] and [[scaling-stages]] |
| What does AI change about team size, roles and hiring? | [[where-the-constraint-moves]] | Then [[team-shape-and-roles-with-ai]] and [[the-assumptions-ledger]] |

If your decision is not in the table, name which of the four levers it concerns. Is it about where a boundary sits, about an interface between teams, about who holds a decision, or about what gets rewarded? Then start from [[where-product-and-tech-organizations-go-wrong]]. That page sorts twelve recurring failures into four families, one for each lever, and names the chapters that address each failure.

## How to Read the Evidence

The table tells you where to look; the next question is how far to trust what you find there. Writing about organizations mixes research, borrowed models, stories and opinion, often without saying which is which. This book keeps six kinds of statement apart, and the wording of a sentence tells you which kind it is. Where the evidence runs out, the text says so. Apart from marked illustrations such as Corvane, it contains no invented statistics, quotations or company cases.

| Kind | What it is | How you recognize it |
| --- | --- | --- |
| Source | A model or an argument from a book or paper | The author, the title and the concept are named: "Larson's four team states, in *An Elegant Puzzle*" |
| Research finding | A result from a study or a survey | The year and what was measured are given |
| Documented practice | What a named company has published about itself | The company and the year are given, and nothing about its internals is inferred |
| Author's experience | What I have seen in my own work | It is marked as my observation, and no employer is named |
| Recommendation | My view of what to do | First person, with the reasoning and the conditions under which it does not hold |
| Illustration | An invented example | Corvane, or any number that is said to be an illustration |

Three sentences about one subject show why the difference matters. "Will Larson's rule of thumb in *An Elegant Puzzle* is six to eight engineers per manager" is a source: you can look it up, and it is that author's rule of thumb, not a law. "I recommend deriving team size from what the team owns and operates, and not copying the number" is a recommendation: it is mine, and you should ask for my reasons. "Corvane formed eleven product teams of about eight" is an illustration: it shows what an idea looks like and proves nothing. The three deserve different weight.

Claims about what AI changes get a second set of labels, because here the evidence is youngest and changes fastest. Each such claim, and only such a claim, starts with one of three words in bold:

- **Proven** means measured and published. The claim cites the study or the report.
- **Emerging** means practiced by some organizations and reported by them, or observed by me and marked so.
- **Speculative** means reasoning about what may follow. The claim says what would confirm it. The claim made earlier on this page, that AI moves the constraint toward judgment and verification, is the example.

A third set appears at the end of each chapter, under "What to Take Away", and is easy to confuse with the AI labels. It sorts the chapter's conclusions into three tiers. **Established** is what the sources agree on. **Depends on context** is what changes with your situation, and the chapter says on what. **The author's synthesis** is this book's own position. The three sets do different jobs. The six kinds classify a single sentence, the AI labels grade how sure anyone can be of one claim about AI, and the tiers tell you how far a chapter's conclusions travel: everywhere, under stated conditions, or as far as you accept my argument.

All of this holds as of a date. Anything that can change, above all a statement about AI, is dated in the text, for example "as of November 2026". This is a living book: I revise it as I learn more, and it is written with AI assistance under my direction, so the structure, the arguments and the errors are mine.

## How the Anchor Books Are Used

Three books carry most of the book's sources. I call them **anchors**: an anchor is the book a chapter starts from. The chapter names the anchor's concept and says where this book goes further or disagrees. For engineering and organization the anchors are two books by Will Larson. *An Elegant Puzzle* anchors the chapters on team size, the states a team can be in, migrations, reorganizations and careers. *The Engineering Executive's Primer* anchors those on engineering strategy, planning, measurement, values and executive roles. For product the anchor is *Build What Matters* by Ben Foster and Rajesh Nerlikar: a product vision, key outcomes, product strategy and the balanced roadmap. Applying that product model to the organization itself, as the second discipline does, is my extension and not theirs.

Two more books carry specific subjects. *Team Topologies* by Matthew Skelton and Manuel Pais supplies the team types, the ways teams interact, and cognitive load as the measure of what a team can own. My own *Grounded Architecture* supplies the approach to technical governance: nudges first, then charging a divergent choice the cost it puts on others, and mandates last. Other sources are named in the chapters that use them, and the bibliography collects them all.

The anchors were written apart: Larson's about engineering, Foster and Nerlikar's about product. On three subjects both have something to say, and they do not say the same. On each I state the tension and take a position.

| Where they meet | Larson | *Build What Matters* | This book's position, and where |
| --- | --- | --- | --- |
| Planning | Budget first, then the allocation of capacity, then the roadmap | Vision first, then strategy, then the roadmap | Larson's model sets how much capacity goes where, and *Build What Matters* sets what it is for; team objectives are the contract between the two ([[planning]]) |
| Decision rights | How decisions are made and recorded: by policy, by consensus or by conviction | Direction is set by a vision from the top | Leaders decide which problems matter and in what order, and teams decide the solutions ([[discovery-delivery-and-empowered-teams]], [[decision-rights-and-decision-records]]) |
| Metrics | Engineering is measured for several purposes, each with its own measures | Progress is measured by key customer and business outcomes | Delivery measures describe the flow, outcome measures say whether it was worth it, and neither rates a person ([[measuring-engineering]], [[product-outcomes-and-organizational-health-signals]]) |

The working detail behind these sources lives in my own working records, each of which restates one source at a time as checklists: [Grounded Engineering Executive](../grounded-engineering-executive/index.html), [Grounded Engineering Management](../grounded-engineering-management/index.html), [Grounded Product Management](../grounded-product-management/index.html), [Grounded Platforms](../grounded-platforms/index.html), [Grounded People Management Tools](../grounded-people-management-tools/index.html) and the [org-design decision records](../org-design/index.html). This book does what those records do not: it connects the sources, shows where they conflict and takes a position. A chapter links to a record for a checklist the book does not repeat, and the records cover several of the subjects this book leaves out.

## Where to Go Next

Everything on this page comes down to one habit. Before you change an organization, ask which capacity is scarce and for whom the change is made. The parts apply that question to one subject after another, and the labels keep the answers honest. Corvane's leaders asked how many engineers to hire, when the useful question was what had run out. The book ends with the same company in 2028, asking whether to hire engineers at all, and it answers with the same question. With that habit, your next hiring plan or reorganization starts with what is scarce and with how you would know that the change worked.

From here there are two ways on. If you have a decision in hand, go back to the routing table and open the chapter it names. If you do not, read on in order.

In order, the next page goes back to the beginning before the book takes the system apart. This introduction claimed that an organization is a designed system with three scarce capacities. Nobody designed that system in one sitting. It started as a few people at one table, and it came to have so many parts one at a time, each structure added when a limit was reached: [[how-organizations-got-complicated]].

## Sources and Evidence

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. Anchor for team size, team states, migrations, reorganizations and careers; the rule of thumb of six to eight engineers per manager is used here as the example of a sourced claim.
- *The Engineering Executive's Primer*, Will Larson, 2024. Anchor for engineering strategy, planning, measurement, values and executive roles.
- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. Anchor for the product chapters; its application to the organization itself is the author's extension.
- *Team Topologies*, Matthew Skelton and Manuel Pais, 2019; second edition 2025. Team types, interaction modes and cognitive load.
- *Grounded Architecture*, Željko Obrenović, [grounded-architecture.io](https://grounded-architecture.io). Technical governance by nudges, taxes and mandates.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. Behavior as a rational response to goals, resources and constraints; used in [[the-organization-as-a-system]].

**Practitioner sources**

- The author's working records, linked under "How the Anchor Books Are Used": the Grounded journals and the org-design decision records.
- The claim that AI moves the constraint is labeled Speculative on this page; the evidence for and against it is weighed in [[where-the-constraint-moves]].

This book is written with AI assistance (Claude Code) under the author's direction; see [how this works](https://zeljkoobrenovic.github.io/book-factory/foundations/ai-mediated-authoring.html). Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
