from pathlib import Path
from datetime import datetime, timezone
import json

OUT = Path('/workspace/scratch/17347c1714f0/out/readers/scan003/R3')
PACKET = Path('/workspace/scratch/17347c1714f0/packets/scan003')
SOURCE = Path('/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans')

# The complete C syntax was read against the ink before being reused.
# Keep the original form of the crowded superscript explicitly uncertain.
reading = (OUT / 'reading.tex').read_text(encoding='utf-8')
reading = reading.replace(r'\Gamma_3^{\deleted{\circ}}', r"\Gamma_3^{\deleted{\unsure{\circ|'}}}")
(OUT / 'reading.tex').write_text(reading, encoding='utf-8')

findings = []
def finding(place, c, h, reading, *, diff_c=False, diff_h=False,
            c_doubt=False, kind='other', marked_in_H=False, evidence='',
            crop=None, confidence='high', unresolved=False, consequential=False):
    findings.append({
        'id': f'R3-003-{len(findings)+1:02d}', 'place': place,
        'c': c, 'h': h, 'reading': reading, 'diff_c': diff_c,
        'diff_h': diff_h, 'c_doubt': c_doubt, 's_id': None,
        'kind': kind, 'marked_in_H': marked_in_H, 'evidence': evidence,
        'crop': str(OUT / crop) if crop else None,
        'confidence': confidence, 'unresolved': unresolved,
        'consequential': consequential,
    })

finding('Top middle block, first word after V_1',
        r'\unsure{borde|bordes}', r'\uncertain{bords}', r'\unsure{borde|bords}',
        diff_c=True, diff_h=True, c_doubt=True, kind='misread word', marked_in_H=True,
        evidence='Crop 01 shows b-o-r-d followed by one short final hook. The ending can be an open e or a compressed s. There is no separate extra s after an e to support bordes. The clearer third row supports borde as the first candidate, but the first row alone does not settle e/s.',
        crop='01_borde.png', confidence='medium', unresolved=True)
finding('Top middle block, word after V_2',
        r'\text{borde}', r'\uncertain{bords}', r'\text{borde}',
        diff_h=True, kind='misread word', marked_in_H=True,
        evidence='Half a: the final low return follows d without an additional letter; this is the same compressed ending as the first row, transcribed borde. The first occurrence carries the page-level e/s uncertainty.',
        confidence='medium', unresolved=True)
finding('Top middle block, word after V_3',
        r'\text{borde}', r'\uncertain{bords}', r'\text{borde}',
        diff_h=True, kind='misread word', marked_in_H=True,
        evidence='Half a: the final low loop and rightward exit are visible after d. No separate terminal s is present.')
finding('Top right block, accent and final letter of bordé',
        r'\unsure{bordé}', 'bord', 'bordé',
        diff_c=True, diff_h=True, c_doubt=True, kind='misread word',
        evidence='Half a: a short raised acute is separate above the last low letter, following the ascender of d. The accented final e is present; the half settles this without an extra crop.')
finding('Top right block, word following bordé',
        'par', r'\uncertain{pour}', 'par',
        diff_h=True, kind='misread word', marked_in_H=True,
        evidence='Half a: after the descender of p there is a single low a body followed by a rightward r stroke; there are no separate o and u bodies.')
finding('Top left table, overworked sign over Gamma double-prime 1',
        r"\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}''_1",
        r"\Gamma''_1",
        r"\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}''_1",
        diff_h=True, c_doubt=True, kind='omission',
        evidence='Crop 02: a small loop with dense additional strokes is present above the corner of Gamma. Its earlier interior may have been open or filled; cancellation is retained, and circle/point remains uncertain. H has neither a mark nor a note encoding this local overmark.',
        crop='02_overmarks.png', confidence='low', unresolved=True)
finding('Top left table, overworked sign over Gamma double-prime 2',
        r"\overset{\deleted{\circ}}{\Gamma}''_2", r"\Gamma''_2",
        r"\overset{\deleted{\circ}}{\Gamma}''_2",
        diff_h=True, kind='omission',
        evidence='Crop 02: a low diagonal stroke meets a dense triangular overmark above Gamma. This is the second instance of the recurring cancelled sign; its uncertainty is marked at the first instance.',
        crop='02_overmarks.png', confidence='low', unresolved=True)
