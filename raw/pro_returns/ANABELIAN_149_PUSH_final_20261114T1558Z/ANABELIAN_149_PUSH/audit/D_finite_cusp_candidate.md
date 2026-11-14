# Finite local cusps after D.30: a positive criterion and the exact remaining arithmetic condition

Candidate only, written during checkpoint09's source freeze. No integrated claim or coverage status changes. No priority claim.

## 1. One cusp label is enough to finish the cofinite-integral case

Let U=P¹_Q−{0,1,∞}, and let s be a continuous noncuspidal section. Assume that the local sections are ordinary integral point sections outside a finite set of primes. Assume in addition that all cuspidal local sections, if any, have the same cusp label c.

Then s is a rational point section.

Proof. If there are no cuspidal local sections, D.5 applies. Otherwise choose the following global unit, according to c:

| c | u(t) | u(c) |
|---|---|---|
| 0 | 1−t | 1 |
| 1 | t | 1 |
| ∞ | t/(t−1) | 1 |

Each u is regular and nonzero at the indicated cusp. At an ordinary local point its Kummer pullback is the actual value u(x_p). At an arbitrary continuous splitting of the corresponding cusp decomposition group its pullback is the actual nonzero leading value u(c)=1: inertia acts trivially on every Kummer root of such a unit. This does not impose a rational tangent hypothesis.

Consequently the global class A=s*κ(u) is represented by an element of Q_p* at every finite place and by a Z_p-unit at all but finitely many places. D.3 gives A=κ(a) for a∈Q*. At one cuspidal place its localization is 1; injectivity Q_p*→widehat(Q_p*) gives a=1. At every ordinary place one therefore has u(x_p)=1. None of the three displayed functions takes the value 1 on U: the respective equations give x_p=0, x_p=1, or 0=−1. There are ordinary places by the cofinite hypothesis, a contradiction. Thus there were no cuspidal places, and D.5 applies.

Combining with D.30, a noncuspidal section for which one Legendre representation at a coefficient prime ≥5 is finitely ramified is a point section if its local cusps use at most one of the three labels. The unproved extra hypothesis is exactly the restriction on cusp labels.

## 2. The general unit version

Let X/Q be a smooth geometrically connected hyperbolic curve with smooth completion C. Suppose s is a continuous noncuspidal section that is locally an ordinary or cuspidal section at every finite place and is ordinary integral outside a finite set. Let T be the set of closed boundary points of C that occur as centres of local cuspidal sections. This is a subset of the finite boundary C−X.

If there is a nonconstant u∈O(X)* whose divisor has coefficient zero at every point of T, then s is a rational point section.

Indeed, u extends as a regular nonzero function at each relevant cusp. The same argument as above makes s*κ(u) the class of one a∈Q*. At every ordinary local point, u(x_p)=a; at every cuspidal centre, u(c_p)=a. Hence every finite-place support point belongs to the finite closed subscheme given by the fibre u=a of the extension of u to C→P¹. The finite-place finite-support argument in D.5/D.22 (Stix Corollary5, with the already audited finite-place Stoll8.2 input) proves that s is geometric, and noncuspidality places the point in X.

In particular, write Λ=O(X)*/Q*, viewed through its injective boundary divisor map. A hypothetical cofinite-integral, nongeometric section must make

    Λ → ⊕_{c∈T} Z,    u ↦ (ord_c u)_c

injective. This is only a necessary condition. For the tripod, Λ has rank2 and the three boundary valuation functionals sum to zero. Thus T must contain at least two cusp labels. This recovers §1 without pretending that two or three labels are impossible.

There is also a precise neighbourhood criterion. Let r be the number of cuspidal finite places of s. If some connected finite étale neighbourhood Y/Q of s has rank(O(Y)*/Q*)>r, then s is a point section. The lifted section is still noncuspidal and cofinally ordinary integral, by the finite-normalization comparison in D.25. Its local cuspidal places are exactly among those r places: an ordinary point lifts to an ordinary point, and a point above a boundary point is a boundary point. There are therefore at most r relevant closed boundary centres on Y. The valuation map from its unit lattice to Z^r has a nonzero kernel, so the preceding criterion applies to the lifted section and then descends to s. In genus zero, the unit rank equals the number of closed boundary points minus one, giving an explicit sufficient count. No assertion is made that such a unit-rich neighbourhood always exists.

## 3. The surviving finite-support profinite unit problem

Return to U. Choose a finite S containing ∞, all nonintegral ordinary places and all cuspidal places, and write Γ=Z[S_f^{-1}]*. Let

    A=s*κ(t),       B=s*κ(1−t).

At every p∉S both local classes are actual units, so their global valuation coordinates vanish outside S. The explicit coordinate description in D.3 therefore places A and B in the full profinite completion of Γ. For each p∉S, the completion map Γ→Z_p* is defined, and

    A_p=x_p,       B_p=1−x_p.

The image of widehat(Γ)² in ∏_{p∉S}(Z_p*)² is exactly the closure of Γ²: the source is compact, the original group is dense in it, and the target is Hausdorff. Consequently the outside-S tuple lies in

    closure(Γ²) ∩ ∏_{p∉S}{(x,y)∈(Z_p*)² : x+y=1}.

