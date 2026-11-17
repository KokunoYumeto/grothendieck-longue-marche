# The actual universal-dihedral image cannot compare the two cusp units

Research note, 17 November 2026, after checkpoint27. Both main decisions remain Open. This is an exact calculation in the actual quotient of A.45, not a new finite target or a census, and not a formal proposition added to the register.

We retain the full profinite group F on x,y and the canonical negative-GT0 data of the four reviewed checkpoint27 notes. Write

    pi:F -> D=<a,T | a^2=1, aTa=T^-1>,
    pi(x)=a, pi(y)=aT, pi(u)=T^k,
    k in 2 Zhat, d=2k+1 in Zhat^times.

Here D is the full profinite infinite dihedral group Zhat(T) semidirect C2(a). A.45 proves that the actual involution alpha induces the identity on D. The actual v=Inn(u^-1)iota descends to the following continuous involution of D:

    v(a)=T^-k(aT)T^k=aT^(2k+1)=aT^d,
    v(aT)=T^-k a T^k=aT^(2k),
    v(T)=T^-1.

Thus pi extends to the genuine homomorphism F semidirect <v> -> D semidirect <v> with the indicated action. The symbol v on the right denotes its order-two head, not an element of D.

Put e=(xu)v as in the reviewed half-rotation proof. Its image is

    e_D=aT^k v,    e_D^2=T^(d-2k)=T.

Conjugation by a and by v each inverts T. Consequently e_D centralizes the entire closed rotation group Zhat(T). For the uniquely normalized q, q_ab=(t,-t); its image under D -> C2(a) is therefore trivial. Hence pi(q)=T^r for some r in Zhat, and

    pi(q)^-1 e_D pi(q)=e_D.

This conclusion does not identify r with the abelian coordinate t. The square identity e_D^2=T, with T of full profinite order, gives a faithful continuous power map Zhat -> closure<e_D>. In particular powers by the actual profinite k and d are legitimate, and

    e_D^d=e_D^(2k+1)=e_D T^k
         =aT^k v T^k=a v.

Every unit d is odd, so pi(x^d v)=a v. The canonical even obstruction therefore satisfies

    pi(Omega_alpha)
      =pi((x^d v)(q^-1 e q)^(-d))=1.

This holds for every actual q supplied by the reviewed cusp normalization; it requires no equality a_reg=d. Thus the universal-dihedral calculation by itself cannot establish that equality or the full nonlinear vanishing. Its abelian image still imposes the already known parity condition: (Omega_alpha)_ab=((d-a_reg)/2,-(d-a_reg)/2), and both units are 1 modulo 4. We do not infer any converse from this quotient calculation, nor construct an actual involution with unequal units.

Dependencies read at use: the complete A.45 proof in work_A/A_involutions.tex was read in the checkpoint27 review; the complete canonical-frame and coefficient-comparison notes were reopened after compaction. Root also reopened the complete C.29 and C.30 proofs and the complete A.39 proof after capture. A.39, with its specified A.6/A.36 dependencies, supplies the previously established descent of an actual full cusp conjugator into GT0 or GT when applicable. No new independent proof of A.6/A.36 is claimed in this note.
