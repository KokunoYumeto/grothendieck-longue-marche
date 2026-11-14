# F.48 candidate: henselian Abhyankar valuations obstruct reconstruction

**Status:** separate candidate for independent review. F.47 is integrated and unchanged. This candidate strengthens a necessary condition for F.9; it does not propose a converse classification.

## 1. Precise statement

Let \(F\) have characteristic zero. Let \(\Gamma_0\) be a totally ordered free abelian group of finite rank \(r\geq1\), with a basis \(\gamma_1,\ldots,\gamma_r\) of positive elements. Equip
\[
             K_0=F(t_1,\ldots,t_r)
\]
with its monomial valuation
\[
 v\left(\sum_{\boldsymbol a}c_{\boldsymbol a}
                    t_1^{a_1}\cdots t_r^{a_r}\right)
       =\min_{c_{\boldsymbol a}\ne0}\sum_i a_i\gamma_i.
 \tag{48.1}
\]
Let \(H=K_0^h\) be its henselization. Then \(H\), and every algebraic extension of \(H\), fails closed-point-preserving étale reconstruction. There is an explicit nonconstant nonalgebraic relative automorphism of the full \(\mathbb G_m\) étale topos over \(H\), induced semilinearly by an automorphism satisfying
\[
 \sigma(t_1)=t_1+t_1^2,\qquad
 \sigma(t_i)=t_i\ (i>1),\qquad \sigma|_F=1.
 \tag{48.2}
\]
Its lift centralizes all of \(G_H\). More precisely,
\[
                  G_H\simeq\widehat{\mathbf Z}(1)^r\rtimes G_F,
 \tag{48.3}
\]
with the diagonal cyclotomic action.

Consequently, let \(K/\mathbf Q\) have finite transcendence degree \(d\), and suppose it admits a nontrivial henselian valuation \(v\), trivial on \(\mathbf Q\), with residue characteristic zero and
\[
 \operatorname{trdeg}_{\mathbf Q}\kappa(v)
       +\dim_{\mathbf Q}\bigl(v(K^\times)\otimes_{\mathbf Z}\mathbf Q\bigr)
       =d.
 \tag{48.4}
\]
Then \(K\) fails reconstruction. Thus a finite-transcendence-degree reconstruction field admits no nontrivial henselian residue-characteristic-zero valuation satisfying the Abhyankar equality (48.4). The value group need not be discrete and its order need not have rank one. No statement is made for a valuation with transcendence defect.

## 2. The monomial base and its henselization

Distinct exponent vectors in (48.1) give distinct values, since the \(\gamma_i\) are linearly independent over \(\mathbf Q\). In a product of two nonzero polynomials, the product of their two least-valued monomials is the unique term of least value. Hence the formula is multiplicative and extends to the rational-function field. Its value group is exactly \(\Gamma_0=\sum_i\mathbf Z\gamma_i\). Its residue field is \(F\): if a rational function has value zero, the least exponent vectors of its numerator and denominator coincide, so its residue is the ratio of their coefficients.

The henselization is an immediate algebraic extension. Therefore
\[
                 v(H^\times)=\Gamma_0,\qquad \kappa(H)=F.
 \tag{48.5}
\]
This is ADH, Corollary 3.3.26, author-PDF p.125, following the henselization universal property and Proposition 3.3.25. Fix an algebraic closure \(\bar H\) and the unique extension of the valuation to it; uniqueness is ADH, Proposition 3.3.11(ii), author-PDF pp.119–121.

Choose an algebraic closure \(\bar F\) of \(F\) inside \(\bar H\). The valuation is trivial on \(\bar F\). Indeed, if a nonzero element algebraic over \(F\) had positive valuation, the nonzero constant term of its minimal polynomial would be the unique term of least valuation; if it had negative valuation, the leading term would be the unique least-valued term. Both are impossible. Reduction therefore embeds \(\bar F\) in the residue field of \(\bar H\).

