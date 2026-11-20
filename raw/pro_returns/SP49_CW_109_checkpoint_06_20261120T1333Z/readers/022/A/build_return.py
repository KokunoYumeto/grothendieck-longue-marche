from pathlib import Path
import json, csv, re, difflib

ROOT = Path('work/readers/022/A')
INPUT = Path('work/inputs/022')
SOURCE = '/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-02_109_scan022.jpg'
HALF_A = SOURCE.replace('.jpg', '_a.jpg')
HALF_B = SOURCE.replace('.jpg', '_b.jpg')
original = (INPUT / 'C.tex').read_text()
reading = original
changes = []

def crop(name):
    return str((ROOT / 'crops' / (name + '.jpg')).resolve())

def change(id, place, old, new, kind, evidence, box, name=None, confidence='high', source=SOURCE):
    global reading
    assert old in original, (id, 'not literal C', old)
    assert reading.count(old) == 1, (id, 'ambiguous replacement', reading.count(old))
    reading = reading.replace(old, new, 1)
    changes.append(dict(id=id, place=place, c=old, h=None, reading=new, diff_c=True, diff_h=False,
                        kind=kind, marked_in_H=False, confidence=confidence, evidence=evidence,
                        crop=crop(name) if name else None, source=source, bbox=box))

change('first-inclusion', 'p.116 line -6, first inclusion and the low quotation pair',
       r"p.116 line -6, $\unsure{R|K}_{\unsure{h|n}}\subset R_n$'' should be $R_h\subset\Sigma_h$.",
       r"p.116 line -6, $\unsure{R|K}_h\subset\unsure{R|K}_n$\raisebox{-1.1ex}{\unsure{''}} should be $R_h\subset\Sigma_h$.",
       'misread symbol or index',
       'The first subscript has a tall upright and a separate low arch, deciding h. Each of the first two capitals has a faint upper contour, independently insufficient to exclude K; the second therefore also receives its own R/K mark. The visible quotation pair stands below and just to the right of the second subscript. Its two strokes are certain, but whether it belongs to this inclusion or opens the next commutation line remains uncertain; it is drawn low at its physical position and marked. The replacement R, both single inclusion signs, Sigma and final period are retained.',
       [402, 78, 1119, 160], '01_formula', 'medium')

change('commutation-opener', 'p117 line 11 & 12, before commutation',
       r"p117 line 11 \& 12, ``commutation .... with.''",
       r"p117 line 11 \& 12, commutation .... with.''",
       'text not on the page',
       'There is only one quotation pair at the boundary of the first two entries: the low pair recorded after the first inclusion. No second, independent pair occurs immediately before commutation. C represents two pairs. Four low marks between commutation and with, the period after with, and the closing pair are all visible and retained. Attribution of the one boundary pair is explicitly left doubtful.',
       [541, 134, 1025, 199], '02_p117_punctuation', 'medium')

old_margin = r"\margin{\deleted{\unsure{?} \unsure{*} p122 \unsure{?}}}"
new_margin = r"""\reversemarginpar
\margin{\tikz[baseline=(cancelref.base)]{
\node[inner sep=0pt](cancelref){\deleted{\unsure{?} \unsure{*} p122 \unsure{?}}};
\draw[line width=.45pt] ([xshift=-.25em,yshift=-.35ex]cancelref.west) -- ([xshift=.25em,yshift=.15ex]cancelref.east);
\draw[line width=.45pt] ([xshift=-.35em,yshift=-.6ex]cancelref.west) -- ([xshift=.05em,yshift=.45ex]cancelref.east);
\draw[line width=.35pt] ([xshift=.65em,yshift=-.75ex]cancelref.west) -- ([xshift=-.1em,yshift=-.15ex]cancelref.east);
}}
\normalmarginpar"""
change('cancelled-margin-geometry', 'cancelled marginal reference left of p.123', old_margin, new_margin,
       'drawing or diagram',
       'The crossed reference is physically left of p.123. Several long, nonparallel strike strokes extend across and beyond the cancelled group, including a lower rising return stroke. The left placement and additional line paths are encoded, while the three uncertain symbols remain uncertain. The outer cancellation extent is clear even though its interior symbols are not.',
       [61, 516, 369, 587], '04_margin_cancel')

change('p132-single-opener', 'p132 line -14, opening quotation',
       "p132 line -14 ``wasn't''", "p132 line -14 `wasn't''",
       'misread symbol or index',
       'The crop shows exactly one isolated curved opening stroke, with blank paper beside it; the closer consists of two distinct strokes. The apostrophe follows n.',
       [530, 841, 705, 890], '07_p132_quote')

change('p146-or', 'p.146 line -1, connector between contractions',
       r"``doesn't \unsure{or} shouldn't''", r"``doesn't or shouldn't''",
       'misread word',
       'The crop separates a closed left o from a narrow right stem/shoulder and its long rightward exit. The heavy junction does not obscure the two letter forms sufficiently to retain the word-level doubt.',
       [1156, 1370, 1208, 1408], '11_p146_or', 'medium')

change('p147-low-mark', '147 line 20, punctuation after the reference',
       "line 20 ``with' not to''", r"line 20\unsure{.|,} ``with' not to''",
       'omission',
       'A small dark low stroke is present after 20, separate from the high arched opening quote. Its low position and compact body support a period, but a short comma is not excluded. The high opener and single closer after with are retained as independently written marks.',
       [535, 1479, 570, 1526], '14_p147_with_quote', 'medium')

