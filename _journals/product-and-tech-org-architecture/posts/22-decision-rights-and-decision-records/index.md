---
title: "Decision Rights and Decision Records"
date: 2026-11-19
author: Željko Obrenović
excerpt: "By what method are decision rights allocated, and how is a decision recorded so that it lasts? For each decision that recurs or stalls, name who decides, whose advice is required and where it is written; choose policy, consensus or conviction to make it; and keep a one-page record that others can find and overturn."
permalink: decision-rights-and-decision-records
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to give a recurring or stalled decision an owner, choose how it is made, and write a record another team can find, rely on and overturn.

> **KEY POINTS:**
>
> * **Most stalled decisions are stalled because nobody knows whose they are.** A decision right names the role that decides, the people whose advice it must take and the place where the decision is written. Allocate one only for a decision that recurs or stalls.
> * **How to decide is a separate choice.** Will Larson's three styles fit different decisions: policy for one that recurs, consensus for a rare one whose context is spread among several people, conviction for one that is contested or stuck.
> * **A decision lasts when it is recorded.** One page states the options, the reasons and the conditions for revisiting it, in a place where another team can find it, rely on it and overturn it.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Escalation Ladder** — a decision with no stated owner travels upward, and the chapter puts it back with the role that has the information.
> * **The Consensus Stall** — a decision with no named decider ends only when everyone agrees, and the chapter names the decider.

<br>

In 2024 a finished feature at Corvane waited a median of nine days before customers could use it. Corvane is the fictional company this book follows. It makes scheduling software for field-service companies and had 180 people that year. The feature was built and its code was in production. It waited for someone to say it was ready. Four people could say "not yet": the team's product manager, its engineering manager, the head of support and the account manager of the customer it was promised to. **Nobody could say yes.** You have probably watched a decision go round a table of well-informed people for weeks, or go up to someone senior who knew the least about it. Both happen when the decision belongs to nobody.

The introduction to this part claimed that alignment needs explicit mechanisms. This chapter takes the first of them: who decides, and how the decision is kept. Its method has three steps. For each kind of decision that recurs or stalls, name the role that has the information to make it, the people whose advice that role must take and the place where the decision is recorded. Then choose how the decision is made, among the three styles Will Larson describes: by policy, by consensus or by conviction, according to how often the decision recurs and how much it is contested. Then write a record that states the options, the reasons and the conditions for revisiting it, because that is what makes a decision last. The chapter starts with Corvane's waiting feature and then defines the three parts of a decision right. It says which decisions to allocate, and how much to specify, against a warning from *Six Simple Rules*. Then come the three styles, the decision record, three ways allocation fails, Corvane's readiness decision followed to its record, and what AI changes.

## Setting the Scene: A Finished Feature and Nobody to Say Yes

Here is the situation in full. Corvane had eleven product teams in 2024, and it had just shortened its releases, so that a change reached production within days; [[the-organization-as-a-product]] tells how. A feature is made of many changes, and a team kept a new feature switched off for customers until it was complete. Switching it on needed a yes. The team's product manager wanted to know that it solved the customer's problem. The engineering manager wanted to know that the team could run it. The head of support wanted her staff briefed before the first call came. And most features that year had been promised to a customer by name, so that customer's account manager had a view on the date. Each of the four was asked, in a chat thread opened for the feature, and the feature went on when all four had stopped objecting.

That took time, and the hard cases went elsewhere. In the last quarter of 2024 the teams finished fourteen features. The median wait, from the last change reaching production to the feature being available to customers, was nine days. That was longer than it now took to release a change. Five of the fourteen never got four agreements. They went to the weekly leadership meeting, where Tomas Rell, co-founder and chief technology officer, decided. Corvane had been here before. In 2019, when it had twelve people, every pricing, design and release decision waited for Tomas Rell, and the company still calls that time the Founder Queue.

Notice what was not missing. Each of the four held real information: the customer's problem, the team's ability to run the feature, the state of support, the promise made. They were willing, and they talked every day. What was missing was the answer to one question: whose decision is this? Without that answer a decision has only two ways to end. Everyone agrees, or it goes up until it reaches someone nobody can refuse. Corvane's readiness decision used both. In my experience this is the usual case. **Most stalled decisions are stalled because nobody knows whose they are**, and more information or more meetings do not move them.

## A Decision Right Has Three Parts

