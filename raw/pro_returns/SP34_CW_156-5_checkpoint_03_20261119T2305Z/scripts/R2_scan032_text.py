from pathlib import Path
root=Path('/workspace/scratch/4770596940a0')
s=(root/'source/SP34_CW_156-5_witnesses/codex/J156-5-04/pages/J156-5-04_156-5_scan032.tex').read_text()
def change(a,b):
 global s
 assert a in s,a
 s=s.replace(a,b,1)
change(r'\deleted{\unsure{Reste}}',r'\deleted{Reste}')
change(r'\inserted{\unsure{$G$|$\in$}}',r'\inserted{$G$}')
change(r'\deleted{\unsure{On}}',r'\deleted{On}')
# Small lower curved mark below the difference sign: reproduce its strokes without assigning a letter value.
hook=r'''\mathbin{\underset{\begin{tikzpicture}[x=1ex,y=1ex,baseline=0pt]
\draw[line width=.45pt,line cap=round] (.30,.65) .. controls (.38,.36) and (.12,.18) .. (0,0);
\draw[line width=.45pt,line cap=round] (.16,.45)--(0,0)--(.20,0);
\end{tikzpicture}}{\setminus}}'''
change("$A\\in F\\setminus G'\\subset F'$", "$A\\in F"+hook+"G'\\subset F'$")
change(r'\margin{\unsure{Ultra} faux}',r'\margin{Ultra faux}')
change(r'\unsure{Le|La}', 'Le')
change(r'\unsure{parmi|pour}', 'parmi')
change(r'\uline{\unsure{impliquées}}',r'\uline{impliquées}')
change(r'\unsure{lesquelles|laquelle}', 'lesquelles')
change(r'\unsure{précédemment}',r'\unsure{précédemment|précédemment\textsuperscript{\#}}')
# The long curve crosses successive lines. Cancellation is preferred, but the grouping-stroke alternative remains in the report.
long_start=r'\margin{les conditions '
change(long_start,r'\margin{\deleted{les conditions ')
change(r"d'impliquer a)}",r"d'impliquer a)}}")
s=s.replace('% @ centre left, long oblique note','% @ centre left, long oblique note; probably cancelled by the long curved stroke, function uncertain')
change(r"L'application \unsure{can.}",r"L'application can.")
# The E-like angular mark lies below qui. Keep the graphic and the word together without assigning it a lexical value.
qmark=r'''\begin{tikzpicture}[x=1ex,y=1ex,baseline=(q.base)]
\node[anchor=base west,inner sep=0pt] (q) at (0,0) {qui};
\begin{scope}[shift={(-.15,-1.5)},scale=.7]
\draw[line width=.45pt,line cap=round] (0,.62)--(.03,0)--(.51,.02);
\draw[line width=.40pt,line cap=round] (.20,.17) .. controls (.30,.23) and (.40,.25) .. (.54,.24);
\draw[line width=.18pt,line cap=round] (.12,.56) .. controls (.28,.62) and (.39,.58) .. (.52,.55);
\draw[line width=.35pt,line cap=round] (.35,.95)--(.40,.73);
\end{scope}
\end{tikzpicture}'''
change("des subdivisions de $F$ qui induisent", "des subdivisions de $F$ "+qmark+" induisent")
oldNB=r"\margin{NB. c'est \unsure{tjrs|tojrs} surj. donc c'est l'\uline{injectivité} qu'il faut prouver ici}"
newNB=r"""\margin{\begin{tikzpicture}[baseline=(n.base)]
\node[anchor=north west,inner sep=0pt,text width=1.95cm,align=left] (n) at (0,0) {NB. c'est \unsure{tjrs|tojrs} surj. donc c'est l'\uline{injectivité} qu'il faut prouver ici};
\draw[line width=.35pt] ([xshift=-.13cm]n.north west)--([xshift=-.13cm,yshift=.08cm]n.south west) .. controls ([xshift=-.13cm,yshift=.03cm]n.south west) .. ([xshift=-.18cm]n.south west);
\end{tikzpicture}}"""
change(oldNB,newNB)
oldc=r"c) \deleted{Les strates ouvertes de $F'$ qui ne sont} $\forall A\in F\setminus G$, $A^\circ$ est une strate ouverte de $F'$."
newc=r"c) \deleted{Les strates ouvertes de $F'$ qui ne sont} \inserted{$\forall A\in F\setminus G$, $A^\circ$ est une strate ouverte de $F'$}."
change(oldc,newc)
change(r'\uline{Dém} \deleted{\unsure{On}} \unsure{On} va prouver \unsure{p. ex}',r'\uline{Dém} On va prouver p. ex')
change(r'\deleted{\uline{\unsure{Dém}}}',r'\deleted{\uline{Dém}}')
change(r'\unsure{inclusion}', 'inclusion')
change(r'\inserted{\unsure{can.}',r'\inserted{can.')
(root/'out/readers/R2/scan032.tex').write_text(s)
print('written',len(s),'characters')
