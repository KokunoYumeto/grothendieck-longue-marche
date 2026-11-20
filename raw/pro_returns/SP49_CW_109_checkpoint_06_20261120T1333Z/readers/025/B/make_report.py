from pathlib import Path
import json,re
D=Path('work/readers/025/B')
A='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-02_109_scan025_a.jpg'
B='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-02_109_scan025_b.jpg'
W='/workspace/scratch/6d55c8c3e5a7/source/SP49_CW_109_scans/H109-02_109_scan025.jpg'
plan=json.loads((D/'unresolved_frozen.json').read_text())
loci={r['id']:r for r in plan['unresolved_loci']}
tex=(D/'reading.tex').read_text()

def loc(crop=None,source=None,bbox=None):
    if crop:
        p=loci[crop]
        return {'crop':str(D/'crops'/f'{crop}.jpg'),'source':p['source'],'bbox':p['bbox']}
    return {'crop':None,'source':source,'bbox':bbox}

def code(tag):
    return tex.split('% BEGIN '+tag+'\n',1)[1].split('% END '+tag,1)[0].rstrip()

changes=[]
def change(id,place,c,reading,kind,confidence,evidence,crop=None,source=None,bbox=None):
    changes.append(dict(id=id,place=place,c=c,h=None,reading=reading,diff_c=True,diff_h=False,kind=kind,marked_in_H=False,confidence=confidence,evidence=evidence,**loc(crop,source,bbox)))

