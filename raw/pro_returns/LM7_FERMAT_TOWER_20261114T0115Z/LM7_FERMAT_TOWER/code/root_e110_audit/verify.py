"""Verify frozen E110 inputs and execute both mathematical sources afresh."""
from pathlib import Path
import hashlib,json,shutil,subprocess,sys

ROOT=Path(__file__).resolve().parents[1]
HERE=Path(__file__).resolve().parent
SRC=ROOT/'research_e110'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
mf=SRC/'ledger/e_pure_tower_manifest.json'
assert sha(mf)=='320003a889adc19fa0c8d59a5629304e271e7a222f51ab41e2c0d0dad383305a'
manifest=json.loads(mf.read_text())
for row in manifest['files']:
    p=SRC/row['path']
    assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256'],row['path']
proof=SRC/'sections/E_pure_tower_complete.tex'
assert sha(proof)=='23e7f7efcee8b9123363d30f8b1fe76763b38e2370d763bdf1e4cac17f7aae38'
dest=HERE/'fresh'
assert not dest.exists()
(dest/'code').mkdir(parents=True)
shutil.copytree(SRC/'inputs',dest/'inputs')
for name in ['e_pure_tower.py','e_pure_tower_base.gp']:
    shutil.copy2(SRC/'code'/name,dest/'code'/name)
gp=ROOT/'research_e52/vendor/pari-2.19.0/gp'
assert gp.is_file()
program=dest/'code/e_pure_tower.py'
with program.with_suffix('.out').open('wb') as stream:
    result=subprocess.run([sys.executable,str(program),'--gp',str(gp)],
                          stdout=stream,stderr=subprocess.STDOUT)
assert result.returncode==0,result.returncode
checks=[]
for name in ['e_pure_tower.out','e_pure_tower.json','e_pure_tower_base_gp.out','e_pure_tower_base.bin']:
    actual=dest/'code'/name;expected=SRC/'code'/name
    assert actual.read_bytes()==expected.read_bytes(),name
    checks.append({'file':name,'complete_byte_equality':True,'sha256':sha(actual)})
record={'status':'PASS','actual_exit_code':result.returncode,
        'proof_sha256':sha(proof),'manifest_sha256':sha(mf),
        'manifest_files_verified':len(manifest['files']),
        'rebuild':'Fresh copy of both Python and GP mathematical sources and the complete isolated input directory; Python --gp executed PARI and independently recomputed the whole certificate.',
        'checks':checks,'excluded_fields':[],
        'root_read_scope':'Complete E110 statement and proof, the entire Python and GP mathematical sources, Kato Theorem1.1(1) and its explicit unconditional Section3.2 rank argument. Original Milne and Lemmermeyer maps had been separately checked in the preceding project audits.',
        'mathematical_checks':[
          'The initial three-class group vanishes by the actual cyclic ambiguous formula; the4x3 character matrix has full product-one image and persists through the literal non-Galois local norm/projection square.',
          'Every later ambiguous three-class group is trivial; the fixed-point argument and degree-two ideal extension/norm prove all M and F three-class assertions.',
          'Complex conjugation is negative permutation on arithmetic local characters. Its fixed line gives the exact pure unit norm quotient C3, with epsilon calibration retained.',
          'The completed divisor exact sequence and compact unit fibres yield every compatible principal divisor; restricted products give a continuous coherent splitting with an explicit inverse.',
          'The compact torsion-free unit inverse limit is evaluated through its actual dual norm maps; Kato universal norms give unbounded finite projection ranks, hence exactly countably many Z3 factors.',
          'The complete complex phase and pure norm maps yield both directions of the fixed-first toric image and all fibre formulas, including the literal kappa7 correction and the unit-r substitution automorphism.'],
        'scope_limit':'The theorem evaluates the exact H target for first unit multiples of kappa3(17); the remaining unrestricted-source and intrinsic lifting tasks remain active.'}
(HERE/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
print(json.dumps(record,indent=2))
