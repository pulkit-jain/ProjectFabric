# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- `ROADMAP.md`'s "Other Framework Features" section split into 7 area sub-headings —
  Governance & Decisions, Session & Context Management, Agile / Alternate Methodology Track,
  Work Package Lifecycle & Quality Gates, Reporting & Communication, Extensibility &
  Customization, Automation & Tooling — each with its own mini-table, so coverage/gaps per
  functional area are scannable at a glance instead of one long undifferentiated list.
- `ROADMAP.md` reorganized into three logical groups: **Knowledge Area Coverage (PMBOK-style)**
  (unchanged), **Infrastructure Features** (external integrations, distribution, data
  storage/runtime, backend/UI — Confluence/Jira projections, MCP server, multi-assistant support,
  Full backend/UI + sub-items, Database-backed state + sub-items, Workflow execution
  engine/CLI installer + sub-items, JSON-schema artifacts, GitHub Issues state), and **Other
  Framework Features** (pure prompt/agent/template mechanics needing no infrastructure —
  Constitution, handoff, DoR, decision log, scope presets, agile ceremony layer, plugin pattern,
  Skills layer, deterministic helper scripts, batch assignment, automation rules, team-level
  customization, embedding-based routing). Previously all lived in one undifferentiated
  "Framework Features" table.
- Revised Design Principle 1 in `docs/architecture.md` from "Zero-code" to **"No infrastructure"**:
  still no backend service, database, installed CLI/package, or long-running orchestration
  engine, but deterministic helper scripts are now explicitly encouraged for tasks with one
  provably-correct answer — math (EVM calculations), sorting (risk register order),
  schema/ID validation (WBS 100%-rule, RACI one-A rule, cross-file ID consistency), and file
  scaffolding (`/pf-0-init`) — bundled under a Skill or a plain `scripts/` folder, invoked by an
  agent, never running unattended. Propagated the rename to `README.md`'s Architecture &
  Extensibility section and every `ROADMAP.md` entry that cited the old "Zero-code" name.
  `ROADMAP.md`'s "JSON-Schema validated artifacts" entry split in two: the artifact-format
  replacement (Markdown → JSON) stays Deferred, and a new "Deterministic helper scripts" entry
  is now Planned, since it's explicitly allowed by the revised principle.

### Added

