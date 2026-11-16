import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,158);t=p.read_text()
t=t.replace(r'(\unsure{donnant} : la \unsure{multiplication} à un \unsure{signe})',r'(\unsure{commutant|donnant} \unsure{à|:} la \unsure{permutation|multiplication} à un \unsure{signe})')
a=t.index('\\[\n');b=t.index("\\deleted{un élément",a)
t=t[:a]+r'''\diagram{\begin{tikzcd}[column sep=small,row sep=large]
\mathrm{R}\mathcal{H}om(\mathrm{pr}_1^*(F_\bullet),\mathrm{pr}_2^!(G_\bullet))\times\arrow[d,no head,bend left=25]
&\mathrm{R}\mathcal{H}om(\mathrm{pr}_2^*(G_\bullet),\mathrm{pr}_1^!(F_\bullet))\arrow[r]\arrow[d,no head,bend left=35]
&K_{X\times_S Y}^{\bullet}\\
\deleted{\text{D'où, pour }\xi^0\in\mathrm{R}^0\Gamma_{X\times_S Y}(\quad)}
&\deleted{\text{et }\eta^0\in\mathrm{R}^0\Gamma_{X\times_S Y}(\quad)}&
\end{tikzcd}}
'''+t[b:]
t=t.replace(r'\margin{si on représente',r'''\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (.25,1.4)..controls(.45,1.1) and (.25,.9)..(.2,.5)..controls(.15,.2) and (.05,.1)..(0,0)..controls(.18,-.1) and (.18,-.45)..(.2,-.8)..controls(.23,-1.15) and (.17,-1.3)..(.35,-1.5);
\end{tikzpicture}}
\margin{si on représente''')
p.write_text(t)
add_element(33,158,'diagram','upper formula and cancelled following line','two curved connectors from pairing factors to empty arguments')
add_element(33,158,'drawing','lower right','curly bracket beside finite-flat-complex annotation')
audit(33,158,'Both halves and enlarged top/bottom passages re-read. The initial parenthesis remains low confidence, with permutation and commutant offered as letter-based alternatives. Reproduced the two curved connector lines into the cancelled formula instead of misreading them as backslashes inside its empty parentheses, and restored the lower annotation bracket. Retained the repeated right member of the eta equation, the visibly different P/Q versus F/G readings, and the overwritten functor names as doubtful.')
