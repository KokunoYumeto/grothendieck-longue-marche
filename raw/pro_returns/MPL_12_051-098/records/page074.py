from save_page import save_page
save_page(74,r'''\scanpage{74}
% archive foliation: 73
\mspage{16}
Relations avec les pts \deleted{\unsure{d}} rationnels \inserted{et la cohomologie} des Variétés abéliennes sur un \deleted{corps de type fini} \inserted{schéma de type fini} ...

Soit $A_K$ VA sur corps $K$ de \uline{type fini} pour commencer. Alors $K$ est le corps de fonctions d'un schéma $S$ irréductible et régulier, de type fini sur $\mathbf{Z}$, \deleted{et} \inserted{tel que} $A_K$ provient d'un schéma abélien sur $S$.

De plus, on a
\[
A_K(K)=A(S)
\]
et on sait que c'est un \uline{groupe de type fini} par Mordell--Weil--Néron--Lang.

Soit $f:A\longrightarrow S$ la projection, et considérons le motif
\[
R^1\unsure{f^*|f_*}(\mathbf{Q}_{A^*}(\unsure{1|0}))\simeq\deleted{\unsure{H^1(A)|H_\ell(A)}}\inserted{T_{\mathrm{motif}}(A)}
\]
\inserted{[où $A^*$ est le dual de $A$]}
qui est un motif ct tordu sur $S$ \deleted{de} pur de poids $1$, qui redonne $A_K$ à isogénie près \deleted{sur $\unsure{K|\overline{K}}$} (sur $K$ ?) comme l'indiquent les conjectures de Tate.
''',[
('top left','text','16'),
('top','text','Relations avec les pts rationnels et la cohomologie'),
('upper middle','text','Soit A_K VA sur corps K'),
('middle','text','De plus, on a'),
('middle','display','A_K(K)=A(S)'),
('middle lower','text','et on sait que c’est un groupe de type fini'),
('lower','text','Soit f:A → S la projection'),
('lower','display','R^1 f^*(Q_{A*}(1)) ≃ T_motif(A)'),
('bottom','text','qui est un motif ct tordu')
],remarks='Whole and halves checked; lower realization formula enlarged. Superscript vs subscript star on f and overwritten twist are uncertain. Ink says poids 1 with no supplied minus sign. ct tordu reading also crosschecked against scan073.')
from pathlib import Path
p=Path(__file__).resolve().parents[1]/'pages/MPL_12_051-098_12_scan073.tex'
s=p.read_text(encoding='utf-8').replace(r'\unsure{et tordu}',r'\unsure{ct tordu|et tordu}')
p.write_text(s,encoding='utf-8')
from save_page import rebuild_doubts
rebuild_doubts()
