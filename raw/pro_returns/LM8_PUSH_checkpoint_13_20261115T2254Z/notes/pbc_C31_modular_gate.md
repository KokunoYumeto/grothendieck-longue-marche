# C.31: exact modular gate for the original source presentation

Status on 2026-11-15 at 18:03 UTC: **comparison lemma proved; computational certificate still pending**. Parent independently approved the comparison before execution. No C.31 full-lift assertion follows until the original source rows and returned correction are replayed.

## The faithful torsion comparison

Let `F_n -> G` be the actual finite source presentation, with kernel `R`. Put

\[
H=F_n/[F_n,R],\qquad K=R/[F_n,R],\qquad N=|G|.
\]

Here `K` is a finitely generated central abelian subgroup of `H`. The integral Hopf exact sequence gives

\[
0\longrightarrow H_2(G,\mathbb Z)\longrightarrow K
\longrightarrow (F_n)_{\mathrm{ab}}
\longrightarrow G_{\mathrm{ab}}\longrightarrow0.
\]

Consequently `K intersect H' = tors(K) = H_2(G,Z)`. The positive-degree homology of a finite group is killed by its order: restriction/transfer through the trivial subgroup has composite multiplication by `N`, whereas that subgroup has zero positive homology. Thus `N tors(K)=0`.

The map `tors(K) -> K/NK` is injective. Indeed, if `Nk` belongs to `tors(K)`, its image in the free abelian group `(F_n)_ab` is zero. Therefore `k` already belongs to the Hopf subgroup `H_2(G,Z)`, and `Nk=0`. No selected splitting of `K`, no rationalization, and no asserted presentation of a processed Schur multiplier is used.

It follows that a relation among the target and **genuine centralizer commutators**, established in the original tail presentation modulo `N`, is an integral relation in `H`.

## Why all allowed words lie in the faithful subgroup

Write `a=alpha(s)` and `b=alpha(r)` in the finite group. The retained left peripheral frames are `B_s,B_r`. The three positive-word central differences are

\[
(B_s s)-(a B_s),\quad (B_r r)-(b B_r),\quad (ab)-(sr).
\]

Their sum is the central defect of the two framed images of `s,r` relative to `sr`. Its image in the free abelianization cancels term by term:

\[
([s]-[a])+([r]-[b])+([a]+[b]-[s]-[r])=0.
\]

Thus the target belongs to `K intersect H'`. For each retained finite centralizer element `c`, the original-source difference `(cs)-(sc)` (or `(cr)-(rc)`) is a genuine central commutator and also belongs to `K intersect H'`.

**The rows for `s^2` and `r^3` are excluded from the modular reduction.** They need not lie in Hopf torsion. The implementation retains their two positions only to preserve the established indexing; their correction coefficients must be zero. All actual correction rows are indexed from 3 onwards.

## Exact computational gate

`code/pbc_build_modular_witness.py` builds `pbc_hermite_modular_witness.g` from the unchanged original-source collector. It initializes a diagonal relation `N e_i` for every original central tail, inserts only the allowed centralizer commutator rows, and performs integer Euclidean row reduction with nonleading coefficients represented modulo `N`. The leading representative `N` is retained during Euclidean replacement so that nonunit pivots use the correct gcd with `N`; it is not incorrectly replaced by zero before that step.

The emitted proof DAG consists of original target/commutator leaves, explicit modulus leaves, original source-identity leaves, and exact subtraction/negation operations. A completed claim must satisfy all of the following:

1. Independent DAG expansion verifies the claimed linear identity modulo `N`, with target coefficient 1 and both forbidden power-word coefficients zero.
2. Every used universal source row is recomputed in the original unprocessed presentation. The abelian-suffix exterior rows are checked as the actual class-two bilinear identities, rather than confused with a single raw associativity normal form.
3. The target and allowed correction leaves are recomputed from the original words. The native positive-word collector already reproduces all 1,862 direct original GAP leaves and the combined target of the known C.27 validation case; its checked arithmetic aborts on overflow. This validation is retained separately and does not replace the new source replay.
4. Source hashes, modulus `N=product(relative_orders)`, finite-group provenance, and the resulting actual correction words are retained.

Only then does the faithful Hopf-torsion comparison turn the modular source-row certificate into the required integral centralization identity. The subsequent full gentle lift and both normalized descent evaluations require their own stated argument; they are not inferred merely from a modular matrix calculation.

## Completed validation on the earlier C.27 source