change('p234-opener','p.234 l.7, before surely',"``surely",r"\unsure{``|`}surely",'misread symbol or index','medium','The single dark upper cluster has a short left leg and a longer bent right portion. A fused double opener is favoured, but a single bent stroke cannot be excluded.','03')
change('p234-cancel-ref','cancelled reference beside l.-6',r'\deleted{p\unsure{23}}',r'\deleted{p23}','misread symbol or index','medium','Under the two cancellation strokes the 2 retains its descending diagonal and low return, and the 3 retains its upper and lower turns. No additional digit is supplied.','05')
change('p243-not','p.243 l-6, after neither...',r'\unsure{not|nor}','not','misread symbol or index','high','The final letter has an upright and a long rightward cross stroke with an upturned tip. It is t, not an r shoulder; the preceding n and closed o are distinct.','07')
change('p247-old-reference','p.247 cancelled first line reference',r'\unsure{l.14}','l.14','misread symbol or index','medium','The surviving looped l, separate point, narrow 1, and crossed/angular 4 remain traceable under the zigzag. The cancellation state is certain independently of the following word.','08')
change('p247-raised-index','p.247 raised condition line, first mapping index',r'i_{\unsure{0|i}}\colon N_0\to N',r'i_0\colon N_0\to N','misread symbol or index','high','The upper i has its own high dot; its low companion is a closed small oval. This excludes the proposed separate low i. The N index is a second round low character and the arrow has a right head.','09')
change('p247-old-index','p.247 cancelled should-it-be mapping',r'$(i_0\colon N)$',r'$(i_{\unsure{0}}\colon N)$','misread symbol or index','low','The old low stroke lies inside the dense diagonal cancellation and cannot be independently resolved as 0. The clear raised replacement is not used to supply the buried index.','10')
change('p247-also-position','p.247 lower interline, to the right of l12 is aspheric',r"\inserted{also}; l-9 ``standard''\n\nl12 ``is aspheric''",r"\node at (934,1141) {; l-9 ``standard''};\n\node at (291,1208) {l12 ``is aspheric''};\n\node[font=\tiny] at (665,1208) {\inserted{also}};",'insertion or placement','high','Also is below the cancelled should-it-be line, beside a descending curved connector and to the right of the l12 quotation. The semicolon and l-9 remain on the higher main line. The anchored nodes preserve the physical placement without assigning also to a new mathematical assertion.','10')
change('p248-opener','p248 l.-3, before handwritten',r'``\uline{handwritten}',r'\unsure{``|`}\uline{handwritten}','misread symbol or index','medium','The high mark is a compact joined bent patch with a short right projection. Its two-stroke interpretation is plausible, but the single connected contour does not securely separate one from two quote strokes.','11')
change('p250-l13-opener','p.250 l.13, before its',"l.13 ``its''",r"l.13 \unsure{``|`}its''",'misread symbol or index','medium','Above the independent i dot there is a bent left quote-like stroke and a small attached right lobe. They may be a fused double opener or one heavy single opener. The two closing strokes are distinct.','13')
change('p255-old-digit','before 255 l16',r'\deleted{\unsure{2}}',r'\deleted{2}','misread symbol or index','high','The abandoned digit retains a curved head, diagonal descent and flat low return; a separate diagonal crosses it. These are sufficient for 2 despite the overstrike.','14')
change('p262-old-reference','262, short dash and cancelled old reference',r'\deleted{\unsure{-13}}',r'-\deleted{\unsure{13}}','deletion state (struck given live or live given struck)','medium','The short dash to the left is isolated from the cancellation strokes and remains live. The following tall stroke and two-lobed form permit 13, but their interiors remain crossed and are not made certain.','15')
change('p262-no-minus','262, live conjunction between -3 and 2',r'\& \unsure{-}2',r'\& 2','misread symbol or index','high','The only intervening short stroke is the low return of the ampersand. There is a gap before the 2 and no independent minus at the reference baseline.','15')
change('p263-final-letter','263 l.19, after allow',r'allow\unsure{s}',r'allow\unsure{e|s}','misread symbol or index','medium','A small separate loop with a light rightward exit follows w. It looks more like e than s in this crop, while the dense lower stroke leaves s possible. Grammar is not used to make allows certain.','16')
change('p264-raised-stroke','264, immediately before l12',r"\unsure{'}l12","'l12",'misread symbol or index','high','There is one detached raised curved vertical, separated from the looped l. It is represented by one apostrophe-shaped stroke; no quotation function is inferred from its position.','17')
change('p269-old-not','p.269 second cancelled fragment',r'\deleted{\unsure{not} $\pi_0,\pi_1$}',r'\deleted{not $\pi_0,\pi_1$}','misread word','medium','The n arch, low o loop, and the tall t with a rightward cross stroke can be followed beneath the crossing. The cancellation also covers the adjacent pi pair.','20')
change('left-rule','left reference/body boundary, almost full sheet height','',code('left_rule'),'drawing or diagram','high','A thin almost vertical ink rule passes immediately to the right of the reference numbers, from the top entries to the last entry. It is drawn beside the corresponding text, not in a separate geometry panel.',source=W,bbox=[219,82,259,2280])
change('right-rule','right side, almost full sheet height','',code('right_rule'),'drawing or diagram','high','A second thin almost vertical ink rule runs down the right side, crossing the ends of the long notes at their actual levels. Its slight rightward drift is retained.',source=W,bbox=[1497,82,1535,2255])
change('p247-connectors','p.247, below the cancelled mapping and beside also','',code('p247_connectors'),'drawing or diagram','high','One curved continuation descends from the left part of the cancellation to the left of also; a second long oblique continuation falls below the old mapping. These visible extensions are retained at that text block.','10')
change('p263-marks','below/right of 263 pushing on the. and to the right of developing','',code('p263_marks'),'drawing or diagram','high','Three separated short dark marks are visible: one small rising oblique, one descending oblique farther right, and one short near-vertical mark lower down. No punctuation function is assigned.',source=B,bbox=[1250,660,1475,729])
change('p269-margin-marks','right of the long rule at p.269 level','',code('p269_marks'),'drawing or diagram','medium','Two small detached points and a short nearly horizontal stroke occur to the right of the long rule. They are reproduced geometrically without incorporating them into the sentence punctuation.',source=B,bbox=[1530,906,1558,940])
change('p273-point','p.273, between reference and l-7','',code('p273_point'),'drawing or diagram','high','The crop shows a detached high point after 273, well above the reference baseline. Its position does not establish a full-stop function, so it is drawn once as a point.','21')

cd=[]
def doubt(place,c,reading,resolved,confidence,evidence,crop=None,source=None,bbox=None):
    cd.append(dict(place=place,c=c,reading=reading,resolved=resolved,confidence=confidence,evidence=evidence,**loc(crop,source,bbox)))

