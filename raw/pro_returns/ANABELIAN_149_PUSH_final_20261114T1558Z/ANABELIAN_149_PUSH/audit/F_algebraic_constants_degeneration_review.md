# Independent review of F.45: algebraic constants and positive transcendence

Reviewer: degeneration agent. Date: 14 November 2026.

Reviewed candidate: audit/F_algebraic_constants_function_fields_candidate.md, Sections 1–9. This review is separate from the F.44 formation-closure review.

**Conclusion: the full written argument passes in its stated positive-transcendence scope.** The moved-divisor, direct valuation, Albanese, and point-function steps retain their exact hypotheses. In particular, Section 6's use of a high-degree point is justified and does not confuse being nonconstant over the function field with being nonalgebraic over \(\mathbf Q\). The algebraic subfield \(\overline{\mathbf Q}\) remains excluded.

## 1. Field predicates and arithmetic detection

For every finite extension of a finitely generated \(L/\overline{\mathbf Q}\), the constants are still \(\overline{\mathbf Q}\), and the extension still has positive transcendence degree. The normal proper model proves that the intersection of all power subgroups is precisely \(\overline{\mathbf Q}^{\times}\). All divisorial values are integers; divisibility by every \(n\) forces them to vanish. Properness and normality then force the function to be a constant.

The Hilbertian input gives exactly the stronger finite-quotient detection needed in the proof. A specialization of the **whole** connected composite cover \(Y\to\mathbf P^1\) to one field makes the intermediate degree-\(n\) fibre on the original curve one degree-\(n\) closed point, and makes its residual \(G\)-torsor connected. This detects the complete arithmetic group \(G\), including any constant factor. No geometric-connectedness hypothesis is silently imposed on the finite cover.

Finite data descend to \(F/\mathbf Q\) with \(L=F\overline{\mathbf Q}\), so \(G_L\) is normal in \(G_F\). Finite extension stability is explicit throughout. Ordinary constant points of a constant variety alone would not detect the required quotients, but the proof uses points over finite extensions of the function field, which are enough by Hilbert irreducibility.

## 2. Moved geometric divisors

A nonidentity finite-order \(C\)-automorphism of the regular function field \(M/C\) admits the indicated equivariant normal model. The smooth locus and the complements of finitely many zeros and poles give a nonempty stable open. Its fixed locus is proper because the automorphism is not the identity on the function field.

The affine function construction is sufficient; Bertini is unnecessary. At a point \(z\ne\sigma z\), the value at \(\sigma z\) and a nonzero linear term at \(z\) can be prescribed by CRT in the two distinct maximal ideals. The zero divisor is smooth at \(z\), hence has a unique prime component there, with multiplicity one. If that component were \(\sigma\)-stable, it would contain \(\sigma z\), contradicting the prescribed nonzero value of the function.

Removing the full finite orbits of all previous prime divisors ensures that every selected pair is distinct from every earlier pair. Passing to one finite normal constant extension preserves the distinctions: components lying over different original prime divisors cannot coincide. The components through the chosen rational smooth points remain discrete prime divisors. A component that is geometrically defined can be descended after a finite constant extension; uniqueness at the rational smooth point gives the same conclusion.

The semilocal CRT formulation is correct. Localizing the normal affine ring away from the union of the finitely many height-one primes leaves precisely their DVRs as nonzero local rings. The selected primes become distinct maximal ideals, so CRT applies. This avoids the false claim that arbitrary height-one ideals were already comaximal in the higher-dimensional coordinate ring.

## 3. The direct integer-valued prolongation

