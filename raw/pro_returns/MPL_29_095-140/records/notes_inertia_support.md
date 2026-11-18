# Research-notes support: inertia, Kummer classes, monodromy and Pi₂

Prepared by `/root/notes_inertia` after the transcription freeze of 2026-11-18 06:04:22 UTC. This is ancillary support for the root agent, not the research-notes deliverable. No source image or crop was opened, and no frozen transcription was changed. The evidence called “manuscript” below is the frozen page file in `MPL_29_095-140_work/pages/`; all other manuscript continuations are explicitly attributed to the supplied modernised context.

## Scope and source discipline

Read both context READMEs and all of `context/notes/RESULTS_STATE.md`. Read the relevant full subsections of `context/hua_project/29.modern.tex`, including its editorial header, the formal-inertia discussion (Hua pp.87–100), Kummer corollary and monodromy/Pi₂ (pp.102–104), inertia functoriality (pp.116–122), Pi₂ against covering towers (pp.175–176), the pro-representability comparison (pp.181–185), and later Kummer examples (pp.199–200). Global searches of the modernised file were used to find recurring objects and words, as recorded below.

Pagination: **Hua page n corresponds to archive scan n+1.** Thus Hua p.95 is our scan096, p.97 is scan098, p.103 is scan104, p.104 is scan105, p.116 is scan117, and p.120 is scan121. In particular, scan121 is **not supplied in the current image package**. No finding on it is confirmed against ink here.

`RESULTS_STATE` gives the external findings as claims to check, not established results, and its own register statuses are earlier runs' claims unless explicitly refereed. Relevant IDs are **Hua, findings register, `29-formal-tame-pi1-self-intersection`**, **Hua, findings register, `29-inertia-matrix-determinant`**, and, much more narrowly, **LM1 E.2** and **LM1 E.11**. The latter two are not settled or strengthened by the scalar finite-dimensional lemma on scan104. The broad GT, sections, finite-category and localizer register summaries provide no direct statement-level match to these eight frozen pages; none is forced into the notes merely by a shared word such as “inertia” or “homotopy”.

## Candidate research items and exact context map

Labels A–O below are temporary support labels. Root should assign the final note IDs. Each **suggested item** is at most four sentences; metadata and search evidence are outside the suggested item.

### A. The formal inertia extension is controlled by a class, but the quotient and action need to be retained

- **Frozen witness:** scan096, author p.5, displayed sequence and sentence with “[self-intersection de X₀ dans 𝓧]”; “entièrement” remains marked uncertain in the frozen text.
- **Kind:** unproved assertion on this leaf / contextual connection; not a new conjecture as a whole.
- **Exact context:** Hua, modernised reading of cote29, **“Le théorème, et deux exemples (pages 95 et 97)” → “L’énoncé”** (Hua p.95 = scan096; lines2438–2461); antecedents **“Le π₁ modéré d’un schéma formel le long de sa fibre spéciale (pages 87 et 89)” → “La suite exacte”, “Lemme 1 : le revêtement universel modéré n’a pas de H¹”, and “Lemme 2 : la classe est celle de l’auto-intersection”** (Hua pp.87,89 = scans088,090, outside supplied evidence; lines2277–2383).
- **Relation:** frozen page **supports/restates** the extension–self-intersection connection in external finding `29-formal-tame-pi1-self-intersection`; earlier context **adds** a proposed Hochschild–Serre/Hurewicz mechanism and an explicit warning about passing from μ to its inertia quotient. It does not license calling the complete proof present on scan096.
- **Suggested item:** **Unproved assertion / connection.** At scan096, “[self-intersection de X₀ dans 𝓧]” accompanies the claim that the tame fundamental-group extension is determined by the base and a degree-two class, with a preceding map from Π₂ᵗ to μᵗ∞. This supports **Hua, findings register, `29-formal-tame-pi1-self-intersection`**, and Hua’s modernised reading, “L’énoncé” (p.95), while “Lemme 2 : la classe est celle de l’auto-intersection” (p.89, outside the supplied scans) adds the proposed construction of the inertia quotient. A careful formulation must retain that quotient and its base-group action; this leaf does not prove a general central or split extension theorem.

### B. Arithmetic centrality is an overstatement in the context

- **Frozen witnesses:** scan096's extension sequence, scan098's arithmetic bases, and the cancelled scan104 relation `fgf^{-1}=g^q`. None of these witnesses asserts unrestricted centrality.
- **Kind:** own targeted counterexample to a contextual assertion.
- **Exact context:** **“La suite exacte”**, Hua p.87 = scan088 (outside package), lines2306–2311: “L’extension est centrale”; repeated in `RESULTS_STATE` finding `29-formal-tame-pi1-self-intersection`. Compare **“La relation, et d’où elle vient”**, Hua p.103 = scan104, lines2679–2694; **“L’énoncé le plus précis”**, Hua pp.121–122 = scans122–123, lines3148–3167, expressly requires triviality of the Tate sheaf to remove path dependence.
- **Relation:** our direct algebraic example **contradicts** the context’s unrestricted adjective “central”, not the wording of scan096. The later context **adds/supports** the needed attention to cyclotomic twisting. A chosen basis of a Tate module does not make a nontrivial Galois action trivial.
- **Suggested item:** **Own check of context.** The arithmetic examples of scan098 and `fgf^{-1}=g^q` on cancelled scan104 require caution with the adjective “central” in **Hua, findings register, `29-formal-tame-pi1-self-intersection`**, and Hua’s “La suite exacte” (p.87). For the formal disc over F₂, the tame extension F₄((u))/F₂((t)), `u³=t`, has inertia C₃ conjugated by Frobenius through inversion, so that inertia is not central. This refutes that unrestricted contextual formulation; the extension must retain its cyclotomic action, or centrality must be restricted to circumstances in which the action on the relevant inertia quotient is trivial.
- **Check:** genuine targeted check, detailed as C1 below; suggested CHECK_EVENTS type **`refuted, with the refined statement's id`**, referring to the refined twisted formulation, not to the frozen manuscript assertion.

