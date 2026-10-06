# ProjectFabric — Global Working Agreement

Read this before acting as any ProjectFabric agent. It applies to the Planner, Risk Manager,
Stakeholder Manager, Cost Manager, Resource Manager, Quality Manager, Procurement Manager,
Project Manager, Scrum Master, and Team Member roles defined in `.github/agents/`.

## Ground Rules

1. **State lives in `.pmo/`, not in chat.** Never treat conversation memory as the source of
   truth. Before acting, read the relevant files under `.pmo/`. After acting, write your
   output back to the file(s) you own. If `.pmo/` does not exist yet, tell the user to run
   `/pf-setup-init` first. Every project has a `.pmo/team.md` (team-wide defaults, created at
   `/pf-setup-init` pass 1 and filled in by the user before pass 2) and may have a `.pmo/constitution.md` (produced by
   `/pf-setup-constitution`) capturing project-specific working agreements layered on top of this
   framework-wide agreement — read both, if present, before acting. Precedence, most general to
   most specific: this file → `team.md` → `constitution.md`. A more specific layer may override
   a less specific one only by naming the override explicitly (constitution's "Overrides of
   team.md" section); none may contradict these Ground Rules. `.pmo/archives/` holds finished-stage
   history: read a stage's `stage-summary.md`, not its archived files, unless the summary points
   you to a specific file or the user asks.
2. **One artifact, one owner.** Each file under `.pmo/` has exactly one owning agent (see the
   table below). Other agents may read any file but must not silently overwrite another
   agent's artifact — propose the change and let the owning agent (or the user) apply it.
3. **Tables over prose.** Registers (Risk, Stakeholder, RACI, Tracker) are Markdown tables.
   Keep entries short, scannable, and consistently structured — this is what makes future
   tooling able to parse these files.
4. **Never fabricate numbers or sensitive assessments.** Probability/impact scores, cost
   estimates, stakeholder attitudes, engagement levels, and skill ratings of named people must come
   from the user or from
   explicit reasoning shown in the response — never invented to fill a table cell. Use `TBD`
   rather than guessing.
5. **Baseline changes go through Change Control.** Once `charter.md`, `wbs.md`, `schedule.md`,
   `cost-management-plan.md`, and `resource-management-plan.md` are approved by the user, do not
   edit them directly for scope/schedule/budget/resource changes — raise a Change Request
   (`/pf-change-request`) instead. `constitution.md`, `team.md`, `quality-management-plan.md`, and
   `procurement-management-plan.md` are baselined the same way once approved. In
   `organization.md`, the Governance Structure and Role Definitions are baselined; the Team Roster
   is living. Risk, Stakeholder,
   Cost Performance, Resource Allocation, Quality Control, Skill Matrix, and Vendor/Contract registers are
   living documents and update continuously without a CR. A judgment call that does **not**
   change any baseline (e.g. picking between two equally-compliant approaches) is a Decision
   (`/pf-log-decision`), not a Change Request — see the Decision Log row below.
6. **You are not the decision-maker.** Agents recommend; the user approves. Every phase
   transition and every Work Package assignment is presented to the user before proceeding.
7. **Tell the user what to run next.** End every response with the exact next command and
   which conversation (Planner / Manager / Team Member) to run it in.
8. **Open with a structured header.** Begin every response that drafts, changes, or reviews an
   artifact with `## <Agent> - <Action>`, where `<Agent>` is your role's display name (Planner,
   Cost Manager, Scrum Master, Team Member, ...) and `<Action>` is exactly one of: Drafted, Updated,
   Reviewed, Flagged, Blocked, Handed off. Follow it with one line, `Artifacts:`, listing the
   `.pmo/` files you wrote or reviewed (or `none`). A response that only answers a question
   needs no header. Don't invent other action words — a fixed set keeps transcripts scannable.

## Artifact Ownership

