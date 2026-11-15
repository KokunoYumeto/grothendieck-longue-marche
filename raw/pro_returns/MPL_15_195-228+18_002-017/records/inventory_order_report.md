# Inventory ordering proposal — mechanical audit only

The canonical inventory and all frozen page/combined TeX files are unchanged. This report accompanies a proposed permutation, not a replacement canonical inventory or a certification of physical reading order.

## Inputs and invariant checks

- Input: `MPL_15_195-228+18_002-017_inventory.csv`; SHA-256 `5076eb2c92276172cae6e5854c9d10a556b6aeae3a1bb868a4db4676e4f3881e`.
- Proposal: `records/inventory_order_proposal.csv`; SHA-256 `a4910c6f454cc30efdad67401bc4aabdb3f5f06861185e2f33850fcb80c8d4f5`.
- Rows: 694 = 447 manual + 247 generated.
- Every original CSV field, including element ID, classification, position and excerpt, is retained exactly as a parsed field value; the complete row multiset is equal. No rows are added or removed.
- `records/inventory_pagination_suggestions.csv` is a separate ten-row suggestion file, excluded from that equality/permutation. It uses existing sheet kinds, fresh per-page IDs above all retained IDs, and exact frozen pagination values; the position fields deliberately identify source lines and leave physical placement for primary-reader review.
- All manual rows retain their relative order within each page. Page order and column order are unchanged.
- All 247 generated rows match final macros exactly by kind, source line and compacted 350-character excerpt; source character offsets and columns disambiguate occurrences.
- Unmatched source-block anchors: 0. Ambiguous source-block anchors: 0. Duplicate exact macro keys: 0.
- All 50 files listed in `records/frozen_manifest.json` match the frozen SHA-256 values before and after this operation.

## Ordering rule and limits

The finalizer (`records/finalize_mechanical.py`, `make_outputs`) intentionally appends generated rows after every page's manual rows. The proposal instead matches each generated row to its source macro and associates it with an explicitly delimited source passage corresponding to a retained manual row. Insertions, deletions and marginal wrappers follow that parent row in source occurrence order; nested macros therefore retain the parser's outer-before-inner order. Two text blocks on 15/227 share a TeX line and are separated by the literal phrase `Plus généralement`; equivalent literal boundaries delimit shared-line passages on 15/225, 15/219 and 15/227. No formula semantics, inferred reading, numerical element ID ordering or global TeX-line sort determines placement.

An enclosing macro can cover an already inventoried drawing without making that drawing's late-added manual row the parent of the enclosing insertion. Thus the insertion containing the ellipse on 15/215 stays beside manual 001, and the insertion containing the ellipse on 15/217 stays beside manual 004. The late-added figure rows themselves remain in their existing manual positions. Every association is recorded below, with the exact macro start line and column.

Free-standing margins that have no uniquely containing manual row are placed at an explicitly marked source boundary. Such placement is a document-order convention for review, not evidence of their physical height on the sheet. The margin on 18/11 lines 25–28 wraps both manual 1000 and 1001 and is placed after 1000. The deletion beginning 18/12 line 2 spans the cancelled page's ten manual blocks and is placed before the first, rather than treated as a deletion contained in that first sentence. No unresolved anchor is silently guessed; an unmatched or ambiguous row would remain at the page tail and be listed below.

## Remaining manual-order issues

Preserving manual order is essential to this proposal's scope, but it prevents a claim that the entire CSV now obeys strict physical top-to-bottom order. The following conflicts or ambiguities are visible in the existing position labels and source correspondence alone; they require the primary reader's judgment, and no original scan was opened for this audit.

| Page | Retained manual rows | Review issue |
| --- | --- | --- |
| 15/197 | 003, then 999 | Bottom page number precedes an added left-margin stroke; the stroke's vertical extent is not specified. |
| 15/203 | 010, then 999 | Bottom page number precedes an added bottom-left stroke; relative height remains unspecified. |
| 15/211 | 009, then 999 | The bottom-left page number precedes the far-left long vertical line (source line 5). The spanning line has no unique vertical rank. |
| 15/215 | 007, 008, 009, 1000, 1001 | Manual 007 is bottom text, 008 is left upper-margin bars, 009 is bottom pagination, and 1000 is an upper insertion ellipse. These retained labels do not form a strict vertical order. |
| 15/217 | 006, then 1000 | Bottom page number precedes the ellipse inside the lower insertion (source line 21); relative height should be checked by the primary reader. |
| 18/11 | 018, then 1000, 1001 | Bottom-right consequence equations precede two added upper-right diagrams. Their generated wrappers/notes remain beside these retained diagram rows in the proposal, so that portion also stays late. |
| 18/16 | 011, then 012 | Bottom equation (32) precedes marks described as left of (30)–(31). This page has no generated rows, so its order is untouched. |

## Sheet classification and element coverage

Canonical/per-page-record `sheet_kind` inconsistencies: 0. Every page has a single allowed classification matching its saved manual record. This verifies metadata agreement only; it does not independently establish whether a sheet is reused typescript, a cover, or another physical class.

All prescribed generated macro classes are covered exactly once. Dedicated pagination rows appear absent for 10 `\mspage` markers on 9 pages. These page numbers are present in the frozen transcription; the issue is inventory granularity/coverage. The proposal deliberately adds nothing.

