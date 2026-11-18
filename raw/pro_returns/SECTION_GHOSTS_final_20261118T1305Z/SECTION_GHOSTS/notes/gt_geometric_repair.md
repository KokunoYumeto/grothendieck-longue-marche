# Ten-point GT geometric repair: exact scope and source log

## Outcome

E176–E179 in sections/part_E_gt_geometric_repair.tex independently reconstruct a qualitative geometric input that was missing from the supplied historical A4.34–A4.39 chain. The construction retains a single labelled Klein subgroup, one source automorphism, both actual forgetting maps, the same Schreier coefficient, and the braid centre. It does not certify the original explicit finite-recursion bound or the later CM vanishing theorem. At this initial stage GT C5/A4.1/A7/A4.57 were pending. Subsequent E190-E191, E195, E197-E198 and E201 close C5 (with its source-Open universal-target clause), A4.1 and A7; only the literal A4.57 compiler remains pending.

The root full proof read and primary-source checks are positive. The cohomology agent also completed full independent E176-E177 and E178-E179 reads, checking the finite-cover/component proof and then the actual quartet maps, ambient completions, Schreier coordinates and braid centre without a defect. Their original Illman scan opening supplied no readable OCR; root and owner visually checked the thesis locator, and the owner subsequently opened the published journal theorem in the Göttingen volume scan. The certificate is code/check_gt_klein_geometry.py and its JSON output; all 32 labelled cases and the coordinate/Schreier identities pass, with data SHA256 1a3fbffc081ade0cb5b7ab3d5c0add017403022a0b90e6e22dd6a10c3929bbdc.

## The actual repair

**E176.** For a smooth aspherical manifold with an iterated finitely generated free fundamental group and a named C2-squared action, every given finite output has a genuine finite refinement recognizing the ordinary centralizer image and fusing every elementwise labelled complement to a fixed-locus path subgroup. The proof first kills every positive mod-two cohomology restriction by a finite free-group homology construction and a two-row LHS argument. Characteristic refinements make every cover compatible with the actual ambient action.

The topological comparison uses bounded-dimensional equivariant triangulations, with product cellular cochains if the triangulation is infinite. It does not assume the noncompact moduli space has a finite triangulation. Two cyclic complete Tate comparisons give fixed-component recognition. For a varying complement action there is no invariant basepoint, so the proof uses the cone of constants; its degree-minus-one class detects an empty fixed set. This gives the required finite fixed point before any conjugator is chosen. The finite centralizer representative is an actual path in the fixed locus, rather than an inference from an infinite centralizer formula.

**E177.** The labels are A=(0,infinity), B=(1,-1), C=(i,-i), and D the regular orbit of z under -z and 1/z. The exact fixed locus in M0,10 has two components. Normalizing the labelled A pair and B-plus determines the Möbius action and leaves only the ordering of C and the free parameter z outside the six exceptional points. The order-32 label centralizer is the product of three independent pair flips and the regular-orbit translations. A C-pair half twist exchanges the two components. Finite fusion therefore uses precisely a pure element or a pure element times this one half twist, which both relevant forgetting maps kill.

**E178.** The ordinary subgroup represented by fixed paths is dense in the full completed centralizer by E176. It is enough to use this subgroup; no complete ordinary centralizer classification or unproved equality of subgroup completions is required. Its base-component label group acts on z through the free Klein action, with invariant u=z²+z⁻². The two selected quartet maps have coordinates u and 2(u+6)/(u−2). At z0=1+sqrt(2), u0=6; the auxiliary coordinate w=(u−6)/(u+2) turns the comparison into w↦−w, so symmetric cusp arcs give the literal swap of the two generators. Full continuity is proved by restriction of the actual forgetting maps on finite-index ambient label stabilizers.

**E179.** Standard full-GT genus-zero naturality and the one corrector from E177 give inner equivalence of the two target actions. The exact profinite cusp-centralizer assertion follows from finite graph-cover refinements. In the index-two free subgroup the two retained abelian coordinates force t=−4c and s=4c. A separate central character of the actual coloured braid subgroup, taking its centre to twice the integer generator, recovers the central factor. The resulting identity is

f(u,w^4)=w^(8c) f(u²,w²) u^(4c) (uw)^(-6c),

with c the exact Schreier coefficient of f, at every multiplier.

## A remaining literature distinction

The opened Nakamura–Schneps paper defines its rho2 by a symmetrizer. Proposition 5.3 identifies that rho2 with minus A_F(-1,1) only on the subgroup satisfying their additional III-prime relation. The Schreier coefficient in E179 is directly minus A_F(-1,1), but that does not by itself identify the two extensions on all GT. Their published full tower theorem also has its additional-relation hypotheses. We therefore do not use the IV-shaped relation alone as permission to invoke that theorem, and do not infer the CM vanishing from the common division field.

The remaining historical CM application still needs its exact genus-one/branch-covariance comparison, or a complete alternative route establishing the necessary common signed conjugator. E176–E179 reduce this dependency; they do not close A7.

## Sources opened

1. **Illman, S. (1972). _Equivariant algebraic topology_ [Doctoral dissertation, Princeton University].** Primary scan: https://ncatlab.org/nlab/files/Illman_EquivariantAlgebraicTopology1972.pdf. Theorem 3.1, printed p48 / PDF p53, states equivariant triangulation for a differentiable compact-Lie-group manifold. The scan was downloaded, relevant pages OCR-read, and p48 visually inspected. Web open turn347192946view1; the web parser has no extracted text. The actual local visual inspection used the rendered scan, now under build/gt_repair_work, which is excluded from the checkpoint. Web screenshot outputs were text-only and are not counted as visual inspections.

