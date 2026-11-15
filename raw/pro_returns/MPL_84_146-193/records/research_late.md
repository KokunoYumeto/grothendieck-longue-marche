# Research-note draft: mathematical scans 172–192

Prepared after the transcription freeze and after reading the supplied context. Only the frozen TeX was read for this analytical task; no original scan image, crop, or transcription file was altered. Short quotations retain explicit doubt where it matters. Approximate lines refer to the per-scan TeX, not physical manuscript lines.

All algebraic checks below concern the explicitly stated local free model over a commutative ring. The context’s Hua entry remains an unreviewed conjectural summary; no claim of novelty or of complete categorical coherence is made. The broader primary-literature identification with quadratic-ring products is being supplied by the root researcher.

## L172.1

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, scan 172, approximate TeX lines 4–15. **Kind:** unproved claim.

**Brief quotation:** `u=2u_1u_2+b_2u_1+b_1u_2`

Under the monic local presentations \(u_i^2+b_i u_i+c_i=0\), the displayed \(u\) satisfies \(u^2+b_1b_2u+b_1^2c_2+b_2^2c_1-4c_1c_2=0\) over every commutative base ring; the accompanying script verifies the universal polynomial remainder over the integers. This establishes the local identity independently of whether the resulting abstract quadratic algebra embeds into the tensor product.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) concerns the broader extension product; this scan adds an explicit quadratic-algebra calculation beyond that entry’s cited interval, and no supplied register row settles this formula.

## L172.2

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, scan 172, approximate TeX lines 13–14. **Kind:** unpursued implication.

**Brief quotation:** `\delta=b^2-4c=\delta_1\delta_2`

The discriminant identity follows by expansion, so in the local free model the product has invertible discriminant exactly when both input discriminants are invertible. Over a field of characteristic two this tests whether both linear coefficients are nonzero; vanishing discriminant alone does not classify the resulting inseparable or nonreduced algebra.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is related by the product construction; the supplied context does not state this discriminant identity or a discriminant classification for these scans.

## L172.3

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, scan 172, approximate TeX lines 18–19; compare scan 192, 8–12. **Kind:** unproved claim (authorial qualification).

**Brief quotation:** `\unsure{injectif} \unsure{sauf si} car. 2 et $b_1=b_2=0$`

The marginal qualification singles out precisely the field case in which the indicated image of the abstract generator loses its nonconstant part. Scan 192’s “ça croule” repeats the same exceptional specialization, but neither passage by itself gives the general base-ring injectivity criterion.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) does not assert this tensor embedding criterion; the later scans add a restriction that should be kept separate from the entry’s asserted invertibility criterion for χ-split extensions.

## L172.4

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, scan 172, approximate TeX lines 18–19; compare scan 192, 12. **Kind:** own idea.

**Brief quotation:** `A\hookrightarrow A_1\otimes A_2`

For the displayed local model, \(i:R[t]/(t^2+bt+c)\to B=A_1\otimes_R A_2\), \(t\mapsto2u_1u_2+b_2u_1+b_1u_2\), has kernel \(\operatorname{Ann}_R(2,b_1,b_2)\,t\), because the four tensor-basis coefficients of \(i(a+dt)\) are \((a,db_2,db_1,2d)\). Thus \(R=\mathbb Z/4\mathbb Z\), \(b_1=b_2=c_1=c_2=0\), gives the nonzero kernel element \(2t\), while a split injection requires the stronger condition \((2,b_1,b_2)=R\). Confidence: high for this conditional algebraic statement, since it is a direct coefficient calculation and the script independently enumerates the small-ring examples.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is only a thematic match; this is an additional local-ring qualification, not a refutation of its abstract product or invertibility claims.

## L172.5

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, scan 172, approximate TeX lines 33–40, 45–48. **Kind:** unproved claim.

**Brief quotation:** `f+\bar f`

