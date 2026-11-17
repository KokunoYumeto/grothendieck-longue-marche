from workflow import save_page
save_page(264,r'''
\scanpage{264}
§ 2 Application à la géométrie algébrique sur une algèbre analytique.

\uline{Th}. 2.1. Soient $A$ une algèbre analytique sur $\mathbb C$, \inserted{$Y=\operatorname{Spec}A$,} $X$ un schéma propre sur $A$, \deleted{Alors} $\widehat Y=\operatorname{Specf}\widehat A$, $\widehat X=X\times_Y\widehat Y$, \deleted{Alors} de sorte que [cf] \deleted{$\unsure{\varphi}$} $\operatorname{Pic}(\widehat X)\simeq\varprojlim\operatorname{Pic}(X_n)$.

Alors

a) $(\operatorname{Pic}(X_n))_n$ satisfait ML

\margin{se généralise aux \uline{\unsure{schémas}} formels en \uuline{car. 0}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]\draw[<->] (0,0)--(2.7,.7);\end{tikzpicture}}}

(ii) $\operatorname{Pic}(X)$ et $\operatorname{Pic}(\widehat X)$ ont $=$ image dans $\operatorname{Pic}(X_{\unsure{0|n}})$.
[\unsure{donc les comp. universelles|donne les comp. universelles}]

(iii) Pour q
\[
\varphi:\operatorname{Pic}(X)\unsure{-|\to}\operatorname{Pic}(\widehat X)
\]
soit un isom il faut s. que $H^1(X,\mathcal O_X)$ soit de longueur finie sur $A$, i.e. $\operatorname{supp}R^1f_*(\mathcal O_X)\subset\{y\}$ ($y$ le pt fermé de $Y$), \deleted{\unsure{ce qui équivaut|ce qui implique} \inserted{\unsure{le groupe}} \unsure{de} \unsure{isomorphisme} \unsure{que le syst.} projectif $(\operatorname{Pic}(X_n))$ soit ess\textsuperscript{t}. constant}
\figure{\begin{tikzpicture}[x=1cm,y=1cm]
\draw (0,0)--(2.5,.8)--(5.2,1.3)..controls(6,1.4)and(6.6,1.3)..(7,1.3)..controls(7.3,1.2)and(7.2,.8)..(7.8,.65)--(10,.7)--(10.5,.5)--(10.4,-.1)--(0,-.2)--(0,0);
\draw (0,.1)--(9.5,1.1);\draw (0,-.1)--(10.5,.5);
\draw (0,0)..controls(.8,-.4)and(1.1,.9)..(1.2,.2)..controls(1.5,-.2)and(1.8,.4)..(2,.9)..controls(2.2,-.4)and(2.5,-.1)..(2.7,.1)--(3.2,1)..controls(3.4,-.3)and(3.8,.1)..(4.1,.7)..controls(4.3,-.3)and(4.7,-.2)..(5,.3)--(5.2,1.2)..controls(5.3,-.2)and(5.8,.5)..(6,1.1)..controls(6.3,.3)and(6,.0)..(6.8,.1)--(7.5,.9)..controls(7.6,-.1)and(8.2,-.1)..(8.6,.0)--(8.5,.8)--(9.1,.2)--(9.8,-.1)--(10.2,.5);
\draw (5.3,1.2) ellipse (.9,.25);
\end{tikzpicture}}

Notons de suite le corollaire suivant de \deleted{l'injectivité de} a) et ii)

\uline{Corollaire} 2.2. Conditions équivalentes

\mspage{263}
''',[
('text','top','§ 2 Application à la géométrie algébrique'),('text','upper','Th. 2.1'),('insertion','above X','Y = Spec A'),('deletion','end of line after A','Alors'),('display','upper middle','hat Y = Specf hat A, hat X = X ×_Y hat Y'),('deletion','before de sorte','Alors'),('text','middle','de sorte que [cf]'),('deletion','before Pic','varphi'),('display','middle','Pic(hat X) ≃ lim Pic(X_n)'),('text','middle','Alors'),('text','middle','a) (Pic(X_n))_n satisfait ML'),('margin note','left of a), tilted','se généralise aux schémas formels en car.0'),('drawing','between a) and marginal note','two-headed oblique connecting arrow'),('text','middle','(ii) Pic(X) et Pic(hat X)'),('text','below (ii)','[donc les comp. universelles]'),('text','lower middle','(iii) Pour q'),('display','lower middle','varphi: Pic(X) - Pic(hat X)'),('text','lower','soit un isom'),('display','within lower paragraph','H^1(X,O_X), supp R^1f_*O_X ⊂ {y}'),('deletion','lower canceled two lines','ce qui équivaut ... syst. projectif'),('insertion','within canceled band','le groupe'),('drawing','around lower cancellation','long outline, oval and crossing strokes'),('text','lower','Notons de suite le corollaire suivant'),('deletion','before a) et ii)','l’injectivité de'),('text','bottom','Corollaire 2.2. Conditions équivalentes'),('text','bottom left','263')
],doubts=[('Th. 2.1 before Pic','canceled varphi','q-like overwritten sign','low'),('left margin','schémas','underlined word compressed','medium'),('(ii) subscript','0','n','medium'),('(ii) bracket','donc les comp. universelles','donne les comp. universelles; last word uncertain','low'),('(iii) map','plain dash','arrowhead not distinct','medium'),('(iii) modal phrase','il faut s. que','il faut s. may be abbreviated faut et suffit','medium'),('canceled lower band','ce qui équivaut / le groupe / de / isomorphisme / que le syst. projectif ... ess.t constant','cancellation crosses the words; ce qui implique alternative','low')],observations='Section2 applies to algebraic geometry over analytic algebra. Th2.1 includes ML, same image in Pic special fibre, criterion for completion map isomorphism using H1 finite length. (ii) bracket after same image is a difficult reading, not normalized to a mathematical expectation. Large canceled reformulation at bottom has uncertain connective and insertion. Cor2.2 starts at foot.')