doubt('p.234 l.7 cancelled high group between the dot groups',r"\deleted{\unsure{''}}",r"\deleted{\unsure{''}}",False,'low','The group is certainly overmarked, but its small surviving upper stubs and lower diagonal do not settle the original quotation strokes. The first ellipsis has three marks; the second has one broad wavy mark and two separate low points.','04')
doubt('cancelled page reference before l.-6',r'\deleted{p\unsure{23}}',r'\deleted{p23}',True,'medium','The residual shapes decide 23; neither an extra final digit nor a new page number is inferred.','05')
doubt('p.234 l.-6 cancelled word before iff',r'\deleted{\unsure{if}}',r'\deleted{\unsure{if}}',False,'low','The heavy crossing leaves two narrow horizontal openings and a low trace, but no securely separable old f ascender. If remains only a tentative reading of the obliterated short item; the nearby live iff does not resolve it.','06')
doubt('p.243 l-6 not/nor, including repeated C_context alternative',r'\unsure{not|nor}','not',True,'high','A clear crossed t ends the word. The expected neither/nor construction is rejected as an ink correction.','07')
doubt('p.247 cancelled reference',r'\unsure{l.14}','l.14',True,'medium','The l, stop, 1 and angular 4 survive the zigzag separately.','08')
doubt('p.247 cancelled quoted word',r'\unsure{aspheric}',r'\unsure{aspheric}',False,'low','The word is covered by repeated diagonal loops. Several low curves and a descender are compatible with aspheric, but its letters cannot be recovered independently. The later live occurrence is not used as proof.','08')
doubt('p.247 raised i index and N index',r'i_{\unsure{0|i}}\colon N_0\to N',r'i_0\colon N_0\to N',True,'high','The low companion of dotted i is an oval, not a second dotted upright. N has another rounded low zero; the colon is two points and the arrow has a right head.','09')
doubt('p.247 cancelled trailing quotation',r"\unsure{''}",r"\unsure{''}",False,'low','The last high short strokes merge with the terminal zigzag. A closing quote pair remains possible, but its count and original contour cannot be established.','10')
doubt('255 cancelled initial digit',r'\deleted{\unsure{2}}',r'\deleted{2}',True,'high','The upper curve, diagonal and low horizontal foot identify the digit despite the independent crossing.','14')
doubt('262 cancelled old reference and preceding dash',r'\deleted{\unsure{-13}}',r'-\deleted{\unsure{13}}',False,'medium','The dash is clear and outside the crossing. The crossed remainder favours 13, with uncertainty retained for the buried forms. This is a scope correction, not a full resolution of the old reference.','15')
doubt('262 possible minus before 2',r'\unsure{-}','',True,'high','No independent minus is present. The short low stroke belongs to the ampersand return and does not extend into the gap before 2.','15')
doubt('263 final letter of allow...',r'\unsure{s}',r'\unsure{e|s}',False,'medium','The small loop and fine exit favour e, while a cramped s remains possible. The text is not silently normalised to grammatical allows.','16')
doubt('264 high mark before l12',r"\unsure{'}","'",True,'high','One separate raised curved stroke is clear. Its geometric identity is preserved without an interpretation of why it precedes the reference.','17')
doubt('p.269 cancelled not',r'\unsure{not}','not',True,'medium','The lower word retains an n arch, o loop and t upright/crossbar. Its cancellation is certain.','20')
# Explicit decisions on the page-specific C_context notation proposals.
doubt('C_context: p.234 final pair and comma',r'(A,i)',r'(A,i)',True,'high','The upper half shows an ordinary A, a low comma and a separately dotted i within round parentheses.',source=A,bbox=[1291,360,1462,456])
doubt('C_context: p.240 inverse-image formula',r'W=(i_{M,i})^{-1}(\underline W)',r'W=(i_{M,i})^{-1}(\underline{W})',True,'high','The half independently shows M and a comma/i as low companions of the main dotted i, a raised minus and 1, and a single underline under the final W only. The W capitals are single ordinary contours.',source=A,bbox=[389,626,765,707])
doubt('C_context: raised Cond abbreviation',r'Cond\textsuperscript{n}',r'Cond\textsuperscript{n}',True,'high','A small raised n sits above/right of d, followed by the parenthesised ii.','09')
doubt('C_context: buried low index in cancelled p.247 mapping',r'i_0',r'i_{\unsure{0}}',False,'low','The old index merges with the diagonal cancellation and is independently doubtful even though the upper replacement has a clear zero.','10')
doubt('C_context: p248 hat on C',r'\widehat C',r'\widehat C',True,'high','Two oblique roof strokes sit above and apart from an ordinary open C; neither roof stroke is part of the C body.',source=B,bbox=[864,149,908,205])
doubt('C_context: p269 first cancelled pi pair',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,'high','The first lowered character is a round loop and the second a short upright. The cancellation crosses the pi bodies, not the visible low index shapes.','19')
doubt('C_context: p269 second cancelled pi pair',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,'high','The first low character has a closed oval; the second has a single descending contour. A low comma separates them.','20')
doubt('C_context: p269 live pi pair',r'\pi_0,\pi_1',r'\pi_0,\pi_1',True,'high','The lower half shows a circular low 0 after the first pi and a single low 1 after the second, with a separate comma.',source=B,bbox=[627,924,759,981])

