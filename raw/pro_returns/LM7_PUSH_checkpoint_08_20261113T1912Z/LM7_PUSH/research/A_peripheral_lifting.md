# Peripheral lifting audit: D.23–D.24

## Proved statements and exact source

The active source is `sections/D_peripheral_agent.tex`. Part A's source
remains frozen for checkpoint04. The new results do not change the open
status of D.1 or D.2.

The source throughout is the actual free profinite group on `x,y`, with
`z=(xy)^-1`; the three peripheral embeddings are the closures of these
cyclic subgroups. The inverse basis replacement `y=x^-1 z^-1` verifies
the third embedding. No pro-p relative result is used without a map to
this full profinite pair.

### D.23: exact abelian relative obstruction

For an elementary-abelian extension `A -> E -> G`, a fixed generating
peripheral triple of E, a peripheral automorphism alpha of G, and a common
unit multiplier lambda, the product of chosen conjugated lifts is `r in A`.
Writing sigma_i for the resulting actions on A, its variation under three
kernel conjugators is exactly

`(1-sigma1)a1 + sigma1(1-sigma2)a2 + sigma1 sigma2(1-sigma3)a3`.

The image is the augmentation submodule `[E,A]`. Therefore the fixed-base-
conjugator class is in `A_G`, with a kernel of size `|A|^2 |A_G|`.
Every base conjugator must also be counted: the resulting change of class
is the sum of the centralizer homomorphisms
`kappa_i:C_G(g_i)->A_G`, `c -> [lift(c),X_i]`. Thus the actual unframed
obstruction is `A_G/H`, where H is the sum of these three images. All lift
and base-conjugator choices are included.

When the obstruction is zero, the exact number of literal weak lifts is

`|A|^2 |A_G| product |C_G(g_i)| / (|H| product |C_E(X_i)|)`.

The proof counts full conjugator triples and divides by their exact
centralizer multiplicity. For an irreducible A, a nongenerating image is a
complement. The unique section of a complement is admissible for alpha and
lambda exactly when it is admissible for the identity shadow, by applying
the inverse unit power to the peripheral conjugacy condition. Thus the
nongenerating count is independent of alpha and lambda. The identity case
has the original generating triple, so every nonempty case has a generating
lift. Noncentral irreducible A has `A_G=0`, so every such chief step lifts.
The remaining abelian chief case is a central kernel C_p.

The full relative-cohomology comparison is explicit. Global cocycle values
`(u,v)` restrict to `(u,v,-sigma3(u+sigma1 v))`. The map from three peripheral
values to the relative class is
`(b1,b2,b3) -> b1+sigma1 b2+sigma1 sigma2 b3 mod [E,A]`.
The pullback extension with its actual chosen peripheral sections maps to r.

The universal central p-cover is
`Fhat/(K^p [Fhat,K]) -> G`, where K is the kernel of the given epimorphism.
Its exact five-term sequence has kernel `H_2(G,F_p)` in the map from the
central kernel to `H_1(Fhat,F_p)`. The actual peripheral product word has
zero exponent sum in `Fhat^ab`, so its class is in that Schur term. When p
does not divide |G| the term vanishes by averaging. The mixed case retains
both the Schur term and all three centralizer maps.

Primary source opened directly: Gareth Wilkes, *Relative extensions and
cohomology of profinite groups*, arXiv:2209.06492v1 (2022), published in
JPAA 229(1) (2025), article 107846, DOI 10.1016/j.jpaa.2024.107846.
Theorem 5.5 gives the finite-kernel relative-extension comparison;
Definition 6.1 and Proposition 6.3 give the relative lifting comparison.
The paper proves the exact cochain map independently, so its source group
and its sign convention are explicit.

### D.24: spin obstruction, full generation, and pro-ell comparison

The extension is

`SL2(F11) x PSL2(F11) -> PSL2(F11)^2`,

with central kernel C2. Two generating triples in PSL2(F11) have the same
ordered conjugacy profile, peripheral orders `(3,11,11)`, and opposite
products of their unique odd-order lifts. The section source has the plus
lift in the first factor and the minus projective triple in the second.
Factor-swap preserves all three labelled peripheral conjugacy classes.
The only permitted lifts of its three peripheral images have product
`(-I,1)`, hence there is no weak lift. The base-centralizer maps vanish
because their values have order dividing both two and the corresponding
odd peripheral order. This is a complete obstruction, not a badly chosen
unrestricted lift.

