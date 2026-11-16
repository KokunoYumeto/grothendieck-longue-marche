from page_work import save_page
text=r'''\cotefile{43}
\scanpage{94}
Soit $\mathcal T'_k$ l'\unsure{espace} de Weil suivant : les objets sont les
\deleted{\unsure{quasi} \unsure{groupes} \unsure{quasi-algébriques}}
\deleted{\unsure{schémas}}
\unsure{quasi-schémas} \unsure{presque} compacts, \unsure{la descente}
est donnée par les morphismes \deleted{\unsure{surjectifs}} \uuline{finis}
surjectifs. Soit $C'(k)$ la catégorie des faisceaux de Weil sur $\mathcal T'_k$.

\margin{Le \unsure{choix|désir} de ``fini'' est imposé par le désir d'avoir
une ``application continue'' $\mathcal T'_k\unsure{\longrightarrow|-}\mathcal T_S$ !}

On a dans $C'(k)$ les foncteurs $H^i(k,G)$,
$\operatorname{Ext}^i(k;F,G)$, \inserted{$\underline{\operatorname{Ext}}^i_k(F,G)$}
et les relations habituelles
\[
\left\{\begin{aligned}
 H^i(k,F)&\simeq\operatorname{Ext}^i(k;\mathbb Z_k,F)\\
 \operatorname{Ext}^{\unsure{n|p+q}}(k;F,G)&\Longleftarrow
 H^p(k,\underline{\operatorname{Ext}}^{\unsure{q}}_k(F,G))
\end{aligned}\right.
\]

On notera que si $k$ est alg. clos, alors
$H^i(k,F)=0$ pour $i>0$. La formation des
$\underline{\operatorname{Ext}}^i_k(F,G)$ commute \unsure{à}
l'extension du corps de base\unsure{\ldots}

Il y a lieu de \deleted{\unsure{calculer}} donner des règles de calcul
pour des $H^i(k,G)$, $\operatorname{Ext}^i(k;F,G)$ si $G$ provient d'un
\inserted{quasi-}\unsure{schéma} en groupes habituel sur $k$,
[p.ex. d'un \unsure{pro.gr.} de Serre de type ``spécial'', i.e. à
morphismes de transition \unsure{finis} pour l'indice grand\unsure{\ldots}].
Il faudrait prouver alors que ($k$ est parfait)

\noindent a) si $G$ est \unsure{simple} sur $k$, les $H^i(k,G)$ sont les
$H^i(k,\widetilde G)$, où $\widetilde G$ est le faisceau de Weil associé\ldots

\noindent b) Kif-kif pour les $\operatorname{Ext}^i(k;F,G)$\ldots
\mspage{93}
'''
elements=[
 ('text','top','Soit T prime k'),
 ('deletion','top lines 2–3','quasi groupes quasi-algébriques; schémas'),
 ('deletion','upper definition before finis','surjectifs'),
 ('margin note','left diagonal bracket','Le choix de fini'),
 ('text','upper middle','On a dans C prime k'),
 ('insertion','above Ext list','underlined Ext i k(F,G)'),
 ('display','middle brace two lines','H i(k,F); Ext n(k;F,G)'),
 ('text','middle lower','On notera que si k est alg. clos'),
 ('text','lower','Il y a lieu de donner des règles'),
 ('deletion','lower first line','calculer'),
 ('insertion','above schéma','quasi-'),
 ('text','bottom','Il faudrait prouver alors que'),
 ('text','bottom item a','si G est simple sur k'),
 ('text','bottom item b','Kif-kif pour les Ext'),
 ('text','bottom left page number','93')]
save_page(94,text,elements,observations='Additional enlarged crops of the opening, spectral-sequence display, lower paragraph and rotated left margin were examined. The first two deleted lines remain especially uncertain. No question from the sealed context was used to choose a reading.')
