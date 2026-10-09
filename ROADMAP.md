# ProjectFabric Roadmap

Governance document tracking what ProjectFabric covers today, what's planned next, and what was
considered and deliberately not pursued. For line-by-line change history see
[CHANGELOG.md](CHANGELOG.md); for the full v1/v2 knowledge-area rationale see
[docs/knowledge-areas.md](docs/knowledge-areas.md).

Status legend: ✅ Done · 🔜 Planned (not started) · ⏸ Deferred (intentionally, for now) ·
❌ Rejected (evaluated, not adopting)

Every feature has a stable **ID** (`KA-`, `INF-`, `GOV-`, `SESS-`, `AGL-`, `WPQ-`, `REP-`, `EXT-`,
`AUT-`) for cross-referencing from `CHANGELOG.md`, commit messages, and Change Requests. IDs are
assigned once and never reused or renumbered, even if a row is later Rejected or removed — a
sub-item of an existing feature gets a decimal suffix (e.g. `INF-08.1`) rather than its own
top-level number.

## Knowledge Area Coverage (PMBOK-style)

| ID | Knowledge Area | Status | Artifact(s) | Owning Agent |
|---|---|---|---|---|
| KA-01 | Integration Management | ✅ Done | `charter.md`, `tracker.md`, status reports, change requests | Project Manager (+ Planner for Charter) |
| KA-02 | Scope Management | ✅ Done | `scope-statement.md`, `wbs.md` | Planner |
| KA-03 | Schedule Management | ✅ Done | `schedule.md` | Planner |
| KA-04 | Cost Management | ✅ Done | `cost-management-plan.md`, `cost-performance.md` (Lightweight or Full EVM mode) | Cost Manager |
| KA-05 | Risk Management | ✅ Done | `risk-register.md` | Risk Manager |
| KA-06 | Stakeholder Management | ✅ Done | `stakeholder-register.md` | Stakeholder Manager |
| KA-07 | Communications Management (partial) | ✅ Done | `communications-plan.md` | Stakeholder Manager |
| KA-08 | Project Organization | ✅ Done | `organization.md` (governance structure, role definitions, team roster of Person / AI / Vendor members, org change log), `raci.md` with roster members as columns. `/pf-setup-organization` builds the structure; `/pf-plan-organization` settles the roster against skill gaps and builds the RACI. Required under classic-waterfall and agile-hybrid, Optional under lean. Governance and roles are baseline; the roster is a living register | Project Manager |
| KA-09 | Resource Management (depth) | ✅ Done | `resource-management-plan.md`, `resource-allocation.md` | Resource Manager |
| KA-10 | Quality Management | ✅ Done | `quality-management-plan.md`, `quality-control-log.md` (QA gate before "Done") | Quality Manager |
| KA-11 | Procurement Management | ✅ Done | `procurement-management-plan.md`, `vendor-contract-register.md` | Procurement Manager |
| KA-12 | Communications Management (full) | 🔜 Planned | `communications-plan.md` (moves from the Stakeholder Manager), `communications-log.md` (new). **v2 Phase 5.** The deferral condition ("if complexity outgrows the Stakeholder Manager") is met because communications and documentation needs are growing. A Communications Manager agent (planning tier) owns both files and the drafts in REP-06; the ownership move needs the Ownership table and Ground Rules updated when built | Communications Manager (planned) |
| KA-13 | Skills Matrix | ✅ Done | `skill-matrix.md`: skills catalog, minimum level per WBS leaf (1-4 scale), team coverage per roster member, and a gap analysis with a proposed action (train, hire, contract, reassign, accept). Built by `/pf-plan-skills`; required under classic-waterfall and agile-hybrid, Optional under lean. Ratings are never invented and are treated as sensitive. `pf_validate.py` checks IDs against the WBS, catalog and roster, and warns on unfilled roles and uncovered requirements | Resource Manager |

## Infrastructure Features

