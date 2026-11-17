# Opening lecture: post-freeze research notes

## Scope and source discipline

These notes concern the frozen transcription of cote 136, scans **003–018**; references to “TeX line” mean the physical line of the individual frozen `pages/MPL_136_002-046_136_scanNNN.tex`, not an independently counted manuscript line. The transcription was frozen at **2026-11-17 15:04:33 UTC**, before this context research; no scan image was consulted and no transcription file was changed for these notes. Quoted words retain the frozen reading; typographic commands such as underlining are omitted from prose quotations, while uncertain symbols are identified rather than silently resolved.

The supplied `context/README.md`, `context/notes/RESULTS_STATE.md` and `context/hua_project/README.md` were read before drafting. The four `MPL_136_..._notes.md` files are supplied first-pass research notes, not independently verified later-page transcriptions. **“Hua” always means Michel Hua’s project, `hua_project/136.modern.tex`, its AI-produced modernised reading of cote 136**, not a diplomatic transcription or a result established here; its substantive text, including the full remainder beyond the lecture, was read. Hua’s page numbers are recorded as his page numbers, with the corresponding archive scan ranges supplied for navigation; later scans have not been visually checked in this research.

Every note below has an actual context search under the matching **L001–L044** identifier in `lecture_searches.json`; `lecture_searches.md` is its compact index. Context relations (**adds**, **restates**, **differs**, **contradicts**) describe what the supplied source contributes, not an adjudication of its unreviewed mathematical claims. A RESULTS_STATE identifier is a link to its stated question or result status, and does not upgrade a first-pass claim to a reviewed theorem. Own ideas are explicitly marked and assigned a confidence level with a reason; none is presented as new to mathematics.

## Historical framing and the move to divided powers

### L001 — The promised Historique is present, but its publication history is a separate question

**Kind:** documentary confirmation of a planning hypothesis. **Frozen anchor:** “1 Historique”; “Plan conf. IHES en 1976” — scan 003, TeX lines 5, 8. **Register:** WG2 §2.4 #5.

These words confirm that the present opening contains the author’s historical lecture plan, extending from differential forms through Sullivan on scans 003–004. Hua, `136.modern.tex`, “Le plan de la conférence : historique (pages 2 et 3)” (**restates**, scans 003–004), supplies an interpretive account, while `MPL_136_047-094_notes.md`, R059 (package scans 048–094), had identified the missing earlier leaves as a documentary gap that these pages now **partly fill**. Neither this confirmation nor Hua’s reading verifies the context README’s further statement that Carmona printed two pages, since that publication was not supplied.

### L002 — The historical attribution contains an explicit question

**Kind:** self-flagged historical attribution. **Frozen anchor:** “Notion des formes diff. (Poincaré ?)” — scan 003, TeX line 10. **Register:** WG2 §2.4 #5, historical context only.

The question mark concerns the attribution of the notion of differential forms and should remain a question in the historical account. Hua, `136.modern.tex`, “Le plan de la conférence : historique (pages 2 et 3)” (**restates**, scans 003–004), arranges the same historical stations, but this supplied modernisation is not independent evidence settling priority. The adjacent attribution “conjecturé par E. Cartan” at TeX line 16 is likewise reported here as what this manuscript says, without converting its compressed historical sketch into a verified chronology.

### L003 — Sullivan’s homotopy equivalence is recalled with a reservation

**Kind:** self-flagged recollection of a theorem. **Frozen anchor:** “simplement connexe (sauf erreur)” — scan 004, TeX line 3. **Register:** follow-ups @305, comparison baseline; WG2 §2.4 #5.

The opening recalls recovery of the rational homotopy type and a categorical equivalence, then refers to Sullivan’s papers for minimal models at TeX line 7. Hua, `136.modern.tex`, “Le plan de la conférence : historique (pages 2 et 3)” (**differs**, scans 003–004), expressly adds finite-type restrictions in an editorial footnote, so those restrictions must not be backfilled into the frozen sentence. The explicit finiteness qualifications in this manuscript occur later in the author’s own integral questions, scans 012–013; the supplied context does not independently verify every hypothesis of the recalled rational theorem.

### L004 — The Sullivan comparison has a compressed acyclicity step

**Kind:** unproved assertion and proof obligation. **Frozen anchor:** “ce qui se vérifie facilement” — scan 005, TeX line 9. **Register:** WG2 §2.4 #5; follow-ups @305, methodological comparison.

The argument distinguishes the algebraic Poincaré lemma on each affine simplex from acyclicity of each simplicial coefficient object, and its global cohomology conclusion needs both assertions. Hua, `136.modern.tex`, “La démonstration de Sullivan, et l’obstacle sur Z (pages 3 à 5)” (**restates**, scans 004–006), retains this two-part proof rather than supplying all the acyclicity details. The parenthetical extension to smooth, real-analytic and complex-analytic forms on the same frozen line is an additional asserted range of applicability whose relevant coefficient objects and acyclicity must be specified.

### L005 — The integral ambition is explicitly qualified by possible obstruction theorems

**Kind:** expectation and self-flagged obstacle. **Frozen anchor:** “Mais il paraît qu’il y a des ths contre !” — scan 005, TeX line 12. **Register:** WG2 §2.4 #5; follow-ups @305.

The margin asks for a functorial integral anticommutative cochain algebra computing integral cohomology, but immediately acknowledges reported obstructions; its final “quand même” versus “en un sens” remains an uncertain frozen reading. `MPL_136_047-094_notes.md`, R050–R051 (scans 069, 074–077, 081, 083, 094), and `MPL_136_189-234_notes.md`, R004 (scans 215, 217, 233), **add** already-recorded tests and hypotheses against stronger unweighted interpretations, rather than refuting every weighted construction. Hua, `136.modern.tex`, “La démonstration de Sullivan, et l’obstacle sur Z” (**restates**, scans 004–006), also treats this as the motivating obstacle; no external obstruction theorem has been independently checked here.

