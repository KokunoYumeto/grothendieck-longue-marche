from pathlib import Path
import csv, re, json, shutil, subprocess, sys
from datetime import datetime, timezone

def table_applies(line,n):
    if not line.lstrip().startswith('|'):return False
    cells=[x.strip() for x in line.strip().strip('|').split('|')]
    for i,c in enumerate(cells[:2]):
        m=re.match(r'^0*(\d+)\s*[–−-]\s*0*(\d+)(?:\b|$)',c)
        if m and int(m.group(1))<=n<=int(m.group(2)):return True
        if i==1 and len(set(re.findall(r'\b0\d\d\b',c)))>1:continue
        if re.match(r'^0*'+str(n)+r'(?:\b|[·,])',c):return True
    return False

ROOT = Path(__file__).resolve().parents[2]
WORK = ROOT / 'work'
SOURCE = ROOT / 'source'
WIT = SOURCE / 'SP49_CW_109_witnesses'
for d in ['pages','records','readers','briefs','inputs','crops','scripts']:
    (WORK/d).mkdir(parents=True,exist_ok=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if not (WORK/'progress.log').exists():
    (WORK/'progress.log').write_text(now+'\nSP49_CW_109 second pass started. Sources unpacked once; no OCR or outside research.\n',encoding='utf-8')
    (WORK/'state.json').write_text(json.dumps({'started_utc':now,'last_checkpoint_utc':now,'checkpoint_number':0,'done':[],'brief_version':1},indent=2))
shutil.copyfile(WIT/'codex/H109-01/PREAMBLE.tex',WORK/'PREAMBLE.tex')
prompt=(WIT/'codex/H109-01/PROMPT.md').read_text()
conventions=prompt.split('## Absolute rules',1)[1].split('## Reading handwriting',1)[0]
(WORK/'briefs/conventions.md').write_text('# Transcription conventions\n\n'+conventions,encoding='utf-8')
if not (WORK/'notation.md').exists():
    (WORK/'notation.md').write_text('# Shared notation table\n\nEntries are added only from ink read in this run; every entry remains subject to the current page’s ink.\n\n| Sign or practice | Scans and locations | Reading | Ink evidence and alternatives |\n| --- | --- | --- | --- |\n',encoding='utf-8')
rows=list(csv.DictReader((WIT/'page_map.tsv').open(),delimiter='\t'))
(WORK/'page_map.json').write_text(json.dumps(rows,indent=2))
for row in rows:
    n=int(row['our_scan']); folder=row['folder']; p=WORK/'inputs'/f'{n:03}'
    p.mkdir(exist_ok=True)
    # Input copies are local convenience only; checkpoints exclude witness inputs.
    shutil.copyfile(WIT/row['codex_file'],p/'C.tex')
    h=(WIT/row['hua_file']).read_text()
    mark='\\page{'+row['their_page']+'}'
    hpart=h.split(mark,1)[1].split('\\page{',1)[0]
    hpart=re.split(r'\\section\{',hpart)[0]
    (p/'H.tex').write_text('% H status: '+row['hua_has']+'; their page '+row['their_page']+'\n'+hpart)
    context=[]
    doubts=(WIT/f'codex/{folder}/{folder}_doubts.md').read_text()
    for line in doubts.splitlines():
        if table_applies(line,n): context.append(line)
    notes=(WIT/f'codex/{folder}/{folder}_notes.md').read_text()
    for para in notes.split('\n\n'):
        if re.search(r'(?i)scan\s+0*'+str(n)+r'\b',para): context.append(para)
    for line in notes.splitlines():
        if table_applies(line,n) and line not in context:context.append(line)
    (p/'C_context.md').write_text('# Earlier witness C doubts, notation and notes for this page\n\n'+'\n\n'.join(context))
    metadata=dict(row)
    metadata['whole']=str(SOURCE/f'SP49_CW_109_scans/{folder}_109_scan{n:03}.jpg')
    metadata['half_a']=metadata['whole'].replace('.jpg','_a.jpg')
    metadata['half_b']=metadata['whole'].replace('.jpg','_b.jpg')
    (p/'metadata.json').write_text(json.dumps(metadata,indent=2))
    # Restore the actual notation supplied to an already prepared reader page.
    snapshot=WORK/f'briefs/notation_before_{n:03}.md'
    if snapshot.exists():shutil.copyfile(snapshot,p/'notation.md')
if not (WORK/'CHECK_EVENTS.tsv').exists():
    with (WORK/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        csv.writer(f,delimiter='\t').writerow(['statement_id','date','who_model_effort_run','type','outcome'])
# The first implementation above selected numeric row IDs as if they were scans.
# Always finish restoration with the corrected header-aware Scan-column extractor.
subprocess.run([sys.executable,str(WORK/'scripts/refresh_context.py'),'9'],check=True)
print('Initialized',len(rows),'page inputs with header-aware context; start',now)
