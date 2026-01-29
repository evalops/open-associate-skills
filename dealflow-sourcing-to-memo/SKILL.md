---
name: dealflow-sourcing-to-memo
description: "End-to-end associate workflow: thesis → sourcing → meetings → diligence → memo, with Salesforce updates. Use when you need to run the full pipeline for a sector or a specific deal."
license: Proprietary
compatibility: Requires web access for research + optional Salesforce logging; can be run without scripts.
metadata:
  author: evalops
  version: "0.1"
---
# Dealflow: sourcing to memo

## When to use
Use this compound skill when you need to simulate a full associate workflow:
- Build a sector view and generate targets
- Source and qualify companies
- Move a specific deal from first meeting to memo/IC
- Keep Salesforce current so the team can route work

## Inputs you should request (only if missing)
- Thesis area (or a company to start from)
- Stage focus and decision timeline
- CRM conventions (Salesforce stages/fields) if known

## Outputs you must produce
- Market map + top targets (if starting from sector)
- Qualified pipeline list (10 new names / week)
- Meeting notes + next steps for each meeting
- Ranked diligence plan + evidence
- Investment memo

## Workflow (default)

### Phase 0: Set thesis (1–3 hours)
1) Define wedge + buyer + why now
2) Build taxonomy and initial market map (50–150 companies)
3) Force-rank top 25 targets
4) Create a weekly sourcing plan

Log: create Campaign `Thesis: <topic> (YYYY-MM)` (optional)

### Phase 1: Source (weekly loop)
1) Loop A: earned network touches (Top 50 humans)
2) Loop B: signal harvest → candidate list
3) Loop C: thesis-driven outreach

Deliverable: weekly pipeline update with 10 new names.

Log: create/update Leads/Accounts + next-step Tasks

### Phase 2: First meeting → decision
For each qualified company:
1) Write meeting brief (kill questions + wedge hypothesis)
2) Run the meeting with structure and note-taking rules
3) Same-day follow-up (value + next steps)

Decision: advance to diligence or pass with reasons.

Log: Event + Notes + Opportunity stage update

### Phase 3: Diligence sprint (3–10 days)
1) Build ranked risk register (top 3–5)
2) Define fastest tests
3) Run customer/product/GTM/team/competitive diligence
4) Produce evidence pack

Log: Tasks per workstream + Activity logs for calls

### Phase 4: Memo
1) Draft memo with clear recommendation
2) Include best argument against
3) Identify what terms would change decision
4) Set IC decision date

Log: attach memo to Opportunity + update stage

## Guardrails
- Do not “diligence everything.” Diligence the top risks.
- Always write “must be true” claims early; update with evidence.
- Treat Salesforce as the source of truth for routing and accountability.

## References
Use atomic skills as needed:
- thesis-market-mapping
- signal-sourcing-engine
- founder-meeting-runbook
- diligence-risk-burndown
- investment-memo-writing
- salesforce-crm-ops
