# Complete root audits after checkpoint 10

## A.61 — uniform inert-prime Heisenberg covers

**Full proof audit PASS, 2026-11-15 20:23 UTC.** The complete 479-line candidate `notes/fgh_A61_draft.tex` was read, not merely its statement or certificate. This is a uniform proof for every prime congruent to three modulo four; the finite executions are corroborating exact certificates.

The trace-zero point count gives the actual endomorphism identity (F^2=[-p]). I freshly opened Silverman's primary PDF, Exercise III.3.7 in its general-characteristic scope (printed pp.105–106) and Theorem V.2.3.1(b) (printed p.142): https://www.math.ens.psl.eu/~obenoist/refs/Silverman.pdf . The current retrievals are `turn961view0` and `turn961view1`. The relative-primality and monic-numerator assertions apply also at p=3. Part (f)'s branch divisor is used in characteristic zero. No reduced geometric-kernel divisor is substituted in characteristic p.

I checked the integral divided operator on the affine elliptic ring, including well-definedness under changing lifts. Quarter-rotation proves (D^p=0) in characteristic p. The multinomial orbit argument proves (E(b^p)=-(Db)^p); the separate p+1-factor expansion proves the stated formula for (E(R^{p+1})), including its single-p-derivative terms. The operator is never assumed to be a derivation.

The division differential identity is proved from all principal parts and its zero constant term in the invariant formal coordinate. Substitution of the actual division polynomial identifies (Dh=R^p). Its leading term proves the exact pole order p of R. The pole bound on (D^{p-1}x), the genus-one absence of a single simple pole, and odd parity prove (DR=a\ne0) and (E(h)=-R). Every function and scalar is over F_p, so the use of (a^{p-1}=1) is justified.

The pole-bounded Frobenius roots A and S exist in the actual affine function ring. Applying E proves (DS=RA/a). At each of the p simple zeros of R, this forces the S contribution to have order at least 2p, while the R contribution has exact order p+1. Thus the otherwise invisible degree-p Taylor term actually vanishes. This is not inferred just from the ordinary differential.

I checked the main and both kinds of tail charts, their integral coefficients after unramified centre lifts, the exact binomial scaling, positive valuations of all discarded coefficients, smoothness at their generic points, and Artin–Schreier irreducibility. The displayed uniformizer has valuation one and translated difference of valuation p+2, giving jump p+1 and the asserted genus. The known positive-genus persistence argument and the genus equality force a tree and rational remaining components. The degree-p main map exhausts the actual map degree. All p² marked cusps therefore lie on the rational marked tree above the unique main point over O.

The characteristic-zero translation lifts give the actual central deck extension. Peripheral inertia makes it nonabelian, and quarter-rotation forces the additive p-th-power map to vanish; hence its group is the exponent-p Heisenberg group. The already audited A.41–A.42 and A.59 apply with their actual hypotheses. No cofinality or universal Task A.5 conclusion follows.

**Independent root execution PASS:** `python3 notes/fgh_A61_certificate.py` completed successfully at p=3,7,11,19, including the characteristic-zero identity, divided operators, actual Frobenius roots, hidden Taylor terms, valuations and genus. Output was observed in full. The retained canonical certificate output and JSON record the same exact assertions.

## D.75 — explicit free factors of the compact Alexander obstruction

**Full proof audit PASS, 2026-11-15 20:23 UTC.** I read the entire candidate `notes/de_compact_axis_draft.tex` and reread D.35's actual action and the complete relevant local/global inverse-limit argument in `sections/D_alexander_separated.tex` (D.63).

The stable quotient by v has the exact multiplier (t^{a(g)}\chi S_\chi(t)); the beta factor becomes one. After the Tate twist, multiplication by u is an integral topological isomorphism onto the augmentation ideal, with actual affine pushforward action. Its Cartier dual is precisely locally constant torsion-valued functions on Z_5 modulo constants. No claim that a high translation power is trivial on the full module modulo a finite power of five is used.

For either global or local Kummer cohomology, primitive reduction remains nonzero on the cyclotomic kernel because (H^1(Z_5^\times,F_5(1))=0). Its compact additive image is all Z_5. Integral divisibility and an integral coboundary change therefore give the entire affine image (5^d Z_5\rtimes Z_5^\times), rather than only a finite approximation. The zero local class gives the pure multiplier group.

An invariant class of functions has a translation defect that is additive. The actual pure multiplier two forces that defect to be zero. Unit orbits are exactly the valuation shells and the zero orbit. This proves all invariants, giving d independent ball functions when d is finite and a direct sum of countably many Q_5/Z_5's when d is infinite. The further local gauge translation lies in (5^r Z_5), so the global inclusion is exactly the first r ball functions. Thus the displayed quotient has the claimed full divisible structure.

The axis Cartier dual embeds equivariantly into the full dual. Its intersection with global invariants is exactly its own global invariants; hence the quotient injects into the actual local/global invariant quotient. D.63 identifies the latter's Pontryagin dual with the kernel of the local H² map to the global-invariant dual and supplies the continuous surjection from K_s. The finite local cohomology and injective discrete dual unions justify the limits. Divisibility of the injected direct sum makes it injective over Z_5, so dualizing a retraction supplies a continuous compact-module splitting. This does not split the nonseparated cohomology quotient.

The explicit local basis kappa(5), kappa(6), the convergent logarithmic coordinates, and their divisibility valuations are correct. The class kappa(101) has r=0,N=1. The exact two-prime cancellation kappa(2)−(log16/log81)kappa(3) has r=0,N=infinity and gives the claimed countably infinite compact free factor. These axis pairs are actual cusp pairs, so their section fibres are nonempty. The complementary compact factor and the general finite-derived obstruction remain open.

**Root certificate execution PASS:** the complete `code/de_compact_axis.py` program was independently rerun. All six finite affine-orbit computations, all defect determinants, the exact logarithm-ratio residue through 5^20, and the five prime examples passed. The finite calculations support the stated formulas; the continuous global duality and splitting are established by the written proof.

Both candidates subsequently passed independent full owner reviews before integration. A.61 received DE and PBC reviews, each with fresh primary-source checks and independent exact execution. D.75 received FGH and PBC reviews, including full exact certificate reruns. The canonical versions are `sections/A_heisenberg_inert.tex` and `sections/D_alexander_compact_factor.tex`.
