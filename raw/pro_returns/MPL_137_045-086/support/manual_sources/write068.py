import sys
sys.path.insert(0,'MPL_137_045-086/support')
from record import save
text=r'''\scanpage{68}
% archive foliation: 67
Comme \uline{donnée}, c'est un hom de bifoncteurs
\[
F(X)\otimes F(Y)\longrightarrow F(X*Y)
\]
or il suffit de se le donner sur la sous catégorie \inserted{$k$-lin} $\unsure{I\times I|\mathcal I\times\mathcal I}$ \inserted{de $K\times K$} (des $C^i\times C^j$) (avec sa structure $k$-lin) donc de se donner des hom de bicomplexes de cochaînes

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
F(C^\bullet) \arrow[d,equal] & \otimes_B & F(C^\bullet) \arrow[d,equal] \arrow[r] & F(C^\bullet*C^\bullet) & \text{dans }B^{\bullet\bullet}\\
C^\bullet && C^\bullet
\end{tikzcd}}

ce qui \unsure{en termes} explicites, si $C^i\deleted{\otimes}\inserted{*}C^j$ correspond au \inserted{\unsure{bi}}complexe de chaînes \inserted{\unsure{fini de}}
\[
C_\bullet^i*C_\bullet^j=\deleted{\unsure{\text{cf. DP}}}\mathrm{DP}.\left(\underset{\Lambda^{i+1}\unsure{\Phi_*|\varphi_*}\otimes\Lambda^{j+1}\Phi_*}{\underbrace{C_*^i\otimes C_*^j}}\right)
\]

\margin{\unsure{Le cas où} $B=\unsure{Ab_k}$}

\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\unsure{(1)} & F(C^i) \arrow[d,equal] & \otimes_B & F(C^j) \arrow[d,equal] \arrow[r] & \operatorname{Hom}_k^\bullet\bigl((C_\bullet^i*C_\bullet^j)^\vee,C^\bullet\bigr)\\
& C^i && C^j & \underset{\unsure{C_i^\bullet*C_j^\bullet}}{\underbrace{\phantom{(C_\bullet^i*C_\bullet^j)^\vee}}}
\end{tikzcd}}
i.e.
\[
\unsure{(2)}\qquad (C^i\otimes_B C^j)\otimes_k
\underbrace{\overbrace{(C_i^\bullet*C_j^\bullet)}^{\text{déf}\ \unsure{C_{ij}^{\bullet}|C_{ij}^{\bullet\bullet}}}}_{\in K^\bullet}
\longrightarrow C^\bullet
\]
avec compatibilité aux op. diff. pour $i,j$ variables.

On peut aussi l'écrire
\[
\deleted{(C^i\otimes_B C^j)\otimes_k}
\]
\[
(1^*)\qquad C^i\otimes_B C^j\longrightarrow
\operatorname{Hom}_k^*\left(\underbrace{C_i^*\otimes C_j^*}_{\Lambda^{i+1}\Phi^*\otimes\Lambda^{j+1}\Phi^*},\underset{=\mathrm{DP}^*(C^\bullet)}{C^*}\right)
\]
ou encore
\[
(2^*)\qquad (C^i\otimes_B C^j)\otimes_k
\underbrace{(\Lambda^{i+1}\Phi^*\otimes^*\Lambda^{j+1}\Phi^*)}_{\unsure{C_{ij}^{*}|C_{ij}^{\bullet}}}
\xrightarrow{u^{ij}}C^*
\]'''
e=[('text','top','Comme donnée c’est un hom de bifoncteurs'),('display','top','F(X)⊗F(Y)→F(X*Y)'),('text','upper','or il suffit de se le donner'),('insertion','upper','k-lin'),('insertion','upper','de K×K'),('diagram','upper middle','F(Cbullet)⊗B F(Cbullet)→F(Cbullet*Cbullet)'),('text','middle','ce qui en termes explicites'),('deletion','middle','⊗ between Ci and Cj'),('insertion','middle','*'),('insertion','middle','bi'),('insertion','middle','fini de'),('display','middle','Cibullet*Cjbullet=DP.(Ci*⊗Cj*)'),('deletion','middle display','cf. DP'),('margin note','left middle diagonal','Le cas où B=Abk'),('diagram','middle/lower','F(Ci)⊗B F(Cj)→Homkbullet((Cibullet*Cjbullet)dual,Cbullet)'),('text','lower middle','i.e.'),('display','lower middle','(Ci⊗B Cj)⊗k(Cibullet*Cjbullet)→Cbullet'),('text','lower','avec compatibilité aux op. diff.'),('text','lower','On peut aussi l’écrire'),('deletion','lower','(Ci⊗B Cj)⊗k'),('display','bottom','(1*) Ci⊗B Cj→Homk*(Ci*⊗Cj*,C*)'),('text','bottom','ou encore'),('display','bottom','(2*) (Ci⊗B Cj)⊗k(Λi+1Φ*⊗*Λj+1Φ*)→C*')]
save(68,text,e)
