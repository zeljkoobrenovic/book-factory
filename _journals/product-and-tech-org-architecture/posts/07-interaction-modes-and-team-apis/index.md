---
title: "Interaction Modes and Team APIs"
date: 2026-11-19
author: Željko Obrenović
excerpt: "How should two teams work together, and how is that agreement made explicit? In one of three modes, chosen on purpose and written down on one page that says what a team owns, how to ask it for something and what it promises."
permalink: interaction-modes-and-team-apis
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to choose one of three interaction modes for a pair of teams and to write the choice down as a one-page team API.

> **KEY POINTS:**
>
> * **Two teams work together in one of three modes.** Collaboration is for discovery and has an end date, X-as-a-Service is for use without talking, and facilitating is for teaching a skill.
> * **A mode nobody chose becomes a queue or a standing meeting.** People fall back on asking each other, which is collaboration without an end date.
> * **The choice is written down in a team API.** One page says what the team owns, how to ask it for something, what it promises and how it communicates.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Review Bottleneck** — a service that was never defined turns its provider into a gate every request passes through.
> * **The Unowned Interface** — an interaction nobody chose has no owner, so it changes when a manager leaves.
> * **The Overloaded Team** — a team in collaboration with all its neighbors at once has little attention left for what it owns.

<br>

In 2022 Corvane formed a platform team of five engineers to help its product teams release faster. Corvane is the fictional company this book follows. By 2024, at 180 people, eleven product teams waited on that team for their launches, 14 launch requests were open, and the median lead time for a change had gone from 4 days to 19. Nobody had decided how a product team should use it. If you have a team that everyone waits on, or a weekly cross-team meeting that nobody remembers starting and nobody dares to cancel, you have seen the same thing: **an interaction between two teams that nobody chose**.

This chapter argues that two teams should work together in one of three **interaction modes**: collaboration, for a limited time, while a boundary between them is still being discovered; X-as-a-Service, when one team can use what the other provides without talking to it; and facilitating, when one team helps the other learn. The choice should be written down in a **team API**, a page that says what a team owns, how to ask it for something and what it promises. A mode nobody chose shows up as a dependency queue or a meeting that never ends. The modes and the team API are the concrete forms of the interface lever of [[the-organization-as-a-system]]. The chapter starts with Corvane's platform team, defines the three modes and their costs, and explains why an unchosen mode turns into a queue or a standing meeting. It then describes the team API with a filled-in example, gives two patterns (choosing a mode for a pair of teams, and giving every collaboration an end date and an exit), shows the common misuses and where the sources disagree, reads Corvane's case again and ends with what AI changes.

## Setting the Scene: A Service Nobody Defined

Here is how a launch worked. From 2023 Corvane had eleven product teams and one platform team, led by Lena Brandt, which held the deployment scripts. A product team that wanted to release a change filed a launch request. One of the five platform engineers then went through the change by hand: its database migrations, its configuration, and the way back if the release failed. Then that engineer released it in a scheduled slot. All eleven teams needed the platform team for some launches, and three needed it for every launch.

The request form was the only part of that relation that had been written down. Three things had never been decided. Nobody had said what the platform team offered: a check, a release, advice, or all three. Nobody had said how a product team should ask beyond filing the ticket. And nobody had said what the platform team promised in return: how long a launch would take, or what a product team could count on doing without it.

Something fills such a gap, and at Corvane it was a person. The platform engineer could not judge a change alone, so an engineer from the product team sat in on each check. Each launch was a small piece of joint work. Five engineers cannot do joint work with eleven teams at once, so the work lined up. At the peak in 2024, 14 launch requests were open, and of the 19 days of median lead time about 17 were spent waiting for a slot. The queue was nobody's decision, which is why nobody could undo it.

## Three Interaction Modes and What Each Costs

