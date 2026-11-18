#!/usr/bin/env python3
"""Independent actual-word reconstruction of the compact quaternion detector.

Work in progress until all assertions and the final payload are produced.
No historical binary/matrix certificate is imported.  Only NumPy is used.
"""
from collections import deque
from pathlib import Path
import hashlib, json
import numpy as np

P = 3

def red(w):
    s=[]
    for a in w:
        if s and s[-1]==-a: s.pop()
        else: s.append(a)
    return tuple(s)

def invword(w): return tuple(-a for a in w[::-1])
def mulword(*ws): return red(sum((tuple(w) for w in ws), ()))

def subst(w, images):
    return red(sum((images[a-1] if a>0 else invword(images[-a-1]) for a in w), ()))

def qmul(a,b):
    # labels 2*u+s: u=0,1,2,3 represents 1,i,j,k; sign=(-1)^s.
    u,s=divmod(a,2);v,t=divmod(b,2)
    if not u: z=v; e=0
    elif not v: z=u; e=0
    elif u==v: z=0; e=1
    else:
        z=6-u-v
        e=0 if (u,v) in ((1,2),(2,3),(3,1)) else 1
    return 2*z+(s+t+e)%2

QI=[next(b for b in range(8) if qmul(a,b)==0) for a in range(8)]
QGEN={1:2,2:4,-1:QI[2],-2:QI[4]}
assert all(qmul(qmul(a,b),c)==qmul(a,qmul(b,c)) for a in range(8) for b in range(8) for c in range(8))
generating_pairs=[]
for a in range(8):
    for b in range(8):
        subgroup={0}; old=-1
        while len(subgroup)!=old:
            old=len(subgroup)
            subgroup|={qmul(g,h) for g in tuple(subgroup) for h in (a,b)}
        if len(subgroup)==8:generating_pairs.append((a,b))
assert len(generating_pairs)==24

def qword(w):
    g=0
    for a in w:g=qmul(g,QGEN[a])
    return g

trans={0:()}; todo=deque([0])
while todo:
    g=todo.popleft()
    for a in (1,2,-1,-2):
        h=qmul(g,QGEN[a])
        if h not in trans:trans[h]=trans[g]+(a,);todo.append(h)
sch=[];edge={}
for g in range(8):
    for a in (1,2):
        h=qmul(g,QGEN[a]);w=mulword(trans[g],(a,),invword(trans[h]))
        if w:edge[g,a]=len(sch);sch.append(w)
        else:edge[g,a]=None
assert len(sch)==9
WEDGE=[(i,j) for i in range(9) for j in range(i+1,9)]

def wedge(v,w):return np.array([(int(v[i])*int(w[j])-int(v[j])*int(w[i]))%3 for i,j in WEDGE],dtype=np.int16)
def bracket45(v,w):return np.r_[np.zeros(9,dtype=np.int16),wedge(v[:9],w[:9])]

def logword(w):
    g=0;v=np.zeros(9,dtype=np.int16);z=np.zeros(36,dtype=np.int16)
    for a in w:
        h=qmul(g,QGEN[a]);j=edge[g,a] if a>0 else edge[h,-a]
        if j is not None:
            t=np.zeros(9,dtype=np.int16);t[j]=1 if a>0 else 2
            z=(z+2*wedge(v,t))%3;v=(v+t)%3
        g=h
    assert g==0
    return np.r_[v,z]

for j,w in enumerate(sch):
    a=np.zeros(45,dtype=np.int16);a[j]=1
    assert np.array_equal(logword(w),a)

def rref(rows,n=None):
    if len(rows)==0:return np.empty((0,n),dtype=np.int16),[]
    a=np.array(rows,dtype=np.int16).copy()%3;r=0;piv=[]
    for c in range(a.shape[1]):
        inds=np.flatnonzero(a[r:,c])
        if not len(inds):continue
        k=r+int(inds[0]);a[[r,k]]=a[[k,r]]
        if a[r,c]==2:a[r]=(2*a[r])%3
        for k in range(a.shape[0]):
            if k!=r and a[k,c]:a[k]=(a[k]-a[k,c]*a[r])%3
        piv.append(c);r+=1
        if r==a.shape[0]:break
    return a[:r],piv

def rank(rows,n=None):return len(rref(rows,n)[1])
def nullspace(a):
    r,p=rref(a);f=[j for j in range(a.shape[1]) if j not in p];out=[]
    for j in f:
        v=np.zeros(a.shape[1],dtype=np.int16);v[j]=1
        for k,c in enumerate(p):v[c]=-r[k,j]%3
        out.append(v)
    return np.array(out,dtype=np.int16)

