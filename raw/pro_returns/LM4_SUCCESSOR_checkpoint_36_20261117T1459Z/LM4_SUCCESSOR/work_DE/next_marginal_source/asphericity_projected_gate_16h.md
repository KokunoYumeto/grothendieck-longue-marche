# Actual asphericity and projected fixed-source gate: scope audit

Research only, 2026-11-16 16:45 UTC. No new numbered statement.

The actual symmetric surface is the 23-line/four-conic complement specified
in symmetric_deletion_fixed_lifting.md. Its both-filled surface and each
one-sided filling are genuine punctured-sphere bundles and are aspherical.
The symmetric surface itself has 64 transverse mixed nodes over 18 allowed
product values. Its product projection is therefore not the same bundle.
Neither normal crossings nor contractibility of individual lifted divisor
components proves a graph-product presentation or asphericity.

An actual equivariant meridian normal form would be useful: the first
coinvariant obstruction module forgets the based braid conjugations in the
node relations. Those conjugations are exactly what a graph-product
identification would have to control. No such identification has been
proved. B89 and the first-module fixed-lifting result do not supply it.

## Primary-source boundary

Crisp, J. (2000). Symmetrical subgroups of Artin groups. Advances in
Mathematics, 152(1), 159–177. https://doi.org/10.1006/aima.1999.1895
Primary publisher abstract:
https://www.sciencedirect.com/science/article/pii/S0001870899918959
Institutional record: https://eprints.soton.ac.uk/29864/

The primary abstract was inspected in the literature search (search refs
turn841search0/1). Its fixed-subgroup theorem assumes a symmetry of an
actual Artin system and a suitable CAT(0) Deligne complex (in particular,
the known FC setting). Neither prerequisite has been identified for this
surface. The full proof was not read. A fresh publisher open at16:44:43
returned403 (turn846view0); this is not a successful full-text audit.
No theorem from this paper is applied.

## Tube-versus-source distinction

Root independently read Tibăr, arXiv:math/0202123, Theorem1.1,
Proposition3.5 and Remark3.6. The nongeneric-member statement concerns a
tube; replacing it by the member requires an additional actual homotopy
comparison. In the local pencil eta=(vw-1)/(w-1)^2,

    eta+1 = w(v+w-2)/(w-1)^2.

The actual source is eta=-1, but its boundary fiber also contains removed
w=0. For an added constant component v=u, its pencil equation is

    eta*w^2 + (-2*eta-u)*w + (eta+1) = 0.

At eta=-1 its two roots are0 and2-u. Thus one added puncture escapes into
that old boundary component. A relative van Kampen calculation of the
whole tube before and after filling these components could be relevant,
but the boundary contribution cannot be discarded. No relative kernel
surjectivity is inferred from the tube theorem.

## Mod-two target caution

Conditional on the standard Stein covering and Stein CW-dimension facts,
mod-two acyclicity of the universal cover would be equivalent here to
asphericity: the universal cover is simply connected and has the homotopy
type of a2-dimensional CW complex, so H2 is free abelian. Vanishing mod2
homology forces H2=0, and Whitehead then gives contractibility. This is a
scope observation, not a new verified primary-source theorem in the paper;
the exact Stein references have not been audited in this component.

## Remaining target

Prove the actual projected equality p(pi1(Z)^F)=H, or find another
geometric description sufficient for it, while retaining the independent
nonabelian fixed-lifting gate through M=[N_A,N_B]. Neither gate is settled
by the first-module calculation. No new finite-group census or additional
general countermodel is proposed.
