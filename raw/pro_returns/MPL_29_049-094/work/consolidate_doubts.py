#!/usr/bin/env python3
"""Index the root reader's explicit doubts; this performs no image reading or OCR."""
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
PREFIX = 'MPL_29_049-094'

def esc(s):
    return s.replace('|', '&#124;').replace('\n', ' ').replace('`', '&#96;')

def arg_at(s, start):
    depth, i = 1, start
    while i < len(s) and depth:
        if s[i] == '{' and (i == 0 or s[i-1] != '\\'):
            depth += 1
        elif s[i] == '}' and (i == 0 or s[i-1] != '\\'):
            depth -= 1
        i += 1
    assert depth == 0
    return s[start:i-1]

def alternatives(s):
    depth = 0
    for i,c in enumerate(s):
        if c == '{': depth += 1
        elif c == '}': depth -= 1
        elif c == '|' and depth == 0: return s[:i],s[i+1:]
    return s, 'No secure alternative; the first reading remains doubtful.'

header = r'''# Notation table and transcription doubts

## Package notation table

This table records the final, pre-context comparison of recurring signs across the package. It is a transcription convention, not an identification of the mathematics with a modern theory. Different visible forms are retained; uncertainties are also marked at their occurrences in the transcription.

| Visible sign or usage | LaTeX transcription | Locations and decision |
|---|---|---|
| Typed inclusion-map glyph | `\iota`, `\iota_a` | 049, 051; short curved iota, distinguished from v and primes. |
| Distribution bases | `\Delta`, `\Lambda` | 049, 051, 053, 055, 057, 059; preserve the two distinct capitals and all multiindices. |
| Typed multiindex N with heavy upright strokes | `\unsure{\mathbf{N}\|\mathbb{N}}` | 049, 053; bold Roman is first reading; a doubled-stroke typeface remains possible. |
| Rounded distribution-order symbol | `\unsure{\nu}` | 051, 053; same glyph read consistently; its nonstandard printed shape remains doubtful. |
| Looped differentiability-class symbol | `\unsure{\omega\|0}` | 055, 057, 059; do not replace it by a class inferred from the argument. |
| Ordinary, prime, and tame fundamental groups | `\pi_1`, `\pi'_1`, `\pi_1^t` | 050–077, 082–094; the prime stroke and the raised t have been compared. No exclamation exponent is confidently present in this package. |
| Raised abbreviation after top | `top$ {}^t$` | 070; raised t, not a prime or an exclamation mark. |
| Picard exponent | `\operatorname{Pic}^\tau`, `\underline{\mathrm{Pic}}^\tau` | 060, 071–077; tau distinguished from tame t, and underlined Pic from plain Pic. |
| Structure-sheaf O with separate lower stroke | `\underline O` | 064, 071–075, 084, 088; the underline is explicit, not silently changed to a script alphabet. |
| Looped script O and F in stratification draft | `\mathcal O`, `\mathcal F` | 087; forms differ from the separately underlined O above. |
| Script module E | `\mathcal E`, `\mathcal E_1`, `\mathcal E_2` | 086; looped module letter retained. |
| Formal-scheme X | `\mathfrak X` | 088, 090, 092, 094; distinguished from ordinary `X` and `X_0`. The overwritten base letters in cohomology are separately doubtful. |
| Plain T versus finite-group Gamma | `T`, `\Gamma` | T in 073 and the normal-bundle notation in 090; Gamma in 063. No confidently identified script T has been converted to Gamma. |
| Projective-space P, retraced/doubled stem | `\unsure{\mathbf P\|P}` | 061, 062, 067; font remains uncertain. Plain, single-stem P is retained in 065, 068. |
| Typed integers with separate underline | `\underline Z` | 093; no blackboard-bold replacement. |
| Heavy handwritten integer symbol | `\mathbf Z`, `\mathbf Z_\ell` | 072, 074, 076, 082, 088; handwritten form distinct from the typed underlined Z. |
| Underlined group/sheaf names | `\underline G`, `\underline{\operatorname{Hom}}`, `\underline{\mathrm{Pic}}` | Retained where visible; ordinary Hom or Pic elsewhere is not underlined by analogy. |
| Frobenius | `F`, `{}_{F^{\unsure{\nu\|1}}}H^1` | 072; left subscript placement retained. |
| Repeated p exponents | `p^{\unsure{\nu\|1}}`, `p^{-\unsure{\nu\|1}}` | 073; every small exponent retains the same nu/one uncertainty. |
| Bars, hats and tildes | `\bar{}`, `\overline{}`, `\widehat{}`, `\widetilde{}` | 065 upper X-prime has a hat/bar alternative; lower X has a bar. Universal-cover tildes and geometric-point bars remain distinct. |
| Inertia letter I, including possible upper stroke | `I_0`, `\overline I_0`, `\overline I'_0` | 088, 092; the extra upper stroke is retained in the displayed occurrences; it may be a pronounced serif, so no uniform algebraic meaning is asserted. |
| A superscript on the Raynaud sheet | `A^{\unsure{\natural\|\sharp}}` | 085; zigzag/accidental-like sign remains uncertain. |
| Headless connectors | `\mathbin{-}` or `\arrow[...,no head]` | Wherever only a shaft is visible; possible arrows receive an in-place alternative, not a silently added head. |
| Empty typed connectors and operators | spacing with no invented sign | 089, 091, 093; absent equals, membership, roots-of-unity, product and arrow glyphs remain absent. |
| Double quotation marks | two backticks and two apostrophes | All ordinary double quotation marks; no replacement by guillemets. Ditto strokes are transcribed separately. |
| Deleted and inserted text | `\deleted{...}`, `\inserted{...}` | Word and symbol identity retained; cancellation does not imply that the mathematical statement has been refuted. |
| Underlining and double underlining | `\uline{...}`, `\uuline{...}` | Visible text emphasis; separate marginal emphasis strokes reproduced in TikZ. |
| Page numbering | `\mspage{...}` only for confidently authorial numbering | Printed typescript numbering is ordinary text. Archive foliation is a comment. Scan 085's handwritten 69 has uncertain attribution and is only a comment. |

## Final in-place doubt register

The following table is generated from the final page files, including doubts inside deletions and diagrams. “Line” is the physical line of the named LaTeX page file, a precise locator rather than a claim about manuscript line numbering; the nearby fragment helps locate it on the scan. Every listed first reading follows the ink, including spellings and headless connectors. “Low” is conservative: it means the word or symbol should be checked against the scan before quotation as secure text, not that the entire surrounding sentence is doubtful. The raw first-pass and audit records in `work/doubts_records.jsonl` are historical working records and may contain readings superseded by this final register.

| File/cote | Scan | Approximate location | First reading | Alternative(s) | Confidence |
|---|---:|---|---|---|---|
'''

