from save_page import save
initial=r'''\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=1.7pt] (329,229)..controls(502,193)and(514,320)..(579,327)--(738,326) (336,342)..controls(497,349)and(466,313)..(515,271)..controls(569,236)and(688,237)..(761,239);
\draw[yellow!70!olive,line width=1.5pt,dashed] (337,275)..controls(451,285)and(492,329)..(576,328);
\draw[orange!80!brown,line width=1.4pt] (365,157)--(466,417) (444,146)--(367,427) (597,160)..controls(623,268)and(692,271)..(718,416) (699,143)--(609,392);
\draw[yellow!70!olive,line width=1.6pt] (274,710)--(770,715) (384,641)..controls(489,662)and(636,669)..(769,658);
\draw[yellow!70!olive,line width=1.5pt,dashed] (273,640)--(386,640)..controls(431,679)and(480,710)..(563,711);
\draw[orange!80!brown,line width=1.3pt] (352,545)--(424,782) (424,542)--(334,785) (556,551)--(654,778) (650,542)--(560,779);
\draw[black,line width=.8pt] (385,611)--(385,666) (385,643)..controls(515,669)and(686,667)..(767,660);
\draw[black,->,line width=.8pt] (272,656)--(314,656) (311,728)--(270,728) (385,714)--(385,693) (606,715)--(606,694) (774,674)--(735,674) (383,608)--(383,628);
\draw[yellow!70!olive,line width=1.6pt] (239,1044)..controls(342,1033)and(445,1037)..(537,1032);
\draw[yellow!70!olive,line width=1.5pt,dashed] (241,984)--(334,983)..controls(392,1018)and(462,1030)..(536,1030);
\draw[orange!80!brown,line width=1.3pt] (317,924)--(364,1094) (369,909)--(285,1085);
\draw[black,line width=1.2pt] (327,970)--(339,970) (310,1032)--(341,1032);
\draw[black,->,line width=.8pt] (242,998)--(282,998) (282,1054)--(238,1054);
\end{tikzpicture}}
'''
nb=r'''\figure{\begin{tikzpicture}[x=.008cm,y=-.008cm,line cap=round,line join=round]
\draw[yellow!70!olive,line width=1.8pt] (1989,928)--(2149,924);
\draw[orange!80!brown,line width=1.3pt] (2039,812)--(2100,980) (2074,824)--(2014,986);
\draw[black,line width=1.4pt] (2038,916)--(2073,916);\draw[black,->] (2059,914)--(2058,892);
\node at (2285,895) {donne};
\draw[yellow!70!olive,line width=1.8pt] (2392,920)--(2432,919)..controls(2437,889)and(2465,866)..(2493,870);
\draw[yellow!70!olive,line width=1.6pt,dashed] (2493,870)..controls(2523,872)and(2543,912)..(2576,919)--(2624,918);
\draw[orange!80!brown,line width=1.3pt] (2475,819)--(2545,985) (2523,818)--(2444,1002);
\draw[black,line width=1.6pt] (2490,849)--(2509,850);\draw[black,->] (2516,854)--(2516,892);
\draw[yellow!70!olive,line width=1.8pt] (1931,1042)--(2154,1043);
\draw[orange!80!brown,line width=1.3pt] (2028,997)--(2075,1097) (2077,993)--(2005,1106);
\draw[black,line width=1.6pt] (2036,1055)--(2059,1055);\draw[black,->] (2046,1040)--(2046,1013);
\node at (2295,1030) {donne};
\draw[yellow!70!olive,line width=1.8pt] (2487,1041)--(2521,1043)..controls(2560,1042)and(2567,994)..(2622,1001)--(2668,1003);
\draw[yellow!70!olive,line width=1.6pt,dashed] (2668,1003)..controls(2699,1019)and(2714,1034)..(2735,1040)--(2825,1041) (2519,1080)--(2607,1078);
\draw[orange!80!brown,line width=1.3pt] (2610,993)--(2672,1127) (2653,995)--(2600,1117);
\draw[black,line width=1.6pt] (2620,1007)--(2645,1008);\draw[black,->] (2660,1008)--(2660,1034);
\draw[yellow!70!olive,line width=1.8pt] (1523,1070)--(1658,1064);
\draw[orange!80!brown,line width=1.3pt] (1557,1035)--(1637,1133) (1604,1028)--(1559,1134);
\draw[black,line width=1.6pt] (1578,1052)--(1601,1052);\draw[black,->] (1559,1086)--(1520,1086);
\draw[black,->] (1723,1076)..controls(1756,1070)and(1747,1113)..(1795,1105);
\node at (1904,1120) {donne};
\draw[yellow!70!olive,line width=2.8pt,<->] (2071,1110)--(2201,1115);
\draw[orange!80!brown,line width=1.3pt] (2117,1087)--(2161,1151) (2142,1086)--(2109,1152);
\draw[yellow!70!olive,line width=1.8pt] (2210,1131)--(2326,1132);
\draw[orange!80!brown,line width=1.3pt] (2250,1088)--(2293,1149) (2275,1088)--(2236,1150);
\draw[black,line width=1.6pt] (2256,1121)--(2280,1121);\draw[black,->] (2225,1149)--(2188,1149);
\end{tikzpicture}}
'''
# The four rows retain their written order: 1, 2, 4, 3.
parts=[r'\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]']
for row,(y,num,grp,cap,mark) in enumerate([(1453,'1','I',-1,'below'),(1655,'2','I',-1,'above'),(1875,'4','II',1,'below'),(2076,'3','II',1,'above')]):
    x1=737; x2=934; out1=1357; out2=1564
    parts.append(r'\draw[yellow!70!olive,line width=1.8pt] (650,%d)--(1040,%d);'%(y+5,y-5))
    # orange crossing positions differ in the four rows
    cross_y=y-50 if row==0 else (y-55 if row==1 else y)
    cross_y2=y-93 if row==0 else (y if row==1 else y-75 if row==2 else y)
    for x,cy in [(x1,cross_y),(x2,cross_y2)]:
        parts.append(r'\draw[orange!80!brown,line width=1.4pt] (%d,%d)--(%d,%d) (%d,%d)--(%d,%d);'%(x-39,cy-72,x+49,y+65,x+35,cy-80,x-48,y+56))
    if row in [0,1]:
        parts.append(r'\draw[black,line width=2pt] (714,%d)--(761,%d);'%(y-5,y-5))
    else:
        parts.append(r'\draw[black,line width=2pt] (718,%d)--(742,%d);'%(y-24,y-24))
    parts.append(r'\node at (778,%d) {$a$};\node at (985,%d) {$a_0^{\prime}$};\node at (1054,%d) {$D$};\node at (558,%d) {%s)};\node at (1153,%d) {donne};'%(y-28,y-30,y+8,y+40,num,y-12))
    parts.append(r'\draw[black,->] (654,%d)--(609,%d);\node at (633,%d) {$\omega$};'%(y+28,y+28,y+49))
    if row in [0,2]:
        parts.append(r'\draw[black,dotted,line width=1.5pt] (905,%d)--(964,%d);'%(y-11,y-11))
    else:
        parts.append(r'\draw[black,line width=1.8pt] (919,%d)--(942,%d);'%(y-30,y-30))
    if row==1:
        parts.append(r'\draw[black,line width=2.2pt] (897,1735)--(965,1567);\node at (943,1683) {$\unsure{b}$};')
    crest=y+cap*55
    parts.append(r'\draw[yellow!70!olive,line width=1.8pt] (1251,%d)--(1283,%d)..controls(1297,%d)and(1297,%d)..(1357,%d)..controls(1410,%d)and(1404,%d)..(1432,%d)--(1673,%d);'%(y,y,y,crest,crest,crest,y,y,y-6))
    outcy=crest-7 if row<2 else crest-35
    for x,cy in [(out1,outcy),(out2,y-74 if row in [0,2] else y)]:
        parts.append(r'\draw[orange!80!brown,line width=1.4pt] (%d,%d)--(%d,%d) (%d,%d)--(%d,%d);'%(x-43,cy-72,x+42,y+66,x+36,cy-82,x-54,y+74))
    parts.append(r'\node at (1384,%d) {$b$};\node at (1590,%d) {$a^{\prime}$};\node at (1700,%d) {$D^{\prime}$};'%(crest-21,y-29,y+2))
    if row in [0,2]:parts.append(r'\draw[black,line width=2pt] (1537,%d)--(1580,%d);'%(y-16,y-16))
    else:parts.append(r'\draw[black,line width=2pt] (1553,%d)--(1574,%d);'%(y-21,y-21))
    parts.append(r'\draw[black,dotted,line width=1pt] (1339,%d)--(1373,%d);'%(crest-13,crest-13))
    if row<3:parts.append(r'\draw[black,->] (1235,%d)--(1275,%d);'%(y+22,y+22))
    else:parts.append(r'\draw[black,->] (1293,%d)--(1255,%d);'%(y+22,y+22))
    parts.append(r'\node at (1250,%d) {$\omega^{\prime}$};'%(y+46))
    if row==2:parts.append(r'\node at (1361,%d) {$\unsure{*}$};'%(crest+24))
