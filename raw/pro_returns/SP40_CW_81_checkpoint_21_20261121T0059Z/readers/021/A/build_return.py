from pathlib import Path
import json,re
P=Path('out/readers/021/A')
groups=[]
def graphic(gid,box,base,paths,nodes=(),qual=None,annotation=None,owner='',crop=None,components=None):
    lines=[f'% {gid} BEGIN; source bbox={box}; source origin=({box[0]},{box[1]}); baseline y={base}; owns: {owner}',f'\\begin{{tikzpicture}}[x=.055mm,y=-.055mm,baseline=({gid}base),line cap=round,line join=round]',f'\\path[use as bounding box] ({box[0]},{box[1]}) rectangle ({box[2]},{box[3]});',f'\\coordinate ({gid}base) at ({box[0]},{base});']
    if annotation: lines += [f'% invisible complete reading/state annotation: {annotation}',f'\\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at ({box[0]},{base}) {{\\phantom{{${annotation}$}}}};']
    lines+=paths
    for x,y,t in nodes: lines += [f'\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({x},{y}) {{${t}$}};']
    lines += ['\\end{tikzpicture}',f'% {gid} END']
    body='\n'.join(lines)+'\n'
    if qual: body='\\unsure{% '+qual+'\n'+body+'}\n'
    groups.append({'tex_fragment':body,'id':gid,'bbox':box,'source_origin':[box[0],box[1]],'baseline_y':base,'coordinate_map':'full-scan coordinates retained in each independent picture; physical x=.055 mm per pixel, physical y=-.055 mm per pixel; declared rectangle fixes local extent; labels anchor=base west, inner/outer sep=0','owner':owner,'qualifier':qual,'annotation':annotation,'crop':crop,'path_commands':paths,'nodes':[{'source_anchor':[x,y],'anchor':'base west','text':t} for x,y,t in nodes],'components':components or []})
    return body

def sig(gid,box,base,head,body,idx,raised=None,hat=None,crop=None,qual=None,extra=(),annotation=None):
    paths=[r'\draw[line width=.45pt] '+head+';',r'\draw[line width=.45pt] '+body+';']
    if hat: paths.append(r'\draw[line width=.45pt] '+hat+';')
    paths+=list(extra)
    nodes=[]
    if idx:nodes.append(idx)
    if raised:nodes.append(raised)
    return graphic(gid,box,base,paths,nodes,qual,annotation,'complete Sigma, its separate head, index and any raised sign/hat; no adjoining relation or word',crop)

