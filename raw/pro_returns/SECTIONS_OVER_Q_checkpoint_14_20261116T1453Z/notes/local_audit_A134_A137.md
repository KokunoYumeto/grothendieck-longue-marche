# Independent saved-source audits: A.134, A.136, A.137

Auditor: `/root/local_preprint`.

## A.134 — completed harmonic twist

Full saved source `work/sections/harmonic_twist_completed_obstruction.tex`
passes.  The audit includes its final explicit prime-repair reciprocity
and its effective choice convention.

The checks cover the actual degree-64 quartic cover and genus-33 proper
model; the common field of degree sixteen and its literal square-root
expressions in every fibre factor; the full finite and large-prime local
point argument; every local invariant, including the real place; and the
exact nonzero character of the global obstruction.  The splitting field
used for prime repair has the stated order-32 Galois group and exact
multiquadratic abelianization.  Its CRT intersection conditions and its
new-prime invariant are justified by actual restriction maps.

For completion, the initial root symbols have zero global sum with the
specified negative real root.  Subtracting the signed rational principal
idele gives precisely the CRT automorphism fixing the first boundary
field.  The negative first coefficient refinement turns the new root
into a principal local square and a positive real root.  This establishes
the individual zero-symbol invariant required by all later mixed-cover
refinements.  The displayed maps preserve each controlled local centre
literally; the factorial exponents are cofinal among all positive
integers.  The fresh coefficient valuations persist and give infinite
support.  The final quadratic obstruction is applied to these actual
completed local data.

Independent rerun of `harmonic_twist_repair_certificate.py` passed all
611 finite centres, 1,833 fourth-power tests, 3,040 unramified root-symbol
checks, common-field/group checks, 295 nonsquare prototypes and the
strict good-prime bound.  The separately retained
`harmonic_root_symbol_independent_audit.py` also checks the signed initial
root data independently.

## A.136 — escaping support on the actual tripod

The source `work/sections/tripod_escaping_support.tex` has also received
a full independent audit by `/root/birational_main`, reported as passed.
The maps use `X=X0 X1`, `Y=Xh²` and `t=4T(1−T)` literally.  The forced
centres and the identity `t+8=−4(T−2)(T+1)` give valuation one at infinitely
many new primes.  At the added boundary `t=−8`, the actual common field
is `Q(sqrt(-6))`; its finite controlled evaluations vanish by the stated
norm identity.  Its conclusion concerns completed coordinates and their
fixed local images; it makes no unsupported section-existence assertion.

## A.137 — actual finite quotient exclusion on the tripod

Full saved source `work/sections/harmonic_tripod_finite_obstruction.tex`
passes.  No arithmetic splitting of the quartic cover is required.

The central extension representing the proper Brauer lift splits over
the free geometric group `H`.  Conjugating this splitting changes it by
a character `H→F₂`, which kills `K=cl(H²[H,H])`.  Thus the extension
descends to `E/K` and the displayed fibre-product map is a topological
isomorphism.  This proves inflation of the actual class.

The retained mod-eight Kummer coordinate first lifts the section to the
harmonic cover and determines the half-coordinate modulo four up to one
global deck sign.  At odd primes where `−1` is not a fourth power that
sign fixes the actual local sheet.  The two-progression fourth-power
detection argument is exact: the fixed-root condition over the
`5 mod 8` Frobenius coset forces a root into `Q(i)`, and the `3 mod 8`
coset removes the remaining `−4` possibility.  The actual quartic torsor
therefore has a fixed sheet on the lifted section.

At every finite place, lift the finite geometric conjugator to the full
geometric group.  Since `K` is contained in the actual cover subgroup,
the conjugated ordinary point section fixes an actual sheet and gives
a point of the quartic cover.  At the real place the same argument
applies to an ordinary point.  For a cusp, the fixed sheet has a stable
inertia orbit, hence gives a real boundary point of the proper cover.
The map to the proper curve kills that inertia, so the proper μ₂ class
pulls back to the Brauer value at that point.  These are the required
exact local comparisons.  Their invariant sum contradicts reciprocity.

The third-derived quotient map is exact by
`Π′⊂Λ`, `Π″⊂Λ′⊂H`, and `Π‴⊂[H,H]⊂K`.
The original order-based lower-central bound is valid and has now been
sharpened as follows.

## Exact class seventeen

