from pathlib import Path
import csv
import hashlib
import json
from PIL import Image

root = Path('/workspace/scratch/0cab6a548abb')
outdir = root / 'edition/second'
with (outdir / '149_scan112_boxes.tsv').open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))

readings = {
    'b01': r"où \(\tilde X,\tilde Y\) sont les rev. universels de \(X,Y\) déduits de \inserted{\(T\longrightarrow X\) et de \(T\longrightarrow Y\),} \\ de telle façon que l'on obtient",
    'b02': r'(17) \(\mathcal E^{\unsure{T|\cdot T}}_{X/Y}\simeq\mathcal E^{\tilde X}_{X/Y}\simeq\operatorname{Ker}(\mathcal E^{\tilde X}_X\longrightarrow\mathcal E^{\tilde Y}_Y)\)',
    'b03': r'(sous hyp de suite exacte) \\ \({}^{Z}\qquad{}^{\tilde X}\)',
    'b04': r'et \\ (18) \(\mathcal E^T_{X/Y}\simeq\deleted{\operatorname{Ker}(\mathcal E^{\unsure{X_{\tilde Y}|\tilde X}}_{\unsure{X/Y|X_{\tilde Y}}}\longrightarrow\mathcal E^{\unsure{\tilde Y|Y}}_{\unsure{Y|\tilde Y}})}\inserted{\mathcal E^Z_{X_{\tilde Y}}\unsure{\simeq|\xrightarrow{\sim}}\mathcal E^{\tilde X}_{X_{\tilde Y}}}\)',
    'b05': r'\margin{\begin{tikzcd} X \arrow[d] & X_{\tilde Y} \arrow[l] \arrow[d] & \tilde X \arrow[l] & Z \arrow[l] \\ Y^{\prime} \arrow[d] & \tilde Y \arrow[l] & {} & {} \\ Y & {} & {} & {} \end{tikzcd}} \\ Une \\ \({}^{T}\)',
    'b06': r'Une autre interprétation de',
    'b07': r'en prenant \(T\) réduit',
    'b08': r'à un pt géométrique \inserted{\(\unsure{\xi|\zeta}_X\)}, qui définit',
    'b09': r'donc un pt géom. \(\unsure{\xi|\zeta}_Y\) de \(Y\),',
    'b10': r'une fibre géom. \(X_{\unsure{\xi|\zeta}_Y}\) de \(X\) sur \(Y\)',
    'b11': r"en \(\unsure{\xi|\zeta}_Y\), \(\unsure{\xi|\zeta}_X\) s'interprète comme un",
    'b12': r'pt géom. de ladite fibre, et on',
    'b13': r'aura \\ (1\unsure{9|4}) \(\mathcal E^{\unsure{\xi|\zeta}_X}_{X/Y}\simeq\mathcal E^{\unsure{\xi|\zeta}_X}_{X_{(\unsure{\xi|\zeta}_Y)}}\simeq\unsure{\Pi|\pi}_1(X_{(\unsure{\xi|\zeta}_Y)},\unsure{\xi|\zeta}_X)\)',
    'b14': r"--- i.e. \(\mathcal E_{X/Y}\) s'interprète comme groupe \\ fondamental des ``fibres \unsure{géom|géom.}'' de \(X/Y\).",
    'b15': r'\margin{111}',
}

