#!/usr/bin/env python3
"""Record per-note literal searches without copying supplied source files."""
from pathlib import Path
from datetime import datetime,timezone
import json,csv,re,hashlib

root=Path(__file__).resolve().parents[1]
context=root.parent/'context'
queries=json.loads((root/'records/context_queries.json').read_text())
files=sorted(p for p in context.rglob('*') if p.is_file())
rows=[];counts={}
for item,terms in queries.items():
    counts[item]=0
    for p in files:
        anchor=''
        for line,text in enumerate(p.read_text().splitlines(),1):
            m=re.search(r'\\scanpage\{([^}]+)\}',text)
            if m:anchor='scan marker '+m[1]
            if text.startswith('#'):anchor=text.lstrip('# ')
            matched=[term for term in terms if term.casefold() in text.casefold()]
            if matched:
                rows.append([item,'; '.join(terms),p.relative_to(context).as_posix(),line,anchor,'; '.join(matched)])
                counts[item]+=1
    if not counts[item]:rows.append([item,'; '.join(terms),'NO LITERAL HIT','','',''])
with (root/'records/context_searches.csv').open('w',newline='') as f:
    w=csv.writer(f);w.writerow(['note_id','query_terms','context_file','line','nearest_source_marker','matched_terms']);w.writerows(rows)
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
(root/'records/context_search_summary.json').write_text(json.dumps({'utc':stamp,'note_hits':counts,'context_file_sha256':{p.relative_to(context).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in files}},indent=2)+'\n')
print(json.dumps(counts,indent=2))
