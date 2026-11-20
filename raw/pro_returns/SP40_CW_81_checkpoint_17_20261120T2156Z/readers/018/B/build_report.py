from pathlib import Path
import json

P=Path('/workspace/scratch/94548b74fbe0/out/readers/018/B')
diffs=[]
def d(i,loc,C,H,reading,evidence,confidence='medium',kind='other',dc=False,dh=False,status=None,crop=None,bbox=None,row=None,parent=None,**extra):
    o={'id':i,'location':loc,'C':C,'H':H,'reading':reading,'evidence':evidence,'confidence':confidence,'kind':kind,'diff_C':dc,'diff_H':dh,'C_doubt_status':status,'readers_crop':crop,'bbox':{'space':'original full scan; top-left origin','xyxy':bbox} if bbox else None}
    if row:o['C_source_doubt_row']=row
    if parent:o['physical_parent']=parent
    o.update(extra)
    diffs.append(o)

d('B01','opening dernière',r'\unsure{dernière}','dernière','dernière','Looped d, low r/n joins, separate i dot and descending-right grave, followed by the comma; reading resolved locally.',dc=True,status='resolved',crop='crop01_opening.png',bbox=[224,58,793,165],row='C18-R01')
d('B02','parenthesis after verra',r'\unsure{récurrence}','récurrence',r'\unsure{rècurrence|récurrence}','The word remains compressed. The small detached accent has a descending-right hook; grave is the selected visible candidate, acute remains supported. No spelling repair is made.',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,status='retained',crop='crop02_recurrence.png',bbox=[440,165,1060,285],row='C18-R02',qualification='H survives as the second candidate; this is a qualified reading difference.')
d('B03','l’ens des classes',r"l'\unsure{ens}",r"l'ens.\ des classes",'l’ens','Three joined letters and a long hooked final stroke are followed by clean intervening space; no abbreviation point appears.',confidence='high',kind='other',dc=True,dh=True,status='resolved',crop='crop03_ens.png',bbox=[373,280,810,373],row='C18-R03')
d('B04','word following raised (unique)',r'\unsure{de|des}','des',r'\unsure{des|de}','The low run has a final hooked continuation resembling s; the endpoint also permits de. Primary order reversed from C without resolving the doubt.',kind='misread word',dc=True,status='retained',crop='crop04_unique.png',bbox=[1080,530,1195,590],row='C18-R04')
d('B05','between de/des and classes','ces $n$','[omitted]','ces $n$','A distinct ces group appears under the long descender from que, followed by a separate n before the next physical line classes.',confidence='high',kind='omission',dh=True,crop='crop04_unique.png',bbox=[1260,527,1480,591])
d('B06','raised (unique), guide G01',r"l'une \inserted{(unique)}",r"l'une \add{(unique)}",'Same insertion, with the full bent guide','The guide begins below/left of de/des, bends upward beneath (unique), and ends with an upturned right end. Current witnesses encode the insertion but omit this independent path.',confidence='high',kind='drawing or diagram',dc=True,dh=True,crop='crop04_unique.png',bbox=[1080,490,1284,565],parent='unique-insertion')
d('B07','upper quoted word',"``composante''",'“composante”',r"``\unsure{composante|composant}''",'The long terminal curved return supports composante; attachment of that return to t leaves composant available. Both opening and closing quote pairs were seen.',kind='other',dc=True,crop='crop05_upper_quote.png',bbox=[976,754,1324,832],qualification='Same primary as H; a changed editorial uncertainty qualification alone supplies no H collation count.')
d('B08','before les deux composantes',r'\unsure{considérons}','considérons','considérons','The separate acute, looped d, and the final low ons run with its hook are recoverable.',dc=True,status='resolved',crop='crop06_considerons.png',bbox=[942,906,1229,975],row='C18-R05')
d('B09','lemma, mark after subscript J',r'\deleted{\unsure{i|j|,}}','[omitted]',r'\unsure{\deleted{j}|\deleted{i}|\deleted{,}|j}','The small dark form has a descending shaft, leftward lower return and crowded transverse upper stroke. Cancelled j is selected; cancelled i/comma and a live j remain possible. Glyph and state remain separate uncertainties.',confidence='low',kind='omission',dc=True,dh=True,status='retained',crop='crop07_lemma_pi.png',bbox=[1298,1220,1328,1261],row='C18-R06a',parent='lemma-Pi')
d('B10','lemma raised ring',r'\unsure{\circ|0}','0',r'\unsure{\circ|0}','Small closed raised ring with a white centre. Circle is the primary shape candidate and zero is retained.',kind='misread symbol or index',dh=True,status='retained',crop='crop07_lemma_pi.png',bbox=[1268,1169,1295,1202],row='C18-R06b',parent='lemma-Pi',qualification='H zero remains an explicit alternative; no conclusive error is claimed.')
d('B11','lemma underline and left rule, G02',r'\uline{Lemme}; tabular left rule',r'\emph{Lemme}; no left rule','One underline and a left rule starting below the first textual line','Underline extends from approximately (308,1275) to (550,1258). The separate left line runs from approximately (255,1247) to (259,1385), beginning beside the underline region rather than above Lemme. The full lemma is represented once.',confidence='high',kind='drawing or diagram',dc=True,dh=True,bbox=[244,1190,562,1395],source_location='half b, bbox [244,89,562,294]; y_full=y_b+1101',qualification='H emph and the single underline agree; the H difference is the left rule. C difference is the observed placement/endpoints of the generic table rule.')
d('B12','lemma endpoint','no full stop','full stop','no full stop','Space after the final Sigma_i^- on the supplied lower half contains no detached sentence point.',confidence='high',kind='text not on the page',dh=True,bbox=[1524,1268,1654,1387],source_location='half b, bbox [1524,167,1654,286]')
d('B13','proof opening Dire',r'\unsure{Dire}','Dire','Dire','Large worked-over D, separate i stroke/dot, and the low re termination are legible. Lower loops belong to the worked-over D; no independent predecessor character is recovered.',dc=True,status='resolved',crop='crop08_dire.png',bbox=[1408,1383,1528,1461],row='C18-R07')
d('B14','qu’une/la correction, guide G03a',r'\deleted{la}\inserted{qu’une}',r'\add{qu’une}\struck{la}','Same words and states, full connected hooked guide','The guide touches the lower-left insertion point, rises across the l ascender region and continues beneath qu’une to a hooked right endpoint.',confidence='high',kind='drawing or diagram',dc=True,dh=True,crop='crop09_insertions.png',bbox=[242,1494,430,1585],parent='proof-insertions')
d('B15','inserted U subscript',r'U_{\unsure{\alpha|x}}',r'U_\alpha',r'U_{\unsure{\alpha|x}}','A small lower loop with a crossing rightward stroke supports alpha; the crossing alone permits x.',status='retained',crop='crop09_insertions.png',bbox=[730,1474,799,1522],row='C18-R08a',parent='proof-insertions')
d('B16','raised Pi in proof insertion',r'\Pi_J^\circ',r'\Pi_J^0',r'\Pi_J^\circ','The second raised ring was separately inspected. Its loop is small and crowded at upper left. Circle/zero uncertainty remains in the record; the first occurrence bears the printed qualifier.',kind='misread symbol or index',dh=True,crop='crop09_insertions.png',bbox=[893,1456,962,1511],parent='proof-insertions',qualification='H zero is retained as an alternative; repeated-glyph printing follows the brief.')
d('B17','apparent comma after inserted U_alpha',r'U_\alpha, de',r'U_\alpha de',r'U_\alpha de','The small hooked form at this position continues directly into the long guide G03b; it supplies no separate punctuation locus. It is drawn once as part of that guide.',confidence='high',kind='text not on the page',dc=True,crop='crop09_insertions.png',bbox=[802,1495,827,1522],parent='proof-insertions')
d('B18','guide beneath U_alpha de Pi, G03b','no guide path','no guide path','One connected guide with its small upper-left hook','Lower-left end begins before ne, rises to the hook beside de, then curves downward and rises to the upper-right endpoint beyond Pi. Two source path commands meet at the same hook/guide point.',confidence='high',kind='drawing or diagram',dc=True,dh=True,crop='crop09_insertions.png',bbox=[753,1482,1017,1559],parent='proof-insertions')
d('B19','H struck un after the raised name','no additional struck word',r'\struck{un}','no additional struck un','Only the live ne group occurs below the raised label. The stroke above/beside it is the connected insertion guide; no second crossed word is supported.',confidence='high',kind='text not on the page',dh=True,crop='crop09_insertions.png',bbox=[754,1492,871,1564],parent='proof-insertions')
d('B20','older form within corrected E_i',r'\deleted{\unsure{\Sigma}}','[omitted]',r'\deleted{\Sigma}','The surviving internal upper and lower obliques form the angular predecessor beneath the heavy E upright and lower arm. Sigma is resolved locally.',kind='omission',dc=True,dh=True,status='resolved',crop='crop10_corrected_Ei.png',bbox=[1303,1503,1367,1557],row='C18-R09a',parent='corrected-Ei')
d('B21','separate rule above corrected E_i, G04',r'\unsure{\overline{E_i}|E_i}',r'E_i','E_i with a locally qualified literal upper stroke','Two separated upper horizontal runs are visible: the lower belongs to the corrected capital head; the upper has a small retraced/returning right end. Upper-stroke presence is clear. Its closure-bar or overwritten-remnant role and exact hand remain unresolved; the stroke is kept once regardless of interpretation.',confidence='low',kind='drawing or diagram',dc=True,dh=True,status='retained',crop='crop10_corrected_Ei.png',bbox=[1316,1490,1380,1514],row='C18-R14',parent='corrected-Ei',shape_confidence='high',qualification='This is the independent actual C bar doubt, not an instantiated example from S. The source renders a qualified graphical overmark rather than selecting an algebraic closure operation.')
d('B22','before il existe','que il',"qu'il",'que il','The e-ending of que remains written before the separate i/l strokes. No elision is supplied.',confidence='high',kind='abbreviation expanded or spelling modernised',dh=True,bbox=[1025,1598,1391,1747],source_location='half b, bbox [1025,497,1391,646]')
d('B23','after tel que','le','la','le','Looped l is followed by a short low e-form, without a separate a bowl.',confidence='high',kind='misread word',dh=True,bbox=[815,1734,893,1822],source_location='half b, bbox [815,633,893,721]')
d('B24','older form within corrected E_j',r'\deleted{\unsure{\Sigma}}','[omitted]',r'\deleted{\Sigma}','Thin angular interior strokes survive inside the heavier corrected E. Sigma is independently recovered at this second locus.',kind='omission',dc=True,dh=True,status='resolved',crop='crop11_formula_choisi.png',bbox=[1275,1730,1326,1779],row='C18-R09b',parent='corrected-Ej')
d('B25','subscript of corrected E_j',r'E_{\unsure{j|J}}',r'E_j',r'E_{\unsure{j|J}}','The index is a nearly straight descending stroke with a small lower left hook and no securely detached dot or top bar. Lowercase j remains primary; J remains possible. No neighbouring formula supplies the reading.',confidence='low',status='retained',crop='crop11_formula_choisi.png',bbox=[1308,1757,1333,1811],row='C18-R09c',parent='corrected-Ej')
d('B26','crossed word after right parenthesis',r'\deleted{\unsure{choisi}}',r'\struck{choisie}',r'\deleted{\unsure{choisi|choisie}}','Tall h, low o/s shapes and dotted strokes survive the horizontal cancellation. No separate final e is secure, but cancellation leaves choisie possible.',kind='misread word',dh=True,status='retained',crop='crop11_formula_choisi.png',bbox=[1406,1712,1576,1793],row='C18-R10',parent='choisi-points',qualification='H survives as an alternative; C primary and unresolved status are retained.')
d('B27','two additional right/upper points beside crossed choisi, G05','[omitted]','[omitted]','Two locally qualified graphical points','Beyond the final dotted-letter group, two small distinct dark points rise diagonally to the right. The selected source draws only this additional pair, once. Their role, attachment, hand and surface origin remain unassigned.',confidence='low',kind='omission',dc=True,dh=True,crop='crop11_formula_choisi.png',bbox=[1567,1735,1591,1762],parent='choisi-points',shape_confidence='medium')
d('B28','quoted word in proof',r'\unsure{composant|composante}','composante',r'\unsure{composant|composante}','The t has a short rightward crossing/return and no separately secure final e. The crossing can conceal an ending; the original alternatives remain.',kind='misread word',dh=True,status='retained',crop='crop12_lower_quote.png',bbox=[237,1892,584,1979],row='C18-R11',qualification='Qualified primary difference; H survives as the alternative.')
d('B29','verb after crossed est',r'\deleted{est} est',r'\struck{est} soit',r'\deleted{est} est','The live form has a small initial loop followed by s/t strokes; there is no separate oi group. The preceding est has a distinct horizontal cancellation.',confidence='high',kind='misread word',dh=True,crop='crop13_live_est.png',bbox=[1204,1849,1479,1922])
d('B30','accent within l’élément','élément','élément',r'\unsure{élêment|élément}','The second detached accent is angular, with two apparent arms. Circumflex is selected, while a hooked acute remains possible. The first accented e is retained from its faint short raised stroke.',kind='abbreviation expanded or spelling modernised',dc=True,dh=True,crop='crop14_element_du.png',bbox=[262,2003,493,2083],qualification='The familiar spelling survives as an explicit alternative; this is a local paleographic doubt.')
d('B31','article before the next pi_zero','du','de','du','After the looped d, the remaining run has the low u trough and rising termination.',confidence='high',kind='misread word',dh=True,crop='crop14_element_du.png',bbox=[528,2008,620,2067])
d('B32','raised (soit Sigma_i^-), guide G06',r'\inserted{(soit $\Sigma_i^-$)}',r'\add{(soit $\Sigma_i^-$)}','Same insertion and full bent/hooked guide','The guide rises from the gap between éléments and de, sweeps over the d ascender and ends in a small right hook. The adjoining éléments and de occur once in the selected source.',confidence='high',kind='drawing or diagram',dc=True,dh=True,crop='crop15_soit_guide.png',bbox=[555,2192,657,2258],parent='soit-insertion')
d('B33','crossed word below card I=2',r'\deleted{\unsure{deux}}','[omitted]',r'\deleted{\unsure{deux}}','A low initial loop/ascender and small rises remain under the strong line. The full word cannot be recovered with confidence; deux stays qualified. The physical page edge is inside the crop.',confidence='low',kind='omission',dh=True,status='retained',crop='crop16_bottom_corrections.png',bbox=[390,2299,560,2337],row='C18-R12',parent='cas-correction')
d('B34','raised card I=2',r'\inserted{\operatorname{card}I=2}',r'\operatorname{card}I=2',r'\inserted{\operatorname{card}I=2}','The expression is physically above the crossed word. The selected G07 keeps that placement, and retains the cancellation rule once.',confidence='high',kind='insertion or placement',dh=True,crop='crop16_bottom_corrections.png',bbox=[382,2268,565,2337],parent='cas-correction')
d('B35','cancelled form before fortiori',r'\deleted{\unsure{OK|cela}}',r'\struck{et}',r'\deleted{\unsure{OK|cela|et}}','A dark loop and tall angled strokes remain under crossing strokes. OK is the selected visible candidate; cela and et remain possible because cancellation obscures the joins.',confidence='low',kind='misread word',dh=True,status='retained',crop='crop16_bottom_corrections.png',bbox=[652,2269,804,2340],row='C18-R13a',qualification='H et survives as a supported alternative, not a conclusively rejected reading.')
d('B36','accent before fortiori',r'\unsure{â|à}','à',r'\unsure{â|à}','The detached upper mark is roof-like; a short bent grave remains possible. The long return immediately below belongs to the a form and is not supplied as a second detached mark.',confidence='low',kind='misread word',dh=True,status='retained',crop='crop16_bottom_corrections.png',bbox=[827,2280,884,2337],row='C18-R13b',qualification='H à survives as the alternative.')
d('B37','final U subscript',r'U_\alpha',r'U_\alpha',r'U_\alpha','Separately viewed low hook/crossing form supports alpha with x still possible. The original compound row explicitly relates this repetition to the inserted form. First-occurrence printing puts the qualifier at B15; this local uncertainty remains in the record.',status='retained',crop='crop17_final.png',bbox=[1213,2300,1248,2335],row='C18-R08b')
d('B38','final OK and rising transverse stroke, G08','live OK','live OK','Qualified whole OK graphic; live/cancelled state unresolved','A thin rising diagonal traverses the upper O/K region and reaches above the right side. It may belong to the letter construction or cancel the word. The glyphs and period remain clear. The literal diagonal is drawn once, with a local uncertainty wrapper and invisible deletion annotation.',confidence='low',kind='deletion state (struck given live or live given struck)',dc=True,dh=True,crop='crop17_final.png',bbox=[1444,2258,1575,2341],shape_confidence='high',qualification='Live OK is primary and the cancelled state is an alternative; no cancellation chronology or mathematical endorsement is inferred.')

