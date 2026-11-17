"""Exact finite-quotient obstruction to the rejected full b-stage mechanism.

This checks the universal commutator polynomial over Z. It is not a test
of the original centralizer K or of whole source-kernel equality.
"""
from pathlib import Path
import json
import sympy as S
P=Path(__file__).resolve().parent
x,y,z=S.symbols('x y z')
G=S.Matrix([[1,x,z],[0,1,y],[0,0,1]])
B=S.Matrix([[1,0,0],[0,1,1],[0,0,1]])
comm=S.simplify(G*B*G.inv()*B.inv())
comm_inverse=S.simplify(G*B.inv()*G.inv()*B)
assert comm==S.Matrix([[1,0,x],[0,1,0],[0,0,1]])
assert comm_inverse==S.Matrix([[1,0,-x],[0,1,0],[0,0,1]])
print('PASS over Z[x,y,z]: [G,B] = I+x E13 and [G,B^-1] = I-x E13')
print('Hence in every modulus m>=2, centralizing either peripheral forces x=0 mod m')
print('At m=2, the 0- and1-peripherals have nontrivial central commutator E13')
out={'symbolic_commutator':str(comm),'inverse_peripheral_commutator':str(comm_inverse),'uniform_consequence':'x=0 modulo every m>=2, hence x=0 in Zhat','scope':'Obstruction only to extending the present single-retained-direction stage condition across the source zero-base operator.'}
(P/'zero_operator_heisenberg.json').write_text(json.dumps(out,indent=2)+'\n')
