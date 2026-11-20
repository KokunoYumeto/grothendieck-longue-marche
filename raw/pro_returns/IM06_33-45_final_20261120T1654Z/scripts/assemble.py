#!/usr/bin/env python3
"""Validate exact original spans, commit reviewed pages, and assemble deliverables.

No OCR or recognition. Input files are read as bytes to retain their newlines.
Only the main reader runs `approve`, after inspecting the reader's proposal.
"""
from pathlib import Path
from datetime import datetime, timezone
import argparse, csv, hashlib, json, collections, zipfile

ROOT = Path(__file__).resolve().parents[1]
FIELDS = ['id', 'cote', 'scan', 'decision', 'find', 'replace', 'what_the_ink_shows', 'confidence']
EVENT_FIELDS = ['statement_id', 'date', 'who', 'type', 'outcome']

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def inputs():
    with (ROOT/'source/IM06_33-45_corrections.tsv').open(encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def page_of(r):
    return f"{r['cote']}_scan{int(r['scan']):03d}"

def exact_result(page, review):
    original = (ROOT/'source/IM06_33-45_pages'/f'{page}.tex').read_bytes().decode('utf-8')
    expected = [r for r in inputs() if page_of(r) == page]
    assert review['page'] == page
    assert [(r['id'],str(r['cote']),int(r['scan'])) for r in review['rows']] == [(r['id'],r['cote'],int(r['scan'])) for r in expected], 'Row identity/order mismatch'
    patches = {}
    for r in review['rows']:
        assert r['decision'] in 'abcd' and len(r['decision']) == 1
        assert r['confidence'] in ('high','medium','low')
        assert r.get('what_the_ink_shows'), 'Missing ink evidence'
        assert r.get('events'), 'Missing reading check event'
        if r['decision'] == 'a':
            old, new = r['find'], r['replace']
            assert old and old != new, ('Empty/no-op patch',r['id'])
            assert original.count(old) == 1, ('Find is not unique in original',page,r['id'],original.count(old))
            a = original.index(old)
            interval = (a,a+len(old))
            if interval in patches:
                assert patches[interval] == new, 'Duplicate location disagrees'
            else:
                for x,y in patches:
                    assert interval[1] <= x or interval[0] >= y, ('Overlapping row spans',page,r['id'])
                patches[interval] = new
        else:
            assert not r.get('find') and not r.get('replace'), ('Non-a row has edit',page,r['id'])
    result = original
    for (a,b),new in sorted(patches.items(), reverse=True):
        result = result[:a]+new+result[b:]
    for crop in review.get('crops',[]):
        p = crop['path'] if isinstance(crop,dict) else crop
        assert p.startswith('crops/') and (ROOT/p).is_file(), ('Missing crop',p)
    return result.encode('utf-8'), len(patches)

def write_tsv(path, fields, rows):
    with path.open('w', encoding='utf-8', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n', extrasaction='ignore')
        writer.writeheader()
        writer.writerows(rows)

def rebuild():
    supplied = {(r['id'],r['cote'],int(r['scan'])):r for r in inputs()}
    approved = {}
    for p in (ROOT/'approved').glob('*.json'):
        j=json.loads(p.read_text(encoding='utf-8'))
        approved[j['page']]=j
    rows=[]
    for page in dict.fromkeys(page_of(r) for r in inputs()):
        if page in approved:
            rows.extend(approved[page]['rows'])
    write_tsv(ROOT/'placements.tsv',FIELDS,rows)
    events=[]
    for r in rows:
        for e in r.get('events',[]):
            events.append(dict(statement_id=r['id'], **e))
    write_tsv(ROOT/'CHECK_EVENTS.tsv',EVENT_FIELDS,events)
    note = ['# Notes on the diplomatic corrections', '',
        'Decisions concern the supplied page and its ink. Mathematical corrections or refinements below are recorded from the supplied correction rows; they are not silently incorporated into the transcription. The visual checks and exact-span checks recorded in CHECK_EVENTS.tsv are not independent proofs of those mathematical claims.', '',
        'Every source row is retained in its original order, including L609 on both 36/014 and 36/016, and the two reports Q100034 and Qsow034 concerning the same occurrence on 36/013. Each is identified by its statement ID together with cote and scan.', '',
        'For category (c) rows whose ink remains unsettled, the proposed reading is already represented by the existing doubt marker or by the surviving text after a recorded cancellation. Such a decision preserves the uncertainty; it does not certify a bare, normalized reading. These cases are identified individually below.', '',
        '## (b) Authorial slips or mathematical refinements — text preserved', '']
    for r in rows:
        if r['decision']=='b':
            src=supplied[(r['id'],str(r['cote']),int(r['scan']))]
            note.extend([f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}", '', r.get('note',''), '', r['what_the_ink_shows'], '', 'Supplied proposed correction/refinement (recorded from the correction table):', '', src['should_read'], ''])
    if not any(r['decision']=='b' for r in rows): note.extend(['None recorded so far.',''])
    note.extend(['## (d) Rows whose place is not on the supplied page',''])
    for r in rows:
        if r['decision']=='d':
            note.extend([f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}", '', r.get('note',''), '', r['what_the_ink_shows'], ''])
    if not any(r['decision']=='d' for r in rows): note.extend(['None.',''])
    note.extend(['## Readings the available ink does not settle',''])
    doubts=[r for r in rows if r.get('unresolved')]
    for r in doubts:
        note.extend([f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}", '', r.get('note',''), '', r['what_the_ink_shows'], ''])
    if not doubts: note.extend(['None recorded so far.',''])
    others=[r for r in rows if r['decision'] in ('a','c') and r.get('note') and not r.get('unresolved')]
    if others:
        note.extend(['## Other row-specific editorial notes',''])
        for r in others:
            note.extend([f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d} (decision {r['decision']})", '', r['note'], ''])
    (ROOT/'notes.md').write_text('\n'.join(note)+'\n',encoding='utf-8')
    return rows,approved

def approve(page, main_note):
    review=json.loads((ROOT/'reviews'/f'{page}.json').read_text(encoding='utf-8'))
    result,n=exact_result(page,review)
    candidate=ROOT/'reviews'/f'{page}.candidate.tex'
    assert candidate.exists() and candidate.read_bytes()==result, 'Candidate differs from documented exact patches'
    (ROOT/'approved').mkdir(exist_ok=True)
    assert not (ROOT/'approved'/f'{page}.json').exists(), 'Already approved; revise explicitly instead'
    stamp=utc()
    for r in review['rows']:
        r['events'].append({'date':stamp,'who':'GPT-6 Astra Pro; effort not exposed; main reader; run IM06_33-45_20261120',
                           'type':'used and rechecked in this run',
                           'outcome':f"{page}: main reader inspected the returned ink crop(s), compared the proposed decision with the original text and row, and checked the unique original span and absence of other edits. Decision {r['decision']}. {main_note}"})
    review['main_reviewed_utc']=stamp
    review['main_review_note']=main_note
    (ROOT/'edited_pages'/f'{page}.tex').write_bytes(result)
    (ROOT/'approved'/f'{page}.json').write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    rows,approved=rebuild()
    first=review['rows'][0]
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f"scan {int(first['scan']):03d} done {utc()} cote {first['cote']}\n")
    print(json.dumps({'approved':page,'unique_patches':n,'pages_done':len(approved),'rows_done':len(rows),'decisions':{r['id']:r['decision'] for r in review['rows']}},ensure_ascii=False))

def validate(complete=False):
    with (ROOT/'source_sha256.tsv').open(encoding='utf-8',newline='') as f:
        hashes=list(csv.DictReader(f,delimiter='\t'))
    for h in hashes:
        source=ROOT/'source'/h['file']
        assert source.is_file(), ('Missing original input',h['file'])
        assert hashlib.sha256(source.read_bytes()).hexdigest()==h['sha256'], ('Original input changed',h['file'])
    rows,approved=rebuild()
    patches=0
    for page,review in approved.items():
        expected,n=exact_result(page,review)
        assert (ROOT/'edited_pages'/f'{page}.tex').read_bytes()==expected, ('Unexpected change',page)
        assert not review.get('open_questions'), ('Unresolved main-reader disposition',page)
        patches+=n
    assert {p.stem for p in (ROOT/'edited_pages').glob('*.tex')}==set(approved)
    if complete:
        assert len(rows)==len(inputs())==71
        assert len(approved)==len(set(page_of(r) for r in inputs()))==58
        assert [(r['id'],str(r['cote']),int(r['scan'])) for r in rows]==[(r['id'],r['cote'],int(r['scan'])) for r in inputs()]
        lines=(ROOT/'progress.log').read_text().splitlines()
        assert len([x for x in lines if x.startswith('scan ')])==58
    result={'pages':len(approved),'rows':len(rows),'decisions':dict(collections.Counter(r['decision'] for r in rows)),
            'unique_patches':patches,'unresolved':[f"{r['id']} {page_of(r)}" for r in rows if r.get('unresolved')],
            'events':sum(len(r.get('events',[])) for r in rows),'source_files_hash_verified':len(hashes),'validated_utc':utc()}
    (ROOT/'validation.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False))

def package(path, final=False):
    validate(complete=final)
    dest=Path(path)
    assert not dest.exists(), 'Refusing to overwrite archive'
    allowed_dirs=['edited_pages','crops','reviews','approved','scripts']
    allowed_files=['placements.tsv','CHECK_EVENTS.tsv','progress.log','notes.md','dispatch.tsv','page_order.txt','validation.json','source_sha256.tsv']
    with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for name in allowed_files:
            p=ROOT/name
            if p.exists():z.write(p,p.relative_to(ROOT).as_posix())
        for directory in allowed_dirs:
            for p in sorted((ROOT/directory).rglob('*')):
                if p.is_file() and '__pycache__' not in p.parts:
                    z.write(p,p.relative_to(ROOT).as_posix())
    print(json.dumps({'archive':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest()}))

def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='action',required=True)
    a=sub.add_parser('approve');a.add_argument('page');a.add_argument('--note',default='')
    a=sub.add_parser('validate');a.add_argument('--complete',action='store_true')
    a=sub.add_parser('package');a.add_argument('path');a.add_argument('--final',action='store_true')
    args=p.parse_args()
    if args.action=='approve':approve(args.page,args.note)
    elif args.action=='validate':validate(args.complete)
    elif args.action=='package':package(args.path,args.final)

if __name__=='__main__':main()
