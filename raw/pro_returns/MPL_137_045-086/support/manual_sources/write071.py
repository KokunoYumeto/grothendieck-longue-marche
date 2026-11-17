import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{71}
% archive foliation: 70
Calcule $F$ à l'aide de sa restriction à $K$ comme
\[
F(\unsure{X|L})\simeq R^0F(L)\simeq\operatorname{Ker}(F(I)\longrightarrow F(J)).
\]
Ceci dit, on a
\diagram{\begin{tikzcd}
F(X)\otimes_B F(Y) \arrow[r,"?"] \arrow[d] & F(X*Y) \arrow[d] \\
F(I)\otimes_B F(J) \arrow[r] & F(I*J)
\end{tikzcd}}
\[
\text{comm. pour }F|K\text{ et sa structure mult.}
\]
Or on sait que \deleted{\unsure{$*$}} $*$ transforme des couples de $\Sigma$-monos en un $\Sigma$-mono (résulte immédiatement des formules de Dold Puppe) donc la 2\textsuperscript{ème} flèche verticale est un mono d'où la détermination unique de $?$.

Le fait qu'il soit indépendant des choix faits est immédiat, et aussi qu'il satisfait aux compatibilités d'ass. et de comm. si sa restriction à $K$ y satisfait. Il reste donc à examiner l'axiome d'unité, \deleted{\unsure{puisque}} il faut donc se donner
\[
\deleted{F(\Psi_0)}1_{B'}\longrightarrow F(\Psi_0)\simeq Z^0(C^\bullet)
\]
et on voit que l'axiome signifie que cela \unsure{nous munit d'une unité|nous donne une unité} pour la structure de ``\unsure{$k$-$\otimes$-Alg}'' de $F(\Psi^0)$ (qui est une ``\unsure{$k$-Alg. comm}'' de $K$).

\margin{\uline{NB} \unsure{On n'a donc ici pas} besoin de l'existence du $\operatorname{Ker}(d^0:C^0{-}C^1)$, il suffit de dire qu'on donne $1_B\longrightarrow C^0$ dont la composée $C^0\longrightarrow C^1$ est nulle, et qui joue le rôle d'une unité \deleted{\unsure{de $C^0$}} \unsure{au sens plus précis}.}
\figure{\begin{tikzpicture}\draw[->] (0,0)--(-1.5,0.9);\end{tikzpicture}}'''
e=[('text','top','Calcule F à l’aide de sa restriction à K comme'),('display','top','F(X)≃R0F(L)≃Ker(F(I)→F(J))'),('text','upper','Ceci dit on a'),('diagram','upper','F(X)⊗BF(Y)→F(X*Y)'),('text','below square','comm pour F|K et sa structure mult'),('text','middle','Or on sait que * transforme des couples de Σ-monos'),('deletion','middle','*'),('text','lower','Le fait qu’il soit indépendant des choix faits'),('text','lower','Il reste donc à examiner l’axiome d’unité'),('deletion','lower','puisque'),('display','bottom','1B′→F(Ψ0)≃Z0(C•)'),('deletion','bottom display','F(Ψ0)'),('text','bottom','et on voit que l’axiome signifie'),('margin note','left vertical','NB On n’a donc ici pas besoin de l’existence du Ker'),('deletion','left margin','de C0'),('drawing','bottom left','arrow to NB margin')]
save(71,text,e)
