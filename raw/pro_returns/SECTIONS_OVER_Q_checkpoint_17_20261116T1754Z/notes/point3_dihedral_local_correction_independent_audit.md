# A210 complete independent audit

Reviewer: local_preprint. Date: 2026-11-16. Result: **PASS**.

Final source: `sections/point3_dihedral_local_correction.tex`.
SHA256: `ab2ae37a199eabca565670bfc314457e85951995aa74c6444b0d95989d425dcc`.
Certificate: `code/point3_dihedral_1129_certificate.py`.
SHA256: `d70d9d57fc8c45b8ec6c08db377295cefce4224f5d4afa6e55b6b10acd1c7771`.
The five missing quad/qquad backslashes were corrected by the author
before this final source hash. No mathematical change was needed.

## Exact arithmetic quotient and inertia

The Hall convention C=[x,y] gives the displayed multiplication
c+c'-a'b, and the actual Ihara conjugating element is central at class
two. Thus the arithmetic action is the literal pure action on x,y,C.
The map x->s, y->r sends C to r^2; its exact kernel is a even and
b+2c divisible by four. The displayed calculation proves arithmetic
stability for every odd cyclotomic character, including the central
action, which is trivial on C2.

The tame identity U phi(V) U^-1=V^q gives exactly
c=(Bm-An)/(q-1)-mn/2 in the same tangential gauge. Wild inertia has zero
pro-two geometric coordinate at q>3. I reread the actual A62 and A207
product formulas: the disjoint new supports have precisely the three
listed valuation vectors, and E=24 n_j(q^2-1)(q^3-1). Hence E/(q-1) is
even and E is divisible by four. This proves trivial D8 inertia for
every global integral class-two lift at every q>3, with no local point
matching assumption.

The completed 24th-root identities allow literal alignment of the
dihedral abelian cocycles with the point-three cocycles. Their central
difference is therefore an actual continuous quadratic character. Its
unramified support condition gives exactly the eight squareclasses on
-1,2,3. All are squares in Q_1129 by the displayed simple-root witnesses.

## Cover, finite sheets, and arithmetic framing

The degree-eight rational map t=((w^4-1)/(w^4+1))^2 has the displayed
deck maps and ramification orders 2,4,2. Its meridian presentation
x^2=y^4=(xy)^2=1 gives the same geometric kernel as the explicit D8
quotient: the presentation has at most eight elements and its image
has eight. This identifies the actual cover, rather than using its
degree alone.

At 1129 all deck maps are rational, and the eight simple point-three
roots trivialize its entire local fibre. This supplies the precise
point-three arithmetic frame. For the residue 828, the two fourth-power
values are squares but not fourth powers, so Frobenius acts on every
sheet by the nonidentity central involution. The two central elements
are fixed by every geometric conjugator. Hensel lifting retains this
whole-disc action and includes all choices of local sheet.

## Continuous correction map

At 1129, the pro-two completion of local units is the root-of-unity
group of order eight. The same 24th-power identities therefore give
equality of the full coefficient-two abelian classes with point three.
The local H0 Tate invariants vanish, so the aligned central difference
is well-defined. Its reduction under the actual central map C->r^2 is
odd by the preceding Frobenius calculation.

The unramified cohomology map identifies the local group with
Z2/(1129^2-1)=C16. A40's global torsor C24 restricts by the literal
fractional coboundary to k->53110k=6k modulo 16. Its image is all even
classes and its kernel has order three. Therefore the twenty-four
global lifts give the eight odd corrections, each three times, and
none matches the ordinary local point. The existing global class-four
lift and the full abelian ordinary matching are retained through their
stated quotient maps.

## Independent execution

Reran the unchanged certificate with all output writes redirected to
a separate temporary directory. All assertions passed: exact Hall
signs, all finite D8 group laws and quotient maps, arithmetic kernel
stability, 37,485 tame parity instances, eight supported quadratic
classes, both complete local fibres, and the exact C24-to-C16 map.
The output/data and source-hash record are retained with prefix
`code/point3_dihedral_local_correction_independent_audit`.

