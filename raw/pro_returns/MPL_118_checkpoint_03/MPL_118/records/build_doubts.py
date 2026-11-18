#!/usr/bin/env python3
"""Assemble primary-reader judgments with literal, lossless doubt extraction."""
from pathlib import Path
from datetime import datetime, timezone
import json
ROOT=Path(__file__).resolve().parents[1]
data=json.loads((ROOT/'records/technical_qa/doubt_occurrences.json').read_text())

# These assignments are the primary reader's judgments after both image passes
# and the cross-page comparison. They are not inferred from language models,
# word length, a contextual edition, or automated image recognition.
LOW={
 3:{1},4:{3},5:{1,2,4,13,14,15,16,17,18,19,20,21,23,24,25,26,28,29},7:{1},
 8:{2,4,5},9:{1,2,4,6,7,9,10,12,13,14,15,16,18,19,20,21,22,23,24,25,26,28},
 10:{2,3,4},11:{1,6},12:{2,7,8,10,11,12,13,14},14:{2,4,5,8,9,11},
 15:{2,3,4,5,6,8,9,10,11,12,16,17,19,20,21,22,23,24,25,26,27,28,30,31,32,33},
 16:{1,2},17:{1,2,3,6,9,12,13},18:{1},19:{1,3,4,5,6},20:{1,2,3,4,5},
 21:{1,2,3,4,5,6,7,8,9,10,11,12,13},22:{1,2,3,4,5},
 23:{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15},24:{1,2,3,4,5,6,7,8,9,10,11},
 25:{1,3,6,7,10,11,12,13,14,15,16,17,18},
 26:{1,2,3,4,5,6,7,8,9,10,11,12,13,14,15},27:{1,2,3,4},
 28:{3,4,5},29:{1,3,4,5},30:{1,2,3,4,5,6,7,8,9,10,11,12},
 31:{1,2,3},32:{3,4,5},33:{3,4,5,6,7,8,9,10,11,12,13},
 34:{3,4,5,6,7},35:{1,2,3,4},36:{1,2,3},37:{1},
 39:{1,2,4,5,6,7,8,9,10,11},40:{3,4,5,7,14,15,16,17},
 41:{1,2,4,5,7,9,12,13,14,15,16,17,18,19,20,21,22}
}
# Ranges describe visual positions, not a reconstruction of manuscript line numbers.
REGIONS={
2:[(99,'cover title')],3:[(1,'upper lattice'),(99,'lower lattice')],
4:[(1,'typed heading'),(2,'financial amount, middle'),(99,'handwritten lower annotation')],
5:[(3,'upper-left equations'),(4,'top-right definitions'),(12,'upper and left notes'),(18,'central lattice revisions'),(21,'side annotations beside central lattice'),(23,'central/lower notes'),(99,'lower lattice')],
7:[(99,'typed name near left edge')],8:[(5,'isolated middle-left display'),(99,'lower diagram')],
9:[(3,'top paired columns'),(12,'upper proper/smooth criteria'),(13,'middle boxed duality band'),(20,'middle WSC/WSF columns'),(23,'lower WSB opening'),(24,'bottom oval diagram'),(99,'bottom explanation and conditions')],
10:[(1,'address panel'),(99,'envelope footer')],
11:[(1,'top heading'),(5,'upper factorization diagrams'),(7,'central cross'),(99,'lower cylinder diagrams')],
12:[(6,'upper diagrams and retraction'),(9,'central cross'),(99,'bottom-right marginal block')],
14:[(4,'upper table'),(6,'middle sketch and adjoint lines'),(99,'lower cross and inverse-image formulas')],
15:[(5,'top heading and numbered items'),(13,'upper span and revised diagram'),(17,'upper/middle numbered consequences'),(19,'middle theorem'),(28,'left NB with cancellations'),(29,'lower Question'),(33,'lower applications'),(99,'last line: overhead strokes')],
16:[(2,'first numbered heading'),(99,'last line')],
17:[(4,'upper gluing description'),(6,'central formulas'),(11,'lower homotopy block'),(99,'last lines')],
18:[(99,'typed examination-notice list, lower portion')],
19:[(1,'upper-right pencil'),(2,'upper-middle answer'),(4,'middle cancelled sketch'),(5,'middle proof outline'),(99,'bottom cancelled label')],
20:[(1,'upper assertion'),(3,'cancelled preliminary cube'),(99,'bottom fibre cases')],
21:[(3,'upper gluing square'),(6,'middle cylinder'),(9,'lower retraction statement'),(99,'bottom oblique lemma')],
22:[(1,'upper comparison diagram'),(5,'middle proof'),(99,'lower lemma')],
23:[(1,'author page number'),(5,'upper warning'),(9,'large lower example'),(99,'bottom example and consequences')],
24:[(1,'author page number'),(3,'top reference'),(9,'central square and prose'),(99,'lower cylinder')],
25:[(2,'central cylinder diagram'),(5,'lower introduction and (i)'),(8,'condition (ii)'),(9,'condition (iii)'),(12,'bottom condition (iv)'),(14,'right oblique margin'),(17,'left oblique margin'),(99,'inverted bottom pencil')],
26:[(2,'upper cancelled note and insertion'),(6,'middle altered argument'),(14,'left marginal and cancelled notes'),(99,'bottom localization argument')],
27:[(2,'upper corollary and margin'),(99,'middle lemma')],
28:[(1,'top lemma'),(4,'central equivalence and proof'),(99,'bottom cancelled factor')],
29:[(3,'main paragraph and zigzag'),(4,'bottom main paragraph'),(99,'inverted pencil')],
30:[(2,'upper-right annotation'),(9,'main Hom comparison'),(99,'last lines')],
31:[(2,'upper finite-subset construction'),(7,'upper surjectivity discussion'),(8,'central lemma'),(99,'bottom injectivity and Kan condition')],
32:[(1,'central Hom formula'),(4,'middle-lower prose and margin'),(99,'bottom cancelled proof opening')],
33:[(4,'top lemma heading'),(8,'middle numbered conditions'),(10,'left vertical margin'),(99,'lower injectivity argument')],
34:[(2,'upper quotient equalities'),(5,'middle reverse implication'),(99,'bottom argument')],
35:[(2,'upper category-of-elements comparison'),(3,'lower summary'),(99,'lower-left marginal qualification')],
36:[(1,'cancelled opening'),(99,'middle discussion')],37:[(99,'middle paragraph')],
39:[(3,'upper theorem'),(7,'left oblique margin'),(10,'middle proof'),(99,'last paragraph')],
40:[(2,'left upper filtration description'),(3,'left lower deleted explanation'),(5,'left foot corollary'),(13,'right cancelled proof, upper'),(14,'right cancelled proof, middle'),(16,'right cancelled proof, lower'),(99,'bottom-left diagram in cancelled proof')],
41:[(12,'top paragraph and overwritten labels'),(14,'cancelled middle sequence'),(18,'middle live sequence'),(20,'lower proof and cancelled lemma'),(21,'bottom limit diagram'),(99,'inverted cancelled blue name')]
}

