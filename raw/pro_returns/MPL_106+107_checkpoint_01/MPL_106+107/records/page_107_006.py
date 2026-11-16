import sys
sys.path.insert(0,'/workspace/scratch/4bbc351d3cab/MPL_106+107/scripts')
from save_page import save
tex=r"""
\mspage{b}
\deleted{\unsure{On peut aussi décrire les mêmes foncteurs}}
\inserted{On a une troisième interprétation du foncteur} \(\Gamma_b''\), en
\deleted{\[\mathrm{Hom}_{(A\times B)^\wedge}(p_A^*(b),\underline{\mathrm{Hom}}(p_A^*(b),X))\]}
\unsure{écrivant}
\[(\unsure{A}\times B)^\wedge\simeq\underline{\mathrm{Hom}}(A^o,B^\wedge)\]
et considérant \deleted{\(\unsure{\Gamma_b}\)}
\[\varepsilon_b:B^\wedge\longrightarrow\mathrm{Ens},\qquad\varepsilon_b(G)=\mathrm{Hom}(b,G)=G(b)\]
alors \(\Gamma_b''(X')\deleted{\unsure{(X)}}=\varepsilon_b\circ X'\).

Ceci se généralise au cas où on se donne \(M\in\mathrm{Ob}\widehat B\), quand on considère
\[\varepsilon_M:B^\wedge\longrightarrow\mathrm{Ens},\qquad G\mapsto\varepsilon_M(G)=\mathrm{Hom}(M,G)\]
considérons donc, pour \(X'':A^o\longrightarrow B^\wedge\) variable
\diagram{\begin{tikzcd}
\Gamma_M'':X''\arrow[r,mapsto]\arrow[d,phantom,"\in"{rotate=90}]&\varepsilon_M\circ\unsure{\Gamma_M''}\\
\underline{\mathrm{Hom}}(A^o,B^\wedge)&
\end{tikzcd}}
je dis qu'on a, revenant à \(X\in\mathrm{Ob}(A\times B)^\wedge\) variable
\[\Gamma_M^{\unsure{''|'}}(X)\simeq p_{B*}\underline{\mathrm{Hom}}(p_A^*(M),X))\]
\margin{fonctoriel en \(M,X\)}
Pour le voir, \deleted{considérons} il faut un iso
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\mathrm{Hom}_{A^\wedge}(a,\Gamma_M''(X))\arrow[r,phantom,"\simeq"]\arrow[d,phantom,"\parallel"]&\mathrm{Hom}_{A^\wedge}(a,p_{B*}\underline{\mathrm{Hom}}(p_A^*(M),X))\arrow[d,phantom,"\wr"]\\
\deleted{\mathrm{Hom}(}\Gamma_M''(X)(a)\arrow[d,phantom,"\parallel"]&\mathrm{Hom}_{(A\times B)^\wedge}(p_B^*(a),\underline{\mathrm{Hom}}(p_A^*(M),X))\arrow[d,phantom,"\wr"]\\
\mathrm{Hom}_{B^\wedge}(M,\underbrace{\unsure{X''}(a)}_{\begin{gathered}\parallel\\\deleted{\unsure{A}}p_{A*}(\unsure{\underline{\mathrm{Hom}}}(p_B^*(a),X))\end{gathered}})\arrow[d,phantom,"\parallel"]&\mathrm{Hom}_{\unsure{A\times B^\wedge|(A\times B)^\wedge}}(p_B^*(a)\times p_A^*(M),X)\arrow[ddl,bend left=25,leftrightarrow]\arrow[ddl,bend left=35,leftrightarrow]\\
\mathrm{Hom}_{(\unsure{A}\times B)^\wedge}(p_A^*(M),\underline{\mathrm{Hom}}(p_B^*(a),X))\arrow[d,phantom,"\parallel"]&\\
\mathrm{Hom}_{(A\times B)^\wedge}(p_A^*(M)\times p_B^*(a),X)&
\end{tikzcd}}
\margin{fonct\unsure{\({}^{\mathrm{el}}\)} en \(M,X,a\)\qquad OK !}
\mspage{5}
"""
elements=[('text','top','b'),('text','top','On a une troisième interprétation'),('display','upper','Hom_(A×B)^hat cancelled'),('display','upper','(A×B)^hat≃Hom(A^o,B^hat)'),('text','upper','et considérant'),('display','upper','ε_b:B^hat→Ens'),('text','upper middle','alors Γ_b″'),('text','middle','Ceci se généralise'),('display','middle','ε_M:B^hat→Ens'),('text','middle','considérons donc'),('diagram','middle','Γ_M″:X″↦ε_M∘Γ_M″'),('text','middle lower','je dis qu’on a'),('display','middle lower','Γ_M″(X)≃p_B*Hom'),('text','lower','Pour le voir'),('diagram','lower half','two chains of Hom identifications; two curved arrows'),('text','foot','5')]
if __name__=='__main__':save(107,6,tex,elements,notes='Generalizes evaluation from b to arbitrary M∈B^hat and verifies the formula through two chains of adjunctions and symmetry, ending “OK !”. Draft has inconsistent or overwritten primes in X′/X″ and Γ_M′/Γ_M″; literal Γ_M″ on the mapping target has a doubt mark. Letter b at top, 5 at foot. Top replacement and struck formula require renewed audit; no context used.')
