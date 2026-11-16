# Root complete proof and source audit of A69

**PASS.** The complete uniform argument has been read and independently
re-derived, including its componentwise cases, wild fixed-point lifting,
and rooted-tree count. The explicit map/group certificate was read in
full and independently executed. Its entire JSON is byte-identical to
the author's output: SHA256
`1f6ac2f7dbc17742805b25846a57d2f900ff36572e5029f37ff8394eab8e848f`.
The code SHA256 is
`2636819004d35d370f39c9e7d541f2fb91bca2856312814c5104be724372dc07`.
This certificate checks the supporting algebra; the universal geometric
argument is the written proof, not an inference from its nine samples.

## Claim, actual cover, and arithmetic transfer

For every power of two m at least two, the actual curve is the smooth
normalization of v^2=w^(2m)-6w^m+1, of genus m-1. The displayed degree
2m map lands in the original E and has four cusps, each of index m/2.
Its first factor to E is the Kummer extraction of an (m/2)-th root of
y/(x-1), followed by actual duplication. The divisor of that elliptic
function has four coefficients +1,+1,-1,-1; it proves both the degree
and exact ramification. The rotation and reflection preserve the full
map, satisfy the dihedral relations, and give 2m distinct automorphisms.
The field extension is therefore genuinely dihedral. The extra rotation
mu keeping v fixed is distinguished from this deck rotation.

The m=2 curve is isomorphic to the first elliptic factor, and hence
isogenous to the original E. It has potential good supersingular
reduction at two. The induction therefore starts before any use of
the new contradiction. The plus-six model is carried to the minus-six
model by the stated root-of-unity change after finite extension.

The conclusion is restricted to this actual family and its actual
intermediates. It gives the Task A5 pro-ell fixed and normalizer
assertions at every coefficient prime, through A41, A42 and A59. It
does not give a cofinal family of all finite covers or settle the
full hidden-kernel question. I reread the hypotheses and finite-field
restriction directions in those three comparison statements.

## Exact primary-source scope

The following primary passages were freshly opened by root:

- Lehr--Matignon, *Automorphisms of curves and stable reduction*,
  Section 6 of the Leiden workshop problem collection, Theorem 6.13, published page 154. The publisher PDF is
  https://www.numdam.org/item/RSMUP_2005__113__129_0.pdf . Its text layer
  is garbled; root viewed and read the actual page image. It gives
  potential good Jacobian reduction for a nilpotent Galois cover of a
  good proper curve with generically tame ramification and an etale
  branch closure. Our base has good reduction after finite extension,
  the only branch closure is the origin section, and generic
  characteristic zero supplies the tameness.
- Saidi, *Galois Covers of Degree p and Semi-Stable Reduction of Curves
  in Mixed Characteristics*, published page 662, publisher PDF
  https://ems.press/content/serial-article-files/41001?nt=1 . The passage
  explicitly extends the tree conclusion to a p-group cover ramified
  only along a divisor etale over the valuation ring. No statement
  about the p-rank of a marked vertical fibre is taken from it.
- Crew, *Etale p-covers in characteristic p*, Corollary 1.8, published
  pages 35--36, https://www.numdam.org/item/CM_1984__52_1_31_0.pdf .
  Both actual page images were read. The corollary treats ramified
  finite p-group actions on smooth proper curves by excision of the
  branch points, and gives the Deuring--Shafarevich formula used here.
- Yang, *p-Groups, p-Rank, and Semi-Stable Reduction of Coverings of
  Curves*, Proposition 1.4, author page 8,
  https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/PSS.pdf .
  The same smooth-curve formula is stated explicitly with the sum
  over points of the covering curve. Its separate warning about
  marked vertical fibres is respected by the present proof.

Thus the reduction theorem is used only for compact type. The entire
special 2-rank calculation below is additional reasoning. The earlier
attempt to extend an unramified Raynaud slope statement across the
marked fibre is not being used.

## Primitive factor and special 2-rank dichotomy