rowmap=[
 ('C18-R01','opening word group',['B01']),
 ('C18-R02','first parenthesis',['B02']),
 ('C18-R03','l’ens des classes',['B03']),
 ('C18-R04','after (unique)',['B04']),
 ('C18-R05','before les deux composantes',['B08']),
 ('C18-R06','lemma Π: cancelled following sign; upper circle',['B09','B10']),
 ('C18-R07','proof opening',['B13']),
 ('C18-R08','added name after donnée; final repetition expressly mentioned in the source row',['B15','B37']),
 ('C18-R09','under E_i and E_j; index of latter',['B20','B24','B25']),
 ('C18-R10','struck word after right parenthesis',['B26']),
 ('C18-R11','quoted word in proof',['B28']),
 ('C18-R12','after bottom cas',['B33']),
 ('C18-R13','before fortiori: cancelled word; accent',['B35','B36']),
 ('C18-R14','bar over corrected E_i',['B21']),
]

doubts=[]
for ids,loc,reading,alts,conf,reason,crop in [
 (['B02'],'first parenthesis','rècurrence',['récurrence'],'medium','Compressed body; short accent hook does not settle its intended direction.','crop02_recurrence.png'),
 (['B04'],'after (unique)','des',['de'],'medium','Long final hook can belong to either ending.','crop04_unique.png'),
 (['B07'],'upper quoted word','composante',['composant'],'medium','Terminal curved return can belong to t or to an e ending.','crop05_upper_quote.png'),
 (['B09'],'mark after lemma J','cancelled j',['cancelled i','cancelled comma','live j'],'low','Crowded crossing and lower hook leave both glyph and state open.','crop07_lemma_pi.png'),
 (['B10'],'lemma raised ring','circle',['zero'],'medium','Small closed ring supplies no stronger character determination.','crop07_lemma_pi.png'),
 (['B15'],'inserted U index','alpha',['x'],'medium','Loop/crossing remains ambiguous.','crop09_insertions.png'),
 (['B16'],'inserted raised Pi ring','circle',['zero'],'medium','Second loop separately seen; first occurrence carries printed doubt.','crop09_insertions.png'),
 (['B21'],'upper stroke over corrected E_i','closure-like upper rule',['surviving overwritten pen stroke'],'low','Stroke is visible; role and hand are unsettled.','crop10_corrected_Ei.png'),
 (['B25'],'corrected E index','j',['J'],'low','Undotted descending stem with small hook.','crop11_formula_choisi.png'),
 (['B26'],'crossed word','choisi',['choisie'],'medium','Cancellation conceals the final join.','crop11_formula_choisi.png'),
 (['B27'],'extra point pair','two graphical points',['unestablished letter/mark attachment'],'low','Shape is retained, but role, hand and surface origin are unassigned.','crop11_formula_choisi.png'),
 (['B28'],'lower quoted word','composant',['composante'],'medium','Short t return does not securely settle a final e.','crop12_lower_quote.png'),
 (['B30'],'l’élément accent','élêment',['élément'],'medium','Angular second accent can also be a hooked acute.','crop14_element_du.png'),
 (['B33'],'crossed bottom word','deux',[],'low','The long cancellation covers most of the low letters.','crop16_bottom_corrections.png'),
 (['B35'],'cancelled form before fortiori','OK',['cela','et'],'low','Overlapping loops and diagonals conceal the word skeleton.','crop16_bottom_corrections.png'),
 (['B36'],'accent before fortiori','â',['à'],'low','Roof-like short mark can also be a bent grave.','crop16_bottom_corrections.png'),
 (['B37'],'final U index','alpha',['x'],'medium','Independently inspected recurrence, printed with the first candidate under the recurring-glyph rule.','crop17_final.png'),
 (['B38'],'final OK state','live OK',['cancelled OK'],'low','The rising diagonal may be part of the letters or a cancellation.','crop17_final.png'),
]:doubts.append({'difference_ids':ids,'location':loc,'reading':reading,'alternatives':alts,'confidence':conf,'reason':reason,'crop':crop})

