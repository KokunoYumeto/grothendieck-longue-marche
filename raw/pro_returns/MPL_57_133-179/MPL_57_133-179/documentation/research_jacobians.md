# Research memo: cote 57, scans 133–179, and cote 44 Theorems 1–7

Research date: 2026-11-18. Researcher: `/root/jacobians_earlier_forms` (ChatGPT, GPT-6 Astra Pro). The transcription was frozen at 2026-11-18 08:54:59 UTC before this comparison; this researcher read no scan images and changed no transcription, inventory, doubt, or check-event file.

## Finding and evidence limits

**No earlier textual form of any of cote 44's seven numbered theorems has been identified in the 43 frozen pages of this selection.** There are direct links to ordinary Picard schemes, curve Jacobians, line-bundle families, and divisor deformation theory, but those links do not supply the higher-codimension cycle objects, maps, or assertions in the seven-theorem programme. This is a bounded documentary conclusion about the supplied text, not a verdict about the archive, the truth of the programme, or its possible historical development.

The full `context/README.md` and full `context/notes/RESULTS_STATE.md` were read before the source comparisons. All 43 present individual page TeX files, including reused leaves, were read; the relevant cote 44 statements were compared directly with the supplied transcription. The earlier notes and the notes for cote 57 scans 271–315 were used as **unchecked leads**: their quoted manuscript readings and bibliographical claims were not upgraded to verified source or literature results. No external literature, Hua modernisation, or Oda result is needed for this particular documentary answer.

### Source and locator key

| Key | Exact file and locator convention | Evidence level in this memo |
|---|---|---|
| P57(n) | `MPL_57_133-179/pages/MPL_57_133-179_57_scanNNN.tex`; `57:n Lx–y` means lines of that individual file | Current frozen diplomatic text, including uncertainty and cancellation marks; no rereading of scans |
| CT | `context/MPL_16+47+54+44_transcription.tex`; cote:scan and aggregate TeX line | Supplied earlier diplomatic transcription, not second-passed here |
| CN | `context/MPL_16+47+54+44_notes.md`; numbered item or D-number | Earlier run's unchecked research notes |
| SN | `context/same_cote_57/MPL_57_271-315_notes.md`; section and J-number | Same-cote first-pass notes, not their underlying page transcriptions |
| RS | `context/notes/RESULTS_STATE.md`; exact statement ID | Register retains its own status distinctions |

RS **WG2 §2.4 #4** is the exact carry-question, not an established theorem; **WG2 §2.3 #12** is the corresponding unchecked programme summary. **WG H9** is an unchecked proposed height/Hodge reduction. **MPL_57_271-315 J03** is explicitly a first-pass lead; no result in the supplied register is used as a proof of any numbered cote 44 theorem.

## Exact seven-theorem comparison

The notation in this table is explanatory only. CT's `\unsure{...}` and `\deleted{...}` readings remain in the frozen source; in particular the complementary index of Theorem 3, the quotient relation, and parts of Theorem 5 are not silently resolved.

| Theorem and exact CT locator | Assertion to be matched | Strongest current-page contact | What is missing from an identification |
|---|---|---|---|
| Th. 1: 44:2, L2787–2790 | Identification, qualified “en substance,” of a subgroup of `Alb(S)` with the kernel of a map to a codimension-i cycle quotient | 57:133 L5–14, 135 L16–22: affine kernel of Picard pullback; 173 L25–29: quotient by line bundles from the base | Different source, target, and kernel; no cycle family ξ, proposed Albanese equivalence, or map `Alb(S) → Z^i/Z^i_alb` |
| Th. 2: 44:2, L2793 | A bound depending only on X for `dim(Alb(S)/N(ξ))`, sharpened to half the odd Betti number | 57:149 L11–21 and 151 L27–38: dimensions and degree-one cohomological/combinatorial contributions for a curve Picard group; 164 L25–34: tangent sequence | No bound uniform over parameter families and no odd-degree cohomological realization for general i; `P_ξ` at 57:160 L7–19 is a projective object |
| Th. 3: 44:2, L2796–2799 | Natural abelian-variety structure on the algebraically trivial cycle quotient and canonical complementary-degree duality | 57:142 L42–46, 144 L7–15, 147 L3–13, 151 L23–38, 173–179: ordinary and generalized Picard objects | No construction of the higher-codimension quotient or its duality; even the generalized curve object E need not be an abelian variety |
| Th. 4: 44:2, L2802–2803; clarification 44:8–9, L2979–2995 | The specific canonical self-duality in odd middle dimension is a polarization | 57:158 L5–25, 160 L33–42, 162 L16: very ample line bundles, projective data, and Brauer–Severi forms | No `P^m`, no cycle-induced symmetric self-correspondence, and no ampleness proof for that correspondence |
| Th. 5: 44:4, L2849–2874 | Proposed Néron–Tate height/intersection identity for restrictions to a generic hyperplane pencil, with geometrically integral fibres | 57:148 L4–20 and 156 L6–18: surface intersection and linear-system calculations; 142–145: a curve-family cohomology sequence | No height pairing, restriction of complementary cycles, pencil identity, normalization, or sign calculation |
| Th. 6: 44:4, L2876–2884 | Under Th. 5's conditions: restriction isomorphism if `2i ≤ n−1`; fixed-factor image if `2i=n`; surjectivity if `2i ≥ n+1` | 57:133 L5–12: pullback for a surjective proper map; 164 L23–34: deformation of `Div → Pic` | A hyperplane inclusion is a different map; neither passage supplies the three ranges or fixed-factor statement |
| Th. 7: 44:6, L2942–2944 | Numerical equivalence equals τ-equivalence for the displayed class of algebraic cycles on smooth projective X | 57:169 L8–26: divisors of rational functions; 173 L3–29: ordinary divisor classes and line bundles | No numerical/τ comparison is stated in this selection, and no unrestricted cycle comparison follows from its divisor vocabulary |

