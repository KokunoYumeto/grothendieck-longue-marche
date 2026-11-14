# MPL_152+120 — Research notes

## Scope, evidence and reading conventions

These notes accompany the complete diplomatic transcription of **cote 152, PDF scans 1–13, followed by cote 120, PDF scans 1–25**. The transcription was frozen at **2026-11-14 16:52:13 UTC**; the supplied context was opened at **16:52:25 UTC**. Research, contextual comparisons and modern terminology have made no changes to the frozen page files or combined fragment.

The 96 numbered items below contain a source and scan, a kind, a short quotation or formula anchor, and a comparison with the supplied context. Reader constructions give their confidence and reasons. Longer calculations appear in separately labelled verification blocks and Appendices A–B. The note numbers are editorial identifiers, and the mathematical examples carry no claim of novelty.

**Locator convention.** A citation such as `152/008` means page 8 of that cote's current official PDF, counting its institutional cover. Handwritten folios and printed archive footer numbers are reported separately. This convention also governs the newly consulted cotes 67, 121, 134-2, 136, 147, 149, 150 and 151. The *Esquisse* has a separate printed/PDF concordance, supplied with every substantive citation.

**Context convention.** `C147` and a bare contextual `147/NNN` expand to `context/MPL_147_138-190_transcription.tex`; `C149` and contextual `149/NNN` expand to `context/MPL_149_091-136_transcription.tex`. The corresponding `_notes.md` files are earlier first-pass research leads. `STATE` or `RESULTS_STATE.md` means `context/notes/RESULTS_STATE.md`, and `STATEMENTS_WITH_STATUS.md` means `context/STATEMENTS_WITH_STATUS.md`; these files belong to the supplied context archive and are not duplicated in this deliverable.

**Status convention.** “Proved”, “Known”, “Refuted” and “Open” attached to a supplied return ID retain the register's attribution to that return. The register reports no full-effort review of those rows; its medium review does not promote them. An intake reading or unchecked plan retains that status. The calculations in these notes address the displayed models and maps and do not upgrade a register entry merely by analogy.

**Search evidence.** The item-specific ledgers in `research/` record the actual searches: `research/context_search_root.json` for P01–P18 and R01–R08; `research/context_search_standing.json` for U01–U09 and T01–T06; `research/q1_context_by_note.json`, `research/q3_context_by_note.json` and `research/q4_context_searches.json` for the three corresponding research sections. Source URLs, selected original-page hashes, failed accesses and index limits are retained in the source ledgers. Public machine transcriptions were used to locate external passages; historical claims below rely on the selected originals that were inspected.

### Guide to the four requested questions

| Question | Recorded outcome | Main items |
|---|---|---|
| Where are *tubulure* and *ombre* introduced and defined? | Earlier precise constructions are located; an explicit identification of the objects named at 149/133 remains unlocated in the bounded search. | Q1-01–Q1-07 |
| Did Grothendieck resolve the sphere “Remords” himself, in December 1981? | His own sphere calculation and retraction of the fear are located; the exact month is unverified, and the general proof retains his stated unfinished status. | R01–R05 |
| How do 120–121 compare with o-minimal structures and named variants? | Explicit model functors, Boolean reconstruction, finiteness tests and named comparisons are given; the all-compact countermodel is checked against the precise 120 branch. | Q3-01–Q3-11; A120-24 |
| What is the relation to Shiota's comparison? | The isomorphism-family map and checked Shiota realizations are specified, together with their scope and an explicit test of the final finite-diagram question. | Q4-01–Q4-12; Appendices A–B |

## 1. Cote 152: word types, plane trees and contours

### P01 — The operations pictured on the first working sheet

**Source:** 152 scan 2, boxes at right and lower family of trees. **Kind:** unpursued implication. **Quote:** “composition”; “insertion d'un cycle”.

The sheet gives insertion and composition pictures before the word-type and tree correspondences on scans 3–5, making compatibility with those operations a concrete requirement for interpreting the later category equivalences. Searches for composition, insertion, arbre, cycle and graphe locate the flag-composition construction in context/MPL_147_138-190_transcription.tex, scans 187–188, but no verbal definition there of the operations drawn on 152/2; this sheet **adds** a separate graphical presentation to that context. It bears on the comparison work suggested by **STRATA C.5** and **STRATA F.5–F.6** in STATEMENTS_WITH_STATUS.md (return claims), through the specific question of transporting composition, without supplying the claimed flag or transporter comparisons itself.

### P02 — The claimed category equivalence needs its arrow-level reading

**Source:** 152 scan 3, paragraph beginning “La cat.”; scan 13, first full paragraph. **Kind:** unproved claim. **Quote:** “équivaut à la cat. isotopique”.

The text specifies disk, orientation, chord set and marked boundary data, and later explains the region-dual tree, but a verification of the stated categorical equivalence still needs the intended morphisms of word types and the induced maps on isotopy classes. The supplied context's nearest same-object search results are the category of local flags in context/MPL_147_138-190_transcription.tex, scans 185–188, and the “maquette simpliciale” in context/MPL_149_091-136_transcription.tex, scan 133; 152 **adds** a disk-and-tree construction rather than restating an arrow-level proof found in those passages. This bears on **STRATA C.1/C.5** and **EXIT_ONE_TYPE P4e** (return claims): the new contribution is an explicit geometric presentation for comparison, not a change to their status.

### P03 — The marked region controls the word data

**Source:** 152 scan 3, data \((D,\omega,K,S_0)\) and conditions at the foot. **Kind:** unpursued implication. **Quote:** “l'unique comp. connexe”; “ordre réduit”.

The distinguished \(S_0\) and its region \(R_0\), together with the conditions on \(S\cap\alpha\), are part of the displayed word data and must be carried through any tree comparison. Searching \(R_0,S_0\), marked points and connected components in the supplied context finds the boundary-component/maquette discussion at 149/133 and the connected-stratum requirements at 147/181, but no matching reduced-order formula; 152 **adds** those boundary-mark and region conditions. The relevant register connection is **EXIT_ONE_TYPE P4e** and **FLAGGED_149 ZD8** (return claims), since forgetting these data is an explicit operation whose effect must be computed.

### P04 — The recursive admissibility rule

**Source:** 152 scan 4, text below the first large drawing. **Kind:** unproved claim / reading question. **Quote:** “se définit par réc”; “deux arêtes consécutives”.

The recursion uses an adjacent two-element orbit and contraction of one edge, with the identity involution as an alternative and orders zero and one explicitly admitted in the margin. A same-word search for involution, admissible and contraction finds no matching recursion in the supplied 147/149 text; the nearest context is the finite local-order construction at 147/189–190, so this page **adds** a concrete combinatorial rule. No register entry supplied here settles the rule's compatibility with the subsequent disk construction; **STRATA C.5** is a comparison target only, and the precise induced involution after contraction remains a useful arrow-level verification.

### P05 — A small exact test of the admissibility wording

**Source:** 152 scan 4, the same recursion. **Kind:** own idea / explicit calculation. **Quote:** “\(\sigma=\mathrm{id}\) ou”.

For the ordered three-edge segment and \(\sigma=(1\,3)\) fixing edge \(2\), the displayed two alternatives both fail: \(\sigma\) is not the identity and its only two-element orbit contains no consecutive edges. The single drawn chord from \(1\) to \(3\) has no other chord to cross, so this calculation records why a proposed translation of the scan-4 recursion into the scan-10 nonpenetration criterion must explicitly account for fixed edges and the relevant boundary convention. The context search for involution/nonpenetration/admissible yields no parallel example in 147/138–190 or 149/91–136; this **adds** a finite test, bears only indirectly on **STRATA C.5**, and has **high confidence** because both alternatives are checked directly, without deciding any doubtful ink.

### P06 — The orientation torsor in a plane tree

**Source:** 152 scan 5, definition of “bicircularisations”. **Kind:** unpursued implication. **Quote:** “compatible aux ‘passages à l'opposé’”.

Fix the underlying graph and its incident-edge sets: the two-element set \(\varepsilon\) maps equivariantly to the set of cyclic orders at all vertices, so changing the chosen element of \(\varepsilon\) reverses those orders simultaneously. With morphisms acting identically on that fixed graph, the exact map on isomorphism classes sends \((\varepsilon,c)\) to the orbit of \(c(e)\), independently of \(e\); its inverse chooses \(c_0\) in the orbit and assigns \(c(+)=c_0,\ c(-)=\operatorname{rev}(c_0)\) on the free torsor \(\{+,-\}\), with the other choice giving an isomorphic object. A reversal-fixed cyclic-order system still permits the nonidentity torsor automorphism, which this orbit-set map forgets, so the groupoid retains its stabilizer. Searches for orientation and opposite orders locate 147/190's powerset-order passage and context/MPL_147_138-190_notes.md, item 190-02; 152 **adds** the explicit torsor formulation, relevant to **STRATA C.2/C.6** (return claims).

### P07 — Low-valence orders and the doubtful last digit

**Source:** 152 scan 5, final two sentences. **Kind:** reading question. **Quote:** “tels que \(\operatorname{card} A_s\geq3\)”.

The cyclic order on a set of zero, one or two incident edges is unique, so the text's preceding degree-three threshold has a direct finite-set explanation. The final bound remains frozen as \(1\mid2\): the weaker bound \(1\) also gives uniqueness, and the calculation therefore supplies no permission to choose a digit from mathematical expectation. Context searches for cyclic orders, degree and orientation produce no exact threshold statement in the supplied 147/149 passages; this **adds** a reading question, with **STRATA F.5** a comparison target for decorated trees rather than an adjudication of the glyph.

### P08 — The general contour retains every boundary component

**Source:** 152 scan 7, second paragraph; scan 8, arc formulas. **Kind:** unpursued implication. **Quote:** “contour comb. (pas néc. connexe)”.

The construction starts with all directed edges and permits a disconnected contour, so every cycle of the boundary traversal belongs to the object being reconstructed. Searches for contour, déploiement and connected components locate context/MPL_147_138-190_transcription.tex, scans 156–163 and 183–190, where deployed stratum/flag spaces retain their components; 152 **adds** a graph-level realization of a component-sensitive construction. This bears on **STRATA C.3/C.5** and **FLAGGED_149 ZD8** (return claims), through the explicit component data, without identifying the graph contour with a normal-crossings tubular space.

### P09 — What is withdrawn on the rotation sheet

**Source:** 152 scan 7, the two lower cancelled paragraphs; scan 8, later formulas. **Kind:** withdrawn in the same text / reading question. **Quote:** “rotation autour de son sommet”.

The quotient \(S\simeq\vec A/\rho_\Gamma\) occurs inside a cancelled paragraph on scan 7, while scan 8 develops the right/left contour operations with several reversed letters and erased inverse exponents. The same-symbol search \(\sigma,\rho\), involution and déploiement finds no formula resolving those amendments in the supplied context; this **adds** evidence of the author's local revision, rather than a context-backed choice of the final convention. It bears on **WG2 §1.8 #5** (unchecked glossary plan) and the composition bookkeeping of **STRATA C.5** (return claim), and the cancelled paragraph must retain its cancelled status in any subsequent argument.

### P10 — The two live rotation descriptions on scan 10

**Source:** 152 scan 10, opening display and final row of the correspondence diagram. **Kind:** reading question. **Quote:** “correspondance fondamentale”.

The frozen text has the opening equality \(\rho_\Gamma=\rho_C\) and later the displayed correspondence \(\rho_\Gamma\leftarrow\rho_C\sigma_C\), alongside a fixed-point-free \(\sigma_C\). Reading those as simultaneous equations on the same identified nonempty edge set yields \(\rho_C=\rho_C\sigma_C\) and hence \(\sigma_C=\mathrm{id}\) by cancellation, which makes a change of identification or an unrevised line a precise reading question. A search for these symbols and “rotation” in both context transcriptions finds no deciding passage; 152 therefore **adds** an internal comparison problem, related to the notation audit requested by **WG2 §1.8 #5**, and no formula has been changed.

### P11 — An explicit permutation dictionary for a later check

**Source:** 152 scans 7–10. **Kind:** own idea / worked comparison. **Quote:** “l'ens des arcs”.

Use fresh notation \(H\) for a finite directed-edge set, \(\alpha\) for its fixed-point-free reversal involution, \(v\) for the cyclic successor permutation at initial vertices, and \(b=v\alpha\) for traversal across an edge followed by that successor; the inverse is \(v=b\alpha\). On bijections \(f:H\to H'\), the two relations \(f\alpha=\alpha'f,\ fv=v'f\) give \(fb=b'f\), and the converse follows by multiplying by \(\alpha\), giving mutually inverse functors between these specified permutation groupoids. Vertices are the cycles of \(v\), so isolated vertices require additional data in a graph presentation. The context search for rotation/involution and graph gluing gives no matching formula in the supplied transcriptions, so this **adds** a checking device relevant to **STRATA C.1/C.5**, with **high confidence** in the algebra and no identification of fresh \(b,v\) with the manuscript's uncertain \(\rho\)-conventions.

### P12 — The nonpenetration criterion has a constructive direction

**Source:** 152 scan 10, boxed criterion; scans 11 and 13, chord construction. **Kind:** unproved claim / unpursued implication. **Quote:** “totalement non pénétrante”.

For \(n\) pairwise disjoint properly embedded chords in a disk, successively cutting along a chord increases the number of complementary regions by one, so the dual graph has \(n\) edges and \(n+1\) vertices and is connected; removing the last chord reverses that step and proves inductively that the dual graph is a tree. This directly checks the construction described on scans 11–13, while the full boxed equivalence also calls for matching the boundary-edge pairing and its orientation conventions with the graph's recovered contour. Context/MPL_149_091-136_transcription.tex, scan 133, asks what its boundary maquette describes; the present pages **add** a concrete dual-complex calculation bearing on **FLAGGED_149 ZD8** and **EXIT_ONE_TYPE P4e** (return claims), rather than replacing their normal-crossings setting by the disk example.

### P13 — The quotient really glues paired edges with reversed directions

**Source:** 152 scan 11, first full prose paragraph. **Kind:** unpursued implication. **Quote:** “en renversant les orientations”.

The quotient map \(q:|C|\to|\Gamma|\) identifies each parameterized edge \(a(t)\) with \((\sigma_Ca)(1-t)\), which explicitly gives the reversal used in reconstructing the underlying graph. A same-object search for quotient, recollement and gluing finds context/MPL_147_138-190_transcription.tex, scans 156–158 and 180, where the gluing datum is a span of neighborhoods/groupoids; 152 **adds** an actual quotient map in a finite graph case. It bears on **STRATA C.3** and **EXIT_ONE_TYPE P1d1** (return claims), as a tractable map whose topological and categorical realizations can be compared, with no inference that the quotient alone proves the homotopy-descent claim of either register entry.

### P14 — Region adjacency and the boundary dual are both retained

**Source:** 152 scans 11 and 13, sentence continued across the reused printout. **Kind:** unpursued implication. **Quote:** “Le polygone combinatoire … est dual”.

One vertex of \(\Gamma\) is assigned to each cut region and one edge to each shared chord, while the contour polygon is dual to the boundary subdivision by chord endpoints. The explicit incidence assignment sends a chord to its two neighboring regions and a boundary interval to the region it borders, thereby retaining the two incidence maps required to compare the dual constructions. Searches for duality, régions and maquette locate 149/133 and the flags at 147/185–188; this **adds** the maps for a disk example and bears on **FLAGGED_149 ZD8**, **STRATA C.1** and **STRATA C.5** (return claims).

### P15 — Removing the chosen orientation is an explicit revision

**Source:** 152 scan 11, top diagram; scan 13, first full paragraph. **Kind:** withdrawn in the same text. **Quote:** “pas néc. plans orientés”.

The top diagram deletes “orienté”, and scan 13 deletes “orientés” after “disques” while explicitly allowing unoriented planes and disks. The data-level map is the simultaneous-reversal orbit map described in P06, so this revision has a specified mathematical operation rather than an unexplained change of terminology. Searches for orientation and opposite orders lead to context 147/190 and note 190-02; 152 **adds** this explicit orientation-forgetting step, relevant to **WG2 §1.8 #5** and to the variance-sensitive constructions claimed in **STRATA C.2/C.6**.

