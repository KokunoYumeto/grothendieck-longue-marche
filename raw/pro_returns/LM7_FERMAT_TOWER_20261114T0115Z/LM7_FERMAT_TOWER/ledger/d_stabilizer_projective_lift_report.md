# D.60: an actual lift in the remaining arithmetic character blocks

## Outcome and actual source

D.60 constructs a further continuous peripheral automorphism of the actual arithmetic source

`X60 = X/J60`, where `X = Bhat/(R50 intersect L2)` and

`J60 = (1-Pi59-Pi60) ker(Z -> Z_*)^Delta`.

The new projector retains 12,288 additional central coordinates, with 28 coinvariant coordinates. The actual arithmetic boundary vanishes on these 28 coordinates by the proved injective norm and compactification maps, after an integral peripheral homology repair. The constructed action fixes the cusp, has multiplier one, is identity on the full actual finite arithmetic group `G3`, and retains the complete D.57 source action and its compatible conjugators. The full prescribed `W_h` action, literal normalized parameter and previously established metabelian/CM comparisons remain unchanged.

The chosen D.59 homology action is replaced on exactly two specified character-orbit summands. The new action descends to the underlying D.59 quotient, with this changed action. It is not asserted to extend the previously chosen D.59 representative unchanged.

The remaining explicit small-character kernel has dimension 353,792 and coinvariant dimension 612. The full source kernel and both comparison kernels are given in the theorem. Neither the remaining invariant boundary nor full profinite realization is evaluated.

## Exact finite groups and maps

The source of the calculation is the actual D.56 quotient

`G3 -> Gdagger = A_* semidirect Q -> G_* = A_* semidirect Q_*`.

The orders are 46,656 and 3,888. The first kernel is `C3^93`; the second is the actual embedded `A4=ker(Q -> Q_*)`. The marked generators are `s=(0,S)` and `r=((1,1,1,0),R)`. These maps come from the same original source `B=C2*C3` and its actual arithmetic quotient. Odd-kernel homology identifies the pulled-back `A_*` character blocks in the full arithmetic homology with the literal homology of the order-46,656 cover. Thus the computation applies to those full arithmetic blocks through a proved integral map.

The forty nonzero unordered `A_*` characters have Q-orbit sizes 8,12,12,8. For each representative the actual source and target homology multiplicities are 96 and 8 over `F4`; cusp multiplicities are 48 and 4. Both homology and cusp maps are onto. The programs retain the edge/vertex cycle bases, literal projections, all stabilizer matrices and exact cusp columns.

The residual invariant exterior kernel has dimension `40*(96^2-8^2)=366080`. Its coinvariant dimensions by orbit are 126,196,196,122, giving 640. The full norm on these coinvariants has rank 548. The compact norm has rank 138, leaving its exact 502-dimensional kernel. The finite calculation does not identify the unknown arithmetic boundary with zero in that kernel.

## Integral projective-cover correction

For either orbit of size eight, its unordered stabilizer is `H=(V4 semidirect C3^2) times C2`. The central order-two element is the actual state 573, representing `5I`; it exchanges the character with its negative and acts semilinearly over the unramified quadratic coefficient ring. The oriented stabilizer has order 36. The certificate retains its literal generators and all semilinear action matrices.

The actual affine module is free of rank eight over `F4[A4]`, and its cusp module is free of rank four. Their projectivity, the cusp splitting, the normal-basis descent for the central involution and induction give projective integral source affine, cusp and compact modules. The target modules are projective over its actual quotient group as well. These assertions are proved integrally in the theorem; a dimension comparison alone is not used.

The compact source has dimension 48 over the quadratic coefficient ring. A projective cover of its retained four-dimensional target has dimension 16. Four projective kernel summands of dimension eight remain. The finite certificate gives their actual embeddings into affine homology, killing the small projection and the cusp radical. Orthogonal idempotent lifting and projectivity produce integral embeddings with exactly those reductions and zero integral small images.

The actual D.57 action on the compact target lifts to an invertible map of its projective cover. Its cusp-valued off-diagonal term also lifts. Making the four extra summands identity therefore gives an invertible integral homology action with the exact prescribed small action and pointwise fixed cusp homology.

