from pathlib import Path
import csv, re, json, shutil
from datetime import datetime, timezone

ROOT=Path('/workspace/scratch/bf95260d39fc')
SRC=ROOT/'source/SP43_CW_29+32_witnesses'
OUT=ROOT/'out'
for d in ['pages','readers','briefs','decisions','crops','scripts']:
    (OUT/d).mkdir(parents=True,exist_ok=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if not (OUT/'progress.log').exists():
    (OUT/'progress.log').write_text(now+'\n')
shutil.copyfile(SRC/'codex/C29-04/PREAMBLE.tex',OUT/'PREAMBLE.tex')
rows=list(csv.DictReader((SRC/'page_map.tsv').open(),delimiter='\t'))
(ROOT/'work').mkdir(exist_ok=True)
(ROOT/'work/page_map.json').write_text(json.dumps(rows,indent=2))
for row in rows:
    stem=Path(row['codex_file']).stem
    d=ROOT/'work'/stem
    d.mkdir(exist_ok=True)
    shutil.copyfile(SRC/row['codex_file'],d/'C.tex')
    h=(SRC/row['hua_file']).read_text()
    m=re.search(r'\\page\{'+row['their_page']+r'\}',h)
    if row['hua_has']=='text' and m:
        end=re.search(r'\\page\{\d+\}',h[m.end():])
        block=h[m.end():m.end()+end.start() if end else len(h)]
        (d/'H.tex').write_text(block)
    else:
        (d/'H.tex').write_text('% Witness H has no transcription of this scan.\n')
    folder=SRC/'codex'/row['folder']
    n=row['our_scan']
    doubt=(folder/(row['folder']+'_doubts.md')).read_text()
    # Page-specific rows only; notation spanning several pages is retained when explicitly including this scan.
    lines=[]
    section=''
    for line in doubt.splitlines():
        if line.startswith('#'):
            section=line
        if line.startswith('|') and re.search(r'(?<!\d)'+n+r'(?!\d)',line.split('|')[1]):
            lines.append(section+'\n'+line)
    notes=(folder/(row['folder']+'_notes.md')).read_text()
    selected=[line for line in notes.splitlines() if re.search(r'(?<!\d)'+n+r'(?!\d)',line)]
    (d/'C_prior_questions.md').write_text('\n'.join(lines)+'\n\nPrior notes mentioning this scan:\n'+'\n'.join(selected)+'\n')
    meta=dict(row,stem=stem,whole=str(ROOT/'source/SP43_CW_29+32_scans'/(stem+'.jpg')),half_a=str(ROOT/'source/SP43_CW_29+32_scans'/(stem+'_a.jpg')),half_b=str(ROOT/'source/SP43_CW_29+32_scans'/(stem+'_b.jpg')))
    (d/'meta.json').write_text(json.dumps(meta,indent=2))
(OUT/'notation.md').write_text('# Notation table\n\nStarted before scan 29/036. No glyph has yet been established from the ink. Entries are provisional page readings, never authority over a later scan.\n\n| Sign or usage | Reading | Evidence | Limits |\n|---|---|---|---|\n')
(OUT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho\ttype\toutcome\n')
(OUT/'checkpoint_index.tsv').write_text('number\tUTC\tfilename\tlibrary_file_id\n')
print('Initialized',len(rows),'page input bundles; started',now)
