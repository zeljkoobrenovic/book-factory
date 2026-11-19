---
title: "Spans, Layers and Managers of Managers"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How many people should a manager lead, and how many layers of managers follow? As many people as the manager can know and develop, which gives the layers by arithmetic; each layer then has to earn its delay by joining decisions the teams below it cannot."
permalink: spans-layers-and-managers-of-managers
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to compute how many managers and layers an organization needs from its team sizes, and to say what each layer must decide to be worth its delay.

> **KEY POINTS:**
>
> * **A span is limited by attention.** A manager can lead as many people as they can know the work of and develop: one team for a line manager and, in Will Larson's rule of thumb, four to six managers for a manager of managers.
> * **Layers follow by arithmetic.** Divide the engineers by the team size and the managers by four to six; the number of layers that comes out can be compared with the chart you have.
> * **A layer must earn its delay.** Each layer adds a step of delay and of distance from information, so it is kept only if it joins decisions that the teams below it cannot join themselves.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Escalation Ladder** — a layer that only relays is one more level for every decision to climb.
> * **The Reorg as Strategy** — a layer added to give a person scope redraws the chart with no stated outcome.

<br>

In 2024 twelve engineering managers at Corvane reported to one person: Dario Vance, the VP Engineering. Corvane is the fictional company this book follows and had 180 people that year. Nobody had decided that the number should be twelve. In one month three requests for a new team reached Dario Vance, because there was nobody else to send them to. A year later Corvane put directors between him and the managers, and a year after that engineers were leaving one of its groups and naming slow decisions as the reason. If you have had a manager with too many reports to know your work, or worked under a level nobody could explain, you know both halves of this story.

Both halves are about numbers nobody derived. The previous chapter placed product, engineering and design together at every level of the organization; this one asks how many levels there are and how many people each manager leads. A **span** is the number of people who report to one manager, and a **layer** is one level of managers. **A manager should have as many people as they can know the work of and develop**: for the manager of a team that is the team, at the size [[team-size-and-composition]] derived, and for a manager of managers about four to six managers, in Will Larson's rule of thumb. The number of layers follows by arithmetic from headcount and those spans. Each layer adds a step of delay and of distance from information, so it is kept only if it joins decisions across the units below it that those units cannot join themselves. The chapter starts with Corvane's twelve, defines spans, computes layers and says what a layer costs and is for. Three patterns follow: deriving the layers, writing what each layer decides, and inspecting as a manager of managers. Then come the disagreement between the sources, two ways layers go wrong, Corvane's arithmetic at four sizes, and what AI may change.

## Setting the Scene: Twelve Managers and One VP

The twelve arose by growth. In 2021, at 50 people, Corvane had about 24 engineers in four teams and two engineering managers, each with two teams; both reported to Tomas Rell, co-founder and CTO. In 2023 the company formed eleven product teams and gave each an engineering manager. With the platform team, led by Lena Brandt, that made twelve managers. Dario Vance joined that year to run the engineering organization, and all twelve reported to him. The number of managers had a reason: one per team. The number of people those managers reported to had none, because nobody had asked the question.

What twelve meant showed in 2024. Dario Vance could answer what was brought to him, and he could not look at what lay between teams. The three requests of that one month each touched more than one team, so each came to the only person above them all. Meanwhile the platform team kept its five engineers while the engineers it served doubled, and the queue of launches waiting for it grew for about a year before anyone with authority over both sides examined it ([[flow-and-the-constraint]]). In 2025 Corvane appointed engineering directors. By 2026, at about 500 people, the people deciding were two or three levels from the information. One level too few had cost attention, and the added level cost time. So how many levels should there be, and what is each one for?

## Spans: How Many People One Manager Can Lead

Levels are computed from spans, so the span comes first. A span, or span of control, is the number of people who report directly to one manager. A **line manager** leads a team of people who do the work; in engineering this is the engineering manager. A **manager of managers** has managers as reports and is usually called a director. What limits a span is the manager's attention. Knowing someone's work well enough to judge it, and giving them feedback and room to grow, take time for each person, every week. This chapter counts the engineering line. Product managers and designers report in lines of their own ([[executive-roles-and-reporting-lines]]), and the same arithmetic applies to them.

