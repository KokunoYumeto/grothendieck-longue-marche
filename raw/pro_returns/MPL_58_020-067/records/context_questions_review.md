# Context-question review: cote 47 and the seven theorems of cote 44

Research working report, 17 November 2026. Prepared after the transcription freeze at **2026-11-17 13:41:05 UTC**. No manuscript image was opened in this review, and no page transcription or combined transcription was edited. The historical quotations below are readings of the **supplied first-pass context transcription**, not a new palaeographical verification.

## 1. Findings and their limits

**No second witness of cote 47 with the unit-fibre compatibility check completed was located in the supplied materials.** The context transcription preserves the unfinished sentence at **47:8**, while its subsequent scans 9–11 move to other calculations. The context research notes explicitly distinguish their proposed proof plan and Koszul calculation from a proof that the manuscript's particular comparison map is an isomorphism. Nothing identified in the frozen cote 58 packet supplies that missing verification. This is a finding about the material supplied for this task, not a claim that no such witness exists elsewhere in the archive or in published mathematics.

**The supplied cote 44 context already contains a second formulation of part of its programme:** the letter headed **“Bures le 12.8.1964”**, addressed **“Mon cher Serre,”** at **44:8–9**. It has direct parallels with Theorems 2–4 and a related quotient construction for Theorem 1. It does not restate all seven theorems. The supplied *Programme de travail* itself is undated; the letter's date therefore does **not** establish whether the letter precedes or follows that programme. The letter is an already supplied parallel formulation, not a discovery in the new cote 58 packet.

**The new cote 58 packet concerns formal comparison, Lefschetz–Grauert properties and their applications to fundamental groups and Picard groups.** Its line-bundle restriction statements at **58:40–41** are relevant background for a Lefschetz theme, but they do not reproduce the intermediate-Jacobian assertions of cote 44, including the three-range assertion of Theorem 6. No earlier form of Theorems 1–7 was identified here.

## 2. Source inventory and evidential status

All paths in this table are relative to `/workspace/scratch/83e74abf5a7c/`. Scan locators are the `\cotefile{...}` and `\scanpage{...}` divisions in the named transcription. They are preferable to inferred manuscript pagination, especially because the context cote 44 packet includes reused and cancelled leaves.

| Source | Exact locator used | Evidential role |
|---|---|---|
| `context_opened/README.md` | “What our planning document asks of these folders”; “What is in this zip” | Defines the carry-question and says the old transcriptions, notes and research returns are claims unless a check is explicitly recorded. |
| `context_opened/notes/RESULTS_STATE.md` | Opening “Status”; “Orientation for this package”; war-game entries listed in §7 below | Supplies IDs and their stated status. Its orientation says “Our results to use and check: none for this cote.” |
| `context_opened/MPL_16+47+54+44_transcription.tex` | Cote 47, scans 2–11; cote 44, scans 2, 4, 6, 8–9 | Supplied first-pass textual witness for the relevant manuscript content. Cote 47 scans 3–11 and the whole cote 44 block were read. |
| `context_opened/MPL_16+47+54+44_notes.md` | F6–F8; D08–D14 | Earlier run's own interpretations and literature comparisons. They are not independent manuscript witnesses or referee verdicts. |
| `context_opened/MPL_16+47+54+44_doubts.md` | Rows for 47:8 and 44:2, 44:4, 44:6, 44:8–9 | Preserves unresolved readings, notably the complementary index in Theorem 3, the exponent and pairing indices in Theorem 5, and the scope of notation in the letter. |
| `MPL_58_020-067_work/MPL_58_020-067_transcription.tex` | Frozen supplied scans 20–67, with gaps in supplied scan numbering; especially 28, 32–33, 38–44, 46–52, 65–67 | New packet, read only. Targeted passages and keyword results were compared with the two context questions. |
| `context_opened/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf` | Printed pp. 63–67 and 131; PDF pages 2–6 and 70 | Printed mathematical comparison. PDF skill was read before use. Printed p. 63 and p. 131 were also rendered and inspected; no manuscript images were used. |

The context's Hua material is another project's modernized reading of cote 58, not a second witness of cote 47 or cote 44. Its full review is being handled separately by the main researcher; no substantive claim below depends on that modernization.

## 3. Cote 47: exactly what remains unfinished

### 3.1 Manuscript sequence in the supplied transcription

