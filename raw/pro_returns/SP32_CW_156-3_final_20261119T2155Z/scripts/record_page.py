#!/usr/bin/env python3
"""Write human/model-entered ink decisions and regenerate the collation apparatus.
No OCR, image analysis, inferred transcription, or automatic reading decisions.
"""
from pathlib import Path
import csv, json, datetime, collections
ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP32_CW_156-3'
def utc(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def change(place,c,h,final,evidence,kind='other',cd=True,hd=True,marked=False,confidence='high',status='decision'):
    return dict(place=place,c=c,h=h,final=final,evidence=evidence,kind=kind,c_diff=cd,h_diff=hd,marked=marked,confidence=confidence,status=status)
def md(s): return str(s).replace('|','\\|').replace('\n','<br>')
def rebuild():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan[0-9][0-9][0-9].json'))]
    rows=[]; inv=[]; counts=[]; allchanges=[]
    text=['# Changes and decisions','', 'Counts treat one localized apparatus row as one place. Resolution or introduction of a doubt mark counts as a change against that witness; macro spelling alone does not. Retained doubts and witness-S confirmations are separately recorded and do not inflate change counts. A row can differ from both witnesses. Locations follow the manuscript text, not typeset output line breaks. These are editorial place counts, not word-error rates. A repeated alphabet decision may be recorded once for its page, as identified in that row.','', '| Scan | Against C | C high / medium / low | Against H | H high / medium / low | All distinct changed places: high / medium / low |','|---|---:|---|---:|---|---|']
    for r in records:
        active=[x for x in r['changes'] if x['c_diff'] or x['h_diff']]
        c=sum(x['c_diff'] for x in active); h=sum(x['h_diff'] for x in active)
        q=collections.Counter(x['confidence'] for x in active)
        cq=collections.Counter(x['confidence'] for x in active if x['c_diff'])
        hq=collections.Counter(x['confidence'] for x in active if x['h_diff'])
        text.append(f"| {r['scan']:03} | {c} | {cq['high']} / {cq['medium']} / {cq['low']} | {h} | {hq['high']} / {hq['medium']} / {hq['low']} | {q['high']} / {q['medium']} / {q['low']} |")
        counts.append((c,h,q)); allchanges.extend(active)
    qc=collections.Counter(x['confidence'] for x in allchanges)
    cq=collections.Counter(x['confidence'] for x in allchanges if x['c_diff'])
    hq=collections.Counter(x['confidence'] for x in allchanges if x['h_diff'])
    text.append(f"| **Total** | **{sum(c for c,h,q in counts)}** | **{cq['high']} / {cq['medium']} / {cq['low']}** | **{sum(h for c,h,q in counts)}** | **{hq['high']} / {hq['medium']} / {hq['low']}** | **{qc['high']} / {qc['medium']} / {qc['low']}** |")
    witness_s=ROOT/'records/witness_s_disposition.md'
    if witness_s.exists():text+=['',witness_s.read_text()]
    text+=['','## Consequential readings','']
    for r in records:
        for s in r.get('consequential',[]): text.append(f"- Scan {r['scan']:03}: {s}")
    for r in records:
        n=r['scan']; folder='J156-3-04' if n<=33 else 'J156-3-05'
        text += ['',f'## Scan {n:03} — manuscript page {n-1}','', '| Place | C | H | Consolidated | Ink / crop evidence | Confidence |','|---|---|---|---|---|---|']
        for x in r['changes']:
            text.append('| '+' | '.join(md(x[k]) for k in ('place','c','h','final','evidence','confidence'))+' |')
            if x['h_diff']:
                rows.append([folder,n-1,n,x['place'],x['h'],x['c'],x['final'],x['evidence'],x['kind'],'yes' if x['marked'] else 'no',x['confidence']])
        text+=['','### Unresolved places','']
        if r.get('doubts'):
            for d in r['doubts']: text.append('- '+md(d[0])+': '+md(d[1])+'; alternatives: '+md(d[2])+'. '+md(d[4]))
        else:text.append('None remaining after this pass.')
        for i,(kind,pos,words) in enumerate(r['inventory'],1):
            inv.append([n,'text','Grothendieck (his hand)',f'{n:03}-{i:02}',kind,pos,words,'yes'])
    (ROOT/(PREFIX+'_changes.md')).write_text('\n'.join(text)+'\n')
    with (ROOT/(PREFIX+'_collation.tsv')).open('w',newline='') as f:
        w=csv.writer(f,delimiter='\t');w.writerow('folder their_page our_scan line their_reading codex_reading final_reading scan_shows kind marked_in_H confidence'.split());w.writerows(rows)
    with (ROOT/(PREFIX+'_inventory.csv')).open('w',newline='') as f:
        w=csv.writer(f);w.writerow('scan sheet_kind hand element kind position first_words_or_objects transcribed'.split());w.writerows(inv)
    notation=json.loads((ROOT/'records/notation.json').read_text()) if (ROOT/'records/notation.json').exists() else []
    doubts=['# Notation table','', '| Sign / usage | Appearance in the ink | Transcription | Scans / qualifications |','|---|---|---|---|']
    doubts+=['| '+' | '.join(md(s) for s in row)+' |' for row in notation]
    doubts+=['','## Remaining doubts','', '| Scan | Place | Reading | Alternatives | Confidence | Ink / contextual qualification |','|---|---|---|---|---|---|']
    for r in records:
        for d in r.get('doubts',[]):doubts.append('| '+str(r['scan'])+' | '+' | '.join(md(x) for x in d)+' |')
    ab=ROOT/'records/abbreviations.json'
    if ab.exists():
        doubts+=['','## Abbreviations (expansions only here)','', '| Written | Likely expansion |','|---|---|']
        doubts+=['| '+' | '.join(md(x) for x in row)+' |' for row in json.loads(ab.read_text())]
    leg=ROOT/'records/legibility.md'
    if leg.exists():doubts+=['','## Legibility and witness comparison','',leg.read_text()]
    (ROOT/(PREFIX+'_doubts.md')).write_text('\n'.join(doubts)+'\n')
    combined='\n'.join((ROOT/'pages'/r['filename']).read_text().rstrip() for r in records)+'\n'
    (ROOT/(PREFIX+'_transcription.tex')).write_text(combined)
def commit(scan,tex,changes,inventory,doubts=(),consequential=(),observations=''):
    folder='J156-3-04' if scan<=33 else 'J156-3-05'
    filename=f'{folder}_156-3_scan{scan:03}.tex'
    (ROOT/'pages'/filename).write_text(tex.strip()+'\n')
    rec=dict(scan=scan,filename=filename,changes=changes,inventory=inventory,doubts=doubts,consequential=consequential,observations=observations)
    (ROOT/'records'/f'scan{scan:03}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    rebuild()
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {scan:03} done {utc()}\n')
    print(f'Saved scan {scan:03}: {len(changes)} decisions; {len(inventory)} inventory elements.')
if __name__=='__main__': rebuild()