### C. “Extension triviale” does not follow from Π₂=0

- **Frozen witness:** scan096, Example I, first case: “extension triviale”; Π₂ᵗ is asserted zero outside the P¹/no-boundary case.
- **Kind:** unproved claim / own logical diagnostic. “Triviale” is literal; interpreting it as “split/direct product” is the mathematical reading being questioned, not a replacement transcription.
- **Exact context:** **“Exemple I : une courbe sur un corps algébriquement clos”**, Hua p.95 = scan096, lines2463–2477. Context repeats “triviale” and adds “La monodromie et le groupe fondamental de la fibre se séparent, et il n’y a rien à calculer.” Compare **“Lemme 2 : la classe est celle de l’auto-intersection”**, pp.89/scan090, and **“Le programme kummérien : la classe, une deuxième fois”**, p.100/scan101.
- **Relation:** Hua **restates** the literal claim and **adds** an unwarrantedly confident splitting gloss. The logical diagnostic **differs** from that gloss: vanishing Π₂ eliminates a left-hand obstruction but does not itself kill the degree-two extension class. It is not a geometric counterexample to every possible hidden hypothesis from the preceding leaves.
- **Suggested item:** **Unproved claim / own diagnostic.** Scan096 calls the extension “triviale” when the punctured curve is not P¹, and Hua’s “Exemple I” (p.95) repeats this as a separation of fibre and monodromy. If “triviale” means split, the stated vanishing of Π₂ is insufficient: a base with Π₂=0 can carry a nonzero central-extension class, as the Heisenberg extension of Z² shows. The useful next check is the Chern class of the normal bundle—especially its degree for a proper positive-genus curve—rather than an inference from Π₂ alone; the current package does not establish a general splitting.
- **Check:** C2 below; **`targeted proof check`**. Do not advertise a verified geometric counterexample without checking the original hypotheses and the comparison with the formal cover category.
- **Additional reading detail:** the final base-group formula on scan096 has `X₀−D₀`, without the prime used in the setup `D′₀`; Hua’s p.95 repeats that unprimed form. This agreement is not a reason to normalise the frozen notation, and the intended boundary should be clarified in any reconstructed theorem.

### D. The P¹ computation needs a degree-zero convention

- **Frozen witnesses:** scan096's Π₂ map and scan098, Example I.2: “partie première à p … du degré de la self-intersection”.
- **Kind:** missing edge case / own conditional calculation.
- **Exact context:** **“Exemple I : une courbe sur un corps algébriquement clos”**, Hua pp.95,97 = scans096,098, lines2478–2491. Hua repeats μₙ and then illustrates negative self-intersection `−d`, without specifying degree zero.
- **Relation:** **restates** the nonzero-degree formula; our observation **adds** the zero-degree boundary and explicitly conditions the calculation on the displayed exact sequence and the asserted multiplication map. Related state ID: `29-formal-tame-pi1-self-intersection`.
- **Suggested item:** **Unpursued edge case.** In the P¹ case scan098 identifies the group with μₙ, where n is the prime-to-p part of the self-intersection degree, as repeated by Hua’s “Exemple I” (pp.95,97). Conditional on scan096’s exact sequence and multiplication-by-degree map, degree zero gives the full tame Tate group as cokernel, while nonzero degree gives a finite cyclic quotient of order the prime-to-p part of its absolute value. The formula therefore needs either a degree-zero convention or an explicit nonzero-degree hypothesis; the leaf supplies neither.
- **Check:** C3 below; **`computation or formal certificate`** (elementary computation, no machine certificate).

### E. The arithmetic Π₂ question remains an explicit question

- **Frozen witness:** scan098, Example II.b: “Mais qu’est Π₂ᵗ(X₀/D′₀)” followed by “???”; `X₀=Spec Z−S`, `S≠∅`.
- **Kind:** self-flagged question.
- **Exact context:** **“Exemple II : les entiers”**, Hua p.97 = scan098, lines2493–2531; **“π₂”**, Hua p.104 = scan105, lines2731–2753; **“π₂ contre la tour des revêtements (pages 175 et 176)” → “Le calcul”**, pp.175–176 = scans176–177, outside supplied images, lines4388–4436.
- **Relation:** Hua **restates** the question without answering it; later context **adds** a covering-tower/Hochschild–Serre route, not a calculation for the arithmetic base in scan098. The present `RESULTS_STATE` has no matching solved entry.
- **Suggested item:** **Self-flagged question.** Scan098 ends its calculation of the allowed tame roots of unity on `Spec Z−S` with “Mais qu’est Π₂ᵗ(X₀/D′₀) ???”. Hua’s “Exemple II : les entiers” (p.97) restates this open question, and his later “Le calcul” under “π₂ contre la tour des revêtements” (pp.175–176, outside the supplied scans) adds a possible approach through cohomology of covering towers. Neither context nor the cited results register supplies this arithmetic Π₂ calculation.

### F. Arithmetic finiteness/nonabelianity must remain a reading question