## Candidate notes for integration

Each discussion below is at most four sentences. All are documentary scope comparisons, not proofs of the manuscript's mathematical assertions.

### JAC01 — Theorem 1: two different kernels

**File/scan:** P57(133), 57:133 L5–14; P57(135), 57:135 L16–22; P57(173), 57:173 L25–29.  
**Kind:** unpursued implication.  
**Short quote:** “le noyau … Pic …”; “en substance” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12.  
**Context:** CT, 44:2 Th. 1, L2787–2790; CN 44:2:1; SN §1, J01.

The subgroup `N` in 57:133 is the kernel of pullback between ordinary Picard functors, whereas CT, 44:2 Th. 1 concerns a subgroup of a parameter variety's Albanese with a cycle quotient as target. The former is useful Picard infrastructure but does not define `N(ξ)` or establish the latter identification. Its own proof begins by admitting representability, and 57:135 warns that a monomorphism between these non-finite-type Picard schemes need not be affine, so even the ordinary Picard argument should not be reported here as a completed substitute.

### JAC02 — Theorem 2: curve dimensions and projective notation

**File/scan:** P57(149), 57:149 L11–21; P57(151), 57:151 L27–38; P57(160), 57:160 L7–19; P57(164), 57:164 L25–34.  
**Kind:** unpursued implication.  
**Short quote:** “g=dim Pic”; “un nb ne dépendant que de X” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12.  
**Context:** CT, 44:2 Th. 2, L2793, and 44:8, L2974; CN 44:2:2, D09–D10; SN §1, J02.

The curve calculation separates normalization genera, multiplicative contributions, and additive contributions, while 57:164 displays tangent spaces for divisors and Picard. These do not supply CT's bound for all family-wise Albanese quotients in arbitrary codimension, or its proposed realization in odd-degree cohomology. In particular, the `P_ξ` at 57:160 belongs to the projective data of a relatively very ample line-bundle class and is not CT's `P_ξ=Alb(S)/N(ξ)`.

### JAC03 — Theorem 3: an explicit endpoint, not the higher-cycle quotient

**File/scan:** P57(142), 57:142 L42–46; P57(144), 57:144 L7–15; P57(147), 57:147 L3–13; P57(151), 57:151 L23–38; P57(179), 57:179 L3–9.  
**Kind:** unpursued implication.  
**Short quote:** “extension de J=Pic⁰ … par T”; “J¹=Pic⁰” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12; MPL_57_271-315 J03.  
**Context:** CT, 44:2 Th. 3, L2796–2799; 44:8, L2974; CN 44:2:3 and D08; SN §1, J03.

The letter in CT explicitly identifies its first endpoint with ordinary `Pic⁰`, giving a direct connection to the current Picard and curve calculations. The pinched-curve object `E=Pic⁰_{Z/S}` is described as an extension of `J` by a torus, and the singular-curve notes separately examine when `Pic⁰` is abelian; neither construction is the asserted higher-cycle quotient or its complementary-degree duality. The current representability discussion also defers the important general cases to later study, so sheafification or a rigidified line-bundle description should not be reported as construction of all `P^i`. This independently supports the limited distinction in the first-pass lead MPL_57_271-315 J03 without verifying that lead's underlying scans.

### JAC04 — Theorem 4: ample input does not identify the required polarization

