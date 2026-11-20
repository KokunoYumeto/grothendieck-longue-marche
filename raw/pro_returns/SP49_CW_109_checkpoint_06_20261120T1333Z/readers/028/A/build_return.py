from pathlib import Path
import json, re, difflib
D=Path('work/readers/028/A')
M=json.loads(Path('work/inputs/028/metadata.json').read_text())
A=M['half_a']; B=M['half_b']; W=M['whole']
F=json.loads((D/'frozen_unresolved.json').read_text())
L={x['id']:x for x in F['loci']}

def crop(i): return str(D/'crops'/f'{i}.jpg')
def loc(i):
    q=L[i]
    return {'crop':crop(i),'source':M[q['source']],'bbox':q['bbox']}

g={
'left_rule':r'\draw[line width=.35pt] (258,90)--(255,545)--(251,935)--(248,1270)--(242,1760)--(239,2275)--(236,2348);',
'right_rule':r'\draw[line width=.35pt] (1537,94)--(1535,350)--(1529,800)--(1527,1100)--(1524,1520)--(1521,1950)--(1519,2280)--(1521,2348);',
'faint_trace':r'\draw[black!22,line width=.25pt] (58,75)--(57,240)--(55,700)--(53,1100)--(50,1700)--(49,2140);\draw[black!12,line width=.25pt] (49,2140)--(49,2215);',
'upper_right_dash':r'\draw[line width=.18pt] (1439,168)--(1447,168);',
'right_point':r'\fill (1522,334) circle[radius=1.0];',
'afraid_marks':r'\fill (479,337) circle[radius=1.1];\draw[line width=.24pt] (396,378)--(400,380);\draw[line width=.24pt] (533,391)--(537,386);',
'again_mark':r'\draw[line width=.18pt] (1089,729)--(1099,730);',
'left_352_point':r'\fill (109,1018) circle[radius=1.1];',
'lower_left_marks':r'\draw[line width=.24pt] (212,2125)--(214,2130)--(218,2131);\fill (226,2125) circle[radius=1.1];',
'lower_right_marks':r'\fill (1433,1990) circle[radius=1.0];\fill (1437,1984) circle[radius=1.0];'
}
overlap=r"in\tikz[baseline=(aold28A.base)]{\node[inner sep=0pt] (aold28A) {\deleted{\unsure{a|o}}};\node[anchor=base west,inner sep=0pt] at (aold28A.base west) {a};}dequacies'"
bottom=r'\node[anchor=base west,inner sep=0pt,font=\fontsize{8}{10}\selectfont] at (1587,2310) {\deleted{\unsure{end|ed}}};'

