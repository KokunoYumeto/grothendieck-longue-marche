# Post-freeze context and Oda research record

## Scope and evidentiary status

This research began only after the parent recorded the transcription freeze at **2026-11-16 00:17:03 UTC** and opened the supplied context. No cote 60 manuscript image or crop was consulted by this researcher, and no transcription was edited. Cote 60 references below are to the frozen text in `MPL_60_002-035_transcription.tex`; earlier manuscript references are to the supplied transcription, not a new palaeographical inspection.

The following supplied files were actually read or searched:

- `context/README.md` — read in full.
- `context/notes/RESULTS_STATE.md` — read in full.
- `context/MPL_16+47+54+44_transcription.tex` — searched throughout, then relevant passages read.
- `context/MPL_16+47+54+44_notes.md` — searched throughout, then relevant page notes and supplements read.
- `context/MPL_16+47+54+44_doubts.md` — searched for the relevant locations and reading caveats.
- `context/Oda_1969_first_de_Rham_cohomology_Dieudonne_modules.pdf` — embedded text extracted for navigation; selected mathematical pages checked visually as specified below. No OCR was used.

The context README calls the earlier return a first run. `RESULTS_STATE.md` likewise identifies returned-package research notes as first-pass leads, even where the older note uses the word “established.” The present memo preserves that distinction. Files merely named in the register, including the original WG/WG2 documents, other MPL package notes, and LM7/LM7_PUSH result CSVs, **were not opened**. Their descriptions below are descriptions of the supplied register entries only.

The references `16/048`, `47/008`, and so on mean cote/scan, with leading zeroes added only for consistent indexing. They do not assert a new archival foliation.

## Search record

The principal literal queries were:

```text
poids|pure|pureté|determin|détermin|altern|symplect|lefschetz|duali|semisimple|semi-simple|ration|type|K_0|Grothendieck|hauteur|symbole|conjecture|A\(X\)|C\(X\)

Oda|54/005|54/5|16/048|16/49|16/050|16/035|16/14|44/004|44/4|altern|determin|détermin|Weil|Haar|K-theory|Grothendieck group|poids|weight|rational|functional equation|fonctionnelle|type filtration|height|local symbol

fonctionnelle|fonctions? L|L_E|f_!|f_\\infty|compactif|résolution des singularités|pureté|purement de poids|de poids|type.*[<≤]|ramification|unipotent
```

These were applied with case-insensitive `rg` to the supplied transcription and notes. A small deterministic text parser tracked `\\cotefile{...}` and `\\scanpage{...}` while displaying keyword hits. It did not recognize handwriting or process images. Follow-up queries located exact note headings, including `16:48:1`–`16:50:1`, `47:8:1`–`47:8:6`, and `D01`–`D05`.

The Oda embedded text was searched for `Dieudonn`, `THEOREM 3.19`, `THEOREM 4.4`, `THEOREM 5.10`, `COROLLARY 5.11`, `Frobenius`, `Verschiebung`, `duality`, and the corresponding numbered statements. The official bibliographic landing page was opened at `https://www.numdam.org/item/ASENS_1969_4_2_1_63_0/`; it confirms the author, title, volume, issue, pages, and DOI. A preliminary broad web query returned excessive output and supplied no additional evidence used here.

## C01 — Rationality, motivic duality, and the determinant hypothesis

**Earlier witness:** `context/MPL_16+47+54+44_transcription.tex`, cote 16, scans 048–050, the letter headed 6 January 1966. **Current witness:** cote 60, scans 009, 013, 017, 021, and 023.

Cote 16/048 asks that cohomology be “motive-theoretically” isomorphic to its natural dual and explicitly suppresses twists for exposition. It also explicitly requires that characteristic-polynomial coefficients be rational. The reciprocal of an algebraic endomorphism is then expressed through Cayley–Hamilton; 16/049 argues from this to algebraicity of inverse isomorphisms. The same page separates inverse-closedness from the stronger splitting and semisimplicity expectations, and 16/050 proposes a deduction of the Weil conjectures rather than presenting its proof.

Cote 60/009 visibly changes an initial “motif” to a `Q_l`-sheaf in one sentence, but the determinant conclusion is subsequently stated for a **motif** of weight rho satisfying the Weil conjectures. That distinction matters. The pure-weight absolute-value condition by itself does not supply the pairing or arithmetic rationality needed for every later sign and parity conclusion. The earlier letter provides a precise context in which rationality and motivic duality are separately stated assumptions. This is an interpretive lead about hypotheses, not permission to insert an omitted hypothesis into the frozen text.