finding('Top left table, overworked sign over Gamma double-prime 3',
        r"\overset{\deleted{\circ}}{\Gamma}''_3", r"\Gamma''_3",
        r"\overset{\deleted{\circ}}{\Gamma}''_3",
        diff_h=True, kind='omission',
        evidence='Crop 02: an incomplete rounded top and a dense left portion are present above Gamma, distinct from the two prime strokes at its right. This repeats the cancelled sign whose ambiguity is marked at its first occurrence.',
        crop='02_overmarks.png', confidence='medium', unresolved=True)
finding('Top left table, first boundary glyph after the minus',
        r"\Gamma'_1-\unsure{\partial|\delta}", r"\Gamma'_1 - \partial",
        r"\Gamma'_1-\partial",
        diff_c=True, c_doubt=True, kind='misread symbol or index',
        evidence='Crop 03: the top starts at the left, arches to the right, and descends into a low loop. The second and third copies have the same open return. This is the handwritten partial glyph, not a separate delta form.',
        crop='03_boundary_notation.png')
finding('Definition beneath the table, first member of the endpoint set',
        r'\partial=\{\unsure{x},y\}', r'\partial = \{x, y\}',
        r'\partial=\{\unsure{x},y\}',
        diff_h=True, c_doubt=True, kind='misread symbol or index',
        evidence='Crop 04: the first letter is very small, with a leftward head and dark meeting strokes; it is not a clear ordinary crossed x. The similarly bent mark at the circled junction in crop 08 supports x, but does not remove the uncertainty. The comma and y are clear.',
        crop='04_endpoint_set.png', confidence='low', unresolved=True, consequential=True)
finding('Three-line display, initial subscript of the first identity',
        r'\Gamma_1', r'\Gamma_1', r'\Gamma_1',
        evidence='Crop 05: the first digit has a rising entry to a straight upright and a two-sided baseline, unlike the adjacent 2 with its turn and one-sided foot. The reading is 1; the formerly mentioned C-audit doubt is not revived.',
        crop='05_initial_identity_index.png')
finding('Three-line display, first single-primed Gamma in the first identity',
        r"\Gamma'_{\unsure{2|1}}", r"\Gamma'_2", r"\Gamma'_{\unsure{2|1}}",
        diff_h=True, c_doubt=True, kind='misread symbol or index',
        evidence='Crop 06: the low digit has a thick hooked head, upright body, and a short foot mainly to the right. It favours 2, but the heavy central stroke does not exclude a short 1. No additional crop was made.',
        crop='06_primed_identity_index.png', confidence='medium', unresolved=True, consequential=True)
finding('Three-line display, final double-prime pair in the first identity',
        r"\Gamma''_1\cup\Gamma''_2\cup\partial",
        r"\Gamma''_1 \cup \Gamma''_2 \cup \partial",
        r"\Gamma''_1\cup\Gamma''_2\cup\partial",
        marked_in_H=True,
        evidence='Half a and crop 07 show a narrow rising 1 under the first double-prime Gamma and a curled 2 under the next. The written pair is 1,2. It is retained despite the different pair suggested by expanding the preceding primed union. H marks index uncertainty in its editorial note.',
        crop='07_identity_right_ends.png', consequential=True)
finding('Three-line display, terminal boundary sign in the second identity',
        r'\unsure{\dot\partial|\partial}', r'\partial', r'\unsure{\dot\partial|\partial}',
        diff_h=True, c_doubt=True, kind='misread symbol or index',
        evidence='Crop 07: a dark detached point is above the curved body, with a visible gap. In the neighbouring copies, the corresponding high starting stroke connects to the descending curve. A separate dot and a broken initial stroke of partial are both ink-supported; neither is silently normalised.',
        crop='07_identity_right_ends.png', confidence='low', unresolved=True, consequential=True)
