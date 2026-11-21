import csv
import json
import re
from pathlib import Path

BASE = Path('/workspace/scratch/8132fe1cca43/work/SP82_C13_148/readers/148_scan036')
PACKET = Path('/workspace/scratch/8132fe1cca43/work/packets/148_scan036')
plan = {x['label']: x for x in json.loads((BASE / 'crop_plan.json').read_text())}
candidate_path = BASE / 'candidate.tex'
candidate = candidate_path.read_text()
candidate = candidate.replace(r'\deleted{muni d’un}', r'\deleted{muni d’}')
candidate_path.write_text(candidate)
figures = re.findall(r'\\figure\{(\\begin\{tikzpicture\}.*?\\end\{tikzpicture\})\}', candidate, re.S)
assert len(figures) == 3
sphere, chart, bottom = figures
changes = []
unresolved = []

def change(place, c, h, final, ink, label, confidence='high', kind='misread word',
           against_c=False, against_h=True, math=False):
    p = plan[label]
    changes.append(dict(place=place, c=c, h=h, final=final, ink=ink,
                        crop=p['crop'], box=p['box'], confidence=confidence,
                        kind=kind, against_c=against_c, against_h=against_h, math=math))

def doubt(place, reading, issue, alternatives, label, confidence='low'):
    p = plan[label]
    unresolved.append(dict(place=place, reading=reading, issue=issue,
                           alternatives=alternatives, confidence=confidence,
                           crop=p['crop'], box=p['box']))

change('a: short word after on trouve', 'ainsi', 'essent.',
       r'ess.\textsuperscript{t}',
       'The short run has an e-like opening, two small s curves, a low dot and a separate raised t; it does not contain the full written sequence essent.',
       'a_text', kind='abbreviation expanded or spelling modernised', against_c=True)
change('a: whole symmetric-square formula',
       r'M_{0,5}^{!}\simeq\mathrm{Sym}_2^*(\unsure{U_{0,3}|M_{0,3}})',
       r'M^{!}_{0,5}\simeq\mathrm{Sym}^{*}_{2}(M_{0,3})',
       r'M_{0,5}^{!}\simeq\mathrm{Sym}_2^*(U_{0,3})',
       'The argument begins with a single descending stroke turning around a rounded bottom into the right stem: U, without the two upper peaks of the preceding M. The indices 0,3, the subscript 2, the separate crossed star and the exclamation mark over M were read together.',
       'a_formula', kind='misread symbol or index', against_c=True, math=True)
change('a: cancellation ends before de',
       r'\deleted{\unsure{Le cas|un cas}} de',
       r'\struck{Le cas de}',
       r'\deleted{\unsure{Le cas|un cas}} de',
       'The horizontal cancellation traverses the short initial fragment and ends before the separate d stem and e of de. The struck fragment itself remains uncertain.',
       'a_second', kind='deletion state')
change('a: dimension abbreviation', 'dim', r'\uncertain{dimension}', 'dim',
       'Only the short d-i-m run is written before réelle; there is no ension continuation.',
       'a_second', kind='abbreviation expanded or spelling modernised')
change('b: supposed cancellation before En', '', r'\struck{\ill{}}', '',
       'Between the stop after 3 and the large E of En is unmarked paper; no cancelled word appears there.',
       'b_start', kind='text not on the page')
change('b: pour before repère', 'pour', r'\struck{\ill{}}', 'pour',
       'The small p-led joined run between prenant and repère is live writing. No independent cancellation crosses it.',
       'b_start', kind='deletion state')
change('b: que at start of formula line', 'que', '', 'que',
       'A descending q and the following joined u-e run stand before the large K.',
       'b_formula', kind='omission')
change('b: dimension abbreviation after Poincaré', 'dim', 'dimension', 'dim',
       'The word between the comma after Poincaré and réelle consists of the short dim run only.',
       'b_formula', kind='abbreviation expanded or spelling modernised')
change('left oblique margin: initial OPS', 'OPS', '', 'OPS',
       'An open oval O is followed by the tall P stroke and the crossing curved S form before the first sigma.',
       'margin', kind='omission')
change('left oblique margin: cancelled lower line',
       r'\deleted{\unsure{pour \(\nu=3\)}}',
       r'\ill{} \(\sigma z=\bar z\)',
       r'\deleted{\unsure{pour} \(\sigma z=\bar z\)}',
       'Below the live equation a long horizontal strike crosses a descending initial word, then a loop-and-arm sigma, a z, two equality bars and a final z with a separate bar above it. The lower formula repeats the live equation; the struck initial word is not fully separable.',
       'margin', confidence='medium', kind='misread symbol or index', against_c=True, math=True)
change('c: initial capital in Card', r'\operatorname{card}', r'\mathrm{card}', r'\operatorname{Card}',
       'The initial letter of this occurrence is a large open C, rising to the height of the neighbouring K. The b occurrence begins with a smaller c.',
       'c_start', kind='other', against_c=True)
change('c: tiny cancelled fragment after i.e.', r'\deleted{\unsure{?}}', '',
       r'\deleted{\unsure{?}}',
       'A small dense, vertically retraced fragment lies between e and the next K. Its former character cannot be securely separated.',
       'c_start', confidence='low', kind='omission')
change('c: interlinear Soit and set-complement formula',
       r'\inserted{Soit \(K\setminus K^\sigma=I\)}',
       r'\struck{\ill{} \(K\setminus K^\sigma=I\), ...}',
       r'\inserted{\unsure{Soit} \(K\setminus K^\sigma=I\),}',
       'The K-complement-I formula stands above the long strike through the lower sentence; the strike does not traverse the formula. The short initial word is heavily retraced and remains doubtful. The I has separate broad upper and lower bars.',
       'c_insert_delete', confidence='medium', kind='insertion or placement', math=True)
change('c: first cancelled line below the insertion',
       r'\deleted{on prend \unsure{comme repère} \(\infty\),}',
       r'\struck{\ill{} \ill{} \ill{} \ill{} \ill{} \ill{}}',
       r'\deleted{on prend \unsure{comme repère} \(\infty\),}',
       'Below the inserted formula, the cancelled line retains the beginning on prend, the separated descenders and uprights of the doubtful middle run, and a two-part terminal infinity form. The high strokes near the inserted comma belong to the rising cancelled repère run below.',
       'c_insert_delete', confidence='medium', kind=r'readable ink left as \ill{}')