HEAD=r'''# MPL 118: notation and reading doubts

## Notation table

This table records the primary reader's conventions after the personal first pass, the personal second audit of all 38 pages, and the final comparison across pages. The comparison was completed before the context archive was opened. Agreement means that the same visible sign receives the same encoding; it does not erase a visible change of notation or remove an unresolved alternative.

| Sign or usage | LaTeX encoding | Evidence and caution |
|---|---|---|
| Small round superscript for opposition | `^\circ` | Compared in the lattices (003, 005, 009), cylinder identities (011), and later duality statements (015–016). A closed round mark is kept distinct from a prime. |
| Prime and repeated primes | `'`, `''` | A raised short stroke is kept on the object or map on which it is drawn; displaced primes in cramped diagrams remain doubtful where marked. |
| Exclamation sign versus raised stroke | `\unsure{'\|!}` | The isolated display in 008 is unresolved. No secure exclamation-mark exponent was identified elsewhere; an expected convention has not been substituted. |
| Rounded b / flat exponent | `\unsure{f^b\|f^\flat}` and primed versions | The upright stem and rounded lower part recur in 011, upper 012, and the right column of 014. The alternative is retained consistently. |
| Sharp exponent | `f^\sharp`, `f^{\sharp\prime}` | The angular crossed sign in lower 012 and left 014 differs visibly from the rounded b/flat mark; it is not normalized to it. The small raised mark in 017 remains doubtful. |
| Fibration inclusion label | `\unsure{\eta_f\|H_f}` | The same unresolved upright/descending letter is kept in 011, 012, and 014. It is not silently identified by the factorization it might denote. |
| Retraction and section letters | `\rho_f`, `\sigma_f`, primed versions; `\lambda_f`, `\varepsilon_Y` | Compared through 011–014; the looped rho, capped sigma, and angular lambda are distinguished. Local overwritten labels remain marked. |
| Quotient letter in the later notes | `\unsure{\sigma\|\gamma}` | Compared in 031, 034, 040, 041. The closed upper loop/cap favours sigma on comparison; gamma is retained as an alternative at every occurrence. This comparison changed the preferred order in 031/034 before freezing. |
| Phi, psi and other Greek labels | `\varphi`, `\psi`, `\Phi`, `\alpha`, `\beta`, `\xi`, `\Theta`, `\Sigma` | Lower-case phi/psi in 012/014 and 039 are distinguished from the preceding quotient letter. Overwritten inverse-image and cone/suspension labels are explicitly doubtful. |
| Basic map classes | `F`, `C`, `S`, `T`, `W`, `\mathrm{Sm}`, `\mathrm{Pr}` | Compared in 003, 005, 008, 009. Multiletter labels remain abbreviations; they are not replaced by modern definitions. |
| Revised multiletter classes | `\mathrm{SprF}`, `\mathrm{SprC}`, `\mathrm{SprB}`, `\mathrm{WSF}`, `\mathrm{WSC}`, `\mathrm{WSB}` | Earlier Spr labels and later WSF/WSC/WSB labels coexist with visible cancellations. Unexpected WSE/WCF spellings are retained where read, not corrected to a preferred class. |
| Universal weak class | `uW`, `U\underline W` as locally written | The small initial letter in early lattices and capital in 015 are not assumed identical graphically; doubtful occurrences are marked. |
| Underlined and overlined classes | `\underline W`, `\overline W`, `\overline{\underline W}_A` | Underlines, overlines, and the index A are separately retained. A thick underline is not automatically a double underline. |
| Presheaf and copresheaf signs | `\widehat A`, `\widehat X`, `\check X` | Hats and checks in 012/014 and later presheaf arguments are distinct from opposition circles and from overbars. |
| Overbar versus short overhead arrow | `\overline{\widehat A}`, `\overline{\mathrm{Cat}}`; alternatives in 015 | The last line of 015 has blunt but slightly hooked stroke endings; both bar and arrow readings are recorded. Later clear bars in 024–025 are kept as bars. |
| Script class of maps | `\unsure{\mathcal M\|\mathcal A}` | Four occurrences in 025 share a highly stylized, partly overwritten letter. The surrounding ordinary category M remains plain/underlined M as visible. |
| Categories of elements and span symbol | `A_{/X}`, `\int` | Slice indices and slashes are literal. The integral-like mark before the upper span in 015 remains doubtful; a visible integral later in 015/020/022 is not replaced by a mere descriptive brace. |
| Slice and coslice notation | `X_{/b}`, `{}_{b}\backslash X`, `{}_{b_0}\backslash X_{/b_1}` | Compared in 003/009 and the later gluing and filtration pages. Index side, slash direction, and extra indices are retained individually. |
| Intervals | `I`, `I_\alpha`, `I_N`, `\Delta^1`, `\Delta_1` | Raised/lowered 1 is kept where seen. Several Δ¹/I readings in 017 remain open. In the upper object of the 025 cylinder, the multiplication-like stroke is `\unsure{\times\|\alpha}`. |
| Indexed families | `j`, `J`, `J_0`, `n`, `2n` | Lowercase j and uppercase J, zero and the raised/low index, are not inferred from the needed argument. In particular 031 retains `Y'_{J_0}\|Y'_j`; 041 retains `f_3\|f_2`. |
| Inclusion, inequality and crossed signs | `\subset`, `\not\subset`, `\neq`, `\notin`, `\le`, `\ge` | Direction and cancellation strokes were compared separately. A slash through a relation is not silently converted into a deletion of the whole expression. |
| Diagram strokes | `\arrow[...]`, `dash`, `dashed`, `hook`, shifted arrows | Solid strokes without visible heads are kept as headless lines; interrupted strokes are dashed. The headless diagonals in 034 and the conflicting small strokes in cancelled 040 are retained. |
| Opposite-direction and implication arrows | `\longleftrightarrow`, `\Longleftrightarrow`, `\Rightarrow`, `\Leftarrow` | Single and double shafts and arrowheads are distinguished. Faint or overwritten implications remain doubtful rather than being chosen by mathematical necessity. |
| Gluing functor and ordinary hom sets | `H_X`, `\mathrm{Hom}`, `\mathrm{Ob}`, `\mathrm{Fl}` | The subscript on H and the argument order in 017–021 are literal; later anomalous Hom formulas have not been repaired. |
| Coproducts, products, limits | `\amalg`, `\prod`, `\varinjlim`, `\varprojlim` where present | Signs and the direction under lim are read from the page. “fractions à droite” in 027 is kept even though 015/025 say “à gauche.” |
| Equality used as shorthand | `=` or `\equiv` as actually drawn | No word such as “même” is supplied in the transcription. In one doubtful 020 occurrence both symbol and word readings are recorded. |
| Double quotation marks | two backticks and two apostrophes | Encoded as LaTeX ``…'' where paired. The isolated ditto-like closing marks in 015 remain isolated; no opening quote was invented. |
| Underlining and emphasis rules | `\uline`, `\uuline`, `\vert`, `\Vert`, TikZ strokes | Horizontal double underlining and vertical single/double/triple margin rules are distinguished; braces are drawn as TikZ rather than described in the transcription. |
| Author's page numbers | `\mspage{...}` | Circled 1 and 2 at 019/020, 2 bis at 021, 3 at 022, doubtful 4/9 and 5 at 023/024, 6 and 7 at 025/026. Later pencil foliation is a comment only. |

## Reading doubts

Every `\unsure` occurrence is indexed below, including nested occurrences within deleted text or a larger doubtful phrase. “T” gives the exact line in the individual TeX page fragment, **not a manuscript line number**; the accompanying visual zone is approximate and makes the location usable without inventing line counts for diagrams and oblique margins. An em dash in Alternatives means that no second defensible reading was found, not that the first reading is secure. Confidence concerns the reading of the ink, not the truth of a mathematical statement; all choices were made by the primary reader, before context was opened.

The literal full macro, surrounding TeX, and offsets are also preserved in `records/technical_qa/doubt_occurrences.json` and `.tsv`. These are mechanical indexes of the transcription, not independent readings or OCR. A figure-level doubt in 040 concerns a local stroke state; its entire encoded diagram is preserved in that index and in the page file.

| Occurrence | File/cote | Scan | Approximate line / position | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|---|
'''

