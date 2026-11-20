"""Apply the main reader's crop decisions to the independent B source."""
from pathlib import Path
R = Path(__file__).resolve().parents[1]
s = (R/'readers/010/B/reading.tex').read_text()
a = (R/'readers/010/A/reading.tex').read_text()
s = s.replace('\\scanpage{10}\n', '\\scanpage{10}\n% Consolidated by root from three independent readings and seventeen adjudication crops.\n', 1)
start = s.index('\\node[inner sep=0pt] at (563,1026)')
end = s.index('\\end{minipage}};', start) + len('\\end{minipage}};')
s = s[:start] + s[start:end].replace(r'\unsure{\bullet|\circ}', r'\unsure{\circ|\bullet}', 1) + s[end:]
start = a.index('% Detached dark fragments beside the lower descending stroke; role uncertain.')
end = a.index('\\draw[opacity=.45]', start)
needle = '\\fill (1587,159) circle[radius=6.5];\n'
s = s.replace(needle, needle + a[start:end], 1)
start = a.index('\\filldraw[fill opacity=.10')
end = a.index('\\end{tikzpicture}}', start)
patch = '% Detached pale irregular patch; hand, origin and role remain undetermined.\n' + a[start:end]
needle = '% Two faint, angular lines at the foot, crossing the last graph and continuing at the right.\n'
s = s.replace(needle, patch + needle, 1)
s = s.replace(r'\draw[opacity=.13,line width=.4pt] (1436,1043) .. controls (1469,1009) and (1529,942) .. (1559,895);', r'''% Only the short supported course is reproduced; a farther upper continuation remains unresolved.
\node[anchor=north west,inner sep=0pt,outer sep=0pt] at (1438,978) {\unsure{\hbox{\begin{tikzpicture}[x=.0056cm,y=-.0056cm,line cap=round,color=black]
\path[use as bounding box] (1438,978) rectangle (1504,1039);
\draw[opacity=.13,line width=.4pt] (1444,1037) .. controls (1460,1018) and (1488,989) .. (1500,980);
\end{tikzpicture}}}};''')
s = s.replace(r'\draw[opacity=.16,line width=.4pt] (369,743) .. controls (379,750) and (386,763) .. (392,774);', r'''\draw[opacity=.16,line width=.35pt] (369,743) .. controls (379,751) and (390,762) .. (405,778) -- (415,786);
\draw[opacity=.25,line width=.4pt] (377,751)--(384,758) (390,764)--(393,767);''')
s = s.replace('% Pale detached marks; hand, purpose, and possible transfer remain undetermined.', '% Pale detached marks; hand, purpose, and surface origin remain undetermined.\n% Above upper disk4 the short course is supported; its faint lower continuation is unresolved.')
s = s.replace(r'\draw[opacity=.14] (252,825)--(278,827);', r'\draw[opacity=.14] (252,825)--(256,825) (259,825)--(264,826) (267,826)--(271,826) (274,827)--(278,827);')
needle = '\\draw[line width=3.7pt] (1118,795)--(1158,853);\n'
s = s.replace(needle, needle + '% Detached short dark trace below the broad segment; role and hand undetermined.\n\\draw[line width=.55pt] (1166,875)--(1165,879);\n', 1)
(R/'pages/J81-01_81_scan010.tex').write_text(s)
print('Wrote crop-adjudicated scan010.')
