---
title: "Quality and Reliability as Operating Model"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Who owns quality and reliability, and where do the checks sit? The teams that ship and operate the software own both: the checks run in the delivery path on every change, the team that builds a service carries its pager, and specialists teach instead of approving."
permalink: quality-and-reliability
timetoread: 20 min read
---

> **IN THIS CHAPTER, YOU WILL:** decide where ownership of quality and reliability sits, where the checks go, and how to answer a proposal for a gate, including an auditor's.

> **KEY POINTS:**
>
> * **The team that ships owns quality and reliability.** A separate team that tests or approves other teams' work becomes a queue, and it teaches the building team that quality is someone else's job.
> * **Checks, pager and review form one loop.** Checks run in the delivery path on every change, the team that builds a service is paged for it, and each incident review ends in a changed check, alert or runbook.
> * **Independence is a property of a check.** A second team member's recorded review, automated checks the author cannot alter and a release log give an auditor what a separate approving team was meant to give.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Review Bottleneck** — a QA team or a launch gate that signs off other teams' releases gathers verification into one approval queue.
> * **The Hero Culture** — an incident review that thanks the rescuer and changes nothing keeps the organization in need of rescue.

<br>

On a Thursday evening in May 2026, a release took down the service that tells technicians which parts they carry. It happened at Corvane, the fictional company this book follows, which had about 500 people and about thirty teams that year. The alert reached a platform engineer who had never seen the service and could not take the release back. Thirteen hours passed before the parts lists returned, and technicians began the next morning's jobs without them. Within a week, the director of the product group concerned proposed a central QA team of ten testers to sign off every release. Customer-reported defects had doubled in a year. If you have sat in the meeting after a bad incident, you have heard the sentence: **from now on, someone independent checks everything**.

Whether such a team would help depends on who owns quality and reliability and where the checks sit, and this chapter answers the proposal by answering that. The previous chapter gave teams a platform that carries the shared mechanics of building and releasing. This one is about what teams do every day on top of it to keep what they ship correct and running. It argues that **quality and reliability are owned by the teams that ship and operate the software**. The checks sit in the delivery path, where they run on every change. The team that builds a service carries its on-call. Incidents are reviewed to change the system. Quality and reliability specialists work as enabling teams, which raise the teams' own practice and do not act as a gate. The chapter starts with the night and the proposal, and compares the places where ownership of quality can sit. It then takes three patterns: checks in the delivery path, the team that builds a service running it, and launch readiness without a launch gate. It answers the strongest objection, that a check must be independent of the author and that auditors require this. It ends by deciding Corvane's proposal and with what AI changes about verification.

## Setting the Scene: Thirteen Hours and a Proposal

The night is worth following hour by hour, because three things were missing in it. The Parts team, six engineers formed in 2025, released at 17:40 with its own deployment script. The parts service began to return errors, and an alert fired. The team had no **on-call rotation**, which is a schedule of who must answer alerts from production at any hour. Alerts for a service without a rotation fell through to the platform engineer on call, as the owner of the shared monitoring, and she was paged at 18:05. She did not know the service. She could not take the release back either, because the team's script had no step for returning to the previous version. And the change had been tested by one person, the engineer who wrote it. A Parts engineer was reached at 06:30, and the service was restored at 07:10. So the team that built the service was **not on call** for it, the release had **no way back**, and the change had passed **no check but its author's**.

The proposal followed from that night, and it sounded right. Defects reported by customers had gone from 22 a month in the first half of 2025 to 47 in the first half of 2026, and nobody independent had looked at the change that failed. A QA team that signs off every release answers both observations at once. Corvane had heard the proposal before. In 2024, at 180 people, two engineering managers asked for a QA team of six. Dario Vance, the VP Engineering, declined and hired two quality engineers to teach the teams instead, as [[team-types]] tells. That chapter decided whether such a team should exist. It left open the question that came back at 500 people with a larger number attached: **who owns quality and reliability, and where do the checks sit?**

