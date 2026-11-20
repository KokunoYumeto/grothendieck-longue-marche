from pathlib import Path
import json

ROOT = Path('/workspace/scratch/6d55c8c3e5a7')
HERE = ROOT/'work/readers/024/B'
META = json.loads((ROOT/'work/inputs/024/metadata.json').read_text())
PLAN = json.loads((HERE/'unresolved_after_halves.json').read_text())
CROPS = {r['id']:r for r in PLAN['loci']}
changes=[]
doubts=[]

def evidence(crop=None, source=None, box=None):
    if crop:
        r=CROPS[crop]
        return {'crop':str(HERE/r['crop']),'source':r['source'],'bbox':r['bbox']}
    return {'crop':None,'source':META[source],'bbox':box}

def change(ident, place, c, reading, kind, confidence, why, crop=None, source=None, box=None):
    changes.append({'id':ident,'place':place,'c':c,'h':None,'reading':reading,
        'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,
        'confidence':confidence,'evidence':why,**evidence(crop,source,box)})

def doubt(place,c,reading,resolved,confidence,why,crop=None,source=None,box=None):
    doubts.append({'place':place,'c':c,'reading':reading,'resolved':resolved,
        'confidence':confidence,'evidence':why,**evidence(crop,source,box)})

change('left-rule','Full-height rule at the left of the correction-text column','',
    r'\draw[line width=0.35pt] (0,0) -- (3,450) -- (1,1250) -- (0,2240);',
    'drawing or diagram','high','A continuous narrow dark vertical rule runs from near the top edge down to the final entry, to the right of most page references. It is reproduced in the first TikZ figure.',
    source='whole',box=[155,20,176,2280])
change('right-rule','Full-height rule near the right edge of the text column','',
    r'\draw[line width=0.35pt] (1280,0) -- (1277,750) -- (1279,1600) -- (1277,2240);',
    'drawing or diagram','high','A second narrow dark vertical rule extends nearly the same height. Several long entries cross it. It is reproduced in the first TikZ figure.',
    source='whole',box=[1434,18,1456,2281])
change('faint-right-trace','Far-right strip of the sheet','',
    r'\draw[gray,line width=0.18pt] (1461,710) -- (1462,1510) -- (1465,2190);',
    'drawing or diagram','medium','The crop shows a faint, narrow, almost vertical trace with intermittent dark patches. Its visible geometry is retained in gray; its origin and function are not asserted. The halves establish the longer extent.',crop='28')
change('left-margin-194','Left edge beside the p194 entry',
    r'\margin{\deleted{\unsure{stating|starting}}}',
    r'\reversemarginpar\margin{\deleted{\unsure{stating|starting}}}\normalmarginpar',
    'insertion or placement','high','The cancelled word is physically to the left of 194 and partly clipped by the sheet edge. The word remains doubtful; this change preserves the physical left side.',crop='04')
change('points-194','At and just to the left of l-11 in the p194 entry',
    'l-11',
    r'\tikz[baseline=(ref.base)]{\node[inner sep=0pt] (ref) {l-11};\fill ([xshift=-1.6pt,yshift=1.4pt]ref.west) circle[radius=0.30pt];\fill ([xshift=1.5pt,yshift=5.5pt]ref.west) circle[radius=0.30pt];}',
    'drawing or diagram','medium','The crop has a small separated point just left of the l and another within its loop. Neither is a period after l. They are represented as points without a punctuation function.',crop='05')
change('apperent','p196 l18',r'\unsure{apperent|apparent}','apperent',
    'misread word','high','After pp the next letter is an open e-like loop with a horizontal entry/exit; the later e is also visible. There is no closed a bowl at the disputed position.',crop='07')
change('it-is-opener','p200 l11, opening quote before it is',"'it is''","``it is''",
    'misread symbol or index','medium','The raised opener has two joined downward legs: a short left leg and a longer right leg, followed separately by the i-dot below. The closing pair is separately visible.',crop='09')
change('is-point','p205, between is and a',r'is\unsure{.} a','is. a',
    'misread symbol or index','high','A distinct dark low oval point is visible after is. It is retained literally; no explanation for its grammatical role is supplied.',crop='11')
change('point-207','Blank space to the right of the p207 continuation, above p208','',
    r'\makebox[0pt][l]{\hspace{3.5em}\raisebox{1.2ex}{\tikz{\fill[rotate=25] (0,0) ellipse[x radius=0.65pt,y radius=0.35pt];}}}',
    'drawing or diagram','high','The lower half shows one dark isolated oblique point in the blank area inside the right rule. It has no attached word or connector; its function is left unassigned.',
    source='half_b',box=[1287,232,1321,267])
change('l7','p209, reference before such a subdivision',r'l.\unsure{-}7','l.7',
    'misread symbol or index','high','The putative minus is the continuous curled upper stroke of the crossed 7. No independently separated short minus precedes it; the period after l is clear.',crop='15')
change('before-I','p210 l17, raised cluster before I suggest',r'\unsure{``}',r'\unsure{*|``}',
    'misread symbol or index','low','The raised cluster has a small central white opening and several outward projections, favouring a star-like mark. A heavily joined or altered opening quotation remains possible; the crop does not securely determine identity.',crop='16')
