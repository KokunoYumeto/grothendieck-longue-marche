"""Independent E99 reconstruction from exact copied source and all five inputs."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SOURCE=ROOT/'research_e99'
BASE=ROOT/'LM7_FERMAT_TOWER/code'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest_path=SOURCE/'ledger/e_two_three_intrinsic_manifest.json'
manifest=json.loads(manifest_path.read_text())
for path,row in manifest['files'].items():
    assert sha(SOURCE/path)==row['sha256'],path
code=HERE/'code';inputs=HERE/'inputs'
code.mkdir(exist_ok=True);inputs.mkdir(exist_ok=True)
name='a_s23_intrinsic.py';program=code/name
assert not program.exists()
shutil.copyfile(SOURCE/'code'/name,program)
names=['e_unramified_sections.py','e_cusp_local_smith.py',
       'a_horizontal_full.py','e_wild_layers.json','a_cusp_kummer.json']
input_hashes={}
for name in names:
    p=BASE/name
    shutil.copyfile(p,inputs/name)
    input_hashes[name]=sha(p)
    if p.suffix=='.py':
        # Preserve the helpers' actual previously executed standalone output;
        # this run imports their functions and its complete stdout is separate.
        assert p.with_suffix('.out').is_file()
        shutil.copyfile(p.with_suffix('.out'),(inputs/name).with_suffix('.out'))
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
for name,value in input_hashes.items():
    assert sha(inputs/name)==sha(BASE/name)==value
record={'status':'PASS','returncode':run.returncode,
        'section_sha256':sha(SOURCE/'sections/E_two_three_intrinsic.tex'),
        'source_sha256':sha(program),'frozen_manifest_sha256':sha(manifest_path),
        'complete_byte_comparisons':comparisons,'comparison_exclusions':[],
        'unchanged_input_hashes':input_hashes}
(HERE/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
