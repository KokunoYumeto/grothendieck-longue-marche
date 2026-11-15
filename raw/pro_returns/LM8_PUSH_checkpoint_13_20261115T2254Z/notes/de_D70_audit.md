# D.70 candidate: source and proof ledger

Status: unregistered candidate; no included source/register/bibliography changes during checkpoint09 freeze. Draft: `notes/de_numberfield_cusp_baire_draft.tex`.

## Exact new scope

For any affine hyperbolic curve over a number field with at least three geometric cusps and one chosen rational cusp, a dense G-delta set of completed parameters at that cusp has singleton actual full geometric pro-ell abelian section fibres, at every coefficient prime. Other cusps need not be rational. The full profinite conclusion uses exactly D.24 and D.56. This is applied to the actual odd Fermat curves and their map `t=-(X/Z)^n`, with cusp pushforward `(kappa(-1)+n*a,0)`; the sign at two is retained. No generic metabelian uniqueness or finite obstruction is asserted, and no one-cusp or two-cusp extension is claimed.

## Integral and topological checks written in the draft

- The peripheral line is primitive in integral homology. Boundary modulo that line is torsion-free; there are at least three geometric cusp directions, and any two have zero intersection.
- At a good finite place away from ell, an unramified extension splits all cusps. Boundary-quotient invariants vanish integrally. The proper Tate-module invariants vanish because reduction injects local ell-primary torsion into a finite residue-field group. Hence both `V` and `V/I` have zero invariants, and the local Kummer map of the chosen cusp is injective.
- Hoshi's actual specialization inertia alternative is applied before using the primitive free-group centralizer. The resulting local conjugator is adjusted inside the cusp and then has zero abelian image, so it belongs to the actual commutator group.
- The parameter space is finite ell-primary roots of unity times a uniform-ell-adic c0 module on a free basis of the torsion-free multiplicative group. Finite-rank units are included. Actual cochains are chosen linearly only on the free factor, and separately on each torsion component.
- For every finite place v, an element with divisor `h*v` exists, where h is the ideal class number. Removing its torsion component preserves the divisor. A depth-M perturbation changes only the valuation at v by `h*ell^M` and is divisible by `ell^M` as an actual cochain.
- Fresh Chebotarev places avoid the finite set of valuations not divisible by `ell^(M+v_ell(h)+1)`. The resulting new valuation has exactly `M+v_ell(h)`, so cannot cancel. No principal-prime condition is added to Chebotarev.
- Integral local coboundaries give a uniform finite ramification set for every reduced actual cocycle. Finite affine-image witnesses use actual elements before invoking Chebotarev.
- Descent is to the actual compact action image. Its normal inner-cusp inertia subgroup has trivial fixed group in the commutator subgroup, including nonprimitive inertia exponents.

## Primary sources reopened in this pass

1. Yuichiro Hoshi, *Conditional results on the birational section conjecture over small number fields*, RIMS1742 (2012), https://www.kurims.kyoto-u.ac.jp/preprint/file/RIMS1742.pdf. Appendix A setup pp.36–37 explicitly concerns ordinary geometrically pro-Sigma sections of arbitrary hyperbolic curves over local fields. Definition A.3 and Remark A.3.1 p.38 give the prime-to-residue-characteristic specialization square and geometric isomorphism. Proposition A.6 pp.41–42 gives the precise specialized inertia alternative. Opened refs: `turn840view0`, `turn841view2`, `turn842view0`, `turn842view1`. Existing key `DE_Hoshi2012`.
2. J.S. Milne, *Algebraic Number Theory*, v3.08 (2020), https://www.jmilne.org/math/CourseNotes/ANT.pdf. Theorem4.4 gives finite ideal class group; Theorem5.1 gives finite generation of units with the Dirichlet rank. Opened refs `turn845view0`, `turn846view0`, `turn846view1`. New pending bibliography entry in `notes/de_D70_pending_refs.bib`; not yet merged into included bibliography.
3. J.S. Milne, *Abelian Varieties*, https://www.jmilne.org/math/CourseNotes/AV.pdf, reopened `turn845view1`. The actual invariant argument in the draft is supplied directly through the integral reduction kernel; no unsupported numbered proposition is assigned to that statement.
4. Chebotarev uses the existing independently verified `PBC_MilneCFT`, ChapterV Theorem3.23. No new theorem scope is needed.

## Independent review

PBC read the complete draft and reports PASS. Its ledger is `notes/pbc_D70_audit.md`. The review explicitly checks integral invariants and Kummer injections, nonsplit-cusp discrimination, fixed torsion cochains, class-number perturbations without principal-prime restriction, finite capture and compact descent, D.24 scope, and the Fermat sign constant at two.

Root read the entire 524-line draft and reopened Hoshi's general Appendix A setup and Proposition A.6; the new proof passes. Root suggested the sharper hypothesis of at least three geometric cusps and only one rational cusp. I checked every step: only the chosen peripheral group must be Galois-stable; all other peripheral lines are compared geometrically, while their quotient becomes Tate after an unramified cusp-splitting extension at good places. No other rational cusp appears in the parameter construction, actual action, global Kummer injection, Chebotarev argument, or D.24 application. The notes-only statement is sharpened accordingly. No integration approval during the checkpoint freeze is presumed.

## Integration

After root released the checkpoint09 source freeze, D.70 was registered as Proved and included in sections/D_numberfield_cusp_baire.tex. Root and PBC both passed the full proof and the sharpened geometric-cusp hypothesis. The verified ANT entry was merged into de_refs.bib. The original draft and pending-entry file remain as the audit trail; no diagnostic PDF was created.
