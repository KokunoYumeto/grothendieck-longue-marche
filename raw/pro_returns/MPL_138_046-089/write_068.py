from workflow import save_page
save_page(68,r'''
\scanpage{68}
% archive foliation: 67
\deleted{
$(p,q,r)$ doit être parmi les \deleted{\unsure{trois}} syst. énumérés

a) $p,2,2$ : $\dfrac1p+\dfrac12+\dfrac12>\left(1+\left(1-\dfrac1s\right)\right)$\quad i.e. $\dfrac1p+\dfrac1s>1$ impossible car $\dfrac1p,\dfrac1s\leq\dfrac12$

b) $(p,3,2)$\quad $(p=3,4,5)$, $s\geq p$ \deleted{\unsure{\frac1p+\frac13+\frac12}}
\[
\frac1s+\frac1p+\underbrace{\frac13+\frac12}_{5/6}>2\qquad
\frac1s+\frac1p>\frac76\qquad\text{impossible car }\frac1s,\frac1p\leq\frac13
\]
}
\[
\frac1p+\frac1q>2-\underbrace{\left(\frac1r+\frac1s\right)}_{\substack{\leq1\\\text{car }\frac1r\leq\frac12\\\frac1s\leq\frac12}}\geq1
\quad\text{donc}\quad\frac1p+\frac1q\geq1\quad\text{impossible car }\frac1p,\frac1q\leq\frac12
\]
\uline{Impossible} !

Car si $\operatorname{Card}I\geq4$, on aura
\[
\frac1{d_1}+\frac1{d_2}+\frac1{d_3}+\frac1{d_4}
\deleted{\unsure{+\sum_{5\leq i\leq\nu}\frac1{d_i}}}
>2+\sum_{5\leq i\leq\nu}\left(1-\frac1{d_i}\right)
\underset{2}{\unsure{\vee|\geq}}
\]
et on vient de voir que c'est impossible !

\deleted{
\uline{Étude du cas} \deleted{$\operatorname{Card}I=2$}\inserted{$(N,N)$} : En caractéristique $0$, c'est le cas bien connu
\[
G\simeq\mu_N(k)\simeq\mathbb Z/N\mathbb Z
\]
\deleted{\unsure{Plus généralement}} \unsure{Bien}, il en est ainsi si car. $p$ premier à $N$.

Si $p\mid N$, on trouve une $p$-extension \inserted{(de degré $p^r$, tlt ramifiée et \unsure{inséparable})} d'une $N'$-extension kummérienne $(N=p^rN',\ (p,N')=1)$. C'est donc une \uline{extension} \deleted{et} \uline{résoluble}, \inserted{mais mieux :} \deleted{\unsure{On ne peut être plus précis}, \deleted{de} les $p$-\deleted{extensions} \unsure{sous-}}

\inserted{\unsure{groupes} $H$ de $\operatorname{GP}(1,k)$ sont \uline{abéliens} et contenus dans}
\deleted{\unsure{toute la théorie}. \unsure{On déduit même que l'extension est}}
\deleted{\uline{abélienne finie}}
sous-groupe unipotent de dim $1$, \inserted{conjugués entre eux, et $H$ isom : $(\mathbb Z/p\mathbb Z)^{\unsure{r|\nu}}$.} On trouve donc

$G\subset\text{Borel}$, et par suite $G$ produit $\frac12$ direct d'un groupe cyclique premier à \unsure{$p$|$2$} car., par un $(\mathbb Z/p\mathbb Z)^r$. En fait, on voit aisément (\deleted{\unsure{ici encore}} qu'on est ds le précédent cas (cyclique premier à car., donc kummérien, qui en est exclu), on \unsure{tombe} en contradiction.

\margin{En tous les cas, on a une extension abélienne, \unsure{non kummérienne|kummérienne} (d'ordre premier à $p$) \unsure{sous} \deleted{\unsure{gr.}} \unsure{gr.} $(\mathbb Z/p^r\mathbb Z)^\nu$}

\uline{Étude du cas} $(N,2,2)$, $(\#G=2N)$. En car. $\ne2$, \uline{l'indice}\inserted{\unsure{d'un pt}} de ramification $2$ est ramification modérée, et faisant une \deleted{\unsure{différence}} extension kummérienne de degré $2$, on \deleted{\unsure{tr}} trouve un $X'/Y'$ qui n'a plus que $2$ pts de ramification \deleted{\unsure{dans}} $Y'$, donc $X'/Y'$ est justiciable de l'étude précédente mais \deleted{\unsure{il faut justifier que}}\inserted{\unsure{voir pour}} si $X'$ de genre $0$ (facile)
\diagram{\begin{tikzcd}
X \arrow[d] & X' \arrow[l] \arrow[d,dash]\\
Y & Y' \arrow[l]
\end{tikzcd}}
}
''',[
('deletion','top, diagonal strokes','(p,q,r) doit être parmi les syst. énumérés; a),b) and calculations'),
('text','top cancelled block','(p,q,r) ... a) p,2,2 ... b) (p,3,2)'),
('deletion','top sentence local','trois'),
('deletion','case b local','1/p+1/3+1/2'),
('display','top case a','1/p+1/2+1/2>...; impossible'),
('display','top case b','1/s+1/p+1/3+1/2>2; >7/6; impossible'),
('display','upper middle, live','1/p+1/q>2-(1/r+1/s) greater or equal 1; impossible'),
('text','middle','Impossible! Car si Card I greater or equal 4, on aura'),
('display','middle','1/d_1+1/d_2+1/d_3+1/d_4>2+sum(1-1/d_i)'),
('deletion','middle formula','+sum 1/d_i'),
('text','middle','et on vient de voir que c’est impossible!'),
('deletion','lower half, large diagonal strokes','Étude du cas (N,N) through X prime de genre 0 (facile), including diagram'),
('text','lower half start','Étude du cas; En caractéristique 0'),
('deletion','case heading local','Card I=2'),
('insertion','above case heading','(N,N)'),
('display','lower half start','G isom mu_N(k) isom Z/NZ'),
('deletion','paragraph start','Plus généralement'),
('text','lower half','il en est ainsi si car p premier à N; Si p divides N'),
('insertion','above p-extension','de degré p^r, tlt ramifiée et inséparable'),
('text','lower half','C’est donc une extension résoluble'),
('deletion','before résoluble','et'),
('insertion','above résoluble','mais mieux:'),
('deletion','several lines in lower half','On ne peut ...; de; extensions; toute la théorie; On déduit; abélienne finie'),
('insertion','between crossed lines','groupes H de GP(1,k) sont abéliens et contenus dans'),
('text','lower half','sous-groupe unipotent de dim 1; On trouve donc; G subset Borel'),
('insertion','right, bracketed','conjugués entre eux, et H isom (Z/pZ)^r'),
('text','lower third','G produit 1/2 direct ... En fait ... contradiction'),
('deletion','within En fait sentence','ici encore'),
('margin note','left lower margin, bracket','En tous les cas, on a une extension abélienne ... (Z/p^r Z)^nu'),
('deletion','margin local','gr.'),
('text','bottom','Étude du cas (N,2,2), #G=2N; En car not equal 2'),
('insertion','above indice','d’un pt'),
('deletion','above extension kummérienne','différence'),
('deletion','near on trouve','tr'),
('deletion','near ramification Y prime','dans'),
('deletion','last line','il faut justifier que'),
('insertion','last line','voir pour'),
('diagram','lower left','X leftarrow X prime over Y leftarrow Y prime')],sheet_kind='cancelled_draft')
