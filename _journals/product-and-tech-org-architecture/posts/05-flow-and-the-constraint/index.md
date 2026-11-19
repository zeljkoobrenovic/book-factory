---
title: "Flow and the Constraint"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Which capacities run out in an organization, where is delivery capacity lost, and what should a leader add to get it back? Three run out (attention, judgment and verification), capacity is lost at one constraining step at a time, and what recovers it depends on the state of the team behind that step."
permalink: flow-and-the-constraint
timetoread: 21 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to find the one step that limits a delivery flow, name the capacity it is short of, and choose what the team behind it needs.

> **KEY POINTS:**
>
> * **Three capacities run out.** They are judgment, attention and verification, and each leaves a different queue: work waiting for an answer, for someone who understands it, or for a check.
> * **A flow moves at the pace of its constraint.** Most lead time is waiting between teams, and capacity added anywhere but the slowest step makes that wait longer.
> * **What to add depends on the team's state.** A team falling behind needs people or less scope, one treading water less work in progress, one repaying debt time, and one innovating protected slack.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Overloaded Team** — the team at the constraint falls further behind while new headcount goes to other teams.
> * **The Review Bottleneck** — a queue for checks grows each time capacity is added to the steps before it.
> * **The Hero Culture** — a person through whom all work must pass is a constraint, however much they are praised for it.

<br>

In 2024 a change at Corvane took about two days to write and seventeen more to reach customers. Corvane is the fictional company this book follows. In the two years before, it had grown from 45 engineers to 95, and its median **lead time**, the time from starting work on a change to its release, had gone from 4 days to 19. Every new engineer had joined a team that wrote changes. Corvane had doubled the number of people who did the two-day part. If you have received headcount, shared it fairly among your teams and seen delivery get no faster, you have met the same thing.

Where the people went mattered more than how many they were. The previous chapter gave teams a sizing rule and boundaries a placing rule; this one follows work as it crosses those boundaries. **Three capacities run out** in an organization: attention, judgment and verification. Capacity is lost at **one constraining step at a time**, most often a queue between teams, where one of the three is exhausted. And what recovers it depends on **the state of the team behind that step**, which says whether the team needs people, less work in progress, time or protected slack. The chapter follows one Corvane change, explains why a flow moves at the pace of its constraint, and defines the three capacities a constraint can be short of. It turns both into a pattern for finding the constraint from wait times, and adds Will Larson's four team states, which say what to give the team behind it. Then come a point where the sources disagree, two planning habits that keep a constraint in place, Corvane's queue diagnosed, and what AI changes. As the last chapter of Part I, it ends by explaining Corvane's slowdown with all of the part's ideas.

## Setting the Scene: Two Days of Work, Seventeen Days of Waiting

In 2024 Corvane had 180 people. Its 95 engineers worked in eleven product teams of about eight, formed the year before by dividing people evenly, and in one platform team of five, led by Lena Brandt. A change passed through two teams on its way to customers. A product team, such as Scheduling or Dispatch, wrote it. The platform team launched it.

A launch was a check done by hand, followed by a release. Corvane had no agreed test of readiness that a product team could run itself, so a platform engineer went through each change before it went out: its database migrations, its configuration, and the way back if the release failed. Then the engineer released it in a scheduled slot. At the peak in 2024, fourteen launch requests were open. The figure shows the path and the time a change spent in each part of it.

---begin mermaid---
flowchart LR
    W["Product team writes the change: about 2 days"] --> Q["Launch queue at Platform: about 17 days, 14 requests open"]
    Q --> L["Platform engineer checks and releases: hours"]
    L --> C["Customers"]
---end mermaid---

**Figure 1:** *The path of a Corvane change in 2024: of 19 days of lead time, about 17 were spent waiting between the team that wrote the change and the team that launched it.*

Corvane's leaders had two explanations for the queue of fourteen. The first was the one behind the hiring plan of 2022: too few engineers. The second arrived with the queue: the platform team was slow. Each explanation named a team to be enlarged or blamed. Neither could say why a company with twice the engineers delivered more slowly than before.

## Why a Flow Moves at the Pace of Its Constraint

