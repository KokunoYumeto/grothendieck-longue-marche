from pathlib import Path
import json, re
OUT=Path('/workspace/scratch/94548b74fbe0/out/readers/022/A')
UNIT='0.085mm'
lines=[r'\scanpage{22}',r'% Reader A independent proposed transcription. Manual geometry; source-only validation.',r'% Drawing coordinate system: original full scan, origin upper left; x right, y down.',r'% TikZ units x=0.085 mm, y=-0.085 mm; all inner scopes use the same units.',r'% Every visible label occurs once. Phantom copies retain editorial state without extra ink.',r'\figure{\begin{tikzpicture}[x=0.085mm,y=-0.085mm,baseline=0pt,',r'  every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt}]',r'\path[use as bounding box] (240,60) rectangle (1681,2095);']
groups=[]; nodes=[]
def add(s): lines.append(s)
def label(i,x,y,w,text,state=None,annotation=None):
    # Fixed base-west anchor. The resize width is a manual transcription dimension,
    # not an image alignment/metric validation.
    payload=text
    ann=annotation or text
    if state=='deleted': payload=r'\rlap{'+text+r'}\phantom{\deleted{'+ann+'}}'
    elif state=='inserted': payload=r'\rlap{'+text+r'}\phantom{\inserted{'+ann+'}}'
    elif state=='deleted inserted': payload=r'\rlap{'+text+r'}\phantom{\deleted{\inserted{'+ann+'}}}'
    mm=w*.085
    add(f'% LABEL {i}: owns exactly the visible contents of this node; state={state or "live"}.')
    add(r'\node at ('+f'{x},{y}'+r') {\resizebox{'+f'{mm:.3f}mm'+r'}{!}{'+payload+'}};')
    nodes.append({'id':i,'origin':[x,y],'anchor':'base west','baseline':'node text baseline','width_source_px':w,'width_mm':round(mm,3),'visible_tex':text,'state':state or 'live','invisible_annotation_tex':ann if state else None,'ownership':'visible node contents once; phantom annotation has no visible copy'})
