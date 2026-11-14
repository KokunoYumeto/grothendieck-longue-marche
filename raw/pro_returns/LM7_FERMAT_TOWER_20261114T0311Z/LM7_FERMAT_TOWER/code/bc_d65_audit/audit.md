# Independent D.65 proof and actual-map audit

**Result: PASS. No correction requested.** The frozen author tree was read only.

The audited proof is `D65_EXPERIMENTS/sections/D_divided_compact_source.tex`, SHA256 `f0cfcb7ab9cc56d3a91572f4e7804f794f765c23e4126e0b9c5963a8e18da8ae`. The audited manifest is `ledger/d_divided_compact_source_manifest.json`, SHA256 `a0912a250ef5a225f30471f02de19b569333813c81ed66adfa0af0be2b25cde1`.

## Scope

I read the complete 643-line proof and all eight mathematical Python sources: the rigid source map, full trace, permutation comparison, projective trace, integral lattice, real exterior lattice, divided correction, and source centralizer programs. I checked their use of the actual D.64 inputs, coefficient conventions, recorded finite framings, and the distinction between the changed lower action and the retained comparison maps.

I did not replay the eight construction programs. Root owns that independent full replay. Instead I wrote and executed `code/bc_d65_maps.py`, which imports data only and independently reconstructs the central modulo-four comparisons. It verifies 161 file hashes: all 145 owned files and both copies of the eight immutable inputs. Its complete stdout is retained; there was no failed execution of this verifier.

## Integral source extension

The source map in D.65.18 is a map of the actual integral marked lattices. The compact projection kills the entire cusp lattice, and the lift through D.64.11 has zero small image. For an ordinary coefficient map into that kernel, the factorization through

\[
P=\mathbf Z_2[G]\otimes_{\mathbf Z_2}\mathsf M_a,
\qquad j(v)=\sum_{g\in G}g\otimes g^{-1}v
\]

is equivariant when the action on (P) is on the first factor. The equivariant extension (q(g\otimes v)=gq(1\otimes v)) makes the composite the actual group trace. Restricting to the selected character fibre gives the stabilizer trace times (3^{97}); multiplication by that odd unit's inverse gives exactly the trace used in the certificate. The target remains the actual comparison kernel.

For the extension across the edge lattice, the quotient (E/U) is a free integral lattice: it is the kernel of the augmentation map on the vertex lattice. Let (f:U\to\mathsf M_a) be the coefficient-of-identity functional of (j_U). An ordinary extension \(\widetilde f:E\to\mathsf M_a\) exists because the lattice sequence splits over \(\mathbf Z_2\). The explicit coinduced extension is

\[
\ell(e)=\sum_{g\in G}g\otimes\widetilde f(g^{-1}e).
\]

It is equivariant and restricts to (j_U). This proves the required relative extension without an assertion that the nonprojective compact lattice is projective.

The original path convention (p(s)=0, p(r)=e_1-e_r) gives the displayed signs. Since (j_U) kills the full cusp class, (N_{36}(t)\ell p(t)=0). On each actual regular cyclic orbit in (P), the zero-sum lattice is ((t-1)P), so choose (b) with \(\ell p(t)=(t-1)b\). Then

\[
\eta_P(g)=\ell p(g)+(1-g)b,quad
\eta_P(s)=(1-s)b,quad
\eta_P(r)=(1-r)(\ell(e_1)+b),\quad \eta_P(t)=0.
\]

On the geometric kernel this is precisely (j_U) on integral homology. It therefore kills each defining kernel of (Y). Lifting the two coefficients through the actual (S_{57}\to\mathcal L) gives the two source conjugators. Their small and \(\mathcal W_h\) coordinates vanish. The formula \(\beta_Y(g)=\eta(g)\alpha_{64,Y}(g)\) consequently has the asserted additive homology change; no precomposition by the old compact action is silently introduced.

## Integral norm and orientation comparison

The signed exchange action is essential. The real exterior embedding in D.65.17 is primitive and sends conjugation to the negative Hermitian conjugation used in D.65.5. Both whole integral operators are even, so their halves modulo two are independent of the integral representative. Integral augmentation relations have norm zero; changing a lift of an augmentation relation by twice a vector contributes the undivided norm of that vector, also zero modulo two.

