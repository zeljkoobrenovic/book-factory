---
title: "Where Product & Tech Organizations Go Wrong: The Failure Patterns"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Why do the same failures recur across product and tech organizations, whoever is in charge? Because the same structural situation draws the same behavior from different people: twelve named patterns, each tracing to a boundary, an interface, a decision right or an incentive that was set reasonably once and then left in place."
permalink: where-product-and-tech-organizations-go-wrong
timetoread: 25 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn twelve named failure patterns, recognize each by its warning signs, and trace it to a boundary, an interface, a decision right or an incentive.

> **KEY POINTS:**
>
> * **The same failures recur because the same situation recurs.** A structure draws the same sensible behavior from whoever stands in it, so replacing the people brings the failure back with a new cast.
> * **Twelve patterns trace to four things a leader can design.** There are three patterns each for boundaries, interfaces, decision rights and incentives, and the family tells you where to look.
> * **Each pattern began as a reasonable choice.** That is why capable leaders keep making them, and why naming the pattern is more useful than blaming the people caught in it.

<br>

"Happy families are all alike; every unhappy family is unhappy in its own way." Ben Foster and Rajesh Nerlikar quote Tolstoy's sentence in *Build What Matters* just before they list ten dysfunctions of product management. Then they give a list short enough to score any company against: ten patterns, the same ten everywhere. Organizations, unlike Tolstoy's families, are unhappy in a small number of shared ways. If you have watched a struggling team get a new leader, or a slow organization get a new chart, and then watched the same trouble come back, you have met one of them.

The trouble comes back because of where it comes from. [[how-organizations-got-complicated]] showed a growing organization adding its structures one at a time, each for a good reason and each with a cost. This page names those costs. Its list is longer than Foster and Nerlikar's ten, because it covers the whole product and tech organization and not only product management. It is still a short list, and the page argues why: **the same failures recur because the same structural situation draws the same behavior from different people**. There are twelve patterns here, in four families, one family for each thing a leader can design: boundaries, interfaces, decision rights and incentives. Each pattern began as a choice about one of those four that made sense where it was made, and was then left in place.

The page is a catalogue. It first says how to read an entry. Then come the three boundary patterns, the three interface patterns, the three decision-right patterns and the three incentive patterns, in that order. It ends with one table of all twelve, used once on a single incident.

## How to Read the Catalogue

Start with the four things the families are named after. A redesign can change four things about an organization directly, and this book calls them **the four levers**; [[the-organization-as-a-system]] argues for them in full. Each family in this catalogue is the set of ways one lever is commonly set wrong.

| Lever | What it sets | The question it answers | Its three patterns |
| --- | --- | --- | --- |
| Boundary | Which team owns what | Whose is this? | The Org Chart as Architecture, The Overloaded Team, The Reorg as Strategy |
| Interface | The agreed way work and knowledge cross between teams | How do they find out? | The Review Bottleneck, The Platform Nobody Asked For, The Unowned Interface |
| Decision right | Who may decide a named kind of question, and with whose input | Who says yes? | The Feature Factory, The Escalation Ladder, The Consensus Stall |
| Incentive | What the organization visibly rewards | What gets you promoted here? | The Output Scoreboard, The Ladder as Checklist, The Hero Culture |

The levers are what a leader can set. What an organization runs out of is something else, and every cost in this catalogue is counted in it. The book names three **capacities** that run out. **Attention** is how much a team can hold in mind well enough to change it safely. **Judgment** is deciding with the relevant information at hand. **Verification** is knowing that what was built is correct and was worth building. No lever creates more of them; a lever only decides where they are spent. [[flow-and-the-constraint]] treats the three in full.

A pattern recurs because of how it is made, and the chain is the same for all twelve. Someone makes a reasonable choice about a lever. The choice creates a situation, and the situation stays after the reason for it has gone. In *Six Simple Rules*, Yves Morieux and Peter Tollman argue that every behavior at work is a rational solution to a problem, given a person's goals, resources and constraints. So whoever stands in the situation does the sensible thing, and the sensible thing has a cost that grows until someone notices. Replace that person, and the successor meets the same situation and finds the same solution. The figure shows the chain and the two places where a remedy can act on it.

