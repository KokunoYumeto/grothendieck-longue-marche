# Research comparison: S20, cote 93 leads, and Hua's reading

Research only, written after the parent's freeze at **2026-11-17 23:01:38 UTC**. This agent read `context/README.md`, all of `context/notes/RESULTS_STATE.md`, and `context/hua_project/README.md` before reading the entire 2,120-line `context/hua_project/64.modern.tex`. It then compared the relevant material with the frozen page TeX for scans 078–115. It performed no image audit and changed no transcription, page, inventory, or doubts file. These are proposed notes for integration, with local identifiers RC01–RC13.

**Citation conventions.** A locator such as **64/082 (31)** means cote 64, scan 082, formula (31), in `MPL_64_078-115/pages/MPL_64_078-115_64_scan082.tex`. Hua's modernized page number is the archive foliation: **Hua page n = supplied scan n+1**. Thus his pp. 74–79 correspond to scans 075–080, of which only 078–080 are supplied here. The findings-register locator is truncated and its explicit scan list does not exhaust its stated page interval; preserve the overlap boundary. Every reference to Hua below credits **Michel Hua's project, AI-produced modernized reading**, not an independent transcription or established result of this run.

## RC01 — S20 has an object-level lead, not local manuscript confirmation

**Kind:** observation and unpursued implication. **Relationship:** differs from the proposed identification; adds a precise scope limitation. **Context:** `context/README.md`, “What our planning document asks of these folders,” lines 17–21, **S20**; `context/SECTIONS_STATE.md`, §11b, lines 218–226, and §21, lines 370–379. **Manuscript:** 64/081–083 (27)–(34); 64/101 title; 64/102–104 (1)–(18); 64/108 (32)–(33); 64/109 (35)–(37).

The supplied range constructs a moduli problem for elliptic curves with finite pinnings, then the algebra of functions with a pole at the origin of **one elliptic curve over k**. Its operation is explicitly a “dérivation de degré +1” (64/103 margin), indexed by a tangent vector at the elliptic origin. Neither that derivation nor the projective quotient `Σ_J` is a connection on the parameter space. A Gauss–Manin comparison would require a family `f:E→B`, its rank-two relative de Rham cohomology, and differentiation in directions of **B**; none is constructed in scans 078–115. A projective connection likewise requires more than the projective line `Σ_J`, the line `O(1)`, and its tensor square.

| S20 ingredient | What the supplied range contains | What it does not supply |
|---|---|---|
| Elliptic family / base | Claimed fine moduli scheme `U_{0,3}×μ₄*`, universal tangent line, 085–086; standard curve for `(J,t,α)`, 094–095 | Relative de Rham complex or its cohomology bundle |
| Differential operation | `Θ_δ:F_n→F_{n+1}` on a fixed elliptic curve, 102–108 | A horizontal derivative in the modular parameter; Gauss–Manin matrix |
| Positive characteristic | Characteristic ≠2 throughout; a characteristic-3 qualification at 107 and 114 | Frobenius, Cartier operator, crystalline cohomology, Hasse invariant, or p-curvature |
| Projective geometry | `E/±1≃Σ_J`, tangent-square identification, 081–082 and 096–097 | Projective connection / Schwarzian equation / indigenous bundle |
| Uniformization | Algebraic Weierstrass equation and chord addition, 105–115 | Period integrals, a Picard–Fuchs equation, or analytic universal covering in this range |

**Verdict on S20 for this range:** no explicit bridge is present. This is not a refutation of the wider historical hypothesis about cotes 93 and 159. A defensible future comparison is to put Gauss–Manin on the family parametrized here and identify its characteristic-p invariants with an actual construction in those cotes. That is our proposed task, not an implication proved in the manuscript. The kernel error at 103 (RC08 below) warns against carrying a characteristic-zero differential argument into characteristic p; it is not itself evidence that the Cartier operation is being discussed.

