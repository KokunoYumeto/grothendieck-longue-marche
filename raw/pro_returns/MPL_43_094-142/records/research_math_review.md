# Independent mathematical review of selected root notes

Review scope: D18, D20, D29, R06, and R15 in records/research_root.md, with a few nearby citation checks. The review used frozen page fragments and supplied contextual transcriptions; no manuscript image was opened and no frozen file was changed. CT means the supplied MPL_16+47+54+44_transcription.tex, retaining its first-pass status.

## Findings

| Note | Mathematical result of review | Action |
|---|---|---|
| D18 | Pass: the Ext transition is multiplication by \(t\), the direct-limit map is correct, and the endomorphism ring is \(k[[t]]\). | Optional addition of the converse construction from a compatible scalar sequence. |
| D29 | Pass for the explicitly specified ordinary étale-sheaf calculation. | Define \(j:U\hookrightarrow X\), name the étale realization, and retain the outstanding comparison with the manuscript's underlined \(k\)-group-valued functors. |
| R06 | Pass: every displayed hypothesis on scan 110 is satisfied, the lengths are \(2\) and \(1\), and the module fails flatness. | Retain the conclusion about the literal inequality sentence, alongside the author's later equality wording. |
| R15 | Pass: evaluation on germs gives an \(\mathcal A_x\)-linear stalk retraction. | Keep the conclusion at stalkwise injectivity; no global sheaf retraction has been constructed. |
| D20 | Pass for the formal composite in the stated shift convention. | Replace “CT 54:3 supplies a duality pairing” by “CT 54:3 states/proposes degree-one duality”; replace “printed construction” by “written construction”. |

## D18: calculation and exact transition maps

Set \(A=k[[t]]\), \(K=k((t))\), \(M_n=A/(t^n)\), and \(E=K/A\). The two-term free resolution of \(M_n\) has differential multiplication by \(t^n\), so its dual complex has the same differential and degree-one cokernel \(A/(t^n)\).

The quotient \(q_n:M_{n+1}\to M_n\) is lifted by the chain map whose degree-zero component is \(\mathrm{id}_A\) and whose degree-one component is multiplication by \(t\): the chain-map identity is \(t^n t=t^{n+1}\). Applying \(\operatorname{Hom}_A(-,A)\) therefore gives
\[
q_n^*:\operatorname{Ext}^1_A(M_n,A)\longrightarrow
\operatorname{Ext}^1_A(M_{n+1},A),\qquad
[a]\longmapsto[ta].
\]
This is the direction and scalar written in D18.

The map
\[
\phi_n:A/(t^n)\longrightarrow E,\qquad
[a]\longmapsto a/t^n+A
\]
has kernel zero and image \(E[t^n]\); moreover,
\(\phi_{n+1}([ta])=\phi_n([a])\). Every Laurent series modulo \(A\) has a finite pole order, so the union of these images is \(E\); this proves the asserted direct-limit isomorphism.

Write \(e_n=t^{-n}+A\). An \(A\)-endomorphism \(f\) preserves \(E[t^n]\), and this cyclic module has the form \(Ae_n\simeq A/(t^n)\), so \(f(e_n)=a_ne_n\) for a unique \(a_n\bmod t^n\). Since \(e_n=te_{n+1}\), compatibility gives
\[
(a_{n+1}-a_n)e_n=0,\qquad
a_{n+1}\equiv a_n\pmod{t^n}.
\]
Conversely, a compatible scalar sequence defines an endomorphism on the union \(E=\bigcup_nE[t^n]\), by multiplication on each cyclic submodule. Composition corresponds to componentwise multiplication, so the result is an isomorphism of rings
\[
\operatorname{End}_A(E)\simeq\varprojlim_nA/(t^n)=A.
\]

The comparison with CT 16/39 is also concrete: the filtration \(E[t]\subset E[t^2]\subset\cdots\) consists of finite-length \(A\)-modules, and each successive quotient is \(k\), matching the one-dimensional graded pieces \((t^{n-1})/(t^n)\). For completeness, \(E\) is an injective hull of \(k\): multiplication by any nonzero \(d\in A\) is surjective on \(E\), so a homomorphism from the principal ideal \((d)\) extends to \(A\) by choosing a preimage of its value at \(d\); Baer's criterion applies because all ideals of this DVR are principal. Every nonzero submodule of \(E\) meets \(E[t]\): multiplying an element of pole order \(n\) by \(t^{n-1}\) gives a nonzero element of \(E[t]\). D18 itself needs only the elementary Ext and endomorphism calculations, so it does not depend on a general local-duality theorem.