remaining=[
 {'place':'p.234 opener before surely','reading':r'\unsure{``|`}','alternatives':'fused double opener; single opener','confidence':'medium','reason':'Joined upper cluster does not separate the stroke count.'},
 {'place':'p.234 cancelled high group between ellipses','reading':r"\deleted{\unsure{''}}",'alternatives':'tentative cancelled closing quote pair; exact underlying count unresolved','confidence':'low','reason':'The dark overmark conceals the original short strokes.'},
 {'place':'p.234 cancelled item before iff','reading':r'\deleted{\unsure{if}}','alternatives':'if is tentative; underlying short item is not securely recoverable','confidence':'low','reason':'Only flattened openings and a low trace survive the crossing.'},
 {'place':'p.247 cancelled quoted word','reading':r'\unsure{aspheric}','alternatives':'aspheric tentative','confidence':'low','reason':'Dense diagonal zigzag buries the interior letters.'},
 {'place':'p.247 cancelled mapping index','reading':r'i_{\unsure{0}}','alternatives':'0 tentative','confidence':'low','reason':'Low stroke merges with cancellation; clear replacement is not evidence for the old glyph.'},
 {'place':'p.247 cancelled terminal quotation','reading':r"\unsure{''}",'alternatives':'closing pair tentative; count unresolved','confidence':'low','reason':'The terminal crossing merges with the high ticks.'},
 {'place':'p248 opener before handwritten','reading':r'\unsure{``|`}','alternatives':'fused double opener; single opener','confidence':'medium','reason':'Only one connected compact contour survives at quote height.'},
 {'place':'p.250 l.13 opener','reading':r'\unsure{``|`}','alternatives':'fused double opener; single opener','confidence':'medium','reason':'Bent left portion and small right lobe are connected.'},
 {'place':'262 cancelled old reference','reading':r'-\deleted{\unsure{13}}','alternatives':'13 tentative after a certainly live dash','confidence':'low','reason':'Crossing leaves the interior of the old reference uncertain.'},
 {'place':'263 last letter after allow','reading':r'allow\unsure{e|s}','alternatives':'e favoured; s possible','confidence':'medium','reason':'The small loop is e-shaped but has a dense retraced lower part.'}
]

inv=[]
def item(element,kind,position,first,hand='his hand'):
    inv.append(dict(sheet_kind='list',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=first,transcribed='yes'))
