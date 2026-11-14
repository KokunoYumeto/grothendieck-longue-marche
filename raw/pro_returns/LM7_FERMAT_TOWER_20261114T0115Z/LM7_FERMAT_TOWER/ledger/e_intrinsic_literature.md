# Primary literature checked for the intrinsic cubic section problem

This reading record belongs to the further work after E.35. It records exact uses and exact comparison maps, rather than claiming that a literature search proves the absence of any other theorem.

## Borne–Emsalem–Stix: a theorem that applies directly

Opened https://arxiv.org/pdf/1301.4429, version2, Definition2.3, Proposition3.5 and Theorem5.10, including the theorem's proof. The hypotheses are a smooth projective positive-genus curve over Q and a boundary that is a union of torsion sub-packets. A singleton rational cusp satisfies the definition. The theorem lifts every proper-curve section to the cuspidally central quotient. E.36 applies it to the actual full section of the proper elliptic curve obtained from a pro3 cocycle by giving it zero components at all other primes. Projection back to pro3 and the exact fiber product C times over T3E V evaluate every rank-ten abelian fiber in the cuspidally central quotient. This is the direct substantive application of the literature search.

## Saïdi: exact hypotheses and the relevant quotient maps

Opened https://arxiv.org/pdf/2109.14882, TheoremA and CorollaryB, printedp4. The result supplies non-geometric sections after finite extensions for specified quotients of proper hyperbolic curves over p-adic local fields with potentially good reduction. It does not state a parameterization of the section fibers for the specified open Fermat cubic over Q. The available field map is restriction G_Q -> G_Qp on section classes; producing local sections by that theorem does not produce a preimage under this restriction map.

Opened https://arxiv.org/pdf/1909.08318, Theorem1 in the introduction and its exact condition(H): H1(k,A) is finite for every finite G_k-module A. This condition fails for Q, since H1(Q,mu3)=Q*/Q*^3 contains the independent cube classes of every rational prime. It also fails for Q(zeta3) by the prime valuations in its Eisenstein ring. Its theorem addresses successive derived quotients of the cuspidal inertia kernel. For the present geometric group, let I=ker(N -> T3E). The exact inclusions N'' subset I' subset [N,I] give actual maps N/N'' -> N/I' -> N/[N,I], with kernels I'/N'' and [N,I]/I', respectively. Thus the cuspidal quotients are related to the requested metabelian group by these maps; their section-lifting fibers cannot be identified without treating the displayed kernels.

Opened https://arxiv.org/pdf/1010.1313, TheoremA and the preceding uniform-goodness definition. The theorem has a proper hyperbolic curve and a uniform condition on all section neighborhoods and finite base extensions. Proper finite etale covers of the compact cubic have genus1 by the unramified Riemann–Hurwitz formula, so passing to such a neighborhood does not turn this curve into the proper hyperbolic input. A ramified cover would instead require a lift through an additional open-curve fundamental group map. No such lift is inferred from the theorem.

## Wickelgren: exact path convention and actual higher obstructions

Opened the original author PDF https://sites.math.duke.edu/~kgw/papers/3NilP1.pdf, section12.2.1, equations(12.4)–(12.10), and the stated Theorem36. The path cocycle is p^-1 g(p), which E.37 uses to derive the negative conjugation term on a based peripheral loop. The explicit class-three calculations in that paper concern the three-punctured projective line, including local mod2 calculations; the actual comparison from the cubic is a map of geometric groups with its kernel, not an identification of the full rank-ten group with the target. The inherited map and the additional map h used in E.31 are both supplied elsewhere in the manuscript, including their origins. E.37 extends the class-two calculation by retaining all eight peripheral path classes and the entire exterior-square module.

Also opened the author's thesis https://sites.math.duke.edu/~kgw/papers/LCS.pdf. Section1.1.3 defines the lower-central obstruction maps in group cohomology for general pointed curves. Its definition alone leaves the arithmetic action and cohomology to be evaluated. E.37 supplies those computations, including the completed support condition and explicit Smith coordinates, for this cubic.

## Pairing convention audit

The opened Sutherland Lecture24, Corollary24.27, gives the tangent/divisor formula with its minus sign at n=3. The opened Silverman second-edition PDF has a reversed argument order in one translation definition. Enge's original 2015 article, https://ems.press/content/serial-article-files/44297?nt=1, section3 formula(7), its equivalence proof, and Remark9 explicitly explain this convention issue. It fixes the actual positive-frame lattice to U=(v,-u). The opposite exploratory coordinates are related by diag(I2,-I8); the official program checks this exact morphism and its exterior square.

## Result and remaining map

The search yielded E.36 and supplied the exact path and pairing comparisons used to complete E.37. E.37 computes the full intrinsic pro3 class-two image and every nonempty fiber. The further maps N/N'' -> N/gamma3N and N/gamma3(I_marked) -> N/gamma3N still have the displayed higher kernels. Their lifting problems are retained in the coverage ledger; no absence-of-results claim is made from this bounded source audit.
