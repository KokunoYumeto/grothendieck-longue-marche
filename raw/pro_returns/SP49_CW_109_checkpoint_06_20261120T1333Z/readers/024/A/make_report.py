from pathlib import Path
import json, re, difflib

root = Path('/workspace/scratch/6d55c8c3e5a7')
out = root / 'work/readers/024/A'
inputs = root / 'work/inputs/024'
meta = json.loads((inputs / 'metadata.json').read_text())
reading = (out / 'reading.tex').read_text()
c_text = (inputs / 'C.tex').read_text()
specs = {r['id']: r for r in json.loads((out / 'unresolved_after_halves.json').read_text())['loci']}

def ev(crop=None, half=None, bbox=None):
    if crop:
        r = specs[crop]
        return dict(crop=str((root / r['crop']).resolve()), source=r['source'], bbox=r['bbox'])
    return dict(crop=None, source=meta[half or 'whole'], bbox=bbox)

changes = []
def ch(ident, place, c, new, kind, confidence, evidence, crop=None, half=None, bbox=None):
    changes.append(dict(id=ident, place=place, c=c, h=None, reading=new, diff_c=True,
                        diff_h=False, kind=kind, marked_in_H=False, confidence=confidence,
                        evidence=evidence, **ev(crop, half, bbox)))

ch('left-rule', 'Long rule between the page-reference column and the correction text', '',
   r'\draw[line width=0.35pt] (166,26)--(166,1210)--(164,2274);',
   'drawing or diagram', 'high',
   'A continuous narrow vertical rule runs down the page at approximately x166, slightly leftward at its foot. It is reproduced with the second rule in the opening TikZ panel.',
   half='whole', bbox=[157,24,175,2281])
ch('right-rule', 'Long rule near the right edge of the correction text', '',
   r'\draw[line width=0.35pt] (1448,25)--(1444,1160)--(1443,2275);',
   'drawing or diagram', 'high',
   'A second continuous thin rule lies near x1446. It is not a bracket attached to a single entry and is reproduced as a long rule.',
   half='whole', bbox=[1435,23,1455,2282])
ch('mark-after-nine', 'p191 l.-9, between the reference and the Riemannian quotation', '',
   r'\raisebox{0.7ex}{\begin{tikzpicture}[x=0.1ex,y=0.1ex]\draw[line width=0.3pt] (0,0)--(3,2);\end{tikzpicture}}',
   'drawing or diagram', 'medium',
   'The crop shows a separate short oblique dark mark to the right of 9, above the baseline. Its geometry is retained without assigning it a punctuation function.', crop='02')
ch('cancelled-for', '193 l5, cancelled group before replace', r'\deleted{\unsure{``for}}',
   r'\deleted{``for}', 'misread word', 'medium',
   'The tall loop and descending loop give f, followed by a small oval and an r shoulder. The raised opening pair and the word have crossing strokes; no closing pair is supplied.', crop='03')
ch('left-note-placement', 'Left edge beside 194', r'\margin{\deleted{\unsure{stating|starting}}}',
   r'\reversemarginpar\margin{\deleted{\unsure{stating|starting}}}\normalmarginpar',
   'insertion or placement', 'high',
   'The cancelled word lies physically left of the page-reference 194 and is clipped at the sheet edge. The default right margin placement is therefore changed; its word doubt is retained.', crop='04')
ch('page-number-order', 'Faint reference for ls 7 & 8 and l18', r'p\unsure{196|191}',
   r'p\unsure{191|196}', 'misread symbol or index', 'medium',
   'The final visible stroke is a narrow near-vertical with no secure bowl. This favours 1 on ink alone; a pale missing part of 6 is not excluded. The neighbouring p197 addition is not used to force 196.', crop='05')
ch('apperent', 'p191/196 l18', r'\unsure{apperent|apparent}', 'apperent',
   'misread word', 'high',
   'After the two long p descenders, the next letter is a small e-shaped loop; another e follows r. There is no closed a with a distinct right stem at the disputed first vowel.', crop='06')
ch('point-after-is', '205 l-7, explanatory parenthesis', r'is\unsure{.} a', 'is. a',
   'misread symbol or index', 'high',
   'A separate dark low point stands between is and a. Its existence and position are clear. A literal dot is retained without assigning a sentence-ending intention.', crop='09')
