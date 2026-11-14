# Abelian intermediate covers do not enlarge the primitive-zero criterion

Status: independently approved by root and topos, and integrated as A.C2.23 in sections/A_abelian_tower_descent.tex. The finite-field agent inserted the input in A_char2_deck.tex and updated its owned claim ledger and report; its validator passed with 58 owned rows. No shared A source or ledger was edited by this author.

Question locus: 149; manuscript pp.17–17v; scans35–36. This deduction is part of the present audit and is not attributed to the manuscript.

## 1. Exact statement

Let \(k\) be an algebraically closed field of characteristic \(p>0\), let \(C/k\) be a smooth proper connected curve, and let \(W\to C\) be a connected finite étale Galois cover with finite abelian group \(A\), of odd order prime to \(p\).

Let \(H\subset A\) be a nontrivial cyclic subgroup of order \(n\), put \(V=W/H\), and let \(h\) generate \(H\). Suppose that the primitive cyclic factor

\[
P_H=\operatorname{im}\left(
\prod_{\ell\mid n}(1-h^{n/\ell}):J_W\longrightarrow J_W
\right)
\]

has \(p\)-rank zero.

Then there is an intermediate quotient \(D=W/K\) such that \(D\to C\) is cyclic of odd order \(N>1\), prime to \(p\), and its primitive conductor-\(N\) factor has \(p\)-rank zero. The integer \(N\) is divisible by \(n\).

Consequently the following two geometric existence conditions on a fixed \(C\) are equivalent:

1. \(C\) has a cyclic odd prime-to-\(p\) étale cover with zero-\(p\)-rank primitive factor.
2. Such a cyclic stage occurs over an intermediate base inside some finite odd prime-to-\(p\) abelian Galois cover of \(C\).

For genus at least two over a finitely generated field, either condition implies A1 by A.C2.20, after descending the finite geometric data. The theorem concerns an abelian **total** cover \(W/C\). A succession of abelian covers can have a nonabelian normal closure over \(C\); that situation is not covered by the equivalence.

## 2. The Tate-module criterion for a primitive factor

Write

\[
\mathcal T_W=T_p(J_W)\otimes_{\mathbf Z_p}\overline{\mathbf Q}_p.
\]

Here \(T_p\) uses geometric \(p\)-power torsion points, so its rank is the \(p\)-rank. Since \(|A|\) is prime to \(p\), the finite \(A\)-action is semisimple. Because \(A\) is abelian, it decomposes into character spaces

\[
\mathcal T_W=\bigoplus_{\psi\in A^\vee}\mathcal T_{W,\psi},
\qquad
A^\vee=\operatorname{Hom}(A,\overline{\mathbf Q}_p^\times).
\]

For a character \(\psi\), the operator defining \(P_H\) acts on its character space by the scalar

\[
\prod_{\ell\mid n}
\left(1-\psi(h)^{n/\ell}\right).
\]

This scalar is nonzero exactly when \(\psi|_H\) is faithful. Indeed, if the order \(m\) of \(\psi(h)\) properly divides \(n\), then for a prime \(\ell\) with \(v_\ell(m)<v_\ell(n)\) one has \(m\mid n/\ell\). Conversely, if its order is \(n\), no factor vanishes.

The image of a homomorphism of abelian varieties on the rational geometric \(p\)-adic Tate module is the Tate module of its image abelian subvariety. One may check this after dividing the homomorphism by its connected kernel and using the resulting isogeny; an isogeny becomes an isomorphism on rational \(p\)-adic Tate modules. Thus the hypothesis is precisely

\[
\mathcal T_{W,\psi}=0
\quad\text{whenever }\psi|_H\text{ is faithful}.
\tag{AT.1}
\]

No inference from a merely nonzero Frobenius kernel is made here.

## 3. Extending one faithful character

Choose a faithful character \(\theta:H\to\overline{\mathbf Q}_p^\times\). It extends to a character \(\chi:A\to\overline{\mathbf Q}_p^\times\).

