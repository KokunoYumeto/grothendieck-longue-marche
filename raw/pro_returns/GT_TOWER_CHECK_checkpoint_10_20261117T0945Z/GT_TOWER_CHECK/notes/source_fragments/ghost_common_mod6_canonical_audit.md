# Independent audit of the genuine mixed-modulus-six survivor

Reviewed `centralizer_common_mod6_canonical_survivor.tex`, CMC.1–17,
and its mathematical programs on 2026-11-17. Result: **PASS**.
This audit verifies the full normalized gentle lift, not just the
finite affine equations.

## 1. Actual common-source automorphism

The affine census was independently replayed from the actual source
spanning tree and the two coefficient projections. It gives the three
base states0,255,256, eight frame records each, ranks81 and80 in the
97-dimensional binary and ternary common modules, and twelve records
of each parity. The retained P/L maps and all source automorphism
words were checked anew.

In the row convention, normal form is j*t_a. Its product is
(a,u)(b,v)=(ab,u+v Ad_a+c(a,b)). Conjugation matrices consequently
compose in the reverse order of the corresponding left-conjugation
maps. The selected program uses exactly this convention and verifies
every base-generator edge. Its inverse formula uses Ad_(a inverse),
as required. The cocycle is the literal tree rewrite, rather than a
split-extension substitute.

The mask31 candidate passes both full-source positive-frame equations
and induces an invertible rank97 map at both primes. The identities
P*induced=raw prove preservation of the actual common kernels. CRT
then gives the pure-source automorphism. The frame equations imply
s maps to sf=beta*s*beta inverse and r maps to f inverse*r=A*r*A inverse;
their product is sr. These images give the same source substitution
x maps to x, y maps to f inverse*y*f. The induced S3 map is identity,
so the full E6 map is an automorphism.

The signed-frame inverse in CMC.5 is consistent with the source
enumeration: the retained relation is q_beta=V*W inverse. At rho0,
W_power1 therefore gives beta12=[[9,8],[4,9]], whose mod3 image is
the inverse of the displayed harmonic matrix W3. It still has the
claimed parity one, with T3 identity.

## 2. The full canonical binary model

