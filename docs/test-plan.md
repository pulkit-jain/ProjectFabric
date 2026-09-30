# Test Plan

How ProjectFabric is validated: since it's a pure prompt/agent framework (no code to unit-test),
validation means simulating a full project lifecycle — playing every agent role in sequence and
writing real `.pmo/` files — to prove the artifacts, cross-references, and handoffs actually work
together, not just read correctly in isolation. This file tracks what's been exercised so future
changes can be checked against real gaps instead of re-deriving them from scratch.

## Method

1. Create a new folder under `_sandbox/<name>/.pmo/` (gitignored, never committed).
2. Play every agent role yourself, in command order, writing the actual Markdown files each
   `/pf-N` command would produce — don't just describe what *would* happen. Run the helper
   scripts for real rather than simulating their output.
3. Deliberately design the fictitious project so at least one scenario forces an interesting
   path (a risk triggering, a gate failing, a vendor conflict) rather than a clean happy path
   only — happy-path-only runs don't find bugs.
4. After the run, `grep_search` the whole repo for stale references related to whatever changed
   (e.g. `"planned for v2"`, `"not yet implemented"`) — direct doc review reliably misses these,
   the combination of a live run + targeted grep catches them.
5. Fix what's found, log it in `CHANGELOG.md` under `### Fixed`, and record the scenario here.
6. Before or alongside a lifecycle run, do the **static audit** below. A lifecycle run is
   played by someone who already knows the framework, so it cannot tell whether a prompt
   actually tells an agent what it needs; the static audit can.

## Static Audit

Mechanical cross-reference checks over the whole repo. Not committed as a script; re-create
checks like these (a short Python script over the Markdown files works) whenever prompts,
templates, agents, or skills change:

- Every prompt has `description` frontmatter and an H1 equal to its filename, and every agent it
  says to "act as" exists.
- Every `/pf-...` command mentioned anywhere resolves to a real prompt, and every prompt is in
  the README commands table.
- Every `templates/*.template.md` is referenced by at least one prompt, agent, skill, or the
  scaffold script, and every template a document points to exists.
- Agent frontmatter has `name`, `description`, `tools`, plus a Tier line; each skill's `name`
  matches its folder and its description is at most 1024 characters; every skill an agent or
  prompt mentions exists.
- The Ownership table's commands exist; the `/pf-0-init` file tree, `pf_scaffold.py`'s list, and
  the README tree agree; every scaffolded artifact has an owner.
- Relative Markdown links resolve; ROADMAP IDs are unique and every cited ID exists.
- A list of stale phrases (`"four Design Principles"`, `"planned for v2"`, `"cannot move files"`,
  agent and skill counts) does not appear outside history.
- The command graph is read by eye: each prompt's "next command" makes sense for every
  Workflow Preset.

## Test Runs Log

| ID | Name | Date | Sandbox Path | Cost Mode | Focus |
|---|---|---|---|---|---|
| T1 | Internal Wiki Migration | 2026-09-28 | `_sandbox/demo-project/` | Lightweight | Cost + Resource Management (first pass, before Quality/Procurement existed) |
| T2 | New Customer Onboarding Video Series | 2026-09-28 | `_sandbox/video-onboarding/` | Full EVM | Quality gate failure/re-review, Procurement vendor tracking |
| T3 | Regional Data Center Migration | 2026-09-28 | `_sandbox/datacenter-migration/` | Lightweight | Rejected CR, cost breach, blocking resource conflict, recurring quality defect, real parallel Workers, genuine handoff resumption, constitution amendment, incomplete closure (the 8 scenarios formerly listed as backlog items T3–T10) |
| T4 | Enterprise CRM Rollout | 2026-09-28 | `_sandbox/crm-rollout/` | Lightweight | Scale (18 work packages, 4 Workers), stakeholder engagement drift/recovery, mid-project risk added via command re-run (the 3 scenarios formerly listed as backlog items T11–T13) |
| A1 | Static audit | 2026-09-30 | whole repo | n/a | Cross-reference audit (see above); found 8 templates that no prompt told an agent to use, plus preset-gating and workflow-chain gaps |
| T5 | Meadowlark Tea Packaging Redesign | 2026-09-30 | `_sandbox/packaging-redesign/` | Full EVM | Everything added since T4 in one project: Workflow Presets (agile-hybrid with three Optional phases skipped), `team.md` with a constitution override, the Agile ceremony layer, Definition of Ready failure and waiver, batch dispatch, decision log with supersession, stage archiving, the four helper scripts, and automation rules |

## Coverage Matrix — Commands

`⏭` = the command's phase was Optional under the project's Workflow Preset and was skipped on
purpose, which exercises the skip path rather than the command itself. `—` = not run.

