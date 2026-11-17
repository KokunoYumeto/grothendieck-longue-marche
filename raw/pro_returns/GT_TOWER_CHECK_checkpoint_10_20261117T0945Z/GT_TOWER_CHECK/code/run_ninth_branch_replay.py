#!/usr/bin/env python3
"""Replay every exact branch surface source word in an isolated directory."""
from pathlib import Path
import shutil,subprocess,hashlib,json,time
ROOT=Path(__file__).resolve().parents[1]
source=ROOT.parent/'work/tower_code/finite_branch_surface_source.py'
out=ROOT/'notes/reproduced/ninth_branch_surface'
out.mkdir(parents=True,exist_ok=True)
target=out/source.name;shutil.copy2(source,target)
start=time.monotonic()
proc=subprocess.run(['python3',str(target)],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,text=True)
target.with_suffix('.root.out').write_text(proc.stdout)
record={'program':source.name,'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'exit':proc.returncode,'seconds':round(time.monotonic()-start,3),'output':proc.stdout}
(out/'manifest.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2));assert proc.returncode==0
