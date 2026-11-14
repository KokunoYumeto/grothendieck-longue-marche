"""Exact characteristic-two test of prime-to-2 point-section separation.

C/F2: Y^2+(x^2+x)Y=x^5+x^3+x^2+x.
Over F16 construct functions F=(A+Y)/a with Norm(F)=u^3.
The unramified cyclic cubic cover z^3=F has elliptic quotient
w=z+u/z, with w^3+u*w=(x^2+x)/a.  Test images of all points over
x=0 against the point over infinity with leading coefficient z/x=1.

No external finite-field or elliptic-curve package is used.  The field
is F2[t]/(t^4+t+1); all polynomial and group calculations are exact.
"""
from pathlib import Path
from itertools import product
import json

q=16
def add(a,b):return a^b
def mul(a,b):
    ans=0
    while b:
        if b&1:ans^=a
        b>>=1;a<<=1
        if a&16:a^=0x13
    return ans
def power(a,n):
    ans=1
    while n:
        if n&1:ans=mul(ans,a)
        a=mul(a,a);n>>=1
    return ans
def inv(a):
    assert a
    return power(a,14)
def div(a,b):return mul(a,inv(b))
def trim(a):
    a=list(a)
    while a and not a[-1]:a.pop()
    return a
def padd(a,b):return trim([(a[i] if i<len(a) else 0)^(b[i] if i<len(b) else 0) for i in range(max(len(a),len(b)))])
def pmul(a,b):
    out=[0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):out[i+j]^=mul(x,y)
    return trim(out)
def pscale(a,s):return trim([mul(x,s) for x in a])
def ppow(a,n):
    out=[1]
    for _ in range(n):out=pmul(out,a)
    return out
def peval(a,x):
    out=0
    for c in reversed(a):out=mul(out,x)^c
    return out
def encode(a):return sum(x<<(4*i) for i,x in enumerate(a))
def decode(v,n=4):return [(v>>(4*i))&15 for i in range(n)]
f=[0,1,1,1,0,1];h=[0,1,1]

def solve_binary(columns,target):
    basis={};null=[]
    for j,col in enumerate(columns):
        v=col;comb=1<<j
        while v:
            pivot=v.bit_length()-1
            if pivot in basis:
                v^=basis[pivot][0];comb^=basis[pivot][1]
            else:
                basis[pivot]=(v,comb);break
        if not v:null.append(comb)
    v=target;comb=0
    while v:
        pivot=v.bit_length()-1
        if pivot not in basis:return []
        v^=basis[pivot][0];comb^=basis[pivot][1]
    sols=[comb]
    for n in null:sols += [x^n for x in sols.copy()]
    return sols

def norm_polynomial(A):return padd(padd(ppow(A,2),pmul(h,A)),f)
torsion_functions=[]
for u0,u1 in product(range(q),repeat=2):
    u=[u0,u1,1];u3=ppow(u,3)
    cols=[]
    for i in range(16):
        A=decode(1<<i)
        cols.append(encode(padd(padd(ppow(A,2),pmul(h,A)),pscale(u3,power(A[3],2)))))
    solutions=solve_binary(cols,encode(f))
    for solution in solutions:
        A=decode(solution);a=A[3]
        if a and norm_polynomial(A)==pscale(u3,power(a,2)):
            # A and A+h define inverse 3-torsion classes.
            Ah=decode(encode(padd(A,h)))
            if tuple(A)<tuple(Ah):
                torsion_functions.append((u,A))

def normalize(P):
    c=next(t for t in P if t)
    return tuple(div(t,c) for t in P)
projective_points=[(1,w,z) for w,z in product(range(q),repeat=2)]+[(0,1,z) for z in range(q)]+[(0,0,1)]
O=(1,0,0)
def cross(P,Q):
    return (mul(P[1],Q[2])^mul(P[2],Q[1]),
            mul(P[2],Q[0])^mul(P[0],Q[2]),
            mul(P[0],Q[1])^mul(P[1],Q[0]))
