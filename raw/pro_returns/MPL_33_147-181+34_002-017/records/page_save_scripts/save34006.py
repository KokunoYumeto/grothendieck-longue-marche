import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
tex=r'''\scanpage{6}
\mspage{4}

dans $\mathbf P^3_k$, alors on a
\[
 \mathbf Z\simeq\operatorname{Pic}(\mathbf P^3)\xrightarrow{\sim}\operatorname{Pic}(X_0),
\]
$k$ étant un corps de car. quelconque.

2. \uline{Rappels sur la structure de} $\pi$.

On suppose $S$ hensélien, i.e. $V$ hensélien.

2.1. Il y a une sous-extension $\widetilde K_{\deleted{\unsure{u}}}$ de $\bar K/K$, qui est la plus grde ss-extension non ramifiée (i.e. étale) \deleted{\unsure{dans}} sur $V$. Si \deleted{$\unsure{\widetilde K_\ell}$ est} $\bar V$ est la clôture normale de $V$ dans $\bar K$, $\widetilde V=\deleted{\unsure{\bar V_\ell}}\bar V\cap\widetilde K_{\deleted{\unsure{u}}}$ la clôture normale dans $\widetilde K_{\deleted{\unsure{u}}}$, alors $\widetilde V_{\deleted{\unsure{u}}}$ est un anneau de valuation discrète tel que
\[
 \deleted{\unsure{\mathfrak m}\widetilde V=\mathfrak m\widetilde V,}
 \qquad \widetilde V\otimes_V k=\bar k
\]
est une \deleted{extension de} clôture séparable de $k$; En d'autres termes, $\widetilde V$ est une \uline{hensélisation stricte} de $V$ p. r. à \deleted{\unsure{une}} la \deleted{\unsure{sa}} clôture séparable $\bar k$ de $k$, et $\widetilde K_{\deleted{\unsure{u}}}$ est le corps des fractions de $\widetilde V$. On pose
\inserted{
\[
\begin{cases}
\widetilde S=\operatorname{Spec}\widetilde V=\text{hensélisé strict de }S\\
\unsure{\bar s}=\operatorname{Spec}\bar k.
\end{cases}
\]
}

\unsure{2.3|2.2}. On se rappelle que \deleted{\unsure{toute}} la donnée de la clôture séparable $\bar K$ de $K$ définit canoniquement une clôture séparable $\bar k$ de $k$.

\deleted{Pour \deleted{\unsure{tout}} \unsure{$n$} \deleted{\unsure{premier à}} \unsure{$p$} \inserted{Si \unsure{$n$} est un} entier \unsure{$n$ premier à} \unsure{$p$} inversible dans $k$, on a
\[
2.1.1.\qquad {}_n\bar k^*\xleftarrow[\unsure{\varphi}]{\sim}{}_n\widetilde V^*\xrightarrow{\sim}\bar K^*
\]
d'où un isomorphisme canonique
\[
\mu_n(\bar K)\simeq\mu_n(\bar k).
\]
Ces isom. sont compatibles avec les \unsure{empilements}
}
\margin{5}
'''
e=[('text','top','dans P³_k alors on a'),('display','top','Z ≃ Pic(P³) → Pic(X₀)'),('text','upper','k étant un corps de car. quelconque'),('text','heading','2 Rappels sur la structure de π'),('text','upper-middle','On suppose S hensélien'),('text','middle','2.1 Il y a une sous-extension'),('deletion','Ktilde subscripts','u (five overwritten subscripts)'),('deletion','middle before sur V','dans'),('deletion','middle after Si','Ktilde est'),('deletion','Vtilde equality','Vbar subscript'),('display','middle-lower','mVtilde=mVtilde; Vtilde tensor k=kbar'),('deletion','before Vtilde tensor k','mVtilde=mVtilde'),('deletion','below display','extension de'),('text','lower','En d’autres termes'),('deletion','after p.r.à','une; sa'),('insertion','before 2.3','Stilde=Spec Vtilde; sbar=Spec kbar'),('text','lower','2.3 On se rappelle que'),('deletion','after que','toute'),('deletion','bottom large cancelled block','Pour tout n; Si n est un entier'),('insertion','cancelled block first line','Si n est un'),('display','cancelled block','2.1.1 n kbar* ← n Vtilde* → Kbar*'),('display','cancelled block','μn(Kbar) ≃ μn(kbar)'),('text','bottom in cancellation','Ces isom. sont compatibles'),('margin note','bottom left','5')]
save_page(34,6,tex,e,remarks='The dark subscripts on Ktilde and Vtilde appear deliberately suppressed; their underlying u is tentative. The numbering after 2.1 is overwritten and retained as 2.3|2.2. The entire bottom passage is cancelled, including its internal earlier cancellations. The last word of the cancelled paragraph is low confidence. No n-torsion subscript has been added to the rightmost Kbar* where it is not visible.')
