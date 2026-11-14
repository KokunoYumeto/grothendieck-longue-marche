# D.29 candidate: reciprocity tests do not imply restricted-product admissibility

**Status:** independently approved by root and integrated as D.29 in `sections/D_unrestricted_reciprocity_extension.tex`. The original proof is retained as an audit record. This is an explicitly constructed family of ordinary local points, not a section. It separates the two conditions in D.27 and does not resolve or refute any continuous section conjecture.

## Precise statement

There are elements \(A_p\in\mathbf Q_p^\times\), one for every finite rational prime, and \(A_\infty=1\), with the following properties.

1. The numbers \(x_v=2+A_v\) belong to \(U(\mathbf Q_v)\), where \(U=\mathbf P^1-\{0,1,\infty\}\). Thus the \(A_v\) are actual translated values \(x_v-2\), rather than arbitrary formal local Kummer classes.
2. For every integer \(n>1\), the tuple \((\kappa_n(A_v))_v\) does **not** belong to \(P^1(\mathbf Q,\mu_n)\). Its valuations are (1) at infinitely many primes. In particular no element of \(\widehat{\mathbf Q^\times}\) has these localizations.
3. Nevertheless, for every number field \(L\subset\overline{\mathbf Q}\), every \(n\ge1\), and every \(\chi\in H^1(L,\mathbf Z/n)\), the expression
   \[
   \sum_w\operatorname{inv}_w\bigl(\kappa_n(A_{L,w})\smile\chi_w\bigr)
   \]
   has only finitely many nonzero summands and equals zero. Here \(A_{L,w}\) is the image of \(A_p\) when \(w\mid p\), and is (1) at every archimedean place. Restricted-product failure persists over every such \(L\), at every modulus \(n>1\).
4. The exceptional rational primes in (2) have Dirichlet density zero. At each of them both original tripod coordinates \(x_p\) and \(1-x_p\) are units, although the new coordinate \(x_p-2\) has valuation (1).

The local data are compatible under restriction to finite number fields. For \(L/K\), the norm of the restricted local class is the original class raised to ([L:K]), with the norm at a place understood as the product over places above it. No stronger norm compatibility is asserted.

## Prime construction

Fix an enumeration \(p_1,p_2,\ldots\) of the rational primes in increasing order. Enumerate finite Galois extensions \(E_j/\mathbf Q\) inside a chosen algebraic closure so that every finite Galois extension eventually occurs. For an explicit numerical prefix, take
\[
 E_1=\mathbf Q,\quad E_2=\mathbf Q(i),\quad
 E_3=E_4=\mathbf Q(\zeta_{24}),\quad
 E_5=\mathbf Q(\zeta_{120}),
\]
and then enumerate the splitting fields of all monic integer polynomials. Repetitions are harmless.

Set \(P_0=M_0=q_0=1\). Given the previous data, put
\[
\begin{split}
R_j&=1+\max\{v_{p_j}(P_{j-1}+1),v_{p_j}(P_{j-1}+2)\},\\
M_j&=\operatorname{lcm}\bigl(M_{j-1},(j!)^j,p_j^{R_j}\bigr).
\end{split}
\]
Choose \(q_j\) to be the least rational prime larger than
\(\max\{2^j,q_{j-1},p_j\}\) that splits completely in
\[
 E_1\cdots E_j\,\mathbf Q(\mu_{M_j}),
\]
and set \(P_j=P_{j-1}q_j\). The field in question is a finite Galois extension of \(\mathbf Q\). Chebotarev applied to the identity conjugacy class supplies infinitely many such primes, so the recursion is defined. Only this complete-splitting case is used (Milne, 2020, Chapter V, Theorem 3.23, printed p. 164). Each prime may also be found by finite exact splitting tests, so the sequence is specified without an oracle for an infinite condition.

In particular,
\[
 q_j\equiv1\pmod {M_j},\qquad q_j>2^j,
\]
and \(q_j\) eventually splits completely in any prescribed finite Galois extension of \(\mathbf Q\).

## Actual local limits and avoidance of the old cusps

