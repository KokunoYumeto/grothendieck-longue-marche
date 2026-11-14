# Frozen central-three A6 cover and Ferrari model

The authoritative package is `code/de_a6_triple_models_manifest.json`.
Copy only its named files into one fresh directory, preserving basenames,
and run from that directory:

```sh
python de_a6_triple_cover.py > cover_replay.out 2> cover_replay.err
python de_a6_triple_model.py > model_replay.out 2> model_replay.err
```

The original runs took46.841 and2.009 seconds. Compare every mathematical
JSON field, excluding only `seconds`, and every NPZ key, shape, dtype
and array value. Hash all originals before and after the isolated replay.
The main scripts deliberately write their own new-prefix output names
in their own directory. All imported legacy modules only define classes
and functions; their main entrypoints are not executed. The legacy
kernel and model NPZ inputs are read only and protected by hashes.

There were no preliminary failures in these two model programs. Their
source and accepted outputs are frozen. The subsequent affine/source
calculations use different filenames and remain ongoing; they are not
part of this package.

The exact mathematical comparisons are recorded in the first three
sections of `research/DE_a6_triple.md`. This package proves the finite
matrix cover, its complete automorphism comparison, the universal free
image, and the explicit Ferrari model with its two projections. It does
not assert that any prescribed CM fibre lifts through the new induced
source; that requires the complete source-kernel calculation.
