---
name: judgment-postmortem-calibration
description: "Build VC judgment faster through structured postmortems: log initial takes, update beliefs with evidence, and review outcomes to refine heuristics. Use after decisions, passes, and major diligence sprints."
license: Proprietary
compatibility: Works offline; improved with longitudinal tracking; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.2"
---
# Judgment postmortem calibration

## When to use
Use this skill when you want to:
- Improve selection judgment (faster learning, fewer repeated mistakes)
- Capture why you said yes/no and how evidence changed your view
- Build an internal "decision log" that compounds
- Review investments or passes after outcomes are known

**Trigger points:**
- After every IC decision (invest or pass)
- After every competitive loss
- Quarterly: review passes that raised from others
- Annually: review portfolio outcomes vs initial thesis

## Inputs you should request (only if missing)
- Deal name + date of first meeting
- Your initial take (reconstruct honestly if not documented)
- Outcome to date (funded by others? traction? pivot? shut down?)
- Original memo or notes (if available)

## Outputs you must produce
1) **Decision log entry** (structured, one page)
2) **Calibration scorecard** (initial beliefs vs reality)
3) **Updated heuristics** (2-5 actionable bullets)
4) **Pattern library update** (what archetype was this?)
5) **Follow-up list** (who to ping, what to track)

Templates:
- assets/decision-log.md
- assets/decision-log.csv (for longitudinal tracking)

## Core principle: Be honest about what you believed

The value of postmortems comes from honest reconstruction of your initial beliefs, not retroactive rationalization. Write down what you *actually* thought at the time, even if it's embarrassing in hindsight.

## Procedure

### 1) Capture the timeline
| Date | Event | Your belief at the time |
|---|---|---|
| First meeting | | |
| Diligence start | | |
| Key call/evidence | | |
| Decision date | | |
| Outcome observed | | |

Key turning points: document "what changed my mind" at each stage.

### 2) Record the initial thesis (be honest)
**At first meeting, I believed:**
- What would make the company win:
- The top risk I was most worried about:
- What evidence I had at the time:
- My confidence level (1-10):
- My recommendation:

**At decision point, I believed:**
- What would make the company win:
- Top risks (ranked):
- Evidence collected:
- Confidence level (1-10):
- Final recommendation:

### 3) Document the decision and rationale
- **Decision:** Invest / Pass / Lost competitive
- **Stated rationale (at the time):**
- **Unstated factors (be honest):**

### 4) Compare to reality (calibration)

**Which predictions were correct?**
| Belief | Correct? | Evidence |
|---|---|---|
| Market thesis | | |
| Product thesis | | |
| Team thesis | | |
| GTM thesis | | |
| Risk #1 | | |
| Risk #2 | | |

**What surprised you?**
- What happened that you didn't predict?
- What didn't happen that you expected?

**Calibration score:**
- Beliefs that were correct: X / Y
- Risks that materialized: X / Y
- Risks that were irrelevant: X / Y

### 5) Identify what you underweighted or overweighted

**Common underweights:**
- Team learning rate (often matters more than initial skill)
- Distribution advantages (often matters more than product)
- Timing (often matters more than execution)
- Founder-market fit (often matters more than pedigree)

**Common overweights:**
- Technical moat (often less durable than assumed)
- TAM calculations (often less meaningful than wedge)
- Competitive dynamics (often less predictive than customer pull)

**For this deal, I underweighted:**
- 

**For this deal, I overweighted:**
- 

### 6) Extract heuristics (portable rules)

Good heuristics are:
- Specific enough to act on
- Falsifiable
- Tied to observed evidence

**Bad heuristic:** "Founders matter."
**Good heuristic:** "When a founder can't name a specific buyer trigger event, seed enterprise sales is usually premature."

**Bad heuristic:** "Be careful with competitive markets."
**Good heuristic:** "If the top 3 competitors all raised >$20m in the last 12 months and none has clear product differentiation, pass unless founder has a distribution wedge."

Write 2-5 heuristics from this postmortem:
1. 
2. 
3. 

### 7) Update your pattern library

**Archetype matching:**
- What archetype did this company fit? (e.g., "first-time founder in crowded market", "second-time founder with distribution", "technical founder without GTM")
- How did this archetype typically perform in your portfolio?
- Should you update your priors on this archetype?

**Pattern update:**
- If this is a new pattern, document it
- If this matches an existing pattern, update the success rate

### 8) Create follow-up list

For every postmortem, create a small follow-up list:
| What to track | Signal | Recheck date |
|---|---|---|
| | | |
| | | |
| | | |

| Who to keep warm | Why | Next touch |
|---|---|---|
| | | |
| | | |

## Quarterly review: Passes that raised

Review all passes from the quarter where the company subsequently raised:
- Who raised from whom?
- At what terms?
- Were our reasons for passing validated or invalidated?
- What would we do differently?

## Annual review: Portfolio outcomes vs initial thesis

For each portfolio company:
- What did we believe at investment?
- What's the current reality?
- Where were we right/wrong?
- What should we have asked that we didn't?

## Salesforce logging (optional)
If Salesforce is your system of record, link the postmortem to the Opportunity:
- Add a Note titled "Postmortem (YYYY-MM-DD)"
- Update pass reasons / outcome fields if your org uses them
- Tag with heuristics extracted (if you have a tagging system)

## Edge cases
- If you have no outcome yet: run a "process postmortem" focused on what you learned and what evidence was missing.
- If the outcome is ambiguous: document what you'd need to see to call it a success or failure.
- If you can't remember your initial thesis: reconstruct as honestly as possible, and start documenting initial beliefs for future deals.
