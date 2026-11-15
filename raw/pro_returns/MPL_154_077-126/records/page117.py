from pathlib import Path
import re
from save_page import save
prior=Path('MPL_154_077-126/pages/MPL_154_077-126_154_scan098.tex').read_text()
banners=re.findall(r'\\begin\{verbatim\}.*?\\end\{verbatim\}',prior,re.S)[:2]
top=r'''\figure{\begin{tikzpicture}[x=.015cm,y=-.015cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.4pt] (2170,882)--(2790,868);
\draw[orange!80!brown,line width=1.8pt] (2170,815)..controls(2198,875)and(2230,968)..(2260,1020) (2248,810)--(2228,1047) (2345,748)--(2384,966) (2370,750)--(2318,928) (2525,747)--(2575,948) (2565,752)--(2505,946) (2704,825)--(2758,1005) (2775,828)--(2713,1010);
\draw[black!75!brown,line width=4pt] (2195,886)--(2245,886) (2328,874)--(2354,874) (2525,870)--(2560,870) (2718,871)--(2770,871);
\foreach \x in {2370,2400,...,2510}\draw[gray] (\x,878)--++(30,-30);
\foreach \x in {2250,2290,...,2500}\draw[gray] (\x,934)--++(55,-45);
\foreach \x in {2780,2793,...,2858}\draw[gray] (\x,869)--++(26,-35);
\foreach \x in {2138,2148,2158,2168}\draw[gray] (\x,847)--++(-5,28);
\node at (2337,849) {$a$};\node at (2556,838) {$b$};\node at (2214,919) {$a'$};\node at (2795,906) {$b'$};
\end{tikzpicture}}
'''
left=r'''\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\draw[gray!70] (419,1640)..controls(560,1585)and(775,1599)..(884,1630) (507,1750)..controls(550,1653)and(578,1628)..(567,1566) (790,1748)..controls(700,1678)and(714,1645)..(723,1581) (510,1938)..controls(534,2013)and(557,2044)..(585,2089) (791,1933)..controls(748,1980)and(740,2038)..(740,2116) (420,2056)..controls(376,2016)and(366,1948)..(365,1886) (926,2033)..controls(968,1987)and(964,1931)..(950,1866);
\draw[yellow!70!olive,line width=2.8pt] (284,1656)--(417,1640)--(407,1563) (507,1751)--(791,1747)--(793,1932)--(509,1937)--cycle (882,1565)--(886,1634)--(997,1635) (284,2067)--(416,2057)--(433,2153) (1023,2035)--(922,2037)--(909,2113);
\draw[black!75!brown,line width=4.2pt] (419,1640)--(507,1751) (791,1747)--(886,1634) (509,1937)--(416,2057) (793,1932)--(922,2037);
\draw[orange!80!brown,line width=2pt] (474,1540)..controls(404,1626)and(391,1717)..(390,1803) (355,1756)..controls(461,1786)and(544,1721)..(598,1680) (833,1574)..controls(933,1646)and(905,1742)..(934,1802) (720,1680)..controls(785,1780)and(883,1796)..(994,1788) (359,1870)..controls(364,2010)and(410,2090)..(492,2144) (330,1909)..controls(462,1885)and(546,1944)..(583,2045) (947,1838)..controls(993,1951)and(927,2053)..(873,2099) (737,2031)..controls(778,1927)and(889,1868)..(990,1912);
\foreach \y in {1812,1863}\draw (496,\y)--(520,\y);
\foreach \y in {1810,1860}\draw (781,\y)--(807,\y);
\foreach \x in {586,638,691}\draw (\x,1740)--++(0,29) (\x,1920)--++(0,28);
\node at (475,1844) {$(1)$};\node at (657,1969) {$(2)$};\node at (838,1832) {$(3)$};\node at (638,1716) {$(\unsure{4})$};
\node at (452,1553) {$\mu'$};\node at (381,1700) {$\mu'$};\node at (463,1757) {$\mu$};\node at (560,1694) {$\mu$};
\node at (810,1584) {$\lambda'$};\node at (948,1726) {$\lambda'$};\node at (742,1687) {$\lambda$};\node at (873,1773) {$\lambda$};
\node at (457,1894) {$\lambda$};\node at (592,1999) {$\lambda$};\node at (389,1974) {$\lambda'$};\node at (486,2109) {$\lambda'$};
\node at (727,1973) {$\mu$};\node at (852,1876) {$\mu$};\node at (912,1970) {$\mu'$};\node at (854,2093) {$\mu'$};
\draw[gray,->] (387,2114)--(391,2067) (975,1971)--(957,2009) (700,1622)--(716,1577);
\end{tikzpicture}}
'''
centre=r'''\figure{\begin{tikzpicture}[x=.018cm,y=-.018cm,line cap=round,line join=round]
\draw[gray!75] (1105,1796)--(1213,1567)--(1273,1734)..controls(1358,1673)and(1399,1615)..(1420,1586)--(1602,1752) (1144,1735)--(1273,1734)..controls(1346,1752)and(1365,1801)..(1398,1829)..controls(1466,1779)and(1545,1740)..(1602,1752) (1273,1734)..controls(1293,1788)and(1292,1817)..(1290,1847) (1359,1822)..controls(1431,1828)and(1502,1857)..(1572,1907)--(1618,1933) (1398,1829)..controls(1389,1875)and(1358,1918)..(1338,1961)..controls(1435,1978)and(1500,1941)..(1572,1907);
\draw[gray!75] (1205,1733)--(1209,1714) (1236,1734)--(1243,1714) (1366,1649)--(1380,1661) (1378,1638)--(1390,1648) (1469,1628)--(1458,1641) (1481,1640)--(1468,1653) (1327,1756)--(1317,1770) (1344,1770)--(1335,1787) (1365,1787)--(1354,1806) (1454,1790)--(1448,1774) (1485,1774)--(1478,1758) (1515,1763)--(1510,1745) (1417,1834)--(1410,1855) (1431,1837)--(1422,1859) (1443,1842)--(1435,1860) (1468,1849)--(1457,1873) (1478,1851)--(1467,1876) (1447,1954)--(1445,1974) (1460,1950)--(1457,1973) (1473,1948)--(1468,1970);
\node at (1207,1550) {$\unsure{y'}$};\node at (1424,1559) {$y$};\node at (1625,1749) {$x'$};\node at (1145,1647) {$\lambda'$};\node at (1252,1648) {$\lambda$};
\end{tikzpicture}}
'''
right=r'''\figure{\begin{tikzpicture}[x=.017cm,y=-.017cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=2.8pt] (1838,1543)--(1928,1542)--(1932,1439) (2019,1618)--(2277,1623)--(2274,1789)--(2020,1785)--cycle (2355,1405)--(2358,1511)--(2478,1510) (1834,1869)--(1942,1866)--(1953,1959) (2427,1870)--(2350,1863)--(2352,1971);
\draw[black!75!brown,line width=4pt] (1928,1542)..controls(1967,1585)and(1981,1608)..(2019,1618) (2277,1623)--(2358,1511) (2020,1785)--(1942,1866) (2274,1789)--(2350,1863);
\draw[orange!80!brown,line width=1.9pt] (1968,1470)..controls(1903,1556)and(1918,1590)..(1913,1643) (1869,1634)..controls(1980,1648)and(2074,1606)..(2103,1546) (2226,1455)..controls(2223,1529)and(2259,1569)..(2277,1623)..controls(2325,1665)and(2353,1662)..(2388,1682) (2208,1493)..controls(2288,1477)and(2351,1511)..(2420,1549) (1934,1719)..controls(1933,1811)and(1922,1859)..(1995,1929) (1900,1761)..controls(1992,1742)and(2050,1790)..(2102,1849) (2318,1746)..controls(2270,1799)and(2259,1858)..(2279,1914) (2226,1880)..controls(2310,1895)and(2364,1861)..(2409,1789);
\foreach \a/\b in {2074/2059,2114/2101,2156/2144}\draw[orange!80!brown,line width=1.7pt] (2025,1666)..controls(\a,1670)and(\b,1725)..(\a,1773);
\draw[orange!80!brown,line width=1.7pt] (2095,1640)..controls(2098,1688)and(2201,1720)..(2263,1730) (2127,1639)..controls(2141,1689)and(2206,1705)..(2264,1710) (2164,1639)..controls(2185,1680)and(2220,1680)..(2266,1680);
\foreach \x in {2101,2137,2173}\draw[orange!80!brown,line width=2pt,->] (\x,1616)--++(0,-43);
\foreach \x in {2099,2141,2187}\draw[orange!80!brown,line width=2pt,->] (\x,1791)--++(0,44);
\foreach \y in {1673,1706,1734}\draw[orange!80!brown,line width=1.8pt,->] (2278,\y)--++(43,0);
\foreach \y in {1668,1698,1725}\draw[orange!80!brown,line width=1.7pt,->] (1966,\y)--(2016,\y);
\foreach \x in {2223,2233,2243}\draw[line width=1.2pt] (\x,1613)--++(0,12);
\foreach \x in {2216,2226,2236,2246}\draw[line width=1.2pt] (\x,1781)--++(0,12);
\foreach \y in {1680,1709,1742}\draw (2264,\y)--(2281,\y);
\node at (1853,1699) {$\mathrm I$};\node at (2137,1949) {$\mathrm{II}$};\node at (2470,1729) {$\mathrm{III}$};\node at (2135,1441) {$\mathrm{IV}$};
\draw (1837,1717)--(1870,1717) (1838,1680)--(1873,1680) (2113,1923)--(2175,1920) (2121,1972)--(2160,1973) (2430,1698)--(2512,1693) (2436,1749)--(2496,1747) (2088,1418)--(2188,1403) (2092,1474)--(2155,1466);
\node at (1965,1595) {$b$};\node at (1976,1824) {$a$};\node at (2320,1814) {$b'$};\node at (2333,1553) {$a'$};\node at (1924,1888) {$x_0$};\node at (2034,1777) {$x$};\node at (2030,1624) {$y$};\node at (2272,1793) {$y'$};
\node at (1893,1584) {$\deleted{\unsure{\mu'}}$};\node at (1971,1567) {$\deleted{\unsure{\mu}}$};\node at (1978,1638) {$\deleted{\unsure{\mu}}$};\node at (1900,1646) {$\deleted{\unsure{b}}$};
\node at (2299,1482) {$\deleted{\unsure{\lambda'}}$};\node at (2247,1478) {$\deleted{\unsure{b}}$};\node at (2247,1567) {$\lambda$};\node at (2301,1539) {$\textcolor{orange!80!brown}{?}$};
\node at (1919,1822) {$\lambda'$};\node at (1909,1749) {$\deleted{\unsure{b}}$};\node at (1988,1773) {$\deleted{\unsure{\lambda}}$};\node at (2241,1821) {$\deleted{\unsure{\mu}}$};\node at (2270,1914) {$\deleted{\unsure{b}}$};\node at (2331,1911) {$\deleted{\unsure{\mu'}}$};
\node at (2300,1852) {$\textcolor{orange!80!brown}{?}$};\node at (2346,1714) {$\textcolor{orange!80!brown}{?}$};
\node at (2015,1660) {$\alpha$};\node at (2019,1700) {$\beta$};\node at (2014,1730) {$\sigma$};\node at (1982,1694) {$(1)$};\node at (2070,1627) {$\gamma$};\node at (2127,1642) {$\beta$};\node at (2170,1644) {$\sigma$};\node at (2175,1609) {$(\unsure{4})$};\node at (2076,1800) {$\sigma$};\node at (2124,1803) {$\beta$};\node at (2178,1802) {$\sigma$};\node at (2151,1840) {$(2)$};\node at (2308,1695) {$\unsure{\sigma}$};
\end{tikzpicture}}
'''
rows='\n'.join('****A START JOB 10 CRAY2    ROOM    5.00.02 PM 17 AUG 82 R6.PR1    SYS JES2 JOB 10 START A****' for _ in range(6))
notice=r'''\begin{verbatim}
DERNIERE MISE A JOUR DE JOURNAL : 11-08-82
ARRET DE L'ORDINATEUR LE MERCREDI 18 AOUT DE 7 H A 8 H.
ATTENTION .........
   ]         UN ARRET EXCEPTIONNEL POUR PREPARER L'ARRIVEE DE NOUVELLES
   ]         UNITES AURA LIEU DU VENDREDI 20 AOUT A 17H 30 AU LUNDI
   ]         23 AOUT A 8H.
\end{verbatim}
'''
text='\\scanpage{117}\n\\texttt{//* CRAY2 0010 I}\n'+'\n'.join(banners)+'\n'+top+'\\begin{verbatim}\n'+rows+'\n\\end{verbatim}\n'+notice+left+centre+right+'\\mspage{116}\n'
save({'scan':117,'sheet_kind':'reused_typed','text':text,'elements':[
('text','upper left','//* CRAY2 0010 I'),('text','upper left','0000 character banner'),('text','middle','CRAY2 letter banner'),('drawing','upper right','four red crossings on yellow line; a a-prime b b-prime; black intervals and hatching'),('text','middle lower','six START JOB 10 CRAY2 lines'),('text','lower left','DERNIERE MISE A JOUR DE JOURNAL; shutdown notices'),('drawing','bottom left','yellow square and four black diagonal corners; red curves; lambda mu primed; sides (1)-(4)'),('drawing','bottom centre','pencil branching curves and ticks; y y-prime x-prime lambda lambda-prime'),('drawing','bottom right','four-sided yellow region; four black diagonals; red curved transport arrows; I II III IV; questions and Greek labels'),('deletion','bottom right drawing','overwritten mu lambda and b labels'),('margin note','bottom left','116')]})
