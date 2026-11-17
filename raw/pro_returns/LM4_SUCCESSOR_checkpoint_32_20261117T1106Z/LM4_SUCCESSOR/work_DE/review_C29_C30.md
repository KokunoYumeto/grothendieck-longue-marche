# Independent adversarial review of C.29–C.30

Reviewer: the topology/census branch of the GPT-6 Astra collaboration. This is a review of the argument, not an assertion of literature priority. Reviewed after checkpoint03 on 16 November2026.

## Conclusion and exact scope

**The proofs of C.29 and C.30 pass this independent review.** I found no missing finite-index topology comparison, no use of an unproved freeness theorem for a closed profinite subgroup, and no hidden assumption that the endomorphism is already invertible. Together they prove that a full unit pair satisfying the full duality and three-cycle equations induces a full profinite automorphism. This applies in particular to a pair also satisfying the full pentagon, and answers the constrained variant explicitly stated in Lochak–Schneps Question1.1.

This does not turn a bare pentagon into a full hexagon, produce a unit multiplier, compare all maximal pro-p equations with one full equation, or solve the main involution-conjugacy question. The unrestricted two-generator substitution can fail to be onto; the independent finite control below confirms that the extra boundary equation is substantive.

## C.29: checks aimed at possible failure points

1. **Image topology.** A continuous image of the compact profinite group F is compact and therefore closed. If H is proper, choose an element outside it and a finite quotient separating that element from H. The inverse image of the image of H in that finite quotient is a proper open subgroup U containing H. This supplies the required proper finite cover; no claim that H itself is open is made.

2. **Discrete comparison.** For the finitely generated discrete surface group G dense in F, U0=U∩G has index [F:U]. Its full profinite completion is U. Finite-index topology here is elementary: the core in G of a finite-index subgroup of U0 has finite index in G. Thus every finite quotient needed for U0 is seen by the induced topology. No pro-p replacement occurs.

3. **Conjugators.** The coset Ug_j is open and meets the dense G. Choosing a_j=v_jg_j with v_j∈U makes φ(c_j) U-conjugate to a_j c_{σ(j)}^{μ_j}a_j^{-1}. Because μ_j is a unit of the full Zhat, its inverse is a valid profinite exponent; closedness of U then puts the actual discrete element a_j c_{σ(j)}a_j^{-1} in U0. It is not enough to know a nonunit peripheral power lies in U, and the proof does not make that mistake.

4. **Covering width.** The double coset corresponding to a_j therefore has width one over the σ(j)th base boundary. Its positively oriented lift is represented by a_j c_{σ(j)}a_j^{-1}. Different base boundary labels give different boundary components upstairs. This remains correct for nonnormal U.

5. **Homology is taken in U.** Every image of a handle generator lies in H⊂U. The image of each handle commutator consequently vanishes in U's abelianization. The surface relation gives the asserted sum of the μ_j times the selected boundary classes in H1(U,Zhat), with conjugation disappearing there. The computation is not mistakenly performed only in H1(F,Zhat).

6. **Completed boundary relation.** A compact connected oriented cover with r boundary components has a free integral homology basis consisting of its handle classes and r−1 boundary classes, with the last boundary equal to minus their sum. Thus the boundary-class map Zhat^r→H1(U,Zhat) has kernel exactly the diagonal Zhat, by an explicit finite-rank split-module computation. There is no unsupported exactness assertion for completion of an arbitrary infinite module. A coefficient vector nonzero only on the selected boundaries can be diagonal only if there are no unselected boundaries. The unit assumption excludes the zero constant.

7. **Single boundary is covered.** If the original surface has m=1, the selected width-one boundary has zero homology only when it is the sole boundary upstairs. Its width then equals the entire covering degree, so that degree is one. Thus the proof does not silently use independence of at least two original boundary classes.

8. **Degree and injectivity.** Once all upstairs boundaries have been selected, there is exactly one width-one boundary over each original boundary. The sum of widths over each original boundary equals the degree, forcing degree one and contradicting U proper. Surjectivity follows. Hopficity of a finitely generated profinite group then gives injectivity; equivalently, preimage under a surjection permutes each finite set of open subgroups of bounded index, forcing its kernel into every open normal subgroup.

9. **Common exponent.** For m≥2, the same diagonal kernel calculation in the original surface abelianization forces all μ_j equal after the specified boundary permutation. Negative common units cause no sign defect: the oriented covering boundary classes are fixed, and their coefficients already record the sign.

