# Evidence record: Tate passage, Serre letter, and cote-16 comparison

Research snapshot: 2026-11-15, after the transcription freeze and the context opening at 00:41:55 UTC. `context/notes/RESULTS_STATE.md` was read in full before using the other context documents. This record is an evidence submission for the primary agent's review; the proposed notes below have not been inserted into the main notes.

The research used frozen TeX and context text, plus primary literature. No manuscript image or OCR was used in this research thread. Page files and the combined transcription were left untouched.

## File and status keys

- **F040**, **F041**, **F042**, **F044** mean `pages/MPL_14_002-044_14_scan040.tex`, `pages/MPL_14_002-044_14_scan041.tex`, `pages/MPL_14_002-044_14_scan042.tex`, and `pages/MPL_14_002-044_14_scan044.tex`, respectively, under `MPL_14_002-044_work/`. All line numbers below are physical TeX source lines, counted from 1.
- **CT** means `context/MPL_16+47+54+44_transcription.tex`. Its lines are global file lines; the cote and scan are supplied separately below.
- **CN** means `context/MPL_16+47+54+44_notes.md`; **CD** means the corresponding `_doubts.md`. These are unreviewed first-pass leads.
- **RS** means `context/notes/RESULTS_STATE.md`. **WG2 §2.4 #3** has status **question or plan item of the war game, round 2; unchecked**. It asks about this material and the author's lettering; it supplies no settled result for the present notes.
- The reproducible context queries and matching lines are in `records/research_tate_queries.json` and `records/research_tate_context_searches.md`. Entries RT1–RT8 correspond to the notes below; RT8-F records the bounded frozen-page search. Unrelated lexical hits have not been treated as mathematical counterparts.

## RT1 — The letter's quotient and the published cycle-class image

**Proposed note, three sentences.** The letter explicitly defines \(C^i(X)\) using algebraic equivalence and rational coefficients. Its comparison with Grothendieck's published \(C_\ell^i(X)\) is the surjection \(q_i:[z]_{\mathrm{alg}}\mapsto\mathrm{cl}_\ell(z)\), whose kernel is the rational group of homologically trivial cycles modulo algebraic equivalence. The map commutes with multiplication by the hyperplane class, so the letter's displayed map induces the later map on algebraic cohomology classes; the quotient and its kernel must remain visible in this comparison.

**Kind and confidence:** observation / exact comparison; high for the written definition and the displayed quotient.

**Frozen evidence:** F044, cote 14, scan 044, lines 6–8. Brief quote: “mod équivalence algébrique, tensorisé par \(\underline{\mathbb Q}\)”; line 8 states the map \(\xi^{n-2i}:C^i(X)\to C^{n-i}(X)\).

**Context and relation:** CT, cote 16, scan 044, line 1725 discusses dimensions of \(C^i\) and \(C^{n-i}\), and scan 045, lines 1739–1746 gives critical-degree cohomological maps. CN, S1, lines 3074–3088 offers a provisional lettering dictionary. **Differs / adds:** cote 14 makes the algebraic-equivalence quotient explicit, and the map below supplies the precise comparison that the dictionary needs. CT, cote 44, scan 006, line 2944 gives a separate \(\tau\)-equivalence assertion; no meaning for that \(\tau\) is imported into F044. Search: RT1, with RT2 for the \(\tau\) passage.

**RESULTS_STATE:** WG2 §2.4 #3, unchecked planning item. No matching settled entry asserts this quotient or settles the letter's formulation.

**Primary check:** [G69], §2, definition of \(C_\ell^i(X)\) as the image of the cycle-class map, followed by §3, A(b). The coefficient convention is important: the published image of cycles tensored with \(\mathbb Q\) is a rational vector space inside cohomology; the \(\mathbb Q_\ell\)-span in the Tate passage is discussed separately in RT6.

**Exact map and justification.** Write \(Z^i_{\mathbb Q}\) for the rational cycle group, \(Z^i_{\mathrm{alg},\mathbb Q}\) for its subspace of algebraically trivial cycles, and \(Z^i_{\mathrm{hom},\mathbb Q}\) for the kernel of the chosen rational cycle-class map. Then

