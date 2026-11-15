from save_page import save
import ast
from pathlib import Path
tree=ast.parse((Path(__file__).parent/'page103.py').read_text())
rows=next(ast.literal_eval(n.value) for n in tree.body if isinstance(n,ast.Assign) and any(isinstance(t,ast.Name) and t.id=='rows' for t in n.targets))
printed=['*'*79]+[('*'+rows[0]).ljust(78)+'*']+['*'*79]+[('*'+r).ljust(78)+'*' for r in rows[1:]]+['*'*79]
rows2=['','                  - J E S N E W S   F R 1 -      LE 16/08/82','',None,'',
'  DEPUIS LE LUNDI 12 JUILLET 82, LES CLASSES DE TRAVAUX D ET E',
'  SERONT ETENDUES POUR UNE TAILLE MEMOIRE SUPERIEURE A 1024 K',
'  SE REPORTER A LA NOTE TECHNIQUE MVS141.','',None,
"  A PARTIR DU LUNDI 9 AOUT 1982 , IL SERA POSSIBLE D'IMPRIMER",
'  SUR XEROX 9700 (DESTINATION SAC) DES FICHIERS UTILISANT LE',
'  COUPLE DE JEUX DE CARACTERES : (GS15,GT15)','',None,'',
'-LE 15/08/82 :','-'*13,
"  -LE 370/168 SERA ARRETE DU VENDREDI 20 AOUT A 19H JUSQU'AU",
'   LUNDI 23 AOUT A 8H.( MISE A NIVEAU TECHNIQUE.).','']
printed2=['*'*66]+[('*'+'-'*64+'*') if r is None else ('*'+r).ljust(65)+'*' for r in rows2]+['*'*66]
fig=[r'''\scanpage{112}
\figure{\begin{tikzpicture}[x=.009cm,y=-.009cm,line cap=round,line join=round]
\draw[orange!75!brown,line width=1.2pt] (239,394)..controls(552,382)and(888,395)..(1186,400) (616,266)..controls(636,379)and(653,452)..(670,539) (664,258)--(599,516) (821,219)--(804,612) (895,238)--(999,628) (978,228)--(875,614) (943,214)--(931,681) (1113,197)--(1087,695);
\draw[yellow!60!green,line width=1.7pt] (231,353)..controls(463,344)and(581,344)..(636,389)..controls(702,446)and(845,477)..(1157,460);
\draw[yellow!60!green,line width=1.7pt] (231,436)..controls(443,439)and(593,425)..(636,389)..controls(704,340)and(962,339)..(1169,339);
\draw[->] (482,354)..controls(475,381)and(477,402)..(480,415);\draw[->] (753,420)--(752,373);
\draw (810,328)--(824,329) (809,357)--(824,358) (806,433)--(820,435) (806,482)--(820,484) (894,328)--(906,330) (900,351)--(912,353) (916,320)--(931,320) (947,315)--(961,316) (947,364)--(960,365) (922,368)--(936,368) (911,443)--(924,444) (950,444)--(961,445) (889,484)--(906,486) (930,488)--(942,489) (966,484)--(980,486);
\node at (788,321) {$\deleted{\bar a}$};\node at (843,322) {$\bar a$};\node at (845,365) {$\bar a'$};\node at (833,433) {$a$};\node at (834,485) {$a'$};
\node at (892,317) {$\bar x$};\node at (937,321) {$\bar y$};\node at (968,317) {$\bar z$};\node at (896,368) {$\bar x'$};\node at (940,376) {$\unsure{\bar y'}$};\node at (976,370) {$\bar z'$};
\node at (897,438) {$x$};\node at (937,451) {$\unsure{y}$};\node at (967,442) {$z$};\node at (884,502) {$x'$};\node at (936,511) {$y'$};\node at (985,509) {$z'$};
\end{tikzpicture}}
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[orange!75!brown,line width=1.2pt] (133,887)..controls(479,871)and(752,879)..(1036,873) (246,717)--(222,1065) (299,737)--(349,1089) (354,731)--(267,1069) (486,740)--(581,1099) (534,725)--(516,1088) (583,738)--(466,1089) (683,768)--(679,1064) (804,731)--(930,1091) (861,746)--(836,1153) (927,734)--(727,1150);
\draw[yellow!60!green,line width=1.8pt] (136,803)..controls(345,804)and(463,833)..(525,878)..controls(591,931)and(656,983)..(802,982)--(1120,962);
\draw[yellow!60!green,line width=1.8pt] (168,982)..controls(320,1012)and(453,951)..(525,878)..controls(597,832)and(812,824)..(1063,811);
\draw[->] (444,839)..controls(425,866)and(422,892)..(433,909);\draw[->] (629,927)..controls(648,908)and(649,875)..(640,848);
\node at (154,768) {$D$};\node at (1102,777) {$\bar D$};\node at (1160,958) {$D$};\node at (133,1031) {$\bar D\unsure{'|^!}$};
''']
labels=[(220,781,"u'"),(216,833,'u'),(210,967,r"\bar u'"),(209,1006,r'\bar u'),(277,779,"v'"),(277,829,'v'),(267,962,r"\bar v'"),(266,1006,r'\bar v'),(372,794,"w'"),(372,834,'w'),(366,953,r"\bar w'"),(365,1006,r'\bar w'),(486,809,r'\bar r'),(481,832,r"\bar r'"),(533,798,r'\unsure{\bar s}'),(531,836,r"\unsure{\bar s'}"),(591,800,r'\bar t'),(575,835,r"\bar t'"),(477,915,r'\unsure{r}'),(463,959,r"r'"),(529,918,r'\unsure{s}'),(525,952,r"\unsure{s'}"),(576,916,r'\bar t'),(577,959,"t'"),(710,802,r'\bar a'),(713,853,r"\bar a'"),(704,953,'a'),(709,1012,"a'"),(658,1013,r'\deleted{a}'),(801,801,r'\bar x'),(838,798,r'\bar y'),(891,790,r'\bar z'),(807,852,r"\bar x'"),(849,851,r"\bar y'"),(896,847,r"\bar z'"),(788,970,'x'),(835,975,'y'),(881,971,'z'),(778,1013,"x'"),(843,1019,"y'"),(892,1012,"z'")]
for x,y,s in labels:fig.append(f'\\node at ({x},{y}) {{$'+s+'$};')
ticks=[(238,788),(237,817),(231,969),(228,998),(300,794),(302,821),(288,969),(284,999),(338,799),(335,824),(329,991),(497,813),(503,836),(512,822),(514,840),(545,814),(539,836),(498,917),(491,941),(516,922),(514,950),(544,920),(549,945),(683,812),(682,851),(683,954),(681,991),(814,808),(826,844),(852,812),(852,840),(885,809),(875,842),(807,972),(795,997),(844,974),(841,1005),(878,973),(884,998)]
for x,y in ticks:fig.append(f'\\draw[line width=.7pt] ({x-5},{y})--({x+5},{y+1});')
fig.append(r'''\end{tikzpicture}}
\uline{NB} $x$ et $\bar x$ (comme $x'$ et $\bar x'$) \unsure{ne sont pas sur le} \unsure{même} \unsure{droite|arcs} !
\figure{\begin{tikzpicture}[x=.01cm,y=-.01cm,line cap=round,line join=round]
\draw[yellow!60!green,line width=1.6pt] (185,1552)--(696,1551);
\draw[yellow!60!green,line width=1.6pt,dash pattern=on 7pt off 5pt] (169,1526)..controls(316,1499)and(351,1394)..(461,1425)..controls(620,1468)and(774,1496)..(906,1499);
\draw[orange!75!brown,line width=1.4pt] (400,1305)--(532,1678) (459,1306)--(472,1647) (500,1327)--(406,1647);
\draw[line width=2.4pt] (450,1449)--(470,1449);
\draw[blue!70!black,line width=1.7pt] (426,1527)--(494,1528);
\draw[->] (485,1429)--(485,1453) (506,1522)--(506,1499) (311,1540)--(308,1491);
\draw[gray,line width=.4pt] (250,1370)--(279,1420) (311,1327)--(338,1403) (382,1321)--(413,1415) (528,1306)--(546,1417) (606,1333)--(614,1423) (691,1356)--(701,1464) (325,1556)--(287,1646) (379,1556)--(322,1680) (425,1555)--(366,1684) (464,1558)--(426,1691) (567,1557)--(540,1623) (647,1572)--(607,1673);
\draw[orange!75!brown,line width=1.4pt] (1133,1336)--(1190,1624) (1156,1318)--(1129,1602) (1174,1355)--(1087,1593);
\draw[yellow!60!green,line width=1.6pt] (1011,1507)..controls(1170,1506)and(1232,1503)..(1345,1494);
\draw[line width=3pt] (1115,1507)--(1167,1507);
\draw[orange!75!brown,line width=1.4pt] (1106,1648)--(1154,1926) (1128,1643)--(1116,1914) (1150,1646)--(1068,1876);
\draw[yellow!60!green,line width=1.6pt] (981,1747)--(1237,1741);
\draw[line width=2.2pt] (1111,1711)--(1132,1712);
\end{tikzpicture}}
\begin{verbatim}''')
fig.append('\n'.join(printed));fig.append('\n'.join(printed2));fig.append(r'''\end{verbatim}
\mspage{111}''')
save({'scan':112,'sheet_kind':'reused_typed','text':'\n'.join(fig),'elements':[('drawing','upper left','yellow crossing branches, red lines, barred a x y z and primed labels'),('deletion','upper drawing','barred a'),('drawing','centre left','D and barred D, labelled u v w r s t a x y z'),('deletion','centre drawing, below a','a'),('text','centre','NB x et x̄ (comme x′ et x̄′)'),('drawing','lower left','yellow solid and dashed curves, red triple crossing, blue and black intervals'),('drawing','lower centre, upper','red triple crossing with black interval on yellow line'),('drawing','lower centre, lower','red triple crossing, black interval above yellow line'),('text','right, upside down, lower large block','JESNEWS DU 09/08/1982 C68 CADARACHE'),('text','right, upside down, upper smaller block','JESNEWS FR1 LE 16/08/82'),('margin note','bottom left','111')]})
