from pathlib import Path
from datetime import datetime,timezone
import re
ROOT=Path(__file__).resolve().parents[1]
assert 'transcription frozen' not in (ROOT/'progress.log').read_text()
changed=[]
for p in sorted((ROOT/'pages').glob('*.tex')):
 s=p.read_text(); before=s
 s=s.replace(r'\unsure D',r'\unsure{D}').replace(r'\unsure R',r'\unsure{R}').replace(r'\unsure\tau',r'\unsure{\tau}')
 def cd(m):
  body=m.group(1)
  if 'ampersand replacement=' in body[:120]:return m.group(0)
  stack=[]; parts=[]; last=0
  for t in re.finditer(r'\\(begin|end)\{([^}]+)\}|(?<!\\)&',body):
   if t.group(1)=='begin':stack.append(t.group(2))
   elif t.group(1)=='end':
    assert stack and stack[-1]==t.group(2)
    stack.pop()
   elif not stack:
    parts.append(body[last:t.start()]);parts.append(r'\&');last=t.end()
  parts.append(body[last:]);body=''.join(parts)
  if body.startswith('['):body='[ampersand replacement=\\&,'+body[1:]
  else:body='[ampersand replacement=\\&]'+body
  return r'\begin{tikzcd}'+body+r'\end{tikzcd}'
 s=re.sub(r'\\begin\{tikzcd\}([\s\S]*?)\\end\{tikzcd\}',cd,s)
 marker=r'\diagram{\begin{array}'
 while marker in s:
  start=s.index(marker); opening=start+len(r'\diagram'); pos=opening+1;depth=1
  while depth:
   if s[pos]=='\\':
    t=re.match(r'\\(?:[A-Za-z]+|.)',s[pos:]);pos+=len(t.group());continue
   if s[pos]=='{':depth+=1
   elif s[pos]=='}':depth-=1
   pos+=1
  closing=pos-1
  s=s[:opening+1]+r'\('+s[opening+1:closing]+r'\)'+s[closing:]
 if s!=before:p.write_text(s);changed.append(p.name)
with (ROOT/'progress.log').open('a') as f:
 f.write('mechanical syntax normalization '+datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')+'; explicit TikZ ampersand replacement; explicit math around two array tables; three custom-macro arguments braced; no reading altered\n')
print('Normalized',len(changed),'files')
