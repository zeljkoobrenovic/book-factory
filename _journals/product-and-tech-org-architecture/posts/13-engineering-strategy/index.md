---
title: "Engineering Strategy"
date: 2026-11-19
author: Željko Obrenović
excerpt: "What is an engineering strategy, and how does it relate to the product strategy? It is a written diagnosis and a few policies that settle recurring decisions once. It takes from the product strategy what must become true, and gives back constraints."
permalink: engineering-strategy
timetoread: 18 min read
---

> **IN THIS CHAPTER, YOU WILL:** learn to write a diagnosis and three policies for an engineering organization, test each policy, and connect the result to the product strategy.

> **KEY POINTS:**
>
> * **Every engineering organization already has a strategy in its behavior.** Writing it down, as a diagnosis and a few policies, is the first step to changing it.
> * **A policy settles a kind of decision in advance.** Three areas cover most conflicts: how capacity is allocated, which rules are fixed and who decides what. Each policy must be a real choice, apply to a decision this quarter and be true of how the organization behaves.
> * **The product strategy is the input.** The engineering strategy takes from it what must become true and in what order, and gives back constraints the product strategy has to respect.

> **[FAILURE PATTERNS THIS CHAPTER ADDRESSES](where-product-and-tech-organizations-go-wrong.html):**
>
> * **The Consensus Stall** — with no policy, a forum argues each recurring technical question again until everyone agrees.
> * **The Escalation Ladder** — with no written decision rights, each such question climbs to the executive.
> * **The Review Bottleneck** — a rule enforced only by approving every design turns the approver into a queue.

<br>

In 2026 three teams at Corvane, the fictional company this book follows, asked for a new message broker. Corvane makes scheduling software for field-service companies and had about 500 people that year, in about thirty teams. A **message broker** is the software that carries messages between services, and Corvane already ran three. The request went to the architecture forum, a meeting of senior engineers that discusses technical choices reaching beyond one team. The forum discussed it in three sessions over six weeks. Every argument made in the room was reasonable. No decision came out, because nothing written said how a request of this kind is answered.

You have probably sat in a review like that one: the same kind of question returns, with different people in the room, and gets a different answer or none. What is missing is a written answer to the kind of question. This chapter's claim is that an engineering strategy is **a written diagnosis** of the engineering organization's situation and **a small set of policies**, on how capacity is allocated, which rules are fixed and who decides what, that settle decisions which would otherwise be argued again each time. It takes the product strategy as an input, because the diagnosis is of the organization's ability to deliver that product, and it gives back constraints the product strategy has to respect. The chapter starts with Corvane's request. It then defines the strategy, says what the strategy takes from the product strategy and gives back, and builds Corvane's strategy through three patterns: diagnose from behavior, write three policies and test each, and operate and review the result. It ends with where the sources disagree and what AI changes.

## Setting the Scene: The Fourth Broker

The three teams had a technical case. The broker they wanted keeps messages, so that a service that was offline can replay what it missed, and the broker they used could not do that. The engineers who objected had a case too. Corvane already ran three brokers, and the oldest, still used by two teams, had never been retired. A fourth would be one more thing to operate, to secure and to learn. Each of the three sessions had different people in it, and each reopened the question from the start.

The forum could not settle the request because it had never settled one of its kind in the same way twice. Its notes for 2025 and 2026 show eleven requests for a new way of deploying software, of messaging or of checking identity. Most were granted, one of them after a single meeting, and the answer depended on who attended. The result was four ways of deploying, three brokers and two **identity libraries**, the shared code that checks who a user is. Deploying, messaging and identity are choices that other teams must live with, and this chapter calls such choices **shared areas**. Corvane had never written an engineering strategy. It had one all the same, visible in those eleven answers: **each team chooses, and nothing is retired**.

## A Strategy Is a Diagnosis and a Few Policies

A written strategy has a known shape. In *The Engineering Executive's Primer*, Will Larson defines an engineering strategy as a document that states three things: the what and the why of engineering's resource allocation against its priorities, the fundamental rules that all teams must follow, and how decisions are made within engineering. He builds it on the **kernel** that Richard Rumelt describes in *Good Strategy Bad Strategy*, which has three elements. The **diagnosis** is, in Larson's words, "a theory describing the nature of the challenge", and its purpose is to identify root causes. The guiding policies are the approaches chosen for dealing with the challenge, and each implies a trade-off. The coherent actions carry the policies out. This chapter says **policy** for a guiding policy: a written rule that settles a recurring decision in advance.

