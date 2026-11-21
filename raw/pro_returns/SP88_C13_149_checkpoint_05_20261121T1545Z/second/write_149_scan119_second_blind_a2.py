from pathlib import Path
import csv
import hashlib
import json
from PIL import Image

root = Path('/workspace/scratch/0cab6a548abb')
page = '149_scan119'
boxfile = root / 'edition/second/149_scan119_boxes.tsv'
cropdir = root / 'edition/crops'
outdir = root / 'edition/second'

readings = {
    'b01': r'''\mspage{57} celui d'un rev. universel (\deleted{\unsure{p.ex.|resp.}}\inserted{ou encore,} d'un $p^t$ géom $\unsure{\beta|\bar{\eta}}$ de $\tilde K_x$ -- i.e. d'une clôture algébrique de $\tilde K_x$ -- \uline{et} \unsure{d'un|d'une} \deleted{isom} ``\unsure{choix} de \unsure{chemins|domaines}'' entre $\xi_{\unsure{\tilde u_x|\tilde U_x}\to\tilde K_x\to\operatorname{Spec}(L)}$ et $\xi_L$ défini par $\tilde L$ -- ce qui revient au $\unsure{\simeq|=}$\inserted{à isom près des \unsure{deux} $\unsure{\bar E_s|\bar\xi_s}$}, d'un $K$-hom de \deleted{$\unsure{K_x}\,\unsure{K_x}$} $\tilde L_x$ ds $\bar L$ -- et ceci à son tour équivaut à la donnée d'un $x'$, \deleted{\uline{et} d'un is} comme dessus. Ceci posé, on a des isom can.''',
    'b02': r'''30) $\left\{\begin{aligned}N_{x'}&\simeq\mathcal E^{\bar L}_{\unsure{\tilde u_x|\tilde U_x}}\\I_{x'}&\simeq\text{Noyau de l'hom canoniq}\end{aligned}\right.$ \inserted{\uline{surjectif}} $\mathcal E^{\bar L}_{\unsure{\tilde u_x|\tilde U_x}}\longrightarrow\mathcal E_{\overline{k(x)}}$ (si la clôture alg. $\overline{\unsure{k|K}(x)}$ de $k(x)$ est induite par la clôture alg. $\bar L$ de $\tilde K_x$) \margin{Cf théorie galoisienne des traits henséliens ici $I_{x'}$ joue le rôle d'un $\pi^{\bar L}_{\unsure{\tilde U_x|\tilde u_x}/k(x)}$ ; en fait $I_{x'}=\pi^{\bar L}_{\unsure{\tilde U_x|\tilde u_x}/\tilde S_x}$ !} (dont (27) est déduit par théorie de Kummer), \deleted{$\unsure{\bar I_{x'}|I_{x'}}\simeq$} \deleted{(\unsure{24|31})} \margin{?} Je présume que (\unsure{dans|ds} la situation actuelle ou même, avec un corps de base $K$) on a $N_{x'}=\operatorname{Norm}_{\mathcal E_L}(I_{x'})$, \inserted{(\uline{a priori} on a \unsure{seulmt|seulement} $\unsure{\subset|\subseteq}$)} ce qui est lié à l'idée qu'on ait aussi $\unsure{I_{x'}|\bar I_{x'}}=\operatorname{Norm}_{\pi_{L/K}}(I_{x'}$ \margin{118}''',
    'b03': r'''\deleted{$\unsure{\bar I_{x'}|I_{x'}}\simeq$}''',
    'b04': r'''\deleted{(\unsure{24|31})}''',
}

