from audit_tools import *
old=r'''\[
\gamma^p:\ J\xrightarrow[\text{degré }p]{}J\qquad p\geq1
\]'''
new=r'''\figure{\begin{tikzpicture}
\node (source) at (0,0) {$\gamma^p:\ J$};
\node (target) at (3,0) {$J$};
\draw[->] (source.east)--(target.west);
\node[anchor=west] at (3.6,0) {$p\geq1$};
\draw (1.1,.14) .. controls (1.05,-.5) and (1.35,-.55) .. (1.65,-.58);
\node[anchor=west] at (1.75,-.6) {degré $p$};
\end{tikzpicture}}'''
finish(334,replacements=[(old,new)],changes=[change('degree-p callout beneath gamma map','degree label under arrow','degree annotation','degree label with curved headless callout','A separate curved stroke descends from the arrow shaft and turns right toward the degree-p label.','drawing or diagram',True,True,'high','page')],note='Reread both halves against the full text. Added the curved headless callout leading from the gamma map toward degré p. Confirmed the cancellation of ab. groupe, the inserted k-, the with/without1 distinction, the unclosed action parenthesis, all six divided-power lines and the index-order slip in the last line. The top exclamation mark and question mark are both present.',doubts=[additional_doubt('right-margin transport word',r'\unsure{transf.|transportant}',confidence='low',evidence='The faint connected ending does not distinguish abbreviation from the longer word.'),additional_doubt('relation introduction',r'\unsure{Je trouve la relation|Je donne la relation}',confidence='low',evidence='Thin linked cursive strokes leave the verb open.'),additional_doubt('crossed initial letter',r'\unsure{F}',confidence='low',evidence='Repeated cancellation strokes obscure the initial letter.'),additional_doubt('crossed word above gamma map',r'\unsure{propre}',confidence='low',evidence='Only the outer word outline survives clearly beneath the horizontal cancellation.')])