def inverse(a):
    n=len(a);r,p=rref(np.c_[a,np.eye(n,dtype=np.int16)])
    assert p[:n]==list(range(n))
    assert np.array_equal(r[:,:n],np.eye(n,dtype=np.int16))
    return r[:,n:]

def modrows(v,rs,piv):
    v=v.copy()%3
    for row,c in zip(rs,piv):
        if v[c]:v=(v-v[c]*row)%3
    return v

def quotient_projection(rel,n):
    rr,pv=rref(rel,n);free=[i for i in range(n) if i not in pv]
    proj=np.column_stack([modrows(np.eye(n,dtype=np.int16)[j],rr,pv)[free] for j in range(n)])
    return proj,rr,pv

def auto45(images):
    a=np.column_stack([logword(subst(w,images)) for w in sch])
    return np.column_stack([a]+[bracket45(a[:,i],a[:,j])[:,None] for i,j in WEDGE])%3

AUTWORDS=[((1,),(2,1)),((1,-2),(2,)),((1,),(1,2,-1)),((2,1,-2),(2,))]
AUT45=[auto45(im) for im in AUTWORDS]
period=np.array([[sum(1 if a==g else -1 if a==-g else 0 for a in w)%3 for w in sch] for g in (1,2)],dtype=np.int16)
kt=nullspace(period);assert len(kt)==7
relations=[np.r_[np.zeros(9,dtype=np.int16),wedge(v,w)] for i,v in enumerate(kt) for w in kt[i+1:]]
assert rank(relations)==21
c=(1,2,-1,-2);boundary=logword(c+c)
relations.append(boundary)
while True:
    rr,_=rref(relations,45);old=len(rr);extra=[]
    for v in rr:
        extra.extend(m@v%3 for m in AUT45[2:])
        extra.extend(bracket45(v,np.eye(45,dtype=np.int16)[j]) for j in range(9))
    relations=list(rr)+extra
    if rank(relations)==old:break
proj,rr,pv=quotient_projection(relations,45)
assert len(rr)==31 and proj.shape==(14,45)
for a in AUT45:assert not np.any(proj@a@rr.T%3)
assert not np.any(proj@boundary%3)

# Choose six noncentral coordinates followed by eight derived coordinates.
central=[];centidx=[]
for j in range(9,45):
    v=proj[:,j]
    if rank(central+[v])>len(central):central.append(v);centidx.append(j)
assert len(central)==8
noncentral=[];nonidx=[]
for j in range(9):
    v=proj[:,j]
    if rank(central+noncentral+[v])>len(central)+len(noncentral):noncentral.append(v);nonidx.append(j)
assert len(noncentral)==6
basis=np.column_stack(noncentral+central);proj=inverse(basis)@proj%3
lift=np.eye(45,dtype=np.int16)[:,nonidx+centidx]
assert np.array_equal(proj@lift%3,np.eye(14,dtype=np.int16))
AUT=[proj@a@lift%3 for a in AUT45]
assert all(not np.any(a[:6,6:]) for a in AUT)
for a in AUT:assert rank(a)==14

def bracket(v,w):return proj@bracket45(lift@v%3,lift@w%3)%3
inner=[]
for i in range(6):
    v=np.eye(14,dtype=np.int16)[i]
    mat=np.column_stack([bracket(v,np.eye(14,dtype=np.int16)[j])[6:] for j in range(6)])
    inner.append(mat.ravel())
ir,ip=rref(inner,48);assert len(ir)==6

PER=[np.array([[1,1],[0,1]],dtype=np.int16),np.array([[1,0],[-1,1]],dtype=np.int16),np.eye(2,dtype=np.int16),np.eye(2,dtype=np.int16)]
PER=[p%12 for p in PER]
def basekey(a,p):return a[:6,:6].astype('u1').tobytes()+p.astype('u1').tobytes()
E14=np.eye(14,dtype=np.int16);E6=np.eye(6,dtype=np.int16);E2=np.eye(2,dtype=np.int16)
reps=[E14];pers=[E2];ainvs=[E6];parents=[None];lookup={basekey(E14,E2):0};adj=[]
q=0
while q<len(reps):
    edges=[]
    for j,(a,p) in enumerate(zip(AUT,PER)):
        nm=reps[q]@a%3;npd=pers[q]@p%12;k=basekey(nm,npd)
        if k not in lookup:
            lookup[k]=len(reps);reps.append(nm);pers.append(npd);ainvs.append(inverse(a[:6,:6])@ainvs[q]%3);parents.append((q,j))
        dest=lookup[k];edges.append(dest)
        assert np.array_equal(nm[6:,6:],reps[dest][6:,6:])
    adj.append(edges);q+=1