G={}
G['s1']=sig('A021G01',[566,155,693,257],226,'(576,196)--(619,194)','(577,202)--(616,208)--(578,225)..controls(592,223)and(610,222)..(620,225)',(631,238,r'\scriptstyle\alpha_0'),hat='(593,175)--(613,162)--(626,176)',crop='c02_first_display.png',qual='head-arm/independent upper-run role remains open; Sigma reading retained',annotation=r'\widehat\Sigma_{\alpha_0}')
G['s2']=sig('A021G02',[735,155,837,241],225,'(747,190)--(784,189)','(747,197)--(773,202)--(743,223)--(783,224)',(793,234,r'\scriptstyle i'),(807,202,r'\scriptstyle+'),'(757,175)--(776,161)--(790,175)','c02_first_display.png')
G['s3']=sig('A021G03',[1236,178,1328,250],225,'(1242,185)--(1285,184)','(1244,192)--(1274,199)--(1248,221)--(1284,219)',(1274,234,r'\scriptstyle\alpha_0'),crop='c02_first_display.png')
G['s4']=sig('A021G04',[1337,178,1400,244],226,'(1344,184)--(1378,188)','(1357,191)..controls(1340,197)and(1346,200)..(1368,208)..controls(1375,215)and(1355,220)..(1348,224)..controls(1365,223)and(1376,223)..(1380,228)',(1381,237,r'\scriptstyle i'),crop='c02_first_display.png')
G['s5']=sig('A021G05',[896,469,1018,563],535,'(905,504)--(950,499)','(912,510)--(935,516)--(904,534)--(955,533)',(960,546,r'\scriptstyle\alpha'),(983,517,r'\scriptstyle+'),'(954,488)--(977,477)--(993,489)',None)
G['cup']=graphic('A021G06',[1000,849,1148,984],925,[r'\draw[line width=.5pt] (1018,860)..controls(1007,891)and(1036,928)..(1062,924)..controls(1089,922)and(1089,889)..(1088,869);',r'\draw[line width=.45pt] (1007,874)--(1064,868);'],[(1009,966,r'\scriptstyle\alpha\in K_0')],None,r'\bigcup_{\alpha\in K_0}','complete cup, crossing high stroke and lower limit; preceding X/setminus outside','c06_crossed_cup.png')
G['s6']=sig('A021G07',[1142,831,1241,934],912,'(1153,875)--(1192,873)','(1155,882)--(1182,887)..controls(1186,894)and(1167,902)..(1154,910)..controls(1177,914)and(1205,907)..(1213,906)',(1194,926,r'\scriptstyle\alpha'),(1210,895,r'\scriptstyle+'),'(1170,847)..controls(1185,846)and(1199,840)..(1205,837)--(1217,849)','c06_crossed_cup.png',qual='detached point and pale lower trace: role, hand and surface origin unresolved',extra=[r'\fill (1157,856) circle[radius=.65];',r'\draw[gray,line width=.2pt] (1155,861)..controls(1153,864)and(1156,866)..(1155,869);'])
G['s7']=sig('A021G08',[911,1078,1034,1178],1152,'(916,1117)--(959,1112)','(921,1124)--(950,1129)--(916,1152)--(970,1150)',(982,1166,r'\scriptstyle\alpha_0'),(985,1122,r'\scriptstyle+'),'(929,1104)--(954,1085)--(999,1100)',None)
G['s8']=sig('A021G09',[1132,1098,1280,1181],1150,'(1143,1113)--(1184,1111)','(1146,1119)--(1173,1127)--(1137,1149)..controls(1154,1147)and(1188,1142)..(1197,1147)',(1210,1164,r'\scriptstyle\unsure{\alpha_0|\alpha}'),crop='c07_final_alpha.png',extra=[r'\draw[line width=.4pt] (1232,1106)..controls(1244,1103)and(1257,1101)..(1260,1106);'])
G['s9']=sig('A021G10',[620,1318,758,1414],1387,'(637,1349)--(683,1340)','(638,1357)--(666,1365)--(630,1387)--(688,1381)',(695,1396,r'\scriptstyle\alpha_0'),(709,1346,r'\scriptstyle+'),crop='c11_exclusion.png')
G['relation']=graphic('A021G11',[777,1327,845,1417],1378,[r'\draw[line width=.5pt] (837,1348)..controls(813,1348)and(793,1356)..(780,1369)..controls(775,1378)and(797,1379)..(833,1375);',r'\draw[line width=.5pt] (818,1331)--(800,1414);'],annotation=r'\not\subset',owner='complete crossed inclusion, both strokes; neighbouring Sigmas outside',crop='c11_exclusion.png')
G['s10']=sig('A021G12',[849,1320,953,1401],1378,'(881,1328)--(894,1324)','(862,1338)..controls(884,1340)and(895,1347)..(887,1357)--(858,1377)..controls(873,1374)and(893,1370)..(901,1373)',(911,1385,r'\scriptstyle i'),(928,1344,r'\scriptstyle+'),crop='c11_exclusion.png',extra=[r'\draw[gray,line width=.25pt] (862,1332)--(878,1329);',r'\fill[gray] (855,1336) circle[radius=.5];'])
G['s11']=sig('A021G13',[302,1559,415,1639],1625,'(318,1580)--(352,1575)','(315,1587)--(343,1598)--(310,1625)--(367,1618)',(369,1628,r'\scriptstyle i'),(381,1579,r'\scriptstyle+'),crop=None)
G['s12']=sig('A021G14',[452,1564,556,1637],1612,'(464,1582)--(497,1578)','(464,1588)--(489,1594)--(463,1610)--(510,1607)',(501,1627,r'\scriptstyle\alpha'),(524,1582,r'\scriptstyle+'),crop=None)
G['s13']=sig('A021G15',[947,1909,1057,1995],1978,'(955,1948)--(994,1944)','(961,1954)--(982,1960)--(954,1977)--(1017,1975)',(1019,1986,r'\scriptstyle\alpha'),(1033,1958,r'\scriptstyle+'),'(992,1932)--(1023,1918)--(1044,1932)',None)
G['s14']=sig('A021G16',[525,2297,635,2345],2341,'(539,2318)--(581,2316)','(539,2326)--(568,2331)--(536,2342)--(587,2341)',(594,2340,r'\scriptstyle\alpha'),(609,2315,r'\scriptstyle+'),crop='c14_bottom_conditions.png')
G['s15']=sig('A021G17',[1156,2290,1216,2340],2326,'(1165,2301)--(1183,2304)','(1166,2308)--(1181,2312)--(1168,2323)--(1190,2325)',(1189,2334,r'\scriptstyle\alpha'),crop='c14_bottom_conditions.png')
G['cancelSigma']=graphic('A021G19',[1137,484,1246,547],532,[r'\draw[line width=.35pt] (1150,499)--(1202,494);',r'\draw[line width=.35pt] (1152,505)--(1186,518)--(1143,529)--(1203,529);',r'\draw[line width=.55pt] (1141,526)--(1172,490)--(1202,492)--(1164,525)--(1215,510)--(1177,535)--(1230,515)--(1201,538);'],[(1220,541,r'\scriptstyle\alpha')],qual='cancelled Sigma-alpha candidate; index remains uncertain',annotation=r'\deleted{\unsure{\Sigma_\alpha}}',owner='cancelled Sigma and alpha, all crossing strokes; K condition and main brace outside',crop='c04_first_brace_cancel.png')
G['brace1']=graphic('A021G18',[1103,401,1480,635],543,[r'\draw[line width=.4pt] (1135,418)..controls(1133,458)and(1131,492)..(1128,526)..controls(1126,547)and(1120,555)..(1115,555)..controls(1110,552)and(1107,548)..(1109,551)..controls(1125,560)and(1122,574)..(1119,601)..controls(1118,615)and(1118,627)..(1121,632);'],[(1160,447,r'K=K_1\cup\{i\}'),(1137,532,G['cancelSigma'])],owner='K=K1 union {i}, incomplete-top-arm main brace, and nested complete cancelled group; no U formula',crop='c04_first_brace_cancel.png')
G['faintpair']=graphic('A021M01',[834,415,892,448],440,[r'\draw[gray!70,line width=.2pt] (840,421)--(848,423) (852,423)--(861,425) (865,426)--(878,428);',r'\draw[gray!70,line width=.2pt] (841,436)--(849,438) (854,438)--(864,440) (868,441)--(887,443);'],qual='two pale interrupted traces; role, hand and surface origin unresolved',owner='two faint traces only; aura and both displays outside',crop='c03_parenthesis_prose.png')
G['lefttick']=graphic('A021M02',[102,880,122,901],895,[r'\draw[gray,line width=.2pt] (109,892)--(116,886);'],qual='pale oblique trace; role, hand and surface origin unresolved',owner='isolated left-margin tick only',crop=None)
G['leadin']=graphic('A021G20',[1352,1129,1420,1183],1161,[r'\draw[line width=.45pt] (1365,1149)..controls(1369,1161)and(1364,1171)..(1357,1176);',r'\draw[line width=.45pt] (1364,1133)--(1367,1139);',r'\fill (1378,1155) circle[radius=1.1];',r'\fill (1381,1161) circle[radius=1.1];',r'\draw[line width=.45pt] (1395,1144)..controls(1391,1148)and(1392,1155)..(1398,1160);',r'\fill (1410,1159) circle[radius=1.1];'],qual='complete candidates j:e., j.e., i:e., i.e.; two intermediate points present, attachment unresolved',annotation=r'\text{j:e.}\mid\text{j.e.}\mid\text{i:e.}\mid\text{i.e.}',owner='complete small marginal lead-in including j dot, two intermediate points, e, final point; diagram outside',crop='c08_margin_leadin.png')
G['cancelVerb']=graphic('A021G21',[588,1428,721,1497],1471,[r'\draw[line width=.35pt] (595,1459)--(595,1472)..controls(615,1469)and(636,1467)..(652,1467)..controls(658,1473)and(658,1487)..(665,1484)..controls(673,1476)and(666,1458)..(665,1436)..controls(664,1428)and(663,1432)..(665,1454)..controls(667,1475)and(682,1477)..(704,1479);',r'\fill (596,1452) circle[radius=1];',r'\draw[line width=.35pt] (701,1448)--(701,1461);',r'\draw[line width=.55pt] (594,1471)..controls(631,1471)and(683,1462)..(710,1459)..controls(715,1458)and(714,1464)..(714,1465);'],qual='complete cancelled candidates impli / impl.; no expanded ending',annotation=r'\deleted{\text{impli}}\mid\deleted{\text{impl.}}',owner='cancelled word only, including initial point, surviving loop and cancellation run; ce qui and live signifie outside',crop='c12_cancel_live_verb.png')
G['pi']=graphic('A021G22',[490,1863,597,1929],1907,[r'\draw[gray,line width=.25pt] (493,1875)--(516,1867);',r'\draw[line width=.35pt] (501,1875)--(509,1906);',r'\draw[gray,line width=.25pt] (520,1880)--(521,1888);',r'\draw[line width=.45pt] (521,1890)..controls(522,1901)and(524,1907)..(528,1910);',r'\draw[line width=.4pt] (529,1871)..controls(533,1871)and(536,1873)..(537,1876);'],[(541,1923,r'\scriptstyle\mathrm I'),(570,1882,r'\scriptstyle\unsure{\circ|0}')],annotation=r'\Pi_I^{\unsure{\circ|0}}',owner='complete Pi, all separated/pale head pieces, lower I and ring; V de and comma outside',crop='c13_pi_ring.png')
G['vpoint']=graphic('A021M03',[321,1836,336,1853],1848,[r'\fill[gray] (327,1843) ellipse[x radius=.5,y radius=1.2];'],qual='small pale point above V; role, hand and surface origin unresolved',owner='point only; V and de outside',crop='c13_pi_ring.png')
G['VE']=graphic('A021G23',[1422,2182,1504,2263],2247,[r'\draw[gray,line width=.3pt] (1426,2194)--(1442,2250)--(1450,2198);',r'\draw[line width=.45pt] (1434,2204)--(1438,2246)--(1466,2243);',r'\draw[line width=.45pt] (1434,2189)--(1462,2187);',r'\draw[line width=.45pt] (1437,2223)--(1463,2220);'],[(1468,2250,r'\scriptstyle\alpha')],annotation=r'\deleted V E_\alpha',owner='overwritten V and live E-alpha together; i.e., intersection and dotted V outside',crop='c14_bottom_conditions.png')
G['brace2']=graphic('A021G24',[463,2225,501,2345],2298,[r'\draw[line width=.4pt] (486,2230)..controls(486,2264)and(483,2287)..(477,2295)..controls(471,2298)and(463,2289)..(468,2289)..controls(483,2288)and(486,2302)..(489,2327)--(494,2344);'],owner='left brace only, through its surviving lower stem at the physical page edge; no unseen lower return',crop='c14_bottom_conditions.png')
G['border']=graphic('A021G25',[251,1811,277,2343],2333,[r'\draw[line width=.4pt] (261,1816)..controls(264,1861)and(266,1954)..(267,2029)..controls(269,2078)and(267,2113)..(260,2157)..controls(257,2178)and(262,2277)..(261,2334);'],owner='corollary left vertical rule only; title and all words outside',crop=None)

