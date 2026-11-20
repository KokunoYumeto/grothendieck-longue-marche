from pathlib import Path
import csv, json, re, shutil
from datetime import datetime, timezone

ROOT=Path(__file__).resolve().parents[2]
OUT=ROOT/'out'
SRC=ROOT/'source'
W=SRC/'SP50_CW_134-1+134-2_witnesses'
PREFIX='SP50_CW_134-1+134-2'
for name in ['pages','briefs','readers','evidence','decisions','scripts']:
    (OUT/name).mkdir(parents=True,exist_ok=True)
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
if not (OUT/'progress.log').exists():
    (OUT/'progress.log').write_text(now+'\nSession: GPT-6 Astra Pro, three independent fresh page readers plus main adjudicator; effort setting not exposed to the agent.\n',encoding='utf-8')
    (OUT/'CHECK_EVENTS.tsv').write_text('statement_id\tdate\twho_model_effort_run\ttype\toutcome\n',encoding='utf-8')
    (OUT/'notation.md').write_text('# Running notation table\n\nNo glyph has yet been read in this pass. Entries are observations, never a substitute for inspecting each occurrence.\n\n| First scan / place | Glyph or convention | Reading | Ink evidence / qualifications |\n| --- | --- | --- | --- |\n',encoding='utf-8')
    (OUT/'state.json').write_text(json.dumps({'prefix':PREFIX,'started_utc':now,'last_checkpoint_utc':now,'next_checkpoint':1,'completed':[],'active_brief':'v01'},indent=2)+'\n')
shutil.copy2(W/'codex/H134-01/PREAMBLE.tex',OUT/'PREAMBLE.tex')
p=(W/'codex/H134-01/PROMPT.md').read_text()
rules=p[p.index('## Absolute rules'):p.index('## The attached draft')]
(OUT/'briefs/conventions.md').write_text(rules+'\n\n## Controlling second-pass overrides\nThe current second-pass instructions control: three fresh readers per page; whole page and TWO supplied halves once each, followed by one tight crop per unresolved place; read with both witnesses. Never follow the superseded first-pass method. Do not compile LaTeX; syntax validation only. Use cotefile at each cote’s first page and scanpage on every page.\n')
rows=list(csv.DictReader((W/'page_map.tsv').open(),delimiter='\t'))
for row in rows:
    stem=Path(row['codex_file']).stem
    d=ROOT/'work/packets'/stem
    d.mkdir(parents=True,exist_ok=True)
    shutil.copy2(W/row['codex_file'],d/'C.tex')
    h=(W/row['hua_file']).read_text()
    pat=r'\\page\{'+row['their_page']+r'\}'
    match=re.search(pat,h)
    if match:
        end=re.search(r'\\page\{\d+\}|\\end\{document\}',h[match.end():])
        text=h[match.start():match.end()+end.start()] if end else h[match.start():]
    else:
        text='% Witness H has no transcription for this page. Do not create H collation rows.\n'
    (d/'H.tex').write_text(text)
    doubts=(W/f"codex/{row['folder']}/{row['folder']}_doubts.md").read_text()
    lines=[]
    for line in doubts.splitlines():
        if line.startswith('|') and re.match(r'\s*'+row['our_scan']+r'(?!\d)',line.split('|')[1] if '|' in line else ''):
            lines.append(line)
    notes=(W/f"codex/{row['folder']}/{row['folder']}_notes.md").read_text()
    nlines=[l for l in notes.splitlines() if re.search(r'(?<!\d)'+row['our_scan']+r'(?!\d)',l)]
    (d/'prior_questions.md').write_text('# Witness C prior questions — prompts for inspection, not evidence\n\n'+'\n'.join(lines)+'\n\n'+'\n'.join(nlines)+'\n')
    row['stem']=stem
    row['packet']=str(d)
    row['images']=[str(SRC/(PREFIX+'_scans')/(stem+s+'.jpg')) for s in ['', '_a','_b']]
    (d/'metadata.json').write_text(json.dumps(row,indent=2)+'\n')
(OUT/'page_order.json').write_text(json.dumps(rows,indent=2)+'\n')
print(json.dumps({'started':now,'pages':len(rows),'first_packet':rows[0]['packet']},indent=2))
