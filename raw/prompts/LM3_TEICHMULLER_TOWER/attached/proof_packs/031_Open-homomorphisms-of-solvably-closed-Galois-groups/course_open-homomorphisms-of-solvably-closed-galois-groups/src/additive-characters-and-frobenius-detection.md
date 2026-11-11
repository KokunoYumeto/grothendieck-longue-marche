# Additive characters and Frobenius detection

*Written by Claude Opus 5.5 (Anthropic), October 2026. Self-checked by the writing AI. Public domain (CC0).*

Two continuous homomorphisms into the prosolvable group \(P\) will be compared through additive \(\ell\)-adic characters: homomorphisms from Galois groups to the additive group \(\mathbb Q_\ell\). Such a character is unramified away from \(\ell\), so it has a value at each Frobenius element. This lesson proves that a character vanishing at the Frobenius elements of infinitely many primes of absolute residue degree one is zero, together with versions for Frobenius averages and corestrictions that allow primes of any degree. The proof combines class field theory with the logarithm rank theorem of [A logarithm rank lemma](a-logarithm-rank-lemma.md). The lesson ends with a representation of the Galois group inside the character space, which supplies enough characters for the later comparisons.

- Additive characters and Frobenius values (Section 1).
- Transfer (Section 2).
- The class-field description (Section 3).
- Frobenius detection (Section 4).
- A signed representation (Section 5).

## 1. Additive characters and Frobenius values

