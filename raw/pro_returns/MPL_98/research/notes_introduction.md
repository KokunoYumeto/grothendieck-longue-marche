# MPL_98 — Research notes

## Evidence and limits of the comparison

These notes concern **98.pdf, scans 002–044**, the complete 43-page supplied range. The diplomatic transcription was frozen at **2026-11-18 01:36:35 UTC**, after one sequential reading of every whole scan and both halves, a second visual audit of every page, and a reconciliation of recurring notation. No OCR was used on the supplied manuscript images. The 43 individual fragments and combined fragment are covered by 44 SHA-256 hashes; the final verification is recorded in progress.log.

The root performed all manuscript reading. Research collaborators worked only after the freeze, on the supplied context, published literature, and mathematical arguments; they did not inspect the scans or independently transcribe pages. Mechanical validation establishes that all 43 fragments are present, the 694 inventory rows are marked transcribed, the combined fragment matches them, and the syntax harness compiles; it does not certify every reading or the mathematics. The doubt register records the remaining uncertainty, especially in the pencil and crowded marginal passages.

**Context keys.** “Hua98” means Michel Hua’s project’s AI-produced modernized reading in the supplied **hua_project/98.modern.tex**, accompanied by **hua_project/README.md**. Its page n is our scan n+1. “RS” means the supplied **notes/RESULTS_STATE.md**, and “README” means the context package’s README.md, not the deliverable README. All four supplied context members were read after the freeze. The source packages are not copied into this return.

Hua98 is credited whenever a note uses its reconstruction, added proof, or proposed link. It is neither a diplomatic witness nor an established-result source. In particular, a mathematically convenient reading cannot replace a frozen letter, subscript, deletion, or incomplete sentence. The reading questions at the end of the numbered notes record those differences without changing the transcription.

Each note identifier keys an actual context search in **research/context_searches.jsonl** and **research/note_plan.json**, recording the query, time, and matching file/line locators; relevant matches and their manuscript scan correspondence are identified in each note. A search hit is not a proof, and an absent substantive match is stated rather than filled with an invented connection. The note bodies contain one to four sentences; longer proofs and counterexamples are in the research memoranda and **research/root_proof_checks.md**.

### Register-status key

| Key or entry | Status supplied by the context | Treatment in this run |
|---|---|---|
| **RS–Ø** | RS Orientation expressly says that no own established result directly matches these norm, cohomology, or bounded-family subjects | No settled result is silently assumed; source comparison, independent proof, or an explicitly limited background use is recorded as appropriate |
| **H98 = Hua, findings register, 98-axiomatic-norms-can-section** | **conjecture (unsearched); Lean card: partly proved; intake: new to us** | Finite locally free scheme and finite-fibre G-set models checked; degree/empty-target refinement identified; the Lean files and certificates were not supplied or run |
| **LM7 E.23; FLAGGED_149 B9; LM1 D.11; LM4 D.12; LM4 F.7** | **Open**, originating returns’ claims | No solution or refutation is claimed; G11 and the disposition table below explain the limited bearing |
| **LM7 C.1; LM7 C.5** | **Known / Proved**, originating returns’ claims | Related Picard/Jacobian background only; the original result files and arithmetic claims were not checked |
| **WG H9; WG H2; WG2 entries** | Unchecked planning guesses or questions | Not promoted to mathematical evidence |
| Other returned-package notes, including **MPL_131 RN001 / §2 / 10** | First-pass leads | Compared only to the supplied summaries; their underlying manuscripts and return files are absent |

RS separately lists a reviewed chain in the GT programme, but none of the checks here relies on that chain. The absence of a direct application is consistent with RS’s own package orientation. No result status in the user’s register has been edited.

### Principal findings and their scope

| Finding | Notes | Qualification |
|---|---|---|
| The top alternating-image construction works integrally | N01–N02 | The full sign-eigenspace is a different object and can be too large in characteristic two |
| A single numerical degree conflicts with arbitrary empty-target base change | N10–N11 | The source’s degree-predicate wording and Hua’s reported hasDeg formalization suggest the refinement; no formal code was checked |
| The finite-orbit G-set site needs an enlarged setting for some Čech nerves | G01–G07 | This concerns abstract groups; continuous profinite actions require their own category |
| The \(G_m\) sequence has a precise conditional reconstruction | G08, G13 | The field setting can satisfy Picard vanishing; the conic counterexample concerns one fixed non-field cover |
| Bounded cycle degree does not bound even pure fixed-quotient sheaves | B02, B31 | \(\mathcal O(n)\) on \(\mathbf P^1\) is explicit; attribution to the faint tentative statement remains conditional |
| Relative field embeddings cannot be ignored | B05–B11 | An arbitrary compositum is not interchangeable with a suitable witness |
| The Tor proof uses the wrong resolution ring in one step | B18, B20 | A polynomial-algebra resolution repairs the proof under stated finiteness hypotheses |
| Input flatness is actually present in the frozen Tor lemma | B19, R09 | The counterexample proves its necessity; it does not expose an omission in that lemma |
| “En tt degré” is defensible for the truncated Hom complex | B22–B24 | Only the subsequent identification with Ext is restricted to \(p\le N\) |
| The reused typescript has a full-rank homogeneous-system error | T06–T07 | The preceding-prefix repair is confined to the notes |

The boundedness arguments below use finite type schemes over noetherian bases and coherent sheaves unless a note explicitly changes that scope. Properness, finite presentation, input flatness, finite degree ranges, and the choice of coefficient ring are kept separate. The counterexamples are checks made in this run, not claims of novelty.