### L006 — The simplex of size one is a rejected proposal

**Kind:** discarded construction, followed by a replacement. **Frozen anchor:** “Donc on aurait envie de prendre”; “mais ce n’est plus” — scan 006, TeX lines 3, 7. **Register:** WG2 §2.4 #5; follow-ups @305.

The author rejects the naive divided-power quotient with relation \(\sum X_i=1\), because solving for a coordinate produces an element outside the given divided-power ideal, and replaces it with \(\sum X_i=t\) for \(t\in J\). Hua, `136.modern.tex`, “Le simplexe de taille t”, under “La construction (pages 5 à 8)” (**restates**, scans 006–009), explains that repair through the triple \((S,J,t)\). This is a local withdrawal of the proposed coordinate-elimination argument, not evidence that the later parameterized construction was itself abandoned.

### L007 — Resolution of S and augmentation to S/J are different assertions

**Kind:** unproved assertion with a concrete algebraic proof target. **Frozen anchor:** “est une résolution de S” — scan 007, TeX line 12. **Register:** WG2 §2.4 #5; follow-ups @305.

The displayed algebra is augmented to \(S/J\), but the differential complex is asserted to resolve \(S\); those targets cannot be interchanged in the comparison argument. Hua, `136.modern.tex`, “Le simplexe de taille t” (**restates**, scans 006–009), uses the elimination of one coordinate, while `MPL_136_189-234_notes.md`, R023 (scans 219–222), **adds** the later rank-one comparison of four algebraic complexes that identifies why the divided-power de Rham differential has the necessary coefficient rather than the ordinary-polynomial obstruction. Tensoring these elementary contractions and checking the augmentation provides the natural proof target, without yet establishing the separate global acyclicity requirement.

### L008 — The manuscript expressly denies ordinary S-cohomology for an arbitrary triple

**Kind:** explicit limitation of the construction. **Frozen anchor:** “Mais on ne peut dire en général quelle est sa cohomologie”; “elle ne sera pas isom.” — scan 007, TeX line 30. **Register:** WG2 §2.4 #5; follow-ups @305.

This sentence rules out reporting the arbitrary \((S,J,t)\) construction as an ordinary \(S\)-cohomology model uniformly in the simplicial set. Hua, `136.modern.tex`, “Le simplexe de taille t” (**restates**, scans 006–009), preserves this limitation, and its “La version complétée et filtrée (pages 232 à 240)” (**adds**, scans 233–241) discusses later hypotheses rather than removing the restriction. `MPL_136_235-281_notes.md`, N02–N03 (scans 235–239), further **adds** a conditional filtered comparison and records withdrawal of an unfiltered formula, reinforcing the need to keep each coefficient and weight convention visible.

## Weights, acyclicity, shadows and rational specialization

### L009 — The universal comparison is indexed by total weight

**Kind:** unproved structural assertion. **Frozen anchor:** “Algèbre … bigraduée”; “diff de bidegré -1,+1” — scan 008, TeX line 36; “covariante de k” — scan 009, TeX line 10. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

For the universal choice \(S=k\{T\}\), the complementary degree \(p\) and exterior degree \(q\) are distinct, and the differential preserves total weight \(w=p+q\). Hua, `136.modern.tex`, “Conventions, valables pour tout le dossier” and “La cohomologie” (**restates**, scans 008–010), explicitly tracks these conventions, while `MPL_136_189-234_notes.md`, R001–R002 and R043 (scans 204, 221, 227–233), **adds** later formulas using total weight as the first index. The candidate label in the Hua findings register should therefore be reconciled with an asserted formula and proof sketch in these pages, not used to call every step a conjecture or to identify a fixed complementary degree with a subcomplex.

### L010 — The exterior grading, not total weight, supplies the parity test

**Kind:** own idea: diagnostic of the modernisation’s grading convention. **Frozen anchor:** “alternée (anticomm. + carré des éléments de degré impair nuls)” — scan 008, TeX line 36. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows. **Confidence:** high for the algebraic diagnostic, because it uses one free divided-power generator over \(\mathbb Z\).

Hua, `136.modern.tex`, “Le cas universel S = k{T}” (**differs**, scans 008–009), adds “alternée pour le degré total,” whereas the frozen sentence names both gradings without making that parity choice explicit. For \(k=\mathbb Z\), \(T\) has total weight one and exterior degree zero, but \(T^2=2T^{(2)}\ne0\), so alternation by total weight cannot hold for this algebra. Hua’s later “Fonctorialités” and “Les algèbres de De Rham spéciales (pages 93 à 107)” (**contradict that earlier gloss**, scans 083–087 and 094–108) instead state alternation in the exterior degree, consistently with the formula. This diagnoses an interpretive mismatch and leaves the frozen wording unchanged.

### L011 — Applying Γ needs an actual simplicial contraction

**Kind:** unproved assertion with a specified homotopy requirement. **Frozen anchor:** “homotope à 0 donc”; “si p≠0” — scan 009, TeX line 12. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

The implication is justified by an actual simplicial homotopy that survives application of the functor, not by the general assertion that a nonlinear divided-power functor preserves acyclic complexes or arbitrary quasi-isomorphisms. `MPL_136_189-234_notes.md`, R034 and R040 (scans 227–233), **adds** this distinction, and Hua, `136.modern.tex`, “Calculs d’homotopie (pages 226 à 232)” (**adds**, scans 227–233), identifies the normalized two-term contraction underlying \(\Phi_*\). The later warning “faux tel quel, à arranger !” reported by `MPL_136_095-141_notes.md`, N05–N06 (scan 100), concerns a different flat-plus-flasque shortcut and must not be mistaken for a retraction of this specific contraction argument.

