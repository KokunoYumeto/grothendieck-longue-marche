# Identifying the homomorphism

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

This lesson turns the prime correspondence of [Matching residue characteristics](matching-residue-characteristics.md) into an equality of homomorphisms. For one fixed coefficient prime \(r\), the additive characters pulled back along the normalized map \(\beta\) and along ordinary restriction agree at the Frobenius elements of infinitely many primes of degree one, hence agree. The character space is a faithful representation of finite quotients of \(P\), so the two homomorphisms agree modulo every finite quotient after a conjugation, and compactness gives one conjugation for all quotients. Removing the normalizer extension proves that every open homomorphism from an absolute Galois group of a number field to \(P\) is a conjugate of restriction, and Hoshi's criterion then gives Uchida's conjecture.

- The identification (Section 1).
- Prosolvable rigidity (Section 2).
- The proof of Uchida's conjecture (Section 3).

## 1. The identification

Keep \(\alpha_0\colon G_F\to P\), \(U\), \(T=G_k\) and \(\beta\colon T\to P\) from [Normalizer extension and Frobenius generation](normalizer-extension-and-frobenius-generation.md), the infinite set \(\mathcal L\), and \(B=\mathbb Q(i)\), \(G_K=\beta^{-1}(P_B)\) from the matching lesson. By Theorem 4.1 of the generation lesson,
\[
\begin{gathered}
\log\chi_r\circ\beta=\log\chi_{k,r}\\
(r\in\mathcal L).
\end{gathered}\tag{1.1}
\]
Let \(\sigma\colon T\to P\) be ordinary restriction, and for \(a\in P\) put \(\sigma_a=\operatorname{Ad}(a)\circ\sigma\), \(\sigma_a(t)=a\sigma(t)a^{-1}\).

For \(b\in\widehat{\mathbb Z}\) let \(b_r\) be its component in \(\mathbb Z_r\). Two facts are used. For a rational prime \(q\ne r\), \(\log(q^b)=b_r\log q\) in \(\mathbb Z_r\), since \(\log\) vanishes on \(\mu_{r-1}\) and is \(\mathbb Z_r\)-linear on \(1+r\mathbb Z_r\). And for a continuous homomorphism \(x\colon\widehat{\mathbb Z}\to\mathbb Q_r\), \(x(b)=b_r\,x(1)\): the image of each factor \(\mathbb Z_p\), \(p\ne r\), is a compact pro-\(p\) subgroup of \(\mathbb Q_r\), hence \(0\).

**Proposition 1.1** ([OpenAI-UC, Proposition 6.1]). There is \(a\in P\) with \(\beta=\sigma_a\) on \(T\).