change('p149-opener', '149. before line 7',
       r"149. \unsure{``}line 7", "149. ``line 7",
       'misread symbol or index',
       'The lower half clearly separates two short upright strokes immediately before the large l of line. No crop was needed after the half settled the pair.',
       [348, 502, 380, 543], None, 'high', HALF_B)

change('circled151-angle', 'circled 151 at the end of the long left arrow',
       r"\draw (n.center) ellipse[x radius=1.04em,y radius=.67em];",
       r"\draw[rotate around={32:(n.center)}] (n.center) ellipse[x radius=1.04em,y radius=.67em];",
       'drawing or diagram',
       'The enclosing oval rises to the right around 151. The arrow bends down the left margin from the earlier p.151 entry and terminates at this oval. The existing arrow path is retained; the oval angle is made explicit.',
       [127, 639, 231, 884], None, 'high', HALF_B)

change('p151-trailing-fragment', 'circled 151, after the cancelled we will fragment at right',
       r"\unsure{in|n} in $(2)$", r"\unsure{n|in} in $(2)$",
       'misread word',
       'The uncancelled right-hand remainder shows one left upright and one low arch; no detached dot or securely separate i is visible. n is the preferred visual reading, with joined in still allowed. The separate next-line in (2) is unaffected.',
       [1518, 1958, 1556, 1989], '17_p151_right_deletions', 'low')

old_ns = r"\deleted{\unsure{n \&}}"
new_ns = r"""\tikz[baseline=(oldns.base)]{
\node[inner sep=0pt](oldns){\deleted{\unsure{n \&}}};
\draw[line width=.35pt] ([xshift=.65em,yshift=1.05ex]oldns.base west) -- ([xshift=.61em,yshift=.66ex]oldns.base west);
\draw[line width=.35pt] ([xshift=.83em,yshift=1.06ex]oldns.base west) -- ([xshift=.85em,yshift=.67ex]oldns.base west);
}"""
change('p153-cancelled-raised-strokes', 'p.153, cancelled short fragment after handy', old_ns, new_ns,
       'drawing or diagram',
       'Two short raised strokes survive above the right portion of the cancelled fragment. Their attribution as quotes or remnants of the struck form is uncertain, so their shapes are drawn without inventing extra letters. The surviving left hump and right crossed lobe do not independently decide the fragment n &; C’s uncertainty is retained.',
       [1195, 2063, 1257, 2114], '19_p153_n_s', 'medium')

old_s = r"\unsure{\uline{s}|S}"
new_s = r"""\tikz[baseline=(finals.base)]{
\node[inner sep=0pt](finals){\unsure{\uline{s}|S|$s_1$}};
\draw[line width=.35pt] ([xshift=.42em,yshift=-.7ex]finals.base west) -- ([xshift=.45em,yshift=-2.05ex]finals.base west);
}"""
change('p153-s-tail', 'p.153, final live s-like sign', old_s, new_s,
       'misread symbol or index',
       'The s-shaped body is followed below by a short leftward hook and a distinct long descending vertical. A simple underline does not account for that vertical. It is reproduced as a line; underlined lowercase s, capital S with an added stroke, and s with a low 1 remain possible. Case and subscript interpretation are not inferred from the wordplay.',
       [1326, 2065, 1361, 2123], '19_p153_n_s', 'low')

change('p154-allo-and-opener', 'p154 line 9, cancelled beginning and live will',
       r"p154 line 9 \deleted{\unsure{allo}} ``will even allow us to handle''",
       r"p154 line 9 \deleted{allo} will even allow us to handle''",
       'misread word',
       'The cancelled beginning independently shows an a bowl, two tall looped l strokes and a final closed o, resolving allo. There is no separate opening pair between that cancelled beginning and will: the strokes high above that gap belong to the preceding developed descender, visible in the lower half. The closing pair after handle is retained. The absent opener is not supplied from the surrounding quotation pattern.',
       [557, 2110, 734, 2177], '20_p154_allo', 'medium')

change('p154-final-cancelled-word', 'p154 line -6, final crossed short word',
       r"\deleted{\unsure{it}}", r"\deleted{\unsure{to|it}}",
       'misread word',
       'A tall stem with a crossbar and a right-hand closed oval survive the crossing, favouring to. The heavy overlap still admits it, so no certain replacement word is asserted. The complete short group is cancelled.',
       [1183, 2195, 1230, 2237], '21_p154_final_cancel', 'low')

change('p154-final-quotes', 'p154 line -2, quotation marks around standard',
       "line -2 ``standard''", r"line -2 \unsure{``|`}standard\unsure{''|'}",
       'misread symbol or index',
       'The opener is a joined loop plus upright, and the closer is one long upright with a short attached branch. Each could be a fused pair, but neither independently separates into two certain strokes. Both occurrences are therefore marked, independently, rather than borrowing certainty from other quotation pairs.',
       [576, 2235, 752, 2297], '22_p154_standard_quotes', 'medium')

# Position-only anchor syntax supports the drawn page marks; it supplies no text.
reading = reading.replace(r'\scanpage{22}', r'\scanpage{22}' + '\n' + r'\tikz[remember picture,overlay]\coordinate (scxxiitop);', 1)
reading = reading.replace(r'p.121 line -17', r'\tikz[remember picture,overlay]\coordinate (scxxiiendows);p.121 line -17', 1)

