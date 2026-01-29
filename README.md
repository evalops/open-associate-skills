# VC Associate Agent Skills Pack (v0.2)

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

## Skills included

### Atomic skills (individual capabilities)

| Skill | Description |
|---|---|
| `thesis-market-mapping/` | Build market maps with force-ranked top 10, kill criteria, contrarian hypotheses |
| `signal-sourcing-engine/` | Sourcing loops as first-class objects with cadence metrics (10/3/1 weekly) |
| `founder-meeting-runbook/` | Meeting prep, structure, notes, and follow-up within 2 hours |
| `diligence-risk-burndown/` | Max 4 risks, fastest tests, anti-confirmation evidence required |
| `investment-memo-writing/` | First-line recommendation, steelman against, decision log |
| `deal-winning-process/` | Competitive round closing with value previews |
| `term-sheet-triage/` | Fast term analysis with scenario tables |
| `judgment-postmortem-calibration/` | Decision logs and heuristic extraction |
| `saas-metrics-diligence/` | SaaS-specific metrics validation |
| `portfolio-support-ops/` | Portfolio company support workflows |
| `salesforce-crm-ops/` | CRM operations with field mapping, dry-run mode, schema discovery |

### Compound skills (full workflows)

| Skill | Description |
|---|---|
| `dealflow-sourcing-to-memo/` | End-to-end 3/5/10-day sprints with gates at each phase |
| `diligence-sprint/` | Time-boxed diligence with daily deliverables and kill gates |
| `portfolio-helpdesk-sprint/` | Structured portfolio support |

## Key changes in v0.2

- **Top 10 force-ranked list** with must-be-true + wedge + why now + what would change your mind
- **Kill criteria and contrarian hypotheses** in thesis mapping
- **Sourcing loops as first-class objects** with weekly/monthly cadence metrics
- **Max 4 risks** in diligence (forces prioritization)
- **Anti-confirmation evidence required** (churned customer + competitor user calls)
- **Steelman "best argument against"** mandatory in memos
- **Decision log** (what changed since first call) in memos
- **Time-boxed compound workflows** with explicit kill/continue/escalate gates
- **Salesforce as hard gate** (no qualified company without SF record + next task)
- **Field mapping config** + dry-run mode + schema discovery for Salesforce

## Quick start

1. Clone this repo
2. Point your agent at this directory
3. For Salesforce integration:
   - Run `python3 salesforce-crm-ops/scripts/sf_describe.py Lead Account Opportunity` to discover your org's schema
   - Edit `salesforce-crm-ops/config/field_map.yaml` and `stages.yaml` for your org
   - Always use `--dry-run` flag first

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