finding('Drawing, right outer arc label when turned clockwise',
        r"\Gamma'_{\unsure{2}}",
        r'\node[inner sep=1pt] at (84,-41.5) {\small $\Gamma\'_2$};'.replace(r"\Gamma\'", r"\Gamma'"),
        r"\Gamma'_2",
        diff_c=True, c_doubt=True, kind='misread symbol or index',
        evidence='Crop 08, turned 90 degrees clockwise: beneath the prime is a curved upper hook, diagonal/curved descent, and broad rightward foot. The crossing hatch passes through its middle but leaves the numeral 2 legible. The left and median labels independently read Gamma-prime-1 and Gamma-prime-3.',
        crop='08_drawing.png')
finding('Drawing, small live letter above the circled junction',
        r'\node[rotate=90,inner sep=0pt] at (-.16,1.59) {\scriptsize $\unsure{x}$};',
        r'\node[inner sep=1pt] at (46.5,-27) {\small $x$};',
        r'\node[rotate=90,inner sep=0pt] at (-.16,1.59) {\scriptsize $x$};',
        diff_c=True, c_doubt=True, kind='other',
        evidence='Crop 08: the small bent letter has the same compact form as the first letter of the endpoint set. Its identification as x remains uncertain; the uncertainty mark is kept at the first occurrence in the set, in accordance with the recurrent-glyph convention. H does include x in its drawing asset, so this is not an H omission.',
        crop='08_drawing.png', confidence='low', unresolved=True)
finding('Drawing, dark worked-over mark to the right of the upper junction',
        r'\deleted{\unsure{x|\partial}}', None, r'\deleted{\unsure{x|\partial}}',
        diff_h=True, c_doubt=True, kind='omission',
        evidence='Crop 08: the dark filled mark has a short rightward return meeting the circlet. Its earlier form is obscured; the x/partial candidates are retained. H drawing comments explicitly say that this blot is not drawn, and there is no drawing command for it.',
        crop='08_drawing.png', confidence='low', unresolved=True)
finding('Line beside the drawing, superscript of the initial Gamma_3',
        r"\Gamma_3^{\deleted{\unsure{\circ|'}}}", r'\Gamma^{*}_3',
        r"\Gamma_3^{\deleted{\unsure{\circ|'}}}",
        diff_h=True, c_doubt=True, kind='deletion state (struck given live or live given struck)',
        evidence='Crop 09: a small pale centre remains inside a round lower portion, with dense crossing/overwriting strokes and an upper upright. A cancelled circlet is the better reading; the earlier prime alternative cannot be fully excluded. This does not look like a clean separate live asterisk. The deletion and uncertainty are retained.',
        crop='09_beside_drawing.png', confidence='medium', unresolved=True, consequential=True)
finding('Line beside the drawing, second double-primed Gamma subscript',
        r"\Gamma''_{\unsure{2|1}}", r"\Gamma''_2", r"\Gamma''_{\unsure{2|1}}",
        diff_h=True, c_doubt=True, kind='misread symbol or index',
        evidence='Crop 09: the digit has a heavy rounded head and very broad two-sided base. Its inner-left recess favours 2, but the overwritten upright and base can also be a 1. It remains marked rather than being selected for algebraic consistency.',
        crop='09_beside_drawing.png', confidence='medium', unresolved=True, consequential=True)
finding('Last list, detached small mark before U',
        r'\unsure{\cdot}\ U,C,V', '$U, C, V$', r'\unsure{\cdot}\ U,C,V',
        diff_h=True, c_doubt=True, kind='omission',
        evidence='Crop 10: the detached mark has a small dark angled body and a faint lower continuation. It can be represented by a dot, but the crop does not establish its intended function or that it is a deliberate punctuation sign. It is retained with uncertainty.',
        crop='10_detached_mark.png', confidence='low', unresolved=True)
finding('First verbal row, punctuation between the middle and right blocks',
        "\\Gamma'_2,\\Gamma'_3&\n\\Gamma'_1",
        "$\\Gamma'_2, \\Gamma'_3$ ; $\\Gamma'_1$",
        "\\Gamma'_2,\\Gamma'_3&\n\\Gamma'_1",
        diff_h=True, kind='text not on the page',
        evidence='Half a: these are separate horizontal blocks with blank space between them. There is no semicolon after Gamma-prime-3. The comma between the two arcs is present.')