drawings = [
    ('left-rule', 'long left vertical rule',
     r'\draw[line width=.25pt,opacity=.7] ([xshift=.35em,yshift=1.8ex]scxxiitop) -- ([xshift=.35em,yshift=-1ex]scxxiibottom);',
     [211, 86, 231, 2316], None,
     'The left rule runs from the first entry to below the final entries, passing through the reference column. It is retained as a line, without assigning editorial meaning.'),
    ('right-rule', 'long right vertical rule',
     r'\draw[line width=.25pt,opacity=.7] ([xshift=.97\linewidth,yshift=1.9ex]scxxiitop) -- ([xshift=.97\linewidth,yshift=-1ex]scxxiibottom);',
     [1490, 83, 1511, 2316], None,
     'A second long straight rule stands near the right edge and passes through portions of longer text lines. Its line geometry is absent from literal C.'),
    ('far-left-trace', 'short faint trace at the far left of the upper block',
     r'\draw[line width=.2pt,opacity=.4] ([xshift=-1.6em,yshift=.5ex]scxxiitop) -- ([xshift=-1.6em,yshift=.7ex]scxxiiendows);',
     [34, 107, 69, 496], '24_far_left_trace',
     'The rotated crop shows a narrow, nearly straight, intermittently dark trace. It is reproduced as observed; the image does not establish whether it is an intentional rule or a reproduction/paper trace.'),
    ('upper-left-ring', 'faint oval trace left of the opening entries',
     r'''\begin{scope}[shift={([xshift=-.55em,yshift=-1.8ex]scxxiitop)}]
\draw[line width=.2pt,opacity=.3] (.35em,.65ex) .. controls (-.4em,1.05ex) and (-.7em,-.1ex) .. (-.35em,-.7ex) .. controls (.1em,-1.1ex) and (.7em,-.45ex) .. (.6em,.15ex);
\draw[line width=.3pt,opacity=.7] (-.48em,.2ex) -- (-.48em,-.2ex);
\draw[line width=.15pt,opacity=.3] (-.05em,.95ex) -- (.2em,.95ex);
\end{scope}''',
     [95, 105, 179, 174], '23_upper_left_ring',
     'The crop shows a faint broken oval, a short dark left arc, and a faint short stroke above it. There is no readable word or numeral. Its physical/ink origin remains unassigned.'),
    ('lower-left-mark', 'small dark mark near the foot of the left rule',
     r'''\begin{scope}[shift={([xshift=.35em,yshift=.5ex]scxxiibottom)}]
\draw[line width=.55pt] (-.13em,.25ex) .. controls (-.01em,.08ex) and (.04em,.2ex) .. (.14em,-.06ex);
\draw[line width=.35pt] (.04em,.35ex) -- (.06em,-.45ex);
\end{scope}''',
     [193, 2233, 238, 2288], '25_bottom_left_mark',
     'The enlargement shows a small dark crossing/irregular stroke on the faint vertical rule. No alphanumeric value is assigned; its visible shape is retained.')
]
for id, place, code, box, name, evidence in drawings:
    changes.append(dict(id=id, place=place, c='', h=None, reading=code, diff_c=True, diff_h=False,
                        kind='drawing or diagram', marked_in_H=False, confidence='high' if name is None else 'medium',
                        evidence=evidence, crop=crop(name) if name else None, source=SOURCE, bbox=box))
overlay = '\n\n' + r'\tikz[remember picture,overlay]\coordinate (scxxiibottom);' + '\n'
overlay += r'\figure{\begin{tikzpicture}[remember picture,overlay]' + '\n'
for id, place, code, *_ in drawings:
    overlay += '% ' + id + ': ' + place + '\n' + code + '\n'
overlay += r'\end{tikzpicture}}' + '\n'
reading = reading.replace('\n% archive sheet number: 21', overlay + '\n% archive sheet number: 21', 1)
(ROOT / 'reading.tex').write_text(reading)

c_doubts = []
remaining = []
def doubt(place, c, proposed, resolved, evidence, box, name=None, confidence='medium', source=SOURCE, alternatives=None):
    c_doubts.append(dict(place=place, c=c, reading=proposed, resolved=resolved, confidence=confidence,
                         evidence=evidence, crop=crop(name) if name else None, source=source, bbox=box))
    if not resolved:
        remaining.append(dict(place=place, reading=proposed, alternatives=alternatives or proposed,
                              confidence=confidence, reason=evidence, crop=crop(name) if name else None,
                              source=source, bbox=box))

doubt('p.116 first capital', r'\unsure{R|K}', r'\unsure{R|K}', False,
      'A pale upper arc favours R, but its closure at the stem is not independently secure. The later clear R is not used to settle this occurrence.', [404,76,446,145], '01_formula', alternatives='R or K')
doubt('p.116 first subscript', r'\unsure{h|n}', 'h', True,
      'The left stroke rises clearly above the low right arch; this is h, not a short n.', [421,111,451,150], '01_formula', 'high')
doubt('p.116 second capital, context alternative', 'R_n', r'\unsure{R|K}_n', False,
      'Its upper curve is pale and incomplete independently of the first and third capitals. The context explicitly raises K here; uncertainty is now marked at this occurrence.', [518,76,562,144], '01_formula', alternatives='R or K; the low n is clear')
doubt('p.116 replacement capital', 'R_h', 'R_h', True,
      'The replacement capital has a closed upper bowl and separate lower diagonal leg. Its looped lowered h is visible.', [882,76,939,155], '01_formula', 'high')
