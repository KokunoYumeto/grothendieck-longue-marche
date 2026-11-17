from workflow import save_page
save_page(61,r'''
\scanpage{61}
% archive foliation: 60
\uline{Corollaire} Pour que $f$ soit un iso, il f. et s. que

a) $f$ induit
\[
\pi_0(f):\pi_0(C)\xrightarrow{\sim}\pi_0(C')
\]
b) $f$ induise
\[
\operatorname{Ob}f=f_0:\operatorname{Ob}(C)\simeq\operatorname{Ob}(C')
\]
c) $\forall i\in I$, $f_{a_i,a_i}:\operatorname{Aut}(a_i)\simeq\operatorname{Aut}(f(a_i))$

\margin{\uline{NB} $f$ équivalence $\Longleftrightarrow$ a) et c) sont vrais}

\uline{Corollaire} Pour qu'une application $f_0:C_0\longrightarrow C'_0$ provienne d'un iso $f:C\simeq C'$, il f. et s. que

a) $f_0$ \deleted{soit} bijection

b) $f_0$ transforme la relation d'équivalence de $C_0$ (par comp. connexes) en celle de $C'_0$ (condition vide si $C,C'$ connexes).

c) $\forall i\in I$, $\operatorname{Aut}(f_0(a_i))$ est isom. à $\operatorname{Aut}(a_i)$.

\medskip\hrulefill\medskip
\deleted{\unsure{On}} Supposons $C=C'$. Alors on trouve
\[
\operatorname{Aut}(C)\longrightarrow\unsure{\mathfrak S|\mathcal S}_{C_0}\qquad\uline{\text{surjection}}
\]
si $\operatorname{Aut}^0(C)$ est le noyau, on trouve donc
''',[
('text','top','Corollaire Pour que f soit un iso'),
('text','upper third','a) f induit; b) f induise; c) pour tout i'),
('display','upper third','pi_0(f): pi_0(C) isom pi_0(C prime)'),
('display','upper middle','Ob f = f_0 : Ob(C) isom Ob(C prime)'),
('display','middle','f_ai,ai : Aut(ai) isom Aut(f(ai))'),
('margin note','left and line below first corollary','NB f équivalence iff a) et c) sont vrais'),
('text','middle to lower third','Corollaire Pour qu’une application f_0 provienne d’un iso'),
('text','lower middle','a) f_0 bijection; b) transforme; c) Aut(f_0(ai)) est isom'),
('deletion','second corollary a)','soit'),
('text','bottom','Supposons C=C prime. Alors on trouve'),
('deletion','before Supposons','On'),
('display','bottom','Aut(C) to permutation group, surjection'),
('text','last line','si Aut^0(C) est le noyau, on trouve donc')])
