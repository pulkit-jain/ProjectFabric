#!/usr/bin/env python3
"""Read-only consistency checks over a project's .pmo/ folder.

Checks the mechanical rules that agents otherwise re-derive by reading tables:
  WBS      hierarchy leaves match the WBS Dictionary; unique IDs; acceptance criteria present
  RACI     exactly one Accountable per work package; IDs match the WBS Dictionary
  Org      roster IDs unique, valid Type and Status; RACI columns and bus/ folders match the roster
  Skills   skill-matrix IDs resolve to the catalog, WBS, and roster; uncovered requirements warned
  Risks    unique IDs; scores are Probability x Impact; sorted by score, descending
  Tracker  IDs match the WBS Dictionary; valid status; Done means 100%; linked R-/CR- IDs exist
  Bus      every bus/<member>/task.md points at a tracker row that has actually been started
  Sprint   every sprint-backlog.md WBS ID exists in the WBS Dictionary

Nothing is modified. Rows whose name/description column is blank are unfilled template
placeholders and are skipped. Exit code: 0 = no FAIL, 1 = at least one FAIL, 2 = bad usage.

Usage:  python pf_validate.py [--pmo .pmo]
"""
import argparse
import re
import sys
from pathlib import Path

COMMENT = re.compile(r"<!--.*?-->", re.S)
SEPARATOR_CELL = re.compile(r":?-{3,}:?")
VALID_STATUS = {"not started", "in progress", "blocked", "review", "done", "descoped"}
MEMBER_TYPES = {"person", "ai", "vendor"}
MEMBER_STATUS = {"proposed", "confirmed", "open"}
LEVELS = {"1", "2", "3", "4"}


class Table(object):
    def __init__(self, headers, rows):
        self.headers = headers
        self.rows = rows

    def header(self, prefix):
        for h in self.headers:
            if h.lower().startswith(prefix.lower()):
                return h
        return None

    def cell(self, row, prefix):
        h = self.header(prefix)
        return row.get(h, "").strip() if h else ""

    def filled(self):
        # Blank second column (name/description) marks an unfilled template placeholder row.
        key = self.headers[1] if len(self.headers) > 1 else self.headers[0]
        return [r for r in self.rows if r.get(key, "").strip()]


def read(path):
    return COMMENT.sub("", path.read_text(encoding="utf-8", errors="replace"))


def split_row(line):
    s = line.strip()
    if s.startswith("|"):
        s = s[1:]
    if s.endswith("|"):
        s = s[:-1]
    return [c.strip() for c in re.split(r"(?<!\\)\|", s)]


def parse_tables(text):
    lines = text.splitlines()
    tables = []
    i = 0
    while i < len(lines) - 1:
        if lines[i].lstrip().startswith("|") and lines[i + 1].lstrip().startswith("|"):
            sep = split_row(lines[i + 1])
            if sep and all(SEPARATOR_CELL.fullmatch(c) for c in sep):
                headers = split_row(lines[i])
                rows = []
                j = i + 2
                while j < len(lines) and lines[j].lstrip().startswith("|"):
                    cells = split_row(lines[j])
                    cells += [""] * (len(headers) - len(cells))
                    rows.append(dict(zip(headers, cells)))
                    j += 1
                tables.append(Table(headers, rows))
                i = j
                continue
        i += 1
    return tables


def find_table(text, *needles):
    for t in parse_tables(text):
        lowered = [h.lower() for h in t.headers]
        if all(any(n.lower() in h for h in lowered) for n in needles):
            return t
    return None


def dupes(values):
    seen, out = set(), []
    for v in values:
        if v in seen and v not in out:
            out.append(v)
        seen.add(v)
    return out


