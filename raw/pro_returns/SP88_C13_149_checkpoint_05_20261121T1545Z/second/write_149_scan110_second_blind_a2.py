from pathlib import Path
import csv
import json
from PIL import Image

root = Path('/workspace/scratch/0cab6a548abb')
outdir = root / 'edition/second'
with (outdir / '149_scan110_boxes.tsv').open(encoding='utf-8', newline='') as handle:
    boxes = list(csv.DictReader(handle, delimiter='\t'))

readings = {
    'b01': r"\uline{et} d'un relèvement en \(T\longrightarrow X\), ou ce \\ qui revient au \(=\), d'une section \\ de \(X_T=X\times_Y T\) sur \(T\). Ceci posé,",
    'b02': r"on aura une \unsure{iden|idée} \\ \unsure{can|car} (avec l'\unsure{hyp-|hyp.} \\ de ``suite exacte d'homo- \\ topie'' \deleted{)} fort)",
    'b03': r'\begin{tikzcd} X \arrow[d] & X_T \arrow[l] \arrow[d] & {} \\ Y & T \arrow[l] & T \arrow[l, equal] \arrow[ul] \end{tikzcd}',
    'b04': r'(12) \(\mathcal{E}^{T}_{X/Y}\simeq\unsure{\Pi|\pi}_1(X_T;T)\simeq\mathcal{E}^{T}_{X_T}\)',
    'b05': r'et on aura',
    'b06': r'(13) \(1\longrightarrow\mathcal{E}^{T}_{X/Y}\longrightarrow\mathcal{E}^{T}_{X}\longrightarrow\mathcal{E}^{T}_{Y}\longrightarrow1\)',
    'b07': r'(Cette hypothèse sera tjrs satisfaite \\ si \(Y=\operatorname{Spec}K\), \(K\) un corps, \\ si \(X\) est géom. \(\unsure{0}\)-connexe sur \(K\))',
    'b08': r"Plus généralement, si on a une \\ suite exacte d'homotopie universelle, \\ mais pas néc. avec \(\mathcal{E}^{T}_{X}\longrightarrow\mathcal{E}^{T}_{Y}\) surj,",
    'b09': r'\margin{109}',
}

