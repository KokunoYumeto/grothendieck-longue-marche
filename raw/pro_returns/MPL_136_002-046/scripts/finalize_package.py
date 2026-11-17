"""Verify the frozen transcription and assemble the complete final archive.

This never changes any page file or the combined transcription.
"""
from pathlib import Path
from datetime import datetime, timezone
import hashlib, json, re, subprocess, sys, zipfile
from create_checkpoint import eligible_for_checkpoint

root=Path(__file__).resolve().parents[1]
package='MPL_136_002-046'
archive_path=root.parent/f'{package}.zip'
assert not archive_path.exists(), 'Refusing to overwrite the final archive.'
log_path=root/'progress.log'
log=log_path.read_text()
assert 'transcription frozen' in log and 'context opened' in log
frozen_part=log.split('context opened',1)[0]
hashes=re.findall(r'^SHA-256 ([0-9a-f]{64}) (.+)$',frozen_part,re.M)
assert len(hashes)==45
for digest,name in hashes:
    assert hashlib.sha256((root/name).read_bytes()).hexdigest()==digest,name

notes=(root/f'{package}_notes.md').read_text()
ids=re.findall(r'^### ((?:L|SH|NH|D)\d+)\b',notes,re.M)
expected={f'L{i:03}' for i in range(1,45)} | {f'SH{i:02}' for i in range(1,26)} | {f'NH{i:02}' for i in range(1,16)} | {f'D{i:03}' for i in range(1,14)}
assert len(ids)==97 and set(ids)==expected and len(set(ids))==97
assert not any(x in notes for x in ['section is still being drafted','This section is being drafted'])

def ledger_ids(filename):
    data=json.loads((root/'research'/filename).read_text())['notes']
    if isinstance(data,dict):
        return set(data)
    found=set()
    for item in data:
        for key in ['id','note_id','note']:
            if key in item and isinstance(item[key],str):
                found.add(item[key]); break
    return found

ledgers=[('lecture_searches.json',{f'L{i:03}' for i in range(1,45)}),
         ('shadow_searches.json',{f'SH{i:02}' for i in range(1,26)}),
         ('negative_hom_searches.json',{f'NH{i:02}' for i in range(1,16)}),
         ('documentary_context_searches.json',{f'D{i:03}' for i in range(1,14)})]
for filename,expected_ids in ledgers:
    assert ledger_ids(filename)==expected_ids,(filename,ledger_ids(filename))

now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with log_path.open('a') as f:
    f.write(f'research completed {now}; 97 itemized notes (44 lecture, 25 shadows, 15 homogeneous-Hom, 13 documentary); all 97 have supplied-context search records\n')
    f.write(f'editorial Markdown table escaping corrected {now}; notation-table pipe only, no reading or transcription changed\n')
    f.write(f'frozen hashes unchanged {now}; all 44 page files and combined transcription match the 45 SHA-256 values recorded before context opened\n')

validation=subprocess.run([sys.executable,str(root/'scripts/validate_package.py'),'--final','--json'],capture_output=True,text=True)
assert validation.returncode==0,validation.stdout+validation.stderr
report=json.loads(validation.stdout)
assert report['passed'] and not report['issues'],report['issues']
(root/'scripts/final_validation.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

state=f'''# Final work state

Completed at {now}.

- All 44 supplied scans 002–046, except blank 019, have saved page files and UTC completion records.
- All 44 have a second visual audit record; root was the sole image reader and transcriber, and no OCR was used.
- The recurring notation comparison was completed before freezing.
- The combined fragment is the exact ordered byte concatenation of the page files.
- The transcription froze at 2026-11-17 15:04:33 UTC; context opened at 15:04:34 UTC.
- All 45 frozen SHA-256 values were checked unchanged at completion.
- The inventory has 902 elements, all marked yes.
- The complete research report has 97 itemized notes and the two requested standing-question sections; every note has a recorded context search.
- The doubts file includes the notation table, chronological corrections, abbreviation guide, and legibility limits.
- Final structural validation passed with zero errors and zero warnings; this does not certify readings or mathematics.
- TeX compilation was unavailable because installed engines lacked format files; the attempted compiler did not read the manuscript.
- Hourly checkpoints 01 and 02 were created and persisted at the scheduled hours; their receipts are in scripts/. No additional checkpoint was made between the scheduled hours.
- The complete canonical deliverables are described in README.md. Research source drafts and scripts are work records, not unfinished substitute deliverables.

Do not rerun transcription, freezing, or context opening: these stages are complete. Any future alternative reading belongs to a new explicitly authorized revision, preserving this frozen return.
'''
(root/'WORK_STATE.md').write_text(state)
with log_path.open('a') as f:
    f.write(f'final package prepared {now}; required deliverables complete; final structural validation 0 errors, 0 warnings; source inputs and older ZIPs excluded\n')

paths=[p for p in sorted(root.rglob('*')) if eligible_for_checkpoint(p,root)]
with zipfile.ZipFile(archive_path,'x',zipfile.ZIP_DEFLATED) as z:
    for path in paths:
        z.write(path,path.relative_to(root))
with zipfile.ZipFile(archive_path) as z:
    assert z.testzip() is None
    for digest,name in hashes:
        assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
    assert not any(n.startswith(('upload/','uploads/','scans/','context/')) or n.endswith('.zip') for n in z.namelist())
print(json.dumps({'path':str(archive_path),'bytes':archive_path.stat().st_size,
                  'archive_entries':len(paths),'research_items':len(ids),
                  'frozen_hashes_verified':len(hashes),
                  'zip_sha256':hashlib.sha256(archive_path.read_bytes()).hexdigest()},indent=2))
