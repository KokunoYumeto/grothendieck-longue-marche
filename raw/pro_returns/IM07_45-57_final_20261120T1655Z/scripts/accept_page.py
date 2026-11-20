#!/usr/bin/env python3
"""Validate a reviewed reader return, write its page, and refresh audit files."""
import argparse, csv, json, hashlib
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT.parent / 'source'
FIELDS = ['id', 'cote', 'scan', 'decision', 'find', 'replace', 'what_the_ink_shows', 'confidence']
EVENT_FIELDS = ['statement_id', 'date', 'who', 'type', 'outcome']

def stamp():
    return datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')

def load_original(page):
    return (SOURCE/'IM07_45-57_pages'/f'{page}.tex').read_bytes().decode('utf-8')

def reconstruct(original, rows):
    edits = []
    for row in rows:
        assert row['decision'] in 'abcd' and len(row['decision']) == 1
        assert row['confidence'] in ('high', 'medium', 'low')
        assert not row.get('unresolved', False), f"Parent must decide {row['id']}"
        if row['decision'] == 'a':
            find, repl = row['find'], row['replace']
            assert find and original.count(find) == 1, f"Nonunique original find for {row['id']}"
            assert find != repl, f"Empty change for {row['id']}"
            item = (original.index(find), original.index(find) + len(find), repl)
            if item not in edits:
                edits.append(item)
        else:
            assert row.get('replace', '') == ''
            assert row.get('find', '') == ''
        assert row.get('what_the_ink_shows'), f"Missing ink record for {row['id']}"
        assert row.get('crops'), f"Missing crop for {row['id']}"
        for crop in row['crops']:
            assert crop.startswith('crops/') and (ROOT/crop).is_file(), crop
    edits.sort()
    for left, right in zip(edits, edits[1:]):
        assert left[1] <= right[0], 'Conflicting original edit spans'
    result = original
    for start, end, replacement in reversed(edits):
        result = result[:start] + replacement + result[end:]
    return result, edits

def refresh():
    accepted = [json.loads(p.read_text()) for p in (ROOT/'review').glob('*.accepted.json')]
    entries = sorted((r for a in accepted for r in a['rows']), key=lambda r:r['row_index'])
    with (ROOT/'placements.tsv').open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, FIELDS, delimiter='\t', lineterminator='\n'); w.writeheader()
        w.writerows({k:r.get(k,'') for k in FIELDS} for r in entries)
    events=[]
    for a in accepted:
        for r in a['rows']:
            e=r['check_event']
            who=f"GPT-6 Astra Pro (session declaration); effort not exposed; run IM07_45-57_20261120T161531Z; {a['reader']}; {a['page']}"
            events.append({'statement_id':r['id'],'date':e['date'],'who':who,'type':e['type'],'outcome':f"table row {r['row_index']}; cote {r['cote']}, scan {int(r['scan']):03}: {e['outcome']}"})
            events.append({'statement_id':r['id'],'date':a['accepted_utc'],'who':who.replace(a['reader'],'main reader'),'type':'used and rechecked in this run','outcome':f"table row {r['row_index']}; cote {r['cote']}, scan {int(r['scan']):03}; main-reader review: {a['review_note']} Decision {r['decision']}. Original-span uniqueness and exact-edit reconstruction verified; no independent mathematical proof claimed."})
    extra_events = ROOT/'review/additional_check_events.json'
    if extra_events.exists():
        events.extend(json.loads(extra_events.read_text()))
    events.sort(key=lambda e:(e['date'],e['statement_id'],e['who']))
    with (ROOT/'CHECK_EVENTS.tsv').open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,EVENT_FIELDS,delimiter='\t',lineterminator='\n');w.writeheader();w.writerows(events)
    notes=['# Notes — IM07_45–57','','## Scope and check method','','All decisions compare the supplied transcription with the supplied facsimile. Tight crops are enlarged with their contrast raised; coordinates and processing are recorded beside each image. No OCR or text-recognition software is used. Mathematical refinements in category (b) are recorded from the corresponding supplied correction row; the visual checks recorded here do not constitute independent proofs of those refinements. The supplied table repeats id L1310 on two different pages; both rows retain that id and their original order, and are distinguished by cote, scan, and table-row index in the review records.','','## (b) Authorial slips and mathematical refinements','']
    bs=[r for r in entries if r['decision']=='b']
    for r in bs:
        notes += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03} (table row {r['row_index']})",'',r.get('note',''),'',f"Ink evidence: {r['what_the_ink_shows']}",'']
    if not bs: notes += ['None recorded so far.','']
    notes += ['## (a) Transcription corrections','']
    for r in [r for r in entries if r['decision']=='a']:
        notes += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03} (table row {r['row_index']})",'',r.get('note',''),'',f"Ink evidence: {r['what_the_ink_shows']}",'']
    notes += ['## (d) Loci not on the assigned page','']
    ds=[r for r in entries if r['decision']=='d']
    for r in ds:
        notes += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03} (table row {r['row_index']})",'',r.get('note',''),'',f"Ink evidence: {r['what_the_ink_shows']}",'']
    if not ds: notes += ['None recorded so far.','']
    notes += ['## (c) Readings already present and resolved flags','']
    cs=[r for r in entries if r['decision']=='c' and r.get('note')]
    for r in cs:
        notes += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03} (table row {r['row_index']})",'',r['note'],'',f"Ink evidence: {r['what_the_ink_shows']}",'']
    if not cs: notes += ['None recorded so far.','']
    notes += ['## Readings not fully settled by the ink','']
    brief_path=ROOT/'review/uncertainty_summary.json'
    if brief_path.exists():
        briefs=json.loads(brief_path.read_text())
        notes += ['The row decisions are final; the following literal readings remain uncertain. Detailed stroke evidence and crop references appear in the corresponding entries above. Existing doubts unrelated to the correction rows are also preserved.','', '| Row id | Cote / scan | Unsettled reading and treatment |','|---|---|---|']
        for item in briefs:
            notes += [f"| {item['id']} | {item['location']} | {item['summary']} |"]
        notes += ['']
    else:
        doubtful=[r for r in entries if r.get('ink_unsettled') or (r['decision']=='a' and '\\unsure{' in r['replace'])]
        for r in doubtful:
            notes += [f"### {r['id']} — cote {r['cote']}, scan {int(r['scan']):03}",'',r.get('note',''),'',f"Recorded reading: `{r['replace']}`" if r['decision']=='a' else 'The existing diplomatic doubt is retained.',f"Ink evidence: {r['what_the_ink_shows']}",'']
        if not doubtful: notes += ['None recorded so far.','']
    (ROOT/'notes.md').write_text('\n'.join(notes),encoding='utf-8')
    return entries

