# Research evidence: Albanese equivalence, cote 14 scans 019–039

Prepared after the transcription freeze. The frozen page files and combined transcription were read only. `context/notes/RESULTS_STATE.md` was read in full before these notes were written. All line numbers below refer to the frozen per-page TeX files, and are approximate locators for the manuscript passage, not reconstructed manuscript line numbers.

Every shortened location “scanNNN” means the file `pages/MPL_14_002-044_14_scanNNN.tex`, cote14; it never means a scan in another cote.

## Provenance and abbreviations used in this record

- **T** = `context/MPL_16+47+54+44_transcription.tex` (earlier, unreviewed transcription).
- **N** = `context/MPL_16+47+54+44_notes.md` (earlier AI research claims, used as leads).
- **R** = `context/notes/RESULTS_STATE.md`.
- Every **WG2** entry below has R status **question or plan item of the war game, round 2, unchecked**; **WG H9** has status **hunch of the war game, Believe, unchecked**.
- **Hua 14-albanese-equivalence-ring** has R status **conjecture (unsearched), reach beyond; intake: new to us, package waiting**.
- Source-relative bibliographic labels are defined at the end. Statements attributed to later papers retain their published scope; neither the earlier notes nor the R register settles the manuscript's general claims.

## Proposed notes, each with its own context comparison

### A01 — Own idea: exact link between the two intersection constructions

**Location:** `pages/MPL_14_002-044_14_scan019.tex`, lines 20–37; scan021, lines 39–49. **Quote:** “des signes différents !!” **Context search:** `positive|positivité|r_\*|Néron`; T, cote44 scans008–009; N, D13. **Delta:** adds a concrete family to the earlier positivity question. **R:** WG2 §2.3 #12; WG H9, with their unchecked statuses.

For the family $z$ on $A\times X$, the diagonal $\delta:A\to A\times A$ gives the exact comparison $\delta^*r_*(p^*z\cdot q^*z)=s_*(z^2)$, by the refined pullback/proper pushforward identity applied to the diagonal square. The manuscript computes the degree of this pullback as $-2d$, with $d=\deg(N_{Y/X}|_{\{0\}\times P})$, and its choices $d=1,-1$ give both signs. This supplies a specific test of cote44 scan009's divisor $D=r_*(p^*z\cdot q^*z)$ and of scan008's warning about primitive decomposition; **confidence high**, because the same correspondence and diagonal pullback explicitly connect the two passages, while the sheets provide no date ordering for the example.

### A02 — Reading question: the displayed projection and cycle types

**Location:** scan019, lines 39–42; scan021, lines 39–49. **Quote:** $p_*(\Theta^2)=-2(0\times0\times P)$. **Context search:** `r_\*|p\^\*|corr.*divis`; T, cote44 scan009; N, D13. **Delta:** adds typing questions to the earlier correspondence formula. **R:** WG2 §2.3 #12, unchecked.

The prose defines $i':A\times Y\to A\times X$, but the marginal arrow in the frozen transcription runs from $A\times X$ to $A\times Y$; likewise $p_*(\Theta^2)$ belongs to cycles on $Y=A\times P$, while the displayed representative retains both $A$-coordinates. A consistent calculation distinguishes $c\in\mathrm{CH}^1(Y)$, its pullback $c'=1_A\times c$, and $p'_*(\Theta_0^2)=-2[0]\in\mathrm{CH}^1(A)$; this explains the types required by A01 without changing the frozen reading. The dimensional ambiguity in the written $c=A\times A\times(a)$ remains recorded as a reading question.

### A03 — Unpursued implication: the definition answers an earlier identification question

**Location:** scan024, lines 8–16; scan025, lines 2–13. **Quote:** “$S_Y(\nu)=0$” and “égal à”. **Context search:** `équivalence d'Albanese|relation d'équivalence|Z.*mathrm.*alb`; T, cote44 scans002 and008; N, D08. **Delta:** adds a definition and proposed ring operations to the earlier unnamed quotient. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

The new text specifies the generators $Z_*(\nu)$ with $\deg\nu=0$ and $S_T(\nu)=0$, thus supplying concrete data absent from cote44 scan008's “une relation d'équivalence que je ne sais pas bien identifier”. Its proposed maps are the quotient homomorphisms $\mathrm{CH}^*(X)\twoheadrightarrow A^*_{\mathrm{alb}}(X)\twoheadrightarrow \mathrm{CH}^*(X)/\mathrm{CH}^*_{\mathrm{alg}}(X)$, obtained from the stated inclusions of relation subgroups. The proofs of the full functorial ring structure still carry the explicit reservation on scan028.

### A04 — Self-flagged reading question: projectivity of the parameter space

**Location:** scan024, lines 8–14; scan029, line2; scan030, line12. **Quote:** “[projectif]”, “Ici il semble …”, and “projectives lisses”. **Context search:** `paramètres|projective|Alb\(S\)`; T, cote44 scans002,008–009; N, D08. **Delta:** adds a stated uncertainty concerning the parameter hypothesis. **R:** WG2 §2.3 #12, unchecked.

The definition retains bracketed projectivity for the parameter $T$, and the margin of Theorem1.4 explicitly questions its use, while the product proof on scan030 again underlines projectivity and smoothness. A reconstruction should track the map $T\to\operatorname{Alb}(T)$ used to factor each family and the Picard-valued map of scan030, with the exact parameter category stated. Cote44's general parameter wording supplies no resolution of this bracketed hypothesis.

### A05 — Reading question: field and rational-point assumptions