notes = {
    'b01': {
        'ambiguities': [
            'The cancelled abbreviation after universel has a descender and is read provisionally p.ex.; resp. remains an alternative. The separate open parenthesis has been retained without supplying a closing parenthesis.',
            'The geometric-point symbol after geom consists of a separate short upper-left hook and a taller branching form. Beta and barred eta are offered; the short hook cannot securely be classified as an accent.',
            'The article before the cancelled isom may be d\'un or d\'une. The quoted phrase is provisionally choix de chemins; the last word also resembles domaines. These are ink-based alternatives, not normalized wording.',
            'The u/U case in the subscript of the first fibre-functor expression is uncertain. The following field letter reads K with a tilde and a subscript x; its dark vertical strokes have been retraced.',
            'The two horizontal strokes after revient au may be a similitude sign or an equals sign. The interlinear insertion is read a isom pres des deux followed by an overbarred E-like or xi-like symbol and an s-like suffix; the word deux and mathematical letter remain uncertain.',
            'Two cancelled K-like clusters precede tilde L_x. Both are represented provisionally as K_x, with separate uncertainty markers; cancellation strokes prevent secure recovery of their complete original forms.',
            'The final deletion clearly contains underlined et, d\'un, and a stopped is-like sequence. No expansion to isom has been supplied.'
        ],
        'correction_layers': [
            'ou encore, is inserted above the crossed abbreviation after universel, with a bent guide to the baseline.',
            'isom is crossed horizontally before the quoted phrase.',
            'et before the quoted phrase is underlined.',
            'The insertion a isom pres ... is written above the line beginning revient au ... d\'un K-hom, with a long curved guide below it. It is encoded as an insertion, not as a replacement of the surrounding baseline words.',
            'The K in K-hom and the K-like letters in the earlier field notation are heavily reinforced; no distinct hidden underletter has been invented.',
            'The K-like material before tilde L_x is cancelled by several diagonal strokes.',
            'A long diagonal cancellation crosses the phrase et d\'un is after x\'; its separate short underline beneath et is retained.'
        ],
        'clipped_context': [
            'The box begins with the complete continuation celui d\'un and ends with the complete line pose, on a des isom can.; no absent preceding text is supplied.',
            'The rightmost Spec(L) expression lies close to the page edge. Its visible closing curve is retained. No adjacent text beyond the rectangle has been consulted.',
            'The main open parenthesis after universel has no securely visible closing partner inside this box.'
        ],
        'layout': 'Author page number 57 is at the top. The main prose occupies ten lines with interlinear corrections; no diagram is present.'
    },
    'b02': {
        'ambiguities': [
            'The formula label is visibly 30) without a separate opening parenthesis. A very pale remnant immediately to its right cannot securely be classified as a letter, cancellation, or rubbed graphite; it is recorded here rather than assigned an invented token.',
            'The main indexed object has an E-shaped calligraphic letter, an upper barred L and a lower tilde u/U; the case of u/U is uncertain.',
            'The initial letter under the bar in the phrase cloture alg. ... de k(x) is tall enough to resemble K, although the following unbarred k(x) has a shorter k. Both k and K are retained as alternatives for the barred expression.',
            'The normalizer insertion is read a priori on a seulmt/seulement followed by an inclusion sign. The abbreviation and whether the inclusion sign has a separate lower bar remain uncertain.',
            'The introductory parenthesis of the last paragraph contains dans or the contraction ds; the ink does not securely distinguish the compressed middle letters.',
            'In the cancelled formula, the detached upper horizontal stroke may be an overbar on I or the upper serif of I. The same ambiguity is retained in the last displayed normalizer formula.',
            'The crossed formula number reads most like (24); the cancellation strokes permit (31) as an alternative. Both digits are explicitly uncertain rather than harmonized with the nearby numbering.'
        ],
        'correction_layers': [
            'surjectif is inserted above the terminal word canoniq and has a curved underline/guide below it.',
            'A separate crossed expression I_x-prime similitude occurs between the Kummer sentence and the last paragraph.',
            'The parenthesized formula number immediately above Je presume is crossed.',
            'The marginal question mark accompanies two long parallel vertical rules beside the final paragraph. These rules are recorded as layout rather than converted to horizontal underlining.',
            'The interlinear a priori ... inclusion note has a horizontal guide below a priori and a bent leader down to the comma after the normalizer equality.'
        ],
        'clipped_context': [
            'There are isolated partial strokes along the upper boundary from the preceding region. They do not form complete additional words and have not been completed.',
            'The terminal homomorphism adjective reaches the right page boundary. The visible sequence canoniq is transcribed; no final ue or terminal punctuation is supplied.',
            'The last formula extends into the right edge. An incomplete outer closing-parenthesis curve is visible beyond I_x-prime; the reading stops after the complete I_x-prime and does not supply the clipped closing delimiter.',
            'The diagonal marginal equality begins close to the left edge, but the visible I_x-prime is sufficiently contained to read. No preceding words have been inferred.'
        ],
        'layout': 'Two rows are grouped by a left brace; the next formula has one rightward arrow. The diagonal left-margin note was also inspected after a clockwise 26-degree rotation of a derivative from the canonical crop. Thin foliation 118 appears at lower left.'
    },
    'b03': {
        'ambiguities': [
            'The detached upper stroke above the crossed I-like letter may be an overbar or an upper serif. The lower suffix is x with a prime; the terminal sign has a wavy upper stroke and a horizontal lower stroke, read as similitude.'
        ],
        'correction_layers': ['The entire short formula is crossed by an oblique, wavering cancellation.'],
        'clipped_context': ['The box contains the short cancelled expression only; no surrounding prose has been completed.'],
        'layout': 'One cancelled mathematical expression, no diagram.'
    },
    'b04': {
        'ambiguities': [
            'The parenthesized cancelled digits most resemble 24. The superposed crossing strokes make 31 a possible alternative; the formula number has not been regularized from neighboring labels.'
        ],
        'correction_layers': ['Several oblique strokes cross the digits inside the visible parentheses.'],
        'clipped_context': ['Both parentheses are visible within the crop; no surrounding words occur.'],
        'layout': 'One cancelled parenthesized number.'
    },
}

