#!/usr/bin/env python3
"""Append final reproducibility tables and the first/last complete briefs."""
from pathlib import Path
import csv,json
R=Path(__file__).resolve().parents[1]
scans=[26,27,28,30,31,32,33]
target=R/'SP39_CW_75_workflow.md'
text=target.read_text().split('\n<!-- FINAL_WORKFLOW_APPENDIX -->')[0].rstrip()
meta=json.loads((R/'workflow_counts.json').read_text())
lines=['','<!-- FINAL_WORKFLOW_APPENDIX -->','', '## Crop counts for the complete run','',
       'Counts are distinct generated crop files. Root inspections of reader crops do not create extra files. Delivery retries of images that were not visible are documented above and do not alter these counts.','',
       '| Scan | Reader A | Reader B | Reader C | New root crops | Total created | Root existing-crop inspections |',
       '|---|---:|---:|---:|---:|---:|---:|']
for scan in scans:
 counts=[]
 for w in 'ABC':
  p=R/f'readers/scan{scan:03}/{w}/crops.tsv'
  with p.open() as f:counts.append(len(list(csv.DictReader(f,delimiter='\t'))))
 m=meta[str(scan)]
 p=R/f'decisions/scan{scan:03}_main_crops.tsv'
 with p.open() as f:new=len(list(csv.DictReader(f,delimiter='\t')))
 assert new==m['root_new']
 lines.append('| '+' | '.join(map(str,[f'{scan:03}',*counts,new,sum(counts)+new,m['root_existing']]))+' |')
briefs=sorted(R.glob('briefs/brief_v*_scan*.md'))
for title,p in [('First brief, in full',briefs[0]),('Last brief used, in full',briefs[-1])]:
 lines += ['',f'## {title}','','Source: '+str(p.relative_to(R))+'.','','````markdown',p.read_text().rstrip(),'````']
target.write_text(text+'\n'+'\n'.join(lines)+'\n')
print('Workflow appendix written with complete first/last briefs and exact crop counts.')
