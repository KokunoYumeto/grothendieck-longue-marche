import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{53}
% archive foliation: 52
\deleted{Soit $\mathcal P\supset K$ une sous-catégorie $k$-additive.}
\diagram{\begin{tikzcd}
\deleted{\underline{\operatorname{Hom}}_{k\text{-lin}}(\mathcal P,B)}\arrow[r,shift left=.6ex,"\deleted{\rho}"]&
\deleted{B}\arrow[l,shift left=.6ex,"\deleted{\sigma}"]
\end{tikzcd}}
\margin{\deleted{$B$ cat. additive avec $\Sigma$ classe de suites exactes et $\Sigma$-noyaux.}}
\margin{\deleted{\unsure{\phi}}}
\diagram{\begin{tikzcd}
\deleted{\underline{\operatorname{Hom}}_{k\text{-lin}}(\mathcal P,\widehat B)}\arrow[d,"\deleted{\vee}"]&\\
\deleted{\underline{\operatorname{Hom}}_{k\text{-lin}}(\mathcal P,B)}\arrow[r,"\deleted{\rho}"]&
\deleted{B^\bullet}\arrow[ul,"\deleted{\sigma}"']
\end{tikzcd}}

$B$ catégorie additive, \deleted{avec noyaux et \unsure{filtres}}
\deleted{\unsure{une} $\Sigma$ de suites exactes}, où
$\forall$ morphisme admet un $\Sigma$-noyau
\diagram{\begin{tikzcd}[column sep=large]
\underline{\operatorname{Hom}}_{k,\Sigma\text{-\unsure{lex}}}(\mathcal P_\bullet,B)
\arrow[r,shift left=.6ex,"\rho"]&B^\bullet\arrow[l,shift left=.6ex,"\sigma"]
\end{tikzcd}}
\margin{non, il faut condition de platitude ?}
cat. des foncteurs $k$-lin
$F:\mathcal P\longrightarrow B$
qui transforment suites $\in\Sigma$
en suites exactes à g.
\[
\left\{\begin{aligned}
\rho(F)&=F(C^\bullet)\\
\sigma(C^\bullet)(L_\bullet)&\simeq\underbrace{\operatorname{Hom}_{k}^\bullet(L_\bullet^\vee,C^\bullet)}_{
\substack{\text{défini grâce à l'existence}\\\text{des }\Sigma\text{-noyaux}}}
\simeq\operatorname{Hom}_k^\bullet(\operatorname{Hom}(L_\bullet,C_\bullet^\bullet),C^\bullet)
\end{aligned}\right.
\]
Formule d'adjonction
\diagram{\begin{tikzcd}[row sep=small,column sep=large]
\operatorname{Hom}(\rho(F),C^\bullet)\arrow[r,"\simeq"]\arrow[d,equal]&\operatorname{Hom}(F,\sigma(C^\bullet))\\
\operatorname{Hom}(F(C^\bullet),C^\bullet)&
\end{tikzcd}}
Le deuxième ens est formé des hom fonctoriels en $L_\bullet$
\[
F(L_\bullet)\longrightarrow\operatorname{Hom}_k^\bullet(L_\bullet^\vee,C^\bullet)
\]
\inserted{$L^\bullet$}
i.e. des hom ``fonctoriels en $L_\bullet$''
\[
L^\bullet\otimes_k F(L_\bullet)\longrightarrow C^\bullet.
\]
Or on a $L^\bullet\simeq\operatorname{Hom}(L_\bullet,C_\bullet^\bullet)$
\[
F(L)\otimes L^\bullet\deleted{\otimes F(L_\bullet)}\simeq
\operatorname{Hom}(L_\bullet,C_\bullet^\bullet)\otimes F(L_\bullet)\xrightarrow{\mathrm{taut.}}F(C^\bullet)
\]
et on trouve qu'on a ainsi la ``\uline{\unsure{fonctorialité}}''
compatibilité à l'op. diff. en $L^\bullet$ et $C^\bullet$, et ``\unsure{fonctorialité}''
'''
save(53,text,[('deletion','top','Soit P superset K'),('diagram','upper','Hom(P,B) ↔ B cancelled'),('margin note','upper right','B cat. additive avec Sigma'),('margin note','upper left','phi cancelled'),('diagram','upper quarter','Hom(P,Bhat) Hom(P,B) B^• cancelled'),('text','middle','B catégorie additive'),('deletion','middle','avec noyaux et filtres'),('deletion','above middle','Sigma de suites exactes'),('diagram','middle','Hom_lex(P,B) ↔ B^•'),('margin note','right middle large ink','non il faut condition de platitude ?'),('text','below left category','cat. des foncteurs k-lin'),('display','middle lower brace','rho(F), sigma(C)(L)'),('text','underbrace','défini grâce à l’existence des Sigma-noyaux'),('text','lower middle heading','Formule d’adjonction'),('diagram','lower middle','Hom(rho F,C) Hom(F,sigma C)'),('text','lower middle','Le deuxième ens'),('display','lower quarter','F(L) → Hom(Lvee,C)'),('insertion','above i.e.','L^•'),('text','lower quarter','i.e. des hom'),('display','lower quarter','L^• tensor F(L) → C'),('text','lower quarter','Or on a L^•'),('display','bottom','F(L) tensor L^• taut F(C)'),('deletion','inside bottom display','tensor F(L)'),('text','bottom','et on trouve')])
