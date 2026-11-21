from pathlib import Path
import csv
import json
from PIL import Image

root = Path('/workspace/scratch/0cab6a548abb')
outdir = root / 'edition/second'
with (outdir / '149_scan103_boxes.tsv').open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))

readings = {
    'b01': r'\(a)\Longrightarrow b)\Longrightarrow c)\Longrightarrow d),\)',
    'b02': r'et \(d\Longrightarrow a\) devrait être',
    'b03': r'connue, ou du moins se prouver ;',
    'b04': r'conditions impliquent \(e\),',
    'b05': r'faudrait une \unsure{compilation|complication} (\unsure{fct.|fond.} des \\ celles',
    'b06': r'\margin{Ça vaudrait la peine de regarder en premier le cas \unsure{\(I\)|\(t\)} où \(X_{\unsure{\eta|y}}=\widehat{U}_{\unsure{\eta|y}}\) a bonne réduction --- \uline{mais} la multisection \inserted{\(X_{\unsure{\eta|y}}-U_{\unsure{\eta|y}}\)} de \(X\) sur \(S\) n\textquotesingle est pas étale. Le cas du genre \(0\) devrait être particulièrement aisé : regarder\ldots}',
    'b07': r'qui lui vient) pour \\ \inserted{\unsure{\(\mathrm{I}\)|et} naturelles}',
    'b08': r'\inserted{\unsure{\(\mathrm{I}\)|et} naturelles} \\ définitives',
    'b09': r'(\(h\) \deleted{est} de type fini',
    'b10': r'\unsure{sur} du \(\pi\) \unsure{à|:} \(\unsure{\ell|\mathcal L}\) \unsure{ad|ct},',
    'b11': r'\inserted{(sans doute)} \\ un \unsure{sens}',
    'b12': r'par \deleted{\unsure{des|de}} la',
    'b13': r'de type \(g,\unsure{\nu|n}\)',
    'b14': "``se réduisant mal''. Mais je m'avise",
    'b15': r'\mspage{51}',
    'b16': r'\margin{102}',
    'b18': r'\unsure{caractéristiques|heuristique})',
    'b19': r'\inserted{sans} \\ un \unsure{sens} géométrique,',
    'b20': r'de \(\mathbb{Q}\))',
}
readings['b06'] = readings['b06'].replace(r'n\textquotesingle est', "n'est")

notes = {
    'b01': {'ambiguities': [], 'clipped_context': []},
    'b02': {'ambiguities': [], 'clipped_context': []},
    'b03': {'ambiguities': [], 'clipped_context': []},
    'b04': {'ambiguities': [], 'clipped_context': ['A small upper stroke of the following line touches the lower edge; it is not completed.']},
    'b05': {
        'ambiguities': ['The long noun after une has the visible sequence comp...tion; compilation is the leading reading, with complication retained as an alternative.', 'The abbreviation after the opening parenthesis is uncertain between fct. and fond.'],
        'clipped_context': ['Descenders from the preceding line enter at the top.', 'The following line is largely cut through horizontally. Its rightmost word celles is wholly visible and is transcribed on a separate line; the clipped preceding words are not completed.']
    },
    'b06': {
        'ambiguities': ['The opening mark reads Ça as part of the marginal sentence; no independent numeral is securely distinguishable in this box.', 'A small character after cas may be I or t, or an overlapping stroke. Its status as a separate character is uncertain.', 'The repeated subscripts resemble either eta or Latin y; this alphabet distinction remains unresolved.', 'The bar below mais is read as an underline, not as a fraction bar. X_subscript minus U_subscript lies interlinearly below it and is represented as an insertion adjoining multisection.'],
        'clipped_context': ['The diagonal marginal note overlaps the main text. Incomplete main-text fragments at the right edge and bottom are not completed.', 'The notation and words are transcribed in marginal-note reading order after visual rotation.'],
        'layout': 'Diagonal marginal note. Viewed unrotated, then using derived rotations of -45 and -35 degrees. The short mathematical expression is interlinear beneath the underlined word mais.'
    },
    'b07': {
        'ambiguities': ['The first sign of the interlinear addition has an I-like shape with top and bottom bars; et is retained as a possible word reading.'],
        'clipped_context': ['The enclosing insertion leader continues outside the lower edge; only the complete words in this box are included.']
    },
    'b08': {
        'ambiguities': ['The sign before naturelles resembles a barred capital I; et is a possible reading.'],
        'clipped_context': ['Small portions of the previous line enter at the upper edge.'],
        'layout': 'The addition above définitives is enclosed by a long curved line below it with a rising right end. The curved enclosure is treated as an insertion leader rather than inventing paired textual parentheses.'
    },
    'b09': {'ambiguities': [], 'clipped_context': ['No closing parenthesis occurs in this box.'], 'cancellation': 'The word est is crossed through but remains readable.'},
    'b10': {
        'ambiguities': ['The first word is tentatively sur.', 'The two separated marks following pi may be à or a colon.', 'The following tall sign may be lowercase script ell or calligraphic L.', 'The final short sequence appears ad; ct remains an alternative.'],
        'clipped_context': []
    },
    'b11': {
        'ambiguities': ['The main-line word following un is only tentatively read sens. Its strokes are visible, but the cursive letter interpretation is not secure.'],
        'clipped_context': [],
        'layout': '(sans doute) is written above the main line.'
    },
    'b12': {
        'ambiguities': ['The cancelled word is uncertain between des and de because the strike obscures its end.'],
        'clipped_context': ['A descender from the preceding line enters at the upper edge.']
    },
    'b13': {
        'ambiguities': ['The letter following g and a comma resembles Greek nu or Latin n; no alphabet choice is imposed.'],
        'clipped_context': ['The tall stroke of type reaches the upper edge, but the word remains readable.', 'Only tiny tips from the following line enter at the lower edge; they are not completed.']
    },
    'b14': {'ambiguities': [], 'clipped_context': ['A small remnant of the preceding line is visible at the upper edge.']},
    'b15': {'ambiguities': [], 'clipped_context': [], 'classification': 'Dark author page number 51.'},
    'b16': {'ambiguities': [], 'clipped_context': [], 'classification': 'Thin foliation 102.'},
    'b18': {
        'ambiguities': ['Initial and medial strokes of the main word overlap the diagonal marginal note. caractéristiques and heuristique are retained as competing readings; the final singular/plural distinction is not secure.'],
        'clipped_context': ['Diagonal marginal-note fragments enter on the left and are not completed in this box.', 'A descender from the preceding main-text line enters above.']
    },
    'b19': {
        'ambiguities': ['The word after un is tentatively sens.'],
        'clipped_context': ['The insertion above is cut at the top and left. Only the complete sans is entered; the clipped remainder is not completed from the overlapping box.']
    },
    'b20': {'ambiguities': [], 'clipped_context': ['A small rounded stroke from the preceding line enters at the top.'], 'symbol': 'The Q has a doubled/blackboard-style outline.'},
}

