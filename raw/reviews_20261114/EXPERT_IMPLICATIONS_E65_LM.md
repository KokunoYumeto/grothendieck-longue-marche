# What follows from the CM parity character (LM7_PUSH D.50, E.58, E.65; LM4 D.32, D.34)

By Claude Fable 5.2 at effort max (field expert of the Longue Marche line, agent a125034fd35557818), 14 Nov 2026.
The chain is taken as holding, as the brief says: it is the work of GPT-6 Astra (ChatGPT Pro mode), checked line by
line by two referees (Claude Opus 5.5 at effort max). Read for this page: the verdict sections of referee A (D.50,
E.58) and referee B (E.61-E.65) and B's step 9; my notes and two consults. Not read: the returns, the two LM4 referee
files, the other agent's file. "Hunch" marks what is mine and unproved. Bibliographic statements are from memory
unless a source is named as read.

## 1. Does it make sense as mathematics?

Yes. I see no clash with anything I know about `GT_0-hat`, and three things fit known theory.

- **The frames are the primitives of Lochak and Schneps.** With `B = C_2 * C_3` completed and `F` the free subgroup of
  level two, an element `(1, f)` acts by `s -> s f`, `r -> f^{-1} r`; `(s f)^2 = 1` is the 2-cycle relation and
  `(f^{-1} r)^3 = 1` the 3-cycle relation. Torsion in a free profinite product is conjugate into a factor
  (Herfort-Ribes), so `s f = b s b^{-1}` and `f^{-1} r = A r A^{-1}`, with `b, A` in `F` unique because the
  centralizers of `s` and `r` meet `F` trivially. That is: `f` is a coboundary for `Int(s)` and for `Int(r)`, the
  cohomological form of the two relations (Lochak-Schneps 1997; not opened). The frames `b, A` are canonical
  primitives. This is also the formalism of the manuscript: the signed normalizers of `rho` and `sigma` of sections
  46 to 49 are these data.
