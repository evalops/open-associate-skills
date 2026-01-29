---
name: signal-sourcing-engine
description: "Run a systematic sourcing engine: network loops, signal harvesting, and thesis-driven outbound. Use when you need to generate proprietary dealflow, keep a pipeline current, or expand coverage."
license: Proprietary
compatibility: Requires web access for research and outreach; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Signal sourcing engine

## When to use
Use this skill when you need to:
- Generate new at-bats (companies and founders) in a specific thesis area
- Build a repeatable sourcing system (not ad hoc coffee chats)
- Turn weak signals into qualified founder meetings

## Inputs you should request (only if missing)
- Thesis wedge (or ask for a short description)
- Stage focus + geography constraints (if any)
- How the firm defines a “qualified” first meeting (traction, team, ICP, etc.)
- Existing CRM rules (Salesforce fields/stages) if available

## Outputs you must produce
1) **Sourcing channels plan** (3 loops)  
2) **Signal rubric** (what to watch + how to score)  
3) **Weekly pipeline update** (new names + next actions)  
4) **Outreach kit** (3 outreach templates + a call script)

Templates:
- assets/signal-rubric.md
- assets/outreach-templates.md
- assets/weekly-pipeline-update.md

## Procedure

### Loop A: Earned network loop (highest signal)
Goal: become “first call” for a cluster of builders and operators.

Steps:
1) Identify 2–3 “talent pools” for the wedge:
   - ex-employee clusters from relevant companies
   - OSS communities (maintainers + power users)
   - buyer/operator communities (CISOs, data eng leads, RevOps, etc.)
2) Build a “Top 50 humans” list and refresh weekly.
3) Provide small, concrete value before asking for meetings:
   - 1 targeted intro
   - a short market map excerpt
   - a recruiting assist on a specific role
4) Track compounding:
   - Touches → warm conversations → referrals → founder intros

### Loop B: Signal harvesting loop (volume, disciplined)
Goal: produce a weekly list of candidates worth human qualification.

Steps:
1) Define 8–12 signals tied to the wedge (avoid generic hype).
   Examples:
   - hiring for “founding AE” or “head of sales” (GTM transition)
   - design partners mentioned in job posts
   - OSS adoption with maintainer activity and downstream usage
   - specific buyer pain appearing in forums where buyers complain
2) Convert signals into candidate lists.
3) Human qualification pass:
   - 10 minutes scan → 50 names → 5 worth work → 1 worth meeting.
4) Log “why” for every pass to improve the rubric.

### Loop C: Thesis-driven outbound loop (precision outreach)
Goal: outreach that feels like “I did the work,” not spam.

Rules:
- Your message must include:
  1) the wedge you believe is emerging
  2) what looks distinct about their approach
  3) a concrete offer (customer intro, operator feedback, recruiting, etc.)
- If it could be sent to 20 companies with minimal edits, rewrite it.

## Qualification checklist (first pass)
A candidate is “qualified for a first meeting” if you can answer:
- Who buys? Who uses?
- What changes the buyer’s mind?
- What do they replace?
- What proof of pull exists (even weak)?
- What’s the likely wedge expansion path?

## Salesforce logging (recommended)
Log *every qualified company* and *every founder contact*.

Minimum viable objects:
- Lead (founder contact) and/or Account (company)
- Opportunity (potential investment)

Minimum fields to capture:
- Source (Loop A/B/C)
- Thesis tag / segment
- Next step + due date
- Status (meet / watch / pass)

Use `salesforce-crm-ops` for API logging patterns.

## Examples
- Input: “Source seed-stage AI security posture management.”
- Output: top 50 humans list, 10 new names this week, 5 outreach targets, 2 warm intros, and Salesforce entries with next steps.

## Edge cases
- If signals are noisy: tighten wedge and require buyer clarity before meetings.
- If outbound response is low: your offer is not concrete enough; fix the offer, not the subject line.
