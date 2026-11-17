# Motivic comparisons and the planning questions

Research only; transcription frozen on 17 November 2026 at 20:48:04 UTC. No page fragment or combined transcription was changed for these notes. The current evidence comprises the 31 selected scans of cote 15, 034–086, not every intervening scan and not the entirety of cotes 12–18.

## Evidence and inherited status

The following abbreviations specify exact files; scan numbers always mean archive scans, not the foliation printed on the leaf. The `pages/...` paths are relative to this package; `context/...` paths identify the supplied external context.

- **P084/P086:** `pages/MPL_15_034-086_15_scan084.tex` and `pages/MPL_15_034-086_15_scan086.tex`, frozen current transcription; their archive foliations are 83 and 85.
- **CT:** `context/MPL_16+47+54+44_transcription.tex`, an explicitly unreviewed first-pass contextual transcription; references such as CT16/047 identify its cote and scan commands. The underlying scanned leaves were not supplied as current evidence.
- **N87:** `context/same_cote_15/MPL_15_087-138_notes.md`; **N195:** `context/same_cote_15/MPL_15_195-228+18_002-017_notes.md`. Both are first-pass research leads, not independently verified neighboring manuscripts.
- **RS:** `context/notes/RESULTS_STATE.md`, read in full; its reported statuses remain attached below. **WG2 §2.4 #3**, **WG2 §2.3 #2**, **WG2 §2.3 #7**, and **WG2 §Summary #2** are unchecked planning questions, not established mathematical results.
- **HM:** `context/hua_project/15.modern.tex`, Michel Hua project's AI-produced modernized reading, read after `context/hua_project/README.md`. Its section V, “Algèbres de Riemann et tores compacts (pages 83 à 87),” is the directly relevant comparison; section VII treats pages 134–138 outside this packet. Modernized explanations are credited to that project and are never used to repair the frozen transcription.

The principal current difference is unusually clear: scan 084 starts with an existing motivic category and explicitly restricts its band to be commutative; scan 086 ends by asking for the character and cocharacter still to be determined. Neither page constructs the category, supplies the arithmetic extension over the geometric base field Q, or formulates period genericity. Notes R01–R14 contain the separate torus, positivity, norm and descent analysis; it is not repeated here.

## Answers to the planning questions

| Planning question | Answer supported by this packet | Context and limit |
|---|---|---|
| Are the motives built from cote 16's Lefschetz correspondence rings? | **Not demonstrated.** P084 begins “M catégorie motivique,” and uses its endomorphism algebra. | CT16/018 defines a Lefschetz correspondence ring; CT16/049 describes a semisimple-motive “yoga.” These provide a proposed relationship, not a construction of P084's category. RS: WG2 §2.4 #3; N87 L01 and N195 M01, first-pass leads. The missing cote 12 typescript remains missing. |
| Is the Lefschetz sl2 inside this motivic Galois group? | **No nonzero sl2 can lie in the Lie algebra of this particular commutative G.** | This is a new consequence of P084's explicit restriction, not a rerun of the already recorded projective-line calculation in N87 L03 / RS MPL_14_087-132 M04. A correspondence action and tensor automorphisms of a fibre functor are different constructions. |
| Is the grading the weight cocharacter? | **The packet leaves the identification and normalization unfinished.** | P086's final NB requests determination of both ε and j. N195 P14's section of ε in a Levi quotient, reported at 18/011, must not be substituted for a weight cocharacter in the full group. |
| What is the exact A–D dictionary? | **Two identifications are well supported by the contextual operations; two remain provisional.** | A maps to modern A and manuscript C to modern B; the likely B-to-D and D-to-C assignments are not explicit definitions in the supplied excerpts. See the separate table below. Current pages add no A–D definitions. |
| Does cote 14 resume CT16/047's singular-hypersurface programme? | **Undetermined here.** | CT16/047 explicitly calls for singular varieties after Serre's objection. No actual cote 14 text is included in this current packet; RS summaries of its earlier returns do not supply the missing witness. |
| Is the arithmetic extension over Q present? | **Not in these 31 scans.** A precise modern Nori sequence is given below. | The “G sur Q” in P084 concerns coefficients, while the geometric field is denoted k. N87 reports an Artin quotient on scans 135–138, which are outside this selection. |
| Did he write a period conjecture? | **No such statement occurs in the current selection; neighboring first-pass notes report explicit written witnesses.** | N195 P15/P22 report live statements on 18/011 and 18/013; P18 records an entirely cancelled 18/012 draft. Independently, his own published 1966 de Rham paper, p. 102 n. 10, is a direct printed witness. |
| Which S15 statements have modern theorems? | **Some categorical and group comparisons do, in specified theories; no blanket identification of P084's M follows.** | Nori–Ayoub group comparison, pure Nori–André comparison, numerical semisimplicity, and the arithmetic Nori sequence are distinct results with distinct inputs. The precise scope appears below. |

