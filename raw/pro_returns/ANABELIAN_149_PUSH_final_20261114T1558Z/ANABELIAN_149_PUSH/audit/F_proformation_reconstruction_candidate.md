# Candidate F.44: reconstruction beyond prosolvable normal closures

Status: candidate for independent review; not integrated. The statement concerns the actual closed-point-preserving CHW convention, not the literal unrestricted version already refuted in F.1 and F.17. It gives a new sufficient arithmetic field class, not the intrinsic converse classification requested in F.9.

## 1. Statement

Let \(\mathcal C\) be a proper subclass of the finite groups, invariant under isomorphism, containing every finite cyclic group and closed under subgroups, quotients and extensions. For a finitely generated field \(K/\mathbf Q\), fix a separable closure and let \(K^{\mathcal C}\) be the compositum of its finite Galois extensions whose Galois groups belong to \(\mathcal C\).

**Candidate theorem.** Every subfield of a finitely generated extension of \(K^{\mathcal C}\) has the all-scheme étale reconstruction property under the actual pinned, closed-point-preserving convention of CHW.

Equivalently, the sufficient class consists of fields \(k_0\) algebraic over some finitely generated \(F_0/\mathbf Q\) such that the normal closure of \(k_0/F_0\) has a virtually pro-\(\mathcal C\) Galois group. This is an equivalence between two descriptions of the proposed sufficient class, not an equivalence with reconstruction for all fields.

This class can strictly exceed F.43. For example, let \(\mathcal C_{60}\) consist of finite groups all of whose nonabelian simple composition factors have order at most \(60\). Then \(\mathbf Q^{\mathcal C_{60}}\) satisfies the theorem and does not belong to F.43's virtually prosolvable sufficient class.

## 2. Elementary group facts and the maximal extension

The closure assumptions imply closure under finite products and subdirect products. Thus the finite Galois \(\mathcal C\)-extensions of \(K\) are directed under compositum, and their union \(k=K^{\mathcal C}\) is Galois over \(K\). Every finite quotient of \(\operatorname{Gal}(k/K)\) lies in \(\mathcal C\). Closed subgroups and quotients of a pro-\(\mathcal C\) group are pro-\(\mathcal C\): each of their finite quotients is a quotient of a subgroup of a finite quotient of the original group.

Because \(\mathcal C\) contains cyclic groups and is extension-closed, it contains every finite solvable group. In particular it contains all finite abelian groups.

There is \(n_0\ge5\) such that
\[
 A_n\notin\mathcal C \qquad (n\ge n_0).
 \tag{1}
\]
Indeed, if arbitrarily large \(A_n\) belonged to \(\mathcal C\), every finite group \(G\) would belong to it. Embed \(G\) in \(S_{|G|}\) by its regular permutation representation and then embed
\[
 S_m\hookrightarrow A_{m+2},\qquad
 \pi\longmapsto \pi\,(m+1\ m+2)^{\epsilon(\pi)}.
\]
Here \(\epsilon(\pi)\) is zero for an even permutation and one for an odd one. Padding with fixed letters embeds this alternating group in every larger alternating group. Subgroup closure would then give \(G\in\mathcal C\), contrary to properness.

Thus “omits arbitrarily large alternating groups” can be replaced by the more convenient uniform exclusion (1). No classification of finite simple groups is used.

## 3. Constants, missing number fields, and finite descent

Put \(C_0=K\cap\overline{\mathbf Q}\). It is a number field and \(K/C_0\) is regular. The finite relative-algebraic-closure assertion is the same opened Stacks Lemma 9.26.11 used in F.43. The Galois restriction identity used below is the same Milne Proposition 7.15/Corollary 7.16:
\[
 \operatorname{Gal}(EL/L)\simeq
 \operatorname{Gal}(E/(E\cap L))
 \quad(E/F\text{ finite Galois},\ L/F\text{ arbitrary}).
 \tag{2}
\]

