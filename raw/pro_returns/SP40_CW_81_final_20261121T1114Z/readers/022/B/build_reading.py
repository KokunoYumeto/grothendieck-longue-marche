from pathlib import Path
import json,hashlib,re
BASE=Path('out/readers/022/B')
lines=[]; groups=[]; labels=[]; fig=None
UNIT='0.0088cm'
def emit(s=''): lines.extend(s.splitlines() or [''])
def text(x,y,s,state=None,size='\\small',ident=None):
    visible=s
    if state=='deleted': visible=r'\rlap{'+s+r'}\phantom{\deleted{'+s+'}}'
    elif state=='inserted': visible=r'\inserted{'+s+'}'
    elif state=='underlined': visible=r'\rlap{'+s+r'}\phantom{\uline{'+s+'}}'
    cmd=fr'\node[font={size},anchor=base west,inner sep=0pt,outer sep=0pt] at ({x},{y}) {{{visible}}};'
    emit(cmd);labels.append({'id':ident,'figure':fig,'anchor_full_scan':[x,y],'anchor':'base west','text':s,'state':state,'font':size,'source_command':cmd})
def startfig(ident,box):
    global fig
    fig=ident;x0,y0,x1,y1=box
    emit(fr'% BEGIN FIGURE {ident}; full-scan rectangle {box}; local origin ({x0},{y0}).')
    emit(r'\figure{\begin{tikzpicture}[x='+UNIT+',y=-'+UNIT+r',every node/.style={inner sep=0pt,outer sep=0pt,anchor=base west}]')
    emit(fr'\path[use as bounding box] (0,0) rectangle ({x1-x0},{y1-y0});')
    emit(fr'\begin{{scope}}[shift={{({-x0},{-y0})}}]')
def endfig(ident):
    emit(r'\end{scope}')
    emit(r'\end{tikzpicture}}')
    emit(fr'% END FIGURE {ident}')
    emit()
def group(ident,box,commands,owns,role=None,qualifier=False,candidates=None,hand='his hand',kind='drawing',crop=None):
    x0,y0,x1,y1=box;w=x1-x0;h=y1-y0
    emit(fr'% BEGIN {ident}; observed full-scan box {box}.')
    emit('% Ownership: '+owns)
    if role:emit('% Role/state: '+role)
    if candidates:emit('% Complete reading/state candidates: '+candidates)
    if qualifier:
        emit(fr'\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({x0},{y1}) {{\unsure{{%')
        emit(r'\begin{tikzpicture}[x='+UNIT+',y=-'+UNIT+r',baseline=(B),every node/.style={inner sep=0pt,outer sep=0pt,anchor=base west}]')
        emit(fr'\path[use as bounding box] (0,0) rectangle ({w},{h});')
        emit(fr'\coordinate (B) at (0,{h});')
        emit(fr'\begin{{scope}}[shift={{({-x0},{-y0})}}]')
    for c in commands:emit(c)
    if qualifier:
        emit(r'\end{scope}')
        emit(r'\end{tikzpicture}%')
        emit(r'}};')
    emit(fr'% END {ident}')
    groups.append({'id':ident,'figure':fig,'observed_bbox':box,'drawing_rectangle':box,'source_coordinate_convention':'Full-scan top-left origin, x right, y down; parent figure uses a declared translation.','x_y_unit_cm':0.0088,'nested_qualified':qualifier,'nested_origin':([x0,y0] if qualifier else None),'nested_baseline':([0,h] if qualifier else None),'parent_anchor':([x0,y1] if qualifier else None),'anchor':'base west; zero inner/outer separation','owns':owns,'role_or_state':role,'candidate_readings':candidates,'hand':hand,'kind':kind,'crop':crop,'literal_commands':commands})
def nodecmd(x,y,s,size=r'\scriptsize',phantom=False):
    return fr'\node[font={size},anchor=base west,inner sep=0pt,outer sep=0pt] at ({x},{y}) {{'+(r'\phantom{'+s+'}' if phantom else s)+'};'