finding('Second verbal row, punctuation between the middle and right blocks',
        r"\Gamma'_3,\Gamma'_1&\Gamma'_2", "$\\Gamma'_3, \\Gamma'_1$ ; $\\Gamma'_2$",
        r"\Gamma'_3,\Gamma'_1&\Gamma'_2",
        diff_h=True, kind='text not on the page',
        evidence='Half a: there is blank space between the blocks and no semicolon. The long line in the right block is the repeated wording, not punctuation or deletion of the V entries.')
finding('Third verbal row, punctuation between the middle and right blocks',
        r"\Gamma'_1,\Gamma'_2&\Gamma'_3", "$\\Gamma'_1, \\Gamma'_2$ ; $\\Gamma'_3$",
        r"\Gamma'_1,\Gamma'_2&\Gamma'_3",
        diff_h=True, kind='text not on the page',
        evidence='Half a: the row has a comma inside each pair but no semicolon between the two horizontal blocks.')
finding('Line below the long formula, separator after dotted U_3 = Gamma_3',
        r'\dot U_3=\Gamma_3\qquad U_3\cup', r'$\dot{U}_3 = \Gamma_3$ ; $U_3 \cup$',
        r'\dot U_3=\Gamma_3\qquad U_3\cup',
        diff_h=True, kind='text not on the page',
        evidence='Half a: there is open space after Gamma_3 and then U_3 followed by a cup. No semicolon is visible. The final cup has no right operand and is not completed in the reading.')
finding('Endpoint-set definition, position relative to the table',
        "\\[\n\\partial=\\{\\unsure{x},y\\}\n\\]",
        r'\qquad \partial = \{x, y\}',
        "\\[\n\\partial=\\{\\unsure{x},y\\}\n\\]",
        diff_h=True, kind='insertion or placement',
        evidence='Whole image and half a: the definition stands below the left three-column table, not alongside it on the same baseline. It is kept as its own display. H puts it in the same display immediately after the array.')
finding('Lower left corner, pencil archive number',
        '% archive sheet number: 2', r'\page{2}', '% archive sheet number: 2',
        diff_h=True, kind='other',
        evidence='Half b: the isolated 2 is small, grey, and at the extreme lower-left corner, unlike the dark main writing. It is treated as the archive pencil number under the brief, not as an author page heading. No mspage is introduced.')
finding('Formula beneath the drawing, dotted U and unfinished union',
        r'\dot U_3=\Gamma_3\qquad U_3\cup', r'$\dot{U}_3 = \Gamma_3$ ; $U_3 \cup$',
        r'\dot U_3=\Gamma_3\qquad U_3\cup',
        evidence='Half a: the first letter has a clear separate round point above it, and both letters have the hooked U form rather than V. The unfinished U_3 cup noted among C slips is retained. The punctuation difference is separately recorded above.',
        consequential=True)

inventory = []
def item(kind, position, first, hand='his hand'):
    inventory.append({'scan': 3, 'sheet_kind': 'text', 'hand': hand,
                      'element': f'003-R3-{len(inventory)+1:02d}', 'kind': kind,
                      'position': position, 'first_words_or_objects': first,
                      'transcribed': 'yes'})
item('display', 'Top left, three columns separated from the verbal blocks by a vertical rule',
     'V_1 V_2 V_3; Gamma double-prime i; short vertical equality strokes; Gamma-prime i minus partial')