Let K be the literal rank97 free group and L=K'K². In K/[K,L],
commutation with K' kills gamma3K, and commutation with squares
kills the squares of the basic class-two commutators. Conversely
these relations make every element of L central. Hence

    [K,L] = gamma3K*(K')².

One may also verify independence by the explicit collected group
Z^97 x C2^4656 with the usual upper-triangular parity cocycle. Its
even-exponent subgroup is precisely

    L/[K,L] = Z^97 (generator squares) direct-sum C2^4656.

There is no further finite exponent relation on the square coordinates
at this stage. If an actual generator image has integral exponent row
a, its square has square-generator coordinates a and commutator
coordinates a_j*a_k modulo2. Its pre-existing commutator coordinate
doubles to zero. The commutator action is the mod2 exterior square.
Thus the two actual s,r actions give precisely all [B,L] relations.

The independent full replay reproduces wedge relation ranks2295 and
4641, fifteen remaining wedge coordinates, the209-by112 integral
relation matrix, and multiplier order65536. The selected correction
replay also recomputes the Smith invariants C2^16 and the quotient by
all52 pure s-centralizer corrections C2^5. This is a full integral
canonical kernel calculation, with no omitted higher central layer.

The complete affine-family count uses a quadratic function for a
valid reason: after the computed canonical quotient, the preimage
of K/L is class two of exponent four. Ordered word sections from
binary vectors therefore have integral coordinates modulo4 of
degree at most two; their commutator coordinates are quadratic over
F2. Composing with the affine source sections preserves this bound.
The saved constant, linear and quadratic values determine the entire
binary family, and the program directly checks additional masks.

## 3. The actual full integral correction

The selected defect word is exactly

    beta * sigma(beta inverse * A * rho(A inverse)),

which equals beta*s*beta inverse*A*r*A inverse*(sr) inverse. Thus it
is the cusp defect of the two specified positive lifts. Its full
sixteen-coordinate value and the correction support [0,2,6,8,17]
were reproduced independently.

The actual binary common-source map to K/L is an isomorphism on its
97-dimensional kernel. The program lifts the chosen modular
s-centralizer vector through that map and checks it is fixed by the
common s action. Its common base is identity. Consequently it joins
with the identity ternary coordinate by the actual source CRT map.
Right multiplication of beta by this correction preserves its finite
positive conjugacy and changes the canonical defect by the displayed
kappa_s value. The corrected112-coordinate vector lies in the full
integral relation lattice: all saved Hermite coordinates are integers.
This verifies vanishing before passing to the smaller C2^5 quotient.

## 4. Natural primary comparison and canonical automorphism

The source kernel formula proves the exact maps

    E6 -> B/(K'K²), kernel order3^98;
    E6 -> E3,       kernel order2^97.

All three actual source kernels lie in B'. Since H2(C2*C3,Z)=0,
the integral five-term sequence identifies their canonical central
kernels with H2 of their finite quotient groups. These identifications
are natural for the identity-induced maps from B.

Localizing the actual LHS homology sequence at2 kills all positive
homology of the first kernel, and localizing at3 does the same for
the second. The resulting edge maps are the actual canonical maps
on H2. They give isomorphisms on the corresponding primary parts.
In E3 the selected f and A are identity, so its defect is a central
s-commutator and is killed by2. Its3-primary part is zero. The
verified binary correction kills the other primary part. The group
order of E6 has only prime divisors2,3, so the whole canonical defect
vanishes.

I independently opened the published primary Chapter6 PDF at
<https://math.mit.edu/~hrm/palestine/weibel/06-group_homology_and_cohomology.pdf>
and checked Proposition6.1.10, Theorem6.5.8, Corollary6.5.10,
Theorem6.8.2 and the exact edge/five-term maps in6.8.3 (printed
pp.163,180,195–196). These supply the stated localized homology
vanishing, finiteness, prime support, and natural edge maps.

Conjugating the two torsion generators by the corrected pure lifts
defines a map from B to E6^c. Reduction to the already verified E6
automorphism sends J6 into the central kernel and hence kills
[B,J6]. Its image I satisfies I*M=E6^c. The central kernel is stem,
so M lies in (E6^c)'=I', forcing I=E6^c. This proves a finite
automorphism of the full canonical cover with cusp sr fixed exactly.

## 5. Full lift and normalization

The established finite-certificate image theorem applies to this
actual pure-framed, positive, cusp-fixed canonical automorphism.
It supplies a full profinite positive automorphism with the specified
finite frames. Its raw exponent vector is (-t,t). The retained pure
abelianization is exactly C36², so t lies in36*Zhat. The named x,y
have exact order36 in the retained source, and consequently both
normalizing powers are literally identity there. Thus normalization
preserves the selected finite pair, both frames, and all eight
five-point insertion values. The normalized element is in H, its
retained pentagon is identity in Gamma6, and its retained signed
frames give Delta1.

## Reproduction footprint

Independent executed copies and saved outputs are:

- `ghost_code/review_census_common_mod6_frames.py/.out/.json/.npz`;
- `ghost_code/review_check_common_mod6_automorphism.py/.out/.json/.npz`
  for the original, canonically obstructed affine point;
- `ghost_code/review_check_modular_binary_central_obstruction.py/.out/.json/.npz`;
- `ghost_code/review_check_common_mod6_liftable_automorphism.py/.out/.json/.npz`;
- `ghost_code/review_check_common_mod6_canonical_correction.py/.out/.json/.npz`;
- `ghost_code/review_mod6_exact_comparison.py/.out/.json`.

The final comparison checks all27 arrays in the latter three complete
certificates against the original independently generated outputs,
with exact equality. The failed original point remains archived; it
is not substituted for the canonically liftable mask31 point.
