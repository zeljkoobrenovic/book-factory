---
title: "Vision and Product Strategy"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How does a product vision become a strategy that teams can act on? By being written as the customer's future journey, and by a strategy that works backward from it in a few ordered steps, each with a milestone and a statement of what will not be done."
permalink: vision-and-product-strategy
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to tell a vision from a feature list, write one as a customer's future journey, and work backward from it to a strategy.

> **KEY POINTS:**
>
> * **A vision is a description of the customer's future journey.** It is specific enough that you could recognize the day it is reached. An ambition statement or a feature list is a different thing.
> * **A strategy works backward from the vision.** It is a few ordered steps from today's journey to the future one, each with what must be true first, a milestone that can be measured and a statement of what will not be done.
> * **A strategy with no diagnosis and no choice is a goal.** Rumelt's kernel of diagnosis, guiding policy and coherent action is the test, and a strategy that passes it lets a leader say no with a reason.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Feature Factory** — a feature list in place of a vision leaves teams building whatever was requested.
> * **The Escalation Ladder** — with no rule for refusing a request, every request travels up to the one person who may decide.
> * **The Consensus Stall** — a strategy that sets nothing aside is agreed by everyone and decides nothing.

<br>

In one month early in 2025 three requests reached Priya Nambiar, who had just become chief product officer of Corvane, the fictional company this book follows. Corvane makes scheduling software for field-service companies and was growing toward 500 people that year. Sales wanted a custom approval step for the largest customer. Sales also wanted route optimization, because a competitor had it. The team that builds the technicians' mobile app wanted an offline mode. Each request could be argued to move an outcome Corvane cared about. The strategy deck opened with a slide titled Vision, which read "The operating system for field service", and that slide could not say which request came first. All three went on the roadmap.

If you have accepted outcomes as the unit of progress, you have probably still sat in that meeting: every request moves some outcome, and nobody can refuse one with a reason. What is missing is a direction and an order. This chapter's claim is that a product vision becomes a strategy teams can act on when it is written as **the customer's future journey**, specific enough to recognize when reached, and the strategy **works backward** from it: a few ordered steps from today's journey to that one, each with a measurable milestone and a statement of what will not be done. The chapter starts with Corvane's three requests. It then defines the vision and writes Corvane's, defines the strategy and writes Corvane's first three steps, and tests the result with Richard Rumelt's kernel of good strategy. It ends with where the sources disagree, what the product strategy hands on to the engineering strategy and to planning, and what AI changes.

## Setting the Scene: Three Requests and a Slide

The first request came from sales. Corvane's largest customer, a lift-maintenance company whose renewal was due, wanted an approval step of its own, in which a supervisor signs off each job before it is scheduled. Keeping that customer would move retained revenue. The second also came from sales. In two lost deals a competitor had shown route optimization, software that orders a technician's jobs to shorten the driving, and winning such deals would move new revenue. The third came from the Technician App team, one of Corvane's product teams. Support tickets showed job updates lost in basements and lift shafts, where phones have no signal, and an offline mode would move the share of jobs completed without a call to the office. Each request had a requester, a reason and a number.

Nothing Corvane had could rank them. Its outcomes said which numbers should move and gave no reason to move one before another. The vision slide stated an ambition that all three requests served equally well. Behind the slide came a list of features with dates. Outcomes had replaced the list of promises in the teams' goals for 2025, but the roadmap itself still had the form of the years when it listed features promised to large customers, and a list always has room for one more line. So all three were accepted. The previous chapter, [[outcomes-over-output]], made outcomes the unit of progress. That leaves open two questions that outcomes cannot answer for themselves: **which outcomes, and in what order**.

## A Vision Is the Customer's Future Journey

The first missing piece is a description of where the customer should end up. In *Build What Matters*, Ben Foster and Rajesh Nerlikar call it the end-state vision, and they define it from the customer's side: what the future looks like when the product meets the customer's need. They are explicit about what it is not: "The vision is not a bulleted list of product features but rather an expression of how the customer will derive value from those features." Their name for its written form is the **customer journey vision**: a description of the journey a customer takes with the product, in six stages: trigger, discovery, evaluation, trial, engagement and retention. The trigger is what makes the customer look for a new solution, and retention is where they decide to stay. It is, they say, far more detailed than a mission statement. It is also the second of the three components of what they call vision-led product management. The first is the key customer outcome, the subject of the previous chapter, and the third is the product strategy, which comes later in this one.

