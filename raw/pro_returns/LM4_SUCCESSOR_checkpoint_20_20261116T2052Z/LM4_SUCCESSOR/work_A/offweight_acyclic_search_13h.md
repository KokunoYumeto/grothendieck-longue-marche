# Bounded off-weight acyclic-coefficient test

This is a completed negative search for a particular mechanism, not a
nonexistence theorem for a full negative lift. No formal statement is added.

## Proposed mechanism and its limitation

We sought an actual noncentral simple coefficient of a different binary
type from the retained 108-dimensional module, occurring in pairwise
products of its weights, for which `H^1(Pi,M)=0`. Such a coefficient would
remove the discretionary source one-cocycles in the finite-to-full action
comparison. It would not automatically give a nonzero action square:
the source boundary restriction calculation also forces `M^tau=0` in the
acyclic case. The remaining possible obstruction would be the simultaneous
reflection/normalizer lift, with the allowed lower frames properly retained.

## Exact finite calculation

The input is the actual module in `check_Q6_forced_frame.py`, with
`H=N semidirect Q6`, `N=F7^13`, `Q6=S3 x A4`, and the three Frobenius
orbits of its 36 character weights. There are exactly 108 distinct weights.
Their unordered pair sums have 3,871 distinct values, including zero.
The 3,870 nonzero values form 69 `Q6`-orbits.

| Orbit size | s-fixed weights | r-fixed weights | H1 dimension for the trivial little-group character | Number of orbits |
|---:|---:|---:|---:|---:|
| 18 | 4 | 0 | 5 | 3 |
| 24 | 0 | 3 | 2 | 6 |
| 36 | 0 | 0 | 6 | 3 |
| 36 | 4 | 0 | 8 | 15 |
| 72 | 0 | 0 | 12 | 42 |

For an orbit of size `d` and the indicated trivial little-group module,
the actual source order-two and order-three matrices have invariant
dimensions `(d+f_s)/2` and `(d+2 f_r)/3`. The possible monomial scalars
have seventh-power order; hence a fixed source weight has scalar one
for both source factors. The free-product cohomology sequence, with no
global invariant vector, gives the difference of these dimensions as
`dim H^1(Pi,M)`.

This also excludes acyclicity for every simple constituent over an
algebraic closure, not just the displayed monomial choice. The little
groups have orders 4, 3, 2, or 1. A group of order a power of two has
only the trivial simple module in characteristic two. For the order-three
little group, a nontrivial character removes the three fixed-weight
contributions to the `r`-invariants and leaves the `s`-invariants
unchanged; the H1 dimension rises from 2 to 5. Descent to the binary
field groups these constituents and cannot create vanishing cohomology.

Thus **no nonzero pair-weight simple coefficient is acyclic on the
actual source**. In particular there is no self-dual, c-stable acyclic
candidate in this family. We stop the proposed branch at this point.
There is no conclusion about arbitrary higher tensor constituents,
other finite heads, norm solvability, cofinality, or the main existential
involution problem.

## Reproducibility

- Producer: `work_A/code/check_Q6_offweight_acyclic.py`.
- Genuine stdout: `work_A/code/check_Q6_offweight_acyclic.out`.
- All orbit representatives and c/Frobenius/duality data:
  `work_A/Q6_offweight_acyclic_classification.json`.

The producer executes only the actual finite-head preparation prefix,
does not change its input, and does not invoke any lift search.
