#!/usr/bin/env python3
"""Derive the primary-component verifier with explicit Bezout eliminations."""
from pathlib import Path
import hashlib,json,py_compile
CODE=Path(__file__).resolve().parent
original=CODE/'pbc_verify_smallmod_trace.py';src=original.read_text()
def replace(old,new):
 global src
 assert src.count(old)==1,(old,src.count(old));src=src.replace(old,new)
replace('from pbc_source_coordinate_bounds import coordinate_bounds','from pbc_source_coordinate_bounds import coordinate_bounds,extended_gcd')
replace("ap.add_argument('--annihilator',type=Path)","ap.add_argument('--annihilator',type=Path,required=True)\nap.add_argument('--prime',type=int,choices=[2,3],required=True)")
replace("assert 1<M<2**64 and sys.byteorder=='little'\ncoordinates,bound_proofs=coordinate_bounds(raw)\ncoordinates=[M if d==N else d for d in coordinates]",
'''global_annihilator=M
M=1;remaining=global_annihilator
while remaining%args.prime==0:M*=args.prime;remaining//=args.prime
assert M>1 and global_annihilator%M==0
annihilator['global_homology_annihilator']=global_annihilator
annihilator['primary_modulus']=M;annihilator['prime']=args.prime
assert 1<M<2**64 and sys.byteorder=='little'
original_coordinates,bound_proofs=coordinate_bounds(raw)
coordinates=[math.gcd(d,M) for d in original_coordinates]''')
replace("elif row[2]=='extra':assert row[3][0]>=3,'Power-word correction forbidden'",
'''elif row[2]=='extra':
     idx=row[3][0];assert idx>=3,'Power-word correction forbidden'
     assert (idx<=args.s_count+2)==(args.prime==2),'Wrong-primary frame correction forbidden' ''')
replace(''' eliminations=[[i,total[i]//coordinates[i-1]] for i in sorted(used_bounds) if total[i]]
 proofs={i:bound_proofs[i] for i in sorted(used_bounds)};corrected=dict(total)
 for i,multiple in eliminations:
  correction=multiple*sum(r['coefficient']*r['value'] for r in proofs[i]['rows'])
  assert correction==total[i];corrected[i]-=correction''',
''' proofs={}
 for i in sorted(used_bounds):
  original=bound_proofs[i];d=original['bound'];g,a,b=extended_gcd(d,M)
  assert g==coordinates[i-1] and a*d+b*M==g
  proofs[i]=dict(original,reduced_bound=g,bezout_source_coefficient=a,bezout_modulus_coefficient=b)
 eliminations=[[i,(total[i]//coordinates[i-1])*proofs[i]['bezout_source_coefficient']] for i in sorted(used_bounds) if total[i]]
 corrected=dict(total)
 for i,multiple in eliminations:
  correction=multiple*sum(r['coefficient']*r['value'] for r in proofs[i]['rows'])
  assert (total[i]-correction)%M==0;corrected[i]-=correction''')
replace("returned=success[2];assert returned[:2]==[0,0]",
'''returned=success[2];assert returned[:2]==[0,0]
 assert all(v==0 for i,v in enumerate(returned,1) if i>=3 and ((i<=args.s_count+2)!=(args.prime==2)))''')
replace("'source_header':source,'modulus':M,'group_order':N,'annihilator_certificate':annihilator,",
"'source_header':source,'modulus':M,'group_order':N,'annihilator_certificate':annihilator,\n  'primary_component_only':True,'prime':args.prime,'global_homology_annihilator':global_annihilator,'other_primary_component_still_required':True,")
replace("'hopf_torsion_faithfulness_comparison':'notes/pbc_C31_small_annihilator.md' if annihilator else 'notes/pbc_C31_modular_gate.md',",
"'hopf_torsion_faithfulness_comparison':'notes/pbc_C31_primary_split_gate.md; no integral conclusion from one component',")
src='''# PRIMARY COMPONENT ONLY: this modulus does not kill the other torsion component.
# Every reduced coordinate bound uses an explicit original-row/constant-modulus
# Bezout identity. Both components and source-row replay remain mandatory.
'''+src
out=CODE/'pbc_verify_primary_trace.py';out.write_text(src);py_compile.compile(str(out),doraise=True)
adapter=(CODE/'pbc_replay_smallmod_source_rows.py').read_text()
old="assert expanded['modulus']==bound['bound']==math.prod(e*e for e in bound['factor_exponents'])"
new="""assert expanded['primary_component_only'] and expanded['prime'] in (2,3)
    assert expanded['global_homology_annihilator']==bound['bound']==math.prod(e*e for e in bound['factor_exponents'])
    component=1;remaining=bound['bound']
    while remaining%expanded['prime']==0:component*=expanded['prime'];remaining//=expanded['prime']
    assert expanded['modulus']==component"""
assert adapter.count(old)==1;adapter=adapter.replace(old,new)
adapter='# Only verifies ORIGINAL rows for one component; it does not establish integral vanishing.\n'+adapter
rp=CODE/'pbc_replay_primary_source_rows.py';rp.write_text(adapter);py_compile.compile(str(rp),doraise=True)
report={'base_verifier_sha256':hashlib.sha256(original.read_bytes()).hexdigest(),
 'primary_verifier_sha256':hashlib.sha256(out.read_bytes()).hexdigest(),
 'primary_source_replay_adapter_sha256':hashlib.sha256(rp.read_bytes()).hexdigest(),
 'coordinate_elimination':'For g=gcd(d,m), compute a*d+b*m=g and subtract (total/g)*a times the original d-row. The remaining integer coordinate is a multiple of m.',
 'scope':'Both independent primary certificates, the integer CRT combination, and every used original source-row replay remain mandatory. C31 OPEN.'}
(CODE/'pbc_primary_verifier_build.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps(report,indent=2))
