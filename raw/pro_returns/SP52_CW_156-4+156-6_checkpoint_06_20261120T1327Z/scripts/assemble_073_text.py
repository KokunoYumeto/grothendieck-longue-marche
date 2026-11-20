"""Assemble root's scan073 decisions from the three frozen independent returns.

This script does no reading or image processing. Every choice is documented in
decisions/156-4_073_adjudication_notes.md and was made from root-viewed crops.
"""
from pathlib import Path
import hashlib

O = Path(__file__).resolve().parents[1]
R = O / 'readers/156-4_073'
s = (R / 'R2/reading.tex').read_text()
r1 = (R / 'R1/reading.tex').read_text()

def once(old, new):
    global s
    assert s.count(old) == 1, (old[:100], s.count(old))
    s = s.replace(old, new, 1)

once(r"\margin{double \unsure{Transitivité} de l'induction}",
     r"\margin{\unsure{double} \unsure{Transitivité} de l'induction}")

# Keep the q-connected paragraph drawing. Named node attachments prevent a
# long typeset word from colliding with the worked sign; they add no content.
once(r"\node at (0,-.62) {échangerait les rôle de};",
     r"\node (roles) at (0,-.62) {échangerait les rôle de};")
once(r"\node (pmark) at ([xshift=-.02cm,yshift=-.62cm]pq.base)",
     r"\node (pmark) at ([xshift=.12cm]roles.base east)")

# R1's literal curled mark includes the short crossing arms seen by root.
a = r1.index(r'\unsure{\begin{tikzpicture}', r1.index('% graphic: faux-mark'))
b = r1.index(r'\end{tikzpicture}}', a) + len(r'\end{tikzpicture}}')
faux = r1[a:b]
a2 = s.index(r'\unsure{\begin{tikzpicture}', s.index(r'\node (curl)'))
b2 = s.index(r'\end{tikzpicture}}', a2) + len(r'\end{tikzpicture}}')
s = s[:a2] + faux + s[b2:]

# Literal title underline: its endpoint precedes the uncertain numeral.
once(r"\node at (310,1555) {\uline{\unsure{Corollaire|Comparabilité}} \unsure{1}};",
     r"\node at (310,1555) {\unsure{Corollaire|Comparabilité} \unsure{1}};" + '\n' +
     r"\draw[line width=.6pt] (315,1611) -- (630,1602);")

# a05 supplies only the right end missing from a04: the first b line ends
# sous-, and the next starts figure. This preserves the compound's own hyphen.
once(r"\node at (400,1934) {b) $G$ est une subdivision d'une};",
     r"\node at (400,1934) {b) $G$ est une subdivision d'une sous-};")
once(r"\node at (350,2010) {sous-figure de $F$ :};",
     r"\node at (350,2010) {figure de $F$ :};")

# The first résulte has a detached acute; the last has none in the crop.
# The whole-line doubt here concerns cancellation scope only.
once(r"\node at (371,2285) {\unsure{b) $\Longrightarrow$ a) résulte de $C7_0$}};",
     r"\node at (371,2285) {\unsure{b) $\Longrightarrow$ a) resulte de $C7_0$}};")

# R3 identified an extra upper arc on the small square's lower-left G;
# root saw it in R1/16. Preserve the retrace without inventing an old letter.
g = r'''\begin{tikzpicture}[x=1ex,y=1ex,baseline=-.4ex]
\node[inner sep=0pt] at (0,0) {$G$};
\draw[line width=.35pt] (-.42,.20) .. controls (-.22,.52) and (.16,.55) .. (.40,.40);
\end{tikzpicture}'''
once('\n' + r'G \arrow[r,phantom,"{\cdots}" description]',
     '\n' + g + '\n' + r'\arrow[r,phantom,"{\cdots}" description]')

s = s.replace('R2-', 'ROOT-')
s = s.replace('% ROOT-FIG-DRAFT. All text is written once.',
              '% ROOT-FIG-DRAFT. All text is written once.\n'
              '% The last resulte is unaccented; its line-level doubt concerns\n'
              '% only cancellation scope, not the letters or the double arrow.')
p = O / 'pages/J156-4-09_156-4_scan073.tex'
p.write_text(s)
print(p)
print('SHA256', hashlib.sha256(p.read_bytes()).hexdigest())
