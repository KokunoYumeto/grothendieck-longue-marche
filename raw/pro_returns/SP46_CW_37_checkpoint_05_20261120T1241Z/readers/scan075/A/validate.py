from pathlib import Path
import json,re
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/A')
r=json.loads((root/'report.json').read_text())
s=(root/'reading.tex').read_text()
required='scan reader image_views reading_path crops decisions inventory notes math_reading_decisions check_events notation abbreviations slips completion'.split()
assert all(k in r for k in required)
assert r['scan']==75 and r['reader']=='A'
assert len(r['image_views'])==3
assert all(d['h_reading'] is None and d['diff_h'] is False for d in r['decisions'])
assert sum(d['c_doubt'] for d in r['decisions'])==4
for d in r['decisions']:
 assert d['reading'] in s, d['id']
 x0,y0,x1,y1=d['bbox'];assert 0<=x0<x1<=1680 and 0<=y0<y1<=2001
for crop in r['crops']:
 assert (root/crop['file']).is_file()
# Literal delimiter and environment checks only: no TeX engine.
clean='\n'.join(line.split('%',1)[0] for line in s.splitlines())
depth=0
for i,ch in enumerate(clean):
 if ch=='{' and (i==0 or clean[i-1]!='\\'):depth+=1
 if ch=='}' and (i==0 or clean[i-1]!='\\'):
  depth-=1;assert depth>=0
assert depth==0
stack=[]
for action,name in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
 if action=='begin':stack.append(name)
 else:assert stack.pop()==name
assert not stack
assert clean.count(r'\[')==clean.count(r'\]')
assert clean.count(r'\(')==clean.count(r'\)')
assert clean.count(r'\begingroup')==clean.count(r'\endgroup')
assert s.count(r'\arrow[r')==6 and s.count(r'\arrow[d')==3
assert s.count(r'\deleted{')==2
assert r['check_events']==[]
print('JSON schema keys, H null policy, 4 C-doubt rows, all recorded snippets, crop existence and bounds: PASS')
print('TeX brace/environment/math-delimiter balance, 6 right arrows, 3 down arrows, 2 deletions: PASS')
print('No TeX compilation performed.')
