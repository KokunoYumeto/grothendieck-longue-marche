"""Exact finite checks for C3:583--595,648--650,658--664.

Python standard library only. Outputs are written beside this script.
The finite fibre-product model is not identified with the universal
profinite normalizer construction.
"""
from itertools import product, permutations
from pathlib import Path
import json

OUT = Path(__file__).resolve().parent

# The order convention in scan 595(63): left factor is u', right is u.
V = list(product(range(2), repeat=2))
E = list(product(range(2), repeat=3))
one = (0, 0, 0)
def emul(a, b):
    s, u, v = a
    t, x, y = b
    return ((s+t+x*(u+v)) % 2, (u+x) % 2, (v+y) % 2)
def dmul(a, b):
    s, u, v = a
    t, x, y = b
    return ((s+t+u*(x+y)) % 2, (u+x) % 2, (v+y) % 2)
def cochain_change(a):
    s, u, v = a
    return ((s+u*v) % 2, u, v)
assert all(emul(emul(a,b),c)==emul(a,emul(b,c)) for a,b,c in product(E,repeat=3))
assert all(cochain_change(emul(a,b))==dmul(cochain_change(a),cochain_change(b)) for a,b in product(E,repeat=2))
def section(v): return (0,)+v
sign_pairs=[]
for a,b in product(V,repeat=2):
    left=emul(section(a),section(b))
    eps=(b[0]*(a[0]+a[1])) % 2
    assert left[0]==eps
    assert (eps==0)==(b[0]==0 or a[0]==a[1])
    sign_pairs.append(dict(left=a,right=b,central_exponent=eps))

# N_r=E x C3, N_s=V x C4, G=V x C2 over V.
# The complete triple fibre product is E x C3 x C4 x C2.
M=list(product(E,range(3),range(4),range(2)))
Mnat=[a for a in M if a[1]==a[2]==0]
def mmul(a,b):
    return (emul(a[0],b[0]),(a[1]+b[1])%3,(a[2]+b[2])%4,(a[3]+b[3])%2)
def to_g(a): return a[0][1:]+(a[3],)
def gmul(a,b): return tuple((x+y)%2 for x,y in zip(a,b))
assert all(to_g(mmul(a,b))==gmul(to_g(a),to_g(b)) for a,b in product(Mnat,repeat=2))
gimage={to_g(a) for a in Mnat}
ker=[a for a in Mnat if to_g(a)==(0,0,0)]
assert len(M)==192 and len(Mnat)==16 and len(gimage)==8 and len(ker)==2
central_three=[((s,0,0),0,2*t,w) for s,t,w in product(range(2),repeat=3)]
intersection=[a for a in central_three if a in Mnat]
assert len(intersection)==4 and all(a[2]==0 for a in intersection)
Gamma=[(e,c,d) for e,c,d,w in M if w==0]
Gamma_nat=[(e,0,0) for e in E]
S_Gamma=[(e,c,d) for e,c,d in Gamma if e[1:]==(0,0)]
assert len(Gamma)==96 and len(S_Gamma)==24
assert len(set(Gamma_nat)&set(S_Gamma))==2
identity_M=(one,0,0,0)
obstruction_lifts=[a for a in Mnat if to_g(a)==(1,0,0)]
assert len(obstruction_lifts)==2
assert all(mmul(a,a)!=identity_M and mmul(mmul(a,a),mmul(a,a))==identity_M for a in obstruction_lifts)

# The twisted a-law of scan 585(47), independently on S3.
S3=list(permutations(range(3)))
eid=(0,1,2)
def pmul(a,b): return tuple(a[b[i]] for i in range(3))
def pinv(a): return tuple(a.index(i) for i in range(3))
def parity(a): return sum(a[i]>a[j] for i in range(3) for j in range(i+1,3))%2
t=(1,0,2)
def tp(e):return t if e else eid
def aa(g):return pmul(tp(parity(g)),g)
twisted_failures=[]
for left,right in product(S3,repeat=2):
    lhs=aa(pmul(left,right))
    rhs=pmul(pmul(pmul(tp(parity(right)),aa(left)),tp(parity(right))),aa(right))
    assert lhs==rhs
    if lhs!=pmul(aa(left),aa(right)):
        twisted_failures.append(dict(left=left,right=right,lhs=lhs,naive=pmul(aa(left),aa(right))))
assert twisted_failures

# Scan 595: the commutator correction is a group word identity.
def comm(a,b):return pmul(pmul(pmul(a,b),pinv(a)),pinv(b))
word_checks=0
naive_word_failure=None
for u,up,a,ap in product(S3,repeat=4):
  for e,ep in product(range(2),repeat=2):
    alpha=pmul(pmul(u,pinv(a)),tp(e))
    alphap=pmul(pmul(up,pinv(ap)),tp(ep))
    alphapp=pmul(pmul(pmul(up,u),pinv(pmul(ap,a))),tp((e+ep)%2))
    naive=pmul(pmul(pmul(up,alpha),pinv(up)),alphap)
    correction=pmul(pmul(tp(ep),comm(ap,tp(e))),tp(ep))
    assert alphapp==pmul(naive,correction)
    word_checks+=1
    if naive!=alphapp and naive_word_failure is None:
        naive_word_failure=dict(u=u,up=up,a=a,ap=ap,e=e,ep=ep)
