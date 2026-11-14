#!/usr/bin/env python3
"""All eight toric relative directions in the actual wild class-two relation."""
from pathlib import Path
from itertools import product
import importlib.util
import json
import numpy as np
import sympy as s
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
BASE=HERE.parents[1]/'LM7_FERMAT_TOWER/code'

def load(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m

def mat(x):return s.Matrix([[s.Rational(a)for a in row]for row in x])
def decode(x):return s.Matrix([[s.Rational(*a)for a in row]for row in x])
def encode(x):return [[str(a)for a in row]for row in x.tolist()]
def integral3(x):return all(int(s.Rational(a).q)%3 for a in x)
def modq(a,q):
    a=s.Rational(a);assert int(a.q)%3
    return int(a.p)*pow(int(a.q),-1,q)%q

P=load('e95_paths',HERE/'a_cusp_kummer_explore.py')
hall=load('e95_hall',BASE/'e_unramified_sections.py').Hall(2)
data=json.loads((BASE/'e_wild_layers.json').read_text())['layers']
relative=json.loads((BASE/'a_wild_kernel.json').read_text())['layers']['2']
first=json.loads((BASE/'a_abelian_kernel_obstruction.json').read_text())
smith=load('e95_smith',BASE/'e_cusp_local_smith.py')
horizontal=load('e95_horizontal',BASE/'a_horizontal_full.py')
T1,J1=P.T,P.J
T2,J2=(s.Matrix(data['2'][k])for k in ['input_tau','input_c'])
ids=[i for i,x in enumerate(hall.degree)if x==2];row={i:j for j,i in enumerate(ids)}

def bracket(a,b):
    out=s.zeros(45,1)
    for i in range(10):
        for j in range(10):
            if a[i] and b[j]:
                for k,n in hall.bracket(i,j).items():out[row[k]]+=a[i]*b[j]*n
    return out

B=[]
for d in range(8):
    e=s.eye(10)[:,d+2]
    B.append(s.Matrix.hstack(*[7*bracket(s.eye(10)[:,i],e)for i in range(10)]))
arc=np.load(BASE/'e_wild_layers_r2_transforms.npz')
left=s.Matrix(arc['left'].tolist())
vals=[x['valuation']for x in data['2']['elementary_operations']]
selected=[i for i,v in enumerate(vals)if v]
moduli=[3**vals[i]for i in selected]
assert moduli==[3]*11+[9]*4
G=(s.eye(10)-T1)*(s.eye(10)+J1)
gauge=first['first_degree_gauge_smith']
L1,Li1,R1,Ri1,D1=(mat(gauge[k])for k in ['left','left_inverse','right','right_inverse','diagonal_matrix'])
assert L1*G*R1==D1
assert L1*Li1==Li1*L1==R1*Ri1==Ri1*R1==s.eye(10)
representative=Li1[:,1:]
coef=[];constants=[];polynomials=[]
for d,label in enumerate(P.labels):
    raw=(left*B[d])[selected,:]
    assert all(modq(a,moduli[i])==0 for i in range(15)for a in (raw*G).row(i))
    cc=-raw*P.sympaths[label]
    coef.append(s.Matrix([[modq(a,moduli[i])for a in (raw*representative).row(i)]for i in range(15)]))
    constants.append(s.Matrix([modq(cc[i],moduli[i])for i in range(15)]))
    polynomials.append(s.Matrix.hstack(constants[-1],coef[-1]))
    # A canonical residue change by3 in each finite horizontal coordinate
    # is precisely an actual first-degree geometric gauge.
    assert all(modq(3*coef[-1][i,j],moduli[i])==0 for i in range(15)for j in range(3))

# Full actual relative relation inverse, retaining its integral domain.
target_left=decode(relative['split_inverse'])[relative['plus_rank']:,:]
DL=decode(relative['left_transform']);DR=decode(relative['domain_transform'])
DD=decode(relative['diagonal'])
relmat=(s.eye(45)-J2)*(T2-7*s.eye(45))
assert DL*target_left*relmat*DR==DD
inverse=-DR[:,:23]*s.diag(*[1/DD[i,i]for i in range(23)])*DL[:23,:]*target_left*(s.eye(45)-J2)
M0=s.eye(45)[:,1:]
assert relmat*inverse*M0==-(s.eye(45)-J2)*M0
assert all(integral3(9*inverse*B[d])for d in range(8))

def obstruction(U,A):
    v=s.zeros(45,1)
    for d,label in enumerate(P.labels):v+=A[d]*B[d]*(U-P.sympaths[label])
    assert v[0]==0
    return v

def residues(v):return tuple(modq((left*v)[i],3**vals[i])for i in selected)

# Literal coefficient-polynomial agreement on all eight directions and mixed
# actual normalized horizontal classes, including finite torsion carries.
polynomial_checks=0;particular_checks=0
for trial in range(729):
    p=s.Matrix([(trial*(i+3)+i*i)%(3 if i<3 else 27)for i in range(9)])
    U=representative*p
    A=s.Matrix([(trial*(i+7)+i*i)%9 for i in range(8)])
    v=obstruction(U,A)
    expected=tuple(sum(int(A[d])*(constants[d][i]+(coef[d]*p)[i])for d in range(8))%moduli[i]for i in range(15))
    assert residues(v)==expected
    polynomial_checks+=1
    sol=inverse*v
    assert integral3(sol)==(not any(expected))
    if integral3(sol):
        assert relmat*sol==-(s.eye(45)-J2)*v
        particular_checks+=1
    # Every relative vector in9W lifts, with its full actual correction.
    vv=obstruction(U,9*A)
    yy=inverse*vv
    assert integral3(yy) and relmat*yy==-(s.eye(45)-J2)*vv
    particular_checks+=1

# The table itself supplies the actual cusp origins and their multiples.
cusp_checks=0
for d,label in enumerate(P.labels):
    for n in [-9,-3,-1,0,1,2,3,9,27]:
        A=s.zeros(8,1);A[d]=n
        assert obstruction(P.sympaths[label],A)==s.zeros(45,1)
        cusp_checks+=1

# Exact fixed-relative solution sets, computed as an affine integral
# congruence lattice, including infeasible relative inputs.
fixed_relative=[]
relative_samples=[]
for i in range(8):
    aa=s.zeros(8,1);aa[i]=1;relative_samples.append(aa)
for i in range(8):
    for j in range(i+1,8):
        aa=s.zeros(8,1);aa[i]=aa[j]=1;relative_samples.append(aa)
for trial in range(12):
    relative_samples.append(s.Matrix([(trial*(j+3)+j*j)%9 for j in range(8)]))
for aa in relative_samples:
    FA=sum((aa[d]*(left*B[d])[selected,:]for d in range(8)),s.zeros(15,10))
    const=sum((aa[d]*(-((left*B[d])[selected,:])*P.sympaths[P.labels[d]])for d in range(8)),s.zeros(15,1))
    block=FA.row_join(s.diag(*moduli))
    ss=smith.local_smith(block.tolist())
    SL,SR,SD=(mat(ss[k])for k in ['left','right','diagonal_matrix'])
    assert SL*block*SR==SD
    rhs=SL*(-const)
    yes=all(integral3(s.Matrix([rhs[i]/SD[i,i]]))for i in range(15))
    record={'relative':[int(x)for x in aa],'nonempty':yes,'smith_values':ss['valuations']}
    if yes:
        sol=SR[:,:15]*s.diag(*[1/SD[i,i]for i in range(15)])*rhs
        assert integral3(sol) and block*sol==-const
        uu=sol[:10,:];vv=obstruction(uu,aa);yy=inverse*vv
        assert not any(residues(vv)) and integral3(yy)
        assert relmat*yy==-(s.eye(45)-J2)*vv
        record['horizontal']=[str(x)for x in uu]
        record['central_correction']=[str(x)for x in yy]
        particular_checks+=1
    fixed_relative.append(record)

# Largest integral relative lattice on which EVERY horizontal input lifts.
universal=s.eye(8)
for i,modulus in enumerate(moduli):
    for j in range(10):
        rr=s.Matrix([[int(polynomials[d][i,j])for d in range(8)]])
        universal=hermite_normal_form(universal*horizontal.row_kernel(rr*universal,modulus))
us=smith.local_smith(universal.tolist())
assert integral3(universal.inv()*9*s.eye(8))
for i,modulus in enumerate(moduli):
    for j in range(10):
        rr=s.Matrix([[int(polynomials[d][i,j])for d in range(8)]])
        assert all(modq(x,modulus)==0 for x in rr*universal)

print('PASS full15-coordinate polynomial and all first-degree gauge/carry maps')
print('PASS',polynomial_checks,'complete mixed-input polynomial comparisons')
print('PASS',particular_checks,'actual integral corrections including the entire9W locus')
print('PASS',cusp_checks,'literal cusp origins and all eight exact directions')
print('PASS',len(fixed_relative),'complete fixed-relative affine systems; nonempty',sum(x['nonempty']for x in fixed_relative))
print('PASS maximal all-horizontal relative lattice; Smith valuations',us['valuations'])
print('constant_matrix=',s.Matrix.hstack(*constants).tolist())
print('ALL PASS')
result={'status':'PASS','coefficient_moduli':moduli,
        'horizontal_representative':encode(representative),
        'horizontal_coordinate_types':['C3']*3+['Z3']*6,
        'constant_matrix':s.Matrix.hstack(*constants).tolist(),
        'polynomial_blocks':{label:encode(polynomials[d])for d,label in enumerate(P.labels)},
        'universal_particular_correction':encode(inverse),
        'relation_matrix':encode(relmat),
        'all_relative_multiples_of9_lift':True,
        'mixed_polynomial_checks':polynomial_checks,'integral_particular_checks':particular_checks,
        'literal_cusp_origin_checks':cusp_checks,
        'fixed_relative_cases':fixed_relative,
        'universal_all_horizontal_lattice':encode(universal),
        'universal_all_horizontal_smith':us}
HERE.joinpath('a_toric_wild_explore.json').write_text(json.dumps(result,indent=2,default=int)+'\n')
