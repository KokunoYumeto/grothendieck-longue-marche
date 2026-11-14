#!/usr/bin/env python3
"""Finite certificate: a nonsplit extension with perfect kernel.

G consists of PSL2(F9) and the nonsquare-determinant coset of PGL2(F9)
followed by the field involution. G -> C2 has perfect kernel and no
section, although abelianizing the kernel leaves the identity C2 -> C2.
"""
from itertools import product
from pathlib import Path
import json

# F9 = F3[u]/(u^2+1), encoded a+3b.
def add(x,y): return (x%3+y%3)%3+3*((x//3+y//3)%3)
def neg(x): return (-x%3)%3+3*((-(x//3))%3)
def sub(x,y): return add(x,neg(y))
def mul(x,y):
    a,b,c,d=x%3,x//3,y%3,y//3
    return (a*c+2*b*d)%3+3*((a*d+b*c)%3)
def power(x,n):
    r=1
    while n:
        if n&1:r=mul(r,x)
        x=mul(x,x);n//=2
    return r
def inverse(x):
    assert x
    return power(x,7)
def det(A):return sub(mul(A[0],A[3]),mul(A[1],A[2]))
def mm(A,B):
    a,b,c,d=A;e,f,g,h=B
    return (add(mul(a,e),mul(b,g)),add(mul(a,f),mul(b,h)),
            add(mul(c,e),mul(d,g)),add(mul(c,f),mul(d,h)))
def canonical(A):
    q=inverse(next(a for a in A if a))
    return tuple(mul(q,a) for a in A)
identity=(1,0,0,1)
PGL={canonical(A) for A in product(range(9),repeat=4) if det(A)}
square={A for A in PGL if power(det(A),4)==1}
nonsquare=PGL-square
assert (len(PGL),len(square),len(nonsquare))==(720,360,360)
involutions=[A for A in nonsquare
             if canonical(mm(A,tuple(power(x,3) for x in A)))==identity]
assert not involutions

# Upper and lower elementary matrices generate the kernel; the proof
# writes each as a commutator with one diagonal element.
diagonal_unit=next(d for d in range(1,9) if power(d,2)!=1)
commutator_coefficient=sub(power(diagonal_unit,2),1)
assert commutator_coefficient!=0
upper=[(1,a,0,1) for a in range(9)]
lower=[(1,0,a,1) for a in range(9)]
generators=upper+lower
generated={identity}; todo=[identity]
while todo:
    A=todo.pop()
    for B in generators:
        C=canonical(mm(A,B))
        if C not in generated:generated.add(C);todo.append(C)
assert generated==square
out={"field":"F3[u]/(u^2+1)","PGL2_order":len(PGL),
     "perfect_kernel_order":len(square),"extension_order":720,
     "nontrivial_coset_size":len(nonsquare),
     "involutions_in_nontrivial_coset":len(involutions),
     "elementary_generator_subgroup_order":len(generated),
     "diagonal_unit":diagonal_unit,
     "nonzero_commutator_coefficient":commutator_coefficient,
     "conclusion":"No section of G -> C2; the quotient after abelianizing its perfect kernel has a section.",
     "scope":"A finite obstruction to an inference, not a counterexample to D3 or D4."}
dest=Path(__file__).with_name("D_embedding_obstruction_output.json")
dest.write_text(json.dumps(out,indent=2)+"\n")
print(json.dumps(out,indent=2))
