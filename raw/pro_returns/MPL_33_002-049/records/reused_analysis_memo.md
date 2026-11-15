# Research support memo: reused typescripts in cote 33, scans 002–049

## Scope and limits

This is research-note support produced **after the transcription was frozen**. I read only the frozen LaTeX fragments and the supplied context; I did not inspect scan images, transcribe, change readings, or modify the transcription, doubts, inventory, or progress log. The examples below test the literal transcribed mathematics and do not establish authorship of the reused sheets or historical novelty.

Context was searched separately for each proposed item across all three supplied files: `README.md`, `notes/RESULTS_STATE.md`, and `same_cote_33/MPL_33_098-146_notes.md`. Exact queries and all hits are in `records/reused_context_search.json`; elementary calculations are retained in `records/reused_scope_checks.json`. None of the context files contains the root-system, product-of-stalks, or filtered-module assertions tested below. The later same-cote notes are explicitly first-pass, unreviewed leads.

**Important correction to a tempting criticism:** scan 033's one global rescaling is not automatically false under scan 035's global vertex-weight definition. Whenever that global weight function exists, it records the relative lengths of disconnected components too. The real scope question is whether scan 035 intends irreducible systems or a normalization: arbitrary independently scaled reducible components need not have the stated three possible global lengths.

## Proposed items (each substantive paragraph is at most four sentences)

### R01. The type-A endpoint formula has an exceptional rank-one test

**Primary:** cote 33, scan 013, heading and (IV). **Kind:** own idea. **Search:** `R01_A1_endpoint`.

The heading includes “$(\ell\geq1)$,” while (IV) states “$(\widetilde\alpha|\alpha_1)=(\widetilde\alpha|\alpha_\ell)=1$.” At $\ell=1$, the same sheet gives $\widetilde\alpha=\alpha_1=\varepsilon_1-\varepsilon_2$ and $\|\alpha_1\|^2=2$, so the displayed endpoint value is 2 in that case. This is an internal exceptional-rank check, not grounds for altering the frozen text or attributing an error to the entire unseen source.

**Confidence:** high for this substitution; the author's intended exception is unresolved.

**Context comparison:** no hits for the same objects in the three context files, and no same-point result in `notes/RESULTS_STATE.md`. **Adds** an independent source-level collation question to the collection in `same_cote_33/MPL_33_098-146_notes.md`, N46 (scans 105, 109, 111, 131, 135, 139, 143); N46 is a methodological parallel, not an earlier instance of this root-system assertion. The relevant register-level scope entry is **MPL_33_098-146 §1**, an unreviewed research lead; no result status changes.

### R02. The L3 generator remains a reading question

**Primary:** cote 33, scan 017, item 4), LaTeX line 12. **Kind:** reading question. **Search:** `R02_L3_generator`.

The generator in “$L_3=L_1+\mathrm Z.(\frac12\sum \unsure{\xi_i|\varepsilon_i})$” has an explicitly unresolved letter, whereas nearby $\xi_i$ are coordinates and $\varepsilon_i$ are basis vectors. Reading the first alternative literally would make the displayed generator a sum of coordinates rather than a vector in the stated basis, so this is a useful collation priority; the mathematical expectation does not settle the ink. Keep the uncertainty exactly as frozen.

**Context comparison:** the only search hits are generic lattice references in **WG H9** and **WG2 §2.1 #2**, plus the unrelated epsilon in `same_cote_33/MPL_33_098-146_notes.md`, N54 (scan 145). The present question **differs** from all of these and **adds** a root-lattice reading issue; there is no matching context scan. WG H9 and WG2 are unchecked planning items, and N54 is an unreviewed research lead; none settles this reading.

### R03. The E6 exponent product is internally inconsistent as printed

**Primary:** cote 33, scan 023, final two displays. **Kind:** own idea. **Search:** `R03_E6_exponent_product`.

The equation with the factor “$(12+1)$” forces the left-hand side to be divisible by 13 for integral $m,m'$, while its right-hand side $51{,}840$ has remainder 9 modulo 13. Equivalently, the other displayed factors force $(m+1)(m'+1)=540/13$, which is not an integer. The preceding list includes exponent 11, providing an internal collation lead, but the transcription must retain its literal 12.

**Confidence:** high for the arithmetic contradiction; no claim about which source stage introduced it.

