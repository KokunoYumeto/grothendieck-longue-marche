import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from audit_tools import *
p=page(33,170);t=p.read_text()
a=t.index('\\margin{[i.e.');b=t.index('\\uline{N.B.}',a)
t=t[:a]+r'''\margin{(**)}
\margin{\diagram{\begin{tikzcd}[row sep=small]
\begin{gathered}
[\text{i.e. }\inserted{\exists N\text{ tel que }}\text{pour tt }\deleted{\unsure{G_P}}P\deleted{\in\operatorname{Ob}\underline{D}_c}\inserted{\text{faisceau}}\\
\text{constructible, }\operatorname{Ext}^i(P,G^{\bullet})=0\\
\text{pour }i>N]
\end{gathered}\arrow[d,leftrightarrow]\\
\text{fibres géom. }G^{\bullet}_{\bar{x}}\text{ est de dim. inj. finie}\\
\text{(pour les }A\text{-Modules)}
\end{tikzcd}}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)..controls(-.05,-.8) and (-.08,-1.9)..(.18,-2.8);
\end{tikzpicture}}
'''+t[b:]
t=t.replace(r'\underline{D}',r'\unsure{\underline{D}|D}')
p.write_text(t)
add_element(33,170,'drawing','left of first NB','faint curved grouping stroke')
audit(33,170,'Both halves and the definition/arrow placement checked. Removed the duplicated «pour i>N» by setting the definition and its geometric-fibre equivalence as a single marginal diagram. Preserved the absent opposite-category o in the fourth row, the unproved status in «Énoncés plausibles», and the expressly admitted equivalence (**). Restored the faint grouping stroke and marked ambiguous D baselines rather than identifying functor and category conventions by mathematical expectation.')
