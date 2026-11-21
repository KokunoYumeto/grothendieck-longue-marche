from pathlib import Path
import csv,json,re,sys,collections
from datetime import datetime,timezone
ROOT=Path('/workspace/scratch/b8c6ff258063')
OUT=ROOT/'SP87_C13_149_work'
SRC=ROOT/'source'
PREFIX='SP87_C13_149'
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def write_csv(name,fields,rows,delimiter='\t'):
    with (OUT/name).open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def md(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def code(s):return '`'+md(s).replace('`','&#96;')+'`'
def load_reports():
    return [json.loads(p.read_text()) for p in sorted((OUT/'review').glob('149_scan*_reviewed.json'))]
def rebuild():
    reports=load_reports();changes=[];marks=[];inventory=[];events=[];notes=[];unresolved=[];hands=[];abbr={};notation=[]
    table=['# Changes against witnesses C and H','', 'Counts are places, not changed tokens. One place can differ from both witnesses; high/medium/low count the rows once. Macro-only differences and certainty-only additions are excluded.','', '| Scan | Against C | Against H | High | Medium | Low | Rows |','|---|---:|---:|---:|---:|---:|---:|']
    totals=collections.Counter();conseq=[]
    body=[]
    for r in reports:
        s=r['scan'];cs=r['changes'];cnt=collections.Counter(c['confidence'] for c in cs);ac=sum(c['against_c'] for c in cs);ah=sum(c['against_h'] for c in cs)
        table.append(f'| {s:03d} | {ac} | {ah} | {cnt["high"]} | {cnt["medium"]} | {cnt["low"]} | {len(cs)} |')
        totals.update({'C':ac,'H':ah,'rows':len(cs),**cnt})
        body += [f'## Scan {s:03d}','', '| Place | Witness C | Witness H | Final reading | Ink evidence and image | Confidence |','|---|---|---|---|---|---|']
        for c in cs:
            evidence=c['evidence'];crop=c.get('crop');box=c.get('box')
            if crop:evidence+=f' Crop: {crop}; original box {tuple(box) if box else "see crop register"}.'
            body.append('| '+' | '.join([md(c['place']),code(c['c']),code(c['h']),code(c['final']),md(evidence),c['confidence']])+' |')
            c=dict(c,scan=s);changes.append(c)
            if c.get('consequential'):conseq.append(f'- Scan {s:03d}, {c["place"]}: {code(c["final"])}. {c["evidence"]}')
        body+=['','### Decisions on the supplied marks of witness C','','These decisions are counted in decisions.tsv separately from the substantive difference rows above. Resolving a first reading changes its certainty without adding a lexical collation difference.','','| Mark | Decision | Final reading | Ink evidence and crop | Confidence |','|---|---|---|---|---|']
        for m in r['marks']:
            evidence=m['evidence']
            if m.get('crop'):evidence+=f' Crop: {m["crop"]}; original box {m.get("box")}.'
            body.append('| '+' | '.join([m['id'],m['decision'],code(m['reading']),md(evidence),m['confidence']])+' |')
        body+=['','### Unresolved places','']
        if r.get('unresolved'):
            for u in r['unresolved']:
                body.append(f'- {u["place"]}: {code(u["reading"])}; alternatives: {code(u.get("alternatives",""))}; confidence {u["confidence"]}.')
                unresolved.append(dict(u,scan=s))
        else:body.append('No remaining reading doubt identified on this page.')
        body+=['']
        auditpath=OUT/'second'/f'149_scan{s:03d}_adjudications.tsv'
        if auditpath.exists():
            audited=list(csv.DictReader(auditpath.open(),delimiter='\t'))
            changed=[a for a in audited if a.get('changed')=='yes']
            body+=['### Changes after the blind second reading','']
            if changed:
                body+=['| Box | Frozen first reading | Blind second reading | Final reading | Decision and crop evidence |','|---|---|---|---|---|']
                for a in changed:
                    body.append('| '+' | '.join([a['box'],code(a['first']),code(a['second']),code(a['final']),md(a['evidence']+' ['+a['crop']+']')])+' |')
            else:body+=['No transcription change was required by the blind comparison. All token differences, including equivalent macro forms and box-scope differences, are adjudicated in second/.']
            body+=['']
        for m in r['marks']:marks.append(dict(m,scan=s,cote='149'))
        inventory.extend(dict(x,scan=f'{s:03d}') for x in r['inventory'])
        for e in r.get('check_events',[]):events.append(dict(e,date=now().split(' ')[0],who=e.get('who','GPT-6 Astra Pro; inherited effort not exposed; SP87 main reader')))
        notes+=[f'## Scan {s:03d}','',r.get('notes',''), '']
        if auditpath.exists():
            nboxes=sum(1 for _ in csv.DictReader((OUT/'second'/f'149_scan{s:03d}_boxes.tsv').open(),delimiter='\t'))
            notes += [f'Blind second-reading audit: {nboxes} anonymous boxes were read independently by a different first-pass reader. The saved readings produced {len(audited)} token-different boxes; every such difference was adjudicated on its saved image crop, and {len(changed)} boxes led to a transcription or doubt-state change. Both original readings and the explicit decisions remain in second/149_scan{s:03d}_adjudications.tsv and its companion files.','']
        for h in r.get('hand_observations',[]):hands.append(dict(h,scan=s))
        for a in r.get('abbreviations',[]):abbr.setdefault(a['form'],{'expansion':a['expansion'],'scans':[]})['scans'].append(f'{s:03d}')
        notation.extend(dict(x,scan=s) for x in r.get('notation_additions',[]))
    table += [f'| **Total** | **{totals["C"]}** | **{totals["H"]}** | **{totals["high"]}** | **{totals["medium"]}** | **{totals["low"]}** | **{totals["rows"]}** |','','## Consequential corrections','']+(conseq or ['None identified so far.'])+['']
    (OUT/f'{PREFIX}_changes.md').write_text('\n'.join(table+body)+'\n')
    coll=[]
    for c in changes:
        if c['against_h']:
            ev=c['evidence']
            if c.get('crop'):ev+=f' [{c["crop"]}; {c.get("box")}]'
            coll.append(dict(folder='149',their_page=c['scan']-1,our_scan=c['scan'],line=c['place'],their_reading=c['h'],codex_reading=c['c'],final_reading=c['final'],scan_shows=ev,kind=c['kind'],marked_in_H='yes' if c.get('marked_in_h') else 'no',confidence=c['confidence']))
    write_csv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    markorder={x['id']:i for i,x in enumerate(csv.DictReader((SRC/'SP87_C13_149_texts/MARKS.tsv').open(),delimiter='\t'))}
    dec=[]
    for m in sorted(marks,key=lambda x:markorder[x['id']]):
        crop='page' if m['decision']=='undecided' else str(m.get('crop'))+'; scan '+str(m['scan'])+' '+str(m.get('box'))
        dec.append({'id':m['id'],'cote':'149','scan':m['scan'],'decision':m['decision'],'reading':m['reading'],'what the ink shows':m['evidence'],'crop':crop,'confidence':m['confidence']})
    write_csv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],dec)
    write_csv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    write_csv('CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    (OUT/f'{PREFIX}_notes.md').write_text('# Reading notes\n\nCoverage is the 23 supplied leaves 079–098 and 100–102; scan099 was not supplied and has not been reconstructed. These notes describe only those leaves. A reported author claim is not an endorsed theorem. CHECK_EVENTS.tsv distinguishes actual mathematical checks or uses from reading. No material outside these pages was researched. Method statements in each initial reading note describe the first-reading stage; the separate blind-audit paragraph records its later review. The paper watermark identified in the supplied error sheet as EXTRA STRONG, and any show-through, are not transcribed as authorial text.\n\n'+'\n'.join(notes))
    nt=['# Notation table','','| Written form | Transcription | Scan | Evidence |','|---|---|---|---|']
    for n in notation:nt.append('| '+' | '.join([md(n['written']),code(n['transcription']),str(n['scan']),md(n['evidence'])])+' |')
    nt+=['','Double quotation marks are transcribed with two backticks and two apostrophes. Distinct locally visible short forms, accents, terminal points, letter case, and pen slips are preserved. A recurring semantic symbol is kept consistent only after direct comparison; individual missing marks are not supplied.','']
    if (OUT/'review/notation_final.md').exists():nt+=['',(OUT/'review/notation_final.md').read_text(),'']
    (OUT/'notation.md').write_text('\n'.join(nt))
    doubts=nt+['# Remaining doubts','','| Scan | Place | Reading | Alternatives | Confidence |','|---|---|---|---|---|']
    for u in unresolved:doubts.append('| '+' | '.join([str(u['scan']),md(u['place']),code(u['reading']),code(u.get('alternatives','')),u['confidence']])+' |')
    doubts+=['','## Abbreviations encountered','','Expansions below are explanatory only; the transcription retains the manuscript forms.','','| Form | Likely expansion | Scans |','|---|---|---|']
    for a,v in sorted(abbr.items()):doubts.append(f'| {code(a)} | {md(v["expansion"])} | {", ".join(v["scans"])} |')
    if (OUT/'review/legibility.md').exists():doubts+=['','## Legibility and comparison of witnesses','',(OUT/'review/legibility.md').read_text()]
    (OUT/f'{PREFIX}_doubts.md').write_text('\n'.join(doubts)+'\n')
    hand=['# Hand log','','Observations are local to the listed leaves unless explicitly stated. Earlier logs supplied with the archive were background warnings, not evidence for these pages.','','| Scan(s) | Habit or notation | Scope and evidence | Witness errors |','|---|---|---|---|']
    for h in hands:
        hand.append('| '+' | '.join([md(h.get('pages',h['scan'])),md(h['habit']),md(h['evidence']),md(h.get('witness_errors',''))])+' |')
    (OUT/f'{PREFIX}_hand_log.md').write_text('\n'.join(hand)+'\n')
    kindmap={'misread symbol or index':'1. Symbols and indices','misread word':'2. Words','omission':'3. Omissions','drawing or diagram':'4. Drawings and diagrams','readable ink left as \\ill{}':'5. Readable ink left as illegible','insertion or placement':'6. Insertions put in the wrong place','deletion state':'7. Struck text','abbreviation expanded or spelling modernised':'8. Abbreviations expanded, spelling modernised','text not on the page':'9. Text that is not on the page','other':'10. Other'}
    fb=['# Error-sheet feedback','','Counts classify each logged place once by its principal error kind. A place may differ from one or both witnesses; the counts are not error rates for all manuscript tokens.','','| Error-sheet kind | Places | Against C | Against H |','|---|---:|---:|---:|']
    for k,title in kindmap.items():
        xs=[x for x in changes if x['kind']==k]
        fb.append(f'| {title} | {len(xs)} | {sum(x["against_c"] for x in xs)} | {sum(x["against_h"] for x in xs)} |')
    fb+=['','## Recurring local observations','', 'The hand log records local letter, punctuation, abbreviation, and attachment habits.']
    if (OUT/'review/feedback.md').exists():fb+=['',(OUT/'review/feedback.md').read_text()]
    (OUT/f'{PREFIX}_sheet_feedback.md').write_text('\n'.join(fb)+'\n')
    pages=sorted((OUT/'pages').glob('149_scan*.tex'))
    combined='\\cotefile{149}\n\n'+'\n\n'.join(p.read_text().rstrip() for p in pages)+'\n'
    (OUT/f'{PREFIX}_transcription.tex').write_text(combined)
    return {'pages':len(reports),'changes':len(changes),'against_c':totals['C'],'against_h':totals['H'],'marks':len(marks),'inventory':len(inventory)}
def commit(scan):
    page=f'149_scan{scan:03d}'; d=OUT/'readers'/page
    target=OUT/'review'/f'{page}_reviewed.json'
    if not target.exists():raise RuntimeError('Root reviewed report required')
    r=json.loads(target.read_text()); draft=d/'draft.tex'
    for i, b in enumerate(r['second_boxes'],1): b['box']=f'B{i:03d}'
    (OUT/'pages'/f'{page}.tex').write_text(draft.read_text())
    with (OUT/'second'/f'{page}_boxes.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['box','kind','x0','y0','x1','y1'],delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(r['second_boxes'])
    with (OUT/'second'/f'{page}_first.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=['box','reading'],delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(r['second_boxes'])
    info=rebuild()
    count=len(list((OUT/'crops').glob(f'{page}_*.png')))
    with (OUT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} done {now()} cote 149: {r["line_count"]} lines read, {count} places cropped, {len(r["changes"])} rows\n')
    print(info)
if __name__=='__main__':
    if len(sys.argv)>1:commit(int(sys.argv[1]))
    else:print(rebuild())
