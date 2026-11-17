"""Independent all-character check using the differential Cartier identity.

No producer code is imported. Instead of Cartier coefficient extraction,
verify (C(v dx)/dx)^5 = - (d/dx)^4 v in the quartic function field.
Also verify divisor conditions for every supplied basis, the Kummer
normalization at the specified point, and direct Frobenius products.
"""
from pathlib import Path
from itertools import product
from collections import Counter
from hashlib import sha256
import json,time
from flint import fq_default_ctx,fq_default_poly_ctx,fmpz_mod_poly_ctx

start=time.time();root=Path(__file__).resolve().parent
raw=(root/'criterion_quartic_all3.json').read_bytes();data=json.loads(raw)
assert data['complete'] and len(data['covers'])==364
P=fmpz_mod_poly_ctx(5);mod=P(data['field']['modulus']);z=P.gen()
assert mod.degree()==8 and z.pow_mod(5**8,mod)==z
assert (z.pow_mod(5**4,mod)-z).gcd(mod)==1
k=fq_default_ctx(modulus=mod,var='z',fq_type='FQ_NMOD');R=fq_default_poly_ctx(k)
x=R.gen();one=k(1);zero=k(0);f=x**3-x
def dec(a):
    assert isinstance(a,int) and 0<=a<5**8
    return k([(a//5**j)%5 for j in range(8)])
def enc(a):return sum(int(c)*5**j for j,c in enumerate(a.to_list()))
def mat(A):return [[dec(a) for a in row] for row in A]
def eye(n):return [[one if i==j else zero for j in range(n)] for i in range(n)]
def mm(A,B):return [[sum((A[i][h]*B[h][j] for h in range(len(B))),zero) for j in range(len(B[0]))] for i in range(len(A))]
def inv(A):
    n=len(A);B=[row[:]+e for row,e in zip(A,eye(n))]
    for j in range(n):
        i=next(i for i in range(j,n) if B[i][j]!=0);B[j],B[i]=B[i],B[j]
        u=B[j][j];B[j]=[a/u for a in B[j]]
        for i in range(n):
            if i!=j:
                u=B[i][j];B[i]=[a-u*b for a,b in zip(B[i],B[j])]
    out=[r[n:] for r in B];assert mm(A,out)==eye(n);return out
def charpoly(A):
    n=len(A)
    if n==0:return R(1)
    B=[r[1:] for r in A[1:]];cp=charpoly(B);ans=(x-A[0][0])*cp
    if n==1:return ans
    row=A[0][1:];col=[A[i][0] for i in range(1,n)];mom=[]
    for j in range(n-1):
        mom.append(sum((a*b for a,b in zip(row,col)),zero))
        col=[sum((a*b for a,b in zip(rr,col)),zero) for rr in B]
    for j in range(n-1):ans-=sum((cp[n-1-h]*mom[j-h] for h in range(j+1)),zero)*x**(n-2-j)
    return ans

# Ring multiplication is general convolution followed by the relation w^4=f.
def mul(A,B):
    C=[R(0) for _ in range(7)]
    for i,a in enumerate(A):
        for j,b in enumerate(B):C[i+j]+=a*b
    for j in range(6,3,-1):C[j-4]+=C[j]*f
    return C[:4]
def power(A,n):
    B=[R(1),R(0),R(0),R(0)]
    for _ in range(n):B=mul(B,A)
    return B
def sub(A,B):return [a-b for a,b in zip(A,B)]
def scale(A,c):return [a*c for a in A]
def lin(row):return [row[0]*x+row[2],R(row[1]),R(0),R(0)]
unit=[R(1),R(0),R(0),R(0)];w=[R(0),R(1),R(0),R(0)]
def linear_inverse(row):
    a=row[0]*x+row[2];b=row[1];adj=[a**3,-a*a*b,a*b*b,R(-b**3)]
    norm=a**4-b**4*f
    assert mul(lin(row),adj)==[norm,R(0),R(0),R(0)]
    return adj,norm
def gpoly(vector,mons):
    v=[R(0) for _ in range(4)]
    for c,(a,b,d) in zip(vector,mons):v[b]+=c*x**a
    return v
def eval_form(vector,mons,coords):
    out=R(0)
    for c,exps in zip(vector,mons):
        h=R(c)
        for a,e in zip(coords,exps):h*=a**e
        out+=h
    return out

def reduce_frac(a,b):
    assert b!=0
    if a==0:return R(0),R(1)
    g=a.gcd(b);a=a//g;b=b//g
    return a,b
def differentiate_component(a,b,i):
    aa=(a.derivative()*b-a*b.derivative())*f+k(i)/4*a*b*f.derivative()
    return reduce_frac(aa,b*b*f)

eta=dec(data['eta']);assert eta**4==-one
maps=[mat(A) for A in data['quotient_maps']];inverses=[inv(A) for A in maps]
for A in maps:
    X,W,Z=map(lin,A)
    assert power(W,4)==sub(mul(power(X,3),Z),mul(X,power(Z,3)))
assert maps[0]==eye(3)
tors=[None]+[tuple(map(dec,T)) for T in data['torsion'][1:]]
assert len({tuple(map(enc,T)) for T in tors[1:]})==8
for a,b in tors[1:]:
    assert b*b==a**3-a and 3*a**4-6*a*a-1==0
    slope=(3*a*a-1)/(2*b)
    # Tangency has intersection multiplicity three precisely at a 3-torsion point.
    assert (slope*(x-a)+b)**2-(x**3-x)==-(x-a)**3
neg=[0]+[next(j for j,S in enumerate(tors) if S==(T[0],-T[1])) for T in tors[1:]]
expected={t for t in product(range(9),repeat=3) if t!=(0,0,0) and t<tuple(neg[a] for a in t)}
assert {tuple(r['torsion_indices']) for r in data['covers']}==expected

def basis_check(tup,rec,tchar):
    mons=rec['basis_monomials'];B=mat(rec['basis_char'+str(tchar)])
    d=sum(mons[0]);assert d==sum(a!=0 for a in tup)+1
    assert len(B)==2 and any(B[0][i]*B[1][j]!=B[0][j]*B[1][i] for i in range(len(mons)) for j in range(i+1,len(mons)))
    assert mons==[[a,b,d-a-b] for a in range(d+1) for b in range(d-a+1) if b<4]
    for i,ti in enumerate(tup):
        if not ti:continue
        a,b=tors[ti];V=inverses[i];eq=x*x-b
        coords=[R([r[0]*a+r[2],r[1]]) for r in V]
        for vec in B:
            h=eval_form(vec,mons,coords);assert h%eq==0
            if tchar==1:
                h=eval_form(vec,mons,[R([r[0],r[1]]) for r in V])
                assert h[0]==h[1]==0
            else:
                # Directional derivative along x_i on C, with w_i^2=b.
                dh=R(0)
                for c,exps in zip(vec,mons):
                    for j,e in enumerate(exps):
                        if not e:continue
                        hh=R(c*e*V[j][0])
                        for l,ee in enumerate(exps):hh*=coords[l]**(ee-(l==j))
                        dh+=hh
                dh+=h.derivative()*(3*a*a-1)*x/(4*b*b)
                assert dh%eq==0
    return B

checked=0;counts=Counter();orders=[]
for rec in data['covers']:
    tup=rec['torsion_indices'];B={t:basis_check(tup,rec,t) for t in [1,2]};mons=rec['basis_monomials']
    QQ=unit;AA=unit;NN=R(1);lead=one
    for i,ti in enumerate(tup):
        if not ti:continue
        a,b=tors[ti];s=(3*a*a-1)/(2*b);c=b-s*a;A=maps[i]
        X,W,Z=map(lin,A);Q=sub(sub(power(W,2),scale(mul(X,Z),s)),scale(power(Z,2),c))
        adj,nn=linear_inverse(A[2]);QQ=mul(QQ,Q);AA=mul(AA,adj);NN*=nn
        if i:
            Xp,Wp,Zp=(r[0] for r in A);lead*=(Wp*Wp-s*Xp*Zp-c*Zp*Zp)/(Zp*Zp)
    assert lead==dec(rec['normalization']) and lead!=0
    M=mat(rec['Cartier_matrix'])
    for tchar in [1,2]:
        target=3-tchar;kpower=(5*target-tchar)//3
        factor=mul(power(QQ,kpower),power(AA,2*kpower+1))
        den=NN**(2*kpower+1)*f*lead**kpower
        for j,vec in enumerate(B[tchar]):
            n=mul(mul(gpoly(vec,mons),factor),w)
            coeff=[M[2*(target-1)+i][2*(tchar-1)+j] for i in range(2)]
            assert all(M[2*(tchar-1)+i][2*(tchar-1)+j]==0 for i in range(2))
            outvec=[sum((coeff[i]*B[target][i][h] for i in range(2)),zero) for h in range(len(mons))]
            outn=mul(mul(gpoly(outvec,mons),AA),w);outd=NN*f
            for i in range(4):
                an,bn=reduce_frac(n[i],den)
                for _ in range(4):an,bn=differentiate_component(an,bn,i)
                assert -an*outd**5==outn[i]**5*f**i*bn,('Cartier identity',tup,tchar,j,i)
    # A direct conjugate product, in the opposite implementation order.
    A=eye(4)
    for j in range(8):A=mm(A,[[a**(5**((-j)%8)) for a in row] for row in M])
    assert A==mat(rec['Cartier_eighth_power'])
    cp=charpoly(A);assert [enc(a) for a in cp.coeffs()]==rec['new_characteristic_polynomial_mod5']
    val=cp(one);assert enc(val)==rec['relative_class_number_mod5'] and (val!=0)==rec['unit']
    active=sum(a!=0 for a in tup)
    assert cp==((x*x+x+1)**2 if active==2 else (x-1)**4)
    counts[(active,rec['unit'])]+=1;checked+=1
    if checked%50==0:print('checked',checked,'seconds',round(time.time()-start,2),flush=True)

assert counts==Counter({(1,False):12,(2,True):96,(3,False):256})
result={'source_sha256':sha256(raw).hexdigest(),'covers_checked':checked,
        'Cartier_columns_checked':4*checked,'rational_differential_component_identities':16*checked,
        'good_two_factor_covers':96,'bad_one_factor_covers':12,'bad_three_factor_covers':256,
        'checks':['irreducible field modulus','three plane-quartic automorphisms','eight elliptic flexes',
                  'all 364 torsion lines','Kummer normalization at P','two Riemann--Roch bases per cover',
                  'fourth-derivative Cartier identity','direct eightfold conjugate product','recursive characteristic polynomial'],
        'seconds':time.time()-start}
Path(__file__).with_suffix('.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2),flush=True)