### L012 — The frozen p=0 is a mathematical reading question

**Kind:** reading question; internal inconsistency. **Frozen anchor:** “si p=0” — scan 009, TeX line 14, following “si p≠0” at line 12. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

The consecutive assertions conflict as written, and the subsequent “acycliques sauf le dernier” makes the zero complementary-degree endpoint exceptional. Hua, `136.modern.tex`, “La cohomologie” (**differs**, scans 009–010), uses the nonzero condition, while `MPL_136_189-234_notes.md`, R040–R041 (scans 231–233), **adds** the later positive-complementary-degree resolution and endpoint calculation. These comparisons support a future reading check but do not authorize changing the frozen \(p=0\).

### L013 — The last term requires a truncation argument, not acyclicity

**Kind:** compressed proof obligation. **Frozen anchor:** “acycliques sauf le dernier”; “tronquée en … degré n” — scan 009, TeX line 20. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

The asserted formula computes \(H^q(X,k)\) in the total-weight strand \(w\) only for \(q\leq w\), with zero above that bound; the last term is not asserted acyclic. `MPL_136_047-094_notes.md`, R029 (scans 081–082), and `MPL_136_189-234_notes.md`, R041 (scan 233), **add** the dimension-shifting or smart-truncation justification needed at the endpoint. Hua, `136.modern.tex`, “La cohomologie” and “Calculs d’homotopie” (**restates**, scans 009–010 and 227–233), supplies the same intended pattern, but exactness of the coefficient strand and the relevant section-acyclicity remain separate things to verify.

### L014 — H⁰ and Hq coexist in the frozen shadow formula

**Kind:** reading question; incompatible displayed indices. **Frozen anchor:** \(H^0(\mathcal X_*,k)\otimes_k k\{T\}\) — scan 010, TeX lines 3, 5; \(H^q(\mathcal X_*,k)\otimes_k k\{T\}\) — line 15. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

The first two occurrences use \(H^0\) although the question fixes exterior degree \(q\); the reindexed formula later on the same page uses \(H^q\). Hua, `136.modern.tex`, “Les ombres (pages 9 à 11)” (**differs**, scans 010–012), consistently gives the latter, and `MPL_136_189-234_notes.md`, R001 (scan 233), **adds** the later degree-by-degree comparison. The natural semantic resolution is therefore visible in the context, but both frozen readings remain part of the evidence.

### L015 — Multiplicative compatibility is weighted compatibility

**Kind:** unproved assertion with a necessary product qualification. **Frozen anchor:** “Ces isom. sont compatibles avec les structures multiplicatives” — scan 010, TeX line 17. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

In total weights \(r,s\), compatibility means the ordinary cup product is multiplied by \(\binom{r+s}{r}\), as dictated by \(T^{(r)}T^{(s)}\), and does not identify each weight copy’s product with the ordinary cup product without that factor. `MPL_136_047-094_notes.md`, R030 (scans 080–082), and `MPL_136_189-234_notes.md`, R003 (scans 204, 217, 231, 233), **add** this explicit qualification; Hua, `136.modern.tex`, “Les ombres” (**restates**, scans 010–012), includes the binomial multiplication. Recovery from a whole system of weighted pairings is a separate claim, already illustrated in `MPL_136_095-141_notes.md`, O03 (scans 113, 117, 135, 141), and `MPL_136_235-281_notes.md`, N73 (scans 237–239, 273), rather than a claim that ordinary integral cohomology itself carries the displayed strict divided powers.

### L016 — An ombre is defined here and recovery is assumed before its later proof

**Kind:** definition followed by an unproved reconstruction assertion. **Frozen anchor:** “la qième ombre de M”; “Cette ‘théorie des ombres’ étant … acquise” — scan 011, TeX lines 3, 5; “supposée” remains marked uncertain in line 5. **Register:** Hua findings register 136-shadow-full-faithfulness; gap g1048; MPL_121_001-048 Q1; MPL_152+120 Q1-06.

The page defines the \(q\)-th shadow as \(\tau_q(M\otimes_k k\{T\})\) and asserts recovery both of \(M\) and of pairings from sufficiently high shadows. Hua, `136.modern.tex`, “Les ombres” (**restates**, scans 010–012), and its later “Les foncteurs « ombres » \(\omega_N\)” and “Le théorème sur \(M\otimes_k S\)” (**adds**, scans 023–035), distinguish this opening promise from the later arithmetic argument; the registered finite-tail result is credited to Hua’s project and prior context, not reproved as a new result here. This supplies a concrete early answer to the register’s requests for a definition of “ombre,” without identifying every occurrence of “tubulure” in other cotes with this construction.

### L017 — The derived cup-product promise is stronger than linear reconstruction

**Kind:** unproved strengthening. **Frozen anchor:** “en raffinant un peu”; “plus l’accouple-” — scan 011, TeX line 5, continued by the derived cup-product display on scan 012, TeX lines 3–5. **Register:** gap g1048, with its prior-result references g1031, g1041, g1034, g1035 and g1080.

The passage promises not only the graded cohomology ring but \(R\Gamma(X,k)\) in \(D(k)\) together with \(R\Gamma\otimes_k^L R\Gamma\to R\Gamma\). `MPL_136_235-281_notes.md`, N39–N40 (scan 273), **adds** the separate derived-unit and multiplication obligations, while Hua, `136.modern.tex`, “Reconstruire un complexe à partir de son ombre (pages 262 à 276)” (**restates and qualifies**, scans 263–277), flags gaps in the later argument. RESULTS_STATE gap g1048 now reports a repaired linear reconstruction in a specified Gabriel quotient but explicitly leaves its monoidal compatibility open; neither that repair nor the underived finite-tail theorem supplies the multiplication statement automatically.

