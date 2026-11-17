# Research support: complete reading of Hua's modernised cote 12

## Scope and provenance

This research-only comparison was made after the primary agent froze the transcription. I read context/README.md, context/hua_project/README.md, all of context/notes/RESULTS_STATE.md, and all 2,934 lines of context/hua_project/12.modern.tex, and compared the latter with the frozen page fragments read-only; I did not view or transcribe the manuscript images and made no changes to the frozen files. “Hua” below always means **Michel Hua's project's AI-produced modernised reading of cote 12**, an interpretation supplied as context and not an independently reviewed result. Searches for each numbered topic in Hua, the supplied first Book II transcription and notes, and RESULTS_STATE are recorded with exact hits and page locators in records/hua_context_searches.json.

Hua's page numbers are the archive foliation, one less than current scan numbers, throughout the matched packet; this is verified by matching subjects and formulas, not inferred from numbers alone. References to portions of Hua outside the supplied 39 scans remain **out-of-packet context**, without any claim of inspecting those manuscript pages. The RESULTS_STATE orientation sentence “No Hua findings fall in these scans” is inaccurate as a search guide: substantial sections of Hua cover precisely these pages.

## Concordance

| Frozen scans,12.pdf | Hua foliation | Exact Hua section or subsection |
|---|---|---|
|051–052|50–51|“12) L'homomorphisme \(L(K)\to\mathbf M^+(K)\) et les invariants birationnels (pages 42 à 51)”|
|053–055|52–54|“13) Caractérisation galoisienne des filtrations (pages 52 à 54)”|
|056–057,059|55–56,58|“14) Invariants de Galois, théorèmes de commutation, et le motif de Lie (pages 55,56 et 58)”|
|058|57|“11) Le coniveau (pages 41,42 et 57)”|
|060|59|“15) La cohomologie absolue : les exigences (page 59)”|
|062–065|61–64|“Les propriétés demandées (pages 61 à 64)”|
|067|66|“La dualité absolue (pages 66 et 68)”|
|071,073|70,72|“Sur un corps fini : la suite de Hochschild–Serre et les poids (pages 70 et 72)”|
|074–080|73–79|“16) Points rationnels et cohomologie des variétés abéliennes (pages 73 à 79)”|
|082|81|“Une courbe sur un corps fini (page 81)”|
|084|83|“Calculs sur \(\mathbb Q_\ell(1)\) et \(\mathbb G_m\) (page 83)”|
|086–089|85–88|“VII.17) Formes positives (pages 85 à 88)”|
|090–092|89–91|“Le dictionnaire algébrique (pages 89 à 91)”|
|092–095|91–94|“Ce que la fonction \(L\) sait de la cohomologie (pages 91 à 94)”|
|096|95|“IX. Poids et niveaux d'espaces de cohomologie \(\ell\)-adiques (pages 95 à 100)”|
|061,072|60,71|Reused typescript, deliberately omitted from Hua's mathematical interpretation; its omission is not evidence of blankness.|

## Proposed note items

### H01 — Level remains distinct from weight

**File/scans:**12.pdf,051,054–055,058,094. **Kind:** unpursued implication. **Quote:** “type dimensionnel”; “une autre filtration que par les poids”. **Search:**H01. **Context:** Hua, “Les moutures, gardées distinctes”; “La filtration par le niveau,” foliation34–35; “Le niveau, troisième mouture,” foliation154 (the latter references outside packet). **Relation:** supports and adds explicit current witnesses. **RESULTS_STATE:**WG2 §2.4 #3; MPL_14_002-044 B04.

Hua identifies the \(D_i\) filtration here with the earlier level of semisimple motives and its later abstract formulation; the current pages support the link by repeatedly separating dimension type from weight and returning to level in the birational calculation. Tate twists change weight by two while preserving level, so the separate filters are necessary even before any conjectural comparison with coniveau. Cancelled058 remains evidence of an attempted connection, not an established theorem because Hua reorganises it under coniveau.

### H02 — The cancelled injectivity question still needs a precise target

**File/scan:**12.pdf,052. **Kind:** self-flagged / conjecture in cancelled draft. **Quote:** “est injectif, ou bijectif, du moins mod torsion”. **Search:**H02. **Context:** Hua, “12) L'homomorphisme…,” foliation51/current052 and preceding foliation48–49/outside packet. **Relation:** restates with scope limitation. **RESULTS_STATE:**WG2 §2.4 #3.

Hua correctly notices the question about the dimension-graded Grothendieck group and primitive motive classes, but its preceding counterexamples to birational reconstruction answer different assertions from the exact homomorphism written052. The entire leaf is cancelled, so record an abandoned formulation without attributing assent to either injectivity or bijectivity. Any answer must first fix the quotient, the primitive target and whether ruled varieties have already been killed.

### H03 — A Grothendieck-ring bijection does not recover extensions

**File/scan:**12.pdf,053. **Kind:** unpursued implication. **Quote:** “n'ont pas de facteurs simples isomorphes communs”. **Search:**H03. **Context:** Hua, “13) Caractérisation galoisienne…,” foliation52/current053. **Relation:** supports and bounds. **RESULTS_STATE:**WG2 §2.4 #3; MPL_15_087-138 L01.

