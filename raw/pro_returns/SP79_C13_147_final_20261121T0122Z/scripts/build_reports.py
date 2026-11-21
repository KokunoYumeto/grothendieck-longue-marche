"""Assemble the human-readable apparatus from visually adjudicated page reports.

No OCR, transcription inference, or semantic normalization occurs here.
"""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv, json, hashlib, shutil, sys

ROOT=Path(__file__).resolve().parents[1]
PREFIX='SP79_C13_147'
ORDER=[80,81,82,85,86,87,88,89,90,92,93,94,95,96,97,98,99,100,101,102,103,104,106,107]

def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def cell(v):
    if v is None: return ''
    if isinstance(v,(list,dict)): v=json.dumps(v,ensure_ascii=False)
    return str(v).replace('|','&#124;').replace('\n','<br>')
def table(headers,rows):
    return '| '+' | '.join(headers)+' |\n| '+' | '.join(['---']*len(headers))+' |\n'+''.join('| '+' | '.join(cell(c) for c in row)+' |\n' for row in rows)
def tsv(path,fields,rows):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fields,delimiter='\t',extrasaction='ignore');w.writeheader();w.writerows(rows)
def report_list():
    return [json.loads((ROOT/'adjudicated'/f'147_scan{n:03d}.json').read_text()) for n in ORDER if (ROOT/'adjudicated'/f'147_scan{n:03d}.json').exists()]
def evidence(ch):
    s=ch.get('ink','')
    if ch.get('crop'):
        s+=f" Crop: {ch['crop']}; original box {ch.get('box')}."
    else: s+=' Evidence: native-resolution page half.'
    return s
