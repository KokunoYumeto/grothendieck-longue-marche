#!/usr/bin/env python3
"""Index the root reader's explicit doubts; never infer or alter readings."""
from pathlib import Path
import json
import re
from reconcile_inventory import macro_spans

ROOT = Path(__file__).resolve().parents[1]

HEADER = r'''# Recurring notation and comparison record

This table was maintained from scan 133 and expanded after the second visual reading, before the context archive was opened. The root reader compared recurring forms across the page files and the scans; uncertain variants have not been made certain merely for consistency.

| Ink / recurring usage | LaTeX convention and examples | Comparison / caution |
|---|---|---|
| One and two underlines | `\uline{…}`, `\uuline{…}`; mathematical `\underline{…}` | Underlined sheaf letters and double-underlined functor names are distinct from an alphabet change. Scans 133, 142, 158–162, 173–179. |
| Double quotation marks | Two backticks and two apostrophes | Checked in 133, 135, 143, 147, 151, 160, 171, 179. |
| Printed guillemets | `« … »` | Retained on the reused printed sheets 154 and 163; not substituted for handwritten double quotation marks. |
| Plain connector and arrowhead | `-`, `\mathbin{\text{---}}`, or TikZ-CD `dash`; arrows use `\arrow` / standard arrow commands | No arrowhead is supplied on the headless connectors in 138–140, 160, 162, 167, 170, 176. Scan 167 restriction stroke remains doubtful. |
| Prime, star, sharp and exclamation | `'`, `*`, `\sharp`, `!`, with their actual index/exponent position | The compact-support notation in 142 is `R^q_!f_U`; it is not silently changed to a prime or to another conventional placement. The sharp/star on 140 remains a reading alternative. |
| Authorial question mark | `?` | Distinguished from editorial `\unsure`; e.g. 133, 144. A question mark does not certify that the marked mathematics is false. |
| Underlined Pic / Prépic / Prépic-prime | `\uline{\mathrm{Pic}}`, double underlining, and literal prime where present | The prime omissions in 174(ii) and the middle paragraph of 177 are preserved. The names in 138–140 are `Pic'`, not silently renamed `Prépic'`. |
| Sheaves and higher direct images | Underlined `O`, `L`, `H^i`, with the visible subscripts | The subscript `f` in 164 and `X/S` in 173–177 are retained. A visibly doubtful terminal exponent in 164 stays `1|2`. |
| Greek ξ, η, δ and ℓ | `\xi`, `\eta`, `\delta`, `\ell` | Class and boundary formulas in 142–145 were compared; the author’s “à vérifier” remains attached to the equation on 144. |
| Bold E, Z and Tate T | `\mathbf E`, `\mathbf Z`, `\mathbf T_\ell(E)` | The bold Tate-module letter on 142 is not read as Gamma or a script T. Plain E in neighbouring text is retained where written. |
| Intermediate scheme Σ and global sections Γ | `\Sigma`, `\Gamma` | Distinguished in 138–140 and 173. The reused typed section symbol in 134 remains `I|\Gamma`, with the ink-first reading I. |
| Curve indices and graph counts | `c_0`, `c_1`, `b_1`, `d_\alpha`, `\mu_\alpha`, `\mu'_\alpha`, `\delta_\alpha`, `\nu_\alpha` | Compared through 147, 149, 151, 153, 155. In particular the unprimed μ in the first equivalence of 155 was rechecked and not changed for mathematical reasons. |
| Meromorphic-function field on reused English pages | `\unsure{\mathfrak M|\mathcal M}` | Same unresolved Gothic/script distinction in 150, 152, 156. Gothic point `\mathfrak p` and its primes are separate. |
| Stars in reused English typescript | Baseline `V*`, `K*`, `\mathfrak p*` where printed; superscript `D_h^*`, `x_k^*` where raised | Compared on 148, 150, 152, 156; not normalized to one convention. |
| Printed ideal alphabets | `\mathfrak j`, `\mathfrak a`, `\mathfrak J`; ordinary radical `\mathrm r` | Compared on 154, 159, 161. A first Roman/Gothic J on 159 is marked doubtful. |
| Hom-space script and Gothic letters | Doubtful Gothic J on 160; script `\mathcal J|\mathcal I` on 162 | Enlarged source glyphs were compared directly after the audit. J is first on 162, but the I alternative remains; no inference from the quotient construction resolves the ink. |
| Projective space / principal bundle | `P`, `\mathrm P`, `\mathbf P`, `\mathcal P` as written | The overwritten source before the last dash on 162 remains `\mathcal P|S`, rather than forcing the mathematically expected base. |
| Tilde, hat, ring | `\widetilde{…}`, `\widehat{…}`, `\mathring{…}` | Completion accents and residue-class rings on 165 were rechecked; its first E accent remains tilde/hat uncertain. Normalizations of curves and surfaces retain their tilde. |
| Affine local divisor notation | `\underline O_{(V)}`, `v_V`, `\mathfrak p` | Compared on 169–171. The word “minimaux” is preserved in 169 and on the printed sheet 161. |
| Page numbering | `\scanpage` for scan numbers; archive foliation in comments | No secure authorial sheet number was identified in these 43 images. Typed page numbers are transcribed as text, not converted to `\mspage`. |

# Doubts

Every occurrence of `\unsure` and `\illegible` in the final page fragments is indexed below, including nested occurrences and repeated readings. “TeX line” means the line in the individual `pages/MPL_57_133-179_57_scanNNN.tex` file, not a reconstructed manuscript line or the combined fragment. Confidence refers to the proposed reading, not the mathematical statement; “medium” is still a real unresolved doubt, and unreadable words, long compressed phrases, and cancellation/margin readings are conservatively classed low. The first alternative is the reader’s best ink-based reading; no alternative is silently supplied when none was read.

| File | Scan | Approximate line / place | Reading | Alternatives | Confidence |
|---|---:|---|---|---|---|
'''