Exactly as in F.43,
\[
             K^{\mathcal C}\cap\overline{\mathbf Q}
                       =C_0^{\mathcal C}.
 \tag{3}
\]
One inclusion follows by base-changing a finite Galois \(\mathcal C\)-extension of \(C_0\) to the regular extension \(K\). For the other, let an algebraic number \(a\) lie in a finite Galois \(\mathcal C\)-extension \(E/K\) inside \(k\). If \(N/C_0\) is the normal closure of \(C_0(a)\), regularity identifies its \(C_0\)-conjugates with its \(K\)-conjugates. Normality of \(E/K\) gives \(N\subset E\), and \(\operatorname{Gal}(N/C_0)\simeq\operatorname{Gal}(KN/K)\) is a quotient of \(\operatorname{Gal}(E/K)\). It belongs to \(\mathcal C\), proving (3).

For every sufficiently large \(n\), Hilbert specialization gives an \(S_n\)-Galois extension \(N/C_0\). Its intersection with \(C_0^{\mathcal C}\) is exactly \(N^{A_n}\). The intersection is Galois over \(C_0\); its group is a quotient of \(S_n\) lying in \(\mathcal C\). The image of the simple \(A_n\) must be trivial, since otherwise it would embed as a subgroup of a group in \(\mathcal C\). Hence the intersection is contained in \(N^{A_n}\). Conversely, the quadratic extension \(N^{A_n}/C_0\) lies in \(C_0^{\mathcal C}\). Therefore
\[
 [Nk:k]=|A_n|,\qquad [k\overline{\mathbf Q}:k]=\infty.
 \tag{4}
\]
The degree assertion follows from (2) and (3).

If \(L/k\) is finitely generated, the relative algebraic closure of \(k\) in \(L\) is finite. Consequently \(L\) cannot contain \(\overline{\mathbf Q}\). There is a finite Galois **number field** \(N_0/\mathbf Q\) not contained in \(L\). This is the exact missing-constant predicate required by F.35's split arithmetic places; merely having a missing finite extension of \(K\) would not suffice.

For any finite collection of schemes, maps, points, values and coefficients over \(L\), choose a finitely generated \(F/\mathbf Q\) inside \(L\), containing \(K\), with \(L=Fk\), and containing that collection's finite descent data. Then
\[
           L/F\text{ is Galois pro-}\mathcal C.
 \tag{5}
\]
Indeed restriction embeds its Galois group as a closed subgroup of \(\operatorname{Gal}(k/K)\). Finite extensions of \(L\), together with finitely many elements in them, are contained in \(Mk\) for a finite extension \(M/F\), after enlarging \(F\) by finitely many elements algebraic over \(K\). All such descent fields remain finitely generated over \(\mathbf Q\).

## 4. Divisibility: no solvability is needed in the fixed-field argument

The field \(k\) contains every root of unity. It is radically closed: given \(a\in k^\times\), place it in a finite Galois \(\mathcal C\)-extension \(E/K\); adjoin the needed roots of unity and \(n\)-th roots of every \(K\)-conjugate of \(a\). The resulting normal extension has an abelian group over the intermediate field containing the roots of unity and a \(\mathcal C\)-group over \(K\). Extension closure puts the whole Galois group in \(\mathcal C\). Thus \(k^\times\) is divisible.

For every finitely generated \(F/\mathbf Q\), the divisor and number-field-unit argument of F.43 gives
\[
                 D(F^\times)=\bigcap_{n\ge1}(F^\times)^n=1.
 \tag{6}
\]
Here a normal proper model puts an element with all divisors zero, and all its roots, in the finite number field of constants. All finite valuations then vanish, so the number-field unit theorem finishes.

Let \(E/k\) be finite. Enlarge to \(Mk/k\), with \(M/K\) finite Galois, and put \(B=M\cap k\). The two Galois extensions \(M/B\) and \(k/B\) are disjoint, so their factors commute in the compositum. For a fixed \(a\in Mk\), choose a finite \(S/K\) inside \(k\), containing \(B\) and all coefficients needed to write \(a\), and put \(F=MS\). This finitely generated field is fixed before considering any root level.

