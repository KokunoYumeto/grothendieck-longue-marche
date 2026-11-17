# Research-only comparison with Michel Hua's modernised reading of cote 57

Prepared after the parent froze the complete transcription at 2026-11-17 11:46:42 UTC. No source image was opened, no transcription was delegated, and no page file or combined transcription was edited for this work. This is a working report for the parent, not the final research notes.

## Sources, reading coverage, and status

- **P57**: the frozen `MPL_57_226-270_transcription.tex`, scans 226–270 (excluding 232 and 247).
- **Hua**: Michel Hua's project, `context/hua_project/57.modern.tex`, **all 2,975 lines read**, including its own methodological preface and every section, not merely the current pages. It is explicitly an AI-produced modernised interpretation, which corrects, supplies, and omits material; its claims are not independent verification of the manuscript.
- **RS**: `context/notes/RESULTS_STATE.md`, especially orientation, open rows LM7 E.23 and LM6 E.21, planning rows, and findings-register entry **57-analytic-pic-completion-criterion**. RS says that no existing reviewed result concerns Picard schemes; the finding's status is **conjecture (unsearched)** in Hua's findings register, with intake **new to us**. That is a status of the contextual project, not the manuscript's own label.
- Both context READMEs were read before using Hua. Context page *p* corresponds to present scan *p+1*; Hua's analytic discussion ends at p.271 = scan272, beyond this package's last scan270.
- Each candidate below has an explicit context-search query. Exact matches and counts are recorded in `records/context_hua_searches.json`; the query runs use the supplied text context only. Context references below distinguish direct comparison, reported outside material, and inference.

## Main findings for the parent

1. The finite-length criterion is explicitly a **theorem with necessity and sufficiency** in scans227 and229 and again an iff in258. The contextual register's word “conjecture” must not be attributed to Grothendieck here.
2. Diagram (D) supports injectivity and, under its exactness/injectivity assumptions, identifies the cokernel with the cokernel of coherent completion. Scan256 proves the finite-length **sufficient** direction in Corollary1.6; a separate analytic-module lemma is needed to identify completeness with finite length for the converse, and the follow-up `records/analytic_module_lemma.md` now supplies a checked proof with primary references.
3. Scan256's lower bubble asserts finite-level coherent cohomology surjectivity and ends “O.K.”; this is stronger than the formal-functions statement written on250 and should be distinguished from surjectivity onto stable images.
4. Hua's current section contains material differences: eventual **kernels** instead of the current uncertain **conoyau|noyau** plus a separate unipotence hypothesis on237; **Remarque** instead of **Th.**1.7 on256; extra **normality** on268; a claimed erroneous quotient on270 where the frozen reading is already `Pic(X)/Im Z^I`; **Grauert** instead of **Cartan** in cancelled258; a sufficiency-only paraphrase of264 despite the letter's explicit iff; and a **reversal** of the global-projectivity example on262.
5. His assertion that properness is needed on248 because inverse images must be cofinal neighborhoods is too strong as an argument: closedness already gives that cofinality. Any missing paracompactness/neighborhood condition must be discussed separately.

## Candidate notes: current witness and mathematical audit

### H01 — The criterion is stated as a theorem, not asked as a conjecture

**P57 scans:** 227(iii),229(iii),256–258. **Kind:** unpursued implication. **Quote:** “it is nec and suff”; “il f. et s.” **Bears on:** Hua findings register **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `nec and suff|necessary and sufficient|longueur finie|finite length|completion-criterion`.

The letter states the analytic Picard comparison criterion with necessity and sufficiency, and the draft labels its Picard specialisation **Th.1.7**, with surjectivity iff the first coherent direct-image stalk has isolated support. Hua, modernised reading of cote57, **“La lettre”** and **“§1. Le théorème analytique”** (pp226–230,247–261), agrees on the mathematical criterion but calls1.7 a *Remarque*, while his findings register calls the criterion a conjecture. These pages change the documentary status to an authorial theorem with a proof attempt, without turning that attempt into a reviewed proof or establishing publication novelty.

### H02 — Germ Picard group is not the Picard group of the reduced fibre