ch('206-cancelled-remnant', '206 after l.20', r'\deleted{\unsure{?}}', r'\deleted{\unsure{?|7}}',
   'misread symbol or index', 'low',
   'The crossed remnant has a curved/angled upper part and a short downstroke. A 7-like numeral is also compatible with the surviving strokes, while no separate question-mark dot can be isolated.', crop='10')
ch('207-isolated-point', 'Right of the p207 continuation ending is more usual.', '',
   r'\hfill\raisebox{1.4ex}{\begin{tikzpicture}[x=0.1ex,y=0.1ex]\fill (0,0) ellipse (1.7 and 1);\end{tikzpicture}}',
   'drawing or diagram', 'high',
   'The lower half has a distinct slanted dark point at x1302, y249, well to the right of the sentence and above its baseline. It is reproduced independently, without making it a second sentence stop.',
   half='half_b', bbox=[1284,236,1320,263])
ch('209-seven', '209 reference before such a subdivision', r'l.\unsure{-}7', 'l.7',
   'misread symbol or index', 'high',
   'The high left hook is continuously joined to the top bar of the crossed 7. There is no separate minus between the period and the numeral.', crop='13')
ch('210-raised-mark', '210 l.17, between here and I suggest', r'\unsure{``}', r'\unsure{``|*}',
   'misread symbol or index', 'low',
   'The raised cluster contains a small white opening and several pointed extremities. Fused quotation strokes remain possible, but the star-like outline is also compatible with the ink. No cancellation state is imposed.', crop='14')
ch('210-right-marks', 'Right margin, level of the first 210 line', '',
   r'\margin{\begin{tikzpicture}[x=0.1ex,y=0.1ex]\draw[line width=0.5pt] (0,6)--(3,4);\draw[line width=1pt] (8,1)--(11,-3);\end{tikzpicture}}',
   'drawing or diagram', 'high',
   'Two isolated dark marks lie beyond the right rule, the second lower and broader. Their relative diagonal placement is reproduced without construing them as quotes or punctuation.', crop='15')
ch('216-cancellation-edges', 'p216 first, cancelled entry',
   r'\deleted{line -10 ``that if the?\'\' (the repeated line -9)}'.replace("\\'", "'"),
   r'\deleted{line -10} ``\deleted{that if the}\unsure{?\'|\'\'} \deleted{(the repeated line -9)}'.replace("\\'", "'"),
   'deletion state (struck given live or live given struck)', 'medium',
   'The wavy cancellation crosses line -10, the words that if the, and the parenthesis. The opening pair is raised clear of it. The closing raised group is also clear of the wave; its first curved element and following tick do not securely distinguish question mark plus one quote from two quotes. There is no secure third separate raised mark.', crop='16')
ch('cf-point', '224 line 2, c.f abbreviation', 'c.f p.32', 'c.f. p.32',
   'omission', 'medium',
   'A separate low point is visible just below/right of the f, before p.32. It is retained as the final period of c.f.; the point is not part of the long f stem.', crop='20')
ch('first-j', '224 first formula, functor name before the colon', r'\unsure{j|J}_A', r'j_A',
   'misread symbol or index', 'medium',
   'The upper entry of the hooked letter lies lower than the capital C in Cat, while its long lower hook descends below that baseline. The glyph is read as lowercase j; its lowered A is separate.', crop='20')
ch('stroke-under-arrow', '224 first formula, under the Cat-to-hat-A arrow', r'\longrightarrow',
   r'\mathrel{\underset{\text{\hspace{-1.1em}\begin{tikzpicture}[x=0.1ex,y=0.1ex]\draw[line width=0.35pt] (1,0)--(0,-5);\end{tikzpicture}}}{\longrightarrow}}',
   'drawing or diagram', 'high',
   'A short, nearly vertical isolated stroke stands below the left part of the arrow shaft. It is distinct from both the arrow and the lower interlinear question and is drawn without assigning it a label value.', crop='20')
