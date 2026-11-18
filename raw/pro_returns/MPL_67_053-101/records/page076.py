import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{76}
\mspage{12}
% archive foliation: 78
Au niveau des multiplicités modulaires \inserted{(analytiques réelles.)}
on trouve sûrement un morphisme \inserted{\unsure{entre celles-ci}}
\deleted{$\unsure{MB_{g,\nu}}$}
\diagram{\begin{tikzcd}
MDB_{g,\nu} \arrow[r] & M_{\mathrm{st}}N\deleted{\unsure{{}_{g,\nu}}}D\deleted{\unsure{{}_{g}}}{}_{g,\nu}
\end{tikzcd}}
où $MDB_{g,\nu}$ désigne la multiplicité modulaire
(M) pour les surfaces holomorphes compactes
``découpées'' (D) à bord (B) de type $g,\nu$, et
$M_{\mathrm{st}}ND_{g,\nu}$, celle pour les courbes algébriques
stables (de type loc. constant) \inserted{de type $g,\nu$} à structure de
propagation \unsure{unnodale|nodale} (N) et à système \inserted{adm.} de
disques (D) autour des pts marqués.

Cette flèche est compatible avec les
flèches canoniques vers la cat. des
types combinatoires\inserted{-toriques} de tels objets
(diagrammes MD (Mumford-Deligne en
``\unsure{moderne|modulaires}'') (\deleted{\unsure{avec poids}}\inserted{incluant} une pondération
des sommets) à structures toriques
associées aux arêtes \ldots\ donnant lieu à un
diagramme commutatif
"""
save(76,tex,[
('text','top','Au niveau des multiplicités modulaires'),
('insertion','top right','(analytiques réelles.)'),
('insertion','under morphisme','entre celles-ci'),
('deletion','above arrow source','MB g,nu'),
('diagram','upper third','MDB g,nu to M st ND g,nu'),
('deletion','target before D','g,nu'),
('deletion','target after D','g'),
('text','middle','où MDB désigne'),
('insertion','above à structure','de type g,nu'),
('insertion','above de disques','adm.'),
('text','lower half','Cette flèche est compatible'),
('insertion','above de tels objets','-toriques'),
('deletion','before une pondération','avec poids'),
('insertion','above deletion','incluant')
],doubts=[('line 2 insertion','entre celles-ci','Small text below morphisme; first word especially compressed.','low'),('arrow target','M_st ND with cancelled indices','Overwritten target indices cannot be separated securely.','low'),('line 10','unnodale','nodale; apparent initial extra stroke retained in the first reading.','low'),('lower paragraph, quoted word','moderne','modulaires; letter sequence highly cursive.','low'),('lower deletion','avec poids','Heavy cancellation over both words.','low')],notations=[('moduli letters',r'M_{\mathrm{st}}ND_{g,\nu}','st appears below M; N,D remain on baseline.')],abbreviations=[('adm.','admissible'),('loc.','localement'),('MD','Mumford-Deligne')],leads=['A surely existing moduli morphism MDB to M_st ND is asserted and compatibility with combinatorial-toric types is announced; constructions and smoothness require separate checking.'])
