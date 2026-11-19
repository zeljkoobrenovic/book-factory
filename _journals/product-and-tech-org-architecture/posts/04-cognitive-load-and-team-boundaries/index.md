---
title: "Cognitive Load and Team Boundaries"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How much can one team own, and where should the boundary between two teams go? A team owns what its members can change and operate without relying on one person, and a boundary belongs where the domain, the rate of change or the risk differs, not where the headcount divides evenly."
permalink: cognitive-load-and-team-boundaries
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to judge whether a team owns too much or too little, and to place a boundary between two teams where the work itself divides.

> **KEY POINTS:**
>
> * **A team owns only what it can change and operate without one particular person.** Cognitive load, the complexity of the domain plus the mechanics the team must also carry, sets how much that can be.
> * **An overloaded team needs less to understand, not more people.** Remove scope or move mechanics to a platform, and test every request for headcount against what the new people would have to learn.
> * **A boundary belongs on a fracture plane.** Cut where the domain, the rate of change or the risk differs, test the cut against past changes, and leave it undrawn when most changes would cross it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Overloaded Team** — the chapter gives the test for when a team owns more than it can hold, and what relieves it.
> * **The Org Chart as Architecture** — it shows what happens when team boundaries follow the headcount and not the work.
> * **The Hero Culture** — it reads the one engineer who knows everything as a sign of overload.

<br>

Late in 2022 the manager of Corvane's Core team asked for two more engineers. Corvane is the fictional company this book follows. Core had six engineers, and earlier that year it had taken on the company's rule engine on top of the shared services it already ran. The request looked reasonable: more to own, so more people. It was granted, and the two engineers joined in January 2023. A quarter later Core's median lead time for work outside the rule engine was 12 days. Before they joined it had been 11. If you have approved headcount for a struggling team and then watched it struggle on, you have seen the same thing. **Core was not short of people. It was short of understanding**, and understanding is sized and divided by other rules.

This chapter gives those rules. A team can own only what its members can change and operate without relying on one particular person. Ownership is therefore sized by **cognitive load**, the mental effort of understanding a domain plus the mechanics the team must also carry. And a boundary between two teams belongs on a **fracture plane**, a seam where the domain, the rate of change or the risk differs, and not where the headcount divides evenly. The chapter starts with Core's request and the reorganization that followed it. It then defines cognitive load, shows how to assess a team's load and how to relieve it, defines fracture planes, and shows how to test a cut and when not to make one. It ends with the usual ways sizing and cutting go wrong, Corvane's re-cut of two teams, and what AI changes.

## Setting the Scene: Six Engineers and a Request for Two More

Here is what Core owned when its manager made the request. In late 2022 Corvane had about 45 engineers and was starting to hire quickly. Core's six ran the services every other team used: accounts and sign-in, notification delivery and the shared data model for customers and jobs. They also maintained their own deployment scripts. Earlier in 2022, after two incidents in which teams had implemented the same scheduling rule differently ([[the-organization-as-a-system]] tells that story), Corvane had moved all scheduling and job-status rules into Core as one component, the rule engine.

That scope showed in two ways. Samir Haddad, a staff engineer, was the only person who could safely change the rule engine's overlap logic, the part that decides whether two jobs for one technician conflict. And Core's median lead time for work outside the rule engine, measured from starting a change to releasing it, rose from 4 days to 11. The rule engine took the team's attention, and everything else waited.

Corvane then did what the manager asked. Two engineers joined Core in January 2023, and a quarter later the lead time for other work was 12 days. The new engineers had to learn the scope before they could change any of it, and the person they learned the rule engine from was Samir Haddad, who spent much of that quarter explaining and little of it building.

Later in 2023 the whole company was reorganized, and headcount was the measure again. Corvane formed eleven product teams of about eight engineers by dividing people evenly. Core was dissolved. Accounts and sign-in went to a new Identity team and notification delivery to a Notifications team. The shared data model and the deployment scripts went to the platform team, which Corvane had formed in 2022 to take release and infrastructure work off the other teams. The rule engine was divided. The Scheduling team got the scheduling rules, the planner calendar screens and travel-time estimation. Travel-time estimation is a separate service that estimates the drive between two jobs, built on map data and a routing library. The Dispatch team got the job-status rules and the live dispatch board. In the first half of 2024, 23 of 31 rule changes needed both teams.

