---
title: "Conway's Law and the Inverse Conway Maneuver"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Why do systems end up shaped like the organizations that build them, and when can a leader use that deliberately? Because every design decision needs people to talk, software is weakest where teams talk least; shaping teams to get a wanted architecture works only when skills and ownership move with them."
permalink: conways-law-and-the-inverse-conway-maneuver
timetoread: 19 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn why software takes the shape of the teams that build it, and how to check whether a team change will produce the architecture you want.

> **KEY POINTS:**
>
> * **Software copies the communication structure of the organization that builds it.** Every design decision needs the people who make it to talk, so the parts of a system fit together inside a team and fit poorly where teams talk least.
> * **A team change is an architecture change, and the reverse.** Shaping teams to match the architecture you want is the inverse Conway maneuver, and it puts technical leaders in the room where teams are drawn.
> * **The maneuver works only when skills and ownership move with the teams.** Where they stay behind, the old architecture reappears inside the new chart.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Org Chart as Architecture** — redrawing teams changes who talks, and leaves code, knowledge and operational duty where they were.
> * **The Unowned Interface** — the law predicts which lines between teams need an agreed contract, before an incident finds them.

<br>

In 2021 a customer of Corvane could have drawn Corvane's team structure without ever seeing an org chart. Corvane is the fictional company this book follows. It makes scheduling software for field-service companies, and in 2021 it had 28 people in product and tech. Its office application and its mobile app each behaved consistently from one screen to the next. They disagreed with each other about one rule: whether a technician could be given a second job inside the travel-time window after the first. The product was sound inside each team's part and **broken on the line between two teams**.

If you build software, you have used a product in which the web and mobile versions of one feature behave differently, and you have probably guessed that two teams built them. That guess is Conway's Law. Two terms first. The **architecture** of a system is its parts and the interfaces between them. An **interface**, in this chapter, is the software kind: the place where two parts of a system meet, with the agreement about what passes between them. This chapter argues that systems mirror organizations because every design decision needs communication between the people who make it, so interfaces form where teams talk least. A leader can use this by shaping teams to match the wanted architecture. That move is called the inverse Conway maneuver, and it works only when the new teams hold the **skills** and the **ownership** the target boundaries require. Otherwise the old architecture reappears inside the new chart. The chapter starts with Corvane's case, gives Conway's argument and the cost of communication behind it, and turns that into a way of predicting where a system's interfaces will be weak. It then sets out the maneuver and its two conditions, the two opposite mistakes, and the trade-offs. It ends with three team changes at Corvane and with what AI changes.

## Setting the Scene: Faults on the Team Lines

Those 28 people worked in four teams under two engineering managers, and each team owned one part of the product. Web built the office application that planners use. Mobile built the technicians' app. Integrations connected customers' billing and stock systems. Core ran the shared services underneath.

The product failed where the parts met. In 2021 the office application accepted a second job for a technician inside a travel-time window, and the mobile app rejected it. Planners and technicians saw different schedules for three weeks, in an incident Corvane calls the Two Calendars. In 2022 a job marked complete on the phone stayed open in customers' billing exports for eleven days. The first fault sat on the line between Web and Mobile, and the second on the line between Mobile and Integrations. No fault of this kind appeared inside any one team's application.

That pattern is too regular to be carelessness. Careless work would have scattered faults through the product, and these sat only where two teams' work met. Each team's code was also correct by that team's own reading of the rule. [[the-organization-as-a-system]] used these incidents to show that replacing a person does not change a structure. This chapter asks a different question about them: why was the product weak exactly where the teams met?

## Conway's Law: What Conway Argued in 1968

Melvin Conway answered that question in 1968, in a paper called "How Do Committees Invent?", published in the magazine *Datamation*. The paper's conclusion is the sentence now known as Conway's Law: "organizations which design systems (in the broad sense used here) are constrained to produce designs which are copies of the communication structures of these organizations." Two words in it matter for the rest of this chapter. He says constrained: this is a limit, not a tendency that effort overcomes. And he says communication structures, which is not the same thing as the org chart. This chapter's main source is a book, *Team Topologies* by Matthew Skelton and Manuel Pais, which builds on Conway, and I read Conway's paper to supplement it.

