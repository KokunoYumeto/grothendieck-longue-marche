from pathlib import Path
import re,sys
sys.path.insert(0,str(Path(__file__).parent))
from workflow import ROOT,PREFIX,utc,update_doubts
n=0
for p in sorted((ROOT/'pages').glob('*.tex')):
 t=p.read_text()
 def fix(m):
  global n
  n+=1
  opts=m[1]
  opts=('ampersand replacement=\\&,'+opts[1:-1]) if opts else 'ampersand replacement=\\&'
  body=m[2].replace('&',r'\&')
  return r'\begin{tikzcd}['+opts+']'+body+r'\end{tikzcd}'
 t=re.sub(r'\\begin\{tikzcd\}(\[[^\]]*\])?(.*?)\\end\{tikzcd\}',fix,t,flags=re.S)
 p.write_text(t)
(ROOT/f'{PREFIX}_transcription.tex').write_text('\n'.join(p.read_text().rstrip() for p in sorted((ROOT/'pages').glob('*.tex')))+'\n')
update_doubts()
with (ROOT/'progress.log').open('a') as f:f.write(f'LaTeX technical revision: explicit ampersand replacement in {n} tikz-cd environments passed as macro arguments {utc()}\n')
print(n,'tikz-cd environments adjusted')
