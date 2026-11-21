"""Assemble human-readable records from page readings approved by the main reader.

This script never reads manuscript images or chooses a transcription. It only
formats the manually adjudicated records, checks coverage, and packages files.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, re, hashlib, sys, zipfile, collections

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parents[1]
PREFIX='SP82_C13_148'
SCANS=[21,22,23,24,25,26,27,28,29,31,32,33,34,35,36,37,38,39,41,42,43,44,46,47]

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def write_tsv(path,fields,rows,delimiter='\t'):
    with path.open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=fields,delimiter=delimiter,extrasaction='ignore')
        w.writeheader();w.writerows(rows)
def cell(x):
    if x is None:return ''
    if not isinstance(x,str):x=json.dumps(x,ensure_ascii=False)
    return x.replace('|','\\|').replace('\n','<br>')
def table(headers,rows):
    return '\n'.join(['| '+' | '.join(headers)+' |','|'+'|'.join(['---']*len(headers))+'|']+['| '+' | '.join(cell(x) for x in r)+' |' for r in rows])+'\n'
def prose(v):
    if isinstance(v,str):return v
    if isinstance(v,list):return '\n\n'.join(prose(x) for x in v)
    if isinstance(v,dict):
        title=v.get('id',v.get('place',v.get('form',v.get('habit',''))))
        body=v.get('text',v.get('issue',v.get('observation',v.get('habit',''))))
        if v.get('reading'):body='Reading: `'+v['reading']+'`. '+body
        extra=[]
        for key in ('alternatives','occurrences','witness_effect','expansion','meaning','pages','holds_at_every_observed_occurrence','confidence'):
            if key in v:
                val=v[key]
                if isinstance(val,list):val=', '.join(map(str,val))
                extra.append(key.replace('_',' ').capitalize()+': '+str(val)+'.')
        return (('**'+str(title)+'** — ') if title else '')+str(body)+(' '+' '.join(extra) if extra else '')
    return str(v)
def evidence(r):
    crop=r.get('crop','page');box=r.get('box',[])
    return r.get('ink','')+' '+str(crop)+(f' {tuple(box)}' if box else '')
def approved():
    return [json.loads(p.read_text()) for p in sorted((OUT/'reviews').glob('148_scan*.json')) if json.loads(p.read_text()).get('approved')]

def rebuild():
    pages=approved()
    allchanges=[];collation=[];decisions=[];inventory=[];checks=[];notes=[];hands=[];doubts=[];abbreviations=[]
    counts=[]
    for p in pages:
        scan=int(p['scan']);ch=p.get('changes',[])
        c=sum(bool(r.get('against_c')) for r in ch);h=sum(bool(r.get('against_h')) for r in ch)
        conf=collections.Counter(r['confidence'] for r in ch)
        counts.append([f'{scan:03d}',len(ch),c,h,conf['high'],conf['medium'],conf['low']])
        section=[f'## Scan {scan:03d}',table(['Place','Witness C','Witness H','Final reading','What the scan shows / crop (original pixels)','Confidence'],[[r.get('place',''),r.get('c',''),r.get('h',''),r.get('final',''),evidence(r),r['confidence']] for r in ch])]
        unresolved=p.get('unresolved',[])
        section+=['### Still unresolved',prose(unresolved) if unresolved else 'None.']
        allchanges.append('\n\n'.join(section))
        for r in ch:
            if r.get('against_h'):
                kind=r.get('kind','other')
                if kind=='deletion state':kind='deletion state (struck given live or live given struck)'
                collation.append(dict(folder='148',their_page=scan-1,our_scan=scan,line=r.get('place',''),their_reading=r.get('h') or '',codex_reading=r.get('c') or '',final_reading=r.get('final',''),scan_shows=evidence(r),kind=kind,marked_in_H=r.get('marked_in_H','yes' if any(s in (r.get('h') or '') for s in ['\\ill','\\unclear','\\uncertain','\\unsure']) else 'no'),confidence=r['confidence']))
        for r in p.get('decisions',[]):
            decisions.append(dict(id=r['id'],cote='148',scan=scan,decision=r['decision'],reading=r['reading'],**{'what the ink shows':r.get('ink','')},crop=str(r.get('crop','page'))+(f' scan {scan:03d} {tuple(r["box"])}' if r.get('box') else ''),confidence=r['confidence']))
        for r in p.get('inventory',[]):inventory.append(dict(scan=scan,**r))
        for r in p.get('checks',[]):checks.append(r)
        notes.append(f'## Scan {scan:03d}\n\n'+prose(p.get('notes','')))
        if p.get('hand_log'):hands.append(f'## Scan {scan:03d}\n\n'+prose(p['hand_log']))
        for r in unresolved:
            if isinstance(r,dict):doubts.append([scan,r.get('place',r.get('line','')),r.get('reading',''),r.get('alternatives',''),r.get('confidence','')])
            else:doubts.append([scan,'',str(r),'',''])
        if p.get('abbreviations'):abbreviations.append(f'### Scan {scan:03d}\n\n'+prose(p['abbreviations']))
    total=[sum(r[i] for r in counts) for i in range(1,7)]
    counts.append(['Total',*total])
    consequential=[]
    for p in pages:
        for r in p.get('changes',[]):
            if r.get('math'):
                summary=r.get('math_summary') or r.get('final','')
                if len(summary)>250:summary=r.get('ink','')
                consequential.append(f'- Scan {int(p["scan"]):03d}, {r.get("place", "")}: {summary} ({r.get("confidence", "")}).')
    intro='# Changes against the two drafts\n\nCounts are editorial places, not characters. A place may differ from both witnesses. Macro syntax alone is excluded. H is absent on scans 022 and 029.\n\n'
    (OUT/f'{PREFIX}_changes.md').write_text(intro+table(['Scan','Rows','Against C','Against H','High','Medium','Low'],counts)+'\n## Consequential corrections\n\n'+('\n'.join(consequential) or 'No mathematical reading changes recorded in the completed pages yet.')+'\n\n'+'\n\n'.join(allchanges)+'\n')
    write_tsv(OUT/f'{PREFIX}_collation.tsv',['folder','their_page','our_scan','line','their_reading','codex_reading','final_reading','scan_shows','kind','marked_in_H','confidence'],collation)
    markorder={r['id']:i for i,r in enumerate(csv.DictReader((ROOT/'source/SP82_C13_148_texts/MARKS.tsv').open(),delimiter='\t'))}
    decisions.sort(key=lambda x:markorder[x['id']])
    write_tsv(OUT/'decisions.tsv',['id','cote','scan','decision','reading','what the ink shows','crop','confidence'],decisions)
    write_tsv(OUT/f'{PREFIX}_inventory.csv',['scan','sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'],inventory,',')
    write_tsv(OUT/'CHECK_EVENTS.tsv',['statement_id','date','who','type','outcome'],checks)
    (OUT/f'{PREFIX}_notes.md').write_text('# Reading notes\n\nThese are observations on the supplied pages only. A page summary does not certify its mathematical claims; actual checks are separately recorded in CHECK_EVENTS.tsv.\n\n'+'\n\n'.join(notes)+'\n')
    (OUT/f'{PREFIX}_hand_log.md').write_text('# Hand log\n\nOnly observed habits are recorded; an observation on one page is not asserted universal.\n\n'+'\n\n'.join(hands)+'\n')
    (OUT/f'{PREFIX}_doubts.md').write_text((OUT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],doubts)+'\n## Abbreviations\n\n'+'\n\n'.join(abbreviations)+'\n\n## Legibility and the two witnesses\n\n'+(OUT/'legibility.md').read_text() if (OUT/'legibility.md').exists() else (OUT/'notation.md').read_text()+'\n## Remaining doubts\n\n'+table(['Scan','Place','Reading','Alternatives','Confidence'],doubts)+'\n## Abbreviations\n\n'+'\n\n'.join(abbreviations)+'\n\nLegibility assessment pending completion of all pages.\n')
    (OUT/f'{PREFIX}_transcription.tex').write_text('\\cotefile{148}\n\n'+'\n\n'.join((OUT/'pages'/f'148_scan{int(p["scan"]):03d}.tex').read_text().rstrip() for p in pages)+'\n')
    categories=['Symbols and indices','Words','Omissions','Drawings and diagrams','Readable ink left as illegible','Insertions put in the wrong place','Struck text','Abbreviations expanded, spelling modernised','Text that is not on the page','Other']
    mapping={'misread symbol or index':categories[0],'misread word':categories[1],'omission':categories[2],'drawing or diagram':categories[3],'readable ink left as \\ill{}':categories[4],'insertion or placement':categories[5],'deletion state':categories[6],'deletion state (struck given live or live given struck)':categories[6],'abbreviation expanded or spelling modernised':categories[7],'text not on the page':categories[8],'other':categories[9]}
    grouped={k:[] for k in categories}
    for p in pages:
        for r in p.get('changes',[]):
            grouped[mapping.get(r.get('kind','other'),categories[9])].append(f'Scan {int(p["scan"]):03d}: {r.get("place", "")}')
    feedback='# Error-sheet feedback\n\nCounts are changed editorial places in the approved pages, not a statistical error rate. Each place is assigned its primary error-sheet category; a correction can affect both witnesses. Changes of macro syntax alone are excluded. The detailed evidence remains in the changes log.\n\n'
    feedback+=table(['Error-sheet category','Places'],[[k,len(grouped[k])] for k in categories])
    for k in categories:
        feedback+='\n## '+k+'\n\n'+('; '.join(grouped[k])+'.' if grouped[k] else 'No changed places recorded.')+'\n'
    feedback+='\n## Recurring observations beyond the listed categories\n\n'
    extra=OUT/'feedback_observations.md'
    feedback+=extra.read_text() if extra.exists() else 'Assessment will be completed after all scans and the blind readings. The hand log records observed letterforms and their specific locations.\n'
    (OUT/f'{PREFIX}_sheet_feedback.md').write_text(feedback)
    print(json.dumps({'approved_scans':[p['scan'] for p in pages],'changes':total[0],'against_C':total[1],'against_H':total[2],'decisions':len(decisions),'inventory':len(inventory)},ensure_ascii=False))

def accept(scan):
    path=OUT/'reviews'/f'148_scan{scan:03d}.json';p=json.loads(path.read_text())
    assert p.get('approved'), 'Main-reader approval is required.'
    assert (OUT/'pages'/f'148_scan{scan:03d}.tex').exists()
    wanted=[r['id'] for r in csv.DictReader((ROOT/'source/SP82_C13_148_texts/MARKS.tsv').open(),delimiter='\t') if int(r['scan'])==scan]
    got=[r['id'] for r in p['decisions']]
    assert len(got)==len(set(got)) and set(got)==set(wanted),(scan,'mark coverage',set(wanted)-set(got),set(got)-set(wanted))
    for r in p['decisions']:
        if r['decision']!='undecided':assert r.get('crop')!='page' and r.get('box'),(r['id'],'resolved mark without crop')
    rebuild()
    crops=list((OUT/'crops').glob(f'148_scan{scan:03d}_*.png'))
    with (OUT/'progress.log').open('a') as f:f.write(f'scan {scan:03d} done {now()} cote 148: {p["lines_read"]} lines read, {len(crops)} places cropped, {len(p["changes"])} rows\n')

def second_files(scan):
    p=json.loads((OUT/'reviews'/f'148_scan{scan:03d}.json').read_text())
    boxes=p['second_boxes'];assert len({r['box'] for r in boxes})==len(boxes)
    write_tsv(OUT/'second'/f'148_scan{scan:03d}_boxes.tsv',['box','kind','x0','y0','x1','y1'],boxes)
    write_tsv(OUT/'second'/f'148_scan{scan:03d}_first.tsv',['box','reading'],boxes)

def tokenise(s): return re.findall(r'\\[A-Za-z]+|\\.|[A-Za-zÀ-ÿ]+|[0-9]+|[^\s]',s)
def compare(scan):
    base=OUT/'second'/f'148_scan{scan:03d}'
    first=list(csv.DictReader(Path(str(base)+'_first.tsv').open(),delimiter='\t'))
    second={r['box']:r['reading'] for r in csv.DictReader(Path(str(base)+'_second.tsv').open(),delimiter='\t')}
    assert set(r['box'] for r in first)==set(second),'Second reading coverage mismatch'
    out=[]
    for r in first:
        s=second[r['box']];out.append(dict(box=r['box'],first=r['reading'],second=s,different='yes' if tokenise(r['reading'])!=tokenise(s) else 'no'))
    write_tsv(Path(str(base)+'_comparison.tsv'),['box','first','second','different'],out)
    print(json.dumps({'scan':scan,'boxes':len(out),'differences':sum(r['different']=='yes' for r in out)},ensure_ascii=False))

def package(target):
    with zipfile.ZipFile(target,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(OUT.rglob('*')):
            if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.zip' and not (p.suffix.lower() in ('.jpg','.jpeg') and ('readers' in p.parts or 'previews' in p.parts or 'halves' in p.parts)):
                z.write(p,p.relative_to(OUT))
    print(str(target))

def freeze():
    paths=[OUT/'pages'/f'148_scan{scan:03d}.tex' for scan in SCANS]+[OUT/f'{PREFIX}_transcription.tex']
    assert all(p.exists() for p in paths),'Cannot freeze an incomplete transcription.'
    hashes={str(p.relative_to(OUT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
    (OUT/'transcription_hashes.json').write_text(json.dumps(hashes,indent=2)+'\n')
    with (OUT/'progress.log').open('a') as f:
        f.write('transcription frozen '+now()+'\n')
        for name,sha in hashes.items():f.write('SHA-256 '+sha+' '+name+'\n')
    print('Frozen '+str(len(paths))+' transcription files.')

def verify_frozen():
    hashes=json.loads((OUT/'transcription_hashes.json').read_text())
    for name,sha in hashes.items():assert hashlib.sha256((OUT/name).read_bytes()).hexdigest()==sha,('Frozen transcription changed',name)
    with (OUT/'progress.log').open('a') as f:f.write('frozen hashes verified unchanged '+now()+f': {len(hashes)} files\n')
    print('All frozen transcription hashes unchanged.')

if __name__=='__main__':
    op=sys.argv[1]
    if op=='rebuild':rebuild()
    elif op=='accept':accept(int(sys.argv[2]))
    elif op=='second':second_files(int(sys.argv[2]))
    elif op=='compare':compare(int(sys.argv[2]))
    elif op=='package':package(Path(sys.argv[2]))
    elif op=='freeze':freeze()
    elif op=='verify-frozen':verify_frozen()
