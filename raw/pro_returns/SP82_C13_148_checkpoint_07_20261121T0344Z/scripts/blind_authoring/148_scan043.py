"""Independent blind authoring of scan043, all 21 prescribed boxes.

Only source inputs were the assigned scan043 scan.jpg and boxes.tsv.  The
fixed crops were made once using blind_io.py crop 43.  Every complete crop was
visually inspected before authoring; later displays enlarged or rotated the
entire saved crop only.  No OCR, research, first reading, witness, other page,
notes, review, comparison, adjudication, outcome, or TeX compilation was used.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json
import os
import tempfile

ROOT = Path('/workspace/scratch/8132fe1cca43')
PACKET = ROOT / 'work/blind_inputs/148_scan043'
OUT = ROOT / 'work/SP82_C13_148/second'
DISPLAY = ROOT / 'work/blind_display/148_scan043'

READINGS = {
'043.B01': r'''Les divers avatars \unsure{géométriques|algébriques} de la
Tour de Teichmüller : \deleted{système de groupoïdes}''',
'043.B02': r'''groupoïdes $\unsure{\mathrm{PTD}|\mathrm{RTD}}\ldots$ avec structures
\inserted{("les $10$ opérations")}
diverses \unsure{dans ce|dont ce} groupoïde dont le \deleted{\unsure{représentant|représentable}}\inserted{\unsure{notion|nature}}
le plus élémentaire est $\deleted{\unsure{\Pi|\Pi_{\mathrm{diff}}}}\quad\Pi_{\mathrm{top}}$''',
'043.B07': r'''\margin{à pts marqués
et dir. tangentes
\unsure{conformes|complexes} en
ceux-ci}
\diagram{\begin{tikzcd}[column sep=4.2em,row sep=1.1em]
 & \Pi_{\mathrm{dR}} \\
\Pi'_{\mathrm{diff}} \arrow[r,shift right=1.7ex,line width=.9pt]
 & \Pi_{\mathrm{diff}} \arrow[l,shift right=1.7ex,line width=.9pt] \arrow[u,line width=.7pt] \\
\phantom{\Pi} \arrow[u,line width=.6pt]
 & \Pi_{\mathrm{an}} \arrow[u,line width=.65pt] \arrow[dl,shift right=.7ex,line width=.6pt] \\
\Pi'_{\mathrm{an}} \arrow[ur,shift right=.7ex,line width=.6pt] & \\
 & \Pi_{\mathrm{hyp}} \arrow[uu,line width=.7pt] \arrow[dl,shift right=.8ex,line width=.65pt] \\
\Pi'_{\mathrm{hyp}} \arrow[uu,line width=.6pt] \arrow[ur,shift right=.8ex,line width=.6pt] & \\
 & \phantom{\Pi} \arrow[uu,line width=.7pt]
\end{tikzcd}}''',
'043.B08': r'''cas topologique (à bord \deleted{\unsure{géo|g}} torique
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round]
\draw[line width=.5pt] (618,102) -- (619,97);
\draw[line width=.5pt] (679,102) -- (679,94);
\end{tikzpicture}}''',
'043.B09': r'''\margin{chirurgie
top.}
\figure{\begin{tikzpicture}[x=.025cm,y=-.025cm,line cap=round]
\draw[line width=.5pt] (158,121) -- (158,116);
\draw[line width=.6pt] (181,121) -- (179,93);
\end{tikzpicture}}''',
'043.B10': r'''cas différentiable (à \deleted{pts marqués}\inserted{bord torique})
\deleted{(avec \unsure{feuillets|points} formels)}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round]
\draw[line width=.45pt] (168,18) .. controls (181,23) and (188,9) .. (196,0);
\draw[line width=.45pt] (248,41) .. controls (255,40) and (252,17) .. (255,0);
\end{tikzpicture}}''',
'043.B11': r'''\margin{ch. diff}''',
'043.B12': r'''cas \inserted{$\mathbb C$-}analytique (à bord $\unsure{\deleted{g}|g}$ torique)''',
'043.B13': r'''\margin{ch.
$\mathbb C$-an. $\unsure{?|y}$}''',
'043.B14': r'''cas hyperbolique (à bord géodésique)
\margin{ch. hyp.}
\figure{\begin{tikzpicture}[x=.02cm,y=-.02cm,line cap=round]
\draw[line width=.55pt] (916,28) -- (919,45) -- (930,52)
 .. controls (926,64) and (918,68) .. (912,68)
 .. controls (908,77) and (903,80) .. (896,79);
\end{tikzpicture}}''',
'043.B15': r'''$\Pi_{\mathbb C\mathrm{alg}}$''',
'043.B16': r'''cas $\mathbb C$-algébrique (courbes M.D,
munies d'une \deleted{\unsure{log-structure|structure}} de
\unsure{propriétés|proportions} de recoll. aux pts
doubles, plus p\textsuperscript{ts} marqués''',
'043.B17': r'''$\Pi_{\overline{\mathbb Q}-\mathrm{alg}}$''',
'043.B18': r'''cas $\overline{\mathbb Q}$-alg. (propriétés
de descente $\unsure{\mathbb C\mathrm{rel}/\overline{\mathbb Q}|\mathbb C\mathrm{an}/\overline{\mathbb Q}}$)
\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round]
\draw[line width=.5pt] (565,21) .. controls (570,26) and (572,10) .. (573,0);
\end{tikzpicture}}''',
'043.B19': r'''cas combinatoire, via cartes \unsure{orientées|reliées}
\uline{\unsure{sans bord|du bord}} \unsure{qlcq|épais}, avec sommets marqués''',
'043.B20': r'''$\Pi_{\mathrm{comb}}$''',
'043.B21': r'''$\Pi_{\mathrm{L\acute ego}}$''',
'043.B22': r'''cas combinatoire "Légo", avec
les $10$ pièces du jeu''',
'043.B23': r'''$\unsure{\Pi_{\mathbb P}|\Pi_P}$''',
'043.B24': r'''cas combinatoire "pantalonique",
avec une seule pièce de
\deleted{\unsure{tripode|pantalon}} triade.''',
'043.B25': r'''\margin{42}''',
}

UNCERTAINTIES = [
('043.B01', 'The long adjective after avatars favors géométriques over algébriques; its opening letters are heavily retraced. The phrase système de groupoïdes has a full horizontal cancellation.'),
('043.B02', 'The capital abbreviation favors PTD over RTD. The heavily revised second line is uncertain: dans ce / dont ce; représentant / représentable; the small inserted word favors notion over nature. The cancelled formula before Pi_top is retained as Pi with Pi_diff an alternative. The quoted insertion reads les 10 opérations.'),
('043.B07', 'Right labels are Pi_dR, Pi_diff, Pi_an and Pi_hyp; left labels are their visibly primed diff/an/hyp counterparts. Opposite arrows are independent shafts, not one double-headed arrow. The margin adjective favors conformes over complexes. The isolated upward left arrow and the lower right arrow entering from outside the crop are retained, with no invented outside label.'),
('043.B08', 'The cancelled material between bord and torique resembles géo, or a shorter g; the black overwriting prevents certainty. No closing parenthesis is visible in this fixed crop, so none is supplied.'),
('043.B09', 'Whole-crop rotation makes chirurgie / top. readable. The physical listing-paper edge hole is not manuscript ink.'),
('043.B10', 'The upper insertion is bord torique over the cancelled pts marqués. In the lower cancelled parenthesis feuillets is favored over points; the final word is read formels.'),
('043.B12', 'C- is visibly inserted above and before analytique. A small g-like sign before torique may have been cancelled; both deletion states are retained as alternatives.'),
('043.B13', 'The note is read ch. C-an. followed by a doubtful question-mark-shaped sign; y is retained as an alternative. No formula symbol is replaced by illegible.'),
('043.B14', 'The main wording is hyperbolique / bord géodésique. The short right-margin note is read ch. hyp.; its adjacent hook/brace-shaped stroke is drawn separately.'),
('043.B15', 'The complex-field C and alg are adjacent in the subscript; no unobserved hyphen is inserted.'),
('043.B16', 'The initials are preserved as M.D in their visible order. The cancelled noun favors log-structure over structure. The following word favors propriétés over proportions. No closing parenthesis is supplied because one is not visible.'),
('043.B17', 'The bar is over Q, not over the entire label; alg follows a visible dash.'),
('043.B18', 'The expression after descente is the main residual formula doubt. Its overwritten leading complex-field-like glyph is followed by small rel/an-like letters before the slash and barred Q. Full candidate readings are retained without assigning an unwitnessed subscript or filling from mathematical meaning.'),
('043.B19', 'The word after cartes favors orientées over reliées. The underlined phrase favors sans bord over du bord. The short word after it may be the abbreviation qlcq; épais is retained as an alternative. These uncertain words are not regularized to make a smoother sentence.'),
('043.B21', 'The heavily retraced subscript reads Légo, including an acute mark. The final letter approaches the right crop boundary.'),
('043.B23', 'The subscript P is outlined/doubled; blackboard-bold P is favored over plain P.'),
('043.B24', 'The deleted word favors tripode over pantalon; triade follows as visible uncancelled text.'),
]


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name+'.', suffix='.tmp', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8', newline='') as handle:
            handle.write(text)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(temporary, path)
    except BaseException:
        try:
            os.unlink(temporary)
        except FileNotFoundError:
            pass
        raise


def main():
    with (PACKET/'boxes.tsv').open(encoding='utf-8', newline='') as handle:
        ids = [row['box'] for row in csv.DictReader(handle, delimiter='\t')]
    assert len(ids) == 21 and ids == list(READINGS)
    data = io.StringIO(newline='')
    writer = csv.writer(data, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for box in ids:
        writer.writerow([box, READINGS[box]])
    target = OUT/'148_scan043_second.tsv'
    atomic_write(target, data.getvalue())
    journal = {
        'reader': 'blind_d',
        'page': '148_scan043',
        'assignment_order': 'scan043 after assignments of scans041 and042',
        'source_inputs': [str(PACKET/'scan.jpg'), str(PACKET/'boxes.tsv')],
        'crop_command': 'python /workspace/scratch/8132fe1cca43/work/SP82_C13_148/scripts/blind_io.py crop 43',
        'crop_count': 21,
        'crop_policy': 'Each prescribed rectangle cropped once; all additional views enlarge or rotate the entire saved crop only.',
        'successfully_viewed_boxes': ids,
        'whole_crop_views': [str(DISPLAY/(box+'.jpg')) for box in ids],
        'additional_successful_views': [
            str(DISPLAY/'043.B01_plain2.png'), str(DISPLAY/'043.B02_plain2.png'),
            str(DISPLAY/'043.B09_rotated.png'), str(DISPLAY/'043.B13_rotated.png'),
            str(DISPLAY/'043.B07_plain2.png'), str(DISPLAY/'043.B10_plain2.png'),
            str(DISPLAY/'043.B16_plain2.png'), str(DISPLAY/'043.B18_plain2.png'),
            str(DISPLAY/'043.B19_plain2.png'), str(DISPLAY/'043.B24_plain2.png'),
        ],
        'view_completeness': 'All 21 complete fixed crops were seen without truncation. No truncated result was counted as viewed.',
        'independence': 'No first reading, witness, other page, notes, review, comparison, adjudication or outcome was opened. No OCR, external research or TeX compilation was used.',
        'conventions': 'Deletion, insertion, margin, underline and doubtful-reading states are explicit. Formula doubts retain candidate symbols. The diagram is tikz-cd and graphical fragments are TikZ.',
        'paper_artifacts': 'Incidental printed ruling/hatching, physical tractor-paper holes at the right edge, and scan/background border strips are not treated as handwritten words or diagram points.',
        'diagram_arrow_inventory': [
            'Right chain: Pi_diff -> Pi_dR; Pi_an -> Pi_diff; Pi_hyp -> Pi_an.',
            'Horizontal pair: Pi_diff -> Pi_prime_diff above; Pi_prime_diff -> Pi_diff below.',
            'First slanted pair: Pi_an -> Pi_prime_an; Pi_prime_an -> Pi_an on separate shafts.',
            'Second slanted pair: Pi_hyp -> Pi_prime_hyp; Pi_prime_hyp -> Pi_hyp on separate shafts.',
            'Left vertical: Pi_prime_hyp -> Pi_prime_an.',
            'Short upward arrow below Pi_prime_diff beside the margin note.',
            'Upward arrow from below the crop into Pi_hyp, with its external source left unlabeled.',
        ],
        'residual_uncertainties': [{'box': box, 'detail': detail} for box,detail in UNCERTAINTIES],
        'confident_items': ['043.B22: les 10 pièces du jeu', '043.B25: 42'],
        'reading_path': str(target),
        'authoring_script': str(Path(__file__).resolve()),
        'reading_written_utc': datetime.now(timezone.utc).isoformat(),
    }
    atomic_write(OUT/'148_scan043_blind_journal.json', json.dumps(journal, ensure_ascii=False, indent=2)+'\n')
    print(f'Wrote complete independent TSV: {target}; {len(ids)} rows. Journal saved.')


if __name__ == '__main__':
    main()
