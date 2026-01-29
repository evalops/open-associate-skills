---
name: diligence-sprint
description: "A time-boxed diligence sprint (3–7 days) that burns down the top risks and produces IC-ready evidence. Use when a deal is live and you need speed without losing rigor."
license: Proprietary
compatibility: Works offline; improved with calls and data access; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Diligence sprint

## When to use
Use this compound skill when:
- A deal is live and you have a hard decision deadline
- You need a clear risk burn-down plan and daily deliverables
- You want to coordinate multiple diligence workstreams

## Inputs you should request (only if missing)
- Deadline (term sheet / IC date)
- Intended role (lead/follow) and check size
- Top 3 “must be true” claims from first meeting
- Customer access constraints

## Outputs you must produce
- Day-by-day plan with owners
- Ranked risk register and fast tests
- Evidence pack
- A memo-ready set of findings

## 5-day default sprint plan (adapt as needed)

### Day 0 (setup, 1–2 hours)
- Align on top 3 risks + tests
- Assign owners and schedule calls
- Create Salesforce Tasks for each workstream

### Day 1 (customers)
- 3 buyer calls + 2 user calls
- Write a customer summary (what triggers purchase, what blocks it, what churn looks like)
- Update risk register

### Day 2 (product)
- Hands-on demo + deployment reality
- Identify integration blockers and time-to-value
- Update risk register

### Day 3 (GTM + metrics)
- Pipeline review + unit economics
- Segment-specific GTM truth (cycle time, pricing, margins)
- Update risk register

### Day 4 (team + competition)
- Team learning rate and decision rights
- Competitive map and “incumbent build” threat
- Update risk register

### Day 5 (synthesis)
- Draft memo sections: market, product, traction, GTM, team, risks
- Prepare IC readout: recommendation + best argument against
- Log deliverables in Salesforce (Files/Notes)

## Guardrails
- If you can’t get a failed customer reference, discount retention claims.
- If the deadline compresses: do fewer risks, not more shallow work.