with boxfile.open(encoding='utf-8', newline='') as handle:
    rows = list(csv.DictReader(handle, delimiter='\t'))
assert [row['box'] for row in rows] == list(readings)

tsv = outdir / f'{page}_second.tsv'
with tsv.open('w', encoding='utf-8', newline='') as handle:
    writer = csv.writer(handle, delimiter='\t', lineterminator='\n')
    writer.writerow(['box', 'reading'])
    for row in rows:
        writer.writerow([row['box'], readings[row['box']]])

view_specs = {
    'b01': [
        ('view1500', None, 0, 'whole canonical crop resized to width 1500'),
        ('panel1', [0, 0, 2758, 840], 0, 'overlapping panel resized to width 2000'),
        ('panel2', [0, 740, 2758, 1600], 0, 'overlapping panel resized to width 2000'),
        ('panel3', [0, 1480, 2758, 2286], 0, 'overlapping panel resized to width 2000'),
        ('topright_detail', [1700, 20, 2650, 300], 0, 'contrast factor 1.6'),
        ('line2_detail', [70, 265, 2380, 610], 0, 'contrast factor 1.6; width limited to 1800'),
        ('middle_detail', [0, 715, 2758, 1330], 0, 'contrast factor 1.6; width limited to 1800'),
        ('bottom_detail', [0, 1260, 2758, 2286], 0, 'contrast factor 1.6; width limited to 1800'),
        ('quotedwords_detail', [30, 720, 1700, 930], 0, 'contrast factor 1.6'),
        ('functor_detail', [1910, 690, 2758, 960], 0, 'contrast factor 1.6'),
        ('geomsymbol_detail', [490, 235, 830, 590], 0, 'contrast factor 1.6'),
        ('insertion_detail', [780, 1010, 2190, 1360], 0, 'contrast factor 1.6'),
        ('cancelledfield_detail', [0, 1410, 480, 1740], 0, 'contrast factor 1.6'),
        ('deletedwords_detail', [0, 1890, 1080, 2130], 0, 'contrast factor 1.6'),
    ],
    'b02': [
        ('view1500', None, 0, 'whole canonical crop resized to width 1500'),
        ('panel1', [0, 0, 3322, 860], 0, 'overlapping panel resized to width 2000'),
        ('panel2', [0, 780, 3322, 1640], 0, 'overlapping panel resized to width 2000'),
        ('panel3', [0, 1560, 3322, 2360], 0, 'overlapping panel resized to width 2000'),
        ('margin_rot26', [0, 120, 1310, 1470], -26, 'clockwise rotation with white fill; contrast factor 1.6; width 1350'),
        ('label_detail', [470, 100, 760, 370], 0, 'contrast factor 1.6'),
        ('surjectif_detail', [2790, 90, 3310, 380], 0, 'contrast factor 1.6'),
        ('closure_detail', [1810, 410, 3322, 1160], 0, 'contrast factor 1.6'),
        ('kummer_detail', [430, 1110, 3322, 1375], 0, 'contrast factor 1.6; width limited to 1800'),
        ('lower_detail', [0, 1410, 3322, 2360], 0, 'contrast factor 1.6; width limited to 1800'),
        ('lowerwords_detail', [470, 1410, 3322, 1850], 0, 'contrast factor 1.6; width limited to 1800'),
        ('lowerinsertion_detail', [1910, 1670, 3220, 1910], 0, 'contrast factor 1.6'),
        ('bottomformula_detail', [930, 1840, 3322, 2360], 0, 'contrast factor 1.6; width limited to 1800'),
        ('marginbottom_detail', [0, 850, 1100, 1440], 0, 'contrast factor 1.6'),
    ],
    'b03': [],
    'b04': [],
}