The quotient by sigma=mu^(m/2) is exactly C_(m/2), with coordinate
w^2. Pullback and norm give the invariant and anti-invariant isogeny
factors in characteristic zero, with new dimension m/2. The odd
differential eigencharacters are all primitive characters of order m.
In characteristic zero the differential representation of endomorphisms
is faithful, so Phi_m(mu)=0 on the new factor and Q(zeta_m) acts
unitally. Every nonzero mu^k-1 for m not dividing k is invertible
in this field, including after specialization and in every rational
realization.

The factors have good reduction because the full Jacobian does, and
the specified automorphisms are defined after the finite extension.
Endomorphisms extend to the good abelian scheme; rational projectors
are interpreted in the isogeny category. On the rational etale Tate
space of the special 2-divisible group they give a unital action of
Q2(zeta_m), a field of degree m/2. If that space is nonzero its
dimension is a positive multiple of m/2, but is at most dim A=m/2.
Consequently the new factor has 2-rank zero or is ordinary. This
argument does not assume that characteristic-two Hodge eigenspaces
remain distinct, and does not replace an integral special realization
by a formal characteristic-zero character calculation.

## All involution cases on the actual special fibre

The compact-type Picard variety is the product of the component
Jacobians. The actual sigma-action permutes these factors. If two
positive-genus components are exchanged, their invariant and
anti-invariant factors are both isogenous to the same Jacobian.
The first has 2-rank zero by induction; the second would be ordinary.
A positive-dimensional abelian variety cannot have both properties.
The diagonal/anti-diagonal comparison remains an isogeny comparison
in characteristic two: its intersection is finite 2-torsion, not a
claim that the two maps coincide. A component on which sigma is
the identity contributes only to the invariant factor and is allowed.

