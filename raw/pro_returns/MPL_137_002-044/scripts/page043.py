from record_page import record
tex=r'''\scanpage{43}
% archive foliation: 42
On trouve que
\[
\beta_*(C^i)=\deleted{\unsure{C_{i*}}}
(\cdots0\longrightarrow\cdots\ 0\longrightarrow
\overset{\unsure{i}}{k}\longrightarrow\overset{\unsure{i-1}}{k}\longrightarrow0\longrightarrow\cdots\longrightarrow0)
\quad\inserted{\text{pour }i\geqslant1},
\]
\[
\inserted{\beta_*(C^0)=(\cdots\deleted{\unsure{k}}\longrightarrow0\longrightarrow\underset{\text{deg }0}{k}\longrightarrow0)}
\]
et $\beta_*(d^i):C^i_*\xrightarrow{d^i}C^{i+1}_*$
est donné par
\[
(d^i)_{\unsure{i|i+1}}=\operatorname{id}_k\qquad i\geqslant0.
\]
\deleted{\unsure{On désignera désormais par} \inserted{$K_*$} la cat. des
complexes de chaînes \unsure{et ceci nous donne}
\unsure{une autre possibilité de construction}
d'un couple $(C,C^\bullet)$.}
\margin{\unsure{Ce n'est pas}\ \unsure{très bon}\ \unsure{de commencer}\
\unsure{à l'intégralité}\ \illegible{2}\ \unsure{pour}\ \unsure{fonctorialité}.}

\uline{Passage de l'exemple 1 à l'exemple 2}

Considérons le foncteur
\[
M\longmapsto M^\vee\qquad
\mathrm{Ab}_k^\circ\longrightarrow\mathrm{Ab}_k
\]
qui induit une équivalence de la catégorie
des \inserted{$k$-}modules libres de t.f. avec elle-même.
Cela donne aussi une équivalence entre
les cat. des complexes de chaînes et cochaînes
à comp. \deleted{\unsure{K_*=K^\vee}} libres de t.f., et entre
celles où les $Z_n$ (et $Z^i$) sont libres de t.f. et \unsure{bornées}.
\deleted{\unsure{On peut donc}\ \unsure{supposer}\ \unsure{les deux équivalences}\
\unsure{et on peut les composer}.}
\deleted{\unsure{On a donc}\ \unsure{par}\ $\alpha^\bullet_*(K)$\ \unsure{et}\ $\alpha'^{\vee}$}
un diagramme d'équivalences
\diagram{\begin{tikzcd}[row sep=large,column sep=large]
\deleted{\unsure{K_*}}\ C\arrow[r,"\alpha_*","\simeq"']\arrow[d,"(\alpha')^\circ"',"\simeq"]&K_*\arrow[dl,"\simeq"]\\
K^{\bullet\circ}&
\end{tikzcd}}
\deleted{\unsure{Les deux définissent une même}\ \unsure{dualité}\
\unsure{en particulier}\ \unsure{à $A$}\ \unsure{ce qui est trivial}.}

\uline{\unsure{Explicitons quand même}}

\uline{Prop. 2} On a une dualité parfaite fonctorielle
en $M\in\operatorname{Ob}K_*$ (et \unsure{vice versa})
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\alpha_k(M)_{\unsure{n|i}}\arrow[d,equal]&\mathbin{\times}&
\alpha'^{\unsure{n|i}}(M)\arrow[d,equal]\arrow[r]&k\arrow[d,"\simeq"]\\
\operatorname{Hom}(C^{\unsure{n|i}}_*,M)&\mathbin{\times}&
\operatorname{Hom}(M,C^{\unsure{n|i}}_*)\arrow[r,"{\text{par }\circ}"']&
\operatorname{Hom}(C^{\unsure{n|i}}_*,C^{\unsure{n|i}}_*)\arrow[r,"\simeq"]&k
\end{tikzcd}}
'''
fig=r'''\margin{\figure{\begin{tikzpicture}[x=.006cm,y=-.006cm,line width=.3pt]
\foreach \a in {0,130,260,390,520,650,780,910,1040,1170,1300,1430,1560,1690,1820,1950,2080}{\foreach \b in {0,12,24,36,48}{\draw[gray!55,line width=.12pt](0,{\a+\b})--(640,{\a+\b});}}
% Separate manually positioned pen strokes, respecting the visible columns and row offsets.
\foreach \x/\y in {180/315,190/505,190/645,300/735,300/875,440/900,610/1015,190/1155,290/1240,440/1135,440/1195,610/1270,290/1410,190/1600,290/1670,440/1690,170/1730,300/1820,440/1830,610/1810,170/1880,50/1970,290/1980}{\draw(\x,\y) .. controls(\x,{\y-15}) and({\x+5},{\y-30})..({\x+3},{\y-45});\draw(\x,\y).. controls({\x-3},{\y+10}) and({\x-5},{\y+22})..({\x-12},{\y+23});}
\foreach \x/\y in {300/325,300/430,70/470,75/565,180/850,380/865,385/920,290/1100,610/1100,290/1190,535/1170,440/1290,190/1325,530/1380,290/1550,75/1560,385/1570,440/1580,525/1630,610/1640,290/1770,610/1760,175/1815,440/1940,535/1985,385/2060,435/2085,170/2050}{\draw({\x+3},{\y-15})..controls({\x-4},{\y-10})and({\x+8},\y)..(\x,{\y+8})..controls({\x-9},{\y+15})and({\x+6},{\y+18})..(\x,{\y+27})..controls({\x-8},{\y+34})and({\x+9},{\y+39})..({\x+5},{\y+43});}
\foreach \x/\y in {365/240,380/307,380/590,380/750,380/980,300/1030,190/1070,290/1140,380/1285,440/1320,610/1420,440/1455,190/1470,440/1510,300/1580,190/1690,535/1750,300/1850,440/1890,535/1930,170/2070,290/2075,440/2100}{\draw[rotate around={-20:(\x,\y)}](\x,\y)ellipse(10 and 5);}
\foreach \x/\y in {350/140,75/324,195/440,308/620,205/965,610/970,301/1012,530/1055,440/1090,195/1140,525/1150,610/1155,195/1280,440/1415,535/1470,380/1530,440/1550,535/1580,190/1688,440/1710,300/1795,535/1780,535/1850}{\fill(\x,\y)circle(2);}
\draw(350,195)..controls(385,174)and(417,180)..(429,202);
\draw(54,324)..controls(80,318)and(92,319)..(106,330);
\draw(347,297)..controls(363,322)and(404,330)..(408,304);
\draw(350,452)..controls(375,475)and(393,475)..(416,460);
\draw(75,684)..controls(106,674)and(121,691)..(110,710);
\draw(100,800)..controls(120,793)and(127,805)..(134,819);
\draw(46,948)..controls(43,1009)and(95,1011)..(92,957);
\draw(50,1060)..controls(76,1090)and(100,1092)..(112,1070);
\draw(530,1082)..controls(560,1118)and(580,1100)..(568,1086);
\draw(47,1250)..controls(101,1268)and(110,1240)..(94,1217);
\draw(180,1251)..controls(199,1231)and(213,1240)..(222,1253);
\draw(280,1205)--(280,1308);\draw(256,1265)--(310,1255);
\draw(380,1215)..controls(395,1166)and(411,1183)..(408,1227);\draw(382,1220)--(382,1290);
\draw(48,1375)..controls(67,1400)and(80,1380)..(73,1402)--(62,1438);\draw(91,1368)--(92,1445);
\draw(353,1340)--(390,1358)--(359,1393)--(407,1413);
\draw(440,1414)..controls(465,1395)and(486,1418)..(478,1450);
\draw(75,1498)..controls(94,1481)and(112,1495)..(113,1518);
\draw[->](535,1545)--(535,1465);
\draw(349,1660)..controls(337,1690)and(370,1723)..(388,1690)..controls(384,1670)and(389,1658)..(385,1656);
\draw(520,1732)..controls(520,1792)and(550,1792)..(549,1748);
\draw(74,1910)..controls(69,1931)and(94,1946)..(93,1916);
\draw(352,1860)..controls(340,1890)and(367,1928)..(394,1895);
\draw(150,1901)..controls(172,1888)and(197,1885)..(204,1920);
\draw(64,2068)..controls(89,2090)and(102,2115)..(81,2115)..controls(56,2102)and(54,2087)..(64,2068);
\draw(50,1960)--(45,2040);\draw(290,1990)..controls(270,2018)and(307,2029)..(290,2047);
\draw(170,2020)..controls(170,2043)and(196,2042)..(201,2040)--(165,2053);
\draw(440,2050)..controls(452,2067)and(465,2072)..(455,2087)..controls(480,2113)and(487,2125)..(473,2130);
\draw(320,-30)..controls(520,15)and(493,100)..(504,280)--(520,800)..controls(520,890)and(550,908)..(600,920)..controls(680,945)and(682,1000)..(682,1050)--(695,1470);
\draw[->](682,1470)..controls(674,1490)and(635,1485)..(630,1455);
\end{tikzpicture}}}
% crop-candidate: scan 43
'''
tex=tex.replace('\nqui induit une équivalence', '\n'+fig+'\nqui induit une équivalence')
record(43,tex,[('text','top','On trouve que'),('display','top','β*(Ci)=elementary chain, degree i,i−1'),('deletion','top after equality','C_i*'),('insertion','top right','pour i≥1'),('display','top right inserted','β*(C0)=(…0→k→0), deg0'),('deletion','β*(C0) old entry','k'),('text','upper','et β*(di):Ci*→Ci+1* est donné par'),('display','upper','(di)i=id_k, i≥0'),('deletion','upper paragraph diagonal strokes','On désignera désormais … cat complexes de chaînes … construction couple'),('insertion','upper paragraph','K*'),('margin note','left upper diagonal','Ce n’est pas … commencer … intégralité … fonctorialité'),('text','heading','Passage de l’exemple 1 à l’exemple 2'),('text','middle','Considérons le foncteur'),('display','middle','M↦M∨, Ab_k°→Ab_k'),('drawing','left lower margin','pen exercises: curves, braces, note-shaped marks, arrows, and large enclosing curve'),('text','middle','équivalence catégorie modules libres t.f.'),('insertion','above modules','k-'),('text','middle-lower','équivalence complexes chaînes/cochaînes libres t.f.; cycles Z_n Z^i'),('deletion','middle-lower after comp','K*=K∨'),('deletion','middle-lower several lines','On peut donc … deux équivalences … composer'),('deletion','before diagram introduction','On a donc par α*(K) et α′∨'),('text','lower-middle','un diagramme d’équivalences'),('diagram','lower-middle','C→K*; C→K•°; K*→K•°'),('deletion','in diagram before C','K*'),('deletion','below diagram','Les deux définissent … dualité … A … trivial'),('text','before Prop 2','Explicitons quand même'),('text','Prop 2','dualité parfaite fonctorielle en M∈ObK*'),('diagram','bottom','α_k(M)_n×α′^n(M)→k; Hom(Cn*,M)×Hom(M,Cn*) composition into End≃k')],doubts=[('top elementary chain degrees','i, i−1','several blue overwritten digits; i+1 on right is possible','low'),('differential component','(di)_i','(di)_{i+1}; overwritten subscript','low'),('crossed paragraph opening','On désignera désormais par K*','On donne …; long crossed wording faint beneath staff','low'),('crossed paragraph second and third lines','et ceci nous donne une autre possibilité de construction','multiple uncertain joins; construction visibly recoverable','low'),('diagonal margin note','Ce n’est pas très bon de commencer à l’intégralité … pour fonctorialité','some words physically unreadable; two estimated words marked illegible after zoom and rotation','low'),('duality paragraph final qualification','bornées','homotopies; end of line very faint','low'),('first heavily cancelled middle formula','K*=K∨','overwritten K and indices','low'),('two cancelled prose lines','On peut donc supposer les deux équivalences et on peut les composer','recovered words tentative; extensive faint cancellation','low'),('cancelled next line','On a donc par α*(K) et α′∨','superscript and object letter uncertain','low'),('equivalence diagram category K','K_*, K^{bullet circ}','source uses ornamented K with changing decorations','medium'),('cancelled sentence below diagram','Les deux définissent une même dualité en particulier à A ce qui est trivial','faint full-line crossing; all uncertain words marked','low'),('underlined introduction','Explicitons quand même','Explicitons pourtant; two small words obscured by staff','low'),('Prop 2 parenthesis','et vice versa','et image …; very faint','low'),('Prop 2 indices','n','i; upper and lower indices kept uncertain across corresponding Hom terms','low'),('marginal pen exercises','TikZ manual approximation','not text-recognized; approximate curves and relative positions, including enclosure','low')],notation=[('linear dual',r'$M^\vee$','scan 43 middle; vee, not a prime'),('categories of finite complexes',r'$K_*,K^{\bullet\circ}$','scan 43 equivalence triangle'),('comparison via perfect pairings',r'$\operatorname{Hom}(C^n_*,M)\times\operatorname{Hom}(M,C^n_*)\to\operatorname{Hom}(C^n_*,C^n_*)\simeq k$','scan 43 bottom; n/i locally doubtful')])
