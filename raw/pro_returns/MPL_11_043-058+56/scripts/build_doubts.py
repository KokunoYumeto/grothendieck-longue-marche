"""Build the final uncertainty concordance from the diplomatic page files.

This reads the saved LaTeX only. It does not recognize or inspect image text.
The first/alternative readings remain exactly those entered by the human-viewing
transcription stream. Repeated occurrences are grouped within a single page.
"""
from pathlib import Path
from collections import OrderedDict
import re

ROOT = Path(__file__).resolve().parents[1]
NAME = "MPL_11_043-058+56"

INTRO = r"""# Notation table and doubts

## Recurring notation: ink-to-LaTeX table

This table was completed before the context archive was opened. The second reading covered all 50 whole-page images and all 100 supplied halves. The final comparison retained differences supported by the ink and retained doubt where the glyph remained unresolved; mathematical expectations were not used to choose a spelling, index, arrowhead, or alphabet.

| Recurring written form | LaTeX used | Locations and visual comparison |
|---|---|---|
| Double-outline affine and projective letters in the typescript | `\mathbb{A}`, `\mathbb{P}` | 11/043,045,047,049 and the later reused typescript; the uncertain first P on 56/024 remains marked. |
| Underlined lower-case structure-sheaf letter | `\underline{o}` | 11/045; the small written lower-case form is retained. |
| Typed small phi and a possible psi | `\phi`; `\unsure{\psi\|\phi}` | 11/043,045: the doubtful fraction on 045 keeps psi first. |
| Capital quotient-map Phi and its bar | `\Phi`, `\bar\Phi`, or `\unsure{\Phi\|\bar\Phi}` | 11/052,054; the faint bar/serif on 054 remains unresolved. |
| The small loop-and-stem phi in quadric calculations and the printed Delzant note | `\varphi` | 56/020,024,026,030,032,036,037; cancelled and overwritten occurrences have their own doubt marks. |
| The recurring handwritten generator resembling y / eta | `\unsure{y\|\eta}` | 11/051,053,055,057; the same unresolved pair is used across these sheets. |
| The degree letter resembling n / m | `\unsure{n\|m}` | 11/051,053; the clearer n on 057 is retained there. |
| Delta and the diagonal notation | `\delta`, `\Delta`, `\widetilde\delta`, `\bar\delta` | 11/048,051,053,055,057; uncertain lower-/upper-case occurrences on 048 remain explicit. |
| Pullback / pushforward stars | `^*`, `_*` | 11/044,046,048 and 56/011; the cancelled upper star above the live lower star on 11/048 is also recorded. |
| Prime strokes | `'`, `''` | I', I'', the projection labels on 11/046, G', Z', T' in cote 56, and lambda-prime on 56/005 were reread as individual strokes. No prime was silently changed to an exclamation-mark exponent. |
| Exclamation marks and question marks | `!`, `?`, with `\unsure{!\|?}` at the crowded occurrence | The author's verification marks on 11/046,057 and 56/014,017,020 are retained as written; they are separate from the transcriber's doubt macros. |
| Disjoint union and external product | `\amalg`, `\boxtimes` | 11/044,046,048,055,057; the occurrence-specific product signs are retained. |
| Epsilon indexing partition classes | `\varepsilon` | 11/055,057; overwritten superscripts/subscripts remain marked. |
| Cohomology generator xi, lambda, and ell | `\xi`, `\lambda`, `\ell` | 56/003,005,011,013,015,020,024,026,028,030,032; subscript and superscript placements were compared across the quadric tables. |
| The coefficient glyph resembling mu / M | `\unsure{\mu\|M}`, or `\unsure{\mu}` where only one candidate is entered | 56/003,005,015; this is unresolved handwriting, not a proposed coefficient convention. |
| Degree n and the parity parameter nu | `n`, `\nu` | Quadric sheets in cote 56; crowded exponents retain local doubt marks. |
| Primitive-cohomology letter resembling R / P | `\unsure{R\|P}` | 56/013, upper box; R is the first reading after the second visual audit. |
| Support subscript resembling x / a | `\unsure{x\|a}` | 56/013; compared with the vertex a on 56/011 and the a-like subscripts on 56/017. The written differences remain visible. |
| Rho rank indices | `\rho_r`, `\rho_n`, `\rho_u`, with `\rho_{\unsure{m\|n}}` | 56/004,014,018,033; the two-humped typed subscript in 56/014 is kept as m first. |
| Curled torus-functor letter | `\unsure{\mathcal T\|\tau}` | 56/012,014,033; all repeated occurrences on those pages carry the unresolved reading. |
| Fraktur / script partition letter | `\unsure{\mathfrak P\|\mathcal P}` | 11/055; the overwritten letter does not securely decide the alphabet. |
| Hats and tildes | `\hat{}`, `\widehat{}`, `\widetilde{}` | Cone diagrams on 56/011,017 and the printed filtered target on 56/037; the untilded H in the final prose and on 038 is retained. |
| Printed Roman mathematical capitals and bold coefficient letters | `\mathrm A`, `\mathrm Q`, `\mathrm H`, `\mathbf Z`, `\mathbf R` | 56/036–038; their printed forms were followed, including the additive notation for A-star. |
| Plain, hooked, straight, and wavy connecting strokes | `-`, `\mathbin{-}`, `\text{---}`, `\hookrightarrow`, `\rightsquigarrow`, or `tikz-cd` arrows with `no head` | Each occurrence was read separately. The doubtful blunt stroke on 56/024 and map strokes on 11/044 retain alternatives. |
| Vertical isomorphism signs | rotated `\simeq` | 56/011,017; these are reproduced at the written orientation. |
| Roman reference numerals with upper and lower rules | `\overline{\underline{\mathrm{XI}}}` and the corresponding numeral | Rechecked on 56/008,012,014,016,018,021,025,027,029,033; typed unruled numerals remain unruled. |
| Matrix punctuation | commas remain in the matrix cells | 56/024,028: the displayed two-by-two matrices retain their visible commas. |
| Double quotation marks | two backticks and two apostrophes | The handwritten and typed quoted words throughout the packet were compared; quotation marks were not changed to guillemets. |
| Underlining and double underlining | `\uline{}`, `\uuline{}` | Word-level extent follows the image. The attachment line below the insertion on 56/035 is not encoded as underlining. |

## Final table of uncertain readings

The table below is generated from **every** `\unsure` and `\illegible` in the final page files. Repetitions of the same reading on one page are grouped. “Top / middle / lower” describes approximate order within the transcription, and `.tex L` gives a precise way to locate the occurrence in its page file; paragraph wrapping need not match the photograph. The first reading and each alternative are copied from the final macros, including incomplete expressions. “Tentative reading only” means that the macro gives no second candidate. Confidence concerns the reading of the ink, not the truth of a mathematical statement.

| File (cote) | Scan | Approximate position / page-file locator | Reading | Alternatives | Confidence |
|---|---:|---|---|---|---|
"""

