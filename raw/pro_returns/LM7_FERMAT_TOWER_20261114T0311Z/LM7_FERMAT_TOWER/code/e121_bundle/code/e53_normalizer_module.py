#!/usr/bin/env python3
"""Exact positional-53 normalizer, genus, norm and extension comparisons.

The optional five-stage GP replay starts from the immutable, previously
certified E119 data objects; it performs no BNF class/unit reconstruction.
"""
from pathlib import Path
from itertools import product
from collections import Counter
import argparse, hashlib, json, shutil, subprocess, tempfile
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form, smith_normal_form

HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
INPUTS=ROOT/'inputs'
NAMES=['e53_order_nine_genus','e53_normalizer_actions',
       'e53_horizontal_upper_norm','e53_horizontal_upper_extension',
       'e53_cyclic_nine_comparison']
arg=argparse.ArgumentParser()
arg.add_argument('--gp')
args=arg.parse_args()
sha=lambda p:hashlib.sha256(p.read_bytes()).hexdigest()
inp=json.loads((INPUTS/'manifest.json').read_text())
for item in inp['files']:
    assert sha(ROOT/item['path'])==item['sha256'],item['path']

def records(path):
    lines=path.read_text().splitlines()
    errors=[s for s in lines if '***' in s and not (
        s.strip().startswith('***   Warning: new stack size = ') or
        s.strip().startswith('***   Warning: new maximum stack size = '))]
    assert not errors,(str(path),errors)
    rr=[json.loads(s) for s in lines if s.startswith('{')]
    assert rr and rr[-1].get('status')=='PASS'
    return rr