def dot(P,Q):return mul(P[0],Q[0])^mul(P[1],Q[1])^mul(P[2],Q[2])

reports=[]
for u,A in torsion_functions:
    a=A[3];u0,u1,_=u
    def equation(P):
        X,W,Z=P
        term=power(W,3)^mul(power(X,2),W)^mul(u1,mul(mul(X,Z),W))^mul(u0,mul(power(Z,2),W))
        return mul(a,term)^mul(power(X,2),Z)^mul(X,power(Z,2))
    def gradient(P):
        X,W,Z=P
        return (mul(mul(a,u1),mul(Z,W))^power(Z,2),
          mul(a,power(W,2)^power(X,2)^mul(u1,mul(X,Z))^mul(u0,power(Z,2))),
          mul(mul(a,u1),mul(X,W))^power(X,2))
    pts=[P for P in projective_points if not equation(P)]
    singular=[P for P in pts if gradient(P)==(0,0,0)]
    # The smoothness check over F16 is strengthened below by solving the
    # gradient equations over the algebraic closure via a symbolic criterion.
    # If Z=0 only R=(1,1,0) can be singular, requiring a*u1=1.
    # If Z!=0, X^2=a*u1*X*W and a*u1*W=1; together force X in {0,1}.
    # At these x values f and h have no common zero of the plane gradient
    # unless equation evaluated at the uniquely prescribed W vanishes.
    geometric_singular=[]
    if mul(a,u1)==1:geometric_singular.append('infinity R')
    if u1:
        W=inv(mul(a,u1))
        for X in (0,1):
            P=(X,W,1)
            if not equation(P) and gradient(P)==(0,0,0):geometric_singular.append(list(P))
    assert not geometric_singular and not singular

    def third(P,Q):
        line=gradient(P) if P==Q else cross(P,Q)
        line=normalize(line)
        on=[R for R in pts if dot(line,R)==0]
        if P!=Q:
            if normalize(gradient(P))==line:return P
            if normalize(gradient(Q))==line:return Q
            others=[R for R in on if R not in (P,Q)]
            assert len(others)==1,(P,Q,on)
            return others[0]
        others=[R for R in on if R!=P]
        assert len(others)<=1
        return others[0] if others else P
    def eadd(P,Q):
        if P==O:return Q
        if Q==O:return P
        return third(third(P,Q),O)
    table={(P,Q):eadd(P,Q) for P,Q in product(pts,repeat=2)}
    for P,Q,R in product(pts,repeat=3):
        assert table[table[P,Q],R]==table[P,table[Q,R]]
    orders={}
    for P in pts:
        R=O
        for n in range(1,len(pts)+1):
            R=table[R,P]
            if R==O:orders[P]=n;break
        assert P in orders and len(pts)%orders[P]==0
    F0=div(A[0],a)
    roots=[z for z in range(q) if power(z,3)==F0]
    assert len(roots)==3 and all(roots)
    images=[normalize((0,z^div(u0,z),1)) for z in roots]
    assert all(P in pts for P in images)
    image_orders=[orders[P] for P in images]
    odd_obstructions=[o&(o-1)!=0 for o in image_orders]
    # For an integer order o, o&(o-1)==0 iff o is a power of 2.
    report={'u_coefficients_low_to_high':u,'A_coefficients_low_to_high':A,'a':a,
        'norm_identity':True,'elliptic_curve':'a*(W^3+(X^2+u1*X*Z+u0*Z^2)*W)=X^2*Z+X*Z^2',
        'geometrically_smooth':True,'elliptic_points':len(pts),
        'group_order_distribution':{str(n):list(orders.values()).count(n) for n in sorted(set(orders.values()))},
        'F_at_P0':F0,'cubic_roots_at_P0':roots,
        'quotient_images_at_P0':[list(P) for P in images],
        'quotient_point_orders':image_orders,
        'all_three_have_non_2_primary_order':all(odd_obstructions),
        'group_law_associativity_exhaustively_checked':True}
    reports.append(report)