The two decisions have one thing in common. Both measured ownership in people: so many engineers for so much scope, so much scope for every eight engineers. Neither asked what a team would have to understand. That leaves two questions, and the rest of the chapter answers them in order. How much can one team own? And where should the line between two teams go?

## Cognitive Load: What One Team Can Hold

The first question has a name in the literature. In *Team Topologies*, Matthew Skelton and Manuel Pais use **cognitive load** for the total mental effort a team needs to understand, change and operate what it owns. To operate a thing means to run it in production and be on call for it. They argue for restricting a team's cognitive load, and they treat thinking about it explicitly as a tool for deciding team size, assigning responsibilities and setting boundaries. The term comes from John Sweller's research on learning in the 1980s; I cite Sweller only for the origin, as a supplement to this book's sources. [[the-organization-as-a-system]] named three capacities that run out in an organization: attention, judgment and verification. In this book's terms, cognitive load is how the first of them, attention, shows up for one team. [[flow-and-the-constraint]] treats all three in full.

*Team Topologies* distinguishes three kinds of load, and the difference matters because each calls for a different response. I read the first two as the complexity of the domain and the mechanics the team must also carry. The third is the learning that makes a team better at its domain.

| Kind of load | What it is | At Core in 2022 | What to do with it |
| --- | --- | --- | --- |
| Intrinsic | The complexity of the domain itself | The scheduling and job-status rules | Accept it, and size the scope to it |
| Extraneous | Mechanics around the work: release steps, tooling, process, hand-offs | Core's own deployment scripts | Remove it, or move it to a platform |
| Germane | Learning the domain and solving its problems | Understanding why planners double-book | Protect it |

Because load has a limit, ownership needs a test, and I use this one: **a team owns a thing only when its members can change it and operate it without relying on one particular person**. *Team Topologies* requires that every part of a system be owned by exactly one team, with no shared ownership. The test says when a team really has what the ownership map gives it. A thing only one person can change is owned by that person. It cannot be changed while that person is away, and the colleagues who are on call for it cannot repair it.

When a team is given more than passes the test, it does not fail all at once. Skelton and Pais describe what happens: “If we stress the team by giving it responsibility for part of the system that is beyond its cognitive load capacity, it ceases to act like a high-performing unit and starts to behave like a loosely associated group of individuals, each trying to accomplish their individual tasks without the space to consider if those are in the team’s best interest.” A team that has become a group of individuals has parts each known to one of them. Those parts are changed slowly, by one person, or not at all.

The same authors offer a rule of thumb for staying short of that point. Classify each domain a team owns as simple, complicated or complex. In a simple domain most work has a clear path. In a complicated one a change needs analysis and often a few attempts. In a complex one a solution takes experiment and discovery. Then give a team at most one complex domain, with nothing else on top of it, and do not give a team several complicated ones. It is their rule of thumb, not a law, and my working checklists in [[team-first-thinking]] record it in that form.

The rule of thumb sounds like a calculation, and it is not one. Cognitive load cannot be measured, only assessed. The source's own method is a question: “A simple and quick way to assess cognitive load is to ask the team, in a non-judgmental way: ‘Do you feel like you’re effective and able to respond in a timely fashion to the work you are asked to do?’” Sweller's concept describes one person learning. Applying it to a whole team is a working idea that practitioners find useful, and I know of no validated measure behind it. The evidence stops there, and the next section works within that limit.

## Pattern: Assess a Team's Load from What It Owns

A load that can only be assessed still needs an assessment that does not rest on opinion alone. The one I use is an ownership list with two counts. List every area the team owns. For each, write down how many members can change it safely and how many can operate it. The **user** of this pattern is the team's lead, together with the leader who assigns the team its scope. The **outcome measure** is the number of areas where either count is below two. An area with a count of one is owned by a person, and an area with a count of zero is owned by nobody. This procedure is mine; it applies the ownership test area by area.

The count comes with four signals that a team owns too much. The list is my own, built on the warning signs in *Team Topologies*.

