---
name: portfolio-support-ops
description: Run portfolio support like an on-call ops function: intake requests, ship intros, recruiting help, board prep, and close-the-loop tracking. Use after investment or when supporting a portfolio CEO.
license: Proprietary
compatibility: Works offline; improved with a strong operator network; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Portfolio support ops

## When to use
Use this skill when:
- A portfolio company asks for help (hiring, customers, partners, strategy)
- You’re prepping for a board meeting or quarterly check-in
- You want to systematize support so it compounds over time

## Inputs you should request (only if missing)
- The specific request (what outcome, by when)
- Company stage and immediate priorities
- Target ICP / customer list (if request is GTM)
- Hiring priorities and role specs (if request is recruiting)
- Any constraints (confidentiality, competitor conflicts)

## Outputs you must produce
1) **Clarified request** (what “done” means)  
2) **Action plan** (owners, next steps, due dates)  
3) **Delivered help** (intros, candidates, docs)  
4) **Close-the-loop note** (did it work?)

Templates:
- assets/help-menu.md
- assets/request-intake.md
- assets/intro-template.md
- assets/board-prep.md

## Procedure

### 1) Build a “help menu” per company
Maintain a short doc per portfolio company:
- Top 3 priorities this quarter
- Hiring: roles + ideal profiles
- GTM: target accounts + buyer personas
- Partnerships: who they want in their ecosystem
- Metrics they care about + current baselines

### 2) Intake requests like a helpdesk
For every request, write:
- Goal (single sentence)
- Deadline
- Best lever (intro, candidate, analysis, fundraising, etc.)
- Owner
- Next step (with date)

### 3) Standardize intros
A high-quality intro includes:
- Why the match is relevant now
- What the ask is (15-min chat, design partner, hire, etc.)
- A suggested time window

### 4) Recruiting support (associate-level)
- Confirm role scorecard (must-have vs nice-to-have)
- Produce 10–20 candidate targets (companies + titles)
- Outreach help (warm paths first)
- Track pipeline weekly (introduced → responded → screened → interviewed)

### 5) Board meeting support
Before the meeting:
- Pre-read the deck and pull 5 questions that matter
- Prepare a short competitive/market update (1 page)
After the meeting:
- Capture action items and chase closure

## Salesforce logging (optional)
Many firms track portfolio support in Salesforce via Activities on the Account.

Minimum:
- Log each support action as an Activity
- Tag it: hiring / customer / strategy / fundraising
- Record outcome in the notes

If you need API workflows, use `salesforce-crm-ops`.

## References
- Mark Suster has useful public writing on boards and how they function in practice.

## Edge cases
- If the ask is vague: ask “What does success look like next week?” and proceed.
- If you can’t help quickly: provide an alternative (another operator, another firm, or a small experiment).