## Principles: Where Ownership of Quality Can Sit

Ownership of quality can sit in three places, set out in the table below. Two terms come first. An **escaped defect** is a fault that a customer finds after release, and it is the plainest measure of what the checks missed. An **enabling team**, defined in [[team-types]], is a small group of specialists who work with one team for a limited time so that the team can afterwards do the work alone. The three placements follow the three team patterns in my record [[quality-engineering-enablement]]; the costs in the third column are my reading.

| Where ownership sits | Who learns that a change is wrong | What it costs | When it fits |
| --- | --- | --- | --- |
| A separate QA or release team tests and approves | The testers, days after the change was made | A hand-off and one shared queue for every team; the building team stops asking whether its own change is right | A check that a regulator or a contract assigns to an independent function |
| A tester placed permanently in each team | The team, through one of its members | One specialist per team, who can become the only person who cares about quality | High product risk, or a team still learning to test |
| The team owns quality, and specialists enable | The author and the team, within minutes or hours | Engineers' time spent on checks, and a slower team while it learns | The default, for teams that release their own changes |

The first placement costs most, for two separate reasons. The first is the queue. **Verification** is knowing that what was built is correct, and [[flow-and-the-constraint]] showed that it is one of three capacities that run out as an organization grows. A team that approves everybody's releases gathers that scarce capacity in one place, and finished work waits there. The second reason would remain even if the gate were fast. A team whose changes are checked by others learns that quality is someone else's job, and the people who find a defect are no longer the people who can prevent the next one. My record calls this anti-pattern "quality as permission". Will Larson reaches the same judgment in *An Elegant Puzzle*, where he advises the reader to "treat gatekeeping as a significant implementation bug rather than as a stability feature to be emulated."

Published research points the same way. *Accelerate*, by Nicole Forsgren, Jez Humble and Gene Kim, reports a research program that continues under the name DORA. I own the book and have no notes on it, so I cite the research through DORA's own guides, read in November 2026, and through my record [[org-health-and-flow-metrics]]. DORA's catalog of **capabilities**, the practices it associates with delivery performance, includes test automation, continuous integration, deployment automation, monitoring and a streamlined change approval. Its guide to test automation reports that performance improves when developers are primarily responsible for creating and maintaining the automated tests. Each of these is a property of a team and its path to production, and none is a department.

The same research supplies the measures by which this chapter judges quality. It measures delivery with four measures: lead time for a change, deployment frequency, **change failure rate** (the share of releases that need a fix or a return to the previous version right away) and **time to restore** (how long recovery takes). DORA's current guide calls the last two change fail rate and failed deployment recovery time, and has added a fifth measure, deployment rework rate, which this chapter does not use. [[measuring-engineering]] treats the measures in depth; this chapter uses the two about stability.

## Pattern: Checks in the Delivery Path

If the team owns quality, its checks need a place, and that place is the delivery path. The **delivery path** is the sequence of steps every change passes on its way from its author to production. A check placed in the path runs on every change, without anyone asking for it and without waiting for a person in another team. The author's automated tests run first. A second member of the team reviews the change. Automated **readiness checks** confirm that the change can be released and taken back; the team runs them on its own change, and they can be owned by a platform team so that no author can weaken them. The release then reaches users gradually while monitoring watches it, and the path records each step in a **release log**. The **user** of this pattern is the team making a change. Its **outcome measures** are the change failure rate and the time a finished change waits before release. Figure 1 shows the path, including the steps after release, which the next section covers.

---begin mermaid---
flowchart LR
    A["Change by its author"] --> B["Author's automated tests"]
    B --> C["Review by a second team member"]
    C --> D["Automated readiness checks"]
    D --> E["Gradual release"]
    E --> F["Monitoring and alerts"]
    F --> G["Owning team on call"]
    G --> H["Incident review"]
    H -->|"adds or changes a check"| B
---end mermaid---

