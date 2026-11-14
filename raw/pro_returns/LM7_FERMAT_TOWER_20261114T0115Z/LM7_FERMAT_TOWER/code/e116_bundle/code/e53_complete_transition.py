#!/usr/bin/env python3
"""Exact first pure-53 norm/class lattice and all inverse coordinates.

This verifier uses the retained literal ideal/norm records and the separately
executed flag-1 class bound.  It never treats the timed-out flag-0 run as proof.
The cohomological equality of the norm image is proved in the accompanying
theorem; all coordinate maps used in that proof are checked here.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import json
import sympy as s

HERE=Path(__file__).resolve().parent
def records(name):
    return [json.loads(x) for x in (HERE/name).read_text().splitlines() if x.startswith('{')]
def vp(x,p=3):
    x=F(x);k=0
    while x.numerator%p==0:x/=p;k+=1
    while x.denominator%p==0:x*=p;k-=1
    return k
def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0]-a[1]*b[1])
def add(a,b):return (a[0]+b[0],a[1]+b[1])
def evaluate(c,a):
    return add(add((c[0],c[3]),mul((c[1],c[4]),a)),mul((c[2],c[5]),mul(a,a)))
def mpow(a,n):
    y=(1,0)
    while n:
        if n&1:y=mul(y,a)
        a=mul(a,a);n//=2
    return y

base=records('e_small_inert_units.out')
assert next(x for x in base if x.get('type')=='base_field' and x['ell']==53)['certification_returns']==[1,1]
bound=records('e53_pure9_class_upper.out')
bb=next(x for x in bound if x['type']=='certified_class_upper_bound')
assert bb['flag']==1 and bb['return']==1 and bb['presentation_cyclic']==[3,3]
norms=records('e53_pure9_norm_witness.out')
maps=records('e53_exact_maps.out')
assert maps[-1]=={'type':'completion','status':'PASS'}
pure_maps=next(x for x in maps if x['type']=='pure_divisor_maps')
quad_maps=next(x for x in maps if x['type']=='quadratic_divisor_maps_PARI_order')
quad_norms=next(x for x in maps if x['type']=='quadratic_prime_generator_norms')
els=[x for x in norms if x['type']=='actual_upper_S_unit_norm']
rec=next(x for x in norms if x['type']=='norm_lattice')
R=s.Matrix(rec['matrix']);L=s.Matrix(rec['left']);Q=s.Matrix(rec['right']);D=s.Matrix(rec['diagonal'])
assert L*R*Q==D and abs(int(L.det()))==abs(int(Q.det()))==1
P=s.Matrix.hstack(*[s.Matrix(x['S_valuations']) for x in els])
assert P[:,:4]==s.zeros(4,4)
P0=P[:,4:];assert abs(int(P0.det()))==9
Ndiv=s.Matrix([[1,1,0,0],[0,0,1,0],[0,0,0,1]])
assert Ndiv*P==R[1:,:]
assert s.Matrix(pure_maps['norm'])==Ndiv
assert Ndiv*s.Matrix(pure_maps['extension'])==3*s.eye(3)
assert s.Matrix(quad_maps['norm'])*s.Matrix(quad_maps['extension'])==2*s.eye(2)
assert quad_norms['coordinates_in_e_pA_pB_a']==[[0,0,0],[1,0,0],[0,1,1],[0,0,0]]
assert quad_norms['signs']==[1,1,1]
relation=s.Matrix([[1,1,0,0],[0,0,1,0]])
assert (relation*P).applyfunc(lambda a:int(a)%3)==s.zeros(2,8)
class_records=[x for x in norms if x['type']=='verified_class_coordinate_relation']
PC=s.Matrix.hstack(*[s.Matrix(x['coordinates']) for x in class_records])
change=s.Matrix([[0,2],[1,1]])
assert (PC-change*relation).applyfunc(lambda a:int(a)%3)==s.zeros(2,4)
change_inv=(pow(int(change.det()),-1,3)*change.adjugate()).applyfunc(lambda a:int(a)%3)
assert (change_inv*change).applyfunc(lambda a:int(a)%3)==s.eye(2)

# The actual three-prime labels are identified by the completions a=b*zeta^i.
cols=records('e53_prime_columns.out')
pc=[x for x in cols if x['type']=='prime_generator']
b=-1
for n in range(3,17):
    delta=((53-b**3)//3**n*pow(b*b,-1,3))%3
    b+=delta*3**(n-1)
    assert (b**3-53)%3**(n+1)==0
local_val=[]
for i in range(3):
    zz=mpow((0,1),i);a=(b*zz[0],b*zz[1]);row=[]
    for p in pc:
        x,y=evaluate([F(a) for a in p['coordinates']],a)
        row.append(vp(x*x-x*y+y*y))
    local_val.append(row)
assert sorted(local_val)==[[0,0,1],[0,1,0],[1,0,0]]
analytic_to_pari=[row.index(1)+1 for row in local_val]

# All elementary finite congruence, norm-image and affine fibre maps.
class_tests=[]
for v in product(range(3),repeat=4):
    w=list(relation*s.Matrix(v));w=[int(a)%3 for a in w]
    class_tests.append({'valuation':list(v),'class':w})
    assert (w==[0,0])==((v[0]+v[1])%3==0 and v[2]==0)
fibre_tests=[]
for n in product(range(-1,2),repeat=8):
    x=n[0]-n[4]-n[5]-n[6];y=n[4]+n[5];z=n[6];w=n[7]
    fibre=(n[1],n[2],n[3],n[5])
    back=(x+y+z,*fibre[:3],y-fibre[3],fibre[3],z,w)
    assert back==n
    assert list(R*s.Matrix(n))==[x,3*y,3*z,w]
    fibre_tests.append({'source':list(n),'target':[x,3*y,3*z,w],'fibre':list(fibre)})

sat=json.loads((HERE/'e53_unit_saturation.json').read_text());assert sat['status']=='PASS' and sat['determinant']%3
characters=json.loads((HERE/'e53_s_norm_explore.json').read_text())
assert characters['S_unit_cubic_character_matrix']==[[0]*7,[0,0,0,1,1,1,0],[0,0,0,2,2,2,0],[0]*7]
# c acts on the character vector by minus the interchange of wild1,wild2.
cchar=s.Matrix([[2,0,0,0],[0,0,2,0],[0,2,0,0],[0,0,0,2]])
im=s.Matrix([0,1,2,0]);assert (cchar*im-im).applyfunc(lambda a:int(a)%3)==s.zeros(4,1)

out={'statement':'E.116 first lower-53 transition','status':'PASS',
     'class_bound_flag':1,'class_bound_return':1,'full_flag0_timeout_not_used':True,
     'analytic_three_labels_to_PARI_one_based':analytic_to_pari,
     'actual_local_valuation_matrix':local_val,
     'pure_norm_matrix':rec['matrix'],'Smith_left':rec['left'],'Smith_right':rec['right'],
     'Smith_diagonal':rec['diagonal'],
     'upper_S_divisor_matrix':[[int(a) for a in row] for row in P.tolist()],
     'divisor_norm':[[int(a) for a in row] for row in Ndiv.tolist()],
     'divisor_extension':pure_maps['extension'],
     'quadratic_divisor_maps':quad_maps,
     'quadratic_generator_norm_coordinates':quad_norms['coordinates_in_e_pA_pB_a'],
     'pure_class_coordinate_map':[[int(a) for a in row] for row in relation.tolist()],
     'to_certified_presentation':[[int(a) for a in row] for row in change.tolist()],
     'from_certified_presentation':[[int(a) for a in row] for row in change_inv.tolist()],
     'pure_class_group':[3,3],'pure_S_class_group':[],
     'ordinary_unit_residue_matrix':sat['matrix'],'ordinary_unit_saturation_det':sat['determinant'],
     'norm_kernel_basis_source_columns':[[0,1,0,0,0,0,0,0],[0,0,1,0,0,0,0,0],
                                         [0,0,0,1,0,0,0,0],[0,0,0,0,-1,1,0,0]],
     'inverse_formula':'target(e^x*pA^(3y)*pB^(3z)*a^w), fibre(r2,r3,r4,r6) maps to exponents (x+y+z,r2,r3,r4,y-r6,r6,z,w)',
     'class_congruence_checks':len(class_tests),'full_norm_fibre_inverse_checks':len(fibre_tests),
     'complex_S_unit_norm_coordinates':'(v_Q0, v_Q1+v_Q2) modulo3',
     'complex_field_norm_coordinate':'v_Q0+v_Q1+v_Q2 modulo3',
     'actual_field_norm_but_not_Sunit_norm_witness':'generator(Q0)/generator(Q1)',
     'complex_ambiguous_S_class_group':[3],
     'complex_full_S_class_group':[3],
     'complex_full_S_class_sigma_action':1,
     'complex_full_S_class_c_action':-1,
     'complex_ambiguous_S_class_conjugation':-1,
     'natural_S_unit_norm_cokernel_conjugation':1,
     'scope':'The class/norm equalities use the exact Hilbert90 and C2 diagrams proved in the theorem; neither the unfinished default flag0 certification nor an uncomputed upper complex class group is substituted.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'e53_complete_transition.json').write_text(text);print(text,end='')