The marked surface boundary identity applies before reduction to actual full-source conjugators. Its cusp errors have zero integral abelianization; wedges with cusp classes disappear under the specified compact quotient. It therefore gives the actual identity in D.65.22, with the original positive cusp convention.

The comparison with the smaller graph retains the odd factors. Pushforward and transfer for the cover of degree (3^{93}) give the inverse maps on the selected component because that deck kernel acts trivially there. Their intersection adjunction gives (H_G=3^{-93}H_\dagger), hence \(\Omega_G=3^{93}\Omega_\dagger\). The group norm has the factor (3^{97}), leaving exactly (3^{-4}) in the stated orientation identity. Its reduction modulo two is one, but the proof retains the integral factor before division.

For a trace change \(2K\), direct multiplication modulo four gives

\[
\frac{(T+2K)\Omega\overline{(T+2K)}^{,t}
       -T\Omega\bar T^{,t}}2
\equiv K\Omega\bar T^{,t}+T\Omega\bar K^{,t}\pmod2.
\]

The product of the two changes is divisible by four. This validates use of the actual compact reduction and the divided trace, with no uncomputed higher integral action assigned to the source.

## Independent exact numerical checks

The independent verifier represents \((\mathbf Z/4)[\omega]\) by pairs of ordinary integer matrices. It does not import any author helper or executable. In each of the two actual character blocks it reconstructs all 256 whole Hermitian norm columns and all 512 whole endomorphism trace columns, checks that each is even, divides, and compares every resulting coefficient to the frozen record.

It enumerates all 1,024 elements of each actual ten-dimensional coinvariant space. The divided-norm kernel is exactly the 16-element image of the recorded source-involution map. It reconstructs all 384 allowable divided trace columns and confirms their rank is 16.

For all eight actual branch/framing matrices, it directly expands the orientation difference modulo four for all 384 columns. Thus 3,072 orientation identities are checked independently, including their signs. The output equals the complete frozen linearized map. Every one of the 80 recorded right-inverse columns is checked by multiplication, and each right inverse annihilates the entire actual source-involution kernel. The two image ranks are six.

These checks prove the specific map identities used in the proof; they are not a claim to reconstruct the marked graph from scratch. The author's full graph constructions and their sources were read, and root's separate replay covers their execution.

## Preservation of the actual lift

The new homology correction is zero on all other compact summands, has zero small image, and is even on the selected compact summands. The full affine map may have an odd cusp component, which the proof explicitly retains. The old invertible cusp/compact diagonal reductions still give an integral homology automorphism.

The earlier self-block corrections have an extra-projective or cusp factor and consequently vanish on the two new compact self blocks. Their actual cusp words have all 36 factors and preserve the integral homology map. The eight subsequent involution words use the current involution and have its fixed (Y)-image; their error is the actual commutator. Their coinvariants fill exactly the four-dimensional kernel just checked.

The proof then corrects the moving component **after** these eight words. Its coefficients lie in the retained source kernel and preserve (Y), the literal small conjugators and \(\mathcal W_h\). The final invariant augmentation correction uses the jointly onto old maps. Thus the error lies in the displayed \(\mathcal J_{65}\), with an invariant defining kernel, invertible Frattini map, and the actual marked fibre-product automorphism. The lower action is precisely D.65.9–10; the statement does not identify it with the formerly chosen lower action.

The dimensions follow from the actual surjection and its two retractions: the new kernel is \(\ker p_2\oplus\ker p_3\), of dimension 5,752 and coinvariant dimension 12. The total retained quotient has dimension 7,682 and coinvariant dimension 26. The remaining source maps onto the 1,918-dimensional old norm kernel, so the theorem correctly retains a nonzero unresolved source kernel.

## Centralizer comparison

The two Bass–Serre sequences give exactly the stated Tate groups for the order-two vertex and the order-four cusp Sylow subgroup. The literal fixed-vertex map is onto; its augmentation-kernel section proves the needed degree-minus-one surjectivity, hence the degree-zero vanishing for the comparison kernel. For the cusp Sylow subgroup both vertex modules are free, and the terminal augmentation comparison is identity; the kernel is Tate-acyclic. Odd averaging gives the order-36 norm statements. These arguments establish the actual centralizer homology maps claimed in D.65.11.

No new external theorem is invoked by this audit. The source anchors are the displayed integral maps and the already audited D.55, D.58, D.60, D.61 and D.64 constructions. No frozen source was changed.
