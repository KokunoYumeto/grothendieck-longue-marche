# F.12–F.14 and F.18–F.30: final independent stack-germ audit

Frozen: 2026-11-13, 23:40 UTC. Statement F.51 is **Refuted**, with complete proved replacements in its proof. Root, Montpellier, and spheres independently read the complete proof and agreed with the correction. No additional LaTeX macros are required.

## Delivered files

- `F51.tex`: numbered statement F.51 and complete proofs.
- `F51_results.csv`: one canonical eight-column result-register row.
- `F51_readings.csv`: one five-column mathematical-scope reading row; no new palaeographic reading is claimed.
- `F51_references.bib`: verified primary reference `FA_Moerdijk2002`.
- `code/F51_checks.py` and `code/F51_checks.output.json`: executed exact supplementary checks.

## Finding and counterexamples

The unrestricted identification between intrinsic actual-open-substack neighbourhood pro-topoi and a descent object built from independently formed neighbourhood germs on an arbitrary étale atlas is false. The difficulty is the exchange of the filtered germ colimit with an infinite atlas descent diagram, not fixed-stage sheaf descent.

1. For the rotation stack [Delta / mu_infty], the annular functions b_n(r) cos(n! theta) define an individually invariant germ for every group element and a coherent datum on the entire independently formed atlas-germ nerve. The tuple-dependent radii cannot be replaced by an actual invariant representative on one neighbourhood. Mapping to the localic topos Sh(R) detects the difference directly: genuine invariant continuous functions are radial, whereas the constructed germ is nonradial in every disc.
2. The same construction on C* x Delta, with mu_infty rotating the first coordinate and the stratum C* x {0}, has a free action. A compact circle supplies the necessary common small transverse disc in the contradiction. Finite or even trivial isotropy therefore does not replace properness.
3. For [P1 / Z], with generator z -> z/(1+z) and D={0}, every invariant open neighbourhood of D is all P1. Its intrinsic deleted neighbourhood is [C_w / Z], w -> w+1, hence C*, with fundamental group Z. The derivative on the normal line is trivial, so the punctured normal stack has fundamental group Z^2. The meridian is killed and the operator survives: (a,b) -> b. Thus the unrestricted intrinsic tangential equivalence fails even for finite coverings, and not only for full sheaf topoi.

## Proved replacements

Every intrinsic pro-neighbourhood construction remains meaningful for arbitrary étale stacks if the full Čech diagram varies over one common actual open-substack stage. Descent data for a fixed target topos have an inverse-image functor, an invertible overlap comparison, and a cocycle equality in degrees 0, 1, and 2. Their finitely many stage indices admit a common refinement. The same argument applies to morphisms and equalities, then to pro-targets. It proves synchronized descent and the intrinsic two-open pushout without properness.

For proper étale groupoids with paracompact locally compact orbit space, relatively compact finite-group quotient charts and properness over compact chart pairs/triples yield finite local bisection constraints. Finite isotropy minima and a positive continuous minorant synchronize these constraints. This proves the chartwise comparison under the geometric hypotheses used by F.13. The proof does not assert invariant cofinality for arbitrary unbounded atlas neighbourhoods: even proper Z-translation on R^2 has the counterexample |y| < exp(-x^2). Data are first restricted to relatively compact quotient charts, glued to one stack neighbourhood, and compared to the original atlas data by their individual common refinements.

The same conclusions hold for an explicitly specified controlled atlas having this common-stage realization property. That condition is a hypothesis; it is not silently supplied to an arbitrary nonproper presentation.

## Audit of current scope changes

The space versions of F.12–F.14 and the common-stage intrinsic two-open pushout remain valid. The revised final paragraph of F.13 correctly limits the independent atlas-germ comparison to proper or explicitly controlled presentations. F.18 explicitly separates the unconditional intrinsic two-open argument from this additional atlas computation. F.19 now keeps the coherent chartwise sector functor distinct from its intrinsic neighbourhood interpretation, and invokes the proper/common-stage hypothesis for the latter. F.20 retains its independent nonexistence statement for the unipotent operator action.

The shared scope paragraph preceding F.26–F.30, the scope sentence and proof in F.26, and the final distinction in F.27 have been read and pass. In particular ordinary vector-bundle descent on an atlas is kept separate from identifying a normal bundle with an intrinsic neighbourhood germ. No new restriction is imposed on abstract exit-category, full-flag homotopy-colimit, or bar-construction statements that use genuine diagrams rather than the invalid atlas-germ substitution.

## Primary source verified

Moerdijk, I. (2002). *Orbifolds as groupoids: An introduction*. arXiv:math/0203100. https://arxiv.org/pdf/math/0203100

Section 3.4, printed page 8, explicitly gives arbitrarily small quotient charts by finite isotropy for proper étale groupoids; no effectiveness assumption is needed. The primary PDF was opened and its exact passage read. The stronger synchronization proof and all three counterexamples are supplied in F.51; they are not attributed to this local-chart statement.

## Exact supplementary computation

All checks passed: 16 annular support and signed-witness checks, 816 rotation residue checks, 584 tuple-subgroup factorial checks, and 1681 parabolic matrix products. The source proof handles arbitrary orders, tuples, and neighbourhoods; these finite checks are supplementary and are not used as a substitute for that proof.
