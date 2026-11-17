#!/usr/bin/env python3
"""Index source citations in the supplied returns; this is not a proof checker.
Run from the directory containing LM4_SUCCESSOR/ and background/.
"""
from pathlib import Path
import re,csv
base=Path('background');out=[]
marker=r'\\begin\{(?:claim|statement)\}\{([^}]+)\}|\\(?:statement|claim)\{([^}]+)\}'
for d in ['LM4_return','LM6_return','LM7_PUSH_checkpoint_09','LM7_tower']:
 for p in sorted((base/d).rglob('*.tex')):
  s=p.read_text();ms=list(re.finditer(marker,s))
  for i,m in enumerate(ms):
   end=ms[i+1].start() if i+1<len(ms) else len(s)
   b=re.split(r'\\(?:bibliography|begin\{thebibliography\}|end\{document\})',s[m.start():end])[0]
   hits=[]
   for h in re.finditer(r'\\cite\w*(?:\[[^\]]*\]){0,2}\{([^}]*?(?:Boggi|BZ|Zalesskii)[^}]*?)\}',b,re.I):
    hits.append(re.sub(r'\s+',' ',b[max(0,h.start()-170):min(len(b),h.end()+170)]))
   if hits:out.append({'run':d,'statement':m[1] or m[2],'file':str(p),'line':s[:m.start()].count('\n')+1,'contexts':' || '.join(hits)})
p=Path(__file__).resolve().parents[1]/'records/centralizer_citation_inventory.csv'
with p.open('w') as f:
 w=csv.DictWriter(f,fieldnames=['run','statement','file','line','contexts']);w.writeheader();w.writerows(out)
print('Citation-bearing statement blocks:',len(out))
for r in out:
 if r['run']!='LM4_return':print(r['run'],r['statement'],r['contexts'][:500])