The title at **47:2** identifies convolution and Fourier transformation on abelian varieties. Scans **47:3–5** develop the integral transform, its relation to the two products and its inversion calculation; the derived version includes inversion, shift and the determinant/tangent factor. At **47:6**, Lemma 1 supplies the key direct-image assertion for the Poincaré bundle. The preceding inversion argument is explicitly dependent on that lemma: **“modulo dém. du Lemme 1.”**

At **47:7**, Lemma 2, attributed in an insertion to Mumford, is the vanishing of the cohomology of a nontrivial algebraically trivial line bundle over an algebraically closed field. The transcription explicitly says **“Nous allons ici admettre le lemme 2”**. The author then constructs the canonical map

\[
\mathbf Rp_*(W)\longrightarrow e_*(\mathcal O_S)\otimes_S\tau_{B^*}[-n].
\]

The construction passes through top cohomology and the identification

\[
R^nq_*\mathcal O_B\simeq\Lambda^nR^1q_*\mathcal O_B
\simeq\Lambda^nt_{B^*},
\]

with **“l'hom identique”** chosen for the determinant line. At **47:8**, the author reduces the isomorphism assertion to the induced maps on derived fibres. Away from the unit section, the admitted vanishing lemma applies. At a unit point $e(s)$, the text reduces to an algebraically closed field and stops at:

> “à faire une vérification de compatibilité.....”

The next heading on the same scan is **“Remarques 1)”**. The remaining material at **47:8–11** discusses transforms of sections and algebraically trivial line bundles, rank and Euler characteristics, a Picard-group determinant map, Chern/Riemann–Roch formulae, and automorphism compatibility. It does not return to complete the unit-fibre comparison. A separate uncertainty at **47:9**, **“ces formules sont-elles bien vraies mod torsion?”**, should not be conflated with the unfinished comparison at 47:8.

For precise navigation in the current context file, the relevant scan blocks begin at lines **2333** (47:7), **2380** (47:8), **2420** (47:9), **2472** (47:10) and **2528** (47:11). These line numbers are working-file aids; the stable citation is the filename plus cote and scan.

### 3.2 What the earlier run did and did not claim

The earlier notes already recognize this boundary:

| Context note | Supplied status | What it contributes | What it expressly does not establish |
|---|---|---|---|
| F6, 47:7 | “Kind: unproved claim” | Locates the vanishing statement in Mumford and explains its support consequence. | Vanishing away from the unit does not determine the scheme structure, degree, determinant twist or the particular comparison map at the unit. |
| F7, 47:8 | “Kind: own idea”; “Editorial proof plan” | A perfect-complex cone and derived-fibre criterion isolates the needed test. | It says the remaining task is to show that the **particular map** induces the required isomorphisms at the unit, beyond equality of cohomology dimensions. |
| F8, 47:7–8 | “Kind: own idea”; “Editorial calculation” | A local Koszul computation matches the exterior-power dimensions with the determinant and shift retained. | It explicitly stops short of **“completing the compatibility of the actual comparison map.”** |

These are helpful analytical leads, but no item is a supplied second historical witness or a completed comparison-map proof. The outside references mentioned by F6–F8 were **not independently rechecked in this focused review**; the point here is the earlier notes' explicit description of their own limited claim.

### 3.3 Contribution of cote 58

No Fourier-transform, convolution, Poincaré-kernel or unit-fibre calculation was identified in the frozen cote 58 text. The packet contains formal-completion comparison problems, with locally free or coherent sheaves and depth conditions. The symbol $\Phi$, used for a support family in the local argument, is not the Fourier functor of cote 47. This source therefore supplies no completed second witness to add to **WG2 §2.4 #4**.

## 4. Cote 44: seven-theorem comparison

The *Programme de travail* begins at **44:2**. Theorems 1–4 are there; Theorems 5–6 are at **44:4**; Theorem 7 is at **44:6**. The letter at **44:8–9** is separately and explicitly dated **12 August 1964**. Its numbering $J^i$ differs from the programme's $P^i$; the correspondence below is a comparison of content, not a declaration that all definitions or universal properties coincide.

