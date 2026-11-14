# Independent E.68 proof and code audit

Status: PASS after a full proof and both-program source read. This note does not claim an execution replay.

Checked exact maps:

- The twelve-map export is replayed with the same right-action convention and all 97 literal N_B words are compared letterwise.
- The full common source has 5331 points; its derived image is formed before the 4957-point coordinate-zero restriction.
- Projection onto both accepted correction images is literal. The complete order certificate proves the exact product, including the possible three-primary overlap.
- The E17 origin words are reevaluated independently and compared with the E17 export; no original-E1 correction vector is transported.
- Membership uses psi(f_i) inverse times the desired distribution value, and target minus Theta(f_i) in the translation factors. The printed order and signs agree with the implementation.
- The four E62 coordinates, three coefficient tuples and four orbifold targets give 48 distinct finite combinations per origin. The whole word fibre is the specified kernel coset inside f_i N_B-prime.
- The projected preimage DAG is substituted into the actual derived-source DAG; every returned word is in N_B-prime and every ancestor is replayed on all 5331 points.
- No automorphism or generating assertion on the unevaluated larger source, and no full-GT existence, is inferred.

## Reviewed hashes

- `sections/E_distribution_orbifold_agent.tex`: `64f01ce27a8156b223f4a40735ac0833b94bc792817334049f5be6ddfcbfb309`
- `code/a_cm_distribution_orbifold.py`: `c1d049ce24b03ed51fb62c3fbf8bd25c0cf2959fab377d3e45a9bcbd4e98a93b`
- `code/a_cm_distribution_orbifold_witnesses.py`: `113d18a58434c7841ee5330d35ca417862422d221ff53e26efbdcc8d39465200`
- `code/a_cm_distribution_orbifold.json`: `b9360b2d977d868ca952a336c830af70d32b26847bb614915bc097ce44689d2c`
- `code/a_cm_distribution_orbifold_witnesses.json`: `37252288bb8956f481b9d63785b32f649adae235b3c508db47d2307f2527d038`