For \(z^n=a\) in \(Mk\), \(\sigma\in\operatorname{Gal}(Mk/k)\) and \(\tau\in\operatorname{Gal}(Mk/F)\), the automorphisms \(\sigma,\tau\) commute, and \(\tau z/z\in\mu_n\subset k\). Therefore
\[
 \tau(\sigma z/z)
 =\frac{\sigma(\tau z/z)}{\tau z/z}\,\sigma z/z
 =\sigma z/z.
\]
Thus \(\sigma z/z\in F\), and \(\sigma a/a\in(F^\times)^n\). If \(a\) is infinitely divisible in \(Mk\), equation (6) gives \(\sigma a=a\) for all \(\sigma\), so \(a\in k\). The converse is radical closedness. The normal-proper-model divisor argument over \(k\), including its finite relative constants, now gives
\[
                  D(L^\times)=k^\times
 \tag{7}
\]
for every finitely generated \(L/k\), and likewise after every finite extension of \(L\).

Only normality, roots of unity, radical closedness and finite generation entered this argument. There is no assertion that the finite Galois group \(\operatorname{Gal}(Mk/k)\) is solvable.

## 5. The precise replacement for finite-quotient detection

Let \(U/L\) be a smooth geometrically connected curve and \(Y\to U\) a connected finite \(G\)-torsor. Descend the smooth proper completion, the open, the entire \(G\)-action and the torsor identity to \(F\) as in (5). Let \(M/F\) be the finite Galois constant field of the cover, and write
\[
 1\longrightarrow N\longrightarrow G\longrightarrow
 P=\operatorname{Gal}(M/F)\longrightarrow1.
\]
Connectedness after base change gives \(M\cap L=F\).

The generic-pencil construction in F.24 works over the finitely generated characteristic-zero field \(F\). Choose its unbounded degree \(n\) larger than \(n_0\) and \(2g+3\). The length-at-most-four jet estimates give simple branch, distinct branch values, and boundary images disjoint from those values and from one another. The ordered lift construction uses one common constant field \(M\), giving a Galois closure with group
\[
 H\subset (G\times_P\cdots\times_PG)\rtimes S_n.
 \tag{8}
\]
The geometric monodromy acts transitively on one geometric \(M\)-component. The spanning-tree gauge makes a literal \(S_n\) lie in \(H\). Its other branch generators supply base elements
\[
 u\in H\cap N^n
\]
of support at most two, whose coordinate labels generate \(N\). These are exactly the geometric conclusions proved in F.24. Neither full wreath monodromy nor equality of the Galois closure's constants with \(M\) is asserted.

The field \(F\) is Hilbertian, by the proof in F.34 using Serre Corollary 3.2.2 and Theorem 3.4.1. Apply the full-group specialization Proposition 3.3.1 to obtain \(\Omega/F\) with group \(H\). Set
\[
 J=\operatorname{Gal}(\Omega L/L)
   =\operatorname{Gal}(\Omega/(\Omega\cap L))\triangleleft H .
\]
Normality follows from (5). The finite quotient \(H/J\) belongs to \(\mathcal C\). Since \(A_n\) is simple and \(A_n\notin\mathcal C\), its image in \(H/J\) is trivial:
\[
                         A_n\subset J.
 \tag{9}
\]
This is the replacement for the prosolvable argument. **It does not assert \(H^\infty\subset J\)**, which need not hold for the new classes.

For a support-at-most-two base element \(u\), select \(i\) in its support and choose \(\tau\in A_n\) with \(\tau^{-1}(i)\) outside that support. Since \(J\triangleleft H\) and \(\tau\in J\),
\[
 [u,\tau]\in J\cap N^n,\qquad
 [u,\tau]_i=u_i u_{\tau^{-1}(i)}^{-1}=u_i.
 \tag{10}
\]
Conjugating by the literal \(S_n\subset H\) preserves \(J\) and transports these labels to any selected coordinate. Hence \(J\cap N^n\to N\) is surjective in each coordinate.

