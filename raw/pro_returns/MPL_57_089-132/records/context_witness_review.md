# Context witness review — Fourier and the seven Jacobian theorems

## Evidence boundary and source keys

**Review boundary.** This comparison was made after the parent recorded the transcription freeze at **2026-11-17 17:42:01 UTC**; no scan image was inspected and no transcription, page fragment, doubts file or inventory was edited. The current page files were read as fixed evidence, chiefly 57:89–94, 97 and 99–103, and 126–131, supplemented by searches of the frozen combined text. The earlier transcription and notes are expressly unreviewed claims under CR, and the 271–315 packet is available here through first-pass research notes only. “Checked” below means checked against the supplied textual file, not independently verified against its manuscript image or proved mathematically.

| Key | Exact file | Citation convention / status |
|---|---|---|
| P57 | `MPL_57_089-132/MPL_57_089-132_transcription.tex`; individual files `MPL_57_089-132/pages/MPL_57_089-132_57_scanNNN.tex` | `57:N` means scan N; the 43 scan labels omit 98. Fixed current text. |
| CT | `context/MPL_16+47+54+44_transcription.tex` | Cote:scan, followed by the local statement or paragraph. Supplied earlier transcription, not second-passed. |
| CN | `context/MPL_16+47+54+44_notes.md` | Item ID or cote:scan:note; unreviewed research claims and leads. |
| SC | `context/same_cote_57/MPL_57_271-315_notes.md` | Item ID plus the scan cited by that item; leads only, not a fresh reading of those scans. |
| RS | `context/notes/RESULTS_STATE.md` | Exact register ID and its supplied status. |
| CR | `context/README.md` | Package identity, scope and the mandatory claim/review distinction. |

**Useful file links:** [frozen current text](sandbox:/workspace/scratch/ac8cd1f230c6/MPL_57_089-132/MPL_57_089-132_transcription.tex), [earlier text](sandbox:/workspace/scratch/ac8cd1f230c6/context/MPL_16+47+54+44_transcription.tex), [earlier notes](sandbox:/workspace/scratch/ac8cd1f230c6/context/MPL_16+47+54+44_notes.md), [same-cote leads](sandbox:/workspace/scratch/ac8cd1f230c6/context/same_cote_57/MPL_57_271-315_notes.md), [research register](sandbox:/workspace/scratch/ac8cd1f230c6/context/notes/RESULTS_STATE.md).

## 1. The precise Fourier witness question

### F01 — No completed check of the particular map is identified

**Loci:** CT 47:7, paragraph containing “Nous allons définir un homomorphisme canonique” and displayed map; 47:8, first paragraph; P57 57:91–94; CN F7–F8; RS WG2 §2.4 #4. **Kind:** bounded documentary finding.

CT 47:7 constructs \(\mathbf Rp_*W\to e_*(\mathcal O_S)\otimes\tau_{B^*}[-n]\), and 47:8 explicitly leaves the unit-fibre case with “à faire une vérification de compatibilité.....”. P57 57:91–94 discusses a Picard extension and the class of a canonical line bundle, but does not display this derived direct-image comparison, its unit restriction, or a verification that this particular map is an isomorphism. CN F7 explicitly isolates that map-level task, and F8 compares the exterior-power cohomology without claiming to complete it. Consequently this packet supplies **no identified second witness of cote 47 with that compatibility check done**; the answer is confined to the supplied material.

### F02 — The positive bridge is a duality and extension problem

**Loci:** P57 57:91, morphism \(B\to\underline{\mathrm{Pic}}_{X/S}\), dual torsor and extension diagram; 57:92, opening and final paragraphs; 57:94, four Künneth summands; CT 47:3, definition of \(\Phi_L\); CT 54:3, universal vector extension and tangent sequence. **Kind:** checked textual comparison, with identification limited to the displayed objects.

P57 57:92 says “drais l'interpréter comme l'extension universelle (de Serre) de \(B\) par un fibré vectoriel” and uses the canonical invertible sheaf on \(A\times B\) to express a relative-connection obstruction. This gives a concrete comparison with CT 54:3, where a universal vector extension and its tangent sequence are compared with Hodge–de Rham cohomology, and with the product line bundles used to define CT 47:3's transform. The shared line-bundle and duality setting does not supply CT 47:3–6's convolution/tensor compatibility, composition kernel or inversion argument. It is therefore a useful neighbouring witness, with a closer explicit formulation in cote 54 than in the unfinished Fourier check.