Corvane lacked words for the choice it had not made. An **interaction mode** is the way two teams have agreed to work together for the time being. In *Team Topologies*, Matthew Skelton and Manuel Pais name three: collaboration, X-as-a-Service and facilitating. Their starting point is that "not all communication and collaboration is good". Chapter 1 called any agreed way for work or knowledge to cross between teams an interface, and [[conways-law-and-the-inverse-conway-maneuver]] called such an agreed way a **team interface**, to keep it apart from a software interface. A mode is the form a team interface takes between two particular teams. The modes apply between teams of the four types of the previous chapter, [[team-types]]: stream-aligned teams, which own a flow of user value end to end; platform teams, which take shared mechanics off them; enabling teams, which close a skill gap and leave; and complicated-subsystem teams, which hold specialist knowledge.

The three modes differ in what the two teams do, in who pays and when, and in when the mode should end. The table sets them side by side.

| Mode | What the two teams do | Who pays, and when | Right when | Ends when |
| --- | --- | --- | --- | --- |
| Collaboration | Work on one problem together, as one team would | Both teams, for as long as it lasts | Something between them is still unknown: a boundary, an interface, a new technology | The unknown is settled, or the agreed date arrives |
| X-as-a-Service | One provides; the other uses it without talking to the provider | The provider, up front; the consumer almost nothing afterwards | The consumer can use what is provided without help | The service no longer fits what its consumers need |
| Facilitating | One helps the other learn to do something itself | The helping team, now | One team lacks a skill the other can teach | The helped team can do it alone |

Collaboration means two teams working on one problem as if they were one team. It is the fastest way to discover something, because nothing is handed off. Skelton and Pais state the price in the same sentence as the benefit: "Collaboration is good for rapid discovery and avoiding hand-offs and delays, but the downside is a higher level of cognitive load." Each team has to keep part of the other's world in mind, and that takes attention. The cost runs for as long as the collaboration does, so it is worth paying only while a boundary or an interface between the two teams is still unknown. The authors' rule of thumb is that a team collaborates with at most one other team at a time.

X-as-a-Service has the opposite cost. One team provides something, and another uses it without talking to the provider. The provider pays up front, in the work of making the thing usable by a stranger: documentation, sensible defaults, versions that do not break their users. The consumer pays almost nothing afterwards. The mode has a condition, which the authors put this way: "The X-as-a-Service model works well only if the service boundary is well chosen and well implemented, with a good service-management practice from the team providing the service."

Facilitating moves a skill, where the first two modes get work done. One team helps another learn to do something itself, such as running its own load tests. The helping team pays now, in the time of people who could have been building. It does not take over the helped team's work, and both sides know the help is temporary. Facilitating is finished when the helped team no longer needs it, so it has an end by definition.

## Why an Unchosen Mode Becomes a Queue or a Standing Meeting

With the modes defined, Corvane's default has a name. When nobody chooses a mode, people who need something from another team ask someone in it. Asking, and working out the answer together, is collaboration. But it is collaboration without the two limits that make it affordable: it has no end date, and it is not restricted to one other team. What it turns into depends on the direction of the need. When one team needs the other, the requests line up at the team that is asked, and the result is a dependency queue. When both need each other, the two teams set up a recurring meeting, and the meeting never ends because the need never does.

Four things you can observe from outside tell you that a mode was not chosen or is the wrong one.

| What you see | Mode in practice | Mode the work probably needs | What is missing |
| --- | --- | --- | --- |
| A ticket queue at one team that many teams wait on | Collaboration with every requester, one at a time | X-as-a-Service | A defined service that requesters can use themselves |
| A recurring meeting of two teams, neither of which can release alone | Collaboration with no end date | X-as-a-Service, or one team in place of two | An interface between them with an owner, or a different boundary |
| Consumers of a service who ask for help every time | A service in name, collaboration in fact | X-as-a-Service | Documentation and defaults that replace the help |
| A helping team still doing the work after a year | Facilitating in name, a hand-off in fact | Facilitating with an end | An end date |

A recurring meeting between teams is not always a symptom, though. In 2022, when Corvane had about 45 engineers, it moved its scheduling rules into one rule engine in the Core team and set up a weekly rules session. Core owned the session. Its purpose was to review changes to the rules. Its output was a new version of a published schema, and the product manager, Priya Nambiar, decided what went into it, on record. That meeting was a team interface someone had designed. The test is whether a meeting has an owner, a purpose and an output.