The page explains injectivity on classes by separation of simple constituents of nonisomorphic simple motives, precisely the input Hua uses. This concerns the Grothendieck ring and its simple basis, without by itself recovering extensions or proving every realization morphism motivic. That distinction matters when connecting the later absolute Ext programme062–063 to the semisimple material053–059.

### H04 — Effectivity by integrality retains a hypothesis question

**File/scan:**12.pdf,054. **Kind:** conjecture / reading question. **Quote:** “à coefficients entiers”; “Conjectures de Tate”. **Search:**H04. **Context:** Hua, “13) Caractérisation galoisienne…,” foliation52–54/current053–055. **Relation:** agrees on proposed criterion, differs in retained hypothesis. **RESULTS_STATE:**MPL_14_002-044 M01; WG2 §2.4 #3.

Hua presents effectivity of a simple motive as equivalent to integrality of geometric Frobenius and explicitly treats the converse as conjectural, preventing the margin from being read as a proved theorem. Frozen054 deletes “simple,” whereas Hua retains simplicity, so the latter is an editorial restriction rather than secure live wording. Equivalence between integral coefficients and algebraically integral roots also presupposes rational characteristic polynomials; algebraic integrality alone does not make coefficients rational integers.

### H05 — Roots of unity and finite monodromy

**File/scans:**12.pdf,054–055. **Kind:** unpursued implication. **Quote:** “racines de l'unité”; “quotient fini”. **Search:**H05. **Context:** Hua, “13) Caractérisation galoisienne…,” foliation53–54/current054–055, finite-image footnote. **Relation:** supports the hypothesis warning. **RESULTS_STATE:**LM6 A.22,A.50; MPL_14_002-044 B04.

The inference from roots of unity to finite monodromy uses semisimplicity, as Hua notes: eigenvalues do not detect a nontrivial unipotent part. Grothendieck explicitly warns055 that the level-zero description does not extend naturally to a filtration of \(\pi_1\), giving a caution for cyclotomic-normalizer analogies rather than a normalizer criterion. It resolves neither LM6 A.22 nor the full profinite assertion recorded as LM6 A.50.

### H06 — Enveloping algebra versus actual group

**File/scans:**12.pdf,056–057. **Kind:** unpursued implication. **Quote:** “seulement l'algèbre enveloppante”. **Search:**H06. **Context:** Hua, “14) Invariants de Galois…,” foliation55–56/current056–057; supplied first Book II transcription16/005 (commutant of grading projectors),16/049 (semisimple-motive yoga). **Relation:** explicit limit on the correspondence-ring bridge. **RESULTS_STATE:**WG2 §2.3 #2,#7; WG2 §2.4 #3; MPL_14_087-132 M04; MPL_15_087-138 §111.

Hua preserves the N.B. that double commutants characterize spans and associative envelopes rather than actual Galois images. This directly bears on whether Lefschetz \(\mathfrak{sl}_2\) sits in the motivic group: equality of enveloping algebras supplies no such inclusion. The projective-line objection is already registered in MPL_14_087-132 M04 and MPL_15_087-138 §111 and should be cited rather than presented as new.

### H07 — The scalar exception in059 differs from Hua

**File/scan:**12.pdf,059. **Kind:** reading question / self-flagged. **Quote:** “Quelle est la partie ‘Algébrique’”; “réduit à \(\mathbf Z(0)\)”. **Search:**H07. **Context:** Hua, “14) Invariants de Galois…,” foliation58/current059, final paragraph and footnote. **Relation:** substantive difference. **RESULTS_STATE:**LM6 A.22; WG2 §2.4 #3.

Hua reads the proposed algebraic part away from finite fields as “nulle” and objects using the central weight cocharacter and homotheties, but frozen059 retains an inserted “réduit à \(\mathbf Z(0)\)” and an uncertain scalar-homothety abbreviation after deleted centre wording. Do not attribute the zero-part assertion confidently to the live manuscript: Hua's objection may address an earlier layer or a different reading. The meaning of “algébrique,” finite-field statement and corrected scalar exception remain questions, not a construction of the CM normalizer in LM6 A.22.

### H08 — Analytic and algebraic Lie algebras differ

**File/scans:**12.pdf,057–059. **Kind:** own idea / context audit. **Quote:** “l'image”; “indépendant de \(\ell\)”. **Search:**H08. **Context:** Hua, “14) Invariants de Galois…,” foliation56,58/current057,059, footnotes first identifying analytic Galois Lie algebra, then Tannakian Lie algebra. **Relation:** extra inference in Hua. **RESULTS_STATE:**WG2 §2.4 #3; LM6 A.22. **Confidence:**high for the distinction, by explicit matrix calculation.