The first step of his reasoning is that organizing a design effort is itself a design decision. Before anyone designs anything, the work is divided among groups. Conway observes that the act of organizing a design team means some design decisions have already been made, explicitly or not, and that each delegation narrows the designs that can still be pursued. A design that would need two groups to work as one is out of reach once they are two groups. So part of the system's structure is chosen when the teams are chosen.

The second step concerns the connections between the parts. Two parts of a system can work together only through an interface, and somebody has to agree what that interface is. Conway's point is that the somebody is always two groups: wherever two parts are connected, the groups that designed them must have negotiated and agreed on an interface specification. Every connection in the system therefore stands for a conversation in the organization. It is a particular kind of conversation: two groups agree an interface so that they do not have to talk about everything else. Inside a group the talk is continuous and needs no specification. The interfaces therefore mark the places where the organization talks least, not most. Draw the system's parts and their connections, draw the groups and who talks to whom, and the two drawings have the same shape. Conway calls this structure-preserving relationship a homomorphism. Skelton and Pais call the pressure it puts on a design, toward the shape of the organization, the "homomorphic force".

Conway's own example shows the copying in miniature. A contract research organization had eight people and two compilers to write, one for COBOL and one for ALGOL. It assigned five people to the first and three to the second. The COBOL compiler ran in five phases, and the ALGOL compiler ran in three. The number of parts followed the number of people.

An argument and an anecdote are not a measurement, and the law has been tested with a measurement at least once. What follows is a research finding, reported with its limits. In a Harvard Business School working paper first issued in 2008 and revised in 2011, Alan MacCormack, John Rusnak and Carliss Baldwin compared five matched pairs of software products. In each pair, one product was built by an open-source community, whose contributors are loosely connected, and one by a commercial firm, whose developers are tightly connected. They measured each product's propagation cost, the share of the system that a change to one element can affect on average. In all five pairs the open-source product had the lower propagation cost, by up to a factor of eight, which means it was the more modular: the loosely connected organization had built the loosely connected product. The authors state the limits themselves. The sample is five pairs, all of them software. And the result fits two explanations: designs may drift toward the shape of their organization, or open-source designers may choose modularity on purpose because distant contributors need it. The study supports the mirroring and does not settle its cause.

## Why Interfaces Form Where Teams Talk Least

Conway's argument can be restated as a cost, and a leader can reason with a cost. Two kinds of interface have to be kept apart first. The interface defined in the introduction is a software interface, between two parts of a system. Chapter 1 used the word for the agreed way in which work and knowledge cross between teams, and in this chapter I call that kind a **team interface**. The line a team interface crosses is a **team line**: the line between two groups of people who decide things together inside the group and seldom across it. Conway's claim is that the two kinds coincide: software interfaces lie on team lines. I call a software interface **weak** when its two sides disagree, or when it changes more slowly than the product needs.

The two kinds coincide because of what a design decision costs on each side of a team line. Inside a team, a decision costs a conversation at a desk, and it can be revisited the next morning when it turns out to be wrong. Across a team line, the same decision costs a meeting, a document and a wait, and revisiting it costs all three again. People make cheap decisions often and correct them, and they make expensive ones once, narrowly, or not at all. This is my reading of Conway and not his wording, and it explains the fit: the parts one team owns are joined by hundreds of small corrected decisions, and the parts two teams own are joined by a few.

An expensive decision at a team line ends in one of three ways: a narrow contract, a duplicate or a queue. The narrow contract is the good outcome. Corvane had one in 2021, the small API through which Core's shared services reached the other three teams, and it seldom needed to change. Both of Corvane's faults were duplicates. The rule for overlapping jobs was decided once in Web and once in Mobile, and the rule for job status once in Mobile and once in Integrations, so the office application, the phone and the billing export each applied their own team's version. Deciding either rule together would have cost more than each team could see a reason to pay. Chapter 1 named this failure The Unowned Interface. The queue is the third outcome, and Corvane had none in 2021. The table gives all three.

