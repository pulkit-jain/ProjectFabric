# ProjectFabric — Global Working Agreement

Read this before acting as any ProjectFabric agent. It applies to the Planner, Risk Manager,
Stakeholder Manager, Cost Manager, Resource Manager, Quality Manager, Procurement Manager,
Project Manager, Scrum Master, and Worker roles defined in `.github/agents/`.

## Ground Rules

1. **State lives in `.pmo/`, not in chat.** Never treat conversation memory as the source of
   truth. Before acting, read the relevant files under `.pmo/`. After acting, write your
   output back to the file(s) you own. If `.pmo/` does not exist yet, tell the user to run
   `/pf-0-init` first. Individual projects may also have a `.pmo/team.md` (team-wide defaults,
   copied in at `/pf-0-init`) and a `.pmo/constitution.md` (produced by
   `/pf-0b-constitution`) capturing project-specific working agreements layered on top of this
   framework-wide agreement — read both, if present, before acting. Precedence, most general to
   most specific: this file → `team.md` → `constitution.md`. A more specific layer may override
   a less specific one only by naming the override explicitly (constitution's "Overrides of
   team.md" section); none may contradict these Ground Rules.
2. **One artifact, one owner.** Each file under `.pmo/` has exactly one owning agent (see the
   table below). Other agents may read any file but must not silently overwrite another
   agent's artifact — propose the change and let the owning agent (or the user) apply it.
3. **Tables over prose.** Registers (Risk, Stakeholder, RACI, Tracker) are Markdown tables.
   Keep entries short, scannable, and consistently structured — this is what makes future
   tooling able to parse these files.
4. **Never fabricate numbers or sensitive assessments.** Probability/impact scores, cost
   estimates, stakeholder attitudes, and engagement levels must come from the user or from
   explicit reasoning shown in the response — never invented to fill a table cell. Use `TBD`
   rather than guessing.
5. **Baseline changes go through Change Control.** Once `charter.md`, `wbs.md`, `schedule.md`,
   `cost-management-plan.md`, and `resource-management-plan.md` are approved by the user, do not
   edit them directly for scope/schedule/budget/resource changes — raise a Change Request
   (`/pf-12-change-request`) instead. `constitution.md`, `team.md`, `quality-management-plan.md`, and
   `procurement-management-plan.md` are baselined the same way once approved. Risk, Stakeholder,
   Cost Performance, Resource Allocation, Quality Control, and Vendor/Contract registers are
   living documents and update continuously without a CR. A judgment call that does **not**
   change any baseline (e.g. picking between two equally-compliant approaches) is a Decision
   (`/pf-12b-log-decision`), not a Change Request — see the Decision Log row below.
6. **You are not the decision-maker.** Agents recommend; the user approves. Every phase
   transition and every Work Package assignment is presented to the user before proceeding.
7. **Tell the user what to run next.** End every response with the exact next command and
   which conversation (Planner / Manager / Worker) to run it in.

## Artifact Ownership

| File | Owning Agent | Updated By |
|---|---|---|
| `team.md` | Planner | `/pf-0-init` (copied in from the team's shared file, or blank from template) |
| `constitution.md` | Planner | `/pf-0b-constitution` |
| `charter.md` | Planner | `/pf-1-initiate-planner` |
| `scope-statement.md`, `wbs.md` | Planner | `/pf-2-plan-scope-wbs` |
| `schedule.md` | Planner | `/pf-3-plan-schedule` |
| `cost-management-plan.md` | Cost Manager | `/pf-3b-plan-cost` |
| `cost-performance.md` | Cost Manager | ongoing during execution, updated each `/pf-11-control-cycle` |
| `risk-register.md` | Risk Manager | `/pf-4-plan-risk`, ongoing during execution |
| `quality-management-plan.md` | Quality Manager | `/pf-4b-plan-quality` |
| `quality-control-log.md` | Quality Manager | ongoing during execution, updated each `/pf-10-check-report` and `/pf-11-control-cycle` |
| `procurement-management-plan.md` | Procurement Manager | `/pf-4c-plan-procurement` |
| `vendor-contract-register.md` | Procurement Manager | ongoing during execution, updated each `/pf-11-control-cycle` |
| `stakeholder-register.md`, `communications-plan.md` | Stakeholder Manager | `/pf-5-plan-stakeholders`, ongoing |
| `raci.md` | Project Manager | `/pf-6-plan-organization` |
| `resource-management-plan.md` | Resource Manager | `/pf-6b-plan-resources` |
| `resource-allocation.md` | Resource Manager | ongoing during execution, updated each `/pf-11-control-cycle` |
| `sprint-backlog.md` | Scrum Master | `/pf-7b-sprint-planning`, `/pf-10b-backlog-refinement`, `/pf-10c-sprint-review` (Agile ceremony layer, gated by Workflow Preset) |
| `standup-log.md` | Scrum Master | `/pf-8b-standup` (Agile ceremony layer) |
| `retro-log.md` | Scrum Master | `/pf-11b-sprint-retro` (Agile ceremony layer) |
| `tracker.md` | Project Manager | `/pf-10-check-report`, ongoing |
| `bus/<worker>/task.md` | Project Manager | `/pf-8-assign-task` |
| `bus/<worker>/report.md` | Worker | `/pf-9-initiate-worker` |
| `memory/work-packages/WP-<id>.md` | Worker | during execution |
| `reports/status-<date>.md` | Project Manager | `/pf-11-control-cycle` |
| `changes/CR-<id>.md` | Project Manager | `/pf-12-change-request` |
| `decisions/DEC-<id>.md` | Project Manager | `/pf-12b-log-decision` (any agent may propose one) |
| `closing/lessons-learned.md`, `closing/final-report.md` | Planner + Project Manager | `/pf-14-close-project` |

## Process Group Mapping

| PMBOK-style process group | ProjectFabric phase | Commands |
|---|---|---|
| Initiating | Initiating | `/pf-0b-constitution`, `/pf-1-initiate-planner` |
| Planning | Planning | `/pf-2` through `/pf-6`, plus `/pf-3b-plan-cost`, `/pf-4b-plan-quality`,
  `/pf-4c-plan-procurement`, and `/pf-6b-plan-resources` |
| Executing | Executing | `/pf-7`, `/pf-8`, `/pf-9`, plus `/pf-7b-sprint-planning` and `/pf-8b-standup`
  (Agile ceremony layer, gated by Workflow Preset) |
| Monitoring & Controlling | Monitoring/Controlling | `/pf-10`, `/pf-11`, `/pf-12`, plus
  `/pf-10b-backlog-refinement`, `/pf-10c-sprint-review`, `/pf-11b-sprint-retro` (Agile
  ceremony layer), and `/pf-12b-log-decision` (Decision Log) |
| Closing | Closing | `/pf-14` |

See [docs/knowledge-areas.md](../docs/knowledge-areas.md) for which knowledge areas each phase covers.
