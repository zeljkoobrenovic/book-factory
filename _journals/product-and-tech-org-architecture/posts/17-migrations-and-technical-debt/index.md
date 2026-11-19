---
title: "Migrations and Technical Debt"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How does an organization retire technical debt at scale without stopping delivery? By migrations that are derisked, enabled and finished, with capacity reserved for them in planning and only a few in flight. A migration that is not finished has added debt."
permalink: migrations-and-technical-debt
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to run a migration in three phases with an owner and an end, count the unfinished ones in your landscape, and argue for the capacity to finish them.

> **KEY POINTS:**
>
> * **Shared debt is retired by migrations.** Debt in what many teams use cannot be repaid from one team's backlog. A migration moves every team: derisk it on the hardest cases, enable the rest with tooling, and finish by moving the last teams and switching the old system off.
> * **The finish decides the return.** The costs come while a migration runs and the benefit only when the old way is gone, so a half-finished migration has added debt.
> * **Delivery continues when migrations are funded and few.** Reserve a fixed share of capacity in planning, limit the number in flight, and give each migration an owner accountable for the last team.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Overloaded Team** — every unfinished migration leaves one more system for the same team to keep running.
> * **The Output Scoreboard** — a migration judged by its launch, or by tickets closed, is never judged by whether the old system is gone.
> * **The Platform Nobody Asked For** — a new way that was not tried on the hardest teams has to be pushed onto all of them.

<br>

In 2024 Corvane, the fictional company this book follows, replaced the way its eleven product teams released software. Corvane makes scheduling software for field-service companies and had 180 people then. Three quarters after the first team tried the new release path, all eleven teams were on it and the old way, a request to the platform team for each launch, was closed. Two years later Corvane had about 500 people in about thirty teams. Those teams ran four ways of deploying, three **message brokers** (the software that carries messages between services) and two **identity libraries** (the shared code that checks who a user is). Since 2024 nothing had been switched off.

You have probably lived with a move like the later ones: announced long ago, both systems still running, and the people who began it working on something else. This chapter's claim, which follows Will Larson's argument in *An Elegant Puzzle*, is that an organization retires technical debt at scale by **migrations**, each run in three phases: derisk it on the hardest cases, enable the rest with tooling that makes moving cheap, and finish it by moving the last teams and switching the old system off. A fixed share of capacity is reserved for migrations in planning and the number in flight is limited, so that delivery continues. Without the last phase the organization runs two systems and has added debt. The earlier chapters of this part described strategy, governance, platform and practice as they should be, and a migration is how a landscape that is not yet like that gets there. The chapter starts with Corvane's finished migration and its three open areas. It explains why shared debt needs a migration and why a half-finished one is worse than none. Three patterns follow: the three phases, reserved capacity with a limit on migrations in flight, and a count that ends in a decision for each unfinished migration. Then come the anti-patterns, Corvane's count, what AI changes, and Part IV read as one loop.

## Setting the Scene: One Migration Finished, Three Areas Left Open

The move of 2024 began with a diagnosis. Dario Vance, Corvane's VP Engineering, had found that a change spent about 17 of its 19 days of **lead time**, the time from starting work on it to its release, waiting for a launch slot at the platform team. A launch slot was a platform engineer checking a change by hand and releasing it. Lena Brandt, who led the platform team, piloted a release path that a product team runs itself. All eleven teams needed the platform team for some launches, and three needed it for every launch. Scheduling, the pilot team, was one of the three. After one quarter Scheduling's median lead time was 6 days. The other ten teams moved over the following two quarters, each with a platform engineer beside it for up to six weeks. When the eleventh team had moved, the launch-request form was closed, and the company's median lead time was under 7 days.

Then Corvane grew. In 2025 and 2026 it formed about nineteen new teams, and nothing told a new team to use the release path. The new teams brought three other ways of deploying, mostly scripts copied or written in a team's first weeks. Messaging spread the same way: there were three brokers, and the oldest, still used by two teams, had never been retired. A second identity library appeared beside the first. In all three areas every way stayed in use, and nobody had the job of moving any team off them. That changed in the middle of 2026, when Corvane wrote its first engineering strategy, with a rule of one standard per shared area, and made the platform team the owner of the move to the release path.