**P57 scans:** 227,256–258. **Kind:** reading question. **Quote:** “Pic(X_y)”; “varinjlim…Pic(f^{-1}(U))”. **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `Pic\(X_y\)|germ|germe|varinjlim|X_n`.

The letter defines its `Pic(X_y)` as the direct limit over neighborhoods of *y*, not as the ordinary Picard group of the fibre, while `X_n=X×_Y Specan(O_y/m_y^{n+1})` denotes nilpotent thickenings. Hua, **“La lettre”**, preserves this definition, but his normalized notation can still be mistaken for an ordinary fibre if quoted without the displayed definition. The criterion concerns the map from that germ to the inverse limit of the thickening Picard groups; replacing either endpoint by `Pic(X_0)` changes the assertion.

### H03 — Exact obstruction to surjectivity in diagram (D)

**P57 scans:** 254–256. **Kind:** own idea. **Quote:** “grâce au lemme des5”; “Comme v^{i+1} est injectif”. **Confidence:** high as a conditional diagram chase; **reason:** both outer integral-cohomology terms are identical and the next coherent comparison is injective. **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `lemme des cinq|diagramme|Krull|cokernel|conoyau|completion-criterion`.

Assuming the exact rows and coherent-completion injections used in (D), put `M=(R^if_*O_X)_y`; the kernel of `H^{i+1}(X_0,Z)→M_{i+1}` is unchanged on completion, and quotienting the two rows by the common image of `H^i(X_0,Z)` gives `coker(w^i)≅M̂/M` and `ker(w^i)=0`. Hua, **“§1. Le théorème analytique”**, states the five-lemma conclusion but does not write this obstruction group. This reformulation isolates precisely the extra algebraic assertion needed for the iff, rather than treating the five lemma itself as a proof that finite length is necessary.

### H04 — The converse needs an analytic completeness lemma

**P57 scans:** 227(iii),250,256,258(iii). **Kind:** unproved claim. **Quote:** “soit artinien”; “il f. et s.” **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `artinien|isolé|longueur finie|complété|Krull|surjectif`.

Corollary1.4 and Corollary1.6 explicitly give finite length ⇒ coherent completion unchanged ⇒ Picard comparison an isomorphism, whereas the theorem also asserts the converse. Hua, **“§1. Le théorème analytique”**, passes from surjectivity of `M→M̂` to isolated support without separately proving that a finite module over a complex analytic local algebra can be complete only when it has finite length. That analytic-module assertion is implicit in the source and not proved by Krull's injectivity alone; our follow-up `records/analytic_module_lemma.md` now proves it from analytic Noether normalization and standard completion facts, while leaving the other comparison inputs separate.

### H05 — Formal existence does not supply the analytic converse

**P57 scans:** 228–229,264. **Kind:** own idea. **Quote:** “reducing to statements(i),(i bis)”; “recall…Pic(X̂)≃lim Pic(X_n)”. **Confidence:** high under the formal existence theorem invoked by the manuscript; **reason:** the constant elliptic example computes the coherent module directly. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `formal|existence|ellipti|finite length|caractéristique`.

Over the complete ring `A=C[[t]]`, the constant elliptic curve `E×Spec A` has `H^1(O)=A`, which has infinite length, while proper formal existence identifies its Picard group with the inverse limit over all thickenings. Thus finite length cannot be necessary for the analogous comparison over arbitrary complete rings; the complex **analytic** algebra hypothesis has real work to do. This agrees with scan228's restriction of the general formal analogue to(i),(i bis), and separates the claim from Hua's uses of formal existence in **“Le schéma de Picard local”** and **“§2. Application à la géométrie algébrique”**.

### H06 — “O.K.” does not prove unrestricted finite-level base change

**P57 scans:** 250,256 lower bubble. **Kind:** unproved claim. **Quote:** “est surjectif, on peut corriger, O.K.” **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `surjectif|images universelles|Mittag|formal functions|fonctions formelles|O.K.`.