ch('live-X', '224 second formula, argument of j_A', r'\deleted{B}\unsure{X|B}', r'\deleted{B}X',
   'misread symbol or index', 'high',
   'The old B has two right-facing bowls. Two independent crossing diagonals form the live X across them; both diagonal tips extend beyond the old bowls.', crop='21')
ch('224-low-point', 'Low left of the question beginning so', '',
   r'\raisebox{-0.7ex}{\begin{tikzpicture}[x=0.1ex,y=0.1ex]\fill (0,0) ellipse (1 and 2);\end{tikzpicture}}\quad',
   'drawing or diagram', 'high',
   'A single isolated upright dark point lies below and left of so, distinct from the pair opening commutes on the line below. It is reproduced once and is not assigned to either quoted phrase.', crop='23')
ch('final-colon', 'Final entry, after twice', 'l.20.twice.', 'l.20.twice:',
   'misread symbol or index', 'high',
   'The terminal mark after twice has two vertically separated dark dots. The separate period between 20 and twice is also visible and retained.', crop='24')

c_doubts=[]
def doubt(place,c,new,resolved,confidence,evidence,crop=None,half=None,bbox=None):
    c_doubts.append(dict(place=place,c=c,reading=new,resolved=resolved,confidence=confidence,
                         evidence=evidence,**ev(crop,half,bbox)))

doubt('p191, opening page reference', r'\unsure{191}', r'\unsure{191}', False, 'low',
      'The middle downstroke and fragments of a curved head fit 9 and the two outside strokes fit 1, but fading prevents certainty in the whole numeral.', crop='01')
doubt('193 l5, cancelled opener and word', r'\unsure{``for}', '``for', True, 'medium',
      'The f loop and descender, small o loop, and r shoulder remain legible beneath the cancellation; the double opener is itself crossed.', crop='03')
doubt('194, cancelled left-margin word', r'\unsure{stating|starting}', r'\unsure{stating|starting}', False, 'low',
      'The edge truncates the beginning. Surviving tall t-like strokes and the -ing ending do not determine whether a medial r was present. Cancellation extent and left-side placement are clear.', crop='04')
doubt('Faint page reference above 198', r'\unsure{196|191}', r'\unsure{191|196}', False, 'low',
      'The last surviving stroke is near-vertical without a visible bowl; 191 is therefore preferred on ink. A faded lower curve could still have belonged to 6.', crop='05')
doubt('p191/196 l18, apperent/apparent', r'\unsure{apperent|apparent}', 'apperent', True, 'high',
      'Both medial vowels have small e-shaped loops. The ordinary English spelling is not substituted.', crop='06')
doubt('205 l-7, dot after is', r'\unsure{.}', '.', True, 'high',
      'The separate low dark point is geometrically definite. Its rhetorical purpose remains unassigned.', crop='09')
doubt('206 after l.20, crossed remnant', r'\unsure{?}', r'\unsure{?|7}', False, 'low',
      'A bent upper mark and short stem survive under crossing ink; either a question-like mark or 7-like numeral can be fitted without supplying invisible strokes.', crop='10')
doubt('209 l.7, possible minus', r'\unsure{-}', '', True, 'high',
      'The left high stroke is part of the top of the crossed numeral 7, not an independent minus.', crop='13')
doubt('210 l.17, raised mark before I', r'\unsure{``}', r'\unsure{``|*}', False, 'low',
      'The small raised cluster can be fused quote strokes or a star-like mark. The crop does not securely establish a separate cancellation stroke.', crop='14')
doubt('p219 l.6, earlier glyph under t', r'\unsure{t}', r'\unsure{t}', False, 'low',
      'The thickened vertical and extra small lower loop are visible, but no full earlier letter can be separated from the final t. C\'s tentative t remains tentative.', crop='18')
doubt('224 page reference, overwritten first digit', r'\unsure{1|2}', r'\unsure{1|2}', False, 'low',
      'A narrow older vertical and small hook are visible within the leading 2, but too much of the older outline is buried to choose 1 or 2.', crop='19')
doubt('224 first functor name', r'\unsure{j|J}_A', r'j_A', True, 'medium',
      'The top of the hooked letter is lower than the capital C and the hook descends below the baseline, supporting lowercase j independently of the expected notation.', crop='20')
