"""Root audit of the frozen D59 files and actual copied-source execution."""
from pathlib import Path
import hashlib
import json
import shutil
import subprocess
import sys

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/'D59_EXPERIMENTS'
HERE=Path(__file__).resolve().parent
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
manifest=SOURCE/'ledger/d_free_character_invariant_lift_manifest.json'
assert sha(manifest)=='9a056e24d49af436073a27dcb818732ebf7d7c16956937e8442226ec4882bebe'
frozen=json.loads(manifest.read_text())
for row in frozen['files']+frozen['immutable_inputs']:
    p=SOURCE/row['path']
    assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
proof=SOURCE/'sections/D_free_character_invariant_lift.tex'
assert sha(proof)=='221b3d0035327edff2d3b060abc62be7534df8e03b9682fb12f626324cd664c6'
work=HERE/'fresh/code'
assert not work.exists()
work.mkdir(parents=True)
names=['d_arithmetic_free_characters.py','d_arithmetic_affine_base.json','d_arithmetic_correction_graph.json']
for name in names:shutil.copy2(SOURCE/'code'/name,work/name)
program=work/names[0]
with program.with_suffix('.out').open('wb') as out:
    result=subprocess.run([sys.executable,str(program)],stdout=out,stderr=subprocess.STDOUT)
assert result.returncode==0,result.returncode
checks=[]
for suffix in ['.out','.json']:
    a=json.loads((SOURCE/'code'/names[0]).with_suffix(suffix).read_text())
    b=json.loads(program.with_suffix(suffix).read_text())
    if suffix=='.json':
        a['summary'].pop('elapsed_seconds');b['summary'].pop('elapsed_seconds')
        excluded='/summary/elapsed_seconds'
    else:
        a.pop('elapsed_seconds');b.pop('elapsed_seconds')
        excluded='/elapsed_seconds'
    assert a==b,suffix
    checks.append({'suffix':suffix,'all_remaining_fields_equal':True,
                   'only_excluded_field':excluded,'actual_fresh_sha256':sha(program.with_suffix(suffix))})
record={'status':'PASS','proof_sha256':sha(proof),'manifest_sha256':sha(manifest),
        'owned_file_hashes_verified':len(frozen['files']),
        'immutable_input_hashes_verified':len(frozen['immutable_inputs']),
        'actual_exit_code':result.returncode,'source_sha256':sha(program),'checks':checks,
        'proof_read_scope':'Root read the entire frozen D59 statement and proof, all 525 lines, plus its entire main program and the needed exact D55 norm/orientation proof. D58 source and fibre-product repairs had already received a full root proof audit.',
        'mathematical_checks':[
          'Actual Q graph, mod-three cusp vectors and affine fixed-space count; active lower bound follows from the nonzero actual compact parameter without assigning its uncomputed full coordinates.',
          'Fourier idempotents descend integrally; trivial unordered-pair stabilizer gives induced projective homology. Nonzero values on every cusp make1-t invertible and kill the map to U_*.',
          'Exact inflation-restriction and finite peripheral restrictions realize the prescribed homology correction inside the existing source kernel.',
          'The Delta-invariant exterior block is regular over Q. Its full norm is injective and compactification has zero kernel there, so the actual D55 orientation identity forces its boundary class to vanish.',
          'The retained moving Delta part is removed by actual augmentation corrections; every source/fibre kernel and the366080-dimensional residual submodule remain explicit.'],
        'conclusion':'Frozen D59 claim proved for X/J; no conclusion for the remaining J boundary or the original full profinite realization.'}
(HERE/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
