import sys
sys.path.insert(0,'MPL_33_147-181+34_002-017_work/records')
from workflow import save_page
save_page(33,173,r'''\scanpage{173}
\mspage{12}

\uline{Proof}. Follows from [A7, Lemma 3.19 of Section 14].

LEMMA 2. Let $(R,M)$ and $(\bar R,\bar M)$ be two regular local domains of the same dimension $n$ with quotient fields $K$ and $\bar K$ respectively. Assume that $K$ is a subfield of $\bar K$, $\bar R$ has center $M$ in $R$ and $M\bar R=\bar M$. Then $R/M$ can be canonically identified with a subfield of $\bar R/\bar M$; assume that under this identification $\bar R/\bar M=R/M$, i.e., given $x$ in $\bar R$ there exists $y$ in $R$ such that $x-y$ is in $\bar M$. Then given $x$ in $R$ and a positive integer $q$ there exists $y$ in $R$ such that $x-y$ is in $\bar M^q$. Also we have that $K\cap\bar R=R$, $K\cap\bar M=M$, $M^qR=\bar M^q$ for any positive integer $q$, and if $A$ is any ideal in $R$ then $(A\bar R)\cap R=A$ and $A$ is principal if and only if $A\bar R$ is principal, in particular $\bar M^q\cap R=M^q$ for any positive integer $q$. Consequently, any completion of $\bar R$ is also a completion of $R$.

\uline{Proof}. From $M\bar R=\bar M$ we at once have $M^q\bar R=\bar M^q$ for all $q>0$. By induction on $q$ we shall show that given $x$ in $\bar R$ there exists $y$ in $R$ such that if $x-y$ is in $\bar M^q$; for $q=1$ this is given, so assume that $q>1$ and that this is true for $\unsure{q.-1|q-1}$. Then given $x$ in $\bar R$ there exists $z$ in $R$ such that $x-z$ is in $\bar M^{q-1}$; since $\bar M^{q-1}=M^{q-1}R$, $x-z=\sum a_ib_i$ with $a_i$ in $M^{q-1}$ and $b_i$ in $\bar R$, the assumption for $q=1$ tells us that there exists $c_i$ in $R$ and $d_i$ in $\bar M$ such that $b_i=c_i+d_i$, let $y=z+\sum a_ic_i$, then $x-y=\sum a_id_i$ which is in $\bar M^q$.

Now let $x_1,\ldots,x_n$ be a minimal basis of $M$, since $M\bar R=\bar M$
\margin{172}
''',[
('text','top center','12'),('text','upper','Proof. Follows from [A7, Lemma 3.19 of Section 14]'),('text','upper through middle','LEMMA 2. Let (R,M) and (bar R,bar M)'),('text','lower','Proof. From M bar R = bar M'),('text','bottom','Now let x_1,...,x_n'),('margin note','bottom left','172')],sheet_kind='reused_typed',remarks='Whole and both halves read. The statement visibly says given x in R (unbarred) in its second approximation sentence, and M^q R (unbarred R) in the subsequent equality. The proof similarly has M^(q-1)R without a bar, but its opening formula uses barred R. All these visible differences are retained. The phrase such that if is typed and retained. A possible stray period after q in q.-1 is marked.')
