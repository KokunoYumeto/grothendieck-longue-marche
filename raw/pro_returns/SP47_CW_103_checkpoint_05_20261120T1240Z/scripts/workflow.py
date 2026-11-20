from pathlib import Path
import json
from datetime import datetime,timezone
R=Path(__file__).resolve().parents[1]
ds=[json.loads(p.read_text()) for p in sorted((R/'decisions').glob('scan*.json'))]
history=json.loads((R/'briefs/history.json').read_text())
first=R/'briefs'/history[0]['file'];last=R/'briefs'/history[-1]['file']
lines=['# SP47_CW_103 — workflow record\n',
'## Execution\n\nThree newly spawned independent readers were assigned each scan in archive order, with no inherited conversation history and no images of other pages. Each received the one-page witness packet, relevant C alerts, the preamble, the current brief and a frozen notation-table snapshot. They viewed the whole page for layout and the two full-resolution halves for reading, then used tight crops only for open loci. They were told not to inspect other readers’ returns. The main reader compared the three complete returns and personally inspected adjudication crops for every witness difference and reader disagreement. The page file, inventory, changes, collation and progress entry were written before beginning the next scan.\n',
'All source files were supplied by the user. No external research, OCR, text-recognition library, or PDF text layer was used. Cropping, enlargement and contrast adjustment used Pillow; scripts did not infer text. The earlier witnesses’ source material is excluded from the output ZIP; readers’ returns and derived crops document this run.\n',
'## Brief revisions\n']
for h in history:lines.append(f"- {h['file']}, first used on scan {h['first_scan']:03}: {h['reason']}\n")
lines+=['\n## Crop counts\n\n','| Scan | Reader A | Reader B | Reader C | Main new crops | Main distinct crops inspected |\n| --- | --- | --- | --- | --- | --- |\n']
runs=[]
for d in ds:
 n=d['scan'];counts=[]
 for letter in 'ABC':
  path=R/'readers'/f'scan{n:03}'/letter/'report.json'
  rep=json.loads(path.read_text());counts.append(len(rep.get('crops',[])))
  runs.append({'scan':n,'reader':letter,'start_utc':rep.get('start_utc'),'end_utc':rep.get('end_utc'),'model':rep.get('model','not exposed'),'effort':rep.get('effort','not exposed'),'brief':d.get('brief','brief_v01.md')})
 paths=set(c for row in d['changes'] for c in row.get('crops',[]))
 paths.update(d.get('additional_main_crops',[]))
 new=len([p for p in paths if p.startswith('crops/')])
 lines.append(f'| {n:03} | {counts[0]} | {counts[1]} | {counts[2]} | {new} | {len(paths)} |\n')
lines.append('\nReader crop counts count generated, inspected evidence crops; one crop can support several tightly related marks. Main counts include reused reader crops, so they are not additional image generations. Source whole pages and halves are not counted as crops. Exact coordinates and processing are in readers’ crop manifests/reports and main crop manifests.\n')
lines.append('\n## What worked and what did not\n\n'+(R/'records/workflow_journal.md').read_text()+'\n')
lines.append('\n## First brief, verbatim\n\n'+first.read_text()+'\n')
lines.append('\n## Last brief, verbatim\n\n'+last.read_text()+'\n')
(R/'SP47_CW_103_workflow.md').write_text('\n'.join(lines))
(R/'records/reader_runs.json').write_text(json.dumps(runs,ensure_ascii=False,indent=2))
print(f'Workflow record rebuilt for {len(ds)} decided pages, {len(runs)} independent readings.')
