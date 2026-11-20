# Scan 005 — text-only consistency audit

**Result: structural/textual match; not ink verified.** Compared `main_observations.md` decisions 1–37 with `pages/H104-01_104_scan005.tex`, original `reader_inputs/scan005/C.tex`, and all three returned `reading.tex` files and issue reports. No image was viewed, no rendering or compilation was performed, and no reading was independently decided. No page or decision file was changed. No substantive returned-text difference remains outside the recorded adjudications.

## Original C uncertainty coverage

Original C contains **39 `\unsure` occurrences**. All are either retained, revised, resolved, or replaced by an unassigned literal trace in accordance with the main observations. Numbers below follow their order in original C, not the main decision numbering.

| C doubt(s) | Final page text or treatment | Main decision(s) |
|---|---|---|
| 1–2: first F alphabet and index | `\mathbb F_{\unsure{n-2|n\,2|n-1}}` | 1 |
| 3: terminal point/comma | Literal cross-like TikZ trace; comment: “no securely assigned lexical/algebraic value” | 2 |
| 4: mark after struck D | `\deleted{D_n}\,\raisebox{1.1ex}{\(\cdot\)}`; point outside deletion | 5 |
| 5: low `E_3` | `\unsure{E_7|E_3|\xi}` | 6 |
| 6–7: first/last argument parentheses | `t_n\unsure{y|f})` and `s_n y)`; following arguments use first candidate `y` | 6 |
| 8–11: isolated stroke, small s/t, struck u | `\unsure{1|\prime}`, `\unsure{s|f}`, `t`, `\deleted{u}` | 8 |
| 12–13: struck verb and old s | `\deleted{si on \unsure{retient|retire}}`, `\deleted{s}\exists` | 9 |
| 14–17: donner, first u index, inserted v index, de/dans | `se donner d'avance`, `u_{\unsure{i|i-1}}`, `\inserted{\(v_i=\)}`, `\inserted{de \(F_{i-1}\)}`; no following inserted comma | 10 |
| 18–20: struck de and first equality indices | `\deleted{de} que`; `f(u_{\unsure{\cdot|i|1}})=u'_{\unsure{i|1}}` | 11 |
| 21–24: resp, function and v/v′ indices | `\inserted{\unsure{rp|resp}}`, without period; `\unsure{g|f}(v_i)=v'_i`; explicit comment carries the `i/1` doubt from u′ | 11 |
| 25–27: struck que, NB, final function | `\deleted{que}`, `(NB on n'exige pas que \(g(u)=u'\))`; explicit comment preserves the preceding `g/f` uncertainty | 12 |
| 28–29: first level and circled letter | `\unsure{\Xi|E}_0`, circled `\unsure{\mathrm b)|\mathrm a)}` | 14 |
| 30–32: struck surj, leading dash, live surj | `\deleted{\pi_0(f)\ \unsure{\text{surj}}}`, `-\pi_0(f)\ \text{\uuline{surj}}` | 15 |
| 33–34: lifted-arrow label and struck witness | `\ell` in the literal shaft drawing; `\deleted{\unsure{w|\exists\,w|u}\in F_2}` | 23–24 |
| 35–36: cancelled F alphabet and first c source index | `\deleted{\forall s,t\in\mathbb F_0,}`, `s_i(u)=s_1(v)` | 26 |
| 37–38: cancelled f and c pi index | `\deleted{\unsure{f_1|f}}u\mathbin{-}v`, `\pi_{\unsure{f|1}}(f)` | 28 |
| 39: cancelled et/f | `\deleted{\text{et}}` inside the local rule/cancellation drawing | 35 |

The repeat conventions are implemented: first `y|f` followed by y; first `\Xi|E` followed by `\Xi_1` with an explicit comment; first `g|f` at v followed by g in NB with an explicit comment; the point/i/1 doubt on the first u remains distinct from the following `i|1` family. The live `plus` is outside `\deleted{de}`. The final c′ t relation is exactly `t_1(u)\mathbin{-}t_1(v)`, and the c pi index remains `f|1`; neither is repaired mathematically.

## Markings and drawing coverage

These items require inventory/omission coverage even when their words or formulas are already represented in a larger block:

| Item | Original C → final page |
|---|---|
| Circle around first b/a, b′), c′ | Retained; final has three `\textcircled` uses. b′ keeps its closing parenthesis; c′ has none. |
| Double underlines | Retained on live `surj` after `\pi_0(f)` and on `\pi_1(f) surj`. Reader A's proposed underline under the first s′ is absent, as expressly rejected by decision 14. |
| Two points above-left of C_i | Added as `\fill (-.5,.65) circle (.025)` and `\fill (-.35,.57) circle (.025)`. |
| Detached traces below chain | Added as a separate TikZ figure. |
| First chain connector | C's ordinary arrow replaced by separate curved-head and shaft paths; terminal trace retained without a punctuation reading. |
| Two oblique segments below first t_n; low right dash | Added as separate `\draw` paths; neither receives a lexical interpretation. |
| Low trial bracket and 0 | C's semantic `\underbrace` replaced by the low traced bracket and bare `0`. |
| Long C_i side brace | **Exact original C path retained unchanged**, per the main reader's implementation instruction; no claim that a proportion adjustment was implemented. |
| Point after existential F_i | Added as `\exists w\in F_i.`. |
| Wavy stroke on b′ arrow | Drawn across the arrow shaft, with ell above; not a detached sim below. |
| Six vertical memberships | All final occurrences use `\rotatebox{-90}{\(\in\)}`. |
| Rule beneath cancelled et | Added as a low `\draw` path with a downward local return; not treated as emphasis. |
| u/v and lower sketches | Separate endpoint geometry is encoded. The lower sketch has `\unsure{fu)|f(u)}`, a headless upper arc, one short lower return, separate w and prime around the down arrow, and three `\fill` points. |
| Final pi grouping | C's `\overbrace` replaced by the recorded top/left boundary and a separate lower `surj` node. |

Other A/B/C disagreements are explicitly covered by the main decisions, including the top alphabet/index, plain array F_1, low E_7/E_3/xi alternatives, first circled label order, primed F_1 at level 0, doubled b′ F_0, all four lower F_2 alphabets, the c′ single t dash, and the lower label/arc. The discarded scan-006 H drawing is not used as scan-005 evidence. Pale background and archive number appear only in the final page's comments.

No `decision_draft` was present when this audit was written; that separately built record was not audited here. This report certifies textual consistency only, including the presence of drawing instructions, not their visual fidelity or rendered layout.

## Addendum — one-pass decision-draft check

Subsequently inspected `decision_draft.json` (88 loci) against the same text sources. No image, rendering, or compilation was used. Alternatives formatting and inventory ordering were excluded from this check as instructed.

**Concrete record gap:** the `readers` fields at the six vertical-membership loci do not fully state the returned `.tex` difference. At **005A52, 005A58, 005A66, 005A67, 005A74, and 005A76**, both A and B actually use `\rotatebox{90}{\(\in\)}`, while C-reader uses `\rotatebox{-90}{\(\in\)}`. Generic summaries such as “vertical membership” and “turned membership” omit the decisive orientation disagreement. Those fields should explicitly record **A: +90; B: +90; C: −90**. At the four lower loci, C-reader's actual alphabet should also be stated: **005A66/005A74: plain `F'_2`; 005A67/005A76: plain `F_2`**. The final page and the main decisions already contain the adjudicated −90 orientation and doubled lower alphabets; this gap concerns the exact three-reader record, not the page transcription.

Other results of this pass:

- All **80 A, 89 B, and 83 C issue IDs** are mapped, including the two excluded metadata/background records. No unknown source ID or altered `reader_evidence` quotation was found.
- There are no duplicate decision IDs. The four reused source references split distinct features rather than duplicate the counted locus: B34 covers prose/deletion (005A31/32); B60 covers level glyph/circle (005A55/56); B71 covers membership/target (005A67/69); C `c_oldf_target` covers cancelled glyph/live target (005A68/69).
- The **24 `unresolved=true` loci** correspond exactly to the 24 `remaining` decision IDs. Main-retained doubt on cancelled `surj` is correctly preserved despite all readers resolving it. Repeated Xi/E, g/f and i/1 uncertainties are correctly retained without requiring a repeated macro in the page.
- No incorrect `diff_C` or `diff_H` flag was identified under the draft's stated counting policy. C uncertainty resolution, pruning, extension and reordering are counted; unchanged side-brace geometry, unchanged headless connectors, and equivalent placement syntax are not counted as C changes.
- No concrete `marked_in_H` error was identified. Local `\ill{}` placeholders are distinguished from unmarked omissions, live incorrect readings, and H's broad editorial notes. In particular, the final unprimed w asserted by H's editorial note is correctly `marked_in_H: no`.

The decision file was not modified. The narrow reader-mapping gap above was sent to the main reader for correction.