| Outcome | What you see in the software | What you see in the organization | At Corvane |
| --- | --- | --- | --- |
| Narrow contract | A small API that rarely changes | Little talk across the line, and it is enough | Core's service API in 2021 |
| Duplicate | The same rule implemented in two places | Each team decides alone | The overlapping-jobs rule in Web and in Mobile, 2021 |
| Queue | One path that every change must take | Requests wait at one team | None in 2021; the worked example shows one from 2023 |

Which lines count as team lines depends on who actually talks, and not on who reports to whom. Conway wrote of communication structure, and *Team Topologies* warns against reading that structure off the org chart, which shows reporting and not conversation. Two teams under one manager that never meet have a team line between them, and two teams in different departments whose engineers talk every day may have almost none. My working notes on this point are in [[org-chart-problems]].

## Pattern: Predict the Weak Interfaces from the Team Structure

The duplicates and the queues can be found before an incident finds them, by reading the team structure as it really communicates. The pattern has three steps. First, list the things your users experience as one: a feature, a rule, a customer journey, a launch. Second, for each of them, mark every team line it has to cross. Third, at each marked line, ask whether a contract exists for what crosses and which team owns it. Every pattern in this book names its user and an outcome measure, a way to know whether it worked. The user of this pattern is the leader or architect who reviews a team structure. The measure is how good the prediction was: the share of cross-team incidents and delays over the next two quarters that fall on lines the review had marked.

Run on common team structures, the three steps give predictable results. The table lists four ways of cutting teams, the thing each cut runs across, and what to expect there.

| Teams cut by | The line runs across | Expect |
| --- | --- | --- |
| Client platform (web, and each mobile platform) | Every feature that exists on more than one client | The same feature behaving differently on each client |
| Technical layer or data store (front end, back end, one team per database) | Every feature that needs more than one layer or store | Slow features, and data that disagrees between stores |
| Product area, with one shared release or infrastructure team | Every launch | A queue at the shared team |
| Site or time zone | Whatever is split between the sites | A software interface at the site line, however the code is organized |

The prediction says where to look. It does not say that something is broken there. A line crossed by a small, owned contract that seldom needs to change is a good interface, and the law is the reason it is good: little needs to be said across it. A team line is a weakness only where a decision that keeps changing has to cross it. *Team Topologies* adds the converse, that a busy line can be a bad sign: not all communication between teams is good, and when two teams that should not need to talk according to the software design are talking, something is wrong with the line between them. My working record on this is [[conways-law]].

## Pattern: The Inverse Conway Maneuver

A law that predicts where a structure will hurt can also be used to choose the structure. The **inverse Conway maneuver** is to decide the architecture you want and then shape the teams to match it, so that the system the organization naturally produces is the one you want. Shaping a team means deciding what it owns as well as who is in it, so moving a part of the system from one team to another is also shaping teams. Inside each wanted part, decisions are then cheap. The expensive ones are left only at the interfaces you chose. *Team Topologies* describes the maneuver under the name reverse Conway maneuver, and it quotes a line that sums it up: "Team assignments are the first draft of the architecture." The users of this pattern are the leaders who decide team boundaries, together with their architects. Its outcome measure is whether a change inside one wanted part can be made and released by one team without waiting for another.

Shaping teams to produce an architecture makes team design an architecture decision, and that settles who has to take part in it. Skelton and Pais argue that managers who decide which teams build which services are implicitly deciding the system architecture, whether or not they know it. They conclude that deciding the shape and boundaries of teams without input from technical leaders is very ineffective.

The same holds in the other direction: an architecture decision is a request to the organization. A design that needs conversations the organization does not have will not be built as drawn. *Team Topologies* turns this into a standing question, saying the law "creates an imperative to keep asking: 'Is there a better design that is not available to us because of our organization?'"

## The Two Conditions: Skills and Ownership

