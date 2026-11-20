import json
from pathlib import Path

ROOT = Path('/workspace/scratch/6d55c8c3e5a7')
OUT = ROOT / 'work/readers/025/A'
BASE = ROOT / 'source/SP49_CW_109_scans'
SRC = {k: str(BASE / ('H109-02_109_scan025' + v + '.jpg')) for k, v in [('whole',''),('a','_a'),('b','_b')]}
frozen = json.loads((OUT / 'unresolved_before_crops.json').read_text())
LOC = {p['id']: p for p in frozen['loci']}

def ev(crop=None, source=None, bbox=None):
    if crop:
        q = LOC[crop]
        return {'crop': str(OUT/'crops'/('crop_'+crop+'.jpg')), 'source': SRC[q['source']], 'bbox': q['bbox']}
    return {'crop': None, 'source': SRC[source], 'bbox': bbox}

changes = []
def change(ident, place, c, reading, kind, confidence, evidence, crop=None, source=None, bbox=None, code_reference=None):
    row = dict(id=ident, place=place, c=c, h=None, reading=reading, diff_c=True, diff_h=False,
               kind=kind, marked_in_H=False, confidence=confidence, evidence=evidence, **ev(crop,source,bbox))
    if code_reference:
        row['code_reference'] = code_reference
    changes.append(row)

change('left-rule','Long rule between reference column and correction text','',
       r'\draw[line width=0.22pt] (232,112) -- (234,572) -- (238,1000) -- (242,1460) -- (247,2270);',
       'drawing or diagram','high','A thin near-vertical line starts below the first reference, separates the references from the correction text, and continues almost to the last entry. It is kept alongside the writing in the same TikZ layout.',source='whole',bbox=[225,102,254,2290],code_reference='reading.tex, drawing-left-rule')
change('right-rule','Long rule to the right of the correction list','',
       r'\draw[line width=0.28pt] (1508,94) -- (1511,595) -- (1514,1120) -- (1518,1690) -- (1524,2263);',
       'drawing or diagram','high','The second thin rule begins near first-line height and runs down the right side; the long p269 writing reaches across it. No editorial function is inferred.',source='whole',bbox=[1498,87,1533,2280],code_reference='reading.tex, drawing-right-rule')
change('far-left-trace','Faint far-left trace ending beside p245','',
       '\\draw[line width=0.15pt,opacity=0.35] (49,292) -- (50,685) -- (53,1065);\n\\fill (53,1069) ellipse [x radius=1.5,y radius=2.3];',
       'drawing or diagram','medium','The half shows a faint vertical trace well left of the reference column. The crop shows its dark terminal point. The geometry is reproduced, while its medium and purpose remain unassigned.',crop='28',code_reference='reading.tex, drawing-far-left-trace')
change('p234-opener','p.234 l.7, opener before surely',r'``surely',r"\unsure{``|'}surely",
       'misread symbol or index','medium','The high mark has a fused angular body and a return; unlike the independently separated strokes before Then, it does not securely establish one versus two quotation strokes.',crop='02')
change('p234-old-reference','Cancelled page reference beside l.-6',r'\deleted{p\unsure{23}}',r'\deleted{p23}',
       'readable ink left as \\ill{}','medium','Under the broad cancellation, the p descender, a 2 with a lower angled return, and the two rightward curves of 3 remain separable. No third numeral is supplied.',crop='04')
change('p243-not','p.243 l-6, after neither...',r'\unsure{not|nor}',r'not',
       'misread word','high','The final letter has a short upright crossed by a long rightward stroke. It is t, not the shoulder-shaped terminal r. The grammatical expectation nor is not used to rewrite it.',crop='09')
change('p245-angular-mark','After the page reference p245',r'p245.',
       '\\node at (114,1052) {p245};\n\\draw[line width=0.6pt] (229,1048) -- (229,1055) -- (232,1051) -- (235,1055);',
       'drawing or diagram','medium','The mark is a small two-legged angle at the left rule, not a securely identifiable round stop. Its visible shape is retained separately, without deciding whether its function was a stop or displaced quotation.',crop='10',code_reference='reading.tex, entry-14 and drawing-p245-mark')
change('p247-old-line','p.247, first cancelled reference',r'\unsure{l.14}',r'l.14',
       'readable ink left as \\ill{}','medium','The looped l, low point, narrow 1 and crossed/angular 4 survive between the cancellation diagonals. The deletion state itself is more certain than this medium-confidence recovery.',crop='11')
change('p247-upper-index','p.247, raised mapping index',r'i_{\unsure{0|i}}',r'i_0',
       'misread symbol or index','high','The raised proposal has a dotted main i and a separate closed low oval. The low oval is 0; it is not another dotted or upright i.',crop='12')
