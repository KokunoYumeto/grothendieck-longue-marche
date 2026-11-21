from pathlib import Path
import json

DEST = Path('/workspace/scratch/94548b74fbe0/out/readers/017/C')
diffs = []

def add(id, location, C, H, reading, evidence, confidence, kind, diff_C, diff_H, status=None, crop=None, bbox=None, row=None, part=None, **extra):
    item = dict(id=id, location=location, C=C, H=H if H is not None else '(no corresponding entry in H)', reading=reading, evidence=evidence, confidence=confidence, kind=kind, diff_C=diff_C, diff_H=diff_H, C_doubt_status=status, readers_crop=crop, bbox={'coordinate_system':'full scan, top-left origin', 'xyxy':bbox} if bbox else None)
    if row:
        item['C_source_row'] = f'C_doubts.txt / Doubtful readings / row {row:02d}'
        item['C_source_local_part'] = part
    item.update(extra)
    diffs.append(item)

add('D01','Opening cancelled clause: first indexed letter',r'\unsure{E_i|\Sigma_i}',r'E_i',r'E_i','A left upright and three surviving horizontal arms support E; the indexed form is kept inside the cancellation.','medium','other',True,False,'resolved','crop01_opening.png',[1040,215,1140,285],1,'E_i / Sigma_i')
add('D02','Opening cancelled clause: short verb',r'\unsure{est}',r'soit',r'\unsure{est|soit}','Crossing strokes cover the middle letters; a short opening loop and tall terminal stroke support est, with soit still possible.','low','misread word',False,True,'retained','crop01_opening.png',[1135,228,1265,278],1,'est',qualification='H soit remains an explicit alternative; this is a qualified primary-candidate difference.')
add('D03','Opening cancelled clause: rare/dense',r'\unsure{rare|dense}','rare','rare','The low sequence has two short r-like shoulders and a rounded ending; rare is readable through the cancellation.','medium','other',True,False,'resolved','crop01_opening.png',[1250,237,1380,276],1,'rare / dense')
add('D04','Full stop after cancelled X',r'X$.}',r'X$}',r'X$.}','A separate dark point follows the crossed X before the lower parenthetical continuation.','high','omission',False,True,None,'crop01_opening.png',[1535,237,1610,289])
add('D05','Raised on ait above opening cancellation',r'\inserted{on ait}','on ait',r'\inserted{on ait}','The two words sit on a distinct raised baseline above the crossed clause.','high','insertion or placement',False,True,None,'crop01_opening.png',[1135,185,1350,233])
add('D06','Opening of parenthetical after on ait','si','où','si','After the opening curve, the small s-form is followed by a separate upright i; the reading si is retained.','high','misread word',False,True,None,'crop01_opening.png',[1390,180,1475,235])
add('D07','Cancelled sentence above the two equalities',r'\unsure{trouve}','trouve',r'\unsure{trouve}','The tall t and several low returns survive; the horizontal cancellation merges the remaining short letter strokes.','low','other',False,False,'retained','crop02_cancelled_sentence.png',[548,325,735,380],2,'trouve')
add('D08','End of first upper equality',r'E_i',r'E_i,',r'E_i','The enlarged space after the dotted index is clear through the right context; no separate comma is recovered there.','high','text not on the page',False,True,None,'crop03_equalities.png',[935,425,1090,500])
add('D09','Detached point far right of second upper equality',r'E_i .',r'E_i .','M01: locally qualified literal triangular point; period is retained as an interpretation alternative.','A compact triangular point lies well to the right of E_i on the lower equality level. Its shape is clear; its punctuation role remains open.','medium','drawing or diagram',True,True,None,'crop03_equalities.png',[1168,554,1185,571],graphic='M01',shape_confidence='high',role_confidence='low',qualification='Both witnesses period readings remain supported alternatives. One physical point is represented once.')
add('D10','Prose before third equality',"Alors je dis qu'on a",'Alors je dis que',"Alors je dis qu'on a",'The apostrophe and low on run follow qu; a small separate final a is visible at the right endpoint.','high','omission',False,True,None,None,[300,620,1000,775],half_evidence='half a, same coordinates as the full scan')
add('D11','Third equality: first join',r'\unsure{\cup|\amalg}',r'\cup','G01: locally qualified retraced cup graphic, with amalg alternative.','One shared left upright and two closely spaced right returns form a heavy overdrawn cup-like sign. The right-hand join after E_1 has a separate simple curve.','medium','drawing or diagram',True,True,'retained','crop04_join.png',[943,780,984,817],3,'first join',graphic='G01',qualification='Original cup/amalg uncertainty is retained. The change records the visible retracing geometry, without assigning a writing sequence.')
add('D12','Dividing rule below third equality',r'\rule{2.4cm}{0.3pt}',None,'G02: bowed single rule with a short hooked right end.','The rule rises gently and has a small downturned right endpoint; it occupies the left part of the writing area.','high','drawing or diagram',True,True,None,None,[298,884,545,913],graphic='G02',half_evidence='half a, same coordinates as the full scan',H_absence='No rule is transcribed in the supplied H body.')
add('D13','First word of angled margin note','introduire','introduisons',r'\unsure{introduire|introduisons}','The ending is compressed into a low connected run and hooked terminal; introduire is the stronger reading, with the longer H ending still supported.','low','misread word',True,True,None,'crop05_margin.png',[45,945,255,1110],qualification='H introduisons survives as an explicit alternative.')
add('D14','Angled margin note: partition letter',r'\unsure{\Pi|\pi}_j',r'\Pi_j',r'\unsure{\Pi|\pi}_j','A joined top and two descending legs are visible. The compact size and curved right leg leave the case unresolved.','medium','other',False,False,'retained','crop05_margin.png',[28,1220,108,1320],4,'Pi_j / pi_j')
add('D15','Angled margin note: under-form of E_j and H terminal ill',r'\deleted{\unsure{\Sigma}}E_j',r'E_j ... \ill{}',r'\deleted{\unsure{\Sigma}}E_j','Angular diagonal remnants are covered by the darker E strokes. The note ends at its closing brace; the edge fragments belong to adjacent main writing.','low','readable ink left as \\ill{}',False,True,'retained','crop05_margin.png',[125,1155,191,1222],4,'crossed Sigma',H_physical_parent='H.marginal.trailing_ill',qualification='The terminal H placeholder is collated once here with the locally recoverable qualified predecessor; no further word is supplied after the brace.')
add('D16','Beginning of main partition paragraph: accent','Considérons','Considérons',r'Consid\unsure{e|é}rons','The enlarged word supplies its complete connected letters; a separate acute over the relevant vowel is not securely isolated from the tall neighbouring return.','low','misread word',True,True,None,'crop14_considerons.png',[315,1145,725,1220],qualification='The accented witness spelling remains an explicit alternative.')
add('D17','Raised Pi_J before de X: curved guide',r'\inserted{\Pi_J}',r'\add{\Pi_J}','Inserted Pi_J plus G03 curved attachment guide.','A long bent curve runs below the raised partition name into the following de; it is preserved in addition to the insertion annotation.','high','drawing or diagram',True,True,None,None,[1215,1100,1390,1240],graphic='G03',half_evidence='half a, same coordinates as the full scan')
add('D18','Cancelled word after de X',r'\deleted{\unsure{des parties|définie}}',r'\struck{définie}',r'\deleted{définie}','The small initial d loop, tall descending f and following short letter sequence are readable beneath the single horizontal strike.','medium','misread word',True,False,'resolved',None,[415,1265,657,1390],5,'des parties / définie',half_evidence='half b, bbox [415,164,657,289], origin at full-scan y=1101')
add('D19','Earlier E_j in par les E_j: overwritten predecessor',r'\deleted{\Sigma}E_j (source doubt table qualifies Sigma)',r'E_j',r'\deleted{\unsure{\Sigma}}E_j','The live E has three dark arms; diagonal remnants form an X-like crossing within it, leaving Sigma as a qualified predecessor.','low','omission',False,True,'retained','crop06_old_sigma.png',[1280,1275,1370,1380],7,'under E_j',qualification='The C table already qualifies this physical under-form although C.tex prints it without unsure.')
add('D20','Opening of intersection: et and its cancellation state',r'\deleted{\unsure{et}}',r'\struck{intersection}\add{intersection}',r'\unsure{\deleted{et}|et} intersection','A small loop and tall return precede the main word. Their low joining stroke merges with the apparent crossing, leaving the local cancellation target uncertain.','low','deletion state (struck given live or live given struck)',True,True,'retained','crop07_intersection.png',[325,1410,425,1480],6,'et',qualification='The selected primary state is cancelled et; live et remains explicit. The H cancelled/added intersection sequence is collated once as this physical opening cluster.')
add('D21','The longer word intersection',r'\unsure{intersection}',r'\add{intersection}','intersection','The longer sequence has the tall internal strokes, low joined middle and terminal tion run needed for intersection.','medium','other',True,False,'resolved','crop07_intersection.png',[400,1400,650,1480],6,'intersection',physical_parent='D20',qualification='H state qualification is recorded under D20; the longer live word agrees.')
add('D22','Raised ternaires Pi_j and caret',r'\inserted{ternaires \Pi_j}',r'\add{ternaires \Pi_j}','Inserted ternaires Pi_j plus G04 two-branch caret.','A shallow left branch descends to the insertion point; a stronger oblique right branch rises from the same point.','high','drawing or diagram',True,True,None,None,[950,1350,1250,1460],graphic='G04',half_evidence='half b bbox [950,249,1250,359], origin at full-scan y=1101')
add('D23','Isolated crossed sign after later E_j',r'\deleted{\unsure{E|\in}}',r'\ill{}',r'\deleted{\unsure{E|\in}}','A narrow two-lobed form and an oblique crossing survive before the following parenthesis; E and membership remain plausible readings.','low','readable ink left as \\ill{}',False,True,'retained','crop08_late_cancel.png',[1175,1505,1225,1580],7,'after later E_j',H_physical_parent='H.body.after_Ej.ill')
add('D24','Lower display: small detached mark by Sigma head and alpha',r'\Sigma_j^\alpha',r'\Sigma_j^\alpha','M03: local qualified short dark mark, with dotless j used in the text node to avoid a second printed dot.','The crop shows a short separate dark piece above the Sigma head, immediately left of alpha. Its possible attachment to the j remains open.','medium','drawing or diagram',True,True,None,'crop09_display_marks.png',[1188,1623,1203,1640],graphic='M03',shape_confidence='high',role_confidence='low',qualification='This records the local placement and unresolved attachment, without assigning an extra mathematical operation.')
add('D25','Two detached specks at right of lower display',None,None,'M02a and M02b: two separate qualified dark-speck paths.','Two compact dark pieces lie diagonally apart in the right blank area, below the formula level; neither yields a secure character candidate.','medium','drawing or diagram',True,True,None,'crop09_display_marks.png',[1568,1738,1581,1755],graphic='M02a; M02b',shape_confidence='high',role_confidence='low',hand='undetermined hand',surface_origin='unestablished')
add('D26','Inserted lower partition name: raised ring',r'\Pi_J^{\unsure{\circ|0}}',r'\Pi_J^0',r'\Pi_J^{\unsure{\circ|0}}','The raised closed ring has no decisive feature separating the circle and zero candidates at this scale.','medium','misread symbol or index',False,True,'retained','crop10_pi_union.png',[775,1970,865,2030],8,'Pi_J above de',qualification='H zero remains an explicit alternative.')
add('D27','Guide under inserted Pi_J with ring',r'\inserted{\Pi_J^{\unsure{\circ|0}}}',r'\add{\Pi_J^0}','The same insertion with G05 curved guide into de.','A curved stroke begins low at the left of de, rises beneath the raised name and ends with a short turn.','high','drawing or diagram',True,True,None,'crop10_pi_union.png',[805,1988,902,2060],graphic='G05')
add('D28','First complement after inserted Pi_J: transverse union stroke',r'\unsure{\overline{\bigcup}|\bigcup}',r'\bigcup','G06: literal cup with short transverse stroke, locally qualified as to mathematical role.','The horizontal begins slightly left of the cup stem and ends before the right stem. Its presence is clear; the path preserves its height inside the cup mouth.','high','drawing or diagram',True,True,'resolved','crop10_pi_union.png',[1115,1975,1185,2037],11,'bar on union / plain union',graphic='G06',role_confidence='low',qualification='The source doubt about presence of a stroke is resolved. Its mathematical role remains separately qualified; the transcription uses the literal drawn form.')
add('D29','Binary partition name: second raised ring',r'\Pi_{J,j}^{\circ} (qualified by source row 8)',r'\Pi_{J,j}^0',r'\Pi_{J,j}^{\circ}, sharing the first ring qualification','The second raised small ring is visible above the two distinct indices J,j. Its circle/zero uncertainty is retained under the first-occurrence convention.','medium','misread symbol or index',False,True,'retained','crop11_binary.png',[1090,2115,1225,2205],8,'binary partition name',qualification='The original C compound row covers this second occurrence even though C.tex has no second unsure macro; H zero remains a supported alternative.')
add('D30','Inserted condition and guide above induites',r'\inserted{(j\in J)}',r'\add{(j\in J)} (induites','Inserted condition plus G07 long hooked guide.','The left curve continues across the top of induites and finishes with a small right hook; it is drawn as one connected guide.','high','drawing or diagram',True,True,None,'crop11_binary.png',[1235,2070,1560,2190],graphic='G07')
add('D31','H opening parenthesis before induites','induites','(induites','induites, with G07 above it','The curve read in H as an opening parenthesis is continuous with the long guide over the word.','high','text not on the page',False,False,None,'crop11_binary.png',[1235,2105,1285,2178],physical_parent='D30',qualification='This local H punctuation interpretation is recorded without a second H change count for the same guide cluster.')
add('D32','Inserted U: repeated subscript forms',r'U_{\deleted{\unsure{J|j}}J}',r'U_J',r'U_{\unsure{\deleted{J}J|\deleted{j}J|J}}','Two displaced lower hooks are visible under the shared upper material. They support the old/live J/j readings and a single retraced J reading.','low','deletion state (struck given live or live given struck)',True,True,'retained','crop12_U.png',[365,2160,430,2235],12,'U subscript under-form',qualification='The original J/j doubt remains. Complete-state alternatives preserve the additional uncertainty about a cancelled predecessor versus retracing.')
add('D33','Insertion state of U_J =',r'\inserted{U_{...}={}}',r'U_J =',r'\inserted{U_{...}={}}','The U expression is raised above sur and connected to the gap before X by the descending guide.','high','insertion or placement',False,True,None,'crop12_U.png',[350,2155,460,2240])
add('D34','Long guide beneath inserted U expression',r'\inserted{U_{...}={}}',r'U_J =','G08: bent guide descending beside sur to its full lower endpoint.','The thin stroke travels under the subscript area, bends right and descends beyond the prose baseline.','high','drawing or diagram',True,True,None,'crop12_U.png',[368,2215,460,2302],graphic='G08')
add('D35','Last quantified letter',r'\unsure{g|j}',r'j',r'\unsure{g|j}','A compact upper loop sits on a long hooked descender. The local g-like top remains clearer than a simple dotted upright, with j retained.','low','misread symbol or index',False,True,'retained','crop13_end.png',[1235,2235,1288,2317],9,'g / j',qualification='H j remains an explicit alternative; no index is selected from the formula context.')
add('D36','Closing punctuation after final quantified condition',r'(g\in J).',r'(j\in J)).',r'(\unsure{g|j}\in J).','One closing curve follows J, followed by a separated full stop.','high','text not on the page',False,True,None,'crop13_end.png',[1388,2215,1470,2300])
add('D37','Final word at right edge',r'\unsure{Pour|Puis}',r'\uncertain{Pour}','Pour','The capital P, small low o and connected ur ending are recoverable; the entire final hook remains inside the crop.','medium','other',True,False,'resolved','crop13_end.png',[1500,2210,1640,2285],10,'Pour / Puis',qualification='The next-sheet wording mentioned in the C table was not used as reading evidence.')