END = r"""
## Abbreviations encountered

The proposed expansions below are explanatory only and are not inserted into the transcription. Some occurrences lack a final point on the page; that punctuation remains as written in the LaTeX.

| Written abbreviation | Proposed expansion / use | Representative location |
|---|---|---|
| `Alg`, `corr.` | algèbre; correspondances | 11/046 margin |
| `coh.`, `coh. alg.` | cohomologie; cohomologie algébrique | 11/044; 56/017 |
| `équiv.` | équivalence | 11/044 |
| `max` | maximal / maximum, according to the phrase | 11/044 |
| `mod` | modulo | 11/044,046; 56/013 |
| `déf` | définition | 11/046 proof annotations |
| `form. de proj` | formule de projection | 11/046 |
| `transit` | transitivité | 11/046 |
| `pr.` | probably projection; the letters are doubtful | 11/048 |
| `deg`, `deg.`, `dim` | degré; dimension | 11/051,053,057; 56/035 |
| `ens.` | ensemble | 11/055 |
| `card` | cardinal | 11/057; 56/016,021 |
| `comp` | composition | 11/057 |
| `i.e.`, `i.e` | id est | both handwritten and typed passages |
| `cf.`, `cf` | confer / compare | 11/043,047,052,054; 56/006,008 |
| `resp.` | respectivement | 56/004,018,022,037 |
| `N°`, `N°s`, `Nos` | numéro; numéros | 56/006,008,012 |
| `Exp`, `Exp.` | exposé | group-scheme typescript and additions in cote 56 |
| `th.` | théorème | 56/006,013,029 |
| `Cor.` | corollary | 11/052 |
| `hom.` | homomorphisme | 56/003 |
| `isom.` | isomorphisme | 56/005 |
| `car. d'EP` | caractéristique d'Euler–Poincaré | 11/051 |
| `corresp.` | correspondent, offered only as a reading alternative | 56/030 |
| `cqfd` | ce qu'il fallait démontrer | 56/025,033 |
| `NB`, `N.B.` | nota bene | 56/016,030 |
| `imp.` | impair | 56/020 parity table |
| `gén.` | générateur | 56/020 |
| `exc.` | excepté | 56/020,030 |
| `mbs` | membres, tentative reading and expansion | 56/020 margin |
| `inj`, `surj`, `bij` | injectif, surjectif, bijectif | quadric diagrams and cancelled annotations |
| `loc.constant`, `alg. clos` | localement constant; algébriquement clos | 56/025; 56/020 |
| `val` | valuation | 56/003 |
| `p` | pages, in pencil counts | 56/002,009 |
| `fpqc` | fidèlement plate quasi-compacte | 56/025,027 |
| `réd` | réduit / réductif, according to the written expression | 56/006 |
| `int` | automorphisme intérieur | 56/014 |
| `Centr`, `Norm` | centralisateur; normalisateur | 56/014,029 |
| `Sch`, `Ens` | schémas; ensembles | 56/014 |
| `rg` | rang | 56/036,037 |
| `grad` | gradué associé | 56/038 |
| `chap.` | chapitre | 56/038 references |
| `Bull. Soc. math. Fr.` | Bulletin de la Société mathématique de France | 56/038 reference 2 |
| `Akad. Amst. Proc.` | abbreviated Amsterdam academy proceedings title | 56/038 reference 3; expansion not supplied in the transcription |
| `t.`, `p.` | tome; page(s) | 56/039 |
| `Cie` | Compagnie | 56/039 |
| `M.` | Monsieur | 56/036 attribution |
| `QED` | quod erat demonstrandum | reused English typescript |
| `SGA`, `EGA` | Séminaire de géométrie algébrique; Éléments de géométrie algébrique | cited references throughout the reused and group-scheme typescripts |
| `BIBLE` | the author's named reference for the Borel seminar text described on 56/008 | 56/006,008,029 |

## Legibility and limits

The printed Delzant note and most of the reused English typescript are comparatively clear. The difficult areas are the small handwritten corrections over type, heavily crossed-out passages, and crowded quadric diagrams. The least secure individual sheets are 11/044,046,051,055,057 and 56/005,011,013,017,020,022,024,030,032,035. Thin pencil numerals and the upside-down pencil diagram on 56/022 also deserve caution.

The uncertainty macros remain part of the diplomatic text; the second reading did not turn them into confident mathematical reconstructions. A small number of obliterated words are marked `\illegible{n}` after enlarged visual attempts. Mathematical symbols instead retain a candidate in `\unsure`. Incomplete formulas, unclosed written parentheses, stray indices, literal typing errors, blanks in references, and apparent degree or target inconsistencies have been kept. The TikZ drawings reproduce outlines, rules, callouts, and marginal strokes schematically; they do not claim facsimile geometry.

All readings were made by the same transcription stream, without OCR. The context archive was kept unopened through the second audit, notation comparison, compilation checks, and hash freeze. A filename/size listing of that archive was inadvertently produced before the first pass; no member content was read then, as recorded in `progress.log`. `records/doubts_rows.md` preserves chronological working entries, including superseded candidates; the table above records the final candidates. Later context-based questions appear only in the research notes.
"""