doubt('224 argument of the second j_A', r'\deleted{B}\unsure{X|B}', r'\deleted{B}X', True, 'high',
      'The live diagonals are individually traceable over the old upper and lower B bowls.', crop='21')
doubt('224 Hom argument, old glyph beneath X', r'\deleted{\unsure{B}}X', r'\deleted{\unsure{B}}X', False, 'low',
      'Live X is visible, but the preceding/underlying upright and partial dark crossbar coincide with the rule and do not identify the older letter securely. The old B in the other argument is not used as proof.', crop='22')
doubt('224 lower question, crossed baseline word', r'\deleted{\unsure{is}}', r'\deleted{\unsure{is}}', False, 'low',
      'Two small joined baseline forms survive under crossing diagonals. They are compatible with is, but the cancellation prevents a secure reading.', crop='23')
doubt('224 lower inserted mapping, numerator', r'\unsure{B|A}/x', r'\unsure{B|A}/x', False, 'low',
      'The numerator overlaps the A above. A left upright and partial bow favour B, but the overlapping upper A prevents excluding A. The separate lower x and slash are clear.', crop='23')

# Decisions on the page-specific context entries, beyond literal uncertainty macros.
doubt('224 context: second and lower functor names', r'j_A', r'j_A', True, 'medium',
      'The second j independently has a low start and a long descender, with a lowered A. The lower question likewise has j and a separate lowered B; neither is given script or blackboard styling.', crop='21')
doubt('224 context: category name and hat', r'\mathrm{Cat}\longrightarrow\widehat A', reading[reading.index(r'\mathrm{Cat}'):reading.index(r'\widehat A')+len(r'\widehat A')], True, 'high',
      'Ordinary C, a, t, a right-pointing arrow and a separate two-sided roof over the ordinary A are visible. The extra stroke beneath the arrow is reported independently.', crop='20')
doubt('224 context: Hom and slice slash', r'\operatorname{Hom}(A/a,\deleted{\unsure{B}}X)', r'\operatorname{Hom}(A/a,\deleted{\unsure{B}}X)', True, 'high',
      'Hom has an ordinary two-stem H; A/a uses an oblique slash and a baseline/lowered a, followed by a comma. This context decision confirms those signs only; the old argument remains a separate doubt.', crop='22')
doubt('224 context: lower arrow and denominator', r'\colon x\to\unsure{B|A}/x', r'\colon x\to\unsure{B|A}/x', False, 'medium',
      'The colon, first x, right-facing short arrow, slash and final x are clear; only the numerator remains unresolved. No mapsto bar is supplied.', crop='23')
doubt('p191/196 and p197 context: interlineation and spelling alternative', r'\unsure{apperent|apparent} \inserted{p197}, l-9', r'apperent \inserted{p197}, l-9', True, 'high',
      'The p197 is raised directly over a large caret between the spelling word and l-9. A separate low comma is retained. The interlineation does not settle the faded earlier page number.', crop='06')
doubt('192 l.-19 context: recense and proposed check-on', "``recense''", "``recense''", True, 'high',
      'Both the source word recense and the proposed check-on are plainly written with double quotes. The writer calls the latter the easiest short replacement; no expansion or correction is made.',
      half='half_a', bbox=[194,249,1454,431])
doubt('193 l5 context: tentative proposed wording', "``turned short'' by possibly ``fizzled out''?", "``turned short'' by possibly ``fizzled out''?", True, 'high',
      'The qualification possibly and the final question mark are live. They are not part of the cancellation before replace.',
      half='half_a', bbox=[526,426,1446,508])
doubt('205 l-7 context: whether/wether', "``whether'' (``wether''", "``whether'' (``wether''", True, 'high',
      'The quoted correction has wh-, whereas the explanatory form lacks h after w and is followed by the castrated-ram gloss.',
      half='half_b', bbox=[694,28,1515,101])
doubt('207 l.15 context: first four-dot span', "``the one.... data''", "``the one.... data''", True, 'high',
      'Four distinct low marks follow one: three larger short marks and one much smaller point. Both quotation groups have two strokes.', crop='11')
doubt('207 l.15 context: second four-dot span', "``the one.... datum''", "``the one.... datum''", True, 'high',
      'Four low marks precede datum. The final connected quote group has two lower legs and is retained as double.', crop='12')
