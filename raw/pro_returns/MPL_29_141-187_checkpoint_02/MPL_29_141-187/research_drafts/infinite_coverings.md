# Research candidates: cote 29, scans 162–172

Prepared after the root reader's freeze and context opening (2026-11-18 06:35:56 UTC), by GPT-6 Astra Pro, supporting agent `/root/doubt_index`. This agent read frozen TeX fragments and context text, not scan images; no transcription, doubt, inventory, or progress file was changed. The following are candidate research notes for the root reader to review. Manuscript quotations below cite the frozen transcription, not a new reading of the images. Source line numbers in the search appendix are **context TeX/text source lines**, not manuscript lines.

Context read: `context/README.md`, `context/notes/RESULTS_STATE.md`, `context/hua_project/README.md`, and the relevant sections of `context/hua_project/29.modern.tex`. **Hua, modernised reading of cote 29** is credited as an AI-produced interpretation, not as our result. His page number is our scan number minus one. The status “conjecture (unsearched)” of **Hua, findings register, 29-h1-five-classes-infinite-group** is an inherited register status, not an assertion that its comparisons are either established or still absent from the literature. The searches and checks performed here are recorded below.

## Candidate notes

### IC01 — Finite index, categorical cokernel, and a component hypothesis

**Scan:** 162. **Quote:** “propre dominant”; “a un conoyau fini”. **Kind:** own idea. **Context:** Hua, modernised reading of cote 29, “La normalité n'est pas une commodité”, “L'énoncé”, their p.161; no exact matching RESULTS_STATE theorem (LM1 E.11 concerns a different group-scheme problem). **Search:** Q01.

**Own-idea confidence and reason:** High for the conditional finite-index argument and cokernel correction: the relevant subgroup maps and component requirement are explicit.

Hua correctly identifies finite index of the image as the stronger conclusion supplied by the argument, but his footnote's assertion that a nonnormal image has no cokernel is false: the categorical cokernel is the quotient by its closed normal closure. For normal connected locally noetherian $Y$, a closed point of the nonempty generic fibre of a dominant finite-type $X\to Y$ gives a finite extension $L/K$, whose absolute Galois group has finite-index image in $G_K$; generic-point surjectivity then makes the image in $\pi_1(Y)$ finite index, without using properness beyond finite type [S01]. This argument concerns a connected component of $X$ that dominates $Y$; if connectedness is not implicit, a base point on the extra vertical component of $Y\amalg\operatorname{Spec}k\to Y$ shows why it must be specified.

### IC02 — The node requires a rational projective model, and gives two different groups

**Scan:** 162. **Quote:** “courbe int. ... avec pt double ordinaire”; $\pi_1(Y)=\widehat{\mathbb Z}$. **Kind:** own idea / reading question. **Context:** Hua, modernised reading of cote 29, “Le contre-exemple”, their p.161; no exact RESULTS_STATE theorem. **Search:** Q02.

**Own-idea confidence and reason:** High for the projective rational single-node model and finite-versus-infinite cover distinction; no new visual confidence is assigned to the frozen uncertain phrase.

Hua's choice of a projective rational curve with exactly one ordinary node makes the normalization $\mathbb P^1$, whereas an arbitrary integral nodal curve in the frozen wording need not have simply connected normalization. In this precise model, finite étale covers are finite sets with a permutation gluing the two branches, so the ordinary étale fundamental group is the full $\widehat{\mathbb Z}$, including its $p$-part in characteristic $p$; infinite chain gluing instead supplies a principal discrete-$\mathbb Z$ cover and must not be confused with that profinite group. Hua's reported reading about removing a $p$-component differs from the frozen uncertain phrase “prouvé ... par ... comparaison”: this is a reading question only, with no change to the frozen text.

### IC03 — The unfinished pushforward question survives on the next page

**Scans:** 162–163. **Quote:** “je crois que ... peut alors ... construire les $f_*(X_1)$”. **Kind:** self-flagged: a step he himself marks as unverified. **Context:** Hua, modernised reading of cote 29, end of “Le contre-exemple”, their pp.161–162; no matching RESULTS_STATE claim. **Search:** Q03.

Contrary to Hua's statement that their p.162 contains only a diagram, scan163 completes a live expectation about $f_*(X_1)$ for étale $X_1/X$ under universal openness. The preceding fibre count for $\underline{\mathrm{Hom}}_Y(X,Y\amalg Y)$ rules out a finite étale representing object of constant degree in the nodal example, but should not be promoted without further argument to nonrepresentability in every category of schemes or algebraic spaces. Full faithfulness of étale descent under universally open surjections is a different statement from existence of the proposed pushforward; Stacks §41.20 makes this distinction useful [S02].

### IC04 — Normal target alone does not give universal openness

**Scan:** 162. **Quote:** “universellement ouvert [p. ex. $Y$ normale]”. **Kind:** own idea. **Context:** Hua, modernised reading of cote 29, “La normalité n'est pas une commodité”, their pp.161–162; the bracket is not discussed there; no matching RESULTS_STATE theorem. **Search:** Q04.

**Own-idea confidence and reason:** High: the explicit blow-up chart image D(xy) union the origin is checked directly; the refutation is conditional on the bracket having no extra implicit hypothesis.

If the bracket claims that the previously stated proper dominant morphism is universally open merely because $Y$ is normal, an additional hypothesis is missing. For $f:\operatorname{Bl}_0\mathbb A^2_k\to\mathbb A^2_k$, the chart $y=xt$ has the open subset (D(t)), whose image is $D(xy)\cup\{(0,0)\}$, not open. Thus even openness fails for this proper dominant morphism with smooth target; the frozen bracket should be retained and annotated as conditional, rather than silently repaired.

### IC05 — Left exactness does not require a finite structural group

**Scans:** 165–166. **Quote:** “exact à gauche”; “une telle section ... est unique”. **Kind:** own idea. **Context:** Hua, modernised reading of cote 29, “Le foncteur” and “α) Le foncteur est exact à gauche”, their pp.164–165; thematic relation to Hua register **29-fundamental-group-scheme-via-torsors**, but the coefficients here are arbitrary constant discrete groups, not finite group schemes. **Search:** Q05.

