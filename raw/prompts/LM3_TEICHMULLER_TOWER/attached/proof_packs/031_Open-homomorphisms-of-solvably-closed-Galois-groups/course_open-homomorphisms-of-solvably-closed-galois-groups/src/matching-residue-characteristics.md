# Matching residue characteristics

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Uchida's partial local correspondence pairs primes of the domain field with primes of the target field, but the auxiliary prime \(\ell\) that makes a pair active may vary, and the correspondence itself does not say that paired primes have the same residue characteristic. This lesson proves that almost every prime of \(\mathbb Q(i)\) above a split rational prime \(q\) has a partner above the same \(q\). Two finiteness statements make this possible: almost every such target prime has only finitely many possible partners, over all auxiliary primes together; and the number of target primes missed at one auxiliary prime is bounded independently of that prime. A choice of \(\ell\) by simultaneous power-residue conditions then forces a contradiction.

- The setting (Section 1).
- Finite fibres (Section 2).
- A uniform bound on missed primes (Section 3).
- Separation by power residues (Section 4).
- Matching residue characteristics (Section 5).

## 1. The setting

Keep the open homomorphism \(\alpha_0\colon G_F\to P\), the number field \(k\), the extension \(\beta\colon G_k\to P\) and the infinite set \(\mathcal L\) of [Normalizer extension and Frobenius generation](normalizer-extension-and-frobenius-generation.md). By Theorem 4.1 there, \(\beta\) is surjective and \(\log\chi_\ell\circ\beta=\log\chi_{k,\ell}\) for \(\ell\in\mathcal L\). Put
\[
\begin{gathered}
B=\mathbb Q(i),\qquad G_K=\beta^{-1}(P_B),\\
\beta_B=\beta|_{G_K}\colon G_K\to P_B .
\end{gathered}
\]
As \(\beta\) is surjective and \(P_B\) has index \(2\) in \(P\), \(K/k\) is quadratic and \(\beta_B\) is surjective.

