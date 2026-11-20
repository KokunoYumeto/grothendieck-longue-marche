from pathlib import Path
import re,json
p=Path(__file__).parent
s=(p/'reading.tex').read_text()
body=re.sub(r'(?m)%.*$','',s)
stack=[]
for i,ch in enumerate(body):
 if ch=='{' and (i==0 or body[i-1]!='\\'):stack.append(i)
 elif ch=='}' and (i==0 or body[i-1]!='\\'):
  assert stack,('unmatched close brace',i)
  stack.pop()
assert not stack,('unmatched opening braces',stack)
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 if m[1]=='begin':envs.append(m[2])
 else:
  assert envs and envs[-1]==m[2],('environment mismatch',m.group())
  envs.pop()
assert not envs
assert len(re.findall(r'(?<!\\)\\\[',body))==len(re.findall(r'(?<!\\)\\\]',body))==3
assert body.count(r'\left(')==body.count(r'\right)')==2
assert body.count('$')%2==0
allowed=set('scanpage unsure Rightarrow begin end mathbb left right draw qquad times overset simeq operatorname deleted mathcal mathscr hspace mathrel quad node rlap phantom subset underline fill figure diagram frown supset Gamma'.split())
macros=set(re.findall(r'\\([A-Za-z]+)',body))
assert macros<=allowed,('unexpected macros',sorted(macros-allowed))
assert r'\cotefile' not in body
assert '% archive sheet number: 10' in s
r=json.loads((p/'report.json').read_text())
assert set(r)==set('scan reader start_utc end_utc full_image_viewed halves_viewed complete_visual_read differences doubts inventory notes notation check_events crops brief_feedback'.split())
required=set('id location C H reading evidence confidence kind diff_C diff_H C_doubt_status readers_crop bbox'.split())
kinds={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
ids=[]
for d in r['differences']:
 assert required<=set(d),d['id']
 assert d['kind'] in kinds,d['kind']
 assert isinstance(d['diff_C'],bool) and isinstance(d['diff_H'],bool)
 assert d['C_doubt_status'] in (None,'resolved','retained')
 if d['readers_crop']:assert (p/d['readers_crop']).is_file(),d['readers_crop']
 ids.append(d['id'])
assert len(ids)==len(set(ids))
actual_rows={int(re.search(r'\.D(\d+)',d['id'])[1]) for d in r['differences'] if re.search(r'\.D(\d+)',d['id'])}
assert actual_rows==set(range(1,16)),actual_rows
for x in r['inventory']:
 assert set(x)==set('sheet_kind hand element kind position first_words_or_objects transcribed'.split())
 assert x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
 assert x['transcribed']=='yes'
manifest=json.loads((p/'crop_manifest.json').read_text())
assert manifest==r['crops']
assert len(manifest)==14
for c in manifest:
 assert (p/c['path']).is_file()
 x0,y0,x1,y1=c['bbox']
 assert 0<=x0<x1<=1678 and 0<=y0<y1<=1206
assert r['check_events']==[]
# Concrete reading/report correspondence checks, without evaluating mathematical claims.
for token in [r'\unsure{=|\Rightarrow}',r'\mathbb P',r'\unsure{Z|2}',r'\deleted{\unsure{\mathcal E|e}}Z',r'\unsure{\operatorname{Hom}}',r'\unsure{O|0}',r'P(\operatorname{Hom}(X,Z)',r'\deleted{\unsure{t|1}}Z',r'\unsure{H|U}',r'\deleted{H}\Gamma',r'\unsure{V|Y}',r'\unsure{V|W}',r'\unsure{\deleted{M}|M|\deleted{U}|U}',r'\unsure{\deleted{R}|R}']:
 assert token in body,token
assert r'\operatorname{Hom}(X,\underline{\operatorname{Hom}}(\mathscr E,Z)' in body.replace(r'\unsure{\operatorname{Hom}}',r'\operatorname{Hom}')
assert r'\draw (18,363) -- (17,562);' in body
assert r'\draw (25,499) -- (31,555);' in body
result=dict(braces='balanced',environments='paired',display_pairs=3,left_right_pairs=2,macro_names='supported',unique_difference_ids=len(ids),C_source_doubt_rows=15,crop_files=14,inventory_items=len(r['inventory']),diff_C=sum(d['diff_C'] for d in r['differences']),diff_H=sum(d['diff_H'] for d in r['differences']),compiler_invoked=False,check_events=0)
(p/'structural_checks.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
