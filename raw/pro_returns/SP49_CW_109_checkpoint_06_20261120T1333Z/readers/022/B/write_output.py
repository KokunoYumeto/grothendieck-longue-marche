from pathlib import Path
import json, re, difflib, hashlib

BASE = Path('/workspace/scratch/6d55c8c3e5a7/work')
OUT = BASE / 'readers/022/B'
C = (BASE / 'inputs/022/C.tex').read_text()
META = json.loads((BASE / 'inputs/022/metadata.json').read_text())
CROPS = json.loads((OUT / 'unresolved_after_halves.json').read_text())
reading = C
changes = []
decisions = []
remaining = []

def evidence_location(number=None, source=None, bbox=None):
    if number is not None:
        item = CROPS[number-1]
        return dict(crop='crops/'+item['id']+'.jpg', source=item['source'], bbox=item['bbox'])
    return dict(crop=None, source=source, bbox=bbox)

def change(identifier, place, old, new, kind, confidence, evidence, number=None, source=None, bbox=None):
    global reading
    if old:
        assert old in C, (identifier, 'not literal C', old)
        assert reading.count(old) == 1, (identifier, reading.count(old), old)
        reading = reading.replace(old, new, 1)
    row = dict(id=identifier, place=place, c=old, h=None, reading=new,
               diff_c=True, diff_h=False, kind=kind, marked_in_H=False,
               confidence=confidence, evidence=evidence)
    row.update(evidence_location(number, source, bbox))
    changes.append(row)

def decision(place, old, new, resolved, confidence, evidence, number=None, source=None, bbox=None):
    assert old in C, ('doubt not literal C', old)
    row = dict(place=place, c=old, reading=new, resolved=resolved,
               confidence=confidence, evidence=evidence)
    row.update(evidence_location(number, source, bbox))
    decisions.append(row)

def doubt(place, text, alternatives, confidence, reason, number=None, source=None, bbox=None):
    row = dict(place=place, reading=text, alternatives=alternatives,
               confidence=confidence, reason=reason)
    row.update(evidence_location(number, source, bbox))
    remaining.append(row)

change('first_formula', 'p.116 line -6, original inclusion',
       r'$\unsure{R|K}_{\unsure{h|n}}\subset R_n$',
       r'$\unsure{R|K}_{h}\subset \unsure{R|K}_n$',
       'misread symbol or index', 'medium',
       'The first lower letter has an upright distinctly taller than its following hump, supporting h. Each of the first two capitals has dark K-like diagonals and a very pale upper curved trace, so neither R/K occurrence can be made certain. The second occurrence is independently marked, rather than inheriting the first occurrence\'s uncertainty silently.', 1)
decision('p.116 line -6, first capital', r'\unsure{R|K}', r'\unsure{R|K}', False, 'medium',
         'A pale upper arc could be the bowl of R; the dark surviving form also permits K. The clear later replacement R does not settle this faded occurrence.', 1)
decision('p.116 line -6, first subscript', r'\unsure{h|n}', 'h', True, 'high',
         'The first upright extends above the low following arch; the lower letter is h on its own strokes.', 1)
decision('p.116 line -6, second original capital (C_context alternative)', r'R_n', r'\unsure{R|K}_n', False, 'medium',
         'This separate capital again has a pale upper curved trace and dark K-like diagonals. Its subscript n is clear. Literal C had left this second capital unmarked although C_context also allowed K here.', 1)
doubt('p.116 first original capital', r'\unsure{R|K}', 'R; K', 'medium', 'Faint upper contour is insufficient to choose between a bowl and a pen-entry trace.', 1)
doubt('p.116 second original capital', r'\unsure{R|K}_n', 'R_n; K_n', 'medium', 'The second faded occurrence independently admits R and K; n is not in doubt.', 1)

change('commutation_opener', 'p117 line 11 & 12, before commutation',
       r'p117 line 11 \& 12, ``commutation .... with.\'\''.replace("\\'", "'"),
       r'p117 line 11 \& 12, commutation .... with.\'\''.replace("\\'", "'"),
       'text not on the page', 'medium',
       'Only one pair of short strokes occurs in the space above-left of commutation: the pair below/right of the preceding R_n, already represented after that formula. There is no second independent opener before commutation. The four intervening dots, stop after with, and closing pair are visible and retained.', 2)

old_box = C[C.index('p.119 line 5,'):C.index('\n\nline 14')]
new_box = old_box.replace(r'\inserted{``not ``unto\'\'}'.replace("\\'", "'"),
                          r'\inserted{\unsure{``}not ``unto\'\'}'.replace("\\'", "'"))