## Requested table: linear statement and nonlinear statement

These are comparisons between particular assertions. The change from linear to nonlinear does not turn one theorem into another.

| Pair | Linear statement, with hypotheses | Nonlinear statement, with hypotheses | What the current pages contribute |
|---|---|---|---|
| Tate and anabelian Hom | For abelian varieties A,B over a finite field k and ℓ different from its characteristic, Tate's map Zℓ⊗Hom_k(A,B) → Hom_Gk(TℓA,TℓB) is an isomorphism [T66, Main Theorem]. | For smooth proper geometrically connected curves of genus at least two over a sub-p-adic field K, dominant K-morphisms are recovered from continuous open homomorphisms of arithmetic fundamental groups over G_K, modulo geometric inner automorphisms [M99, Theorem A]. | P084 uses a representation of a commutative motivic band on a faithful object. It gives neither Hom comparison; in particular it contains no hyperbolic fundamental-group reconstruction. N195 B01 and §4 are already first-pass leads for this comparison. |
| Semisimplicity and trivial centres | For a connected affine group scheme G over a field of characteristic zero, its category of finite-dimensional representations is semisimple if and only if G is an inverse limit of reductive algebraic groups; for finite-type G this is reductivity [DM, Proposition 2.23, p. 26]. | The geometric profinite fundamental group of a hyperbolic curve in characteristic zero is slim: every open subgroup has trivial centre [M04, Lemma 1.3.1]. | P084 actually assumes G commutative. Thus its centre is the entire group, even though multiplicative-type representations are semisimple in characteristic zero; this current hypothesis directly prevents identifying semisimplicity with centrelessness. |
| Polarizations and real structures | A polarization supplies a positive adjoint operation, and the compact-band description is made precise in [DM, Theorem 4.17]. | For a smooth projective real hyperbolic curve, the real section theorem identifies conjugacy classes of sections with connected components of X(R), not individual real points [PAL, Theorem 1.3]. | P084's chosen polarization leads to a unitary kernel and compact torus. It does not produce sections of an arithmetic fundamental-group extension. N195 B03 and RS MPL_18_018-062 RH19 remain comparison leads, not proofs of such an identification. |
| Weights and cyclotomic normalizers | Over number fields, the non-Tate condition excludes equivariant maps Zℓ(1) → TℓA for abelian varieties A; Stix relates this to weights [ST, Definition 26]. | For a hyperbolic curve under the non-Tate hypothesis, the cusp-inertia criterion requires a nontrivial procyclic pro-ℓ subgroup whose normalizer has open arithmetic image **and acts through the cyclotomic character** [ST, Definition 29 and Theorem 30]. | P086 asks for ε and j; it identifies no normalizer conjugation character. RS LM6 A.22 therefore remains Open (return's claim), and the truncated LM6 A.50 entry remains Proved (return's claim) without supplying an unstated missing hypothesis. |

The Tate row deliberately states the finite-field theorem that was checked; it does not silently transplant that theorem to the sub-p-adic base of the anabelian row. Abelianization and Jacobians motivate the comparison, but the full nonabelian homomorphism retains information absent from the Tate module.

## A–D: the most precise dictionary the supplied evidence permits

The modern labels below are checked against [MIL25, Chapter VI §8]: A is the Lefschetz isomorphism restricted to algebraic classes, B algebraicity of the inverse Lefschetz operator, C algebraicity of Künneth projectors, and D equality of homological and numerical equivalence. The manuscript side remains an inference from the **unchecked CT**, not an image-verified definitive concordance.

