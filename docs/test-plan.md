# Test Plan

How ProjectFabric is validated: since it's a pure prompt/agent framework (no code to unit-test),
validation means simulating a full project lifecycle — playing every agent role in sequence and
writing real `.pmo/` files — to prove the artifacts, cross-references, and handoffs actually work
together, not just read correctly in isolation. This file tracks what's been exercised so future
changes can be checked against real gaps instead of re-deriving them from scratch.

## Method

1. Create a new folder under `_sandbox/<name>/.pmo/` (gitignored, never committed).
2. Play every agent role yourself, in command order, writing the actual Markdown files each
   `/pf-N` command would produce — don't just describe what *would* happen.
3. Deliberately design the fictitious project so at least one scenario forces an interesting
   path (a risk triggering, a gate failing, a vendor conflict) rather than a clean happy path
   only — happy-path-only runs don't find bugs.
4. After the run, `grep_search` the whole repo for stale references related to whatever changed
   (e.g. `"planned for v2"`, `"not yet implemented"`) — direct doc review reliably misses these,
   the combination of a live run + targeted grep catches them.
5. Fix what's found, log it in `CHANGELOG.md` under `### Fixed`, and record the scenario here.

## Test Runs Log

| ID | Name | Date | Sandbox Path | Cost Mode | Focus |
|---|---|---|---|---|---|
| T1 | Internal Wiki Migration | 2026-09-28 | `_sandbox/demo-project/` | Lightweight | Cost + Resource Management (first pass, before Quality/Procurement existed) |
| T2 | New Customer Onboarding Video Series | 2026-09-28 | `_sandbox/video-onboarding/` | Full EVM | Quality gate failure/re-review, Procurement vendor tracking |
| T3 | Regional Data Center Migration | 2026-09-28 | `_sandbox/datacenter-migration/` | Lightweight | Rejected CR, cost breach, blocking resource conflict, recurring quality defect, real parallel Workers, genuine handoff resumption, constitution amendment, incomplete closure (the 8 scenarios formerly listed as backlog items T3–T10) |
| T4 | Enterprise CRM Rollout | 2026-09-28 | `_sandbox/crm-rollout/` | Lightweight | Scale (18 work packages, 4 Workers), stakeholder engagement drift/recovery, mid-project risk added via command re-run (the 3 scenarios formerly listed as backlog items T11–T13) |

## Coverage Matrix — Commands

| Command | T1 | T2 | T3 | T4 | Notes |
|---|---|---|---|---|---|
| `/pf-0-init` | ✅ | ✅ | ✅ | ✅ | |
| `/pf-0b-constitution` | ✅ | ✅ | ✅ | ✅ | T3 also exercised amending it mid-project via CR-004 |
| `/pf-1-initiate-planner` | ✅ | ✅ | ✅ | ✅ | |
| `/pf-2-plan-scope-wbs` | ✅ | ✅ | ✅ | ✅ | T3 also exercised descoping a deliverable via CR-005; T4 scaled to 18 leaves |
| `/pf-3-plan-schedule` | ✅ | ✅ | ✅ | ✅ | |
| `/pf-3b-plan-cost` | ✅ | ✅ | ✅ | ✅ | T1/T3/T4 = Lightweight, T2 = Full EVM — both modes covered |
| `/pf-4-plan-risk` | ✅ | ✅ | ✅ | ✅ | T4 exercised a genuine mid-project re-run to add a single risk (R-004), not just initial planning |
| `/pf-4b-plan-quality` | — | ✅ | ✅ | ✅ | Didn't exist yet at T1 |
| `/pf-4c-plan-procurement` | — | ✅ | ✅ | ✅ | T3/T4's plans conclude "Make" for everything — didn't exist yet at T1 |
| `/pf-5-plan-stakeholders` | ✅ | ✅ | ✅ | ✅ | T4 exercised a genuine engagement drift and recovery |
| `/pf-6-plan-organization` | ✅ | ✅ | ✅ | ✅ | T4 scaled RACI to 18 rows × 4 Workers |
| `/pf-6b-plan-resources` | ✅ | ✅ | ✅ | ✅ | T3 deliberately left a conflict unresolved at planning time to test the negative path |
| `/pf-7-initiate-manager` | ✅ | ✅ | ✅ | ✅ | |
| `/pf-8-assign-task` | ✅ | ✅ | ✅ | ✅ | T3 dispatched two Workers in the same round before either reported back |
| `/pf-9-initiate-worker` | ✅ | ✅ | ✅ | ✅ | T3 includes a genuine mid-task handoff and resumption |
| `/pf-10-check-report` | ✅ | ✅ | ✅ | ✅ | T2/T3 exercised the QA-gate-fail path inside this command |
| `/pf-11-control-cycle` | ✅ | ✅ | ✅ | ✅ | |
| `/pf-12-change-request` | ✅ | ✅ | ✅ | ✅ | T3 adds a **Rejected** CR (CR-002) alongside several Approved ones |
| `/pf-13-handoff` | ⚠️ | — | ✅ | — | T3 simulates a fresh instance genuinely resuming from the handoff log, not just writing it |
| `/pf-14-close-project` | ✅ | ✅ | ✅ | ✅ | T3 closes with one work package **Descoped**, not Done, per its step 1 |

