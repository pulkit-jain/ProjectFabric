<div align="center">
    <img src="assets/logo.png" alt="ProjectFabric logo" width="200" height="200">
    <h1>Project Fabric</h1>
    <h3><em>Manage real projects — not just code — with a coordinated team of AI agents inside GitHub Copilot..</em></h3>
</div>


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
  execution, tracks variance, and controls change. A Scrum Master runs an optional Agile ceremony
  layer (sprint planning, standup, sprint review, retro, backlog refinement) alongside the PMBOK
  track, gated by the project's Workflow Preset — there is no dedicated Product Owner agent, the
  user plays that role for backlog priority and acceptance decisions. Team Members do the work: the
  roster in `organization.md` lists each one as a Person, an AI agent, or a Vendor, and AI team
  members execute individual work packages in their own conversations.
- **State lives in files.** Every artifact is a plain Markdown file under `.pmo/`. Agents are stateless between sessions — they re-read the files. This makes handoffs, audits, and future tooling (dashboards, a real backend) possible without redesigning anything.
- **You are the checkpoint.** Every phase transition, every task assignment, every change request is delivered to you to review before it becomes baseline. Nothing silently rewrites the plan.

## Documentation

| I want to... | Read |
|---|---|
| Try it on a small project, step by step | [Getting started](docs/guides/getting-started.md) |
| Understand the three conversations, presets, and baselines | [How a project runs](docs/guides/how-a-project-runs.md) |
| See what a real project looks like | [Example project](docs/example/README.md) |
| Know what to do in a specific situation | [Scenarios](docs/guides/scenarios.md) |
| Look up a command: when, what to give it, what comes back | [Command reference](docs/guides/command-reference.md) |
| Know what each `.pmo/` file is and who owns it | [Artifact reference](docs/guides/artifact-reference.md) |
| Choose rules for the Team Standards section of `team.md` | [Team standards](docs/guides/team-standards.md) |

### Guides still to write

| Guide | What it will cover |
|---|---|
| Recipes (how-to) | Short task pages: add a vendor, close a skill gap, resume after a full conversation, write automation rules, use the helper scripts, archive a stage |
| Troubleshooting and FAQ | An agent skipped a step, the validator reports a FAIL, a file is out of date, working without Python |
| Customising and extending | `team.md`, the constitution, plugins, adding an agent or a command |
| One-page cheat sheet | The command order and the three conversations on one printable page |
| Guide for sponsors and stakeholders | What you will be asked to approve, and how to read a status report |
| Guide for team members | How a person or a vendor receives a brief and reports back, and how an AI team member works |
| Integration guides | One per integration (Confluence, Jira, Office exports), written when each is built |

## Quick Start

1. Copy this repository's `.github/` and `templates/` folders into your project.
   Optional: Python 3.9+ lets agents run the bundled helper scripts (`.github/skills/pf-helper-scripts/`) for cost maths, consistency checks, and scaffolding. Nothing to install; without Python the agents do those tasks by hand.
2. Open GitHub Copilot Chat in VS Code, in agent mode.
3. Run `/pf-setup-init` to create `.pmo/team.md`, fill it in (it holds your Workflow Preset and team defaults), then run `/pf-setup-init` again to create the rest of the project's `.pmo/` folder. Then follow the planning commands in the table below. Each agent finishes by telling you the next command and which conversation to run it in.

The [getting started tutorial](docs/guides/getting-started.md) walks through a complete mini project.

## Repository Layout

```
.github/
  copilot-instructions.md   # global working agreement, read by every agent
  agents/                   # role definitions (Planner, Risk Manager, ...)
  prompts/                  # /pf-<category>-<action> slash commands, one per workflow step
  skills/                   # on-demand bundled reference material and helper scripts
templates/                  # blank artifact templates, copied into .pmo/ at init
plugins/                    # additive extensions (agents/prompts/templates), core untouched
tools/                      # maintainer scripts (command reference generator)
docs/
  guides/                   # user guides: tutorial, concepts, scenarios, references
  example/                  # a filled-in example project
  architecture.md           # file-based state model, extension points
  knowledge-areas.md        # PMBOK-style coverage matrix and Workflow Presets
  test-plan.md              # test scenarios run so far, coverage matrix, future test backlog
  Reference.md              # credits: projects studied, standards, tools
assets/
  logo.png                  # ProjectFabric logo
```