assert len(reps)==9216
kr=np.empty((0,48),dtype=np.int16);kp=[]
for q in range(len(reps)):
    for j,a in enumerate(AUT):
        nm=reps[q]@a%3;dest=adj[q][j]
        d=(nm[6:,:6]-reps[dest][6:,:6])@ainvs[dest]%3
        v=modrows(d.ravel(),ir,ip);v=modrows(v,kr,kp)
        if np.any(v):kr,kp=rref(list(kr)+[v],48)
assert len(kr)==4
for a in AUT:
    ai=inverse(a[:6,:6]);bc=a[6:,6:]
    for row in kr:
        v=modrows((bc@row.reshape(8,6)@ai%3).ravel(),ir,ip)
        assert not np.any(modrows(v,kr,kp))

# Actual inner deck image, modulo the six inner-derivation coordinates.
deck=[E14];dl={E14[:6,:6].astype('u1').tobytes():0};dq=0
while dq<len(deck):
    for a in AUT[2:]:
        nm=deck[dq]@a%3;k=nm[:6,:6].astype('u1').tobytes()
        if k not in dl:dl[k]=len(deck);deck.append(nm)
    dq+=1
assert len(deck)==8
deckinv=[inverse(d) for d in deck]
byperiod={}
for j,p in enumerate(pers):byperiod.setdefault(tuple(map(int,p.ravel())),j)
assert len(byperiod)==1152
CM=AUT[0]@AUT[1]%3;CMINV=inverse(CM);CMPer=PER[0]@PER[1]%12

def powmat(a,n,mod):
    out=np.eye(len(a),dtype=np.int16)
    for _ in range(n):out=out@a%mod
    return out

def sourceword(j):
    w=[]
    while parents[j] is not None:j,a=parents[j];w.append(a)
    return w[::-1]

census=[]
for pk,idx in sorted(byperiod.items()):
    p=np.array(pk,dtype=np.int16).reshape(2,2)
    if not np.array_equal(p@CMPer%12,CMPer@p%12):continue
    i=next(i for i in range(6) if np.array_equal(p%4,powmat(CMPer, i,4)))
    j=next(j for j in range(6) if np.array_equal(p%3,powmat(CMPer, j,3)))
    count=0
    for digits in np.ndindex(*(3,)*4):
        cv=np.array(digits,dtype=np.int16)@kr%3
        k=E14.copy();k[6:,:6]=cv.reshape(8,6)
        g=k@reps[idx]%3
        comm=g@CM@inverse(g)%3@CMINV%3
        dkey=comm[:6,:6].astype('u1').tobytes()
        assert dkey in dl
        residue=deckinv[dl[dkey]]@comm%3
        assert np.array_equal(residue[:6,:6],E6) and np.array_equal(residue[6:,6:],np.eye(8,dtype=np.int16))
        if not np.any(modrows(residue[6:,:6].ravel(),ir,ip)):count+=1
    assert count==(9 if (i-j)%2==0 else 0),(pk,i,j,count)
    census.append({'period':list(pk),'i_mod4':i,'j_mod3':j,'lifts':count,'word':sourceword(idx)})
assert len(census)==36 and sum(x['lifts']>0 for x in census)==18

# Independent ordered-pole surface words; this does not assume branch covariance.
def ored(w):
    s=[]
    for a in w:
        if s and s[-1]==a:s.pop()
        else:s.append(a)
    return tuple(s)

def om(*ws):return ored(sum((tuple(w) for w in ws),()))
u=(2,1);v=(3,1);z=(4,1)
oa=u;ob=om(u[::-1],v)
oc=om(u[::-1],v,u,v[::-1],z,v[::-1],u)
def rewrite_surface(w):
    assert len(w)%2==0
    uvz=tuple((1 if pos%2==0 else -1)*(t-1) for pos,t in enumerate(w) if t!=1)
    return subst(uvz,((1,),(1,2),(1,2,-1,-2,3,2)))
assert [rewrite_surface(w) for w in (oa,ob,oc)]==[(1,),(2,),(3,)]
surface_aut=[]
for j in (1,2,3):
    im=[(t,) for t in range(1,5)];im[j-1]=(j,j+1,j);im[j]=(j,)
    surface_aut.append(tuple(rewrite_surface(ored(sum((im[t-1] for t in w),()))) for w in (oa,ob,oc)))
