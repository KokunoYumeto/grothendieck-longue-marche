# Research register on the reused typescripts

## Scope, evidence, and context status

These notes were prepared only after the primary transcriber froze the transcription and opened the context. They use the frozen page fragments, not scans or crops; they do not alter or adjudicate any frozen reading. Every mathematical counterexample below is an editorial calculation, not a claim that the author noticed the problem, and none is claimed to be new.

The sources are reused typescripts, including numbered Bourbaki drafts and minutes. Their mathematical assertions, editorial decisions, and jokes must not automatically be attributed to the author of the handwritten L-function notes. The supplied context README calls all earlier run products unreviewed claims unless separately marked reviewed; that status is retained here.

### Context-search key

In the notes below, **CT** means the supplied file MPL_16+47+54+44_transcription.tex and **CN** means MPL_16+47+54+44_notes.md. The following searches were run against CT and CN; a topical match is distinguished from a matching assertion.

| Key | Terms searched | Actual relevant witnesses and limits |
| --- | --- | --- |
| H | Haar, ultrafiltre, mesures invariantes | No direct match in CT; no earlier Haar construction was located. |
| D | injective, injective hull, K/A, anneau principal, dualité | CT cote 16, scans 037 and 039, treats injective hulls and injective sheaves; CN R9–R10 compares Matlis theory. This is related machinery, not the same finite-length PID argument. |
| F | Fitting, Filting, déterminantiel, annulateur | CT 16/052, §2 nos. 1–2; CN R14–R15. No direct prior version of the examples or relative-lattice formulas in scans 032–034 was located. |
| T | différente, codifférente, conducteur, trace | CT 16/052, §2 nos. 2–5, and 16/054–056; CN R14–R16. These discuss trace/Kähler comparison and étaleness, not the present complete list of order exercises. |
| S | socle, primaire, irréductible | No direct previous socle criterion of scan 022 was located; occurrences in CT 16/019–021 and 54/004 concern different objects. |
| V | puissance symbolique, pseudo-inversible, degré, déterminantiel | No direct matching symbolic-degree or pseudo-invertibility assertion was located in CT. |
| P | plat, platitude, annulateur, nilpotent | CT 54/004 and 54/006 has a cancelled/reworked flatness and flattening argument; 16/056 concerns étale flatness. Neither states the exact exterior-power quotient criterion of scan 032. |
| M | monogène, discriminant, polynôme | CT 16/052 has the “homogènes” monogeneity lemma; CT 16/054 has the nonzero-discriminant-polynomial argument; CN R6–R7 raises the finite-field obstruction. |
| B | Tribu, 57, 62, 63, 397, 398, 392 | CT 44/007 explicitly cites La Tribu n°57; CT 16/052–056 belongs to Tribu n°65. No identity of authorship or exact date follows from the numbering alone. |

### Results-register connections

The supplied RESULTS_STATE has no directly matching settled result or open mathematical item for these Haar, order, PID, or Fitting exercises. In particular, none advances LM7 E.23 or modifies the refereed modular-descent claim LM7_PUSH D.44. The relevant register entries are the provenance lead **MPL_15_195-228+18_002-017 R01** and the title/pagination lead **MPL_15_195-228+18_002-017 §136**; the discussion below adds another concrete instance of their source-separation issue. Entries **WG2 §2.4 #3** and **WG2 §6. #9** receive only a negative scope result: these reused algebra sheets do not establish a construction of motives from Lefschetz correspondence rings.

## Haar construction

### RT01 — Existence is developed here; uniqueness and the ending are elsewhere

**Witness:** 60/010 lines 12–30; 60/008, 006, 004. **Kind:** unproved claim / incomplete supplied proof. **Context:** H, no direct match; bears on the provenance register entry R01.

The theorem states “il existe une mesure de Haar” and uniqueness “à un facteur constant près,” but the typescript explicitly sends uniqueness to Chap. VII and the final surviving sentence on scan 004 stops during the invariance argument. The internal printed sequence is read mathematically as 010→008→006→004, irrespective of the required archival transcription order. A reconstructed proof must use the locally compact-group setting, positivity and compact support, the uniform-continuity estimate (viii), and the normalization \(I(f_0)=1\); this excerpt should not be described as containing the entire proof of both existence and uniqueness.

### RT02 — The final “et” gives a false zero criterion

**Witness:** 60/010 line 37. **Kind:** own idea, counterexample to the literal typed statement. **Context:** H, no direct match.

The phrase “que si \(\mu=0\) et \(f=0\)” is false: on the one-point group, \(\mu=0\) and \(f(e)=1\) give \(\gamma(\mu)f=0\) without both factors vanishing. For nonnegative finitely supported \(\mu\) and nonnegative \(f\), the elementary criterion uses “or,” because any positive atom of a nonzero \(\mu\) translates a positive value of a nonzero \(f\). **Confidence: high**, by this direct evaluation; the frozen conjunction remains unchanged.

### RT03 — A zero-input case is omitted from the nonemptiness proof

**Witness:** 60/008 line 9. **Kind:** own idea / proof-gap check. **Context:** H, no direct match.

The definition of \(A(f,g)\) requires \(\mu\ne0\), whereas its proposed witness \((M/m)\sum\varepsilon_{s_i}\) vanishes when \(f=0\). The nonemptiness claim remains true in that case, since any positive atom works, but the written witness does not cover it. **Confidence: high**, by substituting \(f=0\); this is a missing case in the proof rather than a counterexample to the claim.

### RT04 — The ultrafilter passage needs simultaneous additivity, not a choice for each function

