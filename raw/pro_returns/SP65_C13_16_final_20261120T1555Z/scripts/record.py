#!/usr/bin/env python3
"""Record manually read evidence and render deliverables; no OCR or TeX compilation."""
import csv, json, re, sys
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT.parent/'source'/'SP65_C13_16_texts'
PREFIX='SP65_C13_16'
RECORDS=ROOT/'scripts'/'records'
RECORDS.mkdir(exist_ok=True)
def utc(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def md(v): return str(v).replace('|',r'\|').replace('\n','<br>')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(md(v) for v in row)+' |' for row in rows])+'\n'
def write_tsv(name,head,rows,delimiter='\t'):
    with (ROOT/name).open('w',newline='',encoding='utf-8') as f:
        w=csv.writer(f,delimiter=delimiter);w.writerow(head);w.writerows(rows)
def crop_references(record):
    references={}
    def visit(value):
        if isinstance(value,str):
            for match in re.finditer(r'\bscan\s*(\d+)\s*\(\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*\)',value,re.IGNORECASE):
                scan,x0,y0,x1,y1=map(int,match.groups())
                key=(scan,x0,y0,x1,y1)
                references.setdefault(key,f'scan {scan:03} ({x0}, {y0}, {x1}, {y1})')
        elif isinstance(value,dict):
            for key,item in value.items():visit(key);visit(item)
        elif isinstance(value,(list,tuple)):
            for item in value:visit(item)
    visit(record)
    return list(references.values())
