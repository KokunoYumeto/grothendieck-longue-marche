from pathlib import Path
import json

ROOT = Path('/workspace/scratch/6d55c8c3e5a7')
OUT = ROOT / 'work/readers/030/C'
SRC = ROOT / 'work/inputs/030/C.tex'
WHOLE = str(ROOT / 'source/SP49_CW_109_scans/H109-03_109_scan030.jpg')
HA = str(ROOT / 'source/SP49_CW_109_scans/H109-03_109_scan030_a.jpg')
HB = str(ROOT / 'source/SP49_CW_109_scans/H109-03_109_scan030_b.jpg')
PLAN = json.loads((OUT / 'frozen_unresolved.json').read_text())['loci']
LOC = {int(q['id'].split('_')[0]): q for q in PLAN}

first_word = r"``\tikz[baseline=(did30C.base)]{\node[inner sep=0pt] (did30C) {didn't};\begin{scope}[shift={(did30C.base west)},x=1em,y=1ex]\draw[overlay,black!45,line width=.3pt,line cap=round] (-1.05,.55) .. controls (-1.1,.18) and (-.93,.15) .. (-.8,.15) -- (-.1,.08);\draw[overlay,black!45,line width=.3pt,line cap=round] (-.55,.6) .. controls (-.65,.15) and (-.46,.04) .. (-.45,-.28);\end{scope}}''"
ref381 = r"l\unsure{-|.}\tikz[baseline=(old381C.base)]{\node[inner sep=0pt] (old381C) {\deleted{\unsure{8}}};\node[anchor=base west,inner sep=0pt] at (old381C.base west) {3};}"
ref386 = r"\tikz[baseline=(l386C.base)]{\node[inner sep=0pt] (l386C) {l};\fill[black!40] ([xshift=.55em,yshift=-.4ex]l386C.base east) circle (.05ex);}\,-11"
with394 = r"\tikz[baseline=(with394C.base)]{\node[inner sep=0pt] (with394C) {``commutes with''};\fill ([xshift=2.8em,yshift=1.0ex]with394C.base east) ellipse (.045ex and .09ex);}"
margin396 = r"\margin{\tikz[x=1ex,y=1ex]{\fill (0,0) circle (.055);\fill (.23,.29) -- (.22,.40) -- (.34,.34) -- (.30,.28) -- cycle;}}"
formula401 = r"\tikz[baseline=(km401C.base)]{\node[inner sep=0pt] (km401C) {$(k-M)$};\fill[overlay] ([xshift=-.3em,yshift=1.1ex]km401C.base west) circle (.055ex);}"
formula385 = r"Formula (7) \raisebox{1.1ex}[0pt][0pt]{$+$}$\cong$'' missing"

replacements = [
    (r"p. 371 l.14 ``didn't''", 'p. 371 l.14 ' + first_word),
    (r'p 372 l.16', r'p 372 l 1.6'),
    (r'``recommendation\'\'', r'\unsure{``|`}recommendation\'\''),
]
# Quote-bearing strings are kept literal, without Python escape ambiguity.
replacements[2] = ("``recommendation''", r"\unsure{``|`}recommendation''")
replacements += [
    (r'l.\deleted{\unsure{8}}\unsure{3|8}', ref381),
    ("bothering''", r"bothering\unsure{''|'}"),
    ("``suggest simply dropping''", r"\unsure{``|`}suggest simply dropping''"),
    (r'resp. with\ldots{}', r'resp. with....'),
    (r"Formula (7) \unsure{``|`|$+$}$\cong$'' missing", formula385),
    (r'386 l.-11', '386 ' + ref386),
    ("to'' is more usual.", r"to'' is more usual\unsure{,|.}"),
    ("p 394 l-7 ``commutes with''", 'p 394 l-7 ' + with394),
    ("``interpreted as saying''", r"\unsure{``|`}interpreted as saying\unsure{''|'}"),
    ("p 396 l.-4 ``commute with'' again l-2.", "p 396 l.-4 ``commute with'' again l-2. " + margin396),
    (r"``$(k-M)$''", r"\unsure{``|`}" + formula401 + "''"),
    ('% archive sheet number: 29\n% The last figure can also be read as 3.', '% archive sheet number: 23 (possibly 29)')
]
reading = SRC.read_text()
for old, new in replacements:
    assert reading.count(old) == 1, (old, reading.count(old))
    reading = reading.replace(old, new, 1)