A policy is easily confused with two other things, a decision and a slogan, and the three differ in how many cases they settle.

| Statement | Example | What it settles |
| --- | --- | --- |
| A decision | "The three teams may use the new broker." | One case |
| A slogan | "We hold a high bar for engineering excellence." | No case, since nobody would say the opposite |
| A policy | "A new technology enters a shared area only as a replacement for one it retires." | Every case of that kind, before it arises |

Policies also exist before anyone writes them. Every engineering organization has a strategy in its behavior: the choices it makes again and again are its policies, written or not. Larson gives the example of Uber in 2014, which in his account had an implicit technology strategy of letting teams select their own tools. Nobody enforced a rule against it, and the service tooling ran any container. Corvane's "each team chooses" is the same strategy, arrived at without a decision. This is why Larson distrusts strategies that describe an ideal: "The reason most written strategies don't apply is that they're actually visions of how things could ideally work, rather than accurate descriptions of how things work today." A written strategy starts from what the organization does. Writing it down makes it something people can discuss, disagree with and change.

Writing it down has an order. Larson's later book, *Crafting Engineering Strategy*, sets it out as five steps. I cite that book only through the checklists I wrote from it, because I have no reading notes for it. **Exploration** gathers what already exists, inside the organization and outside it. **Diagnosis** names the problem. **Refinement** tests the diagnosis and the ideas before anything is committed. **Policy** sets the rules, with their trade-offs. **Operations** are the mechanisms that keep the policies in force. The rest of this chapter follows these steps in three patterns: one for exploration and diagnosis, one for policy and one for operations. Refinement gets no pattern of its own, because its testing is done inside the first two patterns. The figure below shows the steps, and its arrow back from operations is the review of the strategy.

---begin mermaid---
flowchart LR
    E["Exploration: read what exists"] --> D["Diagnosis: name the cause"]
    D --> R["Refinement: test before committing"]
    R --> P["Policy: three areas, each tested"]
    P --> O["Operations: keep it in force"]
    O -->|"review"| D
---end mermaid---

**Figure 1:** *A strategy is written in five steps, and each review returns to the diagnosis.*

## What It Takes from the Product Strategy, and What It Gives Back

Exploration begins with the product strategy, because a diagnosis has to be a diagnosis of the ability to do something. [[vision-and-product-strategy]] described a product strategy as a few ordered steps toward a vision of the customer's future, each with a statement of what must be true first. Those statements, and the order of the steps, are what the engineering strategy takes. They tell the engineering executive what the organization must be able to deliver and when, and the diagnosis asks why it cannot yet. Larson's advice covers the case where nothing above engineering is written down: draft your own understanding of the company's direction, starting from questions such as who the products' users are and how work is prioritized for them.

In return the engineering strategy gives back constraints, of two kinds. The first is whatever has to be built or brought to one form before a product step can start, which can move a step's date or change the order of the steps. The second is capacity kept for work that no product step asks for. Larson tells the engineering executive to think about "the priorities that no one else is asking for", and he names security, reliability, compliance and developer productivity. Capacity held for them is capacity the product strategy cannot count on. How that share is fixed in a plan and defended each quarter is the subject of [[planning]].

At Corvane, what engineering takes can be read off the first two steps of the product strategy that Priya Nambiar, the chief product officer, wrote in 2025. Each step puts a question to engineering. What the engineering strategy gives back needs its policies first, so it is shown in a table at the end of the pattern that writes them.

| Product strategy step | What must be true first | The question it puts to engineering |
| --- | --- | --- |
| 1. Every schedule change reaches the customer and the technician without a phone call | Every change is published in one way; in 2026 three brokers carry them | Why are there three, and what would bring them to one? |
| 2. When a technician is sick, the product proposes a repaired plan | Parts data in one form from the Stock Integrations team, which connects Corvane to customers' stock systems | Who fixes the form of the stock data, and when? |

## Pattern: Diagnose from Behavior

