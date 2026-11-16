import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{15}
\mspage{13}

\uline{Dém} a) Comme $\pi'_0\longrightarrow\pi_0$ est évidemment un isom (car $k'/k$ est \unsure{l'ext. triviale}) il suffit de prouver que $I'\simeq I$, et comme $I'_t\xrightarrow{\sim}I_t$ (car $e=1$) il suffit de prouver que $P'\simeq P$.

b) On sait que $\pi'\mathrel{\text{---}}\pi$ est surjectif, i.e pour tte ext. finie sép. $K_1/K$, $K_1\otimes_K\widehat K$ est un \uline{corps} : en effet, la clôture normale $V_1$ de $V$ dans $K_1$ est finie, donc $V_1\otimes_V\widehat V\simeq\widehat V_1$, \deleted{est} \inserted{c'est donc} un anneau de val. discrète ($V_1$ en étant un), donc $K_1\otimes_K\widehat K\simeq\widehat V_1\otimes_V\widehat K$ est un corps.

\deleted{\unsure{D'ailleurs}} \deleted{Quitte à remplacer $V,V'$ par $\widetilde V,\widetilde V'$ et à comparer leurs complétés \unsure{$\widehat{\widetilde V}\simeq\widehat{\widetilde V'}$} de ces deux anneaux, \unsure{on est ramené}}

c) On en conclut, sur les \inserted{hom de} suites exactes, que $I'\mathrel{\text{---}}I$ est surjectif, puis $P'\mathrel{\text{---}}P$ \uline{surjectif}.
Il reste à prouver que $P'\mathrel{\text{---}}P$ est injectif, et pour ceci que $\pi'\mathrel{\text{---}}\pi$ est injectif, \deleted{\unsure{On}} i.e. que toute extension séparable finie $K'_1$ de $K'=\widehat K$ provient d'une ext. sép. finie de $K$. Or ceci résulte du fait connu (``continuité des racines p. r. aux coefficients'') que deux équations séparables à coefficients dans $\widehat K$ \uline{voisins} définissent des \deleted{\unsure{corps}} $\widehat K$-algèbres isomorphes.
\margin{14}
'''
e=[('text','top','Dém a) Comme π′₀→π₀'),('text','upper-middle','b) On sait que π′—π est surjectif'),('display','middle inline','V₁ tensor Vhat ≃ Vhat₁'),('deletion','middle after Vhat₁','est'),('insertion','middle above est','c’est donc'),('display','middle inline','K₁ tensor Khat ≃ Vhat₁ tensor Khat'),('deletion','middle','D’ailleurs'),('deletion','middle boxed cancellation','Quitte à remplacer V,V′ par Vtilde,Vtilde′'),('display','within cancellation','completion equality'),('text','middle-lower','c) On en conclut'),('insertion','above suites exactes','hom de'),('text','lower','Il reste à prouver'),('deletion','before i.e.','On'),('text','lower','Or ceci résulte du fait connu'),('deletion','last line before Khat-algèbres','corps'),('margin note','bottom left','14')]
save_page(34,15,tex,e,remarks='The parenthesis after k′/k est is slightly faint; l’ext. triviale is tentative. The cancelled comparison-of-completions paragraph is retained, including its unfinished terminal wording. The several unheaded horizontal strokes between group symbols are represented as strokes. The visible voisin ending agrees with coefficients, and is not changed to voisines.')
