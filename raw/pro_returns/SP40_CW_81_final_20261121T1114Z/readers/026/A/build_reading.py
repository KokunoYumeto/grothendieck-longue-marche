from pathlib import Path
import json,re,datetime,hashlib
P=Path('out/readers/026/A')
groups={}

def group(gid, tex, box, owns, candidates, evidence, crop=None, components=None, hand='his hand', role=None):
    source='% BEGIN '+gid+'\n% complete candidates: '+json.dumps(candidates,ensure_ascii=False)+'\n'+tex.rstrip()+'\n% END '+gid+'\n'
    groups[gid]={'id':gid,'bbox':box,'coordinate_space':'full scan, x right and y down','owns':owns,'complete_candidates':candidates,'evidence':evidence,'crop':crop,'components':components or [],'hand':hand,'role':role,'tex':source}
    return source

def graphic(gid, box, paths, annotation, candidates, evidence, crop=None, nodes=None, qualify=False, owns=None, hand='his hand', role=None):
    x0,y0,x1,y1=box
    s=['\\mathord{'+('\\unsure{' if qualify else '')+'\\tikz[x=0.10mm,y=-0.10mm,baseline=(base)]{',f'\\path[use as bounding box] (0,0) rectangle ({x1-x0},{y1-y0});',f'\\coordinate (base) at (0,{y1-y0-3});',f'\\begin{{scope}}[shift={{({-x0},{-y0})}}]', '% Native source pixels; manual paths, not a metric reconstruction.']
    s.extend(paths)
    if nodes:s.extend(nodes)
    s += [f'\\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt] at ({x0},{y1-3}) {{\\phantom{{$'+(annotation or r'\vphantom{\Sigma}')+'$}};','\\end{scope}', '}' + ('}' if qualify else '')+'}']
    return group(gid,'\n'.join(s),box,owns or annotation,candidates,evidence,crop,paths,hand,role)

def sigma(gid, box, head, body, sub='', sup='', subpos=None,suppos=None,roof=None,joined=False,crop=None,first=False,extra=None,candidates=None,qualify=False,shared_sub=False):
    # Every list below is an independently selected native-pixel path, not a scaled font template.
    paths=[]
    if roof: paths.append('\\draw[line width=.38pt,line cap=round] '+' -- '.join(f'({x},{y})' for x,y in roof)+';')
    if head: paths.append('\\draw[line width=.32pt,line cap=round] '+' -- '.join(f'({x},{y})' for x,y in head)+';')
    paths.append('\\draw[line width=.35pt,line cap=round,line join=round] '+' -- '.join(f'({x},{y})' for x,y in body)+';')
    if extra:paths+=extra
    ann=('\\overline{' if roof else '')+'\\Sigma'+('_'+('{'+sub+'}') if sub else '')+('^{'+sup+'}' if sup else '')+('}' if roof else '')
    nodes=[]
    if sub and subpos and not shared_sub:nodes.append(f'\\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\\scriptsize] at ({subpos[0]},{subpos[1]}) {{$'+sub+'$};')
    if sup and suppos:nodes.append(f'\\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\\scriptsize] at ({suppos[0]},{suppos[1]}) {{$'+sup+'$};')
    cs=candidates or ([{'reading':ann+' with joined upper head','hand':'his hand','role':'upper arm/head; no separate run supplied'}] if joined else [{'reading':ann+' with detached head/retrace','hand':'his hand','role':'head/retrace attached to this Sigma'},{'reading':ann+' with independent upper run','hand':{'body_signs_indices':'his hand','independent_upper_run':'undetermined hand'},'role':'independent upper run; semantic attachment unestablished'}])
    return graphic(gid,box,paths,ann,cs,('Upper head joins body locally. ' if joined else 'Separate upper run and lower angular body. ')+('One outer closure roof is separately retained. ' if roof else '')+('Body foot continues into the written lower 1; the index is not drawn twice.' if shared_sub else 'All shown indices and raised signs retain their local positions.'),crop,nodes,qualify or first,role='complete Sigma group with all local decorations')