Cote 60/013 uses a selfduality to specialize a dual-object functional equation; 60/017 expressly acknowledges the more general relation between two L-functions. These support keeping the general duality statement separate from its selfdual specialization. Cote 60/021 explicitly conditions the boundary discussion on resolution of singularities and the Weil conjectures. Cote 60/023 returns to a motive and weight-indexed virtual pieces.

**Prior notes:** `16:48:2` (suppressed twists), `16:48:3` (rational characteristic polynomials), `16:48:4` and supplement S11 (Cayley–Hamilton), `16:49:1`–`16:49:5` (characteristic-p limitation, inverse, splitting, semisimplicity), `16:50:1` (proposed Weil deduction).

**Register bearing:** WG2 §2.4 #3 and WG2 §2.3 #7 remain unchecked plans. `MPL_14_087-132 M09` is a first-pass lead distinguishing numerical semisimplicity from this conditional cohomological programme. Its underlying file was not read. Cote 60 makes the role of duality and rational determinant assumptions more concrete but does not establish semisimplicity or close either plan item.

## C02 — Alternating forms and the precise use of Lefschetz

**Earlier witness:** cote 16, scans 014–018. **Current witness:** cote 60, scans 009 and 017.

Cote 16/014 begins with a rank `2n` lattice equipped with a “2-forme alternée non dégénérée.” Scans 015–018 develop the Lefschetz operators and a ring of Lefschetz correspondences; 16/018 explicitly invokes a “principe de dualité” and asks about characterizing Lefschetz elements. Cote 60/009 invokes Lefschetz for a selfduality, and 60/017 appeals to an invariant nondegenerate alternating form to force the relevant middle dimension even and the determinant sign positive in the odd-total-weight case.

This is a precise structural connection: alternating duality constrains parity and determinant. It does not show that the general category used in cote 60 was constructed from the rings of cote 16. Nor does the rational-coefficient use in cote 60 resolve the integral divided-power and denominator questions discussed in the earlier context notes.

**Register bearing:** WG2 §2.4 #3 and WG2 §6. #9 remain open research plans. The register's `MPL_14_087-132 M01` (rings versus categories), `M05` (two gradings), and `MPL_15_195-228+18_002-017 M01` (category used rather than constructed) are relevant cautions, not independently reread sources.

## C03 — Weighted determinants and an earlier unfinished count

**Earlier witness:** cote 16/020 and its page notes. **Current witness:** cote 60/011–015 and 023.

Cote 16/020 contains an unfinished weighted Betti-number expression and powers involving `(n-i)b_i`. The supplied notes tentatively relate it to a determinant or graded construction. Cote 60 explicitly introduces an alternating product of Frobenius determinants, substitutes weight exponents, and later writes a virtual-weight formula with `sum_i (-1)^i i beta_i(E)`.

The new packet supplies a concrete example of the same kind of weighted-determinant bookkeeping. It does **not** identify the intended completion of the unfinished calculation in 16/020. A retrospective interpretation should remain conditional, particularly because cohomological degree, Frobenius weight, and Lefschetz grading are distinct indices unless an explicit purity statement relates them.

**Register bearing:** `MPL_14_087-132 M05` and the register's `MPL_15_195-228+18_002-017 M03`, P09, and P14 are relevant first-pass grading/Tate-twist leads. Their original files were not read. No status changes are justified.

## C04 — Conjecture lettering is not resolved by cote 60

The earlier transcription and notes distinguish the draft's conjecture labels from the later printed A/B/C/D/I convention. In particular, the correspondence-duality condition called C in the letter at 16/048 is related to the algebraicity of the Lefschetz inverse operator, not automatically to the printed conjecture C on algebraic Künneth projectors. The context supplement S1 is the location of that dictionary; it remains part of the earlier first-pass return.

Cote 60/011 mentions the standard conjectures and 60/021 the Weil conjectures, but the selected scans do not give a fresh A–D dictionary. Consequently they cannot settle the planning request about “his own lettering.” A bibliography or modern gloss should state its naming convention rather than silently translate the manuscript letters.

**Register bearing:** WG2 §2.4 #3 and WG2 §2.2 #4. The latter concerns the earlier hyperplane-flag argument at 16/042 and 045–046; no new proof of that argument or identification of its stopping point is furnished here.

## C05 — Additivity: split K-theory is a comparison, not the same assertion

