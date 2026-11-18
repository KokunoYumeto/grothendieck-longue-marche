# MPL 159 — Research notes after the frozen transcription

## Scope, evidence, and the planning questions

These notes concern cote 159, the 32 supplied scans numbered 1–13, 15–23, and
25–34. The root agent personally read and transcribed the images in one
sequential stream, completed a second image audit of all 32 pages, checked
recurring notation, and froze the 32 page fragments plus their exact combined
transcription at **2026-11-18 01:04:49 UTC**. The context was first opened at
**01:04:50 UTC**; no contextual or mathematical conclusion below changes a
frozen `.tex` file.

The source references below name the **scan number**, not the archive pencil
foliation. `L` numbers are physical lines in the named frozen page `.tex`
file, not claims about original manuscript line breaks. Brief quotations
omit intervening material where shown by an ellipsis; macro-bearing quotations
retain the editorial uncertainty or cancellation. All full readings, including
their doubt alternatives, remain in the transcription and doubts register.

| Planning question | Finding | Notes |
|---|---|---|
| Does the folder concern uniformization by projective connections? | Yes: it treats projective structures, transverse sections, uniformizing representations, and monodromy. | N001, N026–N049 |
| Does it write the specific Schwarzian equation needed for comparison? | No complete scalar normalization has been identified; the coordinate calculation has a sign conflict. | N002, N042–N043 |
| In which characteristic? | Mixed scope: general initial definitions and a question, explicit exclusions of characteristic two, a complex analytic section, and characteristic-zero formal theorems. | N003, N014, N049–N058 |
| Does it compute p-curvature? | No explicit p-curvature/Frobenius/Cartier calculation was located; characteristic-p counterexamples below are our comparisons, not manuscript content. | N004, N050, N058, N070 |
| Does he cite cotes 93 or 64? | No such citation was located in the supplied pages, subject to the recorded legibility limits. | N005 |
| Is the proposed 159–93–64 cluster established? | There is a substantive projective-connection/Gauss–Manin comparison to attempt, but no completed identification, and the actual 93/64 source pages are absent here. | N002, N005, N024, N070 |

The table is an index to the individually checked notes, not an additional
set of unlogged claims. The strongest changes to the supplied interpretation
concern the **object of the canonical-torsor question**, **flat bundles versus
opers**, **the injectivity assertion actually followed by an argument**, and
**the hypotheses and stabilizers in formal normalization**.

### Context and attribution

The authorized context files were read after the freeze, including the whole
`context/notes/RESULTS_STATE.md` and `context/hua_project/159.modern.tex`.
**Hua, modernised reading of cote 159** means the AI-produced interpretation
credited to Michel Hua’s project in `context/hua_project/README.md`; it is
neither our transcription nor our result. Its page n is generally our scan
n+1; the cover and blank omissions explain the different counts.

Each note has an actual `rg` query recorded as `[Qnnn]` in
`context_searches.tsv`, with query, matching files/lines, retained match locations,
and the comparison cited in the note. Subsection names identify the location
inside Hua’s file. RESULTS_STATE entries are connected by their supplied IDs;
their statuses are reports of earlier runs, not independent proof certificates.
The source files behind the truncated MPL_93 entries and the tower-result
register were not supplied, so no claim of reading or rechecking them is made.

The main event ledger uses the requested check categories and separates
documentary comparisons, targeted proof checks, independent proofs, exact
computations, and unproved background. Merely transcribing a statement was
not counted as a mathematical check. Delegated agents worked only after the
freeze on the mathematical checks in `research_checks/`; all image reading
and transcription decisions remained with the root agent. The model was
GPT-6 Astra Pro; a distinct numerical effort setting was not exposed, and
the event ledger records that fact instead of inventing one.


## A. What the dossier does and does not establish


### N001 — The uniformization part of the planning guess is supported

**Kind:** unpursued implication · **Source:** 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L3-5; 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L12-26; 159.pdf scan 023, `pages/MPL_159_159_scan023.tex` L2-6 · **Quote:** `Connexions projectives canoniques et uniformisation des courbes algébriques`

The dossier develops pointed projective bundles, projective connections, monodromy, and the uniformizing representations of compact complex curves, so the uniformization part of the planning guess is supported by substantial content, not only by its title. It also develops a separate formal normalization problem on scans 25–34; the Hodge-theoretic pages do not visibly complete the proposed bridge between those two parts.

**Context comparison:** Adds direct manuscript evidence to context/README.md, “The guess” (S20), and agrees with Hua, modernised reading of cote 159, hua_project/159.modern.tex, §§“Les stations” and “Ce qui ne s’articule pas”, while retaining the unfinished bridge as unfinished. [Q001]


### N002 — Projective structures and scalar differential equations

**Kind:** own idea · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L26-35; 159.pdf scan 020, `pages/MPL_159_159_scan020.tex` L3-19; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L3-15 · **Quote:** `connexions projectives`

Confidence: high for the modern comparison, low for any exact identification of the manuscript’s scalar normalization, because no complete Schwarzian equation is written here and scan 20 has incompatible signs. Beilinson–Drinfeld, Opers, §§2.6–2.7, identify a projective structure with a transverse section of a flat projective-line bundle and with a normalized second-order operator whose solution ratio gives projective coordinates [L1]; this supplies a precise comparison to attempt, not a missing manuscript formula.

**Context comparison:** Bears on RESULTS_STATE.md entry MPL_93_002-046 P01 (“Identifying the normalization of the Schwarzian”) and P09; differs from treating the title-level comparison in context/README.md as an already identified equation, and supplements Hua, hua_project/159.modern.tex, §“Le calcul en coordonnées, et la formule encadrée”. [Q002]


### N003 — There is no single characteristic assumption for all the pages

**Kind:** reading question · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L3-7; 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L10-14; 159.pdf scan 015, `pages/MPL_159_159_scan015.tex` L13-18; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L13-15; 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L23; 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L2-9; 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L40-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L7-9 · **Quote:** `sans condit. de dim ni de car. ?`

The opening question is deliberately unrestricted, scan 13 marks characteristic different from two, the moduli calculation is placed in characteristic zero, the automorphism argument uses invertibility of two, and the formal normalization propositions explicitly use characteristic zero. The density proposition still carries “de car nulle ?”, so neither an all-characteristic theorem nor a uniform blanket hypothesis should be read into the whole dossier.

**Context comparison:** Refines context/README.md, “The guess”, and Hua, hua_project/159.modern.tex, §§“Conventions, valables pour tout le dossier”, “Le théorème de rigidité”, and “La densité de Zariski, et où la situer”, by listing the actual locations and the surviving authorial question. [Q003]


### N004 — No p-curvature calculation has been located

**Kind:** reading question · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L7-36; 159.pdf scan 011, `pages/MPL_159_159_scan011.tex` L3-14; 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L10-26; 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L21-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L7-9 · **Quote:** `stratification`

No explicit p-curvature, Frobenius, or Cartier calculation was read on these 32 supplied pages; that is a bounded negative finding, subject to the marked illegible words and uncertain readings. The changes from connection to stratification and the denominators in the formal recurrence provide reasons for a future characteristic-p comparison, but do not themselves constitute one.

**Context comparison:** Does not confirm the p-curvature part of context/README.md, “The guess” (S20), and respects the evidentiary limit in RESULTS_STATE.md, MPL_93_002-046 P09; Hua, hua_project/159.modern.tex, §“Ce qui ne s’articule pas”, likewise does not supply a manuscript p-curvature computation. [Q004]


### N005 — Cotes 93 and 64 are a proposed comparison, not a manuscript cross-reference

**Kind:** reading question · **Source:** 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L3-5; 159.pdf scan 011, `pages/MPL_159_159_scan011.tex` L3-14; 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L10-26; 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L16-26 · **Quote:** `connexion`

No explicit citation to cote 93 or cote 64 was located in the supplied leaves, and the actual pages of those cotes are not part of this context attachment. The available RESULTS_STATE.md gives only labels or truncated summaries for P01, P09, and C35, so their underlying arguments and the normalization in cote 93 cannot be checked from those summaries.

**Context comparison:** Limits the proposed cluster in context/README.md, “The guess”, and RESULTS_STATE.md, “What other packages’ research notes say about these cotes”, entries MPL_93_002-046 P01, P09, and C35; the precise comparison remains to be made from the sources rather than inferred from their titles. [Q005]


### N006 — The suggested tower and icosahedral links do not receive a solution here

**Kind:** reading question · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L3-24; 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L18-24; 159.pdf scan 023, `pages/MPL_159_159_scan023.tex` L2-6 · **Quote:** `Zariski-dense`

The monodromy here concerns unbranched projective structures on smooth projective curves of genus at least two; it neither gives Schwarz’s finite-monodromy list nor compares the absolute Galois group with GT or GT0. Its characteristic-zero density conclusion actually excludes finite projective monodromy in that setting, so a passage to punctured, branched, or orbifold curves would be needed before applying the suggested finite-group comparison.

**Context comparison:** Does not settle the conditional leads in RESULTS_STATE.md, “Orientation for this package”, namely FERMAT_SUCCESSOR C.20, LM4 F.7, or LM1 D.7; those remain the prior runs’ open claims, not results of this transcription. [Q006]


## B. Pointed projective bundles and stratifications


### N007 — The extension dictionary fixes the object being recovered

**Kind:** unpursued implication · **Source:** 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L7-23; 159.pdf scan 003, `pages/MPL_159_159_scan003.tex` L3-7; 159.pdf scan 008, `pages/MPL_159_159_scan008.tex` L3-24 · **Quote:** `équivalence de catégories`

A pointed Brauer–Severi bundle is encoded by an extension 0→Ω→E→O→0, with the quotient line normalized to O; a first-order projective identification then identifies Ω with Ω¹ of the base curve or variety. This distinction between the pointed bundle and the additional connection is essential when interpreting the subsequent word “canonique”.