def check_wbs(pmo, res):
    path = pmo / "wbs.md"
    if not path.is_file():
        res.append(("SKIP", "WBS", "wbs.md not found"))
        return None
    text = read(path)
    table = find_table(text, "WBS ID", "Acceptance Criteria")
    rows = table.filled() if table else []
    if not rows:
        res.append(("SKIP", "WBS", "WBS Dictionary has no filled rows yet"))
        return None
    ids = [table.cell(r, "WBS ID") for r in rows]
    ok = True
    for d in dupes(ids):
        res.append(("FAIL", "WBS", "%s appears more than once in the WBS Dictionary" % d))
        ok = False
    for r in rows:
        crit = table.cell(r, "Acceptance Criteria")
        if not crit or crit.upper() == "TBD":
            res.append(("FAIL", "WBS", "%s has no acceptance criteria" % table.cell(r, "WBS ID")))
            ok = False

    m = re.search(r"^##\s+Hierarchy\s*$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    hier = []
    if m:
        for line in m.group(1).splitlines():
            mm = re.match(r"^\s*(\d+(?:\.\d+)*)\.?\s+\S", line)
            if mm:
                hier.append(mm.group(1))
    if hier:
        leaves = {i for i in hier if not any(o.startswith(i + ".") for o in hier)}
        for i in sorted(leaves - set(ids)):
            res.append(("FAIL", "WBS", "leaf %s is in the Hierarchy but has no WBS Dictionary row" % i))
            ok = False
        for i in sorted(set(ids) - leaves):
            res.append(("FAIL", "WBS", "Dictionary row %s is not a leaf of the Hierarchy" % i))
            ok = False
    else:
        res.append(("SKIP", "WBS", "no numbered Hierarchy found; leaf/Dictionary match not checked"))
    if ok:
        res.append(("PASS", "WBS", "%d work packages; Hierarchy leaves match the Dictionary, all have "
                    "acceptance criteria" % len(ids)))
    return set(ids)


def check_raci(pmo, res, wbs_ids):
    path = pmo / "raci.md"
    if not path.is_file():
        res.append(("SKIP", "RACI", "raci.md not found"))
        return
    table = find_table(read(path), "WBS ID", "Work Package")
    rows = table.filled() if table else []
    if not rows:
        res.append(("SKIP", "RACI", "no filled rows yet"))
        return
    wp_header = table.header("Work Package")
    role_cols = table.headers[table.headers.index(wp_header) + 1:]
    ok = True
    ids = []
    for r in rows:
        wid = table.cell(r, "WBS ID")
        ids.append(wid)
        accountable, responsible = [], 0
        for col in role_cols:
            tokens = [t for t in re.split(r"[/,\s]+", r.get(col, "").strip().upper()) if t]
            if "A" in tokens:
                accountable.append(col)
            if "R" in tokens:
                responsible += 1
        if len(accountable) != 1:
            who = ", ".join(accountable) if accountable else "none"
            res.append(("FAIL", "RACI", "%s has %d Accountable (%s); exactly one is required"
                        % (wid, len(accountable), who)))
            ok = False
        if responsible == 0:
            res.append(("WARN", "RACI", "%s has no Responsible" % wid))
    for d in dupes(ids):
        res.append(("FAIL", "RACI", "%s appears more than once" % d))
        ok = False
    if wbs_ids is not None:
        for i in sorted(wbs_ids - set(ids)):
            res.append(("FAIL", "RACI", "WBS work package %s has no RACI row" % i))
            ok = False
        for i in sorted(set(ids) - wbs_ids):
            res.append(("FAIL", "RACI", "RACI row %s is not in the WBS Dictionary" % i))
            ok = False
    if ok:
        res.append(("PASS", "RACI", "%d rows; exactly one Accountable each; IDs match the WBS" % len(ids)))


def rows_with(table, prefix):
    # Rows whose key column is filled; a blank key marks an unfilled template placeholder.
    return [r for r in table.rows if table.cell(r, prefix)] if table else []


def check_org(pmo, res):
    path = pmo / "organization.md"
    if not path.is_file():
        res.append(("SKIP", "Org", "organization.md not found"))
        return None
    text = read(path)
    table = find_table(text, "Member ID", "Type")
    rows = rows_with(table, "Member ID")
    if not rows:
        res.append(("SKIP", "Org", "no roster members yet"))
        return None
    roster, ok = {}, True
    ids = [table.cell(r, "Member ID") for r in rows]
    for d in dupes(ids):
        res.append(("FAIL", "Org", "Member ID %s appears more than once in the Team Roster" % d))
        ok = False
    for r in rows:
        mid, mtype, status = table.cell(r, "Member ID"), table.cell(r, "Type"), table.cell(r, "Status")
        if mtype.lower() not in MEMBER_TYPES:
            res.append(("FAIL", "Org", "%s has Type %r; use Person, AI, or Vendor" % (mid, mtype)))
            ok = False
        if status.lower() not in MEMBER_STATUS:
            res.append(("FAIL", "Org", "%s has Status %r; use Proposed, Confirmed, or Open" % (mid, status)))
            ok = False
        roster[mid.lower()] = (mtype.lower(), status.lower())

    unsettled = [i for i in ids if roster[i.lower()][1] in ("proposed", "open")]
    if unsettled:
        res.append(("WARN", "Org", "%d roster entries are not yet Confirmed: %s" % (len(unsettled), ", ".join(unsettled))))

    raci = pmo / "raci.md"
    rtable = find_table(read(raci), "WBS ID", "Work Package") if raci.is_file() else None
    if rtable and rtable.filled():
        gov = find_table(text, "Body", "Decision Rights")
        allowed = set(roster) | {"project manager", "sponsor"}
        allowed |= {gov.cell(r, "Body").lower() for r in rows_with(gov, "Body")}
        used = [c for c in rtable.headers[rtable.headers.index(rtable.header("Work Package")) + 1:]
                if any(r.get(c, "").strip() for r in rtable.filled())]
        for col in used:
            if col.lower() not in allowed:
                res.append(("FAIL", "Org", "RACI column %r is not a Member ID in the Team Roster" % col))
                ok = False

    bus = pmo / "bus"
    for d in sorted(p for p in bus.iterdir() if p.is_dir()) if bus.is_dir() else []:
        if roster.get(d.name.lower(), ("",))[0] != "ai":
            res.append(("WARN", "Org", "bus/%s has no matching AI member in the Team Roster" % d.name))
    if ok:
        res.append(("PASS", "Org", "%d roster members; IDs unique; Types and Statuses valid; RACI columns "
                    "are roster members" % len(rows)))
    return roster


def check_skills(pmo, res, wbs_ids, roster):
    path = pmo / "skill-matrix.md"
    if not path.is_file():
        res.append(("SKIP", "Skills", "skill-matrix.md not found"))
        return
    text = read(path)
    catalog = find_table(text, "Skill ID", "Category")
    reqs = find_table(text, "WBS ID", "Min Level")
    cov = find_table(text, "Member ID", "Level")
    skills = {catalog.cell(r, "Skill ID") for r in rows_with(catalog, "Skill ID")}
    req_rows, cov_rows = rows_with(reqs, "WBS ID"), rows_with(cov, "Member ID")
    if not skills and not req_rows and not cov_rows:
        res.append(("SKIP", "Skills", "no filled rows yet"))
        return
    ok, needed, best = True, {}, {}
    for r in req_rows:
        wid, sid, lvl = reqs.cell(r, "WBS ID"), reqs.cell(r, "Skill ID"), reqs.cell(r, "Min Level")
        if sid not in skills:
            res.append(("FAIL", "Skills", "requirement for %s names %s, which is not in the Skills Catalog" % (wid, sid)))
            ok = False
        if wbs_ids is not None and wid not in wbs_ids:
            res.append(("FAIL", "Skills", "requirement row %s is not in the WBS Dictionary" % wid))
            ok = False
        if lvl not in LEVELS:
            res.append(("FAIL", "Skills", "requirement %s/%s has Min Level %r; use 1-4" % (wid, sid, lvl)))
            ok = False
        else:
            needed[sid] = max(needed.get(sid, 0), int(lvl))
    for r in cov_rows:
        mid, sid, lvl = cov.cell(r, "Member ID"), cov.cell(r, "Skill ID"), cov.cell(r, "Level")
        if sid not in skills:
            res.append(("FAIL", "Skills", "coverage for %s names %s, which is not in the Skills Catalog" % (mid, sid)))
            ok = False
        if roster is not None and mid.lower() not in roster:
            res.append(("FAIL", "Skills", "coverage row %s is not a Member ID in the Team Roster" % mid))
            ok = False
        if lvl.upper() != "TBD" and lvl not in LEVELS:
            res.append(("FAIL", "Skills", "coverage %s/%s has Level %r; use 1-4 or TBD" % (mid, sid, lvl)))
            ok = False
        elif lvl in LEVELS and (roster is None or roster.get(mid.lower(), ("", ""))[1] != "open"):
            best[sid] = max(best.get(sid, 0), int(lvl))
    gaps = ["%s needs level %d, best rostered coverage is %s" % (s, n, best.get(s) or "none")
            for s, n in sorted(needed.items()) if best.get(s, 0) < n]
    for g in gaps:
        res.append(("WARN", "Skills", g))
    if ok and not gaps:
        res.append(("PASS", "Skills", "%d skills; requirements and coverage resolve; every requirement is covered"
                    % len(skills)))


def check_risks(pmo, res):
    path = pmo / "risk-register.md"
    if not path.is_file():
        res.append(("SKIP", "Risks", "risk-register.md not found"))
        return None
    table = find_table(read(path), "ID", "Probability", "Impact", "Score")
    rows = table.filled() if table else []
    if not rows:
        res.append(("SKIP", "Risks", "no filled rows yet"))
        return None
    ok = True
    ids, scores = [], []
    for r in rows:
        rid = table.cell(r, "ID")
        ids.append(rid)
        p, i, s = table.cell(r, "Probability"), table.cell(r, "Impact"), table.cell(r, "Score")
        if not (p and i and s):
            res.append(("WARN", "Risks", "%s is not fully scored (blank Probability, Impact, or Score)" % rid))
            continue
        if not (re.fullmatch(r"\d+", p) and re.fullmatch(r"\d+", i) and re.fullmatch(r"\d+", s)):
            res.append(("FAIL", "Risks", "%s has a non-numeric Probability, Impact, or Score" % rid))
            ok = False
            continue
        if not (1 <= int(p) <= 5 and 1 <= int(i) <= 5):
            res.append(("FAIL", "Risks", "%s has Probability or Impact outside 1-5" % rid))
            ok = False
        if int(p) * int(i) != int(s):
            res.append(("FAIL", "Risks", "%s Score is %s but %s x %s = %d" % (rid, s, p, i, int(p) * int(i))))
            ok = False
        scores.append((rid, int(s)))
    for d in dupes(ids):
        res.append(("FAIL", "Risks", "%s appears more than once" % d))
        ok = False
    for (a, sa), (b, sb) in zip(scores, scores[1:]):
        if sb > sa:
            res.append(("WARN", "Risks", "not sorted by Score descending (%s=%d comes before %s=%d)"
                        % (a, sa, b, sb)))
            break
    if ok:
        res.append(("PASS", "Risks", "%d risks; IDs unique; scores equal Probability x Impact" % len(ids)))
    return set(ids)


def check_tracker(pmo, res, wbs_ids, risk_ids):
    path = pmo / "tracker.md"
    if not path.is_file():
        res.append(("SKIP", "Tracker", "tracker.md not found"))
        return None
    table = find_table(read(path), "WBS ID", "Status", "% Complete")
    rows = table.filled() if table else []
    if not rows:
        res.append(("SKIP", "Tracker", "no filled rows yet"))
        return None
    cr_dir = pmo / "changes"
    cr_ids = {p.stem for p in cr_dir.glob("CR-*.md")} if cr_dir.is_dir() else None
    ok = True
    info = {}
    for r in rows:
        wid = table.cell(r, "WBS ID")
        status = table.cell(r, "Status")
        owner = table.cell(r, "Owner")
        info[wid] = (owner, status)
        if status.lower() not in VALID_STATUS:
            res.append(("WARN", "Tracker", "%s has unrecognised status %r" % (wid, status)))
        pct = re.search(r"(\d+(?:\.\d+)?)\s*%", table.cell(r, "% Complete"))
        if status.lower() == "done" and not (pct and float(pct.group(1)) == 100):
            res.append(("WARN", "Tracker", "%s is Done but %% Complete is not 100%%" % wid))
        if risk_ids is not None:
            for rid in re.findall(r"\bR-\d+\b", table.cell(r, "Linked Risks")):
                if rid not in risk_ids:
                    res.append(("FAIL", "Tracker", "%s links %s, which is not in risk-register.md" % (wid, rid)))
                    ok = False
        if cr_ids is not None:
            for cid in re.findall(r"\bCR-\d+\b", table.cell(r, "Linked CRs")):
                if cid not in cr_ids:
                    res.append(("FAIL", "Tracker", "%s links %s, but changes/%s.md does not exist" % (wid, cid, cid)))
                    ok = False
    for d in dupes([table.cell(r, "WBS ID") for r in rows]):
        res.append(("FAIL", "Tracker", "%s appears more than once" % d))
        ok = False
    if wbs_ids is not None:
        for i in sorted(wbs_ids - set(info)):
            res.append(("FAIL", "Tracker", "WBS work package %s has no tracker row" % i))
            ok = False
        for i in sorted(set(info) - wbs_ids):
            res.append(("FAIL", "Tracker", "tracker row %s is not in the WBS Dictionary" % i))
            ok = False
    if ok:
        res.append(("PASS", "Tracker", "%d rows; IDs match the WBS; linked risks and CRs exist" % len(info)))
    return info


def check_bus(pmo, res, tracker):
    bus = pmo / "bus"
    tasks = sorted(bus.glob("*/task.md")) if bus.is_dir() else []
    if not tasks:
        res.append(("SKIP", "Bus", "no bus/<member>/task.md files"))
        return
    if tracker is None:
        res.append(("SKIP", "Bus", "tracker not available to compare against"))
        return
    ok = True
    for t in tasks:
        member = t.parent.name
        m = re.search(r"WP-(\d+(?:\.\d+)*)", read(t)[:400])
        if not m:
            res.append(("WARN", "Bus", "%s/task.md has no WP-<id> in its heading" % member))
            continue
        wid = m.group(1)
        if wid not in tracker:
            res.append(("FAIL", "Bus", "%s/task.md is for WP-%s, which is not in the tracker" % (member, wid)))
            ok = False
            continue
        owner, status = tracker[wid]
        if status.lower() == "not started":
            res.append(("FAIL", "Bus", "%s/task.md was written for WP-%s but the tracker still says Not Started"
                        % (member, wid)))
            ok = False
        if owner and owner.lower() != member.lower():
            res.append(("WARN", "Bus", "%s/task.md is for WP-%s but the tracker Owner is %r" % (member, wid, owner)))
    if ok:
        res.append(("PASS", "Bus", "%d task files match started tracker rows" % len(tasks)))


def check_sprint(pmo, res, wbs_ids):
    path = pmo / "sprint-backlog.md"
    if not path.is_file():
        res.append(("SKIP", "Sprint", "sprint-backlog.md not found"))
        return
    if wbs_ids is None:
        res.append(("SKIP", "Sprint", "WBS Dictionary not available to compare against"))
        return
    ok, count = True, 0
    for t in parse_tables(read(path)):
        if t.header("WBS ID") is None:
            continue
        for r in t.filled():
            count += 1
            wid = t.cell(r, "WBS ID")
            if wid not in wbs_ids:
                res.append(("FAIL", "Sprint", "sprint-backlog.md lists %s, which is not in the WBS Dictionary" % wid))
                ok = False
    if count == 0:
        res.append(("SKIP", "Sprint", "no filled rows yet"))
    elif ok:
        res.append(("PASS", "Sprint", "%d backlog rows all exist in the WBS" % count))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--pmo", default=".pmo", help="path to the project's .pmo folder (default .pmo)")
    args = ap.parse_args()
    pmo = Path(args.pmo)
    if not pmo.is_dir():
        sys.stderr.write("error: %s is not a directory; run /pf-setup-init first\n" % pmo)
        return 2

    res = []
    wbs_ids = check_wbs(pmo, res)
    check_raci(pmo, res, wbs_ids)
    roster = check_org(pmo, res)
    check_skills(pmo, res, wbs_ids, roster)
    risk_ids = check_risks(pmo, res)
    tracker = check_tracker(pmo, res, wbs_ids, risk_ids)
    check_bus(pmo, res, tracker)
    check_sprint(pmo, res, wbs_ids)

    for level, area, msg in res:
        print("[%s] %s: %s" % (level, area, msg))
    counts = dict((k, sum(1 for r in res if r[0] == k)) for k in ("PASS", "WARN", "FAIL", "SKIP"))
    print("\n%(PASS)d pass, %(WARN)d warn, %(FAIL)d fail, %(SKIP)d skipped" % counts)
    return 1 if counts["FAIL"] else 0


if __name__ == "__main__":
    sys.exit(main())
