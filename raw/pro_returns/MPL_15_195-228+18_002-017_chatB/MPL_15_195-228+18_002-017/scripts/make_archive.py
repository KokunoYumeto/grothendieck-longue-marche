#!/usr/bin/env python3
"""Package completed deliverables; exclude provided originals and generated caches."""
from pathlib import Path
import argparse, hashlib, json, zipfile
ROOT=Path(__file__).resolve().parents[1]
parser=argparse.ArgumentParser()
parser.add_argument('--utc',required=True)
args=parser.parse_args()
archive=ROOT.parent/(ROOT.name+'.zip')
assert not archive.exists(), 'An existing final archive must not be overwritten silently.'
frozen=json.loads((ROOT/'records/frozen_sha256.json').read_text())
for item in frozen['files']:
    assert hashlib.sha256((ROOT/item['file']).read_bytes()).hexdigest()==item['sha256']
validation=json.loads((ROOT/'records/final_validation_report.json').read_text())
assert validation['mechanical_checks_passed']
notes=json.loads((ROOT/'records/research_assembly_report.json').read_text())
assert notes['note_count']==78 and notes['standing_complete']
with (ROOT/'progress.log').open('a') as log:
    log.write('final archive preparation '+args.utc+'; complete deliverables and work records; supplied sources and generated Python caches excluded\n')
manifest=ROOT/'records/package_contents.json'
def selected():
    return sorted(p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.suffix!='.pyc')
files=[p for p in selected() if p!=manifest]
for p in files:
    assert p.suffix.lower() not in ('.jpg','.jpeg','.png','.pdf','.zip')
    assert not p.is_symlink()
contents={'prepared_utc':args.utc,'archive_name':archive.name,
          'excluded':'Supplied scan/source archives, extracted original scans/context documents, intermediate renders and generated Python caches.',
          'self_manifest':'This manifest is included; the following list covers every other member.',
          'member_count_including_this_manifest':len(files)+1,
          'files':[{'file':str(p.relative_to(ROOT)),'bytes':p.stat().st_size,'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for p in files]}
manifest.write_text(json.dumps(contents,ensure_ascii=False,indent=2)+'\n')
files=selected()
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as out:
    for p in files: out.write(p,arcname=str(Path(ROOT.name)/p.relative_to(ROOT)))
with zipfile.ZipFile(archive) as check:
    assert check.testzip() is None
    assert len(check.namelist())==len(files)
    for item in frozen['files']:
        assert hashlib.sha256(check.read(ROOT.name+'/'+item['file'])).hexdigest()==item['sha256']
    for item in contents['files']:
        assert hashlib.sha256(check.read(ROOT.name+'/'+item['file'])).hexdigest()==item['sha256']
receipt={'file':str(archive),'bytes':archive.stat().st_size,'members':len(files),
         'sha256':hashlib.sha256(archive.read_bytes()).hexdigest(),'zip_crc_check':'passed',
         'all_member_hashes_verified':True,'all_50_frozen_hashes_verified_inside_archive':True}
(ROOT.parent/'final_archive_receipt.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