notes = {
    'b01': {
        'ambiguities': ['The lower part of the first inserted T is heavily retraced. An X-like cross is visible within those strokes, but a distinct earlier letter or a subscript cannot be securely separated. The visible T cap and stem are retained without inventing an earlier state.'],
        'clipped_context': ['The lower edge includes only the tips of mathematical accents from the following formula; those incomplete neighbors are not supplied.'],
        'layout': 'The morphisms T to X and T to Y with et de and the following comma are interlinear above de telle façon. Their insertion layer is retained separately from the main sentence.',
        'short_forms_preserved': ['rev.']
    },
    'b02': {
        'ambiguities': ['A small isolated dot stands just left of the first superscript T. It may be a substantive dot or incidental ink; T and dot-T are retained as alternatives.'],
        'clipped_context': ['Descenders of the preceding prose enter at the upper edge. They are not completed.'],
        'symbols': 'The two comparison signs have a wavy upper stroke and one straight lower stroke. Both superscript accents over X and Y in the kernel expression are tildes.',
        'classification': '(17) is a formula label.'
    },
    'b03': {
        'ambiguities': [],
        'clipped_context': ['The lower edge cuts the bases of two mathematical terms from the following line. The complete visible superscripts Z and tilde-X are transcribed alone, using empty bases; no missing base or subscript is completed.'],
        'short_forms_preserved': ['hyp']
    },
    'b04': {
        'ambiguities': [
            'The cancelled kernel expression is crossed repeatedly. Ker, its opening parenthesis, two E-shaped terms, the rightward arrow and the final closing parenthesis remain distinguishable.',
            'The superscript of its first cancelled E may read X_sub_tildeY or tilde-X; the base subscript may read X/Y or X_sub_tildeY.',
            'The superscript and subscript of its second cancelled E are uncertain between the visible Y and tilde-Y forms.',
            'The heavily retraced comparison sign between the two upper replacement terms may be simeq or a rightward arrow with a tilde above it.'
        ],
        'clipped_context': ['Fragments of the preceding parenthetical prose enter at the top edge and are not completed.'],
        'correction_layers': {
            'main_line': 'Formula (18), E^T_(X/Y), a comparison sign, and a kernel expression.',
            'cancellation': 'The kernel expression is crossed with multiple diagonal strokes. The visible but uncertain mathematical letters are represented with unsure, never with an illegible-word placeholder.',
            'interlinear_replacement': 'Above the cancelled material are E^Z_(X_sub_tildeY), a retraced comparison sign, and E^tildeX_(X_sub_tildeY).'
        },
        'classification': '(18) is a formula label.'
    },
    'b05': {
        'ambiguities': [],
        'clipped_context': ['Une is a complete main-text neighbor to the right of the diagram and is included separately.', 'The following main-text word is clipped at the right edge and is not completed.', 'At the bottom, a neighboring E expression is cut through its base and subscripts. Only its wholly visible superscript T is transcribed as a fragment with an empty base.'],
        'diagram_objects': ['upper-left X', 'upper-second X_sub_tildeY', 'upper-third tilde-X', 'upper-right Z', 'middle-left Y-prime', 'middle-second tilde-Y', 'lower-left Y'],
        'diagram_edges': [
            {'from': 'upper-second X_sub_tildeY', 'to': 'upper-left X', 'direction': 'left'},
            {'from': 'upper-third tilde-X', 'to': 'upper-second X_sub_tildeY', 'direction': 'left'},
            {'from': 'upper-right Z', 'to': 'upper-third tilde-X', 'direction': 'left'},
            {'from': 'upper-left X', 'to': 'middle-left Y-prime', 'direction': 'down'},
            {'from': 'upper-second X_sub_tildeY', 'to': 'middle-second tilde-Y', 'direction': 'down'},
            {'from': 'middle-second tilde-Y', 'to': 'middle-left Y-prime', 'direction': 'left'},
            {'from': 'middle-left Y-prime', 'to': 'lower-left Y', 'direction': 'down'}
        ],
        'diagram_labels': [],
        'correction_layers': 'No separate cancelled diagram layer is visible.'
    },
    'b06': {'ambiguities': [], 'clipped_context': []},
    'b07': {
        'ambiguities': ['The middle of prenant is retraced, but no distinct cancelled word is recoverable.'],
        'clipped_context': ['Tiny tips of neighboring notation enter at the bottom edge; no missing characters are supplied.']
    },
    'b08': {
        'ambiguities': ['The inserted point-name has a curling head and a long descending stroke; xi is the leading reading, with zeta retained as an alphabet alternative. The subscript is X.'],
        'clipped_context': ['The head of the inserted point-name is close to the top edge.', 'A preceding E-expression at upper left is cut through its base and index context; it is not reconstructed from neighboring boxes.'],
        'layout': 'The point-name is inserted above the comma after géométrique, with a curved leader.',
        'short_forms_preserved': ['pt']
    },
    'b09': {
        'ambiguities': ['The point-name has the same xi/zeta ambiguity as the inserted point-name, here with subscript Y.', 'A small isolated ink dot occurs after un; it has no securely distinguishable punctuation function.'],
        'clipped_context': ['Only small lower-line tips enter at the bottom edge.'],
        'short_forms_preserved': ['pt', 'géom.']
    },
    'b10': {
        'ambiguities': ['The geometric-fiber subscript contains the xi/zeta point-name followed by subscript Y.'],
        'clipped_context': ['The upper extremities of the final X and Y touch or cross the top edge. Their visible strokes identify X and Y; no invisible accent is added.', 'The long lower stroke of fibre touches the bottom edge.', 'A faint pencil-like loop near the end of géom. is not a complete separable word or numeral.'],
        'short_forms_preserved': ['géom.']
    },
    'b11': {
        'ambiguities': ['Both point-names retain the xi/zeta alphabet alternative; their subscripts are respectively Y and X.'],
        'clipped_context': ['Upper portions of the next line enter along the bottom edge; those neighbors are not completed.']
    },
    'b12': {
        'ambiguities': ['The spacing within ladite is slightly open; it is read as the single written expression ladite.'],
        'clipped_context': ['The ascenders in fibre and et reach the top edge; their remaining strokes are readable.', 'A descender from the preceding line enters at the upper left.'],
        'short_forms_preserved': ['pt', 'géom.']
    },
    'b13': {
        'ambiguities': [
            'The second digit of the formula label is looped and descending; 9 is the leading reading, with 4 retained as an alternative.',
            'The first superscript point-name is heavily retraced. No distinct earlier character can be recovered from beneath it.',
            'All point-names retain the xi/zeta alphabet alternative.',
            'The straight-legged pi-shaped symbol with subscript 1 is ambiguous between capital Pi and lowercase pi.'
        ],
        'clipped_context': [],
        'symbols': 'Parentheses surrounding the point-name in each geometric-fiber subscript are visible and are retained. Both comparison signs have a wavy upper stroke and a straight lower stroke.',
        'classification': 'The parenthesized number is a formula label, not an author page number.'
    },
    'b14': {
        'ambiguities': ['A separate abbreviation period after géom inside the quotation marks is not secure; both with-dot and without-dot readings are retained.'],
        'clipped_context': ['The long lower stroke of fondamental reaches the bottom edge; no following word is cut into the box.'],
        'short_forms_preserved': ['i.e.', 'géom'],
        'symbols': 'The passage begins with a dash. The final X/Y is followed by a period.'
    },
    'b15': {'ambiguities': [], 'clipped_context': [], 'classification': 'Thin foliation 111.'},
}

