"""Assemble the human-reviewed transcription records; never reads image pixels."""
from pathlib import Path
from datetime import datetime,timezone
import csv,json,re,hashlib,argparse
ROOT=Path(__file__).resolve().parents[1]
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def cell(v):return str(v if v is not None else '').replace('|','\\|').replace('\n','<br>')
def write_tsv(path,fields,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def render():
    records=[json.loads(p.read_text()) for p in sorted((ROOT/'records').glob('scan*.json'))]
    changes=['# SP38_CW_75 — changes and decisions','', 'Counts are distinct adjudicated loci, not changed tokens. A locus may differ from both witnesses. C changes include added, resolved or reordered doubt marks; these editorial updates are not all transcription errors. Unchanged retained C doubts and witness-S checks are listed but not counted as changes. H macro-only differences, confidence-only changes with the same reading, editorial page markers and the untranscribed cover are excluded. Confidence totals count each changed locus once.','', '| Scan | Changes vs C | Changes vs H | High | Medium | Low |','| --- | ---: | ---: | ---: | ---: | ---: |']
    totals=[0]*5;consequential=[];collation=[];inventory=[];doubts=[];notes=['# SP38_CW_75 — notes while reading','', 'These notes describe only the supplied pages. Reading a statement is not a proof check. Mathematical checks are identified explicitly in CHECK_EVENTS.tsv; manuscript slips are preserved in the transcription.',''];events=[]
    for rec in records:
        fs=rec['findings']; counted=[x for x in fs if x.get('diff_c') or x.get('diff_h')]
        counts=[sum(bool(x.get('diff_c')) for x in fs),sum(bool(x.get('diff_h')) for x in fs)]+[sum(x.get('confidence')==c for x in counted) for c in ['high','medium','low']]
        totals=[a+b for a,b in zip(totals,counts)]
        changes.append('| '+str(rec['scan'])+' | '+' | '.join(map(str,counts))+' |')
        for x in fs:
            if x.get('consequential'):consequential.append(f"- Scan {rec['scan']}, {x['place']}: {x.get('math_note') or x['final']}")
    changes+=['| **Total** | '+' | '.join(map(str,totals))+' |','','## Consequential corrections','']+(consequential or ['None recorded so far.'])
    for rec in records:
        n=rec['scan']; changes+=['',f'## Scan {n:03d}','',f"Three independent readers: {', '.join(rec['readers'])}. Main decision: {rec['decided_utc']}.",'','| ID / place | C | H | Consolidated reading | Scan evidence / crop | Readers and decision | Confidence |','| --- | --- | --- | --- | --- | --- | --- |']
        for x in rec['findings']:
            ev=x.get('evidence','')
            if x.get('crop'):ev+='; crop: `'+x['crop']+'`'
            if x.get('s_id'):ev+='; S: '+x['s_id']+' — '+x.get('s_decision','')
            rds=x.get('readers','See the three independent readings and reports in readings/.')
            if isinstance(rds,dict):rds='; '.join(k+': '+str(v) for k,v in rds.items())
            if x.get('decision'):rds+='; main: '+x['decision']
            row=[x['id']+' / '+x['place'],x.get('c',''),x.get('h',''),x['final'],ev,rds,x['confidence']]
            changes.append('| '+' | '.join(cell(v) for v in row)+' |')
            if x.get('diff_h') and rec.get('hua_has')=='text':
                collation.append(dict(folder=rec['folder'],their_page=n-1,our_scan=n,line=x['place'],their_reading=x.get('h',''),codex_reading=x.get('c',''),final_reading=x['final'],scan_shows=ev,kind=x['kind'],marked_in_H=x.get('marked_in_H','no'),confidence=x['confidence']))
        changes+=['','### Unresolved','']
        if rec.get('unresolved'):
            for u in rec['unresolved']:
                changes.append('- '+u['place']+': '+u['reading']+'; alternatives: '+u.get('alternatives','')+' ('+u['confidence']+').')
                doubts.append(dict(scan=n,**u))
        else:changes.append('None.')
        for x in rec['inventory']:inventory.append(dict(scan=n,**x))
        notes+=['',f'## Scan {n:03d}','',rec.get('notes','')]
        events+=rec.get('events',[])
    (ROOT/'SP38_CW_75_changes.md').write_text('\n'.join(changes)+'\n')
    (ROOT/'SP38_CW_75_notes.md').write_text('\n'.join(notes)+'\n')
    write_tsv(ROOT/'SP38_CW_75_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    write_tsv(ROOT/'SP38_CW_75_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    for pp in sorted((ROOT/'pending_events').glob('scan*.json')):
        if not (ROOT/'records'/pp.name).exists():events+=json.loads(pp.read_text())
    write_tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    nt=(ROOT/'briefs/notation_current.md').read_text() if (ROOT/'briefs/notation_current.md').exists() else (ROOT/'briefs/notation_initial.md').read_text()
    dt=[nt.rstrip(),'','## Remaining doubts','','| Scan | Place | Reading | Alternatives | Confidence |','| --- | --- | --- | --- | --- |']
    for d in doubts:dt.append('| '+' | '.join(cell(d.get(k,'')) for k in ['scan','place','reading','alternatives','confidence'])+' |')
    if not doubts:dt.append('| — | None recorded so far | | | |')
    dt+=['','## Abbreviations (expansions here only)','','| Written | Suggested expansion | Scans |','| --- | --- | --- |']
    ab={}
    for rec in records:
        for a in rec.get('abbreviations',[]):
            key=(a['written'],a['expansion']);ab.setdefault(key,[]).append(str(rec['scan']))
    for (w,e),ns in ab.items():dt.append('| '+cell(w)+' | '+cell(e)+' | '+', '.join(dict.fromkeys(ns))+' |')
    assess=ROOT/'briefs/legibility.md'
    dt+=['','## Legibility and witness comparison','',assess.read_text().strip() if assess.exists() else 'Assessment in progress; reader reports preserve the evidence and uncertainty for each completed page.']
    irregular=ROOT/'briefs/written_irregularities.md'
    if irregular.exists():dt+=['',irregular.read_text().rstrip()]
    (ROOT/'SP38_CW_75_doubts.md').write_text('\n'.join(dt)+'\n')
    pages=sorted((ROOT/'pages').glob('*.tex'),key=lambda p:int(re.search(r'scan(\d+)',p.name).group(1)))
    (ROOT/'SP38_CW_75_transcription.tex').write_text('\n\n'.join(p.read_text().rstrip() for p in pages)+'\n')
    wf=['# SP38_CW_75 — workflow','', 'Each scan was assigned to three fresh subagents using fork_turns=none, with no access in their instructions to other readers or previous page images. Pages were assigned sequentially, after the previous page was adjudicated and committed. The main reader retained returns and viewed adjudication crops. All reader returns, crop metadata, decisions, brief versions, and scripts are included. No OCR or external research was used.','', 'Runtime model label: GPT-6 Astra Pro; reader effort inherited and not independently exposed by the tool. No unsupported effort level is asserted.','', '## Brief versions','']
    history=ROOT/'briefs/history.json'
    for h in json.loads(history.read_text()) if history.exists() else []:wf.append(f"- Scan {h['scan']:03d}: {h['file']} — {h['reason']}")
    wf+=['','## Crop counts','','R1/R2/R3 counts are the crops each reader made and inspected. Main-created counts only new adjudication crops; main-inspected also includes reused reader crops. Original supplied page/halves are excluded. A shared crop may settle several neighboring details in one locus.','','| Scan | R1 | R2 | R3 | Main-created | Main-inspected |','| --- | ---: | ---: | ---: | ---: | ---: |']
    for rec in records:wf.append('| '+str(rec['scan'])+' | '+' | '.join(str(rec['crop_counts'].get(r,0)) for r in ['R1','R2','R3','main'])+' | '+str(len(rec.get('main_crop_views',[])))+' |')
    for title,path in [('First brief','brief_v01_scan002.md'),('Last brief',json.loads(history.read_text())[-1]['file'] if history.exists() else 'brief_v01_scan002.md')]:
        wf+=['',f'## {title}','',(ROOT/'briefs'/path).read_text()]
    lessons=ROOT/'briefs/lessons.md'
    wf+=['','## What worked and what did not','',lessons.read_text() if lessons.exists() else 'Recorded after each completed page in the decision records; final synthesis pending.']
    (ROOT/'SP38_CW_75_workflow.md').write_text('\n'.join(wf)+'\n')
    return len(records)

def commit(n):
    dp=ROOT/'decisions'/f'scan{n:03d}.json';dec=json.loads(dp.read_text())
    packets=ROOT.parent/'packets'/f'scan{n:03d}';meta=json.loads((packets/'metadata.json').read_text())
    reports={r:json.loads((ROOT/'readings'/f'scan{n:03d}'/r/'report.json').read_text()) for r in ['R1','R2','R3']}
    text=(ROOT/'readings'/f'scan{n:03d}'/dec['base']/'reading.tex').read_text()
    if 'text_file' in dec:text=(ROOT/dec['text_file']).read_text()
    for rep in dec.get('replacements',[]):
        count=text.count(rep['old'])
        if count!=rep.get('count',1):raise ValueError(f"Replacement match count {count}: {rep['old']}")
        text=text.replace(rep['old'],rep['new'])
    if n!=2:text=re.sub(r'\\cotefile\{75\}\s*','',text)
    target=ROOT/'pages'/Path(meta['codex_file']).name
    target.write_text(text.rstrip()+'\n')
    fs=[]
    for item in dec.get('take',[]):
        r=item['reader'];fid=item['id'];match=[x for x in reports[r]['findings'] if x['id']==fid]
        if len(match)!=1:raise ValueError((r,fid,len(match)))
        f=dict(match[0]);f.update(item.get('override',{}));fs.append(f)
    fs+=dec.get('findings',[])
    for i,f in enumerate(fs):
        f['id']=f"S{n:03d}-{i+1:03d}"
        if isinstance(f.get('marked_in_H'),bool):f['marked_in_H']='yes' if f['marked_in_H'] else 'no'
        if f.get('kind','').startswith('readable ink left as'):f['kind']=r'readable ink left as \ill{}'
    rec={k:v for k,v in meta.items() if k not in ['images','codex_file','hua_file','context']}
    rec.update(scan=n,readers=['R1','R2','R3'],decided_utc=now(),findings=fs,inventory=dec.get('inventory',reports[dec.get('inventory_from',dec['base'])]['inventory']),notes=dec['notes'],events=dec.get('events',[]),unresolved=dec.get('unresolved',[]),abbreviations=dec.get('abbreviations',reports[dec['base']].get('abbreviations',[])),crop_counts={r:reports[r]['crop_count'] for r in reports})
    rec['crop_counts']['main']=dec.get('main_crop_count',0)
    rec['main_crop_views']=dec.get('main_crop_views',[])
    (ROOT/'records'/f'scan{n:03d}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    render()
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03d} done {rec["decided_utc"]}\n')
    print(json.dumps({'scan':n,'page':str(target),'findings':len(fs),'time':rec['decided_utc']},ensure_ascii=False))

if __name__=='__main__':
    p=argparse.ArgumentParser();p.add_argument('action',choices=['render','commit']);p.add_argument('scan',nargs='?',type=int);a=p.parse_args()
    if a.action=='commit':commit(a.scan)
    else:print({'pages':render()})