The rules session lasted because it had an owner and a written output. A mode that is chosen and only spoken does not last. Chapter 1 described two engineers who talk every Thursday as an interface that leaves the company with either of them. Two managers who have an understanding about how their teams work together hold an agreement that nobody else can read, and it lasts as long as their relationship does. When one of them moves on, the successor inherits the tickets and the meetings without the understanding, and the two teams fall back to the default. An agreement that is to outlive the people who made it has to be written where both teams, and their next managers, can find it.

## The Team API: The Agreement Written Down

The page on which an agreement between teams is written has a name. Skelton and Pais call it a **team API**: the written description of how to work with a team. A software API tells a program how to use a service without knowing its insides, and a team API tells another team how to use this team without knowing its people. In the terms of the chapter on Conway's Law it describes the team's team interfaces, and the software interfaces the team owns are one item on it. In the authors' description it covers the code and endpoints the team owns, versioning, documentation, working practices, communication channels and current priorities. My own working notes on the book, [[team-first-thinking]], distill that list.

Those contents reduce to four questions that someone outside the team would ask. I add a fifth part, which is my extension and not the source's: the team's current interactions, each with its mode and its end date.

| Part | The question it answers | What goes in it |
| --- | --- | --- |
| What we own | Whose is this? | The services, code, data and decisions the team owns, and what it does not do |
| How to ask us | How do I get something from you? | What needs no asking; the channel for questions; the form of a request |
| What we promise | What can I count on? | Response times, notice of changes, compatibility, each with a number |
| How we communicate | How do I find out what is changing? | Channels, changelog, roadmap, the person to escalate to |
| Current interactions | Whom are you working with, in which mode, until when? | One line per team: mode, purpose, end date |

Here is a filled-in example. In 2024 Corvane's platform team replaced its hand check with automated readiness checks that a product team runs on its own change, and with a release path: the tooling that then releases the change without the platform team. One product team, Scheduling, tried the path first, in a pilot quarter. For the first six weeks a platform engineer worked inside Scheduling, and the platform team repeats that stay with each team that joins. The worked example later in this chapter tells that story. The platform team wrote its team API at the end of that pilot, and the page fits on one sheet.

| Platform team | Team API, end of the 2024 pilot |
| --- | --- |
| **What we own** | The release path: the automated readiness checks and the release tooling. The deployment scripts. The shared infrastructure: hosting, databases and monitoring. The shared data model for customers and jobs. |
| **What we do not do** | We do not check or release a change for a team. A team that runs the release path owns its release. |
| **How to ask us** | To release: nothing to ask. Run the release path as described in the Platform handbook. A question: post it in #platform-help. A change to a readiness check or to the shared data model: file a change request that says what you need, by when and what you have tried. |
| **What we promise** | A question is answered within one working day. A change request gets a yes, a no or a date within five working days. A readiness check changes only after two weeks' notice. The shared data model is versioned, and the previous version keeps working for one quarter. An alert from the release path or the shared infrastructure is answered at any hour by the platform engineer on call. |
| **How we communicate** | #platform-help for questions. A changelog every second Monday. A roadmap, reviewed with the product team leads once a quarter. Escalation: Lena Brandt. |
| **Current interactions** | X-as-a-Service: Scheduling, on the release path, no end date. Facilitating: one platform engineer inside each team that joins the release path, six weeks at most, end date set on the first day. Launch requests: still accepted from teams not yet on the release path, until each has joined. |

Four things in that page are worth copying. It says what the team does not do. Its promises carry numbers. Each interaction has a mode and an end date. And the page was written for a particular user: an engineer in a product team who has never spoken to anyone on the platform team. The measure of a team API follows from that user. Count the share of what other teams need from this team that they get without a person on this team being involved, and ask one consumer what the team promises.

Many organizations already have a document close to this one, the team charter. The charter template in the workbooks to Claire Hughes Johnson's *Scaling People* has eight sections. Six describe the team itself, from mission to risks. Two face other teams: the interfaces the team provides and the interfaces it depends on. A team API is that outward-facing part, extended with how to ask and what is promised.

## Pattern: Choose a Mode for Each Pair of Teams