The negative Euler characteristic assumption is more than the width argument itself needs, but is harmless and matches the intended hyperbolic setting. No claim about disconnected or nonorientable surfaces was imported.

## C.30: independent algebraic derivation

Use exactly xyz=1, z=(xy)^−1, A=f(x,y), B=f(y,z), C=f(z,x), and λ=2m+1. Since λ is a full unit, its dyadic component is odd and m=(λ−1)/2 exists uniquely in Zhat.

The hexagon first gives

\[
Cz^mB=x^{-m}A^{-1}y^{-m}. \tag{1}
\]

Under the continuous substitution (x,y)↦(x,z), the third argument is

\[
w=(xz)^{-1}=xyx^{-1}=z^{-1}yz.
\]

The duality identity, under the relevant substitutions, and simultaneous-conjugation naturality of profinite word evaluation give

\[
f(x,z)=C^{-1},\qquad
f(w,x)=xA^{-1}x^{-1},\qquad
f(z,w)=z^{-1}B^{-1}z.
\]

Substituting these expressions into the hexagon and using x^−1z^−1=y gives exactly

\[
C^{-1}x^{m+1}A^{-1}y^{m+1}B^{-1}z^{m+1}=1.
\]

Equivalently,

\[
Cz^{-m-1}B=x^{m+1}A^{-1}y^{m+1}. \tag{2}
\]

The correct division order is (2) times (1)^−1. The two sides become

\[
Cz^{-2m-1}C^{-1}
 =x^{m+1}A^{-1}y^{2m+1}Ax^m.
\]

Conjugating by x^m yields

\[
x^\lambda A^{-1}y^\lambda A
 =(x^mC)(xy)^\lambda(x^mC)^{-1}.
\]

This is the required full third-boundary relation. All operations are substitutions out of a free profinite group, conjugations, and power identities within one procyclic subgroup. None uses invertibility of the endomorphism under investigation. The argument is valid at the prime two and for mixed-prime units as written; no coordinatewise-to-full inference occurs. C.29 now applies directly.

The additional closed-submonoid argument in C.30 is also sound provided the cited parenthesized-braid composition theorem has the stated hypotheses, which are assigned to the CE/A source audit. In a profinite group any closed submonoid contains the inverse of each of its elements, because a^(n!−1) tends to a^−1 on every finite quotient. I did not independently re-audit the whole parenthesized-braid presentation, and it is not needed for the bare endomorphism-to-automorphism conclusion.

## Primary-source check

The primary Lochak–Schneps PDF was opened independently at:

https://webusers.imj-prg.fr/~pierre.lochak/textes/farb.pdf

I read its definitions on printed page3 and Question1.1 on printed page5 (PDF pages3 and5, numbering from one). The definition explicitly adds invertibility to the formulas x↦x^λ, y↦f^−1y^λf, then lists (I), (II), (III). Question1.1 asks the unconstrained question and adds: “One can ask the same question when (λ, f) satisfies (I), (II), (III).” Thus the scope comparison in C.30 accurately describes the source. This reading establishes what the source asks, not the absence of every later answer.

Primary searches also returned later author-written GT and GT-shadow surveys that retain an invertibility condition. That is a reason to check the proof carefully, not evidence that a redundant condition cannot be removed or that no earlier result exists. No priority claim is warranted by the search.

## Independent unrestricted control

The exact program `check_C30_unconstrained_control.py` uses S3 with x=(01), y=(12), λ=1 and f=[x,y]^−1. The original pair generates all six elements. The image of f is (012), and f^−1yf=x, so the substituted pair generates only the two-element subgroup. Its product is the identity while xy has order three, explicitly failing the third-boundary equation. The actual stdout is `check_C30_unconstrained_control.out` and all checks pass.

This smaller independent control is consistent with CE's separate A5 counterexample; it is not a counterexample to C.29 or C.30 and does not require a new formal statement number.

## Local audit artifacts

- `LochakSchneps2006_openproblems.pdf`: 182953 bytes; SHA256 `9dcfff4212d02e356eac02f042f5d1855c172ddb32745f69a50b71b082d77d89`.
- `check_C30_unconstrained_control.py`: 1358 bytes; SHA256 `140162a5911c3a978dd0492d01b035a914517a3a390b30483eb104a53d1ab3c4`.
- `check_C30_unconstrained_control.out`: 369 bytes; SHA256 `1c0e46222b1135d7ae36bbdb4885f38da4f45ac3f0eb9e9f8aa104b2eb425e72`.
