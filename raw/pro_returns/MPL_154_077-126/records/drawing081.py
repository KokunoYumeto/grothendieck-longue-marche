from save_page import save
# Coordinates are manually read from the displayed scans; no image analysis/OCR.
lines=[r'\scanpage{81}',r'\figure{\begin{tikzpicture}[x=.0045cm,y=-.0045cm,line cap=round,line join=round]']
def draw(style,path): lines.append('\\draw['+style+'] '+path+';')
def ink(path,style=''):
    draw('orange!75!yellow,line width=1.6pt',path)
    if style!='none': draw('black,line width=.45pt'+(','+style if style else ''),path)
# Upper left.
draw('yellow!65!black,line width=1.2pt','(650,451) ellipse (398 and 356)')
for y in [175,305,350,380,400,470,510,555,605,650,700,740]:
    draw('gray,line width=.35pt',f'(250,435) .. controls (500,{y}) and (850,{y+20}) .. (1040,430)')
ink('(365,230) .. controls (370,390) and (410,460) .. (450,495) .. controls (520,565) and (610,610) .. (680,630) .. controls (800,620) and (960,560) .. (1000,590)','dashed')
ink('(485,128) .. controls (525,220) and (570,290) .. (598,323) .. controls (650,405) and (660,470) .. (695,507) .. controls (750,570) and (795,684) .. (830,752)')
ink('(640,95) .. controls (690,178) and (748,245) .. (758,370) .. controls (750,438) and (720,478) .. (695,507) .. controls (641,552) and (608,610) .. (648,667) .. controls (680,711) and (750,735) .. (780,770)')
ink('(787,112) .. controls (720,183) and (640,235) .. (598,323) .. controls (560,400) and (556,474) .. (548,569) .. controls (556,651) and (590,722) .. (697,789)')
ink('(390,731) .. controls (421,605) and (422,533) .. (450,495) .. controls (485,420) and (506,388) .. (558,385) .. controls (707,390) and (932,360) .. (1037,330)')
ink('(514,803) .. controls (590,747) and (631,706) .. (678,630) .. controls (753,580) and (827,443) .. (839,368) .. controls (879,270) and (894,209) .. (892,151)','dashed')
draw('red!65!black,line width=2pt','(250,435)--(1040,430)')
for x,y in [(250,435),(1040,430),(450,495),(598,323),(695,507),(678,630),(616,715)]:
    lines.append(f'\\fill ({x},{y}) circle (3);')
lines.extend([r'\node at (530,818) {$0$};',r'\node at (387,673) {$\unsure{1}$};',r'\node at (626,660) {$\unsure{2}$};',r'\node at (598,707) {$\unsure{3}$};'])
# Upper right.
draw('yellow!65!black,line width=.7pt','(1672,585) ellipse (340 and 338)')
for y in [300,335,365,420,490,555,605,655,715,775,810,850]:
    draw('gray,line width=.35pt',f'(1335,560) .. controls (1550,{y}) and (1820,{y}) .. (2015,592)')
ink('(1384,420) .. controls (1430,495) and (1438,580) .. (1512,579) .. controls (1572,593) and (1601,474) .. (1638,527) .. controls (1665,572) and (1740,580) .. (1760,600) .. controls (1800,655) and (1795,710) .. (1822,715) .. controls (1870,752) and (1900,765) .. (1942,768)')
ink('(1470,321) .. controls (1490,488) and (1535,564) .. (1597,610) .. controls (1680,660) and (1790,742) .. (1850,868)','dashed')
ink('(1634,250) .. controls (1650,390) and (1570,477) .. (1527,507) .. controls (1470,551) and (1510,569) .. (1555,600) .. controls (1578,682) and (1615,714) .. (1665,754) .. controls (1710,812) and (1750,855) .. (1774,894)')
ink('(1699,249) .. controls (1692,400) and (1680,553) .. (1676,659) .. controls (1672,751) and (1655,828) .. (1657,930)')
ink('(1817,267) .. controls (1791,420) and (1795,511) .. (1813,597) .. controls (1840,694) and (1842,716) .. (1775,766) .. controls (1748,827) and (1640,858) .. (1519,891)','dashed')
ink('(1905,334) .. controls (1840,425) and (1784,457) .. (1692,513) .. controls (1590,565) and (1514,621) .. (1450,729) .. controls (1430,766) and (1430,804) .. (1424,834)')
ink('(1984,440) .. controls (1917,495) and (1918,584) .. (1902,663) .. controls (1888,709) and (1840,681) .. (1822,715) .. controls (1755,739) and (1700,799) .. (1625,800) .. controls (1530,799) and (1480,759) .. (1450,729) .. controls (1407,697) and (1368,703) .. (1344,714)','dashed')
draw('red!65!black,line width=2pt','(1335,560) .. controls (1500,390) and (1790,362) .. (2015,592) .. controls (1780,735) and (1480,674) .. cycle')
# Lower left.
draw('yellow!65!black,line width=.8pt','(1066,1466) ellipse (367 and 370)')
for y in [1115,1160,1220,1280,1330,1385,1430,1490,1550,1610,1660,1710,1770]:
    draw('gray,line width=.35pt',f'(700,1500) .. controls (915,{y}) and (1188,{y+10}) .. (1430,1500)')