change('c: point abbreviation in cancelled choice of 0', 'pt', 'pt', r'p\textsuperscript{t}',
       'The p descends below the baseline, while the separate t is placed above its shoulder, before the following 0.',
       'c_delete2', kind='abbreviation expanded or spelling modernised', against_c=True)
change('c: cancelled equation defining 0', r'0=\sigma0', r'0=\infty', r'0=\sigma0',
       'After the equality are two distinct forms: the hooked sigma with a horizontal arm and a separate closed 0. They are not joined into one infinity sign.',
       'c_delete2', kind='misread symbol or index', math=True)
change('c: preposition before une sphère', 'sur', 'dans', 'sur',
       'The short run after pts has low connected curves and no tall d stem; the visible shapes support sur.',
       'c_firstline')
change('c: cancellation scope before the live un',
       r'\deleted{muni d’un} \inserted{\unsure{admettant}} un',
       r'\struck{\ill{}} \uncertain{donc}',
       r'\deleted{muni d’} \inserted{\unsure{admettant}} un',
       'The cancellation ends after the d and apostrophe. A single un stands to its right, before antiautomorphisme; no second cancelled un is visible beneath the insertion.',
       'c_main1', kind='deletion state', against_c=True)
change('c: inserted word over muni d’',
       r'\inserted{\unsure{admettant}} un', r'\uncertain{donc}',
       r'\inserted{\unsure{admettant}} un',
       'The raised word contains a low initial curve and several taller stems, compatible with admettant; it occupies the insertion above the cancelled phrase. The separate live un follows it. The cramped interior joins leave the insertion doubtful.',
       'c_main1', confidence='medium', kind='misread word')
change('c: singular antiautomorphisme', 'antiautomorphisme', r'\uncertain{antiautomorphismes}',
       'antiautomorphisme',
       'The long joined word ends in the small m-e run, followed by space before the dense cancelled sign; no separate terminal s is visible.',
       'c_main1')
change('c: cancelled sign before involutif', r'\deleted{\(\unsure{\sigma}\)}', r'\ill{}',
       r'\deleted{\(\unsure{\sigma}\)}',
       'The dense cancelled glyph has a loop and projecting strokes, but the underlying sigma cannot be isolated with certainty.',
       'c_main1', confidence='low', kind=r'readable ink left as \ill{}', math=True)
change('c: involutif', 'involutif', r'\ill{}', 'involutif',
       'The word has a dotted initial i, joined low middle strokes, a tall l and a long terminal f descending to the right.',
       'c_main1', kind=r'readable ink left as \ill{}')
change('c: singular quoted conjugaison', "conjugaison", r'\uncertain{conjugaisons}',
       chr(96)*2 + "conjugaison''",
       'The final run ends in on before the closing pair of short raised quotation strokes; no final s follows it. The source uses paired quotation marks, not guillemets.',
       'c_main1')
change('c: dimension abbreviation after et de', 'dim', 'dimension', 'dim',
       'At the end of the line only the abbreviated dim is written before modulaire on the following line.',
       'c_main1', kind='abbreviation expanded or spelling modernised')
change('c: point abbreviation after choix d’un', 'pt', 'pt', r'p\textsuperscript{t}',
       'The p has its long downward stroke, with a small t raised to its upper right rather than set on the baseline.',
       'c_modulaire_line', kind='abbreviation expanded or spelling modernised', against_c=True)
change('c: dotted dimension abbreviation after fait une', 'dim.', 'dimension', 'dim.',
       'The short dim run is followed by a visible separate dot before de.',
       'c_main2', kind='abbreviation expanded or spelling modernised')
change('c: dimension abbreviation after soit', 'dim', 'dimension', 'dim',
       'Only the short dim run stands between soit and réelle; no expanded ending is written.',
       'c_main2', kind='abbreviation expanded or spelling modernised')
change('c: capital at start of final parenthesis', 'contient', r'\uncertain{Contient}', 'Contient',
       'Immediately after the opening parenthesis is a tall open C; the following letters are the joined ontient run.',
       'c_main2', kind='other', against_c=True, against_h=False)
change('left sphere: contour and equator',
       r'\draw(0,0)circle(1); \draw(-1,0)arc[start angle=180,end angle=360,x radius=1,y radius=.25]; \draw[densely dotted](-1,0)arc[start angle=180,end angle=0,x radius=1,y radius=.25];',
       'A sphere with its equator, rear part in dashes, and a marked point at the right.',
       sphere,
       'The outer contour stops on both sides of a broad lower-right gap. The rear equator has short separate strokes on the left and a long continuous right segment, while the front arc stops short of the dark right point.',
       'sphere', kind='drawing or diagram', against_c=True, against_h=False, math=True)
change('lower chart: abbreviated heading', 'dim mod', 'dimension modulaire', r'\shortstack{dim\\mod}',
       'The heading is two short written runs, dim above mod. There are no expanded endings.',
       'chart', kind='abbreviation expanded or spelling modernised')
change('lower chart: first graph small endpoint and retrace',
       r'\foreach \x/\y in {-1/.5,-.6/1,0/1.5,.7/1.5,1/.6}{\draw(0,0)--(\x,\y);}',
       'One vertex with five free branches.',
       r'\begin{tikzpicture}[x=.009cm,y=-.009cm]\draw(174,1753)--(85,1705)--(84,1715);\draw(174,1753)--(120,1648);\draw(174,1753)--(217,1595);\draw(178,1740)--(199,1668);\draw(174,1753)--(292,1607);\draw(174,1753)--(300,1680);\fill(174,1753)circle(1.9pt);\end{tikzpicture}',
       'There are five free endpoints. The lowest left endpoint turns down briefly, and a short narrow retrace accompanies the steep central branch near the vertex; the retrace does not create another free endpoint.',
       'chart', kind='drawing or diagram', against_c=True, against_h=False, math=True)
change('lower chart: third graph middle branches and baseline gap',
       r'\draw(0,0)--(1,0)--(2.5,0); \draw(1,0)--(1,1); \draw[thick](1.05,.1)--(1.5,1); \draw(1.1,.2)--(1.2,.5)--(1.3,.5)--(1.4,.8);',
       'The free edge of the middle vertex is crossed by a small oblique tick.',
       r'\begin{tikzpicture}[x=.009cm,y=-.009cm]\draw(694,1750)--(780,1750);\draw(794,1750)--(916,1748);\draw(780,1750)--(779,1669);\draw(783,1750)--(827,1676);\draw(825,1679)--(808,1692)--(821,1689)--(795,1714)--(812,1707)--(800,1723)--(796,1733)--(803,1733);\fill(780,1750)circle(2pt);\end{tikzpicture}',
       'A vertical free branch and a separate sloping branch leave the middle region. Several zigzag crossings run along the sloping branch; they are not a single tick across the upright. A small white interval separates the middle dark vertex from the baseline continuing to the right.',
       'chart', kind='drawing or diagram', against_c=True, math=True)
