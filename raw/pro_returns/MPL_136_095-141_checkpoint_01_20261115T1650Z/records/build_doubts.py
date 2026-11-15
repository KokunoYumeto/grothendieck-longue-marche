#!/usr/bin/env python3
"""Build the English doubt table from root's visual audit and exact marker index."""
from pathlib import Path
import json
import re

BASE = Path(__file__).resolve().parent.parent
ITEMS = json.loads((BASE.parent/'technical_checks/doubt_occurrences.json').read_text())

HEADER = r'''# Notation table

This table records the single reader's visual reconciliation before the transcription was frozen. Differences of position, alphabet, degree, or decoration have been retained when the ink differs; the table does not normalize mathematical meaning. Scan references are to archive cote 136. A doubtful first reading is the reading preferred from the ink, not a correction inferred from the mathematics.

| Recurring sign or convention | LaTeX used | Visual distinction and checked scope |
|---|---|---|
| Completion circumflex | `\widehat X`, `\widehat S`, `\widehat A` | Circumflex distinguished from tilde and the small v of the typed dual module; 095, 099–105, 108, 125. |
| Typed dual-module v | `\check{\underline M}` and primed variants | Small v above M, with underline and prime separately retained; 097, 114, 128, 138. |
| Bigrading | `A^{**}`, `A^{ij}`, `A^{1\,0}` | Both positions retained; the target in 096 is primarily read as `2\,0`, still doubtful, not repaired to another bidegree. |
| De Rham categories | `\mathrm{DR}_{\mathrm{sp}}`, `\mathrm{DR}_{\mathrm{spufl}}` | The same primary readings recur in 096–108; uncertainty remains where an individual suffix is faint. |
| Primes on categories | `\mathrm{DR}_{\mathrm{sp}}'` and `\mathrm{DR}_{\mathrm{spufl}}'` | Actual short raised strokes in 102–106; not exclamation marks. |
| Phi, phi, and Psi | `\Phi`, `\varphi`, `\Psi` | Closed loop/stem, lower-case loop, and open fork distinguished in 096–108; 106 retains `\Phi_*` versus `Q_*` as a local doubt. |
| Gamma algebra and gamma operation | `\Gamma`, `\gamma` | Capital Gamma for algebra/functor notation; lower-case gamma for operations or coefficients. Circumflex and prime/star remain separate in 125. |
| Gamma star position | `\gamma_*`, `\gamma^*`, `\gamma_i^*`, `\gamma_*^{k'}` | The manuscript changes subscript/superscript placement, notably 123–141. These are not silently made uniform. |
| Chain and cochain stars | `C_*^{\mathrm{DR}}`, `C^*_{\mathrm{DR}}`, `C_*^{DRpd}`, `C^*_{DRpd}` | Lower versus upper stars retained throughout 127–141; integral coefficient formulas in 133–135 checked separately. |
| Half-simplicial notation | `\frac12` followed by the written word | Not expanded in the transcription; inserted `co` in 127 remains an insertion. |
| Opposite-category marks | `\mathrm{Ss}^{\circ}`, `\Delta^{\circ}` | Small raised circles retained in 111 and related functor notation. |
| Tau and lambda | `\tau_\infty`, `\lambda(p)`, `\lambda(\infty)` | Tau is not t; the last argument in 117 is primarily infinity, with zero retained as an alternative. |
| S variants | `S`, `S_k`, `S^+`, `\bar S`, `S^{k'}` | Bar, plus, coefficient index and dual-valued superscript are separate; 111–141. |
| Parameter letters | `T`, `t`, `u`, `U` | Capitalization retained as written, including the polynomial-coalgebra variables of 131–139. |
| Polynomial versus PD delimiters | `[X_i]`, `\{X_i\}`, `\{\{X_i\}\}` | Number and shape of delimiters retained; overwritten delimiters in 141 remain doubtful. |
| Divided-power exponents | `X_i^{(j)}`, `t^{(\lambda)}` | Parentheses are part of the written exponent, not an editorial convention; 125, 139, 141. |
| Exterior generators | `dX_i`, `y_i`, `\Lambda^*`, `\bigwedge^*` | Capitals and lower-case dual generators retained; 125–141. |
| Exclamation-like versus prime superscripts | `^{\unsure{!|'}}`, `^{\unsure{'|!}}`, and `'` | In 139 the first two marks have a separate dot and are primarily `!`; the later NB and exact-sequence marks look like primes. The visual difference is preserved and explicitly flagged. |
| Kappa versus pi | `\kappa_n`, `\kappa^n`, `\unsure{\kappa^n|\pi^n}` | Angular handwritten shape in 137–141; index position follows each occurrence. |
| Inequalities | `\leq`, `\geq`, `<`, `>` | Read separately, including the lower bounds in 117, divergence condition in 119 and simplex bounds in 141. |
| Directed versus undirected edges | `\arrow[r]`, `\arrow[l]`, `\arrow[...,dash]` | An unheaded stroke stays unheaded, especially 104, 115, 121, 137 and 139. Right-to-left typed isomorphisms in 140 remain leftward. |
| Inclusions and epimorphisms | `tail`, `two heads`, occasionally both | The handwritten arrow decorations in 139 have both head and tail features and are reproduced as drawn. |
| Limits | `\varprojlim`, `\varinjlim`, underlined `\lim` | No direction added to the simply underlined limit signs of 111. Explicit arrows retained elsewhere. |
| Double quotation marks | two backticks and two apostrophes | Applied to visible double quotes, including 102, 121, 129, 133, 139 and 140. A visibly unclosed quote remains unclosed. |
| Ditto-like strokes | literal dashes or `\unsure{\text{``}|=}` | Pairing cases in 139 retain dash repetition; the isolated mark in 129 remains doubtful. |
| Underlining | `\uline`, `\uuline` | Single versus double strokes retained, including headings and individual summation indices. |
| Source page numbers | `\mspage{n}` for typed text pagination; marginal labels in `\margin` | Printed text-page numbering is separate from tape/sticker numbers and later pencil scan labels. None is silently converted into a lecture page count. |

# Doubts

Each row below corresponds to one occurrence of `\unsure` or `\illegible` in the final page files, including nested occurrences and cancelled material. The line locator is the **line in the individual page's LaTeX source**, a reproducible approximate locator for the passage, not a claimed count of handwritten lines. The file column gives the exact basename within `pages/`; readings are literal LaTeX where appropriate. “No distinct alternative” means that a competing decipherment could not responsibly be proposed, not that the reading is certain.

Confidence is conservative: **medium** indicates a plausible local reading with a remaining visual ambiguity; **low** indicates faded, overwritten, cancelled or substantially incomplete ink. The especially faint scan 108 is low throughout. No context source was used to assign or improve a reading.

| File (cote 136) | Scan | LaTeX line / state | Reading | Alternative or issue | Confidence |
|---|---:|---|---|---|---|
'''

