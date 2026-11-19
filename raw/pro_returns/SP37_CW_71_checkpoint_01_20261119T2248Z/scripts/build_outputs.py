#!/usr/bin/env python3
"""Assemble reviewed decision records; never reads or recognizes scan images."""
from pathlib import Path
import json,csv,re,collections
ROOT=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((ROOT/'decisions').glob('scan*.json'))]
def md(s):
    if not isinstance(s,str):s=json.dumps(s,ensure_ascii=False)
    return s.replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','| '+' | '.join(['---']*len(headers))+' |']+['| '+' | '.join(md(c) for c in row)+' |' for row in rows])+'\n'
counts=[]; totals=collections.Counter(); consequential=[]
for r in records:
    c=collections.Counter()
    for x in r['issues']:
        c['C']+=bool(x.get('against_C')); c['H']+=bool(x.get('against_H'))
        if x.get('against_C') or x.get('against_H'):c[x['confidence']]+=1
        if x.get('consequential'):consequential.append(f"- Scan {r['scan']}, {x['place']}: {x['consequential']}")
    totals.update(c); counts.append([r['scan'],c['C'],c['H'],c['high'],c['medium'],c['low']])
counts.append(['Total',totals['C'],totals['H'],totals['high'],totals['medium'],totals['low']])
change=['# SP37_CW_71 — consolidated changes and decisions\n',
'Counts are places, not characters or words. A place may differ from both witnesses. Resolved doubt marks and altered diplomatic states count as C changes; retained doubts and confirmations of S are recorded but do not add changes. H summaries are not treated as literal transcriptions; on pages classified as text, omitted main text is counted by coherent block. Pages classified desc or nothing have no H collation rows. Macro-only differences do not count.\n',
table(['Scan','Changes vs C','Changes vs H','High','Medium','Low'],counts),
'## Consequential corrections and preserved slips\n\n'+'\n'.join(consequential or ['None recorded.'])+'\n']
collation=[];inventory=[];notes=['# SP37_CW_71 — Notes while reading\n\nNo material beyond the supplied pages and witnesses was researched. A report of a manuscript claim does not certify its proof. Mathematical checks actually performed are distinguished in CHECK_EVENTS.tsv.\n'];doubts=[];abbreviations={};events=[]
for r in records:
    n=r['scan']; change.append(f'## Scan {n:03d}\n\n'+r.get('overview','')+'\n')
    issue_rows=[]
    for x in r['issues']:
        evidence=x['evidence']
        if x.get('image'):evidence+=' Evidence: `'+x['image']+'`.'
        if x.get('readers'):
            evidence+=' Readers: '+'; '.join(f'{k}: {v}' for k,v in x['readers'].items())+'.'
        if x.get('S'):evidence+=' S: '+x['S']+'.'
        issue_rows.append([x.get('id',''),x['place'],x.get('C',''),x.get('H',''),x['reading'],evidence,x['confidence']])
        if x.get('against_H'):
            collation.append([r['folder'],n-1,n,x['place'],x.get('H',''),x.get('C',''),x['reading'],evidence,x.get('kind','other'),x.get('H_marked','no'),x['confidence']])
    change.append(table(['ID','Place','C','H','Final','Scan evidence and decision','Confidence'],issue_rows))
    change.append('### Still unresolved\n\n'+ ('\n'.join('- '+d['place']+': '+d['reading']+'; '+d.get('reason','') for d in r.get('doubts',[])) or 'None.')+'\n')
    for v in r['inventory']:inventory.append([n,v['sheet_kind'],v['hand'],v['element'],v['kind'],v['position'],v['first_words_or_objects'],v['transcribed']])
    notes.append(f'## Scan {n:03d}\n\n'+r.get('notes','')+'\n')
    for d in r.get('doubts',[]):doubts.append([n,d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
    for a in r.get('abbreviations',[]):abbreviations[a['form']]=a['meaning']
    events.extend(r.get('check_events',[]))
(ROOT/'SP37_CW_71_changes.md').write_text('\n'.join(change))
(ROOT/'SP37_CW_71_notes.md').write_text('\n'.join(notes))
for name,headers,rows,delimiter in [
    ('SP37_CW_71_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation,'\t'),
    ('SP37_CW_71_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,','),
    ('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],[[e.get(k,'') for k in ['statement_id','date','who','type','outcome']] for e in events],'\t')]:
    with (ROOT/name).open('w',newline='') as f:
        w=csv.writer(f,delimiter=delimiter);w.writerow(headers);w.writerows(rows)
legibility=(ROOT/'legibility.md').read_text() if (ROOT/'legibility.md').exists() else 'Legibility assessment will be completed after the last page.'
(ROOT/'SP37_CW_71_doubts.md').write_text((ROOT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations (expansions here only)\n\n'+table(['Written form','Probable expansion'],sorted(abbreviations.items()))+'\n## Legibility and witness comparison\n\n'+legibility+'\n')
page_files=[ROOT/'pages'/r['page_file'] for r in records]
(ROOT/'SP37_CW_71_transcription.tex').write_text('\n'.join(p.read_text().rstrip() for p in page_files)+'\n')
print(json.dumps({'pages':len(records),'changes_C':totals['C'],'changes_H':totals['H'],'inventory_elements':len(inventory),'doubts':len(doubts),'check_events':len(events)},ensure_ascii=False))
