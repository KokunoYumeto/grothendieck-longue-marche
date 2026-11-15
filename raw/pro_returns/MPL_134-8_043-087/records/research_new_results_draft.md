# Research comparison draft: NEW_RESULTS and the 26 open register entries

## Scope and source discipline

This is a text comparison against the 44 frozen page transcriptions for scans 043–087, with scan 060 absent from the supplied sequence. The primary reader's freeze time was 2026-11-15 11:49:57 UTC; the frozen combined transcription SHA-256 is `3f85b51570feeb779ae2fd3d9e338ea8f90078fbce6e6e406722a402d6bc8c79`. This comparison used the frozen text, the supplied README, the full RESULTS_STATE register, the full NEW_RESULTS list, and targeted `rg` searches and reads within the supplied context; it did not use scan images.

“No located form” below means that the statement or construction was not located in this bounded transcription corpus. It makes no assertion about other Grothendieck manuscripts or about the existence of a mathematical relation. Where a page supplies a comparison, the actual displayed functor, morphism, or quantifier is recorded; no additional theorem is inferred from shared terminology.

NEW_RESULTS describes its own search as limited and disclaims priority. RESULTS_STATE explicitly treats return statuses as run claims unless an intake verdict is given; the review descriptions below are likewise reports of the supplied records, not a new verification of the mathematical proofs. Referenced OWN_RESULTS, FINDINGS, return CSVs and review files generally are not included under their stated paths; their contents are therefore not reconstructed here. The coverage JSON preserves every source row verbatim, including the register's own ellipses.

Current-page citations use the image scan number; a following manuscript-page number is the `\mspage` token in the frozen transcription. Context citations use the supplied file and the manuscript page or claim ID identified there. All twelve numbered NEW_RESULTS entries and its three closing “Known after all” entries are covered below, followed by all 26 open RESULTS_STATE entries.

## A. Every NEW_RESULTS entry

### NEW_RESULTS 1 — Finite monoids: finite type, finite dimension and bounded homology coincide.

**Source/status:** `context/NEW_RESULTS.md`, row 1; checked by: **“not yet (Pro check prompt drafted)”**. Proof reported at `pro_reviews_max_20261112/1_CATHOT/OWN_RESULTS.md`, §2; antecedent CATHOT G.4 and the medium-review Atiyah route are credited separately in the source. **Register bearing:** CATHOT G.17, still Open as a return claim.

No located form of the finite-monoid equivalences, the conclusion about `U(M)`, or the bounded-homology corollaries occurs in scans 043–087. The closest finite-presentation wording is scan 077, ms. 76: `X$ plat de prés. finie i.e. $X$ proj. de t. f.`, attached to the explicitly displayed functor `\kappa^*(\xi)=X\otimes\xi` in the example `\mathcal M=\mathrm{Ab}_k`; this page supplies no `BM` or universal-group construction. The indicated earlier manuscript target is Chapter V ms. 51–52, located in `context/companion/chunks/DER_III-V.tex` at the definition of `\Hot_0` by finite categories and the restricted Yoneda map `X\mapsto(\xi\mapsto\Hom_{\Hot}(\xi,X))`.

### NEW_RESULTS 2 — Miller's Theorem B under a cohomological bound.

**Source/status:** `context/NEW_RESULTS.md`, row 2; checked by: **“not yet”**. Proof reported at `OWN_RESULTS` §1. **Register bearing:** CATHOT G.17 through the finite-monoid realization question; no standalone Miller entry is present in RESULTS_STATE.

No located form of the stated `BG\to X` theorem, its fundamental-group conclusion, or its p-local variant occurs in the present scans. NEW_RESULTS identifies it as a tool for row 1 and gives no independent Grothendieck manuscript page; the corresponding context anchor is therefore row 1's Chapter V ms. 51–52 discussion in `DER_III-V.tex`. Current scans 066–071 contain coefficient-comparison calculations, but no finite-group map, cohomological dimension bound, or Miller reference was located there.

### NEW_RESULTS 3 — A Kan–Thurston theorem without small quotients, and E.17.