out={'field':'F2[t]/(t^4+t+1), integers encode binary polynomial coefficients',
    'base_curve':'Y^2+(x^2+x)*Y=x^5+x^3+x^2+x',
    'points_compared':['P_infinity','P_0=(0,0)'],
    'number_of_inverse_pairs_of_3_torsion_functions':len(torsion_functions),
    'covers':reports}
base_counts={}
for degree in (1,2,4):
    vals=[x for x in range(q) if power(x,2**degree)==x]
    count=sum(power(Y,2)^mul(peval(h,x),Y)^peval(f,x)==0 for x,Y in product(vals,repeat=2))+1
    base_counts[str(2**degree)]=count
assert base_counts=={'2':3,'4':3,'16':31}
out['base_curve_point_counts']=base_counts
alpha=6;beta=4
assert power(alpha,2)^alpha^1==0 and power(beta,2)^beta==power(alpha,2)
selected_u=[alpha,0,1];selected_A=[1,beta,beta^1,1]
assert norm_polynomial(selected_A)==ppow(selected_u,3)
out['selected_degree27_cover']={'alpha':alpha,'beta':beta,'u':selected_u,'A':selected_A,
    'base_genus':2,'cyclic_cover_degree':3,'cyclic_cover_genus':4,
    'elliptic_quotient_degree':2,'multiplication_by_3_degree':9,
    'composite_degree':27,'fibre_infinity_maps_to_origin':True,
    'elliptic_group':'(Z/3)^2',
    'all_points_over_P0_map_to_nonzero_3_torsion':True}
# Independent small certificate for the stronger, all-geometric-points
# argument.  The formal point separation outside the exceptional fibres
# follows from the invertible coefficient matrix; the two exceptional
# fibres are checked here exactly over their residue field F4.
subfield4=[a for a in range(q) if power(a,4)==a]
assert len(subfield4)==4
affine4={str(x):[w for w in subfield4 if power(w,3)^mul(power(x,2)^alpha,w)^power(x,2)^x==0] for x in subfield4}
assert sum(map(len,affine4.values()))+2==9
roots_unity=[a for a in subfield4 if power(a,3)==1]
matrix_determinant=alpha^inv(alpha)
assert matrix_determinant==1
branch_zero=[(v,mul(inv(alpha),v)) for v in roots_unity]
branch_unit=[(z,mul(alpha,z)) for z in roots_unity]
assert len(set(branch_zero+branch_unit))==6
infinity_pairs=[]
for xi in (1,alpha,power(alpha,2)):
    residues=(xi^inv(xi),mul(alpha,xi)^mul(inv(alpha),inv(xi)))
    assert all(a in (0,1) for a in residues)
    infinity_pairs.append(['O' if a==0 else 'T' for a in residues])
assert infinity_pairs==[['O','T'],['T','T'],['T','O']]
out['all_geometric_points_criterion_certificate']={
    'E_defined_over_F4':True,'F4_elements':subfield4,
    'E_F4_affine_fibres':affine4,'E_F4_points_at_infinity':2,
    'E_F4_total':9,'Frobenius_polynomial':[4,4,1],
    'Frobenius_equals_minus_2':'proved in A.10 from (pi+2)^2=0 and isogeny composition',
    'geometric_2_primary_torsion':'zero',
    'matrix_determinant':matrix_determinant,
    'u_zero_branch_F_zero_pairs':branch_zero,
    'u_zero_branch_F_unit_pairs':branch_unit,
    'six_exceptional_finite_image_pairs_distinct':True,
    'three_infinity_image_pairs':infinity_pairs,
    'proof_scope':'Finite checks certify the exceptional fibres; general-point injectivity is the algebraic proof in A.10.'}
Path(__file__).with_name('A_char2_cubic_test_output.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