- **Frozen witness:** scan098, Example II.a: “sans doute” and the marked-uncertain negative clause `n’est … en général pas … abélien fini`, followed by tame nonabelian number fields and “??”.
- **Kind:** reading question / self-flagged arithmetic speculation.
- **Exact context:** **“Exemple II : les entiers”**, Hua p.97 = scan098, lines2510–2519, says “le groupe entier doit être fini par dévissage”.
- **Relation:** context **differs** from the frozen uncertain wording. It cannot be upgraded to a definite contradiction in the author's intended assertion without the reading being resolved, and it cannot be used to repair the frozen transcription. No relevant settled result in `RESULTS_STATE`.
- **Suggested item:** **Reading question / self-flagged claim.** On scan098 the “sans doute” passage and its uncertain negative wording concern the whole tame group after the abelianization has been displayed, and end with question marks about nonabelian tame number fields. Hua’s “Exemple II” (p.97) instead paraphrases a finite-group claim “par dévissage”; this differs from the frozen reading and supplies no proof on the supplied leaf. Preserve the arithmetic assertion as unresolved in wording and scope rather than treating the computed abelianization as a finiteness proof for the full group.

### G. Semi-global Abhyankar: local commutation proof stops

- **Frozen witness:** scan100, “Version semiglobale … Abhyankar”, b) “Il faut prouver …” and c) “Commutation des Iᵢ: … Étude locale en un pt de”, where the text stops.
- **Kind:** unproved claim / visibly incomplete proof. The preceding pro-ℓ representation fragment is cancelled, separate from the surviving semiglobal programme.
- **Exact context:** **“Abhyankar semi-global, et la même classe une deuxième fois (pages 99 et 100)” → “Une version semi-globale du résultat d’Abhyankar”**, Hua p.99 = scan100, lines2533–2572.
- **Relation:** Hua **restates** the three conclusions but **adds** that the calculation is classical and identifies it with logarithmic inertia; those comments do not complete the proof on scan100. The frozen page **adds/retains** the revised henselian-pair hypothesis, globally invertible primes, and the visible change “produit” → “groupe engendré”, details smoothed in context. Related to the mechanism of `29-formal-tame-pi1-self-intersection`, but not a proof of its global classification.
- **Suggested item:** **Unfinished proof.** Scan100 reduces the proposed semiglobal Abhyankar statement to residual-characteristic control and “Commutation des Iᵢ”, but the final local argument stops at “en un pt de”. Hua’s “Une version semi-globale du résultat d’Abhyankar” (p.99) restates the result and calls the local computation classical, which is an addition to this leaf rather than a written completion. Any reconstruction should use the revised henselian-pair hypothesis and primes invertible along the relevant divisor, and should distinguish pairwise commutation of the inertia factors from centrality under the full fundamental group.

### H. Kummer–Chern equality is explicitly a programme

- **Frozen witness:** scan101, “On veut prouver que … ξᵢ=c(Oₓ(Dᵢ)) (mod nᵢ)”. The Γ-twisted coefficient identification is part of the setup, with cancellations.
- **Kind:** unproved claim, explicitly announced as a proof target.
- **Exact context:** **“Le programme kummérien : la classe, une deuxième fois”**, Hua p.100 = scan101, lines2574–2623; earlier **“Lemme 2 : la classe est celle de l’auto-intersection”**, p.89 = scan090; later **“Les exemples kummériens, et la classe une quatrième fois (pages 199 et 200)” → “Exemple 2 : des diviseurs, et la gerbe”**, Hua p.200 = scan201, outside package, lines5177–5215.
- **Relation:** Hua **restates** the target and **adds** the link to the four occurrences of the same obstruction class, including the later gerbe interpretation. This supports `29-formal-tame-pi1-self-intersection` at the level of a shared programme, not as a completed proof on scan101.
- **Suggested item:** **Explicit proof target.** “On veut prouver” on scan101 identifies the pulled-back group-extension class with the tuple of Kummer Chern classes `c(Oₓ(Dᵢ)) mod nᵢ`. Hua’s “Le programme kummérien” (p.100) restates this and adds a connection to the formal self-intersection lemma (p.89) and to the later divisor gerbe (p.200, both outside the supplied evidence), linking the leaf to **Hua, findings register, `29-formal-tame-pi1-self-intersection`**. The useful research step is a cocycle comparison with the specified twisted coefficient sheaf; this page announces, but does not carry out, that comparison.

### I. Extension to formal schemes or ringed topoi is not developed here

- **Frozen witness:** scan101, final circled 2: “Variantes schémas formels (ou topos loc. annelés généraux)”.
- **Kind:** unpursued extension.
- **Exact context:** **“Le programme kummérien : la classe, une deuxième fois”**, Hua p.100 = scan101, lines2620–2623; earlier formal version pp.87–97, and later divisor-gerbe pp.199–200.
- **Relation:** Hua **restates** the closing direction and **adds** the earlier/later parallels, without supplying a general ringed-topos theorem. `29-formal-tame-pi1-self-intersection` concerns the formal-scheme specialisation only.
- **Suggested item:** **Unpursued extension.** Scan101’s “Variantes schémas formels (ou topos loc. annelés généraux)” proposes carrying the Kummer–Chern identification beyond schemes. Hua’s “Le programme kummérien” (p.100) repeats the direction and connects it to the formal calculation and later gerbe language, but supplies no theorem for arbitrary locally ringed topoi. A formulation would have to specify the topology, the exactness of the chosen Kummer sequence, and the descent data for the root objects before importing the cohomological identity.

### J. The corollary’s inertia coefficient identification needs its own hypotheses

