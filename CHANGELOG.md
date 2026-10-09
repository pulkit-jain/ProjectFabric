# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- **`pi-cadence` Workflow Preset (AGL-04, AGL-04.1).** A fourth preset for a continuing product that
  plans a year roughly and ships in fixed-length Program Increments, with the date fixed and scope
  flexible. New commands `/pf-plan-roadmap`, `/pf-plan-pi` and `/pf-close-pi`; new files
  `roadmap.md`, `pi-plan.md` and `product-backlog.md` (templates and ownership entries). The
  constitution gets a **PI Practices** section where each project sets the PI length, iteration length
  and a Yes or No for five practices (PI objectives with a confidence vote, WSJF, a PI review, ROAM
  risk handling, a PI predictability metric). `pf_rules.py` gained `pi_predictability_pct` and
  `--metric`. Adding a PI's work packages to `wbs.md` and `schedule.md` is planned work, not a Change
  Request (Ground Rule 5). The presets table, the command notes and reference, the artifact reference,
  a scenario and the README are updated. No example project and no live run yet.
- **Artifact relationship diagram** in `docs/guides/artifact-reference.md` (which `.pmo/` files feed
  which, drawn from what each command reads and writes). The constitution template now says it is
  project-specific, that team-wide Working Rules belong in `team.md`, and that team defaults are
  copied into it at init.
- **Working rules guide** (`docs/guides/working-rules.md`): what a team working rule is, how to write
  one, and example rules by area (governance, scope and schedule, cost, risk, quality,
  procurement, people and AI team members, stakeholders, records, security, escalation, handover,
  closing, agile) to copy into `team.md`.
  Linked from the README, the guides index, and the getting-started `team.md` section.

### Changed

- **How the constitution is shown to be approved.** The Initial version row's Approved By in its
  Amendments table is now the approval marker (blank means not approved), stated in the template and
  in `/pf-setup-project-constitution` step 7. `/pf-start-manager` checks it: under classic-waterfall
  or agile-hybrid it tells the user and offers to run `/pf-setup-project-constitution` first (the
  user may continue), under lean it only mentions it.
- **Amendments tables: the agent writes the date and the change, and asks only for the approver.**
  Ground Rule 5 now says every change to `project-constitution.md`, `work-package-definitions.md` or
  `team.md` gets an Amendments row with today's date and a one-line change (with the CR ID when there
  is one); the agent asks the user only for Approved By and never fills it in. For a change made
  through `/pf-change-request` step 5, the approver is the one recorded in the CR. The templates and
  the constitution and cost-planning prompts say the same.
- **Default content for four constitution sections.** `project-constitution.md` is now created with
  default Decision Authority approvers (the Sponsor), Status Report Reviewers (the Sponsor), Escalation
  Rules (five default rules) and Project Completion Criteria (five conditions that
  `/pf-close-project` checks). `/pf-setup-project-constitution` shows these and asks only what to add,
  change or drop.
- **Work package checks moved to their own file, `work-package-definitions.md`.** The Definition of
  Ready and Definition of Done (work package) tables left `project-constitution.md`. The new file is
  owned by the Planner, created by `/pf-setup-init` pass 2 with the standard rows, and tailored in
  `/pf-setup-project-constitution`. `/pf-assign-task`, `/pf-agile-backlog-refinement`,
  `/pf-check-report`, the Team Member and Project Manager agents and `/pf-close-project` read it. The
  constitution's project-level Definition of Done is renamed **Project Completion Criteria**, and
  `/pf-close-project` now checks it.
- **Definition of Done for a work package (WPQ-04).** `project-constitution.md` has a new
  Definition of Done (work package) table (acceptance criteria met, QA gate passed when a quality
  plan exists, a complete report), next to the Definition of Ready. `/pf-check-report` sets "Done"
  only when every row passes, and the Team Member agent, `/pf-close-project` and
  `/pf-setup-project-constitution` refer to it. The existing project-level Definition of Done is
  unchanged.
