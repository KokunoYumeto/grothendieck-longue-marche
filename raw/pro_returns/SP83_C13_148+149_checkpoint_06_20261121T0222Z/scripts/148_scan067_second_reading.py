from pathlib import Path
import csv,json,hashlib,re,os
root=Path('/workspace/scratch/f28c4f52d3ec'); page='148_scan067'
R={}
class Fig:
 def __init__(self,s=.0026):
  self.a=[r'\figure{\begin{tikzpicture}[x='+str(s)+r'cm,y=-'+str(s)+r'cm,line cap=round,line join=round,every node/.style={inner sep=1pt,font=\scriptsize}]']
 def raw(self,s): self.a.append(s); return self
 def path(self,s,style='black,line width=.45pt'): self.a.append(r'\draw['+style+'] '+s+';'); return self
 def node(self,x,y,s,style=''): self.a.append(r'\node['+style+'] at ('+str(x)+','+str(y)+') {'+s+'};'); return self
 def dot(self,x,y,r=10,style='black'): self.a.append(r'\fill['+style+'] ('+str(x)+','+str(y)+') circle[radius='+str(r)+'];'); return self
 def done(self): return '\n'.join(self.a+[r'\end{tikzpicture}}'])
R['B01']=r"""Un pantalon \inserted{(topologique)} subdivisé de
façon standard, avec un ens
$J$ de trous $(\operatorname{card}J=3)$ correspond
à un ``triangle pondéré'' i.e.
\diagram{\begin{tikzcd}J\arrow[r,"\pi"]&\mathbb N\end{tikzcd}}
(NB $\pi(j)=$ nb d'arêtes
qui relient $j$ et $k$, """+Fig(.018).path('(0,7) .. controls (5,4) and (11,4) .. (14,6)','gray,line width=.3pt').path('(1,0)--(2,2) (11,-2)--(12,0)','gray,line width=.25pt').done()+r""" $i\neq j\neq k$)"""
R['B02']=r"""Carte \inserted{\unsure{orientée|orienté}} découpée pantaloniquement,
de façon standard $\Longleftrightarrow$ \deleted{graphe} un graphe pantalonien \unsure{globulisé}"""
b03=r"""marqués sont d'ordre $3$ (\unsure{avec} des sommets \unsure{polygones}
non marqués d'ordre $1$ éventuellement), et est muni
d'une pondération des \deleted{arêtes \illegible{1}}\inserted{drapeaux de type $0,1$}
(sommet \inserted{\unsure{marqué}} et arête incidents) de telle façon
que l'on ait pour chaque
arête (cf ci-contre)"""
R['B03']=r"""\deleted{(i.e. carte cellulaire (\unsure{p. ex.|par ex.} orientée), dont les sommets}
\unsure{"""+b03+r'|\deleted{'+b03+'}}'
f=Fig(.0028)
# The red boundary contours retain their individual shapes; faint preliminary runs remain separate.
f.path('(1500,255) .. controls (1130,250) and (800,480) .. (620,700) .. controls (380,1000) and (240,1250) .. (270,1510) .. controls (300,1880) and (440,2230) .. (650,2400) .. controls (960,2680) and (1320,2750) .. (1630,2680) .. controls (2010,2670) and (2340,2520) .. (2470,2420) .. controls (2760,2180) and (2860,1830) .. (2820,1500) .. controls (2790,1120) and (2540,760) .. (2200,480) .. controls (1950,300) and (1680,240) .. (1500,255)','red!45!black,line width=.65pt')
f.path('(660,2410) .. controls (950,2760) and (1380,2780) .. (1670,2710) .. controls (2170,2680) and (2670,2340) .. (2830,1780) .. controls (2900,1310) and (2590,780) .. (2210,490)','gray,line width=.3pt')
f.path('(1280,1200) .. controls (1375,1200) and (1420,1260) .. (1430,1330) .. controls (1475,1410) and (1495,1515) .. (1470,1590) .. controls (1445,1690) and (1420,1770) .. (1370,1790) .. controls (1300,1850) and (1140,1840) .. (1050,1690) .. controls (950,1600) and (915,1490) .. (960,1390) .. controls (1000,1295) and (1120,1175) .. (1280,1200)','red!45!black,line width=.6pt')
f.path('(1045,1690) .. controls (1130,1870) and (1320,1870) .. (1400,1780)','gray,line width=.28pt')
f.path('(2075,1330) .. controls (2150,1260) and (2280,1250) .. (2330,1350) .. controls (2460,1460) and (2450,1600) .. (2380,1720) .. controls (2280,1920) and (2120,1950) .. (2010,1855) .. controls (1870,1790) and (1875,1660) .. (1900,1600) .. controls (1900,1490) and (1970,1385) .. (2075,1330)','red!45!black,line width=.6pt')
f.path('(1900,1600) .. controls (1860,1760) and (1980,1920) .. (2130,1930) .. controls (2290,1940) and (2430,1690) .. (2440,1510)','gray,line width=.28pt')
# Direction strokes in red, including the separate doubled lower-right run.
f.path('(2225,505)--(2180,468)--(2200,520)','red!45!black,line width=.85pt')
f.path('(760,570)--(724,628)--(773,606)','red!45!black,line width=.85pt')
f.path('(1457,1425)--(1463,1480)--(1443,1450)','red!45!black,line width=.75pt')
f.path('(1968,1450)--(2008,1400)--(1970,1420)','red!45!black,line width=.75pt')
f.path('(2465,2385)--(2445,2440) (2480,2397)--(2460,2455)','red!45!black,line width=.7pt')
for s in [
'(1510,280) .. controls (1460,570) and (1320,900) .. (1300,1200)',
'(790,575) .. controls (900,820) and (1035,1080) .. (1100,1240)',
'(420,950) .. controls (610,1100) and (790,1260) .. (1020,1320)',
'(290,1510) .. controls (510,1450) and (755,1430) .. (960,1480)',
'(650,2400) .. controls (800,2180) and (930,1900) .. (1050,1690)',
'(1430,1330) .. controls (1650,1215) and (1870,1230) .. (2075,1330)',
'(1470,1590) .. controls (1610,1570) and (1760,1590) .. (1900,1600)',
'(1370,1790) .. controls (1540,1810) and (1730,1800) .. (1920,1790)',
'(1200,1810) .. controls (1460,2160) and (1810,2180) .. (2100,1900)',
'(2290,1300) .. controls (2460,1160) and (2540,1070) .. (2690,980)',
'(2425,1530) .. controls (2570,1480) and (2680,1460) .. (2820,1440)',
'(2280,1850) .. controls (2470,1860) and (2640,1890) .. (2800,1960)']:
 f.path(s,'gray,line width=.32pt')