change('right-marks-210','Right margin at the first p210 line','',
    r'\margin{\begin{tikzpicture}[x=1pt,y=1pt]\fill[rotate=-30] (0,0) ellipse[x radius=0.85,y radius=0.35];\fill[rotate=-35] (4,-1.8) ellipse[x radius=1.1,y radius=0.55];\end{tikzpicture}}',
    'drawing or diagram','high','Two separate short oblique dark marks stand to the right of the main vertical rule. They are reproduced without interpreting them as words or punctuation.',crop='17')
change('216-opening-state','p216 cancelled entry, opening quote before that',
    r'\deleted{line -10 ``that if the?\'\' (the repeated line -9)}',
    r'\deleted{line -10} ``\deleted{that if the}',
    'deletion state (struck given live or live given struck)','high','The long cancellation crosses line -10 and the words, but its curve passes below the opening quote group. That group is not crossed by the cancellation. The change concerns the opening edge only.',crop='18')
change('216-closing-state','p216 cancelled entry, raised group after the',
    r'\deleted{line -10 ``that if the?\'\' (the repeated line -9)}',
    r'\deleted{that if the}\unsure{?\'|\'\'|?\'\'} \deleted{(the repeated line -9)}',
    'deletion state (struck given live or live given struck)','medium','The raised terminal group stands wholly above the cancellation curve. It contains one compact curved left component and one separate right stroke; the left component could be a question mark or part of the closing quote group. Both state and punctuation are represented independently of the cancelled words.',crop='19')
change('219-t','p219 l6, its',r'``i\deleted{\unsure{t}}ts\'\'',"``its''",
    'deletion state (struck given live or live given struck)','medium','The crop shows one t with a heavy/retraced stem and a loop at its foot, followed by s. It does not establish a separate earlier t or an independent cancellation. The live word its and both paired quotation edges are clear.',crop='21')
change('low-arrow-stroke','p224, low detached stroke beneath the first long arrow','',
    r'\mathrel{\tikz[baseline=(arrow.base)]{\node[inner sep=0pt] (arrow) {$\longrightarrow$};\draw[line width=0.35pt] (-0.18,-0.18)--(-0.20,-0.30);}}',
    'drawing or diagram','high','There is one short near-vertical detached stroke below the first long arrow, slightly left of its midpoint. The arrow itself has a right head and no left bar. The added stroke is not assigned a comma or other function.',crop='23')
change('second-j-case','p224 equality, the second functor occurrence',r'j_A',r'\unsure{j|J}_A',
    'misread symbol or index','medium','This occurrence was inspected independently. It has a long descending hook, an angled top entry and no separate dot. The strokes do not securely distinguish j from J; the A subscript is clear.',crop='24')
change('argument-X','p224 equality, overwritten first argument',r'\deleted{B}\unsure{X|B}',r'\deleted{B}X',
    'misread symbol or index','high','Two strong crossing diagonals form the live X. An earlier upright and two rounded bowls remain visible as B underneath. The final form can be resolved without using the mathematical context.',crop='24')
change('jb-case','p224 crowded following note',r'j_B',r'\unsure{j|J}_B',
    'misread symbol or index','medium','The independent lower occurrence has a tall upper entry and a long bottom hook, without a dot. Its case remains ambiguous. The low B has two distinct bowls and is not ambiguous.',crop='26')
change('point-before-so','Below-left of so, above-left of the final line quotation','',
    r'\makebox[0pt][r]{\raisebox{-1.2ex}{\tikz{\fill (0,0) circle[radius=0.4pt];}}\hspace{0.5em}}',
    'drawing or diagram','high','One isolated dark point is visible below-left of so. The pair of quotation strokes for the following line lies separately farther down and right. This point is represented once without assigning it to either phrase.',crop='26')
change('twice-colon','p224 final line, following twice','l.20.twice. l.21','l.20.twice: l.21',
    'misread symbol or index','high','There are two distinct vertically arranged low points after twice, establishing a colon. The separate point after 20 is also present and retained.',crop='27')

# Every literal uncertainty in C, with unchanged doubts included.
doubt('p191, initial page reference',r'\unsure{191}',r'\unsure{191}',False,'medium',
    'The three numeral positions are visible, but much of the central curved ink and the last short upright is washed out. 191 remains the best reading; the crop does not justify certainty. The following 192 was not used to restore the ink.',crop='01')
doubt('p193 l5, cancelled word and its opener',r'\deleted{\unsure{``for}}',r'\deleted{\unsure{``for}}',False,'low',
    'A tall looped f-like form and low following traces survive several crossing strokes. for remains plausible, but the two following letters are not securely separable. The small preceding paired mark is itself heavily marked; its cancellation is retained. Confidence in cancellation is higher than confidence in the old word.',crop='03')
doubt('p194, cancelled left marginal word',r'\unsure{stating|starting}',r'\unsure{stating|starting}',False,'low',
    'The clipped start and dense oblique crossings prevent a secure choice between stating and starting. The end -ting and final loop survive. The physical left position is certain and separately corrected.',crop='04')
