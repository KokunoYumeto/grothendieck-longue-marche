import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""\mspage{d}
donc
\[
\underline{\mathrm{Hom}}_B(X,Y^M)\simeq\underline{\mathrm{Hom}}_B(\underbrace{X\times p_A^*(M)}_{\deleted{\unsure{\mathop{=}\limits^{\mathrm{déf}}}X\otimes\unsure{M}}},Y).
\]
\unsure{Relation} valable pour tt $X,Y\in(A\times B)^\wedge$, \unsure{mais nous|mais ici}, nous nous \unsure{intéressons} à cette formule pour $X,Y\in\underline{\mathrm{Hom}}(B^o,A)$, en nous attendant à y trouver aussi $Y^M,X\otimes M$ dans $\underline{\mathrm{Hom}}(B^o,A)$. On a vu des conditions naturelles pour qu'il en soit ainsi pour $Y^M$ (existence de certaines $\varprojlim$ dans $A$, à l'exclusion des $\underline{\mathrm{Hom}}$ internes dans $A$),

Il reste à regarder pour $X\times p_A^*(M)$, qui en tant que foncteur $B^o\mathbin{\text{---}}\widehat A$ s'identifie à
\[
b\longmapsto\underbrace{X(b)\times M(b)}=\bigl\{a\longmapsto\deleted{X}\underbrace{\mathrm{Hom}_A(a,X(b))}_{X(b)(a)=X(a,b)}\times M(b)\bigr).
\]
Comme \unsure{tantôt|d'hab.}, il n'est pratiquement jamais représentable. Mais supposons que dans $A$ les sommes existent (\unsure{les sommes} finies suffisent si les $M(b)$ sont eux-mêmes finis) et définissons
\[
X\otimes M\in\underline{\mathrm{Hom}}(B^o,A)\quad\text{par}
\]
\[
\deleted{(X\otimes M)(b)}=\deleted{\unsure{X(b)}}\underset{\sigma\in M(b)}{\coprod_A}\underbrace{X(b)}
\]
\margin{\diagram{\begin{tikzcd}[column sep=large]
(\phantom{X} \arrow[r,"\unsure{non}","\mathrm{iso}"',"\sim" description] & \displaystyle\underset{\sigma\in M(b)}{\coprod_{\widehat A}}X(b) \\
& {}=(X\times p_A^*(M))(b)
\end{tikzcd}}}
alors on a, pour $X_{\deleted{\unsure{b}}},Y$ dans $\underline{\mathrm{Hom}}(B^o,A)$
\[
\underline{\mathrm{Hom}}_B(X,Y^M)\simeq\underline{\mathrm{Hom}}_B(X\otimes M,Y)\qquad\text{trifonctoriel}
\]
\mspage{9}
"""
elements=[('text','top','d; donc'),('display','top','Hom_B(X,Y^M) ≃ Hom_B(X × p_A*(M),Y)'),('text','upper paragraph','Relation valable pour tt X,Y'),('text','middle','Il reste à regarder'),('display','middle','b ↦ X(b) × M(b)'),('text','lower middle','Comme tantôt, il n’est pratiquement jamais représentable'),('display','lower','X ⊗ M ∈ Hom(B^o,A) par'),('display','lower','(X ⊗ M)(b) = coproduct_A X(b)'),('diagram','lower right margin','comparison with coproduct in Ahat'),('text','bottom','alors on a, pour X,Y'),('display','bottom','Hom_B(X,Y^M) ≃ Hom_B(X⊗M,Y) trifonctoriel'),('text','foot','9')]
if __name__=='__main__':save(107,10,tex,elements,notes='Tensor construction by coproducts in A, juxtaposed with presheaf product. Several cancellations in the defining formulas retained; rightward comparison to coproduct in Ahat has a doubtful “non / iso” label and is not reversed to fit a canonical-map expectation. Parenthetical exclusion of internal Hom conditions is explicit. Claims the presheaf product is practically never representable and states a trifunctorial relative-Hom isomorphism. Prose “mais ici”, “tantôt”, and initial “les sommes” remain doubtful.')
