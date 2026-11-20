#!/usr/bin/env python3
"""Assemble the diplomatic deliverables from explicitly adjudicated page records."""
from pathlib import Path
from collections import Counter
import csv, json, re

OUT=Path(__file__).resolve().parent.parent
PREFIX='SP54_CW_57+63'
MAP=json.loads((OUT/'records/page_order.json').read_text())
records=[]
for m in MAP:
    p=OUT/'records'/(m['page']+'.json')
    if p.exists():records.append(json.loads(p.read_text()))

def md(v):
    if v is None:return '—'
    if isinstance(v,(dict,list)):v=json.dumps(v,ensure_ascii=False)
    return str(v).replace(str(OUT)+'/','').replace('|','&#124;').replace('\n','<br>')
def code(v):return '`'+md(v)+'`' if v is not None else '—'
def readlabel(r):return f"cote {r['cote']}, scan {int(r['our_scan']):03d}"
def write_tsv(name,columns,rows):
    with (OUT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=columns,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)

changes=['# Changes and ink decisions','',
    'Each count is a place recorded in the tables below. A place can count against both witnesses. Certainty-mark changes are included against C; equivalent macro syntax is excluded. H has textual collation only on cote 57 scans 022–023 and 073–079. All cote 63 H entries are descriptions, so they generate no H collation rows.','',
    '| Page | Changes against C | Changes against H | High | Medium | Low |','|---|---:|---:|---:|---:|---:|']
tot=Counter(); collation=[]; inventory=[]; notes=['# Notes while reading','',
    'These notes describe what the supplied pages say. A transcription or descriptive summary is not a proof certificate. Mathematical check events are recorded at their actual level in CHECK_EVENTS.tsv. No external texts were consulted.','']
all_doubts=[]; abbreviations=[]; events=[]; consequence=[]
for r in records:
    cc=Counter()
    for x in r.get('changes',[]):
        cc['C']+=bool(x.get('differs_c'));cc['H']+=bool(x.get('differs_h'));cc[x['confidence']]+=1
    tot.update(cc)
    changes.append('| '+readlabel(r)+' | '+' | '.join(str(cc[k]) for k in ['C','H','high','medium','low'])+' |')
changes.append('| **Total** | '+' | '.join('**'+str(tot[k])+'**' for k in ['C','H','high','medium','low'])+' |')
changes+=['','## Consequential corrections','']
for r in records:
    for x in r.get('changes',[]):
        if x.get('mathematical_consequence'):
            consequence.append('- '+readlabel(r)+', '+x['place']+': '+x['mathematical_consequence'])
