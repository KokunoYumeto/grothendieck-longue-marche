# Root research draft: scans 174–186 and scope

Draft written after the freeze and context opening. None of the following changes the transcription. Each context reference credits Michel Hua's modernised reading of cote 29, not a diplomatic source; his page numbers are one less than the supplied scan numbers here. The canonical per-item searches will be saved in records/CONTEXT_SEARCHES.tsv before integration.

## N174.1 — A programme, not a completed theorem

**Witness:** cote 29, scan 174, outline items 1–7. **Kind:** unproved claim / unpursued implication. **Source words:** “Généralisations à l'aide de la résolution des singularités”; “la dimension cohomologique de certains corps”. **Context:** hua_project/29.modern.tex, “Un plan en sept sections”, their p.173; relation: restates, with a scope qualification.

The outline proposes two base-change theorems, local and global connectivity criteria, and applications through resolution of singularities to cohomological dimension, without supplying their hypotheses or proofs on this sheet. Hua's outline comparison identifies the same programme, but these headings alone cannot establish either a theorem about a particular field or a date for the undated neighbouring sheets. A useful continuation would identify which version of the second theorem the seven sections were intended to prove before matching it to a published result.

## N176.1 — The spectral-sequence calculation needs its hypotheses

**Witness:** cote 29, scan 176, central spectral sequences and final kernel/cokernel displays. **Kind:** unproved claim. **Source words:** “Ker”; “Coker”; the displayed H²/H³ terms. **Context:** hua_project/29.modern.tex, “π2 contre la tour des revêtements”, “Le calcul”, their p.175; relation: restates the intended calculation but differs in notation certainty.

The page sketches a comparison through the spectral sequence with terms H^p(H_i,H^q(tilde X,G)), ending in kernel and cokernel identifications. To justify the familiar low-degree argument one must specify the abelian coefficient object, the vanishing used on the q=1 row, the limiting operation, and the comparison maps; none can be supplied merely by reading the diagram as the expected theorem. Hua prints a coherent modern calculation, whereas the frozen source retains doubts about the first Π exponent, one H degree, i/j indices and unadorned or underlined limits, so his version is a proposed interpretation rather than confirmation of those glyphs.

## N177.1 — A relative H¹ vanishing left unexplained

**Witness:** cote 29, scan 177, bottom third. **Kind:** unproved claim. **Source words:** “H¹(Y′/Y, Hom(π₁(F̄), z))=0” (z is a doubtful Gothic/Greek reading). **Context:** hua_project/29.modern.tex, “π2 contre la tour des revêtements”, “Le cas d'une fibration”, their p.176; relation: restates with missing hypotheses still unresolved.

The terminal vanishing concerns relative descent cohomology for Y′/Y, not an unrestricted group-cohomology group H¹(π₁(Y),−). The preceding diagrams suggest a fibration argument, but the page does not say enough about coefficients, actions, exactness or the covering to verify that vanishing. Hua gives the same route through the fibration; a proof must first identify this relative H¹ and show that every corresponding descent cocycle is a coboundary, since triviality after pullback alone is not enough.

## N179.1 — Recover the presentation before trusting the generator bound

**Witness:** cote 29, scan 179, proposition and final line. **Kind:** unproved claim / reading question. **Source words:** “strictᵗ proreprésentable”; “n″−n′ générateurs” (the latter is explicitly doubtful). **Context:** hua_project/29.modern.tex, “Descente: pro-représentabilité, et une question ouverte”, “La proposition” and “La traduction simpliciale”, their pp.178–180; relation: differs.

The manuscript claims strict pro-representability of pointed descent data, finite generation under its quasi-compactness condition, and ordinary representability when S″ has finitely many connected components. Hua's explanation uses an edge-generator presentation and retains n″ as a rough bound, omitting the manuscript's doubtful sharper n″−n′. In a finite connected simplicial model a spanning tree removes vertex gauge freedom and triangle relations impose the cocycle identities, but the resulting count depends on degeneracies and conventions, so this observation does not certify or silently repair the displayed bound.

## N180.1 — The two explicit open questions are distinct

