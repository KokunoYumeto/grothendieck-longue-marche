# Extension and splitting research items

These notes were written after the transcription freeze and use the frozen fragments without changing them. **C** denotes the supplied, unreviewed first-pass file **same_cote_84/MPL_84_146-193_notes.md**; its section identifiers are locators for leads, not certifications of later scans, which this researcher did not inspect. **RS-Hχ** denotes the entry **Hua, findings register, 84-chi-trivialised-extension-product** as excerpted in **notes/RESULTS_STATE.md**, with the supplied status “conjecture” and an intake verdict at statement level only. Searches for every item are recorded in **extension_context_searches.md**; the conditional computations named below are in **extension_calculation_report.md** and **scripts/research_extensions_checks.py**.

## B01 — The compatibility equivalence is posed as a question

**Source:** pages/MPL_84_097-145_84_scan124.tex, cote 84, scan 124, lines 2–14; **Kind:** self-flagged; **Context relation:** adds an earlier explicit question to C E170.3, scan 170; **Register:** RS-Hχ.

The equivalence between compatibility with the two splitting maps bears “?” both above the double implication and after the second equation, and the next calculation stops at an unfinished relation. C E170.3 supplies a later lead for the complementary splitting identities that could prove the equivalence, but those identities must be hypotheses of the argument, not reconstructed words on scan 124. The frozen \(\equiv|=\) alternatives and the unfinished lower formula therefore remain reading questions even if a conditional proof is available.

## B02 — A proof of the questioned equivalence needs exactness, not division

**Source:** pages/MPL_84_097-145_84_scan124.tex, cote 84, scan 124, lines 2–11; **Kind:** own idea; **Confidence:** high under the stated exact-sequence hypotheses, because the two cancellations are by a monomorphism and an epimorphism; **Context relation:** adds a precise proof to the later identities reported in C E170.3, scan 170, rather than proving RS-Hχ as a whole; **Register:** RS-Hχ.

