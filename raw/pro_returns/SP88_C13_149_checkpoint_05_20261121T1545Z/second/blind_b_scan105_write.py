from pathlib import Path
import csv
import json
import hashlib

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan105'
SECOND = ROOT / 'edition' / 'second'

readings = {
    'b01': r"\inserted{d'\unsure{extension|extensions},}",
    'b02': r'\mspage{52}',
    'b03': r'4.',
    'b04': r'précision de \unsure{notation|notations}.',
    'b05': r'\unsure{je|y} \deleted{\unsure{le|de}} note \deleted{\(\unsure{\mathcal{E}|\mathcal{G}}_X\)}',
    'b06': r'(1) \(\unsure{\mathcal{E}|\mathcal{G}}_X = \Pi_1(X)\)',
    'b07': r'(2)',
    'b08': r'\(\unsure{\mathcal{E}|\mathcal{G}}_X^{(\widetilde{X})} = \Pi_1(X;\widetilde{X}) = \operatorname{Aut}_X(\widetilde{X})\)',
    'b09': r'recouvrant \\ \(\unsure{\mathcal{E}|\mathcal{G}}_A^{\widetilde{A}}\) \inserted{\(=\unsure{\mathcal{E}|\mathcal{G}}_X^{\unsure{\widetilde{X}|\alpha}}\)} (si \(\widetilde{A}\)',
    'b10': r'est une \(A\)-algèbre telle que \(\operatorname{Spec}(\widetilde{A})=\widetilde{X}\)',
    'b11': r'; dans un unique',
    'b12': r'si \(\unsure{\xi|\zeta}\) est un',
    'b13': r"``point géométrique'' de \(X\),",
    'b14': r'(3) \(\unsure{\mathcal{E}|\mathcal{G}}_X^{\unsure{\xi|\zeta}} = \Pi_1(X,\unsure{\xi|\zeta}) = \unsure{\mathcal{E}|\mathcal{G}}_X^{\widetilde{X}(\unsure{\xi|\zeta})}\), où \(\widetilde{X}(\unsure{\xi|\zeta})\) est le \unsure{pro|pro-}',
    'b15': r'\(X\) pointé en \(\unsure{\xi|\zeta}\). Le choix',
    'b16': r'\margin{104}',
}

notes = {
    'b01': {
        'ambiguities': ['Final n/s strokes are fused: extension and extensions remain alternatives.'],
        'clipped_material': ['An insertion leader or enclosing stroke runs along and partly beyond the lower edge; its lettering is not clipped.'],
        'inspection_count': 2,
    },
    'b02': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b03': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b04': {
        'ambiguities': ['The final word is read notation/notations; the possible terminal s is not separately resolved. The first word is read précision from its two dotted i strokes and accented opening letters.'],
        'clipped_material': [],
        'inspection_count': 2,
    },
    'b05': {
        'ambiguities': ['Initial cursive word may be je or y.', 'The crossed word before note has distinguishable strokes compatible with le or de.', 'The crossed mathematical symbol is a script E/G with subscript X; the distinction remains unresolved.'],
        'clipped_material': [],
        'inspection_count': 2,
    },
    'b06': {
        'ambiguities': ['The leading script mathematical letter is visually compatible with calligraphic E or G.'],
        'clipped_material': [],
        'inspection_count': 1,
    },
    'b07': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b08': {
        'ambiguities': ['The leading script mathematical letter is visually compatible with calligraphic E or G.'],
        'clipped_material': ['A small partial stroke from the neighbouring lower line enters at the bottom right; it is not transcribed.'],
        'inspection_count': 1,
    },
    'b09': {
        'ambiguities': ['The inserted superscript above the right-hand script letter is read as either a tightly written tilde-X or alpha.', 'Both script mathematical letters remain E/G alternatives.', 'The long rising insertion leader meets the tilde above the lower A, making those layers overlap.'],
        'clipped_material': ['A tiny stroke from preceding material enters at the far left of the upper line.', 'The parenthetical phrase begins (si A-tilde and continues outside the box; no closing parenthesis is supplied.'],
        'inspection_count': 2,
        'layers': 'Upper prose: recouvrant. Main formula: script letter with subscript A and superscript tilde-A. Inserted equality lies above and to its right, with a rising leader. Lower prose starts the parenthesis (si, followed by tilde-A.',
    },
    'b10': {
        'ambiguities': [],
        'clipped_material': ['Descender fragments from the previous line enter the top edge and are not completed.'],
        'inspection_count': 1,
    },
    'b11': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b12': {
        'ambiguities': ['The tall sinuous mathematical letter is xi or zeta; its upper/middle strokes do not securely distinguish them.'],
        'clipped_material': ['A descender fragment enters at the upper edge, and a small stroke from the following line enters at the lower edge. Neither is completed.'],
        'inspection_count': 1,
    },
    'b13': {
        'ambiguities': [],
        'clipped_material': ['Some descenders of the target phrase meet the bottom edge; the complete identifiable words are retained.', 'Partial strokes from the previous line enter the top edge and are not completed.'],
        'inspection_count': 1,
    },
    'b14': {
        'ambiguities': ['The script mathematical letter remains E/G.', 'Each tall sinuous letter is recorded as xi/zeta.', 'The last visible word is pro, with a possible connected terminal hyphen.', 'A short vertical mark below the superscript parenthesis is read as the descender of its xi/zeta, not as a separately added prime.'],
        'clipped_material': ['Descender remnants from the preceding prose enter at the top edge.', 'Small fragments of the next line enter the bottom edge; they are not completed.'],
        'inspection_count': 2,
    },
    'b15': {
        'ambiguities': ['The mathematical letter after en remains xi/zeta.'],
        'clipped_material': ['The upper ends of the tall mathematical letter and of Le/choix touch the top boundary; no neighbouring letters are inferred.'],
        'inspection_count': 1,
    },
    'b16': {'ambiguities': [], 'clipped_material': ['A dark page/scan border lies along the lower edge.'], 'inspection_count': 1},
}

