# A210 exact one-place correction audit and execution scope

Source: sections/point3_dihedral_local_correction.tex. Certificate: code/point3_dihedral_1129_certificate.py with retained output/data, all PASS. The parent, Birational, and Local complete saved-source audits and independent certificate reruns have all passed. Local's final audited source SHA256 is ab2ae37a199eabca565670bfc314457e85951995aa74c6444b0d95989d425dcc.

The proof uses the SAME completed pair as A207, with no changed A65 modulus. In the fixed tangential gauge, class2 Ihara is pure cyclotomic, and the literal x^m y^n C^c Hall convention gives c=(Bm-An)/(q-1)-mn/2. Every fresh support exponent E=24n(q²-1)(q³-1) makes this even and gives trivial D8 inertia; zero valuations give c0. Aligning the actual global abelian mod2 cocycles with point3 makes the finite difference a quadratic character supported at2,3. All eight such classes split at1129.

The explicit degree8 cover t=((w4-1)/(w4+1))² has geometric D8 monodromy with exact kernel presentation x²=y4=(xy)²=1. Its local point3 fibre splits completely at1129. Above t828, the fourth-root values524,446 are squares but not fourth powers, so Frobenius is literally the central map w->-w on every sheet. This proves the one-place discrepancy, retaining every conjugator.

The local coefficient2 abelian classes agree fully because the unit power-completion at1129 has order8 and the global coordinates differ from3,-2 by24th powers. Thus the exact continuous central comparison lies in C16 and is odd. A40's global C24 generator restricts by k->53110k=6k mod16. The set of actual corrections over all24 global classes is consequently all8 odd residues, each3 times. This is an evaluated local obstruction, not an inference from the projected Selmer calculation in A209.

An earlier unused route was checked: A65 R4,N2 gives h4=8,D=24^9,B2=4,B3=B4=2,M1=C=2^91*3^28*7*13; A66 d3,J18 still has gcd(D0,1128)=24, with initial power-root residues15,16 for targets276,978. It would produce a different congruent-mod-Magnus example. The final proof needs neither that replacement nor its extra modulus.

Finite execution checks: exact symbolic Hall identities and D8 kernel/action;37,485 sample tame parities; all supported quadratic square witnesses; literal cover function/deck/derivative identities; complete1129 fibres; and the correction image. General inertia and cohomology assertions are proved in the source. No external computation or giant prime-recursion stage was executed.
