# E.121 — independent proof, source and marked-ideal audit

**Verdict: PASS. No mathematical correction remains requested.**

Reviewer: `/root/d_galois`. The final proof is
`research_e119_continuation/sections/E_fiftythree_normalizer.tex`, SHA-256
`435bef02e897562e6651305bfee3da289e54235899c113027b1799a2e5a2fae0`.
The amended author manifest is
`de04c68da8e09240a36074cd7dfb3d943d0759811cf6e842fe871b1e24625b1d`.
I verified the byte count and SHA-256 of all 264 entries. All thirteen copied
mathematical inputs also agree byte for byte with the corresponding entries
in the original and amended author freezes. No author file was modified.

## Scope and execution provenance

I read all 573 final proof lines, all five GP sources (326 lines), the entire
387-line Python checker, and the source, dependency and computation ledgers.
The two final proof-only amendments were read in their entirety. The old
128-file author freeze is preserved by the author; the amendments change
neither the mathematical programs nor their outputs or PARI objects.

I wrote and executed two separate focused verifiers:

* `code/d_e121_maps.py` uses only standard-library exact `Fraction` arithmetic,
  HNF coset reduction and finite enumeration. It imports no author Python
  module. It independently reconstructs the displayed normalizer matrices,
  all marked genus maps, full class maps, the positive connecting class, and
  the normal-closure group in a different coordinate system.
* `code/d_e121_ideals.gp` works with copied exact lower-field objects. It
  constructs transformed and extended ideals from every marked HNF basis
  column. It verifies the complete principal-ideal corrections, norm
  identities through extension, and the seven literal cyclotomic S-units
  with all their wild and tame characters.

Both final executions returned exit zero and explicit PASS records. This
is an independent focused proof/map/ideal audit. I did not rerun the author's
five-stage arithmetic construction. Root separately performed that full
copied-source reconstruction, comparing seven whole text outputs and seven
whole decoded PARI objects. Those root executions are not attributed to me.

The first direct principal-ideal product run was interrupted with exit130:
some factored corrections have 237 terms and exponents as large as1824859,
making uncancelled powers unnecessarily large. Its exact source and partial
stdout are preserved under `code/history/direct_uncancelled_powers/`.
The final verifier combines exact prime-HNF exponents before reconstructing
the cancelled ideal. This preserves the literal ideal equality. A small
factor-size diagnostic and its actual output are retained too.

The first successful focused checks are preserved under
`code/history/first_successful_checks/`. Before finalization the finite
matrix application helper was strengthened to reject every nonintegral
`Fraction`, and the HNF-column counter was corrected to include the
intermediate second-conjugation columns. Both full focused checks were then
executed again. The final count is732 marked HNF columns, not624; the checked
ideal identities are unchanged. Rational matrices are serialized as exact
rational strings and decoded back entrywise.

## Actual ideals, local characters and genus maps

The literal lower normalizers have generator images
`g(x)=xi-xi^3 alpha` and `h(x)=xi^4-xi^(-3)alpha`. Substitution into the marked
`xi` and `alpha` verifies their actual field actions. My GP verifier then
transports every column of each ideal HNF through those embeddings. All12
ordered S-prime images agree with the stated permutations.

For all six transformed ordinary class ideals, it checks the full equality
between the transformed HNF and the product of the fixed class ideals with
the retained principal correction. It also checks three horizontal norm,
two horizontal extension and three cyclic-nine norm principal identities:
14 complete principal-ideal identities in total. Every rational prime used
to collect a principal divisor is checked by `isprime`.

The actual ideal norm checks use a second construction. For the horizontal
map, extending the recorded lower ideal gives exactly
`G_i h(G_i) h^2(G_i)`. For the cyclic-nine comparison, extension gives exactly
`G_i g(G_i) g^2(G_i)`. Extension of fractional ideals is injective, so these
equalities identify the recorded norm ideals, with their precise field
embeddings. Absolute ideal norms are checked as well. The two extended
lower class ideals are reconstructed from all six lower HNF columns,
are fixed by `h`, and have the required cubed absolute norms.

