#!/usr/bin/env python3
"""Evaluate a project's automation rules against its current .pmo/ state.

Rules live in .pmo/automation-rules.md as a Markdown table. Each is a human-written condition of
the form  <metric> <operator> <number>  plus a flag message and a suggested command. This script
computes the metrics from the .pmo/ files and reports which enabled rules are triggered. It only
reports: it never edits a file and never runs the suggested command -- the user decides.

Usage:
  python pf_rules.py [--pmo .pmo] [--rules path/to/automation-rules.md]
  python pf_rules.py --list-metrics

Exit code: 0 = evaluated (rules may have triggered), 1 = a rule is malformed, 2 = bad usage.
"""
import argparse
import operator
import re
import sys
from pathlib import Path

from pf_validate import find_table, parse_tables, read

OPERATORS = {
    ">=": operator.ge, "<=": operator.le, "==": operator.eq,
    "!=": operator.ne, ">": operator.gt, "<": operator.lt,
}
CONDITION = re.compile(r"^\s*([a-z_]+)\s*(>=|<=|==|!=|>|<)\s*(-?\d+(?:\.\d+)?)\s*$")

METRICS = {
    "blocked_wp_count": "Work packages with tracker Status Blocked",
    "done_pct": "Percent of non-descoped work packages that are Done",
    "open_risk_count": "Risks in the register whose Status does not start with Closed",
    "open_risk_max_score": "Highest Score among open risks (0 if none)",
    "cost_overrun_pct_max": "Worst single-work-package overrun, in %, from a Lightweight cost-performance.md",
    "cpi_min": "Lowest CPI in a Full EVM cost-performance.md",
    "spi_min": "Lowest SPI in a Full EVM cost-performance.md",
    "draft_decision_count": "decisions/DEC-*.md still at Status Draft",
}


def leading_number(text):
    m = re.match(r"^\s*(\d+(?:\.\d+)?)", text)
    return float(m.group(1)) if m else None


def tracker_rows(pmo):
    path = pmo / "tracker.md"
    if not path.is_file():
        return None
    table = find_table(read(path), "WBS ID", "Status", "% Complete")
    return (table, table.filled()) if table else None


def m_blocked_wp_count(pmo):
    t = tracker_rows(pmo)
    if t is None:
        return None
    table, rows = t
    return sum(1 for r in rows if table.cell(r, "Status").lower() == "blocked")


def m_done_pct(pmo):
    t = tracker_rows(pmo)
    if t is None:
        return None
    table, rows = t
    live = [r for r in rows if table.cell(r, "Status").lower() != "descoped"]
    if not live:
        return None
    done = sum(1 for r in live if table.cell(r, "Status").lower() == "done")
    return round(100.0 * done / len(live), 1)


def open_risks(pmo):
    path = pmo / "risk-register.md"
    if not path.is_file():
        return None
    table = find_table(read(path), "ID", "Probability", "Impact", "Score", "Status")
    if not table:
        return None
    return table, [r for r in table.filled() if not table.cell(r, "Status").lower().startswith("closed")]


def m_open_risk_count(pmo):
    found = open_risks(pmo)
    return None if found is None else len(found[1])


def m_open_risk_max_score(pmo):
    found = open_risks(pmo)
    if found is None:
        return None
    table, rows = found
    scores = [int(table.cell(r, "Score")) for r in rows if re.fullmatch(r"\d+", table.cell(r, "Score"))]
    return max(scores) if scores else 0


def cost_tables(pmo):
    path = pmo / "cost-performance.md"
    return parse_tables(read(path)) if path.is_file() else None


def m_cost_overrun_pct_max(pmo):
    tables = cost_tables(pmo)
    if tables is None:
        return None
    found = False
    worst = 0.0
    for t in tables:
        if t.header("Budgeted Cost") and t.header("Variance %"):
            found = True
            for r in t.filled():
                m = re.search(r"(\d+(?:\.\d+)?)\s*%\s*over", t.cell(r, "Variance %"))
                if m:
                    worst = max(worst, float(m.group(1)))
    return worst if found else None


