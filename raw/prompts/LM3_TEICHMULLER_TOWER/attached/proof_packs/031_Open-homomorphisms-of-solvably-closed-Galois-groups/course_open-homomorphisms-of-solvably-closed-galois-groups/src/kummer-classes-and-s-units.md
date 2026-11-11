# Kummer classes and S-units

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

The next lesson bounds the number of primes that the partial local correspondence misses. A missed prime \(w\) of the target field gives an element \(a_w\) generating a power of \(w\), and the compatible \(\ell\)-power roots of \(a_w\) give a cohomology class. Pulled back along the homomorphism to the Galois group of the domain field, these classes are unramified away from \(\ell\), and such classes are counted by \(S\)-units. This lesson provides the tools: first cohomology with \(\ell\)-adic coefficients, Kummer theory for the \(\ell\)-adic Tate twist, the relation between ramification of a Kummer class and valuations, the identification of classes unramified outside \(S\) with \(S\)-units, and the character of the \(S\)-unit group as a Galois representation.

- First cohomology (Section 1).
- \(\ell\)-adic Kummer theory (Section 2).
- Valuations and unramified classes (Section 3).
- The equivariant \(S\)-unit theorem (Section 4).

## 1. First cohomology

Let \(G\) be a profinite group and \(A\) a Hausdorff topological abelian group with a continuous action of \(G\). A *cocycle* is a continuous map \(c\colon G\to A\) with \(c(gh)=c(g)+g\,c(h)\); a *coboundary* is a cocycle \(g\mapsto ga-a\) with \(a\in A\). The quotient of the group of cocycles by the coboundaries is \(H^1(G,A)\). A continuous homomorphism \(\varphi\colon G'\to G\) makes \(A\) a \(G'\)-module and induces \(\varphi^*\colon H^1(G,A)\to H^1(G',A)\), \(c\mapsto c\circ\varphi\); for an inclusion this is *restriction*. A cocycle satisfies \(c(1)=0\) and \(g\,c(g^{-1})=-c(g)\).

Fix a prime \(\ell\). For a field \(F\) of characteristic \(0\) with algebraic closure \(\overline F\), let \(\mathbb Z_\ell(1)=\varprojlim_n\mu_{\ell^n}\), with transition maps \(\zeta\mapsto\zeta^\ell\), and \(\mathbb Q_\ell(1)=\mathbb Z_\ell(1)\otimes_{\mathbb Z_\ell}\mathbb Q_\ell\); the group \(G_F=\operatorname{Gal}(\overline F/F)\) acts on them through the \(\ell\)-adic cyclotomic character \(\chi_{F,\ell}\). For a continuous character \(\rho\colon G\to\mathbb Z_\ell^\times\), \(\mathbb Q_\ell(\rho)\) denotes \(\mathbb Q_\ell\) with \(g\) acting as multiplication by \(\rho(g)\).

**Lemma 1.1.**

1. If \(\varphi\colon G'\to G\) is surjective, \(\varphi^*\) is injective.
2. If \(H\subseteq G\) is an open normal subgroup and \(A\) is a \(\mathbb Q_\ell\)-vector space with a continuous linear action, restriction \(H^1(G,A)\to H^1(H,A)\) is injective.
3. If \(H\subseteq G\) is a closed subgroup acting trivially on \(A\), the restriction of a class to \(H\) is a well-defined continuous homomorphism \(H\to A\).

*Proof.* (1) If \(c(\varphi(g'))=\varphi(g')a-a\) for all \(g'\), surjectivity gives \(c(g)=ga-a\). (2) Suppose \(c|_H\) is the coboundary of \(a\); replacing \(c\) by \(c-(g\mapsto ga-a)\), we may assume \(c|_H=0\). Then \(c(gh)=c(g)\) for \(h\in H\), and \(c(hg)=c(g\cdot g^{-1}hg)=c(g)\), while also \(c(hg)=h\,c(g)\). So \(c\) is a cocycle of the finite group \(\Delta=G/H\) with values in \(A^H\). Summing \(c(gd)=c(g)+g\,c(d)\) over \(d\in\Delta\) gives \(c(g)=ga'-a'\) with \(a'=-|\Delta|^{-1}\sum_dc(d)\). (3) Coboundaries vanish on \(H\), and \(c(hh')=c(h)+h\,c(h')=c(h)+c(h')\). \(\square\)

If \(H\) is a closed normal subgroup of \(G\) and \(A\) a \(G\)-module, \(G\) acts on \(H^1(H,A)\) by
\[
\begin{gathered}
(t*c)(h)=t\,c(t^{-1}ht)\\
(t\in G,\ h\in H).
\end{gathered}
\]
For \(t\in H\), the cocycle identity gives \(t\,c(t^{-1}ht)=c(h)+h\,c(t)-c(t)\), so \(H\) acts trivially on classes and \(G/H\) acts.

**Lemma 1.2** (twisted restriction). Let \(H\subseteq G\) be open and normal, \(\rho,\chi\colon G\to\mathbb Z_\ell^\times\) continuous characters that agree on \(H\), and \(\varepsilon=\rho\chi^{-1}\), a character of \(G/H\). For a cocycle \(c\colon G\to\mathbb Q_\ell(\rho)\), the restriction \(c|_H\) is a cocycle for the \(H\)-module \(\mathbb Q_\ell(\chi)\), and for the action \(*\) of \(G\) on \(H^1(H,\mathbb Q_\ell(\chi))\),
\[
t*[c|_H]=\varepsilon(t)^{-1}[c|_H]\qquad(t\in G).
\]

*Proof.* The cocycle identity in \(\mathbb Q_\ell(\rho)\) and \(c(t^{-1})=-\rho(t)^{-1}c(t)\) give
\[
\begin{aligned}
&c(t^{-1}ht)\\
&\quad=\rho(t)^{-1}\bigl(c(h)+\rho(h)c(t)-c(t)\bigr).
\end{aligned}
\]
Multiplying by \(\chi(t)\),
\[
\begin{aligned}
&(t*c|_H)(h)\\
&\quad=\varepsilon(t)^{-1}\bigl(c(h)+h\,c(t)-c(t)\bigr),
\end{aligned}
\]
since \(h\in H\) acts on both modules through \(\rho(h)=\chi(h)\). The bracket differs from \(c(h)\) by a coboundary. \(\square\)

## 2. \(\ell\)-adic Kummer theory

Let \(F\) be a field of characteristic \(0\). For \(a\in F^\times\) and \(n\ge1\), choose \(\alpha\in\overline F\) with \(\alpha^{\ell^n}=a\); the map \(g\mapsto g(\alpha)/\alpha\) is a cocycle \(G_F\to\mu_{\ell^n}\), written multiplicatively, and its class does not depend on \(\alpha\).

**Lemma 2.1** (Kummer theory). This defines an isomorphism \(F^\times/F^{\times\ell^n}\to H^1(G_F,\mu_{\ell^n})\). It is compatible with the maps \(F^\times/F^{\times\ell^{n+1}}\to F^\times/F^{\times\ell^n}\) and \(\mu_{\ell^{n+1}}\to\mu_{\ell^n}\), \(\zeta\mapsto\zeta^\ell\).

*Proof.* It is a homomorphism, and its kernel consists of the \(a\) for which \(g(\alpha)/\alpha=g(\zeta)/\zeta\) with \(\zeta\in\mu_{\ell^n}\), that is, \(\alpha/\zeta\in F\) and \(a=(\alpha/\zeta)^{\ell^n}\in F^{\times\ell^n}\). For surjectivity, let \(c\) be a cocycle. Its restriction to the open subgroup \(G_{F(\mu_{\ell^n})}\), which acts trivially on \(\mu_{\ell^n}\), is a homomorphism with open kernel, so \(c\) factors through \(\operatorname{Gal}(E/F)\) for a finite Galois \(E/F\). By Hilbert's Theorem 90 (Theorem 3.1 of [Hilbert's Theorem 90 and Kummer theory](course:NT-CFT/hilberts-theorem-90-and-kummer-theory)), as a cocycle with values in \(E^\times\) it has the form \(g(\alpha)/\alpha\) with \(\alpha\in E^\times\); then \(\alpha^{\ell^n}\) is fixed by \(\operatorname{Gal}(E/F)\), so it lies in \(F^\times\), and \(c\) is its Kummer cocycle. For compatibility, \(\alpha^\ell\) is an \(\ell^n\)-th root of \(a\) when \(\alpha^{\ell^{n+1}}=a\), and \((g(\alpha)/\alpha)^\ell=g(\alpha^\ell)/\alpha^\ell\). \(\square\)

Let \(\widehat{F^\times}=\varprojlim_nF^\times/F^{\times\ell^n}\), a \(\mathbb Z_\ell\)-module.

**Proposition 2.2.** Kummer theory induces isomorphisms
\[
\begin{gathered}
\kappa\colon\widehat{F^\times}\xrightarrow{\ \sim\ }H^1(G_F,\mathbb Z_\ell(1)),\\
\widehat{F^\times}\otimes_{\mathbb Z_\ell}\mathbb Q_\ell\xrightarrow{\ \sim\ }H^1(G_F,\mathbb Q_\ell(1)).
\end{gathered}
\]
They are compatible with field isomorphisms: for an isomorphism \(g\colon F\to F'\) extended to \(\tilde g\colon\overline F\to\overline{F'}\), \(\kappa(g(a))(h)=\tilde g\,\kappa(a)(\tilde g^{-1}h\tilde g)\).

*Proof.* A continuous cocycle \(c\colon G_F\to\mathbb Z_\ell(1)\) reduces to cocycles \(c_n\) with values in \(\mu_{\ell^n}\). Conversely, let \(([c_n])_n\) be compatible classes. The cocycles representing \([c_n]\) form a finite nonempty set \(\Sigma_n\) (they differ by coboundaries of elements of \(\mu_{\ell^n}\)), and reduction maps \(\Sigma_{n+1}\) to \(\Sigma_n\). An inverse limit of nonempty finite sets is nonempty, so there are compatible representatives, which define a continuous cocycle into \(\mathbb Z_\ell(1)\). If all reductions of \(c\) are coboundaries, the sets of \(m_n\in\mu_{\ell^n}\) with \(c_n(g)=g(m_n)/m_n\) are finite, nonempty and compatible, so \(c\) is a coboundary. Hence \(H^1(G_F,\mathbb Z_\ell(1))=\varprojlim H^1(G_F,\mu_{\ell^n})\), and Lemma 2.1 gives \(\kappa\).

For \(\mathbb Q_\ell(1)\): a cocycle into \(\mathbb Q_\ell(1)\) has compact image, so some multiple \(\ell^Nc\) takes values in \(\mathbb Z_\ell(1)\); and an integral cocycle that is the coboundary of \(m\in\mathbb Q_\ell(1)\) has a multiple \(\ell^Nc\), with \(\ell^Nm\in\mathbb Z_\ell(1)\), that is an integral coboundary. So \(H^1(G_F,\mathbb Q_\ell(1))=H^1(G_F,\mathbb Z_\ell(1))\otimes\mathbb Q_\ell\). The compatibility follows from \(\tilde g(\alpha)^{\ell^n}=g(a)\) and \(h(\tilde g\alpha)/\tilde g\alpha=\tilde g\bigl((\tilde g^{-1}h\tilde g)(\alpha)/\alpha\bigr)\). \(\square\)

## 3. Valuations and unramified classes

Let \(F\) be a number field and \(v\) a finite prime of residue characteristic \(p\ne\ell\). The valuation \(\operatorname{ord}_v\colon F^\times\to\mathbb Z\) induces maps \(F^\times/F^{\times\ell^n}\to\mathbb Z/\ell^n\mathbb Z\) and in the limit \(\widehat{\operatorname{ord}}_v\colon\widehat{F^\times}\to\mathbb Z_\ell\). By Proposition 5.3 of [Solvably closed fields and Uchida's conjecture](solvably-closed-fields-and-uchidas-conjecture.md), the decomposition group \(D_v\subseteq G_F\) is the absolute Galois group of \(F_v\), with inertia group \(I_v\). The inertia group acts trivially on \(\mathbb Z_\ell(1)\), because the roots of unity of order prime to \(p\) generate unramified extensions. Let
\[
t_v\colon I_v\longrightarrow\mathbb Z_\ell(1)
\]
be the tame character: the composite of \(I_v\to\operatorname{Gal}(F_v^t/F_v^{\mathrm{ur}})\) with the projection of the canonical isomorphism of Theorem 3.1 of [Tame ramification and the tame Galois group](course:NT-LOC/NT-LOC-08) to its \(\ell\)-component, \(\sigma\mapsto(\sigma(\pi_{\ell^n})/\pi_{\ell^n})_n\) for compatible roots \(\pi_{\ell^n}\) of a uniformizer \(\pi\). It is surjective.

**Lemma 3.1.** For \(a\in\widehat{F^\times}\), the restriction of \(\kappa(a)\) to \(I_v\) is the homomorphism \(\widehat{\operatorname{ord}}_v(a)\,t_v\). So \(\kappa(a)\) vanishes on \(I_v\) if and only if \(\widehat{\operatorname{ord}}_v(a)=0\); the same holds for classes with coefficients in \(\mathbb Q_\ell(1)\).

*Proof.* By Lemma 1.1(3) the restriction is a well-defined homomorphism, so it may be computed with any cocycles. At level \(n\) let \(a_n\in F^\times\) represent \(a\), and write \(a_n=\pi^eu\) in \(F_v\) with \(e=\operatorname{ord}_v(a_n)\) and \(u\) a unit. By Lemma 2.1 of the tame lesson, \(u\) has an \(\ell^n\)-th root \(\beta\) in the maximal unramified extension, which inertia fixes. With \(\alpha=\pi_{\ell^n}^e\beta\), every \(\sigma\in I_v\) satisfies \(\sigma(\alpha)/\alpha=(\sigma(\pi_{\ell^n})/\pi_{\ell^n})^e\). With compatible choices the levels fit together, giving \(\widehat{\operatorname{ord}}_v(a)\,t_v\). As \(t_v\) is surjective onto the torsion-free group \(\mathbb Z_\ell(1)\), the restriction vanishes exactly when \(\widehat{\operatorname{ord}}_v(a)=0\). For rational classes multiply by a power of \(\ell\). \(\square\)

A class is *unramified at \(v\)* if its restriction to \(I_v\) vanishes. Let \(S\) be a finite set of places of \(F\) containing the archimedean places and the primes above \(\ell\), and let \(\mathcal O_{F,S}^\times\) be the group of \(S\)-units, finitely generated by the \(S\)-unit theorem (Theorem 9.4 of [Dirichlet's unit theorem](course:NT-ANT/dirichlets-unit-theorem)).

**Proposition 3.2** ([OpenAI-UC, Lemma 5.2]). Kummer theory induces an isomorphism
\[
\begin{aligned}
&\mathcal O_{F,S}^\times\otimes_{\mathbb Z}\mathbb Q_\ell\\
&\quad\xrightarrow{\ \sim\ }\{c\in H^1(G_F,\mathbb Q_\ell(1)):\\
&\qquad\quad c\text{ is unramified at every}\\
&\qquad\quad\text{finite }v\notin S\}.
\end{aligned}
\]
It is compatible with the automorphisms of \(F\) that preserve \(S\).

*Proof.* By Proposition 2.2 and Lemma 3.1 it suffices to identify the subgroup of all \(a\in\widehat{F^\times}\) with \(\widehat{\operatorname{ord}}_v(a)=0\) for all finite \(v\notin S\), which is \(\varprojlim_nH_n\) with
\[
\begin{aligned}
H_n=\{&[a]\in F^\times/F^{\times\ell^n}:\\
&\operatorname{ord}_v(a)\equiv0\pmod{\ell^n}\\
&\text{for every finite }v\notin S\}.
\end{aligned}
\]
Write \(U_S=\mathcal O_{F,S}^\times\) and \(\operatorname{Cl}_S\) for the \(S\)-class group, a quotient of the finite class group. There is an exact sequence
\[
0\to U_S/U_S^{\ell^n}\to H_n\to\operatorname{Cl}_S[\ell^n]\to0 .
\]
The second map sends \([a]\) to the class of the \(S\)-ideal \(\mathfrak b\) with \(\mathfrak b^{\ell^n}=(a)_S\), the part of \((a)\) away from \(S\); changing \(a\) by an \(\ell^n\)-th power \(c^{\ell^n}\) changes \(\mathfrak b\) by the principal ideal \((c)_S\). It is onto, since \(\mathfrak b^{\ell^n}=(a)_S\) for some \(a\) whenever the class of \(\mathfrak b\) is killed by \(\ell^n\). If \(\mathfrak b=(c)_S\), then \(ac^{-\ell^n}\in U_S\), which gives exactness in the middle. The first map is injective: if \(u\in U_S\) equals \(c^{\ell^n}\) with \(c\in F^\times\), then \(\operatorname{ord}_v(c)=0\) for \(v\notin S\), so \(c\in U_S\).

From level \(n+1\) to level \(n\), the map on the last terms is multiplication by \(\ell\), since \(\mathfrak b_n=\mathfrak b_{n+1}^\ell\). An element \((x_n)\) of the inverse limit satisfies \(x_n=\ell^kx_{n+k}\) for all \(k\), and \(\ell^k\) kills the finite group \(\operatorname{Cl}_S[\ell^\infty]\) for \(k\) large; so the limit of the last terms is \(0\). Inverse limits of exact sequences of finite groups are exact, by the same compactness argument as above. So \(\varprojlim H_n=\varprojlim U_S/U_S^{\ell^n}=U_S\otimes\mathbb Z_\ell\), since \(U_S\) is finitely generated. Rationalizing gives the assertion. The constructions commute with automorphisms preserving \(S\) by Proposition 2.2. \(\square\)

A Kummer class \(\kappa(a)\) of \(a\in F^\times\) is unramified at every finite \(v\nmid\ell\) where \(a\) is a unit, by Lemma 3.1. If \(F\subseteq\mathbb Q^s\), it factors through \(P_F\): the field \(\mathbb Q^s\) contains all roots of unity and all \(\ell\)-power roots of \(a\) (Proposition 1.3 of the first lesson), so the Kummer cocycles may be computed with roots in \(\mathbb Q^s\), and \(\operatorname{Gal}(\overline{\mathbb Q}/\mathbb Q^s)\) fixes them.

## 4. The equivariant \(S\)-unit theorem

Let \(K'/K\) be a finite Galois extension of number fields with group \(\Delta\), and \(S\) a finite \(\Delta\)-stable set of places of \(K'\) containing the archimedean places. Representations of \(\Delta\) over \(\mathbb Q_\ell\) are determined by their characters, as explained in Section 5 of [Additive characters and Frobenius detection](additive-characters-and-frobenius-detection.md).

**Proposition 4.1.** As \(\mathbb Q_\ell[\Delta]\)-modules,
\[
\bigl(\mathcal O_{K',S}^\times\otimes\mathbb Q_\ell\bigr)\oplus\mathbb Q_\ell\cong\mathbb Q_\ell[S],
\]
the permutation module on \(S\). Consequently, for a character \(\phi\colon\Delta\to\mathbb Q_\ell^\times\), the \(\phi\)-eigenspace of \(\mathcal O_{K',S}^\times\otimes\mathbb Q_\ell\) has dimension at most the number of \(\Delta\)-orbits on \(S\).

*Proof.* The \(S\)-logarithmic map \(\varepsilon\mapsto(\log\|\varepsilon\|_w)_{w\in S}\), with the normalized absolute values, is \(\Delta\)-equivariant, has finite kernel, and by Theorem 9.4 of the unit theorem lesson its image is a lattice spanning the hyperplane of vectors with coordinate sum \(0\), an invariant complement of the line of constant vectors. Comparing traces over \(\mathbb R\), as in Lemma 5.2 of the character lesson, proves the isomorphism. The permutation module is the direct sum over orbits of modules \(\mathbb Q_\ell[\Delta/\Delta_o]\), the functions on \(\Delta/\Delta_o\) with \((hf)(x)=f(h^{-1}x)\). A \(\phi\)-eigenvector satisfies \(f(h^{-1}x)=\phi(h)f(x)\), so \(f(g\Delta_o)=\phi(g)^{-1}f(\Delta_o)\) is determined by its value at the coset \(\Delta_o\); each orbit contributes at most one dimension. Eigenspaces of the summand \(\mathcal O_{K',S}^\times\otimes\mathbb Q_\ell\) are at most those of the sum. \(\square\)

When \(S\) consists of the archimedean places and the primes above \(\ell\), the \(\Delta\)-orbits on \(S\) correspond to the archimedean places and the primes above \(\ell\) of \(K\), whose number is at most \(r_1(K)+r_2(K)+[K:\mathbb Q]\le2[K:\mathbb Q]\).

## 5. Exercises

**5.1.** Let \(F=\mathbb Q\) and \(S=\{\infty,\ell\}\). Show that the classes in \(H^1(G_{\mathbb Q},\mathbb Q_\ell(1))\) unramified outside \(S\) form a line spanned by the Kummer class of \(\ell\).

**5.2.** For a prime \(p\ne\ell\), show that the Kummer class of \(p\) restricted to the inertia group at \(p\) is the tame character, and that the Kummer class of \(-1\) vanishes in \(H^1(G_{\mathbb Q},\mathbb Q_\ell(1))\).

**5.3.** Let \(\Delta\) be finite and \(A\) a \(\mathbb Q_\ell\)-vector space with a linear \(\Delta\)-action. Show that every cocycle \(\Delta\to A\) is a coboundary.

**5.4.** Let \(K'/K\) be quadratic with group \(\Delta=\{1,\sigma\}\) and \(\phi\) the nontrivial character. Show that the \(\phi\)-eigenspace of \(\mathcal O_{K'}^\times\otimes\mathbb Q_\ell\) has dimension \(r_1(K')+r_2(K')-r_1(K)-r_2(K)\), the difference of the unit ranks.

**5.5.** In Lemma 1.2, take \(G=H\), \(\rho=\chi\). What does the lemma say?

## 6. Solutions

**5.1.** \(\mathcal O_{\mathbb Q,S}^\times=\{\pm\ell^k\}\), so \(\mathcal O_{\mathbb Q,S}^\times\otimes\mathbb Q_\ell\) is a line spanned by \(\ell\otimes1\), and Proposition 3.2 applies.

**5.2.** \(\operatorname{ord}_p(p)=1\), so Lemma 3.1 gives \(t_p\). The class of \(-1\) is killed by \(2\) in \(\widehat{\mathbb Q^\times}\), hence is \(0\) after tensoring with \(\mathbb Q_\ell\).

**5.3.** This is the last step of the proof of Lemma 1.1(2): \(c(g)=ga'-a'\) with \(a'=-|\Delta|^{-1}\sum_dc(d)\).

**5.4.** The archimedean places of \(K\) that split in \(K'\) give orbits of size \(2\), each contributing \(\mathbf 1\oplus\phi\) to \(\mathbb Q_\ell[S]\); the others give \(\mathbf 1\). So \(\phi\) has multiplicity equal to the number of split places, which is \((r_1(K')+r_2(K'))-(r_1(K)+r_2(K))\), and by Proposition 4.1 this is its multiplicity in \(\mathcal O_{K'}^\times\otimes\mathbb Q_\ell\).

**5.5.** Then \(\varepsilon=1\), and the lemma says that \(G\) acts trivially on \(H^1(G,A)\) by conjugation.

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Section 5.1 (Lemma 5.2). https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