| Theorem | Programme statement and exact locator | Already supplied parallel at 44:8–9 | Assessment and limit |
|---|---|---|---|
| **1** | **44:2**, “Th. 1”: $N(\xi)\subset\operatorname{Alb}(S)$ is, with inserted qualification **“en substance”**, the kernel of the natural map to cycles modulo “alb/ab” equivalence. The argument of $N$, the cycle alphabet and the equivalence subscript retain doubts. | **44:9**, middle: a divisor correspondence $D$ on $T\times T$ descends to $A=\operatorname{Alb}^0(T)$; $N$ is the kernel of the map from $A$ to its dual, and $J=A/N$. **44:8**, first paragraph, names “équivalence d'Albanese” provisionally. | Related kernel/quotient construction, especially in the middle-dimensional positivity problem. The letter does not explicitly identify this kernel with the exact cycle-class map in Theorem 1. |
| **2** | **44:2**, “Th. 2”: $\dim(\operatorname{Alb}(S)/N(\xi))$ is bounded in terms of $X$, with bracket **“en fait, par $\frac12 b^{2i-1}(X)$ !”** | **44:8**, first paragraph: $\dim J^i\leq\frac12 b_{2i-1}$, followed by Tate-module and Hodge-cohomology expectations. | Direct parallel for the half-Betti bound. The letter's date gives an absolute date for this formulation, not priority over the undated programme. |
| **3** | **44:2**, “Th. 3”: $Z^i_{\rm alg}(X)/Z^i_{\rm alb}(X)=P^i(X)$ has a natural abelian-variety structure and a canonical complementary duality. The exponent is explicitly uncertain between $n-i$ and $n+1-i$. | **44:8**, first paragraph: abelian varieties $J^i(X)$, endpoints $J^1=\operatorname{Pic}^0$, $J^n=\operatorname{Alb}^0$, and canonical duality of $J^i$ and $J^{n+1-i}$. | Strong parallel, but the letter explicitly says the equivalence relation is not yet well identified. Its clear complementary index is comparison evidence, not permission to repair the uncertain programme transcription. |
| **4** | **44:2**, “Th. 4”: if $n=2m-1$, canonical self-duality of $P^m$ is associated to a polarization. Margin: **“Connu tel quel”**, **“Hodge”**. | **44:8**, final paragraph, and **44:9**, opening: positivity of the self-duality of $J^m$ means an ample Néron–Severi class, hence a polarization. **44:9**, middle, gives the divisor-correspondence construction and says **“A prouver que cette dernière est positive !”** | Strong parallel with a more explicit construction. The letter calls the positivity assertion unproved and makes its reduction conditional. The programme's margin cannot independently date the programme or supply a proof. |
| **5** | **44:4**, “Th. 5”, margin **“Néron”**: for complementary-codimension cycles whose restrictions to a generic pencil member are algebraically trivial, a Néron–Tate pairing is asserted to equal $(-1)^m Z\cdot Z'$. The page cancels **“au signe près ??”** and proposes a more general fibration statement with a local variant. | No explicit Néron–Tate/intersection formula in the supplied letter. The Hodge-positivity discussion is related motivation only. | No earlier form of this precise theorem located. The exponent $m$, revised dimensions and pairing indices remain features/doubts of the supplied reading, not normalized here. |
| **6** | **44:4**, initially “Cor.” then “Th. 6”, margin **“Lefschetz”**: restriction $P^i(X)\to P^i(Y)$ is an isomorphism for $2i\le n-1$, its image is the fixed factor for $2i=n$, and it is surjective for $2i\ge n+1$. A finite-kernel clause is cancelled. | None of these three range statements occurs in the supplied letter. | No earlier form located. Cote **58:40–41** supplies line-bundle/Picard restriction machinery under explicit formal-comparison and cohomological-vanishing hypotheses; it does not reproduce this arbitrary-codimension fixed-factor theorem. |
| **7** | **44:6**, “Th. 7”: **“L'équivalence numérique = τ-équivalence”**, for algebraic cycles on a nonsingular projective $X$; marginal attribution read uncertainly as **“Matsusaka”**. | No corresponding theorem in the supplied letter. Matsusaka is mentioned at **44:9** as a possible person to ask about positivity, a different question. | No earlier form located. The common personal name does not turn the positivity question into a witness of Theorem 7. The meaning and scope of $\tau$ remain separate interpretation questions. |

### 4.1 Date and proof status of the letter

The following two essential status quotations are in the first paragraph of **44:8**:

> “une relation d'équivalence que je ne sais pas bien identifier pour l'instant”

> “je n'ai pas prouvé grand-chose dessus pour l'instant”

The proposed Hodge-positivity reduction is introduced with **“Moyennant un certain nombre de choses non prouvées”**, and its target is an assertion **“que je ne sais pas prouver”**. The positivity request continues to **44:9**. It is therefore inaccurate to summarize the letter as a complete proof of the programme, or to equate tentative construction language with an established universal algebraic representative.

