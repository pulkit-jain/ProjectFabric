#!/usr/bin/env python3
"""Compute Earned Value metrics for a Full EVM cost-performance.md.

Prints the Full EVM table and the Project Rollup as Markdown, ready to paste. Pure arithmetic:
no files are read or written, and no judgment is applied -- the Status column is left as TBD
for the Cost Manager to set against the thresholds in cost-management-plan.md.

Usage:
  python pf_evm.py --wp "1.1|Script approval|550|550|100|500" --wp "1.2|Video production|8250|8250|100|7500"

Each --wp is  id|name|BAC|PV|percent complete|AC  (name may be omitted: id|BAC|PV|pct|AC).
Formulas are computed at full precision and rounded only for display, so values can differ
slightly from hand calculations that round CPI before dividing.
"""
import argparse
import sys
from decimal import Decimal, InvalidOperation, ROUND_HALF_UP

HEADER = (
    "| WBS ID | Work Package | BAC | PV | EV | AC | CV (EV-AC) | SV (EV-PV) | CPI (EV/AC) | "
    "SPI (EV/PV) | EAC (BAC/CPI) | ETC (EAC-AC) | VAC (BAC-EAC) | Status |"
)
ROLLUP_HEADER = "| BAC | PV | EV | AC | CPI | SPI | EAC | VAC | Status |"


def fail(message):
    sys.stderr.write("error: %s\n" % message)
    sys.exit(2)


def num(text, label):
    try:
        return Decimal(text.replace(",", "").replace("$", "").strip())
    except InvalidOperation:
        fail("%s is not a number: %r" % (label, text))


def parse_wp(value):
    parts = [p.strip() for p in value.split("|")]
    if len(parts) == 5:
        parts.insert(1, "")
    if len(parts) != 6:
        fail("--wp needs id|name|BAC|PV|pct|AC (or id|BAC|PV|pct|AC), got %r" % value)
    wp_id, name, bac, pv, pct, ac = parts
    if not wp_id:
        fail("--wp %r has an empty id" % value)
    row = {
        "id": wp_id,
        "name": name,
        "bac": num(bac, "BAC of %s" % wp_id),
        "pv": num(pv, "PV of %s" % wp_id),
        "pct": num(pct.rstrip("%"), "percent complete of %s" % wp_id),
        "ac": num(ac, "AC of %s" % wp_id),
    }
    if not (Decimal(0) <= row["pct"] <= Decimal(100)):
        fail("percent complete of %s must be between 0 and 100, got %s" % (wp_id, row["pct"]))
    return row


def metrics(bac, pv, ev, ac):
    """Return the derived EVM figures; a figure is None when its divisor is zero."""
    cpi = ev / ac if ac != 0 else None
    spi = ev / pv if pv != 0 else None
    eac = bac / cpi if cpi else None
    return {
        "cv": ev - ac,
        "sv": ev - pv,
        "cpi": cpi,
        "spi": spi,
        "eac": eac,
        "etc": eac - ac if eac is not None else None,
        "vac": bac - eac if eac is not None else None,
    }


def rounded(value, places):
    return value.quantize(Decimal(1).scaleb(-places), rounding=ROUND_HALF_UP)


def money(value, currency, places, signed=False):
    if value is None:
        return "n/a"
    r = rounded(value, places)
    sign = "-" if r < 0 else ("+" if signed and r > 0 else "")
    return "%s%s%s" % (sign, currency, format(abs(r), ",.%df" % places))


def index(value):
    return "n/a" if value is None else format(rounded(value, 2), ".2f")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawTextHelpFormatter)
    ap.add_argument("--wp", action="append", required=True, help="id|name|BAC|PV|pct|AC")
    ap.add_argument("--currency", default="$", help="currency symbol (default $; use '' for none)")
    ap.add_argument("--decimals", type=int, default=0, help="decimal places for money (default 0)")
    args = ap.parse_args()

    cur, dp = args.currency, args.decimals
    rows = [parse_wp(raw) for raw in args.wp]  # validate everything before printing anything
    total = {"bac": Decimal(0), "pv": Decimal(0), "ev": Decimal(0), "ac": Decimal(0)}

    print("## Mode: Full EVM\n")
    print(HEADER)
    print("|" + "---|" * 14)
    for r in rows:
        ev = r["pct"] / Decimal(100) * r["bac"]
        m = metrics(r["bac"], r["pv"], ev, r["ac"])
        for key, val in (("bac", r["bac"]), ("pv", r["pv"]), ("ev", ev), ("ac", r["ac"])):
            total[key] += val
        print("| %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | %s | TBD |" % (
            r["id"], r["name"],
            money(r["bac"], cur, dp), money(r["pv"], cur, dp), money(ev, cur, dp),
            money(r["ac"], cur, dp),
            money(m["cv"], cur, dp, True), money(m["sv"], cur, dp, True),
            index(m["cpi"]), index(m["spi"]),
            money(m["eac"], cur, dp), money(m["etc"], cur, dp), money(m["vac"], cur, dp, True),
        ))

    t = metrics(total["bac"], total["pv"], total["ev"], total["ac"])
    print("\n## Project Rollup\n")
    print(ROLLUP_HEADER)
    print("|" + "---|" * 9)
    print("| %s | %s | %s | %s | %s | %s | %s | %s | TBD |" % (
        money(total["bac"], cur, dp), money(total["pv"], cur, dp), money(total["ev"], cur, dp),
        money(total["ac"], cur, dp), index(t["cpi"]), index(t["spi"]),
        money(t["eac"], cur, dp), money(t["vac"], cur, dp, True),
    ))
    print("\nn/a = undefined because the divisor is zero (no actual cost yet, no planned value, "
          "or no earned value). Status is left as TBD: set it against cost-management-plan.md.")


if __name__ == "__main__":
    main()
