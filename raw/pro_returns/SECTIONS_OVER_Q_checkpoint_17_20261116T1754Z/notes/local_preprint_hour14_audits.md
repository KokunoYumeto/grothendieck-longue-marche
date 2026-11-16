# Continued exact comparisons after checkpoint 13

## A180: actual inverse norm fibre

Source: `sections/two_inert_discrete_norm_fibre.tex`.
Certificate: `code/two_inert_discrete_fibre_certificate.py`, with output and data.

The source proves the literal profile map for actual families over −2.
The profile is one integer pair `(c11,c59)`, with divisor
`P0,n+c11 Rmath11,n+c59 Rmath59,n` at every level. The actual functions
`h_q=q/gamma_q^3` give `div(h_q)=3^(n−1)Rmath_q,n`, so the full ordinary
changed-prime classes are three-primary. Full principality is therefore
exactly the simultaneous primary equation `p+c11*r+c59=0` and vanishing
of every prime-to-three component of `P0,n`.

For such a profile the signed generators of rational norm −2 give the
choice-independent defect in the cokernel of
`(u_n) -> (u_n/N u_(n+1))` on the actual norm-one global units. Its
vanishing is equivalent to an actual compatible family, with the
explicit correction `b_n=g_n/u_n`. The source proves the completed
profile image and the exact abstract connecting map
`lim(hat V_n/V_n) -> lim^1 V_n` directly. It does not give those abstract
quotients a Hausdorff topology or replace their actual unit lattices.

The proof also records the exact two-prime primary identity
`[P_f,n]_(3)=f[P0,n]_(3)` using the split orbit in the quadratic closure
and the older inert branches. The induced bound on the primary `P0,n`
does not state a value of its prime-to-three component.

Birational's independent full saved-source audit passed. The certificate
passed both first-field norm identities, 14 divisor heights, all nine
known integer profiles modulo nine, 547 finite class quotient maps, and
25 defect-sign/correction systems. Its two explicitly abstract examples
record the nonzero `lim^1` defect for the integer tower with multiplication
by three and a finite `F7^2` split-orbit module. They are not arithmetic
class data for the tower.

## A178: full independent audit

Source: `sections/metabelian_finite_support.tex`, including A178.22–24.
Certificate independently rerun: `code/metabelian_finite_support_certificate.py`.
Result: eight actual cover graphs, 264 genus/boundary cases, 40 literal
Fermat maps, and 96 composition maps all passed.

The full saved proof passes. The finite-sheet lift retains the actual
local cusp decomposition subgroup; the one-puncture cover has unramified
proper normalization and the stated enlarged boundary. The torsor
pullback supplies finite abelian descent before a rational origin is
chosen. The attached original Harari–Stix geometric-abelian remarks and
Stoll's Theorem BM0/Proposition Inj were read again; they give exactly
the stated descent and inverse-Selmer implications.

The compactification homology maps, nonsplit boundary recovery, fixed
level-three reference injection, and compact conjugator sets retain
their actual arithmetic groups. The common-kernel proof works for both
free and proper surface groups. The added rational compact-Kummer fibre
uses the actual closed immersion into the Jacobian: its fibre over a
rational Jacobian point is a closed subscheme of Spec(k), and a local
point forces it to be Spec(k). The common-cover tangent parameter then
gives the stated full cusp packet without a deck ambiguity.

## A181: evaluated norm obstruction

Source: `sections/two_inert_evaluated_norm_phantom.tex`.
Independent input: `sections/two_inert_one_step_unit_repair.tex`.
Certificate independently rerun:
`code/two_inert_evaluated_norm_phantom_certificate.py`.

The full source and certificate pass. The evaluated target is the actual
unit `U^3` over K1. Its norm images from the first two global-unit levels
are precisely `U^(3 Z3)` and `U^(9 Z3)`. The A159 norm-one S-unit kernel
preserves both nontrivial changed-prime characters of the intermediate
unit U. Thus the target has no completed S-unit preimage in K3. Its cube
is the literal scalar norm of U, proving the exact order-three support
class in both the actual and completed finite-height quotients.

Every finite field-norm test nevertheless vanishes. At the quadratic
changed-prime places, the residue power image at every depth is the cube
subgroup, and the principal-unit power map is invertible. At the linear
branches every unit is a norm. At three the actual root-stabilizer Artin
map gives surjectivity; elsewhere the root algebras are unramified.
The global norm torus has the full decomposition group at three, with
the same explicit lattice and inflation maps as A162.

The inverse-divisor proof over K1 forces every coherent actual or
completed field family over this unit target into the global units.
At the changed primes and at three there is one totally ramified branch.
At every other prime the affine Frobenius orbit argument kills all
coordinates except possibly one fixed branch, which the zero bottom
valuation also kills. Both global inverse fibres are therefore empty.

