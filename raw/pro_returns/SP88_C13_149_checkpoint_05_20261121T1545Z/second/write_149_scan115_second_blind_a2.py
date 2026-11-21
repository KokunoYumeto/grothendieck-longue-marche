from pathlib import Path
import csv
import hashlib
import json
from PIL import Image

root = Path('/workspace/scratch/0cab6a548abb')
outdir = root / 'edition/second'
with (outdir / '149_scan115_boxes.tsv').open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))

readings = {
    'b01': r'\mspage{57}',
    'b02': r'\(\operatorname{Gal}(\bar K/K)\) de \deleted{\(\unsure{\mathcal E_Y}\)} \(\bar K/K\),',
    'b03': r'\(\operatorname{Spec}\bar K\simeq\tilde Y\).',
    'b04': r'\(\Gamma\), \inserted{ou \(\Gamma_K,\Gamma^{\bar K}_K,\)} en lieu de \(\mathcal E_Y\) --- surtout',
    'b05': r"et qu'il n'a donc plus de ``partie",
    'b06': r"géométrique'' à distinguer d'une",
    'b07': r"``partie arithmétique''\ldots",
    'b08': r'Soit \(K\) \deleted{\unsure{tel}} \inserted{un} corps',
    'b09': r'type fini de \(K\), \(X\) un ``\unsure{modèle|modele}\textquotesingle\textquotesingle',
    'b10': r'qui \uline{ne \deleted{p} dépend pas du modèle} \\ \uline{\(X\) choisi}, comme il est bien connu',
    'b11': r'\margin{114}',
}
readings['b09'] = readings['b09'].replace(r'\textquotesingle\textquotesingle', "''")

notes = {
    'b01': {'ambiguities': [], 'clipped_context': [], 'classification': 'Dark author page number 57.'},
    'b02': {
        'ambiguities': ['The cancelled term has an E-like cursive body with a lower Y-like letter. E_sub_Y is only a tentative reading; the repeated oblique strokes prevent a secure reconstruction of its original mathematical letters. No illegible-word placeholder is used for this mathematical term.'],
        'clipped_context': ['A long descender from the preceding line enters above the cancellation; it is not treated as a newly supplied overbar.'],
        'correction_layers': 'A compact mathematical term after de is repeatedly crossed out; the following bar-K/K remains uncancelled.',
        'symbols': 'Both surviving field expressions contain an overbar on K, a slash, and a second K. The line ends with a comma.'
    },
    'b03': {
        'ambiguities': ['The accent over K is slightly curved but is read as an overbar; the distinct wavy accent over Y is retained as a tilde.'],
        'clipped_context': ['Only the caps of neighboring Gamma-shaped notation from the following line enter at the bottom edge. The missing vertical strokes and labels are not completed.'],
        'symbols': 'The comparison sign has a wavy upper stroke and one straight lower stroke (simeq). A period follows tilde-Y.'
    },
    'b04': {
        'ambiguities': ['The lower part of the E-shaped symbol is heavily retraced; no distinct earlier letter is securely separable.'],
        'clipped_context': ['The upper edge contains only remnants of the preceding line, which are not completed.'],
        'layout': 'The alternate Gamma notations are interlinear above en lieu de. A long curved leader runs beneath the addition toward the main Gamma. The leader is retained as insertion structure, not read as an extra textual parenthesis.',
        'symbols': 'The main and added symbols have a horizontal cap joined to a left vertical stroke (Gamma). The second added Gamma has lower K and upper bar-K. Both added Gamma terms are followed by visible commas.'
    },
    'b05': {
        'ambiguities': [],
        'clipped_context': ['The lower extremity of the q-descender reaches the bottom edge. Only tips of the following line enter below; they are not completed.'],
        'quotation': 'Opening double quotation marks precede partie; the closing marks occur outside this box and are not supplied.'
    },
    'b06': {
        'ambiguities': [],
        'clipped_context': ['A descender from the preceding line enters at upper left; upper strokes from the following line enter at the bottom. No neighboring words are completed.'],
        'quotation': 'Two closing quotation marks follow géométrique; no opening marks are invented in this box.'
    },
    'b07': {
        'ambiguities': [],
        'clipped_context': ['Two preceding-line descenders enter at the top edge.'],
        'quotation': 'Opening and closing double quotation marks are present. Three separate dots follow the closing marks.',
        'nontextual': 'A faint horizontal paper crease crosses the area; it is not interpreted as underlining.'
    },
    'b08': {
        'ambiguities': ['The deleted short word is tentatively tel; its interior strokes are partly hidden by cancellation.', 'The inserted un is physically above the end of Soit, with a curved leader descending in that vicinity. Its precise linear attachment is not secured by the leader. The reading places it at the cancelled-word slot before corps, while its visible location is explicitly recorded here.'],
        'clipped_context': ['A faint small pencil-like trace reaches the lower edge; it does not provide a complete word or numeral.'],
        'correction_layers': 'Main line Soit K [cancelled short word] corps. A separate un is added above the left part of the line.'
    },
    'b09': {
        'ambiguities': ['The grave accent in modèle is not securely distinguishable in this crop; the accented and unaccented spellings are retained as alternatives.'],
        'clipped_context': ['The high ascender in the quoted word touches the top edge.', 'Only upper portions of the next line enter along the bottom; they are not completed.'],
        'quotation': 'Both sets of double quotation marks enclosing the last word are visible.'
    },
    'b10': {
        'ambiguities': ['The exact beginning of the long underline lies near the end of qui. The encoding leaves qui outside the underline and records its physical beginning here.'],
        'clipped_context': ['A small tail from the preceding line enters at the upper edge.'],
        'cancellation': 'A standalone p-shaped false start between ne and dépend is crossed out; no following letters of that false start are visible.',
        'underlining': 'A single long line passes beneath the first-line clause from near the end of qui through modèle. A second line lies beneath X choisi on the following line. These are underlines rather than cancellation of the clause.',
        'punctuation': 'A comma follows choisi. No terminal punctuation after connu is visible in the box.'
    },
    'b11': {'ambiguities': [], 'clipped_context': [], 'classification': 'Thin foliation 114.'},
}