change('p247-lower-index','p.247, cancelled lower mapping index',r'$(i_0\colon N)$',r'$(i_{\unsure{0|i}}\colon N)$',
       'misread symbol or index','low','The lower index merges with the cancellation diagonals. A short low loop remains, but it does not securely discriminate 0 from a very small i; certainty from the clearer raised occurrence is not propagated here.',crop='13')
change('p247-also-placement','p.247, also and the curved marks beside l12',r'\inserted{also}',r'\inserted{also}',
       'insertion or placement','high','The word also is level with the following live l12 is aspheric correction, to the right of the descending curve; it is not physically before the upper l-9 standard entry. The curved marks are drawn in that location. Its exact logical attachment is left open.',crop='13',code_reference='reading.tex, entry-17 and drawing-p247-curves')
change('p247-insertion-arc','p.247, tall opening parenthesis of raised condition question',r'\inserted{(Cond\textsuperscript{n} (ii) should it be $i_{\unsure{0|i}}\colon N_0\to N$)}',
       '\\draw[line width=0.28pt] (535,1065) .. controls (522,1093) and (523,1119) .. (540,1141);\n\\node[rotate=5,font=\\tiny] at (559,1134) {\\inserted{Cond\\textsuperscript{n} (ii) should it be $i_0\\colon N_0\\to N$)}};',
       'insertion or placement','high','The opening parenthesis is a tall arc descending toward the cancelled line, while the raised wording slopes upward to the right. Its drawn arc replaces, rather than duplicates, a normal-height opening-parenthesis glyph. The index decision is separately recorded.',crop='12',code_reference='reading.tex, entry-16')
change('p248-opener','p248 l.-3, opener before handwritten',r'``\uline{handwritten}',r"\unsure{``|'}\uline{handwritten}",
       'misread symbol or index','medium','The opener is one compact oblique body with a short right return. A joined double opener and a single bent stroke remain possible; the underline is clear and unchanged.',crop='15')
change('p262-old-reference','262, cancelled earlier reference',r'\deleted{\unsure{-13}}',r'-\deleted{\unsure{13}}',
       'deletion state (struck given live or live given struck)','high','The short minus is to the left of, and untouched by, the diagonals that cancel the following digits. The old 13 remains uncertain under those diagonals, but the live state of the minus is clear.',crop='19')
change('p262-no-second-minus','262, live reference after ampersand',r'\& \unsure{-}2',r'\& 2',
       'text not on the page','high','Between the ampersand and 2 is white space. The upper arm and lower return belong to the ampersand; there is no independent horizontal minus there.',crop='19')
change('p263-terminal-letter','263 l.19, last letter of allow...',r'allow\unsure{s}',r'allow\unsure{e|s}',
       'misread word','low','A separate small loop follows the w. Its closed counter and exiting stroke look e-like, while a compact looped s remains possible. The expected phrase allows one to is not used to decide the ink.',crop='20')
change('p263-detached-marks','Below and to the right of pushing on the.','',
       '\\draw[line width=0.32pt] (1258,1799) -- (1265,1791);\n\\draw[line width=0.6pt] (1429,1773) -- (1436,1782);\n\\fill (1463,1819) ellipse [x radius=1.6,y radius=2.2];',
       'drawing or diagram','high','The crop separates three detached dark marks: a small up-right trace, a heavier down-right stroke, and a lower compact point. They are not supplied as quotation or sentence punctuation.',crop='21',code_reference='reading.tex, drawing-p263-detached-marks')
change('p264-single-mark','264, high mark immediately before l12',r"\unsure{'}l12",r"'l12",
       'misread symbol or index','high','One short vertical raised stroke stands separately to the left of the looped l. It is not two quotation strokes and is not part of the l.',crop='22')
change('p269-cancelled-contraction','p.269, opening contraction of cancelled question',r"isn't the use",r"\unsure{isn't|is'nt} the use",
       'misread word','low','The cancellation crosses the high area between n and t and the area before n. The letters are recoverable, but the original apostrophe position is not independently recoverable from the surviving strokes.',crop='25')
change('p269-not','p.269, second cancelled phrase',r'\unsure{not} $\pi_0,\pi_1$',r'not $\pi_0,\pi_1$',
       'readable ink left as \\ill{}','high','The initial n, closed o below the crossing, and separate t upright with its rightward crossbar survive the deletion. The word is not.',crop='26')
change('p273-point','Between p.273 and the following l-7','',
       r'\fill (280,2162) ellipse [x radius=1.3,y radius=1.6];',
       'drawing or diagram','high','A small dark point stands above the baseline between the reference and l. Its geometry is certain, but it is not confidently a sentence stop; it is represented once as a detached point.',crop='27',code_reference='reading.tex, drawing-p273-point')