A contemporary primary reference makes the distinction concrete: Katz (1972), introduction, defines a differential equation as a vector bundle with integrable connection; §2.0.2.2 concerns the functions killed by relative derivations, §2.1 the Cartier operation, and §2.3.1 the conjugate filtration with Gauss–Manin. This supplies a comparison framework, not provenance for these manuscript pages. See the bibliography and source-use limits below.

## RC02 — The cote 93 comparison cannot be settled from truncated register headings

**Kind:** reading question / evidence limitation. **Relationship:** adds limits; neither proves nor refutes the prior notes. **Context:** `context/notes/RESULTS_STATE.md`, orientation lines 21–25, the five entries at 297–301, and the missing-source path at 494. The file `MPL_93_002-046_notes.md`, its transcription, and cote 159's text are not supplied in `context/`. The register's §1 excerpt at line 443 is also truncated.

| Prior entry | What may be compared here | What remains unavailable |
|---|---|---|
| **MPL_93_002-046 P09** | The explicit moduli datum and distinction between the tangent of E and that of `Σ_J` (081–083, 094–099) | The actual list of P09's comparison points; it must not be reconstructed from its title |
| **E14**, “Formal deformation versus the coarse invariant” | Stack/groupoid distinctions (083–086) caution against identifying a coarse parameter with a complete deformation problem | Formal base, equation, orders, characteristic and the conjecture itself |
| **E16**, “Families realizing the two smallest displayed orders” | Smooth cubic families can be written from 109's discriminant criterion | Which orders or families E16 means, and their asserted realization |
| **C29**, “A first-order bridge back to the elliptic deformation sheet” | Tangent-square data in 082 (30), 094 (a), 096 (61) provide a candidate comparison datum | The sheet, its first-order equation, and the map C29 asserts |
| **C35**, “A concern about Problem 1 is withdrawn by the following explanation” | Respect the supplied status **withdrawn in the same text** | The concern and the explanation; there is no basis here to reopen or overrule the withdrawal |

The supplied catalogue-oriented `SECTIONS_STATE.md` §11b says cote 93 contains Gauss–Manin / Picard–Fuchs / Cartier material and a copy of Deligne's elliptic-curve formulary; §21 says a link from cote 159's projective structures to later p-adic Teichmüller theory “is not established.” Those are contextual leads only. They do not substitute for the missing notes. No status change for P09, E14, E16, C29 or C35 is justified.

## RC03 — Hua's Legendre-pinning moduli lead is substantially supported, with stated limits

**Kind:** observation. **Relationship:** restates and sharpens the credited lead. **Credit / result ID:** **Hua, findings register, `64-legendre-pinning-moduli`**, supplied at `context/notes/RESULTS_STATE.md:467`; **Hua, modernised reading of cote 64**, “L'épinglage de Legendre sur un corps” and “L'épinglage de Legendre sur une base ; le schéma de modules” (`64.modern.tex:1309–1519`).

The register entry stops at “form a…” and cannot itself be treated as a complete theorem. The complete modernized reading asserts the fine scheme `U_{0,3}×μ₄*`; this is stated directly in the frozen manuscript, 64/085–086 (35)–(39). The pages support the following more exact formulation:

- A Legendre pinning is the **line isomorphism** `κ:T_{E/S,0}→O(1)_t^sharp`, whose tensor square determines an orientation identification `α:μ₄*≃ω_J` (082–083, (31)–(34)). Calling it simply a tangent vector, as the register digest does, suppresses its nontrivial target and twisting data.
- For fixed α the pinnings form a μ₂-torsor (083); without fixed α they form a μ₄-torsor `L_{E/S}` (087–088, (43)–(44)). These are distinct statements, correctly distinguished in Hua's full reading.
- The Legendre-pinned groupoid alone is explicitly “n'est pas rigide” (084); adding the Jacobi level-2 numbering is what yields the claimed fine scheme (085–086). The exact exceptional stabilizers are handled in the parent's separate algebra note.
- Scans 089–092 add the product-group action, its mixed character, the subgroup `D'_3`, and the line-bundle action. Those formulas are genuine local support for the fuller claim, not a consequence inferred merely from the word “Legendre.”