**Figure 1:** *Every check in the delivery path is run by the owning team or by the path itself, and what an incident teaches returns to the path as a check.*

Checks in the path do not make specialists unnecessary; they change what specialists do. A quality engineer in an enabling team works with one team at a time, at Corvane for about six weeks. Together they decide which check should catch which risk, a model my record [[quality-engineering-enablement]] calls release confidence: fast tests close to the code, checks at the boundaries between services, a few end-to-end checks of the most important user journeys, and a way back when a release fails. The specialist also does what automation cannot. DORA's guide says that testers "play an essential role performing exploratory testing and usability testing", which means investigating by hand what nobody thought to automate. Then the specialist leaves. The **user** is the team being helped. The **outcome measures** are whether the team maintains its checks alone a quarter later, and the escaped defects in its services.

## Pattern: The Team That Builds It Runs It

The path does not end at release. Some faults pass every check, and then the question is who is paged. The industry's phrase for the answer is "you build it, you run it": **the team that builds a service carries its on-call**. The reason is the one that counted against the gate. A fault that wakes the people who wrote it is paid for by the people who can prevent the next one, and they can also repair it fastest. Corvane's platform engineer could do neither. The pattern holds under three conditions. The engineers are trained; Larson writes: "Only your trained engineers can go on-call." The rotation is large enough to be bearable, which [[team-size-and-composition]] derives. And its load is measured and reduced, as my record [[operational-excellence]] requires. Reliability specialists, like quality specialists, serve the teams through shared monitoring and through teaching, and do not take the pager for services they did not build. The **user** is the owning team. The **outcome measures** are the time to restore and the number of pages per shift.

Once an incident is over, the team reviews it, and many reviews change nothing. An **incident review** is a meeting that examines an incident after it has been repaired. Four rules make it change the system. It is anchored to a written account that everyone reads beforehand; in *The Engineering Executive's Primer* Larson describes a weekly review of this kind and insists on discussion of the document over a presentation of it. It asks two questions about the system and none about a person: what let the change through, and what slowed the repair. It ends in actions that are each a change to a check, an alert, a runbook (the written steps for operating a service) or the path, with an owner and a date. And the open actions are read out every week until they are closed, which is the rule in [[operational-excellence]]. The test of a review, which is mine, is whether the delivery path is different afterwards. A review that ends by thanking the engineer who stayed up is the start of **The Hero Culture**: the organization praises the rescue and keeps the fault. The **users** are the teams that run services. The **outcome measures** are the incidents that repeat a known cause, and the share of actions closed within a month.

## Pattern: Launch Readiness Without a Launch Gate

A change travels the path every day. A launch is rarer: a new service, or a feature large enough to behave like one, takes real traffic for the first time, and here gates most often return. **Launch readiness** is a short list of conditions that must hold before that moment. My record [[operational-excellence]], which distills Kate Matsudaira's guide for software managers, gives the list. Monitoring and dashboards work. A runbook exists that an engineer new to the service can follow. Service-level objectives, the targets for availability and speed, are set. Recovery has been tested, the behavior when a dependency fails is understood, the load has been tested and compliance requirements are met. The list works when the launching team owns it. What a machine can check becomes a readiness check in the path. The rest is a review that the team calls, to which specialists come as advisers. The **users** are the launching team and whoever will be on call. The **outcome measures** are the incidents in the first month after a launch, and the wait between "ready" and launched.

The same list, held by another team, is a launch gate, and a gate can become a queue while everyone involved works hard. Corvane's launch queue of 2024, at 180 people, was one: the platform team's five engineers checked launches by hand, the check took hours, and the wait for it took about 17 of the 19 days that a change needed from the start of work to its release ([[flow-and-the-constraint]]). The remedy was to turn the hand check into automated readiness checks that each team runs on its own change, and nobody was added to check launches. Four signs show that a launch gate has become a bottleneck:

- **The wait is longer than the check.** Work waits days for a check that takes hours.
- **Open requests grow.** The count of launches waiting rises month after month; at Corvane it reached 14.
- **Nearly everything is approved.** A gate that seldom says no finds little.
- **The gate checks what the team could check.** Its questions have answers the team could establish itself, with a script or a list.

## The Opposing View: Independence and the Auditor

In all three patterns the team that made a change runs the checks on it, and the strongest objection to this chapter starts there. The separation-of-duties view holds that a check made by the author of a change is not independent. **Separation of duties** is the rule that no one person both makes a change and approves it. On this view an organization needs independent testers and a release authority, and in regulated settings auditors ask for evidence of them. The view is right about independence. An author tests what the author thought of, and the fault is usually in what the author did not think of; the engineer who alone tested Corvane's parts change is the example. DORA's guide to change approval treats the requirement as real as well. It calls segregation of duties a common regulatory requirement, under which a change must be approved by someone other than its author.

What the view gets wrong is where independence has to come from. **Independence is a property of a check, not of a department.** The requirement has three parts, and the path can supply each, as the table below shows. Research supports the substitution. DORA's 2019 State of DevOps Report, as DORA's guide presents it, found no evidence that a more formal, external review process is linked to lower change failure rates, found that heavyweight external approval goes with slower delivery, and offers review by a peer as the way to meet segregation of duties.

| What the requirement asks | What supplies it in the path |
| --- | --- |
| Someone other than the author approved the change | A recorded review by a second member of the owning team; the path refuses a change without one |
| The author cannot skip or weaken the checks | Automated checks owned outside the team (at Corvane, by the platform team) and changed only with notice |
| Evidence exists afterwards | A release log: who wrote the change, who reviewed it, which checks ran and when it was released |

I offer this as a recommendation, and it has conditions. Where a regulator or a contract names an independent function or person, that function stays; DORA's guide does not claim that peer review satisfies every regulatory framework, and neither do I. Where a team is too small for a real second reviewer, or its reviews have become a formality, the first row of the table is not met. And a change of unusual risk deserves a second look from outside the team. In each of these cases keep the outside check **explicit, narrow and early**: say which changes it covers, limit it to those, place it before the work is finished, and measure how long work waits for it. My record [[quality-engineering-enablement]] has the same rule for compliance gates. An outside check that passes this test is an exception with a reason. One that covers every change is the gate again.

## Worked Example: Corvane Answers the Proposal

The placement of ownership, the three patterns and the answer to the auditor can now be applied to the proposal of May 2026. Before answering it, Dario Vance asked for four numbers, set side by side for two groups of teams. The eleven older teams had released since 2024 on the release path, a delivery path with automated readiness checks that each team runs itself, and each carried its own on-call rotation. The nineteen newer teams, formed in 2025 and 2026, released in three other ways, and twelve of them had no rotation. The figures are for the first half of 2026, at about 500 people.

| Measure | Eleven older teams | Nineteen newer teams |
| --- | --- | --- |
| Change failure rate | 6% | 21% |
| Customer-reported defects per month | 9 | 38 |
| Median time to restore | 40 minutes | 5 hours |
| Teams the two quality engineers had worked with | 11 of 11 | 2 of 19 |

The table answers the proposal. The teams with the fewest failures had no gate at all: nobody signs off a release of the eleven older teams, and their changes fail least and are repaired fastest. A missing gate cannot explain the difference between the columns, since neither group has one. What the older teams have and the newer ones lack is checks in the path, a pager of their own and their six weeks with a quality engineer. The proposal would also have rebuilt a known queue. That launch queue of 2024, the same five platform engineers checking for eleven teams, produced a wait of 17 days, and ten testers signing off every release of thirty teams is the same design at a worse ratio.

Vance declined the QA team. With Lena Brandt, the Director of Platform, he made four changes, which put the checks, the pager, the review and the specialists where this chapter's patterns put them:

1. **One path.** The release path of 2024 becomes the one standard for all thirty teams. Its readiness checks now include a tested way back, and it requires a recorded review by a second engineer of the owning team. The platform team owns the move, which applies the rule of Corvane's engineering strategy of the same year, one standard for each shared area ([[engineering-strategy]]). The seven teams with the highest change failure rates move first.
2. **The pager with the builder.** Every team carries the on-call for its own services. A team of fewer than eight shares a rotation with one neighboring team, after each has learned the other's services.
3. **A weekly incident review.** Two engineers run it in rotation. Its actions are changes to a check, an alert, a runbook or the path.
4. **Four quality engineers.** The enabling team grows from two to four, in two pairs, and still spends about six weeks with each team.

Two quarters later, at the end of 2026, the measures had moved where the teams had changed. Seven of the nineteen newer teams were on the release path. These seven had been the worst of the nineteen, with a change failure rate of 27 percent between them, and it had fallen to 9. Customer-reported defects across all thirty teams were down from 47 a month to 31. The newer teams' median time to restore had gone from 5 hours to 90 minutes, and every team had a named rotation. The auditor's question arrived as well: a telecom customer's security questionnaire asked for evidence that every production change is approved by someone other than its author. Corvane answered with the recorded review, the readiness checks owned by the platform team and the release log, for the eighteen teams then on the release path, and with the 2027 plan for the rest, and the customer's auditor accepted the answer. The cost was visible too. Each team that moved shipped little for about six weeks, and engineers in the newer teams were on call for the first time. And the work was not finished: twelve teams still released in the three other ways, with no readiness checks in their path.

## What AI Changes Here

The one path Corvane settled on in 2026 was built for change that people write, and coding agents multiply the change. Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. **Proven.** DORA's 2024 report, as DORA summarizes it on its site, found that AI adoption increases individual productivity and job satisfaction and "negatively impacts software delivery stability and throughput", and it concludes that small batch sizes and robust testing remain crucial. **Emerging.** As of November 2026, in the organizations I have observed, review by people is the first step of the path to fall behind when agents write more of the change. This is my observation, not a measurement. The book's illustration is Corvane's fifth stage, in 2027 and 2028 at 1,100 people: merged changes rise 2.4 times in a year, and the median wait for a review goes from 5 hours to 31. Both claims point the same way. When more change arrives than people can read, stability rests on small changes and on the checks that run without a person.

The objection about independence returns here with a new author. **Speculative.** An agent that writes a change and the tests for it is an author checking its own work, and the weakness of self-checking applies to it as it applied to the engineer at Corvane. If that is right, the checks in the path have to come from somewhere other than the agent that made the change: tests derived from a specification the team wrote, readiness checks the agent cannot alter, and a second reader, a person or another agent, for what needs judgment. The claim would be confirmed where teams that keep the authorship of a change and of its tests apart report a lower change failure rate at the same volume of change. [[agentic-delivery]] makes the full argument for delivery organized around verification.

## What to Take Away

**Established.** What the sources agree on:

- Gatekeeping by people is a design defect to remove and not a stability feature (Larson, *An Elegant Puzzle*).
- Delivery performance is associated with capabilities that sit in teams and their paths, among them automated tests maintained by developers (DORA's guides, which continue *Accelerate*).
- A more formal, external approval process has not been found to lower change failure rates (DORA, 2019 State of DevOps Report).
- An incident review is anchored to a written account, and its follow-ups are tracked until they are closed (Larson, *The Engineering Executive's Primer*; Matsudaira, through my record).

**Depends on context.** What changes with the situation:

- Whether a regulator or a contract names an independent function. Where one does, it stays, kept explicit, narrow and early.
- Whether a team is large enough for a real second reviewer and a bearable rotation.
- Whether a team needs a tester of its own for a time, because its product risk is high or it is still learning to test.

**The author's synthesis.** What is this book's own position:

- Quality and reliability are one loop and not two functions. A check in the path catches what the team has learned to catch, the pager brings the team what the checks missed, and the incident review turns that into the next check. A gate or an operations team held by others cuts the loop at the point where the learning would return to the people who write the next change.
- Independence is a property of a check, and three things in the path supply it: a second reviewer, checks the author cannot alter and a release log.
- The four signs of a launch gate that has become a bottleneck, and the application of independence to agents, are mine.

## Checklist

After the next incident, when someone proposes a sign-off, ask which check, which pager and which review were missing, and judge the answer by change failure rate, time to restore and escaped defects. Start by drawing the delivery path of one team.

- [ ] Draw one team's delivery path: every step from a finished change to production, with a tested way back.
- [ ] For each check on the path, write who runs it and how long work waits for it.
- [ ] Mark each check that a person in another team performs, and test it against the four signs of a bottleneck.
- [ ] For each service, name the team that is paged, and mark every service whose builders are not on call.
- [ ] For your last incident, name the check, alert or runbook that changed because of it.
- [ ] Count the incident actions that have been open for more than a month.
- [ ] For each quality or reliability specialist, say whether they approve, do the work or teach, and when the current engagement ends.
- [ ] Where an auditor requires independence, list which of the three you can show today: a second reviewer, checks the author cannot alter, a release log.

The thirteen hours of May 2026 ended in a proposal for a QA team of ten, and Corvane declined it. You can now say why. A sign-off would have added a wait for every team, and it would have supplied neither a way back nor a pager for the Parts team; the independent look it promised comes more cheaply from a second engineer in the team. With this chapter Part IV has described engineering as it should be: a strategy, a way of governing technical choices, a platform, and a daily practice of checks, pagers and reviews. Corvane's landscape is not yet like that. Twelve of its teams still release in ways that have none of this chapter's checks, and telling them to change does not move them. A landscape is moved by a migration, and the next chapter shows how to run one and how to finish it: [[migrations-and-technical-debt]].

## Sources and Evidence

**Books**

- *An Elegant Puzzle: Systems of Engineering Management*, Will Larson, 2019. Gatekeeping as an implementation bug; only trained engineers go on call.
- *The Engineering Executive's Primer*, Will Larson, 2024. The weekly incident review anchored to a written document.
- *Accelerate: The Science of Lean Software and DevOps*, Nicole Forsgren, Jez Humble and Gene Kim, 2018. The research program and its four measures. On the author's bookshelf without notes; cited only through the author's records and DORA's guides.

**Research and reports**

- DORA, [capability catalog](https://dora.dev/capabilities/), [Test automation](https://dora.dev/capabilities/test-automation/) and [software delivery performance metrics](https://dora.dev/guides/dora-metrics/), read November 2026. The capabilities associated with delivery performance; developers as primary maintainers of automated tests; the role of testers; the delivery measures. Supplements the author's sources.
- DORA, [Streamlining change approval](https://dora.dev/capabilities/streamlining-change-approval/), read November 2026, presenting findings of the 2019 State of DevOps Report. No evidence that formal external review lowers change failure rates; peer review as the way to meet segregation of duties.
- DORA, [2024 report](https://dora.dev/research/2024/dora-report/), summary page read November 2026. AI adoption and delivery stability. The full report was not read.

**Practitioner sources**

- Kate Matsudaira, "Software Managers' Guide to Operational Excellence", through the author's record [[operational-excellence]] and its checklist. The launch readiness list; incident follow-ups; on-call load.
- The author's records [[quality-engineering-enablement]] and [[org-health-and-flow-metrics]]. Quality engineering as enablement, the three team patterns, release confidence, the rule for compliance gates; the delivery measures.
- The author's records [[run-engineering-processes]] and [[measuring-engineering-organizations]]. Processes run by engineers in rotation; measuring to operate.
- "You build it, you run it" is used as a widely known industry phrase; its original source was not read, so it is not attributed here.
- The statements under "What AI Changes Here" carry their labels; the Emerging and Speculative ones are the author's observation and reasoning as of November 2026.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