inventory = []
def inv(element,kind,position,words,hand='his hand',**extra):
    item=dict(sheet_kind='text',hand=hand,element=element,kind=kind,position=position,first_words_or_objects=words,transcribed='yes')
    item.update(extra)
    inventory.append(item)

inv('017.C.01','text','Top heading and single underline','Cas particuliers; single underline')
inv('017.C.02','text','Opening supposition and parenthesis','Supposons que forall i in I; si Sigma_i+ Sigma_i-; comp. conn.; X setminus Sigma_i')
inv('017.C.03','deletion','Opening clause to right','E_i est|soit rare dans X.')
inv('017.C.04','insertion','Above opening cancellation','on ait')
inv('017.C.05','deletion','Above upper equalities','Alors on unsure trouve que')
inv('017.C.06','display','Upper two physical rows','barred Sigma_i+ = Sigma_i+ union E_i; barred Sigma_i- = Sigma_i- union E_i')
inv('017.C.07','drawing','Far right of second upper equality','M01: triangular point; period interpretation alternative','undetermined hand',components=['M01 fill path'],role='unresolved punctuation role')
inv('017.C.08','text','Before third equality',"Alors je dis qu'on a")
inv('017.C.09','display','Third equality','barred Sigma_12 = Sigma_12 [qualified retraced cup] E_1 union E_2')
inv('017.C.10','drawing','First join in third equality','G01 shared left stem, inner return, outer return',components=['G01 draw 1: shared left upright','G01 draw 2: inner curve and right upright','G01 draw 3: outer curve and right upright'])
inv('017.C.11','drawing','Below third equality, left of writing area','G02 bowed dividing rule with hooked right end',components=['G02 one connected draw path'])
inv('017.C.12','margin note','Left slant beside Supposons/Soit','introduire|introduisons la partition Pi|pi_j = {deleted unsure Sigma E_j, Sigma_j+, Sigma_j-}')
inv('017.C.13','deletion','Within marginal E_j','Qualified Sigma predecessor')
inv('017.C.14','deletion','Below dividing rule','Supposons')
inv('017.C.15','text','New paragraph after cancelled Supposons','Soit J subset I tel que I = J amalg {i}.')
inv('017.C.16','text','Main partition paragraph','Consid[e|é]rons la partition ... définie par les ... intersection des partitions ... définies par les E_j')
inv('017.C.17','insertion','Above de X in main paragraph','Pi_J')
inv('017.C.18','drawing','Under raised Pi_J','G03 bent guide into de',components=['G03 one connected draw path'])
inv('017.C.19','deletion','After de X','définie')
inv('017.C.20','deletion','Under earlier E_j after par les','Qualified Sigma predecessor')
inv('017.C.21','deletion','Before intersection','Qualified deleted et / live et state',state='cancelled primary; live alternative retained')
inv('017.C.22','insertion','Above partitions de X','ternaires Pi_j')
inv('017.C.23','drawing','Caret after partitions','G04 shallow left branch and stronger oblique right branch',components=['G04 draw 1: curved left branch','G04 draw 2: right oblique branch'])
inv('017.C.24','deletion','After later E_j, before condition','Qualified E / membership sign')
inv('017.C.25','display','Lower middle','X = E_j amalg coproduct over alpha in pi_0(X setminus E_j) of Sigma_j^alpha')
inv('017.C.26','drawing','Near lower-display Sigma head and alpha','M03 short detached dark mark','undetermined hand',components=['M03 one fill path; source origin (1192,1627)'],role='attachment to subscript j remains possible; no further operation assigned')
inv('017.C.27','drawing','Right blank area below lower display','M02a upper-right speck','undetermined hand',components=['M02a first fill path'],role='unestablished; surface origin unestablished')
inv('017.C.28','drawing','Right blank area below lower display','M02b lower-left speck','undetermined hand',components=['M02b second fill path'],role='unestablished; surface origin unestablished')
inv('017.C.29','text','Lower paragraph to page end',"-- c'est aussi la partition définie par celle de ... en les E_j, et la partition ... intersection des partitions binaires ... induites sur ... par les Pi_j (g|j in J). Pour")
inv('017.C.30','insertion','Above de in lower paragraph','Pi_J with qualified raised circle / zero')
inv('017.C.31','drawing','Below raised Pi_J with ring','G05 curved guide into de',components=['G05 one connected draw path'])
inv('017.C.32','drawing','Union inside first lower complement','G06 cup and transverse stroke',components=['G06 draw 1: cup','G06 draw 2: transverse line'],role='transverse stroke visibly present; mathematical role qualified')
inv('017.C.33','insertion','Above induites','(j in J)')
inv('017.C.34','drawing','Over induites','G07 long connected hooked guide',components=['G07 one connected draw path'])
inv('017.C.35','insertion','Above sur, attached before X','U subscript [deleted J + J / deleted j + J / single retraced J] =')
inv('017.C.36','deletion','Within inserted U subscript','Qualified predecessor J / j with single-retraced-J state alternative',state='cancellation/retracing unresolved')
inv('017.C.37','drawing','From below U subscript down beside sur','G08 long bent guide',components=['G08 one connected draw path'])
inv('017.C.38','text','Lower left archive numeral','16, transcribed only in archive-number comment','undetermined hand')

