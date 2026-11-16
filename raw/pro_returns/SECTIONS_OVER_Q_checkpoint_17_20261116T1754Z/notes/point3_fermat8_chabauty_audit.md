# A189: exact dyadic logarithm and the selected metabelian cover

Source: `sections/point3_fermat8_dyadic_chabauty.tex`.

The arithmetic uses only the first A186 genus-two factor
`y^2=x^5-54x`, its actual point `(3,9)`, and the exact rank-one
completed generators supplied by A186.18--21.  No external arithmetic
service is used.  The earlier exploratory Mumford script is separate;
the final certificate checks the literal doubling divisor identities.

## Main exact calculation

Starting with `U2=(x-3)^2`, `V2=(39x-99)/2`, the displayed Newton
lift of `V` modulo `U^2` gives a cubic `L`.  The identity
`f-L^2=constant*U^2*Unew` proves the actual divisor doubling map.
Two applications produce `8D`.  For the centre `c`, half-root
square `d`, and `V(c+t)=v0+v1*t`, exact valuations are

```
c = 249 mod256
v2(c,d,f(c),v0,v1) = (0,6,0,2,-3)
v2(f(c)/(v1^2*d)-1) = 4.
```

The square root of the last ratio in `1+8 Z2` constructs the
actual square-root branch on the symmetric disc over `Q2(sqrt d)`.
Its endpoints are the first divisor point and the hyperelliptic
negative of the second.  The smooth integral model has x and y
units, with x derivative a unit, so the Neron mapping property
puts their Abel--Jacobi difference in the formal group.  This is
why the termwise curve integral computes the abelian logarithm
even at the bad prime two.

The binomial coefficient identity gives `v2(b_n)>=1-2n` for all
positive n.  Symmetric integration therefore gives logarithm slope
`rho=1 mod4` with nonzero first coordinate.  Integration from
`(3,+/-9)` to any distinct point with `x=3 mod8` gives slope
`3 mod4`.  The all-coefficient bounds, not a numerical truncation,
prove the incompatibility.

## Actual curve and section maps

The map from `3u^8-2v^8=1` is exactly
`x=3u^2/v^2`, `y=9u/v^5`.  Every Q2 point has u and v units;
there are no Q2 points in its three old boundary fibres.  Thus
the local global-Selmer-compatible point set is exactly
`(u,v)=(+/-1,+/-1)`.  Rational points are included in that set,
so this also determines all rational points of the proper curve.

For the tripod metabelian assertion use the actual subgroup
`H=ker(Pi -> (Z/8)^2)`.  The equality of the two finite Kummer
classes makes the section's finite image literally that of the
point-3 sheet after a geometric conjugation.  The inclusion
`Pi'' subset closure[H,H]` supplies the actual arithmetic
abelianized-cover extension.  Compactification and the displayed
curve map give `H^ab -> T2 J`.  Ordinary fixed sheets and cusp
decomposition groups give all local Kummer conditions, as in
A178, so the A186 finite Selmer calculation applies.

The conclusion is the exact dyadic centre three and the global
compact coefficient class `+D` or `-D`.  A full global section
classification is not asserted.

## Opened primary references

1. McCallum--Poonen, *The method of Chabauty and Coleman*, original
   author PDF dated 14 June 2010,
   <https://math.mit.edu/~poonen/papers/chabauty.pdf>.
   Section 4.1, Remark 4.1, author-version page 4, explicitly
   identifies the formal antiderivative on the kernel of reduction
   to the Neron special fibre, allowing bad reduction.  The same
   section gives the homomorphism and its local analytic differential.
   Opened web refs: `turn755view1`, `turn757view0`.

2. Poonen, *Rational points on varieties* (AMS, 2017), author PDF
   <https://math.mit.edu/~poonen/papers/Qpoints.pdf>.
   Theorem 5.7.25 and Proposition 5.7.26, printed page143 (PDF156),
   give the finite-type Neron model over a DVR and the extension
   of a map from a smooth scheme.  These apply to the literal
   smooth unit-coordinate model used above and to its quadratic
   local base extension.  Opened web refs: `turn755view2`,
   `turn756view3`, `turn757view2`.

The bibliography fragment is `notes/point3_fermat8_chabauty_references.bib`.

## Reproducible certificate

`code/point3_genus2_chabauty_certificate.py`, with retained output
and JSON data, verifies both actual doubling functions and
divisor identities; every exact rational valuation; fourteen
symmetric reciprocal-square-root coefficients;128 small-disc
integral truncations; and the eighth-power/unit disc map.

The first completed-generator comparison also has the independent
local PARI certificate `code/point3_genus2_generator_certificate.gp`
and output.  Root's subsequent six-factor certificate gives the
stronger literal square-root witnesses in A186.19--20.