| Manuscript label in CT16 | Modern label | Exact contextual witness | Assessment |
|---|---|---|---|
| A | A: Lefschetz on algebraic classes | CT16/044 gives equality of dimensions of algebraic-class spaces; CT16/045 defines the critical-degree A⁰ conditions; CT16/050 discusses the weak algebraic-class variants. | Supported operational identification; its polarization and cohomology subscripts must be retained where present. |
| C | B: algebraic inverse Lefschetz | CT16/042 relates C(X) to algebraicity of Λ_Xφ_*; CT16/045(iv), 048–049 characterize algebraic inverse isomorphisms. | Supported operational identification, not the modern Künneth label C. |
| B | D: homological equals numerical equivalence | CT16/044: “A+index implies B”; CT16/045 says A equals B under the index theorem. | Plausible, matching the modern implication, but no independent defining sentence for manuscript B was supplied. |
| D | C: algebraic Künneth projectors | CT16/040 connects D(Y) with algebraicity of projectors; CT16/048 uses D to obtain rational characteristic polynomials. | Plausible, but these implications do not uniquely constitute a definition of manuscript D. |

**Current difference:** none of these four definitions occurs in P084–P086 or elsewhere in the selected 31 scans. The dictionary refines the answer to WG2 §2.4 #3 only at the level already recorded in N195 M04; it does not upgrade that first-pass lead to a reviewed archival result.

## The arithmetic Q-sequence and the precise S15 scope

Fix Q̄⊂C and compatible Betti fibre functors for rational Nori motives. Write G_N(k,ω_B) for the corresponding affine group scheme over the coefficient field Q, and write underline(Γ_Q) for the proconstant Q-group scheme associated with Gal(Q̄/Q). Kahn's Galois-descent exactness theorem and its Nori application give

\[
1\longrightarrow G_N(\overline{\mathbf Q},\omega_B)
\longrightarrow G_N(\mathbf Q,\omega_B)
\longrightarrow \underline{\operatorname{Gal}(\overline{\mathbf Q}/\mathbf Q)}
\longrightarrow1.
\]

The left map comes from extending the geometric base field; the right map comes from restriction to the full Artin subcategory [K25, Theorem 5.10 and §10, especially Theorem 10.2]. This is exactness of affine group schemes, not a claim of surjectivity on Q-points or a chosen splitting. P084 neither states this sequence nor identifies its kernel with G°. Indeed, its commutative finite-type band cannot surject onto the full nonabelian absolute Galois group; a commutative motivic subcategory sees only its corresponding Artin quotient.

| S15 comparison | Verified theorem | What it does not establish about the manuscript |
|---|---|---|
| Classical Nori and Ayoub groups | The comparison Hopf-algebra maps are inverse; rational coefficients are included in the PID-coefficient theorem [CG, Theorem 9.1]. | No automatic identification with an unspecified category M, and no assertion here of an entire triangulated equivalence or a motivic t-structure. |
| Pure rational Nori motives | Semisimplicity and the equivalence with André motives are given by [AR, Theorems 6.3.3 and 6.4.1]. | Motivated correspondences are not identified with algebraic cycle classes by these comparison theorems alone. |
| Numerical motives | Semisimplicity for numerical equivalence is [J92, Theorem 1]. | It does not itself make a cohomological realization factor through numerical equivalence; Jannsen's Corollaries 1–2 have additional Künneth hypotheses. |
| Arithmetic extension | The exact sequence displayed above holds in the specified Nori setting [K25]. | P084's coefficient field Q does not identify its geometric base, and its commutative band is a restricted case. |
| Hodge fullness, algebraic cycles, period genericity | These are separate comparison or transcendence assertions; [AR, §7.1] and [BC, §2.2] explicitly separate the issues. | None follows merely from the group isomorphism, pure semisimplicity, or existence of a period torsor. |
| Current positive-characteristic and integral material | The pages themselves supply the crystalline/Deuring questions discussed elsewhere in this report. | The characteristic-zero Betti comparisons just cited cannot be applied by changing the base field to a finite field or by discarding integral structures. |

