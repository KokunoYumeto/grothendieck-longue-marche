# Independent FGH audit of D78 — PASS

2026-11-15, after the checkpoint11 source release. I read the full 434-line candidate `notes/de_finite_sha_draft.tex`, the complete exact certificate, canonical D31/D39 normalization passages, and the relevant D77/D63 dependencies. This is an independent mathematical audit, not an inference from the finite calculation.

## Actual operator groups

The pair of inertia groups at2 and3 gives the full two coordinate translation groups because the untwisted action is unramified there and the two indicated valuation-one Kummer classes are primitive. Compactness then gives the actual global equality H semidirect I0. Its faithfulness is correctly checked using the substitution and the two exact boundary axes; it is not a dimension argument.

The K=Q(zeta5) S-unit basis zeta5,phi,pi has three independent local Kummer classes: valuation separates pi, while D77's exact depths separate zeta5 and phi. Localization is therefore injective on the Frattini dual. The closed local image surjects onto the Frattini quotient of the finitely generated pro5 group and hence the full group. Together with the actual order-four cyclotomic quotient this proves local surjectivity onto I0.

The primitive local translation line is also actual. If kappa6 vanished modulo5 on the kernel of the local map to I0, it would descend to I0 and inflate globally to the one-dimensional S-unit group spanned by kappa5. Its local valuation/unit class makes that impossible. Thus the kernel image is all Z5, not merely a finite-index line. Integral monomial gauges preserve the finite augmentation modules and the constant Cartier functional. Both global and local semidirect descriptions have the same zero-translation complement.

## Continuous coinduction and the whole local kernel

The Cartier dual of the completed group ring is continuous functions on the compact translation group with values in Q5/Z5. Continuous Shapiro/coinduction applies; the explicit contraction is continuous because compactness gives a uniform finite partition. The primitive local line has a continuous integral complement, so the same argument applies locally. The invariant constant module has character chi^(-1), obtained from chi² on augmentation and the one Cartier twist.

The exact local quotient substitution t1=t^beta,t2=t^(-alpha) has primitive kernel. D77's primitive cubic Soulé term becomes z³ times a unit because alpha,beta,alpha−beta are units. This bounds full invariants by the three-jet modules. The characters chi^(-1),chi^(-2),chi^(-3) exclude invariants on D_lin. On the quotient by constants, the three characters are chi^(-2),chi^(-3),chi^(-4); their pairwise differences are units, and v5(2^4−1)=1 gives exactly one F5. The cyclotomic kernel acts trivially on that quotient jet and2 topologically generates Z5 units, so this is the entire invariant group. The connecting homomorphism computes the entire local restriction kernel.

I checked the identification with the actual normalized c=48h modulo5 against canonical D31/D39. On ker chi it is the raw kappa3. The connecting defect has its nonzero cubic coefficient; the order-four scalar kills H1 of the cyclotomic quotient, giving equality of global classes. No formal arithmetic coefficient is chosen freely.

## One finite coefficient level at every place

The finite Cartier module M=(A/(5,(u,v)^4))^D embeds in W4^D. This ideal containment is in the correct direction. For every Frobenius, the displayed primitive lies in M: a constant when chi mod5 is not1, a linear coefficient functional when a or b is nonzero, and the fixed cubic vector −48 epsilon21 when both vanish. The inverse action signs and the Cartier multiplier were checked independently in the executed matrix certificate. Binomial denominators up to4 are units, so the reduction for chi=1 mod5 is valid for arbitrary actual 5-adic chi, not only the chosen finite representatives.

At2 and3 the constant primitive works on the entire decomposition group because inertia fixes it and c is unramified. Away from2,3,5 both module and cocycle are unramified, so a Frobenius primitive suffices. At5 the invariant-quotient connecting construction supplies an order-five three-jet primitive, and the integral gauges and substitutions keep it in the same M. Odd-primary cohomology handles the real place. Thus the same finite level works at every place; there is no exchange of a colimit with an infinite local product.

For the upper bound, a finite everywhere-locally-trivial cocycle must vanish on the kernel of its finite operator representation. Otherwise its finite affine image has a nonzero pure translation, and Chebotarev supplies a Frobenius with trivial linear part and nonzero cocycle, contradicting local coboundarity. This makes descent to I_s rigorous. Inflation is injective globally and locally at5. Filtered-colimit exactness gives the stated injection of the inverse finite-localization dual into the exact F5 restriction kernel. The actual c class remains nonzero after passing from lambda[5] to lambda because lambda has zero invariants (also its nonzero cyclotomic-kernel restriction cannot be a coboundary). The finite-level lower bound and the upper bound therefore agree.

## Sources and execution

- **verified:** Milne, Class Field Theory v4.03, V Theorem3.23, printed164, PDF zero-based172, https://www.jmilne.org/math/CourseNotes/CFT.pdf . Fresh primary openings `turn1033view0`, exact find `turn1034view0/1`. The finite affine-image Chebotarev use matches its scope.
- D77's local primitive Soulé certificate and its primary normalization were independently audited in `notes/fgh_D77_audit.md`; D63's finite-duality identification was reread during that review. Canonical D31/D39 exact coefficients were reread for this audit.
- Independent copied certificate: `notes/fgh_D78_certificate.py/.json/.out`. It executed PASS; the full JSON equals the author's, SHA256 `cb9fab8e579f58dfd6e5a552b21dbdc114d0d5da6d650da24af95db4244c5c50`. It checks500 actual Fox/Cartier primitive cases, the local line quotient matrices, the unique nonzero connecting primitive, the determinant valuation, and its pullback to the actual10-dimensional M.

No mathematical correction is required. The conclusion is exactly S_s=K_s=Z/5 and L5=T_s=0 for s=(kappa2,kappa3), with the actual rational point−2 providing a nonempty section fibre. No splitting of the separated-cohomology extension or higher-derived lifting claim is introduced.
