#!/usr/bin/env python3
"""Exact-span application, audit tables, and reproducible packaging; no OCR."""
import argparse
import csv
import datetime as dt
import hashlib
import json
import re
from pathlib import Path
import zipfile

WORK = Path(__file__).resolve().parents[1]
ROOT = WORK.parent
SOURCE = ROOT / 'source'
FIELDS = ['id', 'cote', 'scan', 'decision', 'find', 'replace', 'what_the_ink_shows', 'confidence']
EVENT_FIELDS = ['statement_id', 'date', 'who', 'type', 'outcome']

def now():
    return dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def canonical_time(value):
    if value.endswith(' UTC'):
        return value
    return dt.datetime.fromisoformat(value.replace('Z', '+00:00')).astimezone(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')

def text(path):
    return path.read_bytes().decode('utf-8')

def source_rows():
    with (SOURCE / 'IM01_1-6_corrections.tsv').open(newline='', encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def key(r):
    return (r['id'], str(r['cote']), str(int(r['scan'])))

def page_name(r):
    return f"{r['cote']}_scan{int(r['scan']):03d}"

def dump_tsv(path, fields, rows):
    with path.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n', extrasaction='ignore')
        w.writeheader()
        w.writerows(rows)

def apply_proposal(p):
    page = p['page']
    original = text(SOURCE / 'IM01_1-6_pages' / (page + '.tex'))
    wanted = [r for r in source_rows() if page_name(r) == page]
    assert [key(r) for r in p['rows']] == [key(r) for r in wanted], f'{page}: rows/order differ'
    spans = []
    for r in p['rows']:
        assert r['decision'] in 'abcd' and len(r['decision']) == 1
        assert r['confidence'] in ['high', 'medium', 'low']
        assert r.get('what_the_ink_shows'), f"{r['id']}: missing ink account"
        assert r.get('crops'), f"{r['id']}: missing crop"
        for crop in r['crops']:
            assert (WORK / crop['path']).is_file(), crop['path']
        if r['decision'] == 'a':
            assert r['find'] and original.count(r['find']) == 1, f"{r['id']}: find count {original.count(r['find'])}"
            assert r['replace'] != r['find'], f"{r['id']}: unchanged a"
            start = original.index(r['find'])
            spans.append((start, start + len(r['find']), r['replace'], r['id']))
        else:
            assert not r.get('find') and not r.get('replace'), f"{r['id']}: non-a edit"
        if r['decision'] in 'bd':
            assert r.get('note'), f"{r['id']}: missing note"
    spans.sort()
    for x, y in zip(spans, spans[1:]):
        assert x[1] <= y[0], f'overlapping edits: {x[3]}, {y[3]}'
    result = original
    for start, end, replacement, rowid in reversed(spans):
        result = result[:start] + replacement + result[end:]
    assert result == p['proposed_latex'], f'{page}: proposed page has additional or missing changes'
    return original, result, spans

def accepted():
    return [json.loads(text(p)) for p in sorted((WORK / 'accepted').glob('*.json'))]

def rebuild():
    decisions = {}
    events = []
    for p in accepted():
        for r in p['rows']:
            assert key(r) not in decisions, f'duplicate decision {key(r)}'
            decisions[key(r)] = r
            where = f"cote {r['cote']}, scan {int(r['scan']):03d}: "
            events.append(dict(statement_id=r['id'], date=canonical_time(r['checked_at']),
                who=f"GPT-6 Astra Pro; effort=inherited, not exposed; run={p['worker']}/{p['page']}",
                type=r.get('event_type', 'used and rechecked in this run'), outcome=where+r['event_outcome']))
            for e in r.get('additional_events', []):
                events.append(dict(statement_id=r['id'], date=canonical_time(e.get('checked_at', r['checked_at'])),
                    who=f"GPT-6 Astra Pro; effort=inherited, not exposed; run={p['worker']}/{p['page']}",
                    type=e.get('type', e.get('event_type')), outcome=where+e.get('outcome', e.get('event_outcome'))))
            events.append(dict(statement_id=r['id'], date=p['accepted_at'],
                who='GPT-6 Astra Pro; effort=not exposed; run=main-reader',
                type='used and rechecked in this run', outcome=where+p['main_check']))
    ordered = [decisions[key(r)] for r in source_rows() if key(r) in decisions]
    dump_tsv(WORK / 'placements.tsv', FIELDS, ordered)
    events.sort(key=lambda e: (e['date'], e['statement_id'], e['who']))
    dump_tsv(WORK / 'CHECK_EVENTS.tsv', EVENT_FIELDS, events)
    notes = ['# Notes on the decided corrections', '',
        'This is a diplomatic reading audit. Mathematical refinements from the supplied correction table are reported as such; no mathematical re-proof is claimed unless a check event explicitly says otherwise. Repeated statement ids are distinguished by cote and scan. Decisions refer to the supplied original page.', '',
        'The original scans and source transcription are supplied inputs and are not duplicated in the deliverable. Crop coordinates are recorded in the review records and can be reproduced with `scripts/make_crop.py`. The runtime did not expose a numerical reasoning-effort setting; check events report this rather than inventing one.', '']
    supplied = {key(r): r for r in source_rows()}
    for r in ordered:
        if r['decision'] in 'bd' or r.get('note') or r['confidence'] != 'high':
            notes += [f"## {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d} — decision ({r['decision']})", '', r.get('note') or 'See the ink account for the unresolved reading.', '',
                '**Ink check:** ' + r['what_the_ink_shows'], '', '**Confidence:** ' + r['confidence'] + '.', '']
            proposal = supplied[key(r)].get('should_read', '').strip()
            if proposal:
                notes += ['**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.', '', '```text', proposal, '```', '']
    (WORK / 'notes.md').write_text('\n'.join(notes), encoding='utf-8')
    return len(ordered), len(events)

def accept(page, main_check):
    path = WORK / 'reviews' / (page + '.json')
    p = json.loads(text(path))
    original, result, spans = apply_proposal(p)
    destination = WORK / 'accepted' / (page + '.json')
    assert not destination.exists(), f'{page} already accepted'
    p['accepted_at'] = now()
    p['main_check'] = main_check
    p['original_sha256'] = hashlib.sha256(original.encode('utf-8')).hexdigest()
    p['edited_sha256'] = hashlib.sha256(result.encode('utf-8')).hexdigest()
    (WORK / 'edited_pages' / (page + '.tex')).write_bytes(result.encode('utf-8'))
    destination.write_text(json.dumps(p, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    count, ev = rebuild()
    r = p['rows'][0]
    with (WORK / 'progress.log').open('a', encoding='utf-8') as f:
        f.write(f"scan {int(r['scan']):03d} done {now()} cote {r['cote']}\n")
    print(json.dumps({'accepted':page, 'rows_total':count, 'pages_total':len(accepted()), 'events_total':ev, 'edits':len(spans)}, ensure_ascii=False))

def status():
    pages = list(dict.fromkeys(page_name(r) for r in source_rows()))
    done = {p['page'] for p in accepted()}
    print(json.dumps({'now':now(), 'started':text(WORK/'progress.log').splitlines()[0], 'done':len(done), 'total':len(pages), 'remaining':[p for p in pages if p not in done]},ensure_ascii=False))

def audit(final=False):
    ps = accepted()
    for p in ps:
        original, result, spans = apply_proposal(p)
        assert (WORK/'edited_pages'/(p['page']+'.tex')).read_bytes() == result.encode('utf-8')
        assert p['original_sha256'] == hashlib.sha256(original.encode('utf-8')).hexdigest()
        assert p['edited_sha256'] == hashlib.sha256(result.encode('utf-8')).hexdigest()
    original_rows = source_rows()
    with (WORK/'placements.tsv').open(newline='',encoding='utf-8') as f:
        rows=list(csv.DictReader(f,delimiter='\t'))
    assert len(rows) == sum(len(p['rows']) for p in ps)
    by_key = {key(r): r for p in ps for r in p['rows']}
    for r in rows:
        expected = by_key[key(r)]
        assert all(r[f] == str(expected.get(f, '')) for f in FIELDS), f'placement differs: {key(r)}'
    notes = text(WORK/'notes.md')
    for r in rows:
        if r['decision'] in 'bd' or r['confidence'] != 'high':
            assert f"## {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}" in notes
        assert any(c['path'] in r['what_the_ink_shows'] for c in by_key[key(r)]['crops']), f'crop reference absent: {key(r)}'
    with (WORK/'CHECK_EVENTS.tsv').open(newline='', encoding='utf-8') as f:
        event_reader = csv.DictReader(f, delimiter='\t')
        assert event_reader.fieldnames == EVENT_FIELDS
        events = list(event_reader)
    for e in events:
        assert e['statement_id'] in {r['id'] for r in rows}
        dt.datetime.strptime(e['date'], '%Y-%m-%d %H:%M:%S UTC')
        assert all(e[field] for field in EVENT_FIELDS)
    for r in rows:
        prefix = f"cote {r['cote']}, scan {int(r['scan']):03d}: "
        matching = [e for e in events if e['statement_id'] == r['id'] and e['outcome'].startswith(prefix)]
        assert any('run=main-reader' in e['who'] for e in matching), f'main check absent: {key(r)}'
        assert any('run=reader' in e['who'] for e in matching), f'reader check absent: {key(r)}'
    log_lines = text(WORK/'progress.log').splitlines()
    dt.datetime.strptime(log_lines[0], '%Y-%m-%d %H:%M:%S UTC')
    completed = []
    for line in log_lines[1:]:
        m = re.fullmatch(r'scan (\d{3}) done (.+ UTC) cote (\d+)', line)
        if m:
            dt.datetime.strptime(m.group(2), '%Y-%m-%d %H:%M:%S UTC')
            completed.append(f'{m.group(3)}_scan{m.group(1)}')
    assert len(completed) == len(set(completed)) == len(ps), 'completion log count differs'
    assert set(completed) == {p['page'] for p in ps}, 'completion log coverage differs'
    if final:
        assert all(not p.get('open_issues') for p in ps), 'unadjudicated reader issue'
        assert [key(r) for r in rows] == [key(r) for r in original_rows]
        assert {p.name for p in (WORK/'edited_pages').glob('*.tex')} == {p.name for p in (SOURCE/'IM01_1-6_pages').glob('*.tex')}
    result={'pages':len(ps),'rows':len(rows),'decisions':{d:sum(r['decision']==d for r in rows) for d in 'abcd'}, 'events':len(events), 'crops':len({c['path'] for p in ps for r in p['rows'] for c in r['crops']}), 'all_edits_exact':True, 'complete':len(rows)==len(original_rows)}
    print(json.dumps(result,ensure_ascii=False))
    return result

def package(name, final=False):
    result = audit(final=final)
    dest=ROOT/'deliverables'/name
    dest.parent.mkdir(exist_ok=True)
    assert not dest.exists(), f'Never overwrite a package: {dest}'
    with zipfile.ZipFile(dest,'w',zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in sorted(WORK.rglob('*')):
            if not p.is_file() or p.suffix == '.zip' or '__pycache__' in p.parts or 'page_packets' in p.parts:
                continue
            z.write(p,p.relative_to(WORK).as_posix())
    with zipfile.ZipFile(dest) as z:
        assert z.testzip() is None
    print(json.dumps({'zip':str(dest),'bytes':dest.stat().st_size,'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),**result}))

def main():
    (WORK/'accepted').mkdir(exist_ok=True)
    parser=argparse.ArgumentParser()
    parser.add_argument('command',choices=['init','check','accept','status','audit','package'])
    parser.add_argument('value',nargs='?')
    parser.add_argument('--main-check',default='Compared row decision and exact original span with the returned crop; verified that only the listed correction changes and that every find span occurs once.')
    parser.add_argument('--final',action='store_true')
    a=parser.parse_args()
    if a.command=='init': rebuild();status()
    elif a.command=='check':
        p=json.loads(text(WORK/'reviews'/(a.value+'.json')))
        original,result,spans=apply_proposal(p)
        print(json.dumps({'page':a.value,'edits':spans,'rows':p['rows'],'open_issues':p.get('open_issues',[])},ensure_ascii=False,indent=2))
    elif a.command=='accept': accept(a.value,a.main_check)
    elif a.command=='status': status()
    elif a.command=='audit': audit(final=a.final)
    elif a.command=='package': package(a.value,final=a.final)

if __name__=='__main__': main()