The maneuver as described so far changes less than it seems to. Redrawing teams changes who sits, plans and talks together. It leaves three things where they were: the knowledge of how the code works, the code itself, and the duty to run it in production. Two conditions follow from that. The knowledge has to move, which is the skills condition. The code and the duty have to move, together with the right to decide about them, which is the ownership condition. The figure shows the two as checks between a redrawn chart and a changed architecture.

---begin mermaid---
flowchart TD
    A["Wanted architecture"] --> B["Teams redrawn to match"]
    B --> C{"Does each team hold the skills its boundary needs?"}
    C -->|"yes"| D{"Does each team own its code, its decisions and its operation?"}
    C -->|"no"| F["Old architecture reappears inside the new chart"]
    D -->|"yes"| G["Architecture follows the teams"]
    D -->|"no"| F
---end mermaid---

**Figure 1:** *A redrawn chart changes the architecture only if each new team holds the skills and the ownership its boundary requires.*

The first condition concerns knowledge. Each new team must be able to design, change, release and operate its part without borrowing a person from another team. Where it cannot, the team that holds the missing skill takes part in every change, and a dependency on someone else's skill is a communication path. The old team line is still there, whatever the chart says. This is my application of Conway's argument. *Team Topologies* supports it from the design side: it lists skills first among the inputs to team design, ahead of the desired architecture and the business goals.

The second condition concerns the code, the decisions and the operation. In the words of *Team Topologies*, "Every part of the software system needs to be owned by exactly one team." Other teams may propose changes to the owning team, and they do not make the changes themselves. Ownership in this sense is the code, the right to decide about it, and the duty to operate it. A boundary on the chart that lacks any of the three leaves the previous owner in every change.

When either condition is missing, the old architecture reappears inside the new chart. *Team Topologies* supplies a named case of the failure: the joined-at-the-database monolith, in which a system has been divided into several applications or services and all of them remain coupled to the same database schema. The teams and the services were redrawn. The ownership of the data was not divided, so the missing condition is ownership. Almost every change still needs several teams to agree, and the single system survives its reorganization. The table gives both conditions as checks, with the sign that each is missing.

| Condition | What has to move with the team | Sign that it did not move | What reappears |
| --- | --- | --- | --- |
| Skills | Knowledge of the domain and the code, and of releasing and running it | Changes wait for one person in another team | The old team, as a queue |
| Ownership | The code, the decision rights and the on-call duty | Several teams change the same code or schema; nobody is paged | The old system, with more meetings |

## Anti-Patterns: Two Opposite Mistakes

Two opposite mistakes are common. The first ignores the law itself. It treats architecture as a technical matter that architects decide and teams implement. The architects draw the target, and the teams, left as they were, build what their communication allows. *Team Topologies* is direct about it: "thinking of software architecture as a standalone concept that can be designed in isolation and then implemented by any group of teams is fundamentally wrong."

The second mistake is the opposite one. It accepts the law and ignores the two conditions: it redraws the teams and waits for the architecture to follow. This is the failure pattern this book calls **The Org Chart as Architecture**: the chart changes, and the skills and the ownership do not. One form of it splits teams ever finer in Conway's name, one team for each component on the target diagram. Each split draws a new team line, and the knowledge of how the components work together is not split with it. It stays with the few people who had it, who now sit in one of the new teams, and every other team depends on them. More lines have been drawn, and the skills condition fails on each of them.

## Trade-Offs: Move the Teams, Move the Architecture, or Keep the Mismatch

Each of the two mistakes changes one side and assumes the other will follow by itself. When teams and architecture disagree, the real choice is among three options: close the mismatch from the team side, close it from the software side, or keep it on purpose. Each has a price, and the table says when each is right.

| Choice | Right when | Price |
| --- | --- | --- |
| Move the teams to the wanted architecture | The architecture is what the product needs, and the skills and ownership can move | A reorganization, with its cost to people |
| Move the architecture to the teams | The teams are well formed around their users, and the software cuts across them | A migration |
| Keep the mismatch and own the contract | The area changes rarely, or a larger change is already planned | A standing contract across the team line, and a named owner for it |

