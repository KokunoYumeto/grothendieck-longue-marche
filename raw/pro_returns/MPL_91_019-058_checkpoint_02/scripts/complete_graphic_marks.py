from pathlib import Path
from record_page import ROOT, now, refresh
assert 'transcription frozen' not in (ROOT/'progress.log').read_text()
changes={}
def change(scan,old,new):
 p=ROOT/'pages'/f'MPL_91_019-058_91_scan{scan:03}.tex'
 t=p.read_text(); assert old in t,(scan,old)
 p.write_text(t.replace(old,new),encoding='utf8')
 changes.setdefault(scan,0); changes[scan]+=1
change(24,r'''\diagram{\begin{tikzcd}
&L\arrow[dl,"\sigma"']\\J\arrow[d,dashed,"\unsure{\lambda}"']&L'\arrow[u,"\alpha"]\\G&
\end{tikzcd}}''',r'''\figure{\begin{tikzpicture}
\node[inner sep=0] at (0,0) {\diagram{\begin{tikzcd}[ampersand replacement=\&,column sep=2.2em,row sep=2em]
\&L\arrow[dl,"\sigma"']\\J\arrow[d,dashed,"\unsure{\lambda}"']\&L'\arrow[u,"\alpha"]\\G\&
\end{tikzcd}}};
\draw (-1.15,0.1)--(0.25,1.55)--(1.05,1.28);
\draw (1.04,1.05)--(-0.72,-0.28)--(-1.05,0.02);
\end{tikzpicture}}''')
change(24,r'''\margin{\unsure{condition définie pour l'existence de} $u_0$}''',r'''\margin{\figure{\begin{tikzpicture}[baseline=(m.base)]
\node[text width=4cm,align=center,inner sep=2pt] (m) at (0,0) {\unsure{condition définie pour l'existence de} $u_0$};
\draw (-2.1,0.5)..controls(-2.6,0.15)and(-2.3,-0.48)..(-1.5,-0.5)--(1.9,-0.5)--(2.1,0.5)--cycle;
\draw (0.9,-0.5)..controls(1,-1.1)and(0.5,-1.8)..(0.4,-2);
\end{tikzpicture}}}''')
p=ROOT/'pages'/'MPL_91_019-058_91_scan025.tex';t=p.read_text(); start=t.index(r'\margin{\diagram'); end=t.index('chgt de base.}',start)+len('chgt de base.}')
old=t[start:end]; inside=old[len(r'\margin{'):-1].replace(r'\begin{tikzcd}',r'\begin{tikzcd}[ampersand replacement=\&]').replace('&',r'\&').replace(r'\\&',r'\&')
new=r'''\margin{\figure{\begin{tikzpicture}
\node[anchor=north west,inner sep=0,text width=7cm,align=left] at (0,0) {'''+inside+r'''};
\draw (-0.25,0.3)--(-0.25,-3.7)..controls(-0.25,-4.1)and(0.7,-4)..(0.85,-4.4)..controls(0.9,-4.7)and(1.3,-4.6)..(1.7,-4.6)--(5.6,-4.6)..controls(6,-4.6)and(6,-4.95)..(6.6,-4.95)--(7.05,-4.9);
\end{tikzpicture}}}'''
change(25,old,new)
change(25,r'''\margin{(\uline{sép. clos suffit!})}''',r'''\margin{\figure{\begin{tikzpicture}[baseline=(m.base)]
\node[inner sep=2pt] (m) at (0,0) {(\uline{sép. clos suffit!})};
\draw (-1.8,-0.05)..controls(-2.1,0.6)and(0.9,0.8)..(1.85,0.05)..controls(1.6,-0.25)and(0.4,-0.25)..(0.1,-0.35)..controls(-0.3,-0.45)and(-0.5,-0.7)..(-0.5,-0.9)..controls(-0.6,-0.65)and(-0.1,-0.35)..(0.1,-0.35)..controls(-0.7,-0.4)and(-1.7,-0.35)..(-1.8,-0.05);
\end{tikzpicture}}}''')
change(32,'$X$ has reduced geometric fibers,',r'''$X$ has \figure{\begin{tikzpicture}[baseline=(m.base)]\node[inner sep=2pt] (m) at (0,0) {reduced geometric fibers,};\draw (0,0) ellipse[x radius=2.3cm,y radius=0.35cm];\end{tikzpicture}}''')
change(45,r'\mathbf P_Y^n',r'\unsure{P|\mathbf P}_Y^n')
change(45,r'''\margin{\unsure{Sur le réseau plat|Sur le réseau fidèle}}''',r'''\margin{\figure{\begin{tikzpicture}[baseline=(m.base)]
\node[inner sep=3pt] (m) at (0,0) {\unsure{Sur le réseau plat|Sur le réseau fidèle}};
\draw (-2.35,0.35)..controls(-2.55,-0.1)and(-2.55,-0.3)..(-2.25,-0.3)--(-0.15,-0.3)--(0,-0.75)--(0.12,-0.3)--(2.35,-0.3)..controls(2.5,-0.3)and(2.55,0.1)..(2.4,0.35);
\end{tikzpicture}}}''')
with (ROOT/'audit_changes.md').open('a') as f:
 f.write('\n## Final graphic and alphabet comparison\n\nScans024,025,032,045: restored polygonal/curved enclosures and callout tails in TikZ around the already transcribed content; diagrams remain tikz-cd. Scan045 P is not confidently bold, so both occurrences now carry the same alphabet doubt. Source images personally re-opened before these changes.\n')
with (ROOT/'progress.log').open('a') as f:
 f.write('graphic and alphabet comparison: scans024,025,032,045 amended '+now()+'\n')
refresh()
print(changes)