A rule about flows explains what the two explanations could not. Chapter 1 named work as one of the things that flow between teams; the path one piece of work takes across teams is what this chapter calls a **flow**. A flow is made of **steps**, where someone works on the item, and **queues**, where the item waits for the next step; lead time is the sum of both. In *An Elegant Puzzle*, Will Larson describes management problems as stockpiles that grow and shrink with what flows in and out of them. A queue is such a stockpile: it grows whenever work arrives faster than the next step takes it. The **constraint** of a flow is the step whose capacity is smallest compared with what arrives at it.

Because every item has to pass that step, the whole flow delivers at its pace, whatever the capacity of the other steps. This is the central claim of the theory of constraints, which Eliyahu Goldratt set out in *The Goal* in 1984: a system's output is set by its constraint, so an hour lost there is lost for the whole system, and an hour saved anywhere else changes nothing. *The Goal* is not among the books this one is built on; I cite it for this widely known claim, as a supplement to my sources. Donella Meadows says the same of systems in general in *Thinking in Systems*: any growing system runs into some kind of constraint sooner or later.

The time lost at a constraint shows up as waiting, and mostly as waiting between teams, for two reasons. The first is that a queue does not grow in proportion to load. Larson states the rule: "The expected time to complete a new task approaches infinity as a team's utilization approaches 100 percent". The second reason is that nobody sees the queue. Donald Reinertsen argues in *The Principles of Product Development Flow* (2009) that queues are the main cause of delay in product development, and that they go unmanaged because waiting designs and code, unlike parts piled on a factory floor, are invisible. Reinertsen's book also supplements my sources and is cited for that claim only. Between teams the second reason is at its strongest: the item has left the team that finished it, and for the team that must pick it up it is one request among many.

The rule answers Corvane's puzzle. Capacity added to any step except the constraint sends more work to the constraint's queue. Between 2022 and 2024 Corvane put fifty more engineers into the teams that wrote changes, and they wrote more changes. The platform team stayed at five, so the additional changes joined the launch queue, which reached fourteen requests while lead time reached 19 days. **The hiring wave lengthened the queue it was meant to shorten.**

## Three Capacities That Run Out: Judgment, Attention, Verification

A queue says where work waits. It does not say what the work waits for, and the usual assumption, that it waits for more hands, is often wrong. In a product and tech organization work waits for one of three **capacities**: judgment, attention or verification. A capacity, in this book, is something the work uses up. [[the-organization-as-a-system]] named the three and noted that a redesign creates none of them; it only decides where they are spent. I take them in the order in which Corvane ran short of them, at 12, 50 and 180 people, which is not the order in which this book usually lists them. Meadows explains why the shortage changed with size: "growth itself depletes or enhances limits and therefore changes what is limiting."

The first is **judgment**: deciding with the relevant information at hand. In 2019 Corvane had 12 people at one table, eight of them in product and tech. Every pricing, design and release decision waited for Tomas Rell, the co-founder and CTO, and Corvane later called this the Founder Queue. Tomas had the information and decided well, but there was one of him, and engineers started a second piece of work while the first waited for his answer. That is the sign that judgment has run out: **started work is parked behind a question**. It also runs out when the person who answers has the time and lacks the information, because the decision is made far from the work. Judgment is not the same thing as a **decision right**, which chapter 1 defined as the agreed answer to who may decide a named kind of question. A decision right is a lever and can be moved in a day. Judgment is the capacity that deciding uses up: the time of someone who has the information. Moving a decision right moves where judgment is spent, and it adds judgment only when the new holder has the information to decide with.

The second is **attention**: how much a team can hold in mind well enough to change it safely. The attention meant here is a team's. It is not one person's concentration or a leader's interest in a topic. By 2021 Corvane had 50 people, 28 of them in product and tech, in four teams, and the product had grown past what anyone could keep in mind. Samir Haddad, an engineer in the Core team, was the only one who understood both the scheduling engine and the mobile sync, and changes that touched both waited for him. Nobody in that queue was waiting for a decision. That is the sign that attention has run out: **an area can be changed by one person only, slowly, or not at all**. [[cognitive-load-and-team-boundaries]] measures this capacity as cognitive load, the term used in *Team Topologies*, and sizes what a team owns by it.

