import sys
sys.path.insert(0,'/workspace/scratch/481c6c017cf8/MPL_133/scripts')
from record_page import save
save(38,r"""\scanpage{38}
\[G/Z\]
\[p^\infty\operatorname{Cent}(G/Z)\]
\diagram{\begin{tikzcd}
\uline{\operatorname{Hom}}(\pi,Z)\\
G\arrow[u,"\unsure{\varphi}"]
\end{tikzcd}}
\[\deleted{\unsure{G}}\quad \underbrace{Z^{\unsure{1|\prime}}\times T}\]
\[\operatorname{Cent}(G/Z)\]
\[\deleted{\operatorname{Cent}(G/\unsure{\operatorname{Cent}})}\]
\[
\left\{\begin{array}{l}
\boxed{\operatorname{Cent}(\operatorname{Der}G)\quad\text{unipotent}}\\[5pt]
\deleted{\unsure{liné}}\quad\boxed{(G/Z)_{\mathrm{ab}}\quad\deleted{\text{\unsure{a-tori}}}\ \uline{\text{linéaire}}}\\[5pt]
\boxed{\operatorname{Cent}(G/Z)\quad\text{unipotent}}
\end{array}\right.
\]
\diagram{\begin{tikzcd}
\boxed{(\operatorname{Dér}G)_{\mathrm{ab}}\quad\text{unipotent ?}}\arrow[r]&\text{\unsure{voire|quasi} fini}
\end{tikzcd}}
\[\deleted{\operatorname{Der}G_{\mathrm{ab}}\unsure{\neq|=}\unsure{\operatorname{Div}}}\]
\mspage{37}
""",'text',[('display','top','G/Z'),('display','upper-left','p infinity Cent(G/Z)'),('diagram','upper-right','G to Hom(pi,Z)'),('display','upper-middle','Z times T'),('display','middle','Cent(G/Z)'),('display','middle cancellation','Cent(G/Cent)'),('display','middle boxed group','Cent(Der G) unipotent'),('display','middle boxed group','(G/Z) ab linéaire'),('display','lower boxed group','Cent(G/Z) unipotent'),('diagram','lower oval','(Der G) ab unipotent ?'),('display','lower cancellation','Der G ab'),('marginalia','bottom-left','37')],doubts=[('lower circled formula','oval enclosure','The oval source enclosure is represented by a box inside the diagram; the content and question mark are retained.','high')], observations='Scratch sheet juxtaposes unipotence of centres of derived groups and G/Z, linearity of (G/Z)ab, and asks whether (Der G)ab is unipotent, with a marginal possible stronger finite condition. These are source assertions/questions, not established results.')