**File/scan:** P57(158), 57:158 L5–25; P57(160), 57:160 L33–42; P57(162), 57:162 L16.  
**Kind:** unpursued implication.  
**Short quote:** “très ample”; “A prouver que cette dernière est positive !” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12; WG H9.  
**Context:** CT, 44:2 Th. 4, L2802–2803, and 44:8–9, L2979–2995; CN 44:2:4 and D13; SN §1, J04.

The current very ample line-bundle and projective-frame passages assume ample input in a Picard classification problem. CT asks whether the particular self-correspondence arising from the cycle construction gives a polarization, and its letter explicitly leaves that positivity unproved. No construction or ampleness argument for this correspondence appears in the selection; the nearby margin “Connu tel quel” at CT 44:2 is therefore insufficient to turn these current passages into a proof or another formulation of Th. 4.

### JAC05 — Theorem 5: intersection calculations are not the proposed height identity

**File/scan:** P57(148), 57:148 L4–20; P57(156), 57:156 L6–18; P57(142), 57:142 L10–46; P57(144), 57:144 L17–33.  
**Kind:** unpursued implication.  
**Short quote:** “(D_h²)”; “forme de Néron–Tate” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12; WG H9.  
**Context:** CT, 44:4 Th. 5, L2849–2874; CN 44:4:1–6 and D12; SN §1, J05.

The reused English surface text compares linear-system dimensions and intersection numbers, while the current curve-family pages construct torsor and cohomology classes. Neither passage supplies CT's pairing of restrictions of complementary cycles to a pencil, its equality with an intersection product upstairs, or its normalization and sign. The manuscript's separate “à vérifier” beside `ξ_n=δ_n(η)` at 57:144 is a different compatibility question and does not verify the height formula. WG H9 therefore remains an unchecked proposed reduction.

### JAC06 — Theorem 6: divisor deformation is a different assertion

**File/scan:** P57(133), 57:133 L5–12; P57(164), 57:164 L23–34.  
**Kind:** unpursued implication.  
**Short quote:** “Div/Pic”; “Le facteur fixe” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12.  
**Context:** CT, 44:4 Th. 6, L2876–2884; CN 44:4:4; SN §1, J06 (reporting 57:309(h)).

The current tangent sequence for `Div → Pic` concerns deformation of an effective divisor and its line-bundle class, not restriction of `P^i(X)` to a generic hyperplane section with the three numerical ranges in CT. Nor does the affine-kernel result for a surjective proper morphism establish that restriction theorem. SN J06 reports a closer divisor-level hyperplane question at 57:309(h), with “bijectif ?” and “conditions à préciser”; that is a lead from another selection, not a verified statement of all three ranges or a chronological predecessor.

### JAC07 — Theorem 7: divisor language gives no unrestricted equivalence statement

**File/scan:** P57(169), 57:169 L8–26; P57(173), 57:173 L3–29.  
**Kind:** unpursued implication.  
**Short quote:** “diviseurs de fonctions”; “L'équivalence numérique = τ-équivalence” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §2.3 #12.  
**Context:** CT, 44:6 Th. 7, L2942–2944; CN D14; SN §1, J07 (reporting 57:275 and 314–315).

The current pages define principal divisors and ordinary line-bundle classes but contain no numerical/τ comparison. SN J07 reports an explicit divisor-level comparison in a different selection, and CN D14 warns against transferring such a statement to arbitrary codimension; neither note was treated as a verified literature result here. CT's broad cycle wording and its unspecified τ-relation must therefore be kept separate from both the current divisor foundations and that reported divisor-level lead.

### JAC08 — Chronology is not supplied by packet order

**File/scan:** P57(143), 57:143 L12–16; P57(141), 57:141 L3; P57(157), 57:157 L4–5.  
**Kind:** unpursued implication.  
**Short quote:** “Massy November 21, 1966”; “Bures le 12.8.1964” (CT).  
**Bears on:** WG2 §2.4 #4; WG2 §1.1 #3.  
**Context:** CT, 44:8, L2970; SN §1, J07 and opening scope statement; `context/README.md`, carry-question discussion.

The dated reused letter at 57:143 is later than the dated cote 44 letter, but its date does not date the neighbouring Picard handwriting. The local titles identify Picard topics without establishing when the individual sheets were written, and the date of CT 44:8 does not itself date CT 44:2, 4, or 6. Consequently neither packet order nor thematic similarity warrants the word “earlier” for the possible connections found here.

## Search record and completeness of the comparison

The literal searches were only navigation aids; their matches were followed by reading the complete source passages. In particular, `P_ξ`, `N`, and `ξ` were compared by their definitions rather than treated as shared objects because their letters agree.