The local tensor operator \(T=1+\sigma_1\otimes\sigma_2\) admits maps \(i:A\to B\) and \(q:B\to A\) with \(iq=T\) and \(qi=2\operatorname{id}\); in the basis \((1,u_1,u_2,u_1u_2)\), \(q\) takes the values \((2,-b_1,-b_2,t+b_1b_2)\). These identities explain the displayed factor “2” and imply \(T^2=2T\): \(T\) is generally not idempotent, whereas \(T/2\) is a projector when two is invertible. The script verifies the matrices universally; identification with every doubtful arrow in the drawn diagram remains a reading question.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) supplies a conjectural division-free product lead; this scan adds a concrete factorization whose rank behavior needs hypotheses distinct from categorical existence.

## L172.6

**Source:** `pages/MPL_84_146-193_84_scan172.tex`, scan 172, approximate TeX lines 51; compare scan 192, 12. **Kind:** withdrawn in the same text.

**Brief quotation:** `\deleted{... \unsure{dégénéré|dégénère} en car. 2}`

The blanket-looking degeneration note is crossed out, whereas the later live wording on scan 192 specifies \(2=0,b_1=b_2=0\). It would therefore be misleading to report that the author finally rejects the construction in all characteristic-two cases; the separable cases below remain noncollapsed in the local model.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) contains no corresponding withdrawal; these two scans add the author’s own narrower exception, without resolving the unreviewed categorical claim.

## L174.1

**Source:** `pages/MPL_84_146-193_84_scan174.tex`, scan 174, approximate TeX lines 5–33. **Kind:** reading question.

**Brief quotation:** `\pi=\chi\mathrm{id}-f`

The boxed relation and the conditions that \(f\) vanish on \(L\) and induce \(\chi\operatorname{id}\) on \(E/L\) yield the expected complementary χ-splitting maps. The frozen final implication instead reads “\(f\) nul sur \(L'\),” and the earlier input line also puts \(\lambda\in L\) where the displayed source is \(L'\); these mismatches must be retained as questions about domains, not silently repaired.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) directly concerns these χ-splittings; the present page restates their mechanism but adds domain-label uncertainties absent from the summary claim.

## L174.2

**Source:** `pages/MPL_84_146-193_84_scan174.tex`, scan 174, approximate TeX lines 54–60. **Kind:** unproved claim.

**Brief quotation:** `E_i\simeq A_i\otimes\Delta_i`

The displayed identifications claim compatibility of the product with duality after determinant-line twists. A proof must specify the canonical rank-two duality maps, the tensor-line identifications, and the hypotheses under which the product is functorial; the written string of isomorphisms supplies no coherence verification.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is related at the categorical level, but contains no determinant-twist formula; this page adds a compatibility claim rather than a proof of the whole symmetric monoidal assertion.

## L174.3

**Source:** `pages/MPL_84_146-193_84_scan174.tex`, scan 174, approximate TeX lines 64–67. **Kind:** unpursued implication.

**Brief quotation:** `\pi(x)=2x-F(x)`

At \(\chi=2\), the usual splitting identity \(\pi^2=2\pi\) makes \(s=\operatorname{id}-\pi=F-\operatorname{id}\) an involution. This is a useful route between the extension notation and the conjugations used in scans 172 and 180, but the margin alone does not state all the identities needed to justify that interpretation.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the direct extension-product lead; this marginal specialization helps compare its general χ-language with the quadratic-algebra discussion, without identifying the two settings automatically.

## L176.1

**Source:** `pages/MPL_84_146-193_84_scan176.tex`, scan 176, approximate TeX lines 19–33, 49–50. **Kind:** unproved claim.

**Brief quotation:** `u_1\ast u_2-b_1b_2=\deleted{\unsure{2}}u`

The coefficient calculation concludes that the abstract product generator differs from \(u_1*u_2\) by the scalar \(b_1b_2\), while the scalar coefficient is extracted by pairing with \(x\). Its tensor image agrees with scan 172’s formula, but the abstract element and its potentially noninjective tensor image must be distinguished.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) gives a related split-coordinate product claim; this scan adds the explicit scalar shift for the quadratic-algebra generators, rather than the general χ-product’s full definition.

## L176.2

**Source:** `pages/MPL_84_146-193_84_scan176.tex`, scan 176, approximate TeX lines 40–50. **Kind:** withdrawn in the same text.

