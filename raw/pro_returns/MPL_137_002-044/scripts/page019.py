from record_page import record
tex=r'''\scanpage{19}
% archive foliation: 18
dans la suite des $\operatorname{div}n_{i\alpha}$ est $\beta_{i\ell}$,
et $\Phi(i,\ell)_*$ est le \deleted{complexe}
\inserted{module $\frac12$ simplicial} associé
à
\diagram{\begin{tikzcd}
-0\arrow[r]&\overset{\text{deg $i$}}k\arrow[r,"n"]&
\overset{\text{deg $i-1$}}k\arrow[r]&0-
\end{tikzcd}}
où $\operatorname{div}(n)=\ell$. On a donc
une extension
\diagram{\begin{tikzcd}
0\arrow[r]&\Lambda^{i-1}\Psi\arrow[r]&\Phi(i,n)\arrow[r]&\Lambda^i\Psi\arrow[r]&0
\end{tikzcd}}
où l'hom. assoc. à cette extension
\diagram{\begin{tikzcd}k\arrow[r]&k\end{tikzcd}}
(cf \unsure{\ldots}) est $n\operatorname{id}$, où $\operatorname{div}(n)=\ell$;
donc
\[
\deleted{\unsure{\beta}}\pi_j(\Phi(i,n))=
\left\{\begin{array}{ll}0&\text{si }j\neq i-1\\
k/\operatorname{div}n&\text{si }j=i-1.
\end{array}\right.
\]

\uline{Remarque} 1) La fonction de Hilbert de $\Phi(i,n)$
est donc la même que celle de $\Lambda^i\Phi_\bullet$,
savoir $\binom{n+1}{i}$. Donc si $L_\bullet$ est
donné par le produit de la prop on a
\[
\operatorname{rg}L_n=\sum_{i\leq n+1}(\mu_i+\beta_i)\binom{n+1}{i}
+\sum_{0\leq j\leq n}\nu_j\binom{n}{\unsure{i|j}}.
\]
Donc si $L_\bullet$ est \inserted{$\partial$-parfait, il est}
connu à isom. (non unique)
près quand on connaît a) $\unsure{\operatorname{rg}\pi_i(L_\bullet)=\nu_i}$
et le nombre $\beta_{i+1}$ de ses diviseurs de
torsion, pour tt $i\geq0$, et b) la fonction
$f_{L_\bullet}(n)$ pour $n$ grand (qui donne
\deleted{\unsure{alors}} \inserted{pour $n$ grand} le polynôme
$\sum_{i\geq1}(\mu_i+\beta_i)\binom{n+1}{i}
+\sum_{j\geq0}\nu_j\binom{n}{\unsure{i|j}}$)
'''
record(19,tex,[('text','top continuation','dans la suite des div n_iα est β_iℓ'),('text','top definition','Φ(i,ℓ) est le ... associé'),('deletion','top after le','complexe'),('insertion','above complexe','module ½ simplicial'),('diagram','upper chain','−0→k—n→k→0−; degrés i,i−1'),('text','below chain','où div(n)=ℓ; On a donc une extension'),('diagram','extension','0→Λ^(i−1)Ψ→Φ(i,n)→Λ^iΨ→0'),('text','connecting homomorphism lead','où l’hom. assoc. à cette extension'),('diagram','middle','k→k'),('text','middle explanation','cf …; n id; div(n)=ℓ'),('deletion','before π_j','β'),('display','middle homotopy cases','π_j(Φ(i,n))=0 or k/div n'),('text','Remarque 1','fonction de Hilbert de Φ(i,n)'),('text','rank lead','Donc si L est donné par le produit'),('display','rank formula','rg L_n=Σ(μ_i+β_i)binomial+Σν_j binomial'),('text','lower classification statement','Donc si L est ... connu à isom'),('insertion','above classification','∂-parfait, il est'),('text','lower invariants','a) rgπ_i; β_i+1 diviseurs de torsion; b) f_L(n)'),('deletion','last lines','alors'),('insertion','last lines','pour n grand'),('display','bottom inline polynomial','Σ(μ_i+β_i) binomial+Σν_j binomial')],doubts=[('first diagram endpoint strokes','−0 and 0−','short dashes drawn beyond endpoint zeroes','high'),('cf parenthesis','ellipsis','faint cross-reference seems unfilled','medium'),('homotopy quotient','k/div n','n/ℓ notation alternates visibly; not corrected','medium'),('Hilbert function wording','même; produit de la prop','faint staff obscures words','medium'),('second summand lower binomial index','i / j','ink looks i, though summation index is j','low'),('classification a)','rgπ_i(L)=ν_i','rightmost text close to page edge; exact invariant uncertain','low'),('final polynomial subscript','i / j','same lower-index ambiguity as preceding formula','low')],notation=[('divisor of a scalar',r'$\operatorname{div}(n)$','scan 19; explicit switch between ℓ and representative n retained'),('Hilbert function',r'$f_{L_\bullet}(n)$','scan 19')])