doubt('p196, page number before ls7 & 8',r'\unsure{196|191}',r'\unsure{196|191}',False,'low',
    'The last digit has a surviving upright/curve and a very pale low return; both 6 and 1 remain allowed. The nearby p197 insertion does not settle this occurrence.',crop='06')
doubt('p196 l18, spelling',r'\unsure{apperent|apparent}','apperent',True,'high',
    'Both disputed low joins are e-like; in particular the letter after pp lacks a closed a bowl. The literal spelling apperent is kept, without English normalization. This also covers the repeated apperent/apparent alternative in C_context.',crop='07')
doubt('p205, point after is',r'\unsure{.}','.',True,'high',
    'The low point is geometrically distinct and dark. Its existence is resolved; its grammatical purpose is not inferred. The higher short stroke nearby is at i-dot height.',crop='11')
doubt('p206 l20, cancelled remnant',r'\deleted{\unsure{?}}',r'\deleted{\unsure{?}}',False,'low',
    'A small upright/curved remnant follows 20 and is crossed. Its surviving shape does not securely establish a question mark. No additional reference is supplied. Cancellation is clear, the old character is not.',crop='12')
doubt('p209, sign before second reference 7',r'l.\unsure{-}7','l.7',True,'high',
    'The suspected minus is continuously joined to the top of the crossed 7 and forms its hooked head; no separate minus is visible.',crop='15')
doubt('p210, raised cluster before I',r'\unsure{``}',r'\unsure{*|``}',False,'low',
    'The cluster has several projections around a small white centre, unlike a clean quote pair. A star-like mark is favoured; joined/altered quotation strokes remain possible.',crop='16')
doubt('p219 l6, supposed earlier t',r'i\deleted{\unsure{t}}ts','its',True,'medium',
    'A single t with a heavy retraced stem and closed foot is visible. No independent older character is securely recoverable, so the conjectural cancelled t is removed rather than asserted from the retracing.',crop='21')
doubt('p224, earlier leading numeral',r'\deleted{\unsure{1|2}}224',r'\deleted{\unsure{1|2}}224',False,'low',
    'An older narrow upright and curved traces are entangled with the first live 2. Their full outline is not recoverable; 1 and 2 remain alternatives. The final live number 224 is clear.',crop='22')
doubt('p224, first functor letter',r'\unsure{j|J}_A',r'\unsure{j|J}_A',False,'medium',
    'There is a long hook below the neighbouring letters and an angled upper entry, but no independent dot. Current ink does not decide the case. This confirms the first occurrence of the C_context letter-with-bowl row.',crop='23')
doubt('p224, first overwritten argument',r'\deleted{B}\unsure{X|B}',r'\deleted{B}X',True,'high',
    'Crossing live diagonals establish X over the old two-bowled B. This also covers the overwritten-argument notation/context alternative.',crop='24')
doubt('p224, old argument inside Hom',r'\deleted{\unsure{B}}X',r'\deleted{\unsure{B}}X',False,'low',
    'The live X crosses a heavy old upright/bowed cluster, itself beside the vertical rule. B remains plausible underneath, but two separate old bowls cannot be recovered confidently. The first corrected argument is not used to supply the buried letter.',crop='25')
doubt('p224, cancelled baseline word in the note',r'\deleted{\unsure{is}}',r'\deleted{\unsure{is}}',False,'low',
    'Two small joined baseline forms under oblique crossings are compatible with is, but their individual strokes remain merged. The inserted isn\'t is not used as proof of the old word.',crop='26')
doubt('p224, numerator of the inserted slice expression',r'\unsure{B|A}/x',r'\unsure{B|A}/x',False,'low',
    'The small capital has an upright with angular bowed traces; it is crowded directly beneath the preceding A subscript. B is favoured, A cannot be excluded. The slash and following small x are visible.',crop='26')

# Additional C_context notation and content decisions, without manufacturing H rows.
doubt('C_context: lower functor j_B',r'j_B',r'\unsure{j|J}_B',False,'medium',
    'This separate occurrence was read from its own crop. The long hook and undotted tall top do not decide j/J. The low B is unambiguous.',crop='26')
doubt('C_context: category name',r'\mathrm{Cat}',r'\mathrm{Cat}',True,'high',
    'Cat has ordinary single-stroke handwritten letters. No doubled or script alphabet is seen.',crop='23')
doubt('C_context: hatted target',r'\widehat A',r'\widehat A',True,'high',
    'The target has a separate two-sided roof above ordinary A. No doubled or script alphabet is seen.',crop='23')
doubt('C_context: Hom',r'\operatorname{Hom}',r'\operatorname{Hom}',True,'high',
    'H has two upright strokes joined by a cross stroke, followed by low o and m. No alternate alphabet or omitted letter is supported.',crop='25')
doubt('C_context: first long arrow',r'\longrightarrow',r'\longrightarrow',True,'high',
    'A horizontal shaft and right-pointing head are clear. There is no left bar. The separate low stroke below it is drawn independently.',crop='23')
