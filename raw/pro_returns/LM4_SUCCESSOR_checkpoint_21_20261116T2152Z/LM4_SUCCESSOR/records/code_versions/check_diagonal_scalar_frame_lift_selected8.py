"""Actual diagonal scalar cover over the normalized free-cusp center.

Research certificate.  We retain the old opposite-weight center to lift
the canonical-c cubic shears, rather than assuming a diagonal cover is
stable after that center has been forgotten.  Full scalar closure is a
separate question.
"""
from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
import hashlib
import json
import runpy

ROOT=Path(__file__).resolve().parents[1]
with redirect_stdout(StringIO()):
    P=runpy.run_path(str(ROOT/'work_A/load_A66_W0_lower.py'))
O=P['O']
fm,fp,flin,fva,fsm=[O[k] for k in ('fm','fp','flin','fva','fsm')]


def tup(x):
    return tuple(tup(y) for y in x) if isinstance(x,list) else x


def xor(values):
    out=0
    for value in values:
        out^=value
    return out


def trace(x):
    return x^fp(x,2)^fp(x,4)


def project(x):
    return x^trace(x)


zero=(0,)*36
A0=(zero,)*4
M0=(0,)*10
Z0=(zero,)*16
U0=(0,)*4
H0=O['HN0']
pairs=O['vpairs']
mpairs=[(i,j) for i in range(4) for j in range(i,4)]
mi={ij:k for k,ij in enumerate(mpairs)}


def av(a,b):
    return tuple(fva(x,y) for x,y in zip(a,b))


def sym(a,b):
    return tuple(fm(a[i],b[j])^(fm(a[j],b[i]) if i!=j else 0)
                 for i,j in mpairs)


def weight(a,i):
    return tuple(row[i] for row in a)


def pcoc(a,b):
    out=M0
    for l,r in pairs:
        out=fva(out,sym(weight(a,l),weight(b,r)))
    return out


MD={}


def monodata(key):
    if key not in MD:
        cols=O['CV'] if key=='c' else O['hcols'](key)
        dest=[]
        scales=[]
        for col in cols:
            i=next(i for i,v in enumerate(col) if v)
            assert sum(bool(v) for v in col)==1
            dest.append(i)
            scales.append(col[i])
        assert all(O['partner'][dest[l]]==dest[r] and
                   fm(scales[l],scales[r])==1 for l,r in pairs)
        MD[key]=(dest,scales)
    return MD[key]


def act(key,rows,degree=1):
    dest,scales=monodata(key)
    out=[]
    for row in rows:
        v=[0]*36
        for i,x in enumerate(row):
            v[dest[i]]=fm(fp(scales[i],degree),x)
        out.append(tuple(v))
    return tuple(out)


def monop(key,a,m):
    dest,_=monodata(key)
    for l,r in pairs:
        if dest[l]>dest[r]:
            m=fva(m,sym(weight(a,l),weight(a,r)))
    return act(key,a),m


def pm(g,h):
    a,m,q=g
    b,n,r=h
    b,n=monop(q,b,n)
    return av(a,b),fva(fva(m,n),pcoc(a,b)),O['hmul'](q,r)


PONE=(A0,M0,H0)


def pi(g):
    a,m,q=g
    inv=O['hinv'](q)
    b=act(inv,a)
    _,carry=monop(q,b,M0)
    out=(b,fva(fva(m,carry),pcoc(a,a)),inv)
    assert pm(g,out)==pm(out,g)==PONE
    return out


def pin(g,h):
    return pm(pm(g,h),pi(g))


# Exact old-center projection, including the actual source gauge.
E=tup(P['E'][:4])
gauge=tup(P['ag'][:4])
ecols=[tuple(row[i] for row in E) for i in range(8)]
mcols=[sym(ecols[i],ecols[j]) for i,j in O['zpairs']]


def oldm(z):
    return flin(mcols,z)


assert oldm(O['QS'])==M0
GAUGE=(gauge,M0,H0)


def ungauged(g):
    return pin(GAUGE,(O['mix'](E,g[0]),oldm(g[1]),g[2]))


Sg=ungauged(O['SS'])
assert Sg[0]==A0 and Sg[2]==O['HS']
MS=Sg[1]


def old_project(g):
    a,m,h=ungauged(g)
    return a,fva(m,MS) if O['eps'](h) else m,h


