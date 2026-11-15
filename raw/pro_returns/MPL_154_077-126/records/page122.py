from save_page import save
text=r'''\scanpage{122}
\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.8pt] (343,136)--(587,132)--(587,273)--(353,279)--cycle (704,119)--(978,112)--(976,267)--(710,279)--cycle;
\draw[red!65!brown,line width=2.5pt] (413,260)--(399,192)--(460,139) (404,146)--(470,193) (482,194)--(515,234)--(554,255) (541,134)--(543,197)--(467,263) (704,120)--(710,279)--(976,267)--(978,112) (757,125)--(762,199)..controls(789,202)and(818,241)..(836,273) (780,274)--(842,219)--(911,119) (863,131)--(919,193)--(919,261);
\end{tikzpicture}}
\texttt{D A T A S E T S\quad P I C T U R E S}
'''
cols=[0,15,34,43,51,65,78,84,92,101,113]
def row(fields=None):
 a=[' ']*114
 for p in cols:a[p]='*'
 if fields:
  for i,s in enumerate(fields):
   start=cols[i]+1+(cols[i+1]-cols[i]-1-len(s))//2
   a[start:start+len(s)]=s
 return ''.join(a)
headers=['DDNAME','DESTINATION','CLASS','COPIES','RECORDS-NB','BYTES-NB','FORM','FCB','UCS','SPIN HOLD']
data=['SYSOS3','CNU     M06','A','1','67','3,893','STD.','****','****','']
text+='\\begin{verbatim}\n'+'\n'.join(['*'*114,row(),row(headers),row(),'*'*114,row(),row(data),'*'*114])+'\n\\end{verbatim}\n'
text+=r'''\figure{\begin{tikzpicture}[x=.017cm,y=-.017cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.5pt] (370,409)--(605,399)--(604,567)--(355,560)--cycle (644,409)--(907,398)--(906,562)--(633,575)--cycle;
\draw[red!65!brown,line width=2.9pt] (415,411)--(551,558) (379,558)--(519,413) (468,558)--(585,418) (679,398)--(780,560) (652,571)--(876,405) (779,391)--(874,555);
\draw[gray] (372,554)--(478,717) (473,567)--(560,689) (367,683)--(541,562);
\draw[yellow!70!orange,line width=2pt,opacity=.5] (554,428)--(565,386)--(589,362)--(612,389)--(610,544) (737,456)--(779,414)--(806,494)--(869,464)--(893,522);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.022cm,y=-.022cm,line cap=round,line join=round]
\draw (2422,305)..controls(2457,265)and(2485,296)..(2454,326)..controls(2414,354)and(2384,302)..(2422,305)..controls(2462,351)and(2540,348)..(2543,384)..controls(2538,436)and(2575,482)..(2513,497)..controls(2482,506)and(2460,550)..(2446,574)..controls(2389,621)and(2422,502)..(2456,473)..controls(2495,429)and(2541,401)..(2571,385)..controls(2628,419)and(2551,466)..(2491,427)..controls(2457,404)and(2428,368)..(2422,305);
\draw[line width=1.1pt] (2535,379)..controls(2533,415)and(2536,459)..(2514,485);
\draw[yellow!70!orange,line width=2pt,opacity=.5] (2689,351)--(2658,388) (2730,430)--(2702,484);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.011cm,y=-.011cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.4pt] (652,948)..controls(645,749)and(759,632)..(941,632)..controls(1150,604)and(1194,795)..(1147,934)..controls(1124,1050)and(1053,1102)..(955,1115)..controls(775,1159)and(662,1095)..(652,948);
\draw[yellow!70!olive,line width=2.4pt] (495,947)--(769,940)..controls(859,941)and(790,835)..(888,830)--(1577,798) (420,886)--(1668,856) (1147,934)--(1366,919)..controls(1406,905)and(1411,825)..(1436,823)--(1507,820);
\draw[red!65!brown,line width=2.8pt] (652,948)..controls(749,855)and(776,742)..(865,707)..controls(931,683)and(975,659)..(981,632)--(1040,661)..controls(1139,715)and(1109,769)..(1085,811)..controls(1024,904)and(1095,1037)..(956,1115)--(858,1120)--(791,1109)..controls(761,1020)and(755,929)..(768,741) (652,948)..controls(783,1010)and(1027,994)..(1147,934)..controls(1106,824)and(1061,729)..(980,723)..controls(879,719)and(814,776)..(768,837) (791,1109)--(1047,645) (791,1109)..controls(869,1007)and(1029,809)..(1047,645) (816,1072)--(1047,645) (913,645)..controls(882,768)and(863,1048)..(956,1115) (913,645)..controls(959,719)and(937,1052)..(956,1115) (1047,645)..controls(967,794)and(972,1001)..(956,1115);
\draw[orange!75!yellow,line width=2pt,opacity=.55] (560,752)--(692,1068) (674,717)--(546,1063) (1235,755)--(1340,978) (1358,711)--(1199,1033);
\draw[gray] (496,825)--(764,816)..controls(814,811)and(826,835)..(847,863)..controls(858,890)and(862,921)..(900,931) (764,833)..controls(808,817)and(829,882)..(850,898) (978,932)--(1650,910);
\fill (847,863) circle(5);\draw[->] (1475,799)--(1581,798);\draw[->,line width=1.3pt] (1516,851)--(1643,854);
\node at (1625,792) {$D_1$};\node at (1705,861) {$D_0$};
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.5pt] (1632,688)..controls(1746,554)and(1933,541)..(2030,691)..controls(1990,828)and(1818,905)..(1696,840)..controls(1629,801)and(1624,721)..(1632,688) (1632,688)..controls(1747,735)and(1931,698)..(2030,691) (1659,658)..controls(1787,550)and(1847,737)..(1980,655) (1635,710)..controls(1802,842)and(1895,601)..(2030,691) (1655,773)..controls(1764,872)and(1902,882)..(2025,725);
\draw[red!65!brown,line width=2.5pt] (1630,687)..controls(1669,650)and(1692,591)..(1730,569)..controls(1873,531)and(2011,581)..(2030,683) (2035,702)..controls(2016,824)and(1927,861)..(1801,878)..controls(1679,882)and(1630,821)..(1630,687) (1665,644)..controls(1641,709)and(1673,804)..(1696,840) (1690,610)..controls(1665,751)and(1749,789)..(1801,791)..controls(1840,813)and(1824,852)..(1820,875) (1717,583)..controls(1715,751)and(1824,733)..(1810,877) (1780,573)--(1770,874) (1831,563)..controls(1815,690)and(1670,696)..(1696,840) (1869,563)..controls(1863,650)and(1886,733)..(1924,851) (1897,574)..controls(1830,710)and(1841,811)..(1880,869) (1938,595)--(1837,874) (1975,618)--(1956,831) (2013,654)..controls(1932,710)and(1900,786)..(1909,855);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round,line join=round]
\draw[gray!80] (2065,752)--(2560,741) (2059,803)--(2238,801)..controls(2327,799)and(2291,693)..(2418,686)--(2548,679) (2090,765)--(2552,746) (2418,686)--(2540,697);
\draw[orange!75!yellow,line width=2pt,opacity=.7] (2120,686)--(2237,872) (2246,644)--(2087,846) (2397,697)--(2480,841) (2485,650)--(2362,830);
\node at (2600,690) {$D_1$};\node at (2608,754) {$D_0$};\node at (2060,819) {$D_2$};
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.011cm,y=-.011cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.6pt] (1425,1068)..controls(1514,1069)and(1586,1042)..(1641,1087)..controls(1712,1138)and(1681,1198)..(1747,1197)--(2220,1171)..controls(2337,1168)and(2277,1085)..(2366,1066)--(2879,1038);
\draw[orange!80!brown,line width=1.8pt] (1607,1133)..controls(1958,1148)and(2227,1106)..(2808,1115) (1793,1063)--(1787,1280);
\draw[orange!75!yellow,line width=2pt,opacity=.65] (1975,1011)--(1974,1286) (2149,1055)--(2107,1272) (2122,1048)--(2140,1259) (2552,1028)--(2556,1253) (2747,989)--(2756,1244) (1838,1071)--(1958,1073)..controls(2033,1052)and(2037,1116)..(2058,1173);
\draw[gray!70] (1434,1211)..controls(1494,1226)and(1542,1242)..(1537,1339) (1334,1198)..controls(1497,1153)and(1531,1103)..(1536,1060) (1536,1060)..controls(1556,1186)and(1652,1225)..(1791,1248) (1555,1349)..controls(1628,1252)and(1714,1244)..(1788,1259) (1801,1080)..controls(1845,1111)and(1873,1161)..(1934,1178) (1820,1049)--(2151,1049)..controls(2235,1043)and(2278,1061)..(2307,1118)..controls(2348,1175)and(2483,1185)..(2556,1175) (2307,1118)..controls(2363,1069)and(2298,1045)..(2398,1040) (2556,1175)..controls(2661,1166)and(2633,1100)..(2658,1073)..controls(2686,1026)and(2736,1022)..(2808,1028) (2778,1066)--(2869,1154) (2808,1115)--(2879,1038) (2739,1043)--(2843,1173);
\draw[line width=1.3pt] (1533,951)--(1534,1034) (1542,953)--(1540,1024) (1746,1254)--(1909,1255) (1535,1360)--(1531,1477) (1545,1359)--(1534,1393);
\draw[gray!75,->,line width=1.1pt] (2440,1174)--(2587,1168);
\fill (1787,1183) circle(5) (2307,1118) circle(5) (2556,1175) circle(5) (2756,1172) circle(4);
\node at (1781,1009) {$D_0$};\node at (2568,984) {$D_1$};\node at (2737,958) {$D_2$};\node at (1768,1170) {$\unsure{s'}$};\node at (2290,1107) {$s_0$};\node at (2586,1191) {$s_1$};\node at (2770,1177) {$s_2$};\node at (1694,1128) {$\unsure{q}$};
\draw[gray!65] (836,1480)--(849,1344)..controls(953,1184)and(1148,1175)..(1299,1202)..controls(1466,1171)and(1542,1259)..(1537,1339) (849,1344)..controls(953,1223)and(1136,1164)..(1299,1202) (1530,1500)..controls(1555,1603)and(1447,1714)..(1305,1700)--(1109,1707);
\draw[black!60,line width=1.7pt] (835,1377)--(836,1480) (1160,1201)--(1300,1200) (1109,1707)--(1250,1707);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.012cm,y=-.012cm,line cap=round,line join=round]
\draw[red!65!brown,line width=3.1pt] (274,1528)..controls(300,1676)and(296,1715)..(357,1774)..controls(408,1858)and(425,1938)..(529,2040)..controls(586,2099)and(633,2125)..(710,2150) (295,1896)..controls(411,1683)and(451,1493)..(682,1312) (565,1346)..controls(736,1457)and(810,1452)..(852,1621)..controls(871,1732)and(891,1773)..(905,1801)--(964,1959) (550,2135)..controls(697,2097)and(792,2047)..(850,1936)..controls(884,1846)and(928,1723)..(1001,1645) (389,1640)..controls(492,1627)and(582,1603)..(634,1566)..controls(725,1653)and(784,1680)..(862,1694) (466,1946)..controls(571,1928)and(615,1960)..(656,1984)..controls(738,1937)and(793,1895)..(861,1919);
\draw[orange!80!brown,line width=1.8pt] (343,1525)--(365,1891) (420,1468)--(322,1898) (927,1597)--(893,1961) (1052,1568)--(895,1821);
\draw[red!65!brown,line width=1.8pt,dashed] (502,1649)--(511,1950) (532,1632)--(567,1950) (564,1619)..controls(598,1780)and(668,1822)..(747,1928) (752,1687)--(762,1904) (465,1880)..controls(586,1753)and(636,1696)..(823,1735) (599,1943)..controls(641,1833)and(690,1734)..(710,1637) (656,1984)..controls(700,1869)and(770,1749)..(883,1742);
\draw[yellow!70!olive,line width=2.7pt] (282,1762)--(491,1767) (851,1806)--(974,1802);
\draw[red!50!brown,line width=1.6pt,opacity=.6] (449,1379)--(631,1554) (634,1566)..controls(714,1528)and(788,1475)..(839,1408) (236,1939)..controls(457,1914)and(645,2015)..(742,2101) (414,2097)--(835,1974) (474,2124)--(725,1941) (417,1997)--(831,2010) (544,2075)--(703,1996);
\node at (400,1742) {$7$};\node at (944,1787) {$5$};
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.014cm,y=-.014cm,line cap=round,line join=round]
\draw[orange!80!brown,line width=1.8pt] (1323,1598)--(1293,2151) (1406,1587)--(1400,2130) (1506,1639)--(1512,2107) (1605,1627)--(1622,2130) (1099,1799)--(1825,1780) (1154,1896)--(1831,1865) (1088,1992)--(1812,1952);
\draw[red!65!brown,line width=4pt] (1323,1598)--(1306,1795)--(1099,1799) (1605,1627)--(1617,1785)--(1825,1780) (1088,1992)--(1296,1985)--(1293,2151) (1622,2130)--(1619,1957)--(1812,1952);
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=.014cm,y=-.014cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.4pt] (1668,1651)..controls(1825,1611)and(1924,1645)..(2013,1620)--(2732,1607) (1660,1701)--(1974,1671)..controls(2036,1652)and(1999,1590)..(2075,1581)--(2697,1540);
\draw[yellow!70!olive,line width=2.4pt,dashed] (2013,1620)--(2035,1667)--(2309,1666)..controls(2355,1666)and(2345,1579)..(2387,1572);
\draw[orange!80!brown,line width=2pt] (1896,1524)--(1946,1765) (1955,1503)--(1857,1790) (2223,1511)--(2301,1775) (2288,1496)--(2182,1798) (2248,1508)--(2249,1777) (2505,1500)--(2567,1738) (2569,1483)--(2458,1775);
\draw[gray!70] (1711,1578)--(1954,1574)..controls(2004,1571)and(2019,1613)..(2013,1620);\draw[gray!80] (2013,1620)..controls(2023,1587)and(2038,1590)..(2037,1584) (2013,1620)--(2035,1667);
\node at (2155,1567) {$1$};
\end{tikzpicture}}
\mspage{121}
'''
save({'scan':122,'sheet_kind':'reused_typed','text':text,'elements':[
('drawing','top left','two yellow rectangles red zigzag crossings'),('text','upper middle','DATASETS PICTURES'),('diagram','upper width','printed DDNAME DESTINATION CLASS COPIES RECORDS-NB BYTES-NB FORM FCB UCS SPIN HOLD; SYSOS3 CNU M06 A 1 67 3893 STD'),('drawing','upper left over table','two yellow quadrilaterals red crossings and pencil continuations'),('drawing','upper right','pencil double coil and yellow strokes'),('drawing','middle left','yellow oval red polygonal and curved crossings yellow transport paths D1 D0 arrows'),('drawing','middle centre right','red oval with many red vertical crossing curves and green horizontal curves'),('drawing','middle right','D1 D0 D2 grey sigmoid and horizontal orange crossings'),('drawing','lower middle right','yellow stepped curve red horizontal D0 D1 D2 verticals; s0 s1 s2 s-prime; pencil continuations'),('drawing','middle lower','large faint pencil oval with dark intervals'),('drawing','bottom left','red four-sided region and crossing curves dashed internal curves yellow intervals 7 and 5'),('drawing','bottom middle','four red vertical lines and three horizontal lines four thick corner continuations'),('drawing','bottom right','yellow sigmoid and dashed branch red two X and one triple crossing; 1'),('margin note','bottom left','121')]})