change('lower chart: live realizations label',
       r'\unsure{modulaires|spéciales}', 'spéciales',
       r'\unsure{modulaires|spéciales}',
       'The beginning has low connected m-like humps, without the initial p descender required by spéciales. Later joins run into the cancelled word below, so the full first reading remains uncertain.',
       'chart', confidence='medium')
change('lower chart: cancelled word under realizations',
       r'\deleted{\unsure{polyédriques}}', r'\ill{}',
       r'\deleted{\unsure{polyédriques}}',
       'The crossed lower word retains tall strokes and descenders compatible with polyédriques, but the crossing and overlap prevent a complete letter-by-letter resolution.',
       'chart', confidence='low', kind=r'readable ink left as \ill{}')
change('lower chart: vertical rule beside middle computations', '', '',
       r'\begin{tikzpicture}[x=.009cm,y=-.009cm]\draw(361,1943)..controls(357,2015)and(368,2082)..(360,2141);\end{tikzpicture}',
       'A single continuous vertical stroke stands to the left of both middle-column computations, ending below the second equation.',
       'chart', kind='drawing or diagram', against_c=True, math=True)
change('lower chart: curve following the first 60',
       r'\unsure{(}', '', r'\unsure{(|c}',
       'A separate small curve opens to the right after 60. It can be an opening parenthesis; its status is not secure and no closing mate is visible.',
       'chart', confidence='low', kind='omission', math=True)
change('lower chart: cancelled caption below 120',
       r'\deleted{\unsure{tétraèdre-pyramide}}',
       r'\struck{(tétraédrales \ill{})}',
       r'\deleted{\unsure{tétraèdre-pyr|tétraèdre-pyramide}}',
       'A long strike crosses the caption. The right-hand part after the long connecting stroke retains a descending p and a short following run; a full pyramide ending is not independently legible. The shorter reading is kept alongside C’s longer possibility.',
       'chart', confidence='low', kind='misread word', against_c=True)
change('lower chart: first word of lower parenthesis',
       r'\unsure{tétraèdre}', r'\uncertain{pentagonales}',
       r'\unsure{tétraèdre|pentagonales}',
       'The retouched word shows tall crossed stems and small accent strokes. Its initial and interior joins are too dense to separate every letter; tétraèdre is favoured but not resolved.',
       'chart', confidence='medium')
change('lower chart: end of lower parenthesis', '-pointées', r'\ill{}', '-pointées',
       'After the connecting hyphen a long p descender leads into the joined pointées run, followed by a separate closing parenthesis.',
       'chart', confidence='medium', kind=r'readable ink left as \ill{}')
change('lower chart: isolated cancelled words at left',
       r'\deleted{\unsure{les types}}', 'un mot biffé',
       r'\deleted{\unsure{les types}}',
       'The small dense cancelled fragment has several tall strokes and a right descender; les types remains only a tentative reading, with no complete recovery of its letters.',
       'chart', confidence='low', kind=r'readable ink left as \ill{}')
change('NB: words before pyramidales', 'Nb de structures',
       r'\ill{} \ill{} \uncertain{de} \uncertain{structures}', 'Nb de structures',
       'After the underlined NB, a separate N and lower b are followed by the short de and the long joined structures run.',
       'chart', kind=r'readable ink left as \ill{}')
change('NB: punctuation between the two structure lines', '', '; ... .', '',
       'The first count ends with 30 and the second with 20. No semicolon after 30 or terminal full stop after 20 is visible.',
       'chart', kind='text not on the page')
change('lower chart: endpoints of the two long curved arrows',
       r'5\times3\times2=30\arrow[uuuurr,bend right=55];\quad10\times2=20\arrow[uuuuur,bend left=40]',
       'Curved arrows connect columns 1 and 0.',
       r'\begin{tikzpicture}[x=.009cm,y=-.009cm]\draw(1181,2253)..controls(1330,2040)and(1272,1818)..(981,1734);\draw(981,1734)--(978,1760);\draw(981,1734)..controls(1000,1729)and(1020,1730)..(1037,1735);\draw(536,1797)..controls(647,1809)and(686,1889)..(659,2076);\draw[black!45](659,2076)..controls(636,2164)and(602,2323)..(623,2377);\draw(623,2377)..controls(627,2390)and(633,2395)..(638,2399);\draw(536,1797)--(548,1811);\draw(536,1797)..controls(550,1799)and(568,1794)..(579,1791);\end{tikzpicture}',
       'The outer curve begins near the pyramidales count and has its head beside the third graph. The inner curve reaches down to the bitétraédrales line and has its head below the second graph. Neither line joins one graph column directly to the other.',
       'chart', kind='drawing or diagram', math=True)
change('bottom sketch: outer loop direction and missing strokes',
       r'\draw[->](-.55,.4)..controls(-1.3,.1)and(-1.1,-.5)..(.1,-.35);',
       'A triangle in an oval, arrowheads on two sides and a small ring near the top.',
       bottom,
       'The outer curve has a free lower end and a pointed upper end at the left sloping edge, reversing C’s direction. The rear base is broken and pale; the small upper circuit has separated rear strokes and dark projecting contacts. The front lower edge bears a visible open head.',
       'bottom_drawing', kind='drawing or diagram', against_c=True, against_h=False, math=True)
change('bottom sketch: central glyph', r'\unsure{\sigma}', 'un chiffre',
       r'\unsure{\sigma}',
       'The central mark is an open rounded loop with a thick inward-turning upper-right end. It does not securely distinguish a sigma, a digit, or a direction mark.',
       'bottom_drawing', confidence='low', kind='misread symbol or index', math=True)
change('bottom-left foliation', r'\mspage{35}', '', r'\margin{35}',
       'Two light handwritten numerals stand above the perforations: a double-curved 3 and a 5 with a long upper turn. They are lighter and separate from the manuscript’s top page number.',
       'folio35', kind='omission')

doubt('a: cancelled opening fragment', r'\deleted{\unsure{Le cas|un cas}}',
      'The long strike obscures some short joining strokes. The tall initial favours Le, but not every struck letter is independently clear.',
      ['Le cas', 'un cas'], 'a_second', 'medium')