(OUT / 'reading.tex').write_text(reading)

def loc(n=None, source=None, bbox=None):
    if n is not None:
        q = LOC[n]
        return {'crop': str(ROOT / q['crop']), 'source': str(ROOT / q['source']), 'bbox': q['bbox']}
    return {'crop': None, 'source': source, 'bbox': bbox}

changes = []
def change(id, place, c, r, kind, confidence, evidence, n=None, source=None, bbox=None):
    changes.append({'id': id, 'place': place, 'c': c, 'h': None, 'reading': r,
                    'diff_c': True, 'diff_h': False, 'kind': kind, 'marked_in_H': False,
                    'confidence': confidence, 'evidence': evidence, **loc(n, source, bbox)})

change('371-faint-mark', '371 l.14, low mark before the first d', "``didn't''", first_word,
       'drawing or diagram', 'medium',
       'Below the two separate opening quote strokes there is a faint low hook-and-cross group: a bent left segment runs into a short horizontal, and a second curved upright crosses it. It is reproduced in grey at its observed position without naming it as a letter or assigning an origin.', 2)
change('372-reference-point', '372, first line reference', 'l.16', 'l 1.6', 'insertion or placement', 'high',
       'The l has a continuous low exit and no separate dark stop to its right. A distinct dark point stands to the right of the upright 1, before the 6. The numeral strokes remain 1 and 6; the point is retained in that physical position, without claiming a decimal interpretation.', 3)
change('373-recommendation-opener', '373 l-13, opening quotation', '``', r'\unsure{``|`}', 'misread symbol or index', 'medium',
       'The opener has two pendant limbs meeting at one dark apex. A joined pair is favored, but the shared apex does not securely exclude one bent stroke.', 6)
change('381-reference', '381, overwritten line reference and preceding short mark', r'l.\deleted{\unsure{8}}\unsure{3|8}', ref381,
       'insertion or placement', 'medium',
       'The live outer contour has two open-left lobes and reads 3. Small closed remnants survive within the old writing, but the older 8 is still uncertain. Old and new occupy one glyph space, so they are overlaid. The preceding short, horizontally extended mark favors a dash over a stop; both are retained.', 10)
change('383-bothering-closer', '383 l-9, closing quotation after bothering', "bothering''", r"bothering\unsure{''|'}",
       'misread symbol or index', 'medium',
       'The high terminal group has one long right stem and a short left branch at its middle. Two joined strokes are plausible, but the compact black join prevents a certain count.', 11)
change('383-suggest-opener', '383 l-3, opening quotation before suggest', '``', r'\unsure{``|`}', 'misread symbol or index', 'medium',
       'The high opener is an unbroken arch with two low ends and a common top. A pair is favored but a single bent stroke remains possible.', 12)
change('385-resp-dots', '385 l6, continuation marks after the second with', r'with\ldots{}', 'with....', 'omission', 'high',
       'Four physically separated low dark components follow with: two short horizontal components, then two thicker dot-like components. There is a visible white gap between the first two; no continuous dash is supplied.', 13)
change('385-raised-cross', '385, Formula (7), mark before the congruence sign', r'\unsure{``|`|$+$}', r'\raisebox{1.1ex}[0pt][0pt]{$+$}',
       'misread symbol or index', 'high',
       'Two short strokes cross transversely, forming a tilted plus-shaped cross; they are not parallel quotation stems. The group is raised above and to the left of the congruence sign. This identifies its visible shape, not an arithmetic role.', 14)
change('386-low-point', '386, first line reference, pale point after l', 'l.-11', ref386, 'other', 'medium',
       'A separate pale round point lies well below and to the right of the l exit, before the minus. It is retained geometrically in that lower position; its status as an abbreviation stop or a material spot is not assigned. The two dark pieces left of l align with its interrupted entrance stroke.', 15)
change('388-terminal-punctuation', '388 l13, after usual', 'usual.', r'usual\unsure{,|.}', 'misread symbol or index', 'medium',
       'The separated terminal mark is a short descending oblique with a curved lower end. Its tail favors a comma, but a heavily drawn stop remains possible.', 18)