ink('(927,1126) .. controls (976,1182) and (986,1304) .. (941,1396) .. controls (883,1445) and (899,1516) .. (948,1588) .. controls (990,1678) and (1180,1683) .. (1210,1792)')
ink('(1053,1097) .. controls (1059,1250) and (1044,1355) .. (1043,1393) .. controls (1048,1511) and (1039,1674) .. (1045,1832)','dotted')
ink('(1204,1128) .. controls (1250,1223) and (1297,1260) .. (1299,1391) .. controls (1287,1471) and (1254,1494) .. (1226,1615) .. controls (1206,1675) and (1118,1721) .. (1044,1755) .. controls (997,1762) and (945,1793) .. (920,1814)','dash dot')
ink('(1272,1163) .. controls (1275,1263) and (1231,1359) .. (1168,1430) .. controls (1115,1494) and (1049,1523) .. (1012,1540) .. controls (974,1567) and (1000,1620) .. (982,1630) .. controls (969,1725) and (881,1743) .. (828,1780)')
ink('(1325,1200) .. controls (1225,1280) and (1130,1360) .. (1043,1393) .. controls (995,1418) and (930,1446) .. (912,1497) .. controls (841,1558) and (798,1613) .. (768,1713)','dashed')
ink('(777,1236) .. controls (867,1312) and (920,1394) .. (982,1429) .. controls (1088,1540) and (1212,1641) .. (1287,1748)','dash dot')
ink('(724,1342) .. controls (810,1427) and (879,1440) .. (982,1429) .. controls (1090,1411) and (1140,1490) .. (1197,1576) .. controls (1247,1632) and (1312,1665) .. (1378,1652)')
ink('(702,1419) .. controls (795,1358) and (886,1245) .. (1054,1241) .. controls (1145,1275) and (1066,1335) .. (1093,1367) .. controls (1155,1423) and (1248,1478) .. (1387,1626)')
draw('red!65!black,line width=2pt','(700,1500) .. controls (864,1285) and (1225,1299) .. (1430,1500) .. controls (1212,1619) and (898,1638) .. cycle')
for x,y in [(941,1396),(1043,1393),(982,1429),(912,1497),(1168,1430),(982,1630),(1226,1615)]: lines.append(f'\\fill ({x},{y}) circle (3);')
# Lower right.
draw('yellow!65!black,line width=1.2pt','(2071,1463) ellipse (410 and 419)')
for y in [1160,1270,1335,1380,1410,1460,1500,1550,1610,1670,1725,1780,1840]:
    draw('gray,line width=.35pt',f'(1662,1418) .. controls (1880,{y}) and (2295,{y}) .. (2477,1465)')
ink('(1752,1240) .. controls (1810,1357) and (1867,1405) .. (1898,1495) .. controls (1937,1553) and (2017,1643) .. (2093,1668) .. controls (2180,1720) and (2289,1764) .. (2376,1768)','dashed')
ink('(1996,1065) .. controls (2058,1199) and (2110,1284) .. (2140,1398) .. controls (2190,1464) and (2235,1612) .. (2285,1745) .. controls (2294,1780) and (2303,1815) .. (2302,1840)','dotted')
ink('(2104,1041) .. controls (2024,1149) and (1976,1175) .. (2030,1326) .. controls (2090,1443) and (2070,1545) .. (2093,1668) .. controls (2084,1734) and (2098,1832) .. (2109,1882)','dashed')
ink('(2199,1069) .. controls (2138,1153) and (2058,1240) .. (2030,1326) .. controls (1987,1410) and (1980,1463) .. (1971,1576) .. controls (1977,1671) and (1964,1764) .. (1998,1861)','dash dot')
ink('(2287,1097) .. controls (2255,1190) and (2261,1323) .. (2275,1420) .. controls (2290,1531) and (2180,1638) .. (2093,1668) .. controls (2021,1701) and (1930,1734) .. (1811,1775)')
ink('(2385,1168) .. controls (2280,1197) and (2182,1290) .. (1981,1417) .. controls (1907,1453) and (1817,1559) .. (1729,1698)','dashed')
ink('(2471,1351) .. controls (2335,1395) and (2231,1430) .. (2140,1458) .. controls (2036,1478) and (1830,1517) .. (1662,1497)','dash dot')
ink('(1680,1356) .. controls (1770,1397) and (1880,1420) .. (1981,1417) .. controls (2060,1438) and (2140,1425) .. (2192,1481) .. controls (2275,1520) and (2382,1574) .. (2465,1608)','dashed')
for x,y in [(1898,1495),(1971,1576),(1981,1417),(2093,1668),(1977,1720),(2285,1745),(1811,1775)]: lines.append(f'\\fill ({x},{y}) circle (4);')
lines.extend([r'\node[anchor=west] at (212,875) {$\frac12$ circuits autour de pts d\textquotesingle ordre $1,2$};',r'\draw[->] (1100,790) to[bend right=12] (1002,668);',r'\draw[->] (1215,805)--(1307,744);',r'\draw[->] (1175,878) to[bend left=8] (1146,1024);',r'\node at (1393,994) {ou $0$};',r'\draw[->] (1495,1032) to[bend right=8] (1704,1232);',r'\end{tikzpicture}}',r'\mspage{80}'])
save({'scan':81,'text':'\n'.join(lines),'elements':[('drawing','upper left','circle; red diameter; intersecting orange curves; 0,1,2,3'),('drawing','upper middle right','circle; red lens; orange curves and grey arcs'),('text','middle left','1/2 circuits autour de pts d’ordre 1,2'),('drawing','middle','three arrows from 1,2 to drawings'),('text','middle','ou 0'),('drawing','middle right','arrow toward lower-right circle'),('drawing','lower left','circle; red lens; multiple orange paths'),('drawing','lower right','circle; orange paths with dotted and dashed portions'),('margin note','bottom left','80')]})