doubt('p216 context: cancelled wording and live replacement question',
      r'\deleted{line -10 ``that if the?\'\' (the repeated line -9)}'.replace("\\'", "'"),
      r'\deleted{line -10} ``\deleted{that if the}\unsure{?\'|\'\'} \deleted{(the repeated line -9)}'.replace("\\'", "'"), False, 'medium',
      'The old wording is cancelled but the raised quotation-edge groups are above the cancellation; the closing group remains ambiguous. The following do you mean question is a distinct live entry.', crop='16')
doubt('p216 live entry: dash after functor quote', "'that the functor'' - it", "'that the functor'' - it", True, 'high',
      'There is one dash; the higher thin stroke to its right is the i dot in it. The closing quotation group has two joined short strokes.', crop='17')
doubt('224 context: lower question and inserted wording',
      r"so \inserted{isn't} this \inserted{description} $j_B$ \deleted{\unsure{is}} \inserted{$\colon x\to\unsure{B|A}/x$} wrong",
      r"so \inserted{isn't} this \inserted{description} $j_B$ \deleted{\unsure{is}} \inserted{$\colon x\to\unsure{B|A}/x$} wrong",
      False, 'medium',
      'The caret after so places raised isn\'t there; a second caret before j_B places description there. The small mapping is interlinear after j_B over/after the cancelled word. The ending wrong has no additional visible question mark. Buried is and numerator B/A remain doubtful.', crop='23')

remaining = [
 dict(place='Opening page reference', reading=r'p.\unsure{191}', alternatives='191 (best tentative reading)', confidence='low', reason='The numeral is faded and only fragments of its strokes survive.'),
 dict(place='Left-margin cancelled word beside 194', reading=r'\deleted{\unsure{stating|starting}}', alternatives='stating | starting', confidence='low', reason='The beginning is clipped and the medial strokes are heavily cancelled.'),
 dict(place='Reference above 198', reading=r'p\unsure{191|196}', alternatives='191 | 196', confidence='low', reason='The final narrow stroke favours 1, but a faded lower bowl of 6 cannot be excluded.'),
 dict(place='206 after l.20', reading=r'\deleted{\unsure{?|7}}', alternatives='? | 7', confidence='low', reason='The upper remnant and short downstroke lie under crossing ink.'),
 dict(place='210 mark before I suggest', reading=r'\unsure{``|*}', alternatives='double opening quotation | asterisk-like mark', confidence='low', reason='The raised cluster has merged strokes and several pointed ends; cancellation is not established.'),
 dict(place='p216 cancelled entry, raised closing group', reading=r"\unsure{?'|''}", alternatives="question mark plus one quote | two quotes", confidence='low', reason='Only a curved first component and one separate raised tick can be isolated; both are above the principal cancellation.'),
 dict(place='p219 l.6 overwritten t', reading=r'\deleted{\unsure{t}}', alternatives='t (tentative old glyph)', confidence='low', reason='The extra low loop and thickened stem do not reveal a secure earlier letter.'),
 dict(place='224 initial page-number digit', reading=r'\deleted{\unsure{1|2}}', alternatives='1 | 2', confidence='low', reason='An older upright and hook remain embedded in the final 2.'),
 dict(place='224 Hom argument, old character', reading=r'\deleted{\unsure{B}}X', alternatives='B (tentative old glyph)', confidence='low', reason='The rule and the heavy live X obscure the earlier outline.'),
 dict(place='224 lower question, cancelled word', reading=r'\deleted{\unsure{is}}', alternatives='is (tentative old word)', confidence='low', reason='The two baseline forms are crossed and cannot be separated completely.'),
 dict(place='224 lower mapping numerator', reading=r'\unsure{B|A}/x', alternatives='B | A', confidence='low', reason='The small numerator coincides with the large A of the formula above.')
]

inventory=[]
def inv(element,kind,position,first,hand='one unnamed hand (running handwritten corrections)'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,
                          position=position,first_words_or_objects=first,transcribed='yes'))