def build():
    records=[json.loads(p.read_text()) for p in sorted(RECORDS.glob('*.json'))]
    rows=[(p,r) for p in records for r in p.get('changes',[])]
    counts=[]
    for p in records:
        rr=p.get('changes',[]);cc=Counter(r['confidence'] for r in rr)
        counts.append([f"{p['scan']:03}",sum(r.get('dc',False) for r in rr),sum(r.get('dh',False) for r in rr),cc['high'],cc['medium'],cc['low']])
    totals=['TOTAL']+[sum(r[i] for r in counts) for i in range(1,6)]
    s='# Consolidated reading: changes\n\nOnly changes of reading or source-text state are counted here. Pure macro equivalents and certainty-only resolutions are excluded; the latter are recorded in decisions.tsv and the doubts file. The confidence columns count loci (a locus differing from both witnesses counts once). C and H are the supplied drafts. An em dash in H means that witness omits the locus; `no H page` means the witness is unavailable. Pixel boxes use the original scan coordinate system. `page` means the full-resolution page/halves settled the reading.\n\n'
    s+=table(['Scan','Against C','Against H','High','Medium','Low'],counts+[totals])
    s+='\n## Consequential corrections\n\n'
    consequences=[f"- Scan {p['scan']:03}, {r['place']}: {r['consequence']}" for p,r in rows if r.get('consequence')]
    s+='\n'.join(consequences) if consequences else 'No mathematical change has yet been entered.'
    s+='\n'
    for p in records:
        s+=f"\n## Scan {p['scan']:03}\n\n"
        rr=p.get('changes',[])
        s+=table(['Place','C','H','Final','What the scan shows; crop','Confidence'],[[r[k] for k in ['place','c','h','final','ink','confidence']] for r in rr]) if rr else 'No substantive witness difference recorded.\n'
        s+='\n### Crop examinations\n\n'
        crops=crop_references(p)
        s+='\n'.join('- `'+crop+'`' for crop in crops) if crops else 'No crop reference recorded.'
        s+='\n'
        s+='\n### Unresolved\n\n'
        s+='\n'.join('- '+d[0]+': `'+d[1]+'`; '+d[2]+'; '+d[3]+'.' for d in p.get('doubts',[])) or 'None.'
        s+='\n'
    (ROOT/f'{PREFIX}_changes.md').write_text(s)
    write_tsv(f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],[[16,p['scan']-1,p['scan'],r['place'],r['h'],r['c'],r['final'],r['ink'],r['kind'],r.get('marked_h','no'),r['confidence']] for p,r in rows if r.get('dh')])
    decisions=[d for p in records for d in p.get('decisions',[])]
    byid={d[0]:d for d in decisions}
    original=list(csv.DictReader((SOURCE/'MARKS.tsv').open(),delimiter='\t'))
    write_tsv('decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],[[m['id'],m['cote'],m['scan'],*byid[m['id']][1:]] for m in original if m['id'] in byid])
    inv=[]
    for p in records:
        for n,v in enumerate(p.get('inventory',[]),1):
            inv.append([p['scan'],p.get('sheet_kind','text'),v[3] if len(v)>3 else 'his hand',f"{p['scan']:03}-{n:02}",v[0],v[1],v[2],'yes'])
    write_tsv(f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inv,',')
    s='# Reading notes\n\nThese notes describe only the supplied pages. Transcribing a statement does not certify it. Mathematical checks actually performed are separately recorded in CHECK_EVENTS.tsv; statements merely reported as manuscript content have no fabricated check event. No external source was consulted.\n'
    for p in records:
        s+=f"\n## Scan {p['scan']:03}\n\n"+p.get('notes','')+'\n'
        for audit in p.get('audit_notes',[]):
            s+='\n### Second reading — '+audit['utc']+'\n\n'+audit['note']+'\n'
    (ROOT/f'{PREFIX}_notes.md').write_text(s)
    write_tsv('CHECK_EVENTS.tsv',['statement_id','date','who (model, effort, run)','type','outcome'],[c for p in records for c in p.get('checks',[])])
    s='# Notation table and doubts\n\n## Notation table\n\n'+table(['Notation','Form in ink','Pages','Scope and exceptions'],[v for p in records for v in p.get('notation',[])])
    review_path=ROOT/'scripts/notation_review.txt'
    if review_path.exists():s+='\n### Final comparison across pages\n\n'+review_path.read_text()+'\n'
    s+='\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives or limitation','Confidence'],[[p['scan'],*d] for p in records for d in p.get('doubts',[])])
    s+='\n## Certainty-only resolutions\n\n'+table(['Scan','Mark or place','Resolution'],[[p['scan'],*v] for p in records for v in p.get('certainty',[])])
    s+='\n## Abbreviations\n\nExpansions here are reading aids only and are not substituted into the transcription.\n\n'+table(['Written form','Proposed expansion','Scan'],[[v[0],v[1],p['scan']] for p in records for v in p.get('abbreviations',[])])
    s+='\n## Legibility and witness comparison\n\n'+(ROOT/'scripts/assessment.txt').read_text() if (ROOT/'scripts/assessment.txt').exists() else '\n## Legibility and witness comparison\n\nAssessment remains open during the reading.\n'
    (ROOT/f'{PREFIX}_doubts.md').write_text(s)
    s='# Hand and notation log\n\nEvery observation is restricted to the supplied scans. Entries describe observed scope, exceptions and actual witness consequences; a resemblance does not license replacing a clearly written letter.\n\n'+table(['Habit','Pages','Scope and exceptions','Witness misreadings'],[v for p in records for v in p.get('hand',[])])
    (ROOT/f'{PREFIX}_hand_log.md').write_text(s)
    cats={1:'Symbols and indices',2:'Words',3:'Omissions',4:'Drawings and diagrams',5:'Readable ink left as illegible',6:'Insertion placement',7:'Struck text',8:'Abbreviation or spelling',9:'Text absent from page',10:'Other'}
    ec=Counter(r.get('error',10) for p,r in rows)
    s='# Error-sheet feedback\n\nCounts are changed loci assigned one primary category; a locus affecting both witnesses counts once. Certainty-only decisions are excluded. The same locus can involve secondary features described in the changes log. These are observed collation counts, not estimates of all errors in either draft.\n\n'+table(['Kind','Count'],[[f'{i}. {cat}',ec[i]] for i,cat in cats.items()])
    s+='\n## Places by category\n\n'
    for i,cat in cats.items():s+=f'### {i}. {cat}\n\n'+('; '.join(f"scan {p['scan']:03}: {r['place']}" for p,r in rows if r.get('error',10)==i) or 'No changed locus assigned.')+'\n\n'
    s+='## Additional recurring patterns\n\n'+('\n'.join(v for p in records for v in p.get('feedback',[])) or 'No additional recurring error class was established beyond the ten categories above.')+'\n'
    (ROOT/f'{PREFIX}_sheet_feedback.md').write_text(s)
    combined='\\cotefile{16}\n\n'+'\n\n'.join((ROOT/'pages'/f"16_scan{p['scan']:03}.tex").read_text().rstrip() for p in records)+'\n'
    (ROOT/f'{PREFIX}_transcription.tex').write_text(combined)
if __name__=='__main__':
    if len(sys.argv)>1 and sys.argv[1]=='build':build();sys.exit()
    p=json.load(sys.stdin);n=p['scan'];path=ROOT/'pages'/f'16_scan{n:03}.tex'
    if 'text' in p:text=p.pop('text')
    else:
        text=(SOURCE/'pages'/path.name).read_text()
        for old,new in p.get('replace',[]):
            assert old in text, f'{n}: missing replacement {old!r}'
            text=text.replace(old,new)
    path.write_text(text.rstrip()+'\n',encoding='utf-8')
    (RECORDS/f'{n:03}.json').write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n')
    build()
    with (ROOT/'progress.log').open('a') as f:f.write(f'scan {n:03} done {utc()} cote 16\n')
    print(f'Recorded scan {n:03}: {len(p.get("changes",[]))} changed loci; {len(p.get("decisions",[]))} mark decisions.')