labels=[(1510,135,r'b_1^\infty'),(710,420,r'b_2^\infty'),(325,865,r'b_3^\infty'),(120,1460,r'b_4^\infty'),(490,2470,r'b_5^\infty'),(2770,970,r'a_1^\infty'),(2940,1430,r'a_2^\infty'),(2930,1960,r'a_3^\infty'),(1360,1130,r'b_1^0'),(1050,1160,r'b_2^0'),(920,1270,r'b_3^0'),(865,1480,r'b_4^0'),(955,1725,r'b_5^0'),(1525,1290,r'\unsure{a_1^0}'),(1560,1570,r'a_2^0'),(1440,1845,r'a_3^0'),(1150,1900,r'a_4^0'),(2040,1240,r'\unsure{b_1^1}'),(1805,1570,r'b_2^1'),(1820,1790,r'b_3^1'),(2060,2000,r'b_4^1'),(2350,1240,r'a_1^1'),(2510,1510,r'a_2^1'),(2360,1890,r'a_3^1')]
for x,y,t in labels:f.node(x,y,'$'+t+'$')
f.node(1230,1530,'$0$','text=gray').node(2190,1570,'$1$','text=gray').node(2820,700,r'$\infty$','text=gray')
f.path('(1890,745) .. controls (1850,750) and (1850,795) .. (1890,810) .. controls (1940,810) and (1950,760) .. (1910,745) (1880,752)--(1900,738)--(1903,761)','gray,line width=.28pt')
f.path('(2170,1900)--(2180,2040) (2130,2390)--(2250,2540)','gray,line width=.28pt').dot(1010,1640,5).dot(2180,1900,5)
R['B04']=f.done()
f=Fig(.0034)
f.path('(280,310)--(600,550)--(385,790) (600,550)--(1120,510) (1370,230)--(1120,510)--(1370,720)')
for x,y,t in [(235,245,r'\alpha_s'),(365,845,r'\beta_s'),(605,650,r'\sigma_s'),(590,490,'s'),(850,480,'a'),(1120,445,'t'),(1150,645,r'\sigma_t'),(1430,220,r'\unsure{\beta_t^{*}|\beta_t}'),(1460,745,r'\alpha_t')]:f.node(x,y,'$'+t+'$')
R['B05']=f.done()+r"""
\[
\unsure{\underbrace{\alpha_s+\beta_s}_{\sigma'_s}
=\underbrace{\alpha_t^{*}+\beta_t^{*}}_{\sigma'_t}
|\underbrace{\alpha_s+\beta_s}_{\sigma'_s}
=\underbrace{\alpha'_t+\beta'_t}_{\sigma'_t}}
\]"""
b06=r"""et $=$ la \uline{donnée} d'un
\deleted{\unsure{auto|isom}}\inserted{anti-}isom des torseurs
sous $\unsure{\mathbb Z/\sigma_t|\mathbb Z/\gamma}$
$(\gamma=\sigma'_s=\sigma'_t)$
\[
\begin{array}{c@{\quad}c@{\quad}c}
\text{somme circulaire}&\simeq&\text{somme circulaire}\\
\text{de }[1,\alpha_s]\text{ et }[1,\beta_s]&&[1,\alpha_t]\text{ et }[1,\beta_t].
\end{array}
\]"""
R['B06']=r'\unsure{'+b06+r'|\deleted{'+b06+'}}'
# B07: independent drawing/crossing layer. Complete prose targets are in the overlapping B02/B03/B05/B06 readings.
f=Fig(.0031)
for s in [
'(0,430) .. controls (210,280) and (410,225) .. (650,250) .. controls (880,300) and (1040,450) .. (1100,630) .. controls (1020,825) and (850,995) .. (450,1000) .. controls (200,980) and (80,870) .. (0,780)',
'(0,485) .. controls (130,410) and (310,520) .. (300,665) .. controls (295,780) and (120,875) .. (0,850)',
'(820,520) .. controls (910,545) and (925,645) .. (850,700) .. controls (790,730) and (750,620) .. (820,520)',
'(100,430)--(790,580) (300,665)--(800,635) (260,795)--(825,685)',
'(500,1200) .. controls (480,1510) and (460,1840) .. (490,1900) .. controls (520,2170) and (700,2310) .. (885,2360)',
'(1000,1200) .. controls (1070,1550) and (960,1980) .. (920,2310)',
'(1690,1650) .. controls (1740,1850) and (1810,2160) .. (1980,2350)',
'(2190,1270) .. controls (2380,1450) and (2460,1790) .. (2400,1950) .. controls (2360,2190) and (2250,2340) .. (2150,2466)',
'(500,1670) .. controls (660,1620) and (790,1630) .. (980,1650)',
'(980,1760) .. controls (1230,1640) and (1450,1670) .. (1700,1740)',
'(1020,1850)--(1660,1900)',
'(1730,1880) .. controls (1960,1780) and (2220,1790) .. (2390,1880)',
'(820,820)--(500,1200) (850,700)--(1000,1200)']:
 f.path(s,'gray!70,line width=.3pt')
