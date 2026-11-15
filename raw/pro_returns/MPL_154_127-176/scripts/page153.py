from pathlib import Path
from tikz import *
from commit_page import commit
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{153}
{\ttfamily\unsure{//CRAY2}\quad JOB '*********',\\
// MSGLEVEL=(1,1),MSGCLASS=A\\
// EXEC PGM=IEFBR14\qquad JOB 0025}
'''
s+=start()+comment('Upper pencil lens with three directed short segments.')
s+=path('p','8.22,3.74 9.64,2.97 12.3,2.42 14.65,2.36 16.58,2.98 15.1,4.32 13.41,5.08 11.31,5.22 9.29,4.89',True,True)
s+=paths('p','8.22,3.74 10.2,3.51 14.35,3.11 16.58,2.98;8.22,3.74 9.85,4.42 11.97,4.6 13.8,4.25 15.62,3.67 16.58,2.98;9.65,2.98 9.85,4.42 10.45,5.13;10.16,2.84 10.2,3.51 10.47,5.1;9.62,3.58 10.0,3.29 10.2,3.51;12.42,2.41 12.76,3.73 13.41,5.08 13.65,5.44;13.36,2.37 13.8,4.25 14.12,4.95;13.9,2.14 14.35,3.11 15.46,5.2;14.65,2.36 15.22,3.44 16.2,5.13;9.54,5.07 10.2,3.51')
s+=paths('w,->,line width=1.8pt','9.85,4.42 10.2,3.51;13.41,5.08 13.8,4.25;14.35,3.11 14.65,2.36')
s+=dots('w','8.22,3.74 10.2,3.51 9.85,4.42 13.41,5.08 13.8,4.25 14.65,2.36 16.58,2.98','.07')+dots('w','14.35,3.11','.16')
s+=comment('Large coloured lens: orange transverse curves, green longitudinal curves and dark dashed directed routes.')
s+=path('r,line width=3pt','4.11,8.7 4.66,7.62 6.34,6.49 8.62,5.96 10.29,6.07 12.4,6.9 14.44,7.93 13.53,8.93 12.28,9.66 10.96,10.25 9.41,10.73 8.1,10.94 6.48,10.63 5.17,10.05',True,True)
for q in ['4.11,8.7 5.41,7.1 7.71,6.26 10.22,6.32 12.83,7.16 14.44,7.93','4.11,8.7 5.7,7.28 8.32,6.53 10.89,6.74 13.32,7.47 14.44,7.93','4.11,8.7 5.98,7.61 8.67,6.89 11.31,7.12 13.58,7.67 14.44,7.93','4.11,8.7 6.1,7.9 8.8,7.47 11.6,7.58 14.44,7.93','4.11,8.7 6.71,8.55 9.32,8.28 11.64,8.19 14.44,7.93','4.11,8.7 6.31,9.15 8.67,9.28 11.12,8.94 14.44,7.93','4.11,8.7 6.19,9.52 8.63,9.69 11.36,9.27 14.44,7.93','4.11,8.7 5.93,9.89 8.14,10.06 10.96,9.67 14.44,7.93','4.11,8.7 5.58,10.11 7.59,10.55 9.67,10.32 11.7,9.91 14.44,7.93','4.11,8.7 5.21,10.05 7.6,10.75 9.89,10.58 12.4,9.64 14.44,7.93']:s+=path('green!40!black,line width=.8pt',q)
s+=path('k,line width=1pt','4.11,8.7 7.22,8.54 10.14,8.32 14.44,7.93')
# These are independently entered observed orange transverse strokes.
for q in ['5.58,6.9 6.22,7.78 7.0,9.05 8.31,10.28 8.67,10.75','6.34,6.49 6.61,6.85 7.36,8.02 8.0,8.85 8.53,9.57 9.41,10.73','7.67,6.06 8.0,6.45 8.67,7.44 8.98,7.83 9.84,8.86 10.54,9.8 10.96,10.25','8.62,5.96 9.0,6.59 9.29,6.87 10.52,8.03 11.32,8.84 12.28,9.66','10.29,6.07 10.89,7.56 11.57,8.66 12.01,9.63','11.21,6.44 11.31,6.89 12.16,7.77 13.05,8.41 13.53,8.93','5.31,10.1 5.78,8.95 6.22,7.78 6.61,6.85 6.82,6.16 7.06,5.51','6.48,10.63 7.0,9.05 7.36,8.02 8.0,6.45 8.32,5.27','7.08,10.95 7.62,9.66 8.0,8.85 8.67,7.44 9.29,5.97 9.64,5.52','8.1,10.94 8.53,9.57 8.98,7.83 9.29,6.87 9.36,6.11','8.67,10.75 8.97,10.12 9.84,8.86 10.52,8.03 10.89,7.56 11.31,6.89 11.79,6.3','9.99,10.57 10.54,9.8 11.32,8.84 11.57,8.66 12.16,7.77 12.4,6.9']:s+=path('r,line width=2.3pt',q)
s+=paths('p','5.82,5.86 6.34,6.49 7.36,8.02;7.41,5.43 7.67,6.06;8.2,10.97 8.47,11.69;9.41,10.73 9.83,11.23;10.96,10.25 11.62,11.04')
for q in ['4.11,8.7 6.61,6.85 8.0,6.45 9.0,6.59 11.31,6.89 14.44,7.93','4.11,8.7 6.22,7.78 7.36,8.02 8.98,7.83 10.52,8.03 12.16,7.77 14.44,7.93','4.11,8.7 7.0,9.05 8.0,8.85 9.84,8.86 11.32,8.84 14.44,7.93','4.11,8.7 7.62,9.66 8.53,9.57 10.54,9.8 14.44,7.93','4.11,8.7 7.62,10.28 8.31,10.28 8.97,10.12 11.7,9.63 14.44,7.93','4.11,8.7 6.15,10.34 8.67,10.75 9.41,10.73 12.01,9.63 14.44,7.93']:s+=path('w,dash pattern=on 8pt off 5pt,line width=1.4pt',q)
for q in ['6.22,7.78 6.61,6.85','7.0,9.05 6.22,7.78','7.0,9.05 7.36,8.02','7.62,9.66 8.0,8.85','8.31,10.28 7.62,9.66','8.31,10.28 8.53,9.57','8.53,9.57 8.98,7.83','8.98,7.83 9.29,6.87','10.52,8.03 10.89,7.56','11.32,8.84 11.57,8.66','10.54,9.8 11.32,8.84','11.31,6.89 11.6,6.59','11.31,6.89 11.15,6.49']:s+=path('w,->,line width=1.7pt',q)
s+=dots('w','6.34,6.49 6.61,6.85 6.22,7.78 7.0,9.05 7.36,8.02 8.0,6.45 8.67,7.44 8.98,7.83 9.29,6.87 8.0,8.85 7.62,9.66 8.53,9.57 8.31,10.28 8.67,10.75 8.97,10.12 9.41,10.73 9.84,8.86 10.52,8.03 10.54,9.8 10.96,10.25 10.89,7.56 11.31,6.89 11.57,8.66 11.32,8.84 12.16,7.77 12.4,6.9','.07')
s+=comment('Lower lens bounded by D and D-prime, with zigzag inward-to-upper-rim arrows.')
s+=path('p,line width=.8pt','2.21,19.09 3.41,18.35 4.45,17.94 5.94,17.56 8.83,17.49 10.52,17.72 12.18,18.27 13.26,18.8 11.56,19.21 9.56,19.61 7.1,19.81 5.15,19.81 3.43,19.45',True,True)
s+=paths('p','3.6,16.69 3.22,17.99 3.21,19.4;4.21,17.31 4.45,17.94 5.15,19.81;6.25,16.94 5.94,17.56 5.15,19.81;5.76,17.07 5.94,17.56 7.1,19.81;8.22,16.03 8.38,16.76 8.83,17.49 9.56,19.61;8.59,16.04 8.38,16.76 7.81,19.8;9.07,16.96 8.83,17.49 8.29,19.13;10.54,17.17 10.52,17.72 9.56,19.61;10.19,17.25 10.52,17.72 10.8,19.2;10.99,17.59 11.56,19.21;12.5,17.74 12.18,18.27 11.56,19.21;2.62,18.08 3.26,17.45 3.98,17.13')
s+=paths('w,->,line width=1.4pt','5.15,19.81 4.45,17.94;5.15,19.81 5.94,17.56;7.1,19.81 5.94,17.56;7.89,19.63 8.83,17.49;9.56,19.61 8.83,17.49;9.56,19.61 10.52,17.72;11.67,19.01 12.18,18.27')
s+=dots('w','2.21,19.09 13.26,18.8','.15')+dots('w','4.45,17.94 5.94,17.56 8.83,17.49 10.52,17.72 12.18,18.27 11.56,19.21 9.56,19.61 7.1,19.81 5.15,19.81','.075')
s+=labels([('12.9,18.1','D'),('12.83,19.37',r"D'")])+end()
s+=r'''
\margin{\uline{NB} Même une fois complété par les \unsure{fuseaux} adjacents, le couple \unsure{de flèches} \unsure{demeure} \illegible{2} (car il y a une comp. connexe \unsure{libre}\ -- \unsure{bord du fuseau}).}

\unsure{types} de fuseaux :

1) couloirs : les deux rives sont \unsure{supracritiques} \inserted{(ou fuseaux \deleted{\unsure{biparalléliques}})}

\unsure{2|3}) semi-couloirs : un (et un seul) des deux rives est \unsure{supracritique}.
\inserted{(fuseaux \deleted{\unsure{paralléliques}} \unsure{unilatéraux})}
\inserted{\unsure{triviaux}}