source_rows = [
 (1,'first line directly under on ait',['Eᵢ; est; rare','Σᵢ; dense'], [('E_i / Sigma_i','D01','resolved'),('est','D02','retained'),('rare / dense','D03','resolved')]),
 (2,'struck sentence above equalities',['trouve','—'], [('trouve','D07','retained')]),
 (3,'third equality, first join',['∪','⨿'], [('first join','D11','retained')]),
 (4,'left note',['Πⱼ; crossed Σ','πⱼ; underlying form uncertain'], [('Pi_j / pi_j','D14','retained'),('crossed Sigma','D15','retained')]),
 (5,'after de X',['des parties','définie'], [('cancelled word','D18','resolved')]),
 (6,'start of intersection',['et; intersection','—'], [('et and its state','D20','retained'),('intersection','D21','resolved')]),
 (7,'under Eⱼ and after later Eⱼ',['Σ; E','∈ for the later shape'], [('under E_j','D19','retained'),('after later E_j','D23','retained')]),
 (8,'Π_J above de, and binary partition name',['upper circle','0'], [('Pi_J above de','D26','retained'),('binary partition name','D29','retained')]),
 (9,'last parenthesis',['g','j'], [('quantified letter','D35','retained')]),
 (10,'last word at right edge',['Pour','Puis'], [('final word','D37','resolved')]),
 (11,'first complement after inserted Π_J',['bar on ⋃','plain ⋃'], [('visible transverse stroke','D28','resolved')]),
 (12,'above sur, U subscript',['capital J under final J','j as under-form'], [('subscript and full state alternatives','D32','retained')]),
]