doubt('left oblique margin: cancelled initial word', r'\deleted{\unsure{pour}}',
      'The descending first stroke and remaining low run support pour, but the strike hides the internal joins.',
      ['pour'], 'margin', 'medium')
doubt('c: tiny cancelled fragment after i.e.', r'\deleted{\unsure{?}}',
      'The dense retracing does not reveal the former character.', ['?', 'unidentified cancelled character'], 'c_start')
doubt('c: first word of insertion', r'\unsure{Soit}',
      'The initial and interior letters have been heavily retraced; Soit remains the readable proposal rather than a secure resolution.',
      ['Soit'], 'c_insert_delete', 'medium')
doubt('c: middle of first cancelled line', r'\deleted{\unsure{comme repère}}',
      'The rising strike runs through the letter bodies. The ascenders and descenders admit the phrase but do not expose every letter.',
      ['comme repère'], 'c_insert_delete', 'medium')
doubt('c: inserted word over muni d’', r'\unsure{admettant}',
      'The raised word is cramped against the cancelled line and its internal joins remain uncertain.',
      ['admettant'], 'c_main1', 'medium')
doubt('c: cancelled sign before involutif', r'\deleted{\(\unsure{\sigma}\)}',
      'A dense crossed loop remains; the original sigma cannot be isolated.',
      [r'\sigma', 'unidentified cancelled sign'], 'c_main1')
doubt('lower chart: live realizations label', r'\unsure{modulaires|spéciales}',
      'The low initial humps favour modulaires, but the rest overlaps cancelled writing.',
      ['modulaires', 'spéciales'], 'chart', 'medium')
doubt('lower chart: cancelled word under realizations', r'\deleted{\unsure{polyédriques}}',
      'Heavy crossing strokes obscure the interior letters and the exact overlap with the upper label.',
      ['polyédriques'], 'chart')
doubt('lower chart: mark following first 60', r'\unsure{(|c}',
      'A small isolated right-opening curve has no visible closing mate; whether it is punctuation or a letter is unsettled.',
      ['(', 'c'], 'chart')
doubt('lower chart: cancelled caption', r'\deleted{\unsure{tétraèdre-pyr|tétraèdre-pyramide}}',
      'The right end is a short crossed run after a p descender; no full ending can be securely separated.',
      ['tétraèdre-pyr', 'tétraèdre-pyramide', 'tétraédrales followed by unread text'], 'chart')
doubt('lower chart: first word of lower parenthesis', r'\unsure{tétraèdre|pentagonales}',
      'Retouching masks several joins. The taller stems favour tétraèdre, while the competing H reading is retained for blind review.',
      ['tétraèdre', 'pentagonales'], 'chart', 'medium')
doubt('lower chart: isolated cancelled words at left', r'\deleted{\unsure{les types}}',
      'The cancellation is too dense for a complete letter-by-letter recovery.',
      ['les types'], 'chart')
doubt('NB: earlier state under the last factor 2', '2',
      'The present 2 is clear and heavily retraced. An earlier numeral cannot be separated from the thickened strokes; no former digit is supplied.',
      ['retraced 2', '2 over an unidentified earlier digit'], 'chart', 'medium')
doubt('bottom sketch: central glyph', r'\unsure{\sigma}',
      'The open rounded form with an inward upper-right hook does not securely identify its alphabet or status.',
      [r'\sigma', '0', '3', 'curved orientation mark'], 'bottom_drawing')

def decision(id_, decision_, reading, ink, label, confidence):
    p = plan[label]
    return dict(id=id_, decision=decision_, reading=reading, ink=ink,
                crop=p['crop'], box=p['box'], confidence=confidence)

decisions = [
    decision('M0461', 'first', r'U_{0,3}',
             'The argument has the descending-and-returning U outline rather than the two peaks of M. The whole neighbouring formula, including !, star and indices, was inspected.', 'a_formula', 'high'),
    decision('M0462', 'undecided', r'\unsure{admettant}',
             'A low initial curve and several taller stems admit admettant; the cramped joins in the interlinear word remain unresolved.', 'c_main1', 'medium'),
    decision('M0463', 'undecided', r'\unsure{modulaires|spéciales}',
             'Initial low m-like humps favour modulaires; the remaining letters overlap the crossed lower word and do not resolve the whole reading.', 'chart', 'medium'),
    decision('M0464', 'undecided', r'\unsure{(|c}',
             'The separate small curve opens to the right. Its form fits an opening parenthesis, but there is no closing mate and its status remains uncertain.', 'chart', 'low'),
    decision('M0465', 'undecided', r'\unsure{tétraèdre|pentagonales}',
             'The retouched word retains tall stems and small accent strokes, but several joins are hidden. Tétraèdre is favoured without resolving the whole word.', 'chart', 'medium'),
    decision('M0466', 'undecided', r'\unsure{\sigma}',
             'An open rounded loop turns inward at its thick upper-right end. No secure distinction between letter, digit and graphical direction mark follows from those strokes.', 'bottom_drawing', 'low'),
]

inventory = []
def inv(element, kind, position, first, hand='his hand'):
    inventory.append(dict(element=element, kind=kind, position=position,
                          first_words_or_objects=first, sheet_kind='text',
                          hand=hand, transcribed='yes'))

