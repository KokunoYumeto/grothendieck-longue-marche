from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{160}
\deleted{
\uline{1.1.84}

Compléments et rectifications sur les facettes exceptionnelles de $(\unsure{X|\mathcal X},K)$

a) Avec les notations de \unsure{i)}, on a
\[
\varphi^{-1}(\unsure{X_1^a|X_1^0})=L\cup K_0\qquad(\text{et non }=L\,!)
\]

b) La structure d'une facette exceptionnelle au voisinage d'une arête exceptionnelle (ou mieux, de la \inserted{double} paire de facettes rattachées à un sommet exceptionnel $a$) est de la forme suivante :
'''
s+=start()
s+=paths('g,line width=2.6pt','2.98,11.4 3.07,14.85;5.98,11.03 6.01,14.82;8.5,11.2 8.59,14.8')
s+=paths('red!70!brown,line width=2.5pt','3.0,11.85 3.55,11.59 4.7,11.56 5.81,11.67 5.98,11.83 5.46,12.0 4.25,12.03 3.0,11.85;3.0,11.85 3.53,12.22 4.62,12.29 5.43,12.18 5.98,11.83;3.08,14.16 3.88,13.9 4.95,13.86 5.96,14.1 5.39,14.45 4.12,14.49 3.08,14.16;3.08,14.16 4.5,14.17 5.96,14.1;5.98,11.83 6.84,12.02 7.66,11.99 8.5,11.7;6.01,14.16 6.75,13.93 7.58,13.93 8.59,14.14;3.8,12.23 3.87,13.97;4.98,12.19 5.0,13.88;5.47,12.11 5.27,12.88 5.35,13.49 5.51,13.98;6.76,11.94 6.78,14.02;8.0,11.84 8.01,14.12')
s+=paths('red!70!brown,line width=2.2pt','3.33,12.16 3.53,12.53 3.36,13.11 3.26,13.65 3.51,13.93 3.67,13.7 3.51,13.19 3.36,12.69 3.33,12.16;3.42,12.21 3.22,12.65 3.33,13.12 3.59,13.58 3.51,13.95;4.49,12.15 4.62,12.55 4.49,13.02 4.41,13.58 4.53,13.87 4.69,13.55 4.6,13.13 4.41,12.66 4.49,12.15;7.39,11.9 7.54,12.43 7.37,12.98 7.24,13.49 7.5,14.02;7.4,11.95 7.23,12.45 7.39,12.98 7.51,13.45 7.39,14.05')
s+=paths('red!70!brown,densely dashed,line width=1.8pt','5.98,11.83 6.51,11.39;8.5,11.7 8.07,11.51;8.5,11.7 9.22,11.48;8.5,11.7 9.14,11.86;6.01,14.16 6.7,14.36;6.01,14.16 6.44,14.45;8.59,14.14 9.3,13.94;8.59,14.14 9.29,14.36')
s+=paths('k,dashed,thin','3.11,11.96 3.18,12.75 3.55,12.91 5.47,12.79 5.84,12.56 5.86,11.94;6.12,11.98 6.21,12.66 6.55,12.8 8.1,12.78 8.32,12.57 8.38,11.95')
s+=paths('black!70!brown,line width=3pt','3.04,13.14 5.91,12.98;6.13,13.0 8.53,12.96;8.82,12.93 9.45,12.93')+dots('black!70!brown','1.66,13.21 1.98,13.2 2.3,13.2 2.6,13.2 9.63,12.92 9.88,12.94 10.13,12.96','.07')
s+=paths('blue!60!black,line width=2pt','3.2,11.63 3.19,12.03;5.8,11.61 5.81,11.99;3.24,13.97 3.25,14.43;5.87,13.91 5.88,14.32')
s+=labels([('4.6,11.13','F'),('7.36,11.13',"F'"),('4.08,12.43',r'\delta'),('6.99,12.12',r"\delta'"),('4.65,12.17',r'\unsure{s}'),('7.62,12.04',r"\unsure{s'}"),('10.8,12.87',r'\unsure{D_i|D_1}'),('6.2,13.14',r'\unsure{a}'),('7.73,12.84',r'\unsure{t}')])+end()
s+=r'''
Choix d'une \unsure{la} ``branche principale'' \inserted{$\delta$} de $L$ dans une face exceptionnelle ($F$ ou $F'$ disons) en un sommet \deleted{multiple}\inserted{multiple $s$}; alors les branches de $L$ en $s$ distinctes de \deleted{$\unsure{\delta}$} $\delta$ sont concourantes en un m\textsuperscript{me} pt $\unsure{t}$ de $\partial F$ sur $K_0$ (et par la loi de symétrie, le m\textsuperscript{me} doit se faire avec m\textsuperscript{me} multiplicité.

(De plus, je rappelle que la loi de symétrie s'étend à la multiplicité des \unsure{pts deux sommets|pts demi-sommets} \deleted{\unsure{multiples}} \inserted{de $L$} qui se trouvent sur les deux arêtes ordinaires, incidentes à $a$.)

c) Pour les arêtes de $F$ \inserted{\unsure{non exceptionnelles en $F$}} distinctes des trois arêtes marquées, \deleted{\unsure{la}} la \deleted{bord} rive privilégiée est celle opposée à cette face. -- pour une arête \inserted{ordinaire} passant par un sommet exceptionnel (arête marquée en vert), la \deleted{arête}\inserted{rive} privilégiée est celle qui correspond à la face \unsure{instble}.

d) Pour avoir la position relative correspondant à une face exceptionnelle, il faut modifier le \unsure{ruban généralisé} \deleted{\unsure{(disons}} (dis. $A$ qui \unsure{prend} $\varphi(\partial F^*)$, où $F^*$ est déduite de $F$ par renflement \unsure{vers} les sommets critiques dans la rive \deleted{\unsure{exceptionelle}} privilégiée et opposée à $F$) en \deleted{\unsure{faisant une}}\inserted{déformant $F^*$ de} façon similaire, à partir de la modification obtenue en remplaçant ``\uuline{l'arc} \deleted{\unsure{des deux pts exceptionnels de}} \inserted{\unsure{du bord}} exceptionnel'' \deleted{de la}\inserted{de la} face envisagée (joignant les deux pts critiques principaux \deleted{sur la} face) par un ``\unsure{path}'' parallèle à l'intérieur de $F$ (cf. pointillé au stylo).
}
\margin{159}
'''
(root/'pages/MPL_154_127-176_154_scan160.tex').write_text(s)
commit(160,[('deletion','whole page','whole draft crossed by two long olive strokes'),('text','upper left','1.1.84; Compléments et rectifications'),('text','left a','Avec les notations'),('display','left a','phi inverse; L union K0; et non L'),('text','left b','La structure dune facette exceptionnelle'),('insertion','left b','double'),('drawing','left centre','F,F-prime; delta; two adjacent cylinders; Di'),('text','left lower','Choix dune branche principale'),('insertion','above left lower','delta; multiple s'),('deletion','left lower','multiple; delta'),('text','left bottom continuing right top','De plus je rappelle; loi de symétrie'),('insertion','left bottom','de L'),('deletion','left bottom','multiples'),('text','right c','Pour les arêtes de F'),('insertion','right c','non exceptionnelles en F; ordinaire; rive'),('deletion','right c','la; bord; arête'),('text','right d','Pour avoir la position relative'),('deletion','right d','disons; exceptionelle; faisant une; des deux pts; de la; sur la'),('insertion','right d','déformant F-star de; du bord; de la'),('margin note','bottom left','159')],sheet_kind='cancelled_draft',observations='Whole and halves read, then each of four enlarged text regions and left half re-read. Entire draft is crossed in olive; all live content and internal corrections retained inside deleted. The insertion in b reads double, not droite. The argument of phi inverse has an unresolved superscript/index; marked without mathematical normalization. Several right-column cancellations remain doubtful. Cylinder drawing includes dashed black interior paths, dotted red continuations, blue end marks, crossing strands and all best-read labels. Date read 1.1.84. No reused printed text.')
