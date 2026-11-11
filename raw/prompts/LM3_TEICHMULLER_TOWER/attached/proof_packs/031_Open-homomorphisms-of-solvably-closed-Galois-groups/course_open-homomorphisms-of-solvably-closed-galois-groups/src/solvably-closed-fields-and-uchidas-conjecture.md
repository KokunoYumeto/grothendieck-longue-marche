# Solvably closed fields and Uchida's conjecture

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

A field is *solvably closed* if it has no nontrivial abelian algebraic extension. The algebraic closure of \(\mathbb Q\) and the maximal prosolvable extension of \(\mathbb Q\) are examples. Uchida conjectured in 1981 that every continuous homomorphism with open image between Galois groups of solvably closed Galois extensions of number fields comes from an embedding of the fields [Uchida 1981, p. 595]. This course presents the proof of the conjecture by OpenAI [OpenAI-UC]. This lesson sets up the objects, states the theorem, states the three published results that the proof uses without proving them here, and proves two tools needed throughout: Sylow subgroups of profinite groups, and the local structure of Galois groups inside the maximal prosolvable extension, ending with an identity between the norms of corresponding primes.

- Solvably closed fields (Section 1).
- The conjecture (Section 2).
- Three results of Uchida and Hoshi (Section 3).
- Sylow subgroups of profinite groups (Section 4).
- Local Galois groups inside the prosolvable closure (Section 5).
- The norm identity (Section 6).

## 1. Solvably closed fields

All fields have characteristic \(0\). Fix an algebraic closure \(\overline{\mathbb Q}\) of \(\mathbb Q\); number fields are subfields of \(\overline{\mathbb Q}\) of finite degree over \(\mathbb Q\). For a number field \(M\) put \(G_M=\operatorname{Gal}(\overline{\mathbb Q}/M)\), and write \(\mathcal G=G_{\mathbb Q}\). Infinite Galois groups carry the Krull topology, and the Galois correspondence between closed subgroups and intermediate fields is Theorem 1.2 of [Profinite groups and infinite Galois theory](course:NT-CFT/profinite-groups-and-infinite-galois-theory). Homomorphisms between profinite groups and characters are always continuous. A homomorphism is *open* if its image is open.

**Definition 1.1.** A field \(E\) is *solvably closed* if every abelian Galois extension of \(E\) inside an algebraic closure of \(E\) is trivial. The *prosolvable closure* \(\mathbb Q^s\subset\overline{\mathbb Q}\) is the compositum of all finite Galois extensions of \(\mathbb Q\) in \(\overline{\mathbb Q}\) whose Galois group is solvable. Put
\[
\begin{gathered}
P=\operatorname{Gal}(\mathbb Q^s/\mathbb Q),\\
P_M=\operatorname{Gal}(\mathbb Q^s/M)\quad(M\subset\mathbb Q^s).
\end{gathered}
\]

A compositum of two finite Galois extensions with solvable groups is Galois with solvable group, because restriction embeds its group in the product of the two groups. So \(\mathbb Q^s/\mathbb Q\) is Galois, every finite Galois subextension of \(\mathbb Q^s/\mathbb Q\) has solvable group, and every finite quotient of \(P\) is solvable; the same holds for the closed subgroups \(P_M\), since \(P_M/(P_M\cap U)\) embeds in \(P/U\) for every open normal subgroup \(U\) of \(P\).

We use two facts about finite solvable groups. A finite solvable group \(H\) has a chain of subgroups \(1=H_r\subset H_{r-1}\subset\cdots\subset H_0=H\), each normal in the next, with every quotient \(H_{i-1}/H_i\) cyclic of prime order: refine a chain with abelian quotients by chains of a finite abelian group with cyclic quotients of prime order. And a nontrivial finite solvable group has a nontrivial abelian quotient, since its commutator subgroup is a proper subgroup.

**Lemma 1.2.** Let \(K\) be a field inside an algebraic closure \(\Omega\), and let \(E\subset\Omega\) be a solvably closed algebraic extension of \(K\).

1. \(E\) contains all roots of unity of \(\Omega\), and for every \(n\ge1\) every element of \(E\) has an \(n\)-th root in \(E\).
2. \(E\) contains every finite Galois extension of \(K\) in \(\Omega\) with solvable Galois group.