inv('author pagination', 'margin note', 'top centre', '3')
inv('case a opening and formula', 'text', 'upper page, first line', r'a) K^\sigma=K — on trouve ess.^t')
inv('case a symmetric-square formula', 'display', 'right end of first line', r'M_{0,5}^{!}\simeq\mathrm{Sym}_2^*(U_{0,3})')
inv('case a cancelled fragment', 'deletion', 'start of second line', 'Le cas|un cas')
inv('case a dimension and case reference', 'text', 'second line and its lower right continuation', 'de dim réelle 2 : contient le cas 1° (pentagonal)')
inv('case b introduction', 'text', 'upper third', r'b) card K^\sigma=3. En prenant pour repère')
inv('case b set and parameter line', 'display', 'below case b introduction', r'que K=\{0,1,\infty,\lambda,\bar\lambda\}')
inv('case b case reference', 'text', 'below its parameter formula', 'Contient le cas 3° (bitétraédral)')
inv('left oblique marginal note', 'margin note', 'left margin beside case b', r'OPS \sigma z=\bar z')
inv('cancelled lower marginal line', 'deletion', 'beneath live oblique equation', r'pour \sigma z=\bar z')
inv('case c introduction', 'text', 'middle upper page', r'c) Card K^\sigma=1, i.e.')
inv('tiny cancelled character', 'deletion', 'between i.e. and second K', '?')
inv('case c interlinear insertion', 'insertion', 'above first long cancelled line', r'Soit K\setminus K^\sigma=I,')
inv('case c first cancelled line', 'deletion', 'under the insertion', r'on prend comme repère \infty,')
inv('case c second cancelled line', 'deletion', 'next line', r'et on choisit un p^t 0 tel que 0=\sigma0. OP')
inv('four-point system paragraph', 'text', 'central prose block', r'(\Sigma,I) est un syst. de 4 pts sur une sphère complexe')
inv('cancelled participial phrase', 'deletion', 'start of next paragraph line', 'muni d’')
inv('replacement participial word', 'insertion', 'above muni d’', 'admettant')
inv('cancelled sign after antiautomorphisme', 'deletion', 'before involutif', r'\sigma')
inv('real dimension argument', 'text', 'lower lines of central prose', 'involutif (conjugaison), ils sont bien connus')
inv('pyramidal case parenthesis', 'text', 'above lower chart', 'Contient le cas pyramidal carré, 2°')
inv('sphere sketch', 'drawing', 'left of central prose', 'open lower-right outer contour, equator, right dark point')
inv('lower chart heading', 'text', 'top left of chart', 'dim / mod; 2, 1, 0')
inv('one-vertex graph', 'drawing', 'first chart column', 'one dark vertex and five free branches')
inv('two-vertex graph', 'drawing', 'second chart column', 'two dark vertices, joining edge, three plus two free branches')
inv('three-vertex graph', 'drawing', 'third chart column', 'three dark vertices, horizontal chain, free branches')
inv('cancelled extra sloping branch', 'deletion', 'at middle vertex of third graph', 'oblique branch with zigzag crossings')
inv('component-count row', 'text', 'under graphs', 'nb comp.; 1, 10, 15')
inv('realization-count label', 'text', 'left below component row', 'nb réalisations modulaires|spéciales')
inv('cancelled word beneath realization label', 'deletion', 'left below réalisations', 'polyédriques')
inv('first-column realization count', 'display', 'under first graph', '12')
inv('middle first computation', 'display', 'under second graph', r'10\times3\times2=60')
inv('small open curve after 60', 'text', 'right of first middle result', '(')
inv('middle second computation', 'display', 'below first middle computation', r'+10\times2\times6=120')
inv('vertical rule beside computations', 'drawing', 'left edge of middle-column calculations', 'single tall stroke')
inv('third-column computation', 'display', 'under third graph', r'15\times2\times2=60')
inv('cancelled upper caption', 'deletion', 'below 120', 'tétraèdre-pyr|tétraèdre-pyramide')
inv('lower parenthetical caption', 'text', 'beneath cancelled upper caption', '(tétraèdre|pentagonales-pointées)')
inv('isolated left cancelled words', 'deletion', 'below left chart label', 'les types')
inv('NB structure counts', 'text', 'below chart', 'NB Nb de structures pyramidales; bitétraédrales')
inv('pyramidal count', 'display', 'first NB line', r'5\times3\times2=30')
inv('bitétraédrale count', 'display', 'second NB line', r'10\times2=20')
inv('outer curved leader', 'drawing', 'right of chart', 'pyramidales count to third graph')
inv('inner curved leader', 'drawing', 'through chart middle', 'bitétraédrales line to second graph')
inv('bottom small sketch', 'drawing', 'low centre', 'pyramidal outline, small upper circuit, outer loop, doubtful central sigma')
inv('bottom foliation', 'margin note', 'bottom left above perforations', '35', 'another unnamed hand')

notes = []
def note(id_, kind, text, place, status='observed'):
    notes.append(dict(id=id_, statement_id=id_, kind=kind, text=text, place=place, status=status))

note('S036-C01', 'claim', r'Case a writes K^\sigma=K, identifies the resulting real points with M_{0,5}^{!}\simeq Sym_2^*(U_{0,3}), and gives real dimension 2 and case 1° (pentagonal).', 'case a', 'transcribed, not mathematically checked')
note('S036-C02', 'claim', r'Case b writes card K^\sigma=3, chooses 0,1,infinity in K^\sigma and writes K={0,1,infinity,lambda,bar lambda}, with lambda in the Poincaré half-plane, real dimension 2, and case 3° (bitétraédral).', 'case b', 'transcribed, not mathematically checked')
note('S036-C03', 'claim', r'Case c writes Card K^\sigma=1 and K^\sigma={P}; the live interlinear formula sets I=K\setminus K^\sigma. The cancelled construction includes 0=sigma 0.', 'case c', 'transcribed, not mathematically checked')
note('S036-C04', 'claim', 'The paragraph says that the four-point system on a complex sphere admits an involutive antiautomorphism, called conjugaison, has real modular dimension 1, and gains one real dimension on adding P, for total dimension 2; it refers to the square-pyramidal case 2°.', 'central paragraph', 'transcribed, not mathematically checked')
note('S036-C05', 'claim', 'The lower chart places the dimensions 2,1,0 over its three graphs and gives component counts 1,10,15 beneath them.', 'lower chart', 'transcribed, not mathematically checked')
note('S036-C06', 'claim', 'The first chart column gives 12 realizations; the label specifying their kind remains uncertain.', 'first chart column', 'transcribed, not mathematically checked')
for sid, formula, place in [
    ('S036-C07', '10×3×2=60', 'middle first computation'),
    ('S036-C08', '10×2×6=120', 'middle second computation'),
    ('S036-C09', '15×2×2=60', 'right computation'),
    ('S036-C10', '5×3×2=30', 'first NB line'),
    ('S036-C11', '10×2=20', 'second NB line'),
]:
    note(sid, 'claim', 'The manuscript writes ' + formula + '.', place, 'arithmetic checked')