ABBREVIATIONS = r'''
# Abbreviations met

These expansions are interpretive aids only. They have not been inserted into the transcription, and ambiguous abbreviations retain more than one possible expansion.

| Written form | Possible expansion / meaning |
|---|---|
| abs; abs. | absolu / absolue |
| Aff.; alg.-affine | affine; algébriquement affine / algebraic affine group |
| alg.; alg. clos | algébrique / algébriquement; algébriquement clos |
| appl | application |
| aut. | automorphisme |
| ch. | chaque / changement, according to position |
| Chap; chap | chapitre |
| codim; codim coh | codimension; codimension cohomologique |
| Coh Mac; Coh. Mac. | Cohen–Macaulay |
| coh. plat | cohomologiquement plat |
| comb. lin. | combinaison linéaire |
| cond. | condition |
| const. | constant / constante |
| cor.; Corollaire | corollaire (the full word is also written) |
| cpt; cpte; q.c.; qu. cpt; qu. cpte; q. cpte | compact / compacte; quasi-compact / quasi-compacte; exact short forms vary |
| qu. cpt (175) | quasi-compact; this compressed insertion remains uncertain |
| dém.; Dém | démonstration / démontrer |
| déf; déf.; def. | défini / définie |
| dim | dimension |
| div.; pr. | diviseur; premier |
| ds | dans |
| élts; élémᵗ | éléments; élément |
| ens; ens. | ensemble |
| Ex; ex. | exemple / exact, depending on position; shorthand on 177 remains unresolved |
| fid.; fid. plt; fid. plat; fid. plate | fidèlement; fidèlement plat / plate |
| gr. | groupe |
| hom; hom. | homomorphisme |
| homoth. | homothétie |
| hyp.; l'hyp. | hypothèse |
| i.e. | id est / c’est-à-dire |
| Imp. | implication |
| inv. | inversible |
| isom; isom. | isomorphisme |
| loc; loc. | localement / local / locale, according to position |
| loc. cit. | loco citato, in the reused English text |
| mod. | modulo |
| mono. | monomorphisme |
| N.B. | nota bene |
| nb; nbr | nombre |
| n°; N° | numéro |
| néc! | nécessairement, with the visible doubtful terminal mark on 135 |
| Nér Sév | Néron–Severi; the compressed lettering on 133 is uncertain |
| noeth | noethérien |
| O.K. | author’s acknowledgement at the end of the first proof on 170 |
| p.; pp.; Vol.; Ser.; Math. | page; pages; volume; series; mathematics, in printed bibliographical references |
| prop; prop.; Prop | proposition |
| pt; pts | point; points |
| qu. sép; qs | quasi-séparé; the abbreviated margin on 176 remains doubtful |
| réd | réduit |
| Réciproqt | réciproquement |
| resp. | respectivement; in the English letter, possibly “with respect to” |
| rés. | résulte |
| sch.; schém.; schématiq. | schéma / schématiquement, according to context |
| Sorb. chev. | unresolved abbreviated reference on 135; a Chevalley/Sorbonne reference is only a possibility |
| ss-préschéma | sous-préschéma |
| th.; Th. | théorème |
| tte | toute |
| VA; V.A. | variété abélienne |
| val. | valable / validité; low-confidence margin on 173 |

# Legibility and limitations

All 43 whole-page images and their 86 supplied halves were viewed by the root reader without OCR during the first pass; every page then received a second visual comparison. The transcription remained one sequential stream. Separate assistance was restricted to file-manifest checks, LaTeX syntax and inventory bookkeeping until the transcription was frozen.

The reused printed and English typed pages are generally much clearer than the autograph notes, although fonts, completion accents, and a few typed defects remain uncertain. The least reliable text is the compressed and repeatedly overwritten marginal writing on 158, 160, 162, 173 and 175; the cancelled algebra on 147 and 155; the opening cancelled lines on 144, 149 and 151; and the final compressed words on 179. The uncertainties in those passages are substantive limitations, not guarantees that every reading outside a doubt macro is error-free.

The drawings on 147, 153 and 155 are TikZ reconstructions of visible strokes and labels; they are not photographic facsimiles. Small variations of pen shape, colour, ink pressure and exact spacing are not encoded. Reversed text showing through paper is distinguished from recto writing; where its recto is included, that recto is transcribed separately. No missing mathematical condition or plausible correction was supplied from the later context.

The long contour around the opening ν-paragraph on 151 is a material uncertainty of page state: it has been encoded as cancellation, but an isolating contour rather than a cancellation remains possible. The page-state alternative is recorded in the doubts table as well as here. All author question marks and explicit “à vérifier” wording remain in the text; their interpretation belongs to the research notes.
'''