c_doubts = []
def doubt(place, c, reading, resolved, confidence, evidence, crop=None, source=None, bbox=None):
    c_doubts.append(dict(place=place,c=c,reading=reading,resolved=resolved,confidence=confidence,evidence=evidence,**ev(crop,source,bbox)))

doubt('C_context: p.234 l.7, pair and comma',r'$(A,i)$',r'$(A,i)$',True,'high','The half shows an ordinary A, a low comma with tail, a dotted i and both round parentheses; no alternative sign is imposed.',source='a',bbox=[1287,361,1447,444])
doubt('C_context: p.240 l.3, double subscript, inverse and underline',r'$W=(i_{M,i})^{-1}(\underline{W})$',r'$W=(i_{M,i})^{-1}(\underline{W})$',True,'high','The half already separates lowered M, comma and i, raised -1, and the underline confined to the final W. Crop 08, inspected for the opener, retains that same formula in context.',crop='08')
doubt('C_context: p.247 raised Cond abbreviation',r'Cond\textsuperscript{n}',r'Cond\textsuperscript{n}',True,'high','An angular small n is raised immediately after d, before the parenthesized ii.',crop='12')
doubt('C explicit doubt and C_context: p.247 raised index',r'i_{\unsure{0|i}}\colon N_0\to N',r'i_0\colon N_0\to N',True,'high','The main i has its own high dot; its low companion is a closed oval. The N index is independently a rounded low 0, and the arrow has a right head.',crop='12')
doubt('C_context: p.247 cancelled lower low index',r'i_0\colon N',r'i_{\unsure{0|i}}\colon N',False,'low','The low mark merges with crossing strokes. The clearer raised formula does not settle this independent occurrence.',crop='13')
doubt('C_context: p248 hat over C',r'\widehat C',r'\widehat C',True,'high','Two short oblique roof strokes stand above a single open capital C and are separate from its body.',source='b',bbox=[851,151,920,219])
doubt('C_context: p269 first pi pair in cancelled question',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,'high','The first low digit is a closed oval; the second is a short upright. The comma remains between them below the crossing, and both pi bars are separately visible.',crop='25')
doubt('C_context: p269 second pi pair in cancelled fragment',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,'high','The enlarged cancelled pair independently shows the left low closed 0, a descending comma and the right low 1, despite the higher zigzag.',crop='26')
doubt('C_context: p269 live pi pair',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,'high','The live pair has two pi bars, a low closed 0, a comma and a low short 1; this was clear in the lower half without a new crop.',source='b',bbox=[627,928,765,993])
doubt('C explicit doubt: p234 cancelled quotation-like cluster',r"\deleted{\unsure{''}}",r"\deleted{\unsure{''}}",False,'low','The raised cluster has overlapping dark returns and tails. Its cancelled state is clear, but the original count and identity of the ticks cannot be securely recovered. Both low dot groups have three marks.',crop='03')
doubt('C explicit doubt: p234 cancelled page-reference digits',r'\deleted{p\unsure{23}}',r'\deleted{p23}',True,'medium','The p descender and two numeral shapes remain recoverable under the two cancellation strokes. The last numeral has the two curved portions of 3; no unobserved third digit is appended.',crop='04')
doubt('C explicit doubt: p234 cancelled if candidate',r'\deleted{\unsure{if}}',r'\deleted{\unsure{if}}',False,'low','The dense parallel overstrikes leave only a short inner stem and a low left tail. These permit if but do not establish it.',crop='05')
doubt('C explicit doubt and both C_context not/nor alternatives: p243',r'\unsure{not|nor}',r'not',True,'high','The final short upright is crossed by the long rightward stroke, deciding t. The note about negatives is preserved, including the qualification is one of many possibilities.',crop='09')
doubt('C explicit doubt: p247 cancelled l.14',r'\unsure{l.14}',r'l.14',True,'medium','The looped l, low point, narrow upright 1 and angular 4 with a transverse arm remain visible. The cancellation passes through all of the reference.',crop='11')
doubt('C explicit doubt: p247 cancelled aspheric',r'\unsure{aspheric}',r'\unsure{aspheric}',False,'low','Several word strokes survive between diagonals, including a descending central stem and a final low turn. The full old word cannot be recovered with certainty from those fragments; the live is aspheric below is not used to fill it in.',crop='11')
doubt('C explicit doubt: p247 cancelled lower terminal ticks',r"\deleted{should it be $(i_0\colon N)$\unsure{''}}",r"\deleted{should it be $(i_{\unsure{0|i}}\colon N)$\unsure{''}}",False,'low','The terminal high ticks lie within the cancellation turns. A paired closer remains a possible reading, but the number of original strokes is not secure. The uncertainty of the low index is separately recorded.',crop='13')
doubt('C explicit doubt: cancelled prefix before 255',r'\deleted{\unsure{2}}',r'\deleted{\unsure{2}}',False,'low','An upper curved stroke and a low foot permit 2; the overlaid diagonal and right upright prevent a secure recovery. The deletion extent is certain.',crop='18')
doubt('C explicit doubt: cancelled -13 after 262',r'\deleted{\unsure{-13}}',r'-\deleted{\unsure{13}}',False,'low','The minus is visibly live and outside the crossing. The following narrow upright and two lobes favour 13, but the cancellation still prevents a certain reading of the old digits.',crop='19')
doubt('C explicit doubt: minus before live 2 after ampersand',r'\& \unsure{-}2',r'\& 2',True,'high','There is no independent horizontal stroke between ampersand and 2. Removing the doubt also removes the unsupported minus.',crop='19')
doubt('C explicit doubt: terminal letter after allow at 263 l19',r'allow\unsure{s}',r'allow\unsure{e|s}',False,'low','The detached small loop has an e-like counter and right exit; an abbreviated looped s remains possible. Expected grammar is not used as stroke evidence.',crop='20')
doubt('C explicit doubt: isolated mark before 264 l12',r"\unsure{'}",r"'",True,'high','The crop separates exactly one raised vertical stroke from the left side of the looped l. Its function is not expanded into an opening quote for an invented phrase.',crop='22')
doubt('C explicit doubt: not before second cancelled pi pair',r'\unsure{not}',r'not',True,'high','A low closed o follows n and precedes a crossed t; all three survive the cancellation sufficiently to read not.',crop='26')
doubt('C_context: p234 l-6 second live variable',r'$u$',r'$u$',True,'high','The glyph is open at the top, with two uprights and a low curved joining stroke. It is u; no closed a bowl is present.',crop='05')

