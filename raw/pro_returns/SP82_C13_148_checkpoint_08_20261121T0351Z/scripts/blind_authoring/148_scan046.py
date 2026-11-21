#!/usr/bin/env python3
"""Independent visual authoring for scan046; no comparison or recognition.

Only scan046's permitted source image and box inventory informed these readings.
This script writes the human-authored reading, not an automated recognition result.
"""
import csv
import io
import json
import os
from pathlib import Path
import tempfile
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/8132fe1cca43')
INPUT = ROOT / 'work/blind_inputs/148_scan046'
WORK = ROOT / 'work/SP82_C13_148'
OUT = WORK / 'second/148_scan046_second.tsv'
JOURNAL = WORK / 'second/148_scan046_blind_journal.json'

READINGS = {
    '148-046-heading_triple': r'''\uline{Objets} : Triples $\left(X,\widetilde{\Sigma},\overset{\inserted{\unsure{R|\mathring R}}}{\deleted{\unsure{S|\varnothing}}}\right)$, où
\margin{2}''',
    '148-046-top_symbols': r'''\margin{$X,\unsure{\deleted{\partial X}|\deleted{\Sigma}\inserted{\partial X}},\Sigma,S$}''',
    '148-046-surface_line': r'''$X$, surface à bord compacte orientée.''',
    '148-046-sigma_condition': r'''$\widetilde{\Sigma}$ sous-variété compacte de $X\deleted{\unsure{\setminus\partial X|\partial X}}$, $\Sigma\supset\partial X$''',
    '148-046-finite_subset': r'''$\deleted{\unsure{\partial S|S}}R\subset\Sigma\deleted{\setminus\partial X}$, partie finie''',
    '148-046-left_note': r'''\margin{$\widetilde{\Sigma}=\partial X\amalg\Sigma$
On peut considérer que
$R$ rigidifie, \unsure{mais|ainsi}
que $R$ ``découpe'' $\Sigma\ldots$}
\uline{flèches}
\deleted{\unsure{Varia|Vari}}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0) .. controls (.04,.10) and (.10,.10) .. (.13,.04);
\draw (.43,-.15) .. controls (.38,-.04) and (.42,.10) .. (.49,.12) .. controls (.58,.12) and (.57,-.03) .. (.49,-.08);
\draw (.62,-.15)--(.65,-.20);
\draw (.76,-.22).. controls (.85,-.20) and (.88,-.25)..(.94,-.28);
\end{tikzpicture}}''',
    '148-046-arrows_definition': r'''\margin{$\Sigma\ldots$}
\uline{flèches} : classes d'isotopie d'homéom. \begin{tabular}{l}conservant\\l'orientation\end{tabular}
\margin{$\Sigma$}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)--(.03,-.04);\draw (.04,0)--(.06,-.02);
\draw (1,0)--(1.02,-.06);
\draw (1.7,0)..controls (1.69,-.17) and (1.72,-.27)..(1.77,-.28)..controls (1.8,-.25) and (1.79,-.1)..(1.79,0);
\end{tikzpicture}}''',
    '148-046-components_start': r'''\deleted{Variante}\quad les composantes connexes de $\widetilde{\Sigma}\setminus\partial X\overset{\inserted{=\Sigma}}{\vphantom{X}}$ sont les
\inserted{celles de $\partial X$ sont les cercles de \unsure{raccord|raccords}.}
\uline{cercles de découpage}, les éléments de $\deleted{\unsure{S|\partial R}}\inserted{R}$ sont les
\deleted{(ou de rigidification)}
\deleted{\unsure{points|sommets}} \uline{sommets de $\overset{\inserted{\text{rigidification}}}{\deleted{\text{marquage}}}$}, \deleted{les composantes connexes}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,-.60)..controls (.02,-.47) and (-.04,-.16)..(.16,-.10)--(4.55,-.10);
\draw (.18,-.06)--(4.58,-.06)..controls (4.85,-.05) and (5.04,.15)..(5.15,.28);
\draw (5.86,.52)..controls (6.05,.51) and (6.30,.58)..(6.38,.65)--(6.36,.73);
\draw (3.05,-1.33)..controls (3.00,-.99) and (3.14,-.87)..(3.38,-.88);
\end{tikzpicture}}''',
    '148-046-circle_terms': r'''\uline{cercles de découpage}, les éléments de $\deleted{\unsure{S|\partial R}}\inserted{R}$ sont les
\deleted{(ou de rigidification)}
\deleted{\unsure{points|sommets}} \uline{sommets de $\overset{\inserted{\text{rigidification}}}{\deleted{\text{marquage}}}$}, \deleted{les composantes}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,-.55)..controls (.03,-.40) and (-.06,-.09)..(.17,0)--(4.55,0);
\draw (.17,.04)--(4.55,.04);
\draw (3.1,-1.1)..controls (3.06,-.8) and (3.18,-.64)..(3.43,-.67);
\end{tikzpicture}}''',
    '148-046-components_end': r'''\deleted{\unsure{points|sommets}} \uline{sommets de $\overset{\inserted{\text{rigidification}}}{\deleted{\text{marquage}}}$}, \deleted{les composantes connexes
de $\partial X$ sont les \uline{``trous''}.}
Les composantes connexes de
$X$ sont les $\overset{\inserted{\uline{\unsure{\text{composants}|\text{composantes}}}}}{\deleted{\text{morceaux}}}$ de l'objet envisagé.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,-.35)..controls (-.04,-.08) and (.08,.06)..(.34,.04);
\end{tikzpicture}}''',
    '148-046-variant_diagram': r'''Variante $S_*\unsure{\mathcal T|\mathcal C}D_{\mathrm{top}}^{\pm}$, où
\diagram{\begin{tikzcd}[column sep=large]
S_*\unsure{\mathcal T|\mathcal C}D_{\mathrm{top}} \arrow[r,hook,no head,line cap=round] & S_*\unsure{\mathcal T|\mathcal C}D_{\mathrm{top}}^{\pm} \arrow[r] & [\pm1]
\end{tikzcd}}''',
    '148-046-comme_tantot': r'''comme tantôt.''',
    '148-046-row1': r'''$R=\varnothing,\Sigma=\varnothing$\qquad $\unsure{\mathcal T|\mathcal C}_{\mathrm{top}}$ et $\unsure{\mathcal T|\mathcal C}_{\mathrm{top}}^{\pm}$
\deleted{$\unsure{\partial X|\partial\Sigma}=\Sigma=\varnothing$}
\margin{$+$}''',
    '148-046-row2': r'''$\Sigma=\deleted{\unsure{\partial X|\varnothing}}\partial X$\qquad $S_*\unsure{\mathcal T|\mathcal C}_{\mathrm{top}}$ et $S_*\unsure{\mathcal T|\mathcal C}_{\mathrm{top}}^{\unsure{\pm|+}}$
$R$ quelconque''',
    '148-046-teichmuller': r'''(groupoïdes de Teich-
\inserted{(\unsure{ou|en} \uline{rigidifiés})}
müller \uline{spéciaux}
(topologiques orientés)
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,.14)..controls (-.08,.08) and (-.07,-.03)..(.08,-.04)--(3.1,-.04)..controls (3.2,-.04) and (3.22,-.09)..(3.23,-.12)..controls (3.25,-.03) and (3.40,.02)..(3.37,.19);
\end{tikzpicture}}''',
    '148-046-row3': r'''$\deleted{\unsure{S|\Sigma}}\inserted{R}=\varnothing$\qquad $\unsure{\mathcal T|\mathcal C}_{\deleted{\unsure{\mathrm{top}|*}}}D_{\mathrm{top}}$ et $\unsure{\mathcal T|\mathcal C}D_{\mathrm{top}}^{\pm}$''',
    '148-046-case_comment': r'''(Cas peu intéressant je crois, sauf pour $\Sigma=\unsure{\varnothing|\deleted{\varnothing}}$ également)''',
    '148-046-md_margin': r'''\margin{MD = ``\unsure{modulaire|modulaires}'' ou
Mumford-Deligne}
\deleted{Dé}''',
    '148-046-determination': r'''\deleted{Dé} \uline{Détermination} du
\diagram{\begin{tikzcd}[column sep=large]
\pi_0\left(S_*\unsure{\mathcal T|\mathcal C}D_{\mathrm{top}}\right) \arrow[r,"\sim"] & \pi_0\left(S_*\unsure{\mathcal T|\mathcal C}D_{\mathrm{top}}^{\pm}\right)
\end{tikzcd}}.''',
    '148-046-bipondere': r'''On introduit les \uline{graphes} $\unsure{\mathrm{MD}|\deleted{\mathrm{MD}}}$ bipondérés''',
    '148-046-folio': r'''\mspage{45}''',
}