**Witness:** 60/006, inequality (viii); 60/004 lines 24–28. **Kind:** unpursued implication. **Context:** H, no direct match.

The normalized quantities \(I_g(f)=(f:g)/(f_0:g)\) are bounded for each fixed positive \(f\), and one ultrafilter shrinking the support of \(g\) is used for all \(f\). Estimate (viii), divided by the same denominator and passed to that ultrafilter, supplies the reverse inequality to subadditivity. This identifies the substantive proof obligation behind the terse extension to a positive linear form; independent subsequence choices for different \(f\) would not supply that argument.

## PID duality and the two rédaction strategies

### RT05 — Noncanonical self-duality versus canonical biduality

**Witness:** 60/016, Proposition 1 and its proof. **Kind:** unpursued implication. **Context:** D, related but different from CT 16/037 and 039.

The phrase “non canoniquement en général” concerns \(E^*\simeq E\), whereas the evaluation map \(i_E:E\to E^{**}\) is the canonical isomorphism. For the stated nonfield PID \(A\), finite length reduces the proof to \(A/tA\), whose dual is \(t^{-1}A/A\); the cyclic calculation therefore supports both assertions without choosing a functorial self-duality. The finite-length and PID hypotheses should accompany any reuse of this argument.

### RT06 — Length-counting supplies exactness

**Witness:** 60/012, Proposition 2. **Kind:** unproved claim with a supplied proof sketch. **Context:** D; adds an elementary finite-length route beside CT 16/039.

“Comptant les longueurs” uses the equality of lengths proved on scan 016, so that the left-exact dual sequence acquires a surjective last map. For the stated nonfield PID and finite-length modules this establishes exactness without the injective-module machinery the contre-rédaction deliberately avoids. The example \(A=\mathbb Z\), \(K/A=\mathbb Q/\mathbb Z\), is compatible with the injective/divisible comparison (The Stacks Project Authors, n.d.-i), without changing the chosen proof route.

### RT07 — The injective route and its counter-rédaction are different source texts

**Witness:** 60/026, Definition 1 and Proposition 1; 60/016, bracketed preface. **Kind:** unpursued implication / source relation. **Context:** D and B; bears on register R01.

Rédaction 397 begins with injective modules and the extension characterization, while rédaction 398 says “On se refuse à parler de modules injectifs” and restricts to finite length. The latter is an alternative exposition of the same elementary duality topic, not evidence that injectivity was disproved or withdrawn. Scan 026 ends during the proof's decomposition of an exact sequence, so the omitted diagram chase should remain an uncompleted proof obligation in this excerpt.

## Heights, symbolic degree, and normalization

### RT08 — The height-one reduction uses the normal base

**Witness:** 60/030, §5 exercise 1(a). **Kind:** unproved claim. **Context:** V, no direct matching assertion.

The instruction “Montrer que” concerns finite intermediate domains \(A\subset E\subset F\subset B\) over a noetherian normal domain \(A\). A proof can use integrality, incomparability, and going down from the normal base to identify the relevant primes with height-one primes over \(A\), together with finiteness of fibers. This should not be exported as an unrestricted height-preservation theorem for arbitrary integral extensions with a nonnormal base.

### RT09 — Symbolic-power depth is not primary length

**Witness:** 60/030 line 9; compare 60/024 exercise 2(d). **Kind:** own idea, counterexample. **Context:** V, no direct match; the nearest Fitting material is CT 16/052.

The definition uses the “plus petit entier” \(m\) with \(\mathfrak P^{(m)}\subset\mathfrak Q\), which need not equal \(\ell(F_{\mathfrak P}/\mathfrak QF_{\mathfrak P})\) unless the relevant local ring has stronger hypotheses such as being a DVR. Take \(A=k[[t^2]]\), \(B=k[[t]]\), \(C=k[[t^2,t^3]]\), \({\rm char}(k)\ne2\), \(\mathfrak m=(t^2,t^3)\), and \(\mathfrak Q=t^4C\): here \(\mathfrak m^{(3)}\subset\mathfrak Q\) but \(\mathfrak m^{(2)}\not\subset\mathfrak Q\), while \(C/\mathfrak Q\) has basis \(1,t^2,t^3,t^5\) over \(k\) and length 4. **Confidence: high**, by the explicit semigroup calculation; modern cycle multiplicities use localized length, not this least-power invariant (The Stacks Project Authors, n.d.-d).

### RT10 — The printed degree criterion rejects a principal ideal

**Witness:** 60/030 line 11, exercise 1(b). **Kind:** own idea, counterexample to the literal criterion. **Context:** V, no direct match.

For the same cusp example, the principal ideal \(\mathfrak a=t^4C\) is invertible, but the printed \(\deg_C(\mathfrak a)\) is 3 and the normalization expression is 4, since \(\mathfrak aB=t^4B\). Thus the stated equivalence with pseudo-invertibility fails when its preceding degree definition is read literally. **Confidence: high**, because both sides have been calculated; replacing the degree by a localized-length invariant is a research repair, not a transcription correction.

### RT11 — The suggested choice of generator has a second independent gap

**Witness:** 60/030 line 11, last parenthetical proof instruction. **Kind:** own idea, counterexample to an intermediate inference. **Context:** V, no direct match.

The implication from \(y\notin C\cap(\mathfrak a\mathfrak m_iB)\) to \(yB=\mathfrak aB\) fails even in the cusp above: take \(\mathfrak a=\mathfrak m=(t^2,t^3)\) and \(y=t^3\). Then \(\mathfrak a\mathfrak mB=t^4B\), so the prescribed avoidance holds, but \(yB=t^3B\ne t^2B=\mathfrak aB\). **Confidence: high**, by these principal ideals in the normalization; a correct generator-selection argument needs a stronger condition.

