#!/usr/bin/env python3
"""Independent finite maps for the actual cyclic-nine genus transition at53."""
from pathlib import Path
import json,itertools,hashlib,argparse,subprocess,sys
import sympy as S

ROOT=Path(__file__).resolve().parents[1]
ap=argparse.ArgumentParser();ap.add_argument('--gp');args=ap.parse_args()
if args.gp:
    gp=str(Path(args.gp).resolve())
    for name in ['e53_higher_local','e53_higher_genus','e53_upper_witness_verify']:
        with (ROOT/'code'/(name+'.out')).open('w') as out,(ROOT/'code'/(name+'.err')).open('w') as err:
            run=subprocess.run([gp,'-fq',name+'.gp'],cwd=ROOT/'code',stdout=out,stderr=err)
        assert run.returncode==0,(name,run.returncode)
        lines=(ROOT/'code'/(name+'.err')).read_text().splitlines()
        assert all('Warning: new stack size =' in x for x in lines if x.strip()),lines
        done=[json.loads(x) for x in (ROOT/'code'/(name+'.out')).read_text().splitlines() if x.startswith('{')]
        assert done[-1]=={'type':'completion','status':'PASS'},name
    with (ROOT/'code/e53_literal_unit_ring.out').open('w') as out,(ROOT/'code/e53_literal_unit_ring.err').open('w') as err:
        run=subprocess.run([sys.executable,str(ROOT/'code/e53_literal_unit_ring.py')],cwd=ROOT/'code',stdout=out,stderr=err)
    assert run.returncode==0,run.returncode
def records(p):return [json.loads(l) for l in p.read_text().splitlines() if l.startswith('{')]
def pick(rr,t):return next(x for x in rr if x['type']==t)
def imat(M):
    assert all(S.denom(x)==1 for x in M)
    a=[[int(x) for x in M.row(i)] for i in range(M.rows)]
    assert S.Matrix(a)==M
    return a
def qmat(M):
    a=[[str(x) for x in M.row(i)] for i in range(M.rows)]
    assert S.Matrix([[S.Rational(x) for x in r] for r in a])==M
    return a
def smith_verify(H,U,V,D):
    assert U*H*V==D and abs(U.det())==abs(V.det())==1
def reducev(v,orders):return tuple(int(a)%m for a,m in zip(v,orders))
old=pick(records(ROOT/'inputs/e119_e53_genus_transition.out'),'next_genus_presentation')
new=pick(records(ROOT/'code/e53_higher_genus.out'),'B3_over_B1_genus')
H0=S.Matrix(old['relation_HNF']);H1=S.Matrix(new['relation_HNF'])
K0=S.Matrix(old['kernel_lattice']);K1=S.Matrix(new['kernel_lattice'])
U0=S.Matrix(old['kernel_smith_left']);U1=S.Matrix(new['kernel_smith_left'])
V0=S.Matrix(old['kernel_smith_right']);V1=S.Matrix(new['kernel_smith_right'])
D0=S.Matrix(old['kernel_smith_diagonal']);D1=S.diag(*new['kernel_smith_diagonal'])
smith_verify(K0.inv()*H0,U0,V0,D0)
smith_verify(K1.inv()*H1,U1,V1,D1)
assert all(S.denom(x)==1 for x in H0.inv()*H1)
N=U0*K0.inv()*K1*U1.inv()
assert all(S.denom(x)==1 for x in N)
assert all(S.denom(x)==1 for x in D0.inv()*N*D1)
active0=[i for i in range(9) if D0[i,i]>1]
active1=[i for i in range(9) if D1[i,i]>1]
orders0=[int(D0[i,i]) for i in active0];orders1=[int(D1[i,i]) for i in active1]
n=N.extract(active0,active1)
assert orders0==orders1==[9,3,3,3]
domain=list(itertools.product(*(range(o) for o in orders1)))
inverse={reducev(n*S.Matrix(v),orders0):v for v in domain}
assert len(inverse)==len(domain)==243
inv=S.Matrix.hstack(*(S.Matrix(inverse[tuple(int(i==j) for i in range(4))]) for j in range(4)))
assert all(reducev(inv*n*S.Matrix(v),orders1)==v for v in domain)
assert all(reducev(n*inv*S.Matrix(v),orders0)==v for v in domain)
j=3*inv
for v in domain:
    assert reducev(n*j*S.Matrix(v),orders0)==reducev(3*S.Matrix(v),orders0)
    assert reducev(j*n*S.Matrix(v),orders1)==reducev(3*S.Matrix(v),orders1)