The seven S-unit expressions over `F=Q(zeta9)` are reconstructed from the
literal polynomials in `xi`, rather than assigned abstract basis labels.
Their equality with the certified E119 basis is checked. Exact polynomial
resultants give all seven normalized wild norms. Actual residue fields and
the common global `xi` give all21 ninth-power tame phases. The resulting
character matrix has zero wild row and three equal rows
`(3,6,3,6,0,0,0)`; the S-valuations of the final four units form the identity.
The earlier E119 proof establishes completeness of this S-unit basis; the
present check verifies its exact marked use in E121.

The finite verifier uses the full HNF residue boxes of orders729,81,729 for
the three idelic genus groups. It enumerates their actual restriction
kernels of orders243,27,81. It checks every full forward/backward Smith map
on those kernels, together with both ambient rational inverse compositions.
It separately verifies the explicit four-by-three representative map and
three-by-four inverse for the cyclic-nine kernel.

The displayed class blocks and principal-character blocks reconstruct
`A_f=[[P_f,-X_f],[0,C_f]]`. The negative sign agrees with the principal-idele
relation. The exact relation-lattice and restriction maps are preserved.
Both normalizers are checked on all243 kernel elements. The horizontal
norm, extension and cyclic-nine quotient are reconstructed from the literal
matrices in the proof and checked on every relevant kernel element. Their
composition identities hold in the actual source and target relation
lattices before passing to Smith coordinates.

## Why the full upper class groups follow

The proof of the complete `A(B2)` passes independently. Write
`T=g-1`, `s=g^3-1`, and `M=sA`. The exact computed action on `A/M` has
`T^2=0`. The lower `g`-action is the identity, with the actual E119
norm/extension justification. Therefore
`T(1+sigma+sigma^2)A=0`. Expanding both polynomial identities gives
`M` contained in `(3,T)M`, with no replacement of the actual class map by
an abstract one. Since `g^9=1`, `T^9` belongs to `3 Z3[g]`. The ideal
`(3,T)` consequently acts nilpotently on the finite three-primary class
group. Iteration forces `M=0`. Thus the already computed coinvariant is
the full `A(B2)=C9+C3^3`.

The horizontal extension is actually unramified and S-split. The maximal
subfield of its S-Hilbert class field that is abelian over `L2` is the
S-Hilbert class field of `L2`. Abelianizing the cyclic extension supplies
the exact injection of `A(B2)_h` into `A(L2)` via the actual ideal norm,
with quotient the degree-three Artin character. This gives order81.

The tame inertia marking is essential and is retained correctly. With
commutator `xyx^{-1}y^{-1}`, the positive connecting class is
`E4-A_h E4=E4-E6`. Its exact kernel coordinate is `(3,0,0,0)`. My verifier
checks this from the full nine-dimensional lattice and proves it is outside
`(H-I)A(B2)`. Changing either lift gives precisely the stated difference
subgroups. Its norm is `3u`, so `(sigma-1)A(L2)=<3u>`.

The resulting trace is multiplication by three. The lower class group has
exponent three, hence the full upper group has exponent dividing nine.
Its order81 and its two-dimensional quotient modulo three force
`A(L2)=C9^2`. The positive Artin value and the actual norm-extension
composition determine the two power relations and all full matrices.
The remaining choice `a -> a+3ku` gives the exact displayed shear; every
stated finite map is invariant under it with its own moduli.

The final proof-only replacement of `3N_L^{-1}` is correct and necessary
as an explicit map. The actual norm is onto and its kernel is `3A(L2)`.
For each lower class `b`, every lift `a` with `N_L(a)=b` has the same triple,
because the upper group has exponent nine. Thus `j_L(b)=3a` is an actual
lift-independent rule. The independent finite verifier checks all nine
lower classes and all nine lifts of each. No inverse of the surjective
noninjective norm is asserted.

## Full class maps, normal closure and unit kernels

The verifier checks the horizontal and vertical norm/extension compositions
on every element of `A(B2)` and `A(L2)`, the actual capitulation kernels,
the fixed subgroups, and the quotient coordinates of all three unit-norm
defects. The cyclic-nine quotient has kernel exactly `(g-1)A(B2)`. The
horizontal positive connecting class and every basis shear are retained.

