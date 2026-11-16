import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{4}
\mspage{2}

\unsure{Comme|Alors} $\pi$ opère sur \deleted{$\unsure{H^iX_{\bar K}}$} $E$ par ``transport de structure'', on trouve une représentation $\ell$-adique $(*)$.

\uline{Exemple} 0.4. Soit $A$ un \deleted{\unsure{schéma en}} groupe algébrique \inserted{comm.} sur $K$.
\deleted{\unsure{comm.}} alors on regarde
\[
 E=T_\ell(A(\bar K))\overset{\mathrm{dfn}}=\varprojlim_\nu {}_{\ell^\nu}A(\bar K)
\]
\deleted{\unsure{Comme}} le groupe ne change pas si on remplace $A$ par $(A^\circ)_{\unsure{\mathrm{red}}}$ (NB. $T_\ell$ est un foncteur exact à gauche nul sur les groupes finis), c'est un \deleted{groupe} \uline{module libre sur} $\mathbf Z_\ell$ de rang égal : $2\alpha+\deleted{\unsure{2}}\mu$, où $\alpha$ ($\mu$) est la dim. de la ``partie'' ``abélienne'' resp. \inserted{``partie''} ``torique'' de $(A_K)^\circ_{\mathrm{red}}$. Ici encore, $\pi$ opère sur $E$ par transport de structure.

\uline{Remarque} 0.5. On peut regarder l'exemple $0.\unsure{3}$ comme étant essentiellement \deleted{un} \inserted{le} cas particulier de l'exemple 0.4, \inserted{pour $i=1$}.
De façon précise, \inserted{on montre que} on a un isom canonique
\[
 H^1(A_{\bar K},\mathbf Z_\ell)\simeq \deleted{\unsure{H^1}}\operatorname{Hom}_{\mathbf Z_\ell}(T_\ell(A(\bar K)),\mathbf Z_\ell),
\]
ou ce qui revient au même, puisque $T_\ell(A_{\bar K})$ est libre de type fini sur $\mathbf Z_\ell$ :
\[
 T_\ell(A(\bar K))=\operatorname{Hom}_{\mathbf Z_\ell}(H^1\unsure{(}A_{\bar K},\mathbf Z_\ell),\mathbf Z_\ell).
\]
D'autre part, \deleted{dans 0.3, si} si \deleted{$i=1$} dans 0.3. $X$ est propre et $i=1$, on trouve
\[
\begin{aligned}
 H^1(X_{\bar K},\mathbf Z_\ell(1))&\simeq\varprojlim_\nu H^1(X_{\bar K},\mu_{\ell^\nu})\simeq T_\ell(\operatorname{Pic}(X_{\bar K}))\\
 &\simeq T_\ell(\underline{\operatorname{Pic}}_{X/K}(\bar K))
\end{aligned}
\]
\margin{3}
'''
e=[('text','top','Comme π opère sur E'),('deletion','top line','H^iX'),('text','upper','Exemple 0.4. Soit A'),('deletion','upper line','schéma en'),('insertion','upper right','comm.'),('deletion','before alors','comm.'),('display','upper','E=Tℓ(A(Kbar))'),('deletion','before le groupe','Comme'),('text','upper-middle','le groupe ne change pas'),('deletion','middle','groupe'),('deletion','rank formula','2'),('insertion','above torique','partie'),('text','middle-lower','Remarque 0.5'),('deletion','Remarque line 2','un'),('insertion','Remarque line 2','le'),('insertion','right margin','pour i=1'),('insertion','above De façon précise','on montre que'),('display','lower','H¹(A_Kbar,Zℓ)'),('deletion','first duality display','H¹'),('text','lower','ou ce qui revient au même'),('display','lower','Tℓ(A(Kbar))=Hom'),('text','bottom','D’autre part'),('deletion','bottom line','dans 0.3 si'),('deletion','bottom line','i=1'),('display','bottom','H¹(X_Kbar,Zℓ(1))'),('margin note','bottom left','3')]
save_page(34,4,tex,e,remarks='The first word and the overwritten term before E remain uncertain. The second duality display has an opening parenthesis after H^1 that is not securely visible; it is marked rather than supplied confidently. The faint insertion partie is attached to torique by its stroke. The overwritten reduced-group subscript is doubtful.')
