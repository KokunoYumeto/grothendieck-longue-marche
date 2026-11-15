#!/usr/bin/env python3
"""Package the frozen edition and compact final verification records."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,zipfile
r=Path(__file__).resolve().parents[1]
now=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
frozen=json.loads((r/'records/frozen_hashes.json').read_text())
checks=[{'file':n,'expected_sha256':h,'actual_sha256':hashlib.sha256((r/n).read_bytes()).hexdigest()} for n,h in frozen.items()]
assert len(checks)==42 and all(x['expected_sha256']==x['actual_sha256'] for x in checks)
(r/'records/final_hash_verification.json').write_text(json.dumps({'checked_utc':now,'all_unchanged':True,'files':checks},indent=2)+'\n')
files=[r/n for n in ['DELIVERY_README.txt','MPL_14_087-132_transcription.tex','MPL_14_087-132_doubts.md','MPL_14_087-132_inventory.csv','MPL_14_087-132_notes.md','progress.log']]
files+=sorted((r/'pages').glob('*.tex'))
files+=sorted((r/'records').glob('scan[0-9][0-9][0-9].json'))
files += [r/'records'/n for n in ['frozen_hashes.json','final_hash_verification.json','notation_comparison.json','validation_final.json','note_context_searches.json','research_notes_audit.json','research_notes_human_review.json','delivery_verification.json','checkpoint_02_receipt.json','qa_macros.tex','tex_qa_final/report.json','tex_qa_final/post_compile_hash_verification.json']]
files += [r/'scripts'/n for n in ['validate_package.py','audit_research_notes.py','context_lookup.py','package_final.py']]
assert len(files)==len(set(files)) and all(p.is_file() for p in files)
manifest=''.join(f'{hashlib.sha256(p.read_bytes()).hexdigest()}  {p.relative_to(r).as_posix()}\n' for p in sorted(files))
(r/'MANIFEST.sha256').write_text(manifest)
files.append(r/'MANIFEST.sha256')
output=r.parent/'MPL_14_087-132.zip'
assert not output.exists(),'Refusing to overwrite final archive'
with zipfile.ZipFile(output,'x',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
 for p in sorted(files):z.write(p,p.relative_to(r))
with zipfile.ZipFile(output) as z:
 assert z.testzip() is None
 assert len(z.namelist())==len(files)
 assert len([n for n in z.namelist() if n.startswith('pages/') and n.endswith('.tex')])==41
 for line in manifest.splitlines():
  expected,name=line.split('  ',1)
  assert hashlib.sha256(z.read(name)).hexdigest()==expected,name
 for n,h in frozen.items():assert hashlib.sha256(z.read(n)).hexdigest()==h,n
receipt={'archive':str(output),'created_utc':now,'members':len(files),'bytes':output.stat().st_size,'sha256':hashlib.sha256(output.read_bytes()).hexdigest(),'zip_crc':'passed','manifest_check':'passed for every member','frozen_tex_hashes_in_zip':'all 42 unchanged','library_upload':'pending'}
(r/'records/final_zip_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt))
