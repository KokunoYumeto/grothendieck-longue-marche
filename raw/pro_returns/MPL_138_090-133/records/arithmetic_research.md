# Arithmetic research on frozen scans 104–112

**Researcher:** GPT-6 Astra Pro; inherited effort not exposed; run `MPL_138_090-133/arithmetic_research`.

**Scope and provenance:** Research began after the transcription freeze at 2026-11-17 23:02:39 UTC and context opening at 23:02:52 UTC; this agent read only frozen TeX and supplied textual context, never the scan images, and changed no transcription, doubts, inventory, or main notes. The complete `context/README.md`, `context/notes/RESULTS_STATE.md`, and `context/hua_project/README.md` were read before these notes; Hua's relevant subsections were read and are credited below. Earlier-run statements remain claims at the status given in `RESULTS_STATE.md`; none of their general tower or GT conclusions is imported as a proved premise here.

**Main finding:** The answer to the explicit question on scan 112 is **yes**: the coefficient polynomial \(P\) obtained by the source's remainder procedure is divisible by \(\delta=25c^2-32c+16\). Removing those two degenerate parameters leaves the irreducible cubic \(25c^3-12c^2-24c-16\), with one real class and a conjugate chiral pair; this cubic and these three dessins are already recorded by Gareth A. Jones, Example 7.7, so no claim of novelty in the literature is made.

**Reproducibility:** `arithmetic_certificate.py` produces `arithmetic_certificate.json` using exact rational polynomial arithmetic and exhaustive permutations on six letters; its successful execution at 2026-11-17 23:10:28 UTC checks all 44 frozen SHA-256 entries before and after computation. `arithmetic_supplement.py` and `.json` add exact checks of AR03, AR15, and AR18 at 2026-11-17 23:18:48 UTC; `arithmetic_context_search.json` records separate supplied-context searches for every item below; `arithmetic_check_events.tsv` records actual checks separately from the main ledger. All line numbers refer to the frozen local TeX, not to a re-reading of handwriting; Hua's page number is one less than the scan number used here.

## AR01 — The seven explicit small maps have the stated ramification

**Kind:** unproved-claim check. **Source:** `pages/MPL_138_090-133_138_scan104.tex`, lines 12, 23, 38, 61, 70, 79; `pages/MPL_138_090-133_138_scan105.tex`, line 17. **Brief source quote:** “\(f(z)=\frac4{27}\frac{z^3}{z-1}\)”. **Confidence:** high; exact derivatives and fibre factorizations in the certificate.

The seven displayed functions give the following partitions over \(0,1,\infty\), so their algebra agrees with the asserted small-map types. For the last two maps the useful exact factorizations are \(f-1=(2z-3)^2(z+3)/(27(z-1))\) and \(f-1=(3z-1)^2(3z-4)/4\), respectively, checking the special coordinates on scans 104–105.

| Function | Over 0 | Over 1 | Over infinity |
|---|---|---|---|
| \(z\) | \(1\) | \(1\) | \(1\) |
| \(z^2\) | \(2\) | \(1,1\) | \(2\) |
| \(-4z(z-1)\) | \(1,1\) | \(2\) | \(2\) |
| \(z^2/(4(z-1))\) | \(2\) | \(2\) | \(1,1\) |
| \(z^3\) | \(3\) | \(1,1,1\) | \(3\) |
| \(4z^3/(27(z-1))\) | \(3\) | \(2,1\) | \(2,1\) |
| \(27z(z-1)^2/4\) | \(2,1\) | \(2,1\) | \(3\) |

**Context relationship:** This independently checks the formulas collected by **Hua, modernised reading of cote 138**, subsection “Premiers exemples (pages 103 et 104),” `context/hua_project/138.modern.tex`, lines 1617–1643; relative to `RESULTS_STATE.md`, **EXIT_TOWER E.24** and README Bridge B6, it supplies elementary finite examples and does not determine an arithmetic image on a modular tower.

## AR02 — The barycentric equation is an exact inverse-real-axis calculation

**Kind:** unproved-claim check. **Source:** `pages/MPL_138_090-133_138_scan105.tex`, line 3. **Brief source quote:** “réunion de la droite \(y(=\Im z)=0\), et de la courbe \(2x(x^2+y^2)+(-3x^2+y^2)=0\)”. **Confidence:** high; exact symbolic identity.