S={}
S[1]=sigma('A026-S01',[603,287,679,346],[(607,306),(644,305)],[(607,313),(636,320),(608,332),(649,332)],'\\alpha','\\alpha',(654,342),(654,304),crop='crop_02_family.png',first=True)
S[2]=sigma('A026-S02',[765,827,870,885],[(774,837),(818,831)],[(775,840),(807,846),(773,869),(832,870),(858,878)],'\\alpha','',(834,883),joined=False,crop=None)
S[3]=sigma('A026-S03',[672,892,752,943],[(678,909),(710,907)],[(678,911),(704,917),(675,934),(713,934)],'\\alpha','\\alpha',(717,940),(717,910),joined=True,crop='crop_04_inserted.png')
S[4]=sigma('A026-S04',[827,887,884,943],[(832,901),(850,900),(862,897)],[(832,906),(852,913),(832,929),(863,931)],'','\\alpha',None,(862,901),crop='crop_04_inserted.png',extra=['\\fill (864,925) -- (869,921) -- (873,925) -- (877,920) -- (881,925) -- (880,936) -- (875,933) -- (874,940) -- (870,934) -- (865,935) -- cycle;'],candidates=[{'reading':'\\Sigma_{\\deleted{\\unsure{\\alpha}}}^{\\alpha}','hand':'his hand','role':'lower dark crossed predecessor; alpha candidate, replacement/state retained'}],qualify=True)
S[5]=sigma('A026-S05',[961,874,1040,925],[(968,895),(984,896)],[(965,901),(981,906),(965,921),(986,920)],'','\\alpha,\\unsure{0|\\circ|o}',None,(991,899),crop='crop_04_inserted.png',extra=['\\fill (975,882) -- (980,876) -- (983,883) -- (988,885) -- (980,887) -- (974,885) -- cycle;','\\fill (987,913) -- (993,910) -- (999,914) -- (1006,913) -- (1008,920) -- (1002,919) -- (1003,924) -- (997,921) -- (988,923) -- cycle;'],candidates=[{'reading':'\\Sigma_{\\deleted{\\unsure{\\alpha}}}^{\\deleted{\\unsure{\\alpha}}\\alpha,0}','hand':'his hand','role':'upper and lower overwritten alpha candidates; live alpha and raised 0'},{'reading':'\\Sigma_{\\deleted{\\unsure{\\alpha}}}^{\\deleted{\\unsure{\\alpha}}\\alpha,\\circ}','hand':'his hand','role':'same overwritten indices; raised circle'},{'reading':'\\Sigma_{\\deleted{\\unsure{\\alpha}}}^{\\deleted{\\unsure{\\alpha}}\\alpha,o}','hand':'his hand','role':'same overwritten indices; raised lowercase o'}],qualify=True)
S[6]=graphic('A026-S06',[1045,935,1120,995],['\\draw[line width=.45pt] (1063,953) -- (1087,959) -- (1068,974) -- (1094,976);','\\draw[line width=.38pt] (1097,975) .. controls (1106,971) and (1113,983) .. (1104,989) .. controls (1109,990) and (1114,991) .. (1116,993);','\\draw[line width=.40pt] (1055,940) -- (1094,976);','\\draw[line width=.37pt] (1082,938) -- (1061,964);','\\draw[line width=.35pt] (1090,946) -- (1064,971);'],'\\deleted{\\unsure{\\Sigma_\\alpha|\\text{les}}}',[{'reading':'\\deleted{\\Sigma_\\alpha}','hand':'his hand','role':'cancelled indexed Sigma'},{'reading':'\\deleted{les}','hand':'his hand','role':'cancelled prose group'}],'Crossing strokes traverse the upper and low body; low right return remains visible.','crop_04_inserted.png',qualify=True)
S[7]=sigma('A026-S07',[787,1005,883,1077],[(797,1037),(832,1032)],[(797,1038),(822,1044),(793,1063),(835,1061)],'','\\alpha',None,(848,1028),joined=True,crop='crop_05_si_condition.png',extra=['\\fill (851,1054) -- (858,1050) -- (865,1056) -- (871,1056) -- (874,1063) -- (880,1065) -- (879,1072) -- (874,1067) -- (872,1075) -- (866,1067) -- (858,1066) -- (850,1064) -- cycle;'],candidates=[{'reading':'\\Sigma_{\\deleted{\\unsure{\\alpha}}}^{\\alpha}','hand':'his hand','role':'lower crossed predecessor retained separately from live upper alpha'}],qualify=True)
S[8]=sigma('A026-S08',[762,1097,883,1163],[(779,1127),(814,1121)],[(778,1128),(809,1134),(776,1153),(824,1151)],'\\alpha','\\alpha,0',(826,1160),(831,1121),joined=True,crop='crop_06_connexe_correction.png')
S[9]=sigma('A026-S09',[473,1222,606,1298],[(484,1250),(521,1248)],[(484,1252),(515,1263),(477,1288),(530,1286)],'','\\alpha,0',None,(536,1257),roof=[(491,1238),(600,1230)],joined=True,crop='crop_09_closure_first.png')
S[10]=sigma('A026-S10',[1100,1173,1242,1236],[(1114,1198),(1153,1193)],[(1114,1200),(1142,1209),(1107,1228),(1152,1227)],'','\\alpha,0',None,(1163,1209),roof=[(1144,1178),(1237,1178)],joined=True,crop='crop_10_closure_equation.png')
S[11]=sigma('A026-S11',[1381,1155,1514,1221],[(1392,1183),(1426,1183)],[(1392,1187),(1418,1193),(1384,1213),(1427,1212)],'','\\alpha,0',None,(1438,1195),roof=[(1384,1166),(1507,1160)],crop='crop_10_closure_equation.png')
S[12]=sigma('A026-S12',[1540,1174,1636,1220],[(1545,1184),(1580,1183)],[(1545,1188),(1572,1194),(1544,1213),(1584,1213)],'','\\alpha,0',None,(1588,1196),crop='crop_10_closure_equation.png')
S[13]=sigma('A026-S13',[410,1371,522,1423],[(423,1382),(450,1377)],[(418,1388),(443,1386),(448,1391),(419,1415),(456,1413)],'','\\alpha,0',None,(462,1391),crop='crop_11_et_sigma.png')
S[14]=graphic('A026-S14',[451,1472,576,1521],['\\draw[line width=.28pt] (458,1487) -- (487,1482);','\\draw[line width=.31pt] (459,1493) -- (480,1494) -- (486,1499) -- (459,1514) -- (490,1511);','\\draw[line width=.29pt] (514,1490) -- (515,1486) -- (523,1487) -- (533,1488);','\\draw[line width=.40pt] (542,1490) -- (541,1496);','\\draw[line width=.36pt] (553,1484) .. controls (552,1489) and (558,1489) .. (559,1483);','\\draw[line width=.25pt,black!50] (567,1491) .. controls (571,1499) and (569,1508) .. (563,1515);'],'\\Sigma^{\\unsure{-,0|\\alpha,0|-\\alpha,0}},',[{'reading':'\\Sigma^{-,0},','hand':'his hand','role':'short raised first stroke read as minus; lower comma separate'},{'reading':'\\Sigma^{\\alpha,0},','hand':'his hand','role':'short raised first stroke read as reduced alpha; lower comma separate'},{'reading':'\\Sigma^{-\\alpha,0},','hand':'his hand','role':'raised cluster read as minus-alpha; lower comma separate'}],'First raised run is shallow with a short left hook; the lower long comma is separate.','crop_12_car_sigma.png',qualify=True,owns='complete Sigma, upper pair and following baseline comma')
# Expand the independently retained ring reading in this complete superscript group.
car_states=[]
for first_sign in ['-','\\alpha','-\\alpha']:
    for ring in ['0','\\circ','o']:
        car_states.append({'reading':'\\Sigma^{'+first_sign+','+ring+'},','hand':'his hand','role':'complete raised pair; following low comma separate; upper head retains recorded role qualification'})
