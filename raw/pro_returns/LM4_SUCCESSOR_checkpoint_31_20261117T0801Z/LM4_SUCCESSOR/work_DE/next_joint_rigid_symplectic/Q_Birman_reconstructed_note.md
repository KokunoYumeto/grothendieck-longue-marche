# The cyclic rigid map: a precise intermediate Birman reduction

## Recovery and mathematical status

This note reconstructs the mathematical content retained in conversation after the execution environment failed at about 07:43 UTC on 16 November 2026. It is not represented as a byte-identical restoration of the lost note. The exact supporting program `reconstruct_Q_birman.py` has been newly written and executed against the original eleven-strand monodromy words restored from verified checkpoint 06. Its `.out` and `Q_birman_reconstructed_certificate.json` contain fresh results, not reconstructed stdout.

The actual cyclic rigid map remains

\[
\theta_5:F(f_0,\ldots,f_5)\longrightarrow PB_6.
\]

Its injectivity, the injectivity of its full profinite completion, and comparison of its completed kernel with the closure of its discrete kernel are all **Open**. The results below identify a smaller exact intermediate comparison. They do not infer a presentation from a lower-central rank calculation.

**Subsequent eighth-hour update:** the proposed intermediate injection \(Q\to PB_5\) has now been refuted by the exact word \([(ae)^{-1}f(ae),c]\). Its structural derivation, nonempty Q normal form, finite S3 witness and actual Artin evaluation are recorded in `Q_noninjection_proof.md` and `refute_Q_injection.py/.out`. The word survives in PB6, so the original theta5 question remains open.

## 1. The six linear forms

In the cyclic family, put labels 1 and 3 at 0 and infinity. The fixed pentagon has labels `(2,6,12,9,4)` at `1,zeta,...,zeta^4`, and the moving pentagon has labels `(5,7,11,10,8)` at `u,u zeta,...,u zeta^4`. Retain

\[
S_+=\{1,2,4,5,6,10,11\}.
\]

After inversion of the sphere coordinate and setting \(v=u^{-1}\), label 1 is infinity, the three finite fixed points are \(1,\zeta,\zeta^4\), and the moving points are \(v,\zeta^2v,\zeta^3v\). The corresponding homogeneous root map is

\[
(x,y)\longmapsto(x,\zeta x,\zeta^4x,y,\zeta^2y,\zeta^3y),
\qquad xy(y^5-x^5)\ne0.
\]

The Vandermonde is, up to a nonzero scalar,

\[
x^3y^3(y-x)\prod_{j=1}^4(y-\zeta^jx)^2.
\]

The nine cross-pair differences have multiplicities \((1,2,2,2,2)\); the two within-triplet contributions each have multiplicity three. These integer counts and total degree fifteen are checked by the fresh program. The domain is \(\mathbb C^*\times S_5\). This is a useful precise arrangement formulation, not a general injectivity theorem for partial root maps.

## 2. Delete the endpoint of the unique simple collision

Delete moving label 5. In the actual common marking, the five finite retained labels are

\[
(4,11,1,10,6).
\]

All words in this note use the original B61 geometric meridian basis \(f_0,\ldots,f_5\). A signed integer \(j\) in the code means \(f_{j-1}\), and a negative integer its inverse. The meridian \(f_1\) has literal identity Artin action in this five-strand target. The intermediate map therefore factors through the free group obtained by filling the simple collision at \(u=1\).

In that five-generator group put

\[
t=f_5^{-1}f_4^{-1}f_0^{-1}f_2^{-1}f_3^{-1}.
\]

This is the infinity meridian **after filling \(u=1\)**. It must not be silently treated as the original six-generator infinity meridian. Its shifted signed code is `(-6,-5,-1,-3,-4)`.

The two further source words

\[
[f_0,t],\qquad[f_2,f_5]
\]

are nonempty reduced words and have literal identity Artin action in \(PB_5\). Thus this intermediate map is noninjective, both discretely and on the full profinite completion: a free group is residually finite, so either nonempty word remains nonidentity in its full completion.

Introduce the Nielsen basis

\[
(a,t,c,f,e)=(f_0,t,f_2,f_5,f_4).
\]

Its inverse formula is

\[
f_3=t^{-1}f^{-1}e^{-1}a^{-1}c^{-1}.
\]

