# ProjectFabric

Manage real projects — not just code — with a coordinated team of AI agents inside GitHub Copilot.

ProjectFabric brings classic project-management discipline (PMBOK-style knowledge areas: scope, schedule, risk, stakeholders, organization, and more) into an agentic workflow. Instead of one chat trying to remember everything, specialized agents own specific knowledge areas, and all project state lives in structured files under `.pmo/` — not in chat context.

## Why

AI chat sessions degrade as projects grow: requirements get lost, decisions get forgotten, and nobody is actually managing the plan. ProjectFabric fixes this the way real project offices do: a Charter, a WBS, a Risk Register, a Stakeholder Register, and a Tracker are the source of truth. Agents read and write these files; you approve the decisions.

## Core Idea

- **Roles, not one chat.** A Planner runs discovery and produces the plan. A Cost Manager owns
  estimating, budgeting, and cost performance. A Resource Manager owns capacity planning,
  calendars, and allocation across work packages. A Risk Manager owns the Risk Register. A
  Quality Manager owns quality standards, metrics, and the QA gate before a work package can be
  marked Done. A Procurement Manager owns make-or-buy analysis and vendor/contract management. A
  Stakeholder Manager owns stakeholder analysis and engagement. A Project Manager coordinates
  execution, tracks variance, and controls change. Workers execute individual work packages.
- **State lives in files.** Every artifact is a plain Markdown file under `.pmo/`. Agents are stateless between sessions — they re-read the files. This makes handoffs, audits, and future tooling (dashboards, a real backend) possible without redesigning anything.
- **You are the checkpoint.** Every phase transition, every task assignment, every change request is delivered to you to review before it becomes baseline. Nothing silently rewrites the plan.

## Directory Structure

```
.github/
  copilot-instructions.md   # global working agreement, read by every agent
  agents/                   # role definitions (Planner, Risk Manager, ...)
  prompts/                  # /pf-N slash commands, one per workflow step
templates/                  # blank artifact templates, copied into .pmo/ at init
docs/
  architecture.md           # file-based state model, extension points
  knowledge-areas.md        # PMBOK-style coverage matrix (v1 vs planned)
.pmo/                        # created per-project by /pf-0-init (see below)
  constitution.md
  charter.md
  scope-statement.md
  wbs.md
  schedule.md
  cost-management-plan.md
  cost-performance.md
  risk-register.md
  quality-management-plan.md
  quality-control-log.md
  procurement-management-plan.md
  vendor-contract-register.md
  stakeholder-register.md
  raci.md
  resource-management-plan.md
  resource-allocation.md
  communications-plan.md
  tracker.md
  bus/<worker>/task.md, report.md
  memory/work-packages/WP-<id>.md
  reports/status-<date>.md
  changes/CR-<id>.md
  closing/lessons-learned.md, final-report.md
```

## Quick Start

1. Copy this repository's `.github/` and `templates/` directories into your project (or clone this repo at your project root).
2. Open GitHub Copilot Chat in VS Code (agent mode).
3. Run `/pf-0-init` to scaffold `.pmo/` from the templates.
4. Run `/pf-0b-constitution` to set project-specific working agreements (optional but recommended
   — decision authority, reporting cadence, escalation rules).
5. Run `/pf-1-initiate-planner` and answer the discovery questions. This produces your Charter.
6. Follow the Planning phase commands in order (see table below) to build Scope/WBS, Schedule, Risk Register, Stakeholder Register, and RACI.
7. Run `/pf-7-initiate-manager` to start coordinated execution. The Manager tells you exactly which command to run next and in which conversation.

## Commands

| Phase | Command | Produces |
|---|---|---|
| Setup | `/pf-0-init` | `.pmo/` scaffolded from templates |
| Initiating | `/pf-0b-constitution` | `constitution.md` |
| Initiating | `/pf-1-initiate-planner` | `charter.md` |
| Planning | `/pf-2-plan-scope-wbs` | `scope-statement.md`, `wbs.md` |
| Planning | `/pf-3-plan-schedule` | `schedule.md` |
| Planning | `/pf-3b-plan-cost` | `cost-management-plan.md` |
| Planning | `/pf-4-plan-risk` | `risk-register.md` |
| Planning | `/pf-4b-plan-quality` | `quality-management-plan.md` |
| Planning | `/pf-4c-plan-procurement` | `procurement-management-plan.md` |
| Planning | `/pf-5-plan-stakeholders` | `stakeholder-register.md`, `communications-plan.md` |
| Planning | `/pf-6-plan-organization` | `raci.md` |
| Planning | `/pf-6b-plan-resources` | `resource-management-plan.md` |
| Executing | `/pf-7-initiate-manager` | Manager session started |
| Executing | `/pf-8-assign-task` | `bus/<worker>/task.md` |
| Executing | `/pf-9-initiate-worker` | Worker executes, logs to `memory/work-packages/` |
| Monitoring | `/pf-10-check-report` | `tracker.md` updated |
| Monitoring | `/pf-11-control-cycle` | `reports/status-<date>.md` |
| Controlling | `/pf-12-change-request` | `changes/CR-<id>.md` |
| Any | `/pf-13-handoff` | Handoff prompt for a fresh Manager/Worker instance |
| Closing | `/pf-14-close-project` | `closing/lessons-learned.md`, `closing/final-report.md` |

## Knowledge Area Coverage

ProjectFabric v1 now covers the full core PMBOK-style knowledge-area set — Integration, Scope,
Schedule, Cost, Risk, Quality, Procurement, Resource, Stakeholder (+ partial Communications), and
Organization. See [docs/knowledge-areas.md](docs/knowledge-areas.md) for the full matrix; only a
dedicated Communications Management agent remains deferred to v2.

## Architecture & Extensibility

ProjectFabric v1 is a prompt/agent framework only — no backend, no UI. It is deliberately architected so a future web UI or MCP server could read the same `.pmo/` files directly. See [docs/architecture.md](docs/architecture.md).

## License

MIT. See [LICENSE](LICENSE).