**Context comparison:** Restates the dictionary in Hua, modernised reading of cote 159, hua_project/159.modern.tex, §“Trois descriptions d’un même objet”, and adds its role in limiting the question on scan 9. [Q007]


### N008 — Automorphisms of a nonsplit extension have an obstruction

**Kind:** own idea · **Source:** 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L13-23; 159.pdf scan 019, `pages/MPL_159_159_scan019.tex` L13-15 · **Quote:** `\lambda c=c`

Confidence: high, because an automorphism of Ω extends to the extension precisely when it preserves its class in Ext¹(O,Ω); the kernel of the resulting map on extension automorphisms is Hom(O,Ω). Thus a full semidirect-product description by Aut(Ω) and Γ(Ω) is valid in the split model but need not describe the global automorphism group of an arbitrary extension.

**Context comparison:** Qualifies Hua, hua_project/159.modern.tex, §“Trois descriptions d’un même objet”, using the manuscript’s own class-preservation argument in §“Les automorphismes du couple (P,σ)” (our scan 19); this is a context correction, not a transcription change. [Q008]


### N009 — The fractional action controls the later coefficients

**Kind:** unpursued implication · **Source:** 159.pdf scan 004, `pages/MPL_159_159_scan004.tex` L33-47; 159.pdf scan 005, `pages/MPL_159_159_scan005.tex` L3-24 · **Quote:** `\frac{\omega}{1+a}`

The action on the formal coordinate is fractional linear, and its homogeneous degree-n part is multiplied by (1+a)^(-n). Expanding only through degree n+1 yields the coefficient −n used on scan 7, so later missing-looking integers should be checked against this earlier explicit action rather than normalized silently.

**Context comparison:** Restates Hua, hua_project/159.modern.tex, §§“Le complété formel le long de la section, et l’action de Ω” and “La conséquence graduée”, and supplies a cross-check relevant to the distinct associated-graded issue on scans 28 and 33. [Q009]


### N010 — The tautological line has a different action from the algebra

**Kind:** unpursued implication · **Source:** 159.pdf scan 005, `pages/MPL_159_159_scan005.tex` L26-48; 159.pdf scan 006, `pages/MPL_159_159_scan006.tex` L20-55 · **Quote:** `u_{a*}^{\widehat L}(g)=(a+1)u_{a*}(g)`

The extra factor 1+a is forced by compatibility with the quotient E⊗Ŝ→L̂, so the weight on a homogeneous degree-n element of L̂ is 1−n. Keeping this action separate from the algebra action prevents losing the twist when comparing jet extensions or constructing a second-order operator.

**Context comparison:** Restates Hua, hua_project/159.modern.tex, §“Le complété formel le long de la section, et l’action de Ω”, and adds a concrete normalization constraint for RESULTS_STATE.md entry MPL_93_002-046 P01, whose source formula is not supplied. [Q010]


### N011 — Successive jet extensions remember a multiple of the torsor

**Kind:** unpursued implication · **Source:** 159.pdf scan 007, `pages/MPL_159_159_scan007.tex` L10-36 · **Quote:** `-nv_n`

The extension Jⁿ/Jⁿ⁺² is the pushout of the Ω-torsor along −n times multiplication, with its sign tied to the stated action convention. In positive characteristic the scalar n can vanish, so one such graded extension can lose information even though the whole formal action remains nontrivial.

**Context comparison:** Restates Hua, hua_project/159.modern.tex, §“La conséquence graduée”, and adds an elementary characteristic-p warning relevant to the unrestricted question in §“Les deux données, et l’identification qu’elles forcent”. [Q011]


### N012 — Why r+1 appears, and why rank one is separate

**Kind:** own idea · **Source:** 159.pdf scan 008, `pages/MPL_159_159_scan008.tex` L25-29; 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L3 · **Quote:** `r+1 inv.`

Confidence: high; reason: the canonical contraction C:V*⊗Sym²V→V sends λ⊗vw to λ(v)w+λ(w)v, and for m(a)(v)=av it gives C(m(a))=(r+1)a. This proves the displayed sufficient splitting condition, while in rank one m itself is an isomorphism even when two is not invertible; research_checks/basic_report.md §B1 and its certificate record the check.

**Context comparison:** Supplies the contraction behind Hua, hua_project/159.modern.tex, §“Les deux données, et l’identification qu’elles forcent”; it does not settle the next all-characteristic question. [Q012]


### N013 — The unanswered canonical-object question is about the torsor

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L3-7 · **Quote:** `est-il vrai ... $\mathcal{T}$ est can. déterminé par $X/S$, sans condit. de dim ni de car. ?`

The explicit question asks whether the underlying torsor T is canonically determined when an infinite projective connection is already given, without the stated dimension or characteristic restrictions. It does not ask whether X carries a unique entire projective connection, and the later torsor of quadratic differentials would contradict that stronger interpretation rather than answer the actual question.

**Context comparison:** Differs from Hua, hua_project/159.modern.tex, §§“Les deux données, et l’identification qu’elles forcent” and “Ce qui ne s’articule pas”, where the object of canonicity is broadened to the projective connection itself; no all-characteristic resolution of the narrower question is established here. [Q013]


### N014 — The manuscript deliberately replaces connections by stratifications

**Kind:** withdrawn in the same text · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L7; 159.pdf scan 010, `pages/MPL_159_159_scan010.tex` L17-25 · **Quote:** `\deleted{connexion} \inserted{stratification}`

The replacements on scan 9, continued on scan 10, matter: the transported structure on principal parts does not preserve the augmentation, and integrability is phrased as extension to the whole projective bundle after forgetting the marked section. In characteristic p an ordinary integrable connection alone does not recover all the higher stratification data, as the explicit comparison in N070 demonstrates.

**Context comparison:** Adds the manuscript’s revision history to Hua, hua_project/159.modern.tex, §“Intégrabilité, et l’écriture en coordonnées”, and restricts the p-curvature speculation in context/README.md; the higher-stratification comparison in N070 is our calculation, not manuscript content. [Q014]


### N015 — The scalar-ring notation on scans 9–10 remains a reading question

**Kind:** reading question · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L11-16; 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L34-36; 159.pdf scan 010, `pages/MPL_159_159_scan010.tex` L6-19 · **Quote:** `\mathcal{O}_S[[\delta f_1,\ldots,\delta f_r]]`

The frozen transcription has O_S in several local power-series expressions, whereas a principal-parts algebra on X normally has O_X as its scalar sheaf. This makes O_X a mathematically motivated alternative for future image review, but the context cannot authorize replacing the visible subscript after the freeze.

**Context comparison:** Differs from the normalized O_X conventions in Hua, hua_project/159.modern.tex, §§“Conventions, valables pour tout le dossier” and “Intégrabilité, et l’écriture en coordonnées”; the supplied interpretation is recorded as the source of the alternative, not as evidence that the ink was O_X. [Q015]


### N016 — The coordinate test for integrability stops before its criterion

**Kind:** unproved claim · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L9-38; 159.pdf scan 010, `pages/MPL_159_159_scan010.tex` L3-25 · **Quote:** `Posant`

The formal coordinate transformations F_i and Φ_i transport the canonical structure, but scan 10 ends after “Posant” before an explicit coefficient criterion for descent to the projective bundle is supplied. A continuation would need to identify which transported formal automorphisms are projective-linear and then check the cocycle condition, especially if higher-dimensional or positive-characteristic conclusions are intended.

**Context comparison:** Agrees with the incompleteness noticed in Hua, hua_project/159.modern.tex, §§“Intégrabilité, et l’écriture en coordonnées” and “Les reprises, et leur ordre”; the later rank-one formal theorem is a different, more restricted problem. [Q016]


### N017 — The cut-off symmetric-algebra formula is not a completed claim

**Kind:** reading question · **Source:** 159.pdf scan 003, `pages/MPL_159_159_scan003.tex` L9-12; 159.pdf scan 004, `pages/MPL_159_159_scan004.tex` L26-31 · **Quote:** `\operatorname{Sym}^n(`

Scan 3 ends inside a symmetric-algebra expression; the next leaf restarts the setup and later gives the completed symmetric algebra in the split case. The second passage helps identify the topic but does not supply the missing ink of the earlier unfinished expression.

**Context comparison:** Differs in documentary scope from the completed exposition in Hua, hua_project/159.modern.tex, §§“Les reprises, et leur ordre” and “Le complété formel le long de la section, et l’action de Ω”; no completion has been inserted in the transcription. [Q017]


## C. The Hodge-theoretic interlude


### N018 — The symplectic extension is a distinct source of torsors

**Kind:** unpursued implication · **Source:** 159.pdf scan 011, `pages/MPL_159_159_scan011.tex` L12-48 · **Quote:** `l’orthogonal de $\Omega$ est $\Omega$`

The de Rham extension has an alternating perfect pairing with Ω as its own orthogonal, and a choice of splitting leaves an alternating form on the quotient. This is a torsor problem over the base of a family of curves, so its relation to the pointed projective bundle on an individual curve needs an actual construction rather than an identification from repeated use of Ω.

**Context comparison:** Restates Hua, hua_project/159.modern.tex, §“La cohomologie de de Rham d’une famille de courbes”, while retaining the distinction between the Hodge bundle Ω and the relative differential line ω emphasized by the manuscript’s notation. [Q018]


### N019 — Isotropic splittings exist locally even in characteristic two

**Kind:** own idea · **Source:** 159.pdf scan 011, `pages/MPL_159_159_scan011.tex` L40-48; 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L3-8 · **Quote:** `formes symétriques sur $\check\Omega$`

Confidence: high; reason: after choosing a local splitting, the obstruction matrix is alternating, and a strict triangular matrix u cancels it through u−uᵗ without division by two. The remaining freedom is a symmetric matrix, giving the stated Γ²Ω-torsor locally; this does not assert a global splitting, and the general argument plus finite-field checks are in basic_report.md §B2.

