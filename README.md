# VC Associate Agent Skills Pack (v0.3)

This is a skills bundle for simulating a top-decile venture associate. The skills are designed to force concrete outputs, not just checklists. Every skill answers:

- "Is this worth partner attention?"
- "What must be true?"
- "What's the fastest way to falsify it?"
- "What concrete artifact moves this forward today?"

## Core principles

1. **Force-ranked outputs** - Top 10 companies, top 4 risks, top 3 next steps. No sprawling lists.
2. **Must-be-true + fastest falsification test** - Every thesis, every diligence, every sourcing decision.
3. **Salesforce as mandatory gate** - No "qualified" company exists without a record + next task + owner.
4. **Steelman the bear case** - Every memo includes the best argument against.
5. **Time-boxed workflows with gates** - Kill, continue, or escalate. No deals in limbo.
6. **Measure your judgment** - Brier scores, calibration tracking, learning rate over time.

## Skills included

### Atomic skills (individual capabilities)

| Skill | Description |
|---|---|
| `thesis-market-mapping/` | Build market maps with force-ranked top 10, kill criteria, contrarian hypotheses |
| `signal-sourcing-engine/` | Sourcing loops as first-class objects with cadence metrics (10/3/1 weekly) |
| `founder-meeting-runbook/` | Meeting prep, structure, notes, and follow-up within 2 hours |
| `diligence-risk-burndown/` | Max 4 risks, fastest tests, anti-confirmation evidence required |
| `investment-memo-writing/` | First-line recommendation, steelman against, decision log |
| `deal-winning-process/` | Competitive round closing with value previews and daily action plans |
| `term-sheet-triage/` | Waterfall modeling, multi-investor stacks, participation caps |
| `judgment-postmortem-calibration/` | Brier scores, calibration curves, learning rate measurement |
| `saas-metrics-diligence/` | SaaS-specific metrics validation |
| `portfolio-support-ops/` | Portfolio support with SLAs, outcome tracking, and impact measurement |
| `salesforce-crm-ops/` | CRM operations with field mapping, dry-run mode, schema discovery |

### Compound skills (full workflows)

| Skill | Description |
|---|---|
| `dealflow-sourcing-to-memo/` | End-to-end 3/5/10-day sprints with gates at each phase |
| `diligence-sprint/` | Time-boxed diligence with daily deliverables and kill gates |
| `portfolio-helpdesk-sprint/` | Time-boxed portfolio support with triage, SLAs, and metrics |

## What's new in v0.3

**Salesforce scripts now production-ready:**
- `sf_upsert_lead.py` - Dry-run mode, config-based field mapping, external ID upsert, custom VC fields
- `sf_create_opportunity.py` - Stage mapping, VC fields (pass reason, what-would-change)
- `sf_create_task.py` - Full config support
- `sf_describe.py` - Schema discovery for any org
- Config templates in `salesforce-crm-ops/config/`

**Portfolio skills now have same rigor as dealflow:**
- SLAs by request type (P0/P1/P2)
- Outcome measurement (success rate, impact rating)
- Help menu templates per company
- Sprint structure with daily gates

**Judgment calibration now quantified:**
- Brier score calculation for prediction accuracy
- Calibration curves (predicted % vs actual %)
- Learning rate tracking over quarters
- Archetype performance base rates
- Heuristics with attached probabilities

**Term sheet analysis now handles complexity:**
- Multi-investor liquidation stack modeling
- Full waterfall calculations at multiple exit values
- Participation cap analysis
- Side letter review checklist
- Competing term sheet comparison

## Quick start

1. Clone this repo
2. Point your agent at this directory
3. For Salesforce integration:
   ```bash
   # Discover your org's schema
   python3 salesforce-crm-ops/scripts/sf_describe.py Lead Account Opportunity Task
   
   # Edit config files for your org
   vim salesforce-crm-ops/config/field_map.yaml
   vim salesforce-crm-ops/config/stages.yaml
   
   # Always dry-run first
   python3 salesforce-crm-ops/scripts/sf_upsert_lead.py --dry-run \
     --email founder@example.com --first Ada --last Lovelace --company ExampleAI
   ```

## Validation

If you use the Agent Skills reference library:
```bash
skills-ref validate .
```

## Philosophy

Top associates don't just run checklists. They constantly answer:
- "Is this worth partner attention?"
- "What must be true?"
- "What's the fastest way to falsify it?"
- "What concrete artifact moves this forward today?"

These skills force those outputs. No wandering. No "watching" without a recheck date. Every workflow ends with a clear decision.

**And top associates measure their judgment.** They track predictions, score them against outcomes, and improve their calibration over time. The judgment-postmortem skill now includes Brier scores and learning rate tracking so you can quantify whether you're getting better at picking.
