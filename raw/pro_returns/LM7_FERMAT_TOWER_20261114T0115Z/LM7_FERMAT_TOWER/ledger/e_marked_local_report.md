# E.67 — marked-cusp local section classes

The theorem identifies the actual single marked-cusp quotient `W=Pi/gamma3(I_Q)` and its normal kernel as the completed free class-two group on the profinite space `B=Pi/I_Q`. The arithmetic tangent at Q fixes its peripheral generator by the q-power. Thus the kernel abelianization is the integral measure module on B and its center is the completed exterior square, with actions q times the actual Frobenius permutation and q squared times its exterior action.

The classification is complete on the explicitly specified locus whose inertia becomes trivial in B. Integral invariant measures force nontrivial inertia onto one conjugate of the marked cusp. A finite-coefficient weighted trace argument removes every central inertia correction even when the cusp exponent is divisible by three. The full centralizer is the direct product of the cusp group and the central exterior module. This leaves the exact additional Frobenius parameter C/(F_C-1)C, with its actual compact quotient topology. Zero first kernel coordinate forces inertia to be trivial; all those unramified classes have full lifts.

The full group maps onto exactly the zero central-parameter slice of this ramified locus. At the place above two, an actual nine-dimensional moment map has cokernel (Z/9)^5 times (Z/27)^2. The literal word `[d_B0,d_A0*d_B0*d_A0^-1]` maps nontrivially to this quotient, as detected by the explicit character e_A0*+e_A1*−e_B2* modulo three. Using this word as Frobenius correction gives a ramified marked-depth section with the single primitive B0 inertia ray, but no full lift.

## Computation

Fresh execution of `a_marked_local.py` passed. The certificate retains the actual quotient matrix, integral projection and section, both exact three-adic Smith transformations and their inverses, the finite detecting character, the literal commutator/tame relation, 3000 class-two identities, 1000 nonunit centralizer identities, 3000 moment identities and 144 exact weighted trace valuations. The integer Smith factors are 1,1,63,63,63,63,63,2079,2079; the three-primary factors give the asserted finite quotient.

## Exact remaining scope

This result does not evaluate the entire infinite central coinvariant module as a list of scalar factors, and it does not classify inertia with nontrivial image in B. Both source and target of the full-to-marked map on the stated locus are explicit. No tentative modular root or theta-path coefficient enters the proof. The unramified comparison and its actual full-to-quotient fibers are reserved for E.68.
