# Research contribution: real structures, Hodge comparison and Oda

Research only, after the transcription freeze at 2026-11-15 22:05:33 UTC. No manuscript images were read by this research worker, and no transcription, inventory, doubts or frozen-hash file was modified. All manuscript statements below refer to the root reader's frozen page files; uncertain macros remain uncertain.

## Sources and status

**N** = `context/same_cote_18/MPL_15_195-228+18_002-017_notes.md`; its observations and scan locators are unreviewed first-pass leads, not independently audited quotations. **CT** = `context/MPL_16+47+54+44_transcription.tex`, also first-pass evidence; **CN** = its companion notes. **RS** = `context/notes/RESULTS_STATE.md`, read before this contribution; its explicit referee statuses have not been extended to unrelated notes. Every RH item below states a context search and its result; the supporting CT search extracts are in `research_real_hodge_searches.md`.

### RH01 — Cycle normalization and the two literal discrepancies

**Kind:** reading question. **Witness:** 18/019:L12–19; 18/021, 023, 025. **Quote:** “dépend beaucoup de σ”. **Context search:** `Betti | Tate | Kummer | 2.*pi` → N A06 (15/199–201), N P09 (18/009), CT16/052; adds explicit pushforward and cycle-class factors. **RS:** MPL_15_195-228+18_002-017 A06, P09; first-pass leads.

Scan019 writes the factor \((\sigma(2i\pi))^{-p}\), then writes a single power in the lattice formula and a single minus sign after replacing \(\sigma\) by its conjugate. Direct conjugation of its first formula gives \((-1)^p\), while scans021–025 retain codimension-dependent powers in the Gysin/correspondence comparisons. These are reading or scope questions for the p=1 example and the surrounding general statement; neither discrepancy licenses a post-freeze change.

### RH02 — The orientation torsor explains the Tate sign

**Kind:** unpursued implication. **Witness:** 18/027, 029:L2–10. **Quote:** “une des racines de −1”. **Context search:** `Betti | Tate | involutif` → N A06 (15/199–201), P09 (18/009); adds the projective-line generator and its orientation. **RS:** MPL_15_195-228+18_002-017 A06, P09; LM7 C.1 retains its supplied “Known, return's claim” status.

The written map \(\alpha_\infty(u)=(2\sqrt{-1}\pi)^{-1}v\) identifies the generator after choosing one orientation of \(\mathbf P^1_K\). Changing that choice sends \(u\) to \(-u\), and the map gives the same rank-one lattice because \((-u)\mathbf Z=u\mathbf Z\). This concrete generator calculation supplies the sign used later for real Frobenius on the Tate line.

### RH03 — Fixed topology and transport of the Hodge splitting

**Kind:** unproved claim. **Witness:** 18/032:L9–16; 033:L2–4; 039:L4–28. **Quote:** “ne dépend pas de π”. **Context search:** `Hodge | splitt | bigrad | Betti` → N P10/P13 (18/011), P24 (18/013), CT54/003,005; adds a splitting constructed from a chosen archimedean topology. **RS:** MPL_15_195-228+18_002-017 P10, P13, A05; first-pass leads.

The assertion concerns the two topological identifications of an already topological field K with C, and the comparison on scan039 is explicitly labeled “non comm.” until coefficient conjugation is included. Its precise comparison map is the semilinear transport induced by \(c:K\to K\), together with the passage from X to its conjugate \(X^c\); the filtration and Betti real form determine the Hodge summands through their intersections in each pure degree. Scan041 subsequently varies the topology T itself, so the earlier independence assertion must retain its fixed-topology quantifier.

### RH04 — The commuting conjugations have a concrete fixed-space description

**Kind:** unpursued implication. **Witness:** 18/033:L6; 035:L7–9; 037:L11–20. **Quote:** “σ et τ commutent”. **Context search:** `conjugaison | frobenius | deux | vérifier` → N A07 (15/203:L9–17), A08 (15/203–205); adds the explicit geometric explanation and later cocycle. **RS:** MPL_15_195-228+18_002-017 A23; N A07/A08 are supplied context leads even where RS gives no individual row.

