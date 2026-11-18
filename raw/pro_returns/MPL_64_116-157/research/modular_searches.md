# Search and comparison evidence: modular track

Author: GPT-6 Astra Pro; effort inherited, runtime value not exposed. Date: 2026-11-17 UTC. This records targeted context retrieval and limited mathematical checks, not a second transcription pass.

## Intake and scope

`README.md` and all of `notes/RESULTS_STATE.md` were read before substantive context comparison. The intake identifies cote 64 with the announcement in cote 149 scans 099–101 and bridge B5, expressly treating the LM2 return rows as claims; the result register similarly marks prior returns as claims unless a review is explicitly identified.

Frozen text was read in detail for scans 116–121 and 139–152; scans 153–157 were subsequently read to check the nature of the final arithmetic section. A supplementary search covered all 39 page files, and section starts in the intervening pages were checked; this agent does not claim to have independently reread every line of scans 123–138. No manuscript images or Hua transcription were used for this track.

## Per-note context searches

| Note | Search / retrieval actually performed | Located context and result IDs | Comparison outcome |
|---|---|---|---|
| B01 | Searched `RN099`, `RN100`, `RN101`, `RN103`, `Tate`, `splitting`, and `weights` in `MPL_149_091-136_notes.md`; then read the exact RN099-03, RN101-01, RN101-04 and RN103-05 entries. Extracted `LM_140-2_text.tex` scan 517 by its scan marker. | Cote 149 RN099-03: scans 099–100, proposed modular cusp; RN101-01: scan 101, non-realizability inference; RN103-05: scan 103, earlier Tate residue-action obstruction; `LM_140-2_text.tex`, §37, scan 517, elliptic family over U0,3. | **Adds** analytic uniformization to that family comparison; **differs** from the arithmetic cusp calculation and residue-action test. The earlier obstruction is carried, not newly reviewed. |
| B02 | Searched the frozen pages for `\\tau_\\infty`; read scans 147–150 and extracted `LM_140-3_text.tex` scans 24–26. Read `LM_140-3_notes.md`, second pass for scans 21–30, notes 10–13 and E. | Current matrix involution; §39 scan 25's genuine inertia source T_infinity; `LM2_CONGRUENCE_ROWS.md`, LM2 C.r2. | **Differs**: an involution changing conventions is not a procyclic cusp-inertia source. No inferred contradiction. |
| B03 | Read current scan 145 and scan 147's displayed actions; searched/read the unipotent claim in `LM_140-3_text.tex`, scan 25, and note 10 in the associated notes. Revisited RN099-03. | §39 scan 25 equation (9), lower-unipotent image; cote 149 RN099-03, scans 099–100. | **Adds** an elementary analytic monodromy witness and **restates** the same unipotent subgroup shape up to basis and generator. Arithmetic enhancement not established. |
| B04 | Searched `Legendre`, `échelon`, `C.d1`, `C.r1`–`C.r3`, `B.38`, `E.24`; read `LM2_CONGRUENCE_ROWS.md` in full, `LM_140-2_text.tex` scans 527–528, and notes R24, R28–R29. | LM2 C.d1 and C.r1–C.r3; LM4_SUCCESSOR B.38 (B.5); EXIT_TOWER E.24 (cote 143 §9 scans 29–33); LM §37 scans 527–528. | **Adds** a level-4 pinning construction problem; **differs** from the all-level preservation and exact arithmetic-image claims. Current scan 121 expressly postpones a necessary condition. |
| B05 | Searched `Torelli`, then extracted `LM_140-3_text.tex` scans 20 and 28–30; read corresponding notes 23–27. | §38 scan 20: integral framed lattice; §39 scans 28–30: Pi(2m), reduction modulo 2m, and the equivalence question; LM2 C.d1. | **Restates** the integral geometry and **adds** the explicit reduction-of-frame check; no identification of the projective Legendre quotient without further choices. |
| B06 | Read `LM_140-3_text.tex` §39 scans 22–26 and associated first-pass notes 4, 9, 12–14, own notes C and E; matched `LM2_CONGRUENCE_ROWS.md`. | LM2 C.r1–C.r3, arithmetic outer image and unique-multiplier correction; §39 arithmetic-extension diagram and square-class map. | **Differs** in type of action: current matrices are geometric; context introduces arithmetic extension and outer quotient. **Restates** the pre-existing distinction without re-proving those return claims. |
| B07 | Searched `congruence` in `LM_140-2_notes.md` and `D.19` in `notes/RESULTS_STATE.md`; read the scan-320 own note D and the relevant registered row; compared §39 scan 24 equation (7). | `LM_140-2_notes.md`, scan 320 own note D (literature check left open); EXIT_TOWER D.19; LM2 C.d1. | **Differs** between classical homological congruence and nonabelian procongruence. **Adds** the precise primary-paper verification for type (1,1), without auditing all of EXIT_TOWER D.19. |

