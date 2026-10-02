#!/usr/bin/env python3
"""Scaffold a project's .pmo/ folder from templates/ (what /pf-setup-init describes).

Creates the standard artifact files (template name minus '.template') and the empty working
folders. Never overwrites: an existing file or folder is kept and reported. Optionally fills in
the constitution's Workflow Preset and copies in the team's shared team.md.

Usage:
  python pf_scaffold.py [--pmo .pmo] [--templates templates] [--preset agile-hybrid]
                        [--team path/to/team.md] [--dry-run]
"""
import argparse
import shutil
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


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--pmo", default=".pmo", help="target folder (default .pmo)")
    ap.add_argument("--templates", default="templates", help="templates folder (default templates)")
    ap.add_argument("--preset", choices=PRESETS, help="Workflow Preset to write into constitution.md")
    ap.add_argument("--team", help="existing team.md to copy in instead of the blank template")
    ap.add_argument("--dry-run", action="store_true", help="report what would happen, change nothing")
    args = ap.parse_args()

    pmo, templates = Path(args.pmo), Path(args.templates)
    if not templates.is_dir():
        sys.stderr.write("error: templates folder not found: %s\n" % templates)
        return 2
    team_src = Path(args.team) if args.team else None
    if team_src and not team_src.is_file():
        sys.stderr.write("error: --team file not found: %s\n" % team_src)
        return 2
    missing = [n for n in ARTIFACTS if not (templates / (n + ".template.md")).is_file()]
    if missing:
        sys.stderr.write("error: missing templates: %s\n" % ", ".join(n + ".template.md" for n in missing))
        return 2

    created, kept = [], []
    for name in ARTIFACTS:
        dest = pmo / (name + ".md")
        if dest.exists():
            kept.append(dest)
            continue
        source = team_src if (name == "team" and team_src) else templates / (name + ".template.md")
        text = source.read_text(encoding="utf-8")
        if name == "constitution" and args.preset:
            text = text.replace(PRESET_PLACEHOLDER, "**Preset:** " + args.preset, 1)
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

    verb = "would create" if args.dry_run else "created"
    for p in created:
        print("%s: %s" % (verb, p.as_posix()))
    for p in kept:
        print("kept (already exists): %s" % p.as_posix())
    if args.preset and (pmo / "constitution.md").exists() and (pmo / "constitution.md") in kept:
        print("note: constitution.md already existed, so --preset was not applied")
    print("\n%d %s, %d kept" % (len(created), "would be created" if args.dry_run else "created", len(kept)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
