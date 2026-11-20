from pathlib import Path
from datetime import datetime,timezone
import csv,json,re,sys,zipfile,hashlib
W=Path(__file__).resolve().parents[1];P='SP77_C13_147'
SCANS=[24,26,29,30,31,32,33,34,35,37,38,39,40,41,42,43,44,45,46,47,48,50,52,53]
def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def table(path,fields,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore');w.writeheader();w.writerows(rows)
def md(x):return str(x).replace('|','\\|').replace('\n','<br>')
def code(x):return '`'+md(x).replace('`','&#96;')+'`'
def load_records():return [json.loads(p.read_text()) for p in sorted((W/'records').glob('*.json')) if (W/'pages'/p.with_suffix('.tex').name).exists()]
def assemble():
    if (W/'transcription_sha256.tsv').exists():raise RuntimeError('Refusing to assemble after the transcription freeze')
    recs=load_records();rows=[(r,c) for r in recs for c in r['changes']]
    changes=['# SP77_C13_147 — changes against the witnesses','','Substantive differences only. Macro syntax is excluded. Certainty-only resolutions appear in decisions.tsv and the doubts file. All readings are model readings of the supplied scans.','','| Scan | Against C | Against H | High | Medium | Low |','| --- | ---: | ---: | ---: | ---: | ---: |'];totals=[0]*5
    for r in recs:
        vals=[sum(bool(c.get(k)) for c in r['changes']) for k in ['diff_C','diff_H']]+[sum(c['confidence']==v for c in r['changes']) for v in ['high','medium','low']]
        totals=[a+b for a,b in zip(totals,vals)];changes.append('| '+str(r['scan']).zfill(3)+' | '+' | '.join(map(str,vals))+' |')
    changes.append('| **Total** | '+' | '.join(map(str,totals))+' |')
    changes+=['','## Consequential corrections','']
    changes+=[f"- Scan {r['scan']:03d}, {c['place']}: {code(c['final'])}. {md(c.get('consequence',c['evidence']))}" for r,c in rows if c.get('consequential')] or ['None labelled consequential at this stage.']
    collation=[];decisions=[];inventory=[];checks=[];abbreviations={}
    notes=['# SP77_C13_147 — notes while reading','','Scope: supplied pages only. Describing the author’s claims is not independent verification. CHECK_EVENTS.tsv distinguishes background use from actual local checks. No external mathematical sources were consulted.','']
    doubts=['# SP77_C13_147 — notation and remaining doubts','','## Notation table','','| Form | Meaning / use | Evidence | Scope |','| --- | --- | --- | --- |']
    hand=['# SP77_C13_147 — hand log','','| Habit | Pages | Scope and exceptions | Misread places |','| --- | --- | --- | --- |']
    for r in recs:
        for n in r['notation']:doubts.append('| '+' | '.join(md(n.get(k,'')) for k in ['form','meaning','evidence','scope'])+' |')
        for h in r['hand_log']:hand.append('| '+' | '.join(md(h.get(k,'')) for k in ['habit','pages','scope','misread_places'])+' |')
        for a in r['abbreviations']:abbreviations.setdefault(a['form'],set()).add(a['expansion'])
        changes+=['',f"## Scan {r['scan']:03d}",'','| Place | Witness C | Witness H | Final reading | What the scan shows; crop and original pixel box | Confidence |','| --- | --- | --- | --- | --- | --- |']
        for c in r['changes']:
            ev=c['evidence']+'; '+c.get('crop','page')+' '+str(c.get('box',''))
            if c.get('audit'):ev+='; blind audit: '+c['audit']
            changes.append('| '+' | '.join([md(c['place']),code(c['C']),code(c['H']),code(c['final']),md(ev),c['confidence']])+' |')
            if c['diff_H']:collation.append(dict(folder='147',their_page=r['scan']-1,our_scan=r['scan'],line=c['place'],their_reading=c['H'],codex_reading=c['C'],final_reading=c['final'],scan_shows=ev,kind=c['kind'],marked_in_H=c.get('marked_in_H','yes' if re.search(r'\\(?:ill|uncertain|unsure|maybe)',c['H']) else 'no'),confidence=c['confidence']))
        changes+=['','**Still unresolved:** '+('; '.join((str(x.get('place',''))+': '+str(x.get('reading',''))) if isinstance(x,dict) else str(x) for x in r.get('unresolved',[])) or 'None reported.'),'']
        if r.get('audit'):
            reconciliation=W/r['audit']['reconciliation']
            with reconciliation.open() as f: audit_rows=list(csv.DictReader(f,delimiter='\t'))
            changed_rows=[x for x in audit_rows if x['changed']=='yes']
            changes += ['### Changes from the blind second reading','',f"{r['audit']['boxes']} boxes read; {r['audit']['differences']} boxes differed token by token; {r['audit']['changed']} consolidated box readings changed. All differences, including markup and clipped-context differences, are decided in {r['audit']['reconciliation']}.",'']
            if changed_rows:
                changes += ['| Box | First reading | Blind reading | Final reading | Ink evidence |','| --- | --- | --- | --- | --- |']
                for a in changed_rows:
                    changes.append('| '+' | '.join([a['box'],code(a['first']),code(a['second']),code(a['final_reading']),md(a['evidence']+'; '+a['crop'])])+' |')
            else: changes += ['No consolidated reading changed.']
        decisions+=r['decisions']+r.get('supplemental_unindexed_C_doubts',[]);inventory+=r['inventory'];checks+=r['check_events'];notes+=[f"## Scan {r['scan']:03d}",'']
        for n in r['notes']:notes+=[f"**{n['id']}.** {n['text']}",'']
        for k,label in [('main_review_note','Main reading'),('audit_note','Blind second reading')]:
            if r.get(k):notes+=['**'+label+'.** '+r[k],'']
    for event in checks:
        event['who']=event['who'].replace('inherited effort','effort not separately exposed')
    final_notation=W/'review'/'notation_final.md'
    if final_notation.exists():doubts=['# SP77_C13_147 — notation and remaining doubts','','## Notation table','',final_notation.read_text().rstrip()]
    notation='\n'.join(doubts)+'\n'
    doubts+=['','## Remaining doubts','','| Scan | Place | Reading | Alternatives | Confidence | Reason |','| --- | --- | --- | --- | --- | --- |']
    for r in recs:
        for d in r['doubts']:doubts.append('| '+str(r['scan']).zfill(3)+' | '+' | '.join(md(d.get(k,'')) for k in ['place','reading','alternatives','confidence','reason'])+' |')
    doubts+=['','## Resolved witness-C marks','','All ordered decisions and crop evidence are in decisions.tsv. Certainty-only resolutions do not inflate the changes count.','','| Scan | Mark | Decision | Reading | Confidence |','| --- | --- | --- | --- | --- |']
    for d in decisions:
        if d['decision']!='undecided':doubts.append('| '+' | '.join(md(d[k]) for k in ['scan','id','decision','reading','confidence'])+' |')
    doubts+=['','## Abbreviations','','| Written form | Proposed expansion (only here) |','| --- | --- |']
    doubts+=['| '+code(k)+' | '+md('; '.join(sorted(v)))+' |' for k,v in sorted(abbreviations.items())]
    doubts+=['','## Legibility and witness comparison','','Main prose is generally readable at native resolution. Crowded insertions, cancellations, tiny exponents and overwritten letters carry the greatest residual risk. The witnesses are correlated AI drafts: agreement is not independent evidence. Confidence concerns local readings, not mathematical truth. Remaining doubtful readings are retained in place.']
    final_legibility=W/'review'/'legibility_final.md'
    if final_legibility.exists():doubts[-1]=final_legibility.read_text().rstrip()
    general_notes=W/'review'/'general_notes_final.md'
    if general_notes.exists():notes[4:4]=[general_notes.read_text().rstrip(),'']
    feedback=['# SP77_C13_147 — error-sheet feedback','','One category per substantive logged place. These counts are not error rates for all words. A place can differ from C, H, or both.','','| Error-sheet category | Places | Against C | Against H |','| --- | ---: | ---: | ---: |']
    cats=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    for cat in cats:
        cs=[c for r,c in rows if c.get('error_category','Other')==cat];feedback.append('| '+cat+' | '+str(len(cs))+' | '+str(sum(bool(c['diff_C']) for c in cs))+' | '+str(sum(bool(c['diff_H']) for c in cs))+' |')
    feedback+=['','## Recurring observations','','The hand log records recurring glyph forms, their scopes and exact witness misreadings. Additional observations:']
    for r in recs:
        for s in r.get('feedback',[]):feedback.append(f"- Scan {r['scan']:03d}: {s}")
    for name,parts in [('changes',changes),('notes',notes),('doubts',doubts),('hand_log',hand),('sheet_feedback',feedback)]: (W/f'{P}_{name}.md').write_text('\n'.join(parts)+'\n')
    (W/'notation.md').write_text(notation)
    table(W/f'{P}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    table(W/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],sorted([d for d in decisions if re.fullmatch(r'M[0-9]+',d['id'])],key=lambda x:int(x['id'][1:])))
    table(W/f'{P}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    table(W/'unindexed_C_doubts.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],[d for d in decisions if not re.fullmatch(r'M[0-9]+',d['id'])])
    table(W/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    (W/f'{P}_transcription.tex').write_text('\\cotefile{147}\n\n'+'\n'.join((W/'pages'/f"147_scan{r['scan']:03d}.tex").read_text().rstrip()+'\n' for r in recs));return recs

def approve(scan):
    if (W/'second'/f'147_scan{scan:03d}_second.tsv').exists():raise RuntimeError('Cannot replace a first reading after the blind reading exists')
    r=json.loads((W/'records'/f'147_scan{scan:03d}.json').read_text())
    if not r.get('main_review'):raise ValueError('Explicit visual main_review required')
    (W/'pages'/f'147_scan{scan:03d}.tex').write_text((W/'drafts'/f'147_scan{scan:03d}.tex').read_text())
    table(W/'second'/f'147_scan{scan:03d}_boxes.tsv',['box','kind','x0','y0','x1','y1'],r['boxes'])
    table(W/'second'/f'147_scan{scan:03d}_first.tsv',['box','reading'],r['boxes']);assemble()
    with (W/'progress.log').open('a') as f:f.write(f"scan {scan:03d} done {now()} cote 147: {r['line_count']} lines read, {len(r['crop_files'])} places cropped, {len(r['changes'])} rows\n")
def tokens(s):return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÖØ-öø-ÿ]+|[0-9]+|[^\s]',s)
def compare(scan):
    import difflib
    base=W/'second'/f'147_scan{scan:03d}'
    def get(s):
        with Path(str(base)+s).open() as f:return {r['box']:r['reading'] for r in csv.DictReader(f,delimiter='\t')}
    a=get('_first.tsv');b=get('_second.tsv')
    if set(a)!=set(b):raise ValueError('Box IDs do not match: '+str(set(a)^set(b)))
    out=[]
    for box in a:
        at,bt=tokens(a[box]),tokens(b[box]);diff=[]
        for tag,i,j,k,l in difflib.SequenceMatcher(None,at,bt,autojunk=False).get_opcodes():
            if tag!='equal':diff.append(f'{tag}: {at[i:j]} => {bt[k:l]}')
        out.append(dict(box=box,first=a[box],second=b[box],equal_tokens='yes' if at==bt else 'no',token_differences='; '.join(diff)))
    table(Path(str(base)+'_comparison.tsv'),['box','first','second','equal_tokens','token_differences'],out)
    Path(str(base)+'_comparison_metadata.json').write_text(json.dumps({'compared':now(),'first_sha256':hashlib.sha256(Path(str(base)+'_first.tsv').read_bytes()).hexdigest(),'second_sha256':hashlib.sha256(Path(str(base)+'_second.tsv').read_bytes()).hexdigest(),'method':'Strict lexical token comparison, including LaTeX commands and punctuation; no semantic normalization.'},indent=2)+'\n')
    print(json.dumps({'scan':scan,'boxes':len(out),'differences':sum(x['equal_tokens']=='no' for x in out)}))
def package(dest):
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(W.rglob('*')):
            if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts:z.write(p,p.relative_to(W))
    print(json.dumps({'zip':str(dest),'bytes':Path(dest).stat().st_size}))
if __name__=='__main__':
    action=sys.argv[1]
    if action=='assemble':print('Assembled',len(assemble()),'reviewed pages')
    elif action=='approve':approve(int(sys.argv[2]))
    elif action=='compare':compare(int(sys.argv[2]))
    elif action=='package':package(Path(sys.argv[2]))
