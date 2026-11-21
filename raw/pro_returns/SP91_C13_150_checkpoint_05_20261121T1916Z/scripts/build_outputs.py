from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime, timezone
import csv,json,hashlib,re,sys,zipfile

ROOT=Path(__file__).resolve().parents[1]
BASE=ROOT.parent
PREFIX='SP91_C13_150'
ORDER=json.loads((ROOT/'scripts/page_order.json').read_text())

def now():return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def md(s):return str(s).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join('---' for _ in headers)+' |\n'+''.join('| '+' | '.join(md(v) for v in row)+' |\n' for row in rows)
def tsv(path,headers,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.writer(f,delimiter=delimiter);w.writerow(headers);w.writerows(rows)
def records():
    return [json.loads((ROOT/'records'/f'150_scan{s}.json').read_text()) for s in ORDER if (ROOT/'records'/f'150_scan{s}.json').exists()]
def counted(c):return bool(c.get('against_C') or c.get('against_H'))
def crop_evidence(c):
    result=c.get('evidence','')
    if c.get('crop') and c['crop']!='page':result+=' Crop: `'+c['crop']+'`; box '+str(c.get('box',''))+'.'
    return result

def build():
    rr=records()
    (ROOT/(PREFIX+'_transcription.tex')).write_text('\\cotefile{150}\n\n'+'\n\n'.join((ROOT/'pages'/f"150_scan{r['scan']}.tex").read_text().strip() for r in rr)+'\n')
    countrows=[];total=Counter();consequences=[]
    for r in rr:
        ch=r.get('changes',[]);ct=Counter(c.get('confidence','low') for c in ch if counted(c))
        a=sum(bool(c.get('against_C')) for c in ch);b=sum(bool(c.get('against_H')) for c in ch)
        total.update({'C':a,'H':b,'places':sum(counted(c) for c in ch),**ct})
        countrows.append([r['scan'],a,b,sum(counted(c) for c in ch),ct['high'],ct['medium'],ct['low']])
        for c in ch:
            if c.get('mathematical_consequence'):consequences.append(f"- Scan {r['scan']}, {c['place']}: {c['mathematical_consequence']} ({c['id']}).")
    countrows.append(['Total',total['C'],total['H'],total['places'],total['high'],total['medium'],total['low']])
    changes='# Consolidation changes: cote 150\n\nCounts are substantive reading places; a place differing from both witnesses is counted once in Places and once in each witness column. Equivalent TeX syntax and certainty-only changes are excluded from these counts. At unresolved C/H disagreements, counts compare the leading proposed reading with each witness; the confidence and alternatives remain explicit, and such a comparison does not assert a settled error. Certainty-only decisions, where listed below, are identified explicitly. H page references follow its source page marker (scan number minus one).\n\n'+table(['Scan','Against C','Against H','Places','High','Medium','Low'],countrows)+'\n## Consequential readings\n\n'+('\n'.join(consequences) or 'None recorded yet.')+'\n'
    coll=[];decisionmap={};inv=[];doubts=[];notation=defaultdict(list);abbrevs=defaultdict(list);notes='# Notes while reading\n\nThese notes report the manuscript and the actual reading decisions. Mathematical check events are recorded separately; a transcription or attributed summary is not represented as a proof check.\n';events=[];hand='# Hand log\n';categories=Counter();categoryC=Counter();categoryH=Counter()
    for r in rr:
        s=r['scan'];changes+=f'\n## Scan {s}\n\n'
        rows=[]
        for c in r.get('changes',[]):
            place=c['place']+' ['+c['id']+']'+(' (certainty only)' if not counted(c) else '')
            rows.append([place,c.get('C',''),c.get('H',''),c.get('final',''),crop_evidence(c),c.get('confidence','low')])
            if c.get('against_H'):
                coll.append(['150',int(s)-1,int(s),c['place'],c.get('H',''),c.get('C',''),c.get('final',''),crop_evidence(c),c.get('kind','other'),'yes' if c.get('marked_in_H') else 'no',c.get('confidence','low')])
            if counted(c):categories[c.get('error_category','Other')]+=1
            if c.get('against_C'):categoryC[c.get('error_category','Other')]+=1
            if c.get('against_H'):categoryH[c.get('error_category','Other')]+=1
        changes+=table(['Place','C','H','Consolidated reading','What the scan shows','Confidence'],rows) if rows else 'No substantive reading difference recorded.\n'
        changes+='\nUnresolved: '+('; '.join(r.get('unresolved',[])) or 'None recorded.')+'\n'
        if r.get('audit_adjudications'):
            changes+='\n### Blind second-reading adjudication\n\nThe first reading was recorded before the independent second reading. Every token difference is accounted for below; cropped neighbouring fragments and equivalent markup are identified in the evidence. A changed page reading is marked explicitly.\n\n'
            changes+=table(['Box','First reading','Independent second reading','Final box reading','Page changed','Image decision','Confidence'],[[a['box'],a['first'],a['second'],a['final'],a['changed'],a['evidence']+' Crop: `'+a['crop']+'`; box '+a['box_pixels']+'.',a['confidence']] for a in r['audit_adjudications']])
        for d in r.get('decisions',[]):decisionmap[d['id']]=(s,d)
        for x in r.get('inventory',[]):inv.append([s,x.get('sheet_kind','text'),x.get('hand','his hand'),x['element'],x['kind'],x['position'],x['first_words_or_objects'],x.get('transcribed','yes')])
        for x in r.get('doubts',[]):doubts.append([s,x['place'],x['reading'],x.get('alternatives',''),x.get('confidence','low'),x.get('reason','')])
        for x in r.get('notation',[]):notation[x['form']].append((s,x))
        for x in r.get('abbreviations',[]):abbrevs[x['written']].append((s,x))
        notes+=f'\n## Scan {s}\n\n'+''.join(f"- **{x['id']}**: {x['text']}\n" for x in r.get('notes',[]))
        for x in r.get('check_events',[]):events.append([x['statement_id'],x.get('date',r.get('finalized_at','')),x.get('who','GPT-6 Astra Pro; effort not exposed; SP91_C13_150'),x['type'],x['outcome']])
        hand+=f'\n## Scan {s}\n\n'
        hand+=table(['Habit','Places','Scope','Witness readings affected'],[[x['habit'],x.get('places',''),x.get('scope',''),x.get('witness_errors','')] for x in r.get('hand_log',[])]) if r.get('hand_log') else 'No new habit recorded.\n'
    (ROOT/(PREFIX+'_changes.md')).write_text(changes)
    tsv(ROOT/(PREFIX+'_collation.tsv'),['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    marks=list(csv.DictReader((BASE/'input/SP91_C13_150_texts/MARKS.tsv').open(),delimiter='\t',quoting=csv.QUOTE_NONE))
    dr=[]
    for m in marks:
        if m['id'] not in decisionmap:continue
        s,d=decisionmap[m['id']];crop=d.get('crop','page')
        if crop!='page':crop=f"scan {s}; {crop}; {d.get('box','')}"
        dr.append([m['id'],'150',int(s),d['decision'],d['reading'],d.get('evidence',''),crop,d['confidence']])
    tsv(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],dr)
    tsv(ROOT/(PREFIX+'_inventory.csv'),['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
    nr=[]
    for form,xx in notation.items():nr.append([form,'; '.join(dict.fromkeys(x['meaning'] for _,x in xx)),'; '.join(s+': '+x.get('places','')+' '+x.get('evidence','') for s,x in xx)])
    nt='# Notation table\n\n'+table(['Written form / transcription','Meaning on these pages','Image evidence and places'],nr)
    (ROOT/'notation.md').write_text(nt)
    ar=[[a,'; '.join(dict.fromkeys(x['expansion'] for _,x in xx)),'; '.join(s+': '+x.get('places','') for s,x in xx)] for a,xx in abbrevs.items()]
    assessment=(ROOT/'records/legibility.txt').read_text() if (ROOT/'records/legibility.txt').exists() else 'Assessment remains in progress while the page readings and blind audit are completed.'
    (ROOT/(PREFIX+'_doubts.md')).write_text(nt+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)+'\n## Abbreviations\n\nExpansions below explain the retained short forms; they are not substituted into the transcription.\n\n'+table(['Written','Expansion','Places'],ar)+'\n## Legibility and witnesses\n\n'+assessment+'\n')
    (ROOT/(PREFIX+'_notes.md')).write_text(notes)
    tsv(ROOT/'CHECK_EVENTS.tsv',['statement id','date','who (model, effort, run)','type','outcome'],events)
    (ROOT/(PREFIX+'_hand_log.md')).write_text(hand)
    cats=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    feedback='# Error-sheet feedback\n\nCounts refer to recorded substantive reading places in the changes log. Each place receives one primary category; a place may differ from both witnesses. They do not measure an error rate over all manuscript tokens.\n\n'+table(['Error-sheet kind','Places','Against C','Against H'],[[c,categories[c],categoryC[c],categoryH[c]] for c in cats])
    feedback+='\n## Further recurring observations\n\n'+((ROOT/'records/feedback.txt').read_text() if (ROOT/'records/feedback.txt').exists() else 'See the page-specific hand log for observed letter forms and their scope. The recurrence review is in progress.')+'\n'
    (ROOT/(PREFIX+'_sheet_feedback.md')).write_text(feedback)
    print(json.dumps({'pages':len(rr),'changes_C':total['C'],'changes_H':total['H'],'places':total['places'],'decisions':len(dr),'inventory':len(inv),'doubts':len(doubts)},ensure_ascii=False))

def finalize(s):
    rp=ROOT/'records'/f'150_scan{s}.json'
    r=json.loads(rp.read_text())
    assert r.get('main_reviewed'), 'Main reader must mark its completed visual review'
    assert (ROOT/'pages'/f'150_scan{s}.tex').exists()
    expected={x['id'] for x in csv.DictReader((ROOT/'packets'/f'150_scan{s}'/'marks.tsv').open(),delimiter='\t')}
    assert expected=={x['id'] for x in r.get('decisions',[])},('missing or extra marks',expected)
    for c in r.get('crops',[]):assert (ROOT/c['file']).exists(),c
    for d in r.get('decisions',[]):
        if d['decision']!='undecided':assert d.get('crop') not in ('page',None,''),d
    r['finalized_at']=now();rp.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    build()
    with (ROOT/'progress.log').open('a') as f:f.write(f"scan {s} done {now()} cote 150: {r['line_count']} lines read, {len(r.get('crops',[]))} places cropped, {len(r.get('changes',[]))} rows\n")

def audit_files():
    for r in records():
        stem='150_scan'+r['scan'];bb=r['audit_boxes']
        assert not (ROOT/'second'/f'{stem}_second.tsv').exists(), 'Never overwrite the recorded first reading after a blind reading exists: '+stem
        assert not (ROOT/'second'/f'{stem}_first.tsv').exists(), 'First reading already recorded: '+stem
        tsv(ROOT/'second'/f'{stem}_boxes.tsv',['box','kind','x0','y0','x1','y1'],[[b[k] for k in ['box','kind','x0','y0','x1','y1']] for b in bb])
        # Preserve the recorded source-position context in the first reading.
        # These comments are part of the exact lexical comparison; they never
        # complete clipped manuscript text or alter a page's transcription.
        tsv(ROOT/'second'/f'{stem}_first.tsv',['box','reading'],[
            [b['box'],b['reading'] + ('\n% Source-position context: '+b['comment'] if b.get('comment') else '')]
            for b in bb
        ])

def archive(name):
    dest=BASE/'deliverables'/name;dest.parent.mkdir(exist_ok=True)
    if dest.exists():raise RuntimeError('Archive already exists: '+str(dest))
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(ROOT.rglob('*')):
            rel=p.relative_to(ROOT)
            if not p.is_file() or p.suffix in ('.zip','.pending','.tmp') or '__pycache__' in p.parts:continue
            if rel.parts[0]=='packets':continue
            z.write(p,rel.as_posix())
    print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))

if __name__=='__main__':
    cmd=sys.argv[1] if len(sys.argv)>1 else 'build'
    if cmd=='build':build()
    elif cmd=='finalize':finalize(sys.argv[2])
    elif cmd=='audit-files':audit_files()
    elif cmd=='archive':archive(sys.argv[2])
