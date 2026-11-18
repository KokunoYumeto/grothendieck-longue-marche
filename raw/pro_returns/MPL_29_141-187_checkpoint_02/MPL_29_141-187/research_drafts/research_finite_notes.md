# Research draft: finite pointed torsors, finite étale covers, and scan 187

Prepared 18 November 2026 by GPT-6 Astra Pro, agent `/root/research_finite`; effort setting not exposed to this agent. This is a post-freeze research draft, based only on the frozen text fragments and the supplied context, not a new reading of the scans. The parent reports that the transcription was frozen at 2026-11-18 06:35:56 UTC before the context was opened. No transcription, doubts, inventory, or page files were edited by this agent.

**Citation convention.** All manuscript citations below are cote 29, our scan numbers. Michel Hua's project is credited whenever its AI-produced modernised reading is used; its page number is our scan number minus one. Context leads and register statuses are not treated as established theorems. Actual `rg` searches for every candidate, including all matches, are in `research_finite_context_search.tsv`; the short summary is in `research_finite_context_search_summary.txt`. Detailed mathematical checks and their limits are in `research_finite_checks.md`, and the proposed check-event rows are in `research_finite_events.tsv`.

## Proposed notes

### RF01 — Reducedness is lost during the proof of Proposition 4

- **File/scans:** cote 29, scans 141–142, Proposition 4 and final paragraph.
- **Kind:** self-flagged; unproved claim.
- **Context:** `context/hua_project/29.modern.tex`, “Les groupes admissibles” and “La proposition 4, démontrée deux fois” $their 136–140 = our 137–141$, “La fin de la proposition 4” $their 141 = our 142$; `context/notes/RESULTS_STATE.md`, Hua finding `29-fundamental-group-scheme-via-torsors`.

The warning “Attention, on perd le fait que S est réduit, S1 ne l'est plus” identifies a real limitation of the torsor-trivialising base change $S_1=P$, and the proof ends by invoking “l'unicité” of the pointed map $P\to P\times_vG'$. Hua's modernised reading omits the warning and identifies $P_1$ with $G'_1$, whereas the frozen fragment identifies it with $G_1$. Returning to a diagram over the original $S$ avoids simply reapplying a reduced-base lemma over $P$, but the earlier contextual rigidity lemma concerns equivariant isomorphisms for one fixed group, while the two displayed maps here are respectively $u$- and $v$-equivariant. The equality of those maps, and hence the assertion that the fibre product $R$ is an $H=\operatorname{Eq}(u,v)$-torsor, remains an explicit proof obligation in this check; Hua's account does not by itself discharge it.

### RF02 — What is formal in the strict pro-object construction

- **File/scan:** cote 29, scan 143, first two paragraphs.
- **Kind:** unproved claim; own idea (conditional verification).
- **Confidence/reason:** high for the formal deduction conditional on Proposition 4 and the stated image/minimality hypotheses; no certification of RF01's geometric input.
- **Context:** `context/hua_project/29.modern.tex`, “Le pro-objet” $their 142 = our 143$ and “La pro-représentabilité” in the 1959 letter $their 124–127 = our 125–128, outside this package$; `context/notes/RESULTS_STATE.md`, `29-fundamental-group-scheme-via-torsors`.

The phrase “Ces propriétés formelles suffisent” can be made precise: take the minimal pointed torsors, dominate two of them by a minimal reduction of their product, and use Proposition 4 to make the transition map unique. Minimality of the target and the image condition force each such transition homomorphism to be an epimorphism, giving the strict inverse system asserted on the page. This conditionally checks the formal passage already described by Hua's project, but differs from his phrase “sans passer par les couples minimaux”: the local argument explicitly begins with a minimal $\alpha$ on scan 141 and uses minimality to force $H=G$. It does not prove the missing geometric uniqueness step in RF01 and does not constitute a new construction beyond the registered lead.

### RF03 — Which hypotheses might become unnecessary over a field?