TAIL=r'''
### Geometry and page-state qualifications

These qualifications concern drawn extent or cancellation layers rather than additional unread words; they supplement the in-place doubt macros.

| File/cote | Scan | Approximate position | Reading | Alternatives | Confidence |
|---|---|---|---|---|---|
| 118 | 025 | Left of (ii), toward the beginning of (iii) | Curly stroke alongside the cancelled “modifier…” marginal note; the shape is reproduced | Whether it groups the two numbered conditions or belongs primarily to the marginal instruction is not certain | medium |
| 118 | 035 | Left of lower summary | First brace groups (i), (iv), (iv bis); second is drawn beside (ii), (ii bis) | A faint lower continuation of the second brace may extend toward (iii) | low |
| 118 | 040 | Right-hand proof and bottom-left small diagram | The long diagonals cancel the proof; the theorem and its corollary above remain live | The upward stroke from X′ toward X′₁ in the small last diagram may have an additional earlier local cancellation; both visible directions remain encoded under the doubt mark | low |
| 118 | 012 | Pale material over the last marginal equations | Tentative “étale” and “= Serre” remain in place | The second may be an overwritten earlier label rather than a live addition; the available contrast does not settle the layer | low |

## Abbreviations

The expansions below are tentative reading aids **only in this list**. Abbreviations, missing stops, contractions, and changes of language have not been expanded in the transcription. Mathematical symbols are included where they might otherwise be confused with word abbreviations.

| Abbreviation encountered | Tentative expansion (here only) |
|---|---|
| cat., Cat, (Cat) | catégorie(s), category/categories; the category of categories when used as a symbol |
| coh., prop. | cohomology/cohomological; properties/propriétés according to the heading's language |
| fib., fibs, cofib., cofib | fibration(s), fibered; cofibration(s), cofibered according to the grammar |
| imm., imm | immersion(s) |
| discr., discret | discretely / discrete; “discret” can also be a fully written French word |
| tr, triv., triv | trivial(e) |
| Sm, Pr | smooth; proper (class labels are retained literally) |
| Spr, WSF, WSC, WSB, WSE, WCF | Class labels; no confident letter-by-letter expansion is imposed in this transcription |
| As, Bias, Tot As, asph. | asphérique; bi-asphérique; totalement asphérique, tentatively according to the label |
| tot., génlt | totalement; généralement |
| univ., univt, univers.ly | universellement / universally |
| str | strict / strictement, uncertain in the short annotation |
| ch., chgt, changt, ch. de base | change / changement, changement de base |
| loc., coloc. | localement; colocalement, tentative in 009 |
| localis.tion | localisation |
| fonct., fonct | foncteur / functoriel according to context |
| c^t | constant; the written superscript is retained |
| hom., hom | homotopie / homotopique according to context |
| équiv., équiv | équivalence |
| th., thm., Thm | théorème |
| Cor., Cor, Coroll. | corollaire |
| Dém, Dém. | démonstration |
| resp. | respectivement |
| cf, cf. | confer / voir |
| p.ex. | par exemple |
| i.e. | id est / that is |
| it. | item / de même, tentative |
| ssi (possible sss) | si et seulement si; the final letters are doubtful where marked |
| tt, tte | tout, toute |
| gd | grand |
| mb, mb., m^b | membre |
| ens., ens | ensemble |
| él., él | élément |
| sglt., sgl. | singleton, tentative; neither reading is expanded in 023 |
| dblt | doublet, tentative |
| ss | sous |
| tjrs | toujours |
| néc. | nécessairement |
| surj. | surjectif / surjective |
| inj. | injectif / injective |
| cart., cart | cartésien |
| cocart., cocart | cocartésien |
| comm., comm | commutatif |
| diag., diag | diagramme |
| pr, pr. | projection when attached to a mathematical map; “pour” in some prose shorthand |
| faudr. | faudrait |
| croiss. | croissant(e)(s) |
| OPS | on peut supposer |
| NB | nota bene |
| je soup | je soupçonne, tentative in 029 |
| Ob, Fl, Hom, id | objects, arrows, hom set, identity; mathematical notation, not words expanded in the page files |
| R^i f_* | A mathematical expression, not a word abbreviation |
| D.E.A.; U.E.R. | diplôme d'études approfondies; unité d'enseignement et de recherche |
| M., MM., MR | Monsieur; Messieurs; Monsieur, according to the administrative form |
| HT | hors taxes, tentative handwritten annotation on 004 |
| B. O.; P. C. / P. 6. | Administrative or postal codes on 010; expansion not securely established |

## Legibility and limits of confidence

The typed administrative pages and much of the main mathematical prose are comparatively legible. The least dependable material is the crowded revision of the class lattices in 005 and 009, pale and overwritten notes in 011–014, densely cancelled words and altered labels in 015 and 023–026, the compressed last lines of 030, the oblique filtration margin in 039, and the overlapping cancellation layers in 040–041. Several personal names, inverted pencil jottings, and postal details remain tentative.

Each of the 38 supplied pages was read personally in full-page view and in its supplied halves, then audited personally a second time against the images; selected difficult areas were enlarged and rotated. No OCR was used, and no manuscript page was delegated for reading, transcription, or audit. The separate technical assistant only inspected saved file structure and literal macro counts. Its checks cannot certify a word reading or the completeness of an image transcription.

There are no `\illegible` blocks: tentative visible readings were preferred and explicitly marked. This does **not** mean that every stroke is legible or every tentative reading is reliable. The high number of low-confidence entries is intentional, especially where only a partial contour survives cancellation. Geometry is a hand-built TikZ approximation of the visible drawing, not a pixel facsimile. Static TeX checks found no structural issues, but the available TeX installation lacked its format/packages; no successful compile or rendered-layout verification is claimed.

The transcription was prepared without consulting the contextual edition or research returns. Subsequent contextual suggestions belong only in the research notes and cannot change the frozen text. The final progress log records the freeze hashes and their verification.
'''