## Coverage Matrix — Scenarios

| Scenario | Covered? | Where |
|---|---|---|
| Risk triggers mid-execution → Change Request | ✅ | T1 (R-001, technical) |
| QA gate passes cleanly | ✅ | T2 (Videos 1 & 3), T3 (WP-2.3) |
| QA gate **fails**, vendor rework, re-review passes | ✅ | T2 (Video 2) |
| Make-or-buy analysis concludes "Buy", fixed-price contract | ✅ | T2 |
| Make-or-buy analysis concludes "Make" (kept in-house) | ✅ | T3 |
| Vendor tracked as a non-Worker `Owner` in `tracker.md`/`raci.md` | ✅ | T2 |
| Resource conflict flagged in planning, absorbed by schedule slack | ✅ | T1 (worker-content PTO) |
| Resource over-allocation that actually blocks (not absorbed by slack) → CR | ✅ | T3 (worker-a on 2.1+2.3, resolved via CR-001) |
| Change Request **Approved** | ✅ | T1, T2, T3 (CR-001, CR-003, CR-004, CR-005) |
| Change Request **Rejected** | ✅ | T3 (CR-002, cost increase rejected due to budget freeze) |
| Cost variance actually **breaching** the control threshold (Yellow/Red cost status) | ✅ | T3 (WP-3.1, 18.2% over) |
| Quality trend note firing from a **recurring** defect pattern (2+ occurrences) | ✅ | T3 (timezone bug on 2.1 and 2.2, proactively prevented on 2.3) |
| Two or more Workers genuinely in parallel (dispatched before either reports back) | ✅ | T3 (WP-1.1/WP-1.2, both In Progress simultaneously) |
| `/pf-13-handoff` actually resumed by a fresh Manager/Worker instance | ✅ | T3 (WP-3.2, mid-cutover handoff and clean resumption) |
| Constitution amended mid-project via Change Control | ✅ | T3 (CR-004, risk-acceptance threshold raised, then cited by a later risk acceptance) |
| Project closed with an open/incomplete work package (descope or hold) | ✅ | T3 (WP-4.1 descoped via CR-005 at closing) |
| Constitution escalation threshold referenced in a real decision | ✅ | T1, T2, T3 |
| Cost/Resource/Quality/Procurement baseline updated via CR | ✅ | T1 (cost), T2 (schedule), T3 (schedule, resource, constitution, scope) |
| Project closes with every work package Done | ✅ | T1, T2 |
| Re-running `/pf-4-plan-risk` mid-project to add a single new risk | ✅ | T4 (R-004, inserted in correct sorted position without disturbing existing risks) |
| Stakeholder engagement drift detected and reacted to mid-project | ✅ | T4 (Sales Ops Lead, Supportive → Resistant → Supportive, caught via a Worker's report, not a scheduled cycle) |
| Scale: 15+ work packages, 4+ Workers, `tracker.md`/`raci.md` stay readable | ✅ | T4 (18 work packages, 4 Workers) |

## Future Test Scenarios (backlog)

All scenarios identified so far (T1–T13) are now covered. Add new entries here as new framework
features are built (e.g. once the "Framework Features" backlog items ship — Definition of Ready,
decision log, agile ceremony layer — each should get its own test scenario) or if a real-world
usage surfaces a gap this simulated testing didn't anticipate.

Each future run should also be added to the Test Runs Log and both Coverage Matrices above.