doubt('p.116 replacement Sigma', r'\Sigma_h', r'\Sigma_h', True,
      'The angular upper, diagonal and lower strokes form Sigma; the final h has its own lowered loop and arch.', [1008,77,1091,163], '01_formula', 'high')
doubt('p.116 inclusion signs', r'\subset', r'\subset', True,
      'Both are single open-right arcs; no separate equality bar appears beneath either.', [458,86,1000,137], '01_formula', 'high')
doubt('p.116/p117 boundary quotation pair', "R_n$''", r"\raisebox{-1.1ex}{\unsure{''}}", False,
      'Two strokes are visible low beside n and above-left of commutation. Their quotation shape is clear, but their attribution to one of those two lines is not. Only this one pair is transcribed; no second pair is invented before commutation.', [560,132,585,162], '01_formula', alternatives='Closing pair after the first inclusion, or opening pair for commutation; one physical pair only')
doubt('p114 & 115 section signs', r'\S52 intended rather than \S51.', r'\S52 intended rather than \S51.', True,
      'Each sign has the double curved profile, and the following digits are 52 and 51.', [944,397,1546,461], None, 'high', HALF_A)
doubt('142 line 15 formula', r's_1=\delta_0', r's_1=\delta_0', True,
      'The first body is s-shaped, its 1 is low; the second body has the delta loop and a low 0. Two equality strokes and the terminal period are visible. This is an ink decision, not a mathematical proof.', [601,188,785,249], None, 'high', HALF_B)
doubt('circled 151 final hat', r'\widehat{A}', r'\widehat{A}', True,
      'Two oblique strokes form a roof above the A; the hat is separate from the letter.', [558,878,611,936], None, 'high', HALF_B)
doubt('p.119 line 14 underline of one', r'\uuline{one}', r'\uuline{one}', True,
      'Two distinct horizontal strokes lie beneath one, including a shorter returned upper stroke.', [589,358,663,406], None, 'high', HALF_A)
doubt('cancelled p122 reference, leading symbol', r'\unsure{?}', r'\unsure{?}', False,
      'A large upper hook survives, but any lower dot is covered by the crossing strokes. The cancelled extent includes the symbol.', [80,517,117,575], '04_margin_cancel', 'low', alternatives='Question-mark-like hook; no secure alternative letter')
doubt('cancelled p122 reference, star-like symbol', r'\unsure{*}', r'\unsure{*}', False,
      'Several intersecting strokes survive between the hook and p. The cancellation prevents separating all of the star arms.', [121,530,151,580], '04_margin_cancel', 'low', alternatives='Asterisk-like mark; exact arms unclear')
doubt('cancelled p122 reference, trailing symbol', r'\unsure{?}', r'\unsure{?}', False,
      'A tall right hook and an interior upright survive, with their lower part entered by several strikes. Question mark remains a tentative reading.', [281,526,330,579], '04_margin_cancel', 'low', alternatives='Question-mark-like form; lower component obscured')
doubt('p.123 before line 9', r'\deleted{\unsure{l}}', r'\deleted{\unsure{l}}', False,
      'An extra looping upright overlaps the live initial l and a low strike. The old form may be l, but its independent contour is not fully recoverable.', [533,526,584,581], '05_p123_cancel', 'low', alternatives='Cancelled l-like start')
doubt('p128 old line number', r'\deleted{\unsure{16}}', r'\deleted{\unsure{16}}', False,
      'One upright and a low loop survive the crossing. The upper connection of the second digit is buried, so 16 remains tentative; no digit is supplied from another reference.', [372,719,409,763], '06_p128_cancel', 'low', alternatives='16 tentative; second digit not fully recoverable')
doubt('133 after handwritten', r'\unsure{?}', r'\unsure{?}', False,
      'The small curl immediately before the closing parenthesis has no securely detached lower dot. It is not resolved from the sentence meaning.', [706,906,734,949], '08_p133_question', 'low', alternatives='Question-mark-like curl')
doubt('p140 overwritten line number', r'\deleted{\unsure{3}}4', r'\deleted{\unsure{3}}4', False,
      'The new 4 is clear. An upper loop and middle curved remnant could be an old 3, but the shared strokes do not secure it.', [405,1167,449,1217], '09_p140_reference_quote', 'low', alternatives='Old 3 tentative; live 4 certain')
doubt('p.146 cancelled word', r'\deleted{\unsure{does}}', r'\deleted{\unsure{does}}', False,
      'A left bowl with a tall ascender and several later low loops support does, but the o/e/s boundaries remain crossed. The following live contraction is not used to resolve them.', [709,1359,800,1404], '10_p146_cancel', 'medium', alternatives='does tentative')
doubt('p.146 connector', r'\unsure{or}', 'or', True,
      'The left oval and right stem/shoulder with long exit can be read separately in the crop.', [1156,1370,1208,1408], '11_p146_or', 'medium')
doubt('147 cancelled start', r'\deleted{\unsure{st}}', r'\deleted{\unsure{st}}', False,
      'The right upright and crossbar support t; the left lower curl supports s, but its upper part is entered by the cancellation. The later standard is not used as evidence.', [350,1419,413,1467], '12_p147_cancel', 'low', alternatives='st tentative, with t more secure than s')
doubt('149 before line 7', r'\unsure{``}', '``', True,
      'The lower half separates two raised short strokes immediately before line.', [348,502,380,543], None, 'high', HALF_B)