change('394-isolated-point', '394 l-7, to the right of the quoted phrase', "``commutes with''", with394, 'drawing or diagram', 'high',
       'A small dark upright oval stands apart to the right of the closing pair, near their lower height and above the word baseline. It is preserved as a geometrical mark without a punctuation role or assigned origin.', 20)
change('395-first-opener', '395 l1, opening quotation before interpreted', '``', r'\unsure{``|`}', 'misread symbol or index', 'medium',
       'The opening group has one long left limb and a short right limb joined at the top. A fused pair is favored; one bent stroke is not excluded.', 21)
change('395-first-closer', '395 l1, closing quotation after saying', "''", r"\unsure{''|'}", 'misread symbol or index', 'medium',
       'The terminal group has two lower tips joined in one angled upper body. Its fused center leaves the stroke count uncertain independently of the opener.', 21)
change('396-margin-points', 'right margin, between the 396 and 397 rows', '', margin396, 'drawing or diagram', 'high',
       'Two separated black spots form a short rising diagonal: a rounder lower-left spot and a slightly angular upper-right spot. Their origin and function are unassigned; no connecting stroke is drawn.', 26)
change('401-formula-opener', '401 l.-11, opening quotation before the formula', '``', r'\unsure{``|`}', 'misread symbol or index', 'medium',
       'The opener has two compact right-facing hooks fused along a dark left side. The two hooks favor a doubled opener, but a single curled stroke remains possible.', 24)
change('401-parenthesis-point', '401 l.-11, small point immediately left of the opening parenthesis', r'$(k-M)$', formula401,
       'drawing or diagram', 'high',
       'A separate black point lies below-right of the compact opener and immediately left of the opening parenthesis, at roughly the upper height of the k. The point is preserved once, separately from the quote uncertainty and from the parenthesis.', 24)
change('archive-corner-order', 'lower-left archive corner, comment only', '% archive sheet number: 29\n% The last figure can also be read as 3.',
       '% archive sheet number: 23 (possibly 29)', 'misread symbol or index', 'medium',
       'The final numeral has an open upper bowl and a broad lower return, which favor 3. A lightly closed or incomplete 9 remains possible. The decision uses the surviving strokes, not an expected sequence of corner numbers.', 25)

c_doubts = []
def cd(place, c, r, resolved, confidence, evidence, n=None, source=None, bbox=None):
    c_doubts.append({'place': place, 'c': c, 'reading': r, 'resolved': resolved,
                     'confidence': confidence, 'evidence': evidence, **loc(n, source, bbox)})

cd('372 l.17, explicit C doubt in the last word', r'\unsure{inverse|unverse|universe}', r'\unsure{inverse|unverse|universe}', False, 'low',
   'The e-r-s-e ending is readable. The initial connected minims have no securely separated i-dot and can still be segmented in more than one way; inverse remains favored. Neither wording context nor the material trace through the final e resolves the initial sequence.', 4)
cd('381 line reference, explicit C doubt in the older digit', r'\deleted{\unsure{8}}', r'\deleted{\unsure{8}}', False, 'low',
   'Closed upper and lower remnants are compatible with 8, but the live over-writing and crossing strokes prevent certainty about the earlier contour. Deletion/overwriting extent is certain; the old numeral is not.', 10)
cd('381 line reference, explicit C doubt in the live digit', r'\unsure{3|8}', '3', True, 'high',
   'The heavy live contour has an open left side, an upper right bowl, a middle return, and a lower right bowl ending in a leftward base. These surviving outer strokes decide 3; the closed parts belong to the underlying writing.', 10)
cd('385 Formula (7), explicit C doubt in the opening mark', r'\unsure{``|`|$+$}', r'\raisebox{1.1ex}[0pt][0pt]{$+$}', True, 'high',
   'The visible strokes cross each other transversely. A raised plus-shaped cross is the literal geometry; no quotation function is supplied.', 14)
cd('387 l-17, explicit C doubt in the cancelled ending', r'\deleted{\unsure{s}}', r'\deleted{\unsure{s}}', False, 'low',
   'A small curved body after the final e is crossed by dark oblique strokes. It is compatible with s, but its lower curve is covered. The deletion extends over this ending only, leaving commute and with live.', 16)
