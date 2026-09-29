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
| KA-08 | Project Organization | ✅ Done | `raci.md` | Project Manager |
| KA-09 | Resource Management (depth) | ✅ Done | `resource-management-plan.md`, `resource-allocation.md` | Resource Manager |
| KA-10 | Quality Management | ✅ Done | `quality-management-plan.md`, `quality-control-log.md` (QA gate before "Done") | Quality Manager |
| KA-11 | Procurement Management | ✅ Done | `procurement-management-plan.md`, `vendor-contract-register.md` | Procurement Manager |
| KA-12 | Communications Management (full) | ⏸ Deferred | Dedicated agent if complexity outgrows Stakeholder Manager | — |

## Infrastructure Features

External systems, distribution, data storage/runtime, and backend/UI — the "heavier" category
evaluated against 10 reference multi-agent PM/SDLC repos and GitHub Spec Kit (see
`/memories/repo/reference-repos-comparison.md` for full research notes). Every Rejected entry
here contradicts Design Principle 1 (No infrastructure) or 2 (portable plain-text files) unless
noted otherwise — see [docs/architecture.md](docs/architecture.md#design-principles).

| ID | Feature | Status | Notes |
|---|---|---|---|
| INF-01 | External integration manifest (`.pmo/integrations/`) | 🔜 Planned | Record Confluence page IDs/URLs and Jira issue keys locally so external projections are auditable and idempotent while `.pmo/` remains the source of truth. |
| INF-02 | Confluence artifact publishing | 🔜 Planned | Publish approved `.pmo/` artifacts into a predictable Confluence project page tree with preserved tables, ownership, status, and links back to local artifacts. First version is explicitly one-way. |
| INF-03 | Jira work-package projection | 🔜 Planned | Create and update Jira issues for WBS leaf work packages, retaining the WP ID, acceptance criteria, dependencies, assignee, and local/Jira links. Requires explicit user approval before creating issues. |
| INF-04 | Bidirectional Confluence/Jira synchronization | ⏸ Deferred | Resolve external edits, conflict handling, permissions, deletion, and status mapping only after one-way publication and stable external ID tracking have been validated. |
| INF-05 | MCP server exposing `.pmo/` as tools | ⏸ Deferred | Already an explicit v2 extension point in `docs/architecture.md`. Requires a running server — contradicts Design Principle 1; revisit once v1 knowledge areas are complete. |
| INF-06 | Multi-assistant support (Claude/Cursor folders) | ⏸ Deferred | No second assistant to support yet; revisit if requested. |
| INF-07 | Replacing Markdown artifacts with JSON+schema files (e.g. `wbs.json` + `wbs.schema.json`) | ⏸ Deferred | From ai-sdlc. Already anticipated as a v2+ "structured data migration" in `docs/architecture.md`'s Extension Points, but not needed now — deterministic validation scripts (see Other Framework Features) can check the existing Markdown tables directly without changing the artifact format or losing "just read the Markdown" readability. |
| INF-08 | Full backend/UI (dashboard, Kanban board, real-time board) | ❌ Rejected | Evaluated via agent-scrum, paca, ai-sdlc dashboard. A future read-only renderer over `.pmo/` remains a valid v2+ idea, but not a priority. |
| INF-08.1 | └ WebSockets / real-time collaboration channels | ❌ Rejected | Sub-item of INF-08, from agent-scrum & paca. Real-time push updates need a persistent connection/server process. |
| INF-08.2 | └ Docker/Kubernetes deployment | ❌ Rejected | Sub-item of INF-08, from agent-scrum, paca & ai-sdlc. Containerized deployment implies a running service to deploy in the first place. |
| INF-08.3 | └ Domain-specific vertical workflow templates (Publisher/Sales/HR/Security boards) | ❌ Rejected | Sub-item of INF-08, from agent-scrum's template system. ProjectFabric stays PMBOK-generic by design (see `docs/knowledge-areas.md`); vertical/domain templates would be a different, narrower product. |
| INF-09 | Database-backed state (Postgres/SQLite) | ❌ Rejected | Contradicts Design Principle 2 — Markdown + git is the state model by design. |
| INF-09.1 | └ Relational/cache datastores (SQLite/Postgres/Valkey) | ❌ Rejected | Sub-item of INF-09, from agent-scrum & paca, named explicitly per technology considered. Same rationale — Design Principle 2. |
| INF-09.2 | └ ORM-defined relational schema (e.g. SQLAlchemy models) | ❌ Rejected | Sub-item of INF-09, from agent-scrum & paca. Same rationale — Design Principle 2; there is no relational schema to define when state is Markdown tables. |
| INF-09.3 | └ WASM plugin sandboxing | ❌ Rejected | Sub-item of INF-09 / EXT-01, from paca. Only needed when plugins execute untrusted third-party code in an app runtime; the Planned plugin pattern is additive Markdown files with no code execution, so sandboxing doesn't apply. |
| INF-10 | Workflow execution engine / CLI installer (à la Spec Kit's `specify` CLI) | ❌ Rejected | An installed package/engine, not a small on-demand helper script. Copilot-only, manual-copy distribution is intentional; no multi-agent abstraction layer needed at current scope. |
| INF-10.1 | └ git-worktree pooling / isolated parallel execution branches | ❌ Rejected | Sub-item of INF-10, from APM & ai-sdlc. Isolated git worktrees per parallel Worker require an orchestrator process managing them; T7's test run already proved true parallel Worker dispatch works via plain file state without this. |
| INF-10.2 | └ Autonomous polling/dispatch loop (no user approval per step) | ❌ Rejected | Sub-item of INF-10, from agent-scrum's LangGraph swarm loop. Directly contradicts Design Principle 3 (the user is the checkpoint) instead. |
| INF-10.3 | └ Cryptographic supply-chain attestations (DSSE) | ❌ Rejected | Sub-item of INF-10, from ai-sdlc. Needs PKI infrastructure and a signing/verification service; ProjectFabric's artifacts aren't code shipped to production, so provenance signing doesn't apply. |
| INF-10.4 | └ Real-time signal/metric ingestion pipeline | ❌ Rejected | Sub-item of INF-10, from ai-sdlc. Needs a running ingestion service; a periodic `/pf-11-control-cycle` read of `.pmo/` files is the deliberate lower-tech substitute. |
| INF-10.5 | └ Multi-language script parity (bash/powershell/python triplicates) | ❌ Rejected | Sub-item of INF-10, from Spec Kit. Only needed when shipping a cross-platform CLI; Deterministic helper scripts (AUT-01, see Other Framework Features) can target one runtime since they're invoked locally by the agent, not distributed. |
| INF-10.6 | └ Wheel/package asset bundling for offline distribution | ❌ Rejected | Sub-item of INF-10, from Spec Kit. Only relevant if ProjectFabric became an installable package; manual folder copy is the intentional distribution model. |
| INF-10.7 | └ Dynamic template rendering engine (Jinja2 + conditional logic) | ❌ Rejected | Sub-item of INF-10, from Spec Kit. `templates/*.template.md` use plain Markdown with light variable substitution at most; a full conditional templating engine is unneeded complexity for artifacts a human fills in directly. |
| INF-11 | State in GitHub Issues instead of files (Kanban-as-Issue, label-triggered automation) | ❌ Rejected | From ai-scrum-master-template. E.g. `tracker.md` becomes a single GitHub Issue whose body is rewritten on every status change, with a GitHub Action watching label changes to auto-trigger the next step. Gains free visibility in GitHub's Projects UI, but contradicts Design Principle 2 and locks the framework to one specific GitHub repo. |

## Other Framework Features

Prompt/agent/template-level mechanics that don't require any infrastructure — evaluated against
the same 11 reference repos, grouped by functional area so coverage/gaps per area are scannable
at a glance.

### Governance & Decisions

| ID | Feature | Status | Notes |
|---|---|---|---|
| GOV-01 | Project Constitution (`/pf-0b-constitution`) | ✅ Done | Project-specific principles, decision authority, reporting cadence, escalation rules — layered on top of framework-wide `copilot-instructions.md`. Inspired by GitHub Spec Kit. |
| GOV-02 | Decision log (`.pmo/decisions/`, lifecycle draft→signed-off→superseded) | 🔜 Planned | From ai-sdlc RFC pattern. For judgment calls that aren't scope/schedule/budget changes (so don't need a full Change Request). |
| GOV-03 | Team-level customization layer (`.pmo/team.md`, between framework-wide `copilot-instructions.md` and project-specific `constitution.md`) | 🔜 Planned | From aidlc-workflows' org/team/project memory layering (ProjectFabric currently only has the org and project layers). Useful for an organization running many ProjectFabric projects that wants shared team standards (e.g. "our team always uses Full EVM") without editing every project's `constitution.md` individually. Low priority until someone is actually running multiple concurrent ProjectFabric projects. |

### Session & Context Management

| ID | Feature | Status | Notes |
|---|---|---|---|
| SESS-01 | Checkpoint/resume hints | ✅ Done | `/pf-7`, `/pf-9`, `/pf-11` proactively point to `/pf-13-handoff` before hitting a context limit, not just after. |
| SESS-02 | Handoff protocol | ✅ Done (basic) | `/pf-13-handoff` exists. Lighter than APM's two-artifact (Handover_File + Handover_Prompt) pattern — revisit only if single-prompt handoff proves insufficient in practice. |
| SESS-03 | Memory/session archiving (`.pmo/archives/`, stage summaries) | 🔜 Planned | From APM. Only valuable once projects routinely run long enough to need it. |

### Agile / Alternate Methodology Track

| ID | Feature | Status | Notes |
|---|---|---|---|
| AGL-01 | Scope/workflow presets (classic-waterfall / agile-hybrid / lean) at `/pf-0-init` | ✅ Done | From aidlc-workflows "scope" concept — vary which phases/gates run per project size. Preset chosen at `/pf-0-init`, recorded in `constitution.md`'s new Workflow Preset field, defined authoritatively in `docs/knowledge-areas.md#workflow-presets` (Required/Optional per knowledge area per preset). Cost/Quality/Procurement/Resource-depth managers now check the preset first and ask once before planning if Optional; Planner's handoff calls out the preset explicitly. |
| AGL-02 | Agile/Scrum ceremony layer (sprint planning, standup, retro, backlog refinement) | 🔜 Planned | Alternate track alongside the PMBOK waterfall track, from copilot-scrum-team. Larger effort — needs its own design pass. |

### Work Package Lifecycle & Quality Gates

| ID | Feature | Status | Notes |
|---|---|---|---|
| WPQ-01 | Definition of Ready checklist (before Work Package assignment) | 🔜 Planned | From copilot-scrum-team / ai-sdlc DoR rubric. |
| WPQ-02 | Batch/parallel task assignment (`/pf-8-assign-task` dispatches multiple eligible Workers in one action) | 🔜 Planned | From APM's batch dispatch pattern. T3/T4 test runs already proved `tracker.md` correctly handles two Workers genuinely "In Progress" at once when dispatched manually, one at a time — this would formalize dispatching all currently-eligible, independent work packages in a single `/pf-8` invocation instead of re-running the command per Worker. |

### Reporting & Communication

| ID | Feature | Status | Notes |
|---|---|---|---|
| REP-01 | Structured status-update headers (`## AgentName - ActionType`) | 🔜 Planned | Trivial consistency win from ai-scrum-master-template. |

### Extensibility & Customization

| ID | Feature | Status | Notes |
|---|---|---|---|
| EXT-01 | Plugin/extension pattern (`plugins/<name>/` additive, untouched core) | ✅ Done | `plugins/README.md` documents the convention: `.pf-plugin/plugin.json` manifest declaring contributed `agents/`, `prompts/`, `templates/`; install = copy files into core dirs, uninstall = delete them, core stays byte-identical. No installer script yet (that's the separate Deterministic helper scripts item, AUT-01) — install/uninstall is manual for now. `templates/catalog.json` for discovery remains a follow-up once a real plugin exists to list. |
| EXT-02 | Agent frontmatter `tools:` allow-list + plain-language Tier statement | ✅ Done | Corrected from the original "tier + `disallowedTools`" idea, which was based on aidlc-workflows' convention, not VS Code's real custom-agent schema. VS Code agents use a real `tools:` allow-list (not a deny-list) — all 9 agents now declare `tools: [read, edit, search]` (Worker adds `execute`), and each agent's body opens with a **Tier:** line (Judgment for the 8 planning/managing agents, Execution for Worker) for role clarity. |
| EXT-03 | Skills layer (`.github/skills/<name>/SKILL.md`) | ✅ Done | Evaluated all 9 agents for dense, on-demand reference material worth extracting (vs. core judgment logic needed every invocation, which stays inline). 8 skills built, one per agent that had a genuine candidate: `pf-evm-reference` (Cost Manager — EVM formulas), `pf-critical-path-reference` (Planner — CPM forward/backward pass), `pf-risk-identification-reference` (Risk Manager — elicitation techniques + P/I scale anchors), `pf-quality-audit-reference` (Quality Manager — QA/QC checklists + metrics catalog), `pf-contract-type-reference` (Procurement Manager — Fixed-Price/T&M/Cost-Reimbursable selection guide), `pf-resource-leveling-reference` (Resource Manager — leveling/smoothing/fast-tracking/crashing), `pf-stakeholder-engagement-reference` (Stakeholder Manager — quadrant tactics + Salience model), `pf-raci-facilitation-reference` (Project Manager — workshop steps + anti-patterns + RASCI/DACI variants). Worker was evaluated and correctly excluded — execution guidance is task-specific, not universal reference material. Each owning agent's body now has a one-line pointer to its skill. |

### Automation & Tooling

| ID | Feature | Status | Notes |
|---|---|---|---|
| AUT-01 | Deterministic helper scripts (EVM math, WBS 100%-rule / RACI one-A / cross-file ID validation, `/pf-0-init` template scaffolding, backlog/artifact drift detection) | 🔜 Planned | Now explicitly encouraged by Design Principle 1 (No infrastructure, revised to allow deterministic code) — an LLM computing PV/EV/AC/CPI/SPI or re-deriving a sort order by hand is slower, costlier, and less reliable than a small script. Includes ai-sdlc-style drift detection (e.g. every `bus/<worker>/task.md` has a matching `tracker.md` row, every risk ID referenced in `tracker.md` exists in `risk-register.md`). Bundle under a Skill or a plain `scripts/` folder, invoked by the agent, never running unattended. |
| AUT-02 | Trigger-action automation rules (`.pmo/automation.yml`, e.g. "if cost variance > threshold then flag for CR") | 🔜 Planned | From paca's event-driven workflow engine. A user-editable, inspectable rule list that supplements (not replaces) agent judgment — distinct from Deterministic helper scripts (AUT-01) above (rules are human-authored conditions; scripts are computations an agent invokes). Low priority — agent working-style sections already encode most of this today. |
| AUT-03 | Embedding-based routing / iterative LLM evaluator loops | ❌ Rejected | From AgenticAI_ND_P2. E.g. the user types "I'm worried about vendor risk" instead of `/pf-4-plan-risk`, and a routing layer embeds the request plus each agent's capability description and picks the closest match automatically. Design Principle 3 (the user is the checkpoint) already provides the quality gate; the added LLM cost per turn and the new misrouting failure mode (e.g. a cost question routed to the Risk Manager) aren't justified. |

## Next Up

The core PMBOK-style knowledge-area kit is now complete (Integration, Scope, Schedule, Cost,
Risk, Quality, Procurement, Resource, Stakeholder, partial Communications, Organization). Next:

1. Re-evaluate the "Infrastructure Features" and "Other Framework Features" backlogs above
   (Definition of Ready, decision log, structured status headers, scope presets, agile ceremony
   layer, plugin pattern, agent tiers, session archiving, and external tool projections) now that
   the knowledge-area kit is done.
2. Define the external integration manifest and approval flow, then design the first one-way
  Confluence publication and Jira work-package projection slices.
3. Full Communications Management (dedicated agent) remains deferred until Stakeholder Manager's
   scope genuinely outgrows what one agent can own.
4. Run another full test-run (see Governance below) to validate the four new v1 additions
   (Cost, Resource, Quality, Procurement) interact correctly end-to-end.

## Governance

- One artifact, one owner — see the Artifact Ownership table in
  [.github/copilot-instructions.md](.github/copilot-instructions.md).
- Baseline documents (`charter.md`, `wbs.md`, `schedule.md`, `cost-management-plan.md`,
  `resource-management-plan.md`, `quality-management-plan.md`, `procurement-management-plan.md`,
  `constitution.md`) change only through `/pf-12-change-request`, never by direct edit, once
  approved.
- New `/pf-N` commands are inserted with letter suffixes (e.g. `/pf-3b-plan-cost`,
  `/pf-6b-plan-resources`) between existing numbered commands rather than renumbering, so no
  existing command name ever changes.
- New knowledge areas get a dedicated agent + template(s) + a `/pf-N` prompt, and must be wired
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