What it means for a decision to be someone's was defined in [[the-organization-as-a-system]]. A **decision right** is the agreed answer to three questions about a named kind of decision: who may make it, whose input they must take, and where the decision is written down. The words "a named kind" set the unit. A right covers a class of decisions that comes back, such as "is this feature ready for customers?". It does not cover a single instance, and it is narrower than a job description. A role holds the right, so the right stays in place when the person changes.

The first part is who decides, and the rule for it is that the right goes to **the role that has the information** the decision needs. Usually that is the role closest to the work. In *Six Simple Rules*, Yves Morieux and Peter Tollman count among the gains of a well-designed organization decisions "made as close as possible to where the action takes place and where information is richest". David Marquet's intent-based leadership is a practice for getting there. In *Leadership Is Language* he recalls an agreement with his submarine crew: he would state his intent, the goal to be reached, and they would stop asking permission and state what they intended to do. The crew's phrase changed from "request permission to" to "I intend to". The decision moves to the people who have the information, and the leader still hears it before it takes effect. My notes on the practice are in [[leadership-ladder]].

The second part is whose advice the decider must take. **Required advice** means that the decider has to ask the named people, and hear their answer, before deciding. It does not mean that they have to agree. The second part exists for that difference. A decider who must ask gets what the others know. A decider who must obtain agreement has handed each of them a veto. A named decider with required advice keeps the information of many and the speed of one. For technical decisions this is the advice process of [[architecture-governance]], and this chapter applies the same rule to any decision.

The third part is where the decision is written, so that someone who was not there can find it later; the record has a section of its own below. The three parts can be asked of any decision. The table asks them of Corvane's readiness decision as it stood in 2024.

| Part | The question | A good answer | Corvane's readiness decision, 2024 |
| --- | --- | --- | --- |
| Who decides | Which role has the information? | One role, named | Nobody |
| Whose advice is required | Who must be asked first? | A short list of roles, asked and not outvoted | Four people, each able to block |
| Where it is written | Where would a newcomer find it? | One known place | A chat thread per feature |

## Pattern: Allocate Only the Decisions That Recur or Stall

Before anything is allocated, one objection has to be heard, because it is aimed at the whole idea. [[the-organization-as-a-system]] raised it and left it for this chapter. Morieux and Tollman write: "Resist the pressure to clarify roles, decision rights, and processes." Their reason is that clarity past a threshold lets people comply with their own box. Their example is a relay runner who hands off the baton at exactly the specified mark and takes no interest in whether the handoff worked. They add that a request for clarity is often an attempt to avoid having to cooperate. On their account organizations work because roles overlap and people have to work things out with each other.

I accept the warning and read it as a limit on quantity. My answer to **how much to specify** has two halves. First, allocate a right only for a decision that **recurs or has stalled**. A decision that keeps being escalated, or that has gone round for weeks, is evidence that working it out between people has failed for that decision. Second, for that decision name the three parts and nothing else. A right says who decides. It says nothing about how the work is done, and everything that is not on the list stays with the people doing the work, overlap included. Two things keep even an allocated right from becoming a box. Required advice means the decider cannot ignore the people the decision touches. And the right stays open to challenge: Morieux and Tollman hold that no function should be protected by its decision rights from questioning by others. As a rule of thumb of my own, the allocated decisions of one level of the organization should fit on one page. A second page is a sign that you have passed the threshold.

Allocating one right takes five steps.

1. **Collect.** List the decisions that were escalated or reopened last quarter, or that waited more than two weeks.
2. **Name the kind.** State each as a question that will come back: "is this feature ready for customers?", not "is the skills matrix ready?".
3. **Place it.** Give it to the role that has the information. A dispute about which of two groups owns something is a decision about the boundary between them, and neither group can hold it. It belongs to their **nearest common leader**: the lowest role that both groups report up to.
4. **Name the advice.** List the roles the decider must ask first, and say how long they have to answer.
5. **Write it down, with a date to look again.** A right fits the size at which it was given.

The users of this pattern are the people who wait for decisions and the people who are asked to make them. It has worked when three things are true of the kind of decision you allocated. A decision of that kind waits fewer days. Fewer of them go up a level. And three people involved, asked separately, name the same decider.

## Choosing How to Decide: Larson's Policy, Consensus and Conviction