## Sixteen individual observations

### MB01 — The category is an input on the current page

**File/scan/quote:** P084, 15/084: “M catégorie motivique”; CT, 16/018: “anneau … de correspondances Lefschetzien.” **Kind:** observation and unpursued implication. **RS:** WG2 §2.4 #3, WG2 §Summary #2 [unchecked plans]; MPL_15_087-138 L01 and MPL_15_195-228+18_002-017 M01 [first-pass leads].

The new current witness is the opening assumption of M on 084, not a construction from the CT16 ring. Such a construction would have to specify correspondences between distinct varieties, their composition, projectors and Tate twists, not only the endomorphism algebra of one faithful object. The previously recorded absence of that construction in neighboring extracts is therefore corroborated locally, without deciding what the unavailable cote 12 typescript contains.

### MB02 — Commutativity gives a local obstruction to the proposed sl2 inclusion

**File/scan/quote:** P084, 15/084: “le lien … commutatif”; CT, 16/014–018, Lefschetz operators and ring. **Kind:** own idea, a current-page deduction. **Confidence:** high, because a Lie homomorphism kills commutators when its target is abelian. **RS:** WG2 §2.3 #2 and §2.4 #3 [unchecked plans]; MPL_15_087-138 L03 and MPL_14_087-132 M04 [first-pass subgroup-obstruction leads].

For this particular G, any Lie map sl2→Lie(G) is zero since sl2=[sl2,sl2] and Lie(G) is abelian. This is the additional obstruction supplied by 084; the earlier projective-line calculation is not rederived. It remains consistent with an SL2 action by invertible correspondences, exemplified by [BE, Theorem 3.3], rather than an embedding in this tensor-automorphism group.

### MB03 — The unfinished NB prevents a forced weight normalization

**File/scan/quote:** P086, 15/086: “Il convient de déterminer ε … et j”; N195 P14, reported 18/011: “hom central (Tate)” and “ε∘j=id.” **Kind:** self-flagged unfinished task and comparison. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 P14 [first-pass lead].

The current page supplies the directions ε:G→G_m and j:G_m→G but no composite or exponent convention. A weight grading in a pure Tannakian category is a central cocharacter [DM, Definition 5.1], whereas the cited neighboring section is reported in a Levi quotient. Notes R08–R10 handle the independent integral-character and weight-convention questions; neither that analysis nor this neighboring lead licenses inserting a normalization into P086.

### MB04 — A partial A–D concordance must stay partial

**File/scan/quote:** CT, 16/044: “A+index implies B”; 16/048: “C … equivalent … D … [and] an isomorphism … algebraic”; N195 M04. **Kind:** reading question and contextual comparison. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §2 [first-pass observation].

The operations support A→modern A and C→modern B, while B→modern D and D→modern C remain the plausible completion displayed above. Modern implications [MIL25, VI §8] explain that completion without converting implications into historical definitions. No selected current page strengthens the evidence for the two provisional entries.

### MB05 — The singular-hypersurface question remains outside the supplied source coverage

**File/scan/quote:** CT, 16/047: “work also with singular ones”; N195 M05, reporting 15/223: “Il suffirait de construire.” **Kind:** unpursued programme and source-coverage limit. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_14_002-044 §2 and §107 [first-pass summaries only].

CT reports that Serre's simply-connectedness objection defeated the proposed reduction through nonsingular hypersurfaces and prompted a reformulation for singular varieties. The current 15/034–086 selection contains no execution of that programme, and the actual cote 14 text is not supplied here. The distinct construction reported at 15/223 concerns comparison of cohomological data and cannot answer the missing historical question.

### MB06 — The two occurrences of Q have different roles

**File/scan/quote:** P084, 15/084: inserted uncertain “k un corps,” followed by “G sur Q”; N87 L01, reported 15/135: “M catégorie des (iso)-motifs.” **Kind:** reading distinction. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_087-138 L01 [first-pass lead].

The frozen text distinguishes a geometric base k from a rational coefficient group; the uncertainty on the insertion is retained. Therefore “G sur Q” is not evidence that the motives themselves are over the arithmetic base Q. This locally explains why the requested extension by Γ_Q cannot be read into the notation of 084.