An *active pair at \(\ell\)* is a prime \(v\) of \(K\) active at \(\ell\) for \(\beta_B\) together with its prime \(w\) of \(B\) from (U2) (Section 3 of [Solvably closed fields and Uchida's conjecture](solvably-closed-fields-and-uchidas-conjecture.md)); both lie away from \(\ell\), and \(\beta_B(D_v)\subseteq D_w\) for suitable primes above them. For a prime \(w\) of \(B\) put
\[
\begin{aligned}
\mathcal V_w=\{v:\ &(v,w)\text{ is an active pair}\\
&\text{at some }\ell\in\mathcal L\},
\end{aligned}
\]
and for \(\ell\in\mathcal L\) let \(\mathcal M_\ell\) be the set of primes of \(B\) occurring in no active pair at \(\ell\); it contains the primes above \(\ell\). A prime of \(B\) above a rational prime \(q\) that splits in \(B\) has norm \(q\).

## 2. Finite fibres

**Lemma 2.1** ([OpenAI-UC, Lemma 5.1]). For all but finitely many primes \(w\) of \(B\) above rational primes split in \(B\), the set \(\mathcal V_w\) is finite.

*Proof.* Fix \(r\in\mathcal L\). The group \(\operatorname{Gal}(B/\mathbb Q)=\{1,c\}\) and \(W_B=\operatorname{Ind}_{\langle c\rangle}^{\{1,c\}}(\operatorname{sign})\) is the sign character; by Proposition 5.3 of [Additive characters and Frobenius detection](additive-characters-and-frobenius-detection.md) there is \(\psi\ne0\) in \(\mathcal X_r(B)\) with \(c\psi=-\psi\). By Proposition 4.1(1) there, \(\psi(\operatorname{Fr}_w)\ne0\) at all but finitely many primes \(w\nmid r\) of degree one. Fix such a \(w\), above a split rational prime \(q\ne r\), and put
\[
\begin{gathered}
x_0=\log\chi_r|_{G_B}\in\mathcal X_r(B),\\
z=\frac{\psi(\operatorname{Fr}_w)}{\log q}.
\end{gathered}
\]
Here \(x_0(\operatorname{Fr}_w)=\log Nw=\log q\ne0\), since the positive integer \(q>1\) is not a root of unity, and \(z\ne0\). The character \(\psi-zx_0\) is unramified at \(w\) and vanishes at \(\operatorname{Fr}_w\), so it vanishes on every decomposition group at \(w\). Put
\[
y=(\psi-zx_0)\circ\beta_B\in\mathcal X_r(K).
\]

The character \(\psi\circ\beta_B\) changes sign under the action of \(G_k/G_K\): for \(t\in G_k\setminus G_K\) and \(h\in G_K\),
\[
\begin{aligned}
&(t\cdot(\psi\circ\beta_B))(h)\\
&\quad=\psi(\beta(t)^{-1}\beta_B(h)\beta(t))\\
&\quad=(\beta(t)\psi)(\beta_B(h)),
\end{aligned}
\]
and \(\beta(t)\) acts on \(\mathcal X_r(B)\) through \(c\). By Lemma 2.1(3) of the character lesson, \(\operatorname{res}_{K/k}\operatorname{cor}_{K/k}(\psi\circ\beta_B)\) equals \(\psi\circ\beta_B-\psi\circ\beta_B=0\), so \(\operatorname{cor}_{K/k}(\psi\circ\beta_B)=0\) by injectivity of restriction. On the other hand \(x_0\circ\beta_B=\log\chi_{K,r}=\operatorname{res}_{K/\mathbb Q}\log\chi_{\mathbb Q,r}\), by (4.1) of the generation lesson restricted to \(G_K\). By the transitivity and the corestriction–restriction identity of Lemma 2.1 of the character lesson,
\[
\begin{aligned}
\operatorname{cor}_{K/\mathbb Q}y&=\operatorname{cor}_{k/\mathbb Q}\bigl(\operatorname{cor}_{K/k}(\psi\circ\beta_B)\bigr)\\
&\quad-z[K:\mathbb Q]\log\chi_{\mathbb Q,r}\\
&=-z[K:\mathbb Q]\log\chi_{\mathbb Q,r}\ne0 .
\end{aligned}
\]

Let \(v\in\mathcal V_w\) with \(v\nmid r\), active at some \(\ell\in\mathcal L\). Then \(\beta_B(D_v)\) lies in a decomposition group at \(w\), where \(\psi-zx_0\) vanishes, so \(y(\operatorname{Fr}_v)=0\), whichever auxiliary prime \(\ell\) makes the pair active. By Proposition 4.1(3) of the character lesson there are only finitely many such \(v\), and finitely many primes of \(K\) lie above \(r\). So \(\mathcal V_w\) is finite. The excluded \(w\) are the finitely many with \(\psi(\operatorname{Fr}_w)=0\) and those above \(r\). \(\square\)

## 3. A uniform bound on missed primes

**Proposition 3.1** ([OpenAI-UC, Proposition 5.3]). For every \(\ell\in\mathcal L\),
\[
\begin{gathered}
\#\{w\in\mathcal M_\ell:w\nmid\ell\}\le2[K:\mathbb Q],\\
\#\mathcal M_\ell\le2[K:\mathbb Q]+2 .
\end{gathered}
\]

*Proof.* We use the tools of [Kummer classes and S-units](kummer-classes-and-s-units.md). Fix \(\ell\in\mathcal L\) and a finite set \(J\subseteq\mathcal M_\ell\) of primes not above \(\ell\). For \(w\in J\) choose \(h_w>0\) and \(a_w\in B^\times\) with \((a_w)=w^{h_w}\), and let \(\kappa_w\in H^1(P_B,\mathbb Q_\ell(1))\) be the Kummer class of \(a_w\), which factors through \(P_B\) (Section 3 of that lesson).

*Independence.* The classes \(\kappa_w\) are linearly independent. Inflation to \(G_B\) is injective (Lemma 1.1(1) there), and in \(H^1(G_B,\mathbb Q_\ell(1))\cong\widehat{B^\times}\otimes\mathbb Q_\ell\) the valuation \(\widehat{\operatorname{ord}}_w\) takes the value \(h_w\) on \(a_w\) and \(0\) on \(a_{w'}\) for \(w'\ne w\). By Lemma 3.1 there, \(\kappa_w\) is unramified at every finite prime of \(B\) other than \(w\) and the primes above \(\ell\).

*Twisting.* Let \(\rho=\chi_\ell\circ\beta_B\) and \(\varepsilon=\rho\,\chi_{K,\ell}^{-1}\), characters of \(G_K\) with values in \(\mathbb Z_\ell^\times\). By (4.1) of the generation lesson, \(\log\varepsilon=0\), so \(\varepsilon\) takes values in the roots of unity \(\mu_{\ell-1}\subset\mathbb Z_\ell^\times\). Let \(K'/K\) be the cyclic extension fixed by \(\ker\varepsilon\) and \(\Delta=\operatorname{Gal}(K'/K)\). Pullback along the surjection \(\beta_B\) is injective on \(H^1\) (Lemma 1.1(1)), with values in \(H^1(G_K,\mathbb Q_\ell(\rho))\), and restriction to the open normal subgroup \(G_{K'}\) is injective (Lemma 1.1(2)). On \(G_{K'}\) we have \(\rho=\chi_{K',\ell}\), so we obtain linearly independent classes
\[
\begin{aligned}
c_w&=[\kappa_w\circ\beta_B|_{G_{K'}}]\\
&\in H^1(G_{K'},\mathbb Q_\ell(1))\qquad(w\in J).
\end{aligned}
\]
By Lemma 1.2 there, with \(\chi=\chi_{K,\ell}\), each \(c_w\) lies in the \(\varepsilon^{-1}\)-eigenspace of the action of \(\Delta\).

*Unramified away from \(\ell\).* Suppose \(c_w\) is ramified at a prime \(u\nmid\ell\) of \(K'\), and let \(v\) be the prime of \(K\) below it, with a common prime of \(\overline{\mathbb Q}\) above both. The inertia group \(I_u\) acts trivially on \(\mathbb Q_\ell(1)\), so the restriction of \(c_w\) to \(I_u\) is a nonzero homomorphism to \(\mathbb Q_\ell\); as in Lemma 1.1 of the character lesson it vanishes on wild inertia and on the pro-\(\ell'\) factors, \(\ell'\ne\ell\), of tame inertia, so it is nonzero on a pro-\(\ell\) Sylow subgroup \(J_u\) of \(I_u\). Choose a pro-\(\ell\) Sylow subgroup \(J_v\) of \(I_v\) containing \(J_u\) (Proposition 4.1(2) of the first lesson). If \(\beta_B(J_v)=1\), then \(\kappa_w\circ\beta_B\) vanishes on \(J_u\); so \(\beta_B(J_v)\ne1\), and \(v\) is active at \(\ell\). By (U2) there is a prime \(t\nmid\ell\) of \(B\) with \(\beta_B(J_v)\) contained in an inertia group at \(t\). Since \(t\) occurs in an active pair at \(\ell\), \(t\notin\mathcal M_\ell\supseteq J\), so \(t\ne w\), and \(\kappa_w\) vanishes on the inertia groups at \(t\). Hence \(\kappa_w\circ\beta_B\) vanishes on \(J_u\), a contradiction.

*Counting.* Let \(S\) consist of the archimedean places of \(K'\) and its primes above \(\ell\). By Proposition 3.2 of the Kummer lesson, the \(c_w\) correspond to linearly independent elements of the \(\varepsilon^{-1}\)-eigenspace of \(\mathcal O_{K',S}^\times\otimes\mathbb Q_\ell\), the isomorphism being compatible with \(\Delta\). By Proposition 4.1 there, this eigenspace has dimension at most the number of \(\Delta\)-orbits on \(S\), which is
\[
\begin{gathered}
r_1(K)+r_2(K)+\#\{v\text{ of }K:v\mid\ell\}\\
\le2[K:\mathbb Q].
\end{gathered}
\]
So \(\#J\le2[K:\mathbb Q]\). As \(J\) was arbitrary, this bounds the missed primes away from \(\ell\); at most two primes of \(B\) lie above \(\ell\). \(\square\)

The bound depends on \(K\), but neither on \(\ell\) nor on the degree of \(K'/K\), which may grow with \(\ell\).

## 4. Separation by power residues

**Lemma 4.1** ([OpenAI-UC, Lemma 5.4]). Let \(m,d\ge1\), let \(q_1,\ldots,q_n\) be distinct rational primes, and for each \(j\) let \(\mathcal P_j\) be a finite set of rational primes not containing \(q_j\). For every finite set \(\Sigma\) of rational primes there are infinitely many odd primes \(\ell\equiv1\pmod m\), outside \(\Sigma\) and all the given sets, such that
\[
\begin{gathered}
p^f\bmod\ell\notin\langle q_j\bmod\ell\rangle\\
(1\le j\le n,\ p\in\mathcal P_j,\ 1\le f\le d).
\end{gathered}
\]
The sets \(\mathcal P_j\) may overlap and may contain \(q_i\) for \(i\ne j\).

*Proof.* Choose distinct primes \(s_1,\ldots,s_n\) larger than \(m\), \(d\) and every prime in the lists, and put \(C=\mathbb Q(\zeta_{ms_1\cdots s_n})\). Fix \(j\). A listed rational prime \(p\) does not divide \(s_1\cdots s_n\), so its ramification index \(e_p\) in \(C/\mathbb Q\) equals that in \(\mathbb Q(\zeta_m)\), which divides \([\mathbb Q(\zeta_m):\mathbb Q]\le m<s_j\); so \(e_p\) is prime to \(s_j\). If \(\prod_pp^{x_p}\), over the primes in \(\{q_j\}\cup\mathcal P_j\) with \(0\le x_p<s_j\), were an \(s_j\)-th power in \(C\), the valuation at a prime of \(C\) above \(p\) would give \(s_j\mid e_px_p\), so \(x_p=0\). Thus the classes of these primes are independent in \(C^\times/C^{\times s_j}\), and as \(\mu_{s_j}\subset C\), the Kummer correspondence identifies
\[
\begin{gathered}
\operatorname{Gal}(E_j/C),\\
E_j=C\bigl(q_j^{1/s_j},\ p^{1/s_j}\ (p\in\mathcal P_j)\bigr),
\end{gathered}
\]
with an elementary abelian \(s_j\)-group with one independent coordinate for each listed prime. Choose \(\sigma_j\) fixing \(q_j^{1/s_j}\) and moving every \(p^{1/s_j}\), \(p\in\mathcal P_j\). The degrees \([E_j:C]\) are powers of distinct primes, so the \(E_j\) are linearly disjoint over \(C\) and the \(\sigma_j\) combine to \(\sigma\in\operatorname{Gal}(E/C)\), \(E=E_1\cdots E_n\).

\(E/\mathbb Q\) is Galois, being generated over the Galois field \(C\) by all \(s_j\)-th roots of rational numbers. Conjugating \(\sigma\) by \(\tau\in\operatorname{Gal}(E/\mathbb Q)\) multiplies the root-of-unity factor \(\zeta\) of \(\sigma\) on each radical \(p^{1/s_j}\) by the automorphism \(\zeta\mapsto\tau(\zeta)\): if \(\sigma(p^{1/s_j})=\zeta p^{1/s_j}\), then \(\tau\sigma\tau^{-1}(p^{1/s_j})=\tau(\zeta)p^{1/s_j}\). So triviality of each coordinate is a property of the conjugacy class. By Chebotarev's theorem (Theorem 22.4 of [The Chebotarev density theorem](course:NT-CFT/the-chebotarev-density-theorem)) there are infinitely many primes \(\ell\), unramified in \(E\) and outside \(\Sigma\), the lists and \(\{2\}\), whose Frobenius class contains \(\sigma\). They split completely in \(C\), so \(\ell\equiv1\pmod m\) and \(\ell\equiv1\pmod{s_j}\). For a listed \(p\), \(p\) is an \(s_j\)-th power modulo \(\ell\) exactly when \(X^{s_j}-p\) has a root in \(\mathbb F_\ell\), which contains \(\mu_{s_j}\), that is, exactly when Frobenius fixes \(p^{1/s_j}\). So \(q_j\) is an \(s_j\)-th power modulo \(\ell\), and no \(p\in\mathcal P_j\) is.

The quotient \(\mathbb F_\ell^\times/\mathbb F_\ell^{\times s_j}\) has prime order \(s_j\). For \(1\le f\le d<s_j\), the class of \(p^f\) is the \(f\)-th power of a nontrivial class, hence nontrivial; every power of \(q_j\) has trivial class. So \(p^f\bmod\ell\notin\langle q_j\bmod\ell\rangle\). The conditions for different \(j\) live in linearly disjoint extensions, so overlaps between the lists do not conflict. \(\square\)

## 5. Matching residue characteristics

**Proposition 5.1** ([OpenAI-UC, Proposition 5.5]). For all but finitely many primes \(w\) of \(B\) above rational primes \(q\) split in \(B\), there are a prime \(v\) of \(K\) above the same \(q\) and \(\ell\in\mathcal L\) such that \((v,w)\) is an active pair at \(\ell\).

*Proof.* Suppose there are infinitely many exceptions. By Lemma 2.1 we may choose exceptions \(w_1,\ldots,w_n\), with \(n>2[K:\mathbb Q]+2\), above distinct split rational primes \(q_1,\ldots,q_n\), with every \(\mathcal V_{w_j}\) finite. Let \(\mathcal P_j\) be the set of residue characteristics of the primes in \(\mathcal V_{w_j}\). Since \(w_j\) is an exception, \(q_j\notin\mathcal P_j\).

Apply Lemma 4.1 with \(m=m_0=[k:\mathbb Q]!\) and \(d=[K:\mathbb Q]\). It gives an odd prime \(\ell\equiv1\pmod{m_0}\), so \(\ell\in\mathcal L\), with
\[
\begin{gathered}
Nv\bmod\ell\notin\langle q_j\bmod\ell\rangle\\
(v\in\mathcal V_{w_j},\ 1\le j\le n),
\end{gathered}\tag{5.1}
\]
because \(Nv=p^f\) with \(p\in\mathcal P_j\) and \(1\le f\le[K:\mathbb Q]\). If \(w_j\) occurred in an active pair \((v,w_j)\) at this \(\ell\), then \(v\in\mathcal V_{w_j}\), and the norm identity (Lemma 6.1 of the first lesson), applied to an arithmetic Frobenius lift at \(v\), would give \(Nv=(Nw_j)^a=q_j^a\) in \(\mathbb Z_\ell^\times\) for some \(a\in\widehat{\mathbb Z}\); reducing modulo \(\ell\), \(Nv\bmod\ell\in\langle q_j\bmod\ell\rangle\), contrary to (5.1). So all \(n\) primes \(w_j\) lie in \(\mathcal M_\ell\), contradicting Proposition 3.1. \(\square\)

## 6. Exercises

**6.1.** Show that a prime of \(\mathbb Q(i)\) above an odd rational prime \(q\) has norm \(q\) exactly when \(q\equiv1\pmod4\).

**6.2.** In the proof of Lemma 2.1, show that \(\log\chi_{\mathbb Q,r}\ne0\).

**6.3.** Let \(\varepsilon\colon G_K\to\mathbb Z_\ell^\times\) be a continuous character with \(\log\varepsilon=0\), \(\ell\) odd. Show that \(\varepsilon\) has finite image of order dividing \(\ell-1\).

**6.4.** Take \(n=1\), \(q_1=5\), \(\mathcal P_1=\{2\}\), \(d=1\), \(m=1\) in Lemma 4.1. Find a prime \(\ell\) with \(2\bmod\ell\notin\langle5\bmod\ell\rangle\).

**6.5.** Show that \(\#\{v\text{ of }K:v\mid\ell\}\le[K:\mathbb Q]\) and \(r_1(K)+r_2(K)\le[K:\mathbb Q]\).

## 7. Solutions

**6.1.** A prime \(q\equiv1\pmod4\) splits as \(q=\pi\bar\pi\) with primes of norm \(q\); \(q\equiv3\pmod4\) is inert, with norm \(q^2\), because \(-1\) is not a square modulo \(q\) (the decomposition of primes in quadratic fields, [Decomposition of primes in extensions](course:NT-ANT/decomposition-of-primes-in-extensions)).

**6.2.** Its value at a Frobenius element at a prime \(p\ne r\) is \(\log p\), and \(p>1\) is not a root of unity in \(\mathbb Z_r^\times\).

**6.3.** The kernel of \(\log\) on \(\mathbb Z_\ell^\times\) is the group of roots of unity \(\mu_{\ell-1}\), so \(\varepsilon\) takes values in this finite group.

**6.4.** \(\ell=11\): the powers of \(5\) modulo \(11\) are \(5,3,4,9,1\), the squares, and \(2\) is not a square modulo \(11\).

**6.5.** The local degrees \([K_v:\mathbb Q_\ell]\) over \(v\mid\ell\) add up to \([K:\mathbb Q]\), and each is at least \(1\). Similarly \(r_1+2r_2=[K:\mathbb Q]\).

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Section 5. https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
- [Uchida 1981] K. Uchida, *Homomorphisms of Galois groups of solvably closed Galois extensions*, J. Math. Soc. Japan 33 (1981), 595–604, Proposition 1 (the Kummer argument for cofinite target coverage). https://doi.org/10.2969/jmsj/03340595