The exact matrices, their three conjugators, their products and their
orders are printed in D.24 and saved in JSON. The program enumerates the
generated subgroups exactly: 435600 elements in the base, 871200 in the
extension. Parent independently reran the original certificate successfully.
An updated rerun also saves the actual canonical odd lifts and their
products, and limits the program's finite order bound to p=5,7,11.

SL2(F11) is proved perfect by explicit transvection commutators with
diag(2,6), followed by elementary row reduction. Thus both groups have
trivial maximal pro-ell quotient for every ell. This exact quotient map is
part of the statement.

There is a stronger exact mixed-product comparison. For any finite ell-group
L with a specified generating triple and multiplier-one peripheral beta,
the paired source triples generate E x L and G x L: a subdirect subgroup
gives a common quotient of a perfect group and an ell-group, which is
trivial. These product groups have maximal pro-ell quotient exactly L.
The shadow swap x beta has the same spin obstruction. The shadow id x beta
has the explicit generating triple `(X_i,beta(l_i))`. Consequently this
example has an obstructed and an admitted perfect component over the same
specified finite pro-ell shadow. No leading-term exclusion follows from
this example alone.

## Executed finite checks

- `code/a_peripheral_count.py/.out/.json`: PASS for all sixteen cases in
  six elementary-abelian extensions. Direct enumeration of triples and
  generated subgroups is compared with the count formula and an independent
  enumeration of complements. A4 has 16 weak/12 generating/4 nongenerating
  lifts. D8 tests the nontrivial centralizer-image quotient H of order two.
- `code/a_peripheral_spin.py`: exact matrix search, explicitly restricted
  to supported primes 5,7,11.
- `code/a_peripheral_spin.out/.json`: exhaustive p=5 odd-order search;
  no matching spin profile in this search domain.
- `code/a_peripheral_spin_p7.out/.json`: the same exhaustive p=7 search;
  no matching spin profile in this search domain.
- `code/a_peripheral_spin_p11.out/.json`: first matched profile found and
  then all claimed matrices, products, orders, conjugators and two generated
  subgroup orders verified. PASS_EXPLICIT_NONZERO_OBSTRUCTION.
- Parent's independent rerun is retained under
  `a_peripheral_spin_p11_root_check.*`; these are parent-owned files.

## Exact remaining steps for D.1/D.2

1. A prescribed pro-ell automorphism still needs compatible finite components
   at every full profinite quotient. D.23 only solves the noncentral abelian
   chief steps automatically. D.29 now also solves every A5 chief step over
   an odd-order base, with the exact count and prescribed conjugators.
   D.30 now also proves every A5 chief step over an arbitrary finite base.
   Central C_p Schur obstructions and other nonabelian chief factors remain
   in the full problem; D.32 gives an actual ordinary A6 chief obstruction.
2. D.24 cannot exclude a prescribed pro-ell leading term: the same finite
   pro-ell component has the explicit admitted product branch above.
3. Coupled mixed quotients must retain their actual extension cocycle and
   module action. The peer's Schreier-induced construction in
   `code/de_s3_core.py` provides one such family; no weight-five obstruction
   has yet been evaluated in it. Replacing it by a direct product would lose
   the coupling being tested.
4. No finite tower in this note is asserted cofinal. No finite congruence
   exclusion is asserted to bound a rational leading-term dimension without
   the needed saturation/scaling argument.
5. D.23 retains its stated base-automorphism input. D.29 has now been
   strengthened to an arbitrary new epimorphism q1:Fhat->D with the
   specified peripheral power-conjugacy values. Its two normal subgroups
   K0=ker(q) and K1=ker(q1) are handled separately; neither an equality of
   those kernels nor a base automorphism relating q and q1 is assumed.

## D.25--D.29: exact subsequent results

### D.25: the unit-power removal attempt fails

An attempted route proposed that an obstruction with prime-to-ell target
could be removed by an ell-adic unit power of a compatible finite shadow.
No transformation law for the pointed obstruction had been proved. The
actual five-cycle example in D.25 refutes that proposed general removal
claim: the automorphism has order five, the obstruction is central C2,
and each of its four nonidentity powers is obstructed.