The reconstruction program verifies this exact free-word identity. The five-strand monodromy consequently factors through

\[
Q=\langle a,t,c,f,e\mid[a,t]=[c,f]=1\rangle
  \cong\mathbb Z^2*\mathbb Z^2*\mathbb Z.
\]

**The map \(Q\to PB_5\) is noninjective**, by the subsequent exact extra-stabilizer argument recorded above. The earlier degree-two rank eight out of ten is only a diagnostic compatible with the two displayed commuting relations. It supplies no completeness theorem for the relations.

## 3. The next base is exactly a free group of rank three

Delete label 10 as well. The only moving point is label 11, at \(u\zeta^2\), and the four fixed sphere labels are \(1,2,4,6\), at \(0,1,\zeta^4,\zeta\). The retained finite order is `(4,11,1,6)`.

The coordinate \(u\mapsto u\zeta^2\) identifies the parameter sphere punctured at

\[
\{0,\zeta^2,\zeta^3,\zeta^4\}
\]

with the sphere punctured at those four fixed points. Thus the base group is literally

\[
L=F(a,f,e),
\]

and the quotient \(Q\to L\) kills \(t,c\). This base identification is geometric and remains an isomorphism after full profinite completion. The fresh exact Artin computation independently checks that both \(t,c\) vanish in the four-strand deletion.

## 4. The exact last-strand free-group action

For the five-strand stage, conjugate by the adjacent transposition that moves label 10 to the final strand. The new finite order is `(4,11,1,6,10)`. The last-strand Birman kernel is free of rank four. Write its standard free coordinates as \(y_1,y_2,y_3,y_4\), and introduce the free basis

\[
C=y_3^{-1}y_2^{-1}y_1y_2y_3,
\quad T=y_3^{-1}y_2y_3,
\quad R=y_3,
\quad S=y_4.
\]

The inverse coordinate change is

\[
y_1=RTC T^{-1}R^{-1},\qquad
y_2=RTR^{-1},\qquad y_3=R,\qquad y_4=S.
\]

Both substitutions are checked exactly. The extracted push words of \(c,t\) are \(C,T\), respectively. The convention qualification below is essential if these outputs are called a homomorphism.

The conjugation action of the base generators \(a,f,e\) is the following actual automorphism action on \(F(C,T,R,S)\):

\[
\begin{array}{c|cccc}
 &C&T&R&S\\\hline
a&(RT)^{-1}C(RT)&T&R&(RT)^{-1}S(RT)\\
f&C&STS^{-1}&[S,T]R[S,T]^{-1}&STS T^{-1}S^{-1}.
\end{array}
\]

For \(e\), put

\[
p=S^{-2}C^{-1}T^{-1}R^{-1},\qquad
U=pTp^{-1},\qquad q=US^{-1}T^{-1}.
\]

Then

\[
e(C)=S^{-1}CS,\qquad e(T)=U,\qquad
e(R)=qRq^{-1},\qquad e(S)=S.
\]

The complete signed-word substitutions are in the JSON certificate. The new run evaluates each formula from the original common-base eleven-strand words via deletion and the faithful Artin action. It also checks the images of conjugates of both \(c,t\), so the formulas are not merely an unchecked change of notation.

### The antihomomorphism convention

If a pure braid in the last-strand kernel sends the last free generator to \(q y_5q^{-1}\), the program extracts the projection of \(q\) after filling that last puncture. With the retained Artin convention, this extraction is an **antihomomorphism** on the Birman kernel:

\[
\operatorname{push}(hk)=\operatorname{push}(k)
                         \operatorname{push}(h).
\]

This was originally discovered before the runtime failure and is now freshly rechecked on two canonical pure last-strand generators; their extracted words do not commute, so the order distinction is substantive. Taking the inverse of every extracted word gives the genuine free-group homomorphism. Under that homomorphism \(c,t\) map to \(C^{-1},T^{-1}\). The displayed conjugation automorphisms remain the same, since automorphisms commute with inversion. Freeness, Stallings ranks and normal-membership conclusions are unchanged by this global correction. B65 and B66 do not rely on this extraction convention.

## 5. The exact remaining discrete comparison

The kernel of the abstract quotient

\[
Q=\mathbb Z^2*\mathbb Z^2*\mathbb Z\longrightarrow F(a,f,e)
\]

is free on the two families

