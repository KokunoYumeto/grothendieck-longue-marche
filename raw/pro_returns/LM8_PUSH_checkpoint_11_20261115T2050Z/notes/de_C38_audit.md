# Independent audit of C.38

**Verdict: PASS.** I read the entire candidate `notes/pbc_C38_draft.tex`, against the already checked actual group and lifting constructions in C.33 and P.2/P.4 and the dimension bounds in C.34. This is a structural proof; no illustrative numerical test is needed.

## Actual rational Lie algebra

The finite Magnus representation is faithful on the indicated actual quotient. A first nonzero normalized conjugator term f_n changes Y first by [Y,f_n]. The centralizer of Y in the characteristic-zero free Lie algebra is its degree-one line, so in degrees n at least2 this detects the term. Thus the operator and conjugator filtrations agree, including after passing to rational logarithms. I suggested making this sentence explicit in the candidate.

The rational span of log U is closed under Lie brackets. The two-variable finite BCH polynomial evaluated at nonnegative integer powers lies in that span; rational Vandermonde inversion recovers its ab coefficient, [X,Y]/2. Bilinearity then applies to the whole span. No integral BCH denominator assertion is made.

A basis consisting of actual logarithms gives the finite polynomial product-coordinate map t+R(t), with identity linear term. On a sufficiently small p-adic ball, all higher rational coefficients are absorbed and R is a strict contraction. Powers by Zp remain actual elements of the closed compact group. The contraction therefore gives an entire small exponential neighborhood in U. Scaling any vector of each filtered Lie term into that neighborhood proves that the associated graded Lie algebra is exactly the rationalization of the actual integral graded group. It is not merely the tangent space to the equations.

## Removal of hidden filtered relations

An actual Galois element with multiplier 1+p exists. Its conjugation operator has scalar (1+p)^n on each successive degree. The product of these distinct linear factors annihilates the filtered vector space, so its minimal polynomial is square-free and the operator is semisimple. The resulting eigenspaces identify with the actual graded pieces. Brackets multiply eigenvalues, hence recover the graded Ihara bracket exactly; a weight above the truncation has no eigenspace and is zero. This proves that higher terms of lower brackets cannot create extra relations in the top indecomposable space.

On the Lie abelianization, inner conjugation is trivial. All remaining conjugation operators factor through the abelian multiplier group, commute with the wild grading operator, and preserve its weight spaces. The top weight comes from the actual top filtration quotient, where the action is precisely lambda^m. Thus the selected functionals have exact rational lambda^m covariance under every element, not only under a tame subgroup or modulo p.

## Actual integral characters and arithmetic correction

The map ell(log u) is additive because ell kills every BCH commutator. Its image J is the actual compact subgroup of a finite-dimensional Qp-vector space. It is a Zp-submodule by closure of integer multiplication, bounded by compactness, finitely generated as a submodule of a finite free lattice, and full-rank because log U spans. Choosing a basis of J therefore produces a joint surjection onto Zp^h. This simultaneously resolves integrality and primitivity; no claim that log U is itself an integral Lie lattice is needed.

For m divisible by (p-1)p^(k-1), the exact covariance becomes trivial modulo p^k. The five-term sequence extends each character because the multiplier group has p-cohomological dimension1 after exact tame averaging. The actual arithmetic action is unramified outside p, as checked in C.33. Kronecker–Weber identifies its finite p-power additive characters with multiples of the logarithmic cyclotomic character. Subtracting that character removes the arithmetic restriction and changes nothing on global multiplier one. P.4's actual global lifts preserve the joint surjectivity.

## Simultaneous prime powers

For each fixed p,k, the space V_(p,k) of mod-p restrictions of actual arithmetic-trivial Z/p^k characters is an Fp-vector space. Unbounded d_m gives infinite dimension. Enumerating k,j and choosing each new restriction outside the finite span of the previous ones is therefore valid even though the rational weights and their integral lattices can mix modulo p. No direct independence of distinct rational weight spaces modulo p is assumed.

For a finite chosen collection with target T, independence gives H+pT=T for its image H already on global multiplier one. The quotient T/H is a finite p-group, so multiplication by p cannot be onto unless that quotient is zero. Thus every finite product map is onto. Compactness gives the infinite product, and coprime primary factors can then be combined. Countable baseness supplies the matching countable upper bound on the dimension of finite-target characters. The proof correctly avoids inferring any compatible Zp quotient from unbounded finite orders.