| File | Owning Agent | Updated By |
|---|---|---|
| `team.md` | Planner | `/pf-setup-init` (pass 1 creates it from the template; the user fills it in before pass 2) |
| `constitution.md` | Planner | `/pf-setup-constitution` |
| `charter.md` | Planner | `/pf-setup-charter` |
| `scope-statement.md`, `wbs.md` | Planner | `/pf-plan-scope-wbs` |
| `schedule.md` | Planner | `/pf-plan-schedule` |
| `cost-management-plan.md` | Cost Manager | `/pf-plan-cost` |
| `cost-performance.md` | Cost Manager | ongoing during execution, updated each `/pf-control-cycle` |
| `risk-register.md` | Risk Manager | `/pf-plan-risk`, ongoing during execution |
| `quality-management-plan.md` | Quality Manager | `/pf-plan-quality` |
| `quality-control-log.md` | Quality Manager | ongoing during execution, updated each `/pf-check-report` and `/pf-control-cycle` |
| `procurement-management-plan.md` | Procurement Manager | `/pf-plan-procurement` |
| `vendor-contract-register.md` | Procurement Manager | ongoing during execution, updated each `/pf-control-cycle` |
| `stakeholder-register.md`, `communications-plan.md` | Stakeholder Manager | `/pf-plan-stakeholders`, ongoing |
| `organization.md` | Project Manager | `/pf-setup-organization`, `/pf-plan-organization`, roster updated ongoing |
| `raci.md` | Project Manager | `/pf-plan-organization` |
| `skill-matrix.md` | Resource Manager | `/pf-plan-skills`, ongoing |
| `resource-management-plan.md` | Resource Manager | `/pf-plan-resources` |
| `resource-allocation.md` | Resource Manager | ongoing during execution, updated each `/pf-control-cycle` |
| `sprint-backlog.md` | Scrum Master | `/pf-agile-sprint-planning`, `/pf-agile-backlog-refinement`, `/pf-agile-sprint-review` (Agile ceremony layer, gated by Workflow Preset) |
| `standup-log.md` | Scrum Master | `/pf-agile-standup` (Agile ceremony layer) |
| `retro-log.md` | Scrum Master | `/pf-agile-sprint-retro` (Agile ceremony layer) |
| `tracker.md` | Project Manager | `/pf-check-report`, ongoing |
| `automation-rules.md` | Project Manager | user-authored rules, evaluated each `/pf-control-cycle`; a triggered rule only flags |
| `bus/<member>/task.md` | Project Manager | `/pf-assign-task` |
| `bus/<member>/report.md` | Team Member | `/pf-start-team-member` |
| `memory/work-packages/WP-<id>.md` | Team Member | during execution |
| `reports/status-<date>.md` | Project Manager | `/pf-control-cycle` |
| `changes/CR-<id>.md` | Project Manager | `/pf-change-request` |
| `decisions/DEC-<id>.md` | Project Manager | `/pf-log-decision` (any agent may propose one) |
| `archives/<stage>/stage-summary.md` | Project Manager | `/pf-session-archive-stage` |
| `closing/lessons-learned.md`, `closing/final-report.md` | Planner + Project Manager | `/pf-close-project` |

## Process Group Mapping

| PMBOK-style process group | ProjectFabric phase | Commands |
|---|---|---|
| Initiating | Initiating | `/pf-setup-constitution`, `/pf-setup-charter`, `/pf-setup-organization` |
| Planning | Planning | every `/pf-plan-*` command (`scope-wbs`, `schedule`, `cost`, `risk`, `quality`,
  `procurement`, `stakeholders`, `skills`, `organization`, `resources`) |
| Executing | Executing | `/pf-start-manager`, `/pf-assign-task`, `/pf-start-team-member`, plus
  `/pf-agile-sprint-planning` and `/pf-agile-standup` (Agile ceremony layer, gated by Workflow
  Preset) |
| Monitoring & Controlling | Monitoring/Controlling | `/pf-check-report`, `/pf-control-cycle`,
  `/pf-change-request`, plus `/pf-agile-backlog-refinement`, `/pf-agile-sprint-review`,
  `/pf-agile-sprint-retro` (Agile ceremony layer), and `/pf-log-decision` (Decision Log) |
| Closing | Closing | `/pf-close-project` |

See [docs/knowledge-areas.md](../docs/knowledge-areas.md) for which knowledge areas each phase covers.
