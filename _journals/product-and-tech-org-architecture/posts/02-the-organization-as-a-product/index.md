---
title: "The Organization as a Product: Who It Serves and What It Owes Them"
date: 2026-11-19
author: Željko Obrenović
excerpt: "If an organization is a system that can be architected, whom is it architected for, and how should the work of changing it be run? For its users, and as product work: discovery first, an outcome to judge by, and the smallest change that tests the diagnosis."
permalink: the-organization-as-a-product
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn who the users of an organization's design are, and how to run a change to it the way a product team runs a change to a product.

> **KEY POINTS:**
>
> * **An organization has users, and it owes them outcomes.** The users are the people and teams inside a structure, the teams that depend on each team, and through them the customers.
> * **A finished reorganization is output.** Whether it worked is a separate question, and only an outcome stated before the change can answer it.
> * **Changing an organization is product work.** Discover the problem, state the outcome, place it on a roadmap toward a vision of the organization, make the smallest change that tests the diagnosis, and review the outcome.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Reorg as Strategy** — a reorganization with no stated outcome can only be followed by another one.
> * **The Output Scoreboard** — judging an organizational change by its completion is the same error as judging a team by what it ships.

<br>

Between 2022 and 2024 Corvane, the fictional company this book follows, doubled its engineers from 45 to 95 and reorganized them into eleven product teams. The reorganization was announced, staffed and finished on schedule. Over the same period the **lead time** for a change, the time from starting work on it to its release to customers, went from 4 days to 19. When the board asked whether the reorganization had worked, nobody could answer. Nobody had written down **what working would mean**.

If you build products, you would not ship a feature without knowing who it is for and how you would know it worked. You have probably also lived through a reorganization that had neither. The organization is the one product its leaders build without applying their own discipline to it. This chapter applies it. Its claim is that an organization is architected for its **users**, the people and teams who work in it and the teams and customers who depend on each team, and that it owes them **outcomes**. Changing it is therefore product work. The chapter starts with the users, moves to the difference between the output and the outcome of an organizational change, and shows the product dysfunctions that follow when both are ignored. It then sets out a five-step way of running a change and the one-page brief that holds it, says where the product analogy stops, runs Corvane's case again, and ends with what AI changes.

## Setting the Scene: A Reorganization That Shipped

In 2022 Corvane had 45 engineers in four teams and a backlog that grew faster than the teams could ship. Its leaders concluded that the company needed more engineers in more teams. The plan was to hire up to 95 engineers and to split the four teams into eleven product teams of about eight people each, with a platform team of five to provide the shared release tooling. Corvane later called this plan the hiring wave. Nobody had asked the teams where their work waited, and when Dario Vance joined as VP Engineering in 2023, the diagnosis and the solution were already agreed.

The plan was carried out well. The hires were made. The eleven product teams and the platform team were formed in two waves in 2023, by dividing people evenly. The new structure was announced on the planned date, and every team had a lead and a name. By the only measure the plan contained, completion, the change succeeded.

A year later the picture was different. Lead time had gone from 4 days to 19. All eleven product teams needed the platform team for some of their launches, three of them needed it for every launch, and at the peak in 2024 the platform team had 14 launch requests open. The leadership team disagreed about whether the reorganization had helped, hurt or made no difference. They could not settle it, because no outcome had been stated in 2022 against which the result could be judged. A worse result could not even be called a failure of the change.

## Who the Organization Is For: Three Rings of Users

The hiring wave was designed without asking anyone it affected, and the first question is who should have been asked. A **user** of an organizational design is anyone whose work the design makes easier or harder. There are three rings of them, and each has its own way of being heard. The rings are counted from the structure you are changing, so the same team can be in the inner ring of one change and in the middle ring of another.

| Ring | Who | What they need from the design | How you hear from them |
| --- | --- | --- | --- |
| Inner | The people and the team inside a structure | Work they can understand and finish; decisions they are allowed to make | Interviews; their own account of a working week |
| Middle | The teams that depend on that team | A way to get what they need without queueing | Wait times, dependency lists, their complaints |
| Outer | Customers | A product that is coherent and keeps improving | The product's own outcome measures |

