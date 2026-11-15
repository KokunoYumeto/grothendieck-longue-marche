# Independent PBC audit of A.50

Auditor: /root/pbc_groups. Completed 2026-11-15, approximately 17:37 UTC.
Draft: notes/fgh_A50_draft.tex.
Outcome: **PASS**.
Exact independent execution: notes/pbc_A50_certificate_rerun.out.

## Actual cover and quotient maps

The division-polynomial divisor has eight simple finite zeroes and
pole order eight at the origin. The cyclic-three cover is connected,
has precisely nine totally ramified points, and genus ten.
The explicit quotient-isogeny formula and the division-polynomial
identity make every displayed translation lift an actual function-field
automorphism. Its third power is one by telescoping.
The resulting order-27 deck group cannot be abelian because the
nontrivial inertia above the single branch point is a commutator.
Its class-two exponent-three presentation is the claimed Heisenberg
group.

The quotient q0 by the order-four automorphism is genuinely degree
four. Its three special target points are exactly the kernel of
1−zeta3, and their full inverse image consists of the nine cusps.
Thus the indicated degree-twelve map and its deck translates are
actual punctured maps.

## Fourier intertwiner and exact detected multiplicity

I checked the F=Q(zeta3) representation, the sign and normalization of
the Fourier intertwiner, and the executed identities
AUA^{-1}=V, AVA^{-1}=U^{-1}, A^4=1, char_A=(t−1)(t²+1).
The trivial-central part is precisely the original elliptic
homology, so the remaining part is a threefold multiplicity of
the rational six-dimensional simple module.

Since tau commutes with the center, it is F-linear.
Writing tau=A tensor B_tau is justified by the M3(F) commutant;
the multiplicity operator has characteristic polynomial over F.
Its i and −i multiplicities agree because i is not in F.
The actual quotient has invariant F-dimension one, so
n1+2k=1 and n1+nminus1+2k=3.
Thus (n1,nminus1,k)=(1,2,0).
The unique invariant vector is consequently a pure tensor of the
one-eigenline of A and the one-eigenline of B_tau.
Its Heisenberg span is exactly one three-dimensional F-module.
The deck translates of q0 therefore detect exactly E0³; no inference
from an arbitrary elliptic quotient's dimension is being made.

The noncentral order-three projector has rank one in the
three-dimensional representation. Thus the genus-four quotient
has the decomposition E times E0 times the SAME surface B,
with the same F action. This bridge is essential for interpreting
the arithmetic counts.

## Exact arithmetic certificate and exclusion of every CM factor

The certificate independently reran successfully, including both
complete quadratic-extension counts:

| p | #D(Fp) | #D(Fp²) | trace E | trace E0 | B polynomial |
|---|---:|---:|---:|---:|---|
| 61 | 96 | 3696 | −10 | −13 | t⁴+11t³+60t²+671t+3721 |
| 313 | 312 | 97872 | 26 | −13 | t⁴+11t³−192t²+3443t+97969 |

I also recomputed the first and second traces from these numbers.
The cube-power identity gives an elliptic quadratic polynomial
squared. The quadratic fields are Q(sqrt(−123)) and
Q(sqrt(−1131)); their ratio 41/377 is not a rational square.
At either prime, the auxiliary roots have norm p and trace 11,
with p not dividing 11. Their ideals have different support,
so their ratio is not a root of unity. Every positive power
therefore remains nonreal and generates the same quadratic field.

The F action is enough to exclude the apparent alternatives:
a CM elliptic factor paired with a non-CM elliptic curve would
give an impossible unital map F to Q; two nonisogenous CM
elliptic factors would both have CM field F and hence be
geometrically isogenous. A geometrically simple CM surface
with F action would have a quartic CM field containing F,
necessarily biquadratic and with an induced CM type, hence
would not be simple. Thus any CM factor forces B to be a CM
elliptic square. After finite extension defining that isogeny,
the ordinary reductions would force its fixed CM field to
equal both displayed persistent quadratic fields. This is
a contradiction; two point counts alone are not being used
as a non-CM criterion.

## Remaining implications and scope

I checked the application of Ruppert's corollary to a rational
Tate-module line fixed by an open derived subgroup: a primitive
lattice vector on that line gives torsion of unbounded order
over the corresponding maximal abelian extension. The absence
of geometric CM factors contradicts this.

For the actual CM target, the nonsplit-prime Frobenius argument
works also at the ramified coefficient prime three; split
coefficient primes are at least seven, and the index (2,2)
satisfies the unit congruence for Q(sqrt(−3)).
The use of the already proved A.12 normalizer derivation
argument is consistent with these hypotheses.

I also checked the independent residue-two reasoning:
the tame cyclic-three normalization has good reduction after
the stated finite constant extension; the special order-four
action remains faithful and has one short orbit. Extension of
q0 to the good elliptic model and preservation of the pullback
line-bundle degree force the special quotient to be exactly
the supersingular E0, not a further inseparable quotient.
The Deuring--Shafarevich computation then gives two-rank zero.
The proof correctly does not turn the all-prime normalizer
classification into an all-prime fixed-subgroup assertion.

## Primary sources independently reopened

- Ruppert, Torsion points of abelian varieties in abelian extensions,
  Section 1, Corollary 1, printed p1:
  https://arxiv.org/pdf/math/9803169 .
  Browser reference turn761view0.
- Ishii, On Kummer characters arising from Galois actions on the
  pro-p fundamental groups of once-punctured CM elliptic curves,
  setup printed p4, Theorem 4.5 printed p18 and Corollary 4.10
  printed p21:
  https://arxiv.org/pdf/2312.04175 .
  Browser references turn761view1, turn762view0, turn762view1.
  The last corollary explicitly gives nonvanishing at (m,m)
  for every m at least two under the stated CM setup.
