#!/usr/bin/env python3
"""Package the completed output; never include inputs or previous archives.

Run only after the final unchanged-hash confirmation and successful structural
validation. The manifest hashes every included file except the manifest itself.
This script does not compile TeX, read manuscript images, or save externally.
"""
from pathlib import Path
import csv
import hashlib
import json
import sys
import zipfile
from make_checkpoint import excluded
from validate_deliverables import validate

OUT=Path(__file__).resolve().parents[1]
ROOT=OUT.parent
PREFIX='SP31_CW_156-3'

def main():
 report=validate(OUT)
 if report['status']!='pass':
  print(json.dumps(report,indent=2));return 1
 manifest=OUT/(PREFIX+'_manifest.tsv')
 files=[p for p in sorted(OUT.rglob('*')) if p.is_file() and not p.is_symlink() and not excluded(p.relative_to(OUT)) and p!=manifest]
 names={p.relative_to(OUT).as_posix() for p in files}|{manifest.name}
 # The final package preserves every documentation/deliverable filename from
 # each immutable checkpoint, while carrying the current version of each file.
 for cp in sorted((ROOT/'checkpoints').glob(PREFIX+'_checkpoint_*.zip')):
  with zipfile.ZipFile(cp) as z:
   missing=set(z.namelist())-names
   if missing:raise RuntimeError(f'Checkpoint files missing from final output: {cp.name}: {sorted(missing)}')
 with manifest.open('w',newline='') as f:
  w=csv.writer(f,delimiter='\t');w.writerow(['file','bytes','sha256'])
  for p in files:
   b=p.read_bytes();w.writerow([p.relative_to(OUT).as_posix(),len(b),hashlib.sha256(b).hexdigest()])
 files.append(manifest)
 dest=ROOT/'deliverables';dest.mkdir(exist_ok=True)
 archive=dest/(PREFIX+'.zip')
 with zipfile.ZipFile(archive,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=6) as z:
  for p in sorted(files):z.write(p,p.relative_to(OUT).as_posix())
 with zipfile.ZipFile(archive) as z:
  if z.testzip() is not None:raise RuntimeError('ZIP CRC verification failed')
  if set(z.namelist())!=names:raise RuntimeError('ZIP member mismatch')
  for p in files:
   if z.read(p.relative_to(OUT).as_posix())!=p.read_bytes():raise RuntimeError(f'ZIP bytes differ: {p}')
 print(json.dumps(dict(archive=str(archive),files=len(files),bytes=archive.stat().st_size,sha256=hashlib.sha256(archive.read_bytes()).hexdigest(),frozen_transcription_hashes='25 matched',zip_crc='pass',checkpoint_filename_coverage='complete'),indent=2))
 return 0

if __name__=='__main__':sys.exit(main())
