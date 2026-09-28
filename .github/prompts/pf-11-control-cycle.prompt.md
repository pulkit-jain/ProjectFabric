---
description: Run a periodic monitoring & controlling pass across Tracker, Risk, and Stakeholder state; produce a Status Report.
---

# /pf-11-control-cycle

Act as the `pf-project-manager` agent. Read `tracker.md`, `schedule.md`, `risk-register.md`,
`stakeholder-register.md`, `cost-management-plan.md`, and `resource-management-plan.md`; produce
`.pmo/reports/status-<date>.md` and (in coordination with the Cost Manager and Resource Manager
perspectives) update `.pmo/cost-performance.md` and `.pmo/resource-allocation.md`.

## Steps

1. Compare `tracker.md` against `schedule.md`: flag any work package whose actual dates or
   dependencies have drifted from the baseline, and any milestone now at risk.
2. Review `risk-register.md`: any risk whose trigger condition may have fired, any risk that
   should be re-scored, any newly reported risk not yet logged.
3. Review `stakeholder-register.md` (in coordination with the Stakeholder Manager perspective):
   any stakeholder whose current engagement appears to be drifting away from the desired level.
4. Update `cost-performance.md` (in coordination with the Cost Manager perspective): using
   `tracker.md`'s `% Complete` against the budget baseline in `cost-management-plan.md`, refresh
   the Lightweight or Full EVM table (whichever mode is set) and flag any variance breaching the
   cost control threshold.
5. Update `resource-allocation.md` (in coordination with the Resource Manager perspective):
   refresh assignment/utilization per resource against `resource-management-plan.md`'s capacity
   plan, and flag any resource over-allocated across concurrent work packages.
6. Determine an overall status color: Green (on track), Yellow (at risk, being managed), or Red
   (baseline breach requiring a decision).
7. Write `reports/status-<date>.md` using `templates/status-report.template.md`: accomplishments
   since last cycle, upcoming work, open issues/blockers, risk highlights, cost highlights,
   resource highlights, stakeholder notes, and any change requests raised.
8. Present the Status Report to the user. If it surfaces a baseline breach (schedule, cost, or
   resource conflict), tell the user to run `/pf-12-change-request`. Otherwise, continue the
   assign/report loop with `/pf-8-assign-task`.

## If this conversation runs long

Don't wait to be cut off. If reviewing Tracker, Risk, Cost, and Stakeholder state across several
exchanges pushes this conversation toward its context limit before the Status Report is written,
proactively tell the user to run `/pf-13-handoff` now.
