#!/usr/bin/env python3
"""Build the delivered records from the main reader's page decisions.

This script does no OCR and makes no reading decisions. It formats recorded
human-readable decisions and performs mechanical coverage / syntax checks.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, sys, zipfile

ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP45_CW_37'
KINDS={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised',r'readable ink left as \ill{}','drawing or diagram','other'}

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def readj(p): return json.loads(Path(p).read_text())
def md(s): return str(s).replace('|',r'\|').replace('\n','<br>')
def table(head,rows):
    return '| '+' | '.join(head)+' |\n| '+' | '.join('---' for _ in head)+' |\n'+''.join('| '+' | '.join(md(x) for x in row)+' |\n' for row in rows)
def report(n,r): return readj(ROOT/f'readers/scan{n:03d}/{r}/report.json')
def decisions(): return [readj(p) for p in sorted((ROOT/'decisions').glob('scan*.json')) if re.fullmatch(r'scan\d{3}\.json',p.name)]

def build():
    ds=decisions(); states=readj(ROOT/'run_state.json')
    order=states['scan_order']; byscan={int(d['scan']):d for d in ds}
    ds=[byscan[n] for n in order if n in byscan]
    totals={'C':0,'H':0,'high':0,'medium':0,'low':0}; summary=[]; consequential=[]
    changebody=[]; collation=[]; inventory=[]; notes=[]; events=[]; doubts=[]; abbr={}; notation=[]; workflow=[]
    for d in ds:
        n=int(d['scan']); counts={'C':0,'H':0,'high':0,'medium':0,'low':0}
        rows=[]
        for i,c in enumerate(d.get('changes',[]),1):
            if not (c.get('diff_c') or c.get('diff_h')): continue
            assert c['confidence'] in ('high','medium','low'),(n,c)
            counts['C']+=bool(c.get('diff_c')); counts['H']+=bool(c.get('diff_h')); counts[c['confidence']]+=1
            rid=f's{n:03d}-change{i:02d}'
            ev=c['evidence']
            if c.get('crop'):ev+=' Crop: '+c['crop']
            readers=c.get('readers',{})
            rr='; '.join(f'{k}: {v}' for k,v in readers.items()) or 'See the three retained reader reports.'
            rows.append([rid+' — '+c['locus'],c['c'],c['h'],c['reading'],rr,ev,c['confidence']])
            if c.get('mathematical_consequence'):consequential.append(f'- Scan {n}, {c["locus"]}: {c["mathematical_consequence"]}')
            if c.get('diff_h'):
                assert d['hua_has']=='text',(n,'H rows on description-only page')
                assert c['kind'] in KINDS,(n,c['kind'])
                collation.append([d['folder'],d['their_page'],n,c['locus'],c['h'],c['c'],c['reading'],ev,c['kind'],'yes' if c.get('marked_in_H') else 'no',c['confidence']])
        for k in totals:totals[k]+=counts[k]
        summary.append([n,counts['C'],counts['H'],counts['high'],counts['medium'],counts['low']])
        b=f'## Scan {n:03d}\n\nH status: {d["hua_has"]}. Main-reader decision: {d["decided_utc"]}.\n\n'
        b+=table(['Place / decision id','C','H','Consolidated reading','Independent readings','What the scan shows','Confidence'],rows) if rows else 'No substantive reading differs from either textual witness.\n'
        if d.get('adjudications'):
            b+='\n### Other reader disagreements (not counted as witness changes)\n\n'
            b+=table(['Place','Reader 1','Reader 2','Reader 3','Decision','Ink evidence'],[[a['locus'],a['readers']['r1'],a['readers']['r2'],a['readers']['r3'],a['reading'],a['evidence']+(' Crop: '+a['crop'] if a.get('crop') else '')] for a in d['adjudications']])
        b+='\n### C doubt decisions\n\n'
        cr=[[x['locus'],x['c'],x['decision'],x['reading'],x['evidence']+((' Crop: '+x['crop']) if x.get('crop') else '')] for x in d.get('c_doubts',[])]
        b+=table(['Place','C doubt','Decision','Reading','Ink evidence'],cr) if cr else 'C carries no doubt mark on this page.\n'
        b+='\n### Remaining doubts\n\n'
        ur=[[n,x['locus'],x['reading'],'; '.join(x.get('alternatives',[])),x['confidence'],x.get('reason','')] for x in d.get('unresolved',[])]
        doubts.extend(ur)
        b+=table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],ur) if ur else 'None.\n'
        if d.get('adjudication_note'): b+='\n'+d['adjudication_note']+'\n'
        changebody.append(b)
        for x in d.get('inventory',[]):
            assert x['transcribed']=='yes',(n,x)
            assert x['kind'] in {'text','display','diagram','drawing','margin note','insertion','deletion'},(n,x['kind'])
            inventory.append([n]+[x[k] for k in ['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']])
        note=f'## Scan {n:03d}\n\n'
        for x in d.get('notes',[]): note+=f'**{x["id"]}.** {x["text"]}\n\nSource: {x["basis"]}.\n\n'
        notes.append(note)
        events+=d.get('check_events',[])
        for x in d.get('notation',[]):notation.append([x['sign'],x['latex'],f'Scan {n}: '+x['locus'],x.get('evidence','')+' '+x.get('alternatives','')])
        for x in d.get('abbreviations',[]):abbr.setdefault(x['form'],set()).add(x['expansion'])
        workflow.append([n,d['brief_version'],*d['reader_crop_counts'],d.get('main_crop_count',0),d.get('workflow_observation','')])
    summary.append(['TOTAL',totals['C'],totals['H'],totals['high'],totals['medium'],totals['low']])
    intro='# Changes against witnesses C and H\n\nCounts are distinct recorded loci, not word-error rates. A locus can differ from both witnesses and then contributes to both C and H columns. Confidence columns count each locus once. Purely equivalent macro syntax is excluded. H description-only pages have no H collation rows. C doubt marks resolved or changed count against C; retained doubts are separately recorded.\n\n'
    intro+=table(['Scan','Against C','Against H','High','Medium','Low'],summary)
    intro+='\n## Consequential corrections\n\n'+ ('\n'.join(consequential) if consequential else 'None recorded so far.')+'\n\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(intro+'\n'.join(changebody))
    with (ROOT/f'{PREFIX}_collation.tsv').open('w',newline='') as f:
        wr=csv.writer(f,delimiter='\t');wr.writerow(['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence']);wr.writerows(collation)
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        wr=csv.writer(f);wr.writerow(['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed']);wr.writerows(inventory)
    nt='# Notation table\n\nEntries are observations at specified page loci, not rules for filling unseen ink. Each new reader receives the entries already decided; source shapes remain authoritative.\n\n'+table(['Observed notation','LaTeX','Evidence location','Ink / alternatives'],notation)
    (ROOT/'notation.md').write_text(nt)
    doubttext=nt+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations\n\nExpansions here are interpretive aids and are never substituted into the transcription.\n\n'+table(['As written','Possible expansion'],[[k,'; '.join(sorted(v))] for k,v in sorted(abbr.items())])
    if (ROOT/'legibility_note.md').exists():doubttext+='\n## Legibility and witness comparison\n\n'+(ROOT/'legibility_note.md').read_text()
    (ROOT/f'{PREFIX}_doubts.md').write_text(doubttext)
    (ROOT/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nOnly the supplied pages are used. These notes describe what the pages say; an exercise or assertion is not treated as proved merely because it was transcribed. Mathematical checks, where actually performed, are identified separately in CHECK_EVENTS.tsv.\n\n'+'\n'.join(notes))
    with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        wr=csv.writer(f,delimiter='\t');wr.writerow(['statement_id','date','who','type','outcome'])
        for e in events:wr.writerow([e[k] for k in ['statement_id','date','who','type','outcome']])
    combined='\n'.join((ROOT/'pages'/d['filename']).read_text().rstrip()+'\n' for d in ds)
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
    first=(ROOT/'briefs/reader_brief_v001.md').read_text()
    last=(ROOT/'briefs'/f'reader_brief_{ds[-1]["brief_version"]}.md').read_text() if ds else first
    wf='# Workflow record\n\nEvery scan is assigned in order to three new, independent readers. Each receives only that page’s scan images, C and H text (or H description), C’s page-specific questions and inventory, the conventions, and the current notation snapshot. Their complete readings, reports, and crops are retained under readers/. Main-reader decisions and all three readings are recorded under decisions/ and in the changes log. The main reader reviews crops for disagreements and writes the page and records before starting the next scan.\n\n## Crop counts\n\n'+table(['Scan','Brief','Reader 1','Reader 2','Reader 3','Main new crops','Workflow observations'],workflow)
    wf+='\n## Brief revision history\n\n'+((ROOT/'briefs/revisions.md').read_text() if (ROOT/'briefs/revisions.md').exists() else 'No revisions yet.\n')
    wf+='\n## First brief\n\n'+first+'\n## Last brief used\n\n'+last
    if (ROOT/'workflow_assessment.md').exists():wf+='\n## Assessment\n\n'+(ROOT/'workflow_assessment.md').read_text()
    (ROOT/f'{PREFIX}_workflow.md').write_text(wf)
    states['completed_scans']=[int(d['scan']) for d in ds];(ROOT/'run_state.json').write_text(json.dumps(states,indent=2)+'\n')
    print(json.dumps({'pages':len(ds),'changes':totals,'H_collation_rows':len(collation),'inventory_rows':len(inventory),'remaining_doubts':len(doubts),'check_events':len(events)},ensure_ascii=False))

def compare(n):
    import difflib
    rs=[]
    for r in ['r1','r2','r3']:
        p=ROOT/f'readers/scan{n:03d}/{r}'; rep=readj(p/'report.json'); tex=(p/'reading.tex').read_text();rs.append(tex)
        print('\nREADER',r,'CHANGES',len(rep.get('changes',[])),'CROPS',len(rep.get('crops',[])))
        print(json.dumps({k:rep.get(k) for k in ['coverage','changes','c_doubts','unresolved','notes','brief_feedback']},ensure_ascii=False,indent=2))
    for i in [1,2]:
        print('\nTEX DIFF r1 / r'+str(i+1));print(''.join(difflib.unified_diff(rs[0].splitlines(True),rs[i].splitlines(True),fromfile='r1',tofile='r'+str(i+1))))

def checkpoint():
    state=readj(ROOT/'run_state.json')
    if state.get('pending_checkpoint'):
        print(json.dumps({'pending':state['pending_checkpoint']}));return
    last=datetime.strptime(state['last_checkpoint_utc'],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    elapsed=(datetime.now(timezone.utc)-last).total_seconds()
    if elapsed<state['checkpoint_interval_seconds']:
        print(json.dumps({'due':False,'seconds_until_due':int(state['checkpoint_interval_seconds']-elapsed)}));return
    n=state['checkpoint_number']+1;name=f'{PREFIX}_checkpoint_{n:02d}.zip';p=ROOT.parent/name;now=utc()
    assert not p.exists(),p
    with (ROOT/'progress.log').open('a') as f:f.write(f'checkpoint {n:02d} snapshot {now}\n')
    state.update(checkpoint_number=n,last_checkpoint_utc=now,pending_checkpoint=str(p));(ROOT/'run_state.json').write_text(json.dumps(state,indent=2)+'\n')
    files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
    (ROOT/'checkpoint_file_list.txt').write_text('\n'.join(str(p.relative_to(ROOT)) for p in files)+'\n')
    files=sorted(p for p in ROOT.rglob('*') if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts)
    with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for f in files:z.write(f,f.relative_to(ROOT))
    print(json.dumps({'due':True,'path':str(p),'size':p.stat().st_size,'number':n,'completed_scans':state['completed_scans']}))

def balance():
    results=[]
    for p in sorted((ROOT/'pages').glob('*.tex')):
        s=p.read_text();s=re.sub(r'(?<!\\)%[^\n]*','',s);err=[];stack=[]
        for m in re.finditer(r'(?<!\\)[{}]',s):
            if m.group()=='{':stack.append(m.start())
            elif stack:stack.pop()
            else:err.append('unmatched closing brace at '+str(m.start()))
        if stack:err.append('unclosed braces '+str(stack))
        env=[]
        for m in re.finditer(r'\\(begin|end)\{([^}]+)\}',s):
            if m[1]=='begin':env.append(m[2])
            elif env and env[-1]==m[2]:env.pop()
            else:err.append('environment mismatch '+m[0])
        if env:err.append('open environments '+str(env))
        for a,b in [(r'\[',r'\]'),(r'\(',r'\)')]:
            if s.count(a)!=s.count(b):err.append(a+' '+b+' counts differ')
        if len(re.findall(r'(?<!\\)\$',s))%2:err.append('odd dollar count')
        results.append({'file':p.name,'errors':err})
    (ROOT/'syntax_check.json').write_text(json.dumps(results,indent=2)+'\n');print(json.dumps(results,indent=2))

if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='build':build()
    elif cmd=='compare':compare(int(sys.argv[2]))
    elif cmd=='checkpoint':checkpoint()
    elif cmd=='balance':balance()
    else:raise SystemExit('Unknown command')