For the actual normal closure I used coordinates `(a,u)`, with
`a` modulo9 and `u` a unit modulo27, acting by
`alpha2 -> zeta9^a alpha2` and `eta -> eta^u`. The multiplication rule is
`(a,u)(A,U)=(a+uA,uU)` with the appropriate moduli. All26244 products and
right-inverse identities are checked. Solving the literal equations for
the fixed radicals gives the subgroups fixing `B2`, its conjugate, `B1`,
`L2`, `L1` and `F`, with orders3,3,9,9,27,27. This verifies the intersection
and compositum maps without assigning complex conjugation to `B2` itself.
The local cyclotomic and53-adic conditions then give the actual unramified,
S-split cubic compositum. The stated Artin character is checked on the
entire243-element class group and against both normalizer actions.

The outside-S unit norm map in (E121.20) is valid with both inverse
directions. A unit of the form `Nx` gives a zero-norm divisor of `x`; on
each unramified orbit this divisor is `(tau-1)D`. Changing `x` by a
norm-one element changes the class by a principal divisor and an extended
base divisor, by Hilbert90. Conversely an invariant class produces the
required principal difference and an S-unit norm. The prime-to-three
invariant quotient vanishes through `jN=3`, so the canonical projection
to the three-primary group loses no class in this quotient.

The evaluated invariant quotients have orders81,3,3. Their coordinates
and the kernels of those coordinate maps were independently enumerated.
Combining them with the actual field-norm indices gives the three stated
unit-norm quotients. The Herbrand/capitulation calculation gives the same
indices with the same actual maps.

For each completed unit kernel `K`, the literal torsion is `mu3`. The
quotient `K/mu3` is a free finite-rank `Z3` module. Choose its basis and
lifts `k_i` in `K`. The final proof correctly gives the continuous map

\[
(z,(a_i))\longmapsto z\prod_i k_i^{a_i}.
\]

Its inverse first reads the quotient coordinates, then divides by the
corresponding product. The residual element is in the actual `mu3`.
The two operations are inverse; equivalently, a continuous bijection of
these compact Hausdorff groups is a homeomorphism. Changing the quotient
basis gives a `GL_r(Z3)` coordinate change, and changing lifts gives the
explicit inverse torsion-factor adjustment. This proves the asserted
noncanonical direct-sum isomorphism and its precise ambiguity. It does
not claim a computed numerical basis of the upper unit group.

## Primary sources and retained scope

My earlier complete independent E119 audit in `d_e119_audit/audit.md`
records my own readings of [Milne, Class Field Theory](https://www.jmilne.org/math/CourseNotes/CFT.pdf),
including III3.1 with its cup-product restriction/corestriction proof,
V3.3 and V5.2–5.5, VII3.1 with the unit-lattice argument, and VIII3.1
with the cyclic Hasse-norm proof. Those exact arguments supply the
norm/transfer, S-split reciprocity, Herbrand and local-global inputs here.
The unfinished proof notice after III Lemma3.2 is not used.

I also previously independently read [Lemmermeyer, Ambiguous Class Numbers](https://arxiv.org/pdf/1309.1071),
Proposition1 and its full ideal/Hilbert90 argument. The printed `Am_st`
label does not replace E121's explicit outside-S inverse maps.
For this audit I freshly opened the
[official PARI contract](https://pari.math.u-bordeaux.fr/dochtml/html-stable/General_number_fields.html)
and read the corresponding original `doc/usersch3.tex` passages for
`nfgaloisapply`, ideal HNF and ideal products. Equality of transformed
prime representations is tested only after the actual HNF map. The
certified E119 input contracts remain as reviewed in that earlier audit.

The proof establishes the full positional-level-two S-class groups, all
specified norm/extension/normalizer maps, the exact normal-closure character,
and the three completed unit norm kernels with their choice maps. It makes
no assertion of an upper ordinary class group, an uncomputed numerical
upper unit basis, or stability at later positional levels. The audit makes
no stronger assertion.
