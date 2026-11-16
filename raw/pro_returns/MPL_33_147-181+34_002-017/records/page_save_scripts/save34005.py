import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{5}
\mspage{3}

ou si on préfère
\[
 H^1(X_{\bar K},\mathbf Z_\ell)\simeq T_\ell(\underline{\operatorname{Pic}}_{X/K}(\bar K))\otimes_{\mathbf Z_\ell}\mathbf Z_\ell(-1).
\]

0.6. Lorsque $A$ est un schéma abélien sur $K$, nous verrons que la connaissance du $\pi$-module $T_\ell(A(\bar K))$ donne des informations \unsure{assez} précises sur la structure du \uline{modèle de Néron} de $A$ [\quad], et inversement la \inserted{connaissance du modèle de Néron permet d'obtenir des renseignements complémentaires intéressants sur $T_\ell(A(\bar K))$, et partant sur \unsure{tous les} $H^{\unsure{i|1}}(X_{\bar K})\unsure{?}$ comme $\pi$-modules}.

D'autre part, l'étude des $\pi$-modules plus généraux $H^i(X_{\bar K},\mathbf Z_\ell)$ s'introduit quand on \deleted{\unsure{désire de}} dispose d'un \deleted{modèle} \inserted{schéma} $X$ \deleted{de} sur $S$ de fibre générique $X_K=X_\eta$, et qu'on désire étudier les relations entre \inserted{$H^i(X)$,} $H^i(X_s)$ et $H^i(X_{\bar\eta})$; (p. ex. dans certains cas on pourra montrer $H^i(X_s)\simeq H^i(X_{\bar\eta})^\pi$). Cette \deleted{Deligne, utilisant l'étude} étude locale s'avère comme un outil indispensable pour l'étude \uline{globale} \inserted{cohomologique} d'un morphisme
\[
 f:X\longrightarrow S
\]
avec $S$ régulier de dim 1. \deleted{\unsure{Prenant le}} Dans le cas où $S=\mathbf P^1_k$, et où $f$ ``est'' \deleted{\unsure{disant}} un pinceau \inserted{linéaire} de sections hyperplanes d'une variété projective lisse $X_0$ définie sur $k$, on est dans la situation typique de la \uline{théorie de Lefschetz} [\quad]. S'inspirant d'arguments de Lefschetz, Deligne montrera plus tard que si $X_0$ est une surface de degré $\geq4$
\margin{4}
'''
e=[('text','top','ou si on préfère'),('display','top','H¹(X_Kbar,Zℓ)'),('text','upper-middle','0.6 Lorsque A est un schéma abélien'),('insertion','between paragraphs and left margin','connaissance du modèle de Néron permet'),('text','middle','D’autre part l’étude des π-modules'),('deletion','middle','désire de'),('deletion','middle','modèle'),('insertion','above modèle','schéma'),('deletion','after X','de'),('insertion','above cohomology list','H^i(X)'),('deletion','between lines','Deligne utilisant l’étude'),('insertion','above globale','cohomologique'),('display','lower','f:X→S'),('text','lower','avec S régulier de dim 1'),('deletion','lower','Prenant le'),('deletion','after est','disant'),('insertion','left lower','linéaire'),('text','bottom','S’inspirant d’arguments de Lefschetz'),('margin note','bottom left','4')]
save_page(34,5,tex,e,remarks='The long interlinear addition ends in the left margin, where its cohomological superscript and final small mark remain uncertain. The final surface de degré ≥4 is retained as written; the sentence continues on the next sheet. The empty citation brackets have no numbers supplied.')