inventory=[]
def inv(e,k,pos,first,hand='his hand',**extra):
    inventory.append({'sheet_kind':'text','hand':hand,'element':e,'kind':k,'position':pos,'first_words_or_objects':first,'transcribed':'yes',**extra})
inv('018.01','text','upper three physical lines','cette dernière, si card J')
inv('018.02','text','Ceci posé paragraph, through X setminus E_i','Ceci posé, on voit d’abord')
inv('018.03','insertion','above l’une / des-or-de ces n','(unique)')
inv('B.G01','drawing','under raised (unique)','one bent guide; endpoints (1089,559), (1278,498)',components=['G01'])
inv('018.04','text','lemma, two physical lines','Lemme Toute classe de Pi')
inv('B.G02','drawing','lemma underline and left edge','single underline; separate partial-height left rule',components=['G02-underline','G02-left-rule'])
inv('018.05','deletion','after lemma subscript J','qualified cancelled j/i/comma; live j alternative',state='cancellation primary, live alternative')
inv('018.06','text','proof through final OK','C’est presque une tautologie')
inv('018.07','deletion','under qu’une','la')
inv('018.08','insertion','above crossed la','qu’une')
inv('B.G03a','drawing','between qu’une and crossed la','one long hooked guide')
inv('018.09','insertion','above donnée / ne contient','U_alpha-or-x de Pi_J with raised ring; no independent comma')
inv('B.G03b','drawing','under raised U/Pi label','main guide and its connected upper-left hook',components=['G03b-main','G03b-hook'])
inv('018.10','deletion','within corrected E_i after pas','Sigma predecessor, resolved')
inv('B.G04','drawing','above corrected E_i','one upper rule with retraced right return, locally qualified','undetermined hand',role='closure/remnant unassigned')
inv('018.11','deletion','within corrected E_j','Sigma predecessor, resolved')
inv('018.12','deletion','after pi_zero right parenthesis','choisi / choisie')
inv('B.G05','drawing','right/above crossed choisi','two additional points, locally qualified','undetermined hand',components=['G05-point1','G05-point2'],role='attachment, role and surface origin unassigned')
inv('018.13','deletion','after de cette classe','est; followed by live est')
inv('018.14','insertion','above gap between éléments and de','(soit Sigma_i^-)')
inv('B.G06','drawing','under raised (soit Sigma_i^-)','one bent guide with right hook')
inv('018.15','deletion','bottom beneath card I=2','qualified deux, actual cancellation path G07',components=['G07-cancellation'])
inv('018.16','insertion','above crossed deux','card I=2')
inv('018.17','deletion','between bottom comma and accented a','qualified OK / cela / et')
inv('B.G08','drawing','final OK','OK plus rising diagonal, whole state qualified','undetermined hand',role='letters are in his hand; attribution/function of transverse stroke unestablished')
inv('B.ARCH','text','bottom-left paper edge','archive sheet number 17, comment only','undetermined hand')

