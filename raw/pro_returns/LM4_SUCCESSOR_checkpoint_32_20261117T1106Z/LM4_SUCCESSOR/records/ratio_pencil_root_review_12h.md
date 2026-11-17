# Root review of the common polynomial pencil certificate

16 November 2026. We read the complete crossing engine,
`quadratic_pencil_braid.py`, the geometric audit,
`audit_pencil_geometry.py`, the complete transporter extractor,
`extract_pencil_transports.py`, their genuine outputs, and the two
comparison notes. This review concerns the six initially computed
loops. The additional filled loops being computed later require their
own resulting records; they are not silently included here.

## Crossing equations and interval bounds

The candidate equations are complete. For a quadratic root with
projected real offset h, writing its square as A+iB gives
4h^2(h^2-A)-B^2=0. For two quadratic pairs with a common projected
real component a, put delta=C-A and N=B^2-D^2. Then
N=4a^2 delta, and substitution in
4a^4-4Aa^2-B^2=0 gives
N^2-4AN delta-4B^2 delta^2=0. This elimination is still a necessary
condition when delta=0: no division by delta is used to accept a
crossing. The subsequent exact order comparisons reject extraneous
solutions. The pair's self-crossing requires B=0 and is likewise
checked by order rather than accepted unconditionally.

The engine isolates every interior real candidate by rational Sturm
intervals. Overlapping candidates are checked to have a common root,
and non-disjoint simultaneous crossing pairs are rejected. A
principal-square-root discontinuity is corrected at each negative-axis
crossing of odd multiplicity. The height enclosure is taken from a
sample before the isolating interval, with a uniform analytic
derivative bound. The radicand bound |U|>10^-8 gives
|d sqrt(U)/dx| <= 5000 |U'|; the code checks the polynomial
coefficient bound used for the stated derivative constant. Rational
strands have smaller elementary derivative bounds from |t|<5 and
the displayed coefficient bounds.

Branch labels may be restarted at a polygon vertex. This does not
change braid concatenation: the word acts on ordered strand positions,
and the endpoint configuration is the same. The claimed purity is
separately checked on the concatenated word. The extractor then uses
the single initial marking and its actual whisker word.

The rational coefficient replacement is justified along the specified
paths by the residual and radicand lower bounds. The separation bound
uses the quadratic residual as a product of two distances, with the
second distance bounded by 50. Distinct quadratic factors have
residual (t-1)(q_i-q_j). Thus the bounds cover all rational/rational,
rational/quadratic, same-quadratic, and distinct-quadratic pairs. The
coefficient motion is smaller than the pair separation. This proves a
homotopy of these configurations on the paths; it is not a claim that
the entire rationally deformed discriminant arrangement is unchanged.

## Actual source and based marking

The finite-cover comparison uses an exact fact. If a cover character
of a space factors through filling U, its deletion kernel lies in the
cover subgroup, and equals the deletion kernel between the
corresponding covering groups. The same statement for actual full
completions follows from finite-index subgroup embeddings. It makes
no assertion about the abstract completion of an infinite-index
deletion kernel. Both characters in the displayed coordinate
comparison have this factorization.

We requested two clarifications before formal acceptance. First, the
written original-source polygon uses the distinguished root
zeta=exp(2 pi i/5); its asserted positive imaginary endpoint bound
does not hold for every choice of zeta without changing the polygon.
The producer confirmed that this is the actual original choice and
will state it explicitly. Second, adjacency of the merging pair does
not by itself specify a based meridian product. The formal comparison
must choose their disk, its common whisker, and the standard Artin cut
system, transporting every other whisker outside that disk. The
special boundary meridian then maps literally to ab with the chosen
orientation. The producer agreed to make this construction explicit.

The extractor verifies the local triple full twist by its complete
Artin action, verifies both inverse substitutions on all twenty
generators, and computes literal based conjugators. These steps do
not equate peripheral pair-normalization with normalization of the
whole source kernel.

## Independent review of B.77

We read the full formal proof in `work_CE/B_four_triple_gap.tex` and
the associated research note and genuine output. The triangular
Nielsen basis, the reduction of the local central-product relations
to the automorphism eta, and the identification
(A semidirect Z)*F10 are correct. The finite S4 certificate separates
the retained conjugate of a deleted meridian from the source S3.
Its continuous extension proves the claimed actual-image profinite
failure in the partial group. The actual base1 monodromy does not
admit an inner implementer on this tuple, so the certificate is
explicitly excluded as a counterexample to the full pencil.

Review result: the six-loop algebraic certificate and B.77 are
accepted with the two based-marking clarifications just specified.
Uniform normality in the complete actual pencil and the full
icosahedral centralizer decision remain Open.

## Completed review of all thirty-one lassos and B.78

We subsequently read all of `all_filled_pencil_braids.py`,
`audit_complete_pencil.py`, their genuine successful outputs, and the
complete B.78 proof, including its final actual-image equivalences.
The source choice zeta=exp(2 pi i/5), the marked merging disk, its
common cut, and the pullback convention are now explicit. The
swept-square relation explains why positive section conjugation is
the inverse transport used by the recorded Artin action. Both root
and CE independently accepted this comparison.

The additional discriminant centers are
2(1-q) plus or minus 2 sqrt(q(q-1)). The recorded bounds |q|^2>9/10
and |q-1|>1 control these square roots uniformly during the coefficient
deformation. The rational functions defining the other centers have
the same lower denominator bound. Their perturbations, including
rounding to thirty decimals, are therefore below the stated10^-25.
The maximum parameter bound is now10; the puncture bound50 gives
pair separation10^-14, while the radicand perturbation is below
44 times10^-30. The square-root displacement is consequently below
10^-22. These are sufficient for the same configuration homotopy.

The exact lasso audit checks a squared distance above10^-5 from
each straight whisker to every other center, whereas a critical
square has half-side10^-3. The centers have pair distance above
10^-2 and every pair of straight whisker directions has nonzero
determinant. Thus the squares and whiskers give the asserted
distinguished system. An entry segment meeting its own square can
be adjusted inside that square; this changes no lasso class and
meets no other critical point or whisker. The full155 forward
segment records cover all31 loops; their returns use the exact
inverse whisker braids.

The far-point section in B.78 is valid on the full base. A monic
quadratic bound gives root modulus at most2|t|+3, and the rational
punctures satisfy the same coarse bound. The section
100 max(1,|t|/10) exceeds these bounds and is exactly100 on every
certified loop. Van Kampen therefore supplies all620 listed
relations, including the retained base actions, with no special-fiber
surjectivity assertion. The full-completion kernel is the closure
of the actual discrete filling kernel by right exactness of
completion; the compact source-kernel image is likewise the closure
of its actual discrete image.

The proof that entire-kernel b-normality implies full normality is
valid: H and b generate the generic fiber, and every forgetting
monodromy preserves that fiber's normal closure of the U meridians.
Its converse is immediate. This is an equivalence of the exact
remaining conditions, not a proof that either holds.

Review result: B.78 accepted. The formal paper was integrated and
compiled with all eighteen display closers repaired before its
first twelfth-hour build. No mathematical repair was needed after
the independent review.
