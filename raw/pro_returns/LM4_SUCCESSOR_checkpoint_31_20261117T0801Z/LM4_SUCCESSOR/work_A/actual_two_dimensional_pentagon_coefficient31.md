# The actual two-dimensional pentagon forces the full coefficient equality

Cycle31 research; proposed new theorem, pending independent full review.
All earlier sources remain unchanged. This uses the actual canonical
word of a **full-GT** involution. It asserts no general-GT0 or general-P
conclusion and does not prove the nonlinear cusp equation.

## 1. Exact input and normalization

Let \(\alpha=(-1,\varphi)\in\widehat{GT}\) be an involution, and let
\(u\in\widehat F(x,y)'\) be its actual canonical norm word. A37,
whose complete proof was reread, proves the full profinite pentagon
for this very \(u\): the actual fixed arrow \(A u\), all five genuine
operadic insertions, and C28's trivial fixed subgroup in
\(\widehat P_4\) make its entire discrepancy one. Fixed arrows alone
are not being substituted for that last theorem. Thus in the original
marking \((a,b,c,d,e,f)=(A_{12},A_{13},A_{23},A_{14},A_{24},A_{34})\),
\[
 u(a,ce)u(bc,f)=u(c,f)u(ab,ef)u(a,c).                 \tag{1}
\]

Use the actual first-cusp module
\(\Lambda=\mathbb F_2[[\widehat{\mathbb Z}]]\), with \(x\mapsto(1,1)\),
\(y\mapsto(0,T)\), and write \(U=[u]\), \(\bar U=U(T^{-1})\).
The ORIGINAL A88 normalization is
\[
 \theta=1+(T-1)(U+\bar U),\qquad
 (T-1)D_b=T^b-1,\qquad
                         \theta D_a=1,               \tag{2}
\]
where \(a=a_{\rm reg}\) is the actual full unit.
In particular \(\theta\) is a unit. A45 gives the actual universal
dihedral image \(u(x,y)\mapsto R^k\), with
\[
                         d=d_\alpha=2k+1.
\]
The full-GT dyadic equality \(a_2=d_2\) is already proved in A89.

The new assertion is \(a=d\) in the **full**
\(\widehat{\mathbb Z}\).

## 2. An entire genuine marked quotient with nontrivial odd boundary

Let \(\Bbbk\) be any finite field of characteristic two, and let
\(\rho\in\Bbbk^\times\) have odd order \(n>1\).
Put \(t=\rho+1\ne0\), \(V=\Bbbk^2\), and
\[
 D=\begin{pmatrix}1&0\\t/\rho&1\end{pmatrix},
 \qquad F=\begin{pmatrix}1&t\\0&1\end{pmatrix},
 \qquad R=FD.
                                                               \tag{3}
\]
The letter \(F\) in (3) is a matrix, not the original free group.
Both matrices are involutions. The matrix \(R\) has determinant one
and eigenvalues \(\rho,\rho^{-1}\), which are distinct; hence it has
order \(n\), and \(D,F\) generate the actual dihedral group of order
\(2n\).

In the finite group \(V\rtimes\langle\rho I,D,F\rangle\), with
\((v,M)(w,N)=(v+Mw,MN)\), prescribe the actual sphere-kernel generators
by
\[
 P\mapsto(0,\rho I),\quad A\mapsto(e_1,I),\quad
 C\mapsto(e_2,I),\quad d\mapsto(e_2,D),\quad
 f\mapsto(e_1,F).                                    \tag{4}
\]
This is a homomorphism from the complete marked
\(G=P_4/\langle\Delta_4^2\rangle\), not an independently chosen
tuple. To verify all relations, use the exact free-three
presentation in the earlier cycle31 note. The three conjugation
images under \(d\) in (4) are
\[
 P\mapsto((\rho-1)e_2,\rho I),\quad
 A\mapsto(e_1+(\rho^{-1}-1)e_2,I),\quad C\mapsto(e_2,I);
\]
these are exactly \(C^{-1}PC,C^{-1}P^{-1}CPA,C\).
The three images under \(f\) are
\[
 P\mapsto((\rho-1)e_1,\rho I),\quad A\mapsto(e_1,I),\quad
 C\mapsto(e_2+(\rho-1)e_1,I);
\]
these are exactly \(A^{-1}PA,A,CPA^{-1}P^{-1}A\).
All six defining action relations have therefore been checked
symbolically. In particular the original boundary \(P\) has its
specified nontrivial odd order \(n\); it has not been killed.

Recovering the original six generators by the inverse presentation
gives the following entire tuple:
\[
\begin{array}{c|c}
a&(0,F)\\
b&(0,\rho^{-1}FD)\\
c&(0,D)\\
d&(e_2,D)\\
e&(\rho(e_1+e_2),\rho DF)\\
f&(e_1,F).
\end{array}                                                   \tag{5}
\]
For example \(a=Af,c=Cd,e=d^{-1}Pf^{-1}\), and
\(b=a^{-1}P^{-1}c^{-1}\); thus (5) retains the original ordering.
The quotient is two-dimensional with a nonabelian linear head,
so A94's one-dimensional affine classification does not dispose of
this family.

## 3. Evaluate all five actual pentagon pairs

All evaluations below are evaluations of the same full \(u\).
They extend continuously to this finite group. Set
\[
                         w=e_2/t.
\]
Then
\[
                           (R-I)w=e_1.                \tag{6}
\]

First, the pair \((c,f)\) is the conjugate of the linear pair
\((D,F)\) by the translation \(w\): \(Dw=w\), and
\(w-Fw=e_1\). The pair \((a,c)\) is exactly the linear pair
\((F,D)\). The actual dihedral exponent therefore gives
\[
 u(c,f)=(w-R^{-k}w,R^{-k}),\qquad
 u(a,c)=(0,R^k).                                      \tag{7}
\]
The inverse rotation in the first formula is forced by the reversed
ordered pair, not an arbitrary choice of dihedral generator.

The remaining products obtained directly from (5) are
\[
 ce=(\rho e_1+e_2,\rho F),\quad
 bc=(0,\rho^{-1}F),\quad
 ab=(0,\rho^{-1}D),\quad ef=(e_2,\rho D).              \tag{8}
\]

For the pair \((a,ce)\), conjugate both elements by the translation
\(-q\), \(q=(e_1+e_2)/t\). Their translation parts become \(e_1,e_1\);
their linear parts remain \(F,\rho F\). The line \(\Bbbk e_1\) is
invariant, and these linear parts act on it as \(1,\rho\).
Thus the evaluation reduces to the scalar affine pair
\((1,1),(1,\rho)\). Translating that scalar pair by
minus \(1/(\rho-1)\) makes the second translation zero while leaving
the first unchanged. Since \(u\) is a commutator word, its head is
one; conjugating its translation by a translation does not change
it. Hence
\[
                          u(a,ce)=(U(\rho)e_1,I).      \tag{9}
\]

For \((bc,f)\), both translations already lie in \(\Bbbk e_1\);
the scalar pair is \((0,\rho^{-1}),(1,1)\).
The actual literal duality \(u(y,x)=u(x,y)^{-1}\), and characteristic
two on the additive line, give
\[
                          u(bc,f)=(U(\rho^{-1})e_1,I). \tag{10}
\]

Finally \((ab,ef)\) has both translations in \(\Bbbk e_2\) and
commuting linear parts \(\rho^{-1}D,\rho D\), acting on that line
as the scalars \(\rho^{-1},\rho\). Therefore, for an actual scalar
\(Y_\rho\in\Bbbk\),
\[
                          u(ab,ef)=(Y_\rho e_2,I).     \tag{11}
\]
No formula for \(Y_\rho\) is needed, and it is not set to zero.
In particular the third-cover coefficient has not been discarded.

## 4. The actual pentagon gives the missing weighted covariance

Let \(B_\rho=U(\rho)+U(\rho^{-1})\). Substituting (7)--(11) into
the actual pentagon (1), with the semidirect product law in its
displayed order, gives
\[
 B_\rho e_1=w-R^{-k}w+R^{-k}Y_\rho e_2.
\]
Multiplying by \(R^k\) and using (6) gives
\[
 R^k\bigl[I+B_\rho(R-I)\bigr]w
                         =(1+tY_\rho)w.              \tag{12}
\]

The vectors \(w,Rw\) are independent by (6), so the projections of
\(w\) to both distinct eigenlines of \(R\) are nonzero. Evaluate
(12) on those two eigenlines:
\[
 \rho^k[1+(\rho-1)B_\rho]
 =1+tY_\rho
 =\rho^{-k}[1+(\rho^{-1}-1)B_\rho].                  \tag{13}
\]
The unknown \(Y_\rho\) is retained until this equality, then
eliminated by comparing the two equal values.
By (2) and the definition of \(B_\rho\), (13) is exactly
\[
                     \theta(\rho^{-1})
                        =\rho^{2k}\theta(\rho)
                        =\rho^{d-1}\theta(\rho).       \tag{14}
\]
This uses the original \(\theta\) of A88, not a differently normalized
coefficient involving \(Y_\rho\).

On the other hand, the full continuous geometric-sum identity is
\(\overline{D_a}=T^{1-a}D_a\). Apply coefficient inversion to
\(\theta D_a=1\) in (2). Since \(D_a\) and \(\theta\) are units,
\[
                         \bar\theta=T^{a-1}\theta.     \tag{15}
\]
Specializing (15) at \(\rho\), comparing with (14), and cancelling the
nonzero \(\theta(\rho)\), gives
\[
                              \rho^{a-d}=1.            \tag{16}
\]

For every odd \(n>1\), some finite field of characteristic two contains
an element of exact order \(n\). Apply the construction to that element.
Equation (16) says \(a\equiv d\pmod n\). Hence all odd components of
the two actual profinite units agree. Their dyadic components agree by
the already proved full-GT result A89. Therefore
\[
                 \boxed{a_{\rm reg}=d_\alpha
                         \quad\text{for full-GT involutions}.}  \tag{17}
\]

Equivalently the actual regular-frame scalar satisfies
\(\xi=-(d_\alpha-1)/4\), and the full abelianization of the original
\(\Omega_\alpha\) is zero. Torsion-freeness of
\(\widehat{\mathbb Z}\) justifies this cancellation of four.

## 5. Boundaries and the preserved exploratory correction

This proves a necessary full coefficient equality, not the full word
\(\Omega_\alpha=1\), the missing cubic relation, or a Main-A decision.
It depends on the actual full-GT canonical-\(u\) pentagon A37 and
the full-GT dyadic theorem; neither is inserted for arbitrary GT0 data.
Every quotient above comes from the same complete original P4
presentation, and all five pentagon evaluations were retained.

During exploratory messages an auxiliary scalar \(1+tY_\rho\) was
mistakenly compared with a shifted version of A88's equation. That
normalization was immediately corrected after reopening the complete
A88 proof. It is **not** used here. The correct argument is
(13)--(16), with \(\theta D_a=1\) throughout; it needs neither a
mixed-head ring argument nor a choice between plus/minus exponents.
Those exploratory messages remain preserved in the conversation.

No finite target census, period sweep, producer, private render, or
new external theorem was used. The entire uniform quotient and all
word evaluations are the symbolic proof above. Independent review is
required before any formal promotion.