The bubble claims `M→H^i(X_n,O_Xn)` is surjective, while the earlier Grauert lemma gives a completion-to-inverse-limit isomorphism and Mittag–Leffler, not unrestricted base change to every thickening. The same-finite-image conclusion only needs the appropriate coherent class in the **stable universal image**, and a proof should establish that statement using the Artin–Rees comparison/density rather than assume full finite-level surjectivity. Hua, **“§1. Le théorème analytique”**, reports equal finite images without resolving this stronger line, so the visible “O.K.” records Grothendieck's own local check, not an independent validation of it.

### H07 — Why finite generation and torsion-free quotients both matter

**P57 scans:** 252–254. **Kind:** unpursued implication. **Quote:** “de type fini”; “cf ?”. **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `type fini|sans torsion|stationnaires|Néron|Mittag`.

The stabilization argument uses subgroups of the finitely generated integral cohomology lattice whose quotients embed into complex vector spaces; these subgroups are saturated, so a chain of fixed rank cannot continue changing. Finite generation alone would not suffice, since `2^n Z` is a descending nonstationary chain, and Hua's **“§1. Le théorème analytique”** phrase about finite subgroups in a vector space should be read with the saturation condition retained. Scan254's “cf ?” leaves the topological finite-generation reference unfilled even when the lattice argument is made explicit.

### H08 — Eventual cokernel versus kernel is a substantive difference

**P57 scans:** 235–237. **Kind:** reading question. **Quote:** “conoyau|noyau”; “Si…les Ker…sont unipotents”. **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**. **Search:** `noyau|conoyau|unipotent|vectoriel|Corollaire1`.

Hua, **“Le Picard d'un schéma formel en caractéristique0”**, states that the eventual **kernel** is vectorial or almost radicial under the basic inverse-system hypotheses, whereas frozen scan237 first reads uncertain **conoyau|noyau** and then separately adds unipotence of the transition kernels to obtain vectorial kernels. This separation is mathematically necessary: the projections `G_n=E^n`, for an elliptic curve *E*, satisfy finite type, connected kernels, zero cokernels and trivial component groups, but their nontrivial kernels are abelian varieties, not vector groups. The example is our check, with high confidence from the explicit projections, and supports retaining the frozen doubt rather than importing Hua's stronger statement.

### H09 — Rational points and actual line bundles require a descent step

**P57 scans:** 239–245. **Kind:** unproved claim. **Quote:** “rigoureux?? À expliciter”; “O.K.” **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**. **Search:** `H\^2|Brauer|M_n|descente|points rationnels|Murre|Oort`.

The formal argument first obtains Mittag–Leffler for the *k*-points of Picard schemes and only then uses Čech degree2 of the unit groups `M_n` to reach the actual groups `Pic(X_n)`. Hua, **“Le Picard d'un schéma formel en caractéristique0”**, compresses this step into an exact sequence; his earlier **“La construction, quand A a un corps de représentants”** likewise stresses the Brauer obstruction between Picard-scheme points and line bundles. Scans243–245 therefore add an explicit attempted descent calculation, with a request for rigor followed by an authorial “O.K.”, rather than permission to identify the two kinds of Picard group from the start.

### H10 — Characteristic zero is the structural hinge

**P57 scans:** 228,235–241. **Kind:** unpursued implication. **Quote:** “These results break down of course in car.>0”. **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**. **Search:** `caract|unipotent|torsion|radiciel|Igusa|divisib`.

The argument uses torsion-free geometric cokernels and, for rational-point lifting, unipotent kernels; characteristic0 turns the relevant connected unipotent groups into vector groups. Hua, **“Le Picard d'un schéma formel en caractéristique0”**, agrees with that mechanism, while **“Exemples”** pp283–291 discusses positive/mixed-characteristic failures of smoothness and divisibility. Those later examples are leads about different phenomena, not a verified counterexample to each precise assertion(i),(i bis), and the broad sentence on228 should not erase that distinction.

### H11 — The projectivity argument needs one stable ample class

**P57 scans:** 228–229,245,260,264–268. **Kind:** unpursued implication. **Quote:** “l'image…soit stable i.e. universelle”; “L…ample”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `ample|projectif|universelle|Corollaire2.2|Corollaire1.8`.

