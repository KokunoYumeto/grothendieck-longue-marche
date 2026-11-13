"""Print the French (checked transcription) and the English (output + fixes as assembled in the package) of one scan,
side by side for reading (read-only). usage: python -I -B show_scan_pair_20261113.py UNIT SCAN [MAXCHARS]"""
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
BS = chr(92)
D = Path(__file__).resolve().parent.parent
unit, k = sys.argv[1], int(sys.argv[2])
mx = int(sys.argv[3]) if len(sys.argv) > 3 else 3000


def scan(s, k):
    m = BS + "scanpage{%d}" % k
    i = s.find(m)
    if i < 0:
        return "(scan not found)"
    j = s.find(BS + "scanpage{", i + len(m))
    return s[i:j if j > 0 else len(s)]


fr = scan((D / "source" / "units" / (unit + ".tex")).read_text(encoding="utf-8"), k)
pk = unit.rsplit("_s", 1)[0]
en = scan((D / "translation" / "packages" / (pk + "_en.tex")).read_text(encoding="utf-8"), k)
print("=== FR", unit, k, len(fr), "chars\n" + fr[:mx])
print("=== EN", pk, k, len(en), "chars\n" + en[:mx])