**Own-idea confidence and reason:** High: the finite-limit step follows from the displayed orbit calculation and descent of a group-stable clopen subset.

For a connected base, a pointed isomorphism between torsors is unique because its equalizer with another such isomorphism is group-stable and clopen, and descends to a clopen subset of the base containing the marked point. For two homomorphisms $h_1,h_2:G'\rightrightarrows G''$, the difference map on a $G'$-torsor has a $G'$-stable union of clopen fibres corresponding to the orbit of the identity in $G''$; its image on the connected base is all or nothing, and the marked point selects all. The equalizer therefore is a torsor under $\operatorname{Eq}(h_1,h_2)$, establishing the nontrivial finite-limit step without finiteness of $G'$ or $G''$.

### IC06 — Filtered intersections: two different hypotheses, one direct proof

**Scans:** 167–168, 170. **Quote:** “$S$ loc. noeth ou $\pi$ artinien”; “l'intersection ... $P'$ ... fibré principal homogène sous $\pi'$”. **Kind:** own idea. **Context:** Hua, modernised reading of cote 29, “d) La filtration décroissante” and “L'intersection porte un fibré”, their pp.166–169; relation to Hua **29-fundamental-group-scheme-via-torsors** is methodological only. **Search:** Q06.

**Own-idea confidence and reason:** High: the component saturation and nonempty fibre-intersection arguments are given in full below, with the DCC case separate.

For a group with the descending chain condition on subgroups, the cofiltered family of allowed reductions has a minimal member, so the intersection already is one reduction. For locally noetherian $S$, the torsor $P$ is locally connected: if $Q$ is its marked connected component, its saturation $\bigcup_{g\in\pi}gQ=p^{-1}(p(Q))$ is clopen, so the open surjection $p$ makes (p(Q)) clopen and hence equal to connected $S$. Every pointed reduction contains $Q$, and their intersection is a union of open components with nonempty fibres, each a torsor under the intersection of the subgroups. This proves the live claim without a limit-of-preschemes construction or a constructibility assertion for a non-quasi-compact component.

### IC07 — Cancelled spreading-out and the omitted local-noetherian conclusion

**Scans:** 168, 170. **Quote:** cancelled passage beginning “La question est locale”; live “ou si ... n'importe quelle catégorie ... mais $S$ étant loc. noeth”. **Kind:** withdrawn in the same text: cancelled spreading-out on scan168; live replacement on scans168 and170. **Context:** Hua, modernised reading of cote 29, “L'intersection porte un fibré” and “La conséquence”, their pp.167,169; Hua **29-fundamental-group-scheme-via-torsors**. **Search:** Q07.

Hua uses the spreading-out passage at the top of scan168 as a live reduction, although that passage is cancelled in the frozen transcription. His stated consequence also retains only structural groups satisfying the descending chain condition and drops the separate conclusion for any subgroup-and-finite-product-stable group category when $S$ is locally noetherian. The independently checked component argument in IC06 supports this second branch, but no claim is made here to have independently reconstructed the full strict pro-representability theorem or its size conventions.

### IC08 — A structural torsor is a reduction inside the isomorphism sheaf

**Scan:** 169. **Quote:** “sous-fibré ... principal” inside $\operatorname{Isom}_S(E_S,T)$. **Kind:** own idea / reading question. **Context:** Hua, modernised reading of cote 29, “L'application : ce que le groupe élargi classe”, their p.168; link to Hua **29-fundamental-group-scheme-via-torsors** only through torsor methods. **Search:** Q08.

**Own-idea confidence and reason:** High for the counterexample: the structural group has three elements and the full isomorphism group has six.

The frozen passage specifies a principal structural sub-torsor inside the isomorphism sheaf, whereas Hua replaces this by the assertion that the whole isomorphism sheaf is itself a principal $\pi$-torsor. These differ already for the constant three-element cover with the faithful cyclic action $C_3\subset S_3$: the isomorphism sheaf has six elements per fibre, while the chosen structural torsor has three. The manuscript's reduction-of-structure-group data must therefore be retained in the modern formulation.

### IC09 — Twisted constant groups are not the same as torsion-free groups

**Scan:** 169. **Quote:** “Schémas en groupes comm., constants tordus”; modules “de type fini”. **Kind:** own idea / reading question. **Context:** Hua, modernised reading of cote 29, “L'application : ce que le groupe élargi classe”, their p.168; no matching RESULTS_STATE theorem, and LM1 E.11 is not settled by this class of étale group schemes. **Search:** Q09.

**Own-idea confidence and reason:** High for the finite-module and matrix examples: torsion, the eigenvalue, and compact-to-discrete finite-image obstruction are explicit.

Hua's phrase “sans torsion” does not match the frozen “constants tordus”, and it would exclude the constant group $\mathbb Z/2$, although finitely generated $\mathbb Z$-modules in the stated correspondence include that example. Nor does an infinite underlying set alone place a local system beyond the ordinary profinite fundamental group: finite-image actions on $\mathbb Z^r$, such as a sign action on $\mathbb Z$, are already continuous actions of a profinite group. A genuinely additional example comes from the rational node of IC02 by gluing $\mathbb Z^2$ with $A=\left(\begin{smallmatrix}2&1\\1&1\end{smallmatrix}\right)$; its monodromy has infinite order and cannot be a continuous image of a compact profinite group in discrete $\mathrm{GL}_2(\mathbb Z)$.

### IC10 — Progroup, its pro-discrete completion, and the fuller pro-étale group

**Scans:** 169–170. **Quote:** deleted “continues”; “ne peut plus être interprété comme un simple groupe topologique”. **Kind:** own idea / reading question. **Context:** Hua, modernised reading of cote 29, “L'application : ce que le groupe élargi classe”, their pp.168–169; related to Hua **29-fundamental-group-scheme-via-torsors**, but a different coefficient category. **Search:** Q10.

**Own-idea confidence and reason:** High for the qualified modern comparison: the exact primary-source lemmas and base hypotheses were read; this is not an independent construction of the pro-etale group.