cd('page reference after 396, explicit C last-digit doubt', r'p.39\unsure{7|1}', r'p.39\unsure{7|1}', False, 'medium',
   'The last digit has a short leftward top and a long curved descending stem. That favors 7, but it is also compatible with a hooked 1; no neighboring page-number sequence is used.', 23)
cd('lower-left archive corner, C context alternative', '% archive sheet number: 29\n% The last figure can also be read as 3.', '% archive sheet number: 23 (possibly 29)', False, 'medium',
   'The upper bowl remains open on the left and the lower bowl is broad. The stroke reading favors 23 while retaining 29; the number stays in a comment.', 25)
cd('371 l.14, C context l or l. decision', 'l.14', 'l.14', True, 'medium',
   'A distinct short heavy stop-like group sits after the looped l and before 14, separate from the low l exit. Its horizontal spread is preserved by retaining the stop; the adjacent digit is a plain upright 1 followed by 4.', 1)
cd('372 first reference, C context l or l. decision', 'l.16', 'l 1.6', True, 'high',
   'There is no separate dark stop in the l-to-1 gap. The separate point is between 1 and 6 and is placed there literally.', 3)
cd('372 l.17, C context l or l. decision', 'l.17', 'l.17', True, 'high',
   'The upper half shows a small separate low point after the looped l and before the upright 1; the final numeral has the upper bar of 7.', source=HA, bbox=[735,121,850,181])
cd('372 l.21, C context l or l. decision', 'l.21', 'l.21', True, 'high',
   'The upper half separates the looped l, its low point, and the digits 2 and 1.', source=HA, bbox=[242,179,343,242])
cd('372 l.17, C context quotation framing', r"``with small \ldots{} and finite \unsure{inverse|unverse|universe}''", r"``with small \ldots{} and finite \unsure{inverse|unverse|universe}''", True, 'high',
   'The opening consists of two high strokes in the upper half; the closing pair is separately visible in crop 04. This decision concerns the quote edges only; the lexical doubt remains explicitly marked.', 4)
cd('383 l-9, C context quotation framing', "``much sense in bothering''", r"``much sense in bothering\unsure{''|'}", False, 'medium',
   'The opening pair before much is separately visible in the upper half. The closing group after bothering is compact and stays locally doubtful after its crop.', 11)
cd('372 l.17, C context baseline-dot count', r'with small \ldots{} and finite', r'with small \ldots{} and finite', True, 'high',
   'Exactly three separated low points follow small in the upper half.', source=HA, bbox=[984,127,1267,182])
cd('385 l6, first C context baseline-dot group', r'commutes with \ldots{} (resp.', r'commutes with \ldots{} (resp.', True, 'high',
   'The lower half separates three low points between with and the opening parenthesis.', source=HB, bbox=[520,157,788,220])
cd('385 l6, second C context baseline-dot group', r'resp. with\ldots{}', 'resp. with....', True, 'high',
   'The enlarged group after the second with contains four separate dark components, with white gaps between all four.', 13)
cd('373 row beginning its, C context section mark', r"line 3 of 101 ``no question of dealing'' \quad \S101 l.11", r"line 3 of 101 ``no question of dealing'' \quad \S101 l.11", True, 'high',
   'The first 101 follows of without a preceding sign. Before the second 101, two linked curved turns form the section sign; the following reference is l.11.', source=HA, bbox=[448,294,1389,370])
cd('379 l1, C context double underline and t crossbar', r'not ``to\'\' ``\uuline{with}\'\'', r'not ``to\'\' ``\uuline{with}\'\'', True, 'high',
   'Two distinct returned strokes lie below the complete word with. The higher stroke through to is its t crossbar, not a deletion of to.', source=HA, bbox=[388,623,728,698])
c_doubts[-1]['c'] = c_doubts[-1]['reading'] = r"not ``to'' ``\uuline{with}''"
cd('386 l.-11, C context underline', r'\uline{is}', r'\uline{is}', True, 'high',
   'The lower half shows one short rule under is only; it ends before well.', source=HB, bbox=[451,294,509,355])
cd('385 Formula (7), C context congruence sign', r'$\cong$', r'$\cong$', True, 'high',
   'A wave stands above two separate nearly horizontal bars. The sign is congruence as C encoded, and the word missing remains live to its right.', 14)