car_old=groups['A026-S14']['tex']
car_new=group('A026-S14',car_old.split('\n',2)[2].rsplit('% END A026-S14',1)[0],[451,1472,576,1521],groups['A026-S14']['owns'],car_states,groups['A026-S14']['evidence'],'crop_12_car_sigma.png',groups['A026-S14']['components'],role='complete car Sigma group; 3 first-sign readings by 3 round-mark readings')
S[14]=car_new

# Margin Sigmas are represented in the diagram frame, below.
# Lower family, prose and displays: every native path selected independently.
S[17]=sigma('A026-S17',[117,1653,186,1713],[(125,1665),(151,1660)],[(125,1667),(148,1670),(124,1685),(145,1684),(125,1705),(153,1705)],'1','+',(159,1710),(161,1673),joined=True,crop='crop_14_pairs_correction.png')
S[18]=sigma('A026-S18',[192,1655,254,1711],[(198,1666),(225,1668)],[(198,1674),(221,1678),(199,1701),(228,1701)],'1','-',(230,1709),(234,1669),crop='crop_14_pairs_correction.png')
S[19]=sigma('A026-S19',[334,1635,398,1689],[(341,1645),(362,1641)],[(340,1656),(359,1656),(342,1680),(366,1680)],'2','+',(368,1687),(374,1651),crop='crop_14_pairs_correction.png')
S[20]=sigma('A026-S20',[407,1634,464,1688],[(411,1646),(430,1645)],[(412,1654),(428,1658),(413,1676),(432,1676)],'2','-',(436,1685),(445,1652),crop='crop_14_pairs_correction.png')
S[21]=sigma('A026-S21',[932,1745,1004,1804],[(936,1755),(970,1751)],[(936,1759),(963,1762),(937,1788),(973,1787)],'1','+',(976,1800),(984,1757),crop=None)
S[22]=sigma('A026-S22',[1410,1723,1499,1777],[(1417,1732),(1453,1731)],[(1418,1738),(1444,1744),(1419,1767),(1453,1767)],'2','+',(1458,1773),(1470,1736),crop=None)
S[23]=sigma('A026-S23',[649,1947,743,2014],[(658,1968),(697,1963)],[(658,1973),(683,1978),(653,1999),(694,1998)],'1','+',(705,2010),(707,1971),crop='crop_17_disjoint.png')
S[24]=sigma('A026-S24',[801,1945,889,2011],[(808,1961),(842,1962)],[(808,1968),(837,1973),(810,1993),(849,1993)],'2','+',(850,2007),(866,1964),crop='crop_17_disjoint.png')
S[25]=sigma('A026-S25',[650,2096,739,2154],[(658,2113),(695,2108)],[(658,2120),(685,2125),(659,2147),(710,2141),(711,2151)],'1','+',None,(712,2114),shared_sub=True,crop='crop_19_first_inclusion.png')
S[26]=sigma('A026-S26',[796,2092,882,2149],[(803,2106),(829,2106)],[(803,2111),(824,2117),(806,2136),(834,2137)],'2','-',(839,2145),(849,2106),crop='crop_19_first_inclusion.png')
S[27]=sigma('A026-S27',[1132,2069,1223,2139],[(1142,2085),(1180,2081)],[(1140,2090),(1171,2095),(1139,2120),(1184,2118)],'1','+',(1189,2136),(1195,2090),crop=None)
S[28]=sigma('A026-S28',[1248,2070,1339,2134],[(1257,2087),(1294,2087)],[(1257,2092),(1283,2098),(1258,2119),(1297,2118)],'2','-',(1302,2131),(1315,2089),crop=None)
S[29]=sigma('A026-S29',[1391,2066,1474,2137],[(1402,2083),(1437,2078)],[(1401,2087),(1426,2092),(1399,2116),(1440,2116)],'1','+',(1441,2135),(1448,2089),crop=None)
S[30]=sigma('A026-S30',[645,2181,747,2247],[(654,2196),(699,2189)],[(655,2202),(693,2207),(650,2237),(704,2233)],'2','+',(708,2242),(719,2198),crop='crop_20_second_equality.png')
S[31]=sigma('A026-S31',[807,2177,891,2240],[(817,2192),(844,2185)],[(813,2196),(841,2199),(812,2225),(851,2223)],'1','-',(859,2238),(863,2192),joined=True,crop='crop_20_second_equality.png')
S[32]=sigma('A026-S32',[1136,2166,1229,2230],[(1144,2178),(1179,2174)],[(1144,2181),(1174,2187),(1143,2217),(1190,2214)],'2','+',(1200,2226),(1208,2182),joined=True,crop='crop_20_second_equality.png')
S[33]=sigma('A026-S33',[1263,2168,1350,2232],[(1275,2184),(1306,2183)],[(1275,2185),(1300,2193),(1274,2211),(1312,2211),(1327,2210),(1331,2229)],'1','-',None,(1320,2175),shared_sub=True,joined=True,crop='crop_20_second_equality.png')
S[34]=sigma('A026-S34',[1374,2167,1468,2225],[(1385,2179),(1410,2175)],[(1384,2184),(1407,2191),(1381,2213),(1413,2212)],'2','+',(1430,2222),(1442,2181),joined=True,crop='crop_20_second_equality.png')
S[35]=sigma('A026-S35',[531,2273,625,2336],[(540,2287),(582,2281)],[(541,2290),(571,2297),(537,2324),(583,2321)],'12','',(585,2334),joined=True,crop='crop_21_bottom.png')
S[36]=sigma('A026-S36',[658,2265,748,2330],[(664,2284),(706,2284)],[(664,2290),(694,2296),(662,2318),(708,2318)],'1','-',(715,2327),(717,2279),crop='crop_21_bottom.png')
S[37]=sigma('A026-S37',[784,2271,872,2331],[(791,2283),(819,2279)],[(792,2288),(815,2294),(791,2313),(823,2314)],'2','-',(837,2328),(839,2281),crop='crop_21_bottom.png')
S[38]=sigma('A026-S38',[1164,2259,1254,2325],[(1173,2272),(1208,2274)],[(1174,2276),(1200,2284),(1174,2309),(1211,2311)],'1','-',(1224,2322),(1227,2274),joined=True,crop='crop_21_bottom.png')
S[39]=sigma('A026-S39',[1277,2261,1366,2326],[(1285,2277),(1317,2273)],[(1285,2280),(1310,2288),(1290,2309),(1318,2311)],'2','-',(1331,2323),(1335,2273),joined=True,crop='crop_21_bottom.png')

