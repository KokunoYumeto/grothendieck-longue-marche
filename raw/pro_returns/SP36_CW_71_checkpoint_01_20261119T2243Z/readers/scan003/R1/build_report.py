from pathlib import Path
import json
from datetime import datetime, timezone

ROOT = Path('/workspace/scratch/17347c1714f0/out/readers/scan003/R1')
SOURCE = '/workspace/scratch/17347c1714f0/source/SP36_CW_71_scans/'
findings = []

def finding(place, c, h, reading, diff_c, diff_h, c_doubt, kind, evidence,
            crop=None, confidence='high', unresolved=False, consequential=False,
            marked_in_H=False):
    findings.append(dict(id=f'R1-003-{len(findings)+1:02d}', place=place, c=c, h=h,
                         reading=reading, diff_c=diff_c, diff_h=diff_h,
                         c_doubt=c_doubt, s_id=None, kind=kind,
                         marked_in_H=marked_in_H, evidence=evidence,
                         crop=str(ROOT / crop) if crop else None,
                         confidence=confidence, unresolved=unresolved,
                         consequential=consequential))

finding('Top middle block, first row, word after V_1',
        r'\text{\unsure{borde|bordes}}', r'\uncertain{bords}', r'\text{borde}',
        True, True, True, 'misread word',
        'The enlarged word has the tall d followed by one terminal small turn. There is no additional s after that ending. The other two rows visibly repeat borde.',
        '01_borde.png', confidence='medium', marked_in_H=True)
finding('Top middle block, second row, word after V_2',
        r'\text{borde}', r'\uncertain{bords}', r'\text{borde}',
        False, True, False, 'misread word',
        'Half a shows borde, with a single terminal e-like turn after the d; no extra final s.', marked_in_H=True)
finding('Top middle block, third row, word after V_3',
        r'\text{borde}', r'\uncertain{bords}', r'\text{borde}',
        False, True, False, 'misread word',
        'Half a shows the clearest of the three instances: borde, with the final small e after the d.', marked_in_H=True)
finding('Top right block, first row, reciprocal wording',
        r'\text{\unsure{bordé} par}', r'bord \uncertain{pour}', r'\text{bordé par}',
        True, True, True, 'misread word',
        'Half a shows a small raised acute after the end of bordé. The next word has p, a low a-shaped middle, and a short terminal r; no ou sequence is visible.',
        confidence='high', marked_in_H=True)
finding('Top left block, mark above Gamma double-prime 1',
        r"\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}''_1",
        r"\Gamma''_1", r"\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}''_1",
        False, True, True, 'omission',
        'A small loop above the Gamma corner is heavily worked over. A remnant pale interior supports circlet, but its original state cannot be separated securely from a filled point. The cancellation is present and H omits it.',
        '02_overmarks.png', confidence='low', unresolved=True)
finding('Top left block, mark above Gamma double-prime 2',
        r"\overset{\deleted{\circ}}{\Gamma}''_2", r"\Gamma''_2",
        r"\overset{\deleted{\circ}}{\Gamma}''_2",
        False, True, False, 'omission',
        'A dark triangular worked-over mark stands separately above the second Gamma. It belongs to the same repeated cancelled sign as column 1; its uncertainty is marked at the first occurrence only.',
        '02_overmarks.png', confidence='medium', unresolved=True)
finding('Top left block, mark above Gamma double-prime 3',
        r"\overset{\deleted{\circ}}{\Gamma}''_3", r"\Gamma''_3",
        r"\overset{\deleted{\circ}}{\Gamma}''_3",
        False, True, False, 'omission',
        'Above the third Gamma a worked-over rounded sign retains a small hook at the right. It is the third repetition of the cancelled sign; H has no overmark.',
        '02_overmarks.png', confidence='medium', unresolved=True)
finding('Top left block, first subtraction, boundary sign',
        r"\Gamma'_1-\unsure{\partial|\delta}", r"\Gamma'_1 - \partial",
        r"\Gamma'_1-\partial",
        True, False, True, 'other',
        'Half a shows the same upper hook and low loop in all three subtractions and in the definition below. The hook approaches the closed lower loop from above on its right, supporting partial rather than delta. The enlarged definition confirms this repeated form.',
        confidence='high')