For \(f(z)=4z^3/(27(z-1))\), direct calculation gives
\[
\Im f(x+iy)=\frac{4y\,[2x(x^2+y^2)-3x^2+y^2]}{27((x-1)^2+y^2)},
\]
which verifies the asserted real locus away from the pole, with the pole and infinity interpreted on the projective line. **Context relationship:** This confirms **Hua, modernised reading of cote 138**, “Premiers exemples,” lines 1638–1640; searches of the remaining context give no matching equation, and **EXIT_TOWER E.24** is relevant only through the finite cartographic interpretation, not through any tower-image conclusion.

## AR03 — Two co-pinnings of the cubic star detect the mod-3 cyclotomic character

**Kind:** unproved-claim check. **Source:** `pages/MPL_138_090-133_138_scan104.tex`, lines 68–71. **Brief source quote:** “a deux éléments … \(\Gamma\) opère via le … caractère cyclotomique”. **Confidence:** high; direct quotient-of-labelings proof.

The six labelings of the three points of \(f^{-1}(1)=\mu_3\), modulo the deck group \(z\mapsto\zeta_3z\) of order three, give exactly two classes; complex conjugation swaps them because it acts on \(\mu_3\) by a transposition. Thus the co-pinned action is \(\chi_3\), while the underlying unpinned cover \(z^3\) is defined over \(\mathbb Q\). **Context relationship:** This rechecks, with the labeling argument supplied, **Hua, modernised reading of cote 138**, “Premiers exemples,” lines 1631–1634, and his “Calculs : \(z\mapsto z^n\), la fonction \(g\), Kummer sur \(\mathbb Q\),” lines 582–600; it is a finite cyclotomic instance relevant to **EXIT_TOWER E.24**, and does not settle **LM7_PUSH E.3**.

## AR04 — The two permutation tables generate \(S_6\)

**Kind:** own derived check of the unfinished group calculation. **Source:** `pages/MPL_138_090-133_138_scan106.tex`, lines 18, 21–27, 44–50; `pages/MPL_138_090-133_138_scan107.tex`, lines 5–9. **Brief source quote:** “\(\rho_f=\rho_s^{-1}\sigma\)” and the cancelled “\(\rho_s^3=(\tau_{4,5})\)”. **Confidence:** high for the explicitly stated conditional reading; exhaustive finite computation.

Using the first-listed indices in the frozen doubtful entries and composing right to left gives \(\rho_s=(123)(45)\), \(\sigma_I=(14)(36)\), \(\sigma_{II}=(14)(56)\), and face cycles \((154362)\), \((156432)\); both generated groups have order \(720\), hence are \(S_6\). The cancelled powers \(\rho_s^3=(45)\) and \(\rho_s^4=(123)\) are correct, but the isolated “\(\mathbb Z/6\mathbb Z\)” on scan 106 is not safely identifiable as a claim about the whole monodromy group. **Context relationship:** This adds explicit group computations to **Hua, modernised reading of cote 138**, “Un arbre de degré 6 (pages 105 à 111),” lines 1649–1654, and matches Jones, Example 7.7 [J]; **EXIT_TOWER E.24** concerns a different arithmetic-image problem.

## AR05 — The doubtful index in table II has a mathematical preference

**Kind:** reading question; no transcription change. **Source:** `pages/MPL_138_090-133_138_scan106.tex`, line 49. **Brief source quote:** `\rho_s r_5=r_{\unsure{4|2}}`. **Confidence:** high for the permutation constraint, no new judgment of handwriting.

The choice \(r_4\) completes \((123)(45)(6)\), while \(r_2\) repeats the image of \(r_1\) and leaves \(r_4\) without a preimage, so it cannot be a permutation with the other entries held fixed. This supports the first-listed reading but leaves the frozen uncertainty intact, as it could also indicate a source slip elsewhere in the table. **Context relationship:** **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1652–1654, treats these columns as permutations without preserving this individual doubt; this is the resulting reading question, with **EXIT_TOWER E.24** only contextual and no prior result changed.

## AR06 — Exact completion of the source's remainder computation

