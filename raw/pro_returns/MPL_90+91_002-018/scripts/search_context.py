#!/usr/bin/env python3
"""Execute and record each root-authored research item's context query.

This script searches supplied text. It makes no reading, mathematical or
comparison judgments; those are in the root-authored notes.
"""
from pathlib import Path
from datetime import datetime, timezone
import subprocess, json, re, hashlib

w=Path(__file__).resolve().parents[1]
ctx=w.parent/'context'
note_path=w/'MPL_90+91_002-018_notes.md'
source=note_path.read_text()
heads=list(re.finditer(r'^### ([A-Z][A-Z0-9-]+) — (.+)$',source,re.M))
records=[]
paths=sorted(ctx.rglob('*.md'))
assert len(paths)==3
for i,h in enumerate(heads):
    end=heads[i+1].start() if i+1<len(heads) else len(source)
    block=source[h.end():end]
    q=re.search(r'\*\*Context search:\*\* `([^`]+)`',block)
    assert q,h.group(1)
    cmd=['rg','--json','--ignore-case','--regexp',q.group(1),*[str(p) for p in paths]]
    result=subprocess.run(cmd,capture_output=True,text=True)
    assert result.returncode in (0,1),(h.group(1),result.stderr)
    hits=[]
    for line in result.stdout.splitlines():
        event=json.loads(line)
        if event['type']!='match':continue
        d=event['data'];p=Path(d['path']['text'])
        full=d['lines']['text'].rstrip('\n')
        m=re.search(q.group(1),full,re.I)
        pos=m.start() if m else 0
        start=max(0,pos-75);stop=min(len(full),pos+245)
        excerpt=('…' if start else '')+full[start:stop]+('…' if stop<len(full) else '')
        lines=p.read_text().splitlines()
        heading=''
        for earlier in reversed(lines[:d['line_number']]):
            if earlier.startswith('#'):
                heading=earlier;break
        hits.append({'file':str(p.relative_to(ctx)),'line':d['line_number'],
                     'section':heading,'excerpt':excerpt})
    records.append({'id':h.group(1),'title':h.group(2),'query':q.group(1),
                    'searched_files':[str(p.relative_to(ctx)) for p in paths],
                    'utc':datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
                    'returncode':result.returncode,
                    'match_count':len(hits),'hits':hits})
assert len(records)==50,(len(records),'expected complete 50-item research draft')
assert len({r['id'] for r in records})==50
out=w/'records'/'context_searches.jsonl'
out.write_text(''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in records))
md=['# Per-item context search record','',
    'Each query was run with ripgrep against all three supplied context files. Excerpts are retrieval evidence, not endorsements. The complete source files remain outside this deliverable. Mathematical comparisons are the sole reader’s judgments in the notes.','',
    '| Item | Query | Matches | File coverage |','|---|---|---:|---|']
for r in records:
    counts={p:sum(h['file']==p for h in r['hits']) for p in r['searched_files']}
    md.append('| '+r['id']+' | `'+r['query'].replace('|',r'\|')+'` | '+str(r['match_count'])+' | '+'; '.join(p+': '+str(c) for p,c in counts.items())+' |')
for r in records:
    md.extend(['',f"## {r['id']} — {r['title']}",'',f"Query: `{r['query']}`. Executed {r['utc']}. Matches: {r['match_count']}.",''])
    if not r['hits']:md.append('No literal match in the three supplied files.')
    for h in r['hits']:
        md.append(f"- `{h['file']}`:{h['line']} — {h['section']}: {h['excerpt']}")
(w/'records'/'context_searches.md').write_text('\n'.join(md)+'\n')
(w/'records'/'context_source_manifest.json').write_text(json.dumps({
    'read_by':'root, personally','read_order':['README.md','notes/RESULTS_STATE.md','same_cote_91/MPL_91_099-143_notes.md'],
    'source_hashes':{str(p.relative_to(ctx)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths},
    'research_items':len(records),'notes_sha256_at_search':hashlib.sha256(note_path.read_bytes()).hexdigest()
},indent=2)+'\n')
for r in records:
    counts={p:sum(h['file']==p for h in r['hits']) for p in r['searched_files']}
    print(r['id'],r['match_count'],json.dumps(counts,ensure_ascii=False))