The proof chooses a sufficiently deep thickening whose image in `Pic(X_0)` is stable, takes an ample line bundle there, and then lifts its special-fibre class using the common universal image. Hua, **“§2. Application à la géométrie algébrique”**, preserves this route: it does not require that arbitrarily chosen ample bundles at all depths be compatible. This explains why the projectivity corollary uses Mittag–Leffler plus equality of finite images and does not require the finite-length hypothesis for surjectivity onto the entire formal Picard group.

### H12 — Hua reverses the global-projectivity example

**P57 scan:** 262, Remarque1.10. **Kind:** reading question. **Quote:** “Il en est cependant ainsi dans le cas suivant”. **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**. **Search:** `global|factoriel|contre.exemple|discrète|éclatement|Remarque1.10`.

After warning that local projectivity does not generally imply global projectivity, the frozen text gives a sufficient case: the morphism is an isomorphism away from a discrete set whose local rings are factorial, and it claims a global blowup presentation. Hua, **“§1. Le théorème analytique”**, instead describes the same factorial/discrete blowups as a source of counterexamples to global projectivity. The current reading contradicts that direction of his interpretation; the construction itself remains compressed in the manuscript's “il est facile de construire”.

### H13 — Proper-to-closed is a real revision, not automatically an error

**P57 scan:** 248, Corollary1.2. **Kind:** reading question. **Quote:** deleted “propre”, inserted “fermée”. **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `fermée|paracompact|proper|propre|Corollaire1.2`.

Hua, **“§1. Le théorème analytique”**, restores properness and argues that compact fibres are required for inverse images of base neighborhoods to be cofinal among fibre neighborhoods. For a closed map, however, an open set *U* containing the fibre contains `f^{-1}(V)` with `V=Y−f(X−U)`, so closedness already establishes that cofinality. The separate issue is whether the paracompact-neighborhood hypotheses of Lemma1.1 hold; the correction cannot be justified merely by the cofinality sentence in Hua's footnote.

### H14 — The local Picard corollary does not initially assume normality

**P57 scans:** 268–270. **Kind:** reading question. **Quote:** “et réduit”; “singularité isolée”; “prof A≥2”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `normal|réduit|profondeur|prof|singularité isolée|Corollaire2.4`.

Hua, **“§2. Application à la géométrie algébrique”**, gives Corollary2.4 for an analytic algebra that is reduced, **normal**, and has an isolated singularity. The frozen statement adds reducedness and isolated singularity but not normality, then replaces the ring by the finite algebra of functions on the punctured spectrum to reduce to depth at least2. The added normality would narrow the manuscript's claim and obscure the function of its reduction, so it belongs only in the record of differing interpretations.

### H15 — The exceptional-divisor quotient already reads coherently

**P57 scan:** 270. **Kind:** reading question. **Quote:** “Pic(X)/Im Z^I”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `Z\^I|exception|quotient|composantes|Picard local`.

Hua, **“§2. Application à la géométrie algébrique”**, says his source reads a nonsensical `Pic(X)/I≃Z^I` and replaces it by the quotient by exceptional-divisor classes. The independent frozen transcription already reads `Pic(X)/Im Z^I`, so this package supplies a coherent alternative reading without a mathematical correction to its text. Hua's broader **“Le schéma de Picard local”** uses the same divisor-lattice quotient, but neither this agreement nor the quotient formula alone verifies all component and regularity comparisons after completion.

### H16 — Cartan, not Grauert, in the withdrawn algebraization corollary

**P57 scan:** 258, cancelled Corollary1.10. **Kind:** reading question. **Quote:** “Sém. Cartan1960/61”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `Cartan|Grauert|1960|algébris|1.10`.

Hua, **“§1. Le théorème analytique”**, says the cancelled corollary refers to Grauert1960–1961, whereas the frozen text reads Cartan1960/61. The entire corollary is cancelled, which prevents either bibliographical reading from turning its algebraization assertion into a live theorem. The named reference remains a search lead, and should not be identified with a particular published result without a separate source check.

