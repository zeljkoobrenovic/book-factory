---
title: "Architecture Governance: Advice, Guardrails and Mandates"
date: 2026-11-19
author: Željko Obrenović
excerpt: "Who decides technical direction, and with how much force? By default the team does, after seeking advice and in a record others can find; the organization nudges or taxes where a choice costs other teams, and mandates only where a team cannot carry the risk."
permalink: architecture-governance
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to choose, for any technical decision, among advice, a nudge, a tax and a mandate, and to judge governance by how long a decision waits.

> **KEY POINTS:**
>
> * **The team decides by default, after advice, and writes it down.** Anyone affected and anyone with expertise is asked first. The decision goes into a record that others can find and that a later decision can overturn.
> * **Stronger instruments follow the cost of divergence.** That cost is what one team's different choice costs other teams and the company. Where a team's choice costs other teams, the organization makes the common choice the easy one (a nudge) or makes the team pay what its choice costs others (a tax). The decision stays with the team.
> * **A mandate is the most expensive instrument and should be the rarest.** It is kept for risk a team cannot carry, such as legal exposure or security, on a short written list with reasons.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Review Bottleneck** — a central board that approves designs is this pattern in its plainest form, and the chapter replaces approval with advice and a record.
> * **The Consensus Stall** — advice mistaken for agreement is the failure that follows when a board is removed carelessly.

<br>

In the first half of 2026 the architecture forum of Corvane, the fictional company this book follows, approved 33 of the 36 designs put to it. A design waited a median of 23 days to be heard. Corvane had about 500 people then, in about thirty teams, and those teams ran four ways of deploying, three message brokers and two identity libraries. A message broker is the service through which a company's systems send each other events, such as "this appointment moved". The forum was slow, and the landscape it was set up to keep consistent had **diverged anyway**. Then three teams asked for a fourth broker. If you have waited for an architecture review, or sat on one, you know both halves of that.

The previous chapter ended with an engineering strategy made of policies that settle recurring decisions. It left open how those policies reach thirty teams, and that is the subject here: who decides technical direction, and with how much force. My answer is that a technical decision should be made **as close to the work as the cost of divergence allows**, where the cost of divergence is what one team's different choice costs other teams and the company. By default the team decides, after seeking advice, and records the decision. Where consistency pays, the organization nudges or taxes. It mandates only where a team cannot carry the risk of choosing differently. The chapter starts with Corvane's forum and why a central board is the wrong default. It then sets out the default of advice and a record, the three stronger instruments, and how to choose among them. After that come the people who carry governance, three ways it fails, the broker decision at Corvane, and what AI changes.

## Setting the Scene: A Forum That Approves and a Landscape Nobody Chose

Here is the situation in full. Dario Vance, Corvane's VP Engineering, set up the architecture forum in 2025, while the company grew from eleven product teams toward thirty. It was a meeting of senior engineers, chaired by Samir Haddad, a staff engineer who had been at Corvane since 2019, and attended by whoever else could come. Any design that added a technology, or changed an interface between teams, needed the forum's approval before work started. It met every second week.

A year of that rule produced a queue. In the first half of 2026 teams submitted 36 designs. The forum approved 33, and 27 of those without any change. The median wait from submitting a design to its hearing was 23 days. Meanwhile the landscape kept spreading: four ways of deploying, three message brokers and two identity libraries. Since 2025 the forum had granted most of eleven requests for a new way of deploying, messaging or checking identity. Each was reasonable when judged alone. The forum judged one design at a time, and nothing in its rule asked what a choice would cost the other teams.

Then came the request this chapter follows. Three teams, Dispatch, Notifications and Technician App, wanted a new message broker, because they needed to replay past schedule-change events and none of the three brokers in use could do that. Two other teams, Billing Integrations and Stock Integrations, receive those events and still used the oldest of the three. The forum discussed the request in three sessions over six weeks, with different engineers in the room each time, and did not decide. Those present knew less about the need than the three teams did, and nobody at the table spoke for the two teams on the oldest broker.

## Why a Central Board Is the Wrong Default