- **The shear `V = U^{8 rho}`** in the covariance modulo 12 is the correction `-8 rho_2` at the Tate curve that
  Nakamura-Schneps have in relation (III') and that LM7 A.18, D.18 and LM8 E.8 found by two other routes.
- **Why a non-Galois value can occur.** For a Galois element both frames are path cocycles to the two special fibres
  of the Legendre family (`lambda = 1/2`, CM by `Z[i]`; a root of `lambda^2 - lambda + 1`, CM by `Z[zeta_3]`), and
  both parities are the one quadratic character of `Q^ab(3^{1/4})` over `Q^ab` (I recomputed the two models and the
  twist). That equality is arithmetic: the fields `Q(E_3[4])` and `Q(x(E_4[3]))` coincide. The 2-cycle and 3-cycle
  relations know nothing of it: the `s`-frame comes from one relation, the `r`-frame from the other, and they are
  tied only through `f`. E.58's element has `f` in the nilpotent residual of `H = F'F^3`, so it is trivial in every
  pro-`l` quotient of `F` and lives entirely where the primes 2 and 3 are mixed. This is the same mechanism as LM8
  A.22 (an idempotent mixing 3 and 5) and LM4 D.29 (a multiplier `-1` at one prime only): groups cut out by the
  weak relations allow independent choices on pieces that Galois correlates.

One consequence that neither consult of mine stated, and that does not need `Delta`: **D.50 lifts every pro-`l`
gentle pair to the full profinite `GT_0-hat`.** The pro-`l` group of the pentagon is strictly smaller than the pro-`l`
gentle group for every `l` (LM8 B.12, B.14d). A lift of a gentle pair with non-zero pentagon defect is not in
`GT-hat`. So **`GT-hat` is strictly smaller than `GT_0-hat` for the profinite groups, already by D.50**, and LM7
D.13 (ii) is settled for `GT_0-hat`. In my second consult I wrote that this strictness would follow from `Delta = 0`
on `GT-hat`; it holds either way. What `Delta = 0` would add is much sharper: `GT-hat` inside an open subgroup of
index two, by a relation visible at level 12.

## 2. What follows

1. **A theorem now.** `Delta : GT_0-hat -> F_2` is a continuous surjective character that vanishes on the Galois
   image. The pair of parities maps the multiplier-one part onto `F_2 x F_2`; Galois has the diagonal. The Galois
   image lies in an open subgroup of index two of `GT_0-hat`. `Delta` is invisible in every pro-`l`, pro-nilpotent
   and graded quotient: no Lie approximation of the tower can see it.
2. **The dichotomy.** `Delta = 0` on `GT-hat`: the pentagon forces the two special fibres to agree, a relation of
   level 12. `Delta != 0` on `GT-hat`: `GT-hat` has a quadratic character trivial on Galois, so `GT-hat` is not the
   Galois image. The two branches are not symmetric as problems. Since `Delta` factors through a finite level,
   "`Delta = 0` on `GT-hat`" is true if and only if at some finite level no pentagon shadow has parity one: if true
   it has a finite certificate. "`Delta != 0`" needs a compatible family at every level, that is a lifting theorem
   with the pentagon, which nobody has.
3. **The two CM coordinates.** By LM7 D.16 the Galois image in the product of the two projective adelic CM
   coordinates has index two. Hunch: the intersection of the maximal abelian extensions of `Q(i)` and of
   `Q(sqrt(-3))` is `Q^ab(3^{1/4})`, one quadratic extension of `Q^ab` (a group with two abelian subgroups of index
   two has a commutator subgroup of order at most two), so `Delta` is the only obstruction: the image of the
   multiplier-one part of `GT_0-hat` is the whole product and `ker Delta` maps onto the Galois image. That would
   settle LM2 C.d5.
4. **Torsion.** By LM4 D.32, D.34 the torsion of `GT_0-hat` is involutions of multiplier `-1`, and
   `Delta(tau) = delta((1, f_tau))`. `Delta` is constant on conjugacy classes and zero on complex conjugation, so it
   is a map from the classes of involutions, `H^1(<c>, multiplier-one part)`, to `F_2`. An involution with
   `Delta = 1` would be a second conjugacy class of involutions in `GT_0-hat`.
5. **The Fermat tower's D.46.** Its recorded pair (`T_4 = I`, `W_3 = [i]`) and the bits `(1, 0)` of E.58 differ by
   the Galois class `(1, 1)`: both have `Delta = 1`. D.46 lives on a relative pronilpotent completion; E.58 is in the
   full group. E.58 says that the residual the tower stands at can be removed for some choice of candidate; whether
   D.46 times a Galois element is E.58's element is a finite comparison nobody has made.
6. **Section 47.** The subgroup `C^phi` of LM8_PUSH (extension from level two agrees with descent along
   `F -> C_2 * C_3`) contains Galois. On `C^phi` both frames are values of the one word `f(s, sr)` and of the third
   conjugator, so `Delta` there is computable from `f` at level 12. Whether `Delta = 0` on `C^phi` is not automatic
   (the vanishing on Galois used arithmetic); if it holds, E.58's element is outside `C^phi` and section 47 cuts
   `GT_0-hat` down.

<!-- part 2 joined -->

# What follows from the CM parity character, part 2 (sections 3 to 7)

By Claude Fable 5.2 at effort max (field expert of the Longue Marche line, agent a125034fd35557818), 14 Nov 2026.
Part 1 (sections 1 and 2) is `EXPERT_IMPLICATIONS_E65_LM.md` in this folder; the context guard stopped my shell
before I could append, so this half is a file of its own. Same basis and same marks as part 1: "hunch" is mine and
unproved; bibliographic statements are from memory unless a source is named as read. The chain D.50, E.58, E.65 is by
GPT-6 Astra (ChatGPT Pro mode), refereed by Claude Opus 5.5 at effort max.

## 3. Why Galois has `Delta = 0`: the harmonic map (hunch, derived for this page, unchecked)

The coincidence of the two fields has a geometric source. The modular curves of level 3 and level 4 are both a
sphere, with the tetrahedral group `A_4` and the octahedral group `S_4`, and `A_4` lies in `S_4`. The points of level
3 over `j = 1728` are the edge midpoints of the tetrahedron, which are the vertices of the octahedron; the points of
level 4 over `j = 0` are the face centres of the octahedron, the vertices of the dual cube. The quotient map from the
`A_4`-orbifold (2, 3, 3) to the `S_4`-orbifold (2, 3, 4) has degree two: it identifies the two points of order 3, is
ramified at the point of order 2 (which goes to the point of order 4), and has one more ramification point, over the
point of order 2 below. On the three-pointed sphere this is exactly `w = 4 lambda (1 - lambda)`, with `lambda = 1/2`
as the extra ramification point: the harmonic map of Nakamura and Tsunogai, the quotient of the `lambda`-line by
`lambda -> 1 - lambda`.

So the statement behind `Delta = 0` is: the automorphism is compatible with the covering of the tripod by itself
through the quotient by one involution of `S_3` (and, for the other fibre, by the 3-cycle). Three consequences.

- **Section 47 is the same condition for the whole of `S_3`.** Grothendieck's map `F -> C_2 * C_3` is the quotient of
  the `lambda`-line by `S_3`; the harmonic and the equianharmonic equations are the quotients by `C_2` and by `C_3`.
  So I expect the section 47 subgroup `C^phi` to lie in the harmonic and equianharmonic subgroups, and those to lie
  in `ker Delta`: Galois, inside `C^phi`, inside (harmonic and equianharmonic), inside `ker Delta`, a proper subgroup
  of `GT_0-hat`. Then E.58's element violates section 47, and the second half of LM8 B.28 (section 47 cuts
  `GT_0-hat` down) is settled.
- **`Delta` on `GT-hat` is a parity form of a known open question**: whether every element of `GT-hat` is compatible
  with this degree-two covering, that is, satisfies the harmonic equation. From memory, Nakamura-Tsunogai-Yasuda tie
  that equation to relation (III') of Nakamura-Schneps, which is known on Galois and not on `GT-hat`. I withdraw the
  expectation "`Delta = 0`" of my first consult: I know no mechanism by which the pentagon gives compatibility with a
  covering that is not a map between moduli spaces of genus zero, and LM7_PUSH's finite pentagon tests have removed
  no whole fibre so far. I have no expectation either way.
- **Where the pentagon could still force it.** `GT-hat` acts on the full mapping class group of the sphere with five
  points, which is generated by torsion elements of orders 5 and 4 and has elements of order 3. Their frames project
  to the frames of `s` and `r` when a point is forgotten, and the relations between the torsion generators constrain
  the frames jointly. That is the one place where a relation between the two parities could come from genus zero.

## 4. What it means for Grothendieck's programme

- **Sections 46 to 49.** His loop equations are the 2-cycle and 3-cycle relations (LM2 B.m2), and the group they
  define is now known to be too large at the full profinite level, by an explicit character built from his own
  objects, the normalizers of `rho` and `sigma`. Section 47, the compatibility with `C_2 * C_3`, is where the missing
  condition sits. The companion can say this as a theorem, with section 3 as its reading once that is proved.
- **The Esquisse and the tower.** The two-level principle says that the automorphisms of the whole tower are fixed by
  the pieces of dimension one, (0,4) and (1,1), and the relations of dimension two, (0,5) and (1,2). `GT_0-hat` is
  (0,4) alone; `GT-hat` adds (0,5); the group of Nakamura-Schneps adds the genus-one pieces. `Delta` is a condition
  at the two orbifold points of (1,1), read at level 12. If `Delta` is not zero on `GT-hat`, genus zero does not
  determine the tower and the genus-one pieces carry conditions of their own: `GT-hat` would be strictly larger than
  the Nakamura-Schneps group and than the Galois image. If `Delta = 0` on `GT-hat`, the pentagon reaches into genus
  one at its first test.
- **Section 52 (approximations de Lie).** `Delta` is invisible to every pro-`l` and unipotent quotient, so the
  motivic side (Deligne-Drinfeld, `grt`, mixed Tate motives) cannot see it. It is the first explicit invariant in our
  material that only the full profinite tower carries, which is what LM8 B.1 to B.3 said about section 52.3.

## 5. What the field knows (from what this line has read; the rest needs a search)

- Read by this line: Drinfeld, section 4; Harbater-Schneps, Main Theorem (`GT_0-hat` as the centralizer of `S_3`);
  Minamide-Nakamura (automorphisms of profinite braid groups); Hoshi-Minamide-Mochizuki, Corollaries B and C; the
  introductions of Boggi 2024 and 2026 and of Lochak-Nakamura-Schneps 2026 (by the intake, its Theorem 1.1 leaves
  the compatibility with the cutting homomorphisms open). None of these has a character of `GT_0-hat` trivial on
  Galois, a non-Galois element of the profinite `GT_0-hat`, or the statement that `GT-hat` differs from `GT_0-hat`
  for the profinite groups. I know the strictness only in the pro-`l` and graded settings.
- From memory, to be opened: Lochak-Schneps 1997 (the relations as cocycle conditions for `Z/2`, `Z/3`, `Z/5`);
  Nakamura-Schneps 2000 (relations (III'), (IV)); Nakamura-Tsunogai 2003 and Nakamura-Tsunogai-Yasuda 2010 (the
  harmonic and equianharmonic equations); Collas 2012, two papers (the action of `GT-hat` on torsion of the full
  mapping class groups in genus zero and one is conjugation and a power; the conjugators are the frames).
- To search before any claim of novelty: "`GT-hat` is not `GT_0-hat`" for the profinite groups; finite characters of
  `GT-hat` or `GT_0-hat`; the abelianization of `GT-hat`; torsion in `GT-hat` (LM4 D.32 may be known for `GT-hat`);
  whether the frame classes at the elliptic points appear in Collas or in Schneps's work on special loci.

## 6. Hunches (mine, unproved)

- H1. `C^phi` lies in the harmonic and equianharmonic subgroups, and these lie in `ker Delta` (section 3).
- H2. The two CM coordinates map the multiplier-one part of `GT_0-hat` onto the whole product of the two projective
  adelic norm-one CM groups, and `ker Delta` onto the Galois image: `Delta` is the only obstruction (part 1, 2.3).
- H3. Every involution of `GT_0-hat` has `Delta = 0`. No expectation; an involution with `Delta = 1` would be a
  second conjugacy class of involutions.
- H4. The pentagon has a third frame, at the point of order five, with a coordinate in the norm-one group of
  `Z[zeta_5]`. With the frames of orders 4 and 3 in the five-point group it gives further characters on `GT-hat` of
  the same kind as `Delta`. Each coincidence between the torsion fields of two CM points of the moduli spaces is a
  candidate.
- H5. E.58's element and the tower's D.46 differ by a Galois element at the levels where both are defined.

## 7. Prompt items for GPT-6 Astra (ChatGPT Pro mode), each to be proved or refuted

1. **Main question: `Delta = 0` on `GT-hat`.** Three routes, in this order. (a) The finite certificate: `Delta`
   factors through a finite level, so "`Delta = 0` on `GT-hat`" holds if and only if at some finite level no pentagon
   shadow has parity one; compute every pentagon shadow with its parity at the levels of the five-point group through
   which `Delta` is defined, using the presentation by torsion generators of orders 5 and 4. (b) The frames of the
   torsion of orders 5, 4 and 3 in the five-point group and the relations they satisfy. (c) The harmonic equation for
   `GT-hat` at level 12.
2. H1, with the exact substitution between section 47, the harmonic and equianharmonic equations and relation
   (III'); and section 3 as a theorem: the degree-two map between the pictures of level 3 and level 4 is the harmonic
   map, and the two parities of an automorphism compatible with it agree.
3. H2: the covariance at every level, the image of the two CM coordinates, and the intersection of the maximal
   abelian extensions of `Q(i)` and of `Q(sqrt(-3))`.
4. H3: `Delta` on `H^1(<c>, multiplier-one part)`; the conjugacy classes of involutions of `GT_0-hat`.
5. The abelianization of `GT_0-hat`: is it `Z-hat^x` times `F_2`, or more; every continuous finite character that is
   trivial on Galois.
6. H4: the frame at the point of order five and the characters it gives on `GT-hat`.
7. H5: D.46 against E.58, and the arithmetic boundary of the Fermat tower's residual.
8. The smallest finite quotient of `GT_0-hat` through which `Delta` factors, with a program that evaluates it.

Items 1, 2 and 4 are the successor of LM7_PUSH; items 3, 5 and 8 can go with it or into LM8_PUSH Part C; item 7 is
the Fermat tower's successor; item 6 is new and would be a prompt of its own. Before any of them is sent: the search
of section 5, and the corollary of D.50 stated in part 1 (`GT-hat` strictly inside `GT_0-hat`) written out with its
proof and checked by a referee.

## State of this agent

Context over 70 % (709k of 1M); the guard now allows only Write and Edit. The handoff
(`LM_EXPERT/KNOWLEDGE_HANDOFF.md`) could not be given a section for the work of 14 November. A successor should take,
beside its sections 4 and 5: `CONSULT_LM_EXPERT.md`, `CONSULT_LM_EXPERT_2.md` and the two parts of this page. One
correction to `CONSULT_LM_EXPERT_2.md`: the strictness of `GT-hat` in `GT_0-hat` does not wait for `Delta`; it follows
from D.50 with LM8 B.12 (part 1, end of section 1).
