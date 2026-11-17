from workflow import save_page
save_page(72,r'''
\scanpage{72}
% archive foliation: 71
de $X_i$ suivant les points à l'infini\ldots).

Cl. que $\widehat X_i$ est automatiquement $\omega$-orienté, donc aussi
\[
\widehat X=\coprod\widehat X_i
\]
De cette façon, la catégorie envisagée (des surfaces topologiques ``spéciales'' $\omega$-orientées \inserted{avec homéomorphismes $\omega$-orientés}) devient équivalente à celle des surfaces topologiques \inserted{$\omega$-orientées} à comp. conn. compactes \uline{munies} d'une partie \deleted{\unsure{f}} $S$ discrète, avec les isom. de couples $(\widehat X,S)$.

De $\overline{\mathrm m}$, la catégorie des couples \deleted{$\unsure{(X,S)|(X,o,S)}$} $(X,o,\unsure{\mathcal J|J})$ avec $(X,o)$ comme dessus ($o$ la $\omega$-orientation) et $\mathcal J$ partie discrète de $X$, est équiva-\\
lente à celle des systèmes $(\widehat X,o,S,\mathcal J)$, où $(\widehat X,o)$ est une surface $\omega$-orientée à comp. conn. compactes,
''',[
('text','top','de X_i suivant les points à l’infini ...'),
('text','upper quarter','Cl. que Xhat_i est automatiquement omega-orienté, donc aussi'),
('display','upper third','Xhat=coproduct Xhat_i'),
('text','middle','De cette façon, la catégorie envisagée ...'),
('insertion','above closing parenthesis','avec homéomorphismes omega-orientés'),
('insertion','above surfaces topologiques in target category','omega-orientées'),
('deletion','before S discrète','f'),
('text','lower half','De m, la catégorie des couples (X,o,J) ... systèmes (Xhat,o,S,J)'),
('deletion','lower half before (X,o,J)','(X,S) or (X,o,S)')])
