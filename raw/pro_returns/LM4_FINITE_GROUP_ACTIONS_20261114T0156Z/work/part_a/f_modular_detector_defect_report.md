# F.7 exact normalized detector and defect

Status: proved reduction; the parent centralizer claim remains Open.

The actual first orbit-twenty filling has p0(d^5)=x and p0(e^5)=y. These are the already specified full free basis. Therefore the pure normalized H action descends to x↦x and y↦W y W⁻¹, where W=p0(d⁻ʲ f⁻¹ eʲ) and j is the actual A5 quotient correction. The source word lies in H; the filling is applied only there.

Writing A=ell_x(W), B=ell_y(W), the unique normalized peripheral coordinate is y^B W⁻¹ x^A. Thus the exact detector kernel is the word equation W=x^A y^B. The exact comparison with the original normalized GT0 action is y^B W⁻¹ x^A=f. The latter equality is not proved for arbitrary f and is not inferred from the section property.

The staged text also supplies the two actual pre-filling defects on x and y, including the finite j correction. Replacing j by j+5m changes W to x⁻ᵐ W yᵐ and leaves the normalized coordinate unchanged.

The common section K→H is also a proper full profinite self-embedding K→K. Its two displayed word values have determinant-one abelianization and induce automorphisms of every free pro-p quotient. Their actual A5 images are trivial, while the original x,y generate A5. This explicitly identifies the finite quotient obstruction to full surjectivity; it neither replaces nor settles the separate detector equation.

## Executed certificate

`code/modular_detector_defect_f7.py` passed. It checks both based cusp images, eight common-section basis evaluations, both exact K-word substitutions, the S3 and A5 images, and the determinant-one matrix. On all 4,373 reduced free words of length at most seven it checks the normalization conjugacy identity, zero abelianization, and the kernel word equivalence. It also checks 30,611 finite-correction lift changes. These are exact word checks of the stated formulas and do not assert that finite inputs lift to GT0.

Files: `f_modular_detector_defect.tex`, `f_modular_detector_defect_results.json`, and the executable plus its adjacent JSON/stdout. The fragment is separate from the active F.7 source for root review and integration.