doubts = [
 dict(location='Opening cancelled verb',reading='est',alternatives=['soit'],confidence='low',reason='Central strokes are merged by the crossing.',crop='crop01_opening.png',difference='D02'),
 dict(location='Cancelled sentence above equalities',reading='trouve',alternatives=[],confidence='low',reason='Only some individual letter strokes survive below the cancellation.',crop='crop02_cancelled_sentence.png',difference='D07'),
 dict(location='Point after second equality',reading='literal triangular point',alternatives=['period interpretation'],confidence='low',reason='Its shape is visible; role and hand are unestablished.',crop='crop03_equalities.png',difference='D09'),
 dict(location='First join in third equality',reading='retraced cup graphic',alternatives=['amalg'],confidence='medium',reason='Overlapping curves and uprights remain under one local qualification.',crop='crop04_join.png',difference='D11'),
 dict(location='First marginal word',reading='introduire',alternatives=['introduisons'],confidence='low',reason='The compressed terminal run does not settle every ending stroke.',crop='crop05_margin.png',difference='D13'),
 dict(location='Marginal partition letter',reading='Pi_j',alternatives=['pi_j'],confidence='medium',reason='Case remains uncertain in the compact two-legged form.',crop='crop05_margin.png',difference='D14'),
 dict(location='Marginal E_j predecessor',reading='cancelled Sigma',alternatives=[],confidence='low',reason='The dark live E covers much of the angled under-form.',crop='crop05_margin.png',difference='D15'),
 dict(location='Consid[e|é]rons',reading='e',alternatives=['é'],confidence='low',reason='An independent acute is not securely isolated from the adjacent tall return.',crop='crop14_considerons.png',difference='D16'),
 dict(location='Earlier E_j predecessor in main text',reading='cancelled Sigma',alternatives=[],confidence='low',reason='Crossing diagonals survive under the live E without fully separating the old letter.',crop='crop06_old_sigma.png',difference='D19'),
 dict(location='Opening before intersection',reading='cancelled et',alternatives=['live et'],confidence='low',reason='Glyph and local cancellation target remain crowded together.',crop='crop07_intersection.png',difference='D20'),
 dict(location='Later isolated crossed sign',reading='cancelled E',alternatives=['cancelled membership sign'],confidence='low',reason='A two-lobed shape and slash survive without resolving the letter/sign.',crop='crop08_late_cancel.png',difference='D23'),
 dict(location='Detached mark by lower Sigma/alpha',reading='literal short dark piece',alternatives=['attachment as j dot'],confidence='low',reason='The physical piece is clear but its attachment and hand remain open.',crop='crop09_display_marks.png',difference='D24'),
 dict(location='Right of lower display',reading='two literal dark specks',alternatives=[],confidence='low',reason='Role, hand and surface origin remain unestablished; no character is supplied.',crop='crop09_display_marks.png',difference='D25'),
 dict(location='First raised ring over Pi_J',reading='circle',alternatives=['zero'],confidence='medium',reason='The small raised ring does not settle the character interpretation.',crop='crop10_pi_union.png',difference='D26'),
 dict(location='Transverse line at union mouth',reading='literal cup with transverse stroke',alternatives=['barred-union interpretation'],confidence='low',reason='Stroke presence is resolved; mathematical role is separately unestablished.',crop='crop10_pi_union.png',difference='D28'),
 dict(location='Second raised ring over binary partition name',reading='circle',alternatives=['zero'],confidence='medium',reason='The repeated ring retains the first-occurrence qualification.',crop='crop11_binary.png',difference='D29'),
 dict(location='U subscript sequence',reading='cancelled J followed by J',alternatives=['cancelled j followed by J','single retraced J'],confidence='low',reason='Two lower hooks share crowded upper strokes, leaving glyph and sequence states open.',crop='crop12_U.png',difference='D32'),
 dict(location='Last quantified letter',reading='g',alternatives=['j'],confidence='low',reason='The small loop and long hooked descender remain compatible with both candidates.',crop='crop13_end.png',difference='D35'),
]

