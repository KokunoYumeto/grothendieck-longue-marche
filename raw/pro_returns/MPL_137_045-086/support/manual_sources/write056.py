import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
s=r'''\scanpage{56}
% archive foliation: 55
l'hyp de récurrence. Cela donne donc
\[
\underline{\operatorname{Hom}}_{k,\Sigma\text{-sex}}(\mathcal P_\bullet,B)\xrightarrow{\sim}B^\bullet
\]
(si $B$ muni d'une \deleted{catégorie}\inserted{classe $\Sigma_0$} de suites exactes
telle que $\forall$ morphisme de $B$ admette
un $\Sigma$-noyau).

\uline{NB} Si on \inserted{ne} suppose \deleted{\unsure{plus} que $B$ admette une
classe $\Sigma$ de suites exactes, mais} \unsure{pas autre que}
$\forall$ morphisme de $B^\bullet$ admette un noyau,
l'argument donné montre seulement que
le foncteur ci-dessus $F\longmapsto F(C_\bullet^\bullet)$
\diagram{\begin{tikzcd}
\underline{\operatorname{Hom}}_{k,\Sigma\text{-sex}}(\mathcal P_\bullet,B)\arrow[r,shift right,"\rho"\']&B^\bullet\arrow[l,shift right,"\sigma"\']
\end{tikzcd}}
est pl. fid. (avec adjoint $\sigma$ comme dessus,
mais à valeurs dans $\underline{\operatorname{Hom}}_{k,\mathrm{lin}}(\mathcal P_\bullet,\widehat B)$);
on a néanmoins $\sigma\rho\simeq\mathrm{id}$ i.e.
\[
\deleted{F(L_\bullet)\simeq}\qquad
F(L_\bullet)\simeq\operatorname{Hom}_k^\bullet(L^\bullet,\underbrace{F(C_\bullet^\bullet)}_{\Vert\;C^\bullet})
\]
pour $\forall F\in\underline{\operatorname{Hom}}_{k,\Sigma\text{-sex}}$.

\uline{Re NB} On \deleted{\unsure{en}} vérifie facilement, sous les
conditions du NB, que si $F\longmapsto C^\bullet=F(C_\bullet^\bullet)$
se correspondent ($F\in\operatorname{Ob}\underline{\operatorname{Hom}}_{k,\Sigma\text{-sex}}$), alors
$F$ est $\Sigma$-\unsure{ex.act|ex.} ssi $C^\bullet$ est une $\Sigma_0$-résolution.
(du moins si $B$ cat. abélienne avec $\Sigma$ ttes
les suites exactes\ldots)

\uline{Ex} Soit $\unsure{\lambda|\Lambda}_\bullet\in\mathrm{Ab}_{k\bullet}$, considérons
\inserted{$\mathcal P_\bullet\unsure{-|\longrightarrow}\mathrm{Ab}_k$}
le foncteur $L_\bullet\longmapsto\operatorname{Hom}_{\mathrm{Ab}_{k\bullet}}(\lambda_\bullet,L_\bullet)$.
Il est $\Sigma$-exact à g (et même exact \uline{à g}) --- en fait
\margin{\unsure{TSVP}}
'''
e=[('text','top','l’hyp de récurrence'),('display','top','Hom(P,B) isom B^bullet'),('text','upper','si B muni d’une'),('deletion','upper line 3','catégorie'),('insertion','upper above line','classe Sigma_0'),('text','upper middle','NB Si on suppose'),('insertion','above NB line','ne'),('deletion','two NB lines','plus que B admette une classe'),('text','middle','forall morphisme de B^bullet'),('diagram','middle','Hom(P,B) B^bullet; sigma rho'),('text','middle','est pl. fid.'),('text','middle lower','on a néanmoins sigma rho'),('display','middle lower','F(L) isom Hom(L dual,F(C))'),('deletion','left of display','F(L) isom'),('text','below display','pour forall F'),('text','lower','Re NB On vérifie facilement'),('deletion','Re NB first line','en'),('text','lower','du moins si B cat. abélienne'),('text','bottom','Ex Soit lambda'),('insertion','bottom right above line','P - Ab_k'),('margin note','bottom right','TSVP')]
save(56,s,e)
