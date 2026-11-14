# D.63 — Integral orthogonal compact correction

## Proved result

The actual arithmetic source admits a further peripheral automorphism on
`X63 = X / J63`. It adds a 40,960-dimensional central module with 52
coinvariants. The previous literal source quotient `X62` remains a quotient,
and the complete D.57 action, its compatible conjugators, the full `W_h`
action, normalized parameter, and all proved comparisons through `W_h` are
retained.

The chosen action on `X62` may change. Its exact action on the full homology
source is

`Int(b_t,Y) beta_Y`, where `beta_Y(g) = (A0 eta(g)) alpha62,Y(g)`,

`A0 = -(1-e) T61|eU`, and `T63 = (1-e) T61 (1-e) + e`.

The derivation factors through the actual relative homology quotient
`J_infty`; on its abelian kernel `U` it is the projection `e`. Its source
conjugator changes have zero image in the retained D.57 and `W_h` targets.
The final cusp-inner element is the literal product of the D.62 source
words of length 36, using new source vectors in `S57`. This records the
change of representative rather than asserting an unchanged extension.

## Exact module and integral comparison

For each of the four actual arithmetic character orbits, compact homology
is `P = E + M`, with fibre ranks 32 and 16 over the unramified quadratic
coefficient ring. The actual intersection form is perfect on `M`.

For the new orbits, an invertible Fitting summand factoring through `E*`
would give a projective direct summand of the recorded zero-norm `M`.
For the old orbits, the projective top types of `E*` and `M` are disjoint.
Both arguments prove that the lower intersection block `D` is a unit.
Consequently the actual graph

`psi(v) = v - i_M D^-1 C(v)`

identifies `E` with `M^perp` and retains every old projector kernel.
The independently checked 128-equation Hom maps are injective, so
`Hom_G(P_*, E) = 0`. The adjoint of the actual small compact map therefore
lands in `M`, proving that the new orthogonal summand has zero small image.

The literal cusp map is onto over `Z2`: a source loop `t^36` maps to the
cube of `t_*^12`. This gives
`ker(theta_U) -> ker(theta_P)` onto. Projectivity lifts the new compact
inclusion inside the exact retained source kernel. The full unordered
Sylow norm computations prove projectivity of the cusp lattices on all
four selected components, yielding the actual affine section and the
cross projectors. No assertion of projectivity of the whole compact
lattice or the entire global cusp module is used.

The transported cross norms are:

| Character | Central dimension | Coinvariants | Individual norm ranks |
|---|---:|---:|---|
| `(0,0,0,1)` | 8192 | 12 | 4, 4, 4, 0 |
| `(0,0,1,1)` | 12288 | 16 | 4, 4, 4, 4 |
| `(0,0,1,2)` | 12288 | 16 | 4, 4, 4, 4 |
| `(0,1,0,0)` | 8192 | 8 | 2, 2, 2, 2 |

Each norm is an isomorphism from coinvariants to invariants, and the
cross module injects under actual compactification. The corrected compact
action is block diagonal on the actual orthogonal splitting. D.55's
unquotiented orientation identity therefore forces its actual cross
boundary to vanish. The previously retained 26 self norm-kernel classes
are corrected by the transported actual D.62 source words; their cross
projection is zero. Central augmentation corrections finish the exact
cusp identity, and the invertible Frattini map proves generation.

## Remaining actual kernel

`J63 = (1 - Pi63) J62` is the literal kernel of `X -> X63`.
The full source kernel is its inverse image in `R50`, with
`S63 / (R50 intersect L2) = J63`.

Its full dimension is `48w - 2560 - 5308416*kappa - 81920`.
The specified remaining small-character module has dimension 284160 and
482 coinvariants. Its compact norm has exactly rank 6 and kernel dimension
476. A nonzero vector in this module has an actual source preimage, so the
full source kernel has not disappeared. The remaining arithmetic boundary
and full profinite GT0 realization are unresolved.

## Reproducibility and attempts

Four complete programs, each with actual stdout and JSON:

1. `code/d_remaining_compact_modules.py`
2. `code/d_orthogonal_compact_cross_norm.py`
3. `code/d_all_compact_cross_norm.py`
4. `code/d_compact_splitting_maps.py`

The author independently reran each from copied sources and exact copied
inputs in `d63_author_rebuild/<program>/`. Every complete JSON object and
stdout agrees after excluding only the `elapsed_seconds` values. The
verification source, actual output and result are in
`audit/d63_replay.source.txt`, `audit/d63_replay.out`, and
`audit/d63_replay_verification.json`. This is an author replay; no peer or
parent execution is claimed here.

All attempts are preserved under `code/d63_trials/` with their actual
sources, stdout and available JSON. One initial test assumed zero old
cross coinvariants and failed. A later extractor used the wrong old
block positions: the recorded order is `E0,E1,P0`, not `P0,E0,E1`.
The final version checks the target and both affine embeddings before
extracting blocks. The first mathematically correct run also overwrote
the clock variable with a block offset; its mathematical fields and
stdout are exactly equal to the final run after excluding only elapsed
time. The initial splitting verifier stopped on a missing dictionary key;
its corrected full run is retained separately. None of these unsuccessful
attempts supplies a theorem premise.

The standalone six-page PDF uses the main paper's exact preamble and
existing LuaLaTeX format. Both final compilation passes are clean; all
six final pages were actually viewed at 110 dpi. The final equation tags,
control characters, page image hashes, PDF hash and observations are
retained in the audit records. The final source-typing clarification of
the derivation's restriction through `J_infty` has a preserved prior proof,
PDF and exact diff.


Root has now completed the full 620-line proof and 617-line source audit and four complete copied-source/input replays. Every full JSON and stdout agrees after excluding only elapsed_seconds. The independent peer has completed the full proof/source review and separately reconstructed all Hom, Sylow and cross norm maps. These records are attached separately from the exact author freeze.

## Integrated original-task scope

D.63 constructs the integral graph E to M-perp, the affine lift inside L and the actual peripheral derivation. It retains every earlier central projector kernel and all D.57/W_h data while adding 40960 central coordinates and 52 coinvariants. Its exact lower action is Int(b_t,Y) beta_Y, beta_Y=(A0 eta) alpha62,Y, with homology T63=(1-e)T61(1-e)+e. The residual J63 has specified dimension 284160 and 482 coinvariants, compact norm rank 6 and kernel 476. Its actual arithmetic boundary and the full profinite source realization remain active.
