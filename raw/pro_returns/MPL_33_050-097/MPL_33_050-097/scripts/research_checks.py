"""Exact finite calculations for research notes N43-N46, N66 and N70.

This script reads no scan and changes no transcription. It uses the displayed
E8 coordinates and elementary matrix equations, not OCR or a text database.
"""
from pathlib import Path
import sympy as sp

root = Path(__file__).resolve().parents[1]
e = list(sp.eye(8).columnspace())
alpha = [
    (e[0] + e[7] - sum(e[1:7], sp.zeros(8, 1))) / 2,
    e[0] + e[1],
] + [e[k] - e[k - 1] for k in range(1, 7)]
A = sp.Matrix.hstack(*alpha)
gram = A.T * A
permuted = alpha[0].copy()
permuted[0], permuted[1] = alpha[0][1], alpha[0][0]
assert alpha[0] + alpha[2] == permuted
assert alpha[0] + alpha[1] != permuted
assert ((alpha[0] + alpha[1]).T * (alpha[0] + alpha[1]))[0] == 4
assert 2 * alpha[0] + alpha[2] + e[2] + e[3] + e[4] + e[5] == e[7] - e[6]
coeffs = A.inv() * (e[7] - e[6])
assert list(coeffs) == [2, 2, 3, 4, 3, 2, 1, 0]
assert gram.det() == 1
assert A.inv() * alpha[0] == e[0]
assert all(gram[i, i + 1] == -1 for i in range(2, 7))
assert all(gram[i, i] == 2 for i in range(8))

# Sierpinski-space sheaf PF: Z^2 -> Z, restriction [1,0].
# An endomorphism is a matrix M on X and multiplication q on {a}.
u, v, w, z, q = sp.symbols('u v w z q')
M = sp.Matrix([[u, z], [v, w]])
restriction = sp.Matrix([[1, 0]])
equation = restriction * M - q * restriction
assert sp.solve(list(equation), [u, z]) == {u: q, z: 0}
cross = sp.Matrix([[0, 0], [1, 0]])
assert restriction * cross == sp.zeros(1, 2)
assert cross != sp.zeros(2)

report = f"""# Exact algebra checks on frozen readings

Research checks only; no transcription has been changed.

## E8, cote33 scan075

- alpha1+alpha2 = {list(alpha[0]+alpha[1])}
- Squared norm of alpha1+alpha2 = 4
- alpha1+alpha3 = {list(alpha[0]+alpha[2])}
- The latter equals alpha1 with epsilon1 and epsilon2 interchanged.
- 2alpha1+alpha3 = {list(2*alpha[0]+alpha[2])}
- Adding (epsilon3+epsilon4)+(epsilon5+epsilon6) gives epsilon8-epsilon7.
- epsilon8-epsilon7 simple-root coefficients = {list(coeffs)}
- alpha1 simple-root coefficients = {list(A.inv()*alpha[0])}; not all strictly positive.
- Gram matrix = {gram}
- Gram determinant = {gram.det()}
- Adjacent chain inner products -1 verified for source indices3 through7.
- Source endpoint8 would require an undefined alpha9.
- Integer roots = 8 choose2 times4 = {sp.binomial(8,2)*4}
- Half-integer even-parity roots = 2^7 = {2**7}
- Total = 240
- F4 exponent-plus-one product = 2*6*8*12 = {2*6*8*12}

## Two-point sheaf calculation, cote33 scan051

With opens empty, {{a}}, X={{a,b}}, take F(X)=F({{a}})=Z and identity restriction.
Both original stalks are Z; PF has sections Z^2 on X and Z on {{a}}, restriction [1,0].
The general endomorphism has matrix [[q,0],[v,w]] on X and scalar q on {{a}}.
There are three independent integer parameters, versus two for coordinatewise
endomorphisms of the original stalk family. The matrix [[0,0],[1,0]] with scalar0
is a nonzero sheaf morphism and cannot be a diagonal coordinatewise morphism.

This is a counterexample to the natural Hom identification under the standard
sheaf interpretation visible in the excerpt; missing definitions might impose
additional restrictions, so no unqualified claim about an identified author's
full theorem or book is made.
"""
(root / 'records/root_checks.md').write_text(report)
print('PASS: exact E8 identities, Gram matrix, counts, and two-point Hom calculation.')