def alternatives(body):
    depth = 0
    for i, c in enumerate(body):
        if c == '{': depth += 1
        elif c == '}': depth -= 1
        elif c == '|' and depth == 0 and (i == 0 or body[i-1] != '\\'):
            return body[:i], body[i+1:]
    return body, '—'


def cell(text):
    return '`' + ' '.join(text.split()).replace('|', '&#124;').replace('`', '&#96;') + '`'


def main():
    rows = []
    index = []
    for page in sorted((ROOT / 'pages').glob('*.tex')):
        scan = int(re.search(r'scan(\d+)', page.name)[1])
        text = page.read_text()
        editorial = macro_spans(text, {'deleted', 'inserted', 'margin'})
        for span in macro_spans(text, {'unsure', 'illegible'}):
            contexts = [s.name for s in editorial if s.start <= span.start and s.end >= span.end]
            place = f'TeX line {span.line}' + ('; ' + ', '.join(contexts) if contexts else '')
            if span.name == 'illegible':
                reading, alt, conf = f'{span.body} unreadable word(s)', 'No reading recovered', 'low'
            else:
                reading, alt = alternatives(span.body)
                conf = 'low' if ('deleted' in contexts or 'margin' in contexts or len(reading) > 50) else 'medium'
            rows.append(f'| 57.pdf | {scan} | {place} | {cell(reading)} | {cell(alt)} | {conf} |')
            index.append({'scan':scan, 'tex_line':span.line, 'macro':span.name, 'reading':reading,
                          'alternatives':alt, 'confidence':conf, 'state':contexts})
    page = ROOT / 'pages/MPL_57_133-179_57_scan151.tex'
    lineno = next((n for n,line in enumerate(page.read_text().splitlines(),1) if '\\deleted{Soit' in line), 1)
    rows.append(f'| 57.pdf | 151 | TeX line {lineno}; opening ν-block, page state | Encoded as a deleted block | Long contour may isolate rather than cancel the block | low |')
    (ROOT/'MPL_57_133-179_doubts.md').write_text(HEADER + '\n'.join(rows) + '\n' + ABBREVIATIONS)
    (ROOT/'documentation/doubt_index.json').write_text(json.dumps(index,ensure_ascii=False,indent=2)+'\n')
    print(f'{len(index)} explicit macro occurrences plus one page-state doubt indexed')


if __name__ == '__main__':
    main()