note('S036-N01', 'sheet', 'The face is manuscript on perforated tractor-feed paper. No coherent front-side typescript or reversed printed text was found to transcribe; sheet_kind is text.', 'whole sheet')
note('S036-N02', 'deletion scope', 'Only muni d’ is crossed out. There is one live un to its right; C’s additional cancelled un is unsupported by the visible ink.', 'central paragraph')
note('S036-N03', 'unresolved earlier state', 'The last factor 2 in 5×3×2 is heavily retraced. The current 2 is clear, but an earlier numeral is not recoverable; none has been invented in the text.', 'first NB line')
note('S036-N04', 'drawing', 'The third graph retains an upright free edge and a separately cancelled oblique branch. Its small baseline gap is preserved. The long arrows lead from the NB lines to the second and third graphs.', 'lower chart')
note('S036-N05', 'drawing', 'The bottom outer loop has its head at the upper end. The central loop-shaped glyph remains doubtful and is not assigned a topological meaning.', 'bottom sketch')
note('S036-N06', 'source state', 'The small curve after the first 60 is preserved without supplying a closing parenthesis. The lower two captions remain difficult beneath retouching and cancellation.', 'middle chart column')
note('S036-N07', 'pagination', 'The top 3 is retained as author pagination. The separate, lighter bottom-left 35 is retained as foliation in another unnamed hand.', 'top centre and bottom left')
note('S036-N08', 'date', 'No written date appears on this sheet. No date has been inferred from the paper or arithmetic.', 'whole sheet')
note('S036-N09', 'witness metadata', 'H’s editorial page note and prose drawing synopses are not manuscript prose. The actual drawings are reproduced in TikZ.', 'whole sheet')
note('S036-N10', 'reading workflow', 'Two additional dedicated crops cover the rising first paragraph line and the modulaire line. Earlier adjoining crops contained only contextual fragments of those lines; no decided place was recropped.', 'central paragraph')

checks = []
for sid, lhs, rhs, expression in [
    ('S036-C07', 10*3*2, 60, '10×3×2'),
    ('S036-C08', 10*2*6, 120, '10×2×6'),
    ('S036-C09', 15*2*2, 60, '15×2×2'),
    ('S036-C10', 5*3*2, 30, '5×3×2'),
    ('S036-C11', 10*2, 20, '10×2'),
]:
    checks.append(dict(statement_id=sid, date='2026-11-20',
                       who='reader A; GPT-6 Astra Pro; run SP82_C13_148; effort not exposed',
                       type='computation or formal certificate',
                       outcome=f'Correct as written: {expression} evaluates to {lhs}, equal to the written {rhs}.'))

hand_log = [
    dict(pages=[36], habit='Raised t in the point abbreviation',
         holds_at_every_observed_occurrence=True,
         witness_effect='C and H flatten both p-with-raised-t occurrences to pt.',
         evidence='The cancelled choice of 0 and the later choice of an extra real point each have a descending p with the t raised to its upper right. The separate pts occurrence has not been forced into this form.'),
    dict(pages=[36], habit='Sigma with a loop and long horizontal arm',
         holds_at_every_observed_occurrence=False,
         witness_effect='C misreads the cancelled margin equation as nu=3; H reads sigma followed by 0 as one infinity sign in the cancelled construction.',
         evidence='The secure sigma forms in K-superscripts, the margin equations and the cancelled equation 0=sigma0 have a looped left body and projecting arm. The dense cancelled sign before involutif and the bottom drawing glyph remain uncertain.'),
    dict(pages=[36], habit='U contrasted locally with M',
         holds_at_every_observed_occurrence=True,
         witness_effect='C doubts U/M; H gives M in the symmetric-square argument.',
         evidence='The single observed U turns around a rounded lower bowl; the nearby M has two upper peaks. This observation is restricted to those visible forms on this sheet.'),
    dict(pages=[36], habit='Abbreviations with a detached raised letter',
         holds_at_every_observed_occurrence=True,
         witness_effect='C reads ainsi and H expands to essent. where the source writes ess. with a raised t.',
         evidence='The one short form after on trouve has a low dot and a separated raised t. It remains abbreviated in the text.'),
    dict(pages=[36], habit='Different initial case in card/Card',
         holds_at_every_observed_occurrence=True,
         witness_effect='Both witnesses use lower-case card for case c.',
         evidence='Case b starts the operator with a small c; case c uses a tall open C. Each occurrence is preserved locally.'),
]
notation = [
    dict(form=r'M_{0,5}^{!}\simeq\mathrm{Sym}_2^*(U_{0,3})', pages=[36],
         observed_use='The real-point formula in case a has an exclamation exponent, a star on Sym and a U argument.',
         caution='The star and exclamation are separate marks; neither is a prime.'),
    dict(form=r'K^\sigma,\quad K\setminus K^\sigma=I', pages=[36],
         observed_use='The three cases are expressed with K-superscript-sigma; the interlinear formula names the complement I.',
         caution='The sigma loop must not be merged with the next 0 in the cancelled equation.'),
    dict(form=r'(\Sigma,I)', pages=[36],
         observed_use='The pair at the start of the four-point-system paragraph uses a zigzag capital Sigma and a barred capital I.',
         caution='No new alphabet is inferred from the uncertain lower drawing glyph.'),
    dict(form='35', pages=[36],
         observed_use='Bottom-left handwritten foliation, distinct from top author page 3.',
         caution='Hand remains unnamed; use margin, not author-pagination attribution.'),
]
abbreviations = [
    dict(form=r'ess.\textsuperscript{t}', expansion='essentiellement (probable)', place='case a, after on trouve', confidence='medium'),
    dict(form='dim / dim.', expansion='dimension', place='cases a and b, three occurrences in c, and chart heading', confidence='high'),
    dict(form='mod', expansion='modulaire', place='second line of lower chart heading', confidence='high'),
    dict(form='syst.', expansion='système', place='four-point-system paragraph', confidence='high'),
    dict(form=r'p\textsuperscript{t}', expansion='point', place='cancelled choice of 0; choice of extra real P', confidence='high'),
    dict(form='pts', expansion='points', place='4 pts', confidence='high'),
    dict(form='nb / Nb', expansion='nombre', place='chart row labels and NB text', confidence='high'),
    dict(form='OPS / OP', expansion='not established by an explicit expansion on this sheet', place='oblique margin / end of cancelled construction', confidence='low'),
]

second_boxes = []
def blind(id_, kind, box, reading):
    second_boxes.append(dict(box=id_, kind=kind, x0=box[0], y0=box[1],
                             x1=box[2], y1=box[3], reading=reading))
blind('S36-01', 'handwritten number', plan['page3']['box'], r'\mspage{3}')
blind('S36-02', 'C/H different word', plan['a_text']['box'],
      r'a) \(K^\sigma=K\) --- on trouve ess.\textsuperscript{t} les points réels')
blind('S36-03', 'whole doubtful formula and handwritten numbers', plan['a_formula']['box'],
      r'\(M_{0,5}^{!}\simeq\mathrm{Sym}_2^*(U_{0,3})\)')
blind('S36-04', 'struck passage, C/H different word and handwritten numbers', plan['a_second']['box'],
      r'\deleted{\unsure{Le cas|un cas}} de dim réelle \(2\) : contient le cas \(1^\circ\) (pentagonal)')