### F03 — Current unfinished tasks and the admitted lemma remain separate

**Loci:** P57 57:91, margin; 57:92, opening; 57:94, paragraph after the Künneth display and cancelled connection paragraph; CT 47:7, Lemma 2; CN F7–F8. **Kind:** self-flagged source claims.

P57 57:91 says “fonctorialité doit être explicitée avec un peu de soin !”, while 57:94 says “Il reste à calculer sa classe dans les derniers” and retains a cancelled “canoniquement??” in the connection discussion. These phrases concern the current construction and must not be presented as a completion of a different compatibility problem. CT 47:7 separately says “Nous allons ici admettre le lemme 2,” the vanishing assertion for a nontrivial algebraically trivial line bundle; neither this admitted lemma nor the specific comparison-map check is proved by the current displayed extension/Künneth discussion.

### F04 — What a completed compatibility check would have to calculate

**Loci:** CT 47:7, definition through the identity on top exterior powers; 47:8, derived restriction at a point of the unit; CN F7–F8. **Kind:** editorial criterion, not a completed proof; confidence high for the criterion, from the displayed map and the local exterior-power calculation.

Over the algebraically closed field reached in CT 47:8, put \(T=\operatorname{Lie}(B^*)\), \(\tau=\det T\) and \(\dim B=n\): the check concerns the actual induced morphism
\[
\mathbf L e^*(\mathbf Rp_*W)\simeq R\Gamma(B,\mathcal O_B)
\longrightarrow \mathbf L e^*e_*\tau[-n].
\]
The degree-\(i\) groups are identified, respectively, with \(\Lambda^iT\) and \(\Lambda^{n-i}T^\vee\otimes\det T\simeq\Lambda^iT\), as the Koszul comparison recorded in CN F8 explains. A completed check must calculate the maps induced by **this** morphism and show that they are isomorphisms for all \(0\le i\le n\), consistently with CT 47:7's identity in degree \(n\); equal dimensions or the existence of abstract exterior-power identifications does not establish this. Neither the present extension-class discussion nor CN F8 supplies that calculation, and no canonical global splitting is being inferred.

## 2. Cote 44, Theorems 1–7

Each item distinguishes the statement in the supplied earlier transcription from the evidence in the present packet; none establishes temporal priority.

### J01 — Theorem 1: no parameter-cycle kernel construction

**Loci:** CT 44:2, Th. 1; P57 57:91 and 126–129, 131; CN 44:2:1; SC J01. **Kind:** bounded negative comparison.

CT 44:2 characterizes \(N(\xi)\subset\operatorname{Alb}(S)\) as, “en substance”, the kernel of the map to its proposed cycle quotient. P57 57:91's dual-torsor construction and 57:126–129, 131's affine representability/descent statements concern relative Picard functors, without defining this parameter-cycle kernel. They provide adjacent foundations, not a second statement of Th. 1.

### J02 — Theorem 2: no all-codimension Betti bound

**Loci:** CT 44:2, Th. 2; 44:8, first paragraph of the Serre letter; P57 57:89 and 91–94; CN D09–D10; SC J02. **Kind:** bounded negative comparison.

CT 44:2 bounds \(\dim\operatorname{Alb}(S)/N(\xi)\), “en fait, par \(\frac12b^{2i-1}(X)\) !”, and 44:8 adds a Tate-module expectation. The present \(H^1\), differentials and extension-class calculations concern Picard/de Rham objects, not a bound for these parameter-family quotients in every codimension. CN D09–D10 discuss later, qualified comparisons, but their bibliographical claims were not independently checked in this review and cannot turn the present material into a witness of Th. 2.

### J03 — Theorem 3: ordinary Picard objects do not construct the general cycle quotient

**Loci:** CT 44:2, Th. 3; 44:8, \(J^1\) and \(J^n\); P57 57:91–94, 101, 126–129 and 131; CN D08, D11; SC J03. **Kind:** positive endpoint comparison with a precise limit.

The present Picard, dual-abelian and representability material has a direct endpoint relationship to CT 44:8's \(J^1=\operatorname{Pic}^0\) and \(J^n=\operatorname{Alb}^0\). It does not construct CT 44:2's quotient of algebraically trivial cycles by the proposed Albanese relation or its complementary-degree duality for general \(i\). Even the complementary exponent in CT 44:2 remains marked `\unsure{n-i|n+1-i}`, so the register's normalized formulation must not silently amend that witness.