Three different things are called a vision in practice. They differ in whose point of view they take and in what they can decide when a request arrives.

| What is called a vision | Example | Whose point of view | What it can decide |
| --- | --- | --- | --- |
| An ambition or mission statement | "The operating system for field service" | The company's | Nothing about a single request, since every request serves it |
| A feature list | "Approval workflows, route optimization, offline mode" | The product's | What is built next, without a reason |
| A customer journey vision | "A planner starts Monday with the week already scheduled" (a planner is the person in a field-service company's office who assigns jobs to technicians; Corvane's vision is given in full in the next section) | The customer's | Whether a request lies on the way to that future |

A customer journey vision is usable only under some conditions. Foster and Nerlikar advise breadth over depth: every stage is described, each in only enough detail to show that the journey is plausible. As a default they set the horizon at about three years, which is their rule of thumb and not a law, and they accept that a vision that far out requires a leap of faith. To their rules I add one test, in my own wording: a vision must be **specific enough to recognize when reached**. A reader should be able to say what they would observe in a customer's office on the day the vision is true. "The operating system for field service" fails that test, because no observation would confirm it.

## Pattern: Write the Vision as a Journey

Writing such a vision is this chapter's first pattern. Its author is the head of product, working with the leaders of design and engineering. Its users are the people who have to answer requests: product managers, team leads and the sales team. Foster and Nerlikar recommend forms that can be read in a couple of minutes, such as a comic strip, mock-ups of the future product or a customer's diary entries, and they warn that the mock-ups are concept sketches and not designs to hand to engineering. The outcome measure I use for the pattern is the share of incoming requests that those users can answer by pointing to a stage of the journey, without going to the head of product. Chapter 2 applied the idea of a vision written from the user's side to the organization itself, with the teams in the place of the customer, in [[the-organization-as-a-product]].

Corvane's vision follows the pattern. Priya Nambiar wrote it in 2025 with Noor Achterberg, Corvane's head of design, for the year 2028. It follows one customer through the six stages: an operations manager at a heating company with forty technicians, and one of her planners. Like every Corvane example in this book, it is an illustration.

| Stage | What the customer experiences in 2028 |
| --- | --- |
| Trigger | The operations manager sees her planners spend every Monday rebuilding the week by hand, and hears customers complain that they learned of a moved appointment only when they called. |
| Discovery | She hears from another service company that its week arrives already planned. |
| Evaluation | She loads last month's real jobs and sees the week Corvane would have planned beside the week her planners made. |
| Trial | One region runs for two weeks on proposed schedules. The planner accepts or changes each proposal. |
| Engagement | A planner starts Monday with the week already scheduled. When a technician calls in sick, the plan repairs itself and the customers affected are told before they ask. The technician sees the changed day on the phone. |
| Retention | Each month the operations manager sees the planning hours saved and the share of appointments kept as first promised, and she renews on numbers she can check. |

Read against this journey, the three requests no longer look alike. A custom approval step for one customer appears in no stage of it. An offline mode touches the engagement stage, where the technician sees the changed day on the phone. Route optimization could serve the planned week of the same stage. So the vision does part of the work: it separates the request that lies off the customer's way from the two that lie on it. It does not do the rest. Between the two requests that remain, and among the many things the journey itself requires, the vision gives no order.

## Strategy Works Backward from the Vision

The order comes from the strategy. Foster and Nerlikar define the product strategy as the way from point A, the customer's journey with the product today, to point B, the journey of the vision. In their account it works backward from the vision, takes business realities and constraints into account, identifies the key steps and sets measurable milestones. Its first move is a gap analysis: the future journey is laid beside today's, stage by stage, and the differences are written down. The gaps are not yet an order.

Working backward turns the gaps into steps. You ask of the vision what has to be true just before it can be, then ask the same question of that answer, and continue until you arrive at what is true today. The steps are then carried out in the opposite direction, each ending in a milestone.

---begin mermaid---
flowchart RL
    V["Customer journey vision"] -->|"what must be true first?"| S3["Step 3 and its milestone"]
    S3 -->|"what must be true first?"| S2["Step 2 and its milestone"]
    S2 -->|"what must be true first?"| S1["Step 1 and its milestone"]
    S1 -->|"what must be true first?"| A["Today's journey"]
---end mermaid---

**Figure 1:** *The steps of a strategy are found from the vision backward, by asking what must be true first, and are carried out from today forward.*

