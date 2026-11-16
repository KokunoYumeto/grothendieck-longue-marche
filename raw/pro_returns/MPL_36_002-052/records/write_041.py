from save_page import save
tex=r'''
\scanpage{41}
\diagram{\begin{tikzcd}X\arrow[d]\\S\end{tikzcd}}
\[
\boxed{\underline{\mathcal H}^{1}(X/S;\underline{\operatorname{Hom}}_{S-gr}(\unsure{\gamma|\sigma},G))
\xrightarrow{\sim}\underline{\operatorname{Hom}}_{S-gr}(\gamma,\underline{\mathcal H}^{1}(X/S,G))}
\]
isom de foncteurs, \deleted{pour} quand tout est \uline{affine} sur $S$ (?)
\[
\boxed{\underline{\mathcal H}^{1}(X/S;\underline{\operatorname{Ext}}^{1}_{S-gr}(\gamma,G))
\simeq\underline{\operatorname{Ext}}^{1}_{S-gr}(\gamma,\mathcal H^{1}(X/S,G))}
\]
Sous quelles conditions ???

\[\unsure{P_X|\rho_X}\]
\diagram{\begin{tikzcd}[column sep=large]
X\arrow[d,no head]&\deleted{\unsure{\gamma_X}}&\deleted{\unsure{\gamma_X\times\gamma_X}}\\
S&\gamma&\gamma\times\gamma
\end{tikzcd}}
\[
\mathcal H^1(X/S,\underline{\operatorname{Hom}}_{S-gr}(\gamma,G))\longrightarrow
\operatorname{Hom}(\gamma,\mathcal H^1(X/S,G))
\]
\[
\mathcal H^1(X,\operatorname{Hom}(A;B))\simeq
\]
\margin{$\deleted{\unsure{\operatorname{Ext}_{X/S}|\operatorname{Ext}(X,B)}}$}
\diagram{\begin{tikzcd}[row sep=large]
H^1(X/S;\underline{\operatorname{Hom}}_{S-gr}(\gamma,G))\arrow[d]\\
\underline{\operatorname{Hom}}_{S-gr}(\gamma,H^1(X/S,G))
\end{tikzcd}}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)--(5.5,0);\draw (0,2.2)--(5.5,2.2);\draw (0,0)--(0,2.2);\draw (4.8,0)--(4.8,2.2);
\end{tikzpicture}}
\margin{40}
'''
e=[('diagram','upper left','X → S'),('display','top boxed','H¹(X/S; Hom)'),('text','below first box','isom de foncteurs'),('deletion','same sentence','pour'),('display','second box','H¹(X/S; Ext¹)'),('text','below second box','Sous quelles conditions ???'),('display','middle left','P_X'),('diagram','middle left','X; γ_X; γ_X×γ_X / S; γ; γ×γ'),('deletion','top row of small diagram','γ_X; γ_X×γ_X'),('display','lower middle','H¹(X/S, Hom) → Hom'),('display','below preceding','H¹(X, Hom(A;B)) ≃'),('margin note','left of bottom box','cancelled Ext'),('deletion','left of bottom box','Ext_{X/S}'),('diagram','bottom boxed','H¹ → Hom'),('drawing','around bottom diagram','rectangular enclosure with extended horizontal sides'),('margin note','bottom left','40')]
d=[{'line':'top display and recurring coefficient','reading':'γ','alternatives':'σ','confidence':'medium'},{'line':'middle isolated symbol','reading':'P_X','alternatives':'ρ_X','confidence':'low'},{'line':'crossed objects in small array','reading':'γ_X; γ_X×γ_X','alternatives':'overwritten upper parts obscure the first letters','confidence':'low'},{'line':'cancelled label beside lower box','reading':'Ext_{X/S}','alternatives':'Ext(X,B)','confidence':'low'},{'line':'Hom/Ext subscripts','reading':'S-gr','alternatives':'S-gp','confidence':'medium'}]
save(41,tex,e,d,'The two boxed comparison formulas and the question “Sous quelles conditions ???” are explicit open-condition questions. The affine hypothesis is itself followed by “(?)”; the lower repetition gives only an arrow. The middle abandoned H¹(X, Hom(A;B)) ≃ has no right-hand side and should not be completed. The bottom enclosure is recorded separately from its contents for geometry, not as a second mathematical formula.')
