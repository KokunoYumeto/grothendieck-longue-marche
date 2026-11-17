# A finite noncentral detection level for the A76 obstruction

Proposed post-freeze strengthening. No formal source has been changed.

## General first-relation-module centralizer lemma

Let q:Pi=C2 amalg C3→Q be a finite quotient injecting the two factors,
let L=ker q, and put G=Pi/Phi2(L), where
Phi2(L)=closure([L,L] L²). Then

  image(C_G(s)→Q)=<q(s)>.

Proof. Let m∈Pi lift an element of C_G(s). Set J=q^-1(<q(s)>).
Both s and s'=m s m^-1 lie inJ, and have the same image inG.
Hence they have the same image inJ/Phi2(J), because
Phi2(L)⊂Phi2(J). The open Kurosh theorem expressesJ as a free
profinite product of finitely manyC2 factors and a finite-rank full
free profinite group: noC3 factor occurs, since q injectsC3 andJ/L
has order2. The full torsion theorem conjugates every involution into
one of thoseC2 factors. Distinct factors have distinct images in the
mod2 abelianization. Therefore s ands' are conjugate inJ. If
j^-1 s' j=s, then j^-1m centralizes s inPi, hence belongs to<s>.
It follows q(m)∈<q(s)>. The reverse inclusion is immediate.

This uses only open Kurosh and the full free-factor centralizer,
not a closed-subgroup Kurosh theorem or an assumed splitting of an
unknown negative extension.

The quotientG is finite. L is a full free profinite group of rank
1+|Q|/6, so |G|=|Q|·2^(1+|Q|/6). Equivalently finite generation of
L alone suffices for finiteness. The quotient has a direct finite
Schreier mod2 relation-module construction.

## Application to the original A76 datum

Let E be the actual finite six-cup quotient inA76.7 and L=ker(Pi→E).
It injects the two source factors. Its order is

  |E|=2^1620·72·7^13,

using the actual oldD0 order2^972·72·7^13 and the attained six
108-dimensional binary coefficient copies. Define

  G=Pi/Phi2(L).

By A76's finite transgression argument, EVERY full positive candidate
with the retained finite action preservesL; canonicalc also preservesL.
Thus both preserve its characteristic Phi2(L), and the negative
companion b acts on this same explicit finiteG. No new stability
assumption is being imposed.

For any full source s-conjugator beta retaining the original finite
frame, let n=beta^-1 b(beta^-1). Before b^2=1 has been proved at a
level, n is simply this group element; it must not be called a square
in a semidirect product by C2. Its E-image is a normalizer square
because b_E^2=1 there. Its E-image lies in the six-cup
kernel because the old frame norm is1. The exact invariant5 proves
n_E≠1 for every permitted higher action and frame choice. In
particular n_E∉<s_E>, since s_E has nontrivial oldD0 image.
By the centralizer lemma, n_G cannot centralize s_G. But the exact
identity

  b²(s)=n^-1 s n

then gives b_G²(s_G)≠s_G. Hence the full negative square is already
detected at this canonical finite noncentral relation-module level.
It is unnecessary to appeal only to the full-limit centralizer in
order to locate the failure.

This also rules out an involutory peripheral framed lift toG itself
when it has the prescribed old action, cusp normalization, coefficient
maps, and frame. The conclusion retains the same fixed old finite
frame scope asA76. A repaired frame or action may pass, and the
unframed main involution problem remains Open.


## Every iterated scalar test still passes

Let N0 be the kernel of the original finite quotient D0, and define
N_(j+1)=[N_j,Pi], with closed commutators. The original A56 kernel
U satisfies U=[U,Pi] and U is contained in N0. Inductively U is
contained in every N_j. Consequently every Pi/N_j is an actual
quotient of the SAME D=Pi/U. The original negative involution and
both norm-one frames therefore descend compatibly through every
iterated scalar refinement. Each quotient is finite: given finite
Pi/N_j, the subgroup N_j/[N_j,Pi] is central and finitely generated
in Pi/[N_j,Pi]; transfer to this central subgroup shows that its
exponent divides 6[Pi:N_j], because Pi_ab=C6. A finitely generated
abelian profinite group of bounded exponent is finite.

The existing ordinary full positive lift realizes all these data
simultaneously, while its prescribed-frame negative companion fails
at the single noncentral relation-module quotient G above. Thus
arbitrarily many actual scalar refinements, even with compatible
negative actions and both normalizer norms, do not suffice for this
framed order-preserving lifting problem. This strengthens the precise
failed-method conclusion; it does not exclude reselection of frames.

## Same old action, changed frame: the six-cup gate can pass

The separately stored witness A76_fixed_action_frame_reselection.json
keeps the original WE and PSHIFT exactly unchanged and keeps the
original finite H-head. It changes only the residual right s-frame.
The old source law verifies its conjugacy and normalizer norm, and
the actual six-cup source law verifies the new s-frame conjugacy and
norm in all six coordinates. The complete frame-only old-class space
has rank54 in276 binary affine variables. At each of the four Tate
weights8,11,20,23, exactly29 of4096 possible free-row values satisfy
the six-cup norm equations; the old class equations permit841 joint
choices. The first chosen representative already admits the required
old central correction. No change of the positive action is needed.

The independent verifier is
work_CE/code/verify_original_A56_frame_reselection.py; its fresh output
and original_A56_frame_reselection_independent.json both pass.

This refutes the attempted claim that the six-cup obstruction rules
out every frame for the fixed old action. It does not refute an
unframed full nonexistence statement: passing one finite test gives
no full involution. The enumerated family retains the initial C/H
frame head; unrestricted head changes are not claimed exhausted.
