---
title: "Team Types: Stream-Aligned, Platform, Enabling, Complicated-Subsystem"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Which kinds of teams does an organization need, and when is each one justified? Four kinds are enough: teams that own a flow of user value end to end, and three kinds that are worth having only when they lower the load or the waiting of the first."
permalink: team-types
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn the four team types and a test for deciding whether a proposed or an existing team should exist.

> **KEY POINTS:**
>
> * **Stream-aligned teams are the default.** A team that owns one flow of user value end to end has no hand-off inside that flow, and hand-offs are where work waits.
> * **Three other types exist to serve them.** A platform team carries shared mechanics once, an enabling team closes a skill gap and leaves, and a complicated-subsystem team holds rare knowledge. Each is justified only by lower load or less waiting for stream-aligned teams.
> * **A team that fits none of the four adds a hand-off.** A QA or release team that does one step of every stream's work becomes a queue. Fold it into the streams or turn it into one of the three serving types.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Review Bottleneck** — a functional QA or release team is an approval queue placed inside every stream.
> * **The Platform Nobody Asked For** — the chapter's conditions for a platform team start from mechanics that several teams already repeat.
> * **The Overloaded Team** — a stream-aligned team with nothing taken off it carries more than it can understand.

<br>

In one month of 2024, three requests for a new team reached Dario Vance, the VP Engineering of Corvane. Corvane is the fictional company this book follows, and that year it had 180 people, eleven product teams and a platform team of five. Two engineering managers wanted a QA team of six testers to check every release. The manager of the Scheduling team wanted three specialists for travel-time estimation. Lena Brandt, who led the platform team, wanted a second platform team for test environments. Each request came with a good reason. If you have approved a team that sounded sensible and later found other teams waiting on it, you know the difficulty. Corvane had no way of telling **a team that would help from one that would become the next queue**.

This chapter supplies a way of telling them apart. It argues that an organization needs four kinds of team. **Stream-aligned teams** own a flow of user value end to end. The other three kinds exist for them: **platform teams** remove mechanics they would otherwise each carry, **enabling teams** close a skill gap and then leave, and **complicated-subsystem teams** hold knowledge too specialized to spread. Each of the three is justified only when it lowers the load or the waiting of stream-aligned teams, and a team that fits none of the four, such as a QA team that tests everybody's releases, adds a hand-off inside the stream. The chapter starts with the three requests, says why the stream-aligned team is the default, and takes the platform, enabling and complicated-subsystem teams one by one, each with the conditions that justify it. It then looks at teams that fit no type, maps the team types of two product-management books onto the four, turns the types into a procedure, decides Corvane's three requests and ends with what AI changes.

## Setting the Scene: Three Requests in One Month

The requests arrived in the quarter after Corvane's Scheduling team had first released a change without the platform team, and they came from three directions.

| Request | Asked by | Reason given |
| --- | --- | --- |
| A QA team of six testers who test every release before it goes out | Two engineering managers | Product teams were starting to release without a platform engineer's check, and someone independent should test |
| A travel-time team of three specialists | The manager of the Scheduling team | Travel-time estimation is hard, it is built on map data and a routing library, and it distracts the team from scheduling rules |
| A second platform team of four, for test environments | Lena Brandt | Seven of the eleven product teams maintain their own scripts for setting up a test environment |

Every reason in the table was true, and Dario Vance had learned what a true reason is worth. The platform team itself had been a reasonable request. It was formed to help the product teams release faster, and by 2024 launches waited on it, fourteen at the peak: the median lead time for a change, from starting work to release, had gone from 4 days to 19. Corvane spent much of 2024 removing that queue, which earlier chapters call the launch queue, by giving the product teams a release path they could run themselves, as [[the-organization-as-a-product]] tells. What Vance lacked was a way to say, before anyone was hired, what three more teams would do to the eleven teams that deliver to customers.

## Stream-Aligned Teams: The Default

Such a way exists. In *Team Topologies*, Matthew Skelton and Manuel Pais argue that an organization needs only four types of team: stream-aligned, platform, enabling and complicated-subsystem. The other three are defined by the first. The authors define its central word: "A “stream” is the continuous flow of work aligned to a business domain or organizational capability." A **stream-aligned team** owns one such flow for its users, from the idea for a change to running that change in production, and keeps it for years and not for the length of a project. At Corvane, Scheduling is a stream: planners assign jobs to technicians, and one team owns everything that changes for them.

