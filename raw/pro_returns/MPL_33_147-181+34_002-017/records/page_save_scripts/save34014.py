import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{14}
\mspage{12}

en d'autres termes
\[
 \varepsilon_{K'_n}(\Theta_n)=(\varepsilon^e)_{K_n}(\Theta_n)
\]
et par suite
\[
 \varepsilon_{K'_n}|K_n=(\varepsilon^e)_{K_n}.
\]
Passant à la limite sur $n$, on trouve la

\uline{Proposition} 3.12. Si $\mathfrak mV'=\mathfrak m'^e$, alors l'hom. \inserted{can.} (3.8) provenant de (3.5) s'identifie à la multiplication par $e$.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw (0,1.5)--(0,.3) .. controls (0,.15) and (.04,.05) .. (.07,0);\end{tikzpicture}}

En particulier, si $e=1$ cet hom. est l'identité, \deleted{\unsure{et}} et à fortiori un isomorphisme. \inserted{Ceci s'applique en particulier si $V'=\widetilde V$.} En fait, on a mieux.

\uline{Prop.} 3.13. Supposons $V'=\widehat V$, \deleted{et $V$ \unsure{excellent}} \inserted{\deleted{et $V$ excellent (i.e. $\widehat K$ sép. sur $K$).}} Alors les hom de suites exactes (3.5) et (3.7) sont des isomorphismes.

\deleted{
$\pi'\longrightarrow\pi$ \deleted{est \unsure{donc}} surjectif, i.e. si $K_1$ est une extension finie séparable de $K$, alors $K_1\otimes_K\widehat K$ est un corps. \deleted{et $I'_t\simeq I_t$} \inserted{La clôture \unsure{normale} $V_1$ de $V$ dans $K_1$ est \uline{\unsure{finie}} \unsure{sur $V$}, par suite $V_1\otimes_V\widehat V=\widehat V_1$ intègre (car $V_1$ est un anneau \inserted{de val. discrète); donc $K_1\otimes_K\widehat K=\widehat V_1\otimes_{\unsure{\widehat V}}\widehat K$ est un corps.}}
(Comme $\pi'_0\longrightarrow\pi_0$ est évidemment un isom., et aussi \inserted{$I'_t\mathrel{\text{---}}I_t$, par l'injectivité de \unsure{$I'_t\mathrel{\text{---}}I_t$}}) on est ramené en fait à examiner $P'\mathrel{\text{---}}P$. Ceci \inserted{[ou directement $\pi'\longrightarrow\pi$, donc $I'\mathrel{\text{---}}I$)} est tjs injectif, d'après les résultats connus de \deleted{approximation} \inserted{continuité} des solutions d'une équation algébrique p. r. aux coefficients, qui \unsure{impliquent|expliquent} que des extensions séparables \uline{voisines} définissent des extensions isomorphes de $\widehat K$. \deleted{D'autre part, c'est surjectif} \inserted{Comme $I'\longrightarrow I$ est surjectif} \inserted{(d'après les résultats} \deleted{\unsure{que donne précisément} l'hypothèse d'excellence}

\uline{Remarque} 3.14. La prop. 3.13. montre que dans la plupart des questions \deleted{\unsure{concernant}} du séminaire, on pourrait supposer $V$ \uline{complet}.
}
\margin{\deleted{\uline{Attention}}}
\margin{$\widetilde V\subset\widetilde{\widehat V}\subset\widehat{\widetilde V}$}
\margin{13}
'''
e=[('text','top','en d’autres termes'),('display','top','epsilon_K′_n(Theta_n)=(epsilon^e)_K_n(Theta_n)'),('text','upper','et par suite'),('display','upper','restriction epsilon_K′_n|K_n'),('text','upper-middle','Passant à la limite sur n'),('text','middle','Proposition 3.12'),('insertion','right of l’hom','can.'),('drawing','left of proposition','vertical bracket stroke'),('text','middle','En particulier si e=1'),('deletion','after identité','et'),('insertion','interlinear','Ceci s’applique en particulier si V′=Vtilde'),('text','middle-lower','Prop. 3.13 Supposons V′=Vhat'),('deletion','above Alors','et V excellent'),('insertion','above Alors','cancelled et V excellent (i.e. Khat sép. sur K)'),('deletion','large bottom cancelled block','π′→π surjectif; proof and Remarque 3.14'),('deletion','cancelled proof start','est donc'),('deletion','cancelled proof first insertion','et I′_t≃I_t'),('insertion','cancelled proof interlinear','La clôture normale V₁ de V dans K₁'),('insertion','cancelled proof left margin','de val. discrète; donc tensor is a field'),('insertion','cancelled proof interlinear left','I′_t—I_t par l’injectivité'),('insertion','cancelled proof interlinear','ou directement π′→π donc I′—I'),('deletion','cancelled proof','approximation'),('insertion','cancelled proof above approximation','continuité'),('deletion','cancelled proof lower','D’autre part c’est surjectif'),('insertion','cancelled proof lower','Comme I′→I est surjectif'),('insertion','cancelled proof lower','d’après les résultats'),('deletion','cancelled proof lower','que donne précisément l’hypothèse d’excellence'),('text','bottom cancelled','Remarque 3.14 La prop. 3.13'),('deletion','bottom cancelled remark','concernant'),('margin note','left beside proof','deleted Attention'),('margin note','left lower','Vtilde subset tilde(Vhat) subset hat(Vtilde)'),('margin note','bottom left','13')]
save_page(34,14,tex,e,remarks='The cancelled proof is among the least legible passages in cote 34: interlinear revisions overlap the original proof and large cancellation strokes. Its uncertain connective words, the small I_t insertion, and the tail invoking excellence are low confidence. The completion/strict-henselization chain in the margin is read from the order of its two stacked accents. Prop. 3.13 itself remains outside the large cancellation, while its excellence hypothesis was struck out separately. The subsequent proof and Remarque 3.14 lie inside the large cancellation.')
