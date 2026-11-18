from save_page import save
text=r'''\scanpage{15}
Après \unsure{l'axiome} d'asphéricité : \unsure{corps de} \unsure{Loc 4|Loc 1}, Loc 2, Loc 3,

(\uline{Loc} 1 sous forme faible

a) iso dans $\underline W$

b) si deux parmi $g,f,gf$ dans $\underline W$, le 3e l'est

c) $gf=\mathrm{id}$ et $fg\in\underline W\Rightarrow f,g\in\underline W$)

\textcircled{0} Axiomes Loc mettons au net \unsure{les props} \unsure{constructions} fibs et cofib.

\textcircled{1} \uline{Dualité} (y compris $\underline W=\underline W^\circ$)

\margin{\textcircled{2} Commentaire sur fibrations cofibrations imm. ouvertes, '' fermées Cylindres Cônes \ldots}

\deleted{\textcircled{2}}\inserted{\textcircled{3}} \unsure{a)} Soit des
\diagram{\begin{tikzcd}[column sep=small,row sep=small]
\left\{\vphantom{\begin{matrix}Y\\X_1\end{matrix}}\right.\!Y\arrow[r]\arrow[d]&X_0\\X_1&
\end{tikzcd}}

\diagram{\begin{tikzcd}[column sep=large,row sep=large]
Y\arrow[r,"f_0"]\arrow[d,"f_1"']\arrow[dr,"\deleted{\unsure{\beta}}" description]&X_0\arrow[d,"\alpha_1"]&\\
X_1\arrow[r,"\deleted{\unsure{q_1}}\ \unsure{\lambda_g}","\unsure{\alpha_0}\ \deleted{\unsure{q_0}}"']&\Sigma\arrow[dr]&\\
&&X_0\amalg_Y X_1
\end{tikzcd}}

et passage : la limite

\deleted{Si $f_0$ iso, $q_0$ homotopisme}

a) \uline{Fonctorialité} si $u_Y,u_{X_0},u_{X_1}\in\underline W$, alors $(\Sigma\to\Sigma')\in\underline W$

b) Si $f_0$ iso, alors $\unsure{\alpha_0}$ homotopisme (it. $f_1,\alpha_1$

c) Si $f_0\in\underline W$, alors $\unsure{\alpha_0}\in\underline W$ (it. $f_1,\alpha_1$)

\deleted{\textcircled{\unsure{3}}}\inserted{\textcircled{4}} \deleted{\textcircled{\unsure{a}}} \uline{Thm} du

\margin{``de la somme amalgamée'' (dans (Cat))}

\diagram{\begin{tikzcd}
Y\arrow[r,"f_0"]\arrow[d,"f_1"']&X_0\arrow[d,"q_1"]\\
X_1\arrow[r,"q_0"']\arrow[ur,phantom,"\mathrm{cart}" description]&X
\end{tikzcd}}

avec $q_0,q_1$ cofibrations (resp. fibrations)

Supposons que $\forall x\in X$, $X_{0x}$ \unsure{ou} $X_{1x}$ sont \deleted{\unsure{quasi}} \inserted{$\underline W$-}asphériques. Alors

\diagram{\begin{tikzcd}
\left\{\begin{gathered}Y\longrightarrow X_0\\\downarrow\hspace{1.6cm}\\X_1\hspace{1.6cm}\end{gathered}\right.\arrow[r]&X
\end{tikzcd}}

cofib (resp. fib) à fibres triviales, donc $U\underline W$.

\margin{\uline{NB} Si on suppose \deleted{\unsure{en}} que $\forall a\in X$,
\deleted{$\unsure{X_{0a}}$ \unsure{ou} $\unsure{X_{1a}}$ \unsure{soit}}\inserted{tels que l'une des}
\deleted{\unsure{cat. ponctuelles}, \unsure{l'une des}}
\deleted{\unsure{cat.}} $X_{0a},X_{1a}$ soit $\varnothing$, l'autre soit isom. à $\Delta_0$, alors ce diagramme est cocartésien, et le reste par tt chgt de base (\unsure{ci voir près})}

\uline{Cor.} Si $f_0\in\underline W$, alors $q_0\in\underline W$

Si $f_1\in\underline W$, alors $q_1\in\underline W$

Cas
\diagram{\begin{tikzcd}
Y\arrow[r,hook,"i"]\arrow[d,"f"']&X\arrow[d,"g"]\\
Y'\arrow[r,dash,"i'"']&X'=X\amalg_Y Y'
\end{tikzcd}}

$i$ imm. ouverte ou fermée

\uline{Question} --- si $f$ \unsure{asphérique|cofibré}, il n'en résulte pas que $g$ le soit, et si $f\in\underline W$, il est possible qu'on n'ait pas $g\in\underline W$,

[mais j'ignore si $i\in\underline W$ implique $i'\in\underline W$]

\deleted{\textcircled{\unsure{4}}}\inserted{\textcircled{c}} \uline{Application} aux sommes amalgamées dans les $\widehat A$

\unsure{4)}\uline{Thm} Soit
\diagram{\begin{tikzcd}
Y\arrow[r,hook,"i\ \text{\uuline{mono}}"]\arrow[d,"g"']&X\arrow[d,"f"]\\
Y'\arrow[r,hook,"i'"']&X'\simeq X\amalg_Y Y'
\end{tikzcd}}

(donc carré cartésien et cocartésien, car $Y'\longrightarrow X'$ \uuline{mono})

\margin{(\unsure{de la somme amalgamée, version} $\widehat A$)}

alors \deleted{si $i\in\underline W$, $i'$}
\[
i\in\underline W_A\Rightarrow i'\in\underline W_A
\]
\[
g\in\underline W_A\Rightarrow f\in\underline W_A
\]

\deleted{\textcircled{\unsure{5}}} \uline{Application :} $(\mathrm{Hot}(\underline W))$ \uline{et} $\mathrm{Hot}_A$

\uline{Thm} Calcul des fractions à gauche dans $\overrightarrow{\mathrm{Cat}},\overrightarrow{\widehat A}$
% archive foliation: 14
'''
e=[('text','top','Après l axiome d asphéricité; Loc 4/1,2,3'),('text','top second block','Loc 1 sous forme faible a,b,c'),('display','top a','iso dans W'),('display','top b','deux parmi g,f,gf'),('display','top c','gf=id et fg in W'),('text','top item0','Axiomes Loc mettons au net'),('text','top item1','Dualité y compris W=W opposite'),('margin note','left sloping','2 Commentaire sur fibrations cofibrations imm. ouvertes fermées Cylindres Cônes'),('text','upper item3','Soit des'),('deletion','upper number','2'),('insertion','upper number','3'),('diagram','upper small span','Y→X0; Y→X1'),('diagram','upper central square','Y X0 X1 Sigma → X0 amalg Y X1'),('deletion','upper diagram labels','beta; q1; q0'),('text','upper right','et passage : la limite'),('deletion','under upper diagram','Si f0 iso, q0 homotopisme'),('text','upper a','Fonctorialité'),('text','upper b','Si f0 iso alors alpha0 homotopisme'),('text','upper c','Si f0 in W alors alpha0 in W'),('text','middle item4','Thm du'),('deletion','middle number','3; a'),('insertion','middle number','4'),('margin note','middle left','de la somme amalgamée (dans (Cat))'),('diagram','middle','Y X0 X1 X; cart'),('text','middle right','avec q0,q1 cofibrations (resp. fibrations); Supposons'),('deletion','middle right','quasi'),('insertion','middle right','W-'),('diagram','middle','span → X'),('text','under middle diagram','cofib (resp. fib) à fibres triviales donc UW'),('margin note','middle left NB','Si on suppose que pour tout a; cocartésien; reste par tt chgt de base'),('deletion','NB several lines','en; X0a ou X1a soit; cat. ponctuelles; l une des; cat.'),('insertion','NB above struck lines','tels que l une des'),('text','middle corollaries','Si f0 in W alors q0 in W; Si f1 in W alors q1 in W'),('diagram','lower case','Y hook X; Y prime dash X prime = pushout'),('text','right of case','i imm. ouverte ou fermée'),('text','lower Question','si f asphérique; mais j ignore si i in W implique i prime in W'),('text','lower c','Application aux sommes amalgamées dans les A hat; Thm Soit'),('deletion','lower c number','4'),('insertion','lower c number','c'),('diagram','bottom square','Y hook X; g f; Y prime hook X prime pushout'),('text','bottom right','donc carré cartésien et cocartésien car Y prime→X prime mono'),('margin note','bottom left','de la somme amalgamée version A hat'),('deletion','bottom below square','si i in W i prime'),('display','bottom first implication','i in W_A implies i prime in W_A'),('display','bottom second implication','g in W_A implies f in W_A'),('text','bottom applications','Hot(W) et Hot_A; calcul des fractions à gauche'),('deletion','bottom item number','5')]
save(15,text,'text',e,'Dense planning sheet with revised item numbers and several overdrawn diagram labels. Upper span-to-Sigma labels and the left NB cancellations are the least certain. All surviving words attempted; no completion of the unfinished b) parenthesis. Explicit research lead: “j ignore si i in W implique i prime in W” after the open/closed immersion pushout; later presheaf version states both pushout implications. Item “Thm” is a planned theorem, not evidence of a proof. Heading “corps de” and initial Loc numeral doubtful. Bottom calculation of fractions has arrows over Cat and A hat, retained.')
