from pathlib import Path
import re
from save_page import save
s=Path('MPL_154_077-126/pages/MPL_154_077-126_154_scan096.tex').read_text()
blocks=re.findall(r'\\begin\{verbatim\}.*?\\end\{verbatim\}',s,re.S)
zero=[(11,'00000000'),(9,'0000000000'),(7,'00      0000'),(6,'00     00 00'),(5,'00    00  00'),(4,'00   00   00'),(3,'00  00    00'),(2,'00 00     00'),(1,'0000      00'),(0,'000       00'),(0,'0000000000'),(0,'00000000')]
fives=[(37,'555555555555'),(36,'555555555555'),(35,'55'),(34,'55'),(33,'55'),(32,'555555555'),(31,'5555555555'),(39,'55'),(39,'55'),(38,'55'),(27,'555555555555'),(26,'55555555555')]
ones=[(56,'11'),(54,'111'),(52,'1111'),(53,'11'),(52,'11'),(51,'11'),(50,'11'),(49,'11'),(48,'11'),(47,'11'),(42,'1111111111'),(41,'1111111111')]
nums=[]
for z,f,o in zip(zero,fives,ones):
 line=[' ']*70
 for off,word in [z,(z[0]+14,z[1]),f,o]: line[off:off+len(word)]=word
 nums.append(''.join(line).rstrip())