### P16 — A controlled map toward the stable-tree indexing data

**Source:** 152 scans 5, 11 and 13. **Kind:** own idea / comparison problem. **Quote:** “arbres plans”.

On the full collection of these trees equipped additionally with labelled external flags and at least three flags at every internal vertex, send a cyclically ordered tree to the same labelled incidence tree with the cyclic orders forgotten, and send a label- and order-preserving graph isomorphism to its underlying graph isomorphism. This is an explicitly defined functor of isomorphism groupoids, so its fibers give a concrete place to compare planar choices with the stable-tree indexing data in **STRATA F.4–F.6** and **RESIDUE H.4** (return claims). The supplied context has only the moduli/stratum side in those status rows and the flag constructions at 147/185–188; this **adds** the specified comparison functor, with **high confidence** in its definition and no claim here about extending it to all contractions, realizing moduli spaces, or proving those register rows.

### P17 — The computer sheets give a material date, with its scope

**Source:** 152 scans 3, 6, 9 and 12, reused printed material. **Kind:** unpursued implication / dating evidence. **Quote:** “19 MAY 82 JOB EXECUTION DATE”.

Scan 9 gives an explicit execution date and scans 3, 6 and 12 preserve associated job-control material, furnishing material evidence to compare with the archive's catalogue range beginning in 1982. The dated printout is evidence about the reused sheet, and the relation to the handwriting requires the physical order of printing and writing rather than an automatic assignment of that date to every note in the folder. Searches for the job identifiers, 19 MAY 82 and the title in the supplied context yield no matching sheet; this **adds** dating evidence for the package, bears on the source-critical function of **WG2 §1.8 #5**, and changes no mathematical register status.

### P18 — The least legible formulas remain research questions

**Source:** 152 scan 8, cancelled lower block and margin; scan 10, correspondence diagram and margin. **Kind:** reading question. **Quote:** “déploiement”; “rotation renversée”.

The source has an unresolved word after “Le contour C” and a raised rotation decoration that the frozen text exposes as doubtful, so neither supports a confident new technical term or a silently chosen exponent. Searches for those terms and the \(\rho/\sigma\) notation in 147/138–190 and 149/91–136 locate uses of déploiement but no matching decorated rotation formula; the package **adds** a homonym/notation comparison task under **WG2 §1.8 #5** (unchecked plan). The relevant mathematical checking map is P11's explicitly defined permutation correspondence, which can test a proposed future reading without altering the present one.

## 2. Tubulure and ombre: constructions and the remaining identification

The exact comparison sought at 149/133 remains unlocated in this search. The following items retain the formulas of the earlier constructions, their checked dates and their source limits; the discovery index cannot establish an archive-wide first occurrence.

### Q1-01 — What 149/133 actually supplies

**Kind:** reading question; primary verification. **Source:** cote 149, PDF scan 133, archive footer 132, manuscript p. 66. **Anchors:** “ombres”; “tubulures étales”.

The three relevant places are the insertion above the completion of $X$ along $D$, the parenthesis describing the localization of $X$ along $D_J$, and the left-margin preference for étale tubulures. The notation fixes $\widehat X$, $X_J$, and the stated trace $U_J$ operationally, but this page supplies no site, universal property, or explicit comparison morphism that identifies the named *ombre* with a construction found elsewhere in this search. The original image supports both noun readings at moderate confidence, while the supplied transcription correctly retains uncertainty; the frozen text has not been changed. This **restates** the question in the supplied 149 notes and **adds** direct verification of the three places.

**Context search:** `context/MPL_149_091-136_transcription.tex`, scan 133; `context/MPL_149_091-136_notes.md`, scan 133, notes 133.2, 133-R0, 133-R1, 133.4; all context files searched for `ombre`, `tubulure`, `D_J`, and `\hat X` (Q1-01 in `research/q1_context_by_note.json`). **Register:** INTAKE 20261114 §13.2 — intake reading, not a referee verdict; WG2 §1.8 #5 and §1.1 #6 — unchecked plans; EXIT_ONE_TYPE P4e and FLAGGED_149 ZD8 — “Proved” as return claims, not promoted here to verified results. **Relation:** restates / adds; no verdict on those mathematical claims.

### Q1-02 — The dated 1975 étale-tubular passage

**Kind:** historical source; proposed construction. **Source:** cote 134-2, PDF scans 146 and 174–175, archive footers 145 and 173–174, manuscript pp. 1 and 29–30. **Anchor:** “voisinage tubulaire étale”.

