# Exact algebra checks on frozen readings

Research checks only; no transcription has been changed.

## E8, cote33 scan075

- alpha1+alpha2 = [3/2, 1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 1/2]
- Squared norm of alpha1+alpha2 = 4
- alpha1+alpha3 = [-1/2, 1/2, -1/2, -1/2, -1/2, -1/2, -1/2, 1/2]
- The latter equals alpha1 with epsilon1 and epsilon2 interchanged.
- 2alpha1+alpha3 = [0, 0, -1, -1, -1, -1, -1, 1]
- Adding (epsilon3+epsilon4)+(epsilon5+epsilon6) gives epsilon8-epsilon7.
- epsilon8-epsilon7 simple-root coefficients = [2, 2, 3, 4, 3, 2, 1, 0]
- alpha1 simple-root coefficients = [1, 0, 0, 0, 0, 0, 0, 0]; not all strictly positive.
- Gram matrix = Matrix([[2, 0, -1, 0, 0, 0, 0, 0], [0, 2, 0, -1, 0, 0, 0, 0], [-1, 0, 2, -1, 0, 0, 0, 0], [0, -1, -1, 2, -1, 0, 0, 0], [0, 0, 0, -1, 2, -1, 0, 0], [0, 0, 0, 0, -1, 2, -1, 0], [0, 0, 0, 0, 0, -1, 2, -1], [0, 0, 0, 0, 0, 0, -1, 2]])
- Gram determinant = 1
- Adjacent chain inner products -1 verified for source indices3 through7.
- Source endpoint8 would require an undefined alpha9.
- Integer roots = 8 choose2 times4 = 112
- Half-integer even-parity roots = 2^7 = 128
- Total = 240
- F4 exponent-plus-one product = 2*6*8*12 = 1152

## Two-point sheaf calculation, cote33 scan051

With opens empty, {a}, X={a,b}, take F(X)=F({a})=Z and identity restriction.
Both original stalks are Z; PF has sections Z^2 on X and Z on {a}, restriction [1,0].
The general endomorphism has matrix [[q,0],[v,w]] on X and scalar q on {a}.
There are three independent integer parameters, versus two for coordinatewise
endomorphisms of the original stalk family. The matrix [[0,0],[1,0]] with scalar0
is a nonzero sheaf morphism and cannot be a diagonal coordinatewise morphism.

This is a counterexample to the natural Hom identification under the standard
sheaf interpretation visible in the excerpt; missing definitions might impose
additional restrictions, so no unqualified claim about an identified author's
full theorem or book is made.