What working backward finds is a chain of prerequisites, and the order in which the chain is built also depends on constraints. Foster and Nerlikar list six factors that set it: funding, competitive advantage, the order in which market segments are served, the delivery of an outcome in phases, technology and data dependencies, and strategic leverage such as partnerships. Each step ends in a milestone, which they describe as the point where you know it is time to move into the next phase and as a natural place to reassess the plan. They expect the reassessment to change it: "It's okay to change your strategy along the way. In fact, it's essential." A milestone is an outcome with a measure, so the order of the steps is also the order of the outcomes, which is what Corvane lacked.

To each step I add a third part, which is my addition to their two: a statement of **what will not be done** while the step is under way. A step that refuses nothing gives no order, because any request can be attached to whichever step is current. Richard Rumelt, whose test of a strategy comes two sections below, gives a second reason for the refusal.

## Pattern: Three Steps, Each with a Milestone and a No

The second pattern is to write the first three steps of that chain. Its author is again the head of product, and its users are the product leaders who must answer requests and brief teams. Each step has the three parts just described: what must be true before it can start, the milestone that shows it is done, and what will not be done meanwhile. I write three steps and no more, because the reassessment at each milestone changes what follows. The pattern has two outcome measures: whether each milestone is reached when it is reassessed, and how many requests per quarter still have to be escalated to the head of product.

Corvane's point A in 2025 was far from the vision. Planners built the week by hand and re-planned by phone when a technician called in sick, and customers learned of a moved appointment when they rang the office. The product could detect a conflict in a schedule and could not propose a schedule. The cause lay under the screens: what a planner knows about technicians' skills, parts and customers' time windows was in the planner's head and not held as data. A second obstacle followed from the first, because planners had no reason yet to trust a schedule they had not made themselves. That was the gap.

Working backward from the 2028 vision across that gap gave three steps, listed here in the order in which they are carried out. One principle sets that order, and it answers the second obstacle: earn the planner's trust one disruption at a time before planning the whole week. The percentages are illustrations.

| Step | What must be true first | Milestone | What will not be done |
| --- | --- | --- | --- |
| 1. Every change to the schedule reaches the customer and the technician without a phone call | Each schedule change is published in one way, whichever part of the product makes it; in 2025 changes are recorded and carried by three different systems | 80% of appointment changes reach the customer through the product before the customer contacts the office | No approval workflows built for a single customer |
| 2. For one kind of disruption, a technician who is sick, the product proposes a repaired plan and the planner decides | Step 1's channel, so that a repaired plan reaches the customer and the technician; technician skills, parts on hand and customer time windows held as data and no longer in planners' heads | Planners accept 60% of proposed repairs unchanged | No route optimization beyond today's travel-time estimates |
| 3. The week arrives planned: each Friday the product proposes the next week | Planners trust the proposals, which step 2's milestone shows | Half of customers' weeks start from a proposed schedule | No dispatch without a planner's confirmation |

With the steps written, the three requests of the opening get three different answers. The custom approval step gets a no: it is on no stage of the journey, and step 1 excludes it by name. Route optimization gets a not yet: step 2 excludes it by name, because repairing one technician's day needs no more than the travel-time estimates the product already has, and whether the planned week of step 3 needs more is decided at step 2's milestone. The offline mode gets a yes in a narrower form: the technician of step 1 must receive the changed day on a phone with poor reception, and step 1 needs no more of an offline mode than that. Each answer carries a reason that the requester can check against the page, which the vision slide never offered.

## Testing the Strategy: Rumelt's Kernel

The three steps came from one book's method, and a second source gives an independent test of whether the result is a strategy at all. In *Good Strategy Bad Strategy*, Richard Rumelt argues that a good strategy has a **kernel** of three elements. The diagnosis defines the nature of the challenge. The guiding policy is the overall approach chosen for dealing with the obstacles that the diagnosis names. The coherent actions are coordinated steps that carry out the policy. A document without them is, in his account, usually a set of goals. He also states his reason for the refusal in each step: "Strategy involves focus and, therefore, choice." A choice that sets nothing aside has not been made.

Each element of the kernel has a counterpart in a strategy that works backward from a vision. The mapping in the table is mine, not Rumelt's, and its last column fills it in for Corvane.

| Kernel element (Rumelt) | The question it answers | In a strategy that works backward | Corvane, 2025 |
| --- | --- | --- | --- |
| Diagnosis | What is the challenge? | The gap analysis: why today's journey is not the future one | The product records a schedule and cannot propose one, because what a planner knows is not held as data |
| Guiding policy | What is the approach, and what does it rule out? | The principle behind the order of the steps, with what will not be done | Earn the planner's trust one disruption at a time before planning the week; build nothing for a single customer |
| Coherent action | What is done, so that the actions support each other? | The steps and their milestones | The three steps, each of which makes the next possible |

