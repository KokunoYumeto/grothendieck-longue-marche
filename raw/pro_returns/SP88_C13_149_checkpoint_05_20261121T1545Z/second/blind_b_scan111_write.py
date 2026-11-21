from pathlib import Path
import csv
import json
import hashlib

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan111'
SECOND = ROOT / 'edition' / 'second'

readings = {
    'b01': r"\margin{\unsure{Dans|Sans} l'hyp. d'homo- \\ \unsure{fibration} \\ ``\unsure{sont|tout} \unsure{ca.|ça} \\ \unsure{topie|topos}'', mais \\ \unsure{par|pour} ici.} On \\ \unsure{un|en} \(X\longrightarrow\) \\ (14)",
    'b02': r'On aura une fibration \unsure{hom.|loc.} de',
    'b03': r"(14) \(X\longrightarrow Y'\longrightarrow Y\)",
    'b04': r"et \(\unsure{\mathcal{E}|\mathcal{G}}'_X\longrightarrow\unsure{\mathcal{E}|\mathcal{G}}_{Y'}\) est \unsure{évidemment|evidemment} épi,",
    'b05': r"\deleted{donc} cette suite exacte \unsure{usuell.|usuelle} d'homotopie",
    'b06': r'bien sûr. On aura dans ce cas',
    'b07': r"(15) \(\unsure{\mathcal{E}|\mathcal{G}}_{X/Y}^{T}\xrightarrow{\sim}\unsure{\mathcal{E}|\mathcal{G}}_{X/Y'}^{T^{\unsure{A|a}}}\)",
    'b08': r'qui peut donc se calculer comme',
    'b09': r"(16) \(\unsure{\mathcal{E}|\mathcal{G}}_{X\times_{Y'}T}^{T}\simeq\unsure{\mathcal{E}|\mathcal{G}}_{X/Y}^{T}\)",
    'b10': r"qu'on peut noter \(\unsure{\mathcal{E}|\mathcal{G}}_{X_T}^{T}\), mais en",
    'b11': r'faisant attention que maintenant',
    'b12': r"\(X_T\) désigne non pas \(X\times_Y T\) (qui va être disconnexe \inserted{si \(Y'\longrightarrow Y\) pas iso}) mais \(X\times_Y T\).",
    'b13': r'Bien sûr, à iso. can. près je peux',
    'b14': r"\deleted{\unsure{et|de}} remplacer, pour le calcul de \(\unsure{\mathcal{E}|\mathcal{G}}^{T}_{X_{\deleted{\unsure{T|Y'}}}}\),",
    'b15': r'\(T\) par \(\widetilde{y}\) \unsure{pour|pris} un point de \(X_T\), et pour',
    'b16': r"\(\widetilde{X}\) pour ce qui est de \unsure{l'image} de \(X_{\widetilde{y}}\),",
    'b17': r'\mspage{55}',
    'b18': r'\margin{110}',
}

notes = {
    'b01': {
        'ambiguities': [
            'The angled marginal note has heavily compressed, overlapping prose. Dans/Sans, sont/tout, ca./ça, topie/topos, and par/pour remain unresolved; the proposed fibration is also uncertain.',
            'Line order within the marginal note is recorded provisionally from the visible placement; the surviving pieces are not expanded into a reconstructed sentence.',
            'The short complete body word before X is un/en.',
        ],
        'clipped_material': [
            'The body word following On is cut by the right edge and is not completed in this box.',
            'The Y-shaped target to the right of the X arrow is clipped by the right edge and is not completed.',
            'Some outer strokes of the marginal note approach the crop edge; no external continuation is supplied.',
        ],
        'inspection_count': 3,
        'layers': 'Angled marginal prose overlaps the beginning of the main text. Complete body material retained independently is On, un/en, X with a rightward arrow, and the literal label (14).',
    },
    'b02': {
        'ambiguities': ['The abbreviation after fibration is heavily retraced and remains hom./loc.'],
        'clipped_material': ['Strokes of the angled marginal note enter above and beside the first body word; they are not completed from this box.'],
        'inspection_count': 2,
    },
    'b03': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b04': {
        'ambiguities': ['The script mathematical letter is E/G.', 'The initial accent of évidemment is not independently secure; the accent of épi is visible.'],
        'clipped_material': ['Small ascender remnants from the following line enter the lower edge and are not completed.'],
        'inspection_count': 1,
    },
    'b05': {
        'ambiguities': ['The word following exacte ends in a dotlike stroke; usuell. and usuelle remain alternatives.'],
        'clipped_material': ['Fragments of the previous formula enter along the upper edge.'],
        'inspection_count': 2,
        'layers': 'The initial donc is crossed horizontally; the following cette suite exacte is uncancelled.',
    },
    'b06': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 2},
    'b07': {
        'ambiguities': ['The script mathematical letter is E/G.', 'A faint A/a-shaped trace touches the upper-right end of the right-hand T crossbar. It is retained as an uncertain raised mark; its attachment and ink layer are not secure.'],
        'clipped_material': [],
        'inspection_count': 1,
    },
    'b08': {
        'ambiguities': [],
        'clipped_material': ['Upper parts of the following displayed formula enter at the bottom edge and are not completed in this box.'],
        'inspection_count': 1,
    },
    'b09': {
        'ambiguities': ['The script mathematical letter is E/G.'],
        'clipped_material': ['Descender fragments from the preceding line enter the top edge.'],
        'inspection_count': 1,
    },
    'b10': {
        'ambiguities': ['The script mathematical letter is E/G.'],
        'clipped_material': ['Tiny partial strokes at the bottom belong to the neighbouring line and are not completed.'],
        'inspection_count': 2,
    },
    'b11': {
        'ambiguities': ['A very faint pencil-like or show-through trace between attention and que resembles 28; its status as foreground writing is uncertain, so it is recorded here rather than treated as a word.'],
        'clipped_material': ['Parts of the following line enter along the bottom edge.', 'A descender from the previous line enters at the top edge.'],
        'inspection_count': 2,
    },
    'b12': {
        'ambiguities': [
            'Both visible product expressions are transcribed with base Y: no separate prime is securely visible on either base letter. The explicit prime in the inserted Y-prime to Y condition is visible and retained.',
            'The initial X and multiplication sign in the lower product are heavily retraced, without a separately distinguishable changed underletter.',
        ],
        'clipped_material': ['Descender remnants of the preceding line enter at the upper edge.'],
        'inspection_count': 2,
        'layers': 'The main parenthesis runs from (qui through disconnexe). The condition si Y-prime right-arrow Y pas iso is inserted above the end of disconnexe and the closing parenthesis, linked by a curved leader.',
    },
    'b13': {
        'ambiguities': [],
        'clipped_material': ['Only upper fragments of the following prose and script formula enter the lower edge; they are not completed.'],
        'inspection_count': 3,
    },
    'b14': {
        'ambiguities': ['The initial cancelled short word is et/de.', 'The cancelled index after/below X is T/Y-prime; the strokes are heavily overlaid.', 'The script mathematical letter is E/G.'],
        'clipped_material': ['Partial preceding-line letters enter along the top; they are not transcribed as complete words.'],
        'inspection_count': 2,
        'layers': 'The formula retains the X and records the heavily struck following/lower index separately. The X itself is retraced, but no different underletter can be distinguished.',
    },
    'b15': {
        'ambiguities': ['The word following y-tilde is pour/pris.', 'The y-tilde is read as a point letter; its handwritten shape alone does not securely distinguish lower-case y from capital Y.'],
        'clipped_material': ['The descenders of par and the word after y-tilde meet the lower edge.', 'Fragments of the following line enter at the bottom.'],
        'inspection_count': 2,
    },
    'b16': {
        'ambiguities': ["The contracted phrase after de is tentatively read l'image; its middle strokes are compressed."],
        'clipped_material': ['Descenders from the preceding line enter the upper edge.', 'The lower scan/page border clips the extreme ends of the p and q descenders; the words themselves remain identifiable.'],
        'inspection_count': 2,
    },
    'b17': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b18': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
}