**Context comparison:** Checks and sharpens Hua, hua_project/159.modern.tex, §“La cohomologie de de Rham d’une famille de courbes”; characteristic-two restrictions in the subsequent multiplication map should not be imported into this local symplectic splitting argument. [Q019]


### N020 — Γ² and Sym² have different integral meanings

**Kind:** own idea · **Source:** 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L3-5; 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L9-14 · **Quote:** `\Gamma^2\Omega`

Confidence: high; reason: for finite free V, Γ²V identifies with symmetric invariant tensors, while Sym²V is the quotient by permutation relations; the natural map sends an off-diagonal invariant to twice its product and a diagonal invariant to its square. Thus that map is invertible after inverting two and kills the off-diagonal generators in characteristic two, which explains a genuine condition on the arrow written on scan 13 without changing Γ² to Sym².

**Context comparison:** Builds on Hua’s explicit Γ²-versus-Sym² distinction in hua_project/159.modern.tex, §“La cohomologie de de Rham d’une famille de courbes”, and clarifies which multiplication arrow carries the characteristic qualification in §“Le compte des quadriques”; basic_report.md §B2 gives the calculation. [Q020]


### N021 — The Kodaira–Spencer arrow has tangent source and symmetric target

**Kind:** reading question · **Source:** 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L14-26 · **Quote:** `\mathcal{T}_{S/T}\longrightarrow\Gamma^2\check\Omega`

The frozen reading is T_{S/T}→Γ²Ω̌, obtained from Ω→Ω̌⊗Ω¹_{S/T}, and the text explicitly discusses principally polarized abelian varieties. Landesman’s algebraic proof of infinitesimal Torelli identifies the dual map with multiplication of canonical differentials [L3, Theorem 4.3], supporting this variance without supplying evidence for a different handwritten glyph.

**Context comparison:** Contradicts the specific variance warning in Hua, hua_project/159.modern.tex, §“Gauss–Manin, et ce que la page 11 ne livre pas”, which reads a cotangent source and an exterior-square target; the present first-pass image reading already had T and Γ² before that context was opened. [Q021]


### N022 — The nonhyperelliptic condition is explicitly on the page

**Kind:** reading question · **Source:** 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L22-26; 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L10-14 · **Quote:** `Épi (cas non hyperelliptique) (car.\ne2)`

The surjectivity arrow is expressly qualified by the nonhyperelliptic case and characteristic different from two; the condition was not supplied by this research commentary. Max Noether’s multiplication theorem supplies the relevant ordinary symmetric-square surjectivity [L4, introduction and theorem], with the extra factor-two issue of N020 for the invariant-square map actually drawn.

**Context comparison:** Contradicts Hua, hua_project/159.modern.tex, §“Le compte des quadriques”, insofar as it says the manuscript does not state the nonhyperelliptic hypothesis; this is a documentary correction to the modernized reading. [Q022]


### N023 — The numerical count requires the surjectivity hypothesis

**Kind:** unpursued implication · **Source:** 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L10-14 · **Quote:** `\frac12(g-2)(g-3)`

The displayed subtraction is correct, and for a nonhyperelliptic curve in the stated setting it computes the kernel dimension of multiplication on quadratic canonical forms. Genus two is a useful boundary case: it is hyperelliptic but ordinary Sym² multiplication is an isomorphism, while for hyperelliptic genus g≥3 its image has dimension 2g−1, so the same subtraction is not the kernel dimension.

**Context comparison:** Refines Hua, hua_project/159.modern.tex, §“Le compte des quadriques”, using the actually present hypotheses and the standard hyperelliptic monomial calculation; basic_report.md §B4 checks the arithmetic, and [L3, §4] supplies the tangent-map identification. [Q023]


### N024 — A possible Gauss–Manin bridge still needs a rank-two construction

**Kind:** own idea · **Source:** 159.pdf scan 012, `pages/MPL_159_159_scan012.tex` L28-35; 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L16-67 · **Quote:** `(\mathcal{DR})_X`

Confidence: medium as a research direction, because the kernel of evaluation Ω_X→ω_X and its symplectic orthogonal suggest a rank-two quotient of the pulled-back de Rham bundle. To obtain a projective connection one must specify the quotient and twists, show that the needed connection descends or choose a replacement, and establish transversality; none of those requirements follows merely from the displayed inclusion chain.

**Context comparison:** Adds an explicit list of missing maps to Hua, hua_project/159.modern.tex, §§“Gauss–Manin, et ce que la page 11 ne livre pas” and “Ce qui ne s’articule pas”, and bears on the comparison requested in RESULTS_STATE.md, MPL_93_002-046 P09. [Q024]


### N025 — The final vanishing fragment needs its actual degree hypothesis

**Kind:** reading question · **Source:** 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L50-67 · **Quote:** `R^1f_*(M\otimes\omega^n)=0`

The short condition following the vanishing formula and the later graded-algebra scratchwork remain uncertain readings, so no exact uniform vanishing theorem is extracted from them. For a line bundle M on a smooth proper curve, Serre duality instead supplies the concrete sufficient condition deg(M)+n(2g−2)>2g−2, and a family statement also needs the appropriate fiberwise and base-change hypotheses.

**Context comparison:** Adds a bounded interpretation to Hua, hua_project/159.modern.tex, §§“Le compte des quadriques” and “Les reprises, et leur ordre”, which do not settle the ambiguous final scratchwork; the sufficient condition is an independent comparison, not a proposed transcription correction. [Q025]


## D. Flat bundles, projective structures, and monodromy


### N026 — The dimension issue is a change of moduli problem

**Kind:** reading question · **Source:** 159.pdf scan 015, `pages/MPL_159_159_scan015.tex` L7-18; 159.pdf scan 016, `pages/MPL_159_159_scan016.tex` L41-49; 159.pdf scan 017, `pages/MPL_159_159_scan017.tex` L3-16; 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L26-35 · **Quote:** `fibrés projectifs analytiques à connexion plate`

Scans 15–17 discuss flat projective bundles without a chosen transverse section; scan 18 separately introduces projective connections with a nonstationary section. For fixed X the first deformation problem has dimension 6g−6 at a point with vanishing infinitesimal centralizer, whereas the projective-structure space has dimension 3g−3; over the moduli of curves these become 9g−9 and 6g−6 respectively on the appropriate smooth loci.

**Context comparison:** Contradicts the proposed dimension repair in Hua, modernised reading of cote 159, hua_project/159.modern.tex, §“L’anomalie de la page 15, et ce que la cohérence demande”: the written relative dimension 6g−6 is consistent with the flat-bundle problem actually defined, and should not be changed to the oper-fiber dimension. [Q026]


### N027 — Dimension-zero automorphisms need not be trivial

**Kind:** unproved claim · **Source:** 159.pdf scan 015, `pages/MPL_159_159_scan015.tex` L14-34; 159.pdf scan 016, `pages/MPL_159_159_scan016.tex` L36-47 · **Quote:** `\operatorname{Aut}^{\unsure{\xi|\zeta}}(P)=1`

The claimed passage from dimension zero to the trivial automorphism group fails for the flat-bundle problem: the subgroup V₄ generated by z↦−z and z↦1/z in PGL₂(C) has centralizer V₄. A surface group of genus at least two surjects onto V₄, so the associated flat bundle has no infinitesimal automorphisms but has nontrivial finite ones; the explicit centralizer calculation is checked in monodromy_report.md.

**Context comparison:** Rechecks and credits the same counterexample already given by Hua, hua_project/159.modern.tex, §“L’espace, et le critère de non-dégénérescence”; this is confirmation of a supplied objection, not a new discovery. [Q027]


### N028 — The exclusion of additive and multiplicative reductions controls only the identity component

**Kind:** unpursued implication · **Source:** 159.pdf scan 015, `pages/MPL_159_159_scan015.tex` L14-34; 159.pdf scan 016, `pages/MPL_159_159_scan016.tex` L7-9 · **Quote:** `G_m\subset GP(1)`

The centralizer argument can force the Lie algebra of automorphisms to vanish, but it must retain a separate condition excluding finite centralizers if a rigid set-valued moduli functor is intended. V₄ is not contained in an additive or multiplicative one-dimensional subgroup, so it passes the stated exclusions while violating the stronger conclusion.

**Context comparison:** Restates the distinction in Hua, hua_project/159.modern.tex, §§“L’espace, et le critère de non-dégénérescence” and “Le calcul de dimension”, with the finite subgroup checked explicitly rather than silently strengthening the manuscript’s hypotheses. [Q028]


### N029 — The 6g−6 calculation survives the finite-automorphism objection

**Kind:** unpursued implication · **Source:** 159.pdf scan 016, `pages/MPL_159_159_scan016.tex` L4-43 · **Quote:** `\dim H^1_{DR}(X,\unsure{\mathfrak g})=2\dim H^0_{DR}(X,\unsure{\mathfrak g})+(6g-6)`

For the rank-three adjoint local system on a compact complex curve, Euler characteristic is 3(2−2g) and the invariant pairing gives h²=h⁰, hence h¹=2h⁰+6g−6. Thus H⁰=0 gives the displayed tangent dimension and H²=0, even when a finite stabilizer remains; this is a calculation for the deformation complex, not proof of a smooth coarse scheme at a quotient singularity.

**Context comparison:** Checks and restates Hua, hua_project/159.modern.tex, §“Le calcul de dimension”, while preventing its use to justify the stronger representability assertion challenged in the preceding subsection. [Q029]


### N030 — Representability is explicitly left for further proof

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 016, `pages/MPL_159_159_scan016.tex` L47-49 · **Quote:** `Sans doute peut-on prouver la représentabilité relative`

