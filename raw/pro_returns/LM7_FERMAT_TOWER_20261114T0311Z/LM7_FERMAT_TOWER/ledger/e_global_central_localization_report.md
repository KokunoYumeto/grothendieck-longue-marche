# E.93: exact global central localization

The actual restriction of global central cocycles is
`(z,a) -> (z+b*L(a)*[w], alpha*L(a)*w)`, where `L(a)` is the convergent logarithmic prime sum and the genuine marked Kummer constants remain symbolic. Its entire image is `Z3^25 + C3^9 + C9^5`, its kernel is the restricted prime-exponent module outside `{2,3}`, and its cokernel is `Z3^21`.

The proof gives continuous additive sections, all kernel coordinates, and an explicit rank21 quotient map with an integral inverse. The exterior-to-Hall signed permutation is checked against both actual arithmetic operators before using the primitive Tate vector. The horizontal class retains its exact Smith coordinates and three-divisibility.

The genuine joint coefficient map sends the Tate vector to zero. Thus every ramified central Kummer cocycle has literally zero joint image. The global composite has only the horizontal rho coordinate, with full kernel `restricted primes outside3 + Z3^23 + C3^9 + C9^5`. All finite cyclic coordinates and all inverse free coordinates are retained. Vanishing of the actual source and target abelian invariant groups transfers these maps to every nonempty global section fibre without a further stabilizer quotient.

The independent program completed with all matrix identities, 1134 finite-precision localization checks and 1458 full coordinate inverses passing. The text proves the full integral assertions, including continuity and the exact choice-of-origin translation. No numerical joint origin is asserted for an arbitrary global abelian input. E.23 remains active at those particular origins and at higher nonabelian layers.

## Retained files and rerun

Run `python code/e_global_central_localization.py --source-code ../LM7_FERMAT_TOWER/code` from `research_e93`, or run the same program without arguments from the final common `code/` directory. SymPy is required. The certificate records every input hash. The completed independent peer audit is recorded below.

## Independent verification

An independent peer read the entire proof/program and every relevant actual internal map, then ran a fresh copy against five copied/hash-checked inputs. Every JSON field and the complete stdout agree byte for byte, with no exclusions. The proof audit includes both source markings, exterior/Hall transport, primitive relative line and its horizontal divisibility, all integral inverse maps and finite coordinates, uniform restricted sums, the genuine joint gauge, and the complete actual nonabelian torsor transfer.
