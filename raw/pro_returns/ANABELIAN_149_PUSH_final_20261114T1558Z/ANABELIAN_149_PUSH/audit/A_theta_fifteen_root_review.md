# Independent root review of the exact theta-fifteen example

Date:14November2026, approximately12:51UTC.

Reviewed audit/A_theta_fifteen_candidate.md and the complete
audit/A_theta_Hankel_scan.md. Verdict: approved for integration as
A.C2.18, using the independently approved A.C2.17.

The general high-jet criterion is complete. Riemann–Roch gives
exactly the displayed basis of the degree-n pole space. A nonzero
kernel vector gives a nonzero function vanishing at least n times
at the selected unramified point; the total pole bound is n, so
its whole divisor is forced. There is no extra solution with B=0,
and no omitted branch-point solution for odd torsion on ordinary
theta. Multiplying row i by D^(2i) and column j by D^(−2j) gives
the stated polynomial matrix. A positive answer requires every
maximal minor; early termination is used only after the gcd is a
unit away from the two excluded branch coordinates.

The small-order exclusions used by the example have direct
symbolic proofs independent of the broad scans. The cubic
obstruction is alpha, which is nonzero. At order five, the first
minor is (T^4+T+alpha)^4, and modulo its radical the other minor
is alpha^2, which is also nonzero. Hence theta has no point killed
by3 or5, including the absent origin.

The root wrote and ran a separate exact implementation:
code/A_theta_fifteen_root_independent.py/.json. It uses SymPy
Groebner reduction over F2 with alpha^2+alpha+1 and
t^2+alpha*t+1, rather than the author's polynomial engine.
It verifies the complete degree15 norm, phi(t)=alpha*t, all local
A/B values, the two field identities, the theta-five obstruction,
and every character orbit. All assertions pass. The author's
certificate was also rerun and passes.

The local divisor argument is valid: B(t)=t is nonzero, so only
the selected unramified point has a zero of the norm's order15;
B(0)=B(1)=alpha gives both simple poles; the monic x^6*y term
has unique pole order13 at infinity. Dividing by u^7 gives
15(R−Btheta). Since the proper divisors1,3,5 have been excluded,
the theta class has exact order15. The associated Kummer torsor
is geometrically connected and étale.

The primitive character cycles are killed, while the order3 and
order5 cycles survive. Thus the exact two-rank is8, and those
surviving characters have trivial common deck kernel. The
primitive group-ring endomorphism still annihilates all two-primary
torsion. A.C2.17, rather than the earlier nonfaithful-deck
criterion, supplies the section-separation conclusion.

The table of ten unordered coefficient triples was checked
against the existing3/7/9 constructions and the new15 case.
For the additional seven-family triples, t^2+t=U with U in
{alpha,alpha^2} gives t^5=(t+1)^5=U, as asserted. The resulting
classification is explicitly confined to normalized nonzero F4
triples, equivalently ordinary F4 curves with three rational
hyperelliptic ramification points. A constant Artin–Schreier term
is removed after a finite extension. No classification of
Frobenius-permuted branch triples is inferred from this table.

The wider bounded prime-power scans remain labelled as bounded
audit evidence. The positive proof uses only the exact15 norm
and the complete small-order exclusions needed for exact order.
No universal prime cutoff or unbounded absence assertion is made.