assert old_project(O['SS'])==(A0,M0,O['HS'])
ra=act(O['HR'],P['ac'](O['RR']))
PR=pin((ra,M0,H0),(A0,M0,O['HR']))
assert old_project(O['RR'])==PR
words=[O['ONE'],O['SS'],O['RR'],O['TT'],O['ei'](O['TT'])]
for g in words:
    assert old_project(O['ph'](g))==old_project(g)
    for h in words:
        assert old_project(O['em'](g,h))==pm(old_project(g),old_project(h))
print('Normalized free-cusp center10 is an actual old-source projection; C4 class vanishes there: PASS',flush=True)


def cup(a,b):
    return tuple(tuple(fm(fp(x,2),y) for x,y in zip(a[r],b[i]))
                 for r in range(4) for i in range(4))


def fcoc(a,z,b,w):
    return tuple(project(xor(fm(z[5*i][j],fp(b[i][j],4))^
                             fm(fp(a[i][j],2),fp(w[5*i][j],4))
                             for j in range(36))) for i in range(4))


ONE=(A0,M0,Z0,U0,H0)


def gm(g,h):
    a,m,z,u,q=g
    b,n,w,v,r=h
    b,n=monop(q,b,n)
    w=act(q,w,3)
    return (av(a,b),fva(fva(m,n),pcoc(a,b)),
            av(av(z,w),cup(a,b)),fva(fva(u,v),fcoc(a,z,b,w)),
            O['hmul'](q,r))


def gi(g):
    a,m,z,u,h=g
    ih=O['hinv'](h)
    b=act(ih,a)
    _,carry=monop(h,b,M0)
    n=fva(fva(m,carry),pcoc(a,a))
    w=act(ih,av(z,cup(a,a)),3)
    pre=(b,n,w,U0,ih)
    err=gm(g,pre)
    assert err[0]==A0 and err[1]==M0 and err[2]==Z0 and err[4]==H0
    out=(b,n,w,err[3],ih)
    assert gm(g,out)==gm(out,g)==ONE
    return out


def gin(g,h):
    return gm(gm(g,h),gi(g))


S=(A0,M0,Z0,U0,O['HS'])
R=gin((ra,M0,Z0,U0,H0),(A0,M0,Z0,U0,O['HR']))
T=gm(S,R)
assert gm(S,S)==ONE and gm(gm(R,R),R)==ONE
ordinary=json.loads((ROOT/'work_A/A66_W0_local_ordinary_result.json').read_text())
assert R[2]==tup(ordinary['source_R_central'])
assert (R[0],R[1],R[4])==PR
print('Four diagonal trace-zero scalar covers: actual source S²=R³=1 and ordinary projection: PASS',flush=True)

CC=tup(ordinary['canonical_c_corrections'])
L=tuple(row[:4] for row in CC)
VC=tuple(row[8:] for row in CC)
assert all(not any(row[4:8]) for row in CC)
CW=tup(P['wc'])


def j3(v):
    return tuple(fp(v[O['partner'][i]],4) for i in range(36))


def psi(a,m,i,j,lamb):
    q=xor(fm(a[i][left],a[j][right]) for left,right in pairs)
    if i==j:
        return project(fm(lamb,fp(q,4))^fm(fp(lamb,4),fp(q,2)))
    p=xor(fm(a[j][left],a[i][right]) for left,right in pairs)
    mij=m[mi[tuple(sorted((i,j)))]]
    return project(fm(lamb,fp(mij^q,4))^
                   fm(fp(lamb,4),fp(mij^p,2)))


def shear(g):
    a,m,z,u,h=g
    aa=[j3(v) for v in a]
    zz=tuple(fva(v,flin(aa,row)) for v,row in zip(z,L))
    uu=tuple(u[i]^xor(psi(a,m,i,j,L[5*i][j])
                      for j in range(4) if L[5*i][j]) for i in range(4))
    return a,m,zz,uu,h


def mono_c(g):
    a,m,z,u,h=g
    a,m=monop('c',a,m)
    return a,m,act('c',z,3),u,O['hc'](h)


W=(CW,M0,Z0,U0,H0)
V=(A0,M0,VC,U0,H0)


def candidate_c(g):
    return gin(V,shear(gin(W,mono_c(g))))


CS=candidate_c(S)
assert CS[0]==A0 and CS[2]==Z0 and CS[4]==O['HS']
CM,CU=CS[1],CS[3]


def ca(g):
    a,m,z,u,h=candidate_c(g)
    if O['eps'](g[4]):
        m=fva(m,CM)
        u=fva(u,CU)
    return a,m,z,u,h


