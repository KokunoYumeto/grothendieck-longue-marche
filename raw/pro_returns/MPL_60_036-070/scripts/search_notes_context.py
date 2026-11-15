#!/usr/bin/env python3
"""Run each finished note's declared search against the supplied text context.

No manuscript image or frozen transcription is read or changed. All hits are
counted; complete line locators and capped snippets are retained for review.
"""
from pathlib import Path
import datetime as dt
import json
import re
import sys

root=Path(__file__).resolve().parents[1]
context=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root.parents[1]/'context'
notes=(root/'MPL_60_036-070_notes.md').read_text()
sources=[context/'MPL_16+47+54+44_transcription.tex',context/'MPL_16+47+54+44_notes.md',context/'notes/RESULTS_STATE.md']
indexed={}
for p in sources:
 rows=[];cote=None;scan=None;heading=None
 for number,line in enumerate(p.read_text().splitlines(),1):
  if p.suffix=='.tex':
   c=re.search(r'\\cotefile\{(\d+)\}',line)
   n=re.search(r'\\scanpage\{(\d+)\}',line)
   if c:cote=int(c[1]);scan=None
   if n:scan=int(n[1])
  if line.startswith('#'):heading=line.lstrip('# ').strip()
  rows.append((number,line,cote,scan,heading))
 indexed[str(p.relative_to(context))]=rows

entries=[]
for m in re.finditer(r'^### ((?:LF|A|C|S)\d+) — ([^\n]+)\n(.*?)(?=^### |^## |\Z)',notes,re.M|re.S):
 ident,title,body=m.groups()
 query=re.search(r'\*\*Context search:\*\* `([^`]+)`',body)
 if not query:raise SystemExit(f'{ident} lacks a context query')
 pattern=re.compile(query[1],re.I)
 result={'id':ident,'title':title,'query':query[1],'files':{}}
 for name,rows in indexed.items():
  hits=[]
  for num,line,cote,scan,heading in rows:
   if pattern.search(line):
    hits.append({'line':num,'cote':cote,'scan':scan,'heading':heading,'snippet':line[:360]})
  result['files'][name]={'count':len(hits),'hits':hits}
 entries.append(result)
out={'searched_utc':dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),'source_scope':'Supplied CT, CN, RESULTS_STATE text only; no scans or OCR','note_count':len(entries),'entries':entries}
dest=root/'records/research_context_search.json'
dest.write_text(json.dumps(out,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'note_count':len(entries),'record':str(dest),'zero_total_hits':[x['id'] for x in entries if sum(f['count'] for f in x['files'].values())==0]},ensure_ascii=False))
