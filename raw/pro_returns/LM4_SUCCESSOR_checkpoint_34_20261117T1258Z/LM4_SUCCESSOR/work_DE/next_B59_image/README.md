# Exact class-two and class-three common-image certificates

These files support **B.60** and **B.61**. They concern the specified tetrahedral and cyclic centralizer subgroups inside the pure sphere mapping-class group on twelve marked vertices. B.61 constructs actual words in the two subgroups with the same nonzero image in `P/gamma4(P)`, also killed by the twelve rigid-seven tests through class three. The words differ in `P`. The computation neither constructs an element of the actual profinite intersection nor constructs a compatible tower through every nilpotency class.

## Reproduction

Run the scripts with Python 3.12 and SymPy 1.14.0 from this directory. All calculations that support the conclusions use exact integers, rationals, algebraic-number fields or certified rational intervals. The `.out` files contain actual standard output. The JSON files retain the coefficients, words, matrices and interval witnesses. Paths to earlier B.56–B.59 inputs resolve relative to the script location.

The class-two scripts are:

1. `check_bracket_span.py`: evaluates the tetrahedral bracket identity giving `2w`.
2. `check_cyclic_bracket_span.py`: evaluates the cyclic bracket identity giving `w`.
3. `check_two_w_rigid.py`: proves that the displayed tetrahedral word is outside the full rigid-seven kernel by an exact finite Burau representation.

For the class-three result, run these dependent stages in order:

1. `certify_full11_monodromy.py`: extends the thirteen tetrahedral meridians to all eleven finite normalized strands. It uses exact Sturm isolation on all 78 segments, checks all 55 pair linkings and literally recovers every earlier six-strand word on projection. Recorded runtime 307.36 s.
2. `certify_cyclic_and_transport.py`: verifies the exact common icosahedral configuration in a degree-eight field, certifies homotopies to rational parameters and root approximations, computes the six cyclic meridians and both base transports by exact Sturm isolation, and checks every transported word and pair linking. Recorded runtime 25.92 s.
3. `nilpotent_derivations.py` and `magnus4.py`: reusable exact Artin/Magnus/BCH engines, with executable internal checks. They represent logarithm layers as `D1`, `2D2`, `24D3`, and reconstruct all 990 degree-three coordinates in the full Artin derivations.
4. `check_degree3_upper_obstruction.py`: evaluates the initial discrepancy `a*b0^-2` and a deliberately larger tetrahedral correction space. Its exact rational solution makes this upper-bound obstruction inconclusive; it is not the final existence proof.
5. `check_degree3_actual_corrections.py`: retains all thirteen tetrahedral generator logarithms, 78 binary brackets and ternary brackets, including the lower-layer null relations. It solves the common-image equations exactly over the rationals.
6. `check_degree3_rigid_obstruction.py`: additionally imposes all 70 coordinates of one rigid-seven degree-three test. The exact rational solution satisfies every 1060 equation. Conjugacy by the tetrahedral action later supplies all twelve tests.
7. `collect_integral_class3_lift.py`: collects the rational solution into actual finite power-commutator words, using the multiplier `D=2545920`. It checks universal free class-three BCH collection and integer exponents; it does not take rational roots of group elements.
8. `verify_integral_class3_lift.py`: independently evaluates the resulting explicit integer words in the actual common-base Artin logarithms. This is the decisive final check. It checks all 13 generator powers, 78 commutator powers, 728 tetrahedral triple powers and 39 cyclic triple powers, reconstructs all 990 coordinates, and verifies common-image equality and rigid cancellation. Recorded runtime 25.5 s; the independent root rerun took 25.47 s and is reviewed in `../../records/root_review_B61.md`.

The outputs of stages 4–6 distinguish modular pivot selection from exact rational membership. A rank equality modulo 101 alone is never used to assert rational membership. Their selected inverse matrices and complete rational identities are retained. The existence conclusion ultimately uses stages 7–8, so it does not require a completeness theorem identifying a rational correction span with an integral subgroup intersection.

## Complete word encoding

`class3_common_lift_words.json` specifies the finite words by integer powers in an explicit order. Tetrahedral indices are 1–13; cyclic indices are 0–5. The commutator convention is `[x,y]=x*y*x^-1*y^-1`; the JSON supplies recursively bracketed trees for each standard Lyndon triple. The definitions are

```
a  = [e1*e2^-1*e3,e5]
b0 = [f0,f1]^-2 [f0,f2]^-1 [f0,f3]^-1 [f0,f4]^-1
     [f0,f5]^-1 [f1,f2] [f1,f5]
A  = a^D U^-1
B  = b0^(2D) V
```

Here `U` has 13 generator powers, 78 commutator powers and728 triple powers; `V` has 39 triple powers. Their common degree-two image is `5091840w`. The multiplier need not be minimal. The JSON records the correction coordinates, word factors and complete common-base braid data references, allowing evaluation without expanding the potentially enormous integer powers into individual letters.

The common class-three element centralizes the actual `A5` in the corresponding quotient: the first word centralizes the tetrahedral subgroup, the second the chosen order-five subgroup, and those generate `A5`. Its nonzero primitive degree-two coordinate gives the asserted injective procyclic image in the completed quotient. This quotient assertion does not supply an element of the full profinite centralizer.
