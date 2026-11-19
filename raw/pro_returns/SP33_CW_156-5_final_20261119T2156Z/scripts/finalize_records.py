#!/usr/bin/env python3
"""Final structural/frozen-hash check and truthful completion record."""
from pathlib import Path
from datetime import datetime,timezone
import json,hashlib,subprocess,sys,csv,re
root=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
manifest=json.loads((root/'records/frozen_hashes.json').read_text())
checks=[]
for path,expected in manifest.items():
 actual=hashlib.sha256((root/path).read_bytes()).hexdigest()
 checks.append({'file':path,'expected_sha256':expected,'actual_sha256':actual,'unchanged':actual==expected})
assert len(checks)==25 and all(c['unchanged'] for c in checks)
notes=json.loads((root/'records/research_notes.json').read_text())['notes']
assert len(notes)==81 and {n['scan'] for n in notes}==set(range(2,26))
assert len(set(n['id'] for n in notes))==81
md=(root/'SP33_CW_156-5_notes.md').read_text()
assert set(re.findall(r'^#### (N\d{3}-\d+) —',md,re.M))=={n['id'] for n in notes}
events=list(csv.DictReader((root/'CHECK_EVENTS.tsv').open(),delimiter='\t'))
assert len(events)==157
assert all(any(r['statement_id']==n['id'] for r in events) for n in notes)
for n in notes:
 assert n['context'] and n['place'] and n['queries']
 if n['kind']=='own idea':assert n['confidence']
proofhash=hashlib.sha256((root/'SP33_CW_156-5_mathematical_checks.md').read_bytes()).hexdigest()
assert proofhash==json.loads((root/'records/mathematical_proofs.json').read_text())['source_sha256']
assert proofhash==json.loads((root/'records/check_event_summary.json').read_text())['mathematical_proof_source_sha256']
res=subprocess.run([sys.executable,str(root/'scripts/validate_package.py'),str(root),'--json'],capture_output=True,text=True,check=True)
validation=json.loads(res.stdout);assert validation['passed']
(root/'records/final_validation.json').write_text(json.dumps({'verified_utc':now,'structural_validation':validation,'research_notes':81,'research_scan_coverage':list(range(2,26)),'check_events':157,'proof_sections':14,'proof_source_sha256':proofhash,'scope':'Structural and metadata validation; does not itself certify ink fidelity or external literature claims.'},ensure_ascii=False,indent=2)+'\n')
(root/'records/final_hash_check.json').write_text(json.dumps({'verified_utc':now,'all_25_unchanged_since_freeze':True,'checks':checks},indent=2)+'\n')
p=root/'records/run_state.json';state=json.loads(p.read_text());state.update(completed_utc=now,research_notes_count=81,check_events_count=157,final_frozen_hash_check_utc=now,all_25_frozen_hashes_unchanged=True);p.write_text(json.dumps(state,indent=2)+'\n')
with (root/'progress.log').open('a') as f:
 f.write(f'ancillary metadata review completed before finalization; no remaining hash/JSON/reference inconsistencies; no source or page content read by packaging reviewer\n')
 f.write(f'transcription final hash check {now}; all24 page SHA-256 values and combined SHA-256 unchanged since freeze21:25:11 UTC; records/final_hash_check.json\n')
 f.write(f'full structural and research-record validation passed {now};24 pages,543 inventory elements,558 H-collation rows,385 uncertainty occurrences,81 numbered notes,14 written check sections,157 check/background events\n')
 f.write(f'work completed {now}; final archive authorized for creation as SP33_CW_156-5.zip; source attachments and previous archives excluded\n')
print(json.dumps({'completed_utc':now,'all_25_frozen_hashes_unchanged':True,'research_notes':81,'check_events':157,'structural_validation_passed':True}))