def sigma(ident,box,paths,index,idxxy,sign,signxy,roof=None,bar=None,head_separated=False,crop=None,qualifier=False,extra=None,meaning=None,state=None):
    cmds=[r'\draw[line width=.45pt,line cap=round,line join=round] '+p+';' for p in paths]
    if roof:cmds.append(r'\draw[line width=.45pt,line cap=round,line join=round] '+roof+';')
    if bar:cmds.append(r'\draw[line width=.45pt,line cap=round] '+bar+';')
    cmds += [nodecmd(*idxxy,'$'+index+'$'),nodecmd(*signxy,'$'+sign+'$')]
    if extra:cmds+=extra
    reading=meaning or ((r'\widehat{\Sigma}' if roof else r'\Sigma')+'_{'+index+'}^{'+sign+'}')
    if bar:reading=r'\overline{'+reading+'}'
    cmds.append(nodecmd(box[0],box[3],'$'+(r'\deleted{'+reading+'}' if state=='deleted' else reading)+'$',phantom=True))
    role=('The short head and body are separately drawn. The head/independent-rule role remains unresolved; no mathematical operation is assigned to that separation.' if head_separated else 'The head and body form the locally observed connected letter shape.')
    group(ident,box,cmds,'Complete Sigma glyph, its head/body, '+('roof, ' if roof else '')+('outer bar, ' if bar else '')+'index '+index+' and raised '+sign+'; no adjoining word.',role,qualifier,reading+(' with head stroke | same visible shape with unassigned independent-rule role' if head_separated else ''),crop=crop)

emit(r'\scanpage{22}')
emit('% Reader B independent complete proposal. Manual literal paths; no compilation or rendering performed.')
emit('% Only the final simple equality is a conventional display; the other displayed expressions are labels in the adjoining literal drawing groups.')
startfig('B022-F01',[240,55,1680,505])
text(294,130,r'\unsure{On|Un} procède par récurrence sur $\operatorname{card} K$,','deleted',ident='T01')
text(312,179,"On note d'abord que",'inserted',ident='T02')
text(258,233,'pour','deleted',ident='T03')
text(432,233,'prouver','deleted',ident='T03b')
text(713,224,'que','deleted',ident='T03c')
group('B022-G01',[266,96,1570,238],[
 r'\draw[line width=.3pt,line cap=round] (327,110) .. controls (623,101) and (990,100) .. (1234,108) .. controls (1370,109) and (1471,118) .. (1566,126);',
 r'\draw[line width=.3pt,line cap=round] (268,226) .. controls (437,211) and (605,211) .. (811,215);'
 ],'The two original opening cancellation rules only; all opening words are owned by T01–T03.','Cancellation geometry; no inferred writing chronology.',crop='crops/01_opening.png')
group('B022-M01',[313,224,334,239],[r'\draw[line width=.4pt,line cap=round] (318,234) -- (331,228);'],'Short detached slash below pour; the word pour stays in T03.','Shape supported; attachment, role, hand and surface origin remain unresolved.',True,'visible short slash; no character assigned',hand='undetermined hand',crop='crops/01_opening.png')
text(884,222,r'(si',size=r'\normalsize',ident='T04')
text(1015,218,r'$V=X\setminus$',size=r'\normalsize',ident='T04b')
group('B022-G02',[1153,166,1218,253],[
 r'\draw[line width=.45pt,line cap=round] (1168,175) .. controls (1169,185) and (1170,190) .. (1170,196);',
 r'\draw[line width=.45pt,line cap=round] (1171,202) .. controls (1173,216) and (1193,218) .. (1205,204) .. controls (1216,189) and (1209,179) .. (1200,169);',
 nodecmd(1157,244,r'$\alpha\in K$')
 ],'Top union operator and its alpha-in-K lower limit.','The upper-left stem is interrupted before the returning bowl; both runs are preserved.',crop='crops/03_top_formula_insert.png')
sigma('B022-S01',[1214,151,1293,231],['(1253,183) -- (1223,182) .. controls (1226,189) and (1245,190) .. (1253,197) .. controls (1245,202) and (1230,207) .. (1221,211) -- (1261,212)'],r'\alpha',(1247,225),'+',(1266,191),roof='(1229,167) -- (1251,157) -- (1272,169)',crop='crops/03_top_formula_insert.png')
text(1304,226,',',ident='T05')
text(1339,218,'les',ident='T06')
sigma('B022-S02',[1443,158,1520,226],['(1451,184) -- (1483,186)','(1451,190) .. controls (1461,192) and (1472,192) .. (1474,198) -- (1449,207) -- (1484,209)'],r'\alpha',(1480,221),'+',(1500,193),roof='(1466,174) -- (1485,164) -- (1495,172)',head_separated=True,crop='crops/02_parenthesis_ending.png',qualifier=True)
group('B022-G03',[1526,182,1635,231],[
 r'\draw[line width=.4pt,line cap=round] (1540,188) .. controls (1530,197) and (1528,208) .. (1534,212) .. controls (1539,216) and (1545,215) .. (1551,212);',
 nodecmd(1546,219,r'$\alpha\in K$',r'\normalsize'),
 nodecmd(1526,231,r'$\unsure{(}\alpha\in K$',phantom=True)
 ],'Opening curve and immediately adjoining alpha-in-K; no second printed alpha is outside this group.','C022-R01 retained: parenthesis primary; attachment as a left lead into alpha remains possible.',True,r'(\alpha\in K | \alpha\in K with the same visible left lead',crop='crops/02_parenthesis_ending.png')
