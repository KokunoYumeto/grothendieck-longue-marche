"""Read-only final pre-freeze identity and doubt-coverage checks."""
from pathlib import Path
from datetime import datetime,timezone
from collections import Counter
import re,json,hashlib,html
from tex_macro_extract import extract_file
ROOT=Path('/workspace/scratch/fce80d805cc4/MPL_136_142-188')
BASE=Path('/workspace/scratch/fce80d805cc4/verification')
RUNS=['20261116T000731.323836Z','20261116T001058.643711Z']
expected={};errors=[]
for run in RUNS:
 for item in json.loads((BASE/'compile_runs'/run/'compile_results.json').read_text()):
  if item['exit_code']!=0:errors.append('Failed compilation evidence for '+item['page'])
  expected[item['page']]=item['sha256']
numbers=[n for n in range(142,189) if n!=161]
filenames=[f'MPL_136_142-188_136_scan{n}.tex' for n in numbers]
if set(expected)!=set(filenames):errors.append('Compiled hash evidence does not cover the expected page set exactly')
live={};parts=[];live_ids=[]
for name in filenames:
 path=ROOT/'pages'/name;data=path.read_bytes();digest=hashlib.sha256(data).hexdigest();parts.append(data);live[name]=digest
 if digest!=expected.get(name):errors.append('Live source differs from successful compilation: '+name)
 records,problems=extract_file(path)
 if problems:errors.append('Malformed macro extraction in '+name)
 live_ids.extend(m['id'] for m in records if m['macro'] in {'unsure','illegible'})
combined=ROOT/'MPL_136_142-188_transcription.tex'
combined_bytes=combined.read_bytes()
combined_equal=combined_bytes==b''.join(parts)
if not combined_equal:errors.append('Combined transcription is not exact ordered byte concatenation')
doubts=ROOT/'MPL_136_142-188_doubts.md';text=doubts.read_text()
def cells(line):
 result=[];start=0
 for i,char in enumerate(line):
  if char!='|':continue
  j=i-1
  while j>=0 and line[j]=='\\':j-=1
  if (i-j-1)%2:continue
  result.append(line[start:i].strip());start=i+1
 result.append(line[start:].strip())
 if result and not result[0]:result=result[1:]
 if result and not result[-1]:result=result[:-1]
 return result

def plain(value):
 return re.sub('<[^>]+>','',html.unescape(value)).strip(' `*')
header=None;rows=[];all_confidence_rows=0
for lineno,line in enumerate(text.splitlines(),1):
 if not line.startswith('|'):
  header=None;continue
 parts_=cells(line)
 if any(plain(c).lower()=='confidence' for c in parts_):
  header=[plain(c).lower() for c in parts_];continue
 if header is None or all(re.fullmatch(r'[-: ]+',c or '-') for c in parts_):continue
 if len(parts_)!=len(header):
  errors.append(f'Doubts table malformed field count at Markdown line {lineno}');continue
 item=dict(zip(header,parts_))
 confidence=plain(item['confidence']).lower();all_confidence_rows+=1
 if confidence not in {'high','medium','low'}:errors.append(f'Unassigned/invalid confidence at Markdown line {lineno}')
 if 'occurrence' in item:
  identity=plain(item['occurrence'])
  rows.append({'id':identity,'confidence':confidence,'markdown_line':lineno})
rendered_ids=[r['id'] for r in rows]
missing=sorted(set(live_ids)-set(rendered_ids));extra=sorted(set(rendered_ids)-set(live_ids));duplicates=[i for i,n in Counter(rendered_ids).items() if n>1]
if missing:errors.append('Live doubt IDs absent from table: '+','.join(missing))
if extra:errors.append('Table IDs absent from current source: '+','.join(extra))
if duplicates:errors.append('Duplicate occurrence table IDs: '+','.join(duplicates))
summary={
 'checked_at_utc':datetime.now(timezone.utc).isoformat(),
 'successful_compile_runs':RUNS,'page_count':len(live),'page_hash_matches':sum(live.get(k)==v for k,v in expected.items()),
 'combined_exact_concatenation':combined_equal,'combined_sha256':hashlib.sha256(combined_bytes).hexdigest(),
 'combined_size_bytes':len(combined_bytes),'live_doubt_occurrences':len(live_ids),'table_occurrence_rows':len(rows),
 'missing_ids':missing,'extra_ids':extra,'duplicate_ids':duplicates,'confidence_counts':dict(Counter(r['confidence'] for r in rows)),
 'all_confidence_table_rows_checked':all_confidence_rows,'doubts_sha256':hashlib.sha256(doubts.read_bytes()).hexdigest(),
 'page_sha256':live,'errors':errors,
}
(BASE/'pre_freeze_verification.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps({k:v for k,v in summary.items() if k!='page_sha256'},indent=2))
raise SystemExit(1 if errors else 0)
