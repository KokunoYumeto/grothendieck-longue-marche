# E.47 — complete integral class-three boundary calculation

Root's isolated eight-program replay passed in 55.690 seconds, with every
mathematical JSON entry and NPZ array identical and all originals unchanged.
The complete proof was accepted after correcting one coordinate-description
sentence. The superseded sentence was:

> The remaining ordinary Hall commutators of weight three have logarithms
> $12$ times the Lyndon basis.

The actual logarithms are the Lyndon basis; their **scaled T coordinates**
are twelve times that basis, as in E.47.4. The corrected sentence now states
both coordinates explicitly. No formula, matrix, program, or output changed.

This work is separate from checkpoint05 and the accepted E.44 programs.
The new proof fragment is `sections/E_integral_class_three_agent.tex`.
It is not inserted into the assembler by this agent.

## Exact outcome

For each of the 432 retained multiplier-one E.24 source values, the
complete **boundary correction-image** fibre in the actual common source
with the class-three pro-three completion of the rank-ten subgroup H has
an explicit parametrization `Z3^70`. This consists of six lower parameters
and a central kernel of rank 64. The actual profinite word fibre above an
image is a coset of the kernel of the displayed joint map from the closed
commutator subgroup of the free profinite group; it is not assigned this
70-dimensional parametrization.

The complete central norm matrix is 660 by 330, with Smith diagonal
`1^264, 3, 3, 0^64`. The errors lie in a rational invariant space of
dimension 270. Four common dual invariant rows give all four rational
conditions. The saturated image has index nine over the actual image,
giving exactly two remaining integral residue tests.

On the exact E.37 chart

    U=t1+t2=c+3w, u=t2, t3=u+3e,
    Phi=e+U^2+3Ue+9e^2=0,

the rational conditions have a common pivot minor
`-16*(30*Phi+1-3U-3e)`. It is a unit on every chart.
The free rational coordinates are `(Y40,Y42,Y43,Y44)`. The two residue
tests have matrix

     2    0    1    1
     c+2  1   -c   -c

and the nine exact right sides are retained in the proof and certificate.
The first two columns have determinant two, so every chart is soluble.

The integral right inverse is an actual matrix formula:
`M*P=3*N`, where N is a primitive rank-266 image basis and N_I is a
specified unit row minor. For a norm right side b in the rational image,
the particular solution is `P*(N_I)^(-1)*b_I/3`. The two residue tests are
exactly its integral-divisibility criterion.

The ordinary central kernel has rank 64 and projects with rank 21 to
the 22-dimensional E.44 central norm kernel. Thus a fixed exact E.37
point has an affine `F3^21` finite central image. A higher lower-coordinate
change supplies the last direction: the saved annihilator evaluates the
four rational free-coordinate derivative columns as `(2,0,1,1)` on all
nine charts. Every finite central solution over an admitted finite lower
point therefore lifts when higher lower-coordinate digits may vary.

The complete finite image has `3^25` points per source value, compared
with E.44's `3^28`; E.44's subset compatible with the whole E.37 tower
has `3^27`. The two additional finite lower equations are E.47.22.
All 24 CM rows, with all 18 source values per row, remain nonempty.

The new explicit nonlift is
`t=0, Y41=1, all other free Y=0`, over source row zero and parameters
`(0,0;0)`. Its full class-two tower is exact. The saved 120-coordinate
finite central correction gives an actual E.44 norm solution. The two
new finite equations evaluate `(2,2)`, so this finite E.44 point has
no full class-three lift even after changing every higher lower digit.

The actual source kernel contains the 450 words `[eta_i,u_j^4]`, where
the 45 adjusted H-prime relators are the accepted E.33 ones. Their
ordinary degree-three image has rank 330 modulo three and supplies the
entire three-adic central lattice. The common-source generation and
prime-supported word constructions retain E.41, E.42, E.43, and the
actual `G_L -> G_A -> G_5` map in E.46.26.

## Authoritative replay order

Run these eight scripts from the project root in an isolated copy.
Every filename below has prefix `code/bc_fermat_class_three_`.
All write their own JSON and stdout; every script except
`curve_obstruction.py` also writes its own NPZ.

