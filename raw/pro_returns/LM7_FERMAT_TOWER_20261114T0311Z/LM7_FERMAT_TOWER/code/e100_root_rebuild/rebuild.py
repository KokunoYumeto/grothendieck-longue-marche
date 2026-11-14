"""Rebuild all frozen E100 calculations from the exact copied integral input."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SOURCE=ROOT/'research_e100'
BASE=ROOT/'LM7_FERMAT_TOWER/code'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=SOURCE/'ledger/e_two_three_full_manifest.json'
manifest=json.loads(manifest_path.read_text())
for name,digest in manifest['files'].items():
    assert sha(SOURCE/name)==digest,name
for name,digest in manifest['inputs'].items():
    assert sha(ROOT/name)==digest,name
code=HERE/'code';inputs=HERE/'inputs'
code.mkdir(exist_ok=True);inputs.mkdir(exist_ok=True)
program=code/'a_s23_full.py'
assert not program.exists()
shutil.copyfile(SOURCE/'code'/program.name,program)
helper='e_unramified_sections.py'
shutil.copyfile(BASE/helper,inputs/helper)
shutil.copyfile((BASE/helper).with_suffix('.out'),(inputs/helper).with_suffix('.out'))
with program.with_suffix('.out').open('w') as output:
    run=subprocess.run([sys.executable,str(program),'--source-code',str(inputs)],
                       cwd=HERE,stdout=output,stderr=subprocess.STDOUT,check=False)
assert run.returncode==0,run.returncode
comparisons=[]
for ext in ['.json','.out']:
    original=SOURCE/'code'/program.with_suffix(ext).name
    rebuilt=program.with_suffix(ext)
    same=original.read_bytes()==rebuilt.read_bytes()
    comparisons.append({'file':original.name,'source_sha256':sha(original),
                        'fresh_sha256':sha(rebuilt),'byte_equal':same})
    assert same,original.name
assert sha(inputs/helper)==sha(BASE/helper)
record={'status':'PASS','returncode':run.returncode,
        'section_sha256':sha(SOURCE/'sections/E_two_three_full.tex'),
        'source_sha256':sha(program),'frozen_manifest_sha256':sha(manifest_path),
        'complete_byte_comparisons':comparisons,'comparison_exclusions':[],
        'unchanged_input_sha256':sha(inputs/helper)}
(HERE/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