The third is **verification**: knowing that what was built is correct and was worth building. This is the capacity behind the launch queue of 2024, at 180 people. The product teams understood their own changes, so the queue was not short of attention. Nobody in it was waiting to be told what to build, so it was not short of judgment either. What Corvane lacked was a quick way to establish that a change was safe to release. The sign that verification has run out is **finished work waiting for a check**: a review, a test run, a launch. It has a second, quieter sign: work is released unchecked, and nobody can say afterward whether it worked.

The three differ in what the waiting work is waiting for, and that gives the test for any queue: ask what would empty it, an answer, someone who understands the work, or a check. The name of the step does not tell you. Take changes that wait three days for code review. If any of ten engineers could review them and none has the time, the shortage is verification. If only one engineer understands the module, the shortage is attention, and more reviewers who do not understand it will not empty the queue. If author and reviewer disagree about what the feature should do and nobody settles it, the shortage is judgment. The table sets the three side by side.

| Capacity | What it is | The work is waiting for | Sign that it has run out | At Corvane |
| --- | --- | --- | --- | --- |
| Judgment | Deciding with the relevant information at hand | An answer | Started work parked behind a question; decisions travel upward or are guessed | The Founder Queue, 2019, 12 people |
| Attention | What a team can hold in mind well enough to change it safely | Someone who understands it | One person per area; changes there are slow or avoided | Changes waiting for Samir Haddad, 2021, 50 people |
| Verification | Knowing the work is correct and was worth building | A check | Finished work waits for a review, a test or a launch, or ships unchecked | The launch queue, 2024, 180 people |

## Pattern: Find the Constraint from Wait Times

The rule about flows and the three capacities combine into a pattern for locating a constraint. Its user is the leader accountable for a flow that crosses several teams, together with the teams in that flow. Its outcome measure is the flow's lead time and the share of it spent waiting. It has five steps.

1. Pick one flow, and take ten to twenty changes that were released recently.
2. For each change, record when work on it started, and when it entered and left each team on its way to release.
3. Add up, for each step, the time spent working and the time spent waiting.
4. Find the longest wait. The step behind that queue is the constraint.
5. Ask what the waiting work was waiting for (an answer, someone who understands it, or a check) and name the capacity.

The steps measure waits one by one, and the delivery metrics most organizations already have do not. *Accelerate*, by Nicole Forsgren, Jez Humble and Gene Kim (2018), made lead time for changes one of four key metrics of software delivery, with deployment frequency, change failure rate and time to restore service. Such a figure is a good outcome measure for this pattern, and it does not locate a constraint: a median of 19 days says that the flow is slow, and only the waits, step by step, say that 17 of those days sit in one queue.

Measuring matters because intuition points elsewhere. The constraint is often not where the complaints are, and not where people look busiest: every step before the constraint looks busy, because its work is piling up further along. The constraint can also be one person. In *The Phoenix Project*, a novel by Gene Kim, Kevin Behr and George Spafford (2013), every important piece of work passes through the engineer Brent, and he turns out to be the constraint of the whole IT organization. Samir Haddad was Corvane's Brent in 2021. A person in that position is usually praised for it, which is the failure pattern this book calls **The Hero Culture**.

## Four Team States and What Each One Needs

Knowing the constraint and the capacity it is short of leaves one question: what to give the team behind it. That depends on the state the team is in. In *An Elegant Puzzle*, Larson places every team in one of four states, on a line from worst to best, each with a signal that anyone on the team can report. "A team is falling behind if each week their backlog is longer than it was the week before." A team is **treading water** when it gets its critical work done and cannot start paying down technical debt or begin major new projects. A team is **repaying debt** when it has started to pay debt down and each repayment frees time for the next. A team is **innovating** when its debt is sustainably low, morale is high and most of its work serves new user needs.

Each state is short of something different, and Larson gives each its own fix. The signals and fixes in the table are Larson's; the one-word shortages and the last column are my reading.

| State | Signal | Short of | Larson's fix | What does not help |
| --- | --- | --- | --- | --- |
| Falling behind | The backlog is longer every week | People | Hire until the team is treading water | Asking it to prioritize better |
| Treading water | Critical work gets done; no time for debt or new projects | Focus | Consolidate effort and limit work in progress | More people |
| Repaying debt | Debt is going down, and each repayment frees time | Time | Add time | New projects |
| Innovating | Debt is low; most work serves new user needs | Room | Keep enough slack in the schedule | Filling the schedule |

