<%*
const f = tp.file.folder(true);
const layer = f.startsWith("Company") ? "company" : f.startsWith("Teams") ? "team" : "personal";
const team = f.startsWith("Teams/") ? f.split("/")[1] : "";
const segment = await tp.system.prompt("customer segment");
-%>
---
date: <% tp.date.now("YYYY-MM-DD") %>
type: vpc
tags: [vpc, strategy]
ai-first: true
layer: <% layer %>
team: <% team ? '"[[' + team + ']]"' : "" %>
segment: "<% segment %>"
status: hypothesis
fit: none
evidence: []
strategy: "[[TBD]]"
---

# <% tp.file.title %>

## For future agent
This note is a Value Proposition Canvas for the customer segment <% segment %>. The left half (customer profile) records jobs, pains, and gains from evidence; the right half (value map) records how our offer addresses them. Status hypothesis means the profile is not yet backed by customer evidence; check `evidence:` before trusting it.

## Customer profile

## Customer jobs
What the customer is trying to get done. Functional, social, and emotional; rank by importance.
| Job | Kind | Importance (1-5) | Evidence |
|---|---|---|---|
| TBD | functional | TBD | TBD |

## Pains
Bad outcomes, risks, and obstacles related to the jobs. Rank by severity.
| Pain | Severity (1-5) | Evidence |
|---|---|---|
| TBD | TBD | TBD |

## Gains
Outcomes and benefits the customer wants, required, expected, desired, or unexpected. Rank by relevance.
| Gain | Kind | Relevance (1-5) | Evidence |
|---|---|---|---|
| TBD | expected | TBD | TBD |

## Value map

## Products and services
- TBD

## Pain relievers
How the offer eliminates or reduces specific pains. Reference the pain by name.
| Reliever | Addresses pain | Strength (1-5) |
|---|---|---|
| TBD | TBD | TBD |

## Gain creators
How the offer produces specific gains. Reference the gain by name.
| Creator | Addresses gain | Strength (1-5) |
|---|---|---|
| TBD | TBD | TBD |

## Fit
- Top 3 pains covered by a reliever: TBD
- Top 3 gains covered by a creator: TBD
- Important jobs, pains, or gains we do not address (gaps): TBD
- Fit stage: none, problem-solution (we understand them and have a credible offer on paper), product-market (evidence they want it), business-model (a profitable, scalable model)

## Assumptions to test
Each risky assumption becomes an experiment linked to a solution in discovery ([[Opportunity Solution Tree]]):
- TBD

Method: [[Value Proposition Canvas]].