**Kind:** own derivation completing an unfinished calculation. **Source:** `pages/MPL_138_090-133_138_scan107.tex`, lines 15–34; `pages/MPL_138_090-133_138_scan108.tex`, lines 4–43; `pages/MPL_138_090-133_138_scan109.tex`, lines 5–10. **Brief source quote:** “\(\lambda(P(c)u+Q(c))=1\)”. **Confidence:** high; unique polynomial remainder and exact identities.

Put \(H=z^3(z-1)^2(z-c)\), \(g=z^2-(5c+4)z/6+c/2\), \(\delta=25c^2-32c+16\), and \(R=25c^3-12c^2-24c-16\); then
\[
H'=6z^2(z-1)g,\qquad H\bmod g=P_{\rm rem}(c)z+Q_{\rm rem}(c),
\]
\[
P_{\rm rem}=-\frac{\delta R}{7776},\qquad
Q_{\rm rem}=\frac{c(5c-8)(25c^3-6c^2+8)}{2592}.
\]
These are the source's \(P,Q\) under its specified remainder definition, not a polynomial silently substituted for \(P\): clearing denominators gives \(\widetilde P=\delta R=-7776P_{\rm rem}\), and the leading coefficient \(-625/7776\) agrees with scan 108's \(-\frac16(\frac56)^4c^5\). **Context relationship:** This completes, rather than attributes to the manuscript, the calculation that **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1665–1675, explicitly says was not written out; no exact formula is registered in `RESULTS_STATE.md`, and **EXIT_TOWER E.24** remains outside the scope of this computation.

## AR07 — Endpoint and \(Q\)-exclusions hold exactly

**Kind:** targeted proof check of a source claim. **Source:** `pages/MPL_138_090-133_138_scan111.tex`, lines 12–29, 40–50; `pages/MPL_138_090-133_138_scan112.tex`, line 3. **Brief source quote:** “les zéros de \(P(c)\) sont distincts de \(0,1\) et ne sont pas des zéros de \(Q\)”. **Confidence:** high; exact evaluations and a Bézout identity.

In the remainder normalization of AR06, \(P(0)=8/243\), \(P(1)=1/32\), and \(\gcd(P,Q)=1\), with explicit rational-polynomial Bézout coefficients included in `arithmetic_certificate.json`. Thus the exclusions \(c\ne0,1\) and \(Q(c)\ne0\) follow from \(P(c)=0\), although the distinct-critical-point condition \(\delta(c)\ne0\) does not. **Context relationship:** This independently checks the endpoint argument reported by **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1676–1678; the nearest registered question is **EXIT_TOWER E.24**, to which this finite calculation adds an example rather than a solution.

## AR08 — The quadratic roots require a factor-of-two correction in research commentary

**Kind:** reading/arithmetic question, already identified by Hua; source retained. **Source:** `pages/MPL_138_090-133_138_scan111.tex`, lines 32–34. **Brief source quote:** “\(c=\dfrac{16}{25}\pm\dfrac{24}{25}i\)”. **Confidence:** high; quadratic formula and substitution.

The roots of \(25c^2-32c+16\) are \(16/25\pm12i/25\), because its discriminant is \(-576\) and the denominator in the quadratic formula is \(50\). The frozen \(24/25\) remains as written; this is a research correction, not an emendation or a new discovery of this run. **Context relationship:** Credit belongs to **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” footnote at lines 1680–1682, which explicitly gives this correction; `RESULTS_STATE.md` has no separate arithmetic ID for it, and **EXIT_TOWER E.24** is only the surrounding program.

## AR09 — The explicit \(P\)-versus-\(\delta\) question has answer yes

**Kind:** self-flagged question answered by exact computation. **Source:** `pages/MPL_138_090-133_138_scan112.tex`, lines 3–5. **Brief source quote:** “Mais pourraient-ils être zéros de \(\delta(c)=25c^2-32c+16\quad ?\)”. **Confidence:** high; exact factorization in AR06.

Both zeros of \(\delta\) are zeros of the source's remainder coefficient \(P\), since \(P=-\delta R/7776\), and neither is a zero of \(Q\) by AR07. Consequently the condition \(\delta\ne0\) on scan 109 is essential and removes two of the five roots of \(P\). **Context relationship:** This answers the question left open in **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1678–1680; it is a completed local calculation relative to the supplied context, not a resolution of **EXIT_TOWER E.24** or a claim of literature novelty.

