from pathlib import Path
import csv, re, json, sys

ROOT=Path(__file__).resolve().parents[2]
SRC=ROOT/'source'
W=SRC/'SP36_CW_71_witnesses'
OUT=ROOT/'out'
scan=int(sys.argv[1])
row=next(r for r in csv.DictReader((W/'page_map.tsv').open(),delimiter='\t') if int(r['our_scan'])==scan)
packet=ROOT/'packets'/f'scan{scan:03d}'
packet.mkdir(parents=True,exist_ok=True)
folder=row['folder']; c=W/row['codex_file']
(packet/'C.tex').write_text(c.read_text())
h=(W/row['hua_file']).read_text()
marks=list(re.finditer(r'\\page\{(\d+)\}',h))
match=next((i for i,m in enumerate(marks) if int(m[1])==int(row['their_page'])),None)
if match is None:
    htext=f'% Witness H status: {row["hua_has"]}; no page marker or transcribed text for archive page {row["their_page"]}.\n'
else:
    start=marks[match].start(); end=marks[match+1].start() if match+1<len(marks) else h.find('\\end{document}',start)
    htext=h[start:end if end!=-1 else None]
(packet/'H.tex').write_text(htext)
drawings=[]
for p in sorted((W/'hua/transcripts/71/drawings').glob('*.tex')):
    t=p.read_text()
    if re.search(r'PDF page\s+'+str(scan)+r'\b',t.splitlines()[0]):
        (packet/('H_drawing_'+p.name)).write_text(t); drawings.append(p.name)
d=(W/f'codex/{folder}/{folder}_doubts.md').read_text()
parts=[]; heading=''
for line in d.splitlines():
    if line.startswith('#'): heading=line
    if re.match(r'\|\s*'+str(scan)+r'\s*\|',line): parts.append(heading+'\n'+line)
(packet/'C_doubts.md').write_text('\n\n'.join(parts)+'\n')
a=(W/f'codex/{folder}/{folder}_audit.md').read_text()
m=re.search(r'(?ms)^## Scan 0*'+str(scan)+r'\s*\n(.*?)(?=^## Scan |\Z)',a)
(packet/'C_audit.md').write_text(m.group(0) if m else 'No separate audit section located.\n')
n=(W/f'codex/{folder}/{folder}_notes.md').read_text()
lines=[line for line in n.splitlines() if re.match(r'\|\s*'+str(scan)+r'\s*\|',line) or re.search(r'\b[Ss]can\s+0*'+str(scan)+r'\b',line)]
(packet/'C_notes.md').write_text('\n'.join(lines)+'\n')
inv=list(csv.DictReader((W/f'codex/{folder}/{folder}_inventory.csv').open()))
inv=[r for r in inv if int(r['scan'])==scan]
(packet/'C_inventory.json').write_text(json.dumps(inv,ensure_ascii=False,indent=2))
s=list(csv.DictReader((SRC/'SP36_CW_71_sweep3/readings/cotes71_75_CORRECTIONS.tsv').open(),delimiter='\t'))
s=[r for r in s if re.search(r'\b71/'+str(scan)+r'\b',r['where'])]
(packet/'S.json').write_text(json.dumps(s,ensure_ascii=False,indent=2))
(packet/'PREAMBLE.tex').write_text((W/f'codex/{folder}/PREAMBLE.tex').read_text())
base=SRC/'SP36_CW_71_scans'/f'{folder}_71_scan{scan:03d}'
meta={**row,'images':[str(base)+suffix+'.jpg' for suffix in ['', '_a','_b']], 'H_drawings':drawings}
(packet/'meta.json').write_text(json.dumps(meta,indent=2))
notation=(OUT/'notation.md').read_text()
(packet/'notation.md').write_text(notation)
(OUT/'briefs'/f'notation_before_scan{scan:03d}.md').write_text(notation)
print(json.dumps(meta,indent=2))