new_box = new_box.replace(
    r'\draw[->] (add.south east) .. controls +(0.45,-.42) and +(.17,-.65) .. ([xshift=1.3em]word.east);',
    r'''\coordinate (tip) at ([xshift=1.3em]word.east);
\draw[->] (add.south east) .. controls +(0.45,-.42) and +(.17,-.65) .. (tip);
\draw ([xshift=-.6ex,yshift=-.2ex]tip) -- ([xshift=.4ex,yshift=.6ex]tip) -- ([xshift=.8ex,yshift=-.5ex]tip);''')
assert new_box != old_box
change('boxed_unto', 'p.119 line 5, boxed insertion and arrowhead', old_box, new_box,
       'drawing or diagram', 'medium',
       'The enclosure surrounds not and the quoted unto; its right lower corner joins the long curving arrow. A second angular head stroke is visible at the arrow tip. The tiny trace before not merges with the enclosure and cannot securely be counted as an independent opening pair, so the C pair is retained only as a marked possibility. The quotes around unto and onto are distinct paired strokes.', 3)
doubt('p.119 boxed addition, mark before not', r'\unsure{``}', 'Opening double quote; trace belonging to enclosure', 'low',
      'The small dark trace lies immediately beneath the enclosure stroke; its status as a separate quote cannot be secured.', 3)

for place, text, reason in [
    ('Cancelled left reference, leading mark', r'\unsure{?}', 'A curved upper hook and descending stroke survive, but any separate lower dot is covered by the cancellation.'),
    ('Cancelled left reference, star-like mark', r'\unsure{*}', 'Several small intersecting strokes survive, but the cancellation passes through their centre.'),
    ('Cancelled left reference, final mark', r'\unsure{?}', 'The high hooked outline and lower interior stroke are entangled with the long overstrike.')
]:
    decision(place, text, text, False, 'low', reason, 5)
    doubt(place, text, text, 'low', reason, 5)
decision('p.123, overwritten start before line 9', r'\deleted{\unsure{l}}', r'\deleted{\unsure{l}}', False, 'low',
         'There is an additional small loop/downstroke and crossing stroke to the left of the large live l. The old letter remains only a possible l; the following live l is not used to reconstruct it.', 6)
doubt('p.123 old start', r'\deleted{\unsure{l}}', 'l; unresolved earlier start', 'low',
      'The overwritten low loop does not supply a complete old letter.', 6)
decision('p128, old line reference before -12', r'\deleted{\unsure{16}}', r'\deleted{\unsure{16}}', False, 'low',
         'An upright followed by a low loop fits 16, but diagonal cancellation strokes form part of the same outlines. Only the live -12 is certain.', 7)
doubt('p128 old line reference', r'\deleted{\unsure{16}}', '16; unresolved two-digit start', 'low',
      'Crossing strokes obscure the tops and junction between the old digits.', 7)

change('p132_single_opener', 'p132 line -14, opening quote',
       "p132 line -14 ``wasn't''", "p132 line -14 `wasn't''",
       'misread symbol or index', 'high', 'The opener is one isolated curved upright, whereas the closer consists of two clearly separate strokes. The internal apostrophe follows n.', 8)
decision('133, after handwritten', r'\unsure{?}', r'\unsure{?}', False, 'low',
         'A small independent curl lies just inside the upper part of the closing parenthesis. It could be an abbreviated question mark, but no complete stem and dot are separable.', 9)
doubt('133, handwritten qualification', r'\unsure{?}', 'Question mark; unidentified small curl', 'low',
      'The visible mark is too abbreviated to make its punctuation value certain.', 9)
decision('p140, old digit beneath live 4', r'\deleted{\unsure{3}}', r'\deleted{\unsure{3}}', False, 'low',
         'Two small rightward curves survive within the heavier 4. They permit 3 but do not isolate a complete earlier digit.', 10)
doubt('p140 old digit', r'\deleted{\unsure{3}}', '3; unresolved earlier digit', 'low',
      'The live 4 and old curves share several strokes.', 10)

change('deleted_does', 'p.146, cancelled word between the two references',
       r'\deleted{\unsure{does}}', r'\deleted{does}',
       'misread word', 'medium',
       'Surviving ink independently supplies the low first bowl with a tall d ascender, a closed o, a small e turn, and the final s curl. The whole word is crossed; this decision is based on those remnants rather than the adjacent live contraction.', 11)
decision('p.146 cancelled word', r'\deleted{\unsure{does}}', r'\deleted{does}', True, 'medium',
         'The individual d/o/e/s remnants remain legible on both sides of the horizontal cancellations.', 11)
change('or_resolved', 'p.146 line -1, or', r'\unsure{or}', 'or', 'misread word', 'high',
       'The left closed oval and the following compact r shoulder with its long rightward exit stroke are separable despite the heavy join.', 12)
decision('p.146 line -1, or', r'\unsure{or}', 'or', True, 'high',
         'A closed o and the short r body with an upper rightward exit stroke are visible.', 12)

change('deleted_st', '147, cancelled start before line 2', r'\deleted{\unsure{st}}', r'\deleted{st}',
       'misread word', 'medium', 'The left low s curl and a separate right tall t stem/cross-stroke survive under a diagonal overstrike. The old letters can be read without borrowing the following standard.', 13)