with (SECOND / f'{PAGE}_boxes.tsv').open(encoding='utf-8', newline='') as f:
    boxes = list(csv.DictReader(f, delimiter='\t'))
assert [r['box'] for r in boxes] == list(readings)

tsv = SECOND / f'{PAGE}_second.tsv'
with tsv.open('w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in boxes:
        writer.writerow([row['box'], readings[row['box']]])

inspections = []
for row in boxes:
    box = row['box']
    crop = ROOT / 'edition' / 'crops' / f'{PAGE}_second_{box}.png'
    assert crop.is_file()
    inspections.append({
        'box': box,
        'successful_visual_inspection': True,
        'crop_file': str(crop),
        'bbox_original_pixels': [int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')],
        'rotation_degrees': 0,
        'scale_factor': 3,
        'processing': 'Single original-coordinate Pillow crop, RGB autocontrast with default zero cutoff, LANCZOS enlargement.',
        **notes[box],
    })

observations = {
    'reader_identity': '/root/blind_b',
    'page': PAGE,
    'method': 'Independent image-only diplomatic reading of the supplied boxes. No OCR, text recognition, PDF text layer, external research, TeX compilation, witnesses, first readings, other page images, or comparison output consulted.',
    'task_inputs': [
        str(ROOT / 'source' / 'SP88_C13_149_scans' / f'{PAGE}.jpg'),
        str(SECOND / f'{PAGE}_boxes.tsv'),
        str(SECOND / 'READING_PROTOCOL.md'),
    ],
    'crop_making_script': str(SECOND / 'blind_b_scan105_crop.py'),
    'box_count': len(boxes),
    'successful_visual_inspection_count': len(inspections),
    'total_visual_display_count': sum(item['inspection_count'] for item in inspections),
    'inspection_list': inspections,
    'transcription_sha256': hashlib.sha256(tsv.read_bytes()).hexdigest(),
    'status': 'complete; frozen before comparison',
}

obs = SECOND / f'{PAGE}_second_observations.json'
obs.write_text(json.dumps(observations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

with tsv.open(encoding='utf-8', newline='') as f:
    check = list(csv.DictReader(f, delimiter='\t'))
assert len(check) == 16
assert all(set(r) == {'box', 'reading'} and r['reading'] for r in check)
assert [r['box'] for r in check] == [r['box'] for r in boxes]
assert json.loads(obs.read_text(encoding='utf-8'))['successful_visual_inspection_count'] == 16
print(f'Completed {len(check)} TSV readings, {len(inspections)} successful box inspections, {observations["total_visual_display_count"]} image displays.')
print(f'TSV SHA256: {observations["transcription_sha256"]}')
print(f'Observations SHA256: {hashlib.sha256(obs.read_bytes()).hexdigest()}')