### J04 — Theorem 4: Hodge classes are not the required positivity proof

**Loci:** CT 44:2, Th. 4; 44:9, paragraph after the correspondence descends to \(J\); P57 57:94, Künneth decomposition; CN D13; SC J04. **Kind:** bounded negative comparison.

CT 44:2 claims a polarization from the canonical self-duality of \(P^m(X)\), and 44:9 leaves “A prouver que cette dernière est positive !” for its specific correspondence. P57 57:94 calculates the location of a canonical line-bundle class in a Künneth decomposition and leaves its mixed components to calculate; it supplies no positivity assertion for that correspondence. The shared Hodge vocabulary therefore does not resolve Th. 4 or WG H9.

### J05 — Theorem 5: no Néron–Tate/intersection formula

**Loci:** CT 44:4, Th. 5 and fibration margin; P57 57:97 and 99–101; CN D12; SC J05. **Kind:** bounded negative comparison.

CT 44:4 proposes \(\langle\zeta,\zeta'\rangle=(-1)^m Z\mathbin{.}Z'\) for restrictions to a generic member of a pencil and says it should follow from a finer or more general fibration statement. P57's hyperplane and properness arguments do not introduce that pairing, pencil, intersection computation, normalization or sign. They cannot substantiate the Mordell–Weil-lattice interpretation or the claimed reduction to Hodge index in RS WG H9.

### J06 — Theorem 6: a substantial divisor-level comparison, with different qualifications

**Loci:** CT 44:4, Th. 6; P57 57:97, “Critères d'équivalence” table and question; 57:99, theorem and corollaries; 57:100, Picard-kernel paragraph; 57:102–103, descent/Hartogs square; SC J06. **Kind:** positive thematic witness, not an established earlier formulation.

CT Th. 6 distinguishes an isomorphism for \(2i\le n-1\), a fixed-factor image for \(2i=n\), and surjectivity for \(2i\ge n+1\). P57 57:97 is the closest current passage: it compares Pic, Pic\(^{\tau}\), Pic\(^{0}\) and related groups under hyperplane restriction, with dimension thresholds, cohomological hypotheses and characteristic-\(p\) qualifications, and asks for a “Démonstration algébrique ???”. P57 57:99–100 supplies an affine-group \(H^1\) injectivity argument and a qualified Picard-kernel discussion; the broad Picard-injectivity corollary on 99 is cancelled, which must remain visible in any comparison. These are substantial divisor-level links, but they neither state the all-\(i\) programme nor prove its fixed-factor clause, and their assertions should not be silently strengthened to CT Th. 6.

### J07 — Theorem 7: notation involving Picard components is insufficient

**Loci:** CT 44:6, Th. 7; P57 57:97, restriction table; 57:100, Pic\(^{\tau}\) paragraph; CN D14; SC J07. **Kind:** bounded negative comparison.

CT 44:6 states “L'équivalence numérique = \(\tau\)-équivalence” in the broader cycle programme. P57's use of Pic\(^{\tau}\), N, TN and LN in restriction problems is not a statement of numerical versus torsion-algebraic equivalence for arbitrary cycles. SC J07 reports a much more explicit divisor-level comparison at 57:275 and 314–315, but that remains a lead here and still does not establish CT's unrestricted formulation.

### J08 — “Earlier” is not established by subject matter or reused leaves

**Loci:** CT 44:8, dateline and opening; P57 57:93; CR, package description; SC §9 T07 and J07. **Kind:** chronology boundary.

CT 44:8 is explicitly dated “Bures le 12.8.1964” and says “je n'ai pas prouvé grand-chose dessus pour l'instant”; the current 57:93 has only a cancelled, uncertain salutation, not a usable dateline. CR's broad catalogue dates do not establish the relative date of the particular current handwritten arguments and that letter. SC T07 separately warns that October 1957 on reused typescript dates that reused project, not adjacent Picard handwriting, so neither packet establishes an earlier textual form of Th. 1–7.

### Compact per-theorem witness map

