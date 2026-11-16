# D88 collaboration: finite relative-depth cusp parameters

Status: unregistered structural calculation supporting DE's draft. This note assumes the independently audited exact operator-kernel comparison D87. Scope: the five-valuation of a is zero, the pair is (a,0), and the nonzero global away-five lattice has depth r, while its local unit coefficient has finite depth N >= r. Put e=N-r. No claim about a nonzero kappa(5) coefficient or an infinite local depth is made here.

## 1. Exact scalar presentation and the zero connecting map

Put q_j=t_1^(5^j)-1. For e>0, the actual connecting ideal J=q_r Lambda/(q_N) is identified, by multiplication by q_r, with A=Lambda/(q_N/q_r). The actual generator q_r is retained in the action. Set T=A/(uvw), E=vwA/(uvwA), Q=A/(vw). Then A/(u)=(Z/5^e)[[v]] and cancellation of vw gives E=(Z/5^e)[[v]]. The power-series polynomial q_N/q_r is distinguished, has constant term5^e, and has degree5^N-5^r. Thus A is finite free over Z5[[v]], and u is a non-zero-divisor (evaluate a relation u f=S g at u=0, then cancel u).

The quotient Q/uQ is (Z/5^e)[[v]]/(v²), with the actual q_r generator. After the single Cartier untwist its two tame characters are chi² and chi³. Consequently it has no Gamma-invariants. Every element of Q^Gamma lies in uQ and has a lift in uT. This lift is fixed: its operator difference lies in both uT and E, whereas

    uT intersect E = (uA intersect vwA)/(uvwA) = 0.

Indeed vw modulo u is v², a non-zero-divisor in (Z/5^e)[[v]], so uA intersect vwA=uvwA. Hence the snake map Q^Gamma -> E_Gamma is zero. This is an exact all-depth argument, not a rank comparison.

## 2. Infinite torsion layer

On the actual generator q_r v w, setting u=0 gives the compact Cartier-untwisted action chi*S_chi(1+v)^3 times substitution. Multiplication by v³ identifies it with v³ in the chi-twisted completed group ring (Z/5^e)[[Z5]]. The three missing jets have tame weights chi, chi², chi³ and therefore contribute nothing after exact tame averaging. Continuous invariant functions are finite-support shell functions with arbitrary values in Z/5^e. Thus E_Gamma is the compact product over countably many copies of Z/5^e.

## 3. Actual finite boundary modules

Each boundary, including its exact diagonal half-gauge, identifies with u J_(r,N), where

    J_(r,N) = ker(Z5[C_(5^N)] -> Z5[C_(5^r)]).

The quotient J/uJ has nontrivial tame character chi, so uJ and J have the same full Gamma-coinvariants. On invariant orbit sums, the map from C_(5^N) to C_(5^r) multiplies each of the r nonzero low-valuation shells by5^e and is onto on the zero orbit. Its cokernel is (Z/5^e)^r. On orbit coinvariants the map is onto with free kernel rank e. The cyclic homology sequence therefore gives

    J_(r,N),Gamma = (Z/5^e)^r x Z5^e.

The quotient in the two-boundary normalization sequence has tame character chi² and no homology after tame averaging. Hence

    Q_Gamma = (Z/5^e)^(2r) x Z5^(2e).

The independent certificate uses literal integral matrices on the relative kernel, not just the orbit formula, and obtains exactly these Smith factors.

## 4. Torsion exponent and the complete product type

The zero snake map yields an extension of Q_Gamma by E_Gamma. Split off the free Z5^(2e) quotient continuously. Its remaining compact part K' is a bounded extension of (Z/5^e)^(2r) by the infinite product of Z/5^e, initially of exponent at most5^(2e).

D77's exact natural invariant map gives the divisible local/global quotient (Q5/Z5)^(2e). Its injection fills the maximal divisible subgroup of T_Gamma dual, since both have that finite corank and the remainder is bounded. Thus the actual operator restriction kernel is the dual of K'.

The subgroup I5 has index5^e in I_s. The continuous restriction/corestriction identity kills the whole restriction kernel by5^e; normality of I5 is unnecessary. Therefore K' has exponent5^e. Its quotient (Z/5^e)^(2r) is free over Z/5^e, so this finite quotient splits continuously. The finite summands are absorbed into the countably infinite product. D87 now gives

    S_(a,0) = product_N Z/5^e,
    K_(a,0) = (product_N Z/5^e) x Z5^(2e)       (e>0).

For e=0 the actual global and local operator groups coincide, so S=K=0. The separate natural boundary map retains global ranks2r and local ranks2N, together with the common zero-axis factor; its kernel has rank2e.

## 5. Executed independent support

Files: `pbc_D88_boundary_certificate.py/.json/.out`. Six literal matrix cases (r,N)=(0,1),(0,2),(0,3),(1,2),(1,3),(2,3), dimensions4,24,124,20,120,100. Relative augmentation, its u-multiple, and the diagonal half-gauge have identical integral Smith data: free rank e and r factors5^e. The two- and three-jet operator-difference determinants are both21, a five-adic unit. Finite weighted shell checks cover coefficient exponents1--4 and levels1--6. All checks PASS; the all-depth proof is the argument above.

## 6. Actual rational tangent examples

For every r,e>=0 take a=5^r*kappa(1+5^(e+1)). This is the Kummer class of the rational tangent parameter (1+5^(e+1))^(5^r). Its five-valuation is zero and its logarithm has the required local depth N=r+e. The integer1+5^(e+1) is not a fifth power: factoring n^5-1 and using the exact five-valuation of n^4+n^3+n²+n+1 forces the latter to be5, impossible for n>1. Therefore at least one prime exponent is a five-adic unit, proving the asserted global depth r without needing a factorization of the integer.
