from pathlib import Path
import json,re
R=Path('/workspace/scratch/94548b74fbe0/out/readers/015/B')
t=(R/'reading.tex').read_text()
p=json.loads((R/'report.json').read_text())
clean='\n'.join(re.split(r'(?<!\\)%',x,1)[0] for x in t.splitlines())
stack=[]
for i,c in enumerate(clean):
 if c in '{}':
  n=0;j=i-1
  while j>=0 and clean[j]=='\\':n+=1;j-=1
  if n%2:continue
  if c=='{':stack.append(i)
  else:
   assert stack,('extra close brace',i)
   stack.pop()
assert not stack,stack
envs=[]
for typ,name in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
 if typ=='begin':envs.append(name)
 else:
  assert envs and envs[-1]==name,(typ,name,envs)
  envs.pop()
assert not envs,envs
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert clean.count(r'\[')==clean.count(r'\]')
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
required={'id','location','C','H','reading','evidence','confidence','kind','diff_C','diff_H','C_doubt_status','readers_crop','bbox'}
for d in p['differences']:
 assert required <= set(d),(d['id'],required-set(d))
 assert d['kind'] in allowed,(d['id'],repr(d['kind']))
 if d['readers_crop']:assert (R/d['readers_crop']).is_file(),d['readers_crop']
for d in p['crops']:assert (R/d['path']).is_file(),d['path']
s=[d for d in p['differences'] if d.get('C_source_doubt_row')]
assert len(s)==24
assert set(d['C_source_doubt_row'] for d in s)==set(range(1,22))
resolved=[d['id'] for d in s if d['C_doubt_status']=='resolved']
assert resolved==['D01b','D04','D06','D07','D08','D12','D18','D21a','D21b'],resolved
for d in s:
 assert d['reading'] in t,(d['id'],'reading missing from TeX',d['reading'])
assert '\\unsure{vois. ouvert}' in t
assert '\\overset{\\unsure{\\rule{.8em}{.35pt}}}{\\Sigma}_i^+' in t
assert 'equivaut' not in t
assert '% archive sheet number: 14' in t
assert '\\mspage' not in t
assert p['check_events']==[]
assert all(x['transcribed']=='yes' for x in p['inventory'])
assert len(p['crops'])==20
p['notes']['validation']='One final source/report synchronization pass completed: brace balance, environment nesting, math delimiters, required report fields, permitted kind values, all 20 crop references, all 21 source rows/24 local decisions, exact TeX strings for every source-doubt reading, qualified graphical additions and archive comment were checked. No compiler or rendering was used.'
(R/'report.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
print('Required synchronization passed. Source rows: 21; local source decisions: 24; resolved: 9; retained: 15; crops: 20; check_events: 0.')
