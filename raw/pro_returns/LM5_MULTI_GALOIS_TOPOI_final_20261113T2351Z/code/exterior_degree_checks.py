"""Exact symbolic certificates for the infinite dihedral counterexamples.

The matrices represent r^n and s for every integer n; no finite cutoff is
used to infer the group identities. Normal-form uniqueness is proved in
the manuscript. The free-group label obstruction is abelianization.
"""
import sympy as sp

n = sp.symbols('n', integer=True)
R = lambda k: sp.Matrix([[1,k],[0,1]])
S = sp.Matrix([[-1,0],[0,1]])
eye = sp.eye(2)
assert S*S == eye
assert S*R(n)*S == R(-n)
assert R(n)*R(1) == R(1)*R(n)
reflection_commutator_difference = R(n)*S*R(1)-R(1)*R(n)*S
assert reflection_commutator_difference == sp.Matrix([[0,-2],[0,0]])
central_rotation_difference = R(n)*S-S*R(n)
assert central_rotation_difference == sp.Matrix([[0,2*n],[0,0]])
assert R(n)-eye == sp.Matrix([[0,n],[0,0]])
print('Exact symbolic identity: s r^n s = r^(-n) for arbitrary integer n.')
print('Rotations commute with r; every reflection has nonzero commutation difference:')
print(reflection_commutator_difference)
print('A rotation commutes with s iff 2n=0, hence n=0 over Z:')
print(central_rotation_difference)
print('Thus Z(D_infinity)=1, C(<r>)=<r>, and r^n=1 iff n=0.')
print('Loop embeddings +1 and -1 are conjugate; both degrees satisfy the same exterior equation.')
a = sp.Matrix([1,0])
ainv = sp.Matrix([-1,0])
assert a != ainv
print('Free-group labels a and a^(-1) have different abelianizations',list(a),list(ainv))
print('Conjugation preserves abelianization, so the labels are not conjugate.')
print('ALL EXACT SYMBOLIC CHECKS PASSED')