**Context comparison:** no same-object hits or earlier matching scan. This **adds** an independent arithmetic anomaly beside `same_cote_33/MPL_33_098-146_notes.md`, N46 (the scans listed under R01), without restating any of its examples. No substantive register theorem bears on it; **MPL_33_098-146 §1** supplies the unreviewed reused-source accounting context.

### R04. An ordered root pair tests the asserted norm ratios

**Primary:** cote 33, scan 035, first complete paragraph. **Kind:** own idea. **Search:** `R04_ordered_root_pair`.

The assertion that $n(u,v)=-1$ gives “$\|v\|/\|u\|=1$” and reflection-product order 3 needs an ordering or equivalent extra hypothesis. In the explicit reduced root system $\{\pm e_1,\pm e_2,\pm e_1\pm e_2\}$, choose simple roots $u=e_1-e_2$ and $v=e_2$: then $n(u,v)=-1$ but $\|v\|/\|u\|=1/\sqrt2$, and $s_us_v$ is a quarter-turn of order 4. This is a counterexample to the isolated ordered-pair wording, with missing earlier conventions still to be checked.

**Confidence:** high; the dot products and two reflection matrices are explicit.

**Context comparison:** no same-object hit in the supplied context. The page **adds** a scope test of a separate reused source, of the same methodological kind as `same_cote_33/MPL_33_098-146_notes.md`, N50–N51 (scan 135) and N54 (scan 145), but mathematically **differs** from those local-algebra tests. **MPL_33_098-146 N54** is listed in the results register only as an unreviewed lead, not as a result that settles this root assertion.

### R05. Global length labels and reducible components

**Primary:** cote 33, scans 035 (global label definition) and 033 (Proposition 2 proof). **Kind:** own idea. **Search:** `R05_reducible_scope`.

The global minimum “$\lambda$” in the definition on 035 makes a hypothesis on relative component scales significant: the reduced system $\{\pm e_1,\pm2e_2\}$ has lengths 1 and 2, which do not fit the stated alternatives $\lambda,\lambda\sqrt2,\lambda\sqrt3$. Recover an irreducibility or normalization convention before extending this definition to arbitrary reduced systems. However, once the stated global weight function exists, it records relative component scales, so the single-factor rescaling on 033 is not by itself a counterexample.

**Confidence:** high for the example and this logical distinction; medium for the proposed historical explanation because earlier conventions are unavailable.

**Context comparison:** hits for “lattice” lead only to **WG H9** (cote 44, Theorems 4–5, no exact scan supplied) and the symplectic-lattice part of **WG2 §2.1 #2** (ambiguous listed cotes/scans). This **differs** from those unchecked planning topics and **adds** a source-specific root-system scope question; neither planning row receives a status change. The same-cote note's disposition table also distinguishes generic lattice vocabulary from a demonstrated mathematical connection.

### R06. The E8 dimension label conflicts with its own surrounding coordinates

**Primary:** cote 33, scan 049, (IV) and (VI). **Kind:** reading question. **Search:** `R06_E8_dimension`.

Part (IV) explicitly works in “$\mathrm R^8$,” whereas (VI) writes “$V=\mathrm R^4$” while using the same eight-coordinate root and weight data. This discrepancy is a source-level collation question; it is not resolved by silently substituting the expected dimension. The frozen reading is unchanged.

**Context comparison:** no same-point context entry or scan; this **adds** another independent source anomaly to the comparison programme of `README.md` (S19). The closest source-accounting register entry is **MPL_33_098-146 §1** (unreviewed lead), and the methodological comparison is N46 in `same_cote_33/MPL_33_098-146_notes.md` rather than a matching E8 calculation.

### R07. The highest-root pairing can be checked from these sheets alone

**Primary:** cote 33, scan 049 (IV), scan 037 ($\omega_7$, $\omega_8$), scan 019 (orthonormal basis convention). **Kind:** own idea. **Search:** `R07_E8_pairing`.

Scan 037's two weight displays give $\alpha_8=2\omega_8-\omega_7=\varepsilon_7-\varepsilon_6$, while $\widetilde\alpha=\omega_8=\varepsilon_7+\varepsilon_8$. With the orthonormal basis convention on 019, their pairing is $+1$, conflicting with the literal “$(\widetilde\alpha|\alpha_8)=-1$” on 049. This arithmetic uses only the supplied frozen formulas, and records an internal inconsistency rather than importing a published root table.

