from record_page import record
tex=r'''\scanpage{12}
% archive foliation: 11
$\Lambda^k(\Lambda^i\Phi_{*k})$ et $\Lambda^k(\Lambda^j\Psi_{*k})$ sont spéciaux
(\unsure{bien sûr, ils ne sont pas spéciaux}).

Leurs composantes sont évidemment
libres. De plus, comme $\Lambda^i\Phi_{*k}$ est
homotope à $0$, de même $\Lambda^k(\Lambda^i\Phi_{*k})$, et
leurs $\pi_n$ sont donc nuls et a fortiori
libres de \unsure{r.f.|t.f.}.
\margin{?}
]

\uline{Remarque}. Soit $L_\bullet$ $k$-module $\frac12$ simplicial
\deleted{\unsure{str.}} spécial, alors $L_\bullet$ est connu à isom. près,
i.e. les $\mu_i=\operatorname{rg}M_i$ $(i\geq1)$ et $\nu_j=\operatorname{rg}N_j$
\deleted{$j>0$} \inserted{$j\geq0$}
connus, quand on connaît la \deleted{\unsure{suite des}}
$n\longmapsto\operatorname{rg}_kL_n=f_{L_\bullet}(n)$,
\deleted{En effet} et les
$\operatorname{rg}_k\pi_j(L_\bullet)$ $(=\operatorname{rg}_kN_j=\nu_j)$.
En effet,
on aura
\[
\sum_{i\geq1}\mu_i\underset{\unsure{P_i(n+1)}}{\underbrace{\binom{n+1}{i}}}
=f_{L_\bullet}(n)-\sum_{j\geq0}\nu_j\binom{n}{j}
\qquad(n\text{ grand})
\]
\deleted{On en sait}
i.e.
\[
f_{L_\bullet}(n-1)-\sum_{j\geq0}\unsure{\nu_j|\beta_j}P_j(n-1)
=\sum_{i\geq1}\mu_iP_i(n)
\]
on sait que les \deleted{\unsure{$\binom{n}{i}$}} \inserted{$P_i(n)$}
sont des
\unsure{lin. indépendants} et $=$ forment une
base du $\mathbf Z$-module des polynômes
à \deleted{valeurs} \inserted{coeff. entiers} entières sur les entiers.
Donc la connaissance de $\sum_{i\geq1}\mu_iP_i$
pour $n$ grand implique
'''
record(12,tex,[('text','top continuation','Λ^k(Λ^iΦ_*k) et Λ^k(Λ^jΨ_*k) sont spéciaux'),('text','parenthesis','bien sûr, ils ne sont pas spéciaux'),('text','upper argument','Leurs composantes sont évidemment libres'),('margin note','left beside homotopy argument','?'),('text','closing bracket at right',' ] '),('text','middle heading','Remarque. Soit L k-module ½ simplicial'),('deletion','above spécial','str.'),('text','middle classification statement','L est connu à isom. près'),('deletion','after ν_j','j>0'),('insertion','above deleted index bound','j≥0'),('deletion','after connaît la','suite des'),('text','rank function','n↦rg_kL_n=f_L(n)'),('deletion','after rank function','En effet'),('text','homotopy ranks','et les rg_kπ_j(L)'),('display','lower middle','Σ μ_i binomial = f_L(n)−Σ ν_j binomial; n grand'),('insertion','under first binomial','P_i(n+1)'),('deletion','before i.e.','On en sait'),('display','lower','f_L(n−1)−Σ ν_j P_j(n−1)=Σ μ_i P_i(n)'),('text','lower prose','on sait que les ... sont des lin. indépendants'),('deletion','before sont des','binomial n i'),('insertion','above deleted binomial','P_i(n)'),('text','lower continuation','base du Z-module des polynômes'),('deletion','after à','valeurs'),('insertion','above valeurs','coeff. entiers'),('text','bottom','Donc la connaissance de Σ μ_iP_i pour n grand implique')],doubts=[('top parenthesis','bien sûr, ils ne sont pas spéciaux','initial words and negation faded, staff interference','low'),('homotopy paragraph','nuls; r.f.','t.f.; latter abbreviation faint','medium'),('Remarque','L connu à isom. près','staff lines obscure ends of words','medium'),('index bound correction','j>0 → j≥0','deleted > could be ≥','medium'),('two lower displays','P_i(n+1), ν_j / β_j, P_j(n−1)','several superposed strokes in new polynomial notation','low'),('last paragraph','lin. indépendants; et =','abbreviation and equivalence sign difficult','low'),('last paragraph correction','valeurs deleted; coeff. entiers inserted; entières','attachment of insertion and scope of deletion uncertain; no mathematical repair','low')],notation=[('polynomials associated to binomial coefficients',r'$P_i(n)$','scan 12; upright/hand capital P, locally uncertain'),('exterior-power indices',r'$\Phi_{*k},\Psi_{*k}$','scan 12; star followed by coefficient ring')])