The DVR at a geometric prime divisor contains the number-field constant field and is trivial on it. For every finite constant extension \(C''/C'\),
\[
\mathcal O_v\otimes_{C'}C''
\]
is finite étale over \(\mathcal O_v\). Every localized prolongation is therefore an unramified DVR of ramification index one. A coherent prolongation through the directed union of all finite constant extensions has value group exactly \(\mathbf Z\), since each of its elements already lies in a finite constant extension. It does not acquire the divisible value group \(\mathbf Q\).

This validates the simplified Kummer argument. At level \(n\), the evaluated relation is an equality modulo \(n\)-th powers in the one field \(M\overline{\mathbf Q}\). Taking the fixed integer-valued prolongation gives
\[
v_i(\sigma b_\alpha/b_\alpha)+\lambda_i\equiv0\pmod n
\]
for every \(n\). The valuation is an ordinary integer independent of \(n\), so \(\lambda_i\) is that ordinary integer in \(\widehat{\mathbf Z}\). No norm field depending on the radical level, averaging, or interchange of infinite limits is used.

The automorphism need not preserve the chosen valuation. It is used to construct the pair of distinct valuations and the vector \(v_i(R_j)=-\delta_{ij}\). The final valuation is applied to the single element \(\sigma b_\alpha/b_\alpha\).

The nontrivial geometric automorphism exists as written: choose a missing finite extension of the Hilbertian \(L\), descend it, and take a finite normal \(M\) containing its roots. An automorphism of \(M\overline{\mathbf Q}/L\) fixes the constants, preserves \(M\), and cannot restrict trivially to \(M\), since \(M\) and the constants generate the compositum.

## 4. Albanese span and equivariance

The exact comparison is integral, and the finite kernel disappears under Hom into a torsion-free target. The normalized arithmetic class is a homomorphism because the cyclotomic action is trivial on \(G_L\). It vanishes on the rational basepoint section.

If projected point Kummer images failed to span \(W=(V_\ell A)_{G_L}\), a nonzero integral functional annihilating them could be reduced at a nonzero finite level. Its corresponding finite arithmetic quotient would then vanish on every point decomposition image, contradicting the preceding detection theorem. This argument includes constant abelian varieties: the needed points need not descend to the constant field.

The finitely many spanning point images and their actual values descend to one finitely generated field \(M/\mathbf Q\). Restriction to \(G_{M\overline{\mathbf Q}}\) has finite index in the relevant point groups and preserves their rational spans. The conjugation correction in a point Kummer cocycle is killed in the \(G_L\)-coinvariants. The actual scalar Kummer cocycle transforms by the cyclotomic character, since its value is defined over \(M\). Thus the normalized functional is \(G_M\)-equivariant on the spanning images, then on all of \(W\), and hence on the original Tate module.

Jannsen's theorem is applied over the finitely generated \(M\), not over \(L\) or \(\overline{\mathbf Q}\). Splitting boundary components and fixing the basepoint gives a single unit lattice: a unit with the given divisor and normalized value is unique, so its conjugates agree. The later integral residue calculations and the injective divisor matrix therefore use one common basis. The Picard–Tate contribution is removed only for the particular point-theoretic class.

## 5. Detailed review of Section 6

### 5.1. Why a high-degree point has nonalgebraic unit value

For a nonconstant rational function \(h\) on a smooth proper curve, the map to \(\mathbf P^1_L\) is finite of degree \(d_h\). If \(h(x)\in L\), then \(x\) lies in a fibre of total degree \(d_h\), so
\[
[\kappa(x):L]\le d_h.
\]
Consequently a closed point of degree \(>d_h\) has \(h(x)\notin L\), and therefore \(h(x)\notin\overline{\mathbf Q}\), because \(\overline{\mathbf Q}\subset L\). This is the exact argument needed; it is stronger than merely observing that \(h\) is nonconstant.

Every nonempty inverse-image open is again an open curve over the same Hilbertian field, so it has detecting points of arbitrarily large degree. The degree can simultaneously exceed \(d_h\) and any specified sum of pole degrees.

### 5.2. The affine relation obtained on the inverse-image open

The inverse image of \(T\ne1\) is a Zariski open, since opens are subobjects of the terminal object in the étale topos. It is nonempty: if the point function were identically one, \(\phi(x)=c_xh(x)\) would put every \(h(x)\) in the constant field, contradicting the high-degree point just discussed.

On this open, the recovered unit \(h_1\) represents the class of \(\phi-1\). At a point \(x\) of degree larger than the sum of the pole degrees of \(h\) and \(h_1\),
\[
c_xh-d_xh_1-1
\]
vanishes, with \(c_x,d_x\in\overline{\mathbf Q}^{\times}\subset L^\times\). Unless identically zero, this rational function has zero divisor degree at most that sum. The high degree therefore forces the identity
\[
h_1=Ah+B,\qquad A,B\in\overline{\mathbf Q}^{\times}.
\]
Both coefficients are nonzero because \(c_x,d_x\ne0\).

At any point with \(h(x)\notin\overline{\mathbf Q}\), the same value identity gives
\[
(c_x-d_xA)h(x)=1+d_xB.
\]
Its coefficients lie in the algebraically closed constant field. Hence both coefficients vanish, giving \(d_x=-1/B\) and \(c_x=-A/B=c\). Such a point automatically lies in the open, since \(\phi(x)=1\) would force \(h(x)=1/c_x\) to be algebraic.

For each \(b\in\overline{\mathbf Q}^{\times}\), the same reasoning on the open where \(\phi\ne b\), at a point of sufficiently high degree, gives
\[
h_b=e_b(ch-b).
\]
This open is nonempty because the original function is not constant. If \(h(x)\) is algebraic, take \(b=ch(x)\). Were \(\phi(x)\ne b\), the point would lie in that open but its regular unit \(h_b\) would vanish. Therefore the equality \(\phi=ch\) also holds at the algebraic-value points. The original normalization fixes \(c=1\).

### 5.3. The constant case

If \(h\in L^\times\) is constant, choose \(\beta\in L\) with \(\beta/h\notin\overline{\mathbf Q}\). This uses exactly the positive-transcendence hypothesis.

Every value \(\phi(x)=c_xh\) lies in \(L\) and differs from \(\beta\). The inverse image of \(\beta\) is closed. A nonempty closed subset of the finite-type curve has a closed point, so this inverse image is empty. Hence \(T-\beta\) pulls back on the whole curve.

The resulting unit \(h_\beta\) has all its closed-point values in \(L\), because its actual values differ from \(\phi(x)-\beta\in L\) by algebraic constants. If \(h_\beta\) were nonconstant, a point of degree greater than its degree would contradict this. Thus \(h_\beta\) is constant; normalization makes it \(h-\beta\).

Now both
\[
\phi(x)/h,\qquad
(\phi(x)-\beta)/(h-\beta)
\]
belong to \(\overline{\mathbf Q}\). Since \(\beta/h\) is transcendental over that field, comparing the coefficients of \(1\) and \(\beta/h\) forces both ratios to be one. Therefore \(\phi(x)=h\) at every point.

No missing number field is used in this case. The separating element belongs to the positive-dimensional function field itself.

### 5.4. Higher-dimensional sources

After a finite extension, a chosen geometric closed point and the rational basepoint lie on a smooth geometrically connected curve. The recovered curve unit and the restriction of the global unit have the same Kummer class. Their quotient is divisible at every level, so its divisor on the proper completion is zero; its value at the basepoint is one. Thus the quotient is one. This passes the curve point-function result to the original source without asserting that all its points lie on one fixed curve.

## 6. Subfield descent and strictness

For \(k_0\subset L\) of positive transcendence degree, the compositum \(K=k_0\overline{\mathbf Q}\) is finitely generated over \(\overline{\mathbf Q}\). Choose a finite transcendence basis \(B\) in \(K\); then \(K\) lies in the finite relative algebraic closure of \(\overline{\mathbf Q}(B)\) inside \(L\). Thus \(K/\overline{\mathbf Q}(B)\) is finite. The extension \(K/k_0\) is algebraic, so F.32 applies. It is essential that \(K\) still has positive transcendence degree; this is why the theorem does not descend to the algebraic constant subfield.

Finally, if \(\overline{\mathbf Q}(t)\) had the virtual proper-formation description in F.44, its normal closure over a finite Q-descent would have a quotient equal to the absolute Galois group of a number field. An open pro-\(\mathcal C\) subgroup would descend to an open subgroup of that number-field group, but such a subgroup has arbitrarily large symmetric-group quotients. This contradicts the exclusion of all sufficiently large alternating groups from a proper hereditary \(\mathcal C\). The stated strictness is valid.

No invisible-field-automorphism counterexample was found. The coincidence of constant-point fundamental-group sections on a constant curve is not such a counterexample: full pinned étale-topos maps still retain their distinct support points, and the proof explicitly uses nonconstant finite-extension points to recover the missing Kummer span.

