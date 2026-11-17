"""All 364 pointed cyclic-three covers of W^4=X^3 Z-X Z^3 over F_(5^8).

Construct every J[3] class from the three elliptic quotients.  Compute Cartier
on the two two-dimensional eigenspaces using explicit Riemann--Roch conditions.
All polynomial and field operations are exact.  No point census is used.
Run with PYTHONPATH=runtime_deps python code/criterion_quartic_all3.py.
"""
from pathlib import Path
from itertools import product
import json, time, argparse
from flint import fq_default_ctx, fq_default_poly_ctx

ap=argparse.ArgumentParser();ap.add_argument('--limit',type=int,default=0)
ap.add_argument('--resume',action='store_true');args=ap.parse_args()
start=time.time();p=5;nfield=8
k=fq_default_ctx(p,nfield,'z');R=fq_default_poly_ctx(k);x=R.gen()
O=k(0);I=k(1);f0=x**3-x
def enc(a):return sum(int(c)*p**j for j,c in enumerate(a.to_list()))
def ep(a):return [enc(c) for c in a.coeffs()]
def em(A):return [[enc(a) for a in row] for row in A]
def eye(n):return [[I if i==j else O for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum((a*b for a,b in zip(row,col)),O) for col in zip(*B)] for row in A]
def inv(A):
    n=len(A);B=[r[:]+s for r,s in zip(A,eye(n))]
    for j in range(n):
        h=next(i for i in range(j,n) if B[i][j]!=0)
        B[j],B[h]=B[h],B[j];q=B[j][j];B[j]=[a/q for a in B[j]]
        for i in range(n):
            if i!=j:
                q=B[i][j];B[i]=[a-q*b for a,b in zip(B[i],B[j])]
    return [r[n:] for r in B]
def det(A):
    A=[r[:] for r in A];v=I;n=len(A)
    for j in range(n):
        h=next((i for i in range(j,n) if A[i][j]!=0),None)
        if h is None:return O
        if h!=j:A[j],A[h]=A[h],A[j];v=-v
        u=A[j][j];v*=u
        for i in range(j+1,n):
            z=A[i][j]/u
            for h in range(j,n):A[i][h]-=z*A[j][h]
    return v
def cp4(A):
    B=eye(4);tr=[]
    for j in range(4):B=mm(B,A);tr.append(sum((B[i][i] for i in range(4)),O))
    c=[I]
    for j in range(1,5):c.append(-sum((c[j-i]*tr[i-1] for i in range(1,j+1)),O)/k(j))
    ans=R(list(reversed(c)))
    assert ans(I)==det([[I-A[i][j] if i==j else -A[i][j] for j in range(4)] for i in range(4)])
    return ans
def nullspace(A,n):
    A=[row[:] for row in A];piv=[];jrow=0
    for j in range(n):
        s=next((i for i in range(jrow,len(A)) if A[i][j]!=0),None)
        if s is None:continue
        A[jrow],A[s]=A[s],A[jrow];u=A[jrow][j];A[jrow]=[a/u for a in A[jrow]]
        for i in range(len(A)):
            if i!=jrow:
                u=A[i][j];A[i]=[a-u*b for a,b in zip(A[i],A[jrow])]
        piv.append(j);jrow+=1
        if jrow==len(A):break
    basis=[]
    for j in range(n):
        if j not in piv:
            v=[O]*n;v[j]=I
            for i,h in enumerate(piv):v[h]=-A[i][j]
            basis.append(v)
    for v in basis:assert all(sum((a*b for a,b in zip(row,v)),O)==0 for row in A)
    return basis

# Arithmetic in k[x,w]/(w^4-x^3+x); every element is a length-four tuple.
K0=[R(0)]*4;K1=[R(1),R(0),R(0),R(0)]
W=[R(0),R(1),R(0),R(0)]
def ka(A,B):return [a+b for a,b in zip(A,B)]
def ks(A,B):return [a-b for a,b in zip(A,B)]
def km(A,B):
    C=[R(0) for _ in range(4)]
    for i in range(4):
        for j in range(4):
            if A[i]==0 or B[j]==0:continue
            u=A[i]*B[j]
            if i+j>=4:u*=f0
            C[(i+j)%4]+=u
    return C
def kp(A,n):
    B=K1
    while n:
        if n&1:B=km(B,A)
        A=km(A,A);n//=2
    return B
