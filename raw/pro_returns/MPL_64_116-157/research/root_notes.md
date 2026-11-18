# Root research notes: level pinning, analytic conventions, and documentary structure

All scan references in this file are to cote 64, current PDF scans 116–157. These notes were written after the freeze; their mathematical refinements and comparison readings do not change the transcription. Context paths are relative to the supplied context directory, and an earlier note's status remains a claim unless a specific new check is recorded.

## L. The unfinished Legendre pinning

### L01 — Scans 118–121, “associer … canoniquement un épinglage de Legendre” — unproved claim

The proposed construction must be functorial in \(E\), compatible with base-field changes, independent of the tangent-vector coordinate, and compatible with the chosen fourth root and cyclic ordering, so merely producing numbers satisfying the half-division equations does not complete the stated programme. Scans 120–121 formulate these requirements and explicitly leave the square normalization unfinished; B04 records the resulting limitation for bridge B5. **Comparison: adds** a detailed construction problem to LM_140-2_notes.md, R24/R28 at scans 527–528 and the level-four programme at scan 570 (R22), while **restating** the unfinished status in Hua's “Vers l'épinglage de Legendre (pages 117 à125).” This bears on LM2 C.d1 and LM4_SUCCESSOR B.38 as geometric input, with no upgrade of either registered status.

### L02 — Scan 119(78)–(81), “canoniquement isom.” — unproved claim

The comparison of the two exact sequences is valid: evaluation at \(t\) identifies \(L\otimes F_t^\vee\) with \(\mathcal O(t)\), the first term becomes constants, and the quotient of principal parts is \(T_t\). AC01 supplies the independent proof, including why the identification is independent of a generator of \(F_t\). **Comparison: restates and verifies** the exact-sequence assertion in Hua's “Vers l'épinglage,” corresponding to current scan 119; no separately numbered result in notes/RESULTS_STATE.md settles this linear-algebra step. It supplies condition b's ambient geometry without proving the condition c deferred on scan 121.

### L03 — Scans 120–121, “\(\varphi_i^\omega(\lambda\delta)=\lambda^{-1}\varphi_i^\omega(\delta)\)” — unpursued implication

The displayed weight \(-1\) is exactly the covariance required for \(\delta_i=\varphi_i^\omega(\delta)\delta\) to be independent of the chosen nonzero vector \(\delta\); substituting \(\lambda\delta\) checks this directly. It is a tensorial scaling law, and supplies no connection operator or rule for differentiating a section. **Comparison: restates** Hua's “Vers l'épinglage,” current scans 120–121, and **adds a necessary distinction** to README.md S20 and notes/RESULTS_STATE.md, MPL_93_002-046 P09, whose comparison remains prospective. S02–S05 make a possible connection-theoretic continuation precise without attributing it to this formula.

### L04 — Scans 123–126, “Cela détermine \((\lambda_i)\) … scalaire inv.” — unproved claim

For distinct roots, the vector of cyclic differences spans the kernel of the matrix with rows \((1,1,1)\) and \((\zeta_1,\zeta_2,\zeta_3)\), so the claimed uniqueness up to scalar follows from rank two. AC02 checks this assertion, and L92 checks the more detailed basis expressions without deciding the doubtful sign on scan 126. **Comparison: restates** Hua's “Vers l'épinglage,” which explicitly presents the attachment of these loose calculations to condition b as its own inference, and **adds** a verified linear-algebra step to L01. The attachment and the computation still leave condition c open, and do not settle LM4_SUCCESSOR B.38.

### L05 — Scans 117–118, “Cf prop.” and “les \(x_i\) sont tous distincts” — unproved claim

The determinant condition uses the plane-cubic group law: three distinct points sum to the origin exactly when their divisor is a line section, since a line cuts a divisor linearly equivalent to three times the origin. Distinctness follows from \(2x_i=\varepsilon_i\) with the three distinct nonzero two-torsion points, while the four possible halves are geometric points or, over the stated field, a four-element torsor only when a rational half exists. **Comparison: restates** Hua's “Les involutions … et les points d'ordre 4,” corresponding to current scans 117–118, and **adds** the hypothesis boundary to the finite-level comparison in LM_140-2_notes.md R22, scan 570, without proving LM2 C.d1. The determinant expansion is independently certified in L92's evidence, but the earlier manuscript proposition cited here lies outside the supplied scan range and was not image-audited in this run.