### RT12 — Additivity for a pseudo-invertible factor is a local length statement

**Witness:** 60/024 exercise 2(a). **Kind:** unproved claim. **Context:** V and F; CT 16/052 supplies only related Fitting machinery.

For “\(\mathfrak a\) soit pseudo-inversible,” localization at each height-one prime of \(A\) makes \(\mathfrak a\) principal in the relevant semilocal order. Multiplication by a generator then identifies the quotient used to add the two lengths in \(\chi(\mathfrak a\mathfrak b,C)=\chi(\mathfrak a,C)+\chi(\mathfrak b,C)\). This route concerns lengths and does not validate the least-symbolic-power definition criticized in RT09.

### RT13 — Pseudo-comaximal additivity is a localized exact sequence

**Witness:** 60/024, exercise 2(b). **Kind:** unproved claim. **Context:** V, no direct match.

The “pseudo-étrangers” condition makes the two ideals comaximal after each height-one localization. There product equals intersection, and the usual short exact sequence gives the asserted additivity of \(\chi\). A proof must keep the codimension-one convention explicit rather than treating pseudo-comaximality as global comaximality.

### RT14 — The degree coefficient inherits the least-power defect

**Witness:** 60/024, exercise 2(d), height-one case. **Kind:** own idea / counterexample. **Context:** V, no direct match.

With the degree defined on scan 030, exercise 2(d) gives coefficient 3 for the cusp module \(C/t^4C\) of RT09, whereas its \(A\)-length is 4. Thus the height-one coefficient formula inherits the defect in the least-symbolic-power definition. **Confidence: high**, by the explicit basis in RT09; the different colength comparison in 2(e) is treated separately in RT49.

## Trace duals, differents, socles, and orders

### RT15 — Generic separability must be recovered before using the trace dual

**Witness:** 60/030 exercise 1 hypotheses; 60/024 exercise 3. **Kind:** reading question / scope condition. **Context:** T; adds explicit order exercises to CT 16/052 and CN R16, both earlier leads.

The displayed hypotheses of exercise 1 say only that \(L/K\) has degree \(n\), while the subsequent use of \(C^*\) as a trace-dual lattice requires a nondegenerate trace pairing. In a purely inseparable extension \(k((t))/k((t^p))\), the trace is zero and the trace complement is the whole field, not a finite lattice. The missing surrounding §5 text may supply separability; the modern comparison expressly assumes a finite generically étale algebra (The Stacks Project Authors, n.d.-e).

### RT16 — The conductor identity is an order-theoretic duality claim

**Witness:** 60/024 exercise 3(a). **Kind:** unproved claim. **Context:** T, related to CT 16/052 but not stated there.

The assertion “égal à \(B^*:C^*\)” identifies the conductor through trace-dual lattices, and the localized product formula uses the principal-ideal property of the semilocal normalization. Its proof needs lattice biduality and the precise ambient-field meaning of the colon operation. This adds a conductor calculation to the earlier context's proposed trace different; it does not identify the Kähler and trace differents without a comparison theorem.

### RT17 — Different containment follows the conductor comparison

**Witness:** 60/024, exercise 3(b). **Kind:** unproved claim. **Context:** T, related to CT 16/052 nos. 2–4.

The containment \(\mathfrak D_{C/A}\subset\mathfrak f_{C/B}\cap\mathfrak D_{B/A}\) is to be derived from the conductor formula and reversed inclusions under trace duality. Its proof needs the finite separable-order setting of RT15. It should not be derived from the defective symbolic-degree definition.

### RT18 — The multiplier-ring criterion has a Gorenstein interpretation

**Witness:** 60/024 exercise 3(d); 60/022 exercise 3(e). **Kind:** unpursued implication. **Context:** T; no direct previous multiplier-ring criterion was found.

The condition that \(C^*\) be invertible, together with the implication \(\mathfrak a:\mathfrak a=C\Rightarrow\mathfrak a\) invertible, is the modern Gorenstein-order condition after height-one localization. For orders in number fields, Marseglia (2019, §2) explicitly gives this equivalence and distinguishes it from the stronger Bass condition on every overorder. The note should preserve that localization and order scope, rather than asserting a theorem about arbitrary rings or identifying the present typescript's author or date from modern terminology.

### RT19 — Irreducibility does not imply a globally simple socle quotient

**Witness:** 60/022 exercise 4(a). **Kind:** own idea, counterexample to the unrestricted statement. **Context:** S, no direct matching criterion.

Take \(C=k[x,y]\) and \(\mathfrak q=\mathfrak p=(x)\): fractional ideal quotients give \(\mathfrak q:\mathfrak q=C\) and \(\mathfrak q:\mathfrak p=C\), and the prime ideal \(\mathfrak q\) is irreducible, but \((\mathfrak q:\mathfrak p)/\mathfrak q=k[y]\) is not a simple \(C\)-module. The familiar socle criterion applies after localization at \(\mathfrak p\), or when the primary support is a maximal ideal and the quotient is artinian local. **Confidence: high**, by this explicit domain example; the written “se ramener” needs that localization step.

### RT20 — The socle coefficient ring is a literal reading question

**Witness:** 60/022, exercise 4(a), parenthetical proof hint. **Kind:** reading question. **Context:** S; no direct earlier wording match.

The parenthesis calls the socle an “\((A/\mathfrak p)\)-module” although its current ring is C. The natural comparison would use \(C/\mathfrak p\), but that is a proposed reading/printing correction in these notes only. The frozen letter is not altered.