- **File/scan:** cote 29, scan 143, Example II.
- **Kind:** conjecture; own idea (conditional counterexample to one interpretation).
- **Confidence/reason:** high for the example; medium for its relevance because the antecedent of “les hyp. dessus” is not specified.
- **Context:** `context/hua_project/29.modern.tex`, “Le pro-objet” $their 142 = our 143$, “Le dispositif” in the 1959 letter $their 124–126 = our 125–127$; `context/notes/RESULTS_STATE.md`, `29-fundamental-group-scheme-via-torsors`, LM1 E.11 and LM1 E.2 (scope distinction only).

The tentative claim that allowing all finite $k$-groups “rend vraisemblt inutiles les hyp. dessus” should not be expanded into an unconditional removal of reducedness. In characteristic $p$, on $S=\operatorname{Spec}k[\epsilon]/(\epsilon^2)$, the trivial $\alpha_p$-torsor has the nonidentity equivariant automorphism $z\mapsto z+\epsilon$, which fixes the chosen geometric point, so the usual pointed rigidity fails. This checks a limit on one possible interpretation of the manuscript's conjecture, rather than refuting an unambiguous statement of his. LM1 E.11 concerns a different general group-scheme theorem and LM1 E.2 concerns unipotent sections of linear groups over $\mathbb Q$-algebras; neither is settled or contradicted by this characteristic-$p$, finite-torsor example.

### RF04 — The 1959 and abelian-variety material lies before this packet

- **File/scans:** cote 29, scans 141–143; context-only comparison to scans 125–130.
- **Kind:** reading question; unpursued implication.
- **Context:** `context/hua_project/29.modern.tex`, “Lettre à Serre, 18 août 1959 : le groupe fondamental infinitésimal” $their 124–126 = our 125–127$, “Le calcul sur une variété abélienne” $their 127–129 = our 128–130$, “Le pro-objet” $their 142 = our 143$; `context/notes/RESULTS_STATE.md`, orientation item 1 and `29-fundamental-group-scheme-via-torsors`.

Scans 141–143 supply the minimal-torsor argument and the notation “\(\pi_1^C(S,\xi)\)”, but they neither date these particular leaves nor carry the computation for an abelian variety. Hua's project's dated letter and formula $\pi_1(X/k)=\varprojlim_n {}_nX$, together with the Cartier-dual description, belong to his pages 124–129, our scans 125–130, outside this packet. Thus these leaves add local proof evidence to the registered fundamental-group-scheme lead, while the date and the abelian-variety calculation remain context evidence from an earlier packet. This note makes no new priority or Nori-attribution claim.

### RF05 — The cocycle really has the order printed in the rectangle

- **File/scans:** cote 29, scans 145 and 147.
- **Kind:** unpursued implication; own idea (small formal check).
- **Confidence/reason:** high, by composing the two paths around the frozen diagram.
- **Context:** `context/hua_project/29.modern.tex`, “Données de descente : la relation de cocycle” $their 144–146 = our 145–147$, and its comparison with their 180 = our 181; no matching settled RESULTS_STATE entry.

