from pathlib import Path
from collections import Counter
import json,re
out=Path('/workspace/scratch/6644f30583f9/SP52_work/readers/156-4_072/R1')
pkt=Path('/workspace/scratch/6644f30583f9/page_packets/156-4_072')
r=json.loads((out/'report.json').read_text()); s=(out/'reading.tex').read_text()
C=(pkt/'C.tex').read_text();H=(pkt/'H.tex').read_text()
issues=[]
# Structural fragment checks only; no LaTeX compiler.
body='\n'.join(line.split('%',1)[0] for line in s.splitlines())
level=0
for i,ch in enumerate(body):
 if ch in '{}':
  j=i-1
  while j>=0 and body[j]=='\\':j-=1
  if (i-1-j)%2:continue
  level+=1 if ch=='{' else -1
  if level<0:issues.append(('brace_underflow',i));break
if level:issues.append(('brace_balance',level))
stack=[]
for typ,env in re.findall(r'\\(begin|end)\{([^}]+)\}',body):
 if typ=='begin':stack.append(env)
 elif not stack or stack.pop()!=env:issues.append(('environment_mismatch',env))
if stack:issues.append(('open_environments',stack))
if len(re.findall(r'(?<!\\)\$',body))%2:issues.append(('math_dollar_parity',None))
if '\\cotefile' in s:issues.append(('unrequested_cote_marker',None))
assert '\\scanpage{72}\\mspage{71}' in s
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
for d in r['differences']:
 for k in ('change_c','change_h','math_consequential'):
  if type(d[k]) is not bool:issues.append((d['id'],'non_boolean',k))
 if d['kind'] not in kinds:issues.append((d['id'],'invalid_kind',d['kind']))
 if d['c'] and d['c'] not in C:issues.append((d['id'],'c_quote_not_literal',d['c']))
 if d['h'] and d['h'] not in H:issues.append((d['id'],'h_quote_not_literal',d['h']))
 if d['crop'] and not Path(d['crop']).exists():issues.append((d['id'],'missing_crop'))
 if not d.get('bbox_image'):issues.append((d['id'],'missing_bbox_source'))
 if not d['change_c'] and not d['change_h']:issues.append((d['id'],'neither_witness_changed'))
for q in r['c_doubts']:
 if q['c'] not in C:issues.append((q['id'],'c_doubt_not_literal',q['c']))
for q in r['remaining_doubts']:
 if q['reading'] not in s:issues.append(('remaining_doubt_not_in_reading',q['location'],q['reading']))
ids={d['id'] for d in r['differences']}
for p in r['h_placeholder_dispositions']:
 if not p['difference_ids']:issues.append(('placeholder_unlinked',p['occurrence']))
 if any(x not in ids for x in p['difference_ids']):issues.append(('bad_placeholder_ref',p['occurrence']))
assert H.count('\\ill{}')==len(r['h_placeholder_dispositions'])
assert len(r['context_dispositions'])==23
assert len(r['c_doubts'])==30
assert all(x['transcribed']=='yes' and x['hand']=='his hand' and x['sheet_kind']=='text' for x in r['inventory'])
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in r['inventory'])
print(json.dumps({'issues':issues,'difference_index':[(d['id'],d['location']) for d in r['differences']]},ensure_ascii=False,indent=2))
(out/'structural_check.json').write_text(json.dumps({'issues':issues,'checks':['balanced braces','matched environments','math-dollar parity','scan/folio markers','actual JSON booleans','source quotation comparison','all remaining-doubt snippets present','15 H placeholders linked','30 C doubts and 23 context rows','crop paths exist','inventory enum fields'],'latex_compilation':False},ensure_ascii=False,indent=2)+'\n')