FOOTER = r'''

# Abbreviations encountered

Expansions here are interpretive aids only. They have not been substituted into the transcription. Some strings are labels or conventional mathematical notations rather than abbreviations in a narrow linguistic sense.

| Written form | Probable expansion or function |
|---|---|
| `Ab.` | abelian (groups), in the English minimal-model sheet |
| `Alg.`, `alg.`, `algs.` | algèbre(s), algebra(s) |
| `ass.` | associatif/associative |
| `augm.` | augmentation |
| `bas.` | based (English) |
| `can.` | canonique |
| `car.` | caractéristique |
| `cat.` | catégorie |
| `cf.` | confer; compare / see |
| `coalg.` | coalgèbre |
| `codiff.` | codifférentielle |
| `coh.` | cohomologie |
| `comm.`, `commut.` | commutatif/commutative; a commuting diagram where applicable |
| `compl.` | complémentaire in grading language; completed/completion must be judged locally |
| `Conj.` | conjecture |
| `coord.` | coordonnées |
| `copuiss.` | copuissances |
| `cor.`, `cor. thé.` | corollaire; damaged typed reference in 136 may combine corollary and theorem wording |
| `cqfd.` | ce qu'il fallait démontrer |
| `deg`, `degr.`, `degré tot`, `deg ext` | degree; total degree; exterior degree (the precise written form varies) |
| `dfn` over an equality | definition |
| `diag.` | diagramme |
| `diff.` | différentielle, différentiel, or differential according to the noun |
| `div.`, `p.d.`, `p. div.`, `p.div.` | divisées; puissances divisées |
| `DR`, `DR.`, `DRpd` | De Rham; De Rham à puissances divisées |
| `ds` | dans |
| `dér.` | dérivée |
| `ens.` | ensemble(s) |
| `équiv.` | équivalent(e) |
| `ext.` | extérieur / exterior |
| `gr`, `gr.` | groupe or gradué, according to the local phrase |
| `group.` | group (English) |
| `hom`, `hom.` | homomorphisme; in “idéal hom.”, homogène |
| `i.e.` | id est, that is |
| `int.` | intérieur in “prod. int.” |
| `iso`, `iso.`, `isom.`, `isom` | isomorphisme / isomorphism |
| `k-m` | k-module |
| `lim`, `Lim` | limit; direction only where the manuscript draws it |
| `Mod` | modules / category of modules |
| `NB` | nota bene |
| `néc` | nécessairement |
| `obj`, `ob`, `Ob` | objet(s) |
| `op. diff.` | opérateurs différentiels |
| `p. ex.` | par exemple |
| `par.` | paragraphe |
| `ponct.` | ponctuel(le) |
| `pr` | unresolved shortened word in the very uncertain NB of 121; not expanded confidently |
| `prod.` | produit |
| `proj` / projective-limit notation | projectif, where used |
| `puiss.` | puissances |
| `quelc.` | quelconque(s) |
| `resp.` | respectivement |
| `SGA` | Séminaire de géométrie algébrique |
| `sp`, `spufl` | spécial; spécial universellement flasque, as category suffixes |
| `Ss`, `ss` | the semi-simplicial-set notation used on these sheets; preserved literally |
| `ss-e.v.` | sous-espace vectoriel |
| `str.` | structure(s) |
| `surj.` | surjectif / surjective |
| `syst.` | système |
| `th.`, `thé.` | théorème |
| `tt`, `ttes`, `tous` in abbreviated phrases | tout / toutes where actually abbreviated |
| `ufl.`, `univ.` | universellement flasque; universel(le)/universellement |
| `uni`, `uni.`, `unit.` | unitaire |
| `vect.` | vecteurs |

# Legibility assessment

The reused typescript pages are generally substantially more legible than the handwritten mathematical sheets. Nevertheless, tape, show-through, misstruck type, very small indices and blue marks produce local uncertainties. Their unrelated text, German note, English mathematical sheet, French letter, printed pagination and later marginal labels have all been retained as source content rather than used to reconstruct the lecture.

**Scan 108 is the least reliable page.** Much of the ink has physically disappeared; the whole image, both supplied halves and a further enlarged/contrast inspection did not recover it. Its long guessed formulas and isolated words remain explicitly uncertain, and the unreadable prose is represented by estimated word counts. The lower margins of 119 and the NB of 121 are also particularly weak. In 125, 131, 133 and 135, faint writing makes individual exponents, short connective words and attachments less secure.

Scans 137 and 141 are readable in broad outline but contain dense cancellations, overwritten indices, inserted factors and long formulas running close to an edge. Their order and visible alterations are preserved; this is not a claim that every overwritten mathematical symbol has been recovered with confidence. Scan 139 has an especially consequential exclamation/prime ambiguity and a questionable exterior degree, all recorded locally. Small nonverbal pen marks and curves are reproduced as TikZ approximations; their geometry is necessarily less exact than the image.

The second visual audit covered all 46 supplied pages, in ascending scan order, after the initial whole-page and half-page reading. The source omits blank scan 122. The mechanical LaTeX compilation checks syntax only; it cannot establish paleographic accuracy. The transcription deliberately leaves surprising mathematics, incomplete brackets and open quotations where the ink leaves them. Contextual or mathematical proposals to change a reading belong only in the separate research notes after the freeze.
'''