Also \(J\to P\) is surjective, by (2) and \(M\cap L=F\). Let \(J_i=J\cap\operatorname{Stab}(i)\). Its coordinate homomorphism to \(G\) contains \(N\), by (10). Given any specified image in \(P\), choose \(h\in J\) with that image and then a literal \(\tau\in A_n\) moving \(h(i)\) back to \(i\). It has trivial constant image, so \(\tau h\in J_i\) retains the specified image in \(P\). Consequently
\[
                             J_i\twoheadrightarrow G.
 \tag{11}
\]
No perfectness of \(P\), \(J\) or \(G\) is needed.

The transitive \(A_n\subset J\) makes the specialized degree-\(n\) fibre of the pencil one closed point \(x\in U\). Its decomposition group has image \(J_i\), so it detects the entire prescribed finite **arithmetic** quotient \(G\). Since the degrees \(n\) are unbounded, detecting points have unbounded degrees.

F.29's geometric-component-preserving Bertini argument extends this to every smooth geometrically connected quasiprojective source: apply the opened Poonen–Slavov Theorem 1.5 to all geometric components of the finite cover, retain the arithmetic permutation on those components, and reduce to a curve. The infinite ground field supplies points in the simultaneous good hyperplane opens.

## 6. The Gauss-valuation integrality argument: unchanged predicates

We spell out the parts where a hidden prosolvability assumption could have entered. For an open punctured line over \(L\), a compatible Kummer class with actual values on points over all finite extensions has, after normalization at \(x_0\), the expression
\[
 \kappa(b_0)+\sum_j\lambda_j([P_j(T)]-[P_j(x_0)]),
 \qquad \lambda_j\in\widehat{\mathbf Z}.
 \tag{12}
\]
Choose a finitely generated \(F_0\) containing \(K\), the coefficients and normalization, with \(L=F_0k\). Take a finite Galois \(M/\mathbf Q(t_1,\ldots,t_d)\) containing \(F_0\), every root of the \(P_j\), and the missing number field \(N_0\) supplied in Section 3. There is \(\sigma\in\operatorname{Gal}(Mk/L)\) moving \(N_0\); it preserves \(M\). Its action on the finite Galois constant field \(C_M=M\cap\overline{\mathbf Q}\) is nontrivial.

The normal, \(\sigma\)-stable model and completely split good constant primes of F.35/F.43 yield pairwise separated Gauss valuations \(v_i,\sigma^{-1}v_i\). CRT imposes a simple zero of \(P_i(\alpha)\) at \(v_i\) and excludes every root at \(\sigma^{-1}v_i\). All coefficients, but not necessarily all roots, are fixed by \(\sigma\). Thus
\[
 v_i(P_j(\alpha))=\delta_{ij},\qquad
 v_i(P_j(\sigma\alpha))=0.
 \tag{13}
\]
When the transcendence degree is positive, the residue field is infinite; in degree zero choose the completely split primes larger than the finite root-avoidance bound. This is the exact arithmetic model argument already proved in F.43.

Let \(b_\alpha\in Mk\) be the actual value. Choose finite \(S_0/K\) inside \(k\) with \(F=MS_0\) containing \(b_\alpha\). The field \(F\) is finite over \(M\), is \(\sigma\)-stable, and is fixed independently of all radical levels. For \(\tau\in\operatorname{Gal}(Mk/F)\), the maps \(\sigma,\tau\) commute: on \(M\), \(\tau\) is the identity and \(\sigma\) preserves \(M\); on \(k\), \(\sigma\) is the identity and \(\tau\) preserves \(k\), because it fixes \(K\) and \(k/K\) is normal. This is the only normality requirement. Pro-\(\mathcal C\) need not be prosolvable.

