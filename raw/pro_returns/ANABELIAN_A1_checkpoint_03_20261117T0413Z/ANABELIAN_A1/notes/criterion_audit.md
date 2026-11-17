# Independent audit of AG.39.15 and AG.40

AI-produced working mathematics for ANABELIAN_A1. This file does not certify AG.41 or AG.42; their audit is separate. No priority claim is made.

## Current verdict

AG.39.15 is correct for arbitrary profinite F, closed normal K, and open I containing N=ker(K→K^(r)). Its proof below does not assume that I has r-power index. With the full geometric prime-to-p punctured-curve group as F, the stated compactification and Frobenius consequences follow.

AG.40 is correct conditional on its stated cusp-preserving isomorphism over the identity of the full proper geometrically prime-to-p arithmetic group. The compactness argument is valid; we give an expanded proof. We found one wording correction: the exceptional set upstairs need not be finite. Its image in C is finite; that is precisely what the proof uses. No full configuration exactness assertion is used in this criterion.

A2/K1, A3/K2, and A6 can therefore be recorded as proved, subject to integrating the external cohomology facts with the paper's chosen precise citations. A12/K6's equivalence of all-extension injectivity and emptiness is proved independently below. Emptiness for the full prime-to-p set still depends on the separate fibre-transport audit.

## Sources actually read

1. `background/AS_return/agent_geometric/geometric_section.tex`, AG.39.15 through AG.40, with the earlier AG.39 context.
2. `background/AS_return/sections/A_structure.tex`, AR.8–AR.9.
3. Attached arXiv source `literature/src_arXiv_0801.1452/main.tex`, the setup of Section 1, Remark 1.2, Definitions 1.3, 1.5, 1.6 and 1.10, Lemma 1.7, Proposition 1.8 and all of its proof including Claim 1.9, Corollaries 1.11–1.12; also the point-recognition inverse-limit argument in Propositions 1.21–1.23.
4. Attached arXiv source `literature/src_arXiv_1708.08773/finite-final.tex`, Propositions 2.11 and 2.12 with their proofs.
5. Journal ST2009 PDF opened independently at `https://empslocal.ex.ac.uk/people/staff/ms220/Site/Publications_files/publRIMS.pdf`. It is the journal pagination 135–186, volume 45 (2009). The relevant numbering is unchanged: Remark 1.2 (p.142), Definitions 1.3 and 1.5 (p.143), Lemma 1.7 (pp.143–144), Proposition 1.8 (beginning p.144), proof through p.147, Definition 1.10 (p.147), Corollary 1.11 (pp.147–148).

The original Boxall 1992 paper cited by ST2009 was not obtained at this stage. The exact bibliographic entry in the opened journal is J. Boxall, *Autour d'un problème de Coleman*, C. R. Acad. Sci. Paris Sér. I Math. 315 (1992), no.10, 1063–1066. The attempted Cambridge PDF for the 1995 chapter redirected to a landing page; the author's maintained home redirected to authentication. We do not pretend to have read either full text. The mathematical external input used here is the opened ST2009 Proposition 1.8, not an independently quoted theorem of Boxall.

## 1. What the finiteness theorem actually says

Let k be finite of characteristic p, X/k a smooth proper geometrically connected curve, U=X−S hyperbolic, and Σ a set of primes containing at least one prime different from p. Let Π_U be the arithmetic group retaining the whole G_k and the maximal geometric pro-Σ quotient of the tame group. Its universal pro-cover compactification is denoted by \(\widetilde X_U\).