Hua reinstates continuity in the formulation and says the manuscript does not discuss the topology, although the frozen deletion and margin explicitly warn about it. Under Bhatt–Scholze's hypotheses in §7.4, their Lemma7.4.6 identifies homomorphisms from the pro-étale group to discrete groups with discrete-group torsors and relates the pro-discrete completion to Grothendieck's progroup; Lemma7.4.5 singles out actions on which some open subgroup acts trivially on the whole set [S03]. This supports a qualified modern comparison, not an unqualified identification of the manuscript's pro-object with the full pro-étale group on every scheme: Example7.4.9 exhibits further information visible to the latter. The authors' standing hypothesis there is connected, locally topologically noetherian $X$, with the extension stated in Remark7.4.12, not an unrestricted “schéma quelconque”.

### IC11 — The five classes: keep the piecewise-finite reading visible

**Scan:** 171. **Quote:** $C_4$: “finis par morceaux”; $C_5$: “finis étales p. morceaux”. **Kind:** reading question. **Context:** Hua, modernised reading of cote 29, “Les cinq classes de recouvrements”, their p.170; Hua, findings register, **29-h1-five-classes-infinite-group**. **Search:** Q11.

Both Hua's section and its register summarize $C_4,C_5$ as finite principal and finite étale principal, while the frozen transcription gives piecewise finite and piecewise finite étale. These are materially different definitions, so the register's summary must not be used to replace the frozen wording or to identify the classes without an explicit interpretation. In the comparisons below, assertions about $C_1,C_2,C_3$ use only their displayed definitions; statements involving $C_4,C_5$ are conditional on their including globally finite étale trivializing covers.

### IC12 — Why the finite-group argument is specifically affine descent

**Scan:** 171. **Quote:** “Si $G$ est fini, tous ces homomorphismes sont bijectifs”; “Notre intérêt ici est dans le cas $G$ infini”. **Kind:** own idea. **Context:** Hua, modernised reading of cote 29, “Pourquoi cela n'a d'intérêt que pour $G$ infini”, their p.170; Hua **29-h1-five-classes-infinite-group**. **Search:** Q12.

**Own-idea confidence and reason:** High for the finite-group application of the cited affine descent theorem; the lack of quasi-compactness identifies exactly why that argument does not cover infinite G.

For finite $G$, a Čech cocycle on an fpqc cover is a descent datum on the finite affine scheme $G_T$; effective descent of affine schemes gives a finite étale $G$-torsor, which is itself a finite étale trivializing cover [S04]. This checks Hua's argument and the comparison for every displayed class containing finite étale covers. For infinite $G$ and a nonempty affine $T$, $G_T=\coprod_G T$ is not quasi-compact and hence is not affine, so this particular proof stops there; effectiveness for infinite $G$ requires the distinct theorem used in IC14.

### IC13 — Quasi-finite refinements and the finite-presentation issue

**Scan:** 171. **Quote:** “$C_2$ ... de type fini”; $H^1_{C_3}\simeq H^1_{C_2}$. **Kind:** unproved claim / own idea. **Context:** Hua, modernised reading of cote 29, “Les comparaisons”, their p.170; Hua **29-h1-five-classes-infinite-group**. **Search:** Q13.

**Own-idea confidence and reason:** High for the modern fppf refinement statement in its stated scope; the manuscript finite-type formulation on unrestricted preschemes is not established by refinement alone.

The page asserts this comparison without a proof, and Hua repeats it. The standard modern refinement theorem makes every fppf cover refinable by an fppf cover with locally quasi-finite maps [S05], which proves the expected comparison with the usual local finite-presentation conventions and suitable quasi-compactness. Since the manuscript says finite type and allows general preschemes, it would be inaccurate simply to replace that hypothesis by finite presentation; they coincide over locally noetherian bases, while IC14 gives a different route for affine bases without that substitution.

### IC14 — Modern effective descent supplies the infinite-group comparison on affine bases

**Scans:** 171–172. **Quote:** marginal “élucider ici les questions d'effectivité des données de descente”. **Kind:** self-flagged: a step he himself marks as unverified / own idea. **Context:** Hua, modernised reading of cote 29, “Les cinq classes de recouvrements” and “Les comparaisons”, their pp.170–171; Hua **29-h1-five-classes-infinite-group**. **Search:** Q14.

**Own-idea confidence and reason:** High for the application to ordinary constant-group Cech torsors on affine or qcqs bases; arbitrary non-quasi-separated and nonstandard pi0 conventions are left open.

Gabber's effective fpqc descent theorem for ind-quasi-affine schemes applies to $G_T\to T$ for arbitrary discrete $G$, since separated locally quasi-finite morphisms are ind-quasi-affine [S06,S07]. The descended scheme is étale by fpqc descent of that property, and the action and torsor isomorphism descend, yielding a genuine $G$-torsor [S08]. If $S$ is affine (or quasi-compact and quasi-separated), finitely many affine étale trivializing pieces give a surjective quasi-compact quasi-finite finite-presentation cover, so $H^1_{C_1}(S,G)=H^1_{C_2}(S,G)=H^1_{C_3}(S,G)$ under the displayed Čech-cover definitions. This is a modern deduction with a stronger descent input, not the finite-group affine argument, not a proof from the manuscript, and not a resolution here of arbitrary non-quasi-separated base conventions or of $C_4,C_5$.

### IC15 — Dedekind comparison is supported in a larger verified modern scope

**Scan:** 172. **Quote:** “spectre d'un anneau de Dedekind”; $H^1_{C_2}\xrightarrow{\sim}H^1_{C_1}$. **Kind:** unproved claim / own idea. **Context:** Hua, modernised reading of cote 29, “Les comparaisons”, their p.171; Hua **29-h1-five-classes-infinite-group**, inherited status “conjecture (unsearched)”. **Search:** Q15.

**Own-idea confidence and reason:** High for the Dedekind case as an affine instance of IC14, subject to the same ordinary Cech-torsor interpretation.

