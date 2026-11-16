# Root complete audit of the ordinary-fibre compact kernels, D.93

**Verdict: PASS, subject to the separately requested independent audit
before canonical integration.** Root read the entire notes-only draft
and the entire certificate, then executed the certificate read-only.
The full output is byte-identical to the author's saved JSON. The
structural all-depth proof is checked below independently of those two
finite Smith calculations. No canonical source has been changed.

## Actual rational points, global lattice and local parameters

The point t=2^(5^r) supplies an actual full rational-point section.
Its first Kummer coordinate is 5^r kappa(2), while the second is the
class of the positive odd integer B=2^(5^r)-1; the minus sign has zero
pro-five Kummer class. B is prime to five. Writing h=2^(5^(r-1)),
the strict inequalities (h-1)^5 < h^5-1 < h^5 prove that B is not a
fifth power. Thus some prime valuation of B is not divisible by five.
Its prime support is disjoint from that of the first coordinate. This
proves the exact integral lattice 5^r Z5 times Z5, not merely a rational
rank or a residual rank assertion.

The local logarithmic coefficient is log(x^4)/(4 log6). For x=2 its
mod-five residue is 3/4=2. Since 5^r is 5 modulo20 for r at least one,
2^(5^r) is7 modulo25, so 1-t is -6 modulo25 and its logarithmic
coefficient is1 modulo5. The local vector therefore has the form
(5^r alpha,beta) with both alpha and beta units. The depths of a,b,a-b
are (r,0,0) both globally and locally. The exact D.77 boundary sequence
therefore has no additional free local factor and identifies K with S.
This does not replace equality of maps by an equality of ranks.

## Integral operator comparison and retained scalar generator

Root rechecked the actual D.87.4 invariant-quotient formula, its definitions
and its common-complement image statement. In this family the five-valued
coordinate is zero, so there is no hidden translation graph in the
untwisted complement. With q=t1^(5^r)-1, local elimination of the second
variable is integral because beta is a unit. It gives
t2=t1^(5^r gamma), gamma=-alpha/beta a unit, and the actual translation
ideal (q,v) becomes qR in R=Z5[[u]]. Both v/q and w/u are units, since
r is positive. Consequently the actual ideal (P) is exactly (u^2 q).

The boundary identities and D.77's primitive local cubic element give
the ideal of all multiplier-one operator differences exactly (P).
The primitive difference is P times a unit; this is stronger than a
leading-term or rational assertion. Ordinary Pontryagin duality of the
actual D.87.4 map thus gives the displayed kernel of compact
coinvariants, with the Cartier untwist retained. Dividing the source
ideal by its genuine generator q gives T=R/(u^2 q), with the factor
chi^-1 S_chi(t1^(5^r)) in its actual action. The natural map to the
target still multiplies by q. It is not identified with the identity
between two abstractly isomorphic scalar modules.

## Low jets, exact weight and vanishing of the natural map

The two successive characters of T/u^2T are chi^2 and chi^3.
Neither is trivial on the order-four tame subgroup. Exact averaging,
followed by the homology sequence for the pro-five quotient of Gamma,
kills every Gamma-homology group of that two-jet module. Thus its H0
and H1 both vanish, and the map from the u^2 layer to T is an
isomorphism on coinvariants. This explicitly supplies the injectivity
that right exactness alone would not give.

Since R is a domain, the retained u^2 layer is R/(q), the finite free
integral group ring Z5[C_(5^r)]. On this layer t1^(5^r)=t2=1.
The retained q factor cancels the Cartier untwist; the second axis
contributes chi, the first contributes S_chi(t), and the u^2 generator
contributes S_chi(t)^2. The exact boundary value B_g(t,1)=1 therefore
leaves precisely chi S_chi(t)^3 followed by t mapping to t^chi.
The draft retains every one of these factors.

The actual inclusion map sends the u^2 layer to q u^2, which is zero
in the target R/(u^2 q). Since that layer generates all source
coinvariants by the proved isomorphism, the entire natural map is zero.
This proves that the source coinvariants are the whole compact kernel.
No target torsion-freeness or conjectured elementary-divisor pattern is
needed for this conclusion.

## Explicit matrix, all-depth determinant and exact replay

Two topologically generates Gamma=Z5^times: it has order four modulo
five and 2^4-1 has five-adic valuation one. On the basis t^j its exact
action is M=2(I+T)^3 Pi, with T the cyclic shift and Pi sending j to2j.
The image of M-I in a finite free compact module is closed, so the
coinvariants under this dense cyclic subgroup are exactly the full
compact Gamma-coinvariants.

After adjoining all roots of unity, the t=1 eigencoordinate contributes
16. For each primitive order5^j there is one doubling orbit, of length
4 times5^(j-1). The product of the factors (1+zeta^(2^k)) telescopes to
one around that orbit. A weighted cyclic permutation contributes one
minus its total weight to det(I-M), giving exactly the stated product.
Its factors are all nonzero. The elementary binomial valuation argument
gives valuation j on the j-th primitive factor, and valuation one on
the t=1 factor. Hence the full cokernel is finite, with order
5^(1+r(r+1)/2), for every r. This proof does not infer the formula from
the two matrices computed in the certificate.

Root read every line of the certificate and replayed its run() function
without overwriting the author's source or outputs. It forms the literal
integer matrices, checks their action decomposition, computes integer
Smith forms and full determinants for r=1,2, and verifies the displayed
unit-logarithm congruences in thirty finite examples. Every byte of the
returned JSON agrees. Source SHA-256 is
`8241b00f9f814dfe41b75962af97c8ad8422f9b94da1a474d884f6f448ae7e30`;
output SHA-256 is
`de3615275adba931c68e8002d7fe328c769122bfefb5bfb43b470821a662168f`.
The standalone replay and verification ledger are retained. The exact
Smith factors asserted are only C25 and C5 plus C125 for these two cases.

## Actual section fibres and limits of the conclusion

D.74 applies because each pair has finite prime support and an actual
section already supplied by t. Its translation group is the compact
countable product of Z5, with the isomorphism understood noncanonically.
The two nonzero Kummer coordinates have disjoint prime supports, so the
pair is on none of the three complete cusp lines. Equality with an
ordinary rational point's pair forces z=plus or minus t and
1-z=plus or minus(1-t), by the exact kernel of the rational pro-five
Kummer map. The negative first choice is impossible for either second
sign. Thus exactly the given rational point supplies an ordinary point
class in this fibre; the other classes are neither rational-point nor
cuspidal classes.

The draft does not confuse this first-cohomology translation group with
the finite second-cohomology compact kernel. It asserts no general
section-existence criterion, no full elementary-divisor formula, and no
universal higher-derived lift. These scope boundaries are appropriate.
The imported D.74, D.77 and D.87 arguments have earlier complete root
audits; their precise statements and the needed operator formulas were
rechecked here. No new external source is required for the elementary
arithmetic and determinant steps proved in this draft.