inv('01','drawing','Full height, x approximately 166, between the reference column and the text','Thin left vertical rule','origin of ruled stroke undetermined')
inv('02','drawing','Full height, x approximately 1446, near the right edge','Thin right vertical rule','origin of ruled stroke undetermined')
inv('03','text','Top row','p.191 l7; didn\'t; informal; would be more correct.')
inv('04','text','Second row','l.-9 Riemannian; l-1 + -2 informal again.')
inv('04a','drawing','Raised immediately right of the second-row 9','Short isolated oblique mark')
inv('05','text','192 l.10 row','had turned out shorter than hoped, due to lack')
inv('06','text','192 l.-19, three physical lines','recense is not an English word; I suggest check-on')
inv('07','text','193 l5 row','replace turned short by possibly fizzled out?')
inv('07a','deletion','Within 193 l5, before replace','Double opening quotation and for, cancelled')
inv('08','margin note','Clipped left edge beside the 194 row','stating|starting')
inv('08a','deletion','Nested in the left marginal note beside 194','The whole marginal word is crossed')
inv('09','text','194 principal row','line -14 informal; l-13 informal; l-11 I\'ve got is better.')
inv('10','text','Short continuation under 194','l-8 literature')
inv('11','text','Faint p191/196 row, above 198','ls 7 & 8 insufficient; l18 apperent; p197 corrections')
inv('11a','insertion','Above a caret between apperent and l-9','p197')
inv('12','text','198 short row','l4 don\'t')
inv('13','text','200 l.11 row','its; no apostrophe; it\'s only used as an abbrev for it is')
inv('14','text','200 continuation row','l17 substitute; l19 in terms; l-14 substitute again')
inv('15','text','201 row','l.19 workable; l.-5 don\'t; l-3 isn\'t; l-2 isn\'t')
inv('16','text','202 row','l3 doesn\'t; l8 didn\'t; l13 couldn\'t; l17 wouldn\'t')
inv('17','text','203 short row','l-4 wasn\'t')
inv('18','text','204 short row','l3 isn\'t')
inv('19','text','205 row','l14 insufficient; l-7 whether; wether is. a castrated ram!')
inv('20','text','206 row','l.8 don\'t; l.20 seesaw')
inv('20a','deletion','After the 20 in the 206 reference','Crossed ?|7 remnant')
inv('21','text','207 l.15 row','the one.... data surely should be the one.... datum')
inv('22','text','207 continuation','l-9 allow one to check is more usual.')
inv('22a','drawing','Far right of the 207 continuation, above the text baseline','Single isolated dark point')
inv('23','text','208 row','l.8 a long time ago; l-9 & -10 couldn\'t be')
inv('23a','text','Within the 208 l.8 quoted phrase','a, doubly underlined')
inv('24','text','209 row','l.5 shouldn\'t; l.7 such a subdivision; l.-9 wouldn\'t')
inv('25','text','210 entry, two physical lines','Grammar\'s wrong here; I suggest replace and look to by and then to look to')
inv('25a','text','Raised between here and I in 210','Doubtful double quote or asterisk-like mark')
inv('25b','drawing','Right margin at the first 210 line, beyond the rule','Two isolated slanted dark marks')
inv('26','text','213 row','line 1. At long last')
inv('27','text','p216 first, cancelled entry','p216 followed by the cancelled older entry')
inv('27a','deletion','p216 first entry, left segment','line -10')
inv('27b','text','Raised over the p216 cancellation between -10 and that','Live opening double quotation strokes')
inv('27c','deletion','p216 first entry, central wording','that if the')
inv('27d','text','Raised over the p216 cancellation after the','Live doubtful closing group ?\'|\'\'')
inv('27e','deletion','p216 first entry, right parenthesis','(the repeated line -9)')
inv('28','text','p216 replacement, two physical lines','line -10 & -9: do you mean that the functor; it doesn\'t make sense at present.')
inv('29','text','p217 row','l.5 didn\'t')
inv('30','text','p.219 row','l.6 its; l.8 we\'ve got')
inv('30a','deletion','Within the p.219 l.6 word its','Doubtful old t under the live t')
inv('31','text','221 row','l11 analogy')
inv('32','text','224 last main reference','224 line 2 c.f. p.32')
inv('32a','deletion','Within the first digit of the 224 reference','Old 1|2')
inv('33','display','Same baseline as 224 line 2, across the lower page','j_A: Cat to hat A; j_A(X) = (a to Hom(A/a,X))')
inv('33a','drawing','Under the first formula arrow','Short nearly vertical isolated stroke')
inv('33b','deletion','First argument in the second formula','B under live X')
inv('33c','deletion','Final argument of Hom, at the right rule','Doubtful B under live X')
inv('34','text','Crowded line below the formula, left portion of the page','so isn\'t this description j_B ... wrong')
inv('34a','drawing','Low left of so, above the opening quotes of commutes','Single isolated dark point')
inv('34b','insertion','Above the caret between so and this','isn\'t')
inv('34c','insertion','Above the caret before j_B','description')
inv('34d','deletion','Baseline between j_B and wrong','Doubtful is')
inv('34e','insertion','Interlinear, above the baseline after j_B and over/after cancelled is','colon x to B|A / x')
inv('35','text','Final line','l.17 commutes with; also l.20.twice: l.21 if we have two')
inv('36','margin note','Lower left corner','Archive sheet number 23, comment only','another lighter, pencil-like hand')