The frozen page supports the Dedekind comparison recorded by Hua, but neither the page nor his paragraph supplies its proof. IC14 checks it using modern effective descent for every affine base, hence in particular for spectra of Dedekind rings, without treating the inherited “unsearched” status as settled evidence either way. This changes the research lead from an unsupported potentially-new assertion into an identified consequence of a cited general theorem within that verified scope.

### IC16 — Completion is a covering of a potentially noncomplete DVR

**Scan:** 172. **Quote:** deleted “local complet”, inserted “de valuation”; $H^1_{C_i}(S)\simeq H^1(\widehat V/V,-)$, $i=1,2,3$. **Kind:** own idea / reading question. **Context:** Hua, modernised reading of cote 29, “Les comparaisons”, their p.171; Hua **29-h1-five-classes-infinite-group**. **Search:** Q16.

**Own-idea confidence and reason:** High: the explicit double-cover calculation and the strictly henselian trivialization argument are checked; the frozen cancellation is not reinterpreted visually.

Hua restores completeness to the DVR hypothesis, although the frozen page removes it, and then the extension $\widehat V/V$ would be the identity. For $V=\mathbb C[t]_{(t)}$, the connected finite étale double cover $u^2=1+t$ becomes trivial over $\widehat V=\mathbb C[[t]]$, demonstrating a nontrivial class represented by the completion Čech cocycle. More generally the completion of a DVR with algebraically closed residue field is strictly henselian, so every étale discrete-group torsor over it has a section; combined with IC14 and faithfully flat completion, this proves the displayed comparison for the usual torsor interpretation. It does not reintroduce completeness into $V$.

### IC17 — The complete-local comparison follows from a henselian finite-image argument

**Scan:** 172. **Quote:** “anneau local complet”; $H^1_{C_i}(V,-)\simeq H^1_{C_i}(k,-)$, $i=2,3,4,5$. **Kind:** unproved claim / own idea. **Context:** Hua, modernised reading of cote 29, “Les comparaisons”, their p.171; Hua **29-h1-five-classes-infinite-group**. **Search:** Q17.

**Own-idea confidence and reason:** High for the henselian torsor-class comparison using the cited finite etale and section theorems; the C4/C5 reading caveat is retained.

For a henselian local ring $V$, choose a point over the closed point in a discrete-group étale torsor, lift its finite separable residue extension to a finite étale local extension of $V$, and use the henselian section property to trivialize the torsor after that extension [S09,S10]. A further finite Galois cover therefore trivializes it, reducing classification to a finite-image homomorphism $G_k\to G$ up to conjugacy, and the finite étale equivalence for $V\to k$ identifies these classes. This proves the asserted complete-local comparison under the usual completeness/henselian convention and shows why infinite $G$ still has finite monodromy here; combined with IC14 it also handles $C_1$ in this affine setting. The claimed equalities involving $C_4,C_5$ remain tied to the reading/definition caveat in IC11, rather than silently adopting Hua's “principal” wording.

## Targeted checks actually performed

These are mathematical arguments carried out during this research pass. They do not assert that the cited general literature theorems have been independently re-proved.

1. **IC01, generic point.** With $Y$ connected normal locally noetherian, it is integral. A closed point of $X_K$ has residue field finite over $K$; its maximal separable subextension gives an open subgroup of $G_K$, while a purely inseparable extension does not change the absolute Galois group. The composite into $\pi_1(Y)$ lies in the image from the relevant connected component of $X$, and the generic-point map is surjective [S01]. Its image is consequently finite index. The categorical cokernel is instead the quotient by the closed normal closure, so Hua's nonexistence claim is incorrect even when the image is not normal.

2. **IC02, rational node.** Pull a finite étale cover back to the normalization $\mathbb P^1_k$; it is a disjoint union of copies of $\mathbb P^1_k$. Descent at the single node pairs the two finite fibres by a bijection, i.e. one permutation; a connected cover corresponds to one cycle. The $n$-cycle is the necklace of $n$ rational components and works in every characteristic, while the analogous doubly infinite chain has deck group $\mathbb Z$. This checks the distinction between finite-cover $\widehat{\mathbb Z}$ and the discrete monodromy of the infinite torsor; no general identification of fundamental groups on arbitrary singular curves is inferred.

3. **IC04, blow-up.** In the affine blow-up chart $\operatorname{Spec}k[x,t]$, $f(x,t)=(x,xt)$. On (D(t)), the image with $x\ne0$ is exactly (D(y)), and with $x=0$ it is the origin. Its intersection with the closed $x$-axis is just the origin, which is not an open subset of the axis. Thus the displayed image is not open.

4. **IC05, finite limits.** For two maps on induced pointed torsors, choose an étale trivialization and express their difference as a locally constant map $\delta:P'\to G''$, with $\delta(pg)=h_1(g)^{-1}\delta(p)h_2(g)$ after one consistent left/right convention. The orbit of $1\in G''$ under this twisted action has clopen inverse image because both it and its complement are unions of fibres of a map to a discrete scheme. That inverse image is $G'$-stable, descends to a clopen subset of $S$, and contains the marked point. Thus it is all of $P'$; the fibrewise set where $\delta=1$ is nonempty and simply transitive under $\operatorname{Eq}(h_1,h_2)$. Products and the pointed uniqueness step follow directly from the same local torsor description.

5. **IC06, arbitrary filtered intersection under local noetherianness.** A connected component $Q\subset P$ is open and closed. Fibrewise transitivity of the global constant group action gives $p^{-1}(p(Q))=\bigcup_g gQ$; this and its complement are unions of open components. An open surjection is a quotient map, so (p(Q)) is clopen and hence all $S$. Each clopen pointed reduction is a union of components containing $Q$; their intersection is again a union of components, is clopen, and has a point over every geometric point. Choosing any such point identifies the intersection of the reduction fibres with a torsor under $\bigcap_i G_i$, and the torsor identity is an isomorphism of étale schemes because it is so on all geometric fibres. For the DCC case, choose a minimal group in the cofiltered family; intersecting it with any other group proves that it lies in all of them.