decision('147 cancelled start', r'\deleted{\unsure{st}}', r'\deleted{st}', True, 'medium',
         'A low s with a trailing bend precedes a tall t; the diagonal cancellation is independently visible.', 13)
change('147_standard_opener', '147 line 2, opening quote before standard',
       "line 2 ``standard'", r"line 2 \unsure{``|`}standard'",
       'misread symbol or index', 'medium', 'The raised opener is a compact peaked stroke with two short legs; a fused double quote and one bent quote both fit. The closing single stroke is clear and retained.', 13)
doubt('147 line 2 opener', r'\unsure{``|`}', 'Fused double opening quote; single opening quote', 'medium',
      'The two legs join at a dark peak without a separable gap.', 13)
change('line20_stop', '147 line 20, after reference number', 'line 20', 'line 20.',
       'omission', 'high', 'A separate low oblique dot stands on the reference baseline after 20 and before the raised opener. It is not one leg of the opener.', 14)
change('line20_opener', '147 line 20, opening quote before with',
       "``with' not to''", r"\unsure{`|``}with' not to''",
       'misread symbol or index', 'medium', 'The opener is one broad curved mark, also compatible with a fused double. The single mark after with and the paired closer after to are distinct.', 14)
doubt('147 line 20 opener', r'\unsure{`|``}', 'Single opening quote; fused double opening quote', 'medium',
      'One continuous shallow arch is visible; it does not securely establish a count of two.', 14)
change('149_quote_resolved', '149., before line 7', r'\unsure{``}line 7', '``line 7',
       'misread symbol or index', 'high', 'The lower half shows two separate short raised uprights immediately before the looped l of line; retain the anomalous quote rather than normalizing it away.',
       source=META['half_b'], bbox=[342,499,471,559])
decision('149., before line 7', r'\unsure{``}', '``', True, 'high',
         'The two adjacent raised strokes are individually visible in the half view.', source=META['half_b'], bbox=[342,499,471,559])

decision('p.152 line -9, cancelled start', r'\deleted{\unsure{allow}}', r'\deleted{\unsure{allow}}', False, 'medium',
         'The first small bowl and the two tall loops are visible, but the lower portion after ll is covered by two broad horizontal strokes. Allow remains a plausible reading, not a reconstruction from the live line below.', 15)
doubt('p.152 old start after line -9', r'\deleted{\unsure{allow}}', 'allow; unresolved ending after all', 'medium',
      'The later low letters are merged with the cancellation strokes.', 15)
decision('Circled 151, overwritten part of whereas', r'\deleted{\unsure{as}}', r'\deleted{\unsure{as}}', False, 'low',
         'The small loop and angular strokes between the live where and final as support the candidate as, but the old and new strokes cannot be fully separated. The live replacement does not establish the old letters.', 16)
doubt('Circled 151 old suffix in whereas', r'\deleted{\unsure{as}}', 'as; unresolved overwritten suffix', 'low',
      'Both layers share the same small central loops.', 16)
decision('Circled 151, first cancelled right-hand phrase', r'\deleted{\unsure{If th}}', r'\deleted{\unsure{If th}}', False, 'low',
         'A large I-like upright with bars, another short descender, and t/h-like strokes survive. The cancellations prevent a secure reading of the whole abandoned phrase.', 17)
doubt('Circled 151 first cancelled right-hand phrase', r'\deleted{\unsure{If th}}', 'If th; unresolved abandoned phrase', 'low',
      'Horizontal and oblique strokes pass through the letters and may also be read as their bars.', 17)
decision('Circled 151, cancelled word after target', r'\deleted{\unsure{of}}', r'\deleted{\unsure{of}}', False, 'low',
         'A small enclosed lower loop and a taller stroke permit of, but the compact overstrike does not isolate both letters.', 17)
doubt('Circled 151 cancelled word after target', r'\deleted{\unsure{of}}', 'of; unresolved short word', 'low',
      'The rightmost scribble is strongly crossed in several directions.', 17)
change('work_resolved', 'Circled 151, second cancelled right-hand line', r'\unsure{work|write}', 'work',
       'misread word', 'high', 'A low w is followed by a closed o, a short r connection, then a tall final k with a right-hand arm. These distinguish work from write in this occurrence.', 17)
decision('Circled 151 cancelled work/write', r'\unsure{work|write}', 'work', True, 'high',
         'The closed o and tall final k with its separate right arm are visible through the horizontal crossing.', 17)
change('well_apostrophe', 'Circled 151, apostrophe in cancelled we\'ll', "we'll", r"we\unsure{'}ll",
       'misread symbol or index', 'low', 'The w, e and two tall l loops are visible. No independent apostrophe can be isolated in the crowded area above their join; preserve the candidate but mark its uncertainty.', 17)
