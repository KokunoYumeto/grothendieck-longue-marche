#!/usr/bin/env python3
"""Independent exact decoding of the amended ambient E119 matrix exports."""
from pathlib import Path
import hashlib, json
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
OLD=ROOT/'audit/pre_rational_export/full_tree'
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
new=json.loads((ROOT/'code/e_lower_fiftythree.json').read_text())
old=json.loads((OLD/'code/e_lower_fiftythree.json').read_text())
cases=[]
for key, stem, typ in [
    ('B2_genus','e53_genus_transition','next_genus_presentation'),
    ('L2_genus','e53_positional_genus_transition','positional_genus_transition')]:
    records=[json.loads(x) for x in (ROOT/'code'/f'{stem}.out').read_text().splitlines()
             if x.startswith('{')]
    r=next(x for x in records if x['type']==typ)
    K=S.Matrix(r['kernel_lattice'])
    U=S.Matrix(r['kernel_smith_left'])
    D=S.Matrix(r['kernel_smith_diagonal'])
    F=U*K.inv()
    decoded=S.Matrix([[S.Rational(x) for x in row] for row in new[key]['forward']])
    inverse=S.Matrix(new[key]['inverse'])
    assert decoded==F and inverse==K*U.inv()
    assert decoded*inverse==inverse*decoded==S.eye(F.rows)
    assert all(S.denom(x)==1 for x in F*K)
    fractional=[]
    for i in range(F.rows):
        for j in range(F.cols):
            if S.denom(F[i,j])!=1:
                assert D[i,i]==1
                fractional.append({'row':i,'column':j,'exact':str(F[i,j]),
                                   'Smith_modulus':1,
                                   'old_integer':old[key]['forward'][i][j]})
            else:
                assert int(F[i,j])==old[key]['forward'][i][j]
        if D[i,i]!=1:
            assert list(F.row(i))==old[key]['forward'][i]
    assert len(fractional)==(8 if key=='B2_genus' else 4)
    old[key]['forward']=new[key]['forward']
    cases.append({'key':key,'fractional_entries':fractional,
                  'full_ambient_compositions':'identity',
                  'restriction_to_kernel_lattice':'integral',
                  'nontrivial_Smith_coordinate_rows_unchanged':True})
assert old==new
oldman=json.loads((OLD/'ledger/e_lower_fiftythree_manifest.json').read_text())
changed=[rel for rel,v in oldman['files'].items() if sha(ROOT/rel)!=v['sha256']]
assert not any(x.endswith(('.gp','.bin')) for x in changed)
assert not any(x.endswith('.out') and not x.startswith('code/e_lower_fiftythree')
               for x in changed)
proof=ROOT/'sections/E_lower_fiftythree.tex'
assert sha(proof)==sha(OLD/'sections/E_lower_fiftythree.tex')
result={'statement':'E.119','status':'PASS',
        'scope':'New exact Python-only decoding; unchanged GP records, no GP execution.',
        'cases':cases,'all_other_JSON_fields_identical':True,
        'changed_preexisting_manifested_paths':changed,
        'unchanged_proof_sha256':sha(proof),
        'main_sha256':sha(ROOT/'code/e_lower_fiftythree.py'),
        'JSON_sha256':sha(ROOT/'code/e_lower_fiftythree.json'),
        'encoder_format':'Every ambient forward entry is a canonical exact rational string; integer and rational decoders compare exactly.'}
text=json.dumps(result,indent=2)+'\n'
(ROOT/'ledger/e_lower_fiftythree_export_verification.json').write_text(text)
print(text,end='')
