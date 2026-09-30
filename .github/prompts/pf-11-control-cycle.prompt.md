---
description: Run a periodic monitoring & controlling pass across Tracker, Risk, and Stakeholder state; produce a Status Report.
---

# /pf-11-control-cycle

Act as the `pf-project-manager` agent. Read `tracker.md`, `schedule.md`, `risk-register.md`,
`stakeholder-register.md`, `cost-management-plan.md`, `resource-management-plan.md`, and (if it
exists) `procurement-management-plan.md`; produce `.pmo/reports/status-<date>.md` and (in
coordination with the Cost Manager, Resource Manager, Quality Manager, and Procurement Manager
perspectives) update `.pmo/cost-performance.md`, `.pmo/resource-allocation.md`,
`.pmo/quality-control-log.md`'s Trend Notes, and `.pmo/vendor-contract-register.md`.

## Steps

0. Run `pf_validate.py --pmo .pmo` and `pf_rules.py --pmo .pmo` (see the `pf-helper-scripts`
   skill). Note every validator FAIL/WARN and every TRIGGERED automation rule for the Status
   Report; present each rule's suggested command to the user rather than running it. Fix a
   validator finding only in artifacts you own; route the rest to the owning agent or the user.
   If a script can't be run, skip it and say so.
1. Compare `tracker.md` against `schedule.md`: flag any work package whose actual dates or
   dependencies have drifted from the baseline, and any milestone now at risk.
2. Review `risk-register.md`: any risk whose trigger condition may have fired, any risk that
   should be re-scored, any newly reported risk not yet logged.
3. Review `stakeholder-register.md` (in coordination with the Stakeholder Manager perspective):
   any stakeholder whose current engagement appears to be drifting away from the desired level.
4. Update `cost-performance.md` (in coordination with the Cost Manager perspective): using
   `tracker.md`'s `% Complete` against the budget baseline in `cost-management-plan.md`, refresh
   the Lightweight or Full EVM table (whichever mode is set) and flag any variance breaching the
   cost control threshold. In Full EVM mode, compute the figures with `pf_evm.py` rather than by
   hand.
5. Update `resource-allocation.md` (in coordination with the Resource Manager perspective):
   refresh assignment/utilization per resource against `resource-management-plan.md`'s capacity
   plan, and flag any resource over-allocated across concurrent work packages.
6. Review `quality-control-log.md` (in coordination with the Quality Manager perspective) for
   recurring defect patterns or a metric trending the wrong way across work packages, and add a
   Trend Note if one exists.
7. If `procurement-management-plan.md` exists, update `vendor-contract-register.md` (in
   coordination with the Procurement Manager perspective): contract status, delivery performance,
   and any dispute or variance against the procurement control thresholds.
8. Determine an overall status color: Green (on track), Yellow (at risk, being managed), or Red
   (baseline breach requiring a decision).
9. Write `reports/status-<date>.md` using `templates/status-report.template.md`: accomplishments
   since last cycle, upcoming work, open issues/blockers, risk highlights, cost highlights,
   resource highlights, quality highlights, procurement highlights, stakeholder notes, and any
   change requests raised.
10. Present the Status Report to the user. If it surfaces a baseline breach (schedule, cost,
    resource conflict, or vendor issue), tell the user to run `/pf-12-change-request`. Otherwise,
    continue the assign/report loop with `/pf-8-assign-task`.

## If this conversation runs long

Don't wait to be cut off. If reviewing Tracker, Risk, Cost, and Stakeholder state across several
exchanges pushes this conversation toward its context limit before the Status Report is written,
proactively tell the user to run `/pf-13-handoff` now.