Apply the fixed-field radical calculation in Section 4 to the evaluated relation (12). For \(R_j=P_j(\sigma\alpha)/P_j(\alpha)\), the norm valuations \(v_i\circ N_{F/M}\) give
\[
 [F:M]\lambda_i
       =-(v_i\circ N_{F/M})(\sigma b_\alpha/b_\alpha)
                         \in\mathbf Z\subset\widehat{\mathbf Z}.
 \tag{14}
\]
Since \(\mathbf Q\cap\widehat{\mathbf Z}=\mathbf Z\), all \(\lambda_i\) are ordinary integers. The class is the Kummer class of an actual regular unit, and its residual actual pointwise ratios belong to \(k^\times\), by (7).

Thus every model, fixed-field, roots-of-unity, norm and divisibility predicate used by F.35 is retained. Replacing the fixed finite field \(F\) by fields varying with the radical level would not justify (14); the field here is fixed exactly as in F.43.

## 7. Generalized Albanese, point functions, and CHW

The remaining argument in F.36/F.43 uses the preceding predicates, not solvability.

For a smooth pointed affine source \(X/L\), descend its generalized Albanese \(A\) to an \(F\) as in (5), and put \(H=G_L\triangleleft G_F\). The integral comparison
\[
 H^1(X_{\bar L},\mathbf Z_\ell(1))
       =\operatorname{Hom}(T_\ell A,\mathbf Z_\ell(1))
\]
is exactly the opened Spiess–Szamuely comparison used in F.30; its finite fundamental-group kernel disappears after Hom into a torsion-free target.

Because all roots of unity lie in \(L\), a normalized geometric Kummer functional extends as an arithmetic homomorphism. In \(W=(V_\ell A)_H\), the images of point Kummer homomorphisms span: an integral annihilating functional, reduced at a nonzero finite level, would contradict Section 5's arithmetic finite-quotient detection. Choose finitely many spanning images. Their defining points and actual values descend to one finitely generated \(M/\mathbf Q\). Restriction to \(G_{Mk}\) preserves their rational spans because it has finite index in the corresponding point groups.

Normality of \(G_L\) in \(G_F\), combined with the actual-value Kummer identities, makes the functional \(G_M\)-equivariant on the spanning images and therefore on \(W\). The opened Jannsen Theorem 4.3(ii), p.676, applies over the finitely generated field \(M\), giving a semiabelian character in the normalized unit lattice tensored with \(\mathbf Z_\ell\). It is not applied over the infinite algebraic field \(k\).

The F.27 norm to a punctured line and (14) make curve residues integral; the norm weights are residue degrees, and the selected boundary point has degree one. Transverse complete-intersection curves carry each higher-dimensional boundary coefficient unchanged. The integral divisor matrix then makes all unit exponents ordinary integers. This kills the Picard–Tate component of the particular compatible class, without asserting the whole Picard–Tate module vanishes.

Equation (7) leaves pointwise scalar ambiguity only in \(k^\times\). Section 5 supplies points of unbounded degrees. The pole-divisor argument of F.28/F.43 applies word for word: pull back \(T-1\) and then \(T-b\), with \(b\in k^\times\), to force a nonconstant point function to equal one regular unit. If the normalized Kummer unit is constant, first pass to a finite extension containing \(\beta\) with \(\beta/h\notin k\), available from (4); pull back \(T-\beta\) and apply the same high-degree argument. All finite-extension hypotheses were established above. Two-point smooth curves treat arbitrary dimension.

Thus the precise hypothesis CHW Theorem 4.18(5) holds over every finitely generated \(L/k\): a pinned relative morphism from a connected regular affine pointed source to \(\mathbf G_m\) has an algebraic geometric-point function. The opened theorem, with no extra amenability hypothesis, supplies the entire all-scheme reconstruction statement. Equality on geometric points is not substituted for its full étale-chart comparison.

## 8. Arbitrary subfields and the equivalent sufficient-class description

