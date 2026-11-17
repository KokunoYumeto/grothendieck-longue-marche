from workflow import save_page
tex=r'''\scanpage{20}
\mspage{9}
\margin{19}

et

2°) Comment interpréter toute la structure de graphe orienté à plongement cellulaire, avec pondérations des arêtes et des coins, en termes de l'interprétation de ses sommets \deleted{\unsure{en termes}} \inserted{comme} des str. polygonales sur $\widetilde I$.

\deleted{\unsure{Pour}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[orange!85!black,line width=2pt] (-.8,-.7)--(.85,1.3) (.8,-.65)--(-.3,1.25) (0,-1)--(.18,1.3) (2.6,-1)--(3.3,1.1) (3.4,-.95)--(2.8,1);
\draw[yellow!65!green,line width=1.3pt] (-1.5,0)--(3.7,.1);
\draw[yellow!65!green,line width=1.3pt,dashed] (-.9,.02)..controls(-.4,.4)and(-.15,1)..(.25,.8)..controls(.6,.7)and(.9,.1)..(1.6,.07);
\draw[green!35!black,line width=3pt] (-.4,.09)--(.6,.09);
\draw[black,line width=1.2pt] (.07,.68)--(.36,.68) (.01,1.07)--(.38,1.07);
\draw[->] (-.6,.1)--(-.6,.4);\draw[->] (.8,.12)--(.8,.45);
\node[right] at (3.7,.1) {$D$};\node[right] at (.45,.8) {$D'$};
\end{tikzpicture}}

Pour 1°) L'examen de la situation \inserted{($D\to D'$ dans le cas ``ordinaire'' ($D'$ non supercritique))} montre que $\unsure{\widehat{\operatorname{Pol}}(D)}$ et $\unsure{\widehat{\operatorname{Pol}}(D')}$, i.e. l'ens des arêtes sur $\widetilde{\widetilde D}$ et sur $\widetilde{\widetilde D'}$ (où le $\approx$ indique la ``parallèle'') \inserted{i.e. des demi-arêtes en $D$ et en $D'$} sont les ``$=$'', \deleted{\unsure{et}} \uline{sauf} \deleted{sur les} au voisinage des deux paquets de points antipodiques, correspondant \deleted{aux} en $D$ à \inserted{l'éclatement de} l'arête de spécialisation issue de $D$ (\unsure{et de son l'antipodique}), et en $D'$ l'inverse. De façon plus précise,

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\coordinate (D) at (0,0);\coordinate (E) at (.5,2.1);
\draw[orange!85!black,line width=2.5pt] (D)--(E);
\draw[->,black] (D)--(E) node[midway,left] {$a$};
\foreach \p in {(-1,-.65),(-.5,.65),(.8,-.6),(1,.3)}{\draw[yellow!65!green,line width=2pt] (D)--\p;\draw[dashed] (D)--\p;}
\draw[yellow!65!green,line width=2pt,dashed] (0,0)--(-.15,-1.3);\node[left] at(-.15,-1.3){$a'$};
\foreach \p in {(-.5,2.65),(-.7,2),(.95,1.7),(1.4,2.5)}{\draw[yellow!65!green,line width=2pt] (E)--\p;\draw[dashed] (E)--\p;}
\draw[yellow!65!green,line width=2pt] (E)--(.8,3);\draw[->] (.8,3)--(E);\node[right]at(.8,2.9){$a'$};
\draw[orange!85!black,line width=2pt] (E)--(.2,1.55) (E)--(.75,1.6);
\draw[blue!60!black] (-.45,-.25) arc[start angle=210,end angle=270,radius=.5];\node at(-.45,-.5){$\alpha$};
\draw[blue!60!black,dashed] (.15,-.47) arc[start angle=290,end angle=350,radius=.5];\node at(.6,-.5){$\beta$};
\draw[blue!60!black] (0,1.95) arc[start angle=210,end angle=270,radius=.5];\node at(-.1,1.65){$\alpha'$};
\draw[blue!60!black,dashed] (.62,1.63) arc[start angle=290,end angle=350,radius=.5];\node at(1,1.65){$\beta'$};
\node[fill=white,inner sep=.5pt] at(D){$D$};\node[fill=white,inner sep=.5pt]at(E){$D'$};
\node at(-.65,-1){$\deleted{\unsure{a}}$};
\end{tikzpicture}}

\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw[orange!85!black,line width=2pt] (.2,-.7)--(1,1) (1.1,-.8)--(.4,1.1) (2.2,-.9)--(3,1.5) (3.3,-1)--(2.5,1.5) (2.85,-.9)--(2.8,1.6) (4.6,-.8)--(4.6,1) (5.1,-.7)--(5.8,1.1) (5.8,-.7)--(5.2,1);
\draw[yellow!65!green,line width=1.4pt] (0,0)--(6,.04);
\draw[yellow!65!green,line width=1.4pt,dashed] (1.4,0)..controls(2,.05)and(2.3,1.3)..(2.8,.8)..controls(3.3,1.2)and(3.8,.1)..(4.1,.02);
\draw[brown!60!black] (0,.22)--(5.8,.25) (0,-.25)--(5.8,-.3);
\draw[brown!60!black,dashed] (.95,.24)..controls(1.6,.3)and(2.3,1.9)..(2.8,1.2)..controls(3.2,1.6)and(3.8,.4)..(4.2,.24);
\draw[brown!60!black,dashed] (1.2,-.26)..controls(2,-.1)and(2.3,.75)..(2.8,.5)..controls(3.1,.8)and(3.5,-.1)..(4,-.27);
\draw[black,line width=1pt] (2.55,1.3)--(3.01,1.3) (2.55,.62)--(3.03,.62);
\draw[->] (1.25,-.85)--(2.65,.2);\node[below]at(1.25,-.85){$\sigma$};
\draw (3.9,1.6)--(2.9,.65);\node[right]at(3.9,1.6){$\sigma'$};
\node[right] at(6,.04){$D$};\node[right]at(3.25,.78){$D'$};
\end{tikzpicture}}

\uline{on trouve un isomorphisme canonique entre $\widehat P(D)$ et $\widehat P(D')$} transformant l'un des sommets $\sigma$ de $\widehat P(D)$ provenant de $\bar a$ en \deleted{\unsure{un}} l'un \uline{antipodique} \deleted{\unsure{que}} de l'un des sommets $\sigma'$ de $\widehat P(D')$ correspondant à $\bar a$. Une autre façon de le dire est celle-ci : Désignons par $a'$ l'arête de spécialisation ``opposée'' à $a$ (en $D'$), on trouve un isom des polygônes $\operatorname{Pol}(D)$ au \deleted{$\operatorname{Pol}(D')$,} \deleted{\unsure{un polygône}} \deleted{$\operatorname{Pol}(D')$, transformant} \deleted{\unsure{transformant en} $a$ \unsure{et l'image}} polygône déduit \deleted{\unsure{de}} de $\operatorname{Pol}(D')$ en retirant le sommet $a$, de sorte que $a$ aille sur $a'$.

\margin{\unsure{annulé;} cf plus bas !}

\deleted{Cet isomorp} \deleted{De plus,} on peut \inserted{donc} trouver un unique côté $\gamma$ de $D$, tel que le polygône \deleted{\unsure{déduit}} $\operatorname{Pol}'(D)$ déduit de $\operatorname{Pol}(D)$ en plaçant un point $a''$ dessus, soit isom. à $\operatorname{Pol}(D')$ par un isom prolongeant le précédent. De plus, cet isom est compatible avec les pondérations dans le sens suivant : deux \deleted{sommets} \inserted{sommets des polygônes (ou arêtes de $\Gamma(\underline\Sigma)$)} qui se correspondent ont $=$ pondérations (on donnant à $a''$ la pondération de $\alpha$), et aussi
'''
e=[('text','top left','et; 2°) Comment interpréter toute la structure'),('deletion','left upper','en termes'),('insertion','left upper','comme'),('deletion','left middle','Pour'),('drawing','left middle','D; D prime; concurrent orange lines; two upward arrows'),('text','left lower middle','Pour 1°) L’examen de la situation'),('insertion','left lower middle','D→D prime dans le cas ordinaire'),('display','left lower middle','Pol hat(D); double tilde D'),('insertion','centre left','i.e. des demi-arêtes en D et en D prime'),('deletion','left lower','et; sur les; aux'),('insertion','left lower','l’éclatement de'),('drawing','left bottom margin','two vertices D,D prime; a,a prime; α,β,α prime,β prime'),('deletion','left bottom drawing','a scribble'),('drawing','left bottom','parallel curves and specialization; σ,σ prime; D,D prime'),('text','bottom left to right top','on trouve un isomorphisme canonique'),('deletion','right upper','un; que'),('text','right upper middle','Une autre façon de le dire'),('deletion','right middle','Pol(D prime); un polygône; transformant; image'),('margin note','centre right margin','annulé; cf plus bas !'),('text','right middle','polygône déduit de Pol(D prime)'),('deletion','right middle lower','Cet isomorp; De plus; déduit'),('insertion','right middle lower','donc'),('text','right lower','on peut trouver un unique côté γ'),('display','right lower','Pol prime(D); point a double prime'),('text','right bottom','cet isom est compatible avec les pondérations'),('deletion','right bottom','sommets'),('insertion','right bottom','sommets des polygônes (ou arêtes de Γ(Σ))')]
d=[('left main construction','Pol hat(D), Pol hat(D prime)','Accents crowded with the inserted line above; mark hats doubtful','medium'),('left antipodal clause','et de son l’antipodique','Dense overwritten phrase; exact conjunction/word division uncertain','low'),('right upper','l’un antipodique; que','Overwriting before antipodique; retain visible word with its nonstandard syntax','low'),('right cancellations','transformant en a et l’image; annulé','Several overlapping cancellation strokes; margin links to revision below','low'),('right last line','on donnant','Ink appears on rather than en; no grammatical normalization','medium')]
obs='Open numbered question 2 asks to recover the full oriented cellular graph and weights from polygon structures on tilde I. Construction of canonical isomorphism between refined polygons under specialization, with antipodal correspondence. Right-margin “annulé; cf plus bas!” flags a revised coarse polygon statement; removed vertex is replaced in next live paragraph by inserting a new point a double prime on a unique side γ. Weight-compatibility assertion continues. Distinguish σ in main geometric drawing, a for graph edges, and α/β for blue sectors.'
save_page(20,tex,e,d,obs)
