---
name: portfolio-helpdesk-sprint
description: "Run a lightweight portfolio helpdesk: intake, triage, execute, and close-the-loop with tracking. Use when multiple portfolio support requests come in and you need repeatable execution."
license: Proprietary
compatibility: Works offline; improved with operator network; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Portfolio helpdesk sprint

## When to use
Use this skill when:
- Portfolio support requests are coming in continuously
- You need a triage system and SLA-like execution
- You want to measure whether support actually helped

## Inputs you should request (only if missing)
- Request details (outcome + deadline)
- Company context (stage, ICP, priorities)
- Any sensitive constraints (conflicts, confidentiality)

## Outputs you must produce
- A prioritized queue (P0/P1/P2)
- An action plan per request (owner, next step, due date)
- Delivered help + outcome notes
- Updated help menu per company

## Triage rubric
- P0: urgent (fundraising, key hire closing, major customer escalation)
- P1: important (hiring pipeline, customer intros, partner intro)
- P2: useful (market intel, light strategy review)

## Workflow
1) Intake → clarify “done” → assign priority
2) Execute value actions fast (intros, candidate lists, analysis)
3) Close loop: “Did this help? What’s next?”
4) Update the company’s help menu so future requests are easier

## Salesforce logging (optional)
- Log support actions as Activities on the Account
- Tag by support type
- Record outcome

## Reference
Use `portfolio-support-ops` for deeper playbooks and templates.