---begin mermaid---
flowchart LR
    A["A reasonable choice about a lever"] --> B["A situation left in place"]
    B --> C["The same sensible behavior from whoever holds the role"]
    C --> D["A cost that grows until it is noticed"]
    D -->|"replace the people"| C
    D -->|"change the lever"| B
---end mermaid---

**Figure 1:** *Replacing people leads back to the same behavior, because the situation that draws it is still there; changing the lever changes the situation.*

Every entry below has the same four parts. **What you hear and see** opens with a sentence someone in such an organization might say, and then gives warning signs you can check without knowing anyone's motives. **Why capable people create it** gives the reasonable choice at the start. **What it costs** names the capacity that runs out and, where there is one, an instance at Corvane. **Where the book treats it** names the chapters. Three notes on where the material comes from. The opening sentences are invented. Corvane is the fictional company this book follows, [[corvane-at-five-sizes]] introduces it, and its numbers are illustrations. Where a pattern comes from a named book, the entry credits the book; the names without a credit, the four families and the placing of each pattern under one lever are my arrangement.

## Boundary Patterns: Who Owns What

The first family traces to the first lever. A boundary says which team owns a thing: a service, a customer journey, a rule. A good boundary follows the work, so that one team can understand and change what it owns. The three boundary patterns are boundaries set by something else: by the reporting chart, by a team's reputation for coping, and by the calendar of disappointing results.

### The Org Chart as Architecture

**What you hear and see.** The first of the three is the boundary set by the chart. "We've moved Mobile under the new director. That should fix the handoffs." The Org Chart as Architecture is a reorganization that changes who reports to whom, or how many people each team has, and leaves what teams own and how they reach each other as it was. Afterwards the same teams wait on the same teams. One feature that a user can see needs changes from several teams. And the announcement says who reports to whom and nothing about who owns what.

**Why capable people create it.** The chart is the one part of the structure a leader can change by a date. Ownership, shared knowledge and working agreements between teams take months to move, and a reporting line takes an announcement. An even split by headcount is also fast, looks fair and needs no argument about what each team should own. Behind the choice stands a common belief, which Morieux and Tollman call the hard approach: that structures, processes and systems have a direct and predictable effect on performance, so that the right boxes produce the right results.

**What it costs.** The organization pays the price of a reorganization, and it pays in attention afterwards. Boundaries that follow headcount instead of the work leave each team needing to understand parts of what other teams own, so ordinary changes become handoffs between teams, and handoffs wait. In 2023, while Corvane was growing toward 180 people, it split its four teams into eleven product teams of about eight by dividing people evenly, and added a platform team of five. By 2024 the median lead time for a change, from starting work on it to its release, had gone from 4 days to 19. About two of the 19 days went into writing the change. The rest was spent waiting on another team.

**Where the book treats it.** [[the-organization-as-a-system]] shows what a reporting line does not change, and [[conways-law-and-the-inverse-conway-maneuver]] when redrawing teams does change the software. [[cognitive-load-and-team-boundaries]] and [[team-types]] draw boundaries from the work instead of the chart.

### The Overloaded Team

**What you hear and see.** Where the first pattern redraws lines too easily, the second never redraws one line while scope keeps arriving on one side of it. "Give it to Core. They always manage." The Overloaded Team is the team that is given each new responsibility because it coped with the last one, until it owns more than its members can hold in mind. Its backlog is longer every week. Most other teams have a request waiting on it. One or two members are the only people able to change parts of what it owns. And the same people describe it as the best team and the slowest.

**Why capable people create it.** It is made one reasonable assignment at a time. Whoever has a new responsibility to place gives it to the team that has proved itself, because that is the safe choice, and each addition is small. Nobody adds up the total. Will Larson's *An Elegant Puzzle* describes four states a team can be in, and the first is the one this team reaches: a team is *falling behind* when its backlog is longer each week than the week before. Larson also notes how such a team looks from outside: "Bottlenecked groups tend to be very helpful, but are trying to do more than they're actually able to do."