A right says who decides. It does not say how, and a decider who makes every decision the same way will make most of them the wrong way. Will Larson, in *The Engineering Executive's Primer*, describes "three primary styles: leading with policy, leading from consensus, and leading with conviction". He presents them as styles of leadership. I use them here as three ways of making a decision, which is how he applies them himself: each fits a kind of decision. My working notes on all three are in [[leadership-styles]].

**Policy** fits a decision that recurs. Larson's definition: "Leading with policy is creating a documented, predictable means for making a decision." The decider settles the kind of decision once, in writing, and after that many people can apply the rule consistently without asking. Peter Drucker makes the same point in *The Effective Executive*. The first question about any problem, he says, is whether it is generic or an exception, and his answer is firm: "All events but the truly unique require a generic solution." He calls it the most common mistake to treat a generic situation as a series of unique events. A leader who answers the same question for the fifth time is making that mistake.

**Consensus** fits a rare decision whose context is spread among several people. Larson: "Leading from consensus is pulling together the relevant set of stakeholders to identify a shared approach for a given problem." He starts it with a framing document, a page that states the perspectives already known and invites the others to add theirs. He attaches two conditions: all stakeholders feel heard, and a tight timeline is set and held. And he has the most senior engaged person settle how the group will work, the deadline above all. I call that person the closer. The conditions matter because consensus is the wrong default, and here I argue against the view that the people affected should simply decide together. Consensus works while the group is small and everyone in it pays for delay. In a larger group it hands a veto to whoever cares least about what the delay costs. Corvane's four people with a "not yet" were such a group.

**Conviction** fits a decision that is contested or has stalled. Larson: "Leading with conviction is pulling all the relevant context into your head, thinking through the trade-offs, and personally making a definitive decision." He finds it most useful where the people involved hold incompatible views, or where the consequences are large and lasting. Between two groups that cannot agree, the person who decides is their nearest common leader. Conviction is the style closest to overriding people, so it carries a guard and a duty. The guard is Larson's pair of questions: are you carefully considering the feedback of those closest to the work, and are you adding friction to a team that would have reached a similar decision without you? The duty is to decide in the open: take the advice in writing, say that you are deciding and why, and record it. Required advice therefore belongs to every style. In 2026, at about 500 people, Corvane's Director of Platform chose a message broker after written advice from the teams affected, as [[architecture-governance]] tells. In Larson's terms, as I read them, that was a decision by conviction made by the holder of the right.

Two questions choose among the three styles. Will this kind of decision come back? And can the people who hold the context agree by a set date? The figure puts the two in order.

---begin mermaid---
flowchart TD
    D["A decision that recurs or has stalled"] --> Q1{"Will this kind of decision come back?"}
    Q1 -->|"yes"| P["Policy: write the rule once and name who applies it"]
    Q1 -->|"no"| Q2{"Can the people who hold the context agree by a set date?"}
    Q2 -->|"yes"| C["Consensus: a framing document, a closer, a deadline"]
    Q2 -->|"no, or the date has passed"| V["Conviction: the holder of the right, or the nearest common leader, decides after written advice"]
    P --> R["A one-page decision record"]
    C --> R
    V --> R
---end mermaid---

**Figure 1:** *The style follows the decision: recurrence points to policy, and contest decides between consensus and conviction.*

Side by side, the three styles differ in when they fit, in who decides and in what gets written. The last column, how each is misused, follows my notes on Larson's chapter.

| Style | Fits when | Who decides | What is written | How it is misused |
| --- | --- | --- | --- | --- |
| Policy | The decision recurs | Whoever the rule names, each time | The rule and its review date | A rule for a decision that happens once |
| Consensus | The decision is rare, the context is spread and the group can agree by a date | The group, with a closer who holds the deadline | A framing document, then the decision | No closer and no deadline |
| Conviction | The decision is contested or stalled, or large and lasting | The holder of the right, or the nearest common leader | The advice, the reasoning and the decision | Used on recurring decisions, or without advice |

The users of this pattern are the decider and the people who have to live with the decision. It has worked when the decider meets fewer repeats, meaning decisions of a kind that was already settled once. It has worked when decisions by conviction are few and each has a written reason, and when a decision, once made, is not reopened. That is the sense in which conviction should be used **sparingly and openly**.

## Pattern: A Decision Record Another Team Can Find, Rely On and Overturn

