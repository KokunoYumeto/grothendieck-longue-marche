"""Correct the E98 prose export of the double-derived symbol; retain provenance."""
from pathlib import Path
import hashlib
import json

BASE=Path(__file__).resolve().parents[1]
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
old='R=N, and exact product ranks beginning504 in degree4.'
new="R=N'', and exact product ranks beginning504 in degree4."
paths=[BASE/'ledger/e_split7_complete_results.json',
       BASE/'ledger/e_split7_complete_coverage_notes.json',BASE/'code/assemble.py']
records=[]
for p in paths:
    before=p.read_text();count=before.count(old);assert count>0,(p,count)
    after=before.replace(old,new)
    original_sha=sha(p);p.write_text(after)
    records.append({'path':str(p.relative_to(BASE)),'occurrences':count,
                    'before_sha256':original_sha,'after_sha256':sha(p)})
record={'status':'PASS','reason':"The metadata freezer used adjacent single-quoted Python strings around N'', so its prose summary lost the two prime marks. The complete theorem/proof and every numerical computation already use R=N'' correctly. This exact textual correction affects only the presented ledger and generated-coverage source.",
        'old_text':old,'new_text':new,'changed_files':records,
        'unchanged_complete_proof_sha256':sha(BASE/'sections/E_split7_complete.tex'),
        'frozen_author_program_and_output_retained':True}
(BASE/'ledger/e98_metadata_correction.json').write_text(json.dumps(record,indent=2)+'\n')
print('PASS E98 double-derived symbol restored in all three presented metadata sources; proof and numerical certificates unchanged.',flush=True)