- **Frozen witness:** scan103, “Corollaire”, the deleted phrase “et commutent deux à deux”, the deleted product-isomorphism assertion, the surviving twisted inertia sheaf and Chern/normal-bundle conclusion.
- **Kind:** unproved assertion / hypothesis question prompted by cancellations. Do not infer that cancellation proves the deleted statement false.
- **Exact context:** **“Le théorème kummérien, troisième énoncé”**, Hua p.102 = scan103, lines2646–2675. Hua says the frozen material is hard to read, states an extension with coefficient I and a product-of-μ identification, and records the targeted normal-bundle class.
- **Relation:** Hua **restates** the overall conclusion but **smooths/differs** from the cancellations and remaining uncertainty about the inertia coefficient. The context's normal-bundle interpretation agrees with the last line; it does not justify restoring a cancelled product decomposition. Related ID: `29-formal-tame-pi1-self-intersection`.
- **Suggested item:** **Hypothesis question.** Scan103’s “Corollaire” deletes the separate pairwise-commutation clause and a product description of inertia before asserting the class of the normal bundle. Hua’s “Le théorème kummérien, troisième énoncé” (p.102) restates the intended Kummer identification, but the cancelled text should not be silently restored: invariant cyclic subgroups alone need not commute, as the two order-four subgroups of Q₈ show. The remaining task is to identify the geometric hypothesis or argument that makes the surviving inertia coefficient abelian and identifies its twist with the displayed roots-of-unity sheaf; the page does not write it out.
- **Check:** C4 below; **`targeted proof check`**. This diagnoses the insufficiency of a bare group-theoretic inference, not a geometric counterexample to the intended corollary.

### K. Cancelled quasi-unipotence lemma: the elementary ending is valid, but context changes the stated reading

- **Frozen witness:** whole scan104 is inside `\deleted{…}`; “deux automorphismes”, lemma6.5, and proof ending at existence of exponents N′,N″.
- **Kind:** cancelled draft / incomplete written proof / independent elementary completion.
- **Exact context:** **“Le théorème de monodromie locale (pages 103 et 104)” → “Le lemme”**, Hua p.103 = scan104, lines2696–2729; editorial header lines38–44. Hua’s footnote says the source reads “deux endomorphismes” and supplies invertibility, contrary to the frozen reading. Hua adds an SGA7 attribution and interpretation of the cancellation; neither is independently checked here.
- **Relation:** context **restates** the mathematical automorphism lemma and **adds** its ending; **differs** on the underlying word and on its explanation of cancellation. **LM1 E.2** remains background only: no new exp/log theorem is obtained. **LM1 E.11** remains open in the register.
- **Suggested item:** **Cancelled draft / checked elementary claim.** On scan104, “deux automorphismes” and `FGF⁻¹=G^q` lead to quasi-unipotence, but the cancelled proof stops after choosing repeated powers of an eigenvalue. An independent check completes the argument: the finite nonzero spectrum is permuted by q-th powering, so every eigenvalue is a root of unity and a common power of G is unipotent. Hua’s “Le lemme” (p.103) supplies this ending but says the source had “endomorphismes”, a reading discrepancy with the frozen text; its account of why the page was cancelled is not established by these scans. This does not add to **LM1 E.2** or close **LM1 E.11**, which concern group schemes over rings rather than this finite-dimensional field calculation.
- **Check:** C5 below; **`independent re-proof`**. Do not count reading Hua’s supplied proof as the check; the argument below is the independently written proof and its assumptions.

### L. H² defines a pro-Pi₂ only after the coefficient and universal-cover conventions are fixed

- **Frozen witness:** scan105: “exact à g., donc proreprésentable” and the universal-pointed-cover definition.
- **Kind:** compressed construction / unpursued comparison, not a claimed false inference.
- **Exact context:** **“π₂”** under “Le théorème de monodromie locale”, Hua p.104 = scan105, lines2731–2753; **“Lemme 1 : le revêtement universel modéré n’a pas de H¹”**, Hua p.89 = scan090, lines2313–2343; **“π₂ contre la tour des revêtements (pages 175 et 176)” → “Le calcul”**, Hua pp.175–176 = scans176–177, lines4393–4436; compare **“Quand un foncteur est pro-représentable”**, Hua pp.181–185 = scans182–186, lines4576–4611, concerning a different set-valued functor/strictness setup.
- **Relation:** Hua **restates** pro-representability and **adds** an identification with étale homotopy and later covering-tower context, but writes “exact” where the frozen source says “exact à g.”. The latter distinction should be retained. No RESULTS_STATE row settles this exact construction; finite-model results elsewhere in the register address another problem.
- **Suggested item:** **Compressed construction.** Scan105 defines Π₂ from `M↦H²(X,M)` and explicitly says “exact à g.” for a simply connected X before passing to the universal pointed cover in general. For finite abelian constant coefficients, the long exact cohomology sequence explains that left exactness once H¹ vanishes, but the leaf does not specify the site, the treatment of the pro-cover, or the comparison with a higher homotopy construction. Hua’s “π₂” (p.104) restates the definition and calls it étale homotopy, while “Le calcul” on pp.175–176 (outside this package) adds a covering-tower framework; these are useful comparisons, not a proof of those omitted identifications on scan105.
- **Check:** C6 below; **`targeted proof check`** of left exactness only. No re-proof of pro-representability or Artin–Mazur comparison is claimed.

### M. Functorial inertia begins with dependence on a prolongation