rows = []
for p in sorted((ROOT/'pages').glob('*.tex')):
    scan = int(re.search(r'scan(\d+)', p.name).group(1))
    s = p.read_text()
    for match in re.finditer(r'\\(unsure|illegible)\{',s):
        arg = arg_at(s,match.end())
        line = s.count('\n',0,match.start())+1
        nearby = s[max(s.rfind('\n',0,match.start())+1,match.start()-45):min(s.find('\n',match.end()) if s.find('\n',match.end()) >= 0 else len(s),match.end()+len(arg)+45)]
        if match.group(1) == 'illegible':
            first, alt = f'Physically unreadable: estimated {arg} word(s)', 'No defensible word reading at available image resolution.'
            conf = 'low'
        else:
            first, alt = alternatives(arg)
            conf = 'medium' if first in (r'\nu',r'\mathbf{N}',r'\mathbf P',r'\natural') else 'low'
        rows.append(f'| 29; {p.name} | {scan:03} | TeX line {line}: `{esc(nearby)}` | `{esc(first)}` | {esc(alt)} | {conf} |')

footer = r'''

## Doubts about placement, page state, and graphical form

| File/cote | Scan | Approximate location | First reading/state | Alternative or limitation | Confidence |
|---|---:|---|---|---|---|
| 29 | 050 | Opening seven lines | Rewritten localization paragraph with interlinear additions | Some attachment points and cancellation boundaries remain uncertain even where a tentative word is supplied. | low |
| 29 | 052 | Lemme 3 revision | Stronger finite-fibre statement replaces a finiteness hypothesis | The deletion crosses the inserted word; the exact order of pen actions is not recoverable. | medium |
| 29 | 054 | Condition (ii) | intègre affine and affine inserted at their written anchors | Crowded interlinear text permits a different attachment; the mathematical hypothesis has not been reconstructed. | low |
| 29 | 061–062 | Generic-curve passages | Rewritten section and neighbourhood qualifiers | Some overlapping insertions have no decisive caret; final wording is not a critical reconstruction. | low |
| 29 | 065 | Central completion diagram | Upper hat/bar X-prime, lower barred X | The shapes differ; no identification of the two operations is imposed. | medium |
| 29 | 066 | Corollary and final paragraph | fermé before de codim; Y-prime of codimension at least 2 | The latter clause is transcribed as written; whether it is an extra hypothesis is a research question. | medium |
| 29 | 068–069 | Cancelled model discussion | Entire crossed passages retained | Multiple cancellation layers cannot always be put in a certain chronological order. | low |
| 29 | 071 | Restriction display | Pic(X) to Pic(U) | X is the visible letter; the surrounding Y does not authorize substitution. | high |
| 29 | 071 | Narrow left and lower margins | Questions about normality, projectivity and cycles | Several words remain only tentative; no argument should depend on those readings alone. | low |
| 29 | 073 | Last quotient denominator | Small raised tau-like mark | It may be a correction stroke, not an exponent. | low |
| 29 | 078 | Cancelled earlier cover title | Pi-one / étale-sheaf abbreviation | Crossed letters are only partly separable; no completion from the live title is made. | low |
| 29 | 082 | Top centre and outlined notation | Individually doubtful English words; script S minus Supp D | Spec D is possible; the extra English phrase is particularly unreliable. | low |
| 29 | 085 | Top centre number 69 | Clear numeral, uncertain writer | Not assigned to authorial pagination; the whole-page diagonal may mark reuse rather than substantive retraction. | medium |
| 29 | 086 | Faint d and plus S-three above item 12 | Tentative marks retained | Could be show-through from the other side rather than recto additions. | low |
| 29 | 087 | Whole cancelled draft and ten-object diagram | All visible objects, connectors and overwritten text retained | Cancellation overlaps several labels; m.u. and the category abbreviation remain unresolved. | low |
| 29 | 088 | Inertia sequences | Upper stroke over first I-zero retained | Serif versus separate bar is not completely decidable. | medium |
| 29 | 089, 091, 093 | Typed displays | Visibly empty positions retained as spacing | Expected operators are not supplied, even where the mathematics makes them predictable. | high |
| 29 | 092 | Bottom-left marginal fragment | Tentative “ce qui du / pro. dans / est faux” | Extremely uncertain and without a secure referent; it is not evidence of a retraction. | low |
| 29 | 093 | First line | Inserted n before égal | No clear caret determines whether it belongs before égal or near ordre. | low |
| 29 | 093 | Second sequence below u-prime | A tentatively cancelled a | Could be n; even the cancellation is uncertain. | low |
| 29 | 094 | Central overwriting and final quotient | Tentative live/deleted layers and script R-zero denominator | The denominator is not identified from the desired proof; the last line is partly at the scan edge. | low |
| 29 | all drawings | TikZ reconstructions | Relative geometry, strokes, labels and emphases approximated | TikZ captures the visible structure, not pen texture or exact pixel geometry; uncertainty in a label is marked in place. | medium |

## Abbreviations encountered

Expansions below are interpretive aids only. They have not been inserted into the transcription. A slash separates plausible expansions when the abbreviated form is not decisive.

| Written form or family | Tentative expansion or explanation |
|---|---|
| alg., algéb. | algébrique / algébriquement |
| birat., birat.elle | birationnel / birationnelle; the second written form is itself doubtful |
| can. | canonique / canoniquement |
| car. | caractéristique, or car where it is an ordinary word; determined locally |
| cat. | catégorie |
| cf. | confer, compare |
| C.Q.F.D., cqfd. | ce qu'il fallait démontrer |
| codim | codimension |
| coh., qu.coh. | cohérent; quasi-cohérent |
| comp., compl. | complet / complément, according to the phrase |
| conn. | connexe |
| constr. | constructible |
| Cor., cor. | corollaire |
| Dém. | démonstration |
| dim | dimension |
| ens. | ensemble |
| équiv. | équivalent / équivalence |
| ét. | étale |
| ext. | extension |
| faisc. | faisceau |
| fnt (doubtful) | finite / finite-type shorthand; unresolved in scan 086 |
| fund. | fundamental / fondamental |
| gal. | galoisien |
| gén. | générique / général |
| géo., géom., géométr. | géométrique / géométriquement |
| gr., grps | groupe, groupes |
| hom. | homomorphisme / homotopie, according to context |
| hyp. | hypothèse |
| i.e. | id est, that is |
| iff | if and only if |
| int. | intègre / intégral; an overwritten occurrence is unresolved |
| irrédu. | irréductible |
| isom. | isomorphisme |
| loc., loc. cit. | localement / local; loco citato |
| m.u. | unresolved abbreviation in the cancelled stratification draft, scan 087 |
| nb. | nombre |
| N.B., NB | nota bene |
| néc. | nécessaire / nécessairement |
| noeth. | noethérien |
| N° / n° | numéro |
| n.r. | non ramifié |
| Pb | problème |
| p.ex. | par exemple |
| préschém. | préschéma |
| proj. | projectif / projective |
| prop., Prop. | propre or proposition, depending on position |
| pts | points |
| quelc. | quelconque |
| r. to | with respect to |
| rat/k | rationnel sur k |
| Réf, réf. | référence |
| resp. | respectivement |
| rev., revêt., revêtts | revêtement(s) |
| SGA | Séminaire de géométrie algébrique; the manuscript's abbreviated reference is retained |
| sss | si et seulement si |
| surj. | surjectif / surjective |
| t.f. | type fini |
| th., thme, Thm | théorème |
| tjrs | toujours |
| top., top with raised t | topologique / topologiquement |
| tt, tte, tts | tout, toute, tous |
| univ. | universel / universellement |

## Legibility and limits

The reused typescripts are mostly substantially clearer than the handwriting, but their overtyped deletions and visibly unprinted mathematical operators require care. The handwritten pages alternate between readable prose and extremely compressed strokes; scans 050 and 062, the margins of 071, the cancelled stratification draft 087, the lower margin of 092, and the overwritten formulas at the foot of 094 are the least secure areas. The Greek/order glyph in the distribution typescript and several font distinctions remain unresolved despite comparison across their occurrences.

The root reader inspected every supplied whole page followed by both halves during the first reading, then performed a second image audit of all 42 retained scans; extra rotations and enlargements were used for difficult areas. No OCR was used, and no second agent transcribed or audited images. The mechanical validation only checks packaging and LaTeX syntax and cannot certify the readings. Doubt marks are part of the deliverable, not a claim that all other ink is infallibly read; badly overwritten text, insertion attachment and cancellation extent merit further expert comparison with the scans.
'''

(ROOT/f'{PREFIX}_doubts.md').write_text(header+'\n'.join(rows)+footer)
print(f'Indexed {len(rows)} explicit final doubt occurrences.')
