# Positive intrinsic cubic family E.34

## Completed deliverables

The proof is in sections/E_intrinsic_positive.tex, with result ledger e_intrinsic_positive_results.json. The program e_intrinsic_positive.py has .out and .json outputs. The bibliography file records the two already existing verified keys and adds no duplicates.

## Exact result

Every geometrically abelian pro3 section class of the plus cubic which is unramified outside3 lifts to the full geometric pro3 arithmetic fundamental group. The entire abelian family is Z3^6 plus three order3 factors. Its toric image consists of the two independent Z3 multiples of Kummer3, with kernel Z3^4 plus three order3 factors. All classes in every one of these fibers lift fully.

The statement defines unramifiedness relative to the rational tangent above t0: its geometric cocycle factors through G_Q,{3,infinity}. It keeps the full G_Q arithmetic quotient. It does not confuse this with the total maximal pro3 quotient of G_Q or claim a full profinite geometric lift.

## Proof mechanism

The explicit cubic Puiseux map t=s^3, u=-s, v=-(1-s^3)^(1/3) identifies its actual based action with the restriction of the base free pro3 action. Hain-Matsumoto section8.5, opened directly, states the genuine based unramifiedness needed here.

Over K=Q(zeta3), that base action is trivial modulo its Frattini quotient. The kernel of this automorphism map is pro3. Therefore the action, and every abelian cocycle with this action, factor through the relative quotient of G_Q,{3,infinity} with pro3 kernel and quotient Gal(K/Q)=C2.

Kummer theory over the PID Z[zeta3] identifies the two K_S unit classes as zeta3 and lambda=1-zeta3. Milne's exact global Euler formula gives H2(G_K,{3},F3)=0. The maximal pro3 quotient is consequently free of rank2; the proof includes the finite-embedding-problem argument for this criterion. The relative quotient by C2 has 3-cohomological dimension1. Successive finite3-kernel embedding problems therefore lift every abelian section, and compactness of the finite section sets gives a continuous lift in the full geometric pro3 group.

For the exact abelian count, complex conjugation has plus4/minus6 on the rank10 Tate module, and rational 3-primary generalized-Jacobian torsion is C3 cubed by E.24. Finite coefficient H2 vanishes, and Milne Euler gives H1 order3^(6n+3) modulo3^n. This proves the claimed Z3 module structure, not only its rational rank.

## Scope

This is a complete positive classification of which abelian classes lift in the specified unramified family: every one does. It supplies no classification of the multiplicity of full nonabelian lifts and does not absorb the ramified classes obstructed in E.28 and E.31. E.32 concerns all completed toric pairs in the inherited quotient; its map does not identify these intrinsic fibers.