A decision made in any of the three styles has to outlive the meeting, and two documents do that work. An **RFC**, short for request for comments, is the proposal sent round before the decision: the problem, the options and a recommendation, addressed to the people whose advice is required. Larson's framing document does the same job for the consensus style. A **decision record** is the short page that remains afterwards. [[architecture-governance]] introduced it for technical decisions, where it is called an architecture decision record. Nothing about the format is technical. A decision log can hold a record on working from home next to one on a database, as [[work-from-home]] shows, and my conventions for such a log are in [[markdown-records]].

A record that lasts has eight short fields, and five of them answer the elements that Drucker finds in an effective decision in *The Effective Executive*. Two of his elements are easy to skip. He asks the decider to work out what is right before thinking about what will be accepted, because someone who starts from the acceptable cannot tell a good compromise from a bad one. And he holds that no decision has been made until carrying it out is someone's assignment. One of his terms needs a note. He calls the specifications a decision has to satisfy its "boundary conditions". They are requirements, and they have nothing to do with the boundaries between teams in this book, so the field has a plainer name.

| Field | What it holds | Where it comes from |
| --- | --- | --- |
| Decision and status | One sentence that starts "We will"; proposed, accepted or superseded | The decision record of [[architecture-governance]] |
| Kind of problem | Recurring or one-off, which sets the style | Drucker: generic or exception |
| Must satisfy | The few things any answer has to achieve | Drucker: "boundary conditions" |
| Options and reasons | Each option considered, and why the chosen one is right | Drucker: what is right before what is acceptable |
| Advice received | Who was asked, what they said, and when | The advice process |
| Action | Who does what, by when | Drucker: action built into the decision |
| Revisit when | The date or the evidence that reopens it, and who may reopen it | Drucker: feedback |
| Decider and date | The role, the person, the day | The decision right |

These fields make three things possible for someone who was not in the room. That person can **find** the record, if all records sit in one searchable place and each title states its decision as a sentence. They can **rely on** it, because the status, the date and the decider say whether it still stands, and the "must satisfy" field says what it covers. And they can **overturn** it. The revisit field says what evidence reopens the decision and who may reopen it, and the rule from [[architecture-governance]] applies: an accepted record is never edited, a new record supersedes it, and the old one stays. A decision that cannot be overturned by a stated route gets overturned quietly, by being ignored.

The users of the record are the people who were not there: the next decider, a new colleague, a team the decision touches. Three measures tell whether it works for them. How long does it take to find the record of a decision made a year ago? How many settled decisions were argued again without new evidence? And are old records superseded by new ones, or do they go stale?

## Anti-Patterns: The Ladder, the Stall and the Chart of Everything

The method fails in three ways, and the first two are in this book's catalogue of failure patterns. **The Escalation Ladder** is a right that sits above its information: routine decisions are made two levels above the work. It usually begins as the correct arrangement. A founder who decides everything at twelve people is doing what the company needs, and the Founder Queue became a failure only as Corvane grew. A second Corvane case shows the same thing happening to a right that was allocated on purpose. In 2022, when Corvane had about 45 engineers, Priya Nambiar, then the product manager who worked with every team, was given the right to decide scheduling rules. By 2025 she was chief product officer of a company near 500 people, and every rule question still waited for her. She handed the right to the Scheduling team in 2026, a story told in [[discovery-delivery-and-empowered-teams]]. This is why step five gives a right a date to look again.

**The Consensus Stall** is the opposite failure: the right sits with no one. Meetings end by scheduling another meeting, and whoever was absent reopens what was settled. It has two forms. In the first, nobody was ever named, as with Corvane's readiness decision. In the second, a leader chose consensus and left out Larson's conditions, so there is no closer and no deadline. The remedy for the first form is to name the decider. The remedy for the second is a date, and conviction when the date passes.

The third failure comes from applying this chapter too hard. I call it the chart of everything: a matrix with every decision in the company down the side, every role across the top and a letter in each cell. Named frameworks for assigning roles in a decision, such as RAPID, from Bain, and DACI, are widely known. They are not among this book's sources, and I do not describe them. My objection is to one use of any such scheme. Whichever letters fill the cells, a chart of every decision is the clarity past the threshold that Morieux and Tollman warn of, and people start to consult the chart instead of each other.

## Worked Example: Who Says a Feature Is Ready

