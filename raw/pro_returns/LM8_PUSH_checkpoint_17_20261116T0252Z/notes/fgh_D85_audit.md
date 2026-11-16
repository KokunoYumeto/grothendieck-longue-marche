# Independent FGH audit of D85

**PASS — full written proof, actual module maps, and complete exact certificate.**

The complete 443-line draft `notes/de_sha_global_independence_draft.tex` was read, together with the exact supporting program and `notes/de_D85_sources.md`. No canonical DE file was changed. The independent driver `code/fgh_D85_certificate_rerun.py` executes the original program under a non-main run name, preserves its outputs, and compares the complete result object with the author's JSON. Output is retained in `notes/fgh_D85_certificate_rerun.json/.out`.

## Proof gates checked

1. The reduction to the remaining away-lattice shape uses actual global mod-five independence, and retains the valuation vector as an integral complementary basis vector. The shared graph of the actual Kummer character of five and the integral gauge in the closed away lattice are the established D82/D83 inputs; no formal replacement action occurs.
2. The new integral quotient is literally `(x,g_h)/y(x,g_h)`, with `g_h=(1+y)^(5^h)-1`. Evaluation at y=0, cancellation of y, and then evaluation at x=0 show that it is `x Z5[[x]] direct-sum Z5 g_h`; the second summand is annihilated by x. This is an integral assertion, not a rational dimension count.
3. The actual local relation is `f_lambda(x)+nu*g_h`. In particular, the extra generator is not discarded before imposing the relation. Its compact action is exactly cyclotomic weight three, because substitution contributes one power and the actual Ihara multiplier contributes two. After the Cartier untwist its tame weight is two, so its coinvariants vanish integrally: `2^2-1` is a 5-adic unit.
4. The resulting quotient and action are precisely the actual D84 connecting module. The finite-coset coinduction identifications preserve the original coefficient inclusion. The comparison is not based merely on matching dimensions or abstract isomorphism classes.
5. At the simultaneous infinite endpoint, the proof uses the natural axis quotient and the actual inclusion of the augmentation square into the augmentation ideal. Its quotient has nontrivial tame weight. This establishes the required map, rather than comparing infinite coranks.
6. The local depth is the minimum of the boundary depth and the local index, including exact cancellation and both infinite values. The higher-index away generator cannot change the first nonzero valuation in the indicated comparison.
7. Nonvanishing of the global cubic class is tested against an actual operator with valuation-one Kummer coordinate and zero cubic coordinate. Its multiplier minus one is y times a unit, forcing a hypothetical primitive to be constant; an actual cubic-primitive element in the joint kernel excludes that possibility.
8. The passage to a common finite coefficient level invokes D80's finite exceptional set at the original residual cubic module. It does not assume that the full infinitely ramified module is unramified outside one finite set, or assert a uniform denominator independently at every prime.
9. The asserted actual point is `t=-799`, with `1-t=800=2^5*5^2`; the away lattice has Smith invariants 1 and 5. The section existence used for the first-cohomology fibre is supplied by that actual rational point only.

## Independent computation

The whole result JSON agrees. Checked: 12 exact integral extra-generator action examples; coupled local relations including negative exponents after clearing units; all 480 ordered bases of F5^2 and 2400 local residual spans; 1440 depth cases, including 42 exact cancellations and 36 simultaneous-infinite cases; the exact arithmetic of t=-799. The proof supplies the all-index and infinite statements; these finite checks are supporting certificates only.

The source/dependency ledger's precise scopes were reviewed: D82/D83 actual images and gauge, D77/D78/D81 natural Cartier/coinduction maps, D84 and D79 integral connecting modules, D43/D80 local duality and common finite levels, D74's conditional first-cohomology result. No new external theorem is required beyond those already independently opened and audited.
