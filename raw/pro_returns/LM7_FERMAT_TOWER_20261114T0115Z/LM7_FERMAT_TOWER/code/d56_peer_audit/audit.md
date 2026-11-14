# Independent peer audit of D.56

**Result: PASS after the recorded source-typing clarification.** The final
audited section has SHA256
`c89f160788792bd7a2efd6e851d90c148fca53610287a4c05f760bed97830c69`.
This audit reads the complete proof and all seven program sources. Root owns
the independent complete seven-stage execution; the execution here is a
separately written focused verifier, importing no author program.

## Literal arithmetic quotient and parameter

The verifier reconstructs the marked group of order 576 directly from row
matrices in `SL_2(Z/12)/{+I,-I}`. The 1,152 marked edges determine the linear
map to the group of order 48; the actual twelve-state kernel has commutator
subgroup the stated marked Klein four group. Its eight elements outside
that subgroup have order three. Thus the kernel is the specified `A_4`, and
its abelianization has no two-primary quotient.

All 97 marked free words evaluate to the columns of the displayed rank-four
map on `N_ab/3`. The two module-equivariance identities are checked on all
194 columns. This proves the factorization through the actual `G_3` and the
kernel exact sequence with `C_3^93`; it does not infer that factorization
merely from the orders of the two generators. The affine image has all
3,888 states. All forty projective lines generate the four-dimensional
module. The full commutant has dimension two and its nine displayed
elements form a field.

The arithmetic step uses the original normalized identities of D.49 and
the original `r`-conjugator's `5I` coordinate, proved in D.47's paragraph
“One coherent pair of normalized conjugators.” In the literal quotient,
`5I` acts as `-I`. The two constraints `Sa=-a` and
`a-2v in im(1-R)` have exactly the one solution `(2,1,2,1)`. Conjugation by
the sixth power of the marked cusp sends `s` to `sa` and `r` to `a^-1 r`.
The independent verifier checks the resulting equality on all 7,776
marked affine edges. This proves preservation of this quotient by the
original arithmetic action. The splice factors through its identity
three-primary component by the literal restriction of `C_h` to `A_*`.

## Homology and the forty-dimensional correction space

The marked graph has 3,888 edges and 3,240 vertices, giving rank 649.
Both marked elliptic orders are retained; the cusp order is twelve. The
324 cusps have the single integral sum relation, giving genus 163 and
compact rank 326. Odd averaging over the actual group of order 81
identifies the invariant graph homology with the rank-nine quotient
graph. The cusp map has no extra ramification and has invariant radical
rank three. The moving ranks follow as 640, 320, and 320.

The seven author programs were read in full, including the signed graph
cycles, every marked free word, the ribbon pairing, and the actual deck
actions. The independent verifier checks the coefficient maps from the
moving basis into the full homology basis, the actual fixed subspaces,
the 640-dimensional image of the cusp-defect map, and all 600 columns of
the same-action inclusion. The latter columns are independent and lie
in the cusp kernel. Therefore the kernel-to-derivation quotient really
has dimension forty; this is not obtained by subtracting unverified
nullities. The independent check also confirms cusp rank 323, compact
rank 326, and moving cusp rank 320.

## Maps from the full arithmetic source

The exact sequence `K_3 -> K_* -> P_*` gives a surjection on maximal
abelian pro-two quotients because the finite group `P_*` has no such
quotient. Both averaging idempotents commute with this map since the
actual map `A -> A_*` is onto with odd kernel. This gives the displayed
surjections on full and moving homology, their exterior products, and
coinvariants, with the stated right-exact comparison kernel.

For a lifted peripheral pair, its cusp error belongs to `J=ker(W->W_*)`.
Odd averaging gives `J_A=0`; hence `J_G=0`, and the two-generator
augmentation map `(1-s)J+s(1-r)J -> J` is onto. It removes the error and
proves surjectivity on actual pair spaces. The same-action subspace maps
into the smaller same-action subspace, giving the precise quotient map
and kernel written in D.56. No surjectivity on the same-action subspace
itself is needed or claimed.

As an `A_*`-module, the moving homology has eight copies of its
augmentation module. Over a splitting field its eighty nontrivial
characters occur in forty inverse pairs. This gives invariant exterior
dimension `40*8^2=2560`. The cross term with the invariant rank-nine
module has no invariant vectors. The whole exterior image has dimension
`binom(640,2)+640*9=210240`, with moving dimension 207680.

## Joint source, action descent, and boundary square

The original wording referred to preservation of `K_*` by the D.50
action. That action is defined on `Z_h=Bhat/R50`. The corrected proof
uses its actual subgroup `K_*/R50`. Because `R50` is contained in
`M_infty`, hence in `M_*`, the maximal abelian pro-two kernel of that
subgroup is exactly `M_*/R50`. It is characteristic. The retained map
to `W_h` separately makes `R_h/R50` invariant. Their intersection gives
the descent to `Z_{h,*}`. The map `Z_{h,*}->W_h` is equivariant; descent
to `Bhat/M_*` is stated separately. This correction avoids assuming
that the constructed action acts on the original free profinite group.
Both prior versions and exact diffs are retained by the author.

The image of the pronilpotent residual of `C_h` in the smaller homology
extension is exactly `U_*^-`: the image contains the commutators of its
odd quotient with the normal two-primary kernel, and quotienting by
that moving part makes the image pronilpotent. The actual D.51 argument
then identifies the residual's class-two central image with
`W_* wedge V_*`. It retains the invariant quotient and uses fourth
powers of actual residual preimages to remove their homology
coordinates. The two kernel products consequently give the stated
fiber product and all four source-projection kernels.

The D.54 lifts of the original conjugators map through these source
quotients. Pair changes and central cusp errors therefore map by the
specified homology and exterior maps. Passing to their actual central
correction cokernels gives both boundary squares, including the
same-action ambiguity quotient. This uses the fixed arithmetic seed;
it does not assign a value to the smaller quadratic obstruction.

Finally the group-norm comparison has the actual factor
`|P_*|=12*3^93`, which is even. Its reduction is zero. No norm-factor
division is used to infer the value of the smaller boundary.

## Executed independent certificate

Run `python bc_d56_audit/code/bc_d56_maps.py`. Its complete output and
JSON are retained alongside the source. The four frozen input hashes
are recorded in that JSON. All checks passed. This audit does not
duplicate root's full seven-stage rebuild and does not claim that the
remaining forty-variable arithmetic quadratic zero locus was evaluated.
