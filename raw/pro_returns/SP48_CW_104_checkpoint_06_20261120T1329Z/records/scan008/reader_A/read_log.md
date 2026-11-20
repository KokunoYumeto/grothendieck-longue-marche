# Reader A — scan 008

Independent reading of the authorized scan 008 packet only. Model: GPT-6 Astra Pro; effort inherited/not exposed. Brief v07, PREAMBLE.tex, the supplied notation snapshot, C.tex, H.tex, C_context.md and page.json were read before any image. No H_drawing was supplied. The first packet-path attempt returned file-not-found and exposed no file contents; the packet was then read from its authorized `reader_inputs/scan008` location.

## Image register

1. Whole source, 1691 × 2373, viewed once: portrait handwritten note sheet; seven principal formula/map groups, one terminal diagram, several cancellations and two principal text insertions; archive digit 7 at lower left. No title, date, manuscript folio, readable typed reuse, marginal prose or independent drawing was found.
2. Half a, 1691 × 1266, viewed once: all text and mathematical signs from the opening through the overlapping Soient line checked against both witnesses.
3. Half b, 1691 × 1267, viewed once: all text and mathematical signs from the overlapping canceled sentence to the footer checked against both witnesses. Its whole-image top offset is 1106.
4. Thirteen tight decision crops were made only for loci left open by the halves, then viewed in numbered order once each. Actual source boxes and processing are in `crop_metadata.json`. Each used Pillow crop, autocontrast cutoff 0 and LANCZOS resize to 2600 px wide. No rotation or sharpening was applied. No delivery failure occurred.

## Line and element register

| Element or source line | Observation after direct comparison |
|---|---|
| Opening `De plus, se rappelant la definition de` | C’s opening phrase is supported; H’s additional on, deletion and rappelle are not. The first e of definition is unaccented. |
| `J_n = D̃_n = ens des sous-objet de D_n` | Both equalities, separate tilde, plain D and n indices checked. Hooked J agrees with C, not H’s I. No stop after ens. Final sous-objet has t and its exit, no separate s. |
| `on a, pour ∀ n∈N, une application` | On a and comma visible; ∀, membership and doubled N checked. H’s initial dash/et does not match. |
| `canonique, strictement croissante` | Canonique has the long q descender. The rest agrees with both. |
| Type map | Source J_n, right arrow with two-stroke head, τ_n and doubled N checked. The source J agrees with C. |
| Right-hand caption | `τ_n, application ``type`: opening two ticks only; no enclosing parentheses or closing quotation pair. |
| `dont l’image est formée ... de l’ens` | Formée has acute and distinct final e-like curve. C’s ending doubt resolved. Old des is canceled, not H’s dans; no stop after ens. |
| Old bound and new set | `I_{≤n} des` is all crossed. Live `N_{≤n}={n′∈N | n′≤n}.` checked sign by sign. H’s live inserted des is rejected. |
| `Notons que chaque J_n a un plus grand` | Chaque and hooked J verified. A un plus grand agrees with both witnesses. |
| `élément, qui est ``D_n ...` | Accent, comma and opening quotation pair checked. No closing pair. |
| Parenthetic phrase | `en tant que` resolved; small le is inserted at a caret before sous-objet. Maximal de D_n and closing punctuation checked. |
| Naming phrase | Read `et que je note d_n.` The low e and following looped j descender support H here. No independent deletion is retained from C’s est/il hypothesis. |
| `On a donc` and reference | On a donc agrees; `(par (ii))` is an attached interlinear addition with a long low leader. |
| Singleton display | `τ_n^{-1}(n)={d_n}`: τ, lower n, −1, parentheses, equality and both braces agree with both witnesses. |
| Canceled Si sentence | Entire sentence crossed. J_n, not I_n. No independent terminal full stop; C’s supplied stop removed. |
| `Soient n,n′∈N,` | Both n variables, prime, membership, doubled N and comma checked. |
| Higher canceled start | Crossed x-like and membership forms are visible; whether a complete additional J belongs to this upper attempt remains unresolved. |
| Canceled main start | `x∈J_n, n′=τ_n(x), on` is crossed through its final on. H’s surviving on is not supported. |
| Replacement | `avec n′≤n` stands above the canceled right-hand portion and is retained as insertion. |
| Live considérons | One live occurrence, with ons ending. No separate later inserted second occurrence. |
| Following canceled fragment | Via is readable; x and parenthesis/cancellation curves remain doubtful. Candidate l’in removed; via x / via (x) retained. |
| Canceled lower sentence | `on a alors une/un application`: long line strikes through application as well. Article ending remains unresolved. |
| First Hom arguments | Older rounded O/D contour retained as doubtful beneath the first live D. First n′ prime checked. Second D has one main left stem; C’s doubled-alphabet alternative removed. |
| First Hom target and lower row | Hooked right arrow, `D̃_n=J_n`, then lower `u↦u(d_{n′})`. Both heads, mapsto bar, parentheses, small d and prime checked. No comma after target. H’s single-row layout differs. |
| Bijection sentence | `qui est une bijection des Hom sur l’ens τ_n^{-1}(n′), et considérons`. All words checked, including the agreements. No stop after ens. |
| Second Hom left member | Older D/O contour retained. High mark is 4-shaped, with triangular counter and descending stem; 4/asterisk retained, prime excluded. The ordinary n′ has its own prime. Second argument plain D_n checked. |
| Second Hom right member | Right arrow, both tildes, both n indices and first prime checked. Two separate square-ended low brackets and the hooked J labels underneath preserved. H’s note gets lower placement but has I labels and omits drawn bracket geometry. |
| `on en déduit une ... application` | Live prose agrees. Canceled beginning is bijec, including visible long j descender, with no recoverable continuation beyond c. |
| Lower definition | Left inverse image and equality checked. Label is unaccented def. Live object is `J_{n′,n}`; neither index is canceled. |
| Canceled group after J | Parenthetic boundaries remain visible; inner n/n′ cannot be settled. Retained in place. |
| Lower arrow and Hom | Label is `ρ_{n,n′}`, not φ. Both Hom arguments are J. Prime placements checked independently. |
| Relation beneath inverse image | Two short vertical strokes, left one curved with low return, and a separate upper-left point. Traced literally; no semantic identity supplied. |
| Bracketed lower Hom | `[Hom(D_{n′},D_n)]` is beneath the left inverse image. Both brackets, prime and comma checked; H’s placement under the right member is wrong. |
| Caption beneath J | Low square-ended bracket over four lines: `ens des / éléments / de J_n de / type n′`. All words and accent checked. |
| Mapping below | `ou ξ↦u_ξ^n`: ou has no accent; ξ’s turns, mapsto and right-side indices checked. |
| Final prose | `qui est injective, plus précisément on a la commutativité`. No additional ou and no final de. Final e/acute remains uncertain despite crop. |
| Final diagram objects | `J_{n,n′} → Hom(J_{n′},J_n) → J_n`. The first object’s prime is on the second n, unlike the definition above. Each arrowhead points right. |
| Final labels | First label `ρ_{n,n′}`; second `u↦u(d_{n′})`; all subscripts and the small d checked. |
| Inclusion path | Headless broad lower curve, short open left curl, detached endpoints and inclusion above its low center. C’s endpoint gaps adjusted; H’s bend-right arrowhead is absent from source. |
| Footer | Archive 7 only; retained as a comment. No manuscript date or author folio asserted. |

