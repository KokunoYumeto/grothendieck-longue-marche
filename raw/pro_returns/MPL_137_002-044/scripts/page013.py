from record_page import record
tex=r'''\scanpage{13}
% archive foliation: 12
la connaissance des $\mu_i$.

Si on se donne les \inserted{entiers} $\nu_j\geq0$
\deleted{\unsure{$=\operatorname{rg}\pi_j(L_\bullet)$ $(j\geq0)$}}
$(j\geq0)$ et une fonction \inserted{polynomiale} $f(n)$ à valeurs
entières définie pour $n$ grand, à quelles
conditions existe-t-il $L_\bullet$ str. spécial
avec $\nu_j=\operatorname{rg}\pi_j(L_\bullet)$ $(j\geq0)$ et
$f(n)=f_{L_\bullet}(n)$ pour $n$ grand? Notons
que $g=f-\sum_{j\geq0}\nu_jP_j$ est encore une
fonction \deleted{entière} \inserted{polynomiale} à valeurs entières,
donc de la forme $\sum_{i\geq0}\mu_i\binom{n+1}{i}$
où $(\mu_i)\in\mathbf Z^{(\mathbf N)}$ est uniquement déterminé.
Alors la condition cherchée est
\[
\mu_0=0,\quad\mu_i\geq0\quad\text{si }i\geq1.
\]
Notons que \deleted{\unsure{$\mu_0$}}
\[
\mu_0=g(-1)=f(-1)-\sum_{j\geq0}\nu_j
\frac{(-1)(-2)\cdots(-j)}{j!}
\]
donc on a aussi
\[
(\mu_0=0)\Longleftrightarrow
\left(f(-1)=\underset{\chi((\nu_j))}{\underbrace{\sum(-1)^j\nu_j}}\right)
\]

\deleted{\unsure{Déf.}
\deleted{Complexes}
$k$-Modules $\frac12$ simpliciaux $L_\bullet$ \deleted{\unsure{parfaits}}
``\inserted{str.}\unsure{chaîne-parfait}''
\inserted{(strict. \unsure{chaîne-parfait})}
$=$ tels que $L^!_\bullet$ soit
un complexe de chaînes de $k$-modules
\deleted{\unsure{str.}}
parfait (str. parfait) $=$}
'''
record(13,tex,[('text','top continuation','la connaissance des μ_i'),('text','first paragraph','Si on se donne les ν_j≥0'),('insertion','above ν_j','entiers'),('deletion','after ν_j','=rgπ_j(L); (j≥0)'),('insertion','above fonction','polynomiale'),('text','first paragraph question','à quelles conditions existe-t-il L str. spécial'),('text','middle','Notons que g=f−Σν_jP_j'),('deletion','after fonction','entière'),('insertion','above entière','polynomiale'),('text','middle expansion','donc de la forme Σ μ_i binomial'),('text','middle continuation','où (μ_i)∈Z^(N) est uniquement déterminé'),('display','middle','μ_0=0, μ_i≥0 si i≥1'),('deletion','after Notons que','μ_0'),('display','below middle','μ_0=g(−1)=f(−1)−Σν_j(−1)…(−j)/j!'),('text','between displays','donc on a aussi'),('display','lower equivalence','μ_0=0 iff f(−1)=Σ(−1)^jν_j'),('insertion','below alternating sum','χ((ν_j))'),('deletion','bottom cancelled definition block','Déf; k-Modules ½ simpliciaux; chaîne-parfait'),('deletion','inside cancelled block','Complexes; parfaits; str.'),('insertion','inside cancelled block','str.; (strict. chaîne-parfait)')],doubts=[('first paragraph deleted formula','=rgπ_j(L), (j≥0)','heavy blue overwrite','low'),('polynomial correction','entière → polynomiale','position of insertion relative to fonction uncertain','medium'),('integer sequence exponent','Z^(N)','N handwritten with crossed strokes','medium'),('Notons que deleted mark','μ_0','overwritten digit or sign follows','low'),('bottom cancelled definition','Déf.; chaîne-parfait; strict. chaîne-parfait','multiple diagonal strikes and revisions; exact adjective endings doubtful','low'),('bottom cancelled definition','parfaits; str.','earlier rejected adjective faint','low')],notation=[('Euler-characteristic sign',r'$\chi((\nu_j))$','scan 13; below alternating sum'),('associated chain complex',r'$L^!_\bullet$','scan 13 cancelled definition; exclamation dot visible'),('coefficient sequence with finite support',r'$\mathbf Z^{(\mathbf N)}$','scan 13')])
