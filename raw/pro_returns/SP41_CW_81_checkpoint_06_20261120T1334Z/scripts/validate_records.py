"""Mechanical completeness checks for adjudicated records; no text recognition or reading inference."""
from pathlib import Path
import json,csv,re
w=Path(__file__).resolve().parents[1]
expected=[27,28,29,30,*range(32,56)]
allidx=list(csv.DictReader((w/'validation/C_doubt_index.tsv').open(),delimiter='\t'))
valid_kind={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
valid_inv={'text','display','diagram','drawing','margin note','insertion','deletion'}
valid_sheet={'text','reused_typed','typescript','letter','list','cancelled_draft','cover'}
valid_events={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
errors=[];rows=[];scans=[]
for p in sorted((w/'decisions').glob('scan*.json')):
 d=json.loads(p.read_text());n=d['scan'];scans.append(n);prefix=f'scan {n:03d}'
 ids={x['source_doubt_id'] for x in allidx if int(x['scan'])==n};got={x for f in d['findings'] for x in f.get('c_doubt_ids',[])}
 if ids!=got:errors.append(f'{prefix}: C doubt ID mismatch missing={ids-got}; extra={got-ids}')
 statuses={x:{f['c_doubt_status'] for f in d['findings'] if x in f.get('c_doubt_ids',[])} for x in ids}
 if any(len(v)!=1 for v in statuses.values()):errors.append(f'{prefix}: conflicting C doubt status')
 rejected={x['reader_id'] for x in d.get('rejected_candidates',[])}
 for reader in ('R1','R2','R3'):
  raw_path=w/f'readers/scan{n:03d}/{reader}/return.json'
  if not raw_path.exists():errors.append(f'{prefix}: missing detailed return {reader}');continue
  raw=json.loads(raw_path.read_text())['findings'];references=[]
  for f in d['findings']:
   ref=f.get('reader_source_ids',{}).get(reader,[])
   references.extend(ref if isinstance(ref,list) else [ref])
  missing=[f['id'] for f in raw if f['id'] not in rejected and not any(f['id'] in ref for ref in references)]
  if missing:errors.append(f'{prefix}: unmapped raw findings for {reader}: {missing}')
 for f in d['findings']:
  if set(f.get('readers',{}))!={'R1','R2','R3'}:errors.append(f"{f['id']}: three-reader comparison incomplete")
  if f['confidence'] not in {'high','medium','low'}:errors.append(f"{f['id']}: invalid confidence")
  if f['kind'] not in valid_kind:errors.append(f"{f['id']}: invalid collation kind")
  if d['hua_has']!='text' and f['against_H']:errors.append(f"{f['id']}: H difference on no-text page")
  cp=f.get('crop','')
  if (f['against_C'] or f['against_H']) and not cp:errors.append(f"{f['id']}: changed locus lacks local crop reference")
  if cp.endswith('.png') and not (w/cp).exists():errors.append(f"{f['id']}: missing crop {cp}")
  if f.get('c_doubt_ids') and f['c_doubt_status'] not in {'resolved','retained'}:errors.append(f"{f['id']}: undecided C doubt")
 for e in d['inventory']:
  if e['kind'] not in valid_inv or e['sheet_kind'] not in valid_sheet or e['transcribed']!='yes':errors.append(f'{prefix}: invalid inventory value')
 for ev in d['check_events']:
  if ev['type'] not in valid_events and not ev['type'].startswith('refuted, with'):errors.append(f'{prefix}: invalid check event type')
 t=(w/'pages'/d['filename']).read_text()
 if t.count(r'\scanpage{'+str(n)+'}')!=1:errors.append(f'{prefix}: wrong scanpage header')
 if r'\cotefile' in t:errors.append(f'{prefix}: repeated cote header in page')
 rows.append({'scan':n,'C_doubts':len(ids),'covered':len(got),'findings':len(d['findings']),'inventory':len(d['inventory']),'unresolved':len(d['unresolved'])})
if scans!=expected[:len(scans)]:errors.append('Decided pages do not form the ordered scope prefix')
register=list(csv.DictReader((w/'validation/reader_run_register.tsv').open(),delimiter='\t'))
tasks=[r['task_name'] for r in register]
if len(tasks)!=len(set(tasks)):errors.append('Reader task names are not fresh/unique')
for n in scans:
 rr=[r for r in register if int(r['scan'])==n]
 if len(rr)!=3 or {r['reader'] for r in rr}!={'R1','R2','R3'}:errors.append(f'scan {n:03d}: reader registration incomplete')
 if any(r['fork_turns']!='none' for r in rr):errors.append(f'scan {n:03d}: a reader inherited other-page history')
combined=(w/'SP41_CW_81_transcription.tex').read_text()
if combined.count(r'\cotefile{81}')!=1:errors.append('Combined cote header count is not one')
if [int(n) for n in re.findall(r'\\scanpage\{(\d+)\}',combined)]!=scans:errors.append('Combined page sequence disagrees with decisions')
result={'scope':expected,'decided_scans':scans,'all_valid':not errors,'errors':errors,'page_coverage':rows}
(w/'validation/record_validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2));print(json.dumps(result,ensure_ascii=False))
raise SystemExit(bool(errors))
