from record_page import record
record(5,r'''
\scanpage{5}
% archive foliation: 4
Il n'y a de pb. que si \deleted{\unsure{\exists i}}\inserted{l'un des} $x_i$ \unsure{$\in$}\inserted{est égal à} $x$. Car si $x_i\ne x$, $\Sigma(x_i)=\Sigma'(x_i)$, \deleted{\unsure{or}} $x_{i+1}\in\Sigma'(x_i)$ par hyp. de compatibilité \uline{avec $\Sigma'$}.

\deleted{Mais si au contraire $x_i=x$, \unsure{alors} $\underset{=y}{x_1},x_2,\ldots,\underset{=x}{x_i}$, on aurait partie circulaire\ldots}
\margin{\unsure{Supposons} \inserted{donc d'abord} \deleted{\unsure{dans}} qu'il n'y a pas de partie comp. avec \deleted{\unsure{circulaire}} \deleted{\unsure{finie donc ?}} $\Sigma$ commençant en $y$ et terminant en $x$.}

Donc par hyp. sur $\Sigma$, la partie $(x_1,\ldots,x_n\ldots)$ est finie, \deleted{donc} et son \deleted{\inserted{dernier} point}\inserted{aboutissement} $x_{\unsure{N|n}}$ \inserted{qui} est aussi aboutissement de la partie $(x_0,x_1,\ldots)$, est $\in G_0(j)$, \deleted{cqfd} OK dans le cas envisagé.

Mais si $\exists$ partie comp. avec $\Sigma$ commençant en $y$ et terminant en $x$, alors par le lemme on a \inserted{aussi} $x\in G(j)$ cqfd.

$2^\circ)$ Soit $x\in\overline C(j)$; prouvons que
\[
x\in G(j)\Longleftrightarrow\forall y\in R(x),\ \text{on a }y\in G(j)
\]
\deleted{$\unsure{\text{et}}\ (R(x)=\varnothing\ \unsure{\Longrightarrow}\ x\in G_0(j))$}

\deleted{Si $x\in C_0$ i.e. $R(x)=\varnothing$, c'est clair.}
\deleted{Si $x\notin C_0$ i.e. $R(x)\ne\varnothing$, il faut prouver
\[
x\in G(j)\Longleftrightarrow\forall y\in R(x),\ y\in G(j)
\]}

Prouvons $\Longrightarrow$, Soit $x\in G(j)$, $y\in R(x)$, prouvons $y\in G(j)$. Soit $\Sigma$ $j$-stratégie \deleted{\unsure{ga}} $x$-gagnante, je dis qu'elle est $y$-gagnante. En effet considérons \deleted{\unsure{la}} partie $(\deleted{\unsure{x_0=x_1}}x_1=y,x_2,\ldots,x_n,\ldots)$ \inserted{\uline{maximale}}, compatible \deleted{avec $\Sigma$. \unsure{En effet NB Comme}}\inserted{avec $\Sigma$, alors $(x_0=x,x_1=y,x_2,\ldots,x_n,\ldots)$ est aussi comp. avec $\Sigma$} (NB comme $x\in\overline C(j)$, on a $(x,y)$ compatible avec $\Sigma$).

Alors par hyp. sur $\Sigma$, cette partie est finie, (soit $x_{\unsure{N|n}}$ sa pos. d'aboutissement) et $x_{\unsure{N|n}}\in G_0(j)$. \deleted{\unsure{Prouvons}}

\deleted{\unsure{prouvons que} $x_1=y\in G_0(j)$, on fera une \unsure{réc.} \unsure{(la partie est terminée).}}
\deleted{\uline{\unsure{Lemme}} Si $\unsure{z\in\Sigma(z)}$}
''',[
('text','top','Il n’y a de pb. que si ...'),('deletion','top','exists i; or'),('insertion','top','l’un des; est égal à'),('deletion','upper','Mais si au contraire ... partie circulaire'),('margin note','upper-left diagonal','Supposons donc d’abord ...'),('insertion','margin','donc d’abord'),('deletion','margin','dans; circulaire; finie donc ?'),('text','upper-middle','Donc par hyp. sur Sigma ... est finie'),('deletion','upper-middle','donc; dernier point; cqfd'),('insertion','upper-middle','dernier; aboutissement; qui'),('text','middle','Mais si exists partie comp. avec Sigma ... cqfd'),('insertion','middle','aussi'),('text','middle','2 degrees Soit x in Cbar(j)'),('display','middle','x in G(j) iff forall y in R(x) ...'),('deletion','below display','et (R(x)=empty implies x in G_0(j))'),('deletion','lower-middle','Si x in C_0 ... c’est clair; Si x notin C_0 ... il faut prouver'),('display','deleted lower-middle','x in G(j) iff forall y in R(x), y in G(j)'),('text','lower','Prouvons implication, Soit x in G(j), y in R(x)'),('deletion','lower','ga; la; x_0=x_1; avec Sigma ...'),('insertion','lower','maximale; avec Sigma alors (x_0=x,... ) est aussi comp.'),('text','lower parenthesis','NB comme x in Cbar(j), on a (x,y) compatible'),('text','bottom','Alors par hyp. sur Sigma cette partie est finie'),('deletion','bottom','Prouvons; prouvons que x_1=y in G_0(j) ...'),('deletion','bottom-left','Lemme Si z in Sigma(z)')
],'''The return-to-x issue from scan 004 is explicitly repaired: the margin first excludes a Sigma-compatible path from y back to x, and the next paragraph treats its existence via the lemma (“alors par le lemme on a aussi x∈G(j) cqfd”). This is a same-text proof revision, not evidence of an unresolved gap in that direction. The converse/universal direction begins, with terminal-case passages withdrawn. Bottom deletion and diagonal margin are among the least legible material so far.''')
