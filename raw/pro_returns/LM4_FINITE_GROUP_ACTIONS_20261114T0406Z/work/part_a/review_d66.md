# Independent audit of D.66

**Result: PASS.** I read the complete proof, metadata, and certificate, and independently reran the producer successfully. No mathematical correction is required.

## Actual extension, scalar action, and section label

The actual order-three and order-four representatives are supplied by the previously proved D.27 and D.46. The cusp-normalizer lift has the stated primary unit exponent: D.48 gives the cubic assertion, while in the quartic case its square is a lift of the positive involution and D.55 gives the two-adic unit. The quartic matrix has square minus identity over the two-adic integers. Since \(X^2+1\) is irreducible over \(\mathbb Q_2\), its characteristic polynomial is exactly that polynomial and its determinant, hence multiplier, is1. This verifies the needed primary boundary action.

At the stated scalar coordinate, every nonzero character transforms by the nontrivial scalar of exact order d. Its kernel is consequently normal in the actual semidirect product; the character itself is not incorrectly treated as invariant. The two quotient maps in D.66g are inverse through the specified normal forms. The chosen cusp-normalizer element has quotient order exactly d because its d-th power belongs to that kernel.

The conjugation calculation for the actual section is correct. In \(C_q\rtimes C_d\), conjugation by \((k,0)\) sends \((j,1)\) to \((j+(1-\bar u)k,1)\). The displayed \(k=j/(\bar u-1)\) is defined and sends the original labelled section to the distinguished complement. Conjugating the actual original section by the discrete word power gives the actual order-d section in \(E_N\). No quotient section is being lifted by an unsupported argument.

## Cover, boundaries, and the primary splitting

The kernel of the restriction to the dense discrete free group is the actual degree-q punctured-torus cover. The commutator has zero character, so the cover has q degree-one boundary lifts; Euler characteristic gives genus one. Finite-index topology identifies its full completion with N.

The named boundaries \(f^i c f^{-i}\) have all q distinct labels. Their homology has exactly the common total boundary relation. The element
\[
n_i=(vf^iv^{-1})f^{-j},\qquad j\equiv\bar u i\pmod q,
\]
is in N and gives the stated boundary conjugacy. This proves the exact primary action \(b_i\mapsto b_{\bar u i}\) since the primary multiplier is1.

Deck averaging by \(q^{-1}\sum D\) is available because \(q\ne p\). The action T conjugates the deck group by its scalar, so it preserves the averaging idempotent even though it need not commute with each deck transformation. The filled cover is the exact index-q lattice cover of the torus; its deck maps are translations. The boundary average is zero and the filled homology has trivial deck action. Thus the two identified summands and their maps are correct. The lattice inclusion has p-adic unit determinant, and its equivariance identifies the handle action with the named \(A_p(a)\).

Eliminating \(b_0\) leaves the nonzero boundary labels as a genuine basis. Their orbits all have length d. Both maps in D.66m therefore give a full integral equivariant isomorphism with the claimed regular modules. The formula
\[
\mathcal N\!\left(-\sum_{r\in R}b_r\right)
  =-\sum_{i\ne0}b_i=b_0
\]
is exact before reduction at any primary precision.

## Cohomology and both abelianized extension maps

On the handle lattice the stated polynomial identities imply zero cyclic norm. The determinant of \(T-I\) is p, so its fixed module is zero and its cokernel has order p. On each regular boundary module, the norm image is the full invariant module and its kernel is the image of \(T-I\). The ordinary finite-cyclic periodic cochain complex with these compact p-adic coefficients consequently gives exactly \(H^2=0\) and \(H^1=C_p\).

The kernel of \(N\to H_1(N,\mathbb Z_p)\) is characteristic, so P is an actual quotient of \(E_N\). Its kernel is precisely M and its quotient is the labelled cyclic group. The normal forms in D.66o prove that the action and the displayed cusp power give its entire multiplication.

The correction \(t=(-\kappa_p w)v\) has d-th power zero in the additive kernel by the exact norm identity, and its quotient label makes its order exactly d. The map \(v\mapsto(\kappa_p w,1)\) respects both the action and the cusp-power relation. Its composite with the forward map is
\[
\kappa_p w\,t=\kappa_p w\,(-\kappa_p w)v=v,
\]
while the other composite fixes the kernel and the labelled section. This proves the two inverse maps, not only abstract splitting. The coset of module solutions is the displayed \(-\kappa_p w+\ker\mathcal N\).

The last paragraph correctly retains the difference between this module statement and lifting every module vector to an actual finite-order element in the unquotiented group. The proof is a uniform consequence for the specified coordinates of actual actions; it does not construct an action realizing one of the still-unsettled scalar coordinates.

## Executed certificate

Independent captured stdout is work/part_a/d66_audit_stdout.txt. The rerun returned PASS with:

- 44 scalar-coordinate cases through q=97;
- 2,084 exact section-label conjugations;
- 2,040 comparisons each for inverse-module maps, deck conjugacy, and deck averaging;
- 44 integral norm preimages;
- 550 integral splitting-cocycle pairs;
- 2,090 finite-precision unit checks;
- 2 handle-polynomial checks;
- 820,992 integer vector-coordinate equalities.

The finite enumeration confirms the displayed formulas. Their arbitrary-prime and all-precision validity is supplied by the explicit maps and integral module proof.