**What it costs.** The capacity that runs out is attention. The team's lead time rises, and every team that depends on it waits. In 2022, as Corvane began to grow from 50 people toward 180, its Core team took on a new rule engine for scheduling and job status. Core had six engineers before the change and six after it. It now owned more than it could comfortably understand, and its lead time for other work rose. The same change had relieved Web, Mobile and Integrations, the three teams that had each been building those rules on their own.

**Where the book treats it.** [[cognitive-load-and-team-boundaries]] has the test for when a team owns too much. [[flow-and-the-constraint]] gives Larson's four states and what to add in each, and [[team-size-and-composition]] how large a team can usefully be.

### The Reorg as Strategy

**What you hear and see.** The third boundary pattern is the first one made into a habit. "The structure isn't working. Let's reorganize again in Q3." In The Reorg as Strategy the organization is redrawn each time results disappoint, and no redrawing is ever checked against an outcome. There is more than one reorganization a year. None had a stated outcome, and none was reviewed. The announcement comes before the plan for on-call duty, ownership and work in flight. And nobody can answer a question Larson asks of every reorganization: what will trigger the one after this?

**Why capable people create it.** A reorganization is visible, fast and within a leader's own authority, and a change with no stated outcome cannot be shown to have failed. *Build What Matters* names both halves among its ten dysfunctions: the Roller Coaster, whiplashing changes of direction that come from too short a time horizon, and the Hamster Wheel, output over outcomes. Applying them to reorganizations is my extension, made in [[the-organization-as-a-product]]. A reorganization can also stand in for a harder conversation, and Larson is direct about that case: "There is only one worst kind of reorg: the one you do because you're avoiding a people management issue." Donella Meadows, in *Thinking in Systems*, describes the general trap as shifting the burden: a remedy that relieves the symptom and leaves the underlying problem, so that more of the remedy is needed.

**What it costs.** The capacity spent is attention. Every reorganization resets the working knowledge of who owns what, people have to rebuild it, and sometimes the new chart forgets a duty. Corvane's 2023 reorganization had no stated outcome. When the board asked in 2024, with the company at 180 people, whether it had worked, the leadership team could not answer. In 2025–2026, at 500 people, another reorganization was announced without a plan for moving responsibilities, and two teams lost their on-call rotation. Inside Corvane this second reorganization is known as the Tuesday Reorg.

**Where the book treats it.** [[the-organization-as-a-product]] asks for a stated outcome and the smallest change that would test the diagnosis. [[reorganizations]] covers when to reorganize and how to run one as a migration, and [[scaling-stages]] the signals that a structure has expired.

## Interface Patterns: How Work Crosses Between Teams

Boundaries decide what each team owns. The second lever decides how teams reach across them. An interface is the agreed way work or knowledge crosses from one team to another: an API, a review, a published schema, a meeting. It fails in three ways: as a gate, as a product without users, and by not existing.

### The Review Bottleneck

**What you hear and see.** The first failure is the gate. "It's done. It's just waiting for review." The Review Bottleneck is an interface designed as an approval queue: every change of some kind must pass one team or one board, and that team holds the organization's capacity to verify that kind of change. Finished work waits longer for approval than it took to make. Nearly everything is approved in the end, late. The approving team is praised for rigor and blamed for speed, often in the same meeting.

**Why capable people create it.** After an incident, adding a check is the cheapest safe response, and giving the check to the people who know most is the obvious way to staff it. Each check is reasonable. But the work to be checked grows with every team that is added, and the checkers do not. Larson calls the result the gatekeeper pattern and does not blame the gatekeepers. His advice is to "treat gatekeeping as a significant implementation bug rather than as a stability feature to be emulated." The fault, in other words, is in how the interface was built.

**What it costs.** The pattern uses up verification, the capacity it concentrates. Work ages in the queue, and each increase in what is produced lengthens the wait. At Corvane in 2024, with 180 people, five platform engineers served eleven product teams, and three of those teams needed the platform team for every launch. At the peak 14 launch requests were open. Corvane calls it the Launch Queue, and most of the 19 days of lead time were spent in it. The pattern returned in 2027–2028, at 1,100 people and with coding agents in every team. Merged changes per week rose 2.4 times in a year, review capacity stayed flat, and the median wait for a review went from 5 hours to 31.

