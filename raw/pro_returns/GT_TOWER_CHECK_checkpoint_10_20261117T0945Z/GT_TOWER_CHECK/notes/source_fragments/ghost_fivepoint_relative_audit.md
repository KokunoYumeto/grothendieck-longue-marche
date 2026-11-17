# Five-point relative-cover computation and exact limits

## Actual source and quotient

Use the proved presentation of \(\Gamma_{0,5}=P_4/Z(P_4)\) with generators
\(a=A_{13}, b=A_{23}, x=A_{14}, y=A_{24}, z=A_{34}\). It is the displayed split extension \(F(x,y,z)\rtimes F(a,b)\). The six literal conjugation relators are stored in `fivepoint_relative_tools.py`, together with mutually inverse free-word actions for \(a,b\).

For
\[
J=\ker(\Gamma_{0,5}\longrightarrow (\mathbf Z/4)^5),
\]
the actual split extension restricts to \(F_{129}\rtimes F_{17}\). The fibre and base bases are the explicit Schreier bases of the abelian covers of degrees64 and16. Every one of the17 actual base generators acts on every one of the129 fibre generators by a retained free word. There are2193 relators and1900491 rewritten letters in total; the largest rewritten relator image has8364 letters.

The finite five-point target computed is exactly
\[
Q=\Gamma_{0,5}/\bigl(\gamma_3(J)J^3\bigr).
\]
At class two over \(\mathbf F_3\), BCH collection is literal, with \(1/2=2\). The raw146 first coordinates have66 independent linear relators. The surviving first homology has dimension80. After retaining the central corrections when eliminating those66 coordinates, the central relation space has rank1731 in \(\bigwedge^2\mathbf F_3^{80}\), of dimension3160. Thus the central quotient has dimension1429 and
\[
|Q|=4^5\,3^{1509}.
\]
All row bases, pivot positions, original-row coefficients, rewritten source words, and the actual central corrections are retained in `build_fivepoint_relative_class2.npz`; its `.py`, `.json`, and actual `.out` are saved.

## Independent first-homology comparison

The separate Fox calculation uses all1024 characters of \((\mathbf Z/4)^5\) over \(\mathbf F_9=\mathbf F_3[i]\), \(i^2=-1\). The six actual presentation relators have twisted Fox matrices whose kernels give a trivial character of homology dimension5 and75 nontrivial characters of dimension1. The nontrivial support is precisely the union of the five actual four-point character planes, each of order16, with pairwise intersection only the zero character. It consists of15 sign characters and30 conjugate \(\mathbf F_9\)-pairs.

Each four-point forgetting map admits an actual free-group section; that section maps the abelian-mod-four kernel into the corresponding kernel upstairs. Hence its pullback on the cover's first cohomology is injective. On every nontrivial character in its plane that injection fills the computed one-dimensional space. At the trivial character the five pullbacks span the named five abelian coordinates. Therefore the first homology comparison with all five four-point covers is injective: this first abelian layer itself retains no additional Brunnian class. This conclusion uses the forgetting/section maps as well as the character count.

The separate exact program is `check_fivepoint_relative_h1.{py,out,json}`. Its dimension80 agrees with the independently rewritten relative presentation.

## Finite word-record census

The common finite free source is
\[
P=F_2/\bigl(\gamma_3(J_2)J_2^3\bigr),\qquad
J_2=\ker(F_2\longrightarrow(\mathbf Z/4)^2).
\]
Its order is \(16\,3^{153}\): the free kernel has rank17, with136 central commutators. Its actual abelianization is \(C_{12}^2\), so its derived image is exactly the subgroup whose two residual abelian coordinates vanish. All five pentagon maps, the antisymmetry map, and both three-cycle maps carry \(J_2\) into \(J\); consequently they factor through these exact finite quotients. Their values on all17 source Schreier generators and all136 central basis commutators are saved in `test_fivepoint_relative_class2_maps.npz` and its companion JSON.

