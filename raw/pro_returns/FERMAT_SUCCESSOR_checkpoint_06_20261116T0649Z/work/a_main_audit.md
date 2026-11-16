# Independent audit of LM6 E.6--E.12

AI-produced research notes for the parent agent. No priority claimed. Source work is not a mathematical authority.

## Main outcome

The Selmer theorem for every odd exponent survives, but the printed proof does **not** hold at every line. There is an additional error, beyond the already identified false assertion about `Y_1(7)(Q)`: the cusp Tate parameter has a nonzero leading-coefficient Kummer term. In Steklov's source this originates in Proposition `prop:ramificationindexforcuspidal` (Section 4, source lines 711--729). LM6 E.8 repeats the incorrect conclusion that the cusp parameter is divisible by the Fermat exponent. The repair below supplies all the conductor and finite-flatness conclusions used by the proof, with the sharper twisted Serre level 2.

The numerical constants and finite counterexample below have been checked by `deliverable/code/a_main_exact.py`; the complete successful output is `deliverable/code/a_main_exact.out`. The initial script assertion compared unequally expanded SymPy expressions syntactically; it was corrected to test that their difference is zero. This was a test-harness error, not a mathematical correction.

## 1. Exact local cusp calculation

Let `k` be characteristic zero, `ell >= 5` prime, and let `U_ell` be the plus Fermat curve with the three coordinate divisors removed. On the tripod the Legendre parameter is `t = -X^ell/Z^ell` and

`j(t) = 256 (t^2-t+1)^3 / (t^2(t-1)^2)`.

At any `k`-rational cusp choose the following uniformizer in the completed local field:

| Cusp divisor | Uniformizer | Legendre parameter |
|---|---|---|
| `X=0` | `u=X/Z` | `t=-u^ell` |
| `Y=0` | `u=Y/Z` | `t=1+u^ell` |
| `Z=0` | `u=Z/X` | `t=-u^(-ell)` |

All cusps in a given divisor have the same displayed computation, including those only rational over a completion. At each cusp,

`1/j = 2^(-8) u^(2ell) h_0(u)`, with `h_0(0)=1`.

The universal formal Tate parameter satisfies `q = j^(-1)+O(j^(-2))`, so

`q = 2^(-8) u^(2ell) h(u)`, `h(0)=1`.

