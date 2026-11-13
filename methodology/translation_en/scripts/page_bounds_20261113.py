"""Does anything run off the page? The ink bounding box of every page of a PDF (mutool draw -F bbox), compared with the
sheet and with the type area of the readers (A4, 25 mm margins, a 20 mm column for marginal notes at the right, the
page number in the foot). Read-only, 13 Nov 2026.

off the sheet:      ink beyond an edge of the sheet
outside the area:   ink left of the text block, right of the margin-note column, above the head or below the page number
in the note column: ink right of the text block (marginal notes are expected there)
usage: python -I -B page_bounds_20261113.py FILE.pdf [--list]"""
import re
import subprocess
import sys

sys.stdout.reconfigure(encoding="utf-8")
MM = 72 / 25.4
TOL = 1.5  # points; the task's bound is 2pt


def boxes(pdf):
    r = subprocess.run(["mutool", "draw", "-F", "bbox", "-o", "-", pdf], capture_output=True, text=True,
                       encoding="utf-8", errors="replace")
    out = []
    for m in re.finditer(r'<page bbox="([-\d.e]+) ([-\d.e]+) ([-\d.e]+) ([-\d.e]+)" mediabox="([-\d.e]+) ([-\d.e]+) ([-\d.e]+) ([-\d.e]+)"', r.stdout):
        out.append(tuple(float(x) for x in m.groups()))
    return out


def check(pdf):
    off, outside, column = [], [], []
    for i, (x0, y0, x1, y1, mx0, my0, mx1, my1) in enumerate(boxes(pdf), 1):
        if (x0, y0, x1, y1) == (0, 0, 0, 0) or x1 <= x0:
            continue  # an empty page
        left, right = 25 * MM, mx1 - 25 * MM
        col = right + 10 + 20 * MM
        top, foot = 25 * MM - 12, my1 - 25 * MM + 30 + 3
        d = {"left": left - x0, "right": x1 - col, "top": top - y0, "foot": y1 - foot}
        if x0 < mx0 - 0.5 or y0 < my0 - 0.5 or x1 > mx1 + 0.5 or y1 > my1 + 0.5:
            off.append((i, x0, y0, x1, y1))
        elif max(d.values()) > TOL:
            outside.append((i, {k: round(v, 1) for k, v in d.items() if v > TOL}))
        if x1 > right + TOL:
            column.append(i)
    return off, outside, column


if __name__ == "__main__":
    pdf = sys.argv[1]
    off, outside, column = check(pdf)
    n = len(boxes(pdf))
    print("%s: %d pages | off the sheet: %d | outside the type area: %d | with ink in the note column: %d" % (
        pdf.replace("\\", "/").split("/")[-1], n, len(off), len(outside), len(column)))
    if "--list" in sys.argv:
        for i, x0, y0, x1, y1 in off:
            print("  off the sheet p.%d: x %.0f..%.0f  y %.0f..%.0f" % (i, x0, x1, y0, y1))
        for i, d in outside:
            print("  outside the area p.%d: %s" % (i, d))