### L018 — Setting T=1 rationalizes, and its global formula needs care

**Kind:** unproved comparison assertion; own diagnostic of the context’s product warning. **Frozen anchor:** “quelque soit k” — scan 012, TeX line 14, in the comparison by \((T-1)\). **Register:** WG2 §2.4 #5; follow-ups @305. **Confidence:** high for the product diagnostic, because multiplication by a common scalar acts componentwise.

The ordinary coefficient quotient \(\mathbb Z\{T\}/(T-1)\) is \(\mathbb Q\), as already explained in `MPL_136_047-094_notes.md`, R048 (scans 069, 080–082), which **adds** the factorial-invertibility argument and receives credit for that diagnostic. Hua, `136.modern.tex`, “Remarques et problèmes”, item a (scan 012), **adds** a finite-case verification and an imprecisely worded warning that passage to the quotient does not commute with infinite products. For ordinary ungraded products with a common scalar \(T\), multiplication by \(T-1\) acts componentwise, so that quotient actually does commute with the product. The concrete hazard for the bigraded model is direct-sum totalization over weights before specialization, as tested in L019; the coefficient calculation alone does not prove the global formula for every infinite simplicial set.

### L019 — A discrete-space test exposes the infinite-product qualification

**Kind:** own idea: conditional counterexample to an unrestricted global specialization. **Frozen anchor:** “quelque soit k” — scan 012, TeX line 14. **Register:** follow-ups @305. **Confidence:** high under the explicitly stated direct-sum-of-weights convention; the distinction follows from common denominators.

For a countably infinite discrete simplicial set \(X\), if the bigraded sections are assembled by direct sum over weights before quotienting, the degree-zero comparison becomes \((\mathbb Z^{\mathbb N})\otimes\mathbb Q\longrightarrow\mathbb Q^{\mathbb N}\). Its image consists of sequences with one common integer denominator, so the sequence \((1/p_j)_j\) for distinct primes \(p_j\) is not in the image. This **adds** an explicit diagnostic to the infinite-product warning credited to Hua, `136.modern.tex`, “Remarques et problèmes”, item a (scan 012), rather than claiming that warning as our discovery. For the ungraded product one instead has \((\prod_j\mathbb Z\{T\})/(T-1)\prod_j\mathbb Z\{T\}\simeq\prod_j\mathbb Q\), so the diagnostic concerns the direct sum over weights before specialization, not quotienting an ordinary product by a common principal relation.

### L020 — The general (t−1) specialization lies beside a marginal question mark

**Kind:** assertion beside a marginal question of uncertain attachment. **Frozen anchor:** “Et plus gén. encore”; marginal “?” — scan 012, TeX lines 18–23. **Register:** follow-ups @305; WG2 §2.4 #5.

The bracketed generalization compares \(C_{\mathrm{DRpd}}(X;S,J,t)/(t-1)\) with Sullivan forms over \(S_{\mathbb Q}/(t-1)\); the nearby marginal question mark warrants caution, although its precise attachment is not secure. Hua, `136.modern.tex`, “Remarques et problèmes”, item a (**restates**, scan 012), retains this specialization while explaining the coefficient algebra. The later conditional filtered theory in `MPL_136_235-281_notes.md`, N02–N03 (scans 235–239), **differs** from this quotient claim and cannot be invoked as a blanket proof; the global limit/quotient issue in L019 remains relevant.

## Homotopy reconstruction and the stated missing work

### L021 — The importance of divided powers is a stated conviction

**Kind:** expectation. **Frozen anchor:** “Je suis convaincu que la structure à p.d.” — scan 012, TeX line 25, continued by “est importante” at line 29. **Register:** follow-ups @305; WG2 §2.4 #5.

The author deliberately includes divided powers among “ttes ses structures” in the homotopy-recovery question, so an additive or merely multiplicative comparison does not exhaust his proposal. Hua, `136.modern.tex`, “Remarques et problèmes”, item b and “Ce qui n’est pas établi” (**restates**, scans 012–013), explicitly leaves that integral homotopy question open. The later discussion of universal additive invariants in Hua, “L’invariant additif universel (pages 310 à 317)” (**adds**, scans 311–318), likewise stresses extra operations beyond the underlying chain complex; it does not prove that the particular opening PD structure contains them all.

### L022 — Compatibility with d does not by itself settle descent to cohomology

**Kind:** unpursued implication requiring proof. **Frozen anchor:** “d(x^{(n)})=x^{(n-1)}dx” — scan 007, TeX line 11; “compatible aux p.d.” — scan 008, TeX line 36. **Register:** follow-ups @305, expressly open PD-descent item.

The identity proves that the displayed divided powers of suitable closed elements remain closed, but independence of the representative requires a separate statement about boundaries and the precise domain of those operations. `MPL_136_189-234_notes.md`, R022 (scans 217, 220, 233), **adds** exactly this distinction, and Hua, `136.modern.tex`, “L’algèbre alternée libre à puissances divisées” and “Gribouillis, suite : la structure à puissances divisées induite” (**adds**, scans 215–217 and 329–335), records later unfinished work on compatible and induced structures. No theorem asserting ordinary divided powers on the recovered unweighted cohomology ring should be inferred from the opening compatibility formula, especially after the weighted-product qualification in L015.

### L023 — The proposed derived category of virtual complexes needs a precise definition

**Kind:** proposed construction with an uncertain question mark. **Frozen anchor:** “soient des q-ombres” followed by a frozen `\unsure{?}`; “en ‘inversant’ les flèches” — scan 013, TeX line 4. **Register:** gap g1004; follow-ups @305.

