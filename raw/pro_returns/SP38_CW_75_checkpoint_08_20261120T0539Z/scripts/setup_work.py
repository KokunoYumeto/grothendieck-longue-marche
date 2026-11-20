from pathlib import Path
from datetime import datetime, timezone
import csv, re, json, shutil

BASE=Path('/workspace/scratch/be39e9f81d6d')
SRC=BASE/'source'
W=SRC/'SP38_CW_75_witnesses'
OUT=BASE/'out'
for d in ['pages','readings','decisions','briefs','scripts','crops','records']:
    (OUT/d).mkdir(parents=True, exist_ok=True)
(BASE/'packets').mkdir(exist_ok=True)
if not (OUT/'progress.log').exists():
    (OUT/'progress.log').write_text(datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'\n')
shutil.copy2(W/'codex/J75-01/PREAMBLE.tex',OUT/'PREAMBLE.tex')
prompt=(W/'codex/J75-01/PROMPT.md').read_text()
conventions=prompt[prompt.index('## Absolute rules'):prompt.index('## The attached draft')]
(OUT/'briefs/conventions.md').write_text(conventions)
(OUT/'briefs/notation_initial.md').write_text('# Notation table before scan 002\n\nNo readings established yet. Establish each glyph from this page; do not import mathematical conventions.\n')
rows=list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'))
for row in rows:
    n=int(row['our_scan']); folder=row['folder']; p=BASE/'packets'/f'scan{n:03d}'
    p.mkdir(exist_ok=True)
    shutil.copy2(W/row['codex_file'],p/'C.tex')
    h=(W/row['hua_file']).read_text()
    boundaries=[]
    for m in re.finditer(r'\\page\{(\d+)\}',h):
        start=m.start(); before=h[:start].rstrip()
        if before.splitlines()[-1].startswith('\\section*{'):
            start=h.rfind('\\section*{',0,start)
        boundaries.append((int(m.group(1)),start))
    hn=int(row['their_page'])
    if row['hua_has']=='text':
        k=next(i for i,x in enumerate(boundaries) if x[0]==hn)
        end=boundaries[k+1][1] if k+1<len(boundaries) else h.index('\\end{document}')
        hp=h[boundaries[k][1]:end].strip()+'\n'
    else:
        hp='% Witness H has no page transcription (page_map.tsv: nothing).\n% Editorial cover heading/note are not a transcribed page, and produce no collation rows.\n'
    (p/'H.tex').write_text(hp)
    cd=(W/f'codex/{folder}/{folder}_doubts.md').read_text()
    selected=[]; heading=''
    for line in cd.splitlines():
        if line.startswith('#'): heading=line
        if re.match(r'\|\s*'+str(n)+r'\s*\|',line): selected.append(heading+'\n'+line)
    cn=(W/f'codex/{folder}/{folder}_notes.md').read_text()
    selected+=['C notes: '+line for line in cn.splitlines() if re.search(r'\bScan '+str(n)+r'\b',line)]
    (p/'C_context.md').write_text('\n\n'.join(selected)+'\n')
    sr=[]
    for r in csv.DictReader((SRC/'SP38_CW_75_sweep3/readings/cotes71_75_CORRECTIONS.tsv').open(),delimiter='\t'):
        if re.match(r'75/'+str(n)+r'\b',r['where']):sr.append(r)
    (p/'S.json').write_text(json.dumps(sr,ensure_ascii=False,indent=2)+'\n')
    images=[str(SRC/'SP38_CW_75_scans'/f'{folder}_75_scan{n:03d}{suffix}.jpg') for suffix in ['', '_a','_b']]
    row['images']=images
    (p/'metadata.json').write_text(json.dumps(row,ensure_ascii=False,indent=2)+'\n')
    (OUT/'readings'/f'scan{n:03d}').mkdir(exist_ok=True)
for scan,name in [(4,'01-1.tex'),(5,'01-4.tex'),(6,'01-2.tex'),(8,'01-3.tex'),(16,'01-5.tex')]:
    destination=BASE/'packets'/f'scan{scan:03d}'/'H_drawings'
    destination.mkdir(exist_ok=True)
    shutil.copy2(W/'hua/transcripts/75/drawings'/name,destination/name)
shutil.copy2(BASE/'setup_work.py',OUT/'scripts/setup_work.py')
if not (OUT/'CHECK_EVENTS.tsv').exists():
    (OUT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n')
print(json.dumps({'pages':len(rows),'out':str(OUT),'started':(OUT/'progress.log').read_text().strip()},ensure_ascii=False))