Because the shortages differ, the fixes cannot be swapped. A team that is treading water has enough people and too many things in progress, and new people add onboarding and coordination to a team that is short of focus. A team that is repaying debt and is handed a new project stops repaying, and loses the time each repayment was freeing. An innovating team is the tempting place to take people from, and Larson warns against that as well: "moving one person can shift an innovating team back into falling behind". One remedy applied to all four states helps one team and harms the other three.

Joined to the constraint, the states give a rule for headcount. People go to the team at the constraint, if that team is falling behind, and to one team at a time. Larson writes: "For each constraint, prioritize one team at a time." Where hiring would take too long, he offers another relief: move scope away from the team and keep the teams intact. The capacity that ran out at the constraint says which people or which scope. For verification it is people who can check, or checks moved off the team. For judgment it is someone informed who may decide. For attention it is less to understand. The states of the teams away from the constraint say what each needs other than people; the next section takes the hardest case, a team that is falling behind away from the constraint. Joining the states to the constraint of a flow is my extension of Larson, who applies them team by team.

## Where the Sources Disagree: Fix the Team or Fix the Flow

That rule joins two sources, and on one point they pull apart. Larson reasons team by team. He would hire into a team that is falling behind wherever it sits, and he treats a team that has gelled, whose members have learned to work together, as something a leader should be slow to take apart. The theory of constraints reasons flow by flow. In its widely known steps you find the constraint, get the most out of it, pace every other step to it, and only then add capacity to it. The two give different answers for a team that is falling behind and is not the constraint. Larson would staff it, and Goldratt would not.

I follow Goldratt on the order and Larson on the means. Relieve the constraint first, in one of three ways. Two are Larson's, from the previous section: add people, or move scope away. The third is Goldratt's: limit what reaches the constraint. Which one depends on how long the shortage will last and on who else can safely do the work, as the table below sets out. A team that is falling behind away from the constraint gets less intake, and not more people, until the constraint has moved, because more output from it would only wait. When the constraint moves and that team is now the one behind it, the team gets the people.

| Choice | What you gain | What it costs | Fits when |
| --- | --- | --- | --- |
| Add people to the team at the constraint | Capacity that stays | Months of hiring and onboarding; the team has to gel again | Nobody else can do the work, and the shortage will last |
| Move scope away from it | Relief within a quarter; teams stay intact | The receiving teams carry more | Part of its work can be done safely by the teams that wait for it |
| Limit what reaches it | No new cost; the queue stops growing | Visible slack upstream | Relief is on the way and the queue only has to stop growing |

## Anti-Patterns: Even Shares and Full Utilization

Planning usually follows neither source. The first habit is **even shares**: new headcount is divided in proportion to team size, or according to which stakeholder pushes hardest. **An even share is a decision to leave the constraint where it is.** Larson calls the urge to spread limited resources evenly indecision framed as fairness, and answers it: "it's not a fair outcome if no one gets anything." An even share gives the team at the constraint a fraction of what would lift it out of falling behind, and sends the rest to teams whose output will wait in its queue. The result is **The Overloaded Team** at the constraint and, when the constraint is a check, **The Review Bottleneck**: a queue for review or launch that grows with every hire made upstream.

The second habit is **full utilization**: the belief that every team should be busy all the time and that visible slack is waste. Away from the constraint, a team working at full pace produces work that only waits, and its slack is what keeps the pile in front of the constraint from growing. At the constraint, Larson's rule about utilization applies: a team used to the full is a team with a long queue. Visible slack away from the constraint is the price of flow.

## Worked Example: The Launch Queue, Diagnosed

The pattern, the states and the choice among people, scope and intake can now be applied to the queue the chapter opened with. In 2024 Dario Vance, Corvane's VP Engineering, held a review of how work flowed: he read the launch log and interviewed every team lead ([[the-organization-as-a-product]] tells that story). Followed step by step, the median change looked like this.