- **Frozen witness:** scan117, title “Comportement fonctoriel des groupes d’inertie”, definition by stabilizers, and “en toute rigueur … dépend du choix du prolongement”; normalisation convention under normality.
- **Kind:** self-flagged dependence / unpursued functorial step on the supplied leaf.
- **Exact context:** **“Comportement fonctoriel des groupes d’inertie (pages 116 à 120)” → “1. Ce qu’est un groupe d’inertie, et de quoi il dépend”**, Hua p.116 = scan117, lines2962–2990; **“2. Fonctorialité”**, same larger section pp.116–120, lines2992–3017 (subsection is not individually page-tagged in this file); **“3. Le calcul local”**, lines3019–3041.
- **Relation:** context **restates** the dependence and normalisation convention, then **adds** the equivariant-prolongation inclusion and local branch calculation from continuation pages not proved on scan117. Related ID `29-inertia-matrix-determinant` is downstream, not a claim appearing on this supplied leaf.
- **Suggested item:** **Self-flagged dependence.** Scan117 insists that the inertia conjugacy class “dépend du choix du prolongement”, with normalisation chosen under the stated normality hypothesis. Hua’s “1. Ce qu’est un groupe d’inertie, et de quoi il dépend” (p.116) restates this, and “2. Fonctorialité” adds the inclusion of stabilizers once an equivariant prolongation exists. Thus the research issue is to track that prolongation and its existence through a morphism, not to treat a boundary point alone as determining canonical inertia; scan117 itself does not yet prove the later functorial claims.

### N. The determinant finding is a context-only continuation, not a verified manuscript result here

- **Frozen connection:** scan117 develops the inertia setup and dependence warning; there is no supplied scan121.
- **Kind:** external finding to check / unverified geometric implication.
- **Exact context:** **“4. La matrice des multiplicités”** under “Comportement fonctoriel…”, Hua p.120 = archive scan121, lines3043–3108. The footnote reports a Lean check of the algebraic determinant equivalence and expressly excludes the geometric identification with N and conjugacy conclusion; no Lean file is supplied or run here. **“L’énoncé le plus précis”**, Hua pp.121–122 = scans122–123, adds path/Tate-sheaf qualification and reports marginal “Remords au nᵒ3,4” (context only in this support assignment).
- **Relation:** context **adds** the matrix statement to the supplied page117 setup; the package cannot confirm its original wording, hypotheses, corrections or proof on scan121. `RESULTS_STATE` credits this to **Hua, findings register, `29-inertia-matrix-determinant`** and says “new to us”; it is not an established novelty result. The modernised file calls it probably known and says the cited literature search did not find the explicit determinant/conjugacy formulation.
- **Suggested item:** **External finding not verified against supplied images.** **Hua, findings register, `29-inertia-matrix-determinant`**, concerns Hua p.120, hence archive scan121, which is absent from this package; scan117 supplies only the opening inertia definitions. Hua’s “4. La matrice des multiplicités” says that pullback multiplicities give N and that, for equal branch counts, invertibility is equivalent to `det N=±pʳ` (p the characteristic exponent, p=1 in characteristic zero), but attributes only the matrix-algebra equivalence to its Lean check. The geometric identification of the inertia map, the conjugacy consequence, and the source’s exact hypotheses remain unverified here, and the lack of a reference in that project is not evidence of novelty.

### O. The cancelled pro-ℓ image fragment is not part of the surviving Abhyankar proof

- **Frozen witness:** scan100, cancelled opening before the horizontal separator: “un s-groupe d’indice fini … qui opère sur E via un pro-ℓ-groupe”, followed by “À fortiori” and a cancelled inertia square.
- **Kind:** cancelled assertion, with its surrounding hypotheses absent from this fragment. Cancellation does not establish that the assertion is false.
- **Exact context:** **“Une version semi-globale du résultat d’Abhyankar”**, Hua p.99 = scan100, lines2538–2572, starts with the surviving semiglobal argument and does not reproduce this fragment; related **“Le lemme”** at Hua p.103 = scan104 treats a linear quasi-unipotence conclusion, not the topological pro-ℓ-image assertion. Global searches for `pro-`, `indice fini`, `opère sur … E`, and `ell`-adic terms found no explicit treatment of this cancelled statement in the modernised file.
- **Relation:** the frozen source **adds** a cancelled representation-theoretic lead omitted by Hua's account. No `RESULTS_STATE` entry settles the fragment with its unspecified representation hypotheses; LM1 E.2 is not an answer.
- **Suggested item:** **Cancelled assertion.** Before the surviving Abhyankar paragraph, scan100 cancels the claim that a finite-index subgroup acts on E through a pro-ℓ group, followed by “À fortiori” and an inertia square. Hua’s “Une version semi-globale du résultat d’Abhyankar” (p.99) omits this fragment; his later “Le lemme” (p.103) concerns quasi-unipotence but supplies no missing topology or coefficient hypotheses for it. This is a possible representation-theoretic link to the monodromy draft, with no completed inference or reason for cancellation preserved here.
- **Check status:** no mathematical verification attempted; this is reading and source mapping only.

## Actual mathematical checks (distinct from contextual reading)

These checks were performed in this support task. They are short, elementary checks with restricted conclusions; none completes the omitted global formal-geometric or Kummer–Chern proof. Root should give each final statement/refinement its assigned note ID before adding a CHECK_EVENTS row.

### C1. A tame arithmetic inertia subgroup need not be central

