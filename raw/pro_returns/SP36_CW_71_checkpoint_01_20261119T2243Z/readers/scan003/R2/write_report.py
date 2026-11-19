from pathlib import Path
from datetime import datetime, timezone
import json

ROOT = Path('/workspace/scratch/17347c1714f0/out/readers/scan003/R2')
PACKET = Path('/workspace/scratch/17347c1714f0/packets/scan003')
SOURCE = '/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/'
c_text = (PACKET / 'C.tex').read_text()
h_text = (PACKET / 'H.tex').read_text()
h_drawing = (PACKET / 'H_drawing_01-2.tex').read_text()
reading = (ROOT / 'reading.tex').read_text()
findings = []

def add(place, c, h, result, *, diff_c=False, diff_h=False, c_doubt=False,
        kind='other', marked=False, evidence='', crop=None, confidence='high',
        unresolved=False, consequential=False):
    findings.append({
        'id': f'R2-003-{len(findings)+1:02d}', 'place': place,
        'c': c, 'h': h, 'reading': result, 'diff_c': diff_c, 'diff_h': diff_h,
        'c_doubt': c_doubt, 's_id': None, 'kind': kind, 'marked_in_H': marked,
        'evidence': evidence,
        'crop': str(ROOT / crop) if crop else None,
        'confidence': confidence, 'unresolved': unresolved,
        'consequential': consequential,
    })

add('Upper middle block, first row, word after V_1',
    r'\unsure{borde|bordes}', r'\uncertain{bords}', 'borde',
    diff_c=True, diff_h=True, c_doubt=True, kind='misread word', marked=True,
    evidence='Half a: b-o-r-d-e is legible; the last turn belongs to e, with no distinct final s. The other two rows provide visible same-page letterforms.')
add('Upper middle block, second row, word after V_2',
    'borde', r'\uncertain{bords}', 'borde', diff_h=True, kind='misread word', marked=True,
    evidence='Half a: the final low loop and exit stroke read e. The word is live, not cancelled.')
add('Upper middle block, third row, word after V_3',
    'borde', r'\uncertain{bords}', 'borde', diff_h=True, kind='misread word', marked=True,
    evidence='Half a: the final letter is e, matching the two rows above; no final s is separately written.')
add('Upper right block, first row, accented word',
    r'\unsure{bordé}', 'bord', 'bordé', diff_c=True, diff_h=True, c_doubt=True,
    kind='misread word', evidence='Half a: the ending e and its separate short raised acute stroke are visible.')
add('Upper right block, first row, word after bordé',
    'par', r'\uncertain{pour}', 'par', diff_h=True, kind='misread word', marked=True,
    evidence='Half a: descending p, a, and short terminal r; there is no intervening ou sequence.')

add('Upper left table, cancelled overmark on Gamma double-prime 1',
    r'\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}\'\'_1',
    r'\Gamma\'\'_1', r'\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}\'\'_1',
    diff_h=True, c_doubt=True, kind='omission',
    evidence='Crop 01: a worked-over small rounded mark sits above the Gamma corner. Some internal light area remains, but the original circle versus point cannot be separated reliably from the cancelling ink. H has the live double-prime Gamma but no cancelled overmark.',
    crop='01_top_overmarks.png', confidence='low', unresolved=True)
add('Upper left table, cancelled overmark on Gamma double-prime 2',
    r'\overset{\deleted{\circ}}{\Gamma}\'\'_2', r'\Gamma\'\'_2',
    r'\overset{\deleted{\circ}}{\Gamma}\'\'_2', diff_h=True, kind='omission',
    evidence='Crop 01: a separate triangular mass with a leftward cancelling stroke is above the corner. It is the recurrent cancelled overmark; its original glyph uncertainty is marked at the first occurrence only.',
    crop='01_top_overmarks.png', confidence='medium', unresolved=True)