text(1451,272,'étant disjoints',size=r'\scriptsize',ident='T07')
group('B022-G04',[1639,208,1678,301],[
 r'\draw[line width=.3pt,line cap=round] (1662,213) .. controls (1669,219) and (1672,229) .. (1676,240);',
 r'\draw[line width=.4pt,line cap=round] (1666,262) .. controls (1662,276) and (1653,287) .. (1644,296);',
 nodecmd(1639,301,r'$\unsure{)|)\,)}$',phantom=True)
 ],'Both surviving right-edge closure runs, after the alpha-in-K line and after disjoints.','One spanning close versus two distinct closes is unresolved; the physical edge supplies no connecting ink.',True,') | ) )',crop='crops/02_parenthesis_ending.png')
group('B022-G05',[1077,250,1270,306],[
 r'\draw[line width=.45pt,line cap=round] (1083,255) .. controls (1078,264) and (1079,272) .. (1087,273) .. controls (1137,272) and (1205,276) .. (1251,273) .. controls (1266,273) and (1267,262) .. (1260,261);',
 r'\draw[line width=.5pt,line cap=round] (1161,284) -- (1162,299);',
 r'\draw[line width=.5pt,line cap=round] (1171,284) -- (1172,301);'
 ],'Complete hooked lower bracket and the descending equality strokes; no central brace cusp is supplied.','The bracket attaches the next intersection to X setminus the union.',crop='crops/03_top_formula_insert.png')
group('B022-G06',[1102,306,1166,385],[
 r'\draw[line width=.55pt,line cap=round] (1126,338) .. controls (1120,321) and (1130,312) .. (1141,313) .. controls (1154,311) and (1164,320) .. (1164,337);',
 nodecmd(1106,379,r'$\alpha\in K$'),
 nodecmd(1102,385,r'$\inserted{\bigcap_{\alpha\in K}}$',phantom=True)
 ],'Inserted intersection sign and its alpha-in-K lower limit.','Added below the bracket; its formula continues with S03.',crop='crops/03_top_formula_insert.png')
sigma('B022-S03',[1164,306,1245,356],['(1200,314) -- (1172,313) .. controls (1165,315) and (1166,320) .. (1175,321) -- (1195,326) -- (1172,340) -- (1203,341)'],r'\alpha',(1205,352),'-',(1213,322),crop='crops/03_top_formula_insert.png')
group('B022-G07',[532,288,565,486],[
 r'\draw[line width=.4pt,line cap=round] (549,294) .. controls (558,334) and (551,370) .. (547,382) .. controls (536,379) and (533,391) .. (540,393) .. controls (548,395) and (551,385) .. (547,382) .. controls (559,396) and (558,431) .. (554,448) .. controls (551,463) and (554,475) .. (559,480);'
 ],'The complete left brace, including its closed middle loop.','The loop and curved lower arm are drawn once beside the two conditions.',crop='crops/04_brace_old_relation.png')
text(590,340,r'$\overline V\cap E_\alpha\ne\varnothing$',size=r'\Large',ident='T08')
text(590,455,r'$V\cap$',size=r'\Large',ident='T09')
sigma('B022-S04',[678,397,786,466],['(686,408) -- (726,403)','(685,415) .. controls (710,419) and (730,424) .. (727,432) -- (684,452) -- (731,452)'],r'\alpha',(734,459),'-',(749,411),head_separated=True,crop='crops/04_brace_old_relation.png')
group('B022-G08',[794,384,925,485],[
 r'\draw[line width=.6pt,line cap=round] (803,427) -- (855,421);',
 r'\draw[line width=.6pt,line cap=round] (801,440) -- (857,437);',
 r'\draw[line width=.4pt,line cap=round] (830,418) -- (831,451) -- (836,450);',
 r'\draw[line width=.7pt,line cap=round] (800,433) -- (852,428);',
 r'\draw[line width=.8pt,line cap=round] (800,444) -- (855,439);',
 r'\draw[line width=.6pt,line cap=round] (884,409) .. controls (868,410) and (881,449) .. (895,444) .. controls (910,428) and (902,406) .. (884,409);',
 r'\draw[line width=.55pt,line cap=round] (905,393) -- (874,470);',
 r'\draw[line width=.55pt,line cap=round] (876,391) -- (895,457);',
 r'\draw[line width=.65pt,line cap=round] (882,389) -- (899,446);',
 r'\draw[line width=.65pt,line cap=round] (914,391) -- (886,462);',
 nodecmd(794,485,r'$\deleted{\unsure{\ne|=}\varnothing}$',phantom=True)
 ],'The old relation and its old empty-set glyph, including their local cancellation strokes; replacement is T10.','C022-R03 retained. The short upright can belong to the relation or to its cancellation; all old ink is retained.',True,r'\deleted{\ne\varnothing} | \deleted{=\varnothing}',crop='crops/04_brace_old_relation.png')