The modular variant found a correction after 2,500 source identities at modulus 6,115,295,232. Independent expansion checked its 179,583-node proof DAG and the exact integer residual's divisibility by the modulus. The standard original collector separately replayed all 211 used original-source leaves, including 200 universal identities. Finally the returned correction was checked directly in the retained **original complete central cover**, of order 293,534,171,136. All checks passed. Exact files and hashes are recorded in `code/pbc_modular_validation_report.json`.

The standalone complete-cover replay initially called a low-level inverse routine on an uncollected concatenated frame and failed its final assertion. It was corrected to normalize every word before inversion; the initial failed output is retained, and no conclusion relied on it. This development issue did not alter the modular source calculation or its proof DAG.

This is validation on the C.27 source. It does not claim that the larger iterated C.31 source has passed.

Two transparent reduction optimizations have also passed the known-source validation. `pbc_build_modular_unit.py` replaces a leading coefficient by its gcd with `N` by multiplying the entire row by an explicitly checked unit modulo `N`; a new `mul` node records the operation. Its proof DAG independently verifies and returns exactly the already checked complete-cover correction. `pbc_build_modular_scan.py` then replaces the sorted active-index queue by a forward scan: every coordinate introduced at pivot `i` has index strictly greater than `i`. On the validation source its **entire proof trace is byte-for-byte identical** to the unit-normalized trace (`pbc_modular_scan_validation_comparison.json`).

The first large modular run was stopped cleanly with exit 130 after its 500-row progress report to prioritize the validated optimizations. Its complete partial trace remains retained. No partial reduction is asserted to be a certificate.

The original power identities supply a further exact coordinate reduction. When base generators `g_i,g_j` commute and the relative power of `g_j` is trivial, original source family 3 is `order(j)*tail(j,i)`; if the relative power of `g_i` is trivial, family 4 is `-order(i)*tail(j,i)`. Their gcd supplies a one-coordinate relation. For the large source the final 72 generators have trivial relative squares and commute, so in particular all of their wedge tails have order dividing two.

The `pbc_build_modular_torsion.py` variant installs these original rows first. Its known-source correction was independently expanded, all 297 used leaves were replayed in the original collector, and the correction passed the original complete-cover check. The later coordinate variant represents each coordinate modulo its proved bound (1, 2, 3, or `N`). Its independent Python verifier derives each bound anew from the source, records the exact Bezout combination of original power identities, subtracts those identities from the expanded integer residual, and only then verifies divisibility by `N`. All 299 original/derived source leaves of the known-source test were replayed, and its returned correction is exactly the independently complete-cover-checked correction. See `pbc_modular_coordinates_validation_report.json`.

The unit-only and forward-scan large runs were stopped cleanly with exit 130 after the stronger validated variants became available. Their outputs remain retained. The current coordinate search and the boundary-prioritized positive-certificate variant do not make a negative nonlifting claim from a nonzero remainder; only a fully replayed positive certificate can settle the proposed lift.

As of 18:26 UTC the active run is `pbc_iterated_modular_boundary.g/.out`. It first inserts original exterior rows for source generators 1 and 2 on the abelian suffix, then proceeds through the other original identity families. This avoids processing all suffix-action rows before the distinguished generators. The known-source test independently expanded and replayed all 299 used original/derived leaves and returned the same complete-cover-checked correction. The prior torsion-first and plain coordinate large runs were stopped cleanly with exit 130, with their partial traces retained. The active run had passed 4,500 selected source identities, with target support 6,696 at its last reported point; this is progress, not a completed certificate.

## Computation provenance and stopped alternatives

The native original-word collector completed all 85 target/extra tasks for the 176-generator source, with 15,576 formal central tails. The combined original target has 11,196 nonzero coordinates and maximum absolute coefficient 6,867,206. Its source hash is `95fb384593bfaf97d468bbc51f11cd797484a08cb3ec3b954961085b520ffc88`; the raw normal-form output hash is `14567b223d87042a4920d387cd0ba9846dcfe761637b971dff1de6f6f112b18d`.

The first unbounded-integer run (`pbc_iterated_precollected.g/.out`, proof trace of the same stem) was deliberately stopped cleanly with exit 130 after 1,000 source identities. Its last reported target support was 10,330; proof quotients had grown to thousands of decimal digits. No success was obtained or claimed. The slower duplicate GAP original-target collection (`pbc_iterated_shortcut_v2_original.g/.out`) was also deliberately stopped with exit 130 after the native original-word calculation completed; its last completed part was the `s`-frame difference.