doubt('p.152 line -9 cancelled word', r'\deleted{\unsure{allow}}', r'\deleted{\unsure{allow}}', False,
      'The initial bowl and two tall loops support all; the following low bodies are covered by several horizontal strokes. The final w is not independently clear enough to remove the whole-word doubt.', [1495,1803,1606,1857], '26_p152_allow', 'medium', alternatives='allow tentative; ending covered')
doubt('circled 151 overwritten ending of whereas', r'\deleted{\unsure{as}}', r'\deleted{\unsure{as}}', False,
      'Old and live loops intersect at the re/as boundary. The earlier two-letter reading as and its exact interior contours are not independently recoverable from the crossing; the live whereas is clear.', [477,1941,518,1979], '16_p151_whereas', 'low', alternatives='Cancelled as tentative; precise overlap at re/as boundary uncertain')
doubt('circled 151 cancelled start at right', r'\deleted{\unsure{If th}}', r'\deleted{\unsure{If th}}', False,
      'An I-like upright, a thin low remnant and a later t/h-like cluster survive. The horizontal and oblique crossings prevent a certain reading of the internal f and h.', [1287,1904,1401,1949], '17_p151_right_deletions', 'low', alternatives='If th tentative')
doubt('circled 151 cancelled fragment after target', r'\deleted{\unsure{of}}', r'\deleted{\unsure{of}}', False,
      'The far-right scribble contains a left loop and tall/low strokes compatible with of. They cannot be separated from the cancellation securely.', [1599,1904,1646,1975], '17_p151_right_deletions', 'low', alternatives='of tentative')
doubt('circled 151 cancelled work/write', r"\deleted{we'll \unsure{work|write}}", r"\deleted{we'll \unsure{work|write}}", False,
      'The old we apostrophe ll is legible. The later w and low oval favour work, but taller crossing strokes intersect the ending; write remains possible. Neither candidate is supplied as certain.', [1286,1940,1525,1997], '17_p151_right_deletions', 'low', alternatives='work or write')
doubt('circled 151 final uncancelled short fragment', r'\unsure{in|n}', r'\unsure{n|in}', False,
      'One upright and one arch are visible without a secure i dot. n is preferred, but a joined in remains possible. The crossing stops to its left.', [1518,1958,1556,1989], '17_p151_right_deletions', 'low', alternatives='n or in')
doubt('p.153 cancelled short fragment', r'\deleted{\unsure{n \&}}', r'\deleted{\unsure{n \&}}', False,
      'The left hump and right crossed lobe do not securely recover the letters. Two raised strokes are separately drawn. The subsequent live n & is not used to identify the cancelled fragment.', [1195,2063,1257,2114], '19_p153_n_s', 'low', alternatives='n & tentative; raised strokes have uncertain textual attribution')
doubt('p.153 final s-like sign', r'\unsure{\uline{s}|S}', r'\unsure{\uline{s}|S|$s_1$}', False,
      'The letter body does not settle case. The low hook and descending vertical might belong to an underline/pen tail or to a low 1; the vertical is explicitly drawn.', [1326,2065,1361,2123], '19_p153_n_s', 'low', alternatives='Underlined s; S with a pen tail; or s_1')
doubt('p154 line 9 cancelled beginning', r'\deleted{\unsure{allo}}', r'\deleted{allo}', True,
      'The crop independently preserves the first bowl, both tall looped l strokes and the final closed oval o.', [566,2120,634,2163], '20_p154_allo', 'high')
doubt('p154 line -6 final cancelled word', r'\deleted{\unsure{it}}', r'\deleted{\unsure{to|it}}', False,
      'The tall crossed stem followed by a right oval favours to; heavy shared strokes prevent excluding it. Cancellation of the entire short group is clear.', [1183,2195,1230,2237], '21_p154_final_cancel', 'low', alternatives='to or it')

remaining += [
    dict(place='147 line 20 low punctuation', reading=r'\unsure{.|,}', alternatives='period or short comma', confidence='medium', reason='The independent low dark stroke is compact but slightly elongated; its punctuation value is not decided by the high opening quotation.', crop=crop('14_p147_with_quote'), source=SOURCE, bbox=[535,1503,561,1527]),
    dict(place='p154 line -2 opening quotation', reading=r'\unsure{``|`}', alternatives='fused double or single opening quote', confidence='medium', reason='The joined loop and upright have no certain separation into two independent strokes.', crop=crop('22_p154_standard_quotes'), source=SOURCE, bbox=[575,2235,602,2263]),
    dict(place='p154 line -2 closing quotation', reading=r"\unsure{''|'}", alternatives='fused double or single closing quote', confidence='medium', reason='A long upright and short attached branch remain compatible with either reading.', crop=crop('22_p154_standard_quotes'), source=SOURCE, bbox=[731,2243,752,2267])
]

inventory = []
def inv(kind, position, first, hand='another unnamed hand'):
    inventory.append(dict(sheet_kind='list', hand=hand, element=f'{len(inventory)+1:02d}', kind=kind,
                          position=position, first_words_or_objects=first, transcribed='yes'))

