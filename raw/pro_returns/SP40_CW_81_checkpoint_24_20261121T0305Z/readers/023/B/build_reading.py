from pathlib import Path
import json,re
D=Path('/workspace/scratch/94548b74fbe0/out/readers/023/B')
meta={}
def graphic(ident,bbox,baseline,body,reading,qualifiers=None,unit='.20pt',outer=None,qualified=False,annotation=None,owned=None):
    x0,y0,x1,y1=bbox
    name=ident.replace('-','')+'base'
    ann=annotation or reading
    meta[ident]={'id':ident,'observed_locus_bbox':list(bbox),'drawing_rectangle_local':[0,0,x1-x0,y1-y0], 'source_coordinate_convention':'Full-scan top-left pixel coordinates in literal paths; translation by negative declared origin. These are manual approximations, not measured curve extrema.','declared_origin_full_scan':[x0,y0],'declared_baseline_full_scan_y':baseline,'x_unit':unit,'y_unit':'-'+unit,'anchor':'base west, inner sep=0pt, outer sep=0pt for nested placement','container':outer,'owned_words_and_labels':owned or [reading],'complete_reading':reading,'qualifiers':qualifiers or [],'invisible_annotation':ann,'manual_approximation':True}
    s='% BEGIN '+ident+'\n'
    s+='% Complete reading: '+reading+'\n'
    for q in qualifiers or []: s+='% Qualification: '+q+'\n'
    if qualified:s+='\\unsure{%\n'
    s+='\\begin{tikzpicture}[x='+unit+',y=-'+unit+',baseline=('+name+'),line cap=round,line join=round]\n'
    s+='\\path[use as bounding box] (0,0) rectangle ('+str(x1-x0)+','+str(y1-y0)+');\n'
    s+='\\coordinate ('+name+') at (0,'+str(baseline-y0)+');\n'
    s+='\\begin{scope}[shift={(-'+str(x0)+',-'+str(y0)+')}]\n'
    s+='\\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt,opacity=0] at ('+str(x0)+','+str(baseline)+') {'+ann+'};\n'
    s+=body.strip()+'\n\\end{scope}\n\\end{tikzpicture}'
    if qualified:s+='}'
    s+='\n% END '+ident+'\n'
    return s

