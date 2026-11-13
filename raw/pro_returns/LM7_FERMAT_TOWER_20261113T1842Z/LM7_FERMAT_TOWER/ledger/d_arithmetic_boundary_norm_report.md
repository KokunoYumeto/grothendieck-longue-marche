# D.55 — arithmetic boundary norm and compact orientation

## Actual arithmetic comparison

The compactification map is constructed on the actual G3 cover. Its cusp radical has dimension `n/36−1`, and its compact homology has dimension `2+5n/36`. The source action fixes every cusp homology class because the base action is identity and the cusp defect is central. Thus every allowed homology parameter induces a compact homology map.

For the literal cusp error `z`, the thirty-sixth power of `zt` contributes the cyclic norm of z. Summing over the actual cusp cosets contributes every element of G once. Applying the lifted source map to the marked punctured-surface relation therefore proves the identity

`norm(q(p)) = (wedge² T_c)(Theta) − Theta`.

The norm includes the actual compactification projection. Theta is the inverse-form orientation bivector, not the matrix of the bilinear form. No invertibility assumption is used in this identity.

The complete local-conjugator image lies in the norm kernel. The remaining kernel is recorded exactly as `ker(norm)/local_image`. Before that quotient, its two contributions are the finite Tate norm kernel and the part of the full norm image killed by compactification. Neither contribution is silently omitted, and no arithmetic equality of the norm kernel and local image is asserted.

A point in the actual reduced boundary zero fiber preserves the nondegenerate compact orientation bivector. Its compact map is therefore invertible. Its cusp radical is already fixed, so its full homology action is invertible as well. Generation is thus a consequence of the actual boundary equation, not an independent unresolved test on that zero fiber. The arithmetic zero fiber itself remains unevaluated.

## Actual ordinary relative H2

The integral97-cycle augmentation matrix has Smith factors `(1^96,2)`. Since the marked Q abelianization is C6 and H2(C2*C3,Z)=0, the five-term sequence gives H2(Q,Z)=C2. The universal coefficient sequence and the actual odd kernel of G3→Q give H2(G3,F2)=F2².

The two central double covers detect the marked peripheral factors independently. SL2(Z/12) gives s-lift order4 and cusp-lift order36 over G3; D48's central E gives orders2 and72. Their dual restriction matrix on C2 and C36 is the identity. Thus those two inclusions span H2(G3,F2), and the relative group is the one-dimensional kernel of the sum map on peripheral H1. The original marked B pair maps isomorphically onto that relative orientation class. This statement uses trivial F2 coefficients; its exact relationship to the obstruction is retained through the separately proved norm map.

## Separately evaluated finite norm

The literal1080 graph has compact rank146 and cusp radical35. The program reconstructs the compact quotient, inverse-form bivector and all deck maps. It then reconstructs the exact thirteen original obstruction coordinates and evaluates their full norm through actual subgroup transversals.

The norm has rank9 and kills the four independent local-image vectors. Thus its kernel is exactly that local image. Every one of the18 linear and153 quadratic coefficients of the boundary map agrees through the norm with the compact orientation-bivector defect. This supplies the exact morphism explaining D54's864-point pairing-locus equality. The finite kernel equality is not asserted for G3.

## Reproduction and inputs

Run with Python3; the arithmetic lattice certificate also requires SymPy:

1. `python code/d_arithmetic_relative_h2.py`
2. `python code/d_cm_boundary_norm.py`

The programs are independent. Their immutable inputs are D48's central mixed certificate, D51's diagnostic form, D52's full invariant coefficients, and D54's reduced invariant certificate. Exact hashes are in the manifest. Each program has actual companion stdout and JSON. The author reran both in a copied directory and compared the complete outputs, excluding only elapsed time.

The smaller arithmetic detecting-module experiments were moved to the separate D56 research directory; they are not silently included in this D55 theorem.

## Completed independent verification

The root read the complete frozen proof and every owned program, then rebuilt from exact copied inputs. All complete JSON fields and stdout prefixes agree, excluding only explicitly named elapsed-time fields. The full peer proof review and independently coded focused maps also passed.
