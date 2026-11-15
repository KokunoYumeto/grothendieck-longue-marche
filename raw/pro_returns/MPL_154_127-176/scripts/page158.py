from pathlib import Path
import ast
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{158}
'''+start()
for style,q in [('brown!50','1.04,1.28 1.05,1.69'),('purple!40','1.36,1.31 1.4,1.7'),('yellow!85!orange','1.57,1.38 1.65,1.88'),('orange!90!red','1.83,.98 1.87,1.48'),('orange!90!red','2.07,1.27 2.13,1.84'),('red!70!brown','2.43,1.25 2.5,1.96'),('orange!80!brown','2.76,1.3 2.84,1.99'),('purple!30','3.19,1.32 3.22,2.04'),('orange!90!red','3.48,1.29 3.48,1.84'),('orange!90!red','4.43,1.09 4.39,1.68'),('yellow!70!green','4.8,1.2 4.77,1.79'),('teal!50','5.13,1.26 5.06,1.81'),('g','5.48,1.45 5.43,1.98')]:s+=path(style+',line width=3pt',q,False)
s+=end()+r'''
$X,\check X$ plans projectifs réels duaux

$T$ \deleted{\unsure{système de trois droites}} \inserted{``triangle'' \unsure{de} $X$}, $T'$ triangle dual dans $\check X$

