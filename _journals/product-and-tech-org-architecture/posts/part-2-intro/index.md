---
title: "Part II — TOPOLOGY: Teams and Their Interfaces"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Which kinds of teams does an organization need, how should they work with each other, and how large should they be? Four team types and three ways of working together, chosen so that the teams that deliver to users carry the least load and wait the least, with a team size that is derived and not copied."
permalink: part-2
timetoread: 5 min read
---

> **KEY POINTS:**
>
> * **Every team has to pass one test.** Whose load does it lower, and whose waiting does it remove? The teams that deliver to users are where value is produced, and every other team exists for them.
> * **Four team types and three interaction modes are enough.** The type says what a team is for, the mode says how other teams reach it, and both are written down where others can read them.
> * **Team size is derived, not copied.** It follows from the load a team carries, the on-call rotation it must sustain and the cost of coordinating inside it.

<br>

In 2022 Corvane formed a platform team of five engineers so that its product teams could release faster. Corvane is the fictional company this book follows, and a **platform team** is a team that provides something other teams would otherwise each build for themselves, in this case the shared release tooling. Lena Brandt led it. In 2023 Corvane formed eleven product teams. By 2024, at 180 people, fourteen launch requests were open at the platform team, and a change that took about two days to write waited about seventeen more for a launch slot. The team created to remove a wait had become **the place where launches waited**.

You have probably met a team like this one. It was set up to help the others, as a platform team, a quality team, an architecture group or a security review, and a year later it is the queue everyone complains about. The usual explanations are about staffing and speed: the team is too small, or it is too slow. Two other questions explain more. **What kind of team was it meant to be? And how were the other teams meant to use it?** Corvane's 2022 plan answered neither. It gave the platform team a purpose and a headcount, and it did not say what kind of team this was or how eleven teams would use it.

Part II answers both questions, the kind of team and the way others use it, for every team. It argues that an organization needs **four team types** and **three ways for two teams to work together**, chosen so that the teams that deliver to users carry the least load and wait the least. A team's size follows from the load it carries, its on-call duty and the cost of coordinating inside it, and each of these choices is written down where others can read it. This page gives the test behind that claim, and applies it to the three choices of type, mode and size, in the order in which they depend on each other. Three chapters then answer three questions in order: which kinds of teams an organization needs, how they should work with each other, and how large they should be.

## The Test: Whose Load, Whose Waiting

Part I ended with rules, and two of them produce one test, which I call the load-and-waiting test. The first is that a team can own only what it understands; the effort of understanding it is the team's **cognitive load**. The second is that output is set by the slowest step, so most delivery time goes into waiting between teams. Now look at where value is produced: in the teams that build and run something users use, from the request to the release. Load limits what those teams can own, and waiting limits how fast their work arrives. Any other team, and any dependency between teams, therefore has to pass the test. **Whose load does it lower? Whose waiting does it remove?** A team or a dependency that does neither is overhead, and a leader can refuse it. The lead's two questions, what kind of team and how others use it, are settled by applying this test, as the next section shows.

## Three Choices: Type, Mode and Size

The load-and-waiting test is applied to three choices. The first choice is what a team is for. *Team Topologies*, by Matthew Skelton and Manuel Pais, names the four team types listed below, and Part II argues that four are enough. The first type in the list is the kind that delivers to users. Each of the other three exists for it, and is justified only by the load or the waiting it takes off teams of the first type:

- A **stream-aligned team** owns one flow of user value from end to end. It is the default.
- A **platform team** removes mechanics, such as release tooling, that stream-aligned teams would otherwise each carry.
- An **enabling team** helps other teams close a skill gap, and then leaves.
- A **complicated-subsystem team** holds knowledge too specialized to spread across teams.

The second choice is how two teams work together. *Team Topologies* names three **interaction modes**. In **collaboration** two teams work closely together for a limited time. In **X-as-a-Service** one team uses what the other provides without having to talk to it. In **facilitating** one team helps the other learn. The mode should be chosen deliberately and written down in a **team API**, a short document that says what the team owns, how to ask it for something and what it promises. The test decides between them: the right mode is the one that leaves the teams delivering to users waiting least. An interaction that nobody chose still takes place, and it turns into a queue of requests or a meeting that never ends.

The third choice is how many people a team has. Will Larson's rule of thumb in *An Elegant Puzzle* is six to eight engineers for one manager. Part II treats that number as the result of a derivation and not as a rule. Three things go into the derivation: the load the team carries, the **on-call rotation** it must sustain, which is the schedule by which its members take turns answering alarms outside working hours, and the cost of coordinating inside the team. Six to eight is what the derivation gives under stated assumptions, and when the assumptions change, the number changes.

The three choices depend on each other in one direction. A mode is chosen between two teams, and you can choose it only when you know what type each of them is. A size depends on what the team owns, which its type decides, and on how much of its time other teams take, which its modes decide. So types come first and size comes last. Corvane's 2022 plan went the other way. It fixed the platform team at five before saying what the team would own or how eleven teams would reach it. A size chosen first is a number with nothing to derive it from.

## Chapters in this part

Each of the three chapters answers one question:

- [[team-types]] — Which kinds of teams does an organization need, and when is each one justified?
- [[interaction-modes-and-team-apis]] — How should two teams work together, and how is that agreement written down?
- [[team-size-and-composition]] — How large should a team be, and who should be in it?

The three chapters ask one question about a team from three sides: what it is for, how others reach it, and how many people that takes. For its platform team of five, Corvane's 2022 plan left the first two unanswered and answered the third with a bare number. With the three answers you can put every team in your own organization to the load-and-waiting test, and refuse a new team or a new dependency that passes neither part. If you arrive with one question about a team, open the chapter that answers it; otherwise read in order. So far the claim is that few team types are needed, and that each is justified by what it does for the teams that deliver to users. The first chapter takes the four types one by one, with the test for each: [[team-types]].

## Sources and Evidence

**Books**

- *Team Topologies: Organizing Business and Technology Teams for Fast Flow*, Matthew Skelton and Manuel Pais, 2019. The four team types, the three interaction modes and the team API, named here and treated in the chapters.
- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. The rule of thumb of six to eight engineers for one manager.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
