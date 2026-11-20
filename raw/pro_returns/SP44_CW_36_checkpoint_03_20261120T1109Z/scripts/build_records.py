"""Rebuild cumulative deliverables from the main reader's per-page decisions.

This script does no recognition and makes no reading decisions. Decision JSONs
are hand-authored after comparing the three independent visual returns.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, json, re

OUT=Path(__file__).resolve().parents[1]
data=[json.loads(p.read_text()) for p in sorted((OUT/'decisions').glob('scan[0-9][0-9][0-9].json'))]
def cell(v):
    if v is None: return '—'
    if isinstance(v,list): v='; '.join(map(str,v))
    return str(v).replace('|','&#124;').replace('\n','<br>')
def table(headers, rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join('---' for _ in headers)+'|']+['| '+' | '.join(cell(v) for v in row)+' |' for row in rows])+'\n'
def write_tsv(name, headers, rows):
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=headers,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)

counts=[]; totals=Counter(); collation=[]; inv=[]; doubts=[]; notation=[]; abbreviations={}; checks=[]
ch=['# SP44_CW_36 — changes and decisions','',
    'Source of authority: the supplied scan images, read independently by three fresh readers per page. Witness C, witness H, and sweep S are drafts. Counts below are by separately recorded locus, not by word or glyph. A locus may differ from both witnesses. Resolution of a C doubt is counted as a C change; retention of a doubt with no reading change is recorded but not counted. Pure macro equivalence is excluded. Reader returns and actual crops are retained in this archive.','', '## Counts','']
cons=[]
for d in data:
    n=int(d['scan']); rows=d['rows']; c=Counter()
    for r in rows:
        ac=bool(r.get('against_C')); ah=bool(r.get('against_H'))
        c['C']+=ac; c['H']+=ah
        if ac or ah: c[r['confidence']]+=1
        if r.get('consequential'): cons.append(f"- Scan {n:03d}, {r['place']}: {r['consequential']}")
        if ah:
            collation.append(dict(folder=d['folder'],their_page=n-1,our_scan=n,line=r['place'],their_reading=r['H'],codex_reading=r['C'],final_reading=r['final'],scan_shows=r['ink']+' Evidence: '+r.get('evidence',''),kind=r['kind'],marked_in_H='yes' if r.get('marked_in_H') else 'no',confidence=r['confidence']))
    totals.update(c);counts.append([f'{n:03d}',c['C'],c['H'],c['high'],c['medium'],c['low']])
    inv.extend(dict(scan=n,**r) for r in d['inventory'])
    doubts.extend(dict(scan=n,**r) for r in d.get('unresolved',[]))
    notation.extend(dict(first_scan=n,**r) for r in d.get('notation',[]))
    for a in d.get('abbreviations',[]): abbreviations.setdefault(a['form'],a['expansion'])
    for ev in d.get('check_events',[]):
        checks.append(dict(statement_id=ev['statement_id'],date=ev.get('date',d['decided_utc'][:10]),who=ev.get('who','GPT-6 Astra Pro; effort not exposed; main reader, SP44_CW_36 run'),type=ev['type'],outcome=ev['outcome']))
counts.append(['TOTAL',totals['C'],totals['H'],totals['high'],totals['medium'],totals['low']])
ch += [table(['Scan','Against C','Against H','High','Medium','Low'],counts), '## Consequential decisions','']
ch += cons if cons else ['None recorded yet.']
for d in data:
    n=d['scan'];ch += ['',f'## Scan {n:03d}','',d.get('overview',''),'']
    rr=[]
    for i,r in enumerate(d['rows'],1):
        readings=r.get('readers',['see R1 reading.tex','see R2 reading.tex','see R3 reading.tex'])
        rr.append([f'{n:03d}-{i:02d} · '+r['place'],r['C'],r['H'],r['final'],r['ink']+' '+r.get('evidence',''),r['confidence'],' / '.join(f'R{k+1}: {v}' for k,v in enumerate(readings)),r.get('decision','')])
    ch += [table(['Place / ID','C','H','Final','Scan evidence / crop','Confidence','Three readings','Decision'],rr),'### Unresolved after adjudication','']
    u=d.get('unresolved',[])
    ch += [table(['Place','Reading','Alternatives','Confidence','Reason'],[[r['place'],r['reading'],r.get('alternatives',[]),r['confidence'],r['reason']] for r in u]) if u else 'None.']
    if d.get('sweep'):
        ch += ['', '### Witness S review','',table(['S row (`where`)','S reading / claim','Ink decision','Disposition'],[[r['where'],r['S'],r['ink'],r['disposition']] for r in d['sweep']])]
(OUT/'SP44_CW_36_changes.md').write_text('\n'.join(ch)+'\n')
write_tsv('SP44_CW_36_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
with (OUT/'SP44_CW_36_inventory.csv').open('w',newline='',encoding='utf-8') as f:
    fields=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']
    w=csv.DictWriter(f,fieldnames=fields,extrasaction='ignore');w.writeheader();w.writerows(inv)
write_tsv('notation_observations.tsv',['sign','appearance','convention','first_scan','evidence'],notation)
canonical_path=OUT/'validation/notation_final.json'
canonical=json.loads(canonical_path.read_text()) if canonical_path.exists() else None
display_notation=canonical['entries'] if canonical else notation
write_tsv('notation.tsv',['sign','appearance','convention','first_scan','evidence'],display_notation)
db=['# SP44_CW_36 — notation and doubts','','## Notation table','',
    'Entries are observations of the cited ink. They do not authorize changing a later glyph. A separate underline, double striking, typewriter damage, and a handwritten replacement are distinguished locally.','',
    table(['Sign','Appearance','LaTeX convention','First scan','Evidence'],[[r['sign'],r['appearance'],r.get('convention',r.get('latex','')),r['first_scan'],r['evidence']] for r in display_notation]),
    '## Remaining doubts','',table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],[[r['scan'],r['place'],r['reading'],r.get('alternatives',[]),r['confidence'],r['reason']] for r in doubts]),
    '## Abbreviations (expansions only in this list)','',table(['On the page','Likely expansion'],sorted(abbreviations.items())),
    '## Legibility and witnesses','']
for d in data:
    if d.get('legibility'): db.append(f"- Scan {d['scan']:03d}: {d['legibility']}")
if canonical:
    db += ['', '## Final cross-page notation review','',canonical['review_summary'],'',
           'The complete page-local observation table is retained in notation_observations.tsv. The table at the top consolidates recurrent conventions while preserving the cited local alphabet and correction-layer variants.']
(OUT/'SP44_CW_36_doubts.md').write_text('\n'.join(db)+'\n')
notes=['# SP44_CW_36 — notes while reading','',
    'These notes concern only scans 010–027 in the supplied package. No published version or external literature was consulted. Descriptions of a mathematical assertion report what this draft says; they do not certify it. Actual checks and their limits are recorded in CHECK_EVENTS.tsv. The transcription preserves the ink even where a mathematical diagnostic suggests a slip.','']
for d in data:
    notes += [f"## Scan {d['scan']:03d}",'']
    for j,note in enumerate(d.get('notes',[]),1):
        notes += [f"**N{d['scan']:03d}.{j}.** {note}",'']
(OUT/'SP44_CW_36_notes.md').write_text('\n'.join(notes))
write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
(OUT/'SP44_CW_36_transcription.tex').write_text('\n'.join((OUT/'pages'/d['filename']).read_text().rstrip() for d in data)+'\n' if data else '')
runs=[]
for d in data:
    for rr in ('R1','R2','R3'):
        rp=OUT/'readers'/f"scan{d['scan']:03d}"/rr/'result.json'
        rd=json.loads(rp.read_text())
        runs.append(dict(scan=d['scan'],reader=rr,task_name=f"/root/scan{d['scan']:03d}_{rr.lower()}",fork_turns='none',model='inherited GPT-6 Astra Pro',effort='not exposed',started_utc=rd.get('started_utc','not recorded'),ended_utc=rd.get('ended_utc','not recorded'),brief=d.get('brief'),whole_and_halves_viewed='see independent report',status='complete'))
write_tsv('RUNS.tsv',['scan','reader','task_name','fork_turns','model','effort','started_utc','ended_utc','brief','whole_and_halves_viewed','status'],runs)
summary={'decided_scans':[d['scan'] for d in data],'counts':dict(totals),'collation_rows':len(collation),'inventory_rows':len(inv),'remaining_doubt_rows':len(doubts)}
(OUT/'validation/current_counts.json').write_text(json.dumps(summary,indent=2))
print(json.dumps(summary))
