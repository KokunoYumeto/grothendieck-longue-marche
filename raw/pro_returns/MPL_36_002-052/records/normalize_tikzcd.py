from pathlib import Path
import re
from reconcile import revise,ROOT
for p in sorted((ROOT/'pages').glob('*.tex')):
 s=p.read_text()
 def convert(m):
  options=(m.group(1) or '')
  if 'ampersand replacement' in options:return m.group(0)
  inner=options[1:-1] if options else ''
  opts=r'[ampersand replacement=\&'+(', '+inner if inner else '')+']'
  body=re.sub(r'(?<!\\)&',r'\\&',m.group(2))
  return r'\begin{tikzcd}'+opts+body+r'\end{tikzcd}'
 new=re.sub(r'\\begin\{tikzcd\}(\[[^\]]*\])?(.*?)\\end\{tikzcd\}',convert,s,flags=re.S)
 if new!=s:revise(int(p.stem[-3:]),s,new,'Encoded tikz-cd alignment separators with ampersand replacement so diagrams compile safely inside the required macro arguments; no visible content change.')
