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

## Design principle

Each v1 artifact's schema was written to be additive-compatible with its v2 extension — e.g.
`tracker.md` already has a `% Complete` column that Earned Value calculations can consume later,
and `wbs.md`'s WBS Dictionary already has an `Owner` column that a Resource Manager can extend
with capacity data — so v2 knowledge areas can be added without breaking v1 files or agents.