finding('Definition below top left block, first element of endpoint set',
        r'\partial=\{\unsure{x},y\}', r'\partial = \{x, y\}',
        r'\partial=\{\unsure{x},y\}',
        False, True, True, 'misread symbol or index',
        'The tiny first element has a short upper left stroke and a thick bent right portion; an x remains the best candidate but the tiny strokes do not securely resolve its letter form. The matching small live label in the drawing is treated as the same recurrent glyph.',
        '03_endpoint_set.png', confidence='low', unresolved=True, consequential=True)
finding('First union identity, leftmost Gamma subscript',
        r'\Gamma_1', r'\Gamma_1', r'\Gamma_{\unsure{2|1}}',
        True, True, False, 'misread symbol or index',
        'The crop shows a hooked/arched head, descending stroke, and broad baseline extending to both sides. Its overall outline reads most readily as 2 to this reader, but a serifed 1 remains supported. Both witnesses give a definite 1; I do not regard the enlarged ink as settling that choice.',
        '04_first_identity.png', confidence='low', unresolved=True, consequential=True)
finding('First union identity, first single-primed Gamma subscript',
        r"\Gamma'_{\unsure{2|1}}", r"\Gamma'_2", r"\Gamma'_2",
        True, False, True, 'other',
        'The small digit has a compact hooked head, a descending stroke, and a rightward foot, matching the clear 2 immediately earlier in the line. Read 2; no uncertainty retained here.',
        '04_first_identity.png', confidence='medium', consequential=True)
finding('First union identity, last two double-primed subscripts; C retained slip',
        r"\Gamma''_1\cup\Gamma''_2\cup\partial",
        r"\Gamma''_1 \cup \Gamma''_2 \cup \partial",
        r"\Gamma''_1\cup\Gamma''_2\cup\partial",
        False, False, True, 'other',
        'The first low digit is a pointed 1 with a short descending right stem; the next is a small hooked 2. These are visibly 1 and 2, despite the preceding single-primed pair 2 and 3. No mathematical correction is made.',
        '04_first_identity.png', confidence='high', consequential=True, marked_in_H=True)
finding('Second union identity, terminal boundary sign and detached mark',
        r'\unsure{\dot\partial|\partial}', r'\partial',
        r'\unsure{\partial|\dot\partial}',
        True, True, True, 'misread symbol or index',
        'A separate dark point sits above the curved main stroke. The main stroke lacks the full upper hook seen in other instances of partial, so a broken beginning of partial is my first reading; a deliberate dot cannot be excluded. The detached point itself is certain, its function is not.',
        '05_row2_terminal.png', confidence='low', unresolved=True, consequential=True)
finding('Drawing, right outer curve label when turned upright, subscript',
        r"\Gamma'_{\unsure{2}}", r"\Gamma'_2", r"\Gamma'_2",
        True, False, True, 'other',
        'In the clockwise-turned crop the numeral retains its upper arch and rightward foot on either side of the crossing oblique stroke. The visible form supports 2.',
        '06_drawing.png', confidence='medium')
finding('Drawing, small live letter above the junction inside the loop',
        r'\unsure{x}', r'x', r'x',
        True, False, True, 'other',
        'The small label has the same short bent form as the uncertain first set element. Its identification remains uncertain; it is written unmarked here only because this recurrent glyph has already been marked at its first page occurrence. H drawing asset includes x, so it is not an omission.',
        '06_drawing.png', confidence='low', unresolved=True)
finding('Drawing, heavily overwritten mark to the right of the junction inside the loop',
        r'\deleted{\unsure{x|\partial}}', None,
        r'\deleted{\unsure{x|\partial}}',
        False, True, True, 'drawing or diagram',
        'There is a filled overwritten form with a short trailing curve to its right. The original letter/sign cannot be recovered securely; x and partial remain the ink-supported candidates supplied by C. H drawing comments acknowledge a blot but the drawn asset omits it. I retain the cancelled mark explicitly.',
        '06_drawing.png', confidence='low', unresolved=True)
finding('Identity beside drawing, cancelled superscript of initial Gamma_3',
        r"\Gamma_3^{\deleted{\unsure{\circ|'}}}", r'\Gamma^{*}_3',
        r'\Gamma_3^{\deleted{\circ}}',
        True, True, True, 'deletion state (struck given live or live given struck)',
        'The enlarged sign retains a round white centre and is crossed by a vertical/oblique dark stroke extending above it. This supports a cancelled circlet; it is not a live star, and a lone prime does not account for the surviving loop.',
        '07_side_identity.png', confidence='medium')