cd('401 l.-11, C context letters and delimiters', r'$(k-M)$', r'$(k-M)$', True, 'high',
   'Both delimiters are round. The k has one upright and two arms; the dash is one plain horizontal; M has one ordinary capital contour. The separate opener and point decisions are reported independently.', 24)
cd('382 l.7, C context typing-slip qualification', '(typing slip.)', '(typing slip.)', True, 'high',
   'The upper half reads typing slip with a low stop after slip and a closing parenthesis outside it. No source form for the alleged slip is supplied.', source=HA, bbox=[618,943,835,1002])
cd('388 l13, C context cancellation and surviving closing quotes', r"``equivalent \deleted{with}'' to''", r"``equivalent \deleted{with}'' to''", True, 'high',
   'The old w, short i, tall t and h remnants support with beneath the cancellation. The crossing ends below-left of the two closing quote strokes. Both that pair and the pair after live to remain outside the cancellation.', 17)

remaining = []
def rem(place, r, alternatives, confidence, reason):
    remaining.append({'place': place, 'reading': r, 'alternatives': alternatives, 'confidence': confidence, 'reason': reason})
rem('372 l.17 last word', r'\unsure{inverse|unverse|universe}', 'inverse; unverse; universe', 'low', 'The joined initial minims remain locally inseparable in crop 04.')
rem('373 l-13 opener', r'\unsure{``|`}', 'double opener; single bent opener', 'medium', 'A common apex joins the two limbs in crop 06.')
rem('381 older digit', r'\deleted{\unsure{8}}', '8 favored; earlier contour not securely recoverable', 'low', 'The live numeral and crossing obscure the old contour in crop 10.')
rem('381 short mark after l', r'\unsure{-|.}', 'dash; extended stop', 'medium', 'The short horizontal group is thick and slightly bent in crop 10.')
rem('383 l-9 closer', r"\unsure{''|'}", 'double closer; single bent closer', 'medium', 'The short left branch joins the long right stem in crop 11.')
rem('383 l-3 opener', r'\unsure{``|`}', 'double opener; single bent opener', 'medium', 'The high arch has one shared top in crop 12.')
rem('387 cancelled ending', r'\deleted{\unsure{s}}', 's favored; cancelled interior not certain', 'low', 'Crossing ink conceals the lower curve in crop 16.')
rem('388 terminal punctuation', r'usual\unsure{,|.}', 'comma; period', 'medium', 'The low oblique has a possible descending tail in crop 18.')
rem('395 l1 opener', r'\unsure{``|`}', 'double opener; single bent opener', 'medium', 'The unequal limbs meet at the top in crop 21.')
rem('395 l1 closer', r"\unsure{''|'}", 'double closer; single bent closer', 'medium', 'Two low tips share a fused body in crop 21.')
rem('397/391 page reference', r'p.39\unsure{7|1}', '397; 391', 'medium', 'The short top hook and curved stem fit either numeral in crop 23.')
rem('401 formula opener', r'\unsure{``|`}', 'double opener; single curled opener', 'medium', 'Two hook-like lobes merge along one edge in crop 24.')
rem('archive corner, comment only', '% archive sheet number: 23 (possibly 29)', '23; 29', 'medium', 'An open upper bowl favors 3, but incomplete closure of 9 remains possible in crop 25.')
rem('371 faint low group', first_word, 'geometrical group retained; origin and possible character identity unassigned', 'medium', 'The hook-and-cross geometry is visible, but its origin is not determined by crop 02.')
rem('386 pale low point', ref386, 'geometrical point retained; abbreviation-stop role or material origin unassigned', 'medium', 'The point is pale and displaced downward in crop 15.')
rem('394 isolated oval', with394, 'geometrical point retained; origin and punctuation role unassigned', 'high', 'The distinct oval is separate from the quote pair in crop 20.')
rem('396/397 right-margin spots', margin396, 'two separate spots retained; origin and function unassigned', 'high', 'No connector or letter body accompanies the two spots in crop 26.')
rem('401 point by parenthesis', formula401, 'separate point retained; origin and function unassigned', 'high', 'The point is visibly separate from both opener and parenthesis in crop 24.')

