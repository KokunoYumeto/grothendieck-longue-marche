from pathlib import Path
from tikz import *
root=Path(__file__).resolve().parents[1]
s=r'''\scanpage{135}
en somme, la donnée de $(D,\bar\omega,\omega)$ revient à celle du fuseau accompagné, avec une \unsure{épingle} de ce fuseau i.e. du bigone qu'il définit.
De ce point de vue, $\sigma_2$ est l'opération qui fixe \deleted{\unsure{le}} l'élém. de structure \inserted{d'un repère} de dim $1$ (\unsure{le mur}), et pas celui de dim $0$. Pour $\sigma_0$, serait-ce l'inverse ?

\uline{Non}, cette opération inverse, \deleted{\unsure{i.e.}} \unsure{ou donc} que je note $\sigma$ dans les repères de $\widetilde X$, est celle qui remplace un repère par son symétrique p.r. au \deleted{\unsure{l'}}\inserted{sommet} origine, qui commute bien à $\sigma_2$,
'''
s+=r'''\diagram{\[\begin{tikzcd}[column sep=small,row sep=small]
\sigma\arrow[r,dash]\arrow[dr,dash]&\sigma_2\arrow[r,dash]&\sigma_0\\
&\sigma_1&
\end{tikzcd}\]}
On a les quatre \unsure{disponibles|dispositions}
\diagram{\[\begin{tikzcd}[column sep=small,row sep=small]
\text{fuseaux locaux}\arrow[dr,dash]&\text{fuseaux globaux}\arrow[r,leftrightarrow]\arrow[dr,dash]&\text{\unsure{ds}}\\
\sigma_1,&\sigma,&\sigma_2,&\sigma_0
\end{tikzcd}\]}
sur les repères, dont deux consécutifs commutent. On vient d'interpréter $\sigma,\sigma_2$ comme opérations sur les fuseaux, il resterait à interpréter $\sigma_1$ et $\sigma_0$.

Pour $\sigma_1$, on trouve que les élémts de $\widetilde X^{\swarrow\!\searrow}/\sigma_1$, i.e. les secteurs angulaires de $\widetilde X$, correspondent aux figures formées par une p.r. stable (noire).
'''
s+=start()
s+=paths('g','14.87,3.14 17.08,3.25 19.21,3.09 21.6,2.79')
s+=paths('g,dashed','14.92,3.12 15.88,2.65 17.59,2.64 19.52,2.43 20.78,2.8 21.61,2.78;15.6,3.51 16.39,3.3 17.38,2.86')
s+=paths('r','15.79,2.21 16.43,3.54 17.03,4.52;17.12,2.16 16.49,3.24 15.89,3.92;17.84,2.16 17.76,3.22 17.62,3.68;18.17,2.14 18.14,3.08 18.03,3.61;18.99,2.04 19.33,2.8 19.67,3.83;19.28,2.03 18.94,2.87 18.55,3.7')
s+=paths('w','16.25,2.01 15.83,2.91 15.4,3.73 16.23,2.89 17.3,1.97 16.78,3.34 16.23,3.97;16.54,3.57 17.45,2.5 18.16,2.12 17.89,2.99 17.49,3.48 18.43,2.62 19.26,2.09 18.91,2.94 18.62,3.37 19.63,2.62 20.55,2.34 20.01,3.25 21.28,2.91 21.42,3.14 22.1,3.09')
s+=path('k,->','20.8,3.18 21.67,3.14',False)
s+=path('k,->','16.47,2.98 16.32,2.9 16.08,3.03')
s+=dots('black','16.31,3.32 19.16,2.54',r='.07')
s+=labels([('16.3,2.73',r'\unsure{\bar\omega}'),('17.2,2.91',r'\unsure{\omega}')])
s+=paths('k,line width=2.5pt','14.94,5.91 16.38,5.92;21.11,6.08 22.98,6.09',False)
s+=paths('g,dashed','16.37,5.91 17.0,5.57 17.76,5.44 19.91,5.58 21.11,6.08')
s+=paths('blue!35!green!70!black,line width=1.8pt,dashed','16.37,5.91 17.07,6.37 17.85,6.5 19.79,6.48 21.11,6.08')
s+=paths('w,dashed','16.53,5.94 21.07,6.1',False)
s+=paths('r','17.47,4.72 17.75,5.96 17.95,7.49;18.6,4.54 18.16,5.96 17.29,7.58;18.88,5.04 18.72,7.04;19.22,4.96 19.06,7.03;19.67,4.5 19.98,5.9 20.47,8.13;20.21,4.32 19.88,5.57 19.25,7.49')
s+=dots('black','17.85,6.49 19.92,5.57',r='.1')
s+=path('k,->','17.63,6.2 17.25,6.48 17.15,6.82 17.28,7.08')
s+=path('k,->','20.33,5.72 20.53,5.44 20.43,5.14 19.94,4.97')
s+=paths('k,->','18.0,6.7 18.57,6.67;19.69,5.37 19.33,5.36',False)
s+=labels([('17.54,6.7','a'),('20.21,5.44','b'),('18.32,6.95',r'\omega_a'),('19.5,5.14',r'\omega_b')])
s+=end()
s+=r'''et deux triangles fermés ``\uline{anticonsécutifs}'', donnant naissance à \uline{deux} p.r. quasi-stables, chacune avec une orientation \deleted{\unsure{de D}} \uline{et} orientation \deleted{\unsure{de}} \inserted{de} $X$ en le sommet ($a$ ou $b$), \unsure{les deux étant identifiés} par une orientation du bigone Vert ; Sur \deleted{C'est} les fuseaux locaux, l'op. de $\sigma_1$ est la symétrie centrale, \deleted{celle de $\sigma_2$} Il faudrait comprendre aussi les éléments de $\widetilde X^{\swarrow\!\searrow}/(\sigma_1,\sigma)$, qui sont figurés en dessin en $\{D_{1/2},D_{2/3},D_{5/6},D_{6/7}$
'''
s+=start()
s+=paths('r','16.49,15.78 16.86,17.34 17.43,18.98;17.42,15.65 16.85,17.26 16.31,18.6;19.56,15.78 19.9,17.21 20.24,18.72;20.61,15.68 19.91,17.19 19.05,19.0')
s+=paths('w,line width=2.6pt','15.64,17.4 16.86,17.25 19.88,17.17 22.95,17.35')
s+=paths('w,dashed','15.91,16.72 16.84,16.76 18.43,16.79 19.87,16.76 22.49,16.72;15.54,16.97 16.44,17.02 16.86,17.25 17.79,17.8 18.94,17.8 19.91,17.17 21.72,17.84;15.45,17.63 16.26,17.52 16.86,17.25 17.68,16.85 18.37,16.82 19.91,17.17 21.69,17.88;16.06,17.76 17.07,17.83 18.35,17.87 19.94,17.47 21.09,17.45')
s+=paths('p,line width=.8pt','16.82,15.93 16.59,16.96 16.3,18.8;18.17,16.02 18.83,15.78 21.57,15.75;20.04,17.0 21.66,17.95 21.78,19.1')
s+=paths('k','16.96,15.77 16.16,16.98 15.54,18.1 17.49,15.87 16.17,18.18 18.65,15.89 17.71,17.76 19.99,16.05 19.21,17.74 21.45,16.2 20.23,17.7 23.61,16.49 22.7,17.6 25.17,16.93 24.2,17.85 26.35,17.68 26.78,17.89')
s+=dots('black','16.86,17.25 19.91,17.17',r='.09')
s+=labels([('15.51,17.67','1'),('20.2,17.01','b'),('18.38,17.36',r'\text{arête}'),('18.32,17.72',r'\text{de }D'),('24.69,17.39',r'\text{p.r. critique }D'),('23.54,18.04',r'\text{avec}')])
s+=end()
s+=r'''\margin{134}
\margin{\unsure{fus} $\leftarrow$ \unsure{fus}\par
sommets $\longleftrightarrow$ droites\par
arêtes $\longleftrightarrow$ bisect. ang. locaux}
'''
(root/'pages/MPL_154_127-176_154_scan135.tex').write_text(s,encoding='utf-8')
