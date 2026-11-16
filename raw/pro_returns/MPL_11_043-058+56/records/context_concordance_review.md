# Context concordance review: cotes 11 and 56

Research-only working record for integration by the principal transcriber. The principal transcriber reported the transcription freeze at **2026-11-16 14:05:25 UTC** and the opening of context at **14:05:37 UTC**. This review reads frozen text and supplied contextual text. It does not amend a reading, determine an uncertain letter from context, inspect a scan image, run OCR, or supply the final package notes.

## Source key, scope, and evidential status

- **F11/NNN** means `pages/MPL_11_043-058+56_11_scanNNN.tex`, cote 11, scan NNN.
- **F56/NNN** means `pages/MPL_11_043-058+56_56_scanNNN.tex`, cote 56, scan NNN.
- **CT C/S** means `context/MPL_16+47+54+44_transcription.tex`, the text under `\cotefile{C}` and `\scanpage{S}`. The context directory is `/workspace/scratch/b04fc32065f5/context`.
- **CN C:S:N** means the identically numbered observation in `context/MPL_16+47+54+44_notes.md`; named R/F/S entries refer to that file's later research sections.
- **CD C/S** means rows and discussion assigned to cote C, scan S in `context/MPL_16+47+54+44_doubts.md`.
- **RS** means `context/notes/RESULTS_STATE.md`. Entry IDs below are copied from that file.
- **README** means `context/README.md`.

README and RS were read in full. The three context files were searched for the requested objects and words, then the relevant passages were read. CT is a supplied earlier transcription, with uncertainties; CN contains earlier interpretive claims and subsequent calculations. README describes the earlier package and other returned research as claims to be checked, and identifies the original planning questions as predictions made before reading the present pages. CD also records its own audit process. These layers are preserved: the present concordance does not turn a prior-run claim, a reading audit, or a research plan into an independently proved mathematical statement.

All cote/scan references below refer to the frozen literal text. `\unsure`, `\deleted`, and explicit question marks remain material evidence. The supplied RS often gives only an excerpt from a named return; those full returns were not supplied here and were not reconstructed from the excerpt.

## 1. Targeted search record and bounded no-hits

The search was run on all of CT, CN, and CD, with cote/scan tracking for CT and section tracking for CN/CD. The scratch search manifest is `qa_research/context_search_hits.json`. Its counts are matching **lines**, not mathematical occurrences. TeX line breaks can split phrases: the proper-support hit on CT 47/3 was recovered by reading the passage, although a simple same-line search returned zero. This limitation is expressly retained.

| Object or search | Located evidence | Bound on the result |
|---|---|---|
| `quadrique`, `quadriques` | No literal hit in CT, CN, or CD. | This search did not locate an earlier quadric calculation in these three files. It does not establish absence of a mathematical relationship to their Lefschetz calculations. |
| `vanishing cycle`, `évanesc…` | CT 16/40: the projector onto the `partie évanescente` (E^{n-1}). | A direct textual hit. The comparison with the present Φ-groups requires the actual maps discussed below. |
| `cône`, `cone` | No CT hit; CN 47:8:2 and F7 use “cone” in a derived comparison. | The CN hits concern that comparison's cone; no construction of the present projective cone \(\widehat C\) was located there. |
| `support compact`, `compact-support`, `H_c`, `H_{c}` | No literal hit in the three context files under these patterns. | This bounded search does not answer the explicit question at F56/017. |
| `supports propres`, `proper support` | CT 47/3, long margin, split over TeX lines; CN 47:3:2 and F2. | These passages specify proper support over the base for the Fourier/convolution construction. |
| Hyperplane/Gysin words | CT 16/33, 42, 45, 46, 47; 44/4; 54/8; corresponding CN discussions. | These hits include both cohomological hyperplane maps and a reused hyperplane-arrangement typescript. The actual maps are recorded separately below. |
| `Weyl`, whole-word `tore(s)`, `centralisateur`, `normalisateur`, `centre réductif` | No literal hit in CT, CN, or CD with these patterns. | More general group-scheme and Coxeter/root passages do occur: CT 16/30, 47/3, 44/7, and 54/8. |
| `d'indice 2`, `index-two`, `2-torsion` | No literal hit under the explicit patterns. | CN R1–R2 nevertheless contain a directly relevant integral exterior-algebra calculation; exact-word absence cannot discard it. |
| `Delzant`, `Stiefel`, `Whitney`, `quaternion`, `Clifford` | No literal hit in the three context files. | CT 16/21 and 16/23 do contain Brauer-group calculations. |
| `Brauer` and `\operatorname{Br…}` | CT 16/21, 16/23; CN 16:21:3, 16:21:6, 16:23:2, 16:23:4, R8; CD 16/21 and 16/23. | These supply a comparison location, not an identification of all the invariants in the Delzant offprint. |

