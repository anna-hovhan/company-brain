---
date: {{TODAY}}
type: hub
tags: [hub, strategy]
ai-first: true
layer: company
---

# Company Strategy

## For future agent
This is the company strategy hub: the current strategy kernel, value proposition canvases per customer segment, business model canvases, and Playing to Win choices. Strategy notes explain how the company will win given its [[Mission]] and [[Vision]].

## Current strategy
```dataview
TABLE framework, horizon, status, owner
FROM "Company/Strategy"
WHERE type = "strategy"
SORT status ASC, date DESC
```

## Value proposition canvases (by segment)
```dataview
TABLE segment, fit, status, length(evidence) AS "evidence"
FROM "Company/Strategy"
WHERE type = "vpc"
SORT fit DESC
```

## Business model canvases
```dataview
LIST FROM "Company/Strategy" WHERE type = "bmc"
```

## How strategy connects
[[Mission]] and [[Vision]] set the destination. The [[Strategy Kernel]] (diagnosis, guiding policy, coherent actions) and [[Playing to Win]] choices set the route. [[Value Proposition Canvas]] notes test customer fit per segment. Annual objectives in [[Company OKRs]] turn the guiding policy into measurable outcomes, and [[Company Discovery]] finds the solutions.

Create with `/company-brain:strategy` (kernel, Playing to Win, BMC) or `/company-brain:vpc` (one canvas per segment).