def group(i,bbox,body,owns,qual=None,annotation=None,components=None,crop=None,role=None):
    add('% BEGIN '+i)
    add('% Observed locus '+str(bbox)+'; complete ownership: '+owns)
    if annotation: add('% Complete candidate/state annotation: '+annotation)
    x0,y0,x1,y1=bbox
    if qual:
        add(r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ('+f'{x0},{y0}'+r') {\unsure{%')
        add(r'\begin{tikzpicture}[x=0.085mm,y=-0.085mm,baseline=0pt, every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt}]')
        add(r'\path[use as bounding box] (0,0) rectangle ('+f'{x1-x0},{y1-y0}'+r');')
        add(r'\begin{scope}[shift={('+f'{-x0},{-y0}'+r')}]')
        add(body)
        add(r'\end{scope}')
        add(r'\end{tikzpicture}%')
        add(r'}};')
    else: add(body)
    add('% END '+i)
    groups.append({'id':i,'observed_bbox':bbox,'source_rectangle':([0,0,x1-x0,y1-y0] if qual else bbox),'coordinate_system':'original full scan; x right, y down','outer_origin':([x0,y0] if qual else [0,0]),'inner_scope_translation':([-x0,-y0] if qual else [0,0]),'mapping':'outer_origin + (global_source_coordinates + inner_scope_translation) = original full-scan coordinates' if qual else 'literal source coordinates = original full-scan coordinates','x_unit_mm':.085,'y_unit_mm':-.085,'anchor':'base west; zero inner/outer separation' if qual else 'fixed parent picture origin','baseline':'0pt in every nested picture','owns':owns,'qualification':qual,'complete_candidates_or_state':annotation,'components':components or [],'literal_source':body,'crop':crop,'role':role,'source_quality':'manual path approximation from the permitted one-view inspection; no render or metric validation'})
def math_label(x,y,tex,w=None):
    if w is None: return r'\node at ('+f'{x},{y}'+r') {$'+tex+r'$};'
    return r'\node at ('+f'{x},{y}'+r') {\resizebox{'+f'{w*.085:.3f}mm'+r'}{!}{$'+tex+r'$}};'

# Opening cancelled line and interlinear replacement.
label('T01',294,126,91,r'\unsure{On|Un}','deleted')
label('T02',417,139,240,r'proc\unsure{è|é|e}de','deleted')
label('T03',680,145,636,r'par récurrence sur','deleted')
label('T04',1360,154,215,r'$\operatorname{card} K$,','deleted')
label('T05',315,177,501,r"On note d'abord que",'inserted')
label('T06',256,227,563,r'pour prouver que','deleted')
group('A022-G01-opening-cancellations',[284,96,1581,230],r'''\draw[line width=.45pt] (335,108) .. controls (690,103) and (1060,104) .. (1390,114) .. controls (1490,119) and (1541,124) .. (1569,126);
\draw[line width=.45pt] (284,224) .. controls (434,214) and (642,218) .. (817,213);''','two actual cancellation runs; the six opening text labels remain outside',components=['upper long run','lower cancellation run'],crop='crops/01_opening.png')
label('T07',883,222,87,r'(si')
label('T08',1014,218,111,r'$V=X$')
group('A022-G02-initial-separator',[1124,190,1137,222],r'\draw[line width=.7pt] (1128,196) .. controls (1130,203) and (1129,213) .. (1130,219);','the one short upright separator after X; no adjacent word or letter',annotation=r'\setminus primary; literal nearly upright run retained without changing its direction',components=['one short upright run'],crop='crops/03_initial_formula.png')
group('A022-G03-initial-union',[1150,166,1209,250],r'''\draw[line width=.65pt] (1168,176) .. controls (1168,191) and (1168,212) .. (1182,214) .. controls (1197,218) and (1208,183) .. (1197,168);
\node at (1152,244) {\resizebox{5.100mm}{!}{$\alpha\in K$}};''','union body and its alpha-in-K limit, once',components=['union body','limit label'],crop='crops/03_initial_formula.png')

# Complete literal Sigma glyph groups. Each index/sign belongs only to its group.
sigmas=[
('S01',[1211,151,1290,224],[(1217,182),(1252,183)],[(1217,188),(1243,197),(1217,211),(1252,211)],'hat',[(1232,169),(1257,157),(1272,168)],(1271,188),'+',(1255,224),r'\alpha','crops/03_initial_formula.png',True),
('S02',[1445,159,1520,226],[(1452,184),(1493,186)],[(1453,191),(1478,198),(1451,211),(1497,212)],'hat',[(1467,174),(1483,164),(1497,173)],(1504,190),'+',(1494,225),r'\alpha','crops/02_parenthetical_end.png',True),
('S03',[1158,307,1238,353],[(1164,315),(1197,314)],[(1164,315),(1159,322),(1190,327),(1166,338),(1201,338)],None,None,(1210,322),'-',(1206,351),r'\alpha','crops/03_initial_formula.png',False),
('S04',[678,400,780,463],[(686,411),(728,405)],[(685,419),(715,427),(687,446),(730,445)],None,None,(746,411),'-',(738,462),r'\alpha','crops/04_first_brace.png',True),
('S05',[1408,390,1486,449],[(1415,402),(1444,402)],[(1416,407),(1436,414),(1416,432),(1446,432)],None,None,(1464,404),'+',(1447,444),r'\alpha','crops/04_first_brace.png',True),
('S06',[906,642,1019,732],[(915,668),(965,668)],[(915,668),(941,690),(913,717),(964,713)],'bar',[(922,652),(993,649)],(987,679),'-',(967,729),r'\alpha','crops/05_main_equality.png',False),
('S07',[800,739,876,805],[(809,767),(844,764)],[(810,773),(837,779),(807,790),(848,790)],'hat',[(815,754),(835,744),(849,751)],(850,771),'+',(847,801),r'\alpha','crops/05_main_equality.png',True),
('S08',[1003,739,1091,797],[(1009,764),(1038,762)],[(1008,769),(1033,775),(1008,785),(1040,785)],'bar',[(1011,750),(1069,749)],(1053,767),'-',(1046,794),r'\alpha','crops/05_main_equality.png',True),
('S09',[1122,727,1186,790],[(1128,752),(1155,750)],[(1128,752),(1150,759),(1127,772),(1159,772)],'hat',[(1130,741),(1149,731),(1163,738)],(1165,757),'+',(1160,786),r'\alpha','crops/05_main_equality.png',False),
('S10',[738,800,826,863],[(745,814),(779,817)],[(745,814),(774,824),(743,846),(784,845)],None,None,(805,809),'-',(786,861),r'\alpha','crops/06_comme.png',False),
('S11',[1398,767,1507,851],[(1413,793),(1453,791)],[(1408,799),(1440,811),(1407,825),(1463,826)],'shared_bar',None,(1465,795),'-',(1461,845),r'\alpha','crops/06_comme.png',True),
('S12',[563,1017,671,1100],[(575,1050),(624,1048)],[(575,1050),(569,1055),(614,1065),(574,1087),(633,1081)],'bar',[(575,1032),(665,1026)],(641,1060),'-',(632,1095),r'\alpha','crops/07_inverse_soit.png',False),
('S13',[589,1136,678,1211],[(598,1163),(636,1161)],[(598,1168),(626,1178),(594,1195),(641,1194)],'bar',[(601,1146),(668,1142)],(650,1164),'-',(641,1208),r'\alpha','crops/07_inverse_soit.png',True),
('S14',[716,1540,827,1624],[(726,1582),(772,1581)],[(723,1588),(756,1595),(721,1614),(773,1610)],'hat',[(758,1564),(782,1550),(799,1561)],(799,1587),'-',(783,1622),r'\alpha','crops/10_old_variable.png',True),
('S15',[894,1572,985,1627],[(903,1582),(934,1581)],[(901,1589),(927,1595),(898,1612),(939,1612)],None,None,(958,1588),'-',(943,1625),r'\alpha','crops/10_old_variable.png',True),
('S16',[716,1948,812,2033],[(729,1978),(766,1977)],[(729,1978),(754,1991),(723,2016),(777,2018)],'hat',[(740,1965),(778,1953),(795,1964)],(786,1980),'+',(774,2030),r'\alpha','crops/13_YZ.png',False),
('S17',[1194,1928,1298,2040],[(1203,1964),(1246,1963)],[(1203,1972),(1234,1985),(1199,2000),(1253,2000)],'hat',[(1239,1947),(1258,1933),(1278,1944)],(1279,1971),'+',(1259,2037),r'\beta','crops/13_YZ.png',True),
]
sigma_by={x[0]:x for x in sigmas}
def emit_sigma(code,qualified=False):
    sid,bbox,head,body,mark,markpts,signat,sign,idxat,idx,crop,detached=sigma_by[code]
    cmds=[]
    cmds.append(r'\draw[line width=.7pt] '+ ' -- '.join(f'({a},{b})' for a,b in head)+';')
    cmds.append(r'\draw[line width=.7pt] '+ ' -- '.join(f'({a},{b})' for a,b in body)+';')
    comp=['short head run','body run']
    if markpts:
        cmds.append(r'\draw[line width=.7pt] '+' -- '.join(f'({a},{b})' for a,b in markpts)+';')
        comp.append('roof' if mark=='hat' else 'existing closure bar')
    if mark=='shared_bar':
        cmds.append('% Upper rule is owned once by A022-G14-cancellation-frame, at x=1409..1494, y=773; do not draw it again here.')
        comp.append('existing upper rule shared with G14, no second copy')
    cmds.append(math_label(*signat,sign,17))
    cmds.append(math_label(*idxat,idx,27 if idx==r'\beta' else 23))
    comp+=['raised '+sign,'index '+idx]
    state='cancelled' if code in ['S10','S11','S12','S13','S14','S15'] else 'live'
    ann=(r'\widehat{\Sigma}' if mark=='hat' else (r'\overline{\Sigma}' if mark in ['bar','shared_bar'] else r'\Sigma'))+'_{'+idx+'}^{'+sign+'}'
    if state=='cancelled':
        cmds.append(r'\node[overlay] at ('+str(bbox[0])+','+str(bbox[3])+r') {\phantom{$\deleted{'+ann+r'}$}};')
        comp.append('invisible deleted-state annotation')
    if code=='S11': ann=r'\overline{\Sigma_\alpha^-}|\Sigma_\alpha^-; upper-rule attachment unresolved; cancelled passage state retained'
    elif qualified: ann+=r'; short head role: head/retrace or separate upper run, no extra mathematical operation selected'
    group('A022-'+sid,bbox,'\n'.join(cmds),'complete Sigma body, head, '+('hat, ' if mark=='hat' else 'closure rule, ' if mark=='bar' else '')+'raised sign and index; no adjacent relation or word','head-role uncertainty; first occurrence on page' if qualified else ('shared-rule role uncertainty' if code=='S11' else None),ann,comp,crop,'literal glyph; '+state+' by enclosing text; detached head='+str(detached))

emit_sigma('S01',qualified=True)
label('T09',1305,229,18,',')
label('T10',1338,220,61,'les')
emit_sigma('S02')
group('A022-G04-alpha-parentheses',[1528,182,1680,298],r'''\draw[line width=.55pt] (1538,187) .. controls (1530,198) and (1529,211) .. (1534,216) .. controls (1538,219) and (1543,216) .. (1546,214);
\node at (1547,222) {\resizebox{9.010mm}{!}{$\alpha\in K$}};
\draw[line width=.5pt] (1661,216) .. controls (1670,221) and (1676,239) .. (1679,251);
\draw[line width=.55pt] (1666,266) .. controls (1666,278) and (1656,289) .. (1648,298);''','inner opening parenthesis, alpha-in-K, its right-edge closing parenthesis, and the outer closing parenthesis after disjoints; words etant/disjoints remain outside',components=['inner opener','alpha-in-K label','inner closer at sheet edge','outer closer'],crop='crops/02_parenthetical_end.png')
label('T11',1452,270,204,r'\unsure{etant|étant} \unsure{disjoints|disjointes}')
group('A022-G05-underformula-guide',[1078,250,1268,303],r'''\draw[line width=.65pt] (1085,256) .. controls (1081,269) and (1081,272) .. (1090,274) .. controls (1149,277) and (1225,274) .. (1255,274) .. controls (1268,273) and (1266,262) .. (1259,263);
\draw[line width=.7pt] (1163,284) -- (1165,299);
\draw[line width=.7pt] (1173,284) -- (1175,302);''','rounded hooked under-formula rule and two descending equality ticks; no formula label',components=['one connected hooked rule','left equality tick','right equality tick'],crop='crops/03_initial_formula.png')
group('A022-G06-intersection-insertion',[1108,306,1240,383],r'''\draw[line width=.85pt] (1126,338) .. controls (1116,313) and (1128,308) .. (1142,311) .. controls (1157,313) and (1160,327) .. (1160,338);
\node at (1109,377) {\resizebox{8.160mm}{!}{$\alpha\in K$}};
\node[overlay] at (1120,340) {\phantom{\inserted{$\bigcap_{\alpha\in K}\Sigma_\alpha^-$}}};''','inserted intersection body and its limit; Sigma S03 is separately owned at the same insertion',annotation=r'\inserted{\bigcap_{\alpha\in K}\Sigma_\alpha^-}',components=['intersection body','alpha-in-K limit','invisible insertion annotation'],crop='crops/03_initial_formula.png')
emit_sigma('S03')

# First braced assertion, including the exact loop and marginal arrow.
group('A022-G07-first-brace-arrow',[413,286,584,482],r'''\draw[line width=.6pt] (549,294) .. controls (555,321) and (550,368) .. (546,380) .. controls (542,396) and (533,390) .. (540,383) .. controls (555,378) and (558,432) .. (554,456) .. controls (554,469) and (557,477) .. (560,479);
\draw[line width=.45pt] (457,445) .. controls (510,443) and (548,439) .. (581,435);
\draw[line width=.65pt] (575,431) -- (582,435) -- (574,438);''','main left brace with closed middle loop, marginal arrow shaft and two-leg head; trivial text is outside',components=['continuous brace with closed middle loop','arrow shaft','two-leg arrowhead'],crop='crops/04_first_brace.png')
label('T12',413,449,109,'trivial')
label('T13',582,343,339,r'$\overline V\cap E_\alpha\ne\varnothing$')
label('T14',592,460,77,r'$V\cap$')
emit_sigma('S04')
group('A022-G08-old-relation',[798,412,862,452],r'''\draw[line width=.85pt] (804,426) -- (853,422);
\draw[line width=.8pt] (804,440) -- (854,435);
\draw[line width=.65pt] (831,418) .. controls (831,428) and (831,439) .. (829,449);
\draw[line width=.9pt] (800,430) -- (858,426);
\draw[line width=.9pt] (800,445) -- (859,440);
\node[overlay] at (802,443) {\phantom{$\deleted{\unsure{\ne|=}}$}};''','all observed horizontal/central runs of the crossed old relation; old empty set is G09','old glyph remains ≠ or =',r'\deleted{\unsure{\ne|=}}',components=['upper relation run','lower relation run','short central run','upper crossing/retrace','lower crossing/retrace','invisible candidate annotation'],crop='crops/04_first_brace.png')
group('A022-G09-old-emptyset',[870,384,920,477],r'''\draw[line width=.65pt] (884,411) .. controls (883,397) and (902,406) .. (901,423) .. controls (901,440) and (884,436) .. (884,411);
\draw[line width=.6pt] (904,396) -- (877,465);
\draw[line width=.8pt] (878,390) .. controls (890,412) and (887,441) .. (890,461);
\draw[line width=.8pt] (883,388) -- (902,448);
\draw[line width=.9pt] (916,391) .. controls (908,419) and (888,447) .. (877,473);
\node[overlay] at (877,449) {\phantom{$\deleted{\varnothing}$}};''','old slashed oval and its visible cancellation diagonals; no old relation and no live replacement',annotation=r'\deleted{\varnothing}',components=['old oval','old slashing run','first cancellation diagonal','second cancellation diagonal','third cancellation diagonal','invisible state annotation'],crop='crops/04_first_brace.png')
label('T15',938,449,79,r'$\ne\varnothing$')
label('T16',1095,441,200,'alors que')
label('T17',1340,445,61,r'$V\cap$')
emit_sigma('S05')
label('T18',1498,447,91,r'$=\varnothing$')

label('T19',258,594,825,r'De façon précise, je dis que')
group('A022-M01-precise-upper-tick',[630,563,638,571],r'\draw[line width=.75pt] (633,565) -- (634,568);','one short upper tick near précise; the word and its acute remain in T19','attachment/role/hand/surface origin undetermined',components=['short upright tick'],crop='crops/15_precise.png')
label('T20',606,729,279,r'$\overline V\cap E_\alpha=$')
emit_sigma('S06')
label('T21',1038,722,138,r'$\cap E_\alpha$')
label('T22',1249,712,408,r'(qui est donc $\ne\varnothing$)')
# A complete locally qualified lower annotation group owns both formulas.
add('% BEGIN A022-G10-lower-annotations')
add('% State alternatives: live inserted pair | deleted inserted pair; the frame top belongs once to G14.')
add(r'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (680,733) {\unsure{%')
add(r'\begin{tikzpicture}[x=0.085mm,y=-0.085mm,baseline=0pt,every node/.style={anchor=base west,inner sep=0pt,outer sep=0pt}]')
add(r'\path[use as bounding box] (0,0) rectangle (529,80);')
add(r'\begin{scope}[shift={(-680,-733)}]')
add(r'\draw[line width=.6pt] (688,751) -- (696,766);')
add(r'\draw[line width=.6pt] (699,752) -- (706,771);')
add(math_label(725,802,r'\overline V\cap',73))
emit_sigma('S07')
group('A022-G11-right-connector',[1010,734,1074,756],r'''\draw[line width=.65pt] (1015,751) -- (1028,742);
\draw[line width=.65pt] (1046,740) -- (1055,749);
\draw[line width=.65pt] (1063,739) -- (1070,750);
\node[overlay] at (1010,750) {\phantom{$\unsure{\deleted{=}|=|\Rightarrow}$}};''','three short oblique traces touching the closure rule owned by S08; no second horizontal rule','connector glyph and cancellation state retained',r'\unsure{\deleted{=}|=|\Rightarrow}',components=['left oblique trace','first upper tick','second upper tick','invisible candidate annotation'],crop='crops/05_main_equality.png')
emit_sigma('S08')
add(math_label(1091,789,r'\cap',27))
emit_sigma('S09')
add(r'\node[overlay] at (716,804) {\phantom{$\inserted{\overline V\cap\widehat\Sigma_\alpha^+}$}};')
add(r'\node[overlay] at (1006,796) {\phantom{$\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+}$}};')
add(r'\end{scope}')
add(r'\end{tikzpicture}%')
add(r'}};')
add('% END A022-G10-lower-annotations')
groups.append({'id':'A022-G10-lower-annotations','observed_bbox':[680,733,1209,813],'source_rectangle':[0,0,529,80],'outer_origin':[680,733],'inner_scope_translation':[-680,-733],'mapping':'(680,733)+(source-global-(680,733))=source-global','x_unit_mm':.085,'y_unit_mm':-.085,'anchor':'base west, zero separation','baseline':'0pt','owns':'both lower inserted expressions, their left vertical equals, S07/S08/S09 and separately qualified G11; the top cancellation-frame path remains G14','qualification':'live inserted pair primary; deleted inserted pair alternative','complete_candidates_or_state':r'\inserted{\overline V\cap\widehat\Sigma_\alpha^+},\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+} | \deleted{\inserted{\overline V\cap\widehat\Sigma_\alpha^+},\inserted{\overline{\Sigma_\alpha^-}\cap\widehat\Sigma_\alpha^+}}','components':['two left equality ticks','left V-bar/cap label','S07','G11','S08','right cap label','S09','two invisible insertion-state annotations'],'crop':'crops/05_main_equality.png','source_quality':'manual reconstruction, no render or metric validation'})

# Cancelled proof block: readable labels with invisible deletion annotations.
label('T23',264,850,205,'Comme','deleted')
label('T24',615,849,112,r'$V\subset$','deleted')
emit_sigma('S10')
label('T25',880,863,18,',','deleted')
label('T26',922,847,127,'on a','deleted')
label('T27',1161,845,208,r'$V\cap E_\alpha\subset$','deleted')
emit_sigma('S11')
label('T28',1510,849,142,r'$\cap E_\alpha$,','deleted')
label('T29',265,977,208,'prouvons','deleted')
label('T30',582,958,527,"l'inclusion inverse",'deleted')
group('A022-M02-left-upright',[246,886,257,905],r'\draw[line width=.35pt] (253,890) .. controls (251,895) and (251,898) .. (251,903);','one detached thin upright to left of the cancellation frame; no text','role, attachment, hand and surface origin undetermined',components=['one thin upright'],crop='crops/06_comme.png')
emit_sigma('S12')
label('T31',681,1089,414,r'$\cap E_\alpha\subset\overline V\cap E_\alpha$','deleted')
label('T32',281,1208,91,'Soit','deleted')
label('T33',482,1200,65,r'$x\in$','deleted')
emit_sigma('S13')
label('T34',681,1207,125,r'$\cap E_\alpha$,','deleted')
label('T35',862,1197,219,'prouvons','deleted')
label('T36',1160,1198,259,r'$x\in\overline V\cap E_\alpha$','deleted')
label('T37',1461,1191,63,'i.e.','deleted')
label('T38',257,1313,171,r'$x\in\overline V$,','deleted')
label('T39',498,1301,85,'soit','deleted')
label('T40',658,1294,552,r'$W$ un voisinage de $x$,','deleted')
label('T41',1247,1287,391,"montrons qu'il",'deleted')
label('T42',267,1401,279,'rencontre','deleted')
label('T43',701,1382,76,'Or','deleted')
label('T44',823,1372,92,r'\unsure{on}','deleted')
label('T45',948,1370,103,'peut','deleted')
label('T46',1101,1371,319,'considérer','deleted')
label('T47',1470,1373,132,'cette','deleted')
label('T48',275,1502,216,r'\unsure{formule|relation}','deleted')
label('T49',327,1464,167,'égalité','deleted inserted')
label('T50',564,1492,224,'comme','deleted')
label('T51',883,1480,189,'égalité','deleted')
label('T52',1146,1478,90,'dans','deleted')
label('T53',312,1595,205,"l'espace",'deleted')
group('A022-G12-local-on-and-noun-cancellations',[273,1345,928,1505],r'''\draw[line width=.8pt] (823,1363) .. controls (850,1361) and (881,1368) .. (915,1368);
\draw[line width=.75pt] (276,1498) .. controls (352,1496) and (417,1493) .. (494,1493);''','one local strike on on and one local strike on the old noun; readable labels remain outside',components=['on local strike','old-noun local strike'],crop='crops/09_or_and_noun.png')
group('A022-G13-old-variable',[570,1564,638,1636],r'''\draw[line width=1.0pt] (584,1570) -- (614,1593) -- (582,1624);
\draw[line width=1.0pt] (625,1570) -- (578,1629);
\draw[line width=.65pt] (584,1595) -- (616,1588);
\draw[line width=.65pt] (578,1628) -- (614,1622);
\draw[line width=1.3pt] (632,1571) -- (585,1633);
\node[overlay] at (576,1617) {\phantom{$\deleted{\unsure{Y|Z|X}}$}};''','all surviving old-letter and local crossing strokes before the first equals; complete Y/Z/X candidates remain together','old letter unresolved; cancellation certain',r'\deleted{\unsure{Y|Z|X}}',components=['fork/descending letter candidate','opposite diagonal','upper short run','foot run','heavy local diagonal','invisible full-candidate annotation'],crop='crops/10_old_variable.png')
label('T54',641,1613,31,r'$=$','deleted')
emit_sigma('S14')
label('T55',855,1610,19,r'$=$','deleted')
emit_sigma('S15')
label('T56',1007,1612,135,r'$\cup E_\alpha$','deleted')
label('T57',302,1726,364,'dans lequel','deleted')
label('T58',748,1717,143,'on a','deleted')
label('T59',950,1718,557,r'deux parties ferm\unsure{é|è|e}es','deleted')
label('T60',304,1841,280,'disjointes','deleted')
# All long connected cancellation paths. The upper-rule segment at S11 is one physical run.
group('A022-G14-cancellation-frame',[256,768,1598,1850],r'''\draw[line width=.5pt] (264,836) -- (282,835) .. controls (528,828) and (710,800) .. (1018,788) .. controls (1192,779) and (1331,774) .. (1409,773) -- (1494,773) .. controls (1535,772) and (1564,774) .. (1581,778);
\draw[line width=.5pt] (282,835) .. controls (295,1034) and (305,1230) .. (283,1396) .. controls (279,1481) and (312,1497) .. (312,1597) .. controls (316,1644) and (523,1610) .. (706,1594) .. controls (866,1584) and (1035,1624) .. (1140,1612) .. controls (1243,1608) and (1311,1572) .. (1345,1545);
\draw[line width=.5pt] (516,843) .. controls (588,1000) and (692,1190) .. (786,1273) .. controls (798,1281) and (809,1289) .. (815,1287);
\draw[line width=.5pt] (985,893) .. controls (1050,1046) and (1138,1276) .. (1206,1374) -- (1240,1410);
\draw[line width=.5pt] (1394,847) .. controls (1437,939) and (1487,1069) .. (1501,1154);
\draw[line width=.5pt] (283,1397) .. controls (404,1400) and (535,1390) .. (638,1380) .. controls (627,1357) and (618,1323) .. (634,1305) .. controls (645,1279) and (673,1283) .. (738,1285) .. controls (913,1289) and (1147,1291) .. (1327,1286) .. controls (1336,1284) and (1340,1280) .. (1331,1273);
\draw[line width=.55pt] (815,1329) .. controls (860,1384) and (902,1457) .. (961,1475);
\draw[line width=.55pt] (276,1504) .. controls (447,1495) and (650,1481) .. (908,1476) .. controls (1104,1471) and (1238,1471) .. (1353,1469) .. controls (1439,1467) and (1481,1437) .. (1515,1377) .. controls (1544,1338) and (1565,1328) .. (1597,1319);
\draw[line width=.5pt] (308,1734) .. controls (570,1721) and (826,1714) .. (1050,1710) .. controls (1238,1707) and (1411,1706) .. (1515,1712);
\draw[line width=.5pt] (307,1731) .. controls (298,1765) and (289,1805) .. (302,1827) .. controls (317,1856) and (454,1838) .. (555,1833) .. controls (608,1830) and (645,1821) .. (641,1792) -- (632,1741);''','all long cancellation/frame runs, including the shared upper rule above S11 and the lower continuation around disjointes; adjacent letters/words are owned by their labels/Sigma groups',annotation='enclosing cancellation; exact temporal order and shared-bar authorship are not inferred',components=['top boundary with shared S11 upper segment','left boundary and lower equation sweep','left long diagonal','central long diagonal','right long diagonal','rencontre/W-neighbourhood hooked boundary','Or-to-égalité diagonal','lower middle boundary with right upward hook','last-clause horizontal cancellation','last-clause rounded lower return'],crop='whole + halves; local contexts 05–11')

# Live restart and its two independently underlined words.
label('T61',718,1792,802,r'Or dans $X$ on a les deux')
label('T62',306,1926,201,'parties')
label('T63',581,1902,191,'fermées')
label('T64',841,1894,272,'disjointes')
group('A022-G15-live-underlines',[630,1898,1114,1930],r'''\draw[line width=.65pt] (634,1926) .. controls (681,1920) and (718,1917) .. (758,1914);
\draw[line width=.65pt] (873,1908) .. controls (947,1905) and (1028,1903) .. (1107,1902);''','the two physical underline runs under fermées and disjointes; both word labels remain outside',components=['fermées underline','disjointes underline'],crop='crops/12_detached_slash.png and crops/14_live_fermees.png')
group('A022-M03-fermees-upper-tick',[726,1875,735,1888],r'\draw[line width=.8pt] (731,1879) -- (729,1885);','short detached upper tick before the clear acute of live fermées; the word and acute remain T63','role, attachment, hand and surface origin undetermined',components=['one short tick'],crop='crops/14_live_fermees.png')
group('A022-M04-detached-slash',[1213,1830,1241,1857],r'\draw[line width=.7pt] (1218,1836) -- (1236,1851);','one detached down-right slash above-right of disjointes; adjoining words are outside','role, attachment, hand and surface origin undetermined',components=['one short oblique run'],crop='crops/12_detached_slash.png')
label('T65',639,2026,62,r'$Y=$')
emit_sigma('S16')
label('T66',832,2046,19,',')
label('T67',906,2003,84,r'$Z=$')
group('A022-G16-final-union',[1013,1953,1207,2086],r'''\draw[line width=.65pt] (1043,1963) .. controls (1045,1984) and (1045,2018) .. (1063,2019) .. controls (1085,2020) and (1110,1994) .. (1107,1963);
\node at (1018,2078) {\resizebox{16.150mm}{!}{$\beta\in K\setminus\{\alpha\}$}};''','final indexed union body and its beta-in-K-setminus-alpha limit; adjoining Z and Sigma S17 remain separate',components=['union body','complete limit label'],crop='crops/13_YZ.png')
emit_sigma('S17')
group('A022-M05-sigma-inner-point',[1203,1975,1216,1988],r'\fill (1210,1981) circle[radius=1.8];','one dark point inside the open upper angle of S17; it owns no part of the Sigma paths or beta','role, attachment, hand and surface origin undetermined',components=['one point-shaped fill'],crop='crops/13_YZ.png')
group('A022-M06-below-beta-point',[1282,2042,1292,2054],r'\fill (1287,2048) circle[radius=.7];','one tiny point below-right of S17 beta; the beta remains in S17','role, attachment, hand and surface origin undetermined',components=['one tiny point-shaped fill'],crop='crops/13_YZ.png')
add(r'\end{tikzpicture}}')
add('')
add('et on doit prouver')
add(r'\[')
add(r'\overline{(X\setminus(Y\cup Z))}\cap Y=\overline{(X\setminus Y)}\cap Y')
add(r'\]')
add('ce qui est immédiat')
add('% archive sheet number: 21')
add('')
tex='\n'.join(lines)
(OUT/'reading.tex').write_text(tex)
# Capture exact source spans after complete assembly, including nested groups.
for g in groups:
    bid='% BEGIN '+g['id']; eid='% END '+g['id']
    start=tex.index(bid); end=tex.index(eid,start)+len(eid)
    g['source_start_byte_utf8']=len(tex[:start].encode())
    g['source_end_byte_utf8']=len(tex[:end].encode())
    g['source_start_line']=tex[:start].count('\n')+1
    g['source_end_line']=tex[:end].count('\n')+1
    g['complete_source_excerpt']=tex[start:end]
# S coordinate catalogue includes no optional extrema calculation.
(OUT/'graphical_audit.json').write_text(json.dumps({'coordinate_convention':'original full scan; upper-left origin; x right, y down; x=.085mm and y=-.085mm in every outer and inner picture','manual_dimension_mapping':'fixed text-label widths are w_source_px * .085 mm; this is a declared layout map, not measured image alignment','groups':groups,'labels':nodes,'sigma_catalogue':[{'id':'A022-'+a[0],'bbox':a[1],'detached_head':a[-1],'crop':a[-2]} for a in sigmas],'all_graphics_are_inside_required_figure':True,'validation_scope':'source only; no compilation, rendering, OCR or image-difference operation'},ensure_ascii=False,indent=2)+'\n')
print('Wrote complete reading.tex;',len(groups),'graphical groups;',len(nodes),'visible text/math label nodes; 17 complete Sigma groups.')