The exclamation “donc un foncteur représentable !” is followed by a qualified expectation allowing Artin algebraic spaces, so representability should not be reported as proved on this page. Even after correcting the stabilizer hypothesis, a proof needs an algebraicity theorem and the relevant descent and finiteness conditions; infinitesimal smoothness and objectwise rigidity alone are not that theorem.

**Context comparison:** Agrees with the caution in Hua, hua_project/159.modern.tex, §§“Le calcul de dimension” and “L’espace, et le critère de non-dégénérescence”, and preserves the explicit qualification instead of treating it as a concluded result. [Q030]


### N031 — The quotient notation needs a choice of moduli category

**Kind:** unproved claim · **Source:** 159.pdf scan 017, `pages/MPL_159_159_scan017.tex` L5-18 · **Quote:** `\underline{\operatorname{Hom}}_{\operatorname{gr}}(\pi,H)`

A finite presentation of the surface group gives an affine representation variety by the product-of-commutators equation, but trivial centralizer does not force an orbit to be closed in the full affine representation variety, as required for a direct identification with points of its reductive GIT quotient. A representation Zariski-dense in an upper-triangular Borel gives an example: its diagonal limit leaves the trivial-centralizer locus, so its orbit can be closed in that smaller locus while nonclosed in the full variety; basic_report.md §B5 makes the distinction explicit.

**Context comparison:** Adds a quotient qualification to Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; it does not invalidate the standard analytic Riemann–Hilbert comparison in its proper category. [Q031]


### N032 — The Riemann–Hilbert algebraicity doubt has mathematical substance

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 017, `pages/MPL_159_159_scan017.tex` L16-17 · **Quote:** `n’est pas ... sans doute ... algébrique !`

The marked expectation concerns the comparison from de Rham bundles to representations, not the elementary algebraicity of the representation variety. On the fixed-curve oper locus, algebraic dimension 3g−3 together with Zariski density of a Bers slice in the 6g−6 Betti component obstructs algebraicity of that comparison; the argument and its scope are given in monodromy_report.md using Dumas–Kent [L6].

**Context comparison:** Supports the direction of Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, while adding an actual obstruction and distinguishing it from the separate mapping-class-action expectation. [Q032]


### N033 — The transported outer action is a separate unresolved question

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L3-10 · **Quote:** `sans doute cette opération n’est pas algébrique`

On the Betti representation variety, precomposing by a fixed automorphism of π is algebraic because it replaces each generator matrix by a finite word in the old matrices and their inverses. Transporting this action through a nonalgebraic Riemann–Hilbert map does not automatically prove the resulting de Rham action nonalgebraic, so the manuscript’s expectation is left unresolved in that generality.

**Context comparison:** Refines Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, by separating the checked word-map statement from the unproved transported-action claim; it does not settle RESULTS_STATE.md entry LM1 D.7 on Galois/GT comparisons. [Q033]


### N034 — Canonical Fuchsian uniformization is real analytic

**Kind:** reading question · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L12-24 · **Quote:** `morphisme analytique injectif`

The natural uniformizing representation depends real analytically on Teichmüller space and lands in a totally real Fuchsian locus; it is not a nonconstant holomorphic map into the complex character variety. The word “analytique” therefore needs this distinction, whereas a holomorphic Bers section requires an additional choice and is a different construction [L7, §2].

**Context comparison:** Qualifies Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, where the analytic category is not separated at this point; no word in the frozen text is changed. [Q034]


### N035 — The manuscript suspects nonconstructibility, not constructibility

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L24 · **Quote:** `On suspecte ... pas un sous-ens. constructible`

The sentence retains the negation and the tentative verb despite a rewritten subjunctive or conditional phrase. Its nonconstructibility expectation is supported for the Fuchsian locus: a positive-dimensional complex constructible set contains a positive-dimensional complex analytic piece, which cannot lie in this totally real locus; the same local argument survives an analytic Riemann–Hilbert identification.

**Context comparison:** Contradicts the positive constructibility/algebraicity reading in Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; monodromy_report.md gives the targeted proof and [L7] supplies the geometric input. [Q035]


### N036 — The invariant domain is not unique without an orientation choice

**Kind:** unproved claim · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L24 · **Quote:** `il sera unique`

A cocompact torsion-free Fuchsian subgroup preserves both the upper and lower half-planes, acts freely on both, and has compact quotient on both. Thus the literal uniqueness assertion requires a chosen oriented component or compatible complex marking; the two domains provide a direct counterexample otherwise.

**Context comparison:** Corrects the unqualified uniqueness repeated in Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; the two-component geometry is also explicit in [L7, §2]. [Q036]


### N037 — The fixed-curve projective-connection space is an affine torsor

**Kind:** unpursued implication · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L26-35; 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L6-12 · **Quote:** `C’est un torseur sur le vectoriel de dim finie`

For fixed X, differences of projective connections are quadratic differentials, so the space is a torsor under H⁰(X,K²), of dimension 3g−3 for g≥2 by Riemann–Roch and H¹(K²)=H⁰(K⁻¹)*=0. A torsor supplies no preferred origin, which is why “canonical underlying bundle” does not imply “canonical chosen connection”.

**Context comparison:** Restates Hua, hua_project/159.modern.tex, §§“Le tableau analytique : monodromie, Teichmüller, uniformisation” and “L’énoncé final”, and bears on RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; [L1, §3.1] provides the modern comparison. [Q037]


### N038 — The manuscript asserts and argues fixed-X injectivity

**Kind:** reading question · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L33-40; 159.pdf scan 019, `pages/MPL_159_159_scan019.tex` L3-20; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L13-16 · **Quote:** `En fait c’est un ... mono`

Scan 18 asserts that the forgetful map is a monomorphism, and scans 19–21 pursue an automorphism argument concluding that distinct projective connections are not isomorphic when two is invertible. Over a compact complex curve of genus at least two, pointwise injectivity can be independently proved by uniqueness of the negative section, and Gallo–Kapovich–Marden give the fixed-X proper-embedding statement [L5, §11.4]; the scheme-theoretic family-level word “mono” requires that stronger functorial argument as well.

**Context comparison:** Contradicts the historical description “without answering” in RESULTS_STATE.md, Hua finding 159-monodromy-injectivity-question, and Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”; it does not claim every intermediate handwritten computation is sound. [Q038]


### N039 — Injectivity is not a statement about varying complex structures

**Kind:** unpursued implication · **Source:** 159.pdf scan 018, `pages/MPL_159_159_scan018.tex` L26-35 · **Quote:** `sur $X$`

Fixing X is essential: holonomy on the full space of marked projective structures over Teichmüller space has nontrivial fibers, with grafting providing distinct structures with the same holonomy [L8, introduction and §2.4]. That phenomenon does not refute the fixed-X statement checked in N038.

**Context comparison:** Adds the scope distinction needed when using Hua, findings register, 159-monodromy-injectivity-question, in RESULTS_STATE.md, and Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”. [Q039]


### N040 — The negative section gives an independent injectivity argument

**Kind:** own idea · **Source:** 159.pdf scan 019, `pages/MPL_159_159_scan019.tex` L3-15; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L13-16 · **Quote:** `anti-ample`

Confidence: high under the smooth compact complex genus-at-least-two hypotheses; reason: a transverse section of a flat projective bundle has normal bundle T_X and self-intersection 2−2g. In a ruled surface, if S is negative and S′≡S+dF is a distinct section, then 0≤S·S′=S²+d and hence (S′)²=S²+2d≥−S²>0; therefore the negative section is unique and a flat-bundle isomorphism preserves the oper section, proving fixed-X pointwise injectivity without relying on the disputed coordinate signs.

**Context comparison:** Independently checks the geometric mechanism behind Hua, hua_project/159.modern.tex, §“Les automorphismes du couple (P,σ)”, and refines the treatment of finding 159-monodromy-injectivity-question in RESULTS_STATE.md; monodromy_report.md gives the equivalent quotient-line degree proof. [Q040]


### N041 — The local question is revised from two connections to one

**Kind:** withdrawn in the same text · **Source:** 159.pdf scan 019, `pages/MPL_159_159_scan019.tex` L5-10; 159.pdf scan 019, `pages/MPL_159_159_scan019.tex` L20; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L13-16 · **Quote:** `\deleted{deux}\inserted{une}`

Scan 19 cancels an earlier uniqueness sentence and a moduli diagram, then edits a comparison of c and c′ into a question about an automorphism of one connection. Scan 21 nevertheless states both consequences—distinct connections are not isomorphic and one connection has no automorphisms—so the local revision should not be described as abandonment of injectivity.

**Context comparison:** Adds the sequence of revisions to Hua, hua_project/159.modern.tex, §§“Les automorphismes du couple (P,σ)” and “Le calcul en coordonnées, et la formule encadrée”, and further qualifies RESULTS_STATE.md finding 159-monodromy-injectivity-question. [Q041]


### N042 — The scan 20 formulas have a literal sign conflict

**Kind:** reading question · **Source:** 159.pdf scan 020, `pages/MPL_159_159_scan020.tex` L12-19; 159.pdf scan 020, `pages/MPL_159_159_scan020.tex` L24; 159.pdf scan 020, `pages/MPL_159_159_scan020.tex` L51-58 · **Quote:** `c_{D_t}(1)=1`

The generator formula gives c_D(1)=1, whereas substitution λ=ν=0, μ=1 into the subsequent general formula gives −1; the bracket [−ω,1] also receives inconsistent displayed values later on the page. These are concrete consistency problems in characteristic different from two, so no exact Schwarzian normalization should be extracted from that calculation before resolving the convention or reading; basic_report.md §B3 records the substitution.

**Context comparison:** Adds a literal consistency check to Hua, hua_project/159.modern.tex, §“Le calcul en coordonnées, et la formule encadrée”, and bears directly on RESULTS_STATE.md entry MPL_93_002-046 P01; the frozen signs are retained. [Q042]


