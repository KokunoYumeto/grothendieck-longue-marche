import sys
sys.path.insert(0,'MPL_31_002-051_work/scripts')
from save_page import save
text=r'''\scanpage{49}

et lorsque $i>n$, les \deleted{\unsure{deux}} $H^i(\unsure{\mathfrak g},U(\unsure{m|n}))$ sont nuls d'après b), \inserted{(car $U(\unsure{m|n})$ est fini)}, d'où résulte notre assertion.
\figure{\begin{tikzpicture}\draw (0,0)--(0,.35)--(2.5,.55)..controls (2.7,.55) and (2.8,.6)..(2.8,.75);\end{tikzpicture}}

Si enfin $G$ est \deleted{le groupe} un groupe linéaire unipotent connexe, on distingue deux cas

$1^\circ)$ Caractéristique nulle. Alors $G$ est $\simeq\bar k^n$ sur $\bar k$, donc aussi sur $k$ (en vertu de $H^1(k,\operatorname{Gl}(n))=0$).
Et comme $H^i(k,G_a)=0$ pour $i>0$, l'assertion est valable.

$2^\circ)$ Car. $p\ne0$. Alors on filtre $G$ par $G\supset pG\supset\cdots\supset p^{\unsure{\ell|k}}G=0$. On est ramené au cas où $pG=0$ (les groupes $p^iG$ sont \uline{définis sur $k$}).
\figure{\begin{tikzpicture}\draw (0,0)--(-.08,-.5);\draw (.07,.01)--(0,-.49);\end{tikzpicture}}
Mais, on sait qu'alors $G$ est $\simeq\bar k^{\unsure{n}}$ sur $\bar k$ donc \deleted{$\unsure{\simeq}$} aussi sur $k$ (car $H^1(k,\operatorname{Gl}(n))=0$), et on fait comme dans $1^\circ$.

Supposons que $k$ soit quelconque \ldots

\mspage{48}'''
elements=[('text','top','et lorsque i>n'),('deletion','top','deux'),('insertion','above d’où','car U(m) est fini'),('drawing','under insertion','bent insertion connector'),('text','upper','Si enfin G est'),('deletion','upper','le groupe'),('text','upper middle','1°) Caractéristique nulle'),('display','within paragraph','G est ≃ bar k^n'),('display','within paragraph','H1(k,Gl(n))=0'),('text','middle','Et comme Hi(k,Ga)=0'),('text','middle','2°) Car. p≠0'),('display','within paragraph','G superset pG ... p^ell G=0'),('text','middle','On est ramené au cas où pG=0'),('drawing','left middle','two short vertical marking strokes'),('text','lower middle','Mais, on sait qu’alors'),('deletion','before aussi','≃'),('text','last written line','Supposons que k soit quelconque ...'),('text','bottom left','48')]
save(49,text,elements,observations='Whole and both halves read; complete written area enlarged. The insertion car U(m) est fini is attached after d’après b), as indicated by its bent line. The word est before ≃ and the source’s unfinished final line are retained. The filtration exponent is visually ambiguous ell/k. The index U(m/n) is read consistently with scan048, with explicit doubt.')