| Cote 44 statement | Exact CT locus | Nearest current 57 locus | Relation actually supported | Actual earlier-version witness? |
|---|---|---|---|---|
| Th. 1: \(N(\xi)\) as kernel | 44:2, first displayed map | 57:91; 126–129, 131 | Picard/torsor and representability foundations; no parameter-cycle kernel | Not established; no matching statement or relative dating |
| Th. 2: half-odd-Betti bound | 44:2, Th. 2; compare 44:8, Tate-module paragraph | 57:89, 91–94 | Degree-one cohomological structures; no family-quotient bound | Not established; no matching bound or relative dating |
| Th. 3: general cycle quotient and duality | 44:2, Th. 3; 44:8, endpoint examples | 57:91–94, 101, 126–129, 131 | Ordinary Picard/dual-abelian endpoints; no general \(P^i\) | Not established; endpoint relationship alone is insufficient |
| Th. 4: polarization of self-duality | 44:2, Th. 4; 44:9, final positivity task | 57:94 | Mixed Hodge-class calculation, not positivity of the specified correspondence | Not established |
| Th. 5: height/intersection identity | 44:4, Th. 5 and fibration margin | 57:97, 99–101 | Hyperplane geometry only; no height or intersection formula | Not established |
| Th. 6: three hyperplane ranges and fixed factor | 44:4, Th. 6, after the fibration margin | **57:97–100**; methodological continuation 102–103 | **Strong divisor/Picard restriction parallel**, with characteristic and cohomological qualifications; no general fixed-factor clause | **No established earlier form**; scan order gives no chronology |
| Th. 7: numerical versus \(\tau\)-equivalence | 44:6, sole theorem | 57:97 and 100 | Pic\(^{\tau}\) restriction notation only; SC J07's 275, 314–315 is a separate stronger lead | Not established; no current general-cycle equivalence statement |

## 3. Map to the first-pass 271–315 notes

All entries in this table describe what **SC reports**, with no independent verification of its cited scans in this review.

| SC item / reported locus | Link to the current packet and exact limit |
|---|---|
| F01, 57:294, 297, 310 | The first-order Picard diagrams are adjacent to the extension and connection questions at current 57:91–94; SC quotes “Compatibilité aux spécialisations ???” at 310 and expressly distinguishes it from CT 47:8's map check. |
| F02, 57:283–288 | SC does not find a proof of the admitted vanishing lemma; the same separation of lemma and map-check applies to current F03. |
| F03 and I04, 57:283–286 / 284–288 | Pointed product line bundles, duals and “par transport de structure” are closer comparators to CT 47:3 and 47:11's equivariance than the current extension-class computation, but SC does not claim the missing unit compatibility. |
| D07, 57:287–288 and 294 | The extension-duality lead connects current 57:91–94 with CT 54:3; SC's warning that duality is weaker than a canonical splitting remains applicable. |
| J01, 57:275–277 and 306 | Divisor quotients and a bounded linear-system question are not the general \(N(\xi)\) construction, just as current 57:126–129, 131's Picard descent is not Th. 1. |
| J02, 57:285, 291–292, 313 | Tangent/Picard dimensions and abstract torsion calculations do not yield the half-odd-Betti bound, matching the present J02 boundary. |
| J03, 57:276–277, 283–286, 313 | SC identifies ordinary Picard/Albanese endpoints and warns that Pic/Pic\(^{\tau}\) is not the cycle quotient; current J03 adds concrete representability/descent arguments at that ordinary Picard level. |
| J04, 57:280–281 | The reported “cône convexe” of ample classes is an additional positivity lead, but neither it nor current 57:94 proves positivity of CT 44:9's particular correspondence. |
| J05, 57:289–290, 314–315 | Néron–Severi divisibility and specialization are distinct from a Néron–Tate height formula; both packets leave Th. 5 and WG H9 unsupported. |
| J06, 57:309(h) | The questions “bijectif ?” and “conditions à préciser” have a direct comparator in current 57:97–100's more articulated restriction calculations, without establishing priority or an identity of hypotheses. |
| J07, 57:275 and 314–315 | SC quotes “numériquement équivalent à 0” beside “un multiple d'icelle peut se déformer dans 0”; that is a more explicit divisor-equivalence lead than anything identified here, but not a general-cycle theorem. |
| G02–G03, §§10; T07, §9 | SC itself gives bounded negative witness answers and preserves the unchecked register statuses and chronology boundary, consistent with the present comparison. |

## 4. Exact register mapping

