# E54: complete joint A6–signed source and target replay

The authoritative statement is `sections/E_a6_joint_agent.tex`. The new
program prefix is `de_a6_gl_`; the earlier joint A6/A5 base is
`de_a6_a5_common_source`. Every earlier E48 file remains unchanged.
The package is frozen by `code/de_a6_gl_manifest.json`.

## Exact map and scope

All source maps begin with the same B=C2*C3 and the same ordered pure
generators x=(r^-1s)^2, y=(sr^-1)^2. The exact common source is

    G_A6 ×_{Q30} G_L,

where Q30 has pure image A5^3×(Z/30)^2, and its three actual A5 epikernels
are4,12,18. The second factor records ordinary ordered exponent sums.
The joint perfect residual is C_A6×_{A5^3}C_L. Its perfection is proved
by the complete three-central-bit pullback presentation, retaining all
30 independent generator-lift signs.

The exact image of I=gamma5(Nhat)∩R_nil(H) is P′×_{A5^3}C_L. This gives
simultaneous corrections retaining the old D23 value, the signed value,
and every admitted E43/E44/E47 nilpotent H-boundary value. Common-source
generation uses the actual central kernel over the old source and its
specified abelian coordinates. It does not assume any source-kernel
invariance that has not been proved by the literal Q576 comparison.

The actual joint four-strand target T_{L,A6} has maximum solvable
quotient the old specified S_L of order96. Its actual common target
with T23 is T23×_{S_L}T_{L,A6}. All864 finite points survive; the full
coherent boundary assertion concerns the432 multiplier-one points.
The later E53/E55 uniform symplectic family is not part of E54.

## Stable source chain and exact signed lift

Compile the supplied C++ files with C++17 and optimization, using the
unchanged `de_a6_schreier.cpp` include. Conventional executable names
are obtained by dropping `.cpp`, except the engine is
`de_a6_schreier_fast`.

The existing joint-base chain is `de_a6_a5_common_source.bin` (there is
no `_order.bin` suffix). Its original order log is
`de_a6_a5_common_source_order.out`. The compression and literal maps
are reconstructed by `de_a6_a5_common_source.py`; all actual point
intertwiners are in its JSON. Replaying its supplied complete chain
avoids repeating discovery.

Run these in the isolated copied `code` directory:

```sh
python de_a6_a5_common_source.py
./de_a6_schreier_fast --replay de_a6_a5_common_source.bin
python de_a6_gl_prepare.py
./de_a6_gl_kernel de_a6_gl_model.bin de_a6_a5_common_source.bin de_a6_gl_kernel.json
python de_a6_gl_kernel_replay.py
```

The exact signed lift freshly replays the base, evaluates all1154659
Schreier relators, and closes their entire binary image under s,r.
The answer has dimension42. The separate Python program checks all42
literal basis words, all84 conjugations and the exact rank-two Q4
quotient comparison against the accepted E50 signed map. The full
lift took404.946 seconds; its Python replay took2.764 seconds.

## Smaller quotient control and the complete epikernel comparison

The following control is needed for the statement that the smaller
E45 source does not contain the whole common quotient. It is not used
as a negative old-fibre assertion.

```sh
python de_a6_gl_lower_chain_prepare.py
./de_a6_schreier_fast --replay de_a6_gl_lower_chain.bin
./de_a6_gl_kernel de_a6_gl_lower_chain_model.bin de_a6_gl_lower_chain.bin de_a6_gl_lower_kernel.json
python de_a6_gl_lower_compare.py
```

The complete lower chain has128833 final relations. Its signed kernel
also has dimension42. The specified common orders are1350 and5400;
the actual full source has index216000 in the smaller fibre product.
The earlier wrong-metadata-key attempt is preserved under
`de_a6_gl_lower_failed_initial_field.*`; do not rerun it.

The complete actual epikernel comparison is:

```sh
python de_a6_gl_epikernels_prepare.py
./de_a6_schreier_fast --replay de_a6_gl_A5_source.bin
./de_a6_gl_epikernels de_a6_schreier_full_ordered.bin de_a6_gl_epikernels.input de_a6_gl_A6_factors.json
./de_a6_gl_epikernels de_a6_gl_A5_source.bin de_a6_gl_epikernels.input de_a6_gl_A5_factors.json
python de_a6_gl_presentation_gate.py
python de_a6_gl_common_quotient.py
```

The first presentation has865049 final relations; its factoring
epikernels are exactly4,12,18. The second has23945 relations and
factors0,2,4,10,12,16,18. Each rejected epikernel has a saved actual
relation word, independently replayed in both source and rejected
target. The positive conclusions use every relation, not only the
saved negative witnesses. The final program proves the literal Q15
and Q30 maps, their pure images, the ordinary exponent maps and the
maximum common-quotient equalities by the independently certified
joint source orders.