The “virtual” DR complexes combine bigrading, augmentation, differential, divided powers and a shadow condition followed by an uncertain question mark before their quasi-isomorphisms and localization are fully fixed. Hua, `136.modern.tex`, “Remarques et problèmes”, item b (**restates**, scans 012–013), is followed much later by “Les théories de De Rham admissibles (pages 110 à 120)” (**adds**, scans 111–121), where admissibility and \(\tau_\infty\) comparisons make a related framework more precise. `MPL_136_095-141_notes.md`, N18–N36 (scans 111–121), and RESULTS_STATE gap g1004 retain the connectedness/simple-connectedness of the localized groupoid as an open uniqueness question, not an established identification with the opening virtual category.

### L024 — The integral homotopy equivalence is explicitly a question

**Kind:** conjectural equivalence. **Frozen anchor:** “on peut se demander si”; “induit une équivalence” — scan 013, TeX line 10. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows, scope limitation.

The stated domain is connected, simply connected spaces with a finiteness condition, and the target is restricted by \(H^0\simeq k\), \(H^1=0\), and finite generation; the ambiguous frozen \(H^i_*\) notation is not silently normalized. Hua, `136.modern.tex`, “Ce qui n’est pas établi” and “Remarques et problèmes”, item b (**restates**, scans 012–013), agrees that no equivalence is proved. The frozen margin on scan 012, TeX line 29, specifies “disons les \(H_i\) … de t.f.”, whereas Hua’s item-b footnote instead names \(\pi_i\), a hypothesis-reading **difference** retained here rather than transferred into the transcription. Its later “Retrouver X à partir de ses cochaînes ; l’algèbre des opérateurs (pages 341 à 345)” (**adds**, scans 342–346) asks a new reconstruction question and begins examples rather than resolving this one; the broader connected-nilpotent formulation in follow-ups @305 is the research register’s extension, not the literal opening claim.

### L025 — The negative result on operations concerns a restricted attempted method

**Kind:** partial negative result, reported without full proof here. **Frozen anchor:** “résultats partiels négatifs”; “on ne trouve rien d’intéressant” — scan 014, TeX line 4. **Register:** claims #243; follow-ups @305; MPL_133 B10, application question only.

The negative conclusion concerns reconstructing Steenrod- or Whitney-type operations using multiplicative automorphisms of the universal simplicial DRpd algebra, not every conceivable operation on the entire enhanced object. Hua, `136.modern.tex`, “Le schéma en groupes des automorphismes (pages 173 à 179)” and “La caractéristique 2, et les endomorphismes de A₁ (pages 181 à 199)” (**adds**, scans 174–200), develops that method, but RESULTS_STATE claims #243 warns that the retained parameter presentation needs additional multiplication relations before its classification is accepted. Hua’s “Notes : Eilenberg–Zilber et les opérations de Steenrod (pages 356 à 360)” (**differs**, scans 357–361) records another approach with higher chain data, and is not evidence that the opening reconstruction problem was solved.

### L026 — Integral minimal models are requested and expressly not constructed

**Kind:** stated desideratum and acknowledged absence of work. **Frozen anchor:** “Il faudrait sans doute donner des modèles minimaux à la Sullivan”; “Je n’ai rien fait dans cette direction” — scan 014, TeX line 6. **Register:** follow-ups @305.

The intended use is to express homotopy groups through the integral DRpd object under connectivity and finiteness assumptions. Hua, `136.modern.tex`, “Ce qui n’est pas établi” and “Remarques et problèmes”, item d (**restates**, scan 014), preserves this explicit limit. Its later “Les algèbres de De Rham spéciales”, subsection “Sur \(\widehat{\Delta}\)” (pages 101 à 107) (**differs**, scans 102–108) offers an economical standard object and comparison zigzags, not the missing integral minimal-model theorem.

### L027 — Künneth is missing, with flatness named as the obstruction to the naive argument

**Kind:** acknowledged missing theorem and suspected technical obstacle. **Frozen anchor:** “Je n’ai = pas développé une formule de Künneth”; “on ne peut sans doute supposer … plats” — scan 014, TeX line 6. **Register:** follow-ups @305; gap g1048, related multiplicative issue.

The relevant possible nonflatness is over \(k\{T\}\), so flatness of individual underlying \(k\)-modules would not by itself justify the desired product formula. Hua, `136.modern.tex`, “Remarques et problèmes”, item d (**restates**, scan 014), and “Ce qui n’est pas établi” leave it open, while `MPL_136_189-234_notes.md`, R025 and R038 (scans 221, 229–231), **adds** narrower tensor/Künneth methods under flatness or explicit free-model hypotheses. Those later arguments suggest checking a derived tensor comparison and its PD compatibility, but do not constitute the unqualified theorem requested here.

## Dual chains, coefficient changes and colimits

### L028 — The dual object is a corepresenting object with all its structures

**Kind:** announced construction and compatibility assertion. **Frozen anchor:** “Il est possible de même de définir”; “compatible avec … les structures” — scan 015, TeX lines 9, 13. **Register:** WG2 §2.4 #5; follow-ups @305.

