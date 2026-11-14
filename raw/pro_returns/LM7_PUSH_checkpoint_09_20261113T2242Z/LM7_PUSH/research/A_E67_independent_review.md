# Independent proof and source review of E67

Status: PASS of the complete mathematical proof and the four program sources. This note records a read, not an independent execution of the peer's certificates.

The reviewed statement is `sections/E_orbifold_CM_agent.tex`. The sources are `code/bc_orbifold_CM_characters.py`, `code/bc_orbifold_CM_six.py`, `code/bc_orbifold_CM_linear.py`, and `code/bc_orbifold_CM_export.py`.

## Actual quotient and frame comparisons

The displayed affine quotients retain the positive matrices R and S and the literal triangle words. The two printed Mordell kernel words map to the two translation basis vectors, with the unchanged cyclic deck quotient. The Gaussian words x²y and z²y do the same. The resulting maps therefore have the asserted abelianized geometric kernels, rather than merely equal finite orders.

For Mordell, fixing x and conjugating z by a deck-zero translation gives exactly (B−1)e1=(1−R²)a. The image of 1−R² is the printed line, and a matrix commuting with R has the same scalar on that line and on its one-dimensional quotient. This proves the positive original-orbifold sign without assigning the discrepancy character D3.

For Gaussian, the source convention f(y,x)=f(x,y)⁻¹ gives B e1=e1−v with the stated sign. All four determinant-one centralizer matrices are retained. The explicit image of z and the forced image of y give actual automorphisms; the full Cayley-edge check proves the finite map and its generation. The nine Mordell framed targets correctly retain the three possible z-frames for each of the three positive matrices.

## Complete common correction image

All 97 actual N words have even deck coordinate in every substitution. The Mordell image then has exponent three and the Gaussian image has exponent dividing six, so every N sixth power is killed, including products of the original generators. This proves the stated K6/N′ image equality.

All 4,656 original generator commutators are evaluated. Closing their translation span under every actual N-generator action gives precisely the image of N′. Each retained row operation is accompanied by a literal N′ word, and every pivot word is replayed. The separate linear comparison proves both inclusions between this span and the printed product M×G. The projection ranks sum to nine on this same domain.

The homogeneous Mordell equations intersect M trivially. The Gaussian equations give the stated two-dimensional linear family before its determinant-one restriction. The complete target lists and the actual origin evaluations then give exactly four correction-image points in each fibre. The coset description follows from the literal kernel of the homomorphism Θ. Generation is proved only for the explicitly enumerated two-factor affine image, as stated.

## Export and origin types

The export uses the right action t↦A⁻¹(t−v), hence p(gh)=p(h)[p(g)], matching the complete Schreier tools. It checks this product identity and replays all 97 literal words. The E1-original and E17/E62 origin families are evaluated independently. Absolute targets, origin values and correction differences are separately saved for both families. No K6 equivalence of the two lists is assumed.

The next E66/E67 join must compare the literal N word lists, recompute the actual E17 word values in these 12 maps, and use those absolute target differences. This review assigns no common quotient with the cyclic distribution or Ferrari sources.

## Reviewed hashes

- `sections/E_orbifold_CM_agent.tex`: `4ea79ced2b396eb1327b5ea5ad315a660da6d13f508a020f907fcb14d3ff6155`
- `code/bc_orbifold_CM_characters.py`: `8acf4d1e32c6a00a1aea94a42d8e5d9d7ef930387ec3e722bbdffd838c3a732f`
- `code/bc_orbifold_CM_six.py`: `f09891727048e4815abdb0b6de488ecc8012c3af95db44ed4d7bcc04228f313c`
- `code/bc_orbifold_CM_linear.py`: `bf8c90801f2a44d7106f59a38ade37d2301249679a8eaf5f0de776397ecdd3fc`
- `code/bc_orbifold_CM_export.py`: `9a4c9defb2bae40a5917bf06211f1a2d97bec6fb5ba69e56c6cfa3cfa71c7a92`