inventory = []
def inv(element, kind, position, words, hand='his hand', transcribed='yes'):
    inventory.append({'sheet_kind':'list','hand':hand,'element':element,'kind':kind,'position':position,
                      'first_words_or_objects':words,'transcribed':transcribed})

entries = [
('371 l.14','top row','didn\'t'),
('372 first reference','row 2 left','commutes with'),
('372 l.17','row 2 right','with small ... and finite'),
('372 l.21','row 3 left','commute with'),
('372 l-12','row 3 middle','commute with'),
('372 l-5','row 3 right','its'),
('373 l-13','row 4','recommendation'),
('373 l2','row 5 left','its'),
('373 line 3 of 101','row 5 middle','no question of dealing'),
('373 section 101 l.11','row 5 right, continuing at row 6 left','commuting with'),
('373 l-6','row 6 middle','its'),
('374 l10','row 7','commutation :.. with'),
('377 l.-15','row 8 left','its'),
('377 l-7','row 8 middle','won\'t'),
('377 l-3','row 8 right','don\'t'),
('378 l-7','row 9 left','interpret'),
('378 l-1','row 9 middle-right','commuting with'),
('379 l1','row 10 left','not to with'),
('379 l8','row 10 middle','made up of'),
('379 unnumbered quotation','row 10 right','commute with'),
('379 l.15','row 11','insufficient'),
('380 l.15','row 12','don\'t'),
('381 corrected reference','row 13','commuting with'),
('382 l.1','row 14 left','haven\'t'),
('382 l3','row 14 middle','hadn\'t'),
('382 l.5','row 14 right','breathe'),
('382 l.7','row 15 left-middle','covered (typing slip.)'),
('382 l14','row 15 right','out to prove'),
('383 l.10','row 16 left','inaccurate'),
('383 l11','row 16 middle','its'),
('383 l-10','row 16 right-middle','doesn\'t'),
('383 l-9','row 16 far right, continuing at row 17 left','much sense in bothering'),
('383 l-8','row 17 middle','invaluable'),
('383 l-3','row 17 right, continuing at row 18 left','suggest simply dropping'),
('384 l8','row 19','made up of'),
('385 l6','row 20 left-middle','commutes with ... (resp. with....)'),
('385 l-14','row 20 right','symmetrically'),
('385 Formula (7)','separate row 21 under p385','Formula (7), raised cross, congruence sign, missing'),
('386 l-11','row 22 left-middle','as is well known too'),
('386 l-6','row 22 right','without'),
('387 l-17','row 23 left','commute, cancelled ending, with'),
('387 l-3','row 23 right','commuting with'),
('388 l13','row 24','equivalent, cancelled with, to, is more usual'),
('390 l16','row 25','interpret'),
('392 l8','row 26 left','its'),
('392 l-1','row 26 middle','afraid'),
('393 l-10','row 27','didn\'t'),
('394 l-7','row 28','commutes with'),
('395 l1','row 29 left-middle','interpreted as saying is more usual'),
('395 l4','row 29 right','commute with'),
('395 l16','row 30','interpret'),
('396 l.-4','row 31','commute with again l-2.'),
('397/391 l-13','row 32','its also in l-12'),
('399 l6','row 33 left','commutes with'),
('399 l17','row 33 middle','analogue'),
('399 l19','row 33 right','its'),
('400 l-8','row 34','developed'),
('401 l.7','row 35 left','didn\'t.'),
('401 l.-11','row 35 right','(k-M)')
]
for i,(label,position,words) in enumerate(entries,1):
    inv(f'{i:02d}', 'text', f'{label}; {position}', words)
inv('60','text','nested in 379 l1, beneath with',r'\uuline{with}')
inv('61','deletion','nested in 381 reference, old numeral under live 3',r'\deleted{\unsure{8}}')
inv('62','insertion','nested in 381 reference, live numeral written over the older glyph','3, sharing the old numeral position')
inv('63','text','nested in the Formula (7) row, raised before congruence sign',r'\raisebox{1.1ex}[0pt][0pt]{$+$}')
inv('64','text','nested in 386 first quotation, beneath is',r'\uline{is}')
inv('65','deletion','nested in 387 l-17, after commute',r'\deleted{\unsure{s}}')
inv('66','deletion','nested in 388 l13, before live to',r'\deleted{with}')
inv('67','drawing','low before the first d in 371 l.14','faint hooked horizontal and crossing curved upright',hand='origin unassigned')
inv('68','drawing','below-right of l in 386 first reference','pale low point',hand='origin unassigned')
inv('69','drawing','right of 394 closing quotation, above the word baseline','isolated upright oval',hand='origin unassigned')
inv('70','drawing','right margin beside the gap between 396 and 397 rows','two separated diagonal spots',hand='origin unassigned')
inv('71','drawing','401 formula, immediately left of the opening parenthesis','isolated point',hand='origin unassigned')
inv('72','margin note','lower-left corner; archive number retained only as a comment','23, possibly 29',hand='another unnamed hand (archive numeral)')