\[
0\longrightarrow
\frac{Z^i_{\mathrm{hom},\mathbb Q}}{Z^i_{\mathrm{alg},\mathbb Q}}
\longrightarrow C^i_{\mathrm{alg}}(X)
\xrightarrow{q_i} A_H^i(X)
\longrightarrow0,
\qquad
A_H^i(X)=\operatorname{im}(\mathrm{cl}_H).
\]

The factorisation follows from constancy of cycle class in a connected algebraic family: restriction of the class of a family on \(X\times T\) to \(X\times\{t\}\) uses the same map on \(H^0(T)\), while its positive-degree \(T\)-components restrict to zero. This is also the argument in [K68], §1.2.1. Multiplicativity gives the exact compatibility

\[
q_{n-i}\bigl(\xi^{n-2i}z\bigr)
=\mathrm{cl}_H(\xi)^{\,n-2i}\cup q_i(z).
\]

Here the left-hand kernel is denoted \(\operatorname{Griff}_H^i(X)_{\mathbb Q}\). This comparison supplies no assertion that this kernel vanishes.

## RT2 — A concrete obstruction to Conjecture A with the written equivalence

**Proposed note, three sentences.** For a very general smooth quintic threefold \(V\subset\mathbb P^4_{\mathbb C}\), the letter's map for \((n,i)=(3,1)\) has image \(\mathbb Q H^2\), where \(H\) is the hyperplane class. Clemens's theorem and the Griffiths vanishing recalled in his introduction give nonzero rational homologically trivial classes in \(C^2_{\mathrm{alg}}(V)\), outside that image. Thus the formulation of A written on scan 044 has a concrete counterexample; passing through the quotient \(q_2\) from RT1 removes exactly the classes used in this obstruction.

**Kind and confidence:** verified editorial deduction from identified results; high. This is a statement about the written algebraic-equivalence formulation, without changing the transcription.

**Frozen evidence:** F044, cote 14, scan 044, lines 6–10. Brief quotes: “mod équivalence algébrique”; “Le premier cas qui échappe pour le moment est \(i=1,n=3\)”.

**Context and relation:** CT, cote 44, scan 006, lines 2939–2947, especially Th. 7 at line 2944; CT, cote 16, scan 046, line 1781 has an uncertain \(\tau\)-equivalence annotation. CN, D14, lines 3540–3546 already cites Clemens against an unrestricted reading of Th. 7. **Adds:** the counterexample is applied here directly to the explicit quotient and the actual multiplication map in the 1965 letter, without resolving the context's uncertain \(\tau\). Search: RT2.

**RESULTS_STATE:** no matching settled entry or registered counterexample. WG2 §2.4 #3 is the relevant unchecked lettering question; WG2 §2.1 #5, also an unchecked planning item, records the older cote-44 programme.

**Primary check:** [C83], §0, equation (0.1), Theorem (0.2), Corollary (0.3), and the explanation of “generic” at the beginning of p. 20 were actually read. Equation (0.1) kills the algebraically trivial subgroup under Abel–Jacobi; Theorem (0.2) makes the rational Abel–Jacobi image infinite-dimensional. Their combination gives an infinite-dimensional rational quotient of homologically trivial cycles by algebraic equivalence. “Very general” here means outside a countable union of proper closed subsets, as specified there.

**Calculation of the map.**

1. Weak Lefschetz gives \(H^2(V,\mathbb Q)=\mathbb Q H\). In codimension one, the kernel of the rational cycle-class map is algebraic equivalence; [K68], introduction, records the divisor comparison, §1.1 defines \(\tau\)-equivalence by a nonzero multiple becoming algebraically trivial, and §1.2 places homological equivalence between the relevant relations. Hence \(C^1_{\mathrm{alg}}(V)=\mathbb Q H\).
2. The multiplication map in the letter is
   \[
   m_H:C^1_{\mathrm{alg}}(V)\longrightarrow C^2_{\mathrm{alg}}(V),
   \qquad aH\longmapsto aH^2.
   \]
