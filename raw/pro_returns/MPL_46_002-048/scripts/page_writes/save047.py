import sys
sys.path.insert(0,'/workspace/scratch/0abb0718b9e3/MPL_46_002-048_work/scripts')
from record_page import save
save(47,r'''\scanpage{47}
Donc $\underline{\mathrm{Syst.lin.div}}_{X/S}$ est représentable ssi $\underline{\mathrm{Pic}}_{X/S}$ l'est.

\uline{Donnons nous} un syst. linéaire paramétré par $\check{P}/S$ de Br. Sév., et considérons la section correspondante $\xi$ de $\underline{\mathrm{Pic}}_{X/S}$.
\diagram{\begin{tikzcd}[column sep=large,row sep=large]
\underline L \arrow[d,phantom] & \underline L\otimes_S O_{\check P}(1)\otimes\underline N \arrow[d,phantom] \\
X \arrow[r,no head]\arrow[d,no head] & X\times_S\check P\arrow[d,no head] \\
S \arrow[r,no head] & \check P
\end{tikzcd}}

Je dis que $\xi$ \uline{est représentable par un $\underline L$ inversible sur $X$} \uline{ssi} \uline{$\check P$ est un fibré projectif}.
\margin{[$f:X\to S$ propre, $f_*(O_X)=O_S$ \unsure{univ\textsuperscript{t}}]}

Car la condition est suffisante \inserted{(\unsure{on sait par construction} $\unsure{\mathcal L}$ de $\xi$)}, prouvons qu'elle est nécessaire. \deleted{\unsure{Alors}} En effet, on a alors un Module de prés. finie $Q$ sur $S$, et un \inserted{mono}morphisme $\check P\longrightarrow P(Q)$, je dis que c'est un isom sur un $P(E)$, où $E$ est un quotient loc. libre de $Q$. Ce est par descente, avec le $=$ \unsure{principe} ---

\margin{Il suffit\par
$f_*(O_X)\simeq O_S$\par
et $f$ \deleted{\unsure{plat}} \inserted{de prés. finie}}

\margin{Si $X/S$ \unsure{adm} une section il est trivial que $\check P$ est ``trivial'', \unsure{car alors tout diviseur} \unsure{trivial} sur $X$ .....}
\figure{\begin{tikzpicture}\draw (0,2.6) -- (0,0.3) .. controls (0,0.05) and (0.12,0) .. (0.5,0);\end{tikzpicture}}

\uline{Remarque} Partant d'un Br. Sév. \unsure{non trivial}, on construit un $\xi$ ne provenant pas d'un $\underline L$ \unsure{au} $=$ \unsure{relation d'incidence can.}
\mspage{46}''',[
('text','top','Donc Syst.lin.div_X/S est représentable'),('text','next paragraph','Donnons nous un syst. linéaire'),('diagram','left middle','L; L⊗_S O_P̌(1)⊗N; X—X×_S P̌ / S—P̌'),('text','middle underlined assertion','Je dis que ξ est représentable'),('margin note','right below assertion','f:X→S propre, f_*(O_X)=O_S univᵗ'),('text','proof','Car la condition est suffisante'),('insertion','right of suffisante','on sait par construction L de ξ'),('deletion','before En effet','Alors'),('insertion','above morphisme','mono'),('display','within proof','P̌→P(Q)'),('text','continuation of proof','je dis que c’est un isom sur un P(E)'),('margin note','diagonal middle left','Il suffit f_*(O_X)≃O_S'),('deletion','inside middle left margin','plat'),('insertion','inside middle left margin','de prés. finie'),('margin note','diagonal lower left','Si X/S adm une section'),('drawing','left of last paragraph','long bracket'),('text','bottom remark','Remarque Partant d’un Br. Sév. non trivial'),('text','lower left foliation','46')],doubts=[('proof insertion','on sait par construction L de ξ','Compressed parenthesis joins the sufficiency clause; middle symbol uncertain','low'),('proof, last words','Ce est par descente, avec le = principe','Wording is compressed and not silently regularized','low'),('lower left margin','car alors tout diviseur trivial sur X','Several words weak even after rotation and enlargement','low'),('bottom remark','au = relation d’incidence can.','Small second line touches lower paper edge; proposed reading is particularly tentative','low')],notation=[('Underlined invertible sheaves',r'\underline L,\underline N','Keep manuscript underline; do not turn into calligraphic letters')],observation='Whole page, both halves, enlarged proof/last-line crops, and rotated marginal crops examined. The final remark and lower-left margin are the least secure text on this page. The incidence square has headless strokes and is typeset without supplying arrowheads.')