notation = [
{'sign':'l and low points','location':'371 l.14; 372 references; 381; 386','reading':r'l.14; l 1.6; l.17; l.21; '+ref381+'; '+ref386,'evidence':'Crops 01, 03, 10 and 15 distinguish l exits, numeral strokes, short horizontal groups and detached points; the other two stops are clear in half a.'},
{'sign':r'\S101','location':'373 row beginning its','reading':r'line 3 of 101; \S101 l.11','evidence':'The second 101 alone has two linked curved turns before it; upper half.'},
{'sign':r'\ldots; ....','location':'372 l.17; 385 l6','reading':r'small \ldots{} and finite; commutes with \ldots{} (resp. with....)','evidence':'Half a shows three points after small; half b shows three before the parenthesis; crop 13 resolves four separate components after the second with.'},
{'sign':':..','location':'374 l10','reading':r'``commutation :.. with\'\'','evidence':'The upper half shows one upper point and three lower points: one colon followed by two further baseline dots.'},
{'sign':r'\uuline{with}; \uline{is}','location':'379 l1; 386 l-11','reading':r'\uuline{with}; \uline{is}','evidence':'The upper half separates two rules beneath with; the lower half has one rule beneath is.'},
{'sign':r'\cong','location':'385 Formula (7)','reading':r'$\cong$','evidence':'Crop 14 shows a wave above two separate horizontal bars.'},
{'sign':'raised cross','location':'385 before the congruence sign','reading':r'\raisebox{1.1ex}[0pt][0pt]{$+$}','evidence':'Crop 14 shows two transverse strokes at raised height; no arithmetic interpretation is inferred.'},
{'sign':r'$(k-M)$','location':'401 l.-11','reading':r'$(k-M)$','evidence':'Crop 24 separately confirms the round brackets, ordinary lowercase k, one dash and ordinary capital M.'},
{'sign':'overwritten reference','location':'381','reading':ref381,'evidence':'Crop 10 has one physical glyph position with a clear live 3 and buried loop remnants compatible with an old 8.'},
{'sign':'clear paired quotation groups','location':'371; 372 l-5; 377 l-7; 378 l-1; 380; 388; 395 l4','reading':r"``didn't''; ``its''; ``won't''; ``commuting with''; ``don't''; \deleted{with}'' to''; ``commute with''",'evidence':'Crops 02, 05, 07, 08, 09, 17 and 22 independently resolve separate or distinctly double-limbed groups at the stated locations.'},
{'sign':'compact quotation groups','location':'373 l-13; 383 l-9 and l-3; 395 l1; 401 l.-11','reading':r"\unsure{``|`}recommendation''; bothering\unsure{''|'}; \unsure{``|`}suggest; \unsure{``|`}interpreted as saying\unsure{''|'}; \unsure{``|`}",'evidence':'Crops 06, 11, 12, 21 and 24 leave local fused groups uncertain. No count is transferred from another occurrence.'},
{'sign':'i dot distinct from quotation','location':'392 l8','reading':"``its''",'evidence':'Crop 19 shows two tall marks at the left, then a shorter slanted i-dot nearer the i stem; the third high mark is not added again as a third quote.'},
{'sign':'single opening strokes','location':'377 l-3; 382 l.7; 383 l-10; 387 l-3','reading':r"`don't''; `covered''; `doesn't''; `commuting with''",'evidence':'The assigned halves show one opening stroke at each occurrence, independently; the double closing groups remain visible.'},
{'sign':'unassigned geometric marks','location':'371; 386; 394; right margin beside 396/397; 401','reading':first_word+'; '+ref386+'; '+with394+'; '+margin396+'; '+formula401,'evidence':'Crops 02, 15, 20, 26 and 24 preserve the observed geometry without assigning letters, a punctuation function, or an origin.'}
]
notation[3]['reading'] = r"``commutation :.. with''"

