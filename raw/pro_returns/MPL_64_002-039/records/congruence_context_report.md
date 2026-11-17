# Cote 64, scans 002–039: infinity question and congruence bridge B5

Research-only report by agent `/root/congruence_context`, 17 November 2026. The frozen transcription was read as text; no manuscript image was inspected and no transcription file was changed. `context/README.md` and `context/notes/RESULTS_STATE.md` were read in full before the comparisons below. The Hua project's modernized transcription was not used.

## Principal finding

The finite level-four material supplies a precise, useful portion of B5: a combinatorial realization of the reduction map from rank-two modules over Z/4Z to their mod-two reductions; the corresponding matrix-kernel representations; the projective octahedron; its determinant/sign characters; and the extra central lifting datum needed to recover a linear module. A particularly precise connection is **cote64 scans027(11),028(16) with the S3-equivariance exercise in `context/LM_140-2_text.tex`, scans568–569(68)**. The supplied prior research notes had already given the equivariant quotient map: **`context/LM_140-2_notes.md`, LM_P057api R17, scan569**, uses A↦(v↦det(v,Av)) and identifies its image with the even-weight plane. This run independently verifies that same finite map and locates it in the current manuscript's canonical summand and torsor construction; it does not claim a first solution of the earlier exercise.

The selected packet does not identify or construct the modular place at infinity announced in the planning context. A mod-four image of the usual unipotent cusp matrix can be compared with the octahedron, but that comparison is made in this report, not asserted as a construction found in these pages. There is no new all-level GT congruence-kernel preservation argument here, and no resolution of the outstanding higher-level kernels or full GT image questions registered in the context.

## Source and status discipline

- `context/LM2_CONGRUENCE_ROWS.md` explicitly calls **every row an unreviewed previous-return claim**. In particular, “Proved,” “Known,” and “Refuted” in LM2 C.r1–C.r3/C.d1 describe that return's own statuses. They are not proof checks performed in this run.
- `context/LM_140-2_notes.md`, LM_P057api R17 (scan569; lines6836–6837 in the supplied file), explicitly credits its equivariant formula to the first-pass model and says “Kept; checked in this pass.” That wording reports the earlier run's own check, not an independent review adopted here; the present finite re-proof and computation are recorded separately under C64.CX02. The introductory paragraph at6782 likewise calls R17 a first-pass model idea, and R17 leaves the matching with the author's labels0,1,infinity unspecified.
- The scan locators for LM2 C.r1–C.r3/C.d1's §39 refer to **`context/LM_140-3_text.tex`**, scans 021–030. The research-return label “LM2” must not be mistaken for the archive filename `LM_140-2_text.tex`.
- `context/notes/RESULTS_STATE.md` is a claims register. LM4_SUCCESSOR B.38/E.10, EXIT_TOWER E.24, and LM7_PUSH E.3 are explicitly recorded as open. LM6 F.43 is a previous-return “Proved” claim without an explicit review annotation. EXIT_TOWER E.49 is explicitly unrefereed/under check; it must not be used to close LM7_PUSH E.3.
- For cote 149 scans 099–101, this context contains **earlier research notes**, not the manuscript transcription or scans. Thus the locators and quoted expressions below are reports in `context/MPL_149_091-136_notes.md`, not new readings of the cote 149 images.
- The finite algebra in `congruence_context_checks.py` and its JSON output is independently checked here. No assertion about an infinite arithmetic image, Tate uniformization, or the correctness of an earlier research return follows merely from those checks.

## Exact evidence map

