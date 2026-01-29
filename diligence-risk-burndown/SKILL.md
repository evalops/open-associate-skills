---
name: diligence-risk-burndown
description: "Run diligence as a fast risk burn-down: build a ranked risk register, execute the fastest tests, and produce decision-changing evidence. Use when a deal advances past first meeting."
license: Proprietary
compatibility: Works offline; improved with web access and customer calls; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Diligence risk burn-down

## When to use
Use this skill when:
- A company is past first meeting and needs structured diligence
- You need to answer “what could kill this?” quickly
- You need customer, product, GTM, and team evidence for an IC memo

## Inputs you should request (only if missing)
- Stage + round dynamics (lead? follow? timeline?)
- A draft “must be true” list from the first meeting
- Access to customer references (including churned / lost deals if possible)
- Data room or key docs (deck, pipeline, financial model, product docs)

## Outputs you must produce
1) **Ranked risk register** (top 3–5 risks)  
2) **Diligence plan** (tests, owners, deadlines)  
3) **Evidence pack** (notes + quotes + data)  
4) **Go/No-go recommendation** with rationale

Templates:
- assets/risk-register.md
- assets/diligence-plan.md
- assets/customer-call-script.md
- assets/product-eval-checklist.md

## Procedure

### 1) Build the ranked risk register (start here)
List risks in these buckets:
- Market risk
- Product risk
- GTM risk
- Team risk
- Competitive/moat risk
- Deal/term risk (if relevant)

Then rank by: *decision impact* × *uncertainty*.

Rule: if you can’t name the top 3 ways this fails, you aren’t diligencing yet.

### 2) Define the fastest falsification test for each top risk
For each risk, write:
- What evidence would increase conviction?
- What evidence would kill the deal?
- What is the fastest test that generates that evidence?

Examples of fast tests:
- 5 buyer calls using a consistent script (not friends)
- pipeline inspection: stage aging, sources, cycle time
- hands-on product evaluation with a “blank sheet” re-explain test
- churned / lost prospect reference calls

### 3) Run customer diligence (buyers first)
Do at least:
- 3 buyer calls (people who sign)
- 2 user calls (people who use daily)
- 1 “failed” call (lost deal, churn, or disqualified)

On calls, capture:
- Trigger event
- Alternatives considered
- What would make them churn
- Expansion path and constraints
- Procurement/security blockers

### 4) Product diligence (can it survive reality?)
- Request a live demo, then ask the founder to re-explain from scratch.
- Ask for 2–3 hard examples where the product broke and how they fixed it.
- Identify integration points and estimate real deployment cost.

### 5) GTM diligence (repeatability)
- Validate ICP specificity (not “mid-market enterprises”).
- Validate cycle time and onboarding (time-to-value).
- Validate pricing logic and unit economics *by segment*.

### 6) Team diligence (learning rate + decision rights)
- Look for:
  - ability to change mind with evidence
  - clear ownership of GTM/product/eng
  - healthy conflict resolution

### 7) Competitive diligence (why incumbents don’t win)
- Identify:
  - direct competitors
  - incumbent “good enough” substitutes
  - internal build threat

Ask: “If an incumbent shipped a V1 in 6 months, what still makes you win?”

## Salesforce logging (recommended)
- Ensure an **Opportunity** exists with a “Diligence” stage.
- Log each reference call as an Activity and tag it (buyer/user/churn).
- Create Tasks for diligence workstreams with owners and due dates.
- Attach/record the risk register + evidence pack (as Notes or Files).

Use `salesforce-crm-ops` if you need API patterns.

## Edge cases
- If the process is rushed: focus only on top 2 risks and explicitly document what you *did not* validate.
- If references are all friendly: insist on at least one “failed” reference; otherwise discount the signal.