UNCERTAINTIES = {
    'heading_triple': 'Original third member is heavily cancelled; S versus empty-set-like ink. Inserted R has a closed upper bowl contiguous with its stem; a separate ring over R remains an alternative. The high 2 is retained as a separate annotation.',
    'top_symbols': 'The second item has crossing/overwriting. Favored cancelled partial-X; possible old Sigma under a replacement partial-X.',
    'sigma_condition': 'Cancelled material after X favors setminus partial-X. Final Sigma has no separate tilde; the top horizontal is treated as its own letter stroke.',
    'finite_subset': 'The black cancelled cluster before R favors partial-S or S. The cancelled material after Sigma is read as setminus partial-X.',
    'left_note': 'Margin word after rigidifie favors mais; ainsi retained as alternative. The R in the final line is retained literally. Lower/right overlaps include fleches and only the visible beginning of cancelled Variante; lower clipped contours are drawn without inventing the rest of words.',
    'components_start': 'The insertion ends raccord/raccords. The old symbol replaced by R is heavily overwritten. The cancelled word before sommets may be points or sommets. Curved insertion leaders and the two close horizontal guide strokes are retained without arrowheads.',
    'circle_terms': 'Same physically overlapping correction layers, independently read from this whole crop; cancelled introductory word and former finite-set symbol remain doubtful.',
    'components_end': 'Replacement above morceaux favors composants over composantes. The crossed sentence about trous is kept deleted, with the separate underline of trous retained.',
    'category_glyph': 'The repeated ornate category letter favors calligraphic T; calligraphic C retained as an alternative without normalizing from mathematical context.',
    'variant_diagram': 'Left shaft begins with an open C-shaped hook and has no definite head at the right endpoint. Right shaft has a clear right-facing head. The terminal label visibly has square brackets. A darkened bare endpoint is treated as retracing rather than a distinct marked vertex.',
    'row1': 'The upper final empty-set symbol is heavily retraced; the lower crossed formula favors partial-X = Sigma = empty set. A cropped plus at the lower right is separately retained.',
    'row2': 'Cancelled item between equals and partial-X is uncertain. The right superscript is clipped by the top crop boundary; plus-minus favored, plus alternative.',
    'teichmuller': 'Inserted connector favors ou over en. The inserted word is read rigidifies with acute final e (rigidifiés). Main word is speciaux (spéciaux). Parenthesis openings and the line-ending hyphen are retained rather than regularized.',
    'row3': 'R appears written over an earlier S/Sigma. Ink at the lower left of D favors cancelled old top subscript; star retained as alternative.',
    'case_comment': 'The final empty-set glyph is very black and may itself be cancelled. No replacement is supplied from mathematical expectation.',
    'md_margin': 'modulaire favored, plural modulaires alternative. Read whole crop rotated clockwise 53 degrees; the overlap of cancelled De is retained.',
    'bipondere': 'MD is heavily reworked; retention versus cancellation remains explicit. No further word is supplied after biponderes.',
    'overlap_edges': 'All fixed crops were inspected in full. Legible overlapping material is retained, with small isolated edge contours represented as strokes where feasible; no outside rectangle was consulted or inferred to complete a clipped word.',
}

