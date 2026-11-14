#!/usr/bin/env python3
"""E119. Exact lower positional53 fields, unit maps and class coinvariants.

Full portable reconstruction (ten GP stages, no upper BNF certification):
  python e_lower_fiftythree.py --gp /absolute/path/gp
The complete deserialized GP objects, not implementation serialization bytes,
are arithmetic certificates.  The two dependency sources are frozen E116
sources; all eight owned stages run in an initially empty directory.
"""
from pathlib import Path
from fractions import Fraction
from itertools import product
from collections import Counter
import argparse, hashlib, json, shutil, subprocess, tempfile
import sympy as S
from sympy.matrices.normalforms import hermite_normal_form

HERE=Path(__file__).resolve().parent
INPUTS=HERE.parent/'inputs'
GP_NAMES=[
 'e53_horizontal_base','e53_genus_kummer','e53_six_character_witness',
 'e53_horizontal_norm_matrix','e53_genus_transition','e53_local_genus_maps',
 'e53_positional_horizontal_norm','e53_positional_genus_transition']
DEPS=[('e116_small_inert_units','e_small_inert_units'),
      ('e116_prime_columns','e53_prime_columns')]
parser=argparse.ArgumentParser();parser.add_argument('--gp');args=parser.parse_args()

def parse_bytes(data,label):
    lines=data.decode().splitlines()
    # The exact PARI stack-allocation notice is harmless; mathematical errors
    # start with the same three stars and are rejected separately.
    bad=[x for x in lines if '***' in x and
         not (x.strip().startswith('***   Warning: new stack size = ') or
              x.strip().startswith('***   Warning: new maximum stack size = '))]
    assert not bad,(label,bad)
    rows=[json.loads(x) for x in lines if x.startswith('{')]
    assert rows and rows[-1].get('status')=='PASS',label
    return rows