The two separate norm-kernel systems, their actual-to-completed map,
the exact Milnor injection, the Fox specialization, and the sign
`iota([d_m])=-o` were checked in full. The nonzero continuous class maps
to zero in every finite root-torsor quotient and every `(3^c,T^s)`
coefficient quotient. The finite support class has order three; no
order for the nonzero inverse-limit class is inferred.

Executed counts: 6561 exponent/character checks, 3600 integral divisor
corrections, 726 affine cycle norm maps, 2430 orbit identities, 1092
binomial valuations, 96 coefficient projections, and 1089 root maps.
The corrected unramified norm weights are one, two, and three.

The one-step actual unit repair itself is complete: write the norm-zero
principal divisor as `(sigma−1)D`; replace D's primary class by a divisor
on fixed changed-prime ideals; principalize the prime-to-three remainder;
and apply the displayed Bezout correction. The quadratic transfer is the
literal `v^2/u` formula. It does not assert a multi-step target-preserving
repair, and A181 supplies an evaluated failure of that stronger assertion.

## Retained degree-27 principal relation data

New exact elimination:
`code/two_inert_retained_relation_projection.py`, with output and data.
All 47 retained rows were included. Their 77 outside-S prime labels have
rank 16; the complete rational kernel has dimension 31, and its projected
S-divisor span has rank six. Every projected vector has equal P0 and P2
coefficients. Thus no combination of these particular retained rows can
give the stable divisor `P0+c11 Rmath11+c59 Rmath59`. This statement is
only about the displayed finite relation matrix; it gives no class-group
bound and no arithmetic nonprincipality assertion.

## A182: independent quartic-Prym computation

Code audited and independently rerun:
`code/point3_fermat8_quartic_prym_certificate.py`.
The three equations are `w^4=-12z^3+z`, `w^4=18z^3+z`, and
`w^4=3z^3−2z`. The two finite-field counts, elliptic quotient traces,
reciprocal Prym quartics, and prime-to-characteristic torsion bounds pass.
The three rational Prym torsion orders divide two. The literal rational
classes `[P−iota(P)]=(1−iota)[P−infinity]` have nonzero doubles, since
a principal divisor `2P−2iota(P)` would give a degree-two map from a smooth
plane quartic. They therefore have infinite order. Irreducible Euler
quartics at primes 5, 5, and 13 give Q-simplicity through the actual
good-reduction subvariety factorization. The jet matrices independently
have full rank and correctly impose both points above the fourth roots
`i,-i`. The full A182 source was not yet available at the time of this
finite-computation audit.

## A182 final full source (14:35 UTC)

Read the complete `sections/point3_fermat8_decomposition.tex` and reran
`code/point3_fermat8_decomposition_certificate.py`, including both surface
companions. PASS. Every actual morphism, all21 pulled-back differential
scalars, the good Prym models, rational torsion bounds, explicit infinite-order
points, Frobenius irreducibility, and the full finite-extension Weil
restriction/Jacobian adjunction were checked. No correction requested.

## A183 first integral weight and explicit detecting bound

Source `sections/two_inert_first_weight_vanishing.tex` and certificate
`code/two_inert_first_weight_certificate.py` are complete. Root and Birational
independently passed the proof; Birational reran the certificate. It proves
first weight zero and weight14 nonzero, with actual finite-S and absolute
cohomology maps. Exact primary-source details are retained in
`notes/two_inert_first_weight_primary_audit.md`.

## A184 final full source (14:37 UTC)

Read `sections/two_inert_secondary_unit_character.tex` and reran its
certificate. PASS. The actual Hilbert90 divisor, ideal extension, sigma/tau
maps, persistent anti-character matrix, exact global-unit norm kernels,
secondary map, completed lattice comparison, and shifted inverse-fibre
exclusions all check. No S-unit-kernel or distant-image stabilization was
inferred.

## Retained K3 relation-character continuation (14:43 UTC)

`code/two_inert_retained_unit_character_search.py` evaluates all47 literal
retained degree27 elements at11 and59 by first-field block reduction and
30-digit quadratic Hensel arithmetic. The retained full divisor matrix has
rank22. An exact Smith decomposition with a unimodular right transform gives
the entire saturated integer kernel of rank25. Its local character image is
the diagonal line in F3².

The exact split prime12583 and root v=261 also give every relative norm by
multiplying its nine conjugates. U has primitive order27 residue character.
The pro-three U-coordinate e of each kernel product's relative unit norm is
zero modulo9, and theta3 equals (e/9)(2,2) in every case. This coordinate is a
pro-three coordinate; no ordinary fundamental-unit assertion is used.

These are exact identities in the finite retained matrix and literal local
values. The original full divisor rows remain discovery data; no complete
unit group or negative arithmetic result is inferred. Birational inspected
and passed the local reductions and norm-character witness.