parts.extend([r'\draw[black,line width=.7pt] (535,1445)..controls(536,1520)and(548,1538)..(509,1549)..controls(541,1559)and(516,1655)..(534,1714);',r'\draw[black,line width=.7pt] (523,1846)..controls(529,1895)and(528,1943)..(501,1955)..controls(536,1974)and(520,2056)..(534,2103);',r'\node at (449,1551) {$\mathrm{I}$};\node at (442,1958) {$\mathrm{II}$};',r'\draw[orange!80!brown,line width=.5pt] (1228,2017)--(1261,2028)--(1278,2027)--(1290,2020)--(1301,2059);',r'\end{tikzpicture}}'])
cases='\n'.join(parts)
text=r'''\scanpage{104}
'''+initial+r'''
Opération de rotation autour d'une face
par une flèche de transition

$(\unsure{\overleftarrow D|D},\omega,a)$, $D$ position relative\inserted{orientée}, $a$ arc de transition sur $\widetilde D$, on
trouve $(D',\omega',a')$ où
\deleted{on balaye sur l'arc de transition,}

a) $D'$ \unsure{déduite|déduit} de $D$ en \unsure{transit$^t$ suiv$^t$} $a$

b) $\omega'$ est l'orientat. \uline{opposée} à celle déduite de $\omega$ par transport

c) $a'$ est l'arc de transition sur $\widetilde D'$, qui \uline{suit} l'arc de
transition transporté de $a$, dans la direction $\omega'$.

\uline{NB} Le balayage du \unsure{lieu} de spécialisation

Le balayage de l'arc de spécialisation

l'antibalay. par des
'''+nb+r'''
Pour $\rho(D,\omega,-)=(D',\omega',a')$, \deleted{\unsure{les}}\inserted{\unsure{quatre}} cas à considérer se groupent par deux paires,
correspondant resp. aux cas où $a$ est un arc de spécialisation, un arc de généralisation
'''+cases+r'''
Dans tous les cas, pour déterminer
$a'$, on peut soit prendre l'arc $a'_0$\inserted{de transition}
qui suit $a$ sur $\widetilde D$ dans la direction
\uline{opposée} à $\omega$, et prendre son \uline{transporté}
par balayage\inserted{ou antibalayage}; soit transporter d'abord
$a$ en $b$ par la dite opération, et prendre
le successeur de $b$ pour $\omega'$, parmi
les arcs de transition sur $\widetilde D'$.
Cela résulte du fait que dans une
opération de spécialisation, l'isom can. entre
$\mathrm{Pol}(D)$ et $\mathrm{Pol}(D')$ induit une bijection entre
l'ens. des arcs de transition sur le premier,
\mspage{103}
'''
save({'scan':104,'text':text,'elements':[('drawing','upper left','two yellow paths and two orange crossings'),('text','upper right title','Opération de rotation autour d\'une face'),('text','upper right','(D,omega,a), D position relative'),('insertion','above position relative','orientée'),('deletion','below first paragraph','on balaye sur l\'arc de transition'),('text','upper right a','D\' déduite de D'),('text','upper right b','omega\' est l\'orientat.'),('text','upper right c','a\' est l\'arc de transition'),('drawing','middle left','two orange crossings; directed green paths and vertical arrows'),('drawing','left below middle','one crossing; solid and dashed green paths'),('text','middle','NB Le balayage du lieu de spécialisation'),('drawing','middle right first pair','balayage; donne; upward bend and downward arrow'),('text','middle','Le balayage de l\'arc de spécialisation'),('drawing','middle right second pair','crossing with upward arrow; donne; raised green path'),('text','middle','l\'antibalay. par des'),('drawing','middle','crossing; curved arrow; donne; green arrow and second crossing'),('text','middle below','Pour rho(D,omega,-)'),('deletion','formula line','les'),('insertion','formula line above deletion','quatre'),('drawing','lower left cases I','1) and 2); a, a0\', b, a\', D, D\', omega, omega\''),('drawing','lower left cases II','4) and 3); a, a0\', b, a\', D, D\', omega, omega\''),('text','lower right','Dans tous les cas, pour déterminer'),('insertion','lower right above a0\'','de transition'),('insertion','lower right above balayage','ou antibalayage'),('drawing','lower middle margin','small orange angular stroke'),('margin note','bottom left','103')]})
