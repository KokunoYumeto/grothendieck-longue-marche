#!/usr/bin/env python3
from pathlib import Path
import re
r=Path(__file__).resolve().parents[1]
source=r/'notes/source_fragments'
texts=[(r/'notes/root_references.bib').read_text()]+[(source/(n+'_references.bib')).read_text() for n in ['centralizer','tower','ghost']]
entries={}
for text in texts:
 for e in re.split(r'(?=^@)',text,flags=re.M):
  if not e.strip():continue
  key=re.match(r'@\w+\{([^,]+),',e).group(1)
  lines=[]
  for line in e.splitlines():
   if not line.startswith('@') and not re.match(r'\s*(url|doi|eprint)\s*=',line,re.I):line=re.sub(r'(?<!\\)_',r'\\_',line)
   lines.append(line)
  entries[key]='\n'.join(lines).strip()
assert all(re.search(r'\b(?:verified|unverified)\b',e,re.I) for e in entries.values())
(r/'GT_TOWER_CHECK_references.bib').write_text('\n\n'.join(entries.values())+'\n')
print('Bibliography entries:',len(entries),'all carry verification status')
