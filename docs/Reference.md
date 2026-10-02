# References

Where ProjectFabric's ideas come from. Every reference has an ID, and **the rest of the repository
cites sources by ID only** (for example "from REF-P05"), never by name. To find out what an ID
stands for, look it up here.

ProjectFabric credits sources for ideas and patterns only: the agents, prompts, templates, scripts
and documentation were written for this project, not copied. A line-by-line comparison against the
studied projects (lines of 60 or more characters) found only the standard Keep a Changelog
boilerplate in common; it does not detect paraphrase, so the credits below stay in place regardless.

ProjectFabric is not affiliated with, or endorsed by, any project, company or standards body
named on this page. Product names and marks belong to their owners.

**ID scheme.** `REF-P` projects studied, `REF-M` methods, standards and publications, `REF-T`
platforms, protocols and tools, `REF-X` technologies named only because a studied project used
them. IDs are permanent: never renumber or reuse one.

## 1. Projects studied (`REF-P`)

Licences are what was found in the copy that was studied. Check each upstream repository for its
current licence before reusing anything from it.

| ID | Project | Source | Licence found | What informed ProjectFabric |
|---|---|---|---|---|
| REF-P01 | GitHub Spec Kit | https://github.com/github/spec-kit | MIT, Copyright GitHub, Inc. | The project constitution (GOV-01) |
| REF-P02 | Agentic Project Management (APM) | https://github.com/sdi2200262/agentic-project-management | Mozilla Public License 2.0 for current versions; v0.3.x and earlier MIT (copyright CobuterMan) | The handoff protocol (SESS-02), memory and session archiving (SESS-03), batch task assignment (WPQ-02), and the lesson that state belongs in files (`docs/architecture.md`) |
| REF-P03 | Claude Code agentic project management | Variant of REF-P02; its README points to the REF-P02 repository | MIT, Copyright CobuterMan | The handoff pattern (SESS-02) |
| REF-P04 | aidlc-workflows | https://github.com/awslabs/aidlc-workflows | MIT-0, Copyright Amazon.com, Inc. or its affiliates | Workflow presets (AGL-01), the team-level layer (GOV-03), the plugin pattern (EXT-01). Its tier-and-deny-list convention was evaluated and replaced by the editor's own `tools:` allow-list (EXT-02) |
| REF-P05 | ai-sdlc | https://github.com/ai-sdlc-framework/ai-sdlc | Apache-2.0 | The decision log (GOV-02), the Definition of Ready rubric (WPQ-01), and the idea of drift detection (AUT-01) |
| REF-P06 | copilot-scrum-team | https://github.com/cguldogan/copilot-scrum-team | No licence file found | The Agile ceremony layer (AGL-02) and the Definition of Ready (WPQ-01) |
| REF-P07 | ai-scrum-master-template | Source URL not found in the copy studied | MIT, Copyright Collo.dev | Structured status headers (REP-01) |
| REF-P08 | paca | https://github.com/Paca-AI/paca | Apache-2.0 | Trigger-action automation rules (AUT-02), scaled down to flag-only rules |
| REF-P09 | agent-scrum | Source URL not found in the copy studied | MIT, Copyright Gad Benram | Studied; its backend and UI stack was evaluated and not adopted (INF-08) |
| REF-P10 | AgenticAI_ND_P2 (agentic workflow for project management, a Udacity project) | Source URL not found in the copy studied | No licence file found | Studied; its embedding-based routing was evaluated and not adopted (AUT-03) |
| REF-P11 | project-management-agentic-workflow | Source URL not found in the copy studied | No licence file found | Studied; no feature adopted |

Where no licence file was found, nothing was copied, and the project is credited for the ideas
only.

## 2. Methods, standards and publications (`REF-M`)

