#!/usr/bin/env python3
"""Validate and commit one manually reviewed page, preserving original spans."""
from pathlib import Path
from datetime import datetime, timezone
import argparse, csv, difflib, json, re

BASE = Path(__file__).resolve().parents[1]
FIELDS = ['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence']
EVENT_FIELDS = ['statement_id','date','who','type','outcome']

def now():
    return datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def original_newlines(page, text):
    """Retain the byte-level newline convention of the supplied page."""
    raw=(BASE/'source/IM08_57-64_pages'/f'{page}.tex').read_bytes()
    text=text.replace('\r\n','\n')
    if b'\r\n' in raw:
        assert raw.count(b'\r\n')==raw.count(b'\n')==raw.count(b'\r'), (page,'mixed source line endings')
        return text.replace('\n','\r\n')
    return text

def read_review(page):
    p = BASE/'reviews'/f'{page}.json'
    review = json.loads(p.read_text())
    packet = json.loads((BASE/'packets'/f'{page}.json').read_text())
    original = (BASE/'source/IM08_57-64_pages'/f'{page}.tex').read_text()
    expected = [(r['id'],str(r['cote']),str(r['scan'])) for r in packet['rows']]
    actual = [(r['id'],str(r['cote']),str(r['scan'])) for r in review['rows']]
    assert actual == expected, (expected, actual)
    intervals = []
    for row in review['rows']:
        assert row['decision'] in 'abcd' and len(row['decision']) == 1
        assert row['confidence'] in ('high','medium','low')
        assert not row.get('open_question'), (page,row['id'],row.get('open_question'))
        if row['decision'] == 'a':
            find, replace = row['find'],row['replace']
            assert find and original.count(find) == 1, (page,row['id'],'find not unique')
            assert find != replace, (page,row['id'],'no change')
            i = original.index(find)
            intervals.append((i,i+len(find),replace,row['id']))
        else:
            assert row.get('find','') == '' and row.get('replace','') == ''
        if row.get('checked_on_scan'):
            assert row['what_the_ink_shows'], (page,row['id'],'no ink description')
            crops = re.findall(r'crops/[A-Za-z0-9_.-]+\.(?:png|jpg|jpeg)',row['what_the_ink_shows'])
            assert crops, (page,row['id'],'no crop reference')
            for crop in crops:
                assert (BASE/crop).is_file(), crop
    intervals.sort()
    for left,right in zip(intervals,intervals[1:]):
        assert left[1] <= right[0], (page,'overlapping find spans',left[3],right[3])
    edited = original
    for start,end,repl,_ in reversed(intervals):
        edited = edited[:start]+repl+edited[end:]
    assert edited == review['candidate_latex'], (page,'candidate differs from recorded edits')
    assert edited.count('\n') == original.count('\n'), (page,'line-break count changed')
    known_commands=set()
    for source_path in (BASE/'source/IM08_57-64_pages').glob('*.tex'):
        known_commands.update(re.findall(r'\\[A-Za-z@]+',source_path.read_text()))
    known_commands.update(re.findall(r'\\[A-Za-z@]+',(BASE/'source/PREAMBLE.tex').read_text()))
    new_commands=set(re.findall(r'\\[A-Za-z@]+',edited))-known_commands
    assert not new_commands, (page,'new control word needs manual review',sorted(new_commands))
    for row in review['rows']:
        assert any(e['statement_id'] == row['id'] for e in review['events']), (page,row['id'],'no event')
    return review,original,edited

def refresh_tables():
    sources = list(csv.DictReader((BASE/'source/IM08_57-64_corrections.tsv').open(),delimiter='\t'))
    accepted = {}
    for path in sorted((BASE/'accepted_reviews').glob('*.json')):
        review = json.loads(path.read_text())
        for row in review['rows']:
            accepted[(row['id'],str(row['cote']),str(row['scan']))] = row
    ordered = [accepted[(r['id'],r['cote'],r['scan'])] for r in sources if (r['id'],r['cote'],r['scan']) in accepted]
    with (BASE/'placements.tsv').open('w',newline='') as f:
        w=csv.DictWriter(f,fieldnames=FIELDS,delimiter='\t',lineterminator='\n',extrasaction='ignore')
        w.writeheader()
        for row in ordered:
            output=dict(row)
            page=f"{row['cote']}_scan{int(row['scan']):03d}"
            for field in ('find','replace'):
                output[field]=original_newlines(page,output[field])
            w.writerow(output)
    notes=['# Notes on the IM08_57–64 corrections','',
      'The decisions distinguish the visible manuscript reading from mathematical corrections. Mathematical refinements supplied by the correction table are attributed to it unless CHECK_EVENTS.tsv explicitly records a fresh mathematical check. Reading and visual comparison are not mathematical proofs. References below to another source not being inspected concern its use as evidence for that particular row; a separately assigned page may have been reviewed for its own rows. Retained uncertainties are described in the relevant row notes and remain marked in place.', '',
      'The identifier L832 occurs on three separate supplied rows (cote 62, scans 62, 80 and 91). These remain three placements, in the supplied order.', '']
    for row in ordered:
        if row['decision'] in ('b','d') or row.get('note'):
            notes += [f"## {row['id']} — cote {row['cote']}, scan {int(row['scan']):03d} — decision ({row['decision']})",'',row.get('note') or 'See the corresponding placement for the retained reading.','']
    (BASE/'notes.md').write_text('\n'.join(notes))
    return len(ordered)

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('page')
    ap.add_argument('--commit',action='store_true')
    ap.add_argument('--review',default='')
    args=ap.parse_args()
    review,original,edited=read_review(args.page)
    print(''.join(difflib.unified_diff(original.splitlines(True),edited.splitlines(True),fromfile='original/'+args.page+'.tex',tofile='edited/'+args.page+'.tex')) or 'No LaTeX changes.')
    if not args.commit:
        print('VALIDATED',args.page); return
    assert args.review, 'Provide a concrete main-reader visual review.'
    out=BASE/'accepted_reviews'/f'{args.page}.json'
    out.parent.mkdir(exist_ok=True)
    assert not out.exists(), 'Page already committed; inspect explicitly before revising.'
    t=now()
    review['main_review']={'date':t,'who':'GPT-6 Astra Pro; effort not exposed; main reader; run IM08-20261120','outcome':args.review}
    (BASE/'edited_pages'/f'{args.page}.tex').write_bytes(original_newlines(args.page,edited).encode('utf-8'))
    out.write_text(json.dumps(review,ensure_ascii=False,indent=2)+'\n')
    n=refresh_tables()
    with (BASE/'CHECK_EVENTS.tsv').open('a',newline='') as f:
        w=csv.DictWriter(f,fieldnames=EVENT_FIELDS,delimiter='\t',lineterminator='\n',extrasaction='ignore')
        w.writerows(review['events'])
        for row in review['rows']:
            w.writerow({'statement_id':row['id'],'date':t,'who':review['main_review']['who'],'type':'used and rechecked in this run','outcome':f"Cote {row['cote']}, scan {int(row['scan']):03d}: main-reader review. {args.review} Decision ({row['decision']}); exact original-span uniqueness, nonoverlap, and reconstruction of the page from recorded edits verified."})
    r=review['rows'][0]
    with (BASE/'progress.log').open('a') as f:
        f.write(f"scan {int(r['scan']):03d} done {t} cote {r['cote']}\n")
    print('COMMITTED',args.page,'TOTAL ROWS',n,'TOTAL PAGES',len(list((BASE/'edited_pages').glob('*.tex'))))

if __name__=='__main__':
    main()