**Confidence:** high; the alpha coefficients cancel to the eighth basis vector, and the epsilon dot product is immediate.

**Context comparison:** no matching highest-root/weight item or scan appears in the supplied context. This **adds** an internal check beside N46's independent reused-source anomalies (`same_cote_33/MPL_33_098-146_notes.md`, scans 105, 109, 111, 131, 135, 139, 143); it does not contradict an earlier established result. **MPL_33_098-146 §1** remains an unreviewed source-accounting lead.

### R08. The product-of-stalks Hom assertion has an explicit scope test

**Primary:** cote 33, scan 043, ii), with definition on 041, b). **Kind:** own idea. **Search:** `R08_PX_Hom`.

The phrase “It is easily checked that these maps are inverses” fails for general topological spaces in the literal $P_X$ construction: take $X=\{a,b\}$ with opens $\varnothing,\{b\},X$ and the constant $k$-valued sheaf with identity restriction. Then $P_XF(X)=k^2$, $P_XF(\{b\})=k$, restriction is the second projection, and the maps $\varphi_X(s,t)=(t,0)$ and $\varphi_{\{b\}}=0$ form a sheaf morphism that is not pointwise diagonal. The proposed extraction recovers point maps $(\mathrm{id},0)$ and reconstructs $(s,t)\mapsto(s,0)$, so it does not recover $\varphi$. This tests the general-space wording; unseen earlier restrictions on $X$ must be recovered before a judgment about the complete source.

**Confidence:** high for the finite-space counterexample; no historical novelty claimed.

**Context comparison:** no $P_X$, reflector, or product-of-stalks match. The three “stalk” hits are `same_cote_33/MPL_33_098-146_notes.md`, N18 (scan 120, ordinary direct-image support) and N31 (scans 138, 140, uniform Tor bounds), which **differ** from this Hom assertion; the present example **adds** a separate categorical scope test. No same-point register result settles it; **MPL_33_098-146 N54** is an unreviewed methodological parallel involving a different literal criterion.

### R09. The reflector construction depends on absent categorical conventions

**Primary:** cote 33, scans 045, Theorem 1.4, and 039, proof. **Kind:** unproved claim. **Search:** `R09_reflector`.

The hypothesis “complete … and have enough small objects” and the assertion that the reflector is exact for a “right perfect” coefficient category depend on Chapter I definitions not reproduced on these leaves. The intersection construction on 039 begins the proof, but its continuation and the exact conventions are needed before comparing this with a modern sheafification theorem for an arbitrary coefficient category. This is a dependency question, distinct from the concrete $P_X$ Hom counterexample.

**Context comparison:** the only related search hit is the corrected injective argument in `same_cote_33/MPL_33_098-146_notes.md`, N06 (scan 106), which concerns derived adjunction and **differs** from the reflector theorem. These pages **add** a separate foundational source; **MPL_33_098-146 §1** (unreviewed lead) is the relevant source-accounting entry, with no substantive matching result in `notes/RESULTS_STATE.md`.

### R10. The cancelled sheet explicitly leaves arbitrary n without separation open

**Primary:** cote 33, scan 047, opening paragraph before 19.6. **Kind:** self-flagged: a step the source itself marks as unverified. **Search:** `R10_separation_question`.

The cancelled typescript says “Nous ignorons s'il en est encore ainsi (sans hypothèse de séparation) pour $n$ quelconque,” referring to b)$\Rightarrow$c), and separately states that c)$\Rightarrow$b) fails even for $n=1$. The precise conditions b) and c) are absent from this leaf, so the question must be indexed with that limitation rather than reconstructed from a later textbook. Whole-sheet cancellation does not establish that the author later solved or withdrew the mathematical question.

