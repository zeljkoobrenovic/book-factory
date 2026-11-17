# Verification — part-8-intro (permalink `part-8`)

Verification pass of 17 November 2026. A part introduction cites no external source: each statement about Stripe, Adyen, a network or a regulation repeats a chapter of the part. Each was looked up in the owning chapter's current `index.md`, in that chapter's verification file and in rulings 18–45 of `consistency-issues.md`. No external source was fetched in this pass; "agrees" means agrees with the verified chapter, not re-confirmed at the source. Chapters 38, 40 and 41 were verified when the pass began; the files for chapters 37 and 39 appeared during it and were read before the page was finished.

| # | Claim (short) | Owning chapter | Status | What changed |
| --- | --- | --- | --- | --- |
| 1 | "several hundred deployments a day" | 41 | agrees | The chapter: about 400 a day to one core API service |
| 2 | In every design Stripe or Adyen has published, the record of money is not among the things relaxed; the author's reading, not a stated principle | 37 (inference block) | agrees | — |
| 3 | Both have documented their choices on outages, data stores, limits and rollouts, "with dates" | 37, 38, 40, 41 | agrees | "with dates" cut for length only |
| 4 | "Neither has published how its regions, cells, failover or replication settings work" (lead and KEY POINT 3) | 37 (row 46), 38 (row 57), 39 (rows 40–43); rulings 42(b), 45(a) | corrected to match | Adyen names data-center regions, states failover between data centers in general terms, and an engineer has said it uses both replication modes. Now: neither has published "a cell design, the topology or timing of a failover between regions or which data is replicated synchronously"; KEY POINT 3: "the topology or timing of a failover between regions" |
| 5 | Neither has published how its webhook sender is built | 20 | agrees | — |
| 6 | The published uptime figures measure five different things and cannot rank the two | 37 (row 24); ruling 45(b) | agrees | Still five kinds after the chapter's correction |
| 7 | Ch. 37: a payment path stays up because something else gives way | 37 | agrees | — |
| 8 | Ch. 37: Adyen described in 2021 an edge that keeps answering while accounting runs behind | 37 | agrees | — |
| 9 | Ch. 37: Stripe described in 2017 shedding non-critical requests first | 37 | agrees | — |
| 10 | Ch. 37: what is repaired afterwards is the payments whose outcome nobody knows, which no uptime figure reports | 37 | agrees | — |
| 11 | Ch. 38: Stripe scaled a document database to more than 2,000 shards (2024) | 38 | agrees | — |
| 12 | Ch. 38: Adyen scaled PostgreSQL, with accounting clusters filled in rotation (2021) | 38 | agrees | — |
| 13 | Ch. 38: in what either has published, no transaction spans the shards | 38 | agrees | — |
| 14 | Ch. 38: an outbox stores a state change and the message announcing it in one local transaction | 38 | agrees | — |
| 15 | Ch. 39: the chapter is short because little is public | 39 (row 74) | agrees | — |
| 16 | Ch. 39: a localization law decides first; Stripe's page on India (updated 2023) lists the features cut | 39 (rows 16, 25) | agrees | The page displays "Last updated: May 16, 2023"; the disabled features are Card Updater, Revenue Recognition and Sigma |
| 17 | Ch. 39: Stripe runs on Amazon Web Services | 39; 40 (row 16) | agrees | — |
| 18 | Ch. 39: Stripe "names no regions" | 39 (row 31) | corrected to match | Stripe names data centers in the United States and India for authentication data; the chapter's key point is "names no AWS region", and the page now says that |
| 19 | Ch. 39: Adyen "names five regions without locations" | 39 (rows 40, 76); 37 ("For other pages"); ruling 45(a) | corrected to match | Adyen's website lists its data centers by continent or country. Now: "runs its own data centers and names them by continent or country, no finer" |
| 20 | Ch. 40: a merchant's peak meets the provider's per-customer limit long before its capacity | 40 | agrees | — |
| 21 | Ch. 40: Stripe documents 100 requests a second per account | 40; 21 | agrees | — |
| 22 | Ch. 40: Adyen publishes no limit for payments | 40; ruling 42(a) | agrees | — |
| 23 | Ch. 40: the party that creates the load paces it | 40 | agrees | The chapter's judgement |
| 24 | Ch. 41: Stripe's 2023 annual letter (published 2024) describes about 400 deployments a day, sent to rising shares of traffic and withdrawn automatically | 41 | agrees | — |
| 25 | Ch. 41: a change that reached 1% failed payments for six minutes on 8 February 2024 | 41 | agrees | — |
| 26 | Ch. 41: Adyen's 2018 account switches features on one by one after a release | 41; ruling 43(b) | agrees | The page does not say this is all that is known of Adyen's cadence |
| 27 | A localization law fixes the country where data is stored (gloss) | 39 | agrees | — |
| 28 | Ch. 41: a change is finished when the records agree, given as "my rule" | 41 | agrees | — |
| 29 | Rulings 5 and 43(a), (c) | — | agrees | The page makes no statement they touch |

Counts: 29 statements checked: 26 agree, 3 corrected to match, 0 no longer in the chapter and removed.

## Re-check after chapter verification

Nothing remains. Rows 15–19 were first checked against chapter 39's unverified text and checked again when its file appeared; row 18 changed at that point.

## Other checks

- **KEY POINTS:** three; the first two match the chapters; the third was narrowed (row 4).
- **Chapter paragraphs:** each names the chapter's question and its Larkfield case: the 44-minute outage drill (37), the outbox after 146 purchases (38), the Hamburg chain's questionnaire (39), the wave of about 357,000 renewals paced over 18 hours under K5 (40), the March 2026 upgrade and the May 2027 one starting with 62 of 6,200 studios (41).
- **Larkfield (one correction):** ruling 37(a). The lead now says the 7,900 renewals were turned away before any card was charged, the job marked them failed, and an email job that could not tell a decline from a card never charged sent the dunning emails. Checked and agreeing with the ledger: 1 October and 1 November 2026, 1,840 members, €71,300, 212 disputes, six hours, 146 purchases *(illustrative)*, 44 minutes, 357,000, 18 hours, K5, six days, 62 of 6,200.
- **Links:** all seven `[[permalink]]` targets are valid; "Parts II to VII" is a plain range followed by `[[part-7]]`.
- **Length and format:** 1,200 words (limit 1,200; was 1,183); `timetoread` 5 min (1,200 ÷ 230); unit count and order unchanged. One lead sentence ("One chapter is short for that reason") was cut because the chapter paragraph says it. `spec.json`: p01, p04 and the chapter-39 paragraph brought into line; changelog entry added.
- **Finish:** `validate_spec.py` ok; `check_draft.py structure` pass; build clean for this journal; render check OK.

## Ledger conflicts

None found.

## For the author

- Fields copied from `journal-spec.json` still carry the older wording and were not edited: `thesis.claim` and the thesis statement ("neither has published how its regions, cells or failover work"), `thesis.how_why` ("the public record of both companies is silent") and AC-3 ("regions, cells, failover and the webhook sender are not public for either company"). Rulings 42 and 45 make these too strong for Adyen. The page keeps the word "cell" so that AC-3 is still met.
