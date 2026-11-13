# D.29: a stabilized infinite class-two tower

**Proved progress; the full profinite CM question remains incomplete.**

The alternate CM pair from D.27 survives more than the first characteristic class-two quotient. The new finite groups are

`H^(k)=B/(gamma3(N)[N,N]^(2^k)N^(2^(k+1)))`,

with order `576*2^(4753k+97)`. For k=2 and3 the exact two-kernel orders are2^9603 and2^14356. The complete Z/4 and Z/8 Magnus calculations verify corrected cusp words of1,816,936 and4,448,112 letters. Their multipliers are1 and289, and generation follows from the retained rank97 map on N^ab/2.

The central coordinates are changed; the original D.27 homology masks, its right s-centralizer correction, and its G3 conjugators are retained. The original D.27 certificates remain separately available. The infinite lift fixes the H2 action obtained by reducing the Z/4 certificate, rather than claiming to fix every earlier H2 central representative.

## Exact stabilization

Between two successive exponent steps, the subgroup

`C_k=ker(H^(k+1) -> H^(k-1))`

is an abelian group `(Z/4)^4753`, with basis `a_i^(2^k)` and `[a_i,a_j]^(2^(k-1))`. It is a G2-module: N acts through N^ab/2. Its reduction modulo2 is the earlier Q-module. The exact cusp correction matrix, including the allowed multiplier variation, has mod2 rank4738, kernel dimension4769, and cokernel dimension15.

The second obstruction map from that kernel to the cokernel is computed by dividing the lifted cusp matrix by2. It has full rank15 both at the initial Z/4 step and at every stabilized step. Stabilization is proved by the power formula: normalized degree-two coordinates are `2W_i+(2^k-1)v_i v_i^T`, with diagonal normalization by the inverse of `2^k-1`. For k>=2 this factor is always3 modulo4. The remaining terms depend only on unchanged conjugator parities. The multiplier column is constant for the same reason.

Thus every target in twice C_k can be corrected. At stagek this correction fixes the action at levelk-1 and may change the central data at levelk. Every finite level stabilizes after the next step, giving a compatible inverse system of actual automorphisms. This proves an automorphism of the entire relative class-two pro2 completion. It is an exact infinite construction, not an extrapolation from the finite experiments.

## Other prime kernels and the mixed quotient

For every odd prime p, the prescribed beta image centralizes the order2 generator in Q and lifts to its centralizer over the full pro-p kernel by coprime conjugacy. Take A=1 and the identity action there. At3 retain the original prescribed G3 conjugator. Coprime kernel orders prove surjectivity onto the fibre product of the class-two pro2 quotient and all odd relative pro-p completions. The multiplier has its constructed two-adic component in1+16Z2 and equals1 at every odd prime.

D.28 separately verified a mixed-prime quotient J with the same homology parities and G3 data. Its exact common quotient with this system is C=H times_Q G3, so the actions combine on J times_C R. This adds a proved mixed-prime quotient to the infinite primewise system.

The remaining full profinite step is still substantial: the two-primary kernel has only class2, and many mixed finite quotients are not in the constructed system. D.22's all-finer-quotient test remains the exact criterion. No genuine GT0 realization of the missing CM coset is claimed.

## Reproduction

`code/d_cm_exponent4.py/.out/.json` retains all initial Z/4 correction coefficients and the direct word check. `code/d_cm_pro2_class2.py/.out/.json` retains the stabilized rank15 basis certificates, exact obstruction functionals, Z/8 coefficients and direct word check. The latter reruns the former and the earlier class-two verification chain. The same source formulas prove the characteristic quotient kernels and the infinite compatibility construction.

Independent audit: agent A freshly reran the stabilized code and checked its15/15 rank, full Z8 identity, exact two-level module, multiplier normalization, and inverse-limit compatibility proof. Nonarithmeticality is asserted for the finite characteristic refinements retaining the G6/CM data; a smaller quotient can forget that data.

Subsequent exact refinement D.30 rejects the specific central representative recorded here as a genuine full lift, jointly retaining its G6 data. It also constructs a further explicit central replacement with the same homology data that clears the new degree6 test and preserves an infinite compatible tower. The original quotient automorphism proved here remains valid; the old certificate is retained separately.
