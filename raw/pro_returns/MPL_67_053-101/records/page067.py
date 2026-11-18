import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{67}
% archive foliation: 69
et considérons ``l'espace de
Teichmüller à bord'' correspondant
\deleted{$\unsure{T_{g\nu}}$} $TB_{g\nu}$, qui est \deleted{isom.}\inserted{homéo.} à $\mathbb R^{6g-6+3\nu}$
ou mieux, à $\mathbb C^{3g-3+\nu}\times\mathbb R^\nu$. On a une
application
\diagram{\begin{tikzcd}
\underset{\simeq\mathbb C^{3g-3+\nu}\times\mathbb R^\nu}{TB_{g,\nu}} \arrow[r] &
\underset{\mathbb C^{3g-3+\nu}\deleted{\times\mathbb R^\nu}}{T_{g\nu}}
\end{tikzcd}}
de bouchage des trous, je présume
qu'elle est fibrante \unsure{de faç.},
plus précise, que \deleted{\unsure{dans}\ \unsure{la}}\inserted{c'est la projection}
canonique. \deleted{de} En effet, cela doit
provenir du fait que pour une
sphère à bord \inserted{\unsure{déformante|déformable}} de type $(0,3)$, \deleted{dont}
quand le modèle combinatoire
(\unsure{triangle conducteur}) est fixé, et
qu'on varie seulement \deleted{les} un, deux
ou trois des paramètres ``longueurs''
correspondant aux trois trous, la
sphère ``à bord et ponctuée'' (mono, bi ou
triponctuée suivant les cas) \deleted{\unsure{et le}}\inserted{\unsure{associée|acquise}}
"""
save(67,tex,[('text','top','et considérons l’espace de Teichmüller'),('deletion','top','T_{gν}'),('deletion','upper','isom.'),('insertion','upper','homéo.'),('diagram','upper middle','TB_{g,ν}→T_{gν}'),('deletion','diagram right annotation','×R^ν'),('text','middle','de bouchage des trous je présume'),('deletion','middle','dans la'),('insertion','middle','c’est la projection'),('deletion','middle lower','de'),('text','lower middle','En effet cela doit provenir'),('insertion','lower middle','déformante'),('deletion','lower middle','dont'),('deletion','lower','les'),('text','bottom','la sphère à bord et ponctuée'),('deletion','bottom','et le'),('insertion','bottom','associée')],
 doubts=[('fibration sentence','de faç.','short phrase pale; may be a different connector','low'),('inserted after sphère à bord','déformante','déformable possible, ending compressed','low'),('combinatorial model','triangle conducteur','both words cursive, second seems conducteur','medium'),('last inserted word','associée','acquise possible; no completion from next page','low')],
 notations=[('Bordered Teichmüller space',r'TB_{g\nu}','TB, not a script T; comma explicitly present in displayed source'),('Unbordered marked Teichmüller space',r'T_{g\nu}','same plain T')],
 abbreviations=[('homéo.','homéomorphe'),('isom.','isomorphe'),('faç.','façon')],
 leads=['Presumption that canonical capping TB_{gν}→T_{gν} is a fibration, more precisely the coordinate projection C^{3g−3+ν}×R^ν→C^{3g−3+ν}.','Suggested justification varies boundary lengths of a pair of pants while keeping the combinatorial model fixed; argument continues.'])
