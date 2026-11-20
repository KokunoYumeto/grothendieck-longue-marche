#!/usr/bin/env python3
from pathlib import Path
import json,csv
OUT=Path(__file__).resolve().parent.parent
order=json.loads((OUT/'records/page_order.json').read_text())
versions=sorted((OUT/'briefs').glob('reader_brief_v*.md'))
runs=list(csv.DictReader((OUT/'records/reader_runs.tsv').open(),delimiter='\t'))
done=[r for r in order if (OUT/'records'/(r['page']+'.json')).exists()]
text=['# Reading workflow','',
  'Each page is assigned in the requested order to three newly spawned agents with no inherited conversation or earlier-page images. Each receives a page-specific directory containing only that page’s image paths, C and H extracts, prior C questions, supplied preamble, current brief and notation snapshot. Readers cannot consult each other. The main reader compares their complete returns, inspects the cited crops and makes a tight crop for remaining adjudication places without a reader crop. A page is written and its logs updated before the next page is assigned.','',
  'The original page and supplied halves are viewed once each by each reader. Crop metadata records source pixels, bounding box, scale and any rotation. The main reader retains returns and adjudication crops. No OCR or external research is used. Reader reports record any departures or remaining uncertainty.','',
  '## Reader runs and crop counts','',
  '| Page | Brief | R1 crops | R2 crops | R3 crops | Main-reader new crops | Total crops |','|---|---|---:|---:|---:|---:|---:|']
for r in runs:
  page=r['page'];counts=[sum(p.suffix.lower() in {'.png','.jpg','.jpeg'} for p in (OUT/'readers'/page/x).rglob('*')) for x in ['R1','R2','R3']]
  main=sum(p.suffix.lower() in {'.png','.jpg','.jpeg'} for p in (OUT/'adjudication'/page).rglob('*'))
  text+=['| '+page+' | '+r['brief_version']+' | '+' | '.join(map(str,counts+[main,sum(counts)+main]))+' |']
text+=['','## Brief changes and the observations behind them','']
p=OUT/'records/brief_changes.json'
for change in json.loads(p.read_text()) if p.exists() else []:
  text+=['### '+change['version']+' — first used on '+change['first_page'],'']
  text+=['- '+reason for reason in change['reasons']]
  text+=['']
text+=['## First reader brief','',versions[0].read_text().strip(),'','## Last reader brief used','',versions[-1].read_text().strip(),'']
text+=['## What worked; what needed correction','',
  'The independent readings exposed disagreements both with the witnesses and between readers. Retaining exact proposed page files makes those disagreements reviewable. Tight crops preserve the visible basis of the main decision. The initial brief needed explicit correspondence rules for equivalent macro wrappers and for archive page references; those rows were removed from the final counts, while the original reader reports were retained.','',
  'Heavy typewriter overprinting can establish several underlying letter strokes without establishing the temporal order of the impressions. The final reading retains that uncertainty, including uncertain live/cancelled state. A vote does not determine the reading: the main crop decision can retain uncertainty even when one reader proposed a confident text.','',
  'The record-assembly scripts do not infer or recognize source text. They assemble manually adjudicated readings and keep page order, inventory and difference counts aligned. Static delimiter checks do not verify manuscript readings or mathematical truth.','',
  'Checkpoint ZIPs include the complete current deliverables and reading documentation, excluding input scans/witnesses and earlier checkpoint archives. They are created only at the requested 45-minute interval.','']
delivery=OUT/'records/tool_delivery_notes.md'
if delivery.exists():text+=['## Recorded delivery and comparison details','',delivery.read_text().strip(),'']
(OUT/'SP54_CW_57+63_workflow.md').write_text('\n'.join(text))
print('Workflow updated for '+str(len(runs))+' assigned pages; '+str(len(done))+' decided pages.')