For completeness, extension can be proved one cyclic enlargement at a time. If a character is defined on a subgroup \(B\subset A\), choose \(a\in A\), and let \(r\) be the order of \(a+B\) in \(A/B\). Choose a root \(z\) with \(z^r=\theta(ra)\). Defining the new character on \(B+\langle a\rangle\) by \(\theta(b)z^j\) is well-defined: an equality \(b+ja=b'+j'a\) makes \(j-j'\) divisible by \(r\), and the chosen root relation supplies exactly the needed equality. Repeating finitely often extends to \(A\). Since \(A\) is finite, the resulting image is finite.

Let \(N\) be the order of \(\chi\), let \(K=\ker\chi\), and put \(D=W/K\). Then \(A/K\) is cyclic of order \(N\), so \(D\to C\) is the required type of connected cyclic étale cover. Since the restriction of \(\chi\) has order \(n\), one has \(n\mid N\).

For every \(u\in(\mathbf Z/N)^\times\), the restriction

\[
(\chi^u)|_H=\theta^u
\]

is faithful, because \(n\mid N\) implies \(\gcd(u,n)=1\). Equation (AT.1) therefore gives

\[
\mathcal T_{W,\chi^u}=0
\quad\text{for every }u\in(\mathbf Z/N)^\times.
\tag{AT.2}
\]

## 4. Passing to the cyclic quotient

Let \(q:W\to D\) be the quotient by \(K\). Pullback and norm satisfy

\[
q_*q^*=[|K|],\qquad
q^*q_*=\sum_{\gamma\in K}\gamma^*.
\]

Because \(|K|\) is prime to \(p\), these identities identify \(T_p(J_D)\) with \(T_p(J_W)^K\), already integrally; rational coefficients would suffice. Explicitly, for an invariant Tate vector \(v\), one has

\[
v=q^*\bigl(|K|^{-1}q_*v\bigr).
\]

The characters of \(A\) trivial on \(K\) are exactly the powers of \(\chi\). Among them, the faithful characters of \(A/K\) are exactly \(\chi^u\) for \(u\in(\mathbf Z/N)^\times\). Their Tate spaces vanish by (AT.2). Hence the primitive conductor-\(N\) factor of \(J_D\) has \(p\)-rank zero.

Dualizing conventions may replace character indices by their inverses; faithfulness and the set of primitive powers are unchanged.

This proves the descent assertion. The reverse existence implication is immediate by taking \(W=D\), \(A=H\), and \(V=C\).

## 5. The exact consequence for an abelian base-change strategy

For a genus-two curve in characteristic two, A.C2.5 describes each nontrivial character block of an abelian cover in terms of multiplication-by-two orbits of torsion line bundles. Passing to an intermediate base groups those original character spaces according to their restriction to the new deck subgroup. A faithful cyclic character upstairs has contributions from every original character extending it.

A single theta point on \(C\), or a single killed doubling orbit, need not kill all those contributions. If all faithful contributions actually vanish, the preceding proof produces an original cyclic quotient in which every primitive orbit vanishes. Thus intermediate bases inside an abelian total cover cannot bypass the missing primitive-orbit existence theorem.

In particular, the finite-prime-set avoidance result A.C2.14 cannot be circumvented by taking intermediate cyclic stages of an abelian cover supported on that same finite set of primes. It already excludes every possible descended cyclic cover in that class.

This is a limitation of that construction, not a counterexample to A1. It does not exclude a cyclic cover of some new order, a nonabelian normal closure, or a method not requiring a zero primitive factor.

## 6. Proof inputs and verification

The argument is elementary character theory and the pullback/norm identities for Jacobians. The geometric \(p\)-adic Tate convention and the same invariant-identification argument are stated in the integrated proof of A.C2.20, Section 6. No new external existence theorem is invoked.

The exact finite character checks in code/BC_abelian_descent_and_support_checks.py verify 31,006 extension/order/primitive-restriction assertions across ten abelian groups, including mixed prime and prime-power cases. The output is code/BC_abelian_descent_and_support_checks.json. These checks supplement, rather than replace, the proof for arbitrary finite abelian groups.

The separate audit A_nonabelian_Raynaud_gap.md records why Raynaud's opened nonordinary-cover theorem does not itself provide a sparse group-algebra annihilator or a zero primitive cyclic factor. That audit distinguishes a rigorous algebraic obstruction to the proposed inference from an unproved assertion about actual curve realizations.