**Where the book treats it.** [[flow-and-the-constraint]] finds the step that limits the whole. [[interaction-modes-and-team-apis]] and [[architecture-governance]] replace approval with self-service, advice and guardrails. [[quality-and-reliability]] builds checks into the work, and [[agentic-delivery]] covers verification when agents write the changes.

### The Platform Nobody Asked For

**What you hear and see.** A gate is an interface every team is forced through. The second interface pattern is one that no team comes to. "The platform is ready. Now we need the teams to migrate." The Platform Nobody Asked For is an internal platform, tool or standard built ahead of any team's stated need, and then pushed to teams that have to be made to adopt it. Adoption needs a mandate. Product teams keep their own scripts beside it. Its roadmap lists capabilities and no team's problem. Its builders cannot name the teams they talked to before building, and its success is reported as features shipped.

**Why capable people create it.** Capable engineers see the same problem solved several times over and build the general solution in advance, which is what good engineers are praised for. Research seems unnecessary, because the users are colleagues down the hall. *Build What Matters* has names for both halves of this in product work: the Bridge to Nowhere, "overengineering for future unknowns", and the Ivory Tower, a lack of customer research. Applying them to an internal platform, whose customers are the company's own teams, is my extension.

**What it costs.** A team's attention goes into a product without users, and every other team is handed a migration it did not choose. Corvane's record has no instance of this pattern. Its platform team had the opposite history: it was created to help eleven product teams release faster, and within a year every launch waited on it. That is the previous pattern, so this entry has no Corvane case.

**Where the book treats it.** [[platforms-and-developer-experience]] treats a platform as a product whose users are teams, with an adoption measure. [[team-types]] says when a platform team is justified, and [[migrations-and-technical-debt]] what a migration costs the teams asked to make it. My working record [[platform-as-a-product]] has the practice as a checklist.

### The Unowned Interface

**What you hear and see.** The first two interface patterns are interfaces built wrongly. The third is the crossing for which none was built. "I assumed they knew we had changed it." The Unowned Interface is a place where work or knowledge has to cross between teams and no agreed, owned way exists for it to do so. The same rule is implemented in two teams, with different results. Changes reach other teams after release, through incidents or through customers. And incident reviews end with the word "communication".

**Why capable people create it.** Every team does its own part well, and the crossing is no team's part. Finding out what another team is changing takes effort, the effort falls on the person who asks, and the benefit goes to someone else. Morieux and Tollman call that price an adjustment cost and count it among a person's constraints. Not asking is then the sensible choice. Meadows makes the same point about systems in general: missing information flows are among the most common causes of a system's malfunction.

**What it costs.** What is missing is attention that nobody is in a position to give, because no one holds the whole of what crosses. So the organization gets the same failure repeatedly and blames a person each time. In 2021, at 50 people, Corvane's Web and Mobile teams each implemented the rule for overlapping jobs, and for three weeks planners and technicians saw different schedules. Corvane calls it the Two Calendars. The review found a communication failure, and the Mobile lead was replaced. In 2022 the Mobile and Integrations teams diverged on job-status rules in the same way: a job marked complete on the phone stayed open in customers' billing exports for eleven days.

**Where the book treats it.** [[the-organization-as-a-system]] tells this case in full. [[conways-law-and-the-inverse-conway-maneuver]] predicts which lines between teams need a contract. [[interaction-modes-and-team-apis]] defines the team API, a team's published account of how to work with it, and [[operating-cadence]] covers the meetings and written paths that carry information.

## Decision-Right Patterns: Who Decides

Interfaces carry work and information. Decisions need a lever of their own. A decision right is the agreed answer to who may decide a named kind of question, whose input they must take, and where the decision is written down. Each of the three decision-right patterns puts a decision away from the people who hold the information for it: outside the team, above the team, or with everyone at once.

### The Feature Factory

**What you hear and see.** The first puts the decision outside the team. "Sales needs it for the renewal. Just tell us when it ships." The Feature Factory is a product team that receives a list of features to build, decided by whoever asked for them, and keeps only the decision of how. The roadmap is a list of features with dates and a requester beside each. The team cannot say which customer outcome a feature is meant to change. Nothing that shipped is reviewed, and nothing is removed.