# Five-sided dark graph and its unequal rays.
f.path('(1605,860)--(1875,975)--(1805,1130)--(1580,1202)--(1440,1069)--(1605,860)','black,line width=.6pt')
f.path('(1605,860)--(1557,775) (1875,975)--(2110,895) (1805,1130)--(1900,1255) (1580,1202)--(1585,1380) (1440,1069)--(1115,1165)','black,line width=.6pt')
f.dot(1805,1130,13)
f.path('(1865,970) .. controls (1850,950) and (1890,945) .. (1890,970) .. controls (1890,990) and (1865,987) .. (1865,970)')
f.path('(1640,1330) .. controls (1670,1350) and (1690,1400) .. (1680,1440)')
# Distinct crossing/framing runs; whether they cancel all the prose is not settled.
f.path('(750,1280)--(1410,560)','gray,line width=.8pt')
f.path('(1000,1830)--(2030,815)','black,line width=.75pt')
f.path('(2530,480)--(1870,1830)','black,line width=.5pt')
f.path('(1900,500)--(2160,1360)','black,line width=.42pt')
f.path('(200,1200) .. controls (240,1470) and (250,1740) .. (320,1790) .. controls (350,1850) and (410,1850) .. (450,1850) --(1790,1830)','black,line width=.55pt')
f.path('(0,400)--(2160,370)','black,line width=.55pt')
f.path('(570,625)--(610,1480) (1140,625)--(1270,1650)','black,line width=.35pt')
for x,y,t in [(800,1920,r'A_{0\infty}'),(1130,2000,r'A_{01}'),(1480,2025,r'A_{10}'),(1760,2040,r'A_{1\infty}'),(700,2275,r'A_{\infty0}'),(2510,1870,r'A_{\infty1}')]:f.node(x,y,'$'+t+'$','text=gray')
R['B07']=r'\unsure{'+f.done()+'}'
# B08: independent four drawn units; all visible gaps and directional runs are retained.
f=Fig(.003)
f.path('(130,740) .. controls (105,650) and (100,530) .. (120,505) .. controls (140,370) and (260,210) .. (320,180) .. controls (425,75) and (555,65) .. (610,95) .. controls (730,140) and (790,340) .. (800,470) .. controls (780,620) and (690,740) .. (640,730) .. controls (500,830) and (300,835) .. (240,810) .. controls (180,805) and (145,780) .. (130,740)')
f.path('(800,470) .. controls (775,650) and (680,755) .. (620,760) .. controls (470,835) and (290,850) .. (240,825)','black,line width=.3pt')
f.path('(135,742)--(810,180)','black,line width=.65pt')
f.path('(120,490)--(120,540)','black,line width=1.5pt').dot(195,330,13)
f.path('(300,190)--(320,170)--(338,195) (320,180)--(320,223)','black,line width=.8pt')
f.path('(416,115)--(435,90)--(448,122) (590,110)--(610,88)--(628,110)--(621,72)','black,line width=.8pt')
f.path('(767,340)--(785,305)--(799,350) (83,625)--(100,665)--(118,630)','black,line width=.9pt')
f.path('(450,780)--(323,811)--(355,825)','black,line width=.7pt')
f.path('(1270,1040) .. controls (1070,1070) and (730,1210) .. (530,1560)','black,line width=.6pt,->')
f.path('(560,1640) .. controls (900,1770) and (1260,1420) .. (1430,1125)','black,line width=.6pt,->')
f.dot(1270,1040,7).dot(560,1640,6)
f.node(1060,1910,r'$\unsure{[0,\alpha][1,\beta)|[1,\alpha][1,\beta)}$')
# Residual overtracing at the opening bracket and first numeral is drawn, not silently resolved.
f.path('(780,1800)--(810,1800)--(810,1880)--(780,1880) (782,1840)--(815,1840)','black,line width=.7pt')
f.path('(855,2360) .. controls (865,2180) and (760,2050) .. (650,2110) .. controls (450,2190) and (335,2400) .. (510,2630)','black,line width=.6pt,->')
f.path('(590,2670) .. controls (690,2735) and (805,2645) .. (865,2460)','black,line width=.6pt,->').dot(855,2360,8).dot(590,2670,6)
f.path('(1320,2460) .. controls (1190,2500) and (1040,2620) .. (975,2760)','black,line width=.6pt,->')
f.path('(1085,2600) .. controls (1160,2530) and (1210,2500) .. (1280,2505)','black,line width=.35pt,->')
f.path('(1005,2815) .. controls (1150,2870) and (1330,2680) .. (1400,2530)','black,line width=.6pt,->')
f.dot(1110,2570,10).dot(1250,2740,10).dot(1005,2815,11)
R['B08']=f.done()
R['B09']=r"""\[
\begin{aligned}
\beta+\gamma&=\alpha'&\qquad\alpha&=\frac{\beta'+\gamma'-\alpha'}{2}=\frac{\alpha'+\beta'+\gamma'}{2}-\alpha'\\
\gamma+\alpha&=\beta'&\beta&=\frac{\gamma'+\alpha'-\beta'}{2}\\
\alpha+\beta&=\gamma'&\gamma&=\frac{\alpha'+\beta'-\gamma'}{2}
\end{aligned}
\]
"""
f=Fig(.0032)
f.node(340,130,r"$\unsure{\alpha'}=$",'text=gray').node(710,130,r'$\unsure{\alpha+\beta}$','text=gray')
f.path('(430,135) .. controls (450,95) and (485,95) .. (500,145) .. controls (530,175) and (550,115) .. (560,100) (560,100)--(565,205) (580,135)--(650,135)','gray,line width=.32pt')
f.node(340,580,r"$\unsure{\alpha|\alpha'}=$",'text=gray')
f.node(750,580,r'$\unsure{(\alpha+\beta+\gamma)}$','text=gray')
f.node(1340,580,r'$\unsure{-(\beta+\gamma)}=$','text=gray')
f.path('(1010,645)--(1450,638)','gray,line width=.32pt')
f.node(1350,740,r"$\unsure{\alpha'}$",'text=gray')
f.node(750,740,r"$\unsure{\frac{\alpha'+\beta'+\gamma'}{2}}$",'text=gray')
f.path('(600,540) .. controls (590,500) and (655,475) .. (685,520) (900,530) .. controls (920,480) and (960,520) .. (955,580) (590,760)--(955,785)','gray,line width=.3pt')
R['B09']+=r'\unsure{'+f.done()+'}'
R['B10']=r"""\[
\begin{aligned}
&\unsure{2(\alpha+\beta+\gamma)-\alpha'=\beta'+\gamma'}\\
&\uline{2\alpha}+\beta+\gamma=\beta'+\gamma'\\
&\beta+\gamma=\alpha'
\end{aligned}
\]"""
# B11: labelled pencil triangle; bottom-left join remains open.
f=Fig(.003)
f.path('(1250,220)--(530,1540) (480,1610)--(2015,1600)--(1255,230)','gray,line width=.4pt')
for x,y,t in [(1250,110,'0'),(360,1660,'1'),(2160,1680,r'\infty'),(250,940,r'\gamma=4'),(2180,900,r'\beta=5'),(1250,2020,r'\alpha=3')]:f.node(x,y,'$'+t+'$')
for x,y,t in [(1020,550,'c_1'),(930,790,'c_2'),(850,980,'c_3'),(750,1170,'c_4')]:
 f.path(f'({x-23},{y-10})--({x+23},{y+16})','black,line width=.65pt').node(x-160,y,'$'+t+'$')