graphics=[
 {'id':'G01','source_anchor':'% G01:','observed_bbox':[1080,490,1284,565],'origin':[820,465],'drawing_rectangle':[0,0,670,145],'units':'.08 mm per declared x/y source unit; y down','baseline':[0,115],'paths':['(1089,559) C(1075,521)(1137,517)(1202,516) C(1240,511)(1271,507)(1278,498)'],'words_once':['l’une','(unique)','des|de','ces','n'],'difference_ids':['B04','B05','B06']},
 {'id':'G02','source_anchor':'% G02:','observed_bbox':[244,1145,1645,1395],'origin':[244,1145],'drawing_rectangle':[0,0,1400,255],'units':'.085 mm; y down','baseline':[0,238],'paths':['underline: (308,1275) C(390,1270)(471,1264)(550,1258)','left rule: (255,1247) C(256,1290)(257,1340)(259,1385)'],'words_once':['whole lemma'],'difference_ids':['B09','B10','B11','B12']},
 {'id':'G03','source_anchor':'% G03:','observed_bbox':[242,1482,1017,1585],'origin':[225,1465],'drawing_rectangle':[0,-28,925,140],'units':'.08 mm; y down','baseline':[0,111],'paths':['G03a: (271,1580) C(279,1551)(307,1541)(343,1538) C(376,1535)(414,1527)(423,1517) C(426,1512)(418,1510)(414,1513)','G03b main: (760,1553) C(759,1538)(794,1517)(813,1510) C(838,1511)(861,1528)(891,1525) C(938,1521)(992,1501)(1011,1488)','G03b hook: (813,1510) C(823,1501)(817,1498)(811,1501)'],'words_once':['la, deleted','qu’une, inserted','classe donnée','U_alpha-or-x de Pi_J ring, inserted','ne contient'],'difference_ids':['B14','B15','B16','B17','B18','B19']},
 {'id':'G04','source_anchor':'% G04:','observed_bbox':[1316,1490,1380,1514],'origin':[1308,1480],'drawing_rectangle':[0,0,85,85],'units':'.08 mm; y down','baseline':[0,67],'nested_mark_origin':[1324,1492],'nested_rectangle':[0,0,55,12],'nested_baseline':[0,12],'nested_node_anchor':'base west, zero inner/outer separation, at outer (16,24)','paths':['local mark: (0,6) C(17,5)(34,6)(47,6) L(31,10) L(43,6)'],'words_once':['Sigma predecessor before E_i under the given convention','E_i'],'difference_ids':['B20','B21']},
 {'id':'G05','source_anchor':'% G05:','observed_bbox':[1567,1735,1591,1762],'origin':[1408,1712],'drawing_rectangle':[0,0,190,100],'units':'.07 mm; y down','baseline':[0,70],'nested_mark_origin':[1569,1737],'nested_rectangle':[0,0,20,22],'nested_baseline':[0,22],'nested_node_anchor':'base west, zero inner/outer separation, at outer (161,47)','paths':['fill circle centre (5,16), radius 1.2','fill circle centre (10,6), radius 1.2'],'words_once':['crossed choisi|choisie'],'difference_ids':['B26','B27']},
 {'id':'G06','source_anchor':'% G06:','observed_bbox':[555,2192,657,2258],'origin':[251,2160],'drawing_rectangle':[0,0,470,126],'units':'.08 mm; y down','baseline':[0,95],'paths':['(560,2251) C(563,2228)(599,2215)(646,2205) C(655,2202)(653,2199)(647,2197)'],'words_once':['éléments','(soit Sigma_i^-), inserted','de'],'difference_ids':['B32']},
 {'id':'G07','source_anchor':'% G07:','observed_bbox':[382,2268,565,2337],'origin':[382,2265],'drawing_rectangle':[0,0,190,80],'units':'.08 mm; y down','baseline':[0,59],'paths':['(395,2325) C(443,2318)(509,2322)(556,2318)'],'words_once':['deux, visible once via rlap plus invisible deleted dimensional copy','card I=2, inserted'],'difference_ids':['B33','B34'],'source_choice':'Literal cancellation replaces the visible generic deleted stroke; cancellation state is unchanged from C.'},
 {'id':'G08','source_anchor':'% G08:','observed_bbox':[1444,2258,1575,2341],'origin':[1450,2255],'drawing_rectangle':[0,0,95,85],'units':'.08 mm; y down','baseline':[0,70],'paths':['(1452,2293) C(1470,2287)(1497,2279)(1534,2264)'],'words_once':['OK, visible once via rlap; invisible deleted dimensional copy'],'difference_ids':['B38'],'source_choice':'Whole local unsure marks live/cancelled alternatives. Period remains outside the graphic.'},
]