Corvane's readiness decision can now be followed to its end. At the end of 2024 the question was put on Corvane's list of changes to make to its own organization, and it moved slowly. In the first half of 2025, as the company grew from 180 people toward 500, a working group of two product managers and two engineering managers met four times. It had no deadline and no closer, and it produced two proposals. By then Corvane had a chief product officer, Priya Nambiar, and the two executives each backed one proposal. She held that the product manager should decide readiness. Tomas Rell, with Dario Vance, the VP Engineering, held that the engineering manager should. The two had a rule for such a case. [[executive-roles-and-reporting-lines]] describes the page on which they wrote who decides what between them, and its last line sends a disagreement to the chief executive from both of them, within five working days, on one page. Readiness was not on that page. So they took it together to Ines Okafor, co-founder and chief executive, who was also their nearest common leader.

Ines Okafor decided by conviction, and in the open. She asked for advice in writing from six people close to the decision: two product managers, two engineering managers, the head of support and the head of sales. She wrote down her reasoning, announced a tentative decision and gave one week for objections. Then she made it final, nine working days after the page reached her. The sequence follows the steps for conviction in [[leadership-styles]], my working version of Larson's chapter. The record of her decision fits on one page.

| Field | Content |
| --- | --- |
| Decision and status | We will treat readiness as two decisions. *Ready to run* is decided by the team's engineering manager. *Available to customers* is decided by the team's product manager, once the feature is ready to run, after advice from the engineering manager, the head of support and, for a feature promised to a customer, that customer's account manager. Advice is due within two working days, and silence does not block. A feature that changes what the product promises a customer goes to the chief product officer. Status: accepted. |
| Kind of problem | Whose decision readiness is: one-off. Readiness itself: recurs with every feature, so the answer is a rule. |
| Must satisfy | No finished feature waits more than three working days for a decision. Support never learns of a feature from a customer. The engineering manager is not overruled on whether the team can run a feature. |
| Options and reasons | (a) The product manager decides both: rejected, because the team has to run the feature. (b) The engineering manager decides both: rejected, because the product manager knows the customer's problem and answers for the outcome. (c) A weekly release committee of all four: rejected, because it keeps four vetoes. (d) Two decisions, each with the role that has its information: chosen. |
| Advice received | Six written answers within a week. The head of support asked for a veto: not granted, and she is asked first on every feature. The head of sales asked that promised dates decide: not granted, and the account manager is asked. |
| Action | Priya Nambiar and Dario Vance tell every product manager and engineering manager within a week. Each team's release notes get one line per feature: who decided, when, and whose advice was heard. In force from the first day of the next month. |
| Revisit when | Priya Nambiar and Dario Vance review after two quarters, or sooner if the median wait is above five days. Either may reopen the decision. |
| Decider and date | Ines Okafor, chief executive; second half of 2025. |

Read the record against the chapter. It holds two decisions, made in two styles. The first is the one-off question of whose decision readiness is. It was contested, a consensus had failed for lack of a closer, and it lay on the boundary between two executives' organizations, so their nearest common leader settled it by conviction. Ines Okafor did not decide whether any feature was ready. The second decision is readiness itself, which comes back with every feature. The record turns it into a policy: a written rule that puts each half with the role that has its information, and that every team applies without asking anyone. All three parts of a decision right are in the record: who decides, whose advice is required, and where the decision is written, down to the line in the release notes.

Two quarters later Priya Nambiar and Dario Vance held the review that the record asks for. A finished feature now waited a median of two days, where it had waited nine. One feature had reached the leadership meeting, under the clause about what the product promises a customer. The arrangement also had a cost, and the review recorded it. One product manager had made a feature available against the advice of the head of support. It drew a week of support calls and was withdrawn until the support staff were briefed. Advice that can be overruled will sometimes have been right. The two reviewers kept the right where it was and added one line to the record: advice that is not followed is written down with the reason.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The method above was described for people, and coding agents now do part of the work that those people decide about. **Emerging.** As of November 2026, in the teams I have observed, agents are given the team's decision records as context, and an agent holds no decision right: a person or a team owns every decision that an agent's work depends on. A written record is then the only way a decision reaches work that no person briefed. A decision that lives in someone's memory does not reach an agent at all. This is my observation, and I know of no published measurement.

**Speculative.** If agents raise the volume of changes, more decisions of each kind arrive at the same deciders each week, and a decider who settles them one at a time becomes the queue. The share of decisions that have to be made by policy would then rise, and with it the value of records that an agent can read. The claim would be confirmed where teams report that the wait for a decision grows as the volume of changes grows. [[where-the-constraint-moves]] weighs the published evidence.