inv('text','top, first entry','p.116 line -6; first inclusion, should be, replacement inclusion')
inv('text','top, second entry','p117 line 11 & 12; commutation .... with.')
inv('text','under p117','line -17; I\'d better assume ...')
inv('text','upper block','p.119 line 5; onto')
inv('insertion','boxed left of onto','not "unto"; physically left of the quoted onto')
inv('drawing','around not unto','rounded/open-topped enclosure')
inv('drawing','from boxed addition around to its right','curving rightward arrow ending beyond onto')
inv('text','upper block, following entry','line 14; allows one to')
inv('text','nested under one','two underline strokes beneath one')
inv('text','upper block, out-of-order page reference','p114 & 115 handwritten comment: is §52 intended rather than §51.')
inv('text','upper block','p.121 line -17; endows')
inv('margin note','left of p.123','? * p122 ?; symbols remain doubtful')
inv('deletion','same marginal note','entire ? * p122 ? group crossed')
inv('drawing','same marginal note','several long crossing and return strokes')
inv('text','upper-middle block','p.123 line 9; standard')
inv('deletion','at beginning of line in p.123 entry','extra l-like start')
inv('text','following row, left portion','line 13; with direct sums')
inv('text','same row, right portion','line -1; commutes with')
inv('text','upper-middle block','p.124 line 17; a long time ago')
inv('text','upper-middle block','p128 line -12; standard')
inv('deletion','before -12 in p128 reference','old 16-like number')
inv('text','upper-middle block, left portion','p131 line 16; commutes with')
inv('text','same row, right portion','line 18; it is')
inv('text','upper-middle block','p132 line -14; single opening quote, wasn\'t, double closer')
inv('text','middle block','133 line 13 (handwritten ?); commutes with, single closer')
inv('text','middle block','p.135 line 4; commas needed around ,of course,')
inv('text','middle block','137 line -13; wasn\'t')
inv('text','middle block, left portion','138 line -15; through')
inv('text','same row, right portion','line -5; standard')
inv('text','middle block','p140 line 4; commutes with,')
inv('deletion','under the 4 in p140 reference','old 3-like digit overwritten')
inv('text','middle block','141 line -1; standard')
inv('text','middle-lower block, left portion','142 line 15; s_1=delta_0.')
inv('text','same row, right portion','line -15; allow one to')
inv('text','middle-lower block, left portion','p.146 line -3; usual')
inv('deletion','between the p.146 corrections','does-like word crossed')
inv('text','same row, right portion','line -1; doesn\'t or shouldn\'t')
inv('text','middle-lower block','147 line 2; standard with single closer')
inv('deletion','after 147 and before line 2','st-like start crossed')
inv('text','same row, middle portion','line 10; commutes with')
inv('text','same row, right portion','line 18; doesn\'t')
inv('text','following row','line 20; low punctuation, with, not to')
inv('text','lower block, left portion','148 line 21; developed')
inv('text','same row, right portion','line -1.; standard. inside quotes')
inv('text','lower block, left portion','149. raised pair before line 7; standard')
inv('text','same row, right portion','line 12; isn\'t')
inv('text','lower block, left portion','p.151 line 8; isn\'t')
inv('text','same row, middle portion','line 17; a long time ago')
inv('text','same row and following line','line 18; putting off would be more usual.')
inv('drawing','left of p.151 and p.152 entries','long descending curved arrow from p.151 toward circled 151')
inv('text','lower block, left portion','p.152 line 17; developed.;')
inv('text','same row, middle portion','line -10.; lead to develop;')
inv('text','same row right, continuing below','line -9; which will allow us to define')
inv('deletion','right end of p.152 first physical row','allow-like word crossed; opening pair remains before it')
inv('drawing','left of the renewed line -4 entry','slanted oval around 151 at arrow endpoint')
inv('text','renewed circled 151 entry','line -4; whereas in the target category (Cat) of (2)')
inv('deletion','within whereas','old as-like loops underneath/reworked at the re/as boundary')
inv('text','right of the quoted category wording','the target; live fragment between cancellations')
inv('deletion','right-hand fragment, before the target','If th-like cancelled start')
inv('deletion','far right after target','of-like cancelled fragment')
inv('deletion','right-hand fragment second row','we\'ll work/write crossed, stopping before final n/in')
inv('text','right-hand fragment end','uncancelled n/in')
inv('text','next line of circled 151 entry','in (2) is hatted A.')
inv('text','bottom block, left portion','p.153 line 4; developed')
inv('deletion','same row after developed','quoted handiness, cancelled through the whole word')
inv('text','same row, right portion','handy, n & s-like sign, would be better')
inv('deletion','within handy phrase','n &-like cancelled fragment')
inv('drawing','above cancelled short fragment at p.153','two short raised strokes of uncertain textual attribution')
inv('drawing','below final live s-like sign at p.153','short low hook/underline and long descending stroke')
inv('text','bottom block','p154 line 9; will even allow us to handle, closing pair')
inv('deletion','before will at p154 line 9','allo, with all four letters readable under the strike')
inv('text','following row, left portion','line -9; don\'t')
inv('text','same row, right portion','line -6; wouldn\'t')
inv('deletion','after wouldn\'t','to/it-like short crossed word')
inv('text','last text row','line -2; standard with separately uncertain opener and closer')
inv('drawing','left of main reference column, nearly full page','long left vertical rule','unidentified line mark; hand not established')
inv('drawing','near right edge, nearly full page','long right vertical rule','unidentified line mark; hand not established')
inv('drawing','far-left upper block','short faint vertical trace','unidentified trace; physical/ink origin uncertain')
inv('drawing','upper-left beside opening entries','faint oval trace and small upper stroke','unidentified trace; physical/ink origin uncertain')
inv('drawing','near bottom of left vertical rule','small dark irregular crossing mark','unidentified trace; hand not established')
inv('text','lower-left corner, outside main correction list','archive sheet number 21, retained only as a TeX comment','archive annotation; hand not identified')