finding('Identity beside drawing, second double-primed Gamma subscript',
        r"\Gamma''_{\unsure{2|1}}", r"\Gamma''_2",
        r"\Gamma''_{\unsure{2|1}}",
        False, True, True, 'misread symbol or index',
        'The very heavy digit has an arched upper opening at the left and a broad foot. This favours 2, but the dark upright and large two-sided base leave 1 possible. The crop does not warrant removing the doubt.',
        '07_side_identity.png', confidence='low', unresolved=True, consequential=True)
finding('Last loose line, detached mark before U',
        r'\unsure{\cdot}\ U,C,V', r'U, C, V', r'\cdot\ U,C,V',
        True, True, True, 'omission',
        'Half a clearly shows a small detached ink mark immediately to the left of U. It is not attached to U and no corresponding closing sign follows V. A dot records the visible mark without assigning a further mathematical function.',
        confidence='medium')
finding('Lower formula line, unfinished expression to the right of dotted U relation',
        r'U_3\cup', r'U_3 \cup', r'U_3\cup',
        False, False, True, 'other',
        'Half a shows U_3 followed by a cup and then blank space. Half b adds no continuation. The expression is unfinished as C says; no operand is supplied.', confidence='high')
for row in (1, 2, 3):
    finding(f'Top verbal entries, H semicolon between middle and right blocks in row {row}',
            '', ';', '', False, True, False, 'text not on the page',
            'Half a shows distinct spatial blocks with blank space between the middle statement and the right statement. No semicolon is written there. H introduces a semicolon while linearising the table.')
finding('Lower formula line, H semicolon between the dotted-U identity and unfinished expression',
        r'\dot U_3=\Gamma_3\qquad U_3\cup',
        r'$\dot{U}_3 = \Gamma_3$ ; $U_3 \cup$',
        r'\dot U_3=\Gamma_3\qquad U_3\cup',
        False, True, False, 'text not on the page',
        'Half a shows a large blank gap after Gamma_3, then U_3 cup. There is no semicolon in the ink.')
finding('Drawing orientation relative to surrounding horizontal formulas',
        r'\begin{scope}[rotate=90]', r'\begin{tikzpicture}[x=1mm,y=1mm,line cap=round,line join=round,font=\scriptsize]',
        r'\begin{scope}[rotate=90]',
        False, True, False, 'drawing or diagram',
        'The whole page and half a show the drawing labels turned counterclockwise relative to the surrounding formulas. The one clockwise-rotated crop makes them upright. H redraws upright; the reading retains the source quarter-turn, as C does.',
        '06_drawing.png', confidence='high')
finding('Placement of endpoint-set definition',
        r'\[\partial=\{\unsure{x},y\}\]',
        r'\qquad \partial = \{x, y\}',
        r'\noindent\begin{minipage}[t]{.35\linewidth}\[\partial=\{\unsure{x},y\}\]\end{minipage}',
        True, True, False, 'insertion or placement',
        'Half a puts this short definition below the left three-column block and to the left of the following long equalities. It is not on the table baseline (H) and is not centred across the full page (C). The minipage keeps it in the left block.')

# Python juxtaposition of raw literals is avoided in these exact TeX witness fields:
# replace the few apostrophe-sensitive expressions explicitly from double-quoted strings.
replacements = {
    5: (r"\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}''_1", r"\Gamma''_1", r"\overset{\deleted{\unsure{\circ|\bullet}}}{\Gamma}''_1"),
    6: (r"\overset{\deleted{\circ}}{\Gamma}''_2", r"\Gamma''_2", r"\overset{\deleted{\circ}}{\Gamma}''_2"),
    7: (r"\overset{\deleted{\circ}}{\Gamma}''_3", r"\Gamma''_3", r"\overset{\deleted{\circ}}{\Gamma}''_3"),
    8: (r"\Gamma'_1-\unsure{\partial|\delta}", r"\Gamma'_1 - \partial", r"\Gamma'_1-\partial"),
    11: (r"\Gamma'_{\unsure{2|1}}", r"\Gamma'_2", r"\Gamma'_2"),
    12: (r"\Gamma''_1\cup\Gamma''_2\cup\partial", r"\Gamma''_1 \cup \Gamma''_2 \cup \partial", r"\Gamma''_1\cup\Gamma''_2\cup\partial"),
    14: (r"\Gamma'_{\unsure{2}}", r"\Gamma'_2", r"\Gamma'_2"),
    17: (r"\Gamma_3^{\deleted{\unsure{\circ|'}}}", r"\Gamma^{*}_3", r"\Gamma_3^{\deleted{\circ}}"),
    18: (r"\Gamma''_{\unsure{2|1}}", r"\Gamma''_2", r"\Gamma''_{\unsure{2|1}}"),
}
for n, exact in replacements.items():
    for k, v in zip(('c', 'h', 'reading'), exact):
        findings[n-1][k] = v

