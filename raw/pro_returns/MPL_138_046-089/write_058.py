from workflow import save_page
save_page(58,r'''
\scanpage{58}
% archive foliation: 57
\uline{Automorphismes de groupoïdes.}

1) Soient $C$ \deleted{$\unsure{=(C_0,C_1,C_2)}$} un groupoïde,
$C'$ une catégorie, on s'intéresse
à
\[
\operatorname{Hom}(C,C')=\operatorname{Ob}\,\underline{\operatorname{Hom}}(C,C').
\]
On a
\[
\operatorname{Hom}(C,C')\longrightarrow
\operatorname{Hom}(\underbrace{\operatorname{Ob}C}_{C_0},\underbrace{\operatorname{Ob}C'}_{C'_0})
\]
Soit
\[
f_0:C_0\longrightarrow C'_0
\]
on demande les $f:C\unsure{-|\longrightarrow}C'$ qui
lui donnent naissance. On trouve:

\uline{Proposition} a) Pour qu'il existe un
$f$ au dessus de $f_0$, il f. et il s.
que pour $x,y\in C_0$ \unsure{appartenant} à
la \unsure{$=$|même} comp. connexe de $C$
(i.e. tels que $\operatorname{Hom}_C(x,y)\ne\varnothing$) on ait
$f_0(x)\simeq f_0(y)$.
\deleted{b) \unsure{Supposons} cette condition \unsure{satisfaite}.}
b) Pour $\forall$ composante
connexe $C(i)$ de $C$, soit $a_i\in C(i)_0$,
et pour $\forall$ $x\in C(i)_0$, soit
$u_x:a_i\xrightarrow{\sim}x$. Alors
\[
\begin{aligned}
\operatorname{Hom}_{f_0}(C,C')\xrightarrow{\sim}
&\prod_{\unsure{x\in C_0\setminus\{a_i\}}}
\operatorname{Isom}\bigl(f_0(a_{i(x)}),f_0(x)\bigr)\\
&\times\prod_{\unsure{i}}\operatorname{Hom}\bigl(\operatorname{Aut}(a_i),\unsure{\operatorname{Aut}(f_0(a_i))}\bigr)
\end{aligned}
\]
''',[
('text','top underlined heading','Automorphismes de groupoïdes.'),
('text','upper introduction','1) Soient C un groupoïde, C prime une catégorie'),
('deletion','after first C','=(C_0,C_1,C_2)'),
('display','first formula','Hom(C,C prime)=Ob Hom underlined(C,C prime)'),
('text','before second formula','On a'),
('display','second formula','Hom(C,C prime) -> Hom(Ob C,Ob C prime); underbraces C_0,C prime_0'),
('text','before third formula','Soit'),
('display','third formula','f_0:C_0 -> C prime_0'),
('text','middle paragraph','on demande les f qui lui donnent naissance'),
('text','lower proposition a','Proposition a) Pour qu il existe un f'),
('deletion','after f_0(x) isomorphic f_0(y)','b) Supposons cette condition satisfaite'),
('text','lower proposition b','b) Pour toute composante connexe C(i)'),
('display','bottom product bijection','Hom_f0(C,C prime) -> product Isom times product Hom of Aut groups')])
