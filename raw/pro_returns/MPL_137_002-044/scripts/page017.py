from record_page import record
tex=r'''\scanpage{17}
% archive foliation: 16
ces conditions, les entiers $\mu_i$ $(i\geq1)$,
$\nu_j$ $(j\geq0)$, $\beta_{i\ell}$ $(i\geq1,\ell\in\unsure{\mathfrak P})$
sont uniquement
déterminés par les conditions suivantes

a) Pour \inserted{tout} $i\geq1$, les $\beta_{i\ell}$ \inserted{$\neq0$}
sont les \inserted{multiplicités des} diviseurs
élémentaires de \deleted{\unsure{$H_i$}}
$\pi_{i-1}(L_\bullet)$ $(=H_{i-1}(L^!_\bullet))$

b) \deleted{\unsure{$k$}} $\nu_i=\operatorname{rg}\pi_i(L_\bullet)$
$(=\operatorname{rg}H_i(L^!_\bullet))$

c) On a \deleted{rang} $\mu_i=\operatorname{rg}B_{i-1}(L^!_\bullet)$
\deleted{\unsure{$\beta_{i-1}$}} $-\beta_i$
\[
(\text{où }\beta_i=\sum_\ell\beta_{i,\ell})
\]

d) On a de plus
\[
\left\{\begin{aligned}
\operatorname{rg}Z_i\deleted{\unsure{\partial}}(L^!_\bullet)
 &=\mu_{i+1}\deleted{\unsure{+\mu_i}}+\beta_{i+1}+\nu_i\\
\operatorname{rg}L^!_i
 &=\mu_{i+1}+\deleted{\unsure{\mu_i+}}\beta_{i+1}+\beta_i+\nu_i
\end{aligned}\right.
\]
Enfin $L_\bullet$ est (str.) $\partial$-parfait ssi le nb de
facteurs non nuls qui interviennent est fini.

\uline{Dém} \deleted{\unsure{En fait}} \inserted{Par} la théorie de Dold-Puppe,
on réduit tout à une question de
complexes de chaînes. Comme
tt sous-module d'un $k$-module
projectif de t.f. sur $k$ est itou, on
conclut que tout tel complexe,
s'il est \deleted{\unsure{str. ps. coh.}} \inserted{str.} à comp. proj. de t.f.,
s'écrit comme un produit de
complexes (définis à isom \deleted{unique}
\deleted{\unsure{unique}} près, \deleted{\unsure{par le choix de}}
\inserted{--- mais l'isom}
\inserted{$\prod_i\simeq L^!_\bullet$ n'est pas unique}) de la forme
\diagram{\begin{tikzcd}[column sep=large]
K_i:\quad -0\arrow[r] &
P_i\arrow[r,hook]\arrow[d,equal] &
Q_i\arrow[r]\arrow[d,equal] &0-\\
& B_{i-1}\arrow[r,hook] & Z_{i-1} &
\end{tikzcd}}
\inserted{$P_i$: degré $i$\qquad $Q_i$: degré $i-1$}
'''
record(17,tex,[('text','top continuation','ces conditions, les entiers μ_i,ν_j,β_iℓ'),('text','condition a','Pour i≥1 les β_iℓ sont les diviseurs élémentaires'),('insertion','a above Pour','tout'),('insertion','a above β_iℓ','≠0'),('insertion','a above diviseurs','multiplicités des'),('deletion','a before π','H_i'),('text','condition b','ν_i=rgπ_i(L)=rg H_i(L!)'),('deletion','b before ν','k'),('text','condition c','μ_i=rg B_i−1(L!)−β_i'),('deletion','c before μ','rang'),('deletion','c after associated complex','β_i−1'),('display','c lower right','β_i=Σℓ β_iℓ'),('text','d lead','On a de plus'),('display','d brace','rg Z_i(L!) and rg L!_i'),('deletion','d formula overwrites','∂; +μ_i; μ_i+'),('text','after formulas','Enfin L est (str.) ∂-parfait ssi'),('text','proof heading','Dém; théorie de Dold–Puppe'),('deletion','proof opening','En fait'),('insertion','proof opening','Par'),('text','proof','on réduit tout; complexes de chaînes'),('deletion','proof after s’il est','str. ps. coh.'),('insertion','proof after s’il est','str.'),('text','lower proof','produit de complexes définis à isom près'),('deletion','lower proof','unique twice; par le choix de'),('insertion','lower proof','mais l’isom; Π_i≃L! n’est pas unique'),('diagram','bottom','K_i: −0→P_i↪Q_i→0−; B_i−1↪Z_i−1 with equals'),('insertion','above P_i,Q_i','degré i; degré i−1')],doubts=[('a initial deleted symbol','H_i','scribble too heavy to distinguish entire index','low'),('c deleted index','β_i−1','strike obscures final digit','low'),('d deleted summands','+μ_i; μ_i+','multiple heavy strokes; surviving displayed sums left unrepaired','low'),('proof cancellation','str. ps. coh.','blue strike partly hides letters','low'),('lower proof uniqueness revisions','unique twice; par le choix de; Π_i≃L!','attachment and line-order revisions uncertain','medium'),('diagram Q_i→0','right arrow','short stroke; arrowhead faint','medium')],notation=[('cycles and boundaries',r'$Z_i,B_i$','scan 17; capital Z angled, B double rounded'),('associated-complex ! compared with genuine primes',r'$L^!_\bullet$','scan 17; repeated dots beneath short exclamation stems')])
