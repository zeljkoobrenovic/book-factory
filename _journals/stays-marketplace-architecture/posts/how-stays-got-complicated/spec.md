---
status: accepted
revised: 2026-11-18
---

# Spec: From Inn Door to Instant Book: How Stays Got This Complicated

## Intent

Give a reader who knows nothing about travel accommodation the order in which the book's concepts entered the world, so that the sixteen failure patterns on the next page read as natural consequences rather than as a list of mistakes. The page walks, in plain language and nine steps, from a traveller knocking at an inn door at dusk to today's hotel and home marketplaces. Each step names one need, the concept that answered it (in plain words first, then the book's term with a link to the chapter that owns it), what it made possible for **both** the guest and the innkeeper, host or hotel, and what it cost. It is an explanation of today's complexity told in the order it accumulated, not a history of the industry; [[two-stay-marketplaces]] tells that history with its companies and deals.

**Thesis (disputable):** stays platforms are complex not because anyone designed them badly, but because **each way of selling a night was a good bargain that let a guest book a room she could not see, and let a hotel or host fill a night that would otherwise perish, at the price of one more copy of the room book and one more party standing behind the promise; none was ever retired**, so one night today is promised from many copies by many parties, and fails wherever a copy learns the truth late or a party stands behind less than the guest believes.

**Running question, answered at every step:** *is the room really free for these nights, and who stands behind the promise?*

**Role in the Preface:** after [[introduction]] (which states the perishable promise and opens with a family at a reception desk with no booking) and before [[where-stay-platforms-go-wrong]] (which names the patterns). The page supplies the "why" the patterns page assumes.

**Transition in:** the introduction's hand-off now points here: before the patterns, see how one night came to be promised by so many parties.

Productscape domains covered: none as a product brick; the page is a preface that orders concepts across both models (TAM and HSM).

## Audience

The book's readers (architects and engineering leaders of OTAs, hosted-stays marketplaces, channel managers and PMS vendors), and anyone new to the field they hand the book to. The page assumes no travel vocabulary; every term is introduced in plain words before it is named.

## Success criteria

Reader outcomes (each is a probe a reader can be asked after reading):

- [ ] Given a concept from a later chapter (reservation, no-show, room type, rate plan, GDS, channel manager, agency or merchant model, metasearch, rate parity, listing, iCal sync, facilitated payments, STR registration), the reader says which step introduced it and what limit of the step before it answered.
- [ ] Given a failure-pattern name, the reader says which step makes it possible and why (the tally's last column uses the sixteen names exactly).
- [ ] The reader can retell the walk in one sentence per step, and can say what each step made possible for the guest and for the hotel or host before saying what it cost.
- [ ] The reader can answer the running question for the inn door and for the Seville double booking, and explain why the answer grew.
- [ ] The reader can tell the illustrations (the inn, the letter, the agent's booking, the central office scene) from the dated anchors, and knows the account is simplified.

Shape and evidence:

- [ ] IN THIS SECTION callout and exactly three KEY POINTS naming concrete things (the inn door, the innkeeper's book, the letter, the agent, the website, the host's calendar), no "layers" abstraction; a lead that declares the simplification and links [[two-stay-marketplaces]] for the history.
- [ ] Nine steps, each in the order: where things stood, what stopped working, what was added and its name (plain words first, one new term per paragraph at most), what it made possible for both sides, what it cost, and the running question answered.
- [ ] A tally table `Step | What it made possible | What it added | New party or delay | What can now go wrong`, and an anchor timeline `Year | What its source dates to that year | Step` holding only dates the steps already give, with a sentence on why the undated steps are absent.
- [ ] Every dated or quoted fact fetched from a primary or reputable source (company history pages and filings, official legal texts, an IETF RFC), at most about a dozen; no "first ever" claims in the page's own voice; no motives attributed; Corvane appears only in the last step.
- [ ] Ten figures: one overview of accumulation and one scene per step, the same traveller and host recurring, no brand names, real company names or logos in any image.
- [ ] 3,000–4,700 words before Sources and Evidence.

## Steps (the contract for the body)

| # | Step | Need | Concept (owning chapter) | Gain: guest / hotel or host | Cost | Failure patterns named |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | The inn door at dusk | A bed tonight, far from home | The night as perishable stock; the room as the unit sold ([[introduction]], [[property-and-listing-model]]) | A bed tonight / a room filled that would earn nothing | The inn may be full; the innkeeper takes a stranger in, so payment before the key | — (plain words) |
| 2 | The letter ahead | Certainty before setting out; knowing who comes | Reservation in the book of rooms, inventory per night, no-show, deposit and cancellation terms ([[reservation-lifecycle]], [[rates-and-availability-model]], [[changes-and-cancellations]]) | Sets off knowing there is a bed / fills nights weeks ahead | A room held for nobody; a promise about a room the guest cannot see; two letters for the last room | — (plain words) |
| 3 | The guidebook and the travel agent | Choosing an inn in a town never seen; inns wanting distant guests | Someone vouches (content, [[content-and-media]]); an intermediary sells someone else's room for a commission ([[merchant-and-agency-models]]) | Chooses with someone's word / guests from cities it never advertised in | A third party; a flattering or stale description; a commission; the agent's booking must reach the inn's book | — (plain words) |
| 4 | The chain and the central reservation office | Booking any hotel of a chain from anywhere, with an answer now | Central reservation system; room types; rate codes (rate plans); deliberate overbooking and the walk ([[connectivity-and-channel-managers]], [[property-and-listing-model]], [[rates-and-availability-model]], [[inventory-integrity]]) | Instant answer from one number / rooms filled across cities | Two copies of the count; codes multiply; a walked guest | Rate Plan Sprawl |
| 5 | Airline systems and the switch | Travel agents everywhere already booking on airline screens | Global distribution system; the switch; look-to-book ([[two-stay-marketplaces]], [[stays-marketplace-economics]]) | Hotel and flight from one screen / a worldwide sales force | The same hotel in many systems; a booking acknowledged by an intermediary, not the hotel; load in proportion to shopping | The Same Hotel Twice, Lost at the Front Desk |
| 6 | The online travel agency | Booking alone, at home, at any hour, with photos and an instant confirmation | OTA; agency and merchant models; channel manager and ARI updates ([[two-stay-marketplaces]], [[merchant-and-agency-models]], [[connectivity-and-channel-managers]]) | Compares and books in minutes / a small hotel reaches the world without a sales office | Promises from a copy; one mapping per channel; someone else holds the money; cancellation rules copied into many systems | Phantom Availability, Connectivity Roulette, Ledgerless Money, Policy Spaghetti |
| 7 | Comparing everyone | Too many sites and hotels to check | Guest reviews; metasearch; ranking; rate parity ([[reviews-and-reputation]], [[two-stay-marketplaces]], [[stays-ranking]], [[promotions-and-loyalty]]) | Every seller's price and other guests' word in one place / a good small hotel found on merit | The price shown is a copy; fees added later; the order can be bought; parity rules and then law | Price Drift, Pay-to-Rank Creep |
| 8 | Homes as stays | A whole flat, a room with a local; owners with a spare room | Listing and host, one calendar; payment held until check-in and paid out; two-way reviews; instant book and request to book; iCal sync; damage protection ([[property-and-listing-model]], [[merchant-and-agency-models]], [[reviews-and-reputation]], [[checkout-orchestration]], [[calendar-sync]], [[protection-and-incidents]]) | A kitchen and a neighborhood / one flat let safely to strangers and paid | One unit with no spare room; calendars that agree only after a poll; trust built incident by incident | The Double-Booked Night, Trust After the Incident |
| 9 | Today: every step at once | All of the above, on a phone, under law | Prices that change daily; each type selling the other's supply; tourist taxes; STR registration; models ([[dynamic-pricing]], [[converging-two-marketplaces]], [[taxes-on-stays]], [[stays-regulation]], [[stays-ml-platform]]); Corvane's King's Day and Seville cases ([[meet-corvane]]) | Any night, anywhere, in seconds / any room or home sold on every channel | More copies, more parties, regulators, shocks | The Hotel-Shaped Home, The Tax Patchwork, City-by-City Firefighting, Built for Sunny Days, The Unwatched Model |

**Conclusion:** the tally table; the anchor timeline; a count of what stands behind the Bauers' Feria night that did not stand behind the knock at the inn door; the synthesis (every step moved the promise further from the room and put more copies and more parties behind it; the complexity is the price of all that trade, not a mistake); hand-off to [[where-stay-platforms-go-wrong]].

## Non-goals

- The industry's history, companies, deals and waves — [[two-stay-marketplaces]] (this page links there and reuses its dates, never contradicting them).
- The failure patterns in depth — [[where-stay-platforms-go-wrong]]; Corvane in full — [[meet-corvane]].
- Any concept's mechanics: each step names a concept and links its owning chapter.

## Modalities

- [ ] `checklist.md` — operational checklist
- [ ] `summary.md` — management summary
- [ ] `dialog.md` — two-host dialog
- [ ] `comics.md` — explainer comic

## Open questions

- [[two-stay-marketplaces]] dates AirBed & Breakfast's launch to 11 August 2008 (from a secondary source); Airbnb's own newsroom dates its first guests to October 2007 and its official launch to March 2008. This page uses only the company's "born in 2007" sentence; the chapter's date needs the author's decision.
- [[two-stay-marketplaces]] places Bookings.nl's founding in Enschede; Booking.com's own page says "Founded in 1996 in Amsterdam". This page gives only the year.
- Vacation Rentals by Owner's 1995 founding could not be read on a primary page (the company's site refused automated fetches); the page uses HomeAway's 2011 prospectus instead.

## Decision log

- **2026-11-18** — Modeled on the sibling pages `how-payments-got-complicated`, `how-commerce-got-complicated` and `how-classifieds-got-complicated` (field-evolution skill): nine steps, gain before cost, tally and anchor timeline, ten figures. Written as `spec.md`, because BOOKED has no outcome specs.
- **2026-11-18** — The lead reuses the introduction's family at the reception desk (generic, not Corvane), so the inn door and the missing booking frame the same question; Corvane enters only at step 9, through two canonical ledger cases (King's Day for hotels, Seville for homes).
- **2026-11-18** — Overbooking placed at the chain step rather than the letter step, so that step 2 carries only the reservation, the book, the no-show and the deposit, and overbooking arrives where a hotel has enough rooms and records to plan it.
- **2026-11-18** — Flow rubric by a fresh reader: order sound with fixes; applied "meanwhile" and "from the mid-1990s" markers at steps 6 and 8 so overlapping steps imply no false chronology; kept reviews in step 7 and damage protection as one clause in step 8 to hold the step count at nine.
- **2026-11-18** — Pattern names begin at step 4, the first computer; steps 1–3 name their failures in plain words.

## Sources

- **Internal**
  - `.claude/skills/field-evolution/SKILL.md`; `PLAN.md`; `_research/style-guide.md`; `_research/scenario-ledger.md` (recurring examples 2 and 3 and the King's Day reconstruction).
  - [[two-stay-marketplaces]] (the six waves), [[introduction]], [[where-stay-platforms-go-wrong]], [[glossary]] (owning chapters).
- **External**
  - IHG history page (Holidex 1965, 1977); MICHELIN Guide history article (1900); Booking.com "About" (1996); Expedia Group "About us" (1996); trivago Form 20-F for 2016 (incorporated 2005); HomeAway Form S-1 (2011); Airbnb newsroom "About us" (2007); RFC 5545 (2009); Expedia Group and Airbnb Forms 10-K for fiscal 2025; Regulation (EU) 2022/1925 Article 5(3) and the Commission's gatekeeper page (13 May 2024); Airbnb, "A message from co-founder and CEO Brian Chesky" (5 May 2020); Regulation (EU) 2024/1028 (applies from 20 May 2026).

## Changelog

- **2026-11-18** — Initial spec (field-evolution skill). *(AI-mediated session)*
- **2026-11-18** — Spec accepted (acceptance delegated by the author for these pages); article written; ten figures generated and inspected (compare figure regenerated once for a garbled sign and dollar coins, today figure twice for stray labels and a dollar coin); icon and hero image (hero regenerated once, first attempt was a text-heavy infographic). *(AI-mediated session)*
