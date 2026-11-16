#!/usr/bin/env python3
"""Create a fresh, immutable hourly checkpoint or final ZIP.

Usage: python code/package_return.py checkpoint 01
       python code/package_return.py final
The command refuses to overwrite any existing archive.
"""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,sys,zipfile
root=Path(__file__).resolve().parents[1]
mode=sys.argv[1]
if mode=='checkpoint':
    serial=f'{int(sys.argv[2]):02d}'
    name=f'LM8_PUSH_checkpoint_{serial}.zip'
elif mode=='final':
    raise SystemExit('Use package_compact_checkpoint.py SERIAL STORAGE_PLAN.json --final after materialize_checkpoint_history.py. Raw checkpoint concatenation is superseded; the successful saved-path catalog and complete verified history are mandatory.')
else:raise SystemExit('mode must be checkpoint or final')
dest=root.parent/name
if dest.exists():raise SystemExit('Refusing to overwrite '+str(dest))
excluded=('build/tex-cache/','__pycache__/','background/','inputs/')
omitted_intermediates={
    'notes/de_compile/de_compile_check.pdf': 'Isolated bibliography-free compile test; superseded completely by LM8_PUSH_paper.pdf. Source and logs retained.',
    'notes/de_compile/de_prosolvable_compile.pdf': 'Isolated local-proof compile test; superseded completely by LM8_PUSH_paper.pdf. Source and logs retained.',
    'notes/de_compile/de_compile_D62_D63.pdf': 'Isolated D.62--D.63 compile test with unresolved stand-alone bibliography; superseded completely by the integrated LM8_PUSH_paper.pdf. Source and logs retained.',
    'notes/de_compile/de_compile_D64.pdf': 'Isolated D.64 layout test; superseded completely by the integrated LM8_PUSH_paper.pdf. Source and logs retained.',
    'notes/de_compile/de_compile_D60.pdf': 'Isolated D.60 compile test; superseded completely by the integrated LM8_PUSH_paper.pdf. Source and logs retained.',
    'notes/de_compile/de_compile_D61.pdf': 'Isolated D.61 compile test; superseded completely by the integrated LM8_PUSH_paper.pdf. Source and logs retained.',
    'notes/de_compile/de_compile_D65.pdf': 'Isolated D.65 layout test, fully reviewed at checkpoint08; superseded completely by the integrated LM8_PUSH_paper.pdf from checkpoint09. Source, logs, and prior checkpoint copy retained.',
}
files=[]
for p in sorted(root.rglob('*')):
    if not p.is_file():continue
    rel=p.relative_to(root).as_posix()
    if any(rel.startswith(x) or ('/'+x) in rel for x in excluded):continue
    if rel in omitted_intermediates:continue
    if p.suffix=='.pyc':continue
    # Read each file once: running computations may append to their own logs.
    # The manifest and ZIP must describe exactly the same captured bytes.
    files.append((p,rel,p.read_bytes()))
manifest={'created_utc':datetime.now(timezone.utc).isoformat(),
          'kind':mode,'file_count':len(files),'files':[
    {'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
    for p,rel,data in files],
    'compression_policy':{'default_deflate_level':9,
                          'large_file_threshold_bytes':10000000,
                          'large_raw_file_deflate_level':6,
                          'large_gzip_files':'stored without recompression; captured bytes unchanged'},
    'omitted_intermediates':omitted_intermediates,
    'exclusions':['User-supplied background archive, extracted sources, and reproducible downloaded primary-source caches; exact source URLs and page citations retained',
                  'Reproducible local TeX installation and font cache; installation script and checksums retained']}
with zipfile.ZipFile(dest,'x',compression=zipfile.ZIP_DEFLATED,compresslevel=9) as z:
    for p,rel,data in files:
        if len(data)>=10000000 and (p.suffix=='.gz' or p.name.endswith('.gz.incomplete_stream')):
            z.writestr(rel,data,compress_type=zipfile.ZIP_STORED)
        else:
            z.writestr(rel,data,compresslevel=6 if len(data)>=10000000 else 9)
    z.writestr('PACKAGE_MANIFEST.json',json.dumps(manifest,indent=2)+'\n')
with zipfile.ZipFile(dest) as z:
    bad=z.testzip()
    if bad:raise RuntimeError('ZIP CRC failure: '+bad)
print(json.dumps({'file':str(dest),'bytes':dest.stat().st_size,
                  'sha256':hashlib.sha256(dest.read_bytes()).hexdigest(),
                  'files':len(files)},indent=2))
