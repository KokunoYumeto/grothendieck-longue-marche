from pathlib import Path
import csv
import hashlib
import json
from PIL import Image

root = Path('/workspace/scratch/0cab6a548abb')
outdir = root / 'edition/second'
with (outdir / '149_scan116_boxes.tsv').open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))

readings = {
    'b01': r"c'est la partie ``universelle géom'' de \\ \(\mathcal E^{\bar L}_{\deleted{\unsure{L}}\inserted{X}}\), \deleted{noté \(\mathcal E_{L/K}^{\unsure{g|b}\bar L}\)} \inserted{(relativement à \(K\))} \deleted{qui \unsure{couvre} les \illegible{1}} qui \\ classifie les schémas (finis) étales sur \(L\) \\ qui sont ``non ramifiés'' sur \uline{tout} modèle \\ \deleted{\unsure{étal|étale}} régulier (propre ou non) de \(L/K\).",
    'b02': r'\margin{noté \(\mathcal E_L^{\unsure{g|b}\bar L}\) ou \(\mathcal E_L^{\unsure{g(K)|b(K)},\bar L}\)}',
    'b03': r'Si \(U\) est un modèle quelconque, \\ il se plonge dans un \(X\), et on a \\ \margin{\unsure{\S|1}} des homom surjectifs \\ (21) \(\mathcal E_L^{\bar L}\longrightarrow\mathcal E_U^{\bar L}\longrightarrow\mathcal E_X^{\bar L}=\mathcal E_{\deleted{\unsure{X}}\inserted{L}}^{\unsure{g|b}\bar L}\)',
    'b04': r'On aura \deleted{\unsure{étal}} \\ (22) \(U=X\setminus Z\)',
    'b05': r'\(Z\) partie fermée de \(X\) --- soient \(D_i\) \\ ses composantes de codim \(1\), \(x_i\) le \\ pt gén. de \(D_i\). On a des',
    'b06': r"groupes de décomposition et d'inertie \\ \(N_{x'_i}\) et \(I_{x'_i}\) \inserted{de \(\mathcal E_U^{\bar L}\)} (\unsure{et} relatifs au choix d'un \\ \(x'_i\) au dessus de \(x_i\) dans le normalisé \\ \(\unsure{X|X'|Y}\) de \(\bar L\)), et on trouve",
    'b07': r'\margin{115}',
}

notes = {
    'b01': {
        'ambiguities': [
            'The subscript of the first E has a dark L-like upright and foot crossed by X-like diagonals. The reading treats L as the tentative underletter and X as the visible replacement; the precise stroke chronology remains uncertain.',
            'The superscript character before bar-L in the cancelled notation is ambiguous between g and b.',
            'The cancelled lower clause begins qui, followed by a tentative couvre, then les. Its last crossed word is physically obscured and is recorded as one illegible word.',
            'The deleted word before régulier is uncertain between étal and étale.'
        ],
        'clipped_context': ['The box includes the complete final L/K and its period. No neighboring words have been completed.'],
        'correction_layers': {
            'main_text': 'The quoted universelle géom description, the E expression, qui classifie les schémas, and the subsequent non ramifiés clause remain legible.',
            'upper_deletion': 'noté and the interlinear E_(L/K) expression are crossed through.',
            'insertion': '(relativement à K) is interlinear, with a curved leader toward the surviving qui.',
            'lower_deletion': 'qui [tentatively couvre] les [one obscured word] is crossed through on the main line.',
            'later_deletion': 'The étal/étale word before régulier is crossed through.'
        },
        'underlining': 'tout has a single separate underline.',
        'quotation': 'Two quoted spans are visible: universelle géom and non ramifiés. No separate abbreviation period after géom is securely visible.'
    },
    'b02': {
        'ambiguities': [
            'The superscript character adjoining bar-L in the first term resembles g or b.',
            'The corresponding leading superscript group in the second term is heavily rewritten; g(K) and b(K) are retained as alternatives.',
            'No distinct earlier complete character can be recovered from beneath the dark rewritten second superscript.'
        ],
        'clipped_context': [],
        'layout': 'Diagonal marginal note, read after a -50 degree rotation of the existing crop. It reads noté, the first E notation, ou, and the second E notation.',
        'symbols': 'Both E expressions have subscript L. The first superscript includes a bar over L; the second includes the rewritten parenthesized group, a comma, and bar-L.'
    },
    'b03': {
        'ambiguities': [
            'A small isolated marginal mark beside des is ambiguous between a section-sign-like form and digit 1.',
            'The final superscript character before bar-L is ambiguous between g and b.',
            'The final subscript is a heavy L over X-like diagonal strokes. The underlying X is tentative; the visible L is retained.'
        ],
        'clipped_context': [],
        'correction_layers': 'The U subscript in the middle term is retraced without a securely recoverable different underletter. The final L subscript covers X-like strokes.',
        'short_forms_preserved': ['homom'],
        'symbols': 'The two arrows in (21) point right. The final relation is an equals sign. Each displayed L in a superscript has a separate overbar.',
        'classification': '(21) is a literal formula label.'
    },
    'b04': {
        'ambiguities': ['The crossed short word after On aura is tentatively read étal; its middle letters are partially hidden by cancellation.'],
        'clipped_context': [],
        'nontextual_or_unresolved_traces': ['A faint pencil-like loop to the right of the cancelled word does not yield a complete word or numeral.', 'Two tiny low ink dots stand in otherwise empty space and do not have a securely distinguishable textual function.'],
        'symbols': 'The short descending diagonal between X and Z is transcribed as set difference.',
        'classification': '(22) is a literal formula label.'
    },
    'b05': {
        'ambiguities': ['The O of On is heavily retraced; no distinct previous letter is recoverable.'],
        'clipped_context': ['The high cap of the first D_i touches the upper edge; the D and its i index remain distinguishable.'],
        'short_forms_preserved': ['codim', 'pt', 'gén.'],
        'symbols': 'The visible number following codim is 1. Both D and x carry i indices.'
    },
    'b06': {
        'ambiguities': [
            'A short word between the opening curved mark and relatifs appears to be et. It is retained tentatively rather than silently removed.',
            'The normalization symbol on the last line is uncertain between X, X-prime and Y. The surviving crossed/forked strokes do not securely determine the letter or a separate prime.',
            'The last letters of trouve are retraced, but no earlier separate word is recoverable.'
        ],
        'clipped_context': ['The comma after the closing parenthesis reaches the lower crop edge. No following continuation is supplied.'],
        'correction_layers': 'de E_U^barL is interlinear above the subgroup symbols, with a curved leader descending toward the opening parenthetical passage. N and I have dark retraced stems; no distinct overwritten letters are recoverable.',
        'symbols': 'The subgroup symbols are N and a barred-serif capital I, each indexed by x-prime with lower i. The same primed indexed x recurs in the following line. The unprimed comparison point is x_i.',
        'spelling_preserved': 'au dessus is written without supplying a hyphen.'
    },
    'b07': {'ambiguities': [], 'clipped_context': [], 'classification': 'Thin foliation 115.'},
}