- **Target:** the unrestricted central-extension wording in Hua’s `29-formal-tame-pi1-self-intersection` and “La suite exacte”, not a centrality statement in frozen scan096.
- **Assumptions/construction:** let K=F₂((t)); let ζ satisfy ζ²+ζ+1=0 in F₄; set L=F₄((u)) with u³=t. The extension F₄((t))/K is the degree-two constant extension, and `X³−t` is Eisenstein over F₄[[t]], so `[L:K]=6` and the ramification index is 3, prime to residue characteristic 2. L contains all roots `u,ζu,ζ²u`, and separability follows because 3 is nonzero in F₂, hence L/K is Galois.
- **Check:** define r by `r(u)=ζu`, fixing F₄, and σ by `σ(ζ)=ζ²`, `σ(u)=u`. Both fix K; r has order3, σ order2, and direct evaluation on u and ζ gives `σrσ⁻¹=r²≠r`. The inertia subgroup is `<r>`, because σ acts nontrivially on the residue field while r fixes it.
- **Result:** this tame finite quotient is C₃⋊C₂, with noncentral inertia. It occurs for the punctured formal disc `Spf F₂[[t]]` with boundary `(t)`, so the formal arithmetic setting does not remove the obstruction. If the full inertia kernel were central, every finite quotient image would be central, contradicting this quotient.
- **Refined statement:** retain the natural cyclotomic action on the Tate/inertia coefficient; centrality follows only when that action on the relevant quotient is trivial, e.g. after suitable geometric base change, not merely after choosing a basis.
- **Proposed CHECK_EVENTS type:** `refuted, with the refined statement's id`.
- **Outcome wording:** “Refutes Hua’s unrestricted centrality adjective by the tame C₃⋊C₂ quotient of F₂((t)); refined statement retains the cyclotomic action. Does not refute any centrality claim on scan096, which makes none.”

### C2. Vanishing Pi₂ alone does not split a central extension

- **Target:** the inference from the vanishing Π₂ premise to interpreting “extension triviale” as a split/direct-product assertion on scan096 and in Hua’s gloss.
- **Assumptions/construction:** the torus has contractible universal cover R², hence Π₂=0 and π₁=Z². Let H be the integral Heisenberg group of triples `(a,b,c)` with product `(a,b,c)(a′,b′,c′)=(a+a′,b+b′,c+c′+ab′)`.
- **Check:** projection to `(a,b)` yields `1→Z→H→Z²→1` with central kernel `(0,0,c)`. Every lift of `(1,0)` and `(0,1)` has commutator `(0,0,1)`, since changing either lift by the central kernel does not change that commutator. A section from the abelian group Z² would give commuting lifts, so no section exists.
- **Result/limits:** Π₂=0 does not imply splitting; a nonzero degree-two extension class can remain. This does **not** independently construct an algebraic formal-curve counterexample or identify its fundamental group; checking that comparison and the original hypotheses is an outstanding geometric task.
- **Proposed CHECK_EVENTS type:** `targeted proof check`.
- **Outcome wording:** “The proposed inference Π₂=0 ⇒ split extension fails in the explicit Heisenberg extension of Z²; the formal-geometric assertion and its hidden hypotheses are not thereby fully refuted.”

### C3. Cokernel of multiplication by the self-intersection degree

- **Target:** edge cases of the P¹ formula on scans096–098, conditional on its asserted exact sequence and multiplication map.
- **Assumptions:** let T=`∏_{ℓ≠p}Z_ℓ(1)` in characteristic p>0, or the product over all primes in characteristic zero. Assume the connecting homomorphism in the P¹ case is multiplication by the integer degree d on T.
- **Check/result:** if d=0, `coker(d:T→T)=T`. If d≠0, each ℓ-adic factor gives `Z_ℓ/dZ_ℓ`, zero unless ℓ divides d, and their product is cyclic of order the prime-to-p part of `|d|` (order `|d|` in characteristic zero). This is compatible with μₙ over an algebraically closed field for n prime to the characteristic.
- **Limits:** this checks the abelian-group cokernel, not the asserted geometric exact sequence or its degree normalisation/sign. It exposes the missing zero-degree convention without disproving the nonzero-degree formula.
- **Proposed CHECK_EVENTS type:** `computation or formal certificate` (computation only).

### C4. Invariant cyclic subgroups do not by themselves commute

- **Target:** a possible bare group-theoretic justification for cancelling “commutent deux à deux” on scan103.
- **Assumptions/construction:** in Q₈, let A=`<i>` and B=`<j>`. Each is cyclic of order4 and index2, hence normal.
- **Check/result:** `ij=k` and `ji=−k`, so A and B do not commute; their commutator contains −1 in `A∩B`. Thus invariance plus cyclicity is insufficient, independently of the geometric special assumptions that may have been intended.
- **Limits:** no claim is made that this Q₈ configuration is realised by a cover satisfying every implicit hypothesis on scan103. It is a hypothesis diagnostic, not a refutation of the intended Kummer corollary.
- **Proposed CHECK_EVENTS type:** `targeted proof check`.

### C5. Independent completion of the linear quasi-unipotence lemma

- **Assumptions:** E is finite-dimensional over any field k; F,G are automorphisms; q is an integer >1; `FGF⁻¹=G^q`. Invertibility is already present in the frozen scan104 reading.
- **Proof:** pass to an algebraic closure. Similarity shows that the finite set Φ of nonzero eigenvalues of G equals the eigenvalue set of `G^q`, so `λ↦λ^q` is a surjective self-map of Φ and hence a permutation. For λ on a cycle of length r, `λ^{q^r}=λ`, and since λ≠0, `λ^{q^r−1}=1`. Take N to be the least common multiple of the finitely many resulting positive exponents. Every eigenvalue of `G^N` is 1, so by Cayley–Hamilton `(G^N−1)^{dim E}=0`; this equality descends to k. Hence `G^N` is unipotent, with no characteristic-zero assumption.
- **Result/limits:** the stated linear algebra lemma is correct. This is not the full geometric local monodromy theorem, does not explain why the entire manuscript face is cancelled, and does not supply the group-scheme statements LM1 E.2/E.11.
- **Proposed CHECK_EVENTS type:** `independent re-proof`.