doubt('Circled 151 cancelled apostrophe', r"we\unsure{'}ll", "we'll; we ll", 'low',
      'The upper cancellation and preceding abandoned line occupy the likely apostrophe area.', 17)
change('terminal_n', 'Circled 151, live tail after cancelled we\'ll work', r'\unsure{in|n}', 'n',
       'misread word', 'high', 'The short surviving tail is one n: one initial stem and one arch. No preceding separate i is visible. The cancellation ends to its left, leaving this n live.', 17)
decision('Circled 151 terminal in/n', r'\unsure{in|n}', 'n', True, 'high',
         'A single initial stem and arch stand to the right of the endpoint of the crossing stroke; there is no additional initial i.', 17)

change('handiness_quote_state', 'p.153 line 4, cancellation around handiness',
       r"\deleted{``handiness''}", r"``\deleted{handiness}''",
       'deletion state (struck given live or live given struck)', 'medium',
       'The zigzag cancellation runs through the word handiness. The opening pair is above-left of the crossing and the closing pair stands above-right; neither pair has its own cancellation stroke. The word itself is legible as handiness.', 18)
decision('p.153 cancelled cluster after handy', r'\deleted{\unsure{n \&}}', r'\deleted{\unsure{n \&}}', False, 'low',
         'An initial small arch permits n. The following loop/descender cluster is crossed and cannot be resolved securely as an ampersand independently of the live n and ampersand farther right.', 19)
doubt('p.153 cancelled cluster after handy', r'\deleted{\unsure{n \&}}', 'n &; unresolved cluster', 'low',
      'The crossed second glyph has several low loops and a descending stroke; the adjacent live replacement does not decide it.', 19)
change('153_low_s_mark', 'p.153 line 4, last sign after live n &',
       r'\unsure{\uline{s}|S}', r'$\unsure{s_1|\underline{s}|S_1}$',
       'misread symbol or index', 'low',
       'Below the s/S-shaped body there is a short leftward hook joined to a substantial downward stem. It resembles a low 1 more than a simple underline, but the interpretation and case remain uncertain. The reading therefore explicitly retains both the low-1 and underline possibilities rather than silently discarding the descending stroke.', 19)
decision('p.153 final s/S and lower stroke', r'\unsure{\uline{s}|S}', r'$\unsure{s_1|\underline{s}|S_1}$', False, 'low',
         'The lower hook has a long descending component that a plain underline does not capture. The body\'s case cannot be decided from its height alone.', 19)
doubt('p.153 final s/S and lower stroke', r'$\unsure{s_1|\underline{s}|S_1}$', 's with lower 1; underlined s with turned endpoint; S with lower 1', 'low',
      'The hooked lower mark and the body\'s case remain ambiguous; this is a reading of strokes only, not a proposed mathematical normalization.', 19)

change('allo_resolved', 'p154 line 9, cancelled start', r'\deleted{\unsure{allo}}', r'\deleted{allo}',
       'misread word', 'high', 'The low initial a bowl, two separate tall l loops, and the small final closed o remain visible despite the two oblique cancellation strokes. No following w is present.', 20)
decision('p154 line 9 cancelled allo', r'\deleted{\unsure{allo}}', r'\deleted{allo}', True, 'high',
         'The four surviving letter bodies a/l/l/o can be read directly, including the final o beyond the heavier crossing.', 20)
change('cancelled_tail', 'p154 line -6, cancelled tail after wouldn\'t',
       r'\deleted{\unsure{it}}', r'\deleted{\unsure{to|it}}',
       'misread word', 'low', 'A tall central t-like stem and a conspicuous closed right bowl favour to. The crossing obscures the lower left portion, so C\'s it is retained as an alternative instead of being silently rejected.', 21)
decision('p154 line -6 cancelled tail', r'\deleted{\unsure{it}}', r'\deleted{\unsure{to|it}}', False, 'low',
         'The rightmost body is a distinct closed bowl after the tall looped stem; lower crossed strokes still permit another segmentation.', 21)
doubt('p154 cancelled tail after wouldn\'t', r'\deleted{\unsure{to|it}}', 'to; it', 'low',
      'The final round bowl favours o, but part of the central joining stroke is overwritten.', 21)
change('last_standard_quotes', 'p154 line -2, both quote groups',
       "line -2 ``standard''", r"line -2 \unsure{``|`}standard\unsure{''|'}",
       'misread symbol or index', 'medium', 'The opening group is a closed, hooked cluster and the closing group is another compact joined stroke. Their positions are clear, but neither group securely distinguishes two quote strokes from one bent stroke. The two occurrences are marked separately.', 22)
doubt('p154 line -2 opener', r'\unsure{``|`}', 'Double opening quote; single bent opening quote', 'medium',
      'The opener forms one joined loop and upright with no separable gap.', 22)
doubt('p154 line -2 closer', r"\unsure{''|'}", 'Double closing quote; single bent closing quote', 'medium',
      'The closer has one dark upright and short joined return; a separate count of two is not secure.', 22)

