# Root complete audit of the all-depth D.93 elementary divisors

**Verdict: PASS.** Root read the entire stable addendum, its entire
symbolic/moment certificate and the independent PBC audit. The full
certificate was independently executed and its complete JSON agrees byte
for byte. The all-depth integral proof is valid and may be merged into
the already audited original D.93, preserving both earlier drafts.

## Exact integral kernel and homology sequence

Multiplication by u^3 intertwines the actual weighted action
chi S_chi(t)^3 sigma_chi with chi sigma_chi. Over a characteristic-zero
splitting field its kernel is supported only at t=1. Since the integral
group ring is torsion-free, this implies u f=0 integrally; its literal
coefficient equations identify the kernel exactly with the integral norm
line. On that line the action is chi^4. Thus the displayed short exact
sequence retains an actual integral norm generator.

The augmentation pieces of the target modulo I^3 have tame characters
chi, chi^2 and chi^3, including any finite five-primary torsion. Their
order-four averaging operators vanish, so their full Gamma homology
vanishes. It follows that the I^3 target has the same H0 and H1 as the
full weighted permutation module. Its H1 is zero: after tame averaging
the procyclic resolution identifies it with the actual invariants, and
twice a finite permutation has no fixed vector over Z5. Equivalently,
the pro-five generator has a scalar power of two times a finite
permutation, with no eigenvalue one, and the tame invariants give the
same conclusion. Consequently the norm coinvariants inject, with exact
order five, into the wanted compact kernel.

The basis orbits of doubling give one cyclic quotient C_(5^j) at each
exact additive order5^j. The zero orbit contributes nothing because
its scalar two minus one is a unit. This proves the precise extension
of the sum of these cyclic groups by the retained C5 norm class.

## Literal lift and integral polynomial subtraction

Root expanded the proposed identity directly. For
G=-1-u/3+2u^2/21 and f=4(t+3)/21, one has
u^3 f=t+(2 sigma-1)G as an unrestricted polynomial identity.
All denominators are units at five. Thus f lifts the largest orbit
generator in the exact extension.

Let ell=4 times5^(r-1), c=2^ell-1 and n=5^r. The orbit-sum identity
is used in the actual group ring, where t^(2^ell)=t because n divides
c. It is not asserted in the unrestricted polynomial ring. Before
passing to that ring, the first three u-coefficients of the sum plus
cG are calculated from the exact geometric sums S2,S3,S4. Direct
expansion gives h1=(c+c^2)/3 and
h2=-c/42+c^2/21+c^3/14, as in the draft. Both are divisible by n
in Z5.

The definitions of W0 and W1 therefore give integral coefficients.
Subtracting (t^n-1)(W0+W1 u) cancels the constant, linear and quadratic
coefficients exactly and produces an integral polynomial u^3 Z.
The two relevant binomial coefficients have valuation r, since their
denominators2 and6 are units and n-1,n-2 are units at five. Hence
Z(1)-h3 is divisible by n. This argument is valid for every r; the
polynomial may be very large, but no finite truncation is substituted
for its existence or its exact low coefficients.

## The highest cyclic factor is a nonsplit extension

Applying the intertwining identity proves that c f-(B-1)Z lies in
the exact integral norm line, so it equals k Norm with k in Z5.
Evaluation at t=1 gives n k=16c/21-15Z(1). Replacing Z(1) by h3
changes the right-hand expression after division by n by a multiple
of five. The S2 and S3 contributions also vanish modulo five after
that division. The S4 term leaves 2c/(3n). Consequently
k is congruent to2c/(21n), hence to1 modulo five, because c/n is3
modulo five. All quantities being reduced are integral at five.

The coefficient is a unit and the norm class has exact order five.
The lift f therefore has exact order5^(r+1), not merely a determinant
consistent with that order. This is the essential extension calculation
that the first two Smith examples alone could not establish.

## Splitting the lower factors

After scaling the highest lift so that5^r x_r equals Norm, an arbitrary
lift x_j of the j-th smaller quotient has5^j x_j=a_j Norm. Subtracting
a_j5^(r-j)x_r kills that multiple. Its new quotient still has exact
order5^j. These changes are valid triangular automorphisms of the
mixed-exponent quotient: the multiple of the larger cyclic generator
defines a homomorphism from the smaller cyclic factor. The highest
lift also generates the kernel Norm, so all modified lifts generate
the whole module. Their product of orders equals its exact order from
the short exact sequence. This proves the direct-sum isomorphism

S = (direct sum of C_(5^j), 1 <= j < r) plus C_(5^(r+1)).

The r=1 case has an empty first sum and gives C25, as required.
This is a full integral elementary-divisor proof for every r.

## Executed certificate and scope

Root read every line of the certificate, including the explicit
five-adic residue operation, then called its read-only run() function.
All symbolic identities and all eight exact moment levels passed;
the entire output matches the author JSON. Source SHA-256 is
`3d9b3759bf0f9c47fea68b738b271cdafbfa64cd4ebbf6d753d0edd38f52e004`.
Output SHA-256 is
`721fb2829e29360c46a4a5e46cf8cffa2f2480b46471a635e837c35d86997dd1`.
The initial failed use of an ordinary rational modulo operation and
its corrected predicate are separately retained by the author.
The corrected predicate uses reduced rational numerators and the inverse
of the denominator modulo five, so it tests the intended five-adic residue.

The computation corroborates the exact polynomial identities and moment
formulas. The proof above supplies all depths and the nonsplitting; no
pattern is extrapolated. The original actual arithmetic reduction,
natural zero map, section-fibre existence and scope restrictions of
D.93 remain in force. This refinement adds no general section-image
classification or higher-derived lifting assertion.
