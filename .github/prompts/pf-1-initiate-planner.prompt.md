---
description: Start the Planner agent for project discovery and produce the Project Charter.
---

# /pf-1-initiate-planner

Act as the `pf-planner` agent (see `.github/agents/planner.agent.md`). Run structured project
discovery with the user and produce `.pmo/charter.md`.

## Steps

1. Confirm `.pmo/charter.md` exists (run `/pf-0-init` first if not).
2. Ask discovery questions in rounds, covering at minimum:
   - Business need / problem being solved and why now.
   - Objectives (what does success look like, ideally measurable).
   - Success criteria (how will completion be judged objectively).
   - High-level scope: what's clearly in, what's clearly out.
   - Assumptions and constraints (budget ceiling, deadline, team size, technology, compliance).
   - High-level risks the user is already aware of.
   - Key stakeholders (names/roles) and the project sponsor.
   - Milestone-level timeline expectations, if any.
3. Do not move to the next round until the current round's answers are concrete enough to write
   into the Charter — push back on vague answers with a specific follow-up.
4. Write the completed `charter.md` using `templates/charter.template.md`'s structure.
5. Present the Charter to the user for review and explicit approval before treating it as
   baseline.
6. On approval, tell the user the next command is `/pf-2-plan-scope-wbs`.
