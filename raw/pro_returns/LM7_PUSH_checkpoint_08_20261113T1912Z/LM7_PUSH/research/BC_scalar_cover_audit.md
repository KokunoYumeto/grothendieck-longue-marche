# Independent audit of D.50

## Frozen proof and certificate

Full proof audit: **PASS**. The inspected final source is
`sections/D_pronilpotent_lift_agent.tex`, SHA256
`b27a2116165d03c975e4022125e92fcbf3e599f25d217b350f32a8ec26ef3ff9`.
This includes the revised line breaks in D.50.6 and the explicit equality
between the nilpotent residual and the intersection of the closed lower
central terms. No integrated source was edited during this audit.

Independent executable: `code/bc_scalar_cover_count.py`. It uses only the
Python standard library and no other project certificate. Replay with
`python code/bc_scalar_cover_count.py`; it writes the adjacent JSON. The
saved `.out` records the first authoritative complete pass, in 0.314 seconds.

| Artifact | SHA256 |
|---|---|
| `bc_scalar_cover_count.py` | `e46230642c4bff3d2b105e58ed5dd467f30102ed056a9a41b1c5da474594bc4d` |
| `bc_scalar_cover_count.json` | `0b94599c617129e399e820a6e24312f7a3c311e12b2d40da08c319779641fbd9` |
| `bc_scalar_cover_count.out` | `bc8d39c94fd2d6e39dad080b0a6feaeeac8d11ba7b324711b08d3a3268b5ad94` |

## Exact maps checked

For every subgroup (J\le E) onto (D), with (M=J\cap A), the finite
intertwiner group uses the determinant condition (det B\in\mu_{\exp J}).
Its scalar kernel has order (d\exp J). The normal graph

\[
 m\longmapsto(m,\rho(m))
\]

meets that scalar kernel trivially even for a nonfaithful representation.
The actual isomorphism is

\[
 \widetilde J_\rho\longrightarrow J\times_D Q_\rho,
 \qquad(g,B)\longmapsto(g,[(g,B)]).
\]

Surjectivity follows by multiplying a chosen pair lift by the graph element
for (g(g')^{-1}\in M); it does not require a faithful representation or a
chosen projective splitting. The three matrices in the pants formula have
product (\rho(a_1a_2a_3)), because their prescribed (Q_\rho) coordinates
have product one. Schur scalarization and the regular character therefore
give exactly the coefficient (1/(|M|\dim\rho)) in D.50.11.

The all-genus coefficient in D.50.12 also checks. The unnormalized handle
average is ((|M|/d)^2I). Averaging first over the first (M) coordinate
and then using matrix-coefficient orthogonality gives that exact value.
Sandwiching D.50.14 by an irreducible idempotent forces the second outer
handle value to stabilize the representation; linear inversion and the
dual idempotent force the first. Thus the vanishing of noninvariant blocks
does not assume an extension of those representations.

The actual boundary transport is

\[
 T_i^1\cap J=j_i(T_i^0\cap J)j_i^{-1},\qquad
 (j_i,\widetilde r_i)\in J\times_DQ_\rho.
\]

It gives literal matrix conjugacy and equality of every subgroup weak
count. Ordinary subgroup-poset Möbius inversion retains all proper images.
The full ordinary conjugator union uses the actual centralizer image in
(D); no surjectivity of a centralizer map is presumed.

For generation, the common quotient of (A) and the central kernel
(Z=\ker(D^\dagger\to D)) carries trivial (E)-conjugation. Consequently it
kills ([E,A]). The hypothesis ([E,A]=A) therefore gives the entire
specified fibre product. This proof uses the actual joint source action,
not only the fact that the common quotient is abelian.

For the modular source, each auxiliary representation is scaled so that
the actual chosen order-two and order-three matrices satisfy their torsion
relations. Their determinants belong to (\mu_{\exp J}). Thus each
auxiliary map is a homomorphism from (widehat{C_2*C_3}), rather than only
from the free pants source.

## Compactness and normalization

For the free source use (A=\gamma_\infty(E_0)). For the modular source,
include the specified (S_3) quotient in every finite collection and use
(A=\gamma_\infty(\ker(E_0\to S_3))). In both cases ([E_0,A]=A), and the
actual central refinement has the required nilpotent source image.

The compact space retains all three full conjugator coordinates. Every
finite collection of relations, generation conditions, and prescribed
pronilpotent coordinates has a solution in one actual finite joint source.
The limit generates every finite quotient; its compact image is therefore
the whole source. Hopficity applies to the finitely generated whole source.

The exact local-source map is the fibre product

\[
 \mathcal B/R_{\rm nil}(F)
 \simeq\prod_{p,S_3}\mathcal B/O^p(F).
\]

Its kernel comparison and surjectivity follow from the actual map
(F/R_{\rm nil}(F)\simeq\prod_pF^{(p)}). A local gentle automorphism at
(\ell\ge5), with identity at other primes, has compatible literal
peripheral conjugators by coprime complement conjugacy. The full lift can
be conjugated by an element of the retained kernel to fix (\tau).
Then (f=s\Phi(s)) lies in (F'), since the actual quotient
(\mathcal B/F') factors through the retained quotient. The equations
(\Phi(s)=sf), (\Phi(r)=f^{-1}r), and the exact D.44 conjugation table give
the two gentle equations in the original free generators.

## Independent finite coverage

| Model | Exact checks |
|---|---|
| (Q_8\to V_4), kernel (C_2) | 420 surface cases with both nontrivial scalar phases; literal 32-element pair group and 16-element cover |
| (Q_8\rtimes C_3\to C_3) | 848 surface cases; noncentral normal kernel (Q_8); invariant dimensions 1 and 2; all nine matrix handle averages; 12 boundary and 24 handle noninvariant-block vanishings |
| Degree-two pair cover for (Q_8\rtimes C_3) | 576 actual pairs; all 331,776 products; normal graph and exact pullback |
| All subgroups of (Q_8\rtimes C_3) | All 15 subgroups enumerated; nine onto (C_3); 1,088 proper-subgroup coefficient checks; 136 ordinary Möbius epimorphism checks; 3,672 literal boundary-conjugator choices |
| (D_8\), (M=C_4\), (\rho(r)=-1) | Nonfaithful representation; exact graph/scalar intersection; 1,024 products; quotient (C_4\times C_2); all 32 pullback elements |

The central (Q_8\to V_4) and nonfaithful (D_8) cases test the counting
and cover statements for arbitrary normal kernels. They are not used as
examples of ([E,A]=A). The noncentral binary-tetrahedral example supplies
that latter condition. The finite tests check the identities; the complete
source theorem follows from the algebraic proof audited above.

## Exact graded consequences

The characteristic map (widehat F\to F^{(\ell)}) is the map used to
define the pulled-back source filtration. Retaining the entire local
automorphism therefore retains its exact associated graded coordinate.
The three R8 weight-five realizations, combined with the existing upper
dimension three, give the asserted dimension three for D1.

For D2 the normalized modular lift retains the whole (f_\ell), hence its
weight-nine polynomial. The realized extra polynomial
(X^2Y^2(X+Y)^3) has zero (X^7) coefficient, whereas
(((X+Y)^9-X^9-Y^9)/(XY)) has coefficient 9. Their characteristic-zero
independence and the existing two-dimensional invariant calculation give
dimension two. The map here is the same exact characteristic projection;
no comparison with a different filtration is inserted.
