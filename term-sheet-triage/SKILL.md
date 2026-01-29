---
name: term-sheet-triage
description: Analyze and summarize venture financing terms: economics, control, and 'gotchas' with clear implications for founders and investors. Use when reviewing term sheets, SAFEs/notes, side letters, or board/control terms.
license: Proprietary
compatibility: Requires reading term sheet text; optional cap table math; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Term sheet triage

## When to use
Use this skill when you need to:
- Review a term sheet quickly and identify what matters
- Explain term implications in plain language
- Prepare negotiation positions or highlight risk terms
- Compare two competing term sheets

## Inputs you should request (only if missing)
- The term sheet text (or key terms if redacted)
- Current cap table summary (pre-round)
- Round size and price (or cap/discount if SAFE/note)
- Desired ownership / board goals (if investor-side)

## Outputs you must produce
1) **One-page term summary** (economics + control + unusual terms)  
2) **Red flags list** (ranked)  
3) **Negotiation levers** (what to push, what to accept)  
4) **Scenario table** (who gets paid in outcomes, if liquidation prefs matter)

Templates:
- assets/term-sheet-checklist.md
- assets/scenario-table.md

## Procedure

### 1) Classify the instrument
- Priced equity round
- SAFE
- Convertible note
- Other (revenue-based, etc.)

Then list the “things that actually change outcomes”:
- valuation / price (economic)
- liquidation preference / participation (economic)
- pro rata / follow-on rights (economic + optionality)
- board and protective provisions (control)
- option pool sizing and whether it’s pre/post (dilution)
- vesting and founder terms (incentives)

### 2) Read economics like an outcomes model
For priced rounds, compute:
- pre-money, post-money, ownership
- option pool impact
- liquidation preference stack and participation
- pro rata implications

For SAFEs/notes:
- cap definition (pre vs post, if specified)
- discount, MFN, interest (notes), maturity (notes)
- conversion mechanics in common scenarios

### 3) Read control terms like “who can block what”
Summarize:
- board composition and observer rights
- protective provisions (what requires investor consent)
- information rights and inspection rights
- drag-along and voting agreements

### 4) Identify “gotchas”
Common gotchas to flag explicitly:
- participating preferred (double dip)
- multiple liquidation preference
- overly broad protective provisions
- pay-to-play / punitive anti-dilution (rare but important)
- founder vesting resets without rationale
- redemption rights

### 5) Draft negotiation positions
For each flagged term:
- What it means
- Why it matters
- A reasonable alternative
- How hard to negotiate (easy/medium/hard)

## Public references (useful mental models)
- Brad Feld & Jason Mendelson’s public term sheet series / Venture Deals materials (great for understanding which terms matter in practice).
- Mark Suster’s writing on convertible debt and fundraising dynamics.

These are references for concepts; always anchor the decision on the actual term sheet text.

## Salesforce logging (optional)
- Attach the term sheet as a File to the Opportunity.
- Create a Note: “Term summary + red flags.”
- Update Opportunity stage to “Term Sheet” and set decision date.

## Edge cases
- If terms are incomplete: list missing terms and explain what each missing term could change.
- If there are side letters: treat them as first-class; they often contain the sharp edges.