The inner ring is the one leaders most often speak for without asking. The people in a team know what their structure costs them better than anyone above it, and that knowledge rarely travels upward by itself. In *Six Simple Rules*, Yves Morieux and Peter Tollman make understanding what people actually do their first rule, and they argue that executive teams compete first on the accuracy of their insight into their own organization. A leader's picture of the inner ring is the scarce input to any redesign.

The middle and outer rings experience the design through its interfaces. The previous chapter defined an interface as the agreed way in which work and knowledge cross between teams. The team on the consuming side of an interface is its user, in the same sense that developers are the users of a platform, and it is the one that can say whether the interface works. Customers stand one step further out. They never see the organization, and they meet its design as a product that is coherent across its parts or is not.

One party is missing from the table: the business that funds the organization. It is a stakeholder with outcomes of its own, such as revenue and cost, and it is served through the users, not instead of them. This follows a distinction in *Build What Matters*, where Ben Foster and Rajesh Nerlikar separate the key customer outcome from the key business outcome and argue that business results follow when customers get the outcome they care about. Applying that distinction to the organization itself is my extension, not their claim: the owners are served when the three rings are.

## Output and Outcome of an Organizational Change

Knowing who the users are leads to what the organization owes them. Product management has precise words for this. It distinguishes what a team ships, the **output**, from what changes for the customer because of it, the **outcome**. Melissa Perri gives the failure a name in *Escaping the Build Trap*: "The build trap is when organizations become stuck measuring their success by outputs rather than outcomes." Foster and Nerlikar open their list of product dysfunctions with the same failure, the Hamster Wheel, a team focused on hitting deadlines with little regard for what the work achieves.

An organizational change has the same two sides, and a completion date measures only the first. The table gives four common changes with both sides and a measure a leader could collect.

| Change | Output (it shipped) | Outcome (it worked) | A measure |
| --- | --- | --- | --- |
| Split one team into two | Two teams exist, each with a lead | Each team changes its area without waiting for the other | Lead time; time spent waiting on the other team |
| Create a platform team | The team is staffed and has a roadmap | Product teams release without asking anyone | Share of launches that need a platform ticket |
| Add a layer of directors | Directors are appointed | Decisions are made closer to the teams, and faster | How long a decision waits; how many reach the VP |
| Introduce quarterly planning | The plan is published | Teams work on what was planned, and it mattered | Share of planned outcomes reached |

What the four have in common gives the definition this book uses. An outcome of an organizational change is a change in what its users can do, stated before the change, with one measure and a date. Foster and Nerlikar call the key outcome the "metric of progress", the way to know whether a product is delivering value. I take that idea and point it at the organization, which again is my extension of theirs.

## The Product Dysfunctions, in Organization Design

If organizational changes have outputs and outcomes as products do, they should fail in the ways product work fails. They do. Foster and Nerlikar list ten dysfunctions of product management and group them under themes, the first of which is an internal focus that draws attention away from the customer. That theme transfers along with the symptoms: in organization design, too, the designers' attention is on the structure and on themselves, and off the people the structure is for. Five of the ten describe, with nothing changed but the object, how organizations are commonly redesigned. The left two columns are theirs; the right column is mine.

| Dysfunction (*Build What Matters*) | In product work | In organization design |
| --- | --- | --- |
| The Hamster Wheel | Output over outcomes; hitting deadlines | The reorganization judged by its completion date |
| The Ivory Tower | Lack of customer research | A structure drawn by people who have not talked to the teams in it |
| The Roller Coaster | Twists and turns from a time horizon that is too short | A reorganization every year, each undoing the last |
| The Throne Room | Whipsaw decisions from the person in charge | A structure that follows the newest executive's last company |
| The Negotiating Table | Trying to keep everyone happy | A structure that gives each leader the scope they asked for |

