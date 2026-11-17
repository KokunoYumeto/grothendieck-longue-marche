from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_108+112+113+114+115'

notation = r'''# Notation table

This table was maintained during the single-stream transcription and reconciled against the images before the context archive was opened. A common sign has a common encoding; differences actually visible in the ink are retained, and the table does not impose mathematical consistency on the manuscript.

| Manuscript feature | LaTeX transcription | Cross-page decision |
| --- | --- | --- |
| Double quotation marks | Two backticks and two apostrophes: ``...'' | Used consistently; no typographic curly quotes substituted. |
| Single and double underlining | `\uline{...}`, `\uuline{...}` | Distinct from a frame, drawn with TikZ. |
| Ordinary category letters | `A,B,C,M,N,P,Q` | Not changed to script letters merely because they denote categories. |
| Script letters | `\mathcal E`, `\mathcal F`, `\mathcal L`, `\mathcal P`, `\mathcal Q`, `\mathcal X` | Script F and X in 115009 and 115015 compared; individual alphabet doubts retained. |
| Gothic resolution letter | `\mathfrak F` | 113013; script F remains an alternative in the doubts table. |
| Outlined letters | `\mathbb O`, `\mathbb P`, `\mathbb Z`, `\mathbb N`, `\mathbb L` | The round outlined O in 108 and 114 is not a zero; P/L readings remain marked where doubtful. |
| Heavy letters | `\mathbf W`, `\mathbf Z` | Retained independently of outlined letters. |
| Presheaf hat | `\widehat A`, `\widehat{(A\times B)}` | Hat placement and grouped arguments follow the ink. |
| Opposite-category circle | `^\circ` | Distinguished from the small open v-shaped duality sign. |
| Duality v | `^\vee` | 113 and 115; the uncertain v/circle at 115014 remains `\unsure{\vee|\circ}`. |
| Bar and tilde | `\overline A`, `\widetilde A` | Double waves at 115011–012 remain an explicit double-tilde/single-tilde doubt. |
| Underlined Hom, Bil, W | `\underline{\mathrm{Hom}}`, `\underline{\operatorname{Bil}}`, `\underline W` | Underlining is not silently added to ununderlined occurrences. |
| Exclamation superscript | `^!` | Stroke and dot checked throughout; never converted to a prime. |
| Exclamation subscript | `_!` | Kept distinct from `^!`; especially in the Hom wheels and duality formulas of 115. |
| Two exclamation signs | `^{!!}`, `_{!!}` | Relative upper/lower positions retained, including inconsistent mixed formulas. |
| Prime | `'` | Remains a prime where a small elevated stroke is visible. |
| Star | `^*`, `_*` | Placement retained; 115011's later `\varphi'_*` is not repaired to its earlier `\varphi^*`. |
| b-shaped linearisation exponent | `^{\unsure{b|\flat}}` | 112003; compared with the b/flat doubt at 115012. Bounded derived-category `D^b` is kept separately. |
| Looped additive-presheaf sign | `^{\unsure{\&}}` | 113004–013: ampersand-shaped ink, not silently identified with b, flat, hat, or sharp. |
| Hooked Greek vertical/object letter | `\unsure{\zeta|\xi}` | Consistent across 113003 and 113006 after comparison; zeta is the first reading. |
| Lower-formula exponent in 115004 | `\unsure{\xi|\sharp}` | Dense multiply stroked form; retained separately from the more angular sign on 115011–012. |
| Angular four-shaped functor sign | `\unsure{\sharp|\natural}` | 115011–012 compared directly; the earlier provisional G alternative was discarded. |
| Ambiguous homotopy-type letter | `\unsure{\xi|\varphi}` | 108005; not equated with the exponent in 115004. |
| Delta with f | `\Delta_f` in 108003; `\Delta^f` in 114003 | The lower and raised positions are visible in the respective scans and were deliberately retained. |
| Outlined O with f | `\mathbb O_f` or `\mathbb O^f` | Same position distinction, according to each occurrence. |
| Chain-complex degree dot | `\bullet` | Preserved as the visible index, including under D, L and H. |
| Product, coproduct and tensor | `\prod`, `\coprod`, `\bigoplus`, `\otimes`, `\boxtimes` | Shape and indices retained individually; no replacement based on expected formulas. |
| Direct and inverse limit | `\varinjlim`, `\varprojlim`; plain `\lim` when no direction is drawn | Incomplete or plain-limit notation is not completed. |
| Arrow, headless connector, hook | TikZ-cd arrows, `no head`, `hook` | Arrowheads checked separately from the mathematical direction one might expect; doubts remain explicit. |
| Double arrow, dotted/dashed arrow | `Rightarrow`, `double`, `dotted`, `dashed` as appropriate | Stroke count and line style preserved. |
| Vertical comparison symbols | `\rotatebox{90}{...}` or a labelled phantom connector | Equivalence/equality marks are not silently made into arrows. |
| Author's sheet numbers | `\mspage{n}`; `\mspage{\textcircled{n}}` when circled | Author numbering only; the uncircled 7 on 115014 stays uncircled. |
| Archive foliation | `% archive foliation: n` | TeX comment only, never an author's page number. |
| Cancellation and insertion | `\deleted{...}`, `\inserted{...}` | Dense correction layers are retained, with doubt where their extent is uncertain. |
| Marginal blocks and separators | `\margin{...}`, TikZ in `\figure{...}` | Side notes, braces, frames, pointers and separate ink strokes are retained as such. |
| Abbreviations | Visible letters and punctuation | Expansions occur only in the separate table below. |

'''