The current 50 frozen files were additionally searched for the RS-specific strings `U_3`, `metabel…`, `pro-3`/`pro 3`, `section classes`, whole-word `GT`, `gentle`, `C_2\amalg C_3`, and `\tau=sr` (allowing spaces around the displayed symbols). These searches returned no hits. This records the absence of those direct textual witnesses in the selected files; it does not assert mathematical independence of research programmes.

## 2. Exact mathematical concordance

### C01 — Hyperplane inclusion, restriction, and Gysin multiplication

**Current witnesses:** F56/011, 020, 022, 026, 032. **Context:** CT 16/33, 16/40, 16/42; CN 16:33:1–2, 16:40:1–4, 16:42:1–5; CD 16/33, 16/40, 16/42. **Relation:** direct hit; the present pages add explicit quadric calculations to the shared maps.

CT 16/33 names a smooth hyperplane inclusion \(\varphi:Y\to X\), pullback \(\varphi^*\), pushforward \(\varphi_*\), and \(L_X\), cup-product with the polarization. CT 16/40 explicitly annotates \(\varphi_*\varphi^*\) as \(L_X\). The corresponding current inclusion is

\[
\alpha:Q^{n-1}\hookrightarrow Q^n,
\qquad
H^{i-2}(Q^{n-1})(-1)\xrightarrow{\alpha_*}H^i(Q^n),
\]

introduced at F56/020. F56/022 gives its rank behavior; F56/026 records restriction and pushforward on the named powers, divided power classes, and middle classes. The comparison sends \(X\) to \(Q^n\), \(Y\) to \(Q^{n-1}\), \(\varphi\) to \(\alpha\), and the polarization to the hyperplane class \(\xi\). Under that displayed identification of the map and class, the context push–pull composite is multiplication by the same \(\xi\) whose kernels and cokernels are tabulated in F56/032.

F56/011 also gives an explicit related self-intersection calculation for \(j:X\hookrightarrow\widehat C\):

\[
j^*j_*(c)=c\xi,
\qquad j_*(a)j_*(b)=j_*(ab\xi).
\]

This is a useful precise comparison of the operation; the ambient pair \((X,\widehat C)\) is recorded as it stands. The present formulas do not prove the full context induction statement involving \(C(X),C(Y),A^0(X\times Y)\), or all of the operator identities involving \(\Lambda\). Those claims retain the scope and unresolved readings recorded in CN/CD. RS connections: **WG2 §2.2 #4**, **WG2 §2.4 #3**, **WG2 §6. #9**.

### C02 — Vanishing cycles and the context evanescent projector

**Current witnesses:** F56/002–007, especially 003, 005, 007. **Context:** CT 16/40; CN 16:40:2 and surrounding entries; CD 16/40. **Relation:** direct word/object hit; current pages add a specific quadric degeneration.

F56/003 describes a projective flat family over a strictly local discrete valuation base, a singular special quadric and a nonsingular geometric generic quadric. Its long exact row contains specialization and the groups \(\Phi^{i+1}\). F56/005 records parity-dependent kernels/cokernels and the action of \(\pi\). F56/007 passes to \(U=X-Z\) and writes \(H^i(\overline U_1)\simeq\Phi^{i+1}\), after its assertion about \(H^i(U_0)\), and concentrates the vanishing cycles in degree \(n\).

CT 16/40 supplies the exact projector formula

\[
\varphi^*\Lambda_X\varphi_*=\operatorname{id}_Y-p_E,
\qquad p_E:\text{projection onto the partie évanescente }E^{n-1}.
\]

The passages examined supply no displayed map identifying the present \(\Phi^n\) with this \(E^{n-1}\). Such an identification is therefore not inserted into the transcription or treated as proved by the matching adjective. The present specialization sequence and the context hyperplane push–pull formula provide concrete data for a later comparison. CN/CD also preserve doubts in nearby projector formulas, including the inserted \(L/\Lambda\) and marginal \(L?\) at CT 16/40.

### C03 — Projective cone, punctured cone, and primitive pieces