# Overlay anchors retain the established prose order while locating the nontext marks.
reading = reading.replace('p.116 line', r'\tikz[remember picture,overlay]\coordinate (b022top);p.116 line', 1)
reading = reading.replace('p117 line', r'\tikz[remember picture,overlay]\coordinate (b022loop);p117 line', 1)
reading = reading.replace('p.121 line', r'\tikz[remember picture,overlay]\coordinate (b022faintend);p.121 line', 1)
reading = reading.replace(r'\margin{\deleted', r'\tikz[remember picture,overlay]\coordinate (b022margin);\margin{\deleted', 1)
reading = reading.replace('line -2 ', r'\tikz[remember picture,overlay]\coordinate (b022bottom);line -2 ', 1)

drawings = [
    ('left_rule', 'Long vertical rule through left reference column',
     r'''% B022-D01: left vertical rule, original x approximately 220.
\draw[line width=.3pt] ([xshift=1.2em,yshift=1.8ex]b022top) -- ([xshift=.95em,yshift=-.2ex]b022bottom);''',
     'high', 'A thin continuous vertical rule runs from the first reference down to the last entries, crossing several reference numbers. It is independent of the letter stems.', None, META['whole'], [211,82,233,2284]),
    ('right_rule', 'Long vertical rule near right edge of text',
     r'''% B022-D02: right vertical rule, original x approximately 1500.
\draw[line width=.3pt] ([xshift=.96\linewidth,yshift=1.8ex]b022top) -- ([xshift=.955\linewidth,yshift=-.2ex]b022bottom);''',
     'high', 'A second thin rule runs nearly parallel to the first, from the upper margin to the lower entries; it passes through some right-hand writing.', None, META['whole'], [1487,82,1516,2298]),
    ('faint_left_trace', 'Far-left upper margin, broken vertical trace',
     r'''% B022-D03: faint far-left vertical trace and lower broken continuation.
\draw[black!45,line width=.18pt] ([xshift=-2.1em,yshift=-1.0ex]b022top) -- ([xshift=-2.15em,yshift=-.2ex]b022faintend);
\draw[black!45,line width=.18pt] ([xshift=-2.15em,yshift=-.7ex]b022faintend) .. controls +(0,-.5ex) and +(.15em,.5ex) .. ([xshift=-2.25em,yshift=-.2ex]b022margin);''',
     'medium', 'A separate faint, somewhat interrupted upright trace lies much farther left than the main reference rule. Its visible upper and lower pieces are represented without assigning an editorial function.', None, META['whole'], [38,122,62,596]),
    ('pale_oval', 'Upper-left margin, beside p117',
     r'''% B022-D04: pale broken oval trace; its origin is uncertain.
\draw[black!35,line width=.2pt] ([xshift=-.85em,yshift=2.1ex]b022loop) .. controls +(-.7em,.1ex) and +(-.55em,.2ex) .. ([xshift=-1.65em,yshift=.7ex]b022loop);
\draw[black!70,line width=.25pt] ([xshift=-1.65em,yshift=.7ex]b022loop) .. controls +(-.1em,-.5ex) and +(-.25em,.3ex) .. ([xshift=-1.35em,yshift=-.2ex]b022loop);
\draw[black!35,line width=.2pt] ([xshift=-1.35em,yshift=-.2ex]b022loop) .. controls +(.5em,-.6ex) and +(-.25em,-.5ex) .. ([xshift=-.35em,yshift=.2ex]b022loop);''',
     'medium', 'The crop shows a broken oval outline with a darker left segment. It may be a physical/copy trace rather than intentional writing; the visible shape is retained as an unlabelled trace, without inventing a character or function.', 4, None, None),
    ('lower_bent_mark', 'Lower end of left reference rule, near last entry',
     r'''% B022-D05: short bent dark mark at the lower left rule.
\draw[line width=.65pt] ([xshift=.65em,yshift=1.0ex]b022bottom) -- ([xshift=.97em,yshift=.75ex]b022bottom) -- ([xshift=1.12em,yshift=.3ex]b022bottom);
\draw[line width=.4pt] ([xshift=.97em,yshift=1.12ex]b022bottom) -- ([xshift=.96em,yshift=-.25ex]b022bottom);''',
     'high', 'The magnified trace is a small bent dark stroke across the pale rule with a short downward continuation; no letter or conventional star is securely identifiable.', 23, None, None)
]
draw_code = '\n'.join(d[2] for d in drawings)
reading = reading.replace('\n% archive sheet number: 21', '\n\n'+r'\figure{\begin{tikzpicture}[remember picture,overlay]'+'\n'+draw_code+'\n'+r'\end{tikzpicture}}'+'\n\n% archive sheet number: 21')
for identifier, place, code, confidence, evidence, number, source, bbox in drawings:
    change(identifier, place, '', code, 'drawing or diagram', confidence, evidence, number, source, bbox)

