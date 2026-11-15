#!/usr/bin/env python3
"""Final structural and provenance checks; never changes frozen text."""
from pathlib import Path
import csv
import datetime as dt
import hashlib
import importlib.util
import json
import re
import sys

root=Path(__file__).resolve().parents[1]
context=Path(sys.argv[1]).resolve() if len(sys.argv)>1 else root.parents[1]/'context'
now=dt.datetime.now(dt.timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
spec=importlib.util.spec_from_file_location('package_validator',root/'scripts/validate_package.py')
mod=importlib.util.module_from_spec(spec)
spec.loader.exec_module(mod)
struct=mod.validate(root,False,set())
assert struct['structural_pass'],struct
assert not struct['unknown_commands'] and not struct['unknown_environments']
struct['checked_utc']=now
(root/'records/structural_validation.json').write_text(json.dumps(struct,indent=2,ensure_ascii=False)+'\n')

frozen=json.loads((root/'records/frozen_hashes.json').read_text())
assert len(frozen['sha256'])==36
actual={name:hashlib.sha256((root/name).read_bytes()).hexdigest() for name in frozen['sha256']}
assert actual==frozen['sha256'],'Frozen transcription hash mismatch'

notes=(root/'MPL_60_036-070_notes.md').read_text()
items=re.findall(r'^### ((?:LF|A|C|S)\d+) —',notes,re.M)
expected=[f'{p}{n:02d}' for p,k in [('LF',22),('A',24),('C',7),('S',7)] for n in range(1,k+1)]
assert items==expected,items
search=json.loads((root/'records/research_context_search.json').read_text())
assert [x['id'] for x in search['entries']]==items
assert 'being assembled' not in notes and 'checkpoint status' not in notes
for op,cl in [(r'\(',r'\)'),(r'\[',r'\]')]:
 assert notes.count(op)==notes.count(cl),(op,notes.count(op),notes.count(cl))
assert not [ord(c) for c in notes if ord(c)<32 and c not in '\n\t\r']
rs=(context/'notes/RESULTS_STATE.md').read_text()
ids=[i for i in re.findall(r'^- \*\*([^*]+)\*\*',rs,re.M) if i not in ['LM7','LM7_PUSH','60-inertia-average-duality']]
assert len(ids)==50
assert all(i in notes for i in ids)
assert 'Hua, findings register, 60-inertia-average-duality' in notes

progress=(root/'progress.log').read_text()
for n in range(36,71):
 assert f'60 scan {n:03d} done ' in progress
 assert f'scan {n:03d} audited ' in progress
assert progress.index('transcription frozen ')<progress.index('context opened ')
with (root/'MPL_60_036-070_inventory.csv').open(newline='') as f:
 rows=list(csv.DictReader(f))
classes={int(r['scan']):r['sheet_kind'] for r in rows}
assert len(rows)==413 and all(r['transcribed']=='yes' for r in rows)
assert sum(x=='text' for x in classes.values())==17
assert sum(x=='reused_typed' for x in classes.values())==18
for p in root.rglob('*'):
 if not p.is_file() or '__pycache__' in p.parts:continue
 assert p.suffix.lower() not in ['.jpg','.jpeg','.png','.pdf','.zip','.webp','.tif','.tiff'],str(p)

report={
 'checked_utc':now,'structural_pass':True,
 'frozen_utc':frozen['frozen_utc'],'frozen_hashes_unchanged':True,'verified_frozen_files':36,
 'page_count':35,'inventory_rows':413,'inventory_all_yes':True,
 'sheet_counts':{'text':17,'reused_typed':18},
 'combined_is_exact_ordered_concatenation':True,
 'research_items':60,'research_words_whitespace_count':len(notes.split()),
 'research_context_queries':search['note_count'],
 'results_status_ids_covered':50,'hua_excerpt_assessed':True,
 'math_delimiters_balanced':True,'source_files_and_images_excluded':True,
 'audit_log_complete':True,
 'notes_sha256':hashlib.sha256(notes.encode()).hexdigest(),
 'syntax_record':'records/latex_syntax_validation.json',
 'research_reviews':['records/algebra_final_review.md','records/lfunctions_final_review.md','records/research_final_review.md'],
 'limits':'Structural/syntax checks do not independently certify ink readings; visual reading and doubts are documented separately.'
}
(root/'records/final_validation.json').write_text(json.dumps(report,indent=2,ensure_ascii=False)+'\n')
with (root/'progress.log').open('a') as f:
 f.write(f'research notes completed {now}; 60 items, individual context searches, all 50 supplied status-row IDs plus Hua assessed; bibliography and final research reviews incorporated.\n')
 f.write(f'final structural validation passed {now}; 35 pages, 413 inventory rows all yes; combined fragment is the exact ordered concatenation; no unknown commands or environments.\n')
 f.write(f'frozen hashes unchanged {now}; verified all 35 page files and the combined transcription against the pre-context SHA-256 register.\n')
 f.write(f'final package ready {now}; source scans, input archives, supplied context files, temporary renderings and bytecode excluded.\n')
print(json.dumps(report,ensure_ascii=False,indent=2))