**Why capable people create it.** The name and the mechanism come from *Build What Matters*, where the Feature Factory, "an assembly line of features", is the fifth of the ten dysfunctions. Teams fall into it, the authors write, because customers or internal stakeholders lead them to believe that one more feature will close a deal or keep a customer who might leave. Every request comes from a real customer or a colleague, with revenue attached. Refusing any single one looks worse than building it, so the factory is made one reasonable yes at a time.

**What it costs.** The capacity wasted is judgment. The people who know the product best decide nothing about what it becomes, and nobody learns whether what shipped worked. In one year between 2022 and 2024, while it was growing to 180 people, Corvane shipped forty-one features. Each had been promised to a named customer, and the roadmap was a list of such promises with dates. That year the renewal rate fell.

**Where the book treats it.** [[outcomes-over-output]] covers the ten dysfunctions and the key outcomes that replace them. [[vision-and-product-strategy]] and [[roadmaps-and-horizons]] supply what a team's choices are checked against, and [[discovery-delivery-and-empowered-teams]] says what a team is empowered to decide.

### The Escalation Ladder

**What you hear and see.** In the Feature Factory the decision is taken from the team. On the Escalation Ladder the team sends it away itself. "Let's take it to the leadership meeting." Decisions travel upward until they reach someone senior enough to be safe, and that person has less information than the people who sent them. Routine decisions are made two levels above the work. Teams wait days for answers they could have given themselves, and the same kind of question comes up the ladder again and again.

**Why capable people create it.** It begins as the right arrangement. In a company of twelve the founder decides everything, and should. *Build What Matters* calls the later stage the Throne Room, the founder or chief executive who cannot let go, and adds that "at a certain point, instinct doesn't scale." The ladder persists for a second reason: wherever it is unwritten what a team may decide, escalating is the safe choice for the team. Morieux and Tollman state what is lost. Decisions, they write, should be made as close as possible to where the action takes place and where information is richest. Larson's rule explains why answering escalations does not end them. An escalation that is settled on its own changes no policy, so he treats every escalation as a test case and uses it to update the policy.

**What it costs.** The capacity wasted is judgment: each decision is made late, by the person with the least information about it. Corvane's first named incident is this pattern at its smallest. In 2018–2019, at 12 people, every pricing, design and release decision waited for Tomas Rell, the co-founder and chief technology officer, and the company calls it the Founder Queue. By 2025–2026, at 500 people, Corvane's scarce capacity was judgment, with decisions being made far from their information.

**Where the book treats it.** [[decision-rights-and-decision-records]] covers allocating and recording decisions. [[spans-layers-and-managers-of-managers]] and [[executive-roles-and-reporting-lines]] say what each level keeps, and [[discovery-delivery-and-empowered-teams]] what belongs to the team.

### The Consensus Stall

**What you hear and see.** The first two patterns send a decision to the wrong person. The third sends it to no one person at all. "Let's get everyone aligned before we commit." The Consensus Stall is a decision with no named decider, so that it can be finished only when everyone with a stake agrees. Meetings end by scheduling another meeting. A settled decision is reopened by whoever was absent. People agree in the room and act otherwise afterwards.

**Why capable people create it.** The impulse is a decent one. Asking everyone is respectful, and it protects each person from being wrong alone. Where no decider is named, agreement is also the only way a decision can end. *Build What Matters* calls the product version the Negotiating Table: "trying to keep everyone happy". Patrick Lencioni's *The Five Dysfunctions of a Team* explains why agreement in the room does not hold. His third dysfunction, lack of commitment, follows from the second, fear of conflict: people who have not argued do not commit. He also says what people need in place of consensus: "They just need to be heard, and to know that their input was considered and responded to." A named decider who consults gives them that. Lencioni's subject is trust inside one team, though, and no decision right creates trust; [[trust-conflict-and-psychological-safety]] takes that up.

**What it costs.** The capacity lost is judgment, spread so thin that nobody exercises it. The decision arrives late, and it is the option nobody objected to. At Corvane in 2024, with 180 people, nobody could say who decides that a feature is ready, and at the end of that year the question was still open. In 2025–2026, at 500 people, quarterly planning took nine of the quarter's thirteen weeks. Corvane calls it the Nine-Week Plan. The record gives its length; [[planning]] examines its causes.