*Proof.* (1) Let \(\mu_n\) be the group of \(n\)-th roots of unity in \(\Omega\). The extension \(E(\mu_n)/E\) is Galois, and \(\sigma\mapsto(\zeta\mapsto\sigma(\zeta))\) embeds its group in the abelian group of automorphisms of the cyclic group \(\mu_n\). So \(E(\mu_n)=E\). For a prime \(p\), the field \(E\) contains \(\mu_p\), and Theorem 3.3 of [Hilbert's Theorem 90 and Kummer theory](course:NT-CFT/hilberts-theorem-90-and-kummer-theory) applies: \(E(a^{1/p})\) is an abelian extension of \(E\) for every \(a\in E^\times\), hence equal to \(E\). Iterating over the prime factors of \(n\) gives \(n\)-th roots.

(2) Let \(L/K\) be finite Galois with solvable group, put \(n=[L:K]\) and \(C=K(\mu_n)\). The extension \(LC/C\) is Galois, and restriction to \(L\) embeds \(\operatorname{Gal}(LC/C)\) in \(\operatorname{Gal}(L/K)\), because an automorphism of \(LC\) fixing \(C\) and \(L\) is the identity. Take a chain \(1=H_r\subset\cdots\subset H_0=\operatorname{Gal}(LC/C)\) as above, with \(H_{i-1}/H_i\) cyclic of prime order \(p_i\); each \(p_i\) divides \(n\). The fixed fields \(C=C_0\subset C_1\subset\cdots\subset C_r=LC\) satisfy: \(C_i/C_{i-1}\) is cyclic of degree \(p_i\), and \(\mu_{p_i}\subset C\subset C_{i-1}\). By the Kummer correspondence, \(C_i=C_{i-1}(\beta_i)\) with \(\beta_i^{p_i}\in C_{i-1}\). Now \(C_0\subset E\) by (1). If \(C_{i-1}\subset E\), then \(\beta_i^{p_i}\) has a \(p_i\)-th root \(\gamma\in E\) by (1), and \(\beta_i=\zeta\gamma\) with \(\zeta\in\mu_{p_i}\subset E\); so \(C_i\subset E\). Hence \(L\subset LC\subset E\). \(\square\)

**Proposition 1.3.**

1. \(\mathbb Q^s\) is solvably closed, contains every root of unity, and every element of \(\mathbb Q^s\) has an \(n\)-th root in \(\mathbb Q^s\) for every \(n\ge1\).
2. Every solvably closed algebraic extension of \(\mathbb Q\) inside \(\overline{\mathbb Q}\) contains \(\mathbb Q^s\).
3. For a number field \(M\subset\mathbb Q^s\), every finite Galois extension of \(M\) in \(\overline{\mathbb Q}\) with solvable group lies in \(\mathbb Q^s\). Consequently every homomorphism from \(G_M\) to an abelian profinite group, and every homomorphism \(G_M\to\mathbb Q_\ell\) to the additive group, factors through restriction \(G_M\to P_M\).

*Proof.* (1) The fields \(\mathbb Q(\mu_n)\) are abelian over \(\mathbb Q\), so they lie in \(\mathbb Q^s\). Let \(a\in\mathbb Q^s\) and let \(p\) be a prime. Then \(a\) lies in a finite Galois extension \(L/\mathbb Q\) with solvable group. Let \(L'\) be generated over \(L(\mu_p)\) by all \(p\)-th roots of all conjugates \(\sigma(a)\), \(\sigma\in\operatorname{Gal}(L/\mathbb Q)\). It is the splitting field over \(\mathbb Q\) of \(\prod_\sigma(X^p-\sigma(a))\) together with the minimal polynomials of a generator of \(L\) and of a primitive \(p\)-th root of unity, so \(L'/\mathbb Q\) is Galois. The group \(\operatorname{Gal}(L'/L(\mu_p))\) is abelian by the Kummer correspondence, and \(\operatorname{Gal}(L(\mu_p)/\mathbb Q)\) embeds in \(\operatorname{Gal}(L/\mathbb Q)\times\operatorname{Gal}(\mathbb Q(\mu_p)/\mathbb Q)\). A group with a solvable normal subgroup and solvable quotient is solvable, so \(L'\subset\mathbb Q^s\), and \(a\) has a \(p\)-th root in \(\mathbb Q^s\). Iterating gives \(n\)-th roots. Now let \(E'/\mathbb Q^s\) be an abelian Galois extension. Every finite subextension \(E''/\mathbb Q^s\) is abelian, and if \(E''\ne\mathbb Q^s\) its group has a quotient of prime order \(p\), giving a cyclic extension of degree \(p\). Since \(\mu_p\subset\mathbb Q^s\) and every element of \(\mathbb Q^s\) is a \(p\)-th power, the Kummer correspondence with \(\Delta=(\mathbb Q^s)^{\times}=(\mathbb Q^{s})^{\times p}\) says that \(\mathbb Q^s\) has no nontrivial abelian extension of exponent \(p\). So \(E'=\mathbb Q^s\).

(2) This is Lemma 1.2(2) with \(K=\mathbb Q\): the compositum of all finite solvable Galois extensions lies in the given field.

(3) By (1), \(\mathbb Q^s\) is a solvably closed algebraic extension of \(M\), so Lemma 1.2(2) with \(K=M\) gives the first assertion. Let \(x\) be a homomorphism from \(G_M\) to an abelian profinite group or to \(\mathbb Q_\ell\). Its kernel is a closed normal subgroup with abelian quotient, so its fixed field \(F_x\) is a Galois extension of \(M\) with abelian group. Each finite subextension of \(F_x/M\) is abelian, hence lies in \(\mathbb Q^s\). Therefore \(F_x\subset\mathbb Q^s\), and \(\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q^s)\subset\ker x\). \(\square\)

A solvably closed field contains all roots of unity. For a Galois extension \(E/F\) with \(E\) solvably closed, the *cyclotomic character*
\[
\begin{gathered}
\chi_{E/F}\colon\operatorname{Gal}(E/F)\longrightarrow\widehat{\mathbb Z}^\times,\\
g(\zeta)=\zeta^{\chi_{E/F}(g)}\quad(\zeta\in\mu_\infty),
\end{gathered}
\]
records the action on the group \(\mu_\infty\) of all roots of unity, using \(\operatorname{Aut}(\mu_\infty)=\widehat{\mathbb Z}^\times\). For a prime \(\ell\), the \(\ell\)-adic character \(\chi_\ell\) is its composite with the projection \(\widehat{\mathbb Z}^\times\to\mathbb Z_\ell^\times\). We write \(\chi_\ell\) on \(P\) and \(\chi_{M,\ell}\) on \(G_M\).

## 2. The conjecture

Let \(F_1,F_2\) be number fields and \(E_i/F_i\) Galois extensions with \(E_i\) solvably closed; put \(G_i=\operatorname{Gal}(E_i/F_i)\). A field embedding \(j\colon E_2\to E_1\) *induces* a homomorphism \(\alpha\colon G_1\to G_2\) if
\[
g\circ j=j\circ\alpha(g)\qquad(g\in G_1).
\]
Then \(j(F_2)\subset F_1\): for \(x\in F_2\) and \(g\in G_1\), \(g(j(x))=j(\alpha(g)(x))=j(x)\), so \(j(x)\) lies in the fixed field \(F_1\) of \(G_1\). The embedding determines \(\alpha\), since \(\alpha(g)=j^{-1}\circ g\circ j\) on \(E_2\), where \(g\) maps \(j(E_2)\) into itself by the displayed relation.

**Theorem 2.1** (Uchida's conjecture; [OpenAI-UC, Theorem 1.1]). Let \(F_1,F_2\) be number fields and \(E_i/F_i\) possibly infinite Galois extensions with \(E_i\) solvably closed. Every continuous homomorphism with open image
\[
\alpha\colon\operatorname{Gal}(E_1/F_1)\longrightarrow\operatorname{Gal}(E_2/F_2)
\]
is induced by a unique field embedding \(j\colon E_2\to E_1\).

No condition is placed on the kernel of \(\alpha\). Uchida proved the case of injective \(\alpha\), as a consequence of his isomorphism theorem stated below, the case \(F_1=\mathbb Q\), and the uniqueness of \(j\) [Uchida 1981, Theorem 1 and Proposition 2]. Hoshi showed that \(j\) exists exactly when \(\alpha\) preserves the cyclotomic characters [Hoshi 2025, Theorem 3.4]. The proof in this course derives that compatibility from the openness of \(\alpha\); [Hoshi 2026, Theorem B] gives two further equivalent forms of the conjecture.

The proof occupies the following lessons. [Counting irreducible components](counting-irreducible-components.md) proves a Bézout-type bound used in [A logarithm rank lemma](a-logarithm-rank-lemma.md), which shows that logarithms of suitably independent algebraic numbers span. [Additive characters and Frobenius detection](additive-characters-and-frobenius-detection.md) deduces that additive \(\ell\)-adic characters are detected by Frobenius elements. [Normalizer extension and Frobenius generation](normalizer-extension-and-frobenius-generation.md) proves that a normalized form \(\beta\) of the homomorphism is surjective and preserves cyclotomic logarithms. [Kummer classes and S-units](kummer-classes-and-s-units.md) and [Matching residue characteristics](matching-residue-characteristics.md) show that corresponding primes have the same residue characteristic, and [Identifying the homomorphism](identifying-the-homomorphism.md) identifies \(\beta\) with restriction and proves Theorem 2.1.

## 3. Three results of Uchida and Hoshi

The following results are used in this course without proof. Their proofs, in the cited papers, rest on the reconstruction of decomposition groups of number fields from Galois groups, and are not given in this programme.

**(U1) Uchida's isomorphism theorem** [Uchida 1979, Theorem]. Let \(E_i/F_i\), \(i=1,2\), be Galois extensions of number fields with \(E_i\) solvably closed. Every isomorphism of topological groups \(\theta\colon\operatorname{Gal}(E_1/F_1)\to\operatorname{Gal}(E_2/F_2)\) is induced by a unique field isomorphism \(j\colon E_2\to E_1\), that is, \(g\circ j=j\circ\theta(g)\) for all \(g\).

**Lemma 3.1** ([OpenAI-UC, Lemma 2.3]). The only element of \(P\) commuting with every element of an open subgroup of \(P\) is \(1\).

*Proof.* An open subgroup of \(P\) is \(P_M\) for a number field \(M\subset\mathbb Q^s\), and \(\mathbb Q^s/M\) is Galois with \(\mathbb Q^s\) solvably closed (Proposition 1.3). Let \(c\in P\) commute with every \(h\in P_M\). Apply (U1) with \(E_1=E_2=\mathbb Q^s\), \(F_1=F_2=M\) and \(\theta\) the identity of \(P_M\). Both field isomorphisms \(j=c\) and \(j=\operatorname{id}\) satisfy \(h\circ j=j\circ h\) for all \(h\in P_M\). Uniqueness gives \(c=\operatorname{id}\). \(\square\)

For a finite prime \(v\) of a number field \(M\) and a chosen prime of \(\overline{\mathbb Q}\) above it, \(D_v\subset G_M\) and \(I_v\subset D_v\) denote the decomposition and inertia groups; another choice conjugates both. Decomposition and inertia groups in \(P_N\), for a number field \(N\subset\mathbb Q^s\), are defined with primes of \(\mathbb Q^s\). Pro-\(\ell\) Sylow subgroups are defined in Section 4.

**Definition 3.2.** Let \(M\) be a number field, \(N\subset\mathbb Q^s\) a number field, \(\varphi\colon G_M\to P_N\) an open homomorphism and \(\ell\) an odd prime. A finite prime \(v\nmid\ell\) of \(M\) is *active at \(\ell\)* (for \(\varphi\)) if \(\varphi\) is nontrivial on a pro-\(\ell\) Sylow subgroup of \(I_v\). By Proposition 4.1(2) all pro-\(\ell\) Sylow subgroups of \(I_v\) are conjugate in \(I_v\), and another choice of prime above \(v\) conjugates \(I_v\) in \(G_M\); so the condition does not depend on the choices.

**(U2) Uchida's partial local correspondence** [Uchida 1981, Section 1 and Proposition 1]; [OpenAI-UC, Theorem 2.4]. In the situation of Definition 3.2, every prime \(v\nmid\ell\) of \(M\) active at \(\ell\) determines a unique finite prime \(w\nmid\ell\) of \(N\) such that, for suitable choices of primes of \(\overline{\mathbb Q}\) above \(v\) and of \(\mathbb Q^s\) above \(w\),
\[
\varphi(D_v)\subset D_w .
\]
For these choices, \(\varphi\) is injective on every pro-\(\ell\) Sylow subgroup of \(I_v\) and maps it into \(I_w\). For each fixed \(\ell\), all but finitely many finite primes of \(N\) arise in this way from primes of \(M\) active at \(\ell\).

The pair \((v,w)\) is called an *active pair at \(\ell\)*. The same statement for a homomorphism from a local Galois group is [Hoshi 2026, Lemma 2.3]. The finite exceptional set in the last sentence depends on \(\ell\). The prime of \(\overline{\mathbb Q}\) above \(v\) may be chosen freely: another one is \(s\bar v\) with \(s\in G_M\), its decomposition group is \(sD_vs^{-1}\), and \(\varphi(sD_vs^{-1})\subseteq\varphi(s)D_w\varphi(s)^{-1}\), the decomposition group of another prime of \(\mathbb Q^s\) above the same \(w\).

**(H) Hoshi's criterion** [Hoshi 2025, Theorem 3.4], with the uniqueness [Uchida 1981, Proposition 2]. Let \(E_i/F_i\) be Galois extensions of number fields with \(E_i\) solvably closed, and let \(\alpha\colon\operatorname{Gal}(E_1/F_1)\to\operatorname{Gal}(E_2/F_2)\) be open. A field embedding \(E_2\to E_1\) inducing \(\alpha\) exists if and only if
\[
\begin{gathered}
\chi_{E_2/F_2}\circ\alpha=\chi_{E_1/F_1}\\
\text{as homomorphisms to }\widehat{\mathbb Z}^\times,
\end{gathered}
\]
and there is at most one such embedding.

## 4. Sylow subgroups of profinite groups

Let \(\ell\) be a prime. A profinite group is *pro-\(\ell\)* if all its finite continuous quotients have \(\ell\)-power order. A closed subgroup \(S\) of a profinite group \(G\) is a *pro-\(\ell\) Sylow subgroup* if for every open normal subgroup \(U\) the image \(SU/U\) is a Sylow \(\ell\)-subgroup of \(G/U\).

Three facts about a finite group \(F\) are used. (a) \(F\) has a Sylow \(\ell\)-subgroup (Judson, *Abstract Algebra: Theory and Applications*, Section 15.1, First Sylow Theorem, in the core course [Abstract Algebra II](https://kokunoyumeto.github.io/program-matematika-indonesia/en/#course-C40)). (b) If \(S\) is a Sylow \(\ell\)-subgroup and \(Q\) an \(\ell\)-subgroup, then \(Q\subset gSg^{-1}\) for some \(g\in F\): \(Q\) acts on \(F/S\) by left multiplication, its orbits have \(\ell\)-power sizes, and \(|F/S|\) is prime to \(\ell\), so some coset \(gS\) is fixed, which means \(g^{-1}Qg\subset S\). If \(Q\) is also Sylow, comparing orders gives \(Q=gSg^{-1}\). (c) If \(\psi\colon F\to F'\) is surjective, \(\psi(S)\) is a Sylow \(\ell\)-subgroup: its order is a power of \(\ell\), and \([F':\psi(S)]=[F:S\ker\psi]\) divides \([F:S]\), which is prime to \(\ell\).

**Proposition 4.1.** Let \(G\) be a profinite group and \(\ell\) a prime.

1. \(G\) has a pro-\(\ell\) Sylow subgroup, and every pro-\(\ell\) Sylow subgroup is pro-\(\ell\).
2. Every closed pro-\(\ell\) subgroup of \(G\) lies in a pro-\(\ell\) Sylow subgroup. Any two pro-\(\ell\) Sylow subgroups are conjugate in \(G\).
3. A continuous surjection \(\pi\colon G\to G'\) maps pro-\(\ell\) Sylow subgroups onto pro-\(\ell\) Sylow subgroups.
4. If \(G\) is abelian, it has exactly one pro-\(\ell\) Sylow subgroup. If \(N\subset G\) is a closed normal pro-\(p\) subgroup for a prime \(p\ne\ell\), every pro-\(\ell\) Sylow subgroup \(S\) of \(G\) meets \(N\) trivially and maps isomorphically onto a pro-\(\ell\) Sylow subgroup of \(G/N\).

*Proof.* We use that an inverse limit of nonempty finite sets over the directed set of open normal subgroups is nonempty, and that its projections are surjective when all transition maps are surjective; both follow from compactness of the product of the finite sets.

(1) For an open normal subgroup \(U\) let \(\Sigma_U\) be the finite nonempty set of Sylow \(\ell\)-subgroups of \(G/U\). For \(U'\subset U\), fact (c) maps \(\Sigma_{U'}\) to \(\Sigma_U\). Choose a compatible family \((S_U)\) and let \(S\) be the set of \(g\in G\) with \(gU\in S_U\) for all \(U\). It is a closed subgroup, equal to the inverse limit of the \(S_U\). The transition maps \(S_{U'}\to S_U\) are surjective, because the image of \(S_{U'}\) is a Sylow subgroup contained in, hence equal to, \(S_U\). So \(SU/U=S_U\). The quotients \(S/(S\cap U)\cong S_U\) are \(\ell\)-groups, and the subgroups \(S\cap U\) are cofinal among the open normal subgroups of \(S\); so \(S\) is pro-\(\ell\). The same argument applies to any pro-\(\ell\) Sylow subgroup.

(2) Let \(Q\) be closed pro-\(\ell\) and \(S\) pro-\(\ell\) Sylow. For each \(U\), the set \(C_U\) of \(x\in G/U\) with \(x^{-1}(QU/U)x\subset SU/U\) is nonempty by (b), since \(QU/U\) is a quotient of \(Q\) and hence an \(\ell\)-group. These sets are compatible under the projections, so some \(g\in G\) satisfies \(g^{-1}Qg\subset SU\) for all \(U\). As \(S\) is closed, \(S=\bigcap_USU\), so \(Q\subset gSg^{-1}\), a pro-\(\ell\) Sylow subgroup. If \(Q\) is itself pro-\(\ell\) Sylow, the images of \(Q\) and \(gSg^{-1}\) in each \(G/U\) are Sylow subgroups with one contained in the other, hence equal; two closed subgroups with the same images in all \(G/U\) coincide.

(3) For an open normal \(U'\subset G'\), \(U=\pi^{-1}(U')\) is open normal and \(G/U\cong G'/U'\); the image of \(S\) there is \(SU/U\), a Sylow subgroup. The image \(\pi(S)\) is compact, hence closed.

(4) In a finite abelian group a Sylow subgroup is normal, so by (b) it is the only one; the images of two pro-\(\ell\) Sylow subgroups therefore agree in every finite quotient, and the subgroups agree. For the second claim, \(S\cap N\) is a closed subgroup of the pro-\(\ell\) group \(S\) and of the pro-\(p\) group \(N\), so each of its finite quotients has order a power of \(\ell\) and of \(p\); it is trivial. By (3), the image of \(S\) in \(G/N\) is pro-\(\ell\) Sylow, and \(S\to SN/N\) is a continuous bijective homomorphism of compact groups, hence an isomorphism. \(\square\)

## 5. Local Galois groups inside the prosolvable closure

Let \(K\) be a nonarchimedean local field of residue characteristic \(p\) with algebraic closure \(\Omega\). We use the maximal unramified extension \(K^{\mathrm{ur}}\) and the maximal tame extension \(K^t\) of [Tame ramification and the tame Galois group](course:NT-LOC/NT-LOC-08), Proposition 2.2, and put
\[
\begin{aligned}
D&=\operatorname{Gal}(\Omega/K)\\
&\supset I=\operatorname{Gal}(\Omega/K^{\mathrm{ur}})\\
&\supset W=\operatorname{Gal}(\Omega/K^t).
\end{aligned}
\]

**Lemma 5.1.**

1. Every finite quotient of \(D\) is solvable, and \(W\) is pro-\(p\).
2. \(I/W\) is the tame inertia group \(I_t=\operatorname{Gal}(K^t/K^{\mathrm{ur}})\cong\prod_{\ell'\ne p}\mathbb Z_{\ell'}(1)\), and \(D/I\cong\widehat{\mathbb Z}\), generated by arithmetic Frobenius.
3. For a prime \(\ell\ne p\), every pro-\(\ell\) Sylow subgroup \(J\) of \(I\) meets \(W\) trivially and maps isomorphically onto the factor \(\mathbb Z_\ell(1)\) of \(I_t\). In particular \(J\cong\mathbb Z_\ell\).

*Proof.* (1) A finite quotient of \(D\) is \(\operatorname{Gal}(L/K)\) for a finite Galois \(L/K\), which is solvable by Corollary 2.2 of [Ramification groups and the different of a local extension](course:NT-LOC/NT-LOC-09). The image of \(W\) in \(\operatorname{Gal}(L/K)\) is \(\operatorname{Gal}(L/L\cap K^t)\). Let \(G_0\supset G_1\) be the inertia group and the first ramification group of \(L/K\); by that corollary \(G_1\) is a \(p\)-group and \(G_0/G_1\) has order prime to \(p\). The fixed field \(L^{G_1}\) has ramification index \(|G_0|/|G_1|\) over \(K\), because the inertia group of \(L/L^{G_1}\) is \(G_0\cap G_1=G_1\). That index is prime to \(p\), so \(L^{G_1}/K\) is tame and lies in \(K^t\) by Proposition 2.2 of the tame lesson. Hence \(\operatorname{Gal}(L/L\cap K^t)\subset G_1\) is a \(p\)-group.

(2) The first assertion is Theorem 3.1 of the tame lesson, and the second is the classification of unramified extensions used there, with Proposition 4.1 of the tame lesson.

(3) Apply Proposition 4.1(4) to \(G=I\), \(N=W\): \(J\) maps isomorphically onto a pro-\(\ell\) Sylow subgroup of the abelian group \(I_t\), which is the factor \(\mathbb Z_\ell(1)\). \(\square\)

For \(b\in\widehat{\mathbb Z}\) and \(c\) in a profinite abelian group, \(c^b\) is defined by continuity from the integer powers. If \(g\in D\) maps to \(\phi^b\) in \(D/I\), where \(\phi\) is arithmetic Frobenius, we call \(b=b(g)\) the *residue exponent* of \(g\).

**Lemma 5.2** (tame conjugation). Let \(q\) be the cardinality of the residue field of \(K\) and \(\ell\ne p\). For every \(g\in D\) and every \(t\) in a pro-\(\ell\) Sylow subgroup \(J\) of \(I\),
\[
g\,t\,g^{-1}\equiv t^{\,q^{b(g)}}\pmod W,
\]
where \(q^{b(g)}\) is computed in \(\mathbb Z_\ell^\times\) and acts on the pro-\(\ell\) group \(J\cong\mathbb Z_\ell\).

*Proof.* Work in \(D/W=\operatorname{Gal}(K^t/K)\) and write bars for images. For an element \(h\) of a profinite group, \(n\mapsto h^n\) extends uniquely to a continuous homomorphism from \(\widehat{\mathbb Z}\), since the group is the inverse limit of its finite quotients; this defines \(h^b\) for \(b\in\widehat{\mathbb Z}\). By Proposition 4.1 of the tame lesson, every lift \(\widetilde\phi\) of arithmetic Frobenius satisfies \(\widetilde\phi\,s\,\widetilde\phi^{-1}=s^q\) for \(s\in I_t\). Iterating, \(\widetilde\phi^{\,b}\,s\,\widetilde\phi^{-b}=s^{q^b}\) for integers \(b\ge0\), where \(q^b\) acts through \(\prod_{\ell'\ne p}\mathbb Z_{\ell'}^\times\). Both sides depend continuously on \(b\in\widehat{\mathbb Z}\), and the nonnegative integers are dense in \(\widehat{\mathbb Z}\), so the identity holds for all \(b\). Now \(\bar g=i\,\widetilde\phi^{\,b(g)}\) with \(i\in I_t\), because both sides have image \(\phi^{b(g)}\) in \(D/I\). Since \(I_t\) is abelian, \(\bar g\,\bar t\,\bar g^{-1}=\bar t^{\,q^{b(g)}}\). By Lemma 5.1(3), \(\bar t\) lies in the factor \(\mathbb Z_\ell(1)\), on which the exponent acts through its image in \(\mathbb Z_\ell^\times\), and \(J\to\mathbb Z_\ell(1)\) is an isomorphism. \(\square\)

**Proposition 5.3** ([OpenAI-UC, Section 2.3]). Let \(M\) be a number field, \(v\) a finite prime of \(M\), \(\bar v\) a prime of \(\overline{\mathbb Q}\) above \(v\), and \(\Omega\) an algebraic closure of the completion \(M_v\). The decomposition group of \(\bar v\) in \(G_M\) is isomorphic to \(\operatorname{Gal}(\Omega/M_v)\), compatibly with inertia groups. If \(M\subset\mathbb Q^s\) and \(\bar v^s\) is the prime of \(\mathbb Q^s\) below \(\bar v\), restriction maps the decomposition group of \(\bar v\) in \(G_M\) isomorphically onto the decomposition group of \(\bar v^s\) in \(P_M\).

*Proof.* The primes of \(\overline{\mathbb Q}\) above \(v\) are conjugate under \(G_M\), because the primes of each finite Galois extension of \(M\) above \(v\) are conjugate and the sets of conjugating elements are compatible closed subsets of the compact group \(G_M\). Conjugation preserves the assertion, so we may choose \(\bar v\): fix an embedding \(\iota\colon\overline{\mathbb Q}\to\Omega\) over \(M\), which exists because \(\overline{\mathbb Q}\) is algebraic over \(M\) and \(\Omega\) is algebraically closed, and let \(\bar v\) be the prime defined by the valuation of \(\Omega\). For a finite subextension \(L\) of \(\overline{\mathbb Q}/M\), the field \(\iota(L)M_v\subset\Omega\) is a finite extension of \(M_v\), complete, and contains \(\iota(L)\) as a dense subfield, so it is the completion of \(L\) at the prime below \(\bar v\). For finite Galois \(L/M\), Proposition 4.1 of [Places of number fields in extensions and the product formula](course:NT-LOC/NT-LOC-05) identifies the decomposition group at that prime with \(\operatorname{Gal}(\iota(L)M_v/M_v)\), compatibly with inertia. Passing to the inverse limit, the decomposition group of \(\bar v\) in \(G_M\) is \(\operatorname{Gal}(\iota(\overline{\mathbb Q})M_v/M_v)\); if \(M\subset\mathbb Q^s\), that of \(\bar v^s\) in \(P_M\) is \(\operatorname{Gal}(\iota(\mathbb Q^s)M_v/M_v)\), and restriction to \(\mathbb Q^s\) corresponds to restriction of automorphisms. Let \(Z\) be \(\overline{\mathbb Q}\), or \(\mathbb Q^s\) when \(M\subset\mathbb Q^s\), and \(U=\iota(Z)M_v\). It suffices to show \(U=\Omega\) in both cases.

First, \(U\) contains every root of unity of \(\Omega\), since \(X^n-1\) splits in \(\iota(Z)\). Second, every \(y\in U^\times\) has an \(n\)-th root in \(U\) for every \(n\ge1\). Indeed, \(y\) lies in \(\iota(L)M_v\) for a finite subextension \(L\) of \(Z/M\). By Newton lifting (Theorem 1.1 of [Hensel's lemma, squares and roots of unity in p-adic fields](course:NT-LOC/NT-LOC-03)), applied to \(X^n-u\) at \(X=1\), every \(u\) with \(|u-1|<|n|^2\) is an \(n\)-th power in \(\iota(L)M_v\). Since \(\iota(L)\) is dense there, choose \(x\in\iota(L)^\times\) with \(|y/x-1|<|n|^2\). The field \(Z\) is closed under \(n\)-th roots (trivially for \(\overline{\mathbb Q}\), by Proposition 1.3(1) for \(\mathbb Q^s\)), so \(x=z^n\) with \(z\in\iota(Z)\subset U\). So \(y=z^n(y/x)\) is an \(n\)-th power in \(U\).

By the Kummer correspondence, as in Proposition 1.3(1), \(U\) has no nontrivial abelian extension of prime exponent inside \(\Omega\), hence no nontrivial finite abelian extension there. Let \(U'\subset\Omega\) be a finite Galois extension of \(U\), say \(U'=U(\theta)\), and let \(L''\) be the Galois closure of \(M_v(\theta)\) over \(M_v\) in \(\Omega\). Then \(\operatorname{Gal}(UL''/U)\) is isomorphic to a subgroup of \(\operatorname{Gal}(L''/M_v)\) by restriction, which is solvable by Lemma 5.1(1), and \(\operatorname{Gal}(U'/U)\) is a quotient of it. A nontrivial finite solvable group has a nontrivial abelian quotient, which would give a nontrivial finite abelian extension of \(U\). So \(U'=U\). Every finite extension of \(U\) in \(\Omega\) lies in a finite Galois one, so \(U=\Omega\). Inertia groups correspond because they are the kernels of the actions on the common residue field. \(\square\)

So decomposition groups in \(P_M\) are absolute Galois groups of local fields, and Lemmas 5.1 and 5.2 apply to them, with inertia, wild inertia and residue exponents defined through Proposition 5.3.

## 6. The norm identity

Let \(M\) be a number field, \(N\subset\mathbb Q^s\) a number field, \(\varphi\colon G_M\to P_N\) open, \(\ell\) an odd prime, and \((v,w)\) an active pair at \(\ell\), with the choices of (U2), so that \(\varphi(D_v)\subset D_w\). For \(g\in D_v\), let \(b(g)\in\widehat{\mathbb Z}\) be its residue exponent at \(v\), and let \(a(g)\in\widehat{\mathbb Z}\) be the residue exponent of \(\varphi(g)\in D_w\) at \(w\). Write \(Nv\) for the absolute norm of \(v\), the cardinality of its residue field.

**Lemma 6.1** (norm identity; [OpenAI-UC, Lemma 2.6]). For every \(g\in D_v\),
\[
(Nv)^{b(g)}=(Nw)^{a(g)}\quad\text{in }\mathbb Z_\ell^\times .
\]

*Proof.* Let \(p\) and \(p'\) be the residue characteristics of \(v\) and \(w\); both differ from \(\ell\) by (U2). Let \(\tau\) generate a pro-\(\ell\) Sylow subgroup \(J\) of \(I_v\), and put \(c=(Nv)^{b(g)}\in\mathbb Z_\ell^\times\). By Lemma 5.2,
\[
e:=g\tau g^{-1}\tau^{-c}\in W_v,
\]
the wild inertia group at \(v\), which is pro-\(p\) by Lemma 5.1. By (U2), \(\varphi(\tau)\in I_w\), and \(\varphi\) is injective on \(J\). Since \(I_w\) is normal in \(D_w\) and \(\varphi(g)\in D_w\), also \(\varphi(g\tau g^{-1})\in I_w\), and so \(\varphi(e)\in I_w\).

Consider the images in the tame inertia group \(I_w/W_w\cong\prod_{\ell'\ne p'}\mathbb Z_{\ell'}(1)\). The images of \(\varphi(\tau)\) and of \(\varphi(g\tau g^{-1})=\varphi(g)\varphi(\tau)\varphi(g)^{-1}\) lie in the factor \(\mathbb Z_\ell(1)\), because they generate pro-\(\ell\) subgroups of this abelian group, and its pro-\(\ell\) Sylow subgroup is that factor. So the image of \(\varphi(e)\) lies in \(\mathbb Z_\ell(1)\). The closed subgroup generated by \(\varphi(e)\) lies in \(\varphi(W_v)\), so it is pro-\(p\), and so is its image. A pro-\(p\) subgroup of \(\mathbb Z_\ell(1)\cong\mathbb Z_\ell\) is trivial because \(p\ne\ell\). Hence \(\varphi(e)\in W_w\), that is,
\[
\varphi(g)\varphi(\tau)\varphi(g)^{-1}\equiv\varphi(\tau)^{c}\pmod{W_w}.
\]
On the other hand, \(\varphi(J)\) is a pro-\(\ell\) subgroup of \(I_w\), contained in a pro-\(\ell\) Sylow subgroup of \(I_w\) by Proposition 4.1(2). Lemma 5.2 at \(w\), applied to \(\varphi(g)\in D_w\) and \(t=\varphi(\tau)\), gives
\[
\begin{gathered}
\varphi(g)\varphi(\tau)\varphi(g)^{-1}\equiv\varphi(\tau)^{c'}\pmod{W_w},\\
c'=(Nw)^{a(g)} .
\end{gathered}
\]
The image of \(\varphi(\tau)\) in \(I_w/W_w\) is nontrivial: \(\varphi(J)\cong\mathbb Z_\ell\) is pro-\(\ell\) and \(W_w\) is pro-\(p'\) with \(p'\ne\ell\), so \(\varphi(J)\cap W_w=1\). It lies in \(\mathbb Z_\ell(1)\cong\mathbb Z_\ell\), which is torsion-free; so \(\varphi(\tau)^{c}=\varphi(\tau)^{c'}\) there forces \(c=c'\). \(\square\)

The residue exponent \(a(g)\) is defined on all of \(D_v\) through \(\varphi\); no assumption that \(\varphi\) maps all of \(I_v\) into \(I_w\) is needed.

## 7. Exercises

**7.1.** Show that \(P\) has no nontrivial finite normal subgroup.

**7.2.** Let \(\mathbb Q^{\mathrm{ab}}\) be the maximal abelian extension of \(\mathbb Q\) in \(\overline{\mathbb Q}\). Show that \(\mathbb Q^{\mathrm{ab}}(2^{1/3})\) is a cyclic extension of \(\mathbb Q^{\mathrm{ab}}\) of degree \(3\), so \(\mathbb Q^{\mathrm{ab}}\) is not solvably closed.

**7.3.** Show that the cyclotomic character \(\chi_{\mathbb Q^s/\mathbb Q}\colon P\to\widehat{\mathbb Z}^\times\) is surjective.

**7.4.** Let \(M\subset\mathbb Q^s\) be a number field and \(\varphi\colon G_M\to P_M\) the restriction. Show that for every odd \(\ell\) every finite prime \(v\nmid\ell\) of \(M\) is active at \(\ell\), and that the norm identity holds with \(w=v\) and \(a(g)=b(g)\).

**7.5.** Let \(G=\widehat{\mathbb Z}\) and \(G=\mathbb Z_p^\times\) for an odd prime \(p\). Determine the pro-\(\ell\) Sylow subgroups for every prime \(\ell\).

## 8. Solutions

**7.1.** Let \(F\) be a finite normal subgroup. Conjugation gives a homomorphism \(P\to\operatorname{Aut}(F)\); its kernel, the centralizer \(C\) of \(F\), has finite index and is closed, hence open. Every element of \(F\) commutes with every element of \(C\), so Lemma 3.1 gives \(F=1\).

**7.2.** The field \(\mathbb Q^{\mathrm{ab}}\) contains \(\mu_3\), so by the Kummer correspondence \(\mathbb Q^{\mathrm{ab}}(2^{1/3})\) is cyclic of degree \(1\) or \(3\) over it. If \(2^{1/3}\in\mathbb Q^{\mathrm{ab}}\), then \(\mathbb Q(2^{1/3})\) would lie in a finite abelian extension of \(\mathbb Q\), and every subfield of such an extension is Galois over \(\mathbb Q\). But \(\mathbb Q(2^{1/3})\) is not Galois over \(\mathbb Q\): it is real, and does not contain the nonreal roots of \(X^3-2\).

**7.3.** The cyclotomic polynomials are irreducible over \(\mathbb Q\) ([Cyclotomic polynomials and their automorphisms](course:NT-CFT/cyclotomic-polynomials-and-their-automorphisms)), so \(\operatorname{Gal}(\mathbb Q(\mu_n)/\mathbb Q)\cong(\mathbb Z/n\mathbb Z)^\times\). The fields \(\mathbb Q(\mu_n)\) lie in \(\mathbb Q^s\), and restriction \(P\to\operatorname{Gal}(\mathbb Q(\mu_\infty)/\mathbb Q)\cong\widehat{\mathbb Z}^\times\) is surjective because restriction of Galois groups to a Galois subextension is surjective.

**7.4.** By Proposition 5.3, restriction is injective on \(D_v\), so it is nontrivial on every pro-\(\ell\) Sylow subgroup of \(I_v\), which is isomorphic to \(\mathbb Z_\ell\) by Lemma 5.1. With the prime of \(\mathbb Q^s\) below the chosen prime of \(\overline{\mathbb Q}\), restriction maps \(D_v\) onto the decomposition group of \(v\) in \(P_M\), so \(w=v\) satisfies \(\varphi(D_v)\subset D_w\), and by uniqueness in (U2) it is the prime attached to \(v\). Residue exponents are computed on the common residue field, so \(a(g)=b(g)\), and the identity reads \((Nv)^{b}=(Nv)^{b}\).

**7.5.** \(\widehat{\mathbb Z}=\prod_{\ell}\mathbb Z_\ell\) is abelian, and its unique pro-\(\ell\) Sylow subgroup is the factor \(\mathbb Z_\ell\): its image in each finite quotient \(\mathbb Z/n\mathbb Z\) is the \(\ell\)-primary part. For odd \(p\), \(\mathbb Z_p^\times\cong\mu_{p-1}\times(1+p\mathbb Z_p)\) with \(1+p\mathbb Z_p\cong\mathbb Z_p\) (Proposition 2.1 and Theorem 3.1 of [The multiplicative group of a local field](course:NT-LOC/NT-LOC-11)). Its pro-\(p\) Sylow subgroup is \(1+p\mathbb Z_p\), and for \(\ell\ne p\) it is the \(\ell\)-primary part of \(\mu_{p-1}\).

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Sections 1 and 2. https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
- [Uchida 1979] K. Uchida, *Isomorphisms of Galois groups of solvably closed Galois extensions*, Tôhoku Math. J. (2) 31 (1979), 359–362. https://doi.org/10.2748/tmj/1178229803
- [Uchida 1981] K. Uchida, *Homomorphisms of Galois groups of solvably closed Galois extensions*, J. Math. Soc. Japan 33 (1981), 595–604. https://doi.org/10.2969/jmsj/03340595
- [Hoshi 2025] Y. Hoshi, *Homomorphisms of global solvably closed Galois groups compatible with cyclotomic characters*, Tôhoku Math. J. (2) 77 (2025), 17–32; preprint RIMS-1955 (2021), https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1955.pdf
- [Hoshi 2026] Y. Hoshi, *A note on open homomorphisms between global solvably closed Galois groups*, Kodai Math. J. 49 (2026), 63–79; preprint RIMS-1977 (2023), https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1977.pdf
- T. W. Judson, *Abstract Algebra: Theory and Applications*, Chapter 15 (The Sylow Theorems), in the core course Abstract Algebra II.