| Check | Search family and follow-up | Actual result |
|---|---|---|
| Current selection | Albanese; Jacobi; Néron/Neron; Hodge; Lefschetz; Matsusaka; Betti; hauteur; pinceau; polarisation; numérique; tau; `P^`, `J^`; then all 43 present individual TeX files | No display of the higher-cycle programme; projective `P_ξ`, Picard kernel N, tangent sequence, and surface intersection calculations are the closest possible false matches |
| Exact cote 44 claims | CT cote 44 in full through the dated letter, especially 44:2,4,6,8–9 | The seven comparison targets and the self-flagged uncertainty are present at the exact lines recorded above |
| Earlier cote 44 notes | CN 44:2:1–5, 44:4:1–6, D08–D14 | Useful warnings about hypotheses and scope; bibliographical theorems not independently checked or used as established results |
| Other same-cote selection | SN opening scope and §1 J01–J07 | Its earlier negative answer is consistent with this independently read selection; its individual scans were not inspected and its closer Th. 6/7 leads remain leads |
| Register | Entire RS, with targeted return to WG2 §1.1 #3, §2.3 #12, §2.4 #4, WG H9, MPL_57_271-315 J03 | The directly relevant entries are plans, a hunch, or first-pass research notes; none is an available proof of the seven assertions |

## Proposed CHECK_EVENTS rows for the root to integrate

These rows deliberately distinguish a **documentary scope comparison** from a proof check. The candidate-note IDs below are provisional until the root gives them final note IDs; no row has been appended to the root's `CHECK_EVENTS.tsv` by this researcher. The background rows do not upgrade the mathematical claims, cited literature, or underlying scans in earlier notes.

```tsv
statement_id	date	who	type	outcome
MPL_57_133-179 JAC01	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: read 57:133 L5-14,135 L16-22,173 L25-29 against CT44:2 Th1 L2787-2790; different Picard-pullback and Albanese-to-cycle-quotient kernels; no earlier form identified and neither theorem proved.
MPL_57_133-179 JAC02	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: read curve-dimension and Div/Pic tangent passages against CT44:2 Th2 and44:8; no uniform higher-cycle Betti bound; P_xi at57:160 L7-19 is projective data, not Alb(S)/N(xi).
MPL_57_133-179 JAC03	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: current ordinary/generalized Picard objects match CT44:8's Pic^0 endpoint but do not display CT44:2 Th3's higher-cycle quotient or complementary duality; representability and cited mathematics not proved here.
MPL_57_133-179 JAC04	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: current very ample/projective classification passages do not construct or prove positivity of CT44:2 Th4 and44:8-9's cycle-induced self-correspondence; no earlier form identified.
MPL_57_133-179 JAC05	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: surface intersection and curve-torsor passages do not state CT44:4 Th5's Neron-Tate/pencil identity; 57:144's a-verifier concerns a different Kummer comparison; WG H9 unresolved.
MPL_57_133-179 JAC06	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: 57:133 and164 do not state CT44:4 Th6's three restriction ranges or fixed-factor claim; SN J06's57:309(h) lead remains unverified at its underlying scan.
MPL_57_133-179 JAC07	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary comparison only: 57:169 and173 provide principal-divisor/line-bundle foundations and no numerical/tau comparison; CT44:6 Th7 retains broader cycle wording and an unspecified tau relation; no truth verdict supplied.
MPL_57_133-179 JAC08	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	used and rechecked in this run	Documentary date check only: P57(143) L12 dates a reused letter1966-11-21; CT44:8 L2970 dates its letter1964-08-12; these dates do not date neighbouring handwriting or all numbered theorems, so no chronology is established.
WG2 §2.4 #4	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	carried as background without fault found	Used as the research question; seven exact cote44 statements compared with all43 frozen current page texts. Bounded negative answer for this selection; planning entry is not a theorem and was not upgraded.
WG2 §2.3 #12	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	carried as background without fault found	Used as unchecked programme orientation; comparison targets taken from exact CT44 statements rather than the register summary; no mathematical assertion in the programme proved here.
WG H9	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	carried as background without fault found	Height/Hodge reduction retained as unchecked hunch; current pages supply neither Neron-Tate normalization nor the particular cycle-induced polarization; no implication from Th5 to Th4 established.
MPL_57_271-315 J03	2026-11-18	ChatGPT GPT-6 Astra Pro / jacobians_earlier_forms	carried as background without fault found	Read supplied first-pass J03 and compared its limited distinction with current ordinary/generalized Picard passages and CT44; prior selection's underlying scans not checked and its mathematics not upgraded.
```

If the root records uses of non-register leads separately, CN 44:2:1–5, 44:4:1–6, D08–D14 and SN J01–J07 should receive background-use outcomes that explicitly say their quoted source passages or external references were not verified here. Their names must not be turned into fictitious RS statement IDs; only MPL_57_271-315 J03 among these J-items is indexed as such in the supplied register.