**Witness:** cote 29, scan 180, N.B. and margin. **Kind:** self-flagged: a step he himself marks as unverified. **Source words:** “J'ignore”; “j'ignore si dans ce cas Π¹=Π¹_eff”; “Pb”. **Context:** hua_project/29.modern.tex, “Descente: pro-représentabilité, et une question ouverte”, “La question ouverte”, their p.179; relation: restates, separating the broad proposition from its fpqc margin.

He asks whether the effective-data subfunctor is representable when S,S′,S″ are noetherian and, more strongly, whether every datum is effective, while recording a positive case for groups whose identity is the intersection of their finite-index subgroups. The proposition on scan179 permits a submersive map, but the marginal challenge here specifically says faithfully flat and quasi-compact, a material distinction that a modern answer must respect. N180.2 answers that fpqc case using a later theorem and does not settle arbitrary submersive descent.

## N180.2 — A modern answer to the fpqc marginal question

**Witness:** cote 29, scan 180, margin; scan 179, representability assertion. **Kind:** own idea: modern deduction, not a historical novelty claim. **Confidence:** high for fpqc effectiveness, from the cited theorem and descent of the torsor structure; conditional on N179.1 for the stated representing group. **Source words:** “fid plat quasi-compact”. **Context:** hua_project/29.modern.tex, “La question ouverte”, their p.179; relation: adds a modern answer to the margin, not to every submersive map. **Primary sources:** Stacks Project, Lemmas 40.15.3 (0APK), https://stacks.math.columbia.edu/tag/0APK, and 37.66.8 (0AP9), https://stacks.math.columbia.edu/tag/0AP9.

A G-equivariant descent datum on the constant discrete-group scheme G_{S′} is effective for an fpqc cover: this scheme is separated and locally quasi-finite, hence ind-quasi-affine, and Gabber's descent theorem applies. The compatible action, torsor identity and pointing descend as well, giving Π¹=Π¹_eff in this case without noetherian hypotheses on the schemes or a residual-finiteness assumption on G. Under scan179's asserted representability hypotheses the same representing object then represents the effective functor; that final identification is conditional on that earlier assertion, not a fresh proof of it.

## N181.1 — A prime supplied by the modern reading

**Witness:** cote 29, scan 181, both equivalence displays. **Kind:** reading question. **Source words:** “Équivalence de telles”. **Context:** hua_project/29.modern.tex, “La traduction simpliciale”, their p.180; relation: differs.

The frozen transcription has h(p₁ξ)f(ξ)h(p₀ξ)^{-1}≃f(ξ) in both places, while Hua prints the conventional formula with a second cocycle f′. That is a mathematically useful interpretation of equivalence, but it does not justify inserting an unseen prime in either frozen display. The precise question for a future image review is whether the right-hand f carries a separate prime or whether the page abbreviates the relation.

## N182.1 — Pointing and rigidity require different connectedness inputs

**Witness:** cote 29, scan 182, entire live argument. **Kind:** unproved claim. **Source words:** “tte donnée de descente admet une ponctuation”; “tout automorphisme ... ponctuée est trivial”. **Context:** hua_project/29.modern.tex, “Foncteurs semi-cosimpliciaux, et le van Kampen”, their p.181; relation: adds the distinction compressed in the context.

The first assertion uses π₀(k_*)=e and Π¹(k_*,G)=e to trivialize the restriction along the pointing complex, whereas the second uses π₀(K_*)=e to propagate an identity automorphism from the basepoint. Thus existence of the pointing and uniqueness of a pointed automorphism are separate steps, and these degree-zero and degree-one conditions do not assert contractibility. A complete proof should formulate the topology of the quotient obtained by collapsing the indicated pointing subspaces to points, since it affects continuity of the descended cocycles.

## N183.1 — A counterexample to reconstruction by all continuous maps

**Witness:** cote 29, scan 183, conditions a–c and “suffisantes”. **Kind:** own idea: explicit test of the stated reconstruction. **Confidence:** high, by the explicit functor and map below. **Source words:** “on pourra prendre K=lim π₀ᵢ”. **Context:** hua_project/29.modern.tex, “Quand un foncteur est pro-représentable”, their p.182; relation: contradicts the asserted reconstruction under the ordinary meaning of continuous maps.

