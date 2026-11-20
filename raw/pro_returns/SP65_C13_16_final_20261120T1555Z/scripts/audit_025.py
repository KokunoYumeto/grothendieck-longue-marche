"""Changes established by the root reader's second image reading."""
import json
from record import ROOT,RECORDS,build
path=ROOT/'pages/16_scan025.tex';s=path.read_text()
old=r'''\[
\deleted{\unsure{(*)}}\quad
\boxed{\varphi(x,y)\varphi(t,z)+Q(\psi(x,y),\psi(t,z))
=\varphi(t,x)\varphi(y,z)+Q(\psi(t,x),\psi(y,z))}
\]'''
new=r'''\figure{\begin{tikzpicture}
\node[anchor=west,inner sep=0pt] (e) at (0,0) {$\displaystyle\varphi(x,y)\varphi(t,z)+Q(\psi(x,y),\psi(t,z))=\varphi(t,x)\varphi(y,z)+Q(\psi(t,x),\psi(y,z))$};
\node[anchor=east] at (-0.2,0) {$\deleted{\unsure{(*)}}$};
\draw ([xshift=-4cm,yshift=.15cm]e.north west)--([xshift=.15cm,yshift=.15cm]e.north east);
\draw ([xshift=-.1cm,yshift=.15cm]e.north west)--([xshift=-.1cm,yshift=-.15cm]e.south west)--([xshift=.15cm,yshift=-.15cm]e.south east);
\end{tikzpicture}}'''
assert old in s;s=s.replace(old,new);path.write_text(s)
rp=RECORDS/'025.json';p=json.loads(rp.read_text());r=p['changes'][16]
assert r['place']=='Associativity callout and box'
r.update(c=r'\deleted{\unsure{(*)}} and closed \boxed frame',final=r'\deleted{\unsure{(*)}} and open-right three-sided frame in TikZ',dc=True,ink='scan 025 (455,1590,550,1695): dense hatching covers the small callout. Second full-image reading: the top line extends left beneath the heading; a left vertical and lower line frame the equation, and no right vertical is visible at the scan edge. The closed box was replaced by those visible strokes.')
p['inventory'].append(['drawing','around associativity equation','open-right frame with top line extended left'])
rp.write_text(json.dumps(p,ensure_ascii=False,indent=2)+'\n');build()