| Page | Page TeX line | Frozen pagination marker | Existing sheet_kind | Suggested new ID |
| --- | --- | --- | --- | --- |
| 18/7 | 2 | `\mspage{18}` | `reused_typed` | 021 |
| 18/7 | 19 | `\mspage{6}` | `reused_typed` | 022 |
| 18/9 | 25 | `\mspage{8}` | `text` | 014 |
| 18/10 | 8 | `\mspage{9}` | `cover` | 002 |
| 18/11 | 79 | `\mspage{10}` | `text` | 1024 |
| 18/12 | 27 | `\mspage{11}` | `cancelled_draft` | 021 |
| 18/13 | 15 | `\mspage{12}` | `text` | 013 |
| 18/14 | 8 | `\mspage{13}` | `cover` | 002 |
| 18/15 | 27 | `\mspage{14}` | `text` | 019 |
| 18/16 | 26 | `\mspage{15}` | `reused_typed` | 013 |

On 15/211 line 24, the live underlined heading `\uline{\deleted{\unsure{de X}} \unsure{car $p$}}` has no obvious separate manual heading row. Its deletion has generated row 1010, which is associated in the proposal with manual 005 (`Pts banaux; Pts à valeurs dans Z_l ou Q_l`). That broader row may have been intended to cover the heading; this is a possible granularity gap, not an asserted missing transcription.

The counts of explicit `\diagram`/`\figure` wrappers and manual `diagram`/`drawing` rows were also compared. Count differences, if any, are signals for review, since a compound drawing or inline object may be represented differently at the two levels.

| Page | TeX wrapper | Wrapper count | Manual kind | Row count |
| --- | --- | --- | --- | --- |
| All 49 pages | diagram / figure | — | diagram / drawing | Counts agree per page |

## Source-boundary and wrapper cases requiring review

| Page | Generated element | Macro start | Placement | Reason |
| --- | --- | --- | --- | --- |
| 15/225 | 010 (margin note) | 2:1 | before manual 001 | source boundary only; physical position unverified |
| 15/225 | 011 (deletion) | 2:9 | before manual 001 | source boundary only; physical position unverified |
| 15/227 | 007 (margin note) | 2:1 | before manual 001 | source boundary only; physical position unverified |
| 18/11 | 1005 (margin note) | 24:1 | after manual 006 | source boundary only; physical position unverified |
| 18/11 | 1006 (deletion) | 24:276 | after manual 006 | source boundary only; physical position unverified |
| 18/11 | 1007 (deletion) | 24:302 | after manual 006 | source boundary only; physical position unverified |
| 18/11 | 1008 (deletion) | 24:366 | after manual 006 | source boundary only; physical position unverified |
| 18/11 | 1009 (margin note) | 25:1 | after manual 1000 | one margin wrapper covers manual 1000 and 1001; placed after 1000 |
| 18/11 | 1010 (margin note) | 29:1 | after manual 1001 | source boundary only; physical position unverified |
| 18/11 | 1011 (deletion) | 29:41 | after manual 1001 | source boundary only; physical position unverified |
| 18/11 | 1012 (insertion) | 29:241 | after manual 1001 | source boundary only; physical position unverified |
| 18/11 | 1013 (deletion) | 29:269 | after manual 1001 | source boundary only; physical position unverified |
| 18/11 | 1014 (margin note) | 30:1 | after manual 1001 | source boundary only; physical position unverified |
| 18/11 | 1015 (margin note) | 31:1 | after manual 1001 | source boundary only; physical position unverified |
| 18/11 | 1018 (margin note) | 49:1 | before manual 013 | source boundary only; physical position unverified |
| 18/11 | 1023 (margin note) | 63:1 | after manual 015 | source boundary only; physical position unverified |
| 18/12 | 011 (deletion) | 2:1 | before manual 001 | whole-page cancellation wrapper; placed before first manual block |
| 18/12 | 017 (margin note) | 25:1 | after manual 010 | source boundary only; physical position unverified |
| 18/12 | 018 (margin note) | 26:1 | after manual 010 | source boundary only; physical position unverified |
| 18/12 | 019 (deletion) | 26:34 | after manual 010 | source boundary only; physical position unverified |
| 18/12 | 020 (deletion) | 26:65 | after manual 010 | source boundary only; physical position unverified |
| 18/17 | 012 (margin note) | 2:1 | before manual 001 | source boundary only; physical position unverified |

## Unmatched, ambiguous and duplicate-key anchors

Unmatched: `[]`.

Ambiguous: `[]`.

Duplicate exact keys (resolved only by source occurrence order): `[]`.

## Page counts

