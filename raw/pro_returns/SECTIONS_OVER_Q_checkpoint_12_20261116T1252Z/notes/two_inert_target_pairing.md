# Exact target comparison after A151

This note records proved maps; it makes no claim that the full norm target
is obstructed or solved in the two-prime tower.

Use A151's fields

\[
k=\mathbf Q(\mu_3),\quad F=k(649^{1/3}),\quad
a=3\cdot11^{M_1}59^{M_2},\quad
L_n=\mathbf Q(\mu_{3^n},a^{1/3^n}),\quad24\mid M_i.
\]

## The whole contribution of the specified genus field

Put \(N=3^n\), \(P=\mathbf F_3[\mathbf Z/N]\), and
\(J=P/\mathbf F_3\mathbf1\). This is the actual Cartier dual of the
mod-three augmentation kernel in the root-torsor permutation module,
so it is the finite coefficient norm-torus dual appearing in A109/A149.
Writing \(X\) for translation and \(Z=X-1\) identifies it with
\(\mathbf F_3[Z]/Z^{N-1}\). Translation acts by multiplication by
\(X\); a cyclotomic unit \(u\) substitutes \(X\mapsto X^u\).

The terminal line has the exact equivariant inclusion

\[
i:\mu_3\longrightarrow J,\qquad i(1)=Z^{N-2}.
\]

Translation fixes it because \(Z^{N-1}=0\). Cyclotomic substitution
multiplies it by \(u^{N-2}=u\pmod3\). Thus the indicated source really
has the cyclotomic action, not the trivial action.

Set \(E=FL_n\). A151 proves \(F\cap L_n=k\). Consequently
\(\operatorname{Gal}(E/L_n)=C_3(\chi)\): conjugation by the cyclotomic
involution inverts this cubic radical. Since the translation invariants
of \(J\) are exactly its terminal line,

\[
\operatorname{Hom}_{\operatorname{Gal}(L_n/\mathbf Q)}
  (\operatorname{Gal}(E/L_n),J)=\mathbf F_3\cdot i.
\]

A109's proved finite group calculation gives
\(H^1(\operatorname{Gal}(L_n/\mathbf Q),J)=0\). The actual
inflation--restriction sequence therefore injects
\(H^1(\operatorname{Gal}(E/\mathbf Q),J)\) into this one-dimensional
space. The class \(i_*\kappa_3(649)\), which factors through \(E\), has
nonzero restriction to \(\operatorname{Gal}(E/L_n)\). Hence

\[
H^1(\operatorname{Gal}(E/\mathbf Q),J)
       =\mathbf F_3\cdot i_*\kappa_3(649).
\]

## The exact local map at 11 and 59 is injective

Fix \(q\in\{11,59\}\). All rational \(q\)-adic units have compatible
three-power roots, because \(3\nmid q-1\). Choose tame inertia
\(\tau\) and Frobenius \(\Phi\) fixing these unit roots and the
chosen roots of the uniformizer. On the root labels of \(a\), the
two actions are

\[
\tau:i\mapsto i+M_q,\qquad \Phi:i\mapsto qi.
\]

For \(\kappa_3(649)\), their cocycle values are one and zero,
respectively. Thus a local coboundary for the displayed nonzero global
class would require \(w\in J\) satisfying

\[
(X^{M_q}-1)w=Z^{N-2},\qquad \sigma_q w=w.
\]

Here \(q\) generates \((\mathbf Z/N)^\times\): it is minus one
modulo three and \(v_3(q^2-1)=1\), so the exact order is
\(2\cdot3^{n-1}\) by the elementary lifting-the-exponent identity.
Lift \(w\) to its coefficient vector in \(P\). The difference between
that vector and its Frobenius translate is constant; its coefficient
at label zero is zero, so that difference is literally zero.
The coefficients of \(w\) are therefore constant on all unit labels.
Since \(3\mid M_q\), both \(i\) and \(i-M_q\) are units whenever
\(i\) is, and every unit-label coefficient of
\((X^{M_q}-1)w\) is zero.

In contrast, the coefficients of \(Z^{N-2}\), modulo a constant
vector, are \(-i\pmod3\). This follows by differentiating
\((X-1)^{N-1}=\sum_{i=0}^{N-1}X^i\). Their two values on the unit
residue classes are different, and no single added constant makes both
zero. The two equations have no solution.

Therefore localization at either 11 or 59 is injective on the entire
one-dimensional group above. In particular

\[
\ker\left(H^1(\operatorname{Gal}(E/\mathbf Q),J)
       \longrightarrow\prod_{q\in\{2,3,11,59\}}H^1(\mathbf Q_q,J)
    \right)=0.
\]

This states an exact comparison of the new class field with the actual
norm-torus dual module. It does not assert that every class split by a
larger class field has this form.

The retained program `work/code/two_inert_target_dual_exploration.py`
checks the literal coefficient matrices and impossibility for
\(n=1,\ldots,5\), with output in the adjacent `_output.txt` file.
The proof above is independent of the finite checks.

## The valuation divisor of the target -2

At two the pure root field has the compatible degree-one branch of its
odd-power unit root. Put valuation one on that branch and zero on every
other branch. At every other finite prime the rational target -2 is a
unit; the local norm families use valuation zero. The resulting divisor
has norm \((2)\). This is the concrete divisor choice for the target;
no global principal representative is assumed.

After pullback to \(L_n\) its support is still entirely above two.
A151 proves that \(FL_n/L_n\) splits at every such prime. Its actual
Artin character therefore evaluates to zero on this divisor, at every
level, with the same norm transition as A151. This computes the pairing
with this particular class quotient, rather than inferring an
obstruction from the nonzero quotient alone.

## Remaining map

The unresolved computation is the image of the norm target in the
finite-set degree-two groups for the full augmentation coefficient
system, or equivalently its pairing with all relevant locally trivial
dual classes. The specified genus character above contributes no such
dual class. The entire class group of \(L_n\), and its other
representations under \(\operatorname{Gal}(L_n/\mathbf Q)\), have not
been identified by A151.