| ID | Name | Used for | Notes |
|---|---|---|---|
| REF-M01 | PMBOK® Guide, Project Management Institute (PMI) | The knowledge areas, process groups, make-or-buy analysis, resource leveling, fast-tracking and crashing | PMBOK and PMI are registered marks of the Project Management Institute, Inc. |
| REF-M02 | Earned Value Management | `pf_evm.py` and the `pf-evm-reference` skill (PV, EV, AC, CV, SV, CPI, SPI, EAC, ETC, VAC) | Standard formulas; also standardised in ANSI/EIA-748 |
| REF-M03 | Critical Path Method | The `pf-critical-path-reference` skill (forward and backward pass, float) | A standard scheduling technique |
| REF-M04 | RACI, RASCI and DACI responsibility matrices | `raci.md` and the `pf-raci-facilitation-reference` skill | Standard techniques |
| REF-M05 | Stakeholder power/interest grid | `stakeholder-register.md` quadrants | Commonly attributed to Aubrey Mendelow |
| REF-M06 | Stakeholder salience model | The `pf-stakeholder-engagement-reference` skill | Mitchell, Agle and Wood (1997), "Toward a Theory of Stakeholder Identification and Salience", Academy of Management Review |
| REF-M07 | Pre-mortem | The `pf-risk-identification-reference` skill | Gary Klein, "Performing a Project Premortem", Harvard Business Review (2007) |
| REF-M08 | SWOT analysis and probability/impact scales | The `pf-risk-identification-reference` skill | Standard techniques |
| REF-M09 | Contract types: fixed-price, time and materials, cost-reimbursable (CPFF, CPIF, CPAF) | The `pf-contract-type-reference` skill | Standard procurement terminology |
| REF-M10 | Scrum and Kanban | The Agile ceremony layer (sprint planning, standup, review, retro, refinement), Definition of Ready and Done, and the planned Kanban preset | Scrum as described in the Scrum Guide by Ken Schwaber and Jeff Sutherland |
| REF-M11 | Keep a Changelog 1.0.0 | The format of `CHANGELOG.md` | https://keepachangelog.com/en/1.0.0/ |
| REF-M12 | Semantic Versioning 2.0.0 | Version numbering in `CHANGELOG.md` | https://semver.org/spec/v2.0.0.html |

## 3. Platforms, protocols and tools (`REF-T`)

| ID | Name | Role in ProjectFabric |
|---|---|---|
| REF-T01 | GitHub Copilot and Visual Studio Code | The host. The layout of agents, prompts and skills follows the editor's custom-agent, prompt-file and agent-skill formats |
| REF-T02 | Model Context Protocol (MCP) | How the planned Jira, Confluence, Outlook and Teams integrations reach external systems, using servers the user configures |
| REF-T03 | Jira and Confluence (Atlassian) | Planned integrations (INF-01 to INF-04.1) and the Confluence designer (REP-04) |
| REF-T04 | Microsoft Outlook, Teams, Excel and PowerPoint | Planned integrations and exports (INF-14, INF-15, REP-02, REP-03) |
| REF-T05 | Git and GitLab | Planned version-control conventions (INF-17) |
| REF-T06 | Python standard library | The helper scripts in `.github/skills/pf-helper-scripts/` |
| REF-T07 | python-pptx | Planned optional dependency for the presentation export (REP-03) |
| REF-T08 | markitdown | Planned example of a document-conversion server for importing existing documents (INF-16) |
| REF-T09 | Marp | Deferred alternative presentation export (REP-05) |
| REF-T10 | OpenTelemetry | Evaluated as one option for agent-activity observability (INF-12); not adopted |

## 4. Technologies named only because a studied project used them (`REF-X`)

The roadmap's rejected items name these so the reasons for declining them are recorded. None is
used by ProjectFabric.

| ID | Technology |
|---|---|
| REF-X01 | LangGraph |
| REF-X02 | SQLite, Postgres and Valkey |
| REF-X03 | SQLAlchemy |
| REF-X04 | WebAssembly sandboxing |
| REF-X05 | WebSockets |
| REF-X06 | Docker and Kubernetes |
| REF-X07 | DSSE attestations |
| REF-X08 | Jinja2 |
| REF-X09 | git worktrees |
| REF-X10 | GitHub Issues with GitHub Actions |

## Citing and maintaining

- **Cite by ID only.** Outside this page, never write the name of a studied project (`REF-P`) or
  its authors. Write the ID, for example "from REF-P05".
- Names of methods, platforms and technologies (`REF-M`, `REF-T`, `REF-X`) may still appear where
  they describe what a feature is or does ("Jira projection", "RACI matrix"). Where one is the
  source of a technique, the reference skills carry a `Sources:` line with its ID.
- When an idea is borrowed from another project, or a new standard, tool or platform is cited
  anywhere in the repository, add it here in the same change. Each `ROADMAP.md` note that says
  "From REF-P…" must match a row in section 1.
