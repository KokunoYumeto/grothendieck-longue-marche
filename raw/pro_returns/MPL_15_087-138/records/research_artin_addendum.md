# Artin comparison addendum

Prepared after the freeze from the frozen transcription and supplied context. No scan image was opened and no frozen file was changed.

## T28 — The explicit Artin correspondence construction behind the arithmetic quotient

**File/scan/lines:** cote 15, scan 135, lines 32–43; scan 137, lines 2–4 and 6–30. **Kind:** unpursued implication / own construction. **Quote:** “ss-catégorie ... pleinement fidèle”; “\(Q\)-vectoriels étales”. **Confidence:** high for the construction below, proved by orbit matrices and an explicit averaging projector. **Context relation:** adds the actual correspondence-to-representation functor to **WG2 §2.4 #3**, the README's extension-by-\(\Gamma_{\mathbb Q}\) question, and T19–T21; searches for Artin, étale vectoriels, Galois, and catégorie find no corresponding Artin construction in context/MPL_16+47+54+44_transcription.tex, whose nearest motive-category witness is cote 16/049; cote 16/054 lists finite étale equivalence under a nilpotent quotient, and 16/021 gives the Tate sheaf, while the present note adds the orbit-matrix realization and its idempotent completion.

For finite étale \(X,Y/k\), put \(S_X=X(k^{\mathrm{sep}})\) and \(\Gamma_k=\operatorname{Gal}(k^{\mathrm{sep}}/k)\): the map \(CH_0(X\times_kY)_{\mathbb Q}\to\operatorname{Hom}_{\Gamma_k}(\mathbb Q^{S_X},\mathbb Q^{S_Y})\) sends a closed-point orbit \(O\) to the matrix with entry \(1\) at \((y,x)\) exactly when \((x,y)\in O\), and orbit matrices are bases on both sides. Composition is matrix multiplication, products give tensor products, and idempotent completion includes every finite-image continuous rational representation because the averaging projector splits its presentation by a finite sum of regular representations. The tensor automorphisms of the forgetful functor are the proconstant \(\mathbb Q\)-group \(\underline{\Gamma_k}_{\mathbb Q}\), as the coefficient calculation below shows. To import this identification into the manuscript's \(G'\), the remaining object to exhibit is a tensor functor \(\operatorname{Art}(k)\to M'\) whose composite with the stated embedding into étale rational vector spaces is this full Artin realization; the kept pages supply that embedding but do not document all these objects in the unspecified \(M\).

## Supporting construction

### 1. Rational zero-dimensional correspondences and their matrices

Fix the separable closure \(k^{\mathrm{sep}}\), the profinite group \(\Gamma_k\), and finite étale \(k\)-schemes \(X,Y\). The symbols \(\mathbb Q^{S_X}\) and \(\mathbb Q[S_X]\) are identified by the delta-function basis \(e_x\), with \(\gamma e_x=e_{\gamma x}\). This is a rational permutation representation, independently of the characteristic or coefficient field of \(k\).

The closed points of \(X\times_kY\) correspond to the \(\Gamma_k\)-orbits in \(S_X\times S_Y\). This zero-dimensional scheme has no positive-dimensional subvariety supporting a rational-equivalence relation between zero-cycles, so
\[
CH_0(X\times_kY)_{\mathbb Q}
=
\bigoplus_{O\in\Gamma_k\backslash(S_X\times S_Y)}\mathbb Q[O].
\]
The base change of a closed point is the sum of its distinct geometric points, each with multiplicity one, because the scheme is étale.

Use the convention that a correspondence \(X\to Y\) has matrix rows indexed by \(y\in S_Y\) and columns by \(x\in S_X\). Define
\[
R_{XY}\left(\sum_O a_O[O]\right)(e_x)
=
\sum_{y\in S_Y}a_{O(x,y)}e_y.
\]
A rational matrix \(B=(b_{y,x})\) intertwines the permutation actions precisely when
\[
b_{\gamma y,\gamma x}=b_{y,x}
\quad(\gamma\in\Gamma_k),
\]
so the characteristic matrices of the orbits give a basis of the target. Therefore \(R_{XY}\) is an isomorphism, with inverse obtained by reading the common entry on each orbit.

For correspondences \(B:X\to Y\) and \(C:Y\to Z\), the pullback–intersection–pushforward definition of composition gives, at the geometric pair \((x,z)\),
\[
(C\circ B)_{z,x}=\sum_{y\in S_Y}C_{z,y}B_{y,x}.
\]
Over a separable closure this is the direct count of the intermediate points; descent gives the same formula over \(k\), with residue-field pushforward degrees counting those geometric points. The diagonal of \(X\) gives the identity matrix. The basis map
\[
e_{(x,y)}\longmapsto e_x\otimes e_y
\]
identifies the correspondence tensor product for \(X\times_kY\) with the representation tensor product; the unit is \(\operatorname{Spec}k\), and transpose matrices implement duals through the delta-basis pairing. Graphs and transposed graphs give the corresponding pushforward and pullback conventions explicitly.

Define \(\operatorname{Art}(k)\) to be the additive idempotent completion of this rational correspondence category. Its extended realization \(R\) remains fully faithful: on objects \((X,p)\), \((Y,q)\), both sides restrict \(R_{XY}\) to the subspace \(q\,\operatorname{Hom}(X,Y)\,p\).

### 2. Every finite-image rational representation is obtained

Let \(V\) be a finite-dimensional continuous rational representation of \(\Gamma_k\) with finite image; it factors through \(H=\Gamma_k/N\) for an open normal subgroup \(N\). The corresponding finite Galois extension \(l=(k^{\mathrm{sep}})^N\) gives \(X=\operatorname{Spec}l\), whose geometric points form the regular \(H\)-set, so \(R(hX)\simeq\mathbb Q[H]\).

Choose a rational basis \(v_1,\ldots,v_d\) of \(V\). The map
\[
\theta:\mathbb Q[H]^{\oplus d}\longrightarrow V,\qquad
\theta\bigl((a_{h,j})_{h,j}\bigr)=
\sum_{h\in H,\;1\le j\le d}a_{h,j}\,h v_j
\]
is an \(H\)-equivariant surjection. Choose a rational-linear section \(s\) and form the explicit average
\[
s_H(v)=\frac1{|H|}\sum_{h\in H}h\,s(h^{-1}v).
\]
Then \(s_H\) is \(H\)-equivariant and \(\theta s_H=1_V\), so \(p=s_H\theta\) satisfies \(p^2=p\) and has image isomorphic to \(V\). The orbit-matrix isomorphism represents \(p\) by a rational correspondence on the disjoint union of \(d\) copies of \(X\). The object defined by that idempotent realizes \(V\), proving essential surjectivity without assuming that every representation is itself a permutation representation.

The displayed construction proves the tensor equivalence
\[
R:\operatorname{Art}(k)\xrightarrow{\sim}
\operatorname{Rep}^{\mathrm{fin}}_{\mathbb Q}(\Gamma_k),
\]
where the superscript means finite-image continuous representations. Continuity uses the discrete topology on the finite-dimensional rational vector space, equivalently on its representation matrices.

### 3. Tensor automorphisms over a general rational coefficient algebra

Let \(A\) be a commutative \(\mathbb Q\)-algebra and first restrict to \(\operatorname{Rep}_{\mathbb Q}(H)\) for a finite quotient \(H\). Naturality with respect to the maps
\[
\mathbb Q[H]\longrightarrow V,\qquad h\longmapsto hv
\]
shows that every natural endomorphism of the underlying-vector-space functor after extension to \(A\) acts on all representations by a single element \(a\in A[H]\). Write
\[
a=\sum_{h\in H}e_hh.
\]
Tensor compatibility and the unit condition say
\[
\Delta(a)=a\otimes a,\qquad \epsilon(a)=1.
\]
Comparing the coefficients of \(h\otimes g\) gives exactly
\[
e_h^2=e_h,\qquad e_he_g=0\ (h\ne g),\qquad
\sum_{h\in H}e_h=1.
\]
These equations also give the inverse \(\sum_he_hh^{-1}\). Such an orthogonal idempotent partition describes a locally constant map \(\operatorname{Spec}A\to H\), which is precisely an \(A\)-point of the constant finite group scheme \(\underline H_{\mathbb Q}\).

All objects of \(\operatorname{Rep}^{\mathrm{fin}}_{\mathbb Q}(\Gamma_k)\) factor through finite quotients, and the constructions agree under refinement of those quotients. Thus
\[
\operatorname{Aut}^{\otimes}(\omega)
=
\varprojlim_{N\triangleleft_{\mathrm{open}}\Gamma_k}
\underline{\Gamma_k/N}_{\mathbb Q}
=
\underline{\Gamma_k}_{\mathbb Q}.
\]
In particular its \(\mathbb Q\)-points recover \(\Gamma_k\); the general \(A\)-point description keeps track of the locally constant choices on components.

### 4. The exact remaining comparison with the manuscript

The kept text asserts a fully faithful tensor realization
\[
E:M'\longrightarrow
\operatorname{Rep}^{\mathrm{fin}}_{\mathbb Q}(\Gamma_k)
\]
after choosing \(k^{\mathrm{sep}}\). The construction above supplies \(R:\operatorname{Art}(k)\simeq\operatorname{Rep}^{\mathrm{fin}}_{\mathbb Q}(\Gamma_k)\). The missing manuscript-specific comparison is the triangle
\[
\operatorname{Art}(k)\xrightarrow{J}M'
\xrightarrow{E}\operatorname{Rep}^{\mathrm{fin}}_{\mathbb Q}(\Gamma_k),
\qquad E\circ J\simeq R.
\]
Concretely, one must exhibit in \(M'\) the objects \(h(\operatorname{Spec}l)\) for finite Galois \(l/k\), the orbit correspondences between them, and their rational idempotent summands. Their images contain every regular representation and the averaging projectors above, which is the actual object-level argument needed to fill the triangle.

Without adding this undocumented triangle to the frozen source, the group map evidenced by its stated \(E\) is the quotient
\[
\underline{\Gamma_k}_{\mathbb Q}\longrightarrow G',
\qquad
\ker=
\bigcap_{V\in M'}\ker(\rho_V)
\]
interpreted through its finite quotients. This is the explicit relation between the Artin construction and the source's \(G'\).

### 5. Base field and coefficient field

Here \(k\) is the field over which the finite étale schemes are defined; \(\mathbb Q\) is the coefficient field of correspondences and representations. The orbit matrices have rational entries and the averaging scalar \(1/|H|\) lies in that coefficient field; neither construction requires an embedding \(\mathbb Q\hookrightarrow k\) or \(k\hookrightarrow\mathbb C\). The symbol \(\Gamma_k\) is realized as a proconstant affine group scheme over \(\mathbb Q\) through the displayed inverse limit, with no assertion that an abstract Galois group is itself a vector subspace or a scalar field.

## Primary comparison and source-status note

Deligne–Milne, *Tannakian Categories*, Proposition 6.17 and Remark 6.19, give the Artin-motive/representation and étale-sheaf comparisons in their characteristic-zero motivic setup. Checked the corrected 15 August 2012 text, printed p.61: https://www.jmilne.org/math/xnotes/tc.pdf . Retrieval references for root's reopening: turn53view0 and turn53view1. The supporting argument here spells out the orbit basis, idempotent completion, averaging projector, and coefficient-algebra calculation independently; it does not attribute them to an unwritten passage on cote 15.
