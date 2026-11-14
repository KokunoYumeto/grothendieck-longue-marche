# Original central-stabilization trial provenance

The exact command in d_cm_second_central.command.txt was executed before the frozen D49 verifier was written. Its actual saved output is d_cm_second_central.json. The tool result printed the following stdout (transcribed from that original result; no rerun was made for this provenance note):

```json
{
  "shape": [
    193,
    386
  ],
  "smith_multiplicities": {
    "1": 193
  },
  "elapsed_seconds": 0.16194891929626465
}
```

The copied d_cm_central_base.py is an imported source dependency of that trial, copied from the then-frozen D48 program. It was executed in the trial namespace under redirect_stdout(io.StringIO()); its actual generated certificate is ../code/d_cm_central_mixed.json, because the copied source writes that fixed basename. Its SHA256 is6e2cdf62166c09bb0d2bf5ebccb83bbf910db92d7894c66c12164deb1f6c648a (elapsed_seconds0.536). It differs from the archived D48 certificate only in the recorded elapsed time. The helper's stdout was intentionally captured and discarded at that time, so no historical helper .out is claimed or reconstructed. Its role in this raw archive is an imported dependency, not an independently delivered runnable verifier.

The raw files were subsequently moved from D49_EXPERIMENTS/code into raw_trials to separate this first experiment from the frozen independent verifier. The exact original command retains its original paths. The frozen code/d_cm_fixed_parameter.py reconstructs the graph from the saved D48 certificate and independently verifies both Smith and Hermite images; it has its own actual stdout and a fresh copied-input rerun. No raw file is part of the D49 frozen-file manifest.