Rumelt also turns the kernel into a check, through four hallmarks of bad strategy: fluff, which is inflated language in place of an argument; failure to face the challenge; mistaking goals for strategy; and bad strategic objectives, which are impracticable or miss the critical issue. Corvane's old deck can now be judged by them. "The operating system for field service" is a goal. The list of features with dates that followed it names no obstacle and rules nothing out. So the deck shows two of the four hallmarks: it does not face a challenge, and it mistakes a goal for a strategy. The three steps name the obstacle, which is that the planner's knowledge is not held as data, and each of them refuses something.

A strategy with no diagnosis and no choice shows up in daily work as three of this book's failure patterns. With a feature list in place of a vision, teams build what was requested, which is the Feature Factory. With no rule for refusing, each request travels up to the one person who may decide, which is the Escalation Ladder; at Corvane that person was the CPO. And a strategy that sets nothing aside can be agreed by everyone, because it costs nobody anything. Rumelt's sign for that case is that "universal buy-in usually signals the absence of choice." In this book's terms it is the Consensus Stall in written form: a decision that is finished only when everyone agrees, and so contains nothing anyone would object to.

## Where the Sources Disagree

The sources do not agree with each other, and the first disagreement is over the word vision itself. Rumelt distrusts visions. Of a statement offered as a vision he writes: "This 'vision' communicates an ambition, but it is not a strategy or a guiding policy because there is no information about how this ambition will be accomplished." Foster and Nerlikar build their whole method on a vision. The two positions fit once you see that they describe different objects under one word. Rumelt's target is the ambition statement, of the kind on Corvane's slide, offered as if it were the strategy. Foster and Nerlikar's vision is a described journey, and they say themselves that a vision without a practical plan to reach it is a fantasy. So the vision stays the destination, and Rumelt's kernel is applied to the strategy that leads there.

The second disagreement is with Marty Cagan, whose *Empowered*, written with Chris Jones, I use here through my own summaries of it in [[product-vision-and-principles]] and [[empowered-product-strategy]]. Cagan gives the vision a longer horizon, three to ten years, where Foster and Nerlikar default to about three. He pairs it with **product principles**, stated rules that let teams settle trade-offs without asking. And his strategy does not end in sequenced steps: it is a focus on a few critical problems, with an explicit statement of what will not be prioritized, and it ends in problems handed to teams as objectives. Which horizon fits depends on how fast your market and your technology change. On the form of the strategy I take something from each, and the combination is mine: the steps give the order, as in *Build What Matters*, and each step reaches the teams as a problem to solve, as in *Empowered*. [[discovery-delivery-and-empowered-teams]] develops that division between the order, which leaders set, and the solution, which teams find.

The strongest objection rejects the vision altogether. It holds that a three-year vision is guesswork that will turn out wrong, and that strategy should emerge from fast iteration and data: test, and follow what works. The objection is right that the strategy will change. Foster and Nerlikar expect that, and they recommend reassessing both the roadmap and the vision at a third or a quarter of the time horizon. The objection is wrong that iteration can choose the destination. Iteration improves what exists by comparing it with its near neighbors. It cannot choose between futures, because the alternatives do not exist yet to be measured. Each of Corvane's three requests could have been built and iterated on with good results, and the product would have improved in three directions at once.

## What the Product Strategy Hands On

A product strategy that has passed these tests becomes an input to two other things, and the first is the engineering strategy of Part IV. Each step's "what must be true first" is often an engineering matter. Foster and Nerlikar provide for this in their fifth sequencing factor, technology and data dependencies, the assets needed to support the future journey. At Corvane, step 1's prerequisite is of that kind: every schedule change has to be published in one way, and in 2025 its teams ran three message brokers, the systems that carry such events between services. Step 2 needs parts data in one form from the Stock Integrations team, which connects Corvane to customers' stock systems. The traffic runs both ways: the product strategy tells engineering what must become true, and engineering answers with constraints that can change the order of the steps. [[engineering-strategy]] treats the diagnosis and the policies that settle such questions.