text(937,449,r'$\ne\varnothing$',size=r'\Large',ident='T10')
text(1092,441,'alors que',ident='T11')
text(1340,443,r'$V\cap$',size=r'\large',ident='T12')
sigma('B022-S05',[1409,392,1491,450],['(1447,402) -- (1416,402) .. controls (1412,405) and (1419,409) .. (1436,411) .. controls (1450,416) and (1430,426) .. (1415,431) -- (1447,432)'],r'\alpha',(1450,445),'+',(1464,407),crop='crops/13_brace_positive_sigma.png')
text(1504,442,r'$=\varnothing$',size=r'\large',ident='T13')
text(410,454,'trivial',size=r'\scriptsize',ident='T14')
group('B022-G09',[470,427,587,452],[
 r'\draw[line width=.3pt,line cap=round] (474,447) -- (580,435);',
 r'\draw[line width=.5pt,line cap=round] (574,431) -- (582,435) -- (575,439);'
 ],'The arrow from the marginal word trivial to the second condition. The word itself belongs to T14.','Arrow crosses the brace and ends before the V.',crop='crops/04_brace_old_relation.png')
endfig('B022-F01')
emit('De façon précise, je dis que')
emit()
startfig('B022-F02',[240,630,1678,1938])
text(608,730,r'$\overline V\cap E_\alpha=$',size=r'\Large',ident='T15')
sigma('B022-S06',[905,640,1023,735],['(966,668) -- (917,667) -- (945,689) -- (913,716) -- (965,714)'],r'\alpha',(968,725),'-',(984,678),bar='(920,651) .. controls (942,647) and (975,647) .. (995,650)',crop='crops/05_main_equality_annotations.png')
text(1040,723,r'$\cap E_\alpha$',size=r'\Large',ident='T16')
text(1253,711,r'(qui est donc $\ne\varnothing$)',ident='T17')
group('B022-G10',[680,744,713,779],[
 r'\draw[line width=.4pt,line cap=round] (687,750) -- (695,764);',
 r'\draw[line width=.4pt,line cap=round] (699,752) -- (707,771);'
 ],'The two descending equality strokes below the main left member.','Both strokes are clear; they precede the qualified lower left annotation.',crop='crops/05_main_equality_annotations.png')
# The lower annotation glyphs are individually mapped inside complete state-qualified groups.
leftcmd=[nodecmd(725,804,r'$\overline V\cap$',r'\scriptsize'),
 r'\draw[line width=.4pt,line cap=round] (808,772) -- (841,768);',
 r'\draw[line width=.4pt,line cap=round] (806,778) -- (827,782) -- (805,791) -- (841,790);',
 r'\draw[line width=.4pt,line cap=round] (816,758) -- (835,747) -- (849,756);',
 nodecmd(839,796,r'$\alpha$'),nodecmd(850,776,'$+$'),
 nodecmd(722,814,r'$\unsure{\deleted{\overline V\cap\widehat{\Sigma}_\alpha^+}|\overline V\cap\widehat{\Sigma}_\alpha^+}$',phantom=True)]
group('B022-G11',[722,741,877,817],leftcmd,'Complete lower left annotation: V with bar, cap, hatted Sigma S07 with its separate head, alpha and plus.','Primary deleted by the shared long line G14-C1; live annotation remains an alternative. The head/independent-rule role is also locally retained under the recurring sign convention.',True,r'\deleted{\overline V\cap\widehat{\Sigma}_\alpha^+} | \overline V\cap\widehat{\Sigma}_\alpha^+',crop='crops/05_main_equality_annotations.png')
rightcmd=[
 r'\draw[line width=.35pt,line cap=round] (1009,764) -- (1037,763);',
 r'\draw[line width=.35pt,line cap=round] (1008,769) -- (1029,775) -- (1007,782) -- (1040,783);',
 nodecmd(1041,789,r'$\alpha$',r'\tiny'),nodecmd(1052,771,'$-$',r'\tiny'),
 nodecmd(1089,786,r'$\cap$',r'\scriptsize'),
 r'\draw[line width=.35pt,line cap=round] (1163,750) -- (1132,750) -- (1153,759) -- (1129,771) -- (1166,773);',
 r'\draw[line width=.35pt,line cap=round] (1138,738) -- (1154,730) -- (1166,737);',
 nodecmd(1156,780,r'$\alpha$',r'\tiny'),nodecmd(1165,757,'$+$',r'\tiny'),
 nodecmd(1000,799,r'$\unsure{\deleted{\overline{\Sigma_\alpha^-}\cap\widehat{\Sigma}_\alpha^+}|\overline{\Sigma_\alpha^-}\cap\widehat{\Sigma}_\alpha^+}$',phantom=True)
 ]
