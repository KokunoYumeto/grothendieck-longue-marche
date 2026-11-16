# A208 complete independent audit

Reviewer: local_preprint. Date: 2026-11-16. Result: **PASS**.

Reviewed source: `sections/two_inert_secondary_divisor_comparison.tex`.
Exact source and certificate hashes are retained in
`code/two_inert_secondary_divisor_independent_audit_record.json`.
The final source removes only the extraneous comma in the exponent of
(A.208.15). The independent rerun writes were redirected to a temporary
directory; author output was not used as the test result.

## Actual support-class map

The residue-weighted divisor norm kernel for the cyclic extension M/E2 is
the image of h-1 on the integral divisor lattice. Split orbits have
coefficient sum zero; a nonsplit orbit has one coefficient killed by a
positive residue degree, hence that coefficient is zero. Hilbert 90 gives
the precise change of primitive, so the image in A^h/<c3> is well-defined.
Invariant ideal classes are represented by actual divisors; their h-1
differences are principal. This gives surjectivity. The principalization
of a prime-to-three multiple, followed by the displayed Bezout combination
with the scalar norm, gives injectivity before completion.

A206 identifies the whole kernel of ideal norm with <c3>. The actual
ideal-norm map consequently embeds A^h/<c3> into A2. Equivariance for tau
and A203's two-dimensional anti-unit quotient identify the image with
A2-minus. Passage to completions retains this exact finite quotient.

## Principalization and secondary character

The field/action comparisons use gamma(rho3)=z rho3, gamma restricted to
M equal to sigma, s=gamma^3, h gamma h^-1=gamma^4, and tau gamma tau=gamma^-1.
These are distinct from the A199 automorphism t -> zt. For every actual
anti-unit a the literal relative unit v=sigma^2(a)/sigma(a) is pure and
has norm one. A184 supplies actual unit preimages b and their
preimage-independent secondary character.

The gamma-invariant divisor of its Hilbert-90 primitive descends to an
actual sigma-invariant divisor J of M: at every ramified prime the lower
ramification in M/F' makes the required coefficient divisible by three.
The exact equality 3J=div(f) is retained. Strong sigma-ambiguity puts its
three-class in <c3>; the upper changed-prime classes vanish through their
actual inert extension maps. No inertness assertion is used for the
degree-six two-primes.

The equality a0=gamma(w)tau(w) in F', with a0^3=f tau(f), proves
J+tau(J)=div(a0). Hence [J] is simultaneously in the tau-plus c3 line and
tau-minus. It vanishes in the ordinary class group because 3J is already
principal. Thus x with div(x)=J and u=w/x are actual elements, with u an
actual unit. The factorization of b preserves its prescribed norm exactly.

At a changed prime, pi_M=t^2/q has sigma(pi_M)/pi_M=zeta^2. Gamma acts
trivially on the residue of u. Therefore the residue of b is zeta^(2k),
k=v(x). Evaluating in the pure residue field F_(q^2), and retaining its
inclusion in F_(q^6), gives exactly psi2(v)_q=2k modulo three in A184's
normalization. The exponents (q^2-1)/3 are 1 and 2 modulo three at 11 and
59. Evaluating the cubic character in F_(q^6) would erase this value and
is not the map used in this assertion.

## Complete next norm matrix and global consequences

Read the full arithmetic program and its A199 input conventions. The
residue algorithm writes a global unit as C0+t C1+t^2 C2 in the ramified
cubic over F'. Its three terms have distinct valuation classes modulo
three, so integrality makes the residue exactly that of C0. Coefficient
division after lifting the scalar cube root modulo q^(e+1) is valid in
the unramified degree-six coefficient ring.

Independently reran `code/two_inert_ninth_root_next_norm_characters.py`,
including its imported exact 54-dimensional root certificates and the
printed coefficient-table reconstruction. All assertions passed in about
three seconds. The retained output checks all 306 unit residues, the
complete 51-column matrix, the 13-column compression, all row relations,
rank three, determinant -1, and maximum scalar Hensel precision six.
It checks all three literal anti-unit sigma norms, the pure quadratic
normalizations, and the gamma/h/tau relations.

Completeness of the A199 pro-three unit basis makes the finite matrix the
image of all actual units. The six tame norm conditions, together with
global reciprocity at the unique three-prime and cyclic Hasse norm,
give the actual unit field-norm index 27. The completed assertion uses
actual norm preimages of generators and the converse local norm maps;
it does not replace unit norms by arbitrary field norms. The seven
ramified places and A206's class order 3^4 give ambiguous three-class
order 3^7 through the stated Chevalley formula.

## Retained alignment

For the certified anti-basis, the exact norms N_sigma(a)=1 give
K^3=h(f)^4/f and r0^3=h(f)/f. The divisor equality and the actual unit
h(x)/(r0 x) follow. No equality between eta and psi2 is inferred from
their finite dimensions or from principalization. The source states
this remaining alignment through its actual unit correction.