The first-degree commutator, antisymmetry, three-cycle, and pentagon equations have rank13 on the17 source coordinates. The remaining4 coordinates give81 cases. Their central equations have rank119 on136 variables, and exactly36 first-degree cases are consistent, each with a17-dimensional central fibre. The actual capped216 target and its multiplication table are reconstructed independently. Its mixed-defect values are constant on each central fibre; among the36 surviving cases they occur12 times each with scalar0,1,2. The complete finite census is saved in `census_fivepoint_relative_class2.{py,out,json,npz}` and its small summary files.

This finite enumeration does not assert that every surviving record comes from a profinite gentle element. There is, however, a separate genuine survivor for the identity record, proved by the exact source argument below.

## Genuine identity-record survivor

The auxiliary frame word
\[
A_0=[[x^4,y^4],((xy)^{-1})^4]^2
\]
lies in \(\gamma_3(J_2)\), so its value in \(P\) is one. In the retained signed modular source it has the central order-two value \(5I\). Join these actual source maps over \(B=\widehat{C_2*C_3}\). The pure abelianization of the join is exactly \(C_{12}^2\): the two generators have order dividing12 in every factor and the projection to \(P^{\mathrm{ab}}\) forces the full order. Thus the commutator-normalizing exponent is killed literally.

In the full canonical central cover, a lift of this frame commutes with the named cubic generator: its commutator is central and has order dividing both2 and3. The identity automorphism, trivial quadratic frame, this cubic frame, and trivial cusp frame therefore give the exact positive source certificate. The full finite-image lifting theorem B.2.7/B.2.9 supplies an actual normalized gentle element with \(\Delta=1\) and identity \(f\)-record in \(P\). Every one of the eight five-point evaluations is consequently identity. The frame word and the normalized gentle word are not identified with one another; their exact joint source coordinates are what prove this assertion.

The stronger result is now written by the centralizer agent in A.4.41. It gives genuine parity-one survivors for every finite family whose auxiliary-frame images have odd order, including all targets with odd derived subgroup. In particular it covers every relative pro-three refinement over the abelian \(C_4^5\) base, and compactness gives a single survivor for that entire directed family. Further runs within that family were stopped.

## The actual full quaternion pure image

The script `check_fivepoint_quaternion_pure.g` reuses the literal52-dimensional local braid matrices of A.4.27 and takes the six actual pure-four-braid generators. It verifies:

- pure image order3888, derived subgroup order486, and abelianization \(C_2^3\);
- nonabelian Sylow-two subgroup of order16 and exponent4;
- normal Sylow-three subgroup of order243;
- quotient by that odd normal subgroup of exponent4;
- central full twist of order3.

All decisive values are assertions, and the actual GAP output is saved. Although the derived subgroup here has even order, every fourth power lies in the odd normal subgroup. Thus every evaluation of \(A_0\) has odd-order image, and A.4.41's exact source argument still applies. The order-three central cap preserves this property. No detection result is inferred from the nonabelian Sylow-two subgroup alone.

## Reversed-prime proposal and its exact obstruction

Before any large binary computation was begun, the centralizer agent supplied an actual norm frame for
\[
F_2/\bigl(\gamma_3(J_3)(\gamma_2J_3)^2J_3^4\bigr),
\qquad J_3=F_2'F_2^3.
\]
The source kernel is the free class-two exponent-four group on10 generators. The three cubic-generator conjugates of \(A_0\) are commuting central involutions there. Their product is cubic-generator-fixed, has order2, and has signed value \(5I\). The canonical-cover argument and exact \(C_{12}^2\) normalization again supply a genuine identity record. An independent fresh replay of the full296-letter norm and all source maps is saved as `review_reversed_binary_norm.{py,out,json}`. No redundant deeper binary run was made.

The active next question concerns a ternary recognition layer above a genuinely coupled signed/binary five-point quotient. It must retain the actual restriction map from the five-point cover homology to the common free-source cover; neither the odd-derived calculation nor the norm-frame construction settles that different retained map.