### RT21 — The colon equality in the semilocal proof also needs localization

**Witness:** 60/022 exercise 4(b), last parenthetical clause. **Kind:** own idea, counterexample to a displayed inference. **Context:** S and T; no matching earlier equality.

Even if “de \(C\)” is read as a proposed “de \(\pi C\),” the global equality \(\pi C:\mathfrak m_i=\mathfrak q_i:\mathfrak m_i\) need not hold in a semilocal ring. For \(A=\mathbb Z_{(5)}\), \(C=A[i]\), \(\pi=5\), \(\mathfrak m_1=(2+i)\), and \(\mathfrak m_2=(2-i)\), one has \(\pi C=\mathfrak m_1\mathfrak m_2\), \(\mathfrak q_i=\mathfrak m_i\), \((\pi C:\mathfrak m_i)=\mathfrak m_j\), but \((\mathfrak q_i:\mathfrak m_i)=C\). **Confidence: high**; the intended comparison becomes valid after localizing at \(\mathfrak m_i\), where the other factor is a unit.

### RT22 — Irreducible primary fibers test a Gorenstein local order

**Witness:** 60/022 exercise 4(b), main assertion. **Kind:** unpursued implication / unproved claim. **Context:** T and S.

The main criterion links invertibility of the trace dual to simplicity of the socle of the artinian local fibers \(C_{\mathfrak m_i}/\pi C_{\mathfrak m_i}\). This is the one-dimensional Cohen–Macaulay type-one/Gorenstein mechanism, rather than a general statement that every primary ideal has a simple socle. The literal proof issues in RT20–RT21 and RT63 do not by themselves refute that localized main statement.

### RT23 — The two quotient modules characterize principal trace duals locally

**Witness:** 60/022 exercise 4(c). **Kind:** unproved claim. **Context:** T; no direct earlier quotient-module comparison.

The assertion compares \(C^*/C\) and \(C/\mathfrak D_{C/A}\) after height-one localization. If \(C^*=uC\), multiplication by \(u^{-1}\) gives the required isomorphism, since \(\mathfrak D_{C/A}=u^{-1}C\); the converse requires the stated minimal-generator argument at every maximal ideal. Abstract equality of lengths alone would be insufficient for this converse.

### RT24 — Invertibility of primary ideals detects normalization in codimension one

**Witness:** 60/022 exercise 4(d). **Kind:** unproved claim. **Context:** V and T, no directly matching statement.

The condition \(C_{\mathfrak p}=B_{\mathfrak p}\) for height-one base primes asks for normality at the relevant one-dimensional localizations. The proposed test by primary ideals should be reduced there, where principality of the maximal ideal characterizes a DVR; the hint involving \(\mathfrak p^2\) needs the same localized setting. It does not claim that the whole higher-dimensional order \(C\) is normal.

### RT25 — The quadratic boundary is a statement about every suborder

**Witness:** 60/022 exercise 5, continued on 60/020. **Kind:** unproved claim / unpursued implication. **Context:** T; no directly matching earlier degree bound.

The claim “\([K:Q]\le2\)” quantifies over every full suborder \(C\subset B\), not merely over the maximal order \(B\). The proposed test \(C=\mathbb Z+pB\) compares the one-dimensional quotient \(C/pB\) with the \((n-1)\)-dimensional quotient \(B/C\), yielding the obstruction for \(n>2\); the degree-one case should be separated before the proof's concluding “dimension 2.” Quadratic orders are consistent with the Bass/Gorenstein comparison in Marseglia (2019, §2), but that later terminology does not date the typescript.

### RT26 — The different criterion concerns the normalized unramified branch

**Witness:** 60/020 exercise 6(a)–(c). **Kind:** unproved claim. **Context:** T; adds a branch/conductor formulation to CT 16/054–056.

The three conditions compare nonvanishing of the different at \(\mathfrak P\), a reduced separable local component of the special fiber, and a unique normalized branch with unchanged residue field. A proof must keep the base DVR, finite separable extension, completion step, and the distinction between an order and its normalization. This is related to the earlier context's finite étale/unramified criteria, but is not an unrestricted inference from a nonzero different in a nonflat situation.

### RT27 — Openness of a power basis needs the missing topology

**Witness:** 60/020 exercise 7(a). **Kind:** unproved claim / missing scope. **Context:** M; CT 16/054 also invokes a discriminant polynomial.

“Pour tout \(y\) suffisamment voisin de \(x\)” is a continuity assertion about the determinant of the power-basis matrix. The referenced proposition number is blank, so the topology and its hypotheses must be recovered before giving a complete proof. In a DVR setting, congruence modulo a sufficiently small ideal preserves a unit determinant, but that is a qualified comparison, not text to supply in the blank reference.

### RT28 — The completely split finite-field obstruction is explicit

**Witness:** 60/020, exercise 7(c). **Kind:** unproved claim / context addition. **Context:** M; CT 16/052 and 054, CN R6–R7.

The exact split-fiber condition is “\(n\le\operatorname{Card}(\bar K)\).” In \(B/\mathfrak pB\simeq\bar K^n\), a generator must have distinct coordinates, and such choices lift to a power basis in the stated local setting by Nakayama. This adds the cardinality restriction absent from the preserved earlier fragment, while leaving open whether unavailable antecedent text supplied an infinitude hypothesis.

## Divisor-valued Euler characteristics

### RT29 — Additivity is valuation by valuation

**Witness:** 60/028, Proposition 10 and corollary. **Kind:** unpursued implication. **Context:** V and F, no exact earlier statement.

