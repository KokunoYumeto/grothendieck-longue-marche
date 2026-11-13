# Full intrinsic cubic class-two section classification: E.37

The theorem in sections/E_intrinsic_class2.tex evaluates both the entire image of the section map to the full rank-ten abelian section group and every nonempty fiber. It uses the full intrinsic group N/gamma3N, not a two-coordinate image or the cuspidally central quotient.

## Arithmetic input and exact maps

The eight cusp coordinates in E[3], the Weil pairing sign, and the generalized-Jacobian extension give the actual integral ten-dimensional Tate lattice. The toric rows U=(v,-u) and j=[3I;U] determine the complete Frobenius matrix from the cubic Jacobi sum, with no unresolved higher-action term on the boundary. The determinant line L in the45-dimensional exterior square is primitive; its projection to the elliptic exterior square has index9. The correct rank44 local correction domain is therefore M/L, while its target is the kernel M0 of that elliptic projection.

For every nonbase cusp d, the proof compares the actual abelian tangential-path torsor with the Kummer torsor of the explicitly framed line bundle z_d=O(d-O). The tangent-line ratio f_d supplies every component of3z_d, and the program lists all64 values as epsilon/lambda S-units. The path convention fixes the arithmetic peripheral term as minus kappa(z_d) wedge e_d. The independent E31 residue at7 checks this sign.

## Complete obstruction criterion

For a full abelian section alpha and every prime of K=Q(zeta3) away3, its tame inertia value lies in the toric rank-eight lattice. Its Frobenius value and all eight cusp Kummer values give D_q=alpha(F_q) wedge v_q minus the sum of v_{q,d} kappa(z_d)(F_q) wedge e_d. The actual tame relation produces this exact support representative. The matrix q^-1 exterior-square(A_q)-1 induces an invertible rational map M/L -> M0. The unique correction must lie in the integral rank44 lattice at every prime and tend to zero modulo every3-power. Those two requirements are necessary and sufficient for the global class-two section.

The proof preserves derived inverse limits: it first takes finite-support localization at finite coefficient level, then takes the derived inverse limit of the actual two-term local complexes. Consequently no phantom obstruction is lost. Restriction from Q to K is injective in the three-primary obstruction group, so the criterion evaluates sections over Q itself. The Kummer input is evaluated by division of explicit framed points over finite fields; it does not assume an unexplained arithmetic action obtained from the toric minimum.

## Every nonempty fiber

The complete fiber is a torsor under R_{p!=3}(Z3) direct sum Z3^24 direct sum (Z/3)^9 direct sum (Z/9)^5. The restricted prime coordinates are actual central Kummer twists kappa(p)w. For the unramified component, the two conjugate Frobenii at7 freely generate the rank2 pro3 Galois group, and complex conjugation swaps them. Evaluation at one of them gives the exact presentation M/(B_tau-1)M^c. The official program supplies exact rational left and right Smith transformations, all of whose denominators are units at3. It verifies the diagonal with seven units, nine factors3, five factors9 and24 free coordinates. These matrices provide explicit coordinates for every fiber.

The distinction between a primitive geometric Tate line and its arithmetic cohomology image is retained: the natural prime3 Kummer class can be divisible by3 in the unramified cohomology group. Thus the natural formula uses primes other than3 and24 additional free coordinates.

## Programs and exploration

e_intrinsic_class2.py/.out/.json is the official exact certificate, including all cusp frames, the Weil sign, the full lattice matrices, the Smith coordinate transformations and six local determinant checks. Every check passed.

e_intrinsic_lattice_explore.py/.out/.json supplies an independent simultaneous-invariant calculation, yielding the same torsion and the previous E24 torsion C3^3 on V. The first exploratory attempt used SymPy's unrestricted integer Smith algorithm on a135-by45 matrix and was interrupted after it failed to finish promptly; it had completed the V calculation only. The revised exploratory script uses a proved exponent bound and arithmetic modulo3^5. The official certificate instead uses exact rational DVR operations and completed immediately. No mathematical conclusion was drawn from the interrupted attempt.

The still further maps are N/N'' -> N/gamma3N and N/gamma3(I_marked) -> N/gamma3N, with kernels gamma3N/N'' and gamma3N/gamma3(I_marked). E37 computes the complete intermediate section set through which those requested further lifts must pass; it does not assert their obstructions vanish.

The pairing convention was audited directly using Enge2015, section3 and Remark9. An opened textbook presentation reverses the pairing arguments; applying that convention to the divisor formula would reverse the actual frame sign. The official lattice uses U=(v,-u), derived from the inverse divisor pairing in the vector frame. The exploratory lattice used the opposite sign and is related to it by the exact basis isomorphism diag(I2,-I8), so its invariant factors agree. The official full matrix and its coordinate certificate have been recomputed in the corrected actual frame basis.

The tangential comparison includes its local frame sign: removing tangent powers produces negative frames at the two endpoints. The exact difference from z_d is the order-two torus point epsilon_d with−1 at d andO. It has the constant compatible3-power division sequence epsilon_d, so its pro3 Kummer torsor is canonically trivial. Tensoring that trivialization is the actual comparison map; no full-profinite frame equality is assumed.

## Explicit abelian inputs and the next local calculation

Formula (E37.22) evaluates the proper elliptic input as Z3 plus Z/3 on the same two actual free Frobenius generators. For representatives b in Z3 and r in {0,1,2}, the values b f1+r f2 and its conjugate give an explicit unramified lift to the full generalized-Jacobian lattice. Every remaining input is then a unique toric Kummer class in two rational and three Eisenstein multiplicative completions. The representative choice is a set bijection, with no asserted group splitting.

The auxiliary program e_intrinsic_19.py/.out/.json computes the exact local rank44 Smith forms at both primes above19. Both have valuations 0 repeated8, 1 repeated6, 2 repeated18 and 3 repeated12, so the cokernel exponent is27. This exact computation is used by the subsequent E38 example; its proof and finite metabelian obstruction are recorded in that separate section.