A forum like Corvane's exists for a good reason, and the reason deserves its strongest statement. Some choices should be made once for the whole company. In *Enterprise Architecture as Strategy*, Jeanne Ross, Peter Weill and David Robertson argue that deciding what to standardize is a business decision: standardization brings efficiency and predictability and, in their words about business processes, "necessarily limit[s] local innovation". Among the mechanisms they list for keeping projects to the standards are an architecture compliance process, a formal exception process and a centralized standards team. That is the **architecture-board model**: a central group approves designs before work starts.

The need is real, and the mechanism is where the model goes wrong. A board that must approve is a queue, and the queue grows with the company. Every new team adds designs to check, and the board stays the same handful of senior people. Corvane's 23 days came from this arithmetic. The engineers on the forum were not slow. This book calls the result **The Review Bottleneck**: a hand-over between teams built as an approval queue, where finished work waits longer for approval than it took to make. The capacity it uses up is verification, the knowledge that a design is sound, which [[flow-and-the-constraint]] names as one of three capacities an organization runs out of.

The second fault is information. The board sees each design for an hour, and the team has lived with the problem for months. Gregor Hohpe describes the result in *The Software Architect Elevator*: "The worst-case scenario materializes when people holding relevant information or expertise aren't empowered to make decisions, whereas the decision makers lack relevant information." Both faults point the same way: move the decision to where the information is, and keep centrally only what has a high **cost of divergence**, the term from the lead for what one team's different choice costs other teams and the company. That cost includes engineers who must relearn when they change teams, fixes that have to be made several times, systems someone has to operate, and risk. The principle of this chapter is to decide as close to the work as that cost allows.

## Pattern: The Advice Process and the Decision Record

The practice that leaves a decision with the team and still brings wider knowledge to it is the **advice process**. I take it from Andrew Harmel-Law's article "Scaling the Practice of Architecture, Conversationally", which supplements the books this chapter rests on. He states it as one rule and one qualifier. The rule: "anyone can make an architectural decision." The qualifier: before deciding, the decider must consult everyone who will be meaningfully affected and people with expertise in the area. The decider must seek the advice, listen to it and record it, and is not obliged to follow it.

The advice and the decision are written in a **decision record**, often called an ADR, for architecture decision record. The format most teams use comes from a 2011 post by Michael Nygard, who asks for one or two pages kept in the project's repository. The table gives his five parts and two more, one from Harmel-Law and one of my own.

| Part | What it holds | From |
| --- | --- | --- |
| Title | The decision in a few words | Nygard |
| Status | Proposed, accepted, or superseded with a link to its replacement | Nygard |
| Context | The forces at play, stated as facts | Nygard |
| Decision | "We will …", in full sentences | Nygard |
| Consequences | What becomes easier and what becomes harder, including what the team now pays for | Nygard |
| Advice received | Who was asked, what they said, and when | Harmel-Law |
| Revisit when | The evidence that would reopen the decision | My addition |

Two properties turn such a page into an instrument of governance: others can **find** it, and a later decision can **overturn** it. Finding needs one searchable place for the records of all teams, each with its status. Overturning needs a rule that nobody edits an accepted record. A new record supersedes it, and the old one stays. Nygard is explicit: "If a decision is reversed, we will keep the old one around, but mark it as superseded." A record that only its authors can find is a private decision. My working conventions are in [[markdown-records]], and [[decision-rights-and-decision-records]] treats records beyond architecture.

A record is written by one team, and the advice in it has to come from somewhere. I recommend a standing advisory forum: weekly, open, and with no power to approve. It serves the users of this pattern, who are the team that decides and the teams its decision affects. Harmel-Law describes one in which decisions are "still owned and made by the originators", and my own version is in [[architecture-advisory-forum]].

The pattern is judged by **how long a decision waits**: the days from a team's question to its recorded decision. A second measure keeps the first honest: the share of records that list advice from outside the team.

## Three Instruments Above Advice: Nudge, Tax and Mandate

Advice has a limit. A well-advised team can still make a choice that is good for it and costly for others, and advice gives nobody the means to object with more than words. For that case my book *Grounded Architecture* describes governance as "a portfolio of influences rather than a single enforcement style", with three influences: **nudges**, **taxes** and **mandates**. I define them here from the least force to the most.