## AR10 — The discarded quadratic roots describe a different passport

**Kind:** checked implication of the degeneracy question. **Source:** `pages/MPL_138_090-133_138_scan107.tex`, lines 31–34; `pages/MPL_138_090-133_138_scan112.tex`, lines 3–12. **Brief source quote:** “\(u,v\) distincts entre eux” and the nearby degree lists on scan 112. **Confidence:** high; critical-value and derivative-multiplicity checks.

At \(c=16/25\pm12i/25\), the two roots of \(g\) coincide at \(u=v=(3\pm i)/5\), and \(f=H/Q\) satisfies \(f(u)=1\), \(f'(u)=f''(u)=0\), \(f'''(u)\ne0\). The resulting passport is \((3,2,1)\mid(3,1,1,1)\mid(6)\), consistent with the degree-three entry beside the question on scan 112: these are still three-branch covers, but their branch permutation over \(1\) has order three and they fail the intended two-double-point condition. **Context relationship:** This supplies the degeneration behind the \(\delta\ne0\) condition in **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1669–1680; it adds a concrete distinction relevant to Bridge B6 and **EXIT_TOWER E.24**, without asserting any general arithmetic-image result.

## AR11 — The remaining cubic gives exactly the intended nondegenerate fibres

**Kind:** own derivation; exact completion of the residual factor. **Source:** `pages/MPL_138_090-133_138_scan107.tex`, line 34; `pages/MPL_138_090-133_138_scan109.tex`, lines 35–43; `pages/MPL_138_090-133_138_scan111.tex`, lines 4–8. **Brief source quote:** “\((z^2-\alpha z-\beta)^2(z^2+lz+m)\)”. **Confidence:** high; polynomial division and nonzero resultants.

On \(R(c)=0\), set
\[
B=z^2+\frac{2c-2}{3}z+\frac{5c^2-4c-4}{12};\qquad
H-Q=g^2B,
\]
where the identity is understood modulo \(R\), with the exact multiple \(RT\) before specialization supplied in the certificate. The checks \(\operatorname{Res}_c(R,\delta)=23328000\), \(\operatorname{Res}_c(R,Q)=500\), \(\operatorname{Res}_c(R,\operatorname{disc}_z B)=-256\), and \(\operatorname{Res}_c(R,\operatorname{Res}_z(B,g))=91125\) prove two distinct double points and two distinct simple points over \(1\), with all forbidden collisions excluded. **Context relationship:** This adds the missing residual quadratic to **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1664–1675, and gives the finite nondegenerate example associated with **EXIT_TOWER E.24**, without addressing its general open target.

## AR12 — The doubtful numerator sign on scan 109

**Kind:** reading question; source retained. **Source:** `pages/MPL_138_090-133_138_scan109.tex`, line 43. **Brief source quote:** `f(z)\unsure{+|-}1`. **Confidence:** high for the required algebraic sign, no handwriting adjudication.

Since \((z-u)^2(z-v)^2=g(z)^2\), the displayed equality with numerator \(f(z)-1\) on its left requires \(f(z)-1\) on its right; taking the first-listed plus sign makes the two sides differ by \(2/g^2\). The proven residual factorization AR11 reinforces this reading question while the frozen plus-first uncertainty remains untouched. **Context relationship:** The conditions \(f(u)=f(v)=1\) in **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1664–1669, supply the matching context; this is a local clarification, with **EXIT_TOWER E.24** unaffected.

## AR13 — The admissible cubic has arithmetic \(S_3\) and a cube-root-of-two field

**Kind:** own exact derivation of an arithmetic implication; cubic orbit known in literature. **Source:** `pages/MPL_138_090-133_138_scan109.tex`, lines 22–26; `pages/MPL_138_090-133_138_scan112.tex`, lines 3–5. **Brief source quote:** “\(P(c)=0\)” together with “\((5c+4)^2-72c\ne0\)”. **Confidence:** high; modular irreducibility, discriminant, inverse field identities, and rigid normalization.