**Current witnesses:** F56/009, 011, 013, 015. **Context:** CT 16/33, 16/40 for primitive projectors; CN 47:8:2/F7 for the separate cone search hit. **Relation:** the current pages add the explicit geometric cone calculation; partial overlap through the displayed Lefschetz operator.

F56/011 names \(C,\widehat C,a,E=C-a,\widehat E=\widehat C-a\) and displays a Gysin sequence whose arrow is multiplication by \(\xi\), with an explicit possible minus sign. F56/013 gives the primitive descriptions of \(H^i(E)\) **mod torsion** and the local-support comparison

\[
H^i_a(C)\simeq H^{i-1}(E)\quad(i\geq2),
\]

with the support letter itself uncertain in one occurrence. The exact operation connecting this to CT 16/33 and 16/40 is again multiplication by the polarization and its primitive kernel/cokernel. The context's formulas do not remove “mod torsion” from the current statement.

CN 47:8:2/F7 discusses a cone used in a derived comparison associated with CT 47/8. No \(C,\widehat C,a,E\) construction was located in that passage. The record retains both actual usages and supplies no unexhibited equivalence between the constructions.

### C04 — Closed support, compact support, and proper support over a base

**Current witnesses:** F56/013, 017, 020, 030. **Context:** CT 47/3; CN 47:3:2–3 and F2; CD 47/3. **Relation:** support terminology hit; the current author poses an additional comparison which remains a question in this local review.

F56/017 has a compact-support heading, uses properness of \(\widehat C\), compares exact sequences, then writes “on est amené à prévoir” and finally

\[
\boxed{H_a^*(C)\simeq H_c^*(C)\quad ??}.
\]

The comparison to examine is the natural map induced by the inclusion of the support family \(\{a\}\) into the family of proper supports on \(C\). Writing this map identifies the question; the question marks on the frozen page do not establish that it is an isomorphism.

CT 47/3 instead explicitly defines the morphism-producing functor

\[
\Phi_{\mathcal L}(F)=\mathbf R\operatorname{pr}_{2*}
  (\mathbf L\operatorname{pr}_1^*F\otimes\mathcal L)
\]

and proposes convolution-to-tensor compatibility. Its long margin allows a flat group scheme and \(F,G\) with supports proper over \(S\). These are the exact objects and maps at the search hit. The examined passage contains no calculation of the above \(H_a(C)\to H_c(C)\) map. Consequently it supplies no resolution of F56/017. F56/020 and 030 provide a further concrete compact-to-ordinary comparison with a factor \(2\); the uncertain target/subscript at 020 remains uncertain.

### C05 — Index two in the middle cohomology lattice

**Current witnesses:** F56/024, 028, 030, 035. **Context:** CT 16/14–15; CN R1–R2 and 16:15:2; CD 16/14–15. **Relation:** the current pages add an explicit integral lattice calculation.

F56/024 explicitly says “d'indice 2” and uses the matrix with columns \((1,1)\) and \((1,-1)\). F56/030 supplies the names:

\[
\xi^\nu=\alpha_\nu+\beta_\nu,
\qquad \lambda_\nu=\alpha_\nu-\beta_\nu,
\qquad \varphi_\nu=\alpha_\nu.
\]

Thus the exact homomorphism of free abelian groups is

\[
\mathbb Z\xi^\nu\oplus\mathbb Z\lambda_\nu
\longrightarrow \mathbb Z\alpha_\nu\oplus\mathbb Z\beta_\nu,
\qquad
\begin{pmatrix}1&1\\1&-1\end{pmatrix},
\]

of determinant \(-2\); its cokernel is \(\mathbb Z/2\). The equality
\(\varphi_\nu=(\xi^\nu+\lambda_\nu)/2\) names an actual integral class in the larger lattice. This calculation explains why the bracketed pair \([\xi^\nu,\lambda_\nu]\) on F56/005 and 028 must be read together with the index annotation. Treating it as an integral basis would discard the displayed lattice map.

F56/030 further records \(\lambda_\nu\mapsto2\ell^{2\nu}\) and \(\varphi_\nu\mapsto\ell^{2\nu}\), with “bij exc. 2”. These maps give a direct local source for the factor two. No change to a source basis or coefficient convention is made here.

### C06 — The integral exterior model: an exact restricted comparison

**Current witnesses:** F56/026, 032, 035. **Context:** CT 16/14–15; CN R1–R2; CD 16/14–15. **Relation:** restates a concrete obstruction at the level of a specified integer homomorphism, and adds geometric witnesses.

