# Normalizer extension and Frobenius generation

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

From now on \(F\) is a number field and \(\alpha_0\colon G_F\to P\) is a continuous homomorphism with open image, where \(P=\operatorname{Gal}(\mathbb Q^s/\mathbb Q)\) as in [Solvably closed fields and Uchida's conjecture](solvably-closed-fields-and-uchidas-conjecture.md). The goal of this lesson and the next two is to show that \(\alpha_0\) is ordinary restriction followed by a conjugation in \(P\). This lesson first extends an open part of \(\alpha_0\) to a larger subgroup of \(G_{\mathbb Q}\) in a canonical way. For the extended map \(\beta\) it proves two properties: \(\beta\) is surjective, and \(\beta\) preserves the logarithms of the \(\ell\)-adic cyclotomic characters for infinitely many primes \(\ell\). The key step shows that images of local Frobenius elements generate prescribed cyclic subgroups of suitable finite quotients of \(P\); additive characters from [Additive characters and Frobenius detection](additive-characters-and-frobenius-detection.md) detect a failure of generation.

- The normalizer extension (Section 1).
- Quotient amplification (Section 2).
- Generation by Frobenius images (Section 3).
- Surjectivity and cyclotomic logarithms (Section 4).

Throughout, (U1) and (U2) are the results of Uchida stated in Section 3 of the first lesson, and \(\mathcal G=G_{\mathbb Q}\).

## 1. The normalizer extension

Choose an open normal subgroup \(U\) of \(\mathcal G\) contained in \(G_F\), and put
\[
\begin{gathered}
A=\alpha_0(U),\qquad N=\ker(\alpha_0|_U),\\
T=N_{\mathcal G}(N),
\end{gathered}
\]
the normalizer of \(N\) in \(\mathcal G\). A continuous surjection of profinite groups maps open subgroups to closed subgroups of finite index, so \(A\), of finite index in the open subgroup \(\alpha_0(G_F)\), is open in \(P\). The normalizer \(T\) contains \(U\), so it is open; its fixed field \(k\) is a number field, and \(T=G_k\).

**Lemma 1.1** (extension to the normalizer; [OpenAI-UC, Lemma 4.1]). There is a unique continuous homomorphism \(\beta\colon T\to P\) with \(\beta|_U=\alpha_0|_U\). It is open.

*Proof.* \(\alpha_0\) induces a continuous bijection \(U/N\to A\) of compact groups, hence an isomorphism of topological groups. For \(t\in T\), conjugation by \(t\) preserves \(U\), which is normal in \(\mathcal G\), and \(N\); it induces the continuous automorphism
\[
\theta_t\colon A\to A,\qquad \theta_t(\alpha_0(u))=\alpha_0(tut^{-1}).
\]
The group \(A\) is \(P_{M_A}\) for the number field \(M_A=(\mathbb Q^s)^A\). Apply (U1) with \(E_1=E_2=\mathbb Q^s\), \(F_1=F_2=M_A\) and \(\theta=\theta_t\): there is a unique field automorphism \(j_t\) of \(\mathbb Q^s\) with \(h\circ j_t=j_t\circ\theta_t(h)\) for \(h\in A\). Every field automorphism of \(\mathbb Q^s\) fixes \(\mathbb Q\), so \(j_t\in P\), and \(\beta(t)=j_t^{-1}\) satisfies
\[
\beta(t)\,h\,\beta(t)^{-1}=\theta_t(h)\qquad(h\in A).
\]
An element of \(P\) with this property is unique: two such differ by an element commuting with every element of the open subgroup \(A\), which is \(1\) by Lemma 3.1 of the first lesson. Uniqueness shows that \(\beta\) is a homomorphism, since \(\beta(t)\beta(t')\) induces \(\theta_t\theta_{t'}=\theta_{tt'}\), and that \(\beta(u)=\alpha_0(u)\) for \(u\in U\), since \(\alpha_0(u)\) induces \(\theta_u\). It also shows that every homomorphism \(\beta'\) extending \(\alpha_0|_U\) equals \(\beta\): \(\beta'(t)\alpha_0(u)\beta'(t)^{-1}=\beta'(tut^{-1})\), which is \(\theta_t(\alpha_0(u))\). A homomorphism continuous on an open subgroup is continuous, and \(\beta(T)\supseteq A\) is open. \(\square\)

We keep \(U,A,N,T,k\) and \(\beta\) fixed. Let \(N_1,\ldots,N_r\) be the conjugates \(tNt^{-1}\), \(t\in\mathcal G\), different from \(N\). There are finitely many, at most \([\mathcal G:T]\); we allow \(r=0\). Put \(H_i=\beta(N_i)\).

**Lemma 1.2.** Each \(N_i\) is a closed normal subgroup of \(U\), and each \(H_i=\alpha_0(N_i)\) is a nontrivial closed normal subgroup of \(A\).

*Proof.* Write \(N_i=tNt^{-1}\). As \(U\) is normal in \(\mathcal G\), \(N_i\subseteq U\), and \(N_i\) is normal in \(tUt^{-1}=U\). So \(H_i=\alpha_0(N_i)\) is normal in \(\alpha_0(U)=A\). If \(H_i=1\), then \(tNt^{-1}\subseteq N\), and inductively \(N\supseteq tNt^{-1}\supseteq t^2Nt^{-2}\supseteq\cdots\). Some power \(t^e\) lies in \(U\), since \(\mathcal G/U\) is finite, and \(U\) normalizes \(N\); so \(t^eNt^{-e}=N\), all inclusions in the chain are equalities, and \(t\in T\), contrary to \(N_i\ne N\). \(\square\)

## 2. Quotient amplification

For an odd prime \(\ell\) and a number field \(L\subset\mathbb Q^s\), Galois over \(\mathbb Q\) with group \(R\), the group \(P\) acts on \(\mathcal X_\ell(L)=\operatorname{Hom}(P_L,\mathbb Q_\ell)\) through \(R\), as in Section 1 of the character lesson; in particular each \(H_i\) acts through its image in \(R\).

**Lemma 2.1** (quotient amplification; [OpenAI-UC, Lemma 4.2]). Fix an odd prime \(\ell\) and a finite quotient \(R_0\) of \(P\). There is a finite Galois extension \(L/\mathbb Q\) inside \(\mathbb Q^s\), totally imaginary, such that \(R=\operatorname{Gal}(L/\mathbb Q)\) maps onto \(R_0\) and: for every \(\gamma\in R\), with \(C=\langle\gamma\rangle\), and every proper subgroup \(D\subsetneq C\), there is \(x\in\mathcal X_\ell(L)\) with
\[
\begin{gathered}
x\in\mathcal X_\ell(L)^D,\quad E_Cx=0,\\
x\notin\sum_{i=1}^r\mathcal X_\ell(L)^{H_i}.
\end{gathered}\tag{2.1}
\]

*Proof.* *A first quotient.* Choose an open normal subgroup \(V_1\) of \(P\) contained in the kernel of \(P\to R_0\), in \(A\), and in \(P_{\mathbb Q(i)}\), and not containing a chosen element \(h_i\ne1\) of \(H_i\) for each \(i\). Let \(L_1=(\mathbb Q^s)^{V_1}\), \(R_1=\operatorname{Gal}(L_1/\mathbb Q)\) and \(n=|R_1|\). Then \(R_1\) maps onto \(R_0\), \(L_1\supseteq\mathbb Q(i)\) is totally imaginary, \(P_{L_1}=V_1\subseteq A\), and every \(H_i\) has nontrivial image in \(R_1\).

*A regular Kummer extension.* Let \(m\ge1\) be an integer, chosen below. Choose \(m\) distinct rational primes \(p_1,\ldots,p_m\) splitting completely in \(L_1\), which exist by Chebotarev's theorem, and a prime \(\mathfrak p_j\) of \(L_1\) above \(p_j\); the primes above \(p_j\) are the \(n\) primes \(g\mathfrak p_j\), \(g\in R_1\). By the Chinese remainder theorem in the Dedekind domain \(\mathcal O_{L_1}\) there are \(a_j\in\mathcal O_{L_1}\) with valuation \(1\) at \(\mathfrak p_j\) and \(0\) at the other \(mn-1\) primes \(g\mathfrak p_k\). Then \(g(a_j)\) has valuation \(1\) at \(g\mathfrak p_j\) and \(0\) at the other selected primes. So a product \(\prod_{g,j}g(a_j)^{\varepsilon_{g,j}}\) with exponents \(\varepsilon_{g,j}\in\{0,1\}\), not all zero, has an odd valuation and is not a square: the \(mn\) elements \(g(a_j)\) are independent in \(L_1^\times/L_1^{\times2}\). Let \(L\) be generated over \(L_1\) by their square roots. Any \(\sigma\in\mathcal G\) maps \(\sqrt{g(a_j)}\) to a square root of \(\sigma(g(a_j))\), which is one of the \(g'(a_j)\); so \(L/\mathbb Q\) is Galois. By the Kummer correspondence (Theorem 3.3 of [Hilbert's Theorem 90 and Kummer theory](course:NT-CFT/hilberts-theorem-90-and-kummer-theory)), \(V=\operatorname{Gal}(L/L_1)\) is dual to the group generated by the classes of the \(g(a_j)\), which \(R_1\) permutes freely in \(m\) orbits; the Kummer pairing is compatible with the conjugation action, since \(R_1\) acts trivially on \(\mu_2\). So, as \(R_1\)-modules,
\[
\begin{gathered}
1\to V\to R\to R_1\to1,\\
R=\operatorname{Gal}(L/\mathbb Q),\qquad V\cong\mathbb F_2[R_1]^m,
\end{gathered}
\]
the dual of a free permutation module being again free. \(R\) is solvable, so \(L\subset\mathbb Q^s\), and \(L\) is totally imaginary. No splitting of the sequence is used.

*Sizes.* Every element of \(R\) has order at most \(2n\): its \(n\)-th power lies in \(V\), which has exponent \(2\). Let \(A_R\) and \(H_{i,R}\) be the images of \(A\) and \(H_i\) in \(R\). The image of \(P_{L_1}\subseteq A\) is \(V\), so \(V\subseteq A_R\). Choose \(h_i\in H_{i,R}\) whose image \(g_i\in R_1\) is not \(1\), of order \(d_i>1\). Since \(H_{i,R}\) is normal in \(A_R\supseteq V\), for \(v\in V\) the commutator \(h_ivh_i^{-1}v^{-1}=h_i\cdot(vh_i^{-1}v^{-1})\) lies in \(H_{i,R}\); in additive notation for \(V\) it is \((g_i-1)v\). So \((g_i-1)V\subseteq H_{i,R}\). On \(\mathbb F_2[R_1]\), \(g_i\) permutes the basis \(R_1\) in \(n/d_i\) cycles of length \(d_i\), so \(g_i-1\) has rank \(n-n/d_i\ge n/2\), and on \(V\) rank at least \(mn/2\). Hence
\[
|H_{i,R}|\ge2^{mn/2}. \tag{2.2}
\]
Let \(c\in R\) be a complex conjugation. Its image \(\bar c\in R_1\) is an involution, nontrivial because \(L_1\) is totally imaginary. For \(v\in V\), \(vcv^{-1}=((1-\bar c)v)\,c\), so the \(V\)-conjugates of \(c\) are in bijection with \((1-\bar c)V\), of size at least \(2^{mn/2}\):
\[
|c^R|\ge2^{mn/2}. \tag{2.3}
\]

*Dimensions.* Put \(\eta=2^{-mn/2}\), \(X=\mathcal X_\ell(L)\) and \(W=W_L=\operatorname{Ind}_{\langle c\rangle}^R(\operatorname{sign})\). By Proposition 5.3 of the character lesson, \(W\subseteq X\) and \(\dim X^J\le|R|/|J|\) for every subgroup \(J\subseteq R\). With (2.2),
\[
\begin{aligned}
\dim\sum_{i=1}^rX^{H_i}&\le\sum_{i=1}^r\frac{|R|}{|H_{i,R}|}\\
&\le r\eta|R|.
\end{aligned}\tag{2.4}
\]
For a subgroup \(J\), \(\dim W^J\) is the trace of the projector \(E_J\), that is, the average of \(\chi_W\) over \(J\). By Lemma 5.1(1) of the character lesson and (2.3),
\[
\begin{aligned}
&\Bigl|\dim W^J-\frac{|R|}{2|J|}\Bigr|\\
&\quad=\frac{|J\cap c^R|\,|R|}{2|J|\,|c^R|}\le\frac{\eta|R|}2 .
\end{aligned}\tag{2.5}
\]
Let \(D\subsetneq C=\langle\gamma\rangle\). The map \(E_C\colon W^D\to W^C\) is surjective, since it is the identity on \(W^C\subseteq W^D\). As \(|D|\le|C|/2\) and \(|C|\le2n\), (2.5) gives
\[
\begin{aligned}
&\dim\ker\bigl(E_C|_{W^D}\bigr)=\dim W^D-\dim W^C\\
&\quad\ge\frac{|R|}2\Bigl(\frac1{|D|}-\frac1{|C|}\Bigr)-\eta|R|\\
&\quad\ge|R|\Bigl(\frac1{4n}-\eta\Bigr).
\end{aligned}
\]
Choose \(m\) with \((r+1)2^{-mn/2}<1/(4n)\); this choice depends only on \(n\) and \(r\). Then the kernel has dimension greater than (2.4), so it contains a vector outside \(\sum_iX^{H_i}\). This vector lies in \(W^D\subseteq X^D\) and satisfies (2.1). If \(C\) is trivial, there is no proper subgroup to consider. \(\square\)

## 3. Generation by Frobenius images

**Proposition 3.1** (Frobenius generation; [OpenAI-UC, Proposition 4.3]). Fix an odd prime \(\ell\), a finite quotient \(R_0\) of \(P\), and \(\gamma_0\in R_0\). There are a finite Galois \(L/\mathbb Q\) in \(\mathbb Q^s\), with \(R=\operatorname{Gal}(L/\mathbb Q)\) mapping onto \(R_0\), and a lift \(\gamma\in R\) of \(\gamma_0\), with the following property. There are infinitely many primes \(v\) of \(k\) active at \(\ell\) for \(\beta\), over distinct rational primes \(p\ne\ell\), such that for suitable choices of primes above them:

1. the corresponding target rational prime \(q\ne\ell\) is unramified in \(L\), and the target prime of \(\mathbb Q^s\) restricts to a prime \(w'\) of \(L\) whose Frobenius in \(R\) is \(\gamma\);
2. the image in \(R\) of an arithmetic Frobenius lift at \(v\) generates \(\langle\gamma\rangle\).

*Proof.* Choose \(L\) by Lemma 2.1, any lift \(\gamma\), and put \(C=\langle\gamma\rangle\). Let \(U'\) be an open normal subgroup of \(\mathcal G\) contained in \(U\cap\beta^{-1}(P_L)\), for instance the intersection of the conjugates of this open subgroup, and let \(F'/\mathbb Q\) be the finite Galois extension with \(G_{F'}=U'\). The restriction \(\beta|_{U'}\colon G_{F'}\to P_L\) has open image, as \(U'\) has finite index in \(U\) and \(\beta(U)=A\) is open.

*Choosing primes.* By Chebotarev's density theorem (Theorem 22.4 of [The Chebotarev density theorem](course:NT-CFT/the-chebotarev-density-theorem)) there are infinitely many primes \(w'\) of \(L\), over distinct rational primes \(q\ne\ell\) unramified in \(L\), with Frobenius exactly \(\gamma\); a prime whose Frobenius class contains \(\gamma\) has a conjugate with Frobenius \(\gamma\). By (U2) for \(\beta|_{U'}\), all but finitely many of them are the target primes of primes \(v'\nmid\ell\) of \(F'\) active at \(\ell\). The target prime is unique for each \(v'\), so infinitely many \(v'\) occur. Only finitely many primes of \(F'\) lie over a given rational prime, so we may pass to an infinite subset with distinct source rational primes \(p\), unramified in \(F'\), and then to an infinite subset on which the Frobenius of \(v'\) in \(\operatorname{Gal}(F'/\mathbb Q)\) is a fixed \(\delta\).

*Prolongations.* Fix a prime \(\bar v\) of \(\overline{\mathbb Q}\) above each \(v'\), and let \(v\) be the prime of \(k\) below it. The correspondence at \(v'\) can be realized with \(\bar v\): another prime above \(v'\) is \(s\bar v\) with \(s\in U'\), and replacing \(\bar v\) by \(s\bar v\) conjugates the target decomposition group by \(\beta(s)\in P_L\), which keeps it above \(w'\). The prime \(v\) is active at \(\ell\) for \(\beta\): the inertia group of \(\bar v\) in \(G_{F'}\) lies in that in \(G_k\), and a pro-\(\ell\) Sylow subgroup of the first lies in one of the second (Proposition 4.1(2) of the first lesson). Apply (U2) to \(\beta\colon G_k\to P\) at \(v\), with \(\bar v\): there is a prime \(\bar w_1\) of \(\mathbb Q^s\) with \(\beta(D_v)\subseteq D_{\bar w_1}\). Let \(w_1\) be the prime of \(L\) below \(\bar w_1\). Then
\[
\beta(D_{v'})\subseteq\beta(D_v)\cap P_L\subseteq D_{\bar w_1}\cap P_L ,
\]
a decomposition group of \(P_L\) at \(w_1\). Uniqueness in (U2) for \(\beta|_{U'}\) at \(v'\) gives \(w_1=w'\). Hence the target rational prime of \(v\) is \(q\), and the image of \(D_v\) in \(R\) lies in the decomposition group of \(w'\) in \(R\), which is \(C\). These choices keep \(v'\) and \(w'\), hence \(\delta\) and \(\gamma\).

*The residue degree.* Let \(H=T/U'\subseteq\operatorname{Gal}(F'/\mathbb Q)=\mathcal G/U'\), and let \(f\) be the residue degree of \(v\) over \(p\). The decomposition group of \(v'\) over \(p\) is \(\langle\delta\rangle\), and over \(k\) it is \(\langle\delta\rangle\cap H\), so \(f\) is the index of \(\langle\delta\rangle\cap H\) in the cyclic group \(\langle\delta\rangle\), and
\[
\begin{gathered}
\langle\delta\rangle\cap H=\langle\delta^f\rangle,\\
f=\min\{j\ge1:\delta^j\in H\}.
\end{gathered}\tag{3.1}
\]
In particular \(f\) is the same for all chosen primes. As \(\beta(U')\subseteq P_L\), \(\beta\) induces a homomorphism \(H\to R\); put \(d=\beta(\delta^f)\in R\). Let \(\phi\) be an arithmetic Frobenius lift at \(\bar v\) over \(p\); its image in \(\operatorname{Gal}(F'/\mathbb Q)\) is \(\delta\). Then \(\phi^f\) maps to \(\delta^f\in H\), so \(\phi^f\in D_v\), and it acts on residues as the \(p^f\)-th power: it is a Frobenius lift at \(v\). Its image in \(R\) is \(d\), so \(d\in C\).

*Generation.* Suppose that \(D=\langle d\rangle\ne C\), and choose \(x\) as in (2.1). Pullback along \(\beta|_{U'}\) is a linear map
\[
\begin{gathered}
j\colon\mathcal X_\ell(L)\to\mathcal X_\ell(F'),\\
y=j(x)=x\circ\beta|_{U'} .
\end{gathered}
\]
It is injective, because \(\beta(U')\) is open in \(P_L\) (Lemma 2.1(5) of the character lesson). Since \(\gamma\) fixes \(w'\), \((gx)(\operatorname{Fr}_{w'})=x(\operatorname{Fr}_{w'})\) for \(g\in C\), so \(x(\operatorname{Fr}_{w'})=(E_Cx)(\operatorname{Fr}_{w'})=0\). The character \(x\) is unramified at \(w'\) (Lemma 1.1 of the character lesson), so it vanishes on the decomposition group at \(w'\), which contains \(\beta(D_{v'})\). Hence \(y(\operatorname{Fr}_{v'})=0\) for every chosen \(v'\), and Proposition 4.1(2) of the character lesson gives
\[
E_{\langle\delta\rangle}y=0. \tag{3.2}
\]
The group \(\mathcal G\) acts on \(\mathcal X_\ell(F')\) through \(\operatorname{Gal}(F'/\mathbb Q)\), and \(j\) is \(T\)-equivariant when \(T\) acts on \(\mathcal X_\ell(L)\) through \(\beta\): \((t\cdot j(x'))(h)=x'(\beta(t)^{-1}\beta(h)\beta(t))\), which is \(j(\beta(t)x')(h)\). Let \(a\) be the order of \(\delta\). For \(f\mid j\), a lift \(t\in T\) of \(\delta^j\) has \(\beta(t)\in D\) modulo \(P_L\), so \(\delta^jy=j(\beta(t)x)=y\), because \(x\) is \(D\)-invariant. For \(f\nmid j\), a lift \(t\in\mathcal G\) of \(\delta^j\) is not in \(T\) by (3.1), so \(tNt^{-1}=N_i\) for some \(i\); and \(\delta^jy=t\cdot y\) is fixed by \(N_i\), because \(y\) is fixed by \(N\): \(n\cdot y=j(\beta(n)x)=y\) for \(n\in N\), as \(\beta(n)=1\). Multiplying (3.2) by \(a\),
\[
\begin{gathered}
0=\frac af\,y+\sum_{0\le j<a,\ f\nmid j}\delta^jy,\\
\text{so}\qquad y\in\sum_{i=1}^r\mathcal X_\ell(F')^{N_i}.
\end{gathered}
\]
The finite group \(U/U'\) acts on \(\mathcal X_\ell(F')\), and the image \(Y=j(\mathcal X_\ell(L))\) is stable under it. By Maschke's theorem there is a \(U\)-equivariant projection \(\pi\colon\mathcal X_\ell(F')\to Y\). Each \(N_i\) lies in \(U\), so \(\pi\) maps \(\mathcal X_\ell(F')^{N_i}\) into \(Y^{N_i}\), and by equivariance and injectivity of \(j\), \(Y^{N_i}=j(\mathcal X_\ell(L)^{H_i})\). Applying \(\pi\) and then \(j^{-1}\) gives \(x\in\sum_i\mathcal X_\ell(L)^{H_i}\), contrary to (2.1). Hence \(D=C\), which is assertion 2. \(\square\)

No normality of \(T\) in \(\mathcal G\) is used: only the \(U\)-equivariance of the projection.

## 4. Surjectivity and cyclotomic logarithms

For a prime \(\ell\), \(\log\colon\mathbb Z_\ell^\times\to\mathbb Z_\ell\) is the logarithm vanishing on roots of unity (Section 1 of the logarithm rank lesson), so \(\log\chi_\ell\) and \(\log\chi_{k,\ell}\) are additive characters.

**Theorem 4.1** ([OpenAI-UC, Theorem 4.4]). The homomorphism \(\beta\colon G_k\to P\) is surjective. Put \(m_0=[k:\mathbb Q]!\) and
\[
\mathcal L=\{\ell\ \text{odd prime}:\ \ell\equiv1\bmod m_0\}.
\]
The set \(\mathcal L\) is infinite, and for every \(\ell\in\mathcal L\)
\[
\begin{gathered}
\log\chi_\ell\circ\beta=\log\chi_{k,\ell}\\
\text{in }\mathcal X_\ell(k).
\end{gathered}\tag{4.1}
\]

*Proof.* *Surjectivity.* Let \(R_0\) be a finite quotient of \(P\) and \(\gamma_0\in R_0\). Proposition 3.1 produces an element \(d\) of the image of \(\beta\) in a quotient \(R\) with \(\langle d\rangle=\langle\gamma\rangle\), where \(\gamma\) lifts \(\gamma_0\). So \(\gamma_0\) lies in the image of \(\beta\) in \(R_0\). The image \(\beta(G_k)\) is compact and maps onto every finite quotient of \(P\), so it is \(P\).

*The set \(\mathcal L\).* By Dirichlet's theorem on primes in arithmetic progressions (Theorem 4.1 of [Dirichlet's theorem on primes in arithmetic progressions](course:NT-DIRL/NT-DIRL-02), whose sum over primes \(p\equiv1\pmod{2m_0}\) diverges as \(\sigma\downarrow1\)), \(\mathcal L\) is infinite.

*Cyclotomic logarithms.* Fix \(\ell\in\mathcal L\), take \(R_0=\operatorname{Gal}(\mathbb Q(\mu_\ell)/\mathbb Q)\cong\mathbb F_\ell^\times\), cyclic of order \(\ell-1\), and let \(\gamma_0\) generate it. Proposition 3.1 gives infinitely many active primes \(v\) of \(k\), over distinct \(p\ne\ell\), with Frobenius lifts \(\sigma_v\) such that \(\beta(\sigma_v)\) acts on \(\mu_\ell\) through a generator of \(\mathbb F_\ell^\times\). Let \(q\) be the target rational prime of \(v\), \(f\) the residue degree of \(v\) over \(p\), so \(Nv=p^f\), and \(a=a(\sigma_v)\) the target residue exponent. By the norm identity (Lemma 6.1 of the first lesson), with \(b(\sigma_v)=1\),
\[
p^f=q^{a}\quad\text{in }\mathbb Z_\ell^\times . \tag{4.2}
\]
An element of a decomposition group with residue exponent \(e\) at a prime of residue characteristic \(s\) acts on the roots of unity of order prime to \(s\) as the \(s^e\)-th power, because reduction is injective on them. So \(\chi_\ell(\beta(\sigma_v))=q^a\) and \(\chi_{k,\ell}(\sigma_v)=p^f\). Reducing (4.2) modulo \(\ell\), \(p^f\) generates \(\mathbb F_\ell^\times\); a prime dividing both \(f\) and \(\ell-1\) would make \(p^f\) a proper power in the cyclic group \(\mathbb F_\ell^\times\), so \(\gcd(f,\ell-1)=1\). But \(1\le f\le[k:\mathbb Q]\), so every prime divisor of \(f\) divides \(m_0\), hence \(\ell-1\). Therefore \(f=1\), and
\[
\begin{aligned}
(\log\chi_\ell\circ\beta)(\sigma_v)&=\log q^a=\log p\\
&=\log\chi_{k,\ell}(\sigma_v).
\end{aligned}
\]
The difference of the two sides of (4.1) is an element of \(\mathcal X_\ell(k)\), unramified at \(v\), that vanishes at \(\operatorname{Fr}_v\) for infinitely many primes \(v\nmid\ell\) of absolute residue degree one. Proposition 4.1(1) of the character lesson gives (4.1). \(\square\)

## 5. Exercises

**5.1.** Let \(\alpha_0\colon G_F\to P\) be the restriction. Show that \(T=\mathcal G\) and that \(\beta\) is the restriction \(\mathcal G\to P\).

**5.2.** In the proof of Lemma 2.1, show that \(\operatorname{Gal}(L/\mathbb Q)\) is solvable and that \(L\) is totally imaginary.

**5.3.** Let \(g\) be an element of order \(d\) of a finite group \(R_1\) of order \(n\). Show that \(g-1\) has rank \(n-n/d\) on \(\mathbb F_2[R_1]\).

**5.4.** Show that the residue degree of \(v\) over \(p\) in Section 3 is the index of \(\langle\delta\rangle\cap H\) in \(\langle\delta\rangle\), using that residue degrees multiply in towers and equal orders of decomposition groups at unramified primes.

**5.5.** Show directly that \(\log\chi_{\mathbb Q,\ell}\) restricted to \(G_k\) equals \(\log\chi_{k,\ell}\), and deduce that (4.1) holds for every \(\ell\) when \(\beta\) is the restriction \(G_k\to P\).

## 6. Solutions

**5.1.** Here \(N=U\cap\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q^s)\) is an intersection of two normal subgroups of \(\mathcal G\), hence normal, so \(T=\mathcal G\). The restriction \(\mathcal G\to P\) is a continuous homomorphism extending \(\alpha_0|_U\), so it is \(\beta\) by the uniqueness in Lemma 1.1.

**5.2.** \(R\) is an extension of the solvable group \(R_1\) by the abelian group \(V\), so it is solvable. \(L\) contains \(\mathbb Q(i)\), which has no real embedding.

**5.3.** \(g\) acts on the basis \(R_1\) by left multiplication, with \(n/d\) orbits \(\{h,gh,\ldots,g^{d-1}h\}\). The kernel of \(g-1\) consists of the functions constant on orbits, of dimension \(n/d\).

**5.4.** At an unramified prime the residue degree equals the order of the decomposition group. The decomposition group of \(v'\) over \(p\) has order \(f(v'/p)=f(v'/v)f(v/p)\), and that over \(k\) is \(\langle\delta\rangle\cap H\), of order \(f(v'/v)\). So \(f(v/p)=|\langle\delta\rangle|/|\langle\delta\rangle\cap H|\).

**5.5.** Both are the action of \(g\in G_k\) on \(\mu_{\ell^\infty}\), followed by \(\log\). For the restriction \(\beta\colon G_k\to P\), \(\chi_\ell(\beta(g))=\chi_{\mathbb Q,\ell}(g)\), since \(\mu_{\ell^\infty}\subset\mathbb Q^s\).

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Section 4. https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
- [Uchida 1979] K. Uchida, *Isomorphisms of Galois groups of solvably closed Galois extensions*, Tôhoku Math. J. (2) 31 (1979), 359–362, pp. 360–362 (the regular-module construction). https://doi.org/10.2748/tmj/1178229803