3. Its image meets \(\ker q_2\) only in zero: \(q_2(aH^2)=0\) implies \(a\int_V H^3=5a=0\).
4. The nonzero rational quotient supplied by [C83] is contained in \(\ker q_2\). Therefore \(m_H\) is not surjective.

This uses the infinite-dimensional assertion together with (0.1), rather than relying only on the weaker phrase “not finitely generated”, which by itself would not establish nonzero rational classes.

## RT3 — What the supplied pages establish about A–D lettering

**Proposed note, four sentences.** The surviving Serre letter fixes the meaning of its A but does not reach a written second conjecture. Cote 16's draft \(C_\ell\) is expressed through algebraic inverse Lefschetz maps, matching the operator content called B in the published account. The correspondence action in this comparison is \(z_*(a)=p_{2*}(p_1^*a\cup\mathrm{cl}(z))\), and the draft's inverse construction is \(v^{-1}=(uv)^{-1}u\). The evidence supports that operator comparison and the published dictionary below; it does not supply standalone definitions for every draft letter B and D.

**Kind and confidence:** reading question with verified operator comparison; high for the cited maps, medium for any wider draft dictionary.

**Frozen evidence:** F044, cote 14, scan 044, lines 6, 8 and 10–12. Brief quotes: “les deux conjectures-clef”; “Conjecture A”; the surviving text ends after “est bijectif pour” and is followed by \(\ldots/\ldots\).

**Context and relation:** CT, cote 16, scan 044, lines 1723–1725; scan 045, lines 1748–1750; scans 048–049, lines 1803–1823. CN, S1, lines 3074–3088 is the first-pass dictionary. **Adds / restates:** F044 supplies an earlier explicit A and a precise documentary limit; the inverse-operator comparison restates the useful part of S1 after checking the primary literature. Search: RT3.

**RESULTS_STATE:** WG2 §2.4 #3, unchecked; no settled result in RS fixes these draft letters.

| Published notation | Verified content | What the cited manuscript evidence supports |
|---|---|---|
| A | Hyperplane multiplication on algebraic cohomology classes; [G69] §3 also includes cohomological hard Lefschetz | F044 uses the quotient in RT1. Cote 16's critical-degree descriptions concern cohomology. |
| B | Algebraicity of the Lefschetz inverse/lowering correspondence | The inverse-operator content of draft \(C_\ell\) on CT 16:45 and 16:48–49 matches this. |
| C | Algebraic Künneth projectors | This meaning is explicit in [G69] §2 and [K68] §2. No standalone definition of draft D is recovered merely from its occurrences. |
| D | Homological equivalence equals numerical equivalence | Explicit in [K68] §3.6. Draft B's relations with A and index positivity suggest a comparison, but those relations alone do not define draft B. |

**Primary passages actually checked:** [G69], §§2–3; [K68], §2 definitions, §§2.3 and 2.9, and §3.6. In particular, the proposition in CT 16:48 about complementary-degree algebraic isomorphisms and rational characteristic polynomials has the same operational form as [K68], §2.9. This comparison does not turn the missing draft definitions into established identities.

**The inverse calculation on the source's displayed maps.** The context writes
\[
u:H^{2n-i}(X)\to H^i(X),\qquad
v=L^{n-i}:H^i(X)\to H^{2n-i}(X),\qquad w=uv.
\]
The proposed inverse \(w^{-1}u\) satisfies
\[
(w^{-1}u)v=\mathrm{id}_{H^i(X)},\qquad
v(w^{-1}u)=\mathrm{id}_{H^{2n-i}(X)}.
\]
For the characteristic polynomial \(t^b+a_{b-1}t^{b-1}+\cdots+a_0\) used in that argument,
\[
w^{-1}=-a_0^{-1}
\left(w^{b-1}+a_{b-1}w^{b-2}+\cdots+a_1\mathrm{id}\right).
\]
This is an editorial calculation of the actual maps named in CT, not a correction of its uncertain written powers or its \(u/w\) readings.

## RT4 — The author's unwritten reduction and the incomplete continuation

