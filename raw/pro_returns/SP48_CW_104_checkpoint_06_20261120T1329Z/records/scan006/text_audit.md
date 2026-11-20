# Scan 006 — independent text audit

**Result: PASS for source coverage, C-doubt accounting, difference flags, and implementation of all 25 main observations. No concrete mismatch remains.**

## Scope and authority

This was a clerical text/code audit. The authoritative ink choices are the 25 numbered entries in `records/scan006/main_observations.md`. I read the scan006 C/H witness texts and C context, the actual H drawing code, all three readers’ `reading.tex` and report data, the complete crosswalk and witness doubt table, the assembled page, and the decision draft. I opened no image, crop, PDF, other scan text, or web source; used no OCR; and did not compile or render LaTeX or check the mathematics. I changed only this audit file.

The source-side cross-page remarks in C_context remain witness assertions. They supply no independent evidence. Reader C’s raw prose/notation claims do not override the main choices: in particular the leading computation relation, retained g alternative, F2 alphabet, new detached points, and refined trace gaps follow the main observations.

## Coverage and counting

| Check | Audited result |
|---|---|
| Reader source issues | A 64/64; B 64/64; C 71/71; total 199/199 |
| Crosswalk physical/scope records | All 86 have a final destination; none pending |
| Final decision rows | 90 unique IDs |
| Remaining uncertainty records | Exactly the 21 decision IDs whose unresolved flag is true |
| Inventory | 51 selected rows, including all new literal marks |
| C inline doubts | All 38 literal unsure macros match witness_doubts by original line and candidate text |
| C doubt dispositions | 27 substantive changes; 11 retained/shared doubts |
| Main observations | All 25 represented by page code, decision evidence, and inventory coverage |
| Reader alternatives | A, B, and C entries present at every final issue and nontext record |

The crosswalk raw source index preserves every original report issue field exactly, using the identifier as its dictionary key. The final source maps contain exactly the report ID sets, every source issue has a nonempty destination, and all destination IDs exist. Broad source issues legitimately map to multiple smaller physical loci. Those mappings do not add counts on their own.

| Witness | High | Medium | Low | Total differences |
|---|---:|---:|---:|---:|
| C | 35 | 12 | 6 | 53 |
| H | 52 | 14 | 13 | 79 |

These totals were recomputed from the final issue flags, rather than copied from reader totals. The following boundaries prevent duplicate counts:

- The residual typed-strip omission excludes the separately represented 0/O and n–N gap. The omitted amountsto belongs to the residual passage once.
- The broad marginal-chain scope is supporting metadata, without a second count over its labels, signs, cancellations, and placement decisions.
- The array’s pair of memberships is one arrangement discrepancy against H. Common-D vertical placement is a C change; H already centers its common D beside the two-row array.
- The wholly canceled left connector cluster is one locus. Its cancellation and the removal of a falsely surviving live connector are not counted separately.
- The lower-arc medial gap is included in the paired-arc decision. The right-arm interruption of the broken V is included in the V-geometry decision.
- The F1 and F2 alphabets and the detached first lower arrowhead are distinct physical loci.
- The lower x/y connector and labels exclude the separately added y-prime point; the lower rising-arrow sketch excludes the separate low segment.
- H’s closed loop path and filled shared vertex are one geometry discrepancy. H’s prose caption is not another count.
- H’s omitted hom.topie phrase includes its terminal stop. I69 carries that H difference; I70 is a separate punctuation change against C only.
- Archive 5, editorial title information, and background recovery limits remain metadata, without manuscript-content difference counts.

## C-doubt audit

Every removal, resolution, candidate refinement, addition, or reordering has diff_C=true. Shared same-page marker consolidation alone has diff_C=false. C15 is a deliberate distinction: its u doubt is retained, while its physical placement over the shaft changes, so the locus has diff_C=true for placement.