graphics = [
 dict(id='M01',source_origin=[1172,557],drawing_rectangle=[0,0,7,7],observed_locus_box=[1168,554,1185,571],components=['one triangular fill'],role='point/period role uncertain'),
 dict(id='G01',source_origin=[947,783],drawing_rectangle=[0,0,33,32],observed_locus_box=[943,780,984,817],components=['shared left upright','inner return and right upright','outer return and right upright'],role='cup/amalg reading retained'),
 dict(id='G02',source_origin=[300,887],drawing_rectangle=[0,0,1300,25],observed_locus_box=[298,884,545,913],components=['one connected rule, curved run and terminal hook']),
 dict(id='G03',source_origin=[1215,1100],drawing_rectangle=[0,0,175,140],observed_locus_box=[1275,1170,1375,1220],components=['one connected guide'],text_nodes=['inserted Pi_J','de']),
 dict(id='G04',source_origin=[950,1350],drawing_rectangle=[0,0,300,110],observed_locus_box=[1125,1380,1235,1457],components=['curved left caret branch','oblique right caret branch'],text_nodes=['inserted ternaires Pi_j']),
 dict(id='M03',source_origin=[1192,1627],drawing_rectangle=[0,0,7,7],observed_locus_box=[1188,1623,1203,1640],components=['one short fill'],parent_picture_origin=[1145,1624],fixed_inner_translation=[47,3],role='unresolved; j-dot attachment supported'),
 dict(id='M02',source_origin=[1568,1738],drawing_rectangle=[0,0,13,17],observed_locus_box=[1568,1738,1581,1755],components=['M02a upper-right fill','M02b lower-left fill'],role='unestablished'),
 dict(id='G05',source_origin=[770,1970],drawing_rectangle=[0,0,165,110],observed_locus_box=[805,1988,902,2060],components=['one curved guide'],text_nodes=['inserted Pi_J with qualified ring','de']),
 dict(id='G06',source_origin=[1115,1975],drawing_rectangle=[0,0,70,62],observed_locus_box=[1115,1975,1185,2037],components=['cup contour','transverse line'],role='transverse stroke present; mathematical role qualified'),
 dict(id='G07',source_origin=[1235,2070],drawing_rectangle=[0,0,320,120],observed_locus_box=[1235,2070,1560,2190],components=['one hooked guide'],text_nodes=['inserted (j in J)','induites']),
 dict(id='G08',source_origin=[330,2160],drawing_rectangle=[0,0,145,160],observed_locus_box=[368,2215,460,2302],components=['one bent guide ending at declared source coordinate (453,2294)'],text_nodes=['sur','inserted U with qualified complete-state subscript and equals']),
]

