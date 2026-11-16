# Independent audit of A201

Auditor: local_preprint. Result: PASS.

Audited source: `sections/selmer_class_two_to_three.tex`.
Independent execution: `python work/code/selmer_class_two_to_three_certificate.py`, exit 0; all three symbolic cusp corrections and the uniform denominator-six estimate passed.

## Exact maps checked

The geometric maps are the characteristic pro-prime and lower-central quotient maps of the original tripod group. The rank-two central kernel has the literal Hall basis `[[x,y],x]`, `[[x,y],y]` and cyclotomic weight three. The continuous Hall set section has the same tangential arithmetic splitting as the quotient section. Its raw defect is therefore the actual obstruction, with the cochain comparison of A43 retained.

At a physical prime different from the coefficient prime, the unit-tangent pointed action is unramified. The A49 normalization, Kummer-coordinate and arithmetic-extension comparison applies to each of the three punctured residue discs. An ordinary good-reduction section has identity inertia. Every other admitted local section has inertia conjugate to a power of the specified cusp meridian. This includes an actual cusp section with a completed tangent parameter. Lifting a local geometric conjugator aligns the class-three local section literally with the given class-two representative. Its inertia exponent is a signed coordinate of the global abelian Kummer inertia, and consequently tends to zero outside finite sets.

The symbolic certificate uses the same commutator and collecting conventions as A43. Its extracted central coordinates agree exactly with A201.10 and A201.11. Each coordinate multiplied by six and divided by the inertia exponent is an integral polynomial. Integer-power word identities extend continuously to all pro-prime exponents. This proves the uniform valuation bound even at coefficient primes two and three; the central part of the conjugating element cancels.

Writing each aligned local lift as a central cochain times the Hall lift gives `d z_q = -R`. On tame inertia its value is precisely the certified correction. The strict residue identity therefore gives `psi_q(R)=-(q^2-1)z_q(T_q)` with the displayed sign. The correction family tends to zero, so the full raw-defect residue belongs to the literal image in the denominator of A46.2. No closure or finite-coefficient replacement is used. The A46 real-place calculation covers coefficient two.

Finally, finite nilpotent quotients decompose into their Sylow subgroups. The compatible inverse maps identify the geometric class-three quotient with the product of its pro-prime factors. The product of the continuous central primitives is continuous and gives the required global section. Lifting a geometric conjugator shows that the result is well-defined on the stated section classes.

## Scope

The domain is exactly the set of class-two sections that locally match actual ordinary or cusp sections at every finite prime. The result supplies a global class-three lift of the specified class-two section. It makes no claim that this lift matches the selected local full sections. No finite-support hypothesis is introduced, and the argument proves vanishing of the actual continuous classes including their derived-limit components.

