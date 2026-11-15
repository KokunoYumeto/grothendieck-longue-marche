from save_page import save
text=r'''\scanpage{123}
\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
\draw[yellow!75!olive,line width=1.6pt] (314,721)..controls(306,531)and(392,333)..(538,255)..controls(755,119)and(959,151)..(1088,247)..controls(1276,390)and(1334,574)..(1290,739)..controls(1262,950)and(1111,1133)..(908,1160)..controls(733,1198)and(561,1133)..(415,1046)..controls(329,995)and(317,849)..(314,721);
\draw[orange!85!brown,line width=2.1pt] (750,190)..controls(694,279)and(646,454)..(722,506)..controls(801,566)and(919,510)..(861,466)..controls(793,414)and(727,475)..(693,569)..controls(650,667)and(470,767)..(464,635)..controls(457,462)and(739,532)..(801,689)..controls(831,766)and(826,853)..(869,866)..controls(950,896)and(1165,805)..(1094,687)..controls(1012,543)and(857,595)..(801,689)..controls(750,756)and(675,889)..(730,956)..controls(776,1022)and(994,960)..(1090,857)..controls(1245,697)and(1231,525)..(1142,512)..controls(986,485)and(969,691)..(960,944)..controls(951,1085)and(838,1117)..(818,1159);
\fill[black!75!brown] (314,721) circle(8) (1290,739) circle(8);
\node at (1201,933) {\uline{\unsure{Non|$N_m$}}};
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.014cm,y=-.014cm,line cap=round,line join=round]
\draw[red!60!brown,line width=1.2pt,opacity=.6] (1630,99)--(1628,236);
\draw[gray!70] (1518,646)..controls(1543,533)and(1615,478)..(1726,472)..controls(1852,471)and(1904,549)..(1871,664)..controls(1845,764)and(1770,841)..(1664,824)..controls(1547,811)and(1514,749)..(1518,646) (1518,646)..controls(1496,751)and(1554,808)..(1664,824) (1731,472)..controls(1681,583)and(1672,746)..(1685,843) (1726,472)..controls(1660,639)and(1613,950)..(1620,1141)--(1628,1207);
\draw[gray!60] (1726,472)..controls(1686,541)and(1688,583)..(1731,609)..controls(1788,632)and(1780,572)..(1745,584)..controls(1696,605)and(1685,648)..(1684,685) (1561,551)..controls(1751,489)and(2018,384)..(2150,429)..controls(2286,464)and(2317,652)..(2329,823);
\fill[gray!80] (1518,646) circle(4);\draw[gray!80] (1871,664) circle(4);
\draw[gray!60] (2071,465)..controls(2134,383)and(2183,219)..(2245,213)..controls(2349,221)and(2420,223)..(2513,216) (2442,153)..controls(2427,290)and(2464,387)..(2505,492)..controls(2513,530)and(2502,563)..(2503,605) (2248,493)--(2667,293) (2019,586)--(2196,740) (2237,617)--(2539,784) (2078,839)--(2217,684) (2202,738)--(2485,612) (2091,835)--(2219,1011);
\draw[gray!80,line width=1pt] (2181,966)--(2536,893);\draw[gray!75] (2235,618)..controls(2355,648)and(2318,1012)..(2304,1064)--(2254,1075) (2456,705)--(2542,1006) (2439,770)--(2524,934) (2196,1023)--(2537,813);
\draw[->,line width=1.4pt] (2115,866)--(2189,973);\draw[line width=2pt] (2181,966)--(2208,1011);
\draw[gray!80] (2330,940) circle(5);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round,line join=round]
\draw[gray!70] (1821,1131)--(1884,921)..controls(1888,1027)and(1932,990)..(1960,995)..controls(2065,1021)and(1923,1090)..(1896,1122)--cycle (1931,1116)--(1962,1007)..controls(1982,927)and(1999,902)..(2017,889);
\draw[gray!60] (1510,1146)--(2113,1096);\fill[gray!80] (1510,1146) circle(4);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
\draw[gray!65] (684,1337)..controls(868,1499)and(1189,1522)..(1459,1447)--(1717,1403) (1037,1470)--(1183,1185)--(1292,1469) (1045,1467)..controls(1095,1343)and(1140,1279)..(1183,1185) (1199,1479)--(1280,1375) (1207,1479)--(1285,1381) (1269,1406)..controls(1161,1366)and(1226,1180)..(1284,1141) (1270,1196)--(1510,1146) (1391,1339)--(1581,1422) (1421,1309)--(1517,1448) (1459,1450)--(1579,1308) (1372,1446)--(1587,1305) (1468,1351)--(1528,1276);
\fill (1183,1185) circle(8) (1483,1377) circle(6);
\draw[->,line width=1.8pt] (1198,1200)--(1266,1367);\draw[->,line width=1.6pt] (1272,1362)--(1292,1418);\draw[->] (1285,1417)--(1306,1475);\draw[->,line width=1.2pt] (1483,1377)--(1436,1445);\draw[->] (1483,1377)--(1517,1448);\draw[->] (1483,1377)--(1577,1424);\draw[gray,->] (1483,1377)--(1372,1446);
\draw[gray!65] (1670,1380)--(1767,1182) (1740,1183)--(1815,1378) (1757,1270)..controls(1757,1343)and(1786,1353)..(1866,1364) (1606,1389)--(1860,1376) (1767,1251)--(1823,1189);
\draw[gray!65] (2024,1484)--(2516,1107) (2147,1353)--(2543,1176) (2161,1362)--(2546,1186) (2256,1293)--(2554,1243) (1987,1343)--(2256,1293) (2413,1098)--(2462,1166) (2471,1077)--(2509,1190) (2463,1100)--(2490,1206);
\fill[gray!80] (2256,1293) circle(3);\fill[black!65!brown] (1987,1343) circle(4);
\end{tikzpicture}}
\mspage{122}
'''
save({'scan':123,'sheet_kind':'text','text':text,'elements':[
('drawing','upper left','yellow circle two boundary points single red immersed looping curve; underlined Non'),('drawing','top centre','isolated red vertical stroke'),('drawing','upper centre right','pencil circle chord curl boundary points and long descending curve'),('drawing','upper right','pencil bent curves and crossings; arrow onto oblique interval'),('drawing','middle centre','pencil cusp closed loop and crossing curve'),('drawing','lower middle','pencil broken arch and fan with black points downward arrows'),('drawing','lower middle right','pencil crossing with curved branch'),('drawing','lower right','pencil fan from black point crossing strokes; isolated point and connecting line'),('margin note','bottom left','122')]})
