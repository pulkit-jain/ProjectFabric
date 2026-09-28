# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Initial scaffold: `copilot-instructions.md`, agent definitions (Planner, Risk Manager,
  Stakeholder Manager, Project Manager, Worker), `/pf-0` through `/pf-14` prompt commands,
  artifact templates for Charter, Scope Statement, WBS, Schedule, Risk Register,
  Stakeholder Register, RACI, Communications Plan, Tracker, Work Package, Status Report,
  Change Request, and Lessons Learned.
- `docs/architecture.md` describing the file-based state model and future extension points.
- `docs/knowledge-areas.md` describing v1 vs planned PMBOK-style knowledge area coverage.
- Cost Management knowledge area: `pf-cost-manager` agent, `/pf-3b-plan-cost` command (slotted
  between `/pf-3-plan-schedule` and `/pf-4-plan-risk` without renumbering existing commands),
  `cost-management-plan.template.md` and `cost-performance.template.md` (supporting both
  Lightweight budget-vs-actual and Full EVM tracking modes, chosen per project). Wired into
  `/pf-11-control-cycle`, the Status Report template (Cost Highlights), and the Change Request
  template (Cost impact dimension + baseline reference).
- Project Constitution pattern (inspired by GitHub Spec Kit): `/pf-0b-constitution` command and
  `constitution.template.md`, capturing project-specific principles, decision authority,
  reporting cadence, escalation rules, and project-level Definition of Done — layered on top of
  the framework-wide `copilot-instructions.md`. Owned by the Planner; baselined via Change
  Control once approved.
- Proactive checkpoint/resume hints in the long-running prompts (`/pf-7-initiate-manager`,
  `/pf-9-initiate-worker`, `/pf-11-control-cycle`) pointing to `/pf-13-handoff` before a
  conversation hits its context limit, rather than only after.
- Resource Management (depth) knowledge area: `pf-resource-manager` agent, `/pf-6b-plan-resources`
  command (slotted between `/pf-6-plan-organization` and `/pf-7-initiate-manager`),
  `resource-management-plan.template.md` (roles/resources needed, resource calendars, capacity
  plan, control thresholds) and `resource-allocation.template.md` (living utilization/conflict
  tracking, updated each control cycle). Wired into `/pf-7-initiate-manager`,
  `/pf-11-control-cycle`, the Status Report template (Resource Highlights), and the Change
  Request template (Resource impact dimension + baseline reference).
- `ROADMAP.md`: governance doc tracking knowledge-area coverage status and the framework-feature
  backlog evaluated from reference-repo research, with Done/Planned/Deferred/Rejected markers.
- Quality Management knowledge area: `pf-quality-manager` agent, `/pf-4b-plan-quality` command
  (slotted between `/pf-4-plan-risk` and `/pf-5-plan-stakeholders`),
  `quality-management-plan.template.md` (standards, metrics, QA vs. QC approach, QA gate
  criteria) and `quality-control-log.template.md` (living per-work-package gate review log with
  trend notes). Wired into `/pf-10-check-report` (a work package cannot be set to "Done" until it
  passes the QA gate), `/pf-11-control-cycle` (defect trend review), the Status Report template
  (Quality Highlights), the Change Request template (baseline reference), and the Worker agent
  (QA gate awareness alongside WBS acceptance criteria).
- Procurement Management knowledge area: `pf-procurement-manager` agent, `/pf-4c-plan-procurement`
  command (slotted between `/pf-4b-plan-quality` and `/pf-5-plan-stakeholders`),
  `procurement-management-plan.template.md` (make-or-buy analysis, vendor selection criteria,
  contract types, procurement risk cross-reference, control thresholds) and
  `vendor-contract-register.template.md` (living vendor/contract tracking, updated each control
  cycle). Wired into `/pf-11-control-cycle` (vendor/contract review), the Status Report template
  (Procurement Highlights), and the Change Request template (Procurement impact dimension +
  baseline reference). This completes the core PMBOK-style knowledge-area kit — see
  `ROADMAP.md` for what's left in the framework-feature backlog.

### Fixed

- Stale references to Cost/Resource Management as unimplemented v2 knowledge areas, found while
  validating the framework end-to-end with a full simulated project run (see
  `_sandbox/demo-project/` locally, gitignored): `templates/charter.template.md`'s Budget Summary
  comment, `docs/architecture.md`'s "Non-goals for v1" list, and
  `.github/agents/planner.agent.md`'s knowledge-area flagging guidance all still said cost/
  resourcing were out of scope after both were implemented.
- A second stale v2-scope reference, found via a second end-to-end test run (see
  `_sandbox/video-onboarding/` locally, gitignored) covering a Quality gate failure/re-review
  cycle and Procurement vendor tracking: `README.md`'s "Knowledge Area Coverage" section still
  said Cost, Resource, Quality, and Procurement were "planned for v2" after all four had shipped.

### Added

- `docs/test-plan.md`: test methodology, a log of the two end-to-end sandbox test runs so far,
  command/scenario coverage matrices, and a prioritized backlog of future test scenarios
  (rejected CRs, cost breaches, blocking resource conflicts, recurring quality defects, real
  parallel Workers, handoff resumption, incomplete closure, constitution amendment).
- Third end-to-end test run (T3, "Regional Data Center Migration", `_sandbox/datacenter-migration/`
  locally, gitignored) covering all 8 previously-untested scenarios in one run: a **rejected**
  Change Request (CR-002), an actual cost-threshold breach, a resource conflict that genuinely
  blocked (not just absorbed by slack), a recurring quality defect that fired
  `quality-control-log.md`'s Trend Notes and was proactively prevented on the third occurrence,
  two Workers genuinely dispatched in parallel before either reported back, a real
  `/pf-13-handoff` mid-task resumption by a fresh instance, a `constitution.md` amendment via
  Change Control (CR-004) later cited to accept a new risk without a CR, and project closure with
  one work package **Descoped** rather than Done (CR-005). No framework bugs found this round —
  `docs/test-plan.md`'s coverage matrices updated accordingly.
- Fourth end-to-end test run (T4, "Enterprise CRM Rollout", `_sandbox/crm-rollout/` locally,
  gitignored) clearing the remaining test backlog: an 18-work-package, 4-Worker project to
  stress-test scale (`tracker.md`/`raci.md` stayed fully readable), a genuine stakeholder
  engagement drift (Supportive → Resistant → Supportive) caught via a Worker's report and
  resolved via a Change Request rather than waiting for the next scheduled control cycle, and a
  mid-project risk (R-004) added by re-running the risk identification/scoring dialogue and
  inserted in correct sorted position rather than appended or hand-edited. No framework bugs
  found — `docs/test-plan.md` now shows the full T1–T4 scenario backlog covered.
