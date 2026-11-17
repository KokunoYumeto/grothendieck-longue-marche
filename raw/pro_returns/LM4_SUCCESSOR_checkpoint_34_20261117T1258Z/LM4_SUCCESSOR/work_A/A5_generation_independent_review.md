# Independent review of the proposed all-A5 generation proof

Reviewed work_CE/research_A5_generation.txt during checkpoint05 source freeze. **Pass**, with the exact19-orbit passport certificate retained as an explicit finite input. This note is not a separate formal statement and does not change the frozen register.

## Full automorphism and section count

Canonical duality gives iota(u)=u^(-1). Therefore v=Inn(u^(-1))iota is an actual involution, swaps x and y'=u^(-1)yu, and commutes with alpha. Indeed alpha(u)^(-1)=u^(-1)f and iota alpha=Inn(f)alpha iota give the commutation directly. Thus tau=alpha v is an involution whose integral homology action is minus swap and whose mod-two action is the free rank-one F2[C2] module.

For E=F semidirect_tau C2, the two-row Hochschild--Serre spectral sequence has H^n(E,F2)=F2 for n>=2. The positive cohomology of the free H1(F,F2) module vanishes; the sole possible transgression is zero because the extension splits. The general full finite-vcd restriction/localization theorem used in C8/C28 consequently forces exactly one section class. No assertion about the full centralizer is needed.

If tau acts trivially on a finite quotient and reverses the primitive third cusp, the two local cusp reflections are actual involutions. For a lift e reversing z, its square lies in C_F(z)=<z>; because it commutes with its own square but inverts <z>, torsion-freeness of that full procyclic group forces e²=1. The two reflections e,ze are sections. Their unique section class maps to the same central(1,c) in the finite direct product, forcing qz=1.

## Finite reductions

The19 Aut(A5) orbits described in the CE certificate cover all generating pairs. For a pair involving orders3 and5, every conjugated pair generates because a proper A5 subgroup cannot contain both. In the six one-order-two cases, the negative passport preserves the quotient kernel and a five-cycle class, so the induced automorphism is inner. A proper substituted subgroup is A4,S3 orD5. Its normalizer is itself. An element of A4 cannot invert a three-cycle. In either odd dihedral subgroup the inverter centralizes the named reflection and hence equals it. The corresponding global section has central finite image; the third-cusp section-class incidence gives a product of order at most two, contradicting its odd cusp order.

For different five-cycle-class pairs, cyclic collapse would have exponent ±2. But the induced v swaps the two collapsed powers and has order two, forcing exponent square1 modulo5. This is impossible.

The remaining same-order passports have inner negative and swap actions, because a five-cycle class is preserved. A proper(3,3) image A4 is excluded as above, leaving cyclic order3; a proper(5,5) image is cyclic order5. The collapse exponent is ±1.

In the plus case, v acts trivially on the odd cyclic generator. Its inner representative is an involution in that odd centralizer and hence is1. Thus q(u) is exactly the nontrivial swapping involution t. For arbitrary lifts to SL2(F5), T²=-1: an element squaring to1 in determinant-one characteristic-five matrices is±1, so a nontrivial projective involution cannot have a lift of order two. The two possible U=±T give U Ad(T)(U)=U²=-1, contradicting full duality. Central changes of the arguments do not affect the commutator word.

In the minus case, alpha and v are commuting inner involutions that invert the same odd cyclic subgroup. Their representatives are reflections in its odd dihedral normalizer, and commuting reflections there coincide. Thus tau acts trivially on the A5 quotient. The checked one-section lemma forces the nontrivial third cusp to vanish, the final contradiction.

No maximal pro-p, finite-level uniqueness, or unproved full conjugacy is substituted for the actual full identities in this proof. The conclusion is finite A5 generation for GT0 involutions; no relative generation over the A5 base follows merely from it.