### MB07 — A modern arithmetic sequence also exposes the restriction of this page

**File/scan/quote:** P084, 15/084: “comm de type multiplicatif”; N87 introductory planning table, reported 15/135–138, Artin quotient G→G′. **Kind:** literature comparison and own deduction. **Confidence:** high for the deduction, since every quotient of a commutative group is commutative. **RS:** MPL_15_087-138 S15 and MPL_15_195-228+18_002-017 S15 [first-pass observations]; WG2 §2.4 #3 [unchecked plan].

The exact Nori sequence above is a theorem in a specified modern category [K25], not an assertion transcribed on 084. Its full Γ_Q quotient is incompatible with retaining this page's commutative-band restriction. Consequently the present discussion can at most concern a restricted motivic/Artin subcategory when the geometric base is Q; no identification with the full arithmetic motivic group follows.

### MB08 — Nori–Ayoub comparison does not fill in M retrospectively

**File/scan/quote:** P084, 15/084: “de gerbe G”; N195 M07, reported 15/213: “G(X,ξ)=Aut(ξ).” **Kind:** unpursued implication and literature comparison. **RS:** MPL_15_087-138 S15 and MPL_15_195-228+18_002-017 M07, S15 [first-pass leads].

The checked comparison [CG, Theorem 9.1] supplies an isomorphism between the classical Nori and Ayoub groups with compatible realization data. The new current page still supplies no comparison functor from its M into either theory, so that theorem cannot identify the historical band by itself. Its Betti construction also does not settle the packet's finite-characteristic crystalline questions.

### MB09 — Semisimplicity has to be attached to the equivalence relation

**File/scan/quote:** CT, 16/049: “the category of motives which is semi-simple”; P084, 15/084: “A=End_M(E).” **Kind:** literature comparison. **RS:** WG2 §2.3 #7 [unchecked plan]; MPL_15_087-138 L16 [first-pass lead].

Jannsen's numerical semisimplicity theorem [J92, Theorem 1] verifies a precise modern statement, while [AR, Theorems 6.3.3 and 6.4.1] treats pure rational Nori motives through André motives. Neither identifies the manuscript's unspecified correspondence relation or proves that its intended cohomological realization descends to numerical motives. Current 084 uses a positive adjoint structure on one endomorphism algebra and adds no missing cycle-comparison map.

### MB10 — The reported period witnesses are neighboring evidence, with different textual states

**File/scan/quote:** N195 P15, reported 18/011:L65–76: “Conj. de transcendance forte”; P18, 18/012:L2–24: cancelled body; P22, 18/013:L2–6: “degré de transcendance égal à dim G (4 ou 2)?” **Kind:** conjecture reported by unchecked context. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §2 [first-pass observation]; no dedicated proved period result.

The current selected scans contain no period-genericity statement. N195 reports a live degree g+u assertion for the joint Betti–de Rham and Hodge-splitting data on 18/011, a cancelled normalized degree dim G−1 draft on 18/012, and a live elliptic degree dim G question on 18/013. These distinguish both stronger augmented data and cancellation state; they must not be reported as original manuscript images checked in this packet.

### MB11 — There is also a direct published witness in Grothendieck's own writing

**File/scan/quote:** `context/README.md`, planning paragraph: “His period conjecture is known through others' reports”; N195 P20/P26, reported 18/012 and 013, period questions. **Kind:** bibliographic correction and literature comparison. **RS:** WG2 §2.4 #3 [unchecked plan]; MPL_15_195-228+18_002-017 §2 [first-pass observation].

Grothendieck's 1966 de Rham paper explicitly discusses conjectural independence of elliptic periods and quasiperiods, and extensions to abelian varieties [GR, p. 102 n. 10]. Thus the README phrase cannot be retained as an exclusive bibliographic claim, independently of the neighboring manuscript reports. This establishes a printed witness, not a date or revision chronology for the unverified 18/011–013 leaves.

### MB12 — Faithful representation is not the anabelian Hom theorem