### H17 — Sufficiency-only normalization loses the letter's iff

**P57 scans:** 229(iii),264(iii). **Kind:** reading question. **Quote:** “necessary and sufficient”; “il faut s.” **Bears on:** **57-analytic-pic-completion-criterion**. **Search:** `dès que|il faut|sufficient|longueur finie|essentiellement constant`.

Hua, **“§2. Application à la géométrie algébrique”**, paraphrases2.1(iii) as an isomorphism **as soon as** `H^1(O)` has finite length, although the earlier letter explicitly asserts necessity and sufficiency and264 has the abbreviated “il faut s.”. The uncertain expansion should remain a reading question on264 rather than a silent weakening of the package's overall assertion. Conversely, the heavily cancelled sentence on264 about essential constancy cannot be treated as an unqualified live restatement of229's remark about the universal-image system.

### H18 — The unpublished GAGA bridge is expressly acknowledged

**P57 scans:** 228,266. **Kind:** self-flagged: a step he himself marks as unverified. **Quote:** “as yet unwritten !”; “cf…via Chow's lemma”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `unwritten|GAGA|Gaga|Grauert.Remmert|Chow|Cartan`.

The letter advertises the proper GAGA bridge as unwritten and describes the intended passage from the projective case through Chow's lemma, while266 invokes it to derive the algebraic-analytic statement from1.7. Hua, **“La lettre”**, correctly retains the qualification, whereas his later statement “Il se déduit…par GAGA” compresses the same dependency. The present package supplies an authorial research dependency and an intended method, not a written proof of the full comparison theorem being invoked.

### H19 — Henselian descent is an actual conjecture with a changed endpoint

**P57 scans:** 230–231. **Kind:** conjecture. **Quote:** “I do not have any result along these lines”; “Y_1…étale with trivial residue field extension”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `hens|étale|residue|résidu|good|bon|Mumford`.

The letter explicitly moves beyond the analytic theorem to conjectures for “good” henselian rings and formulates a finite-type version in which a line bundle on the punctured completion descends after a local étale extension with unchanged residue field. Hua, **“La lettre”**, agrees and relates “good” rings to later excellent-ring language, but that modern comparison is his interpretation and does not change Grothendieck's explicit definition. This is a genuine conjectural extension, distinct from the theorem-status analytic criterion and from a claim of descent to the original nonhenselian local ring.

### H20 — Topological formal-fibre expectations remain separate from Picard

**P57 scan:** 230. **Kind:** conjecture. **Quote:** “all ‘topological’ invariants”; “I do not know…π_1”. **Bears on:** WG2 §1.1 #3; LM7 E.23 and LM6 E.21, boundary only. **Search:** `pi_1|pi_0|homotop|homolog|geometric fibers|formal fibres|section`.

Grothendieck expects analogues for fundamental groups, Weil homology and homotopy, connected to vanishing invariants of geometric formal fibres, but explicitly knows only the π0 case here. Hua, **“La lettre”**, records the expectation, and no result in these scans supplies the arithmetic section maps or fibres left open in LM7 E.23 and LM6 E.21. A Picard comparison and a connectedness argument cannot themselves be cited as a proof of those nonabelian conclusions.

### H21 — Mumford's example is a question about the route of descent

**P57 scan:** 231. **Kind:** self-flagged: a step he himself marks as unverified. **Quote:** “I…was not able to understand his construction”; “blue paper, p.16”. **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**. **Search:** `Mumford|Murre|p..16|blue paper|cône|hens`.

The letter suspects that Mumford's example produces a line bundle on the punctured completion that does not descend to the original punctured local scheme, and asks whether this conflicts with his hoped-for étale descent. Hua, **“La lettre”**, preserves the uncertainty; his later **“§2. Application…”**, at p271/scan272 outside this package, reports a possibly confused “Murre” reference to the same page. The shared page-number clue is useful for a future exact bibliographical search, but neither name nor the suspected counterexample should be settled from the contextual paraphrase alone.

## Concise, separately credited links to Hua-only topics