**Source/status:** `context/NEW_RESULTS.md`, row 3. The source reports GALOIS B.11–B.12 followed in full by a medium review and read by the max expert; **OWN_RESULTS §3 is “not yet” checked**, and the cardinality bound was quoted from memory. Proofs reported at `OWN_RESULTS` §3 and GALOIS B.10–B.12. **Register bearing:** CATHOT E.17; related dossier rows PATHS D.K1–D.K5.

No located form of the `BG\to W` construction, small-quotient factorization, or groupoid presentation of invariant ind-objects occurs in scans 043–087. Scan 056, ms. 55, does display `i_Aj_a^o(C)\longrightarrow C^{\Delta^1}`, and scan 059, ms. 58, displays `i^*(C)\times i^*(\Delta^1)\arrow[r]&i^*(C)`; these are the available interval comparison maps, with no accompanying small filtered ind-system assertion. The source's manuscript targets are V ms. 44–46 (`DER_III-V.tex`), VII ms. 129–132 (`DER_VII-c.tex`), and IX ms. 22–23 (`DER_VIII-X.tex`). RESULTS_STATE still marks the sequential CATHOT E.17 entry Open; the differently scoped checked branch and unchecked branch recorded in NEW_RESULTS are retained as source reports without changing that status.

### NEW_RESULTS 4 — Uncountably many maps to S².

**Source/status:** `context/NEW_RESULTS.md`, row 4; checked by: **“not yet”**. Proof reported at `OWN_RESULTS` §4. **Register bearing:** CATHOT D.6, Open as a return claim.

No located form of the sphere-retract criterion, the hypotheses involving `H¹(X; Z)` and `π_n(S³)`, or an uncountability conclusion occurs in the present scans. The source points to CATHOT D.6 and Chapter V ms. 43–46, whose ind-representability discussion is present in `context/companion/chunks/DER_III-V.tex`; its hunch H3 is named in NEW_RESULTS but its text is not supplied here. The register's finite-category two-sphere test therefore receives an explicit bounded no-occurrence mapping, without a new status verdict.

### NEW_RESULTS 5 — Posets of type RP² need at least 34 arrows

**Source/status:** `context/NEW_RESULTS.md`, row 5; checked by: **“not yet”**; source parenthesis: “the return proved 28”. Proof reported at `OWN_RESULTS` §5, bearing on CATHOT G.8. **Register bearing:** CATHOT G.17, Open as a return claim.

No located form of an `RP²` poset, its arrow count, or the lower bound 34 occurs in scans 043–087. The available exact context is NEW_RESULTS row 5 and RESULTS_STATE's CATHOT G.17 row, which retains the interval `[28,49]` and the unresolved exact minimum; the supplied material gives no manuscript page for CATHOT G.8. The later unchecked lower-bound claim is recorded alongside that older register bound, without recomputing either or silently replacing the register's status.

### NEW_RESULTS 6 — Census of small categories.

**Source/status:** `context/NEW_RESULTS.md`, row 6; checked by: **“not yet”**. Proof reported at `OWN_RESULTS` §6 and `1_CATHOT/work/code/`; the source separately credits CATHOT G.14–G.15 and the medium enumeration. **Register bearing:** CATHOT G.17, Open as a return claim.

No located form of the claimed minima `4, 5, 7`, the uniqueness assertions, or the monoid `P₂` occurs in the present scans. The concrete earlier model cited by the source is available in `context/companion/chunks/DER_XIIapp.tex`, ms. 10–11: four named objects and “les seules (six) flèches non identiques de `Z`,” followed by the editorial sphere annotation. Scan 045's `\operatorname{Add}(\Delta_1)` and its complexes describe an explicit additive construction, but no census or arrow-minimization assertion accompanies it.

### NEW_RESULTS 7 — A reversible fundamental localizer not detected by spectra.

**Source/status:** `context/NEW_RESULTS.md`, row 7; checked by: **“not yet (prompt REVERSIBLE_LOCALIZERS drafted)”**. Proof reported at `pro_reviews_max_20261112/DERIVATEURS_EXPERT/RESULT_REVERSIBLE_NOT_STABLE.md`. **Register bearing:** POLES F.14 and RESIDUE I.7, both Open as return claims; RESIDUE D.9 concerns the related homology-classification scope.

