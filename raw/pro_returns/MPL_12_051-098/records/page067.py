from save_page import save_page
save_page(67,r'''\scanpage{67}
% archive foliation: 66
Notons le \uline{th. de dualité absolue} :

Soient $M$ et $M^*$ deux \inserted{(complexes de)} motifs sur $X$ (de type fini sur $\mathbf{Z}$), qui sont ``duals'' pour le \deleted{$\unsure{[|\xi}$} complexe de motifs dualisants \deleted{$\unsure{]|\xi}$} canonique --- [NB Si $X$ est régulier \inserted{partout} de dim $n$, alors c'est la dualité à valeurs dans \deleted{$\unsure{\mathbf{Q}(n)[2n]|\mathbf{Q}(n)[n]}$}\inserted{$\mathbf{Q}(n)[2n+1]$}\margin{shift}\deleted{\unsure{shift}}]

alors $R\Gamma_X(M)$ et $R_!\Gamma_X(M^*)$ \inserted{``\unsure{support pr}|sur $\mathrm{Spec}\,\mathbf{Z}$''} sont duals. Ici [Comme les coefficients sont \unsure{ess.} $\mathbf{Q}$\unsure{\}}, donc il n'y a pas de $\mathrm{Tor}$]

ceci revient aussi à la formule (cas régulier)
\[
\boxed{\begin{array}{lll}
H^i(X,M)&\text{dual de}&\mathrm{Ext}_!^{2n+1-i}(X;M,\mathbf{Q}(n))\\
H^i_!(X,M)&\text{dual de}&\mathrm{Ext}^{2n+1-i}(X;M,\mathbf{Q}(n))
\end{array}}
\]
Si $X$ propre sur $\mathrm{Spec}\,\mathbf{Z}$, inutile de mettre des $!$.

Moyennant le thm de dualité \uline{relative} pour motifs, cet énoncé revient au
''',[
('top','text','Notons le th. de dualité absolue'),
('upper','text','Soient M et M* deux motifs'),
('middle','display','Q(n)[2n+1] and cancelled Q(n) shift'),
('middle','text','alors RΓ_X(M) et R_!Γ_X(M*) sont duals'),
('middle lower','text','ceci revient aussi à la formule'),
('lower middle','display','H^i(X,M) dual de Ext_!^{2n+1-i}; H_!^i dual de Ext'),
('lower','text','Si X propre sur Spec Z'),
('bottom','text','Moyennant le thm de dualité relative')
],remarks='Whole image and halves read, upper corrections and Ici paragraph enlarged. Shift overwritten in the NB and redundant bracket-like glyphs are very uncertain. Final phrase continues beyond supplied page.')