For a line manager the span is one team, and its size is already settled. [[team-size-and-composition]] derived it from the team's scope, on-call rotation and coordination cost, and arrived at Will Larson's rule of thumb from *An Elegant Puzzle*: a manager supports six to eight engineers. Larson gives a reason for each end. With fewer than four engineers a manager tends to become a tech lead manager, who takes on design and implementation work; with more than eight or nine, a coach and safety net, too busy to invest in the team. The least of six for a team with a round-the-clock rotation was my judgement in that chapter, not Larson's. I take those sizes as given. Larson adds: "Never leave managers supporting more than eight individuals."

A manager of managers gets a smaller number. Larson's rule of thumb is "Managers-of-managers should support four to six managers", again with a reason at each end. With fewer than four, the manager should be in a period of active learning, about the problem domain or about the move from supporting engineers to supporting managers. At the other end, "supporting a large team of managers leaves you functioning purely as a problem-solving coach." Larson does not say why this range is lower. My reading is that each report now stands for a whole team, whose work the manager knows only at second hand.

A span outside its range can be recognized without the chart, from how the manager spends the week and from what stops happening. The table gives Larson's description of each case. The last column is my reading; the order in which things lapse under a line manager comes from my record [[engineering-management-operating-model]].

| Manager | Span | Larson's description | What you see |
| --- | --- | --- | --- |
| Line manager | Fewer than four engineers | Tech lead manager | The manager writes much of the design and code |
| Line manager | More than eight or nine | Coach and safety net | Feedback and career conversations stop first, then team health suffers, then delivery |
| Manager of managers | Fewer than four managers | Ramping up | Fine for a stated period; after it, the manager does the managers' jobs |
| Manager of managers | More than six | Problem-solving coach | The manager hears only what is brought; nothing between teams is looked at |

## Layers: The Arithmetic from Headcount to Levels

Given the spans, the layers follow. A layer is one level of managers in the reporting line: the line managers are the first, the managers they report to the second, and so on up to the person who runs the function. The number comes from dividing. Divide the engineers by the team size and you have the teams, each with one line manager. If more than six managers remain, they cannot all report to one person, so divide them by four to six to get a layer of managers of managers. Repeat until six or fewer are left. They report to one leader, who is the top layer.

---begin mermaid---
flowchart LR
    E["Engineers"] --> T["Teams: engineers divided by team size"]
    T --> M["Line managers: one per team"]
    M --> Q{"More than six managers at this level?"}
    Q -->|"yes"| A["Add a layer: divide them by four to six"]
    A --> Q
    Q -->|"no"| S["They report to one leader. Count the layers."]
---end mermaid---

**Figure 1:** *The number of layers is computed from headcount, team size and spans, before any name is placed in a box.*

Run on round numbers, the division adds a layer roughly every time an organization grows four- to sixfold. Larson states the dependence more roughly: "For every additional order of magnitude of engineers, you need to design and maintain a new layer of management." His own spans put the step earlier than a factor of ten, and I read the order of magnitude as the outer bound. The table does the division with the narrowest of his numbers and with the widest. The arithmetic is mine.

| Layers | Who is in them | Engineers, narrowest spans (teams of six, four managers each) | Engineers, widest spans (teams of eight, six managers each) |
| --- | --- | --- | --- |
| 1 | One line manager | 6 | 8 |
| 2 | Line managers and their manager | 24 | 48 |
| 3 | Line managers, directors, a head of engineering | 96 | 288 |
| 4 | One more level below the head | 384 | 1,728 |

The table is for comparing the layers an organization has with the layers its size gives, and there are two possible findings. A missing layer shows as a span above the range. Sixty engineers in eight teams, whose eight managers all report to one head, have two layers where the division gives three, and the head has eight reports where four to six is the rule. A surplus layer shows as spans below four that nobody is growing into. Forty engineers in five teams, with two directors and a VP above the five managers, have three layers where two would do, and spans of two and three.

## What a Layer Costs, and What It Is For

