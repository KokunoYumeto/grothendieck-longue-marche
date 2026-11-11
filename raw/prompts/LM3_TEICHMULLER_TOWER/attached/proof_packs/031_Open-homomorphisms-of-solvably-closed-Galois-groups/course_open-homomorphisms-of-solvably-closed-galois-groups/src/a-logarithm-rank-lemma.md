# A logarithm rank lemma

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson shows that an additive \(\ell\)-adic character of the absolute Galois group of a number field is determined by its values at Frobenius elements of infinitely many primes of degree one. Through class field theory, this comes down to one statement about \(\ell\)-adic logarithms of algebraic numbers: logarithms of enough points of a torus whose coordinates are multiplicatively independent span the whole space. This lesson proves that statement with an interpolation determinant: a determinant of values of exponential functions that is an algebraic integer, very small \(\ell\)-adically, and not too large at the archimedean places, which the product formula forbids. The zero estimate that makes the determinant nonzero is the component bound of [Counting irreducible components](counting-irreducible-components.md). The statement is a special case of the \(\ell\)-adic rank theorem of Waldschmidt and Masser, treated in [Dasgupta 2023, Section 5]; the determinant method is Laurent's [Laurent 1991].

- \(\ell\)-adic logarithms and exponentials (Section 1).
- The statement (Section 2).
- Zariski density of cyclic subgroups (Section 3).
- The zero estimate (Section 4).
- The interpolation determinant (Section 5).

## 1. \(\ell\)-adic logarithms and exponentials

Let \(\ell\) be a prime and \(K\) a finite extension of \(\mathbb Q_\ell\), with ring of integers \(\mathcal O_K\), maximal ideal \(\mathfrak m_K\), and absolute value normalized by \(|\ell|=\ell^{-1}\). The logarithm series \(\log(1+x)\) converges on the principal units \(U^1=1+\mathfrak m_K\), and the exponential series converges for \(|z|<\ell^{-1/(\ell-1)}\); on a sufficiently deep subgroup \(U^{r_0}=1+\mathfrak m_K^{r_0}\) and the corresponding ideal \(\mathfrak m_K^{r_0}\) they are inverse isomorphisms of topological groups (Proposition 2.1 of [The multiplicative group of a local field](course:NT-LOC/NT-LOC-11)). Every unit is a root of unity of order prime to \(\ell\) times a principal unit, and we define
\[
\log\colon\mathcal O_K^\times\longrightarrow K
\]
as the logarithm of the principal-unit factor; this is the restriction of the homomorphism \(\operatorname{Log}_K\) of Proposition 5.1 of that lesson. It is a continuous homomorphism, and its kernel is the group of roots of unity in \(K\): if \(\log u=0\), then \(u^{N}\in U^{r_0}\) for a suitable \(N\ge1\), since \(\mathcal O_K^\times/U^{r_0}\) is finite, and \(\log u^N=0\) forces \(u^N=1\) by injectivity on \(U^{r_0}\). Logarithms of points of \((\mathcal O_K^\times)^n\) are taken coordinatewise.

**Lemma 1.1.** For integers \(k\ge0\), \(|k!|^{-1}\le\ell^{k/(\ell-1)}\).

*Proof.* Legendre's formula gives \(v_\ell(k!)=\sum_{i\ge1}\lfloor k/\ell^i\rfloor\), and \(\sum_{i\ge1}\lfloor k/\ell^i\rfloor\le\sum_{i\ge1}k/\ell^i=k/(\ell-1)\). \(\square\)

## 2. The statement

Numbers \(c_1,\ldots,c_n\) in a field are *multiplicatively independent modulo roots of unity* if \(\prod_jc_j^{\gamma_j}\) is a root of unity only for \(\gamma=0\in\mathbb Z^n\). For points \(u_1,\ldots,u_m\in(E^\times)^n\) and \(a\in\mathbb Z^m\) write \(u^a=\prod_iu_i^{a_i}\), coordinatewise.

**Theorem 2.1** (logarithm rank; [OpenAI-UC, Lemma 3.1]). Let \(n,m\ge1\), let \(E\) be a number field contained in a finite extension \(K/\mathbb Q_\ell\), and let
\[
\begin{gathered}
u_i=(u_{i1},\ldots,u_{in})\in(E^\times)^n,\\
1\le i\le m,
\end{gathered}
\]
have coordinates that are algebraic integers and units of \(K\). Suppose that for every \(a\in\mathbb Z^m\setminus\{0\}\) the coordinates of \(u^a\) are multiplicatively independent modulo roots of unity. If \(m>n(n-1)\), then
\[
\operatorname{span}_K\{\log u_1,\ldots,\log u_m\}=K^n .
\]

