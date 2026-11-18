# Actual mathematical checks behind the finite-cover research draft

Date: 2026-11-18. Checker: GPT-6 Astra Pro, agent `/root/research_finite`; effort setting not exposed. These are mathematical checks performed after the transcription freeze. They are not image-reading records and do not certify the complete manuscript. Statement IDs refer to `research_finite_notes.md`.

## RF01 — What the last line of scan 142 does and does not prove

Let $q_u:P\to P\times_uG'$ and $q_v:P\to P\times_vG'$ be the canonical maps, and $w$ the pointed $G'$-torsor isomorphism between the targets. The required equality is $wq_u=q_v$. Pulling back to $P=S_1$ turns this into the assertion that the canonical sections agree. Faithful-flat base change detects equality of maps, but it does not prove the equality.

The context's preceding rigidity lemma says that two **equivariant isomorphisms between torsors for the same group** agreeing at the marked point coincide. The two maps (wq_u) and $q_v$ have different structural homomorphisms $u$ and $v$; the first is $u$-equivariant and the second $v$-equivariant. They are also not necessarily isomorphisms of schemes. Consequently that stated lemma does not directly supply their equality. The intended extra assertion might follow from minimality by a further argument, but that argument was not established in this check.

A useful boundary test is the trivial $\alpha_p$-torsor over an algebraically closed field: the zero and identity homomorphisms give two different pointed maps into the same trivial torsor. This is **not** a counterexample to Proposition 4, because that torsor is not minimal; it merely demonstrates why the general pointed-map uniqueness cannot be inserted without an additional hypothesis or argument. Outcome: a precise proof obligation, not a refutation of Proposition 4 and not a successful proof check of its geometric step.

## RF02 — Formal pro-representation, conditional on the geometric proposition

Assume the stated closure under products and images, the descending chain condition for allowed subgroups, and Proposition 4. Work in a fixed universe in which the relevant classes have a set of representatives. A pair is ((G,z)), $z\in Z(G)$; a morphism $(G,z)\to(H,w)$ is a homomorphism $a:G\to H$ with $Z(a)z=w$.

1. Descending chains of allowed subgroups terminate, so each pair is dominated by a minimal pair carried by an allowed subgroup.
2. The product formula for $Z$ gives a pair dominating any two prescribed pairs. Reduce it minimally to obtain a common minimal dominator.
3. Proposition 4 says that from a fixed minimal pair there is at most one morphism to a fixed pair. Thus the category of minimal pairs is thin and cofiltered.
4. Any map of minimal pairs has allowed image; its target torsor is induced from that image, so target minimality makes the image the entire target. Thus transition maps are epimorphisms in the intended group category.
5. The map \(\varinjlim_i\operatorname{Hom}(G_i,H)\to Z(H)\) is surjective by minimal reduction. For injectivity, pass to a common minimal dominator of two representatives and apply Proposition 4 to the resulting two homomorphisms into $H$.

Outcome: the formal deduction checks out under the stated assumptions. This is not an independent re-proof of the geometric inputs of the fundamental group scheme, and leaves RF01 open.

## RF03 — Nonreduced-base pointed rigidity fails

Let $k$ have characteristic (p>0), $A=k[\epsilon]/(\epsilon^2)$, and $P=\operatorname{Spec}A[z]/(z^p)$, the trivial torsor for $G=\alpha_{p,A}$. Because $p\geq2$, \(\epsilon^p=0\); hence \((z+\epsilon)^p=z^p+\epsilon^p=0\), and $z\mapsto z+\epsilon$ is an automorphism, inverse $z\mapsto z-\epsilon$. It commutes with the translation coaction of \(\alpha_p\), is distinct from the identity, and reduces to the identity on the geometric fibre where \(\epsilon=0\). In particular it fixes its marked point.

Outcome: the unconditional reducedness-free version of the contextual rigidity statement is refuted. This does not determine which hypotheses the ambiguous phrase on scan 143 intended to remove; neither LM1 E.11 nor LM1 E.2 concerns this example.

## RF05 — Cocycle composition check