## What to Take Away

**Established.** What the sources agree on:

- A decision that recurs needs a rule, and treating it as a series of unique events is the common mistake (Drucker, *The Effective Executive*; Larson's leading with policy, *The Engineering Executive's Primer*).
- Decisions belong close to the action, where information is richest (Morieux and Tollman, *Six Simple Rules*; Marquet's intent-based leadership).
- A decision is not made until carrying it out is someone's assignment, and it needs feedback built in (Drucker).
- Clarity about roles and decision rights helps up to a threshold and harms cooperation beyond it (Morieux and Tollman).

**Depends on context.** What changes with the situation:

- Which style fits depends on how often the decision recurs and how much it is contested. A consensus that works among five people stalls among fifty.
- Who should hold a right depends on size. A right that fitted Corvane at 45 engineers was an Escalation Ladder at 500 people.
- How much to write depends on who was absent. Six people in one room need fewer records than thirty teams.

**The author's synthesis.** What is this book's own position:

- Allocating rights only for decisions that recur or stall, on one page per level, is my answer to Morieux and Tollman's warning.
- Reading Larson's leadership styles as ways of making a decision, chosen by recurrence and contest, and the rule of the nearest common leader are my arrangement.
- The eight-field record, with Drucker's elements as five of its fields, is my format.

## Checklist

Allocation, style and record are one method at three moments. Before the decision you settle whose it is and whose advice it needs. During it you choose policy, consensus or conviction. After it you leave a page from which the next decision can start. A decision that is slow, or that keeps reopening, skipped one of the three. Run these eight checks on your own organization.

- [ ] List the decisions that were escalated, reopened or left waiting for more than two weeks last quarter.
- [ ] For each, ask three people separately who decides it, and compare the answers.
- [ ] Restate each as a kind of decision that will come back, and mark the ones that recur.
- [ ] Place each with the role that has the information; for a dispute between two groups, name their nearest common leader.
- [ ] Name whose advice is required, and say that advice is not consent.
- [ ] Choose the style: a written rule for what recurs, a closer and a deadline for a consensus, conviction for what is stuck.
- [ ] Write one page with the eight fields, and put it where the other records are.
- [ ] Check that your allocated decisions fit on one page, and remove a right that nobody has needed.

Corvane's finished feature waited nine days because four people could say "not yet" and the decision was nobody's. The nearest common leader supplied the missing owner, by conviction, and a rule and a one-page record made the answer last. A leader who allocates rights only for decisions that recur or stall, records them briefly and uses conviction sparingly and openly gets decisions that are made sooner and stay made. This chapter treated decision rights in general. One activity is the largest recurring set of decisions an organization has, and at Corvane in 2026 it took nine weeks of every quarter: planning. The next chapter shows how planning's decision rights are divided: [[planning]].

## Sources and Evidence

**Books**

- *The Engineering Executive's Primer*, Will Larson, 2024. The three leadership styles (leading with policy, from consensus, with conviction) and when each fits; the framing document and the deadline for consensus; the two questions against micromanagement.
- *The Effective Executive*, Peter F. Drucker, first published 1967. The elements of the decision process: generic or exceptional problems, boundary conditions, what is right before what is acceptable, action built into the decision, feedback.
- *Six Simple Rules: How to Manage Complexity without Getting Complicated*, Yves Morieux and Peter Tollman, 2014. The warning against clarifying roles, decision rights and processes; decisions made close to the action; functions that stay open to questioning.
- *Leadership Is Language*, L. David Marquet, 2020, and *Turn the Ship Around!*, 2012. Intent-based leadership and the change from "request permission to" to "I intend to".

**Practitioner sources**

- The author's working records: [[leadership-styles]], [[markdown-records]], [[architecture-advisory-forum]] and [[leadership-ladder]]; [[work-from-home]] as an example of a recorded decision that is not technical; the author's checklists "Decision-Making Process" and "Effective Decisions", made from *The Effective Executive*.
- RAPID and DACI are named as widely known frameworks only. They are not among the author's sources and nothing in this chapter rests on them.
- The use of Larson's styles as ways of making a decision, the nearest common leader, the one-page limit and the eight-field record are the author's. The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
