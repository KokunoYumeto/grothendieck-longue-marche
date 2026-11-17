## 3. Weierstrass algebra: verified statements, failures and convention questions

For this section, F_n means H⁰(E,O_E(nO)), and D_δ is the invariant derivation with value δ at O; this interpretation is stated rather than silently imposed on the ink. The manuscript's field is algebraically closed and has characteristic different from 2. Proofs, exact identities and the finite-field matrices are in `records/research_algebra.md` and `records/verify_algebra.py`.

### ALG01 — The quotient arrow depends on the pole order

**64/102–103, (6)–(11), right arrows; kind: unproved claim.** Quote: “μ_δ est la multiplication par δ” and “can.” **Search:** `parties principales`, `principal parts`, `dérivation`, `Weierstrass`; Hua, “L'algèbre des fonctions à pôle à l'origine,” lines 1610–1619; `MPL_142_001-093_notes.md`, N016.2, scan 016, concerns a different Artin–Schreier obstruction. **Relationship:** agrees with Hua under his convention and adds the scaling check; **register:** no exact settled entry.

With canonical principal parts, differentiating a Laurent leading term gives gr_n(D_δ)=−nμ_δ, which vanishes if the characteristic divides n. Multiplicative rescaling ε_n=cⁿpp_n changes this to −ncμ_δ, still dependent on n. All-degree coefficient-one arrows, multiplicative symbols and the Leibniz rule cannot hold simultaneously, because applying the derivation to the square of a degree-two term would give both one and twice the same nonzero symbol. This refutation, **ALG01-R**, does not determine the uncertain exponent in the frozen diagram.

### ALG02a — The exact positive-characteristic kernel

**64/103, (12) and the following sentence; kind: unproved claim.** Quote: `Ker Θ_δ=F₁=k.1_E`. **Search:** `noyau`, `ker`, `puissances`, `Frobenius`; Hua, algebra subsection, lines 1620–1626; `MPL_146_001-099_notes.md`, R079 at scan 063, is a different principal-unit obstruction. **Relationship:** contradicts the unrestricted assertion, refines Hua's warning; **register:** none.

For δ≠0 and the stated perfect field of characteristic p>0, the exact answer **ALG02-R** is `ker(D_δ|F_n)={g^p:g∈F_floor(n/p)}`. The differential-kernel theorem [Stacks 031W] and orders of zeros and poles prove this, so the dimension is max(1,floor(n/p)) and the first nonconstant element occurs at order 2p. A nonconstant x∈F₂ gives the immediate witness x^p. The nonzero map F₂→F₃⁻ still works because 2 is invertible, so this failure does not by itself destroy the later coordinate construction.

### RC08 — Invertibility of n does not cure an earlier kernel jump

**64/103 (12), compared with Hua's added qualification; kind: unproved claim.** **Search:** `n inversible`, `Ker`, `puissances`; Hua, same subsection, lines 1620–1626. **Relationship:** contradicts a modernization assertion; **register:** none.

Hua claims that n invertible in k suffices for `ker Θ_δ∩F_n=k`. Taking n=2p+1 leaves x^p∈F_{2p} inside F_n and killed by the derivation, even though p does not divide n. **RC08-R** retains the nonzero-δ characteristic-zero assertion and uses ALG02-R in positive characteristic; invertibility at the final graded step cannot erase kernels created earlier.

### ALG02b — Graded and filtered constants are different

**64/102–104, graded algebra and (12); kind: reading question.** **Search:** `gradu`, `algèbre`, `dérivation`; Hua, algebra subsection; no exact non-Hua kernel statement found. **Relationship:** adds a typing qualification; **register:** none.

On F_∞, the characteristic-zero kernel for δ≠0 is k, but on the graded ring R=⊕F_nTⁿ the degree-one derivation kills a distinct constant section in every degree. Its characteristic-zero kernel is k[S], where S=1·T, and its characteristic-p kernel is R^p[S]. Thus the interpretation of (12) must retain which of the graded and filtered algebras is meant.

### ALG03 — The monic cubic is convention sensitive

**64/105–106, (22)–(28); 115 opening; kind: reading question / own idea. Confidence: high for the algebraic alternative, undetermined for authorial intention because ε_n has no explicit Laurent definition here.** Quote: “wp'=Θ_δ(wp)” and “donc ε₃(wp')=δ³.” **Search:** `epsilon`, `principal parts`, `Weierstrass`; Hua, algebra subsection, lines 1636–1649. **Relationship:** differs in convention and adds a consistent alternative; **register:** none.

Ordinary principal parts give ε₃(D_δwp)=−2δ³ and leading cubic coefficient 4. The multiplicative convention ε_n=(−1/2)ⁿpp_n makes ε₂(wp)=δ², ε₃(D_δwp)=δ³ and the monic cubic hold together, but then the quotient arrow is (n/2)μ_δ. Hua instead fixes ordinary principal parts and uses y=−D_δwp/2, a coherent editorial normalization. The isolated monic cubic therefore does not force an unconditional factor-four repair, while ALG01's all-degree problem remains.