The following notes deliberately group related topics from the rest of the full Hua file. Their scan quotations anchor what the current package actually adds; all statements about earlier/later scans are **Hua's interpretation**, not a claim to have inspected those source images or an upgrade of any earlier run.

### H22 — Cone examples distinguish algebraic, henselian and analytic comparison

**P57 scans:** 230–231,268–270. **Kind:** unpursued implication. **Quote:** “henselian closures”; “Pic(Y')…Pic(Ỹ')”. **Bears on:** **57-analytic-pic-completion-criterion**; WG2 §1.1 #3. **Search:** `cône|cone|O_X\(n\)|Danilov|quart|d.*4|hens`.

Hua, **“Le Picard des cônes et de leurs anneaux locaux”**, especially **“Comparaison avec le complété”** (pp184–193 = scans185–194, outside the present images), links the algebraic local-cone comparison to the groups `H^1(X,O_X(n))`, reports necessity explicitly for a curve, and points to plane curves of degree at least4 as tests where ordinary algebraic completion changes Picard. These are well-targeted leads for231's concern about Mumford and for the distinction between descent to *A* and descent to its henselization, not contradictions of the analytic-algebra theorem. His attribution to Danilov is itself mediated through another author and explicitly unread in his project, so it must not be upgraded here to a verified literature equivalence in all dimensions.

### H23 — The earlier local-Picard construction adds representability questions

**P57 scans:** 239–245,268–270. **Kind:** unpursued implication. **Quote:** “On suppose l'existence”; “Pic(X)/Im Z^I”. **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**. **Search:** `local Picard|Picard local|Greenberg|Lie\(Q\)|Brauer|corps de représentants`.

Hua, **“Le schéma de Picard local”** (pp2–12 = scans3–13), treats a local representing group obtained from the inverse system of ordinary Picard schemes modulo an exceptional-divisor lattice, with issues of Brauer obstruction, coefficient fields, independence of resolution, finite-dimensional Lie algebra and a Greenberg construction in mixed characteristic. Current270 supplies the corresponding group-level quotient in a completion comparison, and239–245 explicitly separate actual line bundles from Picard-scheme points. It does not construct that representing local group, prove its independence, or settle Hua's reported mixed-characteristic/nonregular questions, so the group comparison is a useful earlier ingredient rather than the entire later theory.

### H24 — Rigidity, square/cube, Albanese, and relative Picard existence are different jobs

**P57 scans:** 233–241. **Kind:** unpursued implication. **Quote:** “On suppose l'existence…Murre”. **Bears on:** WG2 §1.1 #3; WG2 §2.4 #4; WG H1, boundary only. **Search:** `rigid|cube|carré|Albanese|Murre|descente|existence`.

Hua's earlier sections **“Carré, cube”**, **“Rigidité et schémas abéliens”**, **“Groupes rigides et descente des sous-groupes”**, **“Le schéma d'Albanese”**, **“Théorèmes d'existence relatifs”**, and **“Le foncteur de Picard”** concern construction, duality and descent of relative moduli objects; current241 instead assumes Picard representability and uses it to control an inverse system. These topics fill other chapters of his reported twelve-part **“Le plan d'un traité”** (pp64–65), and this package adds a characteristic-zero completion chapter rather than new proofs of those earlier constructions. In particular, the word “rigide” in those contexts is not the arithmetic centralizer assertion WG H1 and gives no new solution of it here.

### H25 — Connections and universal vector extensions are not the vector kernels here

**P57 scans:** 227–228,237,241. **Kind:** unpursued implication. **Quote:** “Kernel and Cokernel…vector groups”. **Bears on:** WG2 §1.1 #3; WG2 §2.4 #4. **Search:** `connexion|connection|Atiyah|extension vectorielle|Poincaré|vector groups`.

Hua, **“Fibrés à connexion et extension du dual d'une variété abélienne”** (pp79–93 = scans80–94), constructs moduli of line bundles with connection and an intended universal vector extension via dlog, Atiyah classes, and the Poincaré bundle. The vector groups on current227–241 are kernels/cokernels of nilpotent restriction maps and carry no connection datum, so similarity of vocabulary does not identify the constructions. The present scans neither supply the functoriality check Hua reports missing there nor the Fourier-kernel compatibility sought by WG2 §2.4 #4.

