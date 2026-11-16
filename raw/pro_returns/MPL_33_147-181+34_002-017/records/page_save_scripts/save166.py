import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,166,r'''\scanpage{166}
\uline{Sujets de recherches}

a) $\bigwedge^i$ dans catégories dérivées, $\lambda$-anneaux et structures annexes

\diagram{$\left\{\begin{array}{ll}
\text{b)}&\text{Dualité analytique}\\[1em]
\text{c)}&\text{Descente cohomologique et}\\
&\text{applications (finitude}\\
&\text{analytique et algébrique ....)}
\end{array}\right.$}

\diagram{$\left\{\begin{array}{ll}
\text{d)}&\text{Künneth pour complexes}\\
&\text{quasi-cohérents}\\[1em]
\text{e)}&\text{Dualité pour les complexes}\\
&\text{alg. différentiels, et}\\
&\text{site stratifiant ----}
\end{array}\right.$}

\figure{\begin{tikzpicture}\draw (0,0) .. controls (3,.12) and (7,.3) .. (10,.28);\end{tikzpicture}}

f) \deleted{Profondeurs cohomologiques et homotopiques, et ths de Lefschetz locaux et globaux.}

\figure{\begin{tikzpicture}\draw (0,.3)--(2.5,.36);\draw (.15,.15)--(2.3,.16);\draw (.35,0)--(2.45,-.04);\end{tikzpicture}}
\margin{165}
''',[
('text','heading','Sujets de recherches'),('text','upper','a) exterior powers in derived categories'),('text','upper middle','b) Dualité analytique'),('text','middle','c) Descente cohomologique'),('diagram','left group b-c','brace grouping b and c'),('text','middle','d) Künneth pour complexes'),('text','middle lower','e) Dualité pour les complexes'),('diagram','left group d-e','brace grouping d and e'),('drawing','below e','horizontal separator'),('text','lower','f)'),('deletion','lower','Profondeurs cohomologiques et homotopiques'),('drawing','bottom centre','three short horizontal rules'),('margin note','bottom left','165')],remarks='Whole and both halves read. Braces explicitly group b–c and d–e; they are retained as array diagrams, with every word. Item f is cancelled by diagonal strokes. The four dashes and four dots are original. This is an agenda/title-like sheet but classified text because the list is substantive.')