### ALG03b — The selected tangent vector must be nonzero

**64/105, (22)–(25), compared with 115 opening; kind: unproved claim.** Quote: `δ∈t_E`, then “base”; 115: “une base.” **Search:** `delta`, `base`, `chois`; Hua, algebra subsection. **Relationship:** adds the hypothesis needed by the subsequent basis assertion; **register:** none.

The frozen (22) has no nonzero marker, yet δ=0 permits only a constant normalized wp and gives wp'=0, so the displayed bases in (25) fail. The explicit word “base” at 115 supplies the intended restriction in that later passage. This mathematical necessity belongs here rather than as an added star or inequality in (22).

### ALG04a — The prime in (33) can be tested without choosing the ink

**64/108, (32)–(33); kind: reading question.** Quote: the frozen single/double-prime alternative on wp. **Search:** `dérivation`, `Weierstrass`; Hua, algebra subsection, lines 1682–1687. **Relationship:** differs in editorial presentation and adds a local counterexample; **register:** none.

For y²=f(x) and Dx=y, preservation of the relation forces Dy=D²x=f'(x)/2. At a finite branch point, y=0 while f'(x)/2≠0, so the single-prime interpretation fails there and the double-prime interpretation agrees with (32). This conditional compatibility check does not settle the paleography or alter the frozen alternative.

### ALG04b — The squared a₂ term is likewise a compatibility question

**64/108, (31) against (32); kind: reading question.** Quote: the uncertain `a₂P²|a₂P` term. **Search:** `Weierstrass`, `dérivation`, `algèbre`; Hua, algebra subsection. **Relationship:** adds an exact residual test; **register:** none.

Keeping a₂P² in the relation while retaining the derivation in (32) gives the residual a₂(1−2P)P', nonzero in general. Keeping a₂P gives zero. The computation isolates the algebraic consequence of the two readings without promoting the mathematically compatible reading to certainty about the ink.

### R17a — The Vandermonde argument really completes its local task

**64/105 end–106 upper half, Proposition 1 and corollary; kind: unproved claim, checked.** Quote: “il reste à voir” and “sont tous distincts, O.K.” **Search:** `Vandermonde`, `restriction`, `wp`; Hua, algebra subsection, lines 1650–1663. **Relationship:** restates and verifies the proof rather than leaving its temporary task open; **register:** none.

After the permitted affine change, the values −1/t, 1/(1−t), 0 are distinct for t≠0,1, which makes the three-by-three Vandermonde determinant nonzero. Odd functions vanish at nonzero two-torsion because 2 is invertible, while restriction is injective on the span of 1 and wp. This proves the stated kernel F₃⁻=k·wp' and justifies uniqueness of the cubic coefficients once wp is fixed.

### R17b — The cubic degree and constant sign remain diplomatic alternatives

**64/107, Proposition 2 and (29); kind: reading question.** Quote: `wp^{2|3}` and the uncertain minus/plus sign before a₃. **Search:** `Vandermonde`, `sym`, `Weierstrass`; Hua, algebra subsection, lines 1664–1675; later current scan 114 (59). **Relationship:** differs from the modernization's settled cubic formula, adds compatibility evidence; **register:** none.

The proof on 107 itself uses −wp³, and the elementary-symmetric statement requires the polynomial wp³+a₁wp²+a₂wp+a₃. For example roots 1,2,3 give x³−6x²+11x−6, so changing the sign of that fixed a₃ changes the polynomial. This supports the cubic-degree and plus-sign alternatives mathematically, while both frozen doubts remain unchanged.

### RC09 — Fixing δ does not fix the cubic coefficients

**64/106 bottom margin; 107 (30); 114 (55)–(58); kind: reading question / unpursued implication.** Quote: “pour [wp choisi]”, marked uncertain in the frozen margin. **Search:** `choisi`, `coefficients`, `Weierstrass`; Hua, algebra subsection, lines 1664–1675. **Relationship:** contradicts Hua's “pour δ choisi” assertion; **register:** none.

For fixed δ, replacing x=wp by x+b preserves its principal part and derivative but sends a₁ to a₁−3b, a₂ to a₂−2a₁b+3b², and a₃ to a₃−a₂b+a₁b²−b³. Thus **RC09-R** fixes wp and the ordinate convention, or imposes an additional condition removing the additive ambiguity. The manuscript's affine freedom at 114 and trace-zero restriction at 107 preserve precisely this distinction.

### R18 — The characteristic-three qualification is necessary

**64/107, Corollary 2 and (30); 114 closing; kind: unpursued implication.** Quote: “Si car. k≠3.” **Search:** `caractéristique`, `trace`, `somme`, `Weierstrass`; Hua, algebra subsection and “Les involutions σ_i.” **Relationship:** restates and checks the stated restriction; **register:** no exact settled entry.