**Earlier witness:** cote 16/035, a reused typed K-theory sheet. **Current witness:** cote 60/003, 007, 019, and 035.

The reused sheet defines the “groupe de Grothendieck K(C)” by relations arising from direct sums in an additive category and announces higher K-groups and periodicity. Cote 60/003 says characteristic polynomials turn an exact sequence into a product; 60/007 passes to virtual objects; the later derived discussion takes alternating classes; 60/035 diagnoses a failure of additivity for an underived direct image.

The formal connection is the passage from additive relations to multiplicative determinant invariants. It is essential to distinguish split direct-sum relations from exact-sequence or distinguished-triangle relations. The latter are precisely what a nonexact underived operation may fail to preserve. The reused sheet cannot, by its physical presence, be treated as a theorem supporting the motivic sheaf assertions, or as evidence for a historical derivation of them.

**Register bearing:** the caution in the first-pass `MPL_15_195-228+18_002-017 R01` about reused Lie-theory sheets is methodologically parallel only. It does not identify the provenance of this K-theory sheet. No settled register result applies directly.

## C06 — The epsilon notation has two different functions

**Earlier witness:** cote 47/008, remark 1c; prior note `47:8:4`. **Current witness:** cote 60/007, 009, 021, and 027.

Cote 47/008 writes the identities

`epsilon_B(Phi(F)) = chi_A(F)` and `chi_B(Phi(F)) = (-1)^n epsilon_A(F)`,

and identifies epsilon in the margin with virtual rank. These are relative locally constant numerical functions in `H^0(S,Z)`. Cote 60/007 similarly uses epsilon as a virtual dimension/index in reciprocal-polynomial identities. The later cote 60 notation also uses `epsilon(E)` for a normalized determinant or sign.

This is a concrete reason to separate the two meanings in explanatory notes: a virtual rank is additive and integer-valued, while a determinant sign is multiplicative and, under the stated assumptions, has values in `{+1,-1}`. The matching Greek letter is not itself an identity between the invariants. The earlier Fourier-transform formula provides a useful contextual usage but does not fix every overwritten epsilon in the new manuscript.

## C07 — Derived shifts and signs: a bounded comparison

**Earlier witness:** cote 47/004–005 and 008; prior notes `47:8:1`–`47:8:6`, supplement F4. **Current witness:** cote 60/019, 025, and 035.

In 47/004 the transform-composition formula is revised to include `(-1)^n` and inversion. In 47/005 the functor-level statement includes the shift `[-n]` and a determinant-line factor. These are directly relevant examples of why a derived shift alters a virtual class or determinant calculation. The context notes also preserve an unfinished compatibility check, so the draft itself should not be cited as a complete proof of the Fourier-transform theorem.

Cote 60/025 has the local-duality shifts central to the boundary formula, while 60/035 identifies the danger of applying an underived direct image to a virtual relation. The earlier packet therefore supports careful separation of functor identities, Grothendieck-group identities, shifts, and scalar signs. It does not determine the sign of the boundary formula: the two constructions have different categories and normalization data.

## C08 — The Oda comparison is direct for cote 54, indirect for cote 60

**Earlier witness:** cote 54/003, 005, and 007; prior notes D01–D05. **Current witness:** cote 60/009 and 017.

Cote 54/003 discusses the Hodge sequence of an abelian variety and its dual, together with a vector extension and duality. Cote 54/005 explicitly asks to compare these extensions and dualities with “dualité de Cartier,” then asserts orthogonality of Frobenius kernels in the finite p-torsion duality. Cote 54/007 asks whether the extension can be recovered from the p-torsion group scheme.

Oda's Corollary 5.11 directly addresses the filtered first de Rham cohomology in this last question: for an abelian variety over a perfect field of characteristic p, it canonically identifies the Dieudonné module of the finite group scheme `A[p]` with `H^1_dR(A)` and matches the indicated submodule with `H^0(A,Omega^1)`. This is a statement about the group **scheme** with its Dieudonné information, not about the abstract group of geometric p-torsion points. It does not assert a canonical splitting of the Hodge exact sequence.

Theorem 3.19 separately identifies Cartier duality with Dieudonné-module duality. These are sound primary-source comparisons for the earlier questions. They are only indirect context for the duality and alternating-pairing mechanisms of cote 60. No construction of a Dieudonné module, and no replacement of the `l`-adic Frobenius by Oda's semilinear F and V, is supplied in the selected cote 60 scans.