3) fuseaux \uline{ordinaires}

\deleted{ordinaire}
Fuseau : comp. connexe $C$ déterminée par deux ps. droites $D,D'$ en $\unsure{X}$ (qui peuvent être $\unsure{\in}\Sigma$) \deleted{\unsure{telles}} que

\begin{align*}
\text{a)}\quad&\Sigma\cup\{D,D'\}=\Sigma'\quad\inserted{\text{\unsure{syst.} de ps. dr.}}\\
\text{b)}\quad& D\ne D',\ \unsure{\Rightarrow}\ \text{et }\unsure{\{s,\bar s\}}=D\cap D'
\end{align*}
\unsure{sont des sommets de} $\Sigma$

c) $C$ est un couloir de $\unsure{\Sigma'_{\sigma\ne1}}$

\unsure{d}) $D$ et $D'$ sont critiques pour $\Sigma$.

Chaque fuseau détermine une p.r. semi-stble, et on a une corresp. $1-1$ entre \inserted{(classes d'isotopie de)} fuseaux et p.r. semi-stbles. \inserted{\uline{canon.}}

\unsure{d}) signifie aussi que tt \deleted{\unsure{triangle}} \inserted{\unsure{triangle}} de contraction sur la \uline{rive libre} de $D$ ou $D'$ est accolé à un sommet, et qu'à l'intérieur du fuseau, chaque sommet sur une rive est relié à un sommet sur l'autre \inserted{(cas \unsure{I} de type I ou II)}.
Sauf dans cas triviaux, un fuseau est déterminé par les (classes d'isotopie) de ses rives.
\margin{152}
'''
(root/'pages/MPL_154_127-176_154_scan153.tex').write_text(s)
commit(153,[('text','printed vertical right margin','CRAY2 JOB; MSGLEVEL; EXEC PGM=IEFBR14; JOB 0025'),('drawing','upper centre','pencil lens with three directed short intervals'),('drawing','upper middle','large orange and green lens with dark dashed routes'),('margin note','right of coloured lens','NB Même une fois complété'),('text','middle','types de fuseaux; couloirs; semi-couloirs; ordinaires'),('insertion','beside types','fuseaux alternative names; triviaux'),('deletion','beside types and definition','alternative names; ordinaire; telles'),('drawing','lower middle','D, D-prime; lens and directed zigzag'),('text','right lower','Fuseau : comp. connexe C déterminée par deux ps. droites'),('display','right lower','a) Sigma union {D,D-prime}; b) intersections'),('text','right lower conditions c and d','C est un couloir; D et D-prime critiques'),('insertion','right lower','syst. de ps. dr.; classes d’isotopie; canon.'),('text','bottom right','Chaque fuseau détermine une p.r. semi-stble'),('text','bottom left','d) signifie aussi; rive libre; Sauf dans cas triviaux'),('insertion','bottom left','triangle; cas I de type I ou II'),('deletion','bottom left','triangle'),('margin note','bottom left','152')],sheet_kind='reused_typed',observations='Whole, both halves, enlarged marginal NB, types, conditions and bottom paragraphs visually read. The NB and several cancelled alternative names remain exceptionally uncertain despite enlargement; two unresolved NB words are marked illegible. The apparent implication-like sign in condition b and subscript in c are preserved as doubtful readings without mathematical repair. Classification agreement un (et un seul) des deux rives is retained. Printed right-margin text read after rotation. The three drawings are geometric reproductions, not schematic replacement descriptions.')