remaining = [
    dict(place='p234 l7 first opener',reading=r"\unsure{``|'}",alternatives="double opening ticks | single bent opening tick",confidence='medium',reason='Fused angular body does not separate the count after its one crop.'),
    dict(place='p234 l7 cancelled high cluster',reading=r"\deleted{\unsure{''}}",alternatives="paired closing ticks are possible; original identity/count remains hidden",confidence='low',reason='Dense overstrike buries the original strokes.'),
    dict(place='p234 l-6 cancelled word before iff',reading=r'\deleted{\unsure{if}}',alternatives='if remains a candidate; no additional whole word securely recoverable',confidence='low',reason='Only a short inner stem and a low tail survive the overstrikes.'),
    dict(place='p245 mark following the page number',reading=r'\draw[line width=0.6pt] (229,1048) -- (229,1055) -- (232,1051) -- (235,1055);',alternatives='stop-like mark | displaced joined ticks | unassigned pen mark',confidence='medium',reason='The geometry is a small two-legged angle; punctuation function is not settled.'),
    dict(place='p247 cancelled word',reading=r'\unsure{aspheric}',alternatives='aspheric remains the candidate',confidence='low',reason='The crossing obscures too many independent letter strokes; the next-line repetition is not proof.'),
    dict(place='p247 cancelled lower mapping index',reading=r'i_{\unsure{0|i}}',alternatives='0 | i',confidence='low',reason='The low mark intersects the cancellation and must remain independent of the clear raised index.'),
    dict(place='p247 cancelled lower terminal ticks',reading=r"\unsure{''}",alternatives='paired closing ticks remain possible; count is not recoverable',confidence='low',reason='The terminal crossing passes through the tick group.'),
    dict(place='p247 also attachment',reading=r'\inserted{also}',alternatives='a qualification beside l12 is aspheric | a continuation of the revised condition comment',confidence='medium',reason='Physical placement on the lower line is clear, but the descending curve does not uniquely fix the logical attachment.'),
    dict(place='p248 opener',reading=r"\unsure{``|'}",alternatives='double joined opening ticks | single bent tick',confidence='medium',reason='The compact oblique body and short return cannot securely be counted.'),
    dict(place='Cancelled prefix before 255',reading=r'\deleted{\unsure{2}}',alternatives='2 remains the candidate',confidence='low',reason='Crossing strokes partly merge with the candidate numeral.'),
    dict(place='262 cancelled old digits',reading=r'-\deleted{\unsure{13}}',alternatives='13 remains the candidate; minus state is settled',confidence='low',reason='The interior digits are crowded by the cancellation.'),
    dict(place='263 terminal letter after allow',reading=r'allow\unsure{e|s}',alternatives='e | s',confidence='low',reason='A small closed loop and exit suggest e, but a compact s remains possible.'),
    dict(place='p269 cancelled contraction',reading=r"\unsure{isn't|is'nt}",alternatives="isn't | is'nt",confidence='low',reason='The overstrike prevents recovery of the apostrophe position.'),
    dict(place='Far-left faint vertical trace',reading=r'\draw[line width=0.15pt,opacity=0.35] (49,292) -- (50,685) -- (53,1065);',alternatives='drawn trace | paper-related trace',confidence='medium',reason='Its geometry and terminal point are visible; this inspection does not settle its medium or purpose.')
]