| Register entry | Supplied status | Effect of this review |
|---|---|---|
| **WG2 §2.4 #4** | Question or plan item, round 2, unchecked | The demanded completed Fourier witness is not identified; current 57:97–100 gives a strong divisor/hyperplane comparator, but no earlier seven-theorem witness is established. |
| **WG2 §2.3 #12** | Question or plan item, round 2, unchecked | Current material reaches ordinary Picard endpoints and hyperplane restriction; it adds no general cycle representative, all-degree Betti bound, polarization proof or height identity. |
| **WG H9** | Hunch, “Believe”, unchecked | No pencil/height/intersection calculation or Hodge-index reduction appears in the inspected current arguments; leave this status unchanged. |
| **WG2 §1.1 #3** | Question or plan item, round 2, unchecked | The extension, duality and Picard descent links support the broad Book II neighbourhood only, not a proof or chronological identification. |

## 5. Search record and disambiguated hits

Searches were case-insensitive against the frozen combined P57 TeX and against the supplied context text files; counts below are **matching lines**, not mathematical occurrences. They supplement the local reading and cannot prove absence of an equivalent formulation with different vocabulary. Raw TeX, cancellations, reused leaves and diagram commands remain part of the searchable text.

| Search in P57 | Result and interpretation |
|---|---|
| `Fourier|convolut|Pontryagin` | 0 matching lines. |
| `jacob` | 0 matching lines. |
| `\b(?:hauteur|N[ée]ron|Tate|Betti)\b` | 0 matching lines; an initial unbounded `Tate` search caught English “stated” and French “constate”, so those false hits were discarded. |
| `polaris|num[ée]riqu|[ée]quivalence.{0,30}tau|tau.{0,30}[ée]quivalence` | 0 matching lines; this does not redefine Pic\(^{\tau}\) or establish the meaning of the source's abbreviations. |
| `hyperplan` | 3 matching lines: 57:97's setup, 99's generic section, 100's finite immersion into Picards of normal sections. |
| `compatib` | 3 matching lines: 57:119 canonical descent data, 131 fpqc base change, 132 differential operators; none is the Fourier comparison map. |
| `transform` | 3 matching lines at 57:90 and 95, all monoidal transforms in reused English analytic/typescript material; not an integral-transform functor. |
| `Poincar|Weil|Serre|extension universelle` | 3 matching lines: 57:92's Serre extension, 117's Weil descent criterion, 119's Serre/Nagata descent example; the latter two are unrelated namesake hits. |
| `cycle` | 5 matching lines: divisor/1-cycle arguments at 105, 111–113 and one TikZ `--cycle` command at 118; these do not define the higher cycle quotient in CT 44. |
| `Th[ée]or[èe]me\s*[1-7]|Th\.\s*[1-7]` | 3 matching lines at 57:119, referring to descent theorems; raw TeX markup limits this literal-number search. |

| Context search / checked return | Result used in the notes |
|---|---|
| `compatibilité`, `admettre`, `F7`, `F8` in CT/CN | CT 47:7–8 supplies the admitted lemma and explicit unfinished map check; CN F7–F8 explicitly preserve the distinction between a proof plan/cohomology calculation and the actual map. |
| `universelle`, `Hodge`, `tangent` in CT | CT 54:3 supplies the closest explicit extension/tangent comparator to P57 57:91–94. |
| `Th. 1` through `Th. 7`, `Néron`, `Lefschetz`, `positive`, `12.8.1964` in CT | CT 44:2 contains Th. 1–4, 44:4 Th. 5–6, 44:6 Th. 7, and 44:8–9 the dated letter and remaining positivity question. |
| `D08` through `D14` in CN | Unreviewed scope cautions and later-literature leads; no external bibliographical claim was promoted to checked evidence. |
| `F01`–`F03`, `J01`–`J07`, `D07`, `I04`, `G02`–`G03`, `T07` in SC | Mapped above as first-pass leads, including the distinct specialization-compatibility question and the explicit divisor-equivalence wording. |
| `WG H9`, `WG2 §2.3 #12`, `WG2 §2.4 #4` in RS | Exact unchecked statuses and questions retained; no register entry or original report was modified. |

**Conclusion limited to the evidence.** The answer to both requested witness questions is negative in the precise documentary sense above, while the positive links are concrete: duality/universal extension at 57:91–94, hyperplane restriction at 57:97–100, and ordinary Picard representability/descent at 57:126–129, 131. No historical priority, mathematical completion of cote 47, general-cycle theorem or resolution of WG H9 is claimed.