The source is a product of five A8 Nielsen components with common labelled
seven-cycle classes. Their unique odd-order spin lifts have signs
(-1,+1,+1,+1,+1). Five actual generating triples, all pairwise kernel
inequivalent, give the full product. The exact Clifford double cover on
the first component and the forced third-lift sign make every nonzero
row rotation have product -1. All source maps, component conjugators,
kernel-distinguishing relators, and Clifford products are saved in
`a_peripheral_cycle_a8.*`. The earlier bounded A7 search is retained under
the unsuffixed output names; it found no mixed-spin profile in its search
domain and is not an exclusion beyond that domain.

Both finite groups are perfect, so their maximal pro-five quotients are
trivial. This is a proved failure of the removal argument, not a claimed
restriction on the weight-five image. Root independently reran the A8
certificate and obtained byte-identical JSON.

### D.26: independent audit of the root covering theorem

The parent-owned `sections/D_covers_root.tex` proves that the fixed D.24
central-two obstruction restricts to the index times the original class
on every finite-index pants cover, with all induced peripheral groups.
The complete literal weak-lift count is zero at odd index d and
2^(d+2-b_H) at even index. The proof retains the actual double-coset
peripheral powers and uses their unique odd-order lifts to remove every
unframed centralizer ambiguity. No generation claim is made for these
weak lifts. I read the entire proof and independently ran the finite
certificate; the audit output is `a_peripheral_covers_audit.out`.

### D.27: a genuinely coupled good and bad branch

`sections/D_coupled_agent.tex` places the five A8 components in five
columns and lets C5 permute the columns. The exact index-five Schreier
maps give all 25 simple factors; all 300 pairs of coordinate kernels
are separated by literal words. The central product of the five spin
covers on the first row produces a central C2 extension. Row rotation
commutes with the column action and retains the same obstruction for
every nonidentity power.

For every normalized finite-five-group peripheral shadow beta with the
specified C5 quotient, the actual pullbacks over C5 have that same beta
in their maximal pro-five quotient. Row-rotation times beta is obstructed;
identity times beta has explicit compatible peripheral conjugators and
generates. This is an actual semidirect coupling, with its source maps
retained. The script also realizes a nonidentity beta by exact truncated
associative-algebra substitutions and literal conjugating words. Its
low-degree nonidentity is only an illustration, not a weight-five claim.
`a_peripheral_coupled.py/.out/.json` retains every comparison.

### D.28: fixed-point-free A5 wreath chief steps

`sections/D_wreath_agent.tex` proves that every prescribed peripheral
class profile has a generating lift in A5^Omega semidirect D when D is a
transitive five-group of degree at least 25 and every peripheral acts
without fixed points. The exact nonabelian Shapiro map identifies the
problem with a boundary-constrained surface representation. An elementary
lower bound for all representations and upper bounds for nonsurjective
maps and repeated coordinate kernels leave a positive count.

The repeated-kernel step uses K=ker(q), the actual subgroup normalizer,
the unique inner extension over a five-group quotient, an index-five
overgroup, and an explicit subdirect-product argument. Thus it proves
generation, not just existence of a weak lift. The normalized bad fraction
is at most 38122819/33750000000, less than 1/500. The theorem also treats
the actual coupled pullback over a finite five-group L and its maximal
pro-five projection. Root and geometry audited the full proof; root's
independent replay of `a_peripheral_a5_wreath.py` is byte-identical.

### D.29: every A5 chief step over an odd-order base

`sections/D_a5_agent.tex` removes both degree and fixed-point restrictions
for a chief extension with a given original source epimorphism. It proves
an exact count equality, retaining the specified base conjugators, for
every finite odd-order base D. The proof gives the centerless pullback
isomorphism, averages the C2-valued outer permutation cocycle, compares
every induced boundary component by right multiplication by h_i, realizes
unit powers of A5 classes by one actual automorphism, and uses explicit
Hurwitz maps to compare the surface counts. The finite subgroup-poset
inversion then retains exactly the maps with distinct coordinate kernels.
The literal gauge multiplicity is 60^(|Omega|-1).

