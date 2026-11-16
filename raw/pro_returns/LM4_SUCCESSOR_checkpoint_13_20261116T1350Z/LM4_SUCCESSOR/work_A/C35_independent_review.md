# Independent review of C.35

Reviewed the full formal proof at the end of work_CE/C_further.tex and its exact matrix output. **Pass.** No full pentagon assumption is used; the scope is every full GT0 involution.

1. With iota interchanging x,y, the full identity iota alpha=Inn(f) alpha iota follows by checking both generators and f(y,x)=f(x,y)^(-1). Applying it to u=f alpha(u) produces another F' solution (iota u)^(-1). Full R1 uniqueness, not finite-quotient uniqueness, gives canonical duality.
2. A commutator word is unchanged when either finite matrix argument is multiplied by central -1. This follows from zero abelian exponents and remains valid for continuous profinite words.
3. The displayed S conjugation gives the correct binary duality restriction W1 in ±{1,K}; conjugation by J gives W2 in ±{1,I,K}. These are exact eight-element quaternion calculations.
4. At (A,B), Z=J, f(Z,A)=A F3 A^(-1) and f(B,Z)=S F0 S^(-1). Substituting into the negative hexagon gives F1 F3 Ad(BS)(F0)=1. Since BS=-(1+I), this is exactly the stated rho equation. The possible value rho(F0)^(-1)F0 is1 or I. Its intersection with ±{1,K} is1, so f(A,B)=1.
5. The full canonical equation now reads U1=u(A^(-1),B^(-1)). The displayed T induces precisely this substitution and negates K, so duality plus T-fixedness forces U1=±1. This is the necessary use of the actual involution/coboundary, not just arbitrary duality.
6. The (3,3,3) collapse is exactly conjugation by the projective J; binary duality already excludes its two lifts. The mixed-order cases are immediate because projective commutator values lie in V4. The four orbit types account for all96 generating pairs:24 mixed each way and48 order-three pairs split into two24-element Aut-orbits.
7. Arbitrary lifts of the A4 generators to SL2(F3) define genuine evaluations of the free profinite word. Automorphism equivariance and central-input invariance transport every calculation correctly. No finite table is asserted to lift to a full solution.

A separate verification of the discovery pentagon witness found an honest B4 representation: sigma1=sigma3=A^(-1), sigma2=C^(-1), with A=(1,1;0,1), C=(1,0;2,1). Its pure A24 differs from the discovered witness by central -1 only, which does not alter commutator-word values. Its three other pentagon argument pairs commute and the remaining two are reversed. Thus its obstruction is exactly binary duality, consistent with the final conceptual proof. The final proof does not need this witness.

The result proves finite A4 generation. It does not by itself prove generation in a relative pro-p extension over A4: the Frattini module there has higher multiplicities and modular cases at2,3. That further inference remains unmade.
