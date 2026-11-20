# Scan 025: limited mathematical work

Main reader: GPT-6 Astra Pro; effort inherited, not independently exposed.
Work performed during scan 025, after reading its supplied witness texts and
before main ink adjudication. This check is conditional on the literal live
argument finally established by the three readings. It does not decide any
letter, reference number, cancellation, or insertion.

## Claim checked

In a topos, if an epimorphism `e: G -> F` has quasi-compact domain G, then F is
quasi-compact. Here quasi-compact means that every jointly epimorphic family
of subobjects has a finite subfamily which is jointly epimorphic. Equivalently,
one can use covering families of arbitrary objects by passing to their images.

## Argument

Let `(U_i -> F)` be a family of subobjects whose union is F. Pullback along e
gives a jointly epimorphic family `(G x_F U_i -> G)`, since epimorphic families
are stable under pullback in a topos. Quasi-compactness of G supplies a finite
set J for which these pullbacks cover G. The composite

`coprod_{j in J} (G x_F U_j) -> G -> F`

is epimorphic. It factors through `coprod_{j in J} U_j -> F`, so that last map
is epimorphic too. Thus the finitely many U_j cover F, proving the claim.

## Exact limits of this check

This verifies only the descent of quasi-compactness along the displayed
epimorphism, under the stated definition and the usual topos pullback property.
It does not prove the cited existence of a suitable G, the quasi-compactness of
that G as a topos object, the coherence criterion invoked earlier, or equality
of the two constructibility notions. The references themselves are not looked
up. No published source is consulted, and no transcription is repaired to fit
the argument. The claim's connection to the finally read source paragraph will
be confirmed at page adjudication and recorded in the notes and check events.

## Adjudication connection

Confirmed when scan 025 was committed: all three complete readings and the main
local inspections retain the live epimorphism G→F followed by the assertion that
F is quasi-compact. The conditional argument above checks exactly that final
descent step. Notes s025-note10 and s025-note11 and their CHECK_EVENTS rows record
the result and its background assumptions. No reference was consulted.