The first pattern produces the diagnosis. Its author is the engineering executive. Its users are the people who will write the policies and judge them: senior engineers, engineering managers and the product leaders whose steps depend on it. The pattern is to **read what the organization has decided before saying what is wrong with it**, and then to name a cause. Rumelt's warning is that a result is not a diagnosis: "Underperformance is a result. The true challenges are the reasons for the underperformance." Larson adds working rules. Do not skip the diagnosis, because without it no solution can be judged. Have two or three leaders diagnose independently. Take the diagnosis to the skeptics. Be wary when it looks like the diagnosis from your previous job. The outcome measure I use is that those users, asked separately, name the same cause.

Corvane's exploration in 2026 was done by Dario Vance, its VP Engineering. He read three things. The first was the forum's notes, with the eleven requests. The second was an inventory of which team used what. The product teams that existed in 2024 released through the path that the platform team had built in 2024, which lets a team release its own change after automated checks. The teams formed in 2025 and 2026 had brought three other ways of deploying, and the brokers and identity libraries had multiplied in the same way. The third was the product strategy, with what each step needs to be true first. He then asked two people to write their own diagnosis before the three compared notes: Samir Haddad, a staff engineer who had been at Corvane since 2019, and Lena Brandt, the Director of Platform.

The diagnosis they agreed on fits in four lines. Like every Corvane example in this book, it is an illustration.

| Line | Corvane's engineering diagnosis, 2026 |
| --- | --- |
| What is happening | Every team formed since 2025 has chosen its own way of deploying, messaging and checking identity. |
| Why | Technical choices that other teams must live with have no owner and no rule. The 2024 release path was built for eleven teams, and nothing told a new team to use it. |
| What it costs | Step 1 of the product strategy needs one way of publishing schedule changes, and there are three. Engineers who change teams relearn the basics. The platform team's eight engineers support one way of deploying out of four. |
| What it is not | A lack of skill, or a wrong technology. Each choice was reasonable when it was made. |

The second line is what makes these four lines a diagnosis in Rumelt's sense. "Four ways of deploying" is a result, and a strategy aimed at it would be a cleanup. The second line names a cause that somebody can act on: shared choices have **no owner and no rule**. Rumelt's criterion is that "a good strategic diagnosis does more than explain a situation—it also defines a domain of action." Here the domain is narrow: the shared areas, which at Corvane are deploying, messaging and identity. Everything a team decides inside its own services lies outside it.

## Pattern: Three Policies, Each Tested

The second pattern writes the policies that answer the diagnosis, and Larson names where to write them. He structures guiding policies as three questions. What is the organization's **resource allocation** against its priorities, and why? What are the **fundamental rules** that all teams must follow, and why do they matter? And how are decisions made within engineering, which this book calls **decision rights**: who decides what? These are the three things teams otherwise argue about case by case: who gets the engineers, what may differ between teams and who has the last word. The pattern's users are the team leads and senior engineers who face such a decision. Its outcome measure is the number of recurring questions that still reach the forum or the executive each quarter.

A written policy then has to pass a test, and this chapter's test has three questions. **Is it a real choice?** A sensible organization could choose the opposite. This question is my wording of a remark of Larson's: "If a guiding policy doesn't imply a trade-off, you should be suspicious of it." The other two come from the three properties he asks of a useful policy, which are that it is applicable, enforced and creates leverage. **Does it apply to a decision someone faces this quarter?** That is his applicable: the policy can be used in a real case where two goods conflict. **Is it true of how the organization behaves**, or will it be because someone enforces it? That is his enforced, and his question to the author is whether you are willing to enforce the policy; if you are not, write one you will enforce. His third property, leverage, I do not make a question. I check it against the diagnosis: a policy that answers nothing in the diagnosis has no place in the strategy.

Corvane's strategy has three policies, one in each area, written to answer the diagnosis above. Two terms in the table come from elsewhere in the book. Corvane's teams sit in four product groups, each under a director. And its roadmap keeps 25 percent of capacity, the operation share, for work on how the product is built and run and not on features ([[roadmaps-and-horizons]]).

