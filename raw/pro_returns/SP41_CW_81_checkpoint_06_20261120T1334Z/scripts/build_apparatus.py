"""Build human-readable deliverables from adjudicated, source-grounded page records.
No inference of readings, OCR, or automatic collation decisions occur here.
"""
from pathlib import Path
import csv,json,collections,datetime
w=Path(__file__).resolve().parents[1]
records=[json.loads(p.read_text()) for p in sorted((w/'decisions').glob('scan*.json'))]

def cell(v):
    if isinstance(v,list):v='; '.join(str(x) for x in v)
    return str(v or '').replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(cell(x) for x in row)+' |\n' for row in rows)

changes=['# SP41_CW_81 changes and reading decisions\n\nAll readings below were adjudicated against the supplied scan images. C and H are independent draft witnesses; S is the supplied sweep. Raw independent reader returns and crop manifests are retained under `readers/`. Macro-only differences are excluded from H collation. Retained C doubt marks are recorded even where no substantive witness change results.\n\n## Counts\n\n']
countrows=[]; totalC=totalH=0; conf=collections.Counter()
for d in records:
    fs=d['findings']; c=sum(bool(f.get('against_C')) for f in fs);h=sum(bool(f.get('against_H')) for f in fs)
    co=collections.Counter(f.get('confidence','low') for f in fs if f.get('against_C') or f.get('against_H'))
    countrows.append([d['scan'],c,h,co['high'],co['medium'],co['low'],len(d.get('unresolved',[]))]);totalC+=c;totalH+=h;conf.update(co)
countrows.append(['Total',totalC,totalH,conf['high'],conf['medium'],conf['low'],sum(len(d.get('unresolved',[])) for d in records)])
changes.append(table(['Scan','Against C (including doubt status)','Against H','High confidence loci','Medium confidence loci','Low confidence loci','Unresolved loci'],countrows))
changes.append('\nCounts of confidence concern distinct logged change loci, so a locus differing from both witnesses is counted once there. C totals include resolved or changed uncertainty marks as editing changes; they are not an error count. Retained C doubts with no textual change are excluded. H totals count differing primary readings, omissions, placement, drawings and deletion/insertion state; adding or removing a doubt mark alone is excluded.\n\n## Consequential corrections\n\n')
cons=[f"- Scan {d['scan']}, {f['place']}: {f['consequential']}" for d in records for f in d['findings'] if f.get('consequential')]
changes.append('\n'.join(cons) if cons else 'None recorded in decided pages so far.')
coll=[];inv=[];events=[];notes=['# SP41_CW_81 — Notes while reading\n\nThese notes describe the supplied pages. A statement described as the manuscript’s assertion is not certified as true by transcription. Check events state the specific work actually performed. No external research was used.\n']; doubts=[];notation=[];abbrevs=[]
for d in records:
    n=d['scan'];changes.append(f'\n\n## Scan {n:03d}\n\n')
    rows=[]
    for f in d['findings']:
        read=f.get('readers',{})
        rr='; '.join(f'{k}: {v}' for k,v in read.items())
        rows.append([f['id'],f['place'],f['c'],f['h'],f['reading'],rr,f['evidence'],f.get('crop',''),f['confidence'],f.get('c_doubt_status','none')])
        if f.get('against_H') and d.get('hua_has')=='text':
            coll.append([d['folder'],d['their_page'],n,f['place'],f['h'],f['c'],f['reading'],f['evidence'],f['kind'],f.get('marked_in_H','no'),f['confidence']])
    changes.append(table(['ID','Place','C','H','Final','Independent readers R1/R2/R3','What the scan shows / decision','Crop evidence','Confidence','C doubt status'],rows))
    changes.append('\n### Remaining unresolved places\n\n')
    ur=d.get('unresolved',[])
    changes.append(table(['Place','Reading','Alternatives','Confidence','Reason'],[[u['place'],u['reading'],u.get('alternatives',''),u.get('confidence','low'),u.get('reason','')] for u in ur]) if ur else 'None.\n')
    if d.get('sweep'):
        changes.append('\n### Sweep witness S\n\n'+table(['Row ID / place','S reading or claim','Decision from ink','Evidence'],[[s['id'],s['s'],s['decision'],s['evidence']] for s in d['sweep']]))
    for e in d['inventory']: inv.append([n,e['sheet_kind'],e['hand'],e['element'],e['kind'],e['position'],e['first_words_or_objects'],e['transcribed']])
    notes.append(f'\n## Scan {n:03d}\n\n')
    for no in d.get('notes',[]):
        notes.append(f"### {no['id']}\n\n{no['text']}\n")
    for ev in d.get('check_events',[]):events.append([ev['statement_id'],ev['date'],ev['who'],ev['type'],ev['outcome']])
    for u in ur:doubts.append([n,u['place'],u['reading'],u.get('alternatives',''),u.get('confidence','low'),u.get('reason','')])
    notation.extend(d.get('notation',[]));abbrevs.extend(d.get('abbreviations',[]))
(w/'SP41_CW_81_changes.md').write_text(''.join(changes))
(w/'SP41_CW_81_notes.md').write_text(''.join(notes))
for filename,header,data,delimiter in [
 ('SP41_CW_81_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll,'\t'),
 ('SP41_CW_81_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,','),
 ('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events,'\t')]:
    with (w/filename).open('w',newline='') as f:
        wr=csv.writer(f,delimiter=delimiter);wr.writerow(header);wr.writerows(data)
nt=['# Current notation table\n\n']
nt.append(table(['Scan','Sign / form','Ink evidence','Transcription / candidates'],[[a.get('scan',''),a.get('form',''),a.get('evidence',''),a.get('reading','')] for a in notation]))
(w/'notation.md').write_text(''.join(nt))
dt=['# SP41_CW_81 doubts\n\n## Notation table\n\n',nt[1],'\n## Remaining doubts\n\n',table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts),'\n## Abbreviations encountered\n\n']
unique=[];seen=set()
for a in abbrevs:
    key=(a.get('form',''),a.get('expansion',''))
    if key not in seen:seen.add(key);unique.append([*key,a.get('scan','')])
dt.append(table(['As written','Likely expansion (this list only)','Observed scan'],unique))
leg=w/'validation/legibility_note.md'
dt.append('\n## Legibility and witness comparison\n\n'+(leg.read_text() if leg.exists() else 'Reading in progress; assessment will be completed after all pages are decided.\n'))
(w/'SP41_CW_81_doubts.md').write_text(''.join(dt))
trans=['\\cotefile{81}\n']
for d in records:
    t=(w/'pages'/d['filename']).read_text()
    t=t.replace('\\cotefile{81}\n','')
    trans.append(t.rstrip()+'\n\n')
(w/'SP41_CW_81_transcription.tex').write_text(''.join(trans))
print(json.dumps({'decided_pages':len(records),'against_C':totalC,'against_H':totalH,'unresolved':len(doubts),'inventory_elements':len(inv),'check_events':len(events)},ensure_ascii=False))