# Full inventory: every correction reference, separate textual continuation,
# all nested states, the two existing arrow drawings, and the additional marks.
inventory = []
def inv(kind, position, text, hand='another unnamed hand'):
    inventory.append(dict(sheet_kind='list', hand=hand, element=f'{len(inventory)+1:02}',
                          kind=kind, position=position, first_words_or_objects=text, transcribed='yes'))

rows = [
('text','top line','p.116 line -6, original and replacement inclusions'),
('text','second line','p117 line 11 & 12, commutation .... with.'),
('text','third line','line -17, I\'d better assume ...'),
('text','upper quarter, p119','p.119 line 5, onto'),
('insertion','left of onto, inside enclosure','not ``unto\'\''),
('drawing','around insertion','rounded enclosure around not unto'),
('drawing','from enclosure to right of onto','long lower-curving arrow with retraced/angular head'),
('text','next line','line 14, allows one to'),
('text','nested under one','two underline strokes under one'),
('text','upper quarter, full-width line','p114 & 115 handwritten comment: is §52 intended rather than §51.'),
('text','below handwritten-comment line','p.121 line -17, endows'),
('margin note','far left, level with p123','? * p122 ?'),
('deletion','entire marginal p122 reference','multiple crossing strokes over the reference and its adjacent signs'),
('text','p123 first line','p.123 line 9, standard'),
('deletion','start of line before 9','old possible l, overwritten beside live line'),
('text','p123 next line, left part','line 13, with direct sums'),
('text','p123 next line, right part','line -1, commutes with'),
('text','below p123','p.124 line 17, a long time ago'),
('text','next reference','p128 line -12, standard'),
('deletion','p128 reference before -12','old possible 16'),
('text','next line, left','p131 line 16, commutes with'),
('text','same line, right','line 18, it is'),
('text','next line','p132 line -14, wasn\'t'),
('text','next line','133 line 13 (handwritten ?), commutes with'),
('text','next line','p.135 line 4, commas needed around ,of course,'),
('text','next line','137 line -13, wasn\'t'),
('text','next line, left','138 line -15, through'),
('text','same line, right','line -5, standard'),
('text','next line','p140 line 4, commutes with'),
('deletion','p140 reference under 4','overwritten old possible 3'),
('text','middle of sheet','141 line -1, standard'),
('text','next line, left','142 line 15, s_1=delta_0'),
('text','same line, right','line -15, allow one to'),
('text','next line, left','p.146 line -3, usual'),
('deletion','between p146 references','does'),
('text','same line, right','line -1, doesn\'t or shouldn\'t'),
('text','next line, left','147 line 2, standard'),
('deletion','after 147 and before line','st'),
('text','same line, middle','line 10, commutes with'),
('text','same line, right','line 18, doesn\'t'),
('text','indented line beneath 147','line 20., with\' not to'),
('text','next line, left','148 line 21, developed'),
('text','same line, right','line -1., standard.'),
('text','next line, left','149. ``line 7, standard'),
('text','same line, right','line 12, isn\'t'),
('text','next line, left','p.151 line 8, isn\'t'),
('text','same line, middle','line 17, a long time ago'),
('text','same line and continuation below','line 18, putting off would be more usual.'),
('text','next reference, left','p.152 line 17, developed.;'),
('text','same line, middle','line -10., lead to develop'),
('text','same line, right, and following continuation','line -9, which will allow us to define'),
('deletion','after p152 line -9 opener','old possible allow'),
('drawing','left margin from first p151 entry downward','curved arrow ending beside the circled 151'),
('drawing','left of line -4 near bottom quarter','oval surrounding 151'),
('text','beside circled 151','line -4, whereas in the target category (Cat) of (2)'),
('deletion','within whereas','overwritten possible as'),
('text','right of the quotation and continued on next left line','the target n in (2) is A with a hat'),
('deletion','right-hand revision, first upper phrase','possible If th'),
('deletion','right-hand revision, after target','possible of'),
('deletion','right-hand revision, second line','we\'ll work; apostrophe uncertain'),
('text','next reference, near bottom','p.153 line 4, developed; handy n & s/S with lower mark would be better'),
('deletion','p153 quoted rejected word','handiness'),
('deletion','p153 between handy and live n &','possible n &'),
('text','p153, nested lower mark under s/S','hooked lower stroke, possible 1 or turned underline'),
('text','next line','p154 line 9, will even allow us to handle'),
('deletion','p154 before quoted live wording','allo'),
('text','next line, left','line -9, don\'t'),
('text','same line, right','line -6, wouldn\'t'),
('deletion','p154 tail after wouldn\'t','possible to or it'),
('text','last line','line -2, standard'),
('drawing','through left reference column','long thin vertical rule'),
('drawing','near right text edge','long thin vertical rule'),
('drawing','far-left upper margin','faint broken upright trace'),
('drawing','upper-left beside p117','pale broken oval trace'),
('drawing','lower end of left rule','short bent dark mark'),
('margin note','bottom-left corner','archive sheet number 21, recorded as a comment')
]
for kind, position, text in rows:
    hand='another unnamed hand'
    if text=='pale broken oval trace' or text=='faint broken upright trace':
        hand='origin uncertain; no personal attribution'
    if text.startswith('archive sheet number'):
        hand='archive pencil hand, unnamed'
    inv(kind, position, text, hand)