for x,y,t in [(1530,645,'b_5'),(1600,800,'b_4'),(1700,980,'b_3'),(1820,1220,'b_2'),(1910,1370,'b_1')]:
 f.path(f'({x-25},{y+12})--({x+25},{y-14})','black,line width=.65pt').node(x+160,y,'$'+t+'$')
for x,y,t in [(875,1610,'a_1'),(1210,1610,'a_2'),(1510,1605,'a_3')]:
 f.path(f'({x},{y-25})--({x+3},{y+30})','black,line width=.65pt').node(x,y+130,'$'+t+'$')
R['B11']=f.done()
f=Fig(.0034)
f.path('(950,220)--(325,1430) (300,1515) .. controls (850,1550) and (1260,1460) .. (1630,1495) (970,220) .. controls (1080,670) and (1440,1210) .. (1600,1410)','gray,line width=.4pt')
for x,y,t in [(960,120,'0'),(210,1530,'1'),(1740,1540,r'\infty'),(970,1340,'a_3'),(940,1560,'a_2'),(940,1710,'a_1')]:f.node(x,y,'$'+t+'$')
for x,y,t in [(300,800,'c_1'),(470,880,'c_2'),(640,930,'c_3'),(805,975,'c_4'),(1080,970,'b_5'),(1260,950,'b_4'),(1440,890,'b_3'),(1630,835,'b_2'),(1830,785,'b_1')]:f.node(x,y,'$'+t+'$')
f.dot(955,1005,7)
R['B12']=f.done()
f=Fig(.0036)
f.path('(1350,180)--(610,1020)--(1590,1260)--(1355,205)','gray,line width=.4pt')
f.dot(1350,180,7).path('(598,980)--(615,1010)','black,line width=.65pt')
for x,y,t,style in [(1360,70,r'\infty',''),(480,1060,'0','text=gray'),(1670,1320,'1',''),(170,1060,'a',''),(1900,1370,'b',''),(1080,1400,r'\unsure{A_\infty}','text=gray'),(830,475,r'\unsure{A}','text=gray'),(1700,700,r'\unsure{A_0}','text=gray')]:f.node(x,y,'$'+t+'$',style)
for x,y,t in [(1250,350,'b_1'),(1140,470,'b_2'),(1000,610,r'\unsure{b_3}'),(900,735,'b_4'),(785,840,r'\unsure{c_5|b_5}')]:
 f.path(f'({x-20},{y-10})--({x+20},{y+15})','black,line width=.7pt').node(x-130,y-45,'$'+t+'$')