| C doubt | Decision | Disposition | Doubt changed | Locus diff_C |
|---|---|---|---|---|
| C01 | 006L02 | retained | no | false |
| C02 | 006L05 | resolved to doubled D | yes | true |
| C03 | 006L06 | reordered to script N first | yes | true |
| C04 | 006L08 | retained | no | false |
| C05 | 006L11 | resolved to doubled I | yes | true |
| C06 | 006L12 | resolved to canceled N | yes | true |
| C07 | 006L14 | resolved to croissante | yes | true |
| C08 | 006L15 | equals alternative removed | yes | true |
| C09 | 006L17 | less-than-n alternative added | yes | true |
| C10 | 006L19 | resolved to J | yes | true |
| C11 | 006L20 | all eta/g/y alternatives retained | no | false |
| C12 | 006L21 | eta/y retained through shared marker | no | false |
| C13 | 006L23 | retained | no | false |
| C14 | 006L24 | x alternative added | yes | true |
| C15 | 006L25 | u doubt retained; only physical placement changes | no | true |
| C16 | 006L26 | local xi/x retained through shared marker | no | false |
| C17 | 006L28 | retained | no | false |
| C18 | 006L29 | local xi/x/f retained in that order through shared marker | no | false |
| C19 | 006L32 | refined and reordered to downarrow/I/= | yes | true |
| C20 | 006L33 | resolved to canceled D | yes | true |
| C21 | 006L39 | resolved to ens | yes | true |
| C22 | 006L40 | resolved to famille | yes | true |
| C23 | 006L42 | resolved to ordonnés | yes | true |
| C24 | 006L44 | resolved to canceled phi | yes | true |
| C25 | 006L45 | tau removed and K added, k first | yes | true |
| C26 | 006L47 | Soit/Sinon retained | no | false |
| C27 | 006L49 | resolved to canceled K | yes | true |
| C28 | 006L50 | resolved to Phi | yes | true |
| C29 | 006L52 | tau removed and K added; uncertainty shared at first label | yes | true |
| C30 | 006L54 | resolved to n-prime | yes | true |
| C31 | 006L56 | resolved to Considérons | yes | true |
| C32 | 006L58 | tilded D_n-prime / D_n retained in order | no | false |
| C33 | 006L59 | doubled B added between ordinary and script B | yes | true |
| C34 | 006L66 | resolved to asterisk | yes | true |
| C35 | 006L67 | resolved to ens | yes | true |
| C36 | 006L68 | resolved to classes | yes | true |
| C37 | 006L69 | resolved to hom.topie with its internal point | yes | true |
| C38 | 006L71 | resolved to lacets | yes | true |

The local repeated limits are preserved explicitly: eta/y above the middle J, xi/x above the final J, and xi/x/f at the lower endpoint. The first live xi/f/x marker does not silently reorder the endpoint’s local record. The later k occurrence retains k/kappa/K; its removal of tau is substantive and remains counted against C even though its marker is shared.

## Implementation against all main observations

This comparison inspected actual TeX/TikZ code, including path separations and filled marks. Comment labels alone were not accepted as implementation.

| Main | Audited page content |
|---:|---|
| 1 | Literal complete type; both completion signs; shared 0/O; amountsto; blank n–N gap; period before close parenthesis. |
| 2 | Isolated doubled D; script-first N/plain-N doubt; direct mapsto; canceled I_n/D_n; live plain tilded D_n. |
| 3 | Three separately encoded rightward arrows, upper/middle/lower; single prime on source index. |
| 4 | Arrow ends over n in its own cell; membership/doubled I are to its right; detached triangular point is an actual filled path above I. |
| 5 | Canceled plain N; both live upper I forms doubled; croissante resolved; est/subset without equals; canceled in-n/<n before live <=n. |
| 6 | Low multiplication dot, denominator and powers retained; uninterrupted continuation dash; actual unsure{>/=} followed by unfinished final equals. |
| 7 | J chain, both memberships rotated -90; eta/g/y retained; xi/f/x extended; canceled labels and old index retained; diagonal unsure-u uses description/sloped/fill=none over its shaft. |
| 8 | Literal u_xi u_eta= with no right member; subscripts inherit the retained shared ambiguities. |
| 9 | Actual short curved path with a slightly raised left entry; no assigned symbol. |
| 10 | Actual separate point about one-fifth of total stroke length left of its start; uneven trace, narrow weak interval, and disconnected angular down/up terminal fragment. |
| 11 | Separate plain tilded D_n-prime to D_n map precedes the x/y array. |
| 12 | Strict comparisons; one deleted downarrow/I/= cluster without live left connector; two headless right connectors; separate dot; two memberships; resolved deleted D over one common live D between levels; n-double-prime lies on the upper arc; lower arc is two separate paths; two filled points remain. |
| 13 | Plain I ens ordonné; actual isolated filled point before n mapsto; famille d’ens ordonnés; comma/semicolon doubt retained. |
| 14 | Deleted phi resolved; k/kappa/K doubt retained without tau; actual detached oblique path above-left of the label. |
| 15 | str. croiss. has both stops and no comma; image plain I_<=n; actual filled point below-left of I baseline. |
| 16 | Whole uncertain Soit/Sinon l’ens K opening canceled; K resolved; following live Soit capitalized. |
| 17 | Phi_n-prime,n subset plain tilded D_n; rotated vertical equals at the left under the name; actual point above-left; no extra comma; later k retains shared k/kappa/K uncertainty. |
| 18 | Canceled Soit x in Phi_n-prime and its trailing comma; one prime, no added second index. |
| 19 | Considérons resolved; l’ens without stop; old D alternatives retained in order; live B/mathbb-B/script-B alternatives retained. |
| 20 | Plain F0, doubled F1 and F2; four leftward arrow paths; lower first head is a separate curved path with positive gap to the shaft, while the other heads meet their shafts. |
| 21 | Separate plain x; literal open contour with separated left ends; upper inward/down-left head; lower upright and curved-left returns; no filled joining vertex or asserted second head. |
| 22 | Headless connector with primed x and y; y and its prime remain distinct glyphs; actual filled point is below-left of the prime tick and right of the y body. |
| 23 | Three filled points; rising curved path and two explicit upper wings; disconnected low segment with downward left return and headless rounded right end. |
| 24 | Three actual drawn paths: descending left arm and two separated pieces of the rising right arm. Both the central break and right-arm interruption are preserved. |
| 25 | Literal pi_0(F_*,x); ens and classes resolved; d’hom.topie. includes internal and terminal stops; lacets en x on second line. |

