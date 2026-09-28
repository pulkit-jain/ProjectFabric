# ProjectFabric Roadmap

Governance document tracking what ProjectFabric covers today, what's planned next, and what was
considered and deliberately not pursued. For line-by-line change history see
[CHANGELOG.md](CHANGELOG.md); for the full v1/v2 knowledge-area rationale see
[docs/knowledge-areas.md](docs/knowledge-areas.md).

Status legend: ✅ Done · 🔜 Planned (not started) · ⏸ Deferred (intentionally, for now) ·
❌ Rejected (evaluated, not adopting)

## Knowledge Area Coverage (PMBOK-style)

| Knowledge Area | Status | Artifact(s) | Owning Agent |
|---|---|---|---|
| Integration Management | ✅ Done | `charter.md`, `tracker.md`, status reports, change requests | Project Manager (+ Planner for Charter) |
| Scope Management | ✅ Done | `scope-statement.md`, `wbs.md` | Planner |
| Schedule Management | ✅ Done | `schedule.md` | Planner |
| Cost Management | ✅ Done | `cost-management-plan.md`, `cost-performance.md` (Lightweight or Full EVM mode) | Cost Manager |
| Risk Management | ✅ Done | `risk-register.md` | Risk Manager |
| Stakeholder Management | ✅ Done | `stakeholder-register.md` | Stakeholder Manager |
| Communications Management (partial) | ✅ Done | `communications-plan.md` | Stakeholder Manager |
| Project Organization | ✅ Done | `raci.md` | Project Manager |
| Resource Management (depth) | ✅ Done | `resource-management-plan.md`, `resource-allocation.md` | Resource Manager |
| Quality Management | ✅ Done | `quality-management-plan.md`, `quality-control-log.md` (QA gate before "Done") | Quality Manager |
| **Procurement Management** | 🔜 **Next** | Make-or-buy analysis, vendor/contract register | Procurement Manager (new) |
| Communications Management (full) | ⏸ Deferred | Dedicated agent if complexity outgrows Stakeholder Manager | — |

## Framework Features

Evaluated against 10 reference multi-agent PM/SDLC repos and GitHub Spec Kit (see
`/memories/repo/reference-repos-comparison.md` for full research notes).

| Feature | Status | Notes |
|---|---|---|
| Project Constitution (`/pf-0b-constitution`) | ✅ Done | Project-specific principles, decision authority, reporting cadence, escalation rules — layered on top of framework-wide `copilot-instructions.md`. Inspired by GitHub Spec Kit. |
| Checkpoint/resume hints | ✅ Done | `/pf-7`, `/pf-9`, `/pf-11` proactively point to `/pf-13-handoff` before hitting a context limit, not just after. |
| Handoff protocol | ✅ Done (basic) | `/pf-13-handoff` exists. Lighter than APM's two-artifact (Handover_File + Handover_Prompt) pattern — revisit only if single-prompt handoff proves insufficient in practice. |
| Definition of Ready checklist (before Work Package assignment) | 🔜 Planned | From copilot-scrum-team / ai-sdlc DoR rubric. |
| Decision log (`.pmo/decisions/`, lifecycle draft→signed-off→superseded) | 🔜 Planned | From ai-sdlc RFC pattern. For judgment calls that aren't scope/schedule/budget changes (so don't need a full Change Request). |
| Structured status-update headers (`## AgentName - ActionType`) | 🔜 Planned | Trivial consistency win from ai-scrum-master-template. |
| Scope/workflow presets (classic-waterfall / agile-hybrid / lean) at `/pf-0-init` | 🔜 Planned | From aidlc-workflows "scope" concept — vary which phases/gates run per project size. |
| Agile/Scrum ceremony layer (sprint planning, standup, retro, backlog refinement) | 🔜 Planned | Alternate track alongside the PMBOK waterfall track, from copilot-scrum-team. Larger effort — needs its own design pass. |
| Plugin/extension pattern (`plugins/<name>/` additive, untouched core) | 🔜 Planned | From aidlc-workflows. Low priority until a real third-party extension need appears. |
| Agent frontmatter tier + `disallowedTools` (judgment/execution/advisory) | 🔜 Planned | From aidlc-workflows AGENTS.md convention. Low priority, clarity-only change. |
| Memory/session archiving (`.pmo/archives/`, stage summaries) | 🔜 Planned | From APM. Only valuable once projects routinely run long enough to need it. |
| MCP server exposing `.pmo/` as tools | ⏸ Deferred | Already an explicit v2 extension point in `docs/architecture.md`. Requires actual code — contradicts v1's zero-code, pure-Markdown design; revisit once v1 knowledge areas are complete. |
| Multi-assistant support (Claude/Cursor folders) | ⏸ Deferred | No second assistant to support yet; revisit if requested. |
| Full backend/UI (dashboard, Kanban board, real-time board) | ❌ Rejected | Evaluated via agent-scrum, paca, ai-sdlc dashboard. Contradicts the pure-prompt, no-backend architecture — a future read-only renderer over `.pmo/` remains a valid v2+ idea, but not a priority. |
| Database-backed state (Postgres/SQLite) | ❌ Rejected | Markdown + git is the state model by design; a database would break "state lives in files, diffable, human-readable." |
| Workflow execution engine / CLI installer (à la Spec Kit's `specify` CLI) | ❌ Rejected | Copilot-only, manual-copy distribution is intentional; no multi-agent abstraction layer needed at current scope. |
| Embedding-based routing / iterative LLM evaluator loops | ❌ Rejected | User-approval gates already act as the quality gate; added LLM calls/cost aren't justified. |

## Next Up

1. **Procurement Management** — dedicated Procurement Manager agent, make-or-buy analysis,
   vendor/contract register cross-referenced with `risk-register.md`.
2. Re-evaluate the "Framework Features" backlog above once the PJM knowledge-area kit is complete.

## Governance

- One artifact, one owner — see the Artifact Ownership table in
  [.github/copilot-instructions.md](.github/copilot-instructions.md).
- Baseline documents (`charter.md`, `wbs.md`, `schedule.md`, `cost-management-plan.md`,
  `resource-management-plan.md`, `quality-management-plan.md`, `constitution.md`) change only
  through `/pf-12-change-request`, never by direct edit, once approved.
- New `/pf-N` commands are inserted with letter suffixes (e.g. `/pf-3b-plan-cost`,
  `/pf-6b-plan-resources`) between existing numbered commands rather than renumbering, so no
  existing command name ever changes.
- New knowledge areas get a dedicated agent + template(s) + a `/pf-N` prompt, and must be wired
  into `copilot-instructions.md`, `docs/knowledge-areas.md`, `README.md`, and
  `docs/architecture.md` in the same change.
- This file and `CHANGELOG.md` are both updated in the same turn as any change to this repo.