group('B022-G12',[1000,726,1190,803],rightcmd,'Complete lower right formula: Sigma S08 with separate head, minus and alpha; cap; hatted Sigma S09 with alpha and plus. Its shared upper run is exclusively G13.','Primary deleted by the same G14-C1 line; live annotation remains an alternative. No ordinary overline duplicates the horizontal G13 run.',True,r'\deleted{\overline{\Sigma_\alpha^-}\cap\widehat{\Sigma}_\alpha^+} | \overline{\Sigma_\alpha^-}\cap\widehat{\Sigma}_\alpha^+',crop='crops/05_main_equality_annotations.png')
group('B022-G13',[1005,731,1077,759],[
 r'\draw[line width=.4pt,line cap=round] (1010,748) -- (1071,749);',
 r'\draw[line width=.35pt,line cap=round] (1018,754) -- (1027,742);',
 r'\draw[line width=.4pt,line cap=round] (1043,737) -- (1052,748);',
 r'\draw[line width=.4pt,line cap=round] (1062,738) -- (1069,750);',
 nodecmd(1005,759,r'$\rotatebox{90}{$\unsure{\deleted{=}|=|\Rightarrow}$}$',phantom=True)
 ],'The complete short horizontal run and three crossing/raised slants over S08; no second closure rule or generic connector is drawn.','C022-R04 retained: crossed descending equality primary, live equality and arrow-like interpretation remain; the apportionment between connector and formula bar is unresolved.',True,r'\rotatebox{90}{$\deleted{=}$} | \rotatebox{90}{$=$} | \rotatebox{90}{$\Rightarrow$}',crop='crops/05_main_equality_annotations.png')
text(263,852,'Comme',state='deleted',ident='T18')
text(618,850,r'$V\subset$',state='deleted',size=r'\large',ident='T18b')
sigma('B022-S10',[735,798,830,859],['(789,806) -- (747,804) -- (771,821) -- (741,845) -- (794,844)'],r'\alpha',(795,854),'-',(804,810),crop='crops/06_comme.png',state='deleted')
text(880,850,', on a',state='deleted',ident='T19')
text(1167,846,r'$V\cap E_\alpha\subset$',state='deleted',size=r'\large',ident='T20')
sigma('B022-S11',[1394,765,1510,853],['(1405,794) -- (1446,791)','(1405,800) -- (1436,811) -- (1401,827) -- (1468,826)'],r'\alpha',(1446,843),'-',(1459,794),bar='(1412,775) -- (1492,771)',head_separated=True,crop='crops/06_comme.png',state='deleted')
text(1518,846,r'$\cap E_\alpha$,',state='deleted',size=r'\large',ident='T21')
text(275,983,'prouvons',state='deleted',ident='T22')
text(576,960,"l'inclusion",state='deleted',ident='T22b')
text(936,953,'inverse',state='deleted',ident='T22c')
sigma('B022-S12',[557,1019,676,1098],['(621,1047) -- (567,1051) .. controls (565,1055) and (594,1055) .. (610,1062) -- (570,1086) -- (635,1075)'],r'\alpha',(621,1092),'-',(648,1057),bar='(574,1031) .. controls (603,1031) and (631,1027) .. (665,1026)',crop='crops/07_inverse.png',state='deleted')
text(680,1089,r'$\cap E_\alpha\subset\overline V\cap E_\alpha$',state='deleted',size=r'\large',ident='T23')
text(286,1211,'Soit',state='deleted',ident='T24')
text(485,1205,r'$x\in$',state='deleted',size=r'\large',ident='T24b')
sigma('B022-S13',[587,1135,684,1213],['(598,1159) -- (636,1156)','(597,1166) -- (624,1174) -- (596,1192) -- (641,1192)'],r'\alpha',(630,1208),'-',(647,1162),bar='(601,1146) -- (668,1141)',head_separated=True,crop='crops/08_soit_neighbourhood.png',state='deleted')
text(676,1204,r'$\cap E_\alpha$,',state='deleted',size=r'\large',ident='T25')
text(869,1198,'prouvons',state='deleted',ident='T26')
text(1164,1193,r'$x\in\overline V\cap E_\alpha$',state='deleted',size=r'\large',ident='T26b')
text(1462,1192,'i.e.',state='deleted',ident='T26c')
text(260,1304,r'$x\in\overline V$,',state='deleted',size=r'\large',ident='T27')
text(493,1303,'soit',state='deleted',ident='T27b')
text(657,1292,r'$W$',state='deleted',size=r'\large',ident='T27c')
text(713,1292,'un',state='deleted',ident='T27d')
text(820,1293,'voisinage',state='deleted',ident='T27e')
text(1066,1285,'de',state='deleted',ident='T27f')
text(1156,1285,r'$x$,',state='deleted',size=r'\large',ident='T27g')
text(1250,1277,"montrons qu'il",state='deleted',ident='T27h')
text(275,1405,'rencontre',state='deleted',ident='T28')
text(700,1376,'Or',state='deleted',ident='T29')
text(823,1372,r'\unsure{on}',state='deleted',ident='T30')
text(950,1370,'peut',state='deleted',ident='T31')
text(1090,1371,'considérer',state='deleted',ident='T31b')
text(1460,1385,'cette',state='deleted',ident='T31c')
text(280,1505,r'\unsure{formule|relation}',state='deleted',ident='T32')
text(333,1464,r'\inserted{égalité}',state='deleted',ident='T33')
text(566,1486,'comme',state='deleted',ident='T34')
text(891,1484,r'\unsure{égalité|egalité}',state='deleted',ident='T34b')
text(1146,1477,'dans',state='deleted',ident='T34c')
text(312,1601,"l'espace",state='deleted',ident='T35')
group('B022-G15',[573,1564,637,1636],[
 r'\draw[line width=.65pt,line cap=round] (586,1574) -- (608,1589) -- (630,1571);',
 r'\draw[line width=.9pt,line cap=round] (629,1574) -- (580,1628);',
 r'\draw[line width=.7pt,line cap=round] (583,1622) -- (615,1618);',
 r'\draw[line width=.65pt,line cap=round] (581,1597) -- (617,1585);',
 nodecmd(573,1636,r'$\deleted{\unsure{Y|Z|X}}$',phantom=True)
 ],'The complete old variable before the first equals; no additional generic Y, Z or X is printed.','C022-R07 retained with X added as a supported alternative; all strokes are preserved without assigning each stroke to letter or local cancellation.',True,r'\deleted{Y} | \deleted{Z} | \deleted{X}',crop='crops/10_old_variable.png')
