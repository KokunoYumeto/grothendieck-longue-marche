# The intermediate Q injection is refuted by an exact extra stabilizer

This is a new post-recovery result for the eighth-hour review. It is not inserted in the delayed seventh-hour formal register. All computations below use the original B61 common-base braid words restored from verified checkpoint06 and the freshly rerun exact action certificate.

Let

\[
Q=\langle a,t,c,f,e\mid[a,t]=[c,f]=1\rangle
  =\langle a,t\rangle*\langle c,f\rangle*\langle e\rangle
  \cong\mathbb Z^2*\mathbb Z^2*\mathbb Z.
\]

The actual intermediate map \(Q\to PB_5\), obtained from the cyclic rigid family by deleting label5, **is not injective**. The same finite word also gives a nontrivial element of the kernel of its completed map, since its nontriviality is detected by an explicit finite quotient of Q. This result does not settle injectivity of the original six-strand map \(\theta_5\).

## Structural derivation

In the rank-four Birman fiber use the certified basis \((C,T,R,S)\), and put \(V=T^{-1}RT\). The already certified action of f fixes each of

\[
C,\quad V,\quad ST.
\]

Write \(\beta=ae\). Direct substitution in the certified a and e automorphisms gives

\[
\beta(C)=pCp^{-1},\qquad
p=(RT)^{-1}S^{-1}=V^{-1}(ST)^{-1}.
\]

Since f fixes both p and C, it fixes \(\beta(C)\). Therefore

\[
g=\beta^{-1}f\beta=(ae)^{-1}f(ae)
\]

fixes C. Under the genuine Birman free-group homomorphism the source element c maps to \(C^{-1}\), so g fixes that element as well. Consequently the actual five-strand braids satisfy

\[
 [g,c]=1.
\]

The composition convention here is \(\alpha_{ae}=\alpha_a\circ\alpha_e\). The last-conjugator extraction is antihomomorphic, as explicitly checked in the reconstructed action program. Inverting all extracted words supplies the homomorphism, and automorphisms commute with inversion; thus this convention correction preserves the fixed-word argument. The fresh calculation also evaluates the original braid word directly by the faithful Artin action, so the conclusion does not depend solely on the convention discussion.

## Nontriviality in Q

The complete source word is

\[
w=[e^{-1}a^{-1}fae,c]
 =e^{-1}a^{-1}fae\,c\,e^{-1}a^{-1}f^{-1}ae\,c^{-1}.
\]

In the free product \(A*B*E\), with \(A=\langle a,t\rangle\), \(B=\langle c,f\rangle\), \(E=\langle e\rangle\), its twelve nonidentity syllables lie successively in

\[
E,A,B,A,E,B,E,A,B,A,E,B.
\]

Every consecutive pair belongs to distinct factors. This is a nonempty reduced free-product normal form, so \(w\ne1\) in Q.

For an independent finite witness, map \(a,c,f\) to \((1\ 2)\), map e to \((2\ 3)\), and map t to the identity in \(S_3\). Both defining commutations of Q hold. The image of w is a nontrivial three-cycle. Thus w is also nonidentity in \(\widehat Q\), without requiring a general residual-finiteness citation.

In the original cyclic meridian basis, \(a=f_0,e=f_4,f=f_5,c=f_2\). With signed index j denoting \(f_{j-1}\), the source word is exactly

```text
(-5,-1,6,1,5,3,-5,-1,-6,1,5,-3).
```

## Actual braid verification and scope

`refute_Q_injection.py` first checks the structural fixed-word identities in the certified automorphisms. It then substitutes the complete source word into the fresh five-strand deletions and evaluates the faithful Artin action. All five image words are their respective single generators, so the five-strand braid is literally the identity.

The same program substitutes w into the original six-strand rigid images. Its Artin images have lengths

```text
(15705,9489,9119,6417,30465,15129).
```

In particular the first image differs from its single generator, proving nonidentity in \(PB_6\). The source is a commutator, so its exponent sum is zero; the fixed-pair linking criterion of B65 removes the central full-twist ambiguity as well. This is therefore not a kernel element of the full seven-point sphere map.

The exact complete code, fresh stdout and JSON certificate are `refute_Q_injection.py`, `refute_Q_injection.out` and `Q_noninjection_certificate.json`. The JSON stores the five-strand identity images and the full first six-strand nonidentity image, in addition to all source and braid words.

## Consequence for the orbit-family route

The stabilizer of C in the actual base free group \(L=F(a,f,e)\) is larger than the previously visible cyclic group \(\langle f\rangle\). It contains both f and \((ae)^{-1}f(ae)\); these generate a nonabelian free subgroup of L. Indeed the second word is not in \(\langle f\rangle\), and the free-group centralizer of f is \(\langle f\rangle\).

Consequently the C-orbit family indexed by \(L/\langle f\rangle\) already has repeated actual elements. The proposed free independence of the two coset-indexed C/T families is false. Adding this single relation produces another quotient through which the intermediate map factors, but completeness of the enlarged presentation is not claimed. The exact full theta5 kernel and its full profinite topology remain open.
