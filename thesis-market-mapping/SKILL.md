---
name: thesis-market-mapping
description: "Build and maintain a thesis-driven market map and roadmap: segment taxonomy, company list, wedge hypotheses, and 'must be true' claims. Use when exploring a new sector, refreshing coverage, or generating high-conviction sourcing targets."
license: Proprietary
compatibility: Requires web access for research; optional Salesforce logging via REST API.
metadata:
  author: evalops
  version: "0.1"
---
# Thesis market mapping

## When to use
Use this skill when you need to:
- Build an internal point of view on a sector (new thesis or coverage refresh)
- Produce a *market map* (companies + segmentation) that drives sourcing and diligence
- Turn “interesting” into “actionable” (who to meet, what to ignore, what to bet)

## Inputs you should request (only if missing)
- Sector / theme and a *tight wedge* to start with (e.g., “AI eval tooling for regulated industries”)
- Stage focus (pre-seed/seed/A/B+) and check size range
- Any existing notes, prior memos, or firm theses
- Time horizon (what “now” means: 6, 12, 24 months)

## Outputs you must produce
1) **Market map table** (CSV/Sheet-style)  
2) **Thesis one-pager** (max ~1 page) with falsifiable claims  
3) **Top targets list** (top 25 companies + top 50 people)  
4) **Sourcing routing** (who internally should see what, and why)

Recommended templates:
- assets/market-map.csv
- assets/thesis-one-pager.md
- assets/top-targets.md

## Procedure

### 1) Set the aperture (do this first)
Write a 3–5 line problem statement:
- Who is the buyer?
- What job are they trying to get done?
- What is broken about the current workflow?
- What changed that makes a new approach possible now?

Then define the wedge:
- Narrow enough that you can know it better than the internet in 30–60 days.
- Broad enough that it can expand to a big market if you’re right.

### 2) Create a segmentation taxonomy (avoid “misc”)
Create categories that reflect **how buyers buy**, not just product features.
Use 5–9 primary segments max. For each segment, add:
- ICP / buyer role
- Budget source (security, IT, product, compliance, etc.)
- Adoption trigger event (regulatory change, platform shift, cost curve, breach, etc.)
- “Why now” drivers

### 3) Populate the market map (treat it like a database)
Fill the table with:
- Company / product
- Wedge + ICP
- Pricing / GTM motion (PLG, sales-led, channel, services-assisted, etc.)
- Proof of pull (referenceable customers, OSS adoption, hiring, usage signals)
- Differentiation (one sentence)
- Switching costs / moat hypothesis
- Notable risks (one sentence)
- Investors / financing (if known)
- Status (meet / watch / pass)

Rules:
- Keep entries short; you’re optimizing for scan speed.
- Record *unknowns* explicitly; don’t guess.

### 4) Force-rank and write “must be true” claims
Pick the **top 10** companies that matter and write:
- “This becomes huge if ______ is true.”
- Evidence you have **today** (links, conversations, data)
- What would falsify it (what you’d need to see to stop believing)

Then write 3–7 “must be true” claims for the thesis overall, such as:
- Buyer behavior (“CISO will fund this from X budget because…”)
- Distribution (“This category will be won by teams with…”)
- Product leverage (“Model improvements reduce cost by…”)

### 5) Identify archetypes and failure modes
For each segment, list the 2–4 most common failure modes:
- “Nice-to-have” that dies in procurement
- High integration cost with unclear ROI
- Incumbent bundles it “good enough”
- Founder misunderstands buyer / cycle time

This becomes your future screening rubric.

### 6) Convert the map into a sourcing plan
Create a weekly plan:
- 10 “new names” to investigate
- 5 outreach targets
- 3 operator calls (buyer-side truth)
- 1 deep dive (new sub-segment)

Deliverable: a 10-bullet “what changed this week” update.

## Salesforce logging (optional but recommended)
If Salesforce is the system of record, log the map so the firm can route and measure work.

**Option A (simple):**  
- Create a Salesforce **Campaign** called `Thesis: <topic> (YYYY-MM)` and add target companies/people as Campaign Members.

**Option B (low-dependency):**  
- Create/update **Leads** for founder contacts and **Accounts** for companies.
- Store `Thesis=<topic>` in a tagging field if you have one; otherwise prepend it to Description.

If you need API workflows, use the `salesforce-crm-ops` skill.

## Examples
- Input: “Map the AI code review / AI SDLC tooling market for seed deals.”
- Output: market-map.csv with 120 companies, taxonomy, top 25 targets, 5 falsifiable claims, weekly sourcing plan.

## Edge cases
- If the wedge is too broad: propose 2 narrower wedges and proceed with the one that has the clearest buyer + budget.
- If you can’t find buyers: switch to operator calls (the map is empty without buyer truth).