One of this book's own failure patterns turns out to be two of these together. **The Reorg as Strategy**, the habit of reorganizing whenever results disappoint, is the Roller Coaster and the Hamster Wheel at once: repeated change, with each instance judged only by being done. Corvane's hiring wave was a Hamster Wheel with an Ivory Tower behind it: judged by its completion, and drawn without talking to the teams.

## Pattern: Run the Change as Product Work

Organization design fails as product work fails, so the remedy is to do it the way product work is done well. An organizational change run as product work has five steps, and they form the loop a product team runs. The user of this pattern is the leader who owns the change, and its outcome measure is simple: for each change made, whether a stated outcome was reached and reviewed.

---begin mermaid---
flowchart LR
    D["Discovery"] --> O["Outcome and measure"]
    O --> R["Place on the roadmap"]
    V["Vision of the organization"] --> R
    R --> S["Smallest change"]
    S --> W["Outcome review"]
    W --> D
---end mermaid---

**Figure 1:** *Five steps of running an organizational change as product work: each change starts from discovery, is placed against a vision of the organization, and returns to discovery through its review.*

The first step is **discovery**: finding out what the problem is, from the people in the flow, before choosing a structure. It begins with whether the problem is structural at all. In *An Elegant Puzzle*, Will Larson makes this the first step of planning any organizational change: validate that a reorganization is the right tool, by asking whether the problem is structural, whether you are working around a broken relationship, and whether the conditions are temporary. He adds that "most poor working relationships are the by-product of information gaps", which a new org chart does not close. Discovery also has a known way of going wrong. Perri describes the product manager as "waiter", who asks customers what they want, gets a solution in reply and builds it. Asking teams which structure they want is the same error. Discovery asks about the work: where it waits, what they cannot decide, what they do not understand.

The second step turns discovery into an **outcome**, stated before the design, with one measure and a date. The order matters. A structure can be compared with its alternatives only against a stated outcome. Without one, any structure that gets completed counts as a success, and the choice among structures falls to preference and politics.

The third step gives that outcome a **place on a roadmap**. The roadmap works backward from a vision of the organization, and the vision is described from the users' side: what a week in a team looks like when the design works. Foster and Nerlikar insist that a product vision is not a list of features but an expression of how the customer will get value, and that the strategy works backward from it through key steps and measurable milestones. Carried over to the organization, which is my extension of their method, a vision is not a target org chart. It is a description such as "a team can take a customer problem from idea to release without waiting for another team". Placing an outcome on the roadmap makes this change one step toward something, and stops it from being an event.

The fourth step is the **smallest change** that tests the diagnosis, preferred to the full redesign. After discovery the diagnosis is still an assumption. Perri calls such things known unknowns: assumptions to test, which discovery and experimentation turn into facts before you build. For an organization, the smallest change is often one team, one interface or one decision changed for a fixed period, with everyone told that it is a test.

The fifth step, the **outcome review**, closes the loop. Some months after the change, it compares the measure with what was stated and decides whether to keep, extend or reverse the change. Among Larson's questions to ask before committing to a reorganization is one that points here: "What will trigger the reorg after this one?" The brief answers it in advance, with a failure criterion. The review checks that answer against a measurement, and what it finds feeds the next round of discovery.

## The One-Page Change Brief

The five steps fit on one page, which I call the change brief. It has six fields: two for discovery, one each for the outcome, the place on the roadmap and the smallest change, and one for failure and review. Each field blocks a common shortcut.

| Field | What goes in it | The shortcut it blocks |
| --- | --- | --- |
| Users | Which teams and people, in which ring | Designing for the leaders' convenience |
| Problem as discovered | What the users said and what the data shows, in their terms | Starting from a solution |
| Outcome and measure | One measure, its value today, the target, the date | Judging by completion |
| Place on the roadmap | Which step toward the vision this is, and what it makes possible next | The one-off reorganization |
| Smallest change | The least that would test the diagnosis, for how long, and whether it can be reversed | The full redesign as first move |
| Failure and review | The result that would make you reverse it; the review date and who reports | Keeping a change because it was announced |

