from pathlib import Path
R=Path(__file__).resolve().parents[1]
a=(R/'readers/008/A/reading.tex').read_text()
b=(R/'readers/008/B/reading.tex').read_text()
c=(R/'readers/008/C/reading.tex').read_text()
trace=r'''% Upper-right mottled trace: visible patches only; no character, hand or role assigned.
\margin{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[gray,line width=.7pt] (.10,.84) -- (.29,.83) -- (.34,.78);
\fill[gray] (.08,.84) circle(.028cm);
\draw[gray,line width=.5pt] (.37,.70) -- (.38,.63) -- (.43,.56);
\draw[gray,line width=.45pt] (.20,.65) -- (.21,.59);
\draw[gray,line width=.45pt] (.27,.50) .. controls(.32,.45) and(.40,.46) .. (.43,.49);
\draw[gray,line width=.65pt] (.13,.31) .. controls(.19,.42) and(.29,.43) .. (.36,.40);
\fill[gray] (.43,.12) circle(.023cm);
\draw[gray,line width=.4pt] (.43,.12) .. controls(.48,.14) and(.49,.19) .. (.48,.23);
\end{tikzpicture}}
'''
a=a.replace('\\scanpage{8}\n','\\scanpage{8}\n'+trace,1)
a=a.replace("et si $a=a_0a''$",r"et si $\overset{\unsure{\cdot|\prime}}{a}=a_0a''$")
# Complete parentheses and two diagonal paths, with right-hand placement.
start=a.index('\\begin{tikzpicture}[baseline=(u.base)]')
end=a.index('\\end{tikzpicture}',start)+len('\\end{tikzpicture}')
a=a[:start]+'\\begin{flushright}\n'+a[start:end]+'\n\\end{flushright}'+a[end:]
# Preserve the residual curves/dots beside the first lower cancelled continuation.
start=c.index('% Faint residual strokes')
end=c.index('\\end{tikzpicture}',start)+len('\\end{tikzpicture}')
res=c[start:end]
needle='\\end{tikzpicture}\\\\[.8ex]'
assert needle in a
a=a.replace(needle,'\\end{tikzpicture}\n\\quad\n'+res+'\\\\[.8ex]',1)
# Preserve the return arrow's detached point and explicit hooked head, retaining A's qualified tiny stroke.
start=b.index('\\fill ([xshift=.07cm,yshift=-.47cm]n.south east)')
end=b.index('\\end{tikzpicture}',start)
arrow=b[start:end]
old=r'\draw[->] ([yshift=-.25cm]n.south east) -- ++(.16,0) |- (n.north east);'
assert old in a
a=a.replace(old,arrow.rstrip())
# The phantom preserves the macro annotation while the actual cancellation is drawn.
a=a.replace(r'{$\rlap{$q$}\phantom{\deleted{q}}$};',r'{\rlap{$q$}\phantom{\deleted{$q$}}};')
p=R/'pages/J81-01_81_scan008.tex';p.write_text(a)
print(p)
