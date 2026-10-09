#!/usr/bin/env python3
"""Scaffold a project's .pmo/ folder from templates/ (what /pf-setup-init describes), in two passes.

Pass 1 (--team-only): create .pmo/team.md from the blank template and stop, so the user can fill it.
Pass 2 (default): refuse unless team.md is filled in, then create the standard artifact files
(template name minus '.template') and the empty working folders. In project-constitution.md it
copies team.md's five Team Defaults into the Project Defaults table and team.md's Working Rules into
Team Working Rules. Never overwrites: an existing file or folder is kept and reported.

team.md counts as filled when the Team Name is set, every row of the Team Defaults table has a value
other than TBD (Workflow Preset must be one of the four presets), and Working Rules has at least
one rule. Amendments is optional.

Usage:
  python pf_scaffold.py --team-only [--pmo .pmo] [--templates templates] [--dry-run]
  python pf_scaffold.py [--pmo .pmo] [--templates templates] [--dry-run]
"""
import argparse
import re
import sys
from pathlib import Path

# Keep in step with the file list in .github/prompts/pf-setup-init.prompt.md.
ARTIFACTS = [
    "team", "project-constitution", "work-package-definitions", "charter", "scope-statement", "wbs", "schedule",
    "cost-management-plan", "cost-performance", "risk-register", "stakeholder-register", "raci",
    "communications-plan", "tracker", "automation-rules", "sprint-backlog", "standup-log", "retro-log",
]
FOLDERS = [
    "bus", "memory/work-packages", "reports", "changes", "decisions", "archives", "closing",
]
PRESETS = ("classic-waterfall", "agile-hybrid", "lean", "pi-cadence")
DEFAULT_ROWS = (
    "Workflow Preset", "Cost tracking mode", "Control cycle cadence",
    "Cost variance escalation threshold", "Risk acceptance score ceiling",
)


def section(text, heading):
    m = re.search(r"^## %s\s*$(.*?)(?=^## |\Z)" % re.escape(heading), text, re.S | re.M)
    return m.group(1) if m else ""


def check_team(text):
    """Return (problems, rows, rules). Problems lists what is still missing from team.md."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    problems = []
    name = section(text, "Team Name").strip()
    if name.upper() in ("", "TBD"):
        problems.append("Team Name is not set")
    rows = {}
    for line in section(text, "Team Defaults").splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2 and cells[0] not in ("Setting", "") and not set(cells[0]) <= set("-: "):
            rows[cells[0]] = cells[1]
    for name in DEFAULT_ROWS:
        if rows.get(name, "").upper() in ("", "TBD"):
            problems.append("Team Defaults: %s is not set" % name)
    preset = rows.get("Workflow Preset", "").lower()
    if preset and preset != "tbd" and preset not in PRESETS:
        problems.append("Team Defaults: Workflow Preset must be one of %s" % ", ".join(PRESETS))
    rows["Workflow Preset"] = preset
    rules = section(text, "Working Rules").strip()
    if not re.search(r"^\s*\d+\.\s*\S", rules, re.M):
        problems.append("Working Rules: add at least one rule")
    return problems, rows, rules


def fill_constitution(text, rows, rules):
    """Copy team.md's defaults and rules into the constitution template."""
    for name in DEFAULT_ROWS:
        text = re.sub(r"(\| %s \| )TBD( \|)" % re.escape(name),
                      lambda m: m.group(1) + rows[name] + m.group(2), text, count=1)
    return re.sub(r"(## Team Working Rules\b.*?-->\s*)1\.", lambda m: m.group(1) + rules, text, count=1, flags=re.S)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--pmo", default=".pmo", help="target folder (default .pmo)")
    ap.add_argument("--templates", default="templates", help="templates folder (default templates)")
    ap.add_argument("--team-only", action="store_true", help="pass 1: create only team.md, then stop")
    ap.add_argument("--dry-run", action="store_true", help="report what would happen, change nothing")
    args = ap.parse_args()

    pmo, templates = Path(args.pmo), Path(args.templates)
    if not templates.is_dir():
        sys.stderr.write("error: templates folder not found: %s\n" % templates)
        return 2
    missing = [n for n in ARTIFACTS if not (templates / (n + ".template.md")).is_file()]
    if missing:
        sys.stderr.write("error: missing templates: %s\n" % ", ".join(n + ".template.md" for n in missing))
        return 2

    team = pmo / "team.md"
    verb = "would create" if args.dry_run else "created"

    if args.team_only:
        if team.exists():
            print("kept (already exists): %s" % team.as_posix())
            print("\nteam.md already exists: fill it in, then run pass 2 (without --team-only).")
            return 0
        if not args.dry_run:
            pmo.mkdir(parents=True, exist_ok=True)
            team.write_text((templates / "team.template.md").read_text(encoding="utf-8"), encoding="utf-8")
        print("%s: %s" % (verb, team.as_posix()))
        print("\nFill in team.md, then run pass 2 (without --team-only).")
        return 0

    if not team.is_file():
        sys.stderr.write("error: %s not found; run pass 1 first (--team-only)\n" % team)
        return 2
    problems, rows, rules = check_team(team.read_text(encoding="utf-8"))
    if problems:
        sys.stderr.write("error: team.md is not filled in yet; nothing was created:\n")
        for p in problems:
            sys.stderr.write("  - %s\n" % p)
        return 1

    created, kept = [], []
    for name in ARTIFACTS:
        dest = pmo / (name + ".md")
        if dest.exists():
            kept.append(dest)
            continue
        text = (templates / (name + ".template.md")).read_text(encoding="utf-8")
        if name == "project-constitution":
            text = fill_constitution(text, rows, rules)
        if not args.dry_run:
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(text, encoding="utf-8")
        created.append(dest)
    for folder in FOLDERS:
        path = pmo / folder
        if path.exists():
            kept.append(path)
        else:
            if not args.dry_run:
                path.mkdir(parents=True, exist_ok=True)
            created.append(path)

    for p in created:
        print("%s: %s" % (verb, p.as_posix()))
    for p in kept:
        print("kept (already exists): %s" % p.as_posix())
    print("\nWorkflow Preset copied from team.md: %s" % rows["Workflow Preset"])
    print("%d %s, %d kept" % (len(created), "would be created" if args.dry_run else "created", len(kept)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