Whichever you choose, you will choose again. Conway ends his paper on that point: the design that occurs first is almost never the best possible, and so "flexibility of organization is important to effective design." His conclusion is about keeping the organization able to change when a better design is found. [[reorganizations]] covers how to carry such a change out.

## Worked Example: Three Team Changes at Corvane

Corvane changed what its teams were or what they owned three times between 2022 and 2024. The two conditions can be checked for each. The table sets the three side by side: the architecture each implied, where the skills were, who owned what, and what followed. Sizes are given in engineers throughout. Lead time in the last column is the time from starting work on a change to its release. A launch is the platform team's scheduled release of another team's change.

| Change | Architecture it implied | Skills | Ownership | Result |
| --- | --- | --- | --- | --- |
| 2022, 45 engineers in four teams: the scheduling and job-status rules move into Core | One rule engine, used by three applications | An engineer in Core already understood both the scheduling engine and the mobile sync | Core owns the code and its published schema; one product manager decides the rules | No third incident of the kind; Core overloaded |
| 2023, growing from 45 engineers to 95: eleven product teams and a platform team of five | Eleven product areas that change and release separately | Launch knowledge stayed with the five platform engineers | The platform team owns the launches | The eleven areas do not release separately; changes queue for launches; median lead time from 4 days to 19 |
| 2024, 95 engineers: a release path that a product team runs itself, tried first with the Scheduling team | The same eleven areas | A platform engineer worked inside Scheduling for the first six weeks | Scheduling owns its own releases | Scheduling's median lead time 6 days after one quarter |

The 2022 change was an inverse maneuver in its smallest form, and it worked: no person changed teams, and one boundary moved. Corvane wanted one rule engine in place of rules scattered over three applications, and it made the Core team the owner of the rules. Both conditions were met. Samir Haddad, a staff engineer in Core, was the one person who understood both the scheduling engine and the mobile sync, so the skill was already in the receiving team. Core was given the code and its contract with the other teams, a versioned schema with a weekly rules session, and Priya Nambiar, the product manager, was given the decision about what the rules are. No third incident of the kind followed. The price was paid in Core, whose six engineers now owned more than they could comfortably understand.

The 2023 change failed as a maneuver, although nobody at Corvane had called it one. The chart drew eleven product teams, with names such as Scheduling and Dispatch, and so it implied eleven product areas that change and release separately. The previous chapter read the same change as a reorganization without a stated outcome. Read through this chapter, it moved the teams to a wanted architecture and made the mistake of The Org Chart as Architecture: the four teams were divided into eleven, and both conditions were missing for one part of the work, the release. The skill of launching stayed with five platform engineers, and the launches stayed in the platform team's ownership. So the software did not become eleven areas that release separately. A team's change still reached customers through another team. All eleven teams needed a launch for some of their changes, and three needed one for every change. By 2024 there were 14 launch requests open, and the median lead time had gone from 4 days to 19. The architecture had not followed the chart.

The 2024 repair did not redraw a single team. The teams and the wanted eleven areas stayed as they were, and the two missing conditions were supplied. Dario Vance, the VP Engineering, and Lena Brandt, who led the platform team, had the release path rebuilt so that a product team could run it without the platform team. That changed the software, and it moved the ownership of releasing to the Scheduling team, which tried it first. A platform engineer worked inside Scheduling for the first six weeks, which moved the skill. After one quarter Scheduling's median lead time was 6 days. The price was a migration: the other ten teams moved to the new path over the following quarters, and the company-wide median went under 7 days three quarters after the change began. The architecture of the 2023 chart began to exist when skills and ownership caught up with it.

## What AI Changes Here

Corvane's three changes date from 2022 to 2024, before agents wrote much of its code, so it is fair to ask whether the mechanism holds when they do. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, in the teams I have observed using coding agents, an engineer with an agent writes a change in code that another team owns far more easily than before. The change then waits for the owning team's review, as it always did. The writing became cheaper and the agreement did not. Conway's argument rests on the cost of agreement between the people who own two parts, and that cost is unchanged. This is my observation, not a measured result.

