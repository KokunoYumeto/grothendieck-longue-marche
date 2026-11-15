"""Make matrix separators safe inside the required diagram/deleted macros."""
from pathlib import Path
import re
n=0
for p in Path('pages').glob('*.tex'):
 s=p.read_text()
 def fix(m):
  global n
  body=m.group(0)
  if 'ampersand replacement=' in body:return body
  n+=1
  if body.startswith(r'\begin{tikzcd}['):
   body=body.replace(r'\begin{tikzcd}[',r'\begin{tikzcd}[ampersand replacement=\&,',1)
  else:body=body.replace(r'\begin{tikzcd}',r'\begin{tikzcd}[ampersand replacement=\&]',1)
  return re.sub(r'(?<!\\)&',r'\\&',body)
 updated=re.sub(r'\\begin\{tikzcd\}.*?\\end\{tikzcd\}',fix,s,flags=re.S)
 if updated!=s:p.write_text(updated)
print('Prepared',n,'tikz-cd environments; labels and directions unchanged')