notes = [
    'English handwritten corrections cite pages 116–154, with a separate out-of-order reference to pages 114 & 115. Page and line references are preserved as written; this is not manuscript pagination.',
    'At p.116 line -6 the note gives an inclusion correction. The first two capitals remain R/K doubts independently; the first subscript is h. The replacement reads R_h subset Sigma_h. The isolated equality s_1=delta_0 occurs at 142 line 15.',
    'The p114 & 115 entry asks whether §52 is intended rather than §51 and ends with a period. The p117 entry quotes “I\'d better assume ...”.',
    'The p.119 entry has a boxed not unto insertion and a curving arrow beside onto; one in allows one to is doubly underlined.',
    'The earlier p.151 entry says putting off would be more usual. A long curved arrow leads to a separate circled 151 entry on the target category (Cat) of (2), with cancellations and the assertion in (2) is hatted A.',
    'The p.153 correction cancels the quoted word handiness and gives the handy n & s-like wording, followed by would be better. The last sign has an additional low descending stroke whose interpretation remains doubtful.',
    'No title, date, author signature, stated page count, or manuscript page number is visible. The corner 21 is recorded only as an archive-number comment.',
    'The page does not supply definitions of the sets, simplicial symbols or target category needed for a substantive proof check. No mathematical proof, counterexample or computation was performed from this page alone; math_checks is deliberately empty.'
]

notation = [
    dict(sign=r'\unsure{R|K}_h, \unsure{R|K}_n, R_h, \Sigma_h', location='p.116 line -6', reading='Two individually doubtful first capitals; clear replacement R and Sigma; lowered h/n/h/h.', evidence='Crop 01: pale first loops are independent uncertainties; replacement bowl and angular Sigma are clear.'),
    dict(sign=r'\subset', location='p.116 both occurrences', reading='single inclusion signs', evidence='Crop 01: open-right arcs with no second equality line.'),
    dict(sign=r's_1=\delta_0', location='142 line 15', reading='lowercase s with 1, equals, lowercase delta with 0', evidence='Half b: low digits, two equality strokes, closed delta loop.'),
    dict(sign=r'\widehat{A}', location='circled 151, final line', reading='A with a two-stroke hat', evidence='Half b: separate roof above the ordinary A.'),
    dict(sign=r'\S52; \S51', location='p114 & 115', reading='section signs', evidence='Half a: two linked curved portions in each sign.'),
    dict(sign=r'\uuline{one}', location='p.119 line 14', reading='double underline confined to one', evidence='Half a: two returned baseline strokes beneath one.'),
    dict(sign='quotation strokes', location='p132; 147 line 2; 147 line 20; p154 line -2', reading='Single opener at p132; single closer after standard at 147 line 2; single closer after with; two independently doubtful final quotes.', evidence='Crops 07, 13, 14 and 22 separately inspected; no general quotation rule applied.'),
    dict(sign='four low dots', location='p117 commutation entry', reading='....', evidence='Crop 02 shows four separate low dark groups, the last smaller and faint.'),
    dict(sign=r'\unsure{\uline{s}|S|$s_1$}', location='p.153 final live sign', reading='Case and subscript/underline interpretation unresolved; descending line explicitly drawn.', evidence='Crop 19: s-shaped body, low left hook, then long vertical below the right side.'),
    dict(sign='low boundary quote pair', location='between p.116 first inclusion and p117 commutation', reading='one pair only, drawn low; attribution unresolved', evidence='Crops 01/02: one physical pair at x570–579, y137–156; no second independent opener before commutation.')
]

report = dict(scan=22, reader='A', model='GPT-6 Astra Pro', effort='not exposed',
              viewed=[SOURCE, HALF_A, HALF_B],
              layout='One upright handwritten correction-list page in another unnamed hand, densely written from p.116 through p154. Most entries have a page/line reference at left and one or more quoted corrections across the row. A boxed insertion with a curved arrow is in the upper block; a heavily cancelled p122 reference sits left of p.123. Several short words and numerals are cancelled or overwritten. Near the bottom, a long left-margin arrow leads from p.151 to a separate slanted circled 151; that entry has a right-hand continuation with several cancellation groups. Two long vertical rules pass through the page, with a shorter faint far-left trace, an upper-left oval trace and a small mark near the bottom of the left rule. The archive 21 is in the lower-left corner. No separate mathematical diagram or display is present; formulas occur inline within list entries.',
              changes=changes, c_doubts=c_doubts, remaining_doubts=remaining,
              inventory=inventory, notes=notes, math_checks=[], notation=notation,
              abbreviations=[dict(form='p. / p', expansion='page (tentative interpretation only)', place='page-reference column throughout'), dict(form='Cat', expansion='category/categories as a label; not expanded in the text', place='circled 151, (Cat)'), dict(form='&', expansion='and (sign retained)', place='p117; p114 & 115; p.153')],
              brief_feedback='The required whole and each half were viewed once; each of 26 enhanced crops was displayed once. The p152 cancelled word was added as a single late crop after the C-doubt coverage audit; no decided locus was cropped twice. H is descriptive only, so all h fields are null and no H comparison rows are created. Cancellation extent can be clear while interior letters remain doubtful; the cancelled words were not identified by copying their live replacements. At the p116/p117 boundary, one physical quote pair has ambiguous line attribution, and C appears to count it twice. The p153 low s-like sign also requires separating observed line geometry from an uncertain textual interpretation. No OCR, outside pages, other reader files, external sources, subagents or compilation were used.')