| Present packet | Context source and exact locator | What the comparison establishes | What it does not establish |
|---|---|---|---|
| 026(1)–(8), 027(10)–(14), 028(16),(19) | `LM_140-2_text.tex`, 568(68), 569 opening paragraph; `LM_140-2_notes.md`, LM_P057api R17 (569) | The canonical summand and torsor construction realizes the equivariant quotient already described by R17; this run independently verifies its finite formula. | A first solution absent from earlier notes, or an action of GT on a whole compatible system of congruence quotients. |
| 033(30)–(32), 034(33), 036(42)–(44) | `LM_140-2_text.tex`, 569(70)–(71), 570(72)–(73) | The current finite group model gives the octahedral action and identifies determinant with orientation. | The earlier proposed modular-curve/Fermat-conic isomorphism or its ramification and descent data. |
| 037(47)–(48), 038, 039(49)–(50) | `LM_140-3_text.tex`, §45, 176(19), 177(20), 178(21); LM2 C.r3 | A clear finite analogue of the passage from a projective action to a central linear lift; the square records information lost by projectivization. | Reconstruction of the full arithmetic extension from its outer action; the earlier text itself admits a modular-comparison check at 177. |
| 033–036 | `LM_140-3_text.tex`, §39, 024–025(8)–(10); cote149 notes RN099-03 | An independently computed unipotent mod-four action is a quarter-turn of this octahedron. | A cusp family, tangential base point, decomposition group, or inertia extension constructed in this packet. |
| 032, 036(42)–(44), 039(50) | `LM_140-3_text.tex`, §39, 022–026; LM2 C.r1–C.r3 | The finite characters can be named and typed accurately before comparison with outer arithmetic actions. | Identification of the mod-two permutation sign with a full GT character, or recovery of a unique adelic multiplier from an outer congruence action. |
| Packet scope 002–039 | `README.md`, B5 question; LM2 C.d1/C.d5; RESULTS_STATE LM4_SUCCESSOR B.38/E.10 | This packet supplies low-level algebraic infrastructure and specific finite models. | An all-N preservation theorem, K5=1, levels7/11, or the remaining adelic image problem. |

## Suggested short notes for the parent to select or adapt

Each proposed note below contains at most four sentences. IDs are **local report IDs**, not replacements for final note IDs. The matching query ID in `congruence_context_searches.json` logs the actual context search, terms, file arguments, and returned hits for each item.

### C64.CX01 — Requested place at infinity: scope of the present packet

**Suggested note (3 sentences).** The planning question in `context/README.md` connects cote64 with the “place at infinity” discussed in cote149 scans099–101; the supplied earlier notes locate the modular-cusp proposal at RN099-03 (099, manuscript p.49, approximately lines17–21, continuing100 lines1–7) and “structure à l'infini” at RN101-04 (101, manuscript p.50, approximately lines11–13). In the present scans002–039, the positive constructions are finite four-set, square, octahedron, and Z/4Z-module constructions, ending in a projective-to-linear lifting question at037–039; no modular cusp construction has been identified in this selection. This is a statement about this packet, not about the remainder of cote64.

**Evidence and caution.** RN099-03 proposes a Tate-curve calculation and cites Tate; this report does not import that argument as newly checked. A whole-packet terminology screen for modular/elliptic/Tate/infinity/inertia/congruence/level/degeneration terms returned only two false-positive substrings in “commutateur(s)” because the screen included `Tate`; the absence screen supports, but does not substitute for, reading the frozen text. The parent read the entire frozen packet; this subtask focused detailed reading on the module and projective-lifting sections.

### C64.CX02 — Earlier equivariance formula and the current canonical model

**Suggested note (4 sentences).** In `context/LM_140-2_text.tex` scans568–569(68), Grothendieck asks to match the S3-action on sl2(F2) modulo scalars with F2^{0,1,infinity}/diag. The supplied prior note `context/LM_140-2_notes.md`, LM_P057api R17 (scan569), already gives A↦(v↦det(v,Av)), whose even-weight image maps isomorphically to the quotient by the diagonal; its “checked in this pass” status remains an earlier-run claim. Here scan028(16) gives the canonical summand sl(M0)=M0⊕F2·id, scan027(11) identifies M0 with F2^J/F2·diag, and026–029 place these representations in the module/torsor model. This run independently verifies the same quotient isomorphism on all48 group/matrix pairs and all64 additivity pairs, without fixing the author's0,1,infinity labelling or establishing LM2 C.d1's all-level GT claim.

