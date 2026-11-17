import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{49}
% archive foliation: 48
\margin{Il vaut mieux construire $\mathcal P$ ``en l'air'', puis les \unsure{noter}
$\mathcal P_\bullet,\mathcal P_*,\mathcal P^\bullet,\mathcal P^*$ comme pour $K$.}
Soit $\mathcal P_\bullet$ la catégorie des complexes de $k$-chaines $L_\bullet$
qui sont libres de \unsure{r.f.|t.f.} en chaque dim,
et qui n'ont qu'un nb fini de composantes
non nulles. Une suite :
\[
0\unsure{-|\longrightarrow}L'_\bullet\unsure{-|\longrightarrow}L_\bullet\unsure{-|\longrightarrow}L''_\bullet\longrightarrow0
\]
\inserted{d'hom dans $\mathcal P_\bullet$} est dite exacte spéciale, si $\forall n\geqslant0$, la suite
\[
0\longrightarrow L'_n\longrightarrow L_n\unsure{-|\longrightarrow}L''_n\longrightarrow0
\]
est \unsure{ex. ab.} Soit $\Sigma_\bullet$ la
classe de ces suites. Ainsi $\mathcal P_\bullet$ est muni de
$C_\bullet^\bullet$ (complexe de cochaines) et de $\Sigma_\bullet$. On va
voir que, pour ces données, il est sol. d'un
pb universel.
\margin{!}

Soit \deleted{$\unsure{B}$} $B$ une cat. additive. Un ens. $\Sigma$ de
suites
\[
(*)\qquad 0\unsure{-|\longrightarrow}A'\xrightarrow{q}A\xrightarrow{p}A''\unsure{-|\longrightarrow}0
\]
dans $B$ est dit ``une classe de suites exactes''
si elle satisfait aux conditions

Sex 1) Si $(*)\in\Sigma$, alors $A'\xrightarrow{\sim}\operatorname{Ker}p$, $\operatorname{Coker}q\xrightarrow{\sim}A''$,
i.e. les suites $0\unsure{-|\longrightarrow}A'\unsure{-|\longrightarrow}A\longrightarrow A''$ et \deleted{\unsure{les}}
$A'\unsure{-|\longrightarrow}A\longrightarrow A''\unsure{-|\longrightarrow}0$
sont exactes (i.e. $\forall B\in\operatorname{Ob}B$, les suites de groupes
ab.
\[
\left\{\begin{aligned}
0&\unsure{-|\longrightarrow}\operatorname{Hom}(B,A')\unsure{-|\longrightarrow}\operatorname{Hom}(B,A)\unsure{-|\longrightarrow}\operatorname{Hom}(B,A'')\\
0&\unsure{-|\longrightarrow}\operatorname{Hom}(A'',B)\unsure{-|\longrightarrow}\operatorname{Hom}(A,B)\unsure{-|\longrightarrow}\operatorname{Hom}(A',B)
\end{aligned}\right.
\]
\deleted{\unsure{et}} sont exactes.

Sex 2) $\Sigma$ stable par iso, par sommes finies
et contient les suites de la forme
\[
0\unsure{-|\longrightarrow}A\xrightarrow{\mathrm{id}}A\unsure{-|\longrightarrow}0\unsure{-|\longrightarrow}0
\]
\[
0\unsure{-|\longrightarrow}0\unsure{-|\longrightarrow}A\xrightarrow{\mathrm{id}}A\longrightarrow0
\]
(donc aussi les suites de la forme
\[
0\unsure{-|\longrightarrow}A\xrightarrow{\mathrm{inj}}A\times B\xrightarrow{\mathrm{pr.}}B\unsure{-|\longrightarrow}0\qquad)
\]
'''
save(49,text,[('margin note','upper left diagonal','Il vaut mieux construire P'),('text','top','Soit P_• la catégorie'),('display','upper quarter','0 L′ L L′′ 0'),('insertion','left before est dite','d’hom dans P_•'),('text','upper middle','est dite exacte spéciale'),('display','upper middle','0 L′_n L_n L′′_n 0'),('text','upper middle','est ex. ab. Soit Sigma'),('margin note','left of pb universel','!'),('text','middle','Soit B une cat. additive'),('deletion','after Soit','B'),('display','middle','(*) 0 A′ q A p A′′ 0'),('text','middle','dans B est dit'),('text','lower middle','Sex 1'),('deletion','within Sex 1','les'),('display','lower middle brace','two Hom exact sequences'),('deletion','left after brace','et'),('text','below brace','sont exactes'),('text','lower quarter','Sex 2'),('display','lower quarter','0 A id A 0 0'),('display','lower quarter','0 0 A id A 0'),('text','bottom','donc aussi les suites'),('display','bottom','0 A inj A×B pr B 0')])