A **nudge** makes the preferred choice the easy one and forbids nothing. The term is Richard Thaler and Cass Sunstein's, from *Nudge*: any aspect of how a choice is presented that "alters people's behavior in a predictable way without forbidding any options or significantly changing their economic incentives." Their best-known example is the default, the option a person gets by doing nothing, which they call a powerful nudge. In engineering the default takes the form of a **paved path** (the name *Grounded Architecture* uses is golden path): a ready-made, supported way of doing a common task, such as creating a service that already has deployment, logging and monitoring. A team may leave the path, and staying on it is less work.

A **tax** also leaves the choice with the team, and it changes what the choice costs the chooser. The team that diverges pays the cost its choice puts on others. The example in *Grounded Architecture* is money: each department is charged for the cloud resources it uses. My extension, which *Grounded Architecture* does not make, is a tax paid in operating work. A team that adopts a technology nobody else runs operates it, upgrades it, is on call for it, and pays for the migration back if the experiment ends.

A **mandate** states what teams must or must not do. *Grounded Architecture* calls mandates and bans "the most direct forms of governance" and reserves them for compliance, for a few organizational priorities such as security, and for strategic constraints. A mandate's best form is a **guardrail**: a limit that is checked automatically, in the delivery path, so that no meeting is needed to enforce it ([[governance-as-code]]).

With all three defined, the table sets the four instruments side by side, advice included. They differ in who decides, in how each acts, and in what each costs the organization.

| Instrument | Who decides | How it acts | Example | What it costs the organization |
| --- | --- | --- | --- | --- |
| Advice | The team | Brings affected people and experts to the decision | A record with advice from two other teams | Advisers' time |
| Nudge | The team | Makes the common choice the least work | A paved path for new services | Building and keeping up the path |
| Tax | The team | Makes the team pay what its choice costs others | The team operates what it alone adopted | Keeping the account of costs fair and visible |
| Mandate | The organization | Removes the choice | Customer data stays in approved regions | Enforcement, exceptions, and the team's lost information |

The last row costs the most, for three reasons that are my own argument. A mandate has to be enforced, and every mandate breeds requests for exceptions that someone must hear, which rebuilds the queue. It overrides what the team knows about its own case. And it hides evidence: when everyone must use a thing, nobody can tell from its use whether the thing is good. *Grounded Architecture* concludes that mandates are used sparingly and as a last resort. I add one discipline: keep the mandates on **one short written list**, each with its reason and its owner.

## Choosing the Instrument by the Cost of Divergence

Four instruments need a way to pick one, and three questions, asked in order, do it. First, would a different choice create risk that the team cannot carry, such as a breach of the law or of security? Second, does the cost of a different choice fall on others, or stay inside the team? Third, where it falls on others, is there a paved path, or is one worth building? The figure below shows where each answer leads, and two of its boxes need a note. Where the cost stays inside the team, the default still holds: the advice process asks a team to consult the people its decision affects, and here there are none. The team writes a record only if it will itself want to find the reason later. And the last question picks the instrument to start with. Where a paved path exists, start with the nudge; where none exists, the tax is the weakest instrument available.

---begin mermaid---
flowchart TD
    D["A technical decision"] --> Q1{"Would diverging create risk the team cannot carry?"}
    Q1 -->|"yes: law, security"| M["Mandate, as a guardrail where it can be checked"]
    Q1 -->|"no"| Q2{"Does the cost of diverging fall on others?"}
    Q2 -->|"no"| A["The team decides: nobody else is affected; a record if the team wants one"]
    Q2 -->|"yes"| R["Advice process and a decision record"]
    R --> Q3{"Is there a paved path, or is one worth building?"}
    Q3 -->|"yes"| N["Start with a nudge: make the paved path the default"]
    Q3 -->|"no"| T["Start with a tax: the team pays what its choice costs others"]
---end mermaid---

**Figure 1:** *The instrument follows the cost of divergence: the further the cost of a choice travels from the team that makes it, the more force the organization uses.*

Four decisions, put through the three questions, show the range.