assert set(readings) == {row['box'] for row in boxes}
tsv = outdir / '149_scan115_second.tsv'
with tsv.open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in boxes:
        writer.writerow([row['box'], readings[row['box']]])

inspections = []
for row in boxes:
    crop = root / f"edition/crops/149_scan115_second_{row['box']}.png"
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
    'page': '149_scan115',
    'source_image': str(root / 'source/SP88_C13_149_scans/149_scan115.jpg'),
    'box_list': str(outdir / '149_scan115_boxes.tsv'),
    'protocol': str(outdir / 'READING_PROTOCOL.md'),
    'reading_method': 'Independent image-only visual reading. No OCR, witnesses, first readings, candidate text, notation, notes, comparison/adjudication files, external research or TeX compilation was used.',
    'source_page_visual_inspection': True,
    'source_page_use': 'The authorized full page was viewed once to distinguish interlinear addition placement, preceding-line descenders and underlining. Clipped neighbors were not completed from that view.',
    'crop_making_script': str(outdir / 'make_149_scan115_second_blind_a2.py'),
    'inspection_count': len(inspections),
    'inspections': inspections,
    'additional_visual_inspections': [
        {'box': 'b02', 'crop_file': str(root / 'edition/crops/149_scan115_second_b02.png'), 'rotation_degrees': 0, 'successful_visual_inspection': True, 'repeat_view': True}
    ],
    'status': 'Complete independent reading; frozen upon completion report.'
}
obs = outdir / '149_scan115_second_observations.json'
with obs.open('w', encoding='utf-8') as handle:
    json.dump(observations, handle, ensure_ascii=False, indent=2)
    handle.write('\n')

print(json.dumps({
    'page': '149_scan115',
    'rows': len(boxes),
    'inspected_boxes': len(inspections),
    'files': [{'name': path.name, 'sha256': hashlib.sha256(path.read_bytes()).hexdigest()} for path in (tsv, obs)],
}, ensure_ascii=False))