This type is the default because of what it leaves out. Work that passes from one team to another waits at the crossing, and [[flow-and-the-constraint]] showed that such waiting is usually most of the time a change takes. A crossing is also where no one holds the whole outcome, which is how planners and technicians came to see different schedules at Corvane in 2021, at 50 people ([[the-organization-as-a-system]]). A team that owns its stream end to end has no crossing inside the stream. Skelton and Pais ask of any team design how it reduces or avoids handovers between teams in the main flow of change. Most teams in an organization should therefore be of this type.

End-to-end ownership has a price, though: everything the stream needs has to fit inside one team. I keep a working checklist of *Team Topologies*, drawn from the book and linked under Sources, and cite it where my notes are thin. As that checklist records it, a stream-aligned team needs product management, design, development, testing, user experience, security, infrastructure and operability, and monitoring, with the caution that a capability is not the same thing as a dedicated specialist. No team of eight holds all of that in depth beside its own domain. [[cognitive-load-and-team-boundaries]] showed that what a team can understand has a limit, and a team pushed past it is **The Overloaded Team**: it stops owning parts of what it was given. Something has to be taken off the stream-aligned team, without taking a step of its stream away from it.

Three other team types exist to do that, and each takes off a different thing. A platform team takes off mechanics that every team repeats. An enabling team takes off a skill gap, by closing it. A complicated-subsystem team takes off knowledge too rare to spread. None of the three delivers to users, so each has to answer the same two questions: **whose load falls, and whose waiting falls?** In *Team Topologies* the three exist to support the stream-aligned teams and to reduce their cognitive load, which is the total a team has to hold in mind. The second question, about waiting, is my extension, and it rests on [[flow-and-the-constraint]]: a serving team that lowers load and adds a queue has only moved the cost, as Corvane's platform team did.

---begin mermaid---
flowchart TB
    P["Platform team"] -->|"takes off: mechanics every team repeats"| S["Stream-aligned teams: each owns one flow of user value"]
    E["Enabling team"] -->|"takes off: a skill gap, then leaves"| S
    C["Complicated-subsystem team"] -->|"takes off: rare specialist knowledge"| S
    S -->|"delivers"| U["Users"]
---end mermaid---

**Figure 1:** *Only stream-aligned teams deliver to users; each of the other three types is defined by what it takes off them.*

## Platform Teams: Mechanics Carried Once

The first of the three is the one most companies create first. A **platform team** owns internal services and tools that stream-aligned teams use in doing their own work: release pipelines, test and production environments, monitoring, shared data stores. The platform team builds and maintains these mechanics once. What it owns makes it a platform team. Whether it helps depends on how it is used, and Skelton and Pais write: "The platform team’s knowledge is best made available via self-service capabilities via a web portal and/or programmable API". **Self-service** means that a team can use the platform without filing a request and waiting for a person. Corvane's platform team has held the product teams' deployment scripts and the shared data model since 2023, when the company grew to 95 engineers.

A platform team is justified when two things hold: several stream-aligned teams repeat the same mechanics, and the platform can hand those mechanics over as self-service. It should not be created in three cases. The first is when only one or two teams carry the mechanics. My rule of thumb is three teams or more; below that a shared script costs less than a team. The second is when no team has asked, which produces **The Platform Nobody Asked For**: a platform built ahead of any stated need that then needs a mandate to be adopted. The third is when the team could only work by request, because, as [[cognitive-load-and-team-boundaries]] showed, such a platform exchanges load for a queue. The **users** of a platform team are the stream-aligned teams. Its **outcome measures** are the share of uses completed without a request to the platform team, and the stream-aligned teams' lead time. How a platform is run and judged as a product is the subject of [[platforms-and-developer-experience]].

## Enabling Teams: A Skill Gap Closed, Then an Exit

Some load cannot be handed to a platform, because the team has to hold it itself: a skill. An **enabling team** is a small group of specialists in one area, such as test automation, security or performance, who work with a stream-aligned team for a limited time so that the team can afterwards do the work alone. It owns no part of the product. In the checklist the type has three marks: it helps teams learn and does not take the work over, it aims at the autonomy of the teams it helps, and it works with each for a limited period. Corvane did enabling work in 2024 before it had such a team. A platform engineer sat with the Scheduling team for the first six weeks of the new release path, until Scheduling could run it alone, and then went back.

