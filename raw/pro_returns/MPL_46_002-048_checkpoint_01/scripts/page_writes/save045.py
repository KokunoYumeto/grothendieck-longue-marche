import sys
sys.path.insert(0,'/workspace/scratch/0abb0718b9e3/MPL_46_002-048_work/scripts')
from record_page import save
save(45,r'''\scanpage{45}
\uline{Relations} a) Morphismes $X\longrightarrow\unsure{\check{\check{P}}|\check{P}}$ et syst. lin. de div \unsure{sans pts fixes paramétrés} par $P$.

\deleted{Applications}
b) Syst. lin. de div. ``\unsure{str.}'' sans ``p. fixe'' paramétré par $\check{P}$, et applications rationnelles sur $S$
\[
X\longrightarrow\check{P}
\]
avec \unsure{petite} propriété supplémentaire \uline{de nature locale}
\margin{[qui est inutile si $X$ est régulier \deleted{\illegible{1}} ou strict loc. factoriel]}

c)
\[
\underline{\mathrm{Syst.lin}}_{X/S}\xrightarrow{\lambda}\underline{\mathrm{Pic}}_{X/S}
\]
morphisme naturel : (\unsure{ayant} \unsure{d'ailleurs} une section canonique). Si $X/S$ est propre à fibres géom. intègres, alors $\lambda$ est rel. représentable comme la grassmannienne complète d'un schéma de Brauer-Séveri généralisé (Attention, il y a une question d'effectivité des données de descente dans un fibré projectif relatif un Module non loc. libre !].

Si, au lieu de fibres géom. intègres, on suppose $f_*(O_X)\simeq O_S$ \unsure{univ\textsuperscript{t}}, on trouve encore un morphisme représentable par un \uline{ouvert} d'un fibré \deleted{projectif} de Brauer-Séveri généralisé .....
\margin{\uline{\unsure{à vérifier}}\par
\unsure{Montrer}\par
$X\to S$ est \uline{projectif}\par
si $S$ hensélien local à fibres \unsure{géoréd!}\par
si $\unsure{q}(\unsure{\mathrm{Pic}}(X/S))$\par
est \uline{loc} \unsure{noéthérien}}
\mspage{44}''',[
('text','top','Relations a) Morphismes X→P'),('deletion','above b)','Applications'),('text','b), first two lines','Syst. lin. de div. str. sans p. fixe'),('display','b), next line','X→P̌'),('text','following display','avec petite propriété supplémentaire'),('margin note','right below b)','qui est inutile si X est régulier'),('deletion','inside right marginal bracket','obliterated word after régulier'),('text','subdivision marker','c)'),('display','c), top','Syst.lin_X/S →λ Pic_X/S'),('text','c), long paragraph','morphisme naturel'),('text','parenthesis in c)','Attention, il y a une question d’effectivité'),('text','bottom continuation','Si, au lieu de fibres géom. intègres'),('display','bottom paragraph inline','f_*(O_X)≃O_S univᵗ'),('deletion','last line','projectif'),('margin note','diagonal lower left','à vérifier ; Montrer X→S est projectif'),('text','lower left foliation','44')],doubts=[('a), accent above P',r'\check{\check{P}}','Two short angular marks, possibly overwritten single check','low'),('c), parenthesis','ayant d’ailleurs','Compressed connective; first reading remains tentative','low'),('lower left margin','Montrer; géoréd!; q(Pic(X/S)); noéthérien','Very compressed diagonal writing; read in an enlarged rotated crop','low')],notation=[('Ordinary handwritten quotation marks',"``...''",'Use two backticks and two apostrophes; do not replace by guillemets'),('Dual projective object',r'\check P','Use check accent where two converging strokes are visible; mark overwritten double accent separately')],abbreviations=[('géom.','géométriquement / géométriques'),('rel.','relativement'),('univᵗ','universellement')],observation='Dense revisions and low-contrast diagonal margin. The warning about effectiveness is legible; its surrounding grammar is preserved, including the mismatched opening parenthesis and closing bracket. One heavily obliterated word is marked illegible after enlargement; the remaining difficult margin words have proposed readings.')
