"""Compare rerun stdout and JSON outputs with the shipped ones (line endings normalized)."""
import difflib
import json
import sys
from pathlib import Path

shipped = Path(sys.argv[1])   # shipped code folder (read-only)
rerun = Path(sys.argv[2])     # review rerun folder (has code/ and out/)
names = sys.argv[3].split(",")

def norm(text):
    return text.replace("\r\n", "\n").rstrip("\n").split("\n")

for name in names:
    a = shipped / f"{name}.out"
    b = rerun / "out" / f"{name}.out"
    if not a.exists():
        print(f"{name}: no shipped .out")
        continue
    la, lb = norm(a.read_text(encoding="utf-8")), norm(b.read_text(encoding="utf-8"))
    if la == lb:
        print(f"{name}.out: IDENTICAL ({len(la)} lines)")
    else:
        diff = list(difflib.unified_diff(la, lb, "shipped", "rerun", lineterm="", n=0))
        print(f"{name}.out: DIFFERS ({len(diff)} diff lines)")
        for line in diff[:40]:
            print("   ", line[:300])
    ja, jb = shipped / f"{name}.json", rerun / "code" / f"{name}.json"
    if ja.exists() and jb.exists():
        try:
            same = json.loads(ja.read_text(encoding="utf-8")) == json.loads(jb.read_text(encoding="utf-8"))
            print(f"    {name}.json: {'IDENTICAL' if same else 'DIFFERS'}")
        except Exception as exc:  # report, do not hide
            print(f"    {name}.json: could not compare ({exc})")
