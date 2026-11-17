import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{51}
% archive foliation: 50
Il faudrait prouver le
\margin{!}
\uline{Th.} Soit $B$ une cat. \deleted{add.} $k$-additive munie d'une
famille $\Sigma$ de suites exactes,
\margin{\unsure{nb. faut-il supposer} \unsure{que} $B$ cat. abélienne
($\Sigma$ \unsure{des suites ex.})}
$\underline{\operatorname{Hom}}_{k,\Sigma\text{-ex}}(\mathcal P_\bullet,B)$ la \inserted{$k$-}catégorie \deleted{pleine de}
$\underline{\operatorname{Hom}}_k(\mathcal P_\bullet,B)$ formée des foncteurs $\Sigma$-exacts,
i.e. transformant suites de $\Sigma_\bullet$ en suites de $\Sigma$,
\deleted{\unsure{désignons les foncteurs exacts}}
\deleted{$\unsure{\underline{\operatorname{Hom}}}_{\Sigma\text{-ex}}(\mathcal P_\bullet,B)$ la sous-catégorie pleine}
$\underline{\operatorname{Hom}}_{k,\Sigma\text{-lex}}(\mathcal P_\bullet,B)$ la sous-catégorie pleine de
celles qui \deleted{transforment \unsure{les noyaux en noyaux}}
\inserted{commutent aux $\Sigma$-noyaux}.

a) Le foncteur restriction $F\longmapsto F(C_\bullet^\bullet)$
\[
\underline{\operatorname{Hom}}_{k,\Sigma\text{-\unsure{lex|ex}}}(\mathcal P_\bullet,B)
\longrightarrow\deleted{\underline{\operatorname{Hom}}_{k\text{-lin}}(K,B)=}B^\bullet
\]
\deleted{est une équivalence de catégories}
\inserted{est pleinement fidèle,}
\deleted{(\unsure{pour le foncteur} \unsure{sur} $\underline{\operatorname{Hom}}_{k,\Sigma\text{-lex}}$)}
l'image essentielle est
formée des $C^\bullet\in\operatorname{Ob}B^\bullet$ tels que les
$d^i:C^i\longrightarrow C^{i+1}$ admettent des \inserted{$\Sigma$-}\unsure{noyaux}.
\margin{\unsure{est une équivalence de cat.}}
[donc \deleted{$\unsure{K}$} $(\mathcal P_\bullet,C_\bullet^\bullet,\Sigma_\bullet)$ est universel pour
les triples $(B,C^\bullet,\Sigma)$ tels que
les $d^i:C^i\longrightarrow C^{i+1}$ aient des $\Sigma$-noyaux, quand
on prend comme morphismes les
foncteurs \deleted{\unsure{commutant}} $\Sigma$-exacts à g.]

b) Le foncteur \deleted{induit} \inserted{$F\longmapsto F(C_\bullet^\bullet)$}
\[
\underline{\operatorname{Hom}}_{k,\Sigma\text{-ex}}(\mathcal P_\bullet,B)\longrightarrow B^\bullet
\]
(qui est pl. fid. par a)) a comme
image essentielle les $C^\bullet\in\operatorname{Ob}B^\bullet$ qui sont
des $\Sigma$-résolutions (i.e. $\Sigma$-spéciaux et
avec $H^i(C^\bullet)=0$ si $i>0$).
\deleted{[donc le triple $(\mathcal P_\bullet,C_\bullet^\bullet,\Sigma_\bullet)$ apparait comme
universel pour les $(B,C^\bullet,\Sigma)$ tels que
$C^\bullet$ soit \unsure{une} $\Sigma$-résolution, --- les}
'''
save(51,text,[('text','top','Il faudrait prouver le'),('margin note','left top','!'),('text','top theorem','Th. Soit B une cat.'),('deletion','theorem first line','add.'),('margin note','upper right','nb. faut-il supposer B abélienne'),('display','upper quarter inline','Hom_{k,Sigma-ex}(P,B)'),('insertion','above catégorie','k-'),('deletion','after catégorie','pleine de'),('text','upper quarter','Hom_k(P,B) formée'),('deletion','upper middle','désignons les foncteurs exacts'),('deletion','upper middle','Hom_{Sigma-ex} la sous-catégorie'),('text','upper middle','Hom_{k,Sigma-lex}'),('deletion','after celles qui','transforment les noyaux'),('insertion','above same line','commutent aux Sigma-noyaux'),('text','middle a','a) Le foncteur restriction'),('display','middle a','Hom_{k,Sigma-lex} → B^•'),('deletion','right of arrow','Hom_{k-lin}(K,B)='),('deletion','below arrow','est une équivalence de catégories'),('insertion','right below arrow','est pleinement fidèle'),('deletion','parenthesis a','pour le foncteur sur Hom'),('text','middle lower a','l’image essentielle'),('insertion','above noyaux','Sigma-'),('margin note','left diagonal','est une équivalence de cat.'),('text','lower middle bracket','donc (P,C,Sigma) est universel'),('deletion','beginning bracket','K'),('deletion','before Sigma-exacts','commutant'),('text','lower quarter b','b) Le foncteur'),('deletion','b first line','induit'),('insertion','b above first line','F maps to F(C)'),('display','b','Hom_{k,Sigma-ex} → B^•'),('text','bottom b','qui est pl. fid. par a'),('deletion','bottom bracket','donc le triple')])
