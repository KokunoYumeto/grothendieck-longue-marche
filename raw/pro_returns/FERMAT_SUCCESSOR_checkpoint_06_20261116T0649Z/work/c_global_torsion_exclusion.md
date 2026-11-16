# Global torsion exclusion from the actual class at two

**Date:** 2026-11-16. **Author/auditor:** Part C agent. This note gives a new exact consequence of B.36 and the independently constructed primitive inner-path quotient. Publication statement numbering is left to B/root.

## Result

Let \(V\), \(w\), and \(\eta\) have the \(C_0\)-tangent conventions of B.24, B.31, B.35, and B.36, and put

\[
Q=\operatorname{Lie}_3(V)(-1)/\operatorname{ad}_wV.
\]

Then the image of the actual global class \([\eta]\) in

\[
H^1(G_{\mathbf Q(\zeta_3),\{3\}},Q)\otimes\mathbf Q_3
\]

is nonzero. None of the 27 possible local classes furnished by B.36 can be the localization of a global torsion class. The conclusion uses one actual Frobenius at seven and its coefficient action; it does not need a Frobenius word or an identification of complex conjugation after the quaternion basis change.

Together with geometric averaging and B.20's unit-cup comparison, this proves nonvanishing of the specified arithmetic Ross cup-edge class in its one-dimensional rational cohomology space. It does not evaluate the complete global integral action class or remove its finite torsion ambiguity.

## 1. The exact primitive quotient

Use the original ten-dimensional integral basis
\[
(f_1,f_2,A_0,A_1,A_2,B_0,B_1,B_2,C_1,C_2).
\]
Set \(u=3f_1+U_1\) and \(v=3f_2+U_2\). The rows at \(A_0,A_2\) of \((u,v)\) are \((0,-1)\) and \((1,0)\). Hence
\[
B=(u,v,f_1,f_2,A_1,B_0,B_1,B_2,C_1,C_2)
\]
is a unimodular integral basis, with determinant \(-1\) in the original order.

In this new basis write \(e_0=u\), \(e_1=v\), and order the degree-three Hall basis as
\[
[[e_i,e_j],e_k],\qquad i>j,\quad k\ge j.
\]
Since \(w=[e_0,e_1]\), its ten inner-path images are
\[
[e_k,w]=[[e_1,e_0],e_k],\qquad 0\le k<10.
\]
They are ten distinct Hall basis vectors. Thus \(\operatorname{ad}_wV\) is primitive and \(Q\) is free of rank 320, obtained by deleting precisely \((1,0,k)\). There is no saturation or quotient torsion.

The script reconstructs the integer basis inverse, both degree-three basis changes, and verifies
\[
\operatorname{Lie}_3(B^{-1})\operatorname{ad}_wB
   =(\text{the ten indicated unit columns})
\]
modulo \(3^{10}\), in addition to the exact Hall proof.

## 2. The actual Frobenii in the characteristic-two coordinates

Let \(S\) be the compatible compact CM matrix in B.35's strict quaternion basis:
\[
S=-\tfrac12(I_2+I+J+IJ),\qquad S^2+S+I_2=0.
\]
The strict compact basis change preserves \(w\) and conjugates \(R_3\) to \(S\). The actual Frobenius at the chosen prime above seven has compact scalar \(1+3\zeta_3\); its conjugate has \(1+3\zeta_3^2\). Their full degree-one matrices are
\[
T_1=
\begin{pmatrix}
I_2+3S&0\\ U(S-2I_2)&7I_8
\end{pmatrix},
\qquad
T_2=
\begin{pmatrix}
I_2+3S^2&0\\ U(S^2-2I_2)&7I_8
\end{pmatrix}.
\]
Both have cyclotomic value seven. These formulas do not use a complex-conjugation lift. The cross blocks follow by conjugating the actual integral gluing of B.24/B.28.

The actual Frobenius four matrix is
\[
F_4=
\begin{pmatrix}
-2I_2&0\\ -2U&4I_8
\end{pmatrix}.
\]
All three coefficient matrices commute. Their degree-three twisted actions are
\[
R_1=7^{-1}\operatorname{Lie}_3(T_1),\quad
R_2=7^{-1}\operatorname{Lie}_3(T_2),\quad
R_4=4^{-1}\operatorname{Lie}_3(F_4).
\]
After adapting the basis, each preserves the ten deleted Hall columns and acts there by its degree-one matrix, as equivariance of \(\operatorname{ad}_w\) requires. Deleting those rows and columns gives the actual quotient actions, again denoted \(R_i\).

The quotient has no eigenvalue one at good Frobenius: its eigenvalues come from the positive-weight module \(\operatorname{Lie}_3(V)(-1)\). Hence \(D_4=R_4-I\) is rationally invertible.