**Brief quotation:** `\mu=...=1\quad ...\quad\deleted{=2\unsure{,}}`

The attempted coefficient value two is cancelled and replaced by the factorwise pairing calculation giving one; the crossed-out twos in the concluding formulas implement that correction. This is a substantive normalization change, not merely a discarded spelling, and it is essential when comparing the product with its tensor symmetrization.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) does not record this coefficient correction; the page adds evidence that the two directions of comparison were being distinguished during the calculation.

## L176.3

**Source:** `pages/MPL_84_146-193_84_scan176.tex`, scan 176, approximate TeX lines 31. **Kind:** reading question (authorial emphasis).

**Brief quotation:** `\underset{!}{b_1u_2}`

The exclamation mark under \(b_1u_2\) draws attention to the cross term in the expansion. It is an authorial emphasis mark rather than an explicit “à vérifier,” and the term is present in the independently checked local formula.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) contains no term-level check of this expansion; the marked term supplies an additional local verification target, not an independent conjecture.

## L176.4

**Source:** `pages/MPL_84_146-193_84_scan176.tex`, scan 176, approximate TeX lines 52, 55–56. **Kind:** reading question.

**Brief quotation:** `u_1\ast u_2-\mathrm{Tr}_1(u_1)\mathrm{Tr}_2(u_2)=2\cdot`

The displayed trace reformulation ends at “\(2\cdot\),” and the marginal boxed tensor image also has a doubtful terminal mark. The nearby complete identities can explain the intended calculation, but they do not authorize filling this unfinished line in the frozen text.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is a thematic product match only; no supplied context entry completes this exact line, so the unfinished formulation remains open as a textual item.

## L178.1

**Source:** `pages/MPL_84_146-193_84_scan178.tex`, scan 178, approximate TeX lines 15–34. **Kind:** self-flagged: a step he himself marks as unverified.

**Brief quotation:** `Il y a à \unsure{écrire} \unsure{quatre} \unsure{compatibilités}`

The author announces four compatibility checks but writes only the labels \(1^\circ,2^\circ,3^\circ\) on this page. The “OK” at the foot cannot by itself supply an unwritten fourth condition or prove that all quotient relations have been tested.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) asserts agreement of two products without a supplied proof; this page adds explicit evidence of a compatibility task and an incomplete visible enumeration.

## L178.2

**Source:** `pages/MPL_84_146-193_84_scan178.tex`, scan 178, approximate TeX lines 25–29; compare scan 180, 33–41. **Kind:** reading question.

**Brief quotation:** `f-f^{\unsure{\leftrightarrow|\leftrightarrows}}`

If the doubled-arrow operation is the operator \(Tf=f+\sigma f\) defined on neighboring pages, the underbraced raw-tensor identity \(f-Tf=\operatorname{Tr}(f)1\) is generally false: over \(\mathbb Q\), take the nonzero free generator \(f=u_1\) of \(A_1=\mathbb Q[u_1]/(u_1^2+1)\), so \(b_1=0\), \(Tf=0\), and its left side is \(u_1\), not zero. This does not rule out a quotient-level statement or a different use of the operator symbol; the precise ambient map is required before treating the line as a proof.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the relevant comparison claim, but supplies no formula resolving this sign/operator ambiguity; the frozen reading is unchanged.

## L178.3

**Source:** `pages/MPL_84_146-193_84_scan178.tex`, scan 178, approximate TeX lines 31–42. **Kind:** unproved claim.

**Brief quotation:** `\langle f,x+\bar x\rangle=\langle f,\pi(x)\rangle`

The third check identifies a symmetrized pairing with a π-boundary pairing, but its stated ambient domains are too compressed to verify all restrictions from this line alone. The “OK” records the author’s local acceptance, while a full descent proof must separately treat both amalgamating submodules and their intersection.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) asserts an agreement that would require these descent checks; the page offers part of the argument, not an independently established complete result.

## L180.1

**Source:** `pages/MPL_84_146-193_84_scan180.tex`, scan 180, approximate TeX lines 3–24. **Kind:** unproved claim.

