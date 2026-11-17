"""Render the single reader's accumulated register; no image processing."""
from pathlib import Path
import json

root = Path(__file__).resolve().parents[1]
head = r'''# Notation table

The conventions below were developed from the scans before opening the context archive. Ambiguous occurrences remain marked locally; consistency does not authorize replacing a visible different sign.

| Handwritten sign or convention | LaTeX | Evidence / caution |
|---|---|---|
| English cover title | `Mapping cone` | 116 scan 002: no visible hyphen or circumflex. |
| Archive foliation | TeX comment | Small archive numbers are kept separate from the author's page numbers. |
| Authorial page numbers | `\mspage{n}` | 117 scans 006, 008, 010, 012, 014, 016, 018, 020, 021 carry 1–9. |
| Double quotation marks | two backticks and two apostrophes | No conversion into guillemets. |
| Curved X for a topos | `\mathcal X` | 116 scans 004–008; distinguish from plain diagram-category X. |
| Sheaf-category letter | `\mathcal F` | 116 scan 004, display (2); individual sheaves are F. |
| Homotopy-theory letter | `\mathcal H` | 117, especially scans 006–023. |
| Curved category letters | `\mathcal A`, `\mathcal U` | 117; local uncertainty recorded where a plain capital is also plausible. |
| Greek phi | `\varphi` | Gluing functor in 116; do not substitute script F. |
| Greek xi / zeta | `\xi`, `\unsure{\xi\|\zeta}` | 117 scans 022–023: long cursive lower strokes make several occurrences uncertain. |
| Opposite-category upper circle | `^{\circ}` | 117 duality and examples; a visibly written op remains `\mathrm{op}`. |
| Presheaf-category hat | `\widehat A` | 116 and 117; keep visible hats and distinguish them from cancellation. |
| Adjoint decorations | `^*`, `_*`, `_!` | The exclamation mark is not a prime. Repeated f, i, j decorations checked locally. |
| Prime | `'`, `''` | Primed objects, functors and equation numbers; not used as a substitute for !. |
| Indices 0 and 1 | `0`, `1`, or local `\unsure` | Several overwritten indices in 116 remain uncertain. |
| Terminal-category triangle | `\Delta_0` | 117 integrals/products; isolated triangular glyph in 116 scan 003 remains uncertain. |
| Category of homotopy types | `\mathrm{Hot}` | 117; retain subscript H where written. |
| Hom operator | `\operatorname{Hom}` | An underline is added only where drawn. |
| Homotopy Hom operator | `\unsure{\operatorname{Homht}\|\operatorname{Homhot}}`, `\operatorname{Homhot}` | 117 scan 002 remains ambiguous; the clearer scan 005 does not authorize harmonizing a different visible spelling. |
| Integral / product operators | `\int_A`, `\prod_A` | 117 scans 010–012 and 022; keep written order and parentheses. |
| Limit with directional lower arrow | `\underset{\leftarrow}{\lim}`, `\underset{\rightarrow}{\lim}` | Arrow direction follows the ink. |
| Loop symbol | `\Omega` | 117 scan 025; exponents retained row by row. |
| Equals-sign shorthand in prose | `$=$`, `$=^s$` | “revient au =”, “au =”, and the plural form on 117 scan 018; do not expand into “même” or “mêmes”. |
| Isomorphism / equivalence arrow | `\xrightarrow{\sim}` or labelled TikZ arrow | Tilde and arrow direction are independent observations. |
| Abbreviated universal quantifier | `tt`, `toute`, or `\forall` as written | Word, abbreviation and symbol are not interchanged. |
| Underlining | `\uline`, `\uuline` | Single and double underlines remain distinct. |
| Currency amounts on reused sheets | original decimal comma | No recalculation replaces a written total or an ambiguous digit. |

# Doubt register

This register records readings and their alternatives. Audit decisions appear in `working/audit_notes.md`; an earlier alternative retained here documents the reading history and is not a second live transcription. Confidence describes the visual reading, not the truth of the mathematics.

| File | Scan | Approximate line / position | Reading | Alternatives / reason for doubt | Confidence |
|---|---:|---|---|---|---|
'''
def cell(s):
    return str(s).replace('|', '\\|').replace('\n', ' ')