An enabling team is justified when several stream-aligned teams lack the same skill and the skill can be learned. It should not be created when the specialists would go on doing the work for the teams, because then every team waits for them and none learns. It should not be created for a gap in a single team, where training inside that team is cheaper, or without an end date for each engagement. The **user** is the stream-aligned team being helped. The **outcome measure** is whether that team does the work without the enabling team a quarter after the engagement ends, and for the enabling team itself, the number of engagements it has ended. My own record of the type, [[four-fundamental-team-topologies]], puts it bluntly: a permanent dependency on an enabling team is a failure of the enabling team.

## Complicated-Subsystem Teams: Knowledge Too Rare to Spread

A skill of that kind can be learned in weeks. Some knowledge cannot, and the third serving type holds it. A **complicated-subsystem team** owns one bounded part of the system that cannot be changed safely without specialist knowledge. Skelton and Pais give its purpose: "The goal of this team is to reduce the cognitive load of stream-aligned teams working on systems that include or use the complicated subsystem." They add that the expertise is typically hard to find or grow. The checklist gives a video processing engine and a financial reconciliation engine as examples. What defines the type is the rarity of the knowledge. Code that is old, large or disliked is not a complicated subsystem.

Two conditions justify such a team. The first is the source's: the knowledge is rare and slow to grow, so that most members of a stream-aligned team could not change the part safely and could not learn to within a few months. The second is my extension, built on the count of crossing changes in [[cognitive-load-and-team-boundaries]]: most changes to the part must be possible without a stream-aligned team, and most changes to the streams without the specialists. Otherwise the new line is crossed every day. So do not create the team for code that is only unfamiliar, for knowledge an engineer picks up on the job, or where most changes would need both teams. Even a justified team of this type adds a hand-off for the changes that do cross the line, so an organization should have few. The **users** are the stream-aligned teams that use the subsystem. The **outcome measures** are the share of their changes that need the subsystem team, and how long those changes wait.

The three serving types can now be put side by side: what justifies each, when not to create it and how to measure it.

| Type | Takes off the stream-aligned teams | Justified when | Do not create it when | Outcome measure |
| --- | --- | --- | --- | --- |
| Platform | Mechanics every team repeats | Several teams repeat them and can be served self-service | One or two teams need it, no team asked, or it can only work by request | Share of uses without a request; stream-aligned teams' lead time |
| Enabling | A skill gap | Several teams lack a skill they can learn | It would do the work for them, one team has the gap, or engagements have no end | Teams doing the work alone a quarter after the exit |
| Complicated-subsystem | Rare specialist knowledge | The knowledge is rare and slow to grow, and the part changes mostly by itself | The code is only unfamiliar, the knowledge is learned on the job, or most changes cross the line | Share of stream changes that need the team, and their wait |

## Anti-Patterns: Teams That Fit No Type

Some teams are none of the four. The most common is the **functional team**, a team formed around one skill or one step of the work: a QA team that tests every release, a release team that ships every change, an operations team that runs everything in production. One feature separates it from each serving type. A platform team gives the stream a tool and the stream does the work; a functional team does the work itself, every time. An enabling team leaves; a functional team stays. A complicated-subsystem team holds knowledge that is rare; testing and releasing are not rare. A functional team therefore takes one step out of every stream it touches. Each stream gets a hand-off, all the streams share one queue, and the organization has built **The Review Bottleneck**: finished work that waits longer for a check than it took to make. The checklist has the rule: testing, database, architecture and operations work are not set up as mandatory hand-off stages.

The case for functional teams deserves a direct answer. It says that specialists do their best work beside other specialists, and that a pool of testers is cheaper to manage and easier to keep busy than testers spread over eleven teams. The first half is right. The second half counts the cost in the wrong place. The saving appears in the function's budget, and the waiting appears in every stream's lead time, where no budget shows it. The craft can have a home that is not a queue: a community of practice across the stream-aligned teams ([[communities-of-practice-and-chapters]]). Will Larson observes in *An Elegant Puzzle* that centralized groups go one of two ways: some become rigid gatekeepers, and others become advisory and concentrate on educating. In this chapter's terms, which are mine and not Larson's, the second kind has become an enabling team. One condition does favor the functional form: a specialty needed so seldom, such as a yearly security audit, that no stream could keep a specialist busy and little work ever waits for one.