tex=r'''\scanpage{28}

% The list and the ruled sheet share one coordinate field. Coordinates reproduce
% the supplied image's relative positions, including the long blank lower part.
% The faint far-left trace has fading, indeterminate ends: the path represents
% the observed segment, not an asserted original endpoint or a named operation.
\noindent\begin{tikzpicture}[x=.0075cm,y=-.0075cm,line cap=round,line join=round]
\path[use as bounding box] (20,45) rectangle (1670,2348);
% BEGIN left_rule
'''+g['left_rule']+r'''
% END left_rule
% BEGIN right_rule
'''+g['right_rule']+r'''
% END right_rule
% BEGIN faint_trace
'''+g['faint_trace']+r'''
% END faint_trace
% Prominent isolated marks, with no assigned punctuation or editorial function.
% BEGIN upper_right_dash
'''+g['upper_right_dash']+r'''
% END upper_right_dash
% BEGIN right_point
'''+g['right_point']+r'''
% END right_point
% BEGIN afraid_marks
'''+g['afraid_marks']+r'''
% END afraid_marks
% BEGIN again_mark
'''+g['again_mark']+r'''
% END again_mark
% BEGIN left_352_point
'''+g['left_352_point']+r'''
% END left_352_point
% BEGIN lower_left_marks
'''+g['lower_left_marks']+r'''
% END lower_left_marks
% BEGIN lower_right_marks
'''+g['lower_right_marks']+r'''
% END lower_right_marks

\begin{scope}[every node/.style={anchor=base west,inner sep=0pt,font=\fontsize{9}{11}\selectfont}]
\node at (150,108) {p335};
\node at (280,113) {l.7. ``don't''};
\node at (595,118) {l-16 ``wouldn't''.};

\node at (146,176) {p.336};
\node at (280,177) {l.-8 ``skilful''};

\node at (149,237) {p.338};
\node at (280,241) {l12 ``its''};
\node at (570,249) {l-8 ? ``and even'' perhaps.};

\node at (144,301) {p.339};
\node at (286,305) {l-12 ``shouldn't'' \deleted{\unsure{\&|l}}};

\node at (149,363) {340};
\node at (282,366) {l.18 ``afraid''};

\node at (111,429) {p341};
\node at (280,429) {l.2};
\node at (389,434) {``and alongside \uline{got me} back''};
\node at (965,445) {is perhaps better.};
\node at (1322,445) {l7};
\node at (1396,448) {'doesn't''};
\node at (1566,450) {\& l.8};

\node at (167,491) {342};
\node at (286,496) {l13 ``didn't''};
\node at (598,499) {l.-8 ``couldn't''};

\node at (167,557) {344};
\node at (289,558) {l.17 ``commutes with''};
\node at (839,573) {l.20 ``allows us to''};
\node[font=\fontsize{7}{9}\selectfont] at (1338,578) {l.21 ``commuting with''};

\node at (304,610) {l.23 ``commutes with''};
\node at (786,631) {l-9 ``commute with''};

\node at (132,680) {p.345};
\node at (282,685) {l.5 ``commutes with''};
\node at (730,697) {l.7 ``with'' (again).};
\node at (1148,701) {l.10 ``characterises''};

\node at (137,744) {p.348};
\node at (281,750) {l-2 ``won't''};

\node at (133,815) {p350};
\node at (280,817) {l.14 ``its'' also in l.15.};
\node at (821,817) {l-10};
\node at (981,824) {``\unsure{\uuline{i}|\uline{i}}ndependent of''};
\node[font=\fontsize{8}{10}\selectfont] at (1308,831) {(``from'' can also be};
\node at (375,879) {used but is less usual.)};

\node at (131,944) {p351};
\node at (305,944) {l12 ``wasn't''};
\node at (611,947) {l14 ``wouldn't''};
\node at (948,950) {l-11};
\node at (1066,953) {``'''+overlap+r'''};

\node at (133,1006) {p352};
\node at (304,1005) {l8 ``didn't''};

\node at (130,1063) {p353};
\node at (274,1066) {l.9 ``its''};
\node at (537,1073) {l-17 ``inadequate''};

\node at (132,1127) {p354};
\node at (291,1134) {l8 ``don't''};
\end{scope}

% The cancelled marginal word is at the foot of the sheet, outside the right
% rule. The cancellation traverses the whole word; its buried n is not secure.
% BEGIN bottom_note
'''+bottom+r'''
% END bottom_note
\end{tikzpicture}

% archive sheet number: 27
'''
(D/'reading.tex').write_text(tex)

changes=[]
def ch(id,place,c,reading,kind,evidence,confidence='high',cropid=None,source=None,bbox=None):
    row={'id':id,'place':place,'c':c,'h':None,'reading':reading,'diff_c':True,'diff_h':False,'kind':kind,'marked_in_H':False,'confidence':confidence,'evidence':evidence}
    row.update(loc(cropid) if cropid else {'crop':None,'source':source,'bbox':bbox})
    changes.append(row)