A team API records a mode, and somebody has to choose it. The users of this pattern are the leads of the two teams and the manager they share. It worked if both teams, asked separately, name the same mode and the same end date, if neither is in collaboration with more than one other team, and if the wait at the dependency between them falls. The procedure has four steps.

1. Name the pair and what crosses between them: requests, changes, questions, a skill.
2. Ask three questions in order. Is something between the two teams still unknown? Can one team use what the other provides without talking to it? Does one lack a skill the other can teach?
3. Write the mode, its purpose and its end date into both team APIs.
4. Set the date on which the two leads read that line again.

The order of the three questions in step 2 matters, because an unknown rules out a service: a team cannot define well what the two teams have not yet understood. If the honest answer to the second question is "it could, once the service is defined", then the service is the unknown and the answer to the first question was yes. The last outcome in the figure is easy to forget: most pairs of teams in an organization need no standing interaction at all.

---begin mermaid---
flowchart TD
    A["A pair of teams"] --> B{"Is something between them still unknown?"}
    B -->|"yes"| C["Collaboration, with an end date"]
    B -->|"no"| D{"Can one use what the other provides without talking to it?"}
    D -->|"yes"| E["X-as-a-Service"]
    D -->|"no"| F{"Does one lack a skill the other can teach?"}
    F -->|"yes"| G["Facilitating, until the skill has moved"]
    F -->|"no"| H["No standing interaction"]
    C -->|"when the unknown is settled"| D
    G -->|"when the team can do it alone"| D
---end mermaid---

**Figure 1:** *Three questions, asked in order, choose the mode for a pair of teams, and the two temporary modes lead back to the second question.*

The team types of the previous chapter shorten the procedure, because they supply a default. In Skelton and Pais's account, platform teams and complicated-subsystem teams mostly provide what they own as a service, enabling teams mostly facilitate, and stream-aligned teams collaborate only when there is something to discover. A pair whose mode contradicts its types is a signal that one team is misdescribed. A platform team whose every consumer needs a conversation is not yet providing a platform, and an enabling team that ships features for other teams is a second delivery team.

## Pattern: Give Every Collaboration an End Date and an Exit

Collaboration is the one temporary mode that does not end by itself, so it gets a rule of its own: every collaboration has an end date on the day it starts. The same goes for a facilitation, although that has a natural end. The users are again the two teams' leads, and the measure is the number of collaborations in the organization that are past their date. The source gives the end condition and not the date: "Collaborate on potentially ambiguous interfaces until the interfaces are proven stable and functional." Setting a date, in weeks and not in quarters, is my recommendation. It makes two people check the condition on a known day, where otherwise nobody would.

When the date arrives, the collaboration leaves by one of three exits.

- **A service.** This needs three things: a defined interface between the two teams, one team that owns it, and a consumer who can use it without talking to the owner.
- **A boundary change.** If no interface can be drawn, because nearly every change still needs both teams, the line between the teams is in the wrong place. The teams are merged, or the thing both keep changing moves to one of them. [[cognitive-load-and-team-boundaries]] gives the test for where the line belongs.
- **One renewal.** The unknown is still unknown, for a reason the two leads can write down. The collaboration gets a new date, once.

## Anti-Patterns: Collaboration Everywhere, the Service That Is Not One, the Page Nobody Reads

The modes and the page have recognizable misuses. The most common is collaboration as the default for every pair of teams. This is one way to produce **The Overloaded Team**: the team has not been given more to own, but it has been given more to keep in mind. Skelton and Pais name a second cost: "Unnecessary collaboration is particularly expensive, especially as it can mask or hide deficiencies in underlying platforms or capabilities."

The other two modes are faked more often than they are overused. A service whose consumers must ask for help each time is a queue with a service's name, and it is how an interface becomes **The Review Bottleneck**: every request passes through the people who provide the service. Corvane's Launch Queue of 2024 is this book's case of it. The facilitating version is a helping team that does the work. An enabling team that writes each team's load tests has moved no skill and has become a dependency.

The team API has its own two misuses. One is the wall: a page that lists what the team will not do and how long everything takes, written to keep requests away. The other is the page written once and never read again. Its promises go stale, people go back to asking whomever they know, and the crossing between the two teams is again **The Unowned Interface** of chapter 1.