Other teams that fit no type are found in most organizations, and *Team Topologies*, as the checklist records its conversions, gives each a usual fate.

| Team as found | What it usually means | What to do |
| --- | --- | --- |
| QA or release team | A step of every stream is done elsewhere | Move testing and releasing into the streams; keep a few specialists as an enabling team |
| Operations or support team for all systems | Running the software has moved away from the people who build it | Align support to the streams; move shared mechanics to a platform |
| Infrastructure team that works by ticket | A platform team by what it owns, reached through a queue | Replace the tickets with self-service |
| Component team: it owns a technical part because the architecture diagram has a box there | A boundary drawn by technology and not by a stream | Dissolve it into the streams, or convert it if it meets the platform or complicated-subsystem conditions |
| Architecture team that approves designs | A gate | Part-time enabling: architects who work with teams |

## Where the Sources Differ: Two Types, Four Types, Six Structures

A request for a team seldom arrives in the words of *Team Topologies*. Readers from product management know the same teams under other names, and the procedure in the next section has to work with those names too. In *Empowered*, Marty Cagan and Chris Jones describe two types of product team, which I summarize in [[team-topology]]. An **experience team** owns what users and customers see. It is aligned to a customer dimension, such as a persona or a market segment, with as much end-to-end ownership as possible. That is a stream-aligned team. Their **platform team** gives the experience teams leverage through shared services, tooling and abstraction. By my reading it covers two of this chapter's types: the platform team, and the complicated-subsystem team wherever "abstraction" means hiding hard specialist work. *Empowered* has no type that corresponds to the enabling team.

*Build What Matters*, by Ben Foster and Rajesh Nerlikar, starts from structures and not from types. The authors propose six general ways of structuring teams: by product, by feature, by technical layer, by customer segment or persona, by customer-journey stage and by performance metric. Five of the six are choices of stream. The third, by technical layer, forms teams around one skill, which is the functional organization of the previous section. The first consideration the authors give for choosing among the six is to maximize autonomy between teams by minimizing dependencies. By that consideration the layer structure does worst, and that reading is mine. Their "right team" points the same way. As I record it in [[right-team]], their rule of thumb for staffing one product team is five to seven developers, one product manager, half a UX designer, a third of a UI designer and one or two QA engineers. The testers are inside the team.

So the sources differ less in the teams they describe than in what they optimize. Skelton and Pais optimize for flow. Cagan and Jones optimize for what they call empowerment, by which they mean a team that owns a meaningful outcome end to end. The difference decides which to use for what. The two types of *Empowered* cannot tell an enabling team from a functional one, or a team that holds rare knowledge from a platform. This book therefore uses the four types to decide whether a team should exist. The product books say more about what a stream-aligned team should own and decide, and Part III uses them for that, in [[discovery-delivery-and-empowered-teams]].

## Pattern: Name the Type Before You Approve the Team

The four types, under whichever names a request uses, turn into a procedure of four steps, listed below. Put every request for a new team through them, and decline it when step three, what falls for the stream-aligned teams, has no answer. The **user** of the procedure is the leader who approves teams. Its **outcome measures** are the share of teams outside the streams that can name both the teams they serve and the measure they are judged by, and the ratio of stream-aligned teams to the rest.

1. **Name the type** the team claims to be. If it is none of the four, ask what need is behind the request and which type would meet it.
2. **Name the stream-aligned teams** it would serve.
3. **Say what falls** for those teams, load or waiting, and how you will measure it.
4. **Say what ends it**: the exit for an enabling team, a review date for the other two.

A team that already exists is classified with four questions, one for the defining feature of each type, asked in turn as in Figure 2. A team that answers no to all four is folded into the streams it serves or converted into one of the three serving types.

---begin mermaid---
flowchart TD
    Q1{"Does it own a flow of user value end to end?"} -->|"yes"| A1["Stream-aligned"]
    Q1 -->|"no"| Q2{"Does it own tools or services that other teams use in their own work?"}
    Q2 -->|"yes"| A2["Platform"]
    Q2 -->|"no"| Q3{"Does it teach teams and then leave?"}
    Q3 -->|"yes"| A3["Enabling"]
    Q3 -->|"no"| Q4{"Does it hold rare knowledge of one bounded part?"}
    Q4 -->|"yes"| A4["Complicated-subsystem"]
    Q4 -->|"no"| A5["Fits none: fold into the streams or convert"]