blind('S36-05', 'C/H different word and handwritten numbers', plan['b_start']['box'],
      r'b) \(\operatorname{card}K^\sigma=3\). En prenant pour repère \(0,1,\infty\) dans \(K^\sigma\), on trouve')
blind('S36-06', 'C/H different word and handwritten numbers', plan['b_formula']['box'],
      r'que \(K=\{0,1,\infty,\lambda,\bar\lambda\},\ \lambda\in\text{demi-plan de Poincaré},\ \text{dim réelle }2\). Contient le cas \(3^\circ\) (bitétraédral)')
blind('S36-07', 'margin note and struck passage', plan['margin']['box'],
      r'\margin{OPS \(\sigma z=\bar z\) \deleted{\unsure{pour} \(\sigma z=\bar z\)}}')
blind('S36-08', 'struck passage and handwritten number', plan['c_start']['box'],
      r'c) \(\operatorname{Card}K^\sigma=1\), i.e. \deleted{\unsure{?}} \(K^\sigma=\{P\}\),')
blind('S36-09', 'insertion and struck passage', plan['c_insert_delete']['box'],
      r'\inserted{\unsure{Soit} \(K\setminus K^\sigma=I\),} \deleted{on prend \unsure{comme repère} \(\infty\),}')
blind('S36-10', 'struck passage, whole formula and handwritten numbers', plan['c_delete2']['box'],
      r'\deleted{et on choisit un p\textsuperscript{t} \(0\) tel que \(0=\sigma0\). OP}')
blind('S36-11', 'C/H different word and handwritten number', plan['c_firstline']['box'],
      r'\((\Sigma,I)\) est un syst. de \(4\) pts sur une sphère complexe,')
blind('S36-12', 'insertion, struck passages and C/H different words', plan['c_main1']['box'],
      r'\deleted{muni d’} \inserted{\unsure{admettant}} un antiautomorphisme \deleted{\(\unsure{\sigma}\)} involutif (' + chr(96)*2 + r"conjugaison''), ils sont bien connus et de dim")
blind('S36-13', 'handwritten number and abbreviation', plan['c_modulaire_line']['box'],
      r'modulaire \uline{réelle} \(1\), de plus le choix d’un p\textsuperscript{t}')
blind('S36-14', 'C/H different words and handwritten numbers', plan['c_main2']['box'],
      r'réel supplémentaire \(P\) fait une dim. de plus, soit dim réelle totale \(2\) encore. (Contient le cas pyramidal carré, \(2^\circ\))')
blind('S36-15', 'drawing', plan['sphere']['box'], sphere)
graph_prefix = chart.split(r'\node[anchor=west] at (27,1816)')[0]
blind('S36-16', 'drawings, C/H different heading and handwritten numbers',
      [20,1502,1040,1790], graph_prefix + r'\end{tikzpicture}')
blind('S36-17', 'cancelled graphical branch', [760,1645,846,1770],
      r'\begin{tikzpicture}[x=.009cm,y=-.009cm]\draw(780,1750)--(779,1669);\draw(783,1750)--(827,1676);\draw(825,1679)--(808,1692)--(821,1689)--(795,1714)--(812,1707)--(800,1723)--(796,1733)--(803,1733);\fill(780,1750)circle(2pt);\end{tikzpicture}')
blind('S36-18', 'handwritten numbers', [135,1820,797,1900], r'\(1\qquad10\qquad15\)')
blind('S36-19', 'C/H different word, struck passage and handwritten number', [20,1910,335,2132],
      r'\(12\)\quad nb réalisations \unsure{modulaires|spéciales} \deleted{\unsure{polyédriques}}')
blind('S36-20', 'whole doubtful formula and handwritten numbers', [345,1928,673,2145],
      r'\begin{tikzpicture}[x=.009cm,y=-.009cm]\draw(361,1943)..controls(357,2015)and(368,2082)..(360,2141);\node[anchor=west]at(397,1971){$10\times3\times2$};\node[anchor=west]at(420,2020){$=60\ \unsure{(|c}$};\node[anchor=west]at(380,2110){$+10\times2\times6=120$};\end{tikzpicture}')
blind('S36-21', 'handwritten numbers', [675,1908,992,1988], r'\(15\times2\times2=60\)')
blind('S36-22', 'struck passage and departure from C below high confidence', [430,2140,724,2196],
      r'\deleted{\unsure{tétraèdre-pyr|tétraèdre-pyramide}}')
blind('S36-23', 'replacement caption and C/H different word', [428,2174,872,2250],
      r'(\unsure{tétraèdre|pentagonales}-pointées)')
blind('S36-24', 'struck passage', [75,2165,245,2255], r'\deleted{\unsure{les types}}')
blind('S36-25', 'C/H different words and handwritten numbers', [140,2275,1235,2438],
      r'\uline{NB} Nb de structures pyramidales: \(5\times3\times2=30\)\\bitétraédrales: \(10\times2=20\)')
blind('S36-26', 'handwritten overwritten number', [1024,2285,1106,2358], r'\(2\)')
arrow_change = next(x for x in changes if x['place'] == 'lower chart: endpoints of the two long curved arrows')
blind('S36-27', 'graphical arrows', [525,1695,1290,2430], arrow_change['final'])
blind('S36-28', 'drawing and whole doubtful label', plan['bottom_drawing']['box'], bottom)
blind('S36-29', 'handwritten number and margin note', plan['folio35']['box'], r'\margin{35}')

