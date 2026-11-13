INCOMPLETE

# Degree-eight nonmetabelian follow-up: G.23–G.24

## Result and exact remaining obligation

G.23 and G.24 are **Proved**. G.16 remains **Open**. The new work proves that every candidate value of the degree-eight scalar satisfies the universal elliptic group relations to all orders, and replaces an unspecified missing coefficient by an explicit nonmetabelian finite observable. It does not compute that observable on an actual Galois element.

The actual character-(4,4) arithmetic line is still

\[
 \frac{d^3\chi^{(4)}_4}{267840}(A_8+\lambda B_8),
 \qquad
 A_8=\frac{\operatorname{ad}_F^3\epsilon_8}{120},\quad
 B_8=\frac{[\epsilon_4,\operatorname{ad}_F^2\epsilon_4]}2.
\]

Its existence and uniqueness follow from G.15–G.16, with the previously corrected theta-character normalization. The new argument neither changes that normalization nor uses the local Coleman–Ihara scalar to infer a second coordinate.

## G.23: universal equations do not select the arithmetic scalar

Enriquez (2014, Proposition 4.19, equation (48), Sections 4.7–4.8, Proposition 4.20) supplies an actual subgroup inclusion of the exponentiated epsilon-generated positive Lie algebra into the graded universal elliptic Grothendieck–Teichmueller kernel. Both A8 and B8 belong to this algebra by SL2 and bracket closure. Therefore

\[
 t\longmapsto\exp(t(A_8+\lambda B_8))
\]

is an actual one-parameter subgroup for every lambda in Q5. This statement is stronger than a finite truncation or a tangent-space calculation. It uses the proved inclusion, not a conjectural assertion that this subalgebra generates the whole kernel.

Both vectors have CM character (4,4), are fixed by the order-four diagonal CM symmetry, and are negated by interchange of x and y. The full diagonal torus normalizes each candidate line. Moreover, every exact lift of the finite CM group into its characteristic-zero prounipotent extension is conjugate to the linear lift. The proof averages on each successive central vector layer, then takes the convergent product of positive-degree corrections. Such conjugation leaves the leading degree-eight term unchanged. Consequently even exact finite CM transport, together with all universal group equations, does not select lambda.

This is a statement about the universal algebraic group. It does not identify an actual Galois subgroup, the CM value of an analytic elliptic associator, or a Tate-to-CM comparison path. Those may impose further arithmetic conditions.

## G.24: exact saturated ambient lattice and two measurable coefficients

Set

\[
 w_0=x^5y^4,\qquad w_1=x^4yxy^3,
\]
\[
 \alpha(D)=-[w_0]D(x),\qquad
 \nu(D)=[w_1]D(x)+4[w_0]D(x).
\]

The exact associative calculation is:

| Coordinate | A8 | B8 | C8=A8+(31/20)B8 |
|---|---:|---:|---:|
| [w0]D(x) | -1 | 0 | -1 |
| [w1]D(x) | 49/20 | 1 | 4 |
| alpha | 1 | 0 | 1 |
| nu | -31/20 | 1 | 0 |

All standard Lyndon coefficients of C8 and B8 have denominators among 1, 2, and 4; both are special derivations. The integral coordinate pair (alpha,nu) is dual to (C8,B8). This proves the exact saturated **ambient** lattice

\[
 (\mathbb Q_5A_8+\mathbb Q_5B_8)
 \cap\operatorname{Hom}_{\mathbb Z_5}(H,L_9H)
 =\mathbb Z_5C_8\oplus\mathbb Z_5B_8.
\]

It is a lattice statement about the two-dimensional universal geometric plane. It is not a statement about the full three-dimensional ambient middle-character space or the saturation of the actual arithmetic image.

For an actual eighth-Johnson Galois element sigma,

\[
 \alpha(D_8(\sigma))=\frac{d^3\chi^{(4)}_4(\sigma)}{267840},
 \qquad
 \nu(D_8(\sigma))=\alpha(D_8(\sigma))(\lambda-31/20).
\]

Thus one actual value with nonzero alpha determines

\[
 \lambda=31/20+\frac{\nu(D_8(\sigma))}{\alpha(D_8(\sigma))}.
\]

The selected words isolate character (4,4), so no spectral projector is needed. Nonzero arithmetic alpha follows from G.15, but its image may be a proper 5-power ideal: no unit value or integral image index is claimed.

### Characteristic finite quotient

Choose free pro-5 generators a,b lifting the integral homology basis. For every r the quotient of the completed group algebra by (5^r,I^10) is characteristic. In Magnus variables it is

\[
 (\mathbb Z/5^r)\langle X,Y\rangle/(X,Y)^{10},
 \quad a\mapsto1+X,\quad b\mapsto1+Y.
\]

The image of the group is a finite 5-group. If sigma is in Johnson degree eight, then sigma(a)a^{-1} starts in degree nine; its leading Magnus term is exactly D8(sigma)(X). The two displayed word coefficients therefore give alpha and nu modulo 5^r, with no logarithm and no division by 5.

The executed program constructs actual products of standard Lyndon group commutators modulo 125, checks their leading terms against their Lie polynomials, and uses them as central corrections to a,b. For C8 and C8+B8 the measured pairs are respectively (1,0) and (1,1). The inverse substitutions and peripheral commutator preservation are checked. These two finite automorphisms are ambient witnesses of detectability; they are not asserted Galois elements.

## Nonmetabelian source inspection and its exact limitation

Enriquez's Section 7.5 gives explicit total-degree-eight iterated Eisenstein Mellin formulas, but they are full cusp-to-cusp integrals. They do not supply the specialized CM comparison coefficient needed here. No numerical or period guess is assigned to lambda.

Malkin (2020, Theorems 11 and 16) is a genuinely depth-two CM source: it proves second-shuffle Hodge-correlator and Bianchi-complex results. Its Section 2.2.3, Lemma 3 and the following paragraph, explicitly conditions the passage to motivic and ell-adic realizations on its motivic formalism and regulator-injectivity hypothesis. The construction also averages basepoints on a torsion-punctured curve; the remark after Theorem 15 explains why this differs from a fixed-basepoint construction. An exact comparison to the specified once-punctured tangential etale action is missing. Therefore this source does not give an unconditional arithmetic value of nu.

The already inspected local Coleman–Ihara formula remains metabelian. Its specialized scalar -6048 and its normalization caveats are retained unchanged in G.16; it annihilates B8 and therefore cannot evaluate the second coordinate.

## Saved artifacts and review targets

- `sections/g_degree8_nonmet.tex`: complete statements and proofs G.23–G.24; input from `sections/G.tex` immediately after G.16.
- `code/g_degree8_nonmet.py`, `.json`, `.out`: executed exact derivation and actual group-word certificates.
- `sections/G_nonmet_results.json`: two Proved result rows.
- `sections/G_nonmet_coverage.json`: the proved universal obstruction and precise remaining arithmetic and source-comparison obligations.
- `sections/G_nonmet_readings.csv`: exact opened primary-source passages.
- `sections/G_nonmet_refs.bib`: verified Malkin preprint entry. The existing Enriquez2014 entry in B_refs.bib is reused rather than duplicated.
- `code/g_nonmet_metadata.py`: regenerates only the companion result, coverage, and reading ledgers; it does not run root metadata or the assembler.

The proof review should distinguish three levels: all-order membership in the universal elliptic group, the saturated ambient integral lattice, and the still unevaluated actual arithmetic image. Only the first two are proved in this follow-up. Root assembly and checkpointing are untouched.