The two ordinary originals really occur among the strong generators
used by these complete presentation calculations; the small
`de_a6_gl_presentation_gate` certificate records that input condition.

## Complete central pullback and all signs

```sh
python de_a6_gl_central_prepare.py
./de_a6_gl_central de_a6_gl_central_model.bin de_a6_schreier_residual_derived.bin de_a6_gl_central.json
python de_a6_gl_central_replay.py
python de_a6_gl_central_signs.py
python de_a6_gl_boundary.py
```

The exporter reconstructs the ten C_A6 generators as literal F words
through every nested accepted chain. It checks all22824 required word
ancestors in the full9462-point source. The complete pullback retains
all720615 Schreier relations and all10 original-to-normal-form
relations. Its13-column abelian relation matrix has full rank13.
The independent replay checks13 actual identity words and their three
SL2 values using direct2-by-2 matrix multiplication.

The raw field `original_generator_sign_freedoms:10` counts generator
slots. The complete binary sign dimension is30, explicitly checked
by `de_a6_gl_central_signs`. All30 elementary invertible column changes
are retained; the original complete-run data are unchanged.

The full pullback run took220.675 seconds; direct replay1.829 seconds;
the H-commutator and literal gamma5(N) preimage certificate1.180 seconds.
The latter proves the exact rank6/rank6 quotient actions required by
the compactness correction, with all source words and matrices saved.

## Joint four-strand target

```sh
python de_a6_gl_target_prepare.py
./de_a6_schreier_fast --replay de_a6_gl_target.bin
./de_a6_schreier_fast --replay de_a6_gl_target_derived1.bin
./de_a6_schreier_fast --replay de_a6_gl_target_derived2.bin
./de_a6_schreier_fast --replay de_a6_gl_target_derived3.bin
./de_a6_schreier_fast --replay de_a6_gl_target_derived4.bin
./de_a6_subgroup_checks de_a6_gl_target_derived3.bin de_a6_gl_target.input de_a6_gl_target_normal.json normal
python de_a6_gl_target_certificate.py
```

The faithful quotient after its perfect free kernel has781 points.
Its subgroup indices are1,2,6,96,96, with complete relation counts
421070,491742,543926,377977,399945. Every subsequent input is a literal
mixture of the previous strong generators, and the independent final
program reconstructs all mixture words and checks every word DAG.
No intermediate generation claim is inferred from mixtures alone.
The final equal-order inclusion proves the index96 subgroup perfect;
747 original-generator conjugations prove it normal. Its actual map
to the old96-element Cayley table is checked on every strong generator.

The mixture producers are retained in
`de_a6_gl_target_derived{2,3,4}_input.json/.npz` and can also be reproduced
by `de_a6_schreier_mix.py` from the immediately preceding certificate.
The final target order is2^403·3^163·5^117·7^8·11^3·13². Its quotient map
to S_L is the literal projection onto the last251 points followed by
the accepted signed quotient; equal group orders are used only after
this actual map is present.

## Dependencies and prior root gates

The manifest includes the static local import closure, literal data
dependencies and every named hash dependency in the new outputs.
Existing data are supplied read-only. Do not execute legacy dependency
main programs merely because they appear in the import closure.
The earlier E48 complete chain and quotient root audits are
`audit_a6_full_chains_root.json` and
`audit_a6_full_quotients_root.json`; the manifest checks their recorded
hashes against every reused file. All unchanged gates can be cited
directly. The new presentation evaluators still need their new
all-relator evaluations even when the underlying chain has already
passed a root replay.

Compare mathematical JSON records and every literal NPZ array.
Elapsed-time fields and captured input hashes of regenerated timing
records can differ; all originally supplied artifacts must remain
unchanged in the protected source directory. New isolated stdout
should use a root-specific suffix. Replaying existing complete chains
is sufficient; generator discovery is not required.

## Primary input and prefreeze provenance

The original primary source is Robert Steinberg, *Lectures on Chevalley
Groups* (Yale,1967), §7, Theorem10 and Corollary2(b):

https://www.math.utah.edu/~ptrapa/math-library/steinberg/steinberg-yale-notes.pdf

The corollary appears at PDF indices88–89 and explicitly identifies
SL_n(k)→PSL_n(k) as universal under its stated conditions. F5 satisfies
them. Root independently opened the theorem, corollary and page images;
the bib key `DE_Steinberg1967` is verified. The exact model map from
PSL2(F5) to A5 is the action on its five Klein-four subgroups.

The three gathered row separators and the exact target addition are
recorded in `DE_a6_gl_prefreeze_changes.json`. The prior draft was
reconstructed by reversing that patch after preservation was requested;
`DE_a6_gl_before_target_reconstructed.tex` is explicitly labelled as
such. No old mathematical certificate or earlier failed attempt was
rewritten.