add('Upper left table, cancelled overmark on Gamma double-prime 3',
    r'\overset{\deleted{\circ}}{\Gamma}\'\'_3', r'\Gamma\'\'_3',
    r'\overset{\deleted{\circ}}{\Gamma}\'\'_3', diff_h=True, kind='omission',
    evidence='Crop 01: an incomplete rounded outline survives at the right of the dark cancellation. It supports circle as the leading interpretation of the recurrent top overmark. The two live primes remain distinct to the right.',
    crop='01_top_overmarks.png', confidence='medium')
add('Upper left table, first boundary sign in the bottom tier',
    r'\unsure{\partial|\delta}', r'\partial', r'\partial',
    diff_c=True, c_doubt=True, kind='misread symbol or index',
    evidence='Half a: a hooked upper stroke over a closed lower oval matches the boundary sign in the adjacent two columns and in the definition below. No extra delta reading is retained.')
add('Two-point set below the upper left table, first small letter',
    r'\unsure{x}', 'x', r'\unsure{x}', diff_h=True, c_doubt=True,
    kind='other', evidence='Crop 02: the small glyph has a short leftward entry and a heavily joined curved body; x remains the best candidate but distinct crossing strokes are not recoverable. The live glyph in the drawing has the same compact form. H leaves it unmarked.',
    crop='02_boundary_set.png', confidence='low', unresolved=True)
add('First union identity, initial subscript',
    r'\Gamma_1', r'\Gamma_1', r'\Gamma_1', c_doubt=True,
    kind='misread symbol or index',
    evidence='Crop 03 checks the earlier 2/1 question recorded in C_audit.md. The digit has an ascending entry, a near-vertical stem, and a broad two-sided foot: 1. The following clear 2 has a different hooked top and shorter rightward foot. The present C and H readings are supported.',
    crop='03_first_identity.png', consequential=True)
add('First union identity, subscript on the first single-prime Gamma',
    r'\Gamma\'_{\unsure{2|1}}', r'\Gamma\'_2', r'\Gamma\'_{\unsure{1|2}}',
    diff_c=True, diff_h=True, c_doubt=True, kind='misread symbol or index',
    evidence='Crop 03: the upper entry is pointed and the stem nearly upright, resembling 1; the low turn to the right also allows 2. I rank 1 first on stroke shape, without replacing it by the cyclically expected 2. The crop does not settle the digit.',
    crop='03_first_identity.png', confidence='low', unresolved=True, consequential=True)
add('First union identity, final double-prime pair',
    r'\Gamma\'\'_1\cup\Gamma\'\'_2\cup\partial',
    r'\Gamma\'\'_1 \cup \Gamma\'\'_2 \cup \partial',
    r'\Gamma\'\'_1\cup\Gamma\'\'_2\cup\partial',
    c_doubt=True, kind='misread symbol or index', marked=True,
    evidence='Crop 03: the first low digit is an angular 1 and the second has the curled 2 shape. The visible pair is 1,2. C flags this as a possible slip, and H notes uncertainty in these indices; neither mathematical expectation nor the neighbouring rows is used to change the ink.',
    crop='03_first_identity.png', consequential=True)
add('Second union identity, terminal boundary sign',
    r'\unsure{\dot\partial|\partial}', r'\partial', r'\partial',
    diff_c=True, c_doubt=True, kind='misread symbol or index',
    evidence='Crop 04: the detached dark cap lies where the upper hook of this boundary glyph begins; a very faint descending trace continues towards the lower stem. The lower part lacks a separate complete upper hook. I read a broken/faint stroke of partial rather than an additional dot accent.',
    crop='04_second_boundary.png', confidence='medium', consequential=True)

add('Drawing, right outer label after rotation clockwise',
    r'\Gamma\'_{\unsure{2}}', r'\Gamma\'_2', r'\Gamma\'_2',
    diff_c=True, c_doubt=True, kind='misread symbol or index',
    evidence='Crop 05: despite the oblique crossing line, the low digit has a rounded head, descending bend, and rightward base: 2. It does not require a doubt mark.',
    crop='05_drawing_rotated.png')
