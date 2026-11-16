# C47 independent complete proof and exact-code audit

**Verdict: PASS.** The complete notes candidate and complete standalone solver were read. The actual C12 intertwiner proof, C20 frame/covariance construction and C46 witness/normalization were reread at their exact used scope. No fresh external theorem is introduced in the new finite centralizer argument; its coordinate proof and the characteristic-envelope construction are reproduced in full.

## Actual finite detector

The coset module is the left permutation module on right cosets Q/<h>. The identity coset is h-fixed, so its coordinate in (1-h)a is zero. The right side delta_H-b delta_H is nonzero at that coordinate unless b is in <h>. This proves the exact centralizer projection, including when other modules are present. The pure base meets both cyclic torsion subgroups trivially. Thus solutions in the full ambient affine group have the same base as the actual full torsion frames; neither surjectivity of the geometric image nor descent of the automorphism to that single affine quotient is required.

The group order, derived images 96,8,2,1, and the abelian translation extension imply L^(4)=1. All continuous maps from the two-generator free profinite group to L form a finite set of exactly |L|^2 maps. Their kernel intersection is fully characteristic, kills F^(4), and is finite-index. The fixed affine pure restriction is among these maps.

## Normalized multiplication and characteristic quotient

From Phi_f(tau)=tau and Phi_f(s)=sf one gets alpha_f(x)=x and alpha_f(y)=f^{-1} y f in the temporary marking. Composition gives f_gh=f_g alpha_g(f_h) directly. Therefore a retained f modulo the fully characteristic kernel determines its induced automorphism on C and the product of retained pair residues. This gives a finite group of actual residues. No claim that every algebraically compatible finite residue is actual is made. The inner marking adjustment multiplies both frame and intertwiner on the same side, so A^{-1}V and beta^{-1}V remain the specified CM coordinates.

The global-sign normalization modulo four is the established actual CM normalization. With it, the cube in the cubic order-six centralizer and square in the quartic order-four centralizer recover exactly the two parity bits. The unique upper-unipotent intertwiner is checked against both base generators; its uniqueness follows directly by their matrix centralizer.

## Exact solver and sharpness

The entire code was independently imported and Detector.verify() executed without touching the author's source or output. Every JSON field is identical, including the source hash. The literal cycle elimination solves (1-k)a=d, and verifies each returned conjugator by multiplication. The identity, common pure-inner-frame and finite-only parity-one tests all pass. The latter is explicitly not used as a full lifting theorem. The actual full nonzero witness is C46.

If f lies in F^(4), its affine residue is one and both pure frame bases and the normalized intertwiner are one, so Delta vanishes. C46 gives a genuine f in F^(3) with Delta one. This proves least retained derived depth four. It does not identify the outer-action kernel; that distinction is retained throughout.

Exact hashes and the full replay are retained in the adjacent JSON and de_C47_certificate_rerun files. No source or canonical section was changed by this audit.