The brief is written before any structure is drawn, by the leader who owns the change. My rule is that a change that cannot fill the page is postponed. Each empty field marks something that has not been found out or decided: no users means no discovery was done, no measure means there is no outcome, and no failure criterion means the change can never be reversed on evidence. An unfilled brief is a reason to wait.

## Where the Analogy Stops

The strongest objection to all this has two parts: that treating reorganizations as experiments produces change fatigue, and that treating employees as users hands the leader's decision to them. The objection is right about the first part, what repeated change costs people. Larson treats that cost as a first-order constraint: before committing, he asks whether the new structure will last at least six months, and he calls accidentally missing someone "the cardinal sin of reorganization": a person who learns from the announcement that they have no team or no manager. Every further change runs that risk again. An organization is made of people's working lives in a way that a product is not.

The cost of change to people is one of three differences from a product that limit the analogy. The table lists all three, and each changes how a step of the pattern is run.

| A product | An organization | What changes in the method |
| --- | --- | --- |
| Users can stop using it | Users are employees; leaving is costly and slow | Their feedback is quieter, so discovery has to go and get it |
| A test can be shown to a sample and withdrawn | A test changes someone's team, manager or on-call duty, and some changes cannot be undone | Fewer, longer tests; prefer reversible ones; say in advance that it is a test and what happens after |
| Research can be open | Some changes involve people's jobs or pay | Discovery about the work is open; decisions about individuals are not put to a vote |

The objection is wrong about its second part. Running change as product work does not move the decision to the users. The leader still decides, as a product manager does, and deciding by trying to satisfy everyone is itself one of the dysfunctions, the Negotiating Table. Perri says of customers that it is not their job to come up with their own solutions. The same holds for teams. Discovery gives the leader the problem. It does not hand over the decision.

## Worked Example: The Hiring Wave, Run Again

Corvane's case can now be run through the method and within its limits. In 2024 Dario Vance, the VP Engineering, wrote the brief the hiring wave never had. He began by interviewing every team lead and reading the launch log.

| Field | Corvane, 2024 |
| --- | --- |
| Users | The platform team, whose release path is the structure being changed (inner ring), and the eleven product teams that depend on it (middle ring) |
| Problem as discovered | A change is written in about two days and then waits; 14 launch requests are open at the platform team; five platform engineers serve eleven teams |
| Outcome and measure | Median lead time for a change from 19 days to under 7 within two quarters |
| Place on the roadmap | First step toward "a team releases its own work without waiting for another team" |
| Smallest change | A release path that one team, Scheduling, can run without the platform team, for one quarter; reversible |
| Failure and review | Scheduling's lead time still above 10 days after the quarter, which would mean the wait for launches was not the main cause; Lena Brandt, who leads the platform team, reports |

Writing the brief changed the diagnosis. The 2022 plan had assumed that Corvane had too few engineers. The interviews and the launch log showed something else: of the 19 days, about two went into writing a change, and the rest went into waiting for a launch slot, the platform team's scheduled release of the change. The original solution, more engineers, had added capacity to the step that was already fast.

The new diagnosis set the outcome and the test. The outcome was the one in the brief: median lead time under 7 days within two quarters. The test did not touch the eleven teams. It gave one of them, Scheduling, a way to release without the platform team for one quarter, with a failure criterion agreed in advance.

After that quarter Scheduling's median lead time was 6 days. The test had confirmed the diagnosis, and Corvane began extending the release path to the other ten teams, a few teams at a time, over the following two quarters. It did not re-cut the eleven teams, which is what the leadership team had been preparing to do. The smallest change made the larger reorganization unnecessary.

One team's result is not the outcome the brief had promised. At the review two quarters after the brief, with that rollout half done, the median lead time across all eleven teams was 8 days. That was far better than 19 and still short of the target of under 7. Because the brief had stated the target, the miss was visible, and the review had something to decide: keep going, since four teams were not yet on the new release path. The median went under 7 a quarter later, when the last of them were.

