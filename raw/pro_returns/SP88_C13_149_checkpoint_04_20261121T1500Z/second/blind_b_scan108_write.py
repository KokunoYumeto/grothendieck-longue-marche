from pathlib import Path
import csv
import json
import hashlib

ROOT = Path('/workspace/scratch/0cab6a548abb')
PAGE = '149_scan108'
SECOND = ROOT / 'edition' / 'second'

readings = {
    'b01': r'(8) \(\unsure{\mathcal{E}|\mathcal{G}}_X^{\unsure{\xi|\zeta}} \longrightarrow \unsure{\mathcal{E}|\mathcal{G}}_{\deleted{X}\inserted{Y}}^{\eta}\)',
    'b02': r'si on a un hom de schémas ``géom\({}^{\unsure{t}}\).',
    'b03': r"pointés'' \((X,\unsure{\xi|\zeta})\longrightarrow(Y,\eta)\). On",
    'b04': r'\unsure{notera|note} que la ponctuation géom.',
    'b05': r'ext. \unsure{sep|sép} dans \(\Omega\) de \(k(x)\) ---',
    'b06': r'\unsure{définit|definit} \inserted{can\({}^{\unsure{t}}\)} une',
    'b07': r'ponctuation \inserted{géom} complète',
    'b08': r'\(y=f(x)\)\unsure{;|, .} \deleted{par} par composition',
    'b09': r"--- \(\Omega\) ``est'' une",
    'b10': r"\(\underset{\inserted{\substack{\uparrow\\\unsure{\Omega|\alpha}}}}{k(x)}\hookleftarrow k(y)\) --- \unsure{d'où} l'hom (8)",
    'b11': r'(9) \(\unsure{\mathcal{E}|\mathcal{G}}_X^{\overline{k(x)}} \longrightarrow \unsure{\mathcal{E}|\mathcal{G}}_Y^{\overline{k(y)}}\),',
    'b12': r'On posera \\ (10) \(\unsure{\mathcal{E}|\mathcal{G}}_{X/Y}^{\widetilde{X}}=\operatorname{Ker}\bigl(\unsure{\mathcal{E}|\mathcal{G}}_X^{\widetilde{X}}\longrightarrow\unsure{\mathcal{E}|\mathcal{G}}_Y^{\widetilde{X}}=\unsure{\mathcal{E}|\mathcal{G}}_Y^{\widetilde{Y}}\bigr)\)',
    'b13': r'\margin{107}',
}

notes = {
    'b01': {
        'ambiguities': ['Script mathematical letter is retained as E/G.', 'The tall sinuous left superscript is xi/zeta.'],
        'clipped_material': [],
        'inspection_count': 2,
        'layers': 'The right subscript has a lighter X beneath darker Y-shaped strokes. The transcription records the cancelled X and overwritten Y separately. The map points right.',
    },
    'b02': {
        'ambiguities': ['The final abbreviation reads géom followed by a raised t-like letter and a baseline period; the raised letter remains uncertain.'],
        'clipped_material': ['Only the opening double quote is in this box; no closing quotation mark is supplied.'],
        'inspection_count': 2,
    },
    'b03': {
        'ambiguities': ['The mathematical letter following X remains xi/zeta.'],
        'clipped_material': [],
        'inspection_count': 1,
    },
    'b04': {
        'ambiguities': ['The compressed opening word is read notera/note; a final dotlike stroke may be the a of notera.', 'The long middle word is read ponctuation, with both tall t strokes retained.'],
        'clipped_material': ['The descender of que reaches the lower edge; no neighbouring text is supplied.'],
        'inspection_count': 2,
    },
    'b05': {
        'ambiguities': ['A separate accent over the e of sep is not securely distinguished; sep/sép is retained.', 'The field-letter glyph is read as Latin k with an ascender.'],
        'clipped_material': ['The p descender of sep reaches the lower edge.', 'A small partial stroke from the following line enters at the bottom and is not completed.'],
        'inspection_count': 1,
    },
    'b06': {
        'ambiguities': ['The accent in définit is not separately secure against the neighbouring f stroke.', 'The inserted abbreviation is can with a raised t-like letter; its top is clipped, so the letter is marked uncertain.'],
        'clipped_material': ['The top of the inserted raised letter meets the upper boundary.', 'A descender remnant from the preceding line enters at the top.'],
        'inspection_count': 2,
        'layers': 'The can abbreviation sits above the gap between définit and une, connected to the gap by a long rising insertion leader. Its terminal hook is treated as part of that leader, not as punctuation.',
    },
    'b07': {
        'ambiguities': [],
        'clipped_material': [],
        'inspection_count': 2,
        'layers': 'The abbreviation géom is inserted above the gap between ponctuation and complète, with a long curved insertion leader beneath it. No separate period after géom is visible.',
    },
    'b08': {
        'ambiguities': ['Following f(x), a comma-shaped lower stroke and a separately positioned dot can be read as a displaced semicolon or comma plus dot. Both are represented in the uncertainty marker.'],
        'clipped_material': ['A small fragment enters at the lower edge beneath the gap after the second par and is not completed.'],
        'inspection_count': 1,
        'layers': 'The first par has a horizontal cancellation stroke; a second, uncancelled par follows before composition.',
    },
    'b09': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
    'b10': {
        'ambiguities': ['Below the x of k(x) is a small Omega/alpha-shaped addition with a long upward stroke; its letter and precise editorial attachment remain uncertain.', 'The lightly written word after the dash is tentatively read d’où.'],
        'clipped_material': [],
        'inspection_count': 2,
        'layers': 'The main field expression reads k(x) hook-leftarrow k(y). The lower addition is preserved beneath k(x), with its upward pointer, rather than merged silently into the x. The map arrow points left and has a hooked right end.',
    },
    'b11': {
        'ambiguities': ['The script letters remain E/G alternatives.'],
        'clipped_material': ['Fragments of a preceding prose line enter the upper edge; no complete neighbouring word is inferred.', 'The right overline approaches the top edge; the underlying k(y) is complete.'],
        'inspection_count': 1,
    },
    'b12': {
        'ambiguities': ['All four script mathematical letters remain E/G alternatives.'],
        'clipped_material': ['A tiny fragment enters at the lower edge beneath the formula and is not completed.'],
        'inspection_count': 1,
    },
    'b13': {'ambiguities': [], 'clipped_material': [], 'inspection_count': 1},
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
    'method': 'Independent image-only diplomatic reading of the supplied boxes. No OCR, text recognition, PDF text layer, external research, TeX compilation, witnesses, first readings, other page images, or comparison output consulted for this page.',
    'task_inputs': [
        str(ROOT / 'source' / 'SP88_C13_149_scans' / f'{PAGE}.jpg'),
        str(SECOND / f'{PAGE}_boxes.tsv'),
        str(SECOND / 'READING_PROTOCOL.md'),
    ],
    'protocol': 'Previously read neutral READING_PROTOCOL.md retained; no other-page comparison or adjudication accessed.',
    'crop_making_script': str(SECOND / 'blind_b_scan108_crop.py'),
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
assert len(check) == 13
assert all(set(r) == {'box', 'reading'} and r['reading'] for r in check)
assert [r['box'] for r in check] == [r['box'] for r in boxes]
assert json.loads(obs.read_text(encoding='utf-8'))['successful_visual_inspection_count'] == 13
print(f'Completed {len(check)} TSV readings, {len(inspections)} successful box inspections, {observations["total_visual_display_count"]} image displays.')
print(f'TSV SHA256: {observations["transcription_sha256"]}')
print(f'Observations SHA256: {hashlib.sha256(obs.read_bytes()).hexdigest()}')