The proof reduces \(\chi\) to the lengths \(\ell_{\mathfrak p}\), so exact-sequence additivity and the alternating-sum corollary are codimension-one consequences of ordinary length additivity. “Pseudo-nul” means invisibility at those localizations, not that the torsion module itself is zero. This distinction is useful when connecting the sheet to divisor or Fitting computations elsewhere in the reused draft.

### RT30 — Proposition 11 is only a beginning in the supplied selection

**Witness:** 60/028, Proposition 11. **Kind:** unproved claim / incomplete witness. **Context:** V, no directly matching universal-property statement.

The text introduces an additive function \(\varphi\) on finite torsion modules and displays only condition 1 before the selected leaf ends. An expected universal property of the divisor group cannot be quoted as the proposition's complete statement without its remaining hypotheses and conclusion. In particular, additivity alone does not force a function to vanish on pseudo-null modules.

## Fitting ideals, exterior powers, and flatness

### RT31 — The missing start of exercise 22 matters

**Witness:** 60/032, exercise 22(c)–(e). **Kind:** reading question / scope condition. **Context:** F and P; related to CT 16/052 and 54/004–006.

The sheet begins with part (c), while the hypotheses and definitions in 22(a)–(b) are absent from the selected package. The splitting and freeness assertions are naturally local-ring statements; without locality, a nontrivial invertible ideal over a Dedekind domain can be free at a chosen prime and modulo that prime while failing to be globally free. This is a reason to recover the preceding draft page, not a reason to accuse the omitted hypothesis of being absent in the original exercise.

### RT32 — The invariant-factor equivalence uses cyclic splitting

**Witness:** 60/032, exercise 22(d). **Kind:** unproved claim. **Context:** F; adds an explicit local diagonalization exercise to CT 16/052.

The proposed equivalence joins principal Fitting ideals, principal annihilators of exterior powers, and a divisibility-ordered cyclic decomposition. Splitting the cyclic summand of 22(c), as isolated in RT56, gives the indicated induction. A complete proof must retain the missing local hypotheses and distinguish the product formula for Fitting ideals from individual exterior annihilators.

### RT33 — The freeness test can be proved over a local domain

**Witness:** 60/032, exercise 22(e). **Kind:** unproved claim with an editorial proof route. **Context:** P; differs from the flattening assertions in CT 54/004–006.

Assuming the omitted hypotheses make \(A\) a local domain and \(E\) finite, a basis of \(E/\mathfrak pE\) lifts to generators of \(E\) by Nakayama. Their relation module inside \(A^r\) vanishes after localization at \(\mathfrak p\), because \(E_{\mathfrak p}\) is free of the same rank; since \(A\) is a domain, it was already zero. Thus the conclusion follows in that setting, while RT31 explains why a global version needs qualification.

### RT34 — The last divisibility comparison invokes an undefined lambda

**Witness:** 60/032, exercise 22(d). **Kind:** reading question. **Context:** F; no direct earlier wording match.

The divisibility range \(0\le h\le r-1\) invokes \(\lambda_r\) although the displayed factors are indexed through \(\lambda_{r-1}\). The conventional endpoint would be \(r-2\) for comparisons between successive listed factors. This is an index-reading/printing question, independent of the proof of the invariant-factor equivalence.

### RT35 — The exterior-annihilator quotient is actually finite locally free

**Witness:** 60/032, exercise 23, first claim. **Kind:** own idea / stronger consequence. **Context:** P and F; adds a precise finite-module criterion to CT 54/004–006.

With the interpretation of \(r\) in RT64, localization at any prime shows \(\operatorname{Ann}(\bigwedge^rE)=\operatorname{Fitt}_{r-1}(E)\) and \(\operatorname{Fitt}_r(E)=A\): when the local generator number is \(r\), both ideals are the relation-coefficient ideal, and when it is smaller both are the unit ideal. Consequently, for \(\mathfrak a\supset\operatorname{Ann}(\bigwedge^rE)\), the quotient \(E/\mathfrak aE\) is finite locally free of rank \(r\), by Fitting base change and the rank criterion (The Stacks Project Authors, n.d.-g, n.d.-f, n.d.-a). **Confidence: high**, by this local presentation argument; this proves more than the word “plat” on the sheet and does not require assuming finite presentation of \(E\) in advance.

### RT36 — “Radical” must be distinguished from nilradical

**Witness:** 60/032, exercise 23, last sentence. **Kind:** reading question / own test case. **Context:** P; CT 54/004–006 explicitly discusses nilpotents, which is a different issue.

The stated corollary is compatible with the Jacobson radical: constant fiber dimension at all maximal ideals places the top-exterior annihilator in their intersection, so RT35 applies. If “radical de \(A\)” were instead interpreted as the nilradical, the assertion would fail for \(A=k[t]_{(t)}\) and \(E=A/(t)\): there is only one maximal fiber dimension, but the nilradical is zero and \(E\) is not flat. **Confidence: high** for the counterexample; the note identifies the necessary meaning of a term rather than altering it.

### RT37 — The explicit Fitting example checks directly

**Witness:** 60/034, exercise 10(g). **Kind:** own idea / verification. **Context:** F; adds a fully calculable example to CT 16/052 and CN R14.

For the printed \(\mathfrak q=(X,Y^2,YZ,Z^2)\), the submodule \(N=\mathfrak m/\mathfrak q\) is \((A/\mathfrak m)^2\), with basis the classes of \(Y,Z\), and \(M=A/\mathfrak q\) is cyclic. The standard direct-sum and cyclic-module rules give exactly \(\operatorname{Fitt}_0(M)=\mathfrak q\), \(\operatorname{Fitt}_1(M)=A\), \(\operatorname{Fitt}_0(N)=\mathfrak m^2\), and \(\operatorname{Fitt}_1(N)=\mathfrak m\) (The Stacks Project Authors, n.d.-g). **Confidence: high**, by the displayed annihilation and two-element basis; no correction of this example is indicated.

