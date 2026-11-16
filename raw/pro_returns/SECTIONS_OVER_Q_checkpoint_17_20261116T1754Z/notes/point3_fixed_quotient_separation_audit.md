# A.202 exact scope and execution audit

Source: `sections/point3_fixed_quotient_metabelian_separation.tex`.

Certificate: `code/point3_fixed_quotient_separation_certificate.py`, with retained output and structured data.

## Proved refinement

For an arbitrary fixed finite geometric quotient `Q`, the actual A.72 recursion is retained, including its distinguished component, common finite quotient, all local points, and arithmetic fibre-product section. Only its first dyadic prime congruence is sharpened to `q0 = 1+2^L mod2^(L+1)`, and later dyadic precisions are increased. The CRT class still fixes the intersection field used in A.72.4 because it remains one modulo `n0`. The later choices remain in the same local component by the explicit continuation inequalities A.72.13–18.

The exact depth is `E=L+v2(n0)`. Every later factor is one modulo `2^(E+1)`, so the ordinary local limit has exactly `v2(x2-3)=E`, rather than merely a lower bound. This constructs the result for each sufficiently large prescribed integer `E`.

## Actual detecting map

The point-three frame modulo eight gives a dyadic sheet of the literal cover `z^8=-t(1-t)^3/24`. Its compactification is `y^2=x^5-54x`, with `t=x^4/(x^4-54)`. All dyadic sheets satisfy `x=3 mod8`. The factorization

`t-3 = -2(x-3)(x+3)(x^2+9)/(x^4-54)`

therefore gives `v2(t-3)=v2(x-3)+3` exactly. The rational deck group consists of `z -> +/-z`, which fixes `x`, so every fixed sheet has the same depth `E-3`.

A.193's actual proper-cover quotient at `n=E-2` receives the full metabelian quotient and maps the selected section to the finite Jacobian Selmer group. Its exact local test is `n <= v2(x-3)`, which fails. The geometric group has order `2^(4E-5)` and class `4E-8`. No unspecified quotient or change of coordinate is used.

## Three separate conclusions

1. A.72, with the proved precision refinement, gives all-place ordinary local matching in `E_(Q,A)`.
2. A.38 gives a global full profinite class-two lift of the same ordinary completed pair.
3. The finite detector proves that this pair has no everywhere locally point/cusp-matching full metabelian lift, hence no full Selmer lift.

The source asserts no simultaneous locally matching `Q`/class-two lift. The prescribed finite `Q` is fixed before constructing the pair; the detecting quotient depends on the resulting exact dyadic depth.

## Sources and execution

There is no new external theorem input. A.72 supplies its already verified field intersection, Chebotarev prime recursion, finite-cover local continuation and compact-conjugator argument. A.38 and A.193 supply their exact proved quotient maps and the finite Selmer criterion.

The executed finite certificate passes 768 first-depth cases, 9,216 later precision/partial-product cases, the symbolic cover/factorization/deck identities, and 2,432 all-sheet depth/detector-index cases. The general infinite-recursion and limit assertions are proved in the source; no large prime-search stage is represented as executed.