| Page | Manual rows | Generated rows | Boundary/wrapper review rows |
| --- | --- | --- | --- |
| 15/195 | 9 | 16 | 0 |
| 15/196 | 13 | 0 | 0 |
| 15/197 | 4 | 3 | 0 |
| 15/198 | 9 | 0 | 0 |
| 15/199 | 11 | 7 | 0 |
| 15/200 | 12 | 0 | 0 |
| 15/201 | 6 | 6 | 0 |
| 15/202 | 10 | 0 | 0 |
| 15/203 | 11 | 11 | 0 |
| 15/204 | 11 | 0 | 0 |
| 15/205 | 7 | 3 | 0 |
| 15/206 | 14 | 0 | 0 |
| 15/207 | 8 | 8 | 0 |
| 15/208 | 7 | 0 | 0 |
| 15/209 | 3 | 4 | 0 |
| 15/210 | 5 | 0 | 0 |
| 15/211 | 11 | 9 | 0 |
| 15/212 | 6 | 0 | 0 |
| 15/213 | 10 | 4 | 0 |
| 15/214 | 8 | 0 | 0 |
| 15/215 | 11 | 13 | 0 |
| 15/216 | 12 | 0 | 0 |
| 15/217 | 7 | 7 | 0 |
| 15/218 | 13 | 0 | 0 |
| 15/219 | 12 | 23 | 0 |
| 15/220 | 12 | 0 | 0 |
| 15/221 | 10 | 10 | 0 |
| 15/222 | 12 | 0 | 0 |
| 15/223 | 10 | 10 | 0 |
| 15/224 | 10 | 0 | 0 |
| 15/225 | 9 | 14 | 2 |
| 15/226 | 9 | 0 | 0 |
| 15/227 | 6 | 8 | 1 |
| 15/228 | 14 | 0 | 0 |
| 18/2 | 2 | 0 | 0 |
| 18/3 | 13 | 0 | 0 |
| 18/4 | 2 | 0 | 0 |
| 18/5 | 14 | 11 | 0 |
| 18/6 | 15 | 5 | 0 |
| 18/7 | 4 | 16 | 0 |
| 18/9 | 7 | 6 | 0 |
| 18/10 | 1 | 0 | 0 |
| 18/11 | 20 | 22 | 13 |
| 18/12 | 10 | 10 | 5 |
| 18/13 | 5 | 7 | 0 |
| 18/14 | 1 | 0 | 0 |
| 18/15 | 8 | 10 | 0 |
| 18/16 | 12 | 0 | 0 |
| 18/17 | 11 | 4 | 1 |

## Complete generated-row anchor ledger

Source references are to individual `pages/MPL_15_195-228+18_002-017_C_scanNNN.tex` files. Line:column identifies the opening backslash of the exact macro. IDs are preserved, so the proposed sequence need not be numerically ascending.