add('Drawing, live small glyph inside the upper loop',
    r'\unsure{x}', 'x', 'x', diff_c=True, c_doubt=True, kind='other',
    evidence='Crop 05: the same compact x-like glyph as in the set is visible above and left of the junction. Its identity remains uncertain, but the recurrent-glyph convention places the uncertainty marker at the first occurrence on the page only. H_drawing_01-2.tex actually includes x; it is not an omission.',
    crop='05_drawing_rotated.png', confidence='low', unresolved=True)
add('Drawing, cancelled/blotted small mark to the right of the junction',
    r'\deleted{\unsure{x|\partial}}', None, r'\deleted{\unsure{x|\partial}}',
    diff_h=True, c_doubt=True, kind='omission',
    evidence='Crop 05: a dense overworked mark with a short curved rightward extension lies within the loop. The original mark cannot be separated from its cancellation; x and partial remain ink-supported candidates. The H drawing comments explicitly say the blot is not drawn, and its TikZ body contains no such mark.',
    crop='05_drawing_rotated.png', confidence='low', unresolved=True)
add('Expression beside the drawing, cancelled raised sign on initial Gamma_3',
    r'\Gamma_3^{\deleted{\unsure{\circ|\'}}}', r'\Gamma^{*}_3',
    r'\Gamma_3^{\deleted{\circ}}', diff_c=True, diff_h=True, c_doubt=True,
    kind='deletion state (struck given live or live given struck)',
    evidence='Crop 06: a closed small ring with a light centre survives under a heavy vertical/crossing stroke. This is a cancelled circle. A mere prime does not account for the ring, and a live asterisk does not account for the closed centre plus overworking.',
    crop='06_beside_drawing.png', consequential=True)
add('Expression beside the drawing, subscript on second double-prime Gamma',
    r'\Gamma\'\'_{\unsure{2|1}}', r'\Gamma\'\'_2',
    r'\Gamma\'\'_{\unsure{2|1}}', diff_h=True, c_doubt=True,
    kind='misread symbol or index',
    evidence='Crop 06: a rounded top and a very broad thick base support 2, but overinking of the central stem leaves 1 possible. Both candidates are retained; the topology is not used to settle it.',
    crop='06_beside_drawing.png', confidence='low', unresolved=True, consequential=True)
add('Lower formula line, unfinished expression after the dotted-U identity',
    r'U_3\cup', r'U_3 \cup', r'U_3\cup', c_doubt=True,
    kind='other', evidence='Half a: the last cup is present and no following operand is written. C records this under slips retained; H also preserves the unfinished expression. Nothing is supplied.',
    consequential=False)
add('Final group, detached mark preceding U,C,V',
    r'\unsure{\cdot}', None, r'\unsure{\cdot}', diff_h=True, c_doubt=True,
    kind='omission',
    evidence='Crop 07: a small detached black mark with a faint short lower taper is present to the left of U, around its mid-height. It may be a dot or incidental pen mark. No alternative full symbol can be recovered. It is retained as an uncertain dot rather than discarded.',
    crop='07_final_mark.png', confidence='low', unresolved=True)

for row, pair in [(1, r'\Gamma\'_2,\Gamma\'_3'),
                  (2, r'\Gamma\'_3,\Gamma\'_1'),
                  (3, r'\Gamma\'_1,\Gamma\'_2')]:
    add(f'Upper blocks, row {row}, gap between the middle and right columns',
        '', ';', '', diff_h=True, kind='text not on the page',
        evidence=f'Half a: after {pair} there is an open inter-column gap, not a semicolon. H uses a semicolon when serializing the columns. The reading keeps the separate columns without adding punctuation.')
add('Below the drawing expression, gap between dotted-U identity and unfinished U_3 cup',
    r'\qquad', ';', r'\qquad', diff_h=True, kind='text not on the page',
    evidence='Half a: a wide blank interval follows Gamma_3; no semicolon is visible. H supplies one between its two inline mathematical groups.')
add('Placement of the boundary-set definition',
    '\\[\n\\partial=\\{\\unsure{x},y\\}\n\\]',
    r'\qquad \partial = \{x, y\}',
    '\\[\n\\partial=\\{\\unsure{x},y\\}\n\\]',
    diff_h=True, kind='insertion or placement',
    evidence='Whole page and half a: the definition is a separate line below the left table. H typesets it to the right of the left array. This finding concerns placement, not an omitted definition.')

