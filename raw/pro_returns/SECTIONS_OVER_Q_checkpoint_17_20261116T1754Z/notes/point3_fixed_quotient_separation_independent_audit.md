# Independent audit of A202

Auditor: local_preprint. Result: PASS.

Source: `sections/point3_fixed_quotient_metabelian_separation.tex`.
Independently executed `python work/code/point3_fixed_quotient_separation_certificate.py`: PASS, including 768 first-prime depth cases, 9216 later precision/product cases, and 2432 all-sheet detector cases.

The full intersection and recursion in A72 were reread. Its maximal abelian field is exactly the specified cyclotomic field. Enlarging the auxiliary dyadic modulus leaves the required intersection unchanged. The new first residue class remains one modulo the original exponent because the chosen dyadic depth is at least the valuation of the next exponent. Thus the actual Chebotarev fibre-product element exists. All later local precision increases retain the original analytic branch and its distinguished geometric component.

At every controlled dyadic stage the new point has first Kummer coordinate exactly one, by the actual transition and the Hensel construction following A72.18. The ordinary local centre is consequently the limit of the first coefficients. The first multiplier gives valuation exactly E in the difference from three; every later multiplier is one modulo 2^(E+1). The original increasing precisions prove convergence and retain the exact depth.

The cyclic-eight cover and genus-two maps are literal. Every dyadic sheet has a unit x-coordinate congruent to three modulo eight. The displayed factorization proves v2(t-3)=v2(x-3)+3 on every sheet; the two rational deck elements keep x fixed and negate y. At n=E-2 the exact finite Selmer criterion from A193 fails. The order and nilpotency class follow by substitution into its actual finite group.

The final metabelian comparison uses the full local Kummer injection, excludes all three cusp packets by the displayed classes, and projects through the explicitly metabelian finite quotient. The global class-two lift is separately supplied by A38. The source does not assert a simultaneous locally matching lift retaining the arbitrary initial finite quotient and class-two section.