The passage **asserts** representability and equivalence of groupoids; it does not include a full construction proof. Scan 083's margin expressly asks for the construction (RC11). Novelty remains unestablished: the register's “candidate: their search found no reference” is a report about a search, not a mathematical novelty verdict.

**Nearest checked literature, following Hua's lead.** Antieau–Meier, arXiv:1608.00851v3, §4, Definition 4.4 and Proposition 4.5, give the Legendre parameter scheme X and `M(2)≃BC₂,X`; Corollary 4.6 identifies X as coarse moduli. The paragraph following that corollary distinguishes the strictly S₃-equivariant coarse map from the atlas `π:X→M(2)`, which is not S₃-equivariant. Lemma 4.7 recovers equivariance using twists of C₂-torsors; its proof explicitly cautions that the resulting S₃-action on `BC₂,X` is not strict. This checks Hua's nearby citation. It does not identify the exact μ₄-twisted pinning and action in these scans as either new or already published. The paper itself describes its presentation as standard.

## RC04 — Hua's concrete choice of Q₀ is a useful credited addition

**Kind:** independent re-proof of an external lead. **Relationship:** adds an example to the manuscript. **Credit:** Hua, modernised reading of cote 64, “L'épinglage de Legendre sur un corps,” footnote at `64.modern.tex:1371–1376`. **Manuscript:** 64/078 (16)–(19), especially `s_{i'}=i s_i`.

Hua proposes `Q₀={x⁴=−4}` over `Z[1/2]`, with `s_i=1−i`. This polynomial is not written in the supplied scan, so it remains Hua's addition. It checks directly: `(1−i)²=−2i`, `(1−i)⁴=−4`, `i(1−i)=1+i=s_{−i}`, and `−s_i²/2=i`. Since x is a unit on this degree-four cover and 4 is invertible, it is finite étale; scalar multiplication makes it a μ₄-torsor. The map `x↦−x²/2` realizes the diagonal quotient as μ₄*. It becomes trivial after choosing i, agreeing with 086's use of the base μ₄*. This is a recheck of Hua's example, not a new result claimed here.

## RC05 — A modernization error reverses a manuscript correction: μ₄ versus μ₄*

**Kind:** targeted proof check and reading comparison. **Relationship:** contradicts the modernization; the manuscript is correct on this distinction. **Credit / locator:** Hua, modernised reading of cote 64, “L'épinglage de Legendre sur un corps,” `64.modern.tex:1364–1366`; frozen 64/078 (16)–(17).

Hua writes `ω_{Q₀}≃μ₄*`, then “c'est-à-dire `μ₄*≃Aut⁺(Q₀)`.” The second isomorphism cannot hold: over an algebraically closed field of characteristic ≠2, the primitive-root set has two elements and the rotation group of a square has four. The correct formulation, **RC05-R**, is `μ₄≃Aut⁺(Q₀)`, with the induced identification between its generators and `ω_{Q₀}`. Frozen scan 078 (17) already has μ₄ with the asterisk **deleted**. Thus this is not an error to charge to the manuscript; it is introduced by the supplied modernized reading.

## RC06 — The missing tensor square is inherited, not repaired

**Kind:** targeted proof check. **Relationship:** the modernization restates an erroneous general formula; the next manuscript formula supplies its intended special case. **Locators:** 64/080 (22)–(23), margin; 64/081 (26)–(27); Hua, “L'épinglage de Legendre sur une base ; le schéma de modules,” `64.modern.tex:1399–1415`.

Both texts print `M^sharp⊗M^sharp≃M^b` while defining `M^b=M∧_{μ₂}μ₄*`. This loses a tensor power. The corrected statement **RC06-R** is

\[
M^\sharp\otimes M^\sharp\simeq(M\otimes M)^b.
\]

Indeed, the scan's own margin gives `M^sharp=M⊗O_S^sharp`; squaring doubles M as well as the twisting line. For a line-bundle counterexample, take `S=P¹_C`, trivialize Q₀ and μ₄*, and let `M=O(1)`; the printed identity would identify `O(2)` with `O(1)`. More generally the claimed formula is already incompatible with ranks for a module of rank >1. Scan 081 (27), and Hua's very next displayed specialization, correctly use `O(2)` for the square of `O(1)^sharp`. No transcription correction is licensed by this mathematical diagnosis.

## RC07 — Hua's derivative repair is coherent under his chosen principal-part convention

**Kind:** normalization question and targeted mathematical check. **Relationship:** differs from literal formulas; the modernization makes an additional convention. **Locators:** 64/102 (6); 64/103 (9)–(11); 64/105 (23)–(24); 64/106 (28); 64/108 (32)–(33); Hua, “IV. … L'algèbre des fonctions à pôle à l'origine,” `64.modern.tex:1610–1619,1636–1649,1682–1687`.

Hua explicitly defines εₙ as the ordinary leading principal-part map: if z is dual to δ and `f=c z^{-n}+…`, then `εₙ(f)=cδⁿ`. Under that convention, `gr_n Θ_δ=−n μ_δ`, so the replacement `y=−Θ_δ(℘)/2` gives a monic cubic and the stated corrected derivation. The frozen text does not explicitly give that local definition of εₙ; it does call Θ a derivation and its quotient arrow multiplication by δ.

A coordinated independent check by this run's algebra agent supplies another consistent multiplicative normalization: `εₙ=cⁿ ppₙ` gives quotient coefficient `−nc`; at `c=−1/2`, the monic package `℘'=Θ_δ℘`, `ε₂(℘)=δ²`, `ε₃(℘')=δ³` is consistent, while the quotient arrow becomes `(n/2)μ_δ`. The calculation follows immediately by applying the rescaled maps to `d(z^{-n})`. Thus the all-degree coefficient-one diagram requires correction under either normalization, but the isolated monic cubic does **not** force an unconditional factor-four editorial repair. Credit Hua's repair as his chosen convention; preserve the manuscript's prime, coefficient and exponent readings. This note does not duplicate the parent's full algebra check.

## RC08 — Hua's restricted kernel claim still fails in positive characteristic

**Kind:** targeted proof check. **Relationship:** contradicts an added assertion of the modernization while agreeing with its warning about p-th powers. **Locators:** 64/103 (12); Hua, preceding §IV subsection, `64.modern.tex:1620–1626`.

After correcting the quotient coefficient, Hua says that **n invertible in k** implies `ker Θ_δ∩F_n=k`. This implication is false even with δ nonzero. Let `char k=p>2` and take a nonconstant `f∈F₂`; Riemann–Roch and `F₁=k` give a pole of order exactly 2. Then `f^p` is nonconstant, has pole order 2p, and is killed by every k-derivation. Put `n=2p+1`, which is invertible in k: `f^p∈F_n` contradicts the assertion. Injectivity on the nth associated quotient only identifies the kernel at n with the preceding kernel; it does not make earlier kernels disappear.

**RC08-R:** with δ nonzero, the characteristic-zero assertion is valid; in positive characteristic the unrestricted kernel is not k. The exact filtered-kernel refinement is supplied separately by the algebra agent. δ=0 must also be excluded from the characteristic-zero assertion; the original 105 (22) omits a nonzero marker, whereas 115 explicitly says δ is a base. These are mathematical qualifications, not changes to the diplomatic text.

## RC09 — Fixing δ does not fix the Weierstrass coefficients

**Kind:** targeted proof check. **Relationship:** contradicts a modernization change and restates the manuscript's retained affine ambiguity. **Locators:** Hua §IV, `64.modern.tex:1664–1675`; 64/106 bottom margin, 64/107 (30), 64/114 (55)–(58).

Hua says the coefficients are uniquely determined “pour δ choisi.” Frozen scan 106 reads “pour [℘ choisi]” (the word is marked uncertain there); scan 114 explicitly permits `℘↦a℘+b`. Fixing δ and the principal part still permits `X'=X+b`, leaving `Y=−Θ_δX/2` unchanged. Substitution into `Y²=X³+a₁X²+a₂X+a₃` gives

