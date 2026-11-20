#!/usr/bin/env python3
"""Audit completed row placements and package all deliverables/documentation."""
from pathlib import Path
from datetime import datetime, timezone
from collections import Counter
import argparse, csv, hashlib, json, re, zipfile

BASE=Path(__file__).resolve().parents[1]
OUTPUT=BASE.parent/'deliverables'

def table(path):
    with path.open(newline='') as f:
        return list(csv.DictReader(f,delimiter='\t'))

def inventory():
    folders=['edited_pages','crops','reviews','accepted_reviews','scripts']
    files=[BASE/n for n in ['placements.tsv','notes.md','CHECK_EVENTS.tsv','progress.log','page_order.tsv','checkpoint_index.tsv','audit_report.txt','README.txt'] if (BASE/n).is_file()]
    for name in folders:
        if (BASE/name).exists():
            files += [p for p in (BASE/name).rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc']
    return sorted(set(files))

def audit(final=False):
    source=table(BASE/'source/IM08_57-64_corrections.tsv')
    placements=table(BASE/'placements.tsv')
    assert list(placements[0]) == ['id','cote','scan','decision','find','replace','what_the_ink_shows','confidence'], 'Placement schema mismatch.'
    key=lambda r:(r['id'],r['cote'],r['scan'])
    expected=[key(r) for r in source]
    actual=[key(r) for r in placements]
    assert len(actual)==len(set(actual)), 'Duplicate composite row key.'
    assert actual==[k for k in expected if k in set(actual)], 'Placements are out of source order.'
    if final: assert actual==expected, 'Missing corrections.'
    src_pages={f"{r['cote']}_scan{int(r['scan']):03d}.tex" for r in source}
    out_pages={p.name for p in (BASE/'edited_pages').glob('*.tex')}
    if final: assert out_pages==src_pages, 'Missing or extra pages.'
    row_pages={f"{r['cote']}_scan{int(r['scan']):03d}.tex" for r in placements}
    assert row_pages==out_pages
    n_changed=0
    known_commands=set()
    for source_path in (BASE/'source/IM08_57-64_pages').glob('*.tex'):
        known_commands.update(re.findall(r'\\[A-Za-z@]+',source_path.read_text()))
    known_commands.update(re.findall(r'\\[A-Za-z@]+',(BASE/'source/PREAMBLE.tex').read_text()))
    for name in sorted(out_pages):
        original=(BASE/'source/IM08_57-64_pages'/name).read_bytes().decode('utf-8')
        rr=[r for r in placements if name==f"{r['cote']}_scan{int(r['scan']):03d}.tex"]
        intervals=[]
        for r in rr:
            if r['decision']=='a':
                assert r['find'] and original.count(r['find'])==1, (name,r['id'],'find')
                start=original.index(r['find']); intervals.append((start,start+len(r['find']),r['replace']))
            else: assert r['find']==r['replace']==''
            assert r['decision'] in ('a','b','c','d')
            assert r['confidence'] in ('high','medium','low')
            crops=re.findall(r'crops/[A-Za-z0-9_.-]+\.(?:png|jpg|jpeg)',r['what_the_ink_shows'])
            assert crops, (name,r['id'],'no documented crop')
            for crop in crops: assert (BASE/crop).is_file(),crop
        intervals.sort()
        assert all(a[1]<=b[0] for a,b in zip(intervals,intervals[1:]))
        reconstructed=original
        for start,end,repl in reversed(intervals): reconstructed=reconstructed[:start]+repl+reconstructed[end:]
        result=(BASE/'edited_pages'/name).read_bytes().decode('utf-8')
        assert result==reconstructed, (name,'unrecorded changes')
        assert result.count('\n')==original.count('\n'), (name,'line-break count changed')
        assert result.count('\r\n')==original.count('\r\n'), (name,'original newline encoding changed')
        new_commands=set(re.findall(r'\\[A-Za-z@]+',result))-known_commands
        assert not new_commands, (name,'unreviewed new control word',sorted(new_commands))
        n_changed+=result!=original
    events=table(BASE/'CHECK_EVENTS.tsv')
    for r in placements: assert any(e['statement_id']==r['id'] and f"scan {int(r['scan']):03d}" in e['outcome'] for e in events), ('missing event',key(r))
    notes=(BASE/'notes.md').read_text()
    for r in placements:
        if r['decision'] in ('b','d'):
            assert f"## {r['id']} — cote {r['cote']}, scan {int(r['scan']):03d}" in notes
    progress=(BASE/'progress.log').read_text().splitlines()
    datetime.strptime(progress[0],'%Y-%m-%d %H:%M:%S UTC')
    done=re.findall(r'^scan (\d+) done .* cote (\d+)$','\n'.join(progress),re.M)
    assert len(done)==len(out_pages)
    assert {f'{c}_scan{int(s):03d}.tex' for s,c in done}==out_pages
    report=['IM08_57–64 final validation' if final else 'IM08_57–64 checkpoint validation',datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),f'Placements: {len(placements)} / {len(source)}',f'Pages: {len(out_pages)} / {len(src_pages)}',f'Pages with recorded edits: {n_changed}',f'Decisions: {dict(Counter(r["decision"] for r in placements))}',f'Confidence: {dict(Counter(r["confidence"] for r in placements))}',f'Check events: {len(events)}','PASS: source-order placement coverage, original-span uniqueness, nonoverlap, exact byte reconstruction, original CRLF preservation, control-word inventory, unchanged non-edit pages, crop references, note coverage, and completion log.','No OCR or text-recognition was used. No LaTeX normalization or unrelated correction was authorized.','Mathematical refinements in notes are attributed to the supplied correction table unless an event explicitly identifies a fresh mathematical check.']
    (BASE/'audit_report.txt').write_text('\n'.join(report)+'\n')
    return report