doubt('C_context: second long arrow a to Hom',r'a\longrightarrow\operatorname{Hom}',r'a\longrightarrow\operatorname{Hom}',True,'high',
    'The lower half shows a single long shaft with a right arrowhead between a and Hom, without a left bar. This is not changed to mapsto.',source='half_b',box=[1130,1003,1362,1056])
doubt('C_context: A/a and Hom delimiters',r'\operatorname{Hom}(A/a,\deleted{\unsure{B}}X))',r'\operatorname{Hom}(A/a,\deleted{\unsure{B}}X))',True,'high',
    'A, a single diagonal slash and low a precede a comma-like low turn. Two right round delimiters are present. The uncertainty here concerns only the separately recorded old B, not the slash or delimiters.',crop='25')
doubt('C_context: small arrow and slice denominator',r'\colon x\to\unsure{B|A}/x',r'\colon x\to\unsure{B|A}/x',False,'medium',
    'The colon has two points, the arrow has a right head, and the low x is separate from the slash. Only the numerator remains unresolved, as separately recorded.',crop='26')
doubt('C_context: initial informal qualification',"``informal'' would be more correct.","``informal'' would be more correct.",True,'high',
    'The upper half clearly has would be more correct, including the final low period. No stronger assertion is substituted.',source='half_a',box=[585,61,1247,125])
doubt('C_context: recense and proposed check-on',"``recense'' is not an English word and there is no obvious English equivalent. I suggest ``check-on'' as being the easiest short replacement.","``recense'' is not an English word and there is no obvious English equivalent. I suggest ``check-on'' as being the easiest short replacement.",True,'high',
    'The three-line note, including the literal recense, hyphen in check-on and qualified I suggest wording, is legible in the upper half.',source='half_a',box=[204,249,1481,432])
doubt('C_context: turned short and fizzled out',"replace ``turned short'' by possibly ``fizzled out''?","replace ``turned short'' by possibly ``fizzled out''?",True,'high',
    'The word possibly is present and the question mark stands after the closing quotation at the far right. The cancelled preceding word is a separate unresolved locus.',source='half_a',box=[395,420,1441,510])
doubt('C_context: I have got qualification',"``I've got'' is better.","``I've got'' is better.",True,'high',
    'The contraction, quoted got phrase, is better and final period beyond the right rule are visible.',source='half_a',box=[1091,498,1471,569])
doubt('C_context: wether and whether',r'``whether\'\' (``wether\'\' is\unsure{.} a castrated ram!)',"``whether'' (``wether'' is. a castrated ram!)",True,'high',
    'Whether has the first h after w; wether in the parenthesis does not. The parenthetical gloss and exclamation mark are visible. The separate dot after is is confirmed by crop 11.',source='half_a',box=[698,1125,1513,1206])
doubt('C_context: first p207 quotation',"``the one.... data''","``the one.... data''",True,'high',
    'Four separate low marks follow one, with the fourth smaller; data ends in a. Opening and closing paired quote strokes are visible.',crop='13')
doubt('C_context: replacement p207 quotation',"``the one.... datum''","``the one.... datum''",True,'high',
    'There are independently four low points in the replacement, and datum ends in a visible m. The context word surely is retained from the half.',crop='14')
doubt('C_context: allow one to check qualification',"``allow one to check'' is more usual.","``allow one to check'' is more usual.",True,'high',
    'The lower half clearly reads the quoted phrase and is more usual., with its final point.',source='half_b',box=[197,228,992,286])
doubt('C_context: p210 proposed replacement',"I suggest replace ``and look to'' by ``and then to look to''","I suggest replace ``and look to'' by ``and then to look to''",True,'high',
    'Both quoted phrases and then in the replacement are visible across the two lines. I suggest replace is left as written.',source='half_b',box=[210,412,1392,547])
doubt('C_context: p216 live question',"line -10 \\& -9: do you mean 'that the functor'' - it doesn't make sense at present.","line -10 \\& -9: do you mean 'that the functor'' - it doesn't make sense at present.",True,'high',
    'The live two-line question is legible. The opener before that is single and the closing group double. Crop 20 shows one lower dash; the higher short stroke belongs at i-dot height before it, rather than making an equals sign.',source='half_b',box=[209,674,1579,796])
doubt('C_context: p216 cancelled predecessor',r'\deleted{line -10 ``that if the?\'\' (the repeated line -9)}',r'\deleted{line -10} ``\deleted{that if the}\unsure{?\'|\'\'|?\'\'} \deleted{(the repeated line -9)}',False,'medium',
    'The words line -10, that if the and the parenthetical repeated-line note are crossed. The high quotation/punctuation groups stand above the long cancellation. The terminal identity/count remains open; crops 18 and 19 establish the two edge states independently.',crop='19')
