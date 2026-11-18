import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{58}
\mspage{3}
% archive foliation: 60
et telle que

a) $f\mid(\operatorname{Int}H)\cap\mathring D$ est injective, son image $\subset\mathbb C\setminus K$

b) $f(0)=x$, \deleted{$\unsure{f(\pm t)=f(t)}$}

c) $f\mid]-1,0]$ et $f\mid[0,1[$ injectives, avec
même image $\subset K$.

\uline{Scholie} Chaque rive de $K$ \deleted{\unsure{est un}}\inserted{munit} $K$ d'une
structure analytique réelle canonique, via
l'inclusion de $K$ dans $\mathbb C$ (ou dans une
surface conforme quelc), mais le passage
de l'une à l'autre se fait par une
application (identique) qui n'est pas un
iso analytique : les propriétés de régularité
(caractère $C^\infty$, ou analytique réel etc)
reflètent sans doute les propriétés de
régularité correspondantes de $K$ dans $\mathbb C$.
(Ceci \inserted{devrait} se \unsure{magnifier|préciser} dans \deleted{\unsure{le th}}\inserted{un} Scholie
plus circonstancié au Théorème suivant).

\textcircled{\unsure{3|C}} \uline{Recollement}. On doit avoir un
théorème \unsure{dans le} style du
"""
save(58,tex,[('text','top','et telle que'),('text','a)','f|(Int H)∩D° est injective'),('text','b)','f(0)=x'),('deletion','b)','f(±t)=f(t)'),('text','c)','f|]-1,0] et f|[0,1['),('text','main paragraph','Scholie Chaque rive de K'),('deletion','Scholie first line','est un'),('insertion','Scholie first line','munit'),('text','parenthesis below Scholie','Ceci devrait se magnifier'),('insertion','parenthesis','devrait; un'),('deletion','parenthesis','le th'),('text','bottom heading and two lines','3 Recollement. On doit avoir')],
 doubts=[('top b deletion','f(±t)=f(t)','struck-through arguments unclear','low'),('Scholie final parenthesis','magnifier','préciser; letter shapes support magnifier better','low'),('bottom section marker','3','C possible, compare preceding circled marks','medium'),('bottom last line','dans le','compressed phrase','medium')],
 abbreviations=[('quelc','quelconque'),('iso','isomorphisme')],
 leads=['Scholie: two banks of the same topological arc induce two real analytic structures; identity between them need not be analytic.','Self-flagged expectation: regularity (C-infinity, real analytic) of the bank transition reflects regularity of the embedded arc, sans doute; calls for a more detailed scholium.','Recollement introduced prospectively: On doit avoir un théorème ... .'])