---end mermaid---

**Figure 2:** *Four questions classify an existing team, and a team that answers no to all four fits no type.*

Applied to proposed and to existing teams, the steps and the questions leave some ratio of stream-aligned teams to the rest. For that ratio *Team Topologies* offers a rule of thumb, which the checklist records as roughly six to nine stream-aligned teams for every team of another type. Treat it as the authors' rule of thumb. It puts the burden of proof on each additional serving team, and it is not a target. An organization with only four stream-aligned teams for each serving team should put each of its serving teams through steps two and three, and should not dissolve teams to reach a number.

## Worked Example: Corvane's Three Requests, Decided

Dario Vance put the three requests of 2024 through the four steps, with Corvane at 180 people and eleven product teams.

| Request | Type it claims | What falls for the product teams | Decision |
| --- | --- | --- | --- |
| QA team of six | None of the four: a functional team | Nothing; every release would wait for a tester | Declined as proposed; two quality engineers hired as an enabling team |
| Travel-time team of three | Complicated-subsystem | Scheduling's load, a little; but 9 of 11 travel-time changes also change a scheduling rule | Declined |
| Second platform team of four, for test environments | Platform | Seven teams' load, if the environments are self-service | Declined for now; asked again when all eleven teams release without a request to the platform team |

The first request fits no type. Six testers checking every release are a functional team, and at Corvane they would have been the launch queue again: the platform engineer's hand check, removed that year, replaced by a tester's. But the need behind it was real. The two managers wanted confidence in releases that teams now ran themselves, which rests on a skill a team can learn: writing automated tests that tell the team whether its own change is ready. So Corvane hired two quality engineers in place of six testers and set them up as an enabling team. They work with one product team at a time for about six weeks, and an engagement ends when the team adds a readiness check of its own without them. After three quarters the pair had worked with five teams, and all five maintain their own checks.

The second request named a real type and failed its conditions. Travel-time estimation is hard, but its knowledge is not rare: it is a service built on map data and a routing library, which an engineer learns on the job. Its changes also cross the proposed line. In the first half of 2024, 9 of 11 travel-time changes also changed a scheduling rule, so a separate team would have needed Scheduling for almost everything it did. Corvane declined, and when it redrew Scheduling's boundaries in 2025, at about 500 people, it again kept travel time inside the team ([[cognitive-load-and-team-boundaries]]). A part that passes both conditions looks different: a route-optimization solver that only people trained in operations research can change safely, of the kind built by Routewise, the company Corvane later acquires.

The third request also named a real type. It passed the first platform condition, since seven teams repeated the same mechanics, and failed the second. The platform team's first product, the release path, was not yet self-service for everyone: four product teams still released by request. A second product would have opened a second queue. Vance's answer was "not yet", and he gave the condition for asking again: all eleven teams releasing without a request to the platform team.

The four questions of Figure 2, asked of the twelve teams Corvane already had, clear all of them. The eleven product teams, Scheduling, Dispatch, Technician App and the rest, each own a flow of user value, so they are stream-aligned. The platform team owns tools and services that all eleven use in their own work, so it is a platform team, whether or not it was yet self-service. In 2024 the easy conclusion was that the platform team had been a mistake. It had not been a mistake of type. One thing it did, checking each launch by hand, was a functional step that every stream had to pass through, and the release path of 2024 replaced that step with checks the teams run themselves. What had been wrong was how the eleven teams reached the platform team, and that is a different question from what type of team it is.

## What AI Changes Here

The questions that cleared Corvane's teams of 2024 also classify the teams that AI adds. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, organizations I have observed are forming AI enablement teams to help product teams work with coding agents. This is my observation, not a measured result. The book's illustration is Corvane's fifth stage, in 2027 and 2028 at 1,100 people, which has such a team. The questions of Figure 2 apply to it unchanged. If the team teaches product teams and leaves, it is an enabling team, and it is measured by its exits. If every team's use of AI has to pass through it, it is a functional team, and it will become a queue. Shared tooling for agents is a platform question, which [[ai-platform-governance-and-risk]] takes up. No fifth type is needed.