## Evidence and limits of the negative findings

A case-insensitive search over all 39 frozen page files found zero instances of the standalone words `Tate`, `inertie`, or `Galois`, zero stems `cyclotom` and `congruence`, and zero matches for `GT_?0`. It found the sole expression `\\exp(2i\\pi\\tau)` on scan 145, and 13 lines containing `\\tau_\\infty` across scans 147, 148, 150 and 151. These counts are supporting retrieval evidence, not a proof of mathematical absence by themselves.

The substantive negative evidence is the actual sequence of constructions: scan 145 supplies a smooth analytic lattice family and its multiplicative uniformization; scans 146–150 compute changes of frame and identify the discrete modular group; scans 151–152 add differential framing and discuss stabilizers; scans 153–157 discuss quadratic-cover normality, with no exhibited elliptic degeneration or local fundamental-group action. In particular, none of those read passages gives a fiber at q = 0, an identified local arithmetic field, a local/global inertia map, or a residual Galois action. The supplied fragment excludes earlier cote 64 pages, so this does not prove that no such computation occurs anywhere in cote 64.

For B5, scan 117 explicitly identifies level 4, scan 118 states the desired canonical functorial Legendre pinning, and scan 121 explicitly postpones condition c. The later integral framing supplies matrices, but the context's specific projective kernels Pi(2m), their full GT₀ preservation condition, and arithmetic-image problem are absent from the read construction. Hence no registered open status is changed merely because level structures and SL2(Z) appear.

The context has notes on cote 149 rather than its complete verified transcription; the assigned line locators and short quotations from cote 149 are therefore identified as locators in those notes. No stronger claim about reading the original cote 149 manuscript is made.

## Limited mathematical checks performed

1. For g = [[a,b],[c,d]] with ad − bc = 1, multiplication by R = diag(−1,1) on both sides of g inverse gives R g inverse R inverse = [[d,b],[c,a]]. This checks the convention identity only.
2. Over the analytic q-loop, the periods (1,tau) transport to (1,tau + 1). With columns as coordinate vectors, the action is T = [[1,1],[0,1]]. Exact integer matrix multiplication in Python gave S T S inverse = [[1,0],[−1,1]] for S = [[0,−1],[1,0]].
3. E_tau[N] is (N inverse times the period lattice)/(the period lattice). A basis change fixes both of its displayed basis classes if and only if its two columns agree with those of I modulo N, which is precisely membership in Gamma(N). This does not identify an arbitrary pinning moduli problem with that full-level moduli problem.
4. Bux–Ershov–Rapinchuk's theorem applies to Out(F2) = GL2(Z); the orientation-preserving SL2(Z) subgroup has finite index, so its profinite topology is induced from that group and the restriction remains injective. This step transfers the quoted theorem to the present discrete mapping-class group, while keeping the homological quotient SL2(Zhat) separate.

## Literature verification record

| Primary or author document | Exact URL | Locator checked | What it supports / does not support |
|---|---|---|---|
| Tate (1995), author manuscript | https://people.math.harvard.edu/~ctm/home/text/others/tate/tate-unif/tate-unif.pdf | Internal p. 19; internal pp. 22–23 | Torsion extension and arithmetic modular cusp model; used to specify missing ingredients, not to attribute an unwritten argument to cote 64. |
| Bux, Ershov, & Rapinchuk (2011), author PDF | https://m-ershov.github.io/Research/asada_final.pdf | §1, pp. 1–3; Main Theorem and Corollary on p. 2 | Nonabelian congruence definition and faithful completion map; explicit contrast with the usual linear congruence property. |
| Bux, Ershov, & Rapinchuk (2011), publisher | https://ems.press/journals/ggd/articles/4445 | “Cite this article”; dates and DOI | Publication metadata, pp. 327–353, DOI 10.4171/GGD/130; author-PDF page locators deliberately distinguished. |
| Hain (2021), revised author notes | https://sites.math.duke.edu/~hain/teaching/mth790/hain_final_rev_2021.pdf | Title-page date; §4 opening, pp. 29–30 | Direct analytic q-chart and orbifold cusp description; no arithmetic Galois comparison. |

Web search used the standard search engine for discovery and the stronger engine where an official/primary metadata lookup needed verification; all mathematical statements used in this track were checked in the linked author documents, not taken from secondary search-result discussions. Tate's book metadata was cross-checked against the supplied bibliography and bibliographic citations, while the actual torsion/cusp material was read in Tate's own text. No direct technical quotation from a web document is used in the note bodies.
