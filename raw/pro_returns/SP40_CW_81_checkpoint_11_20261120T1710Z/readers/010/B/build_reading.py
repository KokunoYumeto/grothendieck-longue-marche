from pathlib import Path
import json
import re
ROOT=Path('/workspace/scratch/94548b74fbe0')
OUT=ROOT/'out/readers/010/B'
s=(ROOT/'packets/010/C.tex').read_text()
def change(old,new):
 global s
 assert s.count(old)==1, (old[:100],s.count(old))
 s=s.replace(old,new)
# C's drawing paths are reused after visual inspection of every figure.
# The decisions below preserve the source's visible local traces and qualifications.
change(r'\draw[opacity=.65,line width=.55pt] (1018,28)--(1025,29) (1037,27)--(1046,26);',r'''% Detached upper-edge marks: their hand and function remain undetermined.
\draw[opacity=.65,line width=.55pt] (1018,26) .. controls (1020,31) and (1023,32) .. (1025,27);
\draw[opacity=.65,line width=.55pt] (1037,29)--(1037,26) .. controls (1040,28) and (1043,28) .. (1046,25)--(1046,28);''')
change(r'\draw (1328,433) .. controls (1330,406) and (1335,357) .. (1341,329);',r'''% Undetermined trace: pale intervals separate the darker parts of this upper extension.
\draw[opacity=.22] (1328,433) .. controls (1330,406) and (1335,357) .. (1341,329);
\draw[line width=.65pt] (1340,332)--(1339,339) (1338,343) .. controls (1336,351) and (1337,359) .. (1335,365);
\draw[line width=.55pt] (1333,382)--(1332,389) (1331,398)--(1330,403) (1329,411)--(1327,432);''')
change(r'\draw[opacity=.4] (276,827)--(293,828);',r'''\draw[opacity=.14] (252,825)--(278,827);
\draw[opacity=.4] (278,827)--(293,828);''')
# Preserve the cancellation annotation without manufacturing a horizontal strike.
node_start=r'\node[inner sep=0pt,outer sep=0pt,anchor=center] at (548,820) {\deleted{'
a=s.index(node_start)
b=s.index(r'\end{tikzpicture}}}};',a)+len(r'\end{tikzpicture}}}};')
old=s[a:b]
inner=old[len(node_start):-3]
assert inner.startswith(r'\hbox{\begin{tikzpicture}') and inner.endswith(r'\end{tikzpicture}}')
inner=inner.replace('line width=.57pt]', 'line width=.57pt,color=black]',1)
inner=inner.replace(r'\end{tikzpicture}',r'''% Small pale descending trace and dark tip at the lower-left outline.
\draw[opacity=.16,line width=.4pt] (490,861) .. controls (488,885) and (490,901) .. (491,915);
\draw[line width=.55pt] (491,912)--(490,920);
\end{tikzpicture}''')
new=r'''% State remains uncertain: diagonal cancellation | hatching. Only the visible diagonal paths are inked.
\node[inner sep=0pt,outer sep=0pt,anchor=center] at (548,820) {\unsure{\rlap{'''+inner+r'}\phantom{\deleted{'+inner+r'}}}};'
s=s[:a]+new+s[b:]
# Independent local fill-state decisions in three bottom graphs.
a=s.index('at (222,1035)')
b=s.index(r'\end{minipage}};',a)
seg=s[a:b]
seg=seg.replace(r'\unsure{\bullet|\circ}',r'\unsure{\circ|\bullet}',1)
s=s[:a]+seg+s[b:]
for anchor in ['at (563,1026)','at (1075,1032)']:
 a=s.index(anchor)
 b=s.index(r'\end{minipage}};',a)
 seg=s[a:b]
 seg=seg.replace(r'\bullet\arrow',r'\unsure{\bullet|\circ}\arrow',1)
 s=s[:a]+seg+s[b:]
# Additional local geometry, all inspected; no verbal interpretation is placed in the transcription.
extra=r'''
% Hook projecting above/right of the uncertain middle vertex under upper disk 7.
\draw[line width=.65pt] (1153,251) .. controls (1154,245) and (1159,246) .. (1163,252);
% Tiny detached spot just above the outer lower arch in the last middle disk.
\fill (1314,543) circle[radius=1.4];
% Pale detached marks; hand, purpose, and possible transfer remain undetermined.
\draw[opacity=.14,line width=.4pt] (416,241) .. controls (425,250) and (426,260) .. (421,266) .. controls (416,274) and (410,275) .. (403,275);
\draw[opacity=.16,line width=.4pt] (784,42) .. controls (784,49) and (785,55) .. (787,62);
\draw[opacity=.4,line width=.4pt] (786,56)--(786,59);
\draw[opacity=.16,line width=.4pt] (369,743) .. controls (379,750) and (386,763) .. (392,774);
\draw[opacity=.14,line width=.4pt] (1567,352) .. controls (1570,358) and (1576,360) .. (1580,362);
% Pale diagonal inside the right angular trace, with independently detached lower dash.
\draw[opacity=.13,line width=.4pt] (1436,1043) .. controls (1469,1009) and (1529,942) .. (1559,895);
\draw[opacity=.45,line width=.45pt] (1435,1084)--(1437,1093);
% Dark pieces and small detached marks around the upper-right angular-trace endpoint.
\draw[opacity=.75,line width=.45pt] (1568,908)--(1570,917);
\fill[opacity=.65] (1566,921) circle[radius=1.15];
\fill[opacity=.3] (1550,893) circle[radius=1.2];
\fill[opacity=.2] (1603,930) circle[radius=1.6];
'''
pos=s.rfind(r'\end{tikzpicture}}')
assert pos>=0
s=s[:pos]+extra+s[pos:]
(OUT/'reading.tex').write_text(s)
print('Wrote complete reading.tex')