**Attribution and present contribution.** R17 already supplies the equivariant quotient formula, so the earlier version of this report's claim that this connection was “previously missed” was too strong and has been withdrawn. The distinct content located in this manuscript packet is the canonical summand constructed from the three reflections fixing the nonzero vectors, and its integration into the module/torsor and groupoid constructions. Our explicit formula [[a,b],[c,a]]↦[δ_(b,c)], with δ_0=0, is the same quotient map as R17: for nonzero p=(b,c), the function v↦det(v,Av) equals1+δ_p on J, and for p=0 it is zero. Thus the present contribution is an independent verification and a precise comparison with the canonical model, not a new quotient identification.

### C64.CX03 — The octahedral group versus the modular curve

**Suggested note (3 sentences).** `context/LM_140-2_text.tex` scan569(70)–(71) tentatively expects SL2(Z/4Z)/{±1}≅S4 and relates its action to an octahedral Fermat-conic cover, while570 explicitly leaves checks of the modular interpretation outstanding. The present scans033–034 construct Δ_M=P(M)(Z/4Z), identify GL(M)/{±1} with the full order48 octahedron group, and036(44) identifies determinant with geometric orientation, thereby furnishing the finite group and character model needed for that expectation. These pages supply no elliptic-curve family or map of modular curves, so they do not independently establish the Fermat-conic isomorphism, its branching, or its arithmetic descent.

**Precision.** The quotient of GL has order48; its determinant-one subgroup is the rotational order24 subgroup. Do not call all of GL/{±1} “S4.” The modular notation in the older passage has primes and base changes that should not be silently stripped away when discussing its unverified geometric proposal.

### C64.CX04 — Projectivization loses a genuine lifting datum

**Suggested note (4 sentences).** At037(47)–(48), the manuscript explicitly asks to lift an octahedron torsor through 1→{±1}→GL2(Z/4Z)→GL2(Z/4Z)/{±1}→1, and038 reduces this to reconstructing a square from its diagonal and codiagonal two-sets. The recap039 says that Δ_M and I_M depend only on P(M), whereas Q_M does not. This gives a finite model for the linear/projective distinction in `context/LM_140-3_text.tex` §45, scans176(19)–178(21), relevant to the typing issue registered as LM2 C.r3. It is not a proof of the earlier arithmetic extension comparison, which scan177 itself says is being admitted pending verification.

**Precision.** A canonical groupoid description is not a preferred splitting: scan032 explicitly says that the displayed product or semidirect-product identifications depend on a trivialization of P_M. Any final reconstruction statement should preserve this distinction.

### C64.CX05 — Own finite comparison: the cusp unipotent is a quarter-turn

**Suggested note (4 sentences).** As an additional comparison, the lower unipotent matrix written for the modular place at infinity in `context/LM_140-3_text.tex` scan025(9) has, at n=1 modulo4, the action (1,0)→(1,1)→(1,2)→(1,3)→(1,0) on Δ_M, fixing the opposite vertices(0,1) and(2,1). Thus its finite image is a quarter-turn of the octahedron from033, with determinant+1 and nontrivial sign on the three mod-two directions. This calculation was independently checked and gives a concrete possible finite test for the cusp comparison proposed in cote149 note RN099-03. It is an observation made in this run; the current manuscript packet does not make the cusp identification, and the older LM passage marks its own unipotent description “sauf erreur.”

**Caution.** The cycle describes vertices represented by primitive vectors modulo±1, not six chosen vectors in the linear module. The fixed opposite pair lies over the mod-two direction(0,1); the other two antipodal pairs are {(1,0),(1,2)} and {(1,1),(1,3)}.

### C64.CX06 — Exactly how far bridge B5 advances

**Suggested note (3 sentences).** The concrete contribution to B5 is the mod-four/mod-two matrix kernel, its S3-module structure, the octahedral projective action, and the central lift recorded at026–039. The packet introduces no GT action on a compatible tower and therefore does not reprove the prior unreviewed claim LM2 C.d1, nor decide LM2 C.d5's remaining image problem. It also supplies no resolution of the higher-level kernels still marked open as LM4_SUCCESSOR B.38 and E.10 in `context/notes/RESULTS_STATE.md`.

**Terminological caution.** EXIT_TOWER D.19 concerns the comparison of full profinite mapping-class groups with their geometric/procongruence images. It should not be silently substituted for the classical arithmetic congruence maps SL2(Z)^∧→SL2(Zhat) or their finite modular reductions.