ch('342_ref_stop','342, second line reference',r'l-8',r'l.-8','omission','A small closed black point is separate from the l foot and lies below-left of the following horizontal minus. The point is neither the foot nor part of the dash.',cropid='06')
ch('351_overlap','p351 l-11, first a of inadequacies',r"in\deleted{\unsure{a|o}}adequacies'",overlap,'insertion or placement','The small older oval and live a occupy the same character space. The older form is not an additional preceding character. Both possible old forms remain uncertain; the live a and the single closing quotation stroke are legible.',cropid='12')
ch('left_rule','Vertical rule between page references and corrections','',g['left_rule'],'drawing or diagram','One thin dark continuous rule starts near (258,90), separates the left references from the correction text, and runs to (236,2348) at the bottom edge. Both halves show its continuation.',source=W,bbox=[230,78,267,2351])
ch('right_rule','Vertical rule near right edge, crossing several long entries','',g['right_rule'],'drawing or diagram','A thin dark rule begins near (1537,94) and reaches the foot near (1521,2348). At p341 it crosses the terminal t region of does not contraction, and at p344/p345/p350 it passes through or immediately beside the long continuations. The path stays in the text coordinate field.',source=W,bbox=[1507,82,1547,2351])
ch('faint_trace','Far-left fading vertical trace','',g['faint_trace'],'drawing or diagram','The faint grey trace is visible near x58 in the upper crop and near x49 low on the sheet. The upper crop is entered by the trace, so it does not establish the original start. The lower crop shows fading around whole-page y2215 rather than a sharp terminal stroke. The drawn extent is approximate and does not reach the bottom edge.',confidence='medium',cropid='14')
ch('upper_dash','Upper-right blank area above p.338 level','',g['upper_right_dash'],'drawing or diagram','Short isolated horizontal black stroke at about (1439,168) to (1447,168), well left of the right rule; no textual function is assigned.',source=A,bbox=[1428,155,1460,182])
ch('right_point','Blank space just left of right rule at 340 level','',g['right_point'],'drawing or diagram','One small isolated dark point lies immediately left of the rule near (1522,334). It is geometrically separate from the ruled stroke.',source=A,bbox=[1514,325,1542,342])
ch('afraid_marks','340 l.18, isolated marks near afraid','',g['afraid_marks'],'drawing or diagram','The crop shows a small round point above the r/a region, separate from the normal i dot, and two small low oblique marks: one below-left of the word and one below-right. The latter is below the word baseline, so it is retained geometrically without calling it a sentence stop.',cropid='03')
ch('again_low_mark','Between p.345 and p.348, beneath right parenthesis of again','',g['again_mark'],'drawing or diagram','A short separate low horizontal dark mark occurs below the parenthesis, around (1089,729) to (1099,730). This is distinct from the baseline protrusion retained as the period after (again).',cropid='08')
ch('left_352_point','Left margin beside the p352/p353 interval','',g['left_352_point'],'drawing or diagram','Small isolated black point near (109,1018), left of the page-reference column; no punctuation function is inferred.',source=A,bbox=[99,1009,121,1028])
ch('lower_right_points','Lower blank field, just left of right rule','',g['lower_right_marks'],'drawing or diagram','Two tiny dark points sit diagonally apart near whole-image (1433,1990) and (1437,1984). They are preserved as unassigned marks.',source=B,bbox=[1424,875,1447,899])
ch('lower_left_marks','Lower blank field, immediately left of reference rule','',g['lower_left_marks'],'drawing or diagram','A short bent dark stroke and a separate point occur near whole-image (212,2125) and (226,2125); the lower endpoint crop makes their separation clear. Their origin and function are unassigned.',cropid='15')
ch('bottom_note_placement','Bottom-right outside the right vertical rule',r'\margin{\deleted{\unsure{end|ed}}}',bottom,'insertion or placement','The cancelled word is at the extreme foot of the sheet, about 1170 pixels below the final correction entry, and physically to the right of the rule. It is not an immediate continuation of p354. Anchored placement preserves that separation; the reading uncertainty is unchanged.',cropid='13')

c_doubts=[]
def cd(place,c,reading,resolved,confidence,evidence,cropid=None,source=None,bbox=None):
    q={'place':place,'c':c,'reading':reading,'resolved':resolved,'confidence':confidence,'evidence':evidence}
    q.update(loc(cropid) if cropid else {'crop':None,'source':source,'bbox':bbox})
    c_doubts.append(q)