a1=graphic('B023-G01',(260,225,285,246),242,r'''
% PATH B023-G01.p1: the small solid opening a/point-shaped form, once.
\fill (264,236) -- (267,234) -- (275,232) -- (278,235) -- (276,240) -- (266,240) -- cycle;
''',r"a | point-shaped mark after l'on",['a is primary; character versus point-shaped mark remains unresolved.'],unit='.25pt',qualified=True,annotation=r'\phantom{a|$\cdot$}',owned=["the a/point-shaped form after l'on; no neighbouring words"])
u1=graphic('B023-G02',(690,405,802,539),479,r'''
% PATH B023-G02.p1: outer cup, with its returning bottom.
\draw[line width=.55pt] (725,420) .. controls (724,442) and (725,465) .. (733,470) .. controls (746,480) and (756,466) .. (762,418);
% PATH B023-G02.p2: descending inner oblique and short rising return.
\draw[line width=.42pt] (717,427) .. controls (728,441) and (731,459) .. (739,468) .. controls (742,472) and (747,466) .. (749,461);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (693,528) {$\scriptstyle\alpha\in K$};
''',r'\deleted{\bigvee}\bigcup_{\alpha\in K} | \bigcup_{\alpha\in K}', ['The cup is definite; the oblique may be an earlier vee or a retrace. Cancellation/predecessor status stays unresolved.'],qualified=True,annotation=r'$\phantom{\unsure{\deleted{\bigvee}\bigcup|\bigcup}_{\alpha\in K}}$',owned=['cup, oblique, full alpha-in-K limit'])
s1=graphic('B023-S01',(805,386,907,478),463,r'''
% PATH B023-S01.p1: joined Sigma head and angular body, including the lower foot.
\draw[line width=.48pt] (813,416) .. controls (822,412) and (839,413) .. (849,415);
\draw[line width=.42pt] (817,416) .. controls (832,422) and (842,430) .. (845,439) .. controls (845,446) and (830,454) .. (820,459) -- (862,457);
% PATH B023-S01.p2: surviving upright within the Sigma; predecessor/retrace status is qualified.
\draw[line width=.55pt] (836,422) .. controls (838,435) and (838,451) .. (839,459);
% PATH B023-S01.p3: separate roof.
\draw[line width=.55pt] (845,403) .. controls (856,401) and (867,395) .. (872,391) .. controls (878,397) and (884,402) .. (889,404);
% PATH B023-S01.p4: raised plus, both arms.
\draw[line width=.55pt] (871,428) -- (889,426) (880,418) -- (881,436);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (869,469) {$\scriptstyle\alpha$};
''',r'\widehat{\deleted{I}\Sigma}_\alpha^+ | \widehat{\deleted{E}\Sigma}_\alpha^+ | \widehat{\Sigma}_\alpha^+', ['The extra upright survives. I is the strongest predecessor candidate; E and an unassigned retrace of the live Sigma remain complete state alternatives. The roof, plus and alpha are definite.'],qualified=True,annotation=r'$\phantom{\unsure{\widehat{\deleted{I}\Sigma}_\alpha^+|\widehat{\deleted{E}\Sigma}_\alpha^+|\widehat{\Sigma}_\alpha^+}}$',owned=['complete hatted Sigma, internal upright, plus and alpha'])
a2=graphic('B023-G04',(1036,553,1130,624),620,r'''
% PATH B023-G04.p1: reduced second a, the same primary as B023-G01.
\fill (1040,608) -- (1046,604) -- (1051,608) -- (1049,613) -- (1042,613) -- cycle;
% BEGIN B023-M01
% PATH B023-M01.p1: detached brown-grey oblique above the space before en.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1114,570) {\unsure{\begin{tikzpicture}[x=.20pt,y=-.20pt,baseline={(0,7)}]
\path[use as bounding box] (0,0) rectangle (12,10);
\draw[brown!65!black,line width=.55pt] (3,2) -- (8,6);
\end{tikzpicture}}};
% END B023-M01
''',r'a; detached oblique mark above-right', ['The a keeps the first-occurrence qualification at B023-G01. Its local point-shaped alternative remains in the report. The separate brown-grey oblique has unresolved role, hand and surface origin.'],annotation=r'\phantom{a}',owned=['second reduced a','detached brown-grey oblique M01; on and en remain outside'])
meta['B023-M01']={'id':'B023-M01','observed_locus_bbox':[1115,559,1125,568],'drawing_rectangle_local':[0,0,12,10],'declared_origin_full_scan':[1114,563],'declared_baseline_full_scan_y':570,'x_unit':'.20pt','y_unit':'-.20pt','anchor':'base west, inner sep=0pt, outer sep=0pt','container':'B023-G04','owned_words_and_labels':[],'complete_reading':'short brown-grey oblique; no supplied character','qualifiers':['role, hand, attachment and surface origin unresolved'],'manual_approximation':True}
e2=graphic('B023-G05',(639,689,749,796),749,r'''
% PATH B023-G05.p1: displayed E with curved left body and middle arm.
\draw[line width=.52pt] (647,704) -- (684,698) (649,704) .. controls (667,714) and (652,736) .. (650,744) -- (681,741) (660,725) -- (686,724);
% PATH B023-G05.p2: lower-foot retrace and small closed return.
\draw[line width=.5pt] (653,741) .. controls (663,747) and (682,736) .. (688,742) -- (686,749) .. controls (675,751) and (664,749) .. (663,746);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (696,777) {$\beta$};
''',r'E_\beta with a retraced lower foot', ['The extra lower return is preserved as a stroke; no different algebraic letter is inferred.'],annotation=r'$\phantom{E_\beta}$',owned=['displayed E and beta; inclusion lies outside'])
rel=graphic('B023-G06',(374,1420,415,1474),1458,r'''
% PATH B023-G06.p1: first horizontal.
\draw[line width=.40pt] (380,1437) -- (403,1433);
% PATH B023-G06.p2: second horizontal.
\draw[line width=.4pt] (378,1448) -- (407,1443);
% PATH B023-G06.p3: thick bent crossing and lower hook.
\draw[line width=.65pt] (392,1427) .. controls (398,1436) and (402,1459) .. (390,1464);
''',r'\ne | \deleted{\ne}{,}', ['The two bars are visible. The heavy bent crossing may be the live not-equal sign or a cancelled not-equal with a comma; the whole-state qualification remains.'],qualified=True,annotation=r'$\phantom{\unsure{\ne|\deleted{\ne}{,}}}$',owned=['first relation only; adjoining alpha and beta stay outside'])
s5=graphic('B023-S05',(997,1381,1092,1451),1439,r'''
% PATH B023-S05.p1: separate upper return, with pale left entrance.
\draw[black!65,line width=.35pt] (1003,1396) .. controls (1016,1392) and (1058,1387) .. (1055,1394) -- (1033,1401);
% PATH B023-S05.p2: Sigma body and its foot continuing into the alpha index.
\draw[line width=.47pt] (1009,1403) .. controls (1050,1403) and (1050,1406) .. (1043,1415) -- (1011,1430) .. controls (1036,1428) and (1051,1429) .. (1060,1424) .. controls (1067,1420) and (1061,1442) .. (1052,1443) .. controls (1040,1446) and (1042,1438) .. (1069,1434);
% PATH B023-S05.p3: complete raised plus.
\draw[line width=.4pt] (1071,1398) -- (1087,1396) (1080,1393) -- (1082,1404);
''',r'\Sigma_\alpha^+; separate short head/return', ['First printed recurring qualification: separate head/return of Sigma versus independent upper run. The body and alpha share the drawn foot; alpha is not repeated as a node.'],qualified=True,annotation=r'$\phantom{\Sigma_\alpha^+}$',owned=['Sigma body, separate head, connected alpha and plus'])
s6=graphic('B023-S06',(1137,1381,1235,1485),1440,r'''
% PATH B023-S06.p1: folded head and body, joined through the left return; foot flows into beta.
\draw[line width=.47pt] (1144,1396) .. controls (1160,1392) and (1188,1389) .. (1189,1394) .. controls (1176,1398) and (1152,1399) .. (1145,1403) .. controls (1158,1406) and (1181,1405) .. (1178,1414) -- (1149,1430) .. controls (1162,1425) and (1176,1422) .. (1183,1426) .. controls (1191,1438) and (1186,1468) .. (1187,1480) .. controls (1186,1451) and (1203,1435) .. (1211,1449) .. controls (1223,1471) and (1204,1470) .. (1200,1461);
% PATH B023-S06.p2: raised T-shaped plus/top candidate, with no supplied upper arm.
\draw[line width=.42pt] (1209,1396) -- (1228,1393) (1217,1394) -- (1218,1406);
''',r'\Sigma_\beta^+ | \Sigma_\beta^\top', ['The folded head visibly returns to the body; its local connection is recorded separately from S05. Beta continues from the foot. The raised sign has a horizontal and descending stem; plus is primary, top-shaped alternative retained.'],qualified=True,annotation=r'$\phantom{\unsure{\Sigma_\beta^+|\Sigma_\beta^\top}}$',owned=['Sigma, folded head, connected beta, full raised sign'])
s7=graphic('B023-S07',(1300,1482,1404,1557),1535,r'''
% PATH B023-S07.p1: detached short head.
\draw[line width=.5pt] (1312,1499) -- (1344,1496);
% PATH B023-S07.p2: Sigma body below the visible gap.
\draw[line width=.5pt] (1310,1504) -- (1336,1512) -- (1309,1531) -- (1352,1530);
% PATH B023-S07.p3: plus.
\draw[line width=.5pt] (1371,1494) -- (1393,1493) (1381,1485) -- (1381,1505);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1363,1550) {$\scriptstyle\alpha$};
''',r'\Sigma_\alpha^+ with detached head', ['Local gap between head and body remains. Recurring head/independent-run qualification is printed first at S05; no roof is supplied here.'],annotation=r'$\phantom{\Sigma_\alpha^+}$',owned=['complete Sigma, alpha and plus'])
s8=graphic('B023-S08',(1208,1589,1311,1646),1633,r'''
% PATH B023-S08.p1: detached short head.
\draw[line width=.5pt] (1222,1595) -- (1250,1593);
% PATH B023-S08.p2: body below its gap.
\draw[line width=.5pt] (1216,1600) .. controls (1250,1607) and (1253,1608) .. (1243,1618) -- (1215,1629) -- (1258,1628);
% PATH B023-S08.p3: plus with short upper segment.
\draw[line width=.5pt] (1279,1597) -- (1298,1596) (1287,1592) -- (1289,1611);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1258,1642) {$\scriptstyle\alpha$};
''',r'\Sigma_\alpha^+ with detached head', ['The later head/body gap is inspected locally; the first-occurrence role qualifier remains at S05.'],annotation=r'$\phantom{\Sigma_\alpha^+}$',owned=['complete Sigma, alpha and plus; final period outside'])
corr=graphic('B023-G07',(307,1588,926,1700),1680,r'''
% WORDS B023-G07.w1: old clause; invisible deletion copy supplies state without another visible rule.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (334,1675) {\rlap{$E_i$ est \unsure{contenu|contenue}}\phantom{\deleted{$E_i$ est \unsure{contenu|contenue}}}};
% WORDS B023-G07.w2: raised insertion; the annotation retains the complete insertion scope.
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (441,1621) {\rlap{$\exists\alpha\in K$ tel que}\phantom{\inserted{$\exists\alpha\in K$ tel que}}};
% PATH B023-G07.p1: one sloping cancellation rule, including its pale left entrance.
\draw[black!65,line width=.35pt] (334,1677) -- (442,1660);
\draw[line width=.45pt] (442,1660) .. controls (609,1653) and (756,1637) .. (891,1629);
''',r'\deleted{E_i est contenu|E_i est contenue}; \inserted{\exists\alpha\in K tel que}', ['Complete cancelled clause is E_i est contenu / E_i est contenue. No dans un is supplied. Inserted existential has no comma after K.'],unit='.18pt',annotation=r'\phantom{\deleted{$E_i$ est \unsure{contenu|contenue}}\inserted{$\exists\alpha\in K$ tel que}}',owned=['all cancelled E_i est contenu/contenue','all raised existential insertion','one cancellation rule; following live E_i inclusion stays outside'])
m2=graphic('B023-M02',(166,1373,183,1391),1388,r'''
% PATH B023-M02.p1: isolated left-margin point.
\fill (173.5,1381.0) circle (1.35);
''','isolated black point', ['Role, hand, attachment and surface origin unresolved.'],unit='.35pt',qualified=True,annotation=r'\phantom{$\cdot$}',owned=[])
m3=graphic('B023-M03',(1599,1734,1616,1753),1750,r'''
% PATH B023-M03.p1: upper of two distinct far-right points.
\fill (1609,1740) ellipse (1.15 and 1.25);
% PATH B023-M03.p2: lower-left point.
\fill (1605,1746) ellipse (1.15 and .8);
''','two detached oblique points after the unfinished line', ['Role, hand, attachment and surface origin unresolved; neither point is supplied as manuscript punctuation.'],unit='.30pt',qualified=True,annotation=r'\phantom{$\cdot\,\cdot$}',owned=[])
m4=graphic('B023-M04',(259,1839,277,1856),1854,r'''
% PATH B023-M04.p1: small pale oblique before Corollaire.
\fill[black!45] (265,1849) .. controls (265,1847) and (268,1843) .. (269,1844) .. controls (272,1846) and (269,1849) .. (267,1851) -- cycle;
''','small grey oblique before Corollaire', ['Role, hand, attachment and surface origin unresolved; no character supplied.'],unit='.30pt',qualified=True,annotation=r'\phantom{$\cdot$}',owned=[])
fam=graphic('B023-G08',(1327,1789,1590,1880),1858,r'''
% PATH B023-G08.p1: opening parenthesis.
\draw[line width=.38pt] (1358,1794) .. controls (1332,1808) and (1327,1843) .. (1352,1850);
% PATH B023-G08.p2: detached Sigma head.
\draw[line width=.5pt] (1359,1813) -- (1399,1812);
% PATH B023-G08.p3: body and curved low i-stroke sharing the foot.
\draw[line width=.48pt] (1362,1818) .. controls (1390,1823) and (1393,1826) .. (1386,1836) -- (1368,1847) .. controls (1397,1840) and (1406,1846) .. (1406,1850);
% PATH B023-G08.p4: one i-dot, not repeated in a separate i node.
\fill (1403,1833) ellipse (1.4 and 1.6);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1407,1818) {$\scriptstyle\alpha$};
% PATH B023-G08.p5: closing parenthesis merging into the low family alpha.
\draw[line width=.45pt] (1447,1806) .. controls (1451,1827) and (1450,1842) .. (1446,1848) .. controls (1457,1839) and (1466,1847) .. (1459,1854) .. controls (1450,1859) and (1441,1852) .. (1451,1849) -- (1467,1856);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1475,1857) {$\scriptstyle\in$};
% PATH B023-G08.p6: K/I compound, complete left stem and diagonal legs.
\draw[line width=.45pt] (1504,1826) -- (1506,1854) (1506,1837) -- (1527,1827) (1507,1837) -- (1527,1852);
% PATH B023-G08.p7: additional right loop/upright in that same K/I cluster.
\draw[line width=.45pt] (1518,1830) .. controls (1526,1825) and (1525,1842) .. (1521,1844) -- (1514,1836) (1522,1841) -- (1522,1860);
% PATH B023-G08.p8: terminal comma owned by the family group.
\draw[line width=.48pt] (1577,1855) .. controls (1581,1866) and (1576,1874) .. (1570,1876);
''',r'(\Sigma_i^\alpha)_{\alpha\in K}, | (\Sigma_i^\alpha)_{\alpha\in\deleted{I}K}, | (\Sigma_i^\alpha)_{\alpha\in I},', ['The detached Sigma head keeps its own local role qualification. The i-dot occurs once above the hook sharing the Sigma foot. K/I and a deleted-I/live-K state remain unresolved in the final family index. Closing parenthesis and low alpha share their visible lower junction.'],qualified=True,annotation=r'$\phantom{(\Sigma_i^\alpha)_{\alpha\in\unsure{K|\deleted{I}K|I}},}$',owned=['complete parenthesized family','i and its dot','upper alpha','lower alpha-in-K/I cluster','comma'])
pi=graphic('B023-P01',(682,1968,806,2042),2037,r'''
% PATH B023-P01.p1: Pi head.
\draw[line width=.5pt] (690,1979) -- (748,1978);
% PATH B023-P01.p2: left Pi stem with small return.
\draw[line width=.4pt] (714,1977) .. controls (713,1994) and (720,2006) .. (718,2012) -- (714,2010);
% PATH B023-P01.p3: detached right Pi stem.
\draw[line width=.48pt] (727,1989) -- (736,2022);
% PATH B023-P01.p4: complete upper ring, including the small entry.
\draw[line width=.48pt] (776,1978) .. controls (778,1984) and (785,1986) .. (786,1979) .. controls (785,1971) and (778,1972) .. (777,1979);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (756,2037) {$K$};
''',r'\Pi_K^\circ | \Pi_K^0', ['The round raised form retains circle/zero alternatives. The Pi right stem is visibly separate from the head; the full shape is retained.'],unit='.25pt',outer='B023-G11',qualified=True,annotation=r'$\phantom{\Pi_K^{\unsure{\circ|0}}}$',owned=['complete Pi, low K and raised ring'])
s10=graphic('B023-S10',(1340,1910,1454,1978),1973,r'''
% PATH B023-S10.p1: joined Sigma head/body.
\draw[line width=.5pt] (1360,1922) -- (1406,1921) (1361,1923) .. controls (1390,1931) and (1395,1932) .. (1374,1946) -- (1348,1962) -- (1411,1961);
% PATH B023-S10.p2: plus stem and main crossbar.
\draw[line width=.5pt] (1434,1912) -- (1438,1939) (1426,1924) -- (1448,1922);
% PATH B023-S10.p3: short upper-left retrace on the plus.
\draw[line width=.45pt] (1429,1918) -- (1436,1918);
% PATH B023-S10.p4: detached point above-right of the plus.
\fill (1440,1914) circle (1.2);
% PATH B023-S10.p5: complete retraced alpha/index loop, including the shared upright.
\draw[line width=.48pt] (1425,1959) .. controls (1415,1949) and (1414,1972) .. (1424,1968) .. controls (1433,1963) and (1434,1955) .. (1434,1948) .. controls (1435,1960) and (1425,1973) .. (1420,1968) .. controls (1418,1958) and (1429,1960) .. (1438,1968);
% PATH B023-S10.p6: one point over the index, with unresolved i/remnant/independent role.
\fill (1426,1949) ellipse (1.1 and 1.5);
''',r'\Sigma_\alpha^+ with two small points | \Sigma_{\deleted{i}\alpha}^+ with the upper point retained', ['The head is joined to the body here. The lower point may be a predecessor-i dot or a separate trace; index cancellation/state stays qualified. The distinct point above the plus and its short retrace are retained without an assigned operation.'],unit='.25pt',outer='B023-G11',qualified=True,annotation=r'$\phantom{\unsure{\Sigma_\alpha^+|\Sigma_{\deleted{i}\alpha}^+}}$',owned=['complete Sigma, plus with short extra arm, upper point, retraced alpha and lower point'])
shared=r'''
% BEGIN B023-G09
% Complete reading: formée; cup with high cross-stroke and alpha-in-K limit; hatted Sigma_alpha-plus; terminal period.
% The f descender and cup right stem occupy one continuous path. No second printed f or second cup right stem is supplied.
\node[overlay,anchor=base west,inner sep=0pt,outer sep=0pt,opacity=0] at (945,2090) {\phantom{formée $\bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+.$}};
% PATH B023-G09.p1: f entrance/upright continuing into the cup right side and bottom; owns the shared vertical once.
\draw[line width=.5pt] (978,1949) .. controls (985,1964) and (981,1984) .. (984,1993) .. controls (984,2016) and (985,2035) .. (986,2056) .. controls (986,2077) and (972,2092) .. (956,2092) .. controls (941,2091) and (938,2073) .. (936,2041);
% PATH B023-G09.p2: f loop and continuation into the early word strokes.
\draw[line width=.48pt] (984,1989) .. controls (972,1992) and (945,1993) .. (943,1998) .. controls (951,2015) and (973,2028) .. (984,2030) (984,1989) .. controls (991,1977) and (992,1984) .. (996,1986) .. controls (1002,1977) and (1012,1977) .. (1018,1985);
% PATH B023-G09.p3: remaining low word run, with final separate e.
\draw[line width=.5pt] (1030,1980) .. controls (1038,1990) and (1045,1984) .. (1048,1977) .. controls (1056,1984) and (1063,1984) .. (1070,1976) .. controls (1079,1982) and (1093,1976) .. (1098,1979);
\draw[line width=.45pt] (1118,1974) .. controls (1123,1978) and (1129,1977) .. (1134,1975);
% PATH B023-G09.p4: acute mark over the word formée.
\draw[line width=.5pt] (1097,1971) -- (1098,1967) -- (1101,1967);
% PATH B023-G09.p5: independent high horizontal crossing the cup left stem, stopping before the shared right stem.
\draw[line width=.55pt] (934,2054) -- (980,2053);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (944,2121) {$\scriptstyle\alpha\in K$};
% BEGIN B023-S11
% Complete reading: hatted Sigma_alpha-plus; detached short head below a separate roof. Its head role keeps the first-occurrence qualification at S05.
% PATH B023-S11.p1: definite separate roof.
\draw[line width=.5pt] (1049,2028) -- (1079,2008) -- (1105,2028);
% PATH B023-S11.p2: detached head.
\draw[line width=.46pt] (1046,2041) -- (1082,2037);
% PATH B023-S11.p3: Sigma body under the gap.
\draw[line width=.48pt] (1045,2048) .. controls (1061,2053) and (1084,2054) .. (1077,2062) -- (1046,2077) -- (1084,2077);
% PATH B023-S11.p4: complete raised plus.
\draw[line width=.48pt] (1099,2046) -- (1117,2042) (1108,2039) -- (1110,2061);
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1090,2087) {$\scriptstyle\alpha$};
% END B023-S11
% PATH B023-G09.p6: terminal statement point, owned here once.
\fill (1186,2081) ellipse (1.8 and 1.7);
% END B023-G09
'''
meta['B023-G09']={'id':'B023-G09','observed_locus_bbox':[934,1945,1193,2125],'declared_origin_full_scan':[244,1888],'declared_baseline_full_scan_y':2090,'drawing_rectangle_local':[0,0,1402,264],'x_unit':'.25pt','y_unit':'-.25pt','container':'B023-G11','anchor':'inherited full-scan scope; no nested-font offset','owned_words_and_labels':['formée','final cup and high crossing stroke','alpha-in-K limit','complete S11','terminal period'],'complete_reading':r'formée; \bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+.','qualifiers':['Cup cross-stroke presence is resolved; its mathematical role remains unassigned. Shared f/cup vertical occurs once. S11 head-role qualification remains local and is printed first at S05.'],'manual_approximation':True}
meta['B023-S11']={'id':'B023-S11','observed_locus_bbox':[1040,2004,1124,2090],'declared_origin_full_scan':[244,1888],'declared_baseline_full_scan_y':2077,'drawing_rectangle_local':[0,0,1402,264],'x_unit':'.25pt','y_unit':'-.25pt','container':'B023-G09 within B023-G11','owned_words_and_labels':['Sigma, separate roof, detached short head, raised plus, low alpha'],'complete_reading':r'\widehat{\Sigma}_\alpha^+','qualifiers':['Local separated head/body gap below a definitely separate roof; head/independent-run role retained.'],'manual_approximation':True}
rule=r'''
% BEGIN B023-G10
% Complete reading: left vertical emphasis rule beside both lines of the corollary; six separately drawn runs retain the pale interruptions.
% PATH B023-G10.p1: top pale run.
\draw[black!55,line width=.3pt] (272,1939) .. controls (270,1950) and (269,1958) .. (269,1961);
% PATH B023-G10.p2: second run.
\draw[black!70,line width=.30pt] (269,1963) .. controls (268,1971) and (270,1979) .. (270,1985);
% PATH B023-G10.p3: third interrupted run.
\draw[black!65,line width=.3pt] (270,1988) .. controls (272,1997) and (270,2005) .. (272,2009);
% PATH B023-G10.p4: short fourth run.
\draw[black!65,line width=.3pt] (272,2012) -- (273,2020);
% PATH B023-G10.p5: fifth run and separate low bead.
\draw[black!65,line width=.3pt] (273,2024) -- (274,2034);
\fill[black!60] (274,2038) circle (.8);
% PATH B023-G10.p6: long lower run, slight rightward bend, and dark terminal.
\draw[black!75,line width=.35pt] (274,2042) .. controls (277,2071) and (279,2110) .. (287,2135);
% END B023-G10
'''
meta['B023-G10']={'id':'B023-G10','observed_locus_bbox':[265,1937,291,2139],'declared_origin_full_scan':[244,1888],'declared_baseline_full_scan_y':2135,'drawing_rectangle_local':[0,0,1402,264],'x_unit':'.25pt','y_unit':'-.25pt','container':'B023-G11','owned_words_and_labels':[],'complete_reading':'interrupted left vertical emphasis rule, six runs plus one bead','qualifiers':['Manual approximation of pale interruptions; no enclosing box or horizontal lower rule supplied.'],'manual_approximation':True}
outerbody=rule+r'''
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (309,2030) {la};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (413,2022) {partition};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (682,2037) {$%
'''+pi+r'''$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (839,2001) {est};
'''+shared+r'''
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1191,1975) {des};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1340,1973) {$%
'''+s10+r'''$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (1472,1969) {$(\alpha\in K)$};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (325,2133) {et};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (443,2128) {de};
\node[anchor=base west,inner sep=0pt,outer sep=0pt] at (691,2110) {$V=X\setminus$};
'''
cor=graphic('B023-G11',(244,1888,1646,2152),2140,outerbody,r'la partition \Pi_K^\circ est formée des \Sigma_\alpha^+ (\alpha\in K) et de V=X\setminus\bigcup_{\alpha\in K}\widehat{\Sigma}_\alpha^+.', ['Pi retains circle/zero; S10 retains its full index-state/point qualification; final cup crossing is visible with unassigned operation; full word formée and cup share the one declared vertical.'],unit='.25pt',annotation=r'\phantom{la partition}',owned=['entire two-line corollary statement','left emphasis rule','all nested groups and adjoining words; Corollaire heading remains outside'])
tex=r'''\scanpage{23}
Soit maintenant $\beta\in I\setminus K$, \unsure{prouvons} que l'on
'''+a1+r'''$\overline V\cap E_\beta=\varnothing$. En effet, $V$ ne \deleted{contient} \inserted{rencontre} aucun $E_i$ $(i\in I)$ donc $E_\beta\subset X\setminus V=
'''+u1+s1+r'''$, \deleted{\unsure{donc si}} je dis que si $\beta\in I\setminus K$, on
'''+a2+r'''en fait
\[
'''+e2+r'''\subset\bigcup\Sigma_\alpha^+\qquad\text{(ouvert disjoint de }V\text{)}
\]
% slanted
\reversemarginpar\margin{\begin{tikzpicture}\node[rotate=24,anchor=base west,inner sep=0pt,outer sep=0pt] {\shortstack[l]{C'est trivial, \deleted{\illegible{1}}\\du fait que les $E_i$ $(i\in I)$\\sont disjoints}};\end{tikzpicture}}\normalmarginpar
\unsure{ce|} qui \unsure{prouvera|prouve} l'assertion -- mieux, je dis que $\exists\alpha\in K$ tel que $E_\beta\subset\Sigma_\alpha^+$. Cela revient au

\uline{Lemme} Soit $K\subset I$, \deleted{tel que les} \deleted{et} des $\Sigma_\alpha^+$ $(\alpha\in K)$ tels que
\reversemarginpar\margin{%
'''+m2+r'''}\normalmarginpar
\[
\alpha
'''+rel+r'''\beta\in K,\ \alpha\ne\beta\ \Rightarrow\
'''+s5+r'''\cap
'''+s6+r'''=\varnothing.
\]
Soit $i\in I\setminus K$ tel que $E_i\subset\bigcup
'''+s7+r'''$, alors
'''+corr+r'''$E_i\subset
'''+s8+r'''$.

Cela \deleted{signifie que} \unsure{precise|précise|provient|precise le|précise le} du
\margin{%
'''+m3+r'''}
\reversemarginpar\margin{%
'''+m4+r'''}\normalmarginpar

\uline{Corollaire} Avec les hyp. préc. sur $%
'''+fam+r'''$
\figure{%
'''+cor+r'''}

Immédiat par récurrence sur $\operatorname{card} K\geq 0$.
% archive sheet number: 22
'''
# Repair one deliberate source-format join: a TeX space after Rightarrow, not a stray single slash.
tex=tex.replace('\\Rightarrow\\\n','\\Rightarrow\n')
(D/'reading.tex').write_text(tex)
# Exact source spans are administrative source indexing, not image geometry calculations.
for ident,m in meta.items():
    start=tex.index('% BEGIN '+ident+'\n')
    end=tex.index('% END '+ident+'\n',start)+len('% END '+ident+'\n')
    m['source_file']='reading.tex'
    m['source_span']={'char_start_zero_based':start,'char_end_exclusive':end,'line_start_one_based':tex[:start].count('\n')+1,'line_end_one_based':tex[:end].count('\n')}
    m['complete_exact_source']=tex[start:end] if m.get('container') is None else None
    m['source_components']=[]
    for mm in re.finditer(r'% PATH ('+re.escape(ident)+r'\.[^:]+): ([^\n]+)\n',tex[start:end]):
        a=start+mm.start(); command_start=start+mm.end()
        following=tex[command_start:end]
        stop=re.search(r'(?m)^% (?:PATH |BEGIN |END |WORDS )|^\\node|^\\end\{scope\}',following)
        b=command_start+(stop.start() if stop else len(following))
        m['source_components'].append({'owner':mm.group(1),'description':mm.group(2),'complete_commands':tex[command_start:b].rstrip(),'char_start_zero_based':a,'char_end_exclusive':b,'line_start_one_based':tex[:a].count('\n')+1})
(D/'source_map.json').write_text(json.dumps({'scan':'023','reader':'B','source_indexing_only':True,'notes':['All path bodies are hand-set approximations from the single successful views. No rendering, compilation, raster comparison, curve-extrema or other optional coordinate computation was performed.','Nested exact groups are identified by complete source spans in reading.tex; their parent excerpts already contain them, so complete source is not duplicated for each child.','B023-G11 owns every word and punctuation mark in the two-line corollary statement. B023-G09 owns the full word formée, the shared f/cup stroke, final union limit, S11 and the period. B023-G04 owns only the second a and the separate M01; on and en remain outside.'], 'groups':list(meta.values())},ensure_ascii=False,indent=2)+'\n')
print('reading.tex and source_map.json written; graphic groups:',len(meta))