The arithmetic says how many layers the spans require and not what each one costs. There are three costs, and the first is delay. A decision that must pass through a layer waits there for one more person. A question between two teams in different groups goes, with two layers, to the two line managers and then to the one person above both. With three layers it goes to two line managers and two directors before the head decides. Yves Morieux and Peter Tollman, in *Six Simple Rules*, count among the benefits of removing layers "Less waste and fewer mistakes that result from escalating decisions."

The second cost is distance from information. Each layer passes a summary upward, and a summary leaves things out. This needs no bad faith. In *The Manager's Path*, Camille Fournier warns the manager of managers about reports who manage up well, to the detriment of the team under them. My record [[managing-managers]] concludes that every signal arrives filtered, and that a manager under pressure filters toward optimism. Morieux and Tollman state the cost from the other side: decisions should be made as close as possible to where the action takes place and where information is richest.

The third cost is salary, and it is the smallest. Larson makes it a step in planning an organization change: "Set target ratio of management to individual contributors." This **management ratio** sets the number of managers against the number of people who manage nobody, and the arithmetic, which is mine, shows where it comes from. With teams of seven and one layer there is one manager for every 7 engineers. Add directors with five managers each and it is one for every 5.8; add a third layer and it is one for every 5.6. The first layer is nearly the whole cost. Removing an upper layer saves little money, so the case for or against it rests on delay and distance.

What does a layer give for those costs? **A layer earns its place by joining decisions across the units below it that those units cannot join themselves.** Two teams can settle an interface between them. They cannot settle which of them gives up two engineers, whose work goes first when both need the same third team, or who should manage each of them. The nearest concept in my sources is Morieux and Tollman's **integrator**, a role with both an interest in making others cooperate and the power to make them. The test follows. List the decisions a layer made last quarter that involved more than one unit below it and that those units could not have settled themselves. A layer without such a list only relays: it passes requests down and status up.

## Pattern: Derive the Layers Before Drawing the Chart

The arithmetic and the test give three patterns, and the first is to derive the layers before drawing the chart. Its user is the executive who owns the reporting structure. Its outcome measures are the number of managers whose span is outside its range without a stated reason and an end date, and whether the layers equal the computed number. Larson's steps for planning an organization change put projecting headcount and setting the management ratio before identifying teams and groups, and the steps below keep that order. Names go into boxes only after the last one.

1. Project the headcount a year out, so that the chart fits the size it will have to carry.
2. Take the team sizes from [[team-size-and-composition]] and count the teams.
3. Give each team one line manager.
4. Run the division of Figure 1 on the managers, and count the layers.
5. Compare with the chart you have. For every span outside its range, write the reason and the date by which it ends.

The last step will often find a span that is too wide, and then there is a choice. My recommendation is width before depth: add a peer before adding a layer. Eight managers under one director can become two groups of four under two directors, and nothing gets deeper, provided the level above has room for one more report. A peer costs one more manager; a layer costs every decision that crosses it a step. The recommendation does not hold when the level above already has six, and then the division has found a missing layer.

## Pattern: Write What Each Layer Decides

The second pattern puts in writing the reason for each layer the arithmetic justified. Its users are every manager of managers and the leader they report to. Its outcome measures are the share of decisions between teams settled at the lowest layer that spans the teams involved, and the median days from question to decision. The instrument is one page per layer, like the page of who decides what between executives in [[executive-roles-and-reporting-lines]]. It is found by looking back: collect last quarter's decisions between teams and note the layer at which each was settled. A layer at which none was settled is a candidate for merging. [[decision-rights-and-decision-records]] covers decision rights in general. The rows below are my starting point and not a standard.

| Layer | Decides | Leaves to the layer below |
| --- | --- | --- |
| Line manager | Who works on what in the team; hiring and each person's growth; with the product manager, the team's quarter | How the work is done |
| Manager of managers | Moving scope and people between its teams; the order of work across them; who manages each team; a dispute between two of its teams | Anything inside one team |
| Head of engineering | The same between groups; standards shared by all groups; how many engineers each group gets | Anything inside one group |