item('deletion', 'Nested in the top-left display, over Gamma double-prime 1', 'Cancelled circle/point')
item('deletion', 'Nested in the top-left display, over Gamma double-prime 2', 'Repeated cancelled overmark')
item('deletion', 'Nested in the top-left display, over Gamma double-prime 3', 'Repeated cancelled overmark')
item('text', 'Top middle, first row', 'V_1 borde Gamma-prime 2, Gamma-prime 3')
item('text', 'Top middle, second row', 'V_2 borde Gamma-prime 3, Gamma-prime 1')
item('text', 'Top middle, third row', 'V_3 borde Gamma-prime 1, Gamma-prime 2')
item('text', 'Top right, first row', 'Gamma-prime 1 bordé par V_2,V_3')
item('text', 'Top right, second row', 'Gamma-prime 2 — V_3,V_1')
item('text', 'Top right, third row', 'Gamma-prime 3 — V_1,V_2')
item('display', 'Below the top-left table', 'partial = {x?,y}')
item('display', 'Below the top blocks, right, first identity', 'Gamma_1 = Gamma_2 cup Gamma_3 = ...')
item('display', 'Below the top blocks, right, second identity', 'Gamma_2 = Gamma_3 cup Gamma_1 = ...')
item('display', 'Below the top blocks, right, third identity', 'Gamma_3 = Gamma_1 cup Gamma_2 = ...')
item('drawing', 'Middle left; lettering becomes upright after a clockwise quarter-turn',
     'Three arcs Gamma-prime 1,2,3 sharing endpoints; circled upper junction, x?, y, four diagonal strokes and two dotted returns')
item('deletion', 'Nested in the drawing, to the right of its upper junction when upright', 'Dark cancelled x/partial')
item('display', 'To the right of the drawing', 'Gamma_3 with a cancelled superscript = Gamma double-prime 1 cup Gamma double-prime 2? cup partial')
item('deletion', 'Nested in the formula beside the drawing, superscript of initial Gamma_3', 'Cancelled circlet/prime')
item('display', 'Continuation of the line beside the drawing, after first vertical separator', 'U_3 = V_1 cup V_2 cup Gamma double-prime 3')
item('display', 'Right end of that line, after second vertical separator', 'V_3')
item('display', 'Next line, below the long formula', 'dotted U_3 = Gamma_3')
item('display', 'Same line, to the right of dotted U_3 equality', 'U_3 cup, unfinished')
item('display', 'Lower left of the written area, above the fold', 'Small uncertain dot, U,C,V')
item('text', 'Extreme lower-left corner, separate pencil mark', 'Archive pencil 2; recorded in a comment', hand='another unnamed hand')

crops = json.loads((OUT / 'crop_log.json').read_text())
observed = [
    'One short terminal hook after bord; e/s unresolved. No separate es sequence.',
    'All three overmarks exist; their overwritten earlier circle/point form remains uncertain.',
    'Recurring glyph resolved as partial from its upper arch and low return; delta alternative removed.',
    'First endpoint remains x?; comma and y are clear.',
    'Initial first-identity digit resolved as 1 from rising entry, straight stem and two-sided baseline.',
    'First primed subscript favours 2; 1 still possible through the heavy central stroke.',
    'Second-row boundary has a detached point; dotted partial versus broken-stroke partial remains unresolved. First-row double-prime subscripts are 1 and 2.',
    'Clockwise turn confirms arc labels 1,2,3 and y; the upper small mark remains x? and the other mark is obliterated. Four diagonal strokes and two short dotted curves are visible.',
    'Superscript is worked over with a visible round centre, favouring a cancelled circlet; prior prime and the low 2/1 subscript remain uncertain.',
    'Tiny detached angled ink mark before U exists; intention remains uncertain, so the dot candidate stays marked.',
]
for crop, description in zip(crops, observed):
    crop['observed'] = description
    crop['viewed_once'] = True

