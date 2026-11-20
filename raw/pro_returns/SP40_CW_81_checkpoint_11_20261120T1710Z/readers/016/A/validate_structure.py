from pathlib import Path
import json,re
root=Path('/workspace/scratch/94548b74fbe0/out/readers/016/A')
tex=(root/'reading.tex').read_text()
report=json.loads((root/'report.json').read_text())
manifest=json.loads((root/'crop_manifest.json').read_text())
body='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in tex.splitlines())
stack=[]
for i,c in enumerate(body):
 if c in '{}':
  preceding=0;j=i-1
  while j>=0 and body[j]=='\\': preceding+=1;j-=1
  if preceding%2: continue
  if c=='{': stack.append(i)
  else:
   assert stack, f'Unmatched closing brace at {i}'
   stack.pop()
assert not stack, f'Unclosed braces: {stack}'
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 op,name=m.groups()
 if op=='begin':envs.append(name)
 else:
  assert envs and envs.pop()==name,f'Environment mismatch: {name}'
assert not envs,envs
assert body.count('\\[')==body.count('\\]')
assert len(re.findall(r'(?<!\\)\$',body))%2==0
assert r'\scanpage{16}' in body
assert r'\cotefile' not in body and r'\mspage' not in body
assert '% archive sheet number: 15' in tex
assert not re.search(r'\\(?:newcommand|renewcommand|def|input|include|includegraphics)\b',body)
required=[r'\deleted{\unsure{sera|sont}} est',r'\unsure{:|à}',r'\inserted{en conclurait}',r'\deleted{E}\Sigma_{12}',r'\overset{\text{def}}{=}',r'\unsure{\big]}',"ce qui n'est pas."]
for literal in required:assert literal in tex,literal
join=r'\unsure{\deleted{\amalg}\cup|\amalg}'
assert tex.count(join)==2
assert len(report['C_doubt_source_rows'])==13
parts=[p for row in report['C_doubt_source_rows'] for p in row['local_parts']]
assert len(parts)==19 and len({p['id'] for p in parts})==19
ids={r['id'] for r in report['differences']}
assert all(p['id'] in ids for p in parts)
for row in report['differences']:
 assert row['C_doubt_status'] in ('resolved','retained',None)
 if row['readers_crop']:assert (root/row['readers_crop']).is_file(),row['readers_crop']
for crop in report['crops']:
 assert (root/crop['path']).is_file()
 assert crop in manifest['crops']
for comp in report['graphical_components']:
 assert comp['reading_tex_anchor'] in tex,comp['id']
valid_kinds={'text','display','diagram','drawing','margin note','insertion','deletion'}
assert all(x['kind'] in valid_kinds and x['transcribed']=='yes' for x in report['inventory'])
assert report['check_events']==[]
assert all(v['delivered_views']==1 for v in report['viewing_log']['crop_delivery'])
assert report['viewing_log']['whole']['delivered_views']==1
assert all(v['delivered_views']==1 for v in report['viewing_log']['halves'])
assert report['viewing_log']['recrops']==0
macro_names=sorted(set(re.findall(r'\\([A-Za-z]+)',body)))
allowed={'Sigma','amalg','begin','big','cap','coordinate','cup','deleted','draw','end','figure','fill','inserted','ne','node','overline','overset','path','phantom','quad','rlap','scanpage','setminus','subset','subsetneq','text','underbrace','unsure','varnothing'}
assert set(macro_names)<=allowed,sorted(set(macro_names)-allowed)
result={'validation':'source structure only; no TeX compiler or renderer invoked','balanced_braces':True,'balanced_environments':True,'balanced_display_delimiters':True,'even_dollar_delimiters':True,'macro_names':macro_names,'C_source_rows':13,'C_local_parts':19,'difference_rows':len(report['differences']),'diff_C_rows':sum(x['diff_C'] for x in report['differences']),'diff_H_rows':sum(x['diff_H'] for x in report['differences']),'crops_exist':len(report['crops']),'component_anchors_exist':len(report['graphical_components']),'report_transcription_literals_checked':required+[join],'limitations':'No compilation, rendering, glyph-contour tracing or algebraic proof check.','prior_checker_issue':'The first run stopped because this script’s standard-macro allowlist omitted quad. Quad was added; no transcription alteration was required for that issue.'}
(root/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
