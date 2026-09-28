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

## Coverage Matrix — Commands

| Command | T1 | T2 | Notes |
|---|---|---|---|
| `/pf-0-init` | ✅ | ✅ | |
| `/pf-0b-constitution` | ✅ | ✅ | |
| `/pf-1-initiate-planner` | ✅ | ✅ | |
| `/pf-2-plan-scope-wbs` | ✅ | ✅ | |
| `/pf-3-plan-schedule` | ✅ | ✅ | |
| `/pf-3b-plan-cost` | ✅ | ✅ | T1 = Lightweight, T2 = Full EVM — both modes covered |
| `/pf-4-plan-risk` | ✅ | ✅ | |
| `/pf-4b-plan-quality` | — | ✅ | Didn't exist yet at T1 |
| `/pf-4c-plan-procurement` | — | ✅ | Didn't exist yet at T1 |
| `/pf-5-plan-stakeholders` | ✅ | ✅ | |
| `/pf-6-plan-organization` | ✅ | ✅ | |
| `/pf-6b-plan-resources` | ✅ | ✅ | |
| `/pf-7-initiate-manager` | ✅ | ✅ | |
| `/pf-8-assign-task` | ✅ | ✅ | |
| `/pf-9-initiate-worker` | ✅ | ✅ | |
| `/pf-10-check-report` | ✅ | ✅ | T2 exercised the QA-gate-fail path inside this command |
| `/pf-11-control-cycle` | ✅ | ✅ | |
| `/pf-12-change-request` | ✅ | ✅ | Both CRs were **Approved** — Rejected/Deferred never tested |
| `/pf-13-handoff` | ⚠️ | — | T1 only wrote the handoff note; a fresh instance actually resuming from it was never simulated |
| `/pf-14-close-project` | ✅ | ✅ | Both closed cleanly with every work package Done |

## Coverage Matrix — Scenarios

| Scenario | Covered? | Where |
|---|---|---|
| Risk triggers mid-execution → Change Request | ✅ | T1 (R-001, technical) |
| QA gate passes cleanly | ✅ | T2 (Videos 1 & 3) |
| QA gate **fails**, vendor rework, re-review passes | ✅ | T2 (Video 2) |
| Make-or-buy analysis concludes "Buy", fixed-price contract | ✅ | T2 |
| Vendor tracked as a non-Worker `Owner` in `tracker.md`/`raci.md` | ✅ | T2 |
| Resource conflict flagged in planning, absorbed by schedule slack | ✅ | T1 (worker-content PTO) |
| Change Request **Approved** | ✅ | T1, T2 |
| Constitution escalation threshold referenced in a real decision | ✅ | T1, T2 |
| Cost/Resource/Quality/Procurement baseline updated via CR | ✅ | T1 (cost), T2 (schedule only, cost explicitly unaffected) |
| Project closes with every work package Done | ✅ | T1, T2 |
| Change Request **Rejected** or **Deferred** | ❌ | Not tested |
| Resource over-allocation that actually blocks (not absorbed by slack) → re-leveling or CR | ❌ | Not tested |
| Cost variance actually **breaching** the control threshold (Yellow/Red cost status) | ❌ | Both runs stayed Green/under budget |
| Quality trend note firing from a **recurring** defect pattern (2+ occurrences) | ❌ | Both runs had only one isolated defect |
| Two or more Workers genuinely in parallel (dispatched before either reports back) | ⚠️ | T1 assigned 2 in parallel but both were simple/independent; never stress-tested a real collision |
| `/pf-13-handoff` actually resumed by a fresh Manager/Worker instance | ❌ | Only the note-writing half was tested |
| Constitution amended mid-project via Change Control | ❌ | Not tested |
| Project closed with an open/incomplete work package (descope or hold) | ❌ | Not tested |
| Re-running `/pf-4-plan-risk` mid-project to add a single new risk | ❌ | Not tested |
| Stakeholder engagement drift detected and reacted to mid-project | ❌ | Not tested |
| Make-or-buy analysis concludes "Make" (kept in-house) | ❌ | T2's only outsourced item was "Buy" |

## Future Test Scenarios (backlog)

Roughly in priority order — pick whichever is most relevant to what's being changed next:

1. **T3 — Rejected/Deferred CR.** A Change Request the Sponsor rejects or defers; verify the
   Project Manager doesn't apply baseline updates and the work package stays blocked correctly.
2. **T4 — Cost breach.** A project where actual cost genuinely breaches the
   `cost-management-plan.md` threshold (Yellow/Red), forcing a real cost-driven CR.
3. **T5 — Resource over-allocation that blocks.** A resource conflict that can't be absorbed by
   slack, forcing genuine re-leveling (add resource / resequence) or a CR.
4. **T6 — Recurring quality defect.** The same defect type across 2+ work packages, so
   `quality-control-log.md`'s Trend Notes actually fire and the Quality Manager flags a process
   issue (not just a one-off).
5. **T7 — Real parallel Workers.** Two Workers genuinely in flight at once across a control
   cycle boundary, to stress-test `tracker.md` update ordering and `/pf-11-control-cycle`'s read.
6. **T8 — Handoff resumption.** Actually simulate a fresh Manager/Worker instance reading
   `tracker.md`'s Handoff Notes / a Worker's memory log and continuing correctly, not just
   writing the note.
7. **T9 — Incomplete closure.** Run `/pf-14-close-project` with a work package still open, and
   verify it correctly asks the user to close it out, descope via CR, or hold closing.
8. **T10 — Constitution amendment.** Amend `constitution.md` mid-project via Change Control and
   verify downstream agents (e.g. Risk Manager's escalation threshold) pick up the new rule.

Each future run should also be added to the Test Runs Log and both Coverage Matrices above.