**Brief quotation:** `A\overset{\mathrm{def}}=(\unsure{A_1}\otimes A_2)\underset{(A_1\otimes_0 A_2)}\oplus\uline{\unsure{O|0}}`

The displayed amalgamated sums construct the candidate \(A\) and \(E\) without dividing by two. With locally free rank-two inputs and the standard scalar inclusions, the relevant boundary submodules have rank three and the pushouts have rank two, but this module-rank statement alone does not produce an associative multiplication or all canonical comparison maps.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) directly predicts a division-free amalgamated construction; these later pages give more explicit presentations while leaving algebra and coherence claims to be checked separately.

## L180.2

**Source:** `pages/MPL_84_146-193_84_scan180.tex`, scan 180, approximate TeX lines 29–35. **Kind:** unproved claim.

**Brief quotation:** `\unsure{les} \unsure{deux} \unsure{sont} \unsure{transposés}`

The asserted transposition of the two tensor involutions is consistent with the dual bases displayed in scans 176 and 190. In the local free model, the algebra conjugation has matrix \(\bigl(\begin{smallmatrix}1&-b_i\\0&-1\end{smallmatrix}\bigr)\), and its transpose determines the module-side involution, so the adjoint symmetrizer identity can be checked without inverting two.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is related through the extension product, but does not include these matrices; this page adds an adjointness assertion tested by the accompanying local calculation.

## L180.3

**Source:** `pages/MPL_84_146-193_84_scan180.tex`, scan 180, approximate TeX lines 39–50. **Kind:** reading question.

**Brief quotation:** `\langle f,x\rangle=\langle f^{\unsure{\leftrightarrow|\leftrightarrows}},x\rangle`

The first equality cannot hold for one unchanged ordinary tensor pairing in general: replacing \(f\) by \(Tf\) changes its value, for instance at \(f=1\). The page is defining a new product pairing, so the likely mathematical issue is that the same brackets denote pairings on different objects; their source and target must be recorded before using the equality.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) contains no pairing convention that resolves this notation; the page adds a reading-dependent definition, not a contradiction proved against the abstract product claim.

## L180.4

**Source:** `pages/MPL_84_146-193_84_scan180.tex`, scan 180, approximate TeX lines 26–26, 58–64. **Kind:** reading question.

**Brief quotation:** `Sur les \unsure{deux}-\unsure{autres} \unsure{morceaux|on a}`

After the essential tensor–tensor pairing, three further component rules are displayed: scalar–line is zero, tensor–line is evaluated through \(\varphi\), and scalar–tensor through \(\psi\). Together they fill the four blocks of a pairing on two two-term presentations; the doubtful prose “deux-autres” should not be used to suppress one of the three written rules.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the related pushout lead; this page contributes the four-block data needed for descent, with a local numerical wording question.

## L182.1

**Source:** `pages/MPL_84_146-193_84_scan182.tex`, scan 182, approximate TeX lines 12–21, 39–43. **Kind:** withdrawn in the same text.

**Brief quotation:** `\deleted{\tfrac12\mathrm{Tr}}`

The cancelled half-trace and the later unfinished \(\tfrac12\)-expression show that normalization by two was considered but not retained as a completed definition here. A division-free proof must use the boundary identities and quotient relations directly, especially in characteristic two.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) explicitly advertises a construction without division; this page is consistent with that aim but records an abandoned or unfinished normalization route rather than completing the proof.

## L182.2

**Source:** `pages/MPL_84_146-193_84_scan182.tex`, scan 182, approximate TeX lines 39–43. **Kind:** self-flagged: a step he himself marks as unverified.

**Brief quotation:** `\langle(1+\sigma)f,x\rangle=`

The lower calculation ends after an equals sign, and the adjacent bracketed half-expression is also unfinished. These are visible unfinished calculations rather than a written conjecture, so they should remain separate from the earlier statement “cela définit l’accouplement.”

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is a related construction claim only; no supplied context text supplies the missing right-hand sides.

## L182.3

**Source:** `pages/MPL_84_146-193_84_scan182.tex`, scan 182, approximate TeX lines 12, 39–43; compare scans 172 and 190. **Kind:** own idea.

