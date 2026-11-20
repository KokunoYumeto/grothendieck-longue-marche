from pathlib import Path
import json,re,difflib
root=Path('/workspace/scratch/006c0e32b2af/out/readers/scan075/C')
s=(root/'reading.tex').read_text()
r=json.loads((root/'report.json').read_text())
code='\n'.join(re.split(r'(?<!\\)%',line,maxsplit=1)[0] for line in s.splitlines())
depth=0
for i,c in enumerate(code):
 if c in '{}':
  n=0;j=i-1
  while j>=0 and code[j]=='\\': n+=1;j-=1
  if n%2: continue
  depth+=(1 if c=='{' else -1)
  assert depth>=0,('early closing brace',i)
assert depth==0,depth
stack=[]
for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',code):
 if m.group(1)=='begin': stack.append(m.group(2))
 else:
  assert stack and stack.pop()==m.group(2),m.group(0)
assert not stack,stack
assert code.count(r'\(')==code.count(r'\)')
assert code.count(r'\[')==code.count(r'\]')
assert len(r['image_views'])==3
assert len(set(c['file'] for c in r['crops']))==len(r['crops'])
assert all((root/c['file']).exists() for c in r['crops'])
assert all(d['h_reading'] is None and d['diff_h'] is False for d in r['decisions'])
assert all(len(d['bbox'])==4 for d in r['decisions'])
assert sum(d['c_doubt'] for d in r['decisions'])==4
assert code.startswith(r'\scanpage{75}')
assert r'\cotefile' not in code
assert r'\mspage' not in code
assert code.count(r'\deleted{')==2
arrows=re.findall(r'\\arrow\[([rd])',code)
assert arrows.count('r')==6 and arrows.count('d')==3,arrows
summary={
 'braces':'balanced', 'environments':'balanced', 'inline_math_pairs':code.count(r'\('),
 'display_math_pairs':code.count(r'\['), 'diagram_right_arrows':arrows.count('r'),
 'diagram_down_arrows':arrows.count('d'), 'cancellations':code.count(r'\deleted{'),
 'report_json':'valid', 'all_H_readings':None, 'all_H_differences':False,
 'C_doubt_rows':4, 'crop_files':len(r['crops']), 'tex_compilation':'not run'
}
(root/'structure_check.json').write_text(json.dumps(summary,indent=2)+'\n')
print(json.dumps(summary,indent=2))
base=Path('/workspace/scratch/006c0e32b2af/packets/scan075/C.tex').read_text()
print(''.join(difflib.unified_diff(base.splitlines(True),s.splitlines(True),fromfile='packet C.tex',tofile='reading.tex')))