report = dict(
 scan=17, reader='C', start_utc='2026-11-20 17:09:20 UTC', end_utc=None,
 full_image_viewed=True, halves_viewed=True, complete_visual_read=True,
 model='GPT-6 Astra Pro', effort='not separately exposed',
 reader_identity='Independent C-reader; witness C is the supplied C.tex and apparatus.',
 differences=diffs, doubts=doubts, inventory=inventory,
 C_source_row_map=[dict(id=f'C_doubts.txt / Doubtful readings / row {n:02d}', original_place=place, original_reading_columns=cols, local_parts=[dict(name=name,difference=diff,status=status) for name,diff,status in parts]) for n,place,cols,parts in source_rows],
 notes={
  'page_content':'Underlined Cas particuliers; opening cancelled wording and raised on ait; two closure equalities; Alors je dis qu\'on a and a third equality; a dividing rule; an angled partition note; cancelled Supposons; the main partition paragraph with several raised additions; lower partition display and paragraph ending Pour.',
  'author_own_uncertainty':'No separate verbal uncertainty or question mark is recovered. The exact manuscript assertion Alors je dis qu\'on a is retained. The unsure annotations belong to this reading.',
  'title_date_page_counts':'Title Cas particuliers has one underline. No date or separate manuscript page number is recovered. Pencilled archive numeral 16 is recorded only as the prescribed comment, with hand undetermined.',
  'mathematics_led_reading_decisions':'The complement in the opening parenthesis is X setminus Sigma_i as visibly written. The lower transverse union stroke and all doubtful indices are preserved from their own strokes. No mathematical correspondence, proof, numerical geometry comparison, or algebraic repair was used to choose a reading.',
  'H_apparatus':'H page{16} is its page identifier. H note about X setminus Sigma_i and X setminus E_i is editorial apparatus. H emph on the heading conveys the same single emphasis span. H add/struck correspond to insertion/deletion conventions. H uncertain{Pour} adds no independent difference after the word is recovered.',
  'C_scope':'Only the actual Doubtful readings section provides the source doubt identities. Its row 7 qualifies the earlier Sigma even without a C.tex unsure macro; row 8 also covers the second raised ring. Each row and separately named local part is mapped above. The next-sheet words in row 10 were not used.',
  'image_workflow':'Whole scan viewed once for layout; half a once and half b once for full line-by-line reading; all fourteen created crop images viewed once each. No image was reopened after its decision. Crop 14 was added for unresolved accent presence, without remaking another crop.',
  'crop_boundaries':'All deciding target continuations are retained. Crop 05 includes a small edge trace from adjacent main writing near Soit; it supplies no extra marginal word. Crops 02, 09, 10, 11 and 12 contain clipped neighbouring context at their boundaries, while their stated target loci and target endpoints remain in view.',
  'graphic_coordinates':'All local TikZ paths use x=0.01cm and y=-0.01cm, a fixed source origin, and an explicitly declared drawing rectangle. Observed locus boxes are recorded separately from path control points, rectangles and font extents. Inline text uses base-west anchors with zero inner and outer separation. M03 uses the explicitly declared (47,3) translation from outer origin (1145,1624), with its own fixed inner baseline. Coordinate choices and paths are manual visual approximations; no curve-extrema, fitting or image-difference computations were performed.',
  'scope_of_validation':'Direct structural source checks and a complete joint read of reading.tex and report.json are required before return. No compiler, renderer, OCR, external research, package installation or delegated reading was used.'
 },
 notation=[
  dict(location='Opening and two upper equalities',written='Signed Sigma with separate closure rules; dotted i indices',latex=r'\Sigma_i^+,\Sigma_i^-,E_i,\overline{\Sigma_i^+},\overline{\Sigma_i^-}'),
  dict(location='Opening abbreviation',written='comp. conn. with the two points',latex='comp. conn.'),
  dict(location='Third equality',written='Separate upper rule over Sigma_12',latex=r'\overline{\Sigma_{12}}'),
  dict(location='Soit line and lower partition display',written='Squared joins with extended foot',latex=r'J\amalg\{i\}; E_j\amalg\coprod'),
  dict(location='Main partition display',written='Product-shaped large sign, alpha lower limit, pi with lowered small ring',latex=r'\coprod_{\alpha\in\pi_0(X\setminus E_j)}'),
  dict(location='Lower names',written='Capital J and smaller j as separate indices, small raised rings',latex=r'\Pi_J^{\unsure{\circ|0}},\Pi_{J,j}^{\circ}'),
  dict(location='Three lower indexed unions',written='First and last open cups; middle cup has a short internal transverse stroke',latex=r'\bigcup_{j\in J}; G06_{j\in J};\bigcup_{j\in J}'),
  dict(location='Archive lower left',written='Pencilled 16',latex='% archive sheet number: 16')
 ],
 check_events=[],
 crops=json.loads((DEST/'crop_log.json').read_text()),
 graphics=graphics,
 processing_events=[
  dict(type='image metadata read',inputs=['J81-02_81_scan017.jpg','J81-02_81_scan017_a.jpg','J81-02_81_scan017_b.jpg'],results={'full':[1685,2363],'a':[1685,1261],'b':[1685,1262]},scope='PIL image size metadata only'),
  dict(type='required half-coordinate mapping',inputs={'full_height':2363,'half_b_height':1262},mapping='y_full = y_b + (2363 - 1262) = y_b + 1101; x_full = x_b. Half a has zero offset.',scope='Coordinate translation for recorded locations; no image alignment or pixel comparison.'),
  dict(type='required crop preparation',scripts=['crop_reader.py','crop14_reader.py'],inputs='The original full JPEG and the fourteen fixed crop rectangles in crops.',operations='PIL crop; RGB conversion; autocontrast; crop05 rotated -45 degrees with BICUBIC and expand=True; every result enlarged fourfold with LANCZOS; no sharpening.',results='Exact pre-resize/output dimensions, rotations and boxes are in crops and crop_log.json.',scope='Reading aids only; no OCR, recognition, numerical image comparison or geometry fitting.'),
  dict(type='report serialization',script='build_report.py',scope='Serializes manually entered transcription observations and source-row mapping into report.json; performs no mathematical check.'),
 ],
 brief_feedback=[
  'The source doubt row for an actual transverse stroke can be resolved as to stroke presence while a local graphical qualification retains its unestablished mathematical role; the report records those two scopes separately.',
  'Small detached pieces can coincide with a dotted letter interpretation. M03 is drawn once with a dotless j node and an explicit local role qualification; no extra operation is supplied.',
  'H has a terminal marginal ill placeholder and an internal body ill placeholder. Each receives one physical-parent entry; the marginal predecessor and the absence of further marginal words are kept together.'
 ],
 final_validation=None
)
(DEST/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote report.json from the current independent observations.')
