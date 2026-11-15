import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(33,r'''\scanpage{33}

\margin{hyp. de \unsure{induction}}
3°) L'hom can
\[
\diagram{\begin{tikzcd}
\Omega_X|Y \arrow[r] & \underline{\operatorname{Hom}}(\unsure{\varphi|\rho}_{Y/X},\Omega_Y)
\end{tikzcd}}
\]
est injectif [une orientation de X en $y\in Y$ est connue quand on sait comment \inserted{au vois. de y} une rive \inserted{de Y} détermine une orientation de Y]

\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,2.6) .. controls (0,1.8) and (.1,1.2) .. (-.12,1.15) .. controls (.1,1.1) and (0,.4) .. (.15,0);
\node[left] at (-.1,1.2) {\shortstack{hyp. de non\\trivialité}};
\end{tikzpicture}}}
4°) Pour tte $\omega\in\unsure{\Gamma|\Omega}(X)$, l'hom correspondant
\[
\diagram{\begin{tikzcd}
\rho_{Y/X} \arrow[r] & \Omega_Y
\end{tikzcd}}
\]
est injectif [deux rives différentes définissent des orientations différentes de Y]

5°) Pour tout $X\in\operatorname{Ob}\mathcal V$, $\Omega(X)\to X$ est surjectif (il existe localement des orientations $\unsure{\omega|\varphi}$ de X; ou encore:
$\forall n\geq1$, $\Omega(\mathbb R^n)$ est non vide)

\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (.1,1.9) .. controls (-.1,1.4) and (-.1,.4) .. (.12,.15);
\node[left] at (0,1) {\shortstack{\inserted{principe de}\\\deleted{\unsure{hyp.}}\\\deleted{\unsure{forte}} \unsure{l'identité}}};
\end{tikzpicture}}}
6°) Pour tt $X\in\operatorname{Ob}\mathcal V$, $\Omega(X)$ interprété comme espace étalé sur X est séparé sur X, ou encore:
une orientation d'un $X\in\operatorname{Ob}\mathcal V$ est connue en un pt quand on la connaît en des pts arbitrairement voisins. (Il suffit de l'exiger pour $\mathbb R^n$, $n\geq1$, en fait, il sera vrai a posteriori qu'une orientation de $\mathbb R^n$, \inserted{ou de tt X connexe,} est connue quand on le connaît en un seul point\ldots)

\margin{32}
''','text',[
('margin note','upper left beside 3','hyp. de induction'),
('text','top','3° L’hom can; est injectif'),('diagram','top display','Omega_X|Y to Hom'),
('insertion','above explanation after comment','au vois. de y'),('insertion','above rive/détermine','de Y'),
('drawing','left spanning 4 and 5','brace'),('margin note','beside brace 4–5','hyp. de non trivialité'),
('text','upper middle','4° Pour tte omega'),('diagram','middle','rho_Y/X to Omega_Y'),
('text','middle lower','5° Pour tout X'),('display','end 5','forall n geq 1'),
('drawing','left beside 6','curved grouping stroke'),('margin note','left beside 6','principe de l’identité'),('deletion','left beside 6','hyp. forte'),('insertion','left beside 6 above deleted label','principe de'),
('text','bottom','6° Pour tt X'),('insertion','above last lines','ou de tt X connexe,'),('margin note','bottom left','32')
],[
('left margin beside 3','induction','','low','Compressed sloping word; enlarged and rotated crop still leaves middle letters uncertain.'),
('3, first arrow target','varphi_Y/X','rho_Y/X','medium','Loop and stem are more phi-like here; the next display is rho-like.'),
('4, membership expression','Gamma(X)','Omega(X)','medium','The visible left stem and top bar suggest Gamma; no regular lower Omega feet.'),
('5, after orientations','omega','varphi','low','Small isolated looped mark with descending stroke, enlarged; possibly a letter.'),
('6, marginal cancelled label','hyp. forte','','low','Heavy strike-through crosses both words; their exterior strokes remain visible.'),
('6, marginal replacement','l’identité','','medium','Initial narrow strokes overlap the cancelled label.'),
('6, last clause','le connaît','la connaît','high','The visible ending appears e, retained without grammatical correction.')
])
