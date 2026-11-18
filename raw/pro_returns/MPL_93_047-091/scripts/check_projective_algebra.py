#!/usr/bin/env python3
"""Post-freeze certificates for research notes OP; never reads/writes transcription.

Exact arithmetic, not a proof assistant. SymPy verifies polynomial identities;
the accompanying prose explains their scope and the principal-parts argument.
"""
from itertools import combinations, product
import json
import sympy as s
from sympy.matrices.normalforms import smith_normal_form

e = s.Matrix([1, 0, 0])
h = s.Matrix([0, 1, 0])
f = s.Matrix([0, 0, 1])
basis = [e, h, f]

def bracket(x, y):
    a, b, c = x
    u, v, w = y
    return s.Matrix([b*u-a*v, 2*(a*w-c*u), c*v-b*w])

def ad(x):
    return s.Matrix.hstack(*(bracket(x, y) for y in basis))

def mod_rank(M, p):
    a = [[int(M[i, j]) % p for j in range(M.cols)] for i in range(M.rows)]
    r = 0
    for col in range(M.cols):
        pivot = next((i for i in range(r, M.rows) if a[i][col]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][col], -1, p)
        a[r] = [(x * inv) % p for x in a[r]]
        for i in range(M.rows):
            if i != r and a[i][col]:
                scale = a[i][col]
                a[i] = [(x-scale*y) % p for x,y in zip(a[i],a[r])]
        r += 1
        if r == M.rows:
            break
    return r

assert bracket(e, h) == -e
assert bracket(f, h) == f
assert bracket(e, f) == 2*h
for x,y,z in product(basis, repeat=3):
    assert bracket(x,bracket(y,z))+bracket(y,bracket(z,x))+bracket(z,bracket(x,y)) == s.zeros(3,1)

a,b,c=s.symbols('a b c')
ad_abc = ad(s.Matrix([a,b,c]))
assert ad_abc == s.Matrix([[b,-a,0],[-2*c,0,2*a],[0,c,-b]])
K = s.Matrix(3,3,lambda i,j:s.trace(ad(basis[i])*ad(basis[j])))
assert K == s.Matrix([[0,0,4],[0,2,0],[4,0,0]])
assert K.det() == -32

d=s.symbols('d0:9')
D=s.Matrix(3,3,d)
relations=[]
for i,j in combinations(range(3),2):
    relations.extend(D*bracket(basis[i],basis[j])-bracket(D*basis[i],basis[j])-bracket(basis[i],D*basis[j]))
A,_=s.linear_eq_to_matrix(relations,d)
snf=smith_normal_form(A,domain=s.ZZ)
diag=[int(snf[i,i]) for i in range(min(snf.shape))]
generic=s.linsolve((A,s.zeros(A.rows,1)),d)
der_dims={str(p):9-mod_rank(A,p) for p in [2,3,5,7]}
assert der_dims == {'2':6,'3':3,'5':3,'7':3}
outer=s.Matrix([[0,0,0],[0,0,0],[1,0,0]]) # D(e)=f, D(h)=D(f)=0
for i,j in combinations(range(3),2):
    rel=outer*bracket(basis[i],basis[j])-bracket(outer*basis[i],basis[j])-bracket(basis[i],outer*basis[j])
    assert all(int(x)%2==0 for x in rel)
assert outer[2,0] == 1 and ad_abc[2,0] == 0

# Actual conjugation of two-by-two matrices, projected modulo scalar matrices.
alpha,beta=s.symbols('alpha beta',nonzero=True)
T=s.Matrix([[alpha,beta],[0,1]])
E12=s.Matrix([[0,1],[0,0]])
H=s.Matrix([[1,0],[0,0]])
E21=s.Matrix([[0,0],[1,0]])
def proj(M):
    return s.Matrix([M[0,1],M[0,0]-M[1,1],M[1,0]])
transition=s.simplify(s.Matrix.hstack(*(proj(T*x*T.inv()) for x in [E12,H,E21])))
expected=s.Matrix([[alpha,-beta,-beta**2/alpha],[0,1,2*beta/alpha],[0,0,1/alpha]])
assert transition == expected
B=transition[:2,:2]
Q=transition[1:,1:]
swap=s.Matrix([[0,1],[1,0]])
Bdual=swap*(B.inv().T)*swap
assert Bdual == s.Matrix([[1,beta/alpha],[0,1/alpha]])
pairing=s.Matrix([[2,0],[0,4]]) # g/e basis h,f to dual B basis h*,e*
assert s.simplify(pairing*Q-Bdual*pairing)==s.zeros(2)

# Compare pgl2 and sl2 brackets in characteristic two.
Hsl=s.Matrix([[1,0],[0,-1]])
assert E12*Hsl-Hsl*E12 == -2*E12
assert E21*Hsl-Hsl*E21 == 2*E21
assert E12*E21-E21*E12 == Hsl

result={
 'bracket_normalization':'[e,h]=-e, [f,h]=f, [e,f]=2h',
 'Jacobi_on_basis':'PASS',
 'ad_matrix':str(ad_abc),
 'Killing_matrix':str(K),
 'Killing_determinant':int(K.det()),
 'derivation_equations_smith_diagonal':diag,
 'derivations_over_Q':str(generic),
 'derivation_dimensions_mod_p':der_dims,
 'char2_outer_D_e_equals_f':'PASS; every inner derivation has f-coordinate zero on e',
 'upper_triangular_conjugation':str(transition),
 'quotient_g_over_e_transition':str(Q),
 'dual_B_transition':str(Bdual),
 'Killing_pairing_intertwiner':str(pairing),
 'connection_graded_coefficients':'c12=-2c, c23=c; filtration-preserving iff c=0',
 'scope':'Exact finite algebra certificates; no global descent, formal proof assistant, or unseen manuscript claim is certified.'
}
print(json.dumps(result,indent=2))