Choose compatible roots \(u_{i,n}=t_i^{1/n}\) inside \(\bar H\), with \(u_{i,mn}^{m}=u_{i,n}\). Such systems exist by choosing roots successively along the factorial sequence and then restricting to divisors. For each finite \(F'/F\) in \(\bar F\), put
\[
             E(F',n)=HF'(u_{1,n},\ldots,u_{r,n}).
 \tag{48.6}
\]

## 3. Exact degrees, residue fields and value groups

We first check constants without assuming a linear-disjointness theorem. Let \(e_1,\ldots,e_s\) be an \(F\)-basis of \(F'\). Their residues are \(F\)-linearly independent, since reduction on the algebraic constant field is injective. If \(h_1,\ldots,h_s\in H\) are not all zero, choose \(h_j\) of least valuation. The element
\[
          \sum_i e_i h_i/h_j
\]
has nonzero residue, because its coefficients reduce to elements of \(F\) and at least one is nonzero. Thus
\[
 v\left(\sum_i e_i h_i\right)=\min_i v(h_i).
 \tag{48.7}
\]
In particular the \(e_i\) are \(H\)-linearly independent. Their \(H\)-span is a finite-dimensional domain, closed under multiplication, so it is the field \(HF'\). Formula (48.7) proves
\[
 [HF':H]=[F':F],\qquad v((HF')^\times)=\Gamma_0,\qquad
                        \kappa(HF')=F'.
 \tag{48.8}
\]
For the last assertion, an element of value zero has all its coefficients integral and its residue is a linear combination of the residues of the \(e_i\), hence lies in \(F'\).

Now consider the \(n^r\) monomials
\[
       u_{1,n}^{a_1}\cdots u_{r,n}^{a_r},
                  \qquad 0\leq a_i<n.
 \tag{48.9}
\]
Their values have distinct classes modulo \(\Gamma_0\). Consequently a nonzero linear combination over \(HF'\) has a unique term of least value and cannot vanish. They are linearly independent. Adjoining the \(r\) roots has degree at most \(n^r\), so (48.9) is a basis and
\[
 \begin{split}
 [E(F',n):H]&=[F':F]\,n^r,\\
 v(E(F',n)^\times)&=\tfrac1n\Gamma_0,\qquad
 \kappa(E(F',n))=F'.
 \end{split}
 \tag{48.10}
\]
Here the value-group statement follows by expanding every element in that basis and taking the least value. For the residue assertion, if such a sum has value zero, its least-valued term has value in \(\Gamma_0\); among the vectors (48.9), only \(\boldsymbol a=0\) has that value class. Every other term has positive value and disappears on reduction. The residue is therefore that of a coefficient in \(HF'\), hence is in \(F'\). The opposite inclusions in both assertions are supplied by the constants and the parameter roots themselves.

The fields (48.6) form a directed union
\[
                       E=\bigcup_{F',n}E(F',n).
 \tag{48.11}
\]
It is algebraic over the henselian field \(H\), hence henselian for its inherited valuation. For example, uniqueness of the extension from \(H\) to its algebraic closure gives uniqueness for every intermediate algebraic field; Proposition 3.3.11 then applies. Formula (48.10) gives
\[
          v(E^\times)=\Gamma_0\otimes_{\mathbf Z}\mathbf Q,
                        \qquad\kappa(E)=\bar F.
 \tag{48.12}
\]
The value group is divisible and the residue field is algebraically closed. ADH, Corollary 3.3.22, author-PDF p.124, now makes \(E\) algebraically closed. It follows that \(E=\bar H\).

This verifies both the constants and all radical levels before using algebraic closedness. It uses no multivariate power-series closure assertion. Formula (48.3) is also immediate from this explicit union: restriction to \(\bar F\) has a continuous section which acts on the finite constant coefficients and fixes all \(u_{i,n}\); the kernel is the \(r\)-fold product of the compatible root-multiplier groups \(\varprojlim_n\mu_n\). The basis (48.9) shows that every such compatible choice gives an automorphism. Conjugation acts on each multiplier by the cyclotomic character.

## 4. Construct the substitution and its inverse inside \(H\)

First define a field embedding \(s_0:K_0\to H\) by the formulas in (48.2). For a monomial, the new value is unchanged: its only new factor is \((1+t_1)^{a_1}\), a unit of residue one. For a polynomial, its monomial values remain pairwise distinct, so its least value is unchanged. Hence \(s_0\) is injective and valuation preserving, and the same is true on fractions. Henselization universality extends it uniquely to a valued-field embedding
\[
                                \sigma:H\longrightarrow H.
\]

The polynomial \(X^2+X-t_1\) has a unique root \(r_1\) of positive valuation in \(H\): reduction has the simple root zero, so Hensel's lemma gives the root and its uniqueness in the maximal ideal. Since
\[
                  r_1(1+r_1)=t_1,
\]
we have \(v(r_1)=\gamma_1\) and \(r_1/t_1\) has residue one. Replacing \(t_1\) by \(r_1\), while fixing \(F\) and the other \(t_i\), is therefore another valuation-preserving field embedding \(K_0\to H\). Extend it to \(\rho:H\to H\).

On \(K_0\), the composite \(\rho\sigma\) is the identity because \(r_1+r_1^2=t_1\). Also \(\sigma(r_1)\) is a positive-valued root of
\[
                     X^2+X-(t_1+t_1^2),
\]
and \(t_1\) is another such root. Uniqueness of the lift of the simple residue root zero gives \(\sigma(r_1)=t_1\). Thus \(\sigma\rho\) is the identity on \(K_0\) as well. The uniqueness clause of henselization universality forces both composites to be the identity on \(H\). Hence \(\sigma\) is an automorphism with inverse \(\rho\), and it is nonidentity.

This argument constructs the automorphism algebraically inside the henselization. It does not presume that an arbitrary ordered value group admits a formal multiseries substitution.

## 5. Compatible roots and all-inertia centralization

For every \(n\geq1\), the polynomial \(X^n-(1+t_1)\) has a unique root \(\beta_n\in1+\mathfrak m_H\). Its derivative at residue root one is \(n\), a unit because the residue characteristic is zero. These roots satisfy
\[
                 \beta_n^n=1+t_1,\qquad
                 \beta_{mn}^{m}=\beta_n.
 \tag{48.13}
\]
The second equality follows from the uniqueness of the root with residue one, not from a choice of unrelated radicals.

On \(E(F',n)\) define \(\tau\) by
\[
 \tau|_H=\sigma,\qquad \tau|_{F'}=1,\qquad
 \tau(u_{1,n})=u_{1,n}\beta_n,\qquad
 \tau(u_{i,n})=u_{i,n}\ (i>1).
 \tag{48.14}
\]
The first two instructions define an automorphism of \(HF'\): equation (48.8) identifies it with the tensor product over \(F\), and \(\sigma\) fixes \(F\). For the root extension, the algebra
\[
 HF'[X_1,\ldots,X_r]/(X_i^n-t_i)_{i=1}^r
\]
has dimension \(n^r\), and (48.9) identifies it with the field \(E(F',n)\). The images in (48.14) satisfy the transformed defining equations. Thus (48.14) gives a well-defined field embedding. Its image contains \(H\), \(F'\), and all the \(u_{i,n}\), since \(\sigma\) is surjective and \(\beta_n\in H^\times\). It is therefore an automorphism of \(E(F',n)\).

These automorphisms agree when \(F'\) increases, and agree between root levels by (48.13) and the chosen compatibilities of \(u_{i,n}\). They define an automorphism \(\tau\) of \(E=\bar H\).

Let \(g\in G_H\). The maps \(g\tau\) and \(\tau g\) agree on \(H\), because \(g\) fixes \(H\) and \(\tau\) preserves it. They agree on \(\bar F\), because \(g\) preserves the algebraic constants and \(\tau\) fixes them. Write
\[
                  g(u_{i,n})=\zeta_{i,n}u_{i,n},
                    \qquad \zeta_{i,n}\in\mu_n\subset\bar F.
\]
For \(i=1\), both composites give
\[
                       \zeta_{1,n}u_{1,n}\beta_n,
\]
since \(g\) fixes \(\beta_n\). For \(i>1\), both give \(\zeta_{i,n}u_{i,n}\). By (48.11), these are generators of \(\bar H\) as a field, so
\[
                 \tau g=g\tau\qquad(g\in G_H).
 \tag{48.15}
\]
In particular \(\sigma\) has trivial outer Galois action although it moves \(t_1\).

F.40 now gives an actual closed-point-preserving relative automorphism of the full \(\mathbb G_m\) étale topos. Its rational point function is \(a\mapsto\sigma^{-1}(a)\). The values at \(1\) and \(2\) would force any algebraic monomial to be the identity; its value at \(t_1\) is \(r_1\ne t_1\). Thus \(H\) does not reconstruct. F.32 excludes every algebraic extension of \(H\) contrapositively. No invariance of an arbitrary algebraic extension under this particular \(\sigma\) is asserted.

## 6. Reduction of the intrinsic Abhyankar hypothesis

Let \(K,v\) satisfy (48.4), and let \(r\) be the rational rank of its value group. It is positive because \(v\) is nontrivial, and it is finite by (48.4). F.47's complete coefficient-field argument, or ADH Proposition3.3.8, supplies a subfield \(F\subset\mathcal O_v\) mapping isomorphically onto \(\kappa(v)\).

Choose \(\gamma_1,\ldots,\gamma_r\) in \(v(K^\times)\) which form a \(\mathbf Q\)-basis of \(v(K^\times)\otimes\mathbf Q\); replacing signs makes each positive. Choose \(t_i\in K^\times\) with \(v(t_i)=\gamma_i\). Every nonzero polynomial in the \(t_i\) over \(F\) has distinct monomial values, so it cannot vanish. The \(t_i\) are algebraically independent over \(F\), and the restriction to \(F(t_1,\ldots,t_r)\) is exactly (48.1), with value group \(\Gamma_0=\sum_i\mathbf Z\gamma_i\).

The Abhyankar equality gives
\[
 \operatorname{trdeg}_{\mathbf Q}F(t_1,\ldots,t_r)
       =\operatorname{trdeg}_{\mathbf Q}\kappa(v)+r
       =\operatorname{trdeg}_{\mathbf Q}K.
\]
Thus \(K/F(t_1,\ldots,t_r)\) is algebraic. Since \(K\) is henselian, the base embedding extends uniquely to a valued-field embedding of its henselization \(H\) into \(K\). The extension \(K/H\) is algebraic. Section5 excludes it.

When \(r=1\), this includes F.47's residue-drop-one criterion. For larger \(r\), it covers both higher-order-rank groups and nondiscrete archimedean orders on free abelian lattices; only rational independence and the exact equality (48.4) were used. It is a stronger necessary condition for F.9, not a sufficient one.

## 7. Opened primary sources and computational scope

The only new use of an existing bibliography source is ADH (Aschenbrenner, van den Dries, and van der Hoeven, 2017), primary author PDF at https://www.math.ucla.edu/~matthias/pdf/mt.pdf (also independently opened at https://www.texmacs.org/joris/mt/mt.pdf):

* Proposition3.3.8 and Lemma3.3.9, author pp.117–118: coefficient fields, with the full proof already reproduced in F.47.
* Proposition3.3.11(ii), author pp.119–121: henselianity is equivalent to unique extension of the valuation to every algebraic field extension.
* Corollary3.3.22, author p.124: in equicharacteristic zero, henselianity, algebraically closed residue and divisible value group imply algebraic closedness.
* Henselization definition and Proposition3.3.25, author p.125: universal property.
* Corollary3.3.26, author p.125: the henselization is immediate and algebraic.

The exact paragraphs were opened in web refs turn825view0 and turn842view0; degeneration separately opened the same author passages at turn839view0 and turn841view0–1. Published book metadata and the distinction from the729-page author-version pagination were checked for F.47. F.32 and F.40 are the previously proved topos inputs; the present argument supplies the new valued-field construction.

The existing27 exact rational identities in code/F_Puiseux_checks.py verify the same univariate inverse and root-compatibility formulas at finite order. This candidate does not use a multivariate formal-series computation: the exact arbitrary-degree roots in (48.13) and all compatibilities follow from Hensel uniqueness, and (48.10) is proved by valuation independence. No finite numerical test is presented as evidence for the henselian or Galois conclusions.

The targeted primary search made for F.47 is retained as the literature comparison; no opened source was found stating this reconstruction obstruction. No bibliographic priority claim is made.
