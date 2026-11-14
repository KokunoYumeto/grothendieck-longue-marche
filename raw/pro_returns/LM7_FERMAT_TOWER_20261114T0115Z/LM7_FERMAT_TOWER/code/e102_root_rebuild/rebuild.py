"""Fresh copied-source and copied-input execution of the complete E102 Smith map."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent;ROOT=HERE.parent
SRC=ROOT/'research_e102'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
code=HERE/'code';code.mkdir(exist_ok=True)
program=code/'e_kernel_degree4_smith.py'
assert not program.exists()
shutil.copyfile(SRC/'code'/program.name,program)
source_input=ROOT/'research_e100/code/a_s23_full.json'
shutil.copyfile(source_input,code/source_input.name)
with program.with_suffix('.out').open('w') as out:
    run=subprocess.run([sys.executable,str(program)],cwd=HERE,
                       stdout=out,stderr=subprocess.STDOUT,check=False)
assert run.returncode==0,run.returncode
comparisons=[]
for ext in ['.out','.json','.npz']:
    original=(SRC/'code'/program.name).with_suffix(ext)
    fresh=program.with_suffix(ext)
    same=original.read_bytes()==fresh.read_bytes()
    comparisons.append({'file':original.name,'original_sha256':sha(original),
                        'fresh_sha256':sha(fresh),'byte_equal':same})
    assert same,original.name
assert sha(source_input)==sha(code/source_input.name)
assert sha(program)==sha(SRC/'code'/program.name)
record={'status':'PASS','returncode':0,'source_sha256':sha(program),
        'section_sha256':sha(SRC/'sections/E_kernel_degree4_smith.tex'),
        'input_sha256':sha(source_input),'complete_byte_comparisons':comparisons,
        'comparison_exclusions':[]}
(HERE/'comparison.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2),flush=True)
