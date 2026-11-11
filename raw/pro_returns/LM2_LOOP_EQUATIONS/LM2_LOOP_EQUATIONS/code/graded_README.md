# Reproducing the graded calculations

Requires Python3 and SymPy. All computations use exact integer, rational, or finite-field arithmetic. Run the successful computations in this order from this directory:

```
python graded_dimensions.py > graded_dimensions.out
python graded_pentagon_witness.py > graded_pentagon_witness.out
python graded_first_lifts.py > graded_first_lifts.out
python graded_rational_jets.py > graded_rational_jets.out
python graded_lazard13.py > graded_lazard13.out
python graded_braid_transfer.py > graded_braid_transfer.out
python graded_preprint_audit.py > graded_preprint_audit.out
```

Each writes its complete structured output alongside the program. The dimension calculation gives exact rational kernel dimensions and independently checks them using Witt characters. Its modular basis-selection step only proves independence; the matching characteristic-zero character formula proves spanning. No rational rank is guessed from a modular rank.

`graded_greedy_jets.py` and its output retain a failed choice of lift coefficients. The failure occurs in weight10 for that particular earlier choice, and does not imply nonexistence of another lift; the successful coupled computation supplies one through12.

`graded_global_attempt.py` and `graded_block_attempt.py` retain larger elimination approaches that were interrupted. They are included for the audit of every program run, but are not part of the reproduction sequence and their partial outputs support no final mathematical claim. The successful rational-jet program imposes the additional even-coefficient-zero ansatz and verifies all equations directly, so it does not depend on those interrupted attempts.

The finite group checked in `graded_lazard13.py` is the class12 BCH/Lazard group on the 747-dimensional truncated free Lie algebra overF13. Its order is13^747. Verification uses its exact finite algebraic presentation and does not enumerate its elements. This computation does not establish an infinite pro-13 lift, a full profinite lift, or a result about one of the separate small congruence quotients requested in the prompt.

The additional braid-transfer program verifies the actual pure-braid action and center needed for B.g15, so the finite example is excluded from the arithmetic outer image by a genuine finite group pentagon obstruction. It still supplies no infinite GT0 lift.