Let \(k_0\subset L\), with \(L/k\) finitely generated. Choose a finite transcendence basis \(B\) for \(k_0/\mathbf Q\), put \(F_0=\mathbf Q(B)\), and choose a finitely generated \(F\subset L\) containing \(K,B\) and generators of \(L/k\). Then \(L/F\) is Galois pro-\(\mathcal C\). Let \(C\) be the relative algebraic closure of \(F_0\) in \(F\); it is finite over \(F_0\), and \(F/C\) is regular.

For \(a\in k_0\), let \(N/C\) be the normal closure of \(C(a)/C\). Regularity identifies its \(C\)-conjugates with its \(F\)-conjugates, so normality of \(L/F\) puts \(N\subset L\). The group
\[
 \operatorname{Gal}(N/C)\simeq\operatorname{Gal}(FN/F)
\]
is a finite quotient of the pro-\(\mathcal C\) group in (5), hence belongs to \(\mathcal C\). Therefore
\[
                       k_0\subset C^{\mathcal C}.
 \tag{15}
\]
Both fields are algebraic over \(F_0\subset k_0\), so the extension \(C^{\mathcal C}/k_0\) is algebraic. Apply the theorem just established over \(C^{\mathcal C}\), then F.32's algebraic-extension descent. One does not descend along the possibly transcendental extension \(k_0k/k_0\).

If the normal closure \(N/F_0\) of an algebraic extension \(k_0/F_0\) has an open pro-\(\mathcal C\) subgroup \(H\), its fixed field \(C=N^H\) is finite over \(F_0\), and \(N/C\) is Galois pro-\(\mathcal C\). Hence \(k_0\subset C^{\mathcal C}\), giving the sufficient class.

