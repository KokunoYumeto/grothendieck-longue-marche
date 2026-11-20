#!/usr/bin/env python3
"""Exact-span validation and main-reader acceptance of single-page decisions.
Run from the IM02_work directory; source/ is the original, once-unpacked input.
Image reading and editorial acceptance are performed by the main reader, not this script.
"""
from pathlib import Path
import argparse,csv,json,collections,difflib,hashlib
from datetime import datetime,timezone
W=Path(__file__).resolve().parents[2]
D=W/'deliverables'
FIELDS=['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
EVENT_FIELDS=['statement_id','date','who','type','outcome']

def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def source_rows():
    with (W/'source/IM02_6-9_corrections.tsv').open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))
def key(r): return (str(r['id']),str(r['cote']),str(int(r['scan'])))
def pagename(r): return f"{r['cote']}_scan{int(r['scan']):03d}"
def write_tsv(path,fields,rows):
    with path.open('w',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=fields,delimiter='\t',extrasaction='ignore')
        writer.writeheader();writer.writerows(rows)
def inspect(page,report_path=None):
    rp=Path(report_path) if report_path else W/'reviews'/f'{page}.json'
    report=json.loads(rp.read_text())
    original=(W/'source/IM02_6-9_pages'/f'{page}.tex').read_bytes().decode('utf-8')
    wanted=[r for r in source_rows() if pagename(r)==page]
    assert [key(r) for r in report['rows']]==[key(r) for r in wanted], 'Report rows/order differ from supplied page rows'
    patches=[]
    for row in report['rows']:
        assert row['decision'] in 'abcd' and len(row['decision'])==1, row
        assert row['confidence'] in ['high','medium','low'], row
        if row['decision']=='a':
            find,replace=row['find'],row['replace']
            assert find and find!=replace, f"Empty/unchanged patch {row['id']}"
            assert original.count(find)==1, f"Not unique original span {row['id']}: {original.count(find)}"
            start=original.index(find)
            patches.append((start,start+len(find),replace,row['id']))
        else:
            assert not row.get('find') and not row.get('replace'), f"Unexpected edit in {row['decision']} row"
        assert row.get('what_the_ink_shows'), f"Missing observation {row['id']}"
        for event in row.get('events',[]):
            assert all(event.get(x) for x in ['date','who','type','outcome'])
    patches.sort()
    for p,q in zip(patches,patches[1:]):
        assert p[1]<=q[0],f'Overlapping patches {p[3]} / {q[3]}'
    edited=original
    for start,end,replace,_ in reversed(patches):edited=edited[:start]+replace+edited[end:]
    proposed=rp.with_name(rp.stem+'.proposed.tex')
    if proposed.exists(): assert edited==proposed.read_bytes().decode('utf-8'), 'Proposed file contains unrecorded/different edits'
    for crop in report.get('crops',[]):
        assert crop.startswith('crops/') and (D/crop).is_file(),f'Missing crop {crop}'
    return report,original,edited

def rebuild():
    accepted={}
    reports=[]
    for path in sorted((D/'reviews').glob('*.json')):
        report=json.loads(path.read_text());reports.append(report)
        for row in report['rows']:
            assert key(row) not in accepted
            accepted[key(row)]=row
    ordered=[accepted[key(r)] for r in source_rows() if key(r) in accepted]
    write_tsv(D/'placements.tsv',FIELDS,ordered)
    events=[]
    for row in ordered:
        for event in row.get('events',[]):
            events.append(dict(statement_id=row['id'],**event))
    write_tsv(D/'CHECK_EVENTS.tsv',EVENT_FIELDS,events)
    text=['# IM02_6-9 — decisions requiring notes','',
          'Mathematical refinements recorded below are supplied by the corrections table. This run checks their relation to the manuscript; it does not claim an independent proof of those refinements.','']
    for heading,condition in [
        ('(b) Authorial wording or mathematical refinements',lambda r:r['decision']=='b'),
        ('(d) Not at the stated place',lambda r:r['decision']=='d'),
        ('Readings left uncertain',lambda r:r.get('unsettled',False)),
        ('Other material editorial observations',lambda r:r['decision'] in ['a','c'] and not r.get('unsettled',False) and r.get('note'))]:
        selected=[r for r in ordered if condition(r)]
        text += ['## '+heading,'']
        if not selected:text += ['None among the completed pages.','']
        for r in selected:
            text += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}",'',r.get('note') or r['what_the_ink_shows'],'',
                     '**Manuscript evidence:** '+r['what_the_ink_shows'],'']
    (D/'notes.md').write_text('\n'.join(text))
    return len(reports),len(ordered),dict(collections.Counter(r['decision'] for r in ordered))

def accept(page,root_note):
    report,original,edited=inspect(page)
    out=D/'reviews'/f'{page}.json';out.parent.mkdir(exist_ok=True)
    assert not out.exists(), 'Already accepted; explicit revision required'
    dt=now()
    report['main_review']={'date':dt,'who':'GPT-6 Astra Pro; effort not exposed; main reader; run IM02_6-9_20261120','outcome':root_note,'original_sha256':hashlib.sha256(original.encode()).hexdigest(),'edited_sha256':hashlib.sha256(edited.encode()).hexdigest()}
    for row in report['rows']:
        row.setdefault('events',[]).append({'date':dt,'who':report['main_review']['who'],'type':'used and rechecked in this run','outcome':f"Cote {row['cote']}, scan {int(row['scan']):03d}: main reader reviewed the returned decision and cited visual evidence; verified every replacement is an exact, unique original span and all changes are confined to recorded row loci. {root_note}"})
    (D/'edited_pages'/f'{page}.tex').write_bytes(edited.encode('utf-8'))
    out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
    counts=rebuild()
    c,s=page.split('_scan')
    with (D/'progress.log').open('a') as f:f.write(f'scan {s} done {dt} cote {c}\n')
    print(json.dumps({'accepted':page,'pages':counts[0],'rows':counts[1],'decisions':counts[2]}))

def status():
    reports=list((D/'reviews').glob('*.json')) if (D/'reviews').exists() else []
    rows=[r for p in reports for r in json.loads(p.read_text())['rows']]
    start=datetime.strptime((D/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
    elapsed=(datetime.now(timezone.utc)-start).total_seconds()
    print(json.dumps({'utc':now(),'elapsed_minutes':round(elapsed/60,1),'completed_pages':len(reports),'completed_rows':len(rows),'decisions':dict(collections.Counter(r['decision'] for r in rows)),'unaccepted_reports':[p.stem for p in (W/'reviews').glob('*.json') if not (D/'reviews'/p.name).exists()]},ensure_ascii=False))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('action',choices=['inspect','accept','status','rebuild']);parser.add_argument('page',nargs='?');parser.add_argument('--note',default='')
    args=parser.parse_args()
    if args.action=='status':status()
    elif args.action=='rebuild':print(rebuild())
    elif args.action=='accept':
        assert args.note,'Record the main reader visual review before accepting';accept(args.page,args.note)
    else:
        report,original,edited=inspect(args.page)
        print(json.dumps(report,ensure_ascii=False,indent=2))
        print(''.join(difflib.unified_diff(original.splitlines(True),edited.splitlines(True),fromfile=args.page+' original',tofile=args.page+' proposed')))