def escape(value):
    return str(value).replace('&','&amp;').replace('|','&#124;').replace('<','&lt;').replace('>','&gt;').replace('\n',' ')

def alternatives(raw):
    # Only a single top-level vertical stroke is an alternative separator.
    depth=0; cuts=[]
    for i,c in enumerate(raw):
        if c in '{}':
            slash=0;j=i-1
            while j>=0 and raw[j]=='\\': slash+=1;j-=1
            if slash%2==0: depth += 1 if c=='{' else -1
        elif c=='|' and depth==0 and (i==0 or raw[i-1]!='\\'): cuts.append(i)
    if len(cuts)==1:
        i=cuts[0];return raw[:i],raw[i+1:]
    return raw,None

def confidence(item):
    scan=item['scan'];raw=item['raw_contents']
    if item['macro']=='\\illegible':return 'low'
    if scan in {108,121,135,137,141}:return 'low'
    if '\\deleted' in item.get('enclosing_macros',[]):return 'low'
    if scan in {119,125,131,133,139}:return 'low'
    return 'medium'

rows=[]
for item in ITEMS:
    if item['macro']=='\\illegible':
        reading='unreadable prose';alt=f"Approximately {item['raw_contents']} word(s); physically unrecovered ink"
    else:
        reading,alt=alternatives(item['raw_contents'])
        alt=alt or 'No distinct alternative; locally doubtful reading'
    state=', '.join(x.lstrip('\\') for x in item.get('enclosing_macros',[]) if x in {'\\deleted','\\inserted','\\margin'})
    loc=str(item['source_line'])+(' / '+state if state else '')
    values=[Path(item['file']).name,f"{item['scan']:03d}",loc,reading,alt,confidence(item)]
    rows.append('| '+' | '.join(escape(x) for x in values)+' |')

out=HEADER+'\n'.join(rows)+f'\n\nTotal indexed doubt occurrences: **{len(ITEMS)}**.\n'+FOOTER
(BASE/'MPL_136_095-141_doubts.md').write_text(out)
print(f'Wrote {len(ITEMS)} doubt rows with notation reconciliation and legibility assessment.')