**Proposed note, three sentences.** The reduction to surjectivity in odd dimension is explicitly introduced by “Modulo vérification que je n'ai pas écrite en détail”, so this sheet records the author's proposed reduction and not its missing verification. Cote 16 later refers to old attempts to reduce the strong Lefschetz form to the weak one, while writing critical-degree maps on self-products and adjacent hyperplane products. The present letter stops during the Gysin discussion, leaving both the remainder of that argument and the promised second conjecture outside the supplied text.

**Kind and confidence:** unproved manuscript claim / documentary observation; high.

**Frozen evidence:** F044, cote 14, scan 044, lines 6–12; quote as above, and “\(n=2i+1\)”. The written restriction map is \(H^i(X)\to H^i(Y)\); the next Gysin sentence is incomplete.

**Context and relation:** CT, cote 16, scan 045, lines 1739–1750; scan 046, line 1765; scan 047, line 1791, quote “old scribbles” and “strong” / “week”. CN, notes 16:47:3, lines 1425–1431. **Restates / adds:** the ambition to reduce the strong form is restated in the context; F044 adds an explicitly self-qualified earlier witness. Search: RT4.

**RESULTS_STATE:** WG2 §2.4 #3 and WG2 §6. #9, both unchecked planning items; no matching settled verification of this letter's reduction.

**Primary comparison and exact maps:** [K68], §1.4.7, treats a smooth hyperplane inclusion \(j:Y\hookrightarrow X\), with restriction \(j^*\), Gysin \(j_*\), and \(j_*j^*=L_X\). These are the cohomological maps appearing at the end of F044. That comparison does not supply the omitted argument on \(C_{\mathrm{alg}}^i\); RT1 and RT2 explain why its quotient must be retained.

## RT5 — Elliptic powers and the Mumford attribution

**Proposed note, three sentences.** The named example is a power \(C^n\) of an elliptic curve defined over a finite field, with the divisor assertion reduced to the product of two elliptic curves. Tate's 1966 paper, §1, explicitly credits Mumford for pointing out that the elliptic-pair case follows from Deuring's results, giving a close primary-literature match to the attribution on these sheets. Milne's Appendix A.3 example confirms that Tate classes on all powers of such a curve are generated by divisor classes.

**Kind and confidence:** verified historical and mathematical comparison; high for the source match, without an attribution of priority beyond Tate's own statement.

**Frozen evidence:** F041, cote 14, scan 041, line 24, and F042, scan 042, line 2. Brief quotes: “puissance” with marginal “\(C^n\)”; “a été vérifié pr Mumford”; “produit de deux courbes elliptiques”. F040, scan 040, line 2 gives the title “Astuce de Tate”.

**Context and relation:** RT5 finds Mumford references in CT, cote 16, scan 019, line 753, and cote 47, scans 007 and 009, lines 2335 and 2439. They concern other constructions. CN's associated entries do not supply the elliptic-pair Tate attribution. **Adds:** this particular example and attribution are newly supplied by cote 14 relative to the searched context. Search: RT5, with RT6.

**RESULTS_STATE:** explicitly no matching entry for the finite-field elliptic-pair assertion or “Astuce de Tate”. The unrelated elliptic occurrence in LM7 C.8 has not been used as a match.

**Primary check:** [T66], §1, p. 134, main theorem and the immediately following attribution; [M01], Appendix A.3, example on p. 15. Here the base field is the finite field \(\mathbb F_q\), and \(\ell\ne\operatorname{char}(\mathbb F_q)\). The actual map of [T66] is
\[
\operatorname{Hom}_{\mathbb F_q}(A,B)\otimes\mathbb Z_\ell
\longrightarrow
\operatorname{Hom}_{\operatorname{Gal}(\overline{\mathbb F}_q/\mathbb F_q)}
(T_\ell A,T_\ell B),\qquad f\longmapsto T_\ell f.
\]

For the divisor correspondence used in the manuscript's reduction, a line bundle \(\mathcal L\) on \(C\times C\) gives
\[
\phi_{\mathcal L}:C\to C^\vee,\quad
x\longmapsto
\bigl[\mathcal L|_{\{x\}\times C}\otimes
(\mathcal L|_{\{0\}\times C})^{-1}\bigr],
\]
followed by \(T_\ell\phi_{\mathcal L}\). This specifies the comparison with a homomorphism of Tate modules, rather than identifying the two assertions by their names alone.