By 2026 this open state had a price that Corvane could measure. In the first half of the year the eleven teams on the release path had a **change failure rate**, the share of releases that need a fix or a return to the previous version right away, of 6 percent. The nineteen newer teams had 21 percent. The platform team, now eight engineers, supported one of the four ways of deploying. By the end of the year seven of the nineteen had moved to the release path, and twelve still released in the three other ways. Messaging would get worse before it got better: a new broker was approved in 2026 as Corvane's one standard, which meant four brokers, the three older ones and the new one, until the oldest was switched off.

## Why Shared Debt Needs a Migration

The cost Corvane was paying has a name, and no team's own effort was going to remove it. **Technical debt** is the cost of past choices that now slow change. It comes in two kinds, and the distinction, which is my wording, decides who can repay it. **Local debt** sits inside one team's own services: a tangled module, a missing test. The common view that each team pays its debt down from its own backlog, or in a periodic clean-up sprint, is right about this kind, and Martin Fowler's *Refactoring* is the widely known book on that work. **Shared debt** sits in what many teams use: a way of deploying, a broker, a library. No single team's backlog reaches it, because repaying it means that every team on the old way has to move.

For shared debt, Will Larson gives the argument this chapter follows. In *An Elegant Puzzle* he titles the passage "Migrations: the sole scalable fix to tech debt". Most tools and processes, by his rule of thumb, support about one order of magnitude of growth before they stop being effective, so a growing company keeps having to replace them. By then the cheap repairs have been made, and what remains needs many teams working together. "Migrations matter because they are usually the only available avenue to make meaningful progress on technical debt."

That argument needs the term in one fixed sense. In this book a **migration** is the move of every user of a shared system from an old way to a new one, and it ends when the old way is **switched off**: no team uses it, and nobody has to run it, secure it or know it. This is wider than a data migration, a change to the structure of a database, which is one technical step such a move may contain. A migration in the book's sense is a trade. Larson describes it as reduced contribution today in exchange for more capacity tomorrow. The teams that move ship less while they move.

## Why a Half-Finished Migration Is Worse Than None

The capacity comes back only at the end. Before a migration the organization runs one system, during it two, and after the switch-off one again, so every benefit that comes from retiring the old system arrives with the switch-off. The table, which is my arrangement, sets the three states side by side.

| | Before | During | After the switch-off |
| --- | --- | --- | --- |
| Systems to run and secure | The old one | Both | The new one |
| What an engineer who changes teams must learn | One way | Two ways | One way |
| Where a fix or a new check is applied | Once | Twice | Once |
| What the teams have paid | Nothing | Most of the cost of moving | All of it |
| What the organization has gained | Nothing | What each moved team gains for itself | The whole cost of running the old system, saved |

The middle column is the expensive one, so a migration that stalls there has added debt. The organization has paid most of the cost and keeps two systems. My record of Larson's chapter, [[systems-and-tools]], calls the result the 80 percent migration graveyard: migrations launched and then left, with both systems running for good. Camille Fournier and Ian Nowland describe the same end from the platform's side in *Platform Engineering*, which my record [[rearchitecting-platforms]] summarizes: a separate second version that never absorbs the old system leaves two platforms to operate. Nobody at Corvane had called the spread of 2025 and 2026 a migration, but the state was the middle column all the same: several systems doing one job, with three other ways of deploying beside the release path.

If a stalled migration only adds debt, a decision is worth nothing until its migration is finished. A decision about a shared system, such as a rule that names one standard broker, changes nothing in the landscape by being made. It reaches the landscape only when the teams have moved and the old way is off. So an organization's ability to finish migrations sets how fast it can change its own decisions. That step is my reading. Larson's own statement is that there are "two managerial skills that have a disproportionate impact on your organization's success: making technical migrations cheap, and running clean reorganizations." The second skill, the reorganization as a migration of people, belongs to [[reorganizations]]. Designing systems so that such moves stay cheap is the subject of the widely known *Building Evolutionary Architectures*.

## Pattern: Derisk, Enable, Finish

