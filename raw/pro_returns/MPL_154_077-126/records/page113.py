from save_page import save
t=r'''\scanpage{113}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[orange!80!brown,line width=1.4pt] (362,98)--(489,433) (463,99)--(331,453);
\draw[green!25!black,line width=1.8pt] (146,325)..controls(235,336)and(317,228)..(409,229)..controls(515,231)and(588,315)..(676,311);
\draw[green!25!black,line width=1.2pt,dashed] (153,289)..controls(244,283)and(308,189)..(412,197)..controls(526,201)and(604,289)..(684,279);
\draw[yellow!60!green,line width=1.8pt] (166,361)--(671,340);
\draw[yellow!60!green,line width=1.8pt,dashed] (172,396)--(683,383);
\draw[gray,line width=.4pt] (136,394)--(718,385) (208,277)--(262,142) (275,236)--(335,83) (351,201)--(404,80) (403,186)--(452,75) (462,201)--(539,92) (539,222)--(596,150) (599,242)--(658,162) (656,275)--(715,198) (194,415)--(305,532) (240,403)--(385,521) (305,405)--(469,521) (371,400)--(554,520) (435,396)--(635,526) (508,397)--(708,522) (593,397)--(781,514) (647,397)--(815,497);
\draw[<->] (275,249)--(270,377) (604,263)--(596,366);
\draw[->] (366,345)--(352,379) (470,354)--(478,375);
\fill (357,383) circle(4);
\node at (351,72) {$D_1$};\node at (501,75) {$D_2$};\node at (430,248) {$s$};\node at (304,443) {$D_2$};\node at (524,428) {$D_1$};
\end{tikzpicture}}
\uline{non} ! (le sommet $s$ disparaîtrait !)
Et $D_1\cap\Delta_{D'}$ \deleted{\unsure{se transf.}} $\mapsto D_2\cap\Delta_D$ et vice-versa.
[Pourtant, ça vaut la peine de regarder ce que ça donnerait !)
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[orange!80!brown,line width=1.4pt] (339,648)--(474,1051) (487,631)--(302,1068);
\draw[green!25!black,line width=1.7pt] (119,901)..controls(209,924)and(326,826)..(403,827)..controls(523,817)and(596,910)..(757,899);
\draw[green!25!black,line width=1.3pt,dashed] (190,845)..controls(288,826)and(344,772)..(410,779)..controls(506,772)and(601,849)..(703,853);
\draw[yellow!60!green,line width=1.8pt] (153,971)--(650,941);
\draw[yellow!60!green,line width=1.8pt,dashed] (147,935)--(691,908);
\draw[gray,dashed] (151,1005)--(708,972);
\draw[gray] (125,851)--(166,848) (808,687)..controls(801,722)and(804,743)..(805,767) (173,1043)--(252,1132) (735,1047)--(784,1088);
\draw[<->] (301,815)--(309,923) (559,815)--(568,916);
\draw[->] (699,897)--(752,899);
\draw[gray,line width=.4pt] (144,841)--(192,774) (172,844)--(224,774) (210,839)--(233,793) (240,825)--(262,777) (267,815)--(299,771) (304,795)--(326,764) (332,788)--(356,759) (350,774)--(370,751) (382,771)--(394,739) (448,777)--(458,752) (464,780)--(485,756) (489,784)--(507,762) (520,797)--(548,777) (536,802)--(566,780) (560,805)--(583,786) (587,816)--(614,789) (608,822)--(634,801) (146,927)--(133,909) (162,931)--(151,916) (180,930)--(166,916) (210,929)--(196,914) (233,928)--(222,914) (270,927)--(253,908) (295,924)--(276,906) (328,923)--(311,901) (352,921)--(331,903) (380,918)--(354,897) (414,916)--(390,899) (450,916)--(429,898) (485,914)--(466,894) (523,913)--(504,896) (550,912)--(531,895) (584,911)--(566,894) (614,910)--(591,892) (654,908)--(636,892) (776,884)--(786,905) (794,882)--(806,900);
\node at (326,680) {$D_1$};\node at (539,670) {$D_2$};\node at (101,891) {$D'$};\node at (118,979) {$D$};\node[gray] at (339,1089) {$D_2$};\node[gray] at (503,1074) {$D_1$};\node[gray] at (849,807) {$\Delta_{D'}$};
\draw (876,965)..controls(891,964)and(895,989)..(882,1008)..controls(874,1023)and(885,1038)..(872,1042)..controls(885,1050)and(874,1087)..(865,1101);
\node at (925,1047) {$\Delta_D$};
\end{tikzpicture}}
Ici, le sommet est conservé, et \unsure{on a} \deleted{les \unsure{deux}} $D_i\cap\Delta_D$ se continue en $D'\cap\Delta_{D'}$, c'est agréable -- mais dans la carte obtenue par un recollement \unsure{$h'$|$b'$}, je n'arrive pas à suivre les ``circuits autour d'un trou''
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\draw[orange!80!brown,line width=1.5pt] (2188,212)--(2326,607) (2347,189)--(2154,589);
\draw[green!25!black,line width=1.6pt] (2068,405)..controls(2142,398)and(2206,357)..(2261,361)..controls(2337,358)and(2401,389)..(2460,409);
\draw[green!25!black,line width=1.2pt,dashed] (2074,433)..controls(2143,444)and(2212,404)..(2272,403)..controls(2340,391)and(2393,409)..(2461,436);
\draw[yellow!60!green,line width=1.6pt] (2082,492)--(2444,496);
\draw[yellow!60!green,line width=1.6pt,dashed] (2087,535)--(2461,532);
\draw[gray,line width=.4pt] (2118,437)--(2107,459) (2130,435)--(2115,461) (2148,433)--(2132,458) (2169,429)--(2151,456) (2192,420)--(2172,446) (2212,415)--(2198,442) (2252,404)--(2234,431) (2277,404)--(2263,424) (2298,404)--(2284,424) (2326,407)--(2312,429) (2351,412)--(2336,433) (2370,417)--(2354,435) (2394,420)--(2377,442) (2419,428)--(2403,447) (2099,538)--(2074,588) (2139,537)--(2105,584) (2183,535)--(2137,588) (2223,532)--(2180,583) (2280,530)--(2243,587) (2327,532)--(2299,583) (2370,535)--(2333,587) (2407,535)--(2374,588) (2450,537)--(2413,585);
\draw[gray,<->] (2291,417)..controls(2315,438)and(2324,480)..(2309,518);\draw[gray,<->] (2378,420)--(2377,527);
\end{tikzpicture}}
Ici encore, $s$ disparaît au voisinage du lieu du \unsure{recollement}.
\figure{\begin{tikzpicture}[x=.013cm,y=-.013cm,line cap=round,line join=round]
\draw[orange!80!brown,line width=1.4pt] (2295,837)--(2400,1199) (2414,823)--(2240,1161);
\draw[green!25!black,line width=1.6pt] (2104,978)..controls(2228,961)and(2300,972)..(2523,957);
\draw[green!25!black,line width=1.3pt,dashed] (2113,1002)--(2533,998);
\draw[yellow!60!green,line width=1.7pt] (2125,1132)--(2666,1120) (2125,1079)--(2533,1077);
\draw[yellow!60!green,line width=1.7pt,dotted] (2110,1079)--(2125,1079) (2533,1077)--(2600,1077);
\draw[gray,line width=.4pt] (2138,1009)--(2128,1030) (2156,1010)--(2145,1031) (2176,1011)--(2160,1034) (2195,1013)--(2175,1035) (2210,1015)--(2197,1032) (2233,1014)--(2214,1035) (2251,1014)--(2238,1035) (2274,1013)--(2259,1035) (2294,1013)--(2278,1034) (2311,1012)--(2301,1034) (2345,1013)--(2330,1030) (2372,1014)--(2358,1032) (2408,1013)--(2398,1031) (2440,1013)--(2430,1032) (2476,1010)--(2466,1028) (2515,1006)--(2506,1027) (2139,1075)--(2128,1057) (2157,1074)--(2147,1058) (2178,1076)--(2163,1061) (2200,1075)--(2189,1061) (2227,1075)--(2213,1061) (2255,1074)--(2240,1060) (2279,1074)--(2267,1060) (2304,1076)--(2290,1064) (2328,1075)--(2313,1061) (2354,1076)--(2341,1062) (2382,1075)--(2369,1063) (2407,1075)--(2395,1062) (2431,1074)--(2426,1063) (2460,1074)--(2455,1062) (2486,1074)--(2481,1064) (2515,1074)--(2512,1065);
\end{tikzpicture}}
\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round,line join=round]
\draw[green!25!black,line width=1.8pt] (242,1816)..controls(235,1686)and(333,1561)..(464,1565)..controls(583,1570)and(685,1712)..(669,1827)..controls(661,1938)and(568,1994)..(466,2000)..controls(360,2010)and(259,1969)..(242,1852)--(242,1816);
\draw[gray] (241,1816)..controls(221,1961)and(332,2023)..(466,2011)..controls(606,2005)and(684,1919)..(674,1790);
\draw[green!25!black,line width=1pt,dashed] (325,1614)..controls(401,1564)and(507,1561)..(573,1618) (337,1968)..controls(427,2011)and(554,1972)..(610,1913);
\draw[yellow!60!green,line width=1.2pt,dashed] (397,1577)--(527,1590) (395,2008)..controls(437,2042)and(491,2023)..(534,1985);
\draw[orange!80!brown,line width=1.5pt] (443,1527)..controls(492,1580)and(505,1684)..(499,1827)..controls(498,1932)and(490,2006)..(435,2051) (489,1529)..controls(423,1575)and(392,1692)..(388,1796)..controls(383,1896)and(409,1987)..(497,2044);
\draw[orange!80!brown,line width=1.8pt] (315,1659)--(340,1688) (313,1685)--(339,1651) (320,1657)--(337,1678);
\draw[yellow!60!green,line width=1.7pt] (781,1891)..controls(765,1757)and(806,1641)..(890,1589)..controls(934,1559)and(944,1612)..(986,1614)..controls(1028,1610)and(1064,1573)..(1107,1599)..controls(1192,1647)and(1235,1715)..(1219,1820)..controls(1224,1934)and(1158,1985)..(1083,2016)..controls(1053,2083)and(952,2091)..(925,2021)..controls(822,2012)and(775,1987)..(781,1891);
\draw[yellow!60!green,line width=1.5pt] (799,1578)..controls(811,1573)and(827,1585)..(842,1595)..controls(846,1600)and(853,1607)..(870,1613);
\draw[yellow!60!green,line width=1.1pt] (1076,1591)..controls(1149,1624)and(1154,1718)..(1095,1820);
\draw[black,line width=.6pt] (780,1887)..controls(743,1711)and(803,1649)..(890,1591)..controls(929,1578)and(947,1624)..(984,1625);
\draw[dashed] (880,1621)..controls(927,1574)and(956,1659)..(1067,1611) (894,1991)..controls(943,1993)and(945,2006)..(953,2033)..controls(981,2061)and(1048,2065)..(1070,2014)--(1087,1996);
\draw[yellow!60!green,line width=1.1pt] (920,2018)..controls(956,2045)and(1006,2036)..(1069,2035);
\draw[orange!80!brown,line width=1.5pt] (980,1610)..controls(966,1737)and(977,1935)..(1010,2037)--(1033,2069) (1040,1611)..controls(1038,1774)and(1022,1981)..(1020,2020)--(993,2064);
\end{tikzpicture}}
\mspage{112}
'''
save({'scan':113,'sheet_kind':'text','text':t,'elements':[('drawing','upper left','D1 D2 s, green arch and yellow line, dashed copies and arrows'),('text','upper centre','non ! (le sommet s disparaîtrait !)'),('deletion','upper centre','se transf.'),('text','upper centre below','Pourtant, ça vaut la peine de regarder'),('drawing','middle left','D1 D2 D′ D, ΔD′ ΔD and hatching'),('text','centre','Ici, le sommet est conservé'),('deletion','centre','les deux'),('drawing','upper right','red X and green arch, dashed parallel curves'),('text','right margin','Ici encore, s disparaît'),('drawing','middle right','red X and horizontal solid and dashed curves'),('drawing','bottom left','green oval, orange lens and cross'),('drawing','bottom left, right member','yellow indented oval, orange lens and inner yellow curve'),('margin note','bottom left','112')]})
