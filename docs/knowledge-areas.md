# Knowledge Area Coverage

ProjectFabric v1 deliberately covers a core subset of PMBOK-style knowledge areas — the ones with
the highest leverage for getting a project planned and controlled correctly. The rest are
reserved for v2 rather than bolted on shallowly.

## v1 — Implemented

| Knowledge Area | Process Groups Touched | Artifact(s) | Owning Agent |
|---|---|---|---|
| Integration Management | Initiating, Executing, Monitoring & Controlling, Closing | `charter.md`, `tracker.md`, status reports, change requests | Project Manager (+ Planner for Charter) |
| Scope Management | Planning | `scope-statement.md`, `wbs.md` | Planner |
| Schedule Management | Planning | `schedule.md` | Planner |
| Cost Management | Planning, Monitoring & Controlling | `cost-management-plan.md`, `cost-performance.md` | Cost Manager |
| Risk Management | Planning, Monitoring & Controlling | `risk-register.md` | Risk Manager |
| Quality Management | Planning, Executing, Monitoring & Controlling | `quality-management-plan.md`, `quality-control-log.md` | Quality Manager |
| Stakeholder Management | Initiating, Planning, Monitoring & Controlling | `stakeholder-register.md` | Stakeholder Manager |
| Communications Management (partial) | Planning, Executing | `communications-plan.md` | Stakeholder Manager |
| Project Organization | Initiating, Planning | `organization.md`, `raci.md` | Project Manager |
| Resource Management (depth) | Planning, Monitoring & Controlling | `resource-management-plan.md`, `resource-allocation.md`, `skill-matrix.md` | Resource Manager |
| Procurement Management | Planning, Monitoring & Controlling | `procurement-management-plan.md`, `vendor-contract-register.md` | Procurement Manager |

## v2 — Planned, not yet implemented

| Knowledge Area | Why deferred | What v2 would add |
|---|---|---|
| Communications Management (full) | Folded into Stakeholder Manager for v1 | Dedicated agent if communications complexity outgrows what Stakeholder Manager can own alongside engagement |

## Workflow Presets

Not every project needs every v1 knowledge area run as a dedicated planning step. Chosen once in `.pmo/team.md` (filled in during `/pf-setup-init`) and copied by pass 2 into `.pmo/project-constitution.md`'s Project Defaults table, a preset tells every
agent which phases are `Required` (always run before Executing begins) vs. `Optional` (the owning
agent asks the user whether to run it or skip it for this project, rather than assuming yes).
`Optional` never means "silently skipped" — an agent still surfaces the choice once.

| Knowledge Area / Phase | classic-waterfall | agile-hybrid | lean | pi-cadence |
|---|---|---|---|---|
| Constitution | Recommended | Recommended | Optional | Recommended |
| Charter | Required | Required | Required | Required (the yearly product charter) |
| Scope + WBS | Required | Required | Required | Required (for the current PI) |
| Schedule | Required | Required | Required | Required (the PI calendar) |
| Cost Management | Required | Optional (pull in when needed) | Optional | Optional |
| Risk Management | Required | Required | Optional | Required |
| Quality Management | Required | Optional (pull in when needed) | Optional | Required (a release gate) |
| Procurement Management | Required | Optional (pull in when needed) | Optional | Optional |
| Stakeholder + Communications | Required | Required | Optional | Required |
| Organization (governance + roster) | Required | Required | Optional | Required |
| Skills assessment | Required | Required | Optional | Optional |
| RACI | Required | Required | Required | Required |
| Resource Management (depth) | Required | Optional (pull in when needed) | Optional | Optional |
| Agile Ceremony Layer (Scrum Master track) | Off (not offered) | Engaged by default | Optional | Engaged by default |
| Roadmap (yearly plan) | Off (not offered) | Off (not offered) | Off (not offered) | Required |
| PI planning and review | Off (not offered) | Off (not offered) | Off (not offered) | Required |

- **classic-waterfall** (default): full PMBOK coverage, every phase runs in the order in
  `docs/architecture.md`'s Process flow diagram.
- **agile-hybrid**: keeps the scope/schedule/risk/stakeholder/organization/RACI backbone but treats
  Cost, Quality, Procurement, and Resource-depth planning as pull-based — plan them only once the
  project actually needs formal tracking, a quality gate, a vendor contract, or capacity
  conflicts, rather than by default. Pairs with the Agile ceremony layer (Scrum Master agent —
  `/pf-agile-sprint-planning`, `/pf-agile-standup`, `/pf-agile-sprint-review`,
  `/pf-agile-backlog-refinement`, `/pf-agile-sprint-retro`), engaged by default. There is no
  dedicated Product Owner agent — the user plays that role for backlog priority and Sprint
  Review acceptance decisions, per Design Principle 3.
- **lean**: only the phases needed to start assigning and tracking work are required; everything
  else is offered but skipped unless the user asks for it. Intended for small or short-lived
  projects where full PMBOK ceremony would cost more than it returns.
- **pi-cadence**: for a continuing product that plans a year roughly and delivers in fixed-length
  Program Increments (PIs), the date fixed and the scope flexible. A yearly `roadmap.md` holds the
  rough plan; `/pf-plan-pi` plans only the next PI in detail (after the previous one is closed) and
  `/pf-close-pi` closes it. The constitution's PI Practices section switches five practices on or
  off per project: PI objectives with a confidence vote, WSJF prioritization, a PI review, ROAM
  risk handling and a predictability metric. With all five off it is a plain single-team release
  train. It reuses the Agile ceremony layer for the iterations inside a PI.

An agent whose phase is `Optional` for the active preset must still ask once ("this project is
using the lean preset — do you want a Cost Management Plan, or should we skip formal cost
tracking?") rather than silently omitting the artifact. If the user skips it, the agent notes the
skip in one line and gives the next command in the planning chain. Nothing is recorded: later
commands (`/pf-start-manager`, `/pf-control-cycle`) treat a missing Optional artifact as
intentionally skipped.

## Design principle

Each v1 artifact's schema was written to be additive-compatible with its v2 extension — e.g.
`tracker.md` already has a `% Complete` column that Earned Value calculations can consume later,
and `wbs.md`'s WBS Dictionary already has an `Owner` column that a Resource Manager can extend
with capacity data — so v2 knowledge areas can be added without breaking v1 files or agents.