The upper path in the frozen rectangle is \(E\xrightarrow{A_{\alpha'}}E\xrightarrow{a''_\beta}E\xrightarrow{A_{\alpha''}}E\), giving $A_{\alpha''}a''_\beta A_{\alpha'}$. The lower path is \(E\xrightarrow{a'_\beta}E\xrightarrow{A_{\alpha'''}}E\xrightarrow{a'''_\beta}E\), giving $a'''_\beta A_{\alpha'''}a'_\beta$. Thus the boxed order is consistent. If a degenerate path condition yields $g=g^2$, invertibility yields $g=1$. No commutativity, existence of descended objects, or higher coherence was checked.

## RF07b — Group-theoretic kernel comparison

Write $A=\pi_1(\overline X_s)$, $E=\pi_1(X\times_SY)$, $H=\pi_1(X)$, $B=\pi_1(Y)$, $C=\pi_1(S)$. Assume compatible exact rows $A\to E\to B\to1$ and $A\to H\to C\to1$, with the evident maps $E\to H$, $B\to C$.

For $(h,b)\in H\times_CB$, choose $e_0\in E$ mapping to $b$. The quotient $h\,\rho(e_0)^{-1}$ lies in the image of $A\to H$; choose $a\in A$ with that image and multiply its image in $E$ by $e_0$. This proves surjectivity $E\to H\times_CB$. An element in the comparison kernel lies in the image of $A\to E$, and is zero exactly when the same representative lies in the kernel of $A\to E$; hence injectivity is equivalent to \(\ker(A\to H)\subseteq\ker(A\to E)\), the other inclusion being automatic.

A compatible map $X'=X\times_SS'\to X\times_SY$ induced by $S'\to Y$ gives a factorisation $A\to\pi_1(X')\to E$. If \(\pi_1(X')\to H\) is injective, a member of \(\ker(A\to H)\) maps to zero in \(\pi_1(X')\), and hence to zero in $E$. Basepoints and their paths must be chosen compatibly; inner conjugacy does not affect the kernel equality.

Modern source for the exact rows: [Stacks, Proposition 58.15.2, tag 0BUM](https://stacks.math.columbia.edu/tag/0BUM), for flat proper finite-presentation morphisms with geometrically connected reduced fibres. Its hypotheses and proof were read; the theorem is used as a standard input, not independently re-proved. Outcome: successful conditional group chase, with no unannounced translation of historical “séparable”.

## RF08 — Regular-object size check

For an arbitrary infinite discrete group $\pi$, the left regular $\pi$-set is infinite. Therefore it cannot be an object of the category of finite $\pi$-sets. Any formula evaluating a sheaf on that object requires the unrestricted category (or an explicitly different construction), so the repeated finite-set restriction in Hua's version cannot coexist with the frozen draft's chosen object. This checks the category-size issue only, not the cohomology comparison.

## RF09 / RF12 — Frame torsor and finite quotients

Let $X\to Y$ be finite étale of constant rank $n\geq1$. In \(X^n\), the coordinate-equality loci are clopen because the diagonal of a **separated** étale morphism is clopen. Their complement $P$ is finite étale, and over a splitting cover it is the set of bijections $I_n\to I_n$. The permutation action is simply transitive on these \(n!\) frames. The maps defining the action torsor identity are isomorphisms after this étale cover, hence globally.

For $H\subseteq S_n$ fixing the last index, the last-coordinate evaluation identifies the orbit set (S_n/H) with $I_n$. This identity is equivariant under changes of trivialisation, so it descends to $P/H\simeq X$. More generally any finite-group quotient of a finite étale $Y$-scheme is obtained étale locally by the finite orbit set and is finite étale. The existence and compatibility with base change can be expressed through the finite-colimit result in [Stacks, Lemma 58.5.2 and Remark 58.5.3, tag 0BL6](https://stacks.math.columbia.edu/tag/0BL6); the proof there was inspected. Descent of étaleness is [Stacks, Lemma 35.23.31, tag 02VN](https://stacks.math.columbia.edu/tag/02VN).

Outcome: the frame construction, quotient isomorphism, and the marked finite-étale quotient step are checked. The unidentified Proposition 2.5, the local completion argument of scan 155, and its general corollary were not independently certified. The stabiliser formula presupposes \(n\geq1\); the empty rank-zero cover can be treated separately.

## RF10 — Disconnected full frame torsor

Over \(\mathbb C\), take \(X=\mathbb G_m\), \(Y=\mathbb G_m\), and \(z\mapsto z^3\). Its automorphism group \(C_3\) acts regularly on a three-point fibre. The ordered-frame set is $S_3$, on which monodromy acts by multiplication through \(C_3\), giving exactly two orbits. Explicitly the six orderings of $(z,\zeta z,\zeta^2z)$ fall into the two cyclic ordering classes, each a copy of $X$. Thus the frame torsor has two connected components and a chosen component has stabiliser $C_3$. This is consistent with the connected Galois-cover convention checked in [Stacks, 03SF](https://stacks.math.columbia.edu/tag/03SF).

## RF11 — A precise counterexample and a precise repair

Glue two copies $U_1,U_2\simeq\mathbb A^1_k$ by the identity on $D(t)$; call the result $X$. The maps $U_i\to Y=\mathbb A^1_k$ glue to an étale morphism because they are isomorphisms on an open covering of $X$. The scheme $X$ is connected and quasi-compact. The involution $\sigma$ exchanges the charts and their origins and is the identity on $D(t)$. Therefore its geometric fixed-point locus is $D(t)$, which is open but not closed, and the locus where the two-element group acts freely consists of the two origins, which is not open. The action is faithful but has nontrivial inertia on $D(t)$.

This disproves the unrestricted étale/quasi-compact version of the scan-157 claim. The example is not separated or quasi-affine over $Y$. If $X\to Y$ is separated and étale, the equaliser \(\operatorname{Eq}(g,1_X)\) is the inverse image of the clopen diagonal under \((g,1_X):X\to X\times_YX\). Thus it is clopen, and if it meets a connected component it contains that component. For a finite group the union over nonidentity $g$ is clopen, giving the claimed free locus. This directly proves the repair without assuming that arbitrary unions of connected components of $X$ are open.

Outcome: refuted unrestricted claim; verified separated étale version. The finite case used earlier in the manuscript automatically satisfies separatedness.

## RF13 — Zero detection from the retained Gal 5

The initial object (0) is connected in the displayed definition: if $0\simeq U\amalg V$, then for every $T$, \(\operatorname{Hom}(U,T)\times\operatorname{Hom}(V,T)\) is a singleton, with both factors nonempty through the arrows via (0); hence each factor is a singleton and $U,V$ are initial. Preservation of the empty sum gives $F(0)=\varnothing$. If a nonzero connected $C$ had $F(C)=\varnothing$, the map $0\to C$ meets the conditions of the retained Gal 5, and the bijection of empty fibres would imply $0\simeq C$, a contradiction. The component decomposition and sum preservation then imply $F(X)=\varnothing\Rightarrow X\simeq0$.

Outcome: the manuscript's claimed redundancy is checked under its literal connectedness convention. A discarded attempt to manufacture a countermodel with a hidden component fails precisely because Gal 5 applies to the arrow $0\to C$; no countermodel or refutation is claimed.

## RF14 / RF15 — Scope tests for the designated morphism classes

For scan 159, in the usual category of schemes with geometric points the étale morphism \(\varnothing\to\operatorname{Spec}k\) violates axiom 6's surjectivity on point sets. This checks only that “non ramifié” cannot be identified unqualifiedly with all modern étale maps; it is not a consistency theorem for the full list.

For scan 160, a non-surjective open immersion of affine schemes is flat affine but is not a strict epimorphism in schemes. Thus the examples require the covering/surjectivity qualifications implicit in a descent class. This is a scope test, not a new impossibility theorem about the intended category.

## RF17 — Refutation of the global normalisation arrow

Let $Y=X'=\operatorname{Spec}k[t]$, $X=U=\operatorname{Spec}k[t,t^{-1}]$, and identify $U'=D(t)\subset X'$. The product $X\times_YX'$ is $D(t)$; the diagonal used by the manuscript is all of this product, so its integral closure-of-image $X''$ is again $D(t)$. The map $X''\to X$ is an isomorphism, hence finite and surjective, while $X''\to X'$ is birational. The normalisation \(\widetilde X'\) is \(\mathbb A^1\).

A map \(\widetilde X'\to X''\) over $X'$ would split the open immersion $D(t)\hookrightarrow\mathbb A^1$ with composite the identity of \(\mathbb A^1\), which is impossible at the origin. Algebraically it would be a $k[t]$-algebra map $k[t,t^{-1}]\to k[t]$ extending the identity, requiring an inverse to $t$ in $k[t]$. Every recovered hypothesis of scan 187 holds. Outcome: the existence of the claimed **global** reverse arrow is refuted, including the version after “surjectif” was deleted. The proposition's finite-type conclusion remains true.

## RF18 — Complete repair of the finite-type proposition

**Precise checked statement.** Let $Y$ be locally noetherian and universally Japanese. Let $f:X\to Y$ be separated and locally quasi-finite, with $X$ having finitely many irreducible components. Then $f$ is quasi-compact and therefore of finite type. Here locally quasi-finite includes locally finite type, and does not assume global quasi-compactness.

1. **Reduction.** Finite type is local on the target. Restrict to an affine $Y$; it is noetherian Nagata by [Stacks, 033R, Lemma 28.13.8](https://stacks.math.columbia.edu/tag/033R). The inverse image still has finitely many irreducible components, since each nonempty open subset of an irreducible component is irreducible. The source is locally noetherian. To prove quasi-compactness, it suffices to prove it for each reduced irreducible component $Z\subseteq X$, since there are finitely many and their underlying spaces cover $X$. Each $Z\to Y$ remains separated and locally quasi-finite.

2. **Dominant integral setup.** Replace $Y$ by the reduced closure $Y_0$ of the image of $Z$. This is an integral closed subscheme of the affine noetherian Nagata $Y$, hence is affine and Nagata. The morphism from reduced integral $Z$ factors through $Y_0$, is dominant, and stays locally quasi-finite. At the generic point the field extension $L=k(Z)/K=k(Y_0)$ is finite.

3. **Two finite normalisations.** Let $T\to Y_0$ be the normalisation of $Y_0$ in $L$. It is finite because $Y_0$ is Japanese, hence is an affine noetherian normal integral scheme with field $L$. As \(Z\) is locally of finite type over a Nagata scheme, it is Nagata ([Stacks, 035A](https://stacks.math.columbia.edu/tag/035A)); its normalisation \(Z^\nu\to Z\) is finite and surjective ([Stacks, 035S](https://stacks.math.columbia.edu/tag/035S)). This invocation does not assume that \(Z\) is already quasi-compact.

4. **The correct direction of the map.** Every element of the coordinate ring of \(T\) is integral over that of \(Y_0\). Its image in \(L\) therefore belongs to every normal local ring of \(Z^\nu\), giving a canonical map \(j:Z^\nu\to T\). This map is separated, locally quasi-finite, and birational. The separatedness follows from that over \(Y_0\); local quasi-finiteness follows from the finite map \(Z^\nu\to Z\), the locally quasi-finite map \(Z\to Y_0\), and the factorisation through the finite \(Y_0\)-scheme \(T\).

5. **Open immersion without circular quasi-compactness.** On an affine open \(V\subseteq Z^\nu\), the map \(V\to T\) is quasi-finite in the modern global sense, since \(V\) is quasi-compact and \(T\) is affine noetherian, and is separated and birational. Since \(T\) is normal integral with field \(L\), its normalisation in \(V\) is \(T\) itself: functions in \(L\) integral over its normal coordinate ring already belong to that ring. Thus [Stacks, Zariski's Main Theorem, 02LR](https://stacks.math.columbia.edu/tag/02LR) makes \(V\to T\) an open immersion. If two such image opens overlap, their inverse sections into the separated \(T\)-scheme \(Z^\nu\) agree at the generic point and therefore everywhere on the reduced integral overlap. The local open immersions hence patch to a global open immersion \(j\); no global quasi-compactness was assumed to apply Zariski's main theorem.

6. **Finish.** Every open subset of a noetherian scheme is quasi-compact. Thus \(Z^\nu\), as an open of \(T\), is quasi-compact. Its finite surjection onto \(Z\) makes \(Z\) quasi-compact. The finite union of components makes \(X\) quasi-compact over the chosen affine \(Y\); combined with locally finite type, this proves finite type.

**Outcome.** Successful targeted proof of the proposition under the recovered hypotheses. The argument replaces the false map \(\widetilde X'\to X''\) with a correct open immersion of the normalised source into a finite normal model. It is not an attribution of this repair to the manuscript or to Hua, and is not a solution of LM1 E.11.

## Primary-source retrieval ledger

All the following were opened on the official Stacks Project site on 18 November 2026. Their hypotheses/statements were inspected; use as a standard input is distinguished above from independent proof.

| Tag and current displayed label | Used for | Retrieval reference |
|---|---|---|
| [033R, §28.13, especially Lemma 28.13.8](https://stacks.math.columbia.edu/tag/033R) | Japanese/Nagata definitions and equivalence | `turn996960521view1` |
| [035A, Lemma 29.18.1](https://stacks.math.columbia.edu/tag/035A) | Nagata stable under locally finite type | `turn534858198view1` |
| [035S, Lemma 29.55.11](https://stacks.math.columbia.edu/tag/035S) | Finite normalisation of a Nagata scheme | `turn380339812view1` |
| [02LR, Lemma 37.43.2](https://stacks.math.columbia.edu/tag/02LR) | Zariski-main-theorem open immersion | `turn380339812view0` |
| [0BUM, Proposition 58.15.2](https://stacks.math.columbia.edu/tag/0BUM) | Homotopy exact sequence, with stated hypotheses | `turn534858198view0` |
| [0BL6, §58.5](https://stacks.math.columbia.edu/tag/0BL6) | Finite étale colimits, local splitting, descent | `turn996960521view0` |
| [02VN, Lemma 35.23.31](https://stacks.math.columbia.edu/tag/02VN) | Étaleness fpqc local on the base | `turn534858198view2` |
| [03SF, §58.7](https://stacks.math.columbia.edu/tag/03SF) | Connected Galois-cover terminology | `turn380339812view2` |

The retrieval references are internal provenance, not citations to be copied blindly into the parent's chat response; the parent should open any source it cites there. No online text was used to revise the transcription.