notes=[
 'A handwritten correction list citing pages 191 through 224; the faded reference before the inserted p197 remains 191/196. The list has no title, date, stated page count, or authorial pagination; 23 in the lower corner is treated only as an archive number.',
 'At p191 l.18 the writer says informal would be more correct. At 192 l.-19, recense is called not an English word and check-on is suggested as the easiest short replacement.',
 'At 193 l5, the wording turned short is to be replaced possibly by fizzled out, with a final question mark. At 194 l-11 the writer says I\'ve got is better.',
 'The p200 note gives an apostrophe explanation for its/it\'s. At 205 l-7, the proposed whether is contrasted with wether and the latter is glossed as a castrated ram.',
 'At 207 l.15 the two four-dot quoted spans end respectively in data and datum, with surely should be between them. The following allow one to check is called more usual.',
 'At 210 l.17 the writer says the grammar is wrong and suggests replacing and look to by and then to look to; a separate l.4 note says its takes no apostrophe.',
 'At p216 an older entry is crossed out. The live replacement asks whether that the functor is intended and says the text does not make sense at present. The raised quote-edge groups of the cancelled entry lie outside its principal cancellation path.',
 'At 224 line 2 the writer refers to p.32, gives a j_A formula with two corrections from older B-shaped arguments to X, and asks whether the description of j_B by the small x-to-slice expression is wrong. The numerator and several buried words remain doubtful; the final word wrong has no supplied question mark.'
]

notation=[
 dict(sign=r'j_A; j_B',location='224 formula and lower question',reading=r'j_A; j_A; j_B',evidence='Each hooked letter starts lower than the adjacent ordinary capitals and descends; A and B are separate lowered indices. First/second names inspected in crops20/21; lower name in crop23.'),
 dict(sign=r'\mathrm{Cat}; \widehat A; \operatorname{Hom}',location='224 formula',reading=r'\mathrm{Cat}; \widehat A; \operatorname{Hom}',evidence='Single ordinary capital contours; a separate pointed roof above A; H has two upright strokes. Crops20 and22.'),
 dict(sign=r'A/a; x\to\unsure{B|A}/x',location='224 formula and lower inserted mapping',reading=r'A/a; x\to\unsure{B|A}/x',evidence='Slanted slash strokes and separate lower a/x glyphs; right-pointing arrowheads. The lower numerator overlaps the formula above and remains doubtful.'),
 dict(sign=r'\deleted{B}X',location='224 argument of the second j_A',reading=r'\deleted{B}X',evidence='Two old bowls remain under two distinct live crossing diagonals in crop21.'),
 dict(sign=r'\uuline{a}',location='208 l.8',reading=r'\uuline{a}',evidence='Two short underline strokes, joined at an oblique end, are confined to a in half_b.'),
 dict(sign='Four dots in each quoted span',location='207 l.15',reading="``the one.... data''; ``the one.... datum''",evidence='Separate crops11/12 show four low marks in each occurrence; the last mark in the first span is smaller.'),
 dict(sign='Quotation-edge state',location='p216 cancelled entry',reading=r"``\deleted{that if the}\unsure{?'|''}",evidence='Both high groups are above the wavy cancellation in crop16; the closing group has unresolved identity.'),
 dict(sign=':',location='Final line after twice',reading='twice:',evidence='Crop24 shows two vertically separated dark points.'),
 dict(sign='Low point after is',location='205 explanatory parenthesis',reading='is. a',evidence='Crop09 confirms a separate low point; its grammatical function is not inferred.'),
 dict(sign='l.7',location='209 reference',reading='l.7',evidence='Crop13 shows one continuously written top hook and crossbar of 7, with no independent minus.'),
 dict(sign='Mixed single/double quotation strokes',location='200 explanatory parenthesis; 202 first form; 208 first form',reading="'it's''; 'it is''; 'doesn't''; ``a long time ago'",evidence='Crops07/08 and the halves support the mixed quote counts; they are not normalized to matching pairs.')
]