**Where the book treats it.** [[decision-rights-and-decision-records]] gives each kind of decision a decider, the people consulted and a record. [[planning]] returns to the Nine-Week Plan, and [[the-product-engineering-design-triad]] covers three functions deciding together.

## Incentive Patterns: What Gets Rewarded

The first three levers set what people can do. The fourth sets what they have reason to do. An incentive is whatever the organization visibly rewards: promotion, recognition, headcount, a leader's attention. The three incentive patterns reward something that is easier to see than the result: output, the items on a career ladder, and rescue. Meadows describes the general form as the trap of seeking the wrong goal, in which a system works obediently toward the indicator it was given.

### The Output Scoreboard

**What you hear and see.** The first is the trap at the scale of the whole organization. "Velocity is up twelve percent this quarter." The Output Scoreboard is an organization that counts and praises what was produced, whether features, story points, hires or a finished reorganization, and does not ask what changed for a customer. It differs from the Feature Factory in its lever: the factory is about who decides what is built, the scoreboard about what is counted afterwards. Reviews report counts of things shipped. A project is called done on its launch day. Dashboards show internal numbers only.

**Why capable people create it.** Output can be counted this week, by one team. An outcome arrives months later and is shared among several teams, and a leader needs something to report now. *Build What Matters* names the two product forms: the Hamster Wheel, "output over outcomes", and the Counting House, an obsession with internal metrics. Meadows explains why nobody has to behave badly for this to happen. A system given an inaccurate goal, she writes, "may obediently work to produce a result that is not really intended or wanted." People deliver what is counted.

**What it costs.** The capacity lost is verification in its second sense, knowing that what was built was worth building. The organization can no longer tell being busy from being effective. Corvane's hiring wave of 2022–2024 was judged by its completion: 95 engineers hired and eleven teams formed. No outcome had been stated. In 2024, at 180 people, the leadership team could not tell the board whether the plan had worked, although every number in it had been met, and the median lead time for a change had gone from 4 days to 19.

**Where the book treats it.** [[the-organization-as-a-product]] separates the outcome of an organizational change from its output, and [[outcomes-over-output]] does the same for the product. [[measuring-engineering]] and [[product-outcomes-and-organizational-health-signals]] cover the measures, and [[measuring-productivity-with-ai]] what happens to them when output becomes cheap.

### The Ladder as Checklist

**What you hear and see.** The second incentive pattern is the same substitution in one person's career. "I need a cross-team project for my promotion case." A career ladder is the written description of what each level of a role requires. The Ladder as Checklist is a ladder read as a list of items to collect, so that people choose work for the evidence it gives a promotion case. New systems are launched and then left without an owner. Managers ask for headcount as the way to the next level. Reviewing, maintaining and mentoring fall to people who do not expect promotion.

**Why capable people create it.** It starts with a good decision: write down what each level requires, so that promotion is fair and not a matter of who is liked. But written criteria favor what can be shown as evidence, such as a launch, a larger scope or a bigger team, and people then sensibly produce that evidence. Meadows calls this rule beating and notes what makes it hard to see: "Notice that rule beating produces the appearance of rules being followed." Morieux and Tollman explain which work loses. It is extremely difficult, they write, to measure who contributes what to cooperation, which is why they advise judgment over metrics there.

**What it costs.** The organization loses the work it needs most and can evidence least: cooperation, upkeep and checking other people's work. Those are the activities that protect attention and supply verification. Corvane introduced a career ladder in 2025–2026, at 500 people, and its record has no incident from it, so this entry has no Corvane case.

**Where the book treats it.** [[career-ladders-and-leveling]] covers what a ladder should and should not specify. [[performance-calibration-and-growing-managers]] covers judgment in promotion decisions, and [[staff-plus-and-architects]] senior work that does not look like a project.

### The Hero Culture

**What you hear and see.** The third is the smallest in scale: a single act of praise. "Thank goodness she was online on Sunday." The Hero Culture is an organization that thanks and promotes the people who rescue it, and so keeps needing rescue. The same few names appear in every incident and every thank-you. What the heroes own is not written down. The same system is rescued repeatedly, and long hours are praised in public.