text(641,1615,'$=$',state='deleted',size=r'\large',ident='T36')
sigma('B022-S14',[718,1538,831,1624],['(726,1581) -- (773,1580)','(725,1587) -- (754,1596) -- (723,1613) -- (778,1611)'],r'\alpha',(785,1620),'-',(800,1585),roof='(759,1551) -- (784,1540) -- (802,1552)',head_separated=True,crop='crops/10_old_variable.png',state='deleted')
text(847,1609,'$=$',state='deleted',size=r'\large',ident='T37')
sigma('B022-S15',[893,1575,982,1626],['(900,1582) -- (934,1580)','(900,1588) -- (927,1596) -- (898,1609) -- (939,1609)'],r'\alpha',(938,1620),'-',(954,1591),head_separated=True,crop='crops/10_old_variable.png',state='deleted')
text(1002,1616,r'$\cup E_\alpha$',state='deleted',size=r'\large',ident='T38')
text(306,1734,'dans',state='deleted',ident='T39')
text(463,1722,'lequel',state='deleted',ident='T39b')
text(747,1712,'on a',state='deleted',ident='T39c')
text(947,1705,'deux',state='deleted',ident='T39d')
text(1095,1708,'parties',state='deleted',ident='T39e')
text(1295,1706,'fermées',state='deleted',ident='T39f')
text(300,1842,'disjointes',state='deleted',ident='T40')
# All global and local cancellation runs are drawn here once; lower annotations share C1.
cancel=[
 r'\draw[line width=.4pt,line cap=round] (267,835) .. controls (505,826) and (697,801) .. (912,789) .. controls (1178,775) and (1455,767) .. (1578,777);',
 r'\draw[line width=.3pt,line cap=round] (281,838) .. controls (294,936) and (298,1095) .. (309,1210) .. controls (310,1292) and (304,1352) .. (283,1394);',
 r'\draw[line width=.35pt,line cap=round] (276,1394) .. controls (391,1408) and (520,1394) .. (638,1383) .. controls (623,1344) and (614,1305) .. (651,1285) .. controls (866,1285) and (1138,1290) .. (1328,1284) .. controls (1335,1284) and (1338,1281) .. (1331,1277);',
 r'\draw[line width=.4pt,line cap=round] (282,1402) -- (283,1497) .. controls (284,1528) and (332,1520) .. (403,1512) .. controls (658,1484) and (979,1473) .. (1279,1466) .. controls (1428,1475) and (1485,1450) .. (1524,1393) .. controls (1551,1352) and (1569,1333) .. (1600,1316);',
 r'\draw[line width=.35pt,line cap=round] (311,1512) -- (312,1597) .. controls (314,1630) and (382,1633) .. (493,1621) .. controls (613,1606) and (672,1583) .. (777,1592) .. controls (977,1602) and (1117,1621) .. (1225,1600) .. controls (1287,1589) and (1329,1558) .. (1346,1543);',
 r'\draw[line width=.3pt,line cap=round] (515,845) .. controls (574,946) and (632,1068) .. (704,1190) .. controls (740,1245) and (774,1282) .. (812,1288);',
 r'\draw[line width=.3pt,line cap=round] (986,895) .. controls (1043,1016) and (1107,1176) .. (1169,1298) .. controls (1197,1351) and (1225,1394) .. (1244,1412);',
 r'\draw[line width=.35pt,line cap=round] (815,1324) .. controls (857,1374) and (896,1438) .. (950,1472);',
 r'\draw[line width=.3pt,line cap=round] (1394,845) .. controls (1445,953) and (1490,1086) .. (1507,1142);',
 r'\draw[line width=.4pt,line cap=round] (308,1735) .. controls (666,1718) and (1080,1701) .. (1516,1710);',
 r'\draw[line width=.3pt,line cap=round] (308,1736) .. controls (302,1762) and (298,1787) .. (296,1804);',
 r'\draw[line width=.35pt,line cap=round] (296,1809) .. controls (294,1839) and (330,1848) .. (377,1840) .. controls (467,1832) and (540,1828) .. (590,1823) .. controls (638,1820) and (648,1810) .. (627,1745);',
 r'\draw[line width=.65pt,line cap=round] (821,1364) .. controls (847,1355) and (886,1364) .. (917,1368);',
 r'\draw[line width=.6pt,line cap=round] (276,1500) .. controls (349,1490) and (431,1494) .. (494,1494);'
 ]
