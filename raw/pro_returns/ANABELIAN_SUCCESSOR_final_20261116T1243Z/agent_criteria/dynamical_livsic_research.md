# Periodic holonomy and the Verschiebung obstruction

Status: exact assessment of a proposed route, not an existence theorem for A3 or an exponent bound for AR20.

## Arithmetic Frobenius

For a geometrically connected normal variety U/F_q and a unit A on U, the finite etale Kummer torsor z^(q-1)=A has its closed-point Frobenius given by the norm of A. If every such Frobenius is the identity, finite-cover Chebotarev makes the torsor trivial. Consequently A=B^(q-1), which is the arithmetic-Frobenius coboundary Frob_q(B)/B. This is the finite torsor formulation already available in the scalar-Jacobian case of AC.35. It does not directly apply to the Verschiebung map on a general Jacobian.

## An exact counterexample for actual Verschiebung

Let E/F2 be y^2+xy=x^3+1. Its four rational points are O, T=(0,1), R=(1,0), and -R=(1,1), with 2R=T and 2T=O. The curve is ordinary. Write pi for its relative Frobenius and V for Verschiebung, so pi V=[2]. The doubling formula gives

    x([2]P)=x(P)^2+1/x(P)^2,
    x(VP)=x(P)+1/x(P).

Set b=(x+1)/x. Then, as rational functions,

    b^2=(x composed with V)/x.

Every V-periodic point avoids the zeros R,-R and pole T of b: those points map successively to T and O, while O is fixed and b(O)=1. If P has period m, telescoping therefore gives

    (product_{j=0}^{m-1} b(V^j P))^2=1.

In characteristic two this implies that every periodic holonomy is exactly1.

Nevertheless there is no rational c in Fbar2(E)^times with b=(c composed with V)/c. If there were, h=x/c^2 would satisfy h composed with V=h. A nonconstant rational map h:E->P1 has deg(h composed with V)=2deg(h), so h must be constant. This would make x a square up to a constant. But div(x)=2(T-O), and T-O is a nonzero two-torsion divisor class: it cannot be principal on a genus-one curve. Thus x is not a square and no such c exists.

The cocycle does become a coboundary in the perfection, using c=sqrt(x). The counterexample occurs for a genuine etale p-power Verschiebung isogeny of a proper ordinary abelian variety, not merely for an unrelated polynomial map.

## Consequence for the proposed theta argument

An algebraic Livsic statement saying that trivial periodic holonomies force a *rational* coboundary is false in this setting. Any corrected statement must retain purely inseparable and p-primary divisor-class ambiguity. A possible correction after passage to the perfection would still have to be proved and then shown to contradict the particular Picard-cohomology line and theta zero divisor; neither step is established here.

There is also a separate logical gap: a nontrivial return on one periodic character orbit is insufficient for the rational relative class-number criterion. For a cyclic cover every relevant primitive character orbit must avoid eigenvalue1. Failure of A3 only requires at least one bad orbit in every prime cyclic cover; it does not assert that all periodic holonomies are1. Thus even a valid corrected Livsic theorem would not on its own establish A3.

## Sources checked

Searches for an algebraic finite-field Livsic theorem returned the standard topological Livsic theorems with compact hyperbolic/closing and Holder hypotheses, not a theorem covering this situation. The exact counterexample above is self-contained. The integral connection and parameter-space distinction is documented by Zhao Lemmas1.4 and2.7--2.8, already audited in unitroot_tower_research.md. No topological Livsic theorem is imported into the finite-field algebraic argument.
