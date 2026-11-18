from save_page import save
text=r'''
\scanpage{30}
% archive foliation: 29
\margin{\unsure{Copies pédagogiques}\\\unsure{Matériau}}
\deleted{Pourtant, soit $X$}

Il revient au $=$ de dire que pour $(X_j)_{j\in J}$ et $Y$ dans $(\mathrm{Cat})$, si \inserted{$X=\coprod X_j$}
\[
\operatorname{Hom}_{\mathrm{Hot}}(\deleted{\unsure{\Phi}(}X),\deleted{\unsure{\Phi}(}Y))\longrightarrow\prod_{j\in J}\operatorname{Hom}_{\mathrm{Hot}}(X_j,Y)
\]
est bijectif. Mais avec le calcul des fractions, ni l'i\deleted{\unsure{bije}}\unsure{n}jectivité ni la surjectivité n'est claire, elles auraient l'air plutôt fausses, pour les $=$ raisons. C'est quand $=$ bien gênant! \deleted{\unsure{?}}

$a)$ Il se pourrait que pour des \deleted{\unsure{Dém}} éléments des seconds $\unsure{\mathrm m^{\mathrm b}|=^{\mathrm b}}$ $(\varphi_j)_{j\in J}$, il n'existe pas de $(Y\longrightarrow Y')\in W$ \uline{commun pour tous les} $\varphi_j$, tels que
\diagram{\begin{tikzcd}[column sep=large]
X_j\arrow[r,dashed,"\varphi_j"]&Y
\end{tikzcd}}
se représente par
\diagram{\begin{tikzcd}
X_j\arrow[r,"f_j"]&Y'
\end{tikzcd}}
À priori, on aura $Y\lhook\joinrel\longrightarrow Y'_j$ (imm. fermée si on veut), mais \unsure{quand} $=$ par le \unsure{thm.} des \unsure{passages}: les limites, prises par parties finies
'''
elements=[
('margin note','top right','Copies pédagogiques; Matériau'),
('deletion','top left','Pourtant, soit X'),
('text','upper','Il revient au = de dire que'),
('insertion','left below family','X = coproduct X_j'),
('display','upper middle','Hom_Hot(X,Y) → product Hom_Hot(X_j,Y)'),
('deletion','within Hom before X','Phi('),
('deletion','within Hom before Y','Phi('),
('text','middle','est bijectif. Mais avec le calcul'),
('deletion','within injectivité','bije'),
('deletion','after gênant','?'),
('text','lower middle','a) Il se pourrait que'),
('deletion','left of éléments','Dém'),
('diagram','lower','X_j dashed phi_j Y'),
('text','lower','se représente par'),
('diagram','lower','X_j → f_j Y prime'),
('text','foot','À priori, on aura Y hook Y prime_j'),
]
save(30,text,'text',elements,'The author challenges injectivity and surjectivity of the coproduct comparison and considers a common target for fractions. Several cancellation layers and the final abbreviated sentence are insecure; they are marked in place. The equal-like shorthand in prose is rendered by = without expanding it. The small upper-right words may be unrelated reused-sheet writing. No proof checked.')
