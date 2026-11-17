"""Register a visually transcribed page. No OCR or image processing."""
from pathlib import Path
from datetime import datetime, timezone
import csv, re
ROOT = Path(__file__).resolve().parent.parent
PREFIX = "MPL_15_034-086"
def utc():
    return datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")
def balanced_arguments(text, macro):
    pattern = re.compile(r"\\"+macro+r"\{")
    for m in pattern.finditer(text):
        i=m.end(); start=i; depth=1
        while i<len(text) and depth:
            if text[i]=="{" and (i==0 or text[i-1]!="\\"): depth+=1
            if text[i]=="}" and (i==0 or text[i-1]!="\\"): depth-=1
            i+=1
        yield text.count("\n",0,m.start())+1, text[start:i-1]
def register(scan, sheet_kind, blocks, notes=""):
    page=ROOT/"pages"/f"{PREFIX}_15_scan{scan:03d}.tex"
    content=page.read_text()
    inv=ROOT/f"{PREFIX}_inventory.csv"
    fields=["cote","scan","sheet_kind","element","kind","position","first_words_or_objects","transcribed"]
    old=[]
    if inv.exists():
        with inv.open(newline="") as f: old=list(csv.DictReader(f))
    old=[r for r in old if int(r["scan"])!=scan]
    rows=[]
    for kind,position,words in blocks:
        rows.append([15,scan,sheet_kind,len(rows)+1,kind,position,words,"yes"])
    for macro,kind in [("deleted","deletion"),("inserted","insertion"),("margin","margin note")]:
        for line,txt in balanced_arguments(content,macro):
            rows.append([15,scan,sheet_kind,len(rows)+1,kind,f"TeX line {line}",txt.replace("\n"," ")[:200],"yes"])
    with inv.open("w",newline="") as f:
        w=csv.writer(f);w.writerow(fields)
        for r in old:w.writerow([r[k] for k in fields])
        w.writerows(rows)
    dfile=ROOT/"records"/f"doubts_scan{scan:03d}.md"
    doubts=[]
    for line,txt in balanced_arguments(content,"unsure"):
        parts=txt.split("|",1)
        read=parts[0].replace("|","\\|").replace("\n"," ")
        alt=parts[1].replace("|","\\|") if len(parts)>1 else "Ink does not fully decide this reading"
        doubts.append(f"| 15 | {scan} | TeX line {line} | {read} | {alt} | low |")
    for line,txt in balanced_arguments(content,"illegible"):
        doubts.append(f"| 15 | {scan} | TeX line {line} | \\illegible{{{txt}}} | Overwritten or unresolved ink after enlargement | low |")
    dfile.write_text("\n".join(doubts)+"\n")
    if notes:
        with (ROOT/"records/research_leads_before_context.md").open("a") as f:
            f.write(f"\n## Scan {scan}\n{notes}\n")
    with (ROOT/"progress.log").open("a") as f:
        f.write(f"15 scan {scan:03d} done {utc()}\n")
    print(f"Registered scan {scan:03d}: {len(rows)} inventory elements; {len(doubts)} local doubts.")
