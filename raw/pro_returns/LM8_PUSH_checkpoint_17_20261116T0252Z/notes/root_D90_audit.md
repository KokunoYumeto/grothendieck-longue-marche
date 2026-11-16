# Root full proof and certificate audit of the D.90 candidate

**PASS, notes only during checkpoint15 source freeze.** Root read the
entire draft `notes/de_sha_dominant_valuation_cusp_draft.tex`, SHA-256
`6d73d95d7ec8c6ce300c53d5e9207efe04ac6de4a39cc5cdc5268c598be70a9b`,
and every line of the independent literal boundary certificate.
Root reexecuted that certificate and obtained whole JSON equality,
SHA-256 `b12d51825cd77c76482a78e6fe59191e1562b006e0193eb241708443de41dd77`.
The exact source hash and checked depths are recorded in
`root_D90_boundary_verification.json`.

## Actual graph, scalar relation and zero invariant map

The range is a nonzero five-valuation coordinate with depth m at most
the nonzero away-five depth r, and relative local unit depth e=N-r.
The two actual elements checked in D.89 give the exact difference
ideal (P,q_m), because A=5^m times a unit. The binomial quotient by
q_m has unit constant coefficient, so this is an integral equality.
The actual inclusion J=q_r R into R lands in q_m R when m<=r.
Thus its map on actual invariants is literally zero, and D.87
identifies S with the coinvariants of J/(PJ+q_m J).

Modulo q_m, the exact relative norm q_N/q_r becomes 5^e because
t_1^(5^r)=1. The scalar ring is therefore
C[C_(5^m)][[v]]/(uvw), with C=Z/5^e or Z_5 at infinity.
The retained generator q_r contributes chi and cancels the single
Cartier untwist. The valuation-graph multiplier becomes one. The
remaining action is the precise original Alexander action, not an
artificial action assigned to the scalar ring.

## Shell injection and the additional axis kernel

Both v and w are regular. The stated change of variables is
continuous: u is topologically nilpotent in the five-adically
complete cyclic group ring (and nilpotent modulo any finite power
of five), and t_1 is a unit. It preserves q_m. This proves the
regularity of w without incorrectly treating u as regular.
The shell layer E is C[[v]] and has the already checked weighted
action chi*S_chi(1+v)^3. Its coinvariants are product C.

The quotient Q/uQ has the two nontrivial tame characters chi^2
and chi^3. Also (u) intersects (vw) in (uvw): modulo u, v^2 is
regular even over finite C. Therefore uT to uQ is an equivariant
isomorphism and every Q-invariant lifts invariantly. The zero
connecting map injects the shell coinvariants over every coefficient
ring used here.

The two-axis map is correctly not declared injective. The
annihilator of u in the literal cyclic group ring is exactly
C times the norm sum N_m. Solving vf=wg gives the extra kernel
C*v*N_m. Cancellation by v and evaluation on w=0 prove this is
an actual copy of C. Its action has tame weight chi^3: the norm
sum is invariant under multiplier permutations, u*N_m=0 and
v^2*N_m=0 in Q. The final augmentation cokernel has weight chi^2.
Both disappear by exact tame averaging before procyclic
coinvariants are taken.

Each surviving boundary transports by multiplication by u,
with the explicit half-gauge on the diagonal, to the weighted
permutation action t^x to chi*t^(chi*x). The kernel norm line
and augmentation quotient have the two stated nontrivial tame
characters. The zero orbit contributes nothing. The nonzero
valuation-shell orbit of length 4*5^(m-i-1) contributes exactly
C/5^(m-i)C, by the five-valuation of 2 to that power minus one.
The two boundary copies yield every finite cyclic factor in the
statement, naturally under coefficient reduction.

## Splitting requires the actual finite-order and reduction arguments

For finite C=Z/5^e, the whole module is killed by 5^e. If x
lifts a quotient generator of order 5^d, then 5^d*x lies in
the injected product C and is killed by 5^(e-d). In that
specific product, the annihilator equals 5^d times the product.
Subtracting a suitable element therefore gives an order-5^d
lift. Finitely many such lifts split the finite quotient
continuously. Only the cyclic factors of exponent exactly 5^e
are absorbed by the countable product; the smaller factors
remain. This is why the final formula retains two copies of
Z/5^j for j<=min(m,e-1).

For C=Z_5 the abstract endpoint groups alone do not prove
splitting. The proof uses the actual coefficient reduction at
h>=m. Coinvariants commute with this quotient by the same
continuous operator image; that image is compact and closed.
The finite-level zero-snake injection gives
E intersect 5^h M=5^h E. Since the finite quotient Q is killed
by 5^h, this implies 5^h M=5^h E. Lift the finite-level
order-5^j representatives and use 5^h E contained in 5^j E
to correct their orders in M itself. This gives the required
actual continuous section and preserves the finite smaller
cyclic factors at the infinite endpoint. No limit interchange
or infinite-corank subtraction is used.

## Full compact kernel, examples and exact execution

The full global and local depths of a and a-b are both m;
b=0 gives the identical countable boundary product. Thus
D.77's actual boundary map is an isomorphism and K=S. The
equal-image case e=0 is zero. The rational tangent
5^(5^m)*(1+5^(e+1))^(5^r) has the exact asserted depths.
For m=r=1 and e=2 it is 630^5, giving product Z/25 with
two additional Z/5 factors. The finite-support completed
zero-log example is nonzero at away depth r and retains
five-valuation depth m. All supply actual cusp sections.

The independent certificate constructs, rather than prescribes,
the integral cyclic shift and multiplier matrices for m=0,1,2,3.
It verifies the actual augmentation intertwining, diagonal
half-gauge, norm-line action and integer Smith forms. Their
five-primary entries are exactly 5^1 through 5^m. The
coefficient exponents e=1 through 5 cover e<m, e=m, e>m and
the m=0 degeneration. Root read and ran the whole source.
The infinite extension and universal depths rest on the proof,
not those finite samples.

This candidate does not enter the frozen checkpoint15 paper.
The range r<m<N and arbitrary other dependent pairs remain
separate. Integration can follow after the scheduled save,
subject to preserving the fully audited source and current
independent PASS ledgers.