doubt('C_context: p224 note wording and insertions',r'so \inserted{isn\'t} this \inserted{description} $j_B$ \deleted{\unsure{is}} \inserted{$\colon x\to\unsure{B|A}/x$} wrong',r'so \inserted{isn\'t} this \inserted{description} $\unsure{j|J}_B$ \deleted{\unsure{is}} \inserted{$\colon x\to\unsure{B|A}/x$} wrong',False,'medium',
    'Isn\'t is above so/this with a visible insertion marker. Description sits above the following gap with its own marker. The colon-mapping expression is interlinear above the crossed baseline word and before wrong. The word wrong is unqualified, with no terminal question mark supplied. The three recorded symbol/old-word doubts remain.',crop='26')

remaining=[
 {'place':'initial page reference','reading':r'\unsure{191}','alternatives':'191 remains best; no equally defensible complete numeral alternative','confidence':'medium','reason':'Washed-out numeral strokes remain incomplete after crop 01.'},
 {'place':'p193 l5 cancelled token','reading':r'\deleted{\unsure{``for}}','alternatives':'``for is provisional','confidence':'low','reason':'Crossings obscure the old low letters and crowd the opener; crop 03.'},
 {'place':'p194 cancelled left marginal word','reading':r'\unsure{stating|starting}','alternatives':'stating; starting','confidence':'low','reason':'Beginning clipped and crossed; crop 04.'},
 {'place':'p196 page number','reading':r'\unsure{196|191}','alternatives':'196; 191','confidence':'low','reason':'Final digit pale and incomplete; crop 06.'},
 {'place':'p206 after l.20','reading':r'\deleted{\unsure{?}}','alternatives':'? is provisional','confidence':'low','reason':'Small cancelled remnant does not securely preserve its original character; crop 12.'},
 {'place':'p210 before I suggest','reading':r'\unsure{*|``}','alternatives':'star-like mark; joined or altered opening quotation','confidence':'low','reason':'Multi-pronged cluster with a central opening, without decisive identity; crop 16.'},
 {'place':'p216 cancelled entry terminal raised group','reading':r'\unsure{?\'|\'\'|?\'\'}','alternatives':"? followed by one closer; double closer alone; ? followed by a joined double closer",'confidence':'low','reason':'Compact curved left component plus one right stroke; all remain above the cancellation, crop 19.'},
 {'place':'p224 first functor letter','reading':r'\unsure{j|J}_A','alternatives':'j_A; J_A','confidence':'medium','reason':'Undotted hooked form leaves case unsettled; crop 23.'},
 {'place':'p224 second functor letter','reading':r'\unsure{j|J}_A','alternatives':'j_A; J_A','confidence':'medium','reason':'Independent occurrence also has no separating case evidence; crop 24.'},
 {'place':'p224 old argument inside Hom','reading':r'\deleted{\unsure{B}}X','alternatives':'B is provisional underneath X','confidence':'low','reason':'Old cluster and vertical rule merge under the live strokes; crop 25.'},
 {'place':'p224 old leading numeral','reading':r'\deleted{\unsure{1|2}}224','alternatives':'1; 2','confidence':'low','reason':'Old upright and curve are entangled with the new first 2; crop 22.'},
 {'place':'p224 lower functor letter','reading':r'\unsure{j|J}_B','alternatives':'j_B; J_B','confidence':'medium','reason':'This separate hooked occurrence has no dot or decisive size distinction; crop 26.'},
 {'place':'p224 crossed baseline word','reading':r'\deleted{\unsure{is}}','alternatives':'is is provisional','confidence':'low','reason':'Two crossed joined forms remain merged; crop 26.'},
 {'place':'p224 inserted mapping numerator','reading':r'\unsure{B|A}/x','alternatives':'B/x; A/x','confidence':'low','reason':'Small capital crowded under the first formula subscript, crop 26.'},
]

inventory=[]
def inv(kind,position,objects,hand='unnamed handwritten hand'):
    inventory.append({'sheet_kind':'list','hand':hand,'element':f'{len(inventory)+1:02d}','kind':kind,'position':position,'first_words_or_objects':objects,'transcribed':'yes'})