group('B022-G14',[263,765,1606,1856],cancel,'All connected frame/cancellation runs C1–C14. C1 also passes through the feet of the two small lower annotations. All words and formula glyphs are owned separately; no text is embedded in these paths.','The passage is deleted. Path 11 and 12 preserve the lower left interruption. No generic visible sout stroke is added.',crop='crops/06_comme.png')
group('B022-M02',[245,885,257,904],[r'\draw[line width=.3pt,line cap=round] (253,890) .. controls (250,893) and (249,897) .. (251,900);'],'Tiny curved stroke left of the cancellation frame; no adjoining word.','Shape supported; role, hand and surface origin remain unresolved.',True,'small curved stroke; no character assigned',hand='undetermined hand',crop='crops/06_comme.png')
group('B022-M06',[302,1507,312,1517],[r'\fill (307,1512) circle[radius=1.2];'],'Small point below the beginning of the old noun; noun itself belongs to T32.','The point may attach to the noun or its cancellation; its role and hand remain unresolved. No letter is supplied from it.',True,'point; attachment unresolved',hand='undetermined hand',crop='crops/09_or_corrected_noun.png')
group('B022-M07',[1649,1725,1665,1743],[
 r'\fill (1658.1,1729.3) .. controls (1659.1,1728.3) and (1661.0,1729.1) .. (1660.8,1730.5) .. controls (1660.5,1732.0) and (1658.2,1732.3) .. (1657.7,1731.0) -- cycle;',
 r'\fill (1653.0,1736.2) .. controls (1654.2,1735.5) and (1655.9,1736.2) .. (1655.7,1737.7) .. controls (1655.1,1739.0) and (1652.9,1738.8) .. (1652.8,1737.2) -- cycle;'
 ],'Two separate small points near the right paper edge, beside the lower cancelled/live transition; no adjoining word.','Both shapes are supported; attachment, role, hand and surface origin remain unresolved.',True,'two small points; no punctuation assigned',hand='undetermined hand',crop='crops/14_right_edge_marks.png')
text(717,1792,'Or',ident='T41')
text(824,1782,'dans',ident='T41b')
text(1002,1785,r'$X$',size=r'\large',ident='T41c')
text(1058,1785,'on a',ident='T41d')
text(1287,1784,'les',ident='T41e')
text(1403,1782,'deux',ident='T41f')
text(306,1929,'parties',ident='T42')
text(550,1907,'fermées',state='underlined',ident='T43')
text(836,1885,'disjointes',state='underlined',ident='T44')
group('B022-G16',[625,1895,1110,1931],[
 r'\draw[line width=.4pt,line cap=round] (630,1925) -- (757,1916);',
 r'\draw[line width=.4pt,line cap=round] (873,1906) -- (1102,1900);'
 ],'The two separate underline strokes beneath fermées and disjointes; words belong to T43 and T44.','Literal spans are retained; no linguistic restriction of emphasis to a partial word is inferred.',crop='crops/12_lower_sigma_mark.png')
