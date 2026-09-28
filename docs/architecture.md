# Architecture

## Why file-based state

ProjectFabric agents are stateless between sessions by design — a Planner conversation and a
Manager conversation share no memory except what's written to `.pmo/`. This is the same lesson
mature agent-orchestration frameworks (e.g. Agentic Project Management) apply to software
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
Initiating                    Planning                                                                    Executing / Monitoring & Controlling         Closing
   │                              │                                                                                    │                                    │
   ▼                              ▼                                                                                    ▼                                    ▼
Constitution ─► Charter  ──────►  Scope+WBS ─► Schedule ─► Cost ─► Risk ─► Stakeholder ─► RACI ─► Resources ─►  Manager loop:              Lessons
(Planner)        (Planner)          (Planner)              (Cost Mgr) (Risk Mgr) (Stakeholder Mgr)  (Resource Mgr)  assign → execute → report      Learned +
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
- No cost/resource/quality/procurement modeling — see [knowledge-areas.md](knowledge-areas.md)
  for what's deferred and why.