Full source `work/sections/harmonic_quotient_class_fragment.tex` passes.
The actual Schreier quotient is
`P=Π/H=(C₄×C₄)⋊C₈`, with the last generator interchanging the first two
coordinates.  Its Cayley covering graph identifies `Π/K` with the
path-chain group; this is an explicit group isomorphism, including its
kernel and surjectivity.  The lower-central seed and recurrence are
exact, and the retained certificate reran successfully.

A separate calculation, not importing that certificate, is retained in
`work/code/harmonic_quotient_augmentation_audit.py`, its `_output.txt`,
and its `_data.json`.  It computes powers of the augmentation ideal in
the actual regular `F₂[P]` module, proves `I^17=0` and `dim I^16=1`, and
checks every coefficient of `(1+t)²(1+t²)³(1+t⁴)²`.  The exact Fox/path
chain proof in `work/notes/harmonic_quotient_augmentation_audit.md` gives
`DΓ_k⊂I^(k−1)`, hence `Γ₁₈Π⊂K`.  A separate edge-by-edge trace of the
196,606-letter weight-seventeen word gives all 128 x-edges and no
y-edges, a nonzero cycle.  Thus the actual quotient has class exactly
seventeen and the arithmetic map through `Π/Γ₁₈Π` is established.

## A.138 — actual compatible units on the fixed pure-three tower

Full source `work/sections/constant_tower_unit_lift_agent.tex` passes.
The finite-three-group normal-generation argument proves total
ramification for every finite Galois three-extension of `Q(μ₃)`
unramified away from its unique prime above three.  Applied to the
Hilbert three-class fields, it proves the asserted class-group
vanishing.  The cyclic unit-norm argument is exact: cyclic reciprocity
gives all local norms, the Hasse norm theorem gives a global element,
and the displayed principal-divisor correction followed by the
prime-to-three Bezout identity makes it an actual unit of the prescribed
norm.  Both paths in the field norm diagram agree.  The half-powers are
used only in the pro-three unit completions and give the stated
compatible completed factors.  The labeled first-depth quotient and
its Frobenius at 61 give the normalized conductor-nine character.
The independent certificate rerun passed every finite check.

## A.139 — the smaller metabelian class-eight detector

Full source `work/sections/harmonic_cyclic_finite_obstruction.tex` passes.
The two models are related by the actual isomorphism

\[
 W^4=\frac{T(T-1)(T-1/2)}a,
 \quad t=4T(1-T),
 \quad W^8=\frac{t^2(1-t)}{64a^2},
 \quad T=\frac12-\frac{4aW^4}{t}.
\]

The product-root map from the quartic old cover is literal.  The
degree-eight cover is geometrically connected; its proper curve has
genus three and four removed geometric boundary points.  The explicit
root expression at `T=c` splits the residue character and the infinity
pole has order four, proving that the Brauer class extends properly.

Every local sheet over the prescribed `x_p` has centre `T_p` or
`1−T_p`; the alternate centre occurs precisely when `−1` is a fourth
power.  Away from the displayed finite support the direct three-case
valuation argument proves zero evaluation on every ordinary point of
the smaller cover.  Within that support the only permitted flips are
at 17 and 1,119,169, and the displayed nonzero square residues give
zero evaluation on both sheets.  At two no flip is possible and the
invariant remains one-half.  The real character is split.

The Nielsen basis `u=xy^-2,v=y` identifies the actual quotient with
`(C₂)^8 ⋊ C₁₆`.  Its Schreier kernel has the nine independent
mod-two classes `v^j u v^-j` and `v^8`, so the kernel of the displayed
group map is precisely `K_D`, not merely a subgroup of it.  On the
eight-coordinate permutation module the lower central recurrence is
`Γ_k=τ^(k−1)F₂[τ]/τ^8` for `2≤k≤8`.  Thus the group has order 4,096
and class exactly eight.  The inclusion `Π′⊂H_D` gives the actual
metabelian quotient map, and the lower central calculation gives the
map from `Π/Γ₉Π`.

The retained combined Kummer class fixes a sheet of the degree-eight
cover.  The same nonsplit central-extension descent as in A.137 gives
the finite Brauer class; actual local fixed sheets and real inertia
orbits give exactly the evaluated local points.  Reciprocity therefore
excludes the stated locally matching section.  No claim about a
metabelian lift without those local images is made.

Independent rerun of `harmonic_cyclic_detector_certificate.py` passed
the 611 actual local fibres and all available flips, all 4,096 normal
forms and 8,192 generator products, and the nonzero weight-eight word.
