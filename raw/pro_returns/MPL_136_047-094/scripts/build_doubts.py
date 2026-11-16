#!/usr/bin/env python3
"""Format the primary reader's recorded doubts, without reading images or context.

Uncertainty content is extracted mechanically. Confidence policy and the notation
comparison were supplied by the single primary reader after the two source-image
readings, before the context archive was opened. Abbreviation expansions were
subsequently supplemented from the frozen source only; no page reading changed.
"""
from pathlib import Path
import sys, csv, json, re, hashlib
sys.dont_write_bytecode = True
from extract_doubts import extract

root = Path(__file__).resolve().parents[1]
records=[]
for path in sorted((root/'pages').glob('*.tex')):
    data=path.read_bytes()
    found,errors=extract(data.decode(), 'pages/'+path.name, path.stem[-3:], hashlib.sha256(data).hexdigest())
    if errors: raise RuntimeError(errors)
    records.extend(found)

head=r'''# Notation table and doubts — cote 136, scans 048–094

## Recurring notation: final source-only comparison

| Visible form / distinction | Encoding used | Locations and limits of the reading |
|---|---|---|
| Asterisk above a letter | `C^*`, `A^*`, `H^*` | The drawn star is retained; it is not systematically converted to a bullet. |
| Asterisk below a letter | `X_*`, `C_*`, `A_*` | Subscript position is retained, separately from superscript cochain degree. |
| Two gradings | `C^{p,q}`, `A^{**}`, or the visible dots | Commas, stars and dots follow the particular occurrence; no uniform mathematical reindexing is imposed. |
| Normalized-cochain exclamation | `C_{*M}^{*!}`, `C_{*M}^{n!}` | Scans 050, 052, 068, 069: the stroke and detached dot distinguish this from a prime; this was checked across the page stream. |
| Prime | `'`, `S_X^{\prime *}` | Especially scans 070–072 and the primed modules of 082–091; it is not converted to an exclamation mark. |
| Stroke after `(K_n)` | `\unsure{'\|$\exists$}` | Scan 068, opening paragraph: apostrophe-like ink is the first reading; no missing verb has been supplied. |
| Integration operator versus coefficient ring | `K_n` versus `k` | Compared on 054, 056, 065–070, 072; local `K_n\|k_n` alternatives remain on 054, 069, 072 where the arm/stem is weak. |
| Coefficient module in cochain notation | `C_{*M}^*`, `C_{0M}^0` | Scans 065–069: M belongs to the lower index in these occurrences; it is not silently moved to a tensor factor. |
| Phi versus Q | `\Phi`, locally `\unsure{\Phi\|Q}` | Compared on 052, 068, 069, 074–089: the central stem generally supports Phi, but faint local forms retain alternatives. |
| Phi versus Psi | `\Phi`, `\Psi` | The round body and fork are distinguished; ambiguous cases remain marked, including 078 and 089. |
| Bar, tilde, hat | `\bar\Phi`, `\widetilde N`, `\widehat\Phi` | Decorations are retained individually, including doubtful hat on 080 and tilde/direction-like stroke on 089. |
| Lowercase lambda and mu | `\lambda`, `\mu` | Morphisms in 082, 085, 087, 089; uncertain overbars/tilde are not silently standardized. |
| Exterior algebra / divided powers | `\Lambda`, `\Gamma` | Both occur and are sometimes overwritten or deleted (074, 080); the deletions remain visible in the encoding. |
| Capital T and lowercase t | `T`, `t`, `\bar T` | Marked generator, coefficient and exterior image remain distinct; e.g. `(T-t)_{\mathrm{pd}}` on 069. |
| Boundary and differential | `\partial`, `d`, `\delta` where legible | No replacement of one by the expected differential is made; indices remain as drawn. |
| Opposite-category small circle | `^{\circ}` | Scans 058–062 and 091; it is not expanded to `op`. |
| Hatted simplex category | `\widehat\Delta`, `\widehat{\Delta/X}` | Hat and slash are retained where visible; they are not supplied to an undecorated Delta. |
| Half sign before simplicial | `$1/2$` or `\frac12` in the visible context | The shorthand is retained without deciding a modern terminological convention in the transcription. |
| Roman, script and blackboard forms | `\mathrm{DR}`, `\mathcal{DR}`, `\mathbb{DR}`; `\mathcal E`, `\mathcal X` | Distinctions visible on 062 and 089–094 are retained. Some manuscript forms are not typographically unique; doubtful occurrences are marked. |
| Arrow versus plain dash | `\longrightarrow`, `\mathbin{-}`, `\text{---}` | A missing head is not supplied for mathematical convenience; scan 078 explicitly gives the dash first. |
| Double-headed / reversed arrows | `\xleftrightarrow`, TikZ directions and labels | Directions are read locally. The lowest comparison edge on 072 remains a low-confidence direction, separately registered below. |
| Zero versus letter o | `0`, `o`, or `\unsure{o\|0}` | Especially reused typed sheets 055, 063; baseline and typewriter shape do not always decide. |
| Unit l versus digit 1 | `l`, `1`, or a local doubt | No change is inferred from mathematical expectations. |
| Double quotation marks | two backticks and two apostrophes | Used consistently for visible double quotes. A font's curved appearance does not change the source encoding. |
| Equals-sign shorthand in prose | `$=$` | Scans 077, 085: preserved, including `lui-$=$`; proposed expansion appears only in the abbreviations list. |
| Underlining | `\uline`, `\uuline` | Separate single/double strokes retained; the emphatic triple-underlined Non on 091 is encoded by nested permitted underline macros. |
| Circled letters/numbers | `\textcircled{...}` or TikZ ellipse | Shapes are reproduced; a circled D on 077 has its own drawing inventory row although it is not a `\figure` macro. |
| Deletions inside a deletion | nested `\deleted` | Scans 062, 072 and elsewhere: local crossings and the cancelled outer block are both represented. |
| Foliation in a different, usually pencil hand | `\margin{n}` | It is not asserted to be Grothendieck's authorial numbering; therefore no `\mspage` is supplied merely from its position. |
| Typed page headers | `\margin{...}` | Printed/typewritten numbers and chapter headings are retained as sheet content, not assigned as manuscript pagination. |

## How to use the doubt table

Each row registers one uncertainty macro in a page fragment, including nested macros; it does not replace the uncertainty in the transcription. The **file/cote** is 136, and the page filename is given by the uniform pattern `pages/MPL_136_047-094_136_scanNNN.tex`. The locator gives the LaTeX source line and a short surrounding phrase: these are reproducible approximate locators, **not a claim to have counted physical manuscript baselines** (displays and insertions do not have a unique baseline order). The first alternative is always the reading retained from the ink; grammatical or mathematical expectation has not reordered the alternatives.

Confidence is a qualitative judgment of the primary reader, not a probability: **low** for physically lost words, the very faded sheets 048/050/052, long or nested doubtful passages, and the most crowded corrections; **medium** for a plausible but unresolved local reading. None of the unresolved macro readings is promoted to high confidence just because it makes mathematical sense. Nested records may repeat a portion of a longer uncertain passage intentionally. An empty alternative means that no second defensible reading was found, not that the reading is secure. The transcript contains 494 `\unsure` occurrences and 50 `\illegible` occurrences before freezing.

| ID | File / cote | Scan | Approximate line / source locator | Reading retained | Alternatives | Confidence |
|---|---|---|---|---|---|---|
'''