for x,y,t in [(1465,580,'a_3'),(1505,810,r'\unsure{a_2|a_{20}}'),(1545,1015,r'\unsure{a_1}')]:
 f.dot(x,y,8).node(x+145,y-40,'$'+t+'$')
for x,y in [(850,1080),(980,1120),(1020,1130),(1070,1140),(1185,1170),(1220,1180),(1260,1190),(1360,1210),(1430,1230)]:
 f.path(f'({x},{y-30})--({x+2},{y+30})','black,line width=.6pt')
for x,y,t in [(825,1185,r'\unsure{c_1|a_1}'),(1050,1280,r'\unsure{c_2|a_2}'),(1235,1340,r'\unsure{c_3}'),(1435,1400,r'\unsure{c_4}')]:f.node(x,y,'$'+t+'$')
# Extra loops at the overwritten labels, with no inferred chronological deletion.
f.path('(790,475)--(815,375)--(850,525) (790,465)--(850,465)','gray,line width=.35pt')
f.path('(780,1160) .. controls (840,1120) and (865,1205) .. (800,1200) .. controls (765,1190) and (760,1165) .. (780,1160) (1005,1250) .. controls (1070,1205) and (1090,1315) .. (1020,1295)','black,line width=.6pt')
R['B13']=f.done()
R['B14']=r"""\uline{NB} $\alpha',\beta',\gamma'$ \unsure{OK si} $\alpha'+\beta'+\gamma'$ pair"""
# B15: all source-visible curve runs around three filled marks. No abstract edge count is imposed.
f=Fig(.0033)
for s in [
'(520,1370) .. controls (410,1130) and (335,900) .. (370,770) .. controls (660,335) and (1080,80) .. (1430,110) .. controls (1870,110) and (2040,485) .. (2115,880) .. controls (2170,1170) and (2000,1240) .. (1800,1330)',
'(370,770) .. controls (710,545) and (1000,750) .. (1330,855)',
'(1330,855) .. controls (1720,735) and (2020,735) .. (2100,900) .. controls (2130,1090) and (1960,1230) .. (1800,1330)',
'(1330,855) .. controls (1020,790) and (610,850) .. (300,1010) .. controls (285,1140) and (430,1280) .. (520,1370)',
'(1330,855) .. controls (1000,865) and (630,965) .. (315,1100) .. controls (350,1240) and (455,1325) .. (520,1370)',
'(1320,860) .. controls (1020,920) and (720,1070) .. (450,1280) .. controls (470,1320) and (495,1345) .. (520,1370)',
'(1280,850) .. controls (1040,905) and (740,1040) .. (565,1200)',
'(1330,855) .. controls (1610,845) and (1920,910) .. (2050,1030)',
'(1330,860) .. controls (1580,950) and (1800,1050) .. (1960,1160) .. controls (1920,1250) and (1855,1290) .. (1800,1330)',
'(1370,875) .. controls (1630,1010) and (1730,1165) .. (1810,1290)',
'(520,1370) .. controls (760,1100) and (1260,1070) .. (1690,1250)',
'(520,1370) .. controls (850,1260) and (1450,1250) .. (1800,1330)',
'(520,1370) .. controls (920,1450) and (1460,1445) .. (1800,1330)',
'(520,1370) .. controls (880,1530) and (1460,1600) .. (1800,1330)',
'(520,1370) .. controls (860,1690) and (1420,1710) .. (1760,1435)',
'(300,1350) .. controls (270,1620) and (420,1850) .. (540,1940) .. controls (840,2190) and (1340,2180) .. (1750,2070) .. controls (2010,1880) and (2110,1520) .. (2100,1150)',
'(320,1470) .. controls (290,1700) and (410,1810) .. (620,1880) .. controls (850,1990) and (1100,1980) .. (1320,1970)',
'(530,1940) .. controls (1000,2130) and (1440,2180) .. (1810,1985)',
'(1800,1330) .. controls (1870,1510) and (2000,1635) .. (2050,1550) .. controls (2080,1480) and (2040,1390) .. (2000,1360)',
'(1800,1330) .. controls (1930,1350) and (2000,1370) .. (2050,1290)',
'(1990,340) .. controls (2050,560) and (2060,710) .. (2040,880)',
'(1960,1520)--(1870,1770)']:
 f.path(s,'gray!75,line width=.4pt')