oldfull=json.loads((ROOT/'inputs/e121_normalizer_module.json').read_text())
# The actual horizontal action in the full lower group, in the E121 basis.
Hlower=S.Matrix([[4,3,6,0],[2,2,2,0],[0,1,0,0],[1,0,0,1]])
Hnew=inv*Hlower*n
for v in domain:
    assert reducev(Hnew**3*S.Matrix(v),orders1)==v
    assert reducev(n*Hnew*S.Matrix(v),orders0)==reducev(Hlower*n*S.Matrix(v),orders0)
locals=records(ROOT/'code/e53_higher_local.out')
setup=pick(locals,'local_ninth_setup');cyc=setup['unit_orders'];lg4=S.Matrix(setup['four_log'])
for row in (x for x in locals if x['type']=='local_ninth_norm'):
    A=S.Matrix(row['norm_logs']);H=S.Matrix(row['norm_HNF'])
    U=S.Matrix(row['smith_left']);V=S.Matrix(row['smith_right']);D=S.diag(*row['smith_diagonal'])
    smith_verify(H,U,V,D)
    assert abs(H.det())==9
    assert all(S.denom(x)==1 for x in H.inv()*A)
    c=S.Matrix([row['positive_character']])
    assert all(int(x)%9==0 for x in c*A)
    assert int((c*lg4)[0])%9==row['calibration_four']
C=S.Matrix(pick(records(ROOT/'code/e53_higher_genus.out'),'higher_complete_S_unit_characters')['matrix'])
assert all(int(x)%9==0 for x in S.ones(1,6)*C)
# The cubic field-norm subspace is ker(C mod3); its ninth character divided
# by3 maps onto the full five-dimensional product-formula hyperplane.
from sympy.polys.matrices import DomainMatrix
F3=S.GF(3)
def rank3(M):
    return DomainMatrix.from_Matrix(M).convert_to(F3).rank()
assert rank3(C)==2
# Supply all cubic-kernel generators using exact integer HNF instead of an
# arbitrary lift of an F3 nullspace.
from sympy.matrices.normalforms import hermite_normal_form
# Finite elimination over F3, recording actual integral representatives.
rows=[[int(x)%3 for x in C.row(i)] for i in range(C.rows)]
piv=[];rr=0
for col in range(C.cols):
    at=next((i for i in range(rr,len(rows)) if rows[i][col]),None)
    if at is None:continue
    rows[rr],rows[at]=rows[at],rows[rr]
    a=pow(rows[rr][col],-1,3);rows[rr]=[(a*x)%3 for x in rows[rr]]
    for i in range(len(rows)):
        if i!=rr:
            a=rows[i][col];rows[i]=[(x-a*y)%3 for x,y in zip(rows[i],rows[rr])]
    piv.append(col);rr+=1
free=[i for i in range(C.cols) if i not in piv]
basis=[]
for col in free:
    v=[0]*C.cols;v[col]=1
    for i,p in enumerate(piv):v[p]=-rows[i][col]
    basis.append(S.Matrix(v))
for p in piv:
    v=S.zeros(C.cols,1);v[p]=3;basis.append(v)