The promised differential coalgebra with divided copowers is characterized through \(\operatorname{Hom}_k(C_{\bullet\bullet},k')\) for every coefficient \(k\)-algebra \(k'\), so this is stronger and more carefully variable than taking one ordinary linear dual. `MPL_136_095-141_notes.md`, N38, N42 and N51 (scans 123–127, 133), **adds** the later corepresentability construction and identifies structural compatibilities still needing verification. Hua, `136.modern.tex`, “La version duale : coalgèbres et chaînes de De Rham (pages 122 à 134)” and “Le yoga coalgèbres → Algèbres (pages 143 à 151)” (**adds**, scans 123–135 and 144–152), makes this functorial viewpoint explicit; credit for that modernized explanation belongs to his project.

### L029 — Base change is promised at the chain-object level

**Kind:** unproved base-change assertion. **Frozen anchor:** “On aura d’ailleurs” — scan 015, TeX line 15, before the tensor formula at line 17. **Register:** WG2 §2.4 #5; follow-ups @305.

The formula identifies the constructed chain object after extension of coefficients and does not by itself identify cohomology after arbitrary base change. `MPL_136_095-141_notes.md`, N48 and N52 (scans 129, 135), **adds** the same distinction and records the later integral construction from which chain-level base change is intended to follow. Hua, `136.modern.tex`, “La version duale : coalgèbres et chaînes de De Rham” (**restates and elaborates**, scans 123–135), supplies that continuation, without removing the usual need to account for derived tensoring when a cohomological comparison is sought.

### L030 — Preservation of arbitrary colimits is an ordinary categorical claim

**Kind:** unproved functorial assertion. **Frozen anchor:** “commute aux … quelconques (pas néc. … filtrantes)” — scan 015, TeX line 21. **Register:** WG2 §2.4 #5; follow-ups @305.

The intended chain functor is covariant and preserves arbitrary colimits in the simplicial input, while its cochain counterpart reverses them to limits. `MPL_136_095-141_notes.md`, N44–N46 (scans 127–129), **adds** the colimit-over-simplices construction supporting this assertion, and Hua, `136.modern.tex`, “Notations simpliciales. Constructions universelles (pages 300 à 309)” (**adds**, scans 301–310), later gives the wider representable/colimit framework. Ordinary preservation of colimits does not establish preservation of homotopy colimits or invariance under weak equivalences; those are additional comparison properties.

### L031 — The no-finiteness proposal should be formulated with completion in view

**Kind:** own idea: precise test of the proposed dual strategy. **Frozen anchor:** “sans condts de finitude”; “au lieu de son ‘dual’” — scan 015, TeX line 19. **Register:** follow-ups @305. **Confidence:** high for the linear distinction, because Hom converts direct sums to products; conditional for a full structured homotopy theory.

A useful audit is to state separately the direct-sum chain object, its product-valued dual, and the restricted or completed algebra carrying the dual operations, using \(\operatorname{Hom}_k(\bigoplus_w M_w,k)=\prod_w\operatorname{Hom}_k(M_w,k)\). This **builds on**, rather than discovers anew, `MPL_136_095-141_notes.md`, N39–N41 (scans 125–127) and O11 (scans 125, 127, 133, 139), which already distinguishes polynomial representing modules from completed divided-power series. Hua, `136.modern.tex`, “La version duale : coalgèbres et chaînes de De Rham” and “Coalgèbres et comodules (pages 152 à 159)” (**adds**, scans 123–135 and 153–160), supplies the later completion and continuity setting. The test would prevent finite-weight duality from being silently promoted to an unrestricted reflexivity or homotopy-reconstruction theorem.

## Faisceautisation and the stronger D-structure

### L032 — Internal definition does not yet provide the derived pushforward

**Kind:** asserted internal construction followed by a program. **Frozen anchor:** “Il y a une définition évidente”; “Anneau comm. d’un topos” — scan 016, TeX line 5. **Register:** WG2 §2.4 #5; follow-ups @305.

Internalizing the algebraic definition over a ring object in a topos is distinct from constructing the structured \(Rf_*\) requested in the next sentence. Hua, `136.modern.tex`, “Faisceaux tests sur un topos ; la condition de De Rham (pages 79 à 90)” (**adds**, scans 080–091), later specifies flat cokernels, universal acyclicity and comparison maps, and `MPL_136_047-094_notes.md`, R027–R032 and R039 (scans 080–091), records those concrete conditions. The opening therefore supplies a faisceautisation program, not by itself a definition of a unique geometric “topos de De Rham” or an identification with a different modern de Rham site.

### L033 — Existence of suitably flasque structured replacements is explicitly open

**Kind:** self-flagged existence question. **Frozen anchor:** “mais y en a-t-il tjrs ?” — scan 016, TeX line 5. **Register:** WG2 §2.4 #5; gap g1004, related but distinct existence/uniqueness question.

The desired replacement must remain in an appropriate category of PD complexes while giving enough acyclicity to define derived direct images. `MPL_136_047-094_notes.md`, R027–R031 (scans 080–082), **adds** later sufficient test-object hypotheses, whereas `MPL_136_095-141_notes.md`, N04–N06 (scans 098–100), records a false flat/flasque-to-contractible shortcut that **limits** one attempted construction. Hua, `136.modern.tex`, “Réduction à l’algèbre standard” (pages 97 à 100) (**adds**, scans 098–101), preserves that correction, so neither internal algebraic definability nor the later uniqueness conjecture settles this existence question in every topos.

### L034 — The Deligne question is cosimplicial, and the later “Non” answers a narrower condition

**Kind:** reported open problem and reading question. **Frozen anchor:** “le Pb est ouvert — et posé par Deligne”; “topos des ens. cosimpliciaux” — scan 016, TeX line 5. **Register:** WG2 §2.4 #5; follow-ups @305, scope qualification.

Hua, `136.modern.tex`, “Remarques et problèmes”, item g (**differs**, scan 016), paraphrases the example using \(\widehat\Delta\), while the frozen sentence explicitly says cosimplicial sets. `MPL_136_047-094_notes.md`, R040 (scan 091), and Hua, “La condition de De Rham” (**adds**, scan 091), later record an emphatic “Non” for the existence of the specified test embedding in the cosimplicial topos. That later negative answer refines the construction program but is not automatically a proof that every possible structured derived pushforward in the earlier Deligne question is impossible; the two conditions must first be identified precisely.

### L035 — The paracompact case is a tentative recollection

**Kind:** self-flagged positive expectation. **Frozen anchor:** “Mais sauf erreur”; “si … sont exacts” — scan 016, TeX line 5, with “souvenirs” uncertain. **Register:** WG2 §2.4 #5.

The author tentatively recalls a construction for paracompact topological spaces, without naming its source or specifying all the site and resolution hypotheses here. Hua, `136.modern.tex`, “Remarques et problèmes”, item g and “La condition de De Rham” (**restates and adds**, scans 016 and 091), preserves the uncertainty around the topological case, while `MPL_136_047-094_notes.md`, R039 (scan 091), records examples asserted without a proof in that extract. This should be catalogued as a promising stated special case, not generalized into a theorem for arbitrary topoi.

### L036 — The larger D-complex is claimed to resolve k and recover C

**Kind:** structural assertion with a frozen index question. **Frozen anchor:** “résolution de k”; “Coker de la multiplication par dT” — scan 017, TeX line 14, with the kernel displays at lines 16–22. **Register:** follow-ups @305; WG2 §2.4 #5.

The object \(D_*^{\bullet\bullet}=\Gamma\Phi_*\otimes\Lambda\Phi_*\) is presented as an augmented resolution of \(k\), and \(C_*\) is recovered by quotienting by \(dT\), then by a shifted-kernel description. `MPL_136_047-094_notes.md`, R019 and R021 (scans 074–076), and Hua, `136.modern.tex`, “Le complexe comme noyau de la multiplication par dT (pages 73 à 77)” (**adds**, scans 074–078), separate the resolution assertion from componentwise flasqueness and its zero-degree exception. Those later formulas may clarify the frozen \((p,q+1)\to(p,q+2)\) indices and dash at line 22, but they are not silently substituted here, and an objectwise resolution alone does not identify all of its sections with \(k\).

### L037 — The structural passage from D to C is expressly unfinished

**Kind:** self-flagged compatibility problem. **Frozen anchor:** “certaines structures (à expliciter…)” — scan 017, TeX line 24. **Register:** follow-ups @305; WG2 §2.4 #5.

The later warning “est faux” in `MPL_136_047-094_notes.md`, R020 (scans 074–075), **contradicts** an unqualified compatibility claim for the kernel realization, while R022–R024 (scans 075–077) **adds** the distinction between ambient multiplication and the product transported through the quotient description. In particular, the kernel embedding obtained by multiplication with \(dT\) has products zero in the ambient exterior algebra, so it cannot simply preserve the nonzero product intended on \(C\). Hua, `136.modern.tex`, “Le complexe comme noyau de la multiplication par dT” (**restates and develops**, scans 074–078), retains residual operations and axioms still to formulate; this is a substantive continuation of the opening “à expliciter,” not a reason to erase it.

### L038 — The “cohomological multiplicative PD structure” is a proposed stronger invariant

**Kind:** proposed construction with an unspecified universal property. **Frozen anchor:** “La structure multiplicative à pd cohomologique”; “en un sens convenable” — scan 017, TeX line 26. **Register:** follow-ups @305; WG2 §2.4 #5.

The author proposes an invariant from which both \(C\), \(D\) and Sullivan-type complexes could be reconstructed, but does not give its full definition or prove the asserted recovery here. Hua, `136.modern.tex`, “L’invariant additif universel (pages 310 à 317)” and “Gribouillis : coalgèbres et puissances divisées (pages 319 à 324)” (**adds**, scans 311–318 and 320–325), later discusses operations and additional structures beyond the universal additive object. These passages provide a concrete research direction for the opening promise, but their fragmentary operations do not by themselves establish the required enhanced invariant or its relation to homotopy types.

### L039 — The author does not know whether C, or even D, contains the stronger structure

**Kind:** explicit ignorance and conditional alternative. **Frozen anchor:** “J’ignore si les” — scan 017, TeX line 26; “Dans le cas contraire” — scan 018, TeX line 4. **Register:** follow-ups @305.

The ending qualifies the earlier equivalence question by allowing that even \(D\) might fail to recover all the proposed multiplicative PD cohomological structure, in which case the stronger structure would be the preferred algebraic candidate. Hua, `136.modern.tex`, “Remarques et problèmes”, item h and “Ce qui n’est pas établi” (**restates**, scans 017–018), preserves this uncertainty, and “Retrouver X à partir de ses cochaînes ; l’algèbre des opérateurs” (**adds**, scans 342–346) later develops another uncompleted reconstruction route. This is a stated conditional alternative rather than a proof that the scan 013 conjecture is false, and the finiteness, connectivity and suitable-derived-category qualifications remain part of the proposal.

## Notation, additional research tests and remaining frozen anomalies

### L040 — Historical “½ simplicial” must not be forced into Δinj

**Kind:** notation-to-semantics reading question, substantially clarified by the opening. **Frozen anchor:** “(et = simpliciale)” — scan 007, TeX line 18; also scan 004, TeX line 32. **Register:** PRETOT A.12; TOTASPH C.10, comparison only; WG2 §2.4 #5.

These explicit parenthetical equalities favor the historical usage that includes degeneracies, rather than an automatic modern semisimplicial interpretation indexed only by injections. Hua, `136.modern.tex`, “Conventions, valables pour tout le dossier” (**restates and clarifies**, citing his pages 3, 6, 301, corresponding to scans 004, 007, 302), makes that convention explicit, and his “Notations simpliciales. Constructions universelles” uses all ordinal maps later in scans 301–310. `MPL_136_189-234_notes.md`, R009 (scans 194, 227, 229, 231), and `MPL_136_235-281_notes.md`, N74 (scan 235 and cancelled scan 251), had left this as a convention check that the newly available opening **helps resolve**; PRETOT A.12 and TOTASPH C.10 concern specified indexing-category results and cannot be imported solely because the same word occurs.

### L041 — Higher coherent operations are a test for what “all its structures” might require

**Kind:** own idea: a research test, not a proposed solution. **Frozen anchor:** “type Steenrod ou Whitney” — scan 014, TeX line 4; “en un sens convenable” — scan 017, TeX line 26. **Register:** follow-ups @305; claims #243. **Confidence:** medium, because the later notes identify relevant extra data but no comparison to C or D has been constructed.

A useful next test is to ask which of the higher chain operations discussed later can be functorially constructed from the opening \(C\), \(D\), or their proposed stronger invariant, before attempting a homotopy classification. Hua, `136.modern.tex`, “Notes : Eilenberg–Zilber et les opérations de Steenrod” (**adds**, scans 357–361), describes operations involving symmetric-group resolutions and compatible chain maps, while “L’invariant additif universel” (**adds**, scans 311–318) stresses that bare additive chains omit multiplicative information. This extends those supplied leads without claiming that an \(E_\infty\) structure has already been extracted, that the final reading notes have the same authorship or status as the lecture, or that the partial negative automorphism result rules out the proposed test.

### L042 — The binomial comparison should be tested on structure maps, not just coefficients

**Kind:** own idea: sharpened experiment already suggested by the research register. **Frozen anchor:** “k{T}”; “dépendent de façon contravariante” — scans 008, TeX line 6, and 009, TeX line 10. **Register:** follow-ups @304; follow-ups @305. **Confidence:** medium for the proposed comparison test, because the associated-graded coefficient identity supplies a lead but not a compatible model.

The next concrete checks for the registered filtered-binomial comparison are the simplex relation \(\sum X_i=T\), the differential, degeneracies and coefficient functoriality, followed by the derived realization comparison. `MPL_136_047-094_notes.md`, R052 (scans 080–083), already **adds** \(\operatorname{gr}\operatorname{Int}(\mathbb Z)\simeq\Gamma_{\mathbb Z}(T)\), and follow-ups @304 explicitly requests these compatibilities, so neither that identity nor the comparison program is claimed as new here. Hua, `136.modern.tex`, “Le cas universel S = k{T}” and “La version complétée et filtrée” (**adds usable formulas**, scans 008–009 and 233–241), supplies concrete structure maps on which a future comparison can succeed or fail; equality of associated-graded coefficient rings alone does not identify the models.

### L043 — The ordinary dual formula has unreconciled coefficient symbols

**Kind:** reading question. **Frozen anchor:** “pour k′ … variable”; \(\operatorname{Hom}_{\mathbb Z}(C_\bullet(\mathcal X_*,k),k)\) — scan 015, TeX lines 4, 6. **Register:** WG2 §2.4 #5, chain-construction context.

The surrounding prose varies a \(k\)-algebra \(k'\), but the first frozen display keeps target \(k\) and subscript \(\mathbb Z\) after the chain coefficient has been changed to \(k\); the subsequent PD display instead writes \(\operatorname{Hom}_k(-,k')\). Hua, `136.modern.tex`, “Remarques et problèmes”, item e (**differs**, scan 015), gives a normalized integral starting version, while `MPL_136_095-141_notes.md`, N51–N54 (scans 133–135), **adds** the later explicit coefficient-variable formulation and its own notation questions. These sources clarify the intended distinction but do not repair the frozen formula or license an unrestricted identification of \(\mathbb Z\)-linear and \(k\)-linear duals.

