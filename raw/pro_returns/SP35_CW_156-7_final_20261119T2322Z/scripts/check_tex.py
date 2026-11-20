#!/usr/bin/env python3
"""Structural checks only; does not infer or alter manuscript readings."""
from pathlib import Path
import re,json,sys
root=Path(__file__).resolve().parents[1]
files=sorted((root/'pages').glob('*.tex'))
combined=root/'SP35_CW_156-7_transcription.tex'
if combined.exists():files.append(combined)
results=[]
for p in files:
 s=p.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s)
 errors=[];stack=[]
 for m in re.finditer(r'(?<!\\)[{}]',s):
  if m.group()=='{':stack.append(m.start())
  elif stack:stack.pop()
  else:errors.append(f'unmatched closing brace at {m.start()}')
 if stack:errors.append(f'{len(stack)} unmatched opening braces')
 env=[]
 for m in re.finditer(r'\\(begin|end)\{([^{}]+)\}',s):
  typ,name=m.groups()
  if typ=='begin':env.append(name)
  elif not env or env.pop()!=name:errors.append(f'environment mismatch {name}')
 if env:errors.append(f'unclosed environments {env}')
 if len(re.findall(r'(?<!\\)\$',s))%2:errors.append('odd number of unescaped dollar signs')
 if s.count('\\[')!=s.count('\\]'):errors.append('display delimiter imbalance')
 if s.count('\\(')!=s.count('\\)'):errors.append('inline delimiter imbalance')
 for envtext in re.findall(r'\\begin\{tikzcd\}(.*?)\\end\{tikzcd\}',s,re.S):
  if 'ampersand replacement=\\&' not in envtext:errors.append('tikzcd missing ampersand replacement')
 results.append({'file':str(p.relative_to(root)),'errors':errors,'unsure':s.count('\\unsure{'),'illegible':s.count('\\illegible{'),'deleted':s.count('\\deleted{'),'inserted':s.count('\\inserted{'),'margin':s.count('\\margin{')})
print(json.dumps(results,ensure_ascii=False,indent=2))
sys.exit(any(r['errors'] for r in results))