The second is planning, the subject of Part VI. The product strategy tells planning which outcomes come first. Planning decides how much capacity each of them gets, and holds that decision steady. Neither can do the other's job. Corvane's following year shows that a strategy cannot do planning's job: in 2026, a year after the three steps were written, its quarterly planning took nine of the quarter's thirteen weeks. The strategy had said what came first. It had not said who allocates capacity, or how. A planning process, in turn, cannot supply an order of outcomes that no strategy has chosen. [[planning]] takes this up, after the next chapter has laid the steps out in time.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The strategy described above, and what it hands on, were worked out for a world in which showing a future and building toward it are both expensive, and AI lowers both costs. **Emerging.** As of November 2026, product leaders I have observed use generative tools to produce the artifacts of a vision, storyboards and mock-ups of a future product, in hours where they used to take weeks. This is my observation and not a measured result. It lowers the cost of showing a future journey. It leaves the cost of choosing one where it was, since a tool will draw any of ten futures equally well.

Cheaper drawing has a counterpart in cheaper building. **Speculative.** When coding agents make a feature cheaper to build, saying yes to a request costs less engineering time, and it costs the product's coherence as much as before. A feature list would then grow faster, and the need for a vision and a strategy that bound it would grow with it. The claim follows from the argument of Part XI, in [[where-the-constraint-moves]]. It would be confirmed where organizations that use agents report more features shipped per quarter with no movement in retention or in their key customer outcome.

## What to Take Away

**Established.** What the sources agree on:

- A vision describes the customer's future from the customer's side, and a feature list is not one (Foster and Nerlikar, *Build What Matters*; Cagan, *Empowered*, as I summarize it).
- A strategy needs a diagnosis and a choice, and a goal is not a strategy (Rumelt, *Good Strategy Bad Strategy*).
- A strategy is revised as evidence arrives, at its milestones (Foster and Nerlikar).

**Depends on context.** What changes with the situation:

- How far ahead the vision looks. About three years is one source's default and three to ten years another's; the faster your market and technology change, the shorter the horizon you can describe.
- How many steps can be written in advance. I write three; where little is known about the customer, even the second is a guess.
- How detailed the journey is. It depends on how much you know about the customer at each stage.

**The author's synthesis.** What is this book's own position:

- The vision and the strategy do different jobs and fail differently. The vision bounds which problems are worth solving, and fails by being an ambition or a list. The strategy orders them, and fails by having no diagnosis and no refusal. An organization needs both before it can choose one outcome over another.
- The statement of what will not be done on every step, and the mapping of Rumelt's kernel onto a strategy that works backward, are my additions to the sources.

## Checklist

The checklist turns the two patterns and the test into eight questions. Ask them of your product's vision and strategy as they are written today. My working checklists for both are in [[customer-journey-vision]] and [[product-strategy]].

- [ ] Vision: is it written from the customer's side, as a journey, with no feature named?
- [ ] Does it cover every stage from trigger to retention, each in enough detail to be plausible?
- [ ] Could you say what you would observe at a customer on the day it is true?
- [ ] Gap: have you laid today's journey beside the future one and written down the differences?
- [ ] Steps: are the first three steps written, in order, each with what must be true first?
- [ ] Does each step have a milestone that can be measured, and a date to reassess?
- [ ] Does each step say what will not be done while it is under way?
- [ ] Test: can you state the diagnosis in one sentence, and name one request the strategy refuses?

Three requests reached Corvane's CPO in one month of 2025, and all three were accepted. You can now say why, and you can give the three answers the strategy gives: no, not yet, and yes in a narrower form. The strategy behind those answers is a set of ordered steps toward a vision. The next chapter lays those steps out in time and says what each horizon can commit to: [[roadmaps-and-horizons]].

## Sources and Evidence

**Books**

- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. The end-state vision from the customer's side; the customer journey vision and its six stages; the three-year default; product strategy working backward through key steps and measurable milestones; the gap analysis and the six sequencing factors; reassessment.
- *Good Strategy Bad Strategy: The Difference and Why It Matters*, Richard Rumelt, 2011. The kernel of diagnosis, guiding policy and coherent action; the four hallmarks of bad strategy; strategy as choice; the criticism of vision statements. The mapping of the kernel onto a vision-led product strategy is the author's.
- *Empowered: Ordinary People, Extraordinary Products*, Marty Cagan with Chris Jones, 2020. One shared product vision with a horizon of three to ten years; product principles; strategy as focus on a few problems that ends in team objectives. Used through the author's summaries, not from reading notes.

**Practitioner sources**

- The author's records on these sources, with working checklists: [[customer-journey-vision]], [[product-strategy]], [[product-vision-and-principles]] and [[empowered-product-strategy]].
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