changes+=consequence or ['None recorded so far.']
for r in records:
    label=readlabel(r)
    changes+=['','## '+label,'',
      '| Place | C | H | Final reading | Three independent readings | What the scan shows; adjudication evidence | Confidence |',
      '|---|---|---|---|---|---|---|']
    for x in r.get('changes',[]):
        readings=x.get('reader_readings',{})
        rr='; '.join(k+': '+code(v) for k,v in readings.items())
        evidence=(x.get('scan_shows','')+' '+x.get('decision_reason','')+' Evidence: '+str(x.get('evidence',''))).replace(str(OUT)+'/', '')
        changes.append('| '+' | '.join([md(x['place']),code(x.get('c')),code(x.get('h')),code(x['final']),rr,md(evidence),x['confidence']])+' |')
        if x.get('differs_h'):
            collation.append(dict(folder=r['folder'],their_page=r['their_page'],our_scan=r['our_scan'],line=x['place'],their_reading=x.get('h',''),codex_reading=x.get('c',''),final_reading=x['final'],scan_shows=evidence,kind=x['kind'],marked_in_H=x.get('h_marked','no'),confidence=x['confidence']))
    if not r.get('changes'):changes+=['| No reading differences | — | — | — | — | Three readings compared. | — |']
    changes+=['','### C doubt decisions','']
    for d in r.get('c_doubts',[]):
        changes.append('- '+md(d['place'])+': '+code(d['c'])+' → '+code(d['reading'])+'; '+d['status']+'. '+md(d.get('evidence','')))
    if not r.get('c_doubts'):changes.append('No C doubt marks on this page.')
    if r.get('prior_flags'):
        changes+=['','### Other prior C questions','']
        for d in r['prior_flags']:
            if 'reading' in d:
                changes.append('- '+md(d['place'])+': '+code(d['reading'])+'; '+d.get('status','reviewed')+'. '+md(d.get('evidence',d.get('decision',''))))
            else:
                changes.append('- '+md(d.get('place',''))+': '+md(d.get('prior',''))+'. '+md(d.get('decision','')))
    if r.get('reader_only_decisions'):
        changes+=['','### Reader disagreements retaining both witnesses','']
        for d in r['reader_only_decisions']:
            readings='; '.join(k+': '+code(v) for k,v in d['reader_readings'].items())
            changes.append('- '+md(d['place'])+': '+readings+'. Final '+code(d['final'])+'. '+md(d['scan_shows'])+' Evidence: '+md(d['evidence'])+'. These do not count as changes against C or H.')
    changes+=['','### Unresolved places','']
    ds=r.get('remaining_doubts',[])
    for d in ds:
        changes.append('- '+md(d['place'])+': '+code(d['reading'])+'; alternatives '+md(d.get('alternatives',[]))+'; '+d['confidence']+'. '+md(d.get('reason','')))
        all_doubts.append((r,d))
    if not ds:changes.append('None.')
    for x in r['inventory']:inventory.append(dict(scan=str(r['cote'])+'/'+str(r['our_scan']).zfill(3),**x))
    n=r.get('notes',{})
    notes+=['## '+label,'','Statement id: `'+r['page']+':summary`.','',n.get('summary','')]
    for title,key in [('Mathematics and reading decisions','reading_decisions'),('Author’s own checks and doubts','author_checks'),('Titles, dates and pagination','titles_dates_pagination')]:
        values=n.get(key,[])
        notes+=['','### '+title,'']
        if isinstance(values,str):notes.append(values)
        elif isinstance(values,dict):
            for key,value in values.items():
                rendered='not recorded' if value is None else (json.dumps(value,ensure_ascii=False) if isinstance(value,(list,dict)) else str(value))
                notes.append('- '+key.replace('_',' ')+': '+rendered)
        elif values:
            for v in values:
                if isinstance(v,str): notes.append('- '+v)
                elif isinstance(v,dict):
                    place=v.get('place',''); reading=v.get('readings',''); reason=v.get('reason','')
                    quote=v.get('quote',''); body=v.get('text',''); form=v.get('form','')
                    if place or reading or reason or quote or body:
                        notes.append('- '+('**'+place+'.** ' if place else '')+('Readings: `'+reading+'`. ' if reading else '')+('`'+quote+'`. ' if quote else '')+body+(' ('+form+')' if form else '')+(' '+reason if reason else ''))
                    else:notes.append('- '+'; '.join(str(k)+': '+str(val) for k,val in v.items()))
                else:notes.append('- '+str(v))
        else:notes.append('None recorded on this page.')
    notes+=['']
    abbreviations += [(r,a) for a in r.get('abbreviations',[])]
    events+=r.get('check_events',[])

(OUT/(PREFIX+'_changes.md')).write_text('\n'.join(changes)+'\n')
(OUT/(PREFIX+'_notes.md')).write_text('\n'.join(notes)+'\n')
write_tsv(PREFIX+'_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
with (OUT/(PREFIX+'_inventory.csv')).open('w',newline='',encoding='utf-8') as f:
    w=csv.DictWriter(f,fieldnames=['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore');w.writeheader();w.writerows(inventory)

doubts=[(OUT/'notation.md').read_text().rstrip(),'','## Remaining doubts','',
  '| Scan | Place | Reading | Alternatives | Confidence | Ink evidence |','|---|---|---|---|---|---|']
for r,d in all_doubts:
    doubts.append('| '+' | '.join([readlabel(r),md(d['place']),code(d['reading']),md(d.get('alternatives',[])),d['confidence'],md(d.get('reason',''))])+' |')
if not all_doubts:doubts+=['| — | — | No unresolved reading recorded so far | — | — | — |']
doubts+=['','## Abbreviations','',
  'Expansions in this table are interpretive aids only and do not enter the transcription.','',
  '| Page | Abbreviation as written | Proposed expansion | Place |','|---|---|---|---|']
for r,a in abbreviations:
    doubts.append('| '+' | '.join([readlabel(r),code(a.get('abbreviation')),md(a.get('proposed_expansion')),md(a.get('place'))])+' |')
lp=OUT/'records/legibility.md'
doubts+=['','## Legibility and witness comparison','',lp.read_text().strip() if lp.exists() else 'Assessment remains in progress; see the page-specific unresolved readings above.']
(OUT/(PREFIX+'_doubts.md')).write_text('\n'.join(doubts)+'\n')
write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)

parts=[]
for r in records:
    parts.append((OUT/'pages'/(r['page']+'.tex')).read_text().rstrip()+'\n')
(OUT/(PREFIX+'_transcription.tex')).write_text('\n'.join(parts))
print(json.dumps({'pages':len(records),'changes_C':tot['C'],'changes_H':tot['H'],'changes_confidence':{k:tot[k] for k in ['high','medium','low']},'inventory_elements':len(inventory),'unresolved':len(all_doubts),'events':len(events)},ensure_ascii=False))