wrapped_boxes = {'b02', 'b05', 'b06', 'b10', 'b11', 'b12', 'b13', 'b14', 'b15', 'b16'}
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
    item = {
        'box': box,
        'successful_visual_inspection': True,
        'crop_file': str(crop),
        'bbox_original_pixels': [int(row[k]) for k in ('x0', 'y0', 'x1', 'y1')],
        'rotation_degrees': -25 if box == 'b01' else 0,
        'rotation_convention': 'Pillow: negative angle is clockwise',
        'scale_factor': 3,
        'source_coordinate_crop_count': 1,
        'processing': 'One original-coordinate Pillow crop, RGB autocontrast with default zero cutoff, LANCZOS enlargement. b01 additionally rotated clockwise 25 degrees using BICUBIC and expanded white bounds.',
        **notes[box],
    }
    if box == 'b01':
        item['visual_inspection_rotations'] = [0, -25, -25]
    if box in wrapped_boxes:
        wrapped = SECOND / 'diagnostics' / f'{PAGE}_{box}_wrapped.png'
        assert wrapped.is_file()
        item['additional_inspection_view'] = str(wrapped)
        item['additional_view_method'] = 'Labelled overlapping panels composed only from the already-saved enlarged crop; no additional source-image crop and no recognition software.'
    inspections.append(item)

observations = {
    'reader_identity': '/root/blind_b',
    'page': PAGE,
    'method': 'Independent image-only diplomatic reading. No OCR, text recognition, PDF text layer, external research, TeX compilation, witnesses, first readings, candidates, notation tables, notes, or comparison/adjudication files consulted.',
    'task_inputs': [
        str(ROOT / 'source' / 'SP88_C13_149_scans' / f'{PAGE}.jpg'),
        str(SECOND / f'{PAGE}_boxes.tsv'),
        str(SECOND / 'READING_PROTOCOL.md'),
    ],
    'protocol': 'Previously read neutral READING_PROTOCOL.md retained; all subsequent manuscript evidence came from this page and its saved crops.',
    'crop_making_script': str(SECOND / 'blind_b_scan111_crop.py'),
    'inspection_script': str(SECOND / 'blind_b_scan111_inspect.py'),
    'box_count': len(boxes),
    'successful_visual_inspection_count': len(inspections),
    'total_visual_display_count': sum(item['inspection_count'] for item in inspections),
    'canonical_crop_count': len(boxes),
    'derivative_inspection_view_count': len(wrapped_boxes),
    'inspection_list': inspections,
    'transcription_sha256': hashlib.sha256(tsv.read_bytes()).hexdigest(),
    'status': 'complete; frozen before comparison',
}

obs = SECOND / f'{PAGE}_second_observations.json'
obs.write_text(json.dumps(observations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

with tsv.open(encoding='utf-8', newline='') as f:
    check = list(csv.DictReader(f, delimiter='\t'))
assert len(check) == 18
assert all(set(r) == {'box', 'reading'} and r['reading'] for r in check)
assert [r['box'] for r in check] == [r['box'] for r in boxes]
assert json.loads(obs.read_text(encoding='utf-8'))['successful_visual_inspection_count'] == 18
print(f'Completed {len(check)} TSV readings, {len(inspections)} successful box inspections, {observations["total_visual_display_count"]} image displays.')
print(f'TSV SHA256: {observations["transcription_sha256"]}')
print(f'Observations SHA256: {hashlib.sha256(obs.read_bytes()).hexdigest()}')
