from audit_support import revise
old=r'''\diagram{\begin{tikzcd}[row sep=small,column sep=large]
\alpha'(C^i_*)\arrow[d,equal]&\alpha(C^{i+1}_*)\arrow[l,"\alpha'(d^i)"']\arrow[d,equal]\\
\unsure{(C'_i)^\bullet|K'_i}\arrow[r]&\unsure{(C'_{i+1})^\bullet|K'_{i+1}}\\
\vdots\arrow[d]&0\arrow[d]\\
k\arrow[d]&0\arrow[l]\arrow[d]\\
k\arrow[d]&k\arrow[l,"\mathrm{id}"']\arrow[d]\\
0\arrow[d]&k\arrow[l]\arrow[d]\\
0&0\\
\vdots&\vdots
\end{tikzcd}}'''
new=r'''\diagram{\begin{tikzcd}[row sep=small,column sep=large]
&\alpha'(C^i_*)\arrow[d,equal]&\alpha(C^{i+1}_*)\arrow[l,"\alpha'(d^i)"']\arrow[d,equal]\\
&\unsure{(C'_i)^\bullet|K'_i}\arrow[r]&\unsure{(C'_{i+1})^\bullet|K'_{i+1}}\\
&\vdots&\vdots\\
&0\arrow[d]&0\arrow[d]\\
&k\arrow[d]&0\arrow[l]\arrow[d]\\
i+1&k\arrow[d]&k\arrow[l,leftrightarrow,"\mathrm{id}"']\arrow[d]\\
i+2&0\arrow[d]&k\arrow[l]\arrow[d]\\
&0&0\\
&\vdots&\vdots
\end{tikzcd}}'''
revise(42,replacements=[(old,new),(r"\alpha'",r'\alpha^\bullet')],
doubts=[('central complex diagram, identity row','arrowheads visible at both ends','overwritten arrow direction','medium')],
notation=[('raised dot on alpha',r'\alpha^\bullet','Enlarged original at the first functor and the margin shows a filled point, not a slanted prime; shorter occurrences agree.')],
elements=[('display','central diagram left','i+1, i+2 degree labels; initial zero')],
note='Second audit of whole scan and enlarged original regions. Corrected alpha prime to alpha-dot from the filled point, without adding a dot where the manuscript omits it. Recovered initial zero and degree labels in the central complex diagram; retained both visible arrowheads on its overwritten identity arrow. The explicit on admettra assumption and final C-circle uncertainty remain.')