### H26 — Generalized Jacobians and curve moduli are outside the current proof

**P57 scans:** 228,230,260–268. **Kind:** unpursued implication. **Quote:** “if dim X_0≤1”; “π_1”. **Bears on:** LM7 E.23; LM6 E.21; WG2 §1.1 #3; generalized-Jacobian bridge B11, boundary only. **Search:** `jacobienne généralisée|generalized Jacobian|T_ell|xi_n|cocycle|courbes stables|pinç`.

Hua, **“Le Picard des schémas en courbes”** (pp140–154), describes a generalized Jacobian with toric part, an unverified identification of a cohomological obstruction with a Kummer boundary, and a dual-graph count for nodal curves; **“Contracter un sous-schéma fini”** (p303) revisits the unit quotient behind that torus. The current package's dimension≤1 projectivity corollaries are about proper infinitesimal thickenings and do not provide those generalized-Jacobian constructions or their section-class calculations. These outside leads could matter for LM7 E.23 and LM6 E.21, but neither their Kummer compatibility nor the toric finite-generation issue in B11 is settled here.

### H27 — Finiteness, specialization and separation are not one constancy assertion

**P57 scans:** 227,237–245. **Kind:** unpursued implication. **Quote:** “Néron-Sévéri groups…constant for n large”; “th. de finitude de Néron”. **Bears on:** WG2 §1.1 #3; **57-analytic-pic-completion-criterion**; RS returned-package **MPL_57_271-315 E08** as a lead. **Search:** `Matsusaka|Kleiman|Igusa|Néron|Néron.Severi|séparation|torsion|spécialisation`.

Hua's **“Le théorème de finitude”**, **“Structure locale…les constituants de la torsion”**, **“Composante neutre…”**, **“Deux exemples…”**, **“Schémas de Néron–Severi et polarisations”**, and **“Questions ouvertes”** distinguish boundedness, representability, separation, smoothness, and specialization of Picard/Néron–Severi objects. Current227 and237 assert eventual component stability along thickenings of one fixed fibre in characteristic0, which neither proves rank constancy across changing fibres nor contradicts the later positive-characteristic divisibility examples. The same-cote E08 lead in RS concerns that separate continuity question and must not be conflated with the inverse-system theorem.

### H28 — Divisors, depth and pinching give methods, not omitted proofs in this package

**P57 scans:** 268–270; reused n°227 at263,265,267,269. **Kind:** unpursued implication. **Quote:** “prof A≥2”; “Systèmes linéaires”. **Bears on:** WG2 §1.1 #3; WG2 §2.4 #4; WG2 §2.3 #12. **Search:** `profondeur|Seshadri|pseudo.morph|diviseur|recollement|Chevalley|systèmes linéaires`.

Hua's **“Picard et profondeur”**, **“Le théorème de Seshadri”**, **“Séparation: unités et diviseurs…”**, **“Plongements projectifs…”**, **“Pseudo-morphismes et diviseurs”**, **“Notes, et contre-exemples pour le recollement”**, and **“Picard et Albanese des variétés non complètes: Chevalley”** offer depth, divisor, and gluing methods that illuminate the terse extension and quotient steps on268–270. The present reused linear-systems pages are additional documentary content that Hua expressly omits, and their numbering is not evidence for cote44's higher-cycle Theorems1–7. No proof omitted in those outside sections is supplied merely by the recurrence of the same method words here.

## Bounded proof ledger for the analytic criterion