External systems, distribution, data storage/runtime, and backend/UI — the "heavier" category
evaluated against the 11 projects in [docs/Reference.md](docs/Reference.md) (REF-P01 to REF-P11, with
sources and what each informed). Every Rejected entry
here contradicts Design Principle 1 (No infrastructure) or 2 (portable plain-text files) unless
noted otherwise — see [docs/architecture.md](docs/architecture.md#design-principles).

| ID | Feature | Status | Notes |
|---|---|---|---|
| INF-01 | External integration manifest (`.pmo/integrations/`) | 🔜 Planned | **v2 Phase 1.** Record Confluence page IDs/URLs and Jira issue keys locally so external projections are auditable and idempotent while `.pmo/` remains the source of truth. |
| INF-02 | Confluence artifact publishing | 🔜 Planned | **v2 Phase 2.** Publish approved `.pmo/` artifacts into a predictable Confluence project page tree with preserved tables, ownership, status, and links back to local artifacts. First version is explicitly one-way. |
| INF-03 | Jira work-package projection | 🔜 Planned | **v2 Phase 3.** Create and update Jira issues for WBS leaf work packages, retaining the WP ID, acceptance criteria, dependencies, assignee, and local/Jira links. Requires explicit user approval before creating issues. |
| INF-04 | Bidirectional Confluence/Jira synchronization | ⏸ Deferred | Resolve external edits, conflict handling, permissions, deletion, and status mapping only after one-way publication and stable external ID tracking have been validated. |
| INF-04.1 | └ Read-only Jira status drift report | 🔜 Planned | **v2 Phase 3.** Sub-item of INF-04 that does not need conflict handling: pull the status of projected Jira issues and list mismatches against `tracker.md` in the control cycle. Never writes `.pmo/` or Jira; the user decides what to reconcile. |
| INF-05 | MCP server exposing `.pmo/` as tools | ⏸ Deferred | Already an explicit v2 extension point in `docs/architecture.md`. Requires a running server — contradicts Design Principle 1; revisit once v1 knowledge areas are complete. |
| INF-06 | Multi-assistant support (Claude/Cursor folders) | ⏸ Deferred | No second assistant to support yet; revisit if requested. |
| INF-07 | Replacing Markdown artifacts with JSON+schema files (e.g. `wbs.json` + `wbs.schema.json`) | ⏸ Deferred | From REF-P05. Already anticipated as a v2+ "structured data migration" in `docs/architecture.md`'s Extension Points, but not needed now — deterministic validation scripts (see Other Framework Features) can check the existing Markdown tables directly without changing the artifact format or losing "just read the Markdown" readability. |
| INF-08 | Full backend/UI (dashboard, Kanban board, real-time board) | ❌ Rejected | Evaluated via REF-P09, REF-P08 and the dashboard in REF-P05. A future read-only renderer over `.pmo/` remains a valid v2+ idea, but not a priority. |
| INF-08.1 | └ WebSockets / real-time collaboration channels | ❌ Rejected | Sub-item of INF-08, from REF-P09 and REF-P08. Real-time push updates need a persistent connection/server process. |
| INF-08.2 | └ Docker/Kubernetes deployment | ❌ Rejected | Sub-item of INF-08, from REF-P09, REF-P08 and REF-P05. Containerized deployment implies a running service to deploy in the first place. |
| INF-08.3 | └ Domain-specific vertical workflow templates (Publisher/Sales/HR/Security boards) | ❌ Rejected | Sub-item of INF-08, from the template system in REF-P09. ProjectFabric stays PMBOK-generic by design (see `docs/knowledge-areas.md`); vertical/domain templates would be a different, narrower product. |
| INF-09 | Database-backed state (Postgres/SQLite) | ❌ Rejected | Contradicts Design Principle 2 — Markdown + git is the state model by design. |
| INF-09.1 | └ Relational/cache datastores (SQLite/Postgres/Valkey) | ❌ Rejected | Sub-item of INF-09, from REF-P09 and REF-P08, named explicitly per technology considered. Same rationale — Design Principle 2. |
| INF-09.2 | └ ORM-defined relational schema (e.g. SQLAlchemy models) | ❌ Rejected | Sub-item of INF-09, from REF-P09 and REF-P08. Same rationale — Design Principle 2; there is no relational schema to define when state is Markdown tables. |
| INF-09.3 | └ WASM plugin sandboxing | ❌ Rejected | Sub-item of INF-09 / EXT-01, from REF-P08. Only needed when plugins execute untrusted third-party code in an app runtime; the Planned plugin pattern is additive Markdown files with no code execution, so sandboxing doesn't apply. |
| INF-10 | Workflow execution engine / CLI installer (like the CLI installer in REF-P01) | ❌ Rejected | An installed package/engine, not a small on-demand helper script. Copilot-only, manual-copy distribution is intentional; no multi-agent abstraction layer needed at current scope. |
| INF-10.1 | └ git-worktree pooling / isolated parallel execution branches | ❌ Rejected | Sub-item of INF-10, from REF-P02 and REF-P05. Isolated git worktrees per parallel Team Member require an orchestrator process managing them; T7's test run already proved true parallel Team Member dispatch works via plain file state without this. |
| INF-10.2 | └ Autonomous polling/dispatch loop (no user approval per step) | ❌ Rejected | Sub-item of INF-10, from the LangGraph swarm loop in REF-P09. Directly contradicts Design Principle 3 (the user is the checkpoint) instead. |
| INF-10.3 | └ Cryptographic supply-chain attestations (DSSE) | ❌ Rejected | Sub-item of INF-10, from REF-P05. Needs PKI infrastructure and a signing/verification service; ProjectFabric's artifacts aren't code shipped to production, so provenance signing doesn't apply. |
| INF-10.4 | └ Real-time signal/metric ingestion pipeline | ❌ Rejected | Sub-item of INF-10, from REF-P05. Needs a running ingestion service; a periodic `/pf-control-cycle` read of `.pmo/` files is the deliberate lower-tech substitute. |
| INF-10.5 | └ Multi-language script parity (bash/powershell/python triplicates) | ❌ Rejected | Sub-item of INF-10, from REF-P01. Only needed when shipping a cross-platform CLI; Deterministic helper scripts (AUT-01, see Other Framework Features) can target one runtime since they're invoked locally by the agent, not distributed. |
| INF-10.6 | └ Wheel/package asset bundling for offline distribution | ❌ Rejected | Sub-item of INF-10, from REF-P01. Only relevant if ProjectFabric became an installable package; manual folder copy is the intentional distribution model. |
| INF-10.7 | └ Dynamic template rendering engine (Jinja2 + conditional logic) | ❌ Rejected | Sub-item of INF-10, from REF-P01. `templates/*.template.md` use plain Markdown with light variable substitution at most; a full conditional templating engine is unneeded complexity for artifacts a human fills in directly. |
| INF-11 | State in GitHub Issues instead of files (Kanban-as-Issue, label-triggered automation) | ❌ Rejected | From REF-P07. E.g. `tracker.md` becomes a single GitHub Issue whose body is rewritten on every status change, with a GitHub Action watching label changes to auto-trigger the next step. Gains free visibility in GitHub's Projects UI, but contradicts Design Principle 2 and locks the framework to one specific GitHub repo. |
| INF-12 | Observability layer for agent activity (audit trail already covered by existing file-based artifacts — see Governance below) | 🔜 Planned | Two options on the table, not yet chosen between: (a) file-based, no-infrastructure approach — a Ground Rule has every agent self-report one line to `.pmo/logs/agent-activity.jsonl` (timestamp, agent, command, artifact(s) touched, outcome), aggregated on demand by a deterministic helper script (AUT-01) — fits Design Principle 1 since nothing runs unattended, but compliance depends on the model remembering to log each turn; (b) an OpenTelemetry-style exporter for real latency/token/cost metrics — would need a running collector/exporter process, contradicting Design Principle 1, and that data isn't obtainable from inside agent-authored Markdown regardless of exporter choice. Option (a) is compatible with v1's architecture as-is; option (b) would require revisiting Design Principle 1 the same way the deterministic-helper-scripts carve-out did. |
| INF-13 | MCP consumption convention (agents use the user's already-configured Jira/Confluence MCP servers) | 🔜 Planned | **v2 Phase 0.** Foundation for INF-01 to INF-04.1. ProjectFabric ships no MCP server and hard-codes no tool names: the integrating agent lists the user's MCP tools in its `tools:` (exact syntax to be verified in a spike), and a `pf-integration-reference` skill describes the operations abstractly (find/create/update a page or issue) plus the preview → approve → write → record flow and failure handling. Needs a one-paragraph Design Principle 1 clarification in `docs/architecture.md`: consuming a user-configured MCP server adds no ProjectFabric infrastructure. INF-05 (exposing `.pmo/` as an MCP server) is the opposite direction and stays Deferred. |
| INF-14 | Outlook integration through the user's Outlook MCP server | 🔜 Planned | **v2 Phase 5.** Drafts only: status distribution, stakeholder updates and newsletters as *unsent* Outlook drafts, and milestone or sprint-ceremony invites as unsent drafts. Nothing is sent by an agent (Design Principle 3). Recipients come from `communications-plan.md`, and content passes the sensitivity filter (GOV-04). Server-agnostic, like INF-13. |
| INF-15 | Meeting capture from Microsoft Teams | 🔜 Planned | **v2 Phase 5.** Turn Teams meeting transcripts and chat into *proposed* decisions (GOV-02), risks, and actions (GOV-05); the user confirms each one before anything lands in `.pmo/`. It needs a Teams-capable MCP server configured by the user. Transcripts can hold sensitive content, so proposals quote only what they need. |
| INF-16 | Document import with `markitdown` | 🔜 Planned | **v2 Phase 5.** Convert existing Word, PDF, PowerPoint and Excel files to Markdown through a document-conversion MCP server (for example `markitdown`), so a requirements document, RFP or vendor quote can seed `/pf-setup-charter`, `/pf-plan-risk` and `/pf-plan-procurement` instead of being retyped. One-way input: an agent summarizes the converted text with the user; it is never copied into an artifact unreviewed. |
| INF-17 | Git / GitLab version control of `.pmo/` | 🔜 Planned | **v2 Phase 1.** `.pmo/` is plain text, so git already gives history (see the Audit Trail table). This adds conventions: commit when the user approves an artifact or Change Request, tag baselines (for example `baseline-1`, `baseline-CR-001`), put the CR/DEC ID in commit messages, and never push without the user's confirmation. For software projects, optionally link work packages to GitLab issues and merge requests through the user's GitLab MCP server. Not the same as INF-11 (rejected): git versions the files, it does not replace them as the state store. |

## Other Framework Features

Prompt/agent/template-level mechanics that don't require any infrastructure — evaluated against
the same 11 reference repos, grouped by functional area so coverage/gaps per area are scannable
at a glance.

### Governance & Decisions

| ID | Feature | Status | Notes |
|---|---|---|---|
| GOV-01 | Project Constitution (`/pf-setup-project-constitution`) | ✅ Done | Project-specific working rules, decision authority, escalation rules, with the team's defaults and working rules copied in at init — layered on top of framework-wide `copilot-instructions.md`. Inspired by REF-P01. |
| GOV-02 | Decision log (`.pmo/decisions/`, lifecycle draft→signed-off→superseded) | ✅ Done | From the RFC pattern in REF-P05. For judgment calls that aren't scope/schedule/budget changes (so don't need a full Change Request). New `/pf-log-decision` command (pairs with `/pf-change-request`) writes `decisions/DEC-<id>.md` from `templates/decision-record.template.md`; any agent may propose one, Project Manager owns the log. Status lifecycle Draft → Signed-off → Superseded (by a later `DEC-<id>`, never deleted). |
| GOV-03 | Team-level customization layer (`.pmo/team.md`, between framework-wide `copilot-instructions.md` and project-specific `project-constitution.md`) | ✅ Done | From the org/team/project memory layering in REF-P04. `templates/team.template.md` holds Team Defaults (Workflow Preset, cost tracking mode, control cycle cadence, variance/risk thresholds) and Working Rules. The team's `team.md` is created at `/pf-setup-init` pass 1 and must be filled in (Team name, every Team Defaults row, one Working Rule) before pass 2 scaffolds the rest; the script enforces this. `/pf-setup-project-constitution`, `/pf-plan-cost` (cost variance threshold) and `/pf-plan-risk` (risk acceptance ceiling, flag only) read the project's values from the constitution. Precedence is framework Ground Rules → `team.md` → `project-constitution.md`; pass 2 copies the Team Defaults into the constitution's Project Defaults table and the Working Rules into Team Working Rules (the constitution adds Project Working Rules and Exempted Team Working Rules), a changed project value gets its reason in Amendments, and nothing may contradict the Ground Rules. Planner owns it; baselined like `project-constitution.md` once copied in. |
| GOV-04 | Sensitivity labels (Public / Internal / Restricted per artifact) | 🔜 Planned | **v2 Phase 0.** Defaults ship with the framework (for example the stakeholder register is Restricted; risk register, cost and status reports are Internal) and a per-project override table lives in `project-constitution.md`. Publishing (INF-02), newsletters (REP-06) and email drafts (INF-14) filter by label; a Restricted artifact needs the explicit per-publish confirmation already decided for the stakeholder register. Generalizes that decision so it is not a special case. |
| GOV-05 | Issue and action log (`issue-action-log.md`) | 🔜 Planned | **v2 Phase 0.** One table of issues and actions: ID, type, description, owner, due date, status, source, and links to a work package, risk, decision or Change Request. Owned by the Project Manager. Fed by control cycles, standups, sprint-retro action items and meeting capture (INF-15). Today open issues only live inside status reports. The validator checks IDs and links; an overdue-action metric for automation rules needs WPQ-03. |

### Session & Context Management

| ID | Feature | Status | Notes |
|---|---|---|---|
| SESS-01 | Checkpoint/resume hints | ✅ Done | `/pf-start-manager`, `/pf-start-team-member`, `/pf-control-cycle` proactively point to `/pf-session-handoff` before hitting a context limit, not just after. |
| SESS-02 | Handoff protocol | ✅ Done (basic) | `/pf-session-handoff` exists. Lighter than the two-artifact (Handover_File + Handover_Prompt) pattern in REF-P02 and REF-P03 — revisit only if single-prompt handoff proves insufficient in practice. |
| SESS-03 | Memory/session archiving (`.pmo/archives/`, stage summaries) | ✅ Done | From REF-P02. New `/pf-session-archive-stage` (pairs with `/pf-session-handoff`) writes `archives/<stage>/stage-summary.md` from `templates/stage-summary.template.md` and prepares the move of a finished stage's work-package history (WP memory logs, bus task/report files, dated status reports, standup entries) out of the live folders. Only Done (and, with the Agile layer, Accepted) work is archivable; baselines, registers, `changes/`, and `decisions/` are never archived. Agents read the stage summary, not the archived files (Ground Rule 1). The Project Manager runs the `git mv` moves itself after the user approves the list (VS Code also confirms the terminal command); if it can't run commands it hands the block over instead. Nothing is deleted. |

### Agile / Alternate Methodology Track

| ID | Feature | Status | Notes |
|---|---|---|---|
| AGL-01 | Scope/workflow presets (classic-waterfall / agile-hybrid / lean) at `/pf-setup-init` | ✅ Done | From the "scope" concept in REF-P04 — vary which phases/gates run per project size. Preset set in `team.md` (read by `/pf-setup-init` pass 2, no separate question), copied by pass 2 into `project-constitution.md`'s Project Defaults table, defined authoritatively in `docs/knowledge-areas.md#workflow-presets` (Required/Optional per knowledge area per preset). Cost/Quality/Procurement/Resource-depth managers now check the preset first and ask once before planning if Optional; Planner's handoff calls out the preset explicitly. |
| AGL-02 | Agile/Scrum ceremony layer (sprint planning, standup, retro, backlog refinement) | ✅ Done | Alternate track alongside the PMBOK waterfall track, from REF-P06. Built as **core** (not a plugin — considered both, chose core so the ceremony layer is gated by the Workflow Preset like any other phase rather than requiring a separate install step): new `pf-scrum-master` agent owning `sprint-backlog.md`/`standup-log.md`/`retro-log.md`, with 5 new `/pf-agile-*` commands, one per Manager-loop phase — `/pf-agile-sprint-planning`, `/pf-agile-standup`, `/pf-agile-sprint-review`, `/pf-agile-backlog-refinement`, `/pf-agile-sprint-retro`. Engaged by default under agile-hybrid, optional (ask once) under lean, off under classic-waterfall — see `docs/knowledge-areas.md#workflow-presets`. There is no dedicated Product Owner agent — the user plays that role, with Sprint Review (`/pf-agile-sprint-review`) as the ceremony where that acceptance authority is exercised explicitly rather than left implicit. |
| AGL-03 | Kanban Workflow Preset (`kanban`) | 🔜 Planned | **v2 Phase 6.** A further preset beside classic-waterfall, agile-hybrid, lean and pi-cadence: WIP limits recorded in the constitution, `/pf-assign-task` pulls work only while under the limit (overriding batch size), a board script renders columns from `tracker.md` statuses, and rule metrics cover work in progress and blocked-item age. Flow metrics (cycle and lead time) wait for WPQ-03. Whether the Scrum Master agent also coaches Kanban, or a separate flow role is needed, is settled when it is built. |
| AGL-04 | `pi-cadence` Workflow Preset (yearly roadmap, Program Increments, fixed date and flexible scope) | ✅ Done | For a continuing product that plans a year roughly and ships in fixed-length increments. A fourth preset beside classic-waterfall, agile-hybrid and lean, with its own column in the presets table. New artifacts: `roadmap.md` (yearly plan, living, re-planned with a Revision Log row and no Change Request), `pi-plan.md` (one PI: objectives, scope above and below a cut line, ROAM risks, a PI Change Log and the review) and `product-backlog.md`, all owned by the Planner. New commands `/pf-plan-roadmap`, `/pf-plan-pi` (refuses until the previous PI is closed, unless overlap is allowed) and `/pf-close-pi`. Adding a PI's work packages to `wbs.md` and `schedule.md` at `/pf-plan-pi` is planned work, not a Change Request; only moving the PI end date, budget or team is. The iterations inside a PI reuse the Agile ceremony layer. Not run end to end in a live project yet. |
| AGL-04.1 | └ PI Practices (chosen per project in the constitution) | ✅ Done | Sub-item of AGL-04. The constitution's PI Practices section holds the PI length, iteration length and innovation iteration, and a Yes or No for five practices: PI objectives with a confidence vote, WSJF prioritization, a PI review, ROAM risk handling and a PI predictability metric. `/pf-plan-pi` and `/pf-close-pi` run only the practices marked Yes; with all five off the preset is a plain single-team release train. Business value, confidence, Cost of Delay and Job Size come from the user or a named scorer, never from an agent. `pf_rules.py` gained `pi_predictability_pct` and a `--metric` option. ROAM maps onto the existing risk register (Resolved closes a risk; Owned, Accepted and Mitigated stay open). |

### Work Package Lifecycle & Quality Gates

| ID | Feature | Status | Notes |
|---|---|---|---|
| WPQ-01 | Definition of Ready checklist (before Work Package assignment) | ✅ Done | From the Definition of Ready rubrics in REF-P06 and REF-P05. `/pf-assign-task` runs a readiness gate before writing any task, using the Definition of Ready table in `work-package-definitions.md` (seven standard checks that a project can add rows to): testable acceptance criteria, Responsible party plus exactly one Accountable in `raci.md`, inputs/constraints stated, QA gate coverage, assignee not over-allocated, assignee a Confirmed roster member, vendor contract active. A failed check goes back to the owner named in the table's last column (Planner / Project Manager / Quality Manager / Resource Manager / Procurement Manager); the user may waive it, and the result (Passed or Passed with waiver) is recorded in `task.md`'s new Definition of Ready section. `/pf-agile-backlog-refinement`'s Ready flag uses the same checklist minus the predecessors test. The checks are agent-judged; the mechanical ones (RACI one-Accountable, ID consistency) could move into AUT-01. |
| WPQ-02 | Batch/parallel task assignment (`/pf-assign-task` dispatches multiple eligible Team Members in one action) | ✅ Done | From the batch dispatch pattern in REF-P02. `/pf-assign-task` now builds the eligible set (limited to the current sprint if the Agile layer is in use) and, when more than one work package is eligible, offers a batch chosen under independence rules: one work package per Team Member (the earlier by schedule wins, the other stays queued), combined assignee capacity checked against `resource-allocation.md`, and the user asked before anything that looks like it touches the same deliverable runs in parallel. The Definition of Ready (WPQ-01) runs per work package — a failing one drops out without blocking the rest. The whole batch is presented once for approval before any file is written; approving it approves each assignment. Still no autonomous dispatch: the user opens one Team Member conversation per package. T3/T4 had already shown `tracker.md` handles parallel Team Members when dispatched one at a time. |
| WPQ-03 | Structured dates | 🔜 Planned | **v2 Phase 0.** Dates are free text ("Week 3"), which blocks date arithmetic. Keep the week labels working and add a `Project Start Date` (ISO) to the schedule; scripts convert "Week N" to a date and also accept ISO dates in the tracker and schedule. Backward compatible: existing projects keep working. A prerequisite for Jira due dates (INF-03), the Confluence roadmap page (REP-04), a Gantt-style Excel sheet (REP-02), Kanban flow metrics (AGL-03), and date-based automation-rule metrics (AUT-02). |
| WPQ-04 | Definition of Done for a work package | ✅ Done | The standard checks before a work package is set to Done (acceptance criteria met, QA gate passed when a quality plan exists, a complete report) live in a Definition of Done table in `work-package-definitions.md`, next to the Definition of Ready (WPQ-01); the file is owned by the Planner, created by `/pf-setup-init` pass 2 and tailored at `/pf-setup-project-constitution`. A project can add rows or change one with a reason in that file's Amendments. `/pf-check-report` sets Done only when every row passes; the Team Member agent and `/pf-close-project` refer to the table. The user's sprint-review acceptance under the Agile layer comes after Done and is not a row. |

### Reporting & Communication

| ID | Feature | Status | Notes |
|---|---|---|---|
| REP-01 | Structured status-update headers (`## AgentName - ActionType`) | ✅ Done | Trivial consistency win from REF-P07. New Ground Rule 8 in `copilot-instructions.md`: every response that drafts, changes, or reviews an artifact opens with `## <Agent> - <Action>` (Action is one of Drafted / Updated / Reviewed / Flagged / Blocked / Handed off) plus an `Artifacts:` line. Defined once as a Ground Rule so all 10 agents and every future command inherit it without editing each prompt. Compliance is model-followed, like every other Ground Rule. |
| REP-02 | Excel workbook export of `.pmo/` tables | 🔜 Planned | **v2 Phase 4.** One-way export: a generated `.xlsx` with a sheet per artifact (WBS, schedule, tracker, risks, cost performance with live EVM formulas, RACI, decisions, sprint backlog), styled headers, frozen header row, sensible column widths. Decided: a standard-library script in the AUT-01 skill (zip plus hand-written XML), CSV as the fallback, no `openpyxl`. Generated, never hand-edited, never read back. |
| REP-03 | Presentation export (status / steering deck) | 🔜 Planned | **v2 Phase 4.** One-way export with `python-pptx`: a status deck (status colour, accomplishments, top risks, EVM summary, decisions needed, next steps). If the user supplies a `.pptx` template it is filled using that template's layouts; otherwise python-pptx's default is used. `python-pptx` is an optional dependency — the first in ProjectFabric — so the script stops with an install hint when it is missing. |
| REP-03.1 | └ Narration script in speaker notes | 🔜 Planned | **v2 Phase 4.** Sub-item of REP-03: per-slide narration text written into the deck's speaker notes with `python-pptx`, usable for live delivery or for recording a voice-over. Nearly free once REP-03 exists. |
| REP-03.2 | └ Voice-over audio and video | ⏸ Deferred | Sub-item of REP-03. Needs a text-to-speech engine and video assembly (external engines, credentials and cost), which strains Design Principle 1. Revisit only with a concrete need. |
| REP-04 | Confluence page designer skill (`pf-confluence-design`) | 🔜 Planned | **v2 Phase 2.** A core skill that turns `.pmo/` into designed Confluence pages: project home, status, roadmap from the schedule, and risk board. Page structure comes from `.pmo/`; look comes from a theme slot with a neutral default. When the user has a styling skill installed (for example a company design-system skill) it is used as the theme — read, never copied or forked. Needs a fallback for sites where the `{html}` macro is disabled. |
| REP-05 | MARP deck export (no dependency) | ⏸ Deferred | Planned for later by choice. A dependency-free alternative to REP-03: generate MARP Markdown so the deck stays diffable, exported with the Marp CLI when available. |
| REP-06 | Newsletter, blog post and announcement drafts | 🔜 Planned | **v2 Phase 5.** Drafts per audience from `.pmo/`, driven by `communications-plan.md` (audience, format, frequency). Redaction follows the sensitivity labels (GOV-04): stakeholder attitudes, internal risk detail and cost figures never reach a broad audience. Delivery is a Confluence blog post (INF-02, REP-04) or an unsent Outlook draft (INF-14). Drafts only, logged in `communications-log.md`. |
| REP-07 | Technical Writer agent | 🔜 Planned | **v2 Phase 6.** An execution-tier agent, like the Team Member, for documentation work packages: user guides, runbooks, handover material, release notes, polishing the final report. Owns a project `style-guide.md` (voice, glossary, templates) and uses the Confluence designer skill (REP-04). Documentation is not a PMBOK knowledge area, so it is listed here rather than under Knowledge Area Coverage. |
| REP-08 | Portfolio roll-up (read-only multi-project summary) | ⏸ Deferred | Deferred until a second real project exists. A script reads a list of project paths and prints one row per project (status colour, % done, CPI/SPI, top open risk, blocked count, next milestone, open decisions and Change Requests), plus cross-project views: people on several projects, total budget against spend, and off-track projects. Output can go to Excel (REP-02) or a Confluence page (REP-04). Limits: only as fresh as each project's last control cycle, cost modes and thresholds may not be comparable across projects, and it may show only what each project's sensitivity labels (GOV-04) allow. Needs WPQ-03 and GOV-04 first, both already planned. |
| REP-09 | Portfolio Manager agent | ⏸ Deferred | Partner of REP-08, deferred with it. Owns the portfolio file (the list of projects and the roll-up), which closes the one-artifact-one-owner gap a user-owned file would leave. Read-only toward each project's `.pmo/`: it never writes into a project. Whether it is a full agent or a command run from a chosen project is decided when built. |
| REP-10 | User guides | ✅ Done | `docs/guides/`: getting started tutorial (two reader tracks: new to project management, experienced project manager), how a project runs (concepts and glossary), eleven situation scenarios with what you provide and what you get, an artifact reference, and a command reference. The command tables are generated by `tools/gen_command_reference.py` from the prompt files plus the hand-written `command-notes.md` (when to run, what you provide, what you get), with preset columns read from the Workflow Presets table, and `--check` keeps them current. `docs/example/` holds a filled-in fictional project (a company offsite with a Person, an AI, and a Vendor member) that validates with `pf_validate.py`. The root README is now a pitch, an index, and a short quick start. |
| REP-10.1 | └ Recipes, troubleshooting and FAQ, customising and extending guide | 🔜 Planned | Sub-item of REP-10. Recipes can be written from the prompts now. Troubleshooting and FAQ entries should come from problems seen in real runs, so they follow the first live run of the Project Organization flow. Write each guide as soon as its source material exists, without waiting for the others. |
| REP-10.2 | └ One-page cheat sheet, guide for sponsors and stakeholders, guide for team members, integration guides | 🔜 Planned | Sub-item of REP-10. The first three need no new features. An integration guide (Confluence, Jira, Office exports) is written in the same change that builds its integration, so no integration ships without one. |

### Extensibility & Customization

| ID | Feature | Status | Notes |
|---|---|---|---|
| EXT-01 | Plugin/extension pattern (`plugins/<name>/` additive, untouched core) | ✅ Done | `plugins/README.md` documents the convention: `.pf-plugin/plugin.json` manifest declaring contributed `agents/`, `prompts/`, `templates/`; install = copy files into core dirs, uninstall = delete them, core stays byte-identical. No plugin installer script yet — AUT-01's scripts cover `.pmo/` scaffolding, not plugin install — so install/uninstall is manual for now. `templates/catalog.json` for discovery remains a follow-up once a real plugin exists to list. |
| EXT-02 | Agent frontmatter `tools:` allow-list + plain-language Tier statement | ✅ Done | Corrected from the original "tier + `disallowedTools`" idea, which was based on a convention in REF-P04, not VS Code's real custom-agent schema. VS Code agents use a real `tools:` allow-list (not a deny-list) — all 10 agents declare `tools: [read, edit, search]`; Team Member, Cost Manager, and Project Manager add `execute` (Team Member to do its task; the other two to run the AUT-01 helper scripts, where the VS Code terminal-confirmation prompt keeps the user as the checkpoint), and each agent's body opens with a **Tier:** line (Judgment for the 9 planning/managing agents, Execution for Team Member) for role clarity. |
| EXT-03 | Skills layer (`.github/skills/<name>/SKILL.md`) | ✅ Done | Evaluated the 9 agents that existed at the time (the later Scrum Master has not been evaluated) for dense, on-demand reference material worth extracting (vs. core judgment logic needed every invocation, which stays inline). 8 skills built, one per agent that had a genuine candidate: `pf-evm-reference` (Cost Manager — EVM formulas), `pf-critical-path-reference` (Planner — CPM forward/backward pass), `pf-risk-identification-reference` (Risk Manager — elicitation techniques + P/I scale anchors), `pf-quality-audit-reference` (Quality Manager — QA/QC checklists + metrics catalog), `pf-contract-type-reference` (Procurement Manager — Fixed-Price/T&M/Cost-Reimbursable selection guide), `pf-resource-leveling-reference` (Resource Manager — leveling/smoothing/fast-tracking/crashing), `pf-stakeholder-engagement-reference` (Stakeholder Manager — quadrant tactics + Salience model), `pf-raci-facilitation-reference` (Project Manager — workshop steps + anti-patterns + RASCI/DACI variants). Team Member was evaluated and correctly excluded — execution guidance is task-specific, not universal reference material. Each owning agent's body now has a one-line pointer to its skill. A ninth skill, `pf-helper-scripts` (AUT-01), bundles runnable scripts rather than reference text. |

### Automation & Tooling

| ID | Feature | Status | Notes |
|---|---|---|---|
| AUT-01 | Deterministic helper scripts (EVM math, WBS 100%-rule / RACI one-A / cross-file ID validation, `/pf-setup-init` template scaffolding, backlog/artifact drift detection) | ✅ Done | Explicitly encouraged by Design Principle 1. Shipped as a ninth skill, `.github/skills/pf-helper-scripts/` (Python 3.9+, standard library only, so it travels with the `.github/` copy), holding three scripts an agent runs on demand (a fourth, `pf_rules.py`, was added for AUT-02): `pf_evm.py` (Full EVM tables and rollup in `cost-performance.md`'s shape), `pf_validate.py` (read-only checks: WBS Hierarchy vs Dictionary, one Accountable per RACI row, risk Score = P x I and sort order, tracker IDs and linked `R-`/`CR-` IDs, `bus/` task files vs tracker, sprint backlog IDs), and `pf_scaffold.py` (creates `.pmo/`, never overwrites, applies `--preset` and `--team`). Wired into Cost Manager (EVM), Project Manager (validate at each `/pf-control-cycle`), and `/pf-setup-init`. Both agents gained `execute` in their `tools:`; without Python or a terminal they fall back to the manual method. Checked against all three sandbox projects (it found a real unsorted risk register in `datacenter-migration`) and a deliberately broken fixture. Not built: auto-fixing or re-sorting files (the scripts only report), a plugin installer, and Lightweight-mode cost arithmetic. Never runs unattended and never decides — Status colors and every judgment stay with the agent and user. |
| AUT-02 | Trigger-action automation rules (human-authored flag rules, e.g. "if cost overrun > threshold then flag for CR") | ✅ Done | From the event-driven workflow engine in REF-P08, scaled down to fit Design Principle 1: nothing is event-driven or unattended. Rules live in `.pmo/automation-rules.md` (`templates/automation-rules.template.md`), a Markdown table of `Condition` (`<metric> <operator> <number>`), `Flag Message`, `Suggest`ed command, and `Enabled`; the Project Manager owns the file, the user writes the rules and picks the numbers. `pf_rules.py` (in the AUT-01 `pf-helper-scripts` skill) computes eight metrics from `.pmo/` — `blocked_wp_count`, `done_pct`, `open_risk_count`, `open_risk_max_score`, `cost_overrun_pct_max` (Lightweight), `cpi_min`/`spi_min` (Full EVM), `draft_decision_count` — and reports which enabled rules are TRIGGERED. It runs at step 8 of each `/pf-control-cycle`, after the cost, resource, quality, and procurement data are refreshed; a triggered rule only appears in the Status Report with its suggested command, which the user decides on. The shipped example rows are all disabled, so default behavior is unchanged. Deviates from the original `.pmo/automation.yml` idea: YAML can't be parsed with the standard library and Design Principle 2 says state is plain Markdown tables. Not built: schedule-date metrics (dates are free text like "Week 3"), stakeholder/resource metrics, and rules that take actions. |
| AUT-03 | Embedding-based routing / iterative LLM evaluator loops | ❌ Rejected | From REF-P10. E.g. the user types "I'm worried about vendor risk" instead of `/pf-plan-risk`, and a routing layer embeds the request plus each agent's capability description and picks the closest match automatically. Design Principle 3 (the user is the checkpoint) already provides the quality gate; the added LLM cost per turn and the new misrouting failure mode (e.g. a cost question routed to the Risk Manager) aren't justified. |

## Version 2 Plan (decisions made, not built)

Theme: connect `.pmo/` to the tools stakeholders already use — Jira, Confluence, Excel, PowerPoint —
without making any of them a source of truth. `.pmo/` stays authoritative, every external write is
previewed and approved, and nothing runs unattended. Requested capabilities map onto it:
MCP integration for Jira and Confluence (INF-13, INF-01, INF-03, INF-04.1), Excel and presentation
creation (REP-02, REP-03), Confluence publishing with a designed look (INF-02, REP-04), and a
communications and documentation layer (KA-12, REP-06, REP-07, INF-14 to INF-16) with the
foundations it needs (WPQ-03, GOV-04, GOV-05), plus git version control (INF-17) and a Kanban
preset (AGL-03).

### Remaining backlog, reviewed 2026-09-30

| Item | Status | v2 disposition |
|---|---|---|
| INF-01, INF-02, INF-03 | 🔜 Planned | The core of v2 (Phases 1-3) |
| INF-04 bidirectional sync | ⏸ Deferred | Stays deferred; its read-only part is INF-04.1 |
| INF-05 `.pmo/` as an MCP server | ⏸ Deferred | Stays deferred; it is the opposite direction to INF-13 |
| INF-06 multi-assistant, INF-07 JSON schemas | ⏸ Deferred | No change; INF-07 only matters if Excel import is ever added |
| INF-12 observability | 🔜 Planned | Independent of v2; option (a) vs (b) still undecided |
| KA-12 full Communications | 🔜 Planned | Now planned for Phase 5: the trigger (growing communications and documentation needs) is met |
| Loose ends | — | Scrum Master skill evaluation (EXT-03); AUT-01's not-built items; the untested scenarios in `docs/test-plan.md` |

### Design Principle impact

- **1 (No infrastructure):** consuming MCP servers the user has configured is not ProjectFabric infrastructure, but the clarification must be written into `docs/architecture.md` when INF-13 is built. The Excel export follows AUT-01 (on-demand script, standard library). The PowerPoint export uses `python-pptx`, which makes it the **first optional package dependency**: it needs an explicit carve-out in `docs/architecture.md` and in the `pf-helper-scripts` skill's "standard library only" statement — optional, imported by that one script only, and failing with an install hint rather than breaking anything else.
- **2 (Portable plain text):** Jira and Confluence are projections. The link between them and `.pmo/` is a Markdown table (INF-01), not a database.
- **3 (User is the checkpoint):** every external write is previewed first (titles, fields, and a diff against the last publish) and needs approval. No background sync. Email is only ever drafted, never sent; git commits follow user approval and nothing is pushed without confirmation.
- **4 (One owner):** the Project Manager owns `integrations/manifest.md` and the generated `exports/`; exports are regenerated, never hand-edited. New owned artifacts: `communications-log.md` (Communications Manager), `issue-action-log.md` (Project Manager), `style-guide.md` (Technical Writer).
- **5 (Extend by addition):** decided — everything ships in core (decision 1). The company-specific styling stays in whatever separate styling skill or plugin the user installs, and is used, not copied.

### Phases

Tracks A (Atlassian) and B (Office) are independent, and Track B needs no external account, so it can start first and is the easiest to test. Phases 5 and 6 depend on the Phase 0 foundations, and Confluence blog posts in Phase 5 also depend on Phase 2.

| Phase | Track | Features | What gets built | Exit check |
|---|---|---|---|---|
| 0 | All | INF-13, WPQ-03, GOV-04, GOV-05 | Foundations first: structured dates, sensitivity labels and the issue/action log (see their rows). MCP spike: confirm how MCP tools are named in an agent's `tools:`, list what the user's configured Jira, Confluence, Outlook, Teams and document-conversion MCP servers expose. Then the `pf-integration-reference` skill, the preview/approve/record flow, and the architecture clarification | One read-only call (fetch a page, fetch an issue) succeeds from an agent; the validator understands ISO dates, labels and the issue log |
| 1 | A | INF-01, INF-17 | `templates/integration-manifest.template.md` → `.pmo/integrations/manifest.md`: local reference, system, external ID/URL, content hash at last publish, approved by/date, plus a Bindings section naming which MCP tools were used. A `pf_validate.py` check for orphan references and duplicate external IDs. INF-17 (git conventions for `.pmo/`, independent of any MCP server) ships alongside | Manifest validates; a changed artifact is detected by hash |
| 2 | A | INF-02, REP-04 | `/pf-publish-confluence`: one-way page tree (project home, charter, scope, WBS, schedule, risks, decisions, status reports), styled by the `pf-confluence-design` skill (REP-04). Preview → approval → create/update → record IDs. The stakeholder register is published only after explicit confirmation each time, following a preview that warns about its sensitivity (decision 6). Never deletes pages | A sandbox project publishes, is edited, re-publishes, and only the changed pages update; every page type renders in the target Confluence |
| 3 | A | INF-03, INF-04.1 | `/pf-publish-jira`: a mapping proposal (deliverable → Epic, work package → Task, dependencies → issue links, acceptance criteria → description, roster member → assignee through a user-supplied map, sprint backlog → Jira sprint when the Agile layer is on), then preview → approval → write → record keys. A read-only status pull joins `/pf-control-cycle` as drift lines | Keys recorded for every leaf; a status change in Jira shows up as a drift line, not an edit |
| 4 | B: Office | REP-02, REP-03, REP-03.1 | `/pf-export-office`: a standard-library XLSX writer, and a `python-pptx` deck script that fills a user-supplied `.pptx` template when one is given (and uses python-pptx's built-in default otherwise). Both write to `exports/`; the deck also gets a narration script in its speaker notes (REP-03.1) | Workbook opens in Excel without a repair prompt and its EVM formulas agree with `pf_evm.py`; the deck opens in PowerPoint and follows the supplied template |
| 5 | C: Communications | KA-12, REP-06, INF-14, INF-15, INF-16 | The Communications Manager agent and `communications-log.md`; newsletter, blog and announcement drafts filtered by sensitivity label; unsent Outlook drafts and invites; Teams meeting capture into proposed decisions, risks and actions; `markitdown` import to seed artifacts from existing documents | A sandbox project produces a newsletter for two audiences with nothing restricted leaking, an unsent email draft, and a meeting transcript turned into confirmed log entries |
| 6 | D: Flow and documentation | AGL-03, REP-07 | The Kanban preset (WIP limits, board script, flow metrics once WPQ-03 is in) and the Technical Writer agent with its `style-guide.md` | A kanban-preset project respects its WIP limit; a documentation work package is written to the style guide |
| 7 | — | INF-04, INF-12, REP-05, REP-03.2, REP-08, REP-09 | Decide only after Phases 1-6 have run on real projects. REP-05 (MARP deck, no dependency), REP-03.2 (voice-over audio), and REP-08/REP-09 (portfolio roll-up and its agent, until a second real project exists) are deferred by choice | — |

Command names `/pf-publish-*` and `/pf-export-office` are proposals; they follow the
`/pf-<category>-<action>` rule in the Governance section.

### Decisions (resolved 2026-09-30)

1. **Packaging: core.** The manifest, publishing flow, Jira projection, Excel/PowerPoint export and the Confluence designer all ship in core. The designer is a skill, not a fork of anyone's plugin.
2. **Excel: standard-library XLSX writer**, CSV as fallback. No `openpyxl`.
3. **PowerPoint: `python-pptx` now**, able to fill a template supplied by the user. The MARP deck (no dependency) is planned for later as REP-05.
4. **Jira mapping: Epic per deliverable, Task per work package.**
5. **Confluence: publish, with a designed look.** The designer generates styled pages from `.pmo/` (project home, status, roadmap from the schedule, risk board) and has a theme slot. A neutral theme is the default; when the user has a styling skill installed, use it as the theme. Reading Confluence pages as inputs stays deferred.
6. **Stakeholder register: publishable only when the user explicitly confirms each time, after a preview that warns about its sensitivity.** Not part of any default publish, and no sanitized variant for now. This is now the general rule for Restricted artifacts (GOV-04).
7. **Outlook: drafts only.** Status, updates, newsletters and meeting invites are created unsent; an agent never sends email (INF-14).
8. **Meeting capture uses Microsoft Teams** (INF-15).
9. **`markitdown` import is added** (INF-16).
10. **Git and GitLab version `.pmo/`** (INF-17); for software projects GitLab issues and merge requests can be linked to work packages.
11. **Approved:** Kanban as a preset (AGL-03); newsletter, blog and announcement drafts (REP-06); voice-over as a narration script now and audio deferred (REP-03.1, REP-03.2); a Communications Manager and a Technical Writer agent (KA-12, REP-07).
12. **Approved foundations:** structured dates (WPQ-03), sensitivity labels (GOV-04), issue and action log (GOV-05).
13. **Deferred:** a portfolio roll-up across several projects (REP-08) and a Portfolio Manager agent (REP-09), until a second real project exists.

### Risks and constraints

- **Server-agnostic design.** Teams use different MCP servers with different tool names, so operations are described abstractly and the concrete tool names live in the manifest's Bindings section.
- **Fidelity.** Converting Markdown tables to Confluence format can lose merged cells and macros. Drift: if a page was edited in Confluence since the last publish, stop and report instead of overwriting.
- **Sensitive data.** The stakeholder register is published only after explicit confirmation each time, no credentials ever enter the repo, and assignee mappings are user-supplied.
- **Partial failure.** A batch of creates can stop midway; the manifest records what succeeded so a re-run resumes instead of duplicating.
- **Hand-written XLSX XML** may make Excel show a repair prompt if anything is off. The fallback is CSV.
- **`python-pptx` is an optional dependency.** Without it the deck command must stop with a clear install hint; it must never block the Excel export or any other command. A user's template may lack the layouts the script expects, so the script falls back to a default layout and reports which it used.
- **The Confluence `{html}` macro is often disabled** on company sites. The designer needs a fallback that uses only standard Confluence formatting, and the preview should say which mode a page will use.
- **The company theme is optional.** The designer must work with its neutral theme when no styling skill is installed.
- **Tools may be missing in a session.** Commands must say so and stop cleanly, not guess.
- **MCP server availability varies.** Each integration checks that the server it needs is configured and stops with a clear message when it is not; nothing is assumed to be installed.
- **Meeting transcripts are sensitive.** Proposals quote only what they need, the user confirms each entry, and nothing from a transcript is published under a label above its source.
- **Git safety.** Agents commit only after the user approves, never force-push or rewrite history, and never push without confirmation.
- **Ownership changes.** Moving `communications-plan.md` to a new agent, and adding three owned artifacts, each need the Ownership table and Ground Rules updated in the same change.
- **Agent count.** Two more agents take the framework from 10 to 12; each new agent needs the same static-audit and lifecycle coverage as the existing ones.

### How v2 will be tested

- Scripts: like AUT-01 — real sandbox data plus planted defects. The XLSX is checked by unzipping and parsing every part, re-reading it with a second reader, and finally by someone opening it in Excel, which automated checks cannot cover.
- Atlassian: the dry-run preview is the testable artifact in a sandbox. Live writes only against a throwaway Jira project and Confluence space the user names, approving each write. Logged as lifecycle run T6 in `docs/test-plan.md`, alongside a refreshed static audit.

## Next Up

The core PMBOK-style knowledge-area kit is now complete (Integration, Scope, Schedule, Cost,
Risk, Quality, Procurement, Resource, Stakeholder, partial Communications, Organization). Next:

1. The "Other Framework Features" backlog is now clear: every item is Done or Rejected. New ideas
   go through the same reference-repo evaluation against the Design Principles before they are
   added. Still open elsewhere: the Infrastructure items marked Planned or Deferred.
2. Version 2: see the **Version 2 Plan** above (decisions are made). Start with Phase 0 (structured
   dates, sensitivity labels, issue/action log, MCP spike) and Phase 4 (Office exports), which are
   independent of each other.
3. Full Communications Management (dedicated agent) remains deferred until Stakeholder Manager's
   scope genuinely outgrows what one agent can own; revisit after Confluence publishing ships.
4. Close the remaining test gaps listed in `docs/test-plan.md` (lean and classic-waterfall runs,
   same team member batch queuing, the archive refusal path, an installed plugin).

## Governance

- One artifact, one owner — see the Artifact Ownership table in
  [.github/copilot-instructions.md](.github/copilot-instructions.md).
- Baseline documents (`charter.md`, `wbs.md`, `schedule.md`, `cost-management-plan.md`,
  `resource-management-plan.md`, `quality-management-plan.md`, `procurement-management-plan.md`,
  `project-constitution.md`, `team.md`) change only through `/pf-change-request`, never by direct edit, once
  approved.
- New commands are named `/pf-<category>-<action>` (categories: `setup`, `plan`, `agile`,
  `session`, `publish`, `export`). The work-loop commands keep a plain verb (`start`, `assign`,
  `check`, `control`, `change`, `log`, `close`). Command names are stable once released.
- New knowledge areas get a dedicated agent + template(s) + a `/pf-plan-*` prompt, and must be wired
  into `copilot-instructions.md`, `docs/knowledge-areas.md`, `README.md`, and
  `docs/architecture.md` in the same change.
- External systems such as Confluence and Jira are projections of approved `.pmo/` state, not
  competing sources of truth; integrations must retain stable external IDs and require user
  approval before creating or changing external records.
- Every entry in the Infrastructure Features and Other Framework Features tables above is
  evaluated against the five Design Principles in
  [docs/architecture.md](docs/architecture.md#design-principles) (No infrastructure, State lives
  in portable plain-text files, The user is the checkpoint, One artifact one owner,
  Extensibility & customization by addition never modification) — cite these directly rather
  than re-deriving the rationale each time.
- Feature IDs (`KA-`, `INF-`, `GOV-`, `SESS-`, `AGL-`, `WPQ-`, `REP-`, `EXT-`, `AUT-`) are
  permanent once assigned — never renumber or reuse one, even for a Rejected/removed row; a new
  feature always gets the next unused number in its prefix, and a sub-item gets a decimal suffix
  off its parent (e.g. `INF-08.1`).
- This file and `CHANGELOG.md` are both updated in the same turn as any change to this repo.

### Audit Trail

No dedicated audit-log artifact exists — "what changed and why" is reconstructable today across
several existing mechanisms (distinct from `INF-12`'s agent-activity *telemetry*, which doesn't
exist yet):

| Mechanism | What it records |
|---|---|
| Git history (implicit — every `.pmo/` file is plain Markdown) | Every edit, diffable and timestamped by commit; the most complete trail, free by virtue of Design Principle 2 |
| `changes/CR-<id>.md` | Every scope/schedule/budget/resource baseline change, with impact analysis |
| `project-constitution.md`'s Amendments table | Date / Change / Approved By for constitution edits |
| `memory/work-packages/WP-<id>.md` | Team Member's running log of decisions, deviations, blockers per work package |
| `tracker.md`'s Variance Notes | Why actual diverged from planned, per work package |
| `reports/status-<date>.md` | Dated status snapshots at each control cycle |
| `quality-control-log.md`, `vendor-contract-register.md` | QA gate pass/fail history, contract variance history |
| `standup-log.md` / `retro-log.md` (Agile ceremony layer) | Append-only, dated ceremony entries |
| `decisions/DEC-<id>.md` (`GOV-02`) | Judgment calls that aren't scope/schedule/budget changes, with lifecycle Draft → Signed-off → Superseded |
| `archives/<stage>/stage-summary.md` (`SESS-03`) | Per-stage outcome, decisions/CRs raised, and an index of every file moved out of the live folders — originals preserved, nothing deleted |
