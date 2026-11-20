from pathlib import Path
import json,re
base=Path('work/readers/030/A')
r=json.loads((base/'report.json').read_text())
t=(base/'reading.tex').read_text()
c=Path('work/inputs/030/C.tex').read_text()
s=c
for x in r['changes']:
 assert x['c'] in c,('not literal C',x['id'])
 assert x['c'] in s,x['id']
 assert s.count(x['c'])==1,x['id']
 s=s.replace(x['c'],x['reading'],1)
assert s==t
body='\n'.join(line.split('%',1)[0] for line in t.splitlines())
stack=[]
for i,ch in enumerate(body):
 if ch in '{}':
  k=i-1; n=0
  while k>=0 and body[k]=='\\':n+=1;k-=1
  if n%2:continue
  if ch=='{':stack.append(i)
  else:
   assert stack,('unmatched close',i)
   stack.pop()
assert not stack,stack
assert len(re.findall(r'(?<!\\)\$',body))%2==0
assert re.findall(r'\\begin\{([^}]+)\}',body)==re.findall(r'\\end\{([^}]+)\}',body)
assert body.count('\\cotefile{109}')==1
assert body.count('\\scanpage{30}')==1
allowed={'cotefile','scanpage','quad','ldots','unsure','S','uuline','uline','deleted','tikz','fill','node','margin','raisebox','cong'}
macros=set(re.findall(r'\\([A-Za-z]+)',body))
assert macros<=allowed,sorted(macros-allowed)
allowedkind={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
for x in r['changes']:
 assert x['kind'] in allowedkind
 assert x['h'] is None and x['diff_h'] is False and x['marked_in_H'] is False
 assert Path(x['crop']).exists()
for x in r['changes']+r['c_doubts']:
 assert x['crop'] or (x['source'] and len(x['bbox'])==4)
 assert len(x['bbox'])==4
 assert Path(x['source']).exists()
 assert 0<=x['bbox'][0]<x['bbox'][2]<=1682
 assert 0<=x['bbox'][1]<x['bbox'][3]<=1261
for i in r['inventory']:
 assert i['sheet_kind']=='list'
 assert i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
assert len(set(i['element'] for i in r['inventory']))==len(r['inventory'])
frozen=json.loads((base/'frozen_unresolved.json').read_text())
log=[json.loads(line) for line in (base/'crops/crops.jsonl').read_text().splitlines()]
assert len(log)==len(frozen['unresolved'])==26
assert len({x['output'] for x in log})==26
assert all(x['width']==2400 for x in log)
v=json.loads((base/'view_log.json').read_text())
assert all(v[k]['count']==1 for k in ['whole','half_a','half_b'])
assert len(v['crops'])==26 and all(x['count']==1 and x['displayed_singly'] for x in v['crops'])
result={'json_valid':True,'each_c_field_is_literal_C':True,'literal_change_replay_matches_reading':True,'balanced_braces':True,'balanced_math_dollars':True,'balanced_environments':True,'macros_checked':sorted(macros),'no_compilation':True,'changes':len(r['changes']),'c_doubt_and_context_decisions':len(r['c_doubts']),'remaining_doubt_groups':len(r['remaining_doubts']),'inventory_rows':len(r['inventory']),'crop_log_unique_entries':len(log),'view_log_counts':'whole1, half_a1, half_b1, every crop1','h_comparison_rows':0,'math_checks':0}
(base/'static_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