## Divergent readers retained in the record

The draft retains the specific competing returns where they differ: B’s script-first N; A’s retained equals alternative after image; B’s expanded old image qualifier; A/C’s pruned g versus B’s retained g; C’s added x in the second marginal label; three differing canceled array-cluster readings; B’s arc-label placement; C’s common-D placement and array point; B’s initial family-line point; C’s comma/semicolon doubt; C’s resolved phi versus A/B uncertainty; B’s resolved k versus A/C uncertainty; A’s still-doubtful subset capital versus B/C’s Phi; A’s doubled F2 versus B/C plain F2; B’s literal open contour versus the A/C loop syntax; A’s omission of the low V versus B/C presence; and B’s remaining classes doubt versus A/C resolution. Main evidence makes the selections without erasing the competing text.

## Verification boundary

`assembler_validation.json` reports no errors and records successful checks for all 25 decisions, balanced structural delimiters/environments, and diagram ampersand syntax. The page contains 17 first-occurrence unsure macros and 11 deleted groups. The 21 unresolved physical-locus records exceed the inline marker count because shared repetitions keep their local uncertainty in the records.

No compile or rendering claim is made. The audit confirms that the written implementation represents the selected text and literal graphic structure; it does not independently re-read the handwriting or certify visual typesetting.

### Administrative completion status

The builder’s final page guard has passed. The draft now has main_adjudication_complete=true, all 51 inventory rows marked transcribed=yes, empty residual_questions, and empty checks (no mathematical proof or computation was performed). Its page fingerprint matches the audited page. Source coverage, issue counts, remaining-doubt counts, and C/H totals are unchanged.

## Audited input fingerprints

| Input | SHA-256 |
|---|---|
| `SP48_CW_104/records/scan006/main_observations.md` | `3d794384b8a6f44df5a7620ed4b45276edab08a6ce7a00574deaa4adbf26b294` |
| `reader_inputs/scan006/C.tex` | `b916fade1bbcefd80d90f22f786b69aa64b28aff7ea8d2c96e1114b1d04c0f3b` |
| `reader_inputs/scan006/H.tex` | `6d082c65c904b09db624b54446b2cebec42b30087ed9fcbb8304209817a087a6` |
| `reader_inputs/scan006/H_drawing.tex` | `6a207a20ff18a3aa7dab446db6c0d73434684d83a331331abb704cee264f2cb2` |
| `SP48_CW_104/records/scan006/reader_crosswalk.json` | `7e16b2fe7a761a3addb2c76378d52030dc820cc67b0a3187be838746ca417641` |
| `SP48_CW_104/records/scan006/witness_doubts.json` | `da507a407be8e1255a589ba1b38bdbf44c873a46b9ccfb94f5e44d2f2824a2a0` |
| `SP48_CW_104/pages/H104-01_104_scan006.tex` | `374acaaf0637e8342396e0499e32686ee1579078e00b2eb6a17eaed785c987b1` |
| `SP48_CW_104/records/scan006/decision_draft.json` | `1a60cb0a5967b4fa05b7601e3c1aa7777a795cb0b4e4e91af909eff4ca671212` |

Audit saved UTC: 2026-11-20T12:00:56.746273+00:00.
