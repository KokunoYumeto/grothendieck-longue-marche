"""Verify the packaged deliverable and its frozen transcription bytes."""
from pathlib import Path
import hashlib,json,zipfile
R=Path(__file__).resolve().parents[1];archive=R.parent/'deliverables/SP85_C13_149.zip'
required={'SP85_C13_149_transcription.tex','SP85_C13_149_changes.md','SP85_C13_149_collation.tsv','decisions.tsv','SP85_C13_149_doubts.md','SP85_C13_149_inventory.csv','SP85_C13_149_notes.md','CHECK_EVENTS.tsv','progress.log','SP85_C13_149_sheet_feedback.md','SP85_C13_149_hand_log.md','records/transcription_freeze.json','records/validation.json'}
with zipfile.ZipFile(archive) as z:
 names=set(z.namelist());assert required<=names,required-names
 assert z.testzip() is None
 assert len([n for n in names if n.startswith('pages/') and n.endswith('.tex')])==23
 assert not any(n.endswith('.zip') or n.startswith(('source/','upload/','reader_packets/')) or '/halves/' in n for n in names)
 assert not any(n.endswith('PREAMBLE.tex') or n.endswith('MARKS.tsv') for n in names)
 freeze=json.loads(z.read('records/transcription_freeze.json'))
 assert len(freeze['sha256'])==24
 for name,digest in freeze['sha256'].items():assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
 assert json.loads(z.read('records/validation.json'))['passed'] is True
 assert 'transcription hashes verified unchanged' in z.read('progress.log').decode()
report={'archive':archive.name,'members':len(names),'bytes':archive.stat().st_size,'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'frozen_transcription_hashes_verified':24,'original_inputs_and_checkpoint_zips_excluded':True}
print(json.dumps(report))