Hua first treats \(\mathfrak g_\ell\) as the Lie algebra of the compact \(\ell\)-adic image, then explains \(\mathfrak g_M\) as \(\operatorname{Lie}G_M\), although Zariski closure can increase dimension. For \(\ell\ne5\), the compact procyclic closure of \(F=\begin{pmatrix}0&-5\\1&1\end{pmatrix}\) has analytic Lie dimension 1, while roots \(\alpha,\beta\) of \(t^2-t+5\) are multiplicatively independent because their principal ideals have norm 5 and are coprime (\(\alpha+\beta=1\)), making the Zariski closure dimension 2. This tests the inference rather than the existence of a motive or a rational form of the analytic line, and does not decide059's expectation.

### H09 — Effaceability is the specific unfinished Ext step

**File/scans:**12.pdf,062–063. **Kind:** self-flagged. **Quote:** “je doute”; “Ind-motifs ???”. **Search:**H09. **Context:** Hua, “Les propriétés demandées,” foliation61–62/current062–063. **Relation:** supports. **RESULTS_STATE:**WG2 §3.2 #7; MPL_15_195-228+18_002-017 S15:.

Hua identifies the gap between defining hyper-Ext using \(R\underline{\operatorname{Hom}}\) and identifying it with derived Ext in an abelian category of motives. The manuscript isolates effaceability and possible enlargement to Ind-motives; a triangulated six-operation formalism does not by itself answer this question. A modern comparison must distinguish triangulated construction, a suitable heart and compatibility of its Ext groups.

### H10 — Absolute cohomology is not automatically modern motivic cohomology

**File/scans:**12.pdf,060,063–065,067,071. **Kind:** unpursued implication. **Quote:** “Cohomologie absolue”. **Search:**H10. **Context:** Hua, “15) La cohomologie absolue : les exigences” and “Les propriétés demandées,” foliation59,61–64/current060,062–065. **Relation:** credits Hua's Weil-étale comparison. **RESULTS_STATE:**WG2 §3.2 #7; MPL_15_195-228+18_002-017 S15:.

Hua suggests a Weil-étale comparison because expected rational cohomology retains an odd class over finite fields, while warning that the requirements are not simply those of Voevodsky's motivic cohomology. This comparison is Hua's project's suggestion, not the manuscript's terminology. Test the absolute functor, finite-type realization comparison and duality together before identifying a modern construction with this programme.

### H11 — Vanishing at an algebraically closed point versus the odd table

**File/scans:**12.pdf,064–065,071. **Kind:** unproved claim / internal contradiction. **Quote:** “\(H^i(k,M)=0\)”; “pas canoniquement”. **Search:**H11. **Context:** Hua, “Les propriétés demandées,” foliation63–64/current064–065, and “Sur un corps fini…,” foliation70/current071. **Relation:** confirms Hua's tension. **RESULTS_STATE:**WG2 §3.2 #7.

Hua observes that higher absolute-cohomology vanishing on an algebraically closed point, together with Leray and pure weights, leaves no odd \(2j+1\) group of the kind displayed065 and071. The current text supports both sides and marks the odd identification noncanonical, without explicitly retracting either formula. Register an inconsistency, not an authorial withdrawal, unless an actual cancellation linking the claims is found.

### H12 — The duality shift is an actual correction

**File/scan:**12.pdf,067. **Kind:** withdrawn in the same text. **Quote:** inserted “\(\mathbf Q(n)[2n+1]\)”. **Search:**H12. **Context:** Hua, “La dualité absolue,” foliation66/current067 and foliation68/outside packet. **Relation:** supports the revised shift, bounded by omitted continuation. **RESULTS_STATE:**WG2 §3.2 #7.

The page replaces its earlier dualizing shift by \(2n+1\) and uses that value in both pairings, a visible correction independently of Hua. Hua compares this with arithmetic duality and explains an argument on the omitted continuation, but that is context rather than one of these transcribed images. Current067 ends mid-reduction and is not a completed proof of the arithmetic case.

### H13 — The odd class and extension-degree normalization

**File/scan:**12.pdf,071. **Kind:** reading question. **Quote:** “multiplier l'isom obtenu par \(n\)”. **Search:**H13. **Context:** Hua, “Sur un corps fini…,” foliation70/current071. **Relation:** different multiplier. **RESULTS_STATE:**WG2 §3.2 #7.

The frozen margin reads multiplication by \(n\), with doubt, while Hua's prose gives \(1/n\); Hua's own explanatory footnote says restriction sends the normalized Frobenius character to \(n\) times the new generator. Reciprocal factors may reflect opposite directions of the comparison map, so record both the discrepancy and the need to specify that map. Neither direction should silently replace the frozen reading.

### H14 — The \(i=1\) interval is weaker than the preceding alternatives

**File/scan:**12.pdf,073. **Kind:** unpursued implication / reading question. **Quote:** “\(-2\le\rho\le1\)”. **Search:**H14. **Context:** Hua, “Sur un corps fini…,” foliation72/current073, correction footnote. **Relation:** agrees with Hua's arithmetic check. **RESULTS_STATE:**MPL_14_002-044 B04; LM6 A.50.