\[
a'_1=a_1-3b,\qquad a'_2=a_2-2a_1b+3b^2,\qquad
 a'_3=a_3-a_2b+a_1b^2-b^3.
\]

Already over characteristic zero with b=1, a₁ changes. **RC09-R:** the coefficients are determined once ℘ (and the y-normalization) is fixed; δ alone suffices only after an additional normalization that removes the additive ambiguity, such as the trace-zero normalization explicitly restricted to characteristic ≠3 in 107 and 114.

## RC10 — Other notation and convention changes must remain visible

**Kind:** reading questions / convention comparisons. **Relationship:** differs; not automatic mathematical contradiction. **Credit:** Hua, modernised reading of cote 64, the two Legendre-pinning subsections and §IV.

| Comparison | Exact local evidence | Research-note treatment |
|---|---|---|
| Action side | 64/089 inserts “à g.”; Hua `64.modern.tex:1479–1480` says “à droite” | Inversion can convert a left action to a right action, but the conversion must be stated before comparing characters or formulas; do not silently normalize the transcription |
| Jacobi / Torelli | 64/085 deletes “Torelli” and inserts “Jacobi”; 086 still reads “Legendre-Torelli.” Hua `1465–1467` says the latter proper name was not read | The frozen diplomatic reading adds an exact surviving terminological inconsistency; later complex Torelli structures in Hua are outside this range |
| Tensor-twist symbol | Frozen 080–100 use an uncertain sharp-like symbol; Hua `1405–1406` chooses `natural` and acknowledges an unidentified zigzag | A deliberate notation choice, not a newly deciphered glyph |
| Meaning of λ=t | 079–080 put the three nonzero 2-torsion images at `0,1,∞` and the identity image at t; Hua `1391–1393` calls this the Legendre family with λ=t | Sending the identity to ∞ while preserving the order of the first two labelled branch points uses `x=(1−t)z/(z−t)`, giving λ=1−t. Using `x=t(z−1)/(z−t)` gives λ=t while swapping those labels. The identification requires a stated ordering convention |
| U-index / prime | Hua `1661–1662` reports `U_{0,1}` where frozen 106 reads `U_{0,3}`; Hua `1685` prints ℘″ where frozen 108 (33) retains an uncertain single/double-prime reading | Differences between two readings. This research comparison has not reopened the images and cannot settle the palaeography |
| Projective convention | Hua `1325–1329` explains `O_t(1)=V_J/F_t`; frozen 097 (62) states precisely that quotient and its twisted dual | Support for this convention is within the supplied range; one need not borrow later unsupplied pages to justify it |