# Every separate correction/reference entry is covered; nested states are separate rows.
for eid,pos,first in [
 ('01','top row, p225 line 12','delete ``that\'\''),('02','same row, l.-7',"don't"),
 ('03','226 l.2','``do not\'\''),('04','230 l.-2',"'informal''"),('05','p232 l-3',"``inessential''"),
 ('06','p.233 l.1',"``its''"),('07','p.233 l2 & 3',"``shouldn't''"),('08','p.233 l-2',"``synonym''"),
 ('09','p.234 l.7','surely it should be; Then W is a mildly ... of (A,i)'),
 ('10','p.234 continuation, l.-6 and next writing line','x is aspheric ... iff u is aspheric; I suppose! A tautology it surely is as it stands!.'),
 ('11','p.239 l.3',"``suggests that we call an ...''"),
 ('12','p.240 l.3',r'W=(i_{M,i})^{-1}(\underline W)'),('13','p.240 l.10',"``its''"),('14','p.240 l-8',"``doesn't''"),
 ('15','p241 l-15',"``suggested a long time ago''"),('16','p242 l-12',"``its''"),('17','p242 l-2',"``its''"),
 ('18','p.243 l-6, two writing lines','too many negatives: We assume beforehand neither... not....; is one of many possibilities'),
 ('19','p244 l-15',"``doesn't''"),('20','p245. l.4',"``we'll''"),('21','p246 l.2',"``its''"),
 ('22','p.247 first main-line entry','cancelled l.14 and quoted aspheric'),
 ('23','p.247 main line, after old mapping',"; l-9 ``standard''"),
 ('24','p.247 lower continuation, l12',"``is aspheric''"),('25','p.247 lower continuation, l-2',"``didn't''"),
 ('26','p248 l.-3','handwritten: such that C-hat is totally ...'),
 ('27','p249 l-2',"``isn't''"),('28','p.250 l.10',"``developed''"),('29','p.250 l.12',"``its''"),('30','p.250 l.13',"its''"),
 ('31','p251 l.9',"``last but not least''"),('32','p251 l.15',r"``$i\colon A\to M$''.") ,
 ('33','255 l16',"``developed''"),('34','260 l.13',"``didn't''"),
 ('35','262, live l-3 & 2',"``may as well''"),
 ('36','263 l.19','allow[e/s] one to'),('37','263 l20',"'wasn't''"),('38','263 l.-13','``pushing on the.'),
 ('39','263 continuation l-11',"``and was finally''"),('40','263 continuation l.-4',"``developing''"),
 ('41','264, high mark and l12',"'l12 ``developed'' ``length''"),
 ('42','p267 l.2',"``developed''"),('43','p267 l-2','amounts to it being contractible'),
 ('44','p.269 first line','middle of page - followed by cancelled question'),
 ('45','p.269 second line, live continuation',r'\pi_0,\pi_1 are undefined here. Notation is confusing.'),
 ('46','p.270 l.-2',"``we've got''"),('47','p.273 l-7',"``isn't''"),('48','p.274 l-9',"``if I've got''")]:
    item(eid,'text',pos,first)
for eid,pos,first in [
 ('D01','p.234 l.7 between the dot groups',r"\deleted{\unsure{''}}"),
 ('D02','left of l.-6 after p.234 l.7',r'\deleted{p23}'),
 ('D03','p.234 l.-6 before iff',r'\deleted{\unsure{if}}'),
 ('D04','p.247 first main-line reference and word',r"\deleted{l.14 ``\unsure{aspheric}''}"),
 ('D05','p.247 main-line mapping',r"\deleted{should it be $(i_{\unsure{0}}\colon N)$\unsure{''}}"),
 ('D06','before 255',r'\deleted{2}'),
 ('D07','262, between the live dash and live l-3',r'\deleted{\unsure{13}}'),
 ('D08','p.269 after middle of page -',r"\deleted{isn't the use of $\pi_0,\pi_1$ slightly confusing here!}"),
 ('D09','p.269 next line before the live pi pair',r'\deleted{not $\pi_0,\pi_1$}')]:
    item(eid,'deletion',pos,first)