# Darker retracing, limited to observed segments.
f.path('(1330,855) .. controls (1570,930) and (1820,1040) .. (1960,1160)','black,line width=.45pt')
f.path('(520,1370) .. controls (850,1510) and (1490,1590) .. (1800,1330)','black,line width=.45pt')
f.path('(540,1940) .. controls (1000,2140) and (1430,2180) .. (1810,1985)','black,line width=.45pt')
f.path('(1800,1330) .. controls (1880,1520) and (2000,1635) .. (2050,1550)','black,line width=.45pt')
# Irregular, broken local outlines and direction marks.
f.path('(1240,840) .. controls (1240,805) and (1260,780) .. (1285,770) (1308,754)--(1334,743) (1375,742)--(1400,748) (1425,764) .. controls (1450,785) and (1455,800) .. (1455,813) (1455,840) .. controls (1455,910) and (1420,935) .. (1350,925) (1285,905)--(1258,880)','black,line width=.8pt')
f.path('(1250,775) .. controls (1170,860) and (1180,970) .. (1300,1000) .. controls (1390,1020) and (1480,950) .. (1495,870)','gray,line width=.3pt')
f.path('(440,1335)--(461,1315) (420,1380)--(436,1367) (430,1410)--(467,1440) (520,1465)--(559,1465) (575,1440) .. controls (625,1385) and (625,1300) .. (581,1270) --(588,1252) --(606,1275) (505,1285) .. controls (520,1270) and (550,1280) .. (560,1290)','black,line width=.85pt')
f.path('(1690,1260) .. controls (1680,1295) and (1680,1335) .. (1690,1365) (1700,1420)--(1725,1440)--(1738,1425) (1740,1220) .. controls (1800,1170) and (1840,1170) .. (1880,1190) .. controls (1950,1225) and (1970,1300) .. (1970,1330) (1970,1330)--(1955,1300)--(1988,1317) (1970,1330) .. controls (1980,1390) and (1940,1450) .. (1900,1465)','black,line width=.85pt')
for x,y in [(1330,855),(520,1370),(1800,1330)]:f.dot(x,y,25)
f.node(1510,710,r'$\infty$').node(500,1560,'$0$').node(1805,1450,'$1$')
R['B15']=r'\unsure{'+f.done()+'}'
# B16 keeps the two separate vertical rules, raised annotation, deletion and grouping brace.
f=Fig(.003)
f.node(660,190,'trois sommets')
f.node(2550,180,r'\unsure{sommets|sommet} d\textquotesingle ordre $\alpha\textquotesingle,\beta\textquotesingle,\gamma\textquotesingle$')
f.node(750,405,r'$\alpha+\beta+\gamma$ arêtes')
f.path('(1585,85)--(1590,445)','black,line width=.7pt')
f.node(500,630,r'\deleted{$\alpha+\beta+\gamma$}')
f.node(750,830,r'$(\alpha-1)+(\beta-1)+(\gamma-1)$')
f.node(1920,830,'faces-bigones')
f.node(1020,1030,'$2$ faces-triangles')
f.node(1800,625,r'\inserted{$\unsure{=\alpha+\beta+\gamma-2|=\alpha+\beta+\gamma-3}$}')
f.path('(1390,890) .. controls (1340,840) and (1400,750) .. (1520,720) .. controls (1700,770) and (1940,690) .. (2220,680) --(2230,650)','black,line width=.6pt')
f.path('(80,730) .. controls (105,790) and (100,830) .. (76,850) .. controls (42,850) and (28,840) .. (25,830) .. controls (65,850) and (85,880) .. (80,930) .. controls (75,985) and (75,1025) .. (125,1040)','black,line width=.6pt')
f.path('(2510,610)--(2525,1100)','black,line width=.7pt')
f.node(2980,855,r'$\alpha+\beta+\gamma-1$ faces')
R['B16']=f.done()
R['B17']=r'\margin{66}'
# No unobserved connective is silently supplied between the third and fourth prose lines.
R['B03']=R['B03'].replace("d'une pondération",'pondération')
expected=[f'B{i:02}' for i in range(1,18)]
assert list(R)==expected
out=root/'result/second'/f'{page}_second.tsv'
if out.exists():
 raise RuntimeError('Refusing to overwrite an existing independent TSV')