| Step | Team | Working | Waiting |
| --- | --- | --- | --- |
| Write the change | A product team | About 2 days | None |
| Wait for a launch slot | Platform | None | About 17 days |
| Check by hand and release | Platform | Hours | None |

The table puts the constraint at the launch, where one wait holds nearly all of the lead time. The waiting changes were finished and understood, and what they waited for was a check, so the capacity that had run out was verification. The team behind the step was falling behind, by Larson's signal: the platform team's count of open launch requests had grown every month since the eleven teams were formed in 2023.

A team that is falling behind needs people or less scope, and Dario chose scope. Hiring platform engineers would have taken quarters, and the check itself could be changed. Corvane agreed on a set of automated readiness checks that a product team could run on its own change, and with them a release path that did not pass through the platform team. The Scheduling team tried the path for one quarter, and its median lead time came down to 6 days. As the path was extended to the other teams, the company-wide median went from 19 days to 8 at the review two quarters later, and under 7 a quarter after that. Nobody was added to the platform team, and the eleven teams were not reorganized.

During that 2024 review, before the new release path existed, three product teams had asked for engineers. The table gives each team's signal, its state and what it received, with the platform team in the first row: four teams, four states, four different answers, and no team got engineers.

| Team | Signal | State | What it got |
| --- | --- | --- | --- |
| Platform | Open launch requests up every month | Falling behind | Scope removed: product teams run the readiness checks |
| Dispatch | Met its commitments; six projects open for eight engineers; no cleanup for a year | Treading water | Open projects cut from six to three; no added engineers |
| Identity | Halfway through replacing the old permission model; each finished part reduced support work | Repaying debt | Two more quarters without new roadmap commitments |
| Growth | Little debt; one unplanned day a week, used for experiments | Innovating | Kept its unplanned day; no engineers moved out |

Once changes no longer waited for a launch slot, the longest wait at Corvane was for someone to say that a feature was ready for customers, a question nobody had been given the right to answer. Finished features waited for an answer, which is a shortage of judgment. The lever that places judgment is a decision right: naming who, with the information at hand, says a feature is ready. Judgment became the scarce capacity of Corvane's next stage, at 500 people ([[corvane-at-five-sizes]]). A relieved constraint moves, sometimes to a different capacity, so the five steps are run again.

## What AI Changes Here

The queue at a constraint also grows when capacity arrives somewhere else in the flow, and that is what AI does. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, in the teams I have observed, coding agents add capacity to the step of writing changes. In most flows that step is not the constraint, so by this chapter's rule the queues grow at the steps that check: review and launch. This is my observation, not a measured result. The book's illustration is Corvane's fifth stage, in 2027 and 2028, at 1,100 people: merged changes per week rise 2.4 times in a year, review capacity stays flat, and the median wait for a review goes from 5 hours to 31. It is the hiring wave again, with agents in place of hires ([[agentic-delivery]]).

If checking is automated as well, the constraint has one more place to go. **Speculative.** Where agents take over much of the verification, the longest wait becomes the wait for a decision about what is worth building, and judgment is the scarce capacity. This chapter gives no evidence for it; [[where-the-constraint-moves]] weighs what has been published. The claim would be confirmed where teams with largely automated verification report that their longest wait is for a decision.

## Closing Part I: Corvane's Slowdown Without a Villain

This chapter completes Part I, whose ideas form one line of reasoning, and Corvane's slowdown after the hiring wave shows it. [[the-organization-as-a-system]] supplies the description: the launch was an interface that all eleven product teams depended on, behind a boundary that put every release check inside one team. [[the-organization-as-a-product]] adds that the hiring wave was a change made without discovery and without a stated outcome, so nobody looked for the queue. [[conways-law-and-the-inverse-conway-maneuver]] explains the dependencies: software takes the shape of the teams that build it, and teams cut by dividing people evenly got software, and one shared launch, that followed those cuts. [[cognitive-load-and-team-boundaries]] explains why Corvane had no test of readiness that a team could run itself: teams cut by headcount, and not along the fracture planes where the domain, the rate of change or the risk differs, own parts they cannot change without touching another team's, so no team could say alone that its change was safe, and the check went to the platform team. This chapter adds the last step: the hires went to the part of the flow that took two days. The arrangement of teams shapes the product, the size of what a team owns limits what it can do well, and the slowest step sets the pace of all of them.