Conversely (15) places a field in the embedding class inside \(C^{\mathcal C}\) with \(C/F_0\) finite. Let \(C'/F_0\) be the finite normal closure of \(C\). There are only finitely many \(F_0\)-conjugates \(L_1,\ldots,L_r\) of \(C^{\mathcal C}\), because an embedding's restriction to \(C\) determines its image maximal \(\mathcal C\)-extension. Their compositum \(E/F_0\) is Galois and contains \(C'\). The extensions \(C'L_i/C'\), obtained by base change from \(L_i/C_i\) where \(C_i\) is the corresponding conjugate of \(C\), are Galois pro-\(\mathcal C\). The group of \(E/C'=(C'L_1)\cdots(C'L_r)/C'\) embeds as a closed subgroup of the finite product of their Galois groups. Thus \(E/C'\) is pro-\(\mathcal C\). The normal closure of \(k_0/F_0\) has a quotient of this virtually pro-\(\mathcal C\) Galois group, and is again virtually pro-\(\mathcal C\).

## 9. A strict example beyond F.43

For any positive integer \(B\), define \(\mathcal C_B\) as the finite groups whose nonabelian simple composition factors have order at most \(B\). This class contains cyclic groups and is closed under quotients and extensions by the Jordan–Hölder theorem. For subgroup closure, intersect a subgroup with a composition series of the ambient group. The resulting factors are subgroups of the original simple factors. A subgroup of a cyclic prime-order factor is cyclic or trivial; a subgroup of a nonabelian simple factor of order at most \(B\) has only composition factors of order at most \(B\). Refining the series proves the assertion. Since \(|A_n|>B\) for large \(n\), the class is proper.

Take \(B=60\), so \(S_5\in\mathcal C_{60}\). There are infinitely many jointly linearly disjoint \(S_5\)-Galois extensions \(N_i/\mathbf Q\).

Here is a complete regular-family check for that assertion. The map
\[
                  \mathbf P^1_x\longrightarrow\mathbf P^1_t,
                         \qquad t=x^5-x
\]
has four simple finite critical points \(5x^4=1\), with distinct critical values \(-4x/5\). Its finite inertia generators are transpositions. Connectedness makes their transposition graph connected, since the loop at infinity is the inverse of their product. These transpositions generate \(S_5\). Thus the geometric monodromy is \(S_5\); the arithmetic monodromy, a subgroup of \(S_5\) containing it, is also \(S_5\), and its Galois closure is regular over \(\mathbf Q\). This is also exactly the opened Serre Theorem 4.4.1, p.39, whose Morse hypotheses have just been verified.

For a prescribed finite Galois extension \(M/\mathbf Q\), the constant base change of this regular family has full product group \(S_5\times\operatorname{Gal}(M/\mathbf Q)\). Hilbert full-group specialization gives a new \(S_5\)-extension disjoint from \(M\). Iterating with \(M=N_1\cdots N_r\) gives the desired jointly disjoint family. The opened exact source is Serre Proposition 3.3.3 and Corollary 3.3.4, p.24, in addition to Proposition 3.3.1, p.23, and Theorem 3.4.1, p.25.

All \(N_i\) lie in \(k=\mathbf Q^{\mathcal C_{60}}\), and compactness gives a quotient
\[
             \operatorname{Gal}(k/\mathbf Q)
                         \twoheadrightarrow\prod_{i\ge1}S_5.
 \tag{16}
\]
The image of every open subgroup is open in the product and contains all coordinate factors outside a finite set. In particular it has a non-solvable finite quotient \(S_5\). Hence no open subgroup of \(\operatorname{Gal}(k/\mathbf Q)\) is prosolvable.

If this algebraic field \(k/\mathbf Q\) belonged to F.43's sufficient class, it would be algebraic over a finitely generated subfield \(F_0\subset k\). Such an \(F_0\) is a number field. Its normal closure over \(F_0\) is \(k\) itself, since \(k/\mathbf Q\) is Galois. F.43's equivalence would then give an open prosolvable subgroup of the open subgroup \(\operatorname{Gal}(k/F_0)\), contradicting (16). Thus the new class strictly exceeds F.43.

No explicit finite specialization is needed for this existence theorem, and no numerical inverse-Galois assertion is being made without proof.

## 10. An explicit arithmetic description of the union of sufficient classes

For \(m\ge5\), let \(\mathcal D_m\) be the finite groups having no subquotient isomorphic to \(A_m\), where a subquotient means a quotient of a subgroup. This is a proper subclass containing all cyclic groups and closed under subgroups and quotients.

It is also extension-closed. Suppose \(N\triangleleft G\), and suppose a subgroup quotient \(H/L\) of \(G\) is the simple group \(A_m\). The image of \(H\cap N\) in \(H/L\) is normal, hence either trivial or all of \(A_m\). In the first case, \(H\cap N\subset L\), and the subgroup \(H/(H\cap N)\subset G/N\) has quotient \(A_m\). In the second case \((H\cap N)/(L\cap N)\simeq A_m\) is a subquotient of \(N\). Thus if both \(N\) and \(G/N\) belong to \(\mathcal D_m\), so does \(G\).

These subclasses are cofinal among the subclasses allowed by the theorem. Given a proper \(\mathcal C\), choose a finite \(G_0\notin\mathcal C\), and embed \(G_0\) in \(A_m\) for some \(m\ge5\) using the parity-adjusted regular representation from Section 2. Then \(A_m\notin\mathcal C\). No group in \(\mathcal C\) can have an \(A_m\) subquotient, by subgroup and quotient closure, so
\[
                          \mathcal C\subset\mathcal D_m.
 \tag{17}
\]

Consequently the union, over all allowed \(\mathcal C\), of the theorem's sufficient classes has the following explicit equivalent description: there is a finitely generated subfield \(F_0\subset k_0\) over which \(k_0\) is algebraic; and the Galois group of its normal closure has an open subgroup \(H\) such that, for one \(m\ge5\), no finite continuous quotient of \(H\) has \(A_m\) as a subquotient.

This criterion uses the arithmetic of a finite-generation model and its normal closure, not just the abstract absolute Galois group of \(k_0\). It is a sufficient criterion. Necessity for arbitrary reconstruction fields, and therefore F.9's full classification, remains unresolved.

The fields \(k_m=\mathbf Q^{\mathcal D_m}\), \(m\ge5\), form an increasing sequence: \(A_m\subset A_{m+1}\) gives \(\mathcal D_m\subset\mathcal D_{m+1}\). Every finite group \(G\) lies in some \(\mathcal D_m\), since \(|A_m|>|G|\) excludes an \(A_m\) subquotient. Thus every finite Galois extension of \(\mathbf Q\) lies in one \(k_m\), and
\[
                         \bigcup_{m\ge5}k_m=\overline{\mathbf Q}.
 \tag{18}
\]
Each \(k_m\) is radically closed and reconstructs by the theorem, while their increasing algebraic union fails by F.41. In particular the reconstruction property is not preserved by increasing algebraic unions, even with these stronger properties of the stages. This is a consequence of the existing positive and negative theorems, not another classification assertion.

## 11. Source and scope audit

The new group-theoretic assertions are proved above. All arithmetic/geometric inputs are the opened primary sources already used in F.24 and F.32–F.43:

- Milne, *Fields and Galois Theory*, Proposition 7.15 and Corollary 7.16, p.99: finite Galois restriction and the intersection field.
- Stacks Lemma 9.26.11: finiteness of relative constants.
- Serre, *Topics in Galois Theory*, Corollary 3.2.2, p.22; Proposition 3.3.1, p.23; Proposition 3.3.3 and Corollary 3.3.4, p.24; Theorem 3.4.1, p.25; Theorem 4.4.1, p.39. The primary CNRS-hosted PDF was reopened on 14 November 2026 at https://indico.math.cnrs.fr/event/11410/attachments/4760/7351/SerreTopicsGaloisTheory.pdf. The exact linear-disjointness and Morse-family statements were read.
- The supplied SGA1 XII.5.1–5.2 comparison and F.24's explicit pencil/branch-loop proof.
- Poonen–Slavov Theorem 1.5 for finite-cover-preserving Bertini.
- Spiess–Szamuely Propositions 4.1, 4.3 and Corollary 4.2 for integral generalized-Albanese comparison.
- Jannsen, original Theorem 4.3(ii), p.676, for the integral Tate-Hom statement over a finitely generated field.
- CHW Theorem 4.18(5), with the actual pinned/closed-point-preserving convention and no extra amenability hypothesis.
- F.32's already reviewed algebraic descent, including the complemented diagonal of the separated étale basis.

Every use of prosolvability in the earlier argument is replaced by one of: normality of \(k/K\); membership of finite quotients in \(\mathcal C\); survival of sufficiently large \(A_n\); or the field predicates (3), (4), (7). The former implication \(H^\infty\subset J\) is expressly removed.

This candidate neither settles F.9's intrinsic converse nor claims that every reconstructing field has a virtually pro-\(\mathcal C\) normal closure for some proper \(\mathcal C\).

### Targeted literature check, 14 November 2026

Both available search engines were queried with combinations of “étale topoi”, “reconstruction”, “solvable”, “pro-C”, “formation”, “Kummer” and “maximal extension”. The pertinent primary results were the already used CHW reconstruction paper and Carlson–Stix's sub-p-adic theorem. No opened primary result located by these searches stated this proper-subclass extension. This bounded search is not an exhaustive novelty determination.

The current author-hosted CHW PDF, https://math.berkeley.edu/~phaine/files/reconstruction_of_schemes_from_etale_topoi.pdf, was reopened at its introduction and Theorems 0.1/0.3. Its sufficient hypotheses there use the toric divisibility, Picard-torsion and discrete-valuation conditions. The radically closed fields used here do not satisfy its toric divisibility condition.

The official arXiv abstract and PDF of Carlson–Stix, arXiv:2410.22474v2, revised 20 September 2026, were reopened at Theorems A–D and Proposition C, pp.1–2: https://arxiv.org/abs/2410.22474 and https://arxiv.org/pdf/2410.22474. The added relative theorem concerns suitable bases with sub-p-adic function fields. It does not state the present pro-\(\mathcal C\) sufficient class. No priority claim is made.
