#!/usr/bin/env python3
"""Render the decided, ink-adjudicated records; never chooses a reading."""
from pathlib import Path
from collections import Counter
import csv, json

ROOT = Path(__file__).resolve().parents[1]
records = [json.loads(p.read_text()) for p in sorted((ROOT/'decisions').glob('scan[0-9][0-9][0-9].json'))]

def md(s):
    return str(s).replace('|', '\\|').replace('\n', '<br>')

def code(s):
    return '`'+md(s)+'`' if s else '—'

changes = ['# Changes against witnesses C and H', '',
           'Each count is a distinct adjudicated locus, including removal or revision of a C doubt marker. A locus can differ from both witnesses. Confidence counts cover the union of changed loci, counting each locus once even when it differs from both witnesses. Pure macro-syntax differences are excluded. Retained C doubts are recorded below their page table without being counted as changes. H has no text for scan 030, which therefore contributes no H collation rows. Reader A/B/C names identify the three new independent readings; “witness C” identifies the earlier supplied transcription.', '',
           '## Counts', '', '| Scan | Against C | Against H | High | Medium | Low |', '|---|---:|---:|---:|---:|---:|']
total = Counter()
for rec in records:
    loci = [x for x in rec['loci'] if x.get('diff_C') or x.get('diff_H')]
    count=Counter(x['confidence'] for x in loci)
    count['C']=sum(bool(x.get('diff_C')) for x in loci)
    count['H']=sum(bool(x.get('diff_H')) for x in loci)
    total.update(count)
    changes.append(f"| {rec['scan']:03} | {count['C']} | {count['H']} | {count['high']} | {count['medium']} | {count['low']} |")
changes += [f"| **Total** | **{total['C']}** | **{total['H']}** | **{total['high']}** | **{total['medium']}** | **{total['low']}** |", '', '## Consequential corrections and retained mathematical readings', '']
for rec in records:
    for item in rec.get('consequential',[]):
        changes.append(f"- Scan {rec['scan']:03}: {item}")
changes += ['', '## Page decisions', '']

collation=[]; inventory=[]; checks=[]; notes=['# Notes while reading','','The seven supplied scans, their associated witnesses and earlier notes were the only manuscript sources. The separate CHECK_EVENTS.tsv identifies the mathematical checks actually carried out, their scope and limitations; visual reading events remain in the reader reports. No outside literature was researched.','']
doubt_rows=[]; abbrevs=[]
for rec in records:
    scan=rec['scan']
    changes += [f'### Scan {scan:03}', '', '| ID / place | Witness C | Witness H | Consolidated reading | Ink evidence and adjudication | Confidence |', '|---|---|---|---|---|---|']
    for x in rec['loci']:
        if x.get('diff_C') or x.get('diff_H'):
            evidence=x['evidence']
            if x.get('crop'): evidence+=' Crop: '+x['crop']+'.'
            readings=x.get('readers')
            if readings:
                evidence+=' Independent readings: '+ '; '.join(f'{k}: {v}' for k,v in readings.items())+'.'
            if x.get('decision'): evidence+=' Decision: '+x['decision']
            changes.append('| '+ ' | '.join([md(x['id']+' / '+x['location']),code(x.get('C','')),code(x.get('H','')) if scan!=30 else 'No H text',code(x['reading']),md(evidence),x['confidence']])+' |')
        if x.get('diff_H'):
            assert scan !=30
            collation.append({'folder':'J75-04','their_page':scan-1,'our_scan':scan,'line':x['location'],'their_reading':x.get('H',''),'codex_reading':x.get('C',''),'final_reading':x['reading'],'scan_shows':x['evidence']+(' Crop: '+x['crop'] if x.get('crop') else ''),'kind':x['kind'],'marked_in_H':'yes' if x.get('H_marked') else 'no','confidence':x['confidence']})
    retained=[x for x in rec['loci'] if not x.get('diff_C') and not x.get('diff_H')]
    if retained:
        changes += ['', '#### Reviewed loci with the witness reading retained', '']
        for x in retained:
            readinginfo='; '.join(f'{k}: {v}' for k,v in x.get('readers',{}).items())
            changes.append(f"- {x['id']}, {x['location']}: {code(x['reading'])}. {x['evidence']}"+(' Crop: '+x['crop']+'.' if x.get('crop') else '')+(' Readers: '+readinginfo+'.' if readinginfo else ''))
    changes += ['', '#### Still unresolved', '']
    uns=rec.get('doubts',[])
    if uns:
        for x in uns:
            changes.append(f"- {x['location']}: {code(x['reading'])}; alternatives {code(x.get('alternatives',''))}; {x['confidence']} confidence. {x.get('reason','')}")
            doubt_rows.append({'scan':scan,**x})
    else: changes.append('None.')
    changes.append('')
    inventory.extend(rec['inventory'])
    checks.extend(rec.get('check_events',[]))
    abbrevs.extend(rec.get('abbreviations',[]))
    notes += [f'## Scan {scan:03}', '', rec['notes'].strip(), '']

(ROOT/'SP39_CW_75_changes.md').write_text('\n'.join(changes)+'\n')
(ROOT/'SP39_CW_75_notes.md').write_text('\n'.join(notes)+'\n')

def write_table(name, rows, fields, delimiter):
    with (ROOT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore')
        w.writeheader();w.writerows(rows)

write_table('SP39_CW_75_collation.tsv',collation,['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],'\t')
write_table('SP39_CW_75_inventory.csv',inventory,['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],',')
write_table('CHECK_EVENTS.tsv',checks,['statement_id','date','who','type','outcome'],'\t')

doubts=[(ROOT/'notation.md').read_text().rstrip(),'','## Remaining doubts','','| Scan | Place | Reading | Alternatives | Confidence | Ink and context |','|---|---|---|---|---|---|']
for x in doubt_rows:
    doubts.append('| '+' | '.join([str(x['scan']),md(x['location']),code(x['reading']),code(x.get('alternatives','')),x['confidence'],md(x.get('reason',''))])+' |')
doubts += ['','## Abbreviations met','','Expansions in this list are interpretations only; none is substituted into the transcription.','','| Abbreviation | Possible expansion | Scans |','|---|---|---|']
merged={}
for a in abbrevs:
    key=(a['abbr'],a['expansion'])
    merged.setdefault(key,set()).update(a.get('scans',[]))
for (a,e),sc in sorted(merged.items()):
    doubts.append('| '+code(a)+' | '+md(e)+' | '+', '.join(map(str,sorted(sc)))+' |')
doubts += ['','## Legibility and witness comparison','']
lp=ROOT/'legibility.md'
doubts.append(lp.read_text().strip() if lp.exists() else 'Assessment will be completed after the final page.')
(ROOT/'SP39_CW_75_doubts.md').write_text('\n'.join(doubts)+'\n')
print(json.dumps({'pages':[r['scan'] for r in records],'counts':dict(total),'collation_rows':len(collation),'inventory_rows':len(inventory),'remaining_doubt_rows':len(doubt_rows),'check_events':len(checks)},ensure_ascii=False))
