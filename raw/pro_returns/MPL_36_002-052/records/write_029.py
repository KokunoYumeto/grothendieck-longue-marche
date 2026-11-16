from save_page import save
tex=r'''
\scanpage{29}

$\Gamma=\mathbb G$

\margin{$M\times B'\qquad\operatorname{Ext}(B',DM)$

$\deleted{\operatorname{Hom}(B',\operatorname{Ext}(\unsure{M},\unsure{\mathbb G_m}))}=0$}

\diagram{\begin{tikzcd}[row sep=small,column sep=small]
B & B'\\
M \arrow[u,"i"] & M' \arrow[u,"i'"']
\end{tikzcd}}
\quad une biext.\inserted{$\mathcal E$} sous $\mathbb G_m$

\diagram{\begin{tikzcd}[column sep=small]
B' \arrow[r,"\alpha'"] & \underline{\operatorname{Ext}}(B,G_m) \arrow[r,no head] & \underline{\operatorname{Ext}}(M,G_m)
\end{tikzcd}}
nul\quad p.c. $\operatorname{Hom}(B',\underline{\operatorname{Ext}}(M,G_m))\overset{\unsure{\Vert}}{=}0$

\diagram{\begin{tikzcd}[column sep=small]
B \arrow[r,no head,"\alpha"] & \underline{\operatorname{Ext}}(B',G_m) \arrow[r,no head] & \underline{\operatorname{Ext}}(M',G_m)
\end{tikzcd}}
nul\quad p.c. $\operatorname{Hom}(B,\underline{\operatorname{Ext}}(M',G_m))=0$

d'où extensions,

\diagram{\begin{tikzcd}[column sep=small,row sep=tiny]
\unsure{\bullet|0} \arrow[r,no head] & DM \arrow[r,"{\unsure{j'}}"] \arrow[d,equal] & \unsure{G'|C'} \arrow[r,no head,"p'"] & B' \arrow[r] & 0\\
 & T' & & &
\end{tikzcd}}

\margin{\rule{0.8\linewidth}{0.3pt}
$\mathcal E_{M,G'}$ est \unsure{canoniqt} splitté par $\rho$
\rule{0.8\linewidth}{0.3pt}}

\diagram{\begin{tikzcd}[column sep=small,row sep=tiny]
\unsure{\bullet|0} \arrow[r] & DM' \arrow[r,no head,"{\unsure{j}}"] \arrow[d,equal] & \unsure{G|C} \arrow[r,no head,"p"] & B \arrow[r] & 0\\
 & T & & &
\end{tikzcd}}

\margin{$\mathcal E_{G,M'}$ est can. splitté $\rho'$
\rule{0.8\linewidth}{0.3pt}}

\uline{\unsure{Exemple}} si \deleted{\unsure{par}} $\uline{\alpha'}$ \deleted{\unsure{était}} \inserted{\unsure{est}} un isom, alors $i'$ \unsure{revient à se donner}

un $i'\in\unsure{\operatorname{Hom}}(M',\underline{\operatorname{Ext}}(B,G_m))$
\diagram{\begin{tikzcd}[column sep=small]
\unsure{\operatorname{Hom}}(M',\underline{\operatorname{Ext}}(B,G_m)) & \operatorname{Biext}(B,M';G_m) \arrow[l,"\sim"'] & \deleted{\unsure{\operatorname{Hom}}}\inserted{\operatorname{Ext}(B,D(M'))} \arrow[l,"\sim"']
\end{tikzcd}}

\margin{si $\unsure{\operatorname{Ext}}(M',\underline{\operatorname{Hom}}(B,G_m))=0$

p.ex.
\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {$\underline{\operatorname{Hom}}(B,G_m)=0$};\draw (0,0) ellipse (1.35 and 0.28);\end{tikzpicture}}}

\margin{si $\operatorname{Hom}(B,\underline{\operatorname{Ext}}(M',G_m))=0$ p.ex.
\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {$\underline{\operatorname{Ext}}(M',G_m)=0$};\draw (0,0) ellipse (1.40 and 0.32);\end{tikzpicture}}}

\unsure{aussi} \unsure{pour}. Donc la donnée de $i'$ \unsure{équivaut à} celle de l'ext. $G$. Et réciproquement.

Considérons l'image inverse\inserted{\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {$\mathcal E_{i,i'}$};\draw (0,0) ellipse (0.43 and 0.32);\end{tikzpicture}}}
de $\mathcal E$ sur $(M,M')$. Alors des \unsure{splittages}\inserted{$\unsure{\rho_i}$} de cette biextension correspondent aux hom $j$ de $M$ dans $G$ relevant $i$, \unsure{aux hom}\,$j'$ de $M'$ dans $G'$ relev. de $i'$.

\diagram{\begin{tikzcd}[row sep=tiny,column sep=small]
M \arrow[r,no head] & G \arrow[r,no head] & B\\
M' \arrow[r,no head] & G' \arrow[r,no head] & B'
\end{tikzcd}}

\figure{\begin{tikzpicture}[baseline=(t.base)]\node (t) {\deleted{\unsure{sur $k$}}};\draw (0,0) ellipse (0.60 and 0.23);\end{tikzpicture}}

\inserted{Deux relèvements} \deleted{\unsure{si}} $j$ et $j'$ \deleted{\unsure{se}} \unsure{se correspondent ainsi},

\deleted{\unsure{Alors on trouve un} splitt. $\sigma$ canonique \deleted{$\unsure{\sigma'}$} de $\mathcal E_{G,M'}$ et un splitt. $\sigma'$ canonique de $\mathcal E_{M,G'}$, ces deux splittages coïncident sur $M,M'$ avec le splittage \unsure{donné} $h$ de $\mathcal E_{M,M'}$.}

ssi les deux splittages de $\mathcal E_{M,M'}$, déduits d'une part du splittage $\rho$ de $\mathcal E_{M,G'}$ \unsure{et de} $j':M'\longrightarrow G'$, d'autre part du splittage $\rho'$ de $\mathcal E_{G,M'}$ et de $j:M\longrightarrow G$, coïncident.

\margin{28}
'''
e=[('display','top left','Gamma = blackboard G'),('margin note','top right','M x B prime; Ext(B prime,DM)'),('deletion','top right under Ext','Hom(B prime,Ext(M,G_m))'),('display','top right end of cancelled formula','=0'),('diagram','upper left','M -> B; M prime -> B prime'),('text','upper beside small diagram','une biext. sous G_m'),('insertion','above biext. line','E'),('diagram','upper first Ext row','B prime alpha prime Ext(B,G_m) Ext(M,G_m)'),('text','upper first Ext row continuation','nul p.c.'),('display','upper right first row','Hom(B prime,Ext(M,G_m))=0'),('diagram','upper second Ext row','B alpha Ext(B prime,G_m) Ext(M prime,G_m)'),('text','upper second Ext row continuation','nul p.c.'),('display','upper right second row','Hom(B,Ext(M prime,G_m))=0'),('text','middle introduction','d’où extensions'),('diagram','middle first extension','DM=T prime; G prime; B prime; p prime'),('margin note','right of first extension','E_M,G prime est canoniqt splitté par rho'),('drawing','above/below first marginal statement','horizontal enclosing rules'),('diagram','middle second extension','DM prime=T; G; B; p'),('margin note','right of second extension','E_G,M prime est can. splitté rho prime'),('drawing','under second marginal statement','horizontal rule'),('text','middle example','Exemple si alpha prime est un isom'),('deletion','example before alpha prime','par uncertain'),('deletion','example after alpha prime','était uncertain'),('insertion','above cancelled verb','est uncertain'),('display','example continuation','i prime in Hom(M prime,Ext(B,G_m))'),('diagram','example equivalences','Hom <- Biext <- Ext(B,D(M prime))'),('deletion','right object of example equivalence','Hom uncertain'),('insertion','above right object','Ext(B,D(M prime))'),('margin note','below left equivalence','si Ext(M prime,Hom(B,G_m))=0 p.ex.'),('drawing','below left equivalence','Hom(B,G_m)=0 oval'),('margin note','below right equivalence','si Hom(B,Ext(M prime,G_m))=0 p.ex.'),('drawing','below right equivalence','Ext(M prime,G_m)=0 oval'),('text','below equivalence notes','Donc la donnée de i prime'),('text','lower new paragraph','Considérons l’image inverse'),('insertion','above image inverse de','E_i,i prime'),('drawing','around inserted E_i,i prime','oval'),('insertion','above splittages','rho_i uncertain'),('text','lower paragraph continuation','splittages de cette biextension'),('diagram','interlinear lower centre','M - G - B; M prime - G prime - B prime'),('deletion','circled interlinear phrase','sur k uncertain'),('drawing','interlinear right of small diagram','oval around cancelled sur k'),('insertion','lower left above relèvements','Deux relèvements'),('deletion','lower left before j','si uncertain'),('text','lower line before cancelled block','j et j prime se correspondent ainsi'),('deletion','same line small cancelled fragment','se uncertain'),('deletion','lower large crossed block','Alors on trouve un splitt. sigma canonique'),('deletion','inside crossed block','sigma prime uncertain'),('text','bottom final paragraph','ssi les deux splittages de E_M,M prime'),('margin note','bottom left pencil','28')]
d=[{'line':'top deleted formula','reading':'Hom(B prime,Ext(M,G_m))','alternatives':'inner M and G_m obscured','confidence':'low'},{'line':'top vanishing annotations','reading':'Hom(...)=0','alternatives':'equality written vertically at edge, first sign uncertain','confidence':'medium'},{'line':'middle extension diagrams','reading':'j prime, j; G prime, G','alternatives':'j/d; G/C','confidence':'low'},{'line':'right marginal splitting statement','reading':'canoniqt','alternatives':'abbreviation ending uncertain','confidence':'low'},{'line':'example opening','reading':'Exemple si [par deleted] alpha prime [était deleted] [est inserted] un isom','alternatives':'overwritten initial phrase/verb','confidence':'low'},{'line':'example text','reading':'revient à se donner','alternatives':'compressed words','confidence':'low'},{'line':'example Hom expression','reading':'Hom(M prime,Ext(B,G_m))','alternatives':'operator nearly horizontal','confidence':'low'},{'line':'example right rewritten object','reading':'deleted Hom; inserted Ext(B,D(M prime))','alternatives':'old operator uncertain','confidence':'low'},{'line':'after example','reading':'aussi pour; Donc la donnée de i prime équivaut à','alternatives':'first two words and equivalence verb very compressed','confidence':'low'},{'line':'lower paragraph','reading':'splittages; inserted rho_i; aux hom j prime','alternatives':'abbreviation/inserted label and compressed linking text','confidence':'low'},{'line':'lower interlinear cancellation','reading':'sur k','alternatives':'two cancelled tokens','confidence':'low'},{'line':'lower heavily cancelled block','reading':'Alors on trouve un splitt. sigma canonique ... donné h','alternatives':'opening and donné uncertain; complete best reading retained','confidence':'low'},{'line':'bottom final paragraph','reading':'et de j prime','alternatives':'linking words compressed','confidence':'medium'}]
save(29,tex,e,d,'Biextension E under G_m, maps i:M->B and i-prime:M-prime->B-prime, construction of torus extensions and canonical splittings. Example assumes alpha-prime an isomorphism and compares Hom(M-prime,Ext(B,G_m)), Biext(B,M-prime;G_m), Ext(B,D(M-prime)); vanishing conditions noted below. Final live criterion pairs lifts j,j-prime when two induced splittings agree on E_M,M-prime; an earlier extended formulation is crossed out. Many extreme cursive contractions and overwriting: this page needs cautious use; hypotheses cannot be supplied from the expected duality theory. Faint reverse-side show-through is not treated as front-side writing.')