s_loci=[]
for loc,box,reading,view,detail in [
 ('definition U_J,i',[295,790,480,914],r'U_{J,i}','half a','No detached rule above the U.'),
 ('upper positive Sigma',[1014,990,1155,1089],r'\Sigma_i^+','half a','Single Sigma head and angular body; separate plus.'),
 ('upper negative Sigma',[1198,989,1314,1084],r'\Sigma_i^-','half a','Single head with a separate upper-right minus.'),
 ('lemma U_J,i',[424,1303,596,1403],r'U_{J,i}','half b','No upper rule above the U.'),
 ('lemma positive Sigma',[1336,1265,1442,1353],r'\Sigma_i^+','half b','Head, angular body and separate plus individually seen.'),
 ('lemma negative Sigma',[1521,1265,1641,1353],r'\Sigma_i^-','half b','Head and separate right minus; no second independent head rule.'),
 ('inserted U_alpha',[729,1468,800,1528],r'U_\alpha','crop09_insertions.png','Its below/right guide is separately preserved; no closure stroke above U.'),
 ('unequal U_J,i',[350,1620,499,1734],r'U_{J,i}','half b','No independent upper rule.'),
 ('proof positive Sigma_j',[957,1734,1053,1842],r'\Sigma_j^+','crop11_formula_choisi.png','Detached/slightly offset head above the zigzag is read as the Sigma head; no second independent head rule is established.'),
 ('inserted negative Sigma_i',[515,2157,646,2232],r'\Sigma_i^-','crop15_soit_guide.png','Head meets the upper diagonal; right minus separate. Guide lies below the whole insertion.'),
 ('Sigma_i in lower pi argument',[874,2190,961,2257],r'\Sigma_i','half b','Single angular capital with head and low i; retained without mathematical repair.'),
 ('final U_alpha',[1159,2269,1250,2340],r'U_\alpha','crop17_final.png','No detached upper rule above U.'),
 ('final negative Sigma_i',[1301,2258,1400,2340],r'\Sigma_i^-','crop17_final.png','One detached head above the shallow upper diagonal; separate right minus. No additional closure rule is established.'),
]:s_loci.append({'location':loc,'bbox':box,'reading':reading,'view':view,'observation':detail,'S_status':'No matching S example instantiated; current plain C/H reading retained at this independently inspected locus.'})
s_loci.append({'location':'corrected E_i upper rule','bbox':[1316,1490,1380,1514],'view':'crop10_corrected_Ei.png','observation':'Separate upper stroke visibly confirmed; closure/remnant role retained uncertain.','S_status':'Independent C18-R14 locus; S examples concern Sigma/U and do not determine this E stroke.','difference_id':'B21'})

