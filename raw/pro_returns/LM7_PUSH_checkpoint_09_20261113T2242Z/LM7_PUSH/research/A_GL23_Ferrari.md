# Literal GL2(F3) Ferrari batch — complete finite test

This batch is separate from the frozen, independently replayed E.59 files.
It addresses the next finite pentagon test for E.3.  Parent reserved E.62
for the eventual complete statement; no full profinite conclusion is made.

## Exact small group and target

`code/a_cm_gl23_group.py` enumerates the 48 literal invertible 2 by 2
matrices over F3, all 864 ordered generating pairs, and every automorphism
by a complete Cayley-edge test on all possible generating-pair images.
There are 48 automorphisms and 18 epimorphism kernels.  The three nonzero
determinant profiles each have six kernels.  All automorphisms are actual
inner matrix maps or the map g -> det(g)g composed with such a map.
Restriction to the saved SL2(F3) automorphism table is onto, with kernel
two.  The derived subgroup is precisely the determinant-one matrix group.
The projective-line map is given on the four explicitly listed lines,
has image order 24, and has scalar kernel {I,-I}.  No identification with
another named double cover is used.

`code/a_cm_gl23_model.py` retains the actual evaluation map of the free
Ferrari group into the product of the 18 matrix groups, and all Nielsen
coordinate transporters.  The faithful holomorph action has degree 864.
The actual orders are:

| Image | Order |
| --- | --- |
| Free Ferrari group | 2^23 3^3 |
| Nielsen action | 2^16 3^7 |
| Four-strand target | 2^39 3^10 |

All three literal braid relations, the actual xi1/xi2 recovery words,
the four Nielsen conjugation formulas, and all 36 products of signed braid
generators are checked in the faithful action.  The six E.17 pure-pair
substitutions are retained without changing their paths or order.

Profinite-images independently read both entire programs and passed the
complete group/Aut/Nielsen comparison.  That audit did not claim a source
or fibre result from the two target programs alone.

## Actual induced source and its joint maps

`a_cm_gl23_induced.py` forms the same six evaluations over the same six
actual B/F cosets as E.59.  Its degree 31,104 action compresses faithfully
to degree 2,808, with an explicit intertwiner on every discarded orbit.
All ten H generators and all 97 original N_B generators are checked in
both actions.  Complete C++ Schreier certificates give:

| Source image | Order |
| --- | --- |
| G_GL | 2^29 3^6 |
| image of N_B | 2^23 3^4 |
| image of N_B' | 2^21 |

The first two orders have ratio 576.  The actual map
B/N_B -> G_GL/image(N_B) is onto and hence is an isomorphism.  This is
the comparison to the original Q, not a numerical substitution for it.

`a_cm_gl23_joint.py` takes the literal block sum with the frozen E.59
source and target.  Its orders are:

| Common image | Order |
| --- | --- |
| G_(GL,SL) | 2^41 3^6 |
| image of N_B | 2^35 3^4 |
| image of N_B' | 2^24 |
| T_(GL,SL) | 2^63 3^12 |

The retained source block projections have kernel orders 2^12 over GL
and 2^15 over SL.  Thus neither specified source map factors through the
other: a compatible factorization would make their common image the graph
of the factor map, with the order of that projection, contradicting the
displayed kernel.  This assertion concerns the actual quotient maps from
B; it does not assert an unrelated abstract nonexistence of homomorphisms.
The analogous target block maps and their exact kernel orders are saved
by `a_cm_gl23_projections.py`.

## Complete correction coordinates and equations

`a_cm_gl23_pc.py` proves that the two actual N_B' images have central
elementary-abelian derived subgroups of orders 2^3 and 2^6, respectively.
Their quotients by these derived subgroups both have dimension 18 over F2.
All generator squares lie in the derived subgroup.  Every prefix of the
chosen coordinate basis has a complete Schreier certificate, with index
two at every added quotient basis vector.  These actual prefix groups
recover coordinates uniquely.  Every basis product is checked against
the literal permutation product; 256 additional retained random products
are checks of the same proved collection formula.