This is an actual deduction from s; it is not assumed to consist only of diagonal S-unit solutions.

The additional local relations at exceptional cusps are:

| Local cusp | Relation between completed local classes |
|---|---|
| 0 | B_p=1 |
| 1 | A_p=1 |
| ∞ | A_p/B_p=−1 |

At the last cusp t/(1−t) has leading value −1. The tangent-dependent class occupies the remaining direction. If S_0,S_1,S_∞ are the corresponding subsets, the only potentially nonintegral profinite valuation coordinates are therefore of the forms

    p∈S_0: (a_p,0);
    p∈S_1: (0,b_p);
    p∈S_∞: (c_p,c_p).

All coordinates at ordinary places are ordinary integers. These statements do not turn the unknown profinite exponents into integers.

Harari–Voloch's primary Theorem1 identifies precisely the displayed outside-S closure condition with their finite abelian descent/B_S-Brauer condition. Their Conjecture2, specialized to the tripod, asserts that this intersection consists of diagonal S-integral points; Remark2.5 relates its existence version to Skolem's exponential congruence conjecture. The paper itself does not prove that assertion for number fields.

If that intersection statement holds for this S and this tuple, say the outside-S tuple equals (a,1−a), then the compatible almost-everywhere Kummer detection lemma in D.26 gives A=κ(a), B=κ(1−a) globally. Any local cusp would then contradict the corresponding row above: at0 it would imply a=0, at1 a=1, and at∞ a/(1−a)=−1. Hence all local sections are ordinary, and D.5 finishes. This is a conditional implication, not a proof of the needed intersection statement.

## 4. What the modular-curve theorem supplies

Helm–Voloch's Theorem4 assumes a single finite S, good-reduction elliptic curves E_p/Q_p for every p∉S, and integral representations ρ_l whose restrictions are T_l(E_p) for all l and p∉S. It constructs an elliptic curve E/Q realizing all integral Tate representations. Their Theorem3 consequently gives existence of an S-integral point on the specified modular twist when its finite-cover descent set is nonempty.

Those conclusions corroborate and can strengthen the elliptic-realization part of D.30 once cofinite integrality is known. They do not assert that the given local moduli points all equal that one global point. Theorem3 is an existence assertion. Moreover, an arbitrary finite étale neighbourhood of a tripod section need not be a congruence modular curve or a twist of one. Neither assertion therefore supplies the finite-support condition for all neighbourhoods or eliminates the exceptional cuspidal local sections.

The D.30 proof remains unchanged during this checkpoint. A possible later citation can note the older integral realization theorem without replacing the independently checked finite-ramification equivalence.

Liu–Xu's very strong approximation theorem does not change this distinction. Their Theorem1.2 applies to the projection outside S of a full all-place Brauer–Manin adelic point. At a cuspidal place the section supplies a boundary point and a completed tangent class, not an ordinary U(Q_p)-point completing the tuple to that all-place set. Their stronger outside-S B_S assertion is Theorem1.4 for function fields; over Q the stated corresponding Corollary5.11 is restricted to S consisting of archimedean places. Thus substituting Theorem1.2 into §3 would assume the missing ordinary local completion.

## 5. Sources actually opened

- Harari, D., & Voloch, J. F. (2010). The Brauer–Manin obstruction for integral points on curves. Mathematical Proceedings of the Cambridge Philosophical Society, 149(3), 413–421. Primary author PDF: https://www.imo.universite-paris-saclay.fr/~david.harari/articles/dhvol.pdf . Opened Theorem1, Conjecture2, Remark2.5 and their proofs, author pp4–7. The exact number-field intersection is presented as a conjecture, not as a proved application.
- Helm, D., & Voloch, J. F. (2011). Finite descent obstruction on curves and modularity. Bulletin of the London Mathematical Society, 43(4), 805–810. https://doi.org/10.1112/blms/bdr015 . Primary author PDF: https://web.ma.utexas.edu/users/voloch/Preprints/modularity.pdf . Opened Proposition1 and Theorems2–5/Proposition6, author pp3–8, including the last integral-lattice paragraph.
- Stix's supplied arXiv1203.3236v3 source was reopened at Corollaries5–6 and the Selmer/adelic definitions. D.3, D.5, D.22, D.26 and D.30 are the project's previously checked inputs.
- Liu, Q., & Xu, F. Very strong approximation for certain algebraic varieties. Primary author version arXiv:1405.1988v2, https://arxiv.org/pdf/1405.1988 . Opened Definition1.1 and Theorems1.2–1.5, pp2–3, including the explicit distinction between projected all-place Brauer–Manin points and the outside-S B_S condition. No arbitrary finite-S number-field Harari–Voloch theorem is claimed.

No conclusion is drawn that the Harari–Voloch conjecture is equivalent to the full section conjecture, or that arbitrary elements of the closure intersection lift to sections. The implication above only uses the tuple actually induced by s.
