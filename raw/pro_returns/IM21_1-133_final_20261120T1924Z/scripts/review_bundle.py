#!/usr/bin/env python3
"""Print specified page proposals and original evidence for main-reader review."""
from pathlib import Path
import json,re,sys
ROOT=Path(__file__).resolve().parents[1]
result=[]
for key in sys.argv[1:]:
    packet=json.loads((ROOT/'page_packets'/f'{key}.json').read_text())
    proposal=json.loads((ROOT/'proposals'/f'{key}.json').read_text())
    contexts=[]
    for row in proposal['rows']:
        if row['decision']=='a' and row['find'] in packet['latex']:
            i=packet['latex'].index(row['find'])
            contexts.append(dict(id=row['id'],original_occurrences=packet['latex'].count(row['find']),context=packet['latex'][max(0,i-100):i+len(row['find'])+100]))
    crops=list(dict.fromkeys(re.findall(r'crops/[A-Za-z0-9_.-]+\.(?:jpg|jpeg|png)',json.dumps(proposal))))
    item=dict(page=key,source_rows=packet['rows'],proposal=proposal,edit_contexts=contexts,crops=crops)
    needs_full=False
    for row in proposal['rows']:
        if row['decision']!='a':
            excerpts=row.get('source_context',[])
            if row['decision']=='d' or not excerpts:
                needs_full=True
            else:
                for excerpt in excerpts:
                    assert excerpt in packet['latex'], (row['id'],'source_context not original')
    if needs_full:item['original']=packet['latex']
    result.append(item)
print(json.dumps(result,ensure_ascii=False))
