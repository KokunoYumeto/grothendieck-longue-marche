import sys
sys.path.insert(0,'/workspace/scratch/0abb0718b9e3/MPL_46_002-048_work/scripts')
from record_page import save
save(43,r'''\scanpage{43}
\margin{Notion \uline{loc.} \uline{\unsure{triviale}}\unsure{?}}

[\uline{Corollaire} $P$ fibré projectif $\Longleftrightarrow$ $P$ \unsure{adm} loc. une section \inserted{(i.e. est loc. \unsure{trivial})\deleted{\unsure{fibré projectif}}}, et une certaine obstruction dans $H^2(S,\underline{O}_S^*)$ est nulle\ldots]
\margin{en conséquence.}

[\uline{Corollaire} Si $S$ régulier, $P$ fibré projectif ssi il est loc. trivial, ou encore ssi ses fibres génériques le sont.
\margin{\unsure{peut être avec prop 2}}

Autre façon de procéder, valable si $S$ est \uline{strictement \inserted{loc} factoriel} [i.e. tout \uline{schéma} étale dessus est \inserted{loc} factoriel] ----
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0.4,5.1) -- (0.25,5.25) -- (-0.45,5.17) .. controls (-0.65,5.1) and (-0.7,4.7) .. (-0.7,4.3) -- (-0.7,0.6) .. controls (-0.7,0.1) and (-0.55,-0.1) .. (-0.2,-0.1) -- (0.45,0.35);
\draw (-0.45,5.17) -- (0.25,5.2);
\draw (0,4.7) -- (0.18,4.7) -- (0.25,3.05) -- (0.05,2.92);
\end{tikzpicture}}

\uline{Corollaire} \unsure{locale isotrivialité}.
\figure{\begin{tikzpicture}\draw (0,0) .. controls (4,0.15) and (9,0.55) .. (13,0.75);\end{tikzpicture}}

b) \uline{Déf} \uline{Système linéaire} \inserted{\uline{de div. sur} $X/S$}, \uline{paramétré} \uline{par un schéma} $\check{P}/S$ : c'est loc fppf un syst. lin. de div. paramétré par un fibré projectif.
\margin{[$X\to S$ \unsure{fid\textsuperscript{t}} plat loc prés. finie]}
\deleted{Système linéaire}

\deleted{\unsure{Indiquer que}}
Indiquer que $P/S$ est un schéma de Brauer-Séveri.
\margin{\uline{Système linéaire} (tt court).}

classe d'équivalence .....
\mspage{42}''',[
('margin note','top edge','Notion loc. triviale ?'),('text','first bracket','Corollaire P fibré projectif'),('insertion','under first line, anchored after section','(i.e. est loc. trivial)'),('deletion','inside first insertion','fibré projectif'),('display','first corollary, lower line','H²(S,O_S*)'),('margin note','right of first corollary','en conséquence'),('text','second bracket','Corollaire Si S régulier'),('margin note','left edge','peut être avec prop 2'),('text','middle','Autre façon de procéder'),('insertion','above first factoriel','loc'),('insertion','above second factoriel','loc'),('drawing','left edge of second corollary','long curved bracket and smaller bracket'),('text','above separator','Corollaire locale isotrivialité'),('drawing','horizontal separator','slanted horizontal line'),('text','lower half','b) Déf Système linéaire'),('insertion','above Système linéaire','de div. sur X/S'),('margin note','above lower definition, right','[X→S fidᵗ plat loc prés. finie]'),('deletion','right below definition','Système linéaire'),('deletion','below fibré projectif','Indiquer que'),('text','lower paragraph','Indiquer que P/S est un schéma de Brauer-Séveri'),('margin note','right of lower paragraph','Système linéaire (tt court)'),('text','last line','classe d’équivalence .....'),('text','lower left foliation','42')],doubts=[('top note','triviale ?','Last stroke could be punctuation or abbreviated ending','low'),('left margin','peut être avec prop 2','Highly compressed words beside the long bracket','low'),('corollary above separator','locale isotrivialité','Prefix overwritten; no expansion supplied','low'),('bracket above definition','fidᵗ','Could be a shorter abbreviated condition before plat','low')],abbreviations=[('ssi','si et seulement si'),('loc','localement / local, according to position'),('tt court','tout court'),('div.','diviseurs')],observation='The two corollaries and lower definition were read again in enlarged crops. Brackets, insertion connectors, and the source’s trailing points/dashes are retained. The compressed left margin and the wording of the isotriviality corollary are particularly uncertain.')