## T. Two analytic attempts and their limits

### T01 — Scans 131 and143–145, “\(E\simeq V/H\)” and “rigide” — unproved claim

The pointwise lattice description becomes a family statement only when the periods are holomorphic local sections, the condition made explicit in the second attempt on scan 143. A marked automorphism fixing the lattice basis fixes the tangent coordinate and therefore the elliptic curve, which explains the rigidity assertion on scan 144; representing all framed holomorphic families still uses the period-map theorem. **Comparison: restates and makes explicit** LM_140-3_notes.md, R30/R32 at scans 19–20, and LM_140-2_text.tex, scans 259–263, on Teichmüller rigidification and the modular topos. The historical background is already present in Grothendieck (1960–1961a, §2–§3; 1960–1961b, introduction), while Hain (2021, Propositions 2.3–2.4) supplies the precise modern family statement; none is a new result of this run.

### T02 — Scan 132(8), “\(-\varphi(i\varphi(x))\)” — reading question

With \(\varphi:L\to V\) as defined on scan 131, the second displayed expression is not type-correct for \(x\in V\); the preceding expression uses \(\varphi^{-1}(x)\), which is the mathematically meaningful argument (refinement T02.R). **Comparison: agrees with the correction proposed by** Hua's “V. Approche transcendante — première mouture,” its discussion of the construction corresponding to scans 131–132, but that agreement supplies a mathematical diagnosis rather than a new reading of the ink. The literal second expression remains frozen, and no corresponding result-register ID is affected.

### T03 — Scans 135,137,139, “C'est faux, cf calcul plus bas” — withdrawn in the same text

For \(L_z=\mathbb C(z,1)\) and the conjugate transport of scan 132, the matrix \(J_z\) in AC03 gives \(\det(e_1,J_ze_1)=-1/\operatorname{Im}z<0\), giving refinement T03.R and verifying the author's rejection of the asserted orientation on scan 135. Scan 139 explicitly says the chosen basis is “inverse” and considers the alternative line convention \(\mathbb C(1,z)\), so the draft records a genuine internal correction. **Comparison: restates** Hua's “première mouture,” corresponding to scans 134–139, and **adds** an exact orientation calculation to LM_140-3_notes.md, R31/R34 at scans 19–20, on conjugation and basis conventions. This check does not resolve any uncertain bar or inverse in the frozen expressions.

### T04 — Scan 139, “famille … analytique” with \(E_z=\mathbb C/(\mathbb Z+\mathbb Z(-\bar z))\) — reading question

The displayed period ratio is antiholomorphic in \(z\), and the holomorphic period-map criterion therefore excludes the literal formula as a holomorphic framed family on the stated upper-half-plane base. AC04 gives the precise obstruction; the later construction on scans 143–149 uses holomorphic \(\tau\) and supplies a consistent model (refinement T04.R). **Comparison: agrees mathematically with, but does not adopt as a transcription correction,** Hua's deliberate modernization in “première mouture,” corresponding to current scan 139; it also qualifies the family-level inference from LM_140-3_notes.md R30/R32, scans 19–20. This is a local analytic check, with no consequence for the registered arithmetic-image question EXIT_TOWER E.24.

### T05 — Scans 146–148, “échange de \(a\) et de \(d\)” — unproved claim

The natural right action on the ratio is \(\tau\circ g=(d\tau+b)/(c\tau+a)\), and composing it with \(\sigma(g)=\tau_\infty g^{-1}\tau_\infty\) gives the usual left action. AC05 verifies the necessary order reversal \(\sigma(gh)=\sigma(h)\sigma(g)\), so this convention change is algebraically coherent. **Comparison: adds explicit bookkeeping** to LM_140-3_notes.md R34, scan 20, and **restates** Hua's “seconde mouture,” corresponding to scans 146–148, while B02 explains why the infinity subscript is not a computation of the arithmetic inertia source in cote 140-3, scan 25. The formulas do not themselves establish LM2 C.r1–C.r3.

### T06 — Scans 147 and149, “On peut en fait faire opérer” — unproved claim