**Brief quotation:** `\tfrac12`

The factorization \(iq=T,qi=2\operatorname{id}\) gives a precise explanation of the tempting half: restriction of the ordinary tensor pairing to the images of \(A\) and its abstract dual is twice the perfect abstract pairing. In characteristic two that restricted pairing can vanish even when abstract duality remains perfect, so trace degeneracy, tensor-embedding failure, and loss of abstract duality are distinct questions. Confidence: high for the stated local model, because the script verifies \(i^{\mathsf T}q^{\mathsf T}=2I\) as a universal matrix identity.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) provides the broader comparison problem; this is an additional explanation of the normalization obstacle, not a proof of its full monoidal claim.

## L184.1

**Source:** `pages/MPL_84_146-193_84_scan184.tex`, scan 184, approximate TeX lines 5–22, 43–46. **Kind:** unproved claim.

**Brief quotation:** `\unsure{on} \unsure{veut} \unsure{que} \unsure{ce} \unsure{soit}`

The two requested boundary values are exactly the tests needed to descend a bilinear form through the two displayed quotient presentations. They are requirements on a proposed form, not a completed proof that a form satisfying both exists and is nondegenerate.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) asserts agreement of constructions at a higher level; this page adds explicit descent conditions and does not settle that assertion by itself.

## L184.2

**Source:** `pages/MPL_84_146-193_84_scan184.tex`, scan 184, approximate TeX lines 19–22; compare scan 190, 16–24. **Kind:** own idea.

**Brief quotation:** `0\longrightarrow k\longrightarrow A\longrightarrow L_1^\vee\otimes L_2^\vee\longrightarrow0`

Once a descended pairing induces the displayed evaluation isomorphisms on the two graded pieces of these locally free extensions, it is perfect by a local adapted-basis calculation. Confidence: high conditional on those hypotheses, because its matrix is triangular with unit diagonal; this does not establish that every doubtful diagram in the manuscript meets the hypotheses.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the related extension-product claim; this supplies a proof strategy for the missing nondegeneracy step rather than importing a settled result from an unrelated context row.

## L186.1

**Source:** `pages/MPL_84_146-193_84_scan186.tex`, scan 186, approximate TeX lines 12–23. **Kind:** self-flagged: a step he himself marks as unverified.

**Brief quotation:** `E_1\wedge E_2\overset{?}{\longrightarrow}E_1\otimes E_2`

The question mark explicitly marks the return map from the product to the tensor product, and the following “O K” verifies the displayed \(E_1\otimes L_2\) boundary calculation. A full quotient-factorization proof also needs the symmetric boundary and agreement on their intersection; this one checked line should not be reported as all of those checks.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the direct comparison lead; this later page supplies a specific successful local check and an explicitly questioned map.

## L186.2

**Source:** `pages/MPL_84_146-193_84_scan186.tex`, scan 186, approximate TeX lines 3–9. **Kind:** reading question.

**Brief quotation:** `\unsure{\deleted{2u_1}\inserted{0}}`

The four-entry table agrees with \(1+\sigma_1\otimes\sigma_2\) in the specialization \(b_1=b_2=0\), as also suggested by the nearby relations \(-u_i^2=c_i\). For general coefficients the middle entries are \(-b_1\) and \(-b_2\), and the last is \(2u_1u_2+b_2u_1+b_1u_2+b_1b_2\); the source’s uncertain indices must not be normalized to this interpretation.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) gives no such table; the present scan adds a useful special-case check, not a valid unrestricted zero-entry table.

## L186.3

**Source:** `pages/MPL_84_146-193_84_scan186.tex`, scan 186, approximate TeX lines 25–33. **Kind:** unproved claim.

**Brief quotation:** `(x_1+u_1)\unsure{*|\circ}(x_2+u_2)`

The expansion tracks how changing chosen lifts affects the product, with two mixed terms and the \(2u_1\otimes u_2\) term. This is the right type of calculation for independence from splittings, but the frozen line \(b_1\otimes u_2+u_2\otimes b_{1|2}\) has an unresolved variable/type mismatch and cannot be used as an unqualified transition formula.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) asserts a coordinate-independent product; this page adds a lift-change calculation whose doubtful intermediate expression needs separate attention.