def compose_aut(a,b):return tuple(subst(w,a) for w in b)
assert compose_aut(surface_aut[0],compose_aut(surface_aut[1],surface_aut[0]))==compose_aut(surface_aut[1],compose_aut(surface_aut[0],surface_aut[1]))
assert compose_aut(surface_aut[1],compose_aut(surface_aut[2],surface_aut[1]))==compose_aut(surface_aut[2],compose_aut(surface_aut[1],surface_aut[2]))
assert compose_aut(surface_aut[0],surface_aut[2])==compose_aut(surface_aut[2],surface_aut[0])
surface_period=[]
for j,a in enumerate(surface_aut):
    cap=tuple(red(tuple(t for t in w if abs(t)!=3)) for w in a)
    expect=AUTWORDS[0] if j in (0,2) else AUTWORDS[1]
    assert cap==expect+((),)
    mat=np.array([[sum(1 if t==g else -1 if t==-g else 0 for t in w) for w in a] for g in (1,2,3)],dtype=np.int16)
    surface_period.append(mat)
expected=[np.array([[1,1,0],[0,1,0],[0,0,1]]),np.array([[1,0,0],[-1,1,0],[0,0,1]]),np.array([[1,1,0],[0,1,0],[0,-1,1]])]
assert all(np.array_equal(a,b) for a,b in zip(surface_period,expected))
abc=compose_aut(surface_aut[0],compose_aut(surface_aut[1],surface_aut[2]));ft=((1,),(2,),(3,))
for _ in range(4):ft=compose_aut(abc,ft)
boundary2=rewrite_surface((1,2,3,4))
assert ft==tuple(mulword(boundary2,(g,),invword(boundary2)) for g in (1,2,3))
def inv_int_unimod(a):
    assert a.shape==(3,3)
    cof=np.empty((3,3),dtype=np.int16)
    for i in range(3):
        for j in range(3):
            m=a[np.ix_([k for k in range(3) if k!=i],[k for k in range(3) if k!=j])]
            cof[i,j]=(-1)**(i+j)*(int(m[0,0])*int(m[1,1])-int(m[0,1])*int(m[1,0]))
    det=sum(int(a[0,j])*int(cof[0,j]) for j in range(3));assert det in (-1,1)
    out=det*cof.T
    assert np.array_equal(a@out,np.eye(3,dtype=np.int16))
    return out
ma,mb,mc=surface_period
xi1=mc@inv_int_unimod(ma)
xi2=ma@mb@ma@inv_int_unimod(mc)@inv_int_unimod(mb)@inv_int_unimod(ma)
assert np.array_equal(xi1,np.array([[1,0,0],[0,1,0],[0,-1,1]]))
assert np.array_equal(xi2,np.array([[1,0,0],[0,1,0],[1,0,1]]))

payload={
 'status':'PASS',
 'Q8_generating_pairs':len(generating_pairs),
 'schreier_words':[list(w) for w in sch],
 'N8_rank':9,'T_period_kernel_rank':7,'T_commutator_relation_rank':21,
 'full_relation_rank':31,'compact_lie_dimension':14,'abelian_dimension':6,'derived_dimension':8,
 'inner_derivation_rank':6,'linear_base_order':len(reps),'schreier_rows':4*len(reps),
 'outer_central_kernel_rank':len(kr),'inner_deck_order':len(deck),
 'detected_outer_order':len(reps)*3**len(kr)//len(deck),
 'compact_surface_order':32*3**14,'compact_surface_abelianization_order':12**2,
 'centralizer_residues':census,'centralizer_order':sum(x['lifts'] for x in census),
 'ordered_pole_surface_actions':[[list(w) for w in a] for a in surface_aut],
 'ordered_pole_period_matrices':[a.tolist() for a in surface_period],
 'ordered_pole_quotient_order':12*32*3**14,
 'ordered_pole_outer_image_order':144*(len(reps)*3**len(kr)//len(deck)),
 'projection_14_by_45':proj.tolist(),'lift_45_by_14':lift.tolist(),
 'actual_automorphisms_14':[a.tolist() for a in AUT],
 'inner_derivations_rref':ir.tolist(),'outer_kernel_rref':kr.tolist(),
 'relation_rref_31_by_45':rr.tolist(),
}
raw=json.dumps(payload,sort_keys=True,separators=(',',':')).encode()
payload['sha256']=hashlib.sha256(raw).hexdigest()
out=Path(__file__).with_suffix('.json');out.write_text(json.dumps(payload,indent=2)+'\n')
print(json.dumps({k:v for k,v in payload.items() if k not in {'schreier_words','centralizer_residues','projection_14_by_45','lift_45_by_14','actual_automorphisms_14','inner_derivations_rref','outer_kernel_rref','relation_rref_31_by_45','ordered_pole_surface_actions','ordered_pole_period_matrices'}},indent=2))