| Decision | Where the cost of divergence falls | Instrument | Why |
| --- | --- | --- | --- |
| Which library a team uses to handle dates | Inside the team | None, or advice if the team asks; no record needed | Cheap to diverge and cheap to change later |
| Whether a service may write personal data to its logs | On the company, as legal exposure | Mandate, checked as a guardrail | A risk no team can carry |
| Adopting a new database engine | On whoever operates, secures and later migrates it | Advice process with a record, and a tax: the team operates it | The choice is the team's if the team bears its cost |
| Whether a new service uses the standard deployment path | On every engineer who changes teams and every fix that must reach all paths | Nudge: the paved path is the default | Consistency pays, and no one case is dangerous |

An instrument, once chosen, is not fixed. My rule is to start with the weakest one that could work and to **raise it only on evidence**. When teams leave a paved path, the first question is what is wrong with the path. Thaler and Sunstein note that people who know they dislike a default will change it, so low adoption is first of all information about the path. If teams still leave a good path and the others pay for it, the next step up is a tax. A mandate comes only when incidents or measured cost show that divergence is doing harm.

The right mix also changes with size. The table uses the five sizes of Corvane that this book follows. It shows what I would expect to be in use at each size, which is not what Corvane did: at 500 people Corvane had an approving forum. The placement is my synthesis.

| Corvane's size | What changes | Instruments in use |
| --- | --- | --- |
| 12 people, one team | Everyone hears every decision | Conversation |
| 50 people, four teams | A choice in one team is unknown in the next | The advice process and decision records |
| 180 people, twelve teams | The same mechanics are built many times | The first paved path |
| 500 people, about thirty teams | Choices cross groups; regulation and large customers arrive | Taxes, a short mandate list with its first guardrails, an advisory forum |
| 1,100 people, two business units | No person can read every change | Every mandate that can be checked is a guardrail in the delivery path |

At every size the users of the nudge, the tax and the mandate are the teams that choose and the teams that live with the result. The instruments are working when most teams are on the paved paths by choice, when the mandate list stays short, and when a decision does not wait.

## Who Carries Governance: Architects as Connectors

None of these instruments runs by itself. Advice has to come from someone who knows several teams' systems, a paved path exists because someone noticed the same advice being given a fifth time, and a mandate list needs an owner. Governance by advice therefore relies on staff and principal engineers and on architects. This book calls them the staff-plus roles and defines them in [[staff-plus-and-architects]]; here I say only what governance asks of them.

It asks them to connect. Hohpe's image is an elevator in a tall building: the architect rides between the floor where strategy is set and the engine room where the code is written, and is useful because few others visit both. He writes that "instead of the superhero we need 'super glue' architects", who hold architecture, technical details, business needs and people together, and *Grounded Architecture* takes the same line.

In governance that means four jobs. Staff-plus engineers and architects give advice early, while a decision can still change. They turn advice that keeps repeating into a paved path or a guardrail. They keep the mandate list short, as contributors to it and, in the words of *Grounded Architecture*, "not the sole authority". And they carry what teams learn back to the engineering strategy, so that a policy nobody can follow is changed. *Grounded Architecture* puts the stance in one sentence: "Architects should help teams make better decisions, not create approval queues." Their users are the teams and the executives at the two ends of the elevator. I would judge them by the decisions they improved, visible in the records that name their advice, and by how much repeated advice they made unnecessary.

## Anti-Patterns: The Gate, the Stall and the Growing Rulebook

Governance of this kind fails in three ways, and the first is the one the chapter opened with. **The Review Bottleneck** returns whenever teams wait for a forum before they act, whatever the forum is called. Three signs show it. Teams present finished designs instead of open questions. Nearly everything is approved. And work stops until the hearing.

The opposite failure appears when a board is removed and nothing is said about who decides. **The Consensus Stall**, another of this book's failure patterns, is a decision that reopens in meeting after meeting. Here it takes one form: the team treats advice as agreement to be reached, and does not decide until every adviser concurs. Harmel-Law rules this out in a sentence: "We are not looking for consensus here, but we are looking for a broad range of inputs and voices." Advice is heard and recorded, and then the team decides.