rows = []
for line in (ROOT/'work_records/doubts_rows.md').read_text().splitlines():
    if not line.startswith('| '):
        continue
    r = [x.strip() for x in line.strip('|').split('|')]
    if len(r) != 6:
        raise ValueError(line)
    c,n,loc,reading,alt,conf = r
    if (c,n,loc) == ('108','003','6a'):
        r[3:5] = ['Catégorie; O-sharp', 'Accent and O superscript indistinct; Delta_f was resolved in the second audit']
    if (c,n,loc) == ('108','004','11 deletion'):
        r[3:5] = ['équiv', 'Final abbreviated strokes partly crossed']
    if (c,n,loc) == ('108','005','16 opening'):
        r[3:5] = ['Mes', 'Les; initial strokes overlap']
    if (c,n,loc) == ('108','005','16 final line'):
        continue
    if (c,n,loc) == ('108','006','cancelled passage'):
        r[3:5] = ['Prendre la catégorie (d’anneaux [1 unreadable word] finis locaux, sur k, à corps résiduel k', 'une catégorie; one word still physically obscured by cancellation']
    if (c,n,loc) == ('112','003','left NB margin'):
        r[3:5] = ['Si A est tot. asph., alors tous les pt de A-hat_ab quasi iso', 'Very compressed final words; the entire marginal assertion remains low confidence']
    if (c,n,loc) == ('112','004','NB'):
        continue
    if (c,n,loc) == ('113','003','all diagram vertical labels'):
        continue
    if c == '113' and n == '003':
        r[3] = r[3].replace('xi','zeta')
        r[4] = r[4].replace('eta/xi','eta/zeta')
    if (c,n,loc) == ('113','007','printer lines 19–20'):
        r[3:5] = ['NDSDZ; RENGMK', 'RENGMC remains alternative for the second code; similar printer letters']
    if (c,n,loc) == ('115','009','X_I product'):
        r[3:5] = ['product index j/i; factor X_j', 'Index glyph is ambiguous; the displayed alternatives remain in the transcription']
    if (c,n,loc) == ('115','011','bottom functor superscript'):
        continue
    if (c,n,loc) == ('115','014','lower paragraph') and reading.startswith('ss.;'):
        r[3:5] = ['ss.; néct.; ss. pl. ds.', 'Compressed abbreviations; final ds./de uncertain']
    rows.append(r)

# Preserve the reading order within each scan; later audit qualifications follow
# the corresponding scan rather than appearing in a detached chronological tail.
rows.sort(key=lambda r:(int(r[0]),int(r[1])))
table = '| Cote | Scan | Approximate line or position | Reading in the final transcription | Alternatives or cause of doubt | Confidence |\n| --- | --- | --- | --- | --- | --- |\n'
table += '\n'.join('| '+' | '.join(r)+' |' for r in rows)+'\n'