Hua replaces endpoint 1 by 0 because the preceding alternatives at \(i=1\) give \(\rho=0\) or \(-2\le\rho\le-1\). The frozen endpoint 1 is therefore a weaker necessary condition, not itself a false vanishing assertion; the discrepancy concerns presentation as an exact “i.e.” reformulation. This qualification matters when using the page for weight exclusion.

### H15 — Weight of the Tate-module motive

**File/scans:**12.pdf,074–076. **Kind:** reading question. **Quote:** “pur de poids1”; “\(1-1=0\)”. **Search:**H15. **Context:** Hua, “16) Points rationnels…,” foliation73–75/current074–076. **Relation:** differs from written sign and supplies interpretation. **RESULTS_STATE:**LM7 C.1; MPL_14_002-044 M24a.

Hua changes the stated weight of \(T_{\mathrm{mot}}(A)\) from 1 to −1 using \(R^1\) of the dual abelian scheme with twist(1), and076's calculation supports that convention. The frozen coefficient twist074 remains marked \(1|0\), so specify the convention under which the sign is inconsistent instead of pretending the reading settled. This is a compatibility check, not a new proof of LM7 C.1's realization claims.

### H16 — “Bijective” is qualified by a finite kernel

**File/scans:**12.pdf,077,079. **Kind:** withdrawn in the same text / qualified claim. **Quote:** “bijective”; “surj. à noyau fini”. **Search:**H16. **Context:** Hua, “16) Points rationnels…,” foliation76,78/current077,079. **Relation:** supports weaker formulation. **RESULTS_STATE:**FERMAT_SUCCESSOR A.53; SECTIONS_OVER_Q A.186.

The arithmetic-H1 to geometric-invariants map is called bijective in the body079 but surjective with finite kernel in its margin, while077 supplies a finite left term. Hua adopts the weaker formulation, sufficient for the finiteness equivalence. This general mechanism neither verifies nor changes the special Sha claims in the register.

### H17 — Do not misquote the local \(p\)-primary qualification

**File/scan:**12.pdf,082, compared078. **Kind:** reading question / context audit. **Quote:** “essentiellement un \(p\)-groupe, modulo groupe fini”. **Search:**H17. **Context:** Hua, “Une courbe sur un corps fini,” foliation81/current082. **Relation:** differs from Hua's compressed criticism. **RESULTS_STATE:**FERMAT_SUCCESSOR A.54; FLAGGED_149 B9.

Hua flags the problematic earlier vanishings, especially against078, but its footnote compresses the final line into wording that appears to call the entire local \(p\)-group finite. The frozen line explicitly says “modulo groupe fini,” already separating the \(p\)-primary part from finite error. The unverified \(H^1(C,A)=0\) expectation and contradictory \(H^{\ge2}(C,A)=0\) assertion remain distinct problems.

### H18 — Weight parity governs positivity

**File/scans:**12.pdf,086–087. **Kind:** unpursued implication. **Quote:** “alternées si \(\rho\) impair”. **Search:**H18. **Context:** Hua, “VII.17) Formes positives,” foliation85–86/current086–087; supplied first Book II transcription44/008–009, positivity question. **Relation:** links current axioms to the older programme. **RESULTS_STATE:**WG2 §2.3 #12; WG H9; MPL_60_002-035 F21,F22.

The parity rule and tensor-sign observation supply the exact linear structure to compare with the Jacobian positivity problem. Hua links these cones to polarized tensor categories, but the manuscript does not identify arbitrary real structures with polarizations or derive real sections of fundamental groups. Cite the odd-weight obstruction already recorded in MPL_60_002-035 F21–F22, with these pages adding its axiomatic source.

### H19 — Weight zero need not mean a trivial motive

**File/scans:**12.pdf,088–089. **Kind:** own idea / hypothesis question. **Quote:** “Si \(\rho=0\), de sorte que essentiellement \(M\) est défini par un vectoriel”. **Search:**H19. **Context:** Hua, “VII.17) Formes positives,” foliation87–88/current088–089; “Le niveau d'un motif,” foliation2–3/outside packet. **Relation:** text and Hua share the scope problem. **RESULTS_STATE:**MPL_14_002-044 M01; MPL_15_195-228+18_002-017 B03. **Confidence:**high with usual Tate-twist/Hodge conventions.

Allowing Tate inverses, weight 0 includes twists of positive-weight motives; for example \(h^2(E\times E)(1)\) over \(\mathbf C\) has nonzero Hodge types \((1,-1)\) and \((-1,1)\), so is not a sum of units. The identification is appropriate for effective weight-zero/Artin motives over an algebraically closed field, or for the trivial submotive \(\Gamma M\otimes\mathbf1\) used089. Hua repeats the unqualified implication and therefore does not establish that effectiveness or level 0 was written086.

### H20 — The cone axioms can supply isotypic self-duality

**File/scans:**12.pdf,087–089. **Kind:** unpursued implication. **Quote:** “composantes isotypiques”. **Search:**H20. **Context:** Hua, “VII.17) Formes positives,” foliation88/current089, final footnote. **Relation:** refines Hua's warning. **RESULTS_STATE:**WG2 §2.3 #12; MPL_14_002-044 A36.