### C6. Why the coefficient functor is left exact

- **Assumptions:** work on a site where finite constant abelian groups define exact constant-sheaf sequences; assume `H¹(X,M)=0` for every finite constant abelian coefficient M, as in the intended simply connected étale setting.
- **Check:** for a homomorphism `u:A→B` of finite abelian groups, put K=ker u, C=im u, Q=coker u. The long exact sequence for `0→K→A→C→0`, with `H¹(X,C)=0`, gives `0→H²(X,K)→H²(X,A)→H²(X,C)`. The sequence `0→C→B→Q→0`, with `H¹(X,Q)=0`, makes `H²(X,C)→H²(X,B)` injective. Therefore `H²(X,K)` is exactly the kernel of `H²(X,A)→H²(X,B)`; finite products are preserved by additivity, so the functor is left exact.
- **Result/limits:** this supports the frozen phrase “exact à g.” It does not prove right exactness, the categorical pro-representability theorem, continuity through the universal pro-cover, or comparison with higher étale homotopy. Hua’s unqualified “exact” should not erase the frozen qualification.
- **Proposed CHECK_EVENTS type:** `targeted proof check`.

## Search evidence by candidate

All searches were against the supplied `context/hua_project/29.modern.tex` and `context/notes/RESULTS_STATE.md` after freezing. Line references are navigation aids; subsection titles and Hua pagination above are the intended citations. Searching, reading and comparing wording were **not counted as proof checks**.

| Candidate | Same-object / same-word searches | Relevant hits read | Context relation / register link |
|---|---|---|---|
| A | `auto.intersection`, `self.intersection`, `H^{2}`, `pi_{2}`, `mu` | 2277–2383; 2440–2461; 2574–2623; 5177–5215 | Restates main connection; adds prior mechanism; `29-formal-tame-pi1-self-intersection` |
| B | `centrale`, `fg`, `g^{q}`, `Tate`, `trivial` | 2306; 2679–2694; 3148–3167 | Counterexample contradicts unrestricted context adjective; cyclotomic qualification added |
| C | `triviale`, `pi_{2}`, `auto.intersection`, `Chern` | 2463–2477; 2345–2383; 2574–2623 | Restates literal “triviale”, adds splitting gloss; logical check narrows it |
| D | `degré`, `auto.intersection`, `mu_{n}` | 2478–2491 | Restates nonzero-degree case; zero case added conditionally |
| E | `entiers`, `pi_{2}`, `Mais`, `H^{2}` | 2493–2531; 2731–2753; 4388–4436 | Restates open question; later context adds an approach, not an answer |
| F | `sans doute`, `abélien`, `fini par dévissage` | 2510–2519 | Different paraphrase of uncertain negative wording; no settled register match |
| G | `Abhyankar`, `hensélien`, `commutent`, `T_{ell}` | 2533–2572; compare3019–3041 | Restates assertions, smooths incomplete proof and revised formulation |
| H | `kummérien`, `On veut`, `Chern`, `xi_{i}`, `gerbe` | 2574–2623; 2646–2675; 5177–5215 | Restates explicit target and adds four-occurrence comparison; same external finding |
| I | `topos`, `annelés`, `formelle`, `Variantes` | 2620–2623; 2258–2461; 5177–5259 | Restates direction; does not establish general ringed-topos variant |
| J | `invariants`, `commutent`, `Corollaire`, `normal`, `mu` | 2646–2675; 2546–2572 | Smooths cancellation/hypotheses; group-theoretic diagnostic adds precise gap |
| K | `quasi.unipot`, `automorph`, `endomorph`, `Lemme 6.5` | header38–44; 2696–2729 | Restates result, differs on source reading; LM1 E.2/E.11 only delimit scope |
| L | `simplement connexe`, `exact à g`, `pro.repr`, `pi_{2}` | 2313–2343; 2731–2753; 4388–4453; 4576–4611 | Restates construction, drops left qualification, adds homotopy identification |
| M | `inertie`, `prolongement`, `Fonctorialité`, `normalisé` | 2962–3017 | Restates dependency, adds continuation; matrix finding downstream |
| N | `matrice`, `det N`, `criterion`, `Remords`, `conjugaison` | 3043–3108; 3136–3177 | Context-only addition; `29-inertia-matrix-determinant`, source image absent |
| O | `pro-`, `indice fini`, `opère sur … E`, `ell`-adic terms | No explicit modernised treatment; closest2538–2572 and2696–2729 | Frozen cancelled fragment adds a lead absent from context; no check |

## Integration cautions

1. **No frozen reading repair.** In particular, scan104's “automorphismes” versus Hua's “endomorphismes” is a research reading discrepancy; the arithmetic negative wording on scan098 also stays marked uncertain.
2. **Central, abelian, and split are different assertions.** Normal/commutative inertia does not imply centrality under an arithmetic base group; centrality does not imply the extension class vanishes; Π₂=0 does not imply splitting.
3. **Keep source and context proof status separate.** Hua's “classical”, identification with log geometry, or supplied proof ending do not make that proof appear on the frozen leaf. The cancellation of scan104 does not by itself establish a mathematical retraction or a transfer to SGA7.
4. **Do not inflate prior results.** The linear lemma neither reproves LM1 E.2 nor resolves LM1 E.11. The external determinant formalization is reported by Hua, not run here; absence of a reference in that project is not a novelty proof.
5. **Additional context-only issue for root if scan122 is in another agent's remit:** Hua's “L’énoncé le plus précis” reports “Remords au nᵒ3,4” on Hua p.121 (archive scan122), and requires triviality of the Tate sheaf before replacing path-dependent identifications by one globally fixed source. Verify those words against that frozen page only if it is supplied/assigned; this support task has not done so.

