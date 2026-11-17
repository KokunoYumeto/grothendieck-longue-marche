from record_page import record
record(19,r'''\scanpage{19}
\textcircled{1}\quad $|f,g|$

\deleted{\unsure{Soit}} $G$ un ensemble, $C(G)=\mathbb R[G]=\mathbb R^{(G)}$, (fonctions réelles à support fini), $\mathbb R[G]^+=\{f\in\mathbb R[G]\mid f\geq0\}$

\deleted{$\unsure{f,g\in}$} Eparpillement $f'$ de $f$ (ou $f,f'$ équivalentes, on écrit $f'\sim f$) sss $\exists\sigma\in\unsure{\mathfrak S_G},\ f'=f\circ\sigma$ $\Longleftrightarrow$ la suite des valeurs $\ne0$ de $f$, \deleted{\unsure{comptées}} rangées en décroissant et avec multiplicités, sont les \deleted{\unsure{mêmes}} $\Longleftrightarrow f(\mu)=f'(\mu)$ (image directe de la mesure canonique).
\margin{Notation $A(f)$, condition $A(f')=A(f)$}

Si $f,g\in\mathbb R[G]^+$, on pose
\[
|f,g|=\operatorname{Sup}_{f'\sim f}\langle f',g\rangle
=\operatorname{Sup}_{g'\sim g}\langle f,g'\rangle
=\operatorname{Sup}_{\substack{f'\sim f\\g'\sim g}}\langle f',g'\rangle
\]
\margin{\uline{NB} $|f,g|=|f',g'|$ si $f'\sim f$, $g'\sim g$}

\deleted{\uline{Proposi}} Pour que $\langle f',g'\rangle$ réalise le Sup, il f. et s. que pour $\forall\alpha,\beta\in\mathbb R^{+\ast}$, $E_\alpha(f')$ et $E_\beta(g')$ soient en relation d'inclusion (i.e. $\subset$ ou $\supset$), i.e. il f. et s. que $E_\ast(f')\cup E_\ast(g')$ soit \unsure{tot} ordonné $\Longleftrightarrow\exists$ un ordre total sur $G$ [si $G$ est fini ou dénombrable] $\sim[0,n]$ ou $\mathbb N$, tel que $f$ et $g$ soient \unsure{décroissantes}.

\uline{NB} On pose $E_\alpha(f)=\{s\in G\mid f(s)\geq\alpha\}$ (donc $\alpha\leq\beta\Rightarrow E_\alpha(f)\supset E_\beta(f)$) et $E_\ast(f)=\{E_\alpha(f)$

\margin{\uline{NB} Si $f\sim g$ alors le Sup est réalisé ssi $f'=g'$ et
$|f,g|=|f,f|=|g,g|=\|f\|_2^2=\displaystyle\int_G f^2$}

\uline{Propositi} $f'\sim f\Longleftrightarrow\forall g\in C(G)^+,\ |f',g|=|f,g|\Longleftrightarrow\forall A\in\mathcal P_f(G),\ |f',A|=|f,A|$

\textcircled{2}\quad \uline{$f'\prec f$}

\uline{Prop.} Conditions équivalentes sur $f',f\in\mathbb R[G]^+$

a) $\forall g\in\unsure{\mathbb R(G)^+|\mathbb R[G]^+}$, on a
\[
|f',g|\leq|f,g|
\]
b) $\forall A\in\mathcal P_f(G)$, \unsure{$\ldots$}
\[
|f',A|\leq|f,A|
\]
c) \deleted{\unsure{$\forall$}} $\unsure{n|p}\in\mathbb N^{\unsure{\ast|0}}$, on a
\[
\sum_0^{\unsure{n|m}}A(f')_i\leq\sum_0^{\unsure{n|m}}A(f)_i.
\]
\margin{On écrit alors $f'\prec f$}
% archive foliation: 18
''',[
('text','top','circled 1 |f,g|'),
('deletion','top paragraph beginning','Soit'),
('text','upper','G un ensemble, C(G)=R[G]=R^(G), fonctions réelles à support fini'),
('deletion','before Eparpillement','f,g∈'),
('text','upper','Eparpillement f′ de f ... sss ...'),
('deletion','upper paragraph','comptées; mêmes'),
('margin note','left upper','Notation A(f), condition A(f′)=A(f)'),
('text','upper middle','Si f,g∈R[G]^+, on pose'),
('display','upper middle','|f,g|=Sup ...'),
('margin note','left middle','NB |f,g|=|f′,g′| si ...'),
('deletion','middle paragraph heading','Proposi'),
('text','middle','Pour que <f′,g′> réalise le Sup ...'),
('text','middle lower','NB On pose E_α(f)=... et E_*(f)=...'),
('margin note','left lower','NB Si f∼g alors le Sup est réalisé ssi f′=g′ ...'),
('text','lower middle','Propositi f′∼f iff all test pairings equal'),
('text','lower','circled 2 f′≺f; Prop. Conditions équivalentes'),
('text','lower','a) ∀g ... on a'),
('display','lower','|f′,g|≤|f,g|'),
('text','lower','b) ∀A∈P_f(G), ...'),
('display','lower','|f′,A|≤|f,A|'),
('text','bottom','c) n∈N^*, on a'),
('deletion','bottom before n','∀'),
('display','bottom','Σ_0^n A(f′)_i≤Σ_0^n A(f)_i'),
('margin note','bottom right','On écrit alors f′≺f')
],'''New numbered discussion of rearrangements (the written word is Eparpillement), maximal pairing |f,g|, nested positive level sets as the equality condition, and majorization tested either by arbitrary nonnegative functions, indicator functions, or initial partial sums of the ordered values A(f). Several propositions are stated without proof here. The countability bracket is explicit in the common-order formulation, whereas G begins as an arbitrary set. The strict-positive exponent is + followed by star. The definition of E_*(f) is visibly unfinished (no closing brace), and n/p in the final quantifier is not silently reconciled. The marginal equality claim for equimeasurable functions is a separate assertion worth checking against later pages.''')