6. **IC08–IC09, elementary tests.** The structural $C_3$-subtorsor inside $S_3$ has three rather than six elements, refuting replacement by the entire isomorphism torsor. The constant finitely generated group $\mathbb Z/2$ refutes the “torsion-free” substitution. The matrix $A$ above has characteristic polynomial $z^2-3z+1$ and real eigenvalue $(3+\sqrt5)/2>1$, so it has infinite order. Any continuous image of a compact profinite group in a discrete group is finite, which distinguishes this nodal gluing example from finite-image actions on an infinite module.

7. **IC12–IC15, descent and cover extraction.** Finite $G_T$ is affine and finite étale, so the affine descent theorem [S04] applies. For arbitrary $G$, use the separate ind-quasi-affine descent theorem [S06], its locally-quasi-finite criterion [S07], and fpqc descent of étaleness [S08]; the action and its torsor isomorphism descend by faithful descent of morphisms. Over affine $S$, cover the descended $P$ by affine opens and choose finitely many whose images cover $S$, which is possible since $P\to S$ is open and $S$ is quasi-compact. Their finite disjoint union $T\to S$ is étale, quasi-compact, quasi-finite and of finite presentation, and $T\to P$ supplies the desired trivialization. The same reasoning applies over quasi-compact quasi-separated $S$; a claim for arbitrary non-quasi-separated preschemes is deliberately not made. This argument concerns the standard Čech cocycles valued in the constant group scheme; a nonstandard interpretation of functions on $\pi_0(K_{T/S})$ on non-locally-connected spaces would require its own convention check.

8. **IC16, a nontrivial completion cocycle.** In $V=\mathbb C[t]_{(t)}$, (1+t) is a unit, so $V[u]/(u^2-(1+t))$ is finite étale: (2u) is invertible. It is a domain because (1+t) is not a square in $\mathbb C(t)$, as its valuation at $t=-1$ is one; thus its $\mathbb Z/2$-torsor is nontrivial. The binomial power series for $\sqrt{1+t}$ lies in $\mathbb C[[t]]$, so the two roots split the completed cover. Completion of a DVR is faithfully flat; the strictly henselian target trivializes arbitrary étale discrete-group torsors by [S10], and descent then identifies the entire class set with the completion Čech classes in the scope of IC14.

9. **IC17, henselian local rings.** A point in the closed fibre of an étale torsor has a finite separable residue field extension. Lift a finite Galois extension containing it by [S09] to a connected finite étale local cover $V'\to V$, which remains henselian. The pulled-back torsor has a rational closed-fibre point; an affine étale neighbourhood of it admits a section by [S10]. Its descent cocycle for the finite Galois cover takes values in $G$, hence describes a finite-image homomorphism. The equivalence of finite étale covers of $V$ and $k$ identifies all these cocycles and conjugacies, establishing the claimed bijection for torsor classes.

## Primary sources consulted

Links name the primary source and exact result. Root should retrieve these URLs in its own tool context before using web-reference tokens in a user-facing citation. The application arguments above are this agent's checks; the source theorems are used as background.

