# F.9 — exact common kernel element

The seven-point restriction maps used in the F.7 centralizer attack are noninjective. All twelve maps have the same kernel by F.8, and the exact word

\[
w=m_{-1}m_i m_1^{-1}m_i^{-1}
\]

lies in that common kernel. The source is the specified tetrahedral ramification complement, with basepoint `5+4i` and Gaussian-rational square lassos of halfwidth `27/1000`. Winding about `-1` sends `w` to one. This detects the word in the full profinite source and makes its entire procyclic closure a full copy of `Zhat` in the completed kernel.

The joint kernel of all thirty-six maps in F.7.9 equals the joint kernel of the twelve seven-point maps. Each six-set is one selected `C5` five-cycle together with one fixed pole; add the other fixed pole to obtain its seven-set. Literal forgetting of the added pole gives the exact factorization of the six-point map. There are exactly two such six-sets for each of the twelve seven-sets. The supplemental exact certificate lists all twenty-four label containments and forgetting maps. Functoriality proves the same kernel equality after full profinite completion. Thus `w` satisfies every one of the thirty-six constraints.

## Exact comparison of maps

The seven functions in F.9.2 are the F.8 subset `{0,1,2,3,4,7,10}`, in that order. The exact finite certificate checks the corresponding tetrahedral matrices and all 144 products. Their common ramification set is infinity together with the zeros of `z(z^4-1)(z^8+14z^4+1)`.

The unique Möbius map taking the first, second, and seventh coordinates to `0,1,infinity` gives an actual map `Phi:X→Conf_6(C)`. Appending infinity and taking the labelled Möbius quotient gives the exact factorization `f_I=q∘Phi`. The closed ordered configuration paths define pure braids; their inclusion in `B6` is the injection from the ordered-to-unordered configuration cover. Thus an identity in `B6` gives an identity under the specified map to `PΓ_(0,7)`.

## Executed exact certificate

`code/seven_point_kernel_f9.py` uses rational and Gaussian-rational arithmetic throughout. It certifies 18 distinct path segments, up to reversal, through 270 pair checks. All 64 projected crossings are isolated by rational Sturm arithmetic; they are simple, occur at different times, have certified nonzero imaginary separation, and exchange adjacent strands. Denominator and collision checks exclude every domain or configuration singularity. The greatest crossing-polynomial degree is 12.

The three freely reduced braid words have lengths 28, 32, and 32. The exact Artin free-group substitutions give `AB=BC`; the word `ABC^{-1}B^{-1}` acts identically on all six generators. Artin's faithful action therefore proves the braid identity. The full output includes the crossing polynomials, rational isolating intervals and signs, path vertices, braid words, six common Artin images, and identity images. The output is deterministic and does not use the earlier numerical extraction or finite Burau search.

The original primary Artin article has been opened and read: *Theory of Braids*, Annals of Mathematics 48(1) (1947), 101–126, DOI 10.2307/1969218, Theorem 3 on p.103, Theorem 14 on p.112, inverse generator formula on p.113, and projection conventions on pp.125–126. The bibliography entry includes this precise verification note.

## Consequence for F.7

The proposed seven-point injectivity route is refuted for the actual maps used in F.7. The actual residual `A5` centralizer embeds in the source and satisfies these seven-point restrictions, but the proof has never established that every common-kernel element belongs to the residual centralizer. F.9 does not establish that converse, and does not construct a nontrivial residual-centralizer element. The full nonsolvable centralizer comparison remains open.

F.8's peripheral and reducible-element detectors remain valid. The new kernel word has nonzero source abelianization without lying in a source cusp. Its presence illustrates exactly why the earlier full peripheral detection did not prove injectivity.

## Files

- `f_seven_point_kernel.tex`: complete proof fragment.
- `f_seven_point_kernel_results.json`: integration metadata.
- `f_seven_point_kernel_references.bib`: verified primary reference.
- `code/seven_point_kernel_f9.py`: exact reproducible certificate.
- `code/seven_point_kernel_f9_output.json`: all exact arithmetic and word data.
- `code/seven_point_kernel_f9_stdout.txt`: executed output.
- `code/seven_point_six_factorization_f9.py`: all twenty-four exact forgetting factorizations, with JSON and stdout alongside it.

The older exploratory files remain separately labelled as discovery computations.