The third failure belongs to mandates, and I report it from experience. After each incident someone adds a rule, and no rule is ever removed. In a few years the list holds thirty mandates. Teams can no longer tell the three that protect the company from the twenty-seven that record an old preference. The remedy is the discipline of the short list: every mandate carries its reason and its owner, and a mandate whose reason has gone is removed.

## Worked Example: Corvane's New Broker

Corvane's forum and its broker put all of this to use. In 2026, at about 500 people, Dario Vance wrote Corvane's engineering strategy, which [[engineering-strategy]] follows. Its policies changed the forum's rule from approval to advice: the forum now hears questions and does not vote. They also named three **shared areas**, deploying, messaging and identity, where one team's choice is something other teams must live with. Sorted by the cost of divergence, Corvane's decisions then looked as the table shows. The result, an advisory forum, taxes and a short list of mandates, is the mix the size table gave for 500 people.

| Decision | Where the cost of divergence falls | Instrument at Corvane |
| --- | --- | --- |
| What stays inside a team's own services | Inside the team | The team decides |
| Which way of deploying, which broker or which identity library a service uses | On every engineer who changes teams, and on whoever runs each variant | Nudge and tax: one standard per shared area is the default for new services; a team that needs something else writes a decision record and operates its choice itself |
| Bringing a new technology into a shared area | On every team, for years | The advice process, decided and recorded by the Director of Platform; and a mandate: only as a replacement |
| Where customer data is stored | On the company, as legal exposure | Mandate, checked as a guardrail |

The broker request then went through the new arrangement. Messaging is a shared area, so the strategy places the decision with the owner of that area: Lena Brandt, Corvane's Director of Platform. That is as close to the work as this cost of divergence allows. She decided by the advice process. The three teams wrote the proposal as a decision record. Written advice came from the two teams on the oldest broker, as the people affected, and from the forum, as the people with expertise. The advice confirmed the need: replaying schedule-change events served the first step of Corvane's product strategy, set out in [[vision-and-product-strategy]], that every schedule change reaches the customer and the technician. The advice also changed the proposal. A fourth broker kept beside the others would add to a cost every team was already paying, so the record proposed the new broker as a replacement.

The record also fixed what is planned before anyone starts, because the strategy demands it. A new technology enters a shared area only as a replacement, and its record names what it retires, who moves the existing users, and by when. In this chapter's terms that rule is one of Corvane's few mandates: adding without retiring is how three brokers came to exist, and the cost falls on every team for years. The record names the new broker as Corvane's one standard for messaging. New services get it by default, which is the nudge. A team that needs something else writes its own record and operates its choice itself, which is the tax. The platform team owns the migration. Billing Integrations and Stock Integrations move first, on a stated date the oldest broker is switched off, and the other two brokers follow, each with its own date. How such a migration is finished is the subject of [[migrations-and-technical-debt]].

Lena Brandt recorded the decision twelve days after the request reached her under the new rule. The same request had spent six weeks in the forum without a decision. Over the next two quarters the median time from a team's question to a recorded decision was six days, where a design had waited a median of 23 days for a hearing alone. One cost remains, and the record states it: until the first switch-off date Corvane runs four brokers.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. The model above was described for people who write code, and the two claims here ask what becomes of records, guardrails and boards when coding agents write much of it. **Emerging.** As of November 2026, teams I have observed give their coding agents the decision records and the paved-path templates as context. A recorded decision then reaches code written by an agent that nobody briefed, and a guardrail checks an agent's change exactly as it checks a person's. This is my observation; I know of no published measurement, so the chapter makes no Proven claim.

**Speculative.** If agents multiply the number of changes, a board of people falls further behind, and a mandate that is not an automated check stops being enforced at all. Corvane's story for 2027 and 2028, at 1,100 people, is the illustration: fourteen teams have each chosen their own coding agent, model provider and prompt conventions, and security cannot say what data leaves the company. No board of people could have heard fourteen such choices in time, and a data rule that lived in a document checked nothing. By the three questions, what data may leave the company is a mandate, checked as a guardrail. Which agent a team uses is a nudge toward a supported default. The claim would be confirmed where review queues lengthen as the volume of changes rises; [[where-the-constraint-moves]] weighs the published evidence.

## What to Take Away

