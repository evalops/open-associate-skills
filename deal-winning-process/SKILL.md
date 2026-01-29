---
name: deal-winning-process
description: Increase win-rate in competitive rounds: run a clean process, deliver value previews, coordinate partners, and manage timelines without posturing. Use when you’re trying to win a deal.
license: Proprietary
compatibility: Works offline; improved with warm intros and web research; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Deal winning process

## When to use
Use this skill when:
- The company is a “must win” or competitive deal
- You need to help the partner close with founder trust + speed
- You need a structured win plan (value + process + narrative)

## Inputs you should request (only if missing)
- Who else is in the round (competitors, likely lead)
- Founder priorities (price vs partner vs speed vs brand)
- Your firm’s intended role (lead/follow) and constraints
- Timeline (term sheet date, decision date)

## Outputs you must produce
1) **Win plan** (one page)  
2) **Value preview list** (1–3 concrete actions you can do fast)  
3) **Process plan** (meetings + diligence + decision date)  
4) **Founder narrative** (why your firm, in their language)

Templates:
- assets/win-plan.md
- assets/value-preview.md

## Procedure

### 1) Identify the founder’s decision criteria
Ask directly:
- What does a great partner do for you in the next 6–12 months?
- What are you optimizing for in this round (speed, price, control, help)?
- What would make you *not* choose us?

Write the criteria down. Don’t guess.

### 2) Build a one-page win plan
Include:
- Why us (2 bullets)
- What we will do in the next 7 days (specific)
- Who at the firm is involved (right people, not a parade)
- Timeline with dates
- Risks the founder is worried about + how you address them

### 3) Do value previews early (before asking to win)
High-signal previews:
- Customer intro to a real buyer (not “advice”)
- Recruiting assist on a critical role (shortlist + outreach help)
- Operator call that validates a key risk (and shares learnings)

Rules:
- Make offers you can fulfill quickly.
- Close the loop: “Did that help? What else is blocking?”

### 4) Run a clean process
- Send agendas.
- Consolidate diligence asks.
- Keep partner time high-quality: pre-wire internally; no surprises.
- Don’t posture about leading if you aren’t.

### 5) Handle terms responsibly
- Be explicit about what you can offer and what you can’t.
- If you’re using time pressure, ensure it’s real; fake deadlines destroy trust.

## Salesforce logging (recommended)
- Update Opportunity with competitor set + probability (if you track).
- Log value-preview actions as Activities.
- Track next step and owner per action (Tasks with due dates).

Use `salesforce-crm-ops` for API patterns.

## References
- Feld/Mendelson public writing is useful for what terms matter and how to keep terms “simple.”
- Mark Suster is useful for fundraising dynamics and board mechanics.

## Edge cases
- If another firm is leading: your job is to be the best co-investor and prove it with concrete help.
- If the founder is optimizing for brand: your best lever is credible operator help + partner fit, not hype.