(ROOT / 'report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
with (ROOT / 'inventory.tsv').open('w', newline='') as f:
    writer=csv.DictWriter(f, fieldnames=['sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed'], delimiter='\t')
    writer.writeheader(); writer.writerows(inventory)
(ROOT / 'notes.md').write_text('# Scan 022 — independent reader A\n\n'+'\n\n'.join(notes)+'\n\n## Coverage\n\nEvery visible reference/correction entry, including multiple references sharing one physical line, is covered. The inventory also separately records nested deletions, the insertion, underlining, both existing arrow/circle groups, the margin cancellation geometry, the additional page rules and isolated line marks. It has '+str(len(inventory))+' rows.\n\n## Open decisions\n\n'+'\n'.join('- '+x['place']+': '+x['alternatives']+'.' for x in remaining)+'\n')

crop_rows=[json.loads(line) for line in (ROOT/'crops/crops.jsonl').read_text().splitlines()]
(ROOT/'crop_views.json').write_text(json.dumps([dict(path=str(Path(x['output']).resolve()), displayed_count=1, source=x['source'], bbox=x['box']) for x in crop_rows],indent=2)+'\n')
open_loci=json.loads((ROOT/'open_loci.json').read_text())
if not any(x['id']=='26_p152_allow' for x in open_loci):
    open_loci.append(dict(id='26_p152_allow',bbox=[1480,1790,1618,1867],reason='C-doubt coverage audit: cancelled p152 allow was unresolved and had not yet received a crop.',rotate=0))
    (ROOT/'open_loci.json').write_text(json.dumps(open_loci,indent=2)+'\n')

# Static syntax/evidence checks only, never compilation.
brace_depth=0
for i,ch in enumerate(reading):
    if ch in '{}':
        n=0; j=i-1
        while j>=0 and reading[j]=='\\': n+=1; j-=1
        if n%2: continue
        brace_depth += 1 if ch=='{' else -1
        assert brace_depth>=0, ('early closing brace',i)
assert brace_depth==0, brace_depth
envs=[]
for match in re.finditer(r'\\(begin|end)\{([^}]+)\}',reading):
    action,name=match.groups()
    if action=='begin': envs.append(name)
    else: assert envs and envs.pop()==name, ('environment mismatch',name)
assert not envs
assert len(re.findall(r'(?<!\\)\$',reading))%2==0
assert all(c['c']=='' or c['c'] in original for c in changes)
assert all(c['c'] in original for c in c_doubts)
assert all(c['reading'] in reading for c in changes)
assert all(c['h'] is None and not c['diff_h'] for c in changes)
assert all(c['crop'] or (c['source'] and len(c['bbox'])==4) for c in changes+c_doubts)
assert all(c['crop'] or (c['source'] and len(c['bbox'])==4) for c in remaining)
assert len(crop_rows)==26
assert all(Path(x['output']).exists() for x in crop_rows)
allowed={'misread word','misread symbol or index','omission','text not on the page','deletion state (struck given live or live given struck)','insertion or placement','abbreviation expanded or spelling modernised','readable ink left as \\ill{}','drawing or diagram','other'}
assert all(c['kind'] in allowed for c in changes)
diff=''.join(difflib.unified_diff(original.splitlines(True),reading.splitlines(True),fromfile='supplied C.tex',tofile='reader A reading.tex'))
(ROOT/'literal_diff.patch').write_text(diff)
summary=dict(changes=len(changes),c_doubt_decisions=len(c_doubts),c_doubts_resolved=sum(x['resolved'] for x in c_doubts),remaining_doubts=len(remaining),inventory_rows=len(inventory),crops=len(crop_rows),uncertainty_macros=reading.count('\\unsure{'),math_checks=0,static_braces='balanced',static_environments='balanced',static_math_delimiters='even',compilation='not attempted',h_comparison_rows=0)
(ROOT/'validation.json').write_text(json.dumps(summary,indent=2)+'\n')
(ROOT/'inspection.log').write_text('Reader A, scan 022 only. Model GPT-6 Astra Pro; effort not exposed.\nRequired inputs read: brief_v07.md; conventions.md; PREAMBLE.tex; metadata.json; C.tex; H.tex; C_context.md; notation.md. No addendum was present in the assigned input listing.\nWhole viewed once for layout. Half a viewed once. Half b viewed once. Full literal C comparison made during the half readings. H descriptive status respected.\n26 tight enhanced crops generated with work/scripts/crop.py and each displayed once. Crop 24 rotated 90 degrees to make the vertical trace horizontal. Each crop uses LANCZOS width 2400, autocontrast and the script sharpening.\nAll supplied C uncertainty macros and page-context alternatives have individual decisions in report.json. Additional uncertain occurrences marked independently.\nLiteral C/reading change spans checked; report changes quote real C substrings or empty strings for omissions. Full diff saved. Static brace, environment and dollar checks passed. No LaTeX compilation or format building attempted.\nNo OCR, recognition library, PDF extraction, web research, other pages, other readers, or subagents used.\nNo mathematical proof or substantive computation performed; math_checks empty.\n')
print(json.dumps(summary,indent=2))
