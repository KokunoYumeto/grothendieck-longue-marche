"""Independent blind authoring for scan039, all eight prescribed boxes.

Only input sources: the assigned copied scan.jpg and boxes.tsv.  Cropping was
performed once per fixed rectangle by blind_io.py crop 39.  All eight complete
saved crops were viewed before writing.  Additional views magnified or rotated
the entire saved crop only; no new subrectangles were made.  No other page,
witness, first reading, notes, review, comparison, OCR, research, or TeX run.
"""
from pathlib import Path
from datetime import datetime, timezone
import csv
import io
import json
import os
import tempfile

ROOT = Path('/workspace/scratch/8132fe1cca43')
PACKET = ROOT / 'work/blind_inputs/148_scan039'
OUT = ROOT / 'work/SP82_C13_148/second'
DISPLAY = ROOT / 'work/blind_display/148_scan039'

READINGS = {
'S39-01': r'''\unsure{Changer|Change} la base \deleted{\unsure{en|de}} $e_1$ en $\xi e_1$ (où $\xi^4=1$)
\figure{\begin{tikzpicture}[x=.007cm,y=-.007cm,line cap=round]
\draw[line width=.5pt] (711,132) .. controls (712,122) and (716,123) .. (719,120);
\draw[line width=.5pt] (723,132) -- (728,120);
\draw[line width=.45pt] (791,132) -- (792,127);
\draw[line width=.45pt] (982,132) .. controls (980,126) and (985,125) .. (989,132);
\end{tikzpicture}}''',
'S39-02': r'''\deleted{\unsure{aussi|ainsi}} change \deleted{par} $\{\unsure{x|f},\unsure{y|g}\}$ en $\{\xi^2\unsure{x|f},\xi^{\unsure{3|2}}\unsure{y|g}\}$,
\figure{\begin{tikzpicture}[x=.007cm,y=-.007cm,line cap=round]
\draw[line width=.5pt] (126,0) -- (145,0);
\draw[line width=.5pt] (1123,1) .. controls (1128,5) and (1136,2) .. (1141,0);
\draw[line width=.45pt] (1234,12) .. controls (1242,10) and (1246,6) .. (1250,4);
\end{tikzpicture}}''',
'S39-03': r'''donc $\mu$ en $\xi^2\mu$, qui est donc
égal à $\mu$ si $\xi\in\{\pm1\}$, égal à $-\mu$ si
$\xi\in\{\pm i\}$.
\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round]
\draw[line width=.45pt] (1202,0) .. controls (1208,3) and (1212,2) .. (1217,0);
\end{tikzpicture}}''',
'S39-04': r'''La multiplicité modulaire pour les
\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round]
\draw[line width=.5pt] (845,104) -- (850,96) -- (854,104);
\end{tikzpicture}}''',
'S39-05': r'''structures envisagées, \uline{rigidifiées} par la
\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round]
\draw[line width=.65pt] (90,2) -- (135,0);
\draw[line width=.45pt] (375,0) -- (372,14);
\draw[line width=.45pt] (878,127) .. controls (884,119) and (898,118) .. (906,127);
\end{tikzpicture}}''',
'S39-06': r'''donnée de $e_1$, est donc $\mathbb P^1\setminus\{0,\pm2,\infty\}$
\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round]
\draw[line width=.45pt] (497,0) .. controls (502,11) and (531,15) .. (542,0);
\draw[line width=.45pt] (571,117) .. controls (575,114) and (579,115) .. (582,117);
\draw[line width=.45pt] (786,117) -- (790,104);
\draw[line width=.45pt] (896,117) -- (898,99);
\draw[line width=.45pt] (1012,117) -- (1021,104);
\draw[line width=.45pt] (1059,104) -- (1070,100);
\end{tikzpicture}}''',
'S39-07': r'''Elle s'immerse dans la multiplicité
$M_{0,5}$ --- il y a lieu de regarder l'effet
sur les \unsure{groupoïdes|groupes} fondamentaux.''',
'S39-08': r'''\margin{38}''',
}


