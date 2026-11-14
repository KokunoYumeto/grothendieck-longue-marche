# The exact arithmetic condition for canonical central-lift values

**Status:** complete route audit and proved conditional compatibility criterion, awaiting independent review. This file does not assert the missing conditions for an arbitrary section.

## 1. A precise local-to-global criterion with automatic compatibility

Let k be a number field. For every place v choose

\[
\lambda_v\in\widehat{k_v^\times}.
\]

At a real place this is its sign class; at a complex place the completion is trivial. Write lambda_{v,n} for the compatible class in H¹(k_v,mu_n). Use the standard Tate modification at archimedean places in the local duality pairing.

There exists a class A∈widehat(k^×) whose localization is lambda_v at every place if and only if, for every n≥1, both of the following conditions hold:

1. **Restricted-product condition:** lambda_{v,n} belongs to H¹_un(k_v,mu_n) at all but finitely many finite v. Away from v|n this says that the valuation of lambda_{v,n} is zero modulo n.
2. **Reciprocity condition:** for every chi∈H¹(k,Z/n),

\[
\mathcal O_n(\lambda)(\chi)
  :=\sum_v\operatorname{inv}_v
      \bigl(\lambda_{v,n}\smile\chi_v\bigr)=0.
\tag{1}
\]

The sum is finite: outside the union of the finite ramification/support sets both factors are unramified and their cup product in H² of the finite residue field vanishes.

When such A exists, it is unique. It is consequently functorial for multiplicative operations, restriction to finite extensions, and norms, whenever the specified local data satisfy the corresponding identities.

### Proof

For fixed n, put M=mu_n and M^D=Hom(mu_n,Gm)=Z/n. The restricted-product condition says exactly that lambda_n is a point of P¹(k,M). Poitou–Tate exactness gives

\[
H^1(k,\mu_n)\longrightarrow P^1(k,\mu_n)
 \longrightarrow H^1(k,\mathbf Z/n)^*.
\tag{2}
\]

The second arrow is (1), with the indicated convention for signs and real Tate groups. Thus the reciprocity condition is equivalent to existence of an actual global preimage, not merely membership in the closure of the global image. This is Milne, *Arithmetic Duality Theorems*, second edition, I §4, Theorem4.10(b), with S the set of all places. The definitions of P¹ and the local conventions are immediately before Lemma4.8.

For completeness, there is no hidden closure issue in (2). Milne I Lemma4.9 says that the inverse image of every compact subset of P¹ under localization is finite, where global H¹ has the discrete topology. On a compact-open local condition this gives only finitely many global classes (ultimately by Hermite finiteness for extensions of bounded degree and bounded ramification). The global image therefore meets every compact-open subset in a finite closed set, so it is closed in P¹. The exactness in Theorem4.10(b) is expressly Im(beta)=Ker(gamma), with the actual image.

Let S_n be the set of these global preimages. It is a nonempty finite set: a fibre is a coset of the finite localization kernel, and its finiteness follows already from Milne I Lemma4.9 (properness of the localization map for the discrete topology), or Theorem4.10(a). No assertion that the finite-level localization map is injective is needed; such an assertion would be false over some number fields.

For n|m, reduction H¹(k,mu_m)→H¹(k,mu_n) maps S_m to S_n, because the local data were compatible. Hence the S_n form an inverse system of finite nonempty sets. Passing to the cofinal sequence n=r!, compactness gives a nonempty inverse limit. For clarity, this does **not** require surjective transition maps: any finite collection of compatibility constraints is realized by an element at one sufficiently divisible level, so the closed compatibility conditions have the finite-intersection property in the compact product of the finite S_n. An inverse-limit point is precisely the required A.

If A and B have the same localizations, A/B is locally trivial at every finite place at every modulus. D.26's compatible Kummer lemma makes A/B=1. This proves uniqueness. Restriction and norm commute with localization and the finite-level Kummer maps. Thus two proposed global expressions with the same specified local expression agree by this uniqueness; for norms one takes the product over the places of the extension above v.

The criterion also applies componentwise, by Shapiro, to every quasi-trivial torus Res_{L/k}Gm and to a product of such tori. In particular it is the exact arithmetic matching criterion for the difference between a chosen global cuspidally central lift and prescribed local cuspidally central lifts, after those local lifts and comparison paths have actually been specified. Existence of an arbitrary global central lift only gives an origin for this difference torsor.

## 2. What is missing for an added rational puncture

Set

\[
U=\mathbf P^1_k-\{0,1,\infty\},\qquad
 a\in k-\{0,1\},\qquad W=U-\{a\}.
\]

For an ordinary local point x_v∈W(k_v), the canonical new-puncture value, in the inverted torus coordinate if necessary, is

\[
\lambda_{a,v}=x_v-a.
\tag{3}
\]

This is the actual value required by the canonical map from W into the diagonal torus torsor. It is not an arbitrary nonzero coordinate in that torsor's fibre. At old cusps, the corresponding value is read using the given old tangential section; at a newly created cusp x_v=a, an additional tangential class must be chosen. A real connected component similarly does not specify more than the real data warranted by the chosen lift. The criterion in Section1 applies to any fully specified compatible family of such values; it does not silently choose new tangents or real signs.

Even in the subcase where all x_v avoid a and are ordinary, D.26 controls neither of the two new requirements automatically. Its asymptotic integrality concerns the original boundary {0,1,infinity}, not contacts with the interior divisor a. Thus it does not imply that v(x_v−a) is zero modulo n for almost every v. Even if that restricted-product condition is separately established, one must still prove (1) for this translated tuple.