### N043 — The factor two tests preservation of the normalized form

**Kind:** unpursued implication · **Source:** 159.pdf scan 020, `pages/MPL_159_159_scan020.tex` L41-46; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L3-15 · **Quote:** `2\omega=0`

In the explicit convention ∂_x+(1+bt+ct²)∂_t, the change z=t/(1+at) produces the linear coefficient b−2a and quadratic coefficient a²−ab+c−a′. Thus preserving a prescribed zero linear coefficient forces 2a=0; this independently checks the kind of obstruction used on scan 21 without validating all of scan 20’s signs or replacing the operator on ω by exterior differentiation.

**Context comparison:** Differs from Hua, hua_project/159.modern.tex, §“Le calcul en coordonnées, et la formule encadrée”, insofar as it reads a dω=0 condition and suggests a translation action of H⁰(K) on the normalized projective-connection torsor; basic_report.md §B3 gives the declared convention and symbolic certificate. [Q043]


### N044 — No automorphisms is a conclusion for opers under the stated hypotheses

**Kind:** unpursued implication · **Source:** 159.pdf scan 019, `pages/MPL_159_159_scan019.tex` L13-20; 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L13-16 · **Quote:** `a fortiori $2\omega=0$`

Once the underlying pointed bundle has the nonzero extension class used on scan 19, its residual automorphisms are parametrized by one-forms, and scan 21’s 2ω obstruction eliminates them when two is invertible. This oper rigidity does not retrospectively eliminate the finite centralizers of arbitrary flat bundles on scans 15–16.

**Context comparison:** Separates the two moduli problems inside Hua, hua_project/159.modern.tex, §§“Les automorphismes du couple (P,σ)” and “L’anomalie de la page 15, et ce que la cohérence demande”; the distinction is also needed for RESULTS_STATE.md finding 159-monodromy-injectivity-question. [Q044]


### N045 — The horizontal-section question is answered later on the same leaf

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 021, `pages/MPL_159_159_scan021.tex` L18-34; 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L3-18 · **Quote:** `question : y en a-t-il ... horizontales ?; Non`

The marginal question is followed by “Non” and a degree argument continuing on scan 22, so it is not an unanswered conjecture in the finished sequence of leaves. In a determinant-normalized rank-two oper, the oper line has degree g−1 while a horizontal line has degree zero; its map to the negative-degree quotient vanishes, forcing it into the oper line, and the two saturated line subbundles then coincide, contradicting transversality.

**Context comparison:** Restates and checks Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, and the mechanism behind RESULTS_STATE.md finding 159-no-reduction-monodromy-dense, with characteristic-zero degree-zero input made explicit. [Q045]


### N046 — A Borel reduction is excluded by the horizontal-line argument

**Kind:** unpursued implication · **Source:** 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L3-18 · **Quote:** `un groupe de Borel`

A horizontal Borel reduction of a flat PGL₂ bundle gives a horizontal point in each projective fiber and hence the forbidden horizontal section. This establishes the Borel exclusion under the smooth-projective, genus-at-least-two, characteristic-zero hypotheses used in the degree argument.

**Context comparison:** Checks and restates Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, and RESULTS_STATE.md finding 159-no-reduction-monodromy-dense; it is the first exclusion, not by itself the full density theorem. [Q046]


### N047 — The torus-normalizer step uses an étale double cover

**Kind:** unpursued implication · **Source:** 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L18-24 · **Quote:** `normalisateur d’un tore`

A reduction to the torus normalizer becomes a torus reduction after an étale cover of degree at most two, and a torus reduction supplies fixed projective points. The pulled-back curve still has genus at least two by the étale Riemann–Hurwitz formula, so the horizontal-section contradiction applies there as well.

**Context comparison:** Checks and restates Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, and the corresponding part of RESULTS_STATE.md finding 159-no-reduction-monodromy-dense. [Q047]


### N048 — The finite algebraic subgroups require one more argument

**Kind:** unproved claim · **Source:** 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L23-24; 159.pdf scan 023, `pages/MPL_159_159_scan023.tex` L2-6 · **Quote:** `sous-groupe ... distinct de $H$`

Excluding a Borel and a torus normalizer does not on its own exclude the finite tetrahedral, octahedral, or icosahedral groups. If monodromy were finite, its kernel would define a finite étale cover on which the flat projective bundle is trivial and therefore has horizontal sections, again contradicting N045; this completes the characteristic-zero complex density proof.

**Context comparison:** Credits and rechecks the same completion in Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, paragraph “Une lacune, et comment la combler”, rather than claiming it as new; it refines the compressed implication in RESULTS_STATE.md finding 159-no-reduction-monodromy-dense. [Q048]


### N049 — The density conclusion is sound with its characteristic-zero scope

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L23-24; 159.pdf scan 023, `pages/MPL_159_159_scan023.tex` L2-6 · **Quote:** `de car nulle ?; Zariski-dense`

Over C, the completed degree and finite-cover argument proves Zariski density for the monodromy of an unbranched projective structure on a compact curve of genus at least two. The author’s characteristic question should nevertheless remain visible, and a proposed extension to positive characteristic needs a different proof and a precise choice between a connection and a stratification. Irreducibility, Zariski density, and Kleinian nonelementarity are different conditions for arbitrary representations; monodromy_report.md §MC13 gives counterexamples to conflating them.

**Context comparison:** Supports the characteristic-zero conclusion, with the finite-subgroup completion credited to Hua, hua_project/159.modern.tex, §“Le calcul de degrés”, paragraph “Une lacune, et comment la combler”, and rechecks RESULTS_STATE.md finding 159-no-reduction-monodromy-dense without promoting an unrestricted variant. [Q049]


### N050 — The degree-zero step fails for ordinary connections in characteristic p

**Kind:** own idea · **Source:** 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L3-16; 159.pdf scan 022, `pages/MPL_159_159_scan022.tex` L23 · **Quote:** `\deg L=g-1`

Confidence: high for the obstruction to this proof; reason: in characteristic p, a Frobenius pullback F*L has a canonical flat connection and degree p·deg(L), which need not be zero as an integer. Thus the rank-one flat-connection input used on scan 22 cannot simply be carried into characteristic p; this observation neither constructs a counterexample to every stronger stratified statement nor computes a p-curvature for the manuscript’s object.

**Context comparison:** Adds a concrete limit to Hua, hua_project/159.modern.tex, §“La densité de Zariski, et où la situer”, and to S20 in context/README.md; Katz [L2, §5, Cartier descent] supplies the standard Frobenius-pullback comparison. [Q050]


## E. Formal normalization and its hypotheses


### N051 — The inserted symbol isomorphism is part of the theorem

**Kind:** unproved claim · **Source:** 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L2-8; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L4-9 · **Quote:** `est un iso`

The formal theorem is stated in characteristic zero and has an inserted isomorphism J/J²→Ω¹_{X/S}; that hypothesis must accompany the existence claim. With the formal line coordinate and this unit symbol, elimination of higher coefficients is possible recursively, whereas injectivity of the symbol alone supports uniqueness but not the same existence statement.

**Context comparison:** Refines Hua, modernised reading of cote 159, hua_project/159.modern.tex, §§“Le cadre, tel que les pages 32 et 33 le posent” and “Le théorème de rigidité”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; formal_report.md checks the distinction. [Q051]


### N052 — Rank-one conormal alone does not imply a formal disk

**Kind:** own idea · **Source:** 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L2-8; 159.pdf scan 033, `pages/MPL_159_159_scan033.tex` L4-24 · **Quote:** `$\mathcal J/\mathcal J^2$ ... inversible`

Confidence: high; reason: the complete augmented dual-number algebra has one-dimensional J/J² but is not a power-series algebra, so that condition alone is insufficient. In the locally free differential-line setting over a Q-algebra, the extra connection with regular symbol repairs the gap: a lowest-order relation in R[[t]] differentiates to a nonzero relation of one lower order, impossible by minimality; formal_report.md gives the precise separated-complete argument. In characteristic p, even unit symbol allows the truncated algebra F_p[x,t]/(t^p) with C=(∂_x+∂_t)dx, so the characteristic restriction matters already for the formal-disk presentation.

**Context comparison:** Adds a missing justification to Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”, and refines the hypotheses behind RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor rather than rejecting its unit-symbol case. [Q052]


### N053 — The second neighborhood reconstructs the extension

**Kind:** unpursued implication · **Source:** 159.pdf scan 025, `pages/MPL_159_159_scan025.tex` L13-17; 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L20-23 · **Quote:** `E=\Omega^{-1}\otimes\mathcal J/\mathcal J^3`

Once multiplication identifies J²/J³ with Ω², twisting 0→J²/J³→J/J³→J/J²→0 by Ω⁻¹ produces 0→Ω→E→O→0. This explicitly recovers the pointed projective-line bundle from order two, while recovering a compatible connection is a separate higher-order problem.

**Context comparison:** Checks and restates Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”, and the underlying-bundle portion of RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor. [Q053]


### N054 — A prescribed third jet and an arbitrary target connection are not independent

**Kind:** reading question · **Source:** 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L24-28; 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L2 · **Quote:** `pour ... tte $c$`

Here “order 3” is explicitly reduction modulo J⁴, and prescribing the cubic jet determines the compatible target quadratic coefficient rather than leaving it arbitrary. For C=(∂_x+∂_t)dx and u₃=id modulo t⁴, any extension preserves the coefficient of t², so it cannot intertwine C with (∂_x+(1+t²)∂_t)dx; thus the literal “for every c” continuation on scan 27 needs compatibility with u₃ or a different quantifier.

**Context comparison:** Adds a quantifier correction to Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”, and qualifies RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; the corrected statement produces one compatible projective connection from each prescribed third jet, as checked in formal_report.md. [Q054]


### N055 — Rigidity is a consequence of the first nonzero coefficient

