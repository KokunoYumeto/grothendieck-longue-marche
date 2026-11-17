from workflow import save_page
tex=r'''\scanpage{22}
\mspage{10}
\margin{21}

deux secteurs angulaires (ou arêtes de $\operatorname{Pol}'(D)$, $\operatorname{Pol}(D')$) quand celles en $D$ sont pondérées, i.e. à l'exception \unsure{des deux cas des} arêtes \deleted{\unsure{de}} $\alpha,\beta$ \deleted{\unsure{des demi-arêtes}} qui découpent l'arête $\gamma$, et qui ne sont pas encore pondérées. La formule des pondérations implique alors qu'on doit avoir, pour les arêtes $\alpha',\beta'$ correspondantes de $\operatorname{Pol}(D')$
\[
\deleted{\operatorname{poids}(\alpha')+\operatorname{poids}(a'')+}
\]
\[
\operatorname{poids}(\alpha')+\operatorname{poids}(\beta')+\operatorname{poids}(a)=\operatorname{poids}(\gamma)
\]

\uline{NB} Il est commode d'augmenter le polygône $\operatorname{Pol}(D)$ en $\unsure{\overline{\operatorname{Pol}}(D)^*}$, en rajoutant, en tt sommet \deleted{\unsure{qui ne}} \inserted{correspondant} à une arête de spécialisation \deleted{\unsure{quelconque}} $a:D\mathbin{-}D'$ de $\Gamma(\underline\Sigma)$, une ``antipodique'' mais considérée comme arête \deleted{\unsure{orientée}} à bout libre (ayant une origine, mais pas d'extrémité) --- ceci ne rajoute pas d'autres sommets à $\Gamma(\underline\Sigma)$, seult des arêtes libres. Mais tte flèche de spécialisation $D\to D'$ induit un iso
\[
P^*(D)\mathbin{-}P^*(D')
\]

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[yellow!65!green,line width=1.4pt] (-3.5,-.5)..controls(-3.7,3.2)and(3.2,3.5)..(3.3,-.9);
\draw[brown!60!black] (-3.7,.25)..controls(-2.5,3.6)and(3.25,3.4)..(3.3,-.5);
\draw[brown!60!black] (-3.3,.25)..controls(-2.5,2.9)and(2.9,2.9)..(3.05,-.5);
\draw[orange!85!black,line width=2pt] (-3.5,.2)--(-2.9,1.8) (-3.65,1.6)--(-2.6,.65) (-3.8,1.35)--(-2.65,1.3);
\draw[orange!85!black,line width=2pt] (-2.1,1.2)--(-2.1,2.6) (-2.7,2.25)--(-1.9,1.3);
\draw[orange!85!black,line width=2pt] (-.95,1.9)--(-.6,2.95) (-.6,1.85)--(-.6,3) (-.3,1.95)--(-.8,2.95);
\draw[orange!85!black,line width=2pt] (.6,1.75)--(1.45,2.95) (1.13,1.5)--(1.15,3.05);
\draw[orange!85!black,line width=2pt] (1.6,1.4)--(2.1,2.3) (1.95,1.3)--(1.9,2.4) (1.1,1.3)--(2.35,1.85);
\draw[orange!85!black,line width=2pt] (2.2,.95)--(3.1,1.7);
\draw[orange!85!black,line width=2pt] (2.75,.1)--(3.75,.8) (3.1,.05)--(3.7,1) (2.9,.85)--(3.85,.2);
\draw[black,line width=2.5pt] (-3.35,.6)--(-3.12,1.3) (-3.04,.55)--(-2.81,1.25) (-2.43,2)--(-2.1,2.2) (-2.3,1.75)--(-2.03,1.91) (-.85,2.68)--(-.37,2.69) (-.85,2.32)--(-.38,2.32) (.92,2.46)--(1.29,2.36) (.78,2.16)--(1.21,2.04) (1.84,2.03)--(2.12,1.8) (1.67,1.73)--(1.94,1.53) (3.05,.68)--(3.26,.03) (2.77,.7)--(2.97,.07);
\end{tikzpicture}}

La réflexion en termes de $P(D)\mathbin{-}P(D')$ est trompeuse, en effet \inserted{dans le triangle de spécialisation} les triangles de spécialisation (\unsure{non}, en dehors \inserted{s'il y en a} attenant à $T$ \deleted{peuvent} \inserted{sont} disponibles comme tels --- il faudrait donc indiquer la \uline{relation d'adjacence} des triangles de spécialisation de \deleted{$\unsure{\Gamma(\underline\Sigma)}$} $D$, comme faisant partie de la structure de $\Gamma(\underline\Sigma)$ ---

\margin{\uline{NB} elle est déterminée en fait par la structure des pondérations.}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[orange!85!black,line width=2pt] (-.65,-1.25)--(.65,1.65) (.75,-1.25)--(-.5,1.65) (.05,-1.25)--(.05,1.6) (.8,-1.5)--(1.55,.4);
\draw[yellow!65!green,line width=1.4pt] (-1.4,-.4)--(2.1,0);
\draw[yellow!65!green,line width=1.4pt,dashed] (-1.4,-.4)..controls(-.9,-.2)and(-.35,1.2)..(.05,.9)..controls(.4,1.15)and(.45,.1)..(.8,-.1);
\fill (.05,.9) circle (2pt);
\draw[black,line width=2.5pt] (-.1,.65)--(.2,.65) (-.35,-.15)--(.4,-.05);
\draw[black,line width=2.5pt,dashed] (.45,-.04)--(1.3,.06);
\end{tikzpicture}}

et la structure supplémentaire s'obtiendrait en collant d'abord au $\operatorname{Pol}(D)$ les triangles de spécialisation (s'il y en a) qui sont attenants à $T$, soit $\operatorname{Pol}(D,\unsure{a})$ \deleted{\unsure{Ce}} ce nouveau polygône. On peut aussi, \unsure{tout autant}, augmenter \deleted{$\operatorname{Pol}$} $\operatorname{Pol}(D)$, \deleted{$\operatorname{Pol}(D')$}, en y incluant des arcs des \unsure{faux bords} des ``pseudo-triangles de spécialisation'', dont

\margin{oui, et semble plus élégant}
'''
e=[('text','top left','deux secteurs angulaires'),('deletion','left upper','de; des demi-arêtes'),('display','left middle','cancelled poids(α prime)+poids(a double prime)+'),('deletion','left middle display','poids(α prime)+poids(a double prime)+'),('display','left middle','poids(α prime)+poids(β prime)+poids(a)=poids(γ)'),('text','left lower middle','NB Il est commode d’augmenter le polygône'),('deletion','left lower middle','qui ne; quelconque; orientée'),('insertion','left lower middle','correspondant'),('text','left lower','arête à bout libre; pas d’autres sommets'),('display','left bottom','P star(D) − P star(D prime)'),('drawing','top centre','curved green line between brown curves and orange crossing groups'),('text','right upper','La réflexion en termes de P(D) − P(D prime)'),('insertion','right upper','dans le triangle de spécialisation'),('insertion','right middle','s’il y en a'),('deletion','right middle','peuvent; Γ(Σ)'),('insertion','right middle','sont'),('text','right middle','relation d’adjacence des triangles'),('margin note','right edge','NB elle est déterminée en fait'),('drawing','centre lower','triangle with green deformation; black marks; orange crossing'),('text','right lower','la structure supplémentaire s’obtiendrait'),('display','right lower','Pol(D,a)'),('deletion','right lower','Ce; Pol; Pol(D prime)'),('text','right bottom','On peut aussi; pseudo-triangles de spécialisation'),('margin note','gutter bottom','oui, et semble plus élégant')]
d=[('top left exception','des deux cas des arêtes','Compressed phrase, grammar not repaired','low'),('left NB augmented polygon','overline Pol(D) star; qui ne; quelconque; orientée','Accent and cancellations uncertain; bottom P-star notation retained separately','low'),('right qualification before T','non, en dehors; s’il y en a','Parenthesis and insertion are crowded, attachment uncertain','low'),('right final augmentation','tout autant; faux bords','The first phrase and word preceding bords remain uncertain','low')]
obs='NB adds free-ended antipodal edges, claimed to give an iso P*(D)—P*(D prime) for every specialization. Main warning: “La réflexion en termes de P(D)—P(D prime) est trompeuse”; adjacency of specialization triangles must be recorded, with marginal claim that weights determine it. Proposed added structure via attached triangles/pseudo-triangles; margin “oui, et semble plus élégant”. Sum formula poids(α prime)+poids(β prime)+poids(a)=poids(γ). Later continuation needed.'
save_page(22,tex,e,d,obs)