def balanced(s, pos):
    depth = 1
    end = pos
    while depth:
        ch = s[end]
        if ch == "{" and (end == 0 or s[end-1] != "\\"):
            depth += 1
        elif ch == "}" and (end == 0 or s[end-1] != "\\"):
            depth -= 1
        end += 1
    return s[pos:end-1], end


def split_alternative(s):
    depth = 0
    for i, ch in enumerate(s):
        if ch == "{": depth += 1
        elif ch == "}": depth -= 1
        elif ch == "|" and depth == 0:
            return s[:i], s[i+1:]
    return s, "Tentative reading only"


def cell(s):
    return s.replace("\n", " ").replace("|", "&#124;")


rows = []
counts = {"unsure_occurrences": 0, "illegible_occurrences": 0}
for f in sorted((ROOT / "pages").glob("*.tex")):
    cote, scan = re.search(r"_(11|56)_scan(\d+)\.tex$", f.name).groups()
    s = f.read_text()
    deleted_ranges = []
    for m in re.finditer(r"\\deleted\{", s):
        _, end = balanced(s, m.end())
        deleted_ranges.append((m.start(), end))
    grouped = OrderedDict()
    for m in re.finditer(r"\\(unsure|illegible)\{", s):
        arg, _ = balanced(s, m.end())
        kind = m.group(1)
        counts[kind + "_occurrences"] += 1
        key = (kind, arg)
        if key not in grouped: grouped[key] = []
        grouped[key].append((s.count("\n", 0, m.start()) + 1,
                             m.start() / len(s),
                             any(a <= m.start() < b for a, b in deleted_ranges)))
    for (kind, arg), locations in grouped.items():
        lines = ",".join(str(x) for x in sorted(set(x[0] for x in locations)))
        regions = []
        for _, fraction, _ in locations:
            region = "top" if fraction < .33 else "middle" if fraction < .67 else "lower"
            if region not in regions: regions.append(region)
        place = "/".join(regions) + "; .tex L" + lines
        if kind == "illegible":
            reading, alt, confidence = f"\\illegible{{{arg}}}", f"Estimated {arg} obliterated word(s)", "low"
        else:
            reading, alt = split_alternative(arg)
            confidence = "medium"
            if any(x[2] for x in locations): confidence = "low"
            if arg in [r"y|\eta", r"\mu|M", r"\mu", r"\varphi_\nu|\alpha_\nu", r"R|P", r"\chi", r"\cdot|0", r"\text{---}|\longrightarrow"]:
                confidence = "low"
            if (cote, int(scan)) in [("11",46),("11",55),("11",57),("56",17),("56",20),("56",22),("56",24),("56",32)]:
                confidence = "low"
        rows.append(f"| {cote} | {int(scan):03} | {place} | `{cell(reading)}` | {cell(alt) if kind == 'illegible' or alt == 'Tentative reading only' else '`'+cell(alt)+'`'} | {confidence} |")

(ROOT / f"{NAME}_doubts.md").write_text(INTRO + "\n".join(rows) + "\n" + END)
print({**counts, "grouped_rows": len(rows)})
