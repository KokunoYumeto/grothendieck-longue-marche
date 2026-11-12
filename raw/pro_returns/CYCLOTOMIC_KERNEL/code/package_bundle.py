"""Create the requested single ZIP, with checksums and an exact file inventory."""
import hashlib
import json
import zipfile
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ROOT_FILES=[
 'CYCLOTOMIC_KERNEL_paper.tex','CYCLOTOMIC_KERNEL_paper.pdf',
 'CYCLOTOMIC_KERNEL_results.csv','CYCLOTOMIC_KERNEL_readings.csv',
 'CYCLOTOMIC_KERNEL_references.bib','CYCLOTOMIC_KERNEL_report.md',
 'CYCLOTOMIC_KERNEL_source_audit.md','coverage.json',
]
paths=[ROOT/name for name in ROOT_FILES]
assert all(p.is_file() for p in paths)
for folder in ['sections','code']:
    paths.extend(p for p in sorted((ROOT/folder).iterdir())
                 if p.is_file() and p.suffix in {'.py','.sh','.md','.tex','.bib','.json','.txt','.out'}
                 and p.name!='package_bundle_output.json')
assert len(paths)==len(set(paths))
names=[p.relative_to(ROOT).as_posix() for p in paths]
summary={'zip_name':'CYCLOTOMIC_KERNEL.zip',
         'files_including_manifest_and_packaging_record':len(paths)+2,
         'files_before_manifest_and_packaging_record':sorted(names),
         'zip_crc_check':'passed',
         'literature_pdfs_redistributed':False,
         'compiler_auxiliary_files_included':False}
record=ROOT/'code/package_bundle_output.json'
record.write_text(json.dumps(summary,indent=2)+'\n')
paths.append(record)
manifest=ROOT/'SHA256SUMS'
manifest.write_text(''.join(hashlib.sha256(p.read_bytes()).hexdigest()+'  '+
                            p.relative_to(ROOT).as_posix()+'\n'
                            for p in sorted(paths)))
paths.append(manifest)
archive=ROOT.parent/'CYCLOTOMIC_KERNEL.zip'
with zipfile.ZipFile(archive,'w',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in sorted(paths):
        z.write(p,(Path(ROOT.name)/p.relative_to(ROOT)).as_posix())
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None
    assert len(z.namelist())==len(paths)
    for p in paths:
        assert z.read((Path(ROOT.name)/p.relative_to(ROOT)).as_posix())==p.read_bytes()
print(json.dumps(summary,indent=2))