## D29: correct degree-zero test, with its realization named

The calculation is correct on the ordinary small étale site of
\[
X=\mathbb P^1_k,\quad U=\mathbb A^1_k,\quad
Y=\{\infty\},\quad j:U\hookrightarrow X,\quad i:Y\hookrightarrow X,
\]
with \(k\) algebraically closed and \(\Lambda=\mathbb Z/n\mathbb Z\) as in the note. The following exact sequence gives a particularly explicit proof:
\[
0\longrightarrow j_!\Lambda_U\longrightarrow\Lambda_X
\longrightarrow i_*\Lambda_Y\longrightarrow0.
\]
Its maps are extension by zero followed by the adjunction inclusion, and restriction to \(Y\); it is the sequence in Stacks, Lemma 59.70.8, [Tag 03S2](https://stacks.math.columbia.edu/tag/03S2). On degree-zero global sections the right-hand map is the identity \(\Lambda\to\Lambda\), since \(X\) and \(Y\) are connected, so \(H^0(X,j_!\Lambda_U)=0\).

The geometric stalks of \(j_!\Lambda_U\) on \(Y\) vanish, by the formula in Stacks, Proposition 59.70.3, [Tag 03S5](https://stacks.math.columbia.edu/tag/03S5). A global section supported on \(Y\) consequently has zero stalk both on \(Y\) and on its complement, proving \(H_Y^0(X,j_!\Lambda_U)=0\). Meanwhile \(H^0(U,\Lambda_U)=\Lambda\).

Localization yields the exact segment
\[
0=H^0(X,j_!\Lambda_U)\longrightarrow
H^0(U,\Lambda_U)\xrightarrow{\delta}
H_Y^1(X,j_!\Lambda_U),
\]
so the connecting homomorphism \(\delta:\Lambda\to H_Y^1(X,j_!\Lambda_U)\) is injective. The distinguished triangle and this boundary are given in Stacks, §59.79, [Tag 09XP](https://stacks.math.columbia.edu/tag/09XP). Thus the computation and the observed degree shift in D29 are valid.

The manuscript on scan 140 uses underlined relative functors \(\underline H^*_{Y/k}\) and \(\underline H^*_{U/k}\), while scans 94–98 and 128 leave categorical and cohomological comparisons under discussion. The note should explicitly call the example an ordinary étale-cohomology realization and retain the task of identifying its evaluation/comparison with those underlined functors. This preserves the exact force of the example without silently assigning a convention to the frozen source. CT 16/37 supports the methodological comparison through stalks, but it supplies neither the extension-by-zero sequence above nor the localization boundary; the direct primary citations above are better for those two assertions.

Suggested four-sentence replacement body:

> Work on the ordinary étale site with \(X=\mathbb P^1_k\), \(U=\mathbb A^1_k\), \(Y=\{\infty\}\), inclusions \(j:U\hookrightarrow X\), \(i:Y\hookrightarrow X\), and \(\Lambda=\mathbb Z/n\mathbb Z\) for \(n>1\) invertible in the algebraically closed field \(k\).
> The sequence \(0\to j_!\Lambda_U\to\Lambda_X\to i_*\Lambda_Y\to0\) gives \(H^0(X,j_!\Lambda_U)=\ker(\Lambda\xrightarrow{\mathrm{id}}\Lambda)=0\), and the zero stalk on \(Y\) gives \(H_Y^0(X,j_!\Lambda_U)=0\), whereas \(H^0(U,\Lambda_U)=\Lambda\).
> The localization boundary therefore injects \(\Lambda\) into \(H_Y^1(X,j_!\Lambda_U)\).
> This exhibits the degree behavior to compare with the unshifted box on scan 140 and the \(+1\) on scan 136; the identification with the manuscript's underlined \(k\)-group-valued functors remains to be supplied.

## R06: the nonflat coherent module meets the displayed assumptions

The source on scan 110 supplies a proper map to a DVR spectrum, a coherent module with full support, components of \(X\) dominating the base, and the \((S_1)\) condition on its special fibre. In R06, \(R=k[[t]]\), \(X=Y=\operatorname{Spec}R\), and \(f=\mathrm{id}\) satisfy properness and universal openness. The only irreducible component maps onto \(Y\), and the finite module \(M=R\oplus k\) has full support because of its \(R\)-summand.

Its special and generic fibres are
\[
M\otimes_Rk=k^2,\qquad M\otimes_RK=K.
\]
There is one maximal point of each fibre support, so the relevant lengths are \(2\) and \(1\). The special-fibre module over the zero-dimensional ring \(k\) satisfies \((S_1)\), whose depth bound there is \(\min(1,0)=0\); it also has no embedded associated point. Both the \(\ge\) and the doubtful strict \(>\) alternatives in the frozen inequality hold for these lengths.

Tensoring the monomorphism \(R\xrightarrow{t}R\) with \(M\) gives multiplication by \(t\) on \(R\oplus k\), with kernel \(0\oplus k\). Thus flatness fails precisely at the closed point, which is the maximal point of the special-fibre support. This establishes the stated counterexample to the literal inequality-to-flatness sentence while leaving the manuscript's subsequent equality wording as the internal reading question. CT 54/4–6 is a valid comparison to actual flatness revisions, and no assertion about its statements being false follows from this example.

## R15: evaluation is a valid stalk retraction

The source defines its doubtfully named \(\mathcal I|\mathcal J\) as the sheaf of germs of arbitrary functions to \(\mathbb Z\). A germ at \(x\) is represented by a function on a neighbourhood of \(x\), and representatives agreeing on a smaller neighbourhood have the same value at \(x\); therefore
\[
\mathrm{ev}_x:\mathcal I_x\longrightarrow\mathbb Z,\qquad
[a]\longmapsto a(x)
\]
is well-defined, additive, and sends \(1\) to \(1\). The \(\mathbb Z\)-balanced map
\[
r_x:F_x\otimes_{\mathbb Z}\mathcal I_x\longrightarrow F_x,\qquad
m\otimes a\longmapsto a(x)m
\]
is \(\mathcal A_x\)-linear for the left action on the first factor, and
\(r_x(m\otimes1)=m\). Thus the source's homomorphism is injective on every stalk, proving its sheaf injectivity.

This proof neither uses nor changes the later abstract torsion-free-group lemma. The \(r_x\) are stalk maps; the review has not constructed a single sheaf morphism retracting \(F\to F\otimes\mathcal I\). CT 16/37 indeed tests the extension of a sheaf map through the corresponding map of stalks in its injective-hull proof, so the contextual citation is accurate at that methodological level. The main note can introduce \(\mathcal I\) as a temporary name for the source's \(\mathcal I|\mathcal J\) reading doubt.

## D20 and nearby source wording

For the convention \(u:G\to S\sigma[i]\), the precise formal composite is
\[
Rf_*G\xrightarrow{Rf_*u}Rf_*(S\sigma[i])
\xrightarrow{\cong}(Rf_*S\sigma)[i]
\xrightarrow{\gamma[i]}\sigma[i].
\]
The middle arrow is the shift compatibility of the derived functor. D20's formula suppresses this customary identification but has the right source, target, and shift. The note correctly identifies the construction of \(\gamma\) as an outstanding source obligation.

CT 47/7 constructs the particular arrow from the Poincaré direct image to the shifted zero-section object, and CT 47/8 explicitly ends its zero-section argument with a compatibility verification. That citation supports the comparison made in D20. CT 54/3, however, writes “Je dis que” for identification of the universal-extension tangent sequence with \(S_B\), then asserts that \(H^1(A)\) and \(H^1(B)\) are dual; it has not constructed the pairing in the supplied paragraph. The wording “states/proposes degree-one duality” accurately preserves this status.

Two further minor edits are recommended:

- D02's “an earlier explicit base-change assertion” suggests a chronology not supplied by the cited leaves; use “another explicit base-change assertion”.
- D17's CT 44/3 completion lead is a cancelled draft, with a surviving margin, and should be labelled as such when mentioned.

All computations reviewed above are either explicit examples or formal composites in named conventions. No general theorem beyond those concrete calculations is supplied here, and no register status or frozen transcription is changed.