inventory_specs = [
    ('display', 'top left, three columns', r"V_1,V_2,V_3; \Gamma''_i; \Gamma'_i-\partial"),
    ('deletion', 'top left, over first Gamma', r'\deleted{\unsure{\circ|\bullet}}'),
    ('deletion', 'top left, over second Gamma', r'\deleted{\circ}'),
    ('deletion', 'top left, over third Gamma', r'\deleted{\circ}'),
    ('text', 'top middle, first row', r"V_1 borde \Gamma'_2,\Gamma'_3"),
    ('text', 'top middle, second row', r"V_2 borde \Gamma'_3,\Gamma'_1"),
    ('text', 'top middle, third row', r"V_3 borde \Gamma'_1,\Gamma'_2"),
    ('text', 'top right, first row', r"\Gamma'_1 bordé par V_2,V_3"),
    ('text', 'top right, second row', r"\Gamma'_2 --- V_3,V_1"),
    ('text', 'top right, third row', r"\Gamma'_3 --- V_1,V_2"),
    ('display', 'under left table', r'\partial=\{\unsure{x},y\}'),
    ('display', 'upper middle right, first long equality', r'\Gamma_{\unsure{2|1}}=\Gamma_2\cup\Gamma_3'),
    ('display', 'upper middle right, second long equality', r'\Gamma_2=\Gamma_3\cup\Gamma_1'),
    ('display', 'upper middle right, third long equality', r'\Gamma_3=\Gamma_1\cup\Gamma_2'),
    ('drawing', 'middle left, quarter-turned labels', r"\Gamma'_1,\Gamma'_2,\Gamma'_3,x,y; three arcs, loop, four oblique strokes and two dotted returns"),
    ('deletion', 'inside small loop, to right of common endpoint when upright', r'\deleted{\unsure{x|\partial}}'),
    ('display', 'beside drawing, first compartment', r"\Gamma_3^{\deleted{\circ}}=\Gamma''_1\cup\Gamma''_{\unsure{2|1}}\cup\partial"),
    ('deletion', 'superscript of Gamma_3 in first compartment', r'\deleted{\circ}'),
    ('display', 'beside drawing, middle compartment', r"U_3=V_1\cup V_2\cup\Gamma''_3"),
    ('display', 'beside drawing, final compartment', r'V_3'),
    ('display', 'below three-compartment row, left', r'\dot U_3=\Gamma_3'),
    ('display', 'below three-compartment row, right', r'U_3\cup'),
    ('display', 'last loose line above fold', r'\cdot\ U,C,V'),
    ('text', 'bottom left, archive pencil numbering', '2; preserved as a source comment only'),
]
inventory = [dict(scan=3, sheet_kind='text', hand='his hand' if i < 24 else 'another unnamed hand',
                  element=f'003-{i:02d}', kind=kind, position=pos,
                  first_words_or_objects=words, transcribed='yes')
             for i, (kind, pos, words) in enumerate(inventory_specs, 1)]

crop_observations = [
    'Read borde; a single terminal turn follows d, with no separate additional s.',
    'All three overmarks are cancellations. First original sign remains circlet/point; subsequent instances are the same recurrent ambiguity.',
    'Read partial and braces/comma/y clearly; tiny first letter remains uncertain x.',
    'Leftmost digit remains 2/1, best 2 to this reader. First primed subscript read 2. Last two subscripts are clearly 1 and 2 and retained.',
    'Detached dot is real, but its role as a dot accent versus broken opening of partial is unresolved; prefer plain partial.',
    'Turned clockwise. Outer right label is Gamma prime 2; other labels are Gamma prime 1 and 3, and y. Small x-like label remains uncertain by recurrence; adjacent overwritten mark remains x/partial. Four long oblique strokes, two dotted returns, and small endpoint loop were read.',
    'The cancelled superscript preserves a circle; prime-only and live star readings rejected. Heavy second double-primed subscript remains 2/1.',
]
crops = json.loads((ROOT / 'crop_log.json').read_text())
for c, observed in zip(crops, crop_observations):
    c['observed'] = observed