The automorphy factor satisfies \(j(g,h\tau)j(h,\tau)=j(gh,\tau)\), so the displayed \(T_g\) really is an action on the total covering space and descends through lattice translations. For the exact order of operations on scan 149, the conjugation on translation columns is \(\rho(g)=\left(\begin{smallmatrix}a&-b\\-c&d\end{smallmatrix}\right)\), and multiplication is \((g,v)(h,w)=(gh,v+\rho(g)w)\), as AC05 verifies. **Comparison: restates** Hua's “seconde mouture” family action and **adds** the explicit convention needed in LM_140-2_text.tex, scans 261–263, where the universal-family group extension is discussed without its full formula. This is a discrete geometric verification, not a proof of EXIT_TOWER E.24's arithmetic-image assertion.

### T07 — Scans 140 and149, “revêtement universel de \(M_{1,1}\)” — reading question

The precise mathematical interpretation is the classifying map of the framed base \(\mathfrak H\) to the automorphism-retaining quotient \([\mathfrak H/\mathrm{SL}_2(\mathbb Z)]\), while the literal sentence on scan 149 predicates “revêtement universel” of the displayed family. Its total space has fundamental group \(\mathbb Z^2\), and the action on the base has central kernel \(\{\pm I\}\), so neither the total space nor the coarse quotient can be substituted without changing the statement. **Comparison: restates** the modular-topos distinction in LM_140-2_text.tex, scans 259–263, and **qualifies** LM_140-3_notes.md R36, scan 20, whose effective-action observation alone does not remove the exceptional stabilizers. AC07 gives the elementary obstruction; B07 and S06 retain the separate profinite and connection-theoretic boundaries.

### T08 — Scan 140, “\(\Pi_{\mathrm{ab}}\) … de rang \(1\)” — reading question

For a group of type \((1,1)\), the once-punctured torus retracts to two loops, giving \(\Pi\simeq F_2\) and \(\Pi_{\mathrm{ab}}\simeq\mathbb Z^2\), so refinement T08.R is rank two and the rank-one parenthesis is false under the stated type. The second formulation on scan 150 omits that parenthesis rather than supplying an explicit retraction, and the frozen first formulation remains unchanged. **Comparison: agrees with** Hua's acknowledged rank correction in “première mouture,” and **parallels without conflating** the separate rank-one slip registered in LM_140-3_notes.md R33, scan 20. AC07 is an independent rank calculation; it does not prove a profinite completion statement.

### T09 — Scan 140 margin, “Il faudrait expliciter l'action … extérieure” — own idea

An explicit answer uses \(F_2=\langle x,y\rangle\), \(\widetilde S:(x,y)\mapsto(y,x^{-1})\), and \(\widetilde T:(x,y)\mapsto(x,xy)\), whose abelianization matrices are the standard \(S,T\) and which preserve the conjugacy class of \([x,y]\). AC06 checks the presentation relations modulo inner automorphisms, including \((\widetilde S\widetilde T)^3=\operatorname{Inn}(yx^{-1})\widetilde S^2\), and thereby constructs the discrete outer action rather than merely two unrelated lifts. **Comparison: adds a concrete solution to this deferred step**, alongside the broader explicit-action programme in LM_140-2_notes.md item 467-1, scan 467, while the full \(\operatorname{Out}(F_2)\simeq\mathrm{GL}_2(\mathbb Z)\) identification is carried from Bux et al. (2011, §1), and B07 keeps EXIT_TOWER D.19 distinct from LM2 C.d1. **Our confidence: high** for the displayed action because of exact free reduction and the presentation check; it supplies no new GT arithmeticity or congruence-kernel theorem.

### T10 — Scans 141 and151–152, “base \(\varphi\) de \(t_E\)” — unproved claim

The period space is \(\mathbb C^*\times\mathfrak H\) via \((z_1,z_2)\mapsto(z_1,z_2/z_1)\), and the scan 151 action is the genuine representation \(R(g)=PgP\) for the coordinate-swap matrix \(P\). Replacing the tangent basis by \(\lambda\varphi\) divides both periods and the fiber coordinate by \(\lambda\), explaining the inverse powers in scan 152(22). **Comparison: restates** Hua's “La rigidification différentielle (pages 150 et151)” and **adds** an exact action check to the earlier abstract extension in LM_140-2_notes.md items467-5/467-7, scan 467. H02 treats the additional \(B_3\) identification with proper credit, while S02 explains why this frame is not itself the connection proposed in MPL_93_002-046 P09.

### T11 — Scan 152, “pts … d'ordre \(2\)!” — withdrawn in the same text