## Every inline C doubt

| C doubt | Outcome | Issue |
|---|---|---|
| definition / définition | Resolved as unaccented definition | a02 |
| sous-objet / sous-objets | Resolved as singular spelling sous-objet | a05 |
| formée / formé | Resolved as formée | a09 |
| en tant / en | Resolved as en tant | a15 |
| canceled est / il | No distinct canceled word; phrase read que je | a17 |
| on / on y | Read je, with visible looped descender | a17 |
| upper x∈J / x∈ | Retained | a20 |
| considérons / considérer | Resolved as considérons | a22 |
| via x / via (x) / l’in | Refined to via x / via (x); parenthetic status unresolved | a23 |
| une / un | Retained | a24 |
| old O / D in first Hom | Retained | a25 |
| first Hom second D / doubled D | Resolved plain D | a26 |
| old D / O in second Hom | Retained | a29 |
| high asterisk / prime | Refined to 4 / asterisk; prime excluded | a30 |
| canceled bi ce / bi se | Resolved bijec with descending j | a32 |
| canceled (n′) / (n) | Retained | a35 |
| ou / où | Resolved unaccented ou | a41 |
| commutativité / commutativite | Retained | a43 |

The C contextual rows were also checked: J/D/D̃/τ/N alphabets and shapes, −1 and prime placement, ξ and u indices, both rho labels, ens/def/Hom abbreviations, the two unclosed quotation pairs, and the unequal paired-index orders. No other-page primary contextual row was present in this packet. Historical comments about another scan were not used as image evidence.

## Decision crop register

| Crop | Decision or remaining limit |
|---|---|
| 01_definition | No first-e accent; resolved. |
| 02_sous_objet | Complete final t and no further s; resolved. |
| 03_formee | Formée ending and old canceled des; resolved. |
| 04_en_tant_le | En tant and inserted le; resolved. |
| 05_quon | Best reading que je; C deletion removed. |
| 06_old_x | Shared tall contour prevents settling the upper J; retained. |
| 07_considerons | Considérons resolved; via readable; parentheses and une/un remain open. |
| 08_first_Hom | Old O/D unresolved; second D plain. |
| 09_second_Hom | Old D/O unresolved; high sign refined to 4/asterisk. |
| 10_bice | Long j descender yields canceled bijec. |
| 11_lower_J | Live index order n′,n secure; canceled parenthesis remains open. |
| 12_lower_Hom | Left placement, punctuation and literal vertical relation/point recorded. |
| 13_commutativite | Ending e/acute not secure; doubt retained. |

## Final consistency and limits

The complete reading was compared once as text against C. Every substantive amendment in that diff has a report issue, including the terminal full stop, tiny lower relation point, and endpoint gaps. Accurate parts of C’s final TikZ diagram were retained. No image was reopened for this comparison.

There were no mathematical proof/computation checks. The typed formulas are claims observed on the page; the index-order discrepancy is reported from ink and is not corrected or declared mathematically false. The report’s checks array is empty.