The two image-adapted basis attempts (`pbc_image_adapt` and `pbc_image_adapt_v2`) were stopped with exit 130 around 17:51 UTC when the original native collection succeeded. They produced no usable certificate. The second had reached 40 rewritten finite relations, which is retained in its output. These abandoned runs remain evidence of attempted computation, not evidence for C.31.

## Native exact reducer, 2026-11-15 18:40 UTC

The native modular port uses the independently validated original positive collector, GMP6.3.0 exact integers, and zlib1.3.1 gzip level1 for the full proof DAG. It was compiled with g++14.2.0, command `g++ -std=c++17 -O3 ...cpp -lgmpxx -lgmp -lz -o ...`. Assertions remain enabled. An initial attempted Boost-based compile failed because the header was unavailable; the retained implementation uses the already installed GMP instead and introduces no downloaded runtime dependency.

On the known C27 original source, `pbc_native_modular_validation_trace.jsonl` reproduced the ENTIRE parsed GAP DAG identically:120222 records,2452 raw leaves,2000 source relations, identical correction vector. The independent original-coordinate modular expander passed. This trace is therefore also covered by the previously completed independent standard-GAP original-row replay and complete-central-cover correction check for that identical certificate.

For the actual C31 source, the first5000 identity leaves and their preceding2133101 records were compared exactly with the active GAP trace after removing only insignificant spaces. They agree, normalized prefix SHA256 `d97c4581cd22f4c0027b05fc60e1c0c981fc871980294110964e75f959e219ac`; see `code/pbc_native_iterated_prefix_validation.json`. The slower uncompressed GAP boundary run was then deliberately stopped (session68408, exit130), retaining its complete partial output and trace. The native run continues with compressed proof records. No mathematical status changes: it is still a positive-certificate search, and independent original-source replay remains mandatory if a certificate is found.

### Budgeted source-order search and checkpoint controls

Native versions3--5 prioritize genuine power-consistency identities, then the original two-generator suffix exterior identities, then source-generator triples. On the known C27 original source this produces a different valid correction after1000 retained relations. Its full modular DAG was independently expanded,676 original leaves (including the coordinate-bound power identities) were replayed by the standard GAP collector, and the resulting correction was checked in the ORIGINAL complete central cover. Versions4 and5 reproduce that entire validation DAG exactly.

The actual C31 version3 attempt encountered a prohibitively long original positive-word collection before reaching250 relations. It was stopped, with its command/output retained. Versions4 and5 impose a two-million-step budget PER collection call and omit any original identity whose collection exceeds that budget. Such an omitted row never becomes a proof leaf. The search is therefore explicitly only a positive-certificate search; failure or a remaining target does not imply nonlifting. The positive Hopf-torsion certificate gate is unchanged.

Version5 adds shared-filesystem checkpoint controls because separate command sessions have isolated process namespaces. Creating `code/pbc_native_modular_v5_iterated_trace.jsonl.gz.pause` pauses at a safe point, closes the gzip footer, and preserves the live basis/collector state. Removing that marker resumes by appending a fresh gzip member. A pause with149167 complete records was successfully decompressed and hashed, and then resumed; see `code/pbc_native_v5_pause_validation.json`. A `.stop` marker requests graceful termination. Sending a generic execution-tool interrupt to earlier versions did not reliably permit C++ stack unwinding, so archival framing is treated separately.

Every stopped incomplete native compressed stream is retained byte-for-byte as `.incomplete_stream`. `code/pbc_close_interrupted_gzip.py` reconstructs a VALID gzip of every available complete JSONL record and preserves a possible trailing partial decoded record in `.partial_record`. The corresponding `.archive.json` gives raw, decoded, and closed-prefix hashes and explicitly states that no success is claimed. This changes archive framing only; it fabricates no proof record and supplies no mathematical completion.

The currently active version5 provenance is `code/pbc_native_modular_v5_run_provenance.json`. All earlier source files and outputs remain retained. C31 is still Open as of the checkpoint09 preparation.

### Checkpoint09 stable prefix

The only active search, native version5 (execution session44788), was paused via its filesystem marker before18:54UTC. Its closed gzip prefix contains3653272 proof nodes plus the source header, and the live basis/collector state remains in that process. The last250-row progress report was2750 original relations,2747 counted large-modulus pivot improvements, and6547 target coordinates remaining. The current exact values and hashes are recorded in `code/pbc_checkpoint09_trace_manifest.json`. No success is claimed. The pause marker must remain in place until root confirms checkpoint capture; removing it resumes the SAME live calculation and appends the next gzip member.