inventory = []
def inv(kind, position, words, hand='his hand'):
    inventory.append(dict(sheet_kind='list',hand=hand,element=f'{len(inventory)+1:02d}',kind=kind,position=position,first_words_or_objects=words.replace("\\'", "'"),transcribed='yes'))

# Each line-reference entry gets its own row, even when several share a physical line.
text_items = [
('p225, line12','delete ``that\'\''),('p225, l.-7',"don't"),('226 l.2','``do not\'\''),('230 l.-2',"'informal''"),('p232 l-3','``inessential\'\''),
('p.233 l.1','``its\'\''),('p.233 l2 & 3',"``shouldn't''"),('p.233 l-2','``synonym\'\''),
('p.234 l.7','surely it should be ``Then W is a mildly ... of (A,i)\'\''),
('p.234 l.-6, two physical lines','``x is aspheric ... iff u is aspheric\'\' I suppose! A tautology it surely is as it stands!.'),
('p.239 l.3','``suggests that we call an ...\'\''),
('p.240 l.3',r'W=(i_{M,i})^{-1}(\underline{W})'),('p.240 l.10','``its\'\''),('p.240 l-8',"``doesn't''"),
('p241 l-15','``suggested a long time ago\'\''),('p242 l-12','``its\'\''),('p242 l-2','``its\'\''),
('p.243 l-6, two physical lines','too many negatives: ``We assume beforehand neither... not....\'\' is one of many possibilities'),
('p244 l-15',"``doesn't''"),('p245 l.4',"``we'll''"),('p246 l.2','``its\'\''),
('p.247 first cancelled reference and word','l.14 ``aspheric\'\''),('p.247 lower cancelled proposal',r'should it be (i_0:N)'),
('p.247 l-9','``standard\'\''),('p.247 l12 on following line','``is aspheric\'\''),('p.247 l-2 on following line',"``didn't''"),
('p248 l.-3','``handwritten: such that C-hat is totally ...'),('p249 l-2',"``isn't''"),
('p.250 l.10','``developed\'\''),('p.250 l.12','``its\'\''),('p.250 l.13','``its\'\''),
('p251 l.9','``last but not least\'\''),('p251 l.15',r'``i:A\to M\'\'.'),
('255 l16','``developed\'\''),('260 l.13',"``didn't''"),('262 l-3 & 2','``may as well\'\''),
('263 l.19',r'``allow\unsure{e|s} one to\'\''),('263 l20',"'wasn't''"),('263 l.-13','``pushing on the.'),
('263 l-11','``and was finally\'\''),('263 l.-4','``developing\'\''),('264 l12','``developed\'\''),('264 same line, second quoted word','``length\'\''),
('p267 l.2','``developed\'\''),('p267 l-2','``amounts to it being contractible\'\''),
('p.269 middle of page, cancelled first line',"isn't the use of pi0, pi1 slightly confusing here!"),
('p.269 second line, cancelled first fragment','not pi0, pi1'),('p.269 second line, live continuation','pi0, pi1 are undefined here. Notation is confusing.'),
('p.270 l.-2',"``we've got''"),('p.273 l-7',"``isn't''"),('p.274 l-9',"``if I've got''")]
for pos, words in text_items: inv('text',pos,words)

for pos, words in [
('p234 l7, high cluster between low dot groups',r"\unsure{''}"),
('p234 l-6, reference column','p23'),('p234 l-6, before iff',r'\unsure{if}'),
('p247 first cancelled entry',r'l.14 ``\unsure{aspheric}\'\''),
('p247 lower proposal',r"should it be (i_{\unsure{0|i}}:N)\unsure{''}"),
('before 255',r'\unsure{2}'),('after 262, only the digits; preceding minus stays live',r'\unsure{13}'),
('p269 first question',r"\unsure{isn't|is'nt} the use of pi0,pi1 slightly confusing here!"),
('p269 second line, first fragment','not pi0,pi1')]: inv('deletion',pos,words)

