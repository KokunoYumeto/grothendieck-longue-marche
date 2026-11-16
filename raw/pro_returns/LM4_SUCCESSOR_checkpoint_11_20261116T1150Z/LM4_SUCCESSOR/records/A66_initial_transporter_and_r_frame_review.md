# Initial-C transporter and the r-frame gate: precise research review

This is a proof review for the next A66 construction, not a new numbered
statement in the frozen ninth-checkpoint paper. We distinguish the
construction-selected initial frames from arbitrary equivariant frames.

## 1. The extra condition available in the initial construction

A33 constructs its dyadic r-reflection D'_2 by conjugating the original
full Galois r-reflection D_2 and applying A16 followed by coprime
conjugacy. In A16 the prescribed reflection is retained literally;
the final coprime correction conjugates it. Thus D'_2 is still conjugate
to D_2. The relevant conjugators in A33 can be chosen pure: its matrix
transporter is identity modulo two and its final correction lies in
the level kernel. The dyadic s-reflection T_2 is the original full
Galois s-reflection.

For that full Galois involution b, there is a pure transporter between
s T_2 and D_2. To see the actual comparison, write b as the image of
standard conjugation under a peripheral automorphism nu, and write
nu(s)=u_s s u_s^-1 and nu(r)=u_r r^epsilon u_r^-1 with pure
u_s,u_r. The normalized pure-frame uniqueness gives

    T_2 = u_s^-1 b u_s,
    D_2 = u_r^-1 nu(s) b u_r.

Consequently s T_2 and D_2 are conjugate by u_r^-1 u_s. This uses
actual conjugation in the extended source, not an equality of outer
classes. Composing with A33's conjugations gives a pure transporter
from s T_2 to its constructed D'_2 in the dyadic relative quotient.

Fix a congruence level N. The dyadic transporter has a finite image
g_N in Q_N. At every odd relative prime p choose any pure lift of
that same g_N. It sends s T_p to an involution with the same finite
image as the retained r-reflection D'_p=sc. The preimage of their
common finite C2 has pro-p kernel. The two involutions are complements,
so the coprime complement theorem conjugates one to the other by an
element of that kernel. This correction leaves g_N unchanged. The
resulting transporters therefore glue in the actual fiber product
over Q_N.

To pass to initial C, add existence of such a pure transporter to the
compact frame conditions in A33. This is closed: it is the projection
of a closed subset of the compact product of frame and transporter
spaces. For finitely many levels use their common multiple and the
preceding construction, so the finite-intersection property remains.
Hence the initial C-frames can be selected with a pure transporter

    g_C (s_C d_s,C) g_C^-1 = d_r,C.

The printed A33 statement did not explicitly name this additional
closed condition. We therefore do not infer it for an arbitrary later
choice of norm-zero frames. The construction-selected frames admit it
without changing the initial action or the retained finite CM data.
A future formal use must state this selection explicitly.

## 2. Transporting an involutory s-frame through a pro-two residual

Let D -> C be the actual new source quotient with pro-two kernel P.
Assume b_D is an actual order-two automorphism covering b_C. In the
semidirect product E_D=D semidirect <b_D>, suppose an involution d_s
centralizes actual s and has the prescribed d_s,C image. Then s d_s
is an involution. Lift the transporter g_C above to g in D. Its
conjugate d0=g(s d_s)g^-1 is an involution over d_r,C.

Take the inverse image in E_D of the actual finite subgroup
<r_C,d_r,C> isomorphic to S3 in E_C. This is a profinite extension
of S3 by P. A16 gives a section retaining d0. Its order-three
subgroup and actual <r> are two complements to P in the inverse
image of <r_C>. Coprime complement conjugacy supplies p in P taking
the former to <r>. After conjugation, the retained reflection d_r
still has order two and still maps to the exact d_r,C; it inverts
actual r. The element J=b_D d_r lies in D and gives the required
negative r-conjugator, with the original literal C-image. The
corresponding positive r-frame follows from J=h_D(s) A.

Thus, under the explicitly selected initial transporter and an actual
old/new s-frame, existence of some involutory r-frame follows. Failure
of a convenient formula J=(q,s) is not an obstruction. This argument
does not itself supply the finite coordinates of that r-frame, and
it does not solve the s-frame equation, an action-square equation,
a scalar-refinement lift, or full order two in the original group.

The proof uses A16's actual prescribed-reflection lemma and ordinary
coprime complement conjugacy. All groups, kernels, and conjugators
above remain in their stated actual quotients.