**Kind:** unpursued implication · **Source:** 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L6-17; 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L21-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L23 · **Quote:** `la cat. des solutions est rigide`

For a regular symbol over a Q-algebra, a nonidentity tangent-to-identity conjugacy has a first nonzero coefficient b_m, whose contribution to the transported connection begins with m·a₀·b_m in degree m−1. Since m is invertible and a₀ is a non-zero-divisor, it cannot stabilize the connection; this supplies the needed concrete freeness rather than deriving it from the abstract group-action lemma.

**Context comparison:** Checks the rigidity conclusion in Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor, while distinguishing it from the faulty general freeness implication in §“La structure du groupe G”. [Q055]


### N056 — The inserted word “pseudo” preserves a global existence issue

**Kind:** unpursued implication · **Source:** 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L8-12; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L28-34 · **Quote:** `\inserted{pseudo} torseur`

The difference between two lifts of a fixed second jet to a third jet is Hom(Ω,Ω³)=Ω², so the set of global lifts, if nonempty, is acted on simply transitively by Γ(X,Ω²). The inserted “pseudo” therefore matters: local lifts and a difference sheaf do not alone establish a global lift, and no preferred zero is supplied.

**Context comparison:** Qualifies the unqualified torsor wording in Hua, hua_project/159.modern.tex, §§“Le théorème de rigidité” and “L’énoncé final”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; sufficient global lifting hypotheses are isolated in N066. [Q056]


### N057 — The recurrence explains exactly where characteristic zero is used

**Kind:** unpursued implication · **Source:** 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L21-45; 159.pdf scan 031, `pages/MPL_159_159_scan031.tex` L20-44 · **Quote:** `(n+1)\alpha_n=0`

Writing h(t)=t+b_m t^m+⋯, the first change in a connection with constant term a₀ occurs in degree m−1 and has coefficient m a₀ b_m; derivative terms in b_m occur later. A unit a₀ and invertible positive integers therefore let one kill each higher term uniquely, while the cubic coefficient changes the quadratic term by 3a₀b₃ in the convention fixed in formal_report.md. These divisions require a Q-algebra, not merely a ring whose additive characteristic is zero: over Z[x] even the first correction can require the unavailable coefficient −1/4.

**Context comparison:** Checks Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”, and the local mechanism for RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor; it does not assume every long expansion on scans 29 and 31 is correct. [Q057]


### N058 — Positive characteristic has explicit resonant automorphisms

**Kind:** own idea · **Source:** 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L29-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L9-23 · **Quote:** `car. nulle`

Confidence: high: over F_p[x], the nonidentity formal automorphism h(t)=t+t^p commutes with ∂_x+∂_t and, for p≥5, is the identity modulo t⁴. It is therefore a nontrivial stabilizer in the very group used for the characteristic-zero uniqueness statement; higher p-powers cover the small primes, so a characteristic-p extension needs extra structure or a different quotient. The example even has zero p-curvature, because the two commuting partial derivations have zero p-th iterates, as checked in formal_report.md using the definition in [L2, (5.0.4)].

**Context comparison:** Adds a concrete resonance to Hua, hua_project/159.modern.tex, §§“Le calcul du changement de paramètre” and “L’énoncé final”, and explains a limit of RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor and of the S20 p-curvature guess. [Q058]


### N059 — Reciprocal series and compositional inverses must be separated

**Kind:** reading question · **Source:** 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L3-18; 159.pdf scan 031, `pages/MPL_159_159_scan031.tex` L46-48 · **Quote:** `u^{-1}`

For the admissible element h(t)=t+t³ of G, its compositional inverse begins t−t³+3t⁵, whereas t/(1+t²) begins t−t³+t⁵. The reciprocal expression becomes correct only with its denominator evaluated at the inverse variable, so the literal same-variable inverse substitution in the scratch calculations cannot be used as an exact identity, even though the leading-coefficient induction can remain valid.

**Context comparison:** Adds a formal-series qualification to Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”, which discusses the multiplicative factor and denominators without separating its reciprocal from automorphism inversion; formal_report.md and formal_group_certificate.json keep this separate from the valid leading-order argument. [Q059]


### N060 — The associated-graded derivation has an integer coefficient

**Kind:** reading question · **Source:** 159.pdf scan 028, `pages/MPL_159_159_scan028.tex` L33-40; 159.pdf scan 033, `pages/MPL_159_159_scan033.tex` L35-45 · **Quote:** `\lambda\omega^i`

For a derivation C with C(t)≡a₀dx modulo t, Leibniz gives C(t^i)≡i a₀t^(i−1)dx modulo t^i. Thus a formula without i on ordinary symmetric powers is false already for i=2 over Q; divided powers would have a different basis and cannot be silently substituted for the written Sym-algebra.

**Context comparison:** Corrects the corresponding degree-lowering formula repeated by Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”; the literal omission in the frozen text is retained and the simple derivation example is certified in formal_report.md. [Q060]


### N061 — The graded operator is a derivation, not a Sym-linear map

**Kind:** reading question · **Source:** 159.pdf scan 033, `pages/MPL_159_159_scan033.tex` L37-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L3-4 · **Quote:** `\operatorname{Sym}(\Omega)-linéaire`

The degree-lowering associated-graded operator satisfies the Leibniz rule, and for C(t)=dx one has C(t·t)=2t dx while t C(t)=t dx. Its degree-one component determines it as a derivation, which is a valid replacement for the stated Sym(Ω)-linearity but not the same assertion.

**Context comparison:** Corrects the manuscript’s linearity claim and the related i-independent multiplication description in Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”; formal_report.md distinguishes this algebraic error from the less certain coefficient glyphs. [Q061]


### N062 — G(c) is defined as a subset, and need not be a subgroup

**Kind:** reading question · **Source:** 159.pdf scan 030, `pages/MPL_159_159_scan030.tex` L11-21; 159.pdf scan 032, `pages/MPL_159_159_scan032.tex` L10-12; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L28-34 · **Quote:** `un sous-ensemble $G(c)$`

The manuscript’s word is “sous-ensemble”, and an element taking c into the preferred slice need not have its inverse take c into that slice. In the concrete formal model, h′=1+h² takes ∂_t to the quadratic vector field (1+t²)∂_t, while its inverse introduces a nonzero t⁴ coefficient, giving an explicit failure of inverse closure.

**Context comparison:** Contradicts the subgroup terminology in Hua, hua_project/159.modern.tex, §“La structure du groupe G”, and refines its use in §“L’énoncé final”; formal_report.md gives both a finite-group example and the formal-series certificate. [Q062]


### N063 — The coset-transversal assertion is valid without a subgroup claim

**Kind:** unpursued implication · **Source:** 159.pdf scan 030, `pages/MPL_159_159_scan030.tex` L21-42; 159.pdf scan 032, `pages/MPL_159_159_scan032.tex` L6-33 · **Quote:** `G_0\times C_0\arrow[r,"\sim"] & C`

If H×C₀→C is bijective and c∈C₀, every left coset of H in G has exactly one representative g with gc∈C₀: normalize gc by the unique H-coordinate. This proves G(c)≈H\G as sets and the factorization G=H·G(c), without requiring G(c) to be closed under multiplication.

**Context comparison:** Checks the valid part of Hua, hua_project/159.modern.tex, §“La structure du groupe G”, while removing its extra subgroup language; this part of the manuscript’s abstract argument survives the later stabilizer objection. [Q063]


### N064 — The abstract freeness question has a counterexample

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 032, `pages/MPL_159_159_scan032.tex` L6-9; 159.pdf scan 032, `pages/MPL_159_159_scan032.tex` L34 · **Quote:** `gc=c\Longrightarrow g=1\ ?`

The stated normal-form hypothesis does not imply that the full G-action is free: take G=H×K acting on C=H through the first factor and C₀={1}, with K nontrivial. Then H×C₀→C is bijective but K fixes every point; concrete formal freeness therefore needs the coefficient argument of N055.

**Context comparison:** Answers negatively the manuscript’s explicit question and corrects the inference in Hua, hua_project/159.modern.tex, §“La structure du groupe G”; formal_report.md includes a finite certificate. [Q064]


### N065 — The orbit intersection is generally a double-coset space

**Kind:** unproved claim · **Source:** 159.pdf scan 032, `pages/MPL_159_159_scan032.tex` L38-42 · **Quote:** `O\cap C_0\simeq{}_{G_0}\backslash G`

For c∈O∩C₀, the correct set is H\G/Stab_G(c), since the orbit is G/Stab_G(c) and C₀ supplies representatives for its H-orbits. The displayed single-coset version follows when the full action is free, which is false abstractly but can be established in the concrete characteristic-zero regular-symbol setting.

**Context comparison:** Corrects the abstract orbit corollary endorsed by Hua, hua_project/159.modern.tex, §“La structure du groupe G”, without automatically rejecting the concrete formal consequence after N055 supplies its missing hypothesis. [Q065]


### N066 — Global jet quotients need a lifting argument

**Kind:** own idea · **Source:** 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L8-12; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L28-34 · **Quote:** `\Gamma(X,\Omega^{\otimes2})`

Confidence: high about the distinction: a sheaf quotient G/G₀≈Ω² does not alone identify Γ(G)/Γ(G₀) with Γ(Ω²), since a global section of the quotient may have a lifting obstruction. Surjectivity does hold for a globally split completed symmetric algebra by the explicit lift t↦t+qt³, and, over a Q-base, for the completion of a pointed projective-line bundle with a given global very regular projective connection, local conjugacies with the prescribed cubic jet glue uniquely; formal_report.md supplies these sufficient hypotheses.

**Context comparison:** Qualifies Hua, hua_project/159.modern.tex, §§“La structure du groupe G” and “L’énoncé final”, and RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor, while respecting the manuscript’s “pseudo” on scan 27. [Q066]


### N067 — Regularity alone does not give normalization existence