def split_alt(s):
    level=0
    for i,c in enumerate(s):
        if c=='{' and (i==0 or s[i-1]!='\\'): level+=1
        elif c=='}' and (i==0 or s[i-1]!='\\'): level-=1
        elif c=='|' and level==0: return s[:i],s[i+1:]
    return s,''
def cell(s):
    if not s:return '—'
    return '`'+s.replace('\n',' ').replace('|',r'\|').replace('`','&#96;')+'`'

lines=[];judgments=[]
for d in data['occurrences']:
    n=int(d['occurrence_id'].split('-')[-1]);scan=d['scan']
    confidence='low' if n in LOW.get(scan,set()) else 'medium'
    region=next(label for last,label in REGIONS[scan] if n<=last)
    reading,alternative=split_alt(d['body'])
    if scan==40 and n==17:
        reading="X′ → X′₁ upward stroke, within the reproduced cancelled diagram"
        alternative='earlier local cancellation of that upward stroke'
    location=f'{region}; T{d["tex_line"]}'
    lines.append(f'| {d["occurrence_id"]} | 118 | {scan:03d} | {location} | {cell(reading)} | {cell(alternative)} | {confidence} |')
    judgments.append({'occurrence_id':d['occurrence_id'],'position':region,'confidence':confidence,
                      'source':'primary-reader personal image audits and pre-context notation comparison'})
(ROOT/'MPL_118_doubts.md').write_text(HEAD+'\n'.join(lines)+'\n'+TAIL)
(ROOT/'records/doubt_judgments.json').write_text(json.dumps(judgments,ensure_ascii=False,indent=2)+'\n')
stamp=datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')
with (ROOT/'progress.log').open('a') as f:
    f.write(f'doubts register completed {stamp}; {len(lines)} literal unsure occurrences with primary-reader confidence judgments, plus four geometric/page-state qualifications\n')
print(json.dumps({'occurrences':len(lines),'low':sum(x['confidence']=='low' for x in judgments),
                  'medium':sum(x['confidence']=='medium' for x in judgments),'utc':stamp}))
