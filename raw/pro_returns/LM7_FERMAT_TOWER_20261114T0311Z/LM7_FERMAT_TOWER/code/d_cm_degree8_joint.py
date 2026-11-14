#!/usr/bin/env python3
"""Exact simultaneous degree-eight and N-class-two correction.

The correcting group is abelian in BOTH targets. Its order-four generators
are the 4708 high C1 words; its order-two generators are the 45 twice-low
C1 words and the 9105-dimensional gamma3(N) image. Thus every equation
below retains the actual group law, including the modulo-four Bockstein.
"""
from pathlib import Path
from contextlib import redirect_stdout
import io,runpy,json,time,gc
import numpy as np
import d_cm_degree8_magnus as G
OUT=Path(__file__).resolve().parent;started=time.time()
with redirect_stdout(io.StringIO()):X=runpy.run_path(str(OUT/'d_cm_degree8_gamma3.py'))
R=X['R'];fastcomm=X['fastcomm'];pack=X['pack'];gbas=X['bas'];ud=len(X['U'])

# Extend the actual cusp image basis to the whole gamma3 module. The
# resulting 124 functionals are then explicitly extended to all tensor
# coordinates by the same triangular elimination.
eb={k:(v[0],0) for k,v in gbas.items()};od=0
for v in X['U']:
    tag=0
    while v:
        k=v.bit_length()-1
        if k not in eb:eb[k]=(v,tag^(1<<od));od+=1;break
        vv,tt=eb[k];v^=vv;tag^=tt
assert len(eb)==ud and od==124
rawduals=[0]*od
for k,(v,tag) in sorted(eb.items()):
    for j in range(od):
        if ((tag>>j)&1)^((rawduals[j]&v).bit_count()%2):rawduals[j]^=1<<k
assert all(all(not ((e&v[0]).bit_count()%2) for v in gbas.values()) for e in rawduals)
def obstruction(v):return sum(((e&v).bit_count()%2)<<j for j,e in enumerate(rawduals))
for key in ('U','US','UT','columns','ue'):X.pop(key,None)
del eb;gc.collect()
print('Exact gamma3 quotient functionals:',od,flush=True)

d=97;cdim=4753;pairs=[(i,j) for i in range(d) for j in range(i,d)]
ii=np.array([i for i,j in pairs]);jj=np.array([j for i,j in pairs]);diag=ii==jj
one,qs,qr,qr2,qm,ix=(R[k] for k in ('one','qs','qr','qr2','qm','ixQ'))
chord={j:i for i,j in enumerate(R['chN'])};Nwords=R['Nwords']
def inverse(w):return [0 if a==0 else 3-a for a in reversed(w)]
def evaluate(word,startq=one,second=True):
    q=startq;v=np.zeros(d,dtype=np.int64);w=np.zeros((d,d),dtype=np.int64)
    def append(e,sign):
        i=chord.get(e)
        if i is None:return
        if second:
            w[:,i]=(w[:,i]+sign*v)%4
            if sign<0:w[i,i]=(w[i,i]+1)%4
        v[i]=(v[i]+sign)%4
    for a in word:
        if a==0:q=qm(q,qs)
        else:
            qq=qm(q,qr if a==1 else qr2);append(ix[q],1);append(ix[qq],-1);q=qq
    return q,v,w
def bits(v):return int.from_bytes(np.packbits(np.asarray(v%2,dtype=np.uint8),bitorder='little').tobytes(),'little')
def raw(p):return p[5]<<86016 ^ p[6]<<81920 ^ p[7]<<65536 ^p[8]
def read(word,n=6):
    q,w=R['collapse'](word);assert q==R['e'];P=R['poly'](w,n)
    return (0,)+tuple(R['bitpoly'](P[i]) if i<=n else 0 for i in range(1,9))
J=json.loads((OUT/'d_cm_quadratic_search.json').read_text())['witness']
def nword(mask):
    ans=[]
    while mask:
        b=mask&-mask;ans+=Nwords[b.bit_length()-1];mask^=b
    return ans
