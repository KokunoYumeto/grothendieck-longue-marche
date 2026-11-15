import sys
sys.path.insert(0,'MPL_93_002-046_work/tools')
from save_page import save_page
save_page(38,r'''\scanpage{38}
\margin{\figure{\begin{tikzpicture}\node[rotate=35] at (0,0) {\shortstack{Nouveau\\Chapitre}};\draw (-1.2,-1)--(1,.8)--(1,1.7);\end{tikzpicture}}}
1) Programme de la théorie de Dieudonné sur une base \inserted{$S$} où p est localement nilpotent.

 a) \uline{Foncteur de Dieudonné}. On \deleted{va} définiraun foncteur
\[
\diagram{\begin{tikzcd}
\underline D^*:\quad \mathrm{BT}(S)^0 \arrow[r] & \mathrm{Crisloclib}(S),
\end{tikzcd}}
\]
\margin{$\unsure{\mathbb D|D}^*$}
compatible aux images inverses (donc foncteur cartésien sur la catégorie fibrée des groupes de BT sur des bases où p est \unsure{loc.} nilp.). Si $S_0=\operatorname{Var}(p)$ on a une équivalence de catégories (cf.\qquad plus haut)
\[
\mathrm{Crisloclib}(S)\unsure{\approxeq|\simeq}\mathrm{Crisloclib}(S_0)
\]
de sorte que la donnée de $\underline D^*$ équivaut à la donnée de
\[
\diagram{\begin{tikzcd}
\underline D^*:\quad\mathrm{BT}(S_0)^0 \arrow[r] & \mathrm{Crisloclib}(S_0),
\end{tikzcd}}
\]
i.e. on est ramené \deleted{à la car. p.} au cas S de car. p. \deleted{\unsure{Pour connaitre, d}}
Dans le cas général, $\underline D^*(G)$ ne dépend que de $\deleted{\unsure{D^*}}G_0=G\times_S S_0$.

\deleted{\unsure{Utilis}} Plaçons nous sur $S_0$ de car. p. Utilisant $\underline f_G$ et $\underline V_G$ et la compatibilité de $\underline D^*$ aux images inverses, on voit que \deleted{le foncteur}
$\underline D^*(G_0)$ \deleted{peut}\inserted{$=M$} est naturellement muni de morphismes $F_M,V_M$ \deleted{satisfaisant}
\[
\diagram{\begin{tikzcd}
M^{(p)}=\underline f_S^*(M) \arrow[r,shift left,"F_M"] & M \arrow[l,shift left,"V_M"]
\end{tikzcd}}
\]
satisfaisant
\[
V_MF_M=p\operatorname{id}_M,\quad F_MV_M=p\operatorname{id}_{\unsure{M}}(p).
\]
On appelle un tel triple $(M,F_M,V_M)$ un (F-V-\uline{cristal}\inserted{ ou \uline{cristal de Dieudonné}}), et on a donc un foncteur
\[
\diagram{\begin{tikzcd}
\underline D^*:\quad\mathrm{BT}(S_0) \arrow[r] & \text{F-V-Cris}(S_0).
\end{tikzcd}}
\]
C'est ce foncteur qui mérite le nom de \uline{foncteur de Dieudonné}. On \deleted{\unsure{pouve|prouve}} \deleted{prouve que} voit que sa formation commute à tout changement de\inserted{ }base. De plus, on prouve que pour $S_0$ spectre d'un corps parfait, il coïncide \deleted{avec} à isomorphisme canonique près avec le foncteur de Dieudonné habituel, qui est alors une équivalence de catégories, de sorte que dans ce cas la
\margin{37}
''','typed',[
('margin note','upper left','Nouveau Chapitre'),('drawing','upper left','angular outline of marginal label'),('text','title','1) Programme de la théorie de Dieudonné'),('insertion','title after base','S'),('text','a heading','Foncteur de Dieudonné'),('deletion','a first sentence','va'),('diagram','first display','D* BT(S)^0 to Crisloclib(S)'),('margin note','left of first display','D*'),('text','upper continuation','compatible aux images inverses'),('display','upper middle','Crisloclib equivalence'),('text','middle','de sorte que la donnée'),('diagram','middle display','D* BT(S_0)^0 to Crisloclib(S_0)'),('text','middle','i.e. on est ramené'),('deletion','middle line','à la car. p.'),('deletion','middle line right','Pour connaitre, d'),('text','middle','Dans le cas général'),('deletion','before G_0','D*'),('deletion','next paragraph start','Utilis'),('text','next paragraph','Plaçons nous sur S_0'),('deletion','line before M','le foncteur'),('deletion','after D*(G_0)','peut'),('insertion','above peut','=M'),('deletion','after F_M,V_M','satisfaisant'),('diagram','lower middle','M^(p) right F_M left V_M M'),('text','before identities','satisfaisant'),('display','lower middle','V_MF_M and F_MV_M'),('text','lower','On appelle un tel triple'),('insertion','above F-V-cristal','ou cristal de Dieudonné'),('diagram','lower','D* BT(S_0) to F-V-Cris(S_0)'),('text','bottom paragraph','C’est ce foncteur'),('deletion','after On','pouve'),('deletion','next line','prouve que'),('insertion','between de and base','word separation stroke'),('deletion','after coïncide','avec'),('margin note','bottom left','37')
],[
('a, first sentence','définiraun','définira un','high','The printed a and u have no intervening blank; literal fusion retained.'),('left margin D','mathbb D','D','medium','The handwritten vertical is doubled.'),('upper paragraph after p est','loc.','','medium','Last character and punctuation are obscured by a dark overprint.'),('Crisloclib equivalence sign','approxeq','simeq','medium','Two wavering strokes and a lower horizontal are visible.'),('middle, cancelled phrase','Pour connaitre, d','','low','Typed x cancellation covers the accent and final partial word; visible letters retained.'),('before G_0, cancellation','D*','','low','Dense overtyping obscures the base character.'),('start next paragraph, cancellation','Utilis','','low','Tentative partial word under x cancellation; enlarged inspection leaves uncertainty.'),('identity F_MV_M','id_M(p)','id at M^(p)','high','M is low, while (p) appears on the main line; retained without normalizing the formula.'),('bottom, first deleted word after On','pouve','prouve','low','Cancellation leaves pouve-like letters; the more usual spelling is not silently substituted.')
])