CT 16/14 constructs \(\Phi_0\) from an exterior algebra over \(\mathbb Z\) and multiplication/contraction operators. CT 16/15 includes an unrestricted base-ring remark. CN R1 tests the rank-four exterior model with

\[
\xi=e_1f_1+e_2f_2,\qquad\xi^2=2\,\mathrm{vol}.
\]

F56/032 states that the exceptional odd-quadric multiplication map is injective with cokernel \(\mathbb Z/2\); F56/035 writes the divided power basis. For the conic, the map is \(\mathbb Z\cdot1\to\mathbb Z\cdot\xi_1\), \(1\mapsto2\xi_1\). There is an explicit comparison of these rank-one homomorphisms:

\[
\begin{array}{ccc}
\mathbb Z\cdot1&\xrightarrow{L^2}&\mathbb Z\cdot\mathrm{vol}\\
\downarrow\scriptstyle{1\mapsto1}&&\downarrow\scriptstyle{\mathrm{vol}\mapsto\xi_1}\\
\mathbb Z\cdot1&\xrightarrow{\xi\cup-}&\mathbb Z\cdot\xi_1.
\end{array}
\]

Both horizontal maps have matrix \([2]\). This comparison is between the displayed homomorphisms; it does not identify their different graded ambient algebras or compute the full integral order generated by the operators. CN R2's contraction-versus-unweighted-lowering calculation remains an earlier contextual claim to assess in its own specified model. RS **WG2 §6. #9** gains this precise quadric witness; its entire requested programme is not completed by that witness.

### C07 — Two internal consistency questions to retain for the main notes

These are editorial calculations from frozen formulas. They justify questions in the notes and do not authorize a reading change.

**Degree check, F56/011 + 015 + 032.** F56/015 places a \(\mathbb Z/2\) group in \(H^{2(\nu-1)}(E)\) for the odd base quadric \(Q^{2\nu-1}\). Put the parameter of F56/032 equal to \(\nu-1\). Its exceptional multiplication map is then

\[
H^{2\nu-2}(Q^{2\nu-1})(-1)
\xrightarrow{\xi}H^{2\nu}(Q^{2\nu-1}),
\qquad\operatorname{coker}=\mathbb Z/2.
\]

The exact row displayed at F56/011 puts this cokernel in \(H^{2\nu}(E)\), using the adjacent odd-group vanishing recorded in the quadric tables. The compared degrees are therefore \(2\nu-2\) on 015 and \(2\nu\) from that exact row. F56/032 itself contains a source-exponent uncertainty (`2i|i`). Record this as a localized degree/reading consistency question, with all three witnesses, rather than silently replacing the exponent at 015.

**Sign check, F56/024 + 026 + 030.** F56/026 writes \(\lambda_\nu^2=2\xi_{2\nu}=\xi^{2\nu}\). F56/030 writes \(\xi^\nu=\alpha_\nu+\beta_\nu\) and \(\lambda_\nu=\alpha_\nu-\beta_\nu\). At \(\nu=1\), use the \(Q^2\simeq\mathbb P^1\times\mathbb P^1\) reading at F56/024. Let \(a,b\) be the pullbacks of the point classes from the two factors. The product calculation has \(a^2=b^2=0\), with \(ab\) the point class, and the indicated ruling-class assignment sends \(\xi\mapsto a+b\), \(\lambda\mapsto a-b\). It gives

\[
(a-b)^2=-2ab,
\qquad(a+b)^2=2ab.
\]

This explicitly tests the plus sign at 026 against the identifications at 024/030. It leaves the uncertain writing at 024 and any intended coefficient/convention issue visible. No context passage examined resolves that local sign question, and this elementary calculation is not presented as a new mathematical result.

### C08 — Tori, Weyl groups, centres, and reused sheets

**Current witnesses:** F56/004, 006, 008, 012, 014, 016, 018, 021, 023, 025, 027, 029, 031, 033. **Context:** CT 16/30, 47/3, 44/7, 54/8; CN 44:7:1, 54:8:3/D15; CD corresponding pages. **Relation:** the current material adds a named exposé and explicit group-scheme statements; the context supplies more limited thematic/provenance hits.

F56/008 explicitly names exposé XII and A. Grothendieck. F56/029 defines \(W=N/C\), with normalizer and centralizer of the torus, states finite étaleness, and records base change. F56/016 states the comparison from \(R\subset T\) to a quotient of a subgroup of \(W(T)\). F56/023 and 027 give multiplicative/reductive-centre constructions; F56/014 and 033 give maximal-torus representability/local existence arguments. These precise statements supply the current comparison objects.