## Pattern: Inspect What You No Longer See

A layer that decides what crosses teams needs a person who knows those teams well enough to decide, and that makes managing managers a different job from managing a team. A line manager learns about the work by being in the team. A manager of managers learns only by asking. Fournier is blunt about the step: "People who are good at managing a single team, or even a couple of related teams, fall apart when asked to manage managers, or teams that are outside of their skill set." Julie Zhuo, in *The Making of a Manager*, describes the same shift: as a team grows it matters less how good the manager is at the work, and more how much of a multiplier she is for others. Andrew Grove's *High Output Management* is on my bookshelf without notes, so I cite only my one-line description of it: maximizing an organization's output through delegation, clear communication and focused management.

The third pattern replaces what being in the team used to supply. Its user is a manager of managers. Its outcome measure is the number of problems that reached them by escalation, resignation or incident before their own inspection found them; my record [[managing-managers]] uses the same test. Inspection of this kind is support and not suspicion ([[inspected-trust]]). One item needs a definition: a **skip-level meeting** is a meeting with the people who report to your reports, without the manager in between. The pattern is a fixed set of things to look at.

- Each team's flow and health: how often it releases, its incident load, its lead time ([[managing-multiple-teams]]).
- Whether each team can state its goals and say why. Fournier asks this first when a team is not working.
- The small things: hiring, the quarter's goals, last week's postmortem. Fournier's rule is to follow up on all of them "until you figure out what you don't need to follow up on."
- Skip-level meetings, "perhaps once a quarter" with each person in Fournier's version, to hear what a summary leaves out.
- Each manager's one-on-ones and feedback, most closely for a new manager.

Looking is half of the job. What a manager of managers decides is what crosses teams: the middle row of the page above. What they must not do is take a team's problem back from its manager. Fournier gives three cases, a roadmap that keeps changing, a tech lead lost in a redesign and a team that only fights fires, and asks each time whether the manager is accountable. Her answer is yes each time, because the manager is "accountable for the health and productivity of the team." A manager of managers who steps in and runs the team has removed that accountability. The layer inspects and joins; it does not manage the teams a second time.

## Where the Sources Disagree: Add a Layer or Cut One

All three patterns assume that layers are needed, and one of my sources starts from the opposite end. Larson designs a new layer as the organization grows and keeps spans narrow enough for a manager to invest in each report. Morieux and Tollman begin by removing layers: "the first step in reinforcing your managers to play the integrator role is to cut the number of hierarchical layers, which simultaneously increases the span of control and shortens hierarchical lines." Taken alone, that is the delayering view: managers are overhead, and flatter is always better.

The two share more than they dispute. Both judge a layer by one test: its managers must be able to make others cooperate. They differ in where they start. Morieux and Tollman write against managerial layers that cannot add value; Larson writes for growing engineering organizations that have too few. Neither says that flatter is always better. That reading is mine, and so is the resolution: **the fewest layers that keep spans inside Larson's ranges, each with its decisions written down.** The first two patterns already do this: one derives the count, the other writes the page. The table sets out the choice.

| Choice | What you gain | What you give up | Right when |
| --- | --- | --- | --- |
| Wide and flat: spans above the range, one layer fewer | Short lines; decisions near the work | Managers who can only coach; nothing between teams is looked at | Managers are experienced, teams are stable and little crosses between them |
| Narrow and deep: spans below the range, one layer more | Time for each report | A step of delay and filtering for every decision | Briefly, while a new manager grows into a span |
| In range: the fewest layers with spans of four to six | Some of each | Some of each | The default |

## Anti-Patterns: The Relay Layer and the Layer Made for a Person

Two kinds of layer fail that test. The first is **the relay layer**. Its managers pass requests down and status up, and it has all three costs and none of the return. You can recognize it by where questions go: a dispute between two teams of the same group is settled above the group, and the group's director was a stop on the way. This book's name for decisions that travel upward to someone with less information is **The Escalation Ladder**, and a relay layer is one more rung on it.