No located form of `W_S`, the two-local sphere tests, the two projective-space maps, or stable closure occurs in scans 043–087. A precise coefficient comparison is present in scan 068, ms. 67: `$W_k$-asph\qquad $W_k$-coasph.`, together with `LH_\bullet(A,f^*F)\xrightarrow{\simeq}LH_\bullet(B,F)`; scan 049 also proposes the displayed localization functor to `\mathrm D_\bullet(Ab_k)`. The indicated earlier locations are Chapter XII §5 (`DER_XIIb-a.tex`) and Chapter XVI §3 (`DER_XVI.tex`, including the companion block “Integral homology supplies a reversible localizer”); their status claims do not supply the missing `W_S` construction in this packet.

### NEW_RESULTS 8 — XII Théorème 2 (ms. 78) is false for W∞

**Source/status:** `context/NEW_RESULTS.md`, row 8. The source reports **TOTASPH A.13 checked**, its 37-object category recomputed, and agreement between the Pro return and max expert; proof location reported as `DERIVATEURS_EXPERT/FINDINGS.md`, F-G1, with earlier companion entries. **Register bearing:** TOTASPH F.27 and RESIDUE F.6 remain Open; POLES B.2 and POLES G.5 carry their own Proved/Refuted return claims.

No located form of the two-cone construction `X=A⋆{t,s}`, the strong W(7 bis) biconditional, or its counterexample occurs in scans 043–087. The exact earlier target is printed in `context/companion/chunks/DER_XIIb-a.tex`, ms. 78, as Théorème 2, followed by companion block `dgrb517`, “A finite counterexample to the asserted reverse excision”; the source also points to XIIbb-A045 and later uses at ms. 85, 105 and the appendix. Scan 081, ms. 80, instead supplies the concrete interval augmentation `J\longrightarrow1_M` and defines its tensor stability by `(on dit que c'est dans $UW_M$)`, with no cover square or W(7) formula located on that page. NEW_RESULTS' further sentence about all strong-W(7 bis) uses is preserved as that source's claim, without expanding it into a classification theorem.

### NEW_RESULTS 9 — A direct proof that W_Z and W_k fail Loc (7 F)

**Source/status:** `context/NEW_RESULTS.md`, row 9; checked by: **“not yet”**. Proof reported at `FINDINGS` F3-5; parenthetical construction: “trefoil complement over a base of type S¹”. **Register bearing:** GALOIS B.14 and RESIDUE D.9, both Open as return claims.

No located form of Loc (7 F), the trefoil construction, or a fibration-existence counterexample occurs in the present scans. Scan 068, ms. 67, gives the directly relevant coefficient notation without resolving its first occurrence: `$f$ $\unsure{W_h|W_k}$-asph`, and tests it through the displayed arrow from `A_{/b}` to `B_{/b}` and the displayed derived-homology comparison. The exact earlier question is in `context/companion/chunks/DER_XVI.tex`, ms. 105, where the text asks about Loc (7 F) and ends “Je ne hasarderais aucune conjecture à ce sujet !”.

### NEW_RESULTS 10 — For Y simply connected, Ch(Y; y₀, −) total ⇒ Y total.

**Source/status:** `context/NEW_RESULTS.md`, row 10; checked by: **“not yet”**. Proof reported at `FINDINGS` F2-11. **Register bearing:** the totality questions TOTASPH D.7, RESIDUE F.5 and RESIDUE F.6; these entries do not state this path-category assertion verbatim.

No located form of the specified path-category projection or totality transfer occurs in scans 043–087. The exact context map is `X = \uCh(Y; y_0, -) \xrightarrow{\ f\ } Y.` in `context/companion/chunks/DER_XIIb-a.tex`, ms. 102–103, with the direct-image discussion at ms. 112–113; the current text's explicit chain-complex notation is `\mathrm{Ch}_\bullet(Ab_k)` on scan 056, and its interval comparison is `i_Aj_a^o(C)\longrightarrow C^{\Delta^1}` on the same page. No morphism identifying that chain-complex object or interval comparison with the specified `\uCh(Y;y_0,-)` projection is written in this packet, so the shared `Ch` lettering is not used as evidence of the full result.

### NEW_RESULTS 11 — Grothendieck's conjecture of II ms. 36ter ("totally W∞-aspherical ⇒ filtered") is false