If that observation holds widely, it changes where the law shows. **Speculative.** Conway's Law would then describe the structure of ownership and review more than the structure of who writes the code, and weak interfaces would appear as review queues on team lines. The claim would be confirmed where organizations report that cross-team changes written with agents wait longer for the owner's review than changes written inside the owning team. [[where-the-constraint-moves]] takes the argument further.

## What to Take Away

**Established.** What the sources agree on:

- Organizations that design systems produce designs that copy their communication structures, because dividing the work is a design decision and every interface between parts has to be negotiated between groups (Conway, 1968).
- A measured comparison of five matched pairs of software products found the mirroring in every pair, without settling its cause (MacCormack, Rusnak and Baldwin).
- Team design is architecture design, technical leaders belong in it, and every part of a system needs exactly one owning team (Skelton and Pais, *Team Topologies*).

**Depends on context.** What changes with the situation:

- Whether to move the teams, move the architecture or keep the mismatch depends on which side fits what the product needs, and on whether skills and ownership can move.
- How much a predicted weak interface matters depends on how often the thing that crosses the line changes. A stable contract on a team line is a good outcome.

**The author's synthesis.** What is this book's own position:

- Skills and ownership as the two conditions of the maneuver are my test. The sources give the parts; the claim that the old architecture reappears when either is missing is mine.
- Reading the law as a cost of communication is my interpretation of Conway.
- Chapter 1 said teams are components, and chapter 2 said whom they are designed for. This chapter adds that the software takes the components' shape. The design of the teams and the design of the software are therefore one design, and the link between them runs through skills and ownership and not through the chart.

## Checklist

The checklist turns the chapter into eight checks. Run them on the next team change or architecture change you plan, before it is announced.

- [ ] List the features, rules and journeys your users experience as one thing.
- [ ] For each, mark every team line it crosses, using who actually talks and not who reports to whom.
- [ ] At each marked line, name the contract for what crosses it and the team that owns the contract.
- [ ] For a team change, write down the architecture the new chart implies, and have a technical leader review it.
- [ ] For an architecture change, list which teams will have to talk for it to ship, and whether they do.
- [ ] Skills: can each new team design, change, release and operate its part without borrowing a person from another team?
- [ ] Ownership: does exactly one team hold the code, the decision rights and the on-call duty for each part?
- [ ] If a mismatch will remain, say so, and name the owner of the contract that covers it.

A customer could have drawn Corvane's teams from its product. You can now say why: the faults sat where design decisions had to cross a team line and nobody had agreed how. You can also check whether a new chart will change the product, by asking what moves with the teams. If team structure decides architecture, the open question is how to choose the structure. The next chapter gives the rule: size what a team owns by its cognitive load, and cut along fracture planes, in [[cognitive-load-and-team-boundaries]].

## Sources and Evidence

**Books**

- *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, Matthew Skelton and Manuel Pais, 2019. The reverse Conway maneuver; team assignments as the first draft of the architecture; team design as architecture design and the need for technical leaders in it; focused communication between teams; exactly one owning team for each part; the joined-at-the-database monolith; skills as an input to team design.

**Research and reports**

- "How Do Committees Invent?", Melvin E. Conway, *Datamation*, April 1968, read at melconway.com. The law as stated; organizing a design effort as a design decision; the negotiated interface and the homomorphism; the compiler example; flexibility of organization. This paper is not on the author's bookshelf and supplements the sources above.
- "Exploring the Duality between Product and Organizational Architectures: A Test of the 'Mirroring' Hypothesis", Alan MacCormack, John Rusnak and Carliss Baldwin, Harvard Business School Working Paper 08-039, 2008, revised 2011. Five matched pairs of open-source and commercial software products compared by propagation cost; the authors' stated limits. Also a supplement to the author's sources.

**Practitioner sources**

- The author's working records of the *Team Topologies* material: [[conways-law]] and [[org-chart-problems]].
- The statements about coding agents under "What AI Changes Here" are the author's observation as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
