# Post-freeze check: integral Schwarzian and the small-characteristic homography assertion

Run: MPL_93_092-134/integral_schwarzian_check. Model: GPT-6 Astra Pro (inherited); effort setting not exposed. Work is on the frozen text only; no scan images were read by this agent and no transcription file was edited. The root reader remains responsible for readings. The checks below are mathematical checks of explicitly stated interpretations, not a retrospective change to the transcription.

## Results and attribution

The manuscript's normalized local rigidity argument works over arbitrary commutative characteristic-p rings, including rings with nilpotents, with q=p for p>3 and q=p² for p=2,3. The reduction from a general equation t^q=α to t^q=0 can be completed under Pic(A)=0 by faithfully flat descent of a rank-one module of matrix solutions. For odd q the same proof actually removes the Picard hypothesis, as explained below. The determinant must be a unit, not necessarily 1; this correction and the example s=2t over F5 were already made by **Michel Hua, modernised reading of cote 93**, subsection **“L’injectivité en caractéristique p”**, lines 1513–1556, and are rechecked here rather than claimed as a new discovery.

Hua's attached text reports Lean declarations for the α=0 case, universal identities, and the counterexample. Those Lean files and their execution environment are not supplied in this context and have not been run or certified here. This report gives its own elementary proof and a separate exact symbolic/finite computation; it does not use an uninspected formal certificate as a proof.

The RESULTS_STATE entry **Hua, findings register, 93-integral-schwarzian-level-p2** is the principal cross-reference. The register says that no settled result from the user's own runs directly meets this folder; the earlier **MPL_93_002-046 P01, P05, P06, P09** are relevant leads, not theorems imported here. In particular, no inference about zero or nilpotent p-curvature is made merely from the Schwarzian formulas.

## Precise statement checked

Let p be a prime and let A be a commutative F_p-algebra. Put q=p if p>3, q=4 if p=2, and q=9 if p=3. Let B=A[t]=A[T]/(T^q−α), with α∈A. The Hasse operators D_i for 0≤i≤3 are induced by D_i(T^n)=binom(n,i)T^(n−i); they are well-defined on B because q is a p-power greater than 3. For s∈B assume D_1s is a unit and

\[
N(s):=(D_2s)^2-(D_1s)(D_3s)=0.
\]

If Pic(A)=0, there exist a,b,c,d∈A such that Δ=ad−bc is a unit, ct+d is a unit in B, and s=(at+b)/(ct+d). Any two such quadruples differ by multiplication by one common unit of A. The Picard hypothesis is unnecessary when α=0 or q is odd (thus for every p>2 here). For p=2 and arbitrary α, Pic(A)=0 remains a sufficient hypothesis in the theorem proved here; its necessity is not asserted. Conversely any such fractional linear expression has N(s)=0.

This is the corrected mathematical statement assessed here. The frozen scan-122 derivative orders and determinant 1 remain exactly as transcribed, with their recorded doubts.

## 1. The integral identity and composition law

Write s_1=D_1s, s_2=D_2s, s_3=D_3s. In characteristic zero the ordinary expression is

