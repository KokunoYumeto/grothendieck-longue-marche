from save_page import save
text=r'''\scanpage{25}
\mspage{6}
% archive foliation: 24

\diagram{\begin{tikzcd}
X'\arrow[r,dash,"s"]&X\arrow[r,shift left,"f"]\arrow[r,shift right,"g"']&Y
\end{tikzcd}}
de $\overline{\widehat A}$ avec $s\in\overline{\underline W}_A$, peut s'insérer dans
\diagram{\begin{tikzcd}
X\arrow[r,shift left,"f"]\arrow[r,shift right,"g"']&Y\arrow[r,dash,"t"]&Y'
\end{tikzcd}}
avec $t\in\overline{\underline W}_A$.
\margin{OPS $s$ mono}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\deleted{\unsure{X'}}&I\times X\arrow[r,dashed]&Y'\\
I\times X'\arrow[ur,"{\in\underline W_A}"]\arrow[r,hook,"{[\in\underline W_A]}"']
&M\arrow[u,"{[\in\underline W_A]}"]\arrow[r]&Y\arrow[u,dashed,"t"']\\
X'\amalg X'\arrow[u,leftrightarrow]\arrow[r,hook,"{\in\underline W_A}"]
&X\amalg X\arrow[u]\arrow[ur]&
\end{tikzcd}}

On a utilisé les choses suivantes :
\deleted{de $(I_\alpha)_\alpha$, famille d'\unsure{intervalles}}
$\exists$ un ens. de flèches $\unsure{\mathcal M}\subset\mathrm{Fl}(\underline M)$
(ici $M=\widehat A$) avec

(i) toute $f:Y\longrightarrow X$ se factorise en
\diagram{\begin{tikzcd}
Y\arrow[r,"i"]&X_1\arrow[r,dash,"h"]&X
\end{tikzcd}}, avec $i\in\unsure{\mathcal M}$, $h$ homotopisme
\deleted{pour $(I_\alpha)$}

(ii) Si \deleted{$\unsure{g}\!:\!Y$}
\diagram{\begin{tikzcd}
Y\arrow[r,"i"]\arrow[d,"{\deleted{\unsure{g}}\,f}"']&X\arrow[d,dash,"g"]\\
Y'\arrow[r,dash]&X'
\end{tikzcd}}
cocartésien, avec $i,f\in\unsure{\mathcal M}$, et $f\in\underline W$, alors $g\in W$.

(iii) $\exists$ familles génératrices d'intervalles les $I_\alpha$, telles que pour
$\forall X$, $X\amalg X\longrightarrow X\times I_\alpha$ soit $\in\unsure{\mathcal M}$.
\margin{Ce sont donc des intervalles séparants}

(\unsure{iv|0}) $\varinjlim$ finies existent dans $\underline M$, et \deleted{les}
\deleted{sommes \inserted{\uline{directes}} \unsure{dans} $\in\unsure{W}$},
$f,g\in W\ \Longrightarrow\ f\amalg g\in W$.

\margin{L'énoncé des conditions (i) à (iv) \unsure{s'inspire du cas de}
$(\mathrm{Cat})$ et non celui de $\widehat A$, où (iii) est inutile,
pourvu que dans (ii) il suffise \unsure{d'imposer} $i$ (ou $f$) $\in\underline W$.}

\margin{Dans tout $(M,W)$ \unsure{pourvu d'une} \deleted{\unsure{structure}}
$h$ (compatible à $W$ [car les homotopismes sont dans $W$])
$W^{-1}M=\overline W^{-1}\overline M$, et $\overline W$ admet un calcul de fractions
à gauche, moyennant les conditions (i) à (iv) :}
\margin{\deleted{\unsure{modifier pour les cas généraux}}}

\margin{\unsure{Giordano Br}}
'''
e=[('diagram','top','X prime s X parallel f g Y'),('text','upper','de A hat bar avec s in W A bar'),('display','upper','s in W A bar'),('diagram','upper middle','X parallel f g Y t Y prime'),('text','upper middle','avec t in W A bar'),('margin note','upper right','OPS s mono'),('diagram','middle large','cylinder I times X prime M Y and X primes coproducts'),('deletion','middle diagram upper left','X prime'),('text','lower middle','On a utilisé les choses suivantes'),('deletion','lower middle right','de I alpha alpha famille d intervalles'),('text','lower middle','exists un ens. de flèches'),('display','lower middle','script M subset Fl underline M; ici M A hat'),('text','lower i','toute f Y to X se factorise'),('diagram','lower i','Y i X1 h X'),('display','lower i','i in script M h homotopisme'),('deletion','lower i','pour I alpha'),('text','lower ii','Si cocartésien avec'),('deletion','lower ii before square','g Y'),('diagram','lower ii','Y i X f g Y prime X prime'),('deletion','lower ii left arrow','g'),('display','lower ii','i f in script M and f in W implies g in W'),('text','lower iii','exists familles génératrices d intervalles'),('display','lower iii','X coproduct X to X times I alpha in script M'),('margin note','lower left','Ce sont donc des intervalles séparants'),('text','bottom iv','direct limits finies existent dans M'),('deletion','bottom iv','les'),('deletion','bottom iv','sommes dans in W'),('insertion','bottom iv','directes underlined'),('display','bottom right','f g in W implies f coproduct g in W'),('margin note','right diagonal','L énoncé des conditions i à iv'),('margin note','left diagonal','Dans tout M W pourvu d une h'),('deletion','left diagonal','structure'),('display','left diagonal','W inverse M equals W bar inverse M bar'),('text','left diagonal','W bar admet un calcul de fractions à gauche'),('margin note','lower left diagonal','modifier pour les cas généraux'),('deletion','lower left diagonal','modifier pour les cas généraux'),('margin note','bottom inverted pencil','Giordano Br')]
save(25,text,'text',e,'Continues the calculus of fractions cancellation step. Large cylinder/coproduct comparison diagram, then axioms (i)-(iv) for a morphism class in M; margins compare Cat and presheaves and discuss changing (ii)/(iii). Dense margin conditions and overwritten class symbol are marked doubtful. Pencil name-like Giordano Br at inverted lower edge, not silently omitted.')
