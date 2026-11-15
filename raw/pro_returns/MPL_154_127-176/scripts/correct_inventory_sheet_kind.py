#!/usr/bin/env python3
"""One-time metadata correction from printing already in the frozen transcription."""
from pathlib import Path
from datetime import datetime, timezone
import csv
import hashlib
import io

root = Path(__file__).resolve().parents[1]
path = root / "MPL_154_127-176_inventory.csv"
before = path.read_bytes()
rows = list(csv.DictReader(io.StringIO(before.decode("utf-8"), newline="")))
changed = []
for row in rows:
    if int(row["scan"]) in {141,143,146} and row["sheet_kind"] == "text":
        changed.append((row["scan"],row["element"],row["sheet_kind"],"reused_typed"))
        row["sheet_kind"] = "reused_typed"
if not changed:
    raise SystemExit("No pending correction; refusing a duplicate log entry.")
out = io.StringIO(newline="")
writer = csv.DictWriter(out,fieldnames=list(rows[0]))
writer.writeheader()
writer.writerows(rows)
after = out.getvalue().encode("utf-8")
path.write_bytes(after)
now = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
report = [
    f"INVENTORY SHEET-KIND CORRECTION {now}",
    "Only sheet_kind changed, text -> reused_typed, throughout scans141,143,146.",
    "Reason: the user's category includes a printed sheet whose back was reused.",
    "The existing frozen transcription and inventory already record the printing:",
    "141:TeX310–319; inventoryE07, lower paper show-through, plotter-report words.",
    "143:TeX2–38; inventoryE01/E02, CRAY2 character banner and six printed job rows.",
    "146:TeX331–370; inventoryE08–E10, CRAY2 banner, job rows and journal/news text.",
    "No context interpretation was used; no frozen page or combined file was edited.",
    f"Before SHA256: {hashlib.sha256(before).hexdigest()}",
    f"After SHA256: {hashlib.sha256(after).hexdigest()}",
    f"Changed rows: {len(changed)}; total rows remain {len(rows)}.",
    "scan,element,old_sheet_kind,new_sheet_kind",
] + [",".join(values) for values in changed]
(root / "records/inventory_sheet_kind_correction.txt").write_text("\n".join(report)+"\n",encoding="utf-8")
with (root / "progress.log").open("a",encoding="utf-8") as stream:
    stream.write(f"inventory sheet_kind metadata corrected {now}; scans141,143,146 text to reused_typed from already transcribed printing; no transcription edits\n")
print("\n".join(report))