The same review showed what the change had not settled. The teams were still cut by headcount and not by what each could understand, and nobody yet decided when a feature was ready. Those two became the next entries on Corvane's roadmap for its own organization, and later chapters return to both.

## What AI Changes Here

Corvane's brief dates from 2024, and the method has to hold when agents do part of the work. Claims about AI in this book carry one of three labels: Proven, Emerging or Speculative. **Emerging.** As of November 2026, in the teams I have observed adopting coding agents, the division of work inside the team changed within months, with no organizational change announced. Teams change their own way of working faster than a leader's picture of them is refreshed. A design based on last year's picture is then aimed at work that is no longer done that way, so discovery has to be repeated more often. This is my observation, not a measured result.

Agents change how teams work because they shorten the time it takes to produce a software change, and that has a possible effect on the brief itself. **Speculative.** If producing a software change takes less time, the outcome measures of organizational changes will shift from how fast work is produced to how long it waits for a decision or a check. The claim follows from the argument of Part XI, in [[where-the-constraint-moves]]. It would be confirmed where teams report that waiting for review and for decisions, and no longer the time to build, makes up most of their lead time.

## What to Take Away

**Established.** What the sources agree on:

- In product work, success is measured by outcomes and not outputs (Perri, *Escaping the Build Trap*; Foster and Nerlikar, *Build What Matters*).
- Problems are discovered before solutions are chosen, and the user is not asked to supply the solution (Perri).
- A reorganization is first validated as the right tool for the problem (Larson, *An Elegant Puzzle*).

**Depends on context.** What changes with the situation:

- How small the smallest change can be depends on whether the change can be reversed. A release path for one team can be withdrawn; a merged department cannot.
- How open discovery can be depends on whether the change touches people's jobs. Questions about the work are open; decisions about individuals are not.

**The author's synthesis.** What is this book's own position:

- Treating the organization itself as the product, with three rings of users and a one-page change brief, is my extension of those sources. None of them makes that claim.
- The previous chapter said what can be changed, and this one says for whom and how. The four levers are the means and the users' outcomes are the end. A change that names a lever without a user and an outcome is output.

## Checklist

The checklist is the change brief turned into eight questions. Ask them of the next organizational change you plan, before any structure is drawn and before anything is announced.

- [ ] Users: which teams and people does this change serve, and in which ring are they?
- [ ] Discovery: have you heard about the work from the people in the flow, and looked at where it waits?
- [ ] Is the problem structural, or is it a relationship, an information gap or a temporary condition?
- [ ] Outcome: what will the users be able to do afterwards, with which measure, what value today, what target and by when?
- [ ] Roadmap: which step toward your vision of the organization is this, and what does it make possible next?
- [ ] Smallest change: what is the least you could change to test the diagnosis, for how long, and can it be reversed?
- [ ] Failure: which result would make you reverse it?
- [ ] Review: on what date, and who reports?

Corvane's board asked whether the hiring wave had worked, and nobody could answer. You can now say why: the plan named a structure and a date, and it named no user and no outcome. With the system described and the way of changing it set out, the next chapter turns to the first consequence of how teams are arranged, which is that the software they build takes their shape: [[conways-law-and-the-inverse-conway-maneuver]].

## Sources and Evidence

**Books**

- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. The ten dysfunctions of product management and their themes; key customer and business outcomes; the vision as the customer's view; strategy working backward from the vision. Their application to organization design is the author's.
- *Escaping the Build Trap*, Melissa Perri, 2018. The build trap; outputs and outcomes; the waiter archetype; known unknowns and discovery.
- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. Validating that organizational change is the right tool; the questions to ask before committing; the cost of reorganization to people.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. Understanding what people do; executives' insight into their own organization.

**Practitioner sources**

- The author's working checklists on product dysfunctions and outcomes: [[dysfunctions]] and [[outcomes]].
- The statements about coding agents under "What AI Changes Here" are the author's observation as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