for pos, words in [
('p247 raised slanting line above the cancelled proposal',r'Cond\textsuperscript{n} (ii) should it be i_0:N_0\to N'),
('p247 lower live line, right of the descending curve','also'),
('p267 l-2, above the gap between to and being','it')]: inv('insertion',pos,words)

for pos, words in [('p248 l.-3','handwritten, single underline'),('p248 l.-3','is, single underline'),('p269 live sentence','here, single underline')]: inv('text',pos,words)

for pos, words in [
('between reference column and correction text, nearly full height','thin left vertical rule'),
('right of the correction list, nearly full height','thin right vertical rule'),
('far left, upper half','faint vertical trace'),('far left, at p245 level','dark terminal point on faint trace'),
('after page number p245','small two-legged angular mark'),
('p247, left of raised Cond line','tall opening-parenthesis arc'),
('p247, from cancelled lower proposal down beside is aspheric','descending curved mark'),
('p247, below the lower opening parenthesis','oblique descending continuation'),
('below 263 pushing on the., farther left','small up-right detached trace'),
('below 263 pushing on the., farther right','heavier down-right detached trace'),
('to the right of 263 developing line','compact isolated point'),
('between p.273 and l-7, above baseline','small isolated point')]: inv('drawing',pos,words)
inv('margin note','lower-left corner, archive number retained only as a TeX comment','24','another unnamed hand, pale pencil-like numeral')

checks = []
truth_table = [{'P':p,'Q':q,'P_iff_Q':p==q} for p in [False,True] for q in [False,True]]
(OUT/'math_check.json').write_text(json.dumps({'statement_id':'S025-tautology-scope','formalization':'P = x is aspheric; Q = u is aspheric; treat P and Q as independent Boolean inputs for this limited check','truth_table':truth_table,'limits':'This tests only the bare biconditional with independent predicates. The referenced typescript and definitions linking x and u are not supplied. It neither proves nor refutes the source theorem or the author\'s context-dependent comment.'},indent=2)+'\n')
checks.append(dict(statement_id='S025-tautology-scope',type='computation or formal certificate',outcome='I evaluated the four Boolean assignments for P iff Q, with P denoting x is aspheric and Q denoting u is aspheric. It is false at (false,true) and (true,false); a bare equivalence between independent predicates is therefore not a tautology. This is a scope check only: the page is a correction note and supplies no definitions linking x and u, so the result does not refute the referenced statement or the author\'s contextual comment. The ink still reads x, u, and A tautology it surely is as it stands!. The four rows are in math_check.json.'))

notation = [
dict(sign='ordinary mathematical capitals',location='p234, p240, p247, p248, p251',reading=r'W; (A,i); i_{M,i}; N_0\to N; \widehat C; i:A\to M',evidence='The manuscript is wholly handwritten. Each capital has an ordinary single outline; the two Ns and their low indices are separately visible in crop12. No script or double-struck alphabet is supplied.'),
dict(sign='u',location='p234 l-6, second predicate',reading='u',evidence='Crop05 shows an open top, two short uprights and a low joining curve, not a closed a.'),
dict(sign='double subscript and inverse image',location='p240 l3',reading=r'W=(i_{M,i})^{-1}(\underline{W})',evidence='Half a and crop08 separate the comma in the subscript, the superscript minus and 1, and the final W underline.'),
dict(sign='raised n and mapping indices',location='p247 raised condition question',reading=r'Cond\textsuperscript{n}; i_0\colon N_0\to N',evidence='Crop12 shows raised n after d, a dotted main i with a low closed 0, a separate low rounded 0 at N, a two-point colon and a right-headed arrow.'),
dict(sign='cancelled index',location='p247 lower proposal',reading=r'i_{\unsure{0|i}}',evidence='Crop13 leaves the low companion merged with cancellation; this occurrence remains independently uncertain.'),
dict(sign='hat',location='p248 l.-3',reading=r'\widehat C',evidence='Lower half: two short roof strokes stand above the ordinary C.'),
dict(sign='pi with low digits',location='p269 all three pairs',reading=r'\pi_0,\pi_1',evidence='Crops25 and26 independently confirm the cancelled pairs; the lower half confirms the live pair. Each left digit is an oval and each right digit is a short upright.'),
dict(sign='quotation groups',location='p232, p234, p240, p247, p248, p250, p264, p273',reading=r"p232 ''; p234 \unsure{``|'} before surely and `` before Then; p240 ``; p247 ``standard''; p248 \unsure{``|'}; p250 ``its''; p264 'l12 and ``developed'' ``length''; p273 ``isn't''",evidence='The independent edge decisions are recorded in crop_decisions.json; fused groups are not regularized merely because other entries use double quotes.'),
dict(sign='not',location='p243 l-6',reading='neither... not....',evidence='Crop09 shows the final upright/cross stroke of t and three low marks after neither, four after not, the last lying beyond the right rule.'),
dict(sign='live minus outside deletion',location='262 old reference',reading=r'-\deleted{\unsure{13}}',evidence='Crop19 places the short minus wholly left of the cancellation; there is no independent minus between the later ampersand and 2.'),
dict(sign='terminal low dot groups',location='p234, p239, p248',reading='... in each visible group',evidence='Crops03,07,16 show three separate low groups at each location. Some individual marks are elongated rather than circular; no additional close quote is supplied at p248.'),
dict(sign='terminal punctuation',location='p234 last continuation',reading='stands!.',evidence='Crop06 separates an independent exclamation stem and dot from the f descenders above, and shows a further low terminal point to its right.')
]