CT 16/30 is reused typed group-scheme cohomology, involving finite groups, duality, and \(\mathbb G_m\); CT 47/3 extends a convolution transform to flat group schemes. CT 44/7 is a “La Tribu” Coxeter/root text; CT 54/8 is a typed hyperplane-arrangement passage. No action map from the specific \(W=N/C\) at F56/029 to the roots/chambers in those context excerpts is displayed in the inspected passages. The absence of that displayed comparison is the limit of this local search; it asserts no general separation of the subjects.

RS **MPL_15_195-228+18_002-017 R01** is a first-pass reused-sheet provenance lead. The present explicit exposé title/author and the distinct source pagination add evidence of reuse. A motive construction or an identification of a motivic group with this \(W\) is not promoted from coexistence on the packet's sheets.

### C09 — Delzant, degree-two classes, and Brauer context

**Current witnesses:** F56/036–039. **Context:** CT 16/21, 16/23; CN 16:21:3, 16:21:6, 16:23:2, 16:23:4, R8; CD 16/21, 16/23. **Relation:** a Brauer-group hit, with added authorship and integral-degree-two evidence.

F56/036–038 are a printed note by Antoine Delzant on Stiefel–Whitney classes of a quadratic module, including degree-two classes, quaternion constructions, and a Brauer-group comparison. CT 16/21 displays the Néron–Severi / \(H^2(-,\mathbb Z_\ell[1])\) / Tate-module-of-Brauer sequence; CT 16/23 uses an intersection form and an integral discriminant criterion. These are exact source locations for the common degree-two/Brauer vocabulary. No morphism identifying all of Delzant's invariants with the context sequence is supplied in the examined excerpts. CN R8's distinction between finite torsion data and a rationalized quotient is an earlier research claim with its own calculation; the offprint's displayed mod-two data should remain available for a precise comparison.

## 3. Author's flags and their local continuations

This is a selected register within the assigned scope. “Followed by an argument” describes the page's structure and does not certify every step of the argument.

| Frozen witness | Literal status evidence | Treatment in integration |
|---|---|---|
| F11/048 | `Il faut encore \unsure{définir\|vérifier}` associativity of \(\bullet\) and the unit role of \(\delta_I/\Delta_I\). | Preserve the postponed step and the verb uncertainty. |
| F11/057, first marginal flag | `! vérifier` followed by `OK` beside the equality case. | Report both marks together. The local OK cannot be extended to every later case. |
| F11/057, second marginal flag | A second `! vérifier`, without a neighboring OK, beside the ensuing calculation. | Keep the separate location open in the author's flag register. |
| F56/008 | Inserted claim that later numbers remove affine hypotheses; final margin says exposés XI, XII, XV, XVI `devrait être complètement refondu`. | A revision/programme statement on the reused exposé; keep the uncertain upper number in N°s 6–8. |
| F56/012 | `On verra au N°5` for affineness of the maximal-torus prescheme; alternate proof refers to XI 3.12 and 6.2 and finite multiplicative groups \({}_nT\). | Record the forward reference and cited dependencies. The broad later representability discussion is deleted and must remain deleted. |
| F56/014 | `Il reste à vérifier ... de type fini ... !\|?`, then a local argument using the map from \(G\) to the torus parameter scheme. | Record the flag and its following argument together, rather than labeling the whole statement unanswered merely from that opening sentence. |
| F56/017 | `on est amené à prévoir`; boxed \(H_a^*(C)\simeq H_c^*(C)\) followed by `??`. | Explicit author question; C04 gives the map to examine and the bounded context result. |
| F56/020 | `Je m'y perds, ces deux sont définis à un signe près`; target/subscript uncertainty; `exc. 2`; questions for degrees \(0,1,n,n+1\). | Follow through 022, 030, 032 for the later tables and factor two, while retaining the original sign/notation flag. |
| F56/021 | `nous nous bornons à une esquisse` of the proof of Lemma 2.2; EGA references; page ends after `corps résiduel`. | F56/016 begins `algébriquement clos` and continues the complete-DVR argument. Its typed source numeral `160\|16a` and 021's uncertain `15` are recorded below. Read this continuation alongside the stated proof-sketch scope. |
| F56/027 | `ce qui achève de prouver 4.3`; future exposé XIII mentioned for a further decomposition. | Retain the asserted completion of 4.3 and the distinct forward reference. |
| F56/032 | Source exponent `2i\|i` in the odd-quadric multiplication map. | Preserve the reading uncertainty in the degree check C07. |
| CT 16/14 | A `Question` asks for relations in \(L,\Lambda\); exterior model is declared over \(\mathbb Z\). | Use CN R1–R2 as prior calculations, not silent amendments to the model. |
| CT 16/40 | Deleted `équivaut`, inserted `implique` for \(C(X)\to C(Y)\); inserted \(L/\Lambda\), margin \(L?\). | Preserve the direction correction and the unresolved operator. CN/CD record the same locations. |
| CT 47/9 | `ces formules sont-elles bien vraies mod torsion?` following Chern expansions. | An explicit context question. The current quadric factor two supplies an example of integral sensitivity, but no displayed identification with that formula settles the question. |

