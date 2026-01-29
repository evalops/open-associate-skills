---
name: judgment-postmortem-calibration
description: "Build VC judgment faster through structured postmortems: log initial takes, update beliefs with evidence, and review outcomes to refine heuristics. Use after decisions, passes, and major diligence sprints."
license: Proprietary
compatibility: Works offline; improved with longitudinal tracking; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Judgment postmortem calibration

## When to use
Use this skill when you want to:
- Improve selection judgment (faster learning, fewer repeated mistakes)
- Capture why you said yes/no and how evidence changed your view
- Build an internal “decision log” that compounds

## Inputs you should request (only if missing)
- Deal name + date of first meeting
- Your initial take (if you have it) or reconstruct it honestly
- Outcome to date (funded by others? traction? pivot? shut down?)

## Outputs you must produce
1) **Decision log entry** (one page)  
2) **Updated heuristics** (2–5 bullets)  
3) **Follow-up list** (who to ping, what to track)

Templates:
- assets/decision-log.md
- assets/decision-log.csv

## Procedure

### 1) Capture the timeline
- Date of first meeting
- Diligence actions taken
- Decision date (advance/pass/invest)
- Key turning points (“what changed my mind?”)

### 2) Record the initial thesis (be honest)
Write:
- What you believed would make the company win
- The top risk you were most worried about
- What evidence you had at the time

### 3) Compare to reality (as of today)
Answer:
- Which risks materialized?
- Which risks were irrelevant?
- What did you underweight (team, distribution, cycle time, pricing, etc.)?
- What would you do differently next time?

### 4) Extract heuristics (portable rules)
Heuristics should be:
- specific enough to act on
- falsifiable
- tied to observed evidence

Bad heuristic: “Founders matter.”
Good heuristic: “When a founder can’t name a specific buyer trigger event, seed enterprise sales is usually premature.”

### 5) Decide what to track
For every pass/invest, create a small follow-up list:
- 3 signals to watch (product, GTM, hiring, retention)
- 2 people to keep warm (founder, operator, angel)

## Salesforce logging (optional)
If Salesforce is your system of record, link the postmortem to the Opportunity:
- Add a Note titled “Postmortem (YYYY-MM-DD)”
- Update reason codes / pass reasons if your org uses them

## Edge cases
- If you have no outcome yet: run a “process postmortem” focused on what you learned and what evidence was missing.