Hua notes that cross-terms between distinct isotypic pieces vanish once each simple factor is self-dual with the prescribed twist. The stated existence of a nonempty ample cone for each simple supplies just such a nondegenerate form, so within the axiom system this can be deduced rather than added as an unrelated assumption. Without that structure, pairings may join distinct dual simple factors and the product decomposition need not hold.

### H21 — The determinant loses the zero-eigenvalue class

**File/scans:**12.pdf,090–092. **Kind:** unproved claim / context-supported counterexample. **Quote:** “l'hom précédent est injectif”. **Search:**H21. **Context:** Hua, “Le dictionnaire algébrique,” foliation89–91/current090–092. **Relation:** confirms the omission with reading boundary. **RESULTS_STATE:**MPL_60_002-035 §2; MPL_60_036-070 §2.

Hua already gives the endomorphism-class failure: \((k,0)\) is the nonzero class of \(k[t]/(t)\) but \(L=1\) and logarithmic derivative 0. Frozen090–091 marks \(\mathbf N|\mathbf Z\) in several places, yet091's last formula and092 explicitly use \(\mathbf N\), so both category and reading must be reported. On automorphism classes the factor \(t\) is excluded, which is the Frobenius application.

### H22 — The series involution carries another sign question

**File/scan:**12.pdf,091. **Kind:** reading question. **Quote:** “\(\varphi(t)\mapsto1/\varphi(t)\)”. **Search:**H22. **Context:** Hua, “Le dictionnaire algébrique,” foliation90/current091. **Relation:** different formula. **RESULTS_STATE:**MPL_60_002-035 §2.

Hua gives \(\varphi(t)\mapsto1/\varphi(-t)\) to pass between symmetric and exterior-power conventions; the frozen insertion reads inversion without the argument change. The later product \(L=\prod_QQ^{c_P}\) also differs from the initial reciprocal-determinant convention, so the series map and product exponents must be examined together. Neither expected convention may replace the frozen formulas.

### H23 — Characteristic polynomials do not recover Jordan blocks

**File/scans:**12.pdf,092–093. **Kind:** own idea / scope qualification. **Quote:** “comme \(\mathbf N\)-modules”; “l'opération du Frobénius”. **Search:**H23. **Context:** Hua, “Ce que la fonction \(L\) sait de la cohomologie,” foliation91–92/current092–093. **Relation:** qualifies wording repeated by Hua. **RESULTS_STATE:**SECTIONS_OVER_Q D.3; MPL_60_036-070 §2. **Confidence:**high by explicit matrices.

The determinant recovers a semisimplification or \(K_0\)-class, not a general Frobenius module: \(I_2\) and \(\begin{pmatrix}1&1\\0&1\end{pmatrix}\) both give \((1-t)^{-2}\) although nonisomorphic. Purity separates cohomological degrees in a smooth proper fixed-weight situation but does not by itself remove this Jordan ambiguity. Literal recovery needs semisimplicity or interpretation at the level of classes; SECTIONS_OVER_Q D.3 concerns the further weakening from full characteristic data to partial traces.

### H24 — Parity of coefficient weight affects the virtual class

**File/scans:**12.pdf,092–093. **Kind:** unpursued implication. **Quote:** “\(\sum(-1)^i\underline h^i(F)\)”. **Search:**H24. **Context:** Hua, “Ce que la fonction \(L\) sait…,” foliation91–92/current092–093, first footnote. **Relation:** supports Hua's explicit correction only in research. **RESULTS_STATE:**MPL_60_002-035 F21,F22.

Combining \(\chi(F)=\sum_j(-1)^j[H^j]\), \(\chi(F)=\sum_i(-1)^i\underline h^i(F)\), and \(i=j+\rho\), gives \(\underline h^i(F)=(-1)^\rho[H^{i-\rho}]\). Hua supplies this omitted sign as a departure from the page, while frozen093 retains its absence. The sign changes the virtual representative but not separation of characteristic polynomials by distinct weights.

### H25 — The “N°12” link is supported despite a marginal reading question

**File/scans:**12.pdf,093–095, compared051–052. **Kind:** unpursued implication / reading question. **Quote:** “N°12”; “envisagés dans les notes sur les Motifs”. **Search:**H25. **Context:** Hua, “Ce que seule une lecture d'ensemble peut dire” and “Ce que la fonction \(L\) sait…,” foliation92–94/current093–095. **Relation:** supports reference, differs in margin. **RESULTS_STATE:**WG2 §2.4 #3; WG2 §1.1 #2.

Hua identifies “N°12” with the birational programme of foliation42–51, supported by the tail051–052 and explicit wording095. Frozen093 reads “les poids ici sont pour la bonne filtration,” whereas Hua reads a warning that weights are not the right filtration, an unresolved context-suggested wording question. The live094 margin independently requests refinement by another filtration, level or dimension, making that mathematical refinement secure.

### H26 — Relative birational reconstruction is still a programme