The infinity in 109 (37), 114 (54), and 115 is the image of the **identity in the quotient of a single curve**. Neither that coordinate nor the above label conversion identifies it with a modular cusp. The parent's B5 note treats this distinction in the wider context.

## RC11 — Self-flagged incompleteness and an actual withdrawn formulation

**Kind:** observation. **Relationship:** supports Hua's caution, adds exact manuscript markers; does not manufacture a proof from the subsequent presentation.

1. **64/083 margin**, beside (34): “Il faudrait expliciter la construction de E … (via … fonctions ℘ de Weierstrass).” Hua's statement that representability is asserted without demonstration (`1466–1467`) is supported. The cubic reconstruction in 109 supplies algebraic ingredients, but this range does not finish the promised canonical pinning construction.
2. **64/093 closing paragraph:** “Il faut maintenant définir” the relative level-4 Jacobi pinnings and “montrer comment” one canonically defines a Legendre pinning. This is an announced task. Hua `1511–1518` correctly preserves it as a program; its stronger statement that the whole dossier leaves it unfinished relies on later material outside these scans.
3. **64/100 final line:** “Il reste ensuite à exprimer (73).” Hua, “Explicitation calculatoire,” `1588–1599`, correctly stops at that point. The three relations of the abstract lemma at 099 are present; the requested complete coordinate expression is not.
4. **64/110 Proposition 3 and left margin:** the surviving hypothesis is “tous distincts,” after a cancelled “pas … égaux”; the margin says that if two points coincide, the determinant is always zero without necessarily having `x+y+z=0`. Scan 111 uses pairwise distinctness in the converse. Hua's “La loi d'addition,” `1703–1722`, states the corrected proposition but compresses the manuscript's explicit correction. This is an author-local withdrawal of the too-broad determinant criterion, not an unresolved objection. It must not be conflated with **MPL_93 C35**, whose separate withdrawal is known only from a register heading.

