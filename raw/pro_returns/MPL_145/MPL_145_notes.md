# MPL_145 — research notes

Research apparatus to the frozen diplomatic transcription of cote 145, scans 001–038. Prepared 14 November 2026.

## 0. Evidence, locators, and limits

The transcription was completed and visually audited in one sequential stream, its recurring notation reconciled, and its 39 SHA-256 values recorded at **2026-11-14 03:29:17 UTC**, before the contextual ZIP was opened. No contextual reading, mathematical objection, or proposed repair in these notes has been incorporated into that frozen text. All references of the form **145/NNN** identify the supplied scan, not a manuscript folio; **L** in the Γ concordance means a physical line in the corresponding frozen per-page TeX file, while other locations use the manuscript's formula numbers or approximate positions.

Contextual filenames below are relative to the supplied **MPL_145_context.zip**: the checked **LM_140-1_text.tex** through **LM_140-4_text.tex** are primary comparison texts; the neighbouring packages' notes are first-pass research leads, not substitutes for their missing images or transcriptions. In particular, cote 149's original ending is not supplied here, so a physical or verbatim join with it cannot be established from this material. Quotations preserve the frozen readings and explicitly retain significant uncertainty; quotation of a contextual note reports that note's reading rather than a new visual verification of the absent manuscript.

**notes/RESULTS_STATE.md**, built 14 November 2026 at 02:03 UTC, was read before these notes were written. Its “Proved,” “Refuted,” and “Known” labels normally report a research run's claim; the CYCLOTOMIC_KERNEL run is expressly marked reviewed, the specified LM8 entries carry intake verdicts, and LM7_PUSH D.44, D.50, E.58, and E.61–E.67 are expressly under referee check. No register status is changed here, and the bounded independent calculations in §5 are not offered as new literature results or as proofs of the broader open programmes.

Each labelled research item has a kind, a source location, a contextual comparison, and relevant register IDs; its explanatory body has one to four sentences. The Γ tables are a token concordance, and the pagination table is documentary metadata. Uncertainty macros quoted from the diplomatic text appear as literal code so that their alternatives remain visible; they are not executable mathematical notation in this Markdown file.

## 1. Answers to the five specified questions

### Q1 — Five-point equation and date

**Kind:** reading question. **Source:** 145/005–012, 024–026, 033–038, especially “\(\hat\pi=\hat\pi_{0,3}\)” and the final return to outer commutation. **Context:** LM_140-3_text.tex, §41, scans 058 and 075–080; §42, scans 086–087; MPL_142_094-122_notes.md, R25 on scan 100, is an uncertain first-pass lead. **Register:** LM1 D.7; LM2 E.3; LM8 B.28; MPL_144_062-121 Q1.

**No explicit equation identified with \(M_{0,5}\), a pentagon, or an order-five compatibility condition has been found in this packet**: its equations concern three peripheral loops, involutions, cyclic order-three symmetry, and decorated automorphisms. The label “[C]” at 145/005 is strongly connected with LM_140-3/058, which expressly resumes calculations in [C], and with the further references at 086–087, establishing a relative drafting relationship rather than a date for every surviving annotation. The official catalogue assigns cote 145 to spring 1981, describes the manuscripts as undated, and attributes the folder title to Jean Malgoire; **[149] is the catalogue footnote number, not a cross-reference to cote 149** (Université de Montpellier, n.d., cote 145 and note 149). Consequently the defensible dating is “catalogued as spring 1981; no autograph date for an explicit five-point equation established,” and the separate modern pentagon comparison in L01 must not be read back into the source.

### Q2 — Which Γ occurs?

**Kind:** reading question / notation concordance. **Source:** all 38 scans; explicit redefinitions at 145/007, 011, 023–024, 027, and 035. **Context:** LM_140-2_text.tex, scans 104–106, 295–306, and 340–342; LM_140-3_text.tex, scans 058 and 085–089. **Register:** WG2 §1.8 #5; LM1 D.7; LM4 D.12.

There are **78 literal Γ tokens**, including cancelled occurrences and one Γ offered only as an alternative to π; §2 identifies each occurrence and also records the pages without a Γ token. The principal meanings are the finite extended geometric group \(\Gamma_{0,3}\simeq S_3\times C_2\), the \(S_3\)-centralizer in the full peripheral outer automorphism group of \(\widehat\pi_{0,3}\), that full group itself when double-hatted, and extensions or stabilizers of the finite group. Scan 004 uses an unspecified operator group in a cancelled descent draft, and scan 026 has a genuine unresolved transition between the centralizer notation and the finite geometric notation. After matching the \(S_3\) embedding and conventions, LM_140-2/342 explicitly identifies the centralizer with the formally defined arithmetic normalizer quotient \(N_\Sigma/\Sigma\) for \(\Sigma\simeq S_3\); this does not identify it with \(G_{\mathbb Q}\), the specific arithmetic image used in §32, or a modern pentagon-defined GT group.

### Q3 — Filling and §32(f)

**Kind:** reading question. **Source:** 145/004, “compatible avec \(\varphi\),” and 025–026, “noyau de” / “groupe produit.” **Context:** LM_140-2_text.tex, §17, scans 185–189; §29, scans 367–369; §32, scans 395–399; LM_140-3_text.tex, scans 676–677. **Register:** IMPL P3; LM1 D.7; LM1 B.18; FLAGGED_149 A9.