c_fig = c_text[c_text.index(r'\figure{'):c_text.index(r'\end{minipage}')].strip()
r_fig = reading[reading.index(r'\figure{'):reading.index(r'\end{minipage}')].strip()
h_fig = h_drawing[h_drawing.index(r'\begin{tikzpicture}'):h_drawing.index(r'\end{tikzpicture}')+len(r'\end{tikzpicture}')]
add('Drawing as a whole: on-sheet orientation, curves, hatching, and retraced outline strokes',
    c_fig, h_fig, r_fig, diff_c=True, diff_h=True, kind='drawing or diagram',
    evidence='Crop 05: three curved paths join the same two junctions; a separate irregular loop surrounds the upper junction in the rotated view. Four long oblique strokes, their short returns, two dotted returns, and small retraced spurs on the outer boundary are reproduced. The new drawing is a best relative-position approximation. C is a broadly correct schematic with different geometry; H provides a real TikZ drawing, not merely missing image content, but turns it upright and deliberately omits the internal blot. The new figure preserves the quarter-turn on the sheet. The small spurs are not asserted to be arrowheads.',
    crop='05_drawing_rotated.png', confidence='medium')

crops = json.loads((ROOT / 'crop_log.json').read_text())
observed = {
    '01_top_overmarks.png': 'Three crossed/overworked upper marks are present. Circle is the best recurrent reading, with point still possible at the first; the live double primes and subscripts remain distinct.',
    '02_boundary_set.png': 'Partial and braces are clear. The compact first letter remains x-like but unresolved; y and the comma are clear.',
    '03_first_identity.png': 'Initial subscript is 1. First primed subscript remains 1/2, with 1 ranked first. The final double-prime pair is visibly 1,2 and is retained despite the possible mathematical slip.',
    '04_second_boundary.png': 'A detached dark cap and faint continuation align with a broken upper stroke of partial; no independent dot accent is retained.',
    '05_drawing_rotated.png': 'Outer labels resolve to Gamma prime 1 and Gamma prime 2, median label to Gamma prime 3. The live x-like glyph and the blotted mark remain uncertain. Four hatching strokes, two dotted returns, the small loop, endpoint y, and outline retraces are visible.',
    '06_beside_drawing.png': 'The cancelled raised sign contains a closed circle; the first double-prime subscript is 1 and the second remains 2/1.',
    '07_final_mark.png': 'Detached ink mark retained as uncertain dot. Its intentional punctuation status cannot be established.',
}
for crop in crops:
    crop['observed'] = observed[Path(crop['file']).name]

inventory = []
def inv(kind, position, words, hand='his hand'):
    inventory.append({'scan': 3, 'sheet_kind': 'text', 'hand': hand,
                      'element': f'003-{len(inventory)+1:02d}', 'kind': kind,
                      'position': position, 'first_words_or_objects': words,
                      'transcribed': 'yes'})
inv('diagram', 'upper left, three vertical columns and right separator', 'V_1 V_2 V_3; Gamma double-prime_i = Gamma prime_i - partial')
for i in (1, 2, 3):
    inv('deletion', f'upper left table, above Gamma double-prime_{i}', 'cancelled small circle/point overmark')
for i, pair in [(1, '2,3'), (2, '3,1'), (3, '1,2')]:
    inv('text', f'upper middle block, row {i}', f'V_{i} borde Gamma prime_{pair}')
for i, pair in [(1, '2,3'), (2, '3,1'), (3, '1,2')]:
    inv('text', f'upper right block, row {i}', f'Gamma prime_{i}; ' + ('bordé par ' if i == 1 else 'repeat stroke ') + f'V_{pair}')
