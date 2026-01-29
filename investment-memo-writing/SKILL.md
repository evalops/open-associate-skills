---
name: investment-memo-writing
description: Write an investment memo that forces a decision: explicit recommendation, must-be-true claims, evidence, risks, and next steps. Use when preparing for IC or partner discussion.
license: Proprietary
compatibility: Works offline; improved with web comps and diligence evidence; optional Salesforce logging.
metadata:
  author: evalops
  version: "0.1"
---
# Investment memo writing

## When to use
Use this skill when:
- You need to brief partners / IC with a decision-ready document
- You have diligence evidence and need to turn it into a recommendation
- You want to reduce “vibes” and increase clarity

## Inputs you should request (only if missing)
- Company deck + diligence notes
- Round terms (or what’s known so far)
- Firm constraints (ownership target, stage, geography)
- Comparable comps / pricing benchmarks if available

## Output you must produce
A memo that:
- makes a clear recommendation (lead/follow/pass)
- states 3–7 falsifiable “must be true” claims
- names top risks (ranked) and evidence for each
- proposes decision + next steps with dates

Templates:
- assets/memo-template.md
- assets/outcome-framing.md

## Writing rules
- Adjectives are a tax. Replace them with evidence.
- Put the best argument *against* the deal in the memo.
- If it’s important, quantify it or show a proxy.
- Keep TL;DR to 5 bullets max.

## Memo structure (recommended)
1) Recommendation (1 sentence)
2) TL;DR (5 bullets)
3) Why now + wedge
4) Market (buyer, budget, trigger, adoption timing)
5) Product (10x, hard to copy, deployment reality)
6) Traction (the 2–3 metrics that matter)
7) GTM (motion, cycle time, pricing, margin)
8) Competition + moat
9) Team (learning rate, decision rights, gaps)
10) Risks (ranked) + evidence + mitigation
11) Deal + terms + ownership target
12) Next steps + decision date
Appendix: diligence notes, call quotes, data

## Salesforce logging (recommended)
- Attach the memo as a File/Note to the Opportunity.
- Update Opportunity fields: stage, amount (if relevant), close date, next step.
- Record key “must be true” claims in a structured field if you have one; otherwise in Notes.

Use `salesforce-crm-ops` if you need API patterns.

## Edge cases
- If terms are unknown: write the memo “pending terms” and explicitly state what term ranges would change your recommendation.
- If evidence is thin: say so. Propose the smallest next diligence step that would change the decision.