For a number field \(M\) and a prime \(\ell\) put
\[
\mathcal X_\ell(M)=\operatorname{Hom}_{\mathrm{cont}}(G_M,\mathbb Q_\ell),
\]
with \(\mathbb Q_\ell\) as an additive group. It is a \(\mathbb Q_\ell\)-vector space. Its elements factor through the maximal abelian quotient, and through \(P_M\) when \(M\subset\mathbb Q^s\) (Proposition 1.3 of [Solvably closed fields and Uchida's conjecture](solvably-closed-fields-and-uchidas-conjecture.md)). A compact subgroup of \(\mathbb Q_\ell\) is \(0\) or \(\ell^k\mathbb Z_\ell\) for some \(k\); so the image of a pro-\(p\) group, \(p\ne\ell\), or of a finite group under a continuous homomorphism to \(\mathbb Q_\ell\) is \(0\), because \(\ell^k\mathbb Z_\ell\) has the quotient \(\mathbb Z/\ell\mathbb Z\).

**Lemma 1.1.** Let \(x\in\mathcal X_\ell(M)\) and let \(v\nmid\ell\) be a finite prime of \(M\). Then \(x\) vanishes on the inertia group \(I_v\).

*Proof.* Let \(p\) be the residue characteristic of \(v\) and \(q=Nv\). By Proposition 5.3 of the first lesson, \(D_v\) is the absolute Galois group of \(M_v\), and Lemma 5.1 there describes \(I_v\supset W_v\). The restriction of \(x\) to the pro-\(p\) group \(W_v\) is zero, so \(x|_{I_v}\) factors through \(I_v/W_v\cong\prod_{\ell'\ne p}\mathbb Z_{\ell'}(1)\). On each factor with \(\ell'\ne\ell\) it vanishes, being a pro-\(\ell'\) group. The factor \(\mathbb Z_\ell(1)\) is the image of a pro-\(\ell\) Sylow subgroup \(J\) of \(I_v\). For \(t\in J\) and a Frobenius lift \(g\in D_v\), Lemma 5.2 of the first lesson gives \(gtg^{-1}\equiv t^{q}\pmod{W_v}\), so \(x(t)=x(gtg^{-1})=q\,x(t)\). Since \(q\ne1\), \(x(t)=0\). The factors generate a dense subgroup of \(I_v/W_v\), so \(x\) vanishes on \(I_v\). \(\square\)

So for \(v\nmid\ell\) the value \(x(\operatorname{Fr}_v)\) at an arithmetic Frobenius element of \(D_v\) is well defined: two Frobenius elements of \(D_v\) differ by an element of \(I_v\), and another prime above \(v\) conjugates \(D_v\), which does not change values of the homomorphism \(x\) to an abelian group. If \(L\supseteq M\) is a finite extension and \(w\) a prime of \(L\) above \(v\), the restriction of \(x\) to \(G_L\) satisfies
\[
\begin{aligned}
&(\operatorname{res}_{L/M}x)(\operatorname{Fr}_w)\\
&\quad=[\kappa(w):\kappa(v)]\;x(\operatorname{Fr}_v),
\end{aligned}\tag{1.1}
\]
because a Frobenius element at \(w\) acts on residues as the \([\kappa(w):\kappa(v)]\)-th power of a Frobenius element at \(v\).

If \(M/\mathbb Q\) is Galois, \(R=\operatorname{Gal}(M/\mathbb Q)\) acts on \(\mathcal X_\ell(M)\) by
\[
(gx)(h)=x(\tilde g^{-1}h\tilde g)\qquad(h\in G_M),
\]
where \(\tilde g\in\mathcal G\) lifts \(g\); another lift differs by an element of \(G_M\), and conjugation by it does not change values of \(x\). For a prime \(v\nmid\ell\) of \(M\), \((gx)(\operatorname{Fr}_v)=x(\operatorname{Fr}_{g^{-1}v})\). For a subgroup \(J\subseteq R\), the operator \(E_J=|J|^{-1}\sum_{g\in J}g\) is the projector onto the \(J\)-invariants.

## 2. Transfer

Let \(H\) be an open subgroup of index \(n\) in a profinite group \(G\), and choose representatives \(G=\bigsqcup_{i=1}^nt_iH\). For \(g\in G\) write \(gt_i=t_{\sigma(i)}h_i(g)\) with a permutation \(\sigma=\sigma_g\) and \(h_i(g)\in H\). For a continuous homomorphism \(y\colon H\to\mathbb Q_\ell\) put
\[
\operatorname{cor}(y)(g)=\sum_{i=1}^ny(h_i(g)).
\]

**Lemma 2.1.**

1. \(\operatorname{cor}(y)\) does not depend on the representatives and is a continuous homomorphism \(G\to\mathbb Q_\ell\).
2. For a continuous homomorphism \(x\colon G\to\mathbb Q_\ell\), \(\operatorname{cor}(x|_H)=n\,x\).
3. If \(H\) is normal, then \(\operatorname{cor}(y)|_H=\sum_{g\in G/H}g\,y\), where \((g\,y)(h)=y(\tilde g^{-1}h\tilde g)\).
4. If \(H'\subseteq H\) is open and \(y\colon H'\to\mathbb Q_\ell\), then \(\operatorname{cor}_{G\leftarrow H'}(y)\) equals \(\operatorname{cor}_{G\leftarrow H}(\operatorname{cor}_{H\leftarrow H'}(y))\). In particular \(\operatorname{cor}_{G\leftarrow H'}(x|_{H'})\) equals \([H:H']\operatorname{cor}_{G\leftarrow H}(x)\) for \(x\colon H\to\mathbb Q_\ell\).
5. Restriction \(x\mapsto x|_H\) is injective on continuous homomorphisms \(G\to\mathbb Q_\ell\).

*Proof.* (1) Replacing \(t_i\) by \(t_ik_i\) with \(k_i\in H\) replaces \(h_i(g)\) by \(k_{\sigma(i)}^{-1}h_i(g)k_i\), which changes the sum by \(\sum_i(y(k_i)-y(k_{\sigma(i)}))=0\). For \(g,g'\in G\), \(gg't_i=gt_{\sigma'(i)}h_i(g')\), which equals \(t_{\sigma\sigma'(i)}h_{\sigma'(i)}(g)h_i(g')\), so \(\operatorname{cor}(y)(gg')=\operatorname{cor}(y)(g)+\operatorname{cor}(y)(g')\) after reindexing. On a coset \(gU\) of an open normal subgroup \(U\subseteq\bigcap_it_iHt_i^{-1}\) the permutation is constant and \(h_i\) varies continuously, which gives continuity. (2) \(x(h_i(g))=x(t_{\sigma(i)}^{-1})+x(g)+x(t_i)\), and the outer terms cancel in the sum. (3) For \(h\in H\), \(ht_i=t_i(t_i^{-1}ht_i)\), so \(\sigma\) is the identity and \(\operatorname{cor}(y)(h)=\sum_iy(t_i^{-1}ht_i)\). (4) Choose \(H=\bigsqcup_js_jH'\). Then \(G=\bigsqcup_{i,j}t_is_jH'\), and \(gt_is_j=t_{\sigma(i)}h_i(g)s_j=t_{\sigma(i)}s_{\pi_i(j)}k_{ij}\) with \(h_i(g)s_j=s_{\pi_i(j)}k_{ij}\), \(k_{ij}\in H'\). Hence
\[
\begin{aligned}
&\operatorname{cor}_{G\leftarrow H'}(y)(g)=\sum_i\sum_jy(k_{ij})\\
&\quad=\sum_i\operatorname{cor}_{H\leftarrow H'}(y)(h_i(g))\\
&\quad=\operatorname{cor}_{G\leftarrow H}(\operatorname{cor}_{H\leftarrow H'}(y))(g).
\end{aligned}
\]
With \(y=x|_{H'}\), (2) for \(H'\subseteq H\) gives the second assertion. (5) If \(x|_H=0\), the image of \(x\) is the image of the finite set \(G/H\), a finite subgroup of the torsion-free group \(\mathbb Q_\ell\), hence \(0\). \(\square\)

For number fields \(M\subseteq L\) we write \(\operatorname{res}_{L/M}\colon\mathcal X_\ell(M)\to\mathcal X_\ell(L)\) and \(\operatorname{cor}_{L/M}\colon\mathcal X_\ell(L)\to\mathcal X_\ell(M)\) for these maps with \(G=G_M\), \(H=G_L\).

## 3. The class-field description

Let \(V_M=M\otimes_{\mathbb Q}\mathbb Q_\ell=\prod_{w\mid\ell}M_w\). For a global unit \(\varepsilon\), let \(\log\varepsilon\in V_M\) have components the logarithms of \(\varepsilon\) in the fields \(M_w\), as in Section 1 of the logarithm rank lesson. Let \(U_M\subseteq V_M\) be the \(\mathbb Q_\ell\)-linear span of \(\log\mathcal O_M^\times\).

We use the global reciprocity map of [Global existence and the idelic class field correspondence](course:NT-CFT/global-existence-and-the-idelic-class-field-correspondence), Proposition 17.3: a continuous surjection \(\operatorname{rec}\colon\mathbb A_M^\times\to G_M^{\mathrm{ab}}\), trivial on \(M^\times\), whose kernel on the idèle class group \(C_M\) is the closure \(D_M\) of the image of the connected component of the archimedean idèles. Since \(C_M=C_M^1\cdot\mathbb R_{>0}\) with \(C_M^1\) compact and \(\mathbb R_{>0}\subseteq D_M\), the quotient \(C_M/D_M\) is compact, so \(\operatorname{rec}\) induces an isomorphism of topological groups \(C_M/D_M\to G_M^{\mathrm{ab}}\). At a finite prime \(v\), \(\operatorname{rec}\) maps a uniformizer of \(M_v\) to an element acting as arithmetic Frobenius on every abelian extension unramified at \(v\) (Proposition 18.1 of [Ray class fields, conductors and ideal reciprocity](course:NT-CFT/ray-class-fields-conductors-and-ideal-reciprocity)), and it is compatible with field automorphisms (Proposition 16.1 of [The global reciprocity law](course:NT-CFT/the-global-reciprocity-law)).

**Proposition 3.1** ([OpenAI-UC, (3.2)–(3.3)]). For every \(x\in\mathcal X_\ell(M)\) there is a unique \(\mathbb Q_\ell\)-linear form \(\lambda_x\colon V_M\to\mathbb Q_\ell\) with
\[
x(\operatorname{rec}(u))=\lambda_x(\log u)
\]
for every idèle \(u\) whose components are units at the places above \(\ell\) and \(1\) elsewhere. The map \(x\mapsto\lambda_x\) is an isomorphism
\[
\begin{aligned}
\mathcal X_\ell(M)\xrightarrow{\ \sim\ }\{&\lambda\in\operatorname{Hom}_{\mathbb Q_\ell}(V_M,\mathbb Q_\ell):\\
&\lambda(U_M)=0\},
\end{aligned}
\]
compatible with the action of automorphisms of \(M\). For every finite prime \(v\nmid\ell\) and every \(b\in\mathcal O_M\) with \((b)=v^h\), \(h>0\),
\[
\lambda_x(\log b)=-h\,x(\operatorname{Fr}_v). \tag{3.1}
\]

*Proof.* Put \(\psi=x\circ\operatorname{rec}\), a continuous homomorphism \(\mathbb A_M^\times\to\mathbb Q_\ell\) trivial on \(M^\times\). It vanishes on the archimedean components, whose images are connected (from \(\mathbb C^\times\) or \(\mathbb R_{>0}\)) or finite (from \(\{\pm1\}\)), while \(\mathbb Q_\ell\) is totally disconnected and torsion-free. For a finite \(v\nmid\ell\), the unit group \(\mathcal O_v^\times\) is a finite group times a pro-\(p\) group, so \(\psi\) vanishes on it. For \(w\mid\ell\), let \(U^{r_0}\subseteq\mathcal O_w^\times\) be a subgroup on which \(\log\) is an isomorphism onto an open lattice \(\mathfrak m_w^{r_0}\) of \(M_w\). A continuous additive map \(\mathfrak m_w^{r_0}\to\mathbb Q_\ell\) is \(\mathbb Z\)-linear, hence \(\mathbb Z_\ell\)-linear by continuity, and extends uniquely to a \(\mathbb Q_\ell\)-linear form on \(M_w\). For \(u\in\mathcal O_w^\times\), some power \(u^N\) lies in \(U^{r_0}\), and \(\psi(u)=N^{-1}\psi(u^N)\). So the restriction of \(\psi\) to \(\prod_{w\mid\ell}\mathcal O_w^\times\) is \(\lambda\circ\log\) for a unique linear form \(\lambda=\lambda_x\) on \(V_M\).

*Relations.* For \(\varepsilon\in\mathcal O_M^\times\), the principal idèle \(\varepsilon\) has unit components at all finite places, so \(0=\psi(\varepsilon)=\lambda_x(\log\varepsilon)\); hence \(\lambda_x(U_M)=0\). For \(b\) with \((b)=v^h\), the principal idèle \(b\) is a unit at every finite place other than \(v\), and equals \(\varpi_v^h\) times a unit at \(v\), where \(\varpi_v\) is a uniformizer. By Lemma 1.1, \(x\) factors through the Galois group of the maximal abelian extension unramified at \(v\), on which \(\operatorname{rec}(\varpi_v)\) is arithmetic Frobenius. So \(0=\psi(b)=\lambda_x(\log b)+h\,x(\operatorname{Fr}_v)\), which is (3.1).

*Injectivity.* If \(\lambda_x=0\), then \(\psi\) vanishes on \(\mathcal U=\prod_{w\mid\infty}M_w^\times\times\prod_{v\ \mathrm{finite}}\mathcal O_v^\times\) and on \(M^\times\). The quotient \(\mathbb A_M^\times/\mathcal UM^\times\) is the ideal class group, which is finite, so \(\psi\) has finite image and is \(0\). As \(\operatorname{rec}\) is surjective, \(x=0\).

*Surjectivity.* Let \(\lambda\) vanish on \(U_M\). Define \(\psi_0\) on \(\mathcal U\) by \(\psi_0(u)=\lambda(\log(u_w)_{w\mid\ell})\). It is a continuous homomorphism, trivial on \(\mathcal U\cap M^\times=\mathcal O_M^\times\), so it defines a continuous homomorphism on the open subgroup \(\mathcal UM^\times/M^\times\) of \(C_M\), of finite index \(h_M\), the class number. Extend it to \(C_M\) by \(\psi(c)=h_M^{-1}\psi_0(c^{h_M})\); this is a continuous homomorphism, and it extends \(\psi_0\). It vanishes on the image of the connected archimedean component, hence on its closure \(D_M\), so \(\psi=x\circ\operatorname{rec}\) for a continuous \(x\colon G_M^{\mathrm{ab}}\to\mathbb Q_\ell\), and \(\lambda_x=\lambda\).

*Compatibility.* If \(g\) is an automorphism of \(M\) with a lift \(\tilde g\in\mathcal G\), then \(\operatorname{rec}(g(u))=\tilde g\operatorname{rec}(u)\tilde g^{-1}\), and \(\log(g(u))=g(\log u)\). With the action of Section 1 on characters and \((g\lambda)(v)=\lambda(g^{-1}v)\) on linear forms, this gives \(\lambda_{gx}=g\lambda_x\). \(\square\)

The description uses the actual logarithmic image \(U_M\) of the units and makes no assertion about its dimension.

## 4. Frobenius detection

**Proposition 4.1** (Frobenius detection; [OpenAI-UC, Proposition 3.2]). Let \(M\) be a number field, \(\ell\) a prime and \(x\in\mathcal X_\ell(M)\).

1. If \(x(\operatorname{Fr}_v)=0\) at infinitely many primes \(v\nmid\ell\) of absolute residue degree one, then \(x=0\).
2. Suppose \(M/\mathbb Q\) is Galois and fix \(\delta\in\operatorname{Gal}(M/\mathbb Q)\). If \(x(\operatorname{Fr}_v)=0\) at infinitely many primes \(v\nmid\ell\) of \(M\) lying over rational primes unramified in \(M\), whose Frobenius in \(\operatorname{Gal}(M/\mathbb Q)\) is \(\delta\), then \(E_{\langle\delta\rangle}x=0\).
3. If \(\operatorname{cor}_{M/\mathbb Q}x\ne0\), then \(x(\operatorname{Fr}_v)=0\) at only finitely many primes \(v\nmid\ell\), of any residue degree.

*Proof.* (1) Put \(n=[M:\mathbb Q]\), let \(E\) be a Galois closure of \(M\), and choose \(m>n(n-1)\) zero primes \(v_1,\ldots,v_m\) of degree one over distinct rational primes \(p_1,\ldots,p_m\), all unramified in \(E\). Since the class group of \(M\) is finite, there are \(h_i>0\) and \(b_i\in\mathcal O_M\) with \((b_i)=v_i^{h_i}\). Let \(\sigma\) run over the \(n\) embeddings \(M\to E\) and put
\[
u_i=(\sigma(b_i))_\sigma\in(E^\times)^n .
\]

The \(mn\) numbers \(\sigma(b_i)\) have pairwise disjoint nonempty supports. Let \(G=\operatorname{Gal}(E/\mathbb Q)\), \(H=\operatorname{Gal}(E/M)\), fix a prime \(\mathfrak P_i\) of \(E\) above \(v_i\), and let \(D_i\) be its decomposition group over \(p_i\). As \(p_i\) is unramified, \(|D_i|\) is the residue degree of \(\mathfrak P_i\) over \(p_i\); this equals the residue degree over \(v_i\), which is \(|D_i\cap H|\), because \(v_i\) has degree one. So \(D_i\subseteq H\). The primes of \(E\) above \(p_i\) correspond to \(G/D_i\), those above \(v_i\) to \(H/D_i\), and for \(\sigma=g|_M\) the support of \(\sigma(b_i)\) is the set of primes above \(g(v_i)\), corresponding to \(gH/D_i\). Distinct embeddings give distinct cosets \(gH\), whose subsets \(gH/D_i\) of \(G/D_i\) are disjoint; distinct \(i\) involve distinct rational primes. Consequently, if \(\prod_{i,\sigma}\sigma(b_i)^{\gamma_{i\sigma}}\) is a root of unity, its ideal is trivial and all \(\gamma_{i\sigma}=0\). For \(a\in\mathbb Z^m\setminus\{0\}\), a relation \(\prod_\sigma\bigl(\prod_i\sigma(b_i)^{a_i}\bigr)^{\gamma_\sigma}=\zeta\) gives \(a_i\gamma_\sigma=0\) for all \(i,\sigma\), so \(\gamma=0\): the coordinates of \(u^a\) are multiplicatively independent modulo roots of unity. They are algebraic integers, and units at every place above \(\ell\) since their supports lie above the \(p_i\ne\ell\).

Let \(K\) be the completion of \(E\) at a prime above \(\ell\). Since \(K\) contains all conjugates of \(M\), \(m\otimes c\mapsto(\sigma(m)c)_\sigma\) is an isomorphism of \(K\)-algebras \(V_M\otimes_{\mathbb Q_\ell}K\to K^n\). It maps \(\log b_i\otimes1\) to \(\log u_i\): each embedding \(\sigma\) extends to a continuous embedding of the completion of \(M\) at the corresponding place into \(K\), which commutes with the logarithm series and preserves roots of unity. By Theorem 2.1 of the logarithm rank lesson, the vectors \(\log u_i\) span \(K^n\). The form \(\lambda_x\otimes K\) vanishes on them by (3.1), so \(\lambda_x=0\), and \(x=0\) by Proposition 3.1.

(2) Put \(C=\langle\delta\rangle\), \(F=M^C\) and \(y=E_Cx\). Each indicated \(v\) is fixed by \(\delta\), which generates its decomposition group over \(\mathbb Q\); so \((gx)(\operatorname{Fr}_v)=x(\operatorname{Fr}_{g^{-1}v})=x(\operatorname{Fr}_v)\) for \(g\in C\), and \(y(\operatorname{Fr}_v)=0\). By Lemma 2.1(3), \(\operatorname{res}_{M/F}\operatorname{cor}_{M/F}y=\sum_{g\in C}gy=|C|y\), so \(y=\operatorname{res}_{M/F}z\) with \(z=|C|^{-1}\operatorname{cor}_{M/F}y\in\mathcal X_\ell(F)\). The decomposition group of \(v\) over \(F\) is \(C\cap\operatorname{Gal}(M/F)=C\), so the residue degree of \(v\) over \(u=v\cap F\) is \(|C|\), the residue degree of \(v\) over \(\mathbb Q\); hence \(u\) has absolute residue degree one. By (1.1), \(0=y(\operatorname{Fr}_v)=|C|\,z(\operatorname{Fr}_u)\). Infinitely many distinct \(u\) occur, since only finitely many \(v\) lie above each \(u\). By (1), \(z=0\), so \(y=0\).

(3) Suppose there are infinitely many zero primes. Let \(E\) be a Galois closure of \(M\), \(R=\operatorname{Gal}(E/\mathbb Q)\) and \(y=\operatorname{res}_{E/M}x\). Discarding finitely many zero primes, choose for each remaining one a prime of \(E\) above it whose rational prime is unramified in \(E\); by (1.1) these are zero primes of \(y\). Infinitely many of them have the same Frobenius \(\delta\in R\), and (2) gives \(E_{\langle\delta\rangle}y=0\), hence \(E_Ry=E_RE_{\langle\delta\rangle}y=0\). By Lemma 2.1(3), \(\operatorname{res}_{E/\mathbb Q}\operatorname{cor}_{E/\mathbb Q}y=|R|E_Ry=0\), and by Lemma 2.1(5), \(\operatorname{cor}_{E/\mathbb Q}y=0\). But by Lemma 2.1(4), \(\operatorname{cor}_{E/\mathbb Q}(\operatorname{res}_{E/M}x)\) equals \([E:M]\operatorname{cor}_{M/\mathbb Q}x\ne0\). \(\square\)

Exercise 6.4 shows that the degree condition in (1) cannot be dropped.

## 5. A signed representation

Representations here are finite-dimensional over \(\mathbb Q_\ell\), of a finite group \(R\). By Maschke's theorem (Theorem 2.3 of [Representations and complete reducibility](course:RT-FIN/representations-and-complete-reducibility)) every representation is a direct sum of irreducible ones, and for an irreducible \(S\) the number of summands isomorphic to \(S\) is \(\dim\operatorname{Hom}_R(S,V)/\dim\operatorname{End}_R(S)\), independent of the decomposition (Corollary 4.1 there, in the form for fields that are not algebraically closed). Since \(\dim V^R\) is the trace of the projector \(E_R\),
\[
\begin{aligned}
&\dim\operatorname{Hom}_R(S,V)=\dim(S^\vee\otimes V)^R\\
&\quad=\frac1{|R|}\sum_{g\in R}\chi_S(g^{-1})\chi_V(g).
\end{aligned}
\]
So the multiplicities, and therefore the isomorphism class, of a representation are determined by its character \(\chi_V(g)=\operatorname{tr}(g\mid V)\). If \(U\) is a quotient of \(B\), then \(B\cong U\oplus B'\), so every multiplicity of \(U\) is at most that of \(B\).

Let \(M/\mathbb Q\) be finite Galois and totally imaginary, \(R=\operatorname{Gal}(M/\mathbb Q)\), and let \(c\in R\) be the complex conjugation attached to an embedding \(\iota\colon M\to\mathbb C\), that is, \(\iota\circ c=\overline{\iota}\). It has order \(2\). Let
\[
\begin{gathered}
W_M=\operatorname{Ind}_{\langle c\rangle}^R(\operatorname{sign})\\
=\{f\colon R\to\mathbb Q_\ell:\ f(gc)=-f(g)\},\\
(hf)(g)=f(h^{-1}g),
\end{gathered}
\]
with \(\operatorname{sign}(c)=-1\).

**Lemma 5.1.**

1. \(\chi_{W_M}(1)=|R|/2\), \(\chi_{W_M}(g)=-|R|/(2|c^R|)\) for \(g\) in the conjugacy class \(c^R\), and \(\chi_{W_M}(g)=0\) otherwise. In particular \(W_M\) is isomorphic to its dual.
2. \(\mathbb Q_\ell[R]\cong\operatorname{Ind}_{\langle c\rangle}^R\mathbf 1\oplus W_M\), where \(\operatorname{Ind}_{\langle c\rangle}^R\mathbf 1=\mathbb Q_\ell[R/\langle c\rangle]\) is the permutation representation on \(R/\langle c\rangle\).
3. \(R\) acts faithfully on \(W_M\).

*Proof.* (1) Choose coset representatives \(x\) of \(R/\langle c\rangle\) and let \(e_x\) be the function supported on \(x\langle c\rangle\) with \(e_x(x)=1\), \(e_x(xc)=-1\). These form a basis, and \(g\) maps \(e_x\) to \(\pm e_{x'}\) where \(gx\langle c\rangle=x'\langle c\rangle\), with sign \(\operatorname{sign}(x^{-1}gx)\) when \(x'=x\). So \(\chi_{W_M}(g)=\frac12\sum_{y\in R,\ y^{-1}gy\in\langle c\rangle}\operatorname{sign}(y^{-1}gy)\), which gives the values: for \(g\) conjugate to \(c\) there are \(|R|/|c^R|\) elements \(y\) with \(y^{-1}gy=c\). The character of the dual is \(g\mapsto\chi(g^{-1})\), and \(g^{-1}\) is conjugate to \(c\) exactly when \(g\) is. (2) Every \(f\colon R\to\mathbb Q_\ell\) is uniquely \(f_++f_-\) with \(f_\pm(gc)=\pm f_\pm(g)\). (3) If \(g\) acts trivially, then \(ge_1=\pm e_{g}\) must equal \(e_1\), so \(g\in\langle c\rangle\); and \(c\) acts on \(e_1\) by \(-1\). \(\square\)

**Lemma 5.2** (the units as a representation). Let \(U^{\mathrm{alg}}=\mathcal O_M^\times\otimes_{\mathbb Z}\mathbb Q_\ell\). Then \(\mathbb Q_\ell\oplus U^{\mathrm{alg}}\cong\mathbb Q_\ell[R/\langle c\rangle]\), and \(M\otimes_{\mathbb Q}\mathbb Q_\ell\cong\mathbb Q_\ell[R]\).

*Proof.* By the remarks above it suffices to compare characters, and traces can be computed after extending scalars from \(\mathbb Q\) to \(\mathbb R\) or \(\mathbb C\). Let \(\Sigma\) be the set of archimedean places of \(M\); all are complex. \(R\) permutes \(\Sigma\) transitively, and the stabilizer of the place of \(\iota\) is \(\langle c\rangle\), since \(\iota\circ g\in\{\iota,\overline\iota\}\) only for \(g\in\{1,c\}\). So \(\mathbb R^\Sigma\cong\mathbb R[R/\langle c\rangle]\). The logarithmic embedding \(\varepsilon\mapsto(\log|\varepsilon|_w)_{w\in\Sigma}\) is \(R\)-equivariant, has finite kernel, and by Dirichlet's unit theorem (Theorem 9.2 of [Dirichlet's unit theorem](course:NT-ANT/dirichlets-unit-theorem)) its image is a lattice spanning the hyperplane \(\{\sum_wy_w=0\}\). This hyperplane is an invariant complement of the trivial line spanned by \((1,\ldots,1)\). Hence \(\chi_{U^{\mathrm{alg}}}=\chi_{\mathbb Q_\ell[R/\langle c\rangle]}-1\). For the second assertion, \(M\otimes_{\mathbb Q}\mathbb C\cong\mathbb C^{\operatorname{Hom}(M,\mathbb C)}\) by \(m\otimes z\mapsto(\tau(m)z)_\tau\), and \(g\in R\) acts by permuting the coordinates, \(\tau\mapsto\tau\circ g\), without fixed points when \(g\ne1\). So its character is that of \(\mathbb Q_\ell[R]\). \(\square\)

**Proposition 5.3** (signed representation; [OpenAI-UC, Proposition 3.3]). Let \(M/\mathbb Q\) be finite, Galois and totally imaginary, with group \(R\) and a complex conjugation \(c\). For every prime \(\ell\) there are \(R\)-equivariant injections
\[
\mathbb Q_\ell\oplus W_M\hookrightarrow\mathcal X_\ell(M)\hookrightarrow\mathbb Q_\ell[R].
\]
In particular \(R\) acts faithfully on \(\mathcal X_\ell(M)\), and \(\dim\mathcal X_\ell(M)^J\le|R|/|J|\) for every subgroup \(J\subseteq R\).

*Proof.* By Proposition 3.1, \(\mathcal X_\ell(M)\cong(V_M/U_M)^\vee\) equivariantly. By Lemma 5.2, \(V_M\cong\mathbb Q_\ell[R]\), which is self-dual (its character is real and constant on inverses), so the second injection is the dual of \(V_M\to V_M/U_M\). The span \(U_M\) is the image of the equivariant linear map \(U^{\mathrm{alg}}\to V_M\) induced by the logarithm, so every multiplicity of \(U_M\) is at most that of \(U^{\mathrm{alg}}\). By Lemmas 5.1(2) and 5.2,
\[
V_M\cong\mathbb Q_\ell\oplus U^{\mathrm{alg}}\oplus W_M,
\]
and \(V_M\cong U_M\oplus V_M/U_M\) by Maschke's theorem. Every multiplicity of \(V_M/U_M\) is therefore at least the corresponding multiplicity of \(\mathbb Q_\ell\oplus W_M\), and \(\mathbb Q_\ell\oplus W_M\) embeds in \(V_M/U_M\). Dualizing and using \(W_M\cong W_M^\vee\) gives the first injection. Faithfulness follows from Lemma 5.1(3). Finally \(\dim\mathbb Q_\ell[R]^J=|R|/|J|\), the number of \(J\)-orbits on \(R\). \(\square\)

## 6. Exercises

**6.1.** Show that \(\mathcal X_\ell(\mathbb Q)\) is one-dimensional, spanned by \(\log\chi_{\mathbb Q,\ell}\), where \(\log\) is the logarithm of \(\mathbb Z_\ell^\times\) vanishing on roots of unity.

**6.2.** For \(x=\log\chi_{\mathbb Q,\ell}\) and a prime \(p\ne\ell\), show that \(x(\operatorname{Fr}_p)=\log p\), and that \(\log p\ne0\).

**6.3.** Let \(M=\mathbb Q(i)\). Show that \(\mathcal X_\ell(M)\) is two-dimensional, the sum of the trivial and the sign representation of \(\operatorname{Gal}(M/\mathbb Q)\).

**6.4.** Let \(M=\mathbb Q(i)\) and let \(x\ne0\) span the sign part of \(\mathcal X_\ell(M)\). Show that \(x(\operatorname{Fr}_v)=0\) for every prime \(v\) of \(M\) above a rational prime \(p\equiv3\pmod4\), and that \(\operatorname{cor}_{M/\mathbb Q}x=0\). Which hypotheses of Proposition 4.1(1) and (3) fail?

**6.5.** Let \(G=\widehat{\mathbb Z}\), written additively, and \(H=n\widehat{\mathbb Z}\). Show that \(\operatorname{cor}(y)(g)=y(ng)\) for every continuous \(y\colon H\to\mathbb Q_\ell\), and check Lemma 2.1(2) and (3) in this case.

## 7. Solutions

**6.1.** \(V_{\mathbb Q}=\mathbb Q_\ell\) and \(\mathcal O_{\mathbb Q}^\times=\{\pm1\}\) has logarithm \(0\), so \(U_{\mathbb Q}=0\) and \(\mathcal X_\ell(\mathbb Q)\cong\operatorname{Hom}(\mathbb Q_\ell,\mathbb Q_\ell)\) is one-dimensional. The character \(\log\chi_{\mathbb Q,\ell}\) is nonzero by 6.2.

**6.2.** Arithmetic Frobenius at \(p\) acts on roots of unity of order prime to \(p\) as the \(p\)-th power, so \(\chi_{\mathbb Q,\ell}(\operatorname{Fr}_p)=p\in\mathbb Z_\ell^\times\). The kernel of \(\log\) on \(\mathbb Z_\ell^\times\) consists of roots of unity, and \(p>1\) is not one.

**6.3.** \(V_M\cong\mathbb Q_\ell[R]\) has dimension \(2\), and \(\mathcal O_M^\times=\{\pm1,\pm i\}\) has logarithm \(0\), so \(U_M=0\) and \(\mathcal X_\ell(M)\cong V_M^\vee\cong\mathbb Q_\ell[R]\), the sum of the two characters of \(R=\{1,c\}\).

**6.4.** A rational prime \(p\equiv3\pmod4\) is inert in \(M\), so its prime \(v=pO_M\) is fixed by \(c\), and \(-x(\operatorname{Fr}_v)=(cx)(\operatorname{Fr}_v)\), which equals \(x(\operatorname{Fr}_{c^{-1}v})=x(\operatorname{Fr}_v)\). By Lemma 2.1(3), \(\operatorname{res}_{M/\mathbb Q}\operatorname{cor}_{M/\mathbb Q}x=x+cx=0\), and restriction is injective. These primes have absolute residue degree two, so (1) does not apply; and the corestriction vanishes, so (3) does not apply. Indeed Proposition 4.1(2) with \(\delta=c\) gives only \(E_{\langle c\rangle}x=0\), which holds.

**6.5.** For \(G=\widehat{\mathbb Z}\) written additively, \(H=n\widehat{\mathbb Z}\) and representatives \(t_i=i\), \(0\le i<n\): for \(g=1\), \(1+t_i=t_{i+1}\) for \(i<n-1\) and \(1+t_{n-1}=t_0+n\). So \(\operatorname{cor}(y)(1)=y(n)\), and by continuity \(\operatorname{cor}(y)(g)=y(ng)\). Then \(\operatorname{cor}(x|_H)(g)=x(ng)=nx(g)\), which is (2); and \(\operatorname{cor}(y)|_H=n\,y\), the sum of the \(n\) trivial translates, which is (3).

## References

- [OpenAI-UC] OpenAI, *Open Homomorphisms of Global Solvably Closed Galois Groups*, OpenAI Math Release preprint, 5 October 2026, Sections 3.2 and 3.3. https://github.com/openai/math/tree/main/preprints/Open-Homomorphisms-of-Global-Solvably-Closed-Galois-Groups-October-5-2026
