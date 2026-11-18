"""Assemble the reader's reconciled notation, doubt and abbreviation tables.

Only metadata is changed; page LaTeX is never written by this script.
"""
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parents[1]

def update(scan, fn):
    p = ROOT / 'records' / f'{scan:03}.json'
    d = json.loads(p.read_text(encoding='utf-8'))
    fn(d)
    p.write_text(json.dumps(d, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')

def revise96(d):
    d['doubts'][0] = ['opening paragraph', 'la théorie; revêtement', 'le théorie; extension; very rapid pen, with the article and noun both uncertain', 'medium']
    d['doubts'][1] = ['opening paragraph, fourth line', "groupe d'inertie de Galois; égal au", 'Second phrase particularly compressed; the audit replaces the first-pass son reading', 'low']
def revise100(d):
    d['doubts'][5] = ['statement b), relatif', 'colon / à', 'Two dot-like strokes favor a colon; final transcription places colon first', 'medium']
def revise139(d):
    d['doubts'][0] = ['pointed-torsor functor notation, three occurrences', 'calligraphic Z: uncertain 0 in definition, 1-like stroke in proposition source, no distinct exponent in target', 'Letter style and retraced initial exponent remain uncertain; occurrences were compared individually rather than regularized', 'low']
    d['elements'][1][2] = 'Soit Z^0 or Z^1(a;G) = ens. des classes d’isomorphie'

update(96, revise96)
update(100, revise100)
update(139, revise139)

intro = r'''# Reading doubts

## Package notation table

This table records the single reader's decisions, reconciled against the images before the transcription was frozen. Differences that belong to the ink are retained; an unresolved difference is marked in place, not silently standardized. Scan numbers below are archive PDF scan numbers, not the author's pagination.

| Recurring ink / convention | LaTeX transcription | Evidence and limits |
|---|---|---|
| Double quotation marks | Two backticks and two apostrophes | Used for the visible double quotes, including “hensélien,” “point marqué,” “S réduit,” and the cover's “Vrai”; no conversion to guillemets. |
| Prime, double prime, triple prime | `'`, `''`, `^{\prime\prime\prime}` | Checked separately on group, ring, point and diagram symbols; triple-prime notation occurs in the rotated scan 131 diagram. A prime is not substituted for an exclamation exponent. |
| Exclamation mark | Literal `!` in prose | No secure exclamation-mark exponent was identified in this package. `\!` in `>\!` is only a LaTeX spacing command, not a manuscript exclamation mark. |
| Angular two-stem homotopy-group sign | `\unsure{\Pi|\pi}` on 096, 098, 100, 107 | These occurrences were visually compared with 105 and 129. The angular outline favors capital Pi, but case is not secure in the rapid hand; the same explicit alternative is used throughout these four sheets. |
| Clearly tall Pi and underlined Pi | `\Pi_2`, `\Pi_1`, `\underline\Pi_1` | The clearer signs on 105 and 129 remain capital Pi. The underlining of the relative/system-local objects on 129 is retained separately from the un-underlined product and abelian-variety formulas. |
| Tame qualification | Superscript `^t`, subscript `_t`, or word `\mathrm{tame}` | The positions vary between 096–098 and 100 and were not unified. |
| Roots-of-unity notation | `\mu`, `\mu_{n_i}`, `\mu_{\underline n}`, `\mu_t^\infty` | Indices, base subscripts and the infinity sign are retained as they occur. The ambiguous first insertion on 096 remains unsure. |
| Tuple of exponents | `\underline n=(n_1,\ldots,n_r)` | Underlining, rather than a supplied vector arrow, is used in 101 and 103. A few single n occurrences differ in the source and are not automatically changed to underlined n. |
| Ambient script X | `\mathcal X` | Distinguished from ordinary X in 096–098 and from the neighborhood model in 135; it is not read as a Greek letter. |
| Structure-ring letters | `\underline{O}`, `\mathrm O`, `\mathcal O` | Underlined typed O in 095/101/103, upright typed O in 106/107, and script handwritten O in 131/135 are preserved as distinct graphic forms. |
| Base points and their conjugates | `\xi`, `\bar\xi`, `\xi_i`, `\xi_i^0`, `\xi'` | Angular xi and its bars were checked in 096–103, 117, 133 and 138–140. Retraced indices and cancelled points carry local doubt marks. |
| Torsor-pair labels | `(P,\xi)`, `(Q,\eta)`, `(R,\lambda)` | The three pairs are kept distinct in 138–140. No closing argument is added after the fibre-product opening on 140. |
| Gamma versus script letters | `\Gamma`, `\mathcal F`, `\mathcal K` | Gamma in extensions and constant groups is not conflated with the script F/K pen samples on 105. The difficult K sample remains unsure. |
| Inertia bars | `I_i`, `\bar I_i`, `\bar I` | Insertions and replacements of barred for unbarred symbols on 103 are recorded explicitly; the remaining unbarred I in a displayed expression is not repaired from context. |
| Tilde | `\widetilde X`, `\widetilde D`, `\widetilde K` | Covers, pulled-back divisors and fields are kept distinct. An uncertain subscript 1 on 101 remains marked. |
| Completion hats | `\widehat A`, `\widehat X`, `\widehat{\mathbf Z}` | Scans 104, 107 and 111; the hat on the opening Tate expression in 104 is uncertain. Scan 107 has a literal square exponent on the completed integer group. |
| Roman versus Gothic ideal/prime letters | `p` with `\mathfrak p` alternative where needed | The heavily written completed-ring subscripts in 107 do not securely distinguish these alphabets. No global conversion to Gothic is made. |
| Pointed-torsor functor glyph | `\mathcal Z` with local `\unsure` | In 139 the definition favors superscript 0 over 1, the proposition source has a 1-like stroke, and its target has no distinct superscript. The overwritten target glyph and the replacement a are recorded, rather than forcing one formula everywhere. |
| Infinitesimal, separable and reduced indices | `\mathrm{inf}`, `\text{sép}`, `\text{réd}` | Typed indices on 126 and the small handwritten reduced index on 138 were checked independently. The candidate U/H in 137 remains unsure. |
| Bold lettering and pen samples | `\mathbf T`, `\mathbf E_i`, `\mathbf G_i`, etc. | The inverted samples on 105 are reproduced in their relative positions, including cancelled glyphs; they are not expanded into a mathematical assertion. |
| Underlining in prose / notation | `\uline`, `\uuline`, `\underline` | Single and double rules are distinguished; scan 131's uncertain marginal word has two underlines. Heavy single rules are not automatically counted as double. |
| Plain connector without a visible head | `\arrow[...,no head]`, `\arrow[...,dash]`, or `\unsure{-|\to}` | No direction is supplied just because the mathematics suggests one. The lowest strokes of the two triple connectors in 131 have no distinct head. |
| Blank typescript connector slot | `\quad` or a phantom labelled connector | Scans 095 and 097 have gaps where no connector ink is recoverable. Their absent arrows are not reconstructed from published text. |
| Isomorphism / equality / word “même” | `\simeq`, `=`, or the literal word | The author's use of `=` inside French prose, notably 104, 131 and 138, is preserved instead of being expanded to “même.” |
| Ordinary multiplication / contracted products | `\times`, `\times_G`, `\mathbin{\times}^{\Gamma}` | Subscript versus superscript placement follows each formula. The anomalous final formula on 138 is transcribed literally. |
| Author numbering versus foliation | `\mspage{5}`, `{6}`, `{2}`, `{5}`, `{6}` on 096, 098, 126, 129, 130 | Archive corner foliation is only a TeX comment. Circled section numbers on 100/101/103 and typed I-6 on 132 are not promoted to manuscript page numbers. |
| Cancellation, insertion and page state | `\deleted`, `\inserted`, `\margin` | Repeated deletions are retained, including nested deletions in an already cancelled passage. The wholly crossed scan 104 is a cancelled draft, not automatically a refuted theorem. |

## Doubts by page

Confidence concerns the reading, not the truth of a mathematical statement. High-confidence rows document a surprising literal reading or a deliberate non-restoration. Audit additions are grouped with their page; where an audit replaced a first-pass reading, the final reading is stated explicitly.

| Cote | Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
'''

abbreviations = r'''
## Abbreviations encountered

Expansions below are editorial suggestions only. They are not substituted into the LaTeX; a final period is not supplied where the manuscript omits it. Variants in the same row are listed only where they actually occur in the transcription.

| Written form | Probable expansion / sense | Scans or caution |
|---|---|---|
| `il f et s` | il faut et suffit | 095 |
| `cf` | confer / compare | 097 |
| `N°` | numéro | 097 |
| `i.e.`, `i.e` | id est / c'est-à-dire | 096–104, 117, 126, 130–131 |
| `c-à-d` | c'est-à-dire | 104; the reading is unsure |
| `e.g.` | exempli gratia / par exemple | 109 |
| `loc.`, `loc` | localement | 100–103, 133, 135 |
| `n.th.` | noethérien | 100; shorter visible form retained with doubt |
| `noeth.` | noethérien | 133, 135 |
| `préschém.` | préschéma | 133, 135 |
| `schém.` | schéma | 101 |
| `sch.` | schéma | 131; could instead be a symbol naming the representing object |
| `grpes` | groupes | 103 |
| `gr.` | groupes / de groupes | 139, superscript on Hom |
| `s-groupe`, `ss-groupe` | sous-groupe | 100, 138; the S in S-ss-groupe denotes the base, not part of the abbreviation |
| `hom`, `hom.` | homomorphisme; in “principal hom.”, homogène | 096, 101, 107, 135, 137, 139; sense depends on the phrase |
| `isom`, `isom.` | isomorphisme | 096, 103, 108, 131, 135, 138 |
| `ens`, `ens.` | ensemble | 104, 131, 139 |
| `à g.` | à gauche | 105 |
| `cont` | continu | 105, Hom cont |
| `op.` | opérateurs / opérations | 101, “à op. G” |
| `p.r.` | par rapport | 103 |
| `revêtt` | revêtement | 103 |
| `rec.` | recouvrement or revêtement | 100, 103; the abbreviation alone does not settle the terminology |
| `pt` | point | 100, 103, 138 |
| `géom`, `géom.` | géométrique | 100, 103, 117 |
| `gén.` | générique | 100, 103 |
| `car.`, `car` | caractéristique | 098, 100 |
| `alg.`, `alg` | algébrique / algébriquement | 096, 104, 129, 133 |
| `ext.` | extension | 133 |
| `conn` | connexe | 100 |
| `irred` | irréductible | 100; uncertain reading |
| `supp` | support | 100, deleted |
| `Et.` | Étude | 100, deleted and uncertain |
| `Dém.` | Démonstration | 104 |
| `dim` | dimension | 104, 133 |
| `tt`, `tte` | tout, toute | 100, 104, 110, 133, 135; tout/tt remains unsure in 135's opening |
| `déc.` | décomposition | 110 |
| `repr.` | représentant | 110; uncertain reading |
| `NB.`, `N.B.` | nota bene | 110, 131 |
| `fid.` | fidèlement | 131 |
| `qua.`, `qu.` | quasi | 133 |
| `cpts.` | compacts | 133 |
| `princ.` | principal | 138; alternative fully written principal is retained in place |
| `t.q.` | tel que / tels que | 138–139 |
| `th.` | théorème | 107 |
| `universellt` | universellement | 131; ending uncertain, with universelle as alternative |
| `ex.` | exact | 131; the entire “ex. et à gauche” reading remains unresolved |
| `fonct.` | foncteur | 131; only a reading alternative to the uncertain fibré, not an established occurrence |
| `mod` | modulo | 101, marginal Chern class |

## Legibility and limits

The typescripts are substantially easier to read than the rapid manuscript sheets, but carbon-copy gaps, typewriter overstriking, and handwritten replacements still require explicit doubt. The greatest uncertainty is in the opening and right edge of 096, the dense changes in 100–103, the short algebraic proof transitions in 108–110, the very compressed main text and upside-down margin of 131, the marginal neighborhood hypothesis and proof introduction in 135, and the overwritten functor notation and small diagonal annotation in 139. The pencil cover subtitle on 124 remains particularly faint.

The large displays and most clearly printed words are more secure than those passages. This is not a claim that every unmarked word is infallible: even after the second visual audit, fast cursive can support more than one reading. The small word-count illegibility markers are confined to physically unreadable cancelled words; no formula or diagram symbol has been replaced by an illegibility count. The drawings are hand-coded TikZ approximations of the visible contours, positions and labels, not metric facsimiles.

Pale mirrored show-through was distinguished from writing on the viewed face, especially in 108–109, 117–118, 131–132 and 139–140. The actual typescripts on reused sheets were transcribed in full, including when upside down; their provenance was not inferred from typography alone. No OCR, published edition, neighbouring transcription or contextual source was used to establish the readings. All 31 supplied pages received a sequential first reading and a sequential second audit before context access.
'''

rows = []
for p in sorted((ROOT/'records').glob('[0-9][0-9][0-9].json')):
    d = json.loads(p.read_text(encoding='utf-8'))
    for row in d['doubts']:
        cells = [29, d['scan'], *row]
        rows.append('| '+' | '.join(str(x).replace('|', r'\|').replace('\n', ' ') for x in cells)+' |')
(ROOT/'MPL_29_095-140_doubts.md').write_text(intro+'\n'.join(rows)+'\n'+abbreviations, encoding='utf-8')
print(f'Reconciled notation, {len(rows)} doubt rows, abbreviations and legibility statement.')