## L188.1

**Source:** `pages/MPL_84_146-193_84_scan188.tex`, scan 188, approximate TeX lines 18–26, 31–44. **Kind:** withdrawn in the same text.

**Brief quotation:** `(f,\deleted{\unsure{g_1,g_2}}\inserted{\lambda})`

The dual description is reduced from a bilinear form with two auxiliary functionals to a bilinear form with one scalar \(\lambda\). The cancelled conditions labelled a) and b), including the doubled \(2g_i\) restrictions, are replaced by the two trace restrictions; the cancelled version should not be combined with the live one as simultaneous axioms.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) has no dual-data description; this page adds an explicit revision of the quotient-duality calculation.

## L188.2

**Source:** `pages/MPL_84_146-193_84_scan188.tex`, scan 188, approximate TeX lines 20–26, 43–44. **Kind:** unproved claim.

**Brief quotation:** `f(x_1)=\lambda\mathrm{Tr}_1(x_1)`

The live trace restrictions are the natural annihilator conditions for the dual of the pushout presentation of \(A\). For the ordinary linear dual this follows from the universal property of the quotient without a projectivity assumption, whereas identifying that dual with the separately constructed \(E\) still requires the product pairing and, for perfect duality, finite local freeness.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is related through the asserted pushout/pullback agreement; this page adds a concrete dual characterization but not a complete identification with every displayed \(E\).

## L188.3

**Source:** `pages/MPL_84_146-193_84_scan188.tex`, scan 188, approximate TeX lines 51–52. **Kind:** withdrawn in the same text.

**Brief quotation:** `\deleted{A^\vee\unsure{?}}`

The comparison \(E\to A^\vee\) and the tentative scalar identification \(\lambda=\psi(x)\) are cancelled; the apparent question mark is itself a doubtful reading in the frozen transcription. Treating those identifications as established therefore needs the separate pairing calculation rather than reliance on this crossed-out attempt.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) asserts a broader agreement but does not review this cancelled comparison; this page supplies an explicit unresolved or withdrawn local attempt.

## L190.1

**Source:** `pages/MPL_84_146-193_84_scan190.tex`, scan 190, approximate TeX lines 4–12, 25–27. **Kind:** self-flagged: a step he himself marks as unverified.

**Brief quotation:** `$u$ \unsure{décrit|déduit} en termes de $u_1,u_2$ ?`

The opening question asks for the expression of \(u\) in terms of the two input generators, then proposes extraction of coefficients by the dual basis. Scan 176 already contains a related coefficient calculation within the supplied scan order, but these leaves do not establish the chronological order of the author’s work.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) supplies a product claim for an earlier cited interval; this page adds an explicit generator question rather than a new asserted general theorem.

## L190.2

**Source:** `pages/MPL_84_146-193_84_scan190.tex`, scan 190, approximate TeX lines 10–12. **Kind:** unproved claim.

**Brief quotation:** `\mathrm N_{A/k}(u_1*u_2)=\lambda^2c+\mu^2\unsure{-|+}\lambda\mu\beta`

For \(u^2+\beta u+c=0\), the exact formulas are \(\operatorname{Tr}(\lambda u+\mu)=-\lambda\beta+2\mu\) and \(\operatorname N(\lambda u+\mu)=\lambda^2c+\mu^2-\lambda\mu\beta\). The script verifies both from the multiplication matrix; this favors the minus alternative mathematically but does not change the frozen uncertain sign.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) contains no trace/norm calculation; LM2 C.d2 in `context/LM2_CONGRUENCE_ROWS.md` concerns different matrix-norm equations at cote 140-3 scans 198 and 202–203 and does not settle this local quadratic identity.

## L190.3

**Source:** `pages/MPL_84_146-193_84_scan190.tex`, scan 190, approximate TeX lines 10, 25–27; compare scan 176, 19–23. **Kind:** reading question.

**Brief quotation:** `u_1*u_2=\lambda u+\mu`

