#!/usr/bin/env python3
"""Exhaustive exact comparison of the two finite eighteen-parameter loci."""
from pathlib import Path
import json,time
OUT=Path(__file__).resolve().parent;started=time.time()
data=json.loads((OUT/'d_cm_reduced_invariant_equations.json').read_text())
N=18
ol=data['reduced_linear_obstruction_coefficients'];oq=data['reduced_quadratic_obstruction_coefficients']
pl=[int(x,16) for x in data['pairing_linear_coefficients']]
pq=[[int(x,16) for x in row] for row in data['pairing_quadratic_coefficients']]
def solver(cols):
    basis={}
    for j,col in enumerate(cols):
        v=col;w=1<<j
        while v:
            p=v.bit_length()-1
            if p not in basis:basis[p]=(v,w);break
            a,b=basis[p];v^=a;w^=b
    def solve(v):
        w=0
        for p in sorted(basis,reverse=True):
            if v>>p&1:a,b=basis[p];v^=a;w^=b
        assert not v
        return w
    return solve,len(basis)
allp=pl+[pq[i][j] for i in range(N) for j in range(i+1,N)]
pbasis=[]
for c in allp:
    _,nr=solver(pbasis+[c])
    if nr>len(pbasis):pbasis.append(c)
psolve,prank=solver(pbasis);assert prank==9
pl=[psolve(c) for c in pl]
pq=[[psolve(c) for c in row] for row in pq]
values_o=[0]*(1<<N);values_p=[0]*(1<<N)
for mask in range(1,1<<N):
    bit=mask&-mask;i=bit.bit_length()-1;rest=mask^bit
    a=values_o[rest]^ol[i];b=values_p[rest]^pl[i]
    v=rest
    while v:
        bb=v&-v;j=bb.bit_length()-1
        a^=oq[min(i,j)][max(i,j)];b^=pq[min(i,j)][max(i,j)];v^=bb
    values_o[mask]=a;values_p[mask]=b
O=[m for m in range(1<<N) if values_o[m]==0]
P=[m for m in range(1<<N) if values_p[m]==0]
assert O==[int(x,16) for x in data['exact_homology_solution_parameters']]
missing=sorted(set(P)-set(O));unexpected=sorted(set(O)-set(P));assert not unexpected
summary={'scope':'Separate marked order1080 finite model.',
 'parameter_dimension':N,'total_parameters_tested':1<<N,
 'full_class2_homology_locus_count':len(O),
 'intersection_pairing_locus_count':len(P),
 'pairing_preserving_parameters_without_same_action_class2_lift':len(missing),
 'same_zero_locus':not missing,
 'first_pairing_preserving_missing_parameter':hex(missing[0]) if missing else None,
 'first_missing_invariant_obstruction':values_o[missing[0]] if missing else None,
 'elapsed_seconds':round(time.time()-started,3)}
cert={'summary':summary,'pairing_coordinate_basis':[hex(x) for x in pbasis],
 'pairing_linear_coordinates':pl,'pairing_quadratic_coordinates':pq,
 'all_pairing_locus_parameters':[hex(x) for x in P],
 'all_pairing_preserving_missing_parameters':[hex(x) for x in missing]}
(OUT/'d_cm_invariant_zero_loci.json').write_text(json.dumps(cert,indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