\deleted{\unsure{étant des}}
alors les orientations de $T$ et $T'$ se correspondent, de façon que si $\omega$ et $\omega'$ sont associées, d'où des orientations des \deleted{\unsure{trois}} droites \unsure{d'équation} de $T$ et de $T'$, et de $X$ resp. $\check X$ en les sommets de $T$, resp. $T'$, alors pour un \deleted{pt} \inserted{sommet} de $X$ -- $\check X$ et la droite corresp. de $\check X$ -- $X$, les orientations se correspondent.
'''+start()
# Upper-left triangle: distinct point and side numbers; local rotational arrows.
s+=path('w','1.4,7.18 3.36,7.1 5.69,7.16 7.58,7.19')+paths('w,line width=3.5pt','2.38,8.76 3.34,7.2;3.54,6.93 4.5,5.47;4.7,5.1 5.24,4.09')
s+=paths('k','3.66,3.69 4.55,5.08;5.03,5.72 5.62,6.91;5.81,7.35 6.66,8.83')+paths('teal!50,line width=2.6pt,->','4.15,4.71 4.09,5.2 4.2,5.67;5.1,5.68 5.24,5.16 5.14,4.61')+paths('g,->,line width=3pt','3.58,6.64 3.07,6.78 2.74,7.08;3.16,7.86 3.71,7.68 4.05,7.3')+paths('orange!90!red,->,line width=3pt','6.44,7.03 6.11,6.6 5.51,6.51;5.07,7.31 5.44,7.68 5.89,7.74')
s+=paths('k,->','3.58,6.83 4.1,6.0 4.48,5.51;5.58,6.78 4.74,5.47;3.62,7.14 5.47,7.15;4.4,6.4 4.39,6.65 4.56,6.74 4.75,6.6 4.69,6.37')
s+=paths('p','3.54,7.05 4.52,5.54;3.6,7.1 4.38,6.4;3.73,7.1 4.4,6.43;3.85,7.1 4.44,6.48;3.97,7.1 4.48,6.51;4.08,7.1 4.51,6.54;4.2,7.1 4.53,6.59;4.31,7.1 4.57,6.61;4.45,7.1 4.58,6.63')
s+=dots('g','3.36,7.1','.115')+dots('orange!90!red','5.69,7.16','.1')+dots('teal!50','4.59,5.25','.12')+labels([('3.42,3.49','2'),('5.23,3.84','2'),('4.92,5.18','1'),('7.84,7.08','1'),('2.11,8.93','3'),('3.06,7.35','2'),('5.96,7.45','3'),('4.91,6.6',r'\omega')])
# Upper-right dual triangle.
s+=path('g,line width=3.7pt','14.87,4.17 15.22,4.92 16.41,7.85')+path('orange!90!red,line width=4pt','15.55,4.33 14.11,7.04 13.71,7.67')+path('teal!50,line width=2.5pt','13.18,7.05 15.1,7.0 17.18,6.87')
s+=paths('w,->','14.84,4.4 14.72,4.75 14.82,5.28;15.49,5.4 15.71,4.93 15.64,4.3')+paths('w,->,line width=3.2pt','16.73,6.82 16.47,6.46 15.96,6.4;15.56,7.13 15.85,7.45 16.18,7.56')+paths('k,->','14.23,6.59 13.75,6.62 13.39,6.89;13.87,7.56 14.33,7.42 14.69,7.07;14.24,6.52 14.23,6.7;15.28,5.51 15.3,5.07;15.36,6.96 15.84,6.95;15.31,6.18 15.11,6.25 15.07,6.45 15.25,6.54 15.4,6.4 15.24,6.17')
s+=paths('p','14.37,6.55 14.54,6.97;14.48,6.34 14.74,6.97;14.6,6.11 14.94,6.97;14.7,5.88 15.14,6.97;14.84,5.67 15.34,6.97;14.96,5.48 15.54,6.97')+dots('w','15.22,4.92 14.11,7.04','.14')+dots('g','16.05,6.98','.11')+r'\draw[k] (16.05,6.98) circle (.145);'+'\n'+labels([('14.58,4.12','2'),('15.43,4.89','1'),('17.44,6.8','1'),('14.36,7.23','2'),('16.34,7.1','3'),('13.49,7.95','3'),('15.52,6.39',r"\omega'")])
# Small orientation triangles below both principal examples.
s+=path('w,->','1.61,11.52 3.2,11.53 5.44,11.42')+path('k,->','4.32,12.45 4.29,10.56')+paths('k,->','3.24,11.52 4.18,11.48;3.5,11.15 3.42,11.02 3.04,11.04')+path('p','3.2,11.53 4.29,10.56')+paths('p','3.55,11.5 3.53,11.21;3.69,11.51 3.7,11.04;3.85,11.5 3.88,10.91;4.03,11.5 4.06,10.74')+dots('g','3.2,11.53','.08')+labels([('3.34,10.76',r'\omega'),('4.49,10.62',r'\beta'),('3.92,11.82',r'\alpha'),('6.05,11.39','1'),('3.1,11.91','2')])
s+=path('g,line width=3.4pt','8.77,9.22 9.29,10.25 10.36,12.59')+paths('p','9.29,10.25 10.42,9.15 8.88,9.55;9.12,9.94 9.83,9.44;9.04,9.75 9.68,9.41')+paths('k,->','8.92,9.5 10.23,9.03;9.09,9.94 8.73,9.18;9.55,10.27 9.59,10.11 9.43,10.0')+dots('k','9.29,10.25','.09')+labels([('8.57,9.81',r"\omega'"),('10.43,9.19',r"\beta'"),('9.83,10.03',r"\alpha'")])+end()
s+=r'''$\alpha,\beta,\omega$ associés,
mais $\alpha',\beta',\omega'$ \uline{non associés}.
'''+start()
# Isolated coloured pen strokes.
s+=paths('red!70!brown,line width=3pt','1.88,15.7 2.1,15.65;2.18,15.59 2.4,15.55')+path('orange!90!red,line width=3pt','2.55,16.17 2.65,16.44')+path('blue!60!black,line width=2.5pt','3.09,16.1 3.65,15.95')
# Lower crossed lines and a shaded pencil triangle.
s+=paths('orange!90!red,line width=4pt','1.62,19.07 3.21,19.92 6.11,21.47;1.22,21.23 3.21,19.92 5.19,18.64')+path('teal!50,line width=2.5pt','1.19,20.56 5.45,20.25')+path('teal!50,dashed,line width=2pt','1.06,19.41 5.66,19.29')+path('blue!60!black,dashed,line width=2.2pt','1.07,19.99 5.04,19.77')
s+=paths('k,->','3.24,20.29 3.2,19.12;5.27,20.29 5.48,20.24;5.46,19.3 5.65,19.26;4.78,19.8 5.06,19.75')+paths('w,->,line width=3pt','2.47,19.7 2.41,20.01 2.54,20.23;3.85,20.02 3.96,19.82 3.9,19.64')+path('p','1.54,19.96 3.19,19.13')
s+=paths('p','1.79,19.95 2.04,19.7;2.04,19.95 2.34,19.54;2.24,19.95 2.51,19.44;2.46,19.95 2.7,19.34;2.71,19.94 2.88,19.28;2.93,19.94 3.04,19.18')+labels([('3.28,18.95',r'\unsure{\gamma|\delta}'),('5.23,19.75',r'\alpha'),('4.17,20.09',r'\beta')])
# Lower-left orientation key.
s+=path('teal!50,dashed','1.3,23.38 4.43,23.35')+paths('k,->','1.53,23.57 2.57,23.55;2.9,23.12 2.9,22.44;3.2,23.83 3.4,23.65 3.38,23.28 3.19,23.08')+path('p','1.3,23.38 2.59,22.51')+paths('p','1.65,23.36 1.63,23.17;1.83,23.36 1.83,23.05;2.02,23.36 2.04,22.91;2.22,23.36 2.23,22.77;2.43,23.36 2.43,22.64')+dots('k','2.9,23.38','.07')+labels([('2.5,23.91',r'\alpha'),('3.1,22.52',r'\beta'),('3.63,23.12',r'\unsure{\gamma|\delta}')])
# Lower-centre point/line orientation key.
s+=paths('w','11.22,24.14 12.1,24.11;14.74,24.1 16.72,24.26')+path('w,line width=3pt','12.63,24.08 14.31,24.16')+paths('k,->','13.58,24.0 13.57,23.51;13.57,24.74 13.57,24.4;13.67,24.15 14.31,24.15;13.68,23.57 13.8,23.39 13.61,23.23 13.37,23.26;13.64,24.31 13.77,24.16 13.7,23.95')
s+=dots('orange!90!red','12.37,24.13 14.5,24.13','.12')+dots('blue!50!black','13.58,24.13','.13')+dots('teal!50','13.57,23.39 13.57,24.94','.1')+labels([('13.23,23.58',r"\beta'"),('14.04,24.51',r"\unsure{\gamma'}"),('14.04,24.97',r"\alpha'")])+end()
# Printed matter, read after rotation and mirroring; literal repeated banners.
s+=r'{\ttfamily\unsure{//*}\quad CRAY2\quad\unsure{0135}\quad I}'+'\n'
tree=ast.parse((root/'scripts/page144.py').read_text())
zcols=banner=None
for n in tree.body:
 if isinstance(n,ast.Assign):
  if any(isinstance(t,ast.Name) and t.id=='banner' for t in n.targets):banner=ast.literal_eval(n.value)
zcols=[list(range(11,19)),list(range(9,19)),[7,8,15,16,17,18],[6,7,13,14,16,17],[5,6,11,12,15,16],[4,5,9,10,14,15],[3,4,7,8,13,14],[2,3,5,6,12,13],[1,2,3,4,11,12],[0,1,2,10,11],list(range(10)),list(range(8))]
zero=[]
for cols in zcols:
 row=[' ']*61
 for off in [0,14,28,42]:
  for j in cols:row[off+j]='0'
 zero.append(''.join(row).rstrip())
s+=r'{\scriptsize\begin{tabular}{l}'+'\n'
for row in zero+['']+banner:s+=r'\texttt{'+row.replace(' ',r'\ ')+'}'+r'\\'+'\n'
s+=r'\end{tabular}}'+'\n'
for i in range(6):s+=r'{\ttfamily ****A END JOB 135 CRAY2 ROOM 2.28.42 PM 19 AUG 82 R6.PR1 SYS JES2 JOB 135 END A****}\\'+'\n'
s+=r'\margin{157}'+'\n'
(root/'pages/MPL_154_127-176_154_scan158.tex').write_text(s)
commit(158,[('drawing','top left','thirteen coloured pen strokes'),('text','top right','X,checkX plans projectifs réels duaux'),('deletion','top right','système de trois droites; étant des; trois; pt'),('insertion','top right','triangle de X; sommet'),('text','upper middle','alors les orientations de T et T-prime'),('drawing','upper left','triangle with coloured vertices1,2,3 and six rotational arrows'),('drawing','upper right','dual triangle with numbered sides and vertices'),('drawing','middle left','alpha,beta,omega orientation triangle'),('drawing','middle','alpha-prime,beta-prime,omega-prime orientation triangle'),('text','middle left','alpha,beta,omega associés; non associés'),('drawing','left below text','four coloured short pen strokes'),('drawing','lower left','orange crossing, dashed coloured lines and curved arrows'),('drawing','lower left','small shaded orientation triangle'),('drawing','lower centre','coloured points and straight/curved orientation arrows'),('text','printed rotated through paper','CRAY2 0135 I; four zero-character figures; CRAY2 banner'),('text','six printed rows','END JOB135 CRAY2 ROOM2.28.42PM19AUG82R6.PR1SYSJES2'),('margin note','bottom left','157')],sheet_kind='reused_typed',observations='Whole and both halves personally read; prose enlarged and reused printing rotated/mirrored for direct reading. Printed twelve-row zero and CRAY2 banners compared visually against the already entered literal pattern before reuse. Top cancelled/replaced definition has superimposed words and remains doubtful; no duality-based emendation imposed. Two lower Greek labels might be gamma or delta and are explicitly marked. Four small colour strokes and thirteen upper colour trials are retained as drawings.')