## 3. An elementary torsion-localization lemma

Let \(L\) be a finite free \(\mathbf Z_3\)-module with continuous action of an arithmetic group \(G\), and let \(f,t\in G\) have commuting coefficient matrices. Assume \(D_f=\rho(f)-I\) is rationally invertible.

If \([z]\in H^1(G,L)\) is torsion, there is \(y\in L\otimes\mathbf Q_3\) with
\[
z(g)=(\rho(g)-I)y.
\]
Indeed divide an integral coboundary for \(3^n z\) by \(3^n\). Integrality of the cocycle gives \((\rho(g)-I)y\in L\). The local class is represented by \(e=D_fy\), and
\[
(\rho(t)-I)e
=D_f(\rho(t)-I)y
\in D_fL.
\]
Thus every global torsion localization is fixed by \(t\) in \(L/D_fL\).

Only the coefficient matrices must commute: no commutation of \(t,f\) in the arithmetic group and no presentation of that group is needed. Integral changes of cocycle representatives preserve the conclusion.

Apply the lemma to \(L=Q\), \(f=F_4\), and either actual Frobenius at seven. A local candidate which is not fixed cannot arise from global torsion. Testing over \(K=\mathbf Q(\zeta_3)\) enlarges the potential torsion source, so exclusion over \(K\) also excludes torsion over \(\mathbf Q\).

## 4. Exact finite certificate

The program deliverable/code/c_char2_inner_quotient.py constructs the primitive quotient independently of B's rectangular quotient presentation. Its NPZ file records all action matrices, basis changes, the quotient projection, the local Smith transport, and the 27 projected candidates.

The complete Smith valuations are
\[
\begin{array}{c|rrrrr}
&0&1&2&3&4\\ \hline
R_1-I&122&84&56&44&14\\
R_4-I&122&70&26&82&20.
\end{array}
\]
Every pivot is below precision \(3^{10}\), and the exact rational rank 320 is supplied by the good-Frobenius weights.

Each of the 27 B.36 candidates projects to exact order 27 in \(Q/D_4Q\). For every candidate \(e\), both
\[
(R_1-I)e,\qquad(R_2-I)e
\]
are nonzero and have exact order nine.

One uniform coordinate certifies exclusion. In the **zero-based** row numbering of the saved local Smith transport, row 193 has modulus nine and
\[
\bigl((R_1-I)e\bigr)_{193}=6,\qquad
\bigl((R_2-I)e\bigr)_{193}=3
\]
for every candidate. No choice of Kummer comparison or actual candidate can make this test vanish.

The exact order-nine assertion has another short witness. Row 300 has modulus 81. The first difference takes values \(18,45,72\), always \(18\bmod27\); the second takes values \(9,36,63\), always \(9\bmod27\). Nine annihilates every whole difference, while three does not annihilate this coordinate.

Transporting row 193 back to the original B.36 Hall basis gives an especially small certificate. Define \(\ell:A\to\mathbf Z/9\) with its only nonzero values
\[
\begin{array}{c|rrrrr}
(i,j,k)&(2,0,4)&(4,0,2)&(4,0,4)&(4,0,8)&(8,0,4)\\ \hline
\ell([[e_i,e_j],e_k])&-1&-2&3&1&-4.
\end{array}
\]
Direct multiplication checks \(\ell D_4=0\) and \(\ell\operatorname{ad}_w=0\). On the B.36 restriction of a thirteen-coordinate vector, its value after applying \(R_1-I\) is
\[
3x_7+6(x_8+x_9+x_{10}+x_{11})\pmod9.
\]
This is six on B.36's base vector \(b\), and zero on both \(h_3,h_9\). Thus the uniform nonzero value follows immediately for every element of the short affine parametrization. The script checks these five-entry identities independently of its complete quotient Smith calculation.

The candidate collection was already independently exhaustive: c_char2_translation_verify.py enumerates all 59,049 sigma/Frobenius-two candidates, tests both translations for all three Kummer comparisons, and finds exactly nine survivors per comparison. The present test does not select a survivor or assume it is the actual class.

B independently used the rectangular \(330\)-by-\(340\) presentation
\[
A/\bigl((F_4-I)A+\operatorname{ad}_wV\bigr)
\]
and obtained the same order-nine differences for all 27 candidates; its files are b_char2_outer_torsion.py and associated outputs. This is a different quotient construction from literal deletion in a unimodular Hall basis.

Since the actual class is among the candidates, the lemma proves the asserted nonzero rational global class in \(Q\).

## 5. Identification with the arithmetic Ross component

The quotient test by itself proves rational nonvanishing in \(Q\); its component is identified as follows.