- **S01.** Stacks Project, §58.11, “Fundamental groups of normal schemes”, [tag0BQJ](https://stacks.math.columbia.edu/tag/0BQJ). Generic-point surjectivity.
- **S02.** Stacks Project, §41.20, “Descending étale morphisms”, [tag0BTH](https://stacks.math.columbia.edu/tag/0BTH). Fully faithful descent versus effective descent; distinguish its cited fppf statement [tag02W8](https://stacks.math.columbia.edu/tag/02W8) from arbitrary fpqc effectiveness.
- **S03.** Bhargav Bhatt and Peter Scholze, *The pro-étale topology for schemes*, §7.4, Lemmas7.4.5–7.4.6, Example7.4.9 and Remark7.4.12, printed pp.69–71, [author-hosted PDF](https://www.math.uni-bonn.de/people/scholze/proetale.pdf). This draft's summary of this source is confined to IC10.
- **S04.** Stacks Project, §35.37, Lemma35.37.1, “Descending affine morphisms”, [tag0244](https://stacks.math.columbia.edu/tag/0244).
- **S05.** Stacks Project, Lemma37.23.6, locally quasi-finite refinements of fppf covers, [tag0572](https://stacks.math.columbia.edu/tag/0572).
- **S06.** Stacks Project, Lemma40.15.3 (Gabber), effective fpqc descent of ind-quasi-affine schemes, [tag0APK](https://stacks.math.columbia.edu/tag/0APK). The actual lemma and proof were opened; the proof was not independently re-proved here.
- **S07.** Stacks Project, Lemma37.66.8, separated locally quasi-finite morphisms are ind-quasi-affine, [tag0AP9](https://stacks.math.columbia.edu/tag/0AP9).
- **S08.** Stacks Project, Lemma35.23.31, étaleness is fpqc local on the base, [tag02VN](https://stacks.math.columbia.edu/tag/02VN).
- **S09.** Stacks Project, Lemma10.153.7, finite étale equivalence over a henselian local ring and its residue field, [tag04GK](https://stacks.math.columbia.edu/tag/04GK).
- **S10.** Stacks Project, Lemma10.153.3, equivalences (7) and (8), henselian lifting of a rational point of an étale algebra to a section, [tag04GG](https://stacks.math.columbia.edu/tag/04GG).

## Check-event suggestions

The companion `infinite_coverings_check_events.tsv` has the same five-column header as the currently empty package `CHECK_EVENTS.tsv`. It records only actual mathematical checking in this pass, with refined local statement IDs; it does not convert textual comparison into proof or assign these claims a project-wide intake verdict. It is a draft for root review, not an edit to the main check log. General source theorems are marked as background, not as independently re-proved.

## Actual per-note context searches

The appendix below is generated from actual `rg -n -i -e QUERY context` invocations. All matching lines for each listed query are retained, including zero matches if any. These are searches of the supplied four-file context only; a negative hit does not establish absence from the mathematical literature. Queries Q02 and Q14 were narrowed after the initial broad searches to avoid copying unrelated context.

### Q01 — IC01

Query (regular expression): `conoyau|indice fini|LM1 E\.11`

```text
context/notes/RESULTS_STATE.md:15:- **Our open questions they may bear on:** the one matched row, **LM1 E.11** (the source theorem for arbitrary separated locally finitely presented group schemes), came through the tag; it bears only on general group schemes. They may open up instead: ramified coverings, the fundamental group scheme, torsors under discrete groups.
context/notes/RESULTS_STATE.md:347:- **LM1 E.11** [Open (the return's claim)] The full source theorem for arbitrary separated locally finitely presented group schemes, and the Q-algebra statement without linearity, remain unproved here. Where: 50.1--2; 650bis verso--655 verso; 140-4:6,10--16. (LM1_GROUP_SCHEMES_results.csv)
context/hua_project/29.modern.tex:1395:le conoyau sont tués par une puissance de $\mathcal{J}$. Cet ensemble admet un
context/hua_project/29.modern.tex:4113:est d'indice fini.\footnote{La page écrit « a un conoyau fini ». Pour un
context/hua_project/29.modern.tex:4115:n'y a pas de conoyau ; ce que l'énoncé veut dire, et ce que la démonstration
context/hua_project/29.modern.tex:4116:donne, est que l'image est d'\emph{indice fini}. C'est la formulation retenue
context/hua_project/29.modern.tex:4139:L'image est triviale dans un groupe infini : elle n'est pas d'indice fini.
```

### Q02 — IC02

Query (regular expression): `courbe rationnelle sur|groupe fondamental est donc|privé de sa.*composante|restriction au premier`

```text
context/hua_project/29.modern.tex:4129:Prenons pour $Y$ une courbe rationnelle sur $k$ algébriquement clos ayant un
context/hua_project/29.modern.tex:4147:\emph{pour tout $n$}. Le groupe fondamental est donc $\hat{\mathbb{Z}}$ tout
context/hua_project/29.modern.tex:4149:privé de sa $p$-composante », ces derniers mots étant une lecture que la
context/hua_project/29.modern.tex:4154:restriction au premier à $p$ est celle qui s'impose pour les revêtements
```

### Q03 — IC03

Query (regular expression): `La page 162 ne porte|on ne peut pas former|f_\{\*\}`

```text
context/hua_project/29.modern.tex:1540:\subsection*{Lemme 2 : constructibilité de $f_{*}$}
context/hua_project/29.modern.tex:1544:$f_{*}(F)$ est constructible.
context/hua_project/29.modern.tex:1547:moderne correspondant, la constructibilité de $R f_{*}$ pour $f$ de type
context/hua_project/29.modern.tex:1869:\pi_1(X_1) \arrow[d, "f_{*}"'] & \pi_1(U_1) \arrow[l] & \\
context/hua_project/29.modern.tex:1905:\emph{C'est un monomorphisme} parce que $f_{*}(\mathcal{O}_{X}) =
context/hua_project/29.modern.tex:3000:$f_{*}$ ; alors $f'$ et $\varphi$ sont déterminés sans ambiguïté par $f$, et
context/hua_project/29.modern.tex:3001:leur existence signifie seulement que $f_{*}$ passe aux quotients.
context/hua_project/29.modern.tex:3333:absolument connexes (c'est-à-dire $f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{Y}$),
context/hua_project/29.modern.tex:3451:$f_{*}(\mathcal{O}_{X}) = \mathcal{O}_{S}$ \emph{universellement}. Soit $G$ un
context/hua_project/29.modern.tex:4162:dans ce cas, on ne peut pas former $\underline{\mathrm{Hom}}_{Y}(X, Y \sqcup
context/hua_project/29.modern.tex:4167:La page 162 ne porte qu'un carré encadré, $f_{*}(X_{1})$ au-dessus de
```

### Q04 — IC04

Query (regular expression): `universellement ouvert|La normalité n'est pas une commodité|normal.*connexe`

```text
context/hua_project/29.modern.tex:1811:est normal, $X'$ est normal, donc connexe implique irréductible ; par le lemme,
context/hua_project/29.modern.tex:2014:$S$, $\bar{X}$ normal sur $S$, à fibres connexes. On peut alors supposer $X$ et
context/hua_project/29.modern.tex:4104:\section*{La normalité n'est pas une commodité (pages 161 et 162)}
context/hua_project/29.modern.tex:4108:Soit $f : X \to Y$ un morphisme propre dominant, $Y$ \emph{normal} connexe et
```

### Q05 — IC05

Query (regular expression): `Le foncteur est exact à gauche|une telle section|en va de même des images|29-fundamental-group-scheme-via-torsors`

```text
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:374:- **29-fundamental-group-scheme-via-torsors** (cote 29, their pp. 124–129, 136–142; our scans 141, 142, 143) [literature: Killed. The published literature already credit…] The fundamental group scheme — the pro-object classifying pointed torsors under finite group schemes, infinitesimal part included — is obtained by strict pro-representability of the pointed-torsor functor alone, with no Tannakian input, and computed on an abelian variety as lim← ₙX, Cartier-dual to the ind-algebraic lim→ ₙX*. Our intake: new to us: our package for this cote is waiting
context/hua_project/29.modern.tex:4189:\subsection*{$\alpha$) Le foncteur est exact à gauche}
context/hua_project/29.modern.tex:4203:$\xi'_{i}$ ; et une telle section, si elle existe, est unique}. Réduire le
context/hua_project/29.modern.tex:4207:$\pi \to \pi' \rightrightarrows \pi''$ est exacte, il en va de même des images.
```

### Q06 — IC06

Query (regular expression): `noethérien, ou bien|L'intersection porte un fibré|composante connexe de|système filtrant décroissant`

```text
context/hua_project/29.modern.tex:1132:strict $S'$ d'un point de $S$, soit $Z'_{0}$ une composante connexe de
context/hua_project/29.modern.tex:3240:une composante connexe de $Q_{\mathrm{r\acute{e}d}}$.
context/hua_project/29.modern.tex:4119:composante connexe de $X'$.
context/hua_project/29.modern.tex:4221:noethérien, ou bien $\pi$ artinien} (condition de chaîne descendante).
context/hua_project/29.modern.tex:4234:système filtrant décroissant} $(\pi_{i})$, avec des $P_{i} \subset P$
context/hua_project/29.modern.tex:4240:\subsection*{L'intersection porte un fibré}
context/hua_project/29.modern.tex:4246:composante connexe de $\xi$ dans $P$ : elle est ouverte et fermée, $P$ étant
context/hua_project/29.modern.tex:5553:une par composante connexe de l'objet final : elle correspond donc non à un
```

### Q07 — IC07

Query (regular expression): `par étalement sur|catégorie de groupes artiniens|La conséquence|29-fundamental-group-scheme-via-torsors`

```text
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:374:- **29-fundamental-group-scheme-via-torsors** (cote 29, their pp. 124–129, 136–142; our scans 141, 142, 143) [literature: Killed. The published literature already credit…] The fundamental group scheme — the pro-object classifying pointed torsors under finite group schemes, infinitesimal part included — is obtained by strict pro-representability of the pointed-torsor functor alone, with no Tannakian input, and computed on an abelian variety as lim← ₙX, Cartier-dual to the ind-algebraic lim→ ₙX*. Our intake: new to us: our package for this cote is waiting
context/hua_project/29.modern.tex:3571:seconde est le fait géométrique, la première la conséquence dont on se sert.
context/hua_project/29.modern.tex:4244:La question est locale sur $S$, et par étalement sur un $S^{(0)}$ de type fini
context/hua_project/29.modern.tex:4260:\subsection*{La conséquence}
context/hua_project/29.modern.tex:4262:\textbf{Conséquence.} Si $\pi$ varie dans une catégorie de groupes artiniens
```

### Q08 — IC08

Query (regular expression): `Une relation étale est dite|isomorphismes.*Isom|est un revêtement`

```text
context/hua_project/29.modern.tex:3853:  \item[(iii)] $X$ est isomorphe à un $P/H$, où $P$ est un revêtement étale
context/hua_project/29.modern.tex:3880:Donc $P \to Y$ est un revêtement étale galoisien de groupe
context/hua_project/29.modern.tex:4146:branches. C'est un revêtement galoisien de groupe $\mathbb{Z}/n$, et il existe
context/hua_project/29.modern.tex:4273:Une relation étale est dite \emph{à groupe structural $\pi$} si le schéma des
context/hua_project/29.modern.tex:4274:isomorphismes $\underline{\mathrm{Isom}}_{S}(E_{S}, T)$ est un revêtement
```

### Q09 — IC09

Query (regular expression): `commutatifs sans torsion|pas un ensemble fini|LM1 E\.11`

```text
context/notes/RESULTS_STATE.md:15:- **Our open questions they may bear on:** the one matched row, **LM1 E.11** (the source theorem for arbitrary separated locally finitely presented group schemes), came through the tag; it bears only on general group schemes. They may open up instead: ramified coverings, the fundamental group scheme, torsors under discrete groups.
context/notes/RESULTS_STATE.md:347:- **LM1 E.11** [Open (the return's claim)] The full source theorem for arbitrary separated locally finitely presented group schemes, and the Q-algebra statement without linearity, remain unproved here. Where: 50.1--2; 650bis verso--655 verso; 140-4:6,10--16. (LM1_GROUP_SCHEMES_results.csv)
context/hua_project/29.modern.tex:4280:\textbf{Exemple.} Les schémas en groupes commutatifs sans torsion sur $S$, de
context/hua_project/29.modern.tex:4285:$\mathbb{Z}$-module de type fini n'est pas un ensemble fini, et le groupe
```

### Q10 — IC10

Query (regular expression): `pro-étale|construction topologique|continues de|discute pas la topologie`

```text
context/hua_project/29.modern.tex:4277:donner des opérations continues de $\tilde{\pi}_{1}(S, \xi)$ sur $F$},
context/hua_project/29.modern.tex:4290:fondamental élargi} dans SGA 3, et \emph{groupe fondamental pro-étale} dans le
context/hua_project/29.modern.tex:4291:travail de Bhatt et Scholze (2015), qui en donne la construction topologique
context/hua_project/29.modern.tex:4293:pro-représentabilité, et ne discute pas la topologie du pro-groupe obtenu.}
```

### Q11 — IC11

Query (regular expression): `finis principaux|finis étales principaux|29-h1-five-classes-infinite-group`

```text
context/hua_project/29.modern.tex:4314:  \item[$C_{4}$] les mêmes, finis principaux ;
context/hua_project/29.modern.tex:4315:  \item[$C_{5}$] les mêmes, finis étales principaux.
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:375:- **29-h1-five-classes-infinite-group** (cote 29, their pp. 170–171; our scans 171, 172) [conjecture (unsearched) | reach: beyond] For a discrete and possibly infinite group G, the classification of G-torsors is compared across five classes of covering families — fppf quasi-compact, finite type, quasi-finite, finite principal, finite étale principal — with H¹_{C₃} ≃ H¹_{C₂} in general, H¹_{C₂} ≃ H¹_{C₁} over a Dedekind ring, H¹_{C_i} ≃ H¹(V̂/V, −) for i = 1,2,3… Our intake: new to us: our package for this cote is waiting
```

### Q12 — IC12

Query (regular expression): `est alors fini, donc affine|descente fidèlement plate quasi-compacte des schémas affines|Pourquoi cela n'a d'intérêt`

```text
context/hua_project/29.modern.tex:4321:\subsection*{Pourquoi cela n'a d'intérêt que pour $G$ infini}
context/hua_project/29.modern.tex:4330:La raison est le théorème de descente : $G_{T}$ est alors fini, donc affine sur
context/hua_project/29.modern.tex:4331:$T$, et la descente fidèlement plate quasi-compacte des schémas affines est
```

### Q13 — IC13

Query (regular expression): `quasi-fini ou de|type fini, cela ne change|29-h1-five-classes-infinite-group`

```text
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:375:- **29-h1-five-classes-infinite-group** (cote 29, their pp. 170–171; our scans 171, 172) [conjecture (unsearched) | reach: beyond] For a discrete and possibly infinite group G, the classification of G-torsors is compared across five classes of covering families — fppf quasi-compact, finite type, quasi-finite, finite principal, finite étale principal — with H¹_{C₃} ≃ H¹_{C₂} in general, H¹_{C₂} ≃ H¹_{C₁} over a Dedekind ring, H¹_{C_i} ≃ H¹(V̂/V, −) for i = 1,2,3… Our intake: new to us: our package for this cote is waiting
context/hua_project/29.modern.tex:4340:  \item En général, $H^{1}_{C_{3}} \simeq H^{1}_{C_{2}}$ : quasi-fini ou de
context/hua_project/29.modern.tex:4341:    type fini, cela ne change rien.
```

### Q14 — IC14

Query (regular expression): `élucider|Les cinq classes de recouvrements|effectivité.*descente|29-h1-five-classes-infinite-group`

```text
context/hua_project/29.modern.tex:196:    fondamental, les cinq classes de recouvrements, la descente et son
context/hua_project/29.modern.tex:4296:\section*{Les cinq classes de recouvrements (pages 170 et 171)}
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:375:- **29-h1-five-classes-infinite-group** (cote 29, their pp. 170–171; our scans 171, 172) [conjecture (unsearched) | reach: beyond] For a discrete and possibly infinite group G, the classification of G-torsors is compared across five classes of covering families — fppf quasi-compact, finite type, quasi-finite, finite principal, finite étale principal — with H¹_{C₃} ≃ H¹_{C₂} in general, H¹_{C₂} ≃ H¹_{C₁} over a Dedekind ring, H¹_{C_i} ≃ H¹(V̂/V, −) for i = 1,2,3… Our intake: new to us: our package for this cote is waiting
```

### Q15 — IC15

Query (regular expression): `Dedekind|29-h1-five-classes-infinite-group`

```text
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:21:  2. On scans 171-172: the five classes, each comparison claimed, its hypotheses (the Dedekind case) and its proof.
context/notes/RESULTS_STATE.md:375:- **29-h1-five-classes-infinite-group** (cote 29, their pp. 170–171; our scans 171, 172) [conjecture (unsearched) | reach: beyond] For a discrete and possibly infinite group G, the classification of G-torsors is compared across five classes of covering families — fppf quasi-compact, finite type, quasi-finite, finite principal, finite étale principal — with H¹_{C₃} ≃ H¹_{C₂} in general, H¹_{C₂} ≃ H¹_{C₁} over a Dedekind ring, H¹_{C_i} ≃ H¹(V̂/V, −) for i = 1,2,3… Our intake: new to us: our package for this cote is waiting
context/hua_project/29.modern.tex:3417:Dedekind connexe comme limite projective des schémas en groupes finis et plats
context/hua_project/29.modern.tex:4342:  \item Si $S$ est le spectre d'un anneau de Dedekind,
```

### Q16 — IC16

Query (regular expression): `valuation discrète complet|une seule extension suffit|29-h1-five-classes-infinite-group`

```text
context/hua_project/29.modern.tex:4345:  \item Si $S$ est le spectre d'un anneau de valuation discrète complet à corps
context/hua_project/29.modern.tex:4347:    pour $i = 1, 2, 3$ : une seule extension suffit.
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:375:- **29-h1-five-classes-infinite-group** (cote 29, their pp. 170–171; our scans 171, 172) [conjecture (unsearched) | reach: beyond] For a discrete and possibly infinite group G, the classification of G-torsors is compared across five classes of covering families — fppf quasi-compact, finite type, quasi-finite, finite principal, finite étale principal — with H¹_{C₃} ≃ H¹_{C₂} in general, H¹_{C₂} ≃ H¹_{C₁} over a Dedekind ring, H¹_{C_i} ≃ H¹(V̂/V, −) for i = 1,2,3… Our intake: new to us: our package for this cote is waiting
```

### Q17 — IC17

Query (regular expression): `anneau local.*complet|groupe fondamental d'un anneau local complet|29-h1-five-classes-infinite-group`

```text
context/hua_project/29.modern.tex:3478:  \item[(iii)] si $A$ est un anneau local noethérien \emph{complet} sur $S$ de
context/hua_project/29.modern.tex:3493:que la fibre spéciale d'un anneau local complet, ce qui est la version
context/hua_project/29.modern.tex:4348:  \item Si $S$ est le spectre d'un anneau local \emph{complet} $V$ de corps
context/hua_project/29.modern.tex:4355:fondamental d'un anneau local complet est celui de son corps résiduel.
context/notes/RESULTS_STATE.md:18:- **Michel Hua's project (credit it to his project whenever you use it):** Hua, modernised reading of cote 29: coverings with ramification; a tame covering carries a structure, not only a property; the folder opens with Murre's doubts (writing SGA 1's tame exposé) and Grothendieck's reply listing five false statements; the 1967 "donnée de ramification" is an arbitrary catalogue giving the same category. Hua, findings register, **29-fundamental-group-scheme-via-torsors** (our scans 141-143; scans 125-130, 137-140 in 239_MPL_29_095-140): the fundamental group scheme by pro-representability of pointed torsors under finite group schemes, without Tannakian input, lim ₙX on an abelian variety; already credited in the literature, per his register. **29-h1-five-classes-infinite-group** (our scans 171-172; unsearched): G-torsors for a discrete G over five classes of covering families. Our intake: new to us.
context/notes/RESULTS_STATE.md:375:- **29-h1-five-classes-infinite-group** (cote 29, their pp. 170–171; our scans 171, 172) [conjecture (unsearched) | reach: beyond] For a discrete and possibly infinite group G, the classification of G-torsors is compared across five classes of covering families — fppf quasi-compact, finite type, quasi-finite, finite principal, finite étale principal — with H¹_{C₃} ≃ H¹_{C₂} in general, H¹_{C₂} ≃ H¹_{C₁} over a Dedekind ring, H¹_{C_i} ≃ H¹(V̂/V, −) for i = 1,2,3… Our intake: new to us: our package for this cote is waiting
```