assert set(readings) == {row['box'] for row in boxes}
tsv = outdir / '149_scan112_second.tsv'
with tsv.open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in boxes:
        writer.writerow([row['box'], readings[row['box']]])

inspections = []
for row in boxes:
    crop = root / f"edition/crops/149_scan112_second_{row['box']}.png"
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
    'page': '149_scan112',
    'source_image': str(root / 'source/SP88_C13_149_scans/149_scan112.jpg'),
    'box_list': str(outdir / '149_scan112_boxes.tsv'),
    'protocol': str(outdir / 'READING_PROTOCOL.md'),
    'reading_method': 'Independent image-only visual reading. No OCR, witnesses, first readings, candidate text, notation table, notes, comparison/adjudication files, external research or TeX compilation was used.',
    'source_page_visual_inspection': True,
    'source_page_use': 'The same authorized full page was viewed once to distinguish interlinear additions, marginal diagram positions and main text. Clipped neighbors were not completed from the wider view.',
    'crop_making_script': str(outdir / 'make_149_scan112_second_blind_a2.py'),
    'inspection_count': len(inspections),
    'inspections': inspections,
    'additional_visual_inspections': [
        {'box': 'b01', 'crop_file': str(root / 'edition/crops/149_scan112_second_b01.png'), 'rotation_degrees': 0, 'successful_visual_inspection': True, 'repeat_view': True}
    ],
    'status': 'Complete independent reading; frozen upon completion report.'
}
obs = outdir / '149_scan112_second_observations.json'
with obs.open('w', encoding='utf-8') as handle:
    json.dump(observations, handle, ensure_ascii=False, indent=2)
    handle.write('\n')

print(json.dumps({
    'page': '149_scan112',
    'rows': len(boxes),
    'inspected_boxes': len(inspections),
    'files': [{'name': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in (tsv, obs)],
}, ensure_ascii=False))
