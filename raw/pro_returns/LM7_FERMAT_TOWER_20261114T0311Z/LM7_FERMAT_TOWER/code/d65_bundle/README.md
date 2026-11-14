# D65: the divided integral compact source correction

The frozen proof is `sections/D_divided_compact_source.tex`. It gives the actual new source quotient, both integral maps before division, the complete lower-action comparison, and the remaining kernel.

## Reproducing the finite certificates

Use Python 3 with NumPy. Copy the complete top-level `code` directory to a fresh directory before running; the programs write their own named JSON result beside their source. All inputs are included, with exact provenance in `input_manifest.json`.

Run the following programs in order, capturing each actual stdout to the same basename with `.out`:

1. `d_compact_projective_trace.py`: the complete finite affine isometry spaces and projective trace diagnostic.
2. `d_compact_full_trace.py`: every full endomorphism trace column.
3. `d_compact_rigid_source.py`: actual finite conjugator words and marked Bass--Serre compact action.
4. `d_compact_permutation.py`: literal permutation-module comparison and inverse.
5. `d_compact_integral.py`: actual graph, projective split, integral complementary action, signed exterior norm and endomorphism trace modulo four.
6. `d_compact_divided_correction.py`: exact kernel coinvariants, source-s image, all correction columns and right inverses.
7. `d_compact_integral_exterior.py`: independently implemented real exterior action, its primitive embedding/inverse, and the full odd-scalar projector.
8. `d_source_centralizer_norm.py`: literal finite centralizer/fixed-vertex maps and cyclic vertex-freeness.

For exact comparison of downstream input hashes, retain each freshly generated output separately, compare every mathematical field to the frozen result, and restore the frozen raw result before its downstream consumer. The recorded author replay does exactly this and excludes only `elapsed_seconds` values from whole JSON/stdout comparisons. All upstream calculations are separately rebuilt. `audit/d65_replay.py` additionally checks the original workspace source paths; the eight main programs themselves use only local included files.

The actual failed integral serialization run and two earlier successful assertion-stage runs remain under `code/history`. The failed first PDF capture is retained under `qa/history`. They are provenance, not successful final certificates.

The full original profinite realization is not completed: the theorem retains the exact nonzero kernel and its next compact test.