**No explicit return to filling from type \((0,4)\) to \((0,3)\), or to §32(f), is identifiable here**: the cancelled map \(\varphi:\pi\to\pi'\) on scan 004 has no specified surface types or distinguished filled puncture. Scan 025 genuinely displays an enlarged kernel \(\widehat\pi\times\widehat{\mathbb Z}^{3}\), but for forgetting the three peripheral rectifiers and passing to outer automorphisms at fixed type \((0,3)\). In LM_140-2/397, surjectivity of the arithmetic quotient map follows from the two surjective arithmetic representations, whereas 398–399 explicitly contemplate failure of (f) and retain the desired exactness hypothetically; 367 separately questions both injectivity and surjectivity for the full double-hatted map. These pages therefore do not verify the earlier run's claimed filling theorem, whose precise statement and proof are not included in the supplied register extract; §4 separates the relevant maps.

### Q4 — Continuation of cote 149 §4

**Kind:** reading question. **Source:** 145/002, cancelled opening, “bien `\unsure{distinguer}` \(\bar D_{J,\alpha}\) de \(\bar D_J\),” and its six-object diagram. **Context:** MPL_149_091-136_notes.md, 135.1–135.2 and 136.3–136.4 on scans 135–136; MPL_147_048-137_notes.md, discussion of scans 121–133. **Register:** WG2 §1.4 #3; WG2 §1.1 #6; FLAGGED_149 E4; EXIT_ONE_TYPE P4e.

**There is a concrete candidate related or continuation fragment, but a continuation after manuscript p. 67 is not established.** The cancelled distinction between component-indexed and unindexed \(\bar D_J\), followed by the \((J',\alpha')\to(J,\alpha)\to U\) cover diagram, fits the component corrections, cover choices, and cancelled final incidence paragraph reported in the first-pass notes on cote 149's ending. The packet supplies no sustained “tubulure” or “maquette” discussion, no continuation of equations (37)–(40), and no resolution of the torus-kernel or \(\pi_2\) issue after that fragment; the main dossier beginning on 005 instead concerns the three-puncture loop group. A comparison with the actual images and cancellation layers of 149/135–136 is required to distinguish continuation from repetition or reworking, and the folder-level date cannot settle that question.

### Q5 — The intersection-multiplicity inertia calculation

**Kind:** reading question. **Source:** 145/003, “\(g'_1=g_1l_1^\mu\),” 012–020, “\(\varepsilon_i^2=l_i\),” and 024, “\(L_0=\hat\kappa_0(\hat{\mathbb Z})\).” **Context:** MPL_149_001-090_notes.md, D19–D23 on scans 077–079; LM_140-2_text.tex, scans 033, 045, and 075–077. **Register:** WG2 §1.4 #3; CYCLOTOMIC_KERNEL C1/C8; FLAGGED_149 ZCF6.

**No written-out computation of collision inertia as \(\mu\kappa_i\), with \(\mu\) an intersection multiplicity, has been found here.** The μ on scan 003 parametrizes a change of conjugator, the κ on 024 identifies a peripheral subgroup, and the quadratic ramification lifts on 012–020 are a different calculation. The supplied cote 149 notes report that the desired multiplicity formula is presumed on 078 and admitted on 079, while LM's checked text states ramification-degree compatibility and constructs root towers without supplying this packet with the missing global comparison. The reviewed, bounded statements registered as CYCLOTOMIC_KERNEL C1/C8 should be cited within their existing scope; this negative documentary finding neither re-proves them nor resolves the remaining existence statements.

## 2. Complete Γ concordance

### 2.1. Meanings and contextual controls

The letters in the first column are **editorial keys used only in these notes**, not additions to the manuscript. “Pure” below means inducing the identity on the three peripheral classes, and does not mean multiplier \(1\); \(C_2=\{\pm1\}\) in the finite geometric group.

| Key | Page-local meaning | Contextual comparison and register bearing |
|---|---|---|
| O | Unspecified group of operators on \(\pi,\pi'\) in the wholly cancelled scan 004; \(\Gamma_i\) is a subgroup/restriction notation whose exact stabilizer interpretation is not supplied. | LM_140-2_text.tex, 104–106, explicitly constructs mixed classifying topoi from an outer operator action; FLAGGED_149 A9, return claim, supplies the centreless-extension comparison. No type \((g,\nu)\) or discrete/profinite convention can safely be assigned from this leaf alone. |
| G | Finite extended geometric \(\Gamma_{0,3}=S_3\times C_2\), including complex conjugation; its profinite completion is itself. | LM_140-3_text.tex, 085–089, uses the corresponding finite \(T_{0,3}\); WG2 §1.8 #5 and LM4 D.12. This is neither the pure orientation-preserving group nor an arithmetic quotient. |
| C | Centralizer of the positive \(S_3\) outer action in \(\operatorname{Out}_{\rm lac}(\widehat\pi_{0,3})\), explicitly called Γ on 011 and 024. | LM_140-3_text.tex, 058–080, resumes precisely the commuting-automorphism problem; LM_140-2_text.tex, 342, identifies this centralizer with \(N_\Sigma/\Sigma\) for the matched \(\Sigma=S_3\). LM1 D.7 and LM2 E.3 remain open; equality with the full pure subgroup is a question on 024. |
| A | Double-hatted \(\widehat{\widehat\Gamma}=\operatorname{Autext}_{\rm lac}(\widehat\pi_{0,3})\), the full continuous peripheral outer automorphism group in the manuscript's convention. | LM_140-3_text.tex, 035 and 058–075, distinguishes the full ambient group from geometric and arithmetic subgroups; LM1 D.7. A double hat here is not a second completion of the finite G. |
| A! | The subgroup of A acting trivially on the set of peripheral classes; the exponent is an exclamation mark. | LM_140-2_text.tex, 296 and 301, defines the identity-on-\(I\) convention; LM_140-3_text.tex, 058–075, compares its centralizer; WG2 §1.8 #5 and LM1 D.7. The question \(C=A!\) remains a source question on 024. |
| SG | \(S\Gamma=S\Gamma_{0,3}\), extension of G by the integral lattice \(\mathbb Z^{\{0,1,\infty\}}\), recording the local peripheral framing choices. | LM_140-2_text.tex, 295–306, especially the pullback square at 300; LM_140-4_text.tex, 277; LM1 B.18. This is a fixed-type extension, not a change to four punctures. |
| GP | The intended signed stabilizer of \(P=-\bar j\), \(\{(\sigma,\operatorname{sgn}\sigma):\sigma\in S_3\}\), of order six; written \(\Gamma_P^*,\Gamma^*,\Gamma_P\). | LM_140-3_text.tex, 085–087, equations (13)–(21); WG2 §1.8 #5 and LM1 B.18. The star has this local notation role, not a units-group meaning; the erroneous factor-order characterization on 036 is examined in A02. |
| GP~ | A chosen lifted image of GP in \(S\mathcal E\), written \(\tilde\Gamma_P\). | Same comparison as GP; 145/035 supplies explicit tuples. Its intended meaning is clear even though 036's equation (13) requires the separate qualification in A02. |
| Gx | Stabilizer in G of an interior point \(2,-1,\tfrac12\), or of its primed label \(0',1',\infty'\); these are Klein four groups. | LM_140-3_text.tex, 085 and 088–089, gives the fixed-point/stabilizer geometry; LM4 D.12 and WG2 §1.8 #5. Scan 028's subscript 2 after mention of \(\tfrac12\) is preserved as written. |
| G0+ | Positive stabilizer of the puncture 0, the order-two subgroup generated by \(\dot\sigma_0\), used in the local peripheral extension on 037. | LM_140-2_text.tex, 305–306, pushes the framing extension along the chosen local factor; LM1 B.18. This is distinct from G, the full Klein four stabilizer, and the interior point \(0'=2\). |
| G? | Probably G in the margin of 026, but the transition is not explicitly declared on that page. | The preceding definition at 024 is C, whereas the integral lattice, geometric \(\mathcal E\), and lifts in the margin anticipate the explicit G of 027 and SG of 032; WG2 §1.8 #5. This is a contextual inference of medium confidence, not a resolved ink reading. |
| ? | Cancelled provisional Γ without enough syntax to assign a group. | 145/028 before the primed point labels; the neighbouring Gx entries provide context but cannot restore an abandoned expression; WG2 §1.8 #5. |

### 2.2. Every literal token

The ordinal restarts on each scan and follows TeX token order; where a stacked equality is encoded with an underset, that order can differ from left-to-right visual order. The table includes every literal command Γ, not merely every distinct formula; an uncertain alternative is counted once and identified as such. Each key carries the exact comparison and register qualifications in §2.1.

| Token | Scan / TeX line | Written occurrence | Meaning | Local qualification |
|---|---|---|---|---|
| G004.01 | 004 / L3 | `\pi,\Gamma` | O | Cancelled; operator pair. |
| G004.02 | 004 / L3 | `D_{\pi,\Gamma}` | O | Cancelled. |
| G004.03 | 004 / L3 | `\widetilde B_{\unsure{\pi\|\Gamma}}` | O | Cancelled; Γ is only the alternative reading. |
| G004.04 | 004 / L4 | `\pi',\Gamma` | O | Cancelled; operator pair. |
| G004.05 | 004 / L4 | `B_{\pi',\Gamma}` | O | Cancelled. |
| G004.06 | 004 / L5 | `B_\Gamma` | O | Cancelled. |
| G004.07 | 004 / L5 | `\widetilde B_{\unsure{\Gamma}}` | O | Cancelled; doubtful letter. |
| G004.08 | 004 / L8 | `D_{\pi,\Gamma}` | O | Cancelled. |
| G004.09 | 004 / L8 | `D_{\pi,\Gamma_i}` | O | Cancelled; restriction to Γ_i. |
| G004.10 | 004 / L9 | `B_{\pi',\Gamma}` | O | Cancelled. |
| G004.11 | 004 / L9 | `B_{\pi',\Gamma_i}` | O | Cancelled; restriction to Γ_i. |
| G004.12 | 004 / L10 | `B_\Gamma` | O | Cancelled. |
| G004.13 | 004 / L10 | `B_{\Gamma_i}` | O | Cancelled; restriction to Γ_i. |
| G004.14 | 004 / L10 | `\widetilde B_\Gamma` | O | Cancelled. |
| G004.15 | 004 / L13 | `compatible avec \Gamma` | O | Cancelled prose. |
| G004.16 | 004 / L15 | `compatible avec \Gamma` | O | Cancelled prose. |
| G006.01 | 006 / L35 | `\Gamma_{0,3}` | G | Includes complex conjugation. |
| G007.01 | 007 / L11 | `\Gamma_{0,3}` | G | Explicit S3 × {±1}. |
| G011.01 | 011 / L13 | `\Gamma` | C | Definition as commuting outer automorphisms. |
| G011.02 | 011 / L21 | `\Gamma` | C | Domain of (γ,χ). |
| G016.01 | 016 / L19 | `\Gamma` | G | Underbrace S3 × Z/2. |
| G017.01 | 017 / L3 | `\gamma\in\Gamma` | G | Mixed fundamental-group pair. |
| G017.02 | 017 / L13 | `1\in\Gamma` | G | Peripheral loops above identity. |
| G021.01 | 021 / L22 | `\varphi(\widetilde S_3)\subset\Gamma` | G | Ambient finite group. |
| G022.01 | 022 / L15 | `\Gamma` | G | Stabilizer in ambient Γ. |
| G022.02 | 022 / L15 | `\Gamma_{0,3}` | G | Explicit equality. |
| G022.03 | 022 / L17 | `\in\Gamma` | G | Signed pair belongs to ambient group. |
| G022.04 | 022 / L22 | `\Gamma` | G | Codomain of φ. |
| G023.01 | 023 / L16 | `\hat\Gamma_{0,3}` | G | Completion of finite group. |
| G023.02 | 023 / L16 | `\Gamma_{0,3}` | G | Equal to preceding completion. |
| G023.03 | 023 / L16 | `\widehat{\widehat\Gamma}` | A | Full peripheral outer group, explicitly defined. |
| G023.04 | 023 / L20 | `\widehat{\widehat\Gamma}` | A | Quotient in extension (18). |
| G024.01 | 024 / L2 | `\Gamma` | C | Defined as commutant of S3. |
| G024.02 | 024 / L2 | `\widehat{\widehat\Gamma}` | A | Ambient group of commutant. |
| G024.03 | 024 / L2 | `\Gamma` | C | Quotient of the corresponding extension E. |
| G024.04 | 024 / L5 | `\Gamma\cap` | C | First intersection. |
| G024.05 | 024 / L5 | `\Gamma_{\unsure{0,3}}` | G | Finite group in first intersection; subscript doubtful. |
| G024.06 | 024 / L6 | `\Gamma\cap S_3` | C | Second intersection. |
| G024.07 | 024 / L13 | `\widehat{\widehat\Gamma}^{!}` | A! | Upper term of marginal diagram. |
| G024.08 | 024 / L14 | `\widehat{\widehat\Gamma}` | A | Lower left of marginal diagram. |
| G024.09 | 024 / L14 | `S_3\times\Gamma` | C | Right term of marginal inclusion. |
| G024.10 | 024 / L17 | `\Gamma\subset` | C | Equality explicitly unknown. |
| G024.11 | 024 / L17 | `\widehat{\widehat\Gamma}^{!}` | A! | Target of that inclusion. |
| G026.01 | 026 / L11 | `\Gamma` | G? | Margin; geometric interpretation probable, not locally redefined. |
| G027.01 | 027 / L3 | `\Gamma` | G | Explicit new finite definition. |
| G027.02 | 027 / L3 | `\Gamma_{0,3}` | G | S3 × Z/2. |
| G027.03 | 027 / L9 | `élément de \Gamma` | G | Element carrying P to its conjugate. |
| G028.01 | 028 / L8 | `\Gamma_{-1}` | Gx | Interior stabilizer at −1. |
| G028.02 | 028 / L8 | `\subset\Gamma` | G | Ambient finite group. |
| G028.03 | 028 / L8 | `\Gamma_2` | Gx | Written subscript 2 follows prose about 1/2; unresolved mismatch. |
| G028.04 | 028 / L8 | `\subset\Gamma` | G | Ambient finite group. |
| G028.05 | 028 / L10 | `\deleted{\unsure{\Gamma}}` | ? | Cancelled isolated letter before 2=0′. |
| G028.06 | 028 / L12 | `\Gamma_{0'}` | Gx | Interior point 0′=2. |
| G028.07 | 028 / L12 | `\Gamma_{1'}` | Gx | Interior point 1′=−1. |
| G028.08 | 028 / L12 | `\Gamma_{\infty'}` | Gx | Interior point ∞′=1/2. |
| G029.01 | 029 / L13 | `\Gamma` | G | Explicit S3 × Z/2 in presentation programme. |
| G032.01 | 032 / L2 | `S\Gamma` | SG | Extension being requested. |
| G032.02 | 032 / L2 | `S\Gamma_{0,3}` | SG | Same extension, with type. |
| G032.03 | 032 / L2 | `de \Gamma` | G | Base of the lattice extension. |
| G032.04 | 032 / L2 | `S\Gamma` | SG | First factor of fibre product. |
| G032.05 | 032 / L2 | `\times_\Gamma` | G | Base of fibre product. |
| G035.01 | 035 / L4 | `\hat\Gamma` | G | Underset equality; finite completion. |
| G035.02 | 035 / L4 | `\Gamma` | G | Main-line finite S3 × Z/2. |
| G035.03 | 035 / L4 | `\widehat{\widehat\Gamma}` | A | Ambient peripheral outer group. |
| G035.04 | 035 / L6 | `\Gamma_P^*` | GP | Explicit signed graph. |
| G035.05 | 035 / L6 | `stabilité de 0 dans \Gamma` | G | Ambient G; literal point label 0, compare 0′=2 on028. |
| G035.06 | 035 / L8 | `\Gamma_P^*` | GP | Domain of section (11). |
| G035.07 | 035 / L10 | `sur \Gamma` | G | Base of partial section. |
| G035.08 | 035 / L10 | `\Gamma^*` | GP | Contextually same signed subgroup; P omitted in source. |
| G036.01 | 036 / L6 | `\simeq\Gamma` | G | Ambient finite product; sentence and (13) need A02 qualification. |
| G036.02 | 036 / L6 | `\Gamma_P` | GP | Intended signed graph, not justified by printed (13). |
| G036.03 | 036 / L6 | `\tilde\Gamma_P` | GP~ | Lifted image intended by (12) on035. |
| G036.04 | 036 / L8 | `\sigma\in\Gamma_P` | GP | Signed symmetry used in proposed reduction. |
| G037.01 | 037 / L3 | `de \Gamma` | G | Ambient group with Klein-four Sylow subgroups. |
| G037.02 | 037 / L3 | `\Gamma_0^+` | G0+ | Positive cusp stabilizer in local extension. |
| G037.03 | 037 / L3 | `\Gamma_0^+` | G0+ | Same cyclic group generated by dotσ0. |
| G037.04 | 037 / L5 | `S\Gamma` | SG | Presentation explicitly left aside. |
| G038.01 | 038 / L20 | `\widehat{\widehat\Gamma}` | A | Final return to outer commutation. |

### 2.3. Pages without a literal Γ

Scans **001, 002, 003, 005, 008, 009, 010, 012, 013, 014, 015, 018, 019, 020, 025, 030, 031, 033, and 034** contain no literal Γ token. Scan 001 is the printed cover; 002 concerns commensurations; 003 is already a profinite three-loop calculation; 005, 008–010, and the opening of 012 belong to the centralizer investigation; 012–015 and 018–020 develop mixed extensions; 025 concerns the full pure decorated profinite group; 030–031 concern the finite geometric quotient and its mixed extension; 033–034 concern the full decorated profinite group. This scope map is inferred from the explicit adjacent definitions and the same contextual anchors in §2.1; it does not insert a Γ into any of these pages.

## 3. Page-indexed research observations

### N01 — Component labels do not supply the missing stratum extension

**Kind:** unpursued implication. **Source:** 145/002, cancelled opening and diagram, “\(\bar D_{J,\alpha}\)” versus “\(\bar D_J\).” **Context:** MPL_149_091-136_notes.md, 135.1–135.2 and 136.4; MPL_147_048-137_notes.md, scans 121–133. **Register:** FLAGGED_149 E4; EXIT_ONE_TYPE P4e/P1d1; WG2 §1.1 #6.

The component index α is precisely the sort of bookkeeping required when a stratum is disconnected, making the cancelled fragment more specific than a general thematic resemblance to cote 149. The earlier notes distinguish this correction from injectivity of a torus kernel and from coherent incidence maps, neither of which is supplied by the small diagram here. Thus the packet adds a candidate piece of the component indexing, not a proof of the registered stratum-extension criterion or a reconstruction of the maquette's missing topology.

### N02 — Realized commensurations and a coset set

**Kind:** unpursued implication / reading question. **Source:** 145/002, lower half, “germes” and “\(H/\pi\) (classes à droite).” **Context:** LM_140-4_text.tex, scans 190–192 and 203–205; MPL_149_001-090_notes.md, C062.3 on scan 062. **Register:** WG2 §1.8 #5; LM8 A.12.

The definition restricts to finite-index isomorphisms realized by an element of the specified ambient transformation group G and a map \(D/\pi'\simeq D/\pi''\), so it does not identify H with the unrestricted abstract commensurator. Likewise the source calls \(H/\pi\) a set of right classes rather than proving that π is normal and the quotient is a group. LM's “germe de discrétification” construction likewise depends on an ambient group and chosen discrete data, making this a useful warning against replacing geometric realization with abstract peripheral compatibility in the open realization problem.

### N03 — Faithfulness of cover isomorphisms is not restated

**Kind:** unproved claim. **Source:** 145/002, middle NB, “\(v\) est connu quand on connaît \(v_*\).” **Context:** LM_140-2_text.tex, scans 104–105; MPL_149_001-090_notes.md, B028.1 and B029.2. **Register:** FLAGGED_149 A9.

The assertion needs the geometric category and faithfulness assumptions implicit in the fragment, since a group-theoretic isomorphism does not determine an arbitrary map of spaces without such conditions. The checked LM passage proves uniqueness of the conjugating identification under a trivial-centralizer hypothesis, while the cote 149 notes report a related extension-reconstruction argument. These pages add a finite-cover version of that rigidity question but do not enlarge the A9 return claim into an unrestricted reconstruction theorem.

### N04 — The uncertain fixed-index subgroup assertion

**Kind:** reading question / unproved claim. **Source:** 145/002, final two paragraphs, “`\unsure{H_n\|H_1}` est un ss-groupe.” **Context:** LM_140-4_text.tex, scans 190 and 204–205. **Register:** WG2 §1.8 #5; LM8 A.12.

If the first reading \(H_n\) is correct, closure at a prescribed index n requires an argument that does not merely refine to an arbitrary common finite cover. The contextual commensurability constructions allow such refinements and therefore do not by themselves justify this stronger fixed-index claim. A05 gives a bounded lattice diagnostic, while the alternative \(H_1\) and the unfinished last words “et π d'indice” remain documentary uncertainties.

### N05 — The β/γ expectation is not an editorial licence

**Kind:** reading question / self-flagged. **Source:** 145/003, marginal NB beside (2), “On doit en fait avoir `\unsure{\beta=\gamma\|\beta\ne\gamma}`.” **Context:** LM_140-3_text.tex, scan 058, equations (7)–(10bis), and scans 079–080. **Register:** LM1 D.7; WG2 §1.8 #5.

The appeal to abelianization and the later scalar calculations make the equality reading mathematically plausible, but they do not decide the marginal ink after the freeze. The same leaf also has uncertain exponent and sign changes in its final change-of-conjugator formula, so its symbols cannot be identified with LM's normalized parameters without a convention calculation. This records an expectation and a reading question, not a correction of the β/γ sign or a proof of the larger automorphism characterization.

### N06 — The cancelled compatible-automorphism draft

**Kind:** unproved claim in a cancelled draft. **Source:** 145/004, diagrams and lower equations, “compatible avec Γ,” “\(\exists!u'\),” and \(E_\varphi\). **Context:** LM_140-2_text.tex, 104–106; LM_140-3_text.tex, 676–677, equations (91)–(92). **Register:** FLAGGED_149 A9; IMPL P3; INTAKE 20261114 §4.2.

The mixed-topos diagrams have a close primary comparator in LM's construction from an equivariant outer homomorphism with trivial image centralizer. Its later functoriality discussion explains why a specified surjection permits a compatible automorphism of the quotient only when the kernel is preserved. The present leaf is wholly cancelled and leaves \(\varphi\) unspecified, so it adds an abandoned formulation of the descent problem rather than a completed special case of hole filling.

### N07 — Generation is the essential extra condition

**Kind:** unproved claim / self-flagged question. **Source:** 145/005, “sauf erreur”; 009, “Mais comment vérifier … un automorphisme ?” and “`\unsure{Ça}` semble délicat.” **Context:** LM_140-3_text.tex, 075, theorem condition (b), and 211, marginal exclusion of the initial generation condition. **Register:** LM2 B.g11; LM2 F.3; LM1 D.7.

The peripheral product relation constructs an endomorphism, whereas a surjective endomorphism of the finitely generated profinite group is an automorphism, so the unresolved issue is topological generation by the proposed images. LM_140-3/075 preserves a separate generation condition, and the later algebraic discussion on 211 expressly sets that condition aside. Scans 024, 033, and 038 restore it in this packet, so finite-jet, abelianized, or pronilpotent solutions cannot be promoted here to actual full profinite automorphisms.

### N08 — Two different S3 actions explain the apparent lifting reversal

**Kind:** unpursued implication / scope distinction. **Source:** 145/006, “pas de pt fixe,” compared with 021–022, the canonical lift of \(\varphi\). **Context:** LM_140-3_text.tex, 085–089. **Register:** LM4 D.12; LM8 A.12; WG2 §1.8 #5.

The positive \(S_3\) in scan 006 has no common fixed point on the punctured sphere, whereas the later signed graph \(\{(\sigma,\operatorname{sgn}\sigma)\}\) fixes P and has a canonical lift. Their different multipliers and quotient embeddings explain why the later section does not contradict the earlier nonlifting claim. This is a finite geometric example and does not establish realization for arbitrary finite peripheral actions in the full profinite group.

### N09 — Inner defects and the normalized representative

**Kind:** unpursued implication. **Source:** 145/007–008, \(u\rho=\operatorname{int}(g)\rho u\) and \(g\mapsto l_0^\alpha g l_1^{-\alpha}\). **Context:** LM_140-3_text.tex, 058–080, especially 079–080, and 211–212. **Register:** LM1 B.18; LM2 E.3.

Normalizing \(u\) along \(L_0\) leaves a peripheral gauge, and the element g measures the defect of strict commutation rather than an additional independent automorphism. The displayed gauge action is closely paralleled by LM's normalized conjugators and their changes under peripheral multiplication. This provides early coordinates for the later normalized-section programme, with loop order and inverse conventions still required before comparing individual formulas.

### N10 — The pq-to-q substitution remains a reading question

**Kind:** reading question. **Source:** 145/009, \(h=gl_1^{pq}\), followed by \(gl_1^q\sigma_\infty(g)\in L_0\); 010, the ensuing scalar relation. **Context:** LM_140-3_text.tex, 058 and 079–080. **Register:** WG2 §1.8 #5; LM1 B.18.

Since p is a unit, a reparametrization could absorb p into q, but the source does not explicitly announce that substitution between the two displays. The later normalized scalar equations are a useful comparator without proving that an omitted reparametrization, rather than an error, was intended here. Both powers remain in the transcription, and any derived dictionary must state which q it uses.

### N11 — The quotient π/Ẑ is an orbit set

**Kind:** unpursued implication. **Source:** 145/010–012, “ne dépendent que de l'autom ext.” and the injection \((\gamma,\chi)\). **Context:** LM_140-3_text.tex, 079–080, (60), (A)–(C), and 211–212. **Register:** LM1 B.18; LM1 D.7.

The quotient \(\pi/\widehat{\mathbb Z}\) on scan 011 is explicitly formed using the action \(g\mapsto l_0^\alpha g l_1^{-\alpha}\), so it is an orbit set rather than a group quotient by a specified normal subgroup. The claimed injection records the outer automorphism through its gauge class and multiplier, while β is determined from the symmetry equation and is independent of the chosen normalized representative. LM's later gauge formulation restates this coordinate principle, without identifying the resulting centralizer with an arithmetic image.

### N12 — The discrete classification has a stated boundary

**Kind:** unproved claim / scope distinction. **Source:** 145/010–011, “si on travaille sur les groupes discrets” and “une seule autre solution.” **Context:** LM_140-3_text.tex, 085–089; LM_140-2_text.tex, 340–342. **Register:** LM1 D.7; LM4 D.12.

The two outer solutions asserted here are the identity and complex conjugation, with the generation condition and \(p=\pm1\) explicitly retained. This is consistent with centralizing the positive \(S_3\) inside the finite geometric \(S_3\times C_2\), and is not a classification of the full profinite centralizer. The separate arithmetic normalizer quotient in LM must therefore not be substituted for this discrete claim.

### N13 — Quadratic ramification is not intersection multiplicity

**Kind:** unproved claim / unpursued implication. **Source:** 145/012–014 and 019–020, “\(\varepsilon_i^2=l_i\)” and “l'unique … autom.” **Context:** LM_140-3_text.tex, 088; LM_140-2_text.tex, 033, 045, and 075–077. **Register:** CYCLOTOMIC_KERNEL C1/C8; WG2 §1.4 #3.

The proposed lift has square the peripheral generator and represents a local degree-two ramification phenomenon in the symmetry extension. Existence and uniqueness must be read with the selected inertia subgroup and its centralizer, not just with the image transposition in the quotient. The checked LM degree-compatibility and root-tower passages supply context, while the reviewed CYCLOTOMIC_KERNEL statements retain their own scope and do not turn this calculation into the missing arbitrary-contact-order argument.

### N14 — The trial exponent and its cancellations are mathematical evidence

**Kind:** withdrawn in the same text / self-flagged. **Source:** 145/013, “n'est peut-être pas de carré,” the marginal `\alpha=\unsure{2\|1}\ ?`, cancelled “Non !,” and live “OK.” **Context:** LM_140-3_text.tex, 086–088, the later lift conventions. **Register:** WG2 §1.8 #5; LM1 B.18.

The page records an actual trial-and-correction process for choosing a square-root lift, including cancelled algebra rather than a single clean derivation. Its final formulas must be compared with the later reversal of ε on 019 and with LM's expressly changed notation, not treated as stable definitions across the packet. The uncertain trial digit cannot be resolved by selecting whichever exponent makes the subsequent calculation work.

### N15 — The first presentation attempt is explicitly incomplete

**Kind:** self-flagged / unproved claim. **Source:** 145/014, “ces relations ne semblent pas `\unsure{conséquences}` des autres” and “ce qui est inquiétant.” **Context:** LM_140-3_text.tex, 086–088; later 145/018–022. **Register:** LM1 B.18; WG2 §1.8 #5.

The author questions whether the alternative expressions for ρ follow from the earlier relations and then treats the derived involution as a warning. The revisions on 015 and the explicit “C'est faux” on 018 show that the displayed relation lists should not be cited wholesale as verified presentations. LM's later normalization supplies a comparison presentation, but it does not retroactively validate each discarded relation here.

### N16 — A cancelled torsion argument and a live expectation

**Kind:** withdrawn in the same text / conjecture. **Source:** 145/014–015, the cancelled deduction \(\varepsilon_0\varepsilon_1\varepsilon_\infty=1\) and live “Sans doute” before \(\varepsilon_0\varepsilon_1\varepsilon_\infty=\sigma_1\). **Context:** LM_140-3_text.tex, 086–088; 145/017–020. **Register:** LM4 D.12; LM1 B.18.

The torsion-free premise and the chain ending in \(\sigma_\infty\sigma_1\sigma_0=1\) belong to the cancelled block and are not endorsed conclusions of the surviving text. The live replacement is explicitly tentative and is followed by a critique of the discrete/profinite notation and a fresh geometric construction. This is evidence that the author recognized a structural difficulty, not a result about torsion in the full low-type profinite groups of LM4 D.12.

### N17 — The path convention reverses the peripheral product

**Kind:** reading question / explicit convention revision. **Source:** 145/015–017, “Critique des notations,” “composant les chemins comme des fonctions,” and “et non \(l_0l_1l_\infty=1\) !” **Context:** LM_140-3_text.tex, 086–087, equations (13)–(21) and the references to [C]. **Register:** WG2 §1.8 #5; LM1 B.18.

The geometric restart fixes \(l_\infty l_1l_0=1\), whereas 005 began with the ascending product. LM's later comparison expressly acknowledges changed symbols from [C], so the two halves of the packet cannot be merged by a purely typographic replacement of primes or tildes. In particular, scan 036's return to an ascending product is a substantive inconsistency to annotate separately in A02, while the uncertain question mark on 017 remains uncertain.

### N18 — A presentation explicitly marked false

**Kind:** withdrawn in the same text. **Source:** 145/018, margin, “C'est faux,” compared with 020, “Il faut ajouter les relations \(\rho\sigma_0\rho^{-1}=\sigma_1\) etc.” **Context:** LM_140-3_text.tex, 086–087. **Register:** LM1 B.18; WG2 §1.8 #5.

The claimed presentation by (1), (2), and \(\rho^3=1\) is explicitly retracted, using the quotient obtained by setting \(\rho=1\) as a diagnostic. Scan 020 adds the cyclic conjugation relations and simplifies the generators, demonstrating that the earlier list omitted essential compatibility. The contextual presentation is useful for comparison, but the packet's own correction must remain visible as a separate stage.

### N19 — Epsilon is deliberately inverted

**Kind:** reading question / explicit notation revision. **Source:** 145/019, “Les \(\varepsilon_i\) ici sont les \(\varepsilon_i^{-1}\) de tantôt !” and “où il faut compléter.” **Context:** LM_140-3_text.tex, 088; 145/013–014 and 020–022. **Register:** WG2 §1.8 #5; LM1 B.18.

This explicit inversion explains why a global dictionary assigning one fixed ε to the entire packet would be misleading. The products left as dotted expressions are worked out in (9), but the later “au moins!” on 022 continues to qualify completeness of the relation system. LM's local lift description should therefore be matched only after specifying the chosen ε and the peripheral order.

### N20 — A small quotient separates ρ from the reflection generators

**Kind:** unpursued implication. **Source:** 145/020, “ce qui prouve que \(\rho\) n'est pas un mot … aux \(\sigma_i\).” **Context:** LM_140-3_text.tex, 086–087; 145/022, the analogous ε question. **Register:** LM1 B.18.

Setting all \(\sigma_i\) equal to 1 leaves the nontrivial quotient generated by ρ with \(\rho^3=1\), which supplies a concrete obstruction to expressing ρ in those generators alone for the stated presentation. Scan 022 invokes the analogous obstruction for the ε system. This is a useful finite-quotient method inside the geometric presentation problem, without deciding any full profinite lifting or arithmetic-image comparison.

### N21 — The signed section comes with an express notation critique

**Kind:** unproved claim / reading question. **Source:** 145/021–022, “produit \(\frac12\) direct,” “Il faut expliciter,” and the marginal “Critique.” **Context:** LM_140-3_text.tex, 085–087, especially the [C] notation reference on 086. **Register:** WG2 §1.8 #5; LM1 B.18.

The signed \(S_3\) gives a semidirect product with π once its action on the chosen loops is specified, and equation (14) supplies that action. The author then proposes changing the tilde notation and reserving it for lifts to \(S\mathcal E\), so a tilde does not have one unchanging level of meaning even within these two pages. The explicit section is a finite geometric construction, and its later decorated lift on 035 is a separate step.

### N22 — Three lifts of complex conjugation encode real components

**Kind:** unpursued implication / question answered locally. **Source:** 145/022, “trois choix également naturels,” and 028–029, the lifts \(\tau_0,\tau_1,\tau_\infty\). **Context:** LM_140-3_text.tex, 088–089. **Register:** LM4 D.12; LM8 A.12; FLAGGED_149 ZCF6.

The lack of a preferred path from P to its conjugate is later interpreted using the three connected components of the real punctured line. This gives a concrete geometric explanation of the three partial sections, not an arithmetic existence theorem for arbitrary Galois sections. The full profinite finite-action and arithmetic existence problems recorded in the register consequently remain outside this calculation.

### N23 — The triangulated cartographic group

**Kind:** unproved claim / unpursued implication. **Source:** 145/023, “seules relations (16)” and the signature kernel. **Context:** LM_140-3_text.tex, 129–130. **Register:** LM8 G.20; LM4 D.12.

The asserted discrete presentation is \(C_2*C_2*C_2\), with the even-word kernel generated by \(l_0=\tau_\infty\tau_1\), \(l_1=\tau_0\tau_\infty\), and \(l_\infty=\tau_1\tau_0\). LM's later passage returns to the same cartographic group and separately flags a profinite fixed-subgroup assertion for verification. The discrete presentation here therefore does not settle the residual full profinite fixed-subgroup or procyclic-normalizer questions of LM8 G.20.

### N24 — A completed geometric extension is not the full automorphism group

**Kind:** reading question / scope distinction. **Source:** 145/023–024, “le complété profini” versus “le groupe des autom. … à lacets de \(\hat\pi\).” **Context:** LM_140-3_text.tex, 035 and 058–075; LM_140-2_text.tex, 367–369. **Register:** LM1 D.7; IMPL P3.

The single-hatted \(\hat{\mathcal E}\) is a completed geometric extension of the finite G by \(\hat\pi\), whereas the double-hatted group is the full peripheral automorphism group with quotient A. This explicit distinction is the main safeguard against importing a theorem about completed mapping classes into the full peripheral group. It also explains why two visually similar filling or section diagrams may have different kernels and different unresolved hypotheses.

### N25 — The centralizer equality is expressly unknown

**Kind:** conjectural identification / self-flagged. **Source:** 145/024, “j'ignore si cette inclusion est une égalité.” **Context:** LM_140-3_text.tex, 058–080; LM_140-2_text.tex, 340–342. **Register:** LM1 D.7; LM2 E.3; LM8 B.28.

The marginal diagram asks whether the \(S_3\)-centralizer C exhausts the pure subgroup A!, rather than asserting that it does. After matching the \(S_3\) embedding, LM_140-2/342 explicitly identifies \(C=N_\Sigma^!\simeq N_\Sigma/\Sigma=\Gamma_\Sigma\) and \(N_\Sigma=S_3\times C\), providing a formal arithmetic-normalizer interpretation of this centralizer. That source identification does not prove \(C=A!\), identify the formally defined quotient with the specific image of \(G_{\mathbb Q}\), or supply a full pentagon-defined GT characterization.

### N26 — Left/right rectifier ambiguity survives the inverse cancellations

**Kind:** reading question. **Source:** 145/024, (21)–(22), and 025, “multiplication à gauche,” compared with \(g_i\mapsto gg_i\). **Context:** LM_140-2_text.tex, 296–297; LM_140-3_text.tex, 193 and 211–212. **Register:** WG2 §1.8 #5; LM1 B.18.

For the direct convention \(u(l_i)=\operatorname{int}(g_i)l_i^p\), keeping u fixed allows right multiplication of \(g_i\) by the peripheral centralizer, whereas an inverse-conjugator convention changes the side. The visible cancellations of inverse exponents and the retained phrase “à gauche” thus leave a convention mismatch, not permission to replace either reading. LM_140-2/296 itself combines \(\operatorname{int}(g_i^{-1})\) with the words “multiplication à droite,” although that formula requires left multiplication \(g_i\mapsto\lambda_i g_i\), so the contextual text has a further side mismatch rather than a ready-made consistent repair.

### N27 — The opposite-group cocycle has a precise purpose

**Kind:** unpursued implication. **Source:** 145/025, (23)–(24), “opposé au groupe.” **Context:** LM_140-2_text.tex, 296–300; LM_140-3_text.tex, 192–193 and 211–212. **Register:** LM1 B.18.

The composition \(g_i(vu)=v(g_i(u))g_i(v)\) explains why the source changes the coefficient group to the opposite group when describing its three conjugator functions as cocycles. LM's later formulas have the same dependence on evaluation by the acting automorphism, and its discussion of single-valued conjugators likewise motivates an extension. The kernels, number of peripheral factors, and normalizations differ across those passages, so the connection is structural rather than an identification of all the extensions.

### N28 — A marginal shorthand drops the generation condition

**Kind:** reading question / unproved claim. **Source:** 145/025, NB, “Systèmes … satisfaisant la relation (22),” compared with 024, “engendrent … topologiquement.” **Context:** LM_140-3_text.tex, 075 and 211. **Register:** LM2 B.g11; LM2 F.3; LM1 D.7.

The marginal description mentions only the relation, although the main definition on the preceding page also requires the images to generate. It should be read as incomplete shorthand unless an additional argument removes that condition, and no such argument is given here. The same distinction is explicit in LM's theorem and later algebraic simplification, and remains relevant to the register's open passage from finite data to full profinite automorphisms.

### N29 — Covariance is announced before its complete formula

**Kind:** self-flagged / reading question. **Source:** 145/026, “Il faudrait expliciter” and `\gamma_{\unsure{i+1\|i-1}}`; 037, (15). **Context:** LM_140-3_text.tex, 211–212; LM_140-4_text.tex, 277. **Register:** LM1 B.18; WG2 §1.8 #5.

The first covariance formula has an uncertain cyclic index and no clearly written application of ρ to the resulting group element. Scan 037 later gives the explicit tuple transformation \((g_0,g_1,g_\infty)\mapsto(\rho(g_\infty),\rho(g_0),\rho(g_1))\), which is a comparison point rather than a correction to 026. The intervening request for canonical lifted symmetries also explains the transition ambiguity of Γ recorded as G?.

### N30 — Conjugating between the two poles is not π-conjugacy

**Kind:** reading question / unpursued implication. **Source:** 145/027, “\(\pi\)-conjugués … entre eux” and elements carrying P to \(\bar P\). **Context:** LM_140-3_text.tex, 085–089, especially the distinction of pole lifts on 089. **Register:** LM4 D.12; LM8 A.12.

The phrase “entre eux” qualifies the choices of lifts relative to \(\bar P\); the displayed transport from P uses an element of the larger extension lying over a nontrivial quotient symmetry. It therefore does not assert that the sections attached to the two different fixed points are conjugate by π. LM's later distinction of the pole classes makes this a useful check on the subgroup in which conjugacy is being taken.

### N31 — Interior stabilizers and two unresolved point labels

**Kind:** reading question. **Source:** 145/028, “\(\Gamma_{-1}\)” and “\(\Gamma_2\)” after mention of \(\tfrac12\); 035, “stabilité de 0.” **Context:** LM_140-3_text.tex, 085 and 088–089. **Register:** WG2 §1.8 #5; LM1 B.18.

The primed labels are explicitly \(0'=2\), \(1'=-1\), and \(\infty'=\tfrac12\), but the earlier sentence retains the mismatching subscript 2. The section using \(\sigma_0,\tau_0\) was constructed at the interior fixed point \(0'=2\), while 035 says “0” without a prime. These differences must be retained as reading/convention questions, especially because the puncture stabilizer with peripheral normalization on 037 is a genuinely different lifting problem.

### N32 — Fixed loci are used only for the finite geometric action

**Kind:** unpursued implication. **Source:** 145/027–029, “scindages partiels maximaux,” and \(U^{\tau\dot\sigma_1}=\mathbb U-\{1\}\). **Context:** LM_140-3_text.tex, 085–089; MPL_149_001-090_notes.md, C061.3–C063.2. **Register:** LM4 D.12; LM8 A.12; FLAGGED_149 ZCF6.

The fixed points and real components supply a geometric classification strategy for sections over subgroups of \(S_3\times C_2\). The arithmetic section expectations reported in the cote 149 notes involve different groups and additional existence questions. This packet contributes a worked finite model, not a proof that arbitrary full profinite actions or arithmetic sections have the same realization.

### N33 — The full presentation is revised in the margin

**Kind:** self-flagged / withdrawn in the same text. **Source:** 145/029–031, “Il faudrait … gén. et relations,” and 030, “Il faut ajouter les relations.” **Context:** LM_140-3_text.tex, 086–089; 145/018–020. **Register:** LM1 B.18; WG2 §1.8 #5.

The cancelled four-generator start is replaced by a presentation using σ, τ, and ρ, with cyclic conjugation relations added in the margin. Scan 031 reduces the resulting system to \(\rho,\sigma_0,\tau_0\) and the commutator relation. The uncertain marginal assertion about which relations are consequences should not be promoted into a completed redundancy proof merely because the final presentation is concise.

### N34 — An abstract symmetry fails to preserve the extension

**Kind:** unpursued implication / own idea. **Source:** 145/031, “n'est pas compatible avec la structure d'extension” and “elle devrait conserver le centre!” **Context:** LM_140-2_text.tex, 299–300; LM_140-3_text.tex, 086–087. **Register:** FLAGGED_149 A9; LM1 B.18.

The symmetry exchanging \(\sigma_0,\tau_0\) and reversing ρ preserves the stated abstract presentation but cannot preserve the specified quotient map to \(S_3\times C_2\), since it would exchange central and noncentral quotient elements. An ensuing comparison should therefore retain the kernel inclusion, quotient map, and peripheral markings as part of its input, not just the abstract group. **Own inference, confidence high**, because the quotient-centre obstruction is explicit; it illustrates the identified-kernel-and-quotient qualification in the existing A9 return claim rather than strengthening that claim.

### N35 — The integral framing extension is requested and then left aside

**Kind:** self-flagged / unproved construction. **Source:** 145/032, “Il faudrait encore expliciter,” and 037, “je ne vais pas m'y attarder.” **Context:** LM_140-2_text.tex, 295–306; LM_140-4_text.tex, 277, (136)–(140). **Register:** LM1 B.18; IMPL P3.

The source identifies \(S\mathcal E\) as the pullback of an extension \(S\Gamma\to\Gamma\) by \(\mathbb Z^3\), but does not finish the proposed generators-and-relations presentation. LM supplies the general peripheral-framing construction and its local pushouts, adding conceptual interpretation to the request. The missing presentation is not a missing puncture-filling exact sequence, and the local obstruction on 037 does not address §32(f).

### N36 — The marginal kernel conflicts with the displayed projection

**Kind:** reading question / own formal diagnostic. **Source:** 145/033, (4), (6)–(7), and margin “noyau \(i(\hat\pi)\).” **Context:** LM_140-2_text.tex, 297–300; 145/025–026. **Register:** LM1 B.18; IMPL P3.

Equation (7) says that the projection of \(i(g;\alpha_i)\) is \(\operatorname{int}(g)\), so \(i(\hat\pi)\) cannot be its kernel when g is noncentral. The larger outer kernel on 025 and the two different quotients in LM_140-2/300 explain why distinguishing the target matters. A03 gives the direct calculation and its hypotheses; the ambiguous marginal reference remains unchanged.

### N37 — Explicit composition still needs an effective representation of words

**Kind:** limitation stated by the author / own implication. **Source:** 145/033–034, “pas … entièrement explicite et satisfaisante” and “mots (ou limites de tels).” **Context:** LM_140-3_text.tex, 193, (52), and 212, (125). **Register:** LM1 B.18; LM2 B.g11.

The multiplication law uses \(u(g'_i)\), and the conjugation law uses \(u(g)\), so the tuples alone are not a finite symbolic evaluation scheme unless their profinite words are represented effectively. Evaluation in specified finite quotients is available once compatible input words and actions are supplied, but that does not construct the compatible full profinite inputs themselves. **Own inference, confidence high**, because it follows from the displayed substitution dependence; it adds a computational scope qualification to the same cocycle law already present in LM.

### N38 — The identity-rectifier subgroup and its faulty written criterion

**Kind:** unproved claim / reading question. **Source:** 145/035–036, “\(g_0,g_1,g_\infty\) … égaux à 1,” (12), and (13). **Context:** LM_140-3_text.tex, 086, (13), and 087; 145/033, (2). **Register:** LM1 B.18; WG2 §1.8 #5.

The tuple multiplication explains the intended identity-rectifier subgroup, and (12) explicitly provides the signed finite subgroup inside it. The criterion (13), however, reverses the defining peripheral order used on 033 and cannot serve as written even for the identity tuple. A01–A02 prove the separate pure-power exercise and diagnose this order conflict without repairing the text or declaring the full subgroup characterization established by the faulty display.

### N39 — The local obstruction concerns a stronger lift

**Kind:** unproved claim / question answered negatively. **Source:** 145/037, “ils ne se remontent pas” and “qui centralise … \(L_0\).” **Context:** LM_140-2_text.tex, 305–306; MPL_149_001-090_notes.md, D28–D29 on scan 080. **Register:** LM1 B.18; CYCLOTOMIC_KERNEL C1; LM4 D.12.

The obstruction is to lifting the finite stabilizer with the required order and local peripheral normalization in the special extension. The lift at the interior point \(0'=2\) on 028 does not impose that same cusp-normalization condition, so there is no contradiction between the two statements. LM's local pushout of \(T^I\) to the chosen factor T gives the precise comparison, while the reviewed arithmetic cusp statement C1 has a different scope.

### N40 — Strict commutation is abandoned as the final target

**Kind:** self-flagged change of programme / unpursued implication. **Source:** 145/037–038, (17)–(18), “moins intéressant pour la suite,” and “la commutation mod autom. intérieurs.” **Context:** LM_140-3_text.tex, 058–080 and 211–212. **Register:** LM1 D.7; LM2 E.3; LM1 B.18.

The explicit equalities among the rectifiers describe strict commutation of chosen decorated lifts, but the last sentence returns to commutation in the outer quotient. The earlier defect equation \(u\rho=\operatorname{int}(g)\rho u\) on 007 is the appropriate comparator, and replacing it by strict equality would discard admissible outer classes. The final page also retains topological generation, leaving both the quotient bookkeeping and the automorphism condition visible rather than concluding with a complete centralizer classification.

## 4. Filling maps, arithmetic images, and §32(f)

### F01 — Filling while retaining the new base point

**Kind:** reading question / unpursued implication. **Source:** 145/004, the unspecified \(\varphi:\pi\to\pi'\), compared with 025's fixed-type kernel. **Context:** LM_140-2_text.tex, §17, 185–189, and §32, 395–396, “à lacets (pas ext!).” **Register:** IMPL P3; LM1 D.7.

LM's filling construction retains the filled point as a base point and therefore initially targets an automorphism group, not its outer quotient. The point-pushing subgroup maps to inner automorphisms at that stage; it is not the kernel of this Aut-valued map. This target distinction is necessary before interpreting any assertion that the kernel is “larger than point pushing,” and the unlabelled map of 145/004 does not remove it.

### F02 — Full peripheral groups and completed geometric groups

**Kind:** unproved claim comparison. **Source:** 145/023, the single-hat/double-hat distinction; 004, the cancelled compatibility problem. **Context:** LM_140-2_text.tex, §29, 367–369; §27, 340–342. **Register:** IMPL P3; LM1 D.7; LM4 D.12.

LM_140-2/367 explicitly leaves the full double-hatted filling map problematic as to isomorphism, injectivity, and surjectivity, while describing the corresponding map on the single-hatted groups attached to a chosen discretization as an isomorphism. Scan 368 separately asks about the dependence and normality of the embedded point-pushing subgroup. The distinctions established in 145/023 agree with that separation, so surjectivity in the geometric setting is not evidence of surjectivity for every peripheral automorphism.

### F03 — What the argument in §32 actually makes surjective

**Kind:** contextual reading question. **Source:** 145/004 and 024, respectively the descent draft and the separate centralizer equality. **Context:** LM_140-2_text.tex, §32, 395–399, especially (6)–(10). **Register:** IMPL P3; LM1 D.7.

LM_140-2/397 constructs \(\lambda_i:\mathbb\Gamma_{g,\nu}\to\mathbb\Gamma_{g,\nu-1}\) between arithmetic quotient groups and deduces surjectivity from \(\lambda_i\Theta_{g,\nu}=\Theta_{g,\nu-1}\), with both Θ maps surjective. Bijectivity requires equality of their kernels, and 398 explicitly considers the possibility that those kernels shrink as ν increases. Scan 399 then says “je préfère travailler hypothétiquement avec (f)” and surrounds the full double-hatted Birman-shaped sequence with question marks, so neither that sequence nor an extra full-group kernel is proved by this argument. The equality questioned on 145/024 concerns C and A!, a different comparison.

### F04 — The type of the curve and the index of its moduli space differ

**Kind:** reading question about the supplied context. **Source:** 145/005 and 011, \(\widehat\pi_{0,3}\) and its outer centralizer. **Context:** LM_140-2_notes.md, SP6 on 398–399; primary LM_140-2_text.tex, 476–479. **Register:** LM1 D.7; WG2 §1.8 #5.

The earlier LM note speculatively locates the Belyi base case at \(\Theta_{0,4}\), but the primary passage at 476–479 explicitly discusses the arithmetic representation with target \(\mathbb\Gamma_{0,3}\). A type-\((0,3)\) curve group and the parameter space \(M_{0,4}\) play different roles, and counting the variable point as a puncture changes the notation. This is a contextual indexing warning, not a change to any frozen occurrence in MPL_145.

### F05 — Five different kernels or comparison problems

**Kind:** unpursued implication / map concordance. **Source:** 145/004, 023–026, 032–033, and 037. **Context:** LM_140-2_text.tex, 185–189, 295–306, 367–369, and 395–399. **Register:** IMPL P3; LM1 B.18; LM1 D.7.

The following comparison assigns each kernel claim to a specified source and target. The manuscript's explicit enlarged kernel belongs to the last row, while the user's earlier full-group filling claim belongs to the third; identifying them would require an additional theorem absent from these pages. The arithmetic argument of the fourth row establishes a different surjectivity statement.

| Setting | Map or comparison | Kernel/status relevant here |
|---|---|---|
| Geometric mapping classes with one point distinguished | Forget the point after filling, with the appropriate pure or point-stabilizing source | Point pushing in the geometric Birman sequence; this is the completion setting compared in L02. |
| Filling with a retained base point | Peripheral outer automorphisms of the punctured object to automorphisms of the filled group | Point pushing maps to \(\operatorname{Inn}(\pi)\), so it is not killed before passing to Out; LM_140-2/185–189. |
| Full profinite peripheral automorphisms | Full double-hatted Aut-valued map, and separately its composite to Out | Injectivity, surjectivity, and the chosen point-pushing image must be specified; LM_140-2/367–369 and 399 leave difficulties. |
| Arithmetic image/normalizer quotients | \(\mathcal N^!_{g,\nu}\to\mathcal M^!_{g,\nu-1}\), and induced \(\mathbb\Gamma_{g,\nu}\to\mathbb\Gamma_{g,\nu-1}\) | Surjectivity from Θ; bijectivity/equal successive kernels is the extra issue in LM_140-2/397–399. |
| Retained peripheral rectifiers at fixed type \((0,3)\) | \(S\widehat{\widehat{\mathcal E}}^!\to\operatorname{Out}_{\rm lac}^!(\hat\pi)\), 145/025 | Displayed \(\hat\pi\times\hat{\mathbb Z}^{3}\); the projection to Aut has a different kernel, as A03 explains. |

### F06 — No register proof is inferred from a reported prior claim

**Kind:** reading question / evidence limit. **Source:** 145/004 and 025–026. **Context:** LM_140-2_text.tex, 367–369 and 395–399; notes/RESULTS_STATE.md, IMPL P3 and the run-status preamble. **Register:** IMPL P3; LM1 D.7; INTAKE 20261114 §4.2.

The supplied register extract contains no precise statement and proof of the reported “onto with larger-than-point-pushing kernel” theorem for the full filling map. The intake item on topoi and hole filling is expressly a reading, not a referee verdict, and neither it nor a nearby “Proved” label identifies the necessary map by itself. A04 supplies a formal way to test such a claim once its source, target, point-pushing inclusion, and completed-group convention are specified.

## 5. Bounded independent calculations

These are research annotations only. They preserve every frozen formula, distinguish conditional hypotheses from consequences, and make no claim of novelty.

### A01 — A proof of the pure-power “Exercice!” on scan 036

**Kind:** own deduction. **Source:** 145/036, (14), “Exercice!”; the relation on 017 and 033. **Context:** LM_140-3_text.tex, 070 and 076, conjugated-power equations, and 105, (75bis)–(75ter), are the nearest located comparisons, but no exact proof of this pure-power exercise was found. **Register:** LM1 B.18; LM2 B.g11, neither broader open item resolved. **Confidence:** high, because an explicit continuous nilpotent quotient proves exactly the displayed implication.

Put \(R=\widehat{\mathbb Z}\), \(X=I+E_{12}\), \(Y=I+E_{23}\), and \(H=YX\) in \(UT_3(R)\), so the free profinite universal property gives a continuous map
\[
l_0\longmapsto X,\qquad l_1\longmapsto Y,\qquad
l_\infty=(l_1l_0)^{-1}\longmapsto H^{-1}.
\]
Writing a matrix by its entries \((a,b,c)=(a_{12},a_{23},a_{13})\), multiplication is
\[
(a,b,c)(d,e,f)=(a+d,b+e,c+f+ae),
\]
and the integer identities
\[
H^n=(n,n,\tbinom n2),\qquad Y^nX^n=(n,n,0)
\]
extend continuously to \(n=p\in R\), since
\[
n\equiv m\pmod{2N}
\quad\Longrightarrow\quad
\binom n2-\binom m2=\frac{(n-m)(n+m-1)}2\equiv0\pmod N
\]
for every positive N, giving a continuous function \(b(p)\) with \(2b(p)=p(p-1)\). Equation (14) forces \(H^p=Y^pX^p\), hence \(b(p)=0\), then \(p(p-1)=0\), and finally \(p=1\) because the source requires \(p\in R^\times\); conversely \(p=1\) satisfies the defining relation. This proves the exercise without inverting 2 or treating \(\widehat{\mathbb Z}\) as an integral domain, and does not remove conjugators or generation conditions from the larger profinite problems.

### A02 — Equation (13), as written, omits the identity

**Kind:** own formal diagnostic / reading question. **Source:** 145/036, (13), compared with 017, (1), and 033, (2). **Context:** LM_140-3_text.tex, 086, (13), uses the descending peripheral order; the nearest pure-power comparisons are those in A01. **Register:** WG2 §1.8 #5; LM1 B.18. **Confidence:** high, because a quotient modulo 2 already detects the conflict.

At \(p=1,\sigma=\mathrm{id}\), the written ascending equation (13) would require \(l_0l_1l_\infty=1\), but the map in A01 gives
\[
XY(YX)^{-1}=I+E_{13}\ne I,
\]
even in \(UT_3(\mathbb F_2)\), so the printed condition cannot define the claimed subgroup. More precisely, using A01 and invariance of the equation “product equals 1” under cyclic rotation, odd permutations in (13) force \(p=1\), while even permutations reduce after inversion and reversal to A01 with exponent \(-p\), forcing \(p=-1\). Thus its solution pairs in \(R^\times\times S_3\) satisfy \(p=-\operatorname{sgn}\sigma\), a coset omitting the identity, whereas a descending-order variant would give the intended signed graph. This last comparison diagnoses the problem but does not establish what the author meant to alter or change any factor in the transcription.

### A03 — Two forgetful maps, two kernels

**Kind:** own formal diagnostic / conditional kernel calculation. **Source:** 145/033, (4)–(7), margin “noyau \(i(\hat\pi)\),” and 025–026. **Context:** LM_140-2_text.tex, 297–300, especially its two different quotients of the special extension. **Register:** LM1 B.18; IMPL P3. **Confidence:** high for the contradiction; the stated kernel identifications use the peripheral-centralizer description explicitly recorded below.

Call the projection in (4) P in these notes, to distinguish it from the scalar p, and let \(q:\operatorname{Aut}_{\rm lac}(\hat\pi)\to\operatorname{Out}_{\rm lac}(\hat\pi)\), so equation (7) gives
\[
P\,i(g;\alpha_i)=\operatorname{int}(g),\qquad
P\,i(l_0;0,0,0)\ne1
\]
because \(l_0\) and \(l_1\) do not commute, as witnessed by \(XY\ne YX\) in A02's finite quotient. Consequently \(i(\hat\pi\times0)\) is not even contained in \(\ker P\), and, under the centrelessness and peripheral-centralizer hypotheses \(C_{\hat\pi}(l_i)=L_i\) used by the parameterization on 025–026, the actual distinction is
\[
\ker P=i(\{1\}\times\hat{\mathbb Z}^{3}),\qquad
\ker(qP)=i(\hat\pi\times\hat{\mathbb Z}^{3}).
\]
Abelianization identifies the peripheral classes with \(e_0,e_1,-e_0-e_1\), forcing \(p=1,\sigma=\mathrm{id}\) when \(u=1\), and without importing that centralizer identification the tuple formulas already give
\[
\ker P=\{(1,\mathrm{id},g_0,g_1,g_\infty):g_i\in C_{\hat\pi}(l_i)\},
\]
and the outer kernel allows a common inner conjugator g, giving \(g_i=gc_i\) with \(c_i\in C_{\hat\pi}(l_i)\). Thus the formal conflict is independent of choosing a correction to the ambiguous marginal reference, and the larger outer kernel displayed on 025 is not a filling-map computation.

### A04 — A precise conditional test for an extra filling kernel

**Kind:** own idea / formal lemma. **Source:** 145/004's compatible map and 025's different kernel, compared with the filling question. **Context:** LM_140-2_text.tex, 367–368, which separates the Aut-valued map and the chosen point-pushing inclusion. **Register:** IMPL P3; LM1 D.7. **Confidence:** high for the group-theoretic lemma; no claim that the required full profinite hypotheses have been established.

Let \(\psi:A\to\operatorname{Aut}(\pi)\), let q be the quotient to Out, and suppose \(P\le A\) maps isomorphically onto \(\operatorname{Inn}(\pi)\). For \(a\in\ker(q\psi)\), choose the unique \(p_a\in P\) with \(\psi(p_a)=\psi(a)\), so \(p_a^{-1}a\in\ker\psi\), proving
\[
\ker(q\psi)=P\cdot\ker\psi,\qquad P\cap\ker\psi=1.
\]
Under precisely these hypotheses, a kernel strictly larger than P for the Out-valued map is therefore equivalent to a nontrivial kernel for the Aut-valued map. This is a way to audit the reported claim without assuming normality of an unspecified point-pushing image, or mistaking the rectifier factors of 145/025 for evidence of such an extra filling element.

### A05 — A fixed-index commensuration locus need not be a subgroup

**Kind:** own idea / bounded counterexample to an unrestricted interpretation. **Source:** 145/002, final `\unsure{H_n\|H_1}` assertion. **Context:** LM_140-4_text.tex, 190–192 and 204–205, uses commensurability and finite-index refinements. **Register:** WG2 §1.8 #5; LM8 A.12. **Confidence:** high for the lattice calculation, low for its applicability to the unspecified geometric G and U on this fragment.

Take the deck lattice \(\Lambda=\mathbb Z^2\subset\mathbb R^2\), a prime p, and \(u=\operatorname{diag}(p,p^{-1})\), which identifies the index-p lattices \(\mathbb Ze_1+p\mathbb Ze_2\) and \(p\mathbb Ze_1+\mathbb Ze_2\). If \(L\subset\Lambda\) and \(u^2L\subset\Lambda\), every second coordinate of L is divisible by \(p^2\), so \([\Lambda:L]\ge p^2\) and \(u^2\) has no such realization at index p. Thus a fixed-index locus is not generally closed under multiplication even when the ambient commensurator is a group. This diagnoses the need for an extra hypothesis if the reading is \(H_n\), but is not a counterexample to a fully specified hyperbolic or holomorphic claim, and does not eliminate the alternative reading \(H_1\).

## 6. Primary literature comparisons

### L01 — A modern five-point criterion cannot be inferred from three-loop equations

**Kind:** literature comparison / unpursued implication. **Source:** 145/008, 024, 033, and 038, their three-factor peripheral equations. **Context:** LM_140-3_text.tex, 075–080; MPL_142_094-122_notes.md, R25, an uncertain lead. **Register:** LM1 D.7; LM2 E.3; LM8 B.28.

Furusho (2010, Theorem 2, p. 547) writes the group pentagon in the unipotent completion of the pure four-strand braid group, and Remark 11 (p. 554) gives an equivalent five-factor equation in the unipotent completion of the pure sphere braid group on five strings together with the commutator condition. His implication from pentagon to hexagon relations in the specified completion settings does not establish a converse that would supply a pentagon from the order-two/order-three relations in MPL_145. The comparison gives a precise criterion for what would count as the missing five-point equation, while the article's historical question about the full profinite analogue is not used as a statement of its current status.

### L02 — The geometric completed Birman sequence has a specified domain

**Kind:** literature comparison / scope distinction. **Source:** 145/023, 025, 032, and 037, completion and peripheral-extension distinctions. **Context:** LM_140-2_text.tex, 185–189, 295–306, and 367–369. **Register:** IMPL P3; LM1 B.18; LM1 D.7.

For an oriented connected surface of finite type and negative Euler characteristic, Boggi (2018, Corollary 4.7) gives a Birman exact sequence with the completed point-pushing kernel for the specified congruence closures of geometric mapping class groups, under the stated equality of the induced and pro-\(\mathscr C\) topologies on the fundamental group, including the full finite-group and pro-p cases. His §5, equation (6), separately records the procyclic boundary-twist kernel when a boundary framing is retained. These are primary comparisons for separating geometric completion, pointed filling, and peripheral framing; they do not identify the geometric closures with the full peripheral automorphism groups used in MPL_145.

## 7. Standing question: self-flagged unverified steps

This register distinguishes open questions, attempted calculations completed locally, explicit withdrawals, and work the author deliberately leaves aside. An uncertain punctuation mark is not counted as a certain authorial doubt, and an ordinary reading uncertainty in the diplomatic text is not itself a mathematical conjecture.

| ID / kind | Scan and brief source wording | State within this packet | Contextual comparison and register IDs |
|---|---|---|---|
| U01 — expectation / reading question | 003, “On doit en fait avoir `\unsure{\beta=\gamma\|\beta\ne\gamma}`” | Abelianization is proposed as the check; the sign remains graphically uncertain, as N05 explains. | LM_140-3_text.tex, 058 and 079–080; LM1 D.7; WG2 §1.8 #5. |
| U02 — self-flagged claim | 005, “sauf erreur ce sera un autom.” | Conditional on topological generation; 009 asks how to ensure that condition, and 024/033/038 retain it. | LM_140-3_text.tex, 075 and 211; LM2 B.g11; LM2 F.3; N07. |
| U03 — verification undertaken locally | 008, “Il faut vérifier … la relation” | Several displayed rewritings carry out the peripheral-product check, but do not settle automorphy. | LM_140-3_text.tex, 075; LM1 D.7; N07/N09. |
| U04 — explicit open question | 009, “Mais comment vérifier … un automorphisme ?” / “`\unsure{Ça}` semble délicat” | No general elimination of the generation condition is supplied later in the packet. | LM_140-3_text.tex, 075 and 211; LM2 B.g11; LM2 F.3; N07/N28. |
| U05 — tentative trial, locally revised | 013, “n'est peut-être pas de carré,” `\alpha=\unsure{2\|1}\ ?`, cancelled “Non !,” live “OK” | The trial is revised on the page, followed by explicit ε formulas; inverse conventions change again on 019. | LM_140-3_text.tex, 086–088; WG2 §1.8 #5; N14/N19. |
| U06 — relation-independence doubt | 014, “ces relations ne semblent pas `\unsure{conséquences}` des autres” | Completeness of the proposed presentation is not established by that marginal observation. | LM_140-3_text.tex, 086–088; LM1 B.18; N15. |
| U07 — structural warning and withdrawal | 014–015, “ce qui est inquiétant”; cancelled “il faudrait donc avoir” | The resulting torsion argument and product-equals-one chain are cancelled on 015. | LM_140-3_text.tex, 086–088; LM4 D.12; N16. |
| U08 — conjectural replacement | 015, “Sans doute” before \(\varepsilon_0\varepsilon_1\varepsilon_\infty=\sigma_1\) | The text proposes a replacement and then restarts the construction; it is not presented as a finished proof. | LM_140-3_text.tex, 086–088; LM1 B.18; N16. |
| U09 — requested convention repair | 015, “qu'il faudrait distinguer” / “il faudrait …” | The criticism concerns discrete versus profinite groups and notation, addressed by the geometric restart on 016–017. | LM_140-3_text.tex, 086–087; WG2 §1.8 #5; N17. |
| U10 — uncertain punctuation | 017, “et non \(l_0l_1l_\infty=1\) ! `\unsure{?}`” | The order correction is explicit; the additional question mark is not a certain reading and cannot alone establish a further doubt. | LM_140-3_text.tex, 086, (13); WG2 §1.8 #5; N17/A02. |
| U11 — explicit withdrawal | 018, “C'est faux” | The claimed presentation is rejected; 020 adds cyclic conjugation relations. | LM_140-3_text.tex, 086–087; LM1 B.18; N18. |
| U12 — missing calculation | 019, “où il faut compléter l'expression …” | Equations (9) attempt the missing ε products on the same page; completeness of relations remains qualified on 022. | LM_140-3_text.tex, 088; LM1 B.18; N19. |
| U13 — explicit correction | 020, “Il faut ajouter les relations” | The cyclic conjugation relations are supplied in the margin and used in the simplification. | LM_140-3_text.tex, 086–087; LM1 B.18; N18/N20. |
| U14 — calculation programme | 020, “On voudrait maintenant expliciter les \(\varepsilon_i\)” | Compare the calculations and revisions on 019 and 022; the physical page order is preserved rather than rearranged to make the exposition linear. | LM_140-3_text.tex, 088; WG2 §1.8 #5; N19. |
| U15 — action to be supplied | 021, “Il faut expliciter les opérations” | The following equation (14) gives the action, with some entries left as the author's own dots. | LM_140-3_text.tex, 086–087; LM1 B.18; N21. |
| U16 — expressly incomplete relation list | 022, “il faut aussi ajouter (au moins!)” | Adds cyclic conjugation of the ε generators without claiming that the added list is exhaustive. | LM_140-3_text.tex, 086–088; LM1 B.18; N19/N21. |
| U17 — question answered negatively | 022, “On peut encore se demander si \(\rho\) s'exprime …” | The author answers “non,” by reference to the earlier quotient argument. | LM_140-3_text.tex, 086–087; LM1 B.18; N20. |
| U18 — equality explicitly unknown | 024, “j'ignore si cette inclusion est une égalité” | The centralizer C is not identified with A! by this packet. | LM_140-3_text.tex, 058–080; LM1 D.7; LM2 E.3; LM8 B.28; N25. |
| U19 — conjugation formulas requested | 026, “Il faudrait expliciter les opérations” | A provisional covariance formula appears; fuller formulas are given on 037, subject to the local notation shifts. | LM_140-3_text.tex, 211–212; LM1 B.18; WG2 §1.8 #5; N29. |
| U20 — full presentation requested | 029, “Il faudrait … une description … par gén. et relations” | The abandoned start is replaced on 030 and reduced on 031. | LM_140-3_text.tex, 086–089; LM1 B.18; N33. |
| U21 — added relations and doubtful redundancy statement | 030, “Il faut ajouter les relations” and “`\unsure{sont}` conséquences” | The wording and logical status of redundancy are not fully secure; the transcription retains both marginal stages. | LM_140-3_text.tex, 086–089; WG2 §1.8 #5; LM1 B.18; N33. |
| U22 — cancelled question and proposed answer | 030, cancelled “Question,” “Peut-on,” replaced by “On peut … ??” | The whole paragraph is cancelled; 031 gives a different reduction to three generators. | LM_140-3_text.tex, 086–089; LM1 B.18; N33. |
| U23 — uncompleted construction | 032, “Il faudrait encore expliciter l'extension \(S\Gamma\)” | On 037 the author expressly declines to write its presentation. | LM_140-2_text.tex, 295–306; LM_140-4_text.tex, 277; LM1 B.18; N35. |
| U24 — stated computational limitation | 033–034, “pas … entièrement explicite et satisfaisante” | Word evaluation makes the law explicit only when the profinite inputs are themselves supplied as suitable words or limits. | LM_140-3_text.tex, 193 and 212; LM1 B.18; LM2 B.g11; N37. |
| U25 — lift requested, partly supplied | 035, “qu'on voudrait remonter à \(S\mathcal E\)” | Equation (12) supplies the signed subgroup's tuples; the other local lifting problem receives a negative answer on 037. | LM_140-2_text.tex, 305–306; LM_140-3_text.tex, 086–087; LM1 B.18; N38/N39. |
| U26 — expectation and exercise | 036, “Sans doute …” / “Exercice!” | No proof is written on the leaf; A01 proves its separate descending-order exercise, while A02 preserves the problem in (13). | LM_140-3_text.tex, 070, 076, and 105; LM1 B.18; WG2 §1.8 #5. |
| U27 — question answered negatively without a full local proof | 037, “Comment remonter … ?” / “ils ne se remontent pas” | The source invokes the nonsplit local extension and the requirement to centralize \(L_0\). | LM_140-2_text.tex, 305–306; LM1 B.18; N39. |
| U28 — work deliberately left aside | 037, “je ne vais pas m'y attarder” | The generators-and-relations presentation of \(S\Gamma\) and \(S\mathcal E\) is not completed here. | LM_140-2_text.tex, 295–306; LM_140-4_text.tex, 277; LM1 B.18; N35. |
| U29 — redirection of the final programme | 038, “moins intéressant pour la suite” / “plutôt … la commutation mod autom. intérieurs” | This is an unfinished change of target, not a retraction of every preceding strict-commutation computation. | LM_140-3_text.tex, 058–080 and 211–212; LM1 D.7; LM2 E.3; N40. |

## 8. Standing question: title sheets and page counts

### T01 — Cover and internal headings

**Kind:** documentary reading question. **Source:** 145/001, printed IMAG cover; 005, “[C]” and circled 1; 033, circled 2 and “Le groupe \(S\widehat{\widehat{\mathcal E}}\).” **Context:** LM_140-3_text.tex, 058 and 086–087; SECTIONS_STATE.md, section “Autour de la Longue Marche.” **Register:** WG2 §1.8 #5; WG2 §1.4 #3.

Scan 001 is a printed institutional cover, carrying no autograph date or page-count statement. Scan 005 begins a separately headed dossier, “Automorphismes extérieurs du groupe à lacets profini \(\hat\pi=\hat\pi_{0,3}\),” with the marginal addition concerning extensions of \(\mathcal E_{0,3}\), and 033 opens its circled second part. The contextual [C] references support identifying the loop dossier, but do not turn the cover into an authorial title sheet or date its preliminary fragments.

### T02 — Observed counts and two numbering series

**Kind:** documentary count. **Source:** 145/001–038 and every visible `\mspage`. **Context:** SECTIONS_STATE.md, cote 145 description; LM_140-3_text.tex, 058 and 086–087 for the separate [C] dossier. **Register:** WG2 §1.8 #5.

The supplied set contains **38 scans: one printed cover and 37 manuscript pages**, comprising three preliminary manuscript pages, 002–004, and the 34-page loop dossier, 005–038. A lower numbering series runs from 1 to 37, with the reading on 020 retained as `\unsure{19\|10}`, while a separate visible upper series starts at 1 on 005 and eventually reaches 17 on 037. The table records the upper gaps and physical scan order without supplying missing numerals, reordering leaves, inferring missing scans, or claiming that both numbering series were written by the same hand.

### T03 — Catalogue count is consistent but not an autograph count

**Kind:** dating / provenance question. **Source:** 145/001–038. **Context:** official catalogue, cote 145 and note 149; SECTIONS_STATE.md, cote 145 description. **Register:** WG2 §1.4 #3; WG2 §1.8 #5.

The catalogue's 37-page count agrees with the observed manuscript total when the printed cover is excluded (Université de Montpellier, n.d.). The packet itself has no separate written total such as “19 pages” or a title-sheet range such as “Pages 1–67.” The folder designation and its date remain archival metadata, as Q1 explains, and cannot rule out a differently dated preliminary fragment.

| Scan | Visible upper number | Visible lower number | Heading / documentary state |
|---|---|---|---|
| 001 | — | — | Printed IMAG institutional cover and logo; no handwritten title/date/count. |
| 002 | — | 1 | Preliminary stratal cancellation and commensurator fragment. |
| 003 | — | 2 | Preliminary profinite loop-automorphism calculation. |
| 004 | — | 3 | Wholly cancelled descent/topos draft. |
| 005 | 1 | 4 | [C]; circled 1; automorphism title and marginal extension title. |
| 006 | — | 5 | Continuation. |
| 007 | 2 | 6 | Continuation. |
| 008 | — | 7 | Continuation. |
| 009 | 3 | 8 | Continuation. |
| 010 | — | 9 | Continuation. |
| 011 | 4 | 10 | Continuation. |
| 012 | — | 11 | Continuation. |
| 013 | — | 12 | Dense trial calculation and cancellations. |
| 014 | — | 13 | Continuation. |
| 015 | — | 14 | Cancelled block; separator; critique of notation. |
| 016 | — | 15 | Geometric restart and drawing. |
| 017 | 7 | 16 | Mixed fundamental group and path convention. |
| 018 | — | 17 | Presentation and “C'est faux” margin. |
| 019 | — | 18 | Epsilon calculation and inverse-convention NB. |
| 020 | 8 | 19 or 10, doubtful | Presentation and large marginal revision. |
| 021 | — | 20 | Signed action and notation critique. |
| 022 | 9 | 21 | Epsilon relations and signed stabilizer. |
| 023 | 10 | 22 | Cartographic group; separator; single/double hats. |
| 024 | — | 23 | Centralizer and pure decorated coordinates. |
| 025 | 11 | 24 | Composition, opposite cocycle, and outer kernel. |
| 026 | — | 25 | Covariance and special-extension margin. |
| 027 | 12 | 26 | Explicit finite \(\Gamma_{0,3}\) and partial sections. |
| 028 | — | 27 | Interior stabilizers and primed point names. |
| 029 | 13 | 28 | Real fixed set and cancelled presentation start. |
| 030 | — | 29 | Revised full presentation and marginal relations. |
| 031 | 14 | 30 | Three-generator presentation and abstract symmetry. |
| 032 | — | 31 | Short request to explicate \(S\Gamma\). |
| 033 | 15 | 32 | Circled 2; “Le groupe \(S\widehat{\widehat{\mathcal E}}\).” |
| 034 | — | 33 | Multiplication and conjugation formulas. |
| 035 | 16 | 34 | Signed partial section and identity rectifiers. |
| 036 | — | 35 | Equations (13)–(14) and “Exercice!” |
| 037 | 17 | 36 | Local lifting obstruction and conjugation formulas. |
| 038 | — | 37 | Strict commutation; final return to the outer problem. |

## 9. Consequences for the supplied results register

The following is an evidence-to-item index, not an update of the register. It states what this packet contributes beyond the existing entry and preserves the supplied distinction between reviewed results, intake readings, unreviewed return claims, and planning questions.

| Register ID | Supplied status or qualification | Contribution of MPL_145 / these notes |
|---|---|---|
| LM1 D.7 | Open, return claim | Concrete early centralizer coordinates, explicit unknown equality, and no identified five-point equation; Q1–Q3, N07–N12, N24–N25, N40. |
| LM1 B.18 | Open, with prior multiplication and fibre-product reductions claimed | Earlier rectifier-extension formulas, convention changes, and two precisely diagnosed formula issues; N09, N17–N21, N26–N39, A01–A03. |
| LM2 E.3; LM8 B.28 | Open; B.28 intake OPEN | Three-loop and outer-commutation conditions do not establish the additional normalized/orbifold compatibility or its implication from the pentagon; Q1, N25/N40, L01. |
| LM2 B.g11; LM2 F.3 | Open, return claims | Generation remains a separate source condition; the pure-power exercise supplies no integral compatible lift of a general loop solution; N07/N28/N37, A01. |
| LM4 D.12; LM8 A.12 | Open; A.12 intake OPEN | Explicit finite geometric stabilizers and sections, with no unrestricted full profinite realization or torsion classification; N08/N12/N16/N22/N30/N32/N39. |
| LM8 G.20 | Open, intake OPEN | Cartographic discrete presentation supplies context, not the residual full profinite fixed-subgroup result; N23. |
| IMPL P3 | Open candidate prompt | Formal descent and fixed-type framing distinguished from puncture filling; Q3, N06/N24/N35/N36, F01–F06, A04. |
| FLAGGED_149 A9 | Proved by return; FLAGGED_149 intake pending | Cancelled mixed-topos draft and realized commensurations add source comparisons; identified kernel and quotient remain part of extension data; N03/N06/N34. |
| FLAGGED_149 E4 | Proved by return, no completed review supplied | Cancelled component-indexed fragment is a continuation lead, not a new torus-kernel proof; Q4/N01. |
| EXIT_ONE_TYPE P4e/P1d1 | Proved by return, no review verdict supplied here | No recovered coherent incidence construction or recovery of the topology lost by the coarse maquette; Q4/N01. |
| CYCLOTOMIC_KERNEL C1/C8 | Rows are return claims; run explicitly reviewed, zero wrong | Existing bounded inertia/normalizer results are cited rather than re-derived; the missing intersection-multiplicity calculation is not found in this packet; Q5/N13/N39. |
| FLAGGED_149 ZCF6 | Open, return claim | Finite geometric section examples do not discharge the outstanding arithmetic existence assertions; Q5/N22/N32. |
| LM7_PUSH E.3; E.58/E.64/E.65 | E.3 Open; listed proved rows explicitly under referee check | No full profinite lift or CM-image conclusion is inferred from these pages or those unreviewed chains; Q1/N07/A01/L01. |
| WG2 §1.4 #3; WG2 §1.1 #6 | Unchecked planning questions | Candidate component fragment identified; physical continuation and missing inertia proof remain unresolved; Q4–Q5/N01/T03. |
| WG2 §1.8 #5 | Unchecked glossary plan | All 78 Γ tokens located; exclamation, primes, hats, signed stabilizers, loop order, and numbering distinguished; §2, N05/N10/N14/N17/N19/N21/N26/N29/N31, §8. |
| WG H4 | Unchecked hunch | No proof of a real-oriented-blowup, toroidal, or face-asphericity claim follows from the small cancelled diagram on 002; Q4/N01. |
| INTAKE 20261114 §4.2 | Intake reading, expressly not a referee verdict | Used only to identify the prior topoi/hole-filling programme, not to certify a full-group filling theorem; N06/F06. |

## 10. References and source identification

### Primary manuscript and catalogue sources

Grothendieck, A. (n.d.-a). *[C]: Automorphismes extérieurs du groupe à lacets profini; notes on mixed and special extensions, with preliminary fragments* [Unpublished manuscript, cote 145, supplied scans 001–038; dossier catalogued as *Printemps 81 (vieille rédaction)*]. Archives Grothendieck, Université de Montpellier. Source edition in this package: **MPL_145_transcription.tex** and **pages/MPL_145_145_scanNNN.tex**. The descriptive title after [C] identifies the contents and is not an invented autograph title.

Grothendieck, A. (n.d.-b). *La Longue Marche à travers la théorie de Galois* [Unpublished manuscript, cotes 140-1–140-4; broadly dated 1981]. Archives Grothendieck, Université de Montpellier. Supplied checked diplomatic texts: **LM_140-1_text.tex**, **LM_140-2_text.tex**, **LM_140-3_text.tex**, and **LM_140-4_text.tex** in **MPL_145_context.zip**; exact scans are cited with each comparison.

Université de Montpellier. (n.d.). *Archives Grothendieck* [Archival catalogue, cote 145 and note 149; cote 149 for the separate dossier]. Retrieved November 14, 2026, from https://grothendieck.umontpellier.fr/archives-grothendieck/

### Primary research literature

Boggi, M. (2018). *Congruence topologies on the mapping class group* (Version 1) [Preprint]. arXiv. https://doi.org/10.48550/arXiv.1804.06322  
Version consulted: https://arxiv.org/html/1804.06322v1 ; §2.1, Corollary 4.7, and §5, equation (6).

Furusho, H. (2010). Pentagon and hexagon equations. *Annals of Mathematics, 171*(1), 545–556. https://doi.org/10.4007/annals.2010.171.545  
Primary text consulted: https://annals.math.princeton.edu/wp-content/uploads/annals-v171-n1-p13-p.pdf ; Theorem 2 and Remark 11.

### Supplied working materials, not independent mathematical authorities

*Our results so far on these folders (package 40: cotes 145).* (2026, November 14). [Research register, built 02:03 UTC]. **notes/RESULTS_STATE.md**, supplied in **MPL_145_context.zip**. Authorship and status are those described in its own preamble; the present notes do not replace its underlying returns or referee reports.

*MPL_145 contextual materials.* (2026). [Supplied working corpus]. **README.md**, **SECTIONS_STATE.md**, **LM_OVERVIEW.md**, **LM_GLOBAL_PASS.md**, **LM_table_of_contents.txt**, **LM_140-1_notes.md** through **LM_140-4_notes.md**, and the neighbouring cote 142, 146, 147, and 149 research notes. The specific neighbouring files cited above are **MPL_142_094-122_notes.md**, **MPL_147_048-137_notes.md**, **MPL_149_001-090_notes.md**, and **MPL_149_091-136_notes.md**; these are first-pass leads, and their cited original images were not included in this context corpus.

### Reproducibility and editorial boundary

The companion doubts file contains the reconciled notation table, all 346 explicit uncertainty markers, proposed abbreviation expansions, and the legibility assessment; the inventory records 797 transcribed elements across all 38 scans. Structural LaTeX checks were performed, but a full compilation could not be completed because the installed executables lacked the required LaTeX format and package files; no compilation success is claimed. The final hash comparison is recorded in **progress.log**, and all mathematical diagnoses in this file leave the frozen transcription unchanged.

