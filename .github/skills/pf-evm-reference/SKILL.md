---
name: pf-evm-reference
description: 'Earned Value Management (EVM) formulas, computation steps, and interpretation guidance for Full EVM cost tracking mode. Use when the Cost Manager is computing or explaining cost-performance.md during /pf-3b-plan-cost or /pf-11-control-cycle for a project using Full EVM mode.'
---

# Earned Value Management Reference

## When to Use

- A project's `cost-management-plan.md` has **Mode: Full EVM** (not Lightweight).
- Updating `cost-performance.md` during `/pf-11-control-cycle`.
- Explaining a CPI/SPI/EAC/VAC number to the user.

Skip this entirely for Lightweight mode — that mode is just Budgeted vs. Actual vs. Variance,
no formulas needed.

## Inputs (from other `.pmo/` files)

| Term | Definition | Source |
|---|---|---|
| BAC (Budget at Completion) | Total approved budget for a work package | `cost-management-plan.md`'s Budget Baseline table |
| % Complete | Reported physical progress | `tracker.md` |
| AC (Actual Cost) | Actual money/effort spent so far | Reported by the Worker/Project Manager |

## Formulas (compute in this order)

1. **PV** (Planned Value) = the budgeted cost of work that *should* be complete as of the
   scheduled date, per `schedule.md`.
2. **EV** (Earned Value) = % Complete × BAC.
3. **AC** (Actual Cost) = as reported.
4. **CV** (Cost Variance) = EV − AC
5. **SV** (Schedule Variance) = EV − PV
6. **CPI** (Cost Performance Index) = EV / AC
7. **SPI** (Schedule Performance Index) = EV / PV
8. **EAC** (Estimate at Completion) = BAC / CPI
9. **ETC** (Estimate to Complete) = EAC − AC
10. **VAC** (Variance at Completion) = BAC − EAC

## Interpretation

| Metric | > 1.0 | = 1.0 | < 1.0 |
|---|---|---|---|
| CPI | Under budget | Exactly on budget | Over budget |
| SPI | Ahead of schedule | Exactly on schedule | Behind schedule |

| CV / SV / VAC | Positive | Zero | Negative |
|---|---|---|---|
| Meaning | Favorable (under budget / ahead of schedule / will finish under budget) | On target | Unfavorable |

## Worked Example

BAC = $10,000, % Complete = 40%, AC = $4,800, PV (per schedule) = $4,000.

- EV = 0.40 × $10,000 = **$4,000**
- CV = $4,000 − $4,800 = **−$800** (over budget)
- SV = $4,000 − $4,000 = **$0** (on schedule)
- CPI = $4,000 / $4,800 = **0.83** (over budget — spending $1 for every $0.83 of value earned)
- SPI = $4,000 / $4,000 = **1.00** (on schedule)
- EAC = $10,000 / 0.83 = **$12,048**
- ETC = $12,048 − $4,800 = **$7,248**
- VAC = $10,000 − $12,048 = **−$2,048** (projected to finish $2,048 over budget)

## Common Mistakes to Avoid

- Don't confuse PV with the *budget baseline total* — PV is time-phased (what should be spent
  *by this point*), not the whole BAC.
- Don't compute EV from % Complete estimates the Worker didn't actually report — pull it from
  `tracker.md`, never guess it.
- CPI and SPI are ratios, not percentages — report them as e.g. `0.83`, not `83%`.