**Kind:** own idea · **Source:** 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L4-23 · **Quote:** `régulière ... très régulière`

Confidence: high under the standard non-zero-divisor meaning of a regular section; reason: over R=Q[x], the connection C(t)=(x+t³)dx has regular nonunit symbol x. Any change h=t+b₄t⁴+⋯ modifies the cubic coefficient to 1+4xb₄, which cannot vanish with b₄∈R, so uniqueness under regularity must be separated from existence under the stronger unit-symbol condition.

**Context comparison:** Corrects the conflation of regular and very regular in Hua, hua_project/159.modern.tex, §§“Le cadre, tel que les pages 32 et 33 le posent” and “L’énoncé final”; the manuscript’s own revised wording may be aiming at exactly this distinction, and formal_report.md gives the counterexample. [Q067]


### N068 — The theorem reconstructs a compatible connection, not a distinguished universal one

**Kind:** reading question · **Source:** 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L10-28; 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L6-12 · **Quote:** `muni d’une connexion $c$`

The target consists of a pointed projective bundle together with a connection whose completion is identified with the given formal connection; the text does not select one connection on every curve independently of that input. The third-jet ambiguity and the quadratic-differential pseudo-torsor are evidence of the remaining choice, not an assertion of a canonical origin.

**Context comparison:** Qualifies “with its canonical connection” in RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor and the wording of Hua, hua_project/159.modern.tex, §“Le théorème de rigidité”; the underlying bundle can be canonical without the same being true of an independently chosen connection. [Q068]


### N069 — The coefficient glyph and indices remain unresolved readings

**Kind:** reading question · **Source:** 159.pdf scan 028, `pages/MPL_159_159_scan028.tex` L3-29; 159.pdf scan 031, `pages/MPL_159_159_scan031.tex` L3-54; 159.pdf scan 033, `pages/MPL_159_159_scan033.tex` L18-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L3-4 · **Quote:** `\varpi_0|\bar\omega_0`

Several coefficient signs resemble a modified omega or varpi, while some powers and subscripts in the dense calculation on scan 31 are genuinely uncertain. Hua’s normalized coefficient notation helps state a mathematical model, but it cannot decide those shapes or authorize replacing the first reading in the frozen doubt alternatives.

**Context comparison:** Differs in documentary certainty from Hua, hua_project/159.modern.tex, §§“Le calcul du changement de paramètre” and “Le cadre, tel que les pages 32 et 33 le posent”; these are explicit post-context reading questions, not newly settled readings. [Q069]


### N070 — A concrete characteristic-p follow-up would compare higher stratification data

**Kind:** own idea · **Source:** 159.pdf scan 009, `pages/MPL_159_159_scan009.tex` L7; 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L29-45; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L7-9 · **Quote:** `\inserted{stratification}`

Confidence: high for the local test and medium for a global classification, because the full ordinary principal-parts translation stratification Δx=x+ε, Δt=t+ε detects h(t)=t+t^q, q=p^r≥4, invisible to the ordinary connection: Δ(h(t))−h(Δt)=ε^q, with h fixing x and ε. Thus this family of resonant automorphisms does not preserve that full stratification, as verified in basic_report.md §B6; no claim about divided-power stratifications follows from this calculation. Whether the extra data restore an appropriate global normalization theorem, and how they compare with the actual equations in cote 93, remain questions rather than conclusions of these leaves.

**Context comparison:** Adds a specific test to context/README.md, S20, and RESULTS_STATE.md entries MPL_93_002-046 P01 and P09, rather than asserting a p-curvature result from the title; Katz [L2, §5] provides the external language for that future test. [Q070]


## F. Additional authorial questions and their local disposition


### N071 — The two questions on scan 5 are answered by the following calculation

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 005, `pages/MPL_159_159_scan005.tex` L25-48; 159.pdf scan 006, `pages/MPL_159_159_scan006.tex` L20-46 · **Quote:** `Quel est l’hom canon. épi; Quel est l’autom.`

The first question is answered by π(ω⊗f,g)=ωf+g on scan 5, and the second by u^L_a(g)=(1+a)u_a(g) on scan 6. They are working questions resolved in this sequence, not open conjectures; N010 checks the compatibility condition that motivates them.

**Context comparison:** Restates the completed calculation in Hua, modernised reading of cote 159, hua_project/159.modern.tex, §“Le complété formel le long de la section, et l’action de Ω”, and adds the exact local question-and-answer locations. [Q071]


### N072 — “Vérifions” is followed by an explicit check and “OK !”

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 006, `pages/MPL_159_159_scan006.tex` L38-46 · **Quote:** `Vérifions ... en général par acquit de conscience; OK !`

This verification cue is followed immediately by the compatibility calculation and “OK !”, so it should be indexed as a self-check completed by the author rather than as an unresolved warning. A sign inside the written calculation still has a frozen doubt alternative, which remains a reading issue independent of the mathematical check in N010.

**Context comparison:** Adds documentary detail to Hua, hua_project/159.modern.tex, §“Le complété formel le long de la section, et l’action de Ω”, whose normalized presentation does not preserve the same distinction between a completed check and an uncertain glyph. [Q072]


### N073 — The finite-type qualification is a separate question

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 017, `pages/MPL_159_159_scan017.tex` L5-18 · **Quote:** `de t.f. ?`

The finite-type parenthesis concerns the algebraic moduli object behind the analytic flat-bundle space, not the dimension of the oper fiber. A finite presentation makes the representation variety finite type, but identifying the desired de Rham quotient and its representability needs the additional moduli work already flagged on scan 16.

**Context comparison:** Adds the precise question to Hua, hua_project/159.modern.tex, §“Le tableau analytique : monodromie, Teichmüller, uniformisation”, and keeps it separate from the dimension conflation in §“L’anomalie de la page 15, et ce que la cohérence demande”. [Q073]


### N074 — The formal search is initially conditional on existence

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 025, `pages/MPL_159_159_scan025.tex` L11-28; 159.pdf scan 026, `pages/MPL_159_159_scan026.tex` L2-28; 159.pdf scan 027, `pages/MPL_159_159_scan027.tex` L8-12 · **Quote:** `s’il y en a; Quels sont les autres ?`

The insertion “s’il y en a” and the following classification question precede a heavily revised existence sentence and the characteristic-zero theorem on the next leaf. The later local normalization proof addresses existence with unit symbol and a prescribed compatible third jet, while the global lifting pseudo-torsor of N056 retains a separate nonemptiness issue.

**Context comparison:** Adds the successive qualifications to Hua, hua_project/159.modern.tex, §§“Le théorème de rigidité” and “L’énoncé final”, and refines RESULTS_STATE.md finding 159-formal-rigidity-quadratic-torsor rather than reading unconditional existence into the first question. [Q074]


### N075 — The coefficient question is followed by the characteristic-zero induction

**Kind:** self-flagged: a step he himself marks as unverified · **Source:** 159.pdf scan 029, `pages/MPL_159_159_scan029.tex` L20-45 · **Quote:** `\alpha_n=?`

The inserted question asks for the next coordinate-change coefficient, and the following calculation isolates (n+1)α_n before the characteristic-zero proposition. The coefficient mechanism is checked in N057, while N058 explains why the same induction does not provide uniqueness in characteristic p.

**Context comparison:** Restates Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”, with the question’s actual disposition and its denominator restriction made explicit. [Q075]


### N076 — The mark on scan 31 is not a secure authorial question mark

**Kind:** reading question · **Source:** 159.pdf scan 031, `pages/MPL_159_159_scan031.tex` L54 · **Quote:** `\unsure{!|?}`

The mark attached to the arrows is transcribed with exclamation mark as the first reading and question mark as the alternative. It is therefore included among possible verification flags, but no mathematical statement is designated self-doubted on the strength of that uncertain punctuation alone.

**Context comparison:** Adds a bounded reading issue to Hua, hua_project/159.modern.tex, §“Le calcul du changement de paramètre”; the supplied modernization does not resolve the shape, and the transcription remains frozen. [Q076]


### N077 — The cancelled question about knowing C precedes the coefficient decomposition

**Kind:** withdrawn in the same text · **Source:** 159.pdf scan 033, `pages/MPL_159_159_scan033.tex` L16-31 · **Quote:** `\deleted{\unsure{Comment peut-on connaître $C$}}`

The question is both cancelled and uncertain, and the following lines describe C through its coefficients after choosing a local splitting. The decomposition identifies the degree-one coefficient as connection-like rather than O-linear; that valid distinction is checked in formal_report.md §FC-B1, separately from the erroneous Sym-linearity discussed in N061.

**Context comparison:** Adds the deletion state to Hua, hua_project/159.modern.tex, §“Le cadre, tel que les pages 32 et 33 le posent”, while retaining its valid distinction between the linear coefficient and the other coefficient maps. [Q077]


### N078 — The cancelled jet-extension question is taken up on the next page

**Kind:** withdrawn in the same text · **Source:** 159.pdf scan 006, `pages/MPL_159_159_scan006.tex` L55; 159.pdf scan 007, `pages/MPL_159_159_scan007.tex` L10-36 · **Quote:** `Comment calculer les extensions successives`

The question at the bottom of scan 6 is cancelled, but scan 7 calculates precisely the successive extension Jⁿ/Jⁿ⁺² through the −n v_n pushout. This is a resumption in the next leaf, not evidence that the problem was left untouched.

**Context comparison:** Restates the mathematical development in Hua, hua_project/159.modern.tex, §“La conséquence graduée”, and adds the cancelled-question and resumed-answer locations. [Q078]


## G. Standing question: title sheets and page counts


### N079 — The first scan is an institutional cover

**Kind:** reading question · **Source:** 159.pdf scan 001, `pages/MPL_159_159_scan001.tex` L1-13 · **Quote:** `IMAG; INSTITUT MONTPELLIERAIN; ALEXANDER GROTHENDIECK`

