import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,175,r'''\scanpage{175}
\mspage{11}

and by $f^{-1}(W)$ we shall denote as usual the set theoretic inverse image of the set of points of $W$. It can be immediately verified that if $W$ is irreducible and of co-dimension one so that $Q(W,V)$ is the valuation ring of a real discrete valuation $v$ of $K(V)/k$ then $f^{-1}[W]$ is also irreducible of co-dimension one and it is the center of $v$ on $V^*$.

2. \uline{Auxiliary Lemmas}.

LEMMA 1. Let $(R,M)$ be a regular local domain of dimension $n>1$ with quotient field $K$. Let $x_1,\ldots,x_n$ be a minimal basis of $M$. Let $y_1=x_1$, \deleted{$y_{\unsure{1|i}}=x_{\unsure{1|i}}\mid\alpha_1$} \inserted{$y_i=x_i/x_1$} for $i=2,\ldots,n$ and let $S=R[y_2,\ldots,y_n]$. Then we have $(y_1S)\cap R=M$ so that $R/M$ can be canonically identified with a subfield of $S/(y_1S)$ and then the residues $\bar y_2,\ldots,\bar y_n$ respectively of $y_2,\ldots,y_n$ modulo $y_1S$ are algebraically independent over $R/M$ and hence $S/(y_1S)$ can be identified with the polynomial ring $(R/M)[\bar y_2,\ldots,\bar y_n]$ in $n-1$ variables. Then the canonical homomorphism of $S$ onto $S/(y_1S)$ sets up a one to one correspondence between the maximal ideals in $S$ containing $y_1$ and the maximal ideals in the polynomial ring $S/(y_1S)$, and hence if $P$ is a maximal ideal in $S$ containing $y_1$ and $R_1=S_P\subset K$ and $M_1=PR_1$ then $(R_1,M_1)$ is a regular local domain of dimension $n$ having center $M$ in $R$, $y_1$ is part of a minimal basis of $M_1$ and $R_1/M_1$ is a finite algebraic extension of $R/M$.
\margin{174}
''',[
('text','top center','11'),('text','upper','and by f inverse(W)'),('text','heading','2. Auxiliary Lemmas'),('text','middle through bottom','LEMMA 1. Let (R,M)'),('deletion','upper middle','y_1=x_1 vertical alpha_1'),('insertion','above deleted formula','y_i=x_i/x_1'),('margin note','bottom left','174')],sheet_kind='reused_typed',remarks='Whole, both halves, and deleted formula enlarged fourfold. The deleted formula has visibly 1-like subscripts (alternative i marked), a vertical division stroke and handwritten alpha_1; its handwritten replacement y_i=x_i/x_1 is clear. Opening formula uses f inverse(W), later f inverse[W], both retained. This sheet is the internal p11 preceding p12 on scan173, but archive scan order is unchanged.')
