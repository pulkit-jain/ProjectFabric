# Automation Rules

<!-- Human-written conditions checked at each /pf-control-cycle by pf_rules.py (see the
pf-helper-scripts skill). A triggered rule only FLAGS: it appears in the Status Report with a
suggested command, and the user decides. Nothing runs by itself and no baseline changes
automatically. Living document (no Change Request needed) owned by the Project Manager; the user
edits the rules.

Condition format:  <metric> <operator> <number>   e.g.  cost_overrun_pct_max > 15
Operators: >  >=  <  <=  ==  !=
Metrics: blocked_wp_count, done_pct, open_risk_count, open_risk_max_score, cost_overrun_pct_max,
cpi_min, spi_min, draft_decision_count  (run pf_rules.py --list-metrics for what each measures)

Keep any numbers that mirror a threshold in cost-management-plan.md or the constitution in step
with it -- when that threshold changes, change the rule too.

The rows below are examples with example numbers, all disabled. Set Enabled to Yes and replace
the numbers with this project's real thresholds; don't enable a rule whose number you haven't
chosen (Ground Rule 4). -->

| ID | Condition | Flag Message | Suggest | Enabled |
|---|---|---|---|---|
| A-001 | cost_overrun_pct_max > 15 | A work package is over budget beyond the cost control threshold. | /pf-change-request | No |
| A-002 | cpi_min < 0.9 | Cost performance is behind plan on at least one work package (Full EVM). | /pf-change-request | No |
| A-003 | spi_min < 0.9 | Schedule performance is behind plan on at least one work package (Full EVM). | /pf-change-request | No |
| A-004 | blocked_wp_count >= 1 | A work package is Blocked. | /pf-log-decision | No |
| A-005 | open_risk_max_score >= 15 | An open risk scores at or above the escalation level. | /pf-plan-risk | No |
| A-006 | draft_decision_count >= 1 | A decision is still waiting for sign-off. | /pf-log-decision | No |
| A-007 | done_pct >= 100 | Every work package is Done. | /pf-close-project | No |
