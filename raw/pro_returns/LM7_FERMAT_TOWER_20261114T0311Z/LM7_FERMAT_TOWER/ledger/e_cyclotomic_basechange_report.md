# E.76: certified cyclotomic base change

The actual base change is (B_d=L_d(\zeta_9)), where

\[
L_d=\mathbb Q(\zeta_3,\beta_d),\qquad
\beta_d^{3^d}=17\zeta_3,\qquad\beta_{d+1}^3=\beta_d.
\]

The new computation concerns (B_1=\mathbb Q(\zeta_9,\sqrt[3]{17})).
This is a different degree-eighteen field from (L_2), the field involved
in the two original long BNF jobs. Those jobs remain running; their exact
commands, session IDs and last observed status are retained separately.
No duplicate of either original job was launched.

## Exact results

The full class group of (B_1) is (C_3^2), certified by PARI's
unconditional `bnfcertify=1`. The eight fundamental units, the order-nine
root of unity, an integral basis and both class-generator ideals are
retained literally. All three primes above3 have class `(1,0)` and all
three above17 have class `(2,0)`. Thus these six classes generate only one
of the two certified cyclic factors. The second generator is an actual
prime of norm109.

Each (B_d/L_d) is unramified cyclic cubic and splits the original primes
above3 and17 completely. The norm of each one of the three upper primes
above3 is exactly the original prime, with residue degree one. The
adjacent (B)-tower steps are totally ramified at all six primes, and
each two-step extension is cyclic of degree nine. These statements are
proved from the actual roots and local completions.

The six local unit norm characters are evaluated on the entire certified
global unit basis. The resulting indices, ambiguous groups and genus
quotients are:

| Extension over (B_1) | Global unit norm index | Ambiguous class-group order | Genus Galois group over (B_1) |
|---|---:|---:|---|
| (B_2/B_1), degree3 | 27 | 81 | (C_9\oplus C_3^3) |
| (B_3/B_1), degree9 | 2187 | 243 | (C_9^3\oplus C_3) |

The local characters use explicitly listed generators of the actual
local norm quotient. Their generators are not silently identified with
a common Hilbert-symbol root. The separate Kummer character needed for
the cyclic degree-nine field is normalized by the fixed global root
\(\xi=\zeta_9\): arithmetic Frobenius at a prime \(\mathfrak l\)
sends the ninth root by the factor
\(\overline{\beta_1}^{(N\mathfrak l-1)/9}=\overline\xi^e\).
All48 prime factors used in that calculation are retained and checked.

Every prime above3 has image of exact order3 in both computed genus
quotients. The actual automorphism fixing \(\beta_1\) and sending
\(\xi\) to \(\xi^4\) gives a further explicit descent. Its coinvariants
on the relative unramified kernel are (C_3^2), and the prime images are
all `(2,0)`. The proof identifies this group with a subgroup of an
unramified abelian quotient over the original (L_3). Consequently this
is a literal order-three quotient of the original prime class.

## What remains unevaluated

The exact norm and extension maps are displayed in the theorem. Growth
of the ambiguous groups does not determine the order of the particular
prime in the kernels of the genus maps. At the original third level the
proved full order still lies in `{3,9}`. The eventual integer (h), and
the higher principal-class matrices of E.72, remain unevaluated.

The first class-group equality required for the opened stationary
theorem fails: the base three-class group has order9, while the next
one has order at least81. The actual norm map is surjective, so its
kernel has order at least9. No later equality is supplied by this
calculation. A next exact target is a norm-coherent3-unit sequence with
base value \(\lambda^3\), retaining the unit-norm/class obstruction at
each transition.

## Verification and reproduction

Run the matrix and determinant checks against the retained arithmetic
output with:

```sh
python code/e_cyclotomic_basechange.py
```

Rebuild all eight arithmetic stages, including the complete field and
unit certification, in an isolated temporary working directory with:

```sh
python code/e_cyclotomic_basechange.py --gp /absolute/path/to/pari-2.19.0/gp
```

The driver saves the actual combined stdout/stderr of each stage next
to its source. It verifies50 multiplication-determinant norms, six
complete local norm kernels,12 full integral Smith transformations
and inverses, the actual Kummer character, the ray-basis inverse, the
genus restriction map, and both levels of cyclotomic descent. The
finite local precision bounds are proved: at the wild places
\(U_{10}=U_4^3\) and \(U_{16}=U_4^9\).

The first failed `bnrgaloismatrix` invocation used a polynomial-modulus
object where the documented input is a polynomial. Its source/output
is retained. A second attempt deliberately checked that implicit and
explicit ray generators were the same; that check failed. The final
program computes and verifies the actual change of basis modulo the
cyclic relations. Two driver implementation failures, involving
polynomial domains and a completion-marker check, are also retained
with their exact Python source and actual exception output.

The `norm_index_attempts` folder preserves the earlier ideal-reduction,
unit-collision and capitulation searches, including their actual
outputs and saved arithmetic data. None of their unsuccessful searches
is used to assert nonprincipality or a complete unit image.

## Sources and audit

The original published Li--Ouyang--Xu--Zhang paper was opened through
its journal page, including the complete stability proof and the local
norm kernel lemma. Milne's precise local reciprocity, global Artin and
Hasse norm passages were reopened. The proof also derives the two
ambiguous orders directly from the idelic ray quotient and the
commutator subgroup of the Hilbert class field extension.

Independent A full proof and fresh copied-verifier audit passed; every
JSON field matched without exclusions. The audit is retained at
`a_e76_audit/audit.md`. Parent root full GP pipeline audit is pending.
Exact source passages and current audit states are recorded in the
source-evidence JSON.
