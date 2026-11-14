# D.64 — Marked compact isometries and actual source corrections

## Proved source extension

There is an actual peripheral automorphism on X64 = X / J64, where
X = Bhat / (R50 intersect L2). The new kernel of X64 -> X63 has dimension
1930 over F2 and fourteen coinvariants. The complete D.57 action and
literal compatible conjugators, the full W_h action, and the established
metabelian and CM maps through W_h are retained. The original cusp is
fixed and the multiplier is one.

The exact new quotient map on the previous kernel is

    Phi64(z) = (q1(z), p2[q2(z)], p3[q3(z)], norm4(q4(z))),

with target C1 + I2 + I3 + norm4(C4) of dimensions 1920 + 4 + 4 + 2.
Here Ca is induced from the actual kernel of Herm(Ma) -> Herm(P*_a).
It is an actual quotient of J63; no splitting of that quotient is
assumed. The proof constructs its surjection by subtracting a
cusp-containing lift of the small affine image. The cusp map is
integrally onto because the marked source loop of width 36 maps to
the cube of the small loop of width 12.

The lower representative can change. Its exact comparison on the full
homology source is

    T64 = T63 + A1*m1 + A4*m4,
    beta_Y(g) = (A1*eta1(g) + A4*eta4(g))*alpha63,Y(g),
    alpha64,Y = Int(b_t,Y) beta_Y.

The derivations are inflated from the actual J_infty source, restrict
to the affine compact projectors on its kernel U, and vanish on t.
Each Aa takes values in the exact saturated kernel L; its conjugator
changes have actual preimages in S57 and zero images in the retained
targets. The cusp-inner word uses all 36 factors for each earlier
E-self correction. The eight new source-involution corrections
centralize the involution on Y and do not change this Y formula.

## Marked intersection forms and both arithmetic branches

The actual integral graph has 576 edges on each twisted coefficient
fibre. Integral cycle lifts are reconstructed modulo four by solving the
actual incidence equation. The signed half-ribbon formula is then
evaluated only after checking that every coefficient to be divided by two
is even. It gives the actual modulo-two intersection form.

Each affine fibre has dimension 96 over F4, cusp rank 48 and compact rank
48. The small affine fibre has dimension eight, cusp rank four and compact
rank four. On every remaining M16 module the form has rank sixteen.
Its restriction to the actual twelve-dimensional kernel of the small
compact map has rank eight, with a four-dimensional radical.

The small form is independently compared entry by entry with D.57's
complete marked 649-dimensional ribbon form, using its actual Fourier
inclusion. Both arithmetic actions are extracted by applying the
complete 649-dimensional matrices to that same inclusion. All eight
framings in each branch have identical complete homology matrices.

For the two old projective compact modules, the full equivariant
isometry spaces are explicit affine F2 spaces of dimensions eight and
six. Every constant, linear and quadratic coefficient of the isometry
equations is retained. The first old orbit uses masks c3 and 0 for
branches one and three, with actual fixed-seed trial counts 62 and 1.
The second old orbit uses mask zero in both branches on trial one.
Direct checks verify the entire pairing equation, all 72 stabilizer
equations, the marked small square, and rank sixteen.

These finite isometries yield actual integral homology corrections.
The integral old M modules are projective. The difference from the
existing homology matrix is an equivariant modulo-two map into the
kernel of the small compact map. Saturation, the literal cusp
surjection, and projectivity lift it to an integral map M -> L.
The new integral homology action is invertible; the form equality
asserted here is its modulo-two compact equality. This is exactly the
coefficient needed by the exponent-two class-two boundary.

## Norms and source maps

The actual compact kernel and its norms are:

| Character | Induced dimension | Coinvariants | Norm rank | Norm kernel |
|---|---:|---:|---:|---:|
| (0,0,0,1) | 1920 | 4 | 4 | 0 |
| (0,0,1,1) | 2880 | 10 | 0 | 10 |
| (0,0,1,2) | 2880 | 10 | 0 | 10 |
| (0,1,0,0) | 1920 | 4 | 2 | 2 |

D.55's unquotiented orientation identity and the actual isometries
annihilate all six compact norm coordinates. Injectivity of the first
norm on coinvariants permits retention of its whole 1920-dimensional
component. The second old orbit contributes its two-dimensional norm
image.

