# The original associator determines the same sphere-kernel correction

Cycle31 research. This continues the two reviewed sphere-kernel notes,
without changing them. All statements here use the actual full-GT
involution in the original source-based parenthesized-braid convention
of A36. No four-strand action for arbitrary GT0 data is supplied.

Write the involution parameter as \(\varphi=\varphi_\alpha\), reserving
\(f=A_{34}\) for the actual braid generator. Its canonical word is the
already established \(u\in\widehat F(x,y)'\), with
\(u=\varphi\,\alpha(u)\).

## 1. Two literal cabling arrows

Use the actual objects and source-based associativity arrows of A36:

\[
 b_0=(((12)3)4),\qquad b_4=((12)(34)),\qquad
 b_3=(1(2(34))).
\]

Let \(D_1:b_0\to b_4\) be the underlying-identity arrow obtained by
inserting the blocks \((12),3,4\), and let \(D_2:b_4\to b_3\) insert
\(1,2,(34)\). Their actual source-based parameters, also the two left
arguments of the originally marked pentagon, are

\[
 \alpha(D_1)=D_1p,\quad p=\varphi(bc,f),\qquad
 \alpha(D_2)=D_2\varphi(a,ce).                         \tag{1}
\]

These are precisely A36's two-edge path, with its original convention
\(\alpha(D)=D\varphi\). Thus the ordered arguments do not come from
independently relabelling a sphere quotient.

At \(b_0\), the paired block twist \(bc\) is literally inverted: it is
the quotient of the first-three full twist \(abc\) by \(a\), both of
which are literally inverted and commute in this parenthesization.
At \(b_4\), \(f\) is the internally grouped pair twist and is literally
inverted. Transport along \(D_1\), with composition right to left,
therefore gives

\[
 \alpha(bc)=(bc)^{-1},\qquad
 \alpha(f)=p^{-1}f^{-1}p.                             \tag{2}
\]

The action on \((bc,f)\) is exactly the original normalized rank-two
action with parameter \(\varphi\).

## 2. The actual canonical word gives a genuine conjugacy

Retain the established exact presentation

\[
 G=N\rtimes B,\quad N=F(P,A,C),\quad B=F(d,f),\quad
 P=def,\ A=af^{-1},\ C=cd^{-1},\ R=PA,\ S=CP,\ L=SA.
\]

The literal relation \(abc=P^{-1}\) gives
\[
                         bc=f^{-1}R^{-1}.             \tag{3}
\]
Put \(z_u=u(bc,f)\). Both \(p\) and \(z_u\) lie in the closed
commutator subgroup \((\widehat N)'\). Indeed the actual base action is
trivial on \(N_{\rm ab}\), so
\(\widehat G/(\widehat N)'=(\widehat N)_{\rm ab}\times\widehat B\).
Here \((\widehat N)_{\rm ab}=\widehat{\mathbb Z}^{3}\), and all subsequent abelian coordinates of completed elements are taken in this compact abelianization; the prime denotes the closed commutator subgroup. The two inputs in (3) and \(f\) commute there. Both \(\varphi\) and
\(u\) are commutator words, so their evaluations are one in that quotient.

Evaluation of the actual canonical norm equation using (2) gives
\[
                    z_u=p\,\alpha(z_u).               \tag{4}
\]
Equivalently the genuine arrow \(D_1z_u\) is fixed, as in A36/A37.
Consequently
\[
 \gamma:=\operatorname{Inn}(p)\alpha
   =\operatorname{Inn}(z_u)\,\alpha\,
                       \operatorname{Inn}(z_u^{-1}).  \tag{5}
\]
The equality follows from \(z_u\alpha(z_u)^{-1}=p\), with exactly this
order. Unlike the normalized reflection \(\beta\) of the previous
note, \(\gamma\) is now proved to be conjugate to the original
involution by a specified actual word in \((\widehat N)'\).

## 3. A literal free-factor copy of the original canonical system

The subgroup \(F(A,S)\) is a free factor of \(N\): \((P,A,S)\) is a
free basis. Moreover \(f\) fixes both \(A,S\), so its product with that
free factor is direct. The original words are

\[
                       a=Af,\qquad ce=Sf^{-1}.         \tag{6}
\]

The action at \(b_4\) is \(\gamma\), by (1). It inverts \(a,f\)
literally. Its next associativity arrow \(D_2\) says

\[
 \gamma(ce)=\varphi(a,ce)^{-1}(ce)^{-1}\varphi(a,ce).
\]

Since \(f\) is central in the group on \(A,S,f\), any commutator word
evaluated at (6) has zero central \(f\)-coordinate and is its evaluation
at \(A,S\). This can be checked first on discrete words and then by
continuity in the full free profinite group. In particular
\[
 \varphi(a,ce)=\varphi(A,S),\qquad u(a,ce)=u(A,S).
\]
It follows that
\[
 \gamma(A)=A^{-1},\qquad
 \gamma(S)=\varphi(A,S)^{-1}S^{-1}\varphi(A,S).          \tag{7}
\]

Thus (7) is literally the original \(\alpha\) under
\((x,y)\mapsto(A,S)\). The word \(u(A,S)\) is the actual canonical
solution in this copy, not an arbitrary solution of a separate cocycle
equation. The based-arrow construction, the original associator, and
the entire canonical \(u\) have all been retained.

## 4. Exact formula and full abelianization of the common correction

The third-cusp property of the original negative action, now applied
inside the literal copy (7), gives a transporter \(t\in\widehat F(A,S)\)
with
\[
                       \gamma(L)=t^{-1}L^{-1}t,
                       \qquad L=SA.                  \tag{8}
\]
Normalize \(t\) to have zero \(L\)-coordinate in the free basis
\((L,A)\). This is unique: \(L\) is primitive and its full centralizer
in this free group is \(\widehat{\mathbb Z}(L)\).

Let \(h_0\) be the unique zero-\(L\)-coordinate full transporter from
the preceding note:
\(\alpha(L)=h_0^{-1}L^{-1}h_0\), in the free basis \((L,A,C)\).
By (5), \(h_0p^{-1}\) satisfies (8). Since \(p\in(\widehat N)'\), it
has the same zero \(L\)-coordinate. The normalization inside the free
factor \((L,A)\) agrees with the normalization in \((L,A,C)\), so
uniqueness of the primitive centralizer in \(\widehat N\) gives

\[
                              h_0=t\,p.               \tag{9}
\]

There is also an exact integral abelianization, without division or a
finite-head search:
\[
             t_{\rm ab}=-A,\qquad (h_0)_{\rm ab}=-A.   \tag{10}
\]
To prove it, pass only for this calculation to the universal
two-step nilpotent quotient of the free group on \(A,S\), realized by
the integral Heisenberg quotients over all \(\mathbb Z/n\).
The word \(\varphi(A,S)\), being in the commutator subgroup, is central
there. Hence (7) gives
\(\gamma(L)=S^{-1}A^{-1}\) there. The element \(A^{-1}\) is a
transporter for the same equality, since
\[
               A\,L^{-1}A^{-1}=S^{-1}A^{-1}.
\]
Therefore \(tA\) centralizes \(L\) in this class-two quotient. The
commutator coordinate with \(L=SA\) is the difference of the two
abelian coordinates; its vanishing is an exact equality in
\(\widehat{\mathbb Z}\). Since the normalized \(t\) has zero
\(L\)-coordinate, its \((A,S)\)-coordinates are \((r,0)\).
The coordinates of \(tA\) are \((r+1,0)\), so \(r+1=0\).
This proves the first equality in (10); (9) and \(p\in(\widehat N)'\)
give the second.

In particular \(h_0\) is not an \(\alpha\)-coboundary in
\(\widehat N\). Indeed \(\alpha\) acts as minus identity on
\(N_{\rm ab}\), so every \(q\alpha(q)^{-1}\) has abelianization
\(2q_{\rm ab}\), whereas (10) has odd \(A\)-coordinate. Thus the
sections represented by \(\alpha\) and \(h_0\alpha=\beta\) in the
actual semidirect extension are not \(\widehat N\)-conjugate.
This is a genuine section-class distinction, not merely a failure to
choose a convenient transporter.

The same nonconjugacy persists in every actual relative pro-two
quotient of the previous note. Its embedded \(N^{(2)}\) retains the
\(A\)-character modulo two. That character extends to the whole
relative group by zero on the base, because the base action is IA;
it is invariant under \(\alpha\). It is one on \(h_0\) and zero on
every coboundary. In particular forgetting \(h_0\) in those quotients
would replace the original section by a different one.

## 5. The exact remaining role of the odd head

The IA action of \(B\) on \(N^{(2)}\) factors through \(B^{(2)}\).
For every characteristic finite two-group quotient of \(N^{(2)}\),
the induced base action lies in the Frattini automorphism kernel,
which is a two-group by the complete internal proof in the preceding
note. Taking those quotients proves the asserted factorization.

Consequently the normalized compatibility
\[
 \beta_N\theta_b\beta_N^{-1}=\theta_{\alpha_0(b)}
\]
on this retained kernel sees the base through its pro-two image.
This is an exact factorization statement; it is not a realization
claim for arbitrary canonical data or an assertion that the entire
relative quotient carries no odd information. The specified finite
odd head and the original \(\alpha_0\) are still retained in the base.
Any new odd coefficient implication must use that extra based data
together with (9), rather than treating this kernel action as a
faithful record of the full base.

Equations (5), (7), (9), and (10) close the same-correction/cabling
identification at its stated scope. They do not identify the
regular-pants frame of A86 with this negative third-cusp transporter.
In particular \(t\) here is not A86's scalar or its regular reflection
conjugator. The equality \(a_{\rm reg}=d_\alpha\) and the nonlinear
\(\Omega_\alpha=1\) remain open.

All arguments use the complete original source-based insertion
convention of A36/A37 and the actual marked pentagon arguments already
bound in A94. No new producer, finite census, private render, or
unverified four-strand action was used.