abbreviations = '''
## Abbreviations encountered

These are tentative expansions, not additions to the transcription. They describe the manuscript abbreviations; printer job identifiers, program names, data-set names, and Fortran variable names are left as identifiers rather than speculatively expanded. Case, dots, and the presence or absence of a final letter vary in the original.

| Written form | Probable expansion or interpretation |
| --- | --- |
| ab.; abél.; ab; Ab | abélien(s); abelian category/abelian groups according to position; subscript ab is retained literally |
| add.; k-add. | additive; k-additive |
| alg. | algébrique(s), probable in the qualified topos notation |
| Appl.; appl. | application |
| asph.; tot. asph. | asphérique; totalement asphérique |
| bif. | bifoncteur / bifonctoriel |
| can. | canonique |
| cat.; Cat | catégorie(s); category of categories for Cat |
| cf. | confer / compare |
| chgt. | changement |
| cit. | cité |
| clg | unresolved abbreviated word in 108004; chg is an alternative, not an established expansion |
| coh.; coh.^t | cohomologique / cohomologiquement, tentative |
| comm. | commutatif / commute / commutant, according to position |
| contr.; contr.tile / contr.ble | contractile / contractible; the visible abbreviated ending remains uncertain |
| Cor. | corollaire |
| def.; déf. | définition |
| diag. | diagonale |
| ds. | dans, tentative at the cramped occurrence in 115014 |
| dér.; opérat. dér. | dérivé(s); opérations dérivées |
| p.ex. | par exemple |
| el. | elementary / élémentaire |
| eq.; équiv. | equivalence / équivalence |
| ess. | essentiel(le) |
| Ex | exemple |
| fid.; pl. fid. | fidèle; pleinement fidèle |
| fon. | foncteur, tentative in fon. cogénérateur |
| gén; génér. | général / générateur, according to position |
| Geom. | geometric |
| Gr | groupes / group objects |
| Homs | Hom(s), cramped abbreviation in 108004 |
| homotopiq. | homotopique |
| hyp. | hypothèse |
| i.e. | id est |
| induct | induction / inductive, tentative in the cancellation |
| int. | intersection, probable in 115014; distinct from the integration symbol in 108003 |
| inv.; quasi-inv. | inverse; quasi-inverse |
| iso; isom | isomorphisme(s) / isomorphic |
| lim | limite(s); no unshown direction supplied |
| loc.; loc.^t; lc | local / localement; locally constant in derived-category indices |
| mono. | monomorphisme |
| nb. | nombre |
| NB | nota bene |
| néc.; néct. | nécessaire / nécessairement, tentative |
| Ob | objets |
| op.; op. bord | opérateur; opérateur de bord |
| p. | page, where used as a reference; isolated p in 115004 remains uncertain |
| petit. | petite / petit, explicitly contracted in 114005 |
| pl. | plein(e) or pleinement according to position |
| prod. tens. | produit tensoriel |
| proj. | projectif / projection, according to position |
| prop. | proposition |
| pt | points, tentative in the difficult marginal note 112003 |
| quasi iso; q-iso / p-iso | quasi-isomorphisme; the initial letter is uncertain in 112003 |
| récur | récurrence |
| relt. | relativement |
| repr. | représentable / représentant |
| resp. | respectivement |
| SQ / W (before fibrations) | unresolved designation in 108004; no expansion asserted |
| ss. | sous / sous-catégorie(s), tentative where compressed |
| ssi | si et seulement si |
| st.ble; st.bles | stable; stables |
| str. | structure |
| strict. | strictement |
| subm | submersion(s) |
| syst.; syst. de coeff | système(s); système de coefficients |
| tens. | tensoriel |
| tjrs | toujours |
| Top.; top. | topological / topologique |
| tot. | total / totalement |
| Ttes | toutes, tentative |
| UlProj | ultraprojectifs |
| val. | valeurs |
| wtc | weak test category, probable in 108003 |
| DPS | unresolved acronym in 114005; no expansion supplied |
| LH; DR; MU | retained notational abbreviations; their meaning is not inferred from these letters alone |
| CPU; I/O; SEC; MIN | central processing unit; input/output; seconds; minutes |
| SYS; VOL; SER; NOS; STMT; JCL | system; volume; serial; numbers; statement; job control language |

## Legibility and limits

The covers and most printed lines are clear; the main handwritten passages range from readable rapid cursive to tightly compressed formula work. The weakest readings are the cancelled multi-diagram draft in 113003, the diagonal marginal note in 112003, cancelled or overwritten passages in 114005–006, the two orientations and pencil prism of 115003, the lower exponent-heavy formulas of 115004, and the cancelled mixed-variance work in 115009. Individual printer identifiers and repeated banner-character counts are less secure where ruled paper, handwriting, folds, or clipped edges interfere.

Every page received a complete first pass and a second visual audit by the same transcriber, using the whole image and supplied halves, with additional crops and rotations where useful; no OCR was used. The second audit recovered small separators and correction layers and changed several readings. The uncertainty marks remain part of the transcription: they should not be treated as endorsements of the first alternative, and the diagrams' geometric placement is a typeset approximation of the ink rather than a facsimile.

The table gives human-readable positions and groups repeated occurrences of the same doubt. The inline macros are the authoritative indication of the exact scope of uncertainty, including deliberately incomplete formulas and ambiguous deletion extents. Syntax compilation checked braces, environments, and diagram destinations; it does not establish the correctness of a reading or the truth of a mathematical assertion.

## Pre-context notation review record

The exclamation signs, primes, circles, v-shaped dual signs, b/flat signs, ampersand-shaped superscripts, hooked Greek letters, ordinary/script/Gothic alphabets, and quotation marks were compared across the package before freezing. The raised/lowered f distinction in 108003 versus 114003 is supported by the ink; the 115004 exponent was not forced into the angular sharp/natural form of 115011–012. The conflicting arrow directions at the bottom of 115012, the repeated Hom argument order in 115011, and the uncertain equality/inequality in 114005 were preserved rather than corrected mathematically.
'''

(ROOT/'work_records/notation.md').write_text(notation)
(ROOT/(PREFIX+'_doubts.md')).write_text(notation+'## Doubts\n\n'+table+abbreviations)
print(f'Wrote notation table and {len(rows)} grouped doubt rows.')