At **44:9**, the concrete construction is

\[
D=r_*(p^*z\cdot q^*z),\qquad
A=\operatorname{Alb}^0(T),\qquad
N=\ker(A\longrightarrow A^\vee),\qquad J=A/N.
\]

The source treats $D$ as a symmetric divisor correspondence and asks for positivity on the quotient. It also suggests a family $T=\operatorname{Pic}^0(Y)$ with $Y\subset X$ of codimension $m-1$. This explains the relation to Theorems 1 and 4 without filling in missing identifications or ampleness arguments.

### 4.2 Earlier-run interpretations remain distinct

The old notes **D08–D14** give modern comparisons, not earlier historical witnesses. Their own labels are materially qualified: D08 is a comparison requiring a universal property; D09 a later codimension-two proof; D10 a hypothesis-dependent Tate-module comparison; D11 an obstruction to one possible identification; D12 a proposed height identity with comparison in another setting; D13 an editorial positivity test rather than a resolution; D14 a valid divisor comparison with contrary evidence for an unrestricted interpretation under a specified meaning of $\tau$. Those cited papers have not been re-audited in this focused genealogical review. None should be represented as showing that all seven programme assertions are proved, or that the new cote 58 packet contains their earlier drafts.

## 5. What cote 58 actually supplies to these questions

The closest positive connection is **58:40**, headed “Proposition”, and its continuation at **58:41**. Under $(LG)$, it asserts injectivity from Picard groups to the formal completion; the strict condition yields a neighbourhood-limit isomorphism. For a Cartier divisor with associated line bundle $\Lambda$, vanishing of $H^1(Y,\Lambda^{-n})$ for positive $n$ gives injectivity to $\operatorname{Pic}(Y)$, while the added $H^2$-vanishing and strict hypothesis give the corresponding existence/isomorphism assertion. The lemma at 58:41 interprets this by line bundles on the formal completion and on $Y$.

This is a concrete tool relevant to the general Lefschetz setting. It is not the full Theorem 6 of cote 44: no $P^i$ of arbitrary cycle codimension, no intermediate-Jacobian fixed factor, and no three-range dimension statement is supplied here. The permanence “Théorème 1” starting at **58:41** is also a different theorem: projective-flat permanence of $(LG)_n$, not the kernel assertion numbered 1 at 44:2.

The Picard diagrams at **58:65–67** concern cones and restrictions of line bundles. “Jacobson” at **58:48, 50** concerns schemes and is a false keyword hit for the Jacobian question. These distinctions prevent the planning document's broad subject classification from being promoted into evidence for the specific research-end questions.

Search scope: the frozen combined text was searched for Fourier, Pontryagin, Poincaré, Albanese, Jacobian/Jacob-, Néron, Matsusaka, Hodge and compatibility/Picard vocabulary; relevant matches and neighbouring formal-comparison passages were read. This method is bounded by the frozen transcription and its explicit doubts. It does not claim to have searched unsupplied scans, the complete Montpellier archive, correspondence editions, or all later literature.

## 6. Oda's printed paper: useful comparison, not the requested witness

Oda's title, contents and introduction identify the subject as the first de Rham cohomology group, Cartier duality, Dieudonné modules and Picard schemes. In particular, **Corollary 5.11, printed p. 131 (PDF p. 70)** gives the Dieudonné-module comparison for an abelian variety over a perfect field of positive characteristic, with the associated exact sequence matching the Hodge sequence. **Corollary 5.12**, on the same printed page, concerns the comparison involving the Picard scheme of a smooth proper scheme. The paper's **Theorem 1.1, printed p. 67**, concerns Cartier duality for kernels of isogenies.

Those are substantial abelian/Picard comparisons, but they are different constructions from the Poincaré direct-image map at **47:7–8**. The reference immediately following Corollary 5.11 to Grothendieck's conjecture is bibliographic item **[15]**, the 1966 paper on de Rham cohomology; it is not an identification with cote 47. No occurrence of a Fourier/Pontryagin transform or completion of the specific 47:8 compatibility test was located in the printed text inspected/searchable here. Nor does the paper provide a dated earlier form of the seven-theorem Jacobian programme.

Verified bibliographic reference (APA):

Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l'École Normale Supérieure, 4e série, 2*(1), 63–135. https://doi.org/10.24033/asens.1175

