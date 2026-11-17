# Complete original LM7_PUSH E65 quotient-descent audit

New checkpoint34 audit, after the explicit release. The entire original LM7_PUSH E61 source (267 lines), E65 source (327 lines), and complete referee report (252 lines) were reread in bounded, untruncated chunks. This is an exact source/argument audit, not a fresh audit of every external theorem or execution of the historical finite certificates.

## Outcome and precise scope

The original E65 proof does not supply an intrinsic formula on unframed automorphisms of B/N1 when arbitrary pure quotient frames are allowed. The identity quotient automorphism already has two valid pure r-frames with identical abelian and signed-lift normalizations and the same s-frame, but opposite values of the original scalar recipe.

This does NOT prove that no character extension can exist with additional coherent chosen frames, or that the actual GT character cannot factor through a specifically identified action image. The constructed second frame is not asserted to be the image of an actual different GT element acting trivially on the quotient. In particular the actual full-GT CM parity remains open.

## Exact points where the original proof uses full frames

1. LM7_PUSH E61.1--2 and its first proof paragraph use C_B(s) intersect F=1 to make beta unique. This supplies the actual coordinate rho from beta^{-1}_ab. Its signed matrix formula E61.4 is a consequence of this original data and the exact cubic condition; it is not a prescription selecting an arbitrary quotient r-frame.

2. LM7_PUSH E65.1 explicitly states uniqueness of BOTH pure frames. The proof paragraph beginning with the torsion centralizers uses C_B(s) intersect F=C_B(r) intersect F=1. The same injectivity makes conjugation a compact homeomorphism onto the relevant orbit, hence makes the selected frames continuous.

3. LM7_PUSH E65.12 is then forced by uniqueness: the composed transporter Phi_F(A_G)A_F is the uniquely normalized frame of FG, and likewise for beta. Only after that does signed covariance give the multiplicativity of T and W. In B/N1, r-centralizers in the pure subgroup grow; composing selected frames can differ by such a centralizer element. The original proof gives no canonical rule eliminating it.

4. LM7_PUSH E65.14 normalizes the non-pure r-conjugator coset for an arbitrary multiplier. Its subsequent multiplication and transport laws E65.16--17 again use uniqueness. The new normalized automorphism of B/N1 is a genuine quotient automorphism, but that alone does not supply these original coherent frame laws or the original global B3 action used in E65.15.

5. The referee's Step2 explicitly closes existence of the original pure r-frame and confirms uniqueness in B. Step6 checks multiplication precisely through that uniqueness; Step8 repeats it for arbitrary multiplier cosets. Its arithmetic Step9 identifies actual Galois path cocycles with inverse frames through the same uniqueness. Arbitrary quotient frames are not thereby actual arithmetic path cocycles.

6. The referee's Step11 says the frames are determined by a particular finite G6 action in the original reduction. That is a DIFFERENT quotient. This audit does not substitute B/N1 for G6 or contradict that result.

## Full ambiguity witness, beyond a sign-choice shorthand

The exact central model proves that K=(N intersect Fprime)/N1 is a central pro-two kernel in E1prime->Cprime, where E1=F/N1 and C=q(F). The actual product decomposition of C allows elements supported solely at the prime3. Choose b in Z3, b congruent1 mod3, with b²=-2. The explicit matrices i3=[[0,1],[-1,0]] and j3=[[1,b],[b,-1]] have determinant1, square-I and anticommute. Their commutator is-I. Supporting them only at3 produces c_* in Cprime, equal-I at3 andI elsewhere; it is fixed by the actual cyclic action.

The central pro-two kernel has trivial H1 for C3, by the complete elementary coprime-action argument. Thus c_* has a rho-fixed lift h in E1prime. It satisfies q4(h)=I and q3(h)=-I. Both1 andh are pure r-frames for the IDENTITY automorphism of B1, and both have abelianization0. Keep beta=1, so rho_F=0 and V=I in the original E65.2.

For frame1, T=W=I. For frameh, W=I while T=q12(h)^{-1}=5I, which isI at4 and-I at3. Both obey the same original signed lift normalization. This is not the freedom to multiply a projective matrix by the other global lift. The original E65.3 rational line F3(1,-1) receives opposite scalars, so E65.4 yields0 and1 respectively. Purity, abelian normalization, finite covariance and the mod4 lift do not repair the nonuniqueness.

Any strengthened proposal must therefore retain and prove extra frame coherence or a separate well-defined action-image character. Conjugacy of alpha and c on B1 cannot by itself be fed into the original GT0 character-invariance theorem.

## Actual nonlifting obstruction

For any lift w in Fprime of h, w^{-1}rho(w) belongs to N1 and is a C3-cocycle. If it were a coboundary in N1, w could be corrected by an N1 element to a nontrivial rho-fixed element of Fprime, contradicting C_B(r) intersect F=1. Thus this class in H1(C3,N1) is nonbase. The same coprime-action theorem proves N1 is NOT pro-two. This is an actual failure of lifting the newly created quotient frame; it does not determine the original frame sign.

## Formal packaging and source status

The complete cohomology classification is proposed as A109, and the complete ambiguity/nonlifting proof as A110. Their ingredients are the previously fully reviewed A105 and checkpoint33 research, plus the exact central model/geometric stability being formalized in A106--A107. Original sources and every33 byte are unchanged. No new finite computation, census, private PDF or shared paper edit was performed for this audit.

Reread/save UTC: 2026-11-17T12:08:56.501976+00:00

Exact bound original sources:
- /workspace/scratch/a50d05093ca1/recovered_inputs32/background/expanded/LM7_PUSH_checkpoint_09/sections/E_genus_one_sewing_agent.tex; 267 lines; SHA256 6957b7565c585852ec94882e3558a738ba34678119b2f14a8fab7dea6ace8925.
- /workspace/scratch/a50d05093ca1/recovered_inputs32/background/expanded/LM7_PUSH_checkpoint_09/sections/E_cm_character_agent.tex; 327 lines; SHA256 45fb24828a71b3a2444f32b99625a594092732222065515f848bd49e022f15b9.
- /workspace/scratch/a50d05093ca1/recovered_inputs32/background/expanded/referee/REFEREE_B_E61_E65.md; 252 lines; SHA256 0faa565d68df0bdf0d1370dd090529375ccfeb51b22135102a7efab187c06581.
