from record_page import record
tex=r'''\scanpage{44}
% archive foliation: 43
Revenons à la prop. 1. Soit $C^\bullet$ \inserted{$\in\operatorname{Ob}B^\bullet$} un complexe
de cochaînes de $B$, comment reconstituer
le foncteur $k$-lin
\[
F_C:\unsure{K|C}\longrightarrow B
\]
i.e. comment ``calculer'' $F_C(x)$ pour $x\in\operatorname{Ob}\unsure{K|C}$ ?
Il faut bien sûr commencer par ``repérer'' $x$,
disons par $\alpha^\bullet(x)\in\mathrm{Ab}_k^\bullet$. Ceci dit, on trouve

\uline{Prop. 3}. On a un isom. bifonctoriel en $F,x$
(si $F\in\deleted{\unsure{F}}\operatorname{Ob}\underline{\operatorname{Hom}}_{k\text{-}lin}(C,B)$)
\[
\begin{gathered}
F(x)\xrightarrow{\sim}\operatorname{Hom}^\bullet_k(\alpha^\bullet(x),F(C^\bullet))\\
=\operatorname{Hom}^\bullet_k(\alpha^\bullet(x),C^\bullet_F),
\end{gathered}
\]
[où on définit, pour un $K^\bullet\in\operatorname{Ob}\mathrm{Ab}_k^\bullet$ et
$C^\bullet\in\operatorname{Ob}B_k^\bullet$, l'objet $\operatorname{Hom}^\bullet_k(K^\bullet,C^\bullet)$ de $B$
(s'il existe) par l'isom. fonctoriel en $b\in\operatorname{Ob}B$
\[
\operatorname{Hom}_{\inserted{B}}(b,\operatorname{Hom}^\bullet(K^\bullet,C^\bullet))
\simeq\operatorname{Hom}_{B^\bullet}(b\otimes_k K^\bullet,C^\bullet).
\]
Si les $K^i$ sont libres de type fini, $b\otimes_k K^\bullet$
est bien défini, donc $b\longmapsto\operatorname{Hom}_{B^\bullet}(b\otimes_k K^\bullet,C^\bullet)$
l'est, et la question est si ce foncteur est
représentable; il se trouve qu'il l'est si
$K^\bullet$ \deleted{\unsure{est}} $\in\operatorname{Ob}\deleted{\unsure{\mathrm{Ab}_k^\bullet}}K^\bullet$ [ Mais de façon
générale, c'est le sous-foncteur de
\[
\prod_i\underset{\in\operatorname{Ob}B}{\operatorname{Hom}_k(K^i,C^i)}
\]
noyau de
\[
\prod_i\operatorname{Hom}_k(K^i,C^i)\xrightarrow{\delta}
\prod_i\operatorname{Hom}_k(K^i,C^{i+1})
\]
($\delta(u^i)=du^i-u^{i+1}d$) --- \uline{ceci est repr.} si
$B$ \deleted{\uline{abélienne}}\inserted{stable par Ker}, si les $\operatorname{Hom}_k(K^i,C^i)$ sont
repr. (p.ex. les $K^i$ de prés. finie) et les deux
\margin{\unsure{remettre avant énoncé prop. 3}}
'''
record(44,tex,[('text','top','Revenons prop 1; C• complexe cochaînes B; reconstituer foncteur'),('insertion','after C•','∈ObB•'),('display','upper','F_C:K→B'),('text','upper','calculer F_C(x); repérer x par α•(x)'),('text','Prop 3','isom bifonctoriel F,x'),('display','parenthetic hypothesis','F∈Ob Hom_k-lin(C,B)'),('deletion','after F∈','F'),('display','middle','F(x)≈Hom_k•(α•(x),F(C•))=Hom_k•(α•(x),C_F•)'),('text','bracketed definition','K•∈ObAb_k•; C•∈ObB_k•; object Hom_k•'),('text','middle','s’il existe; isom fonctoriel en b'),('display','middle','Hom_B(b,Hom•(K•,C•))≃Hom_B•(b⊗K•,C•)'),('insertion','first Hom subscript','B'),('text','lower-middle','K^i libres type fini; tensor defined; representability'),('deletion','after K•','est'),('deletion','after ∈Ob','Ab_k•'),('text','lower','Mais de façon générale sous-foncteur noyau'),('display','lower','product_i Hom_k(Ki,Ci) with membership in ObB'),('display','lower','product Hom(Ki,Ci)→product Hom(Ki,Ci+1), δ'),('display','bottom inline','δ(ui)=dui−ui+1d'),('text','bottom','ceci est repr si B; Hom representable; prés finie; et les deux'),('deletion','B qualification','abélienne underlined'),('insertion','above abélienne','stable par Ker'),('margin note','left of bottom passage','remettre avant énoncé prop 3')],doubts=[('first functor source and x membership','K','C; ornate category letter has an extra vertical stroke','low'),('Hom superscript recurring','bullet','small dot; prime possible in a few lighter occurrences, retained as bullet from matching clear occurrences','medium'),('K• membership condition','K•∈ObK•','overwritten old Ab_k• and deleted est; literal repeated letter maintained','low'),('last marginal instruction','remettre avant énoncé prop. 3','remonter avant énoncé prop. 3; opening verb compressed','medium'),('last phrase','et les deux','page ends here; continuation not present in supplied package','high')],notation=[('representing-object notation',r'$\operatorname{Hom}^\bullet_k(K^\bullet,C^\bullet)$','scan 44; manuscript dot superscript preserved, no reinterpretation as derived Hom'),('degree-zero chain-map condition',r'$\delta(u^i)=du^i-u^{i+1}d$','scan 44 bottom; minus retained'),('functor comparison',r'$\alpha^\bullet(x)$','scan 44; superscript dot, distinguished from α′ in scan 42')])