# Diagram: a genuine tikz-cd surface with a fixed anchor; all five object rows,
# the two braces and the transverse labels are local TikZ overlays in that surface.
# Coordinates below are full scan coordinates transformed only by the declared origin.
diag_paths=[
 r'\draw[line width=.4pt] (58,30)..controls(62,23)and(77,25)..(100,25)..controls(140,26)and(162,45)..(181,40)..controls(200,35)and(205,19)..(196,21)..controls(184,23)and(188,37)..(207,41)..controls(238,46)and(281,45)..(307,35);',
 r'\draw[line width=.4pt] (42,77)..controls(61,67)and(83,72)..(112,70)..controls(126,68)and(129,60)..(126,54)..controls(120,48)and(120,59)..(127,65)..controls(144,73)and(170,68)..(192,74)..controls(198,76)and(201,79)..(204,82);',
 r'\draw[line width=.4pt] (48,35)--(74,36);',
 r'\draw[line width=.4pt] (48,39)--(60,42)--(46,52)..controls(59,52)and(75,56)..(77,56)--(80,64);',
 r'\fill (91,45) circle[radius=.8];',r'\draw[line width=.4pt] (95,33)--(109,34);',
 r'\draw[line width=.4pt] (185,46)--(201,51);',r'\draw[line width=.4pt] (183,50)--(195,55)--(180,63)--(197,66)--(201,74);',r'\fill (207,62) circle[radius=.8];',r'\draw[line width=.4pt] (215,56)--(225,61) (221,52)--(219,64);'
]
# Third upright row is literal: the point and low alpha are retained once;
# invisible candidates record the uncertain interpretation of their attachment.
third=graphic('A021D03',[1534,1086,1616,1138],1118,[r'\draw[line width=.35pt] (1540,1097)--(1567,1094);',r'\draw[line width=.4pt] (1541,1102)--(1560,1107)--(1538,1118)--(1575,1118);',r'\fill (1582,1107) circle[radius=.9];',r'\draw[line width=.35pt] (1583,1120)..controls(1588,1113)and(1595,1114)..(1596,1120)..controls(1596,1125)and(1587,1125)..(1583,1121)..controls(1594,1124)and(1601,1119)..(1603,1115)..controls(1601,1122)and(1607,1125)..(1611,1124);'],qual='Sigma_i-alpha / Sigma_i,alpha / Sigma_dot-alpha; point attachment and absent separate i-body remain open',annotation=r'\Sigma_{i\alpha}\mid\Sigma_{i,\alpha}\mid\Sigma_{\dot\alpha}',owner='third upright diagram Sigma, detached point and low alpha only',crop='c09_margin_diagram.png')
# Normal glyphs in other rows keep their head separation through complete literal groups.
d1=sig('A021D01',[1505,957,1582,1015],994,'(1511,970)--(1537,968)','(1512,975)--(1528,980)--(1509,995)--(1540,995)',(1542,1005,r'\scriptscriptstyle i'),(1551,975,r'\scriptscriptstyle+'),crop='c09_margin_diagram.png')
d2=sig('A021D02',[1603,961,1665,1017],1000,'(1611,977)--(1634,976)','(1612,982)--(1627,986)--(1611,1001)--(1635,1001)',(1636,1010,r'\scriptscriptstyle i'),crop='c09_margin_diagram.png',extra=[r'\draw[line width=.35pt] (1640,974)--(1655,975);'])
d4=sig('A021D04',[1518,1206,1640,1279],1251,'(1530,1218)--(1565,1216)','(1533,1224)--(1553,1231)--(1528,1251)--(1574,1249)',(1578,1260,r'\scriptscriptstyle\alpha_0'),(1590,1228,r'\scriptscriptstyle+'),crop='c09_margin_diagram.png')
# Use full-source overlays in the fixed diagram surface. All glyph nodes have base-west anchors.
sideSign=graphic('A021D05',[1472,1122,1498,1176],1165,[r'\fill (1480,1156) circle[radius=.9];',r'\draw[line width=.4pt] (1487,1145)..controls(1487,1137)and(1487,1131)..(1491,1125);'],qual='upright ! on page / sideways ou / dash; selected point and curved stroke remain literal',annotation=r'\rotatebox{-90}{$!$}\mid\text{ou}\mid-',owner='middle transverse point and curved stroke only; both transverse Sigmas outside',crop='c09_margin_diagram.png')
pale=graphic('A021M04',[1457,1244,1473,1266],1260,[r'\draw[gray,line width=.2pt] (1463,1259)--(1466,1247);'],qual='short detached pale stroke; brace continuation, role, hand and surface origin open',owner='short pale stroke below/left of outer brace only',crop='c09_margin_diagram.png')
DG='''% A021DG BEGIN; complete marginal diagram; fixed source origin (1435,948).
\\diagram{\\begin{tikzcd}[ampersand replacement=\\&,column sep=0pt,row sep=0pt,execute at end picture={
\\begin{scope}[shift={(A021DGanchor.north west)},x=.055mm,y=-.055mm]
\\begin{scope}[shift={(-1435,-948)}]
'''
for x,y,body in [(1505,994,d1),(1603,1000,d2),(1534,1118,third),(1518,1251,d4),(1472,1165,sideSign),(1457,1260,pale)]:
 DG+=f'\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({x},{y}) {{${body}$}};\n'