**Source/status:** `context/NEW_RESULTS.md`, row 11. The source reports medium and max checks, including recomputation and a reading of Isbell–Mitchell; proof reported at TOTASPH C.5–C.10 and its review. **Register bearing:** TOTASPH C.10 (Refuted, return claim), PRETOT A.12 (Proved with the stated zero-wrong run review), TOTASPH D.7, RESIDUE F.5, TOTEX D.20, IMPL P1 and IMPL P3.

No located form of `Δ_inj`, the filteredness conjecture, or the exact-abelian-colimit bridge occurs in scans 043–087. Scan 058, ms. 57, does say `i.e. $J$ est tot asph.`, immediately after tensor-acyclicity tests on `J\otimes_{\unsure{k}}x`; the upper part also writes the explicit kernel `\unsure{\widetilde W_h^P(I)}\otimes F=\operatorname{Ker}(F^{(I)}\longrightarrow F)`. The context formulation quantified over direct images is in `DER_II-a.tex`, ms. 36–36ter, claim II-C-003 and companion blocks `dgrb105` and `dgrb108`, with `P(y)=\pi_0(y\backslash A)` and `A\to Y/P\to Y` displayed. The current tensor tests do not include that arbitrary-target factorization or a filteredness conclusion, and the register's remaining exactness questions are left at their reported statuses.

### NEW_RESULTS 12 — Counterexample to Conjecture 7.1 of arXiv:2610.38760v1

**Source/status:** `context/NEW_RESULTS.md`, row 12. The source reports medium verification, completion of the fundamental-group calculation and a second Atiyah proof, and a max recheck from published texts. Proof reported at CATHOT G.4, G.6, `1_CATHOT/G6_VERDICT.md` and `EMAIL_CLAIMS_CHECK.md`. **Register bearing:** CATHOT G.17, Open as a return claim.

No located form of the `RP²` finite-monoid obstruction, the universal-group calculation, or the cited contemporary conjecture occurs in scans 043–087. NEW_RESULTS is the available context source for the exact counterexample and review history, and gives the date of sending it rather than a Grothendieck manuscript page. The nearest manuscript target supplied elsewhere in the same list is row 1's Chapter V ms. 51–52 finite-category discussion in `DER_III-V.tex`; the present packet adds no `BM` construction to that comparison.

### Closing entry K1 — Isbell–Mitchell 1973, Theorem 3 (aff Δ filtered; item 11)

**Source/status:** `context/NEW_RESULTS.md`, closing “Known after all” list, first entry. **Register bearing:** TOTASPH C.10 and PRETOT A.12, with the review qualifications recorded under row 11.

No located form of the named affine-category result occurs in the present scans. Its supplied context is the closing entry and `DER_II-a.tex`, companion block `dgrb108` after ms. 36ter, where the claimed exactness of colimits over the increasing-injection category and the affine-arrow criterion are discussed. This records the bibliography as the context's attribution; no new primary-source literature audit is claimed.

### Closing entry K2 — uniqueness in Nielsen realization (Harvey 1971; found again by the La Longue Marche expert)

**Source/status:** `context/NEW_RESULTS.md`, closing “Known after all” list, second entry. **Register bearing:** no exact Nielsen-uniqueness row is present; IMPL P3 is the register's Teichmüller-tower planning entry.

No located form of Nielsen realization, its uniqueness assertion, or a surface action occurs in scans 043–087. The exact available source is the closing NEW_RESULTS entry; DOSSIER's PATHS D.11 mentions a Nielsen monodromy for another comparison, but supplies no identity with this uniqueness assertion. No underlying La Longue Marche page is specified for this closing entry in the supplied context.

### Closing entry K3 — "localiseur spécial" = accessible fundamental localizer follows from Cisinski, Astérisque 308, Cor. 4.2.22.

**Source/status:** `context/NEW_RESULTS.md`, closing “Known after all” list, third entry. **Register bearing:** GALOIS B.13, POLES F.14 and RESIDUE I.7, each retaining its Open return status.

No located form of the phrase “localiseur spécial,” the claimed characterization, or its accessibility hypothesis occurs in the present scans. Current scan 049's displayed localization `W_{\mathcal M}^{-1}\mathcal M\longrightarrow\mathrm D_\bullet(Ab_k)` supplies a concrete coefficient construction but no small-set generation statement. The closing entry provides the exact citation; the related accessible-localizer realization discussion is available in `DER_VIII-X.tex` at Chapter X ms. 3–5, without a supplied identification of this result with a current-page formula.