Fix a prime \(p\). Since \(M_j\) is divisible by \((j!)^j\), for every \(r\ge1\) all sufficiently late factors \(q_j\) lie in \(1+p^r\mathbf Z_p\). Products of any number of these factors remain in that subgroup. Thus the partial products are Cauchy after their finite initial factors. Exactly one factor is equal to \(p\) if \(p\in\{q_j\}\), and no factor is equal to \(p\) otherwise. Consequently they converge to a nonzero element
\[
 A_p=\lim_{N\to\infty}P_N\in\mathbf Q_p^\times,
 \qquad
 v_p(A_p)=\begin{cases}1,&p=q_j\text{ for some }j,\\0,&\text{otherwise.}\end{cases}
\]
No real convergence of the positive products \(P_N\) is claimed. We set \(A_\infty=1\); the positive \(P_N\) have this same Kummer class at the real place for every \(n\).

It remains to check that translating by (2) never produces (0) or (1). Write \(p=p_j\). Because \(M_j\mid M_i\) for every \(i\ge j\), every \(q_i\) with \(i\ge j\) is (1) modulo \(p^{R_j}\). Hence
\[
 A_p/P_{j-1}\in1+p^{R_j}\mathbf Z_p.
\]
For \(c=1,2\),
\[
 v_p(A_p-P_{j-1})\ge v_p(P_{j-1})+R_j
 >v_p(P_{j-1}+c).
\]
The strong triangle inequality gives
\(v_p(A_p+c)=v_p(P_{j-1}+c)<\infty\).
In particular \(A_p\ne-1,-2\). Thus \(x_p=2+A_p\) is a finite value different from (0,1,2); \(x_\infty=3\) has the same property. These are ordinary local points of the new-punctured curve as well as of the original tripod.

## Restricted-product failure

For every \(n>1\), at every sufficiently large \(q_j\nmid n\) the Kummer class \(\kappa_n(A_{q_j})\) has valuation \(1\bmod n\). Over a local field of residue characteristic prime to \(n\), an unramified Kummer class has valuation zero modulo \(n\). Thus the tuple is ramified at infinitely many places and is outside \(P^1(\mathbf Q,\mu_n)\).

Any rational \(a\in\mathbf Q^\times\) has nonzero valuation at only finitely many primes. Its squareclass therefore cannot agree with all the displayed local squareclasses. Since a global completed class has a rational squareclass as its modulus-two component, no \(A\in\widehat{\mathbf Q^\times}\) can have these localizations.

For a fixed number field \(L\), the Galois closure of \(L/\mathbf Q\) occurs among the \(E_j\). Every sufficiently late \(q_j\) splits completely in \(L\). At every \(w\mid q_j\), the element \(A_{L,w}\) consequently has valuation (1). The same argument excludes membership in \(P^1(L,\mu_n)\) for every \(n>1\), and excludes any global completed class over \(L\).

The inequality \(q_j>2^j\) gives \(\sum_jq_j^{-1}<\infty\), hence Dirichlet density zero for the exceptional prime set. At \(q=q_j>2\) one has \(A_q\in q\mathbf Z_q^\times\), so
\[
 x_q\equiv2\pmod q,\qquad 1-x_q\equiv-1\pmod q.
\]
Both original coordinates are units at these primes. This does not claim that the two original coordinate tuples are global completed Kummer classes, nor does it claim that the family is section-induced.

## Every finite-character reciprocity sum still vanishes

Fix \(L,n,\chi\) as in the statement. The kernel of the continuous character \(\chi:G_L\to\mathbf Z/n\) cuts out a finite cyclic extension \(K/L\). Let \(N/\mathbf Q\) be a finite Galois extension containing \(K\) and all its conjugates. Choose \(J\) such that every \(q_j\) for \(j\ge J\) splits completely in \(N\).

For every \(w\mid q_j\) with \(j\ge J\), the local character \(\chi_w\) is zero. Let \(T\) contain all archimedean places of \(L\), all finite places at which \(\chi\) ramifies, and all places above the finitely many \(q_j\) with \(j<J\). If \(w\notin T\), either it lies over a tail prime \(q_j\), where \(\chi_w=0\), or \(A_{L,w}\) is a unit and \(\chi_w\) is unramified. In the latter case the cup invariant is also zero: the local Artin map for an unramified extension evaluates an element by its valuation, and therefore annihilates units (Milne, 2020, Chapter III, Proposition 3.6 and Lemma 3.7, printed pp. 109–110). This proves that the sum has finite support. The same assertion outside \(T\) holds for every finite product \(P_r\).