## RC12 — Topics in the full Hua file outside scans 078–115

**Kind:** credited external leads, with boundary notes. The entire modernized file was read, but only overlapping frozen TeX was compared. These rows identify topics deserving their own notes without treating unsupplied images or a referenced Lean file as checked evidence.

| Hua subsection / file locator | Claimed topic | Relation to this packet and proposed note |
|---|---|---|
| “I. Fourbis combinatoires,” §§1–6, `233–898`; “Une proposition sur End(V),” `899–929` | Squares, S₄, orientations, the description of a free rank-two Z/4-module by `(I,Q,k)`, and its octahedron; several explicit editorial corrections | **Outside range**, Hua pp1–42 → scans002–043. Supplies provenance for the fixed square Q₀ and the future level-4 structures used here; not re-proved or image-checked in this packet |
| “II. Structures octaédrales…,” `930–1077` | A characteristic-5 exception to unqualified octahedral automorphism claims; Hua reports a Lean check | **Outside range**, pp43–52 → scans044–053. A separate credited lead about exceptional characteristic. The cited Lean file and original pages are not supplied; do not mark this run as having verified the certificate |
| “Courbes relatives de type (0,4)” and “Relation avec les courbes elliptiques; f₂ᵗ,” `1080–1230` | Klein quotient, the four-pointed line, and multiplication-by-two on it | **Outside range**, pp53–64 → scans054–065. These would support a fuller `(0,4)↔(1,1)` comparison, but this packet contains only later uses of `Σ_J` and the start of the 2-torsion translation formula at 115 |
| “Détermination de M₁,₁(4),” `1232–1268`; Kummer digression, `1270–1307` | An unfinished level-4 moduli determination; a tangential Kummer equivalence stated “je dis” without a proof | **Outside range**, pp65–73 → scans066–074. Their existence in Hua's interpretation does not license claiming that 078–115 proves the general Kummer equivalence. The `μ₂`-twisting description actually written at 094–095 is the local comparison point |
| “Vers l'épinglage de Legendre,” `1778–1845` | Further attempt at the level-4-to-Legendre construction, still saying “Dieu sait comment — il faudra y revenir”; subsequent coordinate calculation | **Outside range**, pp117–125 → scans118–126. Supports only a credited later lead; does not complete scan100 inside the supplied packet |
| Two “Approche transcendante” subsections, `1847–2054` | Lattices, complex Torelli rigidification, upper half-plane, SL₂(Z), a q-expression, and a differential rigidification; Hua repairs a conjugation convention | **Outside range**, pp126–151 → scans127–152. This is Hua's concrete uniformization content in cote64. It should guide a later S20 check, but cannot be imported into scans078–115 or identified with Gauss–Manin / Cartier merely by subject resemblance |
| “VI. Appendice: normalité des extensions quadratiques,” `2056–2118` | Normality in dimension one, a higher-dimensional caveat, and a proposed quadratic cover with exceptional modular parameter; Hua identifies 1728 as an editorial inference | **Outside range**, pp152–156 → scans153–157. No inference from that proposed j=1728 identification can settle **LM6 A.22** or **LM7_PUSH E.3** here. Their required profinite CM information is absent from this range |

## RC13 — An explicit Legendre differential equation and its characteristic-p polynomial solution

**Kind:** own calculation / conventional comparison, not a novelty claim. **Relationship:** adds a concrete possible S20 comparison beyond the manuscript. **Manuscript starting points:** the parameter scheme at 64/085–086 (37), smooth cubic reconstruction at 109 (34)–(37), and the distinction between quotient coordinates at 079–080 and 114. **Context:** S20 in `context/README.md:18–19`; Hua, “L'épinglage de Legendre sur un corps,” `64.modern.tex:1385–1393`, subject to the parameter-label convention in RC10. This calculation does not settle the unavailable **MPL_93 P09/E14/E16/C29** statements.