### L044 — The diagonal arrow and the quotient define a reading question

**Kind:** reading question. **Frozen anchor:** “inclusion diagonale” on the arrow \(\Phi_{k*}\longrightarrow k_*\) — scan 008, TeX line 20; \(\Psi_{k*}=\Phi_{k*}/(k_*)\) — line 23. **Register:** follow-ups @305; Hua findings register 136-pd-de-rham-shadows.

The frozen arrow orientation conflicts with interpreting \(k_*\) as the diagonal submodule used in the next quotient. Hua, `136.modern.tex`, “Conventions, valables pour tout le dossier” and “Le cas universel S = k{T}” (**differs**, scans 008–009), explicitly writes \(k_*\subset\Phi_*\), and the later constructions in “Faisceaux tests sur un topos ; la condition de De Rham” (**adds**, scans 080–091) likewise start from an embedding. This is a reason to retain a clearly identified reading question for the frozen diagram, not to reverse its arrow after the source-independent transcription stage.

## Coverage and handoff

The opening supports a **functorial, bigraded divided-power construction** and an asserted **weightwise truncated integral comparison with binomially weighted products**, followed by a shadow-reconstruction program; it explicitly denies the uniform ordinary \(S\)-cohomology interpretation for arbitrary triples. The ordinary cohomology ring, its derived cup product, descent of divided powers, and complete integral homotopy type are different targets with different proof obligations. The current file covers the substantive lecture claims, reservations, proposed repairs and notation questions through scan 018; the independent shadow notes cover the later arithmetic argument in the present package, and the parent report handles title leaves, reused sheets, the documentary chronology and the H05/topos cross-checks.

Later-context coverage was not limited to the matching lecture paragraphs: Hua’s sections on test objects and De Rham conditions, standard models, admissibility and uniqueness, dual chains and coefficient functors, automorphisms, free PD algebras, homotopies, filtered completions, graded-module localization, universal constructions, additive invariants, induced PD structures, reconstruction operators and the closing Steenrod/Eilenberg–MacLane material were read. These supplied interpretations are credited as such throughout; none substitutes for an independent later-scan audit or an external literature search.
