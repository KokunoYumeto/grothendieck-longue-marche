# Independent audit of C.34

**Verdict: PASS.** I read the entire candidate `notes/pbc_C34_draft.tex`, following the independent full C.33 audit in `notes/de_C33_audit.md`.

## Dimension formula

For homogeneous degree at least two, peripheral conjugators have no centralizer ambiguity. The three-position permutation representation modulo diagonal inner derivations is the standard two-dimensional representation V. Bracketing with the three peripheral generators descends to a surjection `V tensor L_n(V) -> L_(n+1)(V)`, because brackets with x and y span integrally by Jacobi induction. Its kernel is precisely the special outer derivation space. Taking S3 invariants over Q gives the displayed trace expression for a_n; no independent-bracket assumption enters.

The PBW trace identity is equivariant: the tensor algebra has trace series `(1-tr(g|V)t)^(-1)`, and taking the logarithm of the symmetric-algebra decomposition gives the stated divisor sum. Its Möbius inversion is the Witt character formula. At the identity the leading contribution is `2^n/n`; nonidentity contributions have exponential size at most `2^(n/2)` for a transposition and `2^(n/3)` for a three-cycle. Therefore `a_n = 2^n/(3n(n+1)) + O(2^(n/2))` is correct.

## Asymptotic bracket count

All a_n are nonnegative, and each is at most the dimension `2l_n-l_(n+1)` of the full special outer space. Dividing by 2^n and summing telescopes exactly to `1/2-l_(N+1)/2^N`. At n=5 the full dimension is three and a_5 is one; this lowers the total limiting bound by `2/32=1/16`. Hence `S<=7/16` is justified.

For `r_n=a_n/2^n ~ 1/(3n^2)`, the convolution estimate is valid. The fixed end intervals give `2 sum_(i<=M) r_i` after division by r_n. In the middle half interval the ratio `r_(n-i)/r_n` is bounded independently of n and i, because `n-i>=n/2`; its tail is at most a constant times `sum_(i>M)r_i=O(1/M)`. The other half is symmetric. The even diagonal subtraction in b_n is exactly half of a_(n/2), and its ratio to a_n is exponentially small. Thus `b_n/a_n -> S` and `d_n ~ (1-S)2^n/(3n^2)`, proving positivity and growth along every sufficiently large prime without extrapolating from finite data.

## Integral and profinite comparison

For each p>=5 the actual quotient of the multiplier-one local image through conjugator degree p-1 has nilpotency class at most floor((p-1)/3), strictly less than p. Its integral Magnus logarithm and Lazard comparison use only the small automorphism-group class. The full peripheral correction and coprime S3 step from P.2/P.4 give the actual integral graded groups, not merely formal solutions.

The p-1 tame characters on possible weights 3 through p-1 are distinct, so the filtered Lie lattice splits integrally. The rank of its bracket contribution in the top piece is bounded above by b_(p-1). The annihilator of the actual bracket submodule is saturated in the dual lattice; its reduction modulo p therefore retains the asserted number of independent functionals. This is sufficient even if the bracket submodule itself is not saturated. The full multiplier invariance, continuous character extension, and cyclotomic arithmetic correction repeat the verified C.33 argument exactly.

Independent mod-p values are witnessed on actual global multiplier-one lifts. For finitely many different primes, pairwise coprime orders make the finite joint image the entire product. Including any finite subset of the independent quadratic characters and then using compactness proves the full product surjection.

## Executed independent check

I reran `code/pbc_gentle_dimension_formula.py` through weight 300 without rewriting the author's JSON. The independent stdout is `code/de_C34_dimension_audit.out`. It verifies the trace integrality, nonnegative dimension bounds, comparison with all directly computed dimensions through twelve, and the exact telescope. The values at p=13,17,19,23,29,31 are respectively 1,37,143,1805,77519,273536, as stated. The finite partial sum is approximately 0.21724385834446233; that approximation is a diagnostic only and is not used to prove the eventual assertion.

The result remains a quotient theorem, not a classification of the full abelianization. The draft correctly makes no claim that these odd-primary characters vanish on the pentagon group.