| Signal | What you see | What it tells you |
| --- | --- | --- |
| Single-person knowledge | An area only one member can change or operate | The team does not own it; the person does |
| Lead time rising for the team's other work | Older areas wait while the newest takes the attention | Scope was added and nothing was removed |
| Areas nobody changes | Requests in one area are postponed or worked around | The team has stopped understanding it |
| The team's own answer | The team says it cannot respond in time | The source's direct question, answered |

Here is the list for one team, Core in late 2022, at about 45 engineers.

| Area | Kind | Can change it | Can operate it |
| --- | --- | --- | --- |
| Rule engine | Complex | 1 for the overlap logic, 3 for the rest | 3 |
| Accounts and sign-in | Complicated | 2 | 4 |
| Notification delivery | Complicated | 3 | 4 |
| Shared data model | Complicated | 2 | 3 |
| Deployment scripts | Mechanics | 1 | 2 |

The list shows one complex domain, three complicated ones and a set of mechanics, in a team of six. Two areas could be changed by one person only. Core broke the rule of thumb and failed the ownership test twice, and the request for two engineers mentioned neither fact.

A team can also own too little, and the signs are the reverse. Most of its changes need another team before they can ship. It cannot staff its own on-call rotation. Or it fills its time with work nobody asked for. These three signs come from my own experience and not from *Team Topologies*, whose checklists warn mainly about overload.

## Pattern: Relieve the Load by Removing Scope or Mechanics

Once a team is assessed as overloaded, the usual remedy is the one Core's manager asked for, and it does not work. Adding people does not lower what each member must understand. Scope is not divided by headcount: on call, in review and in design, each member still meets all of it. New members also learn from those who already know, as Core's two engineers learned from Samir Haddad, so the remedy adds teaching to the people who are already the limit. And growth has a ceiling. *Team Topologies* treats a team as small, about five to nine people by the authors' rule of thumb, which [[team-size-and-composition]] examines.

What works is to take something away. Move a domain to another team, or move mechanics to a platform, which is a team that provides tooling and services other teams use. The **user** of this pattern is the overloaded team. Its **outcome measures** are the count of single-person areas, taken from the ownership list, and the lead time for the team's other work. In practice the pattern starts with a question put to every request for headcount: what would the new people have to understand, and who would teach them?

Counting the hiring that Core's manager asked for, there are three remedies. They change different things, and hiring is sometimes the right one.

| Remedy | What it changes | What it costs | Right when |
| --- | --- | --- | --- |
| Remove scope | What the team must understand | A new boundary, and an interface someone has to own | The team holds a complex domain plus others, or domains unrelated to each other |
| Move mechanics to a platform | What the team must carry besides its domain | A dependency on the platform | The load is release steps, tooling or infrastructure that several teams repeat |
| Add people | Hands, not understanding | Onboarding and more coordination | Every area passes the ownership test and the work still exceeds the team |

The second remedy has a condition, though. A platform relieves a team only when it is self-service, meaning the team can use it without filing a request and waiting. Otherwise the team exchanges load for a queue. Corvane found this out with the platform team from the scene, which had held Core's deployment scripts since 2023. By 2024, at 180 people, a product team that wanted to release a change had to file a launch request with that team and wait. Five platform engineers served eleven product teams, 14 launch requests were open at the peak, and the lead time for a change reached 19 days. The teams carried less and waited more. [[the-organization-as-a-product]] tells how Corvane shortened that wait, [[platforms-and-developer-experience]] covers how to build the self-service kind, and the next chapter covers the queue.

## Fracture Planes: Where a Boundary Can Go

Removing scope means cutting it somewhere, which is the second open question, and *Team Topologies* names the place to cut: “A fracture plane is a natural seam in the software system that allows the system to be split easily into two or more parts.” The authors apply the idea to software. I apply it to the scope a team owns, which in a product and tech organization is mostly the same thing.

A seam is natural where the two sides need little knowledge of each other. The interface between them can then stay narrow, and each side's load stays low. A cut through an area that changes together does the opposite. Every change needs both sides, so both sides have to understand both halves, and the boundary has added a second team to each change without removing anything from the first.