The missing reciprocity tests have an exact geometric location. For chi∈H¹(k,Z/n), put

\[
\beta_{a,\chi}=\kappa(t-a)\smile\chi\in\operatorname{Br}(W)[n].
\tag{4}
\]

Define partial_a to be the **cohomological** residue of §1.4.1, which after the identification with Br is the negative of the Witt residue by Theorem1.4.10. With that explicit convention,

\[
\partial_a\beta_{a,\chi}=\chi.
\tag{5}
\]

Indeed t−a is a uniformizer of the smooth curve at its rational point a, and chi is an unramified character there. The local residue of the cup product of a uniformizer with chi is chi. All other points of U have valuation zero on t−a. Purity for the Brauer group of a regular curve gives the split exact sequence

\[
0\longrightarrow\operatorname{Br}(U)[n]
 \longrightarrow\operatorname{Br}(W)[n]
 \xrightarrow{\partial_a}H^1(k,\mathbf Z/n)
 \longrightarrow0,
\tag{6}
\]

split by chi↦beta_{a,chi}. To check the kernel, a class in Br(W) has no residues at the points of W; vanishing of its residue at a is therefore exactly the condition that it extend across a. Surjectivity and preservation of n-torsion follow from the explicit symbols (4). The injection is the generic-point injection for a regular curve. In particular **no nonzero** beta_{a,chi} extends to Br(U), and adding a constant Brauer class cannot change this residue.

The exact source for the residue and purity inputs is the opened author draft of Colliot-Thélène–Skorobogatov, *The Brauer–Grothendieck group*, 31 October2019, §1.4.1 (the uniformizer cup-product formula and equation(1.17)), Theorem1.4.10 (the cohomological residue is the opposite of the Witt residue), and Proposition3.6.1 (the regular-curve residue sequence). The cup order in (4) and equation(1.17) give the positive cohomological residue in (5). Proposition3.6.1 uses the corresponding residue exactness; negating the Witt residue leaves its kernel and exactness unchanged. The sign change does not affect reciprocity vanishing. Cup order alone is not asserted to identify the two residue conventions.

At ordinary points equation(1) is exactly

\[
\sum_v\operatorname{inv}_v\beta_{a,\chi}(x_v)=0.
\tag{7}
\]

An original section on U supplies global pullbacks and reciprocity for classes on U. It does not supply a pullback of the new residue summand (6): those classes live on W and ramify at the interior point a. Thus using section reciprocity to claim (7) would require precisely an extra lift or an additional theorem. The missing tests are identified explicitly, not merely described as an unspecified local-to-global difficulty.

## 3. A small verification of the distinction

The following example tests only the claimed sufficiency of density/integrality information; it is **not** asserted to arise from a global section. Take k=Q, a=2, x_v=3 for every place v except v=3, and x_3=4. All points are ordinary, and the family is integral on W outside a finite set. The tuple in (3) is1 at every place except3, where it is2. For the quadratic character chi of Q(sqrt3)/Q, the only possible nonzero term in (7) is the quaternion symbol (2,3)_3. It is nontrivial because the residue of the unit2 modulo3 is a nonsquare; equivalently the conic for its norm equation has no solution. The sum is therefore1/2. No global squareclass, hence no global completed multiplicative class, has these localizations.

This example does not weaken the full section hypotheses: it need not satisfy the old global t and 1−t Kummer constraints. Its role is just to verify that even **cofinite** integral local points by themselves do not enforce the new reciprocity summand. D.26's density-one conclusion cannot supply that summand by itself.

## 4. Exact consequence for the remaining route

If one could establish restricted-product admissibility and all the new reciprocity tests for the prescribed canonical local values, Section1 would produce a unique global completed value. Any true local norm identities would then force global norm compatibility, without the erroneous surjectivity used in the old route audited in D.24. This removes an artificial compactness objection once canonical matching has been proved.

What remains unproved is precisely the nonemptiness of these canonically constrained finite-level fibres: the two conditions of Section1 for (3), with any necessary new cusp choices. For a birational section these Kummer classes already exist by pullback of rational functions; the criterion therefore does not resolve D2's stronger cofinite-integrality problem. For an arbitrary section of U, it identifies the extra interior-puncture residue data required for D4. It neither constructs a section of pi1(W) nor replaces the remaining nonabelian lifting problem by central data.

## Sources actually opened

- Milne, J.S. (2006). *Arithmetic Duality Theorems* (2nd ed.). I §4, definitions before Lemma4.8, Lemma4.9, Theorem4.10(a)–(b), printed pp.55–57. Official primary book PDF also opened: <https://jmilne.org/math/Books/ADTnot.pdf>; the same text was read in Brian Conrad's academic copy <https://math.stanford.edu/~conrad/BSDseminar/refs/MilneADT.pdf>; author publication page <https://jmilne.org/math/Books/adt.html>.
- Colliot-Thélène, J.-L., & Skorobogatov, A.N. (2019). *The Brauer–Grothendieck group*, author draft dated31October2019. §1.4.1, equation(1.17), Theorem1.4.10, Proposition3.6.1, and the local quaternion residue example following Corollary3.6.3. <https://www.imo.universite-paris-saclay.fr/~jean-louis.colliot-thelene/BGgroup_book.pdf>.
- Internal D.26 for uniqueness in the full compatible completion, and D.23–D.24 for the central-lift torsor and the separate norm-surjectivity obstruction.