2. **Illman, S. (1978). Smooth equivariant triangulations of G-manifolds for G a finite group. _Mathematische Annalen, 233_, 199–220.** DOI https://doi.org/10.1007/BF01405351. Publisher metadata opened at https://link.springer.com/article/10.1007/BF01405351, ref turn254326860view0. The requested direct publisher PDF redirected to metadata. Subsequently downloaded the primary Göttingen volume scan from https://gdz.sub.uni-goettingen.de/download/pdf/PPN235181684_0233/PPN235181684_0233.pdf (301 PDF pages; web service rejected only because file exceeds 10 MB). OCR-read printed pp199-204 (PDF pp206-211) and visually inspected printed p199/PDF p206: the opening unnumbered Theorem, part1, states existence of a smooth equivariant triangulation of every smooth finite-group manifold, with or without boundary. Printed p201/PDF p208 explicitly allows countable locally finite finite-dimensional complexes and states the no-inversions property. This directly supplies the exact finite-group result used in E176. Download and review renders remain in excluded build/gt_repair_work; no full-article reproduction is included in deliverables.

3. **Schneps, L. (2006). Automorphisms of curves and their role in Grothendieck–Teichmüller theory. _Mathematische Nachrichten, 279_(5–6), 656–671.** DOI https://doi.org/10.1002/mana.200410383. Opened author-hosted publisher PDF https://webusers.imj-prg.fr/~leila.schneps/automorphisms.pdf, ref turn517933339view0. Sections1–2, pp656–660, give the actual moduli/mapping-class orbifold setup and distinguish the standard genus-zero action from additional special-morphism relations. Its stated extra-relation scope is retained.

4. **Nakamura, H., & Schneps, L. (2000). On a subgroup of the Grothendieck–Teichmüller group acting on the tower of profinite Teichmüller modular groups. _Inventiones Mathematicae, 141_, 503–560.** DOI https://doi.org/10.1007/s002220000074. Reopened author version3.14, https://webusers.imj-prg.fr/~leila.schneps/newGT.pdf, ref turn399098827view0. Exact locators: standard braid formula(1.1), author pp2–3; Definition1.1 and Theorems1.2–1.4, pp3–5; Definition5.1, Proposition5.3 and the following discussion, pp17–18. Find/open refs turn250107519view0 and turn250107519view1. The distinction between the two rho2 extensions and the III-prime hypothesis was checked in the actual text.

## Search and dependency audit

Opened the supplied later finite configuration recognition/fusion proofs (part_a_effective_configuration_recognition.tex, part_a_finite_configuration_fusion.tex, and part_a_involution_configuration_recognition.tex) and reread the exact A4.39 file. Their methods suggested the replacement, but no historical label “Proved” was used as an input.

Searches included: finite group equivariant triangulation semialgebraic pair finite simplicial complex theorem Illman; “Smooth equivariant triangulations” Illman 1978 pdf; “BF01405351” pdf gdz.sub.uni-goettingen; and Nakamura Tsunogai harmonic equation GT relation IV proved pentagon 2006. Primary Illman thesis and published metadata, Schneps2006, and Nakamura–Schneps2000 were opened. Secondary search hits were used only as locators. No claim of priority or assertion that this general finite-cover mechanism is new is made.

The standard-library certificate independently enumerates the label-centralizer choices from equivariance on the four actual orbits, compares them with the bit description, tests both coloured stabilizers and H intersections, and verifies exact polynomial/Möbius and free-product word identities. It is a certificate for those finite/algebraic claims; it is not a finite census of genuine gentle or GT source records.

## Exact coefficient used in the historical CM character

The historical rho is the symmetrizer extension, not merely the Ihara A_F specialization. In the normalized modular group let theta exchange x,y and write alpha(s)=beta s beta^(-1), with beta pure. Comparing alpha(y) computed from sxs with f^(-1)y^lambda f gives f beta theta(beta)^(-1)=y^t by the primitive cusp centralizer. Abelianization forces the two beta coordinates equal and t=0. Hence f=theta(beta) beta^(-1), so g_F=beta^(-1) is the symmetrizer satisfying f=g_F(y,x)^(-1)g_F(x,y). Its diagonal abelian exponent is exactly the rho used in LM7 E65 and historical A.C2. The Ihara extension in Schneps2006, printed p657, is minus A_F(-1,1)=c2 by definition. E179 does not silently identify these two coefficients.

## Subsequent precise checks

The cohomology reader independently re-derived all of E178-E179, including the (4c,2c) Schreier image and central exponent -2c. The journal Illman theorem was opened after checkpoint05; this strengthens source verification without changing the proof. Parent has requested the next exact task: prove or refute the symmetrizer=c2 comparison, keeping all four historical GT statuses pending in the meantime.

## Coefficient gate subsequently closed

E180 in sections/part_E_gt_coefficient_bridge.tex independently proves the equality of the symmetrizer and Ihara/Schreier coefficients at every multiplier. Its proof retains the literal theta change and historical beta frame and has passed root full proof/source review. The earlier boundary discussion records what E179 alone established; E180 closes that coefficient gap without proving III-prime or the later signed CM covariance.
