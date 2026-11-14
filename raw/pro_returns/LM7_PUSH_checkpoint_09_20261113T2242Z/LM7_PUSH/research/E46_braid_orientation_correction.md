# E.46 based-action display correction

The initial, unintegrated draft of E.46.14 printed

`sigma'_i = f(y_i,sigma_i^2) sigma_i^lambda f(y_i,sigma_i^2)^(-1)`.

The actual convention used throughout E.29 and E.38, and in
Nakamura--Schneps (1.1), is

`sigma'_i = f(y_i,sigma_i^2)^(-1) sigma_i^lambda f(y_i,sigma_i^2)`.

The root caught the reversed conjugation while comparing the draft
with the final paragraph of E.29 and Theorem2.1(2.1) of the opened
Lochak--Nakamura--Schneps2026 primary text. The display was corrected
before its first inclusion in the manuscript. The earlier displayed
formula is retained above as the precise superseded passage.

All eight evaluation pairs, the induced source, and every computed
subgroup remain unchanged. The proof matches the value of f with the
actual Galois word in each coordinate, so it also matches its inverse.
The corrected formula consequently gives the exact Galois generator
images used in the surjectivity and relation proofs. No calculation
of primed-generator arrays had used the reversed display.