The boxed relation “\(A_{\alpha''}a''_\beta A_{\alpha'}=a'''_\beta A_{\alpha'''}a'_\beta\)” is exactly the equality of the upper-right and lower-right composites, with composition read right to left. The trivial-path substitutions on scan 147 give \(g=g^2\), hence \(g=1\), using invertibility rather than any commutativity assumption. This supports Hua's project's cocycle interpretation, but the connection to the later descent equation on our scan 181 is a structural comparison, not a proof of effectiveness of the descent datum.

### RF06 — The packet contains distinct textual strata and a limited date bound

- **File/scans:** cote 29, scans 144, 146, 148 and 150.
- **Kind:** unpursued implication; reading question.
- **Context:** `context/README.md`, “This package in our plan”; `context/hua_project/29.modern.tex`, “« Compléments aux notes IHES » : le \(\pi_1\) d'un produit fibré” $their 148–150 = our 149–151$, final footnote about their 149 = our 150; no matching settled RESULTS_STATE entry.

The cover “Compléments SGA / 1960” on scan 144 and the reused circular dated 23 May 1961 on scan 150 are separate material witnesses, not a date for every intervening argument. The typed pages on scans 146 and 148 concern the Hilbert Nullstellensatz/Jacobson argument and uniform completion by minimal Cauchy filters respectively, rather than the adjacent fundamental-group constructions. Hua's project recognises the circular as reused paper and treats its date only as a lower bound for the accompanying sketch; the searches found no matching discussion of the two reused mathematical typescripts or the cover title. These pages support a mixed compilation around fundamental groups and descent, not the planning guess of a packet devoted specifically to SGA 3 re-edition work.

### RF07a — Product theorem: the hypotheses differ materially from Hua's rendering

- **File/scan:** cote 29, scan 149, statement and final bracket.
- **Kind:** reading question; withdrawn in the same text.
- **Context:** `context/hua_project/29.modern.tex`, “L'énoncé” under “« Compléments aux notes IHES » : le \(\pi_1\) d'un produit fibré” $their 148 = our 149$; no matching settled RESULTS_STATE entry.

The frozen text assumes “Y connexe”, retains the local noetherian hypothesis, and in the field case says “Y connexe sur k sans plus”; Hua's project instead writes \(Y\) nonempty and later simply connected. It also replaces an étale condition on \(S'\) by “connexe”, retaining étaleness only as an example sufficient for the required injectivity of \(\pi_1(X')\to\pi_1(X)\), whereas Hua retains étaleness in the general criterion. These differences affect the scope of the theorem and should remain visible as reading questions, without changing the frozen transcription.

### RF07b — The product theorem reduces to comparison of two fibre kernels

- **File/scans:** cote 29, scans 149 and 151.
- **Kind:** own idea (targeted proof check).
- **Confidence/reason:** high for the group-theoretic comparison, conditional on the two homotopy exact sequences; historical meaning of “séparable” not re-established here.
- **Context:** `context/hua_project/29.modern.tex`, “La démonstration” under the product theorem $their 150 = our 151$, adding an explicit kernel check to Hua's diagram; no matching settled RESULTS_STATE entry.

The assertion “Cet hom est surjectif” follows directly when the two kernels over \(\pi_1(S)\) and \(\pi_1(Y)\) are images of the same geometric-fibre group \(A\). The comparison is injective precisely when \(\ker[A\to\pi_1(X\times_SY)]=\ker[A\to\pi_1(X)]\), and a map \(S'\to Y\) together with injectivity \(\pi_1(X')\to\pi_1(X)\) supplies the reverse containment. This checks the formal mechanism of the manuscript and Hua's reading, while a modern source for the exact rows is the flat, proper, finitely presented, geometrically connected and reduced-fibre theorem in [Stacks, 0BUM](https://stacks.math.columbia.edu/tag/0BUM). The check does not silently identify all those modern hypotheses with the manuscript's abbreviated “séparable”.

### RF08 — The cancelled classifying-topos draft uses arbitrary \(\pi\)-sets

- **File/scan:** cote 29, scan 152, cancelled draft.
- **Kind:** reading question; own idea (scope check).
- **Confidence/reason:** high, since the regular object must itself belong to the stated category.
- **Context:** `context/hua_project/29.modern.tex`, “Le topos des \(\pi\)-ensembles” $their 151 = our 152$; no matching settled RESULTS_STATE entry.

The manuscript's “catégorie des ens où \(\pi\) opère” and regular object \(\pi_S=T\) allow an arbitrary discrete group and arbitrary sets. Hua's project repeatedly inserts “finis”, but if \(\pi\) is infinite its regular \(\pi\)-set is not finite, so the displayed reconstruction \(E=F(\pi_S)\) cannot take place in that restricted category. The draft therefore supports the classifying-topos interpretation for all \(\pi\)-sets; the identification of group cohomology is recorded as its claim, without a new cohomological proof here. The frozen doubts about the final \(\operatorname{Hom}\) notation remain unchanged.

### RF09 — Serre's frame torsor supplies the quotient and its étaleness

- **File/scans:** cote 29, scans 153–154 and 156.
- **Kind:** self-flagged; own idea (targeted proof check).
- **Confidence/reason:** high, by étale-local splitting and descent.
- **Context:** `context/hua_project/29.modern.tex`, “La proposition 3.2” and “La démonstration de Serre” $their 152–155 = our 153–156$; no matching settled RESULTS_STATE entry.

The page credits “la démonstration ainsi que le résultat” to J. P. Serre and marks “\(P/H\) est étale … (vérif)” while constructing \(P\) from distinct \(n\)-tuples. Over an étale splitting of \(X/Y\), \(P\) becomes the constant set of \(n!\) bijections \(I_n\to X_y\), and quotienting by the last-coordinate stabiliser \(H=S_{n-1}\) gives exactly the \(n\)-element fibre of \(X\). This verifies \(P\) as an \(S_n\)-torsor and \(P/H\simeq X\), including the marked étaleness step, using descent of finite étale objects and [Stacks, 02VN](https://stacks.math.columbia.edu/tag/02VN). It confirms Hua's frame-cover explanation while making explicit that the manuscript's invoked Proposition 2.5 is not proved on these leaves.

### RF10 — A connected dominating cover need not keep the full symmetric group

- **File/scans:** cote 29, scans 153 and 156, final corollary.
- **Kind:** unpursued implication; own idea (example).
- **Confidence/reason:** high, from the explicit cyclic degree-three cover.
- **Context:** `context/hua_project/29.modern.tex`, “La démonstration de Serre” $their 152–155 = our 153–156$; no matching settled RESULTS_STATE entry.

The corollary says that when \(X\) is connected one may take “\(P\) connexe” in (iii), but does not say that the full \(S_n\)-frame torsor in (iii bis) is connected. For \(\mathbb G_{m,\mathbb C}\to\mathbb G_{m,\mathbb C}\), \(z\mapsto z^3\), the monodromy is \(C_3\subset S_3\), so its frame torsor has two connected components; choosing one changes the structural group to its stabiliser \(C_3\). This clarifies the older torsor-like use of “galoisien” in the frame construction and prevents conflation with the connected Galois-cover convention in [Stacks, 03SF](https://stacks.math.columbia.edu/tag/03SF). Hua's construction is supported in this qualified sense.

### RF11 — The marked inertia argument needs separatedness

- **File/scans:** cote 29, scans 157 and 155; finite case on scans 153–154.
- **Kind:** self-flagged; own idea (counterexample and repair).
- **Confidence/reason:** high, by an explicit gluing example and the diagonal criterion.
- **Context:** `context/hua_project/29.modern.tex`, “La proposition 3.1 : l'existence de \(X/G\)” $their 154 and 156 = our 155 and 157$, and “La démonstration de Serre”; no matching settled RESULTS_STATE entry.

The step “opère triv. sur tte la composante connexe … (vérif)” is false for an arbitrary nonseparated étale \(X/Y\): on the affine line with doubled origin over \(\mathbb A^1\), the involution exchanging origins fixes \(D(t)\) and has a nonclosed inertia locus. For separated étale \(X/Y\), the equaliser of \(g\) and the identity is both open and closed, as the pullback of the diagonal, so a geometric fixed point forces \(g\) to be the identity on its connected component. Thus the finite étale use on scans 153–154 is sound, and the later phrase “X étant qu. affine sur Y” supplies sufficient separatedness if it is a standing hypothesis. Hua's added quasi-compactness alone does not repair the broad statement, since the doubled-origin example is quasi-compact.

### RF12 — The local completion argument has a descent substitute

- **File/scans:** cote 29, scans 155–156.
- **Kind:** unproved claim; own idea (limited alternative proof).
- **Confidence/reason:** high for the finite étale torsor case; the unreadable proposition reference and general completion hypotheses remain unverified.
- **Context:** `context/hua_project/29.modern.tex`, “La proposition 3.1 : l'existence de \(X/G\)” and its corollary $their 154–155 = our 155–156$; no matching settled RESULTS_STATE entry.

The assertions “alors il opère sans inertie” and “Reste à voir que X/G est étale sur Y” use the component argument of RF11, followed by a faithfully flat residue-field extension and a diagram of completed local rings. In the finite étale frame situation one can instead split the cover étale locally, take the quotient of the resulting finite set, and descend it, which proves the quotient is finite étale without supplying unstated hypotheses for the completion argument. This is a check of that restricted quotient claim, supported by [Stacks, 0BL6](https://stacks.math.columbia.edu/tag/0BL6) and [02VN](https://stacks.math.columbia.edu/tag/02VN), not a verification of the manuscript's general local-ring proof. Hua's project reverses the drawn residue-field tower to its expected algebraic order; that remains a research correction, not an alteration of the frozen drawing.

### RF13 — Why the empty-fibre axiom can be removed

- **File/scan:** cote 29, scan 158, deleted Gal 3 and retained Gal 5.
- **Kind:** withdrawn in the same text; own idea (targeted proof check).
- **Confidence/reason:** high for the literal definition of connectedness and the intended finite component decomposition.
- **Context:** `context/hua_project/29.modern.tex`, “Les axiomes” and “Ce qu'on voit dans la fabrication” $their 157 = our 158$; no matching settled RESULTS_STATE entry.

The deleted axiom “\(F(X)=\varnothing\)” implies initiality reappears as a consequence of Gal 5. The point requiring care is that the page's definition counts the initial object \(0\) as connected: if a nonzero connected \(C\) had \(F(C)=\varnothing\), Gal 5 applied to \(0\to C\) would make it an isomorphism, and Gal 2 plus preservation of sums then handles every \(X\). This checks Hua's redundancy interpretation without replacing the manuscript's connected-object version of Gal 5 by the unrestricted conservativity statement Hua prints. It depends on the retained definition, not the nonzero-connected convention often used elsewhere.

### RF14 — The second axiom list uses “non ramifié” as a covering class

- **File/scan:** cote 29, scan 159, axiom 6 and final lines.
- **Kind:** unproved claim; reading question.
- **Context:** `context/hua_project/29.modern.tex`, “La seconde version : des points au lieu d'un foncteur” $their 158 = our 159$; no matching settled RESULTS_STATE entry.

Axiom 6 explicitly makes \(\operatorname{Hom}(\xi,X)\to\operatorname{Hom}(\xi,Y)\) “surjectif” for every designated nonramified map with connected target. This cannot mean all modern étale morphisms, since the empty étale map to a nonempty connected scheme fails it, so the intended class needs a covering/nonempty-source qualification. Hua's project omits this condition in its prose summary and reads the final covariance statement as a move to a fundamental groupoid, whereas this leaf explicitly asserts only \(\pi_1(X,x)\) and its covariance. The groupoid interpretation is a useful contextual link, but neither that construction nor consistency of all nine axioms is proved by this check.

### RF15 — The category-theoretic examples are affine and quasi-projective

- **File/scans:** cote 29, scans 160–161.
- **Kind:** reading question; unpursued implication.
- **Context:** `context/hua_project/29.modern.tex`, “« Groupe fondamental dans les catégories »” $their 159–160 = our 160–161$; no matching settled RESULTS_STATE entry.

The frozen example says “plats et affines” or “plats et quasi-projectifs”, whereas Hua's project gives flat proper or quasi-proper morphisms. The restriction “on ne suppose pas qu'on peut descendre tout morphisme” accompanies effective descent only within the chosen class \(D\), and scan 161 restricts admissible structural homomorphisms to those induced by ordinary groups. These details make the chosen descent class part of the construction and do not identify it with a fully effective descent theory for all schemes. They also leave a scope question about the example's implicit covering/surjectivity conditions, since flat affine maps alone are not all strict epimorphisms.

### RF16 — Two recovered hypotheses change the finite-type proposition

- **File/scan:** cote 29, scan 187, displayed hypotheses.
- **Kind:** reading question; unproved claim.
- **Context:** `context/hua_project/29.modern.tex`, “Une proposition sur les morphismes de type fini” $their 186 = our 187$; no matching settled RESULTS_STATE entry.

The frozen statement retains “Y loc. noeth et univ. japonais” and “f loc. de type fini quasi-fini”, as well as separatedness and finitely many irreducible components of \(X\). Hua's modernised proposition omits both universal Japaneseness and quasi-finiteness, and consequently leaves the quasi-compactness step unexplained. The recovered words supply the two essential inputs for a normalisation/Zariski-main-theorem proof, as detailed in RF18. Here “quasi-fini” must be read in its local/fibrewise historical sense for the conclusion to be substantive, since modern quasi-finite already includes finite type.

### RF17 — The global normalisation arrow is false even after its correction

- **File/scan:** cote 29, scan 187, final paragraph.
- **Kind:** withdrawn in the same text; own idea (counterexample).
- **Confidence/reason:** high, from the open-immersion example satisfying every recovered hypothesis.
- **Context:** `context/hua_project/29.modern.tex`, “Une proposition sur les morphismes de type fini” $their 186 = our 187$, differing from its unqualified “on conclut par la normalisation”; no matching settled RESULTS_STATE entry.

After deleting “surjectif”, the page still claims a global \(X'\)-map \(\widetilde X'\to X''\) merely from the birational map \(X''\to X'\). Take \(Y=X'=\mathbb A^1_k\), \(X=U=D(t)\), and \(U'=D(t)\); the prescribed graph closure is \(X''=D(t)\), but no \(\mathbb A^1\)-map \(\mathbb A^1\to D(t)\) exists, because its composite with the inclusion would have to be the identity. Thus deleting surjectivity does not repair this step, even though the finite-type conclusion is true in the example. The refuted assertion is the global normalisation arrow, not the proposition; RF18 supplies a different proof.

### RF18 — A repair of the proposition via the open normalisation model

- **File/scan:** cote 29, scan 187.
- **Kind:** own idea (targeted proof check).
- **Confidence/reason:** high under the recovered locally quasi-finite interpretation; the proof is written out and its standard inputs are identified.
- **Context:** `context/hua_project/29.modern.tex`, “Une proposition sur les morphismes de type fini” $their 186 = our 187$; `context/notes/RESULTS_STATE.md`, LM1 E.11 and LM1 E.2 checked for scope and not used.

To prove “il suffit de voir que f est quasi. cpt”, work over an affine Nagata base and on one reduced irreducible component, then normalise \(X\) and the integral closure of its image \(Y_0\) in the finite extension \(k(X)/k(Y_0)\). Both normalisations are finite over their respective schemes, and the separated locally quasi-finite birational map \(X^\nu\to T\) to the resulting normal finite \(Y_0\)-scheme is an open immersion, proved locally by Zariski's main theorem. Since \(T\) is noetherian, \(X^\nu\) is quasi-compact; its finite surjection onto \(X\) gives quasi-compactness of \(X\), and the finite collection of components completes the proof. This repairs the theorem without the false reverse arrow in RF17, using [Stacks, 033R](https://stacks.math.columbia.edu/tag/033R), [035A](https://stacks.math.columbia.edu/tag/035A), [035S](https://stacks.math.columbia.edu/tag/035S), and [02LR](https://stacks.math.columbia.edu/tag/02LR), and has no substantive connection with LM1 E.11 or E.2.

## Standing-question material from this assignment

### Explicitly unverified or tentative steps

| Our scan | Manuscript words | Research treatment |
|---|---|---|
| 142 | “Attention, on perd le fait que S est réduit” | RF01 isolates the geometric uniqueness obligation; not certified. |
| 143 | “vraisemblt … inutiles les hyp. dessus” | RF03 gives a conditional reducedness obstruction; antecedent left open. |
| 154 | “P/H est étale … (vérif)” and question marks | RF09 verifies the finite étale frame case by splitting/descent. |
| 155 | “prop ---” | An incomplete proposition reference, not supplied from context. |
| 157 | “opère triv. … (vérif)” | RF11 gives a counterexample without separatedness and the precise diagonal repair. |
| 187 | “surjectif” deleted from the normalisation arrow | RF17 shows that the weakened existence claim still fails. |

### Titles and counts visible in the frozen fragments

| Our scan | Title or printed numbering | Scope |
|---|---|---|
| 144 | “Compléments SGA”; “1960” | Cover; no page count on this fragment. |
| 146 | Printed page −156−, item 280 | Reused typed mathematical sheet; not packet pagination. |
| 148 | Printed page −167−, item 329 | Reused typed mathematical sheet; not packet pagination. |
| 149 | “Compléments aux notes IHES” | Product theorem group. |
| 150 | Circular dated 23 May 1961; 13e année, 1960/61; exposé 221 | Reused circular, not a page-count statement. |
| 158 | “Catégorie galoisienne” | Abstract finite Galois axioms. |
| 160 | “Groupe fondamental dans les catégories.” | Descent-category construction. |

No count of the form “19 pages” or “Pages 1–67” occurs in the frozen fragments assigned to this agent. This is a text-fragment observation, not a fresh image inspection.