with out.open('w',encoding='utf-8',newline='') as h:
 w=csv.writer(h,delimiter='\t',lineterminator='\n');w.writerow(['box','reading'])
 for box in expected:w.writerow([box,R[box]])
# Structural checks only: no TeX compiler or textual comparison.
rows=list(csv.DictReader(out.open(encoding='utf-8',newline=''),delimiter='\t'))
assert [r['box'] for r in rows]==expected
assert all(r['reading']==R[r['box']] for r in rows)
for box,txt in R.items():
 depth=0
 for i,ch in enumerate(txt):
  if ch in '{}':
   back=0;j=i-1
   while j>=0 and txt[j]=='\\':back+=1;j-=1
   if back%2:continue
   depth+=1 if ch=='{' else -1
   assert depth>=0,(box,'negative brace balance')
 assert depth==0,(box,'brace balance',depth)
 assert txt.count('$')%2==0,(box,'math-dollar balance')
 assert txt.count(r'\begin{tikzpicture}')==txt.count(r'\end{tikzpicture}')
sha=hashlib.sha256(out.read_bytes()).hexdigest()
(root/'result/second'/f'{page}_second.sha256').write_text(sha+'  '+out.name+'\n')
# Update only this reader's second-generation visibility ledgers.
manifest_path=root/'result/second'/f'{page}_second_crop_manifest.json'
m=json.loads(manifest_path.read_text())
for c in m['crops']:
 c['viewed']=True
 c['view_method']='canonical PNG'
 if c['box']=='B04':c['view_method']='verified pixel-identical lossless WebP transport'
 if c['box']=='B07':c['view_method']='two overlapping pixel-exact canonical PNG tiles; full canonical field covered'
m['complete_independent_reading_frozen_sha256']=sha
manifest_path.write_text(json.dumps(m,ensure_ascii=False,indent=2)+'\n')
for suffix in ['dense_tile_manifest','helper_manifest','final_helper_manifest']:
 fpath=root/'result/second'/f'{page}_second_{suffix}.json'
 entries=json.loads(fpath.read_text())
 for e in entries:e['viewed']=True
 fpath.write_text(json.dumps(entries,ensure_ascii=False,indent=2)+'\n')