The second is **the layer made for a person**. It exists to give a senior manager scope, or a title that keeps them, and it is the opposite habit to delayering. Fournier describes the leaders who ask for it as empire builders, who seek to grow their teams and mandates without concern for what is best for the organization. The signs are spans of two or three with no end date. [[executive-roles-and-reporting-lines]] gave a test for a role made to fit a person, and it works for a layer: remove the name and ask which decisions the role joins. A chart redrawn for this reason, with no stated outcome, is also the failure pattern this book calls **The Reorg as Strategy**.

## Worked Example: Corvane's Layers at Four Sizes

The arithmetic can now be run on Corvane at four sizes. Layers are counted up to the person who runs engineering: Tomas Rell in 2021 and Dario Vance from 2023, with Tomas Rell above him holding the technical direction and no part of the line ([[executive-roles-and-reporting-lines]]). The 2028 row is a projection that assumes 2026's proportion of teams to people; it gives notice of a fourth layer before any chart shows one.

| Year and size | Teams and line managers | Layers the arithmetic gives | Layers Corvane had | Widest span |
| --- | --- | --- | --- | --- |
| 2021: 50 people, about 24 engineers | Four teams, two managers | Two | Two: the managers and the CTO | About twelve engineers per manager |
| 2024: 180 people, 95 engineers | Twelve teams, twelve managers | Three, with two or three managers of managers | Two: the managers and the VP | Twelve managers under the VP |
| 2026: 500 people, 260 in product and tech | About thirty product teams and the platform team, a manager each | Three, with five to eight directors for the product teams | Three: the managers, four group directors and the Director of Platform, the VP | Seven or eight managers per group director |
| 2028: 1,100 people, 520 in product and tech | About sixty teams | Four, with ten to fifteen directors and two or three leaders above them | Not recorded beyond two business units | Not recorded |

The first two rows show two different errors. In 2021 the layer count was right and the spans were wrong: each engineering manager had two teams and about twelve engineers, well past Larson's eight or nine. In 2024 a whole layer was missing. Twelve managers need two or three managers of managers, and Corvane had none, so Dario Vance held a span twice the top of Larson's range. The symptoms in the scene are the ones the span table gives for a manager of managers above six. He heard what was brought to him, and nothing between teams was looked at, the platform team's size included.

The third row is the opposite case. In 2025 Corvane appointed an engineering director for each of its four product groups, and by 2026 it had the three layers the arithmetic gives. The top span was in range: Dario Vance had six reports. The directors' spans were not: each had seven or eight managers. And this was the year of the slow decisions. The count was right, so my reading is that no layer should be removed. What was missing was the page: nobody had written what a director decides alone. Late in 2026 Dario Vance and the directors wrote it. A director decides moves of scope and people between the group's teams, the order of work within the group's outcomes and who manages each team; what touches two groups goes to Dario Vance. No result is recorded yet. For the spans, width before depth applies: a fifth and sixth group when the product's boundaries allow, and not a fourth layer.

---begin mermaid---
flowchart TB
    V["Dario Vance, VP Engineering"] --> D["Four engineering directors, one per product group"]
    V --> P["Lena Brandt, Director of Platform"]
    V --> S["Security lead"]
    D --> M["Seven or eight engineering managers per director"]
    M --> T["About thirty product teams"]
    P --> PT["Platform team"]
---end mermaid---

**Figure 2:** *Corvane's engineering line in 2026 has the three layers the arithmetic gives, with six reports at the top and seven or eight under each group director.*

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The derivation has two inputs, team size and spans, and AI may move either. **Emerging.** As of November 2026, managers I have observed use AI tools to summarize status reports, pull requests and incident reviews, which makes part of their information gathering cheaper. This is my observation and not a measured result. It does not by itself widen a span, because gathering was never the limit. The limit is knowing the work well enough to judge it and developing each person, and both happen in conversation. I know of no published measurement of the span a manager can sustain with these tools, so this section makes no Proven claim.