**File/scans:**12.pdf,093,095. **Kind:** conjecture / self-flagged. **Quote:** “Dans quelle mesure faut-il faire les hypothèses”. **Search:**H26. **Context:** Hua, “Ce que la fonction \(L\) sait…,” foliation92,94/current093,095. **Relation:** supports open status. **RESULTS_STATE:**WG2 §2.4 #3; SECTIONS_OVER_Q D.4.

The relative attempt093 is cancelled, then095 asks whether quotienting contributions over strict closed subsets of the base recovers generic-fibre birational invariants and which hypotheses are necessary. Hua says the programme is not resumed in its full reading, so it is not an established reconstruction theorem. SECTIONS_OVER_Q D.4 warns against a jump from closed-fibre linear information to a generic section, without being a counterexample to this precise \(L\)-function question.

### H27 — Title without a stated page count

**File/scan:**12.pdf,096. **Kind:** unpursued implication / documentary. **Quote:** “Poids et niveaux des espaces de cohomologie \(\ell\)-adiques (base var. quelconque)”. **Search:**H27. **Context:** Hua, “IX. Poids et niveaux…,” foliation95/current096. **Relation:** supports title. **RESULTS_STATE:**WG2 §1.1 #2,#3; MPL_15_195-228+18_002-017 §136.

Hua identifies a folder cover introducing a later typescript and working notes, matching frozen096. The cover states no page count; the later extent in Hua is reconstruction, not a count on this sheet. Hua's omission of reused typescripts061 and072 similarly describes its interpretation's scope rather than the current inventory.

### H28 — Period-conjecture evidence limit

**File/scans:**12.pdf,051–096 supplied subset, especially059,063–065. **Kind:** unpursued implication / evidence limit. **Quote:** “indépendant de \(\ell\)”. **Search:**H28. **Context:** full Hua file searched for period/transcendence language; first Book II transcription matches unrelated transcendental terminology and Bott periodicity. **Relation:** bounded negative evidence. **RESULTS_STATE:**MPL_15_087-138 T26; MPL_18_018-062 §2.

Neither these 39 pages nor Hua's full reading supplies a written assertion here that a comparison point is generic or that every polynomial period relation is motivic. Independence of \(\ell\), comparison of cohomology and a tensor-automorphism group are separate assertions. The strongest supplied lead is MPL_18_018-062 §2, pointing to18/059 and “conjecture de transcendance N°1”; that original page is outside this packet.

### H29 — Exact sequence and weight cocharacter occur in earlier context

**File/scans:**12.pdf,056–059. **Kind:** unpursued implication / evidence limit. **Quote:** “structures tensorielles”. **Search:**H29. **Context:** Hua, “Le groupe fondamental,” foliation6–9; “Le groupe fondamental profini, et le Frobenius,” foliation9–13; “Structures supplémentaires…,” foliation14–16, all outside packet. **Relation:** foundational context, later application here. **RESULTS_STATE:**WG2 §2.4 #3; MPL_15_195-228+18_002-017 §2.

Hua describes the map to \(\pi_1\) through Artin motives and distinguishes a canonical epimorphism on component groups from conjectural identification under Tate/Hodge assumptions. Its weight section gives central \(y:\mathbb G_m\to G\) and \(\varepsilon(y(\lambda))=\lambda^2\), formulas not written in the current051–096 fragment. These are contextual leads for the requested exact sequence over \(\mathbf Q\), not newly transcribed scan evidence.

### H30 — The category construction is later in Hua's dossier

**File/scans:**12.pdf,056,059,086–089. **Kind:** unpursued implication / evidence limit. **Quote:** “anneau semi-simple”; “catégorie des motifs”. **Search:**H30. **Context:** Hua, “L'enveloppe pseudo-abélienne,” foliation143–148; “L'exemple des variétés,” foliation149–151, outside packet; first Book II transcription16/018,049. **Relation:** contextual bridge, not present construction. **RESULTS_STATE:**WG2 §2.3 #7; WG2 §2.4 #3; MPL_11_043-058+56 N031; MPL_14_087-132 M01; MPL_15_087-138 L01.

Hua locates a later construction by correspondences, splitting projectors and tensor operations, explaining its homological/numerical and positivity assumptions. Here the category is assumed while semisimple correspondence algebras and positivity cones are used, strengthening the bridge from 16/049 without proving construction from the single abstract Lefschetz operator ring of16/018. Registered projector-splitting and category-starting observations remain prior leads, not new results here.

### H31 — Hua's normalized notation does not settle uncertain ink

**File/scans:**12.pdf,051,054,057–059,086. **Kind:** reading question. **Quote:** “Le thème”; \(\xi|\zeta\), \(\mathfrak g|g\). **Search:**H31. **Context:** Hua, “Les conventions, valables pour tout le dossier,” plus header revision notes for foliation50,53,56,58,85/current051,054,057,059,086. **Relation:** alternatives and declared normalizations. **RESULTS_STATE:**WG2 §1.1 #3.

