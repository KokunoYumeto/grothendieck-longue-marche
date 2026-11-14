"""Fresh copied four-stage E98 reconstruction, with complete byte comparisons."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
SOURCE=ROOT/'research_e98/code'
BASE=ROOT/'LM7_FERMAT_TOWER/code'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
code=HERE/'code';inputs=HERE/'inputs'
code.mkdir(exist_ok=True);inputs.mkdir(exist_ok=True)
names=['e_wild_layers.json','a_cusp_kummer.json','a_abelian_kernel_obstruction.json',
       'e_cusp_local_smith.py','a_horizontal_full.py']
hashes={name:sha(BASE/name) for name in names}
for name in names:
    assert not (inputs/name).exists()
    shutil.copyfile(BASE/name,inputs/name)
    if name.endswith('.py'):
        shutil.copyfile((BASE/name).with_suffix('.out'),(inputs/name).with_suffix('.out'))
programs=['e_global_split7_explore.py','e_global_split7_residues.py',
          'e_global_split7_central.py','e_global_split7_normal_forms.py']
sources={name:sha(SOURCE/name) for name in programs}
stages=[]
for name in programs:
    target=code/name;assert not target.exists()
    shutil.copyfile(SOURCE/name,target)
    command=[sys.executable,str(target)]
    if 'residues' not in name:command+=['--source-code',str(inputs)]
    with target.with_suffix('.out').open('w') as output:
        run=subprocess.run(command,cwd=HERE,stdout=output,stderr=subprocess.STDOUT,check=False)
    assert run.returncode==0,(name,run.returncode)
    stages.append({'program':name,'returncode':run.returncode,'source_sha256':sources[name]})
    print('PASS fresh execution',name,flush=True)
comparisons=[]
for name in programs:
    assert sha(SOURCE/name)==sources[name]
    for ext in ['.out','.json']:
        original=(SOURCE/name).with_suffix(ext);fresh=(code/name).with_suffix(ext)
        assert original.read_bytes()==fresh.read_bytes(),original.name
        comparisons.append({'file':original.name,'source_sha256':sha(original),
                            'fresh_sha256':sha(fresh),'byte_equal':True})
for name in names:assert sha(BASE/name)==sha(inputs/name)==hashes[name]
result={'status':'PASS','stages':stages,'complete_byte_comparisons':comparisons,
        'comparison_exclusions':[],'unchanged_input_hashes':hashes,
        'proof_sha256_at_execution':sha(ROOT/'research_e98/sections/E_split7_complete.tex')}
(HERE/'comparison.json').write_text(json.dumps(result,indent=2)+'\n')
print('PASS all eight COMPLETE JSON/stdout files byte-identical; no exclusions.',flush=True)