group('B022-M03',[1210,1828,1245,1859],[r'\draw[line width=.45pt,line cap=round] (1218,1835) -- (1238,1852);'],'Detached oblique stroke above-right of disjointes; no word owned.','Shape high confidence; role, hand, attachment and surface origin unresolved.',True,'short oblique stroke; no character assigned',hand='undetermined hand',crop='crops/11_dans_lequel.png')
endfig('B022-F02')
startfig('B022-F03',[620,1928,1312,2088])
text(640,2018,'$Y=$',size=r'\Large',ident='T45')
sigma('B022-S16',[719,1947,821,2029],['(768,1977) -- (731,1978) -- (759,1991) -- (724,2014) .. controls (745,2012) and (764,2011) .. (788,2020)'],r'\alpha',(778,2024),'+',(790,1983),roof='(758,1966) -- (778,1953) -- (792,1964)',crop='crops/12_lower_sigma_mark.png')
text(830,2051,',',ident='T46')
text(908,2011,'$Z=$',size=r'\Large',ident='T47')
group('B022-G17',[1011,1956,1205,2081],[
 r'\draw[line width=.45pt,line cap=round] (1043,1962) .. controls (1045,1998) and (1055,2018) .. (1082,2011) .. controls (1108,2004) and (1116,1984) .. (1110,1960);',
 nodecmd(1016,2077,r'$\beta\in K\setminus\{\alpha\}$',r'\normalsize')
 ],'The lower union bowl and complete beta-in-K-setminus-braced-alpha lower limit.','Both braces and the beta descender are retained.',crop='crops/12_lower_sigma_mark.png')
sigma('B022-S17',[1190,1928,1305,2040],['(1201,1962) -- (1242,1961)','(1203,1969) .. controls (1221,1975) and (1239,1975) .. (1234,1985) -- (1198,1999) -- (1253,2000)'],r'\beta',(1251,2036),'+',(1274,1981),roof='(1241,1943) -- (1258,1931) -- (1274,1941)',head_separated=True,crop='crops/12_lower_sigma_mark.png')
group('B022-M04',[1205,1973,1218,1986],[r'\fill (1210,1977) -- (1214,1980) -- (1208,1981) -- cycle;'],'The small inner triangular point of the S17 complete glyph cluster; no Sigma or beta is duplicated.','Shape high confidence; attachment, role, hand and surface origin unresolved.',True,'small point within the Sigma arms; no operation assigned',hand='undetermined hand',crop='crops/12_lower_sigma_mark.png')
group('B022-M05',[1282,2042,1293,2053],[r'\fill (1287,2047) circle[radius=.7];'],'Tiny point below-right of the beta belonging to S17; beta itself occurs once in S17.','A discrete point is supported. Its attachment, role, hand and surface origin remain unresolved.',True,'tiny point; no punctuation or index assigned',hand='undetermined hand',crop='crops/12_lower_sigma_mark.png')
endfig('B022-F03')
emit('et on doit prouver')
emit(r'\[')
emit(r'\overline{(X\setminus(Y\cup Z))}\cap Y=\overline{(X\setminus Y)}\cap Y')
emit(r'\]')
emit('ce qui est immédiat')
emit('% archive sheet number: 21')
emit()
tex='\n'.join(lines)
# Preserve straight apostrophes in diplomatic prose.
tex=tex.replace('qu’il',"qu'il")
(BASE/'reading.tex').write_text(tex)
for g in groups:
    a=tex.index('% BEGIN '+g['id']+';')
    b=tex.index('% END '+g['id'],a)+len('% END '+g['id'])
    if b<len(tex) and tex[b]=='\n':b+=1
    g['source_offsets_characters']=[a,b]
    g['source_lines']=[tex[:a].count('\n')+1,tex[:b].count('\n')]
    g['source_excerpt']=tex[a:b]
    g['source_sha256']=hashlib.sha256(tex[a:b].encode()).hexdigest()
    g['path_command_count']=sum(1 for q in g['literal_commands'] if q.startswith('\\draw') or q.startswith('\\fill'))
    g['text_label_commands']=[q for q in g['literal_commands'] if q.startswith('\\node')]
    g['counting_note']='A path command may contain multiple connected segments; disconnected runs are separate commands here except semantic text nodes.'
(BASE/'source_groups.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n')
(BASE/'text_ownership.json').write_text(json.dumps(labels,ensure_ascii=False,indent=2)+'\n')
print(json.dumps({'reading_bytes':len(tex.encode()),'groups':len(groups),'path_commands':sum(g['path_command_count'] for g in groups),'text_nodes':len(labels)},ensure_ascii=False))