f1=r'''\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\node at (1410,1390) {$?$};\node at (1373,1916) {$?$};
\draw[yellow!70!olive,line width=2.4pt] (1185,1514)..controls(1190,1491)and(1230,1472)..(1261,1456)..controls(1294,1457)and(1312,1473)..(1334,1488)..controls(1350,1462)and(1386,1453)..(1402,1465)..controls(1425,1467)and(1447,1496)..(1462,1484)..controls(1551,1447)and(1592,1458)..(1582,1510)--(1571,1804)..controls(1555,1876)and(1519,1867)..(1497,1865)..controls(1460,1866)and(1455,1829)..(1431,1836)..controls(1419,1841)and(1408,1860)..(1389,1861)..controls(1378,1862)and(1370,1848)..(1366,1856)..controls(1349,1874)and(1320,1842)..(1308,1830)..controls(1291,1851)and(1260,1875)..(1232,1861)..controls(1175,1868)and(1165,1848)..(1169,1807)--cycle;
\draw[orange!80!brown,line width=1.6pt] (1262,1460)--(1231,1860) (1292,1464)..controls(1299,1619)and(1324,1749)..(1168,1775) (1522,1469)--(1497,1865) (1554,1470)..controls(1538,1648)and(1600,1720)..(1438,1772)..controls(1331,1755)and(1327,1654)..(1336,1522) (1178,1599)..controls(1200,1743)and(1255,1739)..(1307,1745)..controls(1458,1767)and(1484,1591)..(1446,1489)..controls(1407,1439)and(1350,1468)..(1336,1522)..controls(1302,1655)and(1225,1712)..(1176,1715) (1292,1464)..controls(1306,1579)and(1386,1666)..(1445,1702)..controls(1495,1691)and(1563,1626)..(1584,1537) (1446,1489)..controls(1447,1601)and(1466,1703)..(1574,1736);
\draw[orange!80!brown,line width=1.6pt] (1395,1465)--(1375,1848) (1373,1473)..controls(1339,1596)and(1321,1726)..(1315,1820)..controls(1310,1840)and(1337,1854)..(1356,1855) (1451,1497)..controls(1454,1620)and(1449,1719)..(1432,1829)..controls(1421,1852)and(1402,1858)..(1388,1857);
\draw[cyan!35!gray,line width=2pt,dashed] (1395,1475)..controls(1373,1466)and(1344,1501)..(1342,1530)..controls(1334,1630)and(1310,1764)..(1324,1813)..controls(1329,1842)and(1379,1848)..(1387,1842)..controls(1431,1831)and(1437,1802)..(1437,1750)--(1440,1527)..controls(1438,1493)and(1412,1486)..(1395,1475);
\draw[black!80!green,line width=3pt] (1261,1456)..controls(1294,1457)and(1312,1473)..(1334,1488)..controls(1350,1462)and(1386,1453)..(1402,1465)..controls(1425,1467)and(1447,1496)..(1462,1484)--(1522,1469) (1232,1861)..controls(1260,1875)and(1291,1851)..(1308,1830)..controls(1320,1842)and(1349,1874)..(1366,1856)..controls(1370,1848)and(1378,1862)..(1389,1861)..controls(1408,1860)and(1419,1841)..(1431,1836)..controls(1455,1829)and(1460,1866)..(1497,1865);
\end{tikzpicture}}
'''
f2=r'''\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.6pt] (1968,1404)--(2028,1355)--(2110,1343)--(2179,1209)--(2260,1150) (2179,1209)--(2116,1140) (2110,1343)--(2053,1287)--(2061,1200) (2053,1287)--(1962,1287) (2028,1355)--(2008,1317) (2110,1343)--(2059,1394)--(2010,1403) (2059,1394)--(2060,1417) (2110,1343)--(2198,1309)--(2242,1331) (2198,1309)--(2207,1263) (2110,1343)--(2186,1364)--(2241,1364) (2186,1364)--(2169,1403);
\draw[orange!80!brown,line width=1.6pt] (2110,1343)--(2103,1460);
\end{tikzpicture}}
'''
f3=r'''\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.7pt] (1649,1950)--(1830,1933)--(1954,1747)--(2050,1743) (1954,1747)--(1887,1648) (1954,1747)--(1969,1821) (1830,1933)--(1784,1798) (1830,1933)--(1851,2076)--(1779,2143) (1851,2076)--(1904,2144) (1830,1933)--(1961,1932)--(2061,1834) (1961,1932)--(2032,2031)--(2135,1949) (2032,2031)--(1956,2096);
\draw[gray,line width=.3pt] (1831,1929)--(1956,1749)--(2080,1643);
\draw[orange!80!brown,line width=1.5pt] (1960,1734)--(2029,1593) (2032,2031)--(2028,2143) (2032,2031)--(2102,2135);
\draw[yellow!70!olive,line width=2pt] (1963,1611)--(2029,1593)--(2188,1589) (2029,1593)--(1971,1488) (2029,1593)--(2114,1473) (2029,1593)--(2032,1512) (2029,1593)--(2061,1643);
\draw[orange!80!brown,line width=1.5pt] (1963,1611)..controls(1932,1523)and(1981,1462)..(2044,1472)..controls(2140,1473)and(2198,1558)..(2150,1617)..controls(2080,1669)and(1974,1678)..(1963,1611);
\draw[black!70!brown,line width=2.4pt] (1963,1611)--(2029,1593)--(2157,1581) (2029,1593)--(1971,1495) (2029,1593)--(2095,1488) (2029,1593)--(2032,1520) (2029,1593)--(2061,1643);
\draw[yellow!70!olive,line width=2pt] (1963,2175)--(2028,2143)--(2050,2128) (2102,2135)--(2180,2097);
\draw[orange!80!brown,line width=1.5pt] (1963,2140)..controls(1944,2190)and(2021,2220)..(2044,2173)..controls(2060,2140)and(2041,2104)..(2006,2114) (2074,2169)..controls(2047,2115)and(2119,2040)..(2152,2087)..controls(2181,2124)and(2189,2204)..(2120,2199)..controls(2102,2205)and(2086,2192)..(2074,2169);
\draw[black!70!brown,line width=2pt] (1963,2175)--(2028,2143)--(2048,2128) (2028,2143)--(1982,2124) (2028,2143)--(1992,2112) (2028,2143)--(2036,2190) (2074,2169)--(2102,2135)--(2170,2108) (2102,2135)--(2111,2082) (2102,2135)--(2077,2190) (2102,2135)--(2140,2182);
\end{tikzpicture}}
'''
f4=r'''\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm]\draw[orange!80!brown,line width=1.7pt] (2213,1569)--(2378,1573)--(2370,1927)--(2204,1925)--cycle (2298,1572)--(2293,1927);\end{tikzpicture}}
'''
rows='\n'.join('****A END JOB 344 CRAY2    ROOM    3.08.54 PM 19 AUG 82 R6.PR1    SYS JES2 JOB 344 END A****' for _ in range(6))
text='\\scanpage{100}\n\\texttt{//* CRAY2 0344 I}\n\\begin{verbatim}\n'+'\n'.join(nums)+'\n\\end{verbatim}\n'+blocks[1]+'\n\\begin{verbatim}\n'+rows+'\n\\end{verbatim}\n'+f2+f1+f3+f4+'\\mspage{99}\n'
save({'scan':100,'sheet_kind':'reused_typed','text':text,'elements':[
('text','upper left','//* CRAY2 0344 I'),('text','upper left','0051 numeral banner'),('text','middle','CRAY2 letter banner'),
('text','middle lower','six END JOB 344 CRAY2 lines'),
('drawing','right overlapping job lines','yellow branching graph with red stem'),
('drawing','lower centre','yellow scalloped boundary, red crossing curves, blue dashed loop, black arcs; question marks above and below'),
('drawing','lower right','yellow branching graph with red attachments and three circled local stars'),
('drawing','right','red rectangle divided vertically'),
('margin note','bottom left','99')
]})