qb=R['D']['canon'](tuple(J['beta']))
beta=nword(int(J['homology_beta_cycles'],16))+R['reps'][qb]
fixed=json.loads((OUT/'d_cm_class2_two.json').read_text())['s_centralizer_basis']
right=int(J['beta_right_s_centralizer_coefficients'],16)
for j,v in enumerate(fixed):
    if (right>>j)&1:beta+=nword(int(v,16))
sw=beta+[0]+inverse(beta);tw=[0,1]

H=json.loads((OUT/'d_cm_degree8_high.json').read_text())
newwords=H['actual_Nielsen_basis_B_words']
highpairs=[tuple(p) for p in H['high_C1_pairs']]
assert len(newwords)==97 and len(highpairs)==4708
def data(words,gword,qexpected):
    q,vg,_=evaluate(gword,second=False);assert q==qexpected
    vcols=[];Ws=[];polys=[]
    for w in words:
        q,v,z=evaluate(w,startq=qexpected);assert q==qexpected
        z=(z+np.outer(vg,v)-np.outer(v,vg))%4
        vcols.append(v);Ws.append(z)
        polys.append(read(gword+w+inverse(gword)))
    return np.stack(vcols,axis=1),np.stack(Ws),polys
ND=data(newwords,[],one);NS=data(newwords,sw,qs);NT=data(newwords,tw,qm(qs,qr))
def c1(i,j,data0):
    M,W,polys=data0
    if i==j:
        z=(2*W[i]+np.outer(M[:,i],M[:,i]))%4
        p=G.mul(polys[i],polys[i])
    else:
        z=(np.outer(M[:,i],M[:,j])-np.outer(M[:,j],M[:,i]))%4
        p=fastcomm(polys[i],polys[j])
    assert G.mindeg(p)>=5
    return z[ii,jj],raw(p)

F=np.zeros((9416,cdim),dtype=np.int16);lowraw=[0]*9416;lowobs=[0]*9416
for k,(i,j) in enumerate(highpairs):
    vc,vp=c1(i,j,ND);sc,sp=c1(i,j,NS);tc,tp=c1(i,j,NT)
    F[k]=(vc-sc)%4;F[4708+k]=(sc-tc)%4
    lowraw[k]=vp^sp;lowraw[4708+k]=sp^tp
    lowobs[k]=obstruction(lowraw[k]);lowobs[4708+k]=obstruction(lowraw[4708+k])
    if k and k%1000==0:print('High C1 exact columns',k,flush=True)

# All upper class-two corrections are twice the original C1 basis.
# Their tensor images are the squares of their degree-four terms.
OD=data(Nwords,[],one);OS=data(Nwords,sw,qs);OT=data(Nwords,tw,qm(qs,qr))
def uppercol(i,j,data0):
    M,W,polys=data0
    if i==j:
        z=(2*W[i]+np.outer(M[:,i],M[:,i]))%4
        p4=G.mp(polys[i][2],2,polys[i][2],2)
    else:
        z=(np.outer(M[:,i],M[:,j])-np.outer(M[:,j],M[:,i]))%4
        p4=G.mp(polys[i][2],2,polys[j][2],2)^G.mp(polys[j][2],2,polys[i][2],2)
    return bits(z[ii,jj]),G.mp(p4,4,p4,4)
upperH=[];upperraw=[];secondH=[];secondraw=[]
for k,(i,j) in enumerate(pairs):
    vc,vp=uppercol(i,j,OD);sc,sp=uppercol(i,j,OS);tc,tp=uppercol(i,j,OT)
    upperH.append(vc^sc);upperraw.append(vp^sp)
    secondH.append(sc^tc);secondraw.append(sp^tp)