doubts = [
    {'place': 'First middle-block borde and its recurrence in row 2', 'reading': 'borde', 'alternatives': 'bords', 'confidence': 'medium', 'reason': 'A single open terminal hook does not completely distinguish e and s; the clearer third occurrence supports e.'},
    {'place': 'Three cancelled overmarks in the top-left table', 'reading': r'\circ', 'alternatives': r'\bullet', 'confidence': 'low', 'reason': 'Overwriting obscures whether the earlier centre was open or filled; first occurrence marked.'},
    {'place': 'First member of the endpoint set and matching small drawing label', 'reading': 'x', 'alternatives': 'No alternative letter confidently identified', 'confidence': 'low', 'reason': 'The small bent strokes are heavily compressed; recurring doubt is marked at the set occurrence.'},
    {'place': 'First identity, first single-primed Gamma subscript', 'reading': '2', 'alternatives': '1', 'confidence': 'medium', 'reason': 'Hooked head and one-sided foot favour 2, but heavy ink hides the distinguishing turn.'},
    {'place': 'Second identity, terminal boundary glyph', 'reading': r'\dot\partial', 'alternatives': r'\partial', 'confidence': 'low', 'reason': 'Detached point may be a separate dot or a disconnected initial stroke.'},
    {'place': 'Drawing, overwritten mark inside the small loop', 'reading': 'x', 'alternatives': r'\partial', 'confidence': 'low', 'reason': 'Dense ink hides the earlier centre; short rightward tail remains.'},
    {'place': 'Line beside drawing, cancelled superscript on initial Gamma_3', 'reading': r'\circ', 'alternatives': "'", 'confidence': 'medium', 'reason': 'A small round centre favours a circlet, but the upper upright and heavy overwriting prevent complete recovery.'},
    {'place': 'Line beside drawing, second double-primed Gamma subscript', 'reading': '2', 'alternatives': '1', 'confidence': 'medium', 'reason': 'Rounded head and recess favour 2; wide overwritten base also allows 1.'},
    {'place': 'Detached mark before final U,C,V', 'reading': r'\cdot', 'alternatives': 'No second symbolic candidate; function uncertain', 'confidence': 'low', 'reason': 'Small angled spot is visible but may be an incidental mark.'},
]

notes = [
    'The page is handwritten throughout its main content. It has no date, title, prose paragraph, or explicit self-doubt sentence. The separate pencil 2 is treated as the archive sheet number, not an author page number.',
    'The upper-left table puts V_1,V_2,V_3 over three double-primed Gamma entries, each bearing a worked-over old overmark. Short paired vertical strokes connect them visually with Gamma-prime i minus partial.',
    'The middle block gives the cyclic pairings V_1 with Gamma-prime 2 and 3, V_2 with 3 and 1, and V_3 with 1 and 2. The right block writes Gamma-prime 1 bordé par V_2,V_3 and repeats the wording by horizontal rules for the other cyclic pairs. These assertions are transcribed as background, not proved from a supplied topology.',
    'A separate definition below the table gives partial = {x?,y}. The first letter remains uncertain; the two-member set itself, braces, comma, and y are visible.',
    'The three long identities have plain unprimed Gamma symbols in their first two members. No prime or circle has been supplied to repair those members.',
    'The first identity ends with Gamma-double-prime 1 union Gamma-double-prime 2 union partial, as both witnesses write. The mismatch with the preceding likely Gamma-prime 2 union Gamma-prime 3 is retained. The local algebraic comparison is documented in the checks rather than used to change the ink.',
    'The drawing consists of three arcs sharing two junctions, labelled Gamma-prime 1 on the left, Gamma-prime 2 on the right, and Gamma-prime 3 at the median arc when the sheet is turned clockwise. A small loop surrounds the upper junction and two small marks; the lower junction is labelled y. Four oblique strokes and two dotted curved returns are reproduced. Curves and positions are a schematic tracing, not a proof of geometric regularity.',
    'Beside the drawing is Gamma_3 with a worked-over superscript, then Gamma-double-prime 1 union Gamma-double-prime 2? union partial, a vertical separator, U_3 = V_1 union V_2 union Gamma-double-prime 3, another separator, and V_3.',
    'Below this is dotted U_3 = Gamma_3 followed by an unfinished U_3 union. The unfinished expression is not completed. The last separate group reads an uncertain tiny dot followed by U,C,V.',
    'H editorial notes and drawing comments were read as witness apparatus, not mistaken for text physically present on the sheet. Their references to another page were not consulted or used as evidence. H drawing does include x and the dotted returns; only its explicitly undrawn dark mark is counted as a drawing omission.',
    'S.json contains no rows. There are consequently no S decisions to accept or overturn on this page.',
    'The whole scan was viewed once for layout, then half a and half b once in order. The lower half contains no main text after the overlapping final list; its only independent written item is the pencil 2. Ten local crops were made and viewed once each. Several tightly grouped recurring marks share a crop; no crop was remade and no second enlargement was made of a decided place.',
    'The final TeX starts with scanpage{3}; the combined-file cotefile{71} marker is intentionally left to the main reader, following the single-marker convention. No mspage is introduced. The C figure paths were reused only after their arcs, hatching, labels and marks had been compared with the ink; the two label adjustments are listed in findings.',
]