report = dict(
    scan=3, reader='R1', model='inherited parent model',
    effort='inherited; value not independently exposed',
    started_utc='2026-11-19T21:59:56Z', finished_utc=datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    images_viewed=[SOURCE + 'J71-01_71_scan003.jpg', SOURCE + 'J71-01_71_scan003_a.jpg', SOURCE + 'J71-01_71_scan003_b.jpg'],
    crops=crops, findings=findings, inventory=inventory,
    doubts=[
        dict(place='Top three cancelled overmarks, marked at first instance', reading=r'\circ', alternatives=r'\bullet', confidence='low', reason='Heavy re-inking leaves only partial loop evidence; all three are cancelled.'),
        dict(place='First endpoint-set element; repeated inside drawing loop', reading='x', alternatives='', confidence='low', reason='Very small bent, partially closed form; no further letter is secure enough to propose.'),
        dict(place='First long identity, leftmost subscript', reading='2', alternatives='1', confidence='low', reason='Arched head and broad baseline suggest 2 but also admit a serifed 1.'),
        dict(place='Second identity, terminal boundary sign', reading=r'\partial', alternatives=r'\dot\partial', confidence='low', reason='Detached point could be a separate dot or a disconnected part of the boundary sign.'),
        dict(place='Drawing, overwritten mark inside endpoint loop', reading='x', alternatives=r'\partial', confidence='low', reason='Filled centre and short curved tail do not reveal the original shape.'),
        dict(place='Side identity, second double-primed subscript', reading='2', alternatives='1', confidence='low', reason='Very heavy head, upright and wide base obscure the numeral shape.'),
    ],
    notes=[
        'The page is a handwritten mathematical working sheet. The upper left has three columns headed V_1,V_2,V_3, followed by double-primed Gamma entries with cancelled overmarks, upright pairs of equality-like strokes, and the single-primed Gamma minus the endpoint sign.',
        'The middle and right verbal blocks record the three cyclic border relations, with borde and bordé par. Horizontal strokes repeat the reciprocal wording in the second and third rows.',
        'The endpoint sign is defined below the left block as the two-element set {x,y}, with the first letter still uncertain in this reading.',
        'Three long union equalities follow. Every unprimed Gamma in their initial parts was read against the ink: the initial operands really lack primes. The first left subscript remains uncertain 2/1 to R1, and the first final pair is visibly double-prime 1 and double-prime 2, not silently made cyclic.',
        'The drawing has three arcs with common endpoints and two adjoining rounded regions. A small loop surrounds one endpoint. Four long oblique strokes cross the regions; two shorter dotted return arcs are also present. Labels read upright with a clockwise quarter turn. The drawing includes a tiny live x-like label and an overwritten mark, as well as y.',
        'Beside the drawing, vertical separators divide the Gamma_3 expression, U_3 = V_1 union V_2 union Gamma double-prime 3, and V_3. A circlet at the first Gamma is cancelled. The second double-primed subscript is heavily inked and remains 2/1.',
        'Below is dotted U_3 = Gamma_3, followed separately by the unfinished U_3 cup. The last loose line is a detached dot and U,C,V.',
        'The lower half is blank apart from the overlapping top edge of the last loose line, small nonlinguistic specks and a pencil 2 at bottom left. The 2 is treated as the archive sheet number, not an established authorial page number.',
        'S.json is empty. There are no S draft readings to decide.',
        'The whole image was viewed once, then each supplied half once in order. Seven crops were made with PIL, each viewed once. No OCR, external source, other page, or other reader directory was consulted. C and H were read as witnesses, and H drawing comments were distinguished from its actual drawn contents.',
        'The H note referring to another page was not used as evidence and no other page was inspected. No source date, title, or written self-doubt is present on this sheet.',
    ],
    checks=[
        dict(statement_id='003-table-relations', type='carried as background without fault found', statement=r"\Gamma''_i=\Gamma'_i-\partial and the three cyclic border relations", outcome='Transcribed and compared with the drawing, but no general mathematical proof of these border statements was attempted. Equality-like upright strokes in the table were not silently converted to additional assumptions.'),
        dict(statement_id='003-endpoint-definition', type='carried as background without fault found', statement=r'\partial=\{x,y\}', outcome='Treated as a definition on the page; x is a paleographic uncertainty. No cardinality or topological claim was independently proved.'),
        dict(statement_id='003-first-final-pair', type='targeted proof check', statement=r"\Gamma'_2\cup\Gamma'_3=\Gamma''_1\cup\Gamma''_2\cup\partial", outcome=r"Conditional on the endpoint interpretation drawn here, namely each \Gamma'_i=\Gamma''_i\cup\partial with the open arc interiors distinct, substitution gives \Gamma''_2\cup\Gamma''_3\cup\partial for the left side. The written right side instead uses interiors 1 and 2. Thus the final pair fails that local cyclic consistency check. This is a mathematical discrepancy, not authority to change the visible 1,2."),
        dict(statement_id='003-three-unprimed-unions', type='carried as background without fault found', statement=r'Initial unprimed-Gamma portions of the three long identities', outcome='The missing accents are source readings, not a claim that the resulting identities have been verified. No definitions from other pages were imported and no repair was made.'),
        dict(statement_id='003-side-U3', type='carried as background without fault found', statement=r"U_3=V_1\cup V_2\cup\Gamma''_3", outcome='Carried as the page assertion. The local picture makes the intended gluing understandable, but no topological theorem was independently established.'),
        dict(statement_id='003-dotted-U3', type='carried as background without fault found', statement=r'\dot U_3=\Gamma_3', outcome='Read the heavy separated dot above U. The meaning of dotted U is not defined on this page, so the equality was not independently proved.'),
    ],
    notation=[
        dict(sign='Angular capital with single/double upper ticks', tex=r"\Gamma_i,\Gamma'_i,\Gamma''_i", place='Table, long identities and drawing', ink='Angular top bar and downstroke, sometimes retraced into a hollow-looking vertical; no blackboard-bold alphabet inferred.', alternatives=''),
        dict(sign='Cancelled small overmark', tex=r'\deleted{\unsure{\circ|\bullet}}', place='First marked instance above Gamma double-prime 1; repeats above 2 and 3', ink='Worked-over small loop/point. Later repetitions carry the first-instance uncertainty.', alternatives=r'\circ|\bullet'),
        dict(sign='Upright doubled strokes', tex=r'\shortparallel', place='Between the second and third rows of each left table column', ink='Two short vertical strokes; third pair partly joined.', alternatives=''),
        dict(sign='Boundary sign', tex=r'\partial', place='First subtraction and endpoint definition', ink='Upper hook descending into a low loop. One later occurrence has a detached upper mark.', alternatives=r'\dot\partial at the second identity only'),
        dict(sign='Tiny repeated endpoint letter', tex=r'\unsure{x}', place='First set element; repeated inside drawing loop without a repeated uncertainty marker', ink='Short upper stroke with a bent thick right part, small enough to leave identity unsettled.', alternatives='No secure second letter reading'),
        dict(sign='Border wording and repeat stroke', tex=r'\text{borde};\ \text{bordé par};\ \text{---}', place='Middle/right top blocks', ink='Three borde entries; right first row has a detached acute; right lower rows use long horizontal repeat strokes.', alternatives=''),
        dict(sign='Dotted U and V', tex=r'U,V,\dot U_3', place='Beside and below drawing; last line', ink='U has a rounded low turn and rising right side; V remains angular. Dot above the lower U is separate and heavy.', alternatives=''),
        dict(sign='Cancelled circlet beside drawing', tex=r'\Gamma_3^{\deleted{\circ}}', place='First compartment beside drawing', ink='Small circular centre crossed by a tall stroke. It is cancelled, not a live asterisk.', alternatives=''),
    ],
    abbreviations=[],
    brief_feedback=[
        'The one-crop-per-place rule is workable if a compact drawing, or a single formula containing two unsettled subscripts, counts as one place. I used one crop for each such compact block and did not crop or view any of those places again.',
        'The brief specifies tikzcd for diagrams, but this page has a table without arrows. I kept the already available array inside the diagram macro, preserving its actual column layout, rather than inventing diagram arrows.',
    ],
)
(ROOT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2) + '\n')
print(f'Wrote {len(findings)} findings, {len(inventory)} inventory elements, {len(crops)} crops.')