inv('drawing','Left of text column, virtually full height','Long vertical rule')
inv('drawing','Right edge of text column, virtually full height','Long vertical rule')
inv('drawing','Far-right strip, middle and lower page','Faint vertical trace; origin not assigned')
inv('text','Top entry, p191','p.191 l7; didn\'t; informal would be more correct.')
inv('text','Second line, same page reference','l.-9 Riemannian; l-1 + -2 informal again.')
inv('text','p192 l10','had turned out shorter than hoped, due to lack')
inv('text','p192 l-19, three lines','recense is not an English word; I suggest check-on')
inv('text','p193 l5','replace turned short by possibly fizzled out?')
inv('deletion','Nested at start of p193 correction','Doubtful cancelled ``for')
inv('margin note','Far left beside p194, clipped by edge','Doubtful stating/starting')
inv('deletion','Nested in p194 left marginal note','The entire doubtful word is crossed')
inv('text','p194 main line','line -14 informal; l-13 informal; l-11 I\'ve got is better.')
inv('drawing','Nested at/left of l-11','Two tiny isolated points, no punctuation role assigned')
inv('text','p194 continuation','l-8 literature')
inv('text','p196/p197 line','ls7 & 8 insufficient; l18 apperent; l-9 & -10 wasn\'t; l-8 isn\'t')
inv('insertion','Above boundary after apperent','p197 with its connecting/caret strokes')
inv('text','p198 l4','don\'t')
inv('text','p200 l11','its; no apostrophe; it\'s used as an abbrev for it is')
inv('text','p200 continuation','l17 substitute; l19 in terms; l-14 substitute again')
inv('text','p201 line','l.19 workable; l.-5 don\'t; l-3 isn\'t; l-2 isn\'t')
inv('text','p202 line','l3 doesn\'t; l8 didn\'t; l13 couldn\'t; l17 wouldn\'t')
inv('text','p203 l-4','wasn\'t')
inv('text','p204 l3','isn\'t')
inv('text','p205 line','l14 insufficient; l-7 whether; wether is. a castrated ram!')
inv('text','p206 line','l.8 don\'t; l.20 seesaw')
inv('deletion','After 20 in p206','Doubtful small cancelled ?')
inv('text','p207 l15','the one.... data surely should be the one.... datum')
inv('text','p207 continuation','l-9 allow one to check is more usual.')
inv('drawing','Blank right side of p207 continuation, above p208','One isolated oblique point inside the right rule')
inv('text','p208 line','l.8 a long time ago; l-9 & -10 couldn\'t be')
inv('text','Nested under a in p208 quotation','Double underline confined to a')
inv('text','p209 line','l.5 shouldn\'t; l.7 such a subdivision; l.-9 wouldn\'t')
inv('text','p210 two-line entry','l.17. Grammar\'s wrong here; I suggest replace and look to by and then to look to; -l.4 its no apostrophe.')
inv('text','Nested raised mark before I in p210','Uncertain star-like/quotation group')
inv('drawing','Right margin beside first p210 line','Two short isolated oblique dark marks')
inv('text','p213 line1','At long last')
inv('text','p216 first entry, cancelled wording with high live groups','line -10; that if the; the repeated line -9')
inv('deletion','p216 first entry, left segment','line -10 crossed')
inv('text','p216 first entry, raised opening group','Opening double quote group above the cancellation')
inv('deletion','p216 first entry, middle segment','that if the crossed')
inv('text','p216 first entry, raised terminal group','Uncertain question/closing-quote group above the cancellation')
inv('deletion','p216 first entry, right parenthesis','(the repeated line -9) crossed')
inv('text','p216 live two-line question','line -10 & -9: do you mean that the functor; it doesn\'t make sense at present.')
inv('text','p217 l5','didn\'t')
inv('text','p219 line','l.6 its; l.8 we\'ve got')
inv('text','p221 l11','analogy')
inv('text','p224 left reference','224 line2 c.f p.32')
inv('deletion','Within first digit of p224 reference','Old doubtful 1/2 under first live 2')
inv('display','p224 long mathematical line','j/J_A : Cat → A-hat; j/J_A(X) = (a → Hom(A/a,X))')
inv('drawing','Under first long arrow in p224 formula','Short detached near-vertical stroke')
inv('deletion','Nested in first argument of p224 equality','Old B under live X')
inv('deletion','Nested in second argument of Hom','Doubtful old B under live X, near vertical rule')
inv('text','p224 crowded following baseline note','so this j/J_B wrong, with three interlinear additions')
inv('insertion','Above gap between so and this','isn\'t with insertion marker')
inv('insertion','Above gap after this','description with insertion marker')
inv('deletion','Baseline between j/J_B and wrong','Doubtful is, crossed')
inv('insertion','Interlinear above the crossed baseline word, before wrong','Colon x → doubtful B/A divided by x')
inv('drawing','Below-left of so and above-left of the final quotation','One isolated point')
inv('text','Final line, p224 continuation','l.17 commutes with; also l.20.twice: l.21 if we have two')
inv('text','Bottom-left corner','Archive sheet number 23, retained only as a comment','another unnamed pencil hand')

