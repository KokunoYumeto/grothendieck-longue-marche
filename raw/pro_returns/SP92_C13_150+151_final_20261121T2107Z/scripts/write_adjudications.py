"""Transcribe root's explicit crop decisions into the immutable comparison record.

This script makes no reading decision. The notes JSON must be written by root
after viewing every differing crop; every key is mandatory. Page edits and
updates to witness/mark records must already have been made separately.
"""
from pathlib import Path
import json, sys, datetime

W=Path(__file__).resolve().parents[1]
page, reader=sys.argv[1:3]
comparison=json.loads((W/'second'/f'{page}_comparison.json').read_text())
notes=json.loads((W/'second'/f'{page}_root_crop_notes.json').read_text())
repair_path=W/'records/v_encoding_repairs.json'
repairs=json.loads(repair_path.read_text()).get(page,{}) if repair_path.exists() else {}
different={x['box']:x for x in comparison['results'] if not x['identical_tokens']}
assert set(notes)==set(different), 'Explicit root note required for every differing box.'
rows=[]
for box,r in different.items():
    note=notes[box]
    assert note.get('viewed') is True and note.get('evidence')
    crop=f'crops/{page}_blind_{box}.png'
    assert (W/crop).exists()
    changed=note.get('changed',False)
    assert isinstance(changed,bool)
    final=note.get('final',repairs.get(box,r['first']))
    assert not changed or final!=r['first'], 'A changed box needs its written final reading.'
    rows.append(dict(box=box,first=r['first'],second=r['second'],final=final,
                     root_viewed=True,crop=crop,coordinates=r['coordinates'],
                     evidence=note['evidence'],changed=changed,
                     representation_only_repair=box in repairs,
                     token_difference_count=len(r['token_differences'])))
out=W/'second'/f'{page}_adjudications.json'
assert not out.exists(), 'Do not overwrite an adjudication.'
out.write_text(json.dumps(dict(page=page,reader=reader,root_reviewed=True,
    adjudicated_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
    adjudications=rows),ensure_ascii=False,indent=2)+'\n')
print(f'{page}: {len(rows)} explicit crop decisions transcribed.')