## RT6 — What the equality of the two outer terms requires

**Proposed note, four sentences.** The margin on scan 042 describes the first term as decomposable algebraic classes, which leads to the multiplication map \(\operatorname{Sym}^i_{\mathbb Q_\ell}H^2(A,\mathbb Q_\ell(1))^{\mathrm{alg}}\to H^{2i}(A,\mathbb Q_\ell(i))\). The manuscript gives the two inclusions and then asserts equality of the outer terms from its hypotheses. The stated elliptic-power example has this divisor-generation property in [M01], Appendix A.3, but the passage supplies no full verification for the uncertain general condition b). Its \(\mathfrak g\)-invariants should therefore be quoted as written, without silently replacing them by a fixed finite-field Galois-invariant space.

**Kind and confidence:** unproved manuscript claim and exact map; high for the proof boundary, medium for expanding the abbreviated symbol \(D^{2i}\) as precisely the image of this multiplication map.

**Frozen evidence:** F041, cote 14, scan 041, lines 10–22; F042, scan 042, lines 4–10. Brief quotes: “décomposables \(\mathbb Q_\ell\)-algébriques”; “à priori on a les inclusions”; “l'hypothèse implique l'égalité des extrêmes”.

**Context and relation:** CT, cote 44, scan 008, line 2974 discusses a Tate module associated with an intermediate Jacobian, but does not make this divisor-generation assertion. CN, D14 concerns equivalence relations instead. **Adds:** the displayed equality and its representation-theoretic hypothesis have no direct counterpart found by RT6. The context's nearby words “Tate” or “Tate module” have not been treated as an identification of the invariant spaces.

**RESULTS_STATE:** explicitly no matching entry that proves this argument or defines \(\mathfrak g(k)\) for it.

**Primary check and exact comparison:** [M01], §1, defines geometric Tate classes as the union of invariants over finite-field models; for one chosen model this can be written
\[
\bigcup_{r\ge1}\ker(F^r-\mathrm{id})
\subset H^{2i}(A_{\overline{\mathbb F}_q},\mathbb Q_\ell(i)).
\]
This formula records the union over finite extensions. The cup-product map sends \(d_1\cdots d_i\) to \(d_1\cup\cdots\cup d_i\). [M01], Appendix A.3, identifies its image with all Tate classes for the elliptic-power example. No identification of the manuscript's unspecified pro-Lie algebra with a particular monodromy Lie algebra has been established in this record.

## RT7 — Frobenius exponent, root-of-unity factor, and scalar extension

**Proposed note, four sentences.** Scan 041 writes \(\varepsilon q^{-1/2}\) with \(\varepsilon\) a root of unity, alongside an uncertain “pseudoalgébrique” and an alternative two-piece decomposition. Dualising a representation changes an eigenvalue \(\alpha\) to \(\alpha^{-1}\), which explains why the representation and Frobenius convention matter for the exponent's sign. A root-of-unity multiple of \(q^{-1/2}\) is nevertheless stronger than the corresponding absolute-value statement, as the explicit elliptic curve calculation below shows. The minus sign, the alternative formulation, and the uncertain Tits attribution must consequently remain evidence to interpret, without using the literature to amend the frozen reading.

**Kind and confidence:** reading question with a verified explicit calculation; high for the distinction established by the calculation, unresolved for the author's intended convention and the Tits reference.

**Frozen evidence:** F041, cote 14, scan 041, lines 4–8 and 16–22. Brief quotes: “\(\varepsilon q^{-1/2}\), \(\varepsilon\) une racine de l'unité”; marginal `\unsure{Pr. Tits}`; “ou”. Line 6 writes \(\mathbb T_K(A)=\mathbb T_\ell(A)\), while line 8 calls it a \(\mathfrak g_K\)-module.

**Context and relation:** RT7 finds no matching text for this convention, “pseudoalgébrique”, or Tits in CT. CN, D03, lines 3445–3450, concerns cote 54, scans 005 and 007, Frobenius–Verschiebung kernels; S17, lines 3199–3203 concerns algebraic Künneth projectors. **Adds:** the eigenvalue wording is new evidence relative to those context passages; neither supplies its missing convention. Search: RT7.

