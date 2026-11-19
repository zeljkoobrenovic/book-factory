---
title: "Part I — FOUNDATIONS: The Organization as a System"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What kind of thing is a product and tech organization, and what decides how well it works? It is a system whose structure produces its results and whose output is limited by one scarce capacity at a time, and because it exists for its users, changing it is product work."
permalink: part-1
timetoread: 5 min read
---

> **KEY POINTS:**
>
> * **An organization is a system, and its structure produces its results.** It behaves as its team boundaries, interfaces and decision rights make it behave, so replacing people changes little when the structure stays.
> * **Output is limited by one scarce capacity at a time.** Designing an organization means finding that constraint and keeping what each team owns within what the team can understand.
> * **The system has users, so changing it is product work.** A change starts with discovery and is judged by an outcome stated in advance, not by having been carried out.

<br>

Suppose that in 2024 Corvane had replaced every one of its managers and kept its teams, its interfaces and its planning exactly as they were. What would have changed? Corvane is the fictional company this book follows. In 2024 it had 180 people, and its 95 engineers worked in eleven product teams and one platform team of five, which ran the release tooling the product teams shared. Its median **lead time**, the time from starting work on a change to its release, had gone from 4 days to 19, and fourteen launch requests were waiting at the platform team. New managers would have found the same fourteen requests in the same queue on their first morning. **Very little would have changed.**

That answer goes against a habit. When an organization does badly, we explain it by the people involved: a weak lead, a slow team, a manager who does not communicate. Corvane had acted on that explanation once. In 2021, at 50 people, its Web and Mobile teams each built the rule for overlapping jobs in their own way, and planners and technicians saw different schedules for three weeks. The lead of the Mobile team was replaced. Eight months later his successor's team and the Integrations team disagreed about the status of a job in the same way. When a failure outlives the person blamed for it, **something that stayed in place produced it**.

Part I is about what stays in place. It argues that a product and tech organization is **a system**: it behaves as its team boundaries, interfaces and decision rights make it behave, and its output is limited by one scarce capacity at a time. It also argues that the system exists for its users, so changing it is product work. This page states the claim in those two halves, first the system and then its users, and after that explains the reading order. Five chapters answer five questions in order: what kind of system an organization is and what can be changed in it, whom it is for and how changing it is run, why software mirrors the teams that build it, how much one team can own, and where capacity is lost.

## The Claim: The Structure Produces the Result

The structure of an organization is something you can write down. **Boundaries** say which team owns what. **Interfaces** are the agreed ways in which teams work with each other: the contracts between them and the regular meetings where they exchange information. **Decision rights** say who decides what. People respond sensibly to all three, so capable people placed in a structure that overloads them or makes them wait produce what the structure allows.

Three mechanisms explain why the structure decides the result, and each has its own chapter:

- **Software takes the shape of the teams that build it.** Every design decision needs the people who make it to talk, so a product is weakest where teams talk least. This is known as Conway's Law.
- **A team can safely change only what it understands.** The mental effort of understanding what a team owns is its **cognitive load**, and it limits how much one team can own.
- **A flow moves at the pace of its slowest step.** That step is the **constraint**, the place where the one scarce capacity has run out, and work that arrives faster than the constraint can take it only waits.

The rule for designing follows from the three mechanisms. Before you replace people or add headcount, find the constraint, and draw boundaries so that each team's cognitive load stays within what the team can carry. Between 2022 and 2024 Corvane did the opposite, in a period it calls the hiring wave. It doubled its engineers from 45 to 95, and every new engineer joined a team that wrote changes. The changes then waited at the platform team, which still had five people. Capacity added away from the constraint made the queue longer.

## The Second Lens: The System Has Users

A system is built for someone, and Part I's second claim is about whom. The **users** of an organization's design are the people and teams who work in it, the teams that depend on each team and, through them, the customers. The organization owes them **outcomes**: results they can observe, such as a shorter lead time. A change to the organization is therefore product work. It starts with **discovery**, which means finding out from the people affected where the problem is before choosing a structure, and it is judged by an outcome stated in advance. Corvane's hiring wave had neither. It was finished on schedule, and when the board asked in 2024 whether it had worked, the leadership team could not answer.

## Why the Chapters Come in This Order

Five chapters build those two lenses, the system and its users, in prerequisite order: each one supplies the terms the next one needs. Two placements in that order are deliberate. The chapter on users comes second, before most of the structure has been described, so that every rule in the later chapters is read as a means to an outcome and not as a rule to apply for its own sake. The chapter on flow comes last, because you can follow work across team boundaries to the place where it waits only after the boundaries have been explained.

## Chapters in this part

Each of the five chapters answers one question:

- [[the-organization-as-a-system]] — What kind of system is an organization, and what in it can a leader design?
- [[the-organization-as-a-product]] — Whom is the organization for, and how should a change to it be run?
- [[conways-law-and-the-inverse-conway-maneuver]] — Why does software end up shaped like the teams that build it, and when can a leader use that on purpose?
- [[cognitive-load-and-team-boundaries]] — How much can one team own, and where should the boundary between two teams go?
- [[flow-and-the-constraint]] — Where is delivery capacity lost, and what recovers it?

Read in order, the five answers are one line of reasoning. The structure produces the result, the result is judged by what it does for the users, the arrangement of teams shapes the product, the size of what a team owns limits what it can do well, and the slowest step sets the pace of all of them. By the end of the fifth chapter you can explain Corvane's slowdown without blaming a person or a team, and you can say why new managers would have found the same queue. If you arrive with one question, open the chapter that answers it; otherwise read in order. So far the claim is that an organization behaves as its structure makes it behave. The first chapter says what that structure consists of. It names the four elements of the system, the four things a leader can design, which are the three given above and the incentives, and the three scarce capacities, attention, judgment and verification, any one of which can be the constraint: [[the-organization-as-a-system]].

## Sources and Evidence

Every source is named and dated in the chapter that uses it, under that chapter's Sources and Evidence. Conway's Law is from Melvin Conway's paper "How Do Committees Invent?" (1968); cognitive load as the measure of what a team can own is from *Team Topologies* by Matthew Skelton and Manuel Pais (2019). Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
