#!/usr/bin/env python3
"""Assemble reviewed diplomatic edits. All matches are against immutable inputs."""
import argparse, collections, csv, difflib, hashlib, json, re, sys, zipfile
from datetime import datetime, timezone, timedelta
from pathlib import Path

OUT = Path(__file__).resolve().parents[1]
WORK = OUT.parent
SOURCE = WORK/'source'
FIELDS = ['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
EVENT_FIELDS = ['statement_id','date','who','type','outcome']

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def raw_text(path): return Path(path).read_bytes().decode('utf-8')
def read_rows(path):
    with Path(path).open(encoding='utf-8',newline='') as f: return list(csv.DictReader(f,delimiter='\t'))
def write_rows(path,fields,rows):
    with Path(path).open('w',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=fields,delimiter='\t',lineterminator='\n'); wr.writeheader(); wr.writerows(rows)
def key(r): return f"{r['cote']}_scan{int(r['scan']):03d}"
def source_rows(): return read_rows(SOURCE/'IM04_13-16_corrections.tsv')
def load_review(page): return json.loads((OUT/'reviews'/f'{page}.json').read_text())

def assemble(original,rows):
    edits=[]
    for r in rows:
        assert r['decision'] in 'abcd' and len(r['decision'])==1, r
        assert r['confidence'] in ['high','medium','low'], r
        if r['decision']!='a':
            assert not r.get('find') and not r.get('replace'), r['id']
            continue
        f,rep=r['find'],r['replace']
        assert f and original.count(f)==1,(r['id'],'find count',original.count(f))
        assert f!=rep,(r['id'],'empty edit')
        start=original.index(f)
        for tag,i,j,x,y in difflib.SequenceMatcher(None,f,rep,autojunk=False).get_opcodes():
            if tag!='equal': edits.append((start+i,start+j,rep[x:y],r['id']))
    dedup={}
    for a,b,s,id_ in edits:
        if (a,b,s) in dedup: dedup[(a,b,s)].append(id_)
        else: dedup[(a,b,s)]=[id_]
    ordered=sorted((a,b,s,ids) for (a,b,s),ids in dedup.items())
    for e1,e2 in zip(ordered,ordered[1:]):
        assert e1[1]<=e2[0] and not (e1[0]==e2[0] and (e1[1]==e1[0] or e2[1]==e2[0])),('overlapping edits',e1,e2)
    text=original
    for a,b,s,ids in reversed(ordered): text=text[:a]+s+text[b:]
    return text,ordered

def rebuild():
    accepted={}
    for p in (OUT/'reviews').glob('*.accepted.json'):
        d=json.loads(p.read_text()); accepted[d['page']]=d
    allrows=source_rows()
    placements=[]; notes=['# Notes on the correction decisions','','This is a diplomatic transcription. Authorial slips and proposed mathematical refinements are preserved. A visual collation is not a mathematical re-proof.','','The supplied table has 81 row occurrences and 77 distinct ids. Repeated ids are retained separately by cote and scan, in the original table order. The exact find/replace fields in placements.tsv are quoted TSV fields and may contain embedded CRLF line breaks; they must be read with a TSV parser. The edited pages preserve their original CRLF convention.','']
    notes += ['## Authorial slips or mathematical refinements (b)','']
    decided={(d['page'],r['id']):r for d in accepted.values() for r in d['rows']}
    for src in allrows:
        if (key(src),src['id']) not in decided: continue
        r=decided[(key(src),src['id'])]
        placements.append({**{k:src[k] for k in ['id','cote','scan']},**{k:r[k] for k in FIELDS if k not in ['id','cote','scan']}})
        if r['decision']=='b': notes += [f"### {r['id']} — cote {src['cote']}, scan {int(src['scan']):03d}",'',r.get('note',''),'',r['what_the_ink_shows'],'']
    notes += ['## Statements absent from the assigned page (d)','']
    for src in allrows:
        r=decided.get((key(src),src['id']))
        if r and r['decision']=='d': notes += [f"### {r['id']} — cote {src['cote']}, scan {int(src['scan']):03d}",'',r.get('note',''),'',r['what_the_ink_shows'],'']
    notes += ['## Readings the ink did not settle','']
    unsure=[]
    for src in allrows:
        r=decided.get((key(src),src['id']))
        if r and (r.get('unsettled') or r['confidence']=='low'):
            unsure += [f"### {r['id']} — cote {src['cote']}, scan {int(src['scan']):03d}",'',r.get('uncertainty_note') or r.get('note',''),'',r['what_the_ink_shows'],'']
    notes += unsure or ['No unresolved reading has been recorded among the completed pages.','']
    write_rows(OUT/'placements.tsv',FIELDS,placements)
    (OUT/'notes.md').write_text('\n'.join(notes),encoding='utf-8')
    return accepted,decided

def commit(page,root_note):
    assert root_note.strip(),'main-reader review note required'
    accepted_path=OUT/'reviews'/f'{page}.accepted.json'
    assert not accepted_path.exists(),'page already committed'
    d=load_review(page)
    src=[r for r in source_rows() if key(r)==page]
    assert d['page']==page
    assert [r['id'] for r in d['rows']]==[r['id'] for r in src], 'row order or coverage mismatch'
    original=raw_text(SOURCE/'IM04_13-16_pages'/f'{page}.tex')
    final,edits=assemble(original,d['rows'])
    candidate=OUT/'reviews'/f'{page}.candidate.tex'
    assert raw_text(candidate)==final, 'candidate contains undocumented edits or is stale'
    for r in d['rows']:
        for crop in r.get('crops',[]): assert (OUT/crop).is_file(),crop
        assert r['what_the_ink_shows'].strip(),r['id']
        if r['decision'] in 'bd': assert r.get('note','').strip(),r['id']
    ts=now()
    d.update({'approved_utc':ts,'main_reader_review':root_note,'original_sha256':hashlib.sha256(original.encode()).hexdigest(),'edited_sha256':hashlib.sha256(final.encode()).hexdigest(),'minimal_edit_count':len(edits)})
    accepted_path.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    (OUT/'edited_pages'/f'{page}.tex').write_bytes(final.encode('utf-8'))
    rebuild()
    with (OUT/'CHECK_EVENTS.tsv').open('a',encoding='utf-8',newline='') as f:
        wr=csv.DictWriter(f,fieldnames=EVENT_FIELDS,delimiter='\t',lineterminator='\n')
        for r in d['rows']:
            wr.writerow({'statement_id':r['id'],'date':ts,'who':f"GPT-6 Astra Pro; effort runtime setting not exposed; run {d.get('reader','page-reader')}/{page}",'type':r.get('event_type','used and rechecked in this run'),'outcome':r.get('event_outcome','Visual collation against the supplied manuscript image: '+r['what_the_ink_shows'])})
            for ev in r.get('additional_events',[]):
                wr.writerow({'statement_id':r['id'],'date':ts,'who':ev.get('who',f"GPT-6 Astra Pro; effort runtime setting not exposed; run {d.get('reader','page-reader')}/{page}"),'type':ev['type'],'outcome':ev['outcome']})
            wr.writerow({'statement_id':r['id'],'date':ts,'who':f'GPT-6 Astra Pro; effort runtime setting not exposed; run main-reader/{page}','type':'used and rechecked in this run','outcome':f"Main-reader review: decision {r['decision']}. {root_note} Exact original-span uniqueness and complete candidate reconstruction verified; no undocumented edits."})
    with (OUT/'progress.log').open('a',encoding='utf-8') as f: f.write(f"scan {int(src[0]['scan']):03d} done {ts} cote {src[0]['cote']}\n")
    print(json.dumps({'page':page,'rows':[r['id']+':'+r['decision'] for r in d['rows']],'minimal_edits':len(edits),'time':ts}))

def audit(final=False):
    accepted,decided=rebuild()
    expected=source_rows()
    source_pages=list(dict.fromkeys(key(r) for r in expected))
    manifest=json.loads((OUT/'reviews/input_sha256.json').read_text())
    for rel,digest in manifest.items():
        assert hashlib.sha256((SOURCE/rel).read_bytes()).hexdigest()==digest,('changed input',rel)
    placements=read_rows(OUT/'placements.tsv')
    expected_completed=[r for r in expected if key(r) in accepted]
    assert [(r['id'],key(r)) for r in placements]==[(r['id'],key(r)) for r in expected_completed], 'placement row order or identity mismatch'
    assert list(placements[0])==FIELDS if placements else True
    for page,d in accepted.items():
        original=raw_text(SOURCE/'IM04_13-16_pages'/f'{page}.tex')
        text,edits=assemble(original,d['rows'])
        assert raw_text(OUT/'edited_pages'/f'{page}.tex')==text,page
        published=[r for r in placements if key(r)==page]
        reconstructed,_=assemble(original,published)
        assert reconstructed==text,('published placement reconstruction',page)
        assert raw_text(OUT/'reviews'/f'{page}.candidate.tex')==text,('candidate mismatch',page)
        assert hashlib.sha256(original.encode()).hexdigest()==d['original_sha256'],page
        assert hashlib.sha256(text.encode()).hexdigest()==d['edited_sha256'],page
        if '\r\n' in original and '\n' not in original.replace('\r\n',''):
            assert '\n' not in text.replace('\r\n',''),('line ending change',page)
        for r in d['rows']:
            for crop in r.get('crops',[]):
                assert (OUT/crop).is_file(),crop
                assert (OUT/crop).with_suffix('.crop.json').is_file(),('crop provenance missing',crop)
    events=read_rows(OUT/'CHECK_EVENTS.tsv')
    allowed_types={'targeted proof check','independent re-proof','computation or formal certificate','used and rechecked in this run','carried as background without fault found'}
    assert all(e['type'] in allowed_types or e['type'].startswith('refuted,') for e in events),'invalid event type'
    for page,id_ in decided:
        own=[e for e in events if e['statement_id']==id_ and e['who'].endswith('/'+page)]
        assert len(own)>=2,(page,id_,'missing reader/main check events')
        assert sum('run main-reader/' in e['who'] for e in own)==1,(page,id_,'main event count')
    lines=(OUT/'progress.log').read_text().splitlines()
    datetime.fromisoformat(lines[0].replace('Z','+00:00'))
    logged={}
    for line in lines[1:]:
        m=re.fullmatch(r'scan (\d{3}) done (\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}Z) cote (\d+)',line)
        assert m,('bad progress line',line)
        pg=f'{m[3]}_scan{m[1]}'
        assert pg not in logged,('duplicate done line',pg)
        logged[pg]=m[2]
    assert set(logged)==set(accepted),'progress/page coverage mismatch'
    assert all(logged[pg]==d['approved_utc'] for pg,d in accepted.items()),'progress timestamp mismatch'
    queue=json.loads((OUT/'reviews/queue.json').read_text())
    assert [a['page'] for a in queue['assignments']]==source_pages[:len(queue['assignments'])],'dispatch order mismatch'
    result={'completed_pages':len(accepted),'expected_pages':len(source_pages),'completed_rows':len(decided),'expected_rows':len(expected),'distinct_input_ids':len(set(r['id'] for r in expected)),'decision_counts':dict(collections.Counter(r['decision'] for r in decided.values())),'changed_pages':sum(d['original_sha256']!=d['edited_sha256'] for d in accepted.values()),'check_events':len(events),'crop_count':len(list((OUT/'crops').glob('*.jpg'))),'remaining_pages':[p for p in source_pages if p not in accepted]}
    if final:
        assert len(accepted)==len(source_pages) and len(decided)==len(expected),result
        assert set(p.stem for p in (OUT/'edited_pages').glob('*.tex'))==set(source_pages)
        assert [r['id'] for r in read_rows(OUT/'placements.tsv')]==[r['id'] for r in expected]
        done=[line for line in (OUT/'progress.log').read_text().splitlines() if ' done ' in line]
        assert len(done)==len(source_pages)
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return result

def package(destination,checkpoint=False):
    dest=Path(destination)
    assert not dest.exists(), 'never overwrite ZIPs'
    if checkpoint:
        first=(OUT/'progress.log').read_text().splitlines()[0]
        start=datetime.fromisoformat(first.replace('Z','+00:00'))
        receipts=sorted((WORK/'checkpoints').glob('*.receipt.json')) if (WORK/'checkpoints').exists() else []
        due=start+timedelta(minutes=45*(len(receipts)+1))
        assert datetime.now(timezone.utc)>=due, f'checkpoint not due until {due.isoformat()}'
    dest.parent.mkdir(parents=True,exist_ok=True)
    with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(OUT.rglob('*')):
            if p.is_file() and p.suffix!='.zip' and '__pycache__' not in p.parts: z.write(p,p.relative_to(OUT))
    print(json.dumps({'zip':str(dest),'size':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),'created_utc':now()}))

if __name__=='__main__':
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest='command',required=True)
    c=sub.add_parser('commit'); c.add_argument('page');c.add_argument('--review',required=True)
    a=sub.add_parser('audit');a.add_argument('--final',action='store_true')
    z=sub.add_parser('package');z.add_argument('destination');z.add_argument('--checkpoint',action='store_true')
    args=p.parse_args()
    if args.command=='commit':commit(args.page,args.review)
    elif args.command=='audit':audit(args.final)
    elif args.command=='package':package(args.destination,args.checkpoint)