def package(name):
    OUTPUT.mkdir(exist_ok=True)
    dest=OUTPUT/name
    assert not dest.exists(), f'Refusing to overwrite {dest}'
    files=inventory()
    manifest='path\tbytes\tsha256\n'+''.join(f'{p.relative_to(BASE)}\t{p.stat().st_size}\t{hashlib.sha256(p.read_bytes()).hexdigest()}\n' for p in files)
    with zipfile.ZipFile(dest,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
        for p in files: z.write(p,p.relative_to(BASE))
        z.writestr('MANIFEST.tsv',manifest)
    with zipfile.ZipFile(dest) as z: assert z.testzip() is None
    print(dest)
    print('bytes',dest.stat().st_size,'entries',len(files)+1,'sha256',hashlib.sha256(dest.read_bytes()).hexdigest())

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--final',action='store_true'); ap.add_argument('--checkpoint',action='store_true'); args=ap.parse_args()
    assert args.final != args.checkpoint
    if args.checkpoint:
        start=datetime.strptime((BASE/'progress.log').read_text().splitlines()[0],'%Y-%m-%d %H:%M:%S UTC').replace(tzinfo=timezone.utc)
        elapsed=(datetime.now(timezone.utc)-start).total_seconds()
        index=BASE/'checkpoint_index.tsv'
        old=table(index) if index.exists() else []
        due=(len(old)+1)*2700
        if elapsed<due:
            print(f'No checkpoint due: elapsed {elapsed:.0f}s; next threshold {due}s.'); return
        report=audit()
        number=len(old)+1; name=f'IM08_57-64_checkpoint_{number:02d}.zip'
        with index.open('a',newline='') as f:
            w=csv.writer(f,delimiter='\t',lineterminator='\n')
            if not old: w.writerow(['number','filename','created_utc'])
            w.writerow([number,name,datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')])
        package(name)
    else:
        report=audit(final=True); print('\n'.join(report)); package('IM08_57-64.zip')

if __name__=='__main__': main()
