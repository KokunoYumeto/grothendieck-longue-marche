import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]))
from record_page import record
record(50,r'''
\scanpage{50}
% archive foliation: 49
\uline{Lemme 1} $P,Q$ ens. de card. $2$, $\varphi:P\longrightarrow Q$ conditions équivalentes.
\inserted{$x\in P$ \deleted{\unsure{notons}} $x'=\underline a_P x$}

\[
\begin{array}{llll}
\text{a) }\varphi\text{ bij}&\text{b) }\varphi\text{ inj}&\text{c) }\varphi\text{ surj}&\text{d) }\varphi\text{ non constante}\\
\text{e) }\varphi\text{ commute à }\mathbf Z_2&&\text{f) }\varphi(x')=\underline a_Q\varphi(x)
\end{array}
\]

\uline{Lemme 2} $P,Q,R$ ens. de card. $\unsure{2}$, $\varphi:P\times Q\longrightarrow R$ appl., $x\in P$, $x'=\underline a x$

Conditions équivalentes

a) $\varphi$ se factorise en iso $P\wedge Q\longrightarrow R$

b) $\varphi_x:y\longmapsto\varphi(x,y):Q\longrightarrow R$ est iso, et $\varphi_{x'}\deleted{\unsure{\underline a_Q\varphi_x}}=\underline a_R\varphi_x$

Théorie orientation \unsure{p. esp.} vectoriels réels de dim finie (cat. $\mathcal V\unsure{\}}$, avec \uline{iso})

a) $\deleted{\unsure{\forall V\in\operatorname{Ob}\mathcal V}}\quad\Omega:\mathcal V\longrightarrow(\mathrm{Ens})$

b) $\Omega(0)\simeq\{\pm1\}$

c) $\forall V\in\operatorname{Ob}\mathcal V$, $W\subset V$ hyperplan, $V'$ demi-espace de $V$ de frontière $W$, on donne application de Stokes
\[
\mathrm{St}_{V'}:\Omega(V)\longrightarrow\Omega(W)\qquad\uline{fonctoriel en }(V,V')
\]

\uline{Axiomes}\quad 1) $\mathrm{St}_{V'}$ bijectif \deleted{(cf lemme 1)}

\margin{\uline{Cor} $\forall V\in\operatorname{Ob}\mathcal V$, $\operatorname{Card}\Omega(V)=2$}

2) Si $V''$ est l'opposé de $V'$, on a $\mathrm{St}_{V''}=\underline a\circ\mathrm{St}_{\unsure{V|V'}}$

\uline{Axiomes équivalents}\quad 1) $\forall V\in\operatorname{Ob}\mathcal V$, $\operatorname{card}\Omega(V)=2$

$\Rightarrow$ $\forall V\in\operatorname{Ob}\mathcal V$, $W\in\operatorname{Hypl}V$, \deleted{\unsure{2)}} l'application
\[
\deleted{\unsure{\{V'\}_{W\subset V}}}\inserted{\unsure{\Omega(W,V)|\Omega(W/V)}}\times\Omega(V)\longrightarrow\Omega(W)
\]
\[
(V',\omega)\longmapsto\mathrm{St}_{V'}(\omega)
\]
se factorise en un \deleted{application} \inserted{iso}
\[
\deleted{\unsure{\Omega_{W,V}}}
\]
\diagram{\begin{tikzcd}[column sep=small]
\Omega(W,V)\wedge\Omega(V)\arrow[r,"\sim"] & \Omega(W)\arrow[dr] & \\
&&\text{fonctoriel en }(V,W)
\end{tikzcd}}

\deleted{\unsure{Défin}} Hom d'une théorie $(\Omega,\mathrm{St})$ dans théorie $(\Omega',\mathrm{St}')$ hom de foncteurs $\varphi:\Omega\longrightarrow\Omega'$ compatible avec b), et c)

\uline{Th}\quad \deleted{\unsure{a)}} a) Tout hom d'une théorie dans une autre est un isom.

b) Pour $2$ théories de l'orientation, $\exists!$ isom de l'une dans l'autre

c) $\exists$ théorie de l'orientation.

\uline{Dém}

a) $\varphi_V:\Omega(W)\simeq\Omega'(W)$ iso, par réc sur dim. utilisant Stokes

De $=$, unicité de $\varphi$ par récurrence sur dim. Existence \unsure{?}

\margin{\unsure{choix?}}

\deleted{\unsure{b)}} \deleted{\unsure{Détermination|Définition} d'une th.} Existence d'une théorie de l'orientation ?

Donner $\Omega\inserted{:\mathcal V\longrightarrow\mathrm{Ens}_2}\Longleftrightarrow$ donner $(\Omega_n)_{n\in\mathbf N}$, $\Omega_n:\mathcal V_n\longrightarrow\mathrm{Ens}_2\unsure{\simeq}\operatorname{Tors}(\mathbf Z_2)$

Donner $\Omega\Longleftrightarrow$ donner $\varepsilon_n:\underset{\substack{\text{''}\\G_n}}{\mathrm{GL}(n,\mathbf R)}\longrightarrow\mathbf Z/2$, \uline{et} $\omega_n:=\Omega(\mathbf R^n)$

Donner $\mathrm{St}\Longleftrightarrow(\mathrm{St}_n)_{n\in\mathbf N^*}$, où $\mathrm{St}_n$ est donnée de Stokes en dim $n$
\[
\Omega(V,W)\wedge\Omega(V)\xrightarrow{\sim}\Omega(W)\quad\text{pour }\dim V=n
\]

donner $\{\mathrm{St}_n\}_{\unsure{n\in\mathbf N}}$ revient à donner
''',[
('text','top','Lemme 1 P,Q ens. de card.2'),
('insertion','top edge','x in P x prime=a_P x'),
('deletion','top insertion','notons'),
('display','upper','a) phi bij to f) phi(x prime)=a_Q phi(x)'),
('text','upper','Lemme 2 P,Q,R'),
('text','upper','Conditions équivalentes'),
('text','upper','a) phi se factorise en iso'),
('text','upper-middle','b) phi_x:y maps to phi(x,y)'),
('deletion','in b equality','a_Q phi_x'),
('text','upper-middle','Théorie orientation p. esp. vectoriels réels'),
('display','middle','a) Omega:V to Ens'),
('deletion','before Omega functor','forall V in Ob V'),
('display','middle','b) Omega(0) isomorphic {+/-1}'),
('text','middle','c) forall V, W hyperplan, V prime demi-espace'),
('display','middle','St_V prime:Omega(V) to Omega(W)'),
('text','middle','Axiomes 1) St_V prime bijectif'),
('deletion','after bijectif','cf lemme 1'),
('margin note','right beside axioms','Cor Card Omega(V)=2'),
('text','middle-lower','2) Si V double prime est lopposé'),
('text','above fold','Axiomes équivalents 1) Card Omega(V)=2'),
('text','at fold','implies forall V, W in Hypl V lapplication'),
('deletion','before lapplication','2)'),
('display','at fold','Omega(W,V) x Omega(V) to Omega(W)'),
('deletion','first domain factor','{V prime}_(W subset V)'),
('insertion','above cancelled domain factor','Omega(W,V)'),
('display','below fold','(V prime,omega) maps to St_V prime(omega)'),
('text','below fold','se factorise en un iso'),
('deletion','after un','application'),
('insertion','above application','iso'),
('deletion','left of tensor formula','Omega_(W,V)'),
('diagram','below fold','Omega(W,V) wedge Omega(V) isomorphism Omega(W); arrow to fonctoriel en (V,W)'),
('deletion','before Hom','Défin'),
('text','lower','Hom dune théorie (Omega,St) dans théorie'),
('text','lower','Th a) Tout hom dune théorie'),
('deletion','before a)','a)'),
('text','lower','b) Pour 2 théories de lorientation'),
('text','lower','c) exists théorie de lorientation'),
('text','lower','Dém a) phi_V iso par réc sur dim'),
('text','lower','De = unicité de phi; Existence?'),
('margin note','right of Existence','choix?'),
('deletion','before crossed heading','b)'),
('deletion','lower cancelled heading','Détermination dune th.'),
('text','lower','Existence dune théorie de lorientation?'),
('text','lower','Donner Omega iff donner (Omega_n)'),
('insertion','above Omega equivalence','V to Ens_2'),
('text','bottom','Donner Omega iff donner epsilon_n:GL(n,R) to Z/2'),
('text','bottom','Donner St iff (St_n) n in N star'),
('display','bottom','Omega(V,W) wedge Omega(V) isomorphism Omega(W)'),
('text','bottom edge','donner {St_n} revient à donner')
],[
('top insertion cancellation','notons','dark overstrike prevents a secure word reading','low'),
('Lemme 2 cardinal','2','narrow final figure resembles 1','medium'),
('Lemme 2 cancelled equality term','a_Q phi_x','order and indices obscured by cancellation','low'),
('orientation heading','p. esp.; calligraphic V followed by brace-like mark','abbreviation p. espaces; mark may be overwritten letter','medium'),
('cancelled opening of a)','forall V in Ob V','all terms heavily struck','low'),
('axiom 2 final subscript','V','V prime; no secure prime visible','medium'),
('equivalent axioms first domain factor','cancelled {V prime}_(W subset V); inserted Omega(W,V)','Omega(W/V); cancelled factor heavily overworked','low'),
('deleted term left of tensor formula','Omega_(W,V)','overwritten formula, indices uncertain','low'),
('before Hom and before theorem a)','Défin; a)','overwritten heading and label','low'),
('right edge beside Existence','choix?','faint overwritten word above heavy question mark','low'),
('cancelled heading','Détermination dune th.','Définition dune th.','low'),
('Omega_n target identification','Ens_2 isomorphic Tors(Z_2)','connecting symbol very heavily reinforced','medium'),
('final line subscript','n in N','only n and membership stroke clearly visible at bottom','low')])
