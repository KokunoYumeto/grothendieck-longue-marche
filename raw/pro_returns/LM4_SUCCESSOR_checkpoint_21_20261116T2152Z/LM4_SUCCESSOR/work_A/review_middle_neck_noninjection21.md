# Independent full audit: the three natural mixed-neck maps are noninjective

Reviewed `work_DE/next_marginal_source/middle_neck_marked_noninjection21.md` completely on 2026-11-16. Verdict: **PASS**, with the minor initial-collar wording clarification recorded below. This proves failure of the natural semicircle-marked F5 injections, not failure of every alternative marking or of the global fixed-source equality.

## Exact collision and path check

Put a=cot(pi/5), b=cot(2pi/5), d=1/sqrt(5). Then a>b>0, a²=1+2d, b²=1−2d, ab=d, and (c1,c2,c3,c4)=(a,b,−b,−a). The actual graphs are

    Z_Aj=lambda_j(Q−i c_j),  Z_Bj=1/Z_Aj,
    lambda_j=2/(1+c_j²).

On the strip c_(k+1)<Im Q<c_k, the selected upper points are exactly B1,...,Bk,A_(k+1),...,A4. Their imaginary signs are strict and remain unchanged along a horizontal path. The two branch roots satisfy Z+1/Z=2Q. For nonreal Q, neither root is real, and their product1 gives opposite imaginary signs. For k2's real path, 0≤Re Q≤d<1 gives the same separation. Thus there are exactly five selected punctures in the literal upper half-plane along every path used.

The mixed-node equation gives

    lambda_i lambda_j[(Re Q)²+(c_i−c_j)²/4]=1,
    Im Q=(c_i+c_j)/2,

and therefore Re Q=|1+c_i c_j|/2 in the inner region. The entire indexed table of inner fixed/mixed critical coordinates is:

| Pair | Real coordinate | Imaginary coordinate |
|---|---:|---:|
| 11,44 | 1+d | a,−a |
| 22,33 | 1−d | b,−b |
| 12,34 | (1+d)/2 | (a+b)/2,−(a+b)/2 |
| 13,24 | (1−d)/2 | (a−b)/2,−(a−b)/2 |
| 14,23 | d | 0 |

There are ten indexed entries and nine distinct base values, because14 and23 coincide. It follows immediately that the horizontal paths to12,23,34 have no earlier mixed or fixed critical value. For k2, both upper nodes14 and23 occur at the endpoint; they are distinct, since distinct A graphs do not meet at Re Q>0. The old puncture Q=1 and the branch collision Q=±1 are avoided. These are exact radical identities, not numerical ordering tests.

Transversality also follows directly. For A_i−1/A_j, the derivative is lambda_i+lambda_j/Z_Aj². If zero, Z_Aj would be purely imaginary. Its real part is lambda_j Re Q>0, a contradiction. The B106 factorization independently ensures that these nodes avoid the retained branch and old punctures.

## Actual bad-piece and based-arc comparison

There is a useful exact strengthening of the half-plane control. Every A and B puncture has Re Z with the sign of Re Q. The same holds for either branch root, since

    Re Q = (Re Z)(1+|Z|^(−2))/2.

Thus, at positive Re Q, all selected punctures lie in the upper-right quadrant. Under t=(Z+1)/(Z−1), Re Z>0 is exactly |t|>1, the actual inner bad piece. The selected vanishing disks, their basepoint, and their transport can all be chosen there after entering the inner region.

One wording precision is needed at the literal initial neck value Re Q=0: its selected punctures lie on Re Z=0, so their meridians cannot already be contained in the open right half-plane. First transport through the actual arbitrarily short critical-free collar to Re Q=epsilon>0. The remainder of the path and its nullhomotopy then lie in the upper-right quadrant. This is precisely the existing natural edge-to-vertex map, not a change of its marking. DE was notified of this clarification.

Along the compact truncated path the punctures remain bounded and distinct. A common basepoint outside their trajectories, and an ambient isotopy of the punctured upper half-plane, transport the complete based F5. Near the endpoint choose a small disk around the chosen colliding pair, disjoint from the other selected punctures. For k2 choose disjoint disks for its two simultaneous upper nodes, retaining both. The short local vanishing arc and its geometric meridian whiskers can then be transported backward inside that same selected half-plane. They therefore belong to the actual initial K, not merely to the ambient fiber with an unidentified conjugator.

The two transported meridians are a pair in a geometric free basis of K. Their commutator is nontrivial in F5. Equivalently, their independent abelianization vectors prevent them from lying in one cyclic centralizer. In transverse holomorphic coordinates at the actual node, the complement is {uv≠0}; its two meridians commute. The common based transport identifies those meridians with the chosen K pair. Hence their nontrivial commutator becomes trivial when the actual critical base disk is retained.

The nullhomotopy lies in the actual inner bad piece after the initial collar. This proves noninjectivity of the natural K→R_inner itself, for k=1,2,3. It is stronger than showing that the physical component labels meet somewhere. It repairs the earlier generic disk-transport gap by the literal separating half-plane and quadrant.

## Scope

The natural first/last necks are unmixed and the one-family detector is unaffected. The three middle natural semicircle markings cannot serve as injective edges in a global five-neck amalgam. No conclusion is drawn about all alternative common rank-five subgroups, completion of a putative amalgam, or the final selected-source equality. A quotient-edge analysis remains a separate possibility.

## Executed exact-certificate review

After the analytic audit, I read DE's complete `check_middle_neck_nodes21.py`, its genuine successful stdout, and its empty stderr. The program independently uses exact radicals, checks all ten indexed inner coordinates, the adjacent-node formulas in the actual q coordinates, the simultaneous14/23 endpoint, and the absence of an earlier equal-height critical value. It also checks the real-branch inequality algebraically. The printed run reports PASS in5.843564426 seconds. The initial failed attempt is retained in `middle_neck_failed_attempt01`; no failed output was overwritten or represented as a successful run. I did not rerun this producer into DE's owned JSON while it was being reviewed.
