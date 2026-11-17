# Independent correction of the symmetric chronological transport convention

Research verification, after B90-B92 were accepted. It changes the
interpretation of the stored finite crossing lists, not their exact
geometry or any conceptual theorem.

The exact PL half-twist certificate in
work_DE/next_marginal_source/check_cut_Artin_convention.py identifies a
positive left-below crossing with geometric push
phi_i(x_i)=x_i x_(i+1) x_i^-1, phi_i(x_(i+1))=x_i.
The actual crossing engine uses exactly this left-below positive sign.

The art() routine, however, updates its current image dictionary by
A <- A compose phi_i. Thus on a CHRONOLOGICAL list
W=(w1,...,wn) it returns phi_w1 compose ... compose phi_wn.
Geometric push is the other composition order. Consequently:

    push(W)=art(reverse(W)),
    pull(W)=art(negate_each(W)),
    F_start=pull(W) compose F_endpoint compose push(W).

For a lasso with chronological whisker W, transported local node
generators likewise use pull(W), not art(W). The raw crossing paths,
signs, discriminant and linking data remain unchanged. Previously
converted based automorphisms and Fox columns must be retained as
superseded convention-failure artifacts and regenerated.

The independent verifier
work_A/code/verify_symmetric_chronological_transport.py
reads the actual endpoint geometry and raw bridge/old-loop words; it
does not modify those inputs. It independently implements free reduction,
the substitutions, and common-inner-conjugator testing. Genuine stdout:
work_A/code/verify_symmetric_chronological_transport.out.
Complete hashed data:
work_A/symmetric_chronological_transport_verification.json.

Results: all42 bridge inverse substitutions, all21 transported F squares,
all42 inverse substitutions per old action, and the exact full-boundary
word preservation pass. For each of the six actual old-base loops the
commutator F A F A^-1 is an inner automorphism on all21 generators.
The exact inner-word lengths, in order0,1,zeta,zeta^2,zeta^3,zeta^4,
are0,11,62,66,68,22. The first loop commutes literally.

DE independently obtained the same six words and produced an additional
exact two-adjacent-half-twist PL certificate, proving the chronological
composition rule geometrically rather than selecting a convention solely
because it passes an outer-commutation test.

The endpoint q=9/25 Möbius and paired peripheral basis itself is unchanged.
Its exact cut-polynomial reads, involution square, peripheral labels,
full Nielsen inverse substitutions and one-sided filling types were read
and checked independently. The retained five paired basis elements give
an F-stable old-F5 splitting. The actual old-base action may still require
its recorded inner corrections; no such correction is discarded.

No source-ideal equality, syzygy vanishing, full fixed lifting, or compact
coefficient comparison follows from this verification. The corrected
finite matrices must still be matched to the actual paired source marking
before any Tate calculation is used.