The upgrade from five-group to odd-order base is exact: a normal image of
K in A5 is 1 or A5, and the first alternative would give an even-order
quotient of an odd-order group. Likewise an odd-order group has no
nontrivial map to Out(A5)=C2. Coupled generation uses that every nontrivial
quotient of a direct power of A5 has even order. No assertion that every
perfect group has no odd-order quotient, and no odd-order solvability
theorem, is used. Maximal pro-ell is stated only when L is an actual
ell-group. Thus every finite pro-ell base for odd ell is included.

The previously audited five-group draft is preserved as
`research/A_D29_five_group_superseded.tex`; original outputs are preserved
under `a_peripheral_a5_invariance_five_group.*`. The active certificate now
checks all 30 power-preimage operations, all eight units modulo 30, all
32 unions of A5 classes, literal Hurwitz maps, outer-cocycle averaging,
and forty genus-zero C5 cases with actual Schreier and cycle-product maps.
It ends with PASS_ALL_DEGREE_A5_COUNT_COMPARISONS. The five-group proof was
independently audited by root and geometry; the odd-order extension was
identified and audited by root before the text upgrade.

Root then identified a second exact strengthening: q1 need not equal
alpha composed with q. The boundary double-coset maps and all cover
genera still agree; the two normalizer calculations use their separate
kernels K0 and K1, with quotients equal to the same finite subgroup C.
The current statement therefore allows every peripheral generating base
shadow, including the actual coupled pullback over any new epimorphism
to odd-order L. The intervening odd-order/base-automorphism draft is
preserved as `research/A_D29_odd_order_automorphism_superseded.tex`.
The certificate is unchanged by this proof-level strengthening.

The even-base step that remained after D.29 is settled by D.30 below.
No cofinal claim or conclusion about the remaining rational dimensions
is made.

### D.30: every A5 chief step over every finite base

The complete proof is sections/D_twisted_agent.tex. The actual centerless
pullback is changed by an explicit component gauge to the subgroup of
S5^(D*\D) semidirect D whose component parities are
epsilon(t_omega d t_(omega d)^-1). For every C containing D* and every
extending character there is an actual replication embedding, with its
explicit outer gauge. Its local cycle-product sets transport by unit
powers and known individual outer flips.

The fixed-character surface argument is integral. A nontrivial handle
parity or an odd boundary factor annihilates the difference of the two
five-cycle class sums. To retain epimorphisms, the complete S5 subgroup
lattice proves that an affected proper image is one unique F20; its
annihilation identity gives the same zero difference. Maps factoring
through the finite base C are subtracted using the same actual induced
section D->E_C on both sides. The normalizer and subgroup-poset count
then retains precisely all distinct coordinate kernels.

The source comparison uses actual boundary Hurwitz maps, Dehn twists
and bounding-pair homeomorphisms matching the C2 characters. Geometry
independently audited this entire character/count argument. Root read
the full proof, including intermediate embeddings and finite-base
subtraction, and reported no substantive gap before independent replay.
No open mathematical input is used in the statement.

a_peripheral_s5_twist.py/.out/.json exhausts all120 permutations, all156
subgroups, all16 unit powers modulo60 and the integer identities.
a_peripheral_s5_maps.py/.out/.json checks all10 character-extension
cases over S3/S4, with4680 actual multiplication and1473 nonempty boundary
comparisons. Both pass. Successive A5 chief steps may be iterated; no
cofinality assertion is made.

### D.31: A6 defeats the prescribed-conjugator extension

sections/D_a6_agent.tex uses the actual extension Aut(A6)->Out(A6)=C2^2.
Every automorphism is constructed from images of a literal generating
pair in the360-element permutation group. All1440 automorphisms, the
actual inner subgroup and quotient, all inner classes and all relevant
class-product counts are retained by a_peripheral_a6_outer.*.

An explicit generating (2,8,8) triple has360 proper lifts in its initial
inner profile. Prescribing the third base conjugator to be the first
outer generator changes the profile to90 weak lifts and no proper lift.
All90 form one inner orbit and generate C8 semidirect_5 C2 of order16.
The complete64 base-centralizer cases give32 cases of360 proper lifts
and32 cases of90 weak but zero proper lifts. Forgetting the labels gives
1800 weak lifts and1440 proper lifts in two full Aut(A6) orbits. This
is a labelled obstruction; the ordinary fibre retains the original map.

