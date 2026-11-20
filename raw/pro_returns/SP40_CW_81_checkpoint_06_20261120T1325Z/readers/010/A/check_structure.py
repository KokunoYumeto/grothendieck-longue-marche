from pathlib import Path
import re,json
BASE=Path(__file__).resolve().parent
s=(BASE/'reading.tex').read_text()
r=json.loads((BASE/'report.json').read_text())
clean=re.sub(r'(?<!\\)%[^\n]*','',s)
depth=0
for m in re.finditer(r'(?<!\\)[{}]',clean):
 depth += 1 if m.group()=='{' else -1
 assert depth>=0,('closing brace',m.start())
assert depth==0,depth
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',clean):
 if m.group(1)=='begin': stack.append(m.group(2))
 else:
  assert stack and stack[-1]==m.group(2),(m.group(2),stack)
  stack.pop()
assert not stack,stack
macros=sorted(set(re.findall(r'\\([A-Za-z]+)',clean)))
allowed={'scanpage','figure','begin','end','draw','fill','node','scriptsize','diagram','bullet','vphantom','arrow','unsure','circ','path','bfseries','small','deleted','hbox','hspace','rlap','phantom','filldraw'}
assert not(set(macros)-allowed),set(macros)-allowed
assert s.count('\\scanpage{10}')==1
assert s.count('{OK};')==5
assert s.count('{ou};')==1
assert s.count('{?};')==1
assert s.count('% archive sheet number: 9')==1
assert s.count(r'\unsure{\bullet|\circ}')==1
assert s.count(r'\unsure{\circ|\bullet}')==3
assert not re.search(r'\\(?:input|include|includegraphics|newcommand|renewcommand)',s)
assert all(x['H'] is None and x['diff_H'] is False for x in r['differences'])
assert len([x for x in r['differences'] if x['C_doubt_status'] is not None])==5
assert {x['source_row'] for x in r['differences'] if x['C_doubt_status'] is not None}=={1,2,3,4,5}
assert all((BASE/x['path']).is_file() for x in r['crops'])
assert len({x['path'] for x in r['crops']})==15
assert len({tuple(x['bbox']) for x in r['crops']})==15
for d in r['differences']:
 if d['readers_crop']:assert (BASE/d['readers_crop']).is_file(),d
 for p in d.get('additional_crops',[]):assert (BASE/p).is_file(),p
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in r['inventory'])
assert len({x['element'] for x in r['inventory']})==len(r['inventory'])
assert any('archive sheet number' in x['first_words_or_objects'] for x in r['inventory'])
assert r['check_events']==[]
result={'braces':'balanced','environments':'balanced','macros':macros,'unsupported_macros':[],'OK_labels':5,'ou_labels':1,'question_marks':1,'archive_sheet_number':9,'source_doubt_rows':5,'existing_distinct_crop_paths':15,'inventory_entries':len(r['inventory']),'check_events':0,'compiler_or_renderer_used':False}
(BASE/'structure_check.json').write_text(json.dumps(result,indent=2)+'\n')
r['notes']['structural_validation']='Passed source-only checks: balanced braces and environments, supported macros, five OK labels, one ou, one ?, archive comment 9, all five source doubt rows, four explicit endpoint-qualification macros, complete relative crop references and inventory identifiers. No compiler or renderer was invoked.'
(BASE/'report.json').write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,indent=2))
