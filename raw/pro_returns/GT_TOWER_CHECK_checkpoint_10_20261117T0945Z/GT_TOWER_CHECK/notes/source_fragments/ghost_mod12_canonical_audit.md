# Independent audit of A.4.59

The complete proof in `centralizer_common_mod12_survivor.tex` passes the
mathematical audit. The four executed programs were copied, without
mathematical changes, into `work/ghost_mod4_review/` and freshly executed
there. Every run has an actual saved output. The final exact comparison
checks every retained numerical array against the original certificate.

## The full canonical model

For the actual free modular kernel K of rank 97 and L4=K'K^4,
the commutator subgroup [K,L4] is exactly gamma3(K)(K')^4. The lower
central quotient has the free class-two collected normal form, so
L4/[K,L4] consists of 97 independent integral fourth-power coordinates
and 4656 independent commutator coordinates modulo four. No higher
commutator or additional integral relation is dropped here.

For an automorphism whose image of k_i has integral exponent row a,
the fourth-power coordinate changes by a. Its commutator correction
is -binom(4,2) a_j a_k = 2 a_j a_k modulo four. The original
commutator part of that image is multiplied by four and vanishes.
This justifies the exact two power-action blocks in the program;
using only their binary reductions would not justify the result.

The bit-plane wedge computation performs genuine unit row operations
over Z/4. Its lifted projection annihilates all 4641 unit-pivot
relations. The remaining relations are twice the seven independent
binary rows, and they are all added to the integral relation matrix.
The 194 power-action rows, 15 order-four rows and seven residual rows
give the entire 216 by 112 matrix. The independent replay returns
96 unit Smith entries, eight entries 2 and eight entries 4. Thus the
full canonical kernel is C2^8 times C4^8.

The s-fixed module computation also retains the seven even residual
constraints. It gives C4^45 times C2^7. All 52 named generators are
collected in the full integral model; their kappas are killed by two.
The quotient of the full canonical kernel by these corrections has
Smith invariants C2^5 times C4^4. This quotient is not substituted for
the full kernel in the decisive check: the selected final defect has
an explicit integral coordinate vector in the full Hermite lattice.

## The selected record and actual automorphism

The literal mixed target is Z/4 in its first 100 coordinates and
Z/2 in its last two, encoded injectively as the even elements of
Z/4 for the equation solve. The source-frame equations correctly
transpose the row-action matrices when applied to the column of
unknown coordinates. The fixed corrected binary record has 97
binary lifting directions after the rank-194 solve.

Adding directions 9,10,15,52,59 gives the selected record. The direct
full-Hermite test returns zero with no extra centralizer correction.
The independent finite automorphism replay uses actual source words,
the exact base cocycle and all 576 base-generator transitions. The
source kernel factors through the marked rank-97 quotient. Its
reduction modulo two is the earlier invertible mask-31 map, hence the
Z/4 map is invertible. Both finite positive frame equations are
verified, extending the pure map to the full source E4. The common
base action is the identity, so the literal fiber product with the
ternary identity automorphism gives the actual E12 automorphism.

## Integral primary transfer and normalization

The maps E12 -> B0/(K'K^4) and E12 -> E3 have kernels of orders
3^98 and 4^97 respectively. Their actual quotient kernels in B0
are contained in B0'. Since H2(C2*C3,Z)=0, the canonical central
kernel is naturally H2 of each finite quotient. The localized
integral homology edge maps therefore identify the entire 2-primary
kernel with the computed M4 and the entire 3-primary kernel with
the canonical kernel for E3. These are the actual maps induced by
the source quotient homomorphisms.

The selected defect vanishes on the first factor by the full integer
Hermite witness. On the ternary factor f3=A3=1, so the defect is the
s-frame commutator and is killed by two. Its 3-primary component is
therefore zero. Transfer rules out all other primary parts, giving
zero in the entire canonical kernel of E12.

The conjugated order-two and order-three generators give an
endomorphism of the canonical cover fixing their product. It
descends because the source relation kernel maps into its central
kernel. Its finite quotient map is an automorphism; centrality and
the stem property then show its image contains the central kernel
and hence the whole finite cover. This supplies the full finite
certificate required by the previously proved image theorem.

The exact pure abelianization is C72^2, and both named generators
have order 72. Thus the raw exponent correction has parameter in
72 Zhat, and the actual normalization preserves the entire retained
source record. The ternary frames and signed CM values are the
previously certified ones, giving an actual normalized parity-one
element with pentagon identity at Gamma12.

## Scope and minor typography

The result proves an actual gentle-group survivor at this specified
finite five-point target, using the full canonical cover. It does
not assert survival at every deeper coefficient modulus. That is a
separate current calculation.

The only issue found in the proof text was cosmetic: the superscripts
`C_{24}^{,2}` and `C_{72}^{,2}` in QCS.2 contain extraneous commas;
this was reported to the author.

The integral homology facts use the same independently opened
primary source as the A.4.55 audit: Weibel, *An Introduction to
Homological Algebra*, Chapter 6, pp. 163, 180 and 195--196,
https://math.mit.edu/~hrm/palestine/weibel/06-group_homology_and_cohomology.pdf.
The relevant maps are the localized integral LHS homology edge maps,
not a comparison of unrelated abstract multiplier groups.