for x,y,text in [(1567,998,r'\scriptscriptstyle\text{ou}'),(1528,1063,r'\scriptstyle E_i'),(1515,1181,r'\scriptstyle E_\alpha')]:
 DG+=f'\\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ({x},{y}) {{${text}$}};\n'
DG+='\\begin{scope}[shift={(1435,1285)},cm={0,-1,1,0,(0,0)}]\n'+'\n'.join(diag_paths)+'\n\\end{scope}\n\\end{scope}\n\\end{scope}\n}]\n|[alias=A021DGanchor,anchor=north west,inner sep=0pt,outer sep=0pt]| \\phantom{\\rule{12.76mm}{18.54mm}}\n\\end{tikzcd}}\n% A021DG END\n'
groups.append({'tex_fragment':DG,'id':'A021DG','bbox':[1435,948,1667,1285],'source_origin':[1435,948],'baseline_y':None,'coordinate_map':'Outer diagram x=.055mm,y=-.055mm; overlay origin is A021DGanchor.north west; shift(-1435,-948) retains full source coordinates. Transverse/brace scope maps (u,v) to full (1435+v,1285-u). This is the clockwise crop inverse, no image alignment calculation. Fixed invisible diagram rectangle12.76mm by18.54mm.','owner':'all five rows, ou, two looped braces, both transverse Sigma labels, the middle qualified sign and detached lower pale trace; j:e. lead-in outside','crop':'c09_margin_diagram.png','path_commands':diag_paths,'child_groups':['A021D01','A021D02','A021D03','A021D04','A021D05','A021M04'],'qualifier':'local qualifiers only on third index, middle sign and pale trace','annotation':None})