If the finish decides the return, a migration should be run in a way that is built to reach the finish. Larson's answer is short: "there is a pretty standard playbook that works remarkably well: de-risk, enable, then finish." The pattern's users are the teams that have to move. Its outcome measure is the old system switched off by the planned date.

---begin mermaid---
flowchart LR
    A["Derisk: does the new way work for the hardest teams?"] -->|"yes"| B["Enable: is moving cheap for the rest?"]
    B -->|"yes"| C["Finish: stop new use, move the last teams"]
    C --> D["Old system switched off"]
    A -->|"no"| E["Change the design, or stop"]
    B -->|"not yet"| F["Build tooling before asking more teams"]
    F --> B
---end mermaid---

**Figure 1:** *A migration passes three phases toward one end state, the old system switched off; the only other honest exit is to stop early.*

**Derisk** comes first, and Larson wants it done as quickly and cheaply as possible. The risk is that the new way does not fit the teams whose situation is least typical, and that this is discovered after everyone else has moved. So the design is tried where it is most likely to break. "Don't start with the easiest migrations, which can lead to a false sense of security." My checklist of his chapter adds working inside one or two of the hardest teams. Corvane's pilot of 2024 did this. Scheduling depended on the platform team for every launch, a platform engineer worked inside the team for six weeks, and the pilot had a stated way to fail: lead time still above 10 days after a quarter.

**Enable** comes second, and it makes the move cheap for every other team. Larson's advice is to slow down and build tooling that migrates "the easy 90 percent" programmatically, and to give teams self-service tools and documentation. "The best migration tools are incremental and reversible", so that a team can move one service at a time and step back when a move fails. The measure of this phase is the effort one team needs to move. At Corvane the hand check became a set of automated readiness checks that a team runs on its own change, and each joining team got one platform engineer for at most six weeks.

**Finish** comes third, and it is the phase that gets skipped. Larson defines it as deprecating the old system, which requires 100 percent adoption. It starts with what he calls stopping the bleeding: all new work uses the new way. Next, the status of the migration is pushed to the teams that still have to move and to their managers. For the last cases his instruction is "Your tool now is: finish it yourself." Corvane finished the moves of 2024: two quarters after the pilot began four teams were still off the path, they moved in the next quarter, and the form was closed. It did not keep the bleeding stopped, because nothing told the nineteen later teams to use the path.

The finish also needs someone whose job it is, and this is the part I add to Larson's phases. Every migration has one **owner**: a team, normally the team that owns the new system, that is accountable for the last team moved and for the switch-off, and not for the launch. My checklist of Larson's chapter reserves recognition for completion. An organization that celebrates the launch is keeping The Output Scoreboard, this book's name for judging work by what was shipped and not by what changed. The user of this rule is the executive who sponsors a migration. Its outcome measure is that every open migration has a named owner and an end date.

## Pattern: Reserve Capacity and Limit Migrations in Flight

Phases and an owner still need capacity, and a migration has two bills. The owning team pays the first, for the design, the tooling and the last moves. The teams that move pay the second, in weeks of their own work. Fournier and Nowland, as my record [[rearchitecting-platforms]] summarizes them, hold that migration is usually the largest cost of rebuilding a platform and that the consuming teams pay it. They ask for it to be counted before anyone commits, including the cost of running old and new together.

The second bill is paid from a fixed share of capacity reserved in planning. The reason is in Larson's four team states, which [[flow-and-the-constraint]] sets out: a team is falling behind, treading water, repaying debt or innovating, and each state has its own remedy. "When the team is repaying debt, the system fix is to add time." Reserving a share in the plan is my way of adding that time before the quarter starts. Corvane did this for one team in 2024, when the Identity team, halfway through replacing its permission model, got two more quarters without new roadmap commitments. Corvane's engineering strategy of 2026 did it for every team: the **operation share** of each product group's roadmap, the quarter of capacity kept for running and improving what exists, goes first to bringing each shared area down to one standard. How large the share should be, and how it is set beside budget and roadmap, is the subject of [[planning]].

