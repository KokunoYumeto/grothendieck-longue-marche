#!/usr/bin/env python3
"""Validate and save the single final ZIP, with a hash manifest of captured bytes."""
from pathlib import Path
import hashlib,json,subprocess,sys,zipfile
from package_files import distribution_files
ROOT=Path(__file__).resolve().parents[1]
PREFIX='LM8_LIE_APPROXIMATIONS'
subprocess.run([sys.executable,str(ROOT/'code/validate_package.py')],check=True)
destination=ROOT.parent/(PREFIX+'.zip')
if destination.exists():raise SystemExit('Refusing to overwrite an existing final ZIP: '+str(destination))
manifest_path=ROOT/'audit/final_manifest.json'
captured={str(p.relative_to(ROOT)):p.read_bytes() for p in distribution_files(ROOT)
          if p!=manifest_path}
manifest={'status':'INCOMPLETE; see the exact task matrix and residual statements',
          'files':[{'path':rel,'bytes':len(data),'sha256':hashlib.sha256(data).hexdigest()}
                   for rel,data in captured.items()]}
manifest_path.write_text(json.dumps(manifest,indent=2)+'\n')
captured[str(manifest_path.relative_to(ROOT))]=manifest_path.read_bytes()
with zipfile.ZipFile(destination,'x',zipfile.ZIP_DEFLATED,compresslevel=8) as z:
    for rel,data in captured.items():z.writestr(ROOT.name+'/'+rel,data)
with zipfile.ZipFile(destination) as z:
    assert z.testzip() is None
    for row in manifest['files']:
        assert hashlib.sha256(z.read(ROOT.name+'/'+row['path'])).hexdigest()==row['sha256']
print(json.dumps({'path':str(destination),'files':len(captured),
                  'bytes':destination.stat().st_size(),'sha256':hashlib.sha256(destination.read_bytes()).hexdigest()}))