The strongest seam is usually the business domain, and its best-known description is Eric Evans's **bounded context**, from *Domain-Driven Design*: the part of a business within which one model and one vocabulary apply consistently. Evans's book is not among my annotated sources, so I cite only this widely known concept. *Team Topologies* puts the bounded context first among its fracture planes. It also gives you a practical test. Where the same word means different things to two groups, as “job” does to a planner and to a billing clerk, a boundary between contexts runs between them.

Domain is one of four planes this chapter uses, and each comes with a question you can ask of a real scope. The last column of the table names two things at Corvane that the plane separates. *Team Topologies* lists more: regulatory compliance, performance isolation, team location and user personas. I keep to the four that decide most cases. The last of them, technology, is the weakest, because teams split by technology each own a layer, and most changes a user can see cross every layer.

| Plane | What differs | Question to ask | At Corvane |
| --- | --- | --- | --- |
| Domain | Vocabulary, model and rules | Do the two sides use the same words for the same things? | Scheduling rules on one side, customers' billing exports on the other |
| Rate of change | How often each side changes | Does one side wait for the other's pace? | Planner screens ship several times a week; each rule change waits for a weekly review |
| Risk | What an error costs | Would a mistake on one side be contained there? | A wrong rule alters every customer's schedule |
| Technology | Skills and tools | Is the difference a real constraint, or a convenience? | The technicians' mobile app and the office web application |

Headcount is not on that list. Corvane's cut of 2023, made while the company grew toward 180 people, put half of the rule engine in each of two teams, and the figure shows where the line fell.

---begin mermaid---
flowchart LR
    ST["Scheduling team"] -->|"owns"| PC["Planner calendar screens"]
    ST -->|"owns"| TT["Travel-time estimation"]
    ST -->|"owns"| SR["Scheduling rules"]
    DT["Dispatch team"] -->|"owns"| JR["Job-status rules"]
    DT -->|"owns"| LB["Live dispatch board"]
    SR ---|"one rule engine: 23 of 31 rule changes need both teams"| JR
---end mermaid---

**Figure 1:** *Corvane's 2023 boundary between Scheduling and Dispatch ran through the rule engine, one domain whose two halves changed together.*

## Pattern: Test a Cut, and Know When Not to Make It

A plane says where a boundary can go, and a particular boundary can be checked before anyone is moved. Take the changes of the last quarter and count how many would have needed both sides of the proposed line. The **users** of this pattern are the two teams the line would create and the teams that depend on them. The **outcome measure** is that share, counted before the cut and again after it. *Team Topologies* asks of any proposed split: “Does the resulting architecture support more autonomous teams (less dependent teams) with reduced cognitive load (less disparate responsibilities)?” The count from history is my way of answering that question with a number.

Even a cut that passes the test has a price. Every boundary replaces shared understanding with an interface, and an interface works only when someone owns it, as [[the-organization-as-a-system]] argued. A cut is therefore worth making only when the load it removes is larger than the interface it adds.

It follows that a fracture plane says where a boundary may go, not that it must. There are four cases in which I would not draw the boundary although a plane exists:

- **Most changes would cross it.** The two sides differ in technology or risk, but the record shows they change together.
- **A resulting team could not operate its part.** It would be too small to carry an on-call rotation, or it would lack a skill the part needs.
- **Nobody is overloaded.** Every area on both sides passes the ownership test, so the cut removes no load and still adds an interface.
- **The two sides would stay coupled underneath.** They would still share a database schema, a build or a release, which *Team Topologies* calls hidden monoliths. [[team-first-boundaries]] lists the checks.

## Anti-Patterns: The Capable Team and the Even Split

What is commonly done instead of these patterns starts with a compliment. **The Overloaded Team** is made when scope goes to the team that copes, on the assumption that capable engineers can own whatever they are given. Capability does raise how fast a team learns a domain. It does not remove the limit on how many domains its members can hold at once. Core was given the rule engine in 2022 because it was Corvane's most capable team, and a year later it was the slowest.

The same assumption applied to many teams is **The Org Chart as Architecture**, which in this chapter takes the form of the even split. The budget sets the size of the teams, and the current backlog sets their scope. But a backlog describes the next two quarters, and a domain outlasts them. Teams drawn around the backlog of 2023 own whatever that backlog happened to contain. Layer teams, one per technology, are the same error with a different divider: each owns a layer, and every change a user can see crosses all of them.

