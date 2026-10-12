#!/usr/bin/env python3
"""Turn "Week N" labels into calendar dates, using the Project Start Date in schedule.md.

Week 1 begins on the Project Start Date and every week has 7 calendar days (no working-day
calendar). A "Week N" used as a start means day 1 of that week; used as a finish or milestone
target it means day 7. "Week N-M" is week N's first day to week M's last day. ISO dates
(YYYY-MM-DD) pass through unchanged; any other text is free text and has no date.

Nothing is modified. Exit code: 0 = ok, 1 = a value could not be converted, 2 = bad usage.

Usage:
  python pf_dates.py --convert "Week 3" --start 2027-01-04 [--end]
  python pf_dates.py [--pmo .pmo]        # list the schedule and tracker dates with calendar dates
"""
import argparse
import re
import sys
from datetime import date, timedelta
from pathlib import Path

BLANK = {"", "tbd", "-", "\u2014", "\u2013", "n/a"}
ISO_SHAPE = re.compile(r"\d{4}-\d{2}-\d{2}")
WEEK = re.compile(r"week\s+(\d+)(?:\s*[-\u2013]\s*(?:week\s+)?(\d+))?", re.I)


def classify(value):
    """Return 'blank', 'iso', 'week' or 'text'."""
    v = value.strip()
    if v.lower() in BLANK:
        return "blank"
    if ISO_SHAPE.fullmatch(v):
        return "iso"
    if WEEK.fullmatch(v):
        return "week"
    return "text"


def parse_start(value):
    """Parse a Project Start Date cell; None while it is blank or TBD. Raises ValueError if malformed."""
    v = value.strip()
    if v.lower() in BLANK:
        return None
    if not ISO_SHAPE.fullmatch(v):
        raise ValueError("%r is not an ISO date (YYYY-MM-DD)" % v)
    return date.fromisoformat(v)


def resolve(value, start, end=False):
    """Calendar date for a cell, or None when it has none (blank, free text, or a week label with no start).

    Raises ValueError for an impossible ISO date or a week number below 1.
    """
    kind = classify(value)
    v = value.strip()
    if kind == "iso":
        try:
            return date.fromisoformat(v)
        except ValueError:
            raise ValueError("%r is not a real calendar date" % v)
    if kind != "week":
        return None
    m = WEEK.fullmatch(v)
    first, last = int(m.group(1)), int(m.group(2) or m.group(1))
    week = last if end else first
    if first < 1 or last < first:
        raise ValueError("%r is not a valid week range" % v)
    if start is None:
        return None
    return start + timedelta(days=7 * week - 1 if end else 7 * (week - 1))


def _list(pmo):
    from pf_validate import find_table, read  # lazy: pf_validate imports this module

    sched = pmo / "schedule.md"
    if not sched.is_file():
        sys.stderr.write("error: %s not found\n" % sched)
        return 2
    text = read(sched)
    cal = find_table(text, "Setting", "Value")
    start = None
    for r in (cal.rows if cal else []):
        if cal.cell(r, "Setting").lower() == "project start date":
            start = parse_start(cal.cell(r, "Value"))
    print("Project Start Date: %s" % (start.isoformat() if start else "not set"))
    bad = 0
    sources = [("schedule.md", find_table(text, "Milestone", "Target"), [("Target", True)]),
               ("schedule.md", find_table(text, "WBS ID", "Planned Start"),
                [("Planned Start", False), ("Planned Finish", True)])]
    tracker = pmo / "tracker.md"
    if tracker.is_file():
        sources.append(("tracker.md", find_table(read(tracker), "WBS ID", "Planned Start"),
                        [("Planned Start", False), ("Planned Finish", True),
                         ("Actual Start", False), ("Actual Finish", True)]))
    for name, table, cols in sources:
        for r in (table.filled() if table else []):
            label = table.cell(r, table.headers[0])
            for col, end in cols:
                raw = table.cell(r, col)
                if classify(raw) not in ("week", "iso"):
                    continue
                try:
                    d = resolve(raw, start, end)
                except ValueError as e:
                    print("  %s  %-10s %-14s ERROR %s" % (name, label, col, e))
                    bad += 1
                    continue
                print("  %s  %-10s %-14s %-10s -> %s" % (name, label, col, raw, d.isoformat() if d else "no date"))
    return 1 if bad else 0


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--convert", metavar="VALUE", help='a cell value such as "Week 3" or "Week 3-4"')
    ap.add_argument("--start", help="Project Start Date (YYYY-MM-DD) for --convert")
    ap.add_argument("--end", action="store_true", help="treat VALUE as a finish or target (last day of the week)")
    ap.add_argument("--pmo", default=".pmo", help="path to the project's .pmo folder (default .pmo)")
    args = ap.parse_args()
    try:
        if args.convert is not None:
            d = resolve(args.convert, parse_start(args.start or ""), args.end)
            print(d.isoformat() if d else "n/a")
            return 0
        pmo = Path(args.pmo)
        if not pmo.is_dir():
            sys.stderr.write("error: %s is not a directory; run /pf-setup-init first\n" % pmo)
            return 2
        return _list(pmo)
    except ValueError as e:
        sys.stderr.write("error: %s\n" % e)
        return 1


if __name__ == "__main__":
    sys.exit(main())