Use the rational compact/boundary splitting \(V_{\mathbf Q_3}=H\oplus W\) and choose a rational Lie lift \(\omega=[u,v]\). The degree-three variation of a commutator is the derivation applied to its two inputs. Its possible multidegrees therefore are
\[
\operatorname{Lie}_3(H),\qquad H^2W,\qquad
J(H\otimes\Lambda^2W),
\quad J(a\otimes(r\wedge s))=[a,[r,s]].
\]
There is no \(W^3\) term, and its \(HW^2\) term belongs to \(\operatorname{im}J\).

More explicitly, write the degree-one, degree-two, and degree-three parts of the image of a generator \(z\) as \(A_gz+B_gz+C_gz\). Then
\[
g[u,v]=[A_gu,A_gv]+[B_gu,A_gv]+[A_gu,B_gv]
\]
modulo degree four. Terms containing \(C_g\) already have degree at least four and cannot contribute. The first term is \(\chi_3(g)w\), and the two others have a compact factor. If the quadratic part lies in \(\Lambda^2W\), its contribution is exactly a bracket \([h,[r,s]]\), proving membership in \(\operatorname{im}J\) rather than only in the whole \(HW^2\) multidegree.

The pure Lie lift is permitted because this step is rational: the class-three Malcev logarithm and BCH formulas exist over \(\mathbf Q_3\), even at the prime three. Its difference from an integral group-commutator lift is a rational degree-three vector and changes \(\eta\) by a rational coboundary. No integral BCH assertion is used.

Average over \(\mathcal A=E[3]\rtimes\mu_6\). B.17's exact path identity says that the difference between \(\eta\) and its average is an inner-path class, so it disappears in \(Q\). The rational splitting is preserved by \(\mathcal A\).

Apply the individual automorphism/path identities over \(K\), where all 54 automorphisms are defined. An individual automorphism need not be \(\mathbf Q\)-rational, and is not being asserted to commute with \(G_{\mathbf Q}\). The average is nevertheless \(G_{\mathbf Q}\)-equivariant, because Galois permutes the set \(\mathcal A\). The rational splitting is preserved because every such automorphism commutes with good Frobenius over \(K\), whose compact and toric weights are different; equivalently, the explicit compact columns \((3I_2,U)^{\mathsf t}\) are preserved. Thus every multidegree used above is stable under averaging.

The average kills \(\operatorname{Lie}_3(H)\) because the origin involution acts there by minus one. It kills \(H^2W\) because translations act trivially on \(H\) and \(W\) has no translation invariants. Its invariant part on \(\operatorname{im}J\) is precisely B.20's rank-two module \(D\), with \(D(-1)\simeq H(1)\).

Moreover \(V^{\mathcal A}=0\), and \(\mathcal A\) fixes \(w\), so \((\operatorname{ad}_wV)^{\mathcal A}=0\). Rational invariants are exact, hence \(A(-1)^{\mathcal A}\to Q_{\mathbf Q_3}^{\mathcal A}\) is an isomorphism. Thus quotienting by inner terms neither loses nor manufactures an invariant Ross component.

The nonzero rational image proved above is therefore exactly the image of the averaged elliptic component. B.20's identity gives a **nonzero** arithmetic cup-edge class. Its rational coefficient space has rank one, so the specified Ross edge spans it; the coefficient of the actual elliptic component relative to that class is the already-proved \(-1\), or \(-1/6\) relative to the tame multiple \(6e_R\). This supplies arithmetic nonvanishing which the real regulator calculation alone did not establish.

This assertion concerns cohomology, not a chosen invariant representative before averaging. On rational continuous cochains the finite averaging idempotent is exact and commutes with the differential. The projected class is invariant by the path identity, so its average is the same class; averaging the permitted rational commutator representative gives a cocycle valued in \(D(-1)\). Since the average is \(G_{\mathbf Q}\)-equivariant, this cocycle is global over \(\mathbf Q\), and its nonzero restriction to \(K\) proves that its global class is nonzero. There is no missing descent assumption.

## 6. Scope and dependencies

This is a computation in the actual geometric coefficient lattice with its actual arithmetic action. All possible comparison maps and actual-class candidates are retained, and every one violates a necessary global torsion condition.

It does not select a complete integral global cocycle, reduce its ambiguity to \((\mathbf F_3)^3\), or make the fixed order-\(3^{30}\) quotient a complete invariant. B.21–B.22 remain applicable. The exact local order \(m_2=3\) and global rational nonvanishing are complementary conclusions.

The new torsion-localization lemma and primitive quotient are proved here. External dependencies are exactly the already verified inputs of B.24, B.28, B.35, B.36: the actual Frobenius-seven scalar; strict quaternion/CM comparison; based prime-to-two specialization; ordinary Abel–Tate comparison with its directly proved tangential normalization. No additional regulator comparison, unrefereed arithmetic presentation, or Frobenius word is used.