**File/scan/quote:** P084, 15/084: “E un motif ‘fidèle’”; N195 B01, reported 15/227: “dans quelle mesure un morphisme de préschémas … est connu par.” **Kind:** comparison of scopes. **RS:** MPL_15_195-228+18_002-017 B01 and §4 [first-pass leads].

The Hom row above compares Tate's linear homomorphism with Mochizuki's open homomorphisms over G_K, including their different field hypotheses [T66; M99]. The extra current evidence is only the chosen faithful object for the commutative band; it does not produce full faithfulness for varieties. No earlier Jacobian or projective-line calculation is repeated.

### MB13 — The current centre is as large as possible

**File/scan/quote:** P084, 15/084: “commutatif” and “G° est un tore”; N195 B02. **Kind:** own idea, local comparison. **Confidence:** high, directly from the stated commutativity. **RS:** MPL_15_195-228+18_002-017 §4 [first-pass comparison]; WG2 §2.4 #3 [unchecked plan].

Here Z(G)=G, so any analogy with the trivial centres of hyperbolic geometric fundamental groups must concern the role of structural rigidity, not equality of properties. This current-page observation is stronger as source evidence than repeating the previously supplied abstract G_m example. The slimness assertion concerns the geometric group [M04, Lemma 1.3.1], with no claim that every arithmetic absolute Galois group is slim.

### MB14 — Positivity and the real section theorem solve different reconstruction problems

**File/scan/quote:** P084, 15/084: “Choisissons une forme de polarisation”; N195 B03, reported 15/217: “réellification”; RS MPL_18_018-062 RH19, reported 18/034: “f∞ j(λ) f∞⁻¹=j(λ′).” **Kind:** unpursued implication and scope distinction. **RS:** MPL_15_195-228+18_002-017 B03 [first-pass lead]; MPL_18_018-062 RH19 [first-pass own-idea lead].

The current polarization governs an adjoint involution and a compact torus, as Notes R02–R05 analyze. The cited real section theorem [PAL, Theorem 1.3] reconstructs real connected components from section classes, so it cannot turn this choice of polarization into a chosen real point. RH19 is an available comparison lead about real Frobenius and a positive form, not an argument present on 084.

### MB15 — No cyclotomic normalizer premise is supplied by the norm character

**File/scan/quote:** P086, 15/086: “déterminer ε”; RS LM6 A.22: “normalizer … has open image”; N195 B04–B05. **Kind:** unpursued implication and ledger boundary. **RS:** LM6 A.22 [Open, return's claim]; LM6 A.50 [Proved, return's claim, displayed summary truncated]; MPL_15_195-228+18_002-017 B04 and §137 [first-pass leads].

Stix's criterion includes the cyclotomic conjugation action as well as open arithmetic image [ST, Definitions 26/29 and Theorem 30]. Neither the final norm-character question on 086 nor the supplied truncated A.50 summary identifies that action for the procyclic subgroup of A.22. The current-page difference is therefore negative but exact: no result status changes, and the missing character step is not supplied by these commutative torus calculations.

### MB16 — A gerbe, a comparison torsor, and a generic period point are separate data

**File/scan/quote:** P084, 15/084: “de gerbe G”; N195 P23, reported 18/013:L8–10: “A-t-on H=G”; N195 M08, reported 15/215: “Caractériser l’image ??” **Kind:** unpursued implication and literature comparison. **RS:** MPL_15_195-228+18_002-017 M08 [first-pass lead]; claims #964 [open candidate problem in the supplied registry]; WG2 §2.4 #3 [unchecked plan].

In the modern period formulation, an isomorphism torsor between de Rham and Betti fibre functors carries a comparison point; genericity of that point is the extra conjecture [BC, Conjecture 2.12]. P084 supplies neither those two fibre functors nor that comparison point, while the reported question H=G concerns generation and need not assert genericity. No classification of places by motivic torsors, no Hodge essential-image assertion and no period transcendence claim is established by the present compactness argument.

## Primary references and checked versions

The manuscript/context quotations above are from supplied files. The following primary sources support the external assertions; the exact checked arXiv versions are linked. No present-day blanket claim about all open standard or period conjectures is inferred from an older paper.