checks = [
    {'statement_id': 'R3-003-M01', 'type': 'carried as background without fault found',
     'statement': r"\Gamma''_i=\Gamma'_i-\partial (i=1,2,3), as arranged in the upper-left table",
     'outcome': 'Read as displayed notation/definitions. No topological interpretation of the V row or the vertical equality strokes was proved.'},
    {'statement_id': 'R3-003-M02', 'type': 'carried as background without fault found',
     'statement': 'The six cyclic border pairings in the middle and right blocks',
     'outcome': 'The pair order was visually checked. No ambient space, separation hypothesis, or definition of borde is supplied here, so no mathematical border theorem was claimed.'},
    {'statement_id': 'R3-003-M03', 'type': 'carried as background without fault found',
     'statement': r'\partial=\{x,y\}',
     'outcome': 'Treated as the page definition, with the first letter marked uncertain. Not independently established from external context.'},
    {'statement_id': 'R3-003-M04', 'type': 'targeted proof check',
     'statement': 'Prime-to-double-prime expansion in the first identity',
     'outcome': "Conditional on the endpoint interpretation partial being contained in each primed arc, the table gives Gamma-prime i = Gamma-double-prime i union partial. Therefore Gamma-prime 2 union Gamma-prime 3 expands to Gamma-double-prime 2 union Gamma-double-prime 3 union partial. The written final pair is 1,2. A concrete local set example, partial={x,y}, Gamma-prime 1={x,y,a}, Gamma-prime 2={x,y,b}, Gamma-prime 3={x,y,c}, gives {x,y,b,c} for the preceding union and {x,y,a,b} for the written final union. This shows the written equality is not a formal consequence of the table, not that the author could not have additional context. No emendation was made."},
    {'statement_id': 'R3-003-M05', 'type': 'targeted proof check',
     'statement': 'The three plain-Gamma equalities Gamma_1 = Gamma_2 union Gamma_3, Gamma_2 = Gamma_3 union Gamma_1, Gamma_3 = Gamma_1 union Gamma_2',
     'outcome': 'As set equalities they imply all three Gamma sets are equal: the first gives Gamma_2 and Gamma_3 contained in Gamma_1, and the second and third supply the reverse inclusions. This is only a logical consequence check; the page alone does not establish whether equal sets were intended. The unprimed ink is preserved.'},
    {'statement_id': 'R3-003-M06', 'type': 'targeted proof check',
     'statement': 'Ordinary prime-to-double-prime pair expansions in rows 2 and 3',
     'outcome': 'With the same explicitly stated endpoint-containment assumption, distributing union gives the pairs (3,1) and (1,2), agreeing with the written indices. This check does not decide whether the detached mark over the final row-2 boundary is a dot; that remains a transcription uncertainty.'},
    {'statement_id': 'R3-003-M07', 'type': 'carried as background without fault found',
     'statement': 'The three-arc drawing, the formula beside it, U_3 = V_1 union V_2 union Gamma-double-prime 3, and dotted U_3 = Gamma_3',
     'outcome': 'These were transcribed and their symbols compared with the ink. No proof was attempted of a boundary relation or of a particular meaning of the dotted U; the necessary definitions are not supplied on this page.'},
]