## Where the Sources Disagree: Written Contracts or Cooperation

The wall is why one of this book's sources would distrust the whole idea. *Team Topologies* holds that communication between teams should be limited and defined: "What we need is focused communication between specific teams." In *Six Simple Rules*, Yves Morieux and Peter Tollman give the opposite advice: "Resist the pressure to clarify roles, decision rights, and processes." Their reason is that clarity beyond a threshold lets people comply with what is written and stop caring about what falls outside it.

I think both sources are right, about different things. Morieux and Tollman are right that a document cannot produce cooperation, and that one written to limit responsibility destroys it. Skelton and Pais are right that a relationship does not reach past the people in it. A team API respects both when it describes the way in: how to reach the team and what it promises. It says nothing about what the team's members may decline to care about, and collaboration remains the right mode whenever something is unknown. The table says when each amount of writing fits.

| Choice | What you gain | What you lose | Fits when |
| --- | --- | --- | --- |
| Unwritten, by relationship | No overhead; flexible | Lost when either person leaves; invisible to newcomers | Everyone still knows whom to ask: one team or a few |
| A one-page team API | Readable by strangers; survives a change of manager | An hour to write and a re-read every quarter | A consumer would not know whom to ask, or a manager is new |
| A detailed service contract | Precise expectations for many consumers | Compliance with the letter; slow to change | Many consumers, a stable service and a real cost of failure |

## Worked Example: Corvane's Platform Team Changes Mode

Corvane's platform team can now be read by mode. In 2024 Dario Vance, the VP Engineering, and Lena Brandt introduced the release path, starting with Scheduling's pilot quarter. The table follows the relation between the platform team and the product teams through five periods.

| Period | Mode in practice | Chosen? | What existed | Result |
| --- | --- | --- | --- | --- |
| 2023 to 2024: launch requests | Collaboration with eleven teams, one ticket at a time | No | A request form | 14 open requests; median lead time 19 days |
| Pilot, weeks 1 and 2, with Scheduling | Collaboration on one question: which hand checks can be automated | Yes, for two weeks | A named question and an end date | An agreed set of automated readiness checks |
| Pilot, weeks 3 to 6 | Facilitating: the platform engineer teaches Scheduling to run the release path | Yes, for four weeks | The checks and an end date | Scheduling releases without the platform team |
| Pilot, from week 7 | X-as-a-Service | Yes | The release path, owned by the platform team | Scheduling's median lead time 6 days after the quarter |
| The two quarters after the pilot | Facilitating for each team that joins, then X-as-a-Service | Yes, six weeks at most per team | The same | Company-wide median 8 days after the first of the two quarters, and under 7 a quarter later |

The table shows what did and did not change. Nobody was added to the platform team, and no team was redrawn. What changed is that a mode was chosen, three times in a row, and that three things existed by the seventh week that had not existed in 2023: a defined service, which was the release path with its checks; an owner for it, the platform team; and an end date for the engineer's stay in Scheduling. The first two, with a consumer able to use the service alone, are what a collaboration needs in order to end in a service, and the third is the end date every collaboration starts with.

The change had a price. The platform team paid up front: the readiness checks had to be built before any product team benefited. And for the six weeks of the stay, four platform engineers handled the launch requests of the other ten teams.

A second pair of Corvane teams left an unchosen collaboration by a boundary change. The rule engine that sat in Core in 2022 was divided in 2023, when Core was dissolved: the Scheduling team got the scheduling rules and the Dispatch team the job-status rules. In the first half of 2024, 23 of 31 rule changes needed both teams. Nobody had chosen that collaboration, and no interface could have ended it, because the line between the two teams ran through the thing both kept changing. In 2025, at about 500 people, Corvane moved the line, and Scheduling got the whole rule engine. With one owner again, the versioned rule schema could serve as the interface between the two teams. Two quarters later, 3 of 28 rule changes needed both.

## What AI Changes Here

