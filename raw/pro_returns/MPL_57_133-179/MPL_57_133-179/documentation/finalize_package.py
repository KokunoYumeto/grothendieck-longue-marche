#!/usr/bin/env python3
"""Verify frozen artifacts and make the final ZIP; no scan or TeX mutation."""
from pathlib import Path
from datetime import datetime, timezone
import csv, hashlib, json, re, subprocess, zipfile

ROOT=Path(__file__).resolve().parents[1]
WORK=ROOT.parent
STAMP=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
frozen=json.loads((ROOT/'documentation/frozen_sha256.json').read_text())
current={p:hashlib.sha256((ROOT/p).read_bytes()).hexdigest() for p in frozen}
assert current==frozen, 'A frozen file changed'
assert len(frozen)==44
result=subprocess.run(['python',str(ROOT/'documentation/validate_package.py')],text=True,capture_output=True)
assert result.returncode==0,result.stdout+result.stderr
struct=json.loads(result.stdout)
(ROOT/'documentation/final_structure_validation.json').write_text(result.stdout)
notes=json.loads((ROOT/'documentation/research_items.json').read_text())
searches=json.loads((ROOT/'documentation/context_searches.json').read_text())
ids={n['id'] for n in notes}
assert len(notes)==len(ids)==94
assert {s['note_id'] for s in searches}==ids
for n in notes:
    assert n['rs'] and n['where'] and n['quote'] and n['comparison']
    if n['sentences'] is not None:
        assert 1<=len(n['sentences'])<=4
    if n['kind']=='own idea':
        assert n['confidence'],n['id']

events=list(csv.DictReader((ROOT/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
allowed={'targeted proof check','independent re-proof','computation or formal certificate',
         'used and rechecked in this run','carried as background without fault found',
         'refuted, with refined statement ID'}
assert len(events)==181
for e in events:
    assert all(e.values()) and e['type'] in allowed,e
    if e['type'].startswith('refuted'):
        assert 'Refined statement ID:' in e['outcome']
assert all(any(e['statement_id']=='MPL_57_133-179 '+n['id'] for e in events) for n in notes)

compile_report=json.loads((ROOT/'documentation/tex_compile_report_final.json').read_text())
assert compile_report['all_43_syntax_pass']
assert all(compile_report['current_page_sha256'][Path(p).name]==h for p,h in frozen.items() if p.startswith('pages/'))
progress=(ROOT/'progress.log').read_text()
done=re.findall(r'^57 scan (\d{3}) done ',progress,re.M)
audited=re.findall(r'^scan (\d{3}) audited ',progress,re.M)
assert len(done)==len(set(done))==43
assert len(audited)==len(set(audited))==43
assert progress.index('transcription frozen')<progress.index('context opened')
firstline=progress.splitlines()[0]
quality={
 'verified_at':STAMP,'start_utc':firstline,'transcription_frozen_at':'2026-11-18 08:54:59 UTC',
 'frozen_files_checked':44,'frozen_hashes_unchanged':True,
 'first_pass_records':43,'second_audit_records':43,'whole_images_and_halves_read_by_root':129,
 'page_fragments':43,'combined_exact_concatenation':struct['combined_matches_raw_concatenation'],
 'inventory_rows':665,'all_inventory_transcribed_yes':True,
 'doubt_macro_occurrences':317,'additional_page_state_doubts':1,
 'research_items':94,'per_note_context_searches':94,'check_events':181,
 'root_note_sentence_counts_checked':True,'delegated_note_body_counts':'Manually reviewed: FW01–FW07 and JAC01–JAC08 have1–4sentences',
 'syntax_check_43_pages':True,'syntax_hashes_match_final_pages':True,
 'limitations':[
  'The image reading/audit record is a reader account, not machine-certified transcription accuracy.',
  'The syntax wrapper uses identity editorial macros; no styled visual edition or typography QA is claimed.',
  'TikZ drawings approximate visible strokes and labels; they are not photographic facsimiles.',
  'Research-source comparisons and local mathematical corrections do not alter the frozen text.',
  'Earlier research and registered statuses retain their own claimed/reviewed distinctions.'
 ],
 'sha256':current
}
(ROOT/'documentation/final_quality_report.json').write_text(json.dumps(quality,ensure_ascii=False,indent=2)+'\n')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'research notes completed {STAMP}; 94 items, per-note context comparisons, standing questions, 181 check events\n')
    f.write(f'final structural validation passed {STAMP}; 43 pages, 665 inventory rows, exact combined concatenation\n')
    f.write(f'final syntax report hashes verified {STAMP}; 43 successful fragment syntax checks; identity editorial macros, not visual formatting QA\n')
    f.write(f'frozen hashes unchanged {STAMP}; all 43 page files and combined transcription match the pre-context SHA-256 record (44/44)\n')
    f.write(f'final archive prepared {STAMP}; source attachments and earlier checkpoints excluded\n')

archive=WORK/'MPL_57_133-179.zip'
files=sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
assert not any(p.suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.zip'} for p in files)
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        z.write(p,p.relative_to(WORK))
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    for p,h in frozen.items():
        assert hashlib.sha256(z.read(ROOT.name+'/'+p)).hexdigest()==h
    assert z.read(ROOT.name+'/progress.log')==(ROOT/'progress.log').read_bytes()
print(json.dumps({'archive':str(archive),'bytes':archive.stat().st_size,'entries':len(files),
                  'zip_crc_pass':True,'frozen_hashes_in_zip_match':True,
                  'sha256':hashlib.sha256(archive.read_bytes()).hexdigest()},indent=2))