The refined certificate is a_peripheral_a6_obstruction.*. An incorrect
initial guess that the bad image was a Sylow subgroup of order32 is
preserved under the explicit failed_sylow32 names. The proved order
is16, with s*r*s^-1=r^5 and inner intersection C4. Both groups have
trivial maximal pro-five quotient. Their actual products with any finite
five-group retain admitted and obstructed labelled branches over the
same specified pro-five shadow.

### D.32: a genuine ordinary A6 chief obstruction

sections/D_a6_ordinary_agent.tex includes the complete centralizer union.
The two relative (6,8,8) profiles in Aut(A6) have9 and6 proper inner
Nielsen orbits, with3240 and2160 literal triples; every triple generates.
The source table specifies all15 automorphisms by their actual generator
images. An initial wrong order/class guess in this extraction is retained
under a6_nielsen_failed_first_class; the correct first order is6 and
its inner centralizer has order3.

The base is the actual common-Out fibre product of twelve Aut(A6)
factors, containing six high-family and all six low-family representatives.
Add a seventh unused high representative as the first coordinate of the
thirteen-factor extension. Every pair of all fifteen source kernels is
separated on K=ker(F->C2^2) by a literal saved relator. The simple
subdirect-product argument proves generation of the actual groups, of
orders4*360^12 and4*360^13.

Swapping the six high/low pairs is an actual order-two base automorphism.
Twelve-coordinate peripheral conjugators have common outer values0,0,e1.
Complete base-centralizer images are the three peripheral lines in C2^2,
with actual tuples proving both values of every image. Hence all ordinary
conjugator choices force the added coordinate into the low profile.
All six low kernels already occur in the swapped base. Every weak lift
is the graph of an actual base coordinate, conjugated in the added A6.
There are2160 weak lifts, all complements, and no epimorphism. The original
base fibre has3240 weak lifts:2160 complements and1080 epimorphisms from
the three unused high kernels. The extension itself splits by a coordinate
graph.

a_peripheral_a6_nielsen.py/.out/.json and
a_peripheral_a6_ordinary.py/.out/.json pass. The latter saves all105
K-kernel relators, all12-coordinate conjugators, all centralizer-image
vectors and the graph maps. Large product generation is proved from
these maps, not claimed from enumeration of the enormous groups.
Root and geometry have the stable proof and certificates for audit.

The base and extension have trivial maximal pro-five quotient. Actual
products with a finite five-group give an obstructed ordinary branch
alpha times beta and an admitted branch identity times beta, with the
same prescribed pro-five shadow beta. This is an exact failure of general
ordinary nonabelian-chief lifting. It alone does not exclude a rational
leading direction in D.1/D.2.

## Source checks that do not supply the missing lift

The exact primary Minamide--Tsujimura 2025 Theorem 1.1 and Lemmas 3.4,
3.8 were opened. They concern strong indecomposability, prime-to-p outer
restrictions, and restrictions of existing peripheral outer actions to
open subgroups. None of these displayed maps constructs the peripheral
lift needed here. The unrestricted Out(Fhat)->Out(F_ell) comparison alone
does not imply the three conjugacy conditions; D.24 gives an actual finite
obstruction to such an inference at a specified component.


## D.41 certificate scope correction

The first finite symplectic check used every nonzero vector, although the proof invoked only the elementary handle vectors and cross-handle sums. The exact original program, output, and JSON are preserved as `code/a_relative_prop_all_vectors_superseded.*`. The authoritative `a_relative_prop.*` now uses precisely a_i, b_i, a_i+a_j, b_i+b_j for i<j and a_i+b_j for i != j, retaining the complete vector and transvection matrices. These eight vectors generate Sp4(F2) of order720, and the two handle vectors generate Sp2(F3) of order24. D.41 now displays the four-factor elementary identity for diag(u,u^{-1}). This corrects the certificate scope; the unchanged infinite proof uses the actual integral surface maps and compactness. Parent and geometry have completed their full proof audits; the refined certificate is stable for parent isolated replay.
