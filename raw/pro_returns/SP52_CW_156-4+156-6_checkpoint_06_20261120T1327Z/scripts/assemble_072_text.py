"""Root assembly after all three independent returns and direct crop adjudication."""
from pathlib import Path
O=Path(__file__).resolve().parents[1]
a=(O/'readers/156-4_072/R1/reading.tex').read_text()
b=(O/'readers/156-4_072/R2/reading.tex').read_text()
# R1 supplies the definition, the correction placement and the literal marginal link.
top=a[:a.index('% R1-FIG-C6:')]
top=top.replace(r'\rlap{\deleted{\mathcal F}}',r'\rlap{$\deleted{\mathcal F}$}')
top=top.replace(r'\unsure{\deleted{tout}|tout}',r'\unsure{tout|\deleted{tout}}')
top=top.replace(r'\unsure{satisfait|satisfont}',r'\unsure{satisfont|satisfait}')
start=top.index('% R1-FIG-A:');end=top.index('% slanted left margin;',start)
parta=r'''% fig-a-insertions: correspond joins the physical line-end hyphen under convention 7; both insertion arms remain.
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node[anchor=west] at (0,0) {a) fermé pour $\leq$, et stable par sup quelc.};
\node[anchor=west] at (0,-.75) {pour $\leq$ [et à ce titre, s'en correspond,};
\node[anchor=west] at (1.5,-1.9) {aux parties fermées};
\node[anchor=west] at (6.9,-1.9) {de $M$,};
\node[anchor=west] at (1.6,-1.25) {\inserted{par $\mathcal F'\mathrel{\vdash\joinrel\dashv}\mathcal F'\cap M$,}};
\node[anchor=west] at (6.7,-1.25) {\inserted{$M'$}};
\draw[line width=.45pt] (1.45,-2.14) .. controls (1.15,-1.67) and (1.37,-1.58) .. (1.7,-1.58) -- (5.3,-1.54) .. controls (5.5,-1.52) and (5.62,-1.50) .. (5.78,-1.43);
\draw[line width=.45pt] (6.8,-2.02) .. controls (6.72,-1.77) and (7.02,-1.58) .. (7.42,-1.44);
\node[anchor=west] at (0,-2.8) {par $M'\unsure{\mathrel{\mapstochar\relbar}|\mathrel{\vdash\joinrel\dashv}|\mapsto}\mathcal F'=\{F\in\mathcal F\mid\overline F\subset M'\}$].};
\end{tikzpicture}}

'''
top=top[:start]+parta+top[end:]
top=top.replace('% slanted left margin; the last parenthesis is not securely framed by the one crop.','% slanted left margin; the terminal close is covered by root crop a05.')
top=top.replace(r'\unsure{(condition large)|(condition lge)}',r'\unsure{(condition lge)|(condition large)}')
# R2 supplies the compact C6 geometry, including all three detached points.
c6=b[b.index('% diagram: C6-group.'):b.index('\nOn dit que')]
c6=c6.replace(r'\unsure{de|dans|ds} $\mathcal F$',r'de $\mathcal F$')
c6=c6.replace(r'\unsure{symétrique|symetrique}',r'sym\unsure{e|é}trique')
c6=c6.replace(r'les \unsure{strates|str.tes} de',r'les \unsure{str.tes|strates} de')
c6=c6.replace(r'\unsure{\deleted{s}|s}tr\unsure{a|.}tes',r'\unsure{\deleted{S}|S|s}tr\unsure{a|.}tes')
c6=c6.replace(r'\unsure{G_m|G_n|G}',r'\unsure{G_n|G_m|G}')
c6=c6.replace(r'Ce \unsure{complément|complement} \unsure{servira}',r'Ce compl\unsure{\.{e}|é|e}ment servira')
# The bottom punctuation is kept as literal uncertain ink, not normalized to a comma or prime.
bottom=b[b.index('On dit que'):]
bottom=bottom.replace("$\\unsure{G|\\mathcal G}'$", "$\\unsure{G|\\rlap{$\\deleted{F}$}G|E}'$")
bottom=bottom.replace(r'\margin{sur la sous-figure $\unsure{G|\mathcal G}$ de $F$}',r'\margin{sur la sous-figure $\unsure{\rlap{$\deleted{F}$}G|G|E}$ de $F$}')
text=top+c6+'\n'+bottom
text=text.replace('R1-FIG-DEFINITION','fig-definition').replace('R1-FIG-B-CORRECTION','fig-b-correction').replace('R1-MARK-AFTER-M','fig-b-curled-mark').replace('R1-FIG-MARGINAL-C','fig-marginal-c').replace('R1-C-HEADLESS-LINK','fig-c-headless-link')
p=O/'pages/J156-4-09_156-4_scan072.tex'
p.write_text(text)
print(p, len(text.encode()), 'bytes')