Every `1+u k[[u]]` unit has a compatible system of all positive integral roots, by the binomial series (or Hensel's lemma with derivative a nonzero element of `k`). Its Kummer class in `H^1(k((u)), Zhat(1))` is zero. After removing the quadratic character of the potentially multiplicative Legendre family, a cuspidal section `s` therefore has Tate extension class

`q(s) = -8 kappa(2) + 2ell s^*kappa(u)`.

In particular, the mod-ell extension class is **`-8 kappa_ell(2)`**, independently of the tangential parameter. It need not vanish.

### Complete counterexample to the printed divisibility assertion

Take `ell=5`, `k=Q_2`, the rational cusp `X=0`, and the tangential section with `s^*kappa(u)=0`. The valuation map on `H^1(Q_2,mu_5)` sends `q(s)` to `-8 mod 5 = 2`. Thus the residual extension is nonsplit and the class is not divisible by 5 in `H^1(Q_2,Zhat(1))`.

The corresponding tame representation can be written, up to unramified upper-triangular change, with

`tau = [[1,2],[0,1]]`, `phi = [[2,0],[0,1]]` in `GL_2(F_5)`.

The script checks `tau^5=1`, `tau !=1`, `phi*tau*phi^(-1)=tau^2`, and that these matrices generate a group of order 20. Hence the failure is visible in a completely explicit finite quotient. The local representation before the Tate quadratic twist may carry an additional scalar quadratic factor; this does not alter the nonsplit extension after that twist.

The precise general correction is this. If a map of completed punctured local curves has `q=a u^e h(u)` with `a in k^x` and `h(0)=1`, then its map on section packets is

`b |-> kappa(a)+e b`.

It is an affine map of torsors, not multiplication by `e` after arbitrary independently chosen origins. The claimed `k`-isomorphism `k((u)) = k((q^(1/e)))` in Steklov is false unless the leading coefficient is an `e`th power (up to the precise parameter change). Over `kbar` it is true; that geometric statement cannot remove the arithmetic Kummer term.

## 2. Complete local table used for residual modularity

For a local point write `a^ell+b^ell+1=0` and `t=-a^ell`. Let `delta_p` denote the quadratic splitting character when the elliptic curve has potentially multiplicative reduction. This may be ramified; no assumption that it is unramified is permissible.

If `v_p(a) !=0`, direct evaluation gives

`v_p(j)=8 v_p(2)-2ell |v_p(a)|`.

If `v_p(a)=0` and `t ==1 mod p`, use `1-t=-b^ell`, giving the same formula with `b`. If `p` is odd and `t` and `1-t` are units, the integral Legendre model has discriminant `16t^2(1-t)^2` a unit and hence good reduction. At `p=2` this last case is impossible; one of `a,b` supplies a nonzero valuation. For `ell>=5`, `v_2(j)<0`.

After the local splitting twist, the potentially multiplicative case is a split Tate representation

`0 -> F_ell(1) -> V -> F_ell ->0`

with Kummer parameter `q`, and `v_p(q)=-v_p(j)`.

| Local situation | After the chosen quadratic twist |
|---|---|
| good reduction, `p != ell` | unramified on `V` |
| potentially multiplicative, odd `p != ell` | `ell | v_p(q)`, so Kummer extension unramified; `V` unramified |
| good reduction, `p=ell` | `E[ell]` is generic fibre of finite flat `E[ell]/Z_ell`; Serre weight 2 |
| potentially multiplicative, `p=ell` | `ell | v_ell(q)`, so `q` modulo ellth powers has a unit representative; the Kummer extension has a finite flat model and weight 2 |
| local point, `p=2` | `v_2(q)=2ell m-8`, so nonzero modulo ell; tame nontrivial unipotent inertia, conductor exponent exactly 1 |
| cusp, `p !=2,ell` | extension class `-8kappa_ell(2)` is unramified; conductor exponent 0 |
| cusp, `p=ell` | `2^(-8)` is a unit; finite flat Kummer extension, weight 2 |
| cusp, `p=2` | `v_2(2^(-8))=-8` nonzero modulo ell; tame unipotent inertia, conductor exponent exactly 1 |

For the tame assertions, on inertia at `p!=ell` the cyclotomic mod-ell character is trivial. Units acquire ellth roots over the maximal unramified extension, since its residue field is algebraically closed and ell is invertible. Therefore the extension restricted to inertia is measured precisely by the valuation modulo ell. Wild inertia is a pro-p group and has no nontrivial map to the additive ell-group. Nontrivial unipotent inertia fixes a line, so its Artin exponent is 1. This also proves the sharper exponent at 2 instead of the printed bounds 2 or 4.

For finite flatness at `ell`, an extension of `Z/ell` by `mu_ell` attached to a unit comes from the finite flat Kummer torsor over `Z_ell`; the extension group scheme can be constructed on the disjoint union of the torsors `z^ell=a^i` for `i=0,...,ell-1`, with the multiplication divided by `a` when the exponents cross ell. Equivalently, the standard finite-flat Kummer classification applies. Serre (1987), Proposition 4 and Proposition 5, Section 2.9, identify its weight as 2. We opened the author's primary PDF: `https://www.college-de-france.fr/media/jean-pierre-serre/UPL5835292064138487263_Serre_Repr.modulaires_Galois.pdf`. Proposition 5 is printed on p.191; it gives good reduction weight 2 and multiplicative reduction weight 2 precisely when `ell | v_ell(j)`.

Ramified versus unramified quadratic twists are treated uniformly: tensor the original local representation by `delta_p`. If a later global twist has the same restriction to inertia, their quotient is unramified. Unramified quadratic twisting preserves unramifiedness, the tame conductor exponent, and finite flatness (by finite étale descent).

## 3. From the local table to R3

The residual representation attached to a global section is continuous into a finite group, hence ramified at only finitely many rational primes. The local splitting quadratic characters can be chosen trivial on inertia outside a finite set: in the good reduction case choose 1, and outside `2ell` a ramified scalar quadratic twist could not produce an unramified original residual representation, since ell is odd. By the cyclotomic reciprocity isomorphism

`G_Q^ab = product_p Z_p^x`,

the product of the finitely many specified inertia quadratic characters yields a global quadratic character `delta`. Its restriction differs from each local choice by an unramified quadratic character. Thus `rho_bar tensor delta` has determinant `chi_bar_ell`, Serre weight 2, and prime-to-ell conductor **2**. The printed conclusion that the level divides 16 is true but weaker.

If the representation were irreducible over `F_ell`, it would be absolutely irreducible. Indeed complex conjugation has eigenvalues `1,-1` (determinant cyclotomic, ell odd). Any invariant line over `Fbar_ell` is one of these two eigenlines, both already defined over `F_ell`, contradicting irreducibility. The representation is odd for the same reason.

The precise Serre modularity theorem therefore supplies a weight-two form of level 2 and trivial character. There are no such forms because `X_0(2)` has genus zero. This contradiction proves reducibility. If using only level-divides-16, the character can likewise be taken trivial: its reduction is trivial by the determinant, and characters modulo a divisor of 16 have 2-power order, on which reduction at ell>=5 is injective. Each `X_0(1),X_0(2),X_0(4),X_0(8),X_0(16)` has genus zero. The level-2 refinement avoids this auxiliary point.

Primary sources opened: Khare--Wintenberger I (`https://www.math.ucla.edu/~shekhar/papers/results.pdf`), II (`https://www.math.ucla.edu/~shekhar/papers/proofs.pdf`). The relevant statement in I is **Theorem 9.1**, together with the Kisin input proving its Hypothesis (H), not Theorem 1.2(1) alone: the latter assumes odd conductor and would not cover level 2. The primary Kisin abstract explicitly states that it proves (H), at `https://dash.harvard.edu/entities/publication/73120378-e139-6bd4-e053-0100007fdf3b`; the author's linked full text is DVI and requires separate access before the user's strict 'theorem opened' requirement is called fully met. This is an access/verification remainder, not a conjectural modularity assertion.

After reducibility, at `p=ell` the good supersingular case cannot occur: the inertia representation of an elliptic curve with good supersingular reduction over the unramified field `Q_ell` is irreducible, whereas a global stable line remains stable locally. The ordinary case has inertial semisimplification `1+chi_bar_ell`; the multiplicative and cusp cases do too after the splitting twist. Patch the inertia characters again and let the two global diagonal characters be `omega` and `chi_bar_ell omega^(-1)`. Both are unramified away from ell, and one is unramified at ell. That character cuts out a finite extension unramified at all finite primes; Minkowski's discriminant theorem forces it to be trivial. Hence the global semisimplification is `1+chi_bar_ell`. A quadratic twist acts trivially on `E[2]`, so full rational two-torsion is preserved.

## 4. R1: finite support, with a full reduction

For a smooth geometrically connected hyperbolic `U/Q`, put `X` for its smooth compactification. A Selmer section means that its restriction at **every** completion is represented by a point or by a rational cusp section. At the real place a point contributes its connected component, not a unique point.

Let `Z` be a finite reduced subscheme of `X` supporting all finite localizations. For a finite étale neighbourhood `U'->U` of the section, its lifted local section is again point or cusp. At an interior local point, containment of the section image in the open subgroup defining the cover means a fixed coset in the finite geometric fibre, hence a rational point in that fibre. At a cusp, intersect its decomposition group with that subgroup: since it contains the lifted local section, it surjects to the local absolute Galois group and the corresponding cusp has residue field the base field. These are exact comparison maps in the direction required.

One may take a cofinal set of such neighbourhoods with compactification genus at least one. To make the usually abbreviated reduction explicit, if a given compactification already has genus at least one, every finite cover does too. If it has genus zero, it has at least three punctures. Take the kernel of mod-3 abelianization of its geometric free group. This subgroup is characteristic, and the fixed section twists it to a neighbourhood over Q. Its degree is `d=3^(r-1)` and each of its `r>=3` boundary inertia groups has ramification index 3. Riemann--Hurwitz gives `2g'-2=d[-2+2r/3]>=0`. Applying this after any initially prescribed neighbourhood proves cofinality.

Let `X'` be such a compactification and `Z'` the reduced inverse image of `Z`. The global section of `X'` has the chosen local point classes. Harari--Stix, Theorem 2.1 in the supplied source (`numbers`, lines 626--654), converts these classes to an adelic point surviving all finite torsors. Its assumptions hold: Q is a number field; `X'` is smooth, proper, geometrically connected; every completion has the given point; the section and its conjugacy comparisons supply condition (iii). In particular it survives finite abelian descent. Stoll, Theorem 8.2 (`BM0`, supplied source lines 2249--2273), applies because `g(X')>=1` and finite places form a density-one set. It gives a rational point of `Z'`.

For all neighbourhoods, the finite nonempty sets `Z'(Q)` have a nonempty inverse limit: any finite collection has a common neighbourhood refinement, and its point maps to the collection. A compatible pro-point over some `z in Z(Q)` has stabilizer the corresponding point decomposition group (for `z in U`) or cusp decomposition group (for `z in X-U`). The section fixes the pro-point by construction. Thus it is point-induced or cuspidal.

The same proof works if the support condition is imposed on any density-one set of finite places, provided the section is Selmer at all places so that the full adelic descent object exists. For the stated consequence, a nonconstant `f:X->W` sends that object into `W(A)_bullet^f-cov=W(Q)`, so it maps to one rational point `w`. The fibre `f^(-1)(w)` is finite; apply the result. No separate finiteness hypothesis on the entire set `W(Q)` is necessary.

Stoll's erratum was opened in full at `https://mathe2.uni-bayreuth.de/stoll/papers/Errata-FiniteDescent-ANT.pdf` (dated March 29, 2017). Section 3 corrects the use of real fibres in Proposition 8.5: only density-one finite support is required. We therefore never replace a real component by a particular point of a scheme-theoretic fibre. The erratum also corrects some abelian-torsor connectedness claims, but explicitly preserves the genus-one descent identities used to obtain Theorem 8.2; our Harari--Stix input supplies full finite descent, avoiding that faulty connected-component shortcut.

## 5. R2 and R4: level 4ell and Mazur

On the finite étale cover `Z_ell` of the tripod parametrizing a cyclic order-ell subgroup `C` of the Legendre elliptic curve, write `P=(0,0)`, `Q=(1,0)`. Let `phi:E->E'=E/<P>` be the degree-two isogeny and `phi':E'->E` its dual. Then

`H_4=(phi')^(-1)(<Q>)`

is a rational cyclic subgroup scheme of order four: if `phi'(R)=Q`, then `2R=phi(Q)!=0`, so `R` has order four. The subgroup `phi(C)` has order ell; coprimality makes `H_4+phi(C)` cyclic of order `4ell`. This gives a Q-morphism `Z_ell->Y_0(4ell)`. It is nonconstant since a fixed elliptic curve has only finitely many degree-two isogeny partners while the Legendre `j` varies. On projective smooth compactifications it is finite and surjective componentwise. Any connected arithmetic component supporting a section is geometrically connected: the section surjects onto `G_Q`, forcing its constant field to be Q.

For `N=4ell`, the modular index is `6(ell+1)`, the cusp number is six, and the elliptic-point counts of orders two and three both vanish. The genus is `(ell-3)/2`, positive for ell>=5. These formulas were checked at ell=3,5,7,11,13,17,19,23 by the exact program, and the elementary modular genus formula proves them for all odd primes.

The invariant line of R3 supplies a lift of the tripod section to `Z_ell`. The lift is Selmer by the finite-fibre argument above. Stoll's Corollary 8.8, read in the supplied primary source at `ModCurves` lines 2387--2406, says every positive-genus `X_0(N)` is excellent for finite abelian descent; hence also for all finite descent because `X_0(N)(Q) subset f-cov subset f-ab`. Its hypotheses are exactly the modular curve over Q and positive genus verified here. R1 makes the lifted section, and then the tripod section, rational or cuspidal. This corrects Steklov's failure at ell=5 by using level 20 instead of level 10.

If a rational tripod point occurs, the given section's containment in the subgroup of `U_ell` fixes a finite fibre point, so it comes from an actual rational point of `U_ell`. Its Legendre elliptic curve has full rational two-torsion. After the quadratic twist from R3, the residual stable line has character 1 or `chi_bar_ell`. In the former case the curve has a rational point of order ell. In the latter, quotient by the stable `mu_ell` subgroup. The dual isogeny has constant kernel `Z/ell`, so the quotient has such a point. The odd-degree isogeny induces an isomorphism on two-torsion. In either case one obtains an elliptic curve over Q with torsion subgroup containing `Z/2 + Z/(2ell)`, excluded by Mazur's torsion theorem for ell>=5.

The exclusion uses exactly Mazur (1977), Theorem (8), not a claim that `Y_1(7)(Q)` is empty. The theorem's full paper is indexed at `https://www.numdam.org/item/PMIHES_1977__47__33_0.pdf`; the web PDF fetch hit a 16 MB size limit. A direct local retrieval was attempted; successful access still needs checking. The theorem itself was retrieved as an indexed primary-source excerpt, but this should not silently be upgraded to 'full primary PDF opened'.

## 6. R5: seven-torsion witness

For `y^2-xy-4y=x^3-4x^2`, the generalized Weierstrass discriminant is `-1664`. The exact multiples of `(0,0)` are

`(0,0), (4,8), (2,2), (2,4), (4,0), (0,4), O`.

The exact rational addition-law program verifies every multiplication and the curve equation. Thus the point has exact order seven and the printed emptiness assertion is false. Full rational two-torsion together with seven-torsion remains impossible by the preceding application of Mazur.

## 7. R6 and composite exponents

The birational map on the plus cubic is

`u=-3Z/(X+Y)`, `v=[9(X-Y)/(X+Y)-1]/2`,

to `v^2+v=u^3-7`. The exact polynomial identity is

`(v^2+v-u^3+7)(X+Y)^3=27(X^3+Y^3+Z^3)`.

The smooth projective curves are therefore Q-isomorphic; the coordinate change `x=4u`, `y=8v+4` gives `y^2=x^3-432`. The identification with `X_0(27)` is explicitly stated in the opened published Kriz--Li (2019), Section 10.1, and also their Introduction Section 1.2, PDF p.3: `https://www.cambridge.org/core/services/aop-cambridge-core/content/view/05E581EF286E02A8B4D681096E24E709/S2050509419000094a.pdf/goldfelds_conjecture_and_congruences_between_heegner_points.pdf`.

Stoll Corollary 8.8 gives finite-descent equality. In genus one its proof uses a nonzero analytic-rank-zero factor of the Jacobian, so the entire elliptic curve has rank zero; no approximate L-value is being inferred from a table. Alternatively, equality makes its finitely generated rational group a compact countable group, hence finite, by the Baire argument. Good reductions at 5 and 7 have respectively 6 and 9 points. Prime-to-residue-characteristic torsion injects under good reduction. Applying both reductions prime by prime bounds torsion order by three; the points `O,(3,-5),(3,4)` supply all three. They are exactly the three rational coordinate cusps. R1 now makes every Selmer section cuspidal.

For odd `n>=3`, choose a prime ell|n and use the finite étale power map

`[X:Y:Z] |-> [X^(n/ell):Y^(n/ell):Z^(n/ell)]`

from `U_n` to `U_ell`. It carries local points and cusp sections to corresponding sections, preserving Selmerness. If the downstairs section lies in a cusp decomposition group, the upstairs one lies in the stabilizer of a cusp above it. This follows by the fixed coset action on the finite geometric cusp fibre; surjectivity to `G_Q` forces that cusp to be rational. Thus every Selmer section upstairs is cuspidal. The rational cusps for odd n are precisely `[0:1:-1],[1:0:-1],[1:-1:0]`, since a rational root of unity of odd order is 1.

The passage from Selmer to all sections is a separate issue owned by the parent agent. No use of the October 2026 local preprint, nor of its global Section 8, occurs anywhere in this Selmer proof.

## 8. Historical source-check checkpoint (subsequently closed; see section 9)

The mathematical repairs above settle the cusp error and give a coherent proof of R1--R7's odd Selmer conclusion. Before labeling the complete user task A.1 closed, the source-access requirement still calls for opening the full Mazur theorem and Kisin's theorem rather than only indexed primary excerpts/abstract. The exact local ordinary/supersingular inertia assertion is cited in the supplied Steklov source to Serre (1971), Propositions 11--12; its original paper should also be opened if that theorem is stated as used independently.

For task A.4 the three elliptic quotients have affine equations `v^2=u^4+1`, `v^2=1-u^4`, and `v^2=1-u^4`. Their Jacobians have models `y^2=x^3-4x`, `y^2=x^3+4x`, `y^2=x^3+4x`, respectively. All have geometric endomorphism ring `Z[i]`. The candidate rational groups are `Z/2 x Z/2` for the first and `Z/4` for the last two. A proof using exact eta-product nonvanishing and finite reductions is being prepared; no claim of a finished analytic/Sha certification is made here yet.

## 9. All source checks and the quartic extension completed

The pending requirements in section8 have all been closed. The full proofs are now in deliverable/sections/A_main.tex, A.1–A.16, and the final access notes are in work/a_main_references.bib.

Mazur's original full PDF was downloaded and Theorem(8), printed p.35 / PDF p.4, read as text and visually. Serre(1972), Propositions11–12, printed pp.273–275, were read through targeted primary retrieval from the author's PDF; they include precisely the e=1 ordinary and supersingular inertia assertions used. Kisin's primary author DVI was downloaded and read with dvi2tty: Theorem(0.1), Corollary(0.2), p.2, and the introduction explicitly supply hypothesis(H). Its SHA256 is a11fdea301d662ada1cd675bea21a89ba9ab0a75955e496e4a1bcdecab97bf7d.

Rubin's correct article is Göttingen volume89 LOG_0029.pdf, not the initially guessed LOG_0034. TheoremA p.527, CorollaryC and Remark(3) p.528 were read as OCR and visually from the scanned pages. Martin–Ono(1997), Theorem2, was opened in the primary author PDF and identifies the whole L-functions of the curves of conductors27,32,64 with the Mellin transforms of explicit eta products/quotients. Each is positive on the positive imaginary axis, giving exact positive central values. Rubin then gives finiteSha.

The quartic proof now gives exact2-isogeny descents, the mod16 obstructions, full rational point lists, the CM rings and Jacobian splitting, three separate R1 proofs, and all classical exponents via finite étale power maps. The first standalone LuaLaTeX attempt failed before source processing because lualatex.fmt was absent; the parent subsequently repaired the format environment and owns the PDF build.

The subsequent certified coefficient census, its analytic proof and all computation states are recorded separately in work/a_main_census_audit.md.

## Independent local refinements A.46–A.49

A.46 proves residual conductor control without local geometricity outside T_ell={2,ell} union prime divisors of ell²−1. The finite geometric residual image has order prime to q there, so factors through the full prime-to-q group. The good-reduction cusp theorem and the corrected leading constant then give unramifiedness after a quadratic twist. Assuming local point-or-cusp geometry only at T_ell is sufficient for R3, while the all-place descent input remains separate.

A.47 is a global natural-quotient witness, not a full-section counterexample. SL2(F7) has no nontrivial prime-to3 quotient: diag(2,4) has order3 and its commutators generate all elementary matrices. Goursat makes the joint geometric image P^(3') times SL2(F7). Combine a global cusp section of P^(3') with rho=diag(chi7 theta,theta^-1), theta the cyclic cubic character of Q(zeta9)^+ of conductor9. Its wild3 inertia diag(2,4) cannot be removed by any quadratic twist. Every finite matrix claim was checked by a_main_local_matrix.py. Thus complete prime-to3 data can miss an actual residual conductor condition in the natural joint quotient.

A.48 records Hoshi's precise intrinsic ramification definition and proves that at q|n the Fermat boundary permutation action already makes every section intrinsically ramified. The local good-reduction theorem cannot simply be applied with the same words at those primes. No unjustified separation of local point and cusp pro-lambda classes is asserted.

A.49 supplies an actual full-section density-one counterexample on the proper elliptic X0(27). For T=T5E and S={3,5,infinity}, the finite Euler formula gives rankH1(G_S,T)=rankH2(G_S,T)+1. Finite E(Q)=C3 and finiteSha make compact5-Selmer zero. Any nonzero integral class yields, with all other coefficient components zero, a full elliptic section. At every q!=5 localT5 cohomology is Kummer and realized by a finite5-primary rational torsion point, which simultaneously has zero other coefficient components. At5 the class cannot be Kummer. This proves the all-place requirement is not supplied by density-one local geometry. It does not claim a hyperbolic lift.

New primary sources opened: Hoshi RIMS1742 AppendixA definitions and propositions; Stix February2014 author preprint section5 Lemma16; Milne Arithmetic Duality Theorems second edition I.5.1 p67, I.3.4 p43, I.4.10(c) and I.4.15. Details and complete proofs are in deliverable/sections/A_local.tex; register rows are work/a_main_local_rows.json.

## Quintic maximal-prosolvable theorem A.50–A.52

The new target is C:y²+y=x⁵, J=Jac(C). Its primitive CM type is given by eigenvalues zeta5,zeta5² on the holomorphic differentials. End_Qbar^0(J)=Q(zeta5), End_Q^0(J)=Q, and End_F^0(J)=F for F=Q(sqrt5). This does not make J a modular-curve quotient over Q, but it does provide a Hilbert modular route over F.

Darmon's original published primary paper, Duke102(3)(2000)413–449, was downloaded and opened. Printed p439 after Table3 explicitly identifies this Jacobian, the Hecke characters of conductor(1−zeta5)² and the two Hilbert eigenforms of level(sqrt5)³. This is an actual CM modularity statement, not a finite numerical coefficient match. Induction from K=Q(zeta5) gives conductor5³·5²=3125. The quadratic character chi5 is trivial on G_K, so J has the quadratic selftwist chi5 and Artin formalism gives L(J/F,s)=L(J/Q,s)², including all bad factors. Thus the certified nonzero Q-central value makes each of the two Hilbert central values nonzero.

The arithmetic input is explicitly Known: Zhang2010, Science China Mathematics53(3)573–592, Theorem4.3.2 printed p588. Its finite local non-principal-series condition holds because the conductor exponent3 is odd whereas a principal series of trivial central character has even conductor exponent. The printed attribution is Tian–Zhang, in preparation (reference4p592); this is disclosed in A.50 and the bibliography. No claim to have opened that unpublished work is made. The full author PDF of Nekovar's Euler-system article remained inaccessible, although its primary indexed Theorem3.2 and proof passages were retrieved. We therefore do not upgrade the source-access status to a full opened article. The full published Zhang2004 GL2II primary is now independently opened at the MSRI/SLMath source, Theorem6.1 p203; its actual printed page range is191–241, not the widely propagated transposition191–214. Zhang2001 TheoremA p28 was also opened and its exponent-one restriction is explicitly not used as if it allowed exponentthree.

The exact computation a_main_quintic.py was run successfully. It computes every good Euler polynomial p≤4096 over the finite field, uses the independently justified bad factor1 at5, reconstructs all4096 coefficients in Python, and checks equality with the exact lfunan coefficients. The model has good reduction at2 by its two affine charts, so genus2red's documented bad-even-reduction caveat is irrelevant. The raw conductor result is3125. Exact data and every coefficient are preserved in a_main_quintic_gp.out and a_main_quintic_data.json.gz.

For c=4pi²/sqrt3125, Lambda(s)=c^(−s)Gamma(s)²L(s). The inverse Mellin series Theta(t)=2sum a_n K0(2sqrt(cnt)) satisfies Theta(t)=w t^(−2)Theta(1/t). The certified interval Theta(1)=[0.3300364476±3.40e−11] is positive and proves w=+1. Then L1=4sqrt(c)sum a_n/sqrt(n)K1(2sqrt(cn)). Weil plus |a_n|≤n^(7/2), the elementary Knu bound, and the decreasing integral 2Gamma(10,k sqrtM)/k^10 bound the complete tails. With M4096 and192-bit Arb arithmetic, L1=[0.71831362842056477051660347805±2.72e−30], with analytic tail<2.068e−30. No tabulated rank, approximate-zero test, or guessed sign is used.

The Known arithmetic theorem therefore makes J(F) and Sha(J/F) finite. J(Q) is finite, and the kernel of restriction Sha(J/Q)→Sha(J/F) lies in finite H1(Gal(F/Q),J(F)), so Sha(J/Q) is finite. Stoll's Jacobian criterion makes C finite-abelian-descent excellent. Euler factors give #J(F3)=10,#J(F11)=125, whence J(Q) has order dividing5. The divisor of y gives an actual order5 class D=[(0,0)−infinity]. The genus2 hyperelliptic linear-system argument excludes ±2D from the Abel image, yielding precisely C(Q)={infinity,(0,0),(0,−1)}.

The plus Fermat quotient is x=−XY/Z²,y=+X⁵/Z⁵; the classical formula has the minus sign in y, with Z_classical=−Z_plus. All three rational target fibres are coordinate cusps. Agent B independently checked that its B.1 finite-support proof uses only solvable neighbourhoods and finite abelian refinements; applying it gives every maximal-prosolvable Selmer section of plus U5 cuspidal. No full-profinite lift is claimed. Complete section: deliverable/sections/A_quintic.tex; rows: work/a_main_quintic_rows.json. B was notified to close the U5 part of its earlier B.12 open statement, leaving finite-derived-length questions separate.

Further exact strengthening A.53: the three cyclic coordinate permutations of this quotient give Jac(X5)→J³. On Z=1 and omega=dX/Y⁴, their differential pairs are (1,−XY)omega,(X²,−Y)omega,(Y²,−X)omega, precisely the six plane-quintic monomials. The root first derived these identities; I independently checked them by differentiation and executed a_main_quintic_maps.py, which reduces all three target identities and six differential identities modulo X⁵+Y⁵+1 and obtains coefficient determinant1. Thus the product homomorphism is a Q-isogeny (no degree-one claim). Rankzero and finiteSha hold for the entire quintic Jacobian. B is supplying the corresponding first-derived k=1 argument as B.26, including the completed-Kummer global-local step; that step is kept separate from the isogeny proof.

A.54 proves the required local-five injectivity. Over Q5(zeta5), each of the four conjugate CM characters has exact conductorlambda² and is nontrivial on U1/U2=F5. A generator of this wild quotient has primitive fifth-root eigenvalues. Therefore Phi5(tau)=0, and (tau−1)(tau³+2tau²+3tau+4)=−5 proves that tau−1 is invertible on every stable prime-to-five Tate lattice. This excludes all prime-to-five local torsion for J. The polynomial identity transfers by the rational isogeny to the entire Fermat Jacobian without any isogeny-degree hypothesis (B supplied this useful simplification). Both local point groups are compact with open Z5 lattices, so they are pro-five and their T5 Kummer maps are injective. A separate exact character computation also proves PhiPsi=PsiPhi=[5] for the explicit isogeny and its transpose. The source input is solely the verified CM conductor, not the Hilbert finite-Sha theorem. Code a_main_quintic_inertia.py was executed and every polynomial and trace check passed.

Independent requested audits of root A.17 and D.4 are complete, with detailed notes in work/a_main_root_audit/A17_D4_audit.md. No mathematical defect was found. All root local-Kummer finite cases were independently replayed successfully. One historical notation qualification was sent to root: transcription(357) calls T_infinity(Gm) the twist(−1), whereas the paper uses the modern twist(1); this should be explicitly translated in D.3/D.4.

## A.55: a complete local bad-prime counterexample

The definition caveat in A.48 now has an actual full local example with an independently proved noncuspidality certificate. On U7/Q7 take P=[2:y:1], y⁷=−129. The integer polynomial F(z)=((4+7z)⁷+129)/49 has F mod7=z+1 and derivative1, so there is a root z≡6 mod7 and y=4+7z≡46 mod49. All coordinates are nonzero.

Its tripod image has t=−128 and1−t=129, with residue pair(5,3) at7. Cubes in F7× are{1,6}; using residue generator3 gives Kummer coordinates(2,1) inF3². The three possible cusp families project to lines(a,0),(0,b),(c,c), because−1 is a cube. This pair belongs to none of them. Thus the actual local point section is noncuspidal in the pro3 quotient and even after its geometric abelianization. The argument does not assume general local point/cusp separation at bad reduction; it proves it for this point by an explicit quotient invariant.

Inertia at7 acts nontrivially on the boundary μ7 points, and hence on the pro3 boundary permutation module modulo its diagonal relation. This outer action is independent of the section, so this point section is intrinsically ramified. The good-prime local cusp-recognition criterion is therefore false as a blanket purely local assertion at bad primes. The literal A9 task concerns full global sections and is not refuted; no global lift of this local point section is asserted. The root's A31 global conclusion with the stipulated local theorem remains logically separate. Exact program a_main_bad_prime.py was executed, with the Hensel data, six successive lifts, and every finite Kummer assertion verified. Proof: deliverable/sections/A_bad_prime.tex. Register: work/a_main_badprime_rows.json.


## A.56–A.57: exact exceptional set and global quotient witnesses

The full proof and precise scope are in deliverable/sections/A_quotient_scope.tex. For each q dividing ell(ell²−1), SL2(Fell) has no nontrivial prime-to-q quotient, proved directly using upper/lower unipotents and split/nonsplit Cartan elements. Hence Goursat gives the complete joint fibre product, allowing fixed prime-to-q cusp data with any global determinant-chi residual representation. Odd q witnesses E_q have Tate valuation2; at the coefficient prime this excludes finite flatness for every quadratic twist. At2 the eight square classes of y²=x³−x have conductor5/6 by exact executed Tate algorithm; finite inertia order dividing24 makes reduction mod ell preserve every ramification-invariant dimension. Sources rechecked: Serre1987 §2.4 and Props3–4; CDT1999 §7.1, author PDF SHA256 e9dac063b9db6fd7b34e79907ce09095688b1fd8b1ea48c8527797b6090ae91c. No full global fundamental-group lift claimed.


## A.58: exact sufficient input audit of A.30

The separate level-dividing16 argument is now written, including trivial nebentypus, semisimplification conductor inequality, and the additional Q(i) quadratic twist needed to remove possible conductor-two inertia at2. Condition(D) requires only nonemptiness of finite-abelian-descent loci for a cofinal family of section neighbourhood compactifications; no compatible choice of adelic points is needed. Stoll8.8 proof constructs a nonconstant map to an abelian variety with finite rational group, so W(Q) is finite without a compact-countability shortcut. All supports are taken at finite places to respect the real-place erratum. The argument is fully in deliverable/sections/A_quotient_scope.tex and row A.58 in work/a_main_quotient_rows.json. No assertion of logical minimality or missing-place extension is made.


## A.59–A.60: an infinite lifting theorem and a genuine rank-one Selmer obstruction

Borne–Emsalem–Stix2015 was opened as a full primary PDF and supplied TeX. Theorem5.10, Proposition3.5 and the continuous H2 argument were checked. The exact quotient is pi1(U)/closure[I,Delta], with I the geometric compactification kernel; its kernel over pi1(E) is the full rank-nine cyclotomic permutation module, not the rank-eight toric abelianization. Every proper section over Q lifts when the boundary is a union of torsion sub-packets. Thus all rank-one exponents on E9 lift through this infinite-kernel, all-coefficient quotient. The cusp residue algebra gives the exact fibre as four completed multiplicative groups. This quotient is strictly smaller than the intrinsic class-two or metabelian groups when nine punctures are present, and the theorem does not assert Selmerness. I avoided the unverified old Saidi2010 number-field statement whose published abstract adds a field condition.

A.60 supplies a new positive obstruction: for any number-field elliptic curve E, D=E[N], nontorsion R and nonempty finite coefficient-prime set P, (1-e_P)kappa(R) has no geometric-abelian Selmer lift. After one finite extension splitting E[N], every tangent unit f_d with divisor N(d-O) gives one global mod-lambda Kummer class, lambda coprime to N. Their supports determine a fixed finite S. At v outside S, the removed primary component of R is finite torsion, while the retained component Q_v is forced by full local Tate Kummer injectivity. For R_j=M^j R, any reduction into E[N] splits into its primary factors; the prime-to-v torsion reduction is injective and multiplication by M^j is a formal-group isometry. Thus every boundary distance of R_j is a lambda multiple, using the entire finite set of f_d at Q_v. All f_d(R_j) therefore lie in finitely many S-power classes. Their lambda-root twists have genus lambda and are geometrically connected; Faltings contradicts infinitely many R_j. For cubic N3 and lambda2 the twists have genus2.

The original Faltings1983 published scan was downloaded; its printed p365 was rendered and visually checked, including the exact inequality g>=2 in Satz7. The complete published1984 one-page erratum was opened and read: it corrects Satz2 to eventual height stationarity and explicitly suffices for the remaining proof. Both references are recorded without pretending the erratum was unnecessary.

The proof applies to all n(1-e_P) on E9, n nonzero integer, including root A44's zero-at2/one-at-odd-primes example. It applies uniformly to elliptic twists with their full flex divisors relative to a flex origin. It makes no claim for arbitrary a, infinite P, an effective bad place, or an unconstructed comparison with a specific congruence cover. A finite-kernel toric quotient already retains the obstruction, so A44's abstract finite-kernel lifts and A59's abstract cc lifts exist but cannot all be locally geometric. The full proof is deliverable/sections/A_rankone_progress.tex; rows work/a_main_rankone_rows.json. The exact script a_main_rankone_units.py and output verify the nine flexes, their residue fields, tangent divisors and normalizations, and857 finite primary-component examples.

The root additionally observed the simple uniform residual independence witness rho=[[chi,kappa_ell(q)],[0,1]] for every odd exceptional q!=ell, including q dividingell+1. I checked and added an explicit finite-flat group scheme over Z_ell, a disjoint union X^ell=q^i with the carry-factor product. Since q is a unit this proves finite flatness, while q-inertia is nonzero unipotent of orderell and survives every quadratic twist. Thus A57 now proves each exceptional residual condition can fail with all the others imposed. The original elliptic witnesses remain separately identified.


## A.61–A.63: every finite coefficient alteration is excluded

The erasure case has been strengthened to arbitrary p-adic changes at any finite coefficient-prime set, including exponents supported only at that set. The final criterion is: on any CM elliptic E punctured at E[N], if an abelian Selmer compact exponent a equals one integer n at all but finitely many coefficient primes, then a=n. Every integer occurs, so the intersection of the lifting set with this entire family is exactly Z. This supplies the same compact-exponent exclusion for the intrinsic metabelian quotient. It does not settle infinite coefficient alterations or identify a specific congruence cover.

The Kummer openness proof is supplied directly, not imported from memory. Over a field defining CM, the torsion image is commutative in the quadratic CM algebra. The Q_p span W of the Kummer translation kernel is stable under a nonscalar degree-one Frobenius; that Frobenius generates the CM algebra and its difference from1 is invertible. If W were proper, a CM idempotent projection of the Kummer cocycle would factor through the torsion image and the elementary central-cocycle identity would make it a coboundary. This contradicts Kummer injectivity and the faithful CM module generated by a nontorsion point. Joint openness for finite P follows by intersecting with open pro-p factors and using the Sylow decomposition of a closed subgroup of a finite product of pro-p groups for distinct primes. The proof remains valid after every finite field extension, including the fields used in the next step.

For each coefficient lambda outside the explicit finite set of primes dividing2*product_p p(p²−1) and ramified in the base field, restrict a hypothesized global unit-character difference modulo lambda^r to F=L(mu_lambda^r). Inflation-restriction is injective because the full cyclotomic group contains2, and the elementary central-cocycle identity kills its H1. A nontrivial class would give a cyclic lambda-power extension. The joint P-division tower has no finite quotient with a lambda factor, so the two extensions are disjoint. Re-choose the zero-primary Frobenius neighbourhood over F itself, then Chebotarev gives a prime simultaneously satisfying that condition and nontrivial in the lambda extension. Local Selmerness forces the compact point to nR and the unit character to its value there, contradiction. This exact base-change order avoids an unproved entanglement compatibility.

At almost every residue prime q, the q-adic component has therefore vanished, so the actual algebraic ratio f(Q_v)/f(nR) is a root of unity. The compact difference Q_v−nR is finite P-primary torsion. Hence the point on the graph in E×Gm is torsion. For n0 use a ratio f_d/f_e regular and nonzero at O; it evaluates to its ordinary value even on a tangent cusp section, so the same proof works. Hindry's Manin–Mumford theorem for E×Gm makes the graph torsion intersection finite; a positive-dimensional torsion coset is impossible since the E-coordinate is nonconstant and the unit coordinate is nonconstant. Stoll8.2 applies to the proper adelic point aR already in the closure of E(L), then local elliptic logarithms force all altered components back to n. No finite-Sha assertion over the splitting field enters.

The full text is deliverable/sections/A_finiteprime.tex and the three rows are work/a_main_finiteprime_rows.json. Parent and B were asked to audit the full chain. B independently checked the CM openness proof. Hindry's complete original published scan was obtained from his author site and opened. Theorem1 printed p587 was visually checked, its proof p588 and curve argument p589 OCR read, and the earlier Bordeaux seminar Theorem1 on18-03 independently checked. The original published page range is575–603; the cover's575–604 metadata is not used.


## A.64–A.65: exact fibres and an infinite-change exponent theorem

A.64 is in deliverable/sections/A_abelian_fibres.tex and was independently approved by root. It proves exact abelian Selmer fibres over rational compact points, including a complete dyadic completed-Kummer local-global argument. A.65, in deliverable/sections/A_unit_exponents.tex, now proves for arbitrary E/Q with full E[N] boundary that an exponent which is a unit at all but finitely many coefficient primes admits an abelian Selmer lift if and only if it is a nonzero integer. Its fibre is the unique point section by A.64. The same exponent-set statement holds metabelianly by projection and actual point-section existence; no metabelian-fibre theorem is claimed.

For a profinite unit u and rational nonT R, every local centre uR is interior, including at bad primes. A nonconstant Q-rational boundary unit has unit values outside one finite S. Its global completed multiplicative class has an actual integer valuation at each S prime, so the decomposition Q×=sign times direct sum of prime valuation groups makes it the Kummer class of one rational number. Local Kummer injectivity gives finite support. Every cofinal proper section-neighbourhood is genus one, has locally geometric points over this support, and survives finite descent; Stoll supplies finite nonempty rational fibres, whose inverse limit identifies the actual global point section. Kummer injection plus Bezout on free Mordell-Weil coordinates then makes u an ordinary integer, hence +/-1. This does not assume that R is primitive.

The erasure proof A.60 also extends to u(1-e_P)R for arbitrary profinite unit u and finite nonempty P. The removed P-primary local component remains finite torsion, u permutes the split full N-torsion set and preserves formal-group distances, and the whole finite family of boundary unit characters still forces fixed-S divisibility for the rational sequence M^jR. Faltings gives the contradiction. B independently audited this extension and agreed. Factoring every almost-everywhere-unit exponent as m*u*(1-e_P) proves the theorem. No CM or finite-Sha hypothesis appears.

The exact prior genus-two-cover exploration is retained as a supplementary diagnostic in A.65 and a_main_unit_covers.py/.out. The eight Eisenstein S-squareclasses yield V²=U⁶+4sqrt(-3)c³ with explicit two elliptic maps. For c=+/-1 the Pryms have certified nontorsion K-points (reductions of orders4 and19 kill torsion), so a rank-zero shortcut cannot settle all covers. The rational norm cover has two cases b=1,3; b=3 maps to certified rankzero E972 with torsionzero and inverse O-fibre V²=-3, giving empty finite-abelian descent. The b=1 cover has two rankone elliptic factors. These are no longer unresolved unit-exponent obstructions, since the direct rational-unit theorem settles that entire family. No extra rank claim for c=+/-2 was needed.


## A.66: infinite nonunit support with divisible valuation profiles

The new theorem is written in deliverable/sections/A_infinite_valuations.tex; row work/a_main_infinite_valuation_rows.json. Root and B independently approved it. If a has finitely many zero components and some prime lambda divides v_p(a_p) for all but finitely many p, abelian Selmer lifting forces a to be a nonzero integer, for arbitrary E/Q with full N-torsion boundary. Infinite positive valuations supply infinitely many ordinary lambda-th powers n_j dividing a. After splitting E[N], the Miller unit with divisor(P)+(Q)-(P+Q)-(O) and its translates have a simple pole at every cusp. Their global mod-lambda characters force cusp distances divisiblelambda. At good unramified q>=5 outside a fixed finite S, Q_v=aR=b_j(n_jR); the formal distance shift is v_q(a_q)-v_q(n_j), a nonnegative multiplelambda. Therefore the rational sequence n_jR lifts into finitely many genus(2lambda-1) covers; Faltings contradicts infinitude. Finite-positive-valuation cases fall under A65. Simple coefficients remove every lambda-versus-N restriction. This excludes a_p=p^r for allp and anyfixedr>=2, a family of infinite nonunit support. It does not exclude the all-valuation-one profile or infinite zero sets.

A convention error discovered in a separate WORK note was corrected before any manuscript insertion: projective mod3 Legendre monodromy over the lambda-tripod has compactification X6 of genus1, not task A12's genus-zero X3 over the j-tripod. Its compact factorization and multiplication-by-two cover calculation remain correct, but do not answer A12(b). The superseded note and exact correction are explicitly marked in work/a_main_x3_factor.md, because the initial note may have been included in checkpoint04. No deliverable statement carried the incorrect X3 label.


## A.67: actual j-line congruence obstructions

A.67 is written in deliverable/sections/A_congruence_obstruction.tex; row work/a_main_congruence_rows.json. It now identifies the actual joint quotient Gamma_m retaining pi1(E) and the finite projective modular cover over J=j/1728, with branch orders(3,2,m). Matrix calculations give Fermat images V4,S4,A5,PSL2F7 and compact fibre-product genera4,46,118,343. Exact Hesse maps identify X3 and its genus4 pullback. This explicitly repairs the earlier work-note confusion with Legendre X6.

The X3 quadratic characters ramify at pairs among the three J1 cusps. Their flex-unit mod2 characters factor through the joint quotient by a direct geometric-kernel argument; no unsupported arithmetic character-extension claim remains. For finite erasures with3 notinP, the M^(2j) rational orbit approaches the same cusp as its retained local component, so these actual X3 characters give fixed-S parity and a genus2 Faltings contradiction. At X4 the sign character kappa2(1-J) has an odd pole at the rational infinity origin. It detects all finite erasures, including3 inP, via genus4 double-cover twists. This character is already the level2 S3 sign quotient, so fullS4 and a nested-level ordering are not claimed essential. The uniform twist statement explicitly requires the rational infinity flex origin, or the same compact-class description after a finite base change.

The initially specific q61 witness for erased3 was strengthened to every n!=0 on E9. With b³3,zeta³1, d1=(b*zeta,1), g=(b²zeta²x-y-2)/(b²x-y-2), the exact identity g(A+d1)=(zeta+2)/(zeta-y(A)) follows from divisors and an evaluated constant and was checked symbolically. Over L=Q(E[3]) the3-Kummer towers are pro3; A61 and quadratic disjointness force the globalg-class to be g(A). Since the erased compact class is unchanged under A->A+d1, it must also be g(A+d1). At the unique local3 place e6, v(zeta+2)=3, rationalA has v(zeta-y(A)) even, and v(g(A))=0 by local conjugacy. The ratio has odd valuation, contradiction. Thus every singleton erasure n(1-e_p) on the least curve fails at the actual finite joint X3 level. Parent and B independently checked the forcing; root checked and approved the uniform local3 proof. q61 (ratio6 nonsquare) remains as an exact independent finite witness.

All requested certificates are copied into deliverable/code: a_main_jline_covers.py/.out, a_main_jline_at3.py/.out, a_main_jline_local3.gp/.out. The symbolic Hesse map, nine flexes, translated-function identity, finite group images and inertia, all four genera, and exact finite-field/local computations were actually run. No finite sample substitutes for the uniform argument.


## A.68: every finite alteration of a nonzero integer dies at actual X3

A.68 is in deliverable/sections/A_finite_congruence.tex; row work/a_main_finite_congruence_rows.json. Parent and B audited the complete proof in work/a_main_coefficient3.md. The prescribed-primary lemma uses the actual open joint Kummer image to realize any finite primary torsion targets, including simultaneous zero targets at other changed primes. For a chosen changedp!=3, after killing the global quadratic unit class in one fixed field, every radical sqrt(g(nR+T)) at a p-primary translate must belong to the joint proper division tower: otherwise it is disjoint and Chebotarev contradicts local Selmerness. The entire proper tower is unramified outside one fixed finite S by good abelian reduction and finite-etale multiplication, so all these values have even outside-S valuations. Parity descends through unramified extensions even at p2. Norm_[p²]g=Cg and its exact iterates then give infinitely many rational multiples with values in finitely many S-squareclasses; genus2 Faltings is a contradiction. This handles all finite simultaneous changes with a changed prime differentfrom3 and a nonzero baseline integer.

Pure coefficient3 alterations on E9 are settled for every integer baseline. For nonzero baseline n, choose a torsion preimage T under alpha-n of d1 and apply prescribed-primary Chebotarev to the nonsquare translated ratio from A67. For baseline0, the q73 residue point(1,0) has exact order9 and g-value56 nonsquare. Its prime-to73 torsion lift S gives a nonsquare algebraic value in the odd3-torsion field; choose alphaT=S and apply the same argument. Zero-primary primes force the global unit class to g(O)=1 because g is regular atO and kills cusp inertia. Thus all finite alterations of a NONZERO integer on the least curve have exact Gamma3 lifting set Z, and pure3 alterations include baseline0. General finite support about0 at other primes remains outside the theorem. No new computation beyond the executed q73 data was needed.


## A.69: all finite support, completing every finite alteration of every integer

The previously open finite-support baseline-zero case is now completely settled at the actual joint X3 quotient. A.69 is in deliverable/sections/A_finite_support.tex; row work/a_main_finite_support_rows.json; full work proof work/a_main_finite_support.md. Parent and B independently read and approved the complete proof, including all field changes. The exact certificate a_main_finite_support.py/.out was executed successfully. A45 and A68 scope paragraphs now acknowledge the stronger result.

The common tower argument uses a finite abelian base F0/K, K=Q(zeta3), and the joint proper P-torsion/R-division tower. A quadratic character kills all odd primary translation kernels. If2 occurs, a residual C3 element has A−1 invertible integrally and hence kills the2-primary translation kernel as well. Therefore every quadratic extension of F0 inside the tower lies in the CM torsion field, which is abelian overK. Zero-primary Chebotarev puts the global unit character's radical into the tower. A torsion value h whose radical is not Galois overK then cannot belong to that tower, and prescribed-primary Chebotarev gives the contradiction. Crucially its noncontainment is established before adjoining targets or killing the residualC3; it persists after every finite intermediate base extension.

For coefficient2, take F0=K(c), c³2, S=(b/c²,-1/2), b³3. Then F0(E2)=F0L supplies the field bridge, and g(S)=(zeta²c−1)/(c−1) is nonsquare at31 (c4,zeta25,value27). Its three cubic conjugates have product1, so its squareclass is not Galois invariant and its radical is not Galois overK. This excludes all finite support containing2, regardless of the other components.

For every p>=5 the local ordinary/supersingular inertia results in opened Serre1972 Props11–12 give the full CM Cartan overK. At splitp both primes abovep are used to generate its two factors. These same inertias show K(Ep)∩L=K. At2, good reduction has Frobenius4=[−2]. If g(S) is square in the unramified dyadic torsion field, then g([-2]S)−g(S)^4 is0 mod4. The exact half-numerator modulo2 is a nonzero function with unique leading-pole monomial zeta*x^10*y, hence pole order23; its denominator reduces to(x+y)^8, whose only affine zero is an order3 cusp. A maximal Cartan orbit has at least24 distinct odd-torsion reductions, contradiction. Thus g(S) is nonsquare uniformly in everyp>=5. The cubicb-conjugates telescope product1 and make its radical non-Galois overK; the tower argument applies. Support{3} was already A68. This completes the actual Gamma3 Selmer exponent classification for all finite alterations of every integer, includingzero. Infinite alterations and finite-quotient fibres remain unclassified.


## A.70–A.71: the complete finite-alteration theorem uniformly across cubic twists

A.70, in deliverable/sections/A_uniform_three.tex, closes the coefficient3 gap in the uniform twist statement. Its full work proof is work/a_main_uniform_cubic_three.md; row work/a_main_uniform_three_rows.json. Root, B, and C independently audited the parity/norm mechanism, and root and C checked the complete arithmetic/local field bridge. Any pure3 alteration forces all torsion-translated normalized flex-unit ratios to be squares in the pro3 torsion tower. At2 every cubic twist becomes E9 over Q2 or a tame cubic overQ2(zeta). Subtract the unique3-torsion lift of the reduction to make the centre formal. The exact parameter z=−x/y is CM-equivariant. Odd formal height gives an odd valuation at the threefold pole. At even height, unramified translation is trivial modulo4; in the ramified case the cubic norm is an integral series in z³ with constantg(T)³, while the denominator norm is exactly1. The same A69 polynomial would vanish on all72 reductions ofE[9]−E[3], impossible. This proves pure3 alterations for every integer baseline uniformly, includingtwistsramifiedat2.

A.71, in deliverable/sections/A_uniform_finite_support.tex, then completes arbitrary finite support around zero on every rational-origin cubic twist. Root proposed the global transport extension, and A/C independently audited it. The short-model flex ratio gd has a universal two-torsion value (zeta²*c−1)/(c−1), c³=2, independent of d. Over K(c) the residual C3 survives except at cube classes 1, 2, 4, all of rank zero by the existing rigorous A.38 census and hence incompatible with nontorsion R. For odd support containing p>=5, take the fixed A.69 E9 witness field M0 and extend by K(cube root of d), an odd abelian extension of degree at most three. The witness remains nonsquare, and any lift of the b-cycle has the same three conjugates of h with product one, even if that lift has order nine. Its radical therefore remains non-Galois over K. Cubic transport identifies the actual retained character and p-torsion target exactly. The A.69 joint-tower argument applies. Support {3} is A.70. Thus all finite alterations of every integer are now classified uniformly for all rational-origin cubic twists with nontorsion R.

The exact executed certificate a_main_twist_transport.py/.out checks all tangent-line identities, the universal two-torsion evaluation, the cubic scaling, and the minimal-model normalization; it selects the already certified d=1, 2, 4 rows without replacing their rigorous L-value enclosures by heuristics. The A.71 row is work/a_main_uniform_finite_support_rows.json. Both new sections were delivered before 06:30 for checkpoint06 integration.

A.72's full work-only proof is work/a_main_gamma3_fibres.md. Root approved its mechanism, and C independently checked the complete argument: the actual Gamma3 kernel over pi1(E) is V4, the infinity-origin inertia is killed, and the finite V4 module has injective global-to-local H1. Its arithmetic image H≤S3 has H1(H,F2²)=0 in every case. Thus the surviving integer fibres are each a single Gamma3 Selmer section class. Manuscript promotion awaits checkpoint06 freeze release. Work/a_main_remaining_infinite_scope.md records the precise remaining infinite-change gap and the hypotheses of the opened primary AML and split-torus sources that do not fill it.