The share is protected by a limit on **migrations in flight**, the migrations that are asking teams to move now. Without a limit the share is spread across many moves and none of them reaches its finish. Larson's remedy for a team that is treading water is to finish more things and reduce concurrent work, and applying it to an organization's migrations is my extension. I use three rules. No team is asked to move by two migrations in the same quarter. An owner finishes one migration before it starts the next. And the migration that can be switched off soonest goes first, because the benefit arrives at the switch-off. These rules are also what lets delivery continue: each team knows the size of its migration work, and the rest of its quarter is its own. The users are the product teams and their directors. The measures are the number of migrations in flight and the part of the reserved share spent on them. The one exception is a security fault, which can force a move outside the limit.

## Pattern: Count the Unfinished, Then Finish, Reverse or Wait

A limit presumes that you know how many migrations are in flight, and most organizations have more than they have announced. Count them by what is still running. For each shared area, list every system that is meant to go, the teams still on it, the owner of the move and its end date. Each such system is one open migration, whether or not anyone called it a project. A row without an owner or a date is a finding in itself. Counting this way is my recommendation: an open cost becomes a number that can be tracked. The user is the VP Engineering or the director who plans capacity. The outcome measure is the number of systems still waiting to be switched off, quarter by quarter.

Each stalled migration on the list stopped for a reason, and the reason is the phase it skipped. Hard teams that cannot move point to derisking, teams that can move only at a cost of weeks point to enabling, and a remainder left to itself points to a finish nobody owned. The mapping of what you see to Larson's phases is mine.

| What you see | Phase skipped | What to do |
| --- | --- | --- |
| The easy teams moved, and the hard ones found that the new way does not fit them | Derisk | Go back to the hardest team; change the design, or stop |
| Every team can move, but each move takes weeks and waits for help | Enable | Build the tooling and the documentation before asking anyone else |
| Most teams moved, the rest were left to move themselves, the owner has other work, and new work still lands on the old way | Finish | Name an owner, stop new use of the old way, move the rest, set the switch-off date |

With the phase known, each open migration gets one of three decisions: finish it, reverse it or wait. Reversing is a legitimate end. My record [[systems-and-tools]] puts it as "Killing a bad one early is also finishing", and Fournier and Nowland build a yearly review with an option to stop into every platform rebuild. The only wrong answer is to keep running both systems with no decision.

| Decision | When it is right | What it means |
| --- | --- | --- |
| Finish | The new way works on the hard cases, and the remaining moves cost less than keeping two systems | The owner moves the rest and switches the old system off |
| Reverse | The new way never passed the hard cases, or few teams have moved and moving them off again is cheaper | The teams that moved come off the new system, and the new system is switched off |
| Wait | The move is worth doing, but the limit on migrations in flight is reached | New use of the old way stops now, and the move starts when another one ends |

## Anti-Patterns: The Graveyard, the Clean-Up Sprint and the Announcement

Migrations fail in three recognizable ways, and each one lacks something the three patterns supply. The names in the last column are this book's failure patterns.

| Anti-pattern | What you see | What is missing | Failure pattern |
| --- | --- | --- | --- |
| The 80 percent graveyard | Migrations launched with an announcement and left when the interesting work ends | An owned finish | The Overloaded Team: one team keeps every old and new system running |
| The clean-up sprint | Every team spends a week on its own debt, and the shared systems are as they were | A migration, because shared debt is in no team's backlog | The Output Scoreboard: debt work is counted in tickets closed |
| The migration by announcement | A date and a rule that every team must move, with no tooling and no owner | Derisking and enabling | The Platform Nobody Asked For: a new way that has to be pushed |

## Worked Example: Corvane Counts Its Migrations

Corvane's landscape can now be counted. At the end of 2026, with about 500 people and about thirty teams, Lena Brandt, by then Director of Platform, and Dario Vance listed every system at Corvane that was meant to go, with its teams, the owner of the move and its end date.

| Shared area | System to be switched off | Teams on it | Owner of the move | End date |
| --- | --- | --- | --- | --- |
| Deploying | Copied deployment scripts | 7 | Platform team, since mid-2026 | None |
| Deploying | The group pipeline, a hosted pipeline that one product group began moving its teams to in 2025 | 3 | Platform team, since mid-2026 | None |
| Deploying | Hand-written scripts | 2 | Platform team, since mid-2026 | None |
| Messaging | The oldest broker | 2 | Platform team | In the decision record |
| Messaging | The two other older brokers | Not counted | Platform team | Each has a date, after the oldest |
| Identity | The second identity library | 5 | None; each team is to move itself | A date, set by a company rule |