cd('p.339 l-12, cancelled sign',r'\deleted{\unsure{\&|l}}',r'\deleted{\unsure{\&|l}}',False,'low','The crossing certainly cancels the whole sign. An upper loop and a low rightward foot survive, but the lower crossing conceals whether the earlier body was an ampersand or a looped l. Cancellation extent is secure; glyph identity is not.',cropid='02')
cd('p350 l-10, initial i underline',r'\unsure{\uuline{i}|\uline{i}}ndependent',r'\unsure{\uuline{i}|\uline{i}}ndependent',False,'medium','A short upper bar and dense touching returned strokes lie below the initial i. Multiple ink passes are certain, but their overlap does not decide a double underline against a retraced single underline. The alternatives of C and C_context are retained.',cropid='09')
cd('p351 l-11, old letter',r'\deleted{\unsure{a|o}}',r'\deleted{\unsure{a|o}}',False,'low','The old body is oval and crowded against the live a. Its apparent right-hand stem can belong to the new a; both old a and old o remain possible. The full reading separately overlays the new a in the same space.',cropid='12')
cd('Bottom-right cancelled word',r'\deleted{\unsure{end|ed}}',r'\deleted{\unsure{end|ed}}',False,'low','A left loop and final d ascender/bowl survive under several oblique cancellation strokes. The potential middle n is largely hidden, so neither end nor ed is excluded. The full-word cancellation is certain.',cropid='13')
cd('p341 l.2, underline scope raised in C_context',r'\uline{got me}',r'\uline{got me}',True,'high','The upper half shows a single low rule beginning under the g, interrupted/crossed by its descender, and extending through the e of me. It stops before back.',source=A,bbox=[680,398,812,466])
cd('p351 l-11, quotation asymmetry raised in C_context',r"``in\deleted{\unsure{a|o}}adequacies'",'``'+overlap,True,'high','Two distinct raised opening bodies occur before in, and exactly one detached high closing stroke occurs after the plural s. The single closer is retained independently of the uncertain overwritten letter.',cropid='12')
cd('p.338 l-8, qualified proposal in C_context',r'? ``and even\'\' perhaps.',r'? ``and even\'\' perhaps.',True,'high','The question mark precedes the proposal; perhaps follows it and a low terminal point is visible farther right. Crop 01 separates the two closing quotation strokes. No stronger recommendation is supplied.',cropid='01')
cd('p341 l.2, qualified wording in C_context',r"``and alongside \uline{got me} back'' is perhaps better.",r"``and alongside \uline{got me} back'' is perhaps better.",True,'high','The full proposal and the qualification is perhaps better are readable in the upper half. Crop 04 shows a compact slanted baseline stop after better, without a distinct comma tail; C period retained.',cropid='04')
cd('p350 l-10, of/from qualification in C_context',r"(``from'' can also be used but is less usual.)",r"(``from'' can also be used but is less usual.)",True,'high','The parenthesis continues onto the next physical line. It explicitly allows from but calls it less usual, and ends with a stop inside the closing parenthesis. The opening pair partly meets the parenthesis but has two small bodies in crop 10.',cropid='10')
# Use unescaped literal quotation strokes in the context decision.
c_doubts[-3]['c']=r'''? ``and even'' perhaps.'''
c_doubts[-3]['reading']=r'''? ``and even'' perhaps.'''

remaining=[
{'place':'p.339 l-12, cancelled sign','reading':r'\deleted{\unsure{\&|l}}','alternatives':r'\&; l','confidence':'low','reason':'The crossing hides the lower letter contour; cancellation is certain but neither candidate is excluded.'},
{'place':'p350 l-10, initial underline','reading':r'\unsure{\uuline{i}|\uline{i}}ndependent','alternatives':r'\uuline{i}; \uline{i}','confidence':'medium','reason':'Several touching ink passes do not securely distinguish two underline levels from retracing.'},
{'place':'p351 l-11, overwritten old letter','reading':r'\deleted{\unsure{a|o}}','alternatives':'a; o','confidence':'low','reason':'The new a occupies the same space and can supply the apparent stem of an old a.'},
{'place':'Bottom-right cancelled word','reading':r'\deleted{\unsure{end|ed}}','alternatives':'end; ed','confidence':'low','reason':'The cancellation hides the middle of the word; the e-like left loop and final d survive.'},
{'place':'Far-left faint trace, original endpoints','reading':g['faint_trace'],'alternatives':'A longer trace fading beyond the observed segment; a trace ending within the fading zones','confidence':'low','reason':'The upper crop is entered by the trace, and the lower trace fades into the paper texture. The drawing records only an approximate observed extent, not a sharply established original start/end.'}
]

inventory=[]
def inv(element,kind,position,words,hand='his hand'):
    inventory.append({'sheet_kind':'list','hand':hand,'element':element,'kind':kind,'position':position,'first_words_or_objects':words,'transcribed':'yes'})