def atomic_text(path: Path, data: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=path.name + '.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temp, path)
    except BaseException:
        try:
            os.unlink(temp)
        except FileNotFoundError:
            pass
        raise

def main() -> None:
    with (INPUT / 'boxes.tsv').open(encoding='utf-8', newline='') as handle:
        boxes = list(csv.DictReader(handle, delimiter='\t'))
    ids = [entry['box'] for entry in boxes]
    assert ids == list(READINGS), 'Authoring inventory must match the permitted box inventory.'
    assert len(ids) == 21 and all(READINGS[key].strip() for key in ids)
    stream = io.StringIO(newline='')
    writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    writer.writerows((key, READINGS[key]) for key in ids)
    atomic_text(OUT, stream.getvalue())
    journal = {
        'page': '148_scan046',
        'mode': 'independent blind visual reading before any comparison',
        'input_paths': [str(INPUT / 'scan.jpg'), str(INPUT / 'boxes.tsv')],
        'crop_command': 'python /workspace/scratch/8132fe1cca43/work/SP82_C13_148/scripts/blind_io.py crop 46',
        'fixed_crop_count': 21,
        'crop_calls_per_box': 1,
        'successfully_viewed_boxes': ids,
        'initial_full_view_format': 'Whole fixed-crop JPG display, made from the one saved PNG for each box.',
        'truncated_output': {
            'affected_boxes': ['148-046-row1', '148-046-row2', '148-046-teichmuller', '148-046-row3', '148-046-case_comment'],
            'counted_as_viewed': False,
            'resolution': 'All five were reopened individually in full before being counted as viewed.'
        },
        'additional_full_crop_views': [
            {'box': '148-046-left_note', 'rotation_degrees_counterclockwise': -37, 'scale': 3},
            {'box': '148-046-md_margin', 'rotation_degrees_counterclockwise': -53, 'scale': 3},
            {'box': '148-046-left_note', 'rotation_degrees_counterclockwise': -28, 'scale': 3},
            {'box': '148-046-teichmuller', 'rotation_degrees_counterclockwise': 0, 'scale': 4},
            {'box': '148-046-row1', 'rotation_degrees_counterclockwise': 0, 'scale': 3},
        ],
        'whole_crop_reinspection': ['components_start', 'circle_terms', 'components_end', 'heading_triple', 'sigma_condition', 'finite_subset', 'top_symbols', 'left_note', 'variant_diagram', 'arrows_definition', 'surface_line'],
        'subrectangles_made': False,
        'all_21_readings_complete_before_tsv_write': True,
        'no_ocr_or_text_recognition': True,
        'no_external_research': True,
        'no_tex_compilation': True,
        'no_comparison_or_other_reading_access': True,
        'printed_text_assessment': 'No foreground machine-printed wording was encountered in these 21 crops. No foreground text was excluded as show-through.',
        'residual_uncertainties': UNCERTAINTIES,
        'authoring_script': str(Path(__file__).resolve()),
        'output_path': str(OUT),
        'output_rows': len(READINGS),
        'write_method': 'UTF-8 csv.writer TSV, tempfile+fsync+os.replace atomically.',
        'written_at_utc': datetime.now(timezone.utc).isoformat(),
    }
    atomic_text(JOURNAL, json.dumps(journal, ensure_ascii=False, indent=2) + '\n')
    print(json.dumps({'written': str(OUT), 'rows': len(READINGS), 'journal': str(JOURNAL)}, ensure_ascii=False))

if __name__ == '__main__':
    main()