def evm_min(pmo, prefix):
    tables = cost_tables(pmo)
    if tables is None:
        return None
    values = []
    for t in tables:
        if t.header("CPI") and t.header("SPI") and t.header("EAC"):
            for r in t.filled():
                v = leading_number(t.cell(r, prefix))
                if v is not None:
                    values.append(v)
    return min(values) if values else None


def m_cpi_min(pmo):
    return evm_min(pmo, "CPI")


def m_spi_min(pmo):
    return evm_min(pmo, "SPI")


def m_draft_decision_count(pmo):
    folder = pmo / "decisions"
    if not folder.is_dir():
        return None
    count = 0
    for p in folder.glob("DEC-*.md"):
        m = re.search(r"\*\*Status:\*\*\s*(\w+)", read(p))
        if m and m.group(1).lower() == "draft":
            count += 1
    return count


COMPUTE = {
    "blocked_wp_count": m_blocked_wp_count,
    "done_pct": m_done_pct,
    "open_risk_count": m_open_risk_count,
    "open_risk_max_score": m_open_risk_max_score,
    "cost_overrun_pct_max": m_cost_overrun_pct_max,
    "cpi_min": m_cpi_min,
    "spi_min": m_spi_min,
    "draft_decision_count": m_draft_decision_count,
}


def fmt(value):
    return format(value, "g") if isinstance(value, float) else str(value)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--pmo", default=".pmo", help="path to the project's .pmo folder (default .pmo)")
    ap.add_argument("--rules", help="rules file (default <pmo>/automation-rules.md)")
    ap.add_argument("--list-metrics", action="store_true", help="print the available metrics and exit")
    args = ap.parse_args()

    if args.list_metrics:
        for name in sorted(METRICS):
            print("%-22s %s" % (name, METRICS[name]))
        return 0

    pmo = Path(args.pmo)
    rules_path = Path(args.rules) if args.rules else pmo / "automation-rules.md"
    if not pmo.is_dir():
        sys.stderr.write("error: %s is not a directory; run /pf-setup-init first\n" % pmo)
        return 2
    if not rules_path.is_file():
        print("No rules file at %s; nothing to evaluate." % rules_path.as_posix())
        return 0
    table = find_table(read(rules_path), "ID", "Condition", "Enabled")
    if not table:
        sys.stderr.write("error: no rules table (ID | Condition | ... | Enabled) in %s\n" % rules_path)
        return 2

    enabled = triggered = unknown = errors = 0
    cache = {}
    for row in table.filled():
        rid = table.cell(row, "ID")
        if not table.cell(row, "Enabled").lower().startswith("y"):
            continue
        enabled += 1
        m = CONDITION.match(table.cell(row, "Condition"))
        if not m:
            print("[ERROR] %s: condition %r is not '<metric> <operator> <number>'" % (rid, table.cell(row, "Condition")))
            errors += 1
            continue
        metric, op, limit = m.group(1), m.group(2), float(m.group(3))
        if metric not in COMPUTE:
            print("[ERROR] %s: unknown metric %r (see --list-metrics)" % (rid, metric))
            errors += 1
            continue
        if metric not in cache:
            cache[metric] = COMPUTE[metric](pmo)
        value = cache[metric]
        if value is None:
            print("[n/a] %s: %s cannot be computed from the current .pmo/ files" % (rid, metric))
            unknown += 1
        elif OPERATORS[op](value, limit):
            print("[TRIGGERED] %s: %s = %s (rule: %s %s) -- %s Suggest: %s" % (
                rid, metric, fmt(value), op, fmt(limit),
                table.cell(row, "Flag Message") or "(no message)",
                table.cell(row, "Suggest") or "none"))
            triggered += 1
        else:
            print("[ok] %s: %s = %s (rule: %s %s)" % (rid, metric, fmt(value), op, fmt(limit)))

    print("\n%d enabled, %d triggered, %d not computable, %d malformed" % (enabled, triggered, unknown, errors))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
