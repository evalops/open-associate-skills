---
name: founder-meeting-runbook
description: "Run high-signal founder meetings: prep, structure the conversation, capture decision-relevant notes, and send crisp follow-ups. Use when taking first meetings, doing partner prep, or screening deals."
license: Proprietary
compatibility: Works offline; improved with web access; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Founder meeting runbook

## When to use
Use this skill for:
- First meetings / second meetings with founders
- Prepping a partner for a meeting
- Turning a conversation into a clear “next step” (diligence or pass)

## Inputs you should request (only if missing)
- Company deck / website / demo link (if available)
- Stage and what the founder is raising
- Your firm’s investment criteria (check size, ownership, etc.)
- Any prior interactions (intro path, prior passes)

## Outputs you must produce
1) **Meeting brief** (5 bullets) before the call  
2) **Meeting notes** (decision-oriented) within 2 hours  
3) **Follow-up email** (value + next steps) same day  
4) **Pass note** (if passing) that is direct and helpful

Templates:
- assets/meeting-brief.md
- assets/meeting-notes.md
- assets/follow-up-email.md
- assets/pass-note.md

## Procedure

### 1) Pre-meeting prep (15–25 minutes)
Do:
- Read everything public (site, docs, pricing, 2–3 customer quotes if possible).
- Write 5 questions you truly don’t know.
- Identify 2–3 “kill questions” (if answered badly, likely a pass).
- Identify the wedge hypothesis: “Why might this be 10x?”

Avoid:
- Writing a long summary nobody uses.
- Asking questions the deck already answers unless you are testing honesty.

### 2) Meeting structure (keep time)
Use a simple structure:
1) Founder story + why this problem (5 min)
2) Product + why now (10 min)
3) Buyer + GTM motion (10 min)
4) Traction + retention + cycle time reality (10 min)
5) Risks / unknowns (5 min)
6) Next steps (2 min)

### 3) High-signal questions (pick 8–12)
#### Buyer / pain
- Who is the buyer with budget authority?
- What is the trigger event that causes purchase now?
- What are they doing today instead?
- What is the “do nothing” competitor?

#### GTM
- How do the first 10 customers find you?
- What is the sales cycle length and who blocks it?
- What is the onboarding path and time-to-value?

#### Traction / truth
- What’s the best evidence this is repeatable?
- What’s the hardest churn story you’ve had?
- What surprised you since launch?

#### Team / learning rate
- Tell me about a major internal disagreement and how you resolved it.
- What do you believe that most people in the space disagree with?

### 4) Note-taking rules (decision oriented)
Your notes must include:
- “What must be true” (3 bullets)
- Strengths (3 bullets)
- Risks (3 bullets, ranked)
- Next diligence step (1–3 bullets with owners)

### 5) Follow-up (same day)
Send:
- A crisp recap of what you heard (so they can correct it)
- 1–2 intros you can actually make (customers/operators/candidates)
- The diligence items needed next (explicit, not a long list)
- A proposed timeline for next steps

### 6) Passing well
If passing:
- Be direct (“we’re going to pass”)
- Name 1–2 concrete reasons (avoid “not a fit”)
- Offer 1 suggestion (ICP change, wedge, metric, etc.)

## Salesforce logging (recommended)
- Log the meeting as an **Event** (or Activity) with notes.
- Update the **Opportunity** stage (e.g., “First meeting,” “Diligence,” “Pass”).
- Create a **Task** for the next step with a due date.

Use `salesforce-crm-ops` if you need API-level logging.

## References to keep you sharp
- Paul Graham essays for founder patterns and early-stage behavior (e.g., “Do Things That Don't Scale”).
- Mark Suster’s writing for board and fundraising dynamics.

(These are reading aids, not a substitute for evidence from the company.)

## Edge cases
- If the founder is evasive: ask for specifics (numbers, names, timelines). If still evasive, treat as a red flag.
- If you’re missing data: propose the smallest next step that would resolve the top risk.
