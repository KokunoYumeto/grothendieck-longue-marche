# Independent PBC full audit of A.69

Status: PASS. I read the complete current proof, including its corrected
single-section branch wording, independently checked the ordinary-component
argument, reopened the precise external reduction and p-rank inputs, and
reran the complete exact certificate without modifying the author's outputs.

The independent execution is retained in
`notes/pbc_A69_independent_rerun.json/.out`. Every mathematical field equals
the author result. Certificate source SHA256:
`2636819004d35d370f39c9e7d541f2fb91bca2856312814c5104be724372dc07`;
author result SHA256:
`1f6ac2f7dbc17742805b25846a57d2f900ff36572e5029f37ff8394eab8e848f`.

## Exact source scope, freshly opened

- Lehr--Matignon, Theorem 6.13 in the primary workshop contribution:
  <https://arxiv.org/pdf/math/0411059>, printed p.21, PDF page20.
  Opened references `turn1143view0`, `turn1144view0`, `turn1145view0`.
  The hypothesis is a nilpotent Galois group, smooth base model, branch
  closure étale over the valuation ring, and tameness in the generic
  characteristic. The conclusion is a tree special fibre / potential
  good Jacobian reduction. Generic characteristic zero satisfies this
  tameness condition. The actual branch divisor here is the single
  elliptic section O. No assertion about slopes of ramified vertical
  components is imported from this theorem.
- Saïdi, *Galois Covers of Degree p and Semi-Stable Reduction of Curves in
  Mixed Characteristics*, published p.662:
  <https://ems.press/content/serial-article-files/41001?nt=1>.
  Opened references `turn1143view1`, `turn1145view1`. The paragraph after
  the stated Raynaud theorem explicitly retains its tree conclusion when
  the cover is étale away from a divisor whose closure is étale over the
  valuation ring. This confirms the ramified scope used here.
- Yang, Proposition 1.4, author printed p.8, PDF page7:
  <https://www.kurims.kyoto-u.ac.jp/~yuyang/papersandpreprints/PSS.pdf>.
  Opened references `turn1143view2`, `turn1144view1`, `turn1145view2`.
  The displayed Deuring--Shafarevich formula applies to possibly ramified
  p-group covers of smooth proper curves. In A.69 it is applied only to
  the actual smooth component quotients, never to an unreduced marked
  vertical fibre.

## Algebraic and reduction checks

The map factors as the cyclic degree-m/2 extraction of `y/(x-1)` followed
by elliptic duplication, so its degree is 2m. The divisor at the four
two-torsion points gives precisely the stated four cusp indices. The two
displayed deck transformations preserve both target coordinates and give
the entire dihedral group. The base m=2 is the unramified elliptic isogeny
case. The symbolic certificate independently checks all coordinate and
duplication identities, not just the curve equations.

The odd differential indices give the primitive cyclotomic factor A_m
with dimension m/2 and a unital action of Q(zeta_m). Its completion at two
is a field of degree m/2. After potential good reduction, that field acts
on the actual rational étale Tate space of the special two-divisible group.
Its dimension is the special two-rank, so the only possibilities are zero
and m/2. The latter is genuinely the ordinary case, rather than a Hodge
signature inference.

## Ordinary component argument

1. On a compact-type special fibre the Jacobian is the product of the
   positive-genus component Jacobians. A pair exchanged by sigma has
   isogenous diagonal and anti-diagonal factors. The first has two-rank
   zero by induction, while the second would be ordinary, an impossibility
   for positive dimension. This remains valid for characteristic-two
   isogenies: two-rank is isogeny invariant.
2. For a fixed component B with nontrivial sigma, pullback and norm identify
   its invariant factor with J(B/sigma), whose two-rank is zero. If the
   anti-invariant Prym is ordinary, Deuring--Shafarevich and
   Riemann--Hurwitz give
   `r = g(B/sigma) + (sum different exponents)/2`.
   Each different exponent is at least two. Hence the quotient has genus
   zero and every different exponent is two. A zero-dimensional Prym in
   this nontrivial-action case forces B itself to have genus zero.