The trace of the constant function 1 over J is 3, so the trace-zero kernel complements constants in F₂ when 3 is invertible. In characteristic three the constants lie in that kernel, and translating x cannot change a₁ because a₁↦a₁−3b. The restriction is therefore structural, not an unnecessary exclusion inherited from a short Weierstrass equation.

### ALG05 — The inverse construction needs its grading

**64/109, (34)–(37), compared with 114 (57); kind: unproved claim.** Quote: “on vérifie que … définissent une courbe elliptique.” **Search:** `quadratique`, `ramifi`, `courbe elliptique`, `Proj`; Hua, end of the algebra subsection. **Relationship:** agrees and supplies the omitted verification; **register:** none.

For squarefree f of degree three and characteristic different from 2, Y²Z=X³+a₁X²Z+a₂XZ²+a₃Z³ is smooth with origin [0:1:0] and genus one [Stacks 0BYA]. The pole section ring is k[S,X₂,Y₃]/(Y₃²−X₂³−a₁X₂²S²−a₂X₂S⁴−a₃S⁶), with degrees 1,2,3; its Proj reconstructs E, while the ungraded affine algebra alone does not specify that operation. The three finite roots and infinity are all branch values, with the latter explicitly included at 114. This fills the algebraic check without choosing the frozen star/infinity subscript or supplying the still-promised canonical pinning construction.

### ALG06 — The determinant's missing hypothesis is already repaired

**64/110–111, Proposition 3, insertion and left NB; kind: self-flagged / withdrawn in the same text.** Quote: “Si deux parmi les x,y,z sont égaux, (42) est tjrs vérifié.” **Search:** `corde`, `loi d'addition`, `distincts`; Hua, “La loi d'addition,” lines 1703–1722. **Relationship:** restates the corrected proposition and preserves the author's correction; **register:** none.

For three distinct nonzero points, the determinant criterion and divisor proof are correct. Repeated rows lose contact multiplicity: on y²=x³−x the triple (0,0),(1,0),(0,0) has zero determinant but nonzero sum (1,0). The inserted “tous distincts,” the NB, and the converse at 111 already repair the broad formulation, so it must not be counted as a live unresolved error.

### ALG07a — Formula (51) gives the negative of the sum on the secant domain

**64/112–113, (47)–(51), NB and last paragraph; kind: unpursued implication.** Quote: “Par principe de prolongement” and “dès que x₀≠y₀.” **Search:** `loi d'addition`, `prolongement`, `distincts`; Hua, “La loi d'addition.” **Relationship:** restates the final domain and adds a precise factorization; **register:** none.

With λ=(r−q)/(u−v), μ=(qu−rv)/(u−v), and w=λ²−a₁−u−v, the exact identity f(t)−(λt+μ)²=(t−u)(t−v)(t−w) proves the formula for −(P+Q). It remains valid when the third intersection coincides with P or Q, so the initial exclusions involving −2P or −2Q can be removed. Condition (50) alone does not exclude P=−Q, as (3,5),(3,−5) on y²=x³−2 show; the earlier NB u≠v must be retained. This checks the manuscript's extension and its ordinate sign rather than supplying a different addition convention.

### ALG07b — Tangent continuation is a precise further consequence

**64/113, final extension; kind: own idea. Confidence: high, because the factorization is exact and uses the displayed monic equation.** **Search:** `tangente`, `loi d'addition`, `prolongement`; Hua, addition subsection; primary comparison [Lynn]. **Relationship:** adds the omitted tangent case; **register:** none.

For P=(u,v) with v≠0, set λ=f'(u)/(2v), μ=v−λu and w=λ²−a₁−2u. Then f(t)−(λt+μ)²=(t−u)²(t−w), so (w,λw+μ)=−2P. If v=0 then 2P=O, and the formulas otherwise remain valid in characteristic three because they divide by 2v, not by 3.

### ALG08 — The final Möbius coefficient is correct

**64/115, lower half, after (60); kind: unproved claim, independently checked.** Quote: “Déterminons l'autom involutif.” **Search:** `Möbius`, `involuti`, `Klein`, `quatre points`; `MPL_142_094-122_notes.md`, B01, scan 108; `MPL_147_003-047_notes.md`, Appendix B; Hua, “Les involutions σ_i et les points d'ordre 4.” **Relationship:** adds the elliptic translation interpretation and arbitrary-root formula; **result link:** LM4 D.12 remains open.

Let A_i=(ξ_i−ξ_j)(ξ_i−ξ_h); the written b gives σ_i(z)=ξ_i+A_i/(z−ξ_i). Its matrix squares to A_iI and has determinant −A_i≠0, proving the stated involution and exchanges of branch points. Translation by nonzero two-torsion commutes with negation and has these same branch permutations, so it descends to this map; the three maps form the geometric Klein four group. This verifies the endpoint's formula without importing a later fixed-point equation into scan 115 or classifying profinite torsion.
