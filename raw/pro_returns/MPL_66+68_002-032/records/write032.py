from record_page import record
record(32,r'''\scanpage{32}
On dit alors que le jeu \unsure{de|est} position à deux joueurs est un jeu \uline{alterné} (les deux joueurs jouent alternativement). Pour qu'une application $\hat\alpha$ existe prolongeant $\alpha$ et ayant les propriétés précédentes, il f. et s. que les \unsure{deux} conditions suivantes soient satisfaites

1) $\forall x,y\in C$, tels que $y\in R(x)$, $y\notin\deleted{\unsure{G_0|C_0}} C_0$, on a $\alpha(y)\ne\alpha(x)$

2) $\forall y\in C_0$, soit $T(y)\unsure{=}\{x\in C\mid y\in R(x)\}\subset C\setminus C_0$, alors $\alpha\mid T(y)$ est constante.

Sous les conditions de 2), on aura alors nécessairement, si $T(y)\ne\varnothing$ et $\alpha(T(y))=\{j\}$, $\hat\alpha(y)=j'\deleted{\unsure{\ne j}}$, où $j'$ est l'élément de $J$ qui est $\ne j$.

Cela montre que $\hat\alpha$ est bien déterminé sur l'ens \deleted{\unsure{de}} des $y\in C_0$ tels que $T(y)\ne\varnothing$, donc aussi sur l'ens des positions \uline{non isolées} (une position \inserted{$y$} est dite \uline{isolée} si elle n'a pas de position antécédente ni suivante, i.e. s'il n'existe pas de $x\in C$ tel qu'on ait $y\in R(x)$ ou $x\in R(y)$). On peut attribuer à $\unsure{\alpha|\hat\alpha}$ des valeurs arbitraires sur les positions isolées.

Quand on a défini \inserted{un} $\hat\alpha$, on peut définir
\[
\begin{aligned}
G&=\{x\in C\mid x\in G(\alpha(x))\}\\
P&=\{x\in C\mid x\in G(\overline{\hat\alpha}(x))\}
\end{aligned}
\]
et on \deleted{$\unsure{N=C\setminus(G\cup P)}$ \unsure{aura encore}} aura
% archive foliation: 31
''',[
('text','top','On dit alors que le jeu de position ... alterné ...'),
('text','upper middle','Pour qu’une application hat α existe ... il f. et s. ...'),
('text','middle','1) ∀x,y∈C ... α(y)≠α(x)'),
('deletion','middle','G_0 / C_0'),
('text','middle','2) ∀y∈C_0, soit T(y) ... α|T(y) est constante'),
('text','middle lower','Sous les conditions de 2) ... hat α(y)=j′ ...'),
('deletion','middle lower','≠j'),
('text','lower','Cela montre que hat α est bien déterminé ...'),
('deletion','lower','de'),
('insertion','lower','y'),
('text','lower','On peut attribuer à α des valeurs arbitraires ...'),
('text','bottom','Quand on a défini un hat α ...'),
('insertion','bottom','un'),
('display','bottom','G={x∈C|x∈G(α(x))}; P={x∈C|x∈G(bar hat α(x))}'),
('text','bottom edge','et on ... aura'),
('deletion','bottom edge','N=C minus (G union P); aura encore')
],'''The alternating-game extension criterion has two conditions: already-alternating nonterminal edges, and constant initiative on all predecessors of each terminal. The extension is forced at every nonisolated terminal and arbitrary on isolated vertices. This may connect a two-colorability question to local terminal compatibility, but the manuscript fixes α on all nonterminals in advance. The final total G definition writes α(x) without a hat, whereas P uses barred hat α; retained as written. The package ends mid-sentence after a cancelled neutral-set formula, so no continuation may be invented.''')