Each of the separate \(\mathbb C^*\) and \(\mathrm{SL}_2(\mathbb Z)\) actions is free on the period space, but \((-1,-I)\) fixes the period vector and acts as \(z\mapsto-z\) on its elliptic fiber. Its four fixed points include three nonzero two-torsion points (refinement T11.R), so removing the zero section does not salvage the cancelled free-action assertion. **Comparison: restates and independently verifies** the correction retained in Hua's “La rigidification différentielle,” and **adds** the explicit fixed-point witness to LM_140-3_notes.md R35/R36, scan 20, on effective modular action and stabilizers. AC08 proves the witness; it gives geometric information relevant to the orientation paragraph's LM4 D.12 lead but does not decide torsion in the full profinite GT group.

### T12 — Scans 150–152, “\((-1,-1)\)”: finite automorphisms versus arithmetic images — own idea

A useful continuation would retain the central involution and the extra stabilizers at square and hexagonal lattices when comparing the frame quotient with finite modular levels. **Comparison: adds a finite geometric test case** to notes/RESULTS_STATE.md, “Orientation for this package,” which names LM4 D.12, LM6 A.22, and LM7_PUSH E.3, and **restates** the special-orbit information in LM_140-3_notes.md R35, scan 20. Those IDs concern full profinite torsion or CM arithmetic images, whereas the present formulas only give complex geometric stabilizers, so they provide neither a proof nor a counterexample to the registered open assertions. **Our confidence: medium** in the proposed usefulness, because explicit stabilizers are available but the arithmetic comparison maps are absent.

### T13 — Scans 132–134, “exactement \(2\) sous-espaces propres” and “\(n\) impair” — unproved claim

For an embedded circle acting faithfully with exactly two conjugate weight spaces, the weights must be \(+1,-1\), since a common absolute weight greater than one would leave a nontrivial finite kernel. Its two order-four elements therefore give \(J,-J\), whose induced real orientations differ by \((-1)^n\) in dimension \(2n\), justifying the odd-\(n\) qualification; in real dimension two, invariant positive inner products differ by a scalar. **Comparison: restates and checks** Hua's “première mouture,” corresponding to scans 132–134, without finding a separately numbered counterpart in notes/RESULTS_STATE.md. The conjugate eigenspace required by the earlier transport convention is still a distinct issue, explicitly flagged on scan 134 and recorded in U03.

### T14 — Scans 151–152 and156, “l'invariant modulaire exceptionnel” — reading question

The analytic stabilizer discussion is over \(\mathbb C\), while the arithmetic appendix examines quadratic orders at residue characteristic two; these passages do not compute the automorphism groups of elliptic curves in characteristic three. **Comparison: differs in coverage** from the explicit request in notes/RESULTS_STATE.md, “Orientation for this package,” to examine the special invariants and their characteristic-three behavior, and **restates only an interpretive lead** from LM_140-2_notes.md, second-pass own note S2 at scans 562–565. H06 preserves Hua's proposed identification with 1728 as an interpretation, rather than reading missing exponents or a coarse coordinate into scan 156. This leaves LM4 D.12, LM6 A.22, and LM7_PUSH E.3 unchanged.

### G01 — Scan 154, cancelled “\(g=ux=yu\)” calculation — unpursued implication