if args.gp:
    gp=str(Path(args.gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e53_normalizer_') as td:
        td=Path(td)
        work=td/'code'
        work.mkdir()
        shutil.copytree(INPUTS,td/'inputs')
        for name in NAMES:
            shutil.copy2(HERE/f'{name}.gp',work/f'{name}.gp')
        for name in NAMES:
            run=subprocess.run([gp,'-q','-f',name+'.gp'],cwd=work,
                               stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (HERE/f'{name}.out').write_bytes(run.stdout)
            assert run.returncode==0,(name,run.returncode)
            records(HERE/f'{name}.out')
        for p in work.glob('*.bin'):
            shutil.copy2(p,HERE/p.name)

data={n:records(HERE/f'{n}.out') for n in NAMES}
def row(n,t):
    vv=[r for r in data[n] if r['type']==t]
    assert len(vv)==1,(n,t)
    return vv[0]
def mat(x):return S.Matrix(x)
def integral(m):return all(S.denom(x)==1 for x in m)
def ints(m):
    assert integral(m)
    out=[[int(x) for x in m.row(i)] for i in range(m.rows)]
    assert mat(out)==m
    return out
def rats(m):
    out=[[str(S.Rational(x)) for x in m.row(i)] for i in range(m.rows)]
    assert mat([[S.Rational(x) for x in r] for r in out])==m
    return out
def imod(m,q):
    assert integral(m)
    return m.applyfunc(lambda x:int(x)%q)
def reduced(m,mods):
    assert integral(m)
    return S.Matrix(len(mods),m.cols,lambda i,j:int(m[i,j])%mods[i])
def apply(m,z,mods):
    v=m*S.Matrix(z)
    assert integral(v)
    return tuple(int(v[i])%mods[i] for i in range(len(mods)))
def all_group(mods):return list(product(*(range(q) for q in mods)))
def snf(H):
    D=smith_normal_form(H,domain=S.ZZ)
    return sorted((abs(int(D[i,i])) for i in range(min(D.shape))
                   if abs(D[i,i])!=1),reverse=True)
def assert_same(m,mods):
    assert integral(S.diag(*mods).inv()*m)

base_records=records(INPUTS/'e119_e53_genus_transition.out')
br=next(r for r in base_records if r['type']=='next_genus_presentation')
lr=next(r for r in records(INPUTS/'e119_e53_positional_genus_transition.out')
        if r['type']=='positional_genus_transition')
HB,KB,UB,DB=[mat(br[k]) for k in ['relation_HNF','kernel_lattice',
                    'kernel_smith_left','kernel_smith_diagonal']]
HL,KL,UL,DL=[mat(lr[k]) for k in ['relation_HNF','kernel_lattice',
                    'kernel_smith_left','kernel_smith_diagonal']]
rhoB=mat([br['restriction_row']])
rhoL=mat([lr['restriction_row']])
qB=[9,3,3,3]
qL=[9,3]

nine=row('e53_order_nine_genus','cyclic_nine_genus')
HF,KF,UF,DF=[mat(nine[k]) for k in ['relation_HNF','kernel_lattice',
                       'kernel_Smith_left','kernel_Smith_diagonal']]
RF=mat(nine['relation_matrix'])
SF=mat(nine['Smith_diagonal'])
SFU=mat(nine['Smith_left'])
SFV=mat(nine['Smith_right'])
KFR=mat(nine['kernel_relations'])
KFV=mat(nine['kernel_Smith_right'])
rhoF=mat([nine['restriction_row']])
assert hermite_normal_form(RF)==HF
assert SFU*HF*SFV==SF and UF*KFR*KFV==DF and KF*KFR==HF
assert all(abs(M.det())==1 for M in [SFU,SFV,UF,KFV])
assert snf(HF)==[9,9,3,3] and snf(KFR)==[9,3,3]
assert imod(rhoF*RF,9)==S.zeros(1,RF.cols)
nc=row('e53_order_nine_genus','cyclic_nine_local_characters')
assert nc['unit_character_matrix']==[[0]*7]+[[3,6,3,6,0,0,0]]*3

actions=[r for r in data['e53_normalizer_actions']
         if r['type']=='actual_normalizer']
assert [r['name'] for r in actions]==['g','h']
AG,AH=[mat(r['genus_action']) for r in actions]
Gfull,Hfull=[mat(r['coinvariant_Smith_action']) for r in actions]
assert Gfull==UB*KB.inv()*AG*KB*UB.inv()
assert Hfull==UB*KB.inv()*AH*KB*UB.inv()
for A in [AG,AH]:
    assert integral(HB.inv()*A*HB)
    assert imod(rhoB*A-rhoB,3)==S.zeros(1,9)
    assert integral(HB.inv()*(A**3-S.eye(9)))
assert integral(HB.inv()*(AG*AH-AH*AG))
assert actions[0]['S_prime_permutation']==[3,1,2,4,5,6]
assert actions[1]['S_prime_permutation']==[2,3,1,6,4,5]
G=reduced(Gfull[:4,:4],qB)
H=reduced(Hfull[:4,:4],qB)
assert G==mat([[1,0,0,0],[2,0,1,2],[2,2,2,2],[0,0,0,1]])
assert H==mat([[4,3,6,0],[2,2,2,0],[0,1,0,0],[1,0,0,1]])
assert_same(G**3-S.eye(4),qB)
assert_same(H**3-S.eye(4),qB)
assert_same(G*H-H*G,qB)
QB=all_group(qB)
QL=all_group(qL)
gimage={apply(G-S.eye(4),x,qB) for x in QB}
himage={apply(H-S.eye(4),x,qB) for x in QB}
assert gimage=={(0,0,0,0),(0,1,1,0),(0,2,2,0)}
assert len(himage)==9
dg=S.diag(*qB)
assert snf(hermite_normal_form(dg.row_join(G-S.eye(4))))==[9,3,3]
assert snf(hermite_normal_form(dg.row_join(H-S.eye(4))))==[9,3]
assert snf(hermite_normal_form(dg.row_join(G-S.eye(4)).row_join(H-S.eye(4))))==[3,3]

nr=row('e53_horizontal_upper_norm','horizontal_genus_norm')
jr=row('e53_horizontal_upper_extension','horizontal_genus_extension')
NG=mat(nr['genus_norm'])
JG=mat(jr['genus_extension'])
NF=mat(nr['coinvariant_Smith_norm'])
JF=mat(jr['coinvariant_Smith_extension'])
assert integral(HL.inv()*NG*HB) and integral(HB.inv()*JG*HL)
assert NF==UL*KL.inv()*NG*KB*UB.inv()
assert JF==UB*KB.inv()*JG*KL*UL.inv()
assert imod(rhoL*NG-rhoB,3)==S.zeros(1,9)
assert imod(rhoB*JG,3)==S.zeros(1,4)
assert integral(HL.inv()*(NG*JG-3*S.eye(4)))
assert integral(HB.inv()*(JG*NG-S.eye(9)-AH-AH**2))
N=reduced(NF[:2,:4],qL)
J=reduced(JF[:4,:2],qB)
assert N==mat([[6,3,6,3],[2,0,0,0]])
assert J==mat([[3,0],[2,1],[2,1],[1,0]])
assert_same(N*J-3*S.eye(2),qL)
assert_same(J*N-S.eye(4)-H-H**2,qB)
assert_same(N*(H-S.eye(4)),qL)
assert_same((H-S.eye(4))*J,qB)
norm_fibres=Counter(apply(N,x,qL) for x in QB)
extension_fibres=Counter(apply(J,x,qB) for x in QL)
assert len(norm_fibres)==9 and set(norm_fibres.values())=={27}
assert set(norm_fibres)==set(product([0,3,6],range(3)))
assert len(extension_fibres)==9 and set(extension_fibres.values())=={3}
kerN=[x for x in QB if apply(N,x,qL)==(0,0)]
kerJ=[x for x in QL if apply(J,x,qB)==(0,0,0,0)]
assert kerJ==[(0,0),(3,0),(6,0)]
assert kerN==[x for x in QB if x[0]%3==0 and (x[1]+2*x[2]+x[3])%3==0]

cr=row('e53_cyclic_nine_comparison','cyclic_nine_actual_comparison')
CG=mat(cr['genus_norm'])
CQ=mat(cr['coinvariant_quotient'])
assert integral(HF.inv()*CG*HB)
assert imod(rhoF*CG-3*rhoB,9)==S.zeros(1,9)
assert CQ==UF*KF.inv()*CG*KB*UB.inv()
pi=reduced(CQ[:3,:4],[9,3,3])
assert pi==mat([[5,3,6,6],[1,1,2,1],[0,0,0,2]])
pi_fibres=Counter(apply(pi,x,[9,3,3]) for x in QB)
assert len(pi_fibres)==81 and set(pi_fibres.values())=={3}
assert {x for x in QB if apply(pi,x,[9,3,3])==(0,0,0)}==gimage
assert_same(pi*(G-S.eye(4)),[9,3,3])
CM=mat(cr['cyclotomic_compositum_Artin_map'])
assert CM==mat([[1,0,1,1],[0,1,0,0]])
assert imod(CM[0,:]*RF,9)==S.zeros(1,RF.cols)
assert imod(CM[1,:]*RF,3)==S.zeros(1,RF.cols)
psi=reduced(mat([cr['mu27_character_on_Q_sigma']])[:,:4],[3])
assert psi==mat([[1,1,2,1]])
assert imod(psi*G-psi,3)==S.zeros(1,4)
assert imod(psi*H-psi,3)==S.zeros(1,4)
assert imod(psi*J,3)==mat([[1,0]])
art_fibres=Counter()
for x in all_group([9,9,3,3]):
    raw=SFU.inv()*S.Matrix(x)
    art_fibres[apply(CM,raw,[9,3])]+=1
assert len(art_fibres)==27 and set(art_fibres.values())=={27}
assert Counter(apply(psi,x,[3])[0] for x in QB)=={0:81,1:81,2:81}

# Positive connecting class from an actual tame inertia lift sigma0 at t1.
inertia=S.zeros(9,1)
inertia[3]=1
boundary=UB*KB.inv()*(inertia-AH*inertia)
delta=apply(S.eye(4),boundary[:4,:],[9,3,3,3])
assert delta==(3,0,0,0) and delta not in himage
assert set(kerN)=={
    tuple((y[i]+k*delta[i])%qB[i] for i in range(4))
    for y in himage for k in range(3)}

# Formal annihilator calculation for the full actual B2 S-class module.
t,s=S.symbols('t s')
assert S.expand((1+t)**3-1)==t**3+3*t**2+3*t
assert S.expand(1+(1+s)+(1+s)**2)==3+3*s+s**2
binomial_nine=S.Poly((1+t)**9-1-t**9,t)
assert all(int(v)%3==0 for v in binomial_nine.all_coeffs())
assert_same((G-S.eye(4))**2,qB)
# If 3^e annihilates a finite module, (3,t)^(9e) annihilates it:
# t^9 is in3R because g^9=1, and each monomial has enough3 factors.
nilpotence_monomials=0
for exponent in range(1,15):
    for a in range(9*exponent+1):
        b=9*exponent-a
        assert a+b//9>=exponent
        nilpotence_monomials+=1

# The resulting full L2 class basis is (u,a), with u=N_h(e0), p(a)=(1,1).
fullL=[9,9]
pL=mat([[6,1],[2,1]])
sigmaL=mat([[1,3],[0,1]])
fullNh=mat([[1,0,6,6],[0,3,6,3]])
fullJh=mat([[0,3],[2,0],[2,0],[0,1]])
fullNvL=mat([[0,2],[2,0]])
fullJvL=mat([[0,6],[6,0]])
fullNvB=mat([[0,0,0,2],[1,0,0,2]])
fullJvB=mat([[6,3],[0,0],[0,0],[0,0]])
lowerNh=mat([[0,0],[1,2]])
lowerJh=mat([[1,0],[1,0]])
assert_same(pL*fullNh-N,qL)
assert_same(fullJh-J*pL,qB)
assert_same(fullNh*fullJh-3*S.eye(2),fullL)
assert_same(fullJh*fullNh-S.eye(4)-H-H**2,qB)
assert_same(fullJvL*fullNvL-3*S.eye(2),fullL)
assert imod(fullNvL*fullJvL,3)==S.zeros(2)
assert_same(fullJvB*fullNvB-3*S.eye(4),qB)
assert imod(fullNvB*fullJvB,3)==S.zeros(2)
assert_same(sigmaL**3-S.eye(2),fullL)
assert_same(S.eye(2)+sigmaL+sigmaL**2-3*S.eye(2),fullL)
assert_same((sigmaL-S.eye(2))*fullNh,fullL)
assert_same(fullJh*(sigmaL-S.eye(2)),qB)
assert imod(fullNvL*fullNh-lowerNh*fullNvB,3)==S.zeros(2,4)
assert_same(fullJh*fullJvL-fullJvB*lowerJh,qB)
assert_same(fullNh*fullJvB-fullJvL*lowerNh,fullL)
fullEL=all_group(fullL)
full_horizontal_norm=Counter(apply(fullNh,x,fullL) for x in QB)
assert len(full_horizontal_norm)==27 and set(full_horizontal_norm.values())=={9}
assert set(full_horizontal_norm)==set(product(range(9),[0,3,6]))
full_horizontal_cap=[x for x in fullEL if apply(fullJh,x,qB)==(0,0,0,0)]
assert full_horizontal_cap==list(product([0,3,6],repeat=2))
assert len({apply(fullJvL,x,fullL) for x in all_group([3,3])})==9
assert {x for x in fullEL if apply(pL,x,qL)==(0,0)}=={(0,0),(3,0),(6,0)}
assert {apply(sigmaL-S.eye(2),x,fullL) for x in fullEL}=={(0,0),(3,0),(6,0)}
assert apply(fullNh,delta,fullL)==(3,0)
assert reduced(pL*fullJvL,qL)==mat([[6,0],[0,0]])
# The actual ideal-Hilbert90 norm defects A^tau/j(A_lower).
b_vertical_image={apply(fullJvB,x,qB) for x in all_group([3,3])}
assert b_vertical_image=={(0,0,0,0),(3,0,0,0),(6,0,0,0)}
defectB=Counter((x[0]%3,x[1],x[2],x[3]) for x in QB)
assert len(defectB)==81 and set(defectB.values())=={3}
fixedL=[x for x in fullEL if apply(sigmaL,x,fullL)==x]
assert set(fixedL)==set(product(range(9),[0,3,6]))
assert Counter(x[0]%3 for x in fixedL)=={0:9,1:9,2:9}
fixedH=[x for x in QB if apply(H,x,qB)==x]
assert set(fixedH)=={(3*r,t,t,s) for r,t,s in product(range(3),repeat=3)}
assert Counter((x[0]//3-x[3])%3 for x in fixedH)=={0:9,1:9,2:9}
assert {x for x in fixedH if (x[0]//3-x[3])%3==0}==set(extension_fibres)
# Every choice a -> a+3ku has the literal coordinate shear below.
for k in range(3):
    change=mat([[1,3*k],[0,1]])
    assert_same(pL*change-pL,qL)
    assert_same(change*sigmaL-sigmaL*change,fullL)
    assert_same(change*fullNh-fullNh,fullL)
    assert_same(fullJh*change-fullJh,qB)

# Literal automorphism group of C=Q(53^(1/9),zeta27).
# (a,b,e): alpha2 -> zeta9^a alpha2, zeta27 -> zeta27^(4^b(-1)^e).
def mul(x,y):
    a,b,e=x
    A,B,E=y
    return ((a+pow(4,b,9)*((-1)**e)*A)%9,(b+B)%9,(e+E)%2)
identity=(0,0,0)
def power(x,n):
    y=identity
    for _ in range(n):y=mul(y,x)
    return y
GG=list(product(range(9),range(9),range(2)))
def inverse(x):
    return next(y for y in GG if mul(x,y)==mul(y,x)==identity)
g=(1,0,0)
h=(8,1,0)
c=(0,0,1)
sigma=power(g,3)
k=power(h,3)
assert power(h,9)==power(g,9)==identity
assert mul(mul(h,g),inverse(h))==power(g,4)
assert k==(6,3,0) and power(k,3)==identity
KB2={power(k,i) for i in range(3)}
Kbar={mul(mul(c,x),c) for x in KB2}
assert KB2!=Kbar and KB2.intersection(Kbar)=={identity}
KB1={mul(x,y) for x in KB2 for y in Kbar}
assert len(KB1)==9
assert KB1==set(product([0,3,6],[0,3,6],[0]))
KL2={power(h,i) for i in range(9)}
assert len(KL2)==9 and KB2.issubset(KL2)
KL1={mul(power(sigma,i),power(h,j)) for i in range(3) for j in range(9)}
assert len(KL1)==27 and all(mul(x,y)==mul(y,x) for x in KL1 for y in KL1)

out={
    'status':'PASS',
    'scope':'The actual normalizer action and norm-extension identities prove the entire B2 and L2 S-class groups and all displayed maps. Later positional levels and ordinary class groups are not assigned these values.',
    'cyclic_nine_genus':[9,9,3,3],
    'cyclic_nine_class_coinvariants':[9,3,3],
    'Q_sigma':[9,3,3,3],
    'g':ints(G),'h':ints(H),
    'g_difference_image':sorted(gimage),'h_difference_image_order':len(himage),
    'g_coinvariants':[9,3,3],'h_coinvariants':[9,3],'joint_coinvariants':[3,3],
    'horizontal_norm':ints(N),'horizontal_extension':ints(J),
    'horizontal_norm_image_index':3,'horizontal_norm_kernel':kerN,
    'horizontal_projected_extension_kernel':kerJ,
    'actual_cyclic_nine_quotient':ints(pi),
    'mu27_character':ints(psi),
    'positive_connecting_class':list(delta),
    'full_B2_S_class':[9,3,3,3],
    'full_B2_sigma_action':'identity',
    'full_L2_S_class':[9,9],
    'full_L2_sigma_action':ints(sigmaL),
    'full_L2_projection':ints(pL),
    'full_horizontal_norm':ints(fullNh),
    'full_horizontal_extension':ints(fullJh),
    'full_vertical_B_norm':ints(fullNvB),
    'full_vertical_B_extension':ints(fullJvB),
    'full_vertical_L_norm':ints(fullNvL),
    'full_vertical_L_extension':ints(fullJvL),
    'full_horizontal_capitulation':full_horizontal_cap,
    'vertical_B_capitulation':[[0,0],[1,1],[2,2]],
    'vertical_L_capitulation':[[0,0]],
    'unit_norm_quotients':{'B_vertical':[3]*6,'B_field_norm_defect':[3]*4,
                           'L_vertical':[3],'L_field_norm_defect':[3],
                           'horizontal':[3],'horizontal_field_norm_defect':[3]},
    'completed_unit_norm_kernels':{'B':{'torsion':[3],'free_rank':18},
                                   'L':{'torsion':[3],'free_rank':6},
                                   'horizontal':{'torsion':[3],'free_rank':22}},
    'exact_Gamma_forward_B':rats(UB*KB.inv()),
    'exact_Gamma_inverse_B':ints(KB*UB.inv()),
    'exact_Gamma_forward_L':rats(UL*KL.inv()),
    'exact_Gamma_inverse_L':ints(KL*UL.inv()),
    'exact_Gamma_forward_nine':rats(UF*KF.inv()),
    'exact_Gamma_inverse_nine':ints(KF*UF.inv()),
    'finite_checks':{
        'Q_sigma_elements':len(QB),'Q_L_elements':len(QL),
        'norm_and_extension_composition_elements':len(QB)+len(QL),
        'cyclic_nine_quotient_fibres':len(pi_fibres),
        'compositum_Gamma_elements':sum(art_fibres.values()),
        'actual_normal_closure_group_order':len(GG),
        'C_over_L1_abelian_products':len(KL1)**2,
        'nilpotence_monomials':nilpotence_monomials,
        'full_L2_elements':len(fullEL),
        'full_horizontal_norm_elements':len(QB)},
    'normal_closure_field_subgroups':{
        'B2_stabilizer':sorted(KB2),'conjugate_B2_stabilizer':sorted(Kbar),
        'B1_stabilizer':sorted(KB1),'L2_stabilizer':sorted(KL2)},
    'source_sha256':{f'code/{n}.gp':sha(HERE/f'{n}.gp') for n in NAMES},
    'input_manifest':inp}
text=json.dumps(out,indent=2)+'\n'
(HERE/'e53_normalizer_module.json').write_text(text)
print(text,end='')