## 4. Titles, counts, attribution, and reuse

### 4.1 Current title and extent witnesses

| Source | Frozen title or imprint evidence | Count/provenance conclusion supported by this selection |
|---|---|---|
| F56/002 | `Situation des ``vanishing cycles'' ; \unsure{irréductibilité} Cas des Quadriques`; margin `\unsure{3 p\|30}`; sequence marker 1. | The three selected handwritten mathematical pages are 003, 005, 007. Their count agrees with the `3 p` alternative, while the uncertain alternative remains in the transcription. |
| F56/009 | `Calculs de cohomologie des quadriques, des cônes projetants`; margin `\unsure{12 p}`; sequence marker 8. | The twelve selected handwritten pages are 011, 013, 015, 017, 020, 022, 024, 026, 028, 030, 032, 035. This checks the count within the selected packet. |
| F56/008 | `XII` and the title on maximal tori, Weyl group, Cartan subgroups, and reductive centre of smooth affine group schemes; `par A. Grothendieck`; source page 0. | Explicit attribution of this exposé. It names Chevalley's 1956/57 seminar and the exposé references denoted BIBLE. Those references date the cited material; this review does not derive a date for all handwriting from them. |
| F56/036 | Printed title on Stiefel–Whitney classes of a quadratic module over a field of characteristic different from 2; Antoine Delzant; communicated by Jean Leray. | Explicit authorship of the printed note. Keep it available when discussing the physical source's mixed authorship. |
| F56/037–038 | Internal printed numerals `(2)`, `(3)`, alongside packet sequence markers 36, 37. | Three content pages of the offprint are selected at 036–038. |
| F56/039 | *Comptes rendus*, t. 255, pp. 1366–1368, séance du 10 septembre 1962; Gauthier-Villars imprint; printer number 162396. | The cited printed span has three pages; scan 039 adds the selected imprint page. The explicit date belongs to this offprint witness. |
| F11/043–058, selected scans | Eight reused typed pages have internal labels `-3.7-`, `-3.6-`, `-3.4-`, `-3.3-`, `-3.18-`, `-3.17-`, `-3.15-`, `-3.14-`; material on \(\mathrm{PGL}(n)\), configurations, stability, and quotient constructions. | The selected inventory contains no cote-11 cover. These internal labels and packet sequence numbers record selected extent and ordering; they do not reconstruct a complete original typescript or establish an unprinted author name. |

The selected package contains **50 source pages: 15 in cote 11 and 35 in cote 56**. The inventory's page-level classes total **22 text, 24 reused typed/printed, 2 covers, 2 cancelled drafts**. Those are counts of selected scans, not a claim that the historical documents each had that total extent.

The two cover counts are unusually concrete additions to the supplied RS title-count lead, **MPL_15_195-228+18_002-017 §136**. That earlier entry reports its own earlier selected title sheets. The present readings do not amend the earlier packet's count; they add the above witnesses for this packet.

### 4.2 Context provenance comparisons

| Exact context location | Evidence | Use here |
|---|---|---|
| CT 16/35; CN 16:35:1; CD 16/35 | Printed `Cohomologie des catégories de Banach`, `par Max Karoubi`. | A concrete contextual example in which a reused text supplies its own author/title. |
| CT 47/2; CD 47/2 | Cover on convolution product and Fourier transform on abelian varieties; source page 1. | A prior cover witness; it supplies no count for the present quadric packet. |
| CT 54/2; CD 54/2 | Cover on duality in cohomology of abelian varieties, with uncertain words; source page 1. | Preserve the supplied title uncertainty in any concordance. |
| CT 54/8; CN 54:8:3 and D15; CD 54/8 | Reused typed hyperplane-arrangement text, printed `-13-`, number 391; CN records its orientation/reuse. | A concrete reused-text provenance comparison. No assertion of a shared physical parent document follows from this alone. |
| CT 44/7; CN 44:7:1; CD 44/7 | `Commentaires`, La Tribu no. 57, Coxeter/root/coroot vocabulary. | Records the actual source of the root-theoretic context hit used in C08. |

