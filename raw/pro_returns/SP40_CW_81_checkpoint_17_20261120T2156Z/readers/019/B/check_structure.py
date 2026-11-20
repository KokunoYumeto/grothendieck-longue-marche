"""Structural source checks only; never invokes TeX or a renderer."""
from pathlib import Path
import json,re
b=Path('/workspace/scratch/94548b74fbe0/out/readers/019/B')
s=(b/'reading.tex').read_text()
r=json.loads((b/'report.json').read_text())
body='\n'.join(line.split('%',1)[0] for line in s.splitlines() if not line.lstrip().startswith('%'))
stack=[]
for m in re.finditer(r'(?<!\\)[{}]',body):
 if m.group()=='{':stack.append(m.start())
 else:
  assert stack,('extra closing brace',m.start())
  stack.pop()
assert not stack,('unclosed braces',stack)
envs=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',body):
 if m.group(1)=='begin':envs.append(m.group(2))
 else:
  assert envs and envs[-1]==m.group(2),('environment mismatch',m.group(0),envs)
  envs.pop()
assert not envs
assert body.count(r'\[')==body.count(r'\]')==5
assert body.count('$')%2==0
for region in re.findall(r'\\\[(.*?)\\\]',body,re.S):
 assert not re.search(r'\n\s*\n',region),'blank line inside display'
assert sorted(e['source_row_id'] for e in r['original_C_doubt_rows'])==[f'R{i:02}' for i in range(1,13)]
assert all((b/e['path']).is_file() for e in r['crops'])
assert all((e['readers_crop'] is None or (b/e['readers_crop']).is_file()) for e in r['differences'])
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}
assert all(e['kind'] in allowed for e in r['differences'])
assert sum(e['diff_C'] for e in r['differences'])==r['counts']['diff_C_total']==8
assert sum(e['diff_H'] for e in r['differences'])==r['counts']['diff_H_total']==13
assert s.count(r'\draw[')==3 and s.count(r'\fill')==4
assert r'\cotefile' not in body
assert r'\unsure{:|à} sommer' in body
assert r'\unsure{deuxième|dernier}' in body
assert r'\unsure{On a|\deleted{O}On a|\deleted{On}On a}' in body
assert r'\deleted{\Sigma_{\unsure{\alpha|0}}}' in body
assert "\\unsure{l\\'" not in body
macros=sorted(set(re.findall(r'\\([A-Za-z]+)',body)))
result={'structural_checks':'passed','brace_balance':'passed','environment_balance':'passed','display_pairs':5,'blank_lines_within_displays':False,'source_rows':12,'crop_files':15,'diff_C':8,'diff_H':13,'literal_graphical_paths':3,'literal_graphical_fills':4,'macros_used':macros,'compiled':False,'rendered':False,'image_reopenings':0}
(b/'structural_check.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(result,ensure_ascii=False))