## B. All 26 open RESULTS_STATE entries mapped to the frozen pages

The source of every ID in this section is `context/notes/RESULTS_STATE.md`, “Open items,” in its original order. Unless otherwise specified, the exact status is **“Open (the return's claim)”**; IMPL P1 and IMPL P3 instead carry **“candidate prompt item: open”**. Companion claim labels and statuses are recorded as context claims, not freshly refereed results.

### 1. TOTASPH F.27 — dwyérienne sieves, discrete flatness and composition

Scans 058 (ms. 57), 081 (ms. 80) and 086 (ms. 85) supply the nearest explicit tests: `i.e. $J$ est tot asph.`, tensor stability of `J\longrightarrow1_M` designated `UW_M`, and `1_M\longleftarrow J\quad\text{\unsure{univ\textsuperscript{t}} str. acycl.}` respectively. No sieve-composition or one-point couniversal-recognition assertion is located in the corpus. The specified earlier source is XII ms. 111–114 in `DER_XIIb-a.tex`; `LesDerivateurs_companion.tex` records XIIba-C035, XIIba-C037 and XIIba-C045, and NEW_RESULTS 8 supplies the reviewed-counterexample report relevant to the strong excision premise.

### 2. CATHOT E.17 — sequential local presentations of invariant ind-objects

No located form of the sequential formula `H_K(X)=\colim_n\Hom_{\Cathot}(X,K_n)` or its local presentation occurs in scans 043–087. The exact earlier discussion is V ms. 44–46 in `DER_III-V.tex`; the current interval map `i_Aj_a^o(C)\longrightarrow C^{\Delta^1}` on scan 056 supplies only the recorded interval comparison. NEW_RESULTS 3 reports the reviewed GALOIS branch and the unchecked OWN_RESULTS branch, while this register row remains Open.

### 3. GALOIS B.13 — accessibility from Der 1–4

Scan 049 proposes a specific localization functor to `\mathrm D_\bullet(Ab_k)`, and scan 077 explicitly studies `\kappa^*:\xi\longmapsto1_M\otimes_k\xi`; no assertion about generation of `\Wlc` by a small set, literal Loc (9), or all Der 1–4 derivators is located in this corpus. The source register points to GALOIS Part B, and `DER_VIII-X.tex`, Chapter X ms. 3–5, is the supplied coefficient/localizer comparison location. Closing NEW_RESULTS K3 records an accessible-localizer characterization without resolving this row's bare-axiom question.

### 4. GALOIS G.6 — functorial higher coefficients on bare derivators

Scans 066–071 give the actual coefficient functor `u_a` with `x\mathbin{\text{---}}\operatorname{Hom}(a,x)` and derived-cohomology comparisons, including `u_a(RH^\bullet(A,F))\simeq RH^\bullet(A,u_a\circ F)` on scan 066. No functorial assignment `\D\mapsto\D'` with the registered localizer equality or an iteratable 2-derivator construction is located in the present scans. The specified context is Chapter X ms. 1–5 in `DER_VIII-X.tex`, together with the register's GALOIS E.11 and RESIDUE I.7 rows.

### 5. RESIDUE F.5 — total asphericity and exact connected colimits

Scan 051, ms. 50, writes `\lambda_!=\Lambda\quad\text{est exact (et commute aux }\underset{\longrightarrow}{\lim}\text{)}`, and scan 058 gives the tensor-acyclicity expression cited above. No exactness conclusion for `\colim_A:\Ab^A\to\Ab` from totality of a nonempty connected shape without a weak terminal object, or equalization in `\operatorname{Aff}_{\mathbb Z}(A)`, is located in the corpus. The supplied comparison is `DER_II-a.tex` at ms. 36–36ter and block `dgrb108`; the same open direction is registered as TOTASPH D.7, while NEW_RESULTS 11 records the checked counterexample to filteredness.

### 6. RESIDUE F.6 — total presheaves and composition of dwyérienne sieves

Scan 058 explicitly passes through `\operatorname{Ker}(F^{(I)}\longrightarrow F)`, and scan 072, ms. 71, writes `\widehat A/X\simeq\widehat{(A_{/X})}`. No comparison of all direct images of a presheaf for `W_{\mathbb Z}` and `W_\infty`, or composition statement for dwyérienne sieves, is located in these scans. The exact context is the RESIDUE F.6 row, its fuller DOSSIER row, and XII ms. 111–114 in `DER_XIIb-a.tex`, linked by the source to TOTASPH F.27.

### 7. POLES F.14 — reversible-localizer classification and Bousfield representability

Scan 068 has `$W_k$-asph\qquad $W_k$-coasph.` and its displayed homology restriction map, but no `RT` fixed-point assertion, spectrum construction, or representability claim is located in the packet. The context source specifies POLES Part F, with the relevant reversible-excision discussion in `DER_XVI.tex`, §3. NEW_RESULTS 7 remains an unchecked claim directed at part (1) of this open entry, and RESIDUE I.7 retains the classification question.

### 8. RESIDUE A.8 — strict adjoint transports over the specified monoids

No located form of the monoid action search, a contractible total category over the specified `M`, or a strict bifibration with right-adjoint transports occurs in scans 043–087. The source's exact manuscript anchor is VI ms. 186, `DER_VI-c.tex`, and claim VIc-C022 in `LesDerivateurs_companion.tex`; its named companion register target is BISITE B.21. Current scan 075 explicitly labels its own map as `appl. de catégories \unsure{$k$-additives|$k$-biadditives} augm.`, and supplies no multiplication table or transport functors for those monoid examples.

### 9. RESIDUE F.7 — universal ordinary Cat-colimit comparisons

No located form of the universal Grothendieck-total-category to ordinary Cat-colimit comparison, or its implication toward filteredness for the specified countable shapes, occurs in the present scans. Scan 051's explicit colimit statement concerns `\lambda_!` and its exactness, while scan 067 displays `LH_0(A,\int F)\mathbin{\text{---}}LH_\bullet(B,F)` without the registered universal Cat-colimit assertion. The context anchors are the RESIDUE F.7 row and the DOSSIER's PATHS A.2 and A.5 comparisons; no manuscript page is specified for F.7 itself.

### 10. RESIDUE I.7 — reversible classification and a second derivator

Scan 047 explicitly writes the coefficient functor `L\varphi=\Phi:\mathcal M\longrightarrow\mathrm D_\bullet(Ab)` alongside its Hot comparison, and scan 075 lists the restriction condition `W_N=f^{*-1}(W_M)`. No reversible-localizer classification across the specified interval, or assignment on all Der 1–4 derivators natural in exact morphisms, is located in these pages. The available context is the full DOSSIER RESIDUE I.7 row, the open POLES F.14 and GALOIS E.11/G.6 rows, and NEW_RESULTS 7's unchecked claim.

### 11. TOTASPH D.7 — exactness of abelian colimits from totality

Scan 058's exact phrase `i.e. $J$ est tot asph.` follows tensor-acyclicity tests, and scan 051 asserts exactness of the displayed `\lambda_!` functor. No form of this register's quantified assertion about `\colim_A:\Ab^A\to\Ab` is located in scans 043–087. The context points to Lead 4, the same direction in RESIDUE F.5, and `DER_II-a.tex` block `dgrb108` after ms. 36ter; NEW_RESULTS 11 is retained with its recorded reviews and does not close this row.

### 12. BISITE B.21 — strict bifibration over the five-element rectangular-band monoid

No located form of `R=\{1,e_{00},e_{01},e_{10},e_{11}\}`, its multiplication, or the requested path-local-system representative occurs in the present scans. Its context is the open register row, the related RESIDUE A.8 row, and the manuscript bifibration question at VI ms. 186 in `DER_VI-c.tex` / VIc-C022. No current-page morphism is supplied that realizes the specified monoid-base construction.

### 13. BISITE F.18 — strict higher indexing of an abstract derivator

No located form of a strict `n`-categorical extension, Street-nerve equivalence class, lax/colax comma object, or the registered universal lifting condition occurs in scans 043–087. The supplied context names the strict-`nCat` indexing question in the register and the exact DOSSIER BISITE F.18 row and its BISITE C.5–C.10 higher-slice/fine-comparison references. No source manuscript page is specified for this open entry, and no additional page identification is inferred.

### 14. CATHOT D.6 — the sequential two-sphere test

No located form of `[BC,S^2]`, countability for every finite category, or the equivalent sequential representation problem occurs in these scans. The register's exact scope is Part D(ii), S², and NEW_RESULTS 4 points back to V ms. 43–46 in `DER_III-V.tex` while recording an unchecked uncountability criterion. The present comparison neither supplies a finite-category example meeting that criterion nor changes the Open status.

### 15. CATHOT E.26 — cofinal-type and all-type geometric comparisons

The current interval calculations are explicit on scans 059, 081, 084 and 086; scan 081 describes `J'\longrightarrow J^{\unsure{\deleted{'}}}` compatible with augmentations and `\inserted{bi-}co-augmentations`. No projective sequence of types, cofinality comparison, or all-type localization assertion is located in the present packet. The specified source pages are VII ms. 108–123 across `DER_VII-b.tex` and `DER_VII-c.tex`; DOSSIER row PATHS C.P3 claims all three comparisons while RESULTS_STATE still marks CATHOT E.26 Open, so both source statuses are retained.

### 16. CATHOT G.17 — finite realization and size questions

No located form of `a_{\mathrm{pos}}(\mathbb{RP}^2)`, the interval `[28,49]`, or an intrinsic classification of finite-category/finite-monoid homotopy types occurs in scans 043–087. The exact context is the register's Part G(i)–(ii) entry and NEW_RESULTS 1, 5, 6 and 12, whose review statuses differ. The earlier finite-category and sphere-model pages cited by those rows are V ms. 51–52 (`DER_III-V.tex`) and XII appendix ms. 8–11 (`DER_XIIapp.tex`); no present-page arrow-count model is located.

### 17. GALOIS B.14 — bare-derivator fibration and factorization questions

Scan 068 begins with `A\arrow[r,"f"]&B` and records its slice test with the displayed arrow from `A_{/b}` to `B_{/b}`, then `LH_\bullet(A,f^*F)\xrightarrow{\simeq}LH_\bullet(B,F)`. No strict-pullback preservation theorem for Grothendieck fibrations with the registered transports, or requested factorization for arbitrary Der 1–4 derivators, occurs in the present scans. The source points to Part B's Loc 7a/7F scope; the context's explicit later question is XVI ms. 105 in `DER_XVI.tex`, and NEW_RESULTS 9 gives an unchecked specialized counterexample claim.

### 18. GALOIS E.11 — bare-derivator functoriality and higher linear coefficients

Scans 049 and 053–055 record the actual adjoint pair `\lambda_!,\lambda^*` between the specified abelian category and chain complexes, and scan 066 records the coefficient functor `x\mathbin{\text{---}}\operatorname{Hom}(a,x)`. No arbitrary-derivator assignment with `W_{\D'}=W_\D^{\mathrm{lc}}` is located in the packet. The context sources are the register's Lead 4/Part E entry, its GALOIS G.6 and RESIDUE I.7 companions, and Chapter X ms. 1–5 in `DER_VIII-X.tex`.

### 19. GALOIS F.8 — reconstruction from ordinary fibre functors

Scan 047 gives explicit adjunction Hom formulas for `\varphi` and `\kappa`, and scan 066 uses `u_a` with `x\mathbin{\text{---}}\operatorname{Hom}(a,x)` to compare derived coefficients. No reconstruction from the specified ordinary `\LC_{\D_R}(X)` and its ordinary fibre functors, with the register's restrictions on enhancement data, is located in scans 043–087. The exact supplied context is the GALOIS Part F excerpt in RESULTS_STATE; no underlying manuscript page for this residual reconstruction question is specified there.

### 20. IMPL P1 — compact/profinite inverse limits and total/exact shapes

**Status: candidate prompt item: open.** Scan 067, ms. 66, writes `v(R\Gamma_{\unsure{\mathrm{Ab}_k}}(B,F))\overset{?}{\simeq}R\Gamma(B,v\circ F)` followed by `\bigl(\simeq LH_\bullet(A^o,(v\circ F)^o)\bigr)`, and scan 069 writes `\mathbb Q_p/\mathbb Z_p` and `x\longrightarrow\operatorname{Hom}(x,I)`. These are the precise current-page duality leads, retaining the question mark and uncertain notation; no general compact/profinite `\lim^1` criterion, common-successor classification, or full exactness equivalence is located here. The source points to IMPL I1 and T A.13–A.20, and RESULTS_STATE's IMPL I1 entry records the intake's duality implication rather than a manuscript page for P1.

### 21. IMPL P3 — the Teichmüller tower as a total/exact index shape

**Status: candidate prompt item: open.** No located form of the Teichmüller tower, its Galois part, LM3's type/gluing index category, or the two-level finality assertion occurs in scans 043–087. The available exact source is the P3 excerpt in RESULTS_STATE, referring to IMPL I1 and LM3 without supplying a manuscript page; closing NEW_RESULTS K2 mentions a Nielsen-realization result but gives no morphism identifying it with this tower question.

### 22. PATHS D.22 — residual intrinsic recognition and finite/cardinal tests

Scan 056 records `i_Aj_a^o(C)\longrightarrow C^{\Delta^1}`, and scan 059 supplies `i^*(C)\times i^*(\Delta^1)\arrow[r]&i^*(C)`, the available current interval comparisons. No finite/cardinal-only recognition theorem, BK finite-shape sufficiency claim, intrinsic cofibration construction without an initial object, or nonaccessible-localizer derivator construction is located in this packet. The specified earlier target is IX-080 in `LesDerivateurs_companion.tex`, located at IX ms. 22 in `DER_VIII-X.tex`, with the broader residual list retained verbatim in the JSON.

### 23. RESIDUE D.9 — homology classification with arbitrary spectra and monodromy

Scans 066–071 explicitly compare coefficients through `u_a` and `f^*`; scan 068 gives `$W_k$-asph\qquad $W_k$-coasph.` and scan 066 lists projective-flat/injective-coflat conditions. No classification for arbitrary spectra, coverings and all `W_\infty`-smooth/proper functors, or monodromy calculation of the registered kind, is located in these scans. The context source is RESIDUE D.9 with D.8/D.12 as its partial-result references, and NEW_RESULTS 7 and 9 supply separately unchecked localizer claims; the register supplies no exact manuscript page for D.9 itself.

### 24. TOTEX D.20 — discrete reflection for total-shape presheaves

Scan 058 supplies a universally quantified tensor-acyclicity discussion ending `i.e. $J$ est tot asph.`, and scan 072 writes `\widehat A/X\simeq\widehat{(A_{/X})}`. No `G_F` arising from a total shape, discrete reflection, or sign-orbit presentation is located in scans 043–087. The exact supplied source is the TOTEX D.20 register row; NEW_RESULTS 11 and the reviewed PRETOT/TOTEX intake summaries are contextual leads, with no source manuscript page stated for this residual integral question.

### 25. BISITE C.10 — strict higher fine recognition and base change

No located form of the specified Street-nerve maps from enhanced strict higher localizations, or the covariant/contravariant base-change assertion, occurs in scans 043–087. The exact supplied context is the register's “Recent-results family 317; Parts C and E,” with the DOSSIER BISITE C.5–C.10 rows identifying its higher-slice/model-structure setting. The present `f^*` calculations on scans 068 and 075 supply the displayed ordinary/additive coefficient maps but no Street-nerve comparison.

### 26. BISITE D.12 — unrestricted topological realization over Y and its proposed dual

No located form of `C_Y`, localization of all topological spaces over a locally compact Hausdorff base, or the specified `\operatorname{Shv}(Y;\mathcal S)` presentation occurs in scans 043–087. Its supplied source is the RESULTS_STATE “Lead 2 unrestricted Top/Y assertion” excerpt; no underlying manuscript page is specified. The packet therefore receives an explicit bounded no-occurrence row for the whole registered question.

## Coverage and limits

Coverage is **12/12 numbered NEW_RESULTS entries, 3/3 closing known-attribution entries, and 26/26 open RESULTS_STATE entries**. Every current-page quotation above comes from the frozen text and retains its code tokens, deletions and uncertainties; the accompanying JSON supplies the exact source row, status, query, match locations and page list for each entry. No open row was solved, rederived or reclassified in preparing this comparison.