- **The standard Definition of Ready list moved from `/pf-assign-task` into the project
  constitution.** `project-constitution.md` now has a Definition of Ready table (seven standard checks,
  each with who fixes a failure) that a project can add rows to. `/pf-assign-task` step 3,
  `/pf-agile-backlog-refinement` and the Project Manager agent now refer to that table instead of
  holding their own copy. The separate "project-level additions" section is gone, since additions are
  just more rows.
- **`/pf-setup-init` pass 2 copies `team.md` into the project constitution; there is no overrides
  table.** `project-constitution.md` now starts with a **Project Defaults** table (same five settings
  as `team.md`'s Team Defaults) and **Team Working Rules** (copied from `team.md`), followed by
  **Project Working Rules** and **Exempted Team Working Rules**, and Status Report Reviewers replaces
  Reporting Cadence. From then on every agent and prompt reads the project's values in the
  constitution, not in `team.md`, which is read at pass 2 and kept as the team's record. A value that
  differs from the team's gets its reason in the constitution's Amendments table.
  `/pf-setup-project-constitution` shows the copied defaults and asks which to change;
  `pf_scaffold.py` does the copying. Ground Rule 1 states the rule once.
- **"Team Standards" (team.md) and "Principles" (project constitution) are now both "Working Rules".**
  They were the same kind of rule at two scopes. The team's section holds rules for every project of
  the team; the project constitution's section holds rules for that project only, on top of the
  team's. `pf_scaffold.py` now checks for at least one Working Rule, and the guide moved to
  `docs/guides/working-rules.md`.
- **Constitution renamed to Project Constitution.** `/pf-setup-constitution` is now
  `/pf-setup-project-constitution`, `.pmo/constitution.md` is now `.pmo/project-constitution.md`, and
  `templates/constitution.template.md` is now `templates/project-constitution.template.md`. Every
  reference in agents, prompts, skills, scripts, templates and docs was updated, and the example
  project's file was renamed. Entries below this one keep the old names as history. An existing
  project's `.pmo/constitution.md` must be renamed by hand.
- **Workflow Preset in the project constitution is now a plain value under its heading** instead of
  a bold `**Preset:** ...` line, like the Team Name section of `team.md`. `pf_scaffold.py` writes the
  preset into that section.

- **`/pf-setup-init` now runs in two passes, and `team.md` is mandatory (GOV-03, AGL-01).** Pass 1
  creates only `.pmo/team.md` from the template. Pass 2 refuses to run until `team.md` has a Team
  name, a non-`TBD` value in every Team Defaults row, and at least one Team Standard (Amendments
  optional), then scaffolds the rest. The Workflow Preset is read from `team.md`; the separate preset
  question and the `--preset` and `--team` options of `pf_scaffold.py` are gone (it gained
  `--team-only` and the completeness check). The templates, prompt, SKILL.md, Ground Rule 1, the
  ownership table and the guides were updated to match.

- **`team.md` thresholds are now actually proposed where they apply (GOV-03).** `/pf-plan-cost` and
  the Cost Manager propose the Cost variance escalation threshold; `/pf-plan-risk` and the Risk
  Manager flag acceptance of a risk scored above the Risk acceptance score ceiling and name the
  approver; `/pf-setup-constitution` step 0 names which Team Default feeds which section. Nothing
  is enforced by a script. `docs/guides/getting-started.md` defines every Team Defaults setting.

- **Slash commands renamed from numbered to category-based names**, `/pf-<category>-<action>`
  (categories `setup`, `plan`, `agile`, `session`; the work loop keeps plain verbs). Every
  reference in agents, prompts, skills, scripts, templates and docs was updated; entries below
  this one keep the old names as history. README's Commands table now has a Category column.
  New commands pick a category instead of a number or letter suffix.

  | Old | New |
  |---|---|
  | `/pf-0-init` | `/pf-setup-init` |
  | `/pf-0b-constitution` | `/pf-setup-constitution` |
  | `/pf-1-initiate-planner` | `/pf-setup-charter` |
  | `/pf-2-plan-scope-wbs` | `/pf-plan-scope-wbs` |
  | `/pf-3-plan-schedule` | `/pf-plan-schedule` |
  | `/pf-3b-plan-cost` | `/pf-plan-cost` |
  | `/pf-4-plan-risk` | `/pf-plan-risk` |
  | `/pf-4b-plan-quality` | `/pf-plan-quality` |
  | `/pf-4c-plan-procurement` | `/pf-plan-procurement` |
  | `/pf-5-plan-stakeholders` | `/pf-plan-stakeholders` |
  | `/pf-6-plan-organization` | `/pf-plan-organization` |
  | `/pf-6b-plan-resources` | `/pf-plan-resources` |
  | `/pf-7-initiate-manager` | `/pf-start-manager` |
  | `/pf-7b-sprint-planning` | `/pf-agile-sprint-planning` |
  | `/pf-8-assign-task` | `/pf-assign-task` |
  | `/pf-8b-standup` | `/pf-agile-standup` |
  | `/pf-9-initiate-worker` | `/pf-start-team-member` |
  | `/pf-10-check-report` | `/pf-check-report` |
  | `/pf-10b-backlog-refinement` | `/pf-agile-backlog-refinement` |
  | `/pf-10c-sprint-review` | `/pf-agile-sprint-review` |
  | `/pf-11-control-cycle` | `/pf-control-cycle` |
  | `/pf-11b-sprint-retro` | `/pf-agile-sprint-retro` |
  | `/pf-12-change-request` | `/pf-change-request` |
  | `/pf-12b-log-decision` | `/pf-log-decision` |
  | `/pf-13-handoff` | `/pf-session-handoff` |
  | `/pf-13b-archive-stage` | `/pf-session-archive-stage` |
  | `/pf-14-close-project` | `/pf-close-project` |

- Python bytecode (`__pycache__/`, `*.pyc`) is now git-ignored.

- **"Worker" renamed to "Team Member"** everywhere outside this changelog's history: the agent is
  `pf-team-member` (`.github/agents/team-member.agent.md`), the command is
  `/pf-start-team-member`, the task bus folder is `bus/<member>/`, and example IDs are `member-a`
  and so on. A team member is now any roster entry of type Person, AI, or Vendor; only AI members
  run in their own conversation and use the bus.

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

- **User guides** (REP-10) in `docs/guides/`: a getting started tutorial with a track for people new
  to project management and one for experienced project managers, a how-a-project-runs concepts
  page with a glossary, ten scenarios that show what you provide and what you get at each step, an
  artifact reference (every `.pmo/` file with its owner and whether it is baseline, living, or
  record), and a command reference. The command reference tables (command, conversation, when to run,
  you provide, you get, files, next command, preset) are generated by
  `tools/gen_command_reference.py` from the prompts, `docs/guides/command-notes.md`, and the
  Workflow Presets table; `--check` fails when a prompt has no notes entry or the file is stale. A
  filled-in fictional example project (a company offsite with a Person, an AI, and a Vendor member,
  a Change Request, a decision, and a status report) is in `docs/example/`. The root README is now a
  pitch, a documentation index, a short quick start, and the commands table. The README also lists
  the guides still to write (recipes, troubleshooting and FAQ, customising, cheat sheet, sponsor and
  team member guides, integration guides).
- **Project Organization depth** (KA-08 extended, KA-13 new). `organization.md` (Project Manager):
  governance structure, role definitions, a team roster whose members are a Person, an AI agent,
  or a Vendor with Proposed / Confirmed / Open status, and an org change log; governance and
  roles are baseline, the roster is living. `skill-matrix.md` (Resource Manager): skills catalog,
  minimum level per WBS leaf on a 1-4 scale, team coverage per roster member, and a gap analysis
  with a proposed action. New commands `/pf-setup-organization` and `/pf-plan-skills`;
  `/pf-plan-organization` rewritten to settle the roster against skill gaps and build the RACI
  from roster Member IDs. Both phases are Required under classic-waterfall and agile-hybrid and
  Optional under lean. `/pf-assign-task` gained an eighth Definition of Ready item (assignee is a
  Confirmed roster member) and a hand-over path for Person and Vendor members. `pf_validate.py`
  gained Org and Skills checks (unique IDs, valid Type and Status, RACI columns and `bus/` folders
  match the roster, skill IDs resolve, levels 1-4, warnings for unconfirmed members and uncovered
  requirements). New templates `organization.template.md` and `skill-matrix.template.md`; skill
  ratings of named people are treated as sensitive (Ground Rule 4).
- Gave every entry in `docs/Reference.md` a permanent ID (`REF-P01` to `REF-P11` projects
  studied, `REF-M01` to `REF-M12` methods and standards, `REF-T01` to `REF-T10` platforms and tools,
  `REF-X01` to `REF-X10` technologies named only because a studied project used them), and made
  the rest of the repository cite sources by ID only. Every direct mention of a studied project in
  `ROADMAP.md`, `CHANGELOG.md` and `docs/architecture.md` was replaced with its ID (for example
  "from REF-P05"), and each of the eight reference skills now carries a `Sources:` line with the IDs
  of the methods it draws on. Names of methods, platforms and technologies still appear where they
  describe what a feature is ("Jira projection", "RACI matrix"), since removing them would make the
  sentences meaningless; the page lists them all with IDs. `docs/test-plan.md`'s static audit gained
  a check for this.
- Added `docs/Reference.md`, a credits page for the whole repository: the eleven projects studied
  (source URL where one was found, the licence and copyright line found in the studied copy, and
  which roadmap items each informed), the standards, methods and publications the content draws on
  (PMBOK, earned value, critical path, RACI, the salience model, the pre-mortem, Scrum, Keep a
  Changelog, Semantic Versioning), the platforms and tools involved, and the technologies named only
  because a studied project used them. Before writing it, a line-by-line comparison (60+ character
  lines) against the studied projects found only standard Keep a Changelog boilerplate in common.
  Also replaced `ROADMAP.md`'s pointer to a local-only notes file with a link to this page, and
  listed the page in the README's directory tree. Where no URL or licence file could be found it
  says so rather than guessing.
- Extended the Version 2 plan in `ROADMAP.md` with the ideas approved by the user (nothing
  built): Outlook unsent drafts and invites (`INF-14`), Microsoft Teams meeting capture
  (`INF-15`), `markitdown` document import (`INF-16`), git/GitLab version control of
  `.pmo/` (`INF-17`), sensitivity labels (`GOV-04`), an issue and action log (`GOV-05`), a Kanban
  preset (`AGL-03`), structured dates (`WPQ-03`), newsletter/blog/announcement drafts (`REP-06`), a
  Technical Writer agent (`REP-07`), and a narration script in speaker notes (`REP-03.1`) with
  voice-over audio deferred (`REP-03.2`). `KA-12` (full Communications, a Communications Manager
  agent) moved from Deferred to Planned because its trigger condition is met. The phases now run
  0 to 7, with Phase 0 holding the foundations (dates, labels, issue log, MCP spike) and new
  Communications (5) and Flow/documentation (6) phases. A portfolio roll-up (`REP-08`) with a
  Portfolio Manager agent (`REP-09`) is recorded as Deferred until a second real project exists.
- Recorded a Version 2 plan in `ROADMAP.md` (nothing built): a "Version 2 Plan" section
  with a reviewed list of the remaining backlog, Design Principle impact, six phases in two
  independent tracks (Atlassian: MCP spike, integration manifest, Confluence publishing, Jira
  projection; Office: Excel and presentation export), risks, and a test approach. Six decisions
  were made with the user: everything ships in core; standard-library XLSX writer; `python-pptx`
  now (filling a user-supplied template) with the dependency-free MARP deck deferred; Jira maps
  Epic per deliverable and Task per work package; a core Confluence designer skill with a theme
  slot that uses the user's installed styling skill, if any (never copied or forked); the
  stakeholder register is publishable only on explicit confirmation each time, after a warning
  preview. New rows: `INF-13` (MCP consumption convention), `INF-04.1` (read-only Jira drift
  report), `REP-02` (Excel), `REP-03` (presentation), `REP-04` (Confluence designer), `REP-05`
  (MARP, deferred); `INF-01` to `INF-03` are tagged with their phases. `python-pptx` will be
  ProjectFabric's first optional package dependency, which needs an explicit carve-out in the
  architecture doc when built. Also replaced the
  stale "Next Up" items (the integration manifest item and the "validate four new v1 additions"
  test run, which T5 superseded).
- Full-framework test: a repeatable static audit (documented in `docs/test-plan.md`, not committed
  as a script) and a fifth lifecycle run, T5 (`_sandbox/packaging-redesign/`, gitignored), that
  exercises everything added since T4 in one project — the agile-hybrid preset with three Optional
  phases skipped, `team.md` with a constitution override, all five Agile ceremonies, a Definition
  of Ready failure and a waiver, batch dispatch, three decisions with a supersession, a partial
  stage archive, all four helper scripts, and automation rules. `docs/test-plan.md` gained a T5
  column, seven new command rows, twelve new scenario rows, and an updated backlog of what is still
  untested (lean and classic-waterfall runs, same-Worker batch queuing, an installed plugin).
  Outcome: 10 defects found and fixed (see Fixed), 0 in the helper scripts themselves this round.
- Implemented `AUT-02`, trigger-action automation rules, scaled down to fit Design Principle 1:
  nothing is event-driven or unattended. New `templates/automation-rules.template.md` becomes
  `.pmo/automation-rules.md`, a table of `Condition` (`<metric> <operator> <number>`), `Flag Message`,
  `Suggest`ed command, and `Enabled`. The new `pf_rules.py` in the `pf-helper-scripts` skill
  computes eight metrics from `.pmo/` (`blocked_wp_count`, `done_pct`, `open_risk_count`,
  `open_risk_max_score`, `cost_overrun_pct_max`, `cpi_min`, `spi_min`, `draft_decision_count`) and
  reports which enabled rules are TRIGGERED. It runs at step 8 of `/pf-11-control-cycle`, after the
  cost, resource, quality, and procurement data are refreshed (it first shipped at step 0 and was
  moved after the full-framework test found the CPI rule reading stale figures); a
  triggered rule only appears in the Status Report with its suggested command — the user decides,
  and nothing is run or edited automatically. The seven shipped example rules are all disabled with
  example numbers, so default behavior is unchanged (Ground Rule 4). Wired into `pf_scaffold.py` and
  `/pf-0-init`, the Ownership table (Project Manager), the Project Manager's Control
  responsibility, `/pf-0b-constitution` (offers to encode escalation conditions as rules), and
  README. Uses a Markdown table rather than the roadmap's `.pmo/automation.yml`: YAML can't be parsed
  with the standard library and Design Principle 2 keeps state in plain Markdown tables.
  Verified: the metrics match the raw `datacenter-migration` data (18.2% worst overrun, 7 of 7
  non-descoped work packages Done) and `video-onboarding` (CPI 1.10); a synthetic fixture covered
  triggered, not triggered, disabled, unknown-metric, and malformed rules, Descoped rows, and a
  Draft decision. No automated test suite was added.
- Implemented `AUT-01`, deterministic helper scripts, as a ninth skill,
  `.github/skills/pf-helper-scripts/` (Python 3.9+, standard library only; ships with the `.github/`
  copy, so no extra install step). Three scripts an agent runs on demand and never unattended:
  `pf_evm.py` prints the Full EVM table and Project Rollup in `cost-performance.md`'s shape;
  `pf_validate.py` is a read-only check of WBS Hierarchy vs. Dictionary, exactly one Accountable per
  RACI row, risk Score = Probability x Impact and sort order, tracker IDs and linked `R-`/`CR-` IDs,
  `bus/` task files vs. tracker, and sprint-backlog IDs; `pf_scaffold.py` creates `.pmo/` from
  `templates/`, never overwrites, and applies `--preset`/`--team`. Wired into the Cost Manager (EVM),
  the Project Manager (validate at step 0 of `/pf-11-control-cycle`), and `/pf-0-init` (scaffold),
  each with a manual fallback when Python or a terminal isn't available. The scripts report and
  compute only; Status colors and every judgment stay with the agent and user.
  Verified: `pf_evm.py` reproduces the `video-onboarding` sandbox's EVM table and rollup exactly;
  `pf_validate.py` passes `crm-rollout` and `video-onboarding` cleanly and flags a planted-defect
  fixture on every rule; `pf_scaffold.py` was run dry, real, re-run (no overwrites), with a bad
  preset, and its output validated as all-skipped. No automated test suite was added.
- Cost Manager and Project Manager now declare `execute` in `tools:` to run those scripts (Worker
  already had it). The VS Code terminal-confirmation prompt keeps the user as the checkpoint.
  Because the Project Manager can now run commands, `/pf-13b-archive-stage` runs its approved
  `git mv` moves itself instead of handing the user a command block (still handing over if it can't).
- Implemented `REP-01`, structured status headers, as new Ground Rule 8 in
  `copilot-instructions.md`: any response that drafts, changes, or reviews an artifact opens with
  `## <Agent> - <Action>` (Action limited to Drafted / Updated / Reviewed / Flagged / Blocked /
  Handed off) and an `Artifacts:` line. Put in the Ground Rules rather than in each prompt so all
  agents and future commands inherit it; pure-Q&A responses are exempt.
- Implemented `WPQ-02`, batch task assignment, inside `/pf-8-assign-task` (no new command). It
  now builds an eligible set (restricted to the current sprint when the Agile layer is in use) and
  offers a batch when more than one work package is eligible, under independence rules: one work
  package per Worker (the earlier by schedule wins), combined assignee capacity checked against
  `resource-allocation.md`, and a question to the user for anything that may touch the same
  deliverable. The Definition of Ready runs per work package and a failure drops only that item.
  The full proposed dispatch is presented once for approval before any file is written, keeping
  the user as the checkpoint; the user still opens one Worker conversation per package. Project
  Manager's Working Style clarifies a batch never stacks two packages on one Worker.
- Implemented `WPQ-01`, the Definition of Ready check: `/pf-8-assign-task` now runs a readiness
  gate before writing any task — testable acceptance criteria, a Responsible party plus exactly
  one Accountable in `raci.md`, inputs/constraints stated, QA gate coverage (if a quality plan
  exists), assignee not over-allocated (if a resource plan exists), vendor contract active (if
  vendor-owned), and any project additions. A failed item is routed back to its owning agent; the
  user may waive it, and the outcome (Passed / Passed with waiver) is recorded in the new
  Definition of Ready section of `work-package.template.md`. `constitution.template.md` gained a
  "Definition of Ready (project-level additions)" section, which `/pf-0b-constitution` now asks
  about. `/pf-10b-backlog-refinement`'s Ready flag uses the same checklist minus the
  predecessors-Done test. Project Manager's Assign responsibility updated. Refreshed ROADMAP's
  "Next Up" item 1 again.
- Implemented `SESS-03`, session/stage archiving: new `/pf-13b-archive-stage` command (pairs with
  `/pf-13-handoff`) and `templates/stage-summary.template.md`. At the end of a stage (sprint,
  milestone, or phase) the Project Manager writes `archives/<stage>/stage-summary.md` — outcome,
  work packages delivered, DEC/CR links, risks, carry-forward, and an index of moved files — and
  prepares the move of that stage's work-package history out of the live folders. Only Done (and,
  with the Agile layer, Accepted) work qualifies; baselines, registers, `changes/`, and
  `decisions/` are never archived. Because the Project Manager's tools (`read`, `edit`, `search`)
  cannot move files, the agent hands the user a `git mv` block and verifies afterward, rather than
  being granted `execute` — keeps least privilege and matches Design Principle 3; a script for this
  belongs to AUT-01. Ground Rule 1 now tells agents to read stage summaries, not archived files,
  which is where the context saving comes from. `/pf-14-close-project` reads the summaries,
  `/pf-11b-sprint-retro` suggests archiving, `/pf-0-init` scaffolds `archives/`, and ROADMAP's
  Audit Trail table gained a row.
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
  all 11 reference repos (`Batch/parallel task assignment` from REF-P02, `Trigger-action automation
  rules` from REF-P08, `Team-level customization layer` from the org/team/project
  layering in REF-P04), plus enriched the existing `Deterministic helper scripts` row with the
  backlog/artifact drift-detection example from REF-P05 and the `Plugin/extension pattern` row with
  the template-catalog idea from REF-P01.
- `ROADMAP.md` Framework Features backlog: added a tracked entry for a Skills layer
  (`.github/skills/<name>/SKILL.md`) — on-demand bundled reference material for agents
  (EVM formulas, RACI facilitation technique, quality-audit checklists), a VS Code Copilot
  customization primitive not yet used anywhere in ProjectFabric.
- `ROADMAP.md`: enriched the Plugin/extension pattern and Embedding-based routing rows with
  concrete examples, and added two new Rejected entries — JSON-Schema validated artifacts (like the schema-checked resources in REF-P05) and State in GitHub Issues instead of files (like the Kanban-as-Issue in REF-P07) — each with the trade-off against ProjectFabric's
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
- Project Constitution pattern (inspired by REF-P01): `/pf-0b-constitution` command and
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

- Found by the full-framework test (static audit A1 plus lifecycle run T5, see `docs/test-plan.md`):
  - Eight templates (`change-request`, `lessons-learned`, `quality-management-plan`,
    `quality-control-log`, `procurement-management-plan`, `vendor-contract-register`,
    `resource-management-plan`, `resource-allocation`) were never referenced by any prompt, so an
    agent had no instruction to use them. `/pf-4b`, `/pf-4c`, `/pf-6b`, `/pf-12`, and `/pf-14` now
    name their template(s). Earlier lifecycle runs missed this because the tester already knew the
    templates existed.
  - `/pf-7-initiate-manager` required the cost, risk, stakeholder, and resource plans regardless of
    Workflow Preset, so a lean or agile-hybrid project would have been sent back to plan phases it
    had legitimately skipped. It is now preset-aware. `/pf-11-control-cycle` likewise now reads
    whichever optional plans exist.
  - Nothing pointed to `/pf-7b-sprint-planning` at the start of the loop (only later ceremonies
    did); `/pf-7` now suggests it when the Agile layer is in use. `/pf-8b-standup` had no next step.
  - `docs/knowledge-areas.md` now says what happens when an Optional phase is skipped (note it in
    one line, give the next command, record nothing).
  - `pf_rules.py` was run at step 0 of `/pf-11-control-cycle`, before `cost-performance.md` was
    refreshed, so the CPI rule read last cycle's figures (0.95 instead of 0.75 in T5). It now runs
    at step 8, after the refresh; the Project Manager agent, skill, ROADMAP and AUT-02's entry
    below were updated to match.
  - `/pf-13b-archive-stage` could archive the most recent status report, which describes still-open
    work and is what the next cycle compares against; it is now excluded.
  - `/pf-6-plan-organization` now runs `pf_validate.py`, because a missing Accountable (planted in
    T5) is easy to miss by eye and was only caught at the first control cycle.
  - ROADMAP's EXT-03 said the skills review covered "all 9 agents"; it now says the later Scrum
    Master has not been evaluated.
- `pf-evm-reference`'s worked example computed EAC from a rounded CPI (0.83), giving $12,048; the
  exact figure is $12,000 (ETC $7,200, VAC -$2,000). Rounding CPI before dividing is an avoidable
  error, so the example now carries full precision and says why. Found while checking the new
  `pf_evm.py` against it.
- `templates/tracker.template.md` listed five status values but `/pf-14-close-project` and the
  `datacenter-migration` sandbox both use `Descoped`; the template comment now includes it.
- `pf-0-init.prompt.md` numbered two steps "3"; renumbered.
- `_sandbox/datacenter-migration` (gitignored test data) has R-004 (score 15) listed after R-003
  (score 6), against the register's descending-score rule. Missed by the T3 run and found by
  `pf_validate.py`; left as-is.
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