Scan 1 is a printed institutional cover with its graphic, rather than an authorial mathematical title or a handwritten page count. It is included in the transcription and inventory, so the 32 supplied scans comprise this cover and 31 mathematical leaves.

**Context comparison:** Adds the cover omitted from the mathematical page sequence used by Hua, hua_project/159.modern.tex, opening folder/page metadata; context/README.md identifies the dossier but supplies no additional authorial count. [Q079]


### N080 — The authorial title includes “canoniques”

**Kind:** reading question · **Source:** 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L3-5 · **Quote:** `Connexions projectives canoniques et uniformisation des courbes algébriques.`

The first mathematical leaf has this title and the section heading “1. Connexions projectives”. Its word “canoniques” belongs to the transcription, while whether the pages construct a canonical chosen connection must be judged from the narrower questions and torsors discussed in N013 and N068.

**Context comparison:** Adds the full handwritten title to context/README.md’s shorter catalogue title and Hua, hua_project/159.modern.tex, §“Ce que le contenu montre, et ce qu’il ne date pas”, without turning a title into a proved existence statement. [Q080]


### N081 — The archive’s foliation is not an authorial page count

**Kind:** reading question · **Source:** 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L2; 159.pdf scan 013, `pages/MPL_159_159_scan013.tex` L2; 159.pdf scan 015, `pages/MPL_159_159_scan015.tex` L2; 159.pdf scan 023, `pages/MPL_159_159_scan023.tex` L7; 159.pdf scan 025, `pages/MPL_159_159_scan025.tex` L29; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L35 · **Quote:** `% archive foliation: 1`

No authorial statement such as “32 pages” or “Pages 1–33” was located on these leaves, and the later pencil numbers are recorded only as archive-foliation comments. The supplied scan sequence is 1–13, 15–23, and 25–34: scans 14 and 24 were omitted as blank by the input package, so 34 PDF positions must not be reported as 34 supplied handwritten pages.

**Context comparison:** Differs from treating Hua, hua_project/159.modern.tex, opening pages{1}{33}, as an authorial count; its mathematical page n corresponds to our scan n+1, and the actual omissions are specified in the supplied task rather than by a manuscript count. [Q081]


### N082 — No date is supplied by the handwritten title

**Kind:** reading question · **Source:** 159.pdf scan 001, `pages/MPL_159_159_scan001.tex` L1-13; 159.pdf scan 002, `pages/MPL_159_159_scan002.tex` L3-5; 159.pdf scan 034, `pages/MPL_159_159_scan034.tex` L28-35 · **Quote:** `Connexions projectives canoniques`

No authorial date was located in the supplied cover or mathematical leaves. An archival grouping near dated neighboring material cannot by itself date these notes, and no chronological claim about priority is drawn from the mathematical parallels in this report.

**Context comparison:** Retains “s.d.” in context/README.md and agrees with the caution in Hua, hua_project/159.modern.tex, §“Ce que le contenu montre, et ce qu’il ne date pas”, while declining to turn its “Dérivateurs” folder association into a date for the handwriting. [Q082]


## Standing question: what the manuscript itself marks for checking

This index covers the explicit interrogatives, uncertainty phrases, and
verification cues found during the image reading and rechecked against the
frozen text. A working question that receives an answer is still listed;
an uncertain punctuation mark is not promoted to a secure question.

| Scan / TeX line | His words or sign, briefly | Disposition and note |
|---|---|---|
| 005 L25 | “Quel est l’hom canon. épi” | Answered later on the same leaf; N071. |
| 005 L48 | “Quel est l’autom.” … “de la situation ?” | Answered on scan 006; N071. |
| 006 L38–46 | “Vérifions” … “par acquit de conscience”; “OK !” | Author performs the check; N072. |
| 006 L55 | Deleted “Comment calculer les extensions successives” | Resumed and calculated on scan 007; N078. |
| 009 L5 | “est-il vrai” … “sans condit. de dim ni de car. ?” | Unrestricted canonical-torsor question remains open here; N013. |
| 016 L12 | “conditions jamais vérifiées si g=0 — et pour cause !” | A genus-zero exclusion, not a request to verify a step; see N029 and the supplementary event. |
| 016 L49 | “Sans doute peut-on prouver la représentabilité relative” | Representability expectation, with Artin-space qualification; N030. |
| 017 L5 | “de t.f. ?” | Finiteness qualification retained; N073. |
| 017 L16–17 | “Il est immédiat”; inserted “sans doute”; marginal “?” | Representation-variety construction is elementary, RH algebraicity is doubted; N031–N032. |
| 018 L9–10 | “sans doute cette opération n’est pas algébrique”; marginal “?” | Transported outer action is not settled by the RH argument; N033. |
| 018 L24 | “On suspecte” … “pas un sous-ens. constructible” | Negative expectation checked for the Fuchsian locus; N035. |
| 019 L20 | “Peut-on avoir” … “?” with “deux” changed to “une” | Both related conclusions appear on scan 021; N041. |
| 021 L18, L32 | “question : y en a-t-il … horizontales ?”; “Non” | Answer continues on scan 022; N045. |
| 022 L23 | “de car nulle ?” | Characteristic-zero degree argument checked; N049–N050. |
| 025 L11, L26 | “s’il y en a”; “Quels sont les autres ?” | Later normalization theorem and global lifting caveat; N074. |
| 029 L22 | “α_n=?” | Leading-coefficient induction follows; N075. |
| 030 L11 | “quand hĉ est-il de la forme ĉ′ ?” | Defines the subset G(c), followed by factorization; N062–N063. |
| 031 L54 | `\unsure{!|?}` | Possible flag only; N076. |
| 032 L34 | “gc=c ⇒ g=1 ?” | False for the abstract hypotheses; concrete formal freeness checked separately; N064–N065. |
| 033 L16 | Deleted, unsure “Comment peut-on connaître C” | Followed by coefficient decomposition; N077. |

No secure occurrence of “à vérifier”, “sauf erreur”, “je présume”, “admis”,
or “il faudrait vérifier” was located. This is a bounded reading observation,
not a claim that the six physically unreadable word groups contain none of
those words. The candidate-search documentation is
`diagnostics/self_flag_candidates.tsv`; it deliberately distinguishes deleted
questions, completed checks, and uncertain punctuation.


## Primary literature consulted after the freeze

The following references supply comparisons in the research notes, not
transcription readings. The listed statements and sections were checked;
this does not claim independent verification of every theorem in each paper.
Longer independent arguments and exact computation scopes are in
`research_checks/basic_report.md`, `formal_report.md`, and `monodromy_report.md`.

| ID | Primary source and location used | Scope of use |
|---|---|---|
| L1 | A. Beilinson and V. Drinfeld, *Opers*, §§2.6–2.7, 3.1–3.3, [author-submitted text](https://arxiv.org/html/math/0501398v1) | Projective structures, second-order operators, and quadratic-differential torsors. |
| L2 | N. M. Katz, *Nilpotent connections and the monodromy theorem*, Publ. Math. IHÉS 39 (1970), 175–232, §5, especially (5.0.4), Theorem 5.1 and Proposition 5.2, [author-hosted published PDF](https://web.math.princeton.edu/~nmk/old/nilpconn.pdf) | Definition of p-curvature and Cartier descent; specific counterexamples here are independently checked. |
| L3 | A. Landesman, *The infinitesimal Torelli problem*, Theorem 4.3, [author-submitted PDF](https://arxiv.org/pdf/1911.02187) | Tangent-map duality with multiplication of canonical differentials. |
| L4 | E. M. Gagliardi and R. V. Martins, *Max Noether Theorem for Singular Curves*, introduction and main theorem, [author-submitted PDF](https://arxiv.org/pdf/2202.09349) | The smooth nonhyperelliptic multiplication theorem, stated within its extension to integral curves. |
| L5 | D. Gallo, M. Kapovich, and A. Marden, *The monodromy groups of Schwarzian equations on closed Riemann surfaces*, Annals of Mathematics 151 (2000), 625–704, §11.4, [author-hosted published PDF](https://www.math.ucdavis.edu/~kapovich/EPR/GaKaMa.pdf) | Fixed-X holonomy embedding/properness; the independent proof here is only pointwise injectivity. |
| L6 | D. Dumas and R. P. Kent IV, *Bers slices are Zariski dense*, Theorem A and §5, [author-submitted PDF](https://arxiv.org/pdf/0807.4509) | Density used for the separate RH dimension obstruction; its main proof is not independently reproduced. |
| L7 | C. T. McMullen, *The moduli space of Riemann surfaces is Kähler hyperbolic*, §2, [author-hosted preprint](https://people.math.harvard.edu/~ctm/papers/home/text/papers/kahler/kahler.pdf) | Fuchsian real analyticity, total reality, and the two half-planes. |
| L8 | S. Baba and S. Gupta, *Holonomy map fibers of CP¹-structures in moduli space*, introduction and §2.4, [author-submitted PDF](https://arxiv.org/pdf/1402.5445) | Holonomy-preserving grafting and the varying-X distinction. |

## Verification and remaining limits

The exact algebra certificates test the stated examples and finite jets;
the reports separately give the all-orders arguments where those are claimed.
No proof assistant certification or numerical evidence is substituted for a
general proof. In particular, the notes do **not** settle the all-characteristic
canonical-torsor question, the general transported mapping-class-action
algebraicity question, arbitrary-base scheme monomorphism, or nonemptiness of
every global third-jet lifting pseudo-torsor.

The 441 doubt occurrences in the frozen transcription are indexed separately;
research context has not been used to erase them. The six `\illegible` groups
are words, not stand-ins for mathematical symbols. The final hash check and
structural validation are recorded in `progress.log`; the supplied environment
lacked the base LaTeX format and required packages, so no successful PDF
compilation is claimed. No supplied scans, attached context sources, or older
checkpoint ZIPs are included in the final package.
