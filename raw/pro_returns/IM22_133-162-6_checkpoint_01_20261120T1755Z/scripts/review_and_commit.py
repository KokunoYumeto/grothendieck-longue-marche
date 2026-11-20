"""Exact-span validation and main-reader commit, invoked after human/model review."""
from pathlib import Path
from datetime import datetime, timezone
import csv,json,sys,hashlib,difflib
W=Path(__file__).resolve().parents[1]
S=W.parent/'source'
PF=['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
EF=['statement_id','date','who','type','outcome']
def now(): return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
def load(stem):
    job=W/'page_jobs'/stem
    packet=json.loads((job/'input.json').read_text())
    result=json.loads((job/'result.json').read_text())
    original=Path(packet['latex_path']).read_bytes().decode('utf-8')
    assert result['stem']==stem
    assert [x['id'] for x in result['rows']]==[x['id'] for x in packet['rows']], 'Missing/reordered/extra rows'
    edits=[]
    for row,src in zip(result['rows'],packet['rows']):
        assert row['decision'] in 'abcd' and len(row['decision'])==1
        assert row['confidence'] in ('high','medium','low')
        assert row.get('events'), 'No actual check event recorded'
        if row['decision']=='a':
            f,r=row['find'],row['replace']
            # Reader text APIs may universal-newline-decode the CRLF source.
            # Restore the source convention in BOTH recorded spans, without
            # altering any source byte outside the correction.
            if '\r\n' in original and '\r' not in f:
                f=f.replace('\n','\r\n');r=r.replace('\n','\r\n')
                row['find'],row['replace']=f,r
            assert f and f!=r,(row['id'],'Empty or unchanged edit')
            assert original.count(f)==1,(row['id'],'Original find not unique',original.count(f))
            edit=(original.index(f),original.index(f)+len(f),f,r)
            if edit not in edits: edits.append(edit)
        else:
            assert not row.get('find') and not row.get('replace'),(row['id'],'Non-a edit')
        if row['decision'] in ('b','d'): assert row.get('note'),(row['id'],'Missing note')
        if row.get('checked_visually'):
            assert row.get('what_the_ink_shows'),(row['id'],'No optical account')
            assert row.get('crop') and (W/row['crop']).exists(),(row['id'],'Missing crop')
            refs=[row['crop']]+[x['crop'] if isinstance(x,dict) else x for x in row.get('additional_crops',[])]
            missing=[p for p in refs if p not in row['what_the_ink_shows']]
            if missing: row['what_the_ink_shows']+=' Crop reference(s): '+', '.join(missing)+'.'
        required=src['checked_on_scan']=='no' or any(k in src['kind'].lower() for k in ('flag','open','not sorted','second model'))
        if required: assert row.get('checked_visually'),(row['id'],'Mandatory image check absent')
    edits.sort()
    for a,b in zip(edits,edits[1:]): assert a[1]<=b[0],('Overlapping edits need reconciliation',stem,a,b)
    revised=original
    for start,end,f,r in reversed(edits): revised=revised[:start]+r+revised[end:]
    candidate=job/'candidate.tex'
    if candidate.exists(): assert candidate.read_text()==revised.replace('\r\n','\n'),'Candidate differs from exact placement edits'
    return packet,result,original,revised
def rebuild():
    source_rows=list(csv.DictReader((S/'IM22_133-162-6_corrections.tsv').open(),delimiter='\t'))
    source_by_key={(r['id'],r['cote'],r['scan']):r for r in source_rows}
    done={}
    events=[]; notes=[]
    for rev in sorted((W/'reviews').glob('*.json')):
        rec=json.loads(rev.read_text())
        for row in rec['rows']:
            done[(row['id'],row['cote'],row['scan'])]=row
            events.extend(row['all_events'])
            if row.get('note'):
                ink=('Written evidence: '+row['what_the_ink_shows']+'\n\n') if row.get('what_the_ink_shows') else ''
                key=(row['id'],row['cote'],row['scan'])
                proposed=('Supplied proposed correction or refinement (editorial note): '+source_by_key[key]['should_read']+'\n\n') if row['decision']=='b' else ''
                notes.append((key,f"### {row['id']} — cote {row['cote']}, scan {int(row['scan']):03d}; decision {row['decision']}\n\n{ink}{proposed}{row['note']}\n"))
    with (W/'placements.tsv').open('w',newline='') as f:
        cw=csv.DictWriter(f,fieldnames=PF,delimiter='\t');cw.writeheader()
        for r in source_rows:
            key=(r['id'],r['cote'],r['scan'])
            if key in done: cw.writerow({k:done[key].get(k,'') for k in PF})
    with (W/'CHECK_EVENTS.tsv').open('w',newline='') as f:
        cw=csv.DictWriter(f,fieldnames=EF,delimiter='\t');cw.writeheader()
        cw.writerows(events)
    note_map=dict(notes)
    preface='# Notes on diplomatic decisions\n\nThe transcription preserves the manuscript, including authorial slips. Mathematical explanations below distinguish the written text from the supplied proposed meaning; they are not claims of a fresh proof unless a check event explicitly says so. Crop references are relative to this archive. Doubt marks indicate unresolved ink.\n\n'
    (W/'notes.md').write_text(preface+'\n'.join(note_map[(r['id'],r['cote'],r['scan'])] for r in source_rows if (r['id'],r['cote'],r['scan']) in note_map))
    return len(done)
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='status':
        returned={p.parent.name for p in (W/'page_jobs').glob('*/result.json')}
        committed={p.stem for p in (W/'reviews').glob('*.json')}
        print(json.dumps({'committed_pages':len(committed),'returned_not_reviewed':sorted(returned-committed),'dispatch':json.loads((W/'dispatch.json').read_text())['current'],'utc':now()},indent=2))
    else:
        stem=sys.argv[2];packet,result,original,revised=load(stem)
        if mode=='inspect':
            print(json.dumps(result,ensure_ascii=False,indent=2))
            print(''.join(difflib.unified_diff(original.splitlines(True),revised.splitlines(True),fromfile='original',tofile='proposed')))
        elif mode=='commit':
            review_note=sys.argv[3]
            assert not (W/'reviews'/f'{stem}.json').exists(),'Already committed'
            ts=now(); final=[]
            for row,src in zip(result['rows'],packet['rows']):
                record=dict(row,cote=src['cote'],scan=src['scan'])
                ev=[]
                for e in row['events']:
                    actor=e.get('who', 'main reader' if e['outcome'].startswith('Main ') else result['reader'])
                    ev.append({'statement_id':row['id'],'date':e.get('date',e.get('date_utc',ts)),'who':f"GPT-6 Astra Pro; effort inherited (not separately exposed); IM22 run 1; {actor}",'type':e['type'],'outcome':f"Cote {src['cote']}, scan {int(src['scan']):03d}. "+e['outcome']})
                ev.append({'statement_id':row['id'],'date':ts,'who':'GPT-6 Astra Pro; effort inherited (not separately exposed); IM22 run 1; main reader','type':'used and rechecked in this run','outcome':f"Cote {src['cote']}, scan {int(src['scan']):03d}. "+review_note+' Original-span uniqueness, row scope and exact replacement reconstruction checked.'})
                record['all_events']=ev;final.append(record)
            rec={'stem':stem,'committed_utc':ts,'original_sha256':hashlib.sha256(original.encode()).hexdigest(),'edited_sha256':hashlib.sha256(revised.encode()).hexdigest(),'rows':final}
            (W/'edited_pages'/f'{stem}.tex').write_bytes(revised.encode('utf-8'))
            (W/'reviews'/f'{stem}.json').write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n')
            total=rebuild()
            with (W/'progress.log').open('a') as f:f.write(f"scan {int(packet['rows'][0]['scan']):03d} done {ts} cote {packet['rows'][0]['cote']}\n")
            print(f'Committed {stem}; {total}/405 rows, {len(list((W/"reviews").glob("*.json")))}/309 pages. {ts}')