| Area | Policy | Why |
| --- | --- | --- |
| Resource allocation | Until each shared area has one standard in use, the operation share of every product group's roadmap goes first to convergence, the work of moving teams onto the standard, in the order the product strategy's steps need it. Messaging comes first. | Convergence that competes with features every quarter does not happen. |
| Fundamental rule | Each shared area has one standard. New services use it. A team that needs something else writes a **decision record**, a short document that states a decision and its reasons, and operates its choice itself. A new technology enters a shared area only as a replacement: its proposal names what it retires, who moves the existing users and by when. | The cost of one more way falls on other teams, where the team that chooses does not see it. |
| Decision rights | A team decides everything that stays inside its own services. A choice in a shared area is decided by the Director of Platform after written advice from the teams affected and from the forum, and it is recorded. The forum advises and does not vote. A team that disagrees can escalate once, to the VP Engineering. | A decision made by whoever attends differs every time. |

Each policy can now be put to the three questions.

| Policy | The opposite a sensible organization could hold | A decision it settles this quarter | How you would know it is true |
| --- | --- | --- | --- |
| Allocation | Every team spends its whole capacity on its own roadmap | Whether the next free engineers go to converging messaging or to a feature | The share spent on convergence, reported by each group every quarter |
| Rule | Each team picks the best tool for its job | The request for a fourth broker | New services that are not on the standard; exceptions that have no record |
| Decision rights | An architecture board approves every design | Who answers the three teams, and by when | How long a choice in a shared area waits; whether it is recorded |

The middle row shows what a policy does to the opening request. Under the rule, the question is no longer whether three teams may add a fourth broker beside the other three. It becomes whether the new broker should replace them, who moves the existing users and by when, and the third policy says who answers. The rule rests on a rule of thumb of Larson's about standards, which he offers as what he has seen work and not as a law: mostly standardize, require a trial of a new technology to promise an order-of-magnitude improvement, and limit how many trials run at once.

The same three policies are what the engineering strategy gives back to the product strategy. Each returns one constraint. The first two answer the two questions that the product strategy's steps put to engineering, and they are constraints of the first kind named earlier: something that has to be in one form before a step can start. The third is of the second kind, capacity the product steps cannot count on.

| Policy | Question it answers | Constraint it returns | What it means for the product strategy |
| --- | --- | --- | --- |
| Rule | Step 1: what would bring three brokers to one? | Messaging comes down to one broker | Step 1's milestone, which is that most appointment changes reach the customer through the product, cannot be reached before that, and a fourth broker moves the other way |
| Decision rights | Step 2: who fixes the form of the stock data, and when? | Parts data is a choice that several teams must live with, so it is treated as a shared area like the other three. The Director of Platform fixes its form after advice from Stock Integrations and the teams building step 2 | Work on step 2's proposals starts when the form is fixed |
| Allocation | None; no product step asks for it | The operation share goes first to convergence | The product steps can count on the rest of the capacity and not on that share |

A statement that fails the test settles nothing. "We hold a high bar for engineering excellence" fails the first question, because no organization would write the opposite, and so it fails the second: it gives the forum no answer for the three teams. A strategy made of such statements is what Rumelt calls bad strategy, "long on goals and short on policy or action", and two of his four hallmarks describe it: fluff, and mistaking goals for strategy. In daily work it shows up as three of this book's failure patterns, and the mapping is mine. With no rule, a forum argues each case again until everyone agrees, which is the Consensus Stall. With no decision rights, each case climbs to the executive, which is the Escalation Ladder. And a rule enforced only by approving every design makes the approver a queue, which is the Review Bottleneck.

## Pattern: Operate It and Review It

A policy that passes the test on paper stays true only through mechanisms, and the third pattern supplies them. The coherent actions of the kernel are, in Larson's account, of three kinds. **Enforcement** is the process that maintains a policy and evaluates exceptions. **Escalation** is how someone argues that a policy is wrong or does not fit their case. **Transition** is how the organization gets from the current state to the new one. He notes that long-lasting policies need fewer one-off actions and more enduring ones. Each mechanism has its own chapter in this book, and this chapter only places them. How a policy is applied across many teams, and with how much force, is the subject of [[architecture-governance]]. A transition that moves many teams is a migration, treated in [[migrations-and-technical-debt]]. The capacity is held in the plan, in [[planning]]. The pattern's users are the teams bound by the policies. Its outcome measure is taken at each review: how many decisions cited a policy, and how many exceptions were recorded.