For each new orbit, the actual source-s correction has rank four in
the ten-dimensional compact kernel coinvariants. The full 36-term
cusp correction is zero on every compact kernel. The program checks
238656 polar identities, both factorizations through the actual cyclic
norms, the actual affine source relations, and all 496 real basis
wedge averages. It retains the nonzero translation in the actual
t^18; the pure Q involution with state 314 is not substituted.

The source-s image admits a simultaneous retraction for both arithmetic
branches. Each compatible compact homology family has sixteen binary
parameters. Its exterior coinvariant action has 137 coefficient
matrices per branch; all 274 are retained and tested. The forty-entry
retraction system has rank 34 in each orbit. The same retraction
intertwines every coefficient of both families, so its six-dimensional
kernel is invariant under the actual retained action.

The actual source word is

    b_s = u * s_tilde * u * s_tilde^-1, with u in S57.

It centralizes the source involution on Y, and its exact class-two
defect is [u, s_tilde*u*s_tilde^-1]. The selected four words in each
orbit map to the four standard basis vectors after retraction.
The exact cusp word and wrap identity are also retained:

    b_t = product(j=0..35) t^j*u*t^-j,
    b_t*t*b_t^-1*t^-1 = [u, U1*...*U35] * [t^36,u]^-1.

The cusp factor disappears only after the specified compactification
map. All thirty-six terms remain in the actual source proof.

After these corrections, the remaining defect in the new quotient is
an augmentation vector in the first compact component. The exact
two-conjugator augmentation map cancels it through actual preimages
in J63. The exterior action preserves the literal intersection of
all four quotient kernels. Frattini generation and the retained
common quotient give the automorphism of X/J64.

## Remaining source kernel and scope

J64 = ker(Phi64) is the exact kernel of X -> X64, and the full
source kernel is its inverse image in R50:

    S64 / (R50 intersect L2) = J64.

Its dimension is dim(J63) - 1930; its specified small-character
part has dimension 282230. The remaining kernel is nonzero:
the fourth compact component has a 1918-dimensional kernel of its
norm, and any nonzero vector there has an actual nonzero source lift
in J64 with the other orbit coordinates zero.

The two tested source maps cover eight of the 22 compact norm-kernel
coinvariant coordinates. Fourteen remain in that test. This is not
asserted to be the coinvariant dimension of J64; passage to its
actual kernel can have additional homology terms. Full profinite
GT0 realization and the remaining arithmetic boundary are unresolved.

## Programs, executions and preserved attempt

Six complete programs, with actual stdout and JSON:

1. code/d_residual_compact_norm.py
2. code/d_residual_compact_pairing.py
3. code/d_residual_compact_isometry.py
4. code/d_residual_compact_cusp.py
5. code/d_residual_compact_coin_action.py
6. code/d_residual_compact_extension.py

Each was rerun from its own copied source and exact copied immutable
inputs under d64_author_rebuild/. Every entire JSON and stdout agrees
after excluding only the values named elapsed_seconds.
Derived producer inputs are copied exactly, and each D64 producer is
also freshly executed in its separate directory. This is an author
replay; no peer or parent replay is claimed.

The first isolated extension replay stopped because the retained
generic helper prelude read d_arithmetic_A4_twisted.json without
listing that immutable file in its input digests. The original full
successful source-directory run, its exact source/stdout/JSON, and
the actual isolated failure are preserved under
code/d64_trials/extension_undeclared_input/. The final version
declares the exact dependency; no mathematical field changed.

The seven-page standalone proof uses the paper's existing preamble
and format. Its two final compilation passes, complete page renders,
actual visual review, equation/control lint, and exact hashes are
recorded in audit/. The initial proof/PDF and exact clarification
diff are retained: the clarification makes the derivation's quotient
restriction literal, names theta_U, and uses explicit semilinear
bracket notation.

## Preserved post-word correction

The original complete freeze is preserved in audit/pre_moving_repair/full_tree. After the eight new source-s words, the proof now explicitly removes their possible reintroduced moving component in (1-e_Delta)K. The two-conjugator augmentation map is onto there; its coefficients lift through the exact source R50 intersect L_{*,2}, preserving Y, literal X_* conjugators, W_h, every earlier invariant projector, and all Phi64 coordinates. No computational source or output changed.