# Hidden state annotations retain the exact complete corrected indices while literal paths
# draw each predecessor only once in its original local position.
for n,ann in [(4,r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}'),(5,r'\Sigma_{\deleted{\unsure{\alpha}}}^{\deleted{\unsure{\alpha}}\alpha,\unsure{0|\circ|o}}'),(7,r'\Sigma_{\deleted{\unsure{\alpha}}}^{\alpha}')]:
    a=S[n].find(r'\phantom{$');b=S[n].find('$}};',a)
    assert a>=0 and b>=0
    S[n]=S[n][:a]+r'\phantom{$'+ann+S[n][b:]
    groups[f'A026-S{n:02d}']['tex']=S[n]

G={}
G['hemi']=group('A026-G01',r'''\unsure{\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (73,55);
\coordinate (b) at (0,53);
\draw[line width=.37pt] (20,6) .. controls (39,8) and (29,32) .. (19,34) .. controls (14,38) and (26,51) .. (30,49) -- (36,43) -- (46,48) -- (64,50);
\draw[line width=.38pt] (2,28) -- (44,28);
\draw[line width=.34pt] (3,29) -- (30,39);
\node[overlay,inner sep=0pt] at (30,35) {\phantom{\deleted{h}}};
}}émisphères''',[286,857,660,937],'complete hémisphères word; literal initial h and adjoining émisphères once',[{'reading':'hémisphères with retraced initial h','hand':'his hand','role':'live word; crossing run interpreted as retrace'},{'reading':'\\deleted{h}émisphères','hand':'his hand','role':'initial h cancelled; continuation live'},{'reading':'\\deleted{hémisphères}','hand':'his hand','role':'whole-word cancellation signalled at initial h'}],'Initial loop is crossed by a short horizontal and oblique stroke; rest of the word remains unobstructed.','crop_03_hemispheres.png',role='uncertain cancellation scope at first h')
G['de']=group('A026-G02',r'''\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (265,115);
\coordinate (b) at (0,108);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,102) {et};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (109,42) {\inserted{de}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (124,102) {plus,};
\draw[line width=.32pt] (94,107) .. controls (100,76) and (138,64) .. (177,51);
}''',[1330,748,1595,863],'et, inserted de, plus, and its bent guide',[{'reading':'et \\inserted{de} plus, with observed guide','hand':'his hand','role':'insertion de before plus'}],'Raised de and a long curved diagonal into the gap before plus are visible on half a.','half_a',components=['curved insertion guide'])
G['insert']=group('A026-G03',r'''\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (490,140);
\coordinate (b) at (0,133);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,64) {\inserted{$'''+S[3]+r'''\text{ et }'''+S[4]+r'''\setminus E='''+S[5]+r'''$}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (105,130) {connexes};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (395,130) {$'''+S[6]+r'''$};
\draw[line width=.30pt] (308,57) .. controls (311,83) and (227,85) .. (185,84) .. controls (94,81) and (83,96) .. (99,132);
}''',[650,865,1140,1005],'inserted complete equation, following connexes, cancelled post-connexes group, and guide; no neighbouring et owned',[{'reading':'\\inserted{\\Sigma_\\alpha^\\alpha et \\Sigma_{\\deleted{\\unsure{\\alpha}}}^\\alpha\\setminus E=\\Sigma_{\\deleted{\\unsure{\\alpha}}}^{\\deleted{\\unsure{\\alpha}}\\alpha,\\unsure{0|\\circ|o}}} connexes \\deleted{\\unsure{\\Sigma_\\alpha|les}}','hand':'his hand','role':'raised equation attached before connexes; all local alternatives remain in S03-S06'}],'Curved guide begins under the equation and turns down beside connexes.','crop_04_inserted.png',components=['one bent guide','S03','S04','S05','S06'])
G['ne']=graphic('A026-G04',[1353,1005,1403,1043],['\\draw[line width=.29pt] (1378,1011) -- (1387,1012) -- (1389,1016);','\\draw[line width=.32pt] (1358,1025) -- (1384,1025);','\\draw[line width=.36pt] (1380,1008) -- (1373,1039);'],'\\unsure{\\ne|+}',[{'reading':'\\ne','hand':'his hand','role':'short upper stroke, lower horizontal and slant'},{'reading':'+','hand':'his hand','role':'cross plus; small upper-right fragment retained without assigned operation'}],'Short upper fragment projects right of the slant; the lower horizontal is longer.','crop_05_si_condition.png',qualify=True)
G['correct']=group('A026-G05',r'''\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (500,132);
\coordinate (b) at (0,124);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (0,60) {\inserted{$X$ connexe, \deleted{et}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (44,123) {\rlap{les $'''+S[8]+r'''$ connexes}\phantom{\deleted{les $\Sigma_\alpha^{\alpha,0}$ connexes}}};
\draw[line width=.29pt,black!55] (36,130) .. controls (16,71) and (184,59) .. (351,21) .. controls (369,17) and (373,19) .. (368,24);
\draw[line width=.45pt] (37,119) -- (484,79);
}''',[603,1063,1103,1195],'inserted X connexe, cancelled et; cancelled les Sigma_alpha^{alpha,0} connexes; guide and strike',[{'reading':'\\deleted{les \\Sigma_\\alpha^{\\alpha,0} connexes}, \\inserted{X connexe, \\deleted{et}}','hand':'his hand','role':'replacement above deleted clause; et separately cancelled'}],'Upper replacement and lower crossed clause retain two separate long runs. The curved upper run is pale in its right half.','crop_06_connexe_correction.png',components=['one curved guide','one long crossing stroke','S08'])
G['aussitot']=group('A026-G06',r'''\deleted{\unsure{aussitôt|aussitot}}''',[1465,1055,1640,1115],'complete crossed aussitôt/aussitot',[{'reading':'\\deleted{aussitôt}','hand':'his hand','role':'cancelled word with circumflex reading'},{'reading':'\\deleted{aussitot}','hand':'his hand','role':'cancelled word without assigned circumflex'}],'Opening au and final tall strokes remain; cancellation crowds the ending and accent.','crop_07_aussitot.png')
G['Efirst']=graphic('A026-G07',[668,1234,714,1280],['\\draw[line width=.29pt] (675,1245) -- (675,1273) -- (693,1271);','\\draw[line width=.24pt,black!45] (676,1258) -- (692,1255);','\\draw[line width=.21pt,black!40] (678,1243) -- (685,1241);','\\draw[line width=.33pt] (699,1239) -- (703,1238) -- (707,1242);'],'E',[{'reading':'E with interrupted/detached top arm','hand':'his hand','role':'pale upper fragment and dark short return assigned to top arm'},{'reading':'E with independent upper-right mark','hand':{'E_body':'his hand','upper_right_mark':'undetermined hand'},'role':'small upper-right return independent; attachment unresolved'}],'Upper arm has a pale short approach and detached dark right return.','crop_09_closure_first.png',qualify=True)
G['faint']=graphic('A026-M01',[450,1259,471,1302],['\\draw[line width=.21pt,black!25] (451,1264) .. controls (466,1264) and (470,1280) .. (465,1289) .. controls (462,1297) and (458,1299) .. (453,1300);'],'',[{'reading':'faint curved trace; no character supplied','hand':'undetermined hand','role':'attachment and surface origin unresolved'}],'Faint curved trace left of the first barred Sigma. Left approach meets crop boundary; only supported visible portion is retained.','crop_09_closure_first.png',qualify=True,owns='faint trace only; no formula or word',hand='undetermined hand')
G['tick']=graphic('A026-M02',[1171,1178,1184,1188],['\\draw[line width=.28pt] (1175,1182) -- (1179,1184);'],'',[{'reading':'short dark tick below the closure roof','hand':'undetermined hand','role':'roof retrace, alpha-adjacent mark or independent trace; unassigned'}],'Detached short tick lies below the first parenthetical closure roof and above its alpha.','crop_10_closure_equation.png',qualify=True,owns='one short upper tick only',hand='undetermined hand')
G['paircorr']=group('A026-G08',r'''\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (480,132);
\coordinate (b) at (0,125);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (284,46) {\deleted{\unsure{distinctes}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (52,105) {\inserted{de $X$,}};
\draw[line width=.29pt] (0,124) .. controls (19,74) and (88,72) .. (157,73) -- (275,57) .. controls (292,65) and (310,63) .. (352,58);
}''',[225,1636,705,1768],'cancelled distinctes, inserted de X comma and connecting bent guide',[{'reading':'\\deleted{\\unsure{distinctes}} \\inserted{de X,}','hand':'his hand','role':'cancelled adjective and lower insertion; guide retained'}],'Letter remnants support distinctes; crossing strokes still obscure parts independently of the clean lower repetition.','crop_14_pairs_correction.png',components=['one bent insertion guide'])
G['opener']=graphic('A026-G09',[313,1632,339,1688],['\\draw[line width=.31pt] (334,1640) -- (323,1640) .. controls (316,1651) and (315,1669) .. (321,1682) -- (330,1683);'],'\\unsure{[|(}',[{'reading':'[','hand':'his hand','role':'square opener with curved lower corner'},{'reading':'(','hand':'his hand','role':'rounded opener with top/bottom serif-like returns'}],'Short horizontal top and turned lower foot favour the square candidate; round opener retained.','crop_14_pairs_correction.png',qualify=True)
# Whole pair-plus-correction group: the guide stays beside its actual families and insertion.
G['paircorr']=group('A026-G08',r"""\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (645,170);
\coordinate (b) at (0,162);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (8,104) {$\{"""+S[17]+','+S[18]+r"""\},$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (223,83) {$"""+G['opener']+S[19]+','+S[20]+r"""\}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (415,77) {\deleted{\unsure{distinctes}}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (185,133) {\inserted{de $X$,}};
\draw[line width=.29pt] (135,145) .. controls (154,95) and (223,93) .. (292,94) -- (410,78) .. controls (427,86) and (445,84) .. (487,79);
}""",[90,1610,735,1780],'both complete binary pairs, cancelled distinctes, inserted de X comma, and connected bent guide',[{'reading':r'\{\Sigma_1^+,\Sigma_1^-\},[\Sigma_2^+,\Sigma_2^-\} \deleted{\unsure{distinctes}} \inserted{de X,}','hand':'his hand','role':'complete primary family/correction state; square opener'},{'reading':r'\{\Sigma_1^+,\Sigma_1^-\},(\Sigma_2^+,\Sigma_2^-\} \deleted{\unsure{distinctes}} \inserted{de X,}','hand':'his hand','role':'complete alternative family/correction state; round opener'}],'Both pairs and the lower de X insertion share the preserved bent guide context; all words and symbols occur once.','crop_14_pairs_correction.png',components=['S17','S18','G09 opener','S19','S20','cancelled distinctes','de X comma','one bent insertion guide'])
G['points']=graphic('A026-M03',[1578,1681,1595,1698],['\\fill (1589,1684) ellipse (1.2 and 1.0);','\\fill (1584,1691) ellipse (1.25 and 1.1);'],'',[{'reading':'two detached points','hand':'undetermined hand','role':'role, attachment and surface origin unresolved'},{'reading':'colon-like pair','hand':'undetermined hand','role':'punctuation-like shape; no syntactic attachment established'}],'Two small points stand below the right end of the adjective underline.','crop_15_non_adjective.png',qualify=True,owns='two points only; adjective and underline excluded',hand='undetermined hand')
G['distins']=group('A026-G10',r'''\tikz[x=.10mm,y=-.10mm,baseline=(b)]{
\path[use as bounding box] (0,0) rectangle (575,149);
\coordinate (b) at (0,143);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (2,76) {\inserted{elles sont \uline{distinctes}, et si}};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (10,140) {on peut trouver};
\draw[line width=.30pt] (0,145) .. controls (-11,102) and (75,93) .. (183,82) -- (525,19) .. controls (559,12) and (570,8) .. (565,1);
}''',[371,1710,946,1859],'inserted elles sont distinctes, et si; following on peut trouver; long bent guide; initial baseline si stays outside',[{'reading':'si \\inserted{elles sont \\uline{distinctes}, et si} on peut trouver','hand':'his hand','role':'first si remains baseline; final si belongs to insertion'}],'Long lower guide turns down beside on and ends in a short right hook. A separate underline belongs only to distinctes.','crop_16_distinctes_insertion.png',components=['one bent guide; underline generated by uline'])
G['cap']=graphic('A026-G11',[761,1971,796,1998],['\\draw[line width=.31pt] (766,1991) -- (775,1980) -- (788,1991);','\\fill (792,1990) ellipse (.65 and 1.1);'],'\\unsure{\\cap|\\wedge}',[{'reading':'\\cap with detached right-foot point','hand':'his hand','role':'angular intersection sign; point as right-foot fragment'},{'reading':'\\wedge with separate point','hand':{'angular_sign':'his hand','point':'undetermined hand'},'role':'wedge-shaped sign; point attachment unestablished'}],'Two sloping arms meet in a sharp upper vertex; a tiny detached point follows the right arm.','crop_17_disjoint.png',qualify=True,owns='one angular operator and its adjacent point')
G['reduceda']=graphic('A026-G12',[408,2107,425,2122],['\\fill (413,2112) -- (418,2111) -- (421,2114) -- (418,2117) -- (413,2116) -- cycle;'],'a',[{'reading':'a','hand':'his hand','role':'reduced letter between on and alors'},{'reading':'independent point with on and alors unchanged','hand':'undetermined hand','role':'character and attachment unestablished'}],'Filled lozenge between on and alors has no recoverable counter.','crop_18_alors.png',qualify=True,owns='single reduced a/point only; on and alors stay outside')
G['incl']=graphic('A026-G13',[748,2107,798,2146],['\\draw[line width=.42pt] (791,2114) .. controls (756,2108) and (747,2134) .. (791,2132);','\\draw[line width=.34pt] (753,2140) .. controls (756,2119) and (773,2117) .. (779,2138);','\\draw[line width=.32pt] (760,2124) -- (780,2135);'],'\\unsure{\\deleted{\\cap}\\subset|\\subset}',[{'reading':'\\deleted{\\cap}\\subset','hand':'his hand','role':'prior intersection beneath live inclusion'},{'reading':'\\subset','hand':'his hand','role':'retraced inclusion with low oblique/curved fragments'}],'Low left prong crosses the lower contour and turns inside the relation.','crop_19_first_inclusion.png',qualify=True)
G['cancelnonempty']=graphic('A026-G14',[900,2087,990,2151],['\\draw[line width=.40pt] (907,2119) -- (939,2118);','\\draw[line width=.42pt] (908,2131) -- (941,2130);','\\draw[line width=.42pt] (938,2108) -- (916,2140);','\\draw[line width=.35pt] (976,2103) .. controls (957,2113) and (958,2135) .. (977,2124) .. controls (989,2118) and (979,2104) .. (976,2103);','\\draw[line width=.45pt] (986,2090) -- (963,2148);','\\draw[line width=.65pt] (905,2117) -- (933,2127) -- (911,2134) -- (944,2110);','\\draw[line width=.43pt] (938,2130) -- (981,2109);','\\draw[line width=.40pt] (956,2131) -- (980,2116) -- (968,2140);'],'\\deleted{\\unsure{\\ne\\varnothing}}',[{'reading':'\\deleted{\\ne\\varnothing}','hand':'his hand','role':'cancelled two-sign cluster; individual glyphs remain qualified'}],'Two heavily overmarked groups end in a long slashed loop.','crop_19_first_inclusion.png',qualify=True)
G['def']=group('A026-G15',r'''\overset{\unsure{\mathrm{déf}|\mathrm{def}}}{=}''',[608,2240,652,2312],'definition label with tiny high tick and equals',[{'reading':'déf above =','hand':'his hand','role':'tiny high stroke read as acute accent over e'},{'reading':'def above = with independent high tick','hand':{'letters_and_equals':'his hand','high_tick':'undetermined hand'},'role':'tick attachment unresolved'}],'A tiny high stroke stands near the e; its attachment remains qualified.','crop_21_bottom.png')
G['bottomtrace']=graphic('A026-M04',[744,2308,755,2325],['\\draw[line width=.18pt,black!40] (748,2313) .. controls (750,2314) and (751,2317) .. (751,2319);'],'',[{'reading':'faint short curved trace','hand':'undetermined hand','role':'role, attachment and surface origin unresolved'}],'Small grey short run below-left of the first final intersection.','crop_21_bottom.png',qualify=True,owns='faint trace only; adjoining operator excluded',hand='undetermined hand')

# Margin diagram. The local frame is parallel to the segment before rotatebox.
G['margin']=group('A026-D01',r'''% margin note written sideways
\reversemarginpar\margin{\diagram{\rotatebox{52}{\begin{tikzcd}[ampersand replacement=\&,column sep=27mm,execute at end picture={
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ([xshift=6mm,yshift=15mm]left.center) {\scriptsize diagramme};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ([xshift=8mm,yshift=4mm]left.center) {$\unsure{\deleted{E}|\deleted{\Sigma}|\deleted{B}}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ([xshift=6.4mm,yshift=-2mm]left.center) {$\unsure{\tikz[x=1mm,y=1mm,baseline=0pt]{\path[use as bounding box] (0,0) rectangle (.5,.5);\fill (.25,.25) circle (.25);}}$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at ([xshift=-7mm,yshift=-10mm]left.center) {$\Sigma^{-}\mathrel{\unsure{\supset|\supseteq}}E_{\unsure{\alpha|{}}}\subset\Sigma^{+}$};
\draw[line width=.35pt] ([xshift=4.0mm,yshift=-11mm]left.center) -- ([xshift=8.5mm,yshift=-11mm]left.center);
}]
|[alias=left]|\bullet\arrow[r,dash] \& \bullet
\end{tikzcd}}}}\normalmarginpar''',[35,940,265,1390],'diagramme, two filled endpoints, connector, cancelled upper glyph, lower complete Sigma-minus superset E-tail subset Sigma-plus label, separate point and lower retrace',[{'reading':'diagramme; cancelled E; segment between filled points; \\Sigma^-\\supset E_\\alpha\\subset\\Sigma^+','hand':'his hand','role':'main diagram, E and lower alpha primary'},{'reading':'same diagram with cancelled Sigma or B','hand':'his hand','role':'upper cancelled glyph alternatives'},{'reading':'same diagram with E and its lower-right flourish, without assigned subscript','hand':'his hand','role':'E-tail attachment unresolved'},{'reading':'same diagram with superset-equals interpretation of double lower run','hand':'his hand','role':'two visible lower runs retained; relation reading qualified'},{'reading':'separate point below line','hand':'undetermined hand','role':'unestablished attachment, role and surface origin'}],'Turned crop shows full word, heavy endpoints, cancelled upper glyph, doubled lower relation run, E lower-right loop and a detached point below the segment.','crop_08_margin.png',components=['two filled endpoints','one line','cancelled upper E/Sigma/B','two lower superset runs','E alpha/flourish','point below segment'],role='native diagram frame; rotatebox 52 degrees; manual dimensions')

# Complete diagram-state candidates retain every locally varying label and the separate point.
diagram_states=[]
for old in ['E',r'\Sigma','B']:
    for middle in [r'E_\alpha','E with lower-right flourish']:
        for rel in [r'\supset',r'\supseteq']:
            diagram_states.append({'reading':'diagramme; '+r'\deleted{'+old+'}; two filled endpoints joined by one segment; '+r'\Sigma^-'+rel+middle+r'\subset\Sigma^+'+'; one separate point below the segment','hand':{'main_word_and_diagram':'his hand','separate_point':'undetermined hand'},'role':'upper glyph cancelled; E-tail and doubled-lower-relation interpretation remain local; point role/attachment/surface origin unresolved'})
old_diagram=G['margin']
body_diagram=old_diagram.split('\n',2)[2].rsplit('% END A026-D01',1)[0]
G['margin']=group('A026-D01',body_diagram,groups['A026-D01']['bbox'],groups['A026-D01']['owns'],diagram_states,groups['A026-D01']['evidence'],'crop_08_margin.png',groups['A026-D01']['components'],role=groups['A026-D01']['role'])

# M02 is inside S10 at its full-scan origin, not printed beside the expression.
old_m02=G['tick']
nested_m02=group('A026-M02',r"""\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1171,1188) {$\unsure{\tikz[x=.10mm,y=-.10mm,baseline=(tickbase)]{\path[use as bounding box] (0,0) rectangle (13,10);\coordinate (tickbase) at (0,10);\draw[line width=.28pt] (4,4) -- (8,6);}}$};""",[1171,1178,1184,1188],'one short upper tick only; no Sigma word/sign owned',groups['A026-M02']['complete_candidates'],groups['A026-M02']['evidence'],'crop_10_closure_equation.png',hand='undetermined hand',role='base-west anchor at full (1171,1188), inner baseline y=10 gives origin (1171,1178); x/y units .10mm')
S[10]=S[10].replace('\\end{scope}',nested_m02+'\\end{scope}',1)
groups['A026-S10']['tex']=S[10]
G['Edis1']=graphic('A026-E02',[1315,1905,1385,1975],['\\draw[line width=.27pt] (1331,1930) -- (1323,1961) -- (1351,1960);','\\draw[line width=.24pt] (1328,1947) -- (1356,1941);','\\draw[line width=.22pt] (1342,1918) .. controls (1348,1910) and (1356,1915) .. (1362,1921);'],'E_1',[{'reading':'E_1 with detached arched top arm','hand':'his hand','role':'upper arc assigned to the E head'},{'reading':'E_1 with independent upper arc','hand':{'E_body_index':'his hand','upper_arc':'undetermined hand'},'role':'upper arc present; its attachment unestablished'}],'Detached curved upper run above the upright/middle/lower E body.','crop_17_disjoint.png',nodes=['\\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\\scriptsize] at (1364,1970) {$1$};'],qualify=False)
G['Edis2']=graphic('A026-E03',[1445,1894,1514,1972],['\\draw[line width=.27pt] (1455,1914) -- (1449,1955) -- (1477,1955);','\\draw[line width=.24pt] (1452,1937) -- (1479,1933);','\\draw[line width=.22pt] (1463,1911) .. controls (1471,1903) and (1481,1902) .. (1487,1910);'],'E_2',[{'reading':'E_2 with detached arched top arm','hand':'his hand','role':'upper arc assigned to the E head'},{'reading':'E_2 with independent upper arc','hand':{'E_body_index':'his hand','upper_arc':'undetermined hand'},'role':'upper arc present; its attachment unestablished'}],'Second detached curved upper run, independently inspected with its E body and index.','crop_17_disjoint.png',nodes=['\\node[anchor=base west,inner sep=0pt,outer sep=0pt,font=\\scriptsize] at (1487,1969) {$2$};'],qualify=False)

# The primary family index retains all three C font/glyph candidates.
text = r'''\scanpage{26}
Soit $X$ un ens. Une \uline{\unsure{décomposition|dècomposition|decomposition|disposition} binaire} de $X$ est un ens de deux parties de $X$ $('''+S[1]+r''')_{\alpha\in\unsure{\mathcal E|\mathscr E|\varepsilon}}$ (les ``hémisphères'') dont la réunion est $X$, et dont \deleted{l'intersection} aucune n'est contenue dans l'autre -- on désigne par $E$ (``équateur'') l'intersection (on n'exclut pas qu'elle soit vide). Quand $X$ est un espace topologique, on s'intéresse au cas où les '''+G['hemi']+' $'+S[2]+r'''$ sont fermés, ('''+G['de']+r''' le plus souvent, '''+G['insert']+r''' et où $E\ne\varnothing$); si les $'''+S[7]+r'''$ connexes et $E'''+G['ne']+r'''\varnothing$, $X$ est connexe, si '''+G['correct']+r''', on conclut '''+G['aussitot']+r''' que $'''+G['faint']+S[9]+r'''\cap '''+G['Efirst']+r'''\ne\varnothing$
'''+G['margin']+r'''
(car $'''+S[10]+r'''\cap E='''+S[11]+r'''\setminus'''+S[12]+r'''$, et $'''+S[13]+r'''$ ne peut être à la fois ouvert et fermé car $'''+S[14]+r'''$ est un ouvert $\ne\varnothing$ et $\ne X$)

Considérons deux décompositions binaires '''+G['paircorr']+r''' on dit qu'elles sont \uline{non \unsure{panachées|penchées|parallèles}}\raisebox{-2mm}{$'''+G['points']+r'''$} si '''+G['distins']+' $'+S[21]+r'''$ dans l'une, $'''+S[22]+r'''$ dans l'autre, tels que
\[
'''+S[23]+G['cap']+S[24]+r'''=\varnothing\qquad(\text{\unsure{d'où|d'ou} }'''+G['Edis1']+r'''\cap '''+G['Edis2']+r'''=\varnothing)
\]
on $'''+G['reduceda']+r'''$ alors
\[
\begin{aligned}
'''+S[25]+r'''&'''+G['incl']+S[26]+r'''\quad'''+G['cancelnonempty']+r'''\quad\text{i.e.}\quad'''+S[27]+r'''\cap'''+S[28]+'='+S[29]+r'''\\
'''+S[30]+r'''&\subset'''+S[31]+r'''\qquad\qquad\text{\unsure{i.e.|i.e|ie}}\quad'''+S[32]+r'''\cap'''+S[33]+'='+S[34]+r'''\\
'''+S[35]+r'''&'''+G['def']+S[36]+G['bottomtrace']+r'''\cap'''+S[37]+r'''\supset E_1\cup E_2,\quad'''+S[38]+r'''\cap'''+S[39]+r'''\ne\varnothing
\end{aligned}
\]
% archive sheet number: 25
'''
# Retain literal newlines after every comment before adjoining text.
(P/'reading.tex').write_text(text)
(P/'groups_work.json').write_text(json.dumps(groups,ensure_ascii=False,indent=2)+'\n')
print('Wrote reading.tex; groups',len(groups),'bytes',len(text.encode()))