Choose the conventional smooth Legendre family over the characteristic-zero base `B=Spec Q[λ,1/(λ(1−λ))]`, so **λ≠0,1**:

\[
y^2=P=x(x-1)(x-\lambda),\quad \omega=dx/y,\qquad
L=\lambda(1-\lambda)\partial_\lambda^2+(1-2\lambda)\partial_\lambda-\tfrac14.
\]

Here `∂_λ` differentiates the **parameter** at fixed x, with its extension to y determined by the equation. In particular `∂_λω=ω/[2(x−λ)]` and `∂_λ²ω=3ω/[4(x−λ)²]`. An exact rational differential certificate is

\[
\boxed{\ L\omega=d_x(f/y),\qquad f=\frac{x(x-1)}{2(x-\lambda)}\ }.
\]

Indeed, dividing both sides by ω reduces the equality to

\[
\lambda(1-\lambda)\frac{3}{4(x-\lambda)^2}
 +(1-2\lambda)\frac1{2(x-\lambda)}-\frac14
 =\partial_x f-\frac{f\,\partial_xP}{2P}
 =\frac{-x^2+2(1-\lambda)x+\lambda}{4(x-\lambda)^2}.
\]

The rational differential identity itself remains valid in characteristic different from 2. **On the stated characteristic-zero base**, it proves the Picard–Fuchs equation for the relative algebraic de Rham class of ω; after base change to C it also gives the equation for local analytic periods. This uses a parameter derivative and does not identify the manuscript's `Θ_δ`, a derivation on one elliptic fibre, with `∂_λ`.

**Accepted review correction — characteristic-p scope.** Rational exactness alone does not justify the corresponding conclusion about global algebraic de Rham classes in positive characteristic. For example, on the smooth curve `y²=x³−x` in characteristic 3, differentiating the equation gives `dy=dx/y` as rational differentials, although the nonzero regular form `dx/y` has a nonzero global de Rham class: global regular one-forms inject into degree-one de Rham cohomology for a smooth proper curve, and a rational primitive is not a global regular function. Accordingly, no characteristic-p global de Rham assertion is inferred here merely from the displayed rational certificate; the polynomial and Cartier arguments below are separate calculations.

For an odd prime p, set `m=(p−1)/2` and

\[
H_p(\lambda)=\sum_{k=0}^{m}\binom{m}{k}^{2}\lambda^k\pmod p.
\]

There is an all-prime coefficient proof that **`LH_p=0` modulo p**. With `a_j=binom(m,j)²` and `a_{m+1}=0`, the coefficient of `λ^j` in `LH_p` is

\[
(j+1)^2a_{j+1}-(j+\tfrac12)^2a_j.
\]

The integer binomial recurrence gives `(j+1)²a_{j+1}=(m−j)²a_j`; since `m≡−1/2 (mod p)`, the difference vanishes, including the top coefficient `j=m`. Moreover an integer coefficient identity, before reduction, is

\[
[x^{p-1}]P^m=[x^m](x-1)^m(x-\lambda)^m
 =(-1)^m\sum_{k=0}^{m}\binom{m}{k}^{2}\lambda^k.
\]

This is the precise sign connecting the usual Hasse polynomial to the displayed cubic. With the standard Cartier normalization, on a smooth specialized fibre over a perfect characteristic-p field the same coefficient gives

\[
C(dx/y)=\bigl((-1)^mH_p(\lambda)\bigr)^{1/p}\,dx/y.
\]

To see it, write `dx/y=y^(−p)P^m dx` and use the coefficient-selection rule for Cartier on rational differentials: only terms of exponent `p−1 mod p` survive. Since `deg P^m=3m<2p−1`, only `x^(p−1)` contributes. This last formula is stated over a perfect field; over the parameter function field one must retain the relative Frobenius twist instead of silently adjoining a pth root. The Cartier convention is ordinary background (compare Katz 1972, §2.1); the coefficient calculation is written out here.

