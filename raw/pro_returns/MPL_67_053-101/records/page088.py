import sys
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/'scripts'))
from record_page import save
tex=r"""
\scanpage{88}
% archive foliation: 90
\[
X(I)/V(I)\simeq X(J)\qquad\text{où }J=J(I)\text{ comme dessus}
\]
Ceci dit soit \deleted{$I\hookrightarrow X$}\inserted{une opération de $V$ sur $X$}
\deleted{on a donc \unsure{de} $X$ une opération $V=V(I)$}\inserted{$V$}$\hookrightarrow G_X$, d'où un $I(V)$ $V$-torseur
des bifaces de $\operatorname{Oc}(V)$, et on a \deleted{$X\simeq$}
\[
X\simeq X(I(V))\qquad\text{iso. canonique},
\]
(et non $X\simeq X(I)$). Mais pour \deleted{un} deux torseurs
$T,T'$ sous un même $V$, on aura
\[
X(T\wedge T')=X(T)\wedge_V T'
\]
\margin{à expliciter}
Soit donc
\[
\begin{gathered}
\uline t=\unsure{\delta|\tau}(I,X)\text{ le }V\text{-torseur tel que}\quad I(V)\simeq I\wedge_V\delta\\
\text{i.e.}\qquad\delta\simeq I(V)\wedge I^{-1}.
\end{gathered}
\]
On aura
\[
\boxed{X=X(I(V))=X(I)\wedge_V\uline t}
\]
\deleted{Donc et l'on} donc
\[
\boxed{X/V\simeq X(I)/V\simeq\unsure{Z|X}(J)}
\]

En résumé :

\uline{Cor à Prop} \deleted{La donnée, d'un \unsure{gr.} $V\simeq D_2$}\inserted{Pour $I\in\operatorname{Ob}\operatorname{Ens}_4$}
donné, d'où $J$ et
$V=V(J)$, la donnée d'un $X$ et d'un plongement
$V\hookrightarrow G_X$ équivaut à la donnée d'un torseur $\uline t$ sous $V$,
via
\diagram{\begin{tikzcd}
\delta \arrow[r,mapsto] & X(I)\wedge_V\deleted{\unsure{\delta}}\uline t
\end{tikzcd}}
On a donc
\[
X/V\simeq\unsure{Z|X}(J)\qquad\text{(iso. canonique)}.
\]

\uline{\unsure{Cor à Cor}}, \inserted{Donc} la donnée de $(X,I\hookrightarrow X)$ équivaut à
celle de a) un pt $\zeta$ de $Z(J)^*$, b) un $V$-torseur $\uline t$,
\deleted{c) un $V$-isom \unsure{un tel} \unsure{point} $X=X(I)\wedge_V\uline t$,}
et
\deleted{$X_\zeta=\text{fibre de}$}
\[
X_\zeta=X(I)_\zeta\wedge\uline t\simeq I\qquad\text{i.e.}\quad\uline t=I\wedge X(I)_\zeta^{-1}.
\]
"""
save(88,tex,[('display','top','X(I)/V(I) isomorphic X(J)'),('text','upper','Ceci dit soit'),('deletion','after soit','I into X'),('insertion','above I into X','une opération de V sur X'),('deletion','upper two lines','on a donc de X une opération V=V(I)'),('insertion','before into G_X','V'),('deletion','after on a','X isomorphic'),('display','upper middle','X isomorphic X(I(V))'),('text','middle','et non X isomorphic X(I)'),('deletion','before deux torseurs','un'),('display','middle','X(T wedge T prime)=X(T) wedge_V T prime'),('margin note','right of identity','à expliciter'),('text','middle lower','Soit donc'),('display','middle lower','t=delta(I,X); I(V) isomorphic I wedge delta'),('text','above first box','On aura'),('display','first box','X=X(I(V))=X(I) wedge t'),('deletion','left of second box','Donc et l’on'),('text','left of second box','donc'),('display','second box','X/V isomorphic X(I)/V isomorphic Z(J)'),('text','lower summary','En résumé Cor à Prop'),('deletion','after Cor à Prop','La donnée d’un gr. V isomorphic D2'),('insertion','above deletion','Pour I in Ob Ens4'),('diagram','lower','delta maps to X(I) wedge_V t'),('deletion','diagram target','delta'),('text','lower','On a donc'),('display','lower','X/V isomorphic Z(J)'),('text','foot corollary','Cor à Cor la donnée de X,I into X'),('insertion','above second corollary','Donc'),('deletion','foot after b','c) un V-isom un tel point X=...'),('deletion','bottom left','X zeta = fibre de'),('display','bottom','X zeta = X(I) zeta wedge t isomorphic I')],doubts=[('torsor symbol','delta','tau; replaced in several places by an underlined t.','medium'),('two quotient formulae','Z(J)','X(J) overwritten with horizontal bars; first line has a clear X(J), left unchanged.','low'),('first corollary deletion','gr.','Short word after d’un obscured.','low'),('second corollary heading','Cor à Cor','Strong retracing of first word.','low'),('bottom cancelled c clause','un tel point','Two words and their placement beneath long strike uncertain.','low')],notations=[('torsor parameter',r'\uline t','Underlined lower-case t, distinct from T,T prime and delta.'),('twisting symbol',r'\delta(I,X)','Alternative tau recorded at definition.'),('quotient curve notation',r'X(J);\ \unsure{Z|X}(J);\ Z(J)','Do not silently change first X to later Z.'),('moduli point',r'\zeta','Zeta with subscript occurrences.')],leads=['Twisting identity X(T wedge T prime)=X(T) wedge_V T prime explicitly marked à expliciter.','Canonical quotient X/V identified independently of the V-torsor twist; first X(J) later overwritten Z(J), a reading issue to keep separate.','Revised corollary encodes four-point configurations by base point zeta in punctured quotient and V-torsor plus an identification of the fibre; inspect redundancy versus categorical equivalence.'])
