import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from audit_page import audit,ROOT,PREFIX
s=(ROOT/'pages'/f'{PREFIX}_68_scan054.tex').read_text()
diag=s[s.index(r'\diagram{'):s.index(r'\end{tikzcd}}')+len(r'\end{tikzcd}}')]
audit(54,[
 (diag,diag.replace(r'\rotatebox{90}{$\supset$}',r'\cup')),
 (r'\unsure{(-1)^{?}|(-1)^p}',r'\unsure{(-1)^q|(-1)^{?}}'),
 (r'\draw[line width=.8pt,->] (0,0)--(0,1.15)--(1.2,1.12);',r'\draw[line width=.8pt] (0,0)--(.04,1.15) .. controls (.45,1.08) and (.83,1.13) .. (1.2,1.12);'),
 (r'\draw[line width=1.2pt,->] (1.2,0)--(0,0);',r'\draw[line width=1.2pt] (1.2,0)--(0,0);'),
 (r'''\draw[line width=.35pt] (3.9,1.35)--(4.5,2.2);
\draw[line width=.35pt] (3.83,2.2)--(4.4,2.85);
\draw[line width=.35pt] (4.3,1.42)--(4.9,2.15);
\draw[line width=.35pt] (4.85,1.4)--(5.55,2.1);''',r'''\draw[line width=.35pt] (3.9,2.25)--(4.43,2.82);
\draw[line width=.35pt] (3.9,1.78)--(4.52,2.37);
\draw[line width=.35pt] (3.87,1.2)--(4.61,2.04);
\draw[line width=.35pt] (4.62,1.44)--(5,1.85);
\draw[line width=.35pt] (5.15,1.35)--(5.64,1.9);'''),
],doubts=[
 ('inserted product sign above first Stokes equation',r'(-1)^q',r'(-1)^{?}; head appears closed with descending stem','low'),
 ('square drawing, corners','right edge ends in downward arrow','other thick corners have no secure arrowheads','medium'),
],comment='Both halves and enlarged exponent, square and terminal degree were checked. Corrected the vertical inclusion shapes to cup-shaped marks; removed unsupported arrowheads from two square edges and matched the five hatch strokes.')
