# Architecture

## Design Principles

These five principles are the canonical statement of what ProjectFabric v1 deliberately is and
isn't. They're referenced (not re-derived) whenever a new feature is evaluated in
[../ROADMAP.md](../ROADMAP.md)'s Framework Features table — a feature that requires abandoning
one of them needs an explicit, deliberate trade-off decision, not a default.

1. **No infrastructure.** No backend service, no database, no installed CLI/package, no
   long-running or autonomous orchestration engine — every capability is a Markdown agent/prompt
   file that Copilot reads directly, and distribution is a manual folder copy. This does **not**
   mean no code at all: deterministic helper scripts are encouraged wherever a task has one
   provably-correct answer — math (e.g. EVM's PV/EV/AC → CPI/SPI/EAC), sorting (e.g. keeping
   `risk-register.md` ordered by score), schema/ID validation (e.g. WBS 100%-rule, RACI's
   one-Accountable rule, cross-file ID consistency), or file scaffolding (e.g. `/pf-0-init`
   copying templates). These are bundled as assets under a Skill (see the Skills layer in
   `ROADMAP.md`; the shipped set is `.github/skills/pf-helper-scripts/`, Python 3 standard library
   only) or a plain `scripts/` folder, invoked by an agent on demand — they never run
   unattended and never make a decision for the user, they just compute or check one deterministic
   thing an LLM would otherwise do slower, more expensively, and less reliably.
2. **State lives in portable plain-text files.** All project state is plain Markdown under
   `.pmo/` — diffable and readable in any editor or Git host without tooling, and usable fully
   offline. Also Ground Rule 1 in [../.github/copilot-instructions.md](../.github/copilot-instructions.md)
   and [../README.md](../README.md)'s "State lives in files".
3. **The user is the checkpoint.** No autonomous agent dispatch — every phase transition, task
   assignment, and baseline change is delivered to the user for review before it takes effect.
   Also Ground Rule 6 in `copilot-instructions.md` and this doc's "Non-goals for v1" below.
4. **One artifact, one owner.** Each `.pmo/` file has exactly one owning agent; other agents may
   read it but must propose changes rather than silently overwrite it. Also Ground Rule 2 and
   the Artifact Ownership table in `copilot-instructions.md`.
5. **Extensibility & customization by addition, never by modification.** New capability —
   plugins, skills, project-specific customization — must layer on top of the core framework
   without editing it: plugins live under `plugins/<name>/` and install by copying files into
   core directories (see `plugins/README.md`), never patching a core agent/prompt/template in
   place; agents get situational reference material (formulas, checklists, technique catalogs)
   split into a `.github/skills/<name>/SKILL.md` file loaded on demand rather than bloating the
   agent body for every invocation; project-specific working agreements go in
   `.pmo/constitution.md`, and team-wide defaults shared across projects go in `.pmo/team.md`
   (precedence: framework Ground Rules → `team.md` → `constitution.md`, each layered on top of
   — not replacing — the one before). A
   feature that requires editing core files to customize behavior violates this principle.

## Why file-based state

ProjectFabric agents are stateless between sessions by design — a Planner conversation and a
Manager conversation share no memory except what's written to `.pmo/`. This is the same lesson
mature agent-orchestration frameworks (e.g. REF-P02) apply to software
delivery, generalized to full project management: chat context degrades and gets compacted, but
a Markdown file on disk doesn't.

Every artifact is:
- **Plain Markdown**, so it's readable and diffable in any editor or Git host, without tooling.
- **Table-structured** for registers (Risk, Stakeholder, RACI, Tracker), so entries are
  consistent and machine-parseable even though the format is human-first.
- **Single-owner**, per the table in `.github/copilot-instructions.md` — this avoids two agents
  racing to update the same file with conflicting information.

## Process flow

```
Initiating                    Planning                                                                                                                    Executing / Monitoring & Controlling         Closing
   │                              │                                                                                                                                    │                                    │
   ▼                              ▼                                                                                                                                    ▼                                    ▼
Constitution ─► Charter  ──────►  Scope+WBS ─► Schedule ─► Cost ─► Risk ─► Quality ─► Procurement ─► Stakeholder ─► RACI ─► Resources ─►  Manager loop:              Lessons
(Planner)        (Planner)          (Planner)              (Cost Mgr) (Risk Mgr) (Quality Mgr) (Procurement Mgr) (Stakeholder Mgr)  (Resource Mgr)  assign → execute → report      Learned +
                                                                                                                                                       → track → control-cycle       Final
                                                                                                                                                       → (change request as needed)  Report
```

The Manager loop is intentionally cyclical, not a single pass — `assign task → Worker executes →
report → tracker update → periodic control cycle` repeats until the WBS is fully delivered.

## Extension points (v2+)

This v1 is a prompt/agent framework only: no backend process, no UI, no database. It is
architected so a later phase can add those without redesigning the artifact model:

- **Read-only dashboard / UI.** Because every artifact is a well-defined Markdown table, a
  future web UI (Gantt from `schedule.md`, Kanban from `tracker.md`, risk heat-map from
  `risk-register.md`) can be built as a pure reader/renderer over `.pmo/`, with no change to how
  agents write these files.
- **MCP server.** A future `projectfabric-mcp` server could expose `.pmo/` as structured tools
  (`list_risks`, `update_tracker_status`, `get_stakeholder_register`) the same way comparable
  platforms expose their data model to AI clients — again without changing the underlying file
  schema, only adding a typed access layer on top.
- **Structured data migration.** If tables outgrow Markdown (very large registers, need for
  real querying), each template's schema is stable enough to mechanically migrate to
  YAML frontmatter or JSON per-row without changing field names or semantics.
- **CLI installer.** Today, `.github/` and `templates/` are copied manually into a project. A
  future `pf init` CLI (mirroring how comparable frameworks distribute via npm) could automate
  copying, versioning, and updates once the template set stabilizes — this is intentionally
  deferred until the workflow itself has been used and refined.
- **Multi-platform support.** v1 targets GitHub Copilot only (`.github/agents/`,
  `.github/prompts/`). Because agent/prompt content is plain Markdown with light frontmatter,
  porting to Claude Code, Cursor, or other assistants later is a matter of adding a build step
  that copies content into each platform's directory convention — not a rewrite.

## Non-goals for v1

- No autonomous agent dispatch — every phase transition and task assignment is delivered to the
  user for review (see Ground Rule 6 in `copilot-instructions.md`).
- No quality or procurement modeling, and no dedicated Communications agent — see
  [knowledge-areas.md](knowledge-areas.md) for what's deferred and why. Cost Management and
  Resource Management (depth) were originally deferred here too, but are now implemented in v1.
