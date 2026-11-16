# Independent saved-source audit of A149

Source: sections/coherent_inert_radicand_update_agent.tex.
Final corrected certificate: code/coherent_inert_radicand_update_certificate.py
and its retained output. Independently rerun after the final source edits:
PASS (960 stable residue checks, 465 coefficient projection bounds).

The ray-class proof uses the actual field Q(mu3), its class number one,
the inert prime11, and the surjection of mu3 onto the three-primary
part of F121*. Higher ray conductors add only eleven-groups. The
normal-generation argument for inertia at three is exact for a finite
three-group, and applies again to the primary Hilbert class fields.
The subsequent class-group transfer to intermediate root fields is
valid because every nontrivial intermediate extension is totally
ramified at the unique three-prime.

The local norm cases retain the actual algebras. At the degree-one
eleven-prime the residue norm has no three-primary restriction. At
the degree-two prime the target and radicand characters are2 and1,
with valuations1 and8, giving the stable equation 8*2-1=0 mod3.
The explicit norm of the uniformizer agrees with this sign. The
two-adic construction uses one actual degree-one root factor, not
an assertion that every root algebra is split. At all other finite
places the unit/unramified argument is valid. Fixed-valuation
compact fibres justify the compatible local families.

For a finite module split by L_m, a locally trivial H1 cocycle
restricts to an everywhere unramified abelian three-character over
L_m and is therefore zero. The full three-decomposition image and
its single local coboundary witness then kill the descended global
class. Finite Poitou--Tate duality gives precisely the H2 localization
injection used in the proof.

The final version kills the image of the connecting defect in each
D/(3^r,T^r) using one finite norm and the actual map from the
permutation augmentation kernel. This avoids a separate local
inverse-H1 comparison. The finite H1 groups are Mittag--Leffler,
so their Milnor term vanishes. The complete coefficient sequence
has a continuous underlying Z3 splitting. Thus the single global
H1(V_z) lift exists. The nested compact-coset proof of
V_z=lim_j Z3(1)[Roots(Z^(3^j)-z)] is correct, and Shapiro sends its
literal basis transition to field norm. This produces one global
compatible completed S-unit family with the specified first beta.
The final argument over Q uses vanishing H0 for the finite root
fields and gives exactly the coefficient-three one-variable lift.

One finite arithmetic witness in the initial draft was corrected:
the old unit equation with X=1 requires Y^24=-1/2=5 modulo11.
Its roots are2 and9. The earlier values5 and6 were roots of -2
and did not solve that equation. The corrected source and executed
certificate now check the literal equation -2*Y^24=1. This correction
does not affect the class-field or compatibility proof.

Final outcome: complete saved-source audit passed. The theorem
concerns the fixed rational coefficient3*11^24, target-2, and
their three-primary norm tower. It supplies no ordinary unit-equation
pair or full metabelian lift.
