# E3: exact cyclic-three source maps after E65

This is a research certificate, separate from the frozen E65 theorem and
from the frozen E59/E62 batches. It records actual finite maps and their
complete correction images. It assigns no value to the restriction of
the E65 character Delta to full GT.

## 1. Literal cyclic-cover map

Let F be the free profinite group on the retained generators x,y, let
H3 be the kernel of x -> 1, y -> 0 in Z/3, and define

    delta3(x^3)=x, delta3(y)=y,
    delta3(x y x^-1)=delta3(x^2 y x^-2)=1.

These values on the actual Schreier basis define the continuous map.
They are precisely D5's positive-coordinate version of Enriquez,
Theorem 8.1 and Remark 8.6, not a new choice of a Kummer normalization.
The target map q3 sends x to [[1,2],[0,1]] and y to [[1,0],[1,1]]
in the literal group SL2(F3). The scalar c3 is the y-exponent after
delta3. On H3, the x-exponent after delta3 is the original x-exponent
divided by three: this holds on the printed free basis, hence on its
abelianization and profinite completion. It is exactly zero on F'.

With the section 1,x,x^2, use coordinates (k;a0,a1,a2), with multiplication

    (k;a)*(l;b)=(k+l; a_j b_(j+k)).

The actual induced source generators are

    x=(1;1,1,q3(x)), y=(0;q3(y),1,1).

For w in H3, coordinate j is q3(delta3(x^j w x^-j)). The coordinate
zero is therefore the required map. A faithful right permutation action
is (j,z) -> (j+k,z*a_j) on three copies of the 24-element matrix group.
Both the multiplication formula and the four Schreier basis values are
checked directly.

All N_B words are the same 97 retained Bass--Serre basis words used by
E59 and E62. The read-only source helper compares them word for word
with the earlier SL2(F5) certificate and supplies the inverse exact
F-word/B-word coordinate maps. Thus the domain N_B' below is literally
the same closed derived subgroup as in E62.

## 2. The single-coordinate image and its exact E62 comparison