Hua standardizes the Lefschetz class to \(\xi\) where its reading had \(\zeta\), and uses \(\mathfrak g_\ell\) after interpreting a Lie algebra; these choices do not settle uncertain glyphs in the frozen text. Its086 equivalent begins “La théorie,” versus frozen “Le thème,” and051 has \(\operatorname{Gr}_\alpha\) and bound \(\rho+\min(2i,2n)\) where the current readings stay marked. Record alternatives and mathematical normalizations in notes, without changes to frozen files.

### H32 — The cross-pairing Tate twist differs from the defining pairing

**File/scans:**12.pdf,086–087. **Kind:** reading question / unpursued implication. **Quote:** \(B(M',M'')=\operatorname{Hom}(M'\otimes M'',\mathbf Q(\rho))\). **Search:**H18,H19. **Context:** Hua, “VII.17) Formes positives,” foliation85–86/current086–087, first footnote. **Relation:** confirms Hua's explicit normalization as a research correction. **RESULTS_STATE:**WG2 §2.3 #12; MPL_60_002-035 F21,F22.

The defining086 pairing takes values in \(\mathbf Q(-\rho)\), while the cross-term087 takes values in \(\mathbf Q(+\rho)\); Hua replaces the latter by the former in its modern statement. With standard weights, source weight \(2\rho\) matches \(\mathbf Q(-\rho)\), whereas the displayed positive twist has weight \(-2\rho\). This explains the mismatch without altering the preserved sign.

### H33 — The last weight calculation specializes the coefficient weight

**File/scans:**12.pdf,093–094. **Kind:** unpursued implication. **Quote:** “purement de poids \(2n\)”. **Search:**H24,H25. **Context:** Hua, “Ce que la fonction \(L\) sait…,” foliation92–93/current093–094, weight-shift footnote. **Relation:** supports Hua's qualification. **RESULTS_STATE:**MPL_60_002-035 §2; MPL_14_002-044 B04.

The preceding093 threshold retains \(\rho\) in \(2n-2+\rho\), but094 writes \(2n,2n-1,2n-2\) before explicitly specializing to \(F=\mathbf Q_\ell(0)\). Hua shifts the general-coefficient values by \(\rho\) and interprets the unshifted numbers as the constant-coefficient case. The manuscript's duality expression should therefore be discussed with its coefficient weight stated, rather than silently generalised.

### H34 — The sharp twisted-coefficient upper bound needs a scope check

**File/scans:**12.pdf,051,073. **Kind:** unproved claim / context audit. **Quote:** “si \(M\) pur de poids \(\rho\)”; “\(M\) motif ct tordu”. **Search:**H01,H14; additionally full Hua reading. **Context:** Hua, “12) L'homomorphisme…,” foliation50/current051; “Motifs constants tordus, et leurs anneaux,” foliation35–40/outside packet; “Poids de la cohomologie \(\ell\)-adique d'une variété singulière ou non propre,” B), foliation107/outside packet. **Relation:** Hua's own later qualification limits its earlier summary. **RESULTS_STATE:**MPL_14_002-044 B04; LM6 A.50.

Hua describes the051 upper bound \(\rho+\min(2i,2n)\) as among established weight bounds, yet later retains only \(2n+2j\) and \(2(i+j)\) for geometric twisted coefficients and explicitly leaves improvement to \(2n+j\) and \(2i+j\) as questions. Its earlier definition identifies “constant tordu” with a lisse realization, not necessarily finite geometric monodromy, so the tight bound cannot be imported as an unrestricted consequence of WeilII. The073 interval computation is therefore conditional on its input bounds, and a finite-geometric-monodromy or genuinely constant coefficient hypothesis must be distinguished from general lisse pure coefficients.

## Self-flags and actual revisions

These are quotation locators to integrate into the primary notes' dedicated register.

| Scan | Author's signal | Status |
|---|---|---|
|052|“On peut se demander”; “injectif, ou bijectif, du moins mod torsion”|Question in wholly cancelled draft; H02.|
|055|“comment caractériser…”|Dimension-type realization question; H05.|
|057|“Question Comment caractériser l'image…”; “Cela doit être…”|Open image description and expected reductivity; H06,H08.|
|059|“On pense”; “Quelle est la partie ‘Algébrique’…”; “je pense”|Motivic descent of image and revised algebraic-part question; H07,H08.|
|060|“On veut”|Absolute-functor and limit requirements; H09,H10.|
|062|“on espère”; “On aimerait pouvoir dire”|Ext classification aspiration; H09.|
|063|“je doute”; “Ind-motifs ???”|Effaceability doubt; H09.|
|065|“on devrait”|Algebraic-closure table; H11.|
|067|Earlier shift deleted, \(2n+1\) inserted|Actual correction; H12.|
|073|Margin “? —”; cancelled question over spectral-sequence arrow|Local uncertainty, distinct from live weakened bound; H14.|
|074|“(sur \(K\) ?)”|Descent/isogeny qualification; H15.|
|075|“On s'attend”; “raisons heuristiques”; “résultat escompté”|Mordell–Weil/H1 expectation and boxed finiteness conjecture.|
|079|“conjecture”; “surjectif mod groupes finis ??”; “On devrait”|Sha/Brauer and higher-cohomology questions.|
|079|Deleted “Il y a une façon de le prouver”|Proof claim withdrawn, without supplied proof.|
|079|“bijective” plus margin “surj. à noyau fini”|Actual qualification; H16.|
|082|“sans doute”; “on doit avoir”|Expected H1 vanishing; H17.|
|084|“si \(i\ge4\) ??”; “quelle est sa taille”|Higher-cohomology vanishing and size questions.|
|095|“Il semblerait opportun”; “Dans quelle mesure…”; “??”|Relative birational reconstruction; H26.|