| Page | Generated ID | Kind | Macro line:column | Parent manual ID | Parent excerpt | Placement/status |
| --- | --- | --- | --- | --- | --- | --- |
| 15/195 | 010 | deletion | 3:9 | 001 | 2°) X domine Spec Z | after; containing source block |
| 15/195 | 011 | deletion | 5:1 | 002 | Alors en plus de ces [cancelled] | after; containing source block |
| 15/195 | 012 | insertion | 5:40 | 002 | Alors en plus de ces [cancelled] | after; containing source block |
| 15/195 | 013 | deletion | 5:62 | 002 | Alors en plus de ces [cancelled] | after; containing source block |
| 15/195 | 014 | deletion | 7:1 | 002 | Alors en plus de ces [cancelled] | after; containing source block |
| 15/195 | 015 | deletion | 15:23 | 006 | Connexion : relation | after; containing source block |
| 15/195 | 016 | deletion | 15:94 | 006 | Connexion : relation | after; containing source block |
| 15/195 | 017 | deletion | 17:60 | 007 | Ils ne sont en général pas isomorphes | after; containing source block |
| 15/195 | 018 | insertion | 17:82 | 007 | Ils ne sont en général pas isomorphes | after; containing source block |
| 15/195 | 019 | deletion | 17:96 | 007 | Ils ne sont en général pas isomorphes | after; containing source block |
| 15/195 | 020 | deletion | 17:193 | 007 | Ils ne sont en général pas isomorphes | after; containing source block |
| 15/195 | 021 | margin note | 19:1 | 007 | Ils ne sont en général pas isomorphes | after; containing source block |
| 15/195 | 022 | deletion | 19:17 | 007 | Ils ne sont en général pas isomorphes | after; containing source block |
| 15/195 | 023 | insertion | 21:160 | 008 | (iii) Si x est une vt | after; containing source block |
| 15/195 | 024 | deletion | 21:196 | 008 | (iii) Si x est une vt | after; containing source block |
| 15/195 | 025 | margin note | 23:1 | 008 | (iii) Si x est une vt | after; containing source block |
| 15/197 | 1000 | deletion | 4:67 | 002 | Un cas intéressant est celui où h=Q | after; containing source block |
| 15/197 | 1001 | deletion | 4:449 | 002 | Un cas intéressant est celui où h=Q | after; containing source block |
| 15/197 | 1002 | margin note | 6:1 | 002 | Un cas intéressant est celui où h=Q | after; containing source block |
| 15/199 | 012 | margin note | 8:1 | 003 | xi_x,Z in T_alpha(Z) | after; containing source block |
| 15/199 | 013 | deletion | 10:1 | 004 | Quand – De plus [cancelled] | after; containing source block |
| 15/199 | 014 | insertion | 10:89 | 004 | Quand – De plus [cancelled] | after; containing source block |
| 15/199 | 015 | insertion | 19:82 | 007 | D'ailleurs xi_x,Z est défini | after; containing source block |
| 15/199 | 016 | deletion | 25:1 | 010 | Donc On peut dire aussi | after; containing source block |
| 15/199 | 017 | insertion | 25:72 | 010 | Donc On peut dire aussi | after; containing source block |
| 15/199 | 018 | insertion | 25:188 | 010 | Donc On peut dire aussi | after; containing source block |
| 15/201 | 007 | insertion | 2:53 | 001 | C, i.e. closure k(a) isomorphic R | after; containing source block |
| 15/201 | 008 | deletion | 2:171 | 001 | C, i.e. closure k(a) isomorphic R | after; containing source block |
| 15/201 | 009 | insertion | 2:202 | 001 | C, i.e. closure k(a) isomorphic R | after; containing source block |
| 15/201 | 010 | insertion | 2:476 | 001 | C, i.e. closure k(a) isomorphic R | after; containing source block |
| 15/201 | 011 | margin note | 4:1 | 001 | C, i.e. closure k(a) isomorphic R | after; containing source block |
| 15/201 | 012 | deletion | 10:17 | 003 | xi_a,infty; xi_bar a,infty; xi_bar a,Z; two plain connecting strokes | after; containing source block |
| 15/203 | 1000 | deletion | 2:48 | 001 | En plus de la structure entière | after; containing source block |
| 15/203 | 1001 | insertion | 2:68 | 001 | En plus de la structure entière | after; containing source block |
| 15/203 | 1002 | deletion | 2:314 | 001 | En plus de la structure entière | after; containing source block |
| 15/203 | 1003 | insertion | 2:342 | 001 | En plus de la structure entière | after; containing source block |
| 15/203 | 1004 | insertion | 2:435 | 001 | En plus de la structure entière | after; containing source block |
| 15/203 | 1005 | margin note | 17:1 | 006 | tau = tau prime tau double prime = tau double prime tau prime; attached labels | after; containing source block |
| 15/203 | 1006 | insertion | 19:21 | 007 | La situation locale | after; containing source block |
| 15/203 | 1007 | insertion | 19:149 | 007 | La situation locale | after; containing source block |
| 15/203 | 1008 | insertion | 19:280 | 007 | La situation locale | after; containing source block |
| 15/203 | 1009 | insertion | 23:14 | 009 | or c'est là ... frobenius ... réelle | after; containing source block |
| 15/203 | 1010 | margin note | 24:1 | 009 | or c'est là ... frobenius ... réelle | after; containing source block |
| 15/205 | 008 | insertion | 4:179 | 002 | N.B. La conjecture de Hodge interprète | after; containing source block |
| 15/205 | 009 | deletion | 6:1 | 003 | F de niveau <= rho iff [cancelled] | after; containing source block |
| 15/205 | 010 | deletion | 13:268 | 006 | En particulier, le dernier sous-espace | after; containing source block |
| 15/207 | 009 | insertion | 2:151 | 001 | Faisons varier x pt complexe | after; containing source block |
| 15/207 | 010 | margin note | 4:1 | 002 | circled faux cf groupoïde fondamental sur Z | after; containing source block |
| 15/207 | 011 | deletion | 6:60 | 003 | Quant aux xi_x,C | after; containing source block |
| 15/207 | 012 | insertion | 6:84 | 003 | Quant aux xi_x,C | after; containing source block |
| 15/207 | 013 | deletion | 6:118 | 003 | Quant aux xi_x,C | after; containing source block |
| 15/207 | 014 | margin note | 10:1 | 004 | NB En car p>0 | after; containing source block |
| 15/207 | 015 | deletion | 16:208 | 007 | Pt motivique de X | after; containing source block |
| 15/207 | 016 | deletion | 16:289 | 007 | Pt motivique de X | after; containing source block |
| 15/209 | 004 | insertion | 2:57 | 001 | rôle de classes de chemins | after; containing source block |
| 15/209 | 005 | deletion | 2:294 | 001 | rôle de classes de chemins | after; containing source block |
| 15/209 | 006 | deletion | 7:68 | 002 | Pts l-adiques; Pts transcendants; Pts Hodge-de Rham; pts de Witt, values and brace | after; containing source block |
| 15/209 | 007 | insertion | 17:43 | 002 | Pts l-adiques; Pts transcendants; Pts Hodge-de Rham; pts de Witt, values and brace | after; containing source block |
| 15/211 | 1002 | margin note | 4:1 | 001 | Questions | after; containing source block |
| 15/211 | 1003 | insertion | 8:60 | 002 | pts de X à val. dans h; characteristic p and 0; generalized motivic points | after; containing source block |
| 15/211 | 1004 | insertion | 8:94 | 002 | pts de X à val. dans h; characteristic p and 0; generalized motivic points | after; containing source block |
| 15/211 | 1005 | insertion | 8:153 | 002 | pts de X à val. dans h; characteristic p and 0; generalized motivic points | after; containing source block |
| 15/211 | 1006 | deletion | 8:299 | 002 | pts de X à val. dans h; characteristic p and 0; generalized motivic points | after; containing source block |
| 15/211 | 1007 | insertion | 10:63 | 002 | pts de X à val. dans h; characteristic p and 0; generalized motivic points | after; containing source block |
| 15/211 | 1008 | insertion | 18:56 | 003 | pts de X à valeurs dans C mod conj. complexe; R; C avec f infini; Z | after; containing source block |
| 15/211 | 1009 | insertion | 18:148 | 003 | pts de X à valeurs dans C mod conj. complexe; R; C avec f infini; Z | after; containing source block |
| 15/211 | 1010 | deletion | 24:8 | 005 | Pts banaux; Pts à valeurs dans Z_l ou Q_l | after; containing source block |
| 15/213 | 011 | insertion | 10:31 | 004 | N.B. En vertu de Borel-Harish | after; containing source block |
| 15/213 | 012 | deletion | 14:23 | 004 | N.B. En vertu de Borel-Harish | after; containing source block |
| 15/213 | 013 | deletion | 25:1 | 006 | pi_1(X,xi)_alpha=Aut(xi); G(X,xi)=Aut underlined | after; containing source block |
| 15/213 | 014 | deletion | 33:43 | 009 | Ex. X connexe sur C; structure filtrée; structure de Hodge | after; containing source block |
| 15/215 | 1002 | insertion | 4:18 | 001 | Résulte de la conjonction des conj. de Hodge et de Tate | after; containing source block |
| 15/215 | 1003 | deletion | 5:55 | 001 | Résulte de la conjonction des conj. de Hodge et de Tate | after; containing source block |
| 15/215 | 1004 | margin note | 7:1 | 008 | five vertical emphasis strokes | after; containing source block |
| 15/215 | 1005 | deletion | 14:50 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1006 | insertion | 14:64 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1007 | insertion | 16:15 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1008 | deletion | 16:28 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1009 | deletion | 16:57 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1010 | insertion | 16:80 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1011 | deletion | 17:1 | 004 | [Cas corps de base R; points and frob infini] | after; containing source block |
| 15/215 | 1012 | margin note | 28:1 | 006 | triangle X, C, R with plain connecting strokes | after; containing source block |
| 15/215 | 1013 | margin note | 34:1 | 1001 | three vertical emphasis strokes | after; containing source block |
| 15/215 | 1014 | insertion | 36:20 | 007 | Pb étudier comment varie la structure de Hodge | after; containing source block |
| 15/217 | 1001 | deletion | 4:34 | 001 | Lien avec la variété des modules pour des motifs polarisés rigidifiés | after; containing source block |
| 15/217 | 1002 | deletion | 14:20 | 002 | C’est une propriété intrinsèque importante de ces M | after; containing source block |
| 15/217 | 1003 | insertion | 14:43 | 002 | C’est une propriété intrinsèque importante de ces M | after; containing source block |
| 15/217 | 1004 | deletion | 14:77 | 002 | C’est une propriété intrinsèque importante de ces M | after; containing source block |
| 15/217 | 1005 | insertion | 14:94 | 002 | C’est une propriété intrinsèque importante de ces M | after; containing source block |
| 15/217 | 1006 | insertion | 20:32 | 004 | Introduire la notion de schéma motiviquement pointé | after; containing source block |
| 15/217 | 1007 | insertion | 21:1 | 004 | Introduire la notion de schéma motiviquement pointé | after; containing source block |
| 15/219 | 013 | deletion | 3:5 | 001 | X préschéma de type fini normal irréductible sur corps k | after; containing source block |
| 15/219 | 014 | insertion | 3:45 | 001 | X préschéma de type fini normal irréductible sur corps k | after; containing source block |
| 15/219 | 015 | deletion | 5:37 | 002 | v,w deux places archimédiennes; Question a), b) | after; containing source block |
| 15/219 | 016 | insertion | 6:71 | 002 | v,w deux places archimédiennes; Question a), b) | after; containing source block |
| 15/219 | 017 | deletion | 7:17 | 002 | v,w deux places archimédiennes; Question a), b) | after; containing source block |
| 15/219 | 018 | insertion | 8:34 | 002 | v,w deux places archimédiennes; Question a), b) | after; containing source block |
| 15/219 | 019 | deletion | 13:1 | 003 | Nous pouvons supposer; clôture algébrique dans k(X) | after; containing source block |
| 15/219 | 020 | deletion | 16:59 | 004 | Soit k_0; clôture algébrique de Q dans k; corps des places | after; containing source block |
| 15/219 | 021 | insertion | 17:1 | 004 | Soit k_0; clôture algébrique de Q dans k; corps des places | after; containing source block |
| 15/219 | 022 | deletion | 18:1 | 004 | Soit k_0; clôture algébrique de Q dans k; corps des places | after; containing source block |
| 15/219 | 023 | insertion | 30:8 | 007 | En effet, X et M_alpha(X) proviennent de X_0 | after; containing source block |
| 15/219 | 024 | insertion | 30:68 | 007 | En effet, X et M_alpha(X) proviennent de X_0 | after; containing source block |
| 15/219 | 025 | deletion | 31:1 | 007 | En effet, X et M_alpha(X) proviennent de X_0 | after; containing source block |
| 15/219 | 026 | deletion | 32:20 | 007 | En effet, X et M_alpha(X) proviennent de X_0 | after; containing source block |
| 15/219 | 027 | deletion | 35:15 | 007 | En effet, X et M_alpha(X) proviennent de X_0 | after; containing source block |
| 15/219 | 028 | margin note | 37:1 | 008 | X_0--X over k_0--A_0--k | after; containing source block |
| 15/219 | 029 | margin note | 42:1 | 009 | E,k_0,A_0,k,X_0,X,Q and cancellation hatching | after; containing source block |
| 15/219 | 030 | deletion | 42:9 | 009 | E,k_0,A_0,k,X_0,X,Q and cancellation hatching | after; containing source block |
| 15/219 | 031 | deletion | 50:7 | 010 | b) Si v et w coïncident sur k; otherwise revision | after; containing source block |
| 15/219 | 032 | insertion | 50:33 | 010 | b) Si v et w coïncident sur k; otherwise revision | after; containing source block |
| 15/219 | 033 | insertion | 52:1 | 010 | b) Si v et w coïncident sur k; otherwise revision | after; containing source block |
| 15/219 | 034 | deletion | 53:1 | 010 | b) Si v et w coïncident sur k; otherwise revision | after; containing source block |
| 15/219 | 035 | margin note | 55:1 | 011 | on peut supposer X_0 to Spec A_0 fid plat | after; containing source block |
| 15/221 | 011 | deletion | 3:1 | 001 | dénombrable (p.ex. de t.f. sur Q); on voit encore | after; containing source block |
| 15/221 | 012 | insertion | 3:43 | 001 | dénombrable (p.ex. de t.f. sur Q); on voit encore | after; containing source block |
| 15/221 | 013 | deletion | 21:8 | 006 | Si k pas dénombrable; 2) E; v and w on E | after; containing source block |
| 15/221 | 014 | insertion | 21:43 | 006 | Si k pas dénombrable; 2) E; v and w on E | after; containing source block |
| 15/221 | 015 | deletion | 22:10 | 006 | Si k pas dénombrable; 2) E; v and w on E | after; containing source block |
| 15/221 | 016 | insertion | 22:34 | 006 | Si k pas dénombrable; 2) E; v and w on E | after; containing source block |
| 15/221 | 017 | deletion | 23:1 | 006 | Si k pas dénombrable; 2) E; v and w on E | after; containing source block |
| 15/221 | 018 | deletion | 28:23 | 008 | On peut supposer X=Spec k; extension finie de Q | after; containing source block |
| 15/221 | 019 | margin note | 31:1 | 009 | cancelled inequality xi_v(M), xi_w(M) with cross-hatching | after; containing source block |
| 15/221 | 020 | deletion | 31:9 | 009 | cancelled inequality xi_v(M), xi_w(M) with cross-hatching | after; containing source block |
| 15/223 | 011 | margin note | 3:1 | 001 | Il suffirait de construire X projectif lisse | after; containing source block |
| 15/223 | 012 | deletion | 6:168 | 003 | Soit k un corps de nbres | after; containing source block |
| 15/223 | 013 | deletion | 6:271 | 003 | Soit k un corps de nbres | after; containing source block |
| 15/223 | 014 | insertion | 6:284 | 003 | Soit k un corps de nbres | after; containing source block |
| 15/223 | 015 | insertion | 6:317 | 003 | Soit k un corps de nbres | after; containing source block |
| 15/223 | 016 | deletion | 10:43 | 005 | On peut aller plus loin | after; containing source block |
| 15/223 | 017 | deletion | 10:166 | 005 | On peut aller plus loin | after; containing source block |
| 15/223 | 018 | margin note | 11:1 | 006 | line ending in a small circle | after; containing source block |
| 15/223 | 019 | deletion | 12:5 | 007 | Les ... tout pris; ces groupes à priori | after; containing source block |
| 15/223 | 020 | insertion | 17:43 | 009 | Nom: groupes fondamentaux discrets | after; containing source block |
| 15/225 | 010 | margin note | 2:1 | 001 | On a vu plus haut qu’une place | before; source boundary only; physical position unverified |
| 15/225 | 011 | deletion | 2:9 | 001 | On a vu plus haut qu’une place | before; source boundary only; physical position unverified |
| 15/225 | 012 | deletion | 3:103 | 001 | On a vu plus haut qu’une place | after; containing source block |
| 15/225 | 013 | deletion | 4:1 | 003 | Cancelled successive versions from Ce ... to X=P¹_C | after; containing source block |
| 15/225 | 014 | insertion | 5:1 | 003 | Cancelled successive versions from Ce ... to X=P¹_C | after; containing source block |
| 15/225 | 015 | deletion | 6:1 | 003 | Cancelled successive versions from Ce ... to X=P¹_C | after; containing source block |
| 15/225 | 016 | deletion | 8:22 | 003 | Cancelled successive versions from Ce ... to X=P¹_C | after; containing source block |
| 15/225 | 017 | insertion | 8:174 | 003 | Cancelled successive versions from Ce ... to X=P¹_C | after; containing source block |
| 15/225 | 018 | deletion | 8:270 | 003 | Cancelled successive versions from Ce ... to X=P¹_C | after; containing source block |
| 15/225 | 019 | margin note | 9:1 | 004 | Q, X, cancelled A_i, k | after; containing source block |
| 15/225 | 020 | deletion | 13:2 | 004 | Q, X, cancelled A_i, k | after; containing source block |
| 15/225 | 021 | margin note | 15:1 | 005 | X above vertical stroke | after; containing source block |
| 15/225 | 022 | insertion | 16:100 | 006 | Il semble qu’on le verrait facilement | after; containing source block |
| 15/225 | 023 | deletion | 16:170 | 006 | Il semble qu’on le verrait facilement | after; containing source block |
| 15/227 | 007 | margin note | 2:1 | 001 | D’autre part, quels sont les foncteurs multiplicatifs | before; source boundary only; physical position unverified |
| 15/227 | 008 | insertion | 3:114 | 001 | D’autre part, quels sont les foncteurs multiplicatifs | after; containing source block |
| 15/227 | 009 | insertion | 3:285 | 002 | Plus généralement, dans quelle mesure un morphisme | after; containing source block |
| 15/227 | 010 | insertion | 3:362 | 002 | Plus généralement, dans quelle mesure un morphisme | after; containing source block |
| 15/227 | 011 | insertion | 3:419 | 002 | Plus généralement, dans quelle mesure un morphisme | after; containing source block |
| 15/227 | 012 | insertion | 5:100 | 003 | C’est lié au Pb de construire des schémas de modules | after; containing source block |
| 15/227 | 013 | insertion | 5:250 | 003 | C’est lié au Pb de construire des schémas de modules | after; containing source block |
| 15/227 | 014 | deletion | 5:289 | 003 | C’est lié au Pb de construire des schémas de modules | after; containing source block |
| 18/5 | 015 | deletion | 2:55 | 001 | Descriptions conjecturales de motifs | after; containing source block |
| 18/5 | 016 | deletion | 8:4 | 004 | structure de Hodge (k=Qbar) | after; containing source block |
| 18/5 | 017 | deletion | 10:4 | 005 | Betti–(Gauss)Manin | after; containing source block |
| 18/5 | 018 | deletion | 14:4 | 006 | Betti-Tate | after; containing source block |
| 18/5 | 019 | deletion | 16:4 | 007 | De Rham filtré cristallin | after; containing source block |
| 18/5 | 020 | insertion | 18:55 | 008 | Descriptions conjecturales des groupes p-divisibles | after; containing source block |
| 18/5 | 021 | deletion | 18:157 | 008 | Descriptions conjecturales des groupes p-divisibles | after; containing source block |
| 18/5 | 022 | insertion | 18:183 | 008 | Descriptions conjecturales des groupes p-divisibles | after; containing source block |
| 18/5 | 023 | insertion | 20:24 | 009 | structure de Hodge-Tate | after; containing source block |
| 18/5 | 024 | deletion | 26:5 | 012 | cristal filtré | after; containing source block |
| 18/5 | 025 | deletion | 26:66 | 012 | cristal filtré | after; containing source block |
| 18/6 | 016 | deletion | 12:1 | 002 | α permet d’identifier | after; containing source block |
| 18/6 | 017 | deletion | 22:25 | 005 | un autre splitting; Le splitting σ1 | after; containing source block |
| 18/6 | 018 | deletion | 36:2 | 010 | underbraces φ(γ), G(Qp), j2(Qp*) | after; containing source block |
| 18/6 | 019 | margin note | 39:1 | 011 | small right-angled stroke | after; containing source block |
| 18/6 | 020 | deletion | 43:44 | 013 | Ker u ... Π1=π/Ker u | after; containing source block |
| 18/7 | 005 | deletion | 10:1 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 006 | deletion | 10:43 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 007 | deletion | 10:120 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 008 | deletion | 10:366 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 009 | deletion | 10:574 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 010 | insertion | 10:590 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 011 | deletion | 10:822 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 012 | deletion | 10:1000 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 013 | deletion | 10:1058 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 014 | insertion | 10:1080 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 015 | insertion | 10:1265 | 002 | Remarque 7.13.11. La commutativité des deux derniers diagrammes | after; containing source block |
| 18/7 | 016 | deletion | 14:73 | 003 | (7.13.12) Z^i(X_t); H^{2i}; cl; sigma | after; containing source block |
| 18/7 | 017 | deletion | 17:1 | 004 | analogue à (7.13.9), et un carré correspondant | after; containing source block |
| 18/7 | 018 | deletion | 17:115 | 004 | analogue à (7.13.9), et un carré correspondant | after; containing source block |
| 18/7 | 019 | insertion | 17:144 | 004 | analogue à (7.13.9), et un carré correspondant | after; containing source block |
| 18/7 | 020 | deletion | 17:265 | 004 | analogue à (7.13.9), et un carré correspondant | after; containing source block |
| 18/9 | 008 | deletion | 4:55 | 002 | Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte | after; containing source block |
| 18/9 | 009 | deletion | 5:52 | 002 | Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte | after; containing source block |
| 18/9 | 010 | insertion | 5:106 | 002 | Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte | after; containing source block |
| 18/9 | 011 | deletion | 5:138 | 002 | Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte | after; containing source block |
| 18/9 | 012 | deletion | 5:205 | 002 | Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte | after; containing source block |
| 18/9 | 013 | insertion | 5:239 | 002 | Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte | after; containing source block |
| 18/11 | 1002 | deletion | 20:60 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; containing source block |
| 18/11 | 1003 | deletion | 21:122 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; containing source block |
| 18/11 | 1004 | insertion | 21:158 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; containing source block |
| 18/11 | 1005 | margin note | 24:1 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; source boundary only; physical position unverified |
| 18/11 | 1006 | deletion | 24:276 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; source boundary only; physical position unverified |
| 18/11 | 1007 | deletion | 24:302 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; source boundary only; physical position unverified |
| 18/11 | 1008 | deletion | 24:366 | 006 | Fil=Filt; Big=Bigr; déf/Q | after; source boundary only; physical position unverified |
| 18/11 | 1009 | margin note | 25:1 | 1000 | U prime subset B prime subset G prime, radical and parabolic labels | after; one margin wrapper covers manual 1000 and 1001; placed after 1000 |
| 18/11 | 1010 | margin note | 29:1 | 1001 | B prime/U prime isomorphic L prime; arrow j from G_m | after; source boundary only; physical position unverified |
| 18/11 | 1011 | deletion | 29:41 | 1001 | B prime/U prime isomorphic L prime; arrow j from G_m | after; source boundary only; physical position unverified |
| 18/11 | 1012 | insertion | 29:241 | 1001 | B prime/U prime isomorphic L prime; arrow j from G_m | after; source boundary only; physical position unverified |
| 18/11 | 1013 | deletion | 29:269 | 1001 | B prime/U prime isomorphic L prime; arrow j from G_m | after; source boundary only; physical position unverified |
| 18/11 | 1014 | margin note | 30:1 | 1001 | B prime/U prime isomorphic L prime; arrow j from G_m | after; source boundary only; physical position unverified |
| 18/11 | 1015 | margin note | 31:1 | 1001 | B prime/U prime isomorphic L prime; arrow j from G_m | after; source boundary only; physical position unverified |
| 18/11 | 1016 | deletion | 37:1 | 009 | fibration, faisant de B un torseur | after; containing source block |
| 18/11 | 1017 | deletion | 42:14 | 011 | P double prime, P, Big_k, Fil_k | after; containing source block |
| 18/11 | 1018 | margin note | 49:1 | 013 | K; k(gamma); k(alpha); k(beta); k(psi); k(phi); Q(psi); Q(phi); Q | before; source boundary only; physical position unverified |
| 18/11 | 1019 | deletion | 54:72 | 013 | K; k(gamma); k(alpha); k(beta); k(psi); k(phi); Q(psi); Q(phi); Q | after; containing source block |
| 18/11 | 1020 | deletion | 55:2 | 013 | K; k(gamma); k(alpha); k(beta); k(psi); k(phi); Q(psi); Q(phi); Q | after; containing source block |
| 18/11 | 1021 | deletion | 58:1 | 014 | K subset Q(k(alpha), conjugate k(alpha)) | after; containing source block |
| 18/11 | 1022 | deletion | 58:43 | 014 | K subset Q(k(alpha), conjugate k(alpha)) | after; containing source block |
| 18/11 | 1023 | margin note | 63:1 | 015 | (2 i pi)^n in k(alpha) si Q(-n) in Ob M | after; source boundary only; physical position unverified |
| 18/12 | 011 | deletion | 2:1 | 001 | fixe, mettons C; sont déterminés à ext. alg. près | before; whole-page cancellation wrapper; placed before first manual block |
| 18/12 | 012 | insertion | 5:20 | 002 | Conjecture de transcendance; Si k est pré-minimal pour M | after; containing source block |
| 18/12 | 013 | insertion | 9:22 | 004 | g_0 est un point maximal | after; containing source block |
| 18/12 | 014 | insertion | 11:21 | 005 | Corollaire; G^u est le k-groupe algébrique engendré | after; containing source block |
| 18/12 | 015 | deletion | 11:318 | 005 | Corollaire; G^u est le k-groupe algébrique engendré | after; containing source block |
| 18/12 | 016 | deletion | 18:17 | 008 | sur Q est 3 (la seule relation étant | after; containing source block |
| 18/12 | 017 | margin note | 25:1 | 010 | i.e. l’équation de G^u=Sl(2); Si l’invariant j est transcendant | after; source boundary only; physical position unverified |
| 18/12 | 018 | margin note | 26:1 | 010 | i.e. l’équation de G^u=Sl(2); Si l’invariant j est transcendant | after; source boundary only; physical position unverified |
| 18/12 | 019 | deletion | 26:34 | 010 | i.e. l’équation de G^u=Sl(2); Si l’invariant j est transcendant | after; source boundary only; physical position unverified |
| 18/12 | 020 | deletion | 26:65 | 010 | i.e. l’équation de G^u=Sl(2); Si l’invariant j est transcendant | after; source boundary only; physical position unverified |
| 18/13 | 006 | deletion | 8:51 | 004 | b) Soit T le lieu de g sur G_Qbar | after; containing source block |
| 18/13 | 007 | deletion | 8:175 | 004 | b) Soit T le lieu de g sur G_Qbar | after; containing source block |
| 18/13 | 008 | deletion | 8:197 | 004 | b) Soit T le lieu de g sur G_Qbar | after; containing source block |
| 18/13 | 009 | deletion | 10:1 | 004 | b) Soit T le lieu de g sur G_Qbar | after; containing source block |
| 18/13 | 010 | deletion | 12:9 | 005 | c) Soit h in C/Qbar; splitting transcendant | after; containing source block |
| 18/13 | 011 | insertion | 12:98 | 005 | c) Soit h in C/Qbar; splitting transcendant | after; containing source block |
| 18/13 | 012 | margin note | 14:1 | 005 | c) Soit h in C/Qbar; splitting transcendant | after; containing source block |
| 18/15 | 009 | deletion | 4:13 | 002 | X variété holomorphe; Y sous-variété holomorphe | after; containing source block |
| 18/15 | 010 | deletion | 12:5 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 011 | deletion | 12:148 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 012 | deletion | 13:3 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 013 | deletion | 13:89 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 014 | deletion | 13:145 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 015 | margin note | 15:1 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 016 | margin note | 16:1 | 004 | H_Y^{2p}(X,Z); tensor C; H_Y^{2p}(X,C); hypercohomology; C_Y; 1/(2 i pi)^p | after; containing source block |
| 18/15 | 017 | deletion | 19:65 | 005 | On est ramené au cas où Y est réduit à un pt a | after; containing source block |
| 18/15 | 018 | insertion | 20:76 | 006 | NB. à priori; multiplicateur de la forme lambda^p | after; containing source block |
| 18/17 | 012 | margin note | 2:1 | 001 | double vertical rule | before; source boundary only; physical position unverified |
| 18/17 | 013 | deletion | 4:139 | 002 | Alors on voit que | after; containing source block |
| 18/17 | 014 | deletion | 7:22 | 003 | lambda = integrals; cercle unité | after; containing source block |
| 18/17 | 015 | deletion | 23:153 | 009 | H^{i+p}; H^i; P_top; P_an | after; containing source block |

## Reproduction

Run `python records/inventory_order_proposal.py`. The helper validates all frozen hashes and all exact macro matches before writing only the proposal CSV, separate pagination-suggestion CSV and this report. It never invokes the finalizer's write path, never changes canonical CSV, pages, combined TeX, original per-page records or notes, and disables bytecode cache writes. Root should review the flagged cases before deciding whether to adopt any permutation or suggested additions.
