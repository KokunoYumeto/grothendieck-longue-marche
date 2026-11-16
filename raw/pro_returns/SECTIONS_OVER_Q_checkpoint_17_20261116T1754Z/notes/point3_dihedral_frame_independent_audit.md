# A212 independent saved-source audit

Reviewer: `/root/local_preprint`. Status: **PASS**.

Source: `sections/point3_dihedral_frame_classification.tex` (currently temporary statement label A.D8).
Source SHA256: `06837c2040018223bafb20944547f84967cda66c735281d99a5317595fd979e1`.
Certificate SHA256: `aaff0f44216d46ce7cb1b20e6e9db5e0e77cdba43a8a8c16875bf60944cdde7a`.

## Mathematical proof

I read the complete saved source and checked its actual arithmetic quotient against A210, the distinguished-lift construction in A40.4 and A40.15–16, and the punctured-disc section map in A49.

For every ordinary local centre at an odd prime greater than three, the finite frame makes the two inertia coordinates integers divisible by 24. Their three nonzero valuation patterns are the stated ones. In either one-sided pattern the other principal unit has zero two-primary Kummer class, so its chosen Frobenius coordinate is an integral coboundary `(q-1)v`. In the negative pattern the exact quotient of coordinates is minus a principal unit; the cocycle of minus one is `(chi-1)/2`, including its displayed coboundary. Substitution into the actual tame Hall relation gives the three stated central inertia formulas. Divisibility by four of the contact exponent makes each central coordinate even. Thus the actual D8 inertia is zero; no additional divisor of `q-1` was assumed.

After literal abelian-cocycle alignment, the global finite difference is a central quadratic character supported on 2, 3, and infinity. Direct multiplication in the arithmetic D8 extension gives conjugation characters `kappa(-2)` and `kappa(-3)` and zero for the central involution. This accounts for every geometric conjugator and remains valid after a central twist. The supported squareclass quotient therefore has exactly two cosets represented by 1 and 2.

The global central generator `(chi^2-1)/24` reduces to `kappa(2)` in the D8 centre. The 24 integral lifts consequently give the two finite geometric classes twelve times each. At the physical prime three, the two valuation residues force positive valuation of the ordinary centre. A49 then maps both that point and point three into the actual cusp-zero decomposition group. Its D8 inertia has order two, so the mod-two Kummer equality of the tangent parameters gives their finite section equality. This proof does not require equality of the full pro-two tangent parameters in the general frame. The two global D8 classes stay distinct locally at three: minus two is square, minus three gives the ramified character, and two gives the nontrivial unramified character. A40.4 therefore identifies the distinguished lift with the point-three D8 class. The final necessary-image statement for every all-place matching lift follows from that same exact local comparison.

## Independent execution

The fixed certificate was rerun completely with output-file writes redirected to a temporary directory. It passed all three symbolic Hall substitutions, 12,480 parity instances, 1,024 literal geometric/arithmetic D8 conjugation identities, the complete supported quadratic quotient and its local-three restrictions, and the 12/12 multiplicity check. The output, data, and source/certificate hashes are retained in `code/point3_dihedral_frame_independent_audit_*`.

No mathematical or editorial correction was required. This is a separate next-period result; the CP17 PDF and parent files were not changed.