Read against one question, whether the finish is owned and dated, the list showed how little was. Two rows of six, both in messaging, had an owner and an end date. The platform team of eight engineers was the owner in five rows, so one owner held most of the list. The group pipeline was a stalled migration inside the list: its product group had meant to move all its teams onto it, three moved, the engineer who led the move changed groups, and its finish was never owned. The identity row was a migration by announcement, a date with no tooling and nobody accountable for the last team.

The decisions went into the plan for 2027. The platform team finishes one migration before it starts the next, and no product team is moved twice in one quarter. The oldest broker comes first: its two teams and its switch-off date are in the decision record. The group pipeline comes second, and it is reversed: its target is given up, its three teams move to the release path, and the pipeline is switched off. These two come first because each can be switched off soonest. The hand-written scripts follow, and then the copied scripts, which have the most teams. The identity move gets an owner, the Identity team, which moves the five teams and removes the second library by the rule's date. The two other brokers wait for their dates, and the strategy's rule of one standard per shared area already stops new use of them. The moving teams' weeks come out of the operation share.

The plan has costs, and the list is what makes them visible. Each team that moved to the release path in 2026 shipped little for about six weeks, and the twelve teams still to move will each pay about the same. Corvane runs four brokers until the first switch-off date. The two brokers that wait remain a cost, held on the list where it can be seen. No results of the 2027 plan are claimed here.

## What AI Changes Here

The largest cost in Corvane's plan is the weeks of the teams that move, and that is the cost coding agents may change. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** Coding agents are being used for the mechanical part of migrations, Larson's "easy 90 percent". In January 2025 engineers at Google published an experience report, "How is Google using AI for internal code migrations?", on applying large language models to code migrations inside the company. They report evidence that this reduces the time migrations need significantly and lowers the barriers to starting and completing migration programs. The authors say that it is an experience report and that they compare against no other approach, which is why the label here is Emerging and not Proven.

**Speculative.** If agents make moving cheap, the enable phase shrinks and the other two phases stay as they were. The hardest teams still have to be tried first, and someone still has to own the last team and the switch-off. Cheaper change also cuts the other way: a new way of doing something is cheaper to create, so systems that will later have to go can multiply faster than before. Later chapters follow Corvane into 2027 and 2028, at 1,100 people, where fourteen teams each choose their own coding agent, model provider and prompt conventions. Like everything about Corvane, that is an illustration. The Speculative claim above would be confirmed if organizations that use agents for migrations report shorter enable phases while the number of systems waiting to be switched off does not fall. [[agentic-delivery]] takes up what agents change in delivery as a whole.

## Part IV as One Loop

The migration is the last of the five elements of the engineering model that this part of the book has built, and with it the five close into one loop. A policy, a written rule that settles a recurring decision, decides ([[engineering-strategy]]). An instrument of governance, from advice to a mandate, applies the decision ([[architecture-governance]]). A platform makes the decided way the easy way ([[platforms-and-developer-experience]]). The teams' own checks keep it true in daily work ([[quality-and-reliability]]). And when the policy changes, a migration moves the rest of the landscape, which is why the ability to finish sets how fast a decision can change. What running that landscape teaches goes into the next policy.

---begin mermaid---
flowchart LR
    P["Policy decides"] --> I["Instrument applies it"]
    I --> F["Platform makes it the easy way"]
    F --> Q["Teams' checks keep it true"]
    Q --> M["Migration moves the rest of the landscape"]
    M -->|"what running it teaches"| P
---end mermaid---

**Figure 2:** *The five chapters of Part IV are one loop, and a landscape shows which pieces of the loop are missing.*

