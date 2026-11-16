# Independent audit of A187

Auditor: local_preprint. Completed 2026-11-16, 15:24 UTC.

Source audited in full: `sections/point3_fermat8_two_primary_selmer.tex`.
Result: **PASS**.

The quartic map is a literal twist of the stated psi-cover: the displayed
inverse, composition with psi, and conjugation by the nontrivial square-root
automorphism all have the correct signs and kernel point. In particular,
the quartic's Jacobian is the dual isogeny curve, and both finite Selmer
sequences have the stated source and target. The complete local upper
bounds in A185 apply to all everywhere locally soluble isogeny torsors;
the actual global connecting images attain those bounds. Both isogeny
Sha kernels, and then the entire two-primary elliptic Sha groups, vanish.

For the Pryms, using the unscaled conjugate targets makes both quadratic
descent maps literal. The pullback sum has connected anti-invariant image,
and its composition with the two pushforwards is exactly multiplication
by two. The opposite composition has zero cross terms because those
homomorphisms are both invariant and anti-invariant and hence have finite
image. Shapiro's evaluation and coset maps commute with every local map,
including the archimedean places. Consequently the asserted exponent two
for each Prym Sha group follows through the actual maps.

For the specified A182 isogeny, multiplication by its kernel order
descends through the finite quotient and defines the claimed inverse up
to that integer. This gives the stated, explicitly degree-dependent Sha
exponent. The finite multiplication sequences then give exactly the
displayed transition image. The continuous comparison uses finite
cocycle orbits and finite sets of cobounding zero-cochains; all finite
strings extend from the highest level, so compactness supplies the
required compatible representatives. No unproved fixed-ramification
comparison is used.

The final section consequence uses the actual compactification and
Abel--Jacobi maps, including the vanishing of horizontal cusp inertia.
Its conclusion is precisely the completed rational two-adic Jacobian
image; no identification of an ordinary local centre with a rational
curve point is made.

Independent execution:

`python work/code/point3_fermat8_two_primary_maps_certificate.py`

All four retained checks passed: the psi-torsor maps and cocycle;
both reciprocal quotient involutions; the integral Prym multiplier and
cross-term cancellation; and the complete displayed map certificate.
The arithmetic inputs are the already independently audited A185 and
A186 certificates.