### RT38 — Relative determinantal divisors require signed valuations

**Witness:** 60/034, exercise 11(a). **Kind:** unproved claim / unpursued implication. **Context:** F and V, no exact earlier formula.

Independence of \(c\) can be checked at every height-one DVR, where multiplying a lattice by \(c\) adds \(v(c)\) to each invariant exponent. The subtraction \((n-k)\operatorname{div}(c)\) cancels exactly that contribution, permitting negative relative exponents when \(N\) is not contained in \(M\). This signed interpretation is needed before using the next part's inequalities.

### RT39 — Monotonicity fails for arbitrary relative lattices

**Witness:** 60/034, exercise 11(b), first assertion. **Kind:** own idea, counterexample. **Context:** F and V, no direct earlier claim.

Let \(A=k[[t]]\), \(V=k((t))\), \(M=A\), \(N=t^{-1}A\), and choose \(c=t\); then \(M/cN=0\), so \(d_0(N,M)=-[t]\) and \(d_1(N,M)=0\). Thus the printed \(d_0\ge d_1\) is false under the displayed hypotheses, which do not require \(N\subset M\). **Confidence: high**, from the defining formula; adding containment would remove this particular obstruction, but is not a permitted transcription change.

### RT40 — The invariant-factor endpoint is undefined

**Witness:** 60/034, exercise 11(b), second inequality. **Kind:** reading question. **Context:** F, no direct earlier wording match.

The range “\(1\le k\le n\)” in \(e_k\le e_{k+1}\) invokes \(e_{n+1}\), although only \(e_1,\ldots,e_n\) are defined by the stated formula. The conventional comparison would end at \(n-1\); this is a proposed index repair only. It is separate from the genuine signed-valuation counterexample to the preceding inequality.

### RT41 — The zeroth relative divisor is the lattice characteristic

**Witness:** 60/034, exercise 11(c). **Kind:** unproved claim. **Context:** V and F; no exact matching earlier formula.

The identity \(d_0(N,M)=\chi(M,N)\) compares the sum of signed local invariant exponents with the local length-difference definition of \(\chi\). At a height-one DVR, choose a common sublattice and subtract the two colengths, which yields precisely that sum. This remains compatible with negative coefficients and does not require the false monotonicity tested in RT39.

### RT42 — The binomial coefficient counts invariant exponents

**Witness:** 60/034, exercise 12(a). **Kind:** unproved claim with an editorial proof route. **Context:** F and V, no directly matching earlier exterior-divisor formula.

At each height-one DVR, choose bases diagonalizing \(N\subset M\); in the \(k\)-th exterior power every invariant exponent occurs in exactly \(\binom{r-1}{k-1}\) of the \(k\)-fold sums. Summing these valuations proves the displayed divisor-length identity for \(1\le k\le r\), while localization also explains “pseudo-injectif.” The proof must retain the finite torsion-free equal-rank hypotheses and should state conventions separately for exterior powers outside that range.

### RT43 — Pseudo-null exterior torsion can be nonzero

**Witness:** 60/034, exercise 12(b). **Kind:** own idea / example. **Context:** F and V, no directly matching example.

For \(A=k[x,y]\) and the rank-one torsion-free ideal \(I=(x,y)\), a presentation with relation \((-y,x)\) gives \(\bigwedge^2 I\simeq A/(x,y)\). Thus exterior torsion need not vanish, although it vanishes at every height-one localization, exactly as “pseudo-nul” predicts. **Confidence: high**, by this explicit presentation; adjoining a free summand gives a rank-two example where \(\bigwedge^2(I\oplus A)\to\bigwedge^2(A^2)\) has this nonzero pseudo-null kernel.

## Historical and title-sheet cautions

### RT44 — The formal-group decision is an editorial withdrawal in another text

**Witness:** 60/014, discussion of rédactions 385–386. **Kind:** withdrawn in the same typed item / source caution. **Context:** B; relates to register R01 and the scope questions WG2 §2.4 #3 and WG2 §6. #9.

“Bourbaki vide toute la rédaction” rejects an exposition for lacking the desired analytic/Lie connection and substantial characteristic-\(p\) formal-group results, while retaining a proposed characteristic-zero section for later use. This is an editorial decision about rédaction 386, not a retraction of a theorem in the handwritten L-function argument. Its mention of formal groups does not establish a link to the motivic programme merely because the paper was reused.

### RT45 — Calendar entries date plans, not the handwriting

**Witness:** 60/014 and 018. **Kind:** reading question / historical scope. **Context:** B; CT 44/007 explicitly refers to Tribu n°57; bears on register R01 and §136.

The pages carry “Décembre 62” and March/June 1963 deadlines, together with internal report number 57 and page numbers 9 and 8. They identify a contemporaneous planning document, but the future dates are not exact composition dates and do not date the later handwriting on reused paper. The context's Tribu-57 reference adds a documentary connection, not an established attribution to a particular individual.

### RT46 — Distinct titles and pagination must remain distinct

**Witness:** 60/010, 012, 014, 016, 018, 020, 022, 024, 026, 028, 030, 032, 034. **Kind:** title/pagination observation. **Context:** B; bears on register §136.

The surviving headings below belong to several independent typed texts, not one 34-page treatise. Their printed page labels and rédaction/report numbers are identifiers rather than explicit total page counts. No explicit total extent is stated on these selected typed title sheets.