| p | H_p(λ), with coefficients reduced modulo p | `[x^(p−1)]P^m` |
|---|---|---|
| 3 | `1+λ` | `−H₃` |
| 5 | `1+4λ+λ²` | `H₅` |
| 7 | `1+2λ+2λ²+λ³` | `−H₇` |
| 11 | `1+3λ+λ²+λ³+3λ⁴+λ⁵` | `−H₁₁` |

**Reproducible check:** `records/legendre_s20_certificate.py` (SymPy 1.14.0) and `records/legendre_s20_certificate.json` record zero rational residual for the exact differential identity, the exact integer coefficient identity, and `4LH_p=0` modulo each of 3,5,7,11. Multiplication by 4 is harmless for these primes. The recurrence proves the polynomial assertion for every odd prime; the finite computations are checks, not its only evidence. The parent proposed the rational identity; this agent independently verified and extended the calculation.

**Limit:** one polynomial solution of an order-two equation does not establish zero p-curvature. Neither the equation, the Hasse polynomial, nor this Cartier calculation is written in the supplied scans. They make a future comparison with cotes 93 and 159 concrete without claiming that Grothendieck made the identification here.

## Search record and result-register relationships

Actual searches covered all supplied frozen page TeX, the full Hua modernization, and relevant supplied context. Search terms included `Gauss`, `Manin`, `Cartier`, `cristal/crystal`, `courbure/curvature`, `connexion/connection`, `uniformis/uniformiz`, `p-adique`, `Frobenius`, `de Rham`, `Picard`, `Schwarz`, `S20`, `MPL_93`, `formal deformation`, and elliptic/deformation combinations. There were **zero literal S20-term hits in the frozen pages and in Hua's entire modernized file** under the combined pattern used; the latter nevertheless has the semantically relevant “Approche transcendante” sections. Absence conclusions above also use the read mathematical objects, not keyword search alone. In other context the hits were the README planning guess, register headings, and `SECTIONS_STATE.md` catalogue descriptions; occurrences of “Cartier divisor” in cote149 notes concern divisors, not the Cartier operation.

The present evidence **adds** precise local source support for Hua's `64-legendre-pinning-moduli`, **differs** from several modernization conventions, and **contradicts** the specific mathematical slips RC05, RC06, RC08 and RC09. It does not revise the status of **MPL_93 P09/E14/E16/C29/C35**, **LM4 D.12**, **EXIT_TOWER E.24**, **LM4_SUCCESSOR B.38**, **LM6 A.22**, or **LM7_PUSH E.3**. These latter entries are contextual questions, not results used as premises in this comparison. Mathematical validation events are recorded separately; simply reading a register did not count as a proof check.

## Primary bibliography and limits of external verification

- Antieau, B., & Meier, L. (2020). *The Brauer group of the moduli stack of elliptic curves*. Algebra & Number Theory, 14, 2295–2333. [Primary author preprint, arXiv:1608.00851v3](https://arxiv.org/pdf/1608.00851). Directly read §4, especially Definition 4.4, Proposition 4.5, Corollary 4.6, and Lemma 4.7, pp14–16 of this PDF. Used only for the presentation and equivariance comparison in RC03, not for a novelty claim about the exact pinning.
- Katz, N. M. (1972). *Algebraic solutions of differential equations (p-curvature and the Hodge filtration)*. Inventiones Mathematicae, 18, 1–118. [Author-hosted primary scan](https://web.math.princeton.edu/~nmk/old/algsoln.pdf). The web reader's general PDF extraction exposes only its cover; indexed text supplied the introduction and §§2.0.2.2, 2.1.1, 2.3.1.1 (printed pp17 and21). These were sufficient to check the precise comparison framework stated in RC01. No claim is made here to have re-proved the article's theorems or checked its full text.

Research actor: GPT-6 Astra Pro, effort setting not exposed to this agent, child task `/root/research_connections`. These notes are independent research comparisons, not a second diplomatic pass.
