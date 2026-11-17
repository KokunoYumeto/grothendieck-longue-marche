from workflow import save_page
save_page(59,r'''
\scanpage{59}
% archive foliation: 58
\[
f\longmapsto\left(
\bigl(\underbrace{\unsure{f_0|f}(u_x)}_{\unsure{\ell_x|e_x}}\bigr)_{x\in C_0},
\bigl(\underbrace{f_{a_i,a_i}:\operatorname{Aut}(a_i)\longrightarrow\operatorname{Aut}(f_0(a_i))}_{\varphi_i}\bigr)
\right).
\]

c) Pour que $f$ soit fidèle, il \unsure{f.|faut} et
suffit que $\forall i\in I$, $\varphi_i$ soit injectif.
Pour que $f$ soit pleinement fidèle,
il \unsure{f.|faut} et suffit que, 1°) pour $i\ne j$,
on ait $\operatorname{Hom}(f_0(a_i),f_0(a_j))=\varnothing$

2°) pour $\unsure{\forall i}\ x,y\in C(i)_0$,
\[
\operatorname{Isom}(f_0(x),f_0(y))\xrightarrow{\sim}\operatorname{Hom}(f_0(x),f_0(y))
\]

3°) $\forall i\in I$, $\varphi_i$ est un iso.

\deleted{d) Si $C$}
Pour que $f$ soit une équivalence,
il f. et s. qu'on ait de plus

4°) Tout $x'\in C'_0$ est isomorphe
à un des $f_0(a_i)$

Pour que $f$ soit un isom.,
il faut et s. qu'on ait 1°, 2°, 3°,
et de plus

4'°) $f_0$ bijective.
''',[
('display','top continuation of previous page','f maps to (f_0(u_x)) and f_ai,ai; underbraces ell_x,phi_i'),
('text','upper c first assertion','c) Pour que f soit fidèle'),
('text','upper c second assertion with condition 1','Pour que f soit pleinement fidèle; 1° i not equal j'),
('text','middle condition 2','2° pour tout i x,y in C(i)_0'),
('display','middle isomorphism','Isom(f_0(x),f_0(y)) -> Hom(f_0(x),f_0(y))'),
('text','middle condition 3','3° pour tout i phi_i est un iso.'),
('deletion','below condition 3','d) Si C'),
('text','lower equivalence paragraph','Pour que f soit une équivalence'),
('text','lower condition 4','4° Tout x prime in C prime_0 est isomorphe'),
('text','lower isomorphism paragraph','Pour que f soit un isom.'),
('text','last line','4 prime° f_0 bijective')])
