from record_page import save
save(18,9,'text',r'''
\uline{Twist de Tate sur structures de Hodge mixtes}

Soit $\mathcal E:(E,E_0,\underset{\text{croiss}}{W_*^{\deleted{\unsure{*}}}},\underset{\text{décr.}}{F^*})$ une structure de Hodge mixte.
On définit une structure de Hodge $\mathcal E(-1)$ \deleted{\unsure{$=\mathcal E(+1)$}}, (twist de Tate (\inserted{\unsure{effectif}})), \deleted{\unsure{p}} avec \unsure{m\textsuperscript{e}|même} $E_0$ \deleted{espace vectoriel sur $Q$}\inserted{module sur $Z$}, de \unsure{m\textsuperscript{e}|même} $E$,
\[
\left\{\begin{aligned}
W_i(\mathcal E(-1))&=W_{i\unsure{-|+}2}(\mathcal E)\\
F^i(\mathcal E(-1))&=F^{i-1}(\mathcal E)
\end{aligned}\right.
\]
\unsure{On trouve bien que}
\[
W_i(\mathcal E(-1)/W_{i-1}(\mathcal E(-1))\simeq[W_i(\mathcal E)/W_{i-1}(\mathcal E)](-1)
\]
(twist de Tate sur structures de Hodge ordinaires).
Bien sûr, on définit pour \unsure{tt} entier $n$ un twist $\mathcal E(n)$,
\[
\left\{\begin{aligned}
W_i(\mathcal E(n))&=W_{i+2n}(\mathcal E)\\
F^i(\mathcal E(n))&=F^{i+n}(\mathcal E)
\end{aligned}\right.
\]

\mspage{8}
''',[
('text','top','Twist de Tate sur structures de Hodge mixtes'),
('text','upper','Soit E:(E,E_0,W_*,F*) une structure de Hodge mixte'),
('display','upper middle','W_i(E(-1)); F^i(E(-1))'),
('text','middle','On trouve bien que'),
('display','middle','W_i(E(-1)/W_{i-1}(E(-1))'),
('text','lower middle','twist de Tate sur structures de Hodge ordinaires; Bien sûr'),
('display','lower','W_i(E(n)); F^i(E(n))')
], 'Whole and both halves inspected; enlarged top and bottom source-pixel crops used. The missing parenthesis and the unchanged i indices in the quotient display are retained; the blotted sign before 2 is uncertain, not repaired from the general n formula.')
