"""Keep visual comparison events distinct from actual mathematical deductions."""
from pathlib import Path
import json
from datetime import datetime,timezone
root=Path(__file__).resolve().parents[1]
ids={'scan170-S3-Hom-description','S175-cone-base','S176-diagram-sources-targets'}
changes=[]
for n in [170,175,176]:
 p=root/f'records/scan{n}/decision.json';d=json.loads(p.read_text())
 for e in d['check_events']:
  if e['statement_id'] in ids and e['type']!='carried as background without fault found':
   e['original_reader_type']=e['type']
   e['type']='carried as background without fault found'
   e['outcome']='Scope audit: this compares written symbols or configurations; it is visual consistency reading, not a proof or mathematical verification. Raw reader report is preserved. '+e['outcome']
   changes.append((n,e['statement_id'],e['who']))
 if n==170:
  d['notes']=d['notes'].replace('The source and target in Hom and the immediately following functor expression agree; reader A performed only that local consistency check (scan170-S3-Hom-description).','The source and target written in Hom and in the immediately following functor expression agree. Reader A compared those written endpoints (scan170-S3-Hom-description); this is recorded as visual consistency reading, not a mathematical proof check.')
 if n==175:
  d['notes']=d['notes'].replace('(**S175-cone-base**, reader B).','(**S175-cone-base**, reader B; a visual comparison of written bases, recorded as background rather than a mathematical check).')
 if n==176:
  d['notes']=d['notes'].replace('The three readers’ **S176-diagram-sources-targets** checks only compare','The three readers’ **S176-diagram-sources-targets** records are visual comparisons carried as background: they compare')
 p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
if changes:
 now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
 with (root/'progress.log').open('a') as f:f.write(f'event-scope audit {now}: {len(changes)} visual comparison events reclassified as carried background; no transcription changes.\n')
 report=root/'records/event_scope_audit.md'
 report.write_text('# Event scope audit\n\nVisual matching of explicitly written endpoints or diagram labels is not by itself a mathematical verification. Five earlier events were reclassified as carried background, with their original type retained in consolidated JSON and their raw reader reports unchanged. The actual type deductions using inverse/direct image, the conditional cone-model deductions and the adjunction calculation remain narrowly scoped checks. Scan 178 arrow tracing was classified the same way when first consolidated. No transcription text was changed.\n\n'+''.join(f'- Scan {n}, {i}, {w}\n' for n,i,w in changes))
print(json.dumps({'reclassified':len(changes)}))
