import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(34,r"""\scanpage{34}
En fin de partie

noir a $\rho$ groupements solidaires \inserted{$G_i$} (avec chacun
$\unsure{\gamma_i|y_i}\geq2$ yeux

blanc : $\rho'$ groupements solidaires \inserted{$G'_j$} ($\ldots$ $\unsure{\gamma'_j|y'_j}\geq2$)

\deleted{Si blanc joue dernier ($\varepsilon=0$) alors les $\rho'$
groupements ont chacun exactement 2
yeux, donc $\unsure{T'|t'}=2\rho'$}

Si $t-2\rho\leq t'-2\rho'$
alors c'est blanc qui joue le dernier
(i.e. $\varepsilon=0$, i.e. $D=d$)

Si $t'-2\rho'<t-2\rho$,
c'est noir qui joue le dernier
(i.e. $\varepsilon=1$, i.e. $D=d-1$)
\mspage{33}
""",'text', [('text','upper-right','En fin de partie'),('display','upper-right','rho groupements solidaires'),('text','right crossed box','Si blanc joue dernier'),('display','middle-right','t-2rho <= t prime-2rho prime'),('display','lower-right','t prime-2rho prime < t-2rho'),('marginalia','bottom-centre','33')], observations='Go terminal-move criterion in terms of territory and counts of solidary groups; a stronger statement assigning exactly two eyes to each white group is crossed out. Left half contains no legible source text apart from overlap and page number.')
