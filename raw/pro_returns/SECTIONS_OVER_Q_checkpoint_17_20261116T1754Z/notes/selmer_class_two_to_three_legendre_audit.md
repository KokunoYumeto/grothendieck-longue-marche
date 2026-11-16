# A.201 independent source and execution audit

Result: PASS, complete saved-source mathematical audit and independent certificate execution.

Source read: `sections/selmer_class_two_to_three.tex`.

The exact certificate was copied to `/tmp/a201_legendre_b7bv5oxy` and executed there, leaving the parent's retained data unchanged. All three cusp word identities and the uniform denominator-six assertions pass.

## Exact maps checked

1. The actual class-three extension has central kernel `Z_l(3)^2`, with the Hall lift `L(a,b,h)=y^b x^a C^h` and the same tangential splitting as A.43. The raw defect is exactly `L(n(g)) gL(n(h)) L(n(gh))^-1`, so an aligned local section has `dz=-R` with the stated sign.
2. At `q != l`, good reduction of the pointed tripod makes the background inertia action trivial. The already proved A.49 punctured formal-disc maps identify annular point inertia with the corresponding literal parameter's tame Kummer character. Genuine cusp tangent classes give the same map directly. Integral interior points have trivial inertia. A lifted geometric conjugator aligns a full local point/cusp lift with the prescribed class-two representative without changing this conjugacy form.
3. Thus inertia is `u c^m u^-1` for `c=x,y,(xy)^-1`, or the identity. Its abelian coordinates are `(m,0)`, `(0,m)`, `(-m,-m)`, or `(0,0)`. Every finite reduction of the global abelian cocycle factors through a finite Galois extension, so the selected `m_q` tend to zero cofinally. This includes completed cusp valuations and does not require finite support of the complete class.
4. The certificate uses the same commutator convention as A.43 and verifies all six exact central correction polynomials. The central coordinates of the conjugating element cancel. Multiplication by six and division by `m` leaves integral polynomial coefficients, giving `v_l(F_c(u,m)) >= v_l(m)-v_l(6)` uniformly in all integral Hall coordinates. Integral word identities and density extend the formulas to continuous pro-l powers, including at two and three.

## Strict residue and convergence

For a normalized central cochain `z`, the first three terms of the displayed strict residue of `dz` telescope to `q^3 z(T)-z(T^q)`. The inertia sum telescopes to `q z(T)-z(T^q)`. Division by the actual unit `q` gives exactly `(q^2-1)z(T)`.

The aligned local lift therefore gives the literal representative `psi_q(R)=-(q^2-1)z_q(T)`. The Hall estimate and `m_q -> 0` imply `(-z_q(T))_q` belongs to the actual restricted product `R_l^0`. Consequently the residue family belongs to the literal image `d_3 R_l^0`, not merely its closure or the product of individual local images.

I reread the complete A.46 proof. Its actual continuous localization isomorphism has precisely this denominator and includes the coefficient-power derived-limit term. The unramified group is zero, and the real degree-three cohomology injectivity supplies the dyadic surjectivity. Thus the conclusion kills the entire continuous obstruction, with no omitted real or inverse-limit term.

Finally every finite class-three nilpotent quotient is the direct product of its Sylow subgroups. The characteristic inverse-limit maps therefore yield the full geometric product of pro-l quotients, with the actual Galois action preserving the factors. Coordinatewise continuous primitives combine to a continuous full profinite primitive. Lifting a geometric conjugator handles the stated section classes.

## Scope preserved

The domain explicitly consists of class-two sections locally arising from actual full point or cusp sections at every finite place. The conclusion is a global continuous class-three lift of that specified section. It does not assert that the new lift preserves the local point/cusp images. Arbitrary ordinary completed Kummer pairs are not silently identified with that locally matching class-two domain.