assert set(readings) == {row['box'] for row in boxes}
tsv = outdir / '149_scan116_second.tsv'
with tsv.open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in boxes:
        writer.writerow([row['box'], readings[row['box']]])

inspections = []
for row in boxes:
    crop = root / f"edition/crops/149_scan116_second_{row['box']}.png"
    with Image.open(crop) as img:
        dimensions = list(img.size)
    inspections.append({
        'box': row['box'],
        'successful_visual_inspection': True,
        'crop_file': str(crop),
        'bbox_original_pixels': [int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')],
        'rotation_degrees': 0,
        'crop_dimensions_pixels': dimensions,
        'created_once_from_authorized_source': True,
        'processing': 'Pillow crop at listed original coordinates; autocontrast; LANCZOS enlargement.',
        **notes[row['box']],
    })

observations = {
    'reader_identity': '/root/blind_a2',
    'page': '149_scan116',
    'source_image': str(root / 'source/SP88_C13_149_scans/149_scan116.jpg'),
    'box_list': str(outdir / '149_scan116_boxes.tsv'),
    'protocol': str(outdir / 'READING_PROTOCOL.md'),
    'reading_method': 'Independent image-only visual reading. No OCR, witnesses, first readings, candidate text, notation, notes, comparison/adjudication files, external research or TeX compilation was used.',
    'source_page_visual_inspection': True,
    'source_page_use': 'The authorized full page was viewed once to distinguish main text, marginal notation and interlinear/cancelled layers. Clipped neighbors were not completed from that view.',
    'crop_making_script': str(outdir / 'make_149_scan116_second_blind_a2.py'),
    'inspection_count': len(inspections),
    'inspections': inspections,
    'additional_visual_inspections': [
        {'box': 'b02', 'crop_file': str(root / 'edition/crops/149_scan116_second_b02_rotminus50.png'), 'bbox_original_pixels': [16, 48, 292, 435], 'rotation_degrees': -50, 'successful_visual_inspection': True, 'derived_from_existing_crop': True}
    ],
    'status': 'Complete independent reading; frozen upon completion report.'
}
obs = outdir / '149_scan116_second_observations.json'
with obs.open('w', encoding='utf-8') as handle:
    json.dump(observations, handle, ensure_ascii=False, indent=2)
    handle.write('\n')

print(json.dumps({
    'page': '149_scan116',
    'rows': len(boxes),
    'inspected_boxes': len(inspections),
    'files': [{'name': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in (tsv, obs)],
}, ensure_ascii=False))