inspections = []
for row in rows:
    box = row['box']
    crop = cropdir / f'{page}_second_{box}.png'
    with Image.open(crop) as im:
        dimensions = list(im.size)
    views = []
    for suffix, bbox, rotation, processing in view_specs[box]:
        path = cropdir / f'{page}_second_{box}_{suffix}.png'
        with Image.open(path) as im:
            size = list(im.size)
        views.append({
            'file': str(path),
            'derived_from': str(crop),
            'bbox_in_canonical_crop_pixels': bbox,
            'rotation_degrees_counterclockwise': rotation,
            'dimensions': size,
            'processing': processing,
            'successful_visual_inspection': True,
        })
    inspections.append({
        'box': box,
        'crop_file': str(crop),
        'bbox_original_pixels': [int(row[key]) for key in ('x0', 'y0', 'x1', 'y1')],
        'rotation_degrees': 0,
        'crop_dimensions': dimensions,
        'processing': 'Pillow RGB crop at the exact supplied source bbox; autocontrast; LANCZOS enlargement by ' + ('3' if box in ('b03', 'b04') else '2'),
        'successful_visual_inspection': True,
        'inspection_mode': 'canonical image directly' if box in ('b03', 'b04') else 'entire canonical content through a whole-crop reduced view, overlapping panels, and image-only details',
        'derived_views_successfully_inspected': views,
        **notes[box],
    })

observations = {
    'reader_identity': '/root/blind_a2',
    'page': page,
    'source_image': str(root / 'source/SP88_C13_149_scans/149_scan119.jpg'),
    'box_list': str(boxfile),
    'protocol': str(outdir / 'READING_PROTOCOL.md'),
    'method': 'Independent image-only diplomatic reading. Only the assigned JPEG, its neutral box list, the neutral protocol, and image derivatives made from the canonical crops were used as reading inputs. No OCR, text recognition, external research, PDF text, first readings, witnesses, candidate text, notes, notation tables, review/comparison/adjudication files, or TeX compilation were accessed.',
    'crop_scripts': [
        str(outdir / 'make_149_scan119_second_blind_a2.py'),
        str(outdir / 'view_149_scan119_second_blind_a2.py'),
    ],
    'writer_script': str(outdir / 'write_149_scan119_second_blind_a2.py'),
    'source_crop_count': 4,
    'successfully_inspected_box_count': 4,
    'successful_image_view_count': 30,
    'failed_image_views': [{
        'file': str(cropdir / '149_scan119_second_b01.png'),
        'reason': 'The initial large-image tool response exceeded available model context and was truncated. This failed call is not counted as a successful inspection; the whole crop was subsequently inspected via the recorded reduced view and overlapping panels.'
    }],
    'inspections': inspections,
    'status': 'Complete; frozen on reporting. No comparison performed.',
}
jsonpath = outdir / f'{page}_second_observations.json'
jsonpath.write_text(json.dumps(observations, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')

with tsv.open(encoding='utf-8', newline='') as handle:
    written = list(csv.DictReader(handle, delimiter='\t'))
assert [row['box'] for row in written] == [row['box'] for row in rows]
assert all(set(row) == {'box', 'reading'} for row in written)
assert len(written) == 4
for output in (tsv, jsonpath):
    print(output.name, hashlib.sha256(output.read_bytes()).hexdigest())
print('rows=4; successfully_inspected_boxes=4; successful_image_views=30')