**RESULTS_STATE:** explicitly no matching entry.

**Primary checks:** [T66], §1 and the end of §2, identifies the covariant Tate module and the action of the finite-field Frobenius endomorphism. [M01], Appendix A.6, defines the Weil-number weight condition and its valuations. Those passages establish the comparison framework, without resolving this manuscript notation.

**Exact changes of representation.** For a matrix \(F\), inversion gives \(F^{-1}\), and the contragredient action on the dual is \((F^{-1})^{\mathsf t}\); both send an eigenvalue \(\alpha\) to \(\alpha^{-1}\). For the arithmetic field automorphism \(\sigma_q:x\mapsto x^q\), the definition of \(\mathbb Q_\ell(1)\) through roots of unity gives action by \(q\), whereas \(\sigma_q^{-1}\) gives action by \(q^{-1}\). These are explicit transformations, and none singles out the convention intended on F041.

The usual scalar-extension map is
\[
V_\ell(A)\longrightarrow V_\ell(A)\otimes_{\mathbb Q_\ell}K,
\qquad v\longmapsto v\otimes1.
\]
F041 line 6 does not write the tensor factor. This record uses the displayed map only to explain the comparison, not to supply text to that line.

**Explicit check of the root-of-unity issue.** For
\[
E/\mathbb F_5:\quad y^2=x^3+x+1,
\]
the discriminant is \(4\pmod5\). For \(x=0,1,2,3,4\), the respective numbers of affine points are \(2,0,2,2,2\); including infinity gives \(\#E(\mathbb F_5)=9\). Thus the Frobenius polynomial is \(t^2+3t+5\), with roots
\[
\alpha=\frac{-3+\sqrt{-11}}2,\qquad
\overline\alpha=\frac{-3-\sqrt{-11}}2,\qquad
\alpha\overline\alpha=5.
\]
For \(\beta=\alpha/\sqrt5\),
\[
\beta+\beta^{-1}=-3/\sqrt5,\qquad
(\beta+\beta^{-1})^2=9/5.
\]
A root of unity and its inverse have an algebraic-integer sum; its square cannot be the rational noninteger \(9/5\). Hence \(\beta\) is not a root of unity, and neither is its inverse. The inverse eigenvalue \(\alpha^{-1}\) has absolute value \(5^{-1/2}\) but has no expression \(\varepsilon5^{-1/2}\) with \(\varepsilon\) a root of unity. This calculation does not refute the manuscript's separate two-piece alternative and does not identify the uncertain Tits statement.

## RT8 — The singular-hypersurface programme: a bounded textual result

**Proposed note, three sentences.** Cote 16, scan 047 explicitly proposes working with singular hypersurfaces and reformulating the standard conjectures for singular varieties, after reporting Serre's objection to the preceding smooth reduction. In the supplied cote-14 text, the Serre letter instead begins with a smooth projective \(X\) and a smooth hyperplane section, and its visible maps are restriction and Gysin for that inclusion. No explicit singular-variety reformulation was found in the 40 supplied frozen pages; this observation is bounded to those pages and the retained search ledger.

**Kind and confidence:** bounded textual observation; high for the quoted passages, with the negative result limited to the supplied text and documented searches.

**Frozen evidence:** F044, cote 14, scan 044, lines 6 and 10–12. Brief quotes: “variété projective lisse connexe”; “section hyperplane lisse”. The inclusion \(j:Y\hookrightarrow X\) and its \(j^*,j_*\) are the concrete link with RT4.

**Context and relation:** CT, cote 16, scan 047, line 1791: “work also with singular ones” and “reformulate for singular varieties the standard conjectures”. CN, 16:47:4–6, lines 1433–1455, records the programme and suggests later research directions. **Differs / no explicit continuation found:** cote 14 supplies the smooth formulation but no explicit answer to this programme in the searched material. The suggestion in CN is an unreviewed editorial lead, not a construction performed by this record. Search: RT8 and RT8-F.

**RESULTS_STATE:** WG2 §2.4 #3, unchecked planning item, is the broader motives/lettering question. The explicit singular-hypersurface question occurs in `context/README.md`, lines 24–25; it has no separately matching RS entry.

**Primary boundary:** [G69], §3 works with smooth projective varieties, and [K68], §1.4.7 supplies the smooth inclusion maps used above. This record attributes the simply-connectedness objection to the context manuscript; it does not assert a new general theorem about specialization, birational maps, or singular varieties.

**Search scope:** at 00:55:16 UTC, case-insensitive searches of all 40 frozen page files gave zero matching lines for each of: `hypersurf`; `singuli|singular|\bsing\.|\bn\.?\s*s\.`; `désingular|desingular|résol|resol|birat`; and `spécialis|specialis|specializ`. Zero lexical matches alone do not prove absence of every indirect allusion. The positive smooth wording and the surviving letter's incomplete ending bound the observation above.

## Verified primary literature and passages read

All five items below are primary research texts, not the supplied context notes. The references identify the passages actually used; the manuscript comparisons and explicit calculations above are editorial deductions.

| Key | Primary reference and stable URL | Passage actually read for this record |
|---|---|---|
| G69 | Grothendieck, A. (1969). *Standard conjectures on algebraic cycles*, pp. 193–199. [Primary text PDF](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/StandardConjs.pdf) | §§2–3: cycle-class image, Künneth condition, Lefschetz map and correspondence action. |
| K68 | Kleiman, S. L. (1968). *Algebraic cycles and the Weil conjectures*, in *Dix exposés sur la cohomologie des schémas*, pp. 359–386. [Primary text PDF](https://agrothendieck.github.io/divers/kleimanweil.pdf); [university mirror](https://download.uni-mainz.de/mathematik/Algebraische%20Geometrie/Lehre/WS23.Padische.1966.kleiman.weil.pdf) | Introduction; §§1.1–1.2; §1.4.7; §2 definitions and §§2.3, 2.9; §3.6. |
| T66 | Tate, J. (1966). *Endomorphisms of abelian varieties over finite fields*. *Inventiones Mathematicae, 2*, 134–144. [Primary text PDF](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf) | §1, main theorem, Mumford/Deuring attribution and \(V_\ell\); end of §2, finite-field Frobenius; §3, Theorem 1. |
| C83 | Clemens, H. (1983). *Homological equivalence, modulo algebraic equivalence, is not finitely generated*. *Publications Mathématiques de l'IHÉS, 58*, 19–38. [Primary text PDF](https://www.numdam.org/article/PMIHES_1983__58__19_0.pdf) | §0, pp. 19–20: (0.1), Theorem (0.2), Corollary (0.3), and meaning of “generic”. |
| M01 | Milne, J. S. (2001). *The Tate conjecture for certain abelian varieties over finite fields*. [Author's submitted-version PDF](https://www.jmilne.org/math/articles/2001aP.pdf) | §1, Tate-class definition; Appendix A.3, lemma and elliptic example on p. 15; Appendix A.6, Weil-number conventions. |

Retrieval note: the direct Kleiman URL returned a 404 on one repeat attempt, while the search service's previously retrieved complete primary-text record remained readable and was used for the cited sections. A university mirror was then opened successfully and its introduction and §1.1 checked as well. The Grothendieck PDF had one text-extraction-empty repeat; the earlier readable primary-text record supplied §§2–3. No claim is based on a search-result snippet alone.

## Handoff priorities

1. Preserve the literal algebraic-equivalence definition in F044 and attach the exact quotient in RT1 before comparing conjecture letters.
2. The quintic argument in RT2 is the most substantive new application relative to the context leads; its rational conclusion uses both (0.1) and Theorem (0.2).
3. The finite-field example and Mumford attribution in RT5 are verified; the general argument and the ambiguous eigenvalue formulation remain at the proof/reading boundaries recorded in RT6–RT7.
4. Report the singular-programme result with its supplied-page boundary, not as an assertion about other cotes or the archive.

Read-only final integrity check: 2026-11-15 01:01:59 UTC; all 41 files in records/frozen_hashes.txt matched their frozen SHA256 values.