inv('display', 'below upper left table', 'partial = {x,y}')
inv('display', 'three-line union display, first line', 'Gamma_1 = Gamma_2 cup Gamma_3')
inv('display', 'three-line union display, second line', 'Gamma_2 = Gamma_3 cup Gamma_1')
inv('display', 'three-line union display, third line', 'Gamma_3 = Gamma_1 cup Gamma_2')
inv('drawing', 'middle left, lettering quarter-turned', 'three arcs Gamma prime_1, Gamma prime_2, Gamma prime_3; x-like mark; y; loop and hatching')
inv('deletion', 'inside drawing loop, beside upper junction in clockwise-rotated view', 'blotted x/partial')
inv('display', 'beside drawing, long line with two upright separators', 'Gamma_3 = Gamma double-prime_1 cup Gamma double-prime_(2/1) cup partial | U_3 = V_1 cup V_2 cup Gamma double-prime_3 | V_3')
inv('deletion', 'raised at first Gamma_3 of the line beside drawing', 'cancelled circle')
inv('display', 'next line, under the long expression', 'dot U_3 = Gamma_3')
inv('display', 'same line, to the right of the dotted-U identity', 'U_3 cup, unfinished')
inv('display', 'lower left above horizontal paper fold', 'uncertain dot; U,C,V')
inv('margin note', 'bottom left', '2, pencil archive sheet number; preserved as a comment', hand='another unnamed hand')

doubts = [
    {'place': 'Upper table, recurrent cancelled overmark', 'reading': r'\deleted{\unsure{\circ|\bullet}}', 'alternatives': r'\circ; \bullet', 'confidence': 'low', 'reason': 'The overworking covers the original small sign. First occurrence alone is marked; the second remains particularly filled.'},
    {'place': 'Set definition and recurrent live small mark in drawing', 'reading': r'\unsure{x}', 'alternatives': 'No second complete candidate can be securely recovered.', 'confidence': 'low', 'reason': 'The compact strokes are consistent between the two occurrences but do not expose a distinct crossing. Only the first occurrence is marked.'},
    {'place': 'First identity, first primed subscript', 'reading': r'\Gamma\'_{\unsure{1|2}}', 'alternatives': '1; 2', 'confidence': 'low', 'reason': 'Pointed entry and upright stem favour 1; the rightward lower bend still allows 2.'},
    {'place': 'Drawing, cancelled mark inside small loop', 'reading': r'\deleted{\unsure{x|\partial}}', 'alternatives': r'x; \partial', 'confidence': 'low', 'reason': 'The dense blot hides its internal stroke order; the surviving curved extension does not settle it.'},
    {'place': 'Expression beside drawing, second double-prime subscript', 'reading': r'\Gamma\'\'_{\unsure{2|1}}', 'alternatives': '2; 1', 'confidence': 'low', 'reason': 'The rounded head favours 2 but the large filled stem and two-sided base allow 1.'},
    {'place': 'Final group before U,C,V', 'reading': r'\unsure{\cdot}', 'alternatives': 'A dot versus an incidental pen mark; no alternative full symbol.', 'confidence': 'low', 'reason': 'The detached mid-height mark is real, but its intended role cannot be recovered from this page.'},
]