def build():
    rs=report_list()
    rows=[];coll=[];decs=[];inv=[];doubts=[];notes=[];events=[];hands=[];abbr={};notation={};feedback=Counter()
    countrows=[];conseq=[];witnessconfidence=[]
    for r in rs:
        n=r['scan'];changes=r.get('changes',[])
        cs=Counter(c.get('confidence','') for c in changes if c.get('against_C') or c.get('against_H'))
        cc=Counter(c.get('confidence','') for c in changes if c.get('against_C'))
        hc=Counter(c.get('confidence','') for c in changes if c.get('against_H'))
        witnessconfidence.append([f'{n:03d}',cc['high'],cc['medium'],cc['low'],hc['high'],hc['medium'],hc['low']])
        countrows.append([f'{n:03d}',sum(bool(c.get('against_C')) for c in changes),sum(bool(c.get('against_H')) for c in changes),cs['high'],cs['medium'],cs['low']])
        for c in changes:
            if c.get('consequential') and (c.get('against_C') or c.get('against_H')):conseq.append(f"- Scan {n:03d}, {c['place']}: {c['final']} — {c['ink']}")
        text=f"## Scan {n:03d}\n\n"
        changetable=[]
        for c in changes:
            if c.get('against_C') or c.get('against_H'):
                changetable.append([c.get('id',''),c['place'],c.get('C',''),c.get('H',''),c['final'],evidence(c),c['confidence']])
                feedback[c.get('category','other')]+=1
            if c.get('against_H'):
                coll.append(dict(folder='147',their_page=n-1,our_scan=n,line=c['place'],their_reading=c.get('H',''),codex_reading=c.get('C',''),final_reading=c['final'],scan_shows=evidence(c),kind=c.get('kind','other'),marked_in_H='yes' if c.get('marked_in_H') else 'no',confidence=c['confidence']))
        text+=table(['ID','Place','Witness C','Witness H','Final reading','What the scan shows','Confidence'],changetable) if changetable else 'No substantive reading differences from either witness.\n'
        if r.get('audit_decisions'):
            text+='\n### Blind second-reading adjudications\n\n'+table(['Box','First reading','Blind reading','Adjudication','Ink evidence and crop','Change'],[[a['box'],a['first'],a['second'],a['final'],a.get('ink','')+' Crop: '+a.get('crop','')+'.',a.get('changed',False)] for a in r['audit_decisions']])
        text+='\n### Unresolved places\n\n'
        if r.get('doubts'):text+='\n'.join(f"- {d['place']}: {d['reading']}. {d.get('reason','')}" for d in r['doubts'])+'\n'
        else:text+='None recorded after visual adjudication.\n'
        rows.append(text)
        for d in r.get('decisions',[]):
            decs.append({'id':d['id'],'cote':'147','scan':n,'decision':d['decision'],'reading':d['reading'],'what the ink shows':d.get('ink',''),'crop':f"{d.get('crop')} {d.get('box')}" if d.get('crop') and d.get('crop')!='page' else 'page','confidence':d['confidence']})
        for i in r.get('inventory',[]):inv.append(dict(scan=n,sheet_kind=r.get('sheet_kind','text'),**i))
        for d in r.get('doubts',[]):doubts.append([f'{n:03d}',d['place'],d['reading'],d.get('alternatives',''),d['confidence'],d.get('reason','')])
        nt=r.get('notes','')
        if isinstance(nt,list):nt='\n\n'.join(str(x) for x in nt)
        count_note=f"Reading count: {r.get('line_count', '')} lines. {r.get('line_count_note', '')}"
        notes.append(f'## Scan {n:03d}\n\n'+count_note+'\n\n'+nt+'\n')
        for e in r.get('check_events',[]):events.append(dict(statement_id=e['statement_id'],date=r.get('adjudicated_at',''),who='GPT-6 Astra Pro; main reader with page reader '+str(r.get('reader',''))+'; second pass SP79_C13_147; effort not separately exposed',type=e['type'],outcome=e['outcome']))
        for h in r.get('hand_log',[]):hands.append([f'{n:03d}',h.get('habit',''),h.get('holds',''),h.get('misread_locations','')])
        for a in r.get('abbreviations',[]):abbr.setdefault(a['form'],set()).add(a['expansion'])
        for a in r.get('notation',[]):notation.setdefault(a['notation'],[]).append((n,a.get('meaning_or_form',''),a.get('evidence','')))
    totals=['Total']+[sum(row[k] for row in countrows) for k in range(1,6)]
    summary='# Consolidated transcription: changes against witnesses C and H\n\n'+table(['Scan','Against C','Against H','High','Medium','Low'],countrows+[totals])
    summary+='\nCounts are substantive places (one row may differ from both witnesses), not tokens. The High/Medium/Low columns above count each substantive place once. Certainty-only changes are recorded in the doubts/decisions apparatus and excluded from these counts. Macro syntax and H editorial matter are excluded. Confidence describes the reading at the place.\n\n### Confidence by witness\n\n'
    wtotals=['Total']+[sum(row[k] for row in witnessconfidence) for k in range(1,7)]
    summary+=table(['Scan','C high','C medium','C low','H high','H medium','H low'],witnessconfidence+[wtotals])
    summary+='\n## Consequential corrections\n\n'+('\n'.join(conseq) if conseq else 'None recorded yet.')+'\n\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(summary+'\n'.join(rows))
    tsv(ROOT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],coll)
    decs.sort(key=lambda d:int(d['id'][1:]))
    tsv(ROOT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decs)
    with (ROOT/f'{PREFIX}_inventory.csv').open('w',newline='') as f:
        w=csv.DictWriter(f,['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],extrasaction='ignore');w.writeheader();w.writerows(inv)
    ntab=table(['Notation','Observed form / use','Evidence'],[[a,'; '.join(dict.fromkeys(v[1] for v in vals)),'; '.join(f'scan {v[0]:03d}: {v[2]}' for v in vals)] for a,vals in notation.items()])
    (ROOT/'notation.md').write_text('# Working notation table\n\n'+ntab)
    dtext='# Notation, remaining doubts, and abbreviations\n\n'+ntab+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence','Reason'],doubts)
    dtext+='\n## Abbreviations\n\nExpansions are editorial suggestions for this list only; they are not substituted into the transcription.\n\n'+table(['Written form','Possible expansion'],[[a,'; '.join(sorted(v))] for a,v in abbr.items()])
    dtext+='\n## Legibility and comparison of witnesses\n\n'+((ROOT/'legibility_note.txt').read_text() if (ROOT/'legibility_note.txt').exists() else 'Assessment in progress; see the individual unresolved places and confidence levels above. No claim of resolution is made for ink retained as doubtful.')+'\n'
    (ROOT/f'{PREFIX}_doubts.md').write_text(dtext)
    (ROOT/f'{PREFIX}_notes.md').write_text('# Notes while reading\n\nThese notes report what the supplied pages say and the local mathematical considerations used in reading them. No outside sources were researched. Reading a statement is not counted as checking its proof.\n\n'+'\n'.join(notes))
    tsv(ROOT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],events)
    (ROOT/f'{PREFIX}_hand_log.md').write_text('# Hand log\n\nThe occurrence ranges below are bounded by the pages visually inspected; an observation is not generalized beyond its evidence.\n\n'+table(['Scan(s)','Habit or notation','Scope of confirmation','Witness misreadings / places'],hands))
    categories=['symbols and indices','words','omissions','drawings and diagrams','readable ink left as illegible','insertion placement','struck text','abbreviations and spelling','text not on the page','other']
    extra_feedback=(ROOT/'feedback_observations.txt').read_text() if (ROOT/'feedback_observations.txt').exists() else 'See the hand log for occurrence-specific observations. The final review will distinguish any additional recurring error from kinds already named in the supplied sheet.'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text('# Feedback on the recurring-error sheet\n\nCounts concern substantive logged places, assigned one principal error-sheet category. They are not estimates of error rates, and a place can differ from one or both witnesses. Certainty-only decisions are excluded.\n\n'+table(['Error-sheet category','Places'],[[k,feedback[k]] for k in categories])+'\n## Additional recurring observations\n\n'+extra_feedback+'\n')
    combined='\\cotefile{147}\n\n'+'\n\n'.join((ROOT/'pages'/f'147_scan{r["scan"]:03d}.tex').read_text().rstrip() for r in rs)+'\n'
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
    print(json.dumps({'pages':len(rs),'changes_C':totals[1],'changes_H':totals[2],'decisions':len(decs),'inventory':len(inv),'doubts':len(doubts)},ensure_ascii=False))

def approve(n):
    stem=f'147_scan{n:03d}'
    (ROOT/'adjudicated').mkdir(exist_ok=True)
    p=ROOT/'adjudicated'/f'{stem}.json'
    if not p.exists():shutil.copyfile(ROOT/'reviews'/f'{stem}.json',p)
    r=json.loads(p.read_text());r['adjudicated_at']=utc();r['main_reader_reviewed']=True
    p.write_text(json.dumps(r,ensure_ascii=False,indent=2)+'\n')
    if not (ROOT/'pages'/f'{stem}.tex').exists():shutil.copyfile(ROOT/'reviews'/f'{stem}.tex',ROOT/'pages'/f'{stem}.tex')
    build()
    with (ROOT/'progress.log').open('a') as f:
        cropcount=len(list((ROOT/'crops').glob(f'{stem}_*.png')))
        rowcount=sum(bool(c.get('against_C') or c.get('against_H')) for c in r.get('changes',[]))
        f.write(f"scan {n:03d} done {utc()} cote 147: {r['line_count']} lines read, {cropcount} places cropped, {rowcount} rows\n")

def second_prepare(n):
    stem=f'147_scan{n:03d}';r=json.loads((ROOT/'adjudicated'/f'{stem}.json').read_text());bs=r['second_boxes']
    # Keep box kinds descriptive of tasks, never of expected readings.  In
    # particular, handwritten digit values and candidate words must not leak
    # into the blind reader's box list.
    clean=[]; first=[]; index=[]
    for position,b in enumerate(bs,1):
        k=b.get('kind','').lower(); categories=[]
        for needles,label in [
            (('diagram',),'diagram'), (('formula',),'formula'),
            (('number','numeral','digit','folio','page label'),'handwritten number'),
            (('margin','marginal','slanted'),'margin note'),
            (('struck','cancel','deletion'),'struck passage'),
            (('insert','replacement'),'insertion'),
            (('different','c/h','disagree','word'),'witness difference'),
            (('drawing','callout','bracket'),'drawing'),
            (('low','medium','doubt','uncertain'),'uncertain reading')]:
            if any(x in k for x in needles):categories.append(label)
        # The identifiers also must not reveal the first reading (for example,
        # a filename such as 'forgetting' would cue a disputed French word).
        blind_id=f'{n:03d}-B{position:02d}'
        clean.append({**b,'box':blind_id,'kind':'; '.join(categories) or 'reading box'})
        first.append({'box':blind_id,'reading':b['reading']})
        index.append({'box':blind_id,'source_box':b['box']})
    tsv(ROOT/'second'/f'{stem}_boxes.tsv',['box','kind','x0','y0','x1','y1'],clean)
    tsv(ROOT/'second'/f'{stem}_first.tsv',['box','reading'],first)
    tsv(ROOT/'second'/f'{stem}_box_index.tsv',['box','source_box'],index)

if __name__=='__main__':
    if len(sys.argv)==1 or sys.argv[1]=='build':build()
    elif sys.argv[1]=='approve':approve(int(sys.argv[2]))
    elif sys.argv[1]=='second':
        for n in map(int,sys.argv[2:]):second_prepare(n)