**Established.** What the sources agree on:

- Some choices should be made once for the whole company, and which ones is a business decision (Ross, Weill and Robertson, *Enterprise Architecture as Strategy*).
- A nudge preserves choice, and a default is a powerful nudge (Thaler and Sunstein, *Nudge*).
- Seeking advice does not mean seeking consensus, and the decider stays accountable (Harmel-Law).
- A decision record is short, lives with the code, and is superseded, never erased (Nygard).

**Depends on context.** What changes with the situation:

- Which choices are worth consistency depends on what divergence has already cost you. Count it before you standardize.
- Where the line for a mandate falls depends on regulation and on the customers you serve.
- Whether you need a forum depends on size. At a dozen people a conversation does its work.

**The author's synthesis.** What is this book's own position:

- One scale of force, from advice to mandate, ordered by the cost of divergence, is my arrangement of *Grounded Architecture*'s three instruments with the advice process as the default.
- The tax paid in operating work, and the rule of raising an instrument only on evidence, are my extensions.
- Measuring governance by how long a decision waits is my recommendation.

## Checklist

The four instruments are one scale with one rule for reading it. The further the cost of a choice travels from the team that makes it, the more force the organization may use. The record is what keeps every point on the scale visible and reversible. Run these eight checks on your own organization.

- [ ] List every approval a team waits for before it may start technical work.
- [ ] Put each through the three questions, and mark the ones that could become advice with a record.
- [ ] Write the mandates that remain on one page, each with its reason and its owner.
- [ ] For each mandate, ask whether a guardrail could check it automatically.
- [ ] Measure the days from a team's question to its recorded decision.
- [ ] Search for the record of a decision made last year in another team, and time how long it takes you.
- [ ] Name a paved path that teams leave, and ask three of them why.
- [ ] Name who gives cross-team advice in each group, and check that their name appears in recent records.

Corvane's forum was slow because it was a queue, and its landscape diverged because approving one design at a time never asked what a choice cost the other teams. The broker was decided by the owner of the shared area, after advice from the teams that needed it and the teams it affected, with a migration plan in the record. A leader who replaces most approvals with advice and records, and keeps a short written list of mandates, can then watch one number: how long a decision waits. A paved path, the main form of the nudge, is something that has to be built, kept up and chosen by its users, which makes it a product. The next chapter treats the platform as exactly that, the paved path made into a product with its own users and its own outcome measure: [[platforms-and-developer-experience]].

## Sources and Evidence

**Books**

- *Grounded Architecture: Redefining IT Architecture Practice*, Željko Obrenović, online edition at grounded-architecture.io, read November 2026. Nudges, taxes and mandates as a portfolio of governance instruments; mandates used sparingly; golden paths; architects who help teams decide and do not create approval queues; the superglue architect. Pages read: "Governance Principles: Nudges, Taxation, Mandates", "Operating Model: General Principles" and "Thinking Like an Architect: Architects as Superglue".
- *The Software Architect Elevator*, Gregor Hohpe, 2020. Decision makers who lack the relevant information; the architect who rides between levels; the "super glue" architect.
- *Nudge: The Final Edition*, Richard H. Thaler and Cass R. Sunstein, 2021. The definition of a nudge; choice architecture; defaults.
- *Enterprise Architecture as Strategy*, Jeanne W. Ross, Peter Weill and David C. Robertson, 2006. Standardization as a business decision; compliance and exception processes and a central standards team as governance mechanisms.

**Practitioner sources**

- "Scaling the Practice of Architecture, Conversationally", Andrew Harmel-Law, martinfowler.com, 15 December 2021. The architecture advice process, the advisory forum, advice recorded with the decision. It supplements the author's bookshelf and was read for this chapter.
- "Documenting Architecture Decisions", Michael Nygard, cognitect.com, 15 November 2011. The five-part decision record and the rule that a superseded record is kept. It supplements the author's bookshelf and was read for this chapter.
- The author's working records: [[architecture-as-advice-and-guardrails]], [[architecture-advisory-forum]], [[markdown-records]], [[decisions-stay-with-teams]], [[governance-as-code]] and [[standardize-before-diverging]].
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
