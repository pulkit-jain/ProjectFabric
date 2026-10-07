#!/usr/bin/env python3
"""Regenerate the command tables in docs/guides/command-reference.md.

Facts that can be read from a prompt file (run-in conversation, files read and written, next
command) are derived. Hand-written facts (when to run, what the user provides, what they get,
which preset row governs it) come from docs/guides/command-notes.md. Preset values are looked up
in the Workflow Presets table of docs/knowledge-areas.md, so they cannot drift from it.

Usage (from the repository root):
  python tools/gen_command_reference.py            rewrite the tables
  python tools/gen_command_reference.py --check    exit 1 if the file on disk is out of date
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROMPTS = ROOT / ".github" / "prompts"
NOTES = ROOT / "docs" / "guides" / "command-notes.md"
TARGET = ROOT / "docs" / "guides" / "command-reference.md"
PRESETS = ROOT / "docs" / "knowledge-areas.md"

# (marker key, member test) in the order the groups appear in the reference page.
SINGLES = {
    "work": {"pf-start-manager", "pf-assign-task", "pf-start-team-member", "pf-check-report", "pf-control-cycle"},
    "change": {"pf-change-request", "pf-log-decision"},
    "close": {"pf-close-project"},
}
PREFIXES = [("setup", "pf-setup-"), ("plan", "pf-plan-"), ("agile", "pf-agile-"), ("session", "pf-session-")]
ORDER = ["setup", "plan", "work", "change", "agile", "session", "close"]
# Usual run order within a group; a command not listed here sorts last, then alphabetically.
RUN_ORDER = [
    "pf-setup-init", "pf-setup-project-constitution", "pf-setup-charter", "pf-setup-organization",
    "pf-plan-scope-wbs", "pf-plan-schedule", "pf-plan-cost", "pf-plan-risk", "pf-plan-quality",
    "pf-plan-procurement", "pf-plan-stakeholders", "pf-plan-skills", "pf-plan-organization",
    "pf-plan-resources",
    "pf-start-manager", "pf-assign-task", "pf-start-team-member", "pf-check-report", "pf-control-cycle",
    "pf-change-request", "pf-log-decision",
    "pf-agile-sprint-planning", "pf-agile-standup", "pf-agile-backlog-refinement",
    "pf-agile-sprint-review", "pf-agile-sprint-retro",
    "pf-session-handoff", "pf-session-archive-stage",
    "pf-close-project",
]

WRITE_VERB = re.compile(r"\b(produce|write|update|append|create|scaffold)\b", re.I)
TOKEN = re.compile(r"`([^`]+)`")
REQUIRED_KEYS = ("When", "You provide", "You get", "Preset")


def group_of(name):
    for key, members in SINGLES.items():
        if name in members:
            return key
    for key, prefix in PREFIXES:
        if name.startswith(prefix):
            return key
    return None


def run_in(name):
    if name == "pf-start-team-member":
        return "Team Member"
    if name == "pf-session-handoff":
        return "The conversation that is full"
    if name.startswith(("pf-setup-", "pf-plan-")):
        return "Planner"
    return "Manager"


def first_paragraph(text):
    lines = text.splitlines()
    start = next((i for i, l in enumerate(lines) if l.startswith("# ")), -1) + 1
    para = []
    for l in lines[start:]:
        if l.strip():
            para.append(l.strip())
        elif para:
            break
    return " ".join(para)


def file_tokens(chunk):
    out = []
    for tok in TOKEN.findall(chunk):
        if tok.startswith((".github", "templates/", "/pf-")) or "pf-" in tok and "/" not in tok:
            continue
        if tok == ".pmo/" or tok.endswith(".md") or tok.endswith("/"):
            tok = tok[5:] if tok.startswith(".pmo/") and tok != ".pmo/" else tok
            if tok not in out:
                out.append(tok)
    return out


def reads_writes(para):
    m = WRITE_VERB.search(para)
    if not m:
        return [], file_tokens(para)
    return file_tokens(para[:m.start()]), file_tokens(para[m.start():])


def next_command(text, own):
    m = re.search(r"^##\s+Steps\s*$(.*?)(?=^##\s|\Z)", text, re.S | re.M)
    if not m:
        return None
    items, cur = [], None
    for line in m.group(1).splitlines():
        if re.match(r"^\s*\d+\.\s", line):
            cur = [line.strip()]
            items.append(cur)
        elif cur is not None and line.strip():
            cur.append(line.strip())
    for item in reversed(items):
        body = " ".join(item)
        if re.search(r"next command|tell the user", body, re.I):
            for tok in re.findall(r"`(/pf-[a-z-]+)`", body):
                if tok != "/" + own:
                    return tok
    return None


def parse_notes(text):
    notes, cur = {}, None
    key = None
    for line in text.splitlines():
        h = re.match(r"^##\s+(/pf-[a-z-]+)\s*$", line)
        if h:
            cur, key = {}, None
            notes[h.group(1)[1:]] = cur
            continue
        b = re.match(r"^-\s+\*\*([^*]+):\*\*\s*(.*)$", line)
        if b and cur is not None:
            key = b.group(1).strip()
            cur[key] = b.group(2).strip()
        elif cur is not None and key and line.startswith("  ") and line.strip():
            cur[key] += " " + line.strip()
    return notes


def preset_table(text):
    rows = {}
    for line in text.splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 4 and not set(cells[0]) <= set("-: ") and cells[0] != "Knowledge Area / Phase":
            rows[cells[0]] = cells[1:]
    return rows


def short(value):
    v = value.lower()
    for prefix, label in (("required", "R"), ("optional", "O"), ("recommended", "Rec"), ("off", "Off"), ("engaged", "On")):
        if v.startswith(prefix):
            return label
    return value


def esc(s):
    return s.replace("|", "\\|").replace("\n", " ")


def build_table(names, notes, presets, prompts):
    out = ["| Command | Run in | When to run | You provide | You get | Files | Next | Preset |",
           "|---|---|---|---|---|---|---|---|"]
    problems = []
    for name in names:
        note = notes[name]
        text = prompts[name]
        para = first_paragraph(text)
        reads, writes = reads_writes(para)
        files = []
        r = note.get("Reads") or ", ".join("`%s`" % t for t in reads)
        w = note.get("Writes") or ", ".join("`%s`" % t for t in writes)
        if r:
            files.append("reads: " + r)
        if w:
            files.append("writes: " + w)
        nxt = note.get("Next") or ("`%s`" % next_command(text, name) if next_command(text, name) else "")
        row = note["Preset"]
        if row.lower() in ("all", "none", ""):
            preset = "All"
        elif row in presets:
            preset = " / ".join(short(v) for v in presets[row])
        else:
            problems.append("%s: preset row %r not found in %s" % (name, row, PRESETS.name))
            preset = "?"
        cells = ["`/%s`" % name, note.get("Run in") or run_in(name), note["When"], note["You provide"],
                 note["You get"], "<br>".join(files) or "none", nxt or "none", preset]
        out.append("| " + " | ".join(esc(c) for c in cells) + " |")
    return "\n".join(out), problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="exit 1 if the file on disk is out of date")
    args = ap.parse_args()

    prompts = {p.name[:-len(".prompt.md")]: p.read_text(encoding="utf-8") for p in PROMPTS.glob("*.prompt.md")}
    notes = parse_notes(NOTES.read_text(encoding="utf-8"))
    presets = preset_table(PRESETS.read_text(encoding="utf-8"))

    problems = []
    for n in sorted(set(prompts) - set(notes)):
        problems.append("no entry in command-notes.md for /%s" % n)
    for n in sorted(set(notes) - set(prompts)):
        problems.append("command-notes.md has an entry for /%s, which has no prompt file" % n)
    for n, note in notes.items():
        for k in REQUIRED_KEYS:
            if not note.get(k):
                problems.append("/%s is missing the %r line in command-notes.md" % (n, k))
    for n in prompts:
        if group_of(n) is None:
            problems.append("/%s does not belong to any group in gen_command_reference.py" % n)
    if problems:
        print("\n".join("error: " + p for p in problems), file=sys.stderr)
        return 2

    groups = {k: [] for k in ORDER}
    for n in sorted(prompts):
        groups[group_of(n)].append(n)
    for names in groups.values():
        names.sort(key=lambda n: (RUN_ORDER.index(n) if n in RUN_ORDER else len(RUN_ORDER), n))

    text = TARGET.read_text(encoding="utf-8")
    for key in ORDER:
        table, problems = build_table(groups[key], notes, presets, prompts)
        if problems:
            print("\n".join("error: " + p for p in problems), file=sys.stderr)
            return 2
        begin, end = "<!-- BEGIN GENERATED: %s -->" % key, "<!-- END GENERATED: %s -->" % key
        pattern = re.compile(re.escape(begin) + r".*?" + re.escape(end), re.S)
        if not pattern.search(text):
            print("error: markers for %r not found in %s" % (key, TARGET.name), file=sys.stderr)
            return 2
        text = pattern.sub(lambda m: begin + "\n" + table + "\n" + end, text)

    if args.check:
        if TARGET.read_text(encoding="utf-8") != text:
            print("out of date: run python tools/gen_command_reference.py", file=sys.stderr)
            return 1
        print("command-reference.md is up to date (%d commands)" % len(prompts))
        return 0
    TARGET.write_text(text, encoding="utf-8")
    print("wrote %s (%d commands)" % (TARGET.relative_to(ROOT).as_posix(), len(prompts)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