**The Hero Culture** keeps both errors from being seen. The engineer who is the only one able to change something gets praised for it, and the praise is sincere. But that engineer is the clearest sign in the organization that a team owns more than it can hold. The ownership list turns the hero into a count of one, which is easier to act on.

## Worked Example: Re-Cutting Scheduling and Dispatch

All of this can be applied to the two teams the scene ended with. In 2025, when Corvane had about 500 people, Dario Vance, its VP Engineering, asked Samir Haddad to run the assessment on Scheduling and Dispatch, the two teams of eight that had shared the rule engine since 2023. Samir Haddad used the count Corvane already had, from the first half of 2024. It covers half a year where the test would normally take a quarter, because a quarter holds only about fifteen rule changes. The boundary had not moved since, so the record still described it. In that period Scheduling's median lead time for a rule change was 9 days. The list below combines the ownership counts with that record of changes.

| Area | Owner since 2023 | Kind | Can change it | From the change record |
| --- | --- | --- | --- | --- |
| Scheduling rules | Scheduling | Complex | 2 | 23 of 31 rule changes needed both teams |
| Job-status rules | Dispatch | Complex | 1 | The same 23 of 31 |
| Travel-time estimation | Scheduling | Complicated | 2 | 9 of its 11 changes also changed a scheduling rule |
| Planner calendar screens | Scheduling | Complicated | 4 | Changed several times a week; 3 of 120 changes needed a rule change |
| Live dispatch board | Dispatch | Complicated | 5 | Changed several times a week |

In the chapter's terms the list shows two faults. One domain, the rules, was held by two teams, and three of every four changes to it crossed the line between them. And Scheduling held half of a complex domain plus two complicated ones, which is more than the rule of thumb allows.

Corvane answered with three decisions, and the third is a boundary it chose not to draw.

| Decision | Plane or reason | Measure |
| --- | --- | --- |
| The job-status rules move to Scheduling, which then owns the whole rule engine | Domain: one vocabulary, and the two rule sets change together | Share of rule changes that need two teams |
| The planner calendar screens move from Scheduling to Dispatch | Rate of change and risk: screens change several times a week and an error in one is visible and reversible; a rule change waits for the weekly review, and a rule error alters every customer's schedule | Scheduling's median lead time for a rule change |
| Travel-time estimation stays inside Scheduling | No boundary, although the technology differs (map data and a routing library): 9 of 11 changes would cross the line, and the two engineers who know it could not carry an on-call rotation | None; revisit when either count changes |

Drawn after the change, the boundary runs between the rules and the planner's screens. The interface across it is the versioned rule schema, the published description of the rules that Corvane introduced together with the rule engine in 2022.

---begin mermaid---
flowchart LR
    ST["Scheduling team"] -->|"owns"| RE["Rule engine: scheduling and job-status rules"]
    ST -->|"owns"| TT["Travel-time estimation"]
    DT["Dispatch team"] -->|"owns"| PC["Planner calendar screens"]
    DT -->|"owns"| LB["Live dispatch board"]
    RE -->|"versioned rule schema"| PC
    RE -->|"versioned rule schema"| LB
---end mermaid---

**Figure 2:** *After the 2025 change the boundary lies on a fracture plane: one team owns the whole rule domain, and the screens that change several times a week sit on the other side of a published interface.*

Two quarters later, 3 of 28 rule changes needed both teams, against 23 of 31 before. Four engineers could change the job-status rules, where one could before. Scheduling's median lead time for a rule change fell from 9 days to 5. No engineer was added. The cost was a quarter in which both teams shipped less, mostly while Dispatch learned the calendar screens. Corvane did not re-cut its other nine product teams at the same time; it started where the count was worst.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The worked example is from 2025, and since then coding agents have started to write part of the code, so the sizing rule has to be checked against them. **Emerging.** As of November 2026, in the teams I have observed, agents make it much cheaper to produce a change in code the team does not know well. They do not change what the team must understand to review that change, operate it and answer for it. The ownership test is therefore unchanged: a team that cannot judge and run what an agent produced for an area does not own that area. This is my observation, not a measured result.

