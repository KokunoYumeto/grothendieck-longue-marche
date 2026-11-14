# Local stratifications: F.31–F.34

The complete LaTeX fragment is `F_local.tex`. It uses only standard LaTeX, amsmath/amssymb and the ordinary `proof` environment. It cites the single key `Mather1970Local` in `local_refs.bib`; there are no custom macro dependencies. Root owns compilation and checkpoint persistence.

## Decisions and proofs

- F.31 proves restrictions really are global stratifications, including local finiteness of split components and their frontier condition. The presheaf is separated. The atlas on a circle obtained by deleting two different points is compatible but has no global section: its forced connected open stratum has two germs at the marked point. Sheafification is compatible local atlases modulo common refinement. Leaf topology is reconstructed by plaques.
- F.32 gives the actual local model `D_r = coproduct_chain closure(S_first)` and proves all Segal maps are homeomorphisms. Matching germs is indispensable. It also corrects two asides: degeneracies identify their repeated-entry summands, and under this literal topology the first-vertex map is finite étale on all of `D_0`, not just on `D_0*`. Normal crossings supply manifold closures and Boolean posets, not this latter covering property.
- F.33 constructs a one-ended infinite-genus surface and adds its point at infinity. The resulting two-stratum compact metrizable space satisfies a–e. Punctured-tail first-homology transition images strictly decrease at every stage, which is incompatible with a constant pro-group. Axiom e alone therefore does not provide a stationary conical link.
- F.34 defines full tube and flag pro-topoi, proves the binary neighbourhood gluing universal property by filtered mapping categories and finite pseudolimits, and proves controlled tube/flag descent. The additional hypotheses are explicit: locally compact paracompact Hausdorff, finite depth, compact recursively conical links, locally trivial link bundles, and compatible retraction/radius control data. Arbitrarily shrunken radial tubes are cofinal by compactness of links and continuous positive minorants. The local-finiteness synchronization step is spelled out, so no infinite product is exchanged with a filtered colimit without justification.

Full sheaf topoi remain pro-objects even in the conical case. Their homotopy and covering reflections can have fixed link models. No asphericity is needed for full geometric gluing. Replacing every elementary homotopy type by its fundamental groupoid requires those elementary types to be 1-types; aspherical strata and all iterated-link fibres are a sufficient geometric criterion. Reconstruction uses the homotopy colimit of classifying spaces and the full flag diagram.

## Requested tests

For `(S²,p)`, the open and closed strata are contractible, but the punctured tube is `S¹ × (0,ε)`. The homotopy pushout is the suspension of `S¹`, hence `S²`. The ordinary constructible-set arrow topos and the ordinary groupoid colimit have contractible shape; the full link diagram retains `H₂ = Z`.

Scan 190 explicitly has seven strata, so it depicts three half-lines in the plane, including the three sectors. The origin link is a circle divided into three points and three arcs. The incident poset has 7 vertices, 12 strict comparable pairs, and 6 strict three-chains. Its proper part is the hexagonal incidence cycle. A tripod-only interpretation gives the wrong number of strata and the wrong link.

## Reading and literature checks

Original scans visually inspected: 181, 182, 185, 187, 188, 189, 190. The transcription of 181–190 was read in full. Eight entries are in `local_readings.csv`, including every ambiguous symbol on which the mathematical definitions depend. For d, the adopted connected-germ meaning is the connected neighbourhood-basis meaning explained explicitly at scan 182.

Mather's 1970 author-hosted scan was opened at `https://web.math.princeton.edu/facultypapers/mather/notes_on_topological_stability.pdf`. Section 7, Proposition 7.1, Corollaries 10.2–10.6 and Proposition 11.1 were cross-checked in `https://webhomes.maths.ed.ac.uk/~v1ranick/surgery/mather.pdf`. The author PDF supplies verified title and year; the AMS 2012 page was blocked, so the bibliography does not pretend that version was opened. STRATA C.3/C.5/C.6 were read and their relevant categorical calculation is checked inside F.34; it is not used in place of the geometric full-topos argument.

## Computations

Run `python work/montpellier/code/local_strata_checks.py`. It checks exact rational homology, the three-ray incidence counts, all finite Segal bijections through degree six, the circle and sphere Betti numbers, and finite certificates of the infinite-genus decreasing images. The proofs establish the unbounded assertions. Run `python work/montpellier/code/local_registers.py` to regenerate the exact-schema CSVs.

## Final scope corrections

The full 2-category of topoi retains arbitrary natural transformations. Accordingly F.34 now uses mapping categories and finite pseudolimits in Cat, not mapping groupoids. The terminal subspace W carries its subspace topology and is held fixed in each Čech/flag diagram. Elementary terms include every tube condition in the flag; taking W equal to the terminal stratum makes that last condition redundant. There is no undeclared inclusion between disjoint strata when a terminal vertex is dropped. Only a specified inclusion of W into W-prime, or an additional specified conical retraction, supplies such a comparison.