assert ca(S)==S
assert ca(R)==gm(gm(S,gi(R)),S)
assert ca(T)==gi(T)
assert ca(ca(S))==S and ca(ca(R))==R
sample=[ONE,S,R,T,gi(T),gm(R,T),gm(T,R)]
for g in sample:
    assert shear(shear(g))==g
    assert ca(ca(g))==g
    for h in sample:
        assert shear(gm(g,h))==gm(shear(g),shear(h))
        assert ca(gm(g,h))==gm(ca(g),ca(h))
print('Old-center scalar shear lift and exact canonical c on actual source: PASS',flush=True)

full=json.loads((ROOT/'work_A/A66_W0_twenty_sframe_solution.json').read_text())
bf=tup(full['BFRAME'])
bp=old_project(bf[0][0])
B=(bp[0],bp[1],bf[1][4:],U0,bp[2])
assert gin(B,S)==S
bn=gm(gi(B),ca(gi(B)))
assert bn[0]==A0 and bn[1]==M0 and bn[2]==Z0 and bn[4]==H0
print('Current full20 frame scalar square:',bn[3],flush=True)

# Corrections that preserve the complete previous twenty-factor norm.
# Their ordinary multiplicity lies in ker J; their weight vector is
# fixed by both S and the diagonal reflection D.  Scalar norms are
# binary linear on this abelian correction space.
SF3=[j3(v) for v in O['SF']]


def d3(v):
    return act(O['HB'],act('c',(v,),3),3)[0]


fixed_coeff=O['fkernel']([fva(v,d3(v)) for v in SF3])
fixed=[flin(SF3,v) for v in fixed_coeff]
assert len(fixed)==12
assert all(act(O['HS'],(v,),3)[0]==v and d3(v)==v for v in fixed)
J=tup(full['shear_columns'])
JK=O['fkernel'](J)
assert len(JK)==12
norm_columns=[]
directions=[]


def pack4(v):
    return sum(x<<(3*i) for i,x in enumerate(v))


def reflection(g):
    return gin(gi(B),ca(g))


for ii,mult in enumerate(JK):
    assert flin(J,mult)==(0,)*4
    for jj,v in enumerate(fixed):
        for scalar in (1,2,4):
            z=tuple(fsm(fm(scalar,x),v) for x in mult)
            k=(A0,M0,z,U0,H0)
            assert gin(k,S)==S
            n=gm(k,reflection(k))
            assert n[0]==A0 and n[1]==M0 and n[2]==Z0 and n[4]==H0
            norm_columns.append(pack4(n[3]))
            directions.append((ii,jj,scalar))
solution,rank=O['bit_solve'](norm_columns,pack4(bn[3]))
print('Old-norm-preserving ordinary correction space: 432 bits; scalar norm rank:',rank,
      '; target solvable:',solution is not None,flush=True)
fixed_frame=None
correction=None
if solution is not None:
    z=Z0
    for k,(ii,jj,scalar) in enumerate(directions):
        if (solution>>k)&1:
            z=av(z,tuple(fsm(fm(scalar,x),fixed[jj]) for x in JK[ii]))
    correction=(A0,M0,z,U0,H0)
    assert gin(correction,S)==S
    fixed_frame=gm(B,correction)
    assert gin(fixed_frame,S)==S
    assert gm(gi(fixed_frame),ca(gi(fixed_frame)))==ONE
    print('Corrected scalar s-frame conjugacy and literal norm: PASS',flush=True)

out=dict(scope='Actual four diagonal scalar covers with old free-center retained; full scalar kernel not determined.',
         old_center_projection_columns=mcols,old_source_gauge=gauge,
         source_center_shift=MS,source_R=R,canonical_c_center_shift=CM,
         canonical_c_scalar_shift=CU,full20_frame_projection=B,
         scalar_frame_square=bn[3],scalar_frame_solved=bn[3]==U0,
         actual_source_and_c_checks='PASS',old_witness=full['old_witness'],
         correction_joint_fixed_weight_basis=fixed,
         correction_shear_kernel_basis=JK,correction_binary_labels=directions,
         correction_norm_columns=norm_columns,correction_norm_rank=rank,
         correction_solution_mask=solution,correction=correction,
         corrected_frame=fixed_frame,corrected_scalar_s_norm=fixed_frame is not None)
(ROOT/'records/diagonal_scalar_frame_lift.json').write_text(json.dumps(out,indent=2)+'\n')
print('No conclusion about the complete scalar refinement or a full negative involution.',flush=True)
