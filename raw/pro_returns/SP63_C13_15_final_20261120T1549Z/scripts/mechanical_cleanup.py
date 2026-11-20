"""Recorded documentation/syntax cleanup; no reading or mathematical decisions."""
from pathlib import Path
import json
from workflow import ROOT,assemble,utc
p=ROOT/'scripts/record_163.py'
p.write_text(''.join(line for line in p.read_text().splitlines(keepends=True) if 'if False else t' not in line))
p=ROOT/'scripts/record_165.py'
text=p.read_text().replace(r"r'\operatorname{frob}_\xi,\operatorname{frob}\x27_\xi; \frac12\text{-linéaire}'",r'''r"\operatorname{frob}_\xi,\operatorname{frob}'_\xi; \frac12\text{-linéaire}"''')
p.write_text(text)
p=ROOT/'records/165.json';d=json.loads(p.read_text())
for n in d['notation']:n[1]=n[1].replace(r'\x27',"'")
p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
p=ROOT/'records/173.json';d=json.loads(p.read_text());d['notes']=d['notes'].replace(r'\n\n','\n\n');p.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
# A text wrapper makes the small TikZ fragment a box inside the math underset.
p=ROOT/'pages/15_scan177.tex';t=p.read_text().replace(r'\underset{\figure{\begin{tikzpicture}',r'\underset{\text{\begin{tikzpicture}');p.write_text(t)
p=ROOT/'scripts/record_177.py';t=p.read_text().replace("fragments=r'\\figure{", "fragments=r'\\text{");p.write_text(t)
for n in [174,176]:
 p=ROOT/f'scripts/record_{n}.py';t=p.read_text().replace("'readable ink left as `\\ill{}`'", "r'readable ink left as `\\ill{}`'");p.write_text(t)
assemble()
with (ROOT/'progress.log').open('a') as f:f.write('documentation and TikZ box syntax cleanup '+utc()+'\n')
