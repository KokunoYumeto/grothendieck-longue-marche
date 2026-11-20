#!/usr/bin/env python3
"""Exact-span audit, atomic page commit, ordered ledgers, and checkpoint packaging.

No OCR and no inference of readings is performed here. All decisions must be
visually/readingly reviewed by the main reader before the explicit commit call.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv, json, hashlib, sys, re, zipfile

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'source'
FIELDS = ['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
EVENT_FIELDS = ['statement_id','date','who','type','outcome']
TYPES = {'targeted proof check','independent re-proof','computation or formal certificate',
         'used and rechecked in this run','carried as background without fault found',
         "refuted, with the refined statement's id"}

def utc():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def original_rows():
    with (SOURCE/'IM21_1-133_corrections.tsv').open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def atomic_text(path, text):
    tmp=path.with_suffix(path.suffix+'.tmp')
    tmp.write_text(text,encoding='utf-8')
    tmp.replace(path)

def write_tsv(path, fields, rows):
    import io
    s=io.StringIO(newline='')
    w=csv.DictWriter(s,fieldnames=fields,delimiter='\t',lineterminator='\n',extrasaction='ignore')
    w.writeheader();w.writerows(rows)
    atomic_text(path,s.getvalue())

def page_data(key):
    return json.loads((ROOT/'page_packets'/f'{key}.json').read_text())

def validate(key):
    packet=page_data(key)
    original=Path(packet['source_tex_path']).read_bytes().decode('utf-8')
    assert packet['latex']==original.replace('\r\n','\n'), 'Packet differs from original'
    proposal=json.loads((ROOT/'proposals'/f'{key}.json').read_text())
    assert proposal['page_key']==key
    expected=[r['id'] for r in packet['rows']]
    got=[r['id'] for r in proposal['rows']]
    assert got==expected, f'Row IDs/order mismatch: {got} != {expected}'
    spans=[]
    for r in proposal['rows']:
        # Page packets use universal-newline text for reading. Restore the source
        # CRLF convention in exact-span records and output bytes before applying.
        if '\r\n' in original:
            assert '\n' not in original.replace('\r\n',''), 'Mixed source line endings require explicit review'
            for field in ('find','replace'):
                r[field]=r.get(field,'').replace('\r\n','\n').replace('\n','\r\n')
        assert r['decision'] in 'abcd' and len(r['decision'])==1
        assert r['confidence'] in {'high','medium','low'}
        assert r.get('event_type') in TYPES, (r['id'],'missing/invalid event type')
        assert r.get('event_outcome'), (r['id'],'missing event outcome')
        if r['decision']=='a':
            f=r['find'];v=r['replace']
            assert f and f!=v, (r['id'],'empty/no-op edit')
            assert original.count(f)==1, (r['id'],'original span count',original.count(f))
            p=original.index(f)
            spans.append((p,p+len(f),v,r['id']))
        else:
            assert not r.get('find') and not r.get('replace'), (r['id'],'non-a edit')
        if r['decision'] in 'bd' or r['confidence']=='low':
            assert r.get('note'), (r['id'],'note required')
        for crop in re.findall(r'crops/[A-Za-z0-9_.-]+\.(?:jpg|jpeg|png)',r.get('what_the_ink_shows','')):
            assert (ROOT/crop).is_file(), (r['id'],'missing crop',crop)
    unique=[]
    for span in sorted(spans):
        if unique and span[:3]==unique[-1][:3]:
            continue
        if unique:
            assert unique[-1][1]<=span[0], ('overlapping edits',unique[-1][3],span[3])
        unique.append(span)
    edited=original
    for start,end,replacement,_ in reversed(unique):
        edited=edited[:start]+replacement+edited[end:]
    assert not proposal.get('unresolved'), 'Main reader must decide every unresolved row'
    return packet,proposal,original,edited,unique

def rebuild():
    records=[]
    for p in (ROOT/'review_records').glob('*.json'):
        records.append(json.loads(p.read_text()))
    records.sort(key=lambda r:r['page_index'])
    byid={}
    for rec in records:
        for row in rec['rows']:
            identity=(row['id'],row['cote'],row['scan'])
            assert identity not in byid
            byid[identity]=row
    # Statement IDs recur on different pages in the supplied table. They are
    # preserved verbatim; row identity includes cote and scan, never ID alone.
    supplied_rows=original_rows()
    supplied_by_identity={(r['id'],r['cote'],r['scan']):r for r in supplied_rows}
    ordered=[byid[(r['id'],r['cote'],r['scan'])] for r in supplied_rows
             if (r['id'],r['cote'],r['scan']) in byid]
    write_tsv(ROOT/'placements.tsv',FIELDS,ordered)
    events=[event for rec in records for event in rec['events']]
    write_tsv(ROOT/'CHECK_EVENTS.tsv',EVENT_FIELDS,events)
    text=['# Diplomatic transcription decisions','',
          'These notes cover only the supplied correction rows. Visual transcription checks do not certify the mathematical assertions. '+
          'Authorial slips and mathematical refinements remain in the transcription when the ink agrees with the supplied page.','',
          'Statements that another page was not inspected describe the individual page-reader assignment. Separate supplied occurrences have their own records; the main review events state any additional cross-page inspection.','',
          'An empty alternative after the separator in \\unsure{reading|} means no transcribed mark. It is used only at supplied targets where writing versus surface matter remains unresolved.','']
    for rec in records:
        noteworthy=[r for r in rec['rows'] if r.get('note') and (r['decision'] in 'abd' or r['confidence']=='low' or r.get('unsettled') or r.get('include_note'))]
        if noteworthy:
            text += [f"## Cote {rec['cote']}, scan {int(rec['scan']):03d}",'']
            for row in noteworthy:
                text += [f"### {row['id']} — decision {row['decision']} ({row['confidence']} confidence)",'',row['note'],'']
                supplied=supplied_by_identity[(row['id'],row['cote'],row['scan'])]
                if (row['decision']=='b' or row.get('include_note')) and supplied.get('should_read'):
                    text += ['Proposed correction in the supplied row (recorded as supplied, not independently proved):', '', '> '+supplied['should_read'].replace('\n','\n> '), '']
    atomic_text(ROOT/'notes.md','\n'.join(text)+'\n')
    return len(records),len(ordered)

def commit(key,review_note):
    packet,proposal,original,edited,spans=validate(key)
    rp=ROOT/'review_records'/f'{key}.json'
    assert not rp.exists(), 'Already committed; amend explicitly if necessary'
    now=utc()
    read_at=datetime.fromtimestamp((ROOT/'proposals'/f'{key}.json').stat().st_mtime,timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
    rows=[];events=[]
    for source,row in zip(packet['rows'],proposal['rows']):
        r=dict(row,cote=source['cote'],scan=source['scan'])
        rows.append(r)
        location=f"Cote {r['cote']}, scan {int(r['scan']):03d}: "
        events.append(dict(statement_id=r['id'],date=read_at,who=proposal['reader'],type=r['event_type'],outcome=location+r['event_outcome']))
        events.append(dict(statement_id=r['id'],date=now,who='main reader; GPT-6 Astra Pro; effort inherited; run IM21-20261120',
                           type='used and rechecked in this run',outcome=location+review_note+' Exact original spans and unchanged surrounding source verified mechanically; no mathematical proof claimed.'))
    rec=dict(page_key=key,page_index=packet['page_index'],cote=packet['rows'][0]['cote'],scan=packet['rows'][0]['scan'],
             reviewed_at=now,review_note=review_note,source_sha256=hashlib.sha256(original.encode()).hexdigest(),
             edited_sha256=hashlib.sha256(edited.encode()).hexdigest(),rows=rows,events=events)
    atomic_text(ROOT/'edited_pages'/f'{key}.tex',edited)
    atomic_text(rp,json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
    pages,nrows=rebuild()
    with (ROOT/'progress.log').open('a') as f:
        f.write(f"scan {int(rec['scan']):03d} done {now} cote {rec['cote']}\n")
    print(json.dumps(dict(committed=key,pages_done=pages,rows_done=nrows,edits=len(spans),time=now)))

def status():
    order=(ROOT/'page_order.txt').read_text().splitlines()
    done={p.stem for p in (ROOT/'review_records').glob('*.json')}
    proposed={p.stem for p in (ROOT/'proposals').glob('*.json')}
    rows=list(csv.DictReader((ROOT/'placements.tsv').open(),delimiter='\t'))
    print(json.dumps(dict(time=utc(),pages_done=len(done),rows_done=len(rows),awaiting_review=[k for k in order if k in proposed-done],next_unproposed=[k for k in order if k not in proposed][:12]),ensure_ascii=False))

def package(path):
    target=Path(path).resolve()
    assert not target.exists(), 'Never overwrite an earlier ZIP'
    excluded={'page_packets','__pycache__'}
    members=[]
    for p in sorted(ROOT.rglob('*')):
        if p.is_file() and not any(part in excluded for part in p.relative_to(ROOT).parts) and p.suffix not in {'.zip','.tmp','.pyc'}:
            members.append(p)
    with zipfile.ZipFile(target,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in members:z.write(p,p.relative_to(ROOT))
    with zipfile.ZipFile(target) as z:
        assert z.testzip() is None
    print(json.dumps(dict(zip=str(target),files=len(members),size=target.stat().st_size,time=utc())))

if __name__=='__main__':
    cmd=sys.argv[1]
    if cmd=='status':status()
    elif cmd=='validate':
        p,r,o,e,s=validate(sys.argv[2]);print(json.dumps(dict(page=p['page_key'],rows=len(r['rows']),unique_edits=len(s),valid=True)))
    elif cmd=='commit':commit(sys.argv[2],sys.argv[3])
    elif cmd=='rebuild':print(rebuild())
    elif cmd=='package':package(sys.argv[2])
    else:raise SystemExit('Unknown command')
