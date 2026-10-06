#!/usr/bin/env python3
"""Scaffold a project's .pmo/ folder from templates/ (what /pf-setup-init describes), in two passes.

Pass 1 (--team-only): create .pmo/team.md from the blank template and stop, so the user can fill it.
Pass 2 (default): refuse unless team.md is filled in, then create the standard artifact files
(template name minus '.template') and the empty working folders, and write the Workflow Preset
from team.md into constitution.md. Never overwrites: an existing file or folder is kept and reported.

team.md counts as filled when the Team name is set, every row of the Team Defaults table has a value
other than TBD (Workflow Preset must be one of the three presets), and Team Standards has at least
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
    "team", "constitution", "charter", "scope-statement", "wbs", "schedule",
    "cost-management-plan", "cost-performance", "risk-register", "stakeholder-register", "raci",
    "communications-plan", "tracker", "automation-rules", "sprint-backlog", "standup-log", "retro-log",
]
FOLDERS = [
    "bus", "memory/work-packages", "reports", "changes", "decisions", "archives", "closing",
]
PRESETS = ("classic-waterfall", "agile-hybrid", "lean")
PRESET_PLACEHOLDER = "**Preset:** TBD"
DEFAULT_ROWS = (
    "Workflow Preset", "Cost tracking mode", "Control cycle cadence",
    "Cost variance escalation threshold", "Risk acceptance score ceiling",
)


def section(text, heading):
    m = re.search(r"^## %s\s*$(.*?)(?=^## |\Z)" % re.escape(heading), text, re.S | re.M)
    return m.group(1) if m else ""


def check_team(text):
    """Return (problems, preset). Problems lists what is still missing from team.md."""
    text = re.sub(r"<!--.*?-->", "", text, flags=re.S)
    problems = []
    m = re.search(r"^\*\*Team:\*\*[ \t]*(.*)$", text, re.M)
    if not m or m.group(1).strip().upper() in ("", "TBD"):
        problems.append("Team name is not set")
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
        preset = ""
    if not re.search(r"^\s*\d+\.\s*\S", section(text, "Team Standards"), re.M):
        problems.append("Team Standards: add at least one rule")
    return problems, preset


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
    problems, preset = check_team(team.read_text(encoding="utf-8"))
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
        if name == "constitution":
            text = text.replace(PRESET_PLACEHOLDER, "**Preset:** " + preset, 1)
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
    if (pmo / "constitution.md") in kept:
        print("note: constitution.md already existed, so the Workflow Preset was not written to it")
    print("\nWorkflow Preset from team.md: %s" % preset)
    print("%d %s, %d kept" % (len(created), "would be created" if args.dry_run else "created", len(kept)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
