from record_page import record
record(20,r'''\scanpage{20}
\uline{NB} C'est une relation \deleted{d'ordre} \inserted{de préordre}. La relation d'équ. associée est $f'\sim f$.
\margin{\uline{NB} Le sup de $\langle f',g\rangle$ pour $f'\prec f$ est atteint \deleted{pour} \inserted{des} $f'\sim f\ldots$}

\deleted{\uline{Cor} $f'\prec f$, $g'\prec g\Longrightarrow|f',g'|\leq|f,g|$}

\uline{Cor} $f'\prec f\Longleftrightarrow\forall g',g\in C(G)^+$, avec $g'\prec g$, on a
\[
|f',g'|\leq|f,g|
\]

\uline{3}\quad\uline{Couples \unsure{privilégiés|priorisés}}

A partir de maintenant, $G$ est un groupe, d'où opération $f\ast g$ sur $\mathbb R[G]^{\unsure{\ast|+}}$, $\mathbb R[G]^+$ est stable.

\margin{\uline{NB} Soient $f,g\in\mathbb R(G)^+$. Considérons les $\|f'\ast g\|_\infty$ ou $(f'\ast g)(0)$ pour $f'\prec f$, alors le Sup est \deleted{\unsure{atteint}\ $\unsure{\|f\ast g\|_\infty}$} \inserted{$=$}, et il est atteint pour $f'\sim f$.}

\uline{Prop} $f,g\in\mathbb R(G)^+$, Conditions équivalentes

a) $f'\prec f$, $g'\prec g$, $\|f'\ast g'\|_\infty\leq\|f\ast g\|_\infty$

b) $\forall f'\prec f$, $g'\prec g$
\[
\underset{\inserted{=\langle f',\check g'\rangle}}{(f'\ast g')(0)}
\leq\operatorname{Sup}_{s\in G}
\underbrace{(f\ast g)(s)}_{\inserted{=\deleted{\unsure{\langle f,\check g\rangle}}\langle f\unsure{\ast|,}\varepsilon_s\check g\rangle}}
\]
a') \deleted{$\unsure{\forall f'\sim f,\ \forall g'\sim g}$} a), b) avec $f'\sim f$, $g'\sim g$

c) $|f,g|=\|f\ast g\|_\infty$

d) $\exists s\in G$ tel que
\diagram{\begin{tikzcd}[row sep=small]
\inserted{E_\ast(g)\cup E_\ast(\check f\ast\varepsilon_s)\ \deleted{\unsure{E_\ast(\check g)}}\ \text{tot. ordonné}}\arrow[d,leftrightarrow]\\
E_\ast(f)\cup E_\ast(\varepsilon_s\check g)\quad\text{tot. ordonné}
\end{tikzcd}}
i.e. $\forall\alpha,\beta\in\mathbb R^{+\ast}$, $E_\alpha(f)$ et $E_\beta(\varepsilon_s\check g)$ en relation d'inclusion

\uline{Def} On dit alors que le \deleted{\unsure{bi}}couple $(f,g)$ est \uline{\unsure{privilégié|priorisé}}
([Il n'est pas clair que la relation soit symétrique --- \deleted{\unsure{elle signifie}\ $\forall s$} mais OK si $G$ commutatif])

\uline{Cor} $f\in\mathbb R[G]^+$, \deleted{\unsure{alors}} $(f,f)$ est \unsure{privilégié|priorisé} (\deleted{\unsure{sss}\ $f\text{ et }f$} \inserted{$\exists s\in G$} tel que $\check f=\varepsilon_s\ast f$ ($\Longleftrightarrow\check f=f\ast\varepsilon_s$)

\margin{\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\node at (0,0) {$E_\ast(\varepsilon_t\ast f)\cup E_\ast(g)\ \text{tot. ord.}$};
\draw (0,0) ellipse (3.2cm and .55cm);
\draw[<->] (1,-.5) -- (.3,-1.3);
\end{tikzpicture}}}
\uline{NB} Si dans la prop. $g$ satisfait la condition précédente, alors la condition de la prop signifie aussi \unsure{eq} $\exists t\in G$ t.q. $E_\ast(f)\cup E_\ast(\varepsilon_t\ast g)$ tot. ordonné
% archive foliation: 19
''',[
('text','top','NB C’est une relation ... La relation d’équ. associée est f′∼f'),
('deletion','top','d’ordre'),
('insertion','above top line','de préordre'),
('margin note','upper right','NB Le sup ... est atteint ... des f′∼f'),
('deletion','upper right note','pour'),
('insertion','upper right note','des'),
('deletion','upper','Cor f′≺f, g′≺g⇒|f′,g′|≤|f,g|'),
('text','upper','Cor f′≺f iff ∀g′,g ...'),
('display','upper','|f′,g′|≤|f,g|'),
('text','heading','3 Couples privilégiés/priorisés'),
('text','upper middle','A partir de maintenant, G est un groupe ...'),
('margin note','left vertical','NB Soient f,g ... Considérons les ...'),
('deletion','within left note','atteint ... norm'),
('insertion','within left note','='),
('text','middle','Prop f,g ... Conditions équivalentes'),
('display','middle','a) f′≺f, g′≺g, norm inequality'),
('display','middle','b) (f′*g′)(0)≤Sup_s(f*g)(s)'),
('insertion','below b expressions','=<f′,check g′>; =<f*ε_s check g>'),
('deletion','below b right','<f,check g>'),
('text','middle lower','a′) ... a),b) avec f′∼f, g′∼g'),
('deletion','middle lower','∀f′∼f, ∀g′∼g'),
('display','middle lower','c) |f,g|=||f*g||∞'),
('text','lower','d) ∃s∈G tel que ... i.e. ...'),
('diagram','lower','E_*(g)∪E_*(check f*ε_s) iff E_*(f)∪E_*(ε_s check g)'),
('insertion','above d','equivalent ordered-level-set condition'),
('deletion','within inserted d condition','E_*(check g)'),
('text','lower','Def On dit alors que le couple ...'),
('deletion','within Def','bi; elle signifie ∀s'),
('text','lower','Il n’est pas clair que la relation soit symétrique ... mais OK si G commutatif'),
('text','bottom','Cor f∈R[G]^+, (f,f) est ...'),
('deletion','within Cor','alors; sss f et f'),
('insertion','above Cor end','∃s∈G'),
('display','bottom','check f=ε_s*f iff check f=f*ε_s'),
('drawing','bottom right','circled E_*(ε_t*f)∪E_*(g) tot. ord.; double arrow'),
('margin note','bottom right','alternative ordered-level-set condition'),
('text','bottom edge','NB Si dans la prop. g satisfait ... ∃t ...')
],'''Self-flagged reservation: “Il n’est pas clair que la relation soit symétrique”, qualified by “mais OK si G commutatif”. The section heading’s adjective is difficult and will require a cross-page ink comparison; it is not silently replaced by a standard technical name. Convolution extremality is characterized by saturation of maximal pairing and nested level sets after reflected translation. The corollary on (f,f) relates this to a translated reflection symmetry; a following NB transfers the condition when g has that symmetry. The top corrects “d’ordre” to “de préordre”, an explicit correction retained in the transcription. Bottom-edge writing is partly crowded/clipped.''')