inv('01','drawing','From top of first line to bottom, between page references and correction text','Left dark vertical rule, x258 to x236')
inv('02','drawing','From top of first line to bottom, near right edge','Right dark vertical rule, x1537 to x1521')
inv('03','drawing','Far-left edge of writing surface, fading at both ends','Faint vertical trace near x58 to x49','unattributed faint trace')
entries=[
('04','Top line, p335, left correction','p335 l.7. ``don\'t\'\''),
('05','Top line, p335, right correction',"l-16 ``wouldn't''."),
('06','Second line, p.336',"p.336 l.-8 ``skilful''"),
('08','Third line, p.338, first correction',"p.338 l12 ``its''"),
('09','Third line, p.338, second proposal',"l-8 ? ``and even'' perhaps."),
('10','Fourth line, p.339',"p.339 l-12 ``shouldn't''"),
('12','Fifth line, 340',"340 l.18 ``afraid''"),
('15','Sixth line, p341, main proposal',r"p341 l.2 ``and alongside \uline{got me} back'' is perhaps better."),
('17','Sixth line, p341, right-hand continuation across rule',"l7 'doesn't'' & l.8"),
('18','Seventh line, 342, first correction',"342 l13 ``didn't''"),
('19','Seventh line, 342, second correction',"l.-8 ``couldn't''"),
('20','Eighth line, 344, first correction',"344 l.17 ``commutes with''"),
('21','Eighth line, 344, second correction',"l.20 ``allows us to''"),
('22','Eighth line, 344, small right-hand continuation across rule',"l.21 ``commuting with''"),
('23','Ninth line, 344 continuation, first correction',"l.23 ``commutes with''"),
('24','Ninth line, 344 continuation, second correction',"l-9 ``commute with''"),
('25','Tenth line, p.345, first correction',"p.345 l.5 ``commutes with''"),
('26','Tenth line, p.345, second correction',"l.7 ``with'' (again)."),
('27','Tenth line, p.345, third correction beside right rule',"l.10 ``characterises''"),
('29','Eleventh line, p.348',"p.348 l-2 ``won't''"),
('30','Twelfth line, p350, first correction',"p350 l.14 ``its'' also in l.15."),
('31','Twelfth line with next-line continuation, p350 l-10',r"l-10 ``\unsure{\uuline{i}|\uline{i}}ndependent of'' (``from'' can also be used but is less usual.)"),
('33','Fourteenth line, p351, first correction',"p351 l12 ``wasn't''"),
('34','Fourteenth line, p351, second correction',"l14 ``wouldn't''"),
('35','Fourteenth line, p351, third correction','l-11 ``'+overlap),
('38','Fifteenth line, p352',"p352 l8 ``didn't''"),
('40','Sixteenth line, p353, first correction',"p353 l.9 ``its''"),
('41','Sixteenth line, p353, second correction',"l-17 ``inadequate''"),
('42','Seventeenth line, p354',"p354 l8 ``don't''")]
for e,pos,words in entries: inv(e,'text',pos,words)
# Nested states and the additional drawings are separately inventoried.
inv('07','drawing','Upper-right blank, y168','Short horizontal mark','unattributed mark')
inv('11','deletion','Immediately after p.339 should not contraction',r'\deleted{\unsure{\&|l}}')
inv('13','drawing','Above and below afraid at 340 l.18','One extra upper point and two low oblique marks','unattributed marks')
inv('14','drawing','Just left of right rule at 340 level','Small isolated point','unattributed mark')
inv('16','text','Nested in p341 l.2 proposal',r'\uline{got me} — one underline spanning both words')
inv('28','drawing','Below (again), between p.345 and p.348','Short horizontal stroke','unattributed mark')
inv('32','text','Nested at the initial i of independent in p350 l-10',r'\unsure{\uuline{i}|\uline{i}}')
inv('36','deletion','Within p351 inadequacies, under the first a',r'\deleted{\unsure{a|o}}')
inv('37','text','Same glyph space as old a/o, p351 inadequacies','Live a written over the old letter')
inv('39','drawing','Left of reference column, between p352 and p353','Isolated dark point','unattributed mark')
inv('43','drawing','Lower blank right, near whole y1984–1990','Two isolated points','unattributed marks')
inv('44','drawing','Lower blank left, near whole y2125','Bent stroke and separate point','unattributed marks')
inv('45','margin note','Extreme bottom right, outside right rule',r'\deleted{\unsure{end|ed}}')
inv('46','deletion','Across the whole bottom-right marginal word','Several oblique cancellation strokes across end/ed')
inv('47','text','Bottom left, outside reference rule; archive number only','27, represented only by archive-number comment','another unnamed hand / archive numbering')
inventory.sort(key=lambda q:int(q['element']))