*Proof.* *Setup.* Fix a finite Galois extension \(L/\mathbb Q\) inside \(\mathbb Q^s\) containing \(B\), with group \(R\). Let \(G_{F'}\) be the intersection of the \(\mathcal G\)-conjugates of the open subgroup \(\beta^{-1}(P_L)\cap G_K\cap G_L\) of \(T\); it is open and normal in \(\mathcal G\), its fixed field \(F'\) is finite Galois over \(\mathbb Q\) and contains \(K\) and \(L\), and \(\beta(G_{F'})\subseteq P_L\), \(\sigma(G_{F'})\subseteq P_L\). Fix \(r\in\mathcal L\). Pullback along \(\beta|_{G_{F'}}\) and \(\sigma|_{G_{F'}}\) gives linear maps
\[
i_\beta,\ i_\sigma\colon\mathcal X_r(L)\longrightarrow\mathcal X_r(F').
\]
Both are injective because their underlying homomorphisms have open image in \(P_L\) (Lemma 2.1(5) of [Additive characters and Frobenius detection](additive-characters-and-frobenius-detection.md)). Since \(L/\mathbb Q\) is Galois, \(\sigma_a(G_{F'})\subseteq aP_La^{-1}=P_L\); let \(i_a\) be its pullback. It depends only on \(a\) modulo \(P_L\), because conjugation by an element of \(P_L\) does not change values of a homomorphism \(P_L\to\mathbb Q_r\).

*Frobenius evaluations.* Let \(q\ne r\) be a rational prime that splits completely in \(F'\); it splits in \(B\). By Proposition 5.1 of the matching lesson, for all but finitely many such \(q\) there are a prime \(w\) of \(B\) above \(q\), a prime \(v\) of \(K\) above \(q\) and \(\ell\in\mathcal L\) with \((v,w)\) an active pair at \(\ell\). Choose a prime \(v'\) of \(F'\) above \(v\) and a prime \(\bar v\) of \(\overline{\mathbb Q}\) above \(v'\); by the remark after (U2) in the first lesson, the target prime of \(\mathbb Q^s\) can be chosen with \(\beta(D_v)\subseteq D_{\bar w}\), \(\bar w\) above \(w\). Let \(u\) be the prime of \(L\) below \(\bar w\). Then
\[
\beta(D_{v'})\subseteq D_{\bar w}\cap P_L ,
\]
a decomposition group of \(P_L\) at \(u\). All these primes have absolute residue degree one, because \(q\) splits completely in \(F'\supseteq L\).

Let \(h\in D_{v'}\) be an arithmetic Frobenius lift; it acts on residues as the \(q\)-th power. Let \(a_q\in\widehat{\mathbb Z}\) be the residue exponent of \(\beta(h)\) at \(u\). Then \(\chi_r(\beta(h))=q^{a_q}\) and \(\chi_{k,r}(h)=q\), so (1.1) gives \((a_q)_r\log q=\log q\). As \(q>1\) is not a root of unity, \(\log q\ne0\), and \((a_q)_r=1\). Every \(x\in\mathcal X_r(L)\) is unramified at \(u\), so on the decomposition group it factors through the residue exponent, and
\[
\begin{aligned}
i_\beta(x)(\operatorname{Fr}_{v'})&=x(\beta(h))\\
&=(a_q)_r\,x(\operatorname{Fr}_u)\\
&=x(\operatorname{Fr}_u).
\end{aligned}\tag{1.2}
\]
This uses only the decomposition containment; the auxiliary prime \(\ell\) of the active pair need not be \(r\).

Under restriction, \(\sigma(h)\) is an arithmetic Frobenius element at the prime \(u'\) of \(L\) below \(\bar v\). Choose \(g\in R\) with \(gu'=u\), possible since \(R\) permutes the primes above \(q\) transitively, and a lift \(a\in P\) of \(g\). Then \(a\sigma(h)a^{-1}\) is an arithmetic Frobenius element at a prime above \(u\), so \(i_a(x)(\operatorname{Fr}_{v'})=x(\operatorname{Fr}_u)\), and by (1.2)
\[
\begin{gathered}
i_\beta(x)(\operatorname{Fr}_{v'})=i_a(x)(\operatorname{Fr}_{v'})\\
(x\in\mathcal X_r(L)).
\end{gathered}
\]
The class of \(a\) modulo \(P_L\) may depend on \(q\), but there are only \(|R|\) classes, so one class serves for infinitely many \(q\). For each \(x\), the character \(i_\beta(x)-i_a(x)\in\mathcal X_r(F')\) then vanishes at infinitely many primes of absolute residue degree one, and Proposition 4.1(1) of the character lesson gives
\[
i_\beta=i_a . \tag{1.3}
\]

*From characters to the finite group.* The group \(T\) acts on \(\mathcal X_r(F')\) by conjugation, and pullback intertwines this action with the action on \(\mathcal X_r(L)\) through \(\beta\), respectively through \(\sigma_a\): for \(t\in T\), \(h\in G_{F'}\) and \(x\in\mathcal X_r(L)\), \((t\cdot i_\beta(x))(h)=x(\beta(t)^{-1}\beta(h)\beta(t))\), which is \(i_\beta(\beta(t)x)(h)\), and likewise for \(\sigma_a\). With \(i\) the common injective map of (1.3),
\[
i(\beta(t)x)=t\cdot i(x)=i(\sigma_a(t)x),
\]
so \(\beta(t)\) and \(\sigma_a(t)\) act in the same way on \(\mathcal X_r(L)\). The field \(L\) is totally imaginary, since it contains \(B\), so \(R\) acts faithfully on \(\mathcal X_r(L)\) by Proposition 5.3 of the character lesson. Hence
\[
\beta(t)\equiv\sigma_a(t)\pmod{P_L}\qquad(t\in T).
\]

*One conjugation for all quotients.* For each such \(L\) let
\[
\begin{gathered}
C_L=\{a\in P:\ \beta(t)\equiv a\sigma(t)a^{-1}\\
\text{modulo }P_L\text{ for every }t\in T\}.
\end{gathered}
\]
It is nonempty. It is a union of cosets of \(P_L\), since for \(b\in P_L\), \(b\sigma(t)b^{-1}\equiv\sigma(t)\) modulo the normal subgroup \(P_L\); so it is open and closed. If \(L\subseteq L'\), then \(C_{L'}\subseteq C_L\), and composita show that finitely many of the \(C_L\) have a common point. By compactness of \(P\) some \(a\) lies in every \(C_L\). The fields \(L\supseteq B\) are cofinal among the finite Galois subextensions of \(\mathbb Q^s/\mathbb Q\), and the \(P_L\) intersect in \(1\), so \(\beta(t)=a\sigma(t)a^{-1}\) for all \(t\). \(\square\)

## 2. Prosolvable rigidity

**Theorem 2.1** (prosolvable rigidity; [OpenAI-UC, Theorem 6.2]). Let \(F\) be a number field in \(\overline{\mathbb Q}\). Every continuous homomorphism \(\varphi\colon G_F\to P\) with open image is conjugate in \(P\) to ordinary restriction: there is \(a\in P\) with \(\varphi(g)=a\,(g|_{\mathbb Q^s})\,a^{-1}\) for all \(g\in G_F\).

*Proof.* Apply the construction of the generation lesson to \(\alpha_0=\varphi\): choose an open normal subgroup \(U\) of \(\mathcal G\) inside \(G_F\) and extend \(\varphi|_U\) to the normalizer of its kernel. Proposition 1.1 gives \(a\) with \(\varphi=\operatorname{Ad}(a)\circ\sigma\) on \(U\), where \(\sigma\) is restriction. Replacing \(\varphi\) by \(\operatorname{Ad}(a^{-1})\circ\varphi\), we may assume \(\varphi=\sigma\) on \(U\). For \(g\in G_F\) and \(u\in U\), normality of \(U\) gives
\[
\begin{aligned}
\varphi(g)\sigma(u)\varphi(g)^{-1}&=\varphi(gug^{-1})\\
&=\sigma(gug^{-1})\\
&=\sigma(g)\sigma(u)\sigma(g)^{-1}.
\end{aligned}
\]
So \(\sigma(g)^{-1}\varphi(g)\) commutes with every element of \(\sigma(U)=\varphi(U)\), which has finite index in the open subgroup \(\varphi(G_F)\) and is therefore open. By Lemma 3.1 of [Solvably closed fields and Uchida's conjecture](solvably-closed-fields-and-uchidas-conjecture.md), \(\sigma(g)^{-1}\varphi(g)=1\). \(\square\)

In particular every open homomorphism \(G_F\to P\) has kernel \(\operatorname{Gal}(\overline{\mathbb Q}/F\mathbb Q^s)\), the kernel of restriction, and image a conjugate of \(P_{F\cap\mathbb Q^s}\).

## 3. The proof of Uchida's conjecture

*Proof of Theorem 2.1 of the first lesson.* Let \(F_1,F_2\) be number fields, \(E_i/F_i\) Galois extensions with \(E_i\) solvably closed, \(G_i=\operatorname{Gal}(E_i/F_i)\), and \(\alpha\colon G_1\to G_2\) continuous with open image. Choose embeddings of \(E_1\) and \(E_2\) into \(\overline{\mathbb Q}\), and identify them with their images. By Proposition 1.3 of the first lesson, \(\mathbb Q^s\subseteq E_i\), and \(\mathbb Q^s/\mathbb Q\) is Galois. Consider the composite
\[
\varphi\colon G_{F_1}\xrightarrow{\ \mathrm{res}\ }G_1\xrightarrow{\ \alpha\ }G_2\xrightarrow{\ \mathrm{res}\ }P .
\]
The first map is surjective. The composite of \(G_{F_2}\to G_2\to P\) is restriction from \(G_{F_2}\) to \(\mathbb Q^s\), whose image \(\operatorname{Gal}(\mathbb Q^s/\mathbb Q^s\cap F_2)\) is open; as \(G_{F_2}\to G_2\) is surjective, \(G_2\to P\) has open image, and so does its restriction to the open subgroup \(\alpha(G_1)\), whose image has finite index in it. Hence \(\varphi\) is open.

By Theorem 2.1, \(\varphi=\operatorname{Ad}(a)\circ\sigma\) with \(\sigma\colon G_{F_1}\to P\) the restriction. The cyclotomic character \(\chi_{\mathbb Q^s/\mathbb Q}\) of \(P\) takes values in the abelian group \(\widehat{\mathbb Z}^\times\), so it is unchanged by conjugation. All roots of unity lie in \(\mathbb Q^s\), so the cyclotomic characters of \(G_{F_1}\), \(G_1\), \(G_2\) and \(P\) are compatible with the restriction maps. For \(g\in G_{F_1}\) with image \(\bar g\in G_1\),
\[
\begin{aligned}
\chi_{E_2/F_2}(\alpha(\bar g))&=\chi_{\mathbb Q^s/\mathbb Q}(\varphi(g))\\
&=\chi_{\mathbb Q^s/\mathbb Q}(\sigma(g))\\
&=\chi_{E_1/F_1}(\bar g).
\end{aligned}
\]
Since \(G_{F_1}\to G_1\) is surjective, \(\chi_{E_2/F_2}\circ\alpha=\chi_{E_1/F_1}\). By Hoshi's criterion (H) of the first lesson, there is a field embedding \(E_2\to E_1\) inducing \(\alpha\), and it is unique. \(\square\)

**What the proof assumed.** Besides the programme lessons cited along the way, the proof used three published results without proof: Uchida's isomorphism theorem (U1), in Lemma 3.1 of the first lesson and in the normalizer extension; Uchida's partial local correspondence (U2), in the generation, matching and identification steps; and Hoshi's criterion with Uchida's uniqueness (H), in the last step. Everything else is proved in the course: the logarithm rank theorem with its zero estimate, the class-field description of additive characters, Frobenius detection, the signed representation, quotient amplification and Frobenius generation, the Kummer description of unramified classes, the uniform bound on missed primes, power-residue separation and the identification.

## 4. Exercises

**4.1.** Show that the sets \(C_L\) in the proof of Proposition 1.1 are closed under multiplication by \(P_L\) on the right.

**4.2.** Deduce from Theorem 2.1 that a continuous open homomorphism \(\varphi\colon G_F\to P\) is injective on every decomposition group of \(G_F\) at a finite prime.

**4.3.** Let \(M\subset\mathbb Q^s\) be a number field and \(\varphi\colon P_M\to P\) a continuous open homomorphism. Show, using Theorem 2.1 for \(G_M\to P_M\to P\), that \(\varphi\) is the restriction of an inner automorphism of \(P\) to \(P_M\).

**4.4.** In the proof of Section 3, show directly that \(\chi_{\mathbb Q^s/\mathbb Q}(\sigma(g))=\chi_{E_1/F_1}(\bar g)\).

## 5. Solutions

**4.1.** For \(b\in P_L\), \(ab\,\sigma(t)\,(ab)^{-1}=a\,(b\sigma(t)b^{-1})\,a^{-1}\), and \(b\sigma(t)b^{-1}\sigma(t)^{-1}\in P_L\) because \(P_L\) is normal; conjugating by \(a\) keeps this element in \(P_L\). So the congruence for \(a\) implies that for \(ab\).

**4.2.** By Theorem 2.1, \(\varphi\) is restriction followed by an automorphism of \(P\), and restriction is injective on decomposition groups at finite primes by Proposition 5.3 of the first lesson.

**4.3.** The composite \(G_M\to P_M\to P\) is open, since \(G_M\to P_M\) is surjective. By Theorem 2.1 it equals \(\operatorname{Ad}(a)\circ\mathrm{res}\). As \(G_M\to P_M\) is surjective, \(\varphi(g)=aga^{-1}\) for \(g\in P_M\).

**4.4.** \(\sigma(g)\) is the restriction of \(g\) to \(\mathbb Q^s\), and the cyclotomic character only involves the action on \(\mu_\infty\subset\mathbb Q^s\subseteq E_1\); the action of \(g\) on \(\mu_\infty\) is that of \(\bar g\).

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Section 6. https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
- [Hoshi 2025] Y. Hoshi, *Homomorphisms of global solvably closed Galois groups compatible with cyclotomic characters*, Tôhoku Math. J. (2) 77 (2025), 17–32, Theorem 3.4; preprint RIMS-1955 (2021), https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1955.pdf
- [Uchida 1981] K. Uchida, *Homomorphisms of Galois groups of solvably closed Galois extensions*, J. Math. Soc. Japan 33 (1981), 595–604, Proposition 2. https://doi.org/10.2969/jmsj/03340595
