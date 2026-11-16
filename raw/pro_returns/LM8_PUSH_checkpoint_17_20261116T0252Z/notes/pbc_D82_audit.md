# Independent audit of D.82

**PASS**, 2026-11-15, approximately22:25 UTC. I read the complete438-line
`notes/de_sha_valuation_draft.tex`, its source ledger, its exact certificate,
and the relevant actual-image, boundary-invariant, and raw-character inputs
in D.39, D.77, and D.78--D.81. No mathematical correction is required.

## Actual Kummer and operator images

I freshly opened Nakamura--Sakugawa--Wojtkowiak,
https://arxiv.org/pdf/1410.1045, equations(1.1)--(1.2), printedpage2;
opened source `turn1072view0`. The exponent in(1.2) is exactly a^(m-1),
and the formula is on the cyclotomic kernel. For m=1+4*5^(r-1), Euler's
congruence makes every exponent1 modulo5^r; the product of the primitive
cyclotomic factors is Phi_(5^r)(1)=5. Thus vanishing of every raw odd
character on the actual operator kernel forces kappa(5)=0 there. The
operator first determines chi by comparison on1 and t1, so this use of
the cyclotomic-kernel formula has the required scope. Factoring a continuous
cocycle through the compact quotient is valid because chi also factors.
No global integral high-weight cochain extension is presumed.

The local primitivity argument is independent of a special-value theorem:
over Q5(zeta5), the valuation of5 is4, while zeta5 has valuation0. Their
classes are independent modulo fifth powers. The unique degree-five
cyclotomic extension has Kummer line zeta5, so a fifth root of5 lies
outside it. This proves a unit value of kappa(5) on the local cyclotomic
kernel. Compactness upgrades its image to all Z5. Together with D.78's
actual local surjectivity onto I0, this gives the actual full affine quotient
Z5(1) semidirect Gamma, rather than a formal prescribed image.

The away-five inertia hypothesis is used precisely where two independent
pure translations are needed for the global actual image. The local
decomposition preserves the graph of the descended cocycle kappa(5)r.
It does not incorrectly replace that graph by a zero-translation complement.
The unit-Kummer saturation on ker(rho0) gives exactly the subgroup Z5 z,
including nonprimitive and zero z. D.81's compact-transversal coinduction
therefore still applies to this actual local subgroup.

## Entire restriction kernel, not only its order-five subgroup

On the local cyclotomic kernel, the pair(kappa5,kappa3) has a compact
additive image stable under the actual tame-multiplier operator. Its two
weights are omega and omega^3; their difference is a unit. The integral
projector therefore supplies an actual element with kappa5=0 and primitive
kappa3. D.77's exact three-boundary restrictions then make beta-1=P times
a unit. This justifies the claimed N1 invariants on both R and J.

The additional valuation translation acts trivially on the connecting
module C=PR/PJ because its augmentation is1. Thus D.81's full connecting
module and its chi^5 character remain valid at zero, nonprimitive, exact
boundary, and ordinary unit vectors. The quotient group is now the actual
affine Q, and the proof correctly checks its extra cohomology: the
translation subgroup has H1(lambda)=Q5/Z5(-2), whose Gamma invariants
vanish by the order-four factor. The Gamma cohomology of lambda of weight-1
also vanishes. Hence H0(Q,lambda)=H1(Q,lambda)=0. The injection into
(C^D)^Q bounds the WHOLE restriction kernel by C5.

D.77's exact local invariants are divisible. This makes the extraction of
an order-five representative of a nonzero quotient class legitimate:
subtract a divisible lift of five times a representative. The resulting
functional on J/PJ has nonzero value on P and satisfies all four annihilator
conditions in(D.82.16). In particular the valuation-translation condition
annihilates f_r J, whereas the unit condition annihilates f_z Lambda;
these two different conditions are not silently identified.

## The new exclusions

If the residual valuation and unit vectors are independent, the primitive
unit-line quotient is F5[[z]], and f_r has nonzero linear term. Thus
f_r J=(z^2), which contains P in J^3. This contradicts the functional's
nonzero value on P.

For a boundary line with primitive unit vector, the actual all-depth
boundary test from D.79 applies directly. If only the valuation vector is
primitive, the new intermediate step is sound: restriction to f_r Lambda
factors through f_r Lambda/f_r augmentation. The compact character there
is chi^3, while Cartier invariance requires chi. At an actual k with
chi=2 and kappa5=0, the difference2^3-2=6 is a unit. Therefore the functional
annihilates the entire f_r Lambda and descends to the primitive valuation
line. The same actual-power boundary test now applies. This argument
retains the actual cocycle graph and does not divide by a local depth.

## Nonzero cases and finite-level scope

For residual span zero, the common cubic primitive from D.81 remains valid
because all local translations act trivially on the fixed ten-dimensional
module. For a nonboundary line, the actual stable one-variable quotient
has nonzero cubic P coefficient. Its four-dimensional Cartier primitive
pulls back to the same fixed ten-dimensional module; both valuation and
unit translations vanish there because they lie on the chosen residual
line. The three lower Cartier eigenvalues have unit differences from1,
and the residual tame and cubic operators generate the full residual group.
The written existence argument and the exact finite certificate agree.

The unrestricted ramification step is exactly the audited D.80 argument:
only finitely many away-five inertia vectors survive modulo5; a common
fixed module handles all others; finite local Tate duality/ML kills the
finitely many exceptions at finitely many larger levels, whose maximum
works everywhere. No infinite product is commuted with a filtered colimit.
The global class is nonzero by actual translation coinduction and inflation.
The order-at-most-five bound then gives the asserted exact S_s.

The three compact depths are the valuations of the actual local classes in
the basis(kappa5,kappa6), hence the three minima in(D.82.3). The actual
point t=10 has pair(kappa2+kappa5,2kappa3), independent away-five inertia,
valuation vector(1,0), and unit vector(2,3) modulo5. Its local span is full,
so its compact kernel vanishes. Nonempty fibre and the countable-product
torsor statement are justified by the actual point and the finite-support
theorem D.74. The general local-matrix constructions are explicitly only
Galois modules; no section existence is asserted.

## Independent execution

I ran the exact certificate with `runpy` under a different module name,
without modifying the owner's output. The complete normalized result is
identical to the owner's JSON, not merely its PASS marker. Checked counts:
300 actual twisted residual operators,20 zero-span operators,625 local
residual matrices, and raw moment congruences at levels1--6. Runtime0.974s.
The independent result is in `notes/pbc_D82_independent_rerun.json/.out`.

Certificate SHA256:
`18adb5e10102c53479b325b0ef07371b6266e5b3aca98753b67707f4d40079c4`.
Owner result SHA256:
`809b41ef23bdfccfe21415bb5cf6154e6fb347d952684081edcdb1f03225947f`.

These finite checks do not substitute for the continuous-cohomology and
all-depth proofs audited above. The hypothesis on away-five inertia remains
essential to the stated result; the draft preserves that boundary.

Audited draft SHA256: `ab8317a81b53d5e9b03b4527577dcf23c65a8549bc3f0d61c7deb14c0ca8afb5`.