assert naive_word_failure is not None

# A strict modular C^natural: SL2(Z/4), with A=image(Pi0)=V4.
I=(1,0,0,1)
def matmul(a,b):
    x,y,z,w=a;v,t,r,s=b
    return ((x*v+y*r)%4,(x*t+y*s)%4,(z*v+w*r)%4,(z*t+w*s)%4)
def matinv(a):
    x,y,z,w=a
    return (w%4,-y%4,-z%4,x%4)
def neg(a):return tuple(-x%4 for x in a)
C=[a for a in product(range(4),repeat=4) if (a[0]*a[3]-a[1]*a[2])%4==1]
rho=(0,1,3,1);sigma=(0,3,1,0)
e0=matmul(sigma,rho);l=matmul(e0,e0);h=neg(l)
A={(1,0,0,1),(1,2,2,1),(3,0,2,3),(3,2,0,3)}
generated={I}
while True:
    bigger=generated|{matmul(a,b) for a in generated for b in [rho,sigma]}
    if bigger==generated: break
    generated=bigger
assert generated==set(C)
tau=(3,0,0,1)
assert matmul(matmul(tau,rho),tau)==matmul(matmul(sigma,matinv(rho)),matinv(sigma))
assert matmul(matmul(tau,sigma),tau)==matinv(sigma)
assert all(matmul(matmul(tau,a),tau) in A for a in A)
assert len(C)==48 and h in A and l not in A
assert all(matmul(matmul(c,a),matinv(c)) in A for c,a in product(C,A))
assert all(matmul(matmul(l,c),matinv(l))==matmul(matmul(h,c),matinv(h)) for c in C)
assert matmul(l,e0)==matmul(e0,l)
center={a for a in C if all(matmul(a,b)==matmul(b,a) for b in C)}
L={I,l}
assert L&center=={I} and L&A=={I}
L0={I,e0,l,matmul(l,e0)}
Pi={a for a in C if tuple(x%2 for x in a)==I}
assert len(Pi)==8
def conjugate(q,c):return matmul(matmul(q,c),matinv(q))
def positive_restricted(q):
    return (all(any(conjugate(q,c)==conjugate(a,c) for a in A) for c in [rho,sigma])
            and all(matmul(conjugate(q,c),matinv(c)) in Pi for c in C))
actual_Lnatural={q for q in L0 if positive_restricted(q)}
assert actual_Lnatural==L
AL={matmul(a,b) for a,b in product(A,L)}
assert len(AL)==8 and AL&center=={I,neg(I)}
assert all(matmul(a,b) in AL for a,b in product(AL,repeat=2))
assert all(matmul(matmul(h,c),matinv(h))==c for c in A)

data={
 'scope':'Finite algebraic models and corrected formal maps; no universal profinite normalizer identification claimed.',
 'source_cocycle':{'formula':'c((u_prime,v_prime),(u,v))=u*(u_prime+v_prime) mod2','associativity_triples':512,'pairs':sign_pairs,'D8_change_from_equation_D15':'(s,u,v)->(s+u*v,u,v)'},
 'fibre_product':{'M_order':192,'Mnatural_order':16,'G_order':8,'projection_kernel_order':2,'central_intersection':intersection,'Gamma_order':96,'Gamma_natural_order':8,'S_Gamma_order':24,'bisection_intersection_order':2,'order4_lifts_of_order2_element':obstruction_lifts},
 'twisted_a_law':{'pairs_checked':36,'nonmultiplicative_pairs':len(twisted_failures),'first_failure':twisted_failures[0]},
 'corrected_alpha_word':{'identities_checked':word_checks,'naive_failure':naive_word_failure,'central_epsilon':'An arbitrary central sign multiplies both sides and cancels in the word check.'},
 'restricted_modular_quotient':{'C_order':48,'Cnatural':sorted(A),'e0':e0,'l':l,'h_minus_l':h,'l_in_Cnatural':False,'inner_l_equals_inner_h':True,'actual_positive_Lnatural':sorted(actual_Lnatural),'Pi_order':8,'L_intersect_Cnatural_order':1,'L_intersect_center_order':1,'corrected_image_order':8,'Cnatural_order':4,'automorphism_kernel':sorted(AL&center),'numerical_subgroup_D_order':2,'gamma_D_over_jL_order':1}
}
(OUT/'B_late_sections.json').write_text(json.dumps(data,indent=2)+'\n')
print('Source-order sign cocycle: 512 triples, 16 sign pairs PASS; equation (D.15), statement D.8 cochain conversion PASS.')
print('Finite fibre product: M=192, Mnatural=16, G=8, kernel=2; Gamma=96, bisection=8, intersection=2.')
print('Central intersection is mu_rho x 1 x mu_G; both lifts of chosen involution have order 4: no section.')
print('Twisted a-law: 36 pairs PASS;',len(twisted_failures),'fail ordinary multiplicativity.')
print('Corrected alpha word:',word_checks,'identities PASS; omitted commutator gives a counterexample.')
print('SL2(Z/4): |C|=48, |A|=4; l=',l,'not in A; -l=',h,'in A; Int(l)=Int(-l).')
print('Restricted diagonal: L intersection A=1; corrected image |AL|=8, versus |A|=4; automorphism kernel={I,-I}.')