For a fixed component B with nontrivial sigma, the function-field
quotient B to B' is separable of degree two even in characteristic two.
Pullback and norm identify its invariant factor with J(B') up to
isogeny. This quotient has 2-rank zero. Deuring--Shafarevich gives
f(B)=r-1, where r is the number of fixed points; an unramified cover
would give f(B)=-1 and is impossible. Riemann--Hurwitz gives new
dimension g(B')-1+(sum of different exponents)/2, with each different
exponent at least two. If the new dimension is zero, these inequalities
force a rational component. If it is positive and ordinary, equality
with f(B) forces g(B')=0 and every different exponent equal to two.
Thus all positive components contributing to the new factor are
ordinary and sigma is their double-cover involution over P1.

## Cyclic fourth roots and the orbit length

For a faithful 2-group on an ordinary smooth curve, subtracting twice
Deuring--Shafarevich from Riemann--Hurwitz gives a sum of nonnegative
terms: the quotient genus minus 2-rank and, at each branch point,
the different exponent minus twice inertia order minus one. Since
wild inertia has G0=G1, equality forces G2=1. The coefficient of
t^2 in a local automorphism t+a t^2+... then embeds inertia into
the additive residue field. Its exponent is two. Cyclic inertia of
order four cannot occur at a point.

If an order-four automorphism squared to sigma, it would induce a
nontrivial involution of P1. That involution has exactly one fixed
point. If this point were unramified in the double cover, the
permutation of its two points would have square the identity, whereas
sigma exchanges them. Hence it is ramified and its unique preimage
has cyclic order-four inertia, a contradiction.

For a contributing component with mu-orbit length d, the restriction
of mu^d has exact order m/d. A smaller order would make a power
mu^k, k<m, the identity on the entire orbit's nonzero Jacobian
contribution, contradicting invertibility of mu^k-1. Its quotient
action on P1 has order m/(2d), because the kernel is exactly the
two-element deck group. A 2-power element of PGL2 in characteristic
two has order at most two; the fourth-root exclusion leaves m/d=2.
Thus d=m/2. The total anti-invariant dimension is also m/2, so
there is exactly one orbit of m/2 ordinary elliptic components,
each with exactly two sigma-fixed points.

## Wild smooth fixed-point lifting

This step is proved locally, not presumed from a tame fixed-point
principle. The stable marked action is over R and fixes its coefficient
ring. At a smooth fixed point on a component where sigma is nontrivial,
the local equation sigma(t)-t has nonzero reduction of finite positive
order. Weierstrass preparation therefore makes its fixed locus finite
flat of positive rank. The absence of a vertical factor is precisely
the nonzero reduction condition. Its horizontal points are generic
fixed points of the actual global involution; properness identifies
them with the closures of generic fixed points.

Those generic fixed points are exactly the four cusps, and every cusp
is individually mu-fixed. A smooth fixed point on a component in the
nontrivial elliptic orbit would therefore be the reduction of a
mu-fixed section and force its unique containing component to be
mu-fixed. This is impossible. Nothing here asserts fixed-point
lifting at a node or on a sigma-trivial component.

## Rooted-tree count

Root the compact-type tree at a component carrying a cusp. It is
mu-fixed. The elliptic orbit vertices all have the same positive
distance from this root. The unique parent path of each is sigma-fixed,
so its parent node is one of its two fixed points. The second is not
smooth by the local argument, and must be a different child node.

The subtree past that child contains no cusp: any path between the
root and a mu-fixed marked vertex is fixed vertex by vertex, which
would force the elliptic vertex to be mu-fixed. It contains no other
member of the elliptic orbit, by equality of their root distances.
If it contained only rational components and no marks, a leaf would
have too few special points for the stable marked model. It must
therefore contain positive genus. These child subtrees are pairwise
disjoint, again by equal root distances of the orbit vertices. The
m/2 elliptic genera and their m/2 extra positive genera force total
genus at least m, whereas the actual genus is m-1. This excludes the
ordinary alternative for every m at least four and closes induction.

## Cusps, intermediate quotients, and all coefficient primes

The four explicit divisors, obtained by expansions at zero and infinity,
join the four cusps with multiples m. Their leading coefficients are
nonzero in characteristic zero, so the precise order is m; the product
identities exclude further zeros. Every cusp difference is m-torsion.

The inertia is the normal subgroup generated by r^2. If HI were the
whole dihedral group, its image in C2^2 would supply an odd rotation
and a reflection in H. Since m is a power of two, these generate the
whole group. Thus every proper intermediate has at least two actual
cusps. Its finite map to E ensures positive proper genus. The actual
norm is surjective up to isogeny, transferring good reduction and
special 2-rank zero. Norms of the cusp functions transfer m-torsion:
over the algebraic closure, pushforward of a point has coefficient
one, irrespective of ramification. This direction of the norm
comparison is checked explicitly.

There is no nonzero geometric 2-power torsion on a 2-rank-zero
special abelian variety, so the cusp differences specialize to zero.
A41 supplies the rational cusp paths, A42 supplies the fixed groups
also at coefficient prime two, and A59 supplies all normalizers for
the nilpotent closure. The whole-group quotient is the original
punctured elliptic curve. All field restrictions are the previously
proved restrictions in those actual arithmetic comparison maps.

No remaining gap was found in this uniform-family proof. The source
ledger, the failed preliminary marked-fibre routes, and the finite
supporting certificate remain separately retained.

## Final clarified draft and additional primary checks

The final clarified draft, SHA256
`34c99d85c5b8dc41dce1a4e622d3484190264d2f12c9391c0d60169784211c99`,
was compared again. It includes all four explicit cusp divisors, the
elementary proper-intermediate cusp count, extension of the defined
endomorphisms, and the local fixed-locus algebraization/properness
sentence. These additions pass without changing the certificate.

Root additionally opened Bouw--Wewers, *Group actions on curves and
the lifting problem*, AWS2012 notes, Section2.2 equation(3) and
Exercise2.12(c), at
https://swc-math.github.io/aws/2012/2012BouwWewersNotesPreliminary.pdf .
The classical lower-numbering and Sylow-p inertia convention agree
with the independently derived different sum. The actual source
title is recorded here to avoid confusing it with another set of
Hurwitz-space notes.

Root opened Jan Vonk's author notes at
https://pub.math.leidenuniv.nl/~vonkjb/teaching/2021_topics/Topics.pdf ,
Corollary2.16 and proof, printed23. The factorization explicitly has
a uniformizer-power factor; nonzero reduction sets that exponent
to zero in the fixed-locus application. This proves finite flatness
under the stated complete-DVR hypothesis. Both final source gates pass.
