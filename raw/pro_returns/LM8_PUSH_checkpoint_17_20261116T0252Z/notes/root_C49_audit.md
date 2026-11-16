# Root complete audit of the actual level-24 and level-60 frames

**Verdict: PASS.** Root read the entire 281-line C.49 draft and all331
lines of its exact program. The whole program was executed independently
without invoking its writer; its entire JSON is byte-identical to the
author's result. Root also read the complete independent FGH audit and
freshly opened the exact Tate-curve primary source. Integration is approved
within the stated multiplier-one scope.

## Genuine local coordinates and their actual lifts

The Eisenstein and Gaussian bases agree with the specified signed
matrices: omega=-R and i=S. Their two norms are respectively
a^2-ab+b^2 and a^2+b^2. For the Eisenstein ring, a odd and b even,
norm one modulo eight forces b zero modulo eight; each odd a modulo
eight is permitted. The displayed polynomial for b=8c has an odd
derivative and a root modulo two, so all four residues lift to actual
2-adic norm-one units. After fixing the single global sign by reduction
modulo four, exactly the scalar residues1 and5 remain.

In the Gaussian ring, the exact norm equation first forces b divisible
by four and then a congruent to plus or minus one modulo eight. The
second restriction uses reduction modulo sixteen and cannot be recovered
by merely enumerating norm-one pairs modulo eight. The two displayed
Cayley parameters, with their two signs, lift all four permitted signed
residues. The normalized image is exactly1 and1+4i. At the odd primes,
scalar square-root correction of the norm gives an actual lift of every
norm-one residue, including at the ramified Eisenstein prime three.

The modulo-three and modulo-five ring computations give the asserted
cyclic factors of orders six and four. Chinese remaindering with the
fixed 2-adic sign gives paired image orders96 and576. The realization
step is C.20's actual adelic surjectivity. The finite ring enumeration
alone is not used to assert a full gentle lift. The sign in each CM
coordinate is one global sign; the two coordinates may choose their
signs independently of each other, but not independently at each prime.

## The signed cubic frame and shear constraints

For multiplier one the actual pure cubic frame lies in F'. Its
abelianization is fixed by the order-three peripheral action; the
determinant-three relation is injective on the full profinite integer
lattice, so that abelianization is zero. This is the exact primitive
calculation in C.26, preserved under the marking and inverse changes.
The signed pure image modulo four is abelian and omits -I. Thus the
actual cubic frame is I modulo four. Combining it with the genuine
CM coordinate chosen to be I modulo four makes the lower-right-one
intertwiner itself I modulo four and fixes the global sign in A=VT^-1.

The source and commutator images are computed from the literal U^2 and
S U^2 S^-1. They have orders768/16 at24 and11520/960 at60. The derived
image is the full product of its displayed local projections. The
order-eight projection at three is Q8: it has one nonidentity involution,
and SL2(F3) has no element of order eight, as also follows directly from
its three possible traces and determinant-one characteristic polynomials.
This removes any possible confusion with a cyclic group of order eight.

At eight the cubic coordinate is scalar, forcing the shear to be zero
modulo eight. At four the same argument forces zero modulo four.
The modulo-three quotient by Q8 sends R to the inverse class of U,
so A=VT^-1 requires t+k=0 modulo three. There is no condition at five,
where the source commutator image is all SL2(F5). At24 the constraints
determine the shear uniquely from the cubic coordinate. Since every
CM pair is actually realized, these necessary constraints also determine
the full actual framed image at that level.

## Actual arithmetic realization of the extra C5

Root reread the Tate normalization in the canonical C.20 proof and
freshly opened Milne, *Elliptic Curves*, second edition, III section3,
equations(23)--(26), printed pages102--103. The exact opened passage is
`turn1267view0`, from https://www.jmilne.org/math/Books/EC2.pdf;
`turn1261view0` and `turn1264view0` record the preceding retrievals.
The integral power-series identities and Tate uniformization support the
formal parameter calculation used here.

In the fixed tangential coordinate of C.20, the parameter is
q=z^2/256 times a formal unit with constant one. Its compatible n-th
root has constant factor2^(-8/n). The prescribed tangential splitting
fixes z^(1/n) and the unique formal unit root with constant one.
The remaining arithmetic factor therefore gives t=-8 kappa_2 in the
normalized representative. A compatible torsion-basis change alters
the shear by a cyclotomic coboundary, which vanishes on the
multiplier-one subgroup; the single quadratic twist disappears in
the projective normalization. The draft does not silently change the
specified tangent or permit different primewise signs.

The splitting field of X^5-2 has group C5 semidirect C4: Eisenstein
gives the degree-five field, coprimality with the cyclotomic degree
four gives the full degree twenty, and the cyclotomic action on the
root translations is faithful. Its derived subgroup is C5. The actual
closed derived Galois subgroup therefore maps onto this C5, proving
surjectivity of kappa_2 modulo five on G_Qab. The coefficient -8 is
a unit modulo five.

The paired arithmetic CM image at60 has order288, which is prime to
five. If this nonzero shear character vanished on the kernel of the
paired image, it would factor through a group of that order, an
impossibility. Thus the actual arithmetic subgroup realizes every shear
modulo five while fixing both level-sixty CM coordinates. Multiplication
by these actual arithmetic elements supplies every remaining shear
above each actual CM pair. This proves full realization; finite source
compatibility is not being substituted for it.

## Group law, arithmetic subgroup and character conclusion

On H=ker(lambda), the shear is additive and the two genuine CM
coordinates multiply. Their sign normalizations are multiplicative.
At60 the shear kernel is12 Z/60, a C5, and choosing shear zero modulo
five gives an explicit splitting over the paired coordinates. At24 the
shear is already a homomorphism of the CM pair. This proves the framed
direct products and orders96 and2880.

The signed parity is k+l modulo two and factors through level twelve.
Every finite parity-zero CM pair has an adelic lift, and that lift has
the same zero parity. C.20 therefore identifies it with the arithmetic
paired image. The independent arithmetic C5 supplies the full framed
kernel at60. Equal parity in C6 times C4 is a cyclic C12 generated
by the two rotations together. The remaining factors are unrestricted,
giving arithmetic orders48 and1440 and the displayed direct products.
The quotient is C2 in both cases, so its finite-order character group
is exactly the trivial character and the one indicated parity character.

## Executed program and scope

The exact replay checks the finite pure and derived groups, genuine
local lifting conditions, every allowed shear, cyclic product generators,
arithmetic kernels, raw signed-frame recovery, all residue evaluations,
and finite corroborations of the separate all-depth local lift proofs.
Source SHA-256 is
`fdb8d0e1f8af51336e5e67681dcd825f914ff75bd5972e8eb2c2a6d47179dce5`;
the whole byte-identical JSON has SHA-256
`2eb7b7cf299f7a467fc985825015de3ac9a0ceb7c0e53a752b14779b71c85db3`.
The replay source, full result and verification ledger are retained.

These are exact actual images on the multiplier-one group and its
G_Qab subgroup. The proof does not state an order for the arbitrary-
multiplier framed image, classify every character of the whole gentle
group, or find a smallest finite detector. In particular the extra C5
at60 is a shear coordinate and must not be conflated with the paired
CM image. The draft preserves these distinctions and addresses exactly
the named frame-level calculation.