rows = [json.loads(s) for s in (root/'working/doubts.jsonl').read_text().splitlines() if s.strip()]
rows.sort(key=lambda x:(x['cote'], x['scan']))
body = ''.join('| '+ ' | '.join(cell(v) for v in [f"{r['cote']}.pdf",r['scan'],r['line'],r['reading'],r['alternatives'],r['confidence']])+' |\n' for r in rows)
tail = r'''
# Abbreviations

Expansions below are interpretive aids only; they are not inserted into the transcription.

| Written form | Probable expansion / meaning |
|---|---|
| cat., cats | catégorie, catégories |
| fonct., fonct | foncteur |
| loc., localis. | localisation, according to its occurrence |
| équiv., équiv. f., équiv. faible | équivalence, équivalence faible |
| asph. | asphérique |
| resp. | respectivement |
| cf. | confer / compare |
| NB, N.B. | nota bene |
| Re NB | return to the preceding nota bene |
| i.e. | id est |
| p.r. | par rapport |
| néc. | nécessairement |
| q.c., quelc., qq | quelconque(s), where the ending is abbreviated |
| tt, tte | tout, toute |
| gr. | groupe |
| ab., abél. | abélien / abélienne |
| add. | additif / additive |
| coh. | cohomologie / cohomologique, according to context |
| hom., h. | homomorphisme or homotopique; not always distinguishable without context |
| Id, Ident. | identité |
| Ob | objets |
| Ens | ensembles |
| Cat | catégories |
| Top | topos / associated topos in the local notation |
| Ch | complexes (the standalone crossed notation on 117 scan 003 remains uncertain) |
| Ex., ex. | exemple |
| g., dr. | gauche, droite |
| pl. fid. | pleinement fidèle |
| ssi | si et seulement si |
| th. | théorie / théorème, according to context |
| pt | point |
| comm. | commute / commutation |
| p. ex. | par exemple |
| O.K. | approval / acknowledgment, as written |
| déf., def | définition |
| lim | limite |
| M., MM., Mme | Monsieur, Messieurs, Madame (reused administrative sheets) |
| N°, n° | numéro |
| P., P.S. | pour (signature delegation), post-scriptum |
| D.E.A. | Diplôme d'études approfondies (typed circular) |
| U.E.R., U.S.T.L. | Unité d'enseignement et de recherche; Université des sciences et techniques du Languedoc |
| C.N.R.S., I.N.S.E.R.M. | Centre national de la recherche scientifique; Institut national de la santé et de la recherche médicale |

# Legibility and limitations

All whole-page images and both supplied half-images were visually inspected in the first pass, without OCR. A complete second visual reading of all 34 pages is recorded page by page in `progress.log`. This register and the recurring notation were checked before the transcription freeze and before any context contents were opened.

The continuous prose and typed reused sheets are generally more legible than the loose jottings, corrections and oblique marginal notes. The least secure regions are the cropped and overdrawn formulae of 116 scan 003; the indices and retraction formula of 116 scan 004; the loose Hom notes of 117 scans 002–003; the marginal warnings of 117 scans 010 and 014; the crowded double sheet 117 scan 021; and the pale cancelled writing on 117 scan 022. Names and a few digits on the account sheets are explicitly doubted rather than silently normalized.

The diagrams and signatures are reconstructed from visible strokes; relative geometry is approximate, and uncertain labels are marked. Unmatched punctuation and apparently surprising variance, adjunction or index choices are preserved when visible. No outside source is used to supply a missing manuscript reading.
'''
(root/'MPL_116+117_doubts.md').write_text(head+body+tail)
print(f'Rendered {len(rows)} doubt records.')