Associativity and conjugation give \(y=uxu^{-1}\) and \(g'g=(u'u)(u^{-1}x'u)x\), so the cancelled scratch work correctly relates left and right normal forms in a split extension. **Comparison: restates** the opening of Hua's “VI. Appendice,” corresponding to current scan 154, and **adds a local convention check** alongside T06's noncancelled semidirect-product calculation; no identification of the doubtful diagram's particular group \(G_0\) or symmetric-group label is inferred. The module \(\ker(\mathbb F_2^A\to\mathbb F_2)\) is visible in the diagram, but the page supplies too little definition to attach this cancelled computation to a specific LM2 or EXIT_TOWER result. Cancellation is a documentary state here, not evidence that the displayed associativity identity is false.

## U. Steps the manuscript itself leaves unverified or retracts

### U01 — Scan 118, “Je voudrais … associer … canoniquement” — self-flagged

This is an announced functorial construction, with its remaining obligations itemized on scans 120–121 rather than completed. **Comparison: restates** Hua's “Vers l'épinglage,” and **adds** the precise authorial programme to LM_140-2_notes.md, scan 570 (R22), on Jacobi level four; B04/L01 record the limited bearing on LM2 C.d1 and LM4_SUCCESSOR B.38.

### U02 — Scan 121, “Dieu sait comment — il faudra … y revenir” — self-flagged

The explicitly deferred point is condition c, the prescribed square of \(\kappa\), followed by a necessary dependence relation and the unfinished word “Posant.” **Comparison: restates** Hua's “Vers l'épinglage” and H01, with no later solution in current scans 123–126; L04/L92 explain why their proportionality calculation does not discharge it. The corresponding finite-level input remains incomplete for the B5 comparison.

### U03 — Scans 134–135 and139, “non pas \(L_\omega\), mais \(L_{\omega'}\)” and “C'est faux” — withdrawn in the same text

Scan 134 flags the conjugate-eigenspace convention, and scan 135 retracts the consequent orientation assertion, with the negative orientation calculated on scan 137 and discussed again on scan 139. **Comparison: restates** Hua's first analytic attempt and the convention issues in LM_140-3_notes.md R31/R34, scans 19–20; T03/AC03 independently check the orientation defect. These are internal changes of convention, not silently harmonized formulas in the transcription.

### U04 — Scan 139 margin, “faudrait vérifier … bien analytiquement naturel” — self-flagged

The author explicitly asks for analytic naturality after proposing a changed line convention. **Comparison: differs from treating the adjacent theorem as already verified**, agrees with Hua's first-draft correction, and qualifies the family interpretation in LM_140-3_notes.md R30/R32, scans 19–20. T04/AC04 show the exact holomorphic obstruction for the literal displayed family, while scans 143–149 give the later consistent family.

### U05 — Scan 140 margin, “Il faudrait expliciter l'action … extérieure” — self-flagged

The outer action is requested explicitly, and the second attempt's restatement on scan 150 does not supply generators on \(\Pi\). **Comparison: adds a concrete instance** to LM_140-2_notes.md item 467-1, scan 467, which asks for other explicit outer actions; T09 supplies one modern discrete answer with its limits. This does not review the full EXIT_TOWER D.19 claim.

### U06 — Scan 152, “pts … d'ordre \(2\)!” and the deleted free-action sentence — withdrawn in the same text

The fixed-point observation withdraws the claim that the product acts freely on the family, including the attempted removal of the zero section. **Comparison: restates** Hua's frame discussion and **adds** an explicit correction to the stabilizer context in LM_140-3_notes.md R35/R36, scan 20; T11 verifies the three surviving nonzero fixed points. It is not an open conjecture once the marginal correction is read.

### U07 — Scan 132 margin, “voir une autre explication” — self-flagged

This points to another explanation rather than asserting a specific conjecture or supplying a missing proof. **Comparison: restates** the transition to the compact-circle description in Hua's first analytic attempt, corresponding to scans 132–134; T13 checks that description, but no result-register ID is directly implicated. It is recorded separately so a deferral is not lost by being treated as ordinary exposition.

### U08 — Scans 138 and154–156, question marks and “sauf” — reading question

The uncertain marginal “(?)” among the competing action formulas on scan 138 belongs to a calculation in revision, and is not sufficient to formulate a separate conjecture beyond T03–T05. No literal “sauf erreur,” “je présume,” or “admis” was found in the frozen selection, while scan 154's “sauf … au dessus” denotes an exceptional locus and scan 156's “Cette condition est aussi suffisante” is an unproved assertion rather than an explicit uncertainty marker. **Comparison: adds a bounded marker inventory** to Hua's treatment of the two drafts and arithmetic appendix, with no corresponding result ID; A06 proves the sufficiency under stated hypotheses. This is an inventory of the supplied fragment, not a claim about missing leaves or the rest of cote 64.

## C. Title sheets, page counts, and reused paper

### C01 — Scan 128, “Relations entre \(M_{11}\) et \(M_{04}\)” — reading question

This is a separate title sheet and should not be absorbed into the prose that follows. **Comparison: restates** Hua's opening to “V. Approche transcendante,” which identifies its page 127 as the same title, while notes/RESULTS_STATE.md's broad cote 64 orientation gives no separate proposition or authorial page range for it. No page count is written on this cover.

### C02 — Scan 129, “Approche transcendante” and the doubtful count “(22|21 p)” — reading question

The pencilled count is doubtful between 22 and 21, and its hand is not securely attributed; Hua's “V. Approche transcendante” confidently gives “21 p” for its page 128. **Comparison: differs** in certainty rather than resolving the number: current scans 131–152 occupy 22 scan positions but 21 retained mathematical pages because 142 was omitted as blank, so either counting convention is arithmetically possible. The count remains a marginal annotation, not an authorial page number or a corrected total.

### C03 — Scan 131, “Modules des courbes elliptiques : théorie transcendante” — reading question

This internal heading begins the first analytic attempt, followed by a second attempt beginning on scan 143 without a comparably explicit new title. **Comparison: restates** Hua's division into “première mouture” and “seconde mouture,” but those division labels are Hua's editorial organization, while the current transcription preserves scan order. The archive numbers recorded as comments throughout this selection are not promoted to `\mspage`, and no additional authorial page-range statement is inferred.

### C04 — Scans 153 and155, “normalité des ext. quadratiques” and “Normalité des extensions quadratiques” — reading question

Scan 153 is a title cover, and scan 155 repeats a fuller heading inside the arithmetic material; no page count accompanies either. **Comparison: contradicts the limited documentary assertion** in Hua's footnote after its page 151 that page 152 is blank, since that page corresponds to current scan 153, while agreeing with its ensuing arithmetic appendix's subject. H05 records the discrepancy without altering the frozen cover or inferring a mathematical contradiction.

### C05 — Scan 124, printed thesis notice — reading question

The notice is headed “AVIS DE SOUTENANCE D'UNE THESE DE DOCTEUR-INGENIEUR,” names Alain Pappalardo's thesis on mass transfers in unsaturated soils, and is dated 4 November 1980 for a defense on 12 November 1980. **Comparison: adds the actual printed title and dates** to Hua's “Vers l'épinglage” footnote, which merely identifies its page 123 as a typed defense notice; exact-term context searches found no other matching item or result ID. These are dates of the reused printed paper, not independent dates for adjacent mathematical writing.

### C06 — Scan 127, “LES NOMBRES ENTIERS : UNE PRESENTATION EN TERMES DE LANGAGE ALGORITHMIQUE” — reading question

This printed announcement schedules Jambon's lecture for 12 December 1980 and has its own title and institutional matter, all retained in the transcription. **Comparison: adds its contents** to Hua's first-analytic-section footnote, which only identifies its page 126 as a typed seminar announcement; searches found no matching result-register entry. It supplies a documentary paper date, not a proven composition date of the analytic drafts.

### C07 — Scan 157, “OBJET : Surveillance des examens” — reading question

The reused printed letter bears “9 JUIN 1981” preceded by an uncertain extra “1,” and assigns examinations on 16 June 1981, with mathematical scratch work written across it. **Comparison: adds the printed metadata and retained uncertainty** to Hua's arithmetic appendix, which discusses the scratch calculations without a full diplomatic account of the notice. The mathematical use of a printed sheet presupposes its availability, but identifying the neighboring sheets' dates requires physical evidence beyond this selection; no result-register ID is affected.

## R. Additional post-freeze reading questions

### R01 — Scan 140, “grands théorèmes marteaux-pilons” (last word doubtful) — reading question

Hua's “première mouture,” corresponding to current scan 140, instead gives “grands théorèmes orthodoxes.” **Comparison: differs** in a lexical reading whose plausibility cannot override the frozen ink-based uncertainty; neither alternative is established by the mathematical fact that a mapping-class theorem is invoked. The disagreement is reserved for a later independent image audit and changes no result-register status.

### R02 — Scan 147 marginal diagram, \(\zeta\) or \(\xi\) (doubtful) — reading question

The frozen vertical multiplier label is a doubtful \(\zeta\) or \(\xi\), whereas Hua's “seconde mouture,” corresponding to its page 146, prints a label “2” in the diagram. **Comparison: differs** at one diagram label, and the surrounding ratio \(z_1/z'_1\) identifies the mathematical role without settling the handwritten character. No diagram label is replaced after the freeze.

### R03 — Scans 147–148, “Introduisons l'élément”: physical order versus exposition — reading question

Hua's “seconde mouture” explicitly reverses the corresponding pages 146–147 to put the convention discussion before the family action. **Comparison: differs** editorially, while the present package retains the supplied PDF scan order 147 then 148, even though equation numbering and the logical dependency run the other way. This explains the apparent discontinuity without proposing that the scanned order should be silently repaired.

