from pathlib import Path
from datetime import datetime, timezone
import json,re
root=Path('/workspace/scratch/17347c1714f0/out/readers/scan006/R3')
s=(root/'reading.tex').read_text()
r=json.loads((root/'report.json').read_text())
t=re.sub(r'(?<!\\)%[^\n]*','',s)
depth=0
for i,ch in enumerate(t):
 if ch in '{}':
  n=0;j=i-1
  while j>=0 and t[j]=='\\': n+=1;j-=1
  if n%2: continue
  depth+=1 if ch=='{' else -1
  assert depth>=0,('unmatched closing brace',i)
assert depth==0,('brace depth',depth)
stack=[];envcounts={}
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
 action,name=m.groups()
 if action=='begin': stack.append(name);envcounts[name]=envcounts.get(name,0)+1
 else: assert stack and stack.pop()==name,('environment mismatch',name)
assert not stack
inline=len(re.findall(r'(?<!\\)\$',t));assert inline%2==0
def delimiters(token):
 return len(re.findall(r'(?<!\\)'+re.escape(token),t))
for a,b in [(r'\[',r'\]'),(r'\(',r'\)')]:
 assert delimiters(a)==delimiters(b),(a,delimiters(a),b,delimiters(b))
for f in r['findings']: assert f['reading'] in s,f['id']
for d in r['doubts']: assert d['reading'] in s,d['place']
assert sum(f['c_doubt'] for f in r['findings'])==24
assert len(r['crops'])==17
assert all(Path(cr['file']).exists() and cr['observed'] for cr in r['crops'])
assert r['base_view_counts']=={'whole':1,'half_a':1,'half_b':1}
result={'checked_utc':datetime.now(timezone.utc).isoformat(),'method':'static source checks only; no TeX compilation','braces_balanced':True,'environments_balanced':True,'environment_counts':envcounts,'inline_dollar_count':inline,'display_open_count':delimiters(r'\['),'display_close_count':delimiters(r'\]'),'all_finding_readings_exactly_present_in_tex':True,'all_doubt_readings_exactly_present_in_tex':True,'c_doubt_decisions':24,'crops_present_with_observations':17,'result':'passed'}
(root/'static_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
r['finished_utc']=datetime.now(timezone.utc).isoformat()
r['static_validation']=result
(root/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False,indent=2))
