# Independent full review: the actual pillowcase stabilizer and marked section

Reviewer: DE. Cycle30 late research; all frozen formal sources remain unchanged.

**Verdict: PASS at the stated ordinary scope.** I read the entire current
`work_CE/one_family_full_stabilizer_and_marked_section30.txt`, the entire
44-check producer, its genuine standard output and empty standard error,
and the certificate's full marked input/checked-image data. I also freshly
read the entire B144 formal source to bind the resulting section to the
actual graph, source, and category conventions. No fresh producer execution
is claimed.

The reviewed proof SHA-256 is
`0eee300427719cbe48d82b319daaccf73d99fe9a6c4c97b25430c7c8a4fa10cc`.

## 1. Actual quotient and all signed actions

The original free fiber is `F(r,bar_r,w)`, with
`f=w^-1 bar_r^-1` and `g=r^-1 w`. After imposing the four stated
squares, `r` and `bar_r` are involutions. The equations for `f^2` and
`g^2` make each of them invert `w`. Consequently `z=bar_r r` commutes
with `w`, and `r` inverts `z`. Conversely `bar_r=z r`, the original
`f`, and the original `g` satisfy all four squares in
`Z^2(z,w) semidirect C2(r)`. These inverse presentation maps establish
the exact quotient, including the infinite-order independent translations.

Directly from the actual operators,

- `m` fixes `r,z` and sends `w` to `w z^-1`;
- `u=m^-1 v` sends `r` to `w^-2 r`, `z` to `w^4 z`, and fixes `w`.

Thus, in column-vector coordinates, the two matrices are
`M=((1,-1),(0,1))`, `U=((1,0),(4,1))`, with reflection corrections
`0` and `(0,-2)`. The signed inverses are integral automorphisms and
the original four relations are preserved in both directions. The
producer additionally evaluates the actual old `f,C,tau` words, not
only the newly asserted coordinates. Its extension by `tau` is valid:
`tau` acts as `(n,epsilon) -> (-n+epsilon e1,epsilon)`, and commutation
with the displayed source automorphisms is exactly
`A e1+2b=e1`. This is included in the actual old-generator checks.

## 2. Whole-source faithfulness and exact stabilizer

The affine composition identity is the actual ordered one. Since
`b_s=(I-A_s)e1/2` holds on both generators, the composition rule proves
it on every signed source word. If the original free word `r` is fixed,
the quotient reflection is fixed; its unique normal form forces `b_s=0`
and hence `A_s e1=e1`.

Conjugation by `diag(2,1)` gives the upper and lower parabolics with
off-diagonal entries `-2` and `2`. Their every-nonzero-power inclusions
between `|x|<1` and `|x|>1` are strict. The lower map's possible pole is
outside its source domain, and infinity has the stated image. For a
mixed cyclically reduced word, conjugation by a suitable power of its
last factor makes its two end syllables belong to that factor without
cancelling them. It then maps one ping-pong domain into the disjoint
other domain. This establishes faithfulness for all words, including
exclusion of a word mapping to minus the identity matrix; no tested
finite word collection is used.

An integral determinant-one matrix fixing `e1` is precisely
`((1,k),(0,1))=M^-k`. Faithfulness therefore forces `s=m^-k`.
Every such power fixes the actual original `r`, so this necessary
quotient test is also sufficient for the original stabilizer.
Together with the previously proved exact cocycle/character comparison,
it gives the complete equality `H intersect S=<m>`.

## 3. Marked ordinary section and remaining fixed kernel

Substitution into both B144 presentation maps gives the actual discrete
one-family fixed subgroup

`J_a=<A,m,v | [A,m]>=Z^2(A,m)*Z(v)`.

The actual B130 word `A_src=s1 s4^-1 s1^-1` maps to `A`, is fixed, and
commutes with the actual `m`. The assignments `A -> A_src`, `m -> m`,
`v -> v` therefore satisfy every relation and split the actual ordinary
fixed projection. This embeds the specified mixed three-source subgroup
with exactly the displayed presentation. Both stated ordinary split
extensions follow from this same section and the actual quotient map.
They leave the entire remaining fixed-kernel equality unresolved.

## 4. Preserved failed compact extension and corrected domain

Before this full source read, DE proposed extending B144's norm-copy
retraction to the entire ordinary quotient and inferring full ambient
topology of the mixed three-source subgroup. Root and CE identified the
typing error, and DE explicitly withdrew that proposed consequence.

The actual ordinary group is
`Gamma_a=A(Gamma) semidirect Q^0`, with `Q^0=T0 semidirect S`.
It is **not** `A(Gamma) semidirect S`. Odd-vertex deletion is compatible
with `Q^0`, but the subsequent deletion onto the selected `S/L` orbit is
only `S`-equivariant. Thus the norm-copy retraction is defined on the
infinite-index preimage of `S`; it does not give a retraction from the
whole ordinary group. No full ambient topology, completed section, or
compact stabilizer equality is inferred from that restricted retraction
or from discrete matrix faithfulness. No such stronger claim was promoted
to a formal source or to a completed theorem.

The reviewed CE source already states the correct ordinary limitation.
The whole retained-fiber action must remain in any future compact
finite-target extension argument. The original icosahedral `K=1` problem
and the remaining fixed-source equality are unaffected by this new
ordinary section.
