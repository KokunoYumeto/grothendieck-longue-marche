# Full independent source review: A105 original CM parity

**PASS.** I read the entire proposed A105 mathematical source at its initial hash 4312128d9db75230c402b533b9942457c7f6edc986c2dc2c276802c7cb20b50c, then read the entire final diff to acd5911db9ecdea7bdc7c1f109efc70e802834aeff00ba5c81989b76ab031950. The final changes add the LM7_PUSH provenance prefix and rename the exponent of S to j_0; no mathematical assertion changes.

## Original inputs actually checked

I reopened and read the complete 327-line original E_cm_character_agent.tex, complete 267-line E_genus_one_sewing_agent.tex, and complete referee companion REFEREE_B_E61_E65.md. The final JSON binds their actual bytes. An initially truncated combined read was followed by complete untruncated reads of E61 and the referee report. The original E65 text was fully visible and read. I also read DE's complete source-binding note.

The original formulas have exactly the required composition order: Sigma=alpha c=(1,phi), Sigma(s)=s phi=beta_s s beta_s^-1, Sigma(r)=phi^-1 r=A_r r A_r^-1. The actual correction is V=U0^(8rho), with V4=I and V3=X^nu. The signed multiplier-one covariance and exact Phi=Y^nu X^-nu are the original E61.4/E65.9–10 statements, not inferred from arbitrary compatible matrices. The referee's pure-r-frame existence argument and its qualified Galois comparison were read; no external theorem is represented as freshly fetched in this audit.

## Complete proof checks

1. The quaternion subgroup and all stated X and j conjugations check literally. The actual norm solution U_nu=Y^-nu X^nu satisfies Phi beta_nu(U_nu)=U_nu. The fixed subgroup of beta_nu on Q8 is its center, so the finite solutions are exactly plus/minus U_nu, without manufacturing a second canonical profinite word.

2. The unique pure gamma conjugating s to su follows from the already bound finite-factor torsion/centralizer result. The exact actual equation alpha(su)=su gives alpha(gamma) beta_s=gamma. Consequently beta_s,ab=2 gamma_ab, and duality makes gamma_ab diagonal. The original mod-four signed map factors through exponent sums modulo two, so q4(beta_s)=I.

3. No homomorphism sends the order-two modular s to the order-four signed S. The proof first cancels s in identities inside the free kernel, then evaluates those identities. I independently checked B S B^-1=S Phi=X^nu S X^-nu; G=X^-nu H; X^-nu B=j(H)^-1 H; U=Y^-nu[S,H]X^nu. For H=S^aR^b, the two cases give S^(2a) and S^(-2a-1), whose squares are exactly [S,H]=(-I)^b. Thus (B^-1X^nu)^2=epsilon_u I in the correct inverse-frame order.

4. The pure r-frame has global zero abelianization: det(rho_cyc-I)=3 and multiplication by three is injective on Zhat. This is not a mod-three argument. The signed cyclic discrepancy consequently disappears on A_r, giving A_3 C A_3^-1=Phi^-1 C=X^nu C X^-nu. The six-element C-centralizer and the C3 character force A_3=epsilon_A X^nu C^-nu. Hence T3=epsilon_A C^nu and its scalar on the ORIGINAL line F3(1,-1) is epsilon_A.

5. The original E65 character epsilon_2 is on the MOD-THREE reduction of the W centralizer, as E65.3 specifies. S_out=S65^-1 generates the same C4 and gives the same exponent parity. Therefore the original two named bits have signs epsilon_A and epsilon_u, with the required common mod-four normalization. Galois vanishing gives Delta(alpha)=delta(alpha c), so their product is exactly (-1)^Delta(alpha).

6. The full-GT specialization uses only A103's actual d U11=1 and U11=epsilon_u modulo three. It gives epsilon_u=d mod3. The other sign epsilon_A is not determined. The concluding non-pure negative conjugator J_r=s phi A_r is correctly retained; its norm equation cannot be replaced by alpha(A_r)=A_r^-1.

## Scope and verification

No correction requested. This is an entire-source mathematical audit plus exact final-byte diff binding, not a program execution or rendered-page review. No old certificate was run. The result closes the identification with the original named CM frames, and leaves their actual vanishing question open.