\[
\{g t g^{-1}:g\langle a\rangle\in L/\langle a\rangle\},
\qquad
\{g c g^{-1}:g\langle f\rangle\in L/\langle f\rangle\}.
\]

This follows from the free-product normal form, or from the Bass–Serre tree. The quotient graph is the Bass–Serre tree of \(L=\langle a\rangle*\langle f\rangle*\langle e\rangle\), so there is no additional free factor from cycles in that graph. Since the base map is already an isomorphism, injectivity of \(Q\to PB_5\) is equivalent to free independence of the two actual orbit families

\[
\{\alpha_g(T)\}_{L/\langle a\rangle},\qquad
\{\alpha_g(C)\}_{L/\langle f\rangle}
\]

in \(F(C,T,R,S)\), with inverses inserted if the homomorphic push convention is used. The subsequent exact calculation shows that the C stabilizer also contains \((ae)^{-1}f(ae)\). Thus the free-independence condition is false, not merely unproved. The full stabilizers and a complete presentation of the actual image have not been identified.

Two tempting simplifications have not supplied the missing proof. After killing \(C,T\), the relative abelianization loses information: many orbit words have the same label in the resulting \(\mathbb Z[F(R,S)]\)-module. Moreover, the complementary factor \(\langle T,R,S\rangle\) is preserved by \(a,f\) but is not preserved by \(e\), whose formula contains \(C\). Thus neither a module-rank argument nor the simplest invariant-free-factor Cohen–Lyndon argument establishes injection.

Even a proof of this intermediate injection would leave the normal kernel of \(F_6\to Q\) to compare in the final free fiber for \(PB_6\). A discrete proof would in turn leave the full induced profinite topology to establish. Injectivity of a completed relation module alone is insufficient; one would need, for example, an actual finite-cover construction extending every finite source quotient or a justified profinite graph argument.

## 6. Literature boundary

The general full-orbit pullback constructions in Cohen's orbit-configuration work supply a bundle and a monodromy factorization. A space embedding of the full root map does not automatically prove injectivity of this partial-root map on fundamental groups, still less on their full profinite completions.

Likewise, a generic multitwist right-angled Artin group assertion is unavailable for the present unpowered generators. Jankiewicz and Schreve's *Right-angled Artin subgroups of Artin groups* (2022), Example 5.8, gives a lantern-based failure of the unpowered parabolic-center RAAG assertion in braid groups. Their spherical positive result uses sufficiently large powers. Their Lemma 5.4 also imposes a component-selection condition for multitwists. The exact hypotheses have not been verified here. Humphries's 1989 free-product theorem has additional intersection and complementary-region hypotheses that have likewise not been established for these actual curves.

These are limitations on proposed routes, not evidence for either answer to the remaining injection question.

## 7. The final free fiber does not reduce to one boundary orbit

Return to the full six-strand map and move label 5 to the last strand. The remaining finite labels have order `(4,11,1,10,6)`. In its rank-five free fiber let the total boundary be \(B=y_1y_2y_3y_4y_5\). A fresh run of `reconstruct_final_fiber.py` verifies that the push of \(f_1\) is conjugate to \(B^{-1}\). The push of \([a,t]\) has length 36 and remains a nonempty word of length 32 after setting \(B=1\). Thus this latter fiber element is outside the normal closure of the boundary; expressing every final-stage relation only through conjugates of the simple-collision boundary is insufficient.

The same fresh run computes the push of \([c,f]\), of length 24, whose boundary-filled word has length 30. This row is explicitly new after recovery: the old attempt to add it failed before execution. These checks neither prove nor refute injectivity of the final map.

## Reproducible files

- `check_B65_reconstructed.py` and its fresh `.out`: all finite dihedral transports, the two constant sets, six exact deletions, purity, fixed-pair linking, and the central full twist.
- `B65_reconstructed_certificate.json` and `cyclic_rigid_braid_words.json`: complete fresh B65 data.
- `reconstruct_Q_birman.py` and its fresh `.out`: both exact relations, the Nielsen change, the F3 base deletion, all three fiber automorphisms, the antihomomorphism check, and the six-form collision multiplicities.
- `Q_birman_reconstructed_certificate.json`: all actual words and substitutions used in the new run.

The new files replace the corresponding unavailable seventh-hour working files mathematically, not byte for byte. No failed or unexecuted command is represented as a successful computation.
