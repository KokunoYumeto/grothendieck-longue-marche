from pathlib import Path
ROOT=Path(__file__).resolve().parents[4]
HERE=Path(__file__).resolve().parent
tex=(ROOT/'packets/010/C.tex').read_text()
tex=tex.replace('\\scanpage{10}\n','\\scanpage{10}\n% Independent reader C, scan 010. All source coordinates below refer to the full scan.\n',1)
# Each physical endpoint was inspected separately; these uncertainties are local.
tex=tex.replace('\\unsure{\\bullet|\\circ}\\arrow[r,dash,line width=.65pt,start anchor=center,end anchor=center,shorten <=1pt,shorten >=1pt] \\& \\circ',
                '\\unsure{\\circ|\\bullet}\\arrow[r,dash,line width=.65pt,start anchor=center,end anchor=center,shorten <=1pt,shorten >=1pt] \\& \\circ',1)
start=tex.index('\\node[inner sep=0pt] at (563,1026)')
end=tex.index('\\end{minipage}};',start)+len('\\end{minipage}};')
block=tex[start:end].replace('\\bullet\\arrow','\\unsure{\\circ|\\bullet}\\arrow',1)
tex=tex[:start]+block+tex[end:]
start=tex.index('\\node[inner sep=0pt] at (1075,1032)')
end=tex.index('\\end{minipage}};',start)+len('\\end{minipage}};')
block=tex[start:end].replace('\\bullet\\arrow','\\unsure{\\bullet|\\circ}\\arrow',1)
tex=tex[:start]+block+tex[end:]
# The projecting middle-row trace has pale intervals and short dark portions.
tex=tex.replace('\\draw (1328,433) .. controls (1330,406) and (1335,357) .. (1341,329);',r'''% Role and hand of the projecting trace and detached blob remain undetermined.
\draw[opacity=.35] (1328,433) .. controls (1330,406) and (1335,357) .. (1341,329);
\draw[line width=.8pt] (1328,430)--(1330,410) (1332,397)--(1334,387) (1335,376)--(1336,369) (1338,359)--(1340,338) (1340,334)--(1341,329);
\fill (1314,544) circle[radius=1.4];''',1)
# Preserve the bent outlines of the two detached traces without assigning letters.
tex=tex.replace('\\draw[opacity=.65,line width=.55pt] (1018,28)--(1025,29) (1037,27)--(1046,26);',r'''% Detached shape candidates; function and hand remain undetermined.
\draw[opacity=.65,line width=.65pt] (1018,27) .. controls (1020,30) and (1024,30) .. (1025,27);
\draw[opacity=.75,line width=.75pt] (1037,28)--(1038,25)--(1040,27)--(1044,27)--(1045,25)--(1046,27);
% Pale curved trace beneath the second upper disk: no letter assigned.
\draw[opacity=.16,line width=.4pt] (414,240) .. controls (425,246) and (428,263) .. (418,269) .. controls (412,274) and (405,274) .. (400,273);''',1)
# Main right curl was already present. Add only the distinct adjacent upper trace.
tex=tex.replace('\\draw[opacity=.22,line width=.4pt] (1518,375) .. controls (1540,374) and (1561,405) .. (1524,401);',r'''\draw[opacity=.22,line width=.4pt] (1518,375) .. controls (1540,374) and (1561,405) .. (1524,401);
% A separate pale short slant above-right; role and hand undetermined.
\draw[opacity=.14,line width=.4pt] (1567,351) .. controls (1568,356) and (1574,359) .. (1576,363);''',1)
# Separate pale diagonal in the lower-left open gap.
tex=tex.replace('\\node at (201,691) {OK};',r'''\draw[opacity=.18,line width=.4pt] (368,743) .. controls (378,748) and (390,766) .. (398,777);
\node at (201,691) {OK};''',1)
# Preserve the original disk and visible diagonals, with a doubtful cancellation state.
# The phantom deleted copy supplies the annotation without adding a horizontal stroke.
needle='\\deleted{\\hbox{\\begin{tikzpicture}'
a=tex.index(needle)
arg_start=a+len('\\deleted{')
depth=1;i=arg_start
while depth:
 if tex[i]=='{': depth+=1
 elif tex[i]=='}': depth-=1
 i+=1
G=tex[arg_start:i-1]
G=G.replace('\\end{tikzpicture}',r'''% Small pendant stroke below the lower-left outline.
\draw[opacity=.6] (490,911)--(489,920);
\end{tikzpicture}''',1)
rep='\\unsure{\\rlap{'+G+'}\\phantom{\\deleted{'+G+'}}}'
tex=tex[:a]+rep+tex[i:]
tex=tex.replace('\\node[inner sep=0pt,outer sep=0pt,anchor=center] at (548,820)',
 '% State doubt: diagonal cancellation (primary) | hatching. No chronology inferred.\n\\node[inner sep=0pt,outer sep=0pt,anchor=center] at (548,820)',1)
# A separate faint diagonal runs into the interior of the right angular trace.
tex=tex.replace('\\draw[opacity=.23] (1568,905) .. controls (1572,924) and (1571,943) .. (1581,957);',r'''\draw[opacity=.23] (1568,905) .. controls (1572,924) and (1571,943) .. (1581,957);
\draw[opacity=.13,line width=.4pt] (1440,1036) .. controls (1452,1019) and (1469,995) .. (1490,985);
\draw[opacity=.6,line width=.5pt] (1568,907)--(1569,915);
\fill[opacity=.5] (1567,921) circle[radius=1];
\fill[opacity=.3] (1550,894) circle[radius=1];''',1)
tex=tex.replace('\\draw[opacity=.4] (276,827)--(293,828);',r'''\draw[opacity=.12,line width=.4pt] (250,826)--(276,828);
\draw[opacity=.4] (276,827)--(293,828);''',1)
tex=tex.replace('% Two faint, angular lines at the foot, crossing the last graph and continuing at the right.',r'''% Detached irregular pale patch at the right margin; role and origin undetermined.
\filldraw[fill=black,fill opacity=.04,draw opacity=.10,line width=.3pt] (1628,797) .. controls (1627,791) and (1631,788) .. (1636,790) -- (1637,786) -- (1640,791) -- (1645,793) .. controls (1648,800) and (1641,804) .. (1637,807) .. controls (1634,804) and (1630,803) .. (1628,797) -- cycle;
% Two faint, angular lines at the foot, crossing the last graph and continuing at the right.''',1)
(HERE/'reading.tex').write_text(tex)
print('Wrote',HERE/'reading.tex')