| Link | Current documentary evidence | What this report can safely say |
|---|---|---|
| Coherent formal functions |250, Lemma1.3 |Named Grauert result is invoked; not reproved here.|
| Finite integral cohomology |254, “cf ?” |Used in the lattice argument; citation missing on page.|
| Stabilization of lattice kernels |252–254 |Saturated subgroups of bounded rank explain the algebraic step; finite generation alone does not.|
| Exact inverse-limit exponential row |252–254, Proposition1.5 |Attempt uses ML for images; must keep its hypotheses.|
| Injectivity of Picard comparison |256(D), item(a) |Conditional diagram chase valid if the rows and coherent injections hold.|
| Cokernel = coherent completion cokernel |256(D) |Our transparent reformulation of the same diagram, not a new archive statement.|
| Finite length ⇒ isomorphism |250 Cor1.4;256 Cor1.6 |Explicit sufficient direction; exactness provides the implication.|
| Isomorphism ⇒ finite length |227,229,258 assert iff |Analytic-module lemma is implicit in the manuscript; subsequently proved with primary inputs in `records/analytic_module_lemma.md`.|
| Equality of finite images |227(ii),256(a)/bubble,258(ii) |Authorial assertion; the bubble's full finite-level coherent surjectivity is stronger than needed and not justified by formal functions alone.|
| Proper algebraic-analytic comparison |228,266 |GAGA dependence explicitly “as yet unwritten!” in the letter.|
| Punctured-spectrum injectivity |268–270 |Depth reduction provided; “Un raisonnement facile” leaves argument terse.|
| Punctured-spectrum surjectivity |270 |Resolution, regular formal fibres, quotient lattice and2.1(iii) form proof route; no independent complete verification claimed.|

## Reading questions suggested by context — no text changes

| Current location | Frozen reading | Hua's different version | Consequence |
|---|---|---|---|
|227(i)|Artin-Riesz|Artin–Rees|Modern normalization must stay out of transcription.|
|237(iii)|conoyau\|noyau; separate unipotent-kernel addition|eventual kernel vectorial/radicial|Substantive theorem distinction; E^n projections refute unqualified kernel claim.|
|248 Cor1.2|proper deleted, closed inserted|proper restored|Cofinality argument in Hua does not justify the restoration.|
|256–258|Th.1.7|Remarque1.7|Authorial theorem status matters.|
|258 cancelled1.10|Cartan1960/61|Grauert1960–1961|Bibliographical lead differs; entire passage remains cancelled.|
|262 Rem1.10|sufficient global-projectivity case|suggested global counterexamples|Direction of interpretation is reversed.|
|264(iii)|“il faut s.”; letter229 explicitly iff|“dès que”|Do not flatten package-wide necessity claim to sufficiency.|
|268 Cor2.4|reduced + isolated singularity|reduced + normal + isolated singularity|Added normality hides the depth reduction.|
|270|Pic(X)/Im Z^I|reported Pic(X)/I≃Z^I then corrected|Current independent reading already gives meaningful quotient.|

The transcription remains frozen throughout; all these comparisons belong only to research notes.

## Supplementary proof route sent to the parent

The following **our own proof route** was initially proposed for the converse in H04. It has subsequently been checked in full, including the nonreduced case and exact primary references, in `records/analytic_module_lemma.md`; the sketch is retained here to document the sequence of the research.

Let `A` be a complex analytic local algebra and `M` a finite `A`-module with `M→M̂` surjective (hence an isomorphism, by separatedness). Finite submodules and quotients of `M` are complete: Artin–Rees compares the induced topology on a submodule, and Krull separatedness of the quotient makes the submodule closed. A prime filtration therefore makes every factor `A/p` complete; if `M` has positive-dimensional support, one factor `R=A/p` is a positive-dimensional analytic local domain. Analytic Noether normalization makes `R` finite over `B=C{t_1,…,t_d}`, `d>0`, and the maximal-ideal topology of `R` is equivalent to the `m_B R` topology. Since `B` is normal and characteristic zero, the normalized fraction-field trace is a `B`-linear retraction `R→B`; thus `B` is a direct summand of the complete finite `B`-module `R` and is complete. This contradicts, for example, the existence of the divergent series `sum n! t_1^n` in `B̂=C[[t_1,…,t_d]]` outside `B`. Hence support has dimension zero and `M` has finite length.

This argument would close the **analytic-module** part of the necessity direction, conditional on the named standard inputs; it does not fix the separate finite-level-surjectivity line in the scan256 bubble, nor supply the manuscript's unwritten GAGA comparison.