### 4.3 Complete selected-page foliation register

The following register transcribes the number markers already encoded in the frozen files. “Sequence” is the observed marker equal to scan minus one; the name does not attribute that marking to a particular historical hand. “Additional source marker” records the separate typed/printed/overwritten numeral. Neither column is a reconstructed total page count. Cover annotations and the extra uncertain margin on 56/027 are listed separately. All uncertainty and deletion macros are retained literally.

| Frozen source | Inventory class | Sequence marker | Additional source marker(s) | Other count/number annotation |
|---|---|---|---|---|
| F11/043 | reused_typed | `42` | `-3.7-` | — |
| F11/044 | text | `43` | — | — |
| F11/045 | reused_typed | `44` | `-3.6-` | — |
| F11/046 | text | `45` | — | — |
| F11/047 | reused_typed | `46` | `-3.4-` | — |
| F11/048 | text | `47` | — | — |
| F11/049 | reused_typed | `48` | `-3.3-` | — |
| F11/051 | text | `50` | — | — |
| F11/052 | reused_typed | `51` | `-3.18-` | — |
| F11/053 | text | `52` | — | — |
| F11/054 | reused_typed | `53` | `-3.17-` | — |
| F11/055 | text | `54` | — | — |
| F11/056 | reused_typed | `55` | `-3.15-` | — |
| F11/057 | text | `56` | — | — |
| F11/058 | reused_typed | `57` | `-3.14-` | — |
| F56/002 | cover | `1` | — | `\unsure{3 p\|30}` |
| F56/003 | text | `2` | — | — |
| F56/004 | cancelled_draft | `3` | `\unsure{63\|68}` | — |
| F56/005 | text | `4` | — | — |
| F56/006 | cancelled_draft | `5` | `1` | — |
| F56/007 | text | `6` | — | — |
| F56/008 | reused_typed | `7` | `0` | — |
| F56/009 | cover | `8` | — | `\unsure{12 p}` |
| F56/011 | text | `10` | — | — |
| F56/012 | reused_typed | `11` | — | — |
| F56/013 | text | `12` | — | — |
| F56/014 | reused_typed | `13` | `\unsure{84\|82}` | — |
| F56/015 | text | `14` | — | — |
| F56/016 | reused_typed | `15` | `\unsure{160\|16a}` | — |
| F56/017 | text | `16` | — | — |
| F56/018 | reused_typed | `17` | `\deleted{\unsure{58}}4` | — |
| F56/020 | text | `19` | — | — |
| F56/021 | reused_typed | `20` | `\unsure{15}` | — |
| F56/022 | text | `21` | — | — |
| F56/023 | reused_typed | `22` | `23` | — |
| F56/024 | text | `23` | — | — |
| F56/025 | reused_typed | `24` | `\unsure{10\|19}` | — |
| F56/026 | text | `25` | — | — |
| F56/027 | reused_typed | `26` | `21` | `\unsure{03}` |
| F56/028 | text | `27` | — | — |
| F56/029 | reused_typed | `28` | `\unsure{12}` | — |
| F56/030 | text | `29` | — | — |
| F56/031 | reused_typed | `30` | `26` | — |
| F56/032 | text | `31` | — | — |
| F56/033 | reused_typed | `32` | `\unsure{37\|31}` | — |
| F56/035 | text | `34` | — | — |
| F56/036 | reused_typed | `35` | — | — |
| F56/037 | reused_typed | `36` | `(2)` | — |
| F56/038 | reused_typed | `37` | `(3)` | — |
| F56/039 | reused_typed | `38` | — | — |

## 5. RESULTS_STATE mapping and status control

The following is an integration map, not a rewritten results register. “Retain” means retain the supplied status with its qualification. The new local evidence is stated in the middle column.