report = {
    'scan': 3, 'reader': 'R2', 'model': 'inherited parent model',
    'effort': 'inherited; value not independently exposed',
    'started_utc': '2026-11-19T22:00:06Z',
    'finished_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'images_viewed': [SOURCE+'J71-01_71_scan003.jpg', SOURCE+'J71-01_71_scan003_a.jpg', SOURCE+'J71-01_71_scan003_b.jpg'],
    'crops': crops, 'findings': findings, 'inventory': inventory, 'doubts': doubts,
    'notes': [
        'The page consists of an upper three-column arrangement, two adjacent verbal blocks, a definition of a two-point set, three union identities, a quarter-turned sketch, a long expression beside it, a dotted-U identity, an unfinished U_3 cup expression, and a final U,C,V group preceded by a small uncertain ink mark.',
        'The left table records Gamma double-prime_i = Gamma prime_i - partial for i=1,2,3. The nearby verbal rows say V_1 borde Gamma prime_2,Gamma prime_3; V_2 borde Gamma prime_3,Gamma prime_1; V_3 borde Gamma prime_1,Gamma prime_2. The right block writes Gamma prime_1 bordé par V_2,V_3, then repeats that wording by two long horizontal strokes for the cyclic pairs. These are page claims, not claims independently proved here.',
        'The three long identities use unprimed Gamma in their first two members, exactly as both text witnesses say. No unprinted primes, bars, or other mathematical repairs have been introduced. In the first line, the terminal pair is visibly double-prime 1 and double-prime 2; the first primed subscript remains uncertain.',
        'The sketch has three arcs between two junctions, two rounded adjacent regions, an irregular small loop around one junction, four oblique hatching strokes, two dotted returns, the outer labels Gamma prime_1 and Gamma prime_2, the median label Gamma prime_3, a live x-like glyph, a blotted glyph, and y. Small outline retraces are reproduced as strokes without assigning an arrow meaning.',
        'The expression alongside the sketch retains its two upright separators and isolated final V_3. The next line has a real dot over U_3, followed by = Gamma_3 and an independently unfinished U_3 cup group. No completion or intervening semicolon is added.',
        'The lower part of the sheet is blank apart from the thin pencil 2 at bottom left. That number is preserved as an archive-sheet comment, not treated as authorial pagination. No title, date, authorial page count, or prose self-doubt occurs in the ink on this page.',
        'All ten packet text files and meta.json were read. The whole image and the two supplied full-resolution halves were each viewed once, in that order. Seven local crops were made and each viewed once. No other page, other reader directory, OCR, text layer, internet resource, or outside research was used.',
        'S.json is an empty array, so there are no S rows to confirm or overturn. C_notes.md is empty; the C audit, doubt table, notation hypotheses, and inventory were checked against the supplied page images.',
        'The supplied H notes contain references to another page and describe decisions made in a prior pass. Those references were not followed and were not used as ink evidence. H drawing content was read directly; its x node is acknowledged rather than falsely reported missing.',
        'The reading starts with scanpage{3}. The single combined cotefile{71} heading is left to the assembling reader, avoiding a repeated heading within a combined transcription. Pure macro differences such as H page{2}, H Vert, and the C scan metadata are not treated as substantive misreadings.',
        'File integrity was checked: report.json parses, finding IDs are unique, the three logged source images and seven crop files exist, and reading.tex has balanced unescaped braces. A pdflatex compile was attempted with the supplied PREAMBLE.tex, but the environment has no pdflatex.fmt format file; compilation therefore could not start. No rendered-output inspection is claimed.',
    ],
    'checks': [
        {'statement_id': '003-table-boundaries', 'type': 'carried as background without fault found', 'statement': 'Gamma double-prime_i = Gamma prime_i minus partial, with cyclic bordering assertions for V_i.', 'outcome': 'Read against the ink and preserved. No definitions or proof of these topological assertions are supplied on this page, and no external page was consulted.'},
        {'statement_id': '003-first-union-expansion', 'type': 'targeted proof check', 'statement': 'If the depicted arcs all contain partial, then Gamma prime_2 cup Gamma prime_3 expands as Gamma double-prime_2 cup Gamma double-prime_3 cup partial.', 'outcome': 'Checked by writing each Gamma prime_i as (Gamma prime_i minus partial) cup partial under that explicit endpoint-containment assumption, then taking the union. This explains why the visible terminal pair 1,2 in the first line is mathematically suspicious if the uncertain primed digit is 2. It does not settle that digit, establish the author\'s definitions, or authorize a correction. The visible pair 1,2 is retained.'},
        {'statement_id': '003-three-union-identities', 'type': 'carried as background without fault found', 'statement': 'The complete three displayed identity chains involving unprimed, primed, and double-primed Gamma.', 'outcome': 'No independent proof was attempted. In particular, the equality of the initial unprimed terms is not validated from this page. The local conditional expansion above is the full mathematical scope of this run.'},
        {'statement_id': '003-U3-line', 'type': 'carried as background without fault found', 'statement': 'U_3 = V_1 cup V_2 cup Gamma double-prime_3 and dot U_3 = Gamma_3.', 'outcome': 'The symbols and separators were checked visually. The meaning of the dot and the necessary topological hypotheses are not defined in the page; these equations were not independently proved.'},
    ],
    'notation': [
        {'sign': 'Angular capitals with rightward top stroke', 'tex': r'\Gamma_i,\Gamma\'_i,\Gamma\'\'_i', 'place': 'table, three identity rows, drawing, and lower expressions', 'ink': 'Angular two-stroke Gamma; some stems are thick or retraced, not a distinct double-struck alphabet. Single and double high ticks remain distinct.', 'alternatives': 'No alternative alphabet retained.'},
        {'sign': 'Crossed small overmark', 'tex': r'\deleted{\unsure{\circ|\bullet}}', 'place': 'first marked above Gamma double-prime_1; repeated above the next two columns', 'ink': 'Rounded, filled, or triangular remains under cancelling strokes.', 'alternatives': r'\circ; \bullet. Only the first occurrence is explicitly marked.'},
        {'sign': 'Boundary sign', 'tex': r'\partial', 'place': 'bottom tier of table, set definition, union endpoints', 'ink': 'Upper hook with lower curved oval; the second union row has a broken/faint upper stroke.', 'alternatives': 'delta rejected for the recurring glyph; dotted partial rejected for the second-row instance on balance.'},
        {'sign': 'Turned equality', 'tex': r'\shortparallel', 'place': 'between second and third tiers of the upper left table', 'ink': 'Two short upright strokes in each column; the rightmost pair is joined by excess ink.', 'alternatives': 'H Vert is an equivalent encoding, not a substantive difference.'},
        {'sign': 'Repeated wording', 'tex': r'\text{---}', 'place': 'second and third rows of the upper right block', 'ink': 'Long horizontal stroke after the primed Gamma; it repeats bordé par rather than cancelling the V pair.', 'alternatives': 'No ditto words silently supplied.'},
        {'sign': 'Pointed and hooked low numerals', 'tex': r'1,2;\unsure{1|2};\unsure{2|1}', 'place': 'first identity and formula beside drawing', 'ink': 'Clear 1 can have an ascending entry and broad two-sided foot; clear 2 has a rounded/hooked head and rightward foot. Thick intermediate forms remain ambiguous.', 'alternatives': 'Explicit local alternatives are kept at the two crowded indices; the initial identity subscript is resolved as 1.'},
        {'sign': 'Small endpoint glyph and y', 'tex': r'\unsure{x},y', 'place': 'set definition and quarter-turned drawing', 'ink': 'The live small glyph is compact with joined strokes; y has a long descending tail.', 'alternatives': 'x is uncertain at first occurrence; the repeated drawing occurrence is unmarked by convention.'},
        {'sign': 'Dotted U and ordinary U,V,C', 'tex': r'\dot U_3;U,C,V', 'place': 'lower formula and last group', 'ink': 'U has a curled entry and rounded bottom; V is angular. The dot over U_3 is a separate heavy dot.', 'alternatives': 'No U/V ambiguity retained.'},
    ],
    'abbreviations': [],
    'brief_feedback': [
        'The first-occurrence rule for recurrent ambiguous glyphs can make a later item in the required C-doubt list appear unmarked. I have reported the later drawing x explicitly as unresolved while marking only the set-definition occurrence in reading.tex.',
        'The brief requests one cotefile heading at combined start while assigning one-page readings. I omitted that combined heading from this page fragment and recorded the decision here.',
    ],
}

# Raw strings above quote TeX prime ticks with a backslash only to keep Python
# literals readable. TeX requires plain apostrophes, so normalize that sequence.
def normalize(value):
    if isinstance(value, str):
        return value.replace("\\'", "'")
    if isinstance(value, list):
        return [normalize(x) for x in value]
    if isinstance(value, dict):
        return {k: normalize(v) for k, v in value.items()}
    return value

report = normalize(report)
(ROOT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(json.dumps({'findings': len(findings), 'inventory_items': len(inventory),
                  'crops': len(crops), 'remaining_doubt_groups': len(doubts),
                  'report': str(ROOT/'report.json')}, indent=2))