\[
-2\frac{s'''}{s'}+3\left(\frac{s''}{s'}\right)^2
=12\left(-\frac{s_3}{s_1}+\frac{s_2^2}{s_1^2}\right).
\]

The right-hand expression defines G_0 without dividing by 2 or 3: one inverts only the étale derivative s_1. Thus the notation G/12 is mnemonic in characteristics 2 and 3, not a literal quotient operation on arbitrary sections. With the factor dt² included, G_0(t,s)=N(s)/s_1²·dt².

For a composite r=F(s(t)), put a=D_t^1s, b=D_t^2s, c=D_t^3s, A=D_s^1r, B=D_s^2r, C=D_s^3r. Taylor composition to order three gives

\[
r_1=Aa,\qquad r_2=Ab+Ba^2,\qquad r_3=Ac+2Bab+Ca^3.
\]

Direct polynomial expansion over Z yields

\[
r_2^2-r_1r_3=A^2(b^2-ac)+a^4(B^2-AC).
\]

After inverting a and A this is the cocycle law, because ds²=a²dt². No cancellation by 2, 3, or 12 occurs. For a fractional linear function F(z)=(Az+B)/(Cz+D) with invertible determinant and denominator, its first three Hasse coefficients are Δ/(Cz+D)², −ΔC/(Cz+D)³, ΔC²/(Cz+D)^4; their numerator N(F) is zero. The same calculation applies to coefficients annihilated by D_1,D_2,D_3, not just constant coefficients.

The accompanying `integral_certificate.py` expands the displayed composition identity symbolically and gets the zero polynomial. This finite symbolic identity proves the universal coefficient calculation; extension from coordinate Taylor expansions to the appropriate sheaves requires the usual coordinate/étale descent and is not a claim that a global algebraic solution exists for every connection.

## 2. Which constants are invisible to the first three Hasse derivatives?

In the polynomial ring A[T], monomials are independent over A, so the common kernel of D_1,D_2,D_3 is A[T^q] with q as above. For p>3, D_1 eliminates all exponents not divisible by p, and a p-divisible exponent has its first three binomial coefficients zero modulo p. For p=2, D_1 and D_2 detect the low two binary digits, leaving precisely exponents divisible by 4. For p=3, D_1 detects the units digit and D_3 the next ternary digit, leaving precisely exponents divisible by 9. In the quotient B=A[T]/(T^q−α), the common kernel is consequently the embedded coefficient algebra A.

This argument remains valid when A has nilpotents: every nonzero coefficient from F_p is a unit in A, so its product with a coefficient of the polynomial can vanish only when that coefficient vanishes. For a relative curve, the corresponding notation must mean the relative Frobenius-constant subalgebra (base coefficients retained), not necessarily the set of absolute p-th powers of its ring; for example an imperfect base element need not itself be a p-th power.

The need to change the invariant group at small primes is tangible: in characteristic 2, s=t+t² has D_1s=1 and G_0(t,s)=dt², and in characteristic 3, s=t+t³ has D_1s=1 and G_0(t,s)=−dt². Both additions are invisible to the ordinary first derivative, so first-level Frobenius constants do not give invariance of G_0. These are already Hua's examples at lines 1505–1508; they have been checked again here. The ordinary G=12G_0 vanishes identically in those characteristics, which is a different statement from the refined invariant vanishing.

## 3. Local rigidity for α=0, with nilpotents allowed

Let B=A[t]/t^q and s=a_0+a_1t+…+a_(q−1)t^(q−1). Because t is nilpotent, D_1s is a unit if and only if a_1 is a unit in A. First replace s by v=(s−a_0)/a_1; then v=t+βt²+…, where β=a_2/a_1. Next replace v by w=v/(1+βv); the denominator is a unit since v is nilpotent, and w=t mod t³. Both replacements are homographies with coefficients in A, so the calculation in §1 preserves N=0.

Induct on d=3,…,q−1. If all coefficients of w−t below degree d have already vanished, write w=t+h t^d+O(t^(d+1)). Modulo t^(d−2),

\[
D_1w\equiv1,\quad D_2w\equiv0,\quad
D_3w\equiv h\binom d3 t^{d-3}.
\]

Consequently N(w)=0 implies h·binom(d,3)=0 in A: coefficient comparison is valid because 1,t,…,t^(q−1) is a free A-basis. This is a **linear equation in h**, not h²=0. The binomial coefficient is a unit in every case needed:

- If p>3 and 3≤d<p, it is d(d−1)(d−2)/6, a nonzero element of F_p.
- If p=2 and q=4, the only d is 3 and the coefficient is 1.
- If p=3 and q=9, the coefficients for d=3,4,5,6,7,8 are 1,1,1,2,2,2 modulo 3.

Thus h=0 even in a nonreduced ring. Induction proves w=t, hence

\[
s=a_0+\frac{a_1t}{1-\beta t}
=\frac{(a_1-a_0\beta)t+a_0}{-\beta t+1}.
\]

The matrix has determinant a_1 and the denominator is a unit. This proves the α=0 statement without Pic(A)=0. It directly validates the surviving coefficient argument on scans 123–124; the crossed-out characteristic-three branch is not needed and is not used as a valid proof.

## 4. Completing the reduction from general α

Take A'=A[u]/(u^q−α), a free and faithfully flat A-algebra of rank q. In B'=B⊗_A A', set z=t−u. Since q is a p-power in characteristic p, z^q=0, and B'=A'[z]/z^q. The Hasse operators relative to A' are unchanged by this translation. Section 3 supplies an invertible matrix M over A' satisfying the required fractional linear relation, after translating its variable z back to t.

Define the A-linear map

\[
\Phi:A^4\longrightarrow B,\qquad
(a,b,c,d)\longmapsto s(ct+d)-at-b,
\]

and K=ker Φ. Flatness gives K⊗_A A'=ker Φ'. **Every** vector in ker Φ' is a scalar multiple of M, including vectors not themselves invertible. Explicitly, if M represents s=(at+b)/(ct+d), then [-1,s]M=(det M)/(ct+d)·[-1,t]. Writing an arbitrary kernel matrix as M L therefore reduces its equation to [-1,t]L[t,1]^tr=0, a polynomial of degree at most two. Since q≥4 and 1,t,t² are independent over A', comparison gives the off-diagonal entries of L zero and its diagonal entries equal. Thus K⊗_A A'≅A', with M a generator. The same calculation may be made after the invertible translation t=z+u.

Finite projectivity descends along a faithfully flat ring map; this standard step was checked in the [Stacks Project, Proposition 10.83.3, tag 058S](https://stacks.math.columbia.edu/tag/058S). Its rank is one after every residue-field extension, hence K is an invertible A-module. If Pic(A)=0, choose a generator M_0 of K. After extension to A' it is a unit scalar times M, so both det M_0 and its denominator ct+d become units. Units descend along faithfully flat maps, proving they were units already over A and B, respectively. This finishes the general-α theorem under the hypothesis actually written on scan 122.

For uniqueness, over A' any two matrix solutions differ by a scalar; globally they are two generators of the same invertible module K and therefore differ by one element of A*. “Transformation diagonale” can correctly mean a common scalar diagonal matrix; arbitrary independent diagonal transformations would not preserve the given fraction.

**Refinement for odd q.** The determinant restricts to an isomorphism K^⊗2→A: after the faithfully flat extension it sends M⊗M to the unit det M. The denominator map K⊗_A B→B, (a,b,c,d)↦ct+d, is also an isomorphism, because it is so after the same extension. As B is free of rank q over A, taking the top exterior power of this latter isomorphism as A-modules gives K^⊗q≅A. When q is odd, the trivializations of K^⊗2 and K^⊗q imply K≅A, so no Pic(A)=0 assumption is needed. For q=4 the argument only shows that the possible line-module obstruction has order dividing two and becomes trivial over B; no counterexample establishing necessity is claimed. This refinement is a proof checked in this run, not an assertion of novelty and not an inference from Hua's unavailable Lean artifacts.

This proof supplies an argument omitted in the manuscript and explicitly left unverified in Hua's attached footnote (lines 1540–1556). It is a proof completed in this run, without a claim of historical or mathematical novelty. The finite code checks all four α and every s over A=F2[ε]/ε² for q=4; those computations support this example only and are not substituted for the descent proof.

## 5. The determinant-one claim fails

This is Hua's correction, rechecked here. Put A=F5, B=A[t]/t⁵, s=2t. Then D_1s=2 is a unit and D_2s=D_3s=0. If 2t(ct+d)=at+b, comparison of 1,t,t² gives b=c=0 and a=2d. An invertible matrix then has d≠0 and determinant 2d², which is 2 or 3, never 1. The certificate exhaustively enumerates the 5⁴ matrices and confirms four invertible solutions and no determinant-one solution.

The correction ad−bc∈A* is therefore essential even when A is a field and Pic(A)=0. It is not an ambiguity resolved by invoking locality. None of these calculations changes the frozen `ad-bc=1`.

## 6. Primary literature comparison and limits

[Hoshi, *A note on Schwarzian derivatives and Sugiyama–Yasuda locally exact differentials*, Osaka J. Math. 61 (2024), 313–333](https://ir.library.osaka-u.ac.jp/repo/ouka/all/97634/ojm61_03_313.pdf), Definition 6.2 and Remark 6.4.2, uses a level-one invariant which is zero in characteristics 2 and 3. Section 3 instead treats level-two projective structures in characteristic 2 using locally exact differentials. This supports Hua's distinction between that literature and the quadratic-differential-valued G_0 of scan 121; it does not prove that Grothendieck's construction is new or exhaust the literature. No novelty or priority claim is made. The paper's full global results, and the Lean files named by Hua, are not independently re-proved here.

## 7. Context search / note mapping

Each query was checked against the supplied context text; cited line ranges identify context locations, not replacement readings.

| Proposed note | Search terms / objects | Context location | Relation of these scans / this check |
|---|---|---|---|
| D01 | facteur 12; G_0; dérivées divisées | Hua IX, “Le facteur 12”, lines 1452–1476; RESULTS_STATE finding 93-integral-schwarzian-level-p2 | Restates the formula; checks integral interpretation and distinguishes it from literal division. |
| D02 | cocycle; N_comp; G0_comp | Hua IX, lines 1459–1471 | Rechecks the claimed identity with an explicit Z-polynomial proof; does not inspect the claimed Lean certificate. |
| D03 | 12 nul; canonique; Conn_0 | Hua IX, lines 1471–1476; earlier notes P05/P06 | Restates ordinary-torsor degeneration; refined torsor must be kept separate and no p-curvature conclusion follows here. |
| D04 | O'_X; D^(1); D^(2); D^(3); p² | Hua IX, “L’injectivité…”, lines 1493–1504 | Rechecks the polynomial kernel and clarifies relative constants over a nonperfect base. |
| D05 | char_two; char_three; t+t²; t+t³ | Hua IX, lines 1505–1510 | Rechecks Hua's two distinguishing examples, matching the manuscript's change of Frobenius level. |
| D06 | c_0(s); D^(2); D^(3) | Hua IX, lines 1513–1517; frozen scans 121–123 | Differs from the doubtful orders on scan 122; reading question only, with no transcription repair. |
| D07 | rigidity_of_gt; rigidity_four; rigidity_nine; nilpotent | Hua IX, lines 1527–1556; earlier E12 warns against discarding nilpotents | Independently checks the linear leading-coefficient argument over nonreduced A; same local conclusion as Hua's claimed formal check. |
| D08 | Cas p=3; Lucas; on gagne encore | Hua IX, lines 1533–1540 | Supports the surviving argument and documents withdrawal of the crossed-out branch. |
| D09 | ad-bc=1; det_one_counterexample; 2t | Hua IX, lines 1517–1525 | Rechecks Hua's refutation and credits it. |
| D10 | alpha=0; Pic(A); réduction | Hua IX, lines 1540–1556; manuscript scan 123 opening | Adds the faithful-flat kernel-module descent proof to the explicit gap. |
| D11 | transformation diagonale; Pic(A); PGL_2 | Hua IX, lines 1517–1525, 1540–1556 | Clarifies common-scalar uniqueness and the sufficient role of Pic(A)=0. |
| D12 | Hoshi; Sugiyama; locally exact; level | Hua IX, lines 1476–1488; RESULTS_STATE finding | Primary-source check confirms a distinction of invariants, without any novelty conclusion. |
| D14 | Pic(A); alpha=0; determinant; rank q | Hua IX, lines 1540–1556, general-alpha reduction; this report §4 | Adds the this-run determinant/exterior-power implication removing Pic(A)=0 for odd q, without a novelty claim. |

## 8. Suggested compact notes (root may map or edit)

### D01 — The integral invariant is defined before division

**Cote 93, scan 121, middle and lower displays; kind: unproved claim.** The assertion “G(t,s)=12G_0(t,s)” admits the integral interpretation G_0=((D_2s)²−D_1s D_3s)/(D_1s)²·dt², so its definition uses only invertibility of the first derivative, even when 12 is zero. This rechecks **Hua, modernised reading of cote 93**, IX “Le facteur 12”, and bears on **Hua, findings register, 93-integral-schwarzian-level-p2**; the notation “1/12” at the next page is not literal division in those rings.

### D02 — A denominator-free proof of the cocycle

**Cote 93, scans 120–122, cocycle and refined-torsor passages; kind: own idea; confidence: high, explicit polynomial identity.** For Taylor coefficients (a,b,c) of s and (A,B,C) of r relative to s, the identity N(r)=A²(b²−ac)+a⁴(B²−AC) proves the cocycle for G_0 after only the étale first derivatives are inverted. This gives a direct check of the assertion “s’étendent à G_0”, agreeing with Hua IX's reported `N_comp`/`G0_comp` results, whose Lean artifacts were not supplied or rerun.

### D03 — The ordinary and refined torsors separate at small primes

**Cote 93, scan 121, “toutes les connexions… sont égales”; kind: unpursued implication.** In characteristics 2 and 3, the equality G=12G_0 collapses the coordinate sections of the ordinary torsor while G_0 can remain nonzero. This restates Hua IX “Le facteur 12” and bears on **MPL_93_002-046 P05/P06**: it gives no p-curvature vanishing assertion by itself.

### D04 — The kernel is a relative Frobenius-constant algebra

**Cote 93, scan 122, upper margin on O'_X; kind: unproved claim.** The assertion “sinon c’est… (p²)” is confirmed in A[t]: the common kernel of D_1,D_2,D_3 is A[t^p] for p>3, A[t⁴] for p=2, and A[t⁹] for p=3, including nonreduced A. It agrees with Hua IX “L’injectivité…” and the finding **93-integral-schwarzian-level-p2**; over a general base these are relative constants, not necessarily absolute powers of all coefficients.

### D05 — First Frobenius level is too small for G_0

**Cote 93, scans 121–122, Frobenius action and qualification “p>3”; kind: own idea; confidence: high, exact calculation rechecking Hua.** Hua IX's tests s=t+t² in characteristic 2 and s=t+t³ in characteristic 3 give G_0=dt² and −dt² respectively, although the added term is killed by D_1. They explain why the manuscript's first-level invariance statement must be replaced by the refined constant algebra for G_0; they do not contradict the collapse of ordinary G.

### D06 — Conflicting divided-derivative orders

**Cote 93, scan 122, definition of c_0 and following equality; kind: reading question.** The frozen reading records uncertain 2/3 orders and an equality beginning “(D^(3)s)²”, whereas the calculation on scan 123 and Hua IX “L’injectivité…” use (D_2s)²=D_1s D_3s. The latter is the condition checked in this report, and the discrepancy remains a reading question without altering the frozen page.

### D07 — The leading-coefficient argument does not require reduction

**Cote 93, scans 123–124, “donc a=0 OK”; kind: own idea; confidence: high, coefficient proof.** After normalizing s=t mod t³, the least remaining coefficient h satisfies the linear equation h·binom(d,3)=0, and the binomial coefficient is a unit in every range considered, so nilpotent h causes no exception. This independently checks the local conclusion in Hua IX's reported `rigidity_*` results and avoids the invalid inference from h²=0 to h=0 noted as a general danger in earlier **MPL_93_002-046 E12**.

### D08 — The characteristic-three branch is replaced on the same sheet

**Cote 93, scan 124, cancelled block and surviving right-hand argument; kind: withdrawn in the same text.** The long crossed-out p=3 case distinction is replaced by the digit argument ending “On gagne encore !”, which gives binom(d,3)=1 or 2 modulo 3 for 3≤d≤8. This agrees with Hua IX's description of the withdrawal and validates the surviving step, not the cancelled one.

### D09 — Picard triviality does not allow determinant one

**Cote 93, scan 122, “avec ad-bc=1”; kind: unproved claim, refuted in the stated form.** Hua IX already supplies s=2t over F5[t]/t⁵ as a counterexample, and a fresh coefficient check gives b=c=0, a=2d, hence det=2d²≠1. This rechecks Hua's correction; the valid refinement is determinant a unit, as in D10.

### D10 — A descent proof fills the general-α gap

**Cote 93, scan 123 opening, reduction to “α=0”; kind: own idea; confidence: high, faithfully flat descent plus explicit local proof.** Passing to A[u]/(u^q−α) reduces to the nilpotent coordinate t−u, and the module of all quadruples satisfying s(ct+d)=at+b becomes free of rank one. It descends to an invertible A-module, which Pic(A)=0 trivializes; its generator has unit determinant and denominator by faithful flatness. This supplies the missing reduction that **Hua, modernised reading of cote 93**, IX lines 1540–1556 explicitly leaves unchecked, using the independently verified local argument D07 and Stacks tag 058S.

### D11 — Uniqueness means a common scalar

**Cote 93, scan 122 insertion “uniques à… transformation diagonale”; kind: unpursued implication.** In the truncated model, comparing the coefficients of 1,t,t² shows that all matrix solutions form one free line after the root extension, so invertible solutions differ by a common unit scalar, not by arbitrary independent diagonal operations. This clarifies the normalization language in Hua IX and the sufficient role of Pic(A)=0 in D10; D14 separately removes that hypothesis when q is odd.

### D12 — The literature comparison concerns different invariants

**Cote 93, scans 121–124; kind: own idea; confidence: high for the checked comparison, no priority claim.** Hoshi's 2024 paper, Definition 6.2 and Remark 6.4.2, confirms the collapse of the level-one invariant for p≤3, while its §3 treats level two in characteristic 2 through locally exact differentials. This supports Hua IX's distinction from the quadratic-differential-valued G_0 but neither proves novelty nor settles all links to Cartier or p-curvature.

### D14 — Odd degree removes the Picard hypothesis

**Cote 93, scans 122–123, Pic(A)=0 and the general-alpha reduction; kind: own idea; confidence: high, determinant and exterior-power argument.** In D10 the descended matrix-solution line K has K²≅A via the determinant, while its unit denominator gives K⊗_A B≅B. Taking top exterior powers as A-modules, with B free of rank q, gives K^q≅A; when q is odd this forces K≅A, so Pic(A)=0 is unnecessary for p>2. This is an implication checked in this run that adds to Hua IX lines 1540–1556, with no novelty claim; for q=4 the argument gives a possible 2-torsion line obstruction and makes no claim that such an obstruction is realized.