The cubic \(R\) has no root modulo \(7\), is therefore irreducible over \(\mathbb Q\), and has discriminant \(-5038848=-3\cdot1296^2<0\), giving one real root, two nonreal conjugates, and splitting group \(S_3\). More explicitly,
\[
c=\frac{4+18t+6t^2}{25},\qquad
t=-\frac{25c^2}{36}+\frac{31c}{18}+\frac29,\qquad t^3=2,
\]
so \(\mathbb Q(c)=\mathbb Q(t)\cong\mathbb Q[T]/(T^3-2)\) for the displayed corresponding root \(t\), and fixing the unique pole and the uniquely triple and double zeros fixes \(\infty,0,1\), proving that distinct \(c\)'s define distinct covers and that \(\mathbb Q(c)\) is their field of moduli and a field of definition. **Context relationship:** This supplies an explicit link to **Hua, modernised reading of cote 138**, “Calculs : \(z\mapsto z^n\), la fonction \(g\), Kummer sur \(\mathbb Q\),” lines 582–600, and completes his “Un arbre de degré 6,” lines 1684–1686; Jones [J], Example 7.7, already states this cubic's \(S_3\) orbit, whereas **EXIT_TOWER E.24** and **LM7_PUSH E.3** remain open problems of different scope.

## AR14 — Three oriented classes refine the two-drawing presentation

**Kind:** checked implication, independently matched to known literature. **Source:** `pages/MPL_138_090-133_138_scan106.tex`, lines 20–50. **Brief source quote:** the two labels “I” and “II”. **Confidence:** high for the passport classification; identification with the frozen tables remains conditional on AR05's reading.

With \(\rho_s=(123)(45)\), exactly eighteen involutions of type \(2^2 1^2\) give a six-cycle \(\rho_s^{-1}\sigma\), and division by the order-six centralizer gives three oriented classes: conditionally, table I and its distinct mirror, and the reflexible table II. The normalized cubic roots give the same one-real-plus-conjugate-pair structure, but no claim is made that a particular sign of the imaginary part identifies the drawing I; the independent dual-passport enumeration in `maps_moduli_certificate.json`, key `degree6_repeated_passport`, agrees with the three-class count and full automorphism orders \(2,1,1\). **Context relationship:** This refines the two examples discussed by **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1649–1654 and 1684–1686, and is already explicit in Jones [J], Example 7.7; `context/LM_140-2_text.tex`, scans 573–574, lines 16920–16930, later raises Galois action on spherical regular maps, while **EXIT_TOWER E.24** is the broader unresolved image question.

## AR15 — The localized algebra needs the \(P\)-equation and \(Q\)-invertibility separately

**Kind:** reading question and derived scheme calculation. **Source:** `pages/MPL_138_090-133_138_scan111.tex`, lines 37–41. **Brief source quote:** “\(\mathbb Q[c]_{\delta(c)c(c-1)}/P(c)Q(c)\)”. **Confidence:** high conditional on reading the displayed denominator as the principal ideal of the product.

The intended conditions produce
\[
\mathbb Q[c,1/(\delta c(c-1)Q)]/(P)\simeq\mathbb Q[c]/(R),
\]
because \(P=-\delta R/7776\) and \(c(c-1)\delta Q\) is invertible modulo \(R\). If the displayed slash instead literally means quotient by \((PQ)\) while only \(\delta c(c-1)\) is inverted, it also retains the unwanted point \(c=8/5\), where \(Q=0\), \(P=-8/125\ne0\), and \(\delta=144/5\ne0\); this creates a reading question rather than permission to replace the source display. **Context relationship:** The separately stated conditions in **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1669–1678, support the first interpretation; relative to **EXIT_TOWER E.24**, this identifies one finite cubic parameter algebra only.

## AR16 — The final logarithmic derivative suggests a general elimination method

**Kind:** checked implication of an unfinished calculation. **Source:** `pages/MPL_138_090-133_138_scan112.tex`, lines 22–35. **Brief source quote:** “\(\varphi,\psi\) … unitaires premiers entre eux … multiplicités données”. **Confidence:** high for the identity and numerator degree, not a claim of a completed general algorithm on the page.

