#!/usr/bin/env python3
"""Assemble the final deliverable without its supplied images or sources.

This reads the frozen transcription and supporting work files, checks the
recorded hashes, writes a new ZIP beside the package directory, and verifies
its contents. It never rewrites the transcription or opens the context.
"""
from pathlib import Path
import hashlib,json,zipfile

base=Path(__file__).resolve().parents[1]
out=base.parent/'MPL_122.zip'
expected=json.loads((base/'work/frozen_hashes.json').read_text())
for name,digest in expected.items():
    assert hashlib.sha256((base/name).read_bytes()).hexdigest()==digest,name

allowed={'.tex','.md','.csv','.log','.json','.py','.txt'}
files=sorted(p for p in base.rglob('*') if p.is_file()
             and p.suffix.lower() in allowed and '__pycache__' not in p.parts)
with zipfile.ZipFile(out,'w',zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p in files:
        z.write(p,p.relative_to(base).as_posix())
with zipfile.ZipFile(out) as z:
    assert z.testzip() is None
    names=set(z.namelist())
    required={'MPL_122_transcription.tex','MPL_122_doubts.md',
              'MPL_122_inventory.csv','MPL_122_notes.md','progress.log'}
    assert required<=names
    assert len([n for n in names if n.startswith('pages/') and n.endswith('.tex')])==32
    for name,digest in expected.items():
        assert hashlib.sha256(z.read(name)).hexdigest()==digest,name
    assert not any(Path(n).suffix.lower() in {'.jpg','.jpeg','.png','.pdf','.zip'} for n in names)
print(json.dumps({'path':str(out),'files':len(files),
                  'bytes':out.stat().st_size,
                  'sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
                  'crc_check':'passed','frozen_hashes_in_zip':'all 33 match'},
                 indent=2))