report = dict(scan=25,reader='A',model='GPT-6 Astra Pro',effort='not exposed',
viewed=frozen['viewed'],
layout='One handwritten correction-list sheet, in one principal hand, with page references in a narrow left column and line references plus quoted wording to their right. There are 31 main row groups, several containing multiple correction entries. A thin rule separates the reference column from the text and another runs down the right side; both stay beside the writing in reading.tex. A faint far-left trace has a dark endpoint. The p234 and p243 notes run onto indented continuations. The p247 region has two cancellations, a raised upward-slanting parenthetical condition question, the lower live is aspheric entry, also beside a descending curve, and a further oblique stroke from the lower parenthesis. There are underlines at handwritten and is in p248 and here in p269. The inserted it is above the to/being gap in p267. At p269 a cancelled question is followed by a cancelled short fragment and a live sentence. Detached small marks are retained near p245, p263 and p273. The pale archive 24 is only a comment. Two edge punch-hole outlines and paper folds are physical features, not transcribed language. No title, date, stated page count, author pagination, formal commutative diagram, or separate marginal prose note is present.',
changes=changes,c_doubts=c_doubts,remaining_doubts=remaining,inventory=inventory,
notes=[
'The list cites typescript pages 225 through 274; it does not state a number of pages or supply a title or date. The pale 24 at the bottom left is the archive number.',
'At p234 l7, surely it should be introduces the proposed wording about W being a mildly ... of (A,i). The following l-6 correction reads x is aspheric [cancelled candidate if] iff u is aspheric, then I suppose! A tautology it surely is as it stands!. Both emphatic qualifications and the final !. are preserved.',
'At p240 l3, the written correction is W=(i_{M,i})^{-1}(underlined W). At p243 l-6 the words too many negatives introduce We assume beforehand neither... not...., expressly qualified on the next line as is one of many possibilities; the visible not is preserved.',
'The p247 raised question is Cond raised n (ii) should it be i_0:N_0 to N. A shorter should it be mapping beneath is cancelled. The lower live correction is is aspheric, with also physically beside it. No question mark is supplied where none is securely visible.',
'At p248 l.-3, handwritten and is are underlined in such that C-hat is totally ...; the opening quote has no supplied closing counterpart. At p251 l15 the map is i:A to M.',
'At p267 l-2, it is inserted between to and being in amounts to it being contractible. At p269 the cancelled question calls use of pi0,pi1 slightly confusing here!; the live text says pi0,pi1 are undefined here. Notation is confusing. Here alone is underlined.',
'The page consists of proposed corrections and comments, not self-contained proofs. The limited truth-table check does not validate the referenced mathematics or add assumptions to the transcription.'
],math_checks=checks,notation=notation,
abbreviations=[dict(form='p / p.',expansion='page (interpretation only)',place='reference column throughout'),dict(form='l / l.',expansion='line (interpretation only)',place='line-reference entries throughout'),dict(form=r'Cond\textsuperscript{n}',expansion='Condition (tentative expansion only)',place='p247 raised line'),dict(form='iff',expansion='if and only if (interpretation only)',place='p234 l.-6')],
brief_feedback='The supplied files were all read. H has description status only, so every change has h=null, diff_h=false and marked_in_H=false; no comparison is manufactured from its description. The whole and two halves were each displayed once. The 28 unresolved loci were frozen before cropping in unresolved_before_crops.json; crop.py generated exactly one enhanced crop per locus and all 28 were displayed once. crops/crops.jsonl records source boxes and processing, and crop_decisions.json records the resulting decisions. The inventory covers every correction entry, each cancellation and insertion, three underlines, all reproduced drawing/mark elements and the comment-only archive number. No other-page image, other reader output, OCR, outside research, compilation or package installation was used. The full-page local TikZ layout is needed to keep the long rules and crowded p247 curves in their physical relation to the text. The small p245 mark and faint far-left trace are geometrically preserved without forcing a functional interpretation.')

