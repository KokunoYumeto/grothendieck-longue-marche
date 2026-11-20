"""Document the already-adjudicated C-mark coverage on scans before v007.

This is an explicit crosswalk to existing outcomes, not a new reading pass.
No source image is opened and no transcription text is changed.
"""
from pathlib import Path
from datetime import datetime,timezone
import json,re
w=Path(__file__).resolve().parents[1]
# Ordered list: C001, C002, ... -> existing zero-based c_doubts row.
mapping={3:list(range(15)),4:[],5:[],7:[],9:list(range(4)),10:[0,1,3,4],11:[0,1,2,3,4],12:[0,1,2,3,4,5],13:[0,10,1,2,3,11,4,5,12,6,13,7,8,9],15:list(range(5)),16:list(range(4))}
for n,rows in mapping.items():
 p=w/f'decisions/scan{n:03d}.json';d=json.loads(p.read_text())
 marks=re.findall(r'^## (C\d{3})\b',(w.parent/f'packets/scan{n:03d}/C_marked_loci.md').read_text(),re.M)
 assert len(marks)==len(rows)
 for q in d['c_doubts']:q['c_mark_ids']=[]
 for mark,idx in zip(marks,rows):d['c_doubts'][idx]['c_mark_ids'].append(mark)
 d['c_mark_count']=len(marks);d['c_mark_coverage']=marks
 d['coverage_crosswalk_note']='Existing outcomes cross-referenced to the mechanical C-mark list after scan018. No text or reading decision changed; no image reopened.'
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
 cp=w/f'decisions/approved_scan{n:03d}_config.json'
 if cp.exists():
  c=json.loads(cp.read_text());c['c_doubts']=d['c_doubts'];cp.write_text(json.dumps(c,ensure_ascii=False,indent=2)+'\n')
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (w/'progress.log').open('a') as f:f.write(f'C-mark coverage crosswalk verified for scans 003–018 {now}; no transcription or image reinspection.\n')
print('Mapped all existing inline C doubts on the 11 pre-scan018 pages to their existing outcomes.')