The pattern also covers who writes the strategy, how it is launched and when it is reviewed. Larson's instruction to the engineering executive is blunt: "Commit to writing this yourself!" The executive is the one who will enforce it. He advises a working group of three to five people for early, fast feedback. The diagnosis and the policies then go to a wider set of senior engineers, managers and product leaders. The people most likely to object are found and heard before the launch. Then the strategy is announced, with a commitment to review its impact in two months. In my own strategy work I keep the diagnosis, the policies and the description of how the strategy is operated as separate records, hold exceptions in a register, and review live decisions monthly and the fit of the policies quarterly.

Corvane's launch followed that process. Dario Vance wrote the strategy himself in 2026. His working group was Samir Haddad, Lena Brandt and the engineering director of one product group, and Priya Nambiar read the diagnosis against the product strategy. Two months after the launch he reviewed it. Two policies were working. Four requests had been answered in one session each, with the forum advising by the rule and Lena Brandt deciding, and two exceptions had been recorded, each with the team that operates it. One policy was not true. Two of the four product groups had spent the operation share on features and not on convergence. The allocation policy was rewritten to name who reports the share: each group's director, every quarter. The review had applied the test's third question to the strategy itself.

## Where the Sources Disagree

The sources do not line up in every respect, and the first difference is the place of a vision. The product strategy of chapter 10 works backward from a vision of the customer's future. Larson's engineering strategy starts from today, and he derives the vision from strategies: write five engineering strategies, he says, and forecast their implications two years ahead. The two fit once the product strategy is treated as the input. The destination comes from the product side, and the engineering strategy describes the organization that has to get there, as it is now.

The second difference lies inside Larson's own account, and it is about who writes. His first recipe is bottom-up: "To write an Engineering strategy, write five design documents, and pull the similarities out." That route builds the consensus that people without authority need before a strategy is followed. For an executive he describes a more direct path, since an executive does not rely on consensus for enforcement, and the risk moves to a weak diagnosis or ineffective policies. Rumelt names the risk of the consensus route: a statement reached by people who could not agree on what to give up is a political outcome and not a strategy. Where an organization has an engineering executive, I take the direct path for the writing and keep the bottom-up recipe as the method of exploration. The past decisions are read, as Corvane's forum notes were, and the executive writes.

The strongest objection wants no written strategy at all. It holds that an engineering organization needs good judgment case by case, and that a written strategy is obvious, or obsolete by the time it is approved, or a loss of the teams' autonomy. Each part has an answer in this chapter. Case by case meant, at Corvane, by whoever attended. Obvious can be tested: had Corvane's strategy been obvious, its eleven answers would have agreed. Obsolete is what the review is for, and Corvane's first came after two months. On autonomy, Larson's observation is that the concern is usually about how a strategy was set, or about one specific strategy, and that it is worth hearing. A policy on decision rights also tells a team in writing what it may decide without asking, which the unwritten strategy never did. The objection is right about one thing: judgment is still needed in every case that no policy covers, and most cases are of that kind.

## What AI Changes Here

Claims about AI, and only those, carry one of three labels in this book: Proven, Emerging or Speculative. A written strategy now has a second kind of reader. **Emerging.** As of November 2026, teams I have observed put their engineering rules into the instruction files that coding agents read before they change a repository. A fundamental rule written as a policy, such as "new services use the standard path", can be applied by an agent on every change. A slogan gives the agent nothing to apply. This is my observation and not a measured result.

The same agents change how often the decisions arise. **Speculative.** When a coding agent can set up another broker or another deployment script in an afternoon, one more way of doing something costs less to create and as much as before to operate, secure and learn. Requests like Corvane's would then arrive more often, and many would not arrive as requests at all. The claim follows from the argument of Part XI, in [[where-the-constraint-moves]]. It would be confirmed where organizations that use agents report a rising number of distinct technologies per team in the areas where they have no written rule.

## What to Take Away

**Established.** What the sources agree on:

- A strategy has a diagnosis, policies and actions that carry them out (Rumelt's kernel; Larson, *The Engineering Executive's Primer*).
- A policy implies a trade-off, and one that implies none deserves suspicion (Larson; Rumelt on choice).
- A written strategy that describes an ideal and not today is not applied (Larson).

**Depends on context.** What changes with the situation:

- Who writes it. Where an engineering executive can enforce, the executive writes. Where nobody can, Larson's bottom-up recipe builds the consensus that enforcement needs.
- How many rules are fixed. In my view the number grows with the number of teams that must live with each other's choices: a dozen teams can settle most shared choices by talking, and thirty cannot.
- How often it is reviewed. Two months after launch is Larson's advice. After that, review it whenever the product strategy's steps change.

**The author's synthesis.** What is this book's own position:

- The strategy is there before anyone writes it. Corvane's eleven answers were a policy of letting each team choose. Writing replaces a strategy nobody chose with one that names its cause, can be tested against a decision and can be found untrue at a review.
- The three-question test (a real choice, a decision this quarter, true of behavior) is my wording of Larson's and Rumelt's criteria.
- The exchange with the product strategy runs both ways: what must be true and in what order comes in, and constraints go back.

## Checklist

The checklist turns the three patterns and the test into eight questions. One way to start is to list the last ten technical questions your review forum handled, write the policy each answer implies, and test the three that recur most. My working checklist for the writing process is in [my record of the practice](../grounded-engineering-executive/engineering-strategy.html).

- [ ] Behavior: have you listed the recurring technical decisions of the last year and how each was answered?
- [ ] Input: can you name what the current step of the product strategy needs to be true first?
- [ ] Diagnosis: does it name a cause somebody can act on, and have two leaders written it independently?
- [ ] Policies: is there one for capacity, one for fixed rules and one for who decides?
- [ ] Choice: could a sensible organization hold the opposite of each policy?
- [ ] Use: does each policy settle a decision someone faces this quarter?
- [ ] Truth: is each policy true of how the organization behaves, and who checks?
- [ ] Review: is there a date, about two months after launch, on which the strategy is checked against the decisions made since?

Three Corvane teams asked for a fourth broker, and the forum could not answer in six weeks. You can now say why: the only strategy Corvane had was the unwritten one, and it said yes to everyone. Under the three policies the request becomes a different one, about a replacement, its users and a date, and a named person decides it. Policies that settle recurring decisions still leave a question open: how are they applied across thirty teams without a board that approves every design? The next chapter gives the instruments of governance, from advice to mandate, and the record that holds each decision: [[architecture-governance]].

## Sources and Evidence

**Books**

- *The Engineering Executive's Primer*, Will Larson, 2024. The definition of an engineering strategy; diagnosis, guiding policies and coherent actions after Rumelt; the three policy areas; applicable, enforced and leverage-creating policies; enforcement, escalation and transition; writing it yourself, the working group, launch and the two-month review; the Uber example of an implicit strategy; the rule of thumb on standardizing and exploring.
- *Good Strategy Bad Strategy: The Difference and Why It Matters*, Richard Rumelt, 2011. The kernel; what a diagnosis is and does; the hallmarks of bad strategy; consensus statements as political outcomes.
- *Crafting Engineering Strategy*, Will Larson, 2025. The five steps of exploration, diagnosis, refinement, policy and operations. Cited only through the author's checklists of the book, not from reading notes.
- *Build What Matters*, Ben Foster and Rajesh Nerlikar, 2020. The product strategy as steps working backward from a vision, as presented in [[vision-and-product-strategy]].

**Practitioner sources**

- The author's record of the writing process, with a working checklist: [Engineering Strategy](../grounded-engineering-executive/engineering-strategy.html) in Grounded Engineering Executive. The author's own strategy records, kept as separate documents for the [diagnosis](../tech-strategy/diagnosis.html), the [policy](../tech-strategy/policy.html) and the [operating model](../tech-strategy/operate.html).
- The author's seven Engineering Strategy checklists (Basics, Exploration, Diagnosis, Refining, Policy Setting, Operations, Style Guide), which summarize *Crafting Engineering Strategy*.
- The statements under "What AI Changes Here" are the author's observation and reasoning as of November 2026 and are labeled as such.

Corvane is fictional; recommendations and labeled assumptions are the author's judgement.