Set X_n=ℕ^n with truncation maps and F(J)=colim_n Hom(X_n,J): filtered colimits of these representables preserve finite limits, and surjectivity of the transitions implies that membership in F(A) for A⊂J is exactly containment of the representative's image in A, so F preserves even arbitrary intersections of subsets. Every projection K=lim X_n=ℕ^ℕ→X_n is surjective, verifying c). The function g(x)=x_{x₀+1} is continuous because each input has a neighbourhood fixing a sufficiently long prefix, but it factors through no single X_n, since x₀ can be chosen at least n and the later coordinate varied. Consequently the canonical F(ℕ)→C(K,ℕ) is not surjective, refuting the specific reconstruction claimed on the page even when a,b,c hold; N183.3 gives a sufficient finite-stage repair.

## N183.2 — Strict transition maps do not imply surjective limit projections

**Witness:** cote 29, scan 183, “Il faut de plus” before c). **Kind:** own idea: explicit counterexample to a contextual identification. **Confidence:** high, by the inverse system of finite injections. **Context:** hua_project/29.modern.tex, “Quand un foncteur est pro-représentable”, their p.182; relation: supports the manuscript's separate c), contradicts the modern reading's conflation.

For an uncountable set A, index finite subsets S⊂A and put X_S=Inj(S,ℕ), with restriction maps. Every transition is surjective because a finite injection extends over a larger finite subset, but the inverse limit is Inj(A,ℕ)=∅. Thus strictness in the sense of surjective transitions does not imply c), precisely as the source's “Il faut de plus” warns; Hua instead says that all three conditions characterize strict pro-representability. The associated colimit-of-Hom functor still satisfies a,b by the argument of N183.1, so this is a substantive distinction and not merely terminology about the limit.

## N183.3 — Finite stages repair the advertised reconstruction

**Witness:** cote 29, scan 183, the reconstruction formula. **Kind:** own idea: refined sufficient statement. **Confidence:** high, by compactness and a common-stage argument. **Source words:** “\(F(I)\underset{?}{\simeq}C(K,I)\)”. **Context:** hua_project/29.modern.tex, “Quand un foncteur est pro-représentable”, their p.182; relation: refines the unqualified assertion, not a change to the transcription. **Primary background:** Stacks Project, Section 5.22, https://stacks.math.columbia.edu/tag/08ZW.

If the inverse system consists of finite discrete sets with surjective transitions, its limit K is profinite, and each continuous map K→J to a discrete set has finite image. Cover K by basic cylinders on which the map is constant, select a finite subcover, and dominate their finitely many indices by one index i; surjectivity K→X_i then defines a map X_i→J inducing the original map. The same surjectivity checks equality of representatives at a common stage, proving colim Hom(X_i,J)≅C(K,J). This compactness proof isolates what fails for ℕ^ℕ in N183.1, where local finite-prefix dependence need not be uniformly bounded.

## N183.4 — Space, group and the meaning of π₀

**Witness:** cote 29, scan 183, final N.B. **Kind:** reading question / unproved claim. **Source words:** “L esp. top”; “(quasi) compact”; “Bourb. Topologie II p.232, prop6”. **Context:** hua_project/29.modern.tex, “Quand un foncteur est pro-représentable”, their p.182; relation: differs.

The source calls L a topological space, while Hua calls it a topological group and interprets the comparison as a group-theoretic warning. Its π₀ must also be defined carefully: the page's separation by clopen sets points toward a quotient detected by locally constant functions, which cannot be identified with the ordinary connected-component space in unrestricted topological generality without proof. The compact case and the cited Bourbaki proposition deserve a separate source comparison; neither a group structure nor a corrected final word has been inserted into the frozen text.

## N184.1 — A cancelled sheet retains two unresolved notation differences

