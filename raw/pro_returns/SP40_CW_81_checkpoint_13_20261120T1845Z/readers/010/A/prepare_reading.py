from pathlib import Path
BASE=Path(__file__).resolve().parent
ROOT=BASE.parents[3]
s=(ROOT/'packets/010/C.tex').read_text()
s=s.replace('% crop-candidate: scan 10','% crop-candidate: scan 10\n% Independent reader A: graphical paths checked against scan010 and its supplied halves.\n% Residual strokes are retained geometrically; their hand and origin remain undetermined.',1)
def replace_once(old,new):
 global s
 assert s.count(old)==1,(old,s.count(old))
 s=s.replace(old,new,1)
# Distinct endpoint loci; the page does not establish a mathematical role for filling.
anchor=r'\node[inner sep=0pt] at (222,1035)'
a=s.index(anchor)
b=s.index(r'\end{minipage}};',a)
block=s[a:b]
assert block.count(r'\unsure{\bullet|\circ}')==1
s=s[:a]+block.replace(r'\unsure{\bullet|\circ}',r'\unsure{\circ|\bullet}',1)+s[b:]
for anchor in (r'\node[inner sep=0pt] at (563,1026)',r'\node[inner sep=0pt] at (1075,1032)'):
 a=s.index(anchor); b=s.index(r'\end{minipage}};',a)
 block=s[a:b]
 block=block.replace(r'\bullet\arrow',r'\unsure{\circ|\bullet}\arrow',1)
 s=s[:a]+block+s[b:]
# The upper-edge marks have curved/angular ends rather than plain short rules.
replace_once(r'\draw[opacity=.65,line width=.55pt] (1018,28)--(1025,29) (1037,27)--(1046,26);',r'''\draw[opacity=.65,line width=.55pt] (1018,27) .. controls (1020,30) and (1023,31) .. (1025,28);
\draw[opacity=.65,line width=.55pt] (1037,29)--(1039,25)--(1043,26)--(1046,24)--(1047,27);''')
# Additional marks seen in the single permitted local crop of the variant disk.
replace_once(r'\fill (1587,159) circle[radius=6.5];',r'''\fill (1587,159) circle[radius=6.5];
% Detached dark fragments beside the lower descending stroke; role uncertain.
\draw[line width=.7pt] (1596,174)--(1595,180) (1595,182)--(1593,187);
\fill (1584,198) circle[radius=1.2]; \fill (1598,226) circle[radius=1.2];''')
replace_once(r'\fill (1343,492) circle[radius=6.6];',r'''\fill (1343,492) circle[radius=6.6];
% Small detached spot above the outer lower arch; its role is undetermined.
\fill (1317,544) circle[radius=1.6];''')
replace_once(r'\draw[opacity=.22,line width=.4pt] (1518,375) .. controls (1540,374) and (1561,405) .. (1524,401);',r'''\draw[opacity=.22,line width=.4pt] (1518,375) .. controls (1540,374) and (1561,405) .. (1524,401);
% Smaller pale bent trace above and right of the preceding curl.
\draw[opacity=.13,line width=.35pt] (1567,351) .. controls (1571,354) and (1574,360) .. (1582,359);''')
replace_once(r'\draw[opacity=.4] (276,827)--(293,828);',r'''\draw[opacity=.14,line width=.4pt] (249,826)--(276,827);
\draw[opacity=.4] (276,827)--(293,828);''')
# Keep the explicit diagonal cancellation geometry and annotate its state without
# adding a new generic horizontal strike across the already drawn cancellation.
start=s.index(r'\node[inner sep=0pt,outer sep=0pt,anchor=center] at (548,820) {\deleted{\hbox{')
end=s.index(r'\end{tikzpicture}}}};',start)+len(r'\end{tikzpicture}}}};')
old=s[start:end]
inner_start=old.index(r'\begin{tikzpicture}')
inner_end=old.index(r'\end{tikzpicture}')+len(r'\end{tikzpicture}')
inner=old[inner_start:inner_end]
inner=inner.replace(r'\end{tikzpicture}',r'''% Small dark hanging trace below the lower-left circumference.
\fill[opacity=.7] (490,916) ellipse[x radius=1.3,y radius=3.2];
\end{tikzpicture}''')
new=r'''% Primary state: cancellation; hatching remains a supported alternative.
\node[inner sep=0pt,outer sep=0pt,anchor=center] at (548,820) {%
\rlap{\hbox{'''+inner+r'''}}%
\phantom{\deleted{\hbox{'''+inner+r'''}}}};'''
s=s[:start]+new+s[end:]
# Disconnected parts of the lower-right traces are retained in the same drawing.
replace_once(r'\draw[opacity=.23] (1568,905) .. controls (1572,924) and (1571,943) .. (1581,957);',r'''\draw[opacity=.23] (1568,905) .. controls (1572,924) and (1571,943) .. (1581,957);
\draw[opacity=.6,line width=.5pt] (1569,908)--(1571,917);
\fill[opacity=.65] (1568,921) circle[radius=1];
% Fainter oblique trace within the right angular group; endpoints approximate.
\draw[opacity=.12,line width=.35pt] (1444,1037) .. controls (1458,1016) and (1480,991) .. (1504,980);
% Detached short stroke below that group; no character or relation assigned.
\draw[opacity=.4,line width=.45pt] (1435,1087)--(1438,1098);''')
# Three further pale bounded shapes, whose origin and hand remain undetermined.
insert=r'''% Additional residual shapes, transcribed graphically without character readings.
\draw[opacity=.16,line width=.35pt] (415,242) .. controls (423,251) and (424,263) .. (418,270) .. controls (415,274) and (409,276) .. (402,276);
\draw[opacity=.16,line width=.35pt] (369,743) .. controls (379,751) and (390,762) .. (405,778) -- (415,786);
\draw[opacity=.25,line width=.4pt] (377,751)--(384,758) (390,764)--(393,767);
\filldraw[fill opacity=.10,draw opacity=.16,line width=.3pt]
(1629,793) .. controls (1629,790) and (1631,788) .. (1635,788)
--(1636,786)--(1640,790)--(1645,792)
.. controls (1649,795) and (1648,799) .. (1646,802)
--(1643,803)--(1640,806)--(1637,808)--(1634,804)--(1630,804)
.. controls (1627,801) and (1627,797) .. (1629,793)--cycle;
'''
pos=s.rindex(r'\end{tikzpicture}}')
s=s[:pos]+insert+s[pos:]
(BASE/'reading.tex').write_text(s)
print('Wrote complete reading.tex, retaining the page-wide connected graphical layout.')