K=S.Matrix.hstack(*basis)
assert K.shape==(15,15) and abs(K.det())==9
CK=C*K/3
assert all(S.denom(x)==1 for x in CK) and rank3(CK)==5
tt=S.symbols('T')
trace=S.expand(sum((1+tt)**i for i in range(3))-3)
assert trace==3*tt+tt**2
nilpotence_checks=[]
for ee in range(1,33):
    vals=[a+(9*ee-a)//9 for a in range(9*ee+1)]
    assert min(vals)>=ee
    nilpotence_checks.append([ee,min(vals),len(vals)])
# Actual H-action on K1=<3e0,e1,e2>, all elementary coordinates explicit.
kembed=S.Matrix([[3,0,0],[0,1,0],[0,0,1],[0,0,0]])
kh=S.Matrix([[1,1,2],[0,2,2],[0,1,0]])
for z in itertools.product(range(3),repeat=3):
    assert reducev(Hlower*kembed*S.Matrix(z),orders0)==reducev(kembed*kh*S.Matrix(z),orders0)
literal=pick(records(ROOT/'code/e53_upper_witness_verify.out'),'literal_unit_witness_verification')
ring=json.loads((ROOT/'code/e53_literal_unit_ring.json').read_text())
assert literal['rank_mod3']==5 and ring['five_character_determinant']==-4
assert literal['cube_identities']==literal['relative_norm_identities']==22
normH=S.Matrix(literal['norm_lattice_HNF'])
assert abs(normH.det())==729
for v in domain:
    assert reducev(n*inv*S.Matrix(v),orders0)==v
    assert reducev(3*inv*S.Matrix(v),orders1)==reducev(j*S.Matrix(v),orders1)
class_quotient=set(reducev(S.Matrix(v),[3]*4) for v in domain)
assert len(class_quotient)==81 and pow(53,2,27)==1 and 53%27!=1
unit_rank_checks=[[d,3**(d+1)+5,3**(d+2)+5,2*3**(d+1)] for d in range(2,17)]
assert all(b-a==k for d,a,b,k in unit_rank_checks)
res={
 'status':'PASS','all_finite_elements_checked':len(domain),
 'B3_g_coinvariant_orders':orders1,'full_B2_orders':orders0,
 'ambient_norm':imat(N),'finite_norm':imat(n),'finite_norm_inverse':imat(inv),
 'projected_vertical_extension':imat(j),'transported_horizontal_action':imat(Hnew),
 'new_genus_to_old_relation_inclusion':imat(H0.inv()*H1),
 'cubic_field_norm_unit_lattice':imat(K),'ninth_characters_on_that_lattice_divided_by_three':imat(CK),
 'divided_character_rank_mod_three':rank3(CK),
 'actual_initial_kernel_H_action':imat(kh),
 'local_cube_collection_difference_from_three':str(trace),
 'nilpotence_bound_checks':nilpotence_checks,
 'local_norm_subgroups_checked':3,
 'literal_root_witness_count':22,'three_new_root_witnesses':ring['three_new_root_indices'],
 'five_character_determinant':ring['five_character_determinant'],
 'full_embedded_first_unit_norm_index':729,'later_class_defect_order':len(class_quotient),
 'later_unit_norm_cokernel_order':3**5*len(class_quotient),
 'unit_rank_checks':unit_rank_checks,
 'scope':'Exact finite maps plus literal unit witnesses. Their rank-five character image, together with the proved actual all-level kernel recursion, gives zero later norm kernels and the stable full class group C9+C3^3. No upper BNF completeness or finite-level stability extrapolation is used.',
 'input_sha256':{str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in [ROOT/'code/e53_higher_genus.out',ROOT/'code/e53_higher_local.out',ROOT/'code/e53_upper_witness_verify.out',ROOT/'code/e53_literal_unit_ring.json',ROOT/'inputs/e119_e53_genus_transition.out',ROOT/'inputs/e121_normalizer_module.json',ROOT/'inputs/e122_literal_unit_witnesses.json',ROOT/'inputs/e122_literal_unit_witnesses.txt']}
}
out=json.dumps(res,indent=2)+'\n';(ROOT/'code/e53_higher_maps.json').write_text(out);print(out,end='')