Corvane changed mode in 2024, before its teams used coding agents, so the last question is what agents change. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Emerging.** As of November 2026, the teams I have observed that use coding agents write down for the agent what a colleague would have asked in person: instruction files in the repository that say how to build and test the code and which conventions to follow. This is my observation and not a measured result. An agent reads what is written and has no hallway to ask in, so the written part of an interaction is the only part an agent can use. A team API written for a stranger in another team also serves an agent working for that stranger.

**Speculative.** If agents make changes cheaper to produce, requests reach provider teams faster, and an interaction handled by people falls behind sooner than one a consumer can use alone. Corvane's later history illustrates the reasoning and is not evidence for it. In 2027–2028, at 1,100 people, merged changes per week rose 2.4 times while review capacity stayed flat, and the median wait for a review went from 5 hours to 31. Review at Corvane was an interaction that passed through people. The claim would be confirmed where queues at provider teams grow in step with their consumers' change volume and self-service interfaces do not. [[agentic-delivery]] and [[where-the-constraint-moves]] weigh the published evidence.

## What to Take Away

**Established.** What the source states:

- Two teams work together in one of three modes: collaboration, X-as-a-Service and facilitating (Skelton and Pais, *Team Topologies*).
- Collaboration buys discovery at the price of cognitive load, and X-as-a-Service works only with a well-chosen, well-run service boundary (Skelton and Pais).
- A team describes how to work with it in a team API (Skelton and Pais).

**Depends on context.** What changes with the situation:

- How long a collaboration lasts depends on what is still unknown. The source gives a condition; the date is my recommendation.
- How much to write down depends on size. Where everyone knows whom to ask, a team API is overhead; where a consumer would not know, it is the least structure that works.
- Which exit a collaboration takes depends on whether an interface can be drawn between the two teams. If none can, change the boundary.

**The author's synthesis.** What is this book's own position:

- Reading a dependency queue and a standing meeting as modes nobody chose is my application of the source's modes.
- The fifth part of the team API, current interactions with a mode and an end date each, and the three exits are mine.

## Checklist

A mode and a team API are one decision at two moments. The mode is what two teams agree, and the team API is what remains of the agreement when the people who made it are not in the room. When nothing was agreed, what remains is a queue or a standing meeting. So read each recurring cross-team meeting and each dependency queue as a question: which mode is this, and did anyone choose it? Then run these eight checks on your own team.

- [ ] List the teams your team interacts with every week, and what crosses between you and each.
- [ ] For each, name the mode in practice, and say whether anyone chose it.
- [ ] For each recurring cross-team meeting, name its owner, its purpose and its output; cancel or redesign one that has none.
- [ ] For each queue your team waits in or runs, say what a requester would need in order not to ask.
- [ ] Give every collaboration and every facilitation an end date, and check that your team collaborates with at most one other team.
- [ ] For each collaboration past its date, choose an exit: a service, a boundary change, or one renewal with a written reason.
- [ ] Write your team API on one page: what you own and do not do, how to ask, what you promise, how you communicate, your current interactions.
- [ ] Ask one consumer what your team promises, and correct the page until the answer matches it.

In 2023 Corvane's platform team of five lacked something before it lacked people. It lacked a page: a defined service, a way to ask and a promise. The page still leaves one question open. A team's type decides what it owns, and its modes decide how much of its time other teams consume: collaboration takes attention every week, and a service has to be kept running. Together they decide how many people the team needs, and in which roles. The next chapter derives that number: [[team-size-and-composition]].

## Sources and Evidence

**Books**

- *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, Matthew Skelton and Manuel Pais, 2019. The three interaction modes and the cost of each; the condition for X-as-a-Service; collaborating on ambiguous interfaces until they are stable; the cost of unnecessary collaboration; team interfaces and focused communication; the team API; the typical modes of each team type.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. The warning against clarifying roles, decision rights and processes beyond a threshold.
- *Scaling People: Tactics for Management and Company Building*, Claire Hughes Johnson, 2023. The team charter of the companion workbooks, with its provided and dependent interfaces.

**Practitioner sources**

- The author's working records and checklists on *Team Topologies*: [[team-interaction-modes]], [[team-first-thinking]], [[evolve-team-structures]] and [[team-topologies-operating-model]]. The team API's contents and the typical modes by team type are cited through these records.
- The author's record of the team charter template: [[team-charter]].
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