item('I01','insertion','p.247 raised line over the cancelled question',r'\inserted{(Cond\textsuperscript{n} (ii) should it be $i_0\colon N_0\to N$)}')
item('I02','insertion','p.247 below cancelled mapping, right of l12 text',r'\inserted{also}')
item('I03','insertion','p267 over gap between to and being, with caret',r'\inserted{it}')
item('U01','text','p248, nested underline','single underline confined to handwritten')
item('U02','text','p248, nested underline','single underline confined to is')
item('U03','text','p.269, nested underline','single underline confined to here')
item('G01','drawing','left reference/body boundary','thin long vertical rule')
item('G02','drawing','right edge of correction text','thin long vertical rule')
item('G03','drawing','p.247 below cancellation, left of also','descending curved connector')
item('G04','drawing','p.247 below old mapping','long oblique continuation')
item('G05','drawing','263 continuation, right of developing','short rising oblique')
item('G06','drawing','below 263 pushing on the.','short descending oblique')
item('G07','drawing','lower/right of previous oblique','short near-vertical mark')
item('G08','drawing','p.269 right of rule, upper position','small isolated point')
item('G09','drawing','p.269 right of rule, lower-left point','small isolated point')
item('G10','drawing','p.269 right of rule, lower position','short nearly horizontal stroke')
item('G11','drawing','p.273 reference/right gap','one raised isolated point')
item('A01','margin note','lower left corner','archive number 24, preserved as a comment','another unnamed hand (pencilled archive numbering)')

# This placement row quotes actual newlines and actual node code, not literal backslash-n escapes.
for row in changes:
    if row['id']=='p247-also-position':
        original=Path('work/inputs/025/C.tex').read_text()
        start=original.index('\\inserted{also};')
        stop=original.index("l12 ``is aspheric''",start)+len("l12 ``is aspheric''")
        row['c']=original[start:stop]
        start=tex.index('\\node at (934,1141)')
        stop=tex.index('\\node at (844,1208)',start)
        row['reading']=tex[start:stop].rstrip()

