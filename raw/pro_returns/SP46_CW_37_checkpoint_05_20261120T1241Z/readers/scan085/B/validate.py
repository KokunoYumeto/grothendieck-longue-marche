from pathlib import Path
import json,re
root=Path('/workspace/scratch/006c0e32b2af')
out=root/'out/readers/scan085/B'
r=json.loads((out/'report.json').read_text())
m=json.loads((out/'crop_manifest.json').read_text())
t=(out/'reading.tex').read_text()
c=(root/'packets/scan085/C.tex').read_text()
required={'scan','reader','image_views','reading_path','crops','decisions','inventory','notes','math_reading_decisions','check_events','notation','abbreviations','slips','completion'}
assert set(r)==required
assert r['scan']==85 and r['reader']=='B'
assert len(r['image_views'])==3 and m['source_actual_visual_views']==[1,1,1]
assert r['check_events']==[]
allowed_kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
allowed_inventory={'text','display','diagram','drawing','margin note','insertion','deletion'}
for d in r['decisions']:
 assert d['h_reading'] is None and d['diff_h'] is False
 assert d['kind'] in allowed_kinds
 assert d['confidence'] in {'high','medium','low'}
 assert d['c_reading'] in c,(d['id'],'C snippet not exact')
 assert d['reading'] in t,(d['id'],'Final snippet not exact')
 assert len(d['bbox'])==4
 x1,y1,x2,y2=d['bbox']
 assert 0<=x1<x2<=1699 and 0<=y1<y2<=2154
 if d['crop']: assert Path(d['crop']).exists()
for x in r['inventory']:
 assert x['kind'] in allowed_inventory
 assert x['transcribed']=='yes'
for x in m['crops']:
 assert x['actual_visual_views']==x['requested_visual_deliveries']==1
 assert Path(x['file']).exists()
assert len(set(x['file'] for x in m['crops']))==len(m['crops'])==5
assert len(re.findall(r'\\unsure\{',c))==2
assert sum(d['c_doubt'] for d in r['decisions'])==2
assert len(re.findall(r'\\unsure\{',t))==4
assert sum(d['unresolved'] for d in r['decisions'])==4
clean='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in t.splitlines())
level=0
for i,ch in enumerate(clean):
 if ch not in '{}': continue
 back=0;j=i-1
 while j>=0 and clean[j]=='\\': back+=1;j-=1
 if back%2: continue
 level+=1 if ch=='{' else -1
 assert level>=0,('negative brace level',i)
assert level==0
stack=[]
for a,name in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
 if a=='begin': stack.append(name)
 else:
  assert stack and stack[-1]==name,(a,name,stack)
  stack.pop()
assert not stack
assert clean.count(r'\begingroup')==clean.count(r'\endgroup')==1
assert clean.count(r'\scanpage{85}')==1
assert r'\cotefile' not in clean
assert not re.search(r'\\(?:newcommand|renewcommand|def)\b',clean)
result={'schema_valid':True,'required_keys_present':True,'all_decision_snippets_exact':True,'all_H_readings_null':True,'all_H_differences_false':True,'bbox_bounds_valid':True,'brace_balance':0,'environment_balance':True,'group_balance':True,'explicit_C_doubts_covered':2,'final_uncertainties_covered':4,'source_views':[1,1,1],'unique_crops':5,'actual_crop_views':[x['actual_visual_views'] for x in m['crops']],'tex_compiled':False,'check_events':[]}
(out/'structure_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