For \(\varphi=\prod_i(z-\alpha_i)^{p_i}\) and \(\psi=\prod_j(z-\beta_j)^{q_j}\) with distinct, disjoint roots and the source's hypothesis \(\deg\varphi>\deg\psi\), logarithmic differentiation gives
\[
\frac{f'}f=\sum_i\frac{p_i}{z-\alpha_i}-\sum_j\frac{q_j}{z-\beta_j}.
\]
If there are \(a\) distinct \(\alpha_i\)'s and \(b\) distinct \(\beta_j\)'s, the numerator over their squarefree product has degree \(a+b-1\) and leading coefficient \(\deg\varphi-\deg\psi\ne0\), making its roots the remaining critical points whose images must be constrained. **Context relationship:** This supplies the missing numerator structure behind **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1687–1688, which calls it an approach by \(f'/f\); searches find no matching general elimination result in `RESULTS_STATE.md`, and **EXIT_TOWER E.24** is not proved by this method sketch.

## AR17 — The isolated critical-value implication cannot be universal

**Kind:** reading question about a surrounding conditional, not a refutation of an attributed theorem. **Source:** `pages/MPL_138_090-133_138_scan112.tex`, line 14. **Brief source quote:** “\(f'(z)=0\Rightarrow f(z)=0\)”. **Confidence:** high for failure as an unconditional statement; low for reconstruction of the intended missing premise.

For every admissible \(R\)-root, the critical points \(u,v\) instead satisfy \(f(u)=f(v)=1\), so the isolated implication is false if applied universally to the preceding family. It may belong to the nearby contradiction discussion or a discarded case, but the available frozen text does not justify silently supplying that premise. **Context relationship:** **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1676–1678, restricts its zero-value argument to the hypothetical \(P=Q=0\), which suggests a possible context and leaves this reading question open; no claim in **EXIT_TOWER E.24** is thereby refuted.

## AR18 — The intermediate reduction has algebraically determined signs

**Kind:** reading question, with a direct algebraic check. **Source:** `pages/MPL_138_090-133_138_scan108.tex`, lines 11, 15–19, 32–33. **Brief source quote:** `[(\alpha-2)\beta\unsure{+|-}(\beta+1)c]u`. **Confidence:** high for the required algebra, no new claim about the ink.

Writing \(A=(\alpha-2)(\alpha-c)+\beta+1\) and \(D=(\alpha-2)\beta-(\beta+1)c\) gives the remainder
\[
\bigl[(\alpha^3+2\alpha\beta)A+(\alpha^2+\beta)D\bigr]u
+\beta(\alpha^2+\beta)A+\alpha\beta D,
\]
so the indicated sign in \(D\) must be minus, the \(A\)-factor uses \(\alpha-c\), and the first term on line 15 needs its \(u\)-factor if the displayed multi-line expression is read literally as a polynomial. Also \(A=-(5c^2-10c-4)/36\), agreeing with the first-listed minus on line 33; all original alternatives and the missing factor remain frozen. **Context relationship:** This checks and extends the two partial reductions credited to **Hua, modernised reading of cote 138**, “Un arbre de degré 6,” lines 1673–1675, rather than treating his normalized algebra as new transcription evidence; **EXIT_TOWER E.24** remains outside the local correction.

## Primary literature checked

**[J]** Gareth A. Jones, *Regular dessins with a given automorphism group*, arXiv:1309.5219v1 (2013), Example 7.7, printed page 12, [primary PDF](https://arxiv.org/pdf/1309.5219). This exact example has the same cubic, passport, three oriented classes, arithmetic \(S_3\), and geometric monodromy \(S_6\); Jones refers further to Girondo–González-Diez, *Introduction to Compact Riemann Surfaces and Dessins d'Enfants*, Example 4.58, and Lando–Zvonkin, *Graphs on Surfaces and their Applications*, §2.2.2.3, which were not opened in this run. The symbolic and permutation certificates here were completed before finding this literature match; their role is an independent check and a completion of the supplied manuscript calculation, not a literature priority claim.

## Notation and proof boundaries

- \(P\) in AR07–AR18 means the exact remainder coefficient \(P_{\rm rem}\) of AR06; \(\widetilde P=-7776P\) is its denominator-cleared associate, and \(R\) is the cubic remaining after inverting \(\delta\).
- The arithmetic action \(S_3\) on the three parameter embeddings is distinct from the geometric degree-six monodromy group \(S_6\).
- The \(S_3\) orbit in this example does not prove faithfulness of the absolute Galois action on all maps or all regular maps, or settle any GT/CM comparison in `RESULTS_STATE.md`.
- Mathematical support for an alternate sign or index is kept in research notes; it does not resolve frozen palaeographic uncertainty.
