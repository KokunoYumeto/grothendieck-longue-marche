#!/usr/bin/env python3
"""Record a separate context search for every numbered research note; no OCR."""
from pathlib import Path
from datetime import datetime, timezone
import json, re, sys

root=Path(__file__).resolve().parents[1]
context=Path(sys.argv[1]).resolve()
oda=Path(sys.argv[2]).resolve() if len(sys.argv)>2 else None
files=[context/'MPL_16+47+54+44_transcription.tex',context/'MPL_16+47+54+44_notes.md',context/'MPL_16+47+54+44_doubts.md',context/'README.md',context/'notes/RESULTS_STATE.md']
if oda and oda.exists(): files.append(oda)
indexed=[]
for p in files:
    cote=scan=None
    rows=[]
    for n,line in enumerate(p.read_text().splitlines(),1):
        m=re.search(r'\\cotefile\{(\d+)\}',line)
        if m: cote=int(m.group(1))
        m=re.search(r'\\scanpage\{(\d+)\}',line)
        if m: scan=int(m.group(1))
        rows.append((n,line,cote,scan))
    indexed.append((p,rows))
notes=(root/'MPL_11_043-058+56_notes.md').read_text()
parts=re.split(r'(?m)^### (N\d{3}) — ',notes)
result=[]
for i in range(1,len(parts),2):
    ident,body=parts[i:i+2]
    m=re.search(r'\*\*Search:\*\* `([^`]+)`',body)
    if not m: raise ValueError(f'Missing query: {ident}')
    query=m.group(1)
    pattern=re.compile(query,re.I)
    hits=[]
    for p,rows in indexed:
        matched=[{'line':n,'cote':c,'scan':s,'text':line[:360]} for n,line,c,s in rows if pattern.search(line)]
        scopes=sorted({f'{h["cote"]}/{h["scan"]:03d}' for h in matched if h['cote'] is not None and h['scan'] is not None})
        hits.append({'file':p.name,'count':len(matched),'scan_hits':scopes,'sample':matched[:6]})
    result.append({'id':ident,'title':body.splitlines()[0],'query':query,'files':hits})
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(root/'records/context_searches.json').write_text(json.dumps({'searched_utc':stamp,'notes':result},ensure_ascii=False,indent=2)+'\n')
out=['# Per-note context searches','',f'Searched {stamp}. One separately executed query per numbered note; regex, case-insensitive; native text only.','',
'The preceding context ZIP was opened only after the transcription freeze. CT scan numbers below are extracted from the supplied context LaTeX. Counts and snippets document searches, not evidence of mathematical identity; each note states the inspected comparison and its limits. The Oda file searched is a native text-layer extraction of the supplied PDF, not OCR.','']
for row in result:
    out += [f'## {row["id"]} — {row["title"]}','',f'Query: `{row["query"]}`','']
    for h in row['files']:
        out += [f'- **{h["file"]}**: {h["count"]} matching lines.']
        if h['scan_hits']: out += ['  Context scans: '+', '.join(h['scan_hits'])+'.']
        for x in h['sample'][:3]:
            sample=x['text'].replace('`','\\`')
            out += [f'  - L{x["line"]}: `{sample}`']
    out += ['']
(root/'records/context_searches.md').write_text('\n'.join(out)+'\n')
print(f'{len(result)} separate note queries recorded across {len(files)} files.')