## Additional wider-context reading requested by root

**Coverage:** subsequently read all of `29.modern.tex` lines245–1380, including the early correspondence, the three ramification-data constructions, local Kummer data, fundamental groups, functoriality, descent, Galois structures, the strict-local classification, the opening finiteness programme, and “Deux complétions d’un croisement normal, et le groupe fondamental local”. One tool display truncated a short middle portion; lines550–635 were re-read to close that coverage gap. These early pages are context only, outside this package's supplied images; their prose is Hua's interpretation.

Only the following links materially help the assigned frozen pages:

1. **Regular branches and conjugacy are already the stated repair to Abhyankar.** In **“Ce que Murre n’arrivait pas à voir (pages 1 à 11)” → “La réponse : cinq énoncés faux, et un diagnostic”**, Hua pp.1–11 (archive scans002–012), lines263–300, the modernised account says the earlier Abhyankar statement required regular Dᵢ and that inertia is defined only up to inner automorphism. This **adds historical/contextual support** to scan100’s explicit regular components and to scan117’s careful conjugacy convention; it is not a missing proof supplied by those frozen leaves. **“29 avril 1967 : le plan en six paragraphes”**, same section, lines302–339, also discusses propagation of prime-to-residue-characteristic inertia through specialisation, the exact issue scan100(b) says “Il faut prouver”. The earlier discussion is therefore a useful proposed antecedent for candidate G, with no new claim of proof completion.

2. **The nonconstant roots-of-unity coefficient is built into the early data.** **“Exemple 3, dans ses deux moutures (pages 18 et 19)” → “Première mouture : par une factorisation de s”**, Hua pp.18–19 (scans019–020), lines602–631, allows locally constant, not necessarily globally constant, group maps; **“Le cas kummérien (pages 19 et 20)”**, pp.19–20 (scans020–021), lines673–739, uses local identifications `u:G_{S′}≃μ_n`. **“La donnée est auxiliaire : l’analogie du site et du topos (pages 22 à 24)” → “Trois exemples d’équivalence”**, pp.22–24 (scans023–025), lines843–853, makes the replacement by globally constant Z/n coefficients conditional on a global identification of roots of unity. This **supports** the qualification in candidates A/B/H: arithmetic twisting is part of the object, not eliminated by an arbitrary orientation at one base point.

3. **The local normal-crossings theorem has a specific cover category.** **“Le cas kummérien local, et la ramification modérée au sens large (pages 21 et 22)”**, Hua pp.21–22 (scans022–023), lines743–798, distinguishes local branches from treating the whole divisor as one component, and describes the Abhyankar characterisation using normality above the boundary and tame behaviour at its generic points. This **adds useful scope** to G and M/N: a later local inertia calculation needs this branchwise category and its hypotheses. It does not establish that scan103's much compressed corollary has written all those hypotheses.

4. **“Actions commute” has two different uses and should not be conflated.** **“Revêtements galoisiens, et pourquoi la catégorie est indispensable (pages 30 et 31)” → “La définition, complétée”**, Hua pp.30–31 (scans031–032), lines1089–1129, supplies from the correspondence the condition that the Galois action commute with the model’s automorphism action. **“La lettre d’accompagnement : le cas strictement local (pages 34 à 38)”**, pp.34–38 (scans035–039), lines1227–1277, expresses this as commuting left Gᵢ and right H actions on a torsor, with classification `Hom(Gᵢ,H)/H`. This **adds a concrete cocycle/action framework** for H and M, but it is not the same assertion as pairwise commutation of different branch inertia subgroups on scan100/103, and hence does not remove candidate J’s hypothesis question by itself.

5. **Local reductions and functoriality are stated with qualifications, not as naive pullback.** **“Fonctorialité en S et en R (pages 25 à 29)” → “L’image inverse d’une donnée, et pourquoi elle est encombrante”** and **“Descente et passage à la limite”**, Hua pp.25–29 (scans026–030), lines1043–1087, distinguish strict pullback of a ramification datum from essential equivalence and announce descent/limit results without proofs. The same section’s opening (lines966–1023) makes quotient/base-change compatibility explicit and declines to write out composition/transitivity. This **adds** a useful warning for the variants on scan101 and the prolongation issue on scan117: local equations and pointwise stabilizers need compatible descent data; the early context does not grant a completed general ringed-topos functoriality theorem.

6. **A nearby context-only link for root’s separate scan107 note.** **“Deux complétions d’un croisement normal, et le groupe fondamental local (pages 41 et 42)” → “Le feuillet de calcul”**, Hua pp.41–42 (scans042–043), lines1318–1354, connects its completions `k[y][[x]]`, `k[x][[y]]`, `k[[x,y]]` to the later local picture at Hua p.106 (=scan107), but does not itself distinguish the full strict local spectrum from its boundary complement in that later diagram. Root is separately checking scan107; this support task did not read its image or add manuscript evidence for it.

These are additions to the source map, not further mathematical checks, so they generate no CHECK_EVENTS rows.