outcomes={
 '01':('retained doubt','Initial page number remains unsure 191.'),
 '02':('confirmed','A low point after again is visible; retain C period.'),
 '03':('retained doubt','Cancelled ``for remains provisional; cancellation retained.'),
 '04':('retained doubt','stating/starting remains open; physical left side corrected.'),
 '05':('confirmed with addition','No period after l; two isolated points at/left of its loop are drawn.'),
 '06':('retained doubt','196/191 remains open independently of inserted p197.'),
 '07':('resolved','apperent resolved; insertion p197 and following low comma confirmed.'),
 '08':('confirmed','First explanatory it\'s has one tapered opener and two separate closing strokes; C retained.'),
 '09':('resolved','Opener before it is has two joined legs; changed to paired opening quotes.'),
 '10':('confirmed','Wouldn\'t opener has two joined legs and double closer; C retained.'),
 '11':('resolved','Distinct low point after is retained without uncertainty; wether opener/closer retained.'),
 '12':('retained doubt','Cancelled remnant after 20 still only provisionally ?.'),
 '13':('confirmed','Four low marks before data, C retained.'),
 '14':('confirmed','Four low marks before datum, independently confirmed.'),
 '15':('resolved','No independent minus before 7; top stroke belongs to crossed numeral.'),
 '16':('retained doubt','Star-like mark favoured over joined quotation, both retained.'),
 '17':('resolved','Two oblique isolated marks reproduced geometrically.'),
 '18':('resolved','Opening quote group lies clear above cancellation.'),
 '19':('partly resolved','Terminal group lies clear above cancellation; identity/count remains unsure ?\', \'\', or ?\'\'.'),
 '20':('confirmed','One lower dash; higher stroke at i-dot height, no equals sign added.'),
 '21':('resolved','Single retraced t, no independently established old t; conjectural deletion removed.'),
 '22':('retained doubt','Old 1/2 beneath first live 2 remains uncertain.'),
 '23':('partly resolved','First j/J case retained; Cat/hat/arrow confirmed; low detached stroke drawn.'),
 '24':('partly resolved','Live X over B resolved; second j/J occurrence independently marked doubtful.'),
 '25':('retained doubt','Slash/comma/delimiters confirmed; old B beneath X remains provisional.'),
 '26':('partly resolved','Insertion placement confirmed; j/J_B, old is and B/A numerator remain doubtful; isolated point drawn.'),
 '27':('resolved','Colon after twice, while period after20 retained.'),
 '28':('geometry retained','Faint vertical trace reproduced; no editorial or material origin assigned.'),
}
for record in PLAN['loci']:
    status,decision=outcomes[record['id']]
    record['initial_status']='unresolved after the required half view, before any crop'
    record['status']='inspected once'
    record['outcome_status']=status
    record['decision']=decision
    record['displayed']=True
(HERE/'unresolved_after_halves.json').write_text(json.dumps(PLAN,ensure_ascii=False,indent=2)+'\n')

