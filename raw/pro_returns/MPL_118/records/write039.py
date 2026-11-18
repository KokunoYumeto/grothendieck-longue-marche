from save_page import save
text=r'''
\scanpage{39}
% archive foliation: 38
Passage à la limite

\uline{\unsure{Thm}} Soient $I$ un ordonné \deleted{filtrant}, $X,Y$ dans $(\mathrm{Cat})$, $(X_i)_{i\in I}$ et $Y=(Y_i)_{i\in I}$ deux filtrations par des sous-cat. fermées (resp. ouvertes), \deleted{\unsure{$f$}} $X=\bigcup X_i$, $Y=\bigcup Y_i$.
\[
f:X\longrightarrow Y
\]
tel que $f(X_i)\subset Y_i$, soit $f_i:X_i\unsure{\mathbin{-}|\longrightarrow}Y_i$.
Supposons que les $f_i$ soient des équiv. faibles, alors $f$ est une équiv. faible.

\margin{\unsure{On suppose que les inf existent et que les filtrations} \unsure{commutent}, \unsure{dans le cas où} $i=\operatorname{Inf}j_\alpha$, \unsure{on ait} $X_i=\bigcap_\alpha X_{j_\alpha}$.}

On est ramené par dualité au cas des ss-catégories ouvertes. On va \deleted{\unsure{supposer}} interpréter la filtration de $X$ comme la donnée de
\diagram{\begin{tikzcd}X\arrow[r,"\varphi"]&I\end{tikzcd}}
défini par
\[
\varphi(x)=\operatorname{Inf}_{\substack{i\text{ dans }I(x)=\\\{i\in I\mid x\in X_i\}}}i
\]
--- on suppose donc que dans $I$ les Inf \inserted{(des parties non vides)} existent. On \deleted{\unsure{pourra}} \inserted{aura}, pour
\[
\alpha:x\longrightarrow y
\]
$\varphi(x)\leq\varphi(y)$ (car $I(y)\subset I(x)$, donc $\operatorname{Inf}I(y)\geq\operatorname{Inf}I(x)$) d'où la valeur de $\varphi(\alpha)$. On \deleted{\unsure{aura supposé, où}} \inserted{devra supposer}
\[
X_i=\varphi^{-1}(I_i)\qquad\text{où}\qquad I_i=\{j\in I\mid j\leq i\}
\]
\deleted{\unsure{$\varphi$}} i.e. $\underbrace{x\in X_i}_{\text{i.e. }i\in I(x)}\Longleftrightarrow\varphi(x)\leq i$

\margin{\uline{NB} $\varphi(x)$ est ainsi le plus petit élément de $I(x)$ et $I(x)=\{j\in I\mid j\geq\varphi(x)\}$.}
'''
elements=[('text','top title','Passage à la limite'),('text','upper','Thm Soient I un ordonné'),('deletion','upper','filtrant'),('display','upper','X,Y dans (Cat); (X_i); Y=(Y_i)'),('text','upper','deux filtrations par des sous-cat. fermées'),('deletion','upper middle before X union','f'),('display','upper middle','X=union X_i; Y=union Y_i'),('display','upper middle','f:X → Y'),('text','middle','tel que'),('display','middle','f(X_i) subset Y_i; f_i:X_i - Y_i'),('text','middle','Supposons que les f_i soient des équiv. faibles'),('margin note','left tilted upwards','On suppose; i=Inf j_alpha; X_i=intersection X_j_alpha'),('text','middle lower','On est ramené par dualité au cas'),('deletion','middle lower','supposer'),('text','middle lower','interpréter la filtration de X'),('diagram','lower middle','X phi → I'),('text','lower','défini par'),('display','lower','phi(x)=Inf i'),('text','lower','on suppose donc que dans I les Inf existent'),('insertion','right above Inf','des parties non vides'),('deletion','lower','pourra'),('insertion','above pourra','aura'),('display','lower','alpha:x → y'),('display','lower','phi(x) ≤ phi(y); I(y) subset I(x); Inf I(y) ≥ Inf I(x)'),('text','bottom','d’où la valeur de phi(alpha)'),('deletion','bottom','aura supposé, où'),('insertion','above cancelled phrase','devra supposer'),('display','bottom','X_i=phi^-1(I_i); I_i={j in I | j≤i}'),('deletion','bottom left','phi'),('display','bottom','x in X_i iff phi(x)≤i; i.e. i in I(x)'),('margin note','lower right','NB phi(x) est ainsi le plus petit élément de I(x)'),('display','within NB','I(x)={j in I | j≥phi(x)}')]
save(39,text,'text',elements,'New title Passage à la limite. Filtered is cancelled in the first line. Left marginal condition is especially uncertain despite repeated rotation/enlargement; its prose is explicitly marked rather than silently reconstructed. The formula i=Inf j_alpha and X_i=intersection X_j_alpha is clearer. Several late corrections surround the Inf construction; source direction of f_i is only a plain dash or weak arrowhead. No claim checked.')