def sc(A,c):return [a*c for a in A]
def klin(v):return [v[0]*x+v[2],R(v[1]),R(0),R(0)]
def normadj(v):
    a=v[0]*x+v[2];b=v[1]
    adj=[a**3,-a*a*b,a*b*b,R(-b**3)]
    nn=a**4-b**4*f0
    assert km(klin(v),adj)==[nn,R(0),R(0),R(0)]
    return nn,adj

# Three elliptic quotient maps, obtained by permuting Fermat coordinates.
eta=next(a for a,m in (x**4+1).roots())
assert eta**4==-I
u=[I,O,k(-2)];v=[O,I,O];t=[eta,O,2*eta]
maps=[]
for uu,vv,tt in [(u,v,t),(v,u,t),(u,t,v)]:
    rr=[a/eta for a in tt]
    A=[[(a+b)/2 for a,b in zip(uu,rr)],vv[:],[(b-a)/4 for a,b in zip(uu,rr)]]
    Xi,Wi,Zi=map(klin,A)
    assert ks(kp(Wi,4),ks(km(kp(Xi,3),Zi),km(Xi,kp(Zi,3))))==K0
    maps.append({'A':A,'inverse':inv(A),'X':Xi,'W':Wi,'Z':Zi})
assert maps[0]['A']==eye(3)

def ecadd(P,Q):
    if P is None:return Q
    if Q is None:return P
    a,b=P;c,d=Q
    if a==c:
        if b==-d:return None
        m=(3*a*a-1)/(2*b)
    else:m=(d-b)/(c-a)
    z=m*m-a-c;return z,m*(a-z)-b
tors=[None]
for a,m in sorted((3*x**4-6*x*x-1).roots(),key=lambda z:enc(z[0])):
    b=(a**3-a).sqrt();tors.extend([(a,b),(a,-b)])
assert len(tors)==9
for T in tors[1:]:assert ecadd(ecadd(T,T),T) is None
neg=[0]+[next(j for j,S in enumerate(tors) if S==(T[0],-T[1])) for T in tors[1:]]

def monomials(d):return [(a,b,d-a-b) for a in range(d+1) for b in range(d-a+1) if b<4]
def monoval(m,coords):
    ans=R(1)
    for a,e in zip(coords,m):ans*=a**e
    return ans
def monoder(m,coords,dcoords):
    ans=R(0)
    for j,e in enumerate(m):
        if not e:continue
        v=R(e*dcoords[j])
        for h,ee in enumerate(m):v*=coords[h]**(ee-(h==j))
        ans+=v
    return ans
cache={}
def constraints(i,ti,d):
    key=(i,ti,d)
    if key in cache:return cache[key]
    a,b=tors[ti];V=maps[i]['inverse'];mons=monomials(d)
    coords=[R([row[0]*a+row[2],row[1]]) for row in V]
    dx=[row[0] for row in V];eq=x*x-b
    derivw=(3*a*a-1)/(4*b*b)*x
    e0=[];e1=[];p0=[];p1=[]
    for mon in mons:
        g=monoval(mon,coords);h=monoder(mon,coords,dx)+g.derivative()*derivw
        g=g%eq;h=h%eq;e0.append([g[0],g[1]]);e1.append([h[0],h[1]])
        pc=[R([row[0],row[1]]) for row in V];gg=monoval(mon,pc)
        p0.append(gg[0]);p1.append(gg[1])
    out=([list(r) for r in zip(*e0)],[list(r) for r in zip(*e1)],[p0,p1])
    cache[key]=out;return out
def rr_basis(tup,tchar):
    active=[(i,j) for i,j in enumerate(tup) if j];d=len(active)+1;A=[]
    for i,j in active:
        vals,ders,poles=constraints(i,j,d);A.extend(vals);A.extend(poles if tchar==1 else ders)
    mons=monomials(d);B=nullspace(A,len(mons));assert len(B)==2,(tup,tchar,d,len(B))
    return d,mons,B
def tok(v,mons):
    out=[R(0) for _ in range(4)]
    for c,(a,b,z) in zip(v,mons):out[b]+=c*x**a
    return out
def fromk(G,mons,d):
    ans=[G[b][a] for a,b,z in mons]
    assert tok(ans,mons)==G,('degree escape',d,[a.degree() for a in G])
    return ans
def coordinates(v,B):
    ids=next((i,j) for i in range(len(v)) for j in range(i+1,len(v)) if B[0][i]*B[1][j]-B[0][j]*B[1][i]!=0)
    i,j=ids;dd=B[0][i]*B[1][j]-B[0][j]*B[1][i]
    a=(v[i]*B[1][j]-v[j]*B[1][i])/dd;b=(B[0][i]*v[j]-B[0][j]*v[i])/dd
    assert all(z==a*u+b*w for z,u,w in zip(v,B[0],B[1]))
    return [a,b]