An inconsistency is not automatically a retraction:064 versus065/071 and078 versus082 have conflicting assertions without a cancellation connecting them. Visible shift correction067, qualification079, cancelled proof claim079, and setup changes074/090/095 are genuine revision evidence. Whole cancelled leaves052/058 and the cancelled attempt093 should be identified as abandoned drafts or formulations without claiming every sentence was mathematically repudiated.

## Priority findings

1. Preserve059's inserted scalar exception; Hua's “nulle” is not the current live reading.
2. Separate analytic \(\mathfrak g_\ell\) from Lie of a Zariski closure.
3. Credit Hua for the already noted091 kernel,064/065/071 conflict,074 weight sign,073 sharpened bound,087 pairing twist and078/082 contradiction.
4. Add091's \(\varphi(-t)\) versus \(\varphi(t)\),071's \(n\) versus \(1/n\), and093's marginal “bonne filtration” as reading questions.
5. Do not turn082's “modulo groupe fini” into total local \(p\)-group finiteness.
6. Qualify093's recovery statement for Jordan blocks.
7. Qualify088's weight-zero implication by effectiveness/level or restriction to the trivial submotive.

## Exact early-Hua evidence for the arithmetic-group question

The following locators are all outside the39 supplied scans and must be labelled contextual evidence.

| Hua heading and foliation | What Hua attributes to the manuscript | Hua's editorial qualification / current use |
|---|---|---|
|“Le groupe fondamental (pages 6 à 9)”|The Artin subcategory gives \(G\to\pi_1(S,\xi)\), and the displayed map \(\varprojlim_\alpha G_\alpha/G_\alpha^0\to\pi_1(S,\xi)\) is boxed as an isomorphism; a justification using Tate or Hodge follows.|Hua deliberately prints an epimorphism first, reserving isomorphism for the conjectural argument; source line624ff.|
|Same heading, final paragraph|A finite connected étale \(S'\to S\) gives \(G'\) as inverse image of its open \(\pi_1\)-subgroup, and component identification for all \(S\) is equivalent to connectedness over algebraically closed fields.|Neither the exact sequence over \(\mathbf Q\) nor identification of its kernel with \(G_{\mathrm{mot}}(\overline{\mathbf Q})\) is explicitly printed by Hua; the specialization is an inference.|
|“Le groupe fondamental profini, et le Frobenius (pages 9 à 13)”|\(\rho_\ell:\pi_1(S,\xi)\to G(\mathbf Q_\ell)\), \(\eta_\ell:G(\mathbf Q_\ell)\to\pi_1(S,\xi)\), with \(\eta_\ell\rho_\ell=\mathrm{id}\).|An \(\ell\)-adic-point section is not automatically a splitting of group schemes over \(\mathbf Q\).|
|“Structures supplémentaires sur le groupe de Galois motivique (pages 14 à 16)”|Central weight cocharacter \(y:\mathbb G_m\to G\); Tate character \(\varepsilon:G\to\mathbb G_m\) defined by \(\mathbf Q(-1)\), with \(\varepsilon(y(\lambda))=\lambda^2\).|This explains the normalization of the weight cocharacter, without identifying it with the centred grading of a Lefschetz \(\mathfrak{sl}_2\).|

No explicit period-genericity or period-transcendence conjecture occurs anywhere in Hua's full supplied reading; the selected packet has none either. A tensor-functor torsor in the early sections is not by itself the period conjecture.

## Current title register

| Scan | Visible heading or title | Numbering/count distinction |
|---|---|---|
|053|“Caractérisation galoisienne des filtrations”|Visible13; no page-count statement.|
|056|“Invariants de Galois et thms de commutation”|Visible14; no page-count statement.|
|060|“Cohomologie absolue”|Visible15; no page-count statement.|
|067|“th. de dualité absolue” within prose|An internal underlined label, not a separate cover or page count.|
|074|“Relations avec les pts rationnels et la cohomologie des Variétés abéliennes sur un schéma de type fini”|Visible16, with wording revised from a field to a scheme; no count.|
|084|“Calculs pour \(T_\ell(\mathbf G_m)=\mathbf Q_\ell(1)\) et \(\mathbf G_m\)”|Internal heading; no count.|
|086|“Formes positives”|Visible17; no count.|
|090|“Dictionnaire”; “Fonctions \(L\) — Cohomologie à action galoisienne”|Enclosed18; no count.|
|096|“Poids et niveaux des espaces de cohomologie \(\ell\)-adiques (base var. quelconque)”|Cover, without page count.|