The hypothesis concerns every nonzero \(a\), not only the points \(u_i\) themselves; for \(n=1\) it says that \(u_{11},\ldots,u_{m1}\) are multiplicatively independent modulo roots of unity (Exercise 7.2). For \(n=2\) and \(m=3\) the theorem is an \(\ell\)-adic form of the six exponentials theorem.

## 3. Zariski density of cyclic subgroups

Let \(\overline E\) be an algebraic closure of \(E\). We use the Zariski topology of the torus \(\mathbb G_m^n(\overline E)\) as in Section 1 of [Counting irreducible components](counting-irreducible-components.md).

**Lemma 3.1.** Let \(c\in(\overline E^\times)^n\) have coordinates multiplicatively independent modulo roots of unity. Then \(\{c^t:t\ge0\}\) is Zariski dense in \(\mathbb G_m^n(\overline E)\). Consequently, if \(V\subseteq\mathbb G_m^n(\overline E)\) is closed, nonempty and satisfies \(cV\subseteq V\), then \(V=\mathbb G_m^n(\overline E)\).

*Proof.* Let \(Q=\sum_{\alpha\in\mathcal A}q_\alpha x^\alpha\) be a polynomial, with \(\mathcal A\subset\mathbb Z_{\ge0}^n\) finite, vanishing at all \(c^t\). The numbers \(\lambda_\alpha=c^\alpha\) are pairwise distinct: \(c^\alpha=c^\beta\) means \(c^{\alpha-\beta}=1\), so \(\alpha=\beta\). The equations \(\sum_\alpha q_\alpha\lambda_\alpha^t=0\) for \(0\le t<|\mathcal A|\) have an invertible Vandermonde matrix, so \(Q=0\). A closed set containing all \(c^t\) is cut out by polynomials vanishing at all \(c^t\), hence by \(0\). For the second claim, take \(x\in V\). Then \(c^tx\in V\) for all \(t\ge0\), and multiplication by \(x\) is a homeomorphism of the torus, so \(V\) contains the closure \(x\cdot\mathbb G_m^n=\mathbb G_m^n\). \(\square\)

## 4. The zero estimate

Fix \(n,m,E,K\) and \(u_1,\ldots,u_m\) as in Theorem 2.1. For integers \(D,S\ge1\) let \(\mathcal M_{D,S}\) be the matrix with rows indexed by \(\alpha\in\{0,\ldots,D\}^n\), columns indexed by \(a\in\{0,\ldots,nS\}^m\), and entries
\[
(u^a)^\alpha=\prod_{j=1}^n\Bigl(\prod_{i=1}^mu_{ij}^{a_i}\Bigr)^{\alpha_j}\in E .
\]

**Proposition 4.1.** If \((S+1)^m>(nD)^n\), then \(\mathcal M_{D,S}\) has rank \((D+1)^n\), the number of its rows.

*Proof.* Otherwise the rows are linearly dependent over \(E\): there is a nonzero polynomial \(P=\sum_\alpha p_\alpha x^\alpha\) of degree at most \(D\) in each variable with \(P(u^a)=0\) for all \(a\in\{0,\ldots,nS\}^m\). For \(0\le j\le n\) put
\[
\begin{aligned}
Z_j=\{&x\in\mathbb G_m^n(\overline E):P(u^ax)=0\\
&\text{for all }a\in\{0,\ldots,jS\}^m\}.
\end{aligned}
\]
Each \(x\mapsto P(u^ax)\) is a polynomial of total degree at most \(nD\), so \(Z_j\) is closed, and \(Z_0\supseteq Z_1\supseteq\cdots\supseteq Z_n\ni1\). Since \(P\ne0\) and the torus is irreducible of dimension \(n\), \(\dim Z_0\le n-1\). The \(n+1\) dimensions \(\dim Z_0\ge\cdots\ge\dim Z_n\) lie in \(\{0,\ldots,n-1\}\), so \(\dim Z_j=\dim Z_{j+1}=:d\) for some \(j<n\).