notes = {
    'b01': {
        'ambiguities': ['The two horizontal strokes after au are transcribed literally as an equals sign rather than expanded to a word.'],
        'clipped_context': ['The lower tip of the Y subscript in the product reaches the bottom edge. The two arms and stem are identifiable; no neighboring material is completed.'],
        'layout': 'Three manuscript lines; et has one underline. Each T has its ordinary capital crossbar, with no independently visible overbar.'
    },
    'b02': {
        'ambiguities': ['The shortened final word of the first line resembles iden; idée is retained as an alternative. It has not been expanded to identification.', 'The first word of the second line is uncertain between can and car. No abbreviation has been expanded.', 'The abbreviated hyp has a final short horizontal mark, uncertain between a hyphen and a period.', 'The opening parenthesis before avec is retraced and has a dark vertical smear immediately to its left; no separate underletter can be securely recovered.'],
        'clipped_context': [],
        'cancellation': 'A closing-parenthesis-shaped mark immediately after the closing quotation marks of topie is crossed through. The following fort and final closing parenthesis remain legible.',
        'layout': 'Four manuscript lines. The actual line division within d\u2019homo-/topie is retained.'
    },
    'b03': {
        'ambiguities': ['The diagonal has a clear upper-left arrowhead. Its lower-right tail has a short bent stroke that could be mistaken for a second head. The transcription reads the clear arrow as pointing from the right-hand T to X_T and records the tail uncertainty here.'],
        'clipped_context': [],
        'diagram_objects': ['upper-left X', 'upper-middle X_T', 'lower-left Y', 'lower-middle T', 'lower-right T'],
        'diagram_edges': [
            {'from': 'upper-middle X_T', 'to': 'upper-left X', 'kind': 'leftward arrow'},
            {'from': 'upper-left X', 'to': 'lower-left Y', 'kind': 'downward arrow'},
            {'from': 'upper-middle X_T', 'to': 'lower-middle T', 'kind': 'downward arrow'},
            {'from': 'lower-middle T', 'to': 'lower-left Y', 'kind': 'leftward arrow'},
            {'from': 'lower-right T', 'to': 'lower-middle T', 'kind': 'equals sign; no arrowhead'},
            {'from': 'lower-right T', 'to': 'upper-middle X_T', 'kind': 'diagonal upper-left arrow; lower-tail hook uncertain'}
        ],
        'diagram_labels': [],
        'correction_layers': 'No separate legible cancellation or replacement layer is visible.'
    },
    'b04': {
        'ambiguities': ['The pi-shaped symbol before subscript 1 has two straight legs and a long cap; capital Pi and lowercase pi remain alternatives.'],
        'clipped_context': [],
        'symbols': 'Both comparison signs consist of a tilde above a single straight bar (simeq). The separator inside parentheses has both an upper dot and a lower descending mark (semicolon).',
        'classification': '(12) is a formula label and is retained literally.'
    },
    'b05': {'ambiguities': [], 'clipped_context': []},
    'b06': {
        'ambiguities': [],
        'clipped_context': ['A very faint pencil-like loop/number remnant touches the top edge between the first and second E symbols; it is not complete enough to transcribe as a separate number.'],
        'correction_layers': 'The last superscript T is heavily retraced. No distinct earlier letter is recoverable.',
        'classification': '(13) is a formula label and is retained literally.',
        'symbols': 'The sequence begins and ends in digit 1. All four arrows point to the right.'
    },
    'b07': {
        'ambiguities': ['The small numeral before -connexe is heavily looped/retraced and is tentatively read 0. No distinct underlying numeral can be recovered.'],
        'clipped_context': ['The bottom of the initial si on the third line reaches the crop edge; the visible letters remain recognizable.'],
        'short_forms_preserved': ['tjrs', 'géom.'],
        'layout': 'The paragraph is enclosed by an opening parenthesis on its first line and a closing parenthesis at the end of its third line.'
    },
    'b08': {
        'ambiguities': [],
        'clipped_context': ['Only tiny traces of the following line enter the extreme lower edge; no letters are completed.'],
        'short_forms_preserved': ['néc.', 'surj'],
        'symbols': 'The arrow between E_X^T and E_Y^T points to the right. The final visible punctuation is a comma.'
    },
    'b09': {'ambiguities': [], 'clipped_context': [], 'classification': 'Thin foliation 109.'},
}

assert set(readings) == {row['box'] for row in boxes}
with (outdir / '149_scan110_second.tsv').open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in boxes:
        writer.writerow([row['box'], readings[row['box']]])

inspections = []
for row in boxes:
    crop = root / f"edition/crops/149_scan110_second_{row['box']}.png"
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
        'processing': 'Pillow crop at the listed original coordinates; autocontrast; LANCZOS enlargement.',
        **notes[row['box']],
    })

observations = {
    'reader_identity': '/root/blind_a2',
    'page': '149_scan110',
    'source_image': str(root / 'source/SP88_C13_149_scans/149_scan110.jpg'),
    'box_list': str(outdir / '149_scan110_boxes.tsv'),
    'protocol': str(outdir / 'READING_PROTOCOL.md'),
    'reading_method': 'Independent image-only visual reading. No OCR, first-reading TSV, witnesses, page TeX, notes, notation table, review metadata, comparison/adjudication output, external research, or TeX compilation was used.',
    'source_page_visual_inspection': True,
    'source_page_use': 'The authorized full page was viewed once to establish line and diagram layout. Clipped neighboring text was not completed from that view.',
    'crop_making_script': str(outdir / 'make_149_scan110_second_blind_a2.py'),
    'inspection_count': len(inspections),
    'inspections': inspections,
    'additional_visual_inspections': [
        {'box': box, 'crop_file': str(root / f'edition/crops/149_scan110_second_{box}.png'), 'rotation_degrees': 0, 'successful_visual_inspection': True, 'repeat_view': True}
        for box in ('b02', 'b01', 'b07')
    ],
    'status': 'Complete independent reading; frozen upon completion report.'
}
with (outdir / '149_scan110_second_observations.json').open('w', encoding='utf-8') as handle:
    json.dump(observations, handle, ensure_ascii=False, indent=2)
    handle.write('\n')

print(json.dumps({'page': '149_scan110', 'rows': len(boxes), 'inspected_boxes': len(inspections), 'files_written': 2}, ensure_ascii=False))