report = {
    'scan':30,
    'reader':'C',
    'model':'GPT-6 Astra Pro',
    'effort':'not exposed',
    'viewed':[WHOLE,HA,HB],
    'layout': 'One full handwritten correction-list sheet in one principal hand, with page references down the left and 35 physical writing rows. Several rows contain multiple correction entries; 373 commuting with, 383 much sense in bothering, and 383 suggest simply dropping continue onto later physical rows. The separate Formula (7) row lies below the p385 entries. There are two nested underline spans, an overwritten reference at 381, a cancelled ending at 387, and a whole cancelled with at 388. No mathematical diagram or free-standing picture is present. Small unassigned marks occur before the first correction, by two later references/formulae, after the 394 quotation, and in the right margin. Two nearly vertical pale/dark strips near whole-image x212 and x1490 run through most of the sheet, dark near the top and fading lower down; crops 22 and 27 show broad shadow/highlight character consistent with material creases rather than pen rules. The small grey two-lobed lower-right spot in crop 28 has a light surrounding rim and discolored lower halo and is treated as a material feature, not writing. The archive numeral is at the lower-left corner in another hand. Black photographic surround is visible at the paper edges.',
    'changes': changes,
    'c_doubts': c_doubts,
    'remaining_doubts': remaining,
    'inventory': inventory,
    'notes': [
        'The sheet is an English wording/typographic correction list citing pages 371 through 401; it has no visible title, date, or manuscript page heading.',
        'Repeated corrections use commute/commutes/commuting with, and entries also request interpret, made up of, its, and contractions. The 379 l1 entry explicitly sets not to beside doubly underlined with.',
        'At 372 l.17 the last word after finite remains lexically uncertain. The literal point in the preceding reference is between the digits 1 and 6.',
        'At 382 l.7, covered is followed by the qualification (typing slip.). The alleged source typo is not written on this page.',
        'At 385, Formula (7) is followed by a raised cross-shaped mark, a congruence sign, a closing quote pair and missing. The referenced formula itself is not reproduced.',
        'At 388 l13, with is cancelled after equivalent, to remains live, and the note says is more usual. Both closing quote groups remain live. The terminal low punctuation is comma/period uncertain.',
        'At 395 l1, interpreted as saying is also described as more usual. At 396 the note adds again l-2.; at the following 39[7/1] reference it adds also in l-12.',
        'The final entry quotes (k-M) at 401 l.-11. The sheet supplies no argument or mathematical step to verify; no mathematical proof/check event is claimed.',
        'The lower-left archive numeral is read from its own strokes as 23, possibly 29, and is preserved only in a comment.'
    ],
    'math_checks': [],
    'notation': notation,
    'abbreviations': [
        {'form':'p, p., p-','expansion':'page (tentative expansion, list only)','place':'page-reference column throughout'},
        {'form':'l, l.','expansion':'line (tentative expansion, list only)','place':'line references throughout; literal point placement varies'},
        {'form':'resp.','expansion':'respectively (tentative expansion, list only)','place':'385 l6'}
    ],
    'brief_feedback': 'Applied brief v14 and the supplied conventions. The whole image was displayed once, then half a once and half b once. Twenty-eight unresolved loci were frozen in frozen_unresolved.json before crop generation; crop.py produced one crop per locus and every one was then displayed singly, with no repeat crop or page-image reopening. The requested context addendum and refreshed C_context.md were read when supplied; the mistakenly extracted scan033 and scan031 rows were disregarded. H has description-only status, so every change has h=null and diff_h=false; there are no manufactured H collation rows. Inventory coverage is one row per correction entry, followed by separate nested underline, overwrite, deletion, raised-mark, unassigned-mark and archive-comment rows. Material creases and the lower-right material spot are described in layout rather than redrawn as ink. All literal alterations are listed in changes. No OCR, recognition library, outside research, other-reader output, other-page image, or LaTeX compilation was used.'
}
(OUT / 'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'reading':str(OUT/'reading.tex'),'report':str(OUT/'report.json')}))
