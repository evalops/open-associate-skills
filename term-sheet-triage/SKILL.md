---
name: term-sheet-triage
description: "Analyze and summarize venture financing terms: economics, control, and 'gotchas' with clear implications. Use when reviewing term sheets, SAFEs/notes, side letters, or board/control terms. Fast triage for deal decisions."
license: Proprietary
compatibility: Requires reading term sheet text; optional cap table math; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.2"
---
# Term sheet triage

## When to use
Use this skill when you need to:
- Review a term sheet quickly and identify what matters (< 30 minutes)
- Explain term implications in plain language to partners
- Prepare negotiation positions or highlight risk terms
- Compare two competing term sheets
- Advise founders on incoming terms (from investor or founder side)

## Inputs you should request (only if missing)
- The term sheet text (or key terms if redacted)
- Current cap table summary (pre-round)
- Round size and price (or cap/discount if SAFE/note)
- Desired ownership / board goals (if investor-side)
- Founder goals / constraints (if advising founder)

## Outputs you must produce
1) **One-line summary** (economics in one sentence)
2) **One-page term summary** (economics + control + unusual terms)
3) **Red flags list** (ranked, max 5)
4) **Negotiation levers** (what to push, what to accept, difficulty rating)
5) **Scenario table** (who gets paid in outcomes: 1x, 3x, 10x)

Templates:
- assets/term-sheet-checklist.md
- assets/scenario-table.md

## Procedure

### 1) One-line economics summary (do this first)
Write one sentence: "$Xm at $Ym pre ($Zm post), Z% ownership to new investors, with [standard/non-standard] prefs."

Examples:
- "$3m at $12m pre ($15m post), 20% to Series A, 1x non-participating"
- "$500k SAFE at $8m cap, ~5.9% assuming conversion at cap"

### 2) Classify the instrument
- Priced equity round (Series Seed, A, B, etc.)
- SAFE (post-money or pre-money cap)
- Convertible note
- Other (revenue-based, etc.)

### 3) Extract the economics that matter

**For priced rounds:**
| Term | Value | Standard? | Impact |
|---|---|---|---|
| Pre-money | | | |
| Post-money | | | |
| New investor ownership | | | |
| Option pool (pre/post) | | | |
| Liquidation preference | | 1x non-participating | |
| Participation | | None | |
| Anti-dilution | | Broad-based weighted avg | |
| Pro-rata rights | | | |
| Pay-to-play | | None | |

**For SAFEs/notes:**
| Term | Value | Standard? | Impact |
|---|---|---|---|
| Cap | | | |
| Discount | | | |
| MFN | | | |
| Interest rate (notes) | | | |
| Maturity (notes) | | | |
| Conversion trigger | | | |

### 4) Extract control terms
| Term | Provision | Standard? | What it blocks |
|---|---|---|---|
| Board composition | | | |
| Board observer | | | |
| Protective provisions | | | |
| Information rights | | | |
| Drag-along | | | |
| Founder vesting | | | |
| Voting agreement | | | |

### 5) Identify red flags (max 5, ranked)

Common gotchas to flag:
| Red flag | Why it matters | How bad (1-5) |
|---|---|---|
| Participating preferred | Double dip on exit | 4-5 |
| >1x liquidation preference | Blocks smaller exits | 5 |
| Full ratchet anti-dilution | Punitive in down round | 4 |
| Overly broad protective provisions | Investor can block normal operations | 3-4 |
| Redemption rights | Forces liquidity event | 3-4 |
| Founder vesting reset without rationale | Demotivates founders | 3 |
| Pay-to-play with harsh penalties | Can wipe out early investors | 3 |
| Side letters with extra rights | Creates investor conflicts | 2-3 |
| Super pro-rata | Squeezes out other investors | 2-3 |
| Aggressive option pool sizing | Dilutes founders pre-money | 2-3 |

### 6) Build scenario table (who gets paid)

| Scenario | Exit value | Founders | Seed | Series A | Notes |
|---|---|---|---|---|---|
| Acqui-hire | $5m | | | | |
| Modest exit | $30m | | | | |
| Good exit | $100m | | | | |
| Great exit | $500m | | | | |

Show both $ amounts and % of total. This reveals whether prefs actually matter.

### 7) Draft negotiation positions

For each non-standard term:
| Term | Current | Ask | Difficulty | Rationale |
|---|---|---|---|---|
| | | | Easy/Med/Hard | |

**Negotiation difficulty guide:**
- Easy: Standard market term, any reasonable investor will accept
- Medium: Investor will push back but may concede
- Hard: Material to investor's model, expect trade-offs

### 8) Summary recommendation

One paragraph:
- Is this a fair deal?
- What are the 1-2 terms worth negotiating?
- What should be accepted as-is?
- Any deal-breakers?

## Public references (useful mental models)
- Brad Feld & Jason Mendelson's public term sheet series / Venture Deals materials (great for understanding which terms matter in practice).
- Mark Suster's writing on convertible debt and fundraising dynamics.

These are references for concepts; always anchor the decision on the actual term sheet text.

## Salesforce logging (optional)
- Attach the term sheet as a File to the Opportunity.
- Create a Note: "Term summary: [one-line summary] | Red flags: [list]"
- Update Opportunity stage to "Term Sheet" and set decision date.

## Edge cases
- If terms are incomplete: list missing terms and explain what each missing term could change.
- If there are side letters: treat them as first-class; they often contain the sharp edges. Flag any side letter provisions that differ from the main terms.
- If comparing two term sheets: create a side-by-side comparison table and highlight where they differ.
