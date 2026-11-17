from record_page import record
tex=r'''\scanpage{10}
% archive foliation: 9
dire que $L_\bullet\simeq L^0_\bullet\otimes_{\mathbf Z}k$, où $L^0_\bullet$
est un complexe de $\mathbf Z$-modules \unsure{$\frac12$ simpliciaux}
spécial.

\uline{Proposition 2} Les $k$-modules \inserted{$\frac12$ simpliciaux} spéciaux
(resp. str. spéciaux) sont stables par
produits tensoriels [et par les op.
tensorielles $\Lambda^i$, $\Gamma^i$, $\operatorname{Sym}^i$?]
\margin{\unsure{faux}}
\margin{[\ ] faux}

Le cas strict. spécial se ramène
au cas spécial, en se plaçant sur $\mathbf Z$\unsure{\ldots}

1° Produit tensoriel. On se réduit
à prouver que les modules
\[
\left\{\begin{array}{ll}
\Lambda^i\unsure{\Phi_*}\otimes\Lambda^j\Phi_* &(i,j\geq1)\\
\Lambda^i\Psi_*\otimes\Lambda^j\Psi_* &(i,j\geq0)\\
\Lambda^i\Phi_*\otimes\Lambda^j\Psi_* &(i\geq1,\ j\geq0)
\end{array}\right.
\]
sont spéciaux. Or ils sont à composantes
libres de \unsure{r.f.|t.f.}, et par Künneth-Eilenberg-
Zilber leurs $\pi_i$ sont itou, il reste à
montrer qu'il n'y a qu'un nb fini
de facteurs $M_i$, $N_j$ $\neq0$. \deleted{\unsure{On va}} \inserted{Ce résultat}
\deleted{\unsure{prouver}} résulte du

\deleted{\uline{Lemme} Sous les conditions du cor 2 de
prop 1 sont encore équivalentes celles
suivantes (en supposant \deleted{\unsure{Spec $k$ connexe}}, \inserted{$k$ connexe}
de sorte que $\mu_i=\operatorname{rg}M_i$ et $\nu_j=\operatorname{rg}N_j$ est
défini)

a) $\operatorname{rg}_kL_n$ est un polynôme en $n$
pour $n$ grand

b) $\exists$}
'''
record(10,tex,[('text','top continuation','dire que L≃L^0⊗Z k'),('text','proposition heading','Proposition 2 Les k-modules spéciaux'),('insertion','above spéciaux','½ simpliciaux'),('text','proposition continuation','resp. str. spéciaux; produits tensoriels'),('text','bracketed extension','et par les op. tensorielles Λ, Γ, Sym?'),('margin note','left beside proposition','faux'),('margin note','left beside bracket','[ ] faux'),('text','proof first paragraph','Le cas strict. spécial'),('text','proof 1°','Produit tensoriel'),('display','three braced cases','Λ^i Φ⊗Λ^j Φ; Λ^i Ψ⊗Λ^j Ψ; Λ^i Φ⊗Λ^j Ψ'),('text','middle-lower proof','sont spéciaux. Or ils sont'),('deletion','after M_i,N_j≠0','On va'),('insertion','right above deletion','Ce résultat'),('deletion','before résulte du','prouver'),('text','before cancelled lemma','résulte du'),('deletion','lower block, diagonal strikes','Lemme Sous les conditions; a); b)∃'),('deletion','inside cancelled lemma','Spec k connexe'),('insertion','inside cancelled lemma','k connexe')],doubts=[('top continuation','dire; ½ simpliciaux; L^0','staff overlaps letters and superscript','medium'),('left upper margin','faux','possibly a short proof cue; bracketed faux clearer','low'),('proposition operations','Λ^i, Γ^i, Sym^i?','superscripts faint; question mark visible','medium'),('case 1 first Φ','Φ_*','extra mark near upper right of Φ unclear','low'),('proof abbreviation','r.f.','t.f.','medium'),('cancelled lemma','Spec k connexe; k connexe; μ_i,ν_j; est défini','overwrites and several diagonal cancellations','medium')],notation=[('question in bracketed stability claim',r'[$\Lambda^i$, $\Gamma^i$, $\operatorname{Sym}^i$?]','scan 10; preserve question and separate marginal faux'),('superscript zero',r'$L^0_\bullet$','scan 10; circular small superscript, unlike !')])