### C64.CX07 — Keep the three finite characters separate from an adelic multiplier

**Suggested note (4 sentences).** The manuscript identifies the octahedron's colour, orientation, and diagonal-orientation characters respectively with sg·det, det, and sg at036(42)–(44), and relates the corresponding square two-sets at039(50). This supplies precise finite bookkeeping for comparison with the outer congruence actions in `context/LM_140-3_text.tex` §39, scans022–026. In that earlier context, LM2 C.r1–C.r3 explicitly distinguish the unit multiplier of a genuine arithmetic action from the square class visible after passage to outer congruence actions; their stated statuses remain unreviewed previous-run claims here. No equality between the present finite sg and any character on full GT follows without specifying a homomorphism that pulls one back to the other.

**Precision.** The direct current result is a statement about characters of GL2(Z/4Z) and its projective quotient. For N=4 the unit group has trivial square subgroup, but that exceptional finite observation would not recover a unique adelic multiplier at all levels; this report does not use it to strengthen LM2's claims.

### C64.CX08 — Optional record of limits on boundary and CM follow-up

**Suggested note (3 sentences).** The square-lifting problem at037–039 is not yet a boundary normal-line or tangential-base-point construction of the kind recorded as LM6 F.43, and no new arithmetic index or witness test for EXIT_TOWER E.24 is supplied. Nor do the finite characters in this packet decide the full-GT extra-coset question LM7_PUSH E.3. The register's possible resolution through EXIT_TOWER E.49 is explicitly unrefereed/under check and is not adopted here.

**Editorial recommendation.** This optional note is mainly a guard against overclaiming in a programme-level summary; omit it if the final note set already states the packet's scope adequately.

## Independent finite proof details

Let V=F2² and J=V\{0}. The canonical map F2^J→V sends δ_v to v and has kernel the diagonal line because the sum of the three nonzero vectors is zero. For A=[[a,b],[c,a]]∈sl(V), set p(A)=(b,c), and let ψ(A) be the class of δ_(b,c), with δ_0=0. In the quotient, [δ_u]+[δ_v]=[δ_(u+v)], so ψ is additive, its kernel is the scalar line, and it is onto a group of order4.

There is also a basis-free proof of equivariance, independently derived here and already present in equivalent form in LM_P057api R17. The two-dimensional F2-space has a unique nonzero alternating form ω, preserved by GL(V); p(A) is characterized by ω(p(A),x)=ω(x,Ax). Trace zero makes the right side an F2-linear function of x, and this characterization makes p(gAg^-1)=g p(A). The computational check exhausts all6 elements of GL2(F2), all8 trace-zero matrices, and all64 matrix pairs for additivity; an added eight-case comparison checks directly that R17's even-weight function has the same quotient class as ψ. This verifies precisely the finite quotient identification in C64.CX02, not the entire category equivalence stated by the manuscript or the earlier note's author-label matching.

For C64.CX05, the program enumerates the12 primitive vectors of (Z/4Z)² and their6 classes modulo±1, then computes the action of L=[[1,0],[1,1]]. The cycle decomposition is two fixed points and one4-cycle, and L has order4. Reduction modulo2 swaps two of the three nonzero vectors; det(L)=1 modulo4. The interpretation as a quarter-turn uses the antipodal pairs defined by the reduction map in scan033.

## Output and audit files

- `records/congruence_context_report.md`: this report.
- `records/congruence_context_checks.py`: reproducible independent finite checks.
- `records/congruence_context_checks.json`: successful check output.
- `records/congruence_context_searches.py`: reproducible targeted context queries, plus a scope-limited terminology screen of the frozen packet.
- `records/congruence_context_searches.json`: complete query arguments and hits, keyed to every suggested note.
- `records/congruence_context_events.tsv`: check-event fragment for the parent to merge/adapt; previous-run statuses are preserved as background, and the two new finite checks have their own entries.

No final research notes, frozen page files, combined transcription, images, or context sources were changed. No external literature was opened; previous notes' bibliographic assertions, including Tate uniformization, are carried only as explicitly identified context leads.
