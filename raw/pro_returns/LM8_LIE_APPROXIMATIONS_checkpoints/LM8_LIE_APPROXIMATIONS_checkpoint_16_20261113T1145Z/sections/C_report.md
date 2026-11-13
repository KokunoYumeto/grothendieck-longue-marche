# Part C: completed characteristic-zero classification and integral tests

| Requested task | Statements | Outcome |
|---|---|---|
| Item2 and exact manuscript question | Opening paragraph, C.1–C.9 | General assertion refuted; strongest correct existence criterion proved |
| Over Qbar | C.1–C.3 | Complete classification, including bad spherical gerbes and effective bad footballs; family-wise obstruction proofs |
| Descent to Q | C.4 | Proved: geometric existence descends after changing finite cover/group |
| M11 over Z | C.5–C.7 | pi1^et=1; no finite etale scheme atlas; finite level-three atlas exists after inverting3 |
| M04/M05 with symmetric groups | C.8–C.10 | Labelled integral pi1 trivial; quotient-stack pi1=S4,S5; V4 retained in the four-point case; dimension2 explicitly retained in the five-point case |

## Findings and proof structure

The question occurs in §52.2, folio744, scans193–194: a connected smooth separated finite-type multiplicity of dimension1 is conjectured to equal [U/G]. The immediately following finite etale scheme-cover formulation is the one used. Characteristic0 is imposed only after this question, and the modular/integral discussion occurs at folios745–746, scans195–197.

For effective orbifold curves the only failures are a projective line with one cone point or two unequal cone orders. For a football F(m,n), the fundamental group is C_gcd(m,n), and the two inertia-kernel orders are m/gcd(m,n) and n/gcd(m,n). This excludes each bad member explicitly.

For a general DM curve, the complete criterion is that its analytic universal cover be an ordinary curve. A spherical universal cover P(r,s) with either weight greater than1 is an obstruction. The paper lists the exact cases by the effective orbifold signature and the kernel of generic inertia. In particular P(n,n), n>1, is a simply connected nonneutral root gerbe over P1, so the effective-orbifold list alone is wrong. The neutral gerbe P1×Bμ_n is a finite quotient and shows that ineffectiveness alone is not an obstruction.

Over Q there is no further obstruction to existence: descend an atlas to a finite field extension, compose with the finite etale extension of the base, and take a frame torsor or connected Galois closure. This does not claim that a chosen group or geometrically connected atlas descends unchanged.

For the integral test, C.5 extends finite etale covers across a relative normal-crossings boundary that meets every residue characteristic. C.6 then computes the compactified elliptic stack through the general Weierstrass atlas W=A5_Z−V(c4,Delta) and the connected coordinate-change group. The complement has codimension≥2, purity identifies pi1(W) with pi1(A5_Z), and the latter is trivial by the generic fiber and the absence of everywhere-unramified number fields. Connected descent then gives pi1(barM11_Z)=1; the boundary lemma gives the open-stack assertion. This proof includes2 and3. Its nontrivial inertia prevents a finite etale scheme atlas.

For M04 and M05, the explicit compactifications are P1 and the blowup of P1×P1 in the three diagonal sections0,1,∞. Their relative SNC boundaries satisfy the same lemma, and their geometric compactifications are simply connected. Boundary Z-sections eliminate arithmetic covers. The quotient atlases remain finite etale for constant finite groups even in characteristics dividing the group order. The S4 action has ineffective kernelV4; replacing it byS3 changes the stack and its fundamental group. M05 has relative dimension2, so only a surface, not a curve, can be its finite atlas.

## Exact literature checks

Behrend–Noohi: Theorems1.1,4.2,4.4; Remark4.3; Propositions5.6,5.7,7.2,7.4–7.6; Corollaries5.9,5.10,7.7 were checked against the supplied original LaTeX and the opened author PDF. Their Proposition7.6(ii) has a second-weight misprint, corrected using its proof. Their final subgroup generator list in the proof of Corollary7.7 omits Schreier conjugates; the kernel of a surjection to C_n supplies the required index-n subgroup, and the finite-cover proof is given explicitly.

SGA1 XIII Proposition5.5 was checked in the original recomposed PDF, p.332 (printed p.317; original pp.431–432). Its tameness hypothesis is over maximal points of the base, which for Spec Z is the generic point, and its conclusion uses exponents prime to the residue characteristic. Thus C.5 does not assume tame special fibers. X Theorem3.1 supplies purity. Milne's author text, Theorems4.3 and4.9, verifies the number-field input. Bruin's §4 constructs the full-level-three scheme explicitly; Theorem7.1 states the finite etale smooth affine result.

Actual manuscript images inspected: scans193 and194. Remaining C passages were read in the checked transcription. The ambiguous U/M in formula(10) is recorded, but none of the proofs depends on deciphering it.

## Reproducible checks

`python code/c_stack_checks.py` completed successfully. It exhausts all144 ordered football pairs with weights1–12 (12 good,132 bad), all24 S4 cross-ratio substitutions (six functions, four permutations each), all120 S5 actions on ten boundary divisors (trivial kernel), and all81 matrices overF3 (48 invertible,24 determinant1). Exact symbolic polynomial computation gives gcd_Q(c4,Delta)=1; the primitive a1^4 coefficient excludes vertical common divisors. The nodal model has c4=1, Delta=0 and tangent determinant−1 overZ, which verifies the all-characteristic assertion without finite-prime sampling.

Artifacts: `code/c_stack_checks.py`, `.json`, `.out`; metadata regenerates with `python code/a_c_metadata.py`. All requested Part C questions are decided with the stated stack, finite-group and dimension conventions. No priority claim is made. Status counts:6 Proved,2 Known,2 Refuted.