**Witness:** cote 29, scan 184, top and boxed right-centre label. **Kind:** reading question. **Source words:** the doubtful “qu. tot. / disco”; “π₁^eff(S,a)”. **Context:** hua_project/29.modern.tex, “Trois feuillets d'un autre ordre”, “Un feuillet d'esquisses”, their p.183; relation: differs.

The frozen reading of the boxed symbol is π₁^eff(S,a), consistent with a second effective-functor label on the sheet, whereas Hua reads π₁^# and explicitly declines to interpret #. Near the upper diagram the frozen text marks the abbreviated words as doubtful, while Hua supplies “groupe topologique discret”. These are post-freeze comparison questions, with low confidence at the abbreviated words, and the cancelled state of the entire sheet prevents treating either proposed reading as a settled definition.

## N185.1 — The live text deliberately changes representability language

**Witness:** cote 29, scan 185, first kernel paragraph. **Kind:** withdrawn in the same text / reading question. **Source words:** deleted “strictement pro”, inserted “T-”. **Context:** hua_project/29.modern.tex, “Le noyau, et le foncteur semi-cosimplicial”, their p.184; relation: differs.

Grothendieck replaces “strictement pro” by “T-” before “représentables”, then claims closure of T-representable functors under inverse limits by taking a direct limit of spaces and an associated π₀. Hua flattens this distinction to pro-representability, obscuring a change that matters in light of N183.1. For a diagram actually given by continuous maps of spaces, continuous maps from its topological colimit into a fixed discrete set satisfy the expected limit identity; whether all the required natural transformations arise that way, and whether the subsequent π₀ operation preserves the same functor, are additional questions.

## N186.1 — A van Kampen programme with a limited link to current projects

**Witness:** cote 29, scan 186, last paragraph. **Kind:** unpursued implication. **Source words:** “Il y a lieu de généraliser”; “catégories galoisiennes attachées à chaque pt”; “Van Kampen”. **Context:** hua_project/29.modern.tex, “Le van Kampen”, their p.185; notes/RESULTS_STATE.md, EXIT_TOWER B.27 and FINMON C2-CP2; relation: adds a methodological cross-link, not a proof or status change.

The proposed generalisation replaces bare components of a simplicial space by Galois categories at its points, suggesting a descent diagram of categories rather than only a presentation of one group. This bears methodologically on the colimit-of-groupoids construction claimed in EXIT_TOWER B.27, but supplies neither that run's finite diagram nor its proof. It does not answer FINMON C2-CP2: the Π⁰/Π¹ formalism on these sheets does not determine the full higher homotopy type or the minimum size of a finite category modelling CP², and those register entries remain background claims with their stated status.

## N186.2 — A coefficient letter retained despite the expected convention

**Witness:** cote 29, scan 186, first pair of Π formulas. **Kind:** reading question. **Source words:** “Π¹(F*,ζ;E)” (ζ/ξ doubtful). **Context:** hua_project/29.modern.tex, “Le noyau, et le foncteur semi-cosimplicial”, their p.185; relation: differs.

The frozen source has E as the final argument of both Π⁰ and Π¹ in this pair, whereas Hua's uniform exposition uses the group variable G in degree one. The surrounding convention makes G a plausible intended coefficient, but that is not evidence to replace the written E. This is a local notation question, not a mathematical counterexample or a proof check.

## N141.1 — Boundaries of the results-state connection

**Witness:** cote 29, scans 141–143 and 171–172. **Kind:** unpursued implication / scope note. **Source words:** “gr. finis”; “G un groupe discret”. **Context:** notes/RESULTS_STATE.md, LM1 E.11, LM1 E.2, MPL_11_043-058+56 N063/N100, and Hua findings 29-fundamental-group-scheme-via-torsors / 29-h1-five-classes-infinite-group; relation: narrows the subject-only matches.

The packet develops finite-group-scheme torsors and torsors for possibly infinite discrete groups, giving direct material for the two named Hua findings. It supplies no fibrewise-unipotent section to which LM1 E.2 could be applied and no proof of the source theorem for arbitrary separated locally finitely presented group schemes in LM1 E.11. The latter remains open as recorded, the former remains only the return's claimed result here, and N063/N100 remain subject-level leads rather than evidence of a shared theorem.