report={
 'scan':24,'reader':'B','model':'GPT-6 Astra Pro','effort':'not exposed',
 'viewed':[META['whole'],META['half_a'],META['half_b']],
 'layout':'A continuous handwritten English correction list, with cited page numbers mostly left of a long vertical rule and the correction text to its right. A second dark vertical rule stands near the right edge of the writing; a faint longer trace appears farther right. There is one principal unnamed text hand, a clipped cancelled marginal word at p194, several corrections/insertions, a broad wavy cancellation through the first p216 entry, and crowded mathematical writing/interlineations at p224. Isolated points and two right-margin marks are retained geometrically. The visible archive number 23 is in a separate pencil hand at bottom left; it is not manuscript pagination. There is no title or date, printed form, stamp, diagram, or reused typed text on this sheet.',
 'changes':changes,'c_doubts':doubts,'remaining_doubts':remaining,'inventory':inventory,
 'notes':[
   'English corrections address cited typescript pages from a faint initial number read as 191 through 224. The listed numerals are references, not pagination of these notes. No title, date, or stated page count is present; archive 23 is only a comment.',
   'At p191 l18 the writer says informal would be more correct. At p192 l-19 the writer says recense is not English and suggests check-on as the easiest short replacement. At p193 l5, possibly fizzled out is proposed for turned short with a terminal question mark.',
   'At p194 l-11, I\'ve got is said to be better. The p196 l18 spelling reads apperent. An inserted p197 begins the references to wasn\'t and isn\'t.',
   'At p200 l11 the possessive its is distinguished from the abbreviation it\'s for it is. At p205 l-7, whether is contrasted with wether, glossed as a castrated ram, with an exclamation mark and a literal low point after is.',
   'At p207 l15 the one.... data surely should be the one.... datum; each quoted span has four low dots. In its continuation allow one to check is called more usual. At p208 l8 only a is double-underlined.',
   'At p210 l17 the writer says Grammar\'s wrong here and suggests replacing and look to by and then to look to. The separate -l.4 correction requests its with no apostrophe. The raised mark before I remains doubtful.',
   'At p216 a first entry mentioning line -10, that if the, and the repeated line -9 is cancelled, while its high quotation/punctuation groups stand above the cancellation. The new two-line entry asks do you mean that the functor and says it doesn\'t make sense at present.',
   'At p224 line2 a reference to p32 precedes a displayed functor to A-hat and a Hom formula, with two overwritten arguments. The following crowded note inserts isn\'t, description and a colon/mapping expression into a question ending wrong, without a visible terminal question mark. Functor case and the small slice numerator remain uncertain.',
 ],
 'math_checks':[
   {'statement_id':'S024-jA-variance','type':'targeted proof check','outcome':'Using the ordinary functor-set interpretation of Hom, I checked the variance of the displayed a-assignment at fixed X: a morphism a→a\' induces postcomposition A/a→A/a\'; precomposition then gives Hom(A/a\',X)→Hom(A/a,X). Thus the written assignment is compatible with a presheaf target A-hat. This checks the displayed typing/variance only; it does not establish any surrounding result or settle j/J from mathematics.'},
   {'statement_id':'S024-lower-slice-typing','type':'targeted proof check','outcome':'I compared the lower candidate x→B/x with the displayed j_A:Cat→A-hat. If B is the intended numerator and x is an object of B, then B/x is a category and the assignment has objects of B as inputs; it is not literally the same type as Cat→B-hat. This is a conditional scope/type check, consistent with the writer asking whether the description is wrong. It does not resolve the numerator B/A or any cancelled word, and no mathematical correction was inserted.'}
 ],
 'notation':[
   {'sign':r'\unsure{j|J}_A; \unsure{j|J}_A; \unsure{j|J}_B','location':'p224 first declaration, equality, and following note','reading':'Three independently doubtful cases, each marked','evidence':'Crops23,24,26 show separately undotted descending hooks with angled tops; neither case is securely decided.'},
   {'sign':r'\mathrm{Cat}; \widehat A; \operatorname{Hom}','location':'p224 formula','reading':r'\mathrm{Cat}; \widehat A; \operatorname{Hom}','evidence':'Crops23/25 show ordinary single contours, a distinct pointed roof, and H with two stems.'},
   {'sign':r'\longrightarrow; \to; A/a; \unsure{B|A}/x','location':'p224 formula and interlinear mapping','reading':'Right arrows without left bars; slashes retained, final numerator doubtful','evidence':'Crops23,25,26 and the lower half independently show arrowheads, diagonal slashes and small denominator letters.'},
   {'sign':r'\deleted{B}X; \deleted{\unsure{B}}X','location':'p224 two corrected arguments','reading':'First live X certain; second old B remains uncertain','evidence':'Crop24 separates two strong diagonals over two old bowls; crop25 is crowded against the vertical rule.'},
   {'sign':'l.7','location':'p209 second reference','reading':'No minus before crossed 7','evidence':'Crop15 shows the short curved upper stroke joined directly into the numeral.'},
   {'sign':r'\uuline{a}','location':'p208 l8','reading':'Double underline only beneath a','evidence':'Lower half shows two short returned baseline strokes below a, ending before long.'},
   {'sign':'four low dots','location':'p207 both quoted spans','reading':'.... in each occurrence','evidence':'Crops13 and14 independently separate four low marks.'},
   {'sign':'quote edges outside cancellation','location':'p216 first entry','reading':r'``\deleted{that if the}\unsure{?\'|\'\'|?\'\'}','evidence':'Crops18/19 place each high group above the wavy cancellation; terminal identity/count is unresolved.'},
   {'sign':'colon','location':'p224 final line, after twice','reading':'twice:','evidence':'Crop27 shows two vertically separated dark points.'},
   {'sign':'isolated points and short strokes','location':'p194 l-11; p207 right blank; p210 right margin; p224 below arrow and below-left of so','reading':'Geometrical TikZ marks without an assigned punctuation role','evidence':'Crop05, lower half, crops17,23,26 retain their positions and separation from neighbouring text.'},
 ],
 'abbreviations':[
   {'form':'p. / p','expansion':'page, tentative list only','place':'references throughout'},
   {'form':'l / l. / ls','expansion':'line / lines, tentative list only','place':'line references throughout'},
   {'form':'abbrev','expansion':'abbreviation, tentative list only','place':'p200 l11'},
   {'form':'c.f','expansion':'compare, tentative list only','place':'p224 line2'},
   {'form':'Cat','expansion':'categories, mathematical category-name interpretation only','place':'p224 formula'},
   {'form':'Hom','expansion':'maps/functors, interpretation used only for the stated conditional typing check','place':'p224 formula'},
 ],
 'brief_feedback':'No page addendum or H_context file was supplied in this page input directory. H status is desc, so every change row has h=null and diff_h=false, and no comparison with its descriptive paraphrase is manufactured. Whole image and each supplied half were displayed exactly once. All 28 loci listed after the halves received exactly one enhanced crop from scripts/crop.py; every generated crop was displayed and inspected, with no recrop or reopened half. The before-crop list, decisions, crop files and crop log are retained. No OCR, external research, other-page inspection or LaTeX compilation was used. The distinction between genuine minute ink marks and copying artefacts remains interpretive at the faint far-right trace; its observed geometry is retained without assigning origin. Static checks and a literal C diff were used for final consistency. Inventory covers every list entry and every nested insertion/deletion, underline, marginal item and retained geometric mark.',
 'coverage':{'whole_views':1,'half_a_views':1,'half_b_views':1,'crops_generated':28,'crops_inspected':28,'literal_C_uncertainties_reviewed':16,'H_status':'desc','inventory_rows':len(inventory)},
 'crop_decisions':[{k:r[k] for k in ('id','crop','question_after_half','outcome_status','decision','displayed')} for r in PLAN['loci']],
}

# Literal apostrophes in raw strings above must not acquire TeX backslash escapes.
def clean(obj):
    if isinstance(obj,str): return obj.replace("\\'", "'")
    if isinstance(obj,list): return [clean(v) for v in obj]
    if isinstance(obj,dict): return {k:clean(v) for k,v in obj.items()}
    return obj
report=clean(report)
(HERE/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts_and_context_decisions':len(doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'math_checks':len(report['math_checks'])}))
