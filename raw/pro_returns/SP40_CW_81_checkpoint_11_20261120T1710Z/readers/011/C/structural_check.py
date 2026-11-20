from pathlib import Path
import re,json
p=Path('/workspace/scratch/94548b74fbe0/out/readers/011/C')
s=(p/'reading.tex').read_text()
r=json.loads((p/'report.json').read_text())
# Strip only unescaped TeX comments for structural checks.
t='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in s.splitlines())
stack=[]
for k,c in enumerate(t):
 if c=='{' and (k==0 or t[k-1]!='\\'):stack.append(k)
 elif c=='}' and (k==0 or t[k-1]!='\\'):
  assert stack, f'Extra close brace at {k}'
  stack.pop()
assert not stack,stack
st=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',t):
 if m[1]=='begin':st.append(m[2])
 else:
  assert st and st[-1]==m[2],(st,m.group())
  st.pop()
assert not st,st
assert t.count(r'\[')==t.count(r'\]')
assert t.count('$')%2==0
required={'scan','reader','start_utc','end_utc','full_image_viewed','halves_viewed','complete_visual_read','differences','doubts','inventory','notes','notation','check_events','crops','brief_feedback'}
assert set(r)==required,(set(r)-required,required-set(r))
permitted={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
fields={'id','location','C','H','reading','evidence','confidence','kind','diff_C','diff_H','C_doubt_status','readers_crop','bbox'}
assert len({d['id'] for d in r['differences']})==len(r['differences'])
for d in r['differences']:
 assert fields<=set(d),d['id']
 assert d['kind'] in permitted,d['kind']
 assert d['confidence'] in {'high','medium','low'}
 assert d['C_doubt_status'] in {'resolved','retained',None}
 if d['C_doubt_status']=='resolved':assert d['diff_C'],d['id']
 if d['readers_crop']:assert (p/d['readers_crop']).exists(),d['readers_crop']
for i in r['inventory']:
 assert set(i)=={'sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'}
 assert i['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'}
 assert i['transcribed']=='yes'
for c in r['crops']:
 assert (p/c['path']).exists(),c['path']
assert len(r['crops'])==13
assert {int(re.match(r'CD(\d+)',d['id'])[1]) for d in r['differences'] if d['id'].startswith('CD')}==set(range(1,16))
assert r['check_events']==[]
assert r'\cotefile' not in t
assert r'\scanpage{11}' in t
assert r'\times_{\unsure{Y|V}}U' in t
assert r'\operatorname{Hom}(X,\underline{\operatorname{Hom}}(\mathscr E,Z)' in t
assert r'P(\operatorname{Hom}(X,Z)' in t
assert '% archive sheet number: 10' in s
known={'scanpage','unsure','Rightarrow','begin','end','mathbb','qquad','times','overset','simeq','operatorname','underset','cdot','deleted','mathcal','mathscr','mathrel','quad','node','rlap','phantom','draw','underline','subset','figure','fill','diagram','arrow','big','Gamma','supset'}
used=set(re.findall(r'\\([A-Za-z]+)',t))
assert used<=known,sorted(used-known)
print(json.dumps({'braces':'balanced','environments':'balanced','display_delimiters':'balanced','dollar_delimiters':'even','macro_names':'approved preamble or standard LaTeX/TikZ','source_C_doubt_rows':15,'local_decision_rows':len(r['differences']),'diff_C_rows':sum(d['diff_C'] for d in r['differences']),'diff_H_rows':sum(d['diff_H'] for d in r['differences']),'remaining_doubt_records':len(r['doubts']),'inventory_items':len(r['inventory']),'crop_files':len(r['crops']),'compiler_invoked':False},indent=2))
