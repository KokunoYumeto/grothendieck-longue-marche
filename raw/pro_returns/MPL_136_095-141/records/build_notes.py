#!/usr/bin/env python3
"""Assemble post-freeze notes and indexes; never write any transcription file."""
from __future__ import annotations
import csv, hashlib, json, re
from collections import Counter
from pathlib import Path
from research_items import ITEMS
from research_context import ANCHORS, REL
ROOT=Path(__file__).resolve().parent.parent
REC=ROOT/'records'
SEARCH=json.loads((REC/'note_context_searches.json').read_text())
S={row['id']:row for row in SEARCH['notes']}
Q={row['id']:row for row in json.loads((REC/'note_quote_locations.json').read_text())}
ids=[x['id'] for x in ITEMS]
assert len(set(ids))==len(ids), 'duplicate IDs'
assert set(ids)==set(S)==set(Q)==set(REL), 'incomplete context/search/location map'
assert SEARCH['query_source_sha256']==hashlib.sha256((REC/'research_items.py').read_bytes()).hexdigest(), 'rerun searches after registry edit'
for x in ITEMS:
    assert x['context'] in ANCHORS and x['body'] and x['quote'] and x['query']
    assert S[x['id']]['status'] in {'matched','no_match'}
    assert Q[x['id']]['status']=='located', 'unlocated quotation cue'
    if 'own idea' in x['kind']: assert x['confidence'], 'own idea lacks confidence/reason'

def nkey(item):
    return int(re.search(r'\d+',item['id']).group())

def code(s):
    # An inline code delimiter longer than the literal French quotation marks.
    runs=re.findall(r'`+',s)
    n=max([len(t) for t in runs]+[0])+1
    return '`'*n+' '+s+' '+'`'*n

texts=[(REC/'notes_frontmatter.md').read_text().rstrip()]
groups=[('N','5.1 Handwritten lecture material and the English donor'),
        ('R','5.2 Reused French mathematical typescripts'),
        ('O','5.3 Independent mathematical diagnostics and proposals'),
        ('L','5.4 Literature and later-context comparisons')]
for prefix,title in groups:
    texts.append('\n### '+title+'\n')
    for x in sorted([x for x in ITEMS if x['id'].startswith(prefix)],key=nkey):
        a=ANCHORS[x['context']]; sr=S[x['id']]; qr=Q[x['id']]
        m=qr['matches'][0]
        p=[f"\n#### {x['id']} — {x['kind']}\n",
           f"**Source:** cote 136, scan(s) {x['scans']}. **Cue location:** scan {m['scan']:03d}, approximately page-file line {m['line']}.",
           f"\n**Frozen-text cue:** {code(x['quote'])}\n",
           x['body'],
           f"\n**Context:** {x['context']}, `{a['path']}`, {a['loc']}. {a['text']} **Relationship:** {REL[x['id']]}",
           f"\n**RESULTS_STATE connection:** {x['results_ids']}."]
        if x['confidence']:
            p.append('\n**Confidence and reason:** '+x['confidence']+'.')
        result=(f"{sr['matching_lines']} matching lines in {sr['matched_file_count']} context files" if sr['status']=='matched' else 'no lexical matches in any of the six context files')
        p.append(f"\n**Search:** {code(x['query'])}; {result}. Complete hits and input hashes: `records/note_context_searches.json`, item {x['id']}.")
        texts.append('\n'.join(p))
texts.append('\n'+(REC/'notes_backmatter.md').read_text().strip()+'\n')
out=ROOT/'MPL_136_095-141_notes.md'
out.write_text('\n'.join(texts),encoding='utf-8')
with (REC/'research_note_index.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['id','cote','scans','kind','quote','context_anchor','results_state_ids','confidence','search_status','matching_lines','matched_file_count']
    w=csv.DictWriter(f,fieldnames=fields);w.writeheader()
    for x in ITEMS:
        s=S[x['id']]
        w.writerow(dict(id=x['id'],cote=136,scans=x['scans'],kind=x['kind'],quote=x['quote'],context_anchor=x['context'],results_state_ids=x['results_ids'],confidence=x['confidence'] or '',search_status=s['status'],matching_lines=s['matching_lines'],matched_file_count=s['matched_file_count']))

def scans_in(s):
    nums=set()
    for a,b in re.findall(r'(\d{3})[–-](\d{3})',s):nums.update(range(int(a),int(b)+1))
    nums.update(map(int,re.findall(r'\b\d{3}\b',s)))
    return nums

admin={110:'Nearly blank reverse: archival foliation only; standing title/numbering section.',
       118:'German letter fragment: standing title/numbering section; no mathematical claim.',
       120:'Reused typewriter letter: date and thirty-page quantity distinguished from lecture dating/count.'}
with (REC/'research_page_coverage.csv').open('w',newline='',encoding='utf-8') as f:
    w=csv.writer(f);w.writerow(['cote','scan','primary_note_ids','disposition'])
    for n in range(95,142):
        if n==122:continue
        matches=[x['id'] for x in ITEMS if x['id'][0] in 'NR' and n in scans_in(x['scans'])]
        assert matches or n in admin, f'scan {n} has no research disposition'
        w.writerow([136,f'{n:03d}','; '.join(matches),admin.get(n,'Individual mathematical/source notes above; full doubt list retained separately.')])
report=dict(notes=len(ITEMS),groups=dict(Counter(x['id'][0] for x in ITEMS)),own_ideas=sum('own idea' in x['kind'] for x in ITEMS),context_files=len(SEARCH['context_files']),search_statuses=dict(Counter(S[x['id']]['status'] for x in ITEMS)),located_cues=len(Q),page_coverage=46,bytes=out.stat().st_size,words=len(out.read_text().split()),notes_sha256=hashlib.sha256(out.read_bytes()).hexdigest())
(REC/'research_notes_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(report,ensure_ascii=False))