(OUT/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

decisions = [
('01','Double closer retained','The high final group has a vertical portion and a shorter oblique portion joined near their tops; no text change.'),
('02','First opener remains double/single uncertain; Then opener is double','The surely opener is fused; two strokes are separately visible before Then.'),
('03','Cancelled ticks retained doubtful; both dot groups counted as three','The blotted high cluster cannot be securely recovered; the low groups are separately spaced, with some elongated marks.'),
('04','Cancelled p23 recovered at medium confidence','The surviving p, 2 and 3 contours decide two digits without a supplied third numeral.'),
('05','Cancelled if retained doubtful; second live variable confirmed u','The old word remains under horizontal overstrikes; the live letter is open above its low joining curve.'),
('06','stands!. confirmed','Independent exclamation stem and dot followed by a further low point; the stem is distinct from the f descenders above.'),
('07','Three low dots retained after an','Three discrete short low marks precede the two closing ticks.'),
('08','Double opener and complete C formula confirmed','Two short legs join at the opener; the lowered M, comma and i, superscript -1 and final W underline are separately visible.'),
('09','not resolved; three/four dot counts confirmed','The last upright is crossed like t. The fourth final point lies beyond the right vertical rule.'),
('10','Small angular mark drawn; punctuation function open','The mark after 245 is a joined two-legged angle and cannot securely be a round stop.'),
('11','l.14 recovered at medium confidence; aspheric retained doubtful','The reference strokes survive; the word remains buried between zigzags. Cancellation scope includes the quote-edge crossings.'),
('12','Cond raised n and raised i_0:N_0 to N confirmed','The i index is a closed low oval, not another i. The tall left opening parenthesis and slanting position are preserved.'),
('13','Lower index and terminal ticks remain doubtful; also moved to its lower physical line','The low index merges with cancellation. Also stands beside the lower is aspheric line, right of the descending curve; its exact semantic attachment remains open.'),
('14','Double opener before standard and semicolon retained','The two high opener strokes are separate; the low s beginning is not a third quotation mark.'),
('15','l.-3 and underline confirmed; opener remains double/single uncertain','The low reference point is clear, but the raised opener is a compact fused shape.'),
('16','Three low marks and absent closer retained','The first two ellipsis marks are elongated and the last compact; there is no secure closing quote.'),
('17','Double opener before last its confirmed','A larger left curved stroke and a small separate right mark are present.'),
('18','Cancelled 2 retained doubtful','Upper curved remnant and low foot favour 2, but cancellation prevents recovery with certainty.'),
('19','Minus before old digits is live; old 13 retained doubtful; no minus before live 2','The first short dash is untouched; the later space after ampersand has no independent dash.'),
('20','Final letter e/s unresolved, e placed first','The small independent loop has an e-like counter and exit; compact s is possible.'),
('21','Three detached ink marks reproduced geometrically','Two slanted strokes and one lower compact point remain separate from text and are not assigned punctuation roles.'),
('22','Single raised stroke before l12 resolved','One short upright is separate from the looped l.'),
('23','Quote groups around developed and length confirmed','The closer and next opener have two strokes each, separate from the f descender; final length closer is a joined two-legged form.'),
('24','l-2 confirmed','A clear short horizontal follows l, without a separate abbreviation point.'),
('25','First pi pair confirmed; contraction apostrophe position newly uncertain','The low 0, comma and 1 survive, while the upper cancellation buries the internal apostrophe location; terminal exclamation is crossed.'),
('26','not resolved; second pi pair confirmed independently','The n, closed o, and t upright/crossbar survive; low indices and comma remain visible.'),
('27','Raised point added geometrically; double opener retained','The separate point is above the reference baseline; the opener before isn\'t has two joined lower legs.'),
('28','Faint trace and dark endpoint reproduced; medium/purpose open','The crop preserves a narrow pale continuation ending in one dark point. The whole/half view establishes its longer vertical course.')]
(OUT/'crop_decisions.json').write_text(json.dumps([dict(id=k,displayed=True,display_count=1,decision=d,evidence=e,**ev(k)) for k,d,e in decisions],ensure_ascii=False,indent=2)+'\n')

print(json.dumps({'changes':len(changes),'c_doubts':len(c_doubts),'c_doubts_resolved':sum(d['resolved'] for d in c_doubts),'remaining_doubts':len(remaining),'inventory_rows':len(inventory),'math_checks':len(checks),'crops':len(decisions)},indent=2))