The program `a_cm_kummer3_probe.py` evaluates all 4,656 pair commutators
of these 97 words. Their coordinate-zero values include all 23
nonidentity matrices in SL2(F3). Every matrix is saved with an actual
commutator word in N_B'. Therefore

    q3 delta3(N_B') = SL2(F3).

The upper bound is the displayed 24-element target; the saved actual
preimages give the reverse inclusion without relying on an abstract
group identification. For each of the 24 original G6 words f0, the
program prints a word u in N_B' with

    q3 delta3(f0*u) = q3(f0*u),  c3(f0*u) = 0 mod 3.

This is the finite D5 equation because q3(y) has order three. Since
N_B' is contained in K6 and in F', the original G6 word and its
abelian coordinate are retained. This test alone makes no assertion
about the other Ferrari targets.

There is, however, an exact simultaneous comparison with the already
proved E62 corrections. Write C for E62's actual image of N_B', of order
2^24, and use the two maps on that identical source:

    N_B' -> C,
    N_B' -> SL2(F3),  u -> q3 delta3(u).

Their joint image is subdirect. Every common quotient is a two-group.
The literal matrix group's abelianization is C3: the Cayley-graph
character sends q3(x) and q3(y) to 1, and its kernel is the enumerated
quaternion subgroup of order eight. A nontrivial finite two-group has
a quotient C2, so SL2(F3) has no nontrivial two-group quotient. Goursat's
two actual projection kernels consequently give the full direct
product C x SL2(F3).

It follows that each specified E62 correction can be retained while
solving this single K3 equation: after choosing its preimage u0, choose
v in N_B' with C-value 1 and q3 delta3(v) equal to the required final
matrix correction. The word f0*u0*v retains the actual complete E62
source and target values. Its c3 value modulo three is zero because
q3 delta3(f0*u0*v)=q3(f0), f0 belongs to F', and the displayed matrix
abelian character sends both q3(x),q3(y) to 1. This is an exact finite
comparison and does not assert a full profinite GT lift.

Saved initial probe runtime: 0.454455 seconds.

## 3. All three based cyclic coordinates

The program `a_cm_kummer3_orbit.py` enumerates the whole finite N_B
image in the displayed wreath product. It obtains the derived image
from explicit commutators and closes it under conjugation by actual
N_B generators until stable. Every added generator is a derived word,
and the final normal subgroup contains all original generator
commutators. These two containments prove the derived-image equality.
It repeats the same procedure for the second derived image.

The exact orders are

| Image | Order |
| --- | ---: |
| N_B | 13,824 |
| N_B' | 1,536 |
| N_B'' | 512 |

All three projections of N_B' are onto SL2(F3). Their three abelian
characters are equal, and the second derived image is exactly the
product of the three order-eight character kernels. Thus the
abelianization of the complete three-coordinate derived image is C3.
The JSON also retains a tested preliminary guess under the key
`equals_balanced_SL23_cubed`; its value is intentionally false. The
actual charge image is the diagonal {(a,a,a)}, which is smaller than
all sum-zero triples. Both asserted kernel equalities are true.
It again has no nontrivial two-group quotient. The simultaneous
comparison with E62 therefore remains a full direct product.

No equation has been assigned to a conjugate coordinate merely because
the coordinate exists. The asserted full-GT equation is D5's literal
delta3 equation; all additional coordinates here retain its actual
source kernel and conjugation maps.

Saved runtime: 0.081874 seconds.

## 4. The complete B-core

The program `a_cm_kummer3_core.py` induces the preceding 72-point F
action through the actual six cosets of F in B=C2*C3. For the retained
section t_q, its transition at b is

    delta3-induced(t_q b t_(qb)^-1).

This gives a faithful 432-point action of the actual induced image.
The program verifies s^2=r^3=1, inverse transitions, every elementary
wreath product, and the literal x,y and all 97 N_B comparisons at the
base coset. It then supplies complete Schreier certificates for the B,
N_B, N_B', and N_B'' images. Every literal word DAG is independently
replayed in Python, and every final Schreier relation is replayed by
the existing complete-chain verifier.

| Image | Exact order |
| --- | ---: |
| B | 2^30 * 3^7 = 2,348,273,369,088 |
| N_B | 2^27 * 3^5 = 32,614,907,904 |
| N_B' | 2^27 * 3 = 402,653,184 |
| N_B'' | 2^27 = 134,217,728 |

In particular, even the complete six-coset orbit has derived-image
abelianization C3. This proves, through the same actual projection
maps, that its common quotient with the E62 binary correction group
is trivial. Its full joint correction image is the direct product.

The initial attempt to compute the second derived image used all
4,600 strong generators and was killed by the memory limit. The
original program, stdout, stderr and failed input are preserved in
`A_K3_core_initial_attempt/` with hashes. The B, N_B and N_B' complete
certificates had already passed. The revised program first computes
a complete greedy certificate selecting 16 actual strong generators,
checks that its order is unchanged, and then computes the second
derived image from those generators. This completed successfully;
the saved resumed-run time is 0.609370 seconds, and individual complete
certificate times remain in the JSON. No incomplete run supplies an
order or an exclusion.

## 5. Remaining exact question and next comparison

E6 already imposes the five finite distribution equations for
N=2,3,4,6,12 together with the c_N multiplicative equations in the
actual matrix quotient. Its complete 459-point source was not joined
to E62. The next finite comparison is the actual common image of
N_B' in that distribution source and in E62's C, retaining all binary
overlap characters. The preceding results do not decide that common
image, and do not decide Delta on full GT.

The primary-source audit continues to retain the scope of every map:
Enriquez supplies the full-GT D5 equations; the harmonic identities in
Furusho's Theorems 3.1/3.4 also use the additional relation IV; and the
opened Nakamura--Tsunogai accessory formulas have Galois source. No
value of Delta is assigned from those more restricted formulas.