For short exact rows with inclusion maps \(a,a'\), quotient maps \(q,q'\), and a row morphism \((r,f,s)\), assume the complementary identities \(a\pi+\omega q=\chi I\) and \(a'\pi'+\omega'q'=\chi I\). Then \(r\pi=\pi'f\) implies \((f\omega-\omega's)q=0\), hence \(f\omega=\omega's\), while the latter equality implies \(a'(r\pi-\pi'f)=0\), hence the former. This supplies a conditional answer to the manuscript's “?” without cancelling \(\chi\), and works even when \(\chi\) is a zero divisor. It does not repair the doubtful letters or the incomplete calculation on the sheet.

## B03 — Functoriality is asserted at two different levels

**Source:** pages/MPL_84_097-145_84_scan126.tex, cote 84, scan 126, lines 16–35; **Kind:** unproved claim; **Context relation:** adds earlier formulations to C E170.2, scan 170, and differs in scope from the editorial local groupoid of C R11; **Register:** RS-Hχ.

The sheet calls functoriality for isomorphisms “c'est clair par construction” and extends it to homomorphisms with “Ça marche aussi,” followed by change-of-ends diagrams. These statements require the actual category of \(\chi\)-split extensions, its morphisms, and compatibility with the two endpoint maps to be specified. C R11 already claims a strict monoidal law for a declared local rank-one groupoid, but that calculation does not identify these drawn general homomorphisms with that groupoid or establish the global functor claimed here.

## B04 — The comparison square retains the scalar condition

**Source:** pages/MPL_84_097-145_84_scan126.tex, cote 84, scan 126, lines 2–18; compare scan 128, lines 39–45; **Kind:** unpursued implication; **Context relation:** adds earlier manuscript evidence for the restriction discussed in C E148.1 and E170.5, scans 148 and 146/154/170; **Register:** RS-Hχ.

The square labelled “comm!” uses \(T_{-\gamma b}\), while the displayed calculation ends \(U-\gamma b'=-U-\gamma b\). With the first, plus reading \(b'=b+\chi U\), the residual between the two paths is \((2-\gamma\chi)U\), so the subsequently explicit hypothesis \(\gamma\chi=2\) is sufficient exactly as written. This is an endpoint-comparison calculation under a scalar condition, not evidence that the product operation itself fails whenever that scalar condition is unavailable.

## B05 — An extra minus is not the inverse of a translation

**Source:** pages/MPL_84_097-145_84_scan128.tex, cote 84, scan 128, lines 22–23; **Kind:** reading question; **Context relation:** differs literally from the translation convention used in C §10.3 and bears on the sign distinction in C E170.4–E170.5, scans 168/170 and 146/154/170; **Register:** RS-Hχ.

The margin says “Mais attention” and retains the live chain \(\widetilde T_{\widetilde U}=T_{-\widetilde U}=-T_{-U}=T_U^{-1}\), with one additional earlier minus cancelled. For the coordinate convention \(T_U(\eta,\zeta)=(\eta,\zeta+U\eta)\), the inverse is \(T_{-U}\), whereas its scalar negative also negates both endpoints; the two matrices differ by \(\begin{pmatrix}-2&0\\2U&-2\end{pmatrix}\). C §10.3 therefore suggests checking whether the live minus is an unremoved sign change or belongs to a different endpoint identification, but cannot select a different frozen reading. The endpoint distinction matters because C's counterexample is itself explicitly conditional on fixing both ends.

## B06 — Two uses of the swapped coefficient need to be distinguished

**Source:** pages/MPL_84_097-145_84_scan128.tex, cote 84, scan 128, lines 4–5, 18–26 and 32–45; **Kind:** reading question; **Context relation:** adds a convention problem to C E146.1 and E170.5, scans 146 and 146/154/170; **Register:** RS-Hχ.

The sheet first has \(\widetilde b_i=-b_i\), then “\(\widetilde b=\widetilde b_1\widetilde b_2=b_1b_2\),” but the later comparison writes \(\widetilde b\) with \(-b\) beneath it. One reading of the argument distinguishes the coefficient obtained by swapping both factors from the coefficient of the complementary splitting of their product; treating both uses as the same coefficient without tracking those identifications gives opposite signs. C's subsequent split-coordinate analysis makes that distinction consequential but does not settle the earlier notation, so no sign is harmonized in the transcription.

## B07 — Existence of gamma is a hypothesis of this construction

**Source:** pages/MPL_84_097-145_84_scan128.tex, cote 84, scan 128, lines 38–45; pages/MPL_84_097-145_84_scan142.tex, scan 142, lines 32–38; **Kind:** unpursued implication; **Context relation:** adds an earlier occurrence of the restriction in C E148.1, E156.1 and E164.3, scans 148, 156 and 164; **Register:** RS-Hχ.

The words “Supposons que” precede \(\exists\gamma\in k,\ \gamma\chi=2\), replacing the provisional quotient \(-2b/\chi\) by \(v=-\gamma b\). Thus this construction requires \(2\in\chi k\), not necessarily that \(\chi\) be invertible; the explicit case \(\chi=2,\gamma=1\) in scan 142 needs no inversion of 2. C's separate all-\(\chi\) local product model R11 addresses existence of a product, so its positive result and this restricted comparison are different assertions rather than contradictory claims.

## B08 — A choice of gamma can leave a comparison ambiguity

**Source:** pages/MPL_84_097-145_84_scan128.tex, cote 84, scan 128, lines 43–45; **Kind:** own idea; **Confidence:** high for the stated finite-ring example, because both translations are computed explicitly; **Context relation:** adds an instance tied to the earlier \(v=-\gamma b\) formula to C R13 and E154.2, scans 146/154 and 154; **Register:** RS-Hχ.

The formula “\(v=-\gamma b\)” can depend on the chosen solution of \(\gamma\chi=2\): over \(\mathbb Z/4\), with \(\chi=2\) and \(b=1\), the choices \(\gamma=1,3\) give \(v=3,1\), respectively. Both send \(b\) to \(-b\) through \(b\mapsto b+\chi v\), yet their translations differ by the nonzero automorphism with parameter 2. This realizes the annihilator phenomenon already identified in C R13, now within the manuscript's comparison formula, and requires the auxiliary choice to be stated when discussing canonicity. It does not deny that the displayed specialization \(\chi=2\) has the distinguished available choice \(\gamma=1\).

## B09 — The last coordinate increment on scan 130 lacks a factor

**Source:** pages/MPL_84_097-145_84_scan130.tex, cote 84, scan 130, lines 38–58; **Kind:** reading question; **Context relation:** differs from the coordinate identity in C E146.3 and §10.3, scan 146 and the local model; **Register:** RS-Hχ.

The frozen final line is “\(\pi_{(p_1,p_2)}(\eta,\zeta)+U(\eta)\),” while the same sheet defines \(b'_i=b_i+\chi U_i\) and \(U=b_1\otimes U_2+U_1\otimes b_2+\chi U_1\otimes U_2\). In the same coordinates these definitions give \(b'_1\otimes b'_2-b_1\otimes b_2=\chi U\), so C's matching identity suggests checking a missing \(\chi\) or an implicit coordinate transport in the final equality. The literal same-coordinate residual is \((\chi-1)U\), recorded in the calculation report; it is an editorial test, not a correction to that line.

## B10 — The positive and negative splitting conventions coexist in the draft

**Source:** pages/MPL_84_097-145_84_scan132.tex, cote 84, scan 132, lines 25, 33–34, 48–49 and 69–70; **Kind:** reading question; **Context relation:** adds conflicting draft signs beside the positive coordinate changes reported in C E146.1 and §10.3, scan 146; **Register:** RS-Hχ.

The table writes \(b'_i=b_i+\chi U_i\), the next tensor expansion uses \((b_1-\chi U_1)\otimes(b_2-\chi U_2)\), and the lower calculation returns to the plus convention. Scan 134 also explicitly changes the naming of the increments, so the differences should be studied as successive coordinate conventions before being called a single mathematical contradiction. C's later positive-convention model provides a comparison convention but cannot decide which draft line the author intended to replace.

## B11 — The cocycle calculation has a precise sign test

**Source:** pages/MPL_84_097-145_84_scan132.tex, cote 84, scan 132, lines 40–70 and 79–91; **Kind:** own idea; **Confidence:** high for the formal sign comparison, because the residuals are exact polynomial expansions; **Context relation:** adds a test of this earlier draft to C R11 and E170.5, scans 146/164/170 and 146/154/170; **Register:** RS-Hχ.

“Je dis que \(U''=U+U'\)” is compatible with the displayed bilinear formula when \(U''_i=U_i+U'_i\) and \(b'_i=b_i+\chi U_i\), matching the composition law already claimed for the local model in C R11. If the same formula for \(U'\) instead uses \(b'_i=b_i-\chi U_i\), the scalar-coordinate residual is \(2\chi(U_1U'_2+U_2U'_1)\). This isolates the effect of mixing the two signs in this sheet without re-proving the context's full monoidal model. A valid cocycle computation is evidence for gluing chosen local splittings, but does not by itself provide unit, associativity and symmetry constraints for all extension morphisms.

## B12 — Three indices in the successive-change calculation remain open

**Source:** pages/MPL_84_097-145_84_scan132.tex, cote 84, scan 132, lines 11–12, 62 and 70; **Kind:** reading question; **Context relation:** adds local reading questions to the same two-factor coordinate changes of C E146.1 and E170.5, scans 146 and 146/154/170; **Register:** RS-Hχ.

The upper vertex retains \(p''_3|p''_2\), and the successive-increment line retains \(U''_2=(U_2|U'_2)+U'_2\), where the vertical bars here report the frozen transcription's alternatives. The two-factor convention suggests \(p''_2\), and the adjacent \(U''_1=U_1+U'_1\) plus the expanded second-factor sum suggest \(U_2\) as the first summand. The lower pair actually reads \(b''_2=b_2+\chi U'_2\), suggesting a missing prime on \(b_2\) only if \(U'_2\) is the second successive increment rather than the total one. These are contextual reading questions with explicit alternatives and reasons, not grounds to alter the frozen occurrences.

## B13 — The minus sign in the dual extension has an explicit local source

**Source:** pages/MPL_84_097-145_84_scan134.tex, cote 84, scan 134, lines 31–46; pages/MPL_84_097-145_84_scan136.tex, scan 136, lines 2–8; **Kind:** unpursued implication; **Context relation:** adds an earlier sign explanation to C E160.2–E160.3 and E170.4, scans 160–162 and 168/170; **Register:** RS-Hχ.

After “signe étrange,” scan 134 attributes the signs to \(-\mathrm{id}\) in the extension diagram and gives \(\varphi(x,y)=-x\psi(y)+y\psi(x)\). For \(x\in L\), this formula becomes \(y\mapsto-x\psi(y)\), which acts as \(-\mathrm{id}_L\) after identifying the quotient-linear maps to \(L\) with \(L\). That explains the left endpoint sign in this particular diagram and is compatible with C's insistence that endpoint conventions matter. It is not a proof that every later tensor-product sign has already been reconciled.

## B14 — The special dual and all three primes need independent definitions

**Source:** pages/MPL_84_097-145_84_scan134.tex, cote 84, scan 134, lines 40–56; pages/MPL_84_097-145_84_scan136.tex, scan 136, lines 2–8 and 32–43; **Kind:** reading question; **Context relation:** differs in notation and adds definition questions beside C E148.3, E160.1–E160.3, scans 148, 160–162; **Register:** RS-Hχ.

The actual readings are \(\operatorname{Hom}^{!}(E,L)\) and \([\pi'_1,f'_1]'\), with separate primes on \(\pi_1\), \(f_1\), and the bracket; none should be silently identified with the later shifted operator \(\pi'=\pi-(\chi-1)\mathrm{id}\) in C E160.3. The incomplete set-builder on scan 134 suggests maps whose restriction to \(L\) is scalar, but its unfinished \(\alpha\)-expression does not define the displayed quotient map \(f\mapsto\lambda\) in full. A precise definition would need either uniqueness of that scalar (for example, faithfulness of \(L\)) or pairs \((f,\lambda)\) satisfying \(f\alpha=\lambda\alpha\); this is a proposed clarification because a scalar annihilating \(L\) is otherwise invisible. C's later trace and duality discussions are comparison leads, not evidence that this special dual, its bracket, and all its primes already carry those later definitions.

## B15 — The two “strange signs” involve different types of input

**Source:** pages/MPL_84_097-145_84_scan136.tex, cote 84, scan 136, lines 25–55; pages/MPL_84_097-145_84_scan134.tex, scan 134, lines 36 and 63–78; **Kind:** self-flagged; **Context relation:** adds an earlier unresolved sign warning to C E160.3 and E170.5, scans 160–162 and 146/154/170; **Register:** RS-Hχ.

The author flags “signe étrange!” beside \((U_1*U_2)(x_1*x_2)=-\chi U_1(x_1)\otimes U_2(x_2)\), while the same sheet writes \(u_1*u_2=\chi u_1\otimes u_2\). The \(U_i\) are quotient-linear maps in the surrounding calculation, whereas the \(u_i\) are submodule vectors, so merely replacing the negative sign by the positive vector formula would erase a type distinction. Scan 134's explicit renaming \(U'_i=-U_i\) and C's later emphasis on endpoint and splitting conventions identify what must be tracked, but do not by themselves resolve this warning.

## B16 — One tensor-restriction check is explicitly discharged

**Source:** pages/MPL_84_097-145_84_scan138.tex, cote 84, scan 138, lines 7–28; **Kind:** self-flagged; **Context relation:** adds an earlier completed local check beside C E156.2 and E166.3, scans 156 and 166; **Register:** RS-Hχ.

After the asserted formula for \(f_1*f_2\), the author writes “Vérifions,” computes its value on \(x_1*u_2\), cancels the two \(\chi f_1(x_1)\otimes\lambda_2u_2\) terms, and ends “OK.” Under the displayed scalar restrictions \(f_i|_{L_i}=\lambda_i\mathrm{id}\), this checks the value \(\lambda_1\lambda_2\pi_1(x_1)\otimes u_2\) on that mixed summand. The local check should therefore be recorded as discharged; symmetry, the overlap, and compatibility with composition require their own arguments before a complete descent or functoriality claim follows.

## B17 — Division by \(\chi\) is stronger than the integral identity

**Source:** pages/MPL_84_097-145_84_scan138.tex, cote 84, scan 138, lines 31–35; **Kind:** reading question; **Context relation:** differs in presentation from the undivided identities and annihilator cautions in C E164.1 and R13, scan 164 and the local groupoid section; **Register:** RS-Hχ.

The actual final expression is “\(\frac1\chi\,\pi_1*\pi_2=\pi\),” while the preceding values support the undivided identity \(\pi_1*\pi_2=\chi\pi\). The contextual alternative is to understand this as a divisibility mnemonic for an independently constructed \(\pi\), because multiplication by a zero divisor need not determine a map uniquely. Neither the handwritten expression nor the later integral matrix formulas justify imposing invertibility of \(\chi\) on the entire construction.

## B18 — The surviving splitting formula is not its cancelled rewrite

**Source:** pages/MPL_84_097-145_84_scan140.tex, cote 84, scan 140, lines 15–42; **Kind:** withdrawn in the same text; **Context relation:** adds an earlier cancelled normalization attempt beside C E146.1 and E152.1, scans 146 and 152; **Register:** RS-Hχ.

The live expression is \(p(x_1*x_2)=x_1*x_2-(x_1-p_1(x_1))*(x_2-p_2(x_2))\), and the following rewrite with an overall \(\chi\) is cancelled. Applying the mixed-product relations to the surviving expression gives \(\pi_1(x_1)\otimes p_2(x_2)+p_1(x_1)\otimes\pi_2(x_2)-\chi p_1(x_1)\otimes p_2(x_2)\), matching scan 138 with \(\lambda_1=\lambda_2=1\). This comparison does not require the unwritten identities \(\pi_i=\chi p_i\), and the cancelled line should not be reinstated as a general normalization rule.

## B19 — The scalar restriction does not require \(\chi=1\)

**Source:** pages/MPL_84_097-145_84_scan140.tex, cote 84, scan 140, lines 46–65; **Kind:** reading question; **Context relation:** adds an earlier normalization problem beside C E152.1, scan 152, without equating their two differently written corrections; **Register:** RS-Hχ.

After a cancelled coefficient expression, the actual live line is “\(2-\chi=1\).” With the same sheet's mixed-product rule and \(u_1*u_2=\chi u_1\otimes u_2\), the three terms on an input \(u_1*u_2\) instead total \((2\chi-\chi)\lambda_1\lambda_2u_1\otimes u_2=\chi\lambda_1\lambda_2u_1\otimes u_2\), with no condition \(\chi=1\). The suggested reading question is whether the live scalar line omits a factor or records an abandoned normalization, since C E152.1 later reports a different cancelled \(2\chi=\chi\) followed by \(\chi=\chi\). That later correction is evidence of continued checking, not permission to alter this frozen line or turn it into a standing hypothesis.

## B20 — The strict extension isomorphism remains conditional on constructing \(F_{11}\)

**Source:** pages/MPL_84_097-145_84_scan142.tex, cote 84, scan 142, lines 3–30; **Kind:** unproved claim; **Context relation:** restates the conditional block-map problem in C E166.1–E166.3 and E168.1, scans 166–168; **Register:** RS-Hχ.

“Si on a pu définir \(F_{11}\)” is the hypothesis of the assertion that \(F\), with identities on \(L_1\otimes L_2\) and \(M_1\otimes M_2\), is an extension isomorphism. The two displayed requirements prescribe a restriction and a quotient composite of \(F_{11}\), but those prescriptions alone do not construct a compatible middle map. C's later four-block analysis confirms that the remaining block and the endpoint convention are substantive conditions, rather than consequences of drawing the squares.

## B21 — The boxed comparison is an earlier conditional candidate

**Source:** pages/MPL_84_097-145_84_scan142.tex, cote 84, scan 142, lines 32–48; **Kind:** unproved claim; **Context relation:** adds an earlier occurrence of the conditional candidate examined in C E156.2 and E164.3, scans 156 and 164; **Register:** RS-Hχ.

The box gives \(\chi\mathrm{id}-(\pi'_1+\pi'_2)+\gamma\pi'_1\otimes\pi'_2\) together with “\(\gamma\chi=2\),” followed at \(\chi=2\) by \(F_{11}(x)=\bar x+x\). If these primed partial operators are identified with the \(P_i\) of C E164.3, its coefficient tuple is \((\chi,-1,-1,\gamma)\), the \(\delta\chi=2\) specialization of that later coefficient family. This identifies a candidate and its scalar condition, not a proof of that notational identification, descent, or naturality; the later specialized tensor check supplies only its stated scope.

## B22 — The involution correspondence at \(\chi=2\) does not need \(2^{-1}\)

**Source:** pages/MPL_84_097-145_84_scan142.tex, cote 84, scan 142, lines 38–51; **Kind:** own idea; **Confidence:** high under the stated exact-sequence hypotheses, because both directions use explicit factorization through a monomorphism; **Context relation:** adds the converse factorization to C E150.2 and E160.3, scans 150 and 160–162; **Register:** RS-Hχ.

The margin says that the data of \(\pi_1\) “équivaut” (a frozen doubtful word) to an involution inducing \(-\mathrm{id}_{L_1}\) and \(+\mathrm{id}_{M_1}\). For an exact row \(0\to L\xrightarrow{a}E\to M\to0\) and \(\pi a=2\mathrm{id}_L\), the map \(\sigma=\mathrm{id}_E-a\pi\) has those endpoint actions and satisfies \(\sigma^2=\mathrm{id}_E\). Conversely, such an endomorphism \(\sigma\) has \(\mathrm{id}_E-\sigma=a\pi\) for a unique \(\pi\), because its quotient action is the identity, and its restriction to \(L\) gives \(\pi a=2\mathrm{id}_L\). No division by \(2\) occurs, so this is not an eigenspace decomposition assertion, including when the two endpoint signs coincide in characteristic \(2\).

## B23 — Preservation of the submodules is not the whole descent condition

**Source:** pages/MPL_84_097-145_84_scan144.tex, cote 84, scan 144, lines 12–43; **Kind:** unproved claim; **Context relation:** differs in stated hypotheses from the compatible-morphism constructions in C E170.1–E170.2 and R11, scan 170 and the local groupoid section; **Register:** RS-Hχ.

The opening names endomorphisms \(f_i\) but freezes the restriction as \((u_i|f_i)(L_i)\subset L_i\), so \(f_i(L_i)\subset L_i\) is the apparent intended hypothesis, not a certain reading of that letter; the sheet then proposes \(f(x_1*x_2)=f_1(x_1)*f_2(x_2)\) and the endpoint map \(f^!_1\otimes f^!_2\). Under that interpretation, its mixed-summand diagram also needs the equality \(\pi_1f_1=f^!_1\pi_1\), and likewise for the second factor, whereas preservation of \(L_i\) alone does not supply it. The unfinished “Ex” and following incomplete equations therefore remain a live compatibility investigation, not a proof of functoriality for every submodule-preserving endomorphism.

## B24 — A shear detects the missing compatibility on scan 144

**Source:** pages/MPL_84_097-145_84_scan144.tex, cote 84, scan 144, lines 12–37; **Kind:** own idea; **Confidence:** high for the stated split vector-space example, because the defining relation is tested by explicit matrices; **Context relation:** adds a counterexample to the broader proposed hypotheses while leaving C R11's restricted morphism model intact; **Register:** RS-Hχ.

Under B23's interpretation of the initial hypothesis, take \(\chi=1\), \(E_i=k\ell_i\oplus km_i\), \(L_i=k\ell_i\), \(\pi_i(\ell_i)=\ell_i\), \(\pi_i(m_i)=0\), \(f_2=\mathrm{id}\), and the submodule-preserving shear \(f_1(\ell_1)=\ell_1,\ f_1(m_1)=m_1+\ell_1\). The product relation gives \(m_1*\ell_2=0\), whereas the proposed image is \((m_1+\ell_1)*\ell_2=\ell_1\otimes\ell_2\ne0\). The calculation report verifies the same obstruction with the tensor quotient matrix, so the displayed action cannot descend under submodule preservation alone. This does not refute functoriality for morphisms satisfying \(\pi_if_i=f_i^!\pi_i\).

## B25 — The last scalar identity states an additional compatibility

**Source:** pages/MPL_84_097-145_84_scan144.tex, cote 84, scan 144, lines 52–96; **Kind:** unpursued implication; **Context relation:** adds an earlier map-compatibility formulation beside the scalar-extraction cautions of C E158.1–E158.2, scan 158; **Register:** RS-Hχ.

The lower diagrams change to maps \(f_i:E_i\to L_i\), and the final live line is “\(\lambda_1\pi_1(x_1)=f_1(x_1)\chi\).” If \(f_i|_{L_i}=\lambda_i\mathrm{id}\), this is exactly compatibility with the \(\chi\)-retraction \(\chi\mathrm{id}_{L_i}\) on the target; the scalar restriction by itself does not imply it on all of \(E_i\). Neither the doubtful quotient of \(\lambda\)'s nor this equation permits cancelling a possibly nonunit \(\lambda_i\) or a zero-divisor \(\chi\), matching the later context's distinction between annihilated maps and scalar identities.

## B26 — The Hua register entry must retain separate scopes

**Source:** pages/MPL_84_097-145_84_scan126.tex, cote 84, scan 126, lines 8–24; pages/MPL_84_097-145_84_scan128.tex, scan 128, lines 38–45; pages/MPL_84_097-145_84_scan130.tex, scan 130, lines 21–58; pages/MPL_84_097-145_84_scan132.tex, scan 132, lines 40–91; pages/MPL_84_097-145_84_scan142.tex, scan 142, lines 3–51; **Kind:** reading question; **Context relation:** adds earlier textual provenance to C R10–R13 and E170.2–E170.5, scans 146–170 and the local-model sections; **Register:** RS-Hχ.

The present sheets support the local coefficient rule “\(b=b_1\otimes b_2\)” and an attempted splitting-change cocycle, while their fixed-endpoint pushout/pullback comparison explicitly uses \(\gamma\chi=2\) and a still-conditional \(F_{11}\). They do not state a tensor unit, associativity and symmetry coherence data, or the \(T_0\)-generation-on-\(V(\chi)\) invertibility criterion in these eleven handwritten pages. C R11–R13 later claim those local rank-one model laws and an ideal-theoretic invertibility test, but their identification with global extension objects and with Hua's \(T_0\) criterion remains a separate task under C R10. Thus the unrestricted product, its invertible objects, global coherence, and a particular strict-endpoint comparison must receive separate verdicts; a restriction on the comparison does not refute the all-\(\chi\) local product.

## Standing register of author-marked checks, qualifications and unfinished assertions

The line references below are physical lines of the frozen page TeX, not newly assigned handwriting lines. Quotation marks enclose the short surviving author cue; a transcription alternative is explicitly labelled as such and is never counted as an author question mark. A completed local check is retained so it cannot later be misreported as an unresolved author doubt.

| Cote 84, scan and lines | Exact brief author cue | Standing and scope | Notes |
|---|---|---|---|
| 124:7,10–14 | “?” over the double implication, and a second “?” after it | Two authorial question marks; the following equivalence calculation is unfinished and one attempted equality is cancelled. The equality/equivalence alternatives and uncertain letters are transcription doubts. | B01–B02 |
| 124:16–30 | the final isolated “\(E_1\wedge\)” | Proposed induced-product morphism and mixed-summand diagram, followed by an unfinished expression; no authorial question mark is added by this observation. | B01–B03, B23 |
| 126:4,11,13–14 | “comm!”; “car” | Claimed commutative translation square; the short displayed arithmetic uses a sign choice and the condition supplied explicitly on scan 128. “car” is followed by a mark, not a completed independent proof. | B04 |
| 126:23–24 | “c'est clair par construction”; “Ça marche aussi” | Isomorphism naturality asserted, then extended verbally to homomorphisms; the category and compatibilities require specification. The preceding doubtful words in line 23 are transcription doubts. | B03 |
| 128:22–23 | “Mais attention” | Explicit warning at the translation/inverse chain; the surviving global minus requires checking as a map, independently of the cancelled doubtful minus. | B05 |
| 128:39–45 | “L'on veut que”; “Supposons que” | Desired comparison followed by the sufficient hypothesis \(\gamma\chi=2\); the exclamation over the equality is author emphasis, not a transcription doubt. | B06–B08 |
| 130:54–58 | “NB”; “transforme” | Claimed transport formula; same-coordinate reading has the coefficient discrepancy identified in B09. There is no authorial question mark here. | B09 |
| 132:40–49,79–91 | “Je dis que \(U''=U+U'\)” | Claimed cocycle with a partially worked, unfinished expansion and mixed draft sign conventions; the doubtful indices/signs are transcription alternatives. | B10–B12 |
| 134:32–39 | “signe étrange”; “Ces signes sont” | Authorial sign warning followed by an attribution to \(-\mathrm{id}\); doubtful connecting words remain transcription doubts. | B13, B15 |
| 134:51–56 | “\(\exists\lambda;\)” | Scalar-restriction definition is unfinished in the surviving set-builder. No question mark is attributed to the author. | B14 |
| 134:63–79 | “Si on pose”; “d'où” | Explicit change of increment convention and a boxed resulting formula; the closing marginal wording is doubtful transcription, not an author objection. | B10, B15 |
| 136:11–12,35–45 | “\({}_{\lambda_1}E_1*{}_{\lambda_2}E_2\simeq\)”; “de \(=\)” | Incomplete product identification and connective, with a terminal equality after the \(U_1*U_2\) value. | B14–B15 |
| 136:44–48 | “signe étrange!” | Surviving authorial warning at the negative product of quotient-linear maps; not discharged merely by the positive submodule-vector product below. | B15 |
| 138:13,20–28 | an exclamation over “\(=\)”; “Vérifions”; “OK” | One mixed-restriction check explicitly undertaken and locally discharged; broader descent is not checked by this one cancellation. | B16 |
| 138:35 | “\(\frac1\chi\,\pi_1*\pi_2=\pi\)” | Live normalization notation needing a divisibility or invertibility interpretation; no authorial question mark. | B17 |
| 138:38,49–51 | “\(x_1*x_2\simeq\)” followed by a doubtful expression; a cancelled bracket expression | Unfinished lower scratch work, not a completed additional identification. The uncertainty is transcriptional. | B14, B17 |
| 140:12,32–42 | “comm.”; the cancelled rewrite beginning “\(=\chi\)” | Claimed splitting diagram with surviving expanded formula; the overall-\(\chi\) rewrite is withdrawn. | B18 |
| 140:57–65 | cancelled “\((2-\chi)\lambda_1\lambda_2u_1\otimes u_2\)”; live “\(2-\chi=1\)” | Normalization attempt with a live scalar line that cannot safely be promoted to a general hypothesis. | B19 |
| 142:3–5 | “Si on a pu définir \(F_{11}\)” | Conditional construction; the word transcribed as “Concentrons” is doubtful, not an author question. | B20 |
| 142:32–38 | “\(\gamma\chi=2\)”; “on aura” | Conditional comparison candidate and its \(\chi=2\) specialization. | B21 |
| 142:51 | “NB”; the word transcribed doubtfully as “équivaut” | Compressed assertion relating retractions and involutions; no authorial question mark is present. | B22 |
| 144:12–37 | “t.q.”; the proposed equations for “\(f\)” | Rough functoriality proposal, interpreted as submodule preservation despite the frozen \(u_i|f_i\) letter alternative; its mixed-summand condition is additional. | B23–B24 |
| 144:40–43 | “Ex”; “\(f=\)”; “\(f_1(x_1)=f_1(\pi\)” | Explicit example marker followed by unfinished formulas; no completed example or proof. | B23–B25 |
| 144:80–96 | doubtful quotient of \(\lambda\)'s; “\(\lambda_1\pi_1(x_1)=f_1(x_1)\chi\)” | Unfinished normalization followed by a live compatibility equation; the fraction's uncertainty is transcriptional. | B25 |

## Register-scope checklist for integration

| Clause in Hua findings register 84-chi-trivialised-extension-product | Evidence in the eleven handwritten pages | What remains outside that evidence |
|---|---|---|
| Local product coefficient \(b=b_1\otimes b_2\) | Explicit on scans 128 and 130; splitting-change formula on 130–134. | A consistent choice of every draft sign and transport convention, followed by the required descent proof. |
| Product for every \(\chi\) | The product formulas themselves do not require dividing by \(\chi\); their local cocycle has a positive-convention polynomial model. | A \(\gamma\chi=2\) condition on a later comparison cannot be silently imposed on the product itself; the bare \(\chi^{-1}\) notation on scan 138 also cannot supply a global hypothesis. |
| Functoriality | Isomorphisms and homomorphisms asserted on 126; compatible mixed-summand actions investigated on 124, 138 and 144. | Compatibility of morphisms with the chosen \(\chi\)-splittings; scan 144's initial submodule-preserving hypothesis is insufficient. |
| Pushout/pullback agreement | Desired strict-endpoint comparison, \(\gamma\chi=2\), and a candidate middle block on 128/142. | Existence in other regimes, endpoint sign conventions, actual descent and naturality of the candidate; comparison is not settled merely by conditional block data. |
| Symmetric monoidal category | Local multiplication and an attempted binary-change cocycle. | Unit, associator, symmetry and coherence, plus identification of C R11's local model with the claimed global category. |
| \(M=\mathcal O\) invertibility iff \(T_0\) generates \(L\) on \(V(\chi)\) | No occurrence of that criterion in these eleven pages. | C R12's local ideal criterion and its connection to Hua's particular \(T_0\), as well as any global claim. |
| \(\chi=2\) involution language | Explicit on scan 142, with a direct exact-sequence interpretation in B22. | Invertibility of \(2\), eigenspace splitting, and stronger algebra/trace identifications are not consequences. |

These are scope distinctions for the handwritten extension block only. They do not classify the intervening typed leaves or use their contents as extension-theoretic evidence.
