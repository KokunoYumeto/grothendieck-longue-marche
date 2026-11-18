#!/usr/bin/env python3
"""Record the required end-of-run checks without changing frozen transcription."""
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import csv
import hashlib
import re
import subprocess
import sys

root=Path(__file__).resolve().parent.parent
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
expected=[n for n in range(47,92) if n not in {71,79,85}]
hashes=[]
for line in (root/'records/frozen_transcription.sha256').read_text().splitlines():
    if not line.strip(): continue
    digest,rel=line.split(maxsplit=1)
    rel=rel.lstrip('*')
    actual=hashlib.sha256((root/rel).read_bytes()).hexdigest()
    assert actual==digest,(rel,digest,actual)
    hashes.append((rel,actual))
assert len(hashes)==43

inventory=list(csv.DictReader((root/'MPL_93_047-091_inventory.csv').open(newline='')))
assert len(inventory)==1020 and all(r['transcribed']=='yes' for r in inventory)
pages={int(r['scan']):r['sheet_kind'] for r in inventory}
assert sorted(pages)==expected
assert Counter(pages.values())=={'typed':6,'reused_typed':8,'cover':3,'text':25}

notes=(root/'MPL_93_047-091_notes.md').read_text()
note_ids=re.findall(r'^### ((?:BT|EC|SC|OP|HC)\d+|S20-\d+) —',notes,re.M)
assert len(note_ids)==len(set(note_ids))==315
events=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(newline=''),delimiter='\t'))
assert len(events)==424
assert set(note_ids)<={r['statement_id'] for r in events}
valid_types={'targeted proof check','independent re-proof','computation or formal certificate',
    'used and rechecked in this run','carried as background without fault found',
    "refuted, with the refined statement's id"}
assert all(r['type'] in valid_types and all(r.values()) for r in events)
assert all('GPT-6 Astra Pro' in r['who'] and 'effort' in r['who'] and 'MPL_93_047-091' in r['who'] for r in events)
assert not re.search(r'turn\d+(?:search|view|fetch)\d+',notes)

for name in ['MPL_93_047-091_notes.md','MPL_93_047-091_doubts.md']:
    expected_cells=None
    for number,line in enumerate((root/name).read_text().splitlines(),1):
        if not line.startswith('|'):
            expected_cells=None;continue
        cells=len(re.findall(r'(?<!\\)\|',line))-1
        if expected_cells is None: expected_cells=cells
        else: assert cells==expected_cells,(name,number,cells,expected_cells)

result=subprocess.run([sys.executable,str(root/'scripts/validate_package.py')],capture_output=True,text=True)
assert result.returncode==0,result.stdout+result.stderr

report=[
    f'Final pre-packaging validation: {stamp}',
    'Frozen transcription: all43 SHA-256 values unchanged (42 page files plus combined fragment).',
    'Pages: exactly42 in requested ascending order; blanks071,079,085 excluded.',
    'Combined transcription: exact validated page concatenation.',
    'Inventory:1020 elements, all transcribed=yes; per-page IDs unique and contiguous.',
    'Sheet classes:6 typed,8 reused_typed,25 text,3 cover.',
    'Research notes:315 unique item IDs; all have check-event coverage.',
    'CHECK_EVENTS.tsv:424 rows; correct schema, allowed event types, model/effort/run attribution.',
    'Main notes and doubts: Markdown table column counts consistent.',
    'Research source citations: primary URLs in source registers; no retrieval IDs in main report.',
    'Actual context-search registers: root68 notes, BT69, EC60, SC118, totaling315 notes.',
    'Pre-freeze syntax record:42/42 fragments passed; no recompilation-driven transcription edits after freeze.',
    'Mechanical checks do not certify every visual reading or prove the unresolved research statements.',
    '',result.stdout.strip(),'',
    'Final frozen-hash comparison:'
]
report += [digest+'  '+rel for rel,digest in hashes]
(root/'records/final_validation.txt').write_text('\n'.join(report)+'\n')

status=f'''# Final work status

Updated {stamp}

All42 supplied pages are transcribed, reread, inventoried, and visually audited by the root alone. The combined fragment and all42 page files remain byte-for-byte identical to the SHA-256 freeze at10:49:51 UTC; context was first opened at10:49:56 UTC. The final hash comparison is recorded in `final_validation.txt` and `progress.log`.

The deliverables are complete: diplomatic transcription,42 page files,1,020-element inventory, notation/doubts/abbreviations/legibility report,315 itemized research notes,424 check events, progress log, proof records, actual context searches, and reproducing scripts. Post-freeze research and peer review are documented in `method.md` and the check ledger. Questions which could not be settled remain explicitly labeled; no reading was changed to match a source or a mathematical expectation.

Final structural and research-coverage checks passed. The final archive is prepared from this directory with input scans, supplied context, downloaded sources, caches, and earlier checkpoints excluded; ZIP CRC is checked by the packaging command. The three hourly checkpoints already saved are01–03. Work is complete before the next checkpoint due at11:47:46 UTC, so no extra off-schedule checkpoint is created.

The transcription is frozen. Do not rerun the earlier transcription-building or doubt-rebuilding scripts as a research operation; they are preserved solely as work records. The final report assembler and final-validation script do not modify any frozen transcription file.
'''
(root/'records/current_status.md').write_text(status)
with (root/'progress.log').open('a') as f:
    f.write(f'post-freeze research completed {stamp};315 notes;424 check events; source, context and peer-review records assembled\n')
    f.write(f'report formatting checked {stamp}; escaped one literal table bar in notation metadata only; no doubt reading or transcription changed\n')
    f.write(f'final frozen-hash verification {stamp}; all43 hashes unchanged from10:49:51 UTC (42 pages and combined transcription)\n')
    for rel,digest in hashes:
        f.write(f'SHA-256 unchanged {digest}  {rel}\n')
    f.write(f'final validation passed {stamp};42 pages;1020 inventory elements all yes;315 notes with complete event coverage; ready for final ZIP and persistent save\n')
print('\n'.join(report[:13]))