def cell(s):
    s=' '.join(str(s).split()).replace('|','&#124;')
    # Backticks in the manuscript quotation encoding must remain literal.
    return '<code>'+s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;').replace('&amp;#124;','&#124;')+'</code>'

lines=[head]
for r in records:
    parts=json.loads(r['top_level_bar_parts'])
    low=r['scan'] in {'048','050','052'} or r['macro']=='illegible' or len(r['content'])>110 or bool(r['parent_id'])
    if r['scan'] in {'070','072','076','077','089','094'} and ('deleted' in r['context'] or 'inserted' in r['context']):low=True
    conf='low' if low else 'medium'
    reading=parts[0] if r['macro']=='unsure' else '\\illegible{'+r['content']+'} — estimated unreadable word count'
    alternatives=' ; '.join(parts[1:]) or 'No secure alternative'
    context=r['context']
    if len(context)>180:context=context[:85]+' … '+context[-85:]
    loc=f"TeX L{r['tex_line']}; {context}"
    lines.append(f"| {r['record_id']} | 136 | {r['scan']} | {cell(loc)} | {cell(reading)} | {cell(alternatives)} | {conf} |\n")

lines.append(r'''
### Additional uncertainties not reducible to a single lexical macro

| ID | File / cote | Scan | Approximate line / source locator | Reading retained | Alternatives | Confidence |
|---|---|---|---|---|---|---|
| M1 | 136 | 072 | Lowest edge of the comparison cube | Leftward direction, with doubtful comparison label | Rightward head is possible where strokes overlap; the cube is not repaired from its expected commutativity | low |
| M2 | 136 | 048–094 | Marginal pencil-like numbers, generally one less than the scan number | Number transcribed as a margin | Authorial versus later foliation is not established by these images | low |
| M3 | 136 | 062, 072, 085, 089, 091 | Cancelled or overlaid diagrams | Objects and arrows typeset with the indicated local doubts | Some crossing strokes may belong to cancellation rather than an additional arrow; geometric spacing is approximate | low |
| M4 | 136 | 070 | Insertion adjoining item 2 | Crowded phrase beginning “et si on remplace” and including both S(X) and S(X)' | Exact word order and attachment remain uncertain; no syntactically smoother wording supplied | low |
| M5 | 136 | 075 | Sentence beginning “est faux” | The retraction is clear; the next underlined verb is `tuer` with `lier` alternative | No stronger reading is justified by the strokes | low |
| M6 | 136 | 094 | Hodge-type coefficient and final localization assertions | Indices, bounds and missing qualifications retained as written | Potential mathematical emendations are questions for the research notes, never silent source corrections | medium |

## Abbreviations met

Expansions below are editorial aids only. They have **not** been substituted in the page files; alternatives are given where the abbreviation admits more than one expansion. Mathematical object names are listed only when they also function as manuscript shorthand. Personal initials and standard unit symbols on reused notices are retained as printed and are not expanded into unverified names.

| Form on the sheets | Proposed expansion / sense | Representative scans |
|---|---|---|
| `1/2 simplicial`, `ss`, `ss.` | semi-simplicial / semi-simpliciaux in the author's terminology; modern convention requires separate examination | 054–069, 074, 091 |
| `SS` | category/topos of the semi-simplicial objects under discussion | 058, 074 |
| `ab.`, `(Ab)` | abéliens; category of abelian groups | 052, 058, 062 |
| `Alg.`, `alg.` | algèbre(s) | 074, 094 |
| `ant.` | antérieure(s) | 091 |
| `augm.` | augmentation | 070 |
| `av.` | avec | 062 |
| `bidegr.` | bidegré(s) | 083 |
| `can.`, `can` | canonique | 048, 064, 066 |
| `cat.`, `cat`, `Cat.` | catégorie | 056, 062, 066, 072, 089, 094 |
| `Chap` | chapitre | 059 |
| `coch.` | cochaînes | 070 |
| `coeff.` | coefficients | 060, 062, 064 |
| `coh.` | cohomologie | 064, 082 |
| `comm.`, `comm` | commutatif/commutative; commutant where attached to a diagram | 064, 072, 074, 080–085 |
| `comp.` | complexe; compatible, according to phrase | 070, 083 |
| `compl.` | complexe(s) | 089 |
| `cov.` | covariant | 062 |
| `deg.`, `deg`, `degr` | degré(s) | 083, 089 |
| `dér.` | dérivée(s) | 094 |
| `diff.`, `diff` | différentiel/différentielle | 054, 060, 074, 080, 089, 091, 094 |
| `div.` | divisée(s) | 077, 091, 094 |
| `p.d.`, `p. d.`, `p.d`, `pd`, `p. div.` | puissances divisées | 053, 069, 074–077, 080, 083, 089–094 |
| `ens.` | ensemble(s) | 048, 058, 091 |
| `Ens` | ensembles | 050, 058 |
| `ép.` | épimorphisme/épimorphe, tentative | 050 |
| `épi.`, `épim.` | épimorphisme | 048, 083 |
| `etc.` | et cetera, where actually written | 058 |
| `ex.` | existence in “ex. et un.”; exemple in “par ex.” | 054, 060, 070 |
| `un.` | unicité | 054 |
| `ext.`, `ext` | extérieur | 083, 089, 091 |
| `faç.` | façon | 076 |
| `f.`, `f` in the typewritten schematic discussion | fixe / partie fixe | 073, 092 |
| `gén.` | général | 054 |
| `gr.` | gradué in “alg. diff. gr.”; groupe when that phrase requires it | 070, 074, 076 |
| `hom`, `hom.`, `homom.` | homomorphisme | 054 onward, 087 |
| `homot` with superscript `t` | homotopiquement, tentative expansion of the superscript contraction | 072 |
| `hyp.` | hypothèse(s) | 056, 072 |
| `i.e.` | id est | 048 onward |
| `infér` with superscript `t` | inférieurement, tentative reading and expansion | 060 |
| `inj.` | injectif/injection | 048 |
| `iso.`, `isom.`, `Isom.` | isomorphisme(s) | 048, 050, 064, 072, 082, 089, 091 |
| `quasi-isos` | quasi-isomorphismes | 094 |
| `lib.` | libre | 083 |
| `lin.` | linéaire | 085 |
| `loc.` | localement | 064, 077, 083 |
| `loc. lib.` | localement libre | 083 |
| `mod.` | modulo | 073 |
| `mb` | membre | 082 |
| `endom` | endomorphismes | 056 |
| `m.` (alternative reading), `=` in prose | même; equals-sign shorthand is retained literally, including “lui-=” | 077, 085 |
| `NB` | nota bene | many sheets |
| `néc.` | nécessaire | 065, 076 |
| `op.` | opération(s) | 054, 065, 077, 080 |
| `par r. à` | par rapport à | 062 |
| `p.ex.` | par exemple | 060, 070 |
| `pr.` | projection, in the diagram label “pr. sur” | 072 |
| `prop.` | propriété(s) or proposition, according to phrase | 067 |
| `proven.` | provenant | 064 |
| `puiss.` | puissances | 077 |
| `rel.` | relation(s) | 076 |
| `rés.` | résolution | 070 |
| `resp.` | respectivement | 059, 062, 073 |
| `satisf.` | satisfaisant | 070 |
| `sing.` | singulier/singulière | 070 |
| `qd` | quand | 069 |
| `tjs` | toujours | 069 |
| `cqfd` | ce qu’il fallait démontrer | 056 |
| `ds` | dans | 060, 064 |
| `dfn`, `déf` | définition | 050, 060, 064 |
| `ssi` | si et seulement si | 068 |
| `suppl.` | supplémentaire(s) | 060 |
| `surj.` | surjectif/surjection | 069 |
| `syst.` | système | 062, 065, 067–069, 085, 089 |
| `tot.` | total | 074 |
| `tt` | tout | 066, 067 |
| `tte` | toute | 091 |
| `ttes` | toutes | 082, 085, 094 |
| `élémt` | élément | 067, 089 |
| `univ.`, `Univ.` | universellement / universel, according to noun or adjective | 094 |
| `Ob` | objets (of a category) | 048, 066, 091 |
| `App` | applications | 067 |
| `Ker`, `Coker`, `Hom`, `Isom`, `Ext` | kernel, cokernel, homomorphisms, isomorphisms, extension groups | formulas throughout |
| `DR`, `DRpd`, `DRsp` and decorated forms | De Rham; divided-power and special variants as locally indicated | 074–094 |
| `EGA`, `SGA` where printed | Éléments de géométrie algébrique; Séminaire de géométrie algébrique | reused mathematical sheets |
| `U.E.\unsure{R}.` | unité d'enseignement et de recherche | 084 |
| `S.M.F.` | Société mathématique de France | 084 |
| `U.S.T.L.` | Université des sciences et techniques du Languedoc | 086 |
| `CNRS` | Centre national de la recherche scientifique | 086 |
| `UV` | ultraviolet | 086 |
| `RMN` | résonance magnétique nucléaire | 086 |
| `Mme`, `MR` | Madame; Monsieur | 084, 086 |
| `N°`, `n°` | numéro | 086, 088 |
| `AMC/GJ` | administrative initials/code; expansion not established | 086, 088 |

## Legibility and scope of trust

The least trustworthy sheets are **048, 050 and 052**, where fading and physical loss of ink affect continuous prose as well as formula labels. Whole pages, both supplied overlapping halves, enlarged views and additional contrast views were inspected. A plausible reading was preferred to an unreadable-word count whenever the residual strokes supported one; the remaining `\illegible{n}` marks estimate physically unreadable words and are not substitutions for missing mathematical symbols. Their 50 occurrences do not mean only 50 words: the argument records an estimated count.

The next most difficult features are the overwritten and cancelled diagrams on **062 and 072**, the cramped insertion on **070**, the dense product/divided-power revisions on **075–077**, and the indices and category notation on **089–094**. Drawing coordinates reproduce relative layout approximately and are not a facsimile. A successful LaTeX compilation establishes syntax only: it neither verifies a reading nor proves a mathematical assertion. Reused typed leaves are generally clearer, but broken typewriter glyphs, handwritten corrections and the distinction between zero and letter o remain locally uncertain.

All 46 included scans were transcribed and personally read again by the same primary reader. No OCR or delegated image reading was used. A separate worker checked only source syntax, macro balance, inventory counts and trial compilation. Blank scans 047 and 079 were absent from the supplied image set. The context archive was kept closed until the page files and combined transcription were frozen; any context-derived alternative belongs in the research notes and cannot alter those files.
''')
out=root/'MPL_136_047-094_doubts.md'
out.write_text(''.join(lines),encoding='utf-8')
print(f'Wrote {out}; {len(records)} macro rows plus 6 additional uncertainty rows.')