def main():
    p=argparse.ArgumentParser();p.add_argument('page');p.add_argument('--note',required=True);p.add_argument('--allow-candidate-mismatch',action='store_true')
    a=p.parse_args()
    dst=ROOT/'review'/f'{a.page}.accepted.json'
    assert not dst.exists(), f'Already accepted {a.page}'
    src=ROOT/'review'/f'{a.page}.final.json'
    if not src.exists(): src=ROOT/'review'/f'{a.page}.json'
    data=json.loads(src.read_text())
    assigned=json.loads((ROOT/'assignments'/a.page/'rows.json').read_text())
    assert [(r['row_index'],r['id']) for r in data['rows']]==[(r['row_index'],r['id']) for r in assigned]
    original=load_original(a.page)
    new,edits=reconstruct(original,data['rows'])
    candidate=ROOT/'review'/f'{a.page}.proposed.tex'
    if not a.allow_candidate_mismatch:
        assert candidate.read_bytes().decode('utf-8') == new, 'Candidate changed unrelated text or lost edits'
    data.update({'accepted_utc':stamp(),'review_note':a.note,'original_sha256':hashlib.sha256(original.encode()).hexdigest(),'edited_sha256':hashlib.sha256(new.encode()).hexdigest(),'unique_edit_count':len(edits)})
    (ROOT/'edited_pages'/f'{a.page}.tex').write_bytes(new.encode('utf-8'))
    dst.write_text(json.dumps(data,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    entries=refresh()
    cote,scan=a.page.split('_scan')
    with (ROOT/'progress.log').open('a',encoding='utf-8') as f:
        f.write(f'scan {scan} done {data["accepted_utc"]} cote {cote}\n')
    print(json.dumps({'accepted':a.page,'rows':[r['id'] for r in data['rows']],'decisions':[r['decision'] for r in data['rows']],'unique_edits':len(edits),'total_rows_done':len(entries),'total_pages_done':len(list((ROOT/'review').glob('*.accepted.json'))),'utc':data['accepted_utc']}))

if __name__=='__main__':main()