| Scan(s) | Title or identifier visible in the frozen text | Pagination caution |
| --- | --- | --- |
| 010; 008, 006, 004 | CHAPITRE VIII; CONSTRUCTION de MESURES INVARIANTES; §1 Construction d'une mesure de Haar; n°357 on the continuation sheets | Continuations have printed 55, 56, 57, encountered in reverse archival order. |
| 016 and 012 | COMPLÉMENTS AU CHAPITRE VII D'ALGÈBRE; DUALITÉ DES MODULES DE LONGUEUR FINIE SUR UN ANNEAU PRINCIPAL; Rédaction n°398; CONTRE-RÉDACTION | Scan012 is printed page 2; this does not itself state a total of two pages. |
| 026 | Same duality title; Rédaction n°397; Modules injectifs | A separate rédaction from n°398. |
| 014 and 018 | n°57; Séminaire BOURBAKI; DÉCISIONS LOCALES DIVERSES | Printed pages 9 and 8; December1962 and March/June1963 planning entries. |
| 020, 022, 024, 030 | n°392 | Printed 6–44, 6–43, 6–42, 6–41; chapter/section pagination, not a stated total. |
| 028 | n°392 | Printed 4–22, separate from the chapter-6 exercise leaves. |
| 032 and 034 | n°392 | Printed 6–40 and 6–36, with intervening printed pages absent from this selected set. |

## Additional separated exercise obligations

### RT47 — The different's own multiplier ring is a separate converse

**Witness:** 60/022, exercise 3(e). **Kind:** unproved claim. **Context:** T; no direct matching criterion in CT 16/052–056.

The criterion \((\mathfrak D_{C/A})_{\mathfrak p}:(\mathfrak D_{C/A})_{\mathfrak p}=C_{\mathfrak p}\) is asserted to be equivalent to invertibility of the trace dual, not merely to follow from it. The forward consequence from an invertible trace dual is straightforward because its inverse different is invertible; the converse requires an additional local-order argument about the inverse of the canonical/trace-dual ideal. The later multiplier characterization in RT18 should not be cited as though it supplies that converse for a ring not already known Gorenstein.

### RT48 — Every normalization ideal is pseudo-invertible, not necessarily globally invertible

**Witness:** 60/030, last sentence. **Kind:** unpursued implication. **Context:** V, no direct earlier assertion.

“Si \(C=B\), tout idéal \(\ne0\) de \(B\) est pseudo-inversible” only tests localizations over height-one primes of \(A\). These are semilocal one-dimensional normal domains, so their ideals are principal, while a nonzero ideal of the higher-dimensional normal ring \(B\) can still fail to be globally invertible. This distinction prevents the final sentence from being read as a claim that every normal noetherian domain is Dedekind or factorial.

### RT49 — Normalization colength is a separate invertibility criterion

**Witness:** 60/024, exercise 2(e). **Kind:** unproved claim. **Context:** V, no direct earlier formulation.

The equality \(\chi(\mathfrak a,C)=\chi(\mathfrak aB,B)\) is intended to characterize pseudo-invertibility by comparing colengths before and after normalization. This is a separate local length statement and is not refuted merely by the defective least-symbolic-power definition. Its converse needs its own semilocal-order proof rather than an appeal to the literal exercise 1(b).

### RT50 — Adoption of the closed-subgroup exposition is an editorial decision

**Witness:** 60/014, discussion of rédaction 384. **Kind:** unproved/editorial programme. **Context:** B; CT 44/007, and register R01.

The adoption of the closed-subgroup-space text is a direction for a future exposition, without the relevant propositions reproduced here. It is evidence about the reused editorial document, not a theorem or conjecture in the handwritten functional-equation argument. Its provenance should therefore remain distinct when indexing research claims.


### RT51 — Biduality gives the orthogonal-submodule correspondence

**Witness:** 60/012, Proposition 3. **Kind:** unproved claim with a supplied proof sketch. **Context:** D; CT 16/037 and 039 supplies related injective machinery, not this lattice correspondence.

The double-orthogonal argument uses canonical biduality together with exactness from Proposition 2. It gives an inclusion-reversing bijection between the submodules of E and its dual, exchanging sums and intersections. This is stronger than the noncanonical existence of an isomorphism \(E\simeq E^*\) and does not require choosing one.

### RT52 — Primary components contribute only at height one

**Witness:** 60/024, exercise 2(c). **Kind:** unproved claim. **Context:** V; no direct matching earlier assertion.

The stated primary-component formula discards contributions supported in higher codimension, rather than adding every primary component indiscriminately. Localizing at a height-one base prime and applying length additivity isolates the components that can survive. A proof must state the relevant primary decomposition and explain why embedded components contribute zero to this divisor-valued invariant.

### RT53 — Vanishing away from height one does not depend on the bad degree

**Witness:** 60/024, exercise 2(d), non-height-one case. **Kind:** unpursued implication. **Context:** V; no matching earlier formulation.

The vanishing of \(\chi(\mathfrak q,C)\) when the primary support does not have height one follows from its codimension-one definition. It is logically independent of the erroneous least-power coefficient in the height-one case of RT14. The whole exercise should therefore not be rejected wholesale on the basis of that one coefficient defect.

### RT54 — Equality after normalization tests the trace-dual lattice

**Witness:** 60/024, exercise 3(c). **Kind:** unproved claim. **Context:** T; CT 16/052 gives related trace/Kähler comparison questions, not this criterion.