- Implemented `GOV-03`, the team-level customization layer: new `templates/team.template.md`
  (Team Defaults — Workflow Preset, cost tracking mode, control cycle cadence, variance and risk
  thresholds — plus Team Standards) copied into each project's `.pmo/team.md` at `/pf-0-init`
  (from the team's shared master copy, or blank). Precedence is now explicit in Ground Rule 1:
  framework Ground Rules → `team.md` → `constitution.md`; a constitution may override a team item
  only via its new "Overrides of team.md" table with a stated reason, and nothing may contradict
  the Ground Rules. `/pf-0-init`, `/pf-0b-constitution`, and the Cost Manager now propose team
  defaults first. Planner owns `team.md`; it is baselined like `constitution.md` (added to Ground
  Rule 5 and ROADMAP's baseline list). No new command — folded into `/pf-0-init` to avoid
  command sprawl. Sharing across projects is a manual copy, consistent with Design Principle 1.
  Also refreshed ROADMAP's stale "Next Up" item 1 (it still listed the now-done decision log).
- Implemented `GOV-02`, the Decision Log: new `/pf-12b-log-decision` command (pairs with
  `/pf-12-change-request`, same as the Agile ceremony layer's pairing pattern) writes
  `decisions/DEC-<id>.md` from `templates/decision-record.template.md` — context, options
  considered, the decision and why, consequences, and a Decision Owner. Status lifecycle Draft →
  Signed-off → Superseded (by a later `DEC-<id>`, never deleted). Any agent may propose a
  decision; the Project Manager owns the log, same ownership pattern as Change Requests. Ground
  Rule 5 in `copilot-instructions.md` now explicitly distinguishes a Decision (no baseline impact)
  from a Change Request (baseline impact). Wired into `copilot-instructions.md` (Artifact
  Ownership, Process Group Mapping), `pf-0-init.prompt.md` (scaffolds `decisions/`), `README.md`
  (directory tree, commands table), and `ROADMAP.md` (GOV-02 → Done, plus added as a 9th
  mechanism in the Governance section's Audit Trail table).
- Added an "Audit Trail" subsection to `ROADMAP.md`'s Governance section, resolving the forward
  reference left by `INF-12`'s note. Documents the 8 existing mechanisms that together provide
  "what changed and why" today (git history, `changes/CR-<id>.md`, `constitution.md`'s Amendments
  table, `memory/work-packages/WP-<id>.md`, `tracker.md`'s Variance Notes,
  `reports/status-<date>.md`, `quality-control-log.md`/`vendor-contract-register.md`,
  `standup-log.md`/`retro-log.md`) — explicitly distinguished from `INF-12`'s still-Planned
  agent-activity *telemetry*, which is a separate, not-yet-built concern.
- Parked `INF-12`, an observability layer for agent activity, in `ROADMAP.md`'s Infrastructure
  Features table as 🔜 Planned — not built yet. Two options recorded, not yet chosen between:
  (a) file-based self-reported `.pmo/logs/agent-activity.jsonl` + a deterministic aggregation
  script (fits Design Principle 1), or (b) an OpenTelemetry-style exporter for real latency/
  token/cost metrics (needs a running collector, contradicts Design Principle 1). Audit trail
  (what changed and why) is separately already covered by existing artifacts (CRs, tracker
  variance notes, work-package memory logs, git history) — this item is specifically about
  agent-activity telemetry, not audit trail.
- Added a **Sprint Review** ceremony (`/pf-10c-sprint-review`) to the Agile ceremony layer,
  closing the gap flagged when reviewing AGL-02: ProjectFabric has no dedicated Product Owner
  agent, and Sprint Review is where that role's acceptance authority needs to be exercised
  explicitly. Runs after `/pf-10-check-report` marks the sprint's work packages Done and before
  `/pf-11b-sprint-retro` — the user (acting as Product Owner) accepts or rejects each completed
  work package against its WBS Dictionary acceptance criteria; a passed QA gate is necessary but
  not sufficient for acceptance. `sprint-backlog.template.md`'s current-sprint table gets a new
  "Sprint Review Outcome" column (Not Reviewed / Accepted / Rejected). `scrum-master.agent.md`
  now states the Product-Owner gap explicitly and reorders its Responsibilities to match real
  ceremony order (Planning → Standup → Review → Retro → Backlog Refinement, the last being
  ongoing rather than sprint-boundary-bound). Wired into `pf-10-check-report.prompt.md` and
  `pf-11b-sprint-retro.prompt.md`'s cross-references, `copilot-instructions.md`,
  `docs/knowledge-areas.md`, `README.md`, and `ROADMAP.md`'s AGL-02 note.
- Built AGL-02, the Agile/Scrum ceremony layer, as **core** (option 1 from the plugin-vs-core
  discussion — chosen so ceremony engagement is gated by the Workflow Preset like any other
  phase, not a separate install step). New `pf-scrum-master` agent owns three new artifacts
  (`sprint-backlog.md`, `standup-log.md`, `retro-log.md`) and four new letter-suffixed commands,
  each paired to an existing Manager-loop phase: `/pf-7b-sprint-planning` (pairs with
  `/pf-7-initiate-manager`), `/pf-8b-standup` (pairs with `/pf-8-assign-task`),
  `/pf-10b-backlog-refinement` (pairs with `/pf-10-check-report`), `/pf-11b-sprint-retro` (pairs
  with `/pf-11-control-cycle`). Engaged by default under the agile-hybrid Workflow Preset,
  optional (ask once) under lean, off under classic-waterfall — new row added to
  `docs/knowledge-areas.md#workflow-presets`. Wired into `copilot-instructions.md` (roles list,
  Artifact Ownership table, Process Group Mapping), `README.md` (Core Idea, directory tree,
  commands table, and a stale "four Design Principles" reference corrected to five),
  `pf-0-init.prompt.md` (scaffolds the three new files), and `ROADMAP.md` (AGL-02 → Done). Also
  updated `plugins/README.md`'s illustrative manifest example (previously named `scrum-team` /
  `scrum-master.agent.md`) to a generic `example-role` name, since core now owns the real
  `scrum-master.agent.md` filename and reusing it in the plugin example risked a naming collision.
- Added a stable Feature ID (`KA-`, `INF-`, `GOV-`, `SESS-`, `AGL-`, `WPQ-`, `REP-`, `EXT-`,
  `AUT-`, one prefix per `ROADMAP.md` table/section) to every feature row, including a decimal
  suffix for existing `└` sub-items (e.g. `INF-08.1`). IDs are permanent once assigned — never
  renumbered or reused, even for a Rejected/removed row — so they can be cited from
  `CHANGELOG.md`, commit messages, and future Change Requests instead of matching on feature
  names. `ROADMAP.md`'s Governance section gets a new rule documenting the ID-stability
  convention, and cross-references between related rows (e.g. INF-10.5 → AUT-01, INF-09.3 →
  EXT-01) now cite IDs instead of prose feature names where it was ambiguous.
- Scope/workflow presets (classic-waterfall / agile-hybrid / lean), chosen at `/pf-0-init` and
  recorded in `constitution.md`'s new Workflow Preset field. `docs/knowledge-areas.md` gets a new
  "Workflow Presets" section defining, per preset, which knowledge areas are Required vs. Optional
  (agile-hybrid keeps the Scope/Schedule/Risk/Stakeholder/RACI backbone but pulls in Cost/
  Quality/Procurement/Resource-depth only when needed; lean requires only the minimum to start
  assigning and tracking work). Cost, Quality, Procurement, and Resource Manager agents each got a
  new "Check the preset" responsibility bullet — they read the preset first and ask once before
  planning if their phase is Optional, rather than assuming yes. Planner's Handoff now calls out
  the preset explicitly when recommending the next command.
- Added a 5th Design Principle to `docs/architecture.md`: **"Extensibility & customization by
  addition, never by modification."** Codifies the pattern already in use (plugins install by
  copying files into core dirs, Skills split situational reference material out of agent bodies,
  `.pmo/constitution.md` layers project-specific rules on top of the framework-wide agreement)
  as an explicit, citable principle so future features are evaluated against it the same way as
  the other four.
- Evaluated all 9 agents for Skills candidates and built 7 more (8 total): `pf-critical-path-reference`
  (Planner — CPM forward/backward pass, float, worked example), `pf-risk-identification-reference`
  (Risk Manager — elicitation techniques + concrete Probability/Impact scale anchors),
  `pf-quality-audit-reference` (Quality Manager — QA/QC checklists + common metrics catalog),
  `pf-contract-type-reference` (Procurement Manager — Fixed-Price/T&M/Cost-Reimbursable selection
  guide + fee structure variants), `pf-resource-leveling-reference` (Resource Manager — leveling
  vs. smoothing, fast-tracking, crashing), `pf-stakeholder-engagement-reference` (Stakeholder
  Manager — per-quadrant tactics, Salience model, resistant-stakeholder tactics), and
  `pf-raci-facilitation-reference` (Project Manager — workshop steps, anti-patterns, RASCI/DACI
  variants). Worker was evaluated and correctly excluded (no universal reference material —
  execution guidance is task-specific). Each owning agent now has a one-line pointer to its skill.
  `ROADMAP.md`'s Skills layer entry updated to reflect full coverage across all agents.
- Extensibility & Customization area built out (reorganizing existing agents before adding new
  features, per user request): all 9 agent files (`.github/agents/*.agent.md`) now declare a
  real VS Code `tools:` allow-list (`[read, edit, search]`, Worker adds `execute`) and open with
  a plain-language **Tier:** statement (Judgment for the 8 planning/managing agents, Execution
  for Worker). `plugins/README.md` documents the additive plugin convention
  (`.pf-plugin/plugin.json` manifest, install-by-copy/uninstall-by-delete, core untouched). First
  real Skill built: `.github/skills/pf-evm-reference/SKILL.md` (EVM formulas, computation order,
  interpretation table, worked example), extracted out of `cost-manager.agent.md` so the formulas
  only load on demand. `ROADMAP.md`'s "Agent frontmatter tier + `disallowedTools`" idea corrected
  to reflect VS Code's real schema (`tools:` allow-list, not a `disallowedTools` deny-list) —
  another stale assumption caught by actually implementing the feature, same pattern as prior
  test-run bugs.
- `ROADMAP.md` Framework Features: 13 sub-items broken out into their own explicit `└` rows for
  full traceability under Full backend/UI (WebSockets, Docker/Kubernetes, domain-specific
  vertical templates), Database-backed state (SQLite/Postgres/Valkey, ORM schemas, WASM plugin
  sandboxing), and Workflow execution engine (git-worktree pooling, autonomous polling loops,
  DSSE attestations, signal ingestion pipelines, multi-language script parity, wheel bundling,
  Jinja2 templating) — previously subsumed silently under their parent category.
- `ROADMAP.md` Framework Features: three new items found via a systematic one-by-one re-review of
  all 11 reference repos (`Batch/parallel task assignment` from APM, `Trigger-action automation
  rules` from paca, `Team-level customization layer` from aidlc-workflows' org/team/project
  layering), plus enriched the existing `Deterministic helper scripts` row with ai-sdlc's
  backlog/artifact drift-detection example and the `Plugin/extension pattern` row with Spec Kit's
  template-catalog idea.
- `ROADMAP.md` Framework Features backlog: added a tracked entry for a Skills layer
  (`.github/skills/<name>/SKILL.md`) — on-demand bundled reference material for agents
  (EVM formulas, RACI facilitation technique, quality-audit checklists), a VS Code Copilot
  customization primitive not yet used anywhere in ProjectFabric.
- `ROADMAP.md`: enriched the Plugin/extension pattern and Embedding-based routing rows with
  concrete examples, and added two new Rejected entries — JSON-Schema validated artifacts (à la
  ai-sdlc's schema-checked resources) and State in GitHub Issues instead of files (à la
  ai-scrum-master-template's Kanban-as-Issue) — each with the trade-off against ProjectFabric's
  zero-code, portable-plain-text design principles.
- `docs/architecture.md`: added a canonical "Design Principles" section (Zero-code, State lives
  in portable plain-text files, The user is the checkpoint, One artifact one owner) consolidating
  statements that were previously scattered across README.md, copilot-instructions.md, and
  test-plan.md. `ROADMAP.md`'s Rejected/Deferred Framework Features entries and README.md's
  "Architecture & Extensibility" section now cite this section directly instead of re-deriving
  the rationale in ad-hoc phrasing each time.
- Roadmap entries for future one-way Confluence artifact publishing, Jira work-package
  projection, and a local external integration manifest, with bidirectional synchronization
  explicitly deferred until the projection model is validated.
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