| Command | T1 | T2 | T3 | T4 | T5 | Notes |
|---|---|---|---|---|---|---|
| `/pf-0-init` | ✅ | ✅ | ✅ | ✅ | ✅ | T5 used `pf_scaffold.py` with `--team` and `--preset`, then re-ran it (nothing overwritten) |
| `/pf-0b-constitution` | ✅ | ✅ | ✅ | ✅ | ✅ | T3 exercised amending it mid-project via CR-004; T5 added an "Overrides of team.md" row and a Definition of Ready addition |
| `/pf-1-initiate-planner` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `/pf-2-plan-scope-wbs` | ✅ | ✅ | ✅ | ✅ | ✅ | T3 also exercised descoping a deliverable via CR-005; T4 scaled to 18 leaves |
| `/pf-3-plan-schedule` | ✅ | ✅ | ✅ | ✅ | ✅ | |
| `/pf-3b-plan-cost` | ✅ | ✅ | ✅ | ✅ | ✅ | T1/T3/T4 = Lightweight, T2/T5 = Full EVM. T5: Optional under agile-hybrid, asked once, team default mode accepted |
| `/pf-4-plan-risk` | ✅ | ✅ | ✅ | ✅ | ✅ | T4 exercised a genuine mid-project re-run to add a single risk (R-004), not just initial planning |
| `/pf-4b-plan-quality` | — | ✅ | ✅ | ✅ | ⏭ | Didn't exist yet at T1. T5 skipped it (Optional); the rest of the run had to tolerate its absence |
| `/pf-4c-plan-procurement` | — | ✅ | ✅ | ✅ | ⏭ | T3/T4's plans conclude "Make" for everything. T5 skipped it (Optional) |
| `/pf-5-plan-stakeholders` | ✅ | ✅ | ✅ | ✅ | ✅ | T4 exercised a genuine engagement drift and recovery |
| `/pf-6-plan-organization` | ✅ | ✅ | ✅ | ✅ | ✅ | T4 scaled RACI to 18 rows × 4 Workers. T5 planted a missing Accountable that the validator later caught |
| `/pf-6b-plan-resources` | ✅ | ✅ | ✅ | ✅ | ⏭ | T3 deliberately left a conflict unresolved at planning time to test the negative path |
| `/pf-7-initiate-manager` | ✅ | ✅ | ✅ | ✅ | ✅ | T5 with missing Optional plans (see A1 finding) |
| `/pf-7b-sprint-planning` | — | — | — | — | ✅ | Two sprints; capacity taken from the user, not invented |
| `/pf-8-assign-task` | ✅ | ✅ | ✅ | ✅ | ✅ | T3 dispatched two Workers in the same round. T5: batch of two, one dropped on a failed Definition of Ready, re-dispatched later; a waiver recorded in `task.md` |
| `/pf-8b-standup` | — | — | — | — | ✅ | A Blocked work package surfaced here and led to DEC-001 |
| `/pf-9-initiate-worker` | ✅ | ✅ | ✅ | ✅ | ✅ | T3 includes a genuine mid-task handoff and resumption |
| `/pf-10-check-report` | ✅ | ✅ | ✅ | ✅ | ✅ | T2/T3 exercised the QA-gate-fail path. T5 had no quality plan, so no QA gate ran |
| `/pf-10b-backlog-refinement` | — | — | — | — | ✅ | One Ready, two Not Ready (Legal review not scheduled; printer inputs missing) |
| `/pf-10c-sprint-review` | — | — | — | — | ✅ | User-as-Product-Owner rejected 2.1; rework without a CR, later a cost CR |
| `/pf-11-control-cycle` | ✅ | ✅ | ✅ | ✅ | ✅ | T5 ran three cycles including one ad hoc; found that rules ran before the cost refresh |
| `/pf-11b-sprint-retro` | — | — | — | — | ✅ | Sprint 1 only |
| `/pf-12-change-request` | ✅ | ✅ | ✅ | ✅ | ✅ | T3 adds a **Rejected** CR (CR-002) alongside several Approved ones |
| `/pf-12b-log-decision` | — | — | — | — | ✅ | Three decisions: Draft → Signed-off, and one Superseded by a later one |
| `/pf-13-handoff` | ⚠️ | — | ✅ | — | ✅ | T3 simulates a fresh instance genuinely resuming from the handoff log. T5 wrote a Manager handoff into the tracker |
| `/pf-13b-archive-stage` | — | — | — | — | ✅ | Partial-stage archive with a real move; the validator still passed afterward. The refuse-unfinished-work path was reasoned from the prompt, not run |
| `/pf-14-close-project` | ✅ | ✅ | ✅ | ✅ | ✅ | T3 closes with one work package **Descoped**, not Done, per its step 1. T5 read a stage summary |

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
| Change Request **Approved** | ✅ | T1, T2, T3 (CR-001, CR-003, CR-004, CR-005), T5 (CR-001) |
| Change Request **Rejected** | ✅ | T3 (CR-002, cost increase rejected due to budget freeze) |
| Cost variance actually **breaching** the control threshold (Yellow/Red cost status) | ✅ | T3 (WP-3.1, 18.2% over), T5 (WP-2.1, CPI 0.75) |
| Quality trend note firing from a **recurring** defect pattern (2+ occurrences) | ✅ | T3 (timezone bug on 2.1 and 2.2, proactively prevented on 2.3) |
| Two or more Workers genuinely in parallel (dispatched before either reports back) | ✅ | T3 (WP-1.1/WP-1.2, both In Progress simultaneously), T5 (1.1 and 1.2) |
| `/pf-13-handoff` actually resumed by a fresh Manager/Worker instance | ✅ | T3 (WP-3.2, mid-cutover handoff and clean resumption) |
| Constitution amended mid-project via Change Control | ✅ | T3 (CR-004, risk-acceptance threshold raised, then cited by a later risk acceptance) |
| Project closed with an open/incomplete work package (descope or hold) | ✅ | T3 (WP-4.1 descoped via CR-005 at closing) |
| Constitution escalation threshold referenced in a real decision | ✅ | T1, T2, T3, T5 (10% team threshold) |
| Cost/Resource/Quality/Procurement baseline updated via CR | ✅ | T1 (cost), T2 (schedule), T3 (schedule, resource, constitution, scope), T5 (cost) |
| Project closes with every work package Done | ✅ | T1, T2, T5 |
| Re-running `/pf-4-plan-risk` mid-project to add a single new risk | ✅ | T4 (R-004, inserted in correct sorted position without disturbing existing risks) |
| Stakeholder engagement drift detected and reacted to mid-project | ✅ | T4 (Sales Ops Lead, Supportive → Resistant → Supportive, caught via a Worker's report, not a scheduled cycle) |
| Scale: 15+ work packages, 4+ Workers, `tracker.md`/`raci.md` stay readable | ✅ | T4 (18 work packages, 4 Workers) |
| Workflow Preset **agile-hybrid**: three Optional phases skipped, later commands and scripts tolerate their absence | ✅ | T5 |
| `team.md` copied in at init; constitution overrides a team default with a stated reason | ✅ | T5 (control cycle cadence) |
| Definition of Ready **fails** (input missing), work package dropped from the batch, re-dispatched later | ✅ | T5 (WP-1.2) |
| Definition of Ready failure **waived** by the user and recorded in `task.md` | ✅ | T5 (WP-2.2, Legal review) |
| Sprint Review **rejects** a work package; rework without a CR, then a cost CR | ✅ | T5 (WP-2.1) |
| Decision lifecycle Draft → Signed-off → Superseded | ✅ | T5 (DEC-002 superseded by DEC-003) |
| Decision (no baseline change) kept distinct from a Change Request | ✅ | T5 (DEC-001 vs CR-001) |
| Validator catches a real slip at a control cycle, owner fixes it, re-run passes | ✅ | T5 (3.1 had no Accountable) |
| Automation rules: TRIGGERED, not triggered, and not computable in the same run | ✅ | T5 (A-001 n/a in Full EVM) |
| Automation rules read stale data if run before the cost refresh | ✅ found + fixed | T5 (CPI read 0.95 instead of 0.75) |
| EVM computed by `pf_evm.py`; a breach drives a CR | ✅ | T5 |
| Stage archive with a real move; `pf_validate.py` still passes afterward | ✅ | T5 (Sprint 1, partial) |
| Static audit finds prompts that never tell an agent to use their template | ✅ found + fixed | A1 (8 templates) |
| `## <Agent> - <Action>` status header on responses (REP-01) | ⚠️ not file-verifiable | It governs chat responses, not artifacts |

## Future Test Scenarios (backlog)

Gaps left by T5, in rough priority order:

- A **lean** project run, to check the minimum path (`/pf-7-initiate-manager` with almost nothing
  planned) end to end. Only the prompts were reviewed, not a live run.
- A **classic-waterfall** run against the current prompts. T1–T4 predate presets, the Definition
  of Ready, and the scripts.
- Batch dispatch where two eligible work packages share a Worker (the earlier one goes, the other
  queues) — not triggered in T5.
- `/pf-13b-archive-stage` refusing an unaccepted work package, run rather than reasoned.
- A plugin actually installed and removed (`plugins/README.md` has never been exercised).
- Lightweight-mode cost with `pf_rules.py`'s `cost_overrun_pct_max`.

Add new entries here as new framework features are built, or if real-world usage surfaces a gap
this simulated testing didn't anticipate. Each future run should also be added to the Test Runs
Log and both Coverage Matrices above.
