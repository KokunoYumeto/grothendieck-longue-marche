# Notes on the decided corrections

This is a diplomatic reading audit. Mathematical refinements from the supplied correction table are reported as such; no mathematical re-proof is claimed unless a check event explicitly says otherwise. Repeated statement ids are distinguished by cote and scan. Decisions refer to the supplied original page.

The original scans and source transcription are supplied inputs and are not duplicated in the deliverable. Crop coordinates are recorded in the review records and can be reproduced with `scripts/make_crop.py`. The runtime did not expose a numerical reasoning-effort setting; check events report this rather than inventing one.

## L1186 — cote 1, scan 004 — decision (a)

Mixed case: correct the transcription’s a to x, but preserve the author’s written R. The supplied correction proposes intended Cx subset C and calls R an author slip; that mathematical interpretation has not been independently checked in this visual review. No edit from R to C is proposed.

**Ink check:** At the start of the second line of the Gamma_1 definition the manuscript has C followed by a tiny compact crossed/forked x, then the inclusion sign, then an unmistakable R with a tall loop and diagonal right leg. The tiny x is consistent with the compact x in x in R and xC on the line immediately above. The ink therefore reads Cx subset R. Visually inspected full scan and crops/1_scan004_L1186_context.jpg and crops/1_scan004_L1186_Cx.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
Cx subset C (his slip; the transcription should keep the ink: Pro's "a(?)" is "x")
```

## L1181 — cote 1, scan 008 — decision (b)

The manuscript reads exactly as the original transcription: \varphi_{f+g}\leq\varphi_f+\varphi_g and \varphi_{fg}\leq\varphi_f\varphi_g. Preserve the author's written formulas. The supplied correction characterizes these as the author's slip and proposes \varphi_{f+g}(s+t)\leq\varphi_f(s)+\varphi_g(t) and \varphi_{fg}(s+t)\leq\varphi_f(s)\varphi_g(t), and also asserts integrated forms (10), (11) and capital-Phi subadditivity. Those mathematical assertions and its counterexample were not checked here. The row kind says misreading of ours, but its evidence expressly says his slip and transcription not in question; the visible ink supports decision b.

**Ink check:** In the final two lines of (5), the left subscripts are f+g and fg. Each inequality has a visible angled upper stroke and separate horizontal lower stroke, reading \leq. The first right-hand side has two phi symbols with f and g subscripts separated by a plus; the second has the two subscripted phi symbols adjacent. No argument (s+t), (s), or (t) is written on either line. These observations are visible in crops/1_scan008_L1181_sum.jpg and crops/1_scan008_L1181_product.jpg, inspected after enlargement and contrast adjustment.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
phi_{f+g}(s+t) <= phi_f(s) + phi_g(t) and phi_{fg}(s+t) <= phi_f(s) phi_g(t); the integrated forms (10), (11) and Phi_{f+g} <= Phi_f + Phi_g hold
```

## L1182 — cote 1, scan 029 — decision (b)

Preserve the written B∈\underline a. The supplied correction proposes B_+∈\underline a and attributes the discrepancy to the author’s definition (1); its rearrangement argument and counterexample were not mathematically checked in this visual transcription pass. Definition (1) is a pointer supplied by the correction, not a formula inspected on this page.

**Ink check:** In crops/1_scan029_L1182_condition.jpg the surviving line reads Δ(A)<+∞ ⇔ B∈a, with a underlined. The B is a large capital with two lobes; there is no plus sign or subscript attached to it. A separate earlier Δ(A)<∞ is struck through above. This agrees with the original LaTeX at the row’s place.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
Delta(A) < +inf iff B_+ in a, with definition (1)
```

## L1183 — cote 1, scan 029 — decision (b)

The original LaTeX matches the actual product identity and the deleted local corner formula, so no edit is proposed. The row’s account uses Δ^E(1_E+A), whereas the local deleted ink and original transcription have Δ_E(1_E+A_E). The supplied proposed definition via a corner determinant and trace-norm continuity is a mathematical refinement; its claim that this makes (2) and Prop. 8 hold, and its rank-one counterexample to definition (1), were not checked. References (1) and (2) are supplied pointers, not formulas inspected here; the displayed corner formula on this page is (5).

**Ink check:** In crops/1_scan029_L1183_prop8.jpg the middle line under Prop. 8 visibly reads Δ(AB)=Δ(A)Δ(B); the curved insertion pointer connects the block to A,B∈1+a with underlined a. In crops/1_scan029_L1183_corner.jpg the displayed formula is labelled (5) and reads Δ(1+A)=Δ_E(1_E+A_E), followed by E=s. Both E characters on the right-hand side are below the baseline. Long diagonal deletion strokes cross the surrounding passage, already represented by the original enclosing \deleted{…}.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
define Delta on 1+a by the corner formula (2) (Fuglede-Kadison determinant of A_E, T(E) finite), extended by continuity in trace norm; then (2) and Prop. 8 hold
```

## L1184 — cote 1, scan 031 — decision (b)

Keep the proposition’s written Tr E <= t. The supplied correction table proposes Tr E = t in a non-atomic algebra and characterizes the inequality as an author slip. That proposed mathematical refinement is carried as supplied background, not independently proved here. The later equality in the manuscript is a visual observation only.

**Ink check:** In Prop. 9, immediately under Sup, Tr E is followed by a less-than shape with a rising oblique upper stroke and a distinct low horizontal bar, then t: Tr E <= t, as transcribed. The enhanced tight crop shows that the upper part is angled, not a second horizontal equality bar. The later proof display visibly has Tr E = t under its Sup. Full scan and crops/1_scan031_L1184_prop9.jpg, crops/1_scan031_L1184_sup_condition.jpg, and crops/1_scan031_L1184_proof.jpg were visually inspected.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
sup over Tr E = t (non-atomic algebra)
```

## L1185 — cote 1, scan 036 — decision (b)

The original transcription \operatorname{Tr}E<t matches the manuscript. Preserve the written strict inequality. The supplied table calls this the author's slip and proposes \operatorname{Tr}E=t; its mathematical rationale is carried as background and has not been checked. Its reference to Proposition 9 on scan 31 is a supplied pointer, not an observation from this page or another scan inspected here.

**Ink check:** In the first line of the Proposition, the subscript below sup visibly reads Tr E < t: the relational sign has two connected arms meeting at the left, with no separate lower bar and no pair of parallel equals strokes. The line begins Delta_t(A) = sup and continues with the overwritten determinant/Delta notation and EAE. Inspected on the full scan and crops/1_scan036_L1185_sup.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
sup over Tr E = t
```

## L1187 — cote 1, scan 039 — decision (b)

Leave the existing doubtful exponent unchanged. The supplied correction table proposes omitting the exponent in the intended min–max formula, while retaining its written presence as an author slip. That mathematical correction was carried as attributed background, not proved. The visual check supports retaining the written superscript and its existing uncertainty; it does not support silently omitting it or making its digits definite.

**Ink check:** The boxed min–max formula has a visible raised group of strokes just after its closing parenthesis. crops/1_scan039_L1187_minmax.jpg locates it in the formula; crops/1_scan039_L1187_exponent.jpg shows that the small upper stroke meets the top rule of the box and the lower curved stroke is fraction-like. The ink is consistent with 1/2 but the numerator and division stroke are not cleanly separable. The original already retains this as ^{\unsure{1/2}}.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
rho_n(h) = Inf_{E_{n-1}} Sup (hx,x) for h >= 0, without the exponent (his slip; keep the exponent in the transcription, with a note)
```

## L1189 — cote 1, scan 039 — decision (b)

Preserve the written strict < and retain both original explicit +/− doubts. The supplied table proposes ≤ and the definite index m+n+1 as the intended Ky Fan inequalities; its mathematical assertion about strictness was carried as attributed background and was not checked. Mathematical expectation cannot resolve the compressed index signs. The visible single < supports an author-slip note rather than changing it to ≤.

**Ink check:** In crops/1_scan039_L1189_kyfan.jpg the second line has a single angular less-than sign between the left-hand term and the first rho on the right, with no separate lower equality stroke visible. The final sign before 1 in each left-hand subscript is compressed: the first is a dark short blob; the second is a short horizontal wedge with a slight upward end. Neither yields a securely isolated crossing vertical stroke. The original < and both m+n\unsure{+|-}1 readings remain supported.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
<= in place of <; index m+n+1 (Pro) in both lines
```

## L1188 — cote 1, scan 040 — decision (a)

The supplied original LaTeX already has an unqualified plus, whereas this row describes an earlier minus/doubt and says the plus was resolved by sense without rereading ink. The present visual check does not justify a certain plus, nor a completely certain minus: preserve the uncertainty as \unsure{-|+} at this one sign. The nearby special-case plus is an observation of written ink, not proof that the boxed sign is plus. The supplied table invokes Ky Fan and the special-case norm inequality in support of the intended plus; that mathematical rationale is attributed to the table and was not checked. This is a transcription-certainty correction while preserving a possible author slip, not a substitution of intended mathematics.

**Ink check:** The boxed Corollary 4 right-hand sign between rho_i(u) and rho_i(v) is a horizontal dark stroke with a small upward projection near its right side, but no clearly resolved downward crossing. It looks minus-like, while the upward projection prevents a secure exclusion of a very compressed plus. The separate special-case inequality immediately below has an unambiguous plus with crossing strokes. These are visible in crops/1_scan040_L1188_corollary.jpg, crops/1_scan040_L1188_sign.jpg, and crops/1_scan040_L1188_special_case.jpg; all were inspected after enlargement and contrast adjustment.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
sum_1^n rho_i(u+v) <= sum_1^n (rho_i(u) + rho_i(v))
```

## L1190 — cote 1, scan 056 — decision (a)

The original definite superscript 2 is made explicitly doubtful as 2|1; the visible raised ink is not silently removed. The supplied table proposes the unsquared coefficient rho_i and calls the discrepancy a pen or reading slip, but this review does not establish its mathematical claim. The summation-index uncertainty already in the page is preserved unchanged. The main reader also inspected the raised mark and its comparison digit; the small hooked stroke remains ambiguous between 2 and 1, so the explicit doubt is retained.

**Ink check:** The sum after the square root has a definite dark superscript mark above and to the right of rho, distinct from the dotted subscript i. The superscript has a short hooked top followed by a descending stroke and rounded terminal. Unlike the clear 2 in the immediately preceding uu* sum, it does not visibly have a broad lower return/foot. At this resolution the superscript can be read as a compressed 2 or a 1; I cannot settle the digit from the strokes. The full scan and all four listed contrast-enhanced crops were visually inspected, including a direct comparison with the preceding clear 2. Crops: crops/1_scan056_L1190_equations.jpg, crops/1_scan056_L1190_radical_coefficient.jpg, crops/1_scan056_L1190_exponent_left.jpg, crops/1_scan056_L1190_exponent_right.jpg.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
sqrt(uu*) = sum rho_i b_i-bar tensor b_i
```

## L1191 — cote 1, scan 058 — decision (b)

Retain the strict < exactly as written. The supplied correction table proposes ≤ in its place and describes the intended chain as equality; its mathematical explanation was carried as attributed background and not independently checked. The scan establishes a written strict sign, so this is not a transcription misreading.

**Ink check:** The final displayed-in-prose chain in crops/1_scan058_L1191_chain.jpg visibly has ≤ after the first norm and < after the product of the two norms. crops/1_scan058_L1191_lastsign.jpg shows the latter as an upper diagonal meeting a lower nearly horizontal arm, with no separate equality stroke below it. It reads \|u\|_1\leq\|v\|_2\|w\|_2<\|u\|_1, as in the original LaTeX. The preceding line includes the written equality of the two 2-norms and the existing cancellations in the surrounding words.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
||u||_1 <= ||v||_2 ||w||_2 <= ||u||_1 (equality)
```

## L1192 — cote 1, scan 071 — decision (c)

The original page already reads |\det(1+u)|\leq\det(1+|u|), exactly the row's requested reading. The row's account of an equality is not the current original transcription. No edit is needed. The decision is based on the observed sign, not on the table's mathematical counterexample or coefficient argument.

**Ink check:** Corollaire 4, formula circled 6, has an upper angled stroke descending to a left vertex and running right, with a separate short lower horizontal stroke: the sign is \leq, not two parallel equals strokes. This is visible in the full scan and inspected crop crops/1_scan071_L1192_determinant.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
|det(1+u)| <= det(1+|u|)
```

## L1211 — cote 1, scan 071 — decision (d)

This row corrects an earlier reader's off-page mathematical verdict, not words written in this manuscript or in the current original LaTeX. The visible reduction announcement remains as transcribed. The supplied table asserts that coefficient domination, summable zeros, and a genus lemma validate the reduction, and points to struck page 80 and K1-05 111-112. Those are attributed pointers/assertions from the table; those pages were not inspected and that mathematical claim was not checked here.

**Ink check:** Below formula circled 10, the manuscript visibly announces a proof reduction: Pour la preuve, on [struck est] ramènera au cas où u est hermitien positif, où c'est facile. Theorem 1 above announces the determinant product and genre 0. The phrase cannot work and any verdict rejecting the reduction are absent from this page. Inspected full scan and crops/1_scan071_L1211_reduction.jpg and crops/1_scan071_L1211_theorem.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
the reduction is valid: coefficient domination plus summable zeros plus the genus lemma (struck page 80, K1-05 111-112)
```

## L1194 — cote 1, scan 074 — decision (b)

Retain the author’s strongest-possible claim as written. The table’s as_the_page_reads field says (16), but both the scan and original LaTeX read circled (17); this is a discrepancy in the supplied row, not a transcription error. The table attributes a refutation to a Ky Fan inequality not implied by the stated inequalities. That mathematical assertion and its example were not independently checked here and are carried only as attributed background.

**Ink check:** The top passage writes Le système des inégalités followed by a circled 17 (the second digit has a top bar, descending stem and crossbar, not a 6 loop), then (pour m,n variables) et la conséquence (15). The following line contains semblent les inégalités les plus fortes possibles, continuing with the rho_i(u+v) bound on the next line. This agrees with the original LaTeX at the row’s place. Full scan and crops/1_scan074_L1194_claim.jpg and crops/1_scan074_L1194_number17.jpg were visually inspected.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
not the strongest: Ky Fan rho_{i+j-1}(u+v) <= rho_i(u)+rho_j(v) is not implied
```

## L1193 — cote 1, scan 075 — decision (b)

Keep the numerator r as written. The supplied correction table proposes rho_i in the numerator, citing differentiation of the logarithmic expression and consistency with the f_phi formula. That mathematical rationale is carried with attribution only; no derivative or analytic argument was checked in this visual pass. This is a written author slip according to the table, not a transcription misreading.

**Ink check:** In crops/1_scan075_L1193_derivative.jpg the numerator is a single r: a short descending stem with a horizontal shoulder to the right, without the loop, descender, or following subscript seen in the denominator’s rho_i. The same r shape occurs immediately after 1+ in that denominator. crops/1_scan075_L1193_comparison.jpg places the derivative beside the preceding log expression and confirms the original transcription A′(r)=Σ r/(1+r rho_i(u)).

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
A'(r) = sum rho_i/(1+r rho_i(u))
```

## L1570 — cote 1, scan 082 — decision (b)

Retain degrés as written in the original transcription. The flagged alternatives idéaux and classes were proposed in the supplied table from its account of material in neighboring folders; they are not supported by the observed initial and middle letter strokes here. I did not read those folders or adopt their mathematical subject matter as evidence for a letter. This decision records a visual reading of the heading, not a claim about the mathematical classification of the operators.

**Ink check:** The title word after et begins with a loop and tall ascender forming d, followed by compressed middle strokes including a conspicuous downward g-like stroke, and a short connected ending. The visible sequence supports degrés. No separate initial i or i-dot appears before the d-shaped form, and the central descender does not support classes. The surrounding heading reads Inégalités de convexité et ... remarquables d'opérateurs compacts. Inspected the full scan and crops/1_scan082_L1570_heading.jpg, crops/1_scan082_L1570_word.jpg, and crops/1_scan082_L1570_word_detail.jpg.

**Confidence:** high.

## L1195 — cote 1, scan 085 — decision (b)

Preserve all three written inequality directions and the sigma/rho order. The supplied table proposes f(1/rho) <= f(1/sigma) and rho_M...rho_n >= sigma_M...sigma_n, attributing the issue to reversal of hypothesis (5). That assertion, the numerical example, and the pointer to K1-03 notes S11-S12 are supplied background only; this page review did not inspect those other sources or independently check the mathematics.

**Ink check:** Formula (10) has reciprocal sigma arguments on the left, reciprocal rho arguments on the right, and a less-than shape over a low bar between the f-expressions, so the ink reads f(1/sigma_1,...,1/sigma_n) <= f(1/rho_1,...,1/rho_n). In the following displayed computation, the tail-product comparison after d’où visibly uses <= between rho_M...rho_n and sigma_M...sigma_n. The en vertu de line also visibly uses <= between the sigma initial product and the rho initial product. These all agree with the original LaTeX. Visually inspected full scan and crops/1_scan085_L1195_formula10.jpg, crops/1_scan085_L1195_tail_products.jpg, and crops/1_scan085_L1195_en_vertu.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
f(1/rho) <= f(1/sigma); rho_M...rho_n >= sigma_M...sigma_n
```

## L1198 — cote 1, scan 109 — decision (b)

Preserve the written assignment of ω and g to “le genre et l’ordre”, together with the boxed inequality. The supplied correction table proposes the intended interpretation ω=order and g=genus and labels the inconsistent assignment an author slip or reading issue. The scan supports the original wording; the proposed mathematical interpretation is carried with attribution only, without checking the genus/order theorem.

**Ink check:** crops/1_scan109_L1198_assignment.jpg shows “Donc, si ω et” at the right end of one line, followed by “g sont respectivement le genre et l’ordre” on the next. The words genre and ordre occur in that sequence, without deletion or an insertion exchanging them. The box beneath reads ω−1≤g≤ω. crops/1_scan109_L1198_following.jpg shows the next paragraph’s references to an integer symbol and to ω, with the original existing symbol uncertainties left untouched.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
omega = order, g = genus: order-1 <= genus <= order
```

## L1199 — cote 1, scan 110 — decision (b)

Preserve the author’s written order 1 and his qualification “sauf erreur”. The supplied correction table proposes order 1/alpha and genus 0, and points to a computation on 114. That mathematical correction is carried with attribution only; the pointed-to page was not read, and no exponent-of-convergence or order computation was checked.

**Ink check:** crops/1_scan110_L1199_order.jpg shows the product ∏(1−z/n^α), the condition α>1, and the phrase “est d’ordre” continuing on the next line as “1 (sauf erreur) et de genre 0.” The 1 is an isolated upright numeral with no fraction bar or alpha beneath it. The parenthetical “sauf erreur” is visible surviving text and already appears in the original LaTeX.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
order 1/alpha, genus 0
```

## L1196 — cote 1, scan 112 — decision (b)

Keep the written pi upper bound. The supplied correction table proposes pi/3 <= theta < pi/2 and states that positive c in Re z >= c|z| requires theta < pi/2. This proposed intended range and its mathematical justification are attributed to the table and were not independently checked in this visual review.

**Ink check:** The angle sentence visibly says entre pi/3 et pi. The first pi has a heavy fraction bar below it and a distinct denominator 3; the second pi has its top bar and two downward strokes, with blank paper below and no fraction bar or denominator 2. The next line visibly contains x >= c|z|. The original LaTeX therefore matches the written upper bound pi. Visually inspected the full scan and crops/1_scan112_L1196_angle_context.jpg and crops/1_scan112_L1196_angle_bounds.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
theta in [pi/3, pi/2[
```

## L1197 — cote 1, scan 120 — decision (b)

The manuscript reads as the original transcription; retain its stated inference from unboundedness on the unit ball to not being entire. The supplied correction calls this the author's slip and instead asserts that S is entire on l^1 while unbounded on the unit ball, citing an integral representation and local boundedness. Those mathematical claims are attributed to the supplied table and were not checked in this visual transcription pass.

**Ink check:** The final three lines of the Proposition visibly contain Cependant, a struck elle, then cette fonction n'est pas bornée / dans la boule unité de l^1, et n'est par / suite pas une fonction entière de lambda. The negation pas before une fonction entière is present, and entière is followed by de and a clear lambda. Inspected the full scan and enlarged crop crops/1_scan120_L1197_conclusion.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
S is entire (holomorphic on all of l^1) and unbounded on the unit ball
```

## L1200 — cote 1, scan 126 — decision (b)

Retain |UA|=U|A|U^{-1} as written. The supplied correction table proposes |UA|=|A| for unitary U and labels the written conjugation an author slip. That mathematical replacement is carried with attribution only; no operator-identity or determinant argument was checked in this visual pass.

**Ink check:** crops/1_scan126_L1200_conjugation.jpg shows “(car |UA|” at the right end of the penultimate line, continuing “=U|A|U^{-1}” on the final line. Both flanking U letters and the superscript −1 are clear surviving ink. The next identity similarly reads |UB|=U|B|U^{-1}. crops/1_scan126_L1200_unitary.jpg locates the preceding statement “|A+B|=U(A+B), U unitaire”. The original LaTeX follows these written forms.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
|UA| = |A|
```

## L1202 — cote 1, scan 144 — decision (a)

Mixed case. Resolve only the first relation’s existing =|<= doubt to the clearly written <=. Preserve the codimension line’s written >= signs as author text. The supplied table states that the codimension of an intersection is at most the sum and proposes <= there; this mathematical correction was not independently checked. Other existing uncertainties, including the factor argument v|u, remain unchanged because they are outside this row’s sign issue.

**Ink check:** At the first product relation, the sign after rho_(m+n-1)(vu) has an upper stroke rising from a left vertex to the right, a rightward return, and a separate lower bar: it is <=, not two horizontal equality bars. The later boxed conclusion also clearly has <=. In the codimension line the first comparison after codim(H cap E_(n-1)) has a right-facing upper angle over a lower bar, so it is >= as transcribed; the following comparison before m-1+n-1 likewise faces right. Visually inspected the full scan and crops/1_scan144_L1202_top_relation.jpg, crops/1_scan144_L1202_codimension.jpg, and crops/1_scan144_L1202_boxed_conclusion.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
<= in both places
```

## L1203 — cote 1, scan 149 — decision (b)

Preserve the original transcription, including the author's underlined décroissante assertion and the unsigned displayed expression. The supplied correction identifies these as author slips, claims the terms need not decrease, supplies a diagonal-matrix counterexample, and says the bound still follows from the Lemma's eigenvalue description. That mathematics is attributed to the table and has not been checked here. The bounds and Lemma were inspected only as written page context, not as a proof of the correction.

**Ink check:** Item 2 visibly says that the terms alpha_{n-k}(u)u^k form une suite décroissante d'hermitiens positifs; décroissante is underlined and is not struck. Its displayed inline expression for P_n(u) has a sum followed directly by alpha_{n-k}(u)u^k, without a visible (-1)^k factor. The boxed bound below visibly includes 0 <= P_n(u) <= alpha_n(u) . 1. The later Lemme writes a primed sum of products of lambda symbols and the inserted condition ne contenant pas i. Inspected full scan and crops/1_scan149_L1203_assertion.jpg, crops/1_scan149_L1203_bounds.jpg, and crops/1_scan149_L1203_lemma.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
the terms need not decrease; 0 <= P_n(u) <= alpha_n(u) holds by the Lemma (eigenvalues e_n(lambda_j, j != i))
```

## L1204 — cote 2, scan 016 — decision (b)

Preserve the written isomorphism and its existing uncertainty on “non”. The supplied correction table proposes interpreting the isomorphism only after forgetting to underlying O-Modules, and invokes Mackey’s formula for G-modules. Those mathematical qualifications are carried with attribution only; no representation-theoretic claim or supplied S_2⊂S_3 counterexample was checked. The present scan establishes the written statement, not whether a forgetful functor was tacitly intended.

**Ink check:** crops/2_scan016_L1204_isomorphism.jpg shows the injectivity condition, an inserted “fonctoriel” above the line, the compressed word already represented as \unsure{non} before “canonique”, and the displayed u^*u_*(F)≃F^{(G′/G)}. The quotient G′/G is parenthesized in superscript and the prime belongs to its first G. No written qualification to underlying O-Modules is attached to this formula. crops/2_scan016_L1204_category.jpg shows the local category being described as Modules on the topos where G acts.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
an isomorphism of the underlying O-Modules only; as G-modules Mackey's formula applies
```

## L1201 — cote 2, scan 021 — decision (b)

Retain both written exponents i. The supplied table proposes i-1, cites the next-page proof and Proposition 3, and invokes the degree-one identity and Newton’s identity. Those cross-page comparisons and mathematical assertions were not independently checked here. L1568 flags this same physical place; both rows yield no edit, so no overlapping edit is needed.

**Ink check:** At the bottom of the page, Proposition 2 writes the two compositions with a superscript i above each (-1). Each exponent consists of a single short vertical/slanted stroke with a separate dot above; neither has a following minus sign or numeral 1. The (i-1)! factors follow on the baseline. The original LaTeX (-1)^i(i-1)! therefore matches both written expressions. Visually inspected the full scan and crops/2_scan021_L1201_prop2.jpg; the same two exponents are enlarged further in the independently inspected crops/2_scan021_L1568_prop2_formulas.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
(-1)^(i-1) (i-1)! id, as in the proof on 22 and Prop. 3
```

## L1568 — cote 2, scan 021 — decision (b)

The flag does not reveal a transcription error on this page: preserve both exponents i as author text. The flag’s statements about the proof, Proposition 3, and Hua register entry 2-chern-ring-gamma-comparison are pointers/reports supplied in the table, not observations from this page; those sources were not read. Its claim that degree 1 selects the proof’s sign is unverified mathematical background. This is the same physical locus as L1201 and creates no additional edit.

**Ink check:** The suspected sign misreading was checked directly at Proposition 2: in both compositions the raised exponent after (-1) is a dotted i alone. There is no raised -1 after that i; the visible -1 belongs to the separate baseline factorial (i-1)!. Thus this page itself reads exactly the exponent i reported by the flag and transcribed in the original LaTeX. Visually inspected full scan and crops/2_scan021_L1568_prop2_formulas.jpg, with proposition context in crops/2_scan021_L1201_prop2.jpg.

**Confidence:** high.

## L1205 — cote 2, scan 029 — decision (b)

The original transcription faithfully records the four listed relations. The proposed universal lambda-relations are not omitted visible ink; inserting them would supplement the author's mathematical definition. Preserve the page. The supplied table says they are needed for a homomorphism of augmented lambda-rings, refers to page 28 and Pro note L02, and supplies a purported counterexample without them. Those assertions and pointers are attributed to the table and were not checked; no other page or note was read.

**Ink check:** The generator line shows c^i(x) with i >= 1. The brace encloses four written relation lines: c^i(1)=0; c^n(x+y) as a sum of c^i(x)c^j(y); c^n(x*y)=Q_n(...) for x,y in I(K); and c^n(E_s)=0 for n>n_s. There is no additional c(lambda^k x) relation inside that displayed list. A later bracketed explanation separately writes lambda^i(E_s)=0 for i>n_s. Inspected full scan and crops/2_scan029_L1205_generators.jpg, crops/2_scan029_L1205_relations.jpg, and crops/2_scan029_L1205_lambda_context.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
add the lambda-relations c(lambda^k x) = universal polynomial in c(x), as 28 requires (homomorphism of augmented lambda-rings)
```

## L1206 — cote 2, scan 043 — decision (b)

Preserve the displayed formula. The supplied correction table offers a rational-Picard-group qualification, and the integral statement 2c_1(f_*O_X)=−B for its branch divisor B. These are attributed mathematical refinements, not missing visible ink; they were not proved or checked here. The table’s separate c_1 expression is carried only as source-table background, not reported as observed manuscript text.

**Ink check:** crops/2_scan043_L1206_box.jpg shows the final boxed ordered pair f_!(ξ)=(nδ, nδ(1/2)k_Y+f_*(d)−nf_*((1/2)k_X)), with the divisor letters underlined. Both one-half factors are visible and the Y and X subscripts follow their respective k terms. No tensor-Q or modulo-torsion qualification is written in or next to this displayed result. The supplied row’s separate c_1(f_*O_X) expression is not separately written in the inspected page text.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
valid in Pic(Y) tensor Q, i.e. modulo torsion; integrally 2 c_1(f_*O_X) = -B (B the branch divisor)
```

## L1207 — cote 2, scan 043 — decision (b)

Preserve the heading’s written target X. The supplied correction table proposes Y as its intended target. The same page later explicitly writes f:x→Y, but that context does not change the heading’s visible X. This is an author-slip note rather than a transcription correction. No claim about a surface case was checked; that case appears only in the supplied row’s pointer.

**Ink check:** crops/2_scan043_L1207_heading.jpg shows the heading ending “dans une variété X.” The final letter has two crossing diagonal strokes and is clearly X, with no descending stem as in Y. The source-curve letter immediately before “dans” is also X after a cancellation. crops/2_scan043_L1207_targetcontext.jpg separately shows the later parenthetical f:x→Y, whose target is a distinct Y with a long descending stem.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
... dans une variete Y
```

## L675 — cote 5, scan 003 — decision (a)

Replace only the existing uncertain adjective with zariskienne; preserve its surrounding \uline and all other text. The supplied reading is supported by the observed word and the same-page z comparison.

**Ink check:** The underlined adjective following localisation has a descending cursive z-shaped initial, followed by the compressed ar/is sequence, a tall angular k-like middle stroke, and the ienne ending: zariskienne. The initial has the same descending curled form as the z in the lower X_zar diagram label; it is not a closed g-loop. Inspected full scan and crops/5_scan003_L675_phrase.jpg, crops/5_scan003_L675_word.jpg, and crops/5_scan003_L675_zar_comparison.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'isomorphismes de localisation zariskienne'
```

## L676 — cote 5, scan 003 — decision (b)

The original \xrightarrow{\approx} represents the visible arrow and equivalence mark. Preserve this author claim. The supplied table proposes instead an exact fully faithful i_* with a specified essential image, and cites J/J^2 as an O/J-module outside that image. Those mathematical assertions are attributed to the table and were not checked.

**Ink check:** The right margin says dire que, then Mod(X_zar), then a rightward arrow with two wavy approximation/equivalence strokes above it, leading to Mod(O_{X_0}). The arrow and approximation mark are explicitly visible; no fully faithful/exact qualification or essential-image condition is written in this margin note. Inspected full scan and crop crops/5_scan003_L676_margin.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
i_* : Mod(X_zar) -> Mod(O/J) is fully faithful and exact, with essential image the O/J-modules whose maps F_(U,T) -> F_(U,U) are isomorphisms
```

## L677 — cote 5, scan 003 — decision (b)

Keep connexion intégrable exactly as the original. The supplied table refines this claim by characteristic and by site: exact in characteristic zero; stratification without divided powers in characteristic p; quasi-nilpotent integrable connection on the PD site. Its cited Berthelot-Ogus 6.6 locator is expressly unverified in the table. I checked only the written words and did not inspect that source or establish these mathematical refinements.

**Ink check:** The final bracketed sentence writes dans le cas relatif lisse, includes a struck short word, and then qu'il admette une connexion intégrable. The word connexion has no inserted or adjacent quasi-nilpotente qualifier, and stratification is not written in this sentence. Inspected full scan and crop crops/5_scan003_L677_connection.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
exact in characteristic 0; in characteristic p: 'stratification' (no divided powers), 'connexion intégrable quasi-nilpotente' (PD site)
```

## L692 — cote 5, scan 004 — decision (d)

This is a bibliographic/catalogue-placement correction, not a correction to the leaf’s transcription. The identification as Serre–Tate, Good reduction of abelian varieties, section 7, the SA15-12 reused-material assignment, and the SA15-19 cross-reference are supplied by L692; the leaf alone does not display the paper title or authors, section number, or those catalogue codes. Nor can this image alone establish who supplied the mathematical symbols or lower page number. L1312 gives a different placement instruction, moved to SA15-19. Both are retained as attributed catalogue instructions; neither supplies an on-page edit. The present transcription task does not choose or execute an external catalogue reclassification.

**Ink check:** The leaf has a centered -32- at the top and a predominantly typewritten English text, with mathematical symbols filled into the typed lines. It visibly contains THEOREM 12. No separate scientific marginal commentary is visible on this scanned side. A handwritten numeral 3 is present at the lower left, already represented by the original mspage{3}; therefore a blanket claim that the page has no handwritten mark would be too strong. Visually inspected full scan, crops/5_scan004_L692_typescript_header.jpg and crops/5_scan004_L692_lower_number.jpg, and the theorem passage in crops/5_scan004_L1312_theorem12.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
5:4 is a typescript preprint page (-32-) of Serre-Tate, Good reduction of abelian varieties, §7, with nothing of his on it; reused material (SA15-12), cross-referenced to SA15-19 only
```

## L789 — cote 5, scan 004 — decision (d)

The substantive correction concerns the catalogue account of cote 100 scans 3–45 and references 100:4,5,7,9,48–51. Those locations are pointers supplied in L789 and were not inspected. Its assertion of no use of SA15-17 there cannot be decided from 5:4. The row itself leaves whether 5:4 uses SA15-17 to another part; this page review makes no such dependency claim and does not edit the transcription.

**Ink check:** The inspected 5:4 leaf contains THEOREM 12 about the conductor of an abelian variety and a final typed sentence beginning For elliptic curves. It contains no on-page statement assigning catalogue dependencies among SA15-17, SA15-16 and SA15-19. The theorem and final sentence are visible in crops/5_scan004_L789_page_context.jpg, which was inspected along with the full scan.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
on cote 100 scans 3-45 nothing uses SA15-17: no elliptic curves, no ordinary reduction, no canonical lifts; the uses are SA15-16 (Serre-Tate deformation theorem, 100:4, 5, 7) and the trait case of SA15-19 itself (100:48-51, used on 100:9). Whether cote 9 or 5:4 uses SA15-17 is for part 1.
```

## L1312 — cote 5, scan 004 — decision (d)

The requested move from documents to SA15-19 concerns catalogue placement, not on-page transcription. The attribution to Serre–Tate and characterization as good reduction of CM abelian varieties are supplied by L1312; this cropped passage does not itself state the authors or the CM hypothesis. L692 supplies a different classification as SA15-12 reused material with only an SA15-19 cross-reference. Retain both as attributed catalogue instructions; their difference has no effect on this transcription. No physical or textual move is proposed here.

**Ink check:** The visible typescript heading reads THEOREM 12 and is followed by an underlined statement about the conductor of the abelian variety A and bad reduction. The page shows no catalogue label SA15-19 or instruction moving the leaf there. The full scan and crops/5_scan004_L1312_theorem12.jpg were visually inspected; the original LaTeX already carries the theorem heading and passage.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
the 'THEOREM 12' leaf (5:4) is Serre-Tate's good reduction of CM abelian varieties: moved to SA15-19
```

## L688 — cote 5, scan 005 — decision (d)

This row replaces a source-table assessment by a broader mathematical/catalogue assessment, rather than identifying a manuscript wording to change on this page; hence d and no edit. The assigned page contains the beginning of the construction, not the table’s multi-page review summary. The table reports initiality and normal-form verification and points to results or issues on 5:27, 5:33, 5:41 and 5:45; those assertions remain attributed background and no proof or other page was checked. D2/D3 supplied in this packet have absent loci and coordinate mismatches, recorded separately; their source identifies GPT-6 Astra, not a Hua human check.

**Ink check:** crops/5_scan005_L688_initiality.jpg shows the category of artinian rings and the written sentence “On va construire un objet initial de cette catégorie.” crops/5_scan005_L688_construction.jpg shows the displayed W^{(ν)} quotient presentation and the underlined word “universel” in the following bracketed description. crops/5_scan005_L688_artinian.jpg shows the written assertion that W^{(ν)} is artinian with residue field k and the inserted maximal-ideal statement. These relevant passages agree with the supplied original LaTeX. The row’s quoted editorial classification “his text; known” does not occur in this manuscript text.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: his text, with W^(nu) (the universal Artinian ring with nu-nilpotent divided powers, 5:5-8) proved initial and its normal form verified; two of his open questions answered (5:33 carry relations suffice; 5:41 c_n = 1/prod a_i! mod p, not always 1); one wrong sign (5:27 log) and one incomplete criterion (5:45 Exemple 1)
```

## D2 — cote 5, scan 005 — decision (d)

Routing mismatch: the cited target does not occur on 5_scan005, and the correct page is not supplied in the packet. No edit is safe at an unrelated place. The source is “DM01 other_errors.tsv (GPT-6 Astra, ChatGPT Pro mode)”; it is not a Hua human check. The row also conflicts internally: should_read gives \forall, while its evidence describes cancelled “tout”. Main-reader decision: (d), no change. The main reader rechecked the full assigned scan and exact coordinate crop and searched the supplied page transcriptions; no matching target was established elsewhere. The actual destination remains unidentified. The conflicting replacement/evidence cannot be resolved from the supplied target, so neither is transferred to unrelated ink.

**Ink check:** The full assigned scan and original LaTeX contain no “on a pour … f∈R_*” locus. crops/5_scan005_D2_supplied_box.jpg uses the supplied coordinates [1115,1305,1280,1385] exactly; on this scan the box contains essentially blank paper, not a cancelled word or a forall symbol. It lies near the lower part of the artinian-ring paragraph, whose different text is visible in crops/5_scan005_L688_artinian.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
\forall
```

## D3 — cote 5, scan 005 — decision (d)

Routing mismatch: this target is not on the assigned page, and its actual page is not provided in the packet. Leave unrelated text untouched. The DM01 source identifies GPT-6 Astra, not a Hua human check. The row also conflicts internally: should_read is \deleted{que}, whereas its evidence describes cancelled phi and psi letters. Main-reader decision: (d), no change. The main reader rechecked the full assigned scan and exact coordinate crop and searched the supplied page transcriptions; no matching target was established elsewhere. The actual destination remains unidentified. The conflicting replacement/evidence cannot be resolved from the supplied target, so neither is transferred to unrelated ink.

**Ink check:** The full assigned scan and original LaTeX contain no “ce qui prouve” locus. crops/5_scan005_D3_supplied_box.jpg uses the supplied coordinates [675,1690,835,1775] exactly; here it shows ordinary cursive strokes from the phrase about omitting the relation Λ_0−λ_0, with no horizontal cancellation through a phi–psi pair. The named “ce qui prouve” passage and deleted group are absent from this page.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
\deleted{que}
```

## L678 — cote 5, scan 006 — decision (b)

Retain the original explicit \unsure{p-1|p}; no new textual change is required to represent the unresolved ink. The supplied row asks to resolve the bound to p, but the visible extra upright stroke and merged middle strokes prevent that certainty. Its argument that the struck term moved into the sum, the algebra needs alpha=p, and C_i^p denotes the binomial coefficient is attributed to the supplied correction, not used to decide the letter. This is a no-edit b outcome preserving an already doubtful transcription while declining to impose the proposed intended bound. The main reader rechecked all three crops and likewise retains the explicit doubt: the separate upright mark is real, while the crowded central ink does not settle the reading.

**Ink check:** Above the lower sum, the bound has a heavily inked p-shaped stem/loop and a separate short upright stroke immediately to its right. The dark horizontal/loop area between them is too merged to identify or exclude a minus unambiguously. The earlier Theta_i^p = at the left is visibly struck. A separate p-1 near the page top has a clearer minus and upright 1, used only as a same-page stroke comparison. Inspected full scan and crops/5_scan006_L678_sum_context.jpg, crops/5_scan006_L678_upper_bound.jpg, and crops/5_scan006_L678_pminus1_comparison.jpg.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'\sum_{\alpha=1}^{p}C_i^p\Theta_i^\alpha\lambda_i^{p-\alpha}' (C_i^p is his notation for the binomial C(p,alpha))
```

## L679 — cote 5, scan 009 — decision (b)

Keep the expansion exactly as transcribed: the visible exponents are a-prime_i and alpha_i, despite the different preceding division notation. The supplied correction table proposes q_i for the outer powers and a-prime_i for the Lambda_i factors, classifies the written line as a pen slip, and says the later lines use the correct exponents. Those mathematical assessments are attributed to the table and were not independently proved here. The observation of the following line’s symbols is only a visual/textual comparison.

**Ink check:** The preceding division line visibly writes a_i = p q_i + a-prime_i; the q has a distinct descending stroke. In the next expansion the outer exponent of (Lambda_i^p) and the outer exponent of (c_i Lambda_(i+1)) are both a-prime_i, with a small a body and separate prime mark, not q_i. The factors Lambda_i beside them have an alpha-shaped exponent with subscript i, matching alpha_i. The final factor Lambda_(i+1) in that line again has a-prime_i. The following product line visibly has Lambda_i to a-prime_i and Lambda_(i+1) to a_(i+1)+q_i. Visually inspected full scan and crops/5_scan009_L679_division_and_expansion.jpg, crops/5_scan009_L679_exponents.jpg, and crops/5_scan009_L679_following_line.jpg.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
(Lambda_i^p)^{q_i} Lambda_i^{a'_i} = (c_i Lambda_{i+1})^{q_i} Lambda_i^{a'_i}, a_i = p q_i + a'_i
```

## L1313 — cote 5, scan 010 — decision (d)

The change from divided-powers placement to reused-typescript material under SA15-12 concerns catalogue metadata rather than on-page transcription. The label reused and the destination SA15-12 are supplied by L1313; the image directly establishes the upside-down typescript and its A^5/divisor passage, not a catalogue move. The existing 9|6 foliation uncertainty remains unchanged because this row does not request a foliation edit. No mathematical claim in the typescript was checked.

**Ink check:** The scan is upside down. After rotating the relevant original-coordinate crops 180 degrees, the page shows French typewritten prose about the divisor D-div(g), including the explicit product B=A x A x A x A x A and the conclusion D=div(g). The page number 34 is also visible. This identifies the passage referenced by the row, but no SA15-12 catalogue label or moving instruction is on the page. Visually inspected the original full scan plus crops/5_scan010_L1313_typescript_rot180.jpg and crops/5_scan010_L1313_number_rot180.jpg. Enhancement for both: crop at recorded ORIGINAL pixel coordinates, rotate 180 degrees, resize with Lanczos to width 2800, then contrast x1.5.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
the upside-down reused typescript on 5:10 (a divisor of A^5): moved to SA15-12
```

## L686 — cote 5, scan 013 — decision (b)

Preserve the original active bound and its \deleted{\unsure{+1}}. The active (p-1)nu reading is clear; the exact deleted characters remain doubtful under the heavy cancellation, already represented by the existing macro. The supplied correction proposes (p-1)(nu+1) on digit-count grounds and says the limit is unaffected. Those mathematical claims are attributed to the table and were not checked; they do not authorize restoring cancelled ink or adding parentheses to the transcription. Main-reader review confirms this disposition: the active bound is legible, while the cancelled group remains covered by its existing explicit doubt.

**Ink check:** The local digit expansion visibly runs from a_0 to a_nu. The next bound reads chiff n <= (p-1)nu, followed by a small group of strokes heavily cancelled by repeated diagonal marks. That cancelled group is consistent with the original doubtful +1, but the cancellation does not permit independent high-confidence recovery of both underlying characters. No active parentheses enclosing nu+1 are written. In the ratio directly below, the numerator is again (p-1)nu with no +1. Inspected full scan and crops/5_scan013_L686_digits.jpg, crops/5_scan013_L686_bound.jpg, crops/5_scan013_L686_cancellation.jpg, and crops/5_scan013_L686_ratio.jpg.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
chiff n <= (p-1)(nu+1)
```

## L1314 — cote 5, scan 014 — decision (d)

The row changes an editorial/catalogue classification, not words to be replaced in the manuscript transcription. The visible sheet is a page-and-line proof-correction list, so the proposed description is visually supported, but the source identification “SA15-12” comes only from the supplied correction table and is not written on this page. Preserve the complete original figure and all on-page words unchanged.

**Ink check:** crops/5_scan014_L1314_pagelines.jpg shows page and line references such as p.64/l.28, p.66/l.44,49 and p.67/l.26 beside corrections, including an encircled “minuscule”. crops/5_scan014_L1314_instructions.jpg shows p.70/l.21 with underlined “Suppr. virgule !!!”, the two “le composé” entries, the correction 74→73, X_K with an encircled “K maj.”, and the final instruction to complete the bibliography with [6]. Red checking marks and long diagonal rules traverse the list. The original TikZ transcription represents this correction-sheet layout; no “divided powers” label is written on the sheet.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
a proof-correction list for another document (5:14): SA15-12
```

## L683 — cote 5, scan 017 — decision (a)

Mixed case: resolve the original transcription's X|X' and X|Y doubts to the two visible X letters. Preserve both manuscript readings. The supplied correction table calls them author slips and proposes X' in the first Hom and Y in the last; those are proposed intended readings, not the visible ink. No mathematical correction is inserted. A single contiguous find/replace span owns both small edits and preserves all intervening text, macros, and CRLF exactly.

**Ink check:** The first Hom subscript has an unprimed X: two crossing diagonals and no separate upper-right prime in crops/5_scan017_L683_first_hom.jpg. A plainly separated prime is visible beside X in the earlier alpha,beta diagram, inspected for letter comparison in crops/5_scan017_L683_xprime_comparison.jpg. The last Hom target is a heavy X with all four arms, including a distinct lower-right arm, in crops/5_scan017_L683_last_hom.jpg. The nearby Y in 'Pour tout topos Y' instead has two upper branches and one lower stem, as shown in crops/5_scan017_L683_y_comparison.jpg. The scan and all four enlarged contrast-adjusted crops were inspected visually.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
Hom_top(X', L(alpha,beta)); Hom_top(L(alpha,beta), Y)
```

## L684 — cote 5, scan 019 — decision (b)

Preserve the written omega_X^*. The supplied correction proposes omega_Y^* on mathematical typing grounds, describing this as an author slip. That intended reading and its mathematical explanation are attributed to the supplied row and were not independently proved; the decision here is based on the subscript strokes.

**Ink check:** In crops/5_scan019_L684_base_change.jpg and crops/5_scan019_L684_omega_subscript.jpg the first omega has a subscript X: two diagonal strokes cross, continuing to both lower arms. It is not a fork with a single descending stem. The second omega in the display also has X. In crops/5_scan019_L684_diagram_labels.jpg the upper arrow label has the same crossed X, whereas the lower omega label has Y with a single long descending stroke. Thus the original omega_X^* on the left of the base-change arrow matches the visible ink.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
omega_Y^*(R^i v_*(E))
```

## L680 — cote 5, scan 027 — decision (b)

The sign exponent n is clear and must remain as written. The supplied correction table proposes (−1)^{n−1}, with summation n≥1, and explains that the written sign gives −log rather than the inverse of exp. This is attributed mathematical background, not a proof checked here. Retain the existing summation-bound uncertainty because the ink does not settle its lower extra stroke. No change to the author’s sign or the bound is proposed. Main-reader review confirms the bare n exponent and retains the existing explicit bound doubt; this row is fully adjudicated without asserting that the compressed bound has been deciphered.

**Ink check:** crops/5_scan027_L680_diagram.jpg shows the upper arrow label log(1+x)=Σ(−1)^n(n−1)!x^{(n)}. The superscript on (−1) consists of a single n-shaped stroke; there is no following minus sign or 1. The next baseline factor visibly contains n−1 inside its parentheses, providing a local contrast with the bare superscript. The summation bound has a compressed >-shaped mark followed by 0, with a tiny lower stroke that does not securely distinguish > from ≥; the original \unsure{n>0|n\geq0} already records that uncertainty. The reverse arrow is labelled exp x=Σ_{n≥0}x^{(n)}.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
log(1+x) = sum_{n>=1} (-1)^(n-1) (n-1)! x^(n)
```

## L688 — cote 5, scan 027 — decision (d)

This is a source-table assessment/classification change, not a replacement of manuscript words. Preserve the on-page statements and diagram. The table’s reports about W^{(ν)}, a verified normal form, answers on 5:33 and 5:41, and a criterion on 5:45 are attributed background only; those pages and claims were not checked. Its reference to the present log sign is handled by L680 and does not justify inserting the broader assessment into the transcription.

**Ink check:** crops/5_scan027_L688_inversecontext.jpg shows the final sentence saying there are “deux isom de groupes inverses l’un de l’autre”, followed by the local logarithm diagram. The full assigned scan concerns truncated or nilpotent divided powers and these displayed maps. Neither the quoted assessment “his text; known” nor the proposed multi-page review summary is written on this page. The local log-sign matter is inspected separately under L680.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: his text, with W^(nu) (the universal Artinian ring with nu-nilpotent divided powers, 5:5-8) proved initial and its normal form verified; two of his open questions answered (5:33 carry relations suffice; 5:41 c_n = 1/prod a_i! mod p, not always 1); one wrong sign (5:27 log) and one incomplete criterion (5:45 Exemple 1)
```

## L685 — cote 5, scan 032 — decision (a)

Mixed case: resolve only the two existing \unsure{J|I} markers to the visually definite J, in the quotient-generator index and in the ideal-generator parenthesis. Preserve the author’s written x∈I, y∈A in the scaling relation and his written generator membership x∈J. The supplied table proposes x∈A, y∈I and generator membership x∈I as intended mathematics; those are author-slip corrections according to the table, not what the ink says. No divided-power argument was checked. The unique multiline find/replace preserves every intervening byte and changes only these two uncertainty macros. The main reader retained a TeX control-word delimiter after \in when removing each uncertainty macro, so the written J remains a separate token.

**Ink check:** crops/5_scan032_L685_scaling.jpg clearly reads Γ^n(xy)−x^nΓ^n(y), x∈I, y∈A: the I has upper and lower horizontal serifs, while A has its distinct triangular body. crops/5_scan032_L685_quotientindex.jpg shows x∈J in the generator indexing of B, with a long right stem and a leftward lower hook. crops/5_scan032_L685_generators.jpg shows “J idéal engendré par les Γ^n(x)” followed by “(n≥1, x∈J)”; crops/5_scan032_L685_generatorindex.jpg enlarges that second J and shows its right stem turning left at the bottom. The two hooked generator letters are distinct from the scaling line’s serif I.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
x in A, y in I; generators x in I
```

## L688 — cote 5, scan 033 — decision (d)

L688 refines a broad source-table assessment rather than specifying a replacement for manuscript text. The local question about sufficiency of the carry relation remains a question in the ink, as the original transcription records. Preserve the page and its existing uncertainty macros unchanged. The assertion that the carry relations suffice is supplied by the correction table, not established by this visual check; its claims and pointers concerning other scans likewise were not checked.

**Ink check:** The full scan and crops/5_scan033_L688_relations_question.jpg show the handwritten question Quelles sont les relations?, including a separate question-mark stroke and dot. In crops/5_scan033_L688_carry_question.jpg the lower-left marginal note visibly asks On se demande s'il suffit and is followed by the p-th-power relation Gamma^{p^nu}(x)^p = ((p^{nu+1})!/(p^nu!)^p) Gamma^{p^{nu+1}}(x). The note is written diagonally beneath the displayed relations and has a large question mark in its preceding lines; it does not contain an affirmative answer to the sufficiency question. These are the on-page passages corresponding to the supplied row's 5:33 pointer. The row's quoted label his text; known does not occur in the page LaTeX.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: his text, with W^(nu) (the universal Artinian ring with nu-nilpotent divided powers, 5:5-8) proved initial and its normal form verified; two of his open questions answered (5:33 carry relations suffice; 5:41 c_n = 1/prod a_i! mod p, not always 1); one wrong sign (5:27 log) and one incomplete criterion (5:45 Exemple 1)
```

## L1315 — cote 5, scan 034 — decision (d)

This is a catalogue/topic-classification correction, not a replacement for text present in this page's transcription. The visible typewritten leaf directly supports identifying 5:34 as a passage about quasi-functions on an abelian variety. The table's placement in SA15-12, its description of the leaves as isolated, and its association with a height-type estimate at 5:36 remain supplied catalogue assertions. Neither that catalogue entry nor scan 5:36 was inspected. Preserve the entire original page, including its existing 41 and 33 page markers.

**Ink check:** The scan is a leaf of typewritten/printed text with mathematical notation. The inspected crop crops/5_scan034_L1315_topic.jpg clearly contains 'de la quasi-fonction principale' and 'Soit A une variété abélienne définie sur K'. These phrases already occur in the original LaTeX. The upper-right printed 41 and lower-left handwritten 33 are visible in crops/5_scan034_L1315_printed_number.jpg and crops/5_scan034_L1315_handwritten_number.jpg, matching the existing page markers. No 'divided powers' heading or SA15-12 catalogue identifier appears on this leaf. The full scan and all three enhanced crops were inspected.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
isolated printed leaves (5:34 quasi-functions on an abelian variety; 5:36 a height-type estimate): SA15-12
```

## L1315 — cote 5, scan 036 — decision (d)

The supplied row replaces a catalogue/topic classification, not text occurring in this page. The visible estimate passage and the physical typescript are consistent with the row's description of 5:36, but the particular height-type identification and assignment to SA15-12 are supplied catalogue claims, not on-page titles. The row's 5:34 pointer was not inspected. Preserve the entire transcription unchanged.

**Ink check:** The full scan is a leaf of regular typewritten French prose with mathematical symbols entered among it; it begins mid-sentence and contains no title identifying a work or author. In crops/5_scan036_L1315_printed_estimate.jpg the passage visibly contains the absolute-value bounds |phi(m)| <= d, |phi(2m)-2phi(m)| <= d and the displayed recurrence expression with 2^h. In crops/5_scan036_L1315_folio39bis.jpg the top-right foliation clearly reads 39 bis; the full scan also shows handwritten 35 at lower left, both already represented in the original LaTeX. No on-page SA15-12 identification or divided-powers heading is visible.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
isolated printed leaves (5:34 quasi-functions on an abelian variety; 5:36 a height-type estimate): SA15-12
```

## L687 — cote 5, scan 039 — decision (a)

Resolve the original m|n doubt to n from the letter forms, independently of the table's mathematical-consistency rationale. This agrees with the supplied correction. Only the uncertainty marker at this factorial is changed; the rest of the valuation calculation and page are preserved. The assigned row is in section b), with no visible Proposition 6 label on this page.

**Ink check:** The questioned factorial occurs in the c_n valuation line of section b), inspected in crops/5_scan039_L687_valuation.jpg and crops/5_scan039_L687_factorial.jpg. Its opening parenthesis curves down on the left and meets or nearly meets the letter's left foot; that curve can create the impression of an extra letter stroke. Separating the parenthesis, the letter has one internal down-up turn and a rightward falling tail, matching the n in the nearby n! denominator and n=p phrase (crops/5_scan039_L687_n_comparison.jpg and crops/5_scan039_L687_n_equal_p.jpg). The same-page m=p and m! forms show two internal down-up turns (crops/5_scan039_L687_m_equal_p.jpg and crops/5_scan039_L687_m_comparison.jpg). The visible reading is n!. The following fraction also visibly has n in its numerator. The full scan and all six enlarged contrast-adjusted crops were inspected.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
nu_p((pn)!) - p nu_p(n!) - 1
```

## L688 — cote 5, scan 041 — decision (d)

The proposed multi-page assessment replaces a source-table classification, not manuscript wording, so no page edit is appropriate. Preserve the author’s written question. The supplied table proposes c_n≡1/∏a_i! mod p and says it is not always 1; that is an attributed answer from the table, not text found on the scan and not a result proved in this pass. The table’s further initiality, normal-form and other-page claims remain attributed background outside this page’s visual check.

**Ink check:** crops/5_scan041_L688_coefficient.jpg shows c_n multiplying the displayed product x^{a_0}π(x)^{a_1}π²(x)^{a_2}⋯π^r(x)^{a_r}. crops/5_scan041_L688_question.jpg shows the bracketed request to know c_n mod p, calls it an element of F_p^*, and ends with the visible question “Est-ce tjs 1?” followed by the closing bracket. The question mark is explicit; no answer or product-of-factorials formula is appended. The original LaTeX already preserves this wording and its interrogative status.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: his text, with W^(nu) (the universal Artinian ring with nu-nilpotent divided powers, 5:5-8) proved initial and its normal form verified; two of his open questions answered (5:33 carry relations suffice; 5:41 c_n = 1/prod a_i! mod p, not always 1); one wrong sign (5:27 log) and one incomplete criterion (5:45 Exemple 1)
```

## L681 — cote 5, scan 045 — decision (b)

Preserve the written n!A. The supplied row proposes n! pi A, equivalently requiring pi^n/n! to belong to pi A, and supplies a counterexample to the written criterion. These are mathematical corrections to the author's statement; the scan does not show the additional pi. No counterexample or divided-power criterion was independently proved here.

**Ink check:** In crops/5_scan045_L681_condition.jpg, the condition reads pi^n in n!A for all n >= 2. After the handwritten n are the separate factorial stroke and dot, followed directly by the two slanting sides and crossbar of A. There is no intervening pi, insertion mark, or added factor. The wider crops/5_scan045_L688_exemple1.jpg locates this formula in Exemple 1 after the words leur existence equivaut au fait que, as in the original LaTeX.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
existence iff pi^n in n! pi A (pi^n/n! in pi A) for all n >= 2
```

## L688 — cote 5, scan 045 — decision (d)

L688 revises a broad source-table assessment rather than manuscript wording. Its local pointer to an incomplete criterion in Exemple 1 concerns the same written n!A condition inspected for L681, which remains unchanged because the ink is clear. Initiality, normal-form, carry-relation, coefficient, and logarithm claims about other pages remain attributed background; those pages were not read for this assignment.

**Ink check:** The full scan and crops/5_scan045_L688_exemple1.jpg show the underlined heading Exemple 1, the assumption that A is torsion-free over Z, the relation pi^n = n! pi^{(n)}, and the existence statement containing pi^n in n!A for all n >= 2. The narrow crops/5_scan045_L681_condition.jpg confirms the absence of pi before A. The supplied row's label his text; known and its broad retrospective assessment do not occur on this manuscript page.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: his text, with W^(nu) (the universal Artinian ring with nu-nilpotent divided powers, 5:5-8) proved initial and its normal form verified; two of his open questions answered (5:33 carry relations suffice; 5:41 c_n = 1/prod a_i! mod p, not always 1); one wrong sign (5:27 log) and one incomplete criterion (5:45 Exemple 1)
```

## L1316 — cote 5, scan 046 — decision (d)

This row changes a supplied catalogue/topic description, not a phrase in the page transcription. The original LaTeX already transcribes the displayed differentials passage and proposition. The supplied sweep-2 SA15 correction identifies the sheet as an EGA typescript, links 5:46 with 5:48, and calls the rings complete; those identifications are attributed to the supplied row, not independently established here. In particular, the visible proposition says preadic topologies; no completeness condition is inserted into the transcript. Page 5:48 was not read. Preserve the whole page unchanged. Both crops use Pillow LANCZOS enlargement to 2800 pixels across and contrast factor 1.6.

**Ink check:** The full scan is a corrected typescript. In crops/5_scan046_L1316_differentials.jpg the typed words are “module de différentielles analytiques” and the reference is (18.13.1); the formula has a barred Omega with superscript 1, not divided-power notation. In crops/5_scan046_L1316_proposition.jpg the underlined heading is Proposition (18.13.5), followed by “Soient A un anneau topologique”; the visible hypotheses say “semi-locaux noethériens” and “topologies préadiques”. Handwritten additions and cancellations appear around the typed hypotheses. No heading or sentence “divided powers” occurs on this page.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
an EGA typescript on differentials of complete semi-local rings (5:46, 5:48): SA15-12
```

## L1316 — cote 5, scan 048 — decision (d)

The correction changes catalogue description/placement, not text that occurs in this page's transcription. Retain the original page unchanged. The visible text establishes a typescript discussing differential modules over a semi-local noetherian ring with its r-preadic topology. The fuller description 'EGA typescript on differentials of complete semi-local rings', its grouping with scan 5:46, and placement SA15-12 are supplied-table assertions. This single-page review does not establish the provenance, the companion-page association, or a completeness hypothesis beyond the actual wording inspected here.

**Ink check:** The assigned scan is typewritten text with handwritten corrections. Its header reads '- IV-977 -22-' (crops/5_scan048_L1316_header.jpg), and the body begins with section (18.13.4). The inspected passage expressly says that B is an 'anneau semi-local noethérien, muni de sa topologie r-préadique' (crops/5_scan048_L1316_semilocal.jpg). The displayed (18.13.4.1) uses Hom_B of the barred differential module and Der_A(B,L), followed by a handwritten continuous-derivations equality (crops/5_scan048_L1316_differentials.jpg). These visible features support a topic identification concerning differentials and semi-local rings and are already represented in the original LaTeX. The full scan and all three enhanced crops were visually inspected; no 'divided powers' heading or SA15-12 identifier is visible on this page.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
an EGA typescript on differentials of complete semi-local rings (5:46, 5:48): SA15-12
```

## L689 — cote 5, scan 049 — decision (a)

L689 owns the only physical edit on this page: add the omitted small preposition with explicit accent uncertainty, giving Lettre \unsure{à|a} \unsure{Deligne}. The table proposes definite à and cites a comparison on 5:3; that other page was not read in this single-page review. The visible hook supports a/à but the available scan does not let this reader certify the accent. L1324's overlapping heading/surname matter is handled without a duplicate edit. No writer, date, or letter-body claim is inferred from this small addition. Main-reader review of the enlarged hook and crease also leaves the accent unresolved; the explicit doubt is the final diplomatic decision.

**Ink check:** The two-line upper-right docket is visible in crops/5_scan049_L689_heading.jpg. Between 'Lettre' and the surname there is a separate small dark open hook, omitted from the original LaTeX. It is clear in crops/5_scan049_L689_preposition.jpg and crops/5_scan049_L689_preposition_fullheight.jpg. Its open-loop form is compatible with the a in the second line's p-adiques (crops/5_scan049_L689_a_comparison.jpg). A faint trace above the small hook lies close to the paper crease and cannot securely be identified as an accent. The surname has a tall initial, loop/ascender and descending g-like stroke, but its compressed final strokes remain less secure; the existing Deligne doubt is retained. The full scan and all listed enhanced crops were inspected.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'Lettre à Deligne / sur coh. p-adiques'
```

## L690 — cote 5, scan 049 — decision (d)

The phrase 'another's letter; known' is not text in the original LaTeX. The row corrects attribution and historical/mathematical assessment of the letter rather than this cover's transcription. Its assertions of the writer, 10 Dec 1965 date, unsigned typed file-copy status, and identification of the docketing hand depend on the supplied table and its pointer to 5:49-51; only 5:49 was inspected here. The small docket correction is owned by L689.

**Ink check:** The full page is essentially blank apart from the short upper-right handwritten docket and the lower number 48. In crops/5_scan049_L690_docket.jpg the docket says 'Lettre', then the small a/à hook and a surname consistent with the existing doubtful Deligne, followed by 'sur coh. p-adiques'. There is no date, address, signature, typed letter text, or duality argument on this assigned leaf. This crop and the full scan were visually inspected.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
his letter to Deligne of 10 Dec 1965 (unsigned typed file copy; docket in his hand); the duality part is right, with smooth base change as the ingredient that replaces relative purity
```

## L691 — cote 5, scan 049 — decision (d)

The row's quoted assessment is absent from the original page and concerns attribution, the associated programme, and later mathematical history. Its 5:49-53 and cote 4 Lemma 8.4.3 references are supplied pointers, not material inspected here. The own-letter attribution and later-work conclusions are retained only as table assertions. L689 owns the shared docket edit; this row makes no second change.

**Ink check:** Inspection of the full scan and crops/5_scan049_L691_docket.jpg shows only the brief handwritten 'Lettre [a/à] [Deligne?] / sur coh. p-adiques' docket, with the isolated hook and compressed surname strokes described under L689. The page has no programme, letter-body discussion, constant-coefficient claim, Poincaré lemma, characteristic-p remark, or cited lemma statement.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
his programme and his own letter to Deligne (5:49-53); the letter's doubts (constant-coefficient rigid cohomology, rigid Poincaré lemma) are confirmed by later work; its char-p remark is Lemma 8.4.3 of cote 4
```

## L1324 — cote 5, scan 049 — decision (c)

The ORIGINAL LaTeX already supplies this row's requested cover wording and explicitly marks the surname uncertain, so no second edit is needed for L1324. The row's abbreviated quotation omits the small a/à hook; L689 alone owns the addition of that visible material. Retaining the surname doubt does not establish who wrote the letter or who docketed it. The main reader also retains the existing surname doubt after inspecting the enlarged ending.

**Ink check:** The heading crop crops/5_scan049_L689_heading.jpg and the inspected tighter surname crop crops/5_scan049_L1324_surname.jpg show the surname's tall initial and ascender, a descending g-like stroke, and closely joined, partly faint final strokes. 'Deligne' is plausible but its ending is not secure enough to remove the original \unsure{Deligne}. The second line reads 'sur coh. p-adiques'. The isolated hook before the surname is separately recorded under L689.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
its cover (5:49) reads 'Lettre Deligne / sur coh. p-adiques' (surname marked uncertain at the final letters by the note)
```

## L693 — cote 5, scan 050 — decision (b)

Preserve n=dim X, as the supplied row itself requests. The row proposes n=dim Y as the intended parameter and explains this by the local induction step; this is attributed mathematical background, not grounds for changing the visibly typed X. The visual check does not establish the validity of that argument.

**Ink check:** In crops/5_scan050_L693_dimX.jpg the typewritten induction parameter is n=dim X. The final capital has crossing diagonals with upper and lower serifs, not the fork and single lower stem of Y. The wider crops/5_scan050_L693_induction.jpg includes clear Y letters in Se localisant sur Y and dim(Y-y), providing on-page comparators. It also shows a blank interval between dim(Y-y) and n; no comparison sign is clearly visible in that interval, matching the original LaTeX spacing.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
keep the typed 'dim X'; note that the argument needs n = dim Y
```

## L1317 — cote 5, scan 050 — decision (d)

This is a catalogue/topic correction, not an on-page replacement. The letter salutation and duality subject are directly visible; the docket label Lettre Deligne and proposed new item SA15-20 are supplied by the correction table. No other leaf, docket, catalogue, or author attribution was checked. Preserve the original page text.

**Ink check:** The full scan and crops/5_scan050_L1317_letter_opening.jpg show the typewritten salutation Cher Deligne, the handwritten date 10.12.1965, and an opening proposal concerning la demonstration du theoreme de dualite and avoiding recours au theoreme de purete relative. These support identification of the visible passage as a letter addressed to Deligne discussing duality. The docket wording Lettre Deligne and catalogue number SA15-20 do not appear on the inspected face of this page.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
the duality part of the letter docketed 'Lettre Deligne' (5:50): new item SA15-20
```

## L707 — cote 6, scan 002 — decision (d)

The supplied row refines a broad catalogue and mathematical assessment rather than identifying a mistranscribed phrase on this page. Preserve the whole transcription. This page itself supports the salutation John, date, folio 1, chapter heading, nilpotent closed-immersion condition and cartesian-section definition. The surname Tate, full letter range 6:2–32, folios 1–30, Pisa letterhead on 6:3 and later chapter ranges come from the supplied sweep-3 SA15 table; no other page was inspected. The table calls the construction the infinitesimal site and discusses later claims and divided-power refinements; those are background assertions, not text to interpolate here. The quoted later margin “faute d’introduire les puiss. div.” is not present on this page. All four crops use Pillow LANCZOS enlargement to 2800 pixels across and contrast factor 1.6.

**Ink check:** The full scan is a typescript with handwritten corrections. In crops/6_scan002_L707_date_folio.jpg the top-right handwriting reads “Pise, Mai 1966” and a separate numeral 1 marks the folio. In crops/6_scan002_L707_letter_opening.jpg the salutation is “Cher John,”; the opening says “un projet de théorie, ou plutôt” followed by inserted “de” before “début de théorie”, and the underlined heading is “Chapitre 1” / “La notion de cristal.” In crops/6_scan002_L707_nilpotent_thickenings.jpg, paragraph 1.0 defines C using R-préschémas T sous S; the arrows run S to T, and the typed condition is “une immersion fermée définie par un idéal localement nilpotent”. This passage contains no divided-power condition. In crops/6_scan002_L707_crystal_definition.jpg, Definition 1.1 calls a crystal of quasi-coherent modules “une section cartésienne de la catégorie fibrée précédente au dessus de C”. These are already represented in the original LaTeX.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: 6:2-32 is a typescript letter to John Tate ('Cher John', 'Pise, Mai 1966', Pisa letterhead 6:3), folios 1-30; chapters 1-2.3 (6:2-21) define crystals on the infinitesimal site (nilpotent thickenings, no divided powers); 1.5-1.17 true as stated for that site (slips corrected), the key test of 1.17 fails in characteristic p (his margin: 'faute d'introduire les puiss. div.'), and 2.1-2.2 (de Rham cohomology is a crystal) hold only with divided powers (Berthelot 1974)
```

## L696 — cote 6, scan 005 — decision (b)

Preserve the author-written de R dans S. The supplied correction proposes de S dans R and cites the closed-subscheme setting; that is the intended mathematical reading reported by the table, not the visible order of the letters. The on-page preceding phrase S fermé dans R was visually checked, but the mathematical assertion and the cited Pro note 005.5 were not independently verified.

**Ink check:** The typescript in crops/6_scan005_L696_R_dans_S.jpg unmistakably reads de R dans S: the first capital has the upright stem, upper loop and diagonal leg of R, and the second is the curved S. Neither capital is struck out or replaced. The wider crops/6_scan005_L696_definition_context.jpg includes the preceding words S fermé dans R and the formula V(J^{n+1}), while the following neighborhood phrase still reads de R dans S. The nearby corrections to the neighborhood symbol do not alter these two words.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'de S dans R' (correction 3)
```

## L697 — cote 6, scan 006 — decision (b)

Preserve \underline F_R as an author/typescript slip. The supplied correction recommends F_S and reports agreement with Michel Hua's 'F_R read F_S' (correction 4). That recommendation is recorded as an intended mathematical correction, but cannot be applied as a diplomatic transcription repair because the typed ink plainly reads R. This is the explicit ink-based exception to applying the reported Hua change. The rationale about objects over S with their unique stratification is attributed to the supplied table, not proved here.

**Ink check:** The equivalence sentence visibly ends 'à la catégorie F_R elle même' in crops/6_scan006_L697_equivalence.jpg. The enlarged target in crops/6_scan006_L697_target.jpg has a straight left stem, a closed upper bowl, and a separate descending diagonal leg: it is an unambiguous typewritten capital R, with no cancellation or inserted S. The preceding 'objets de F_S munis' has a clearly curved S subscript, inspected in crops/6_scan006_L697_s_comparison.jpg. The original \underline F_R therefore reflects the actual ink. The full scan and all three contrast-enhanced crops were inspected visually.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'à la catégorie F_S' (correction 4)
```

## L698 — cote 6, scan 007 — decision (b)

Preserve the written caractéristique nulle. The supplied correction proposes the stronger hypothesis that R is a Q-scheme and offers a counterexample over Z[x]. That refinement and counterexample are mathematical background attributed to the supplied table, not a different reading of the typescript.

**Ink check:** The full scan and crops/6_scan007_L698_characteristic.jpg show et si R at the end of one typed line and est de caractéristique nulle, alors une stratification at the start of the next. The words caractéristique nulle are clear and are not struck out or replaced. No Q-schéma wording or related insertion appears at this locus.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'si R est un Q-schéma' (correction 5)
```

## H0495 — cote 6, scan 007 — decision (d)

The supplied row is explicitly a second-model suggestion not checked by a person. Its alleged note has no corresponding visible ink on this supplied scan, so it must not be inserted. Decision d records text not found on the assigned page; no alternate page or source location is inferred. Preserve all existing insertion/deletion macros, the lower-left insertion, and the page margins unchanged.

**Ink check:** No d’après Mumford elle l’est annotation is visible on the supplied page face. In crops/6_scan007_H0495_hypothesis_margins.jpg, the lissité paragraph and both lateral margins are visible: the typescript has hypothèse inserted above a struck word, while the adjacent margin has pale paper-watermark shapes but no such ink note. In crops/6_scan007_H0495_visible_margin_note.jpg the actual lower-left marginal insertion reads compatible aux puissances p.ièmes, already represented by the existing inserted macro. In crops/6_scan007_H0495_upper_addition.jpg the actual upper insertion begins du moins si R loc.noeth. and ends aux Modules cohérents, also already represented. Full-page inspection likewise does not reveal the proposed Mumford phrase.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
an ink margin note « d'après Mumford elle l'est »
```

## L694 — cote 6, scan 009 — decision (b)

Preserve the missing p in the first VF relation as an author/typescript slip. The supplied sweep-3 SA15 row proposes VF = p.id_{M^(p)} and reports that Michel Hua noted the same omission; the visual finding agrees with the row’s account that p is missing in the typescript itself. That intended mathematical correction is not inserted into a diplomatic transcript. The cited 1.12 on 6:11 was not inspected. The two crops were enlarged with Pillow LANCZOS to 2800 pixels across and contrast factor 1.6.

**Ink check:** In crops/6_scan009_L694_weight_one_relations.jpg the first equation has a plainly typed p and point between the equals sign and id_M. In the second equation, VF = is followed directly by id with M(p) below; the intervening space contains no p, point, insertion mark or cancelled p. Thus the typed line reads FV [cancelled ink] = p. id_M, VF = id_M(p), as transcribed. In crops/6_scan009_L694_weight_i_relations.jpg the later line separately has p with superscript i before id in both equations. The full scan also shows the earlier handwritten insertion “de poids 1”.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
VF = p.id_{M^(p)} (correction 1)
```

## L695 — cote 6, scan 009 — decision (b)

Preserve the sentence ending “de poids 1” as an author/typescript slip. The supplied sweep-3 SA15 row proposes “de poids 2” and explains that an earlier weight correction was not carried into this sentence. The earlier visible correction does not overwrite or alter the later clear numeral 1. The table’s intended weight and supporting claims about T^1, 1.12 (6:12) and 2.2 (6:21) remain attributed background; those other pages were not inspected. All three crops use Pillow LANCZOS enlargement to 2800 pixels across and contrast factor 1.6.

**Ink check:** In crops/6_scan009_L695_tensor_sentence.jpg the sentence begins with “de poids 2i” and ends on the next line with “bicristal de Tate de poids 1.” The final character has the straight stem and broad horizontal foot of the typed numeral 1, unlike the curved diagonal form of the 2 in 2i; there is no cancellation or handwritten replacement at this final 1. In crops/6_scan009_L695_corrected_weight.jpg the preceding definition has a handwritten 2 crowded before the typed i, with a separate circled 2i in the left margin. In crops/6_scan009_L695_tate_maps.jpg the displayed F and V each carry the same typed p with superscript i. The original LaTeX preserves both the corrected 2i definition and the uncorrected final 1.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'... du bicristal de Tate de poids 2' (T^1, F = V = p) (correction 2)
```

## H0496 — cote 6, scan 010 — decision (a)

The unverified second-model suggestion was decided from the actual ink and is confirmed. Replace only the contents of the existing deleted span, including both visible parentheses, and retain the cancellation with \deleted{(sauf erreur)}. The words remain deleted text; they are not restored as active prose. No mathematical assertion about the surrounding functor was checked.

**Ink check:** Between 'est' and the underlined 'pleinement fidèle' there is a typewritten parenthesis covered by diagonal handwritten cancellation strokes. In crops/6_scan010_H0496_context.jpg and the tighter crops/6_scan010_H0496_struck_words.jpg, the underlying type shows an opening parenthesis, the s-a-u-f sequence (including the tall serifed f), a word gap, and the e-r-r-e-u-r sequence ending at a closing parenthesis. The diagonal cancellation does not erase the typewritten baseline and the repeated r shapes. The reading is '(sauf erreur)', not the original uncertain 'évidemment'. The full scan and both enhanced crops were visually inspected.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
the struck words are « (sauf erreur) », typed and struck in ink
```

## L699 — cote 6, scan 013 — decision (b)

Preserve “stratifiés relativement à X_K” as a clear author/typescript slip. The supplied sweep-3 SA15 row proposes “relativement à K”, explaining that the relevant base is the field K, and reports agreement with Michel Hua’s project. This is an intended mathematical correction; the observed second X_K has not been cancelled or replaced in the scan. No exception to a contrary ink reading is involved: the row itself records the written X_K. The mathematical argument and the reference to 1.8 are carried only as attributed table background. Both crops use Pillow LANCZOS enlargement to 2800 pixels across and contrast factor 1.6.

**Ink check:** In crops/6_scan013_L699_relative_base.jpg the line reads “Modules cohérents [struck stratifiés] sur X_K, stratifiés relativement à X_K.” Both occurrences have a full-size X with two crossing diagonal strokes and a separate capital K lowered to its right as a subscript. The second X is clear, uncancelled and not an insertion mark; it is not merely K. The strikeout is over the earlier word stratifiés, before sur, and does not extend to the relative-base expression. In crops/6_scan013_L699_field_context.jpg the next context separately says “comme ici K est de caractéristique nulle” and has the inserted words “et X_K lisse dessus”. The relative-base expression in the original LaTeX matches the visible X_K.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'stratifiés relativement à K' (correction 6)
```

## L1318 — cote 6, scan 016 — decision (d)

This row changes a catalogue/topic description rather than wording present in the page's transcription. The visible heading and 'pour chaque nombre premier' definition directly support the topic description 'bicrystals at every prime'. Preserve the original LaTeX. The SA15-2 placement is supplied by the correction table and is not independently established by this page inspection.

**Ink check:** The inspected crop crops/6_scan016_L1318_heading_and_primes.jpg shows the underlined heading '1.15. Bicristaux et biisocristaux sur une base quelconque'. The following lines visibly say 'Pour chaque nombre premier p', introduce S_p, and give for each p a bi-crystal structure through F_p,V_p. These words and symbols already appear in the original LaTeX. The full scan and the enhanced heading/definition crop were inspected. No SA15-2 catalogue label or 'crystalline site' heading appears on the leaf.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
bicrystals at every prime (6:16): SA15-2
```

## H0497 — cote 6, scan 016 — decision (d)

The second-model row is explicitly not checked by a person. Its alleged margin note is absent from the visible assigned page, so it must not be inserted into this transcription. Decision d records that the suggested text has no located span on 6:16; it does not assert that the text belongs on any other page. No alternative destination is inferred or proposed. The main reader also inspected the full scan and all four margin bands and confirms the absence on this supplied page. Preserve the original page unchanged. The source-location discrepancy remains documented; decision (d) is final and no unadjudicated page decision remains.

**Ink check:** No margin wording corresponding to 'il faudrait faire le lien avec ce ... Cartier !' is visible on the assigned scan. The full page was inspected, then four overlapping enhanced horizontal bands preserving both side margins and the top/bottom edges were inspected: crops/6_scan016_H0497_margins_top.jpg, crops/6_scan016_H0497_margins_upper_middle.jpg, crops/6_scan016_H0497_margins_lower_middle.jpg, and crops/6_scan016_H0497_margins_bottom.jpg. The upper-right handwriting is the number 14, and the lower-left handwriting is 15. The side margins show the pale paper watermark, minor specks/staining, and no multiword ink note. Small handwritten corrections within the typed body do not form the alleged wording. No note-specific tight locus could be made because no such note was found; the bands document the complete inspected margin coverage.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
an ink margin note « il faudrait faire le lien avec ce … Cartier ! »
```

## L710 — cote 6, scan 018 — decision (b)

Preserve the written S-prime and its existing inserted macro. The supplied row proposes unprimed S as correction 13 on mathematical grounds; the enhanced crop instead confirms that the author typed a separate prime before the closing quotation mark. The site-theoretic rationale is attributed to the table and was not independently proved.

**Ink check:** In crops/6_scan018_L710_inserted_value.jpg the inserted typed phrase reads valeur en S-prime, followed by its closing quotation marks and de. There is a distinct single raised mark immediately after S, separated from the following pair of raised strokes forming the closing quotation mark. Thus the prime is actual ink, not merely one stroke of the quotation mark. The insertion is joined by an ink guide to the gap after comme; crops/6_scan018_L710_context.jpg locates it above the R^i f_cris* expression and also shows f:S-prime to S in the same passage.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
'valeur en S' (correction 13)
```

## L700 — cote 6, scan 020 — decision (b)

Preserve the written assertion unchanged. The supplied sweep-3 SA15 row proposes a mathematical qualification and a different derived-category formulation; those are not visible corrections or omitted words in this passage. Its reference to smoothness over a perfect field, its discussion of kernels in O_C-modules, and the perfect-field unit-crystal example are carried only as attributed table background, not as conclusions of this visual review. The table reports that Michel Hua’s project raised the issue; this does not supply contrary written ink. The reference to 1.13 was not independently checked. Both crops use Pillow LANCZOS enlargement to 2800 pixels across and contrast factor 1.6.

**Ink check:** In crops/6_scan020_L700_abelian_assertion.jpg the uncancelled typescript reads “Comme les cristaux de modules sur un préschéma S forment une catégorie abélienne, on peut prendre la catégorie dérivée; ses objets seront appelés simplement” followed by “complexes de cristaux”. No condition of smoothness or a perfect base field is inserted into that sentence. In crops/6_scan020_L700_deletion_boundary.jpg the preceding definition beginning “On ... désigne” is enclosed and crossed by deletion strokes through its final words “base variable,”; the boundary turns up before Comme and does not cancel the assertion about crystals. The original LaTeX correctly ends its deleted passage before the quoted assertion.

**Confidence:** high.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
true for S smooth over a perfect field (1.13: stratified modules on smooth lifts); in general crystals are not closed under kernels in O_C-modules, and one works in the derived category of O_C-modules with crystal cohomology (correction 7)
```

## L708 — cote 6, scan 028 — decision (d)

The requested refinement is an external source-table assessment. The on-page turn to isocrystals, conjectural wording, diagonal cancellation, and marginal rejection are already represented in the original LaTeX; preserve all author text, deletion boundaries, margin macros, and existing doubts unchanged. The confidence qualification concerns only the small existing doubtful ce in the margin; the cancellation and surrounding wording are clear. Mathematical claims about the conjecture’s failure and results on other pages are attributed to the supplied table, with no proof claimed.

**Ink check:** In crops/6_scan028_L708_isocrystals.jpg the typescript explicitly says prendre partout des isocristaux. In crops/6_scan028_L708_conjecture_start.jpg the bracketed passage begins J’aurais assez tendance à croire and includes the independence of G(B), all artinian rings of residue field k, and the underlined si et seulement si before A est ordinaire. A long oblique cancellation stroke crosses this passage; the full scan and crops/6_scan028_L708_cancellation_end.jpg show it continuing through the final paragraph about a general base, down to the last line with handwritten sons. In crops/6_scan028_L708_rejection_margin.jpg the separate left-margin note visibly begins Faux, continues n’est jamais vrai en car p>0, and underlines jamais. The short connecting word after Faux is a compressed wavy stroke; the existing unsure{ce} is retained. The source-table label his conjectures, some withdrawn on the page; known since is not manuscript text.

**Confidence:** medium.

**Proposed reading or refinement from the supplied table:** The following preserves the table’s precise proposal for comparison; mathematical and cross-source claims are attributed to that table, not certified by this visual audit.

```text
refined: after 2.7 he passes to isocrystals (6:28); the 2.8 conjecture (G(B) independent of the lift over all artinian rings iff A ordinary) is cancelled on the page with 'Faux, ce n'est jamais vrai en car p>0 !', and is false for every ordinary elliptic curve (k[t]/(t^{p+1}), check event 6:28); 6:29-30 are decided by the nonzero p-curvature of Gauss-Manin (computed for the Legendre family, p = 3, 5, 7); 3.1-3.2 are the universal extension and Grothendieck-Messing (true with nilpotent PD, e < p-1), and 3.2 asks for the Tate module of the generic fibre (the 'foncteur mystérieux')
```