reading_rows = {
    633:('a: short word after on trouve','The source short form is ess. with raised t, rather than C ainsi or H expanded essent.'),
    639:('a: whole symmetric-square formula','U is resolved from the whole formula crop.'),
    641:('a: cancelled opening fragment','The fragment remains doubtful; the cancellation ends before live de, unlike H.'),
    642:('a: dimension abbreviation','Keep dim rather than H expansion.'),
    650:('b: pour before repère','Live pour is visible; H treats this place as cancelled unread text.'),
    655:('b: que at start of formula line','Que is present before K.'),
    656:('b: dimension abbreviation','Keep dim; the display-boundary difference is macro-only.'),
    660:('left oblique margin','OPS is present before the live equation.'),
    661:('left oblique margin: cancelled lower line','The lower equation repeats sigma z = bar z, with a cancelled doubtful initial pour.'),
    662:('left oblique margin: cancelled lower line','The terminal form is barred z, not C numeral 3.'),
    666:('c: tiny cancelled fragment','Retain the dense uncertain cancelled mark omitted by H.'),
    668:('c: interlinear insertion','The formula and doubtful Soit stand above the cancellation; they are live inserted text.'),
    669:('c: first cancelled line','The tentatively read cancelled wording is retained; H leaves it unread.'),
    673:('c: cancelled equation defining 0','Read sigma followed by a separate 0, not infinity.'),
    678:('c: preposition before une sphère','Sur, not H dans.'),
    679:('c: replacement and cancellation scope','Only muni d’ is struck; admettant remains doubtful; one live un and singular antiautomorphisme follow.'),
    680:('c: sign, involutif and quotation','Keep the doubtful cancelled sigma; involutif is readable and conjugaison is singular with paired quotation marks.'),
    681:('c: first dimension abbreviation','Keep dim rather than expansion.'),
    687:('c: dotted dimension abbreviation','Keep the written dim.'),
    688:('c: last dimension abbreviation','Keep the written dim.'),
    694:('sphere drawing and chart heading','The long diff includes real drawing details and H expansion of dim mod; other TikZ/box syntax is macro-only.'),
    695:('lower chart graphs','Retain the separate cancelled sloping branch and the real baseline gap. H describes a tick across the upright.'),
    697:('lower chart live label','Modulaires is favoured but the C alternatives remain unresolved against H spéciales.'),
    698:('lower chart cancelled label','Keep the doubtful crossed polyédriques.'),
    700:('lower chart curve after 60','The isolated curve is retained; the apparent displacement of the right-column equation is alignment, not changed arithmetic.'),
    701:('lower chart captions','The cancelled caption and replacement word remain uncertain; -pointées is retained.'),
    703:('lower chart captions','The numerical 60/120 opposition is an alignment artefact; H’s adjacent annotation contains genuine different word readings.'),
    704:('lower left cancelled words and NB opening','Retain doubtful les types and readable Nb de structures.'),
    705:('lower chart outer arrow and NB punctuation','The arrow runs from the first NB count toward the third graph; the source has no semicolon after 30.'),
    706:('lower chart inner arrow and retraced factor 2','The inner arrow reaches the second graph. The present 2 is clear; an earlier digit is not supplied.'),
    707:('bottom sketch','TikZ replaces H editorial synopsis, preserving the observed contour and arrow directions.'),
    708:('bottom sketch and foliation','The central glyph stays doubtful sigma; the outer-loop direction is corrected and foliation 35 is retained.'),
}
macro_notes = {
    629:'Archive scan marker versus H editorial page marker.',
    630:'H editorial description of author pagination; source 3 is retained.',
    635:'Superscript/subscript ordering only; the exclamation mark is present in both readings.',
    636:'Superscript/subscript ordering only.',
    637:'Star placement syntax only.',
    638:'Star placement syntax only.',
    640:'Closing math delimiter and H editorial uncertainty note; the note is not source prose.',
    648:'Operator-spacing command in H, not a written comma.',
    664:'Operator-spacing command in H, not a written comma. The independently observed capital C is logged separately.',
    674:'H editorial account of two struck lines; the actual insertion state is adjudicated at rows668–669.',
    684:'Straight versus typographical apostrophe only.',
    691:'Case numeral shifted by the alignment into H editorial drawing synopsis.',
    692:'Case numeral/delimiter alignment against H editorial drawing prose.',
    693:'TikZ boundary versus H editorial drawing synopsis; graphical changes are logged separately.',
    702:'The 2 and 6 belong to distinct aligned equations, both visible and retained; no factor is changed.',
}
differences_review=[]
for row in csv.DictReader((PACKET/'differences.tsv').open(), delimiter='\t'):
    sr=int(row['source_row'])
    if sr in reading_rows:
        place, explanation=reading_rows[sr]
        differences_review.append(dict(source_row=sr,decision='reading decision',place=place,note=explanation))
    else:
        differences_review.append(dict(source_row=sr,decision='macro-only',place='source alignment or macro syntax',
                                       note=macro_notes.get(sr,'Math delimiters, degree notation, grouping or display wrappers only; no different manuscript reading is introduced.')))

result=dict(
    scan=36, reader='A', lines_read=34,
    reader_metadata=dict(model='GPT-6 Astra Pro', reasoning_effort='not exposed', run='SP82_C13_148'),
    reading_workflow=dict(
        whole_page_views=1, successful_half_views=[1,1],
        image_proxies='Same-dimension quality95 JPEG proxies of the whole and native overlapping halves; no resizing.',
        line_count_detail='20 prose, marginal and interlinear baselines, including the separate pentagonal parenthesis; 12 lower chart/caption baselines; 2 pagination baselines. Drawing paths and the central drawing glyph were read separately.',
        crops_saved=len(plan), crops_visually_read=len(plan),
        chart_proxy='The original saved chart PNG was too large for the image output; its same-dimension quality95 JPEG proxy was actually viewed. Evidence rectangles refer to the original saved PNG.',
        failed_image_outputs='A half2 image output and the chart PNG output did not display; each was successfully viewed afterward through the stated same-dimension proxy. No failed display is counted as a visual reading.',
        boundaries='Only scan036 source packet, current notation snapshot and its own saved images/crops were read. No OCR, web research or TeX compilation.',
        root_review='Root independently viewed the whole, halves and all18 crops. The ess. raised t, raised-t point abbreviations and muni d’ cancellation boundary incorporate that corroboration.'
    ),
    changes=changes, decisions=decisions, inventory=inventory, unresolved=unresolved,
    notes=notes, checks=checks, hand_log=hand_log, notation=notation, abbreviations=abbreviations,
    second_boxes=second_boxes, differences_review=differences_review
)
expected_marks={r['id'] for r in csv.DictReader((PACKET/'marks.tsv').open(),delimiter='\t')}
assert {d['id'] for d in decisions}==expected_marks
assert len(decisions)==len(expected_marks)
assert len(differences_review)==80
assert {d['source_row'] for d in differences_review}==set(range(629,709))
assert len({b['box'] for b in second_boxes})==len(second_boxes)
assert all(x['type']=='computation or formal certificate' for x in checks)
assert all(isinstance(x['box'],list) and x['box']==next(p['box'] for p in plan.values() if p['crop']==x['crop']) for x in changes)
(BASE/'result.json').write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'decisions':len(decisions),'inventory':len(inventory),
                  'unresolved':len(unresolved),'notes':len(notes),'checks':len(checks),
                  'second_boxes':len(second_boxes),'differences_review':len(differences_review)}))