notes={
 'page':page,'reader':'reader_c','phase':'blind independent second reading',
 'allowed_inputs_only':True,'comparison_seen':False,'first_reading_seen':False,
 'source':'source/SP83_C13_148+149_scans/148_scan067.jpg',
 'original_directly_viewed_once':True,'box_count':17,
 'canonical_crop_paths':[f'result/crops/{page}_second_{b}.png' for b in expected],
 'source_only_helpers':16,'B07_full_field_tile_coverage':[[0,0,2723,1320],[0,1200,2723,2466]],
 'transport':{'B04':'Pixel-identical lossless WebP directly viewed.','B07':'Canonical PNG and WebP could not be delivered within image transport cap; both pixel-exact overlapping PNG tiles directly viewed and jointly cover the full image.','B12':'An earlier tool output was truncated without delivering the image. The subsequent isolated canonical view succeeded.'},
 'scope':{
  'B01':'Complete prose, raised insertion and arrow. Tiny faint residual strokes between the comma and i≠j≠k are drawn without identification; no ellipsis is supplied. The π argument is j by its descender. Clipped label from the following drawing is context.',
  'B02':'Complete heading and insertion; orientée/orienté and the final globulisé remain open. Bottom edge clips the following paragraph, read in B03.',
  'B03':'First line is certainly horizontally struck. The larger crossing/framing lines do not establish the cancellation state of every later line; live/deleted whole-body alternatives are retained. Old phrase after arêtes remains one unreadable word; tiny raised marqué and polygones are tentative. No d\u2019une is supplied between muni and pondération. Lower edge clips following diagram, read in B05.',
  'B04':'All labelled outer and inner boundaries and connecting arcs reproduced. Numeric superscripts 0 and 1 and infinity kept distinct. Preliminary gray traces, red directions, isolated loop and two disconnected fragments retained. Some overwriting of a1^0 and b1^1 remains doubtful. Neighboring clipped prose is context.',
  'B05':'Full local tripod and complete equality, including underbrace labels. Superscript stars versus primes remain uncertain. Larger crossing strokes are in B07.',
  'B06':'Full torsor wording and interval comparison. Anti- insertion, cancelled older prefix, underlined donnée and doubtful quotient retained. Relation read as ≃; the long crossing diagonal is independently drawn in B07, not treated as part of that sign. Larger cancellation scope remains uncertain.',
  'B07':'Entire prescribed field covered by two lossless tiles. This entry records drawing/crossing geometry and six pale A labels. Its overlapping prose is independently recorded in the complete B02/B03/B05/B06 units; clipped left prose starts are not reconstructed in B07. Gray contours meet the left and lower crop boundaries and are left open. Curves and joins under the prose remain doubtful rather than being replaced by a regular graph.',
  'B08':'All four drawings, their gaps, endpoints/dots and direction marks are reproduced. Whole interval caption is uncertain, including overwritten opening numeral/bracket; final parenthesis is preserved. First helper clipped its right end, which was subsequently viewed in full helper and was already included in canonical crop.',
  'B09':'Main black equations fully read. Faint overprinted calculations cannot be securely segmented throughout; readable pale spans and residual loops are recorded as a doubtful separate layer, without asserting a completed algebraic calculation. Top/bottom neighboring drawing fragments are context.',
  'B10':'All three pale equations. Whole first formula remains uncertain; underline beneath 2α retained. Clipped black symbols from adjacent units excluded.',
  'B11':'Full triangle, three vertex labels, all 12 indexed side labels, 4/5/3 counts and ticks. Small bottom-left gap remains open.',
  'B12':'Full triangle and horizontal c1...c4, dot, b5...b1 sequence. Vertices 0,1,infinity and a3/a2/a1 on and below the base retained. Neighboring a at upper-right is context.',
  'B13':'Full triangle and all ticks, including closely spaced base runs. Several labels are overwritten; c5 versus b5 and base c/a alternatives remain open. Pale A-like labels behind the dark writing are tentatively drawn/read rather than erased. Vertex 0 is pale; outside a,b retained. Upper fragment of a preceding fraction is context.',
  'B14':'Full NB line. The middle compact two-word group reads tentatively OK si (an O loop followed by K-like branches and si), not securely a set-membership formula. Last pair is read literally.',
  'B15':'All three filled marks, labels 0,1,infinity, broken local loops, directions, faint contour runs and darker retracing reproduced. Several runs merge under overtracing, so no abstract number of edges or forced join is asserted. Bottom prose belongs B16.',
  'B16':'Complete lower captions and counts, the deleted sum, raised equality, left grouping brace and both vertical separators are preserved. The raised final digit looks 2 but 3 remains plausible; no arithmetical correction is made. Right caption sommets/sommet remains open. Adjacent black page perforations are not ink.',
  'B17':'Folio 66 is complete. Attribution: unnamed hand (folio annotation; attribution uncertain).'
 },
 'no_ocr':True,'no_web':True,'no_tex_compilation':True,
 'verification':'TSV roundtrip, exact box order, brace/dollar/environment balance only.',
 'frozen_sha256':sha,'frozen_before_any_comparison':True,
 'diagram_method':'Manually transcribed source-visible paths in TikZ. Coordinates approximate the visible geometry; gray layers and uncertain joins are explicitly preserved rather than inferred from topology.'
}
(root/'result/second'/f'{page}_second_notes.json').write_text(json.dumps(notes,ensure_ascii=False,indent=2)+'\n')
os.chmod(out,0o444)
print(json.dumps({'rows':len(rows),'sha256':sha,'path':str(out),'bytes':out.stat().st_size,'canonical_crops':17,'source_only_helpers':16,'B07_tiles':2},indent=2))
