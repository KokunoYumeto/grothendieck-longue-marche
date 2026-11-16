from audit_page import audit
from pathlib import Path
p=Path('pages/MPL_36_002-052_36_scan052.tex');old=p.read_text();new=old
start=new.index('\\[\nH^1(A,')
end=new.index(r'\margin{\figure',start)
new=new[:start]+r'''\diagram{\begin{tikzcd}[column sep=small,row sep=small]
H^1(A,\unsure{A_G|G_A})\simeq H^1(S,G)\times & \underline{H^0(S,R^1f_*(G_A))}\arrow[d,phantom,"\rotatebox{90}{$\simeq$}"]\\
&\begin{gathered}\text{Classes à isom près de $G_A$-torseurs}\\\deleted{\unsure{fou}}\ \text{rigidi\uline{fiés} rel. à $e_A$}\end{gathered}\arrow[d,phantom,"\rotatebox{90}{$\simeq$}"]\\
&\begin{gathered}\text{Classes de \deleted{torseurs} $G_A$-torseurs}\\\text{rigidi\uline{fiables} rel. à $e_A$.}\end{gathered}
\end{tikzcd}}
'''+new[end:]
new=new.replace(r'\unsure{sous hyp. de}',r'\unsure{sous hyp. de|en hyp. de}')
new=new.replace(r'\unsure{A|B},A;G',r'\unsure{B|A},A;G')
new=new.replace(r'\arrow[u,"\unsure{i}"]',r'\arrow[u,phantom,"\unsure{\wr|i}"]')
audit(52,[(old,new)],notes='Whole final sheet and enlarged title and lower diagram reread. Integrated the H0 factor with its vertical identifications, eliminating the transcription duplicate and retaining the line beneath that factor. Lower Tors first argument reads B-like before A; the vertical curly sign is represented as an uncertain wr rather than supplying an arrowhead. Missing Ext superscripts and pr2 star remain unsupplied, and A_G remains the primary literal reading.')
