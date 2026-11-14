# D5: a discontinuous action with empty fixed set

| Demand | Outcome | Statements |
|---|---|---|
| Every abstract semilinear action has exactly one cyclotomic-kernel fixed completed geometric closed pro-point | Refuted: the fixed set can be empty, even for an action normalizing the original deck group | D.12--D.14 |
| Construct or rule out an action normalizing no deck group of a finite hyperbolic quotient | Proved existence, with exactly one fixed cusp | D.10--D.11 |

The root agent proposed the ultralimit and its CRT strengthening. The Part F agent independently checked the finite-quotient local convergence, geometric conjugator issue, local Kummer argument, completed-point convention, and discontinuity proof, and wrote `sections/D_ultralimit_extension.tex`. Root then independently accepted the complete written D.12--D.14 proof. The corresponding three rows are in `audit/D_ultralimit_results.json`. Under root's express direction, the extension is now input in D.tex before the unresolved D1--D4 obligations, and the former D.U5 statement is removed as superseded.

The R22 crossed cocycle is explicitly supplied: fix the continuous point action rho_0 at 1/2 and set a_g=s(g)rho_0(g)^(-1)=lim s_n(g)rho_0(g)^(-1). It belongs to Pi, satisfies a_(gh)=a_g rho_0(g)a_h rho_0(g)^(-1), and its twisted action is s(g). D.14 computes the fixed set of this cocycle as empty.

## Construction and the point where continuity fails

The explicit local point is a=1+sum 3^(r!) in Q_3. Its integer partial sums have errors of 3-adic valuation (N+1)! and real size at most 2*3^(N!), giving a direct elementary proof of transcendence over Q by evaluating a putative integer polynomial.

Choose rational integers x_n converging 3-adically to a, with fresh primes q_n such that v_qi(x_j)=delta_ij. The full CRT construction is effective: x_n has the prescribed residue modulo 3^n, valuation exactly one at q_n, and residue one modulo every earlier q_i; choose q_n dividing no earlier x_j. Each x_n is at least two and belongs to the open tripod. Continuous global point sections s_n exist.

A nonprincipal ultrafilter gives s(g)=lim s_n(g) in the compact profinite arithmetic fundamental group, for every g. The homomorphism law and section identity survive this pointwise limit. A nonprincipal ultrafilter is a choice-principle ingredient; the proof does not claim an algorithm for evaluating the resulting abstract section.

The independent square classes give a continuous surjection kappa:G_Q -> product F_2. The cover z^2=t detects the character epsilon composed with kappa, where epsilon is the ultrafilter functional. It kills the dense direct sum but sends the all-one sequence to one, so it is discontinuous. Since kappa is a quotient map of compact groups, the composite is discontinuous. Thus the section and its semilinear action are provably discontinuous, without using the section conjecture to infer discontinuity.

## Local compatibility in the full nonabelian group

For each finite arithmetic quotient F of the fundamental group, write P for the image of the geometric group. The corresponding finite étale F-torsor has a constant quotient by P. Hensel gives a common small 3-adic ball on which its fibres are Galois-equivariantly and F-equivariantly identified, preserving the constant quotient. This last condition places every conjugator in P, which is essential: arbitrary arithmetic conjugacy would not suffice.

The P-conjugacy orbit of the local point section at a is finite and hence closed in the product F^(G_Q3). The ultralimit still belongs to this orbit. For all finite arithmetic quotients simultaneously, closed sets of geometric conjugators have the finite-intersection property; compactness of the full geometric deck group supplies one conjugator. Therefore s restricted to G_Q3 is geometrically conjugate, in the full profinite arithmetic group, to the continuous local point section at a.

## Why a cyclotomic fixed pro-point is impossible

Suppose a completed geometric closed pro-point were fixed. Its base coordinate x is algebraic over Q. Choose a finite local extension L/Q_3 containing x, and put H=G_L intersect ker(full cyclotomic character). After the preceding geometric conjugation, the local point section s_a fixes the corresponding pro-point on H.

Choose a unit f of the tripod regular and nonzero at x: f=t in the interior and at cusp1, f=1-t at cusp0, and f=t/(t-1) at infinity. The covers w^(3^n)=f(t) extend étale across x, so the fixed pro-point forces the Kummer class of f(a)/f(x) to vanish on H. This includes all cusp cases and uses no continuity of the global abstract section.

The local lemma is proved directly. A continuous Z_p(1)-cocycle vanishing in cohomology on H literally vanishes there because H acts trivially. It descends continuously to the compact abelian cyclotomic image A. Commuting any a in A with an a_0 having chi_p(a_0) different from one shows that chi_p(a_0)-1 kills its cohomology class. The class is therefore p-power torsion. For a finite local field, the intersection of all p^n-th-power subgroups of L* is exactly its prime-to-p roots of unity: valuation removes the uniformizer component, and the separated pro-p principal-unit filtration removes the remaining component. Hence the original ratio is a root of unity. This makes f(a), and therefore a, algebraic over Q, a contradiction.

Only the existence part of the universal unique-fixed-point assertion is refuted. The example does not exhibit two fixed points. The generic scheme point is not included: the manuscript's completed-point convention here is the compatible system of geometric closed points on proper finite levels, as explicitly fixed in D.7.

## Verification and sources

- `code/F_D5_ultralimit_checks.py` computes twelve exact CRT points and verifies all local congruences and the complete 12 by 12 identity valuation matrix. The first points are 10, 301, 25663, 629707. The result is saved in `code/F_D5_ultralimit_output.json`. These finite checks concern only the explicit arithmetic input; the full ultralimit and fixed-set claims are proved above and in the paper.
- SGA1's supplied complete source, Exposé IX section6, supplies the arithmetic finite-cover correspondence and the constant quotient. The local uniformity is proved explicitly by the finite collection of Hensel sheets, retaining both deck equivariance and the constant quotient.
- Stix's supplied actual source, *On cuspidal sections of algebraic fundamental groups*, section2.2 and sections8.1--8.3, especially Proposition26 and the section-value definition, was opened locally and checked against the primary arXiv PDF https://arxiv.org/pdf/0809.0017. It supplies the Kummer evaluation interpretation. The commuting-cocycle identity and local-unit kernel calculation are proved in D.13 rather than attributed to an unverified statement.
- No local section-surjectivity theorem, adelic finiteness assertion, or unrefereed R24 claim is used. D1--D4 remain their separate continuous questions.
