# Next actual mixed ordinary-cup layer

Research after A69; not a formal statement or a scalar-lifting conclusion.
The full negative involution and cofinality questions remain Open.

## Exact coefficient actions

Use the normalized eight source cocycles: rows0..3 are the four free cusp
classes, and rows4..7 are the four binary s-classes. The exact actual
matrices, extracted from the retained source normalization, are

- positive action P=(4 5)(6 7), fixing0..3;
- canonical c on multiplicities C=(6 7), fixing0..5;
- negative action PC=(4 5), fixing0..3,6,7.

The physical monomial c-action remains present in each coefficient.
Thus the ranks on the binary four-dimensional multiplicity space are
2,1,1 respectively. On all32 mixed ordinary slots (one cusp row and one
binary row, in either order), the ranks are16,8,8. The negative C2-H1
multiplicity has dimension16 overF8, so automatic norm surjectivity is
not available for the whole mixed module.

Exact extraction: check_A70_mixed_coefficient.py/.out and
A70_mixed_coefficient_actions.json. The filename is provisional; no
formal A70 statement is reserved.

## The sixteen fixed-negative-multiplicity slots

First take selected rows0,1,2,3,6,7. Let a contain these six copies of V,
and let z contain the sixteen ordered slots (r,i) with exactly one cusp
index. Define

    (a,z)(b,w)=(a+b,z+w+(a_r^2 b_i)_(r,i)).

This is a finite class-two two-group. H acts with degree1 on a and
cubed monomial scalars on z. P and C both swap the selected binary rows,
so each acts on the z-slots by the corresponding ordered-pair swap.
Their product has identity multiplicity action on all sixteen slots.

The source S has zero cusp coordinates. Therefore every displayed cup
vanishes on (a(S),s a(S)), and the literal source S has order2 with z=0.
R is constructed as the actual conjugate of pure r by a lift of its
normalized affine cocycle. This gives R^3=1 and the exact old projection.

The fiber product with the prior actual residual is an actual source
quotient. A commutator of a pure free-row input and a pure binary6/7-row
input at one physical weight has no old opposite-weight-center part,
and its old free-only cubic component is zero. Its new mixed components
are a^2b and ab^2, which span the two ordered coefficient copies
independently. Varying the rows and the physical weight attains all
sixteen copies. Hence the whole new kernel lies in the derived/Frattini
subgroup of the joint residual. Its Frattini quotient is the same old
eight-cocycle module; actual R surjects onto it by the original H1
argument, so finite Frattini gives the full fiber product. The same
argument works at every finite integral level, and compactness handles
the existing integral tower. This step is essential: an abstract group
law alone would not prove that computed frames are actual source frames.

## Actual actions and the computed norms

Both actions include their actual normalized inner terms, including the
nonzero binary-row inner coordinates. Canonical c uses the selected
multiplicity swap and the physical c-action; positive h uses its own
selected multiplicity swap. Their inner terms are transported through
the full eight-cocycle gauge. The code checks the projected affine
formulas against the old source actions before solving anything higher.

The complete coefficient-cocycle space has dimension44 overF8 (eight
cohomology classes and36 coboundaries). Source s/r matching reconstructs
literal canonical c. The positive correction is chosen by the full
40-condition system of literal cusp and s-conjugacy class. The resulting
negative square is extracted as the unique inner vector from the source
s/r values. All sixteen coordinates of that vector are zero.

The new negative coefficient action has trivial multiplicity and is the
physical cubic c-action. It is identity on cusp invariants, so literal-
cusp inner corrections have zero norm; a nonzero square in this fixed
affine family would therefore have been a real obstruction. The saved
calculation instead gives zero. The full s-conjugacy and normalizer norm
also solve in every coordinate, with coefficient norm rank8 on the
20-dimensional s-centralizer. The displayed old r-frame is not used:
its arbitrary coordinate representative had not been solved. A new
r-frame can be obtained existentially from the selected initial
transporter/A16 after the actual quotient and s-frame are in hand, with
new r-frames allowed to vary and initial/older family data retained.

Exact actual-law producer/output:
  check_mixed_binary67_cubic.py
  check_mixed_binary67_cubic.out
Saved values:
  mixed_binary67_cubic_result.json

This is a new mixed quotient, not another free-cusp-only quotient. Its
positive action is nontrivial. It does not assert scalar stability or
full realization of these exact new frames; that is the next gate.

## The other sixteen mixed slots: structural plan only

The slots involving binary rows4,5 have negative multiplicity a free
C2 permutation module: they occur in swapped pairs. Consequently the
negative action on the cusp-invariant inner corrections is free, and
its norm is onto its invariant space. The same is true on the
s-centralizer after tensoring with the physical coefficient involution.
This suggests a direct proof that action-square and s-frame defects can
always be removed in these sixteen coordinates, after the actual source
and peripheral corrections are constructed. The physical involution
must remain in this argument; it is the tensor with a regular C2 module
that gives freeness. No computation or formal theorem for this second
half is yet asserted here.

## Next scalar issue

The new ordinary brackets involve binary s-rows as well as cusp rows.
Their scalar third commutators can include two binary inputs and one
cusp input, unlike the free-only128 calculation. The source s-values
are now nonzero, even though the mixed cups themselves vanish on s^2.
Any proposed scalar cover must therefore retain actual source power
corrections and the nontrivial multiplicity actions. The A68 free-only
128 proof cannot simply be reused with an enlarged row count.

## Update before checkpoint10: the regular half is now computed exactly

The complementary sixteen slots involving binary rows4,5 have now been
constructed and evaluated in the original group law. Their positive
multiplicity swaps4,5; canonical c fixes these two multiplicity rows;
the negative multiplicity is therefore the free swap. Source S^2=R^3,
canonical source c, the literal cusp, and positive s-conjugacy class all
pass their exact checks.

For the first peripheral positive correction, the negative square is a
NONZERO inner vector. It is nevertheless removable in this half. If
j and j' are a swapped pair, the invariant square vector satisfies
v_(j')=C3(v_j). Choose the cusp-fixed inner correction a_j=v_j and
a_(j')=0. Then a+B(a)=v. Replacing h by Inn(a)h keeps the old quotient
action and literal cusp and makes the actual negative square one.
This is a nontrivial norm repair, not an assertion that the first lift
already had order two.

The s-frame is then corrected in the same regular pair fashion. Its
norm lies in the S-centralizer and is fixed by the paired coefficient
involution. Put the norm in one member of each pair and zero in the
other, and multiply the frame on the right. Direct group operations
verify the resulting conjugacy and norm. The complete image dimension
is160 overF8 (eight pairs times the20-dimensional physical s-centralizer).
The displayed r-coordinate test is explicitly skipped; a fresh r-frame
remains available through the selected initial transporter/A16.

Producer/output and stored complete coefficients:
  check_mixed_binary45_cubic.py
  check_mixed_binary45_cubic.out
  mixed_binary45_cubic_result.json

The two halves glue through their common actual old quotient. Their new
kernels are independent by the same free/binary one-weight commutator
argument. Thus the candidate full mixed32 extension has an actual source
image, an involutory negative quotient action, and a solved s-frame,
retaining the preceding integral/free-only cubic quotient action and
s-frame. The construction may reselect new r-frames over the literal
initial C-frame; it does not assert preservation of an arbitrary stored
r-frame at every intermediate new level. Older distinct-type families
remain paired through their actual common C quotient. A full scalar-
refinement calculation and full realization of these new data are still
outstanding. The regular-half computation is newly completed and awaits
independent review after checkpoint10.
