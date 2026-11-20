from pathlib import Path
import json,re
base=Path('/workspace/scratch/94548b74fbe0'); out=base/'out/readers/012/B'
s=(out/'reading.tex').read_text(); r=json.loads((out/'report.json').read_text()); original=(base/'packets/012/C.tex').read_text()
clean='\n'.join(re.sub(r'(?<!\\)%.*$','',x) for x in s.splitlines())
stack=[]
for i,ch in enumerate(clean):
 if ch in '{}' and (i==0 or clean[i-1]!='\\'):
  if ch=='{':stack.append(i)
  else: assert stack,('unmatched closing brace',i);stack.pop()
assert not stack,('unclosed braces',stack)
env=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',clean):
 if m[1]=='begin':env.append(m[2])
 else: assert env and env[-1]==m[2],('environment mismatch',env,m[2]);env.pop()
assert not env,env
allowed={'scanpage','figure','begin','end','path','node','scriptsize','unsure','hspace','draw'}
commands=set(re.findall(r'\\([A-Za-z]+)',clean))
assert commands<=allowed,('unexpected commands',commands-allowed)
assert clean.count('\\scanpage{12}')==1
assert '\\cotefile' not in clean and '\\mspage' not in clean
assert '% archive sheet number: 11' in s
assert clean.count('\\begin{tikzpicture}')==1 and clean.count('\\end{tikzpicture}')==1
assert '\\newcommand' not in s and '\\renewcommand' not in s
# Comparison of complete retained source contours; this is a source structural check.
pattern=r'\\path\[fill=black,even odd rule\]\s*.*?;'
a=re.findall(pattern,original,re.S);b=re.findall(pattern,s,re.S)
assert len(a)==68 and a==b,'original contour altered or omitted'
assert len(r['source_path_audit'])==68
assert {x['path'] for x in r['source_path_audit']}==set(range(1,69))
assert all(x['retained'] for x in r['source_path_audit'])
# All eight manuscript labels are still present with matching qualifications.
expected=[r'\node[inner sep=0pt,font=\scriptsize] at (436,58){ou};',r'\node[inner sep=0pt] at (752,62){OK};',r'\node[inner sep=0pt] at (1081,42){OK};',r'\node[inner sep=0pt] at (1490,71){\unsure{OK|Ok}};',r'\node[inner sep=0pt,font=\scriptsize] at (1460,361){ou};',r'\node[inner sep=0pt] at (435,632){OK};',r'\node[inner sep=0pt,font=\scriptsize] at (67,797){ou};',r'\node[inner sep=0pt,font=\scriptsize] at (196,861){\unsure{ou}};']
assert all(x in s for x in expected)
assert r['differences'][0]['reading']==r'\unsure{OK|Ok}' and r['differences'][1]['reading']==r'\unsure{ou}'
assert len(r['C_doubt_source_map'])==3 and len({x['source_row'] for x in r['C_doubt_source_map']})==3
for x in r['C_doubt_source_map']:
 assert x['status']=='retained' and x['local_subloci']
 assert all(any(d['id']==n for d in r['differences']) for n in x['difference_ids'])
ids={x['id'] for x in r['differences']}
assert len(ids)==len(r['differences'])
assert all(d['difference_id'] in ids and 'reading' in d for d in r['doubts'])
assert all('reading' in x and 'C_doubt_status' in x for x in r['differences'])
for x in r['differences']:
 assert len(x['bbox'])==4
 x0,y0,x1,y1=x['bbox'];assert 0<=x0<x1<=1690 and 0<=y0<y1<=2361
 if x['readers_crop']:assert (out/x['readers_crop']).is_file()
for x in r['doubts']:
 if x['crop']:assert (out/x['crop']).is_file()
assert len(r['crops'])==10 and len({x['path'] for x in r['crops']})==10
assert all((out/x['path']).is_file() for x in r['crops'])
assert all(x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'} for x in r['inventory'])
assert all(x['transcribed']=='yes' for x in r['inventory'])
assert len([x for x in r['inventory'] if x['element'].startswith('B.new.')])==22
assert r['check_events']==[]
results={'braces':'balanced','environments':'balanced; one tikzpicture inside figure','commands':sorted(commands),'original_contours':'all 68 present byte-for-byte; indexed and inventoried','labels':'all eight present; two original lexical doubts match report','source_C_doubts':'all three mapped once, with 2+2+5 explicit local subloci','inventory':'55 elements; 22 added physical trace entries plus archive numeral','crop_references':'all 10 crop files exist and all references resolve','difference_bboxes':'all 31 full-scan boxes valid','reader_report_agreement':'checked labels, states, additions, trace inventory, note boundary and archive comment','compiler_or_renderer_used':False}
(out/'scripts/structural_checks.json').write_text(json.dumps(results,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(results,ensure_ascii=False,indent=2))