abbreviations=[
 dict(form='p.',expansion='page (interpretation only)',place='Opening reference and p.219/p.32'),
 dict(form='p',expansion='page (interpretation only)',place='Faint reference above198 and p197/p216/p217'),
 dict(form='l; l.; ls',expansion='line; lines (interpretation only)',place='References throughout'),
 dict(form='abbrev',expansion='abbreviation (interpretation only)',place='200 apostrophe explanation'),
 dict(form='c.f.',expansion='compare / confer (tentative interpretation only)',place='224 line2, before p.32')
]

report=dict(
 scan=24,reader='A',model='GPT-6 Astra Pro (inherited)',effort='not exposed',
 viewed=[meta['whole'],meta['half_a'],meta['half_b']],
 layout='One handwritten correction list on an otherwise untyped sheet. Page references occupy a narrow left column separated by a long vertical rule; a second long rule lies near the right edge. One text hand writes all running entries. The cancelled word beside194 is at the clipped left edge. p197 and three additions in the final question are interlinear with placement evidence. The p216 older entry is crossed by one wavy horizontal cancellation. The final main entry has two inline formulas spanning the page, with corrections at both arguments and a crowded question below. Small isolated ink marks occur after the early l.-9 reference, right of the207 continuation, beyond the right rule at210, under the first formula arrow, and low left of the final question. The lower-corner archive23 is lighter and separately commented. There is no mathematical diagram with object nodes, no title, no date and no stated page count.',
 changes=changes,c_doubts=c_doubts,remaining_doubts=remaining,inventory=inventory,notes=notes,
 math_checks=[dict(statement_id='S024-jA-variance',type='targeted proof check',outcome='Under the conventional interpretation of Hom as the set of functors and A/a as a slice, I checked the variance: an arrow a to a\' induces postcomposition A/a to A/a\', and precomposition then gives Hom(A/a\',X) to Hom(A/a,X). A functor X to Y gives covariant postcomposition in the second argument. Thus the displayed direction Cat to hat A is compatible with the written assignment. This conditional type check does not resolve any glyph or verify the criticism of the unseen tapuscript; no source-page definition or external proof was consulted.')],
 notation=notation,abbreviations=abbreviations,
 brief_feedback='All supplied inputs were read, including the full shared notation snapshot; there was no page addendum or H_context file in this input directory. H has desc status and therefore no H collation rows are manufactured. The whole image was viewed once for layout and each supplied half once for line-by-line reading. A frozen list of24 unresolved loci was written before crops; each had one crop generated by work/scripts/crop.py and was displayed once. Crop decisions and view counts are retained separately. The inventory proceeds top to bottom and separately lists nested cancellations, insertions, underline and geometric marks. C\'s16 explicit uncertainty macros each have a decision, and page-specific context alternatives are also recorded. Only static checks were used; no OCR, external research, other reader material, other page images, or LaTeX compilation was used. The two long rules are represented together as a geometry panel because the running transcription is not a facsimile layout.'
)

(out/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
(out/'literal_diff.txt').write_text('\n'.join(difflib.unified_diff(c_text.splitlines(),reading.splitlines(),fromfile='C.tex',tofile='A/reading.tex',lineterm=''))+'\n')
print(json.dumps({'changes':len(changes),'c_doubts_and_context_decisions':len(c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'math_checks':len(report['math_checks'])}))