All 97 original N_B sixth powers lie in these derived images.  Hence
the image of K6=N_B' N_B^6 equals the image of N_B'.  Since N_B' is
contained in F', it is also the image of F' intersect K6.  The whole
finite-value fibres over the specified G6 points therefore have exactly
2^21 and 2^24 elements.

`a_cm_gl23_gentle.py` uses the exact class-two multiplication law.  It first
solves the quotient norm equations, of rank 15 in 18 variables.  For each
of the eight remaining quotient values it solves the entire central
equations.  It independently tests every answer as a literal permutation.
For all 24 original multiplier-one G6 points this gives 16 GL values and
32 joint values.  These are complete finite fibres, not a search among
chosen representative words.

`a_cm_gl23_pentagon.py` evaluates every coordinate basis element through
its actual N_B' word DAG in the Ferrari models.  The GL and SL components
in the joint calculation use precisely the same source word.  All 24
rows give four full pentagon/braid/twist values in the GL test and four
in the joint test.  On the 32 joint gentle values, GL pentagon alone
admits eight and SL pentagon alone admits sixteen, with intersection four.
Both literal full twists are fixed on every gentle value.

The source projection of joint gentle values covers all sixteen GL gentle
values twice and all four E.59 gentle values eight times.  The final four
joint points cover only two of the four GL pentagon values, each twice,
and cover both E.59 pentagon values, each twice.  These are actual coordinate
projections in `a_cm_gl23_projections.py`; the GL restriction is retained.

## Generation, proof and independent review

`a_cm_gl23_generation.py` completed all 768 joint gentle source generation
checks and all 96 final joint target generation checks: every point generates
the whole specified group.  Each has an exact Schreier certificate and an
independent word-DAG replay.  The authoritative runtime is 221.490 seconds.
The program also retains actual F' preimages as finite N_B word DAGs together
with the literal N_B-to-F word map; all integral abelianizations are zero.
`a_cm_gl23_single_generation.py` independently proves generation at all
96 GL-only final target points, in 27.119 seconds.  The GL-only source
generation follows from the proved surjection of the complete joint gentle
list onto all sixteen GL-only gentle values in each fibre.

The complete statement and proof are in `sections/E_gl23_ferrari_agent.tex`,
E.62.  They retain the actual Q quotient, both projection kernels, exact
K6 and F'-intersection images, all source cochains, and the Goursat proof
of generation after restoring the entire G6 factor.  Profinite-images read
the entire proof and the pc/gentle/pentagon/projections/generation programs
independently, without rerun, and passed the mathematics.  Its two editorial
corrections were applied: the Nielsen transporter expresses the new pair as
the automorphic image of its representative, and a missing backslash in
E62.13 was restored.  The initially reviewed text is retained separately.

The standalone five-page LuaLaTeX build is clean, with no warnings, and
every rendered page has been inspected.  The first build's twelve-point
table overflow is preserved; shortening only its column headings resolved
it.  `a_cm_gl23_structure.py --check-existing` independently checked both
retained structural chains and every exact subgroup input without replacing
them.  The full isolated replay and immutable manifest are supplied next.
E.3 remains open after this finite test: the result proves a complete finite
fibre, without a compatible full profinite pentagon lift.

## Preserved failed execution

The first `a_cm_gl23_projections.py` execution requested the nonexistent
old filename `a_cm_sl23_B_source.out`.  The old E.59 output is actually
`a_cm_sl23_B_source_chain.out`.  The initial program/stdout/stderr are
preserved as `a_cm_gl23_projections_failed_old_output_path.*`.  The sole
repair changed that read-only input pathname.  No E.59 artifact was edited.

The first manifest invocation redirected its own stdout to a filename
inside the manifest's research-file glob.  Its completed stdout therefore
changed the hash recorded while it was empty.  The immediate hash-only
check detected that single mismatch.  The initial manifest and failure
record are retained as `E62_initial_self_output_manifest.json` and
`E62_initial_manifest_check.*`.  The final invocation writes stdout only
to the tool result, so no protected output changes during manifest creation.
No mathematical source or result changed in this packaging repair.
