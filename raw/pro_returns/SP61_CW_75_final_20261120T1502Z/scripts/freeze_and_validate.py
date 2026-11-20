"""Freeze the completed transcription and record final mechanical verification.

No image reading, OCR, TeX compilation or mathematical checking occurs here.
"""
import csv
import hashlib
import re
import shutil
from collections import Counter
from pathlib import Path
from reading_support import ROOT, PREFIX, assemble, build_changes, read_table, log, utc
from validate_delivery import validate

manifest=ROOT/'transcription_hashes.sha256'
if manifest.exists():
    raise RuntimeError('Transcription is already frozen; do not overwrite the freeze.')
progress=(ROOT/'progress.log').read_text()
for stage in ['done','audited']:
    scans=[int(n) for n in re.findall(r'^scan (\d+) '+stage+r' ', progress, re.M)]
    if scans!=list(range(16,26)):
        raise RuntimeError('Incomplete or out-of-order '+stage+' record: '+repr(scans))
last_first=progress.rindex('scan 025 done ')
first_second=progress.index('scan 016 audited ')
assert last_first<first_second
assemble();build_changes()
for directory in ROOT.rglob('__pycache__'):
    shutil.rmtree(directory)
paths=sorted((ROOT/'pages').glob('*.tex'))+[ROOT/(PREFIX+'_transcription.tex')]
digests={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in paths}
manifest.write_text(''.join(digest+'  '+name+'\n' for name,digest in digests.items()))
log('transcription frozen')
with (ROOT/'progress.log').open('a') as f:
    for name,digest in digests.items():
        f.write('SHA-256 '+digest+'  '+name+'\n')

errors,warnings=validate(ROOT,strict_macros=True)
if errors or warnings:
    raise RuntimeError('Validation did not pass cleanly: '+repr((errors,warnings)))
decisions=read_table('reading_decisions.tsv')
collation=read_table(PREFIX+'_collation.tsv')
expected=[r for r in decisions if r['against_H']=='yes']
assert len(expected)==len(collation)
for r,c in zip(expected,collation):
    assert c['our_scan']==r['scan'] and c['line']==r['place']
    assert c['their_reading']==r['H'] and c['codex_reading']==r['C']
    assert c['final_reading']==r['final'] and c['scan_shows']==r['evidence']
    assert c['confidence']==r['confidence'] and c['kind']==r['kind']
assert len({r['id'] for r in decisions})==len(decisions)
assert all(r['against_C']=='yes' or r['against_H']=='yes' for r in decisions)
for scan in range(16,26):
    rs=[r for r in decisions if r['scan']==str(scan)]
    assert [r['id'] for r in rs]==[f'S{scan:03}-{n:03}' for n in range(1,len(rs)+1)]
with (ROOT/(PREFIX+'_inventory.csv')).open(newline='') as f:
    inventory=list(csv.DictReader(f))
assert len({r['element'] for r in inventory})==len(inventory)
assert sum('archive numeral' in r['position'] for r in inventory)==10
doubts=read_table('remaining_doubts.tsv')
crops=read_table('crop_register.tsv')
events=read_table('CHECK_EVENTS.tsv')
assert len({(r['scan'],r['key']) for r in crops})==len(crops)
assert len({r['statement_id'] for r in events})==len(events)
for name,digest in digests.items():
    assert hashlib.sha256((ROOT/name).read_bytes()).hexdigest()==digest
log('frozen transcription hashes verified unchanged; all 10 pages and combined fragment')
log('strict mechanical validation passed; 0 errors, 0 warnings; no TeX compilation')

counts=Counter(r['confidence'] for r in decisions)
report=f'''# Final mechanical verification

Completed {utc()} after the ten second image readings and the cross-page comparison.

## Result

The existing validator passed in strict macro mode with **0 errors and 0 warnings**. No TeX compiler, renderer, OCR system or image-reading helper was used. These checks establish file and record consistency; they do not establish the correctness of a handwriting reading or mathematical claim.

- Ten expected page fragments, scans 16–25, with one matching scan marker each.
- One ordered combined fragment with a single leading cote marker and the same page contents.
- Balanced braces, math delimiters and environments; no disallowed fragment commands.
- Required reports present; required CSV/TSV headers, values and column counts valid.
- {len(decisions)} unique, contiguous decision IDs; every row differs from at least one witness according to the canonical flags.
- {len(collation)} H collation rows exactly match the corresponding canonical readings, evidence, categories and confidence values.
- {len(inventory)} unique inventory elements, all transcribed; ten explicitly include the pencilled archive numerals with uncertain hand attribution.
- {len(doubts)} grouped doubt rows; {len(crops)} distinct registered crops; {len(events)} mathematical check events.
- First readings and second image readings each have one completion entry per page in order; all first readings precede the first second reading.
- The eleven frozen SHA-256 values were verified unchanged after the mechanical checks.
- No images, input archives, witness files, compiled artifacts or caches are present in the deliverable directory.

## Final counts

| Measure | Count |
| --- | ---: |
| Difference loci | {len(decisions)} |
| Against C | {sum(r['against_C']=='yes' for r in decisions)} |
| Against H | {sum(r['against_H']=='yes' for r in decisions)} |
| High confidence | {counts['high']} |
| Medium confidence | {counts['medium']} |
| Low confidence | {counts['low']} |

Against-C and against-H counts overlap. Confidence includes tentative differences, so these are not counts of proven errors.

## Earlier preflight

`mechanical_preflight.md` is retained as the dated interim snapshot. Its old counts and pending items describe that earlier state. This final verification supersedes those status items; the sheet feedback, completed audits and frozen hashes now exist, and generated Python caches have been removed. The final packaging script verifies the same frozen hashes again and checks ZIP contents after writing.
'''
(ROOT/'final_verification.md').write_text(report)
print('Frozen files:',len(digests))
print('Strict mechanical validation: 0 errors, 0 warnings.')
print('Final counts:',len(decisions),'decisions;',len(collation),'H rows;',len(inventory),'inventory rows;',len(doubts),'doubts;',len(crops),'crops;',len(events),'check events.')