Corvane's landscape is that loop with pieces missing. Take its four ways of deploying. No policy told a new team which way to use. The release path of 2024 was not offered to the new teams as a **paved path**, a supported default that is easier to take than to avoid, in a form they could adopt in their first weeks. And three other ways were in use with nobody moving teams off them, which is three unfinished migrations. So the four ways of deploying are a missing policy, a missing paved path and three unfinished migrations. This part of the book opened with that landscape and said that each choice in it had been reasonable when it was made. That remains true: what was missing was every step that would have had the choice made once, for all teams.

## What to Take Away

**Established.** What the sources say:

- Migrations are usually the only way to make real progress on technical debt as a company and its code grow (Larson, *An Elegant Puzzle*).
- A migration runs in three phases, derisk, enable and finish, and the finish means 100 percent adoption and the old system retired (Larson).
- A team that is repaying debt needs time (Larson's four team states).
- The teams that move usually pay the larger part of a migration's cost, and it should be counted before anyone commits (Fournier and Nowland, *Platform Engineering*, as summarized in my record).

**Depends on context.** What changes with the situation:

- The size of the reserved share depends on how much shared debt you carry and on what your product strategy needs first.
- The limit on migrations in flight depends on how many teams each migration touches.
- Whether to finish or reverse depends on whether the new way passed the hard cases and on how far the move has gone.

**The author's synthesis.** What is this book's own position:

- The split into local and shared debt, and the claim that the ability to finish migrations sets how fast an organization can change its own decisions.
- One owner accountable for the last team, the limit on migrations in flight, the count by systems still to be switched off, and the diagnosis by the phase that was skipped.
- Part IV as one loop of policy, instrument, platform, checks and migration.

## Checklist

Shared debt is not repaid in place; the organization moves away from it. The phases, the owner, the reserved share, the limit and the count all serve one end, the old system switched off. That end also closes the loop of Part IV, because a changed policy reaches the landscape only through a finished migration. Run these eight checks.

- [ ] For each shared area, such as deploying, messaging and identity, list every system still in use.
- [ ] Mark each system that is meant to go with the teams on it, the owner of the move and an end date, and note what is missing.
- [ ] For each stalled move, name the phase that was skipped.
- [ ] Decide for each one: finish, reverse or wait. Record the decision.
- [ ] Check that new work cannot land on an old way.
- [ ] Count the migrations that ask teams to move this quarter, and set a limit.
- [ ] Find the share of capacity reserved for migrations in your plan, and what was spent on them last quarter.
- [ ] List the three technical decisions most often made differently across your teams, and for each write the policy, the instrument and the migration it implies.

Corvane's move of 2024 ended because it was tried on a hard team, made cheap for the rest and carried to the last team by its owner, and the later moves had no owner and no end. With this chapter the engineering model is complete, and it stands beside the product model of Part III: vision, strategy, roadmap and empowered teams on one side, and strategy, governance, platform, quality and migrations on the other. Wherever a product decision and an engineering decision have to be made together, somebody has to be placed to join them, and that is why the organization needs a leadership structure at each level. [[part-5]] derives that structure.

## Sources and Evidence

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. Migrations as the sole scalable fix to technical debt; the phases derisk, enable and finish; cheap migrations and clean reorganizations as two managerial skills; the four team states and the remedy for a team that is repaying debt. From the author's Kindle notes.
- *Platform Engineering: A Guide for Technical, Product, and People Leaders*, Camille Fournier and Ian Nowland, 2024. The cost of migration paid by the consuming teams, the separate second version that leaves two platforms to operate, and the yearly review with an option to stop; used through the author's record [[rearchitecting-platforms]].
- *Refactoring*, Martin Fowler, and *Building Evolutionary Architectures*, Neal Ford, Rebecca Parsons and Patrick Kua, are named as widely known titles on neighboring subjects. No claim in this chapter rests on them.

**Research and reports**

- "How is Google using AI for internal code migrations?", Stoyan Nikolov and others, arXiv 2501.06972, January 2025. An experience report on applying large language models to code migrations at one company, with no comparison against other approaches. It supplements the author's bookshelf; its abstract was read for this chapter.

**Practitioner sources**

- The author's working records: [[systems-and-tools]], with its checklist of Larson's migration chapter, and [[rearchitecting-platforms]].
- The statements under "What AI Changes Here" are labeled, and the Speculative one is the author's reasoning as of November 2026.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