**Why capable people create it.** The gratitude is deserved, which is what makes the pattern hard to argue with. A rescue is visible. The work that would have made it unnecessary is not. So recognition goes to the first, and nobody has a reason to do the second. Larson's heading for his advice is "Kill your heroes, stop doing it harder", and he gives the reason: "Unless your problem is that people aren't trying hard, the 'work harder' mantra only breeds hero programmers whose heroic ways make it difficult for nonheroes to contribute meaningfully." Lencioni's fifth dysfunction, inattention to results, is the same thing seen inside a team: individual recognition put above the collective result.

**What it costs.** The pattern concentrates attention in one person. The hero becomes a constraint and a single point of failure, and the team cannot work without them. At Corvane in 2021, with 50 people, Samir Haddad, a staff engineer, was the only engineer who understood both the scheduling engine and the mobile sync.

**Where the book treats it.** [[cognitive-load-and-team-boundaries]] reads the one engineer who knows everything as a sign of an overloaded team, and [[flow-and-the-constraint]] as a constraint. [[quality-and-reliability]] covers on-call and incident practice that does not depend on one person, and [[values-operating-principles-and-rituals]] what the organization praises in public.

## The Twelve Patterns at a Glance

That is the catalogue. The table puts the twelve in one place, each with its family, one warning sign and the chapters to start with. Read it from the warning sign: find what you are seeing, read across to the family, and you have the lever to look at before you look at the people.

| Pattern | Family | Warning sign | Chapters |
| --- | --- | --- | --- |
| **The Org Chart as Architecture** | Boundaries | After a reorganization the same teams wait on the same teams | [[the-organization-as-a-system]], [[conways-law-and-the-inverse-conway-maneuver]], [[team-types]] |
| **The Overloaded Team** | Boundaries | One team's backlog grows every week and most other teams wait on it | [[cognitive-load-and-team-boundaries]], [[flow-and-the-constraint]] |
| **The Reorg as Strategy** | Boundaries | More than one reorganization a year, none with a stated outcome | [[the-organization-as-a-product]], [[reorganizations]] |
| **The Review Bottleneck** | Interfaces | Finished work waits longer for approval than it took to make | [[flow-and-the-constraint]], [[architecture-governance]], [[agentic-delivery]] |
| **The Platform Nobody Asked For** | Interfaces | Adoption of an internal platform needs a mandate | [[platforms-and-developer-experience]], [[team-types]] |
| **The Unowned Interface** | Interfaces | The same rule is built twice, and incident reviews end with "communication" | [[the-organization-as-a-system]], [[interaction-modes-and-team-apis]] |
| **The Feature Factory** | Decision rights | The roadmap is a list of features, each with a requester and a date | [[outcomes-over-output]], [[discovery-delivery-and-empowered-teams]] |
| **The Escalation Ladder** | Decision rights | Routine decisions are made two levels above the work | [[decision-rights-and-decision-records]], [[spans-layers-and-managers-of-managers]] |
| **The Consensus Stall** | Decision rights | Meetings end with another meeting, and settled decisions reopen | [[decision-rights-and-decision-records]], [[planning]] |
| **The Output Scoreboard** | Incentives | Reviews count what shipped and nobody asks what changed | [[outcomes-over-output]], [[measuring-engineering]] |
| **The Ladder as Checklist** | Incentives | Projects are chosen for promotion cases | [[career-ladders-and-leveling]], [[performance-calibration-and-growing-managers]] |
| **The Hero Culture** | Incentives | The same few names are in every incident and every thank-you | [[cognitive-load-and-team-boundaries]], [[quality-and-reliability]] |

One Corvane incident shows how the table is used, and why it is usually used more than once. The Launch Queue of 2024, at 180 people, was a Review Bottleneck at the platform team. Behind it stood two more patterns: teams cut by headcount, which is the Org Chart as Architecture, and a decision on readiness that belonged to nobody. A real incident usually shows several patterns at once, and naming each one separates the levers, so that one lever can be changed and its effect measured before the next. Dario Vance, Corvane's VP of Engineering, changed the interface and nothing else. He gave one team, Scheduling, a release path it could run without the platform team. After one quarter Scheduling's median lead time was 6 days. Company-wide the median went from 19 days to 8 within two quarters and to under 7 a quarter later. The eleven teams were not re-cut. Compare the Two Calendars, where a person was replaced and the failure returned.

