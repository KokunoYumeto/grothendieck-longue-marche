# Independent root review of C.35

Reviewed 2026-11-16 05:15–05:20 UTC. We read the full formal proof
and standalone matrix checker, then ran the checker successfully.

The argument passes review for every full GT0 involution. It does not
use the pentagon. The canonical-duality calculation is an identity in
the full free profinite group: iota alpha=Inn(f) alpha iota and
u=f alpha(u) make (iota u)^(-1) a second solution in F-prime, so full
uniqueness gives the two-cycle. No uniqueness statement is made for
the finite quotient.

The finite computation is a necessary-condition argument applied to
the evaluations of the actual full words. A commutator word is
unchanged by central changes of its inputs, also in the profinite
case by continuity and its zero abelian exponents. The two quaternion
duality sets were checked directly. At (A,B), with Z=(AB)^(-1)=J,
the substitutions f(Z,A)=A F3 A^(-1) and f(B,Z)=S F0 S^(-1) reduce
the exact negative hexagon to F1 F3 Ad(BS)(F0)=1. Since
BS=-(1+I), this gives F1 in {1,I}. Its intersection with the
duality set {plus/minus1,plus/minusK} is {1}. The canonical equation
then makes U1 fixed by the displayed T-conjugation, forcing U1 to
be central. For the other equal-order pair, precisely the value
plus/minusJ would collapse its projective generators; duality
excludes it. The two mixed-order cases are automatic in A4.

The four displayed Aut(A4) orbits each have24 elements and exhaust
all96 ordered generating pairs. Conjugation by GL2(F3) realizes
the automorphisms, so the four checks cover every epimorphism from
F to A4. The requested one-sentence proof that SL2(F3)'=Q8 was
added and independently checked: Q8 is normal, the quotient is
cyclic of order3, and [A,I] together with its A-conjugates generates
Q8.

The discovery enumerations are retained as records, but finite
assignment realizability is not part of this proof. The actual
full-word identities are the input. Full generation remains open.