| Exact RS entry ID | Present evidence or explicit limit | Status treatment |
|---|---|---|
| **LM7 E.23** | The supplied entry concerns section classes for geometric metabelian/marked depth-two arithmetic quotients of \(U_3/\mathbb Q\). The direct-term search above found no selected-page witness for those objects or their section maps. No map from the present quadric, cone, or group-scheme constructions to that section-class calculation was found in the inspected passages. | Retain **Open (the return's claim)**. No promotion and no claim of mathematical independence. |
| **LM7_PUSH D.44** | The supplied entry concerns \(\widehat B=C_2\amalg C_3\), its kernel to \(\mathfrak S_3\), and the specified generators \(\tau=sr\), \(x=\tau^{-2}\), etc. These direct strings/objects have no located witness in the selected pages. | Retain **Proved (the return's claim; the parts used by D.50 and E.58 refereed as claimed on 14 Nov)**. This concordance adds no proof or upgrade. |
| **WG2 §2.4 #3** | C01–C06 supply explicit polarization, Gysin, primitive, and integral examples. The selected reused exposé's group schemes do not by themselves supply a functor constructing the category of motives from the cote-16 correspondence rings. | Retain **unchecked question/plan**; add exact source witnesses only. |
| **WG2 §6. #9** | C05–C06 supply the index-two matrix, a rank-one map of matrix \([2]\), and the comparison to CT 16/14/CN R1. The full universal property, all eight formulas, and the integral orders through the requested ranks are not computed here. | Retain **unchecked question/plan**. A concrete local calculation does not promote the whole prompt. |
| **WG2 §2.2 #4** | C01 identifies the precise hyperplane maps and points to CT 16/33, 40, 42, 45–46. The quadric tables add a specific family of examples. | Retain **unchecked planning account**; no proof of the general flag induction supplied by this local comparison. |
| **WG2 §2.3 #2** | CN R1–R2 and current integral classes make coefficient/normalization questions concrete. This review gives no identification of the full rational operator algebra with all the matrix factors named by the RS entry. | Retain **unchecked question/plan**. |
| **WG2 §2.3 #7** | No proof of the listed general semisimplicity or nilpotence assertions is supplied by the calculations here. The full external sources named by the entry were not reread for this local concordance. | Retain the **unchecked** supplied entry; do not turn a register excerpt into a theorem verified here. |
| **WG H9**; **WG2 §2.3 #12** | CT 44/4 and its CN entries supply the hyperplane/pencil/height context hit. The present quadric maps provide no displayed identification with the general height-pairing formula in these RS entries. | Retain **hunch/unchecked** and **unchecked plan**, respectively. |
| **MPL_15_195-228+18_002-017 R01** | C08 and §4 add explicit reused-sheet titles, author names, source pagination, and group-scheme witnesses. The exact omitted map is recorded where a motivic identification would be needed. | Retain **first-pass research lead**. |
| **MPL_15_195-228+18_002-017 §136** | §4 adds uncertain cover readings `3 p\|30`, `12 p`, matching selected handwritten counts, and all 50 marker records. | Retain **first-pass research lead** for the earlier packet; attach the new packet's evidence. |
| **MPL_14_002-044 §101** | §3 adds the present postponed associativity/unit check, two verification flags, support comparison question, sign doubts, and group-scheme forward references. | Retain **first-pass research lead**; these locations extend a register, not settle its prior entries. |
| **MPL_14_087-132 M01**; **MPL_14_002-044 M01**; **MPL_15_195-228+18_002-017 M01**; **MPL_14_002-044 §2**; **MPL_15_195-228+18_002-017 §2** | Rings/categories and motive-construction leads. The principal transcriber is integrating the full cote-11 correspondence material; this assigned concordance supplies the exact quadric/operator maps and provenance limits. | Retain the supplied **first-pass lead** status. No promotion from shared terminology. |
| **MPL_14_002-044 M27**; **MPL_14_087-132 M04**, **M05**, **M09** | Motivic-group action, gradings, and semisimplicity leads. No additional action morphism or equivalence proving these claims is constructed by C01–C09. | Retain the supplied **first-pass lead** status and the original qualifications. |

## 6. Integration priorities and limits

The source additions most useful for the main notes are the explicit hyperplane comparison C01, the index-two homomorphism C05, the restricted integral-model comparison C06, the author's support question C04, the two internally localized checks C07, and the title/foliation evidence in §4. The full mathematical status of the earlier CN and RS assertions requires their actual arguments and conventions; this local record does not certify them collectively.

The provenance record establishes what the selected text itself names: Grothendieck's exposé XII on one reused sheet, Delzant's printed note and its 1962 imprint, the two uncertain cover counts, and multiple sequences of page numerals. It does not use the contextual material to supply missing letters or reorder frozen readings. No image, OCR output, or unopened source return was used in this review.
