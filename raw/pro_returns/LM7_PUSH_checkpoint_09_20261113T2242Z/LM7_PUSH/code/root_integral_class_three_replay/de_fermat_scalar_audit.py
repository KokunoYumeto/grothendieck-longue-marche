#!/usr/bin/env python3
"""Independent exact class-two audit of the integral source scalar row.

This recomputes literal word coefficients by integer Heisenberg group
multiplication and checks the filtered affine solutions against every
previously computed group-pentagon tensor coefficient.
"""
from pathlib import Path
import json
import numpy as np

here=Path(__file__).resolve().parent
def mul(x,y):
    a,b,c=x;A,B,C=y
    return a+A,b+B,c+C-b*A
def inv(x):
    a,b,c=x;return -a,-b,-c-a*b
def power(x,n):
    a,b,c=x;return n*a,n*b,n*c-a*b*n*(n-1)//2
def comm(x,y):return mul(mul(mul(x,y),inv(x)),inv(y))
def coeff(word):
    images={1:(1,0,0),-1:(-1,0,0),2:(0,1,0),-2:(0,-1,0)}
    out=(0,0,0)
    for a in word:out=mul(out,images[a])
    assert out[:2]==(0,0)
    return out[2]
x=(1,0,0);y=(0,1,0);z=inv(mul(x,y))
assert comm(x,y)==comm(z,x)==comm(y,z)==(0,0,1)
for m in range(-12,13):
    for f2 in range(-12,13):
        out=(0,0,0)
        for element in (power(comm(x,y),f2),power(x,m),
                        power(comm(z,x),f2),power(z,m),
                        power(comm(y,z),f2),power(y,m)):
            out=mul(out,element)
        assert out==(0,0,3*f2-m*(m+1)//2)

source=json.loads(here.joinpath('a_ihara_pentagon_inputs.json').read_text())
filtered=json.loads(here.joinpath('a_ihara_pentagon_scalar.json').read_text())
certificate=np.load(here/'de_fermat_pentagon_arithmetic_fast_certificate.npz')
values=np.array([coeff(r['literal_word']) for r in source['candidate_records']],dtype=np.int64)
kernel=np.array([coeff(w) for w in filtered['true_kernel_literal_words']],dtype=np.int64)
assert kernel.tolist()==[3,0,0,0,0]
coords=certificate['candidate_coordinates'];D=certificate['direction_residuals'];base=certificate['base_residual']
rows=[]
for branch in filtered['branch_results']:
    ids=branch['input_record_indices'];v0=int(values[ids[0]])
    differences=np.r_[values[ids[1:]]-v0,kernel]
    assert not np.any(differences%3)
    row=differences//3%3;rhs=(2-v0)//3%3
    assert row.tolist()==branch['source_f2_divided_row']
    assert rhs==branch['source_f2_divided_rhs']
    particular=np.array(branch['particular_parameters'],dtype=np.int64)
    homogeneous=np.array(branch['homogeneous_parameters'],dtype=np.int64)
    assert (v0+differences@particular)%9==2
    assert not np.any(differences@homogeneous%9)
    L=np.zeros((11,len(particular)),dtype=np.int64)
    L[:6,:len(ids)-1]=(coords[:,ids[1:]]-coords[:,ids[0],None])%3
    L[6:,len(ids)-1:]=np.eye(5,dtype=np.int64)
    b=(base+D[:,:6]@coords[:,ids[0]])%3
    assert not np.any((b+D@L@particular)%3)
    assert not np.any(D@L@homogeneous%3)
    result={'branch':branch['branch'],'literal_base_f2_mod9':v0%9,
            'source_scalar_target_mod9':2,
            'all_29520_pentagon_coefficients_still_zero':True,
            'homogeneous_scalar_and_pentagon_equations_verified':True,
            'homogeneous_parameter_dimension':homogeneous.shape[1]}
    rows.append(result);print(json.dumps(result))
out={'integer_Heisenberg_hexagon_central_coordinate':'3*f2-m*(m+1)/2',
     'source_coefficient_at_chi7':2,
     'five_true_kernel_coefficients':kernel.tolist(),
     'branch_results':rows,
     'scope':'Independent exact coefficient and saved full group-pentagon solution-space audit. The scalar uses the integral torsion-free Z3 identity before reduction modulo9.'}
here.joinpath('de_fermat_scalar_audit.json').write_text(json.dumps(out,indent=2)+'\n')
print('PASS: integral source scalar and all saved full pentagon coefficients agree.')