report={
 'scan':25,'reader':'B','model':'GPT-6 Astra Pro (inherited; exposed in the reader brief)','effort':'not exposed',
 'viewed':[W,A,B],
 'layout':'Portrait handwritten correction list on one sheet, with no title, date, or manuscript pagination. Entries cite p225 through p.274. A thin long rule separates the left reference area from the body, and another long rule stands at the right, passing through ends of long notes. The p.234 and p.243 notes continue on a second writing line. The p.247 block has two dense cancellations, a smaller raised condition line, a lower also beside a curved continuation, and a second slanted continuation. At p267, it is raised over a caret. At p.269 the abandoned question and a second abandoned fragment precede a live statement. All ordinary writing and corrections appear in the same hand. The pale lower-left 24 is archive numbering. Two pale circular marks near the right paper edge are physical sheet features. The inventory covers every separate correction entry and separately records nested deletions, insertions, underline spans and ink rules/isolated marks; no mathematical diagram or standalone display is present.',
 'changes':changes,'c_doubts':cd,'remaining_doubts':remaining,'inventory':inv,
 'notes':[
  'The page is an untitled list of corrections referring to pages 225–274. It states no document page count and no date. The handwritten reference numbers are not pagination of this note sheet; the separate archive number is 24.',
  'At p.234 l.7, surely it should be introduces a quoted formulation about W, mildness and (A,i). Both dot groups and the cancelled high group are retained without supplying the missing words.',
  'At the following l.-6 entry, x is aspheric iff u is aspheric is followed by I suppose! and A tautology it surely is as it stands!. Both exclamations and the extra final stop remain.',
  'At p.243 l-6 the author writes too many negatives, quotes a formulation with neither ... not, and qualifies it as one of many possibilities. The visible t is retained despite the grammar.',
  'At p.247 the smaller raised condition (ii) question proposes i_0: N_0 to N. The old quoted word and shorter mapping remain cancelled. Also stands lower, beside the l12 wording, and is kept at that physical level.',
  'At p248 the word handwritten and the verb is are each singly underlined. The expression has C with a separate hat and an unclosed initial quotation, followed by three low continuation marks.',
  'At p267, it is added above a caret between to and being in the contractibility wording.',
  'At p.269 an earlier question about slightly confusing use of pi_0 and pi_1, and then a shorter not/pi fragment, are cancelled. The live statement says the two symbols are undefined here, with here underlined, and that the notation is confusing. The referenced typescript page is not available for validating that complaint.'
 ],
 'math_checks':[
  {'statement_id':'S025-aspheric-biconditional','type':'computation or formal certificate','outcome':'Computed all four truth values of P iff Q, where P abbreviates x is aspheric and Q abbreviates u is aspheric. The two unequal assignments make the biconditional false, so it is not a propositional tautology when P and Q are independent. Source definitions could identify P and Q; they are not supplied, so this does not decide the author\'s context-dependent tautology comment. The literal x, u, iff and I suppose! remain unchanged. The four-row computation is recorded in math_check.json.'},
  {'statement_id':'S025-preimage-formula','type':'targeted proof check','outcome':'Checked the conditional set-theoretic interpretation: for f:X to Y and S contained in Y, f^{-1}(S)={x in X: f(x) in S} is a subset of X. Therefore the displayed inverse-image notation is type-consistent if i_{M,i} has the corresponding source/target and the two W collections have those ambient types; no inverse bijection is needed. The page gives no domains or definitions, so this is only a conditional consistency check and does not prove the asserted W equality. No letter, index or sign was inferred from this check.'}
 ],
 'notation':[
  {'sign':r'(A,i)','location':'p.234 l.7','reading':r'(A,i)','evidence':'Upper half: ordinary A, separate comma below midline, dotted i, and round delimiters.'},
  {'sign':r'W=(i_{M,i})^{-1}(\underline W)','location':'p.240 l.3','reading':r'W=(i_{M,i})^{-1}(\underline{W})','evidence':'Upper half: both low companions and comma are visible; raised -1; underline only under final W; no doubled capital outlines.'},
  {'sign':r'Cond\textsuperscript{n}','location':'p.247 raised line','reading':r'Cond\textsuperscript{n}','evidence':'Crop09: small raised n is separate from the following parenthesised ii.'},
  {'sign':r'i_0\colon N_0\to N','location':'p.247 raised line','reading':r'i_0\colon N_0\to N','evidence':'Crop09: each low zero is round, colon has two points, and the arrow has a right head.'},
  {'sign':r'i_{\unsure{0}}','location':'p.247 cancelled mapping','reading':r'i_{\unsure{0}}','evidence':'Crop10: independent uncertainty is retained at the buried old index.'},
  {'sign':r'\widehat C','location':'p248 l.-3','reading':r'\widehat C','evidence':'Lower half: two small oblique roof strokes stand above ordinary C.'},
  {'sign':r'\pi_0,\pi_1','location':'p.269 first cancelled pair','reading':r'\pi_0,\pi_1','evidence':'Crop19 separately shows a low loop and a low straight stroke.'},
  {'sign':r'\pi_0,\pi_1','location':'p.269 second cancelled pair','reading':r'\pi_0,\pi_1','evidence':'Crop20 shows an oval 0, low comma, and a single lowered 1.'},
  {'sign':r'\pi_0,\pi_1','location':'p.269 live pair','reading':r'\pi_0,\pi_1','evidence':'Lower half independently confirms the two lowered digit shapes.'},
  {'sign':'x; u; iff','location':'p.234 l.-6','reading':'x; u; iff','evidence':'Upper half and crop06: u has an open bowl and no closed a counter; iff has two tall looped f forms.'},
  {'sign':'not','location':'p.243 l-6','reading':'not','evidence':'Crop07: the final upright and long rightward cross stroke decide t.'},
  {'sign':'ellipsis marks','location':'p.234 l.7; p248 l.-3','reading':'... in each group','evidence':'Crop04 has three marks in each group, with the second group beginning in a broad wavy stroke; crop12 has two elongated low marks and one shorter point. No words or closing delimiter are supplied.'},
  {'sign':'detached high stroke','location':'264 before l12','reading':"'",'evidence':'Crop17: one independent short curved vertical stands to the left of l; its grammatical function is left unassigned.'},
  {'sign':'final small loop after allow','location':'263 l.19','reading':r'allow\unsure{e|s}','evidence':'Crop16 favours e from a small counter and fine exit but does not exclude a cramped s.'},
  {'sign':'opening quotation count','location':'p.234 surely; p248 handwritten; p.250 l.13 its','reading':r'\unsure{``|`} at each occurrence','evidence':'Crops03,11,13 were inspected independently; each retains a connected group compatible with a double or single opener.'},
  {'sign':'p.233 stop; p267 l-2; p232 closing pair','location':'corresponding reference and quotation loci','reading':r"p.233; l-2; inessential''",'evidence':'Crops02,18,01 respectively confirm the low reference stop, absence of an extra stop in l-2, and joined but visibly two-part closing quotation.'}
 ],
 'abbreviations':[
  {'form':'p / p.','expansion':'page (tentative list interpretation)','place':'reference column throughout'},
  {'form':'l / l.','expansion':'line (tentative list interpretation)','place':'line references throughout'},
  {'form':r'Cond\textsuperscript{n}','expansion':'Condition (tentative list interpretation)','place':'p.247 raised line'},
  {'form':'iff','expansion':'if and only if (list interpretation only)','place':'p.234 l.-6'}
 ],
 'brief_feedback':'The exact-one-view rule was followed for the whole and each half. All 21 unresolved loci were frozen before cropping, then each was cropped once by scripts/crop.py at 2400 pixels and actually displayed once. No OCR, external research, other-page image, other-reader output, agent delegation, compilation or installation was used. The biggest scope issue is the heavily cancelled p.247 word and quote edge; the state is clearer than the buried letters, so doubts are retained. The C_context note about the cancelled index required an independent doubt there despite the clear raised zero. H is description only and contributes no collation rows. The whole-page anchored TikZ layout is necessary to retain the long rules and scattered marks in their relationship to the text. Coverage and literal-diff checks are static only.'
}
(D/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')

# Preserve the per-crop outcomes, including confirmations that do not become changes.
crop_decisions={
 '01':'Confirmed C: closing quote is a joined but two-part raised group; no new collation row.',
 '02':'Confirmed C: a separate low stop occurs after p in p.233.',
 '03':'Added independent opening-quote count uncertainty before surely.',
 '04':'Retained the cancelled quote doubt; confirmed three mark groups on each side.',
 '05':'Resolved cancelled page-reference digits as 23; supplied no missing final digit.',
 '06':'Retained cancelled if as tentative; independently confirmed open-bowl u and live iff.',
 '07':'Resolved not from the crossed final t; retained four low marks after it, including the faint last one.',
 '08':'Resolved l.14; retained aspheric uncertainty and the whole cancelled phrase state.',
 '09':'Resolved raised i index as 0; confirmed N_0, colon, right arrow, parentheses, Cond raised n.',
 '10':'Retained old trailing quote doubt, added old index uncertainty, kept also lower, and preserved the two descending extensions.',
 '11':'Added independent opening-quote count uncertainty before handwritten; confirmed one underline.',
 '12':'Confirmed three terminal low marks after totally; no closing quotation was supplied.',
 '13':'Added independent opening-quote count uncertainty before the l.13 its; confirmed separate i dot and double closer.',
 '14':'Resolved the cancelled digit as 2.',
 '15':'Kept the preceding dash live, retained uncertainty in cancelled 13, and rejected a separate minus before live 2.',
 '16':'Revised the last-letter doubt to e|s with e visually favoured.',
 '17':'Resolved one detached apostrophe-shaped stroke without interpreting its role.',
 '18':'Confirmed C l-2 without an extra stop.',
 '19':'Confirmed the cancelled question, first pi indices and terminal exclamation; no source-page claim was inferred.',
 '20':'Resolved cancelled not and confirmed the second pi pair.',
 '21':'Preserved the isolated high point once, geometrically, without assigning a full-stop function.'
}
(D/'crop_decisions.json').write_text(json.dumps([dict(id=k,decision=v,**loc(k)) for k,v in crop_decisions.items()],ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'changes':len(changes),'c_doubts':len(cd),'c_doubts_resolved':sum(d['resolved'] for d in cd),'remaining_doubts':len(remaining),'inventory':len(inv),'math_checks':len(report['math_checks']),'crops':len(loci)},indent=2))
