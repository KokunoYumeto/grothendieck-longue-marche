# D.36: order-five ordinary A6-chief obstruction

## Authoritative result and replay

The complete proof is in sections/D_order5_agent.tex. Its finite base is
\(D=(M^4\rtimes A_5)\times\operatorname{Aut}(A_6)\), with the actual deleted
permutation module \(M\) over F2, an explicit two-generator source, and an
order-five operator on the four module copies. The stabilizer of a
twenty-point permutation action has an explicit V4-valued outer character.
The resulting centerless twisted induced extension has kernel A6^20.

Every based path is retained. In particular, the boundary transport includes
the module coordinate of the source tree word in addition to the local
conjugator. The complete exact count, after subtracting every proper image,
is 360 times

    H = 61478762617650840528585632300833961934848
    L = 61478762617650840213814367698461663428608
    (H,L,L,L,L)
    H-L = 314771264602372298506240

These are counts of distinct source-kernel orbits after the explicitly
proved 360-element equivalence classes. The full ordinary centralizer
union is proved separately from the count. It cannot add another boundary
profile: the base module centralizer is the cyclic peripheral group, and
the Aut(A6) peripheral centralizers have precisely their three outer lines.

A finite lexicographic exhaustion of the four low-colour families gives
an actual order-five peripheral automorphism on a finite base. An unused
high-colour source gives a split A6^20 chief extension. Every nonidentity
power has weak solutions and no generating solution. Both groups have
trivial maximal pro-five quotient; actual products retain a specified
pro-five shadow together with both an obstructed and an admitted branch.
No conclusion selecting D.1's rational leading dimension is asserted.

The minimal replay consists of the ten files listed by
code/a_peripheral_order5_manifest.json. The command is:

    python a_peripheral_order5_replay.py

It may be run after copying those ten files into a fresh directory. It
requires Python with sympy and a C++17 compiler. The complete execution
took 10.394 seconds and passed. The manifest includes all exact input and
authoritative JSON hashes. The replay regenerates:

- the actual source module, its kernel relators and span;
- every full-outer subgroup of Aut(A6), including the exhaustive adjoining closure;
- the exact Schreier-to-surface Tietze maps;
- the framed counts with and without the fixed boundary flip;
- one actual generating surface map in each colour;
- every induced twenty-coordinate source pair and literal peripheral conjugator;
- all 25 ordered module-character transporter sets.

The authoritative surface suffix is surface20_framed. The authoritative
count suffix is boundary_framed_flip; its no-flip companion has the
opposite pattern (L,H,H,H,H).

## Retained failed route: natural SL2(F4) module

The natural two-dimensional F4 module of SL2(F4) has a one-dimensional
H1 in the tested exact source. The crossed-homomorphism constraints have
rank one over F4, leaving only one independent non-complement source
direction. This prevents the proposed two-copy multiplicity construction
in that specific module. It does not exclude another module or another
finite-group route.

The complete source calculation is preserved in:

    code/a_peripheral_a5_module.py
    code/a_peripheral_a5_module.out
    code/a_peripheral_a5_module.json

## Retained failed route: identity boundary classes

The deleted F2 module succeeds: it is simple, has endomorphism field F2,
and H1=0. Four source copies generate the full semidirect product.
The genus-five cover has an eight-dimensional nondegenerate cup pairing;
the selected order-five action gives (0,1,1,1,1) on one actual character
pair.

For identity boundary classes, the all-homomorphism counts for the two
cup types differ by 720*1296^(g-1) in the executed genera 2 through 8.
This is not a generating-map discrepancy. The complete full-outer
subgroup enumeration consists of ten conjugacy classes and 452 actual
subgroups. After every proper image is removed, the two generating
counts agree in each executed genus 2 through 6. At genus five both are

    101559958012028377497600

Thus the compact-boundary version of this candidate supplies no
obstruction. The exact calculations remain in:

    code/a_peripheral_a6_cup_count.py/.out/.json
    code/a_peripheral_a6_outer_subgroups.cpp/.out/.json
    code/a_peripheral_a6_cup_epi.py/.out/.json

No all-genus conclusion is inferred from the finite genus range.

## Superseded incomplete-framing search

The first nontrivial-boundary calculation retained the prescribed local
base conjugator but omitted the module part of the Shapiro tree-path
value. Its boundary classes did not yet represent the intended source
comparison. The missing term is

    epsilon_V((T^j-1) v(T_omega))

and appears explicitly in D.36.21. The error was reported to root and the
geometry reviewer before any theorem or exhaustion claim used those
numbers.

Every source and output from that stage was copied under an explicit
_incomplete_framing suffix, including:

    a_peripheral_surface20_incomplete_framing.py/.out/.json
    a_peripheral_surface20_boundary_incomplete_framing.out/.json
    a_peripheral_a6_boundary_search_incomplete_framing.py/.out/.json
    a_peripheral_a6_boundary_unique_incomplete_framing.out/.json
    a_peripheral_boundary_phase_incomplete_framing.py/.out/.json
    a_peripheral_boundary_configuration_incomplete_framing.json

The earlier unsuffixed exploratory files surface20.json,
surface20_boundary.json, a6_boundary_search.json, a6_boundary_unique.json,
boundary_phase.*, and boundary_configuration.json are also nonauthoritative.
None is a dependency of the D.36 replay manifest. The historical phase
witness with masks 7 and 15 belongs to that superseded search. The
authoritative corrected construction uses masks 7 and 128, retains the
full path term, and adds one fixed outer flip at the first x-boundary.

The final certificate evaluates the actual nonabelian Shapiro formula,
not just its outer character. It verifies the cycle-product class and
constructs the entire kernel conjugator on every peripheral cycle for
all five colours. This closes the exact framing comparison required by
the corrected count.

## Audit state

The parent independently replayed all ten minimal inputs in an isolated
directory in 9.376 seconds. All seven regenerated authoritative JSON
outputs agree byte-for-byte, and the protected original artifacts remained
unchanged. The parent read the complete proof and accepted the ordinary
centralizer union, kernel stabilizer/transporter comparison, finite product,
split weak lift, and all four nonidentity-power exclusions. The geometry
reviewer independently read the complete proof and accepted the same exact
comparisons; that second review did not rerun the large surface counts.
The work does not modify checkpoint05, whose manuscript scope ends
earlier.