**Location:** scan026, lines2–18; scan033, line30; scan036, line2. **Quote:** “$A_Y(k)$ est divisible!” **Context search:** `corps alg clos|corps algébriquement clos|divisible|point marqué`; T, cote44 scans008–009; N, D08–D10. **Delta:** makes explicit a field convention visible in the earlier letter. **R:** WG2 §2.3 #12 and #13, unchecked.

The group-law proof selects points $a,a'$, the later argument uses divisibility of $A_Y(k)$, and the family decomposition chooses $y_0\in Y(k)$, whereas the local definition on scan024 says only “corps $k$”. Cote44 scan008 expressly works over an algebraically closed field, where the surjective isogeny $[n]:A_Y\to A_Y$ is surjective on $k$-points. The new notes should retain this explicit map as the justification for divisibility and record that the supplied pages do not repeat that field convention at the start of §1.

### A06 — Unproved claim: simultaneous choices in the additive construction

**Location:** scan025, lines15–19; scan026, lines2–28. **Quote:** “sous réserve que $Z$ a été choisi”. **Context search:** `Alb\(S\)|application naturelle|famille`; T, cote44 scan002, Theorem1; N, 44:2:1. **Delta:** adds a proposed proof of closure under addition. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

The construction uses $T\times T'$, $\nu\times a'$, $a\times\nu'$, and pulled-back correspondences, whose cross terms vanish because the projected zero-cycles have degree zero. The exact qualification concerns defined intersections at the selected points, especially $Z(a)$ and $Z'(a')$. This is part of the same moving problem later marked “à vérifier”, and the marginal “Lemme d'isog.” remains too uncertain to identify a missing cited result.

### A07 — Self-flagged unproved claim: moving the cycles for pullback

**Location:** scan027, lines4–8; scan028, lines2–4. **Quote:** “à vérifier” and “Nous laissons ici les détails”. **Context search:** `correspondance|fonctor|équiv|intersections`; T, cote44 scans002 and009; N, D08. **Delta:** adds the exact unfinished step behind the functoriality claimed by the earlier programme. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

The missing verification is the simultaneous choice of rationally equivalent $Z',\nu'$ for which pullback by $f\times\mathrm{id}_T$ and evaluation at $\nu'$ are defined. The displayed identity $f^*(Z'(\nu'))=Z'_1(\nu')$ records the intended compatibility, while the source explicitly leaves the existence of suitable representatives unproved. A statement that the folder already proves every pullback property must include this reservation.

### A08 — Unproved claim: ideal, proper pushforward, and projection formula

**Location:** scan025, lines2–11; scan028, lines6–12. **Quote:** “produits extérieurs” and “les $=$s propriétés formelles générales”. **Context search:** `produit|correspondance|Néron|équivalence`; T, cote44 scans002,004; N, D08 and D12. **Delta:** adds the quotient-ring formalism and its stated proof routes. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

The external-product route identifies $zz'$ with diagonal pullback of $z\times z'$, so the ideal assertion depends on the pullback verification in A07. Proper pushforward is assigned to the uncertain abbreviation “AQT”, and the projection formula is asserted in Scholie1.3 rather than separately checked. The abbreviation remains unexpanded in the transcription and unidentified by the supplied context.

### A09 — Unpursued implication: explicit endpoint identifications

**Location:** scan029, lines5–11; scan030, line2. **Quote:** “$u:A_T\longrightarrow\underline{\operatorname{Pic}}_X^0$”. **Context search:** `J\^1|operatorname\{Pic\}|J\^n|operatorname\{Alb\}`; T, cote44 scan008; N, D08. **Delta:** supplies the maps underlying the earlier endpoint claims. **R:** WG2 §2.3 #12 and #13, unchecked.

For zero-cycles, the diagonal correspondence gives the implication from the kernel of the degree–Albanese map to the new relation, and for divisors the family is evaluated through $\operatorname{Alb}(T)\xrightarrow{u}\operatorname{Pic}^0(X)$. Thus the manuscript connects $P^n(X)$ with $\operatorname{Alb}^0(X)(k)$ and $P^1(X)$ with $\operatorname{Pic}^0(X)(k)$ by specific maps, sharpening the assertions in cote44 scan008. The reverse zero-cycle implication still invokes the blank reference in A10.

### A10 — Unproved claim: an empty internal reference

**Location:** scan029, line11. **Quote:** “résulte de [ , 1.2.]”. **Context search:** `1\.2|noyau|application naturelle`; T, cote44 scan002, Theorem1; N, 44:2:1 and D08. **Delta:** adds a visible missing reference, without identifying it from context. **R:** WG2 §2.3 #12, unchecked.

The unnamed reference is used to show that an arbitrary correspondence carries a degree-zero Albanese-kernel zero-cycle to another Albanese-kernel zero-cycle. The map requiring justification is $\operatorname{Alb}(T)\to\operatorname{Alb}(X)$ induced by the correspondence, including its compatibility with cycle evaluation. Neither the supplied earlier transcription nor its notes identifies the blank citation.

### A11 — Conjecture/question with a later negative answer: zero-cycles

**Location:** scan029, line9. **Quote:** “Vrai pr tous les cycles???” **Context search:** `équivalence linéaire|équivalence.*Alb|Murre|Mumford`; T, cote44 scans002 and008; N, D08–D09. **Delta:** adds an explicit question to the earlier quotient programme. **R:** WG2 §2.3 #12 and #13; Hua 14-albanese-equivalence-ring, with the statuses above.

On $F=E\times E$ over $\mathbf C$, the Albanese map $a:\mathrm{CH}_0(F)^0\to F$ sends $[x]-[0]$ to $x$, and Mumford's theorem gives a nonzero kernel: injectivity would express every class as $[a(z)]-[0]$, contradicting his obstruction to bounded parametrization. Hence the map from rational-equivalence classes to the manuscript's zero-cycle quotient has nonzero kernel in this concrete example. This answers the written general question negatively through the exact quotient map, using [M], pp.196 and203.

### A12 — Own idea: the four-point box can survive rational equivalence

**Location:** scan030, lines14–19. **Quote:** “On ignore si cet $\nu$ est lin. équiv. à 0”. **Context search:** `produit|équiv.*lin|Albanese`; T, cote44 scans002 and008; N, D08. **Delta:** adds a concrete test family for the earlier quotient. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

On $E\times E$, each degree-zero cycle decomposes into its two axis projections plus sums of $b(x,y)=[(x,y)]-[(x,0)]-[(0,y)]+[(0,0)]$. The degree-zero axis summands map isomorphically to the two elliptic factors, so the boxes generate the Albanese kernel, which is nonzero by [M]. Therefore some displayed boxes are rationally nontrivial, while the manuscript's calculation $S_{E\times E}(b(x,y))=0$ makes all of them Albanese-trivial; **confidence high**, from the explicit axis decomposition and the cited obstruction to bounded parametrization.

### A13 — Unpursued implication: the square-zero calculation is explicit

**Location:** scan030, lines4 and12–16; scan034, lines6–8. **Quote:** “Alors $zz'=0$”. **Context search:** `Z.*alg|Z.*alb|équivalence|produit`; T, cote44 scan002; N, D08. **Delta:** adds a ring-theoretic consequence of the new definition. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

For the four-point parameter cycle in scan030, both projection sums cancel, and the product identification $\operatorname{Alb}(T\times T')\simeq\operatorname{Alb}(T)\times\operatorname{Alb}(T')$ gives its zero Albanese image. Evaluation by the external product of the two families supplies the stated product $zz'$. Thus the algebraically trivial ideal is proposed to square to zero in the Albanese quotient; the written argument concerns the quotient operation and retains the moving qualifications from §1.

### A14 — Conjecture: numerical strengthening remains a question

**Location:** scan030, lines4–5; scan034, line8. **Quote:** “num. équiv. à 0??” **Context search:** `tau|numérique|Matsusaka`; T, cote44 scan006, Theorem7; N, D14. **Delta:** restates the numerical-versus-torsion difficulty as a product question. **R:** WG2 §2.3 #12, unchecked.

The live addition asks whether one algebraically trivial factor and one numerically trivial factor suffice, whereas Corollary2.4 later states the conclusion for one algebraically trivial and one $\tau$-trivial factor. The latter calculation is $z=mz_0$, $mZ'$ algebraically trivial, hence $zZ'=z_0(mZ')=0$, using the divisibility asserted immediately before it. Cote44 scan006 asserts numerical $=\tau$ in a work programme, and its unreviewed note D14 flags the unrestricted assertion; these supplied pages provide no proof extending Corollary2.4 to the numerical formulation.

### A15 — Reading question: degrees and Albanese components

**Location:** scan031, lines4–18; scan036, lines2–4. **Quote:** “$A_Y^*(k)$” and “de degré $n$”. **Context search:** `Alb|Pic|cycle|degré`; T, cote44 scans002 and008; N, D08. **Delta:** adds a component-sensitive formulation absent from the earlier letter. **R:** WG2 §2.3 #12, unchecked.

Scan031 distinguishes the full degree-graded Albanese object $A_Y^*$ from its identity component $A_Y^0$, while scan036 writes $A_{0\,\mathrm{alb}}(A)$ next to an algebraically trivial subgroup without repeating the degree-zero restriction on the left. The actual evaluation map on degree-zero cycles is $u_Z:\operatorname{Alb}^0(Y)(k)\to P^i(X)$. Any identification involving all zero-cycles must also retain the degree map and its components.

### A16 — Self-flagged then addressed: dependence only on the correspondence class

**Location:** scan031, lines22–23; scan034, line2. **Quote:** “À réserver pr plus tard”. **Context search:** `noyau|correspondance|équiv`; T, cote44 scan002, Theorem1; N, D08. **Delta:** supplies a later argument for a claim first postponed in the new text. **R:** WG2 §2.3 #12, unchecked.

Scan034 returns to Theorem2.1$i$: the square-zero calculation annihilates the map for algebraically trivial $Z$, and $\tau$-triviality gives $mu=0$. The explicit divisibility argument is $u(a)=u(mb)=m u(b)=0$, for $a=mb$. This postponed step is therefore addressed within the supplied text, subject to the field convention and preceding quotient formalism.

### A17 — Unproved claim and later obstruction: the integral universal cycle

**Location:** scan032, lines13–29; scan033, lines2–4. **Quote:** “on ne sait pas si on peut trouver $U$”. **Context search:** `universel|universal|isogénie|cycle`; T, cote44 scans002 and008; N, D08–D10. **Delta:** adds the exact integral obstruction hidden by the earlier existence programme. **R:** WG2 §2.3 #13 and WG2 §2.4 #4, unchecked.

The identity $S_Y(U(a))=a$ is precisely the universal zero-cycle condition after normalizing the fiber at zero. Voisin's [V25, Definition1.1 and Theorem1.4] constructs smooth complex projective threefolds with representable $\mathrm{CH}_0$ and no such integral cycle on $\operatorname{Alb}(Y)\times Y$. The manuscript's replacement $S_Y(U(a))=na$ consequently records a mathematically substantive weakening, and the later counterexamples give a direct answer to the written uncertainty without resolving its dating.

### A18 — Unpursued implication: the multiplication-by-$n$ construction

**Location:** scan033, lines4–34. **Quote:** “On prend comme isogénie la multiplication pr $n$”. **Context search:** `isogénie|isogeny|universal|miniversal`; T, cote44 scan008; N, D10. **Delta:** adds the chosen isogeny and the equality needed by the earlier programme. **R:** WG2 §2.3 #13, unchecked.

The exact factorization sought is $v_{Z'}=u_Z\circ[n]$, with $Z'=Z\circ U$ and $S_Y\circ U_*=[n]\circ S_{A_Y}$ on $\mathrm{CH}_0(A_Y)^0$. [ACV23, Definition4.2 and Lemma4.7] calls the analogous cycle miniversal and constructs cycles inducing multiplication by a positive integer for surjective regular homomorphisms. The comparison identifies the maps and the integer retained by the manuscript, while the representability of its particular quotient remains a separate proof obligation.

### A19 — Reading question: equality of cycles versus equality in the quotient

**Location:** scan033, lines11–32. **Quote:** deleted “$U(a)=n\nu$”. **Context search:** `équiv|noyau|application naturelle`; T, cote44 scan002; N, D08. **Delta:** adds a visible revision in the proposed proof. **R:** WG2 §2.3 #12, unchecked.

Equality $S_Y(U(a))=S_Y(n\nu)$ gives $U(a)-n\nu$ in the Albanese kernel, hence equality after the quotient map, and evaluation by $Z$ then yields $Z'(S_Y\nu)=nZ(\nu)$. The source deletes an equality of unqualified cycles and inserts a sign read as $=|\equiv$, so the quotient map is exactly what the argument must retain. The cancelled $n^2$-formula and the surviving divisibility argument should remain visible as stages of the draft.

### A20 — Reading question: an arbitrary-codimension “diviseur”

**Location:** scan034, line4. **Quote:** “un diviseur de la forme $Z(a_0)$”. **Context search:** `diviseur|codimension|J\^i`; T, cote44 scan008; N, D08. **Delta:** adds a statement using abelian parameters, with a terminological mismatch. **R:** WG2 §2.3 #12, unchecked.

The corollary fixes arbitrary codimension $i$, so evaluating $Z\in A^i_{\mathrm{alb}}(A\times X)$ at $a_0$ again has codimension $i$. Its written word “diviseur” and its uncertain label $2.7|2.2$ are retained, while the mathematical map is the evaluation $A(k)\to P^i(X)$. The earlier intermediate-Jacobian letter contains the same arbitrary-codimension scope but supplies no missing wording for this corollary.

### A21 — Unproved claim: divisibility and its exact use

**Location:** scan034, lines6–8. **Quote:** “est $n$ divisible”. **Context search:** `dimension|Alb\(S\)|V.A.|Murre`; T, cote44 scan002; N, D09. **Delta:** adds a group property to the earlier abelian-variety programme. **R:** WG2 §2.3 #12 and #13, unchecked.

The source obtains divisibility from representation by an abelian parameter variety and surjectivity of its multiplication map on algebraically closed points. This supplies the division used in Corollary2.4, but a proof that $P^i(X)$ itself is represented by an abelian variety still needs the boundedness and kernel arguments listed in cote44 scan002. Kahn [K, Theorem0.1 and pp.844–846] proves existence of the universal regular homomorphism in codimension two for smooth projective $X$ of dimension greater than two over an algebraically closed field, and bounds every surjective regular homomorphism $\mathrm{CH}^2(X)_{\mathrm{alg}}\to B(k)$ by $2\dim B\le b_3(X)$, using prime-to-characteristic torsion and correcting the group-behavior gap for correspondence point maps.

### A22 — Own idea: a precise scope test for the saturation assertion

**Location:** scan035, lines6–25. **Quote:** “Si $N\varphi$ est alg., $\varphi$ l'est”. **Context search:** `application|homomorphisme|noyau|Albanese`; T, cote44 scan002, Theorem1; N, D08–D09. **Delta:** adds a counterexample to the unrestricted wording, while identifying an implicit ambient-group restriction to check. **R:** WG2 §2.3 #12; Hua 14-albanese-equivalence-ring, with the statuses above.

Take $k=\mathbf C$, $Y=\mathbf P^1$, $X=E$ elliptic, $i=1$, and a nonzero $t\in\operatorname{Pic}^0(E)[2]$; define $\varphi(\infty)=t$ and $\varphi(y)=0$ elsewhere. Then $2\varphi=0$ satisfies Definition2.5, but $\varphi([\infty]-[0])=t$ although $S_{\mathbf P^1}([\infty]-[0])=0$, violating condition1 for $\varphi$. Thus the literal assertion for all maps has this explicit counterexample; **confidence high**, and the reading question is whether the author has already restricted the ambient group to maps satisfying condition1.

### A23 — Own idea: rational correspondences and torsion

**Location:** scan035, line29; scan036, lines11–13. **Quote:** “un cycle à coeff rationnels quelconque”. **Context search:** `torsion|coeff|isogénie|Q`; T, cote44 scan008; N, D10. **Delta:** supplies an exact torsion test for the warning, rather than identifying integral and rational point actions. **R:** WG2 §2.3 #12 and #13, unchecked.

For an elliptic curve over $\mathbf C$, the correspondence $\frac12\Delta_E$ would require a homomorphism $h:E(\mathbf C)\to E(\mathbf C)$ with $2h=\mathrm{id}$. A nonzero $t\in E[2]$ gives $2h(t)=h(2t)=0$ whereas $\mathrm{id}(t)=t$, proving that no such homomorphism exists. This verifies the source's warning through an explicit correspondence and group equation; **confidence high**.

### A24 — Unproved claim: composition of algebraic homomorphisms

**Location:** scan036, line13. **Quote:** “Ces homs se composent”. **Context search:** `correspondance|transpos|composition`; T, cote44 scans002,009; N, D08. **Delta:** adds a proposed category of the groups $P^i(X)$. **R:** WG2 §2.3 #12, unchecked.

The formal calculation uses representing cycles for $N\varphi$ and $M\psi$, whose composition represents $MN(\psi\circ\varphi)$. This still requires the descended action of integral correspondences on the quotient groups, so the previously marked pullback and intersection verifications are inherited by the composition claim. The source supplies no separate construction of a representing variety for every object in this category.

### A25 — Conjecture/question: closure under inverse maps

**Location:** scan037, lines2–3. **Quote:** “s'ils peuvent s'inverser”. **Context search:** `isomorphisme|semi.simple|inverse|algébrique`; T, cote16 scan049; cote44 scan002; N, S14 and D08. **Delta:** adds an inverse-closure question for the correspondence-defined homomorphisms. **R:** WG2 §2.3 #7 and #12, unchecked.

The requested inverse is the inverse of a group isomorphism $P^j(X')\to P^i(X)$, together with an integral multiple represented by a correspondence. Cote16 scan049 also asks for algebraic inverses of realized correspondence maps, providing a related algebraic-splitting programme with explicitly different source and target groups. The supplied pages construct neither the inverse correspondence nor a comparison functor proving the two inverse problems equivalent.

### A26 — Unproved claim: transposition and the complementary degree

**Location:** scan037, lines5–12. **Quote:** “$i+j=n+1$”. **Context search:** `dualité canonique|n.1.i|Pic|duale`; T, cote44 scans002,008; cote54 scans003,005; N, D08 and D02. **Delta:** supplies the correspondence map behind the earlier duality claim. **R:** WG2 §2.3 #12 and WG2 §2.4 #4, unchecked.

The new construction sends the map $u_Z:A(k)\to P^i(X)$ induced by $Z$ to $u_{{}^tZ}:P^j(X)\to P^{i+j-n}(A)=P^1(A)\simeq A^\vee(k)$. This is the exact degree calculation connecting the proposed complementary $P^i$-duality with Picard duality, while cote54 frames its duality comparison through universal vector extensions and de Rham cohomology. The source immediately flags the independence of the representative cycle, so this passage gives the proposed morphism rather than a completed descent proof.

### A27 — Self-flagged unproved claim: descending transposition

**Location:** scan037, lines14–19; scan038, lines12–22. **Quote:** “il faut vérifier” and “Cf plus bas”. **Context search:** `dualité|canoniquement duales|noyau`; T, cote44 scans002,008; N, D08. **Delta:** exposes a prerequisite behind the earlier canonical-duality claim. **R:** WG2 §2.3 #12, unchecked.

The needed kernel statement is that two cycles producing the same map $A(k)\to P^i(X)$ have transposes producing the same map $P^j(X)\to A^\vee(k)$. The following section instead opens an ℓ-adic vanishing problem and marks its proof unfinished, so the cross-reference does not complete this descent in the supplied run of pages. The same requirement remains explicit for general maps $P^i(X)\to P^{i'}(X')$.

### A28 — Own idea: a comparison map to the algebraic Abel–Jacobi image

**Location:** scan024, lines8–12; scan035, lines6–18; scan037, lines5–14. **Quote:** “$S_Y(\nu)=0$”. **Context search:** `relation d'équivalence|Abel|regular|universality`; T, cote44 scan008; N, D08. **Delta:** adds a concrete comparison map to the earlier identification question. **R:** WG2 §2.3 #13, unchecked.

For complex smooth projective $X$ and the projective parameter spaces $T$ retained in the bracketed definition, a family $Z$ on $T\times X$ induces $\operatorname{Alb}(T)\to J_a^{2i-1}(X)$, as in [V22, Introduction, pp.1–2], so its Abel–Jacobi map kills every generator $Z_*(\ker S_T)$ of the manuscript's relation. Hence there is an induced homomorphism $P^i(X)\to J_a^{2i-1}(X)$ through which the Abel–Jacobi map factors. **Confidence high** for this factorization by the displayed maps; the injectivity and representability of this quotient are further questions, and this record asserts neither.

### A29 — Self-flagged unproved claim: Theorem3.1

**Location:** scan038, lines10–22; scan039, lines8–12. **Quote:** “dém. pas faite”. **Context search:** `T_.*ell|sous.module|Betti|cohomologie`; T, cote44 scan008; N, D09–D10. **Delta:** adds the exact unproved implication supporting the earlier cohomological bounds. **R:** WG2 §2.3 #12 and #13, unchecked.

The proposed implication sends vanishing of the point-family map $u_Z$ to vanishing of the cohomological correspondence $a({}^tZ)$, and the author labels the theorem's proof unfinished. Scan039 reduces the discussion to the middle Künneth summand but supplies no subsequent step from the quotient relation to the vanishing of that summand. Thus this is a documented gap, not a completed proof of cote44's general Tate-module or dimension claim.

### A30 — Reading question: the two coefficient operations

**Location:** scan038, line12. **Quote:** “mod. torsion (i.e. à coefficients $\mathbf Q_\ell$!)”. **Context search:** `torsion|Z_.*ell|Q_.*ell`; T, cote44 scan008; N, D10. **Delta:** adds a coefficient qualification to the earlier integral expectation. **R:** WG2 §2.3 #13, unchecked.

For a finitely generated $\mathbf Z_\ell$-module $M$, the canonical map $M/\mathrm{tors}\to M\otimes\mathbf Q_\ell$ is injective; for $M=\mathbf Z_\ell$, its cokernel is $\mathbf Q_\ell/\mathbf Z_\ell$. For maps $f:M\to N$ between such modules, the vanishing tests agree through the explicit identities $f\otimes\mathbf Q_\ell=0\Longleftrightarrow\operatorname{im}f\subset N_{\mathrm{tors}}\Longleftrightarrow\bar f=0$. Thus the source's rational vanishing formulation retains the same kernel, while an integral comparison still retains the displayed lattice inclusion.

### A31 — Reading question: cohomological degrees

**Location:** scan038, lines10,20,33. **Quote:** $H^{(n-i)+1}$ in the theorem display. **Context search:** `H\^.*2i|T_.*ell|cohomologie`; T, cote44 scan008; N, D10. **Delta:** adds a degree audit to the earlier realization claim. **R:** WG2 §2.3 #12 and #13, unchecked.

The correspondence formula is $a({}^tZ)(\alpha)=p_{A*}(p_X^*\alpha\smile\operatorname{cl}Z)$, so its target degree is $\deg\alpha+2i-2n$. A target in $H^1(A)$ therefore uses $\deg\alpha=2(n-i)+1$, matching the opening display but differing from the theorem's written exponent and the uncertain later $3|1$. These are reading questions only; the three frozen exponents remain unchanged.

### A32 — Reading question: the curve map on points

**Location:** scan038, lines24–35; scan039, line3. **Quote:** “$C(k)\mathbin{-}A(k)$ surjectif”. **Context search:** `Alb\(S\)|application naturelle|courbe|jacobienne`; T, cote44 scans002,008; N, D08–D09. **Delta:** adds an explicit obstruction to the literal curve-point assertion. **R:** WG2 §2.3 #12 and #13, unchecked.

An included ample curve in an abelian surface has one-dimensional image, so its inclusion on algebraically closed points omits the points of the nonempty surface complement. The map naturally associated to the intended reduction is $J(C)\to A$, induced by $C\hookrightarrow A$, and the points of $C$ generate $J(C)(k)$; [K, Lemma1.1 and Remark1.2] explicitly uses this Jacobian correspondence and generation mechanism. The passage therefore needs a comparison through $J(C)$, while the frozen $C(k)\to A(k)$ remains literal.

### A33 — Own idea: the algebraic Künneth projectors of the curve

**Location:** scan039, lines8–12. **Quote:** “est algébrique, comme … on vérifie aisément”. **Context search:** `Künneth|projecteurs|pi_|pi\^`; T, cote16 scans033–034,046; N, S6 and S17. **Delta:** adds an explicit curve-level construction to the earlier projector programme. **R:** WG2 §2.4 #3, unchecked.

For a chosen $c_0\in C(k)$, use $\pi_0=[c_0\times C]$, $\pi_2=[C\times c_0]$, and $\pi_1=[\Delta_C]-\pi_0-\pi_2$, acting by pushforward to the second factor. These cycles induce the three cohomological projectors, and $\mathrm{id}_X\times\pi_r$ gives the corresponding three pieces on $X\times C$. **Confidence high**, from the action of each displayed cycle; this supplies the asserted algebraicity of the curve decomposition but leaves the unfinished middle-factor argument in A29.

### A34 — Conjecture/question: the converse to Theorem3.1

**Location:** scan038, line22; scan039, lines3–12. **Quote:** “A-t-on une réciproque”. **Context search:** `noyau|sous.module|cohomologie|T_.*ell`; T, cote44 scans002,008; N, D09–D11. **Delta:** adds a converse question to the earlier realization expectations. **R:** WG2 §2.3 #12 and #13, unchecked.

The converse asks whether $a({}^tZ)=0$ forces $u_Z=0$ in the manuscript's quotient, thereby identifying the kernel of a cohomological realization on these family maps. The explicit comparison $P^i(X)\to J_a^{2i-1}(X)$ of A28 provides a map to examine over $\mathbf C$, but its kernel is exactly additional information that these pages do not determine. Neither the curve reduction nor the earlier register supplies the requested converse in the stated generality.

### A35 — Unpursued implication: a verified later realization in selected codimensions

**Location:** scan038, lines10–12,17–22. **Quote:** “ne dépend que de $u_Z$”. **Context search:** `T_.*ell|sous.module|Betti`; T, cote44 scan008; N, D09–D10. **Delta:** adds a verified scoped comparison to the earlier cohomological expectation. **R:** WG2 §2.3 #13, unchecked.

For a smooth proper variety $X$ over a field $K$, [ACV23, Proposition8.2] constructs $T_\ell B\hookrightarrow H^{2i-1}(X_{K^{\mathrm{sep}}},\mathbf Z_\ell(i))/\mathrm{tors}$ for a surjective regular homomorphism to $B$ equipped with a miniversal cycle of degree $r$, in codimensions $i=1,2,\dim X$, with $\ell\ne\operatorname{char}K$ and $\ell\nmid r$. This verifies the precise later statement cited as a lead in N,D10 and identifies its cycle and excluded primes. A comparison from the manuscript's $P^i(X)$ to that algebraic representative is still required before using this injection to answer its general Theorem3.1.

### A36 — Unpursued implication: the modern autoduality keeps the same transpose

**Location:** scan019, lines20–37; scan037, lines5–19. **Quote:** “Dualité” and “pas du cycle $Z$”. **Context search:** `autodualité|positive|polarisation`; T, cote44 scans002,008–009; N, D13. **Delta:** adds a later construction with the same composed correspondence. **R:** WG2 §Lookups #3 and WG2 §2.3 #12, unchecked.

[ACV25, Theorems1 and12.12] constructs a canonical autoduality for geometrically stably rational smooth projective threefolds over perfect fields using the cycle $-{}^tZ\circ Z$ from a universal codimension-two cycle. Over characteristic zero their map agrees with the Hodge principal polarization, while their Conjecture5.1 explicitly retains a positivity question in positive characteristic under its stated diagonal-decomposition hypothesis. This comparison fixes the sign and the cycle composition linking it to the manuscript, and does not promote the arbitrary-codimension duality programme to a theorem.

### A37 — Reading question: verdict on the supplied Hua register entry

**Location:** scan024, lines8–16; scan025, lines2–11; scan028, lines2–12; scan029, lines5–11; scan030, lines4–19; scan034, lines6–8. **Quote:** “à vérifier”. **Context search:** `14-albanese-equivalence-ring|Albanese|Murre`; R; T, cote44 scans002 and008; N, D08–D09. **Delta:** confirms the stated definition and propositions but qualifies the claim of proved functoriality. **R:** Hua, findings register, **14-albanese-equivalence-ring** [conjecture (unsearched), reach beyond; intake pending].

The supplied register excerpt correctly points to the definition through Albanese-kernel zero-cycles, the proposed quotient ring, the stated pullback/pushforward properties, and the endpoint calculations. Its wording “shows” requires qualification because scan028 explicitly leaves the moving verification undone; the bracketed projectivity in scan024 and the field convention in A05 also belong in the scope. The excerpt ends after “identifies…”, so no verdict is assigned here to words absent from the supplied register.

### A38 — Unpursued implication: Oda's degree-one comparison retains the full Picard scheme

**Location:** scan038, lines10–12 and24–35; scan039, lines8–12. **Quote:** “Homomorphisme $\ell$-adique”. **Context search:** `Dieudonn|Cartier|t_E|H\^1`; T, cote54 scans003,005,007; N, D01–D05; supplied `Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`, printed pp.64,124,131. **Delta:** adds a proved characteristic-$p$ degree-one comparison to the earlier duality programme. **R:** WG2 §1.1 #2 and WG2 §2.4 #4, unchecked.

Oda's Corollary5.11 gives $M({}_pA)\simeq H^1_{\mathrm{dR}}(A)$ for an abelian scheme over a perfect field of characteristic $p$, with $VM({}_pA)$ mapped onto $H^0(A,\Omega^1)$ and with the displayed exact sequences corresponding. His Corollary5.12 gives $DM({}_p\operatorname{Pic}_{X/k})\hookrightarrow H^1_{\mathrm{dR}}(X)$ for smooth proper $X$ with a $k$-point, with image $\bigcap_n\ker(d\circ V^n)$. The group scheme in this map is the kernel of $[p]$ on the full Picard scheme, retaining its nonreduced structure, as his Introduction explicitly explains. These maps supply a precise realization comparison for the abelian source in scan038; compatibility with the manuscript's quotient $P^i(X)$ and its unfinished vanishing statement remains the additional step to establish.

## Standing-question contributions for the parent notes

### Steps explicitly marked unverified or postponed in these scans

| Scan / frozen TeX line | Manuscript wording | Step and later state in the supplied pages |
|---|---|---|
|024:14|“?”|Unattached reservation beside the opening definition; attachment should remain uncertain.|
|026:18|“sous réserve que” / “choisi convenablement”|Defined evaluations at selected parameter points; no independent moving proof supplied.|
|028:2–4|“à vérifier”; “Nous laissons ici les détails…”|Simultaneous movement needed for pullback.|
|029:2|“Ici il semble … $T$ projectif”|Use of projectivity in the endpoint argument.|
|029:9|“On ignore …”; “Vrai pr tous les cycles???”|Equality with rational/linear equivalence; later mathematical answer discussed in A11–A12.|
|029:11|Blank “[ , 1.2.]”|External/internal support for preservation of Albanese kernels.|
|030:4|“num. équiv. à 0??”|Proposed numerical strengthening, not settled by the later $\tau$-version.|
|030:5|Deleted “À voir…”|Heavily uncertain cancelled strengthening, not treated as a live theorem.|
|030:17|“On ignore…”|Rational triviality of the four-point box, even for curves.|
|030:19|“Il y a intérêt à transformer…”|External-product reformulation proposed, not subsequently developed explicitly.|
|031:23|“À réserver pr plus tard”|Dependence on the $\tau$-class, explicitly revisited in034:2.|
|032:19,27|Uncertain “dont il faut vérifier”; “O.K.”|A local check around the proposed universal family; the existence of $U$ remains open in the next line.|
|032:29–033:2|“on ne sait pas si on peut trouver $U$”|Integral universal cycle replaced by the multiplication-by-$n$ construction.|
|035:23|“Va être généralisé en2.7(ii)”|Functoriality extension is then stated.|
|036:13|“mais attention…”|A rational cycle need not induce an integral point-group homomorphism; exact torsion example A23.|
|037:2–3|“?”; “Une question plus subtile…”|Algebraicity of inverses.|
|037:14,19|“il faut vérifier”; “Cf plus bas…”|Descent of transposition from cycles to induced maps; remains unfinished.|
|038:17,20|“dém. pas faite”; question mark over implication|Theorem3.1's forward cohomological implication.|
|038:22|“A-t-on une réciproque”|Converse realization implication.|
|039:12|“on vérifie aisément”|Algebraic curve Künneth projectors; explicit construction A33.|

### Titles and counts in this part

- Scan017 is the cover “Équivalence d'Albanese et de Picard des cycles algébriques”; the visible “16” is a sheet/page marking, not an explicit count of leaves.
- Scan024 names “Théorie de l'équivalence d'Albanese des cycles” and §1 “L'anneau des [classes d']équivalence d'Albanese”.
- Scan031 names §2 “Familles de classes de cycles mod équiv. d'Alb.”.
- Scan038 names §3 “Homomorphisme ℓ-adique associé à une famille abélienne de cycles”.
- The inspected text in this thread supplies manuscript page marks 18,20,23–38, rather than a title followed by an explicit total page count; no total is inferred from those marks.

## Primary bibliography and verification record

**[M]** Mumford, D. (1969). *Rational equivalence of 0-cycles on surfaces*. Journal of Mathematics of Kyoto University9(2),195–204. [Author-hosted scan](https://www.dam.brown.edu/people/mumford/alg_geom/papers/1969e--0-cycles-Euclid.pdf). Read introduction pp.195–197 and proof/conclusion pp.202–203; web PDF screenshot requested for pp.196 and203. Search metadata misleadingly labels this PDF with an unrelated title, but its first page identifies Mumford's article and 1969 issue. Tool refs for root reopening: `turn20view0`, `turn22view0`, `turn22view1`.

**[K]** Kahn, B. (2021). *On the universal regular homomorphism in codimension2*. Annales de l'Institut Fourier71(2),843–848. [Published PDF](https://www.numdam.org/item/10.5802/aif.3408.pdf), [DOI](https://doi.org/10.5802/aif.3408). Read Theorem0.1, bound argument, gap statement, Lemma1.1 and Remark1.2, pp.843–846; PDF screenshot requested for p.844. Tool refs: `turn12view0`, `turn20view5`.

**[ACV23]** Achter, J. D., Casalaina-Martin, S., & Vial, C. (2023). *A functorial approach to regular homomorphisms*. Algebraic Geometry10(1),87–129. [Published PDF](https://api.algebraicgeometry.nl/Article/19846/2023-1-003.pdf), [DOI](https://doi.org/10.14231/AG-2023-003). Read Definition4.2, Lemma4.7, Corollary4.8, Theorem6.1, §§8.1–8.2 and Proposition8.2; screenshot requested for printed p.120. Tool refs: `turn12view1`, `turn20view1`, `turn20view2`, `turn22view2`, `turn22view3`.

**[V22]** Voisin, C. *Geometric representability of 1-cycles on rationally connected threefolds*. [Author-hosted manuscript](https://webusers.imj-prg.fr/~claire.voisin/Articlesweb/1cycleRC.pdf). Read Introduction, the explicit $\operatorname{Alb}(M)\to J_a^{2k-1}(X)$ construction and Remark0.1; also located current Corollary0.14 on absence of universal zero-cycles (the earlier context's cited numbering0.13 comes from a different version). Tool refs: `turn28view0`, `turn40view3`; bibliographic year here is a label, not an independently verified journal publication date.

**[V25]** Voisin, C. (2025). *Varieties with representable $\mathrm{CH}_0$-group and a question of Colliot-Thélène*, arXiv:2508.02331v2,15October2025. [Primary HTML](https://arxiv.org/html/2508.02331v2). Read Definition1.1, Theorem1.4, §1 and the exact Albanese morphism. Tool refs: `turn28view2`, `turn40view4`.

**[ACV25]** Achter, J. D., Casalaina-Martin, S., & Vial, C. (2025). *Decomposition of the diagonal, intermediate Jacobians, and universal codimension-2 cycles in positive characteristic*. Astérisque455. [Author-hosted manuscript dated19March2025](https://www.math.uni-bielefeld.de/~vial/diagonal.pdf), [publisher listing](https://smf.emath.fr/publications/decomposition-de-la-diagonale-jacobiennes-intermediaires-et-cycles-universels-de?language=en). Read Theorem1, Theorem4.4, Conjecture5.1, Theorem12.12, Remark12.13 and the start of§13. Tool refs: `turn28view1`, `turn40view0`, `turn40view1`, `turn40view2`.

**[O]** Oda, T. (1969). *The first de Rham cohomology group and Dieudonné modules*. Annales scientifiques de l'École Normale Supérieure,4th series,2(1),63–135. Supplied file `context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf`; [published PDF](https://www.numdam.org/item/ASENS_1969_4_2_1_63_0.pdf). Read the Introduction pp.63–65, Theorem5.10 p.124, Corollaries5.11–5.12 p.131, and the preceding discussion of the full and reduced Picard schemes in §4; visually inspected rendered printed p.131 at full size to verify the exact maps and filtration. Corollary5.11 is a corollary, not a theorem numbered5.11. Root-reopen web ref: `turn64view0`.

## Evidence handling

- No source images or OCR were used in this research thread.
- No frozen transcription file was changed.
- Each note's context search was subsequently run and recorded in `records/research_albanese_context_search.md`; the selected comparison appears in the note metadata above.
- Own calculations in A01, A22, A23, A28, A30–A33 give the actual maps or cycle operators. They do not assert historical intention, novelty, or a theorem solving the general programme.