Primary publisher/archive record opened: <https://www.numdam.org/item/ASENS_1969_4_2_1_63_0/>. Research-tool source reference: **`turn5view0`**. This record supplies author, title, journal, year, volume, issue, pages and DOI, and identifies bibliography [15]. The final-answer author should open the source independently before citing this child-agent web reference, as required by the search-tool citation instructions. No further web source was used for the conclusions in this review.

## 7. Connections to the supplied results register

| Exact ID in `context_opened/notes/RESULTS_STATE.md` | Supplied status | What this review changes or does not change |
|---|---|---|
| **WG2 §2.4 #4** | “question or plan item of the war game (round 2; unchecked)” | The direct target: no completed second witness of 47 and no earlier forms of all seven theorems found in the new 58 packet. The already supplied 44:8–9 parallel can be indexed more precisely, with chronology left open. |
| **WG2 §1.1 #3** | “question or plan item … (round 2; unchecked)” | The first Book II package drew cotes 16, 44, 47 and 54 from different archival folders. This grouping is planning context; it does not establish that cote 58 contains the same research-end arguments. |
| **WG2 §2.3 #12** | “question or plan item … (round 2; unchecked)” | Its synopsis of Theorems 2–5 is useful as a question index. The supplied programme still has an uncertain complementary index at 44:2 and proof-status qualifications. No new proof is supplied here. |
| **WG H9** | “hunch of the war game (Believe; unchecked)” | The claimed height/Hodge-index interpretation of cote 44 Theorems 4–5 is neither proved nor refuted by failure to find an earlier witness in cote 58. The letter confirms that a positivity reduction was being contemplated, while explicitly calling its prerequisites and positivity assertion unproved. |
| **MPL_43_094-142 A01** | First-pass research-note lead | A generalized-Jacobian question about other scans, represented here by a digest. It is not an included second witness of cote 47 or a genealogy of the seven theorems. |
| **MPL_136_095-141 1.5**, **MPL_136_189-234 R008**, **MPL_136_235-281 N16** | First-pass research-note leads | Abelian varieties on reused typescript are mentioned in these digests. No underlying completed Fourier comparison or earlier seven-theorem text is supplied by these entries. |

The register's **LM6 F.6** is an open higher-dimensional anabelian sufficiency/reduction question. Its possible relationship to Lefschetz tools is separate from these two witness questions. None of the register's “Proved”, “Known” or “Open” rows identified here settles the requested historical comparison, and no status has been edited.

## 8. Suggested compact notes for the main research deliverable

### Witness question for cote 47

**Kind: context comparison / unresolved witness search.** Cote 58:20–67 supplies no second Fourier-transform witness. In the already supplied `MPL_16+47+54+44_transcription.tex`, cote 47:7 admits Lemma 2 and cote 47:8 leaves the unit-fibre comparison at “à faire une vérification de compatibilité.....”; scans 9–11 do not return to it. The old notes F7–F8 explicitly stop short of completing the particular comparison map. Thus **WG2 §2.4 #4** remains unresolved within these supplied materials; this is not an archive-wide absence claim.

### Forms of the Jacobian programme

**Kind: context comparison / chronology unresolved.** The new cote 58 pages do not yield earlier forms of cote 44 Theorems 1–7. The already supplied cote 44:8–9 letter, headed “Bures le 12.8.1964” and addressed to Serre, parallels Theorems 2–4 and supplies a related kernel/quotient construction for Theorem 1, but no versions of Theorems 5–7. Since the supplied *Programme de travail* is undated, neither priority nor a complete seven-theorem genealogy is established. The letter expressly states its unproved status, so this comparison does not settle **WG H9** or the programme synopsis **WG2 §2.3 #12**.

### Limited positive relation of cote 58

**Kind: unpursued implication.** Cote 58:40–41 develops Picard restriction by formal comparison and vanishing of negative normal powers. This is a relevant Lefschetz tool, but it does not state the arbitrary-codimension $P^i$ restriction/fixed-factor theorem numbered 6 at cote 44:4. Calling it an earlier form of that theorem would require an identification and chronological evidence absent from the supplied packet.

## 9. Preservation and exclusions

This report is an independent research record. It incorporates only brief quotations and source locators; it does not reproduce any supplied source file. Temporary extraction/rendering of the printed Oda PDF was kept outside the work package. No old-context text or formula has been substituted into the frozen cote 58 transcription, and no manuscript image was consulted during this review.