def cover(tup):
    active=[(i,j) for i,j in enumerate(tup) if j]
    QQ=K1;AA=K1;ZZ=K1;NN=R(1);lead=I
    for i,j in active:
        a,b=tors[j];slope=(3*a*a-1)/(2*b);intercept=b-slope*a
        mp=maps[i];Q=ks(ks(kp(mp['W'],2),sc(km(mp['X'],mp['Z']),slope)),sc(kp(mp['Z'],2),intercept))
        nn,adj=normadj(mp['A'][2]);QQ=km(QQ,Q);AA=km(AA,adj);ZZ=km(ZZ,mp['Z']);NN*=nn
        if i:
            xx,ww,zz=(row[0] for row in mp['A'])
            z=(ww*ww-slope*xx*zz-intercept*zz*zz)/(zz*zz)
            assert z!=0;lead*=z
    bases={t:rr_basis(tup,t) for t in [1,2]};M=[[O for _ in range(4)] for _ in range(4)]
    for tchar in [1,2]:
        target=3-tchar;power=(5*target-tchar)//3
        d,mons,B=bases[tchar];d2,mons2,B2=bases[target]
        common=NN**(2*power+1)*f0*lead**power
        factor=km(kp(QQ,power),kp(AA,2*power+1))
        for j,v in enumerate(B):
            numerator=km(km(tok(v,mons),factor),W)
            cc=[]
            for i,ai in enumerate(numerator):
                bb=common*f0**i;H=ai*bb**4
                C=R([H[5*h+4].pth_root() for h in range(max(0,(H.degree()-4)//5+1))])
                cc.append(C*f0**(3-i))
            out=km(km(cc,kp(W,3)),ZZ);den=common*f0**3
            quot=[]
            for h in out:
                z,rem=h.divmod(den);assert rem==0,('Cartier denominator',tup,tchar,j)
                quot.append(z)
            coeff=coordinates(fromk(quot,mons2,d2),B2)
            for h,c in enumerate(coeff):M[2*(target-1)+h][2*(tchar-1)+j]=c
    A=eye(4)
    for j in range(nfield):A=mm(M,[[a.pth_root() for a in row] for row in A])
    cp=cp4(A);val=cp(I)
    assert all(a**5==a for a in cp.coeffs())
    return {'torsion_indices':tup,'active':len(active),'normalization':enc(lead),
            'basis_monomials':bases[1][1],'basis_char1':em(bases[1][2]),'basis_char2':em(bases[2][2]),
            'Cartier_matrix':em(M),'Cartier_eighth_power':em(A),
            'new_characteristic_polynomial_mod5':ep(cp),'relative_class_number_mod5':enc(val),
            'unit':val!=0}

tuples=[t for t in product(range(9),repeat=3) if t!=(0,0,0) and t<tuple(neg[j] for j in t)]
assert len(tuples)==364
if args.limit:tuples=tuples[:args.limit]
recs=[];outpath=Path(__file__).with_suffix('.json')
if args.resume and outpath.exists():recs=json.loads(outpath.read_text())['covers']
done={tuple(r['torsion_indices']) for r in recs}
def save():
    out={'field':{'p':5,'degree':8,'modulus':list(map(int,k.modulus()))},'eta':enc(eta),
         'curve':'W^4=X^3 Z-X Z^3','point':[1,0,0],'ell':3,'constant_degree':8,
         'torsion':[None]+[[enc(a) for a in P] for P in tors[1:]],
         'quotient_maps':[em(a['A']) for a in maps],
         'covers':recs,'complete':len(recs)==364,'seconds':time.time()-start}
    outpath.write_text(json.dumps(out,indent=2)+'\n')
for ind,tup in enumerate(tuples):
    if tup in done:continue
    rec=cover(tup);recs.append(rec)
    if rec['unit'] or len(recs)%20==0 or len(recs)<=5:
        print(json.dumps({'n':len(recs),'tuple':tup,'cp':rec['new_characteristic_polynomial_mod5'],
                          'unit':rec['unit'],'seconds':round(time.time()-start,3)}),flush=True)
    if len(recs)%20==0:save()
save();print('complete',len(recs),'good',sum(r['unit'] for r in recs),'seconds',time.time()-start,flush=True)
