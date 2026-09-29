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
| Project Organization | Planning | `raci.md` | Project Manager |
| Resource Management (depth) | Planning, Monitoring & Controlling | `resource-management-plan.md`, `resource-allocation.md` | Resource Manager |
| Procurement Management | Planning, Monitoring & Controlling | `procurement-management-plan.md`, `vendor-contract-register.md` | Procurement Manager |

## v2 — Planned, not yet implemented

| Knowledge Area | Why deferred | What v2 would add |
|---|---|---|
| Communications Management (full) | Folded into Stakeholder Manager for v1 | Dedicated agent if communications complexity outgrows what Stakeholder Manager can own alongside engagement |

## Workflow Presets

Not every project needs every v1 knowledge area run as a dedicated planning step. Chosen once at
`/pf-0-init` and recorded in `.pmo/constitution.md`'s Workflow Preset field, a preset tells every
agent which phases are `Required` (always run before Executing begins) vs. `Optional` (the owning
agent asks the user whether to run it or skip it for this project, rather than assuming yes).
`Optional` never means "silently skipped" — an agent still surfaces the choice once.

| Knowledge Area / Phase | classic-waterfall | agile-hybrid | lean |
|---|---|---|---|
| Constitution | Recommended | Recommended | Optional |
| Charter | Required | Required | Required |
| Scope + WBS | Required | Required | Required |
| Schedule | Required | Required | Required |
| Cost Management | Required | Optional (pull in when needed) | Optional |
| Risk Management | Required | Required | Optional |
| Quality Management | Required | Optional (pull in when needed) | Optional |
| Procurement Management | Required | Optional (pull in when needed) | Optional |
| Stakeholder + Communications | Required | Required | Optional |
| RACI (Organization) | Required | Required | Required |
| Resource Management (depth) | Required | Optional (pull in when needed) | Optional |

- **classic-waterfall** (default): full PMBOK coverage, every phase runs in the order in
  `docs/architecture.md`'s Process flow diagram.
- **agile-hybrid**: keeps the scope/schedule/risk/stakeholder/RACI backbone but treats
  Cost, Quality, Procurement, and Resource-depth planning as pull-based — plan them only once the
  project actually needs formal tracking, a quality gate, a vendor contract, or capacity
  conflicts, rather than by default. Pairs with the still-planned Agile ceremony layer in
  `ROADMAP.md`.
- **lean**: only the phases needed to start assigning and tracking work are required; everything
  else is offered but skipped unless the user asks for it. Intended for small or short-lived
  projects where full PMBOK ceremony would cost more than it returns.

An agent whose phase is `Optional` for the active preset must still ask once ("this project is
using the lean preset — do you want a Cost Management Plan, or should we skip formal cost
tracking?") rather than silently omitting the artifact.

## Design principle

Each v1 artifact's schema was written to be additive-compatible with its v2 extension — e.g.
`tracker.md` already has a `% Complete` column that Earned Value calculations can consume later,
and `wbs.md`'s WBS Dictionary already has an `Owner` column that a Resource Manager can extend
with capacity data — so v2 knowledge areas can be added without breaking v1 files or agents.