The asserted equality after extending the different to \(B_{\mathfrak p}\) is proposed as a criterion for invertibility of \(C^*_{\mathfrak p}\). It needs a local-order proof using the conductor identity and the trace-dual lattice in the separable setting. The preceding containment RT17 supplies one ingredient, but is not by itself the converse.

### RT55 — A primitive element is chosen to avoid the conductor at one branch

**Witness:** 60/020, exercise 7(b). **Kind:** unproved claim. **Context:** M and T; CT 16/052–054 and CN R6–R7 are related but do not state the same branchwise assertion.

Part (b) asks for a primitive element whose generated order agrees with the normalization at a chosen branch with separable residue extension, expressed by avoiding the conductor in that prime. Its proof must combine a residue-field generator, a local power basis and a sufficiently close globally primitive element. This local assertion is distinct from the all-branches-at-once cardinality obstruction of 7(c).

### RT56 — A principal relation ideal produces a cyclic direct summand locally

**Witness:** 60/032, exercise 22(c). **Kind:** unproved claim. **Context:** F; no exact previous splitting statement was found.

In a local ring, write the relation coefficients as \(\alpha b_i\) and express \(\alpha\) as their linear combination, so \(\alpha(1-\sum u_ib_i)=0\). If \(\alpha\ne0\), the parenthesis cannot be a unit, so some \(b_i\) is a unit; this yields a relation \(\alpha y\) with y unimodular, and clearing its coordinate in the other relations gives the required cyclic summand. The zero relation ideal gives a free module, while the missing hypotheses and generator convention of 22(a)–(b) must still be recovered.

### RT57 — Lattices in a subspace need finiteness and saturation checks

**Witness:** 60/034, exercise 11(d). **Kind:** unproved claim. **Context:** V and F; no directly matching earlier subspace formula.

For lattices in a proper subspace W, replacing M by \(M\cap W\) needs finiteness and saturation checks before importing the cited exercises. The text permits additional noetherian normal hypotheses in certain cases, which helps establish those checks locally in codimension one. That permission is a scope qualification, not an explicit complete list of all cases.

### RT58 — The distributions-and-jets question is a separate editorial programme

**Witness:** 60/014, discussion of rédaction 385. **Kind:** self-flagged / editorial question. **Context:** B; the reused discussion at CT 44/007 is related in provenance only.

The instruction to recast finite-support distributions with jets, and to omit the algebraic case, specifies a future treatment rather than reproducing its proofs. The question “pourquoi pas les limites inductives et projectives ??” is an explicit suggestion in that programme. It should be indexed as an editorial question in the typed source, not as an unresolved step in the handwritten L-function derivation.

### RT59 — The crossed-word erratum concerns another publication's terminology

**Witness:** 60/018, Errata. **Kind:** reading question / source observation. **Context:** B; no matching earlier erratum was located.

The “filrtant/filtrant” uncertainty and the proposed “flirtant” correction belong to an editorial joke/erratum in the reused sheet. They do not license modernizing the visible word or replacing the transcription with the expected technical term. Their exact letters and any doubt remain in the diplomatic text.

### RT60 — The homological-algebra publication is explicitly conditional

**Witness:** 60/018, final footnote. **Kind:** self-flagged / editorial expectation. **Context:** B; register R01 concerns reused-text provenance, not fulfillment of this plan.

The phrase “l'éventuelle publication” marks a conditional future intention concerning homological algebra. It gives neither a completed publication nor a proof that all of the listed revisions were carried out. This expectation is distinct from the nearby report assignments and their administrative question marks.

### RT61 — The exterior-class formula is the same codimension-one count

**Witness:** 60/034, exercise 12(b), final display. **Kind:** unpursued implication. **Context:** F and V; CT 47/009 has a different Chern-class heuristic, not this divisor-class proof.

After discarding the pseudo-null exterior torsion, the class formula \(c(\bigwedge^kM)=\binom{r-1}{k-1}c(M)\) follows from the same height-one invariant-exponent count as RT42. This interprets the displayed class at the divisor/first-Chern level and does not infer formulas for all higher Chern classes. The binomial expression requires the stated rank range or separately declared conventions at its endpoints.

### RT62 — The injective-module criterion is an extension property

**Witness:** 60/026, Proposition 1. **Kind:** unproved claim / incomplete supplied proof. **Context:** D; CT 16/037 and 039 concerns related injective objects, while the present draft works with modules.

The equivalence says that exactness of \(\operatorname{Hom}(-,P)\) is the ability to extend a map from every submodule to its ambient module. One direction is the surjectivity in the dual short exact sequence; the reverse follows by factoring an arbitrary exact sequence through its image, as the final three rows begin to do. The proof stops in this selection, so its completion is an explanatory route in these notes, not text supplied to the frozen diagram.

### RT63 — The object whose primary component is meant is unspecified

**Witness:** 60/022, exercise 4(b). **Kind:** reading question. **Context:** S and T; no direct earlier wording match.

The frozen text calls \(\mathfrak q_i\) the primary component “de C,” although a primary decomposition of the unit ideal cannot supply the proper object used in the argument. The natural comparison is a component of \(\pi C\), which is the explicitly conditional interpretation tested in RT21. This proposed correction remains solely in the notes.

### RT64 — The minimum defining r uses a mismatched variable

**Witness:** 60/032, exercise 23, opening. **Kind:** reading question. **Context:** F and P; no matching earlier malformed definition.

The text calls r the least integer k satisfying a condition written with \(\bigwedge^{r+1}E\), so the literal condition does not depend on k. The mathematical analysis in RT35 uses the explicit editorial interpretation \(r=\min\{k\ge0:\bigwedge^{k+1}E=0\}\). Neither frozen index has been changed.