notes=[
'The sheet is an English-language correction list citing fifteen manuscript/typewritten-page references from p335 through p354. Those are references in the list, not pagination of this note sheet.',
'p.338 l-8 gives the tentative wording ? ``and even\'\' perhaps.; the question mark and qualification are retained.',
'p341 l.2 proposes ``and alongside got me back\'\' and explicitly says is perhaps better. The underline spans got me.',
'p350 l-10 prefers independent of while adding that from can also be used but is less usual. The parenthetical qualification continues onto the next physical line.',
'p351 l-11 gives the live inadequacies with an overwritten first a and an asymmetric quotation: two opening strokes and one closing stroke.',
'There is no visible title, date, stated total page count, authorial pagination, or mathematical display. The separate lower-left 27 is the archive sheet number and is included only as a comment.',
'The bottom-right word stands outside the right rule at the foot of the sheet and is wholly cancelled; end and ed remain possible.',
'Two long dark rules and a faint far-left trace are recorded in their relationship to the text and the large lower blank area. The faint trace has no sharp established original endpoints.'
]
notes[1]="p.338 l-8 gives the tentative wording ? ``and even'' perhaps.; the question mark and qualification are retained."
notes[2]="p341 l.2 proposes ``and alongside got me back'' and explicitly says is perhaps better. The underline spans got me."

notation=[
{'sign':r'l.-8','location':'342, second correction','reading':r'l.-8','evidence':'Crop 06 separates a low point from both the l foot and the minus.'},
{'sign':r'\uline{got me}','location':'p341 l.2','reading':r'\uline{got me}','evidence':'Upper half: one rule extends from the g through the e of me and stops before back.'},
{'sign':r'\unsure{\uuline{i}|\uline{i}}','location':'p350 l-10','reading':r'\unsure{\uuline{i}|\uline{i}}','evidence':'Crop 09: touching stacked pen passes; retraced single and double underline remain possible.'},
{'sign':'Opening and closing quotation strokes','location':'p.338 and even; p341 does not contraction; p.345 with; p350 from','reading':r'''``and even''; 'doesn't''; ``with''; (``from'' ''','evidence':'Crops 01, 05, 07, 10 independently inspected. The p341 opener is one curled high body; the other listed openers/closers have paired bodies, including the compact pair touching the parenthesis before from.'},
{'sign':"`` ... '",'location':'p351 l-11','reading':"``"+overlap,'evidence':'Crop 12: separate paired opening marks and one terminal high stroke.'},
{'sign':'l12','location':'p351 first reference','reading':'l12','evidence':'Crop 11: a full upright 1 separates the looped l from 2; there is no abbreviation point in that space.'},
{'sign':'Period after better','location':'p341 l.2','reading':'better.','evidence':'Crop 04 shows a compact slanted baseline body, without a separate descending comma tail.'},
{'sign':'Period after (again)','location':'p.345 l.7','reading':'(again).','evidence':'Crop 08 shows a short baseline protrusion immediately right of the parenthesis, joined to it; this is retained as C period. The lower isolated short stroke is a different mark.'},
{'sign':'Overlapping old/new a','location':'p351 l-11','reading':overlap,'evidence':'Crop 12 shows the older oval and the live a within one glyph space.'}
]