This homology change is realized on the source. Its coefficient module is the exact kernel `L=ker(S -> S_*)` on the two selected character orbits. The source `S` is projective over the full finite group, and the target `S_*` is projective over its quotient. The cyclic maps on the two torsion generators and the cusp have orders `2 -> 2`, `3 -> 3`, and `36 -> 12`; their kernels are odd or trivial. The exact sequence for `L` splits on all three cyclic subgroups. Inflation-restriction gives the required actual continuous derivation, and the cusp norm equation gives a literal cusp correction inside `L`. All conjugator corrections therefore preserve their exact elements in the D.57 source. This proves an integral peripheral automorphism, rather than only a linear candidate.

## The new actual central zero

Each pair of distinct extra projective summands gives a cross-wedge module with matrix coordinate `Mat8(F4)`. Its real dimension is 128 per character pair, or 1,024 after induction over the eight pair cosets. There are six such pairs in each of the two orbits. All twelve actual norms are injective; their coinvariant dimensions are

- first orbit: 4,4,0,4,0,0;
- second orbit: 4,2,2,2,2,4.

The total is 28. The affine projectors kill cusp homology, so they induce compact projectors and compactification is injective on the selected cross modules. The repaired homology action is identity on their factors and commutes with these projectors. D.55's exact orientation identity therefore has zero right hand side after projection. Injectivity of the actual norm followed by compactification proves that the literal arithmetic cusp error has zero coinvariant class on the new module. Central augmentation corrections kill its remaining representative while retaining the full homology and D.57 maps.

The D.59 character family is disjoint from these new characters: the former is nontrivial on every original cusp class, whereas the new characters are pulled back from a quotient that kills all those cusp classes. Its previous homology action and central-zero argument remain intact.

## Exact residual and next map

The theorem gives the actual direct sum

`ker(Z -> Z_*) = moving_Delta_part + C59 + C60 + J60`.

Accordingly, `ker(X60 -> X59)=C60` and `ker(X60 -> Y)=moving_Delta_part + C59 + C60`. The full remaining class-two source map is `X -> X60`, with kernel `J60`. Its full source preimage is

`S60 = {b in R50 : image_T2(b) is in J60}`,

and `S60/(R50 intersect L2)=J60`. A nonzero element of the specified 353,792-dimensional residual, with its actual preimage under `R50 -> Z`, is an explicit source-kernel witness. The residual coinvariants have dimension 612. The next boundary lies in `(J60)_G`; it is not evaluated by the present statement.

## Reproduction and provenance

Four complete programs, outputs and JSON certificates are included:

1. `d_arithmetic_A4_twisted.py`: exact marked graph, four character blocks, homology/cusp maps and free A4 bases.
2. `d_arithmetic_A4_central.py`: full 366,080-dimensional residual comparison through 768-dimensional A4 coinvariants, exact stabilizer quotient maps and compact norms.
3. `d_arithmetic_A4_projective.py`: actual projective-cover matrices, two initially grouped extra summands and their affine idempotents/norms.
4. `d_arithmetic_A4_cross_completion.py`: splits those groups into the four retained summands and checks all twelve individual cross norms and semilinear multiplication maps.

Programs 2 and 3 use the program-1 certificate; program 4 uses programs 1 and 3. Every original run is retained. Program 3's output records its earlier grouped cross block (8,192 coordinates and 16 coinvariants); program 4 retains all six pairs and proves the final 12,288/28 result. No original output is relabelled as the later result.

For exact replay with raw input-hash provenance, the author runs each program in its own copied directory with its exact frozen input JSON. Every upstream input's entire mathematical certificate is itself independently rebuilt by its corresponding replay. All complete JSON and stdout comparisons exclude only the named `elapsed_seconds` values. Root and peer review will be recorded separately from the author replay.

The final isolated compile uses the exact current paper preamble and the existing local LuaLaTeX format. Two final passes have no overfull/underfull box or missing-character warnings. All eight final110dpi pages were actually viewed. Exact proof/PDF/image hashes and observations are retained in `audit/d60_layout/visual.json`. Root and peer audits remain pending at this author freeze.

## Integrated review and current original-task scope

D.60 realizes an integral and peripheral homology replacement on two actual arithmetic character orbits, retains the complete D57 and W_h projections, and kills twelve new central blocks of total rank12288 with28 invariant coordinates. Its actual residual small-character kernel has dimension353792 and612 coinvariants; the full remaining boundary and profinite realization remain active.

The complete proof and mathematical source programs were read by root. Actual independent replay and primary-source scopes are in the attached audit records. The full integrated build and rendered-page review follow.