| Key | Primary source and exact locator | Link |
| --- | --- | --- |
| T66 | J. Tate, *Endomorphisms of Abelian Varieties over Finite Fields* (1966), Main Theorem, p. 134. | [PDF](https://pazuki.perso.math.cnrs.fr/index_fichiers/Tate66.pdf) |
| M99 | S. Mochizuki, *The Local Pro-p Anabelian Geometry of Curves* (1999), Theorem A, p. 3. | [PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/The%20Local%20Pro-p%20Anabelian%20Geometry%20of%20Curves.pdf) |
| M04 | S. Mochizuki, *The Absolute Anabelian Geometry of Hyperbolic Curves* (2004), Lemma 1.3.1 and Corollary 1.3.2. | [PDF](https://www.kurims.kyoto-u.ac.jp/~motizuki/Absolute%20Anabelian%20Geometry.pdf) |
| ST | J. Stix, *On cuspidal sections of algebraic fundamental groups*, author version 2 August 2012, Definitions 26/29 and Theorem 30. | [PDF](https://www.math.uni-frankfurt.de/~stix/research/preprints/STIXcuspsec20120802homepage.pdf) |
| PAL | A. Pál, *The real section conjecture and Smith's fixed-point theorem for pro-spaces*, Theorem 1.3; checked arXiv v2 (2009), published 2011. | [PDF](https://arxiv.org/pdf/0905.1205v2) |
| DM | P. Deligne and J. S. Milne, *Tannakian Categories*, author revision 2012 of the 1982 article, Proposition 2.23, Theorem 4.17, Definition 5.1. | [PDF](https://www.jmilne.org/math/xnotes/tc.pdf) |
| J92 | U. Jannsen, *Motives, numerical equivalence, and semi-simplicity* (1992), Theorem 1, Corollaries 1–2. | [PDF](https://epub.uni-regensburg.de/26642/1/jannsen10.pdf) |
| CG | U. Choudhury and M. Gallauer, *An isomorphism of motivic Galois groups*, Theorem 9.1; checked arXiv v3 (18 May 2017). | [PDF](https://arxiv.org/pdf/1410.6104v3) |
| AR | D. Arapura, *An Abelian Category of Motivic Sheaves*, Theorems 6.3.3 and 6.4.1, §7.1; checked arXiv v4 (9 October 2012), published 2013. | [PDF](https://arxiv.org/pdf/0801.0261v4) |
| K25 | B. Kahn, *Galois descent for motivic theories*, Theorem 5.10 and §10; checked arXiv v4 (29 May 2025). Earlier versions have different numbering. | [PDF](https://arxiv.org/pdf/2312.01825v4) |
| GR | A. Grothendieck, *On the de Rham cohomology of algebraic varieties* (1966), p. 102, note 10. | [PDF](https://www.numdam.org/article/PMIHES_1966__29__95_0.pdf) |
| BC | J.-B. Bost and F. Charles, *Some remarks concerning the Grothendieck period conjecture*, §2.2, especially Conjecture 2.12 and Proposition 2.13; checked arXiv v2 (9 April 2014), published 2016. | [PDF](https://arxiv.org/pdf/1307.1045v2) |
| BE | A. Beauville, *The action of SL2 on abelian varieties*, Theorem 3.3; checked arXiv v1 (11 May 2008). | [PDF](https://arxiv.org/pdf/0805.1541v1) |
| MIL25 | J. S. Milne, *Tannakian Categories*, penultimate author version 16 February 2025, Chapter VI §8: Conjectures 8.1 and 8.32, p. 247 definitions A/B, Corollary 8.33. Used to verify modern labels, not their historical assignment. | [PDF](https://www.jmilne.org/math/Books/tcdraft.pdf) |

## Ledger effect

No supplied open problem is solved and no first-pass archival interpretation is promoted to reviewed status. The specific additions are the **current** existing-category witness on 084, the commutative-band obstruction to sl2 and to the full arithmetic Γ_Q quotient, and the unfinished ε/j witness on 086; the established neighboring calculations and comparisons are cited rather than rederived. LM6 A.22 remains Open, LM6 A.50 retains its Proved-return-claim label with its truncated statement caveat, and claims #964 receives no resolution.