The scalar names are reversed relative to scan 176: there \(\lambda\) is the constant coefficient and \(\mu\) the coefficient of \(u\), while here they occur as \(\lambda u+\mu\). This is a change of local notation, so carrying the earlier numerical values into the later names without swapping them would create a false inconsistency.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) gives no λ/μ convention; this cross-page comparison adds a notation warning while leaving both frozen readings intact.

## L190.4

**Source:** `pages/MPL_84_146-193_84_scan190.tex`, scan 190, approximate TeX lines 16–24, 45–49. **Kind:** unproved claim.

**Brief quotation:** `base \inserted{duale} de $E$`

The basis statement and the two conditions \(\langle u,e\rangle=1\), \(\langle u,x\rangle=0\) characterize the abstract generator uniquely if the displayed pairing is perfect. They define an abstract element even when its map to the tensor algebra collapses, which is crucial for understanding the qualification on scan 192.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is the related product lead; this page adds a dual-basis construction that must be separated from any claim of tensor-product injectivity.

## L192.1

**Source:** `pages/MPL_84_146-193_84_scan192.tex`, scan 192, approximate TeX lines 8–12. **Kind:** self-flagged: a step he himself marks as unverified.

**Brief quotation:** `$A$: avec $1$ \unsure{ça} \unsure{croule} si $2=0,\ b_1=b_2=0$`

At that specialization the displayed tensor element \(u_1*u_2\) is zero, so together with one it cannot be a basis of an embedded rank-two algebra. The abstract monic quadratic algebra nevertheless remains free of rank two, and in characteristic two with \(b_1=b_2=1\) the construction instead gives \(t^2+t+c_1+c_2\), preserving the noncollapsed separable case.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) should not be read as a claim that every tensor realization is faithful; this scan adds the author’s explicit failure case and qualifies that interpretation without disproving abstract existence.

## L192.2

**Source:** `pages/MPL_84_146-193_84_scan192.tex`, scan 192, approximate TeX lines 14–36, 60–62. **Kind:** own idea.

**Brief quotation:** `b_1=\beta_1e_1\qquad c_1=\gamma_1e_1^{\unsure{\otimes2|2}}`

To globalize the scalar formula, track generator changes \(u_i'=a_i u_i+r_i\): the product generator changes by \(u'=a_1a_2u+a_1b_1r_2+a_2b_2r_1-2r_1r_2\), with the corresponding transformed monic coefficients. Confidence: high for this transition identity, verified symbolically over the integer polynomial ring; checking overlap cocycles gives a concrete route to gluing, but a full categorical associator is a further requirement.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) claims a global symmetric monoidal product; this is an additional local transition calculation bearing on descent, not a new proof of its coherence or invertibility assertions.

## L192.3

**Source:** `pages/MPL_84_146-193_84_scan192.tex`, scan 192, approximate TeX lines 41–43, 56. **Kind:** reading question.

**Brief quotation:** `u_2^2\unsure{+|=}\beta_{\unsure{1|2}}u_2+\gamma_2=0`

The frozen lower equation retains both the doubtful operation sign and the subscript alternative \(\beta_{1|2}\), while the final correspondence has \(\gamma_{2|1}\). The independent coefficient calculation can identify a consistent mathematical convention, but none of these symbols may be changed after context opening.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) gives no line-level reading capable of deciding these indices; the comparison raises a convention question rather than correcting the transcription.

## L192.4

**Source:** `pages/MPL_84_146-193_84_scan192.tex`, scan 192, approximate TeX lines 43, 49–62. **Kind:** unproved claim.

**Brief quotation:** `u=\unsure{2}uu'+`

The product-generator calculation is left unfinished, although the page ends with a complete generic equation \(u^2+\beta u+\gamma=0\). The preceding basis correspondences explain a method to compute \(\beta,\gamma\), but the last generic equation alone does not supply their values or prove that the construction is independent of choices.

**Context comparison:** `context/notes/RESULTS_STATE.md`, Hua, findings register, 84-chi-trivialised-extension-product (conjectural, unreviewed; cited scans 146–170) is related at the product level; this page adds an incomplete return to coordinates rather than completing the entire assertion in the context.