Each project you run gets a `.pmo/` folder, created by `/pf-setup-init`. Every file in it, with its
owner, is listed in the [artifact reference](docs/guides/artifact-reference.md).

## Commands

Commands are grouped by category. Four categories share a command-name prefix (`setup`, `plan`,
`agile`, `session`); the rest are the plain-verb work loop. For what each command needs from you and
what it returns, see the [command reference](docs/guides/command-reference.md).

| Category | Command | Phase | Produces |
|---|---|---|---|
| Setup | `/pf-setup-init` | Setup | `.pmo/` scaffolded from templates |
| Setup | `/pf-setup-project-constitution` | Initiating | `project-constitution.md` |
| Setup | `/pf-setup-charter` | Initiating | `charter.md` |
| Setup | `/pf-setup-organization` | Initiating | `organization.md` (governance structure, roles, roster start) |
| Plan | `/pf-plan-scope-wbs` | Planning | `scope-statement.md`, `wbs.md` |
| Plan | `/pf-plan-schedule` | Planning | `schedule.md` |
| Plan | `/pf-plan-cost` | Planning | `cost-management-plan.md` |
| Plan | `/pf-plan-risk` | Planning | `risk-register.md` |
| Plan | `/pf-plan-quality` | Planning | `quality-management-plan.md` |
| Plan | `/pf-plan-procurement` | Planning | `procurement-management-plan.md` |
| Plan | `/pf-plan-stakeholders` | Planning | `stakeholder-register.md`, `communications-plan.md` |
| Plan | `/pf-plan-skills` | Planning | `skill-matrix.md` |
| Plan | `/pf-plan-organization` | Planning | `organization.md` (roster settled), `raci.md` |
| Plan | `/pf-plan-resources` | Planning | `resource-management-plan.md` |
| Work loop | `/pf-start-manager` | Executing | Manager session started |
| Work loop | `/pf-assign-task` | Executing | `bus/<member>/task.md` |
| Work loop | `/pf-start-team-member` | Executing | An AI team member executes, logs to `memory/work-packages/` |
| Work loop | `/pf-check-report` | Monitoring | `tracker.md` updated |
| Work loop | `/pf-control-cycle` | Monitoring | `reports/status-<date>.md` |
| Change and decisions | `/pf-change-request` | Controlling | `changes/CR-<id>.md` |
| Change and decisions | `/pf-log-decision` | Controlling | `decisions/DEC-<id>.md` |
| Agile | `/pf-agile-sprint-planning` | Executing | `sprint-backlog.md` |
| Agile | `/pf-agile-standup` | Executing | `standup-log.md` |
| Agile | `/pf-agile-backlog-refinement` | Monitoring | `sprint-backlog.md` upcoming candidates |
| Agile | `/pf-agile-sprint-review` | Monitoring | `sprint-backlog.md` review outcomes |
| Agile | `/pf-agile-sprint-retro` | Monitoring | `retro-log.md` |
| Session | `/pf-session-handoff` | Any | Handoff prompt for a fresh Manager/Team Member instance |
| Session | `/pf-session-archive-stage` | Any | `archives/<stage>/stage-summary.md`, finished-stage files moved out of the live folders |
| Close | `/pf-close-project` | Closing | `closing/lessons-learned.md`, `closing/final-report.md` |

The Agile commands are the optional ceremony layer, gated by the project's Workflow Preset.

## Knowledge Area Coverage

ProjectFabric v1 now covers the full core PMBOK-style knowledge-area set — Integration, Scope,
Schedule, Cost, Risk, Quality, Procurement, Resource, Stakeholder (+ partial Communications), and
Organization. See [docs/knowledge-areas.md](docs/knowledge-areas.md) for the full matrix; only a
dedicated Communications Management agent remains deferred to v2.

## Architecture & Extensibility

ProjectFabric v1 is a prompt/agent framework only — no backend, no UI. It is deliberately architected so a future web UI or MCP server could read the same `.pmo/` files directly. See [docs/architecture.md](docs/architecture.md) for the full architecture, including the five canonical [Design Principles](docs/architecture.md#design-principles) (No infrastructure, State lives in portable plain-text files, The user is the checkpoint, One artifact one owner, Extensibility & customization by addition never modification) that every new feature is evaluated against.

## License

MIT. See [LICENSE](LICENSE).