That explanation has no villain in it. Part I opened with a question: if Corvane replaced every manager tomorrow and kept its teams, interfaces and planning exactly as they are, what would change? The queue at the platform team would still be there. It came from where a check was placed and from where capacity was added, and new managers would have inherited both. **The hiring wave added capacity where the constraint was not.**

## What to Take Away

**Established.** What the sources agree on:

- A flow delivers at the pace of its constraint, and capacity added to another step does not raise its output (Goldratt, *The Goal*; Meadows on limits, *Thinking in Systems*).
- Waiting time rises steeply as a team's utilization approaches 100 percent (Larson, *An Elegant Puzzle*; Reinertsen on queues).
- A team is in one of four states, and each state has its own fix: people, less work in progress, time or slack (Larson).

**Depends on context.** What changes with the situation:

- Whether to relieve a constraint by adding people, by moving scope away or by limiting what reaches it depends on how long the shortage will last and on who else can safely do the work.

**The author's synthesis.** What is this book's own position:

- The three capacities, and the question that tells them apart (what is the work waiting for?), are my own arrangement. The sources speak of constraints and do not sort them this way.
- Joining Larson's team states to the constraint of a flow is my extension of both sources.

## Checklist

Finding the constraint and naming a team's state are two halves of one diagnosis: the wait says where capacity is lost, what the work waits for says which capacity, and the team's state says what to add. Draw your delivery flow across teams, mark the longest wait and name the state of the team behind it.

- [ ] Pick one flow and ten to twenty recent changes; record when each started and when it entered and left each team.
- [ ] Add up working and waiting time per step, and mark the longest wait.
- [ ] Ask what the waiting work waits for: an answer (judgment), someone who understands it (attention) or a check (verification).
- [ ] Name the state of the team behind that wait, starting with whether its backlog grows every week.
- [ ] If that team is falling behind, choose between adding people, moving scope away and limiting what reaches it.
- [ ] Name the states of the other teams in the flow and what each needs that is not headcount.
- [ ] Does your next hire go to the team at the constraint, or is it an even share?
- [ ] After the change, measure the waits again: the constraint will have moved.

In 2024 a Corvane change waited seventeen days after two days of work. You can now say where those days went, what they were short of, and why new managers would have found the same queue. Part I leaves you with three rules: size what a team owns by its cognitive load, place boundaries on fracture planes, and find the constraint before you add capacity. They do not say what to build with them. Which kinds of team an organization needs, how those teams should work with each other and how large each should be is the problem Part II solves, with team types, interaction modes and sizes that apply the three rules: [[part-2]].

## Sources and Evidence

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. The four team states, their signals and fixes; one team at a time; moving scope before people; utilization and waiting; slack; the case against top-down global optimization; problems as stocks and flows.
- *Thinking in Systems: A Primer*, Donella H. Meadows, edited by Diana Wright, 2008. Growing systems meet constraints, and growth changes what is limiting.
- *The Goal: A Process of Ongoing Improvement*, Eliyahu M. Goldratt and Jeff Cox, 1984. The theory of constraints: a system's output is set by its constraint. Not among the author's main sources; cited for its widely known central claim and steps.
- *The Principles of Product Development Flow*, Donald G. Reinertsen, 2009. Queues as the main and least visible cause of delay in product development. Not among the author's main sources; cited for that widely known claim.
- *The Phoenix Project*, Gene Kim, Kevin Behr and George Spafford, 2013. A novel; the engineer Brent as a person who is the constraint.
- *Team Topologies*, Matthew Skelton and Manuel Pais, 2019. Cognitive load as the measure of a team's attention, treated in [[cognitive-load-and-team-boundaries]].

**Research and reports**

- *Accelerate: The Science of Lean Software and DevOps*, Nicole Forsgren, Jez Humble and Gene Kim, 2018. The four key metrics of software delivery, including lead time for changes measured from commit to production.

**Practitioner sources**

- The author's working summaries of the four team states and of managing by stocks, flows and the constraint: [[organizational-design]] and [[systems-and-tools]].
- The statement about coding agents under "What AI Changes Here" is the author's observation as of November 2026 and is labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