def atomic_write(path, text):
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + '.', suffix='.tmp', dir=path.parent)
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
    assert len(ids) == 8 and ids == list(READINGS)
    data = io.StringIO(newline='')
    writer = csv.writer(data, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for box in ids:
        writer.writerow([box, READINGS[box]])
    target = OUT/'148_scan039_second.tsv'
    atomic_write(target, data.getvalue())
    journal = {
        'reader': 'blind_d',
        'page': '148_scan039',
        'assignment_order': 'scan039 after assignments of scans037 and038',
        'source_inputs': [str(PACKET/'scan.jpg'), str(PACKET/'boxes.tsv')],
        'crop_command': 'python /workspace/scratch/8132fe1cca43/work/SP82_C13_148/scripts/blind_io.py crop 39',
        'crop_count': 8,
        'crop_policy': 'Each prescribed rectangle cropped once; additional views magnified or rotated the whole saved crop only.',
        'successfully_viewed_boxes': ids,
        'whole_crop_views': [str(DISPLAY/(box+'.jpg')) for box in ids],
        'additional_successful_views': [
            str(DISPLAY/'S39-01_plain2.png'), str(DISPLAY/'S39-02_plain2.png'),
            str(DISPLAY/'S39-07_rotated.png'), str(DISPLAY/'S39-03_plain2.png'),
            str(DISPLAY/'S39-07_plain2.png'),
        ],
        'view_completeness': 'Every one of the eight entire fixed crops was visible. No truncated image output was counted as viewed.',
        'independence': 'No witness, first reading, other page, notes, review, comparison or outcome was opened. No OCR, external research or TeX compilation was used.',
        'symbol_policy': 'No formula or diagram symbol is replaced by an illegible marker; doubtful symbols retain favored readings and alternatives.',
        'print_scope_decision': {
            'treatment': 'Pale blue listing treated as reverse-side show-through, not face-side manuscript text.',
            'visual_evidence': 'The pale blue capital-letter rows show laterally reversed letter forms, especially the L/P-like forms and the longer capital-letter sequence visible beneath the final handwritten line in S39-07. A 180-degree rotation of the whole S39-07 crop does not make these forward-facing. The black handwriting is normally oriented. This decision rests on reversal, not merely on the pale color or on the paper being reused.',
        },
        'residual_uncertainties': [
            {'box':'S39-01', 'detail':'The opening favors Changer over Change. The heavily cancelled short item between base and e_1 favors en, with de an alternative. The subscript is read as numeral 1.'},
            {'box':'S39-02', 'detail':'The first cancelled word favors aussi over ainsi. The cancelled par is kept. The paired variables favor x,y, with f,g alternatives; the second transformed superscript favors 3 over 2. These are visual alternatives, not mathematical completions.'},
            {'box':'S39-03', 'detail':'The repeated letter is read xi; the parameter is read mu. The visible expressions are kept in full, including both plus/minus sets and the final i.'},
            {'box':'S39-05', 'detail':'The horizontal stroke under rigidifiées is below the letter bodies and intersects only descenders; recorded as underline, not deletion.'},
            {'box':'S39-07', 'detail':'The last noun favors groupoïdes over groupes. The main text is read Elle s\'immerse ... il y a lieu de regarder l\'effet.'},
            {'box':'S39-01 through S39-06', 'detail':'Small adjacent-line fragments at fixed crop boundaries are retained as TikZ strokes, without extrapolating clipped words.'},
        ],
        'confident_items': ['S39-04: La multiplicité modulaire pour les', 'S39-06: P^1 minus {0, plus/minus 2, infinity}', 'S39-08: 38'],
        'reading_path': str(target),
        'authoring_script': str(Path(__file__).resolve()),
        'reading_written_utc': datetime.now(timezone.utc).isoformat(),
    }
    atomic_write(OUT/'148_scan039_blind_journal.json', json.dumps(journal, ensure_ascii=False, indent=2)+'\n')
    print(f'Wrote complete blind reading: {target}; {len(ids)} rows. Procedural journal saved.')


if __name__ == '__main__':
    main()