The attached ST2009 Definition 1.3(iii) calls a point a of a set map f exceptional when \(\#f^{-1}(f(a))>1\). Definition 1.5 applies this to the map \(\overline D\) from closed points upstairs to commensurability classes of decomposition subgroups. Definition 1.10 puts \(E_U\) equal to its image in \(X^{\rm cl}\).

Proposition 1.8(iii) states injectivity of \(\overline D\) over a fixed geometric point; (iv) gives finite fibres over one closed point and injectivity over one rational point; (v) says the exceptional set is Π_U-stable; under the additional hypothesis that Σ is cofinite, (vi) states that \(E_{\widetilde U}/\Pi_U\) is finite. This quotient is \(E_U\). The same numbering and hypotheses occur in the opened journal PDF.

Remark 1.2 says that the commensurability maps are unchanged upon passing to any open subgroup. More explicitly, if H is open in Π_U and D_1,D_2 are closed subgroups, then D_1 and D_2 are commensurate if and only if D_1∩H and D_2∩H are commensurate. One direction is immediate. For the other, D_i∩H has finite index in D_i; the common intersection has finite index in both. Universal pro-cover points are the same on replacing U by its H-cover. In particular, when H is the preimage of G_L for a finite constant extension L/k, the exceptional points upstairs are exactly the same points and the exceptional image on X_L is the finite inverse image of E_U.

For Σ=Primes−{p}, all hypotheses are met when C is proper of genus at least two: U=C is hyperbolic and Σ is nonempty and cofinite. Consequently there is one finite set \(E_C\subset C^{\rm cl}\) whose geometric inverse image excludes all exceptional labels over all finite extensions. If R is a closed point outside E_C, a decomposition subgroup at R cannot be commensurate, even after conjugation, with a subgroup at another geometric point. Conjugation moves the lift and preserves the underlying closed-point label. This is exactly the use in AG.40 Step 3.

### Check of their proof and its hypotheses

Their proof first replaces U by an open-subgroup cover whose compactification has genus >1 and is nonhyperelliptic. Commensurability invariance just proved makes finiteness upstairs descend under this finite cover. For a nonhyperelliptic compactification X, the difference morphism \(\delta:X\times X\to J_X\), \((P,Q)\mapsto[P-Q]\), is injective on geometric points away from the diagonal. Indeed, equality of two differences gives \(P+Q'\sim P'+Q\); distinct linearly equivalent effective degree-two divisors would supply a degree-two map to the projective line, contrary to nonhyperellipticity. Equality of the divisors then gives the equal ordered pair, unless both differences vanish.

The image W of δ contains no translate of a positive-dimensional abelian subvariety. A two-dimensional such translate would be W itself, hence an abelian variety containing zero and generating J_X. Then J_X would have dimension two, contrary to nonhyperellipticity. A one-dimensional translate would, by the quasi-finite bijection off zero, admit a finite radicial cover mapping nontrivially to X. Its normalization has genus one (purely inseparable extensions of the elliptic function field preserve genus), so it cannot map nontrivially to a genus>1 curve; after factoring off inseparability, the separable part contradicts Riemann–Hurwitz.

An exceptional pair has zero abelian Kummer difference after a finite constant extension. Therefore its nonzero difference class lies in \(J_X(\bar k)\{\Sigma'\}\), the torsion supported on the complementary primes. Here Σ' is finite. The opened proof applies Boxall's finite-prime torsion intersection theorem to W and concludes that its intersection with that subgroup is finite. Injectivity of δ away from the diagonal then gives finitely many exceptional geometric pairs on X. For the prime-to-p choice the complementary prime set is exactly {p}, with no missing restriction to odd p, p-rank, ordinarity, or nonhyperellipticity of the original curve. The cover reduction is what handles genus two and hyperelliptic original curves.

We have checked the derivation and the hypotheses of the stated ST theorem. We have not independently reproved Boxall's theorem or the nonhyperelliptic-cover existence result cited within ST's proof.

## 2. Same-prime quotient lemma (full proof of AG.39.15)

Let F be a profinite group, K a closed normal subgroup, r a prime, and N the kernel of the maximal pro-r quotient K→K^(r). Because N is characteristic in K, it is normal in F. Let I≤F be open and contain N. We prove that the continuous epimorphism I→I/N induces an isomorphism \(I^{(r)}\to(I/N)^{(r)}\).

Take an arbitrary continuous quotient I/J which is a finite r-group, where J is open and normal in I. Put I_0=core_F(I); it is open normal in F, contained in I, and contains N. Put J_0=J∩I_0. Then J_0 is open normal in I_0 and \(I_0/J_0\hookrightarrow I/J\), so I_0/J_0 is an r-group. Take M=core_F(J_0). There are only finitely many F-conjugates of J_0, because J_0 is open. Since I_0 is normal in F, \(I_0/M\) embeds in the product of the quotients \(I_0/{}^fJ_0\), each isomorphic to I_0/J_0. Thus I_0/M is an r-group.

The image of K in F/I_0 is an r-group: N⊂I_0, so this image is a finite quotient of K/N, a pro-r group. The image of K in F/M is an extension of that image by a subgroup of I_0/M. It too is an r-group. By the universal defining property of N, N is killed by K→F/M. Therefore \(N\subset M\subset J_0\subset J\).

Every finite r-quotient of I consequently kills N. This is exactly the asserted isomorphism of maximal pro-r quotients, with its natural map, not merely an abstract isomorphism. No finite-generation assumption, normality of I, or r-power-index assumption on I was used.

### Compactification and arithmetic compatibility

Take \(F=\pi_1((C-P)_{\bar k})^{(p')}\), \(K=\ker(F\to\Delta_C)\), r≠p. An open I/N in F/N corresponds to an actual connected finite étale cover \(D^\circ\to(C-P)_{\bar k}\) whose Galois closure has prime-to-p order. The full pro-prime-to-p topology on its geometric group is induced from F: for an open subgroup with a prime-to-p Galois core, the normal-core construction again gives a prime-to-p group, since extensions and subgroups of products of prime-to-p groups have prime-to-p order. Thus I is the full prime-to-p geometric group of D^circ.

Let D be its smooth compactification. Let T⊴I be the closed normal subgroup generated by the inertia groups of the points in D−D^circ. Then \(I/T=\pi_1(D)^{(p')}\). The image of T in I/N is precisely the closed normal subgroup generated by the images of those inertia groups. Taking a maximal pro-r quotient commutes with quotient by a closed normal subgroup, by the universal property of continuous maps to finite r-groups. Therefore

\[
 ((I/N)/\overline{TN}/N)^{(r)}
 \simeq (I/T)^{(r)}
 =\pi_1(D)^{(r)}.
\]

This isomorphism is induced by the actual punctured-cover and compactification maps. Every arithmetic conjugation preserving the cover preserves its puncture inertia system and all kernels in this construction. It is therefore equivariant for the outer action of G_L when the cover descends to a finite field L. Consequently it identifies \(H^1(D_{\bar L},\mathbf Z_r)\) with its actual Frobenius action, not only its rank or characteristic polynomial modulo r.

If two such arithmetic relative groups are isomorphic over G_L and their cusp decomposition groups correspond, corresponding covers have isomorphic compactified r-adic H^1 representations. Hence they have equal integral Weil polynomials and equal compactified point counts over each finite extension of L. The missing points are indexed by the cusp double cosets, and their degrees are the indices of the projected decomposition groups in G_L. Thus these degrees also agree. Subtracting the missing points gives equal point counts for the open covers over every constant extension.

## 3. Compactness recognition with no finite-level substitution

Suppose \(\beta:G_P\xrightarrow\sim G_Q\) is the isomorphism in AG.40, over id_{Π_C}, preserving the cusp decomposition conjugacy class. For a finite extension L/k, restrict both groups to the preimage of G_L; β remains an isomorphism over id_{Π_{C_L}} and carries the base-changed cusps. Choose R∈(C−P)(L) and a decomposition subgroup D_R^P. Let S=β(D_R^P), a closed subgroup mapping isomorphically onto G_L.

Let \(\mathcal H\) be the directed set of all open subgroups H≤(G_Q)_L containing S, ordered by reverse inclusion. All these subgroups have full arithmetic projection, so their connected covers X_H of C_L−Q are geometrically connected over L. The source cover for β^{-1}(H) has a rational point above R because it contains D_R^P. By Section 2's point-count equality, X_H(L) is a nonempty finite set.

For H'⊂H the covering map gives a map X_{H'}(L)→X_H(L). The inverse limit of these sets is nonempty even though no individual transition map is asserted surjective. To prove this, take their product, a compact space. Compatibility along each transition defines a closed condition. Any finite set of compatibility conditions is satisfied by choosing a point on the cover for the intersection of the finitely many subgroups involved and projecting it to the relevant covers. Thus the closed conditions have the finite-intersection property, and compactness supplies a compatible family (x_H).

The component at H=(G_Q)_L is a point T∈(C−Q)(L). Choose a geometric lift \(\widetilde T\) over T in the universal pro-cover with every projection equal to x_H. This is possible by the same compactness argument in the profinite fibre above T. Its decomposition subgroup D_{\widetilde T} maps isomorphically to G_L: all these covers are étale at T and the residue field upstairs is \(\bar L\). For every H, rationality of x_H says that D_{\widetilde T}∩H surjects onto G_L. Since D_{\widetilde T} itself projects injectively, this implies D_{\widetilde T}⊂H. Therefore

\[
D_{\widetilde T}\subset\bigcap_{H\supset S}H=S.
\]

Both sides project isomorphically onto G_L, so they are equal. Thus β carries a genuine noncuspidal point decomposition subgroup to the decomposition subgroup of a genuine noncuspidal point of the target, in the whole profinite quotient.

If R lies outside E_C and P,Q, its proper image D_R in Π_{C_L} equals the proper image D_T. The finite-exception uniqueness from Section 1 forces T=R. This works for every closed R of C outside the one fixed finite set, upon taking L=k(R). It does not assume an a priori bijection of rational point sets, and does not identify one finite quotient with the inverse limit.

## 4. Self-normalization of a rational point section

The exact ST2009 Lemma 1.7 hypotheses are: Z⊂Π_U is closed, pr(Z) is open in G_k, and pr|_Z is injective. Its conclusion is that pr embeds the commensurator in G_k; commensurator, normalizer, and centralizer coincide and contain Z with finite index. If Z is the section of an L-rational point and we work in Π_{U_L}, its projection is the whole G_L. Therefore the conclusion specializes to

\[N_{\Pi_{U_L}}(Z)=Z_{\Pi_{U_L}}(Z)=Z.\]

This does not assert self-normalization of every closed-point subgroup in the original Π_U without enlarging constants. It is exactly sufficient for AG.40.

For clarity, the key proof of the lemma can be re-derived. A geometric commensurator σ centralizes the open intersection of Z and σZσ^{-1}, because both project injectively to the same abelian arithmetic group. If σ≠1, choose an open characteristic N⊴Δ_U not containing σ. The open subgroup \(\bar H=\langle N,\sigma\rangle\) has a nonzero image of σ in its abelianization, detected by the cyclic quotient \(\bar H/N\). The open part of Z centralizing σ stabilizes \(\bar H\), so this abelian image is fixed by the Frobenius action on the corresponding genuine cover. The abelian geometric group is a product of prime-adic Tate modules of the generalized Jacobian (proper Jacobian for proper covers); none has a nonzero Frobenius-fixed element because its eigenvalues have nonzero Weil weights, and its Tate module is torsion-free. This contradiction proves that the geometric part of the commensurator is trivial. Its injection into the procyclic arithmetic group gives the rest.

## 5. Full conditional criterion

Let k be finite of characteristic p, C/k smooth proper geometrically connected with g≥2, P,Q∈C(k), r≠p. Let G_P,G_Q be the maximal cuspidally pro-r quotients relative to the full proper geometrically prime-to-p arithmetic group Π_C. Suppose β:G_P→G_Q is a continuous isomorphism over id_{Π_C} carrying the cusp decomposition group to a conjugate of the cusp decomposition group. We prove P=Q.

### 5.1. Principal p-primary difference

Projection of the cuspidal decomposition groups gives conjugate point decomposition groups at P,Q in Π_C. A conjugator can be made geometric: multiply it by an element of the target decomposition subgroup with the same arithmetic projection. After passing to the geometric abelianization, the Kummer difference [P−Q] has zero class in H^1(G_k,T_ell J_C) for every ell≠p. Since J_C(k) is finite, its ell-adic completion is its ell-primary subgroup and the Kummer map is injective on that subgroup. Thus [P−Q] has p-power order. There is e≥0 with p^e(P−Q) principal. A rational generator over \(\bar k\) descends to k(C)^× by Hilbert 90: its Galois ratios are constants, and killing that scalar cocycle gives f with

\[\operatorname{div}(f)=p^e(P-Q).\]

### 5.2. The central extensions and the multiplier

Let M=Z_r(1). Divide the geometric cuspidal kernel in G_P by its commutators with the full geometric subgroup. The resulting arithmetic extension E_P→Π_C is the maximal geometrically cuspidally central quotient. Its kernel is procyclic, generated by the puncture inertia, because the original cuspidal kernel is normally generated by the conjugate puncture inertia groups. It is exactly M, not a finite quotient: in the geometric punctured surface presentation the puncture word is the product of the g handle commutators. Map the first pair of handles to \(1+e_{12},1+e_{23}\) in the Heisenberg pro-r group UT_3(Z_r) and all other handles to 1. The puncture word maps to \(1+e_{13}\), of infinite r-adic order, and its normal closure is central in that target. This proves that the central inertia generator has infinite r-adic order. The arithmetic action is the cyclotomic action, as on tame inertia. The same construction gives E_Q.

The class of the geometric central extension is the degree-one orientation class in \(H^2(\Delta_C,M)\simeq Z_r\), with the sign fixed by the Kummer residue convention. One equivalent construction is the Kummer first Chern class of O_C(P); its canonical trivialization on C−P gives the homomorphism from the punctured group to the extension and maps local inertia with residue +1. Its geometric restriction is the class of a point, hence a generator. This is the familiar punctured-surface orientation extension; no configuration-group injection enters.

Because β preserves the proper quotient and the geometric subgroup, it descends to an isomorphism \(\bar\beta:E_P\to E_Q\) over id_{Π_C}. On M it acts by a unit u∈Z_r^×. Restricting the extension isomorphism to the geometric group gives u times the degree-one class equal to the same degree-one class. Thus u=1.

### 5.3. The difference cocycle and its residues

On the continuous fibre product E_P×_{Π_C}E_Q define

\[\chi(u,v)=\bar\beta(u)v^{-1}\in M.\]

The common arithmetic projection acts on M cyclotomically. Multiplication verifies \(\chi(ee')=\chi(e)+e\cdot\chi(e')\); therefore χ is a continuous crossed homomorphism. Pull back to the arithmetic geometrically prime-to-p group Γ of C−{P,Q}, using its natural maps to both central extensions. On inertia at P the second map is trivial and the first has residue +1; on inertia at Q the first map is trivial and the inverse of the second gives residue −1. Thus χ has residues (+1,−1).

The Kummer class κ_r(f) has residues (p^e,−p^e). Hence κ_r(f)−p^eχ has zero restriction to both inertia groups. Since M is trivial under the geometric group, a cocycle vanishing on these inertia groups vanishes on their closed normal closure. The kernel of Γ→Π_C is precisely that closure. Thus this difference descends to H^1(Π_C,M).

Inflation-restriction gives an isomorphism

\[H^1(G_k,M)\xrightarrow\sim H^1(\Pi_C,M),\]

because \(H^1(\Delta_C,M)^{G_k}=0\). Explicitly \(H^1(\Delta_C,M)\) is Hom(T_rJ_C,Z_r(1)); the arithmetic Frobenius eigenvalues on its Q_r-extension have complex absolute value \(\sqrt{\#k}\), so none is 1, and the Z_r-module is torsion-free. Finite-field Kummer theory identifies H^1(G_k,M) with the r-primary completion of k^×. Therefore there is a∈k^× representing κ_r(f)−p^eχ.

### 5.4. Evaluation at all good closed points

Take any closed point R outside E_C∪{P,Q}, and put L=k(R). Section 3 gives a conjugacy in (G_Q)_L between β(D_R^P) and D_R^Q. The projection of a conjugator to Π_{C_L} normalizes D_R. Section 4 says this normalizer is exactly D_R. Multiply the conjugator by the inverse of the element of D_R^Q with that projection. This leaves its conjugation of the subgroup unchanged and makes it belong to the cuspidal kernel.

In E_Q its image therefore lies in M. Conjugating a section by an element of M changes its M-valued cocycle by a coboundary. It follows that χ restricts to zero in H^1(G_L,M) along the genuine section of R. Evaluation of the preceding Kummer identity gives

\[\kappa_{r,L}(f(R)/a)=0.\]

The point R is allowed to have arbitrary degree. The field L is chosen separately for each R, and β and the extension comparison are restricted along G_L→G_k; no incompatible Frobenius convention is introduced.

### 5.5. Infinitely many usable points and contradiction

Assume P≠Q. Then f is nonconstant. Over \(\bar k\) it gives a surjective finite map to the projective line. The excluded closed points have finitely many geometric inverse images, and their images under f form a finite set. Because r≠p, \(\mu_{r^\infty}(\bar k)\) is infinite. Choose a nontrivial ζ in that group with aζ outside the finite set of excluded values. Every geometric point over aζ is defined over a finite field. Choose one and regard it as a closed point R of C. Then R avoids all exclusions, and f(R)/a=ζ belongs to k(R)^×.

The inverse-limit Kummer map from a finite field's multiplicative group to H^1(G_{k(R)},Z_r(1)) is injective on its r-primary subgroup. Consequently the nontrivial r-power root ζ has nonzero Kummer class, contrary to the evaluation identity. This proves P=Q.

This last argument does not require choosing all roots of unity in the original k, and a root becoming an r-th power in some finite extension does not make its entire r-adic Kummer class vanish. The completion of a finite cyclic group preserves its r-primary subgroup.

## 6. Exact equivalence with emptiness of the exceptional set

For every nonempty Σ⊂Primes−{p}, let Π_C^Σ retain the full arithmetic quotient. Assume C is proper hyperbolic over finite k. Then E_C^Σ is empty if and only if the point-section map is injective after every finite constant extension.

If distinct L-rational points have geometrically conjugate sections, choose their lifts so that the subgroups are equal. The universal pro-cover for C_L is the same universal pro-cover with the open arithmetic group Π_{C_L}^Σ. Equal decomposition groups are commensurate. The lifts remain distinct because their geometric images are distinct. Thus the original exceptional set is nonempty.

Conversely, take two distinct upstairs points with commensurate decomposition groups D_1,D_2. Proposition 1.8(iii), whose proof only needs Lemma 1.7 and no cofiniteness, shows that their geometric images are distinct. The intersection D_1∩D_2 is open in both. Its arithmetic projection is open in G_k because the D_i project injectively onto open subgroups. Choose a finite L/k containing both point residue fields and with G_L contained in that projection. Since each D_i projects injectively, their restrictions over G_L are precisely the same inverse image of G_L in D_1∩D_2. They give equal sections of distinct L-points. This is a collision in the whole Π_{C_L}^Σ.

ST2017 Proposition 2.11(i), read in full, states E_{C'}=f^{-1}(E_C) for any étale Σ-covering f, including constant extensions. This is compatible with the equivalence. Its ramified statement is an inclusion with the ramification locus, so must not be promoted to equality. Proposition 2.12, under J_C-largeness, only confines exceptional points to a proper algebraic subfield, finite of degree at most two over the Σ'-torsion field (degree one for nonhyperelliptic C); it does not exhibit a nonempty exceptional set or contradict emptiness for the full prime-to-p set.

## 7. Negative controls and full-group examples

The script `code/criterion_negative_controls.py` has been run. Its retained `.out` and `.json` files contain all finite coordinates, point counts, and arithmetic constants below. The profinite collision claims are proved here, not inferred from a finite computation.

### 7.1. Genus one: full prime-to-p collision

Take E/F_2 given by \(y^2+xy=x^3+1\), with origin O at infinity. Its affine F_2-points are (0,1),(1,0),(1,1), so it has four rational points. It is nonsingular: a potential affine singularity must have x=0 from F_y=x, but at (0,1) the derivative F_x=y+x^2 is 1; the standard projective infinity point is also nonsingular. The inverse of (x,y) is (x,y+x). Hence T=(0,1) is a nonzero point of exact order two.

The entire geometric fundamental group of an elliptic curve is abelian. Its prime-to-two quotient is the product of the odd Tate modules. Using O as splitting, the class of the point section of T is exactly its Kummer class in that product. The two-primary point T is divisible by every odd integer in the finite group E(F_2); consequently every odd-adic Kummer component vanishes. Thus O,T collide in the entire geometrically prime-to-two group, not just in an abelianized approximation of a larger nonabelian group.

For every \(x\in E(\bar F_2)\), the same argument over a finite field containing x gives a collision between x and x+T. These are distinct. Thus the exceptional image is all of E^{cl}; it is infinite. The exact failed AG.40 hypothesis is the finite-exception statement in Step 3. ST2009 Proposition 1.8 assumes hyperbolicity of U; the proper genus-one curve is not hyperbolic. The rest of the Kummer argument does not repair that missing input.

### 7.2. Genus two: abelianized prime-to-p collision

Take C/F_2 given by

\[y^2+x(x+1)y=x^5+1.\]

At finite ramification points x=0,1 there are respectively P=(0,1),Q=(1,0), and F_x=y+x^4 is 1 at both. The infinity chart u=1/x,v=y/x^3 is

\[v^2+(u+u^2)v=u+u^6,\]

whose derivative in u is 1 at (0,0). This is a smooth genus-two hyperelliptic curve, with three simple Artin–Schreier branch points (0,1,∞). For an elementary genus check, put z=y/[x(x+1)] in the function field. The right-hand Artin–Schreier function is \((x^5+1)/(x^2(x+1)^2)\). At 0, subtract the Artin–Schreier coboundary \((1/x)^2+1/x\); the remaining pole has order one. At 1 the original pole has order one, and at infinity it has order one. The degree-two separable map therefore has different contribution two at each of three points, giving 2g−2=−4+6=2.

The rational function x/(x+1) has divisor 2P−2Q. The class [P−Q] is nonzero, because a function with divisor P−Q would give a degree-one map to the projective line, impossible in positive genus. Hence its exact order is two. Both point sections become equal up to geometric conjugation in the entire extension by \(\Delta_C^{\rm ab,(2')}\), by finite-field Kummer theory. The program gives N_1=N_2=3 and #J_C(F_2)=4, consistently.

The full AG.40 input does not survive replacing all groups by their geometric abelianizations. At a once-punctured curve the sole puncture inertia is zero in the geometric abelianization, since the puncture word is a product of commutators. Thus there is no central cusp kernel Z_r(1) in that abelianized punctured group and no cocycle with residue +1 at that cusp. Moreover, even the cohomology-retention statement needed for point recognition fails for general open subgroups of the proper abelian quotient: an index-r geometric subgroup has r-adic abelian rank 2g, while its actual degree-r étale curve cover has genus 1+r(g−1), hence r-adic rank 2+2r(g−1)>2g. Therefore the relevant failure occurs before using finite exceptions or Kummer evaluations; AG.39.15 must be applied to the full punctured pro-prime-to-p group and its actual cuspidal kernel, not to an abelianized replacement.

### 7.3. Every singleton prime set has infinitely many exceptions

**Elementary automorphism lemma.** Let D be a finitely generated pro-r group, with Frattini quotient \(D/\Phi(D)\cong F_r^d\). Then the kernel of Aut(D)→GL_d(F_r) is pro-r.

Here is a proof avoiding an unopened automorphism theorem. For a finite r-group H, every maximal subgroup has index r, so a tuple whose images generate H/Φ(H) generates H. Fix one basis of H/Φ(H), and consider the set of all ordered lifts of that basis to H. It has cardinality |Φ(H)|^d, an r-power. The kernel of Aut(H)→Aut(H/Φ(H)) acts freely on this set: fixing a generating tuple fixes H pointwise. Therefore the kernel's order divides this r-power, so it is an r-group. A finitely generated pro-r group has a cofinal system of open characteristic subgroups (intersect all subgroups of bounded index). Its finite quotients are r-groups; the image of Φ(D) in each is the finite quotient's Frattini subgroup. Passing to the inverse limit of the preceding finite kernels proves the assertion.

Now assume C/k proper hyperbolic has a rational point O, write Δ_r for its geometric pro-r group, and use s_O to express Π_C^{\{r\}}=Δ_r⋊G_k. The Frattini rank is d=2g. Choose a prime q different from r and not dividing |GL_d(F_r)|. The q-adic direct factor \(Z_q\subset\widehat Z=G_k\) has trivial image under G_k→Aut(Δ_r): its image in GL_d(F_r) is a q-group, hence trivial, and its remaining image in the pro-r kernel is both pro-q and pro-r, hence trivial. Consequently s_O(Z_q) is central in the entire arithmetic group.

For every closed point x of degree divisible by q, choose h∈Z_q with q-adic coordinate 1. This h acts nontrivially on a geometric point over x, because its image modulo deg(x) is nonzero. Let z=s_O(h), and choose any lift \(\tilde x\) in the universal pro-cover. Then z\tilde x differs from \(\tilde x\) already on the geometric curve, whereas

\[D_{z\tilde x}=zD_{\tilde x}z^{-1}=D_{\tilde x}.\]

Thus x is exceptional. There are infinitely many such closed points: for sufficiently large j the Weil bound implies \(\#C(k_{q^j})>\#C(k_{q^{j-1}})\), so there is a point of exact degree q^j. If C(k) is empty, first take a finite constant extension with a point; the equality of exceptional inverse images under constant extension shows that infiniteness descends. Therefore E_C^{\{r\}} is infinite for every proper hyperbolic C over every finite field of characteristic different from r.

This proof gives actual all-level collisions after finite extensions. It also shows exactly why ST2009's cofiniteness hypothesis cannot be omitted from AG.40's finite-exception argument. We make no inference that arbitrary finite sets with more than one prime have virtually pro-Σ automorphism groups; that would require a separate theorem and is not supplied here.

### 7.4. Explicit noncofinite collision

Let \(L=F_2[t]/(t^7+t+1)\), and take \(C/L:y^2+y=x^5\) with O=∞. It is smooth of genus two. The program verifies the field identity for every nonzero element of the 128-element ring, so irreducibility of the chosen modulus is checked rather than assumed. Put

\[P=(t,t^6),\qquad Q=(t^2,t^6+t^5).\]

They satisfy the equation and Q is the F_2-Frobenius image of P. The orbit has seven distinct points; the code gives their complete coordinates. Work in the geometrically pro-three quotient over F_2. We have \(|GL_4(F_3)|=24\,261\,120\), which is not divisible by seven. The preceding argument gives a central image of Z_7⊂G_{F_2}. Its element with seventh-adic coordinate 1 has image 1 in Gal(L/F_2), so sends a lift of P to a lift of Q while leaving the decomposition group unchanged. Intersect that common decomposition subgroup with the preimage of G_L. This gives equal section subgroups for the two L-rational points in the entire geometrically pro-three arithmetic group over L.

The program finds #C(L)=129, of which 126 points have exact degree seven over F_2, making 18 exceptional degree-seven closed points. Infinitely many other degrees are handled by the preceding theorem; no bounded computation is being used to prove infiniteness.

## 8. What remains outside this audit

The general classification asked in A12 for arbitrary nonempty Σ⊂Primes−{p} is not supplied by the preceding results. We have proved the singleton case (infinite), the empty set gives a trivially infinite exceptional set, and ST2009 proves finiteness for every cofinite set. The additional passage from finiteness to emptiness requires the configuration transport to be checked for the corresponding Σ. The main full-prime-to-p emptiness implication also requires that transport. We do not label the full A12 item complete on the basis of these cases.

Neither class-number witness existence nor fixed norm-module vectors follows from the conditional criterion alone. The proof has not inserted either of those unproved claims as an input.

## 9. Strengthening: proper-field support replaces finiteness

The following strengthening was suggested independently during the parallel audit and checked here. It is useful both for an independent proof of the main theorem and for the J_C-large prime sets in ST2017.

Fix any nonempty Σ⊂Primes−{p}, any r∈Σ, and use the full proper geometric pro-Σ group in the definitions of G_P,G_Q. The same-prime lemma, compactification comparison, central extension construction, and self-normalizer argument remain valid. Assume β is a cusp-preserving isomorphism over id_{Π_C^Σ}. Suppose that there is a proper algebraic subfield F⊊\bar k containing k such that, for every closed R whose geometric points are not F-rational, the point transported by β has the same label R. Then P=Q.

Only the final Kummer argument changes. Let n be the exact order of [P−Q] in J_C(k), and choose f∈k(C)^× with div(f)=n(P−Q). This order exists because J_C(k) is finite. The argument for the central extensions uses neither that n is p-primary nor that n is coprime to r: the difference κ_r(f)−nχ has zero residues, hence is a constant class κ_r(a), and χ evaluates to zero at every point with unchanged label. Thus κ_r(f(R)/a)=0 for every such R.

The function f/a is not an r-th power in \(\bar k(C)^×\). If r∤n its valuations at P,Q already rule this out. If r|n and f/a=b^r, then div(b)=(n/r)(P−Q), contradicting the exact order of [P−Q]. The geometric divisor class has the same order as its k-rational class, since J_C(k)→J_C(\bar k) is injective. Equivalently, a rational principal divisor descends by Hilbert 90.

Let D be the smooth compactification of the Kummer cover z^r=f/a. It is geometrically connected, since r is prime and f/a is not a geometric r-th power; r≠p makes it generically separable. Take a finite L/k containing μ_r. Because F is a proper subfield of \bar k, some prime ell has finite exponent in the supernatural degree [F:k]. To see this directly, the nonzero closed subgroup G_F⊂\hat Z has a nonzero ell-adic projection for some ell, and a nonzero closed subgroup of Z_ell is open. Put L_m equal to the degree-ell^m extension of L. Then

\[F_0=F\cap\bigcup_m L_m\]

is a finite extension of k: the degrees outside ell are bounded by [L:k], and the ell-part of [F:k] is bounded. Thus all excluded F-rational points lying in C(L_m) belong to the fixed finite set C(F_0). Write B=#C(F_0)+2, including P,Q.

For every remaining R∈C(L_m), the zero r-adic Kummer class implies that f(R)/a is an r-th power in L_m. Since μ_r⊂L_m and f has no zero or pole away from P,Q, the fibre of D above R consists of exactly r L_m-rational points. Hence

\[\#D(L_m)\ge r\bigl(\#C(L_m)-B\bigr).\]

Writing Q_m=#L_m and applying the Weil bounds to the geometrically connected proper curves C and D gives

\[(r-1)(Q_m+1)\le (2g_D+2r g_C)\sqrt{Q_m}+rB.\]

This is impossible as m→∞. Thus P=Q. The auxiliary ell is allowed to equal p or r; the extension is an extension of finite constants and no ramification issue occurs. Only the Kummer degree r must be different from p.

In particular, if E_C^Σ is supported over a proper algebraic subfield, the needed same-label assertion follows from compactness recognition and the definition of E. Thus, once the generalized configuration transport is established, *almost Σ-separated* in the sense of ST2017 implies *Σ-separated*, i.e. E_C^Σ=∅. This conclusion uses no finiteness assertion about E_C itself.

The finite-exception case is a special case: finitely many closed-point residue fields generate one finite F, which is proper in \bar k. In fact the original roots-of-unity proof also works directly with arbitrary n, so no coprimality condition was hidden there.

## 10. An independent proper-field bound for p-primary point differences

We can remove the Boxall finiteness input entirely from an alternative proof of the main point-separation theorem. Define

\[B_C=\{R\in C(\bar k):\exists S\ne R,\ [R-S]\in J_C(\bar k)[p^\infty]\}.\]

We prove that B_C is supported over one proper algebraic subfield of \bar k. This is a statement about divisor classes, not a replacement of group collisions by a claimed converse.

### 10.1. The fibres of the difference map

For every nonzero t∈J_C(\bar k), the set

\[\{(R,S)\in C(\bar k)^2:R\ne S,[R-S]=t\}\]

has at most two elements. Indeed, for two such pairs, R+S' is linearly equivalent to R'+S. If these effective degree-two divisors are equal, the nonzero-difference condition forces the ordered pairs to be equal. Otherwise they define a degree-two pencil on C. There is at most one such pencil when g≥2: two distinct degree-two maps would give a birational map of C to a curve of bidegree (2,2) in P^1×P^1, whose arithmetic genus is one, impossible. The degree-two pencil is separable even in characteristic two, because a purely inseparable degree-two map to P^1 would identify C with a Frobenius twist of a rational curve, again impossible in positive genus. Denote its involution by iota. Equality of the two fibre divisors then forces (R',S')=(iota(S),iota(R)). This is the sole possible second pair.

### 10.2. A nontrivial arithmetic subgroup fixing all p-primary torsion

Let f be the p-rank of J_C. Then \(T_pJ_C\cong Z_p^f\) and its finite quotients identify with the geometric p-power torsion groups. Choose an odd prime ell≠p not dividing |GL_f(F_p)|, with |GL_0(F_p)|=1. The kernel of GL_f(Z_p)→GL_f(F_p) is pro-p, as its congruence filtration has elementary abelian p-group successive quotients. The ell-adic factor H=Z_ell⊂G_k has trivial image in GL_f(F_p), since the latter order is prime to ell; its image in the pro-p congruence kernel is also trivial. Thus H fixes all of J_C(\bar k)[p^∞].

If t=[R−S] is a nonzero p-primary difference, H acts on the at-most-two-element fibre over t. A pro-ell group with ell odd cannot act nontrivially on a set of cardinality at most two. Hence H fixes R and S individually. Therefore

\[B_C\subset C(F),\qquad F=\bar k^H\subsetneq\bar k.\]

If f=0, the p-primary torsion group itself is zero, so B_C is empty because the Abel map of a positive-genus curve is injective.

### 10.3. Application to the conditional criterion

From the compactness proof, β carries the point R to an actual target point S over the same finite field. Because β is over id_{Π_C}, their full proper point sections have equal geometric conjugacy class. Passing to the Jacobian Kummer map proves [R−S] is p-primary. This is only the necessary implication from group collision to divisor-class torsion, which has already been proved in Section 5.1. Therefore R outside B_C must have S=R.

Section 9 now applies with the explicit proper field F above and proves P=Q. This independently establishes the conditional cuspidal criterion without ST2009's exceptional-set finiteness, Boxall's theorem, or an assumption that a p-primary divisor difference produces a group collision. It retains only the exact cusp isomorphism as input, the full same-prime compactification lemma, the compactness recognition, the elementary degree-two-pencil bound, standard curve cohomology, finite-field Kummer theory, and the Weil bound.

Consequently, after the independent verification of AG.41 and AG.42, this is an alternative complete route to the main theorem. The original K1 audit remains useful for checking the earlier proof exactly as written, but it is not an indispensable external premise of this replacement proof.

## 11. General J_C-large sets and the finite-or-infinite dichotomy

For any nonempty Σ⊂Primes−{p}, put

\[T_{\Sigma'}J_C=\prod_{s\in\Sigma'}T_sJ_C,\qquad H=\ker(G_k\to\operatorname{Aut}(T_{\Sigma'}J_C)).\]

Here the p-adic Tate module means the étale p-adic module, of rank equal to the p-rank. Under the ST2017 definition, Σ is J_C-large exactly when H is nontrivial. Every Σ'-primary geometric torsion point is fixed by H. The fibre argument of Section 10.1 shows that 2H fixes each ordered pair realizing a nonzero Σ'-primary difference. Since multiplication by two is injective on the closed subgroup H⊂\hat Z, 2H is still nonzero. Thus

\[B_C^\Sigma\subset C(\bar k^{2H}),\qquad \bar k^{2H}\ne\bar k.\]

This recovers and makes explicit the support mechanism of ST2017 Proposition 2.12: for a nonhyperelliptic curve the fibre is a singleton, so H itself suffices; for a hyperelliptic curve one may need the index-at-most-two subgroup 2H.

In the generalized criterion, compactness carries each R to S with [R−S] Σ'-primary by Kummer theory at all primes in Σ. Hence outside B_C^Σ the labels agree. Section 9 then proves the generalized conditional criterion for every J_C-large Σ. If the configuration transport is verified for arbitrary nonempty Σ, it follows that E_C^Σ=∅ for every J_C-large Σ and every proper hyperbolic C over a finite field. Every cofinite Σ is J_C-large: choose an auxiliary odd ell outside the finite set Σ' and outside the prime divisors of all finite groups GL_rank(T_s)(F_s), s∈Σ'; then Z_ell acts trivially on the complementary Tate module.

Even without J_C-largeness, finiteness of E_C^Σ supplies finite-field support and Section 9 applies. Therefore, again under the generalized transport theorem, a finite exceptional set must be empty. Every E_C^Σ is consequently either empty or infinite. This is a dichotomy, not a classification of which alternative occurs for every arbitrary Σ. The singleton theorem in Section 7.3 supplies explicit infinite cases; the J_C-large theorem supplies empty cases. We have not proved that these exhaust all possible prime sets.

## 12. Literal ST2017 prime-set scope, including the characteristic prime

The criterion and exception equivalence now allow every prime set Sigma containing at least one r different from p. The auxiliary Kummer cover, orientation class, same-prime lemma, and r-adic curve cohomology all use that r. Including p in Sigma creates no new requirement for those steps. Configuration transport is supplied by the independently audited algebraic Stix route (not by an unjustified characteristic-zero lift of a p-cover).

For the complementary-prime support assertion, the p-Kummer comparison is explicit. Over an algebraic closure, [p^n] is surjective on Jacobian points with kernel J[p^n](kbar). Quotient first by the connected component J[p^n]^0; that quotient is radicial and induces a bijection on geometric points, and the remaining isogeny to J is finite etale with geometric kernel J[p^n](kbar). Thus the usual division-point Kummer cocycle is exactly the cocycle seen by these etale isogenies. Milne, Jacobian Varieties, Proposition 9.1 identifies the abelian curve fundamental group with that of J for all primes, including p. Passing to the inverse limit detects the whole p-primary subgroup of finite J(L). This needs no ordinary hypothesis. Source A.CR4/7/9/10 and their JSON statements have been updated.

## 13. R6 parity scope and an exact negative control for one lemma

The direct free-action stabilizer argument works for a nontrivial odd-order deck element: a fixed [Q'-P'] forces the hyperelliptic pencil, hence a^2 fixes a point, impossible for a free odd-order action. It cannot simply be stated for a free involution in odd characteristic.

Exact control over F7: D:y^2=x^8+1 has genus three, delta(x,y)=(-x,-y) is fixed-point free, and the quotient C:v^2=u^5+u has genus two via (u,v)=(x^2,xy). The affine fixed-point equations force x=y=0, off D; at infinity delta exchanges the two points. Let P'=(1,3),Q'=(-1,3). Their images (1,3),(1,4) in C differ. Nevertheless delta(P')=iota(Q') and delta(Q')=iota(P'), so delta(Q')+P' and Q'+delta(P') are fibres of the hyperelliptic pencil. Thus delta fixes [Q'-P']. Code criterion_r6_control.py checks all finite data and records the geometric smoothness/fixed-point arguments. This is a counterexample only to that unrestricted stabilizer lemma: no p-primary assertion or point-section collision is claimed. The full R6 implication can be distinguished from its direct odd-order proof and, after A1, is in any case vacuously true as an exclusion of collisions.

## 14. Independent rational witnesses on R8

The parent generated two finite exact candidates; I independently read the producer and verified the normalization and cohomological formulas, then wrote criterion_r8_verify.py without importing producer routines. It uses independent binary Rabin field tests and a separate CRT interpolation path to reconstruct every multiple of the supplied generator, checks every tangent doubling and its Y-coordinate sign, rechecks the elliptic pullback description, and recomputes every Frobenius product by direct powers rather than the producer's recurrence.

Both candidates are verified. Degree 191 works over F_(2^380), extension degree ten of the original F_(2^38); degree 229 works over F_(2^152), extension degree four. The full input JSONs retain all 190 or 228 nonzero reduced multiples, Cartier coefficients, and linear Frobenius multipliers. All coefficients and multipliers are nonzero; none of the multipliers is one. Additional identities A_(2i)=A_i^2, A_(-i)=A_i, A_i^(2^19)=A_i, and A_(-2^19 i)=A_i^(2^38) hold exactly. The nineteen-degree minimal polynomial bit encodings are 892407 (multiplicity ten) for 191; 713865,785567,913207 (each multiplicity four) for 229. These are coherent mod-two characteristic polynomials; no characteristic-zero zeta polynomial is asserted.

The monic normalization uses no extension: after reducing A(u)^3 to a5*u^5+b3*u^3+b1*u+b0, set u=a5*x and y_original=a5^3*Y+S(a5*x). This gives monic f and constant h=a5^-3. For degree-two Mumford representatives, V_i=v_i+u_i*((f+v_i^2+h*v_i)/(u_i*h) mod u_i); norm identity V_i^2+h*V_i+f=V_i3^2*u_i^2*u_(2i) proves the normalized doubling function g_i=(Y+V_i)/(V_i3*u_(2i)). With t=x^2/Y, its leading unit is one. The residue Cartier calculation gives c_i=V_i3*(u_(2i))_1. Rigidification at infinity makes this the P-split twist, not a different constant torsor. The Artin-Schreier comparison proves that all A_i!=1 is exactly absence of rational new two-torsion, hence odd relative class number.

The pointed hyperelliptic involution commutes with the pointed Frobenius descent and inverts deck transformations. Over the first constant-deck field, the new etale cohomology is rank zero or one over each nontrivial F2[Z/ell] factor, and Frobenius is multiplication by a unit fixed by <s,-1>, s=-2^19. If 19 does not divide ord_ell(2), this fixed ring is a product of F2, so the unit is one. The independently certified R8 geometric counterexample has positive primitive two-rank for every nontrivial odd cover, so all such primes fail over every extension. Every odd prime below 191 has 19 not dividing its order: the hypothetical values 19j+1 below 191 are 39,77,115,153, all composite. The degree191 success therefore proves the exact least prime over all extensions. Orders of s modulo191,229 are ten,four, proving the stated minimal field degrees for each specified prime.

Complete inclusion sections/B_root_r8_witness.tex (B.W1–B.W3) and notes/r8_witness_statements.json are ready. All ten hexadecimal entries were mechanically compared against the verified JSONs. Isolated LuaLaTeX compilation succeeds in five pages with no overfull box, missing glyph, or undefined citation; the only isolated missing hyperlink is B.R5, supplied in the integrated paper.

## 15. B1 approaches pushed past the previous criteria

The universal assertion is still not proved. The exact successes above are a new positive instance, including a least-prime result, rather than a claim to settle every curve.

(a) A fixed cover that fails the rational criterion remains bad after every constant extension, because its rational p-torsion persists. Choosing a larger field therefore cannot repair a fixed pointed cover. One must vary the character or cover.

(b) A large quotient A=J(L)_(p') does not supply a prime quotient with both sufficiently large rank and primitive-root behaviour. Failure for every prime-cyclic quotient only gives at least one p-character orbit of zeros on each projective character line; it does not make every nontrivial Fourier coefficient vanish. The corrected pair count cannot be applied as if it did. For a fixed p, unconditional existence of enough primes with p primitive is not available from the elementary arguments; appealing to it would hide an Artin-type problem.

(c) Higher genus adds effective-divisor terms through degree g-1. Point occupancies alone, even together with p>(2g-2)^2, no longer compute L_P(chi,1) modulo p. Replacing them by theta/effective-divisor occupancies has not yielded a bound that forbids one zero orbit on every projective line.

(d) The following unpointed twist bound is independently derived. Let a constant cyclic degree-ell cover be fixed, f=ord_ell(p), and W its new etale Fp cohomology. Every factor F_(p^f) of Fp[Z/ell] has W-rank at most g-1 by coherent character dimension. Frobenius is linear over that factor. Twisting by deck translation delta^t multiplies its matrix by zeta^t. At most g-1 choices of t make one a resulting eigenvalue on a given factor; conjugate characters give the same t. There are (ell-1)/f factors, so at most (g-1)(ell-1)/f of the ell twists have rational new p-torsion. Thus when f>=g-1 a good unpointed twist exists; in genus two this holds for every constant prime-cyclic cover. This does not solve B1 because splitting at the prescribed P selects one particular twist. Extending by ell to split that fibre can turn all ell-order nontrivial eigenvalues into one. There is no transfer from the good unpointed twist to the required pointed twist without an additional argument.

(e) For supersingular scalar Frobenius, the pointed-involution fixed-ring argument gives a uniform finite field for multipliers only after allowing a field depending on the order of Frobenius on the deck group. Trying to kill every multiplier by one base-field extension fails because those deck-group orders have unbounded valuations at the multiplier-order primes. The first constant-deck degree can absorb the chosen extension and remove precisely the power intended to kill the multiplier. The R8 degree191 and229 successes make clear that the geometric positive-rank obstruction by itself is not a rational nonexistence theorem.