report={
'scan':28,'reader':'A','model':'GPT-6 Astra Pro','effort':'not exposed',
'viewed':[W,A,B],
'layout':'One handwritten correction list occupies the upper approximately 1135 of 2362 pixels. Fifteen page-reference groups contain twenty-nine correction/proposal loci, over seventeen physical writing lines. The p344 entries have a continuation line; the p350 parenthesis continues onto the following line. Page references stand left of a dark vertical rule and correction text stands mainly to its right. A second dark vertical rule near x1530 intersects several long right continuations. Both dark rules extend to the sheet foot. A much fainter far-left trace is visible with fading ends. The lower half is otherwise largely blank, with scattered isolated marks, an archive 27 at lower left, and a wholly cancelled word outside the right rule at lower right. No diagram, display, title or date is present. The main writing appears in one hand; the archive numeral is separately identified. Two pale round paper marks near the outer right edge are physical surface features, not read as lettering.',
'changes':changes,'c_doubts':c_doubts,'remaining_doubts':remaining,'inventory':inventory,
'notes':notes,'math_checks':[],
'notation':notation,
'abbreviations':[
{'form':'p / p.','expansion':'page (tentative expansion only)','place':'Left page-reference column; presence or absence of the stop retained separately'},
{'form':'l / l.','expansion':'line (tentative expansion only)','place':'Correction references throughout; stops and minus signs retained separately'}],
'brief_feedback':'The required visual sequence was followed: one whole-page display, one display of each full-resolution half, a frozen list of fifteen unresolved loci, and one generated/displayed enhanced crop per frozen locus. No additional crop, OCR, external source, other-page image, other-reader return, compilation, installation, or mathematical proof work was used. All four explicit C uncertainty macros and five page-specific context decisions are included. H is description-only, so every comparison has h=null and no H difference is claimed. The whole-page geometry is encoded with the text in one TikZ field to keep the rules, text crossings and extreme bottom-right note in place. The faint trace is entered by crop 14 and fades in crop 15; its original exact endpoints remain uncertain. Prominent isolated dark marks are drawn without assigning a function; minute grey paper/scan speckles and pale circular paper features are not interpreted as handwriting. Mathematical wording is limited to usage examples such as commutes with; there is no substantive mathematical proposition to test. Inventory covers all twenty-nine correction/proposal loci, the nested underline and correction states, three vertical traces/rules, retained isolated marks, the marginal note and its deletion, and the archive-number comment.'
}
(D/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

audit={
'scan':28,'reader':'A','inputs_read':['work/briefs/brief_v13.md','work/briefs/conventions.md','work/PREAMBLE.tex','work/inputs/028/C.tex','work/inputs/028/H.tex','work/inputs/028/C_context.md','work/inputs/028/metadata.json','work/inputs/028/notation.md'],
'original_displays':[{'path':p,'count':1} for p in [W,A,B]],
'frozen_list':'frozen_unresolved.json',
'crop_count':15,
'crop_displays':[{'id':q['id'],'path':crop(q['id']),'count':1,'rotate':0,'reason':q['question']} for q in F['loci']],
'crop_log':'crops/crops.jsonl',
'prohibited_actions_performed':[],
'counts':{'changes':len(changes),'c_doubts':len(c_doubts),'remaining_doubts':len(remaining),'inventory':len(inventory),'math_checks':0},
'confirmation_outcomes':[
{'crop':'01','outcome':'Two closing strokes after even; C confirmed.'},
{'crop':'02','outcome':'Whole sign cancelled; ampersand/l unresolved.'},
{'crop':'03','outcome':'Isolated marks retained geometrically; not inserted as punctuation.'},
{'crop':'04','outcome':'Compact baseline stop after better; C period retained.'},
{'crop':'05','outcome':'One curled opening body before does not contraction; C single retained.'},
{'crop':'06','outcome':'Distinct low point in l.-8; C changed.'},
{'crop':'07','outcome':'Two connected quotation bodies before with; C confirmed.'},
{'crop':'08','outcome':'Baseline stop touching parenthesis retained; separate lower mark recorded.'},
{'crop':'09','outcome':'Multiple touching underline passes; C double/retraced-single uncertainty retained.'},
{'crop':'10','outcome':'Two opening quotation bodies beside parenthesis, left one partly fused; C confirmed.'},
{'crop':'11','outcome':'Full-height numeral 1 before 2; l12 confirmed.'},
{'crop':'12','outcome':'Old a/o unresolved; overlap preserved. Single closer confirmed.'},
{'crop':'13','outcome':'Whole marginal word cancelled; end/ed unresolved. Letter baseline is roughly horizontal, though cancellation is oblique.'},
{'crop':'14','outcome':'Faint trace enters crop; exact original upper endpoint not established.'},
{'crop':'15','outcome':'Faint trace fades low on sheet; lower-left small marks also retained.'}
]
}
(D/'audit.json').write_text(json.dumps(audit,ensure_ascii=False,indent=2)+'\n')
print(json.dumps(audit['counts']))