3. Subtracting twice Deuring--Shafarevich from Riemann--Hurwitz on an
   ordinary curve gives the displayed sum of nonnegative terms. Thus every
   inertia group has second ramification group zero and is elementary
   abelian. In particular cyclic inertia of order four is impossible.
   If a fourth root of the hyperelliptic involution existed, its induced
   involution on P1 would have one fixed point. An unramified fibre there
   would have two points and cannot support a permutation whose square is
   the deck transposition. The fibre is therefore ramified, producing the
   forbidden order-four inertia. This also covers elliptic B.
4. For an orbit of positive-genus anti-invariant components of length d,
   the stabilizing power mu^d has exact order m/d. A smaller order would
   make a nontrivial mu^k act identically on that nonzero Jacobian factor,
   contradicting invertibility of mu^k-1 in the primitive cyclotomic
   field action. Its quotient action on P1 has order m/(2d), at most two
   in characteristic two. The fourth-root exclusion gives d=m/2.
   The total anti-invariant dimension then forces exactly one such orbit,
   consisting of m/2 ordinary elliptic components. Each has two fixed
   points under sigma.

## Smooth fixed points and the rooted tree

At a smooth special fixed point on a component with nontrivial sigma,
the local action is on R[[t]], fixing R. The series sigma(t)-t has a
nonzero reduction of finite order. Weierstrass preparation therefore
gives a nonempty finite flat horizontal fixed locus, with no vertical
factor. Its generic points specialize to the given point. For these
ordinary elliptic components the degree is two. The only generic fixed
points are the four marked cusps, each individually fixed by mu. A smooth
fixed point on a nontrivially permuted elliptic component is consequently
impossible. The proof correctly makes no such lifting claim at nodes or
on components on which sigma acts trivially.

Root the tree at a marked cusp component, which is mu-fixed. The elliptic
orbit has one common positive depth. The parent edge of each orbit vertex
is sigma-fixed, hence accounts for one of its two fixed points. The other
fixed point must be a different node and hence a child edge. Its descendant
subtree has no marked point: a path from the fixed root to a fixed mark
would force the orbit vertex to be mu-fixed. It has no other orbit vertex,
since all orbit vertices have the same depth. An unmarked finite attached
subtree must contain positive genus, or a rational leaf would violate
stability. These subtrees are disjoint for distinct equal-depth orbit
vertices. The genus sum is therefore at least m/2+m/2=m, contradicting
the actual genus m-1. This proves the induction without presuming a
particular stable graph or silently assuming every component is rational.

## Cusp divisors, intermediates, and final scope

The two function products give connections among all four cusp divisors
with coefficient m. The actual inertia is the normal Frattini subgroup
generated by r squared, so every proper intermediate has at least two
cusps. Its map to E ensures positive genus; its norm Jacobian isogeny
quotient preserves potential good reduction and zero special two-rank.
Pushforward of a geometric point has coefficient one, so the norms retain
the same m-torsion bound on all cusp differences. Their specializations
are zero because a two-rank-zero abelian variety has no nonzero geometric
two-power torsion. The exact hypotheses of A.41 and A.42 are therefore met
for each cusp and a distinct companion. A.59 applies to every actual
intermediate because its geometric Galois closure remains a two-group.

No substantive mathematical correction or scope gap was found. The result
is the stated entire two-power dihedral family and its actual intermediates;
it does not claim a cofinal family or settle the universal cover question.


## Final clarification check

I also read the subsequent explicit four cusp divisors, elementary odd-rotation/reflection proof of the Frattini consequence, finite-extension/endomorphism sentence, and local different-sum derivation. All agree with the argument audited above. The final audited draft SHA256 is `34c99d85c5b8dc41dce1a4e622d3484190264d2f12c9391c0d60169784211c99`; the prior full-audit draft hash remains recorded in the JSON ledger. The exact certificate is unchanged.