crops=json.loads((P/'crop_manifest.json').read_text())
for c in crops:c['viewed']=True;c['successful_visual_deliveries']=1
(P/'crop_manifest.json').write_text(json.dumps(crops,ensure_ascii=False,indent=2)+'\n')

report={
 'scan':18,'reader':'B','start_utc':'2026-11-20 18:24:23 UTC','visual_pass_end_utc':'2026-11-20 19:07:25 UTC','end_utc':None,
 'full_image_viewed':True,'halves_viewed':True,'complete_visual_read':True,
 'differences':diffs,'doubts':doubts,'inventory':inventory,
 'notes':[
   {'topic':'page content','text':'Opening continuation, a Ceci posé paragraph, an underlined Lemme with a separate left rule, and its densely corrected proof. No independent diagram or mathematical display; formulas are within prose.'},
   {'topic':'author uncertainty','text':'No lexical assertion of uncertainty such as peut-être is supplied on this page. The author writes OK at the conclusion; its transverse stroke has an unresolved state. The cancelled form earlier in the line remains uncertain. Reading the written OK is not a proof check.'},
   {'topic':'title/date/page counts','text':'Lemme is underlined. No date or independent manuscript page-number heading was seen. Archive 17 appears at lower left and is a comment only. H page{17} is treated as its editorial page marker.'},
   {'topic':'mathematics-led decisions','text':'No formula was repaired, proved, recomputed or used to determine an unclear glyph. The written X setminus Sigma_i and que il remain. H’s note proposing E_i for Sigma_i is apparatus; it adds no manuscript occurrence.'},
   {'topic':'compound C rows','text':'Fourteen original doubtful-reading rows retain their source identities. R06, R08, R09 and R13 are split into independently reported local parts. R14 remains independent of R09 even though the crop is shared. Notation, Slips retained and Abbreviations tables are not counted as extra doubt rows.'},
   {'topic':'abbreviations','text':'card, ens, i.e. and OK remain unexpanded. The period after ens supplied by H is absent; the two points of i.e. are seen.'},
   {'topic':'source representation','text':'All free graphic groups use fixed local origins, baseline coordinates, base-west text nodes and zero inner/outer node separation. Paths are manual approximations of viewed ink. Font extents and rendered fit were not measured or validated.'},
   {'topic':'visible duplication safeguards','text':'The comma-like hook after inserted U belongs to G03b; no comma is separately printed. The guide does not supply H’s additional struck un. éléments and de are included in G06 once. The point pair G05 is additional to the dotted-letter group. Final OK and bottom deux use visible rlap text with invisible deletion-dimensional copies; no generic additional cancellation is drawn there.'},
   {'topic':'crop bounds','text':'Every planned target’s guide endpoints and deciding ink were included. Neighbouring non-target text can meet crop boundaries. Bottom crops include the physical paper edge; the fortiori f descender reaches that physical edge. No unseen extension is supplied, and no target was reopened or recropped.'},
 ],
 'notation':[
   {'location':'opening cardinality formula','latex':r'\operatorname{card}J=\operatorname{card}I-1=n-1','evidence':'Small c in card, capitals J/I, separate equals and midline minuses.'},
   {'location':'repeated U_J,i','latex':r'U_{J,i}','evidence':'Capital J, comma and separate lowered i; checked at definition, lemma and unequal expression.'},
   {'location':'lemma and insertion','latex':r'\Pi_J^{\unsure{\circ|0}}','evidence':'Two hanging strokes below a head; small raised ring. Only first printed occurrence bears doubt.'},
   {'location':'inserted and final U','latex':r'U_{\unsure{\alpha|x}}','evidence':'Crossed/looped small form, separately inspected at both places; first occurrence qualified.'},
   {'location':'corrected E_i and E_j','latex':r'\deleted{\Sigma}E_i; \deleted{\Sigma}E_{\unsure{j|J}}','evidence':'Angular internal remnants survive the heavy E forms; second index stays uncertain.'},
   {'location':'proof and conclusion','latex':r'\ne;\in;\subset','evidence':'Crossed paired equal strokes, open membership form, and a single open inclusion bowl; no extra equality line supplied.'},
   {'location':'lower argument','latex':r'\pi_0(X\setminus\Sigma_i)','evidence':'Two pi legs with low zero, backslash, angular Sigma and low i; retained as written.'},
   {'location':'quoted prose','latex':"``...''",'evidence':'Paired ticks, sometimes joined, at both physical quotations.'},
   {'location':'upper E_i rule','latex':'G04 literal locally qualified stroke','evidence':'Separate upper horizontal with short retrace; shape retained without assigning closure semantics.'},
 ],
 'check_events':[],
 'crops':crops,
 'C_doubt_source_map':[{'source_row_id':i,'original_place':loc,'local_difference_ids':ids,'count_original_row_once':True} for i,loc,ids in rowmap],
 'graphical_components':graphics,
 'S_witness_review':{'source_row':'SA01-K81-06','source_author_viewed_scan':False,'source_span':'scans015–022','source_read':'packets/018/S_rows.json','page_examples_matched':[],'loci':s_loci,'conclusion':'No current-witness closure omission is inferred from S. The separate corrected-E_i stroke is reported independently, with its role unresolved.'},
 'report_silent_source_choices':[
   {'location':'opening formula and conclusion','choice':'All card letters, I/J, n, minus/equality signs and (n-1)+1=n are retained from the individually read upper half; no arithmetic verification was performed.'},
   {'location':'Ceci posé paragraph','choice':'Ceci posé, on voit d’abord que E_i est dans; classes, qui sont des ouverts. Soit; qui contient E_i; et; les deux composantes; de X setminus E_i; all retained after half reading, with the local doubts/differences separately reported.'},
   {'location':'lemma','choice':'Toute classe de; distincte de; est contenue dans; ou; same lexical text retained. Single underline agrees with H emph. Exact observed rule placement is B11.'},
   {'location':'proof first line','choice':'C’est presque une tautologie : retained, including the two separated colon points. Dire resolved at B13.'},
   {'location':'proof correction group','choice':'la is crossed and qu’une raised. classe donnée keeps its acute; ne contient remains live. H’s reversed macro ordering does not change the same physical attachment, so no separate order count.'},
   {'location':'i.e. and unequal expression','choice':'pas, i.e. est, ne U_J,i, comma, signifie, existe un, j in J, tel que and the full parenthesized pi expression are retained after visual reading. The inequality is literal, not prose expansion.'},
   {'location':'after lower quoted word','choice':'de cette classe and first crossed est retained; live est is B29. qui ne contient pas E_i and the following semicolon retained; no upper stroke on this later E_i is supplied.'},
   {'location':'last two physical lines','choice':'il est donc contenu dans l’un des; éléments; (soit Sigma_i^-); de; pi_0(X setminus Sigma_i), d’après l’étude du cas; fortiori; U_alpha subset Sigma_i^-; commas and terminal point retained. Every independent altered spelling and state is separately logged.'},
   {'location':'unreadable texture','choice':'Diffuse background gray texture and crop-edge pieces of adjoining letters were not assigned new characters. Connected lower loops of Dire remain within that glyph, with no independent predecessor invented.'},
   {'location':'archive/comment','choice':'Archive 17 is transcribed once in a TeX comment and added to the inventory; C inventory omitted that inventory item. This is an inventory completion, not a newly discovered textual numeral.'},
 ],
 'processing_provenance':{
   'read_scope':['complete brief_v16_scan018.md','complete PREAMBLE.tex','complete assigned C.tex and H.tex','metadata.json','C_doubts.txt','C_notes.txt','C_inventory.json','notation.md','later-supplied S_rows.json','three assigned images','supplied crop.py source','own B files'],
   'initial_order':'UTC clock and initial text reads were requested in one batch; start was not backdated. Aggregated text output was truncated, so the brief, preamble and packet texts were then read in separate successful complete deliveries before image reading.',
   'image_views':[{'path':'source/SP40_CW_81_scans/J81-02_81_scan018.jpg','purpose':'layout','successful_deliveries':1},{'path':'source/SP40_CW_81_scans/J81-02_81_scan018_a.jpg','purpose':'line-by-line upper half','successful_deliveries':1},{'path':'source/SP40_CW_81_scans/J81-02_81_scan018_b.jpg','purpose':'line-by-line lower half','successful_deliveries':1}],
   'full_dimensions':[1683,2363],'half_a_dimensions':[1683,1261],'half_b_dimensions':[1683,1262],
   'coordinate_mapping':'All report boxes are original-full-scan coordinates unless explicitly labelled. Half a uses zero offset. Half b is bottom-aligned: y_full=y_b+1101, from 2363-1262. No pixel-difference/alignment computation was performed.',
   'crop_processing':'One preplanned tight crop per unresolved locality; 17 total. Rotation 0. PIL autocontrast; aspect-preserving LANCZOS enlargement to the recorded widths, height=round(original_crop_height*output_width/original_crop_width); UnsharpMask radius 1.1, percent 120, threshold 3. Crops were each delivered and viewed once, separately.',
   'crop_script':'make_crops.py','report_script':'build_report.py','failed_image_deliveries':0,'reopened_successful_images':0,'recropped_targets':0,
   'actual_calculation_scope':['Image metadata dimensions were read. Half-b offset was obtained by the finite height subtraction 2363-1262=1101.','The crop script performed only the stated raster display resizing and filtering, with the exact source boxes and output dimensions in crops.','Source-coordinate maps and drawing paths are manual declarations; no curve extrema, font metrics, image comparison or geometric alignment check was performed.'],
   'prohibited_work_not_performed':['OCR/text recognition','internet/research','other-page viewing','other-reader/root-decision reads','delegation','TeX compilation','rendering','package installation','mathematical proof/computation checks','optional geometric/pixel-comparison checks'],
   'status_message':'Root reported an unexpected interrupted task status after crop03; execution continued from the same context. No image delivery had failed, and no successful view was repeated.',
   'structural_validation':'Pending final source-only check; no compilation or rendering is claimed.'
 },
 'brief_feedback':[
   'A visibly separate rule over a corrected capital can have a secure shape while its closure/remnant role remains unresolved. The selected source uses a local qualified graphical overmark to preserve the line once, with both interpretations retained in the record.',
   'The small hook adjacent to inserted U_alpha is connected to the guide; a punctuation transcription would duplicate that physical mark.',
   'The final OK permits live/cancelled state alternatives. The whole graphic is locally qualified; actual diagonal geometry is retained without an additional generic strike.',
 ],
}
(P/'report.json').write_text(json.dumps(report,ensure_ascii=False,indent=2)+'\n')
print('Wrote report.json and updated the existing crop manifest; no image reopened.')