notation = [
    {'sign': 'Gamma, plain/single-prime/double-prime', 'tex': r"\Gamma_i,\Gamma'_i,\Gamma''_i", 'place': 'Throughout upper table and equalities', 'ink': 'Angular capital with a rightward top; left stems are sometimes retraced and thick. Prime strokes occur separately above-right; low digits remain distinct.', 'alternatives': 'No alternate alphabet inferred from heavy/retraced stems.'},
    {'sign': 'Cancelled overmark', 'tex': r'\deleted{\unsure{\circ|\bullet}}', 'place': 'First occurrence in upper-left table, repeated over the next two Gamma entries', 'ink': 'Small rounded/filled or triangular overworked marks above Gamma, not its live prime strokes.', 'alternatives': r'\circ or \bullet; first occurrence marked, later repetitions unmarked.'},
    {'sign': 'Vertical equality-like strokes', 'tex': r'\shortparallel', 'place': 'Between the second and third tiers of the left table', 'ink': 'Two short upright strokes, with the third pair partly joined.', 'alternatives': r'\Vert is an equivalent H rendering, not a substantive witness difference.'},
    {'sign': 'Boundary glyph', 'tex': r'\partial', 'place': 'Subtractions in top-left table, set definition, ends of unions', 'ink': 'High left starting hook arcs rightwards and descends to a low return/loop.', 'alternatives': 'Delta rejected for the ordinary recurrent glyph after crop 03.'},
    {'sign': 'Detached point over boundary glyph', 'tex': r'\unsure{\dot\partial|\partial}', 'place': 'End of second long identity', 'ink': 'Separate upper point, then a gap before the curved body.', 'alternatives': 'A genuine dot or a disconnected starting stroke.'},
    {'sign': 'Numeral 1 and numeral 2', 'tex': '1,2', 'place': 'First identity and lower formula', 'ink': '1 can have a rising entry and two-sided foot; 2 normally has a hooked head and one-sided curved foot. Heavy overwriting obscures two of the smaller instances.', 'alternatives': '2/1 retained at the first primed subscript of row 1 and second double-primed subscript beside the drawing.'},
    {'sign': 'U, V, union, dotted U', 'tex': r'U,V,\cup,\dot U_3', 'place': 'Formula beside/below drawing and final list', 'ink': 'U has a hooked ascending entry and rounded return; V has two meeting strokes; the union cup is shorter. The dot over U_3 is distinct and round.', 'alternatives': 'No U/V or dot uncertainty retained at the dotted U formula.'},
    {'sign': 'Endpoint letters', 'tex': r'\unsure{x},y', 'place': 'Set and clockwise-turned drawing', 'ink': 'First letter is small and bent; y has a prominent descender. The same small first-letter form recurs above the drawing junction.', 'alternatives': 'x uncertain; no second letter candidate confidently recovered.'},
    {'sign': 'Repeated wording', 'tex': r'\text{---}', 'place': 'Second and third rows of the right verbal block', 'ink': 'Long horizontal repeat strokes between Gamma-prime i and its V pair.', 'alternatives': 'Repeat of bordé par, not cancellation of adjacent symbols.'},
    {'sign': 'Tiny detached mark', 'tex': r'\unsure{\cdot}', 'place': 'Before final U,C,V', 'ink': 'Small dark angled spot with a faint lower continuation.', 'alternatives': 'Intent/function uncertain; no second symbolic candidate.'},
]

report = {
    'scan': 3, 'reader': 'R3', 'model': 'inherited parent model',
    'effort': 'inherited; value not independently exposed',
    'started_utc': '2026-11-19T22:00:18Z',
    'finished_utc': datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    'images_viewed': [str(SOURCE / n) for n in ['J71-01_71_scan003.jpg','J71-01_71_scan003_a.jpg','J71-01_71_scan003_b.jpg']],
    'crops': crops, 'findings': findings, 'inventory': inventory,
    'doubts': doubts, 'notes': notes, 'checks': checks, 'notation': notation,
    'abbreviations': [],
    'brief_feedback': [
        'The supplied half a is an exact top crop at the same 1682-pixel width as the whole image, and half b overlaps the final list. Both were nevertheless viewed once in the prescribed order.',
        'For clustered recurrent ambiguities (the three overmarks and three adjacent terminal boundary glyphs), one shared tight crop was used for comparison, rather than several overlapping crops of the same strokes. The drawing likewise received one rotated crop covering its unresolved labels and marks.'
    ],
}
(OUT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')
print(json.dumps({'report': str(OUT / 'report.json'), 'reading': str(OUT / 'reading.tex'),
                  'findings': len(findings), 'inventory_items': len(inventory),
                  'crops': len(crops), 'unresolved_doubts': len(doubts)}, ensure_ascii=False))
