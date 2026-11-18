"""Assemble research notes and record actual context searches.

This script never writes the frozen transcription or page files.
The source parts and check records are retained as work documentation.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
WORK = ROOT.parent
PARTS = ROOT / "documentation" / "research_checks"
NOW = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
WHO = "GPT-6 Astra Pro; effort not exposed; MPL_93_092-134/root"

sources = [
    WORK / "context" / "README.md",
    WORK / "context" / "notes" / "RESULTS_STATE.md",
    WORK / "context" / "same_cote_93" / "MPL_93_002-046_notes.md",
    WORK / "context" / "hua_project" / "README.md",
    WORK / "context" / "hua_project" / "93.modern.tex",
]
part_paths = [PARTS / "notes_intro.md"]
part_paths += [PARTS / f"notes_{letter}.md" for letter in "ABCDEF"]
part_paths += [PARTS / "notes_closing.md"]
present = [p for p in part_paths if p.exists()]
full = "\n\n".join(p.read_text().rstrip() for p in present) + "\n"
(ROOT / "MPL_93_092-134_notes.md").write_text(full)

notes = list(re.finditer(r"^### ([A-F]\d\d) — (.*)$", full, re.M))
events = []
queries = []
for i, match in enumerate(notes):
    note_id, title = match.groups()
    end = notes[i + 1].start() if i + 1 < len(notes) else len(full)
    block = full[match.end():end]
    qm = re.search(r"^\*\*Context query:\*\* (.+)$", block, re.M)
    cm = re.search(r"^\*\*Check:\*\* (.+?) \|\| (.+)$", block, re.M)
    if qm is None or cm is None:
        raise ValueError(f"{note_id}: missing context query or check event")
    pattern = qm.group(1)
    check_type, outcome = cm.groups()
    result = subprocess.run(
        ["rg", "-n", "-i", "--", pattern, *[str(p) for p in sources]],
        text=True, capture_output=True,
    )
    if result.returncode not in (0, 1):
        raise ValueError(f"{note_id}: invalid context regex: {result.stderr}")
    per_file = {}
    for line in result.stdout.splitlines():
        file_name, line_no, _content = line.split(":", 2)
        rel = str(Path(file_name).relative_to(WORK))
        per_file.setdefault(rel, []).append(int(line_no))
    if not per_file:
        queries.append([note_id, NOW, pattern, "(no matches)", "0", ""])
    for file_name, line_nos in sorted(per_file.items()):
        # Record locations rather than reproduce the supplied context.
        queries.append([note_id, NOW, pattern, file_name, str(len(line_nos)), ",".join(map(str, line_nos))])
    events.append([f"MPL_93_092-134 {note_id}", NOW.split()[0], WHO, check_type, outcome])

with (ROOT / "documentation" / "context_searches.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["note_id", "search_utc", "pattern", "context_file", "matching_line_count", "matching_lines"])
    w.writerows(queries)

for extra in [PARTS / name for name in [
    "background_events.tsv", "source_refutations.tsv", "agent_events.tsv",
    "final_review_events.tsv", "final_context_review_events.tsv",
]]:
    if extra.exists():
        with extra.open(newline="") as f:
            reader = csv.DictReader(f, delimiter="\t")
            for row in reader:
                events.append([row[k] for k in ["statement_id", "date", "who", "type", "outcome"]])

allowed_types = {
    "targeted proof check", "independent re-proof", "computation or formal certificate",
    "used and rechecked in this run", "carried as background without fault found",
    "refuted, with the refined statement's id",
}
for event in events:
    if event[3] not in allowed_types:
        raise ValueError(f"Unknown check-event type: {event}")

with (ROOT / "CHECK_EVENTS.tsv").open("w", newline="") as f:
    w = csv.writer(f, delimiter="\t")
    w.writerow(["statement_id", "date", "who", "type", "outcome"])
    w.writerows(events)

print(f"Assembled {len(notes)} notes from {len(present)} parts.")
print(f"Recorded {len(events)} check events and {len(queries)} per-file context-query results.")
print(f"UTC {NOW}")