| Order | Suffix | Measured main runtime | New inputs produced earlier in this list |
|---|---|---:|---|
| 1 | `integral.py` | 2.015 s | None |
| 2 | `norm_smith_probe.py` | 7.237 s | `integral.npz` |
| 3 | `rational_obstruction.py` | 14.167 s | `integral.npz` |
| 4 | `curve_obstruction.py` | 0.558 s | `rational_obstruction.json` |
| 5 | `integral_tests.py` | 4.979 s | `integral.npz` |
| 6 | `graph_tests.py` | 13.023 s | `integral_tests.npz`, `curve_obstruction.json` |
| 7 | `fibres.py` | 7.420 s | `integral.npz`, `integral_tests.npz`, `curve_obstruction.json`, `graph_tests.json` |
| 8 | `finite_image.py` | 1.335 s | `fibres.npz`, `integral.npz`, `integral_tests.npz`, `graph_tests.json/.npz`, `curve_obstruction.json` |

The total measured main time is about 51 seconds; imports add some time.
The programs do not need to rerun the earlier finite source construction.

The accepted input data read by the new scripts are:

- `bc_fermat_class_two_integral_kernel.npz` — actual adjusted-relator
  central basis, used by step 2.
- `bc_fermat_class_two_3adic_norms.npz` — the integral E.37 Smith system
  and abelian basis, used by steps 3, 6, 7, and 8.
- `bc_fermat_class_two_3adic_tower.json` — exact 432 source residues,
  used by step 8.
- `bc_fermat_class_three_norms.npz` — accepted E.44 norm matrix and
  kernel, used by steps 5, 7, and 8.
- `bc_fermat_class_three_tower_comparison.json` — all nine E.44/E.37
  affine comparisons and all 432 source records, used by steps 3, 4,
  6, 7, and 8.

The direct legacy Python imports are `de_fermat_schreier.py`,
`bc_fermat_class_two.py`, `bc_fermat_class_two_integral_model.py`,
`bc_fermat_class_three_burnside.py`, and
`bc_fermat_class_two_fibres.py`. The last imports
`de_ferrari_mod9_lift.py` and `de_ferrari_two_family_words.py` to define
classes/functions; its `main` is not run and `load_data` is not called.
Keeping the already accepted `code` directory in the isolated copy
preserves these ordinary import dependencies.

Comparisons should ignore only `elapsed_seconds`. All mathematical JSON
entries, all NPZ arrays, and all non-timing stdout are authoritative.
The intermediate files retain their limited-stage status language:
the complete lifting assertion is certified by the final two scripts.

## Preserved attempted extension and correction

The first `graph_tests` draft tried to divide the entire unrestricted
central-error polynomial coefficientwise by three. Its assertion
correctly stopped before any chart or fibre conclusion was made.
The ordinary monomial coefficients have 486 entries not divisible by
three, even though their integer-valued cubic evaluations have the
required divisibility. The two weighted test polynomials have four
exceptional monomial rows:

    t3   : (-28,-48)    t2   : (-2,-6)
    t3^3 : (-8,-60)     t2^3 : (2,12)

The exact E.37 substitution `t3=u+3e,t2=u` combines these terms with
coefficients divisible by three. The authoritative script first makes
that actual substitution and then checks every coefficient. It retains
the mixed error coefficients separately and verifies their exact
integer polynomial reconstruction.

The failed draft and its explanation are preserved in
`research/class_three_integral_attempts/graph_tests_prechart.py` and
`graph_tests_prechart_failure.txt`. No theorem used its failed assertion.

## Scope and source maps

This is a complete result for the stated class-three pro-three boundary
quotient and the actual finite/common sources. It does not assign these
finite shadows to arbitrary full GT elements. The positive statements
are proved by actual word preimages and actual generating maps, including
the simultaneous retained factors. The new negative statement is the
specified projection from the full class-three tower to E.44.

The comparison with a fixed exact E.37 point and the comparison allowing
higher E.37 digits to vary are both retained, with the explicit derivative
map connecting them. The respective finite central dimensions are 21
and 22; no finite central fibre was identified across those maps without
that calculation.