tex='''\\scanpage{21}
% Diplomatic reading A. Literal source groups use fixed image-coordinate origins;
% .055mm per source pixel, negative y direction. Manual geometric approximations,
% source-only validation; no compilation, rendering or metric fit is claimed.
Soit $\\alpha_0\\in K_1$, je dis que \\unsure{l'on a|on a}
\\[
'''+G['s1']+r'\cap'+G['s2']+r'=\varnothing\qquad\text{\unsure{i.e|i.e.}}\qquad'+G['s3']+r'\cap'+G['s4']+r'=\varnothing'+'''
\\]
(ce qui ach\\unsure{è|é|e}vera la d\\unsure{è|é}monstration, car on aura
'''+r'\figure{'+G['faintpair']+'}'+'''
\\[
U=X\\setminus\\bigcup_{\\alpha\\in K}
'''+G['s5']+r'\qquad'+G['brace1']+'''
\\]
comme dans le lemme.

Or \\unsure{comme|\\deleted{co}mme} on a
'''+r'\margin{'+G['lefttick']+'}'+'''
\\[
E_i\\subset U_{J,i}=X\\setminus
'''+G['cup']+G['s6']+'''
\\]
cela implique que
\\[
E_i\\subset X\\setminus
'''+G['s7']+'='+G['s8']+'''
\\]
% independent right-margin group; transverse labels run bottom-to-top.
\\margin{'''+G['leadin']+DG+'''}
d'autre part $\\alpha_0\\in K_1$ \\unsure{signifie|signifi}
\\[
'''+G['s9']+G['relation']+G['s10']+'''
\\]
ce qui $'''+G['cancelVerb']+'''$ signifie aussi que
$'''+G['s11']+r'\cap'+G['s12']+r'=\varnothing'+'''$, cqfd.

\\uline{Corollaire du lemme} Pour une classe
% The following left rule owns no text, and starts beneath the heading.
\\noindent\\begin{minipage}[t]{.04\\linewidth}
$'''+G['border']+'''$
\\end{minipage}\\begin{minipage}[t]{.93\\linewidth}
'''+r'$overset{'+G['vpoint']+r'}{V}$ de $'+G['pi']+'''$, son expression
\\[
V=X\\setminus\\bigcup_{\\alpha\\in K}
'''+G['s13']+'''
\\]
du lemme pr\\unsure{é|ê|e}c\\unsure{é|e}dent est \\uline{unique} -- on a
\\[
'''+G['brace2']+r'\begin{aligned}K={}&\{\alpha\in I\mid\overline V\cap E_\alpha\ne\varnothing\quad\text{i.e.}\quad'+G['VE']+r'\cap\dot V\ne\varnothing\}\\'+G['s14']+r"&\ \text{est l'unique comp. de }X\setminus"+G['s15']+r'\ \text{contenue dans }X\setminus V'+'''
\\end{aligned}
\\]
\\end{minipage}
% archive sheet number: 20
'''
# Do not accidentally use an accent command for the apostrophe in l'unique.
tex=tex.replace("l\\'unique","l'unique")
tex=re.sub(r'\\\[(.*?)\\\]',lambda m:'\\['+re.sub(r'\n[ \t]*\n','\n',m.group(1))+'\\]',tex,flags=re.S)
(P/'reading.tex').write_text(tex)
(P/'groups.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n')
# Store every proposed group's complete selected source with exact offsets.
source_audit=[]
for g in groups:
 start=tex.index(g['tex_fragment']); end=start+len(g['tex_fragment'])
 source_audit.append({**g,'source_file':'reading.tex','start_byte_utf8':len(tex[:start].encode()),'end_byte_utf8_exclusive':len(tex[:end].encode()),'start_line':tex.count('\n',0,start)+1,'end_line':tex.count('\n',0,end)+1,'exact_source':tex[start:end]})
(P/'source_audit.json').write_text(json.dumps({'groups':source_audit,'whole_file':'reading.tex','ordinary_text_audit':'reading.md','validation':'Source only; no compiler, rendering, metric test or mathematical proof check.'},ensure_ascii=False,indent=2)+'\n')
print('Wrote complete reading.tex and',len(groups),'source groups.')
