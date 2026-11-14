#!/usr/bin/env python3
"""The full actual gamma3(N) module through K degree eight.

Unlike degree seven, conjugation by N can act on this module.  All degree
six, seven and eight terms of the actual torsion-conjugate action are kept.
"""
from pathlib import Path
from contextlib import redirect_stdout
from itertools import product
import io,runpy,json,time
import d_cm_degree8_magnus as G
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):R=runpy.run_path(str(OUT/'d_cm_rank4_refine.py'))
oldcomm=G.comm
def fastcomm(a,b):
    da,db=G.mindeg(a),G.mindeg(b);dd=da+db
    if dd>8:return G.UNIT
    if dd<5:return oldcomm(a,b)
    z=[0]*9
    for i in range(da,9-db):
        if not a[i]:continue
        for j in range(db,9-i):
            if b[j]:z[i+j]^=G.mp(a[i],i,b[j],j)^G.mp(b[j],j,a[i],i)
    extra=8-dd
    if extra:
        aa=tuple(a[i] if i<=extra else 0 for i in range(9))
        bb=tuple(b[i] if i<=extra else 0 for i in range(9))
        h=G.mul(G.inverse(aa),G.inverse(bb));zz=z.copy()
        for i in range(dd,9):
            for j in range(1,9-i):
                if z[i] and h[j]:zz[i+j]^=G.mp(z[i],i,h[j],j)
        z=zz
    return tuple(z)
def read(word,n=4):
    q,w=R['collapse'](word);assert q==R['e'];P=R['poly'](w,n)
    return (0,)+tuple(R['bitpoly'](P[i]) if i<=n else 0 for i in range(1,9))
def trunc(p,n):return tuple(p[i] if i<=n else 0 for i in range(9))
def pack(p):return p[6]<<81920 ^ p[7]<<65536 ^ p[8]

labels=[];b6={}
for i,j,k in product(range(9),repeat=3):
    z=R['bracket'](R['rel'][i],2,R['bracket'](R['rel'][j],2,R['rel'][k],2),4)
    rem=z
    while rem:
        p=rem.bit_length()-1
        if p not in b6:
            b6[p]=rem;labels.append(['222',i,j,k]);break
        rem^=b6[p]
assert len(labels)==240
labels += [['223',i,j,k] for i,j,k in json.loads((OUT/'d_cm_rank4_degree7.json').read_text())['degree7_basis_indices']]
labels += json.loads((OUT/'d_cm_degree8_common.json').read_text())['degree8_gamma3_basis_indices']
assert len(labels)==9105

L4words=[]
for power,d in ((1,4),(2,2),(4,1)):
    for w in product(range(4),repeat=d):
        if R['lyndon'](w):L4words.append(R['lieword'](w)*power)
words={'2':R['relwords'],'3':[R['lieword'](w) for w in R['L3']],'4':L4words}
base={k:[read(w) for w in ww] for k,ww in words.items()}
J=json.loads((OUT/'d_cm_quadratic_search.json').read_text())['witness']
def nword(mask):
    ans=[]
    while mask:
        bit=mask&-mask;ans+=R['Nwords'][bit.bit_length()-1];mask^=bit
    return ans
qb=R['D']['canon'](tuple(J['beta']))
short=nword(int(J['homology_beta_cycles'],16))+R['reps'][qb]
fixed=json.loads((OUT/'d_cm_class2_two.json').read_text())['s_centralizer_basis']
right=int(J['beta_right_s_centralizer_coefficients'],16)
for j,v in enumerate(fixed):
    if (right>>j)&1:short+=nword(int(v,16))
bp=read(short,3);fullks=G.mul(bp,G.involution(G.inverse(bp)));assert not fullks[1]
ks=(0,0,fullks[2])+ (0,)*6
def S(p):return trunc(G.mul(G.mul(ks,G.involution(p)),G.inverse(ks)),4)
sb={k:[S(p) for p in pp] for k,pp in base.items()}
tb={k:[read([0,1]+w+[2,0]) for w in ww] for k,ww in words.items()}
def build(data):
    inners={}
    ans=[]
    for typ,i,j,k in labels:
        key=(typ[1:],j,k)
        if key not in inners:inners[key]=fastcomm(data[typ[1]][j],data[typ[2]][k])
        p=fastcomm(data[typ[0]][i],inners[key]);assert G.mindeg(p)>=6
        ans.append(pack(p))
    return ans
U=build(base);US=build(sb);UT=build(tb)
print('Actual gamma3 module basis/action vectors:',len(U),flush=True)
ue=R['echelon'](U);assert len(ue)==9105
columns=[u^s for u,s in zip(U,US)]+[s^t for s,t in zip(US,UT)]
bas={}
for j,v in enumerate(columns):
    cert=1<<j
    while v:
        k=v.bit_length()-1
        if k not in bas:bas[k]=(v,cert);break
        v^=bas[k][0];cert^=bas[k][1]
    if j and j%2000==0:print('gamma3 correction columns',j,'rank',len(bas),flush=True)
target=int(json.loads((OUT/'d_cm_degree8_seed.json').read_text())['degree8_target'],16)
inside,_,rr=R['solve'](target,ue);assert inside and not rr
good,sol,rem=R['solve'](target,bas)
witness=None
if good:
    m=(1<<len(U))-1
    witness={'gamma3_beta_correction':hex(sol&m),'gamma3_A_correction':hex(sol>>len(U)),
     'exact_full_degree8_equation_checked':True,
     'retains_complete_H2_action':True}
summary={'actual_gamma3_module_dimension':len(U),'cusp_correction_rank':len(bas),
 'cusp_cokernel_dimension':len(U)-len(bas),'recorded_D31_degree8_target_in_gamma3':inside,
 'replacement_in_gamma3_alone_found':good,
 'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_gamma3.json').write_text(json.dumps({'summary':summary,'witness':witness,
 'basis_labels':labels,'remaining_target':hex(rem),
 'actual_S_inner_factor_degrees2_3':[hex(fullks[2]),hex(fullks[3])]},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