notation = [
dict(sign=r'\unsure{R|K}_h; \unsure{R|K}_n; R_h; \Sigma_h',location='p.116 line -6',reading=r'\unsure{R|K}_h\subset\unsure{R|K}_n; R_h\subset\Sigma_h',evidence='Crop 01: both original capitals are faded and separately doubtful; original h and n are distinct; the replacement R has a complete bowl and leg; the final capital is an angular three-part sigma. No doubled capital alphabet is visible.'),
dict(sign=r'\subset',location='p.116, both inclusions',reading=r'\subset',evidence='Crop 01: both signs are single curved outlines open on the right, without a separate lower equality bar.'),
dict(sign="''",location='below/right of the original R_n',reading="''",evidence='Crop 01 shows two short adjacent strokes beyond the low n. Crop 02 shows no additional independent pair before commutation. The one visible group is retained at the first formula.'),
dict(sign=r'\S52; \S51',location='p114 & 115 comment',reading=r'\S52; \S51',evidence='Half a: both signs have the visible double-curved section shape; digits are 52 and 51.'),
dict(sign=r'\uuline{one}',location='p.119 line 14',reading=r'\uuline{one}',evidence='Half a: two distinct low strokes lie under one only.'),
dict(sign=r's_1=\delta_0',location='142 line 15',reading=r's_1=\delta_0',evidence='Half b: open s body with low 1, two equality bars, a delta with closed lower bowl, and low 0. This is ink identification, not an identity proof.'),
dict(sign=r'\widehat{A}',location='circled 151, final left continuation',reading=r'\widehat{A}',evidence='Half b: ordinary capital A with two separate roof strokes above it.'),
dict(sign=r'(\mathrm{Cat}); (2)',location='circled 151, target-category wording',reading=r'(\mathrm{Cat}); (2)',evidence='Half b: a single ordinary capital C followed by at, with round parentheses; the formula reference is an ordinary 2 in round parentheses.'),
dict(sign='quotation counts',location='p132; 147 line 2 and line 20; 149; p154 last line',reading='Single opener at p132; uncertain fused openers at the two 147 entries; definite double before line 7 at 149; both final groups separately uncertain.',evidence='Crops 08, 13, 14 and 22, with half-b inspection of 149; all uncertain occurrences are marked independently in reading.tex.'),
dict(sign=r's_1 | \underline{s} | S_1',location='p.153 after n &',reading=r'$\unsure{s_1|\underline{s}|S_1}$',evidence='Crop 19: the lower short hook joins a long downward stroke; a plain horizontal underline alone does not preserve all of it. Case and interpretation remain open.')
]

report = dict(
    scan=22, reader='B', model='GPT-6 Astra Pro', effort='not exposed',
    viewed=[META['whole'], META['half_a'], META['half_b']],
    layout='One handwritten correction list in another unnamed hand, running from cited p116 through p154 with an out-of-order p114 & 115 comment. References occupy a loose left column; some lines hold two or three corrections. Two long thin vertical rules cross the sheet. A faint far-left upper upright and a pale broken oval are also visible. The p119 addition is boxed and linked by a curved arrow to the right of onto. A heavily cancelled reference occupies the left margin near p123. A second long curved arrow links the first p151 entry to a lower circled 151. That lower entry contains a compact right-hand revision with several cancellations. There are no free-standing mathematical diagrams, no title, and no manuscript page number; the lower-left 21 is an archive corner number. All text blocks, nested states, and visible nontext line marks are inventoried.',
    changes=changes, c_doubts=decisions, remaining_doubts=remaining,
    inventory=inventory,
    notes=[
        'The page lists proposed corrections for cited pages 116–154, with a separate question about a handwritten reference on pages 114 & 115.',
        'At p116 line -6 an inclusion is explicitly replaced by R_h subset Sigma_h; the two original capitals remain visually uncertain. No definitions of the objects occur on this page.',
        'At p114 & 115 the writer asks whether §52 is intended rather than §51. The last mark is a period as written, not a supplied question mark.',
        'The p151 line-18 wording putting off is said to be more usual. The separate circled-151 entry quotes a target-category phrase and identifies the target in (2) as A with a hat, with abandoned wording still present.',
        'At p153 the rejected handiness and proposed handy wording are followed by would be better; the final s/S-shaped sign has an unresolved lower mark.',
        'There is no title, stated page count, or pagination belonging to these notes. The archive corner number is 21.'
    ],
    math_checks=[],
    notation=notation,
    abbreviations=[
        dict(form='p.; p', expansion='page (reference label; not expanded in the text)', place='reference column throughout'),
        dict(form='&', expansion='and (ampersand; retained as written)', place='p117; p114 & 115; p153'),
        dict(form='§', expansion='section sign; retained as written', place='p114 & 115 comment')
    ],
    brief_feedback='The supplied v07 brief was followed: one whole view, one view of each half, then 23 planned enhanced crops, each generated once and displayed once. Compact adjacent cancellations in the right-hand 151 revision were inspected together in one tight crop, without recropping them individually. H is descriptive only; there are no H comparison rows. The page supplies correction directives rather than mathematical hypotheses, so visual/formula identification is not counted as a substantive mathematical check. Static checks only; no compilation. Overlay anchors locate the added line drawings relative to existing text entries without reordering the prose. The pale upper-left oval may be a physical/copy trace; its shape is preserved without attributing intention.'
)

