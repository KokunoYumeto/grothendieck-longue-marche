# Independent root review of B.61

Reviewed 2026-11-16 05:19–05:20 UTC against the complete formal
statement, the common-base certification code and output, and the
independent integral-word evaluator.

## Outcome

The scoped theorem passes review: the two actual subgroups have a
nonzero common image through nilpotency class three, and that image
vanishes in every rigid-seven quotient through that class. It is not
an element of their full intersection. The distinct actual words
have discrepancy in gamma4(P).

## Marking and arithmetic

The degree-eight field computation compares all labelled points
after the same normalization at labels2,4,6. The cyclic root
perturbation is accompanied by a genuine homotopy estimate. Although
the perturbed moving–fixed collision parameters are ratios of
perturbed roots, the difference of the actual point coordinates
changes by at most8 times10^(-7), uniformly for |v|<7. The certified
distance to the actual root positions is larger than that error.
Moving–moving and normalizing pairs remain separated. The interval
calculation supplies crossing-free identifications from the exact
algebraic base to the rational bases, and both braid transports use
the appropriate inverse directions. Thus the comparison is at one
actual marked configuration, not just at equal abelianizations.

The Artin/Magnus computation is used through degree four to recover
the first three logarithmic derivation terms. The degree-three
free-Lie tower coordinates are reconstructed in full, so equality
is not inferred merely from a projection of the derivation. The
fixed normalized pair has zero linking, which chooses the copy of
the pure sphere mapping-class group in the pure disk braid group
modulo its central full twist.

## Actual integral words

Root reran `next_B59_image/verify_integral_class3_lift.py` successfully;
the independent run finished in25.47seconds. It checked the thirteen
tetrahedral generator powers, seventy-eight commutator powers,
all728 tetrahedral triple powers, and all39 cyclic triple powers.
It verified the vanishing of the first two correction layers,
reconstructed the full990-dimensional third layer, and established
equality of a^D U^(-1) and b0^(2D)V for D=2545920. It also checked
the rigid degree-three cancellation. The common degree-two image
is5091840w, hence nonzero.

The theorem consequently does not depend on treating a modular
rank calculation as rational membership or on inferring integral
words from a rational span. The rational calculations select a
candidate; the displayed integer powers and their direct evaluation
provide the claimed group elements.

The final profinite cyclic injection follows by projecting to the
primitive completed degree-two coordinate: multiplication by the
nonzero integer5091840 on Zhat is injective at every prime. This
justifies the completed-quotient conclusion, not an injection of a
new subgroup into the actual full centralizer.