For each finite \(w\in T\), the elements \(P_r\in L_w^\times\) converge to \(A_{L,w}\). The subgroup \((L_w^\times)^n\) is open. For example Hensel's lemma applied to \(Z^n-u\) at \(Z=1\) shows that a sufficiently deep principal unit \(u\) is an \(n\)-th power: it suffices that \(v_w(u-1)>2v_w(n)\). There are only finitely many such \(w\), so for one sufficiently large \(r\),
\[
 \kappa_n(P_r)=\kappa_n(A_{L,w})\quad\text{for all finite }w\in T.
\]
At real places both \(P_r>0\) and \(A_{L,w}=1\) have trivial Kummer class, including when \(n\) is even; at complex places the class is always trivial. The entire desired sum therefore equals
\[
 \sum_w\operatorname{inv}_w
       \bigl(\kappa_n(P_r)\smile\chi_w\bigr)=0.
\]
The equality to zero is global Brauer reciprocity for the one global class \(\kappa_n(P_r)\smile\chi\in\operatorname{Br}(L)[n]\), including the real invariants (Milne, 2020, Chapter VIII, Theorem 4.2, printed p. 241).

The finite set \(T\) depends on the character. Nothing in this argument gives a fixed finite set outside which \(\kappa_n(A_{L,w})\) itself is unramified. That uniform assertion is false, as the valuation computation proves.

## Restriction and norm bookkeeping

For \(L/K\) and \(w\mid v\), the element \(A_{L,w}\) is the image of the same rational-local limit defining \(A_{K,v}\). Restriction compatibility is literal. As an element of \(K_v\) embedded into each \(L_w\), its local norm is \(A_{K,v}^{[L_w:K_v]}\). Multiplying over \(w\mid v\) gives \(A_{K,v}^{[L:K]}\). This identity survives Kummer completion and also holds at the archimedean places where the chosen element is (1). It is the ordinary norm-of-restriction identity, not a new global norm-compatible system.

## Exact logical consequence for D.27

Poitou–Tate exactness applies to the restricted product. A tuple outside that domain cannot be inserted into its kernel simply because every individually meaningful finite-character sum is zero. This construction shows that even all finite constant extensions, all moduli, locally finite support for each test, and the natural restriction/norm-of-restriction identities do not remove the domain condition.

The family is not claimed to satisfy the original global \(t\) and (1-t) Kummer conditions of a tripod section, or the conditions on all its accessible finite étale neighbourhoods. It consequently does not refute an inference that genuinely uses those additional constraints. It proves that a route using only characterwise reciprocity and finite-base functoriality cannot establish new-puncture admissibility. D.26's density-one statement also cannot be promoted to this uniform divisibility condition merely by observing that the exceptional set here is sparse.

## Finite reproducibility certificate

The canonical executable `code/D_unrestricted_reciprocity_checks.py` constructs the first five primes by exact trial division, checks the prescribed cusp-avoidance congruences, and verifies 45 exact quadratic Hilbert reciprocity products for the finite rational products. Its JSON output is `code/D_unrestricted_reciprocity_checks.json`. The old adjacent audit paths are retained with explicit supersession; the audit script forwards to the canonical program.

| \(j\) | \(p_j\) | \(R_j\) | \(M_j\) | \(q_j\) | \((q_j-1)/M_j\) |
|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 4 | 5 | 1 |
| 2 | 3 | 2 | 36 | 37 | 1 |
| 3 | 5 | 1 | 1080 | 2161 | 2 |
| 4 | 7 | 1 | 11612160 | 58060801 | 5 |
| 5 | 11 | 1 | 1916006400000 | 17244057600001 | 9 |

The numerical checks certify this prefix and the listed finite identities. The proofs above, rather than any finite sample, establish the infinite local limits and all-character assertions.

## Primary source actually opened

Milne, J. S. (2020). *Class field theory* (Version 4.03, August 6). Author's course notes. https://www.jmilne.org/math/CourseNotes/CFT.pdf

Opened Chapters III.3.6–3.7 (printed pp. 109–110), V.3.23 (printed p. 164), and VIII.4.2 (printed p. 241). The existing bibliography key is `D_MilneCFT2020`. The construction and its separation of logical conditions are derived here; the source supplies only the explicitly identified local and global class-field statements and complete-splitting existence.