OUT.joinpath('reading.tex').write_text(reading)
OUT.joinpath('report.json').write_text(json.dumps(report, ensure_ascii=False, indent=2)+'\n')
OUT.joinpath('inventory.json').write_text(json.dumps(inventory, ensure_ascii=False, indent=2)+'\n')
OUT.joinpath('inventory.tsv').write_text('sheet_kind\thand\telement\tkind\tposition\tfirst_words_or_objects\ttranscribed\n'+'\n'.join('\t'.join(row[k] for k in ('sheet_kind','hand','element','kind','position','first_words_or_objects','transcribed')) for row in inventory)+'\n')
OUT.joinpath('notes.md').write_text('# Scan 022 — reader B\n\n'+'\n\n'.join(report['notes'])+'\n\n## Method and remaining decisions\n\n'+report['brief_feedback']+'\n\n'+f'{len(changes)} C-change loci; {len(decisions)} C doubt/context decisions; {len(remaining)} marked unresolved occurrences; {len(inventory)} inventory rows.\n\n'+ '\n'.join('- '+x['place']+': '+x['reason'] for x in remaining)+'\n')
OUT.joinpath('literal_diff.patch').write_text(''.join(difflib.unified_diff(C.splitlines(keepends=True),reading.splitlines(keepends=True),fromfile='inputs/022/C.tex',tofile='readers/022/B/reading.tex')))

# Static checks: actual C literals, report coverage, braces, environment balance,
# mathematical-mode delimiters, permitted state macros, and crop display log.
assert len([x for x in decisions if x['c'].startswith(r'\unsure') or x['c'].startswith(r'\deleted')]) >= 23
assert all(row['h'] is None and not row['diff_h'] for row in changes)
assert all(row['c']=='' or row['c'] in C for row in changes)
assert all(row['reading'] in reading for row in changes)
assert all(row['reading'] in reading for row in remaining)
clean='\n'.join(line.split('%',1)[0] for line in reading.splitlines())
balance=0
for i,char in enumerate(clean):
    if char in '{}' and (i==0 or clean[i-1]!='\\'):
        balance += 1 if char=='{' else -1
        assert balance>=0, ('brace underflow', i)
assert balance==0, ('brace imbalance', balance)
environments=[]
for typ,name in re.findall(r'\\(begin|end)\{([^}]+)\}',clean):
    if typ=='begin': environments.append(name)
    else:
        assert environments and environments[-1]==name, ('environment',typ,name,environments)
        environments.pop()
assert not environments
assert len(re.findall(r'(?<!\\)\$',clean))%2==0
assert len(re.findall(r'\\unsure\{', reading))==len(remaining)
assert len(CROPS)==23

read_files=['briefs/brief_v07.md','briefs/conventions.md','PREAMBLE.tex','inputs/022/metadata.json','inputs/022/C.tex','inputs/022/H.tex','inputs/022/C_context.md','inputs/022/notation.md','scripts/crop.py']
logs=dict(inputs_read=read_files, input_sha256={p:hashlib.sha256((BASE/p).read_bytes()).hexdigest() for p in read_files},
          view_counts=dict(whole=1, half_a=1, half_b=1),
          crops_generated=23, crops_displayed=[x['id'] for x in CROPS],
          crop_method='scripts/crop.py; LANCZOS width 2400, autocontrast, unsharp mask; no rotation needed for these nearly horizontal loci',
          forbidden_operations_performed=[],
          static_checks=dict(literal_C_change_fields=True, literal_C_doubt_fields=True, H_rows_absent=True, all_change_readings_present=True, all_remaining_doubts_marked=True, braces_balanced=True, environments_balanced=True, dollar_delimiters_even=True, compilation_attempted=False),
          counts=dict(changes=len(changes), c_doubt_decisions=len(decisions), remaining_doubts=len(remaining), inventory=len(inventory), math_checks=0))
OUT.joinpath('review_log.json').write_text(json.dumps(logs, ensure_ascii=False, indent=2)+'\n')
print(json.dumps(logs['counts']))