Let \(V\) be an irreducible component of \(Z_{j+1}\) of dimension \(d\), and let \(b\in\{0,\ldots,S\}^m\). For \(x\in V\) and \(a\in\{0,\ldots,jS\}^m\), we have \(a+b\in\{0,\ldots,(j+1)S\}^m\), so \(P(u^au^bx)=P(u^{a+b}x)=0\). Thus \(u^bV\subseteq Z_j\). Translation by \(u^b\) is a homeomorphism of the torus, so \(u^bV\) is irreducible, closed and of dimension \(d\). It lies in a component \(C\) of \(Z_j\), of dimension at most \(d\); a proper closed subset of \(C\) would have smaller dimension, so \(u^bV=C\) is a component of \(Z_j\).

These \((S+1)^m\) translates are distinct. If \(u^bV=u^{b'}V\) with \(b\ne b'\), then \(c=u^{b-b'}\) satisfies \(cV=V\), and the coordinates of \(c\) are multiplicatively independent modulo roots of unity by hypothesis. Lemma 3.1 would give \(V=\mathbb G_m^n\), contrary to \(V\subseteq Z_0\). So \(Z_j\) has at least \((S+1)^m>(nD)^n\) irreducible components, while Theorem 5.2 of the counting lesson, applied over \(\overline E\) with \(\delta=nD\), allows at most \((nD)^n\). \(\square\)

## 5. The interpolation determinant

*Proof of Theorem 2.1.* Suppose that the logarithms span a subspace of dimension \(r<n\).

*The case \(r=0\).* Then \(\log u_{1j}=0\) for all \(j\), so every coordinate of \(u_1=u^{e_1}\) is a root of unity, contrary to the hypothesis with \(a=e_1\). Hence \(1\le r<n\).

*Normalization.* Replacing every \(u_i\) by \(u_i^N\) for a common integer \(N\ge1\) preserves the hypotheses, since \((u^N)^a=u^{Na}\) and \(Na\ne0\), and does not change the span of the logarithms. Choose \(N\) so that every coordinate lies in \(U^{r_0}\), where exponential and logarithm are inverse. The \(\mathcal O_K\)-module generated by \(\log u_1,\ldots,\log u_m\) is finitely generated and torsion-free over the principal ideal domain \(\mathcal O_K\), hence free, of rank \(r\) since it spans an \(r\)-dimensional space; choose a basis \(b_1,\ldots,b_r\in K^n\). A further common power \(\ell^s\) multiplies the logarithms and the basis by \(\ell^s\), so we may assume that
\[
\begin{gathered}
\rho=\max_{t,j}|b_{t,j}|\quad\text{satisfies}\\
\eta=\rho\,\ell^{1/(\ell-1)}<1 .
\end{gathered}
\]
Then \(\log u_i=\sum_{t=1}^rz_{i,t}b_t\) with \(z_i=(z_{i,1},\ldots,z_{i,r})\in\mathcal O_K^r\). From now on the points, \(E\), \(K\), the basis and \(\eta\) are fixed.

*Exponential functions.* For \(\alpha\in\mathbb Z_{\ge0}^n\) and \(z\in\mathcal O_K^r\) put
\[
\begin{gathered}
f_\alpha(z)=\exp\Bigl(\sum_{t=1}^r\beta_{\alpha,t}z_t\Bigr),\\
\beta_{\alpha,t}=\sum_{j=1}^n\alpha_jb_{t,j}.
\end{gathered}
\]
The argument has absolute value at most \(\rho<\ell^{-1/(\ell-1)}\), so the series converges. Expanding, \(f_\alpha(z)=\sum_{\nu\in\mathbb Z_{\ge0}^r}c_{\alpha,\nu}z^\nu\) with \(c_{\alpha,\nu}=\beta_\alpha^\nu/\nu!\), and Lemma 1.1 gives
\[
\begin{gathered}
|c_{\alpha,\nu}|\le\eta^{|\nu|},\\
|\nu|=\nu_1+\cdots+\nu_r,
\end{gathered}\tag{5.1}
\]
uniformly in \(\alpha\), since integers have absolute value at most \(1\). For \(a\in\mathbb Z_{\ge0}^m\) put \(z(a)=\sum_ia_iz_i\in\mathcal O_K^r\). Then \(\sum_t\beta_{\alpha,t}z(a)_t=\sum_j\alpha_j\log\bigl((u^a)_j\bigr)\), which lies in \(\mathfrak m_K^{r_0}\), and since \(\exp\) is a homomorphism inverse to \(\log\) there,
\[
f_\alpha(z(a))=(u^a)^\alpha .
\]

*The determinant.* Let \(D\ge1\), \(A=(D+1)^n\), and \(S=\lceil(nD)^{n/m}\rceil\), so that \((S+1)^m>(nD)^n\) and \(S\le(nD)^{n/m}+1\). By Proposition 4.1 choose distinct columns \(a^{(1)},\ldots,a^{(A)}\) of \(\mathcal M_{D,S}\) with
\[
\Delta_D=\det\bigl((u^{a^{(k)}})^\alpha\bigr)_{\alpha,k}\ne0 .
\]
It is an algebraic integer of \(E\), since its entries are.

*\(\ell\)-adic smallness.* Write the rows as \(f_\alpha(z(a^{(k)}))\). Truncate each series at \(|\nu|\le T\). By multilinearity, the truncated determinant is a finite sum over families \((\nu_\alpha)_\alpha\) of terms \(\prod_\alpha c_{\alpha,\nu_\alpha}\cdot\det\bigl(z(a^{(k)})^{\nu_\alpha}\bigr)_{\alpha,k}\). A family with \(\nu_\alpha=\nu_{\alpha'}\) for some \(\alpha\ne\alpha'\) gives a determinant with two equal rows. For a family of \(A\) distinct multi-indices, the second factor has absolute value at most \(1\), and by (5.1) the first is at most \(\eta^{\sum_\alpha|\nu_\alpha|}\). At most \(\binom{T'+r}r\le(T'+1)^r\) multi-indices have \(|\nu|\le T'\). With \(T'+1=\lfloor(A/2)^{1/r}\rfloor\), at least \(A/2\) of the \(\nu_\alpha\) have \(|\nu_\alpha|\ge\lfloor(A/2)^{1/r}\rfloor\), so for \(A\) large
\[
\begin{aligned}
\sum_\alpha|\nu_\alpha|&\ge\tfrac A2\bigl((A/2)^{1/r}-1\bigr)\\
&\ge c_rA^{1+1/r},\qquad c_r=2^{-2-1/r}.
\end{aligned}
\]
By the ultrametric inequality the truncated determinant has absolute value at most \(\eta^{c_rA^{1+1/r}}\). As \(T\to\infty\) the truncated series converge to the entries, and the determinant is continuous, so
\[
\begin{gathered}
\log|\Delta_D|\le-c\,A^{1+1/r},\\
c=c_r\log(1/\eta)>0,
\end{gathered}\tag{5.2}
\]
for all large \(D\). Here \(\log|\cdot|\) is the real logarithm of the absolute value of \(K\).

*Archimedean size.* Let \(H\ge1\) bound \(|\tau(u_{ij})|\) for all embeddings \(\tau\colon E\to\mathbb C\) and all \(i,j\). An entry \((u^a)^\alpha\) is a product of at most \(\sum_ia_i\sum_j\alpha_j\le m\,nS\cdot nD\) coordinates, so \(|\tau((u^a)^\alpha)|\le H^{mn^2DS}\). Expanding the determinant into \(A!\le A^A\) products,
\[
\begin{aligned}
\log|\tau(\Delta_D)|&\le C'ADS\\
&\quad+A\log A,\\
C'&=mn^2\log H,
\end{aligned}\tag{5.3}
\]
with \(C'\) independent of \(D\).

*The product formula.* Let \(\lambda\) be the place of \(E\) induced by \(E\subset K\). By the product formula (Theorem 5.2 of [Places of number fields in extensions and the product formula](course:NT-LOC/NT-LOC-05)), written with the absolute values extending the usual ones on \(\mathbb Q\) and with each complex place counted through its two embeddings,
\[
\begin{aligned}
0={}&\sum_{\tau\colon E\to\mathbb C}\log|\tau(\Delta_D)|\\
&+\sum_{v\ \mathrm{finite}}[E_v:\mathbb Q_{p_v}]\log|\Delta_D|_v,
\end{aligned}
\]
where \(p_v\) is the rational prime below \(v\). Every finite term is at most \(0\) because \(\Delta_D\) is an algebraic integer, and the term at \(\lambda\) is \([E_\lambda:\mathbb Q_\ell]\log|\Delta_D|\). With (5.2) and (5.3),
\[
\begin{gathered}
c\,[E_\lambda:\mathbb Q_\ell]\,A^{1+1/r}\\
\le[E:\mathbb Q]\bigl(C'ADS+A\log A\bigr).
\end{gathered}
\]
As \(D\to\infty\), the left side has order \(D^{n+n/r}\) and the right side is \(O(D^{n+1+n/m}+D^n\log D)\). Since \(r\le n-1\) and \(m>n(n-1)\),
\[
\frac nr\ge\frac n{n-1}=1+\frac1{n-1}>1+\frac nm ,
\]
so the inequality fails for large \(D\). This contradiction proves \(r=n\). \(\square\)

## 6. Remarks

The proof uses the hypothesis on \(u^a\) only through Lemma 3.1 in the zero estimate, and in the case \(r=0\). The exponent \(n\) in the component bound \((nD)^n\) produces the threshold \(m>n(n-1)\): the zero estimate needs \(S\) of order \(D^{n/m}\), and the comparison of \(D^{n+n/r}\) with \(D^{n+1+n/m}\) is decided by \(n/(n-1)\) against \(1+n/m\). Theorem 2.1 is a special case of the \(\ell\)-adic rank theorem of Waldschmidt and Masser for matrices of logarithms of algebraic numbers ([Dasgupta 2023, Section 5]); the threshold \(m>n(n-1)\) is exactly the condition that its rank bound \(mn/(m+n)\) exceed \(n-1\).

## 7. Exercises

**7.1.** Let \(n=2\) and \(u_i=(x_i,x_i)\) with \(x_i\in E\) units of \(K\) that are not roots of unity. Show that the logarithms span a line, and identify the hypothesis of Theorem 2.1 that fails.

**7.2.** Prove Theorem 2.1 for \(n=1\) directly.

**7.3.** Show that the minimum of \(\sum_{k=1}^A|\nu_k|\) over \(A\) distinct \(\nu_k\in\mathbb Z_{\ge0}\) is \(A(A-1)/2\), and compare with the bound \(c_1A^2\) of Section 5.

**7.4.** Let \(m=3\), \(n=2\). Show that \(m>n(n-1)\), and state the conclusion of Theorem 2.1 as a statement about the rank of a \(3\times2\) matrix of \(\ell\)-adic logarithms.

**7.5.** Let \(\ell\) be odd, \(k\ge1\), and \(u\in1+\ell^k\mathbb Z_\ell\) with \(u\notin1+\ell^{k+1}\mathbb Z_\ell\). Show that \(v_\ell(\log u)=k\), and deduce that replacing \(u\) by \(u^{\ell^s}\) multiplies \(|\log u|\) by \(\ell^{-s}\).

## 8. Solutions

**7.1.** \(\log u_i=(\log x_i,\log x_i)\) lies on the diagonal line. The coordinates of \(u^a\) are equal, so they are not multiplicatively independent: \(c_1c_2^{-1}=1\).

**7.2.** For \(n=1\) the condition \(m>0\) always holds. The span is \(K\) unless every \(\log u_{i1}=0\), that is, unless every \(u_{i1}\) is a root of unity; the hypothesis with \(a=e_1\) excludes this for \(u_{11}\).

**7.3.** The smallest possible values are \(0,1,\ldots,A-1\), with sum \(A(A-1)/2\). The bound of Section 5 with \(r=1\) is \(c_1A^2=A^2/8\), smaller by a constant factor, as it must be since it is derived from a cruder count.

**7.4.** \(3>2\). The \(3\times2\) matrix with rows \(\log u_1,\log u_2,\log u_3\) has rank \(2\): its rows span \(K^2\).

**7.5.** Write \(u=1+x\) with \(v_\ell(x)=k\). For \(j\ge2\), \(v_\ell(x^j/j)=jk-v_\ell(j)\), and \(v_\ell(j)\le\log_3j<j-1\le(j-1)k\), so \(v_\ell(x^j/j)>k\). The first term of \(\log(1+x)=x-x^2/2+\cdots\) therefore determines the valuation: \(v_\ell(\log u)=k\). Since \(\log\) is a homomorphism, \(\log u^{\ell^s}=\ell^s\log u\), whose absolute value is \(\ell^{-s}|\log u|\).

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Section 3.1 (Lemma 3.1). https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
- [Laurent 1991] M. Laurent, *Sur quelques résultats récents de transcendance*, Astérisque 198–200 (1991), 209–230. http://www.numdam.org/item/AST_1991__198-199-200__209_0/
- [Dasgupta 2023] S. Dasgupta, *Ranks of matrices of logarithms of algebraic numbers I: the theorems of Baker and Waldschmidt–Masser*, Essential Number Theory 2 (2023), 93–138, Section 5. https://arxiv.org/abs/2303.02037