upperH+=secondH;upperraw+=secondraw
q,v144,w144=evaluate([0,1]*144);assert q==one and not np.any(v144) and not np.any(w144%2)
upperH.append(bits(w144[ii,jj]//2))
upperraw.append(int(json.loads((OUT/'d_cm_degree8_seed.json').read_text())['t48_degree8_column'],16))
uppercols=[h|(obstruction(p)<<cdim) for h,p in zip(upperH,upperraw)]
ub=R['echelon'](uppercols);rows=cdim+od
jointduals=[]
for j in range(rows):
    if j in ub:continue
    e=1<<j
    for k in sorted(ub):
        if (e&ub[k][0]).bit_count()%2:e^=1<<k
    assert all(not ((e&v[0]).bit_count()%2) for v in ub.values())
    jointduals.append(e)
print('Joint upper image rank:',len(ub),'cokernel:',len(jointduals),flush=True)

# Exact modulo-four functionals on the order-four lower variables.
# Each H-part is even because doubling the corresponding high word has
# zero tensor image. This is the precise Bockstein divisibility check.
mask=(1<<cdim)-1
fp=[bits(v) for v in F];fs=[bits(v//2) for v in F]
ext=[]
for j,(p,b) in enumerate(zip(fp,fs)):
    ob=0
    for k,e in enumerate(jointduals):
        eh=e&mask;eu=e>>cdim
        val=((eh&p).bit_count()+2*(eh&b).bit_count())%4
        assert val%2==0
        bit=(val//2)^((eu&lowobs[j]).bit_count()%2)
        ob|=bit<<k
    ext.append(p|(ob<<cdim))
target=int(json.loads((OUT/'d_cm_degree8_seed.json').read_text())['degree8_target'],16)
targetob=obstruction(target)
goal=sum((((e>>cdim)&targetob).bit_count()%2)<<k for k,e in enumerate(jointduals))<<cdim
lb=R['echelon'](ext);good,z,rem=R['solve'](goal,lb)
print('Joint lower rank:',len(lb),'solved:',good,flush=True)
witness=None
if good:
    selected=[j for j in range(9416) if (z>>j)&1]
    hv=(-np.sum(F[selected],axis=0,dtype=np.int64))%4
    assert not np.any(hv%2)
    pv=target
    for j in selected:pv^=lowraw[j]
    ug=bits(hv//2)|(obstruction(pv)<<cdim)
    ok,up,rr=R['solve'](ug,ub);assert ok and not rr
    hs=bits(hv//2)
    for j in range(len(uppercols)):
        if (up>>j)&1:pv^=upperraw[j];hs^=upperH[j]
    assert not hs and not obstruction(pv)
    ok,us,rr=R['solve'](pv,gbas);assert ok and not rr
    # R.solve's exact image-basis certificate proves equality;
    # the next program evaluates the complete resulting group words.
    witness={'high_C1_beta_change':hex(z&((1<<4708)-1)),
     'high_C1_A_change':hex(z>>4708),
     'upper_old_C1_beta_change':hex(up&mask),
     'upper_old_C1_A_change':hex((up>>cdim)&mask),
     'multiplier144_change':up>>(2*cdim),
     'gamma3_beta_change':hex(us&((1<<ud)-1)),
     'gamma3_A_change':hex(us>>ud),
     'lambda':1+144*(up>>(2*cdim)),
     'exact_Z4_and_tensor_equations_solved':True}
summary={'gamma3_dimension':ud,'gamma3_cusp_rank':len(gbas),'gamma3_cokernel':od,
 'order4_correction_generators':4708,'order2_correction_generators':9150,
 'joint_upper_variables':len(uppercols),'joint_upper_rank':len(ub),
 'joint_upper_cokernel':len(jointduals),'joint_lower_variables':len(ext),
 'joint_lower_rank':len(lb),'joint_degree8_class2_seed_found':good,
 'remaining_target':hex(rem),'elapsed_seconds':round(time.time()-started,3)}
(OUT/'d_cm_degree8_joint.json').write_text(json.dumps({'summary':summary,'witness':witness,
 'joint_upper_annihilators':[hex(e) for e in jointduals]},indent=2)+'\n')
print(json.dumps(summary,indent=2),flush=True)