The context D03 invokes Oda's Theorem 1.1 and Corollary 1.3 for dual kernels of isogenies; D05 invokes Corollary 5.11. The latter has been visually reverified here. The detailed D03 annihilator calculation still needs all Frobenius twists and variance conventions; the present research does not promote that entire editorial calculation to a separately refereed theorem.

## C09 — Heights and local symbols: no new proof in the selected packet

**Earlier witness:** cote 44/002, 004, and 008–009. **Current witness:** cote 60/002–035, searched throughout.

Cote 44/002 states duality and polarization expectations for intermediate Jacobian objects. Theorem 5 at 44/004, labelled “Néron,” proposes an intersection formula for a Néron–Tate pairing and has a marginal remark about a more general fibration statement and a local variant. The 12 August 1964 letter at 44/008 explicitly says that little has been proved; 44/009 leaves positivity to be proved. These are a direct source for the planning title's height material.

The selected cote 60 packet is explicitly titled notes on the functional equation and develops L-functions, duality, determinants, and boundary corrections. Its pairing signs can be compared with the earlier questions, but it supplies no height pairing, local-symbol normalization, or proof of the proposed intersection formula. Hits for “hauteur” in the reused algebra exercises concern height-one prime ideals; they are not arithmetic heights. A “dualité locale” heading does not by itself mean local height symbols.

**Register bearing:** WG H9 is explicitly an unchecked hunch, and WG2 §2.3 #12 an unchecked plan. Neither is proved or refuted by this packet. The appropriate contribution is a sharper division of evidence: the available cote 60 scans substantially concern the L-function part of the planned grouping, while the height and local-symbol questions remain tied to other witnesses.

## C10 — Type bounds and boundary correction are new within this supplied comparison set

Cote 60/021 explicitly gives the boundary object's type bound `<= tau+(n-1)` and weight bound `<= rho+2n`, under stated conjectural assumptions. The subsequent pages develop its functional equation and the correction factor. The searches above found no earlier context passage giving the same type bound, the same boundary L-function, or the same compact-support/direct-image comparison formula.

There were irrelevant keyword hits: “poids” in the reused root-system material at cote 44/007 is representation-theoretic terminology, while “ramification” in reused algebra sheets does not supply the needed sheaf-boundary calculation. These hits were excluded. Thus no earlier context formula was found that would repair or resolve the questionable signs in the new draft. This negative finding is restricted to the supplied context files; it is not a claim about the whole archive or literature.

## C11 — Ledger items not advanced

`RESULTS_STATE.md` lists LM7 E.23 as open: a section-class problem for geometric metabelian and marked depth-two quotients of `U_3/Q`. It lists LM7_PUSH D.44 as proved, with a stated 14 November 2026 referee qualification concerning the parts used by D.50 and E.58. These are pro-finite/group-theoretic statements, not the L-function boundary problem here. No direct mathematical connection was found, and no change in their supplied statuses is proposed.

Likewise the register's additional referee list is a statement about those identified entries, not a general certification of every returned-package note. The supplied context is useful for exact cross-references and research leads; it does not turn this manuscript draft into a proof of any listed conjecture.

## C12 — Oda's underlying dual is the finite-length dual on the reused algebra sheets

**Current witness:** cote 60/016, with continuation 60/012 and the injective-module version at 60/026. **Primary comparison:** Oda (1969), Definition 3.5 and preceding paragraph, printed p. 82; Theorem 3.19, p. 89.

Cote 60/016 defines `E* = Hom_A(E,K/A)` for a principal ideal domain A with fraction field K and proves canonical biduality for finite-length modules. Cote 60/012 proves exactness and the orthogonal-submodule correspondence. Oda identifies `C(k)` with `B(k)/W(k)`, where `B(k)` is the fraction field of the Witt ring, and defines

`D(M) = Hom_{W(k)}(M,C(k))`.

Thus the **underlying module duality** is precisely the same finite-length construction, specialized to the Witt discrete valuation ring. Oda then adds the essential operator rules

`(F alpha)(x) = alpha(Vx)^sigma`, and `(V alpha)(x) = alpha(Fx)^(sigma^{-1})`.

This is a useful exact bridge between the algebra on the reused sheets and the supplied characteristic-p reference. It also identifies the limit of that bridge: the finite-length duality alone does not contain the F/V structure, the group-scheme anti-equivalence, or the de Rham comparison theorem. Physical juxtaposition supplies no proof of authorial intent or historical dependence. The p. 82 image was checked specifically to verify this comparison and both semilinear formulas.