The two questions about load and waiting may also get harder to answer well. **Speculative.** If coding agents let a stream-aligned team handle unfamiliar mechanics and neighboring specialties at lower load, then fewer proposed serving teams will lower anyone's load by enough to be worth a hand-off. Rare knowledge and widely shared platforms would stay justified. The claim would be confirmed where stream-aligned teams report that they dropped a dependency on a specialist team after adopting agents, with no rise in incidents. [[team-shape-and-roles-with-ai]] weighs what has been published.

## What to Take Away

**Established.** What the sources agree on:

- An organization needs four team types; most teams are stream-aligned, and the other three exist to support them and to reduce their cognitive load (Skelton and Pais, *Team Topologies*).
- A platform is best consumed as self-service, and an enabling team works with a team for a limited time and aims at that team's autonomy (*Team Topologies*).
- The product-side sources reach the same default: teams that own a customer-facing outcome end to end, supported by platform teams (Cagan and Jones, *Empowered*; Foster and Nerlikar, *Build What Matters*).

**Depends on context.** What changes with the situation:

- How many teams must share a need before a serving team pays for itself. Three is my rule of thumb for a platform, not a law.
- How rare knowledge has to be. What one company must hire specialists for, another company's engineers learn on the job.
- Whether a small company needs any serving team. At four teams, a shared script and a helpful colleague may be enough.

**The author's synthesis.** What is this book's own position:

- The two-question test, whose load falls and whose waiting falls, adds waiting to the source's cognitive load.
- The second condition for a complicated-subsystem team, that most changes do not cross the new line, is my extension.
- The mapping of *Empowered* and *Build What Matters* onto the four types, and the four steps for a request, are mine.

## Checklist

The four types are four answers to one question, what a team does for the flow of value to users: a stream-aligned team answers it by delivering to users, and each of the other three by what it takes off the teams that do. A team's name does not answer it. List your teams, give each a type, and test every team that is not stream-aligned.

- [ ] List every team and give it one of the four types, or mark it "none".
- [ ] For each stream-aligned team, name its users and the flow of value it owns end to end.
- [ ] For each platform team: which teams repeat the mechanics it carries, and what share of uses needs no request?
- [ ] For each enabling team: when does each current engagement end, and which teams now work without it?
- [ ] For each complicated-subsystem team: is the knowledge rare, and what share of the streams' changes needs the team?
- [ ] For each team marked "none": which step of which streams does it perform, and how long does work wait for it?
- [ ] Decide for each team marked "none": fold it into the streams, or convert it to a serving type.
- [ ] Put the next request for a new team through the four steps before anyone discusses headcount.

Three requests reached Dario Vance in one month, and none was approved as proposed. You can now say why: one fitted no type and hid a need that an enabling team could meet, and two fitted a type and failed its conditions. You have four team types and what each is for. What the types leave open is the thing that went wrong at Corvane's platform team, which was of the right type all along. A platform team can be used without a word or through a queue of requests, and an enabling team can teach or take over. The next chapter takes up how teams of these four types should work with one another, and how that agreement is written down: [[interaction-modes-and-team-apis]].

## Sources and Evidence

**Books**

- *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, Matthew Skelton and Manuel Pais, 2019. The four team types; the definition of a stream; the purpose of a complicated-subsystem team; self-service as the way a platform is consumed; avoiding handovers in the main flow of change; the ratio of stream-aligned teams to others; the conversions of existing team types.
- *Empowered: Ordinary People, Extraordinary Products*, Marty Cagan with Chris Jones, 2020. Experience teams and platform teams. Cited through the author's summary; the mapping onto four types is the author's.
- *Build What Matters: Delivering Key Outcomes with Vision-Led Product Management*, Ben Foster and Rajesh Nerlikar, 2020. Six ways of structuring teams and the considerations for choosing among them; the staffing rule of thumb for one product team.
- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. Centralized groups that become gatekeepers or become advisory.

**Practitioner sources**

- The author's working records and checklist of the *Team Topologies* material: [[four-fundamental-team-topologies]], [[team-topologies-operating-model]], [[stream-aligned-product-teams]] and [[platform-and-devops-operating-model]].
- The author's records on quality engineering as enablement and on communities of practice: [[quality-engineering-enablement]] and [[communities-of-practice-and-chapters]].
- The author's summaries of the product books: [[team-topology]] for *Empowered* and [[right-team]] for *Build What Matters*.
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