**Context comparison:** no separation/filtration/regular-sequence match in any supplied context file. This **adds** a different explicit uncertainty to the inventory in `same_cote_33/MPL_33_098-146_notes.md`, §VI (e.g. S14/N55, scan 145, another reused source's missing proof), rather than restating one of its questions. It bears on **MPL_33_098-146 §65** as the standing-question inventory (unreviewed lead), not on an open LM4/LM7 result.

### R11. A small example separates the two filtrations on R

**Primary:** cote 33, scan 047, (19.6.1), the paragraph introducing $R''_k$. **Kind:** own idea. **Search:** `R11_induced_modified_filtrations`.

The statement “les filtrations $(R''_k)$ et $(R'_k)$ sont en général distinctes” has a simple test: set $A=k[t]$, $J=(t)$, $N=A$, $R=tA$, $N_0=A$ and $N_k=0$ for $k\geq1$. Then $N'_1=tA$, so $R'_1=R\cap N'_1=tA$, whereas $R''_1=R_1+JR_0=t^2A$. This illustrates why modification of a filtration and passage to a submodule cannot simply be interchanged.

**Confidence:** high; direct substitution in the two definitions gives a strict inclusion.

**Context comparison:** no same-object hit or matching scan. This **adds** a concrete example to the source-qualification programme beside N50–N51 (scan 135) in `same_cote_33/MPL_33_098-146_notes.md`, but **differs** from their completeness/coefficient-field examples. No substantive result entry bears on this filtration calculation; **MPL_33_098-146 §1** is only the unreviewed reused-source context.

### R12. The restriction projection has a literal domain question

**Primary:** cote 33, scan 041, b). **Kind:** reading question. **Search:** `R12_projection_index`.

The defining equation uses the projection $\widetilde p_{xV}$ but says “where for $x\in U$,” although that projection is supplied by the product over $x\in V$. This is an indexing/domain question separate from the stronger Hom assertion on 043; a point of $U\setminus V$ already prevents the displayed component from being one of the stated projections. The frozen text is left unchanged.

**Context comparison:** the “stalk” matches N18 (scan 120) and N31 (scans 138, 140) in `same_cote_33/MPL_33_098-146_notes.md` concern other constructions and **differ**. The present leaf **adds** an elementary source-indexing issue; no same-point register entry or matching context scan was found.

### R13. Reused-source provenance must remain separate

**Primary:** cote 33, scans 005–049 odd, especially 009, 011–037, 039/041/043/045 and 047. **Kind:** reading question. **Search:** `R13_reuse_provenance`.

The typed root-system pages, “Variétés de groupe” editorial sheet, English sheaf-theory pages, and cancelled filtered-module sheet are distinct source strands; printed page order supplies useful internal continuations but does not establish a single author. Their explicit questions and gaps should be recorded, while keeping them separate from the handwritten étale-cohomology programme. No source identity is inferred here from familiarity with the mathematics.

**Context comparison:** this **restates** the provenance caution in `same_cote_33/MPL_33_098-146_notes.md`, scope §1 and N42/N56 (scans 099, 101–121, 125–143), and **adds** new observed strands. It also adds pagination evidence beside T07/T08 (scans 099, 101–145 odd), without identifying the two packages' reused sources as the same works. **MPL_33_098-146 §1** is expressly an unreviewed lead; no historical attribution is upgraded.

## Additional standing-question reminders

- Scan 019 explicitly says “Il restera naturellement à vérifier dans chaque cas que le système R est réduit et irréductible”; the type A verification on 013 discharges one case in the original typed order, not all cases.
- Scan 009 asks whether to define hyperalgebras generally and proposes the formal-kernel “sorites”; this is an editorial uncertainty of a reused source.
- Scan 021's “On verra … ci-dessous” concerning the two Dynkin types for a Coxeter diagram is deferred exposition, not automatically a new conjecture.
- In scan 023, “qu'il reste à calculer” is immediately followed by the quotient calculation in the same paragraph; do not leave that particular calculation classified as still open.
- Scan 047's change “quotient” to “filtré” is a title revision on the cancelled sheet, not itself a proof that the underlying mathematics was retracted.

## Register disposition for this memo

The root-system and elementary sheaf/filtration examples do not advance **LM7 E.23**, **LM4 D.12**, **LM4 F.7**, or **LM7_PUSH C.6**. Finite Weyl groups are not evidence about profinite GT torsion or geometric A5 centralizers; “lattice” is not enough to identify these pages with **WG H9**, and “graded” is not enough to identify (19.6.1) with **WG2 §2.1 #2**. Those statuses remain exactly as supplied. No result already recorded as settled has been re-derived in this memo.
