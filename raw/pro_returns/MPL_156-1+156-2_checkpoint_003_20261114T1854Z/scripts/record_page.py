from pathlib import Path
import sys, json, csv
from datetime import datetime, timezone
ROOT = Path(__file__).resolve().parents[1]
NAME = "MPL_156-1+156-2"
def now():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
entry = json.load(sys.stdin)
cote, scan = entry["cote"], entry["scan"]
stem = f"{NAME}_{cote}_scan{scan:03d}"
page = ROOT/"pages"/f"{stem}.tex"
if page.exists() and not entry.get("revision"):
    raise SystemExit("Page already exists; explicit revision required.")
page.write_text(entry.pop("tex").strip()+"\n", encoding="utf-8")
entry["saved_utc"] = now()
(ROOT/"records"/f"{stem}.json").write_text(json.dumps(entry,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
records = [json.loads(p.read_text()) for p in sorted((ROOT/"records").glob(f"{NAME}_*.json"))]
with (ROOT/f"{NAME}_inventory.csv").open("w",encoding="utf-8",newline="") as f:
    writer=csv.writer(f)
    writer.writerow(["cote","scan","sheet_kind","element","kind","position","first_words_or_objects","transcribed"])
    for rec in records:
        for n,e in enumerate(rec["elements"],1):
            writer.writerow([rec["cote"],rec["scan"],rec["sheet_kind"],n,*e,"yes"])
notation={}
abbreviations={}
for rec in records:
    notation.update(rec.get("notation",{}))
    abbreviations.update(rec.get("abbreviations",{}))
lines=["# Notation table","","| Manuscript sign or convention | LaTeX transcription |","|---|---|"]
def cell(s):
    return str(s).replace("|","&#124;").replace("\n"," ")
for k,v in notation.items():
    lines.append(f"| {cell(k)} | {cell(v)} |")
lines += ["","# Reading doubts","","Line positions are approximate manuscript lines, not lines of the LaTeX source.","","| Cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |","|---|---:|---|---|---|---|"]
for rec in records:
    for d in rec.get("doubts",[]):
        lines.append("| "+" | ".join(cell(s) for s in [rec["cote"],rec["scan"],*d])+" |")
lines += ["","# Abbreviations","","Expansions here are editorial proposals only; abbreviations remain unexpanded in the transcription.","","| Abbreviation | Proposed expansion |","|---|---|"]
for k,v in abbreviations.items():
    lines.append(f"| {cell(k)} | {cell(v)} |")
lines += ["","# Legibility and limits","","This is a visual reading of the supplied whole-page images and overlapping full-resolution halves, with no OCR. The final assessment will be completed after the second visual audit."]
(ROOT/f"{NAME}_doubts.md").write_text("\n".join(lines)+"\n",encoding="utf-8")
with (ROOT/"progress.log").open("a",encoding="utf-8") as f:
    f.write(f"{cote} scan {scan:03d} {'revised' if entry.get('revision') else 'done'} {now()}\n")
if entry.get("observations"):
    with (ROOT/"records"/"observations.md").open("a",encoding="utf-8") as f:
        f.write(f"\n## {cote} scan {scan:03d}\n\n{entry['observations']}\n")
print(f"Saved {cote} scan {scan:03d}; {len(records)} pages; {len(entry['elements'])} inventory elements.")