The new explanation identifies \(f_\infty\) with the Q-linear action of complex conjugation on Betti cohomology and writes \(\tau=f_\infty\sigma=\sigma f_\infty\). In the decomposition \(V=V^+\oplus V^-\), its real fixed space is \(V^+_{\mathbf R}\oplus iV^-_{\mathbf R}\), because \(\tau(x+iy)=fx-ify\). This supplies the calculation behind the earlier “à vérifier” lead, while the separate l-adic compatibility mentioned in N A08 still requires its realization comparison.

### RH05 — The normalizer formula and Hodge fullness are stated together

**Kind:** unproved claim. **Witness:** 18/034:L17–35; 037:L23–29. **Quote:** “pleinement fidèle en vertu des conj. de Hodge”. **Context search:** `frobenius | pleinement fidèle | Hodge | réellification` → N A20/A23 (15/213–215); restates their fullness claim and adds \(f_\infty j(\lambda)f_\infty^{-1}=j(\lambda')\). **RS:** MPL_15_195-228+18_002-017 A20, A23, M08; first-pass leads.

The page records both a rational involution and its conjugation action on the Hodge torus, including inversion on the norm-one subtorus. The proposed realization functor has target a Hodge structure equipped with this conjugate-Hodge isomorphism, and its asserted fullness is explicitly attributed to the Hodge conjectures. The normalizer equation alone does not provide the algebraic correspondences needed for that asserted fullness: it states the compatibility those correspondences must preserve.

### RH06 — The displayed natural isomorphism has a minus-minus tensor defect

**Kind:** own idea (explicit calculation). **Witness:** 18/035:L9–24. **Quote:** “n'est pas compatible avec le produit tensoriel”. **Context search:** `foncteur | Betti | tordu | tensor` → N A06/A23 (15/199–201,215), CT16/049; adds a complete calculation of the displayed map. **RS:** MPL_15_195-228+18_002-017 A06, A23. **Confidence:** high; reason: multiplication of the two explicit scalars gives the defect.

For \(W(V)=V^+\oplus iV^-\), the map \(a_V(v_++v_-)=v_++iv_-\) is a Q-linear isomorphism, and ambient multiplication gives the tensor comparison \(W(V)\otimes W(U)\to W(V\otimes U)\). For \(v\in V^-\) and \(u\in U^-\), that multiplication sends \(a_V(v)\otimes a_U(u)\) to \(-v\otimes u\), whereas \(a_{V\otimes U}(v\otimes u)=v\otimes u\). The calculation proves the particular map's failure and also shows why the subspace W itself remains closed under the required tensor construction.

### RH07 — The tentative tensor nonisomorphism is detected on an Artin line

**Kind:** own idea (explicit obstruction). **Witness:** 18/035:L26; 037:L20. **Quote:** “Il semble”. **Context search:** `tordu | cocycle | real | frobenius` → N A23 (15/215), CT16/049; adds an explicit obstruction on a tensor subcategory. **RS:** MPL_15_195-228+18_002-017 A23; WG2 §2.4 #3. **Confidence:** high; reason: the tensor relation yields an impossible rational square.

Let A be the sign Artin motive of C/R, with Betti basis a, \(a\otimes a\mapsto1\), and \(f_\infty(a)=-a\); then \(W(A)=i\mathbf Q a\), whose tensor square maps \((ia)\otimes(ia)\) to −1. Any tensor isomorphism between the two rational fibre functors on the Artin subcategory would send a to \(qia\), with \(q\in\mathbf Q^\times\), and preservation of \(A^{\otimes2}\simeq\mathbf1\) would give \(-q^2=1\), an impossibility. This proves the obstruction for the full real-motive category containing A; on the Tate subcategory the explicit maps \(e_n\mapsto i^n e_n\) on \(\mathbf Q(-n)\) preserve tensor products, so the manuscript's category scope matters.

### RH08 — The cohomology-of-real-points line needs its superscript resolved

**Kind:** reading question. **Witness:** 18/035:L13–21; 040:L21–28. **Quote:** frozen \(H^{\unsure{*|0}}(X(\mathbf R),\mathbf Q)=V^f\). **Context search:** `real | réellification | Betti | invariants` → N A07/A23 (15/203,215); adds a concrete check of the doubtful superscript, and scan040 supplies the quotient-space comparison. **RS:** MPL_15_195-228+18_002-017 A23; first-pass lead.

For these tests, \(X(\mathbf R)\) means the usual R-rational points, equivalently the fixed locus of complex conjugation: for \(X=\mathbf P^1_{\mathbf R}\), \(H^1(X(\mathbf C),\mathbf Q)^{f_\infty}=0\), whereas \(X(\mathbf R)=\mathbf RP^1\simeq S^1\) has \(H^1=\mathbf Q\). Scan040 instead writes the quotient \(X(\mathbf C)/\pi\), which for this example is a closed disk and has the rational cohomology of the invariant part. The degree-zero reading also requires care: for \(X=\operatorname{Spec}\mathbf C\) over R, there are no real points but the invariants in the two-point complex Betti H⁰ equal Q. These calculations leave the frozen `*|0` unchanged and make the superscript and the intended fixed-locus-versus-quotient convention questions for a future reading, rather than assigning the usual rational-point meaning to the manuscript without examination.

### RH09 — The reality of the period point is sharper than triviality of its torsor

**Kind:** own idea (explicit example). **Witness:** 18/036:L2–19; 037:L17–20. **Quote:** “\(\overline\alpha=f_\infty\alpha\)”. **Context search:** `torseur | alpha | réel | Tate` → N P11/P19 (18/011–012), A05 (15/197–199); adds the real torsor and its distinguished comparison point. **RS:** MPL_15_195-228+18_002-017 P11, P19, A05. **Confidence:** high; reason: a one-dimensional comparison and a displayed coboundary give both conclusions.

On the Tate category, the real comparison torsor has group \(\mathbf G_m\), and the real lines in the two fibre functors admit a tensor-compatible isomorphism chosen on their generator. Its cocycle value −1 is the explicit coboundary \(i^{-1}\bar i=-1\), but the distinguished period comparison is imaginary in the generator convention of scan029. Thus the equation on scan036 correctly tests \(\alpha\in P(\mathbf R)\); replacing that test by the existence of some point of \(P(\mathbf R)\) changes the assertion even in this example.

### RH10 — The even-Tate converse fails on the Artin–Tate summand

**Kind:** own idea (verified counterexample to the written assertion). **Witness:** 18/036:L21–29; 038:L16. **Quote:** “somme de puissances tensorielles de Q(2)”. **Context search:** `Q(2) | frobenius | Tate | tordu` → N A23/M03 (15/215;18/011), plus RS's Hua entry; adds a complete realization of the lead's counterexample. **RS:** Hua, findings register, **18-real-frobenius-trivial-converse**; MPL_15_195-228+18_002-017 A23, M03. **Confidence:** high; reason: algebraic projectors and two eigenvalue computations suffice.

For the sign Artin motive A and \(T=\mathbf Q(-1)\), the actual motive \(L=A\otimes T\) has \(f_\infty=(-1)(-1)=+1\), yet its Hodge weight is 2. It occurs as the anti-invariant summand for the algebraic deck involution on \(H^2(\mathbf P^1_{\mathbf C})\), with \(\mathbf P^1_{\mathbf C}\) regarded as an R-scheme, whereas tensor powers of \(\mathbf Q(2)\) have weights in \(4\mathbf Z\) and direct summands preserve the weight grading. The computation supports Hua's recorded refutation and remains valid in this Artin–Tate example with algebraic Hodge classes, so the page's “moyennant conj. de Hodge” does not remove it; Appendix A supplies the projector.

### RH11 — The abstract group Gm does not determine real Frobenius

**Kind:** own idea (explicit comparison). **Witness:** 18/036 diagram. **Quote:** “G ≃ Gm ou G ≃ {e}”. **Context search:** `Tate | hom central | graduation | G_m` → N M03/M11/P14 (18/011–012); adds a test of the displayed vertical equivalence. **RS:** MPL_15_195-228+18_002-017 M03, M11, P14; LM1 A.8 remains its supplied “Refuted, return's claim”. **Confidence:** high; reason: the two rank-one characters generate faithful one-dimensional groups with opposite specified involutions.

The subcategory generated by T has group \(\mathbf G_m\) and real Frobenius −1, while the subcategory generated by \(L=A\otimes T\) has group \(\mathbf G_m\) and real Frobenius +1. In each case every nonzero tensor power has nonzero weight, so there is no relation killing a power of its generating character; arbitrary invertible scalars therefore give the Tannaka group. These two explicit realizations show why the abstract group at the bottom of the diagram cannot by itself characterize the assertion \(f_\infty=1\).

### RH12 — The centrality margin requires the meaning of “Q tordu”

**Kind:** reading question. **Witness:** 18/036:L31. **Quote:** “Q tordu” and “comm.”, both retained with the frozen doubts. **Context search:** `tordu | central | Tate | Q(2)` → N M03/P14/M11 (18/011–012); adds an unresolved definition in the centrality margin. **RS:** MPL_15_195-228+18_002-017 M03, P14, M11.

The margin proposes a category generated by “Q tordu” and Q(2), and relates this to centrality of \(f_\infty\) and commutativity of G. T itself already gives a commutative group with central nontrivial \(f_\infty\), so any proposed reading of “Q tordu” must account for that Tate object and its weight. The page does not define the phrase locally, and the context's grading conventions do not decide its ink or intended generator.

### RH13 — The maximal-compact normalizer discussion is withdrawn on the sheet

**Kind:** withdrawn in the same text. **Witness:** 18/038:L20–44. **Quote:** “compact maximal”, inside deletion. **Context search:** `normalisateur | Norm | compact | polarisation` → N B03 (15/203,215,217), CT44/002,008–009; adds a withdrawn normalizer approach to the earlier positivity/descent discussion. **RS:** MPL_15_195-228+18_002-017 B03; WG2 §2.3 #12.

The entire paragraph containing \(f_\infty C f_\infty^{-1}=C^{-1}\), the proposed normalizers and the maximal-compact assertion is enclosed by the frozen deletion state. Within that withdrawn text the author also moves from G to \(G/i(G_m)\), so both the scalar quotient and the cancellation belong to the evidence. The live conjugation equation on scans034/037 survives independently, but scan038 supplies no completed maximal-compact argument to import into it.

### RH14 — A real form in de Rham cohomology is constructed even without real descent of X

**Kind:** unpursued implication. **Witness:** 18/039:L17; 040:L15–28. **Quote:** “même si X pas définissable sur R !”. **Context search:** `Betti | réel | descente | Hodge` → N A06/A07/A23 (15/199–203,215), CT54/003,005; adds a real subspace obtained through comparison, followed by explicit real descent when X is defined over R. **RS:** MPL_15_195-228+18_002-017 A06, A23.

The map written on scan039 is \(H^*(X_{\rm top},\mathbf R)\hookrightarrow H^*_{\rm dR}(X)\), obtained by extending the Betti coefficients through the selected archimedean topology. For a real model, scan040 additionally uses the semilinear diagonal action \(f_\infty\otimes c\), whose invariant vectors are \(V^+_{\mathbf R}\oplus iV^-_{\mathbf R}\). These displayed maps identify exactly how the comparison real form and the real model's descent form are related, rather than identifying the two subspaces without the involution.

### RH15 — The p,q degree in the boxed inclusions is a frozen reading question

**Kind:** reading question. **Witness:** 18/040:L33–35; 041:L6–12. **Quote:** \(H^{p,q}(X)\subset F^pH^q(X)\). **Context search:** `filtration | bigrad | Hodge` → N P09/P10/P13 (18/009,011), CT54/003,005; adds a total-degree convention question to the earlier filtration-index leads. **RS:** MPL_15_195-228+18_002-017 P09, P10, P13.

The source term is \(H^q(X,\Omega^p_X)\), while the boxed target uses \(H^q(X)\) rather than displaying the total degree p+q. The direct sum over p,q and the filtration construction make that index worth checking against the original convention, but the source is frozen and the apparent mismatch remains in the transcript. An application of the formula must first specify which graded component the written q denotes.

### RH16 — The final totally-real-field assertion has an embedding calculation

**Kind:** own idea (explicit verification of the stated intersection). **Witness:** 18/041:L20–26. **Quote:** “Kr est une ext. algébrique”. **Context search:** `tot.*réel | totally real | K_r | topologie` → N A12 (15/207) records a different totally-real-extension question; no matching intersection formula found in CT. **RS:** MPL_15_195-228+18_002-017 A05 and WG2 §2.4 #3 are broad links; no dedicated settled row. **Confidence:** high for the field calculation over all archimedean embeddings; reason: extension of a transcendence basis constructs the required embedding.

For the manuscript's K admitting an archimedean embedding, any transcendental \(t\in K\) can be included in a transcendence basis and sent to a nonreal transcendental complex number, after which the embedding extends over the remaining algebraic extension into C. The induced topology has complex completion, because its image contains \(\mathbf Q+\mathbf Q\sigma(t)\), a dense subspace of C, so t is excluded from the intersection of the written \(R_T\). An algebraic element survives exactly when each of its conjugates is real, since each embedding of its number field extends to K; consequently the intersection is precisely K's totally real algebraic subfield.

### RH17 — The p-adic questions remain questions on this package's list

**Kind:** self-flagged. **Witness:** 18/043:L20–22. **Quote:** “comparaison possible” and “Définition”. **Context search:** `p-adique | crist | Dieudonné | Oda` → N P01–P05 (18/005), A16 (15/211), CT54/003,005,007; restates the realization programme with an explicit mixed-characteristic comparison question and a positive-characteristic cohomology question. **RS:** MPL_15_195-228+18_002-017 P01, P02, P03, P04, A16.

The two question marks record separate tasks, with the discretely valued complete base and residue characteristic p written into the comparison task. Oda's supplied paper gives a precise degree-one abelian case in characteristic p: its Corollary 5.11 identifies \(M(A[p])\) with \(H^1_{\rm dR}(A)\) over a perfect field, respecting the Dieudonné operators and carrying VM to \(H^0(A,\Omega_A^1)\). That concrete morphism supplies evidence for one realization comparison while leaving the scope of the manuscript's entire numbered programme open.

### RH18 — Oda directly addresses the earlier p-torsion extension question

**Kind:** unpursued implication. **Witness:** 18/043; CT54/003,005,007. **Quote:** context54/007 asks “peut-elle se déduire de la connaissance de p^A ??”. **Context search:** `extension | p^A | Cartier | transposée` → CT54/003,005,007 and CN D01–D05; restates N P04's lead but verifies the supplied printed map and Hodge-sequence compatibility. **RS:** MPL_15_195-228+18_002-017 P04, A16; first-pass leads.

Oda, Corollary 5.11, p.131, identifies the short exact sequence in the Dieudonné module of \(A[p]\) with \(0\to H^0(A,\Omega_A^1)\to H^1_{\rm dR}(A)\to H^1(A,\mathcal O_A)\to0\). Its printed remark attributes this to a conjecture in Grothendieck's 1966 de Rham paper, reference [15], so the documented attribution is to that publication. This verifies a concrete extension-recovery link to CT54/007 without identifying the undated manuscript with the printed conjecture or assigning it priority.

### RH19 — Polarization and real Frobenius meet in the positive Weil form

**Kind:** own idea (explicit compatibility calculation). **Witness:** 18/034 normalizer formula; 037; 038 cancelled normalizers. **Quote:** “f∞ j(λ) f∞⁻¹ = j(λ′)”. **Context search:** `polarisation | positive | autodualité | Hodge` → CT44/002,008–009 and N B03 (15/203,215,217); adds the morphism and sign calculation connecting the two structures. **RS:** MPL_15_195-228+18_002-017 B03; WG2 §2.3 #12; MPL_14_002-044 A36 retains first-pass status. **Confidence:** high; reason: functoriality of the polarization and \(C^2=(-1)^n\) give the identity.

On a weight-n geometric realization with its real algebraic polarization \(q:V\otimes V\to\mathbf Q(-n)\), functoriality gives \(q(fx,fy)=(-1)^nq(x,y)\). With the Weil operator C, the live normalizer relation gives \(fCf^{-1}=C^{-1}\), and the positive real form \(B(x,y)=(2\pi i)^nq(x,Cy)\) satisfies \(B(fx,fy)=B(x,y)\) by the two cancelling signs. Appendix C records the exact calculation; this is the requested bridge through an actual pairing and involution, with no assertion that the involution alone chooses a polarization.

### RH20 — The nonlinear real-section map has a precise linear image

**Kind:** unpursued implication. **Witness:** 18/034,037 real Frobenius; 039–040 real descent. **Quote:** “automorphisme ... x↦x̄”. **Context search:** `réellification | real structure | section | polarisation` → N B03 (15/203,215,217); adds the abelianization map relating the real-section comparison to this manuscript's involution. **RS:** MPL_15_195-228+18_002-017 B03; LM7 E.23 remains Open and is not resolved by this comparison.

For a smooth projective hyperbolic curve over R, Pál's real-section result identifies \(\pi_0(X(\mathbf R))\) with conjugacy classes of continuous sections of its arithmetic fundamental-group sequence. A section sends complex conjugation to a lift whose conjugation action on the geometric group descends through \(\pi_1(X_{\mathbf C})\to\pi_1(X_{\mathbf C})^{\rm ab}\), and dual étale H¹ realizes the corresponding real Frobenius. Two lifts differ by an element of the geometric group, whose inner action vanishes after this abelianization; consequently this particular linear action retains the involution while forgetting the possible component distinction recorded by the section class.

## Appendix A — Explicit Artin–Tate counterexample and Hua adjudication

Write \(Y=\operatorname{Spec}\mathbf C\) as an R-scheme and let \(d\) be its nontrivial deck automorphism. The rational algebraic projectors \(e_+=(1+d)/2\) and \(e_-=(1-d)/2\) give
\[
h^0(Y)=\mathbf1\oplus A,\qquad f_\infty|_A=-1,\qquad A^{\otimes2}\simeq\mathbf1.
\]
The identification of Artin motives with finite continuous rational Galois representations is given in Deligne–Milne, Proposition 6.17, with the realizations in Remark 6.18; the concrete projectors here already exhibit the two summands.

Set \(X=\mathbf P^1_{\mathbf R}\times_{\mathbf R}Y\), which is exactly \(\mathbf P^1_{\mathbf C}\) regarded as an R-scheme. The Künneth and projective-line projectors give
\[
h^2(X)=T\oplus(A\otimes T),\qquad T=\mathbf Q(-1).
\]
On \(X(\mathbf C)=\mathbf P^1(\mathbf C)\sqcup\mathbf P^1(\mathbf C)\), let u₁,u₂ be the degree-two classes with the complex orientations; real Frobenius interchanges the two components and reverses each orientation, so its matrix and fixed vector are
\[
f_\infty=\begin{pmatrix}0&-1\\-1&0\end{pmatrix},\qquad
f_\infty(u_1-u_2)=u_1-u_2.
\]
The algebraic map \(1\times d\) interchanges u₁,u₂ without the orientation sign, so its projector \((1-(1\times d)^*)/2\) has image \(L=A\otimes T\), proving that the fixed line is a motivic summand rather than only a Betti eigenspace.

The concrete group maps from \(\mu_2\times\mathbf G_m\) are \(\rho_T(a,t)=t\) and \(\rho_L(a,t)=at\), sending the same element \((-1,-1)\) to −1 and +1 respectively. The Hodge character of L has type (1,1), hence weight 2; all tensor constructions from \(\mathbf Q(2)\) have weights in \(4\mathbf Z\), and morphisms of Hodge structures preserve those weights, so no such construction contains L. Products of the projective-line and finite étale schemes used here have cohomology generated by their factor hyperplane classes and component classes, all algebraic, which verifies the Hodge-conjecture premise relevant to this example directly. Hua's truncated register supplies the example as a lead; the calculations above verify the objection to scans036/038, without certifying any unsupplied portion of Hua's argument.

## Appendix B — Tensor structures and the real torsor

For the Q-space \(V=V^+\oplus V^-\), put \(W(V)=V^+\oplus iV^-\subset V_{\mathbf C}\). The ambient tensor multiplication has the four components
\[
V^+\otimes U^+\mapsto V^+\otimes U^+,
\quad V^+\otimes iU^-\mapsto i(V^+\otimes U^-),
\quad iV^-\otimes U^+\mapsto i(V^-\otimes U^+),
\quad iV^-\otimes iU^-\mapsto-(V^-\otimes U^-),
\]
which are Q-isomorphisms onto the corresponding summands of W(V⊗U); associativity follows from multiplication in C, and the unit is Q with f=1. The pointwise map a uses +1 in the plus summand and i in the minus summand, so its defect is exactly −1 on the minus-minus component.

For the Artin line A with \(A^{\otimes2}=\mathbf1\), a tensor isomorphism would identify its Betti pairing \(a^2=1\) with the W-pairing \((ia)^2=-1\), forcing \(q^2=-1\) over Q (or R). For the Tate generator T there is no tensor relation \(T^m=\mathbf1\) for nonzero m, and the assignment \(e_n\mapsto i^n e_n\) gives a tensor isomorphism to W on every positive, negative or zero tensor power. On the category generated by both A and T, the group is \(\mu_2\times\mathbf G_m\) and real Frobenius is \((-1,-1)\): its projection to \(\mathbf G_m\) is the coboundary \(i^{-1}\bar i=-1\), while its projection to \(\mu_2\) is nontrivial because every coboundary \(b^{-1}\bar b\) with \(b\in\{1,-1\}\) equals 1.

## Appendix C — Exact polarization/real-section row

| Linear statement and map | Nonlinear statement and map | Verified relation carried by this package |
|---|---|---|
| A real geometric polarization is \(q:V\otimes V\to\mathbf Q(-n)\), with \(q(fx,fy)=(-1)^nq(x,y)\); the associated Weil form is \(B(x,y)=(2\pi i)^nq(x,Cy)\). | For a smooth projective hyperbolic curve X/R, \(\pi_0(X(\mathbf R))\to\operatorname{Sec}(\pi_1(X)\to\operatorname{Gal}(\mathbf C/\mathbf R))\) is the real-section bijection, with sections taken up to geometric inner conjugation (Pál). | A section acts on the geometric group, then on its abelianization and dual H¹. That action yields the real-Frobenius compatibility in scans034/037, and inner conjugation acts trivially after abelianization. |

The positive-form calculation uses the actual identities \(f^2=1\), \(fC=C^{-1}f\) and \(C^2=(-1)^n\):
\[
\begin{aligned}
B(fx,fy)
&=(2\pi i)^nq(fx,Cfy)\\
&=(2\pi i)^nq(fx,fC^{-1}y)\\
&=(-1)^n(2\pi i)^nq(x,C^{-1}y)\\
&=(-1)^{2n}(2\pi i)^nq(x,Cy)=B(x,y).
\end{aligned}
\]
A real polarization supplies q in this calculation, while the manuscript's normalizer equation supplies the relation with C; no polarization has been inferred from the rational involution alone. For sections s₁,s₂, write \(s_2(c)=g s_1(c)\) with g in the geometric group, so \(\operatorname{Ad}(s_2(c))=\operatorname{Ad}(g)\operatorname{Ad}(s_1(c))\); passing to the geometric abelianization kills \(\operatorname{Ad}(g)\) and proves the stated comparison exactly.

## Author-marked qualifications in this research span

| Frozen locator | Words or state | What to retain |
|---|---|---|
| 18/021 first diagram | `\unsure{?}` on an upward arrow | The frozen reading treats the mark as uncertain; it is a possible author question, not a confirmed assertion. |
| 18/034 final sentence | “en vertu des conj. de Hodge” | Declared conjectural input for fullness. |
| 18/035:L11 | Tensor question followed by underlined “Oui” | A local question answered affirmatively on the sheet. |
| 18/035:L24–26 | “n'est pas compatible”; “Il semble” | The specific-map failure is asserted; existence of another tensor isomorphism is tentatively discussed. |
| 18/036:L10,21,29 | “si on admet”; “en vertu”; “moyennant conj. de Hodge” | Conjectural input remains visible, including in the deleted argument. |
| 18/038:L20–44 | Entire normalizer/maximal-compact paragraph deleted | Withdrawn working argument, not a live theorem. |
| 18/043:L20–22 | Two terminal question marks | Comparison and construction questions. |

## Primary sources checked

1. **Deligne, P.; Milne, J.S.** *Tannakian Categories*, 1982; corrected author version dated 15 August 2012, [PDF](https://www.jmilne.org/math/xnotes/tc2012.pdf). Checked Theorem 3.2 (fibre-functor torsors), Theorem 4.17 (polarization and compact band), Example 5.21 (Weil form), Proposition 6.17 and Remark 6.18 (Artin category and realizations); web refs `turn8view0`, `turn12view0`, `turn12view1`, `turn22view1`, `turn22view2`. The file is a versioned 2012 witness, not an assertion about an unexamined later edition.
2. **Milne, J.S.** *Shimura varieties and moduli*, author PDF, §5, especially the Tate convention and polarization formulas (5.4)–(5.5), [PDF](https://www.jmilne.org/math/xnotes/svhIP.pdf); web refs `turn15search2`, `turn22view0`. The formula used in Appendix C has precisely this cohomological convention; replacing C by its inverse requires the corresponding sign convention throughout.
3. **Pál, A.** *The real section conjecture and Smith's fixed-point theorem for pro-spaces*, published 2011; checked author preprint arXiv:0905.1205v2 dated 17 September 2009, Theorem 1.3 and Example 5.8, [PDF](https://arxiv.org/pdf/0905.1205), [published DOI](https://doi.org/10.1112/jlms/jdq075); web refs `turn8view1`, `turn12view3`, `turn14view1`. The table uses its smooth projective hyperbolic-curve case with all primes.
4. **Oda, T.** *The first de Rham cohomology group and Dieudonné modules*, Ann. Sci. ENS (4) 2 (1969), 63–135, Corollary 5.11 on printed p.131, [published PDF](https://www.numdam.org/article/ASENS_1969_4_2_1_63_0.pdf), DOI 10.24033/asens.1175; web refs `turn8view2`, `turn12view4`, `turn14view2`. Both the supplied PDF's printed page131 and its embedded text were checked; no OCR was run on any manuscript scan.

The external sources supply the definitions and precise published comparison statements; the Artin–Tate, tensor-defect, square-obstruction, fixed-space and abelianization calculations above are written out here and are not attributed to an unreviewed prior run.