assert set(readings) == {row['box'] for row in boxes}
with (outdir / '149_scan103_second.tsv').open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in boxes:
        writer.writerow([row['box'], readings[row['box']]])

inspections = []
for row in boxes:
    crop = root / f"edition/crops/149_scan103_second_{row['box']}.png"
    with Image.open(crop) as img:
        dimensions = list(img.size)
    inspections.append({
        'box': row['box'],
        'successful_visual_inspection': True,
        'crop_file': str(crop),
        'bbox_original_pixels': [int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')],
        'rotation_degrees': 0,
        'crop_dimensions_pixels': dimensions,
        'reused_existing_image_only_crop': True,
        **notes[row['box']],
    })

observations = {
    'reader_identity': '/root/blind_a2',
    'page': '149_scan103',
    'source_image': str(root / 'source/SP88_C13_149_scans/149_scan103.jpg'),
    'box_list': str(outdir / '149_scan103_boxes.tsv'),
    'protocol': str(outdir / 'READING_PROTOCOL.md'),
    'reading_method': 'Independent visual reading of the existing Pillow crops. No OCR, first-reading TSV, candidate TeX, witnesses, notes, comparison output, external research, or TeX compilation was used.',
    'source_page_visual_inspection': True,
    'source_page_use': 'The same authorized page image was viewed once to distinguish diagonal marginal writing from the main-text layers. Clipped neighboring words were not completed from the wider view.',
    'crop_making_script': str(outdir / 'make_149_scan103_second_blind_a2.py'),
    'inspection_count': len(inspections),
    'inspections': inspections,
    'additional_visual_inspections': [
        {'box': 'b06', 'crop_file': str(root / 'edition/crops/149_scan103_second_b06_rotminus45.png'), 'bbox_original_pixels': [17, 800, 440, 1668], 'rotation_degrees': -45, 'successful_visual_inspection': True, 'derived_from_existing_crop': True},
        {'box': 'b06', 'crop_file': str(root / 'edition/crops/149_scan103_second_b06_rotminus35.png'), 'bbox_original_pixels': [17, 800, 440, 1668], 'rotation_degrees': -35, 'successful_visual_inspection': True, 'derived_from_existing_crop': True},
        {'box': 'b05', 'crop_file': str(root / 'edition/crops/149_scan103_second_b05.png'), 'rotation_degrees': 0, 'successful_visual_inspection': True, 'repeat_view': True},
    ],
    'status': 'Complete independent reading; frozen upon completion report.'
}
with (outdir / '149_scan103_second_observations.json').open('w', encoding='utf-8') as handle:
    json.dump(observations, handle, ensure_ascii=False, indent=2)
    handle.write('\n')

print(json.dumps({'page': '149_scan103', 'rows': len(boxes), 'inspected_boxes': len(inspections), 'files_written': 2}, ensure_ascii=False))