In the letter to Breen dated 17/19 July 1975, Grothendieck writes the two-stratum sheaf data $F_0,F_1,F_0\to i_0^*i_{1*}F_1$ and proposes describing this last functor through an étale tubular topos of $X_0\subset X$. The following page gives the topological model, with $p:\partial T\to X_0$: $T=(\partial T\times[0,1])\amalg_{\partial T\times\{1\}}X_0$ and $T\setminus X_0\simeq\partial T\times[0,1[$. The étale construction is presented as a project he thinks possible; the concrete quotient and the 1975 date are directly visible. This **adds** an earlier dated source to the neighborhood language of 147/140 and the étale wording of 149/133, without asserting a first occurrence throughout the archive.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–142 and 180; `context/MPL_149_091-136_transcription.tex`, scan 133; `context/STATEMENTS_WITH_STATUS.md`, STRATA C.1–C.8; all context files searched for tubular-neighborhood wording, recollement and the two inclusion indices (Q1-02 ledger). **Register:** WG2 §1.8 #5 — unchecked glossary plan; INTAKE 20261114 §13.2 — intake reading; EXIT_ONE_TYPE P1d1 — “Proved” as a return claim. **Relation:** adds a primary historical construction, with no reproof of coherent gluing.

### Q1-03 — The germ and its canonical maps in 147

**Kind:** definition / stated functoriality. **Source:** cote 147, PDF scans 140 and 142, archive footers 139 and 141, manuscript pp. 69–70. **Anchor:** “germe”.

For a local immersion $D'\to Y$ of smooth analytic spaces, 147/140 introduces the tubular neighborhood as a germ of analytic space around $D'$, explicitly independent of the additional normal-crossings divisor. Scan 142 envisages a direct topological/topos definition and records, for $D''\to D'\to Y$, the canonical diagram whose lower row is $\mathcal V_{D'',Y}\to\mathcal V_{D',Y}\to Y$ and whose upper row is $D''\to D'$. The qualification accompanying the proposed topological definition must remain attached to it: these pages state the germ construction and maps, while a full site construction is not written in the checked passage. This **restates** the supplied first-pass reading and **adds** original-page verification, giving a precise adjacent object for the glossary question.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–146, 157–164; `context/MPL_147_138-190_notes.md`, notes attached to scans 163–164; Q1-03 ledger searches `germe`, local immersions and the $V$ notation in every context file. **Register:** EXIT_ONE_TYPE P1a1 and P1d1 — “Proved” as return claims; WG2 §1.8 #5 — unchecked plan. **Relation:** restates / adds source verification; neither claim is re-proved here.

### Q1-04 — The provisional neighborhood-limit description in 151

**Kind:** provisional definition. **Source:** cote 151, PDF scans 27–29, archive footers 26–28. **Anchor:** “à titre provisoire”.

For closed $Y\hookrightarrow X$ with $X$ paracompact, scan 28 proposes $V_{Y,X}$ as the germ around $Y$, regarded as a topos through the displayed projective limit of open neighborhoods. Scan 29 defines $V^*_{Y,X}=V_{Y,X}\cap(X\setminus Y)=V_{Y,X}\setminus Y$ and the span $V^*_{Y,X}\to V_{Y,X}$, $V^*_{Y,X}\to X\setminus Y$. This **adds** an explicit neighborhood-indexed description to 147/140–142 and **restates** the germ/punctured-germ pattern of the supplied 147/163–164. The heavily revised homotopy-equivalence paragraph on scan 28 is not treated as a settled assertion.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–142, 157–164; `context/MPL_149_091-136_transcription.tex`, scan 133; all context searched for open neighborhoods, germs, $V$ notation and topological limits (Q1-04 ledger). **Register:** INTAKE 20261114 §13.2 — intake reading; MPL_150_085-099+151_001-031 §106–107 — first-pass research leads; EXIT_ONE_TYPE P1d1 — return claim. **Relation:** adds / restates; exact identification with $X_J$ remains a question.

### Q1-05 — The conical definition and an exact comparison of its parameters

**Kind:** definition; reader's concrete comparison. **Source:** cote 150, PDF scans 12 and 22, archive footers 11 and 21, manuscript pp. 1 and 6; relative version begins PDF scan 13; comparison source 134-2/175. **Anchor:** “cocartésien”.

Cote 150/12 specifies $Y\subset T$, a closed boundary $\dot T$, and a multiplicative $[0,1]$-action with $\lambda y=y$, $0T\subset Y$, and pushout square $\{0\}\times\dot T\to Y$, $[0,1]\times\dot T\to T$, giving $T=C(f)$, $f(x)=0x$, via $[(\lambda,x)]\mapsto\lambda x$. Scan 22 defines a germ by equality $\lambda T=\lambda'T'$ of rescaled neighborhoods with matching conical structures over $Y$. For the same $f$, the endpoint-one quotient of 134-2/175 maps to the endpoint-zero quotient by $[(x,t)]\mapsto[(1-t,x)]$, $y\mapsto y$, with inverse $[(\lambda,x)]\mapsto[(x,1-\lambda)]$. This concrete comparison has high confidence because both formulas preserve the quotient relations and compose to identities; the comparison map to 149's $X_J$ remains unspecified.

**Context search:** `context/MPL_147_138-190_transcription.tex`, scans 140–142 and 190 (tubular neighborhoods and local fibrations); `context/MPL_149_091-136_transcription.tex`, scan 133; all context searched for conical, cone, pushout and action notation (Q1-05 ledger, together with the Q1 tubular-germ search). **Register:** INTAKE 20261114 §13.2 — intake reading; WG2 §1.8 #5 — unchecked plan; EXIT_ONE_TYPE P1a1 — return claim. **Relation:** adds a verified definition and a concrete coordinate comparison; no conditional theorem is proposed.

### Q1-06 — A checked definition of module shadows in 136

**Kind:** definition; unresolved comparison. **Source:** cote 136, PDF scans 23–26, archive footers 22–25; cover at PDF scan 2. **Anchor:** “ombres virtuelles”.

Here $S=k\{T\}$ is the divided-power polynomial algebra, $S^{+(N)}=\bigoplus_{i\ge N}kT^{(i)}$, and scan 25 writes $\omega_0(M)=M\otimes_k S$, $\omega_N(M)=S^{+(N)}\omega_0(M)$; scan 26 calls the $\omega_N$ shadow functors and introduces $\mathrm{Omb}(k)$ through graded $S$-modules, with a question mark on the proposed lower grading bound. The recovery map is written $M\to\pi_N(\omega_N(M))$, $x\mapsto(xT^{(i)})_{i\ge N}$, where $\pi_N$ selects compatible families $T^{(j)}x_i=\binom{i+j}{i}x_{i+j}$. Scan 23 visibly has an $S$ under its first tensor sign, so the scan-25 formula is cited without silently altering that earlier line. This **adds** an explicit lexical and mathematical definition; no morphism from this construction to the $X_J$ or $\widehat X$ of 149/133 has been established in the checked passages.

**Context search:** every supplied context file searched for `ombre`, `omega_N`, `pi_N`, divided powers and graded-module wording; the noun hits meet `context/MPL_149_091-136_transcription.tex`, scan 133 and its notes, while the module formulas are newly located external material (Q1-06 ledger). **Register:** WG2 §1.8 #5 — unchecked glossary plan; INTAKE 20261114 §13.2 — intake reading of the previously bounded corpus. **Relation:** adds; it does not contradict an absence claim limited to 147/138–190 and 150/1–43. **Dating:** catalogue range begins 1975–1976; no autograph date on these checked leaves establishes their individual day or year.

### Q1-07 — A checked pointed-disc shadow map in 67

**Kind:** definition; unresolved comparison. **Source:** cote 67, PDF scans 63–64, archive footers 62–63, pencil numbers 65–66, manuscript p. 6 on scan 64. **Anchor:** “ombre de D”.

For fixed $(X',a)$, scan 63 considers compact pointed conformal discs $D\subset\operatorname{Int}(X')$ with the stated rectifiability condition on $\partial D$, associates a Euclidean disc in $T_{X',a}$ compatible with its conformal structure, and scan 64 names the map $D\mapsto o(D)$. It records compatibility with concentric rescaling, $o(\lambda D)=\lambda o(D)$, for $0<\lambda\le1$. This **adds** another explicitly mapped use of the noun, while its comparison with the localization along $D_J$ in 149 remains open in the checked material. The catalogue's range, beginning in 1977 and extending to 1984, does not date these individual leaves before the 1983 notes.

**Context search:** `context/MPL_149_091-136_transcription.tex`, scans 133–134; `context/MPL_147_138-190_transcription.tex`, scans 163–164; frozen `work/MPL_152+120_transcription.tex`, cote 152 scans 3 and 11 (disc data); all context searched for shadows, discs, the tangent notation and homotheties (Q1-07 ledger). **Register:** WG2 §1.8 #5 — unchecked glossary plan; INTAKE 20261114 §13.2 — bounded intake reading. **Relation:** adds a lexical construction; the occurrence of discs alone supplies no comparison map to the 152 data or to 149.

### Source and search ledger

#### Primary originals actually inspected

All scan numbers below count the modern initial PDF cover. The archive footer generally equals PDF scan minus one; pencil numbers are separately reported where they differ. Local extracts preserve the original images and their hashes are recorded in `research/q1_primary_extract_manifest.json`; the original-source copies are outside `work/`.

| Source URL | Exact checked location | Passage checked / use |
|---|---|---|
| <https://grothendieck.umontpellier.fr/149.pdf#page=133> | PDF133; footer132; ms66 | Three noun locations, completion and localization notation; Q1-01 |
| <https://grothendieck.umontpellier.fr/147.pdf#page=140> | PDF140,142; footers139,141; ms69–70 | Germ and canonical neighborhood arrows; Q1-03 |
| <https://grothendieck.umontpellier.fr/134-2.pdf#page=146> | PDF146,174,175; footers145,173,174; ms1,29,30 | Autograph date; sheaf-gluing functor; endpoint-one cone; Q1-02 |
| <https://grothendieck.umontpellier.fr/150.pdf#page=2> | PDF2; footer1 | Autograph folder date: December 1981–January 1982 |
| <https://grothendieck.umontpellier.fr/150.pdf#page=12> | PDF12–16,22–23; footers11–15,21–22; ms1–3,6 | Action/pushout; relative neighborhood; boundary and strictness; germ and reconstruction data; Q1-05 |
| <https://grothendieck.umontpellier.fr/151.pdf#page=27> | PDF27–29; footers26–28 | Provisional limit, punctured object and gluing span; Q1-04 |
| <https://grothendieck.umontpellier.fr/136.pdf#page=23> | PDF2,23–26; footers1,22–25 | Cover; $\omega_N$, recovery map, virtual-shadow terminology; Q1-06 |
| <https://grothendieck.umontpellier.fr/67.pdf#page=63> | PDF63–64; footers62–63; pencil65–66 | Tangent-disc map and its name; Q1-07 |

The 151 extract also contains PDF2 and41–44, supplied to the root researcher for Q2; those latter pages are not used as Q1 evidence. Cote150 PDF22–23 were also inspected; scan22 is used in Q1-05, while the equivalence claim on scan23 is retained only as a source locator, without a verdict on its proof.

#### Discovery search and evidential limits

1. **Complete supplied context text search:** all seven files under `context/`, plus the frozen combined transcription; no supplied scan image used. `research/q1_context_search.json` records the first broad sweep and `research/q1_context_by_note.json` records every query, hit, exact file, line and scan available for each proposed note. Previous notes and registers remain leads or claims with their recorded statuses.
2. **Public machine index:** 636 available French transcript files from <https://github.com/Commutator-IO/grothendieck-project>, excluding cotes120 and152, plus two canonical Longue Marche transcript files from <https://github.com/ivan-gentile/la-longue-marche>. Exact noun searches and broader tubular/germ searches were used for discovery, not as an edition; `research/q1_index_manifest.json` records exact paths, URLs, hashes and comparison to the observed repository tree, with word hits in `research/q1_public_index_hits.json`.
3. **False-negative control:** the machine text for149 omitted the two checked *ombre* readings and misread the margin containing *tubulures*. A negative result in this index therefore proves only a failure to retrieve that spelling from that index.
4. **Unverified leads retained as leads:** the later156-4/156-6/156-7/156-8 shadow vocabulary; the longer conical-neighborhood material indexed under119; a Cox1978 tubular-neighborhood reference in Brown's bibliography preserved in134-2. No technical claim here relies on those passages without original verification.
5. **Web lookup:** exact-term searches for Grothendieck with *tubulure*, *tubulures étales*, *ombre(s)* and *localisé*; official Montpellier catalogue verification for dates and direct PDF paths; author-text check in the *Esquisse*, §5, printed pp32–33, as an additional locator only. The selected web refs, exact URLs and search terms are in `research/q1_web_ledger.json`; direct PDF opens through the web reader failed, so verified HTTP byte-range retrieval supplied the original pages for visual inspection.

#### Register handling and outstanding question

No return claim was silently upgraded. In particular, EXIT_ONE_TYPE P1a1/P1b1/P1d1/P4e, LM6 F.43 and FLAGGED_149 ZD8 retain the status **“Proved (the return's claim)”** recorded in `RESULTS_STATE.md`; WG2 §1.8 #5 and §1.1 #6 retain **unchecked plan** status, and INTAKE 20261114 §13.2 remains an **intake reading, not a referee verdict**.

The remaining concrete research question is to locate the site or universal property intended by the two words on149/133, together with the morphism to the localization along $D_J$ and the induced punctured object. Confidence is high that this is the unresolved step in this bounded search, because the checked 149 passage names the objects without such a construction, while the sources above supply precise adjacent maps but no identified comparison to that $X_J$.


## 3. Grothendieck's own return to the Remords

The continuation was checked in the original images of cote 151, PDF scans 41–44 (archive footers 40–43). The searchable public text served as a locator; the wording and cancellations were checked against those originals after the freeze.

### R01 — His own explicit reconsideration

**Source:** context 147 scan 180, “Remords”; external 151 PDF scan 41, upper half. **Kind:** withdrawn in a continuation / authorial resolution of the stated fear. **Quote:** “cette crainte n'était pas fondée”.

Grothendieck retracts the fear recorded at 147/180 and tests the sphere's gluing through gerbes [R-S1]. The same-object search locates the original span \(1\leftarrow\mathbb Z\to1\) and arrow-category calculation in context/MPL_147_138-190_transcription.tex, scan 180; the new passage **adds** his own reconsideration while retaining that earlier calculation of the ordinary constructible-sheaf topos. It bears on **EXIT_ONE_TYPE P1d1** [Proved, the return's claim] and **INTAKE 20261114 §13.2–13.3** [intake readings]: the contribution here is historical evidence of his response, with no upgrade of those statuses.

### R02 — The calculation that convinced him

**Source:** 151 PDF scans 42–43, equation (24) and equation (25). **Kind:** unpursued implication / own explicit algebraic check. **Quote:** “un magnifique succès”. **Confidence:** high for the calculation below, because the maps and their inverse are explicit; no novelty claim.

The continuation glues two neutral \(A\)-gerbes by an equivalence over the punctured tube and obtains \(H^2(S^2,A)\cong A\) from automorphisms of the trivial extension of \(\mathbb Z\) by the abelian group \(A\) [R-S1]. Explicitly, the map \(A\to\operatorname{Aut}_{\mathbb Z,A}(\mathbb Z\times A)\) sends \(a\) to \(\phi_a(n,b)=(n,b+na)\); its inverse extracts the second component of \(\phi(1,0)\), since a homomorphism fixing \(A\) and the quotient \(\mathbb Z\) has exactly this form. The identities \(\phi_a\phi_b=\phi_{a+b}\) and \(\phi_a^{-1}=\phi_{-a}\) check the identification used in his computation. Searches for gerbes and \(H^2\) find no such calculation in the supplied 147/149 transcriptions, so this **adds** the author's test to 147/180 and to **EXIT_ONE_TYPE P1d1** and **INTAKE 20261114 §13.2** with their recorded qualifications.

### R03 — An exact modern comparison for the same sphere

**Source:** context 147 scan 180; external 151 PDF scans 42–43; Treumann, Examples 1.4 and 1.6. **Kind:** unpursued implication / literature comparison. **Quote from supplied context:** “cohomologie ... nulle en dim \(>0\)”.

Treumann describes the sphere's ordinary exit category by two objects and one nonidentity arrow, and its exit 2-category by retaining \(\mathbb Z\) as the automorphism group of that arrow; a constructible stack consequently includes a natural automorphism of its gluing functor [R-S2]. In these displayed skeletal models, with the ordinary category viewed as a locally discrete 2-category, the truncation functor \(q:\operatorname{EP}_{\leq2}\to\operatorname{EP}_{\leq1}\) fixes the objects and arrow and sends every element of that automorphism group to the identity 2-cell. This **restates** 147/180's ordinary-category calculation and **adds** a named primary comparison for the coherence retained in 151's gerbe gluing. **EXIT_ONE_TYPE P1d1** already records the full-shape versus ordinary-shape claim, and **STRATA C.1/C.5–C.6** record coherent gluing claims; they are cited with their return statuses rather than re-proved here.

### R04 — What he still leaves unverified

**Source:** 151 PDF scan 43, after equation (25), and scan 44; context 147 scans 179–180. **Kind:** self-flagged: unverified general reconstruction. **Quote:** “Sans aller plus loin”.

After his sphere test, Grothendieck endorses the homotopy-colimit intuition and postpones further verification [R-S1]. This **adds** his own test to 147/179–180, leaving general reconstruction unproved there. It bears on **EXIT_ONE_TYPE P1d1/P1a1**, **STRATA C.5–C.6** [return claims] and **WG2 §1.1 #6** [unchecked plan], without replacing their statements by the assertion that one example proves the whole programme.

### R05 — The December 1981 date remains a source question

**Source:** 151 PDF scans 2, 27 and 41–44; 150 PDF scan 2; *Esquisse* §5, printed p. 25 / PDF p. 21; Montpellier catalogue, cotes 150–151. **Kind:** reading question / chronology. **Quote from supplied context:** “Remords”.

No date occurs on the inspected 151 leaves; the original 150 folder carries December 1981–January 1982, and Grothendieck retrospectively dates this period of work on stratified structures to the same interval in *Esquisse* [R-S3–R-S4; S1]. These are positive period anchors, while the catalogue's 1981–1990 span describes the composite cote 151 and no inspected source dates its specific sphere calculation to December alone. Searches for décembre/December/1981 in the supplied context yield no autograph date connecting the two passages, so this **adds** a dating qualification to **INTAKE 20261114 §13.2** [intake reading] and the linked **WG2 §1.1 #6** chronology lead. The exact month remains unverified.

### R06 — The local-flag construction already retains topological spaces

**Source:** context 147 scan 188, equation (303); 152 scans 2–3 and 13. **Kind:** unpursued implication. **Quote:** “une catégorie dans (Top)? Oui”.

The supplied context gives the map \(D_{\Delta_2}\to D_{\Delta_1}\times_{D_{\Delta_0}}D_{\Delta_1}\), with objects the local strata and arrows the local flags, so a comparison with 152's composition pictures must specify maps on those spaces as well as on their sets of components. Searching for the same category/flag terminology locates context/MPL_147_138-190_notes.md, item 188-02, which already proposes a sphere calculation; that note remains a lead. Cote 152 **adds** explicit disk-and-tree operations for comparison with this topological category, bearing on **STRATA C.1/C.5** and **EXIT_ONE_TYPE P1d1**, without treating the prior note as a completed proof.

### R07 — A separate admitted step survives the sphere test

**Source:** context 147 scans 177–178, equation (295), and scan 190; 120 scan 25. **Kind:** self-flagged: unverified comparison. **Quote:** “Admettant ce point”; “Elle servira plus loin”.

The context expressly admits the canonical comparison from the fundamental groupoid of the punctured normal-bundle construction to that of the tubular object, and later postpones the use of local triviality to construct the elementary tubular fibrations. The generic-triviality question on 120/25 **adds** an axiomatic target for those product charts; its occurrence supplies no missing canonicity proof for (295). Same-word searches locate these admissions in context/MPL_147_138-190_transcription.tex, scans 178 and 190, and the relevant existing claims are **EXIT_ONE_TYPE P1a1** and **BISITE D.5**; R01–R02 only change the evidence concerning the sphere objection.

### R08 — The normal-meridian arrows must also be retained

**Source:** context 147 scan 178 and 149 scans 133–134; 120 scan 25. **Kind:** unpursued implication. **Quote:** “par l'image des \(\pi_2\)”; “j'ai eu un peu peur”.

The two context passages explicitly retain the boundary maps \(\pi_2(D)\to\mathbb Z^r\) and \(\pi_2(D_J)\to T^J\), so replacing the gluing datum by a list of abstract fundamental groups would also discard the displayed homomorphisms and their kernels. The exact link to 120/25 is the requirement that a simultaneous diagram trivialization intertwine every arrow, expressed by \(v f=f'u\) in Q4-08. This **restates** the normal-meridian bookkeeping already visible in context/MPL_147_138-190_transcription.tex, scan 178, and context/MPL_149_091-136_transcription.tex, scans 133–134, and **adds** the finite-diagram compatibility test. It bears on **EXIT_ONE_TYPE P1b1**, **FLAGGED_149 ZD8**, and **STRATA C.5–C.6** with their recorded return statuses.

### Primary sources for this question

- **[R-S1]** Alexander Grothendieck, Montpellier cote 151, [official PDF](https://grothendieck.umontpellier.fr/151.pdf), scans 41–44, archive footers 40–43; equation (25) is on PDF scan 43. Original images inspected, including deletions; the short quotations from this source occur in Q1-04, R01, R02 and R04.
- **[R-S2]** David Treumann, *Exit paths and constructible stacks*, [arXiv:0708.0659](https://arxiv.org/abs/0708.0659), inspected [August 2007 PDF](https://arxiv.org/pdf/0708.0659), Examples 1.4 and 1.6, pp. 2–4. These examples, rather than a claim that the whole general reconstruction follows from them, support R03.
- **[R-S3]** Université de Montpellier, [archive inventory](https://grothendieck.umontpellier.fr/archives-grothendieck/), entries 150–151 and note 152 attached to entry 150. Consulted 14 November 2026; the catalogue's folder dating is recorded at its own level of attribution.
- **[R-S4]** Grothendieck, [cote 150 official PDF](https://grothendieck.umontpellier.fr/150.pdf), scan 2 / archive footer 1, dated folder, directly inspected. The retrospective passage is in [S1], *Esquisse*, §5, printed p. 25 / PDF p. 21.

## 4. Cotes 120–121 and the o-minimal comparison

### Source conventions and status

`C147` means `context/MPL_147_138-190_transcription.tex`; `C149` means `context/MPL_149_091-136_transcription.tex`. `STATE` means `context/notes/RESULTS_STATE.md`, read before these notes. **WG2 B15 (§1.2)** is an unchecked planning question; **BISITE D.12** and **CATHOT E.17** are **Open (the return's claim)**, without a full review recorded here. **TOTASPH E.6** is **Proved (the return's claim)**. The additionally supplied `context/STATEMENTS_WITH_STATUS.md` has now been read directly: **STRATA C.1/C.5/C.6/C.8** are **Proved (the return's claim)**; **STRATA C.2/C.3** are **Known (the return's claim)**; **RESIDUE G.3** is **Open (the return's claim; no review)**. Its stated global limit is retained: no row there has had full-effort review, and the medium review does not promote a status. The **MPL_150_085-099+151_001-031 §106** research note remains only a first-pass lead.

The contextual searches are saved in `research/q3_context_searches.json`. Both contextual transcriptions were searched for `modér`, `compact`, `fonction`, `graphe`, `quotient`, `amalgam`, `limite`, `faisceau`, `anneau`, `corps`, `zéro`, `sépar`, `prolong`, `produit`, and `voisinage`; the relevant contextual notes and state register were searched as well. Neither supplied contextual transcription contains `modér`, so the exact M1–M11 terminology has no same-word antecedent in these two selections; the notes identify the actual nearest construction instead of inventing a previous axiom system.

### Q3-01 — A compact-model presentation has an explicit o-minimal realization

**Source:** 120 scans 3–24, especially 6 and 17. **Kind:** unpursued implication; reader's construction. **Quote:** “son graphe”; “les parties modérées … sont compactes”.

For a fixed o-minimal expansion \(\mathcal S\) of the real field with real parameters, put \(K_n(\mathcal S)=\{A\subset\mathbb R^n:A\text{ is compact and }\mathcal S\text{-definable}\}\): this supplies an explicit interpretation of the manuscript's compact branch, and the model functor sends \((n,A)\) to the same compact definable set and each map to the same function with the same graph. Its morphisms are exactly the continuous definable maps: a definable continuous map on compact \(A\) has compact graph, and a compact graph projects homeomorphically onto the Hausdorff domain \(A\). This **adds** an actual model to the compact/local vocabulary in C147 scans 181–184 and bears on **WG2 B15 (§1.2)** as a setting, without settling its localization question. **Confidence: high**, because the comparison on objects, arrows and underlying sets is explicit; the axiom verification appears in the table below.

### Q3-02 — The stated M1–M11 have a fully explicit non-finiteness model

**Source:** 120 scans 3, 10, 13, 15, 17–18, 21. **Kind:** own idea; concrete verification. **Quote:** “axiome (facultatif)” on scan 7; “compactes” on scan 17.

Take \(R=\mathbb R\) with its usual topology and let \(K_n^{\mathrm{all}}\) consist of **every** compact subset of \(\mathbb R^n\); the verification below proves M1–M11 for this family, on the branch in which optional M0 is absent. In particular the ternary Cantor set belongs to \(K_1^{\mathrm{all}}\), and its empty interior and infinitely many points exclude a presentation as a finite union of points and intervals, which is the one-dimensional finiteness clause in the cited o-minimal definition. This **adds** a concrete test to C147 scan 184's compactness/finiteness discussion and leaves **WG2 B15 (§1.2)** and **BISITE D.12** at their recorded statuses. **Confidence: high**, because the proof checks the actual coordinate maps, scalar functions, and compact graphs, rather than comparing terminology.

### Axiom-by-axiom realization and verification

This table is a proof for the two expressly defined families \(K_n(\mathcal S)\) and \(K_n^{\mathrm{all}}\), not an extra axiom attributed to the manuscript. For \(K_n(\mathcal S)\), all the displayed coordinate and field maps are definable; quantification over a definable compact set defines its distance function, and the definable Tietze extension used for M7 is Aschenbrenner–Fischer, Lemma 6.6. For \(K_n^{\mathrm{all}}\), ordinary continuous extension follows either from Tietze's theorem or from that same lemma applied to the expansion of \(\mathbb R\) naming every subset of every finite power (this expansion is definably complete because the real order is complete).

| Manuscript item | Exact operation or construction in the two compact families |
|---|---|
| M1, 120/003 | For \(u:[1,n]\to[1,m]\), the coordinate map \(u^*(x)_i=x_{u(i)}\) is continuous; its image of a compact set is compact. In the definable model this image is definable by the existential formula \(y_i=x_{u(i)}\). |
| M2, 120/003 | Surjective \(u\) makes \(u^*\) a closed coordinate embedding. The inverse image of a compact set is compact: the inverse on the image is a coordinate projection. |
| M3, 120/003 | \(A\cap(u^*)^{-1}(B)\) is closed in compact \(A\), since compact \(B\) is closed in a Euclidean space. This is the precise relative inverse-image operation retained by the axiom. |
| M4, 120/003 | The product \(A\times B\) is compact; its defining formula is the conjunction of the formulas for \(A\) and \(B\). |
| Optional M0, 120/007 | \(\mathbb R\) is noncompact in its usual topology, so these two concrete compact models follow the non-M0 branch explicitly allowed on scan 7. M0 and M9 on this underlying real topological space cannot both hold: they respectively put \(\mathbb R\) in \(\mathcal M_1\) and require that member to be compact. |
| M5, 120/010 | Finite unions of compact sets are compact; the empty set is compact. |
| M6, 120/013 | For nonempty closed \(Z\subseteq X\subset\mathbb R^n\), put \(h(x)=d(x,Z)\) and \(q(x)=(h(x),h(x)x_1,\ldots,h(x)x_n)\). The zero fibre is \(Z\), and equality \(q(x)=q(y)\) off \(Z\) gives \(h(x)=h(y)>0\) followed by \(x_i=y_i\) for every \(i\). Each graph is compact; \(Z=\varnothing\) is handled by \(h=1\). |
| M7, 120/013 | A moderate scalar function on compact \(Z\) is continuous by the compact-graph argument. Extend it continuously to the ambient Euclidean space by Tietze, or definably and continuously by the cited definable Tietze theorem, and restrict to compact \(X\); the restricted graph is compact. |
| M8, 120/015 | \(\mathbb R=\bigcup_{N\geq1}[-N,N]\), a filtered union of compact definable parts. |
| M9, 120/017 | The real line is Hausdorff and the members of each family are compact by definition. |
| M10, 120/018 | The closed intervals \([x-\varepsilon,x+\varepsilon]\), \(\varepsilon>0\), form a compact neighbourhood basis at \(x\). Real parameters supply these intervals in \(\mathcal S\). |
| M11(a), 120/021 | \(\{0\},\{1\}\) are compact definable sets. In fact \(R_0=\mathbb R\) for the chosen parameter convention. |
| M11(b), 120/021 | The restrictions of difference and multiplication to compact \(A\subset\mathbb R^2\) are continuous definable maps, with compact graphs. |
| M11(c), 120/021–023 | On compact \(A\subset\mathbb R^*\), inversion is continuous and has compact image \(A^{-1}\); use \(B=A^{-1}\) itself. The graph is the closed level set \(xy=1\) inside the compact rectangle \(A\times B\). |

### Q3-03 — The Boolean and compact operations are related by an explicit reconstruction

**Source:** 120 scans 3–5, 7, 17. **Kind:** unpursued implication; reader's construction. **Quote:** “\(\mathcal M_n\subset\mathcal P(R^n)\)”.

For the o-minimal realization \(K_n(\mathcal S)\), let \(\mathcal B_n\) be the Boolean algebra generated by these compact definable sets and use \(\tau_n(x)_i=x_i/\sqrt{1+x_i^2}\); then the formula \(\mathcal S_n=\{\tau_n^{-1}(B):B\in\mathcal B_n,\ B\subset(-1,1)^n\}\) recovers the original definable family. The proof is that every bounded definable set is a finite union of locally closed cells, each cell \(C\) is its compact closure minus the compact frontier relative to that closure \(\operatorname{cl}(C)\setminus C\), and \(\tau_n\) and its inverse are definable; the reverse containment follows directly from Boolean closure. This **adds** a specified passage from compact pieces to unrestricted definable sets beside C147 scans 181–184's passage from local pieces to a space, and bears on **WG2 B15 (§1.2)** without a localization conclusion. **Confidence: high** in this formula for the fixed o-minimal realization; no reconstruction claim for arbitrary M1–M11 is made.

### Q3-04 — A named geometric comparison has specified inverse assignments

**Source:** 120 scans 17–20. **Kind:** unpursued implication; literature comparison. **Quote:** “faisceau des germes de fonctions modérées”.

Van den Dries–Miller's analytic-geometric categories are related to o-minimal expansions of \(\mathbb R_{\mathrm{an}}\) by the actual inverse assignments \(\mathcal C\mapsto\mathcal S(\mathcal C)_n=\{A:A\in\mathcal C(\mathbb P^n(\mathbb R))\}\) and \(\mathcal S\mapsto\mathcal C(\mathcal S)\), the latter tested in analytic charts; equivalently the first uses the displayed \(\tau_n\). This supplies a named and proved global/local comparison to examine beside the compact-piece and sheaf descriptions on scans 17–20, while the explicit all-compact model in Q3-02 records what M1–M11 alone permits. It **adds** exact comparison assignments to C147 scan 182's sheafification language and bears on **WG2 B15 (§1.2)**; it supplies no change to **BISITE D.12**. The source is van den Dries–Miller, §§1–3 and Appendix D, with the 2012 corrections consulted.

### Exact modern definition: the coordinate operations compared

Coste, *Topological types of fewnomials* (1998), printed p. 82, gives S1–S6 and the graph definition of maps; the primary PDF is saved at `research_sources/coste-bcp44.pdf`. This table records the comparison in the already fixed family \(D_n=\mathcal S_n\); it does not combine separate manuscript conditions into an unstated axiom system.

| Modern clause | Actual manuscript operation and map in the realization |
|---|---|
| S1: Boolean algebra containing the ambient power | M0 supplies \(R^n\), M5 supplies unions, and M3 supplies intersections; complementation is explicit for the early 121 family (PDF 4). For the compact family the reconstruction Q3-03 explicitly performs Boolean completion followed by \(\tau_n^{-1}\). |
| S2: diagonals | M1 sends \(R^{n-1}\) under a coordinate-repetition map to \(\Delta_{ij}=\{x:x_i=x_j\}\). This uses M0 in the all-definable realization; on a compact domain it gives the corresponding compact diagonal. |
| S3: cylinders | The exact map is \((A,R)\mapsto A\times R\), using M4 and M0. |
| S4: coordinate projection | Use \(u:[1,n]\hookrightarrow[1,n+1]\); the manuscript's \(u^*\) is \((x_1,\ldots,x_{n+1})\mapsto(x_1,\ldots,x_n)\). |
| S5: addition and multiplication graphs | M11(b) on \(A=R^2\) gives difference and multiplication; the graph of addition follows from \(x+y=x-(0-y)\) by the proved graph-composition formula. |
| S6: one-dimensional finiteness | In the real-line realization of the early 121 family, finite locally closed decomposition plus clause (f) gives the finite interval/point conclusion proved at Q3-06. The compact family alone has the explicit Cantor countermodel Q3-02. |
| Maps | \(\Gamma_f\in D_{m+n}\) is precisely definability of \(f\); \(\Gamma_f\in K_{m+n}\) gives exactly continuous definable \(f\) on compact definable source and target, by the graph-projection homeomorphism. Q3-07 calculates the inclusion functor on these arrows. |

For the transported spaces of 120/006–007, choose a presentation \(i_X:|X|\xrightarrow\sim A_X\) and send an arrow to \(i_Y f i_X^{-1}\). These formulas preserve identities and composition, while the inverse assignment gives a concrete model its identity presentation; the maps \(i_X\) are the natural comparison isomorphisms. Thus the object/arrow calculation extends from embedded models to the manuscript's transported structures, with the specified charts supplying the equivalence data.

### Cote 121: primary manuscript and exact comparison

**All 121 scan references below now mean PDF page numbers including the cover, as required by the user; archive footer numbers are separate.** The official PDF is `research_sources/121-ranged.pdf` (27,378,881 bytes; SHA-256 `fc7b1ba2e63ebafaa72cfb6cf2dfcc76676b00833ae2d878aebf5502d146f37b`). It has 73 PDF pages: the modern wrapper is PDF page 1, so archive scan `s` is PDF page `s+1`; the handwritten folio is a third, separately reported numbering. The primary checks for this Q3 comparison used PDF scans 004–024 and 070–073 (archive footers 003–023 and 069–072); the Q4 worker checked PDF scans 030–037 (archive footers 029–036) after I located the diagram/stratification discussion there. This is a located comparison of those passages, not a claim that every paragraph of all 72 archive scans was transcribed or reviewed.

### The two presentations actually visible in cote 121

The following table contains the manuscript-content summary; the verification and examples following it are the reader's constructions. The final compact presentation is separately located from the earlier Boolean-family discussion: no sentence in the checked final four leaves identifies its families with the earlier family or carries over all of that family's conditions.

| Primary locus | Written mathematical data, paraphrased |
|---|---|
| 121/004 (footer 003; handwritten 5) | \(\mathcal F\subseteq\mathcal P(X)\): finite Boolean operations; finite-valued functions. |
| 121/005–006 (footers 004–005; handwritten 6–7) | Closure; dense interior in closure; descending closed nowhere-dense chains terminate. |
| 121/010 (footer 009; handwritten 11) | (f): locally closed members have finitely many connected components, each admissible. |
| 121/015–017 (footers 014–016) | Finite compatible decompositions; connected leaves use (f). |
| 121/019–024 (footers 018–023) | Restriction and local completion; compactness gives global equality. |
| 121/070–071 (footers 069–070; handwritten 71–72) | \(C_n\): coordinate maps, products, graphs, transport, coverage. |
| 121/072 (footer 071; handwritten 73) | Hausdorff base; compact models; model neighbourhoods; function sheaf. |
| 121/073 (footer 072; handwritten 74) | Finite unions/gluing; pushout and scalar-extension questions. |

For the displayed operations, send each coordinate, product or scalar function to itself; the corresponding 120 labels are M1, M4, M5 and M7–M10. This supplies the comparison maps without ordering the undated drafts chronologically.

### Q3-05 — The Boolean-family and compact-model presentations have an actual shared realization

**Source:** 120/003–024; 121/004–010 and 070–073. **Kind:** unpursued implication; reader's construction. **121 quote anchor:** “parties de X”.

For the same fixed o-minimal \(\mathcal S\), put \(D_n=\mathcal S_n\), \(K_n=\{A\in D_n:A\text{ compact}\}\), and \(\mathcal F_X=\{A\subseteq X:A\in D_n\}\) for a definable \(X\subseteq\mathbb R^n\); the displayed assignments supply the power families, compact parts and Boolean families without changing their underlying subsets. The compact graph map is sent to its identical definable graph, while a definable map \(f:X\to Y\) acts on Boolean families by the specified inverse-image homomorphism \(f^{-1}:\mathcal F_Y\to\mathcal F_X\). This **adds** actual comparison assignments beside C147/181–184's local-stratum and sheaf constructions, and bears on **WG2 B15 (§1.2)** as an unchecked choice of geometric setting. **Confidence: high**, because the operations are verified below; no equivalence for every manuscript family is asserted.

### Verification for the early 121 family

For \(\mathcal F_X=D(X)\), Boolean closure is built into the defining formulas. Closure is definable by
\[
x\in\overline A^{\,X}\quad\Longleftrightarrow\quad
x\in X\ \land\ \forall\varepsilon>0\ \exists a\in A\ (\|a-x\|<\varepsilon).
\]
Every definable set is a finite union of locally closed cells; a dense finite union of locally closed subsets of a space has dense interior, so the relative-interior clause follows for \(A\subseteq\overline A^X\). Here is an elementary proof of that finite-union assertion: write each locally closed piece as \(F_i\cap U_i\), discard the union of the closed nowhere-dense boundaries of the \(F_i\), and work in the resulting dense open part, where every surviving \(F_i\) is open as well as closed; there the pieces are open, and density supplies a nonempty piece in every remaining open set.

For a closed nowhere-dense inclusion \(B\subset A\), the identity \(B\subseteq\operatorname{cl}(A\setminus B)\setminus(A\setminus B)\) and the o-minimal frontier dimension inequality give
\[
\dim B<\dim(A\setminus B)\leq\dim A.
\]
Thus a chain of the kind on 121/006 has at most \(n+1\) nonempty dimension levels inside \(\mathbb R^n\). Finally the component theorem gives the precise finite family of connected components, each definable, required by 121/010. The cited inputs are van den Dries–Miller 4.2, 4.3 and 4.7(1), checked in the author text cited in bibliography item 1; the displayed closure formula and decreasing-dimension application are the present verification.

### Q3-06 — The one-dimensional finiteness clause has a direct proof in this comparison

**Source:** 121/006 and 010; compared to 120/003 and 017. **Kind:** unpursued implication; explicit proof. **121 quote anchor:** “connexes”.

The early 121 construction decomposes a family member into finitely many locally closed pieces (121/006–009), and its clause (f) splits each piece into finitely many connected members; on \(X=\mathbb R\), a connected subset is an interval or a point, since a missing \(c\) between two of its points separates it into the relatively open parts below and above \(c\). Hence the manuscript's actual finite decomposition and finite-component operations give the one-dimensional finite interval/point conclusion in that real-line realization, and the Cantor set used in Q3-02 fails exactly the finite-component test. This **adds** a precise finiteness mechanism to C147/184's compact-stratification claim and bears on **WG2 B15 (§1.2)** without settling its open localization problem. **Confidence: high** in this elementary real-line argument; it does not attribute coordinate-projection or real-field closure to the early family on an arbitrary topological \(X\).

### Verification detail for Q3-06: the finite decomposition recursion

The finite locally closed decomposition used in that argument has an explicit recursion with precisely the written operations:
\[
A_0=A,\quad F_j=\operatorname{cl}(A_j),\quad
U_j=\operatorname{int}_{F_j}(A_j)
      =F_j\setminus\operatorname{cl}_{F_j}(F_j\setminus A_j),\quad
A_{j+1}=A_j\setminus U_j.
\]
All these sets remain in the Boolean family, each \(U_j\) is open in the closed set \(F_j\), and \(F_{j+1}\subseteq F_j\setminus U_j\) is closed and nowhere dense in \(F_j\) by the dense-interior clause. The descending-chain clause therefore ends the recursion, giving the required finite disjoint union \(A=\coprod_jU_j\); this verifies the step without inserting a cell-decomposition theorem as a new manuscript axiom.

### Q3-07 — Optional M0 is realized by all definable sets, with a calculated map comparison

**Source:** 120/007 and 021; 121/004 and 070–073. **Kind:** own construction. **120 quote:** “Oublions les structures topologiques”.

The family \(D_n=\mathcal S_n\) realizes M0, M1–M8 and M11: M6 uses \(q(x)=0\) on \(Z\) and \(q(x)=(1,x)\) off \(Z\), M7 extends a scalar function by zero off \(Z\), and the remaining clauses use the displayed Boolean, coordinate and field formulas. Its graph-defined arrows are all definable functions, and the compact-model inclusion sends each \(K_n\)-object and continuous definable arrow to the same object and arrow in this model; the step function \(f:[0,1]\to\{0,1\}\), \(f(0)=0\), \(f(x)=1\) for \(x>0\), is an explicit definable arrow whose graph omits its limit point \((0,1)\), so it is not an arrow of the compact-graph model. This **adds** the exact functor and its arrow-level limit beside C147/182's function-sheaf discussion and bears on **WG2 B15 (§1.2)** at its unchanged unchecked status. **Confidence: high**, from the piecewise formulas and the missing graph limit point; the Euclidean compactness axiom M9 is not asserted for \(D_n\), which contains \(\mathbb R\).

### Q3-08 — Local completion has an explicit inclusion and an explicit new section

**Source:** 120/019–020; 121/019–024. **Kind:** unpursued implication; reader's construction. **121 quote anchor:** “Localisation”.

For \(\mathcal F=D(\mathbb R)\), the map to the locally completed family is the literal inclusion \(A\mapsto A\), and the integer subset \(\mathbb Z\) belongs to the completion because every point has an interval meeting it in either a singleton or the empty set. It is absent from \(D(\mathbb R)\) by the finite interval/point clause; on compact definable \(X\), finitely many definable neighbourhoods cover \(X\), and the locally defined set is the finite union of its definable traces, proving equality of the two families there. This **adds** a tested sheaf-completion map to C147/182's presheaf-to-sheaf passage and bears on **WG2 B15 (§1.2)** and **BISITE D.12**, the latter remaining open in the supplied register. **Confidence: high**, because both the new section and the finite-cover reconstruction are explicit.

### Q3-09 — Cote 121's final scalar-extension question has the same verified modern witness

**Source:** 121/072–073 and 120/013–014. **Kind:** self-flagged question; construction answering it in the specified model. **121 quote anchor:** “Question”.

On the compact definable realization, the map requested on 121/073 is the restriction to \(X\) of the definable continuous extension from Aschenbrenner–Fischer, Lemma 6.6; the quotient coordinates and amalgam maps in A120-07–A120-08 then give the two-inclusion pushout. This **restates**, at the exact extension-map level, the operation in 120/013–014 and **adds** a model with witnesses beside C147/164 and 171's amalgam diagrams. It bears on **STRATA C.1/C.3/C.6** and **WG2 B15 (§1.2)** at the return-claim statuses stated above, without elevating them or the unchecked plan to a new settlement. **Confidence: high** for the compact definable construction, with the arbitrary-span scope question still recorded at A120-06.

### Q3-10 — The admissible scalar field records a genuine parameter choice

**Source:** 120/004–005, 021–023. **Kind:** own construction. **120 quote:** “\(R_0\) est un sous-corps de \(R\)”.

Keep the ambient topological field \(R=\mathbb R\), but take only compact semialgebraic subsets defined over the real algebraic field \(F=\mathbb R\cap\overline{\mathbb Q}\); the earlier M1–M11 verification still works, since projection preserves this coefficient field, the distance and extension formulas introduce no new parameters, and rational-endpoint intervals supply M10 at every real point. Here \(R_0=F\): every \(a\in F\) supplies its singleton, while a finite Boolean formula in polynomial signs over \(F\) is locally constant at a transcendental real number because none of its nonzero polynomials vanish there, so it cannot define that singleton. This **adds** an explicit parameter convention and its inclusion into the all-real-parameter model beside C149/105 and 122's field language, and bears on **WG2 B15 (§1.2)** without identifying that field with the arithmetic fields in those context pages. **Confidence: high**, from the sign calculation and the parameter-preserving formulas; the main realization Q3-01 deliberately used all real parameters, making \(R_0=\mathbb R\).

### Q3-11 — A real-closed-field interval tests the exact topological clauses

**Source:** 120/017–018; 121/010 and 072. **Kind:** unpursued implication; reader's explicit test. **120 quote:** “\(R\) séparé”; “compactes”.

For \(F=\mathbb R\cap\overline{\mathbb Q}\), the coefficient inclusion \(F\hookrightarrow\mathbb R\) induces the concrete interval embedding \(i:[0,1]_F\hookrightarrow[0,1]_{\mathbb R}\), and \([0,1]_F\) is definably compact by Peterzil–Steinhorn, Theorem 2.1, being closed and bounded in the pure real-closed-field structure. Choose a transcendental \(c\in(0,1)\): the cover consisting of \([0,1]_F\cap(-\infty,a)\) for \(a\in F,\ a<c\), and \([0,1]_F\cap(b,\infty)\) for \(b\in F,\ b>c\), has no finite subcover, because a finite choice covering both endpoints must contain both kinds of set and leaves algebraic points between its largest \(a\) and smallest \(b\). The same cuts between any two algebraic points show that all topological connected components of \([0,1]_F\) are singletons, so this concrete interval fails both literal topological compactness and the finite-component test, despite its one-interval definable description. This **adds** a checked base-field map beside C149/105's field vocabulary and C147/184's compactness discussion, with **WG2 B15 (§1.2)** still unchecked; **confidence high**, because the cover and each separating cut are explicit.

### Verification detail for Q3-10: preservation of the scalar parameter field

The checked proof of Aschenbrenner–Fischer Lemma 6.6 gives this extension on a nonempty closed \(Z\), writing \(g=\tau\circ f\):
\[
\tau(t)=\frac32+\frac{t}{2\sqrt{1+t^2}},\qquad
G(x)=
\begin{cases}
g(x),&x\in Z,\\
\displaystyle\inf_{a\in Z}\frac{g(a)\,d(x,a)}{d(x,Z)},&x\notin Z,
\end{cases}
\qquad \widetilde f=\tau^{-1}\circ G.
\]
Every constant displayed is rational, the quantified variable \(a\) ranges over the already defined \(Z\), and distances and the infimum are specified by order-field formulas using only the coefficients of \(Z\) and \(f\); real-closed-field quantifier elimination consequently produces semialgebraic definitions over that same \(F\). This is the reason for parameter preservation in Q3-10, rather than an assumption that an unspecified definable extension automatically preserves parameters; the empty-domain case uses the zero extension.


#### Additional verification of the displayed extension on compact \(Z\)

For the nonempty compact domain used here, put \(m=\min_Z g>1\) and \(M=\max_Z g<2\). The numerator \(H(x)=\min_{a\in Z}g(a)\|x-a\|\) satisfies \(|H(x)-H(y)|\le M\|x-y\|\), by the triangle inequality, so \(G=H/d(\,\cdot\,,Z)\) is continuous off \(Z\). A nearest point gives \(G(x)\le M\), while every distance ratio is at least one and gives \(G(x)\ge m\); in particular \(\tau^{-1}(G(x))\) is defined.

A minimizing point \(a_x\) obeys \(\|x-a_x\|\le(M/m)d(x,Z)\), so \(a_x\to z\) as \(x\to z\in Z\). With \(b_x\) a nearest point, the inequalities \(g(a_x)\le G(x)\le g(b_x)\) and \(a_x,b_x\to z\) prove continuity at \(z\). Finally \(\tau^{-1}(s)=(2s-3)/\sqrt{1-(2s-3)^2}\) uses rational coefficients, completing the parameter check; the empty-domain extension is zero. These are direct verifications of the already displayed construction, also checked independently in the research review.

### Scope of the joint answer

The supported positive correspondences are the compact definable model and its graph arrows, the all-definable realization of the optional-M0 algebraic branch, the explicit Boolean compactification formula Q3-03, the early 121 family \(D(X)\) with its finite-dimensional and finite-component properties, and the named analytic-geometric and weak-polytope constructions Q3-04/A120-24. The proved all-compact counterexample is scoped to **120 M1–M11 without optional M0**; it is not a counterexample to the early 121 finite-component requirement. The precise remaining verification for a claimed equivalence of the entire manuscript apparatus with an o-minimal structure is to identify the actual family in each finite power, show that the early 121 Boolean/finiteness operations apply to those same families, and account for the real-field and graph-map convention; the checked leaves do not supply that identification, and no theorem with those missing identifications inserted as hypotheses is proposed here.

### Page-level notes on the mathematical development

### A120-01 — The graph calculus can be checked without a tameness finiteness axiom

**Source:** 120 scans 3–6. **Kind:** unproved claim, with explicit verification. **Quote:** “\(gf\) modéré”.

The composite graph is \(\Gamma_{gf}=p_{13}\bigl(p_{12}^{-1}(\Gamma_f)\cap p_{23}^{-1}(\Gamma_g)\bigr)\) inside \(A\times B\times C\), with the relative inverse images taken in that moderate product, so M3, M4 and M1 perform the three operations and coordinate interchange performs graph inversion. This **adds** an elementary graph-level construction beside the product diagrams in C147 scans 165 and 168; the context search found no earlier M-labelled graph calculus in the supplied selections. It bears on the choice of a concrete category in **WG2 B15 (§1.2)**, whose status remains an unchecked plan.

### A120-02 — Empty objects and admissible points are separate steps in the written construction

**Source:** 120 scans 4–5. **Kind:** unpursued implication; reading caution. **Quote:** “\(\mathrm{Card}\ R_0\ge2\)”.

The revision from \(R_0\ne\varnothing\) to \(|R_0|\ge2\) makes the empty-set conclusion use the actual intersection \(\{a\}\cap\{b\}=\varnothing\) for two distinct admissible points; one admissible point supplies no such intersection argument. This **adds** a nullary/finite-object check to C147 scan 164's elementary point object, and the exact formula \(\{x\}\in R^n\) on scan 5 remains a reading question rather than an edited formula. No selected register entry settles this point; **WG2 B15 (§1.2)** supplies only the surrounding programme.

### A120-03 — Finite unions impose a real extra closure operation

**Source:** 120 scans 6 and 10. **Kind:** unpursued implication; concrete example. **Quote:** “parties de cardinal \(\le1\)”; “stable par réunions finies”.

On a set containing distinct \(0,1\), the scan-6 family of empty and singleton subsets contains \(\{0\}\) and \(\{1\}\) while their union has cardinal two, so this example records exactly the extra operation introduced by M5. This **adds** an axiom-level finite-union test to C147 scan 184's finite-strata discussion, whose compactness argument concerns a specified stratification. The connection is to **WG2 B15 (§1.2)** as a proposed ambient framework, without changing its unchecked status.

### A120-04 — The categorical reconstruction is a claim to verify at the stated data

**Source:** 120 scans 7–8. **Kind:** unproved claim. **Quote:** “la donnée d'un \(\mathcal M_*\) est équivalente”.

The proposed reconstruction sends \(\mathcal M_n\) to the subsets underlying subobjects of \(R^n\) in \((\mathcal E,R,U)\), with \(U\) the faithful conservative transportable underlying-set functor carried from scan 6. A proof must check that the images of the coordinate maps land among those subobjects and that the recovered graph morphisms return exactly \(\mathcal E\); these are the actual maps behind the asserted equivalence. This **adds** a concrete-recognition problem beside C147 scan 150's topos-gluing equivalence, and bears on **WG2 B15 (§1.2)** without identifying that open-test localization with this reconstruction.

### A120-05 — Finite graph descent is supplied on the next sheet

**Source:** 120 scans 9–12. **Kind:** unproved claim followed by its proof. **Quote:** “leur réunion aussi”.

The scan-9 colimit assertion is explained on scan 12 by the equality \(\Gamma_f=\bigcup_i(g_i\times1_Y)(\Gamma_{f_i})\), whose finite union is moderate by M5. This **adds** an explicit finite-graph descent argument to the amalgamated-space diagrams of C147 scans 164 and 171; it is the quotient-set universal map and its graph that are checked here. It bears on **STRATA C.1, C.3, C.6** as an elementary comparison of gluing mechanisms, with the return-claim statuses and review limits stated above.

### A120-06 — The scan-11 separation criterion needs its span scope recorded

**Source:** 120 scans 10–11 and 13. **Kind:** reading question; own concrete test. **Quote:** “les \(f_\alpha\) … séparent … les pts de \(X_1\)”.

For the finite discrete span \(X_1=Z=\{0,1\}\), \(i_1=1_Z\), \(X_2=\{*\}\), and \(i_2\) constant, the pushout is \(\{*\}\), but every compatible pair of scalar functions is constant on \(X_1\), so scan 11(b)'s point-separation requirement fails for this span from scan 10's unrestricted question. Scan 13 expressly writes two inclusions in its proved construction, and the note should preserve this narrower geometric scope rather than silently extend the criterion to every span. This **differs** from the inclusion diagrams in C147 scans 164 and 171 and bears on **STRATA C.1/C.3**, whose specified crossing data remain untouched. **Confidence: high**, because every set and map in the test is displayed.

### A120-07 — The quotient by one moderate part is encoded by a finite map

**Source:** 120 scan 13. **Kind:** unpursued implication; explicit construction. **Quote:** “contraction de \(Z\) en un point”.

Write \(q=(f_\alpha):X\to R^A\); M6 says \(q^{-1}(e)=Z\) and gives point separation on \(X\setminus Z\), so the image \(q(X)\) has exactly the fibres prescribed by collapsing \(Z\), and its graph description supplies the moderate quotient. This **adds** a finite-coordinate quotient model beside the groupoid amalgam of C147 scan 156 and the spatial amalgam of scan 164. It bears on **WG2 B15 (§1.2)** and the elementary gluing setting of **STRATA C.1/C.3**, without settling their enhanced coefficient questions.

### A120-08 — M7 is the extension input in the amalgam construction

**Source:** 120 scans 13–14. **Kind:** unproved claim with manuscript proof mechanism. **Quote:** “qui prolonge”.

M7 extends the common embedding \(Z\hookrightarrow R^I\) to maps \(a_i:X_i\to R^I\), and M6 supplies \(h_i:X_i\to R^{A_i}\) with fibre \(Z\) over \(e_i\); the two maps \((a_1,h_1,e_2)\) and \((a_2,e_1,h_2)\) into \(R^{I\amalg A_1\amalg A_2}\) have exactly the required common image of \(Z\). Their finite union is the moderate model used by scan 12's graph-descent proof. This **adds** coordinate witnesses to C147 scan 171's product-of-spans diagram and bears on **STRATA C.1/C.3/C.6** as a comparison of explicit constructions, at the return-claim statuses stated above.

### A120-09 — Scalar extension is a precise modern point of contact

**Source:** 120 scan 13. **Kind:** unpursued implication; literature comparison. **Quote:** “\(\exists g:X\longrightarrow R\) modérée”.

In the compact definable realization, \(Z\subset X\) is closed and a moderate \(f\) is continuous, so Aschenbrenner–Fischer, Lemma 6.6, supplies a definable continuous extension to \(\mathbb R^n\), whose restriction to \(X\) has compact graph and is exactly M7's required arrow. This **adds** a verified extension theorem to the neighbourhood and gluing constructions of C147 scans 140–142 and 164; the supplied context contains no Tietze or M7 statement. The consequence bears on **WG2 B15 (§1.2)** only as an available tame model, not as a resolution of **BISITE D.12**.

### A120-09a — The marginal one-inclusion amalgam has a coordinate construction

**Source:** 120/013, margin, and 014. **Kind:** unpursued implication; reader's construction. **Quote:** “une … flèche … libre” (the frozen reading remains uncertain).

For the displayed span \(X_1\hookleftarrow Z\xrightarrow{u}X_2\), choose \(j:X_2\hookrightarrow R^I\), extend \(ju\) to \(a:X_1\to R^I\) by M7, and choose \(h:X_1\to R^A\) from M6 with \(e\in R_0^A\) and \(h^{-1}(e)=Z\); use the two maps \((a,h):X_1\to R^{I\amalg A}\) and \((j,e):X_2\to R^{I\amalg A}\). Their union identifies exactly \(z\sim u(z)\), since \(h\) separates points off \(Z\), while its \(e\)-fibre records precisely the image of \(u\); M5 and the scan-12 graph formula prove the pushout universal property. This **adds** an explicit reading of the margin's proposed generalization beside C147/164 and 171, and bears on **WG2 B15 (§1.2)** and the **MPL_150_085-099+151_001-031 §106 [first-pass lead]** to STRATA gluing. **Confidence: high** for the construction, independently of the uncertain marginal noun.

### A120-10 — The strict ind-structure specifies its bounded pieces

**Source:** 120 scans 15–16. **Kind:** unpursued implication; comparison construction. **Quote:** “de réunion \(E\)”; “\(A\cap\mathcal Y\)”.

The collection \(\mathcal M_E\), its finite unions, and the inherited structures on its members specify the directed system of actual inclusions used by the strict ind-object; a locally moderate part is tested by intersection with each one of these members. This **adds** a bounded-piece system to the local-stratum structure in C147 scans 181–184, where the chosen local germs and their sheafification carry different explicit data. It bears on **CATHOT E.17** as an ind-presentation comparison and on **TOTASPH E.6** **[Proved, return's claim]** through the directed indexing family, but supplies no proof of the open homotopy-invariant representability problem in E.17.

### A120-11 — The manuscript warns about a specific subobject passage

**Source:** 120 scans 16–17. **Kind:** self-flagged limitation. **Quote:** “ne correspond pas néc. à une partie … modérée”.

The warning must be kept beside the quotient claim: that claim uses intersections with every moderate piece, while a categorical monomorphism is given by its arrows in the ind-category, and the manuscript explicitly refuses to identify the two descriptions without further work. This **adds** a subobject-recognition issue to C147 scan 183's locally immersed stratum inclusion, whose source topology is separately specified. It bears on **CATHOT E.17** and **WG2 B15 (§1.2)** as a constraint on the comparison data, without changing either status.

### A120-12 — Compact graphs prove the continuity assertion

**Source:** 120 scan 17. **Kind:** unproved claim with short verification. **Quote:** “c'est OK si … compactes”.

For a moderate \(f:A\to B\), the graph projection \(p:\Gamma_f\to A\) is a continuous bijection from a compact space to a Hausdorff space, hence is a homeomorphism, and \(f=\pi_B\circ p^{-1}\) is continuous. This **adds** the exact comparison map behind the topology functor beside the neighbourhood maps in C147 scans 140–142. It bears on **WG2 B15 (§1.2)** by supplying actual continuous maps, while its objectwise proof does not evaluate the open-test localization of **BISITE D.12**.

### A120-13 — Countability is explicitly retained in the topology claim

**Source:** 120 scan 18. **Kind:** unproved claim. **Quote:** “quand on suppose … ind-dénombrable”.

The assertion that the final topology restricts to the original topology of each moderate part is stated for an increasing sequence, and that quantifier must remain attached to the assertion during comparison with ind-categories. This **adds** a countable-exhaustion restriction beside C147 scan 184's locally finite stratification discussion. It bears directly on **CATHOT E.17**'s sequential ind-presentation problem, but concerns the topology of already supplied compact pieces rather than the existence of the homotopy-invariant presentation asked for there.

### A120-14 — M10 supplies the local neighbourhood witnesses

**Source:** 120 scan 18. **Kind:** self-flagged desideratum made an axiom. **Quote:** “On voudrait”.

M10 supplies moderate neighbourhoods in \(R\), and finite products plus intersection with a model \(X\subset R^n\) supply the corresponding neighbourhoods in \(X\). This **adds** concrete basis objects to the fundamental-neighbourhood systems used in C147 scans 181–182, while those context passages additionally impose connectedness and local-product requirements on strata. It bears on **WG2 B15 (§1.2)** as geometric input and leaves the realization question **BISITE D.12** open as recorded.

### A120-15 — Locality of maps uses compactness and finite unions together

**Source:** 120 scan 19. **Kind:** unproved claim with proof mechanism. **Quote:** “au voisinage de chaque pt”.

Compactness extracts finitely many moderate neighbourhoods covering the moderate domain \(X\); the local graphs then form the finite union of the global graph, so M5 proves moderation of the map. This **adds** a compact-to-finite descent mechanism beside C147 scan 182's passage from a presheaf to its associated sheaf. It bears on **STRATA C.6** only as a comparison of descent data and on **WG2 B15 (§1.2)** as local geometry; neither register conclusion follows solely from this finite-graph argument.

### A120-16 — Scalar functions are a concrete probe of the structure

**Source:** 120 scan 19. **Kind:** unproved claim; verification target. **Quote:** “connue quand on connaît … dans \(R\)”.

For a target embedding \(Y\hookrightarrow R^n\), a candidate map \(f:X\to Y\) is tested by its \(n\) scalar coordinate functions, and the graph is recovered by their simultaneous graph equations; this is the actual map-level mechanism behind the scalar-probe claim. This **adds** a ringed or function-sheaf presentation to C147 scan 182's sheaf of local stratifications. It bears on **WG2 B15 (§1.2)** but gives no equivalence between the open-test cosheaf construction of **BISITE D.1/D.12** and this scalar-function sheaf.

### A120-17 — The compact-containment wording has a direct interval test

**Source:** 120 scan 20. **Kind:** reading question; own concrete test. **Quote:** “les parties compactes sont les parties contenues dans une partie modérée”.

In the compact semialgebraic realization, \((0,1)\hookrightarrow[0,1]\) is a subset contained in a moderate part, but the cover \((0,1)=\bigcup_{n\ge3}(1/n,1)\) has no finite subcover, so the literal compactness equivalence on this line fails for this actual inclusion. Whether this phrase names the ideal of relatively compact subsets remains a reading question; the frozen sentence is retained. This **differs** from C147 scan 184's use of compactness for a given compact ambient space and bears on **WG2 B15 (§1.2)** and **BISITE D.12** as a warning about the actual category to compare. **Confidence: high** in the interval calculation; **low** in assigning an intended replacement wording.

### A120-18 — The marginal request about compact subparts tests the intended model

**Source:** 120 scan 20, margin. **Kind:** unproved claim or desideratum; own concrete test. **Quote:** “Dire qu'une partie compacte … est modérée”.

The ternary Cantor inclusion \(C\hookrightarrow[0,1]\) supplies a compact subpart of a compact semialgebraic space, while \(C\) has infinitely many points and no interval, so an o-minimal \(K_1(\mathcal S)\) cannot contain it. The proposed marginal closure therefore needs its own status recorded when comparing the text to that model; the all-compact model Q3-02 does satisfy it. This **adds** a specific compact-subobject test to C147 scan 184 and bears on **WG2 B15 (§1.2)** without deciding its open localization question. **Confidence: high**, from the displayed inclusion and the one-dimensional finiteness definition.

### A120-19 — The polynomial structure begins after topology is explicitly set aside

**Source:** 120 scans 21–22. **Kind:** unpursued implication. **Quote:** “Oublions les structures topologiques”.

The field section first asks for moderate graphs of \((x,y)\mapsto x-y\) and \((x,y)\mapsto xy\), so sums and products of scalar moderate functions are obtained by composing their joint graph with these two operations; constants come from \(0,1\in R_0\). This **adds** scalar algebra to C149 scan 105's ring/field objects and scan 122's local rings, whose particular arithmetic constructions are not identified with the manuscript's moderate function ring. No selected result directly settles this M11 calculation; **WG2 B15 (§1.2)** supplies the general geometric setting only.

### A120-20 — Subring and subfield conclusions occur on different sheets

**Source:** 120 scans 21 and 23. **Kind:** unproved claim with subsequent proof. **Quote:** “sous-anneau”; “sous-corps”.

The live scan-21 conclusion gives a subring, and scan 23 supplies inversion by the level set \(\{(x,y)\in A\times B:xy=1\}\), using M11(c)'s moderate bound \(B\); applying it to a nonzero admissible singleton yields its reciprocal singleton and the subfield conclusion. This **adds** the exact reciprocal construction to the field and valuation language in C149 scans 105 and 122. The supplied register has no direct moderate-scalar-field result, and none of the arithmetic status rows is altered by this elementary comparison.

### A120-21 — The inverse graph's dimension label remains a reading question

**Source:** 120 scans 22–23. **Kind:** reading question. **Quote:** “\((x,x^{-1})\in R^2\)”; “\(\in\mathcal M_1\)”.

The frozen scan-22 line places the inverse graph in \(\mathcal M_1\), while scan 23 constructs it as a subset of \(A\times B\subset R^2\); this is an internal dimensional reading question and provides no permission to rewrite the subscript. It **adds** a precise notation question beside C149 scan 105's expressly announced “révision de notations”. No selected register entry settles this reading.

### A120-22 — The zero-set argument supplies the separation off the collapsed part

**Source:** 120 scans 23–24. **Kind:** unproved claim with explicit argument. **Quote:** “séparent les pts de \(X\setminus Y\)”.

The joint map \(x\mapsto(f_\alpha(x),f_\alpha(x)g_\beta(x))_{\alpha,\beta}\) sends \(Y\) to zero, and equal images of two points outside \(Y\) give a shared nonzero \(f_\alpha\), then equality of every \(g_\beta\), and hence equality of the points. This **adds** the algebraic multiplication mechanism to the quotient construction of C147 scan 156, while the more directly comparable internal statement is M6 at 120 scan 13. It bears on **WG2 B15 (§1.2)** as an explicit quotient map and has no consequence for the unresolved enhanced gluing statuses.

### A120-23 — The final sentence on scan 24 overstates that same separation

**Source:** 120 scan 24, final proposition. **Kind:** reading question; own concrete test. **Quote:** “sépare les pts de \(X\)”.

On \(X=[0,1]\), \(Y=\{0,1\}\), use \(f(x)=x(1-x)\) and \(g(x)=x\): the resulting map \(x\mapsto(f(x),f(x)g(x))\) sends both endpoints to \((0,0)\), exactly as the quotient requires, so its coordinates cannot separate those two points of \(X\). The preceding paragraph's separation on \(X\setminus Y\) is the statement supported by the displayed proof; the final larger set and the misplaced-looking \(\lambda\) underbrace remain untouched in the transcription. This **adds** an explicit collapsed-fibre check to C147 scan 164's gluing data and bears on **WG2 B15 (§1.2)** only at the elementary quotient level. **Confidence: high**, because the two endpoint values are computed directly.

### A120-24 — A countable compact-definable exhaustion gives a precise named comparison object

**Source:** 120 scans 15, 18–20. **Kind:** unpursued implication; literature comparison. **Quote:** “suites croissantes d'espaces modérés”.

For a sequence \(X_1\subseteq X_2\subseteq\cdots\) of compact definable spaces, take the same union and stage inclusions, use definable open sets and continuous definable scalar functions on each stage, and declare an open family admissible when its trace on every stage has a finite subfamily covering that trace's union; this is the countable-exhaustion construction entering Piękosz's **weak polytopes** (his §6, WD1–WD6). The identity on every \(X_n\) is the comparison of objects, and maps represented by compatible definable maps from each source stage into some target stage supply the corresponding maps of these presentations. This **adds** a named stagewise model beside C147 scan 182's local sheaf construction and bears on **CATHOT E.17** without proving its general representability claim. **Confidence: high** for the displayed countable presentation; no equivalence of all possible manuscript ind-objects with all weakly definable spaces is asserted.

### Primary bibliography and verification scope

1. Lou van den Dries and Chris Miller, *Geometric categories and o-minimal structures*, Duke Mathematical Journal 84 (1996), 497–540; author revision of 20 February 2001: <https://people.math.osu.edu/miller.1987/newg.pdf>. Definitions and comparison: §§1–3 and Appendix D; graph operations: Appendix B; finiteness and dimension inputs: 4.2, 4.3 and 4.7(1).
2. Chris Miller, *An upgrade for “Geometric categories and o-minimal structures”*, version 14 November 2012: <https://people.math.osu.edu/miller.1987/geofix.pdf>. The corrections were consulted; the present notes use no Whitney-stratification-of-maps assertion.
3. Matthias Aschenbrenner and Andreas Fischer, *Definable versions of theorems by Kirszbraun and Helly*, Proceedings of the London Mathematical Society 102 (2011), 468–502, DOI <https://doi.org/10.1112/plms/pdq029>; author manuscript <https://www.mat.univie.ac.at/~maschenbrenner/pdf/KH.pdf>, §6.2, Lemma 6.6 and its proof, p. 31. The proof was checked with its definably complete ordered-field and closed-domain scope; the empty-domain extension here is zero.
4. Artur Piękosz, *O-minimal homotopy and generalized (co)homology*, Rocky Mountain Journal of Mathematics 43 (2013), 573–617; author version <https://arxiv.org/abs/0808.3866>, §6, pp. 20–21, especially WD1–WD6 and the definition of weak polytope. Only the specified countable construction is used; the page range was checked against the author's publication list <https://piekosz.pl/>.
5. Heinrich Tietze, *Über Funktionen, die auf einer abgeschlossenen Menge stetig sind*, Journal für die reine und angewandte Mathematik 145 (1915), 9–14; metadata <https://geodesic.mathdoc.fr/item/JRAM_1915__145_149430/>. The original full text was not successfully fetched, so this is a bibliographical pointer; the extension verification uses item 3 and the displayed calculation.
6. Grothendieck, Montpellier cote 121, <https://grothendieck.umontpellier.fr/121.pdf>, 73 current PDF pages including the institutional cover. The exact selected primary-image checks and page-number convention are recorded above; source hashes and retrieval details are in the research ledger.
7. Michel Coste, *Topological types of fewnomials*, Banach Center Publications 44 (1998), 81–92: <https://matwbn.icm.edu.pl/ksiazki/bcp/bcp44/bcp4416.pdf>, printed p. 82 / PDF p. 2, clauses S1–S6 and graph-defined maps. Direct retrieval succeeded after the web reader returned 403; the operation table gives the present reader's comparison.
8. Ya'acov Peterzil and Charles Steinhorn, *Definable Compactness and Definable Subgroups of o-Minimal Groups*, Journal of the London Mathematical Society 59 (1999), 769–786, DOI <https://doi.org/10.1112/S0024610799007528>. Definition 1.1 and Theorem 2.1 with its proof were read in the author-associated full-text copy <https://www.academia.edu/18806220/Definable_Compactness_and_Definable_Subgroups_of_o_Minimal_Groups>.


## 5. Comparison of tame theories, Shiota and the final diagram question

The following items specify the comparison maps and the verified scope of the cited results. Appendices A–B give the complete calculations for the two readings of 120/025 that are explicitly tested: simultaneous isomorphism of finite diagrams and the displayed nested-subset example.

### Q4-01 — The comparison has an explicit morphism

**Source:** 120/025, “espaces modérés”; *Esquisse* §5, printed pp. 29–30. **Kind:** unpursued implication / literature comparison. **Context search:** `isotop`, `comparaison`, `modér`, `système`; `MPL_147_138-190_transcription.tex`, scans 177–180 and 190; `RESULTS_STATE.md`, **MPL_150_001-043 Q4b** [first-pass lead], **WG2 §1.1 #6** [unchecked plan].

Grothendieck takes \(T\) finer than \(T'\) and \(T\)-moderate spaces \(X,Y\), and writes the canonical map \(\operatorname{Isom}_{T}(X,Y)\to\operatorname{Isom}_{T'}(X,Y)\) with a requested bijection on components and homotopy equivalence of its semisimplicial models, together with requested analogous comparisons for constrained map families and systems of spaces; “catégories isotopiques (ou même ∞-isotopiques)” records the specified levels [S1]. This **adds** a precise comparison target to the 147/177–180 system of normal/tubular pieces and to the 147/190 promised use of local triviality. It **restates with an exact map** the comparison lead in **MPL_150_001-043 Q4b**; its first-pass status is unchanged.

### Q4-02 — What the compact Hauptvermutung actually supplies

**Source:** 120/025, “espaces modérés”; *Esquisse* §5, printed p. 29. **Kind:** unpursued implication / literature comparison. **Context search:** `Shiota`, `Hauptvermutung`, `triangul`, `isotop`; `RESULTS_STATE.md`, **MPL_150_001-043 Q4b** [first-pass lead]; nearest geometric system: `MPL_147_138-190_transcription.tex`, scans 177–178.

Fix an o-minimal expansion of an ordered field, compact polyhedra \(P,Q\) (finite unions of simplices), and finite families of compact subpolyhedra \(P_i,Q_i\). Inclusion \(\operatorname{Homeo}_{\rm PL}(P,P_i;Q,Q_i)\to\operatorname{Homeo}_{\rm def}(P,P_i;Q,Q_i)\) is the exact comparison: Shiota's theorem supplies a PL representative, and the Supplement supplies a definable isotopy from each given definable homeomorphism to such a representative [S2–S3]. This **adds** the checked theorem and its actual morphism to **MPL_150_001-043 Q4b**.

### Q4-03 — A broader result of Shiota also deserves a precise locator

**Source:** 120/015–020, “ind-structures”, “Espaces loc. modérés”; *Esquisse* §5, printed p. 29. **Kind:** unpursued implication / literature comparison. **Context search:** `loc.`, `homeom`, `triangul`, `Shiota`; `MPL_147_138-190_transcription.tex`, scans 181–182 and 190; `RESULTS_STATE.md`, **MPL_150_001-043 Q4b** [first-pass lead], **WG2 B15 (§1.2)** [unchecked plan].

For o-minimal structures \(S\subseteq S'\) over the same ordered field, the identity-on-sets-and-maps functor \(J:\mathrm{Def}_{S}\to\mathrm{Def}_{S'}\) preserves and reflects existence of homeomorphisms between \(S\)-definable objects, by Shiota's introductory Corollary (i); Theorem 4 treats noncompact finite definable families by standard semilinear models, unique up to semilinear homeomorphism [S3]. This **adds** a named comparison beyond the compact case to **MPL_150_001-043 Q4b**, while 147/181–182 supplies the contextual local-product vocabulary. The objects in 120/015–020 carry specified filtered or local structure, so the relevant next question is which of those objects and maps are represented by the finite families covered by the cited construction.

### Q4-04 — Grothendieck records the state of his own proof

**Source:** 120/025, “À prouver”; *Esquisse* §5, printed p. 30. **Kind:** self-flagged: unverified step. **Context search:** `à prouver`, `axiom`, `admet`, `comparaison`; `MPL_147_138-190_transcription.tex`, scan 178, “Admettant ce point”; `RESULTS_STATE.md`, **MPL_150_001-043 Q4b** [first-pass lead].

The *Esquisse* describes the axioms as provisional and explicitly records that he had not attempted their comparison proof [S1]. That statement **adds** an authorial status report alongside the unfinished heading in 120/025 and **restates the pattern of a reserved step** visible at 147/178. No proof of the complete comparison is recorded in the present 120 selection.

### Q4-05 — Generic triviality has a concrete semialgebraic realization

**Source:** 120/025, “fibré … trivial au sens modéré relatif”. **Kind:** unpursued implication / checked model. **Context search:** `trivial`, `fibré`, `fibration`, `voisinage`; `MPL_147_138-190_transcription.tex`, scans 177, 182 and 190; **BISITE D.5**, **RESIDUE G.5** [return claims: Proved; not fully reviewed].

In the compact semialgebraic model, Hardt trivialization gives \(h_i:U_i\times Z_i\to X|U_i\) with \(p h_i=\mathrm{pr}_1\); closure of its graph in \(\overline U_i\times Z_i\times X\) gives the manuscript's compact relation \(R_i\) without changing its graph over \(U_i\) (Appendix B; [S4]). This **adds** a verified model and explicit maps to the postponed fibrational construction at 147/190. It bears on the local-product maps of **BISITE D.5** and **RESIDUE G.5** by exhibiting the particular product charts, without changing their recorded status.

### Q4-06 — The inclusion-chain example is covered by marked-subset compatibility

**Source:** 120/025, “\(Z\subset X\subset Y\times[0,1]\)”. **Kind:** unpursued implication / checked model. **Context search:** `diagramme`, `produit`, `Z_j`, `X_i`; `MPL_147_138-190_transcription.tex`, scans 181–182; **STRATA C.5** [return claim: Proved], **WG2 B15 (§1.2)** [unchecked plan].

Apply definable Hardt triviality to the projection \(Y\times[0,1]\to Y\), marking both \(Z\) and \(X\): on each piece the same homeomorphism carries fixed nested fiber subsets to the two marked subsets [S4]. The resulting three restrictions commute with both inclusions, giving the exact simultaneous identification requested by this special diagram in the compact semialgebraic model (Appendix B). This **adds** a concrete realization of the product description at 147/181–182 and bears on **STRATA C.5** as a source of compatible geometric pieces.

### Q4-07 — A finite parallel-pair diagram obstructs the broad generic assertion

**Source:** 120/025, “Énoncé analogue pour un diagramme fini … ?” and “trivial par morceaux”. **Kind:** own idea / checked counterexample to the explicit broad reading. **Confidence:** high for simultaneous isomorphism of diagrams, because the intertwining equations force conjugacy and preserve order; no novelty claim. **Context search:** `diagramme`, `trivial`, `système`, `morphismes`; `MPL_147_138-190_transcription.tex`, scans 177–180 and 182; **STRATA C.5–C.6** [return claims: Proved], **WG2 B15 (§1.2)** [unchecked plan].

On \(Y=[-1,1]\), the finite diagram with two objects \(A=B=Y\times S^1\) and parallel arrows \(\mathrm{id},R_c\), where \(R_c(z)=(c+i\sqrt{1-c^2})z\), is a diagram of compact semialgebraic spaces and continuous semialgebraic maps. An isomorphism between its fibers at \(c,d\) consists of \(u,v\) with \(v=u\) and \(uR_c=R_du\), so rotation order is constant within each diagram-isomorphism class. Every nonempty parameter interval contains both finite-order and infinite-order rotations, which rules out simultaneous trivialization on every such interval and hence outside any rare compact exceptional set (Appendix A). This **adds** an explicit obstruction to the unspecified finite-diagram reading, against the contextual need to retain the actual gluing morphisms at 147/179 and **STRATA C.5–C.6**; the meaning of the manuscript's abbreviated “essentially” remains a reading/interpretation question.

### Q4-08 — Turning arrows into graphs requires a product compatibility check

**Source:** 120/006, “graphe”; 120/025, “diagramme fini”. **Kind:** own idea / checked diagnostic. **Confidence:** high, because the relevant commutative-square equation is written explicitly. **Context search:** `diagramme`, `morphismes`, `commutatif`; `MPL_147_138-190_transcription.tex`, scans 177–180; **STRATA C.1**, **STRATA C.5–C.6** [return claims: Proved].

For an arrow \(f:X\to Y\), a diagram isomorphism \((u,v)\) acts on its graph by \((x,f(x))\mapsto(u(x),v(f(x)))\), and the required equality is \(v f=f' u\). For an ambient map carrying one marked graph onto another, the relevant check is that its restriction to the graph equals \((u\times v)|_{\Gamma(f)}\), with \(u,v\) homeomorphisms of the full source and target; Appendix A exhibits the order invariant that this check retains. This **adds** an explicit compatibility test to the systems of maps at 147/179 and to the crossing-data claims **STRATA C.1, C.5–C.6**.

### Q4-09 — The final display contains an internal reading question

**Source:** 120/025, page-file lines 5–13. **Kind:** reading question. **Context search:** `Z`, `produit`, `fibre`; `MPL_147_138-190_transcription.tex`, scan 182; **MPL_150_001-043 Q4b** [first-pass lead] is the nearest comparison entry, with no register claim deciding this reading.

The frozen first display writes \((Z_i)_{i\in\pi_0(Y\setminus Y')}=(U_i)_{i\in I}\), whereas the following product uses \(U_i\) as the base part and \(Z_i\) as the fiber. The contextual product \(X_i\times Z\) at 147/182 **adds** a useful comparison of the two roles but does not decide the marks on this page. The first display must remain as transcribed; the interpretations in Q4-05–Q4-07 follow the subsequent relative-trivialization sentence explicitly.

### Q4-10 — The manuscript itself flags all three final questions

**Source:** 120/025, “À prouver”, “Énoncé analogue … ?”, “convenable … ???”. **Kind:** self-flagged: unverified steps. **Context search:** `Admettant`, `servira`, `trivial`; `MPL_147_138-190_transcription.tex`, scans 178 and 190; **MPL_150_001-043 Q4b** [first-pass lead], **BISITE D.12** and **RESIDUE G.3** [return claims: Open].

The first map-triviality assertion, the arbitrary finite-diagram extension, and the explicit nested-subset test all occur under or beside visible proof/question markers. These **add** three independently recorded targets to the admission at 147/178 and the promised later construction at 147/190. Their distinct exact maps are treated in Q4-05–Q4-08; the broad realization questions **BISITE D.12** and **RESIDUE G.3** retain their recorded open status.

### Q4-11 — Cote 121 supplies a local definition and labelled conjectures

**Source:** 120/025, “diagramme fini”; external primary 121/030–037 = official PDF pages 30–37 (footer numbers 29–36; handwritten pp. 31–38) [S6]. **Kind:** self-flagged / exact primary-source comparison. **Context search:** `équisingul`, `partition`, `diagramme`, `stratifi`; `MPL_147_138-190_transcription.tex`, scans 181–182; **WG2 B15 (§1.2)** [unchecked plan], **STRATA C.5–C.6** [return claims: Proved].

At 121/030 (footer 29) Grothendieck defines diagram equisingularity using local product maps that are open embeddings and identifies ordered indexing sets as the case to be used; at 121/035 (footer 34) the finite-poset/proper-map assertion is explicitly labelled Conjecture 2, with a visible revision to privileged partitions [S6]. This **adds** an actual local diagram condition and authorial status to 120/025 and the product vocabulary at 147/181–182. Appendix A now includes a finite-poset example for global simultaneous fiber-diagram trivialization; identifying that global condition with 121's local formulation would require an additional argument, which is not supplied by these pages.

### Q4-12 — Shiota proves a restricted finite-diagram comparison

**Source:** 120/025, “diagramme fini”; Shiota's 2010 preprint, Lemma 1.1 and following discussion, p. 2 [S2]. **Kind:** unpursued implication / checked literature comparison. **Context search:** `diagramme`, `morphismes`, `système`, `isotop`; `MPL_147_138-190_transcription.tex`, scans 177–180; **MPL_150_001-043 Q4b** [first-pass lead], **STRATA C.5–C.6** [return claims: Proved].

For finitely many PL maps of compact polyhedra over an ordered field \(R\supseteq\mathbb R\), Lemma 1.1 constructs compatible real PL models under the hypotheses that no source repeats and no directed cycle occurs, including finite marked unions of open simplices [S2]. Its comparison equation is \(\tau_i f_i=(g_i)_R\pi_i\), and the following discussion uses PL conjugacy classes to show the need for hypotheses. This **adds** an established positive diagram comparison to **MPL_150_001-043 Q4b** and the coherent-map context at 147/179; both examples in Appendix A repeat sources, so that particular hypothesis is visibly absent there.

### Appendix A — The compact finite-diagram calculation

This is a reader's fully specified calculation of one reading of 120/025. It concerns natural isomorphism of the actual diagrams over the base, including every arrow. The manuscript's abbreviated qualification “essentially” is left unresolved; no weaker equivalence relation is silently substituted.

Let \(\mathcal D\) be the finite category with two objects \(a,b\), identity arrows, and exactly two nonidentity arrows \(\alpha,\beta:a\to b\). There are no composites of two nonidentity arrows. Put

\[
Y=[-1,1],\qquad S^1=\{(x,y)\in\mathbb R^2:x^2+y^2=1\},
\qquad A=B=Y\times S^1.
\]

Both objects have their projection to \(Y\). Define a functor \(D:\mathcal D\to\mathrm{Top}/Y\) by

\[
D(\alpha)(c,z)=(c,z),\qquad
D(\beta)(c,(x,y))=
\bigl(c,cx-\sqrt{1-c^2}\,y,\sqrt{1-c^2}\,x+cy\bigr).
\]

The formula preserves the circle because the displayed matrix is orthogonal with determinant one. Its graph is semialgebraic: introduce the auxiliary coordinate \(s\geq0\) with \(s^2=1-c^2\), and use the two displayed polynomial coordinate equations; the nonnegative root is unique. The formula is continuous on the compact domain, hence its graph is compact. Thus the objects and arrow graphs belong to the standard compact semialgebraic model, with no limiting or noncompact object required.

At a parameter \(c\), the two arrows are \(\mathrm{id}_{S^1}\) and \(R_c\). A natural isomorphism \(D_c\to D_d\) has components \(u:S^1\to S^1\) at \(a\) and \(v:S^1\to S^1\) at \(b\). Naturality for \(\alpha\) is \(v\circ\mathrm{id}=\mathrm{id}\circ u\), so \(v=u\); naturality for \(\beta\) is then

\[
u\circ R_c=R_d\circ u,\qquad
u\circ R_c^n=R_d^n\circ u \quad(n\geq1).
\]

Consequently \(R_c^n=\mathrm{id}\) exactly when \(R_d^n=\mathrm{id}\), since \(u\) is a bijection. This argument uses only bijectivity, so allowing more bijections as components does not remove the obstruction.

Write \(c=\cos\theta\) for \(0<\theta<\pi\). Multiplication by \(c+i\sqrt{1-c^2}\) is multiplication by \(e^{i\theta}\), whose \(n\)-th power is one precisely for \(n\theta\in2\pi\mathbb Z\). Thus rational \(\theta/(2\pi)\) gives finite order and irrational \(\theta/(2\pi)\) gives infinite order. Every nonempty open interval in \((-1,1)\) corresponds under the continuous strictly monotone map \(\theta\mapsto\cos\theta\) to a nonempty angle interval, containing both sorts of angle. No nonempty interval therefore has mutually isomorphic fiber diagrams.

A rare compact subset \(Y'\subseteq[-1,1]\) is closed with empty interior. Its nonempty open complement contains an interval \(J\subset(-1,1)\), and a connected component containing \(J\) contains finite-order and infinite-order parameters. A trivialization of the diagram over that component identifies every pair of its fibers by composition of the two fiber identifications, contradicting the calculation. The same calculation rules out trivializations on an open cover of any nonempty parameter interval.

#### The same calculation for an ordered indexing set

There is also a height-two finite poset with elements \(a_1,a_2,b_1,b_2\) and relations \(a_i<b_j\) for all \(i,j\), with no other nonidentity arrows. Put a labelled copy of \(Y\times S^1\) at each object. Assign the canonical identity between copies to the three arrows \(a_1\to b_1\), \(a_1\to b_2\), \(a_2\to b_1\), and assign \(R_c\) to \(a_2\to b_2\). There are no compositions of two nonidentity arrows, so this assignment defines the diagram. Between two fibers, the three identity arrows force

\[
v_1=u_1,\qquad v_2=u_1,\qquad v_1=u_2;
\]

the fourth forces \(v_2R_c=R_du_2\). All four components are therefore one map \(u\), and the same conjugacy/order calculation applies. Adding the base as a terminal fifth object, with all arrows to it the projection, produces a finite-poset diagram whose arrows are proper: its spaces are compact Hausdorff, and its maps continuous. This explicitly records the finite-poset version of the global obstruction without asserting that 121's local equisingularity definition is equivalent to global simultaneous trivialization.

**An explicit isotopy of the second arrow.** Put \(q(c,t)=1-t+tc\), for \(c\in[-1,1]\), \(t\in[0,1]\), and set \(H_t(c,z)=(c,R_{q(c,t)}z)\). This is a continuous semialgebraic family of homeomorphisms over \(Y\), with \(H_0=\mathrm{id}\) and \(H_1=D(\beta)\); its inverse at each \(t\) uses the transpose rotation matrix. Thus the individual second arrow has an explicit isotopy to the identity, while a natural isomorphism of the two-arrow diagram satisfies the stricter, already computed conjugacy equation.

**Scope of the conclusion.** The obstruction applies to the explicit broad reading “every finite diagram is simultaneously constant up to isomorphism over the indicated base pieces.” The nested-subset example has simultaneous maps obtained as restrictions of one ambient trivialization in Appendix B. The displayed isotopy specifies another exact relation among the rotation maps; the present transcription does not say which such relation is intended by the abbreviated qualification “essentially.”

### Appendix B — Recovering the compact relation and the inclusion-chain model

Work in the compact semialgebraic model and let \(p:X\to Y\) be a continuous semialgebraic map. Hardt triviality, in the compatible-subset form proved in [S4, Theorem 5.22], supplies a finite partition of \(Y\) and base-preserving semialgebraic homeomorphisms on its parts. Refine the parts by a finite cell decomposition; the homeomorphisms restrict to every refined part. For each cell \(C\), remove \(\overline C^{\,Y}\setminus C\). The resulting exceptional set \(Y'\) is closed, semialgebraic, and nowhere dense: a locally closed cell is open in its closure, and a nonempty relatively open subset of \(Y\) contained in its closure must meet the cell, so each removed set is closed with empty relative interior. There are only finitely many cells. The surviving part of each cell is closed in \(Y\setminus Y'\), and its complement is a finite union of the other closed parts; hence it is also open. Every connected component \(U_i\) therefore lies in one original trivializing part.

Choose \(y_i\in U_i\) and identify the model fiber with the compact fiber \(Z_i=p^{-1}(y_i)\). This gives a homeomorphism

\[
h_i:U_i\times Z_i\xrightarrow{\sim}p^{-1}(U_i),
\qquad p\circ h_i=\mathrm{pr}_1.
\]

The closure

\[
R_i=\overline{\Gamma(h_i)}\ \subseteq\
(\overline U_i\times Z_i)\times X
\]

is compact and semialgebraic. The graph is closed over its domain \(U_i\times Z_i\), because \(h_i\) is continuous and \(X\) is Hausdorff, so restriction of \(R_i\) to this domain recovers exactly \(\Gamma(h_i)\). This supplies the relation in the frozen text while allowing multiple limiting values over \(\overline U_i\setminus U_i\), which the text does not require to be a graph.

For compact semialgebraic \(Z\subseteq X\subseteq Y\times[0,1]\), apply the same compatible-subset theorem to the projection of \(Y\times[0,1]\), with \(Z\) and \(X\) both marked. On a piece the resulting map \(h_i:U_i\times[0,1]\to U_i\times[0,1]\) carries \(U_i\times Z_i\) onto \(Z|U_i\) and \(U_i\times X_i\) onto \(X|U_i\), with \(Z_i\subseteq X_i\subseteq[0,1]\). Its restrictions give the two arrows of the inclusion-chain isomorphism and commute with the projection to \(U_i\); the preceding graph-closure construction supplies compact relations for them.

### Primary sources and verification scope

- **[S1]** Alexander Grothendieck, *Esquisse d'un programme*, §5, printed pp. 29–30; the copy inspected is [EsquisseFr.pdf](https://webusers.imj-prg.fr/~leila.schneps/grothendieckcircle/EsquisseFr.pdf), PDF pp. 25–26. Its comparison map, requested levels, and statement about the unattempted proof were read directly; no historical dating of cote 120 is inferred from this comparison.
- **[S2]** Masahiro Shiota, “O-minimal Hauptvermutung for polyhedra I,” *Inventiones mathematicae* **196** (2014), 163–232, [DOI 10.1007/s00222-013-0467-y](https://doi.org/10.1007/s00222-013-0467-y). Publisher abstract checked; author's [2010 preprint](https://arxiv.org/abs/1002.1508): Lemma 1.1, p. 2; Theorem 2.1 and Complement, pp. 5 and 17.
- **[S3]** Masahiro Shiota, *O-minimal Hauptvermutung for polyhedra II*, [arXiv:1310.5489v3](https://arxiv.org/abs/1310.5489v3), §2, p. 9 (restatement of I's uniqueness theorem and Supplement at I p. 227), Theorem 4, p. 13, and introductory Corollary (i), p. 6. The author explicitly supplies “through homeomorphisms” for the Supplement, explaining an omission in I's wording; this was checked in the full text. The PDF internally bears a later title-page date, so the bibliographic identifier here is its exact arXiv version.
- **[S4]** Michel Coste, *An Introduction to O-minimal Geometry*, November 1999 / Pisa 2000, §5.7, Theorem 5.22, pp. 61–63. The [author-hosted PDF](https://perso.univ-rennes1.fr/michel.coste/polyens/OMIN.pdf) timed out/returned 503; the same primary text, explicitly labelled author content, was read in the [author's uploaded full text](https://www.researchgate.net/publication/228392940_An_introduction_to_O-minimal_geometry). The theorem supplies finite base partitions and compatibility with finitely many marked subsets; the graph-closure and rotation calculations above are supplied here.
- **[S5]** Robert M. Hardt, “Semi-algebraic local-triviality in semi-algebraic mappings,” *American Journal of Mathematics* **102** (1980), 291–302, [DOI 10.2307/2374240](https://doi.org/10.2307/2374240). Journal table of contents and metadata checked; the original article's full text was not accessible. The exact theorem used in this draft was checked in [S4], whose text attributes the semialgebraic case to Hardt.
- **[S6]** Alexander Grothendieck, Montpellier cote 121, [official archive PDF](https://grothendieck.umontpellier.fr/121.pdf): scans/PDF pp. 30–37 (footer numbers 29–36; handwritten pp. 31–38), visually inspected; scans/PDF pp. 70–73 (footer numbers 69–72; handwritten pp. 71–74) were also checked for comparison/axiom context. Q4-11 uses only the former passage; no supplied transcription scan was reopened for this comparison.


## 6. Standing question I — Steps marked by the manuscript itself

These items record the author's proof markers, questions, and stated desiderata. Reader uncertainty in a `\unsure` macro is recorded in the doubts file and does not by itself give the author a mathematical doubt.

### U01 — The amalgamation question is followed by a scoped construction

**Source:** 120 scan 10, final paragraph; scans 11–14. **Kind:** self-flagged question, subsequently addressed for the displayed inclusions. **Quote:** “existe-t-il une somme amalgamée ?”.

The unrestricted span question is followed by a separation criterion and, on scan 13, a proposition explicitly displaying two inclusions under M5–M7, with the coordinate construction on scan 14. This later construction must be recorded beside the question; A120-06 checks why the scan-11 criterion cannot be applied unchanged to every span in the original wording. A120-09a supplies the reader's coordinate proof for the one-inclusion generalization suggested by the uncertain margin. The same-object search locates the amalgams in context/MPL_147_138-190_transcription.tex, scans 164 and 171, so these pages **add** an axiomatic construction to that context and bear on **STRATA C.1/C.3/C.6** [return claims].

### U02 — A remaining proof obligation is discharged in the same paragraph

**Source:** 120 scan 12, opening paragraph. **Kind:** self-flagged step, completed in the following lines. **Quote:** “Il nous reste à prouver”.

The stated obligation is moderation of the induced map, and the paragraph supplies it through the finite union of the images of the component graphs, as detailed in A120-05. Searches for graphs and amalgamation locate the contextual space-gluing diagrams at 147/164 and 171; this **adds** the graph argument rather than leaving the displayed obligation open. It bears on **STRATA C.1/C.3/C.6** with their return statuses.

### U03 — The continuity wish is made an explicit assumption

**Source:** 120 scan 17, topology paragraph; scan 18, continuation. **Kind:** self-flagged desideratum, made an axiom. **Quote:** “On voudrait que les applications modérées soient continues”.

The same paragraph introduces M9, compact moderate parts in a Hausdorff scalar space, and A120-12 gives the graph projection that proves continuity under that stated setup. The neighborhood search locates context 147/140–142 and 190; this **adds** explicit topological input to the earlier tubular programme, bearing on **WG2 B15 (§1.2)** [unchecked plan]. The wish is therefore recorded together with the assumption that the manuscript immediately uses to implement it.

### U04 — The neighborhood-basis wish becomes M10

**Source:** 120 scan 18, last paragraph. **Kind:** self-flagged desideratum, made an axiom. **Quote:** “On voudrait”; “c'est l'axiome”.

The paragraph asks for moderate neighborhoods and introduces M10 in the scalar space, with products and restriction supplying the model-space neighborhoods described in A120-14. Searches for voisinage and local triviality locate context 147/181–182; this **adds** a specified basis requirement to that context and bears on **WG2 B15 (§1.2)** without changing its unchecked status.

### U05 — Generic triviality is expressly left to prove

**Source:** 120 scan 25, heading and item 1. **Kind:** self-flagged: unverified step. **Quote:** “À prouver”.

The map-triviality assertion, including a rare exceptional part and a compact relation over each surviving component, occurs under this heading and has no subsequent proof in the supplied 120 pages. Q4-05 and Appendix B provide a checked semialgebraic realization with the exact relation; this **adds** a model to context 147/190's promised tubular fibrations. It bears on **BISITE D.5**, **RESIDUE G.5** [return claims] and **WG2 B15 (§1.2)** [unchecked plan], retaining each status.

### U06 — The extension to finite diagrams carries a question mark

**Source:** 120 scan 25, penultimate paragraph. **Kind:** self-flagged: unverified step. **Quote:** “Énoncé analogue pour un diagramme fini ... ?”.

The question preserves the diagram's arrows, so its literal simultaneous-isomorphism reading is tested by the complete rotation calculation in Q4-07 and Appendix A. Searches for diagramme and morphismes locate context 147/177–180; this **adds** an exact obstruction to that particular reading while the uncertain qualifier on the following line remains unresolved. It bears on **STRATA C.5–C.6** [return claims] as a compatibility issue, without identifying this global assertion with 121's separate local definition.

### U07 — The proposed nested-subset test remains visibly exploratory

**Source:** 120 scan 25, last paragraph. **Kind:** self-flagged: unverified step. **Quote:** “convenable ... ???”; “Ce serait déjà intéressant”.

The final paragraph singles out \(Z\subset X\subset Y\times[0,1]\); Q4-06 and Appendix B give the compatible marked-subset construction for this precise compact semialgebraic example. The product search locates context 147/181–182, so this **adds** a concrete proposed test to the earlier local-product language. **WG2 B15 (§1.2)** and **BISITE D.12** retain their recorded unchecked/open statuses.

### U08 — A doubtful marginal instruction is kept at its reading status

**Source:** 120 scan 9, upper margin. **Kind:** reading question. **Quote:** frozen as “le donner ... après ... ou postuler”, with doubt marks.

This appears to be an instruction about where to place or assume a proposition, but its uncertain words do not securely identify an additional authorially admitted theorem. Searches for postuler, proposition and admettre find the explicit admission at context 147/178 as the nearest methodological parallel; the present margin **adds** a reading question and bears on **WG2 §1.8 #5** [unchecked glossary plan]. The uncertainty remains in the frozen transcription and the doubts table.

### U09 — Cote 152's revisions are recorded without inventing proof markers

**Source:** 152 scans 3–5 and 7–13. **Kind:** reading question / withdrawn passages. **Quote:** “équivaut”; deleted “orientés”.

The second reading and the frozen-text search identify no explicit à-vérifier/sauf-erreur/je-présume formula in the surviving mathematical prose of this selection; the cancelled rotation paragraphs and the orientation revisions are documented in P09 and P15. The equivalence and recursion still have verification questions P02/P04/P10/P12, whose status comes from the written arguments rather than a newly attributed authorial warning. Searching the same proof-marker vocabulary locates the actual “Remords” and admission at context 147/178–180; 152 **adds** combinatorial constructions and revisions, bearing on **STRATA C.1/C.5** and **WG2 §1.8 #5** with their recorded qualifications.

## 7. Standing question II — Title sheets and visible numbering

### T01 — The institutional covers carry no manuscript total

**Source:** 152 scan 1; 120 scan 1. **Kind:** reading / bibliographical observation. **Quote:** “INSTITUT MONTPELLIERAIN ALEXANDER GROTHENDIECK”.

Both first scans are institutional covers with the IMAG design and carry no visible manuscript title or total-page statement. Searches for this cover wording in the supplied 147/149 selections yield no matching title sheet, so these covers **add** bibliographical framing to the package rather than a mathematical register result. The package has 13 supplied scans for 152 and 25 for 120, including these two covers.

### T02 — The plane-tree text has its own internal sequence

**Source:** 152 scan 5, heading; scans 7–8, 10–11 and 13. **Kind:** reading / bibliographical observation. **Quote:** “Arbres plans.”

The heading on scan 5 begins an internal sequence visibly numbered \(1,1',2,2',3,3'\) on scans 5, 7, 8, 10, 11 and 13 respectively, alongside the lower numbers carried by the surrounding sheets. The lower sequence in the supplied file runs from 1 at scan 2 to 12 at scan 13, with the doubtful readings at scans 9–10 retained in the doubts table; no separate total is written with this internal title. The same-title search finds no matching heading in the supplied 147/149 selections, so this **adds** a distinct internal text and its numbering, relevant to **WG2 §1.8 #5** only as an unchecked bibliographical/glossary lead.

### T03 — The tame-topology title is itself revised

**Source:** 120 scan 2. **Kind:** withdrawn wording / reading question. **Quote:** “Topologie modérée”; “(Autour de l'Eloge)”.

The frozen title retains a doubtful deleted “Structures” and an inserted “Topologie”, with the subtitle and visible lower 1; the upper annotation remains \(1/18\mid118\), without a secure interpretation as a date or total. Searches for the title and Eloge find no matching heading in the supplied 147/149 transcription selections, so this sheet **adds** the package's own revised title to the broader moderate-topology leads in **WG2 B15 (§1.2)**. No page-count claim is extracted from the doubtful upper annotation.

### T04 — Two visible numbering sequences coexist in cote 120

**Source:** 120 scans 2–25. **Kind:** reading / bibliographical observation. **Quote:** visible numbers 1–24 and 1–11.

The longer sequence runs 1–24 across scans 2–25, while the mathematical leaves at scans 3, 5, 7, 9, 11, 13, 15, 17, 19, 21 and 23 carry the additional sequence 1–11; the transcription preserves each occurrence rather than replacing them with PDF positions. Searches for page and folio numbering locate comparable coexisting author/scan locators at context 147/179 and 149/133, so this **adds** the exact concordance needed to cite the present package. No supplied register entry settles a mathematical issue through these numbers, and no written “24 pages” total is supplied by the sequence alone.

### T05 — Catalogue extent and observed extent agree after the covers are counted

**Source:** Montpellier catalogue, cotes 152 and 120; supplied scan manifest. **Kind:** reading / bibliographical comparison. **Quote from the supplied request:** “Catégorie des types de mots [dont arbres plans]”.

The catalogue lists 12 pages for cote 152 and 24 for cote 120; adding the institutional cover in each current PDF gives the observed 13 and 25 scans [R-S3]. The longer word-type description is the catalogue title supplied in the request, while the manuscript's internal plane-tree heading is recorded at T02. Context searches for the catalogue titles and page counts find no competing count in the supplied neighboring selections, so this **adds** the package concordance and changes no research-register status.

### T06 — The printed listing provides a dated sheet, with its own limits

**Source:** 152 scan 9, printed execution-date line; reused printed sheets at scans 6, 9 and 12. **Kind:** reading / chronology. **Quote:** “19 MAY 82”.

The printed date is transcribed as the date on that listing sheet; no autograph date is written on the supplied mathematical sheets that assigns the same day to their composition. The search for that date, PREDONTA and CSSBATCH yields no match in the supplied context, so the listing **adds** a physical dating datum and changes no mathematical result. This is also recorded as P17, with the technical abbreviations explained only in the doubts file.

## 8. Verification limits and unresolved tasks indexed to the supplied register

| Register or source question | Contribution of this package | Remaining task recorded here |
|---|---|---|
| WG2 §1.8 #5; INTAKE 20261114 §13.2 | Q1 records original-page definitions and explicit maps; P09–P11 record the rotation revisions and a checking dictionary. | Locate the exact site or universal property behind 149/133's named objects and its comparison morphism; resolve the marked glyphs from further ink evidence. |
| EXIT_ONE_TYPE P1d1; STRATA C.1/C.5/C.6 | R01–R03 add the author's sphere test and the explicitly typed modern truncation map. | The return claims keep their review status; the sphere test alone does not provide the general reconstruction proof left open in the continuation. |
| Chronology of the Remords continuation | R05 records the original folder date and the retrospective period reference. | Obtain an autograph or independently grounded date for the specific 151/041–044 leaves. |
| WG2 B15 (§1.2); BISITE D.12 | Q3 gives models, exact family/graph maps, compactification, parameter tests and local completion. | Identify the actual families and arrows in any proposed full comparison with the open-test realization; the supplied planning/open statuses remain. |
| CATHOT E.17; TOTASPH E.6 | A120-10/A120-13/A120-24 specify the directed and countable presentations and the weak-polytope construction. | The existence of the homotopy-invariant presentation in E.17 remains open as recorded; the explicit exhaustion does not settle that existence problem. |
| MPL_150_001-043 Q4b; STRATA C.5–C.6 | Q4 gives the actual isomorphism-family comparison, checked Shiota statements, compatible marked-subset charts and the rotation computation. | Verify the requested higher-parametric comparison at its full stated scope and identify the abbreviated “essentially” in 120/025; no such interpretation was inserted into the frozen transcription. |
| FLAGGED_149 ZD8; EXIT_ONE_TYPE P4e; RESIDUE H.4 | P12–P16 supply disk-dual and labelled-tree maps; R08 retains the meridian arrows. | Establish any comparison with the exact normal-crossings or moduli objects in those returns through their specified maps; the finite examples do not promote those statuses. |

The complete 38-page transcription, every doubt marker and all 734 inventory rows remain the image-based record. The research records preserve source limits and computations so that further work can address the remaining questions without silently replacing that record.