What may change is how much scope passes the test. **Speculative.** Agents could pull a team's load in two directions. They could lower it, by explaining unfamiliar code on demand and by absorbing mechanics. Or they could raise it, by producing more change than the team can understand. I do not know which pull is stronger. The ownership list would show it: if teams using agents take on more areas and the count of single-person areas stays flat, the limit has moved. [[where-the-constraint-moves]] and [[team-shape-and-roles-with-ai]] weigh the published evidence.

## What to Take Away

**Established.** What the sources agree on:

- A team has a limit on what it can understand, and beyond it the team behaves as a group of individuals (Skelton and Pais, *Team Topologies*).
- Every part of a system needs exactly one owning team (*Team Topologies*).
- Systems split most easily along natural seams, and the business domain, Evans's bounded context, is the first to look for.

**Depends on context.** What changes with the situation:

- Which remedy fits an overloaded team depends on what its load consists of: domains call for removing scope, repeated mechanics for a self-service platform, and plain volume of work for people.
- Which plane to cut on, and whether to cut at all, depends on how past changes fall across the line and on whether each resulting team can operate what it gets.

**The author's synthesis.** What is this book's own position:

- The ownership test with its two counts, the count of changes that cross a proposed line and the three signs of underload are mine, built on *Team Topologies*.
- Reading cognitive load as the capacity of attention seen in one team is this book's framing; [[flow-and-the-constraint]] argues it.

## Checklist

This chapter gave one rule for sizing a team's scope and one for placing a boundary. They are the same rule seen from two sides. A team's scope is right when the team passes the ownership test. A boundary is right when it lets the teams on both sides pass it, with a narrow interface between them. Headcount enters only after both are settled. So when a request for people or a proposal for a reorganization reaches you, you can ask first what the team would have to understand and what share of changes would cross the proposed lines, and decline what the answers do not support. Take one team that has asked for people and run these eight checks before deciding whom to hire.

- [ ] List every area the team owns, including the mechanics it maintains for itself.
- [ ] For each area, count the members who can change it safely and the members who can operate it.
- [ ] Mark every area where either count is below two.
- [ ] Classify each domain as simple, complicated or complex, and check for a complex domain with others on top of it.
- [ ] Ask the team whether it can respond in time to the work it is asked to do.
- [ ] Decide what to take away: a domain to another team, or mechanics to a self-service platform.
- [ ] For any proposed cut, name the fracture plane and count how many of last quarter's changes would have crossed the line.
- [ ] Check the four reasons not to cut: changes cross the line, a team cannot operate its part, nobody is overloaded, or the sides stay coupled underneath.

Core's request for two engineers can now be read in full. It left out two areas that only one person could change, a complex domain added on top of three complicated ones, and the fact that nothing had been taken away. With that, teams as components have a sizing rule and their boundaries have a placing rule. Neither rule says anything yet about the work that moves across those boundaries from one team to the next. That work has one place where it waits longest, and finding that place is the subject of the next chapter: [[flow-and-the-constraint]].

## Sources and Evidence

**Books**

- *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, Matthew Skelton and Manuel Pais, 2019. Cognitive load as the limit on a team's responsibilities; the three kinds of load; the effect of overload; the question for assessing load; the simple, complicated, complex rule of thumb; single ownership; fracture planes; the question for testing a split; hidden monoliths; team size of five to nine.
- *Domain-Driven Design: Tackling Complexity in the Heart of Software*, Eric Evans, 2003. The bounded context, cited as the widely known concept; it supplements the author's annotated sources.

**Research and reports**

- “Cognitive Load During Problem Solving: Effects on Learning”, John Sweller, *Cognitive Science*, 1988. Cited only for the origin of the term cognitive load; it supplements the author's annotated sources.

**Practitioner sources**

- The author's working records and checklists on *Team Topologies*: [[team-first-thinking]], [[team-first-boundaries]] and [[static-team-topologies]].
- The ownership list with two counts, the count of changes crossing a proposed line and the signs of underload are the author's practice and are labeled as such in the text.
- The statements under “What AI Changes Here” are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