## Oda: primary-source verification and limits

### Bibliography

Oda, T. (1969). The first de Rham cohomology group and Dieudonné modules. *Annales scientifiques de l’École Normale Supérieure, 4e série, 2*(1), 63–135. https://doi.org/10.24033/asens.1175

Official bibliographic record: https://www.numdam.org/item/ASENS_1969_4_2_1_63_0/

The supplied PDF has 74 physical pages. Its first physical page is a repository cover; printed page 63 is physical page 2. For the relevant main text, physical page = printed page minus 61.

| Source location | Verification performed | Result and restriction |
|---|---|---|
| Introduction, printed pp. 63–65; physical pp. 2–4 | Embedded text read | Describes characteristic-p cohomology, Picard schemes, and the Dieudonné ring. It distinguishes general varieties from the abelian case. The Hodge sequence is not claimed to be canonically split. |
| Definition 3.5 and preceding paragraph, printed p. 82; physical p. 21 | **Page image personally checked** | Identifies `C(k)` with the fraction-field quotient of the Witt ring, then defines the dual module using `Hom_W(M,C(k))`, with F and V interchanged through the Frobenius-semilinear rules. This verifies the underlying finite-length duality comparison in C12. |
| Theorem 3.19, printed p. 89; physical p. 28 | **Page image personally checked** | For finite commutative p-primary group schemes, `M(DG)` is canonically isomorphic to `D(MG)` as left Dieudonné modules, compatibly with biduality. This is the exact duality bridge used here. |
| Proposition 3.24, printed pp. 100–101; physical pp. 39–40 | Embedded text navigation/read | Links a homomorphism of an abelian variety to its dual with the induced module map and compatible bilinear form. No independent polarization-positivity conclusion is claimed from this passage. |
| Theorem 4.4, printed p. 105 and following; physical p. 44 and following | Embedded statement read; not separately visually audited | Gives Picard/formal-group comparison statements under properness, global-function, rational-point, and Picard-scheme hypotheses. Its notation should not be generalized to all smooth proper varieties without those hypotheses. |
| Theorem 5.10, printed p. 126; physical p. 65 | **Page image personally checked** | Constructs the cohomological map. In the smooth proper case its image is described by the common kernel of the successive `d V^n` maps. This is a distinguished subspace in general, not automatically all of `H^1_dR`. |
| Corollary 5.11 and following remark, printed p. 131; physical p. 70 | **Page image personally checked** | For abelian varieties over a perfect characteristic-p field, `M(A[p])` is canonically `H^1_dR(A)`; `V M(A[p])` corresponds to `H^0(A,Omega^1)`, and the sequence corresponds to the Hodge sequence. Oda expressly attributes the conjecture to Grothendieck's cited paper. |
| Corollary 5.12, printed p. 131; physical p. 70 | **Page image personally checked** | Gives a canonical injection from the dual Dieudonné module of the Picard p-torsion into first de Rham cohomology in the proper smooth setting with a rational point, with the stated image. It reinforces the need to distinguish general varieties from the abelian isomorphism case. |

The only verbatim quotation used from Oda here is the short remark, “This was conjectured in Grothendieck [15].” All theorem descriptions are paraphrases. The Oda reference [15] is *On the de Rham cohomology of algebraic varieties*; that paper itself was not opened in this task.

Oda's coefficient data must be retained. Over a perfect field k of characteristic p, the Dieudonné ring uses Witt vectors and operators satisfying `FV=VF=p` with Frobenius-semilinear scalar relations. On the p-killed module corresponding to `A[p]`, these still carry essential structure. Oda does not prove the global `l`-adic L-function equations of cote 60, supply a boundary type filtration, or justify replacing purity by selfduality. His theorem answers a precise part of the earlier de Rham/p-torsion question, which is its proper evidentiary role in this packet.

## Editorial disposition

All findings above are for the research notes. They supply no authorized changes to the frozen transcription. The strongest positive links are (i) explicit rationality and motivic duality in 16/048–050, (ii) alternating-form and Lefschetz structure in 16/014–018, (iii) virtual-rank epsilon and shifts in 47/004–008, (iv) the primary Oda theorem answering the filtered-cohomology part of 54/007, and (v) Oda's precise use of the finite-length duality present on the reused algebra sheets in cote 60. The strongest negative findings are the absence of an earlier matching boundary/type formula in the supplied context and the absence of a height/local-symbol proof in the selected cote 60 scans.