## What to Take Away

**Established.** What the sources agree on:

- Behavior at work is a rational response to goals, resources and constraints, so it changes when the context changes (Morieux and Tollman, *Six Simple Rules*).
- A system given the wrong goal, or rigid rules, produces the wrong result or the appearance of compliance without anyone behaving unreasonably (Meadows, *Thinking in Systems*: seeking the wrong goal, rule beating).
- Product organizations share a short list of named dysfunctions, and teams pass through recognizable states (Foster and Nerlikar, *Build What Matters*; Larson, *An Elegant Puzzle*).

**Depends on context.** What changes with the situation:

- A warning sign is a prompt to look, not a verdict. A founder deciding everything is the right design at twelve people and the Escalation Ladder at five hundred.
- A sign can trace to a missing condition instead of a lever. If the decider is named and people still do not commit, the gap may be trust, which is Lencioni's subject and which no redesign supplies.
- Some review, some escalation and some consensus are right. The pattern is present when the queue, the ladder or the meeting is where most of the time goes.

**The author's synthesis.** What is this book's own position:

- The four families and the placing of each pattern under one lever are my arrangement. Several patterns touch more than one lever, and I placed each under the lever I would change first.
- The Feature Factory is named by *Build What Matters*. The other eleven names are mine, with the sources credited in each entry for the mechanism.
- That each pattern begins as a locally reasonable choice is my reading of those sources and the argument of this page. I have not shown it with data.

## Checklist

Read together, the twelve patterns are four questions that were answered once and never asked again: whose is this, how do they find out, who says yes, and what gets rewarded. Each pattern is what an organization looks like when one of those answers has outlived the situation it was given for. So the useful response to a pattern is to ask its question again and change that answer, before changing the people caught in it. Take one recurring problem in your organization and run these eight steps on it.

- [ ] Describe what happens without a motive: what waits, where, and how often.
- [ ] Find the closest warning sign in the table and name the pattern. If two fit, keep both.
- [ ] Name the lever: boundary, interface, decision right or incentive.
- [ ] Ask the lever's question again: whose is this, how do they find out, who says yes, what gets rewarded?
- [ ] Find the reasonable choice that created the situation, and ask whether its reason still holds.
- [ ] Name the capacity that is running out: attention, judgment or verification.
- [ ] Check whether the last remedy changed a person or the lever, and whether the problem came back.
- [ ] Read the chapters in the table's last column before deciding what to change.

Tolstoy's sentence was about families. Organizations are unhappy in a small number of shared ways, and you can now name twelve of them and the lever behind each. So far the patterns have appeared one at a time, each with a fragment of one company's history. The next page puts the fragments together. It introduces Corvane, one fictional company in which the patterns appear in turn as it grows from 12 people to about 1,100: [[corvane-at-five-sizes]].

## Sources and Evidence

**Books**

- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. The ten dysfunctions of product management, eight of which are credited in the entries; the name and mechanism of the Feature Factory; the Tolstoy epigraph.
- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. The four team states; the gatekeeper pattern; the worst kind of reorganization; escalations as inputs to policy; heroes.
- *Thinking in Systems: A Primer*, Donella H. Meadows, edited by Diana Wright, 2008. The system traps of seeking the wrong goal, rule beating and shifting the burden; missing information flows.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. Behavior as a rational solution in a context; adjustment costs; the hard approach; judgment over metrics.
- *The Five Dysfunctions of a Team*, Patrick Lencioni, 2002. Fear of conflict and lack of commitment, used for the Consensus Stall; inattention to results, used for the Hero Culture.

**Practitioner sources**

- The author's working records: [[dysfunctions]], a summary of the *Build What Matters* dysfunctions, and [[platform-as-a-product]].
- The four families and the assignment of each pattern to one lever are the author's. The sentences that open each entry are invented.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