if args.gp:
    gp=str(Path(args.gp).resolve())
    with tempfile.TemporaryDirectory(prefix='e119_full_') as td:
        td=Path(td);work=td/'code';inp=td/'inputs';dep=td/'dep'
        for p in (work,inp,dep):p.mkdir()
        for alias,original in DEPS:
            shutil.copy2(INPUTS/(alias+'.gp'),dep/(original+'.gp'))
        for alias,original in DEPS:
            run=subprocess.run([gp,'-q','-f',original+'.gp'],cwd=dep,
                               stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (INPUTS/(alias+'.out')).write_bytes(run.stdout)
            assert run.returncode==0,(original,run.returncode)
            parse_bytes(run.stdout,original)
            for dest in (inp,INPUTS):
                shutil.copy2(dep/(original+'.bin'),dest/(alias+'.bin'))
        for name in GP_NAMES:shutil.copy2(HERE/(name+'.gp'),work/(name+'.gp'))
        for name in GP_NAMES:
            run=subprocess.run([gp,'-q','-f',name+'.gp'],cwd=work,
                               stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
            (HERE/(name+'.out')).write_bytes(run.stdout)
            assert run.returncode==0,(name,run.returncode)
            parse_bytes(run.stdout,name)
        for p in work.glob('*.bin'):shutil.copy2(p,HERE/p.name)

records={name:parse_bytes((HERE/(name+'.out')).read_bytes(),name) for name in GP_NAMES}
dep_records={a:parse_bytes((INPUTS/(a+'.out')).read_bytes(),a) for a,o in DEPS}
def row(name,typ):
    r=[x for x in records[name] if x['type']==typ];assert len(r)==1,(name,typ)
    return r[0]
def mat(x):return S.Matrix(x)
def ints(m):return [[int(v) for v in m.row(i)] for i in range(m.rows)]
def imod(m,n):return m.applyfunc(lambda x:int(x)%n)
def integral(m):return all(S.denom(x)==1 for x in m)
def r3(m):
    a=[[int(v)%3 for v in m.row(i)] for i in range(m.rows)];rank=0
    for j in range(m.cols):
        pivot=next((i for i in range(rank,len(a)) if a[i][j]),None)
        if pivot is None:continue
        a[rank],a[pivot]=a[pivot],a[rank]
        q=pow(a[rank][j],-1,3);a[rank]=[(q*x)%3 for x in a[rank]]
        for i in range(len(a)):
            if i!=rank:
                q=a[i][j];a[i]=[(x-q*y)%3 for x,y in zip(a[i],a[rank])]
        rank+=1
        if rank==len(a):break
    return rank

base=row('e53_horizontal_base','cyclotomic_base')
lower=row('e53_horizontal_base','positional_first')
real=row('e53_horizontal_base','real_fixed_upper')
assert base['class_number']==1 and base['flag0_return']==1
assert mat(base['tame_characters'])==S.zeros(3,7)
assert lower['flag0_return']==1 and lower['class_number']==27
assert lower['class_cyclic']==[9,3] and lower['S_class']==[3,3]
assert real['flag']==1 and real['return']==1 and real['natural_upper_class_cyclic']==[3]
assert real['S_prime_classes']==[[1],[1],[0],[0],[0]]

# Literal Kummer radicals and the local Hensel witness, checked in Q[x]/Phi9.
x=S.Symbol('x');phi=x**6+x**3+1
def reduce(p):return S.rem(p,phi,x)
def polynomial(v):return sum(S.Rational(a)*x**i for i,a in enumerate(v))
rad=row('e53_genus_kummer','actual_genus_radicals')
pis=[polynomial(v) for v in rad['radicals']]
assert reduce(S.prod(pis))==53
assert all(reduce(pis[j].subs(x,x**4)-pis[(j+1)%3])==0 for j in range(3))
assert abs(mat(rad['valuation_matrix']).det())==1
assert rad['local_cube_at_three']==[1,1,1]
assert mat(rad['local_cube_units_at_53'])==S.ones(3)
hensel=row('e53_local_genus_maps','hensel_cube_witness')
w=polynomial(hensel['root_polynomial'])
def v3(n):
    n=abs(int(n));assert n;v=0
    while n%3==0:v+=1;n//=3
    return v
assert v3(S.resultant(phi,reduce(w**3-pis[0]),x))==13
assert v3(S.resultant(phi,reduce(3*w*w),x))==6

# A second tame calculation uses pairs in (Z/53^2)[z]/(z^2+z+1).
p=53;mod=p*p
def mul(a,b,m):return ((a[0]*b[0]-a[1]*b[1])%m,
                       (a[0]*b[1]+a[1]*b[0]-a[1]*b[1])%m)
def power(a,n,m):
    z=(1,0)
    while n:
        if n&1:z=mul(z,a,m)
        a=mul(a,a,m);n//=2
    return z
def evpoly(poly,a,m):
    val=(0,0)
    for c in S.Poly(poly,x).all_coeffs():
        val=mul(val,a,m);val=((val[0]+int(c))%m,val[1])
    return val
roots=[]
for a,b in product(range(p),repeat=2):
    if power((a,b),3,p)==(0,1):roots.append((a,b))
assert len(roots)==3
tame=[]
for a in roots:
    f=power(a,9,mod);f=((f[0]-1)%mod,f[1]);d=mul((9,0),power(a,8,mod),mod)
    dinv=power(d,p*(p*p-1)-1,mod)
    assert mul(d,dinv,mod)==(1,0)
    corr=mul(f,dinv,mod);ar=((a[0]-corr[0])%mod,(a[1]-corr[1])%mod)
    assert power(ar,9,mod)==(1,0)
    vals=[]
    for pi in pis:
        z=evpoly(pi,ar,mod)
        if z[0]%p==z[1]%p==0:z=(z[0]//p,z[1]//p)
        else:z=(z[0]%p,z[1]%p)
        assert power(z,(p*p-1)//3,p)==(1,0)
        vals.append(z)
    tame.append({'xi_mod53':a,'xi_mod2809':ar,'unit_residues':vals})

# The exact horizontal class maps are calibrated by literal residue primes.
pm=row('e53_genus_kummer','actual_prime_norms')['records_p_xi_alpha_beta_genus_class_Sclass']
for p,xi,a,b,e,cl,sc in pm:
    assert S.isprime(p) and pow(xi,3,p)!=1 and pow(xi,9,p)==1
    assert pow(a,3,p)==53%p and b==a*xi%p
    assert sum(e)%3==0 and sc==[0,(e[0]+2*e[1])%3]
art=row('e53_local_genus_maps','horizontal_Artin_and_transfer')
assert art['Artin_row_on_L_S_basis']==[2,0]
NH=mat(art['norm_on_B_genus_coordinates']);JH=mat(art['extension_on_L_S_basis'])
assert imod(NH*JH,3)==S.zeros(2) and imod(JH*NH,3)==S.zeros(2)
for pp,i,f,cl,sc,ar in art['actual_prime_basis']:
    assert sc==[q%3 for q in cl] and ar==2*sc[0]%3

# Exact group giving transfer: I sits in F3^3 semidirect C3, tau=(-e0,h).
def cyc(e,b):return tuple(e[(j-b)%3] for j in range(3))
def prod(a,b):
    e,k=a;f,l=b;ff=cyc(f,k)
    return (tuple((e[i]+ff[i])%3 for i in range(3)),(k+l)%3)
def gp_power(a,n):
    out=((0,0,0),0)
    for _ in range(n):out=prod(out,a)
    return out
GG=[(e,b) for e in product(range(3),repeat=3) for b in range(3) if (sum(e)+b)%3==0]
assert len(GG)==27
assert all(prod(a,b) in GG for a in GG for b in GG)
tau=((2,0,0),1)
assert gp_power(tau,3)==((2,2,2),0)
assert all(tuple(sum(cyc(e,j)[i] for j in range(3))%3 for i in range(3))==(0,0,0)
           for e,b in GG if b==0)

# Full completed unit bases: independently saturated ordinary units and an
# independently determined principal S-divisor lattice.
norm=row('e53_horizontal_norm_matrix','actual_horizontal_norm')
NM=mat(norm['norm_matrix']);HN=mat(norm['image_HNF'])
rel=NM.row_join(S.Matrix([3,0,0,0,0,0,0]))
assert HN==hermite_normal_form(rel) and abs(HN.det())==9
sat=row('e53_horizontal_norm_matrix','unit_saturation')
RM=mat(sat['matrix']);RI=mat(sat['inverse_mod3'])
assert RM.det()==-17 and imod(RM*RI,3)==S.eye(9)
assert imod(RI*RM,3)==S.eye(9)
ch=row('e53_six_character_witness','six_characters')
C=mat(ch['character_matrix']);Vals=mat(ch['S_valuation_matrix'])
assert r3(C)==2 and all(sum(C[:,j])%3==0 for j in range(15))
assert all(C[i,:]==C[0,:] for i in range(3))
assert all(C[i,:]==C[3,:] for i in range(3,6))
assert r3(C[:,:9])==1
VH=hermite_normal_form(Vals)
assert abs(VH.det())==9
assert all((Vals[0,j]-Vals[1,j])%3==(Vals[0,j]-Vals[2,j])%3==0 for j in range(15))

def norm_M_inverse(t):
    z,xx,yy,a1,a2,a3,ww=t
    assert (a2-a1)%3==(a3-a1)%3==0
    r=a1;ss=(a2-a1)//3;tt=(a3-a1)//3;dd=r+ss+tt
    xp=xx-2*dd;yp=yy-dd;n=S.zeros(15,1)
    n[11]=r;n[9]=ss;n[10]=tt;n[7]=xp;n[8]=yp-xp;n[12]=ww
    n[0]=(z-2*yp-dd-ww)%3
    return n
def equal_target(got,target):
    return int(got[0]-target[0])%3==0 and list(got[1:])==list(target[1:])
M_checks=0
for z,a1,b2,b3 in product(range(3),range(-2,3),range(-1,2),range(-1,2)):
    for xx,yy,ww in ((-2,3,1),(0,0,0),(2,-1,-2)):
        t=(z,xx,yy,a1,a1+3*b2,a1+3*b3,ww)
        assert equal_target(NM*norm_M_inverse(t),t);M_checks+=1
MK=S.zeros(15,9);MK[0,0]=3
for j,idx in enumerate([1,2,3,4,5,6,13,14],1):
    b=S.zeros(15,1);b[idx]=1;MK[:,j]=b-norm_M_inverse(tuple(NM*b))
assert all(int((NM*MK)[0,j])%3==0 for j in range(MK.cols))
assert NM[1:,:]*MK==S.zeros(6,9)
assert MK[:,0]==S.Matrix([3]+[0]*14)
Mkernel_checks=0
for z in range(9):
    for j in range(14):
        a=S.zeros(15,1);a[0]=z;a[j+1]=1
        t=tuple(NM*a);res=a-norm_M_inverse(t)
        # Pivot equations force precisely the displayed eight free columns.
        ks=[int(res[i]) for i in [1,2,3,4,5,6,13,14]]
        diff=res-MK[:,1:]*S.Matrix(ks)
        assert list(diff[1:])==[0]*14 and int(diff[0])%3==0
        assert imod(diff-MK[:,0]*(int(diff[0])//3),9)==S.zeros(15,1)
        Mkernel_checks+=1

pn=row('e53_positional_horizontal_norm','positional_horizontal_norm')
NL=mat(pn['norm_matrix'])
assert hermite_normal_form(NL.row_join(S.Matrix([3,0,0,0,0])))==S.eye(5)
def norm_L_inverse(t):
    z,xx,yy,cc,dd=t;xp=xx-2*cc;yp=yy-2*cc+dd
    n=S.zeros(15,1);n[9]=cc;n[12]=dd;n[8]=-xp;n[7]=xp-yp;n[0]=(z-2*cc)%3
    return n
LK=S.zeros(15,11);LK[0,0]=3
freeL=[1,2,3,4,5,6,10,11,13,14]
for j,idx in enumerate(freeL,1):
    b=S.zeros(15,1);b[idx]=1;LK[:,j]=b-norm_L_inverse(tuple(NL*b))
assert NL[1:,:]*LK==S.zeros(4,11)
assert all(int((NL*LK)[0,j])%3==0 for j in range(11))
L_checks=0
for z,xx,yy,cc,dd in product(range(3),range(-2,3),range(-2,3),range(-1,2),range(-1,2)):
    t=(z,xx,yy,cc,dd);assert equal_target(NL*norm_L_inverse(t),t);L_checks+=1

# Both complete idele presentations, all exact Smith forward/inverse maps.
def verify_genus(r,expected_gamma,expected_kernel,norm_key):
    Rel=mat(r['relation_matrix']);H=mat(r['relation_HNF'])
    U=mat(r['smith_left']);V=mat(r['smith_right']);D=mat(r['smith_diagonal'])
    K=mat(r['kernel_lattice']);KR=mat(r['kernel_relation_matrix'])
    KU=mat(r['kernel_smith_left']);KV=mat(r['kernel_smith_right']);KD=mat(r['kernel_smith_diagonal'])
    ar=mat([r['restriction_row']])
    assert H==hermite_normal_form(Rel) and U*H*V==D
    assert abs(U.det())==abs(V.det())==1
    assert K*KR==H and integral(KR) and KU*KR*KV==KD
    assert abs(KU.det())==abs(KV.det())==1
    assert abs(K.det())==3 and imod(ar*Rel,3)==S.zeros(1,Rel.cols)
    gd=[int(D[i,i]) for i in range(D.rows) if D[i,i]!=1]
    kd=[int(KD[i,i]) for i in range(KD.rows) if KD[i,i]!=1]
    assert gd==expected_gamma and kd==expected_kernel
    N=mat(r[norm_key]);dd=kd+[1]*(K.rows-len(kd))
    assert imod(N*KD,3)==S.zeros(N.rows,N.cols)
    images=Counter();roundtrips=0
    for xx in product(*(range(q) for q in kd)):
        z=S.Matrix(list(xx)+[0]*(K.rows-len(xx)))
        raw=K*KU.inv()*z
        assert integral(raw) and int((ar*raw)[0])%3==0
        back=KU*K.inv()*raw
        assert back==z
        images[tuple(int(v)%3 for v in N*z)]+=1;roundtrips+=1
    assert len(images)==9 and len(set(images.values()))==1
    # Exhaust the full finite abelian extension and its actual restriction.
    fibres=Counter()
    for xx in product(*(range(q) for q in gd)):
        z=S.Matrix(list(xx)+[0]*(H.rows-len(xx)));raw=U.inv()*z
        fibres[int((ar*raw)[0])%3]+=1
    assert fibres=={0:roundtrips,1:roundtrips,2:roundtrips}
    return {'Gamma':gd,'coinvariants':kd,'norm_matrix':ints(N[:,:len(kd)]),
            'norm_fibres':{str(k):v for k,v in sorted(images.items())},
            'exact_Smith_roundtrips':roundtrips,'Gamma_restriction_fibres':dict(fibres),
            'kernel_lattice':ints(K),'forward':ints(KU*K.inv()),
            'inverse':ints(K*KU.inv()),'relation_HNF':ints(H)}

gb=row('e53_genus_transition','next_genus_presentation')
gl=row('e53_positional_genus_transition','positional_genus_transition')
resB=verify_genus(gb,[9,3,3,3,3],[9,3,3,3],'actual_norm_matrix')
resL=verify_genus(gl,[9,3,3],[9,3],'norm_matrix')
ordinary=row('e53_genus_transition','ordinary_class_actual_generation')
assert ordinary['orders']==[9,3,3]
assert r3(mat(ordinary['genus_coordinates']))==2
assert all(S.isprime(rec[1]) for rec in ordinary['factor_records'])
assert mat(ordinary['S_prime_coordinates'])==S.Matrix([[3,0,6,0,0,0],[1,1,1,0,0,0],[0,0,0,0,0,0]])
K=mat(gb['kernel_lattice']);KU=mat(gb['kernel_smith_left'])
ideal_lifts=S.zeros(9,2);ideal_lifts[6,0]=1;ideal_lifts[6,1]=-1;ideal_lifts[8,1]=2
JB=KU*K.inv()*(3*ideal_lifts)
JBred=S.Matrix(4,2,lambda i,j:int(JB[i,j])%([9,3,3,3][i]))
assert JBred==S.Matrix([[6,3],[0,0],[0,0],[0,0]])
JL=mat(gl['extension_matrix_to_coinvariants'])
JLred=S.Matrix(2,2,lambda i,j:int(JL[i,j])%([9,3][i]))
assert JLred==S.Matrix([[6,0],[0,0]])
transfer_checks=0
for N,J,mods in [(mat(gb['actual_norm_matrix'])[:,:4],JBred,[9,3,3,3]),
                  (mat(gl['norm_matrix'])[:,:2],JLred,[9,3])]:
    assert imod(N*J,3)==S.zeros(2)
    for xx in product(*(range(q) for q in mods)):
        z=S.Matrix(xx);a=imod(N*z,3);r=J*a-3*z
        assert all(int(r[i])%mods[i]==0 for i in range(len(mods)))
        transfer_checks+=1

# Exact necessary capitulation bounds and the two S-unit index formulae.
capB=[(a,b) for a,b in product(range(3),repeat=2)
      if all(int((JBred*S.Matrix([a,b]))[i])%[9,3,3,3][i]==0 for i in range(4))]
capL=[(a,b) for a,b in product(range(3),repeat=2)
      if all(int((JLred*S.Matrix([a,b]))[i])%[9,3][i]==0 for i in range(2))]
assert capB==[(0,0),(1,1),(2,2)] and capL==[(0,0),(0,1),(0,2)]

sources=[HERE/(n+'.gp') for n in GP_NAMES]+[INPUTS/(a+'.gp') for a,o in DEPS]
out={
 'statement':'E.119','status':'PASS','GP_stages':10,
 'full_B1_S_class_group':[3,3],'full_B1_ordinary_three_class_group':[9,3,3],
 'full_L1_S_class_group':[3,3],'full_L1_ordinary_three_class_group':[9,3],
 'real_fixed_class_upper_flag':1,'real_fixed_class_upper_cyclic':[3],
 'Kummer_radicals':rad['radicals'],'Hensel_error_derivative_valuations':[13,6],
 'independent_tame_local_cube_tests':tame,
 'horizontal_class_norm':ints(NH),'horizontal_class_extension':ints(JH),
 'horizontal_finite_group_order':len(GG),'horizontal_group_products_checked':len(GG)**2,
 'ordinary_unit_saturation_determinant':int(RM.det()),
 'S_divisor_HNF':ints(VH),'complete_six_character_matrix':ints(C),'six_character_rank':2,
 'norm_to_M':{'matrix':ints(NM),'index':9,'kernel_free_rank':8,'kernel_torsion':[3],
              'kernel_basis':ints(MK),'inverse_checks':M_checks,'kernel_coordinate_checks':Mkernel_checks},
 'norm_to_L1':{'matrix':ints(NL),'index':1,'kernel_free_rank':10,'kernel_torsion':[3],
               'kernel_basis':ints(LK),'inverse_checks':L_checks},
 'B2_genus':resB,'B2_extension_to_coinvariants':ints(JBred),
 'L2_genus':resL,'L2_extension_to_coinvariants':ints(JLred),
 'norm_transfer_composition_checks':transfer_checks,
 'B2_actual_capitulation_embeds_in':capB,'L2_actual_capitulation_embeds_in':capL,
 'B2_S_unit_norm_index_per_actual_capitulation_order':3**5,
 'B2_field_norm_S_unit_index':9,
 'L2_S_unit_norm_index_per_actual_capitulation_order':3,
 'L2_field_norm_S_unit_index':1,
 'successful_GP_record_counts':{k:len(v) for k,v in records.items()},
 'source_sha256':{str(p.relative_to(HERE.parent)):hashlib.sha256(p.read_bytes()).hexdigest() for p in sources},
 'scope':'The full lower B1 and L1 class/unit maps are evaluated. At B2 and L2 the evaluated groups are precisely the sigma-coinvariants, with exact norm, extension and quotient maps. The full upper class groups retain the explicit unevaluated kernels (sigma-1)A2; no higher stability is asserted.'}
text=json.dumps(out,indent=2)+'\n';(HERE/'e_lower_fiftythree.json').write_text(text);print(text,end='')
