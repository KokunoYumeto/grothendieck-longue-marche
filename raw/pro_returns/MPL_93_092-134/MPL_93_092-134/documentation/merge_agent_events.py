"""Map provisional research-agent IDs to final note IDs; preserve dated records.

Only post-freeze research is merged. This script does not alter transcription.
The original event files remain in documentation for provenance.
"""
from pathlib import Path
import csv
import re

ROOT = Path(__file__).resolve().parent / "research_checks"
FIELDS = ["statement_id", "date", "who", "type", "outcome"]
PREFIX = "MPL_93_092-134 "
uniform = {
    "E01": "E01", "E02": "E01.simply_connected_scope", "E03": "E02",
    "E04": "E03", "E05": "E05", "E06": "E06", "E07": "E08",
    "E08": "E10", "E09": "E11", "E10": "E12", "E11": "E13",
    "E12": "E15", "E13": "E16", "E14": "F06", "E15": "F08",
}
s20 = {"F01":"F01", "F02":"B13", "F03":"F06", "F04":"F02",
       "F05":"F03", "F06":"F04", "F07":"F05", "F08 / S20":"F08 / README S20"}
types = {
    "background carried without new proof":"carried as background without fault found",
    "literature/source verification":"used and rechecked in this run",
    "read and compared against supplied context":"used and rechecked in this run",
}
rows, crosswalk = [], []
for filename in ["integral_check_events.tsv", "uniformization_CHECK_EVENTS.tsv",
                 "S20_proposed_CHECK_EVENTS.tsv", "legendre_check_events.tsv"]:
    with (ROOT / filename).open(newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            old = row["statement_id"]
            new = old
            if filename.startswith("integral") and re.fullmatch(r"D\d\d", old):
                new = PREFIX + old
            elif filename.startswith("uniformization") and old.startswith(PREFIX):
                new = PREFIX + uniform[old[len(PREFIX):]]
            elif filename.startswith("S20_") and old.startswith(PREFIX):
                new = PREFIX + s20[old[len(PREFIX):]]
            elif filename.startswith("legendre") and old.startswith("S20.Legendre"):
                new = PREFIX + "F09"
            row["statement_id"] = new
            row["type"] = types.get(row["type"], row["type"])
            row["outcome"] += f" [Source record: {filename}; original ID: {old}.]"
            if filename.startswith("uniformization"):
                row["outcome"] += " Note IDs inside the original outcome belong to that report's provisional numbering; see agent_note_id_crosswalk.tsv."
            rows.append(row)
            crosswalk.append([filename, old, new])

with (ROOT / "agent_events.tsv").open("w", newline="") as f:
    w = csv.DictWriter(f, FIELDS, delimiter="\t")
    w.writeheader()
    w.writerows(rows)
with (ROOT / "agent_note_id_crosswalk.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["source_report_events", "original_statement_id", "final_statement_id"])
    w.writerows(dict.fromkeys(tuple(r) for r in crosswalk))
print(f"Merged {len(rows)} dated agent events, with explicit ID crosswalk.")