The layer count is different: it may move through team size. **Speculative.** If teams settle at four or five engineers, the lower sizes of [[team-size-and-composition]], the same headcount means more teams, and so more line managers or managers who each lead two small teams. If teams keep their size and own more, the arithmetic does not change. A span held above Larson's ranges for years, with unchanged attrition and promotion rates, would confirm that the ranges themselves have moved. [[team-shape-and-roles-with-ai]] makes the full argument. This chapter claims only that the division is run again when one of its inputs changes.

## What to Take Away

**Established.** What the sources say:

- Larson's rules of thumb, each with a reason: six to eight engineers per manager, four to six managers per manager of managers, and a new layer as the organization grows (*An Elegant Puzzle*).
- Managing managers is a different job: information arrives filtered, skip-level meetings and follow-up replace what a line manager sees, and each manager stays accountable for the team (*The Manager's Path*).
- Managerial layers that cannot add value should be removed, and decisions belong where information is richest (*Six Simple Rules*).

**Depends on context.** What changes with the situation:

- Where in its range a span sits: it depends on the managers' experience, the stability of the teams and how much crosses between them.
- Whether a span that is too wide gets a peer or a layer: it depends on whether the level above has room.
- How closely a manager is inspected: a new manager closely, an experienced one less.

**The author's synthesis.** What is this book's own position:

- The arithmetic of layers and of the management ratio, and the finding that salary is the least of a layer's three costs.
- The test of a layer by the decisions it joins, the page per layer, and width before depth.
- The reading that Larson and Morieux and Tollman agree on the test, with the fewest layers the spans allow as the resolution.

## Checklist

Spans and layers are one calculation with two prices. With a layer too few, somebody has twelve reports and looks at nothing between teams; with a layer too many, every decision waits a step for someone who knows less. The count the arithmetic gives is therefore both the least an organization needs and the most it should tolerate. Compute it, compare it with your chart, and write for each layer the decisions it makes that the layer below cannot.

- [ ] Count your engineers, your teams and the layers of managers between an engineer and the head of engineering.
- [ ] Run the division: teams, line managers, then four to six per manager of managers. How many layers does it give, and how many do you have?
- [ ] List every manager whose span is outside its range. Does each have a reason and an end date?
- [ ] For each layer, write the decisions it made last quarter that involved more than one unit below it.
- [ ] Which decisions between two teams were settled above the lowest manager who spans both?
- [ ] For each manager of managers: which problems reached them by escalation, resignation or incident first?
- [ ] Before adding a layer, ask whether a peer would do. Before removing one, ask who will join its decisions.

In 2024 twelve managers reported to Dario Vance, and nobody had chosen the number. You can now say what it was: a missing layer, by Larson's four to six. The layer added in 2025 was the right count with its decisions unwritten. Everything in this chapter followed the reporting line: who reports to whom, and what each level decides for the levels below. Some decisions do not follow that line. The choice of a message broker, or the design of an interface between two groups, cuts across teams that share no manager below the top. Those decisions belong to a second track of leaders, staff engineers and architects, who work across the reporting structure and not along it: [[staff-plus-and-architects]].

## Sources and Evidence

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. The rules of thumb and their reasons: six to eight engineers per manager, four to six managers per manager of managers, ramping up and coaches, a new layer of management per order of magnitude of engineers, and the management ratio as a step in planning an organization change.
- *The Manager's Path*, Camille Fournier, 2017. Managing managers as a different job: follow-up, skip-level meetings and their purpose, managing up, the manager's accountability for the team, empire builders.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. Integrators, cutting layers as the first step in reinforcing them, removing positions without power, and decisions where information is richest.
- *The Making of a Manager*, Julie Zhuo, 2019. The manager as a multiplier as the team grows.
- *High Output Management*, Andrew Grove. On the author's bookshelf without notes; mentioned only by its description there.

**Research and reports**

- None. The chapter cites no study; the arithmetic of layers and of the management ratio is the author's.

**Practitioner sources**

- The author's working summaries: [[managing-managers]] and [[managing-multiple-teams]] (Fournier's two chapters), [[managing-a-growing-team]] (Zhuo), [[senior-leadership]], [[organizational-design]] (Larson's sizing rules), [[inspected-trust]] and [[engineering-management-operating-model]] (span guardrails).
- The statements about AI under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
