# B.26: spherical catalogue completed

**Proved and executed.** The four complete catalogues contain 10, 30, 20, and 57 finite-subgroup conjugacy classes for types (0,3), (0,4), (0,5), and (0,6). All local orders, group permutations, orientation signs, puncture stabilizers, section multipliers, centralizers, maximal extensions, and group orbits are retained in the JSON outputs. The CSV files list every conjugacy class separately.

The proof is `b26.tex`. It enumerates all positive-Euler-characteristic quotient orbifolds, proves n<=nu for the infinite families, and identifies decorated quotients up to precisely their stratum-preserving homeomorphisms. Finite permutation groups verify the presentations; injection of all local groups and N*chi_orb=2 prove that these are the full orbifold groups. Section data come from the complete lifted mirror coset graph and the cone/corner cosets, not from sampled numerical points.

Reproduce by running `python work/part_b/code/catalogue_spheres.py`. The retained stdout is `code/catalogue_spheres_stdout.txt`. The program also recomputes the independent six-column multiset comparisons against B.23 and B.25; both pass. Those prior CSV files are included inputs.

Remaining B(f) types at this checkpoint: punctured tori with 2–4 punctures, genus two with 0–2 punctures, genus three closed, and explicit abelian finite-outer-subgroup/extension ambiguity bookkeeping. The raw finite-outer-subgroup datum does not choose an extension in the torus case, as proved in B.22. No completeness claim has been made for these outstanding cases.
